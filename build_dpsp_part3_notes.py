# build_dpsp_part3_notes.py
# Generates production-ready bilingual TNPSC Group 1 notes for:
# "Directive Principles of State Policy – Part 3" (Articles 48–51, Full Summary, FR vs DPSP, Basic Structure)
# Target file: data/notes/polity/directive_principles_part_3.json

import json
import os

def create_dpsp_part3_notes():
    note_data = {
        "meta": {
            "topic_id": "polity_directive_principles_part_3",
            "repository_id": "polity_directive_principles",
            "display_title": "Directive Principles of State Policy – Part 3",
            "part": 3,
            "total_parts": 3,
            "subject": "polity",
            "chapter": "Directive Principles of State Policy",
            "language": "English + Tamil"
        },
        "metadata": {
            "version": "2.0",
            "status": "approved",
            "review_status": "gold_standard",
            "difficulty": "foundation",
            "estimated_study_time": {
                "reading": "35 min",
                "revision": "15 min",
                "total": "50 min"
            }
        },
        "keywords": [
            "Directive Principles of State Policy Part 3",
            "அரசு வழிகாட்டு நெறிமுறைகள் பகுதி 3",
            "Article 48 Agriculture Animal Husbandry Cattle Slaughter Prohibition",
            "உறுப்பு 48 விவசாயம் கால்நடை பராமரிப்பு பசு வதை தடை",
            "Article 48A Environment Forests Wildlife",
            "உறுப்பு 48A சுற்றுச்சூழல் காடுகள் வனவிலங்குகள்",
            "42nd Constitutional Amendment 1976",
            "42வது அரசியலமைப்பு திருத்தம் 1976",
            "Article 49 National Monuments Protection",
            "உறுப்பு 49 தேசிய நினைவிடங்கள் பாதுகாப்பு",
            "Article 50 Separation of Judiciary from Executive",
            "உறுப்பு 50 நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு",
            "Article 51 International Peace Security Arbitration",
            "உறுப்பு 51 சர்வதேச அமைதி பாதுகாப்பு நடுவர் மன்றம்",
            "Articles 36 to 51 Complete Article Map",
            "உறுப்புகள் 36 முதல் 51 முழுமையான வரைபடம்",
            "Fundamental Rights vs Directive Principles",
            "அடிப்படை உரிமைகள் vs வழிகாட்டு நெறிமுறைகள்",
            "Directive Principles vs Fundamental Duties",
            "வழிகாட்டு நெறிமுறைகள் vs அடிப்படைக் கடமைகள்",
            "Article 48A vs Article 51Ag",
            "உறுப்பு 48A vs உறுப்பு 51A g",
            "DPSP and Basic Structure Doctrine",
            "DPSP மற்றும் அடிப்படை அமைப்புக் கோட்பாடு",
            "Minerva Mills Kesavananda Bharati Champakam Dorairajan",
            "மினர்வா மில்ஸ் கேசவானந்த பாரதி செண்பகம் துரைராஜன் வழக்குகள்"
        ],
        "learning_outcomes": {
            "Understand": {
                "en": [
                    "Understand Article 48 (Scientific Agriculture, Animal Husbandry & Cattle Breed Preservation/Slaughter Prohibition).",
                    "Understand Article 48A (Environment, Forests, Wildlife added by 42nd Amendment 1976) and compare it with Article 51A(g).",
                    "Understand Article 49 (Protection of Monuments and Objects of National Importance) and Article 50 (Separation of Judiciary from Executive).",
                    "Understand Article 51 (Promotion of International Peace, Security, Treaty Respect & Arbitration).",
                    "Understand the complete Article Map for Articles 36 to 51 and the 3-fold conventional classification.",
                    "Understand the legal evolution of Fundamental Rights vs DPSP from Champakam Dorairajan (1951) to Minerva Mills (1980).",
                    "Understand DPSP's integration with Fundamental Duties (Part IV-A) and the Basic Structure of the Constitution."
                ],
                "ta": [
                    "உறுப்பு 48 (அறிவியல் விவசாயம், கால்நடை பராமரிப்பு & கால்நடை இனம் பாதுகாப்பு/வதை தடை) ஆகியவறைப் புரிந்து கொள்ளுதல்.",
                    "உறுப்பு 48A (சுற்றுச்சூழல், காடுகள், வனவிலங்குகள் 1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டது) என்பதைப் புரிந்து கொண்டு உறுப்பு 51A(g)-உடன் ஒப்பிடுதல்.",
                    "உறுப்பு 49 (தேசிய முக்கியத்துவம் வாய்ந்த நினைவிடங்கள் பாதுகாப்பு) மற்றும் உறுப்பு 50 (நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு) ஆகியவற்றைப் புரிந்து கொள்ளுதல்.",
                    "உறுப்பு 51 (சர்வதேச அமைதி, பாதுகாப்பு, ஒப்பந்த மரிப்பு & நடுவர் மன்றம் மேம்பாடு) ஆகியவற்றைப் புரிந்து கொள்ளுதல்.",
                    "உறுப்புகள் 36 முதல் 51 வரையிலான முழுமையான உறுப்பு வரைபடத்தையும் 3 வகை மரபுவழி வகைப்பாட்டையும் புரிந்து கொள்ளுதல்.",
                    "செண்பகம் துரைராஜன் (1951) முதல் மினர்வா மில்ஸ் (1980) வரை அடிப்படை உரிமைகள் vs DPSP சட்ட வளர்ச்சியைப் புரிந்து கொள்ளுதல்.",
                    "அடிப்படைக் கடமைகளுடனான (பகுதி IV-A) DPSP ஒருங்கிணைப்பையும் அரசியலமைப்பின் அடிப்படை அமைப்பையும் புரிந்து கொள்ளுதல்."
                ]
            },
            "Remember": {
                "en": [
                    "Remember that Article 48A was added by the 42nd Constitutional Amendment Act, 1976.",
                    "Remember that Article 48A is a State Directive (Part IV), while Article 51A(g) is a Citizen Duty (Part IV-A).",
                    "Remember that Article 50 directs separation of Judiciary from Executive in PUBLIC SERVICES of the State.",
                    "Remember that Article 51 deals with International Peace, Law & Arbitration (India's foreign policy DPSP anchor).",
                    "Remember that Minerva Mills (1980) held that the BALANCE between Part III and Part IV is part of Basic Structure.",
                    "Remember that the DPSP classification into Socialist, Gandhian, and Liberal categories is CONVENTIONAL ACADEMIC, not written in Constitution text."
                ],
                "ta": [
                    "உறுப்பு 48A 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது என்பதை நினைவில் கொள்ளுதல்.",
                    "உறுப்பு 48A என்பது அரசு வழிகாட்டுதல் (பகுதி IV), உறுப்பு 51A(g) என்பது குடிமகன் கடமை (பகுதி IV-A) என்பதை நினைவில் கொள்ளுதல்.",
                    "உறுப்பு 50 மாநிலத்தின் பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க வழிகாட்டுகிறது என்பதை நினைவில் கொள்ளுதல்.",
                    "உறுப்பு 51 சர்வதேச அமைதி, சட்டம் & நடுவர் மன்றம் பற்றியது என்பதை நினைவில் கொள்ளுதல் (வெளியுறவுக் கொள்கை DPSP நங்கூரம்).",
                    "பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலையே அடிப்படை அமைப்பின் பகுதி என மினர்வா மில்ஸ் (1980) தீர்ப்பளித்தது என்பதை நினைவில் கொள்ளுதல்.",
                    "சமதர்ம, காந்திய, தாராளமய DPSP வகைப்பாடு மரபுவழி கல்வியின் பிரிவே தவிர அரசியலமைப்பில் எழுதப்படவில்லை என்பதை நினைவில் கொள்ளுதல்."
                ]
            },
            "Analyze": {
                "en": [
                    "Analyze the distinction between Article 48 (Agriculture/Cattle Prohibition - Gandhian) and Article 48A (Environment/Wildlife - Liberal-Intellectual).",
                    "Analyze the constitutional difference between Article 49 (Monuments Protection DPSP) and Articles 29-30 (Minority Cultural Rights FRs).",
                    "Analyze Article 50 separation of powers in Indian context vs rigid separation of powers in US Constitution.",
                    "Analyze the 4-phase evolution of FR vs DPSP hierarchy: Champakam (1951 FR superior) -> Re Kerala Education (1958 Harmonious) -> 25th CAA 1971 (31C 39b/c priority) -> Minerva Mills (1980 Balance is Basic Structure).",
                    "Analyze the complementary synergy between DPSP (Part IV State goals) and Fundamental Duties (Part IV-A Citizen duties)."
                ],
                "ta": [
                    "உறுப்பு 48 (விவசாயம்/கால்நடை வதை தடை - காந்தியம்) மற்றும் உறுப்பு 48A (சுற்றுச்சூழல்/வனவிலங்கு - தாராளமயம்) இடையேயான வேறுபாட்டை பகுப்பாய்வு செய்தல்.",
                    "உறுப்பு 49 (நினைவிடங்கள் பாதுகாப்பு DPSP) மற்றும் உறுப்புகள் 29-30 (சிறுபான்மையினர் பண்பாட்டு உரிமைகள் FR) இடையேயான வேறுபாட்டை பகுப்பாய்வு செய்தல்.",
                    "அமெரிக்க அரசியலமைப்பின் கடுமையான அதிகாரப் பிரிப்பு vs இந்தியச் சூழலில் உறுப்பு 50 அதிகாரப் பிரிப்பை பகுப்பாய்வு செய்தல்.",
                    "FR vs DPSP படிநிலையின் 4 கட்ட வளர்ச்சியை பகுப்பாய்வு செய்தல்: செண்பகம் (1951) -> கேரளா கல்வி (1958) -> 25வது திருத்தம் 1971 -> மினர்வா மில்ஸ் (1980).",
                    "DPSP (பகுதி IV அரசு இலக்குகள்) மற்றும் அடிப்படைக் கடமைகள் (பகுதி IV-A குடிமகன் கடமைகள்) இடையேயான நிரப்பு தொடர்பைப் பகுப்பாய்வு செய்தல்."
                ]
            },
            "Apply": {
                "en": [
                    "Apply TNPSC trap points to distinguish Article 48A (State Environment Duty) from Article 51A(g) (Citizen Environment Duty).",
                    "Avoid confusing Article 50 (Judiciary/Executive Separation in public service) with full rigid separation of powers.",
                    "Correctly identify all 16 Articles from 36 to 51 in statement-based and chronology MCQs."
                ],
                "ta": [
                    "உறுப்பு 48A (அரசு சுற்றுச்சூழல் கடமை) மற்றும் உறுப்பு 51A(g) (குடிமகன் சுற்றுச்சூழல் கடமை) ஆகியவற்றை வேறுபடுத்த டிஎன்பிஎஸ்சி பொறி புள்ளிகளைப் பயன்படுத்துதல்.",
                    "உறுப்பு 50-ஐ (பொது சேவையில் நீதித்துறை/நிர்வாகப் பிரிப்பு) முழுமையான கடுமையான அதிகாரப் பிரிப்புடன் குழப்பிக் கொள்ளாமல் இருத்தல்.",
                    "கூற்று மற்றும் காலவரிசை வினாக்களில் உறுப்புகள் 36 முதல் 51 வரையிலான 16 உறுப்புகளையும் சரியாக அடையாளம் காணுதல்."
                ]
            }
        },
        "subject": "Polity",
        "topic": "Directive Principles of State Policy – Part 3",
        "language": "bilingual",
        "ui_type": "polity",
        "sections": [
            {
                "id": "sec_article_48",
                "title_en": "1. Article 48: Organisation of Agriculture and Animal Husbandry",
                "title_ta": "1. உறுப்பு 48: விவசாயம் மற்றும் கால்நடை பராமரிப்பை அமைத்தல்",
                "type": "standard_topic"
            },
            {
                "id": "sec_article_48a",
                "title_en": "2. Article 48A: Protection and Improvement of Environment, Forests & Wildlife",
                "title_ta": "2. உறுப்பு 48A: சுற்றுச்சூழல், காடுகள் மற்றும் வனவிலங்குகள் பாதுகாப்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_article_49",
                "title_en": "3. Article 49: Protection of Monuments and Places/Objects of National Importance",
                "title_ta": "3. உறுப்பு 49: தேசிய முக்கியத்துவம் வாய்ந்த நினைவிடங்கள் மற்றும் இடங்கள் பாதுகாப்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_article_50",
                "title_en": "4. Article 50: Separation of Judiciary from Executive",
                "title_ta": "4. உறுப்பு 50: நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரித்தல்",
                "type": "standard_topic"
            },
            {
                "id": "sec_article_51",
                "title_en": "5. Article 51: Promotion of International Peace and Security (Foreign Policy DPSP Anchor)",
                "title_ta": "5. உறுப்பு 51: சர்வதேச அமைதி மற்றும் பாதுகாப்பை மேம்படுத்துதல் (வெளியுறவுக் கொள்கை DPSP)",
                "type": "standard_topic"
            },
            {
                "id": "sec_complete_classification",
                "title_en": "6. Complete DPSP Classification Revision (Socialist, Gandhian & Liberal)",
                "title_ta": "6. DPSP முழுமையான தத்துவார்த்த வகைப்பாட்டுத் திருப்புதல் (சமதர்ம, காந்திய & தாராளமய)",
                "type": "standard_topic"
            },
            {
                "id": "sec_article_map_36_51",
                "title_en": "7. Complete Articles 36 to 51 High-Yield Constitutional Map",
                "title_ta": "7. உறுப்புகள் 36 முதல் 51 வரையிலான முழுமையான அரசியலமைப்பு வரைபடம்",
                "type": "standard_topic"
            },
            {
                "id": "sec_fr_vs_dpsp",
                "title_en": "8. Fundamental Rights (Part III) vs Directive Principles (Part IV) & Judicial Evolution",
                "title_ta": "8. அடிப்படை உரிமைகள் (பகுதி III) vs வழிகாட்டு நெறிமுறைகள் (பகுதி IV) & நீதித்துறை வளர்ச்சி",
                "type": "standard_topic"
            },
            {
                "id": "sec_dpsp_vs_fd",
                "title_en": "9. DPSP (Part IV) vs Fundamental Duties (Part IV-A) & Basic Structure Integration",
                "title_ta": "9. DPSP (பகுதி IV) vs அடிப்படைக் கடமைகள் (பகுதி IV-A) & அடிப்படை அமைப்பு ஒருங்கிணைப்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_landmark_cases_amendments",
                "title_en": "10. Landmark Supreme Court Rulings & Constitutional Amendments Summary",
                "title_ta": "10. முக்கிய உச்ச நீதிமன்ற தீர்ப்புகள் & அரசியலமைப்பு திருத்தங்களின் தொகுப்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_traps_revision",
                "title_en": "11. TNPSC Traps, Full DPSP Comparison Framework & 2-Minute Revision",
                "title_ta": "11. டிஎன்பிஎஸ்சி பொறிகள், முழு DPSP ஒப்பீட்டு அமைப்பும் 2-நிமிட திருப்புதலும்",
                "type": "standard_topic"
            }
        ],
        "content": {
            "definition": {
                "en": "Part 3 of the Directive Principles of State Policy series completes the analysis of Part IV (Articles 48 to 51), covering scientific agriculture & cattle breed preservation (Article 48), environment & wildlife protection (Article 48A), national monuments protection (Article 49), separation of judiciary from executive (Article 50), and international peace & security (Article 51). It also provides a master synthesized analysis of Articles 36–51, FR vs DPSP evolution, DPSP vs Fundamental Duties, landmark Supreme Court cases, and Basic Structure integration.",
                "ta": "அரசு வழிகாட்டு நெறிமுறைகள் தொடரின் பகுதி 3, பகுதி IV (உறுப்புகள் 48 முதல் 51 வரை) பற்றிய ஆய்வை நிறைவு செய்கிறது. இது அறிவியல் விவசாயம் & கால்நடை இனம் பாதுகாப்பு/வதை தடை (உறுப்பு 48), சுற்றுச்சூழல் & வனவிலங்கு பாதுகாப்பு (உறுப்பு 48A), தேசிய நினைவிடங்கள் பாதுகாப்பு (உறுப்பு 49), நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு (உறுப்பு 50), மற்றும் சர்வதேச அமைதி & பாதுகாப்பு (உறுப்பு 51) ஆகியவற்றை உள்ளடக்கியுள்ளது. மேலும் இது உறுப்புகள் 36–51 இன் முழுமையான வரைபடம், FR vs DPSP வளர்ச்சி, DPSP vs அடிப்படைக் கடமைகள், முக்கிய உச்ச நீதிமன்ற தீர்ப்புகள் மற்றும் அடிப்படை அமைப்பு ஒருங்கிணைப்பு ஆகியற்றின் தொகுக்கப்பட்ட ஆய்வை வழங்குகிறது."
            },
            "introduction": {
                "en": "Part 3 concludes the DPSP chapter with comprehensive coverage of Articles 48, 48A, 49, 50, and 51, followed by a complete 3-fold classification revision, a 16-article master map (36–51), the historical evolution of FR vs DPSP from Champakam Dorairajan (1951) to Minerva Mills (1980), DPSP vs Fundamental Duties, 10 mandatory bilingual comparison tables, mind map, and TNPSC trap points.",
                "ta": "பகுதி 3 உறுப்புகள் 48, 48A, 49, 50, மற்றும் 51 ஆகியவற்றை விரிவாக உள்ளடக்கி DPSP பாடத்தை நிறைவு செய்கிறது. அதனைத் தொடர்ந்து முழுமையான 3 வகைப்பாடு திருப்புதல், 16-உறுப்புகள் முதன்மை வரைபடம் (36–51), செண்பகம் துரைராஜன் (1951) முதல் மினர்வா மில்ஸ் (1980) வரையிலான FR vs DPSP வரலாற்று வளர்ச்சி, DPSP vs அடிப்படைக் கடமைகள், 10 கட்டாய இருமொழி ஒப்பீட்டு அட்டவணைகள், மன வரைபடம் மற்றும் டிஎன்பிஎஸ்சி பொறி புள்ளிகள் ஆகியவற்றை வழங்குகிறது."
            },
            "sec_article_48": [
                {
                    "title": "1. Scientific Agriculture & Animal Husbandry (அறிவியல் விவசாயமும் கால்நடை பராமரிப்பும்)",
                    "points": {
                        "en": [
                            "Constitutional Mandate: Article 48 directs the State to endeavor to organize agriculture and animal husbandry on modern and scientific lines and shall, in particular, take steps for preserving and improving the breeds, and prohibiting the slaughter of cows and calves and other milch and draught cattle.",
                            "Dual Objective:\n1. Scientific Agriculture & Animal Husbandry: Modernising farming, green revolution, soil health cards, cross-breeding, veterinary infrastructure.\n2. Preservation of Cattle Breeds & Slaughter Prohibition: Preserving indigenous breeds (e.g. Kangayam, Umblachery, Ongole, Gir) and prohibiting slaughter of cows, calves, and other milch (பால் தரும்) and draught (பாரம் இழுக்கும்) cattle.",
                            "Ideology: Conventional Gandhian Principle (cattle protection) combined with Liberal-Scientific objective (modern agriculture).",
                            "Judicial Landmark – Hanif Quareshi Case (1958) & State of Gujarat v. Mirzapur Moti Kureshi (2005):\n- In Hanif Quareshi (1958), SC held total ban on slaughter of ALL cattle (even old & unserviceable) was unreasonable restriction on butcher trade under Art 19(1)(g).\n- In Mirzapur Kureshi (2005 7-Judge Bench), SC OVERRULED earlier stance and UPHELD total ban on slaughter of cow progeny (including old bulls/bullocks), holding that draught cattle contribute to agriculture, organic dung manure, and rural economy even in old age!",
                            "TNPSC Trap: Article 48 text does NOT prohibit consumption of beef explicitly; it commands the STATE to organize agriculture scientifically and prohibit slaughter of cows, calves, milch & draught cattle."
                        ],
                        "ta": [
                            "அரசியலமைப்பு கட்டளை: உறுப்பு 48 நவீன மற்றும் அறிவியல் முறைகளில் விவசாயம் மற்றும் கால்நடை பராமரிப்பை அமைக்க அரசு முயல வேண்டும், மேலும் குறிப்பாக இனங்களைப் பாதுகாப்பதற்கும் மேம்படுத்துவதற்கும் பசுக்கள், கன்றுகள் மற்றும் பிற பால் தரும் மற்றும் பாரம் இழுக்கும் கால்நடைகளைக் கொல்வதைத் தடை செய்வதற்கும் நடவடிக்கைகள் எடுக்க வேண்டும் எனக் கட்டளையிடுகிறது.",
                            "இரட்டை நோக்கம்:\n1. அறிவியல் விவசாயம் & கால்நடை பராமரிப்பு: விவசாயத்தை நவீனமயமாக்கல், பசுமைப் புரட்சி, மண் வள அட்டைகள், கலப்பினப் பெருக்கம், கால்நடை பராமரிப்பு உள்கட்டமைப்பு.\n2. கால்நடை இனப் பாதுகாப்பு & வதை தடை: நாட்டுப்புற இனங்களைப் பாதுகாத்தல் (எ.கா. காங்கேயம், உம்பளச்சேரி, ஓங்கோல், கிர்) மற்றும் பசுக்கள், கன்றுகள், பால் தரும் மற்றும் பாரம் இழுக்கும் கால்நடைகளை வதை செய்வதைத் தடுத்தல்.",
                            "தத்துவம்: மரபுவழி காந்தியக் கோட்பாடு (கால்நடை பாதுகாப்பு) மற்றும் தாராளமய-அறிவியல் நோக்கம் (நவீன விவசாயம்).",
                            "முக்கிய நீதித்துறைத் தீர்ப்பு – ஹனிஃப் குரேஷி வழக்கு (1958) & குஜராத் அரசு எதிர் மிர்சாபூர் மோதி குரேஷி (2005):\n- ஹனிஃப் குரேஷி வழக்கில் (1958), அனைத்துக் கால்நடைகளையும் (வயதானவை உட்பட) முழுமையாக வதை செய்ய தடை விதிப்பது உறுப்பு 19(1)(g)-ன் கீழ் இறைச்சி வியாபாரிகள் மீதான நியாயமற்ற கட்டுப்பாடு என SC தீர்ப்பளித்தது.\n- மிர்சாபூர் குரேஷி வழக்கில் (2005 7-நீதிபதிகள் அமர்வு), SC முந்தைய நிலையை மாற்றி பசு மற்றும் அதன் சந்ததிகளை (வயதான எருதுகள் உட்பட) முழுமையாக வதை செய்யத் தடை விதிப்பதை உறுதி செய்தது. வயதான காலத்திலும் பாரம் இழுக்கும் கால்நடைகள் விவசாயம், இயற்கை எரு உரம் மற்றும் கிராமப் பொருளாதாரத்திற்குப் பங்காற்றுகின்றன எனத் தீர்ப்பளித்தது!",
                            "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 48 உரை மாட்டிறைச்சி உண்பதை வெளிப்படையாகத் தடை செய்யவில்லை; விவசாயத்தை அறிவியல் ரீதியாக அமைக்கவும் பசுக்கள், கன்றுகள், பால் தரும் மற்றும் பாரம் இழுக்கும் கால்நடைகளை வதை செய்வதைத் தடுக்கவும் அரசுக்கு ஆணையிடுகிறது."
                        ]
                    }
                }
            ],
            "sec_article_48a": [
                {
                    "title": "1. Protection of Environment, Forests & Wildlife (சுற்றுச்சூழல், காடுகள் & வனவிலங்குகள் பாதுகாப்பு)",
                    "points": {
                        "en": [
                            "Constitutional Mandate: Added by the 42nd Constitutional Amendment Act, 1976. Article 48A states: 'The State shall endeavor to protect and improve the environment and to safeguard the forests and wild life of the country.'",
                            "Ideology: Liberal-Intellectual Principle.",
                            "Interplay between Article 48A and Article 51A(g):\n- Article 48A (Part IV DPSP): Imposes a positive constitutional duty on the STATE to protect and improve environment, forests, and wildlife.\n- Article 51A(g) (Part IV-A Fundamental Duty): Imposes a fundamental duty on EVERY CITIZEN of India to protect and improve the natural environment including forests, lakes, rivers and wildlife, and to have compassion for living creatures.",
                            "Judicial Integration with Article 21:\n- In M.C. Mehta cases (Ganga Pollution, Taj Trapezium, Vehicular Pollution), SC held that Article 48A (State duty) and Article 51A(g) (Citizen duty) read together with Article 21 make the 'Right to Clean Environment and Pollution-Free Water/Air' a justiciable Fundamental Right under Article 21!",
                            "Key Enacting Statutes: Wildlife Protection Act 1972, Water Act 1974, Forest Conservation Act 1980, Air Act 1981, Environment Protection Act 1986, National Green Tribunal (NGT) Act 2010.",
                            "TNPSC Trap: Article 48A is a DPSP added by 42nd Amendment 1976 (State duty). Do not confuse it with Article 51A(g) which is a Fundamental Duty of citizens!"
                        ],
                        "ta": [
                            "அரசியலமைப்பு கட்டளை: 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது. உறுப்பு 48A கூறுகிறது: 'நாட்டின் சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாக்கவும் அரசு முயல வேண்டும்.'",
                            "தத்துவம்: தாராளமய-அறிவுசார்க் கோட்பாடு.",
                            "உறுப்பு 48A மற்றும் உறுப்பு 51A(g) இடையேயான தொடர்பு:\n- உறுப்பு 48A (பகுதி IV DPSP): சுற்றுச்சூழல், காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாக்கவும் மேம்படுத்தவும் அரசு மீது ஒரு நேர்மறை அரசியலமைப்பு கடமையை விதிக்கிறது.\n- உறுப்பு 51A(g) (பகுதி IV-A அடிப்படைக் கடமை): காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகள் உள்ளிட்ட இயற்கைச் சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும், உயிரினங்கள் மீது கருணை காட்டவும் இந்தியாவின் ஒவ்வொரு குடிமகனுக்கும் அடிப்படைக் கடமையை விதிக்கிறது.",
                            "உறுப்பு 21-உடனான நீதித்துறை ஒருங்கிணைப்பு:\n- எம்.சி. மேத்தா வழக்குகளில் (கங்கை மாசுபாடு, தாஜ் மஹால் பகுதி, வாகன மாசுபாடு), உச்ச நீதிமன்றம் உறுப்பு 48A (அரசு கடமை) மற்றும் உறுப்பு 51A(g) (குடிமகன் கடமை) ஆகியவற்றை உறுப்பு 21-உடன் இணைந்து வாசித்து 'தூய்மையான சுற்றுச்சூழல் மற்றும் மாசுபாடற்ற நீர்/காற்று உரிமை' என்பது உறுப்பு 21-ன் கீழ் ஒரு அமல்படுத்தக்கூடிய அடிப்படை உரிமை எனத் தீர்ப்பளித்தது!",
                            "முக்கிய இயற்றப்பட்ட சட்டங்கள்: வனவிலங்கு பாதுகாப்புச் சட்டம் 1972, நீர் சட்டம் 1974, வனப் பாதுகாப்புச் சட்டம் 1980, காற்று சட்டம் 1981, சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் 1986, தேசிய பசுமை தீர்ப்பாய (NGT) சட்டம் 2010.",
                            "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 48A என்பது 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்ட DPSP (அரசு கடமை). அதை குடிமக்களின் அடிப்படைக் கடமையான உறுப்பு 51A(g)-உடன் குழப்பிக் கொள்ள வேண்டாம்!"
                        ]
                    }
                }
            ],
            "sec_article_49": [
                {
                    "title": "1. Protection of Monuments & Objects of National Importance (தேசிய நினைவிடங்கள் பாதுகாப்பு)",
                    "points": {
                        "en": [
                            "Constitutional Mandate: Article 49 directs the State to protect every monument or place or object of artistic or historic interest, declared by or under law made by Parliament to be of national importance, from spoliation, disfigurement, destruction, removal, disposal or export, as the case may be.",
                            "Ideology: Liberal-Intellectual Principle.",
                            "Distinction between Article 49 and Articles 29–30:\n- Article 49 is a DPSP directing the State to protect MONUMENTS AND HISTORICAL OBJECTS of national importance across India.\n- Articles 29 and 30 are JUSTICIABLE Fundamental Rights under Part III protecting the language, script, culture, and educational institutions of MINORITIES.\n- Article 49 focuses on physical heritage/monuments; Articles 29-30 focus on minority cultural identity and institutions.",
                            "Key Enacting Statute & Authority: Ancient Monuments and Archaeological Sites and Remains (AMASR) Act, 1958 and Archaeological Survey of India (ASI 1861).",
                            "TNPSC Trap: Article 49 applies ONLY to monuments/places declared by PARLIAMENT by law to be of 'national importance'."
                        ],
                        "ta": [
                            "அரசியலமைப்பு கட்டளை: உறுப்பு 49 கலை அல்லது வரலாற்று முக்கியத்துவம் வாய்ந்த, நாடாளுமன்றச் சட்டத்தால் அல்லது அதன் கீழ் தேசிய முக்கியத்துவம் வாய்ந்ததாக அறிவிக்கப்பட்ட ஒவ்வொரு நினைவிடத்தையும் அல்லது இடத்தையும் அல்லது பொருளையும் சேதப்படுத்துதல், சீர்குலைத்தல், அழித்தல், அகற்றுதல், விற்பனை செய்தல் அல்லது ஏற்றுமதி செய்வதிலிருந்து பாதுகாப்பது அரசின் கடமையாகும் எனக் கட்டளையிடுகிறது.",
                            "தத்துவம்: தாராளமய-அறிவுசார்க் கோட்பாடு.",
                            "உறுப்பு 49 மற்றும் உறுப்புகள் 29–30 இடையேயான வேறுபாடு:\n- உறுப்பு 49 என்பது இந்தியா முழுவதும் தேசிய முக்கியத்துவம் வாய்ந்த நினைவிடங்கள் மற்றும் வரலாற்றுப் பொருட்களைப் பாதுகாக்க அரசுக்கு ஆணையிடும் ஒரு DPSP ஆகும்.\n- உறுப்புகள் 29 மற்றும் 30 என்பவை சிறுபான்மையினரின் மொழி, எழுத்து, பண்பாடு மற்றும் கல்வி நிறுவனங்களைப் பாதுகாக்கும் பகுதி III-ன் கீழ் உள்ள அமல்படுத்தக்கூடிய அடிப்படை உரிமைகள் ஆகும்.\n- உறுப்பு 49 பௌதிக பாரம்பரியம்/நினைவிடங்கள் மீது கவனம் செலுத்துகிறது; உறுப்புகள் 29-30 சிறுபான்மையினரின் பண்பாட்டு அடையாளம் மீது கவனம் செலுத்துகின்றன.",
                            "முக்கிய இயற்றப்பட்ட சட்டம் & முகமை: பழங்கால நினைவிடங்கள் மற்றும் தொல்லியல் இடங்கள் மற்றும் எஞ்சியவை (AMASR) சட்டம் 1958 மற்றும் இந்தியத் தொல்லியல் துறை (ASI 1861).",
                            "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 49 நாடாளுமன்றச் சட்டத்தால் 'தேசிய முக்கியத்துவம் வாய்ந்தது' என அறிவிக்கப்பட்ட நினைவிடங்கள்/இடங்களுக்கு மட்டுமே பொருந்தும்."
                        ]
                    }
                }
            ],
            "sec_article_50": [
                {
                    "title": "1. Separation of Judiciary from Executive (நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு)",
                    "points": {
                        "en": [
                            "Constitutional Mandate: Article 50 directs: 'The State shall take steps to separate the judiciary from the executive in the public services of the State.'",
                            "Ideology: Liberal-Intellectual Principle.",
                            "Constitutional Objective: To secure Judicial Independence and eliminate executive influence over judicial adjudication.",
                            "Historical & Statutory Implementation:\n- Under colonial rule, District Collectors/Magistrates exercised both Executive powers (law & order/revenue) and Judicial powers (trying criminal cases).\n- Article 50 was implemented statutorily by Parliament enacting the Code of Criminal Procedure (CrPC), 1973 (effective April 1, 1974), which separated Judicial Magistrates (under High Court control) from Executive Magistrates (under State Govt control).\n- Judicial officers (Judicial Magistrates/District Judges) are placed under the control of the concerned High Court (Articles 233 to 237).",
                            "Clarification on Separation of Powers Doctrine:\n- Article 50 mandates separation of Judiciary from Executive specifically in public services.\n- The Constitution of India does NOT follow a rigid, absolute separation of powers like the US Constitution. Instead, India follows a system of checks and balances where Executive is part of Legislature (Parliamentary democracy).",
                            "TNPSC Trap: Article 50 specifically mentions separating judiciary from executive 'in the public services of the State'. CrPC 1973 fulfilled this constitutional mandate."
                        ],
                        "ta": [
                            "அரசியலமைப்பு கட்டளை: உறுப்பு 50 வழிகாட்டுகிறது: 'மாநிலத்தின் பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க அரசு நடவடிக்கைகள் எடுக்க வேண்டும்.'",
                            "தத்துவம்: தாராளமய-அறிவுசார்க் கோட்பாடு.",
                            "அரசியலமைப்பு நோக்கம்: நீதித்துறை சுயசார்பைப் பாதுகாப்பது மற்றும் நீதித்துறை தீர்ப்பளிப்பின் மீது நிர்வாகத் தலையீட்டை ஒழிப்பது.",
                            "வரலாற்று & சட்டப்பூர்வ அமலாக்கம்:\n- காலனித்துவ ஆட்சியின் கீழ், மாவட்ட ஆட்சியர்கள்/மேஜிஸ்திரேட்டுகள் நிர்வாக அதிகாரங்கள் (சட்டம் ஒழுங்கு/வருவாய்) மற்றும் நீதித்துறை அதிகாரங்கள் (குற்றவியல் வழக்குகளை விசாரித்தல்) இரண்டையும் பயன்படுத்தினர்.\n- 1973 குற்றவியல் நடைமுறைச் சட்டத்தை (CrPC 1973 - ஏப்ரல் 1, 1974 முதல் அமுல்) இயற்றுவதன் மூலம் உறுப்பு 50 சட்டப்பூர்வமாக செயல்படுத்தப்பட்டது, இது நீதித்துறை மேஜிஸ்திரேட்டுகளை (உயர் நீதிமன்ற கட்டுப்பாட்டின் கீழ்) நிர்வாக மேஜிஸ்திரேட்டுகளிடமிருந்து (மாநில அரசு கட்டுப்பாட்டின் கீழ்) பிரித்தது.\n- நீதித்துறை அதிகாரிகள் (நீதித்துறை மேஜிஸ்திரேட்டுகள்/மாவட்ட நீதிபதிகள்) தொடர்புடைய உயர் நீதிமன்றத்தின் கட்டுப்பாட்டின் கீழ் வைக்கப்பட்டுள்ளனர் (உறுப்புகள் 233 முதல் 237 வரை).",
                            "அதிகாரப் பிரிப்புக் கோட்பாட்டின் தெளிவுரையாக்கம்:\n- உறுப்பு 50 பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிப்பதை வெளிப்படையாகக் கட்டளையிடுகிறது.\n- இந்திய அரசியலமைப்பு அமெரிக்க அரசியலமைப்பு போன்ற கடுமையான, முற்றுமுழுதான அதிகாரப் பிரிப்பைப் பின்பற்றவில்லை. மாறாக, இந்தியா கட்டுப்பாடுகள் மற்றும் சமநிலைகள் அமைப்பைப் பின்பற்றுகிறது, இதில் நிர்வாகத்துறை சட்டமன்றத்தின் பகுதியாகும் (நாடாளுமன்ற ஜனநாயகம்).",
                            "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 50 'மாநிலத்தின் பொது சேவைகளில்' நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிப்பதைக் குறிப்பிட்டுச் சொல்கிறது. CrPC 1973 இந்த அரசியலமைப்பு கட்டளையை நிறைவேற்றியது."
                        ]
                    }
                }
            ],
            "sec_article_51": [
                {
                    "title": "1. Promotion of International Peace & Security (சர்வதேச அமைதியும் பாதுகாப்பும்)",
                    "points": {
                        "en": [
                            "Constitutional Mandate: Article 51 directs that the State shall endeavor to:\n(a) Promote international peace and security;\n(b) Maintain just and honourable relations between nations;\n(c) Foster respect for international law and treaty obligations in the dealings of organized peoples with one another; and\n(d) Encourage settlement of international disputes by arbitration.",
                            "Ideology: Liberal-Intellectual Principle.",
                            "Constitutional Status as Foreign Policy Anchor: Article 51 is the primary constitutional anchor for India's Foreign Policy (Panchsheel, Non-Aligned Movement, UN Peacekeeping, International Law compliance).",
                            "Distinctions:\n- Article 51 is a Part IV DPSP guiding STATE FOREIGN POLICY.\n- Article 51A (Part IV-A) contains FUNDAMENTAL DUTIES OF CITIZENS (added by 42nd Amendment 1976).\n- Treaty Enforcement: Under Article 253, Parliament has exclusive power to make laws for giving effect to international agreements.",
                            "TNPSC Trap: Article 51 is the LAST article of Part IV (DPSP). Article 51A is Part IV-A (Fundamental Duties). Do not confuse 51 (State Foreign Policy DPSP) with 51A (Citizen Fundamental Duties)!"
                        ],
                        "ta": [
                            "அரசியலமைப்பு கட்டளை: உறுப்பு 51 அரசு பின்வருவனவற்றிற்கு முயல வேண்டும் எனக் கட்டளையிடுகிறது:\n(a) சர்வதேச அமைதி மற்றும் பாதுகாப்பை மேம்படுத்துதல்;\n(b) நாடுகளிடையே நியாயமான மற்றும் கெளரவமான உறவுகளைப் பேணுதல்;\n(c) ஒழுங்கமைக்கப்பட்ட மக்களின் பரஸ்பர தொடர்புகளில் சர்வதேச சட்டம் மற்றும் ஒப்பந்தக் கடமைகளுக்கு மரியாதையை வளர்த்தல்; மற்றும்\n(d) சர்வதேச தகராறுகளை நடுவர் மன்றம் மூலம் அமைதியான முறையில் தீர்ப்பதை ஊக்குவித்தல்.",
                            "தத்துவம்: தாராளமய-அறிவுசார்க் கோட்பாடு.",
                            "வெளியுறவுக் கொள்கை நங்கூரமாக அரசியலமைப்பு அந்தஸ்து: உறுப்பு 51 இந்தியாவின் வெளியுறவுக் கொள்கைக்கான (பஞ்சசீலம், அணிசேரா இயக்கம், ஐ.நா அமைதிப்படை, சர்வதேச சட்ட இணக்கம்) முதன்மை அரசியலமைப்பு நங்கூரமாகும்.",
                            "வேறுபாடுகள்:\n- உறுப்பு 51 என்பது அரசின் வெளியுறவுக் கொள்கையை வழிகாட்டும் பகுதி IV DPSP ஆகும்.\n- உறுப்பு 51A (பகுதி IV-A) குடிமக்களின் அடிப்படைக் கடமைகளைக் கொண்டுள்ளது (42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது).\n- ஒப்பந்த அமலாக்கம்: உறுப்பு 253-ன் கீழ், சர்வதேச ஒப்பந்தங்களுக்குச் செயலாக்கம் அளிக்கச் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரம் உண்டு.",
                            "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 51 என்பது பகுதி IV-ன் (DPSP) கடைசி உறுப்பாகும். உறுப்பு 51A என்பது பகுதி IV-A (அடிப்படைக் கடமைகள்). 51-ஐ (அரசு வெளியுறவுக் கொள்கை DPSP) 51A-உடன் (குடிமகன் அடிப்படைக் கடமைகள்) குழப்பிக் கொள்ள வேண்டாம்!"
                        ]
                    }
                }
            ],
            "sec_complete_classification": [
                {
                    "title": "1. Complete Master Classification of Articles 36 to 51 (முழுமையான 3 வகைப்பாடு)",
                    "points": {
                        "en": [
                            "MANDATORY DISCLAIMER: The 3-fold classification into Socialist, Gandhian, and Liberal-Intellectual categories is a CONVENTIONAL ACADEMIC CLASSIFICATION used by constitutional scholars. It is NOT explicitly provided in the Constitution text.",
                            "1. Socialist Principles (சமதர்மக் கோட்பாடுகள்):\n- Directives aiming at socio-economic justice, welfare state, labor protection, and income equality.\n- Articles: 38 (Social order & minimising inequalities), 39 (Livelihood, resources, wealth, equal pay, worker/child health), 39A (Free legal aid), 41 (Work, education, public assistance), 42 (Humane work conditions & maternity relief), 43 (Living wage & leisure), 43A (Workers' participation in management), 47 (Raising nutrition & public health).\n\n2. Gandhian Principles (காந்தியக் கோட்பாடுகள்):\n- Directives embodying Mahatma Gandhi's Gram Swaraj, village upliftment, cottage industry, prohibition, and cattle welfare.\n- Articles: 40 (Village Panchayats), 43 (Cottage industries), 43B (Co-operative societies - 97th CAA), 46 (Educational/economic interests of SC/ST/weaker sections), 47 (Prohibition of intoxicating drinks), 48 (Prohibition of slaughter of cows/calves/milch/draught cattle).\n\n3. Liberal-Intellectual Principles (தாராளமய-அறிவுசார்க் கோட்பாடுகள்):\n- Directives promoting liberal ideology, uniform laws, scientific temper, environment, monuments, judicial independence, and international peace.\n- Articles: 44 (Uniform Civil Code), 45 (Early childhood care below 6 yrs), 48 (Scientific agriculture/animal husbandry), 48A (Environment, forests & wildlife - 42nd CAA), 49 (National monuments protection), 50 (Separation of judiciary from executive), 51 (International peace, security & arbitration)."
                        ],
                        "ta": [
                            "கட்டாய எச்சரிக்கை: சமதர்ம, காந்திய மற்றும் தாராளமய-அறிவுசார் பிரிவுகளாகப் பிரிப்பது அரசியலமைப்பு அறிஞர்களால் பயன்படுத்தப்படும் ஒரு மரபுவழி கல்வி வகைபாடே தவிர, அரசியலமைப்பு உரையில் வெளிப்படையாக வழங்கப்படவில்லை.",
                            "1. சமதர்மக் கோட்பாடுகள்:\n- சமூக-பொருளாதார நீதி, நல அரசு, தொழிலாளர் பாதுகாப்பு மற்றும் வருமான சமத்துவத்தை நோக்கமாகக் கொண்ட வழிகாட்டுதல்கள்.\n- உறுப்புகள்: 38 (சமூக ஒழுங்கு & சமத்துவமின்மையைக் குறைத்தல்), 39 (வாழ்வாதாரம், வளங்கள், செல்வம், சம ஊதியம், தொழிலாளர்/குழந்தை சுகாதாரம்), 39A (இலவச சட்ட உதவி), 41 (வேலை, கல்வி, பொது உதவி), 42 (மனிதத்தன்மை வேலை நிலைமைகள் & பேறுகால உதவி), 43 (வாழ்வாதார ஊதியம் & ஓய்வு), 43A (மேலாண்மையில் தொழிலாளர்கள் பங்கேற்பு), 47 (சத்துணவு & பொது சுகாதாரத்தை உயர்த்துதல்).\n\n2. காந்தியக் கோட்பாடுகள்:\n- மகாத்மா காந்தியின் கிராம சுயராஜ்யம், கிராமப்புற மேம்பாடு, குடில்தொழில், மதுவிலக்கு மற்றும் கால்நடை நலன்களை வெளிப்படுத்தும் வழிகாட்டுதல்கள்.\n- உறுப்புகள்: 40 (கிராம ஊராட்சிகள்), 43 (குடில்தொழில்கள்), 43B (கூட்டுறவுச் சங்கங்கள் - 97வது திருத்தம்), 46 (எஸ்சி/எஸ்டி/எளிய பிரிவினர் கல்வி/பொருளாதார நலன்கள்), 47 (போதைப் பானங்கள் மதுவிலக்கு), 48 (பசுக்கள்/கன்றுகள்/பால் தரும்/பாரம் இழுக்கும் கால்நடைகள் வதை தடை).\n\n3. தாராளமய-அறிவுசார்க் கோட்பாடுகள்:\n- தாராளமயத் தத்துவம், சீரான சட்டங்கள், அறிவியல் மனப்பான்மை, சுற்றுச்சூழல், நினைவிடங்கள், நீதித்துறை சுயசார்பு மற்றும் சர்வதேச அமைதியை மேம்படுத்தும் வழிகாட்டுதல்கள்.\n- உறுப்புகள்: 44 (பொது சிவில் சட்டம்), 45 (6 வயதுக்குட்பட்ட முன்பருவக் கல்வி), 48 (அறிவியல் விவசாயம்/கால்நடை வளர்ப்பு), 48A (சுற்றுச்சூழல், காடுகள் & வனவிலங்குகள் - 42வது திருத்தம்), 49 (தேசிய நினைவிடங்கள் பாதுகாப்பு), 50 (நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு), 51 (சர்வதேச அமைதி, பாதுகாப்பு & நடுவர் மன்றம்)."
                        ]
                    }
                }
            ],
            "sec_article_map_36_51": [
                {
                    "title": "1. Articles 36 to 51 Master Constitutional Map (அரசியலமைப்பு உறுப்புகள் 36 முதல் 51 வரை முழுமையான வரைபடம்)",
                    "points": {
                        "en": [
                            "Article 36: Definition of State for Part IV (Adopts Article 12 definition).",
                            "Article 37: Application of DPSP (Non-justiciable in courts, but Fundamental in Governance).",
                            "Article 38(1): Securing a Social Order for promotion of welfare of people (Social, Economic, Political Justice).",
                            "Article 38(2): Minimising inequalities in income, status, facilities, and opportunities (Added by 44th CAA 1978).",
                            "Article 39(a): Right to adequate means of livelihood for all citizens.",
                            "Article 39(b): Material resources distribution to subserve common good (Protected by Art 31C).",
                            "Article 39(c): Prevention of concentration of wealth and production means (Protected by Art 31C).",
                            "Article 39(d): Equal pay for equal work for men and women (Equal Remuneration Act 1976).",
                            "Article 39(e): Protection of health and strength of workers and tender age of children.",
                            "Article 39(f): Opportunities for healthy development of children (Substituted by 42nd CAA 1976).",
                            "Article 39A: Equal justice and free legal aid to the poor (Added by 42nd CAA 1976; NALSA Act 1987).",
                            "Article 40: Organisation of Village Panchayats (Gandhian DPSP; 73rd CAA 1992 Part IX).",
                            "Article 41: Right to work, education, and public assistance (Subject to State economic capacity).",
                            "Article 42: Just and humane conditions of work and maternity relief (Maternity Benefit Act 1961).",
                            "Article 43: Living wage, decent standard of life, leisure, and rural cottage industries (KVIC Act 1956).",
                            "Article 43A: Workers' participation in management of industrial undertakings (Added by 42nd CAA 1976).",
                            "Article 43B: Promotion of voluntary formation & autonomous functioning of Co-operative Societies (Added by 97th CAA 2011).",
                            "Article 44: Uniform Civil Code (UCC) for citizens throughout India (DPSP, not FR; Goa precedent).",
                            "Article 45: Early childhood care and education for children below 6 years (Substituted by 86th CAA 2002).",
                            "Article 46: Educational and economic interests of SCs, STs & weaker sections (DPSP anchor for Art 15/16 reservations).",
                            "Article 47: Duty to raise nutrition, standard of living, public health & prohibition of liquor/injurious drugs.",
                            "Article 48: Scientific organization of agriculture & animal husbandry, breed preservation, cow slaughter prohibition.",
                            "Article 48A: Protection and improvement of environment, safeguarding forests and wildlife (Added by 42nd CAA 1976).",
                            "Article 49: Protection of monuments, places, and objects of national importance declared by Parliament.",
                            "Article 50: Separation of judiciary from executive in public services of the State (CrPC 1973).",
                            "Article 51: Promotion of international peace, security, just national relations, international law respect & arbitration."
                        ],
                        "ta": [
                            "உறுப்பு 36: பகுதி IV-க்கான அரசின் வரையறை (உறுப்பு 12 வரையறையை ஏற்கிறது).",
                            "உறுப்பு 37: DPSP பயன்பாடு (நீதிமன்றங்களால் அமல்படுத்த முடியாதது, ஆனால் ஆட்சியில் அடிப்படையானது).",
                            "உறுப்பு 38(1): மக்கள் நலனுக்கான சமூக ஒழுங்கை உருவாக்குதல் (சமூக, பொருளாதார, அரசியல் நீதி).",
                            "உறுப்பு 38(2): வருமானம், அந்தஸ்து, வசதி, வாய்ப்புகளில் சமத்துவமின்மையைக் குறைத்தல் (44வது திருத்தம் 1978 மூலம் சேர்க்கப்பட்டது).",
                            "உறுப்பு 39(a): அனைத்துக் குடிமக்களுக்கும் போதுமான வாழ்வாதார வழிவகைகள் உரிமை.",
                            "உறுப்பு 39(b): பொது நலனுக்காகச் சமூகத்தின் பொருள் வளங்களைப் பகிர்ந்தளித்தல் (உறுப்பு 31C பாதுகாப்பு).",
                            "உறுப்பு 39(c): செல்வக் குவிப்பு மற்றும் உற்பத்தி சாதனங்கள் குவிவதைத் தடுத்தல் (உறுப்பு 31C பாதுகாப்பு).",
                            "உறுப்பு 39(d): ஆண், பெண் இருபாலருக்கும் சம வேலைக்கு சம ஊதியம் (சம ஊதியச் சட்டம் 1976).",
                            "உறுப்பு 39(e): தொழிலாளர்கள் மற்றும் குழந்தைகளின் ஆரோக்கியம் மற்றும் வலிமை பாதுகாப்பு.",
                            "உறுப்பு 39(f): குழந்தைகள் ஆரோக்கியமான முறையில் வளர்வதற்கான வாய்ப்புகள் (42வது திருத்தம் 1976 மூலம் மாற்றப்பட்டது).",
                            "உறுப்பு 39A: ஏழைகளுக்குச் சம நீதியும் இலவச சட்ட உதவியும் (42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது; NALSA சட்டம் 1987).",
                            "உறுப்பு 40: கிராம ஊராட்சிகளை அமைத்தல் (காந்திய DPSP; 73வது திருத்தம் 1992 பகுதி IX).",
                            "உறுப்பு 41: வேலை, கல்வி மற்றும் பொது உதவி பெறும் உரிமை (அரசின் பொருளாதாரத் திறனுக்கு உட்பட்டது).",
                            "உறுப்பு 42: நியாயமான, மனிதத்தன்மையுள்ள வேலை நிலைமைகளும் பேறுகால உதவியும் (பேறுகால நலச் சட்டம் 1961).",
                            "உறுப்பு 43: வாழ்வாதார ஊதியம், கண்ணியமான வாழ்க்கை முறை, ஓய்வு & கிராமப்புறக் குடில்தொழில்கள்.",
                            "உறுப்பு 43A: தொழிற்சாலைகள் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பு (42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது).",
                            "உறுப்பு 43B: கூட்டுறவுச் சங்கங்களின் தன்னாட்சி செயல்பாட்டை மேம்படுத்துதல் (97வது திருத்தம் 2011 மூலம் சேர்க்கப்பட்டது).",
                            "உறுப்பு 44: இந்தியா முழுவதும் குடிமக்களுக்கான பொது சிவில் சட்டம் (UCC - DPSP, FR அல்ல; கோவா முன்னுதாரணம்).",
                            "உறுப்பு 45: 6 வயதுக்குட்பட்ட குழந்தைகளுக்கான முன்பருவக் பராமரிப்பும் கல்வியும் (86வது திருத்தம் 2002 மூலம் மாற்றப்பட்டது).",
                            "உறுப்பு 46: எஸ்சி, எஸ்டி & எளிய பிரிவினரின் கல்வி, பொருளாதார நலன்களை மேம்படுத்துதல்.",
                            "உறுப்பு 47: சத்துணவு, வாழ்க்கை முறை, பொது சுகாதாரத்தை உயர்த்துதல் & மதுவிலக் கொண்டுவருதல்.",
                            "உறுப்பு 48: அறிவியல் விவசாயம் & கால்நடை வளர்ப்பு, இனம் பாதுகாப்பு, பசு வதை தடை.",
                            "உறுப்பு 48A: சுற்றுச்சூழல், காடுகள் மற்றும் வனவிலங்குகள் பாதுகாப்பு (42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது).",
                            "உறுப்பு 49: நாடாளுமன்றத்தால் அறிவிக்கப்பட்ட தேசிய முக்கியத்துவம் வாய்ந்த நினைவிடங்கள் பாதுகாப்பு.",
                            "உறுப்பு 50: மாநிலத்தின் பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரித்தல் (CrPC 1973).",
                            "உறுப்பு 51: சர்வதேச அமைதி, பாதுகாப்பு, நாடுகளுக்கிடையே கெளரவமான உறவுகள், சர்வதேச சட்டம் & நடுவர் மன்றம் மேம்பாடு."
                        ]
                    }
                }
            ],
            "sec_fr_vs_dpsp": [
                {
                    "title": "1. Fundamental Rights vs DPSP: Four-Phase Judicial Evolution (FR vs DPSP நீதித்துறை வளர்ச்சி)",
                    "points": {
                        "en": [
                            "Phase 1 – Champakam Dorairajan Case (1951): Supreme Court held that Fundamental Rights (Part III) are SUPERIOR to Directive Principles (Part IV). DPSP must run as subsidiary/subordinate to Part III. Led to 1st Amendment Act 1951 inserting Art 15(4).\n\nPhase 2 – Re Kerala Education Bill (1958): Supreme Court introduced the Doctrine of Harmonious Construction (இணக்கமான விளக்கக் கோட்பாடு). Held that court should attempt to give effect to both Part III and Part IV without destroying either.\n\nPhase 3 – Golak Nath (1967) & 25th Amendment Act (1971):\n- Golak Nath (1967): SC held FRs are sacrosanct and cannot be curtailed by Parliament even to implement DPSP.\n- 25th Amendment Act 1971: Parliament inserted Article 31C stating that laws implementing DPSP Article 39(b) and 39(c) cannot be invalidated under Articles 14, 19, or 31.\n- Kesavananda Bharati (1973): SC UPHELD Article 31C Part 1, establishing that DPSP 39(b)/(c) can take precedence over FRs under Arts 14 and 19.\n\nPhase 4 – Minerva Mills Case (1980) & Present Position:\n- 42nd Amendment 1976 attempted to extend 31C protection to ALL DPSPs over Part III.\n- Minerva Mills (1980): Supreme Court STRUCK DOWN that extension. SC declared: 'The Indian Constitution is founded on the bedrock of the BALANCE between Part III and Part IV. To give absolute primacy to one over the other is to disturb the harmony of the Constitution. This HARMONY AND BALANCE is a BASIC FEATURE of the Constitution.'\n- Present Status: Fundamental Rights enjoy general primacy over DPSP, EXCEPT that laws implementing Article 39(b) and Article 39(c) take precedence over Article 14 and Article 19!"
                        ],
                        "ta": [
                            "கட்டம் 1 – செண்பகம் துரைராஜன் வழக்கு (1951): அடிப்படை உரிமைகள் (பகுதி III) வழிகாட்டு நெறிமுறைகளை (பகுதி IV) விட மேலானவை என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. DPSP பகுதி III-க்கு துணையாகவே செயல்பட வேண்டும். இது 1வது திருத்தச் சட்டம் 1951-க்கு வழிவகுத்தது.\n\nகட்டம் 2 – கேரளா கல்வி மசோதா வழக்கு (1958): உச்ச நீதிமன்றம் இணக்கமான விளக்கக் கோட்பாட்டை (Harmonious Construction) அறிமுகப்படுத்தியது. நீதிமன்றம் இரண்டையும் அழிக்காமல் பகுதி III மற்றும் பகுதி IV ஆகிய இரண்டிற்கும் செயலாக்கம் அளிக்க முயல வேண்டும் எனத் தீர்ப்பளித்தது.\n\nகட்டம் 3 – கோலக் நாத் (1967) & 25வது திருத்தச் சட்டம் (1971):\n- கோலக் நாத் (1967): DPSP-ஐ அமல்படுத்துவதற்காகக் கூட நாடாளுமன்றத்தால் அடிப்படை உரிமைகளைக் குறைக்க முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n- 25வது திருத்தச் சட்டம் 1971: நாடாளுமன்றம் உறுப்பு 31C-ஐ இணைத்தது, DPSP உறுப்பு 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்களை உறுப்புகள் 14, 19, 31-ன் கீழ் செல்லாததாக்க முடியாது என்றது.\n- கேசவானந்த பாரதி (1973): உச்ச நீதிமன்றம் உறுப்பு 31C முதல் பகுதியை உறுதி செய்து, DPSP 39(b)/(c) உறுப்புகள் 14, 19-ஐ விட முதன்மை பெறலாம் என நிறுவியது.\n\nகட்டம் 4 – மினர்வா மில்ஸ் வழக்கு (1980) & தற்போதைய நிலை:\n- 42வது திருத்தம் 1976 31C பாதுகாப்பை அனைத்து DPSP-களுக்கும் நீட்டிக்க முயன்றது.\n- மினர்வா மில்ஸ் (1980): உச்ச நீதிமன்றம் அந்த நீட்டிப்பை ரத்து செய்தது. SC அறிவித்தது: 'இந்திய அரசியலமைப்பு பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையின் அடித்தளத்தில் நிறுவப்பட்டுள்ளது. ஒன்றிற்கு மற்றொன்றை விட முழு முதன்மை அளிப்பது அரசியலமைப்பின் இணக்கத்தைக் குலைப்பதாகும். இந்த இணக்கமும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அம்சமாகும்.'\n- தற்போதைய நிலை: DPSP-ஐ விட அடிப்படை உரிமைகளுக்கே பொதுவான முதன்மை உண்டு, ஆனால் உறுப்பு 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்கள் உறுப்புகள் 14 மற்றும் 19-ஐ விட முதன்மை பெறுகின்றன!"
                        ]
                    }
                }
            ],
            "sec_dpsp_vs_fd": [
                {
                    "title": "1. DPSP vs Fundamental Duties & Basic Structure (DPSP vs அடிப்படைக் கடமைகள் & அடிப்படை அமைப்பு)",
                    "points": {
                        "en": [
                            "DPSP (Part IV) vs Fundamental Duties (Part IV-A):\n- Part IV DPSP (Articles 36–51): Directives addressed to the STATE. Imposes positive socio-economic governance duties on government.\n- Part IV-A Fundamental Duties (Article 51A): Directives addressed to CITIZENS of India. Added by 42nd Amendment 1976 on Swaran Singh Committee recommendation.\n- Direct Synergy (Art 48A vs Art 51A(g)): Article 48A commands the STATE to protect environment & wildlife; Article 51A(g) commands EVERY CITIZEN to protect environment & wildlife.\n\nDPSP and Basic Structure Doctrine:\n- In Minerva Mills (1980), SC affirmed that the harmony and balance between Part III (FRs) and Part IV (DPSP) is an essential element of the Basic Structure of the Constitution.\n- In Unni Krishnan (1993), SC held that Fundamental Rights and DPSP are supplementary and complementary to each other, and Part III rights must be read in the light of Part IV goals."
                        ],
                        "ta": [
                            "DPSP (பகுதி IV) vs அடிப்படைக் கடமைகள் (பகுதி IV-A):\n- பகுதி IV DPSP (உறுப்புகள் 36–51): அரசுக்கு வழங்கப்பட்ட வழிகாட்டுதல்கள். அரசாங்கத்தின் மீது நேர்மறை சமூக-பொருளாதார ஆட்சிக் கடமைகளை விதிக்கிறது.\n- பகுதி IV-A அடிப்படைக் கடமைகள் (உறுப்பு 51A): இந்தியாவின் குடிமக்களுக்கு வழங்கப்பட்ட வழிகாட்டுதல்கள். ஸ்வரன் சிங் குழு பரிந்துரையால் 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது.\n- நேரடி ஒருங்கிணைப்பு (உறுப்பு 48A vs உறுப்பு 51A(g)): உறுப்பு 48A சுற்றுச்சூழலையும் வனவிலங்குகளையும் பாதுகாக்குமாறு அரசுக்கு ஆணையிடுகிறது; உறுப்பு 51A(g) சுற்றுச்சூழலையும் வனவிலங்குகளையும் பாதுகாக்குமாறு ஒவ்வொரு குடிமகனுக்கும் ஆணையிடுகிறது.\n\nDPSP மற்றும் அடிப்படை அமைப்புக் கோட்பாடு:\n- மினர்வா மில்ஸ் வழக்கில் (1980), பகுதி III (FR) மற்றும் பகுதி IV (DPSP) இடையிலான இணக்கமும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அமைப்பின் அத்தியாவசிய அம்சம் என உச்ச நீதிமன்றம் உறுதிப்படுத்தியது.\n- உன்னி கிருஷ்ணன் வழக்கில் (1993), அடிப்படை உரிமைகளும் DPSP-யும் ஒன்றுக்கொன்று துணையாகவும் நிரப்பியாகவும் செயல்படுகின்றன என்றும், பகுதி IV இலக்குகளின் வெளிச்சத்திலேயே பகுதி III உரிமைகள் வாசிக்கப்பட வேண்டும் என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
                        ]
                    }
                }
            ],
            "sec_landmark_cases_amendments": [
                {
                    "title": "1. Master Summary of DPSP Constitutional Amendments (அரசியலமைப்பு திருத்தங்களின் தொகுப்பு)",
                    "points": {
                        "en": [
                            "1. 42nd Constitutional Amendment Act, 1976 (Added 4 New DPSPs):\n- Article 39(f): Opportunities for healthy development of children.\n- Article 39A: Equal justice and free legal aid to the poor.\n- Article 43A: Participation of workers in management of industries.\n- Article 48A: Protection and improvement of environment, forests and wildlife.\n\n2. 44th Constitutional Amendment Act, 1978:\n- Added Article 38(2): Mandated State to minimise inequalities in income, status, facilities, and opportunities.\n\n3. 86th Constitutional Amendment Act, 2002:\n- Substituted Article 45: Changed focus to early childhood care & education for children below 6 years (inserted Art 21A for 6-14 yrs FR).\n\n4. 97th Constitutional Amendment Act, 2011:\n- Added Article 43B: Promotion of voluntary formation, autonomous functioning & professional management of Co-operative Societies."
                        ],
                        "ta": [
                            "1. 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் (4 புதிய DPSP-கள் சேர்க்கப்பட்டன):\n- உறுப்பு 39(f): குழந்தைகள் ஆரோக்கியமான முறையில் வளர்வதற்கான வாய்ப்புகள்.\n- உறுப்பு 39A: ஏழைகளுக்குச் சம நீதியும் இலவச சட்ட உதவியும்.\n- உறுப்பு 43A: தொழிற்சாலைகள் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பு.\n- உறுப்பு 48A: சுற்றுச்சூழல், காடுகள் மற்றும் வனவிலங்குகள் பாதுகாப்பு.\n\n2. 1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம்:\n- உறுப்பு 38(2) சேர்க்கப்பட்டது: வருமானம், அந்தஸ்து, வசதி, வாய்ப்புகளில் சமத்துவமின்மையைக் குறைக்க அரசுக்கு ஆணையிட்டது.\n\n3. 2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம்:\n- உறுப்பு 45 மாற்றப்பட்டது: 6 வயதுக்குட்பட்ட குழந்தைகளுக்கான முன்பருவக் பராமரிப்பு மீது கவனம் செலுத்தியது (6-14 வயது FR-க்காக உறுப்பு 21A சேர்க்கப்பட்டது).\n\n4. 2011-ன் 97வது அரசியலமைப்பு திருத்தச் சட்டம்:\n- உறுப்பு 43B சேர்க்கப்பட்டது: கூட்டுறவுச் சங்கங்களின் தன்னார்வ உருவாக்கம் & தன்னாட்சி செயல்பாட்டை மேம்படுத்துதல்."
                        ]
                    }
                },
                {
                    "title": "2. Master Summary of Landmark DPSP Supreme Court Rulings (முக்கிய வழக்கு தீர்ப்புகள்)",
                    "points": {
                        "en": [
                            "1. Champakam Dorairajan (1951): FRs superior to DPSP; DPSP runs as subsidiary to Part III.\n2. Re Kerala Education Bill (1958): Doctrine of Harmonious Construction introduced.\n3. Golak Nath (1967): FRs sacrosanct; Parliament cannot amend Part III for DPSP.\n4. Kesavananda Bharati (1973): Upheld Art 31C Part 1; DPSP 39(b)/(c) can prevail over Arts 14 & 19.\n5. Minerva Mills (1980): Balance between Part III and Part IV is a Basic Feature of Constitution.\n6. Waman Rao (1981): Confirmed Basic Structure doctrine applies post-April 24, 1973.\n7. Randhir Singh (1982): Equal Pay for Equal Work (Art 39(d)) enforceable under Arts 14 & 16.\n8. Sanjeev Coke (1983) & Abu Kavur Bai (1984): Priority of Art 39(b)/(c) laws for nationalization.\n9. Mirzapur Moti Kureshi (2005): Total ban on cow progeny slaughter upheld under Art 48.\n10. M.C. Mehta Cases: Art 48A + 51A(g) read into Art 21 Right to Clean Environment."
                        ],
                        "ta": [
                            "1. செண்பகம் துரைராஜன் (1951): FR-கள் DPSP-ஐ விட மேலானவை; DPSP பகுதி III-க்கு துணையாகவே செயல்படும்.\n2. கேரளா கல்வி மசோதா (1958): இணக்கமான விளக்கக் கோட்பாடு அறிமுகப்படுத்தப்பட்டது.\n3. கோலக் நாத் (1967): FR-கள் புனிதமானவை; DPSP-க்காக பகுதி III-ஐத் திருத்த முடியாது.\n4. கேசவானந்த பாரதி (1973): உறுப்பு 31C பகுதி 1 உறுதி செய்யப்பட்டது; DPSP 39(b)/(c) உறுப்புகள் 14 & 19-ஐ விட மேலோங்கலாம்.\n5. மினர்வா மில்ஸ் (1980): பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையே அரசியலமைப்பின் அடிப்படை அம்சம்.\n6. வாமன் ராவ் (1981): ஏப்ரல் 24, 1973க்குப் பிறகு அடிப்படை அமைப்புக் கோட்பாடு பொருந்தும் என உறுதி செய்யப்பட்டது.\n7. ரந்தீர் சிங் (1982): சம வேலைக்கு சம ஊதியம் (39(d)) உறுப்புகள் 14 & 16-ன் கீழ் அமல்படுத்தத்தக்கது.\n8. சஞ்சீவ் கோக் (1983) & அபு கவூர் பாய் (1984): தேசியமயமாக்கல் சட்டங்களுக்கு உறுப்பு 39(b)/(c) முன்னுரிமை.\n9. மிர்சாபூர் மோதி குரேஷி (2005): உறுப்பு 48-ன் கீழ் பசு சந்ததிகள் வதை மீதான முழுத் தடை உறுதி செய்யப்பட்டது.\n10. எம்.சி. மேத்தா வழக்குகள்: உறுப்பு 48A + 51A(g) தூய்மையான சுற்றுச்சூழல் உரிமையாக உறுப்பு 21-க்குள் வாசிக்கப்பட்டது."
                        ]
                    }
                }
            ],
            "sec_traps_revision": [
                {
                    "title": "1. High-Yield TNPSC Traps for Part 3 & Complete DPSP (டிஎன்பிஎஸ்சி பொறிகள்)",
                    "points": {
                        "en": [
                            "Article 48A (Environment DPSP) was added by 42nd Amendment 1976 (State duty). Do not confuse with Article 51A(g) (Citizen duty).",
                            "Article 50 demands separation of judiciary from executive 'in the public services of the State'. CrPC 1973 fulfilled this.",
                            "Article 51 is a DPSP on Foreign Policy & International Peace. Article 51A is Part IV-A (Fundamental Duties).",
                            "Minerva Mills (1980) declared that the BALANCE between Part III (FRs) and Part IV (DPSP) is a Basic Feature of the Constitution.",
                            "Laws implementing Article 39(b) and Article 39(c) ONLY take precedence over Articles 14 and 19 under Article 31C.",
                            "DPSP classification into Socialist, Gandhian, and Liberal is a CONVENTIONAL ACADEMIC division, NOT written in Constitution text."
                        ],
                        "ta": [
                            "உறுப்பு 48A (சுற்றுச்சூழல் DPSP) 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது (அரசு கடமை). அதை உறுப்பு 51A(g)-உடன் (குடிமகன் கடமை) குழப்ப வேண்டாம்.",
                            "உறுப்பு 50 'மாநிலத்தின் பொது சேவைகளில்' நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்கக் கோருகிறது. CrPC 1973 இதை நிறைவேற்றியது.",
                            "உறுப்பு 51 என்பது வெளியுறவுக் கொள்கை & சர்வதேச அமைதி பற்றிய DPSP. உறுப்பு 51A என்பது பகுதி IV-A (அடிப்படைக் கடமைகள்).",
                            "பகுதி III (FR) மற்றும் பகுதி IV (DPSP) இடையிலான சமநிலையே அரசியலமைப்பின் அடிப்படை அம்சம் என மினர்வா மில்ஸ் (1980) அறிவித்தது.",
                            "உறுப்பு 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்கள் மட்டுமே உறுப்பு 31C-ன் கீழ் உறுப்புகள் 14 மற்றும் 19-ஐ விட மேலோங்குகின்றன.",
                            "DPSP-ஐ சமதர்ம, காந்திய, தாராளமயப் பிரிவுகளாகப் பிரிப்பது ஒரு மரபுவழி கல்விப் பிரிவே தவிர, அரசியலமைப்பு உரையில் எழுதப்படவில்லை."
                        ]
                    }
                }
            ],
            "tables": [
                {
                    "title_en": "1. Article 48 (Agriculture/Cattle) vs Article 48A (Environment/Wildlife)",
                    "title_ta": "1. உறுப்பு 48 (விவசாயம்/கால்நடை) vs உறுப்பு 48A (சுற்றுச்சூழல்/வனவிலங்கு)",
                    "headers_en": ["Feature", "Article 48 (Original 1950)", "Article 48A (Added 42nd CAA 1976)"],
                    "headers_ta": ["அம்சம்", "உறுப்பு 48 (அசல் 1950)", "உறுப்பு 48A (42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது)"],
                    "rows_en": [
                        ["Core Focus", "Scientific organisation of agriculture, animal husbandry, breed preservation, cow slaughter ban", "Protection and improvement of natural environment, safeguarding forests and wildlife"],
                        ["Ideological Category", "Conventional Gandhian (cattle protection) & Scientific directive", "Conventional Liberal-Intellectual Principle"],
                        ["Constitutional History", "Part of original 1950 Constitution text", "Inserted by 42nd Constitutional Amendment Act, 1976"],
                        ["Implementing Laws", "State Cattle Slaughter Prohibition Acts, KVIC, Livestock Breeding policies", "Wildlife Protection Act 1972, Forest Conservation Act 1980, Environment Protection Act 1986"]
                    ],
                    "rows_ta": [
                        ["முதன்மை கவனம்", "விவசாயம், கால்நடை வளர்ப்பு, இனம் பாதுகாப்பு, பசு வதை தடை ஆகியவற்றின் அறிவியல் அமைப்பு", "இயற்கைச் சூழலைப் பாதுகாத்தல் மற்றும் மேம்படுத்துதல், காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாத்தல்"],
                        ["தத்துவப் பிரிவு", "மரபுவழி காந்திய (கால்நடை பாதுகாப்பு) & அறிவியல் வழிகாட்டுதல்", "மரபுவழி தாராளமய-அறிவுசார்க் கோட்பாடு"],
                        ["அரசியலமைப்பு வரலாறு", "அசல் 1950 அரசியலமைப்பு உரையின் பகுதி", "1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இணைக்கப்பட்டது"],
                        ["செயல்படுத்தும் சட்டங்கள்", "மாநில கால்நடை வதை தடைச் சட்டங்கள், KVIC, கால்நடை இனப்பெருக்கக் கொள்கைகள்", "வனவிலங்கு பாதுகாப்புச் சட்டம் 1972, வனப் பாதுகாப்புச் சட்டம் 1980, சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் 1986"]
                    ]
                },
                {
                    "title_en": "2. Article 48A (State Environment Duty) vs Article 51A(g) (Citizen Environment Duty)",
                    "title_ta": "2. உறுப்பு 48A (அரசு சுற்றுச்சூழல் கடமை) vs உறுப்பு 51A(g) (குடிமகன் சுற்றுச்சூழல் கடமை)",
                    "headers_en": ["Aspect", "Article 48A (Part IV DPSP)", "Article 51A(g) (Part IV-A Fundamental Duty)"],
                    "headers_ta": ["அம்சம்", "உறுப்பு 48A (பகுதி IV DPSP)", "உறுப்பு 51A(g) (பகுதி IV-A அடிப்படைக் கடமை)"],
                    "rows_en": [
                        ["Target Entity", "Addressed to the STATE (Government, Parliament, Legislatures, Authorities)", "Addressed to EVERY CITIZEN of India"],
                        ["Constitutional Mandate", "'State shall endeavor to protect and improve environment and safeguard forests/wildlife'", "'Duty of every citizen to protect/improve environment including forests, lakes, rivers, wildlife'"],
                        ["Part & Location", "Part IV (Directive Principles of State Policy)", "Part IV-A (Fundamental Duties)"],
                        ["Judicial Integration", "SC reads 48A and 51A(g) together into Article 21 to enforce Right to Clean Environment", "SC uses 51A(g) to uphold statutory environmental duties and citizen compliance"]
                    ],
                    "rows_ta": [
                        ["இலக்கு அமைப்பு", "அரசுக்கு வழங்கப்பட்டது (அரசாங்கம், நாடாளுமன்றம், சட்டமன்றங்கள், அமைப்புகள்)", "இந்தியாவின் ஒவ்வொரு குடிமகனுக்கும் வழங்கப்பட்டது"],
                        ["அரசியலமைப்பு கட்டளை", "'சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் காடுகள்/வனவிலங்குகளைப் பாதுகாக்கவும் அரசு முயல வேண்டும்'", "'காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள் உள்ளிட்ட சூழலைப் பாதுகாப்பது ஒவ்வொரு குடிமகனின் கடமை'"],
                        ["பகுதி & இடம்", "பகுதி IV (அரசு வழிகாட்டு நெறிமுறைகள்)", "பகுதி IV-A (அடிப்படைக் கடமைகள்)"],
                        ["நீதித்துறை ஒருங்கிணைப்பு", "தூய்மையான சுற்றுச்சூழல் உரிமையை அமல்படுத்த SC 48A மற்றும் 51A(g) ஆகியவற்றை உறுப்பு 21-க்குள் சேர்த்து வாசிக்கிறது", "சட்டப்பூர்வ சுற்றுச்சூழல் கடமைகள் மற்றும் குடிமக்கள் இணக்கத்தை உறுதிப்படுத்த SC 51A(g)-ஐப் பயன்படுத்துகிறது"]
                    ]
                },
                {
                    "title_en": "3. Article 49 (Monuments Protection DPSP) vs Articles 29–30 (Minority Cultural Rights FR)",
                    "title_ta": "3. உறுப்பு 49 (நினைவிடங்கள் பாதுகாப்பு DPSP) vs உறுப்புகள் 29–30 (சிறுபான்மையினர் பண்பாட்டு உரிமைகள் FR)",
                    "headers_en": ["Feature", "Article 49 (Part IV DPSP)", "Articles 29 & 30 (Part III FRs)"],
                    "headers_ta": ["அம்சம்", "உறுப்பு 49 (பகுதி IV DPSP)", "உறுப்புகள் 29 & 30 (பகுதி III FRs)"],
                    "rows_en": [
                        ["Legal Status", "Non-justiciable policy directive directing State to protect monuments of national importance", "JUSTICIABLE Fundamental Rights enforceable directly in Supreme Court under Article 32"],
                        ["Subject Focus", "Physical historical heritage, monuments, places, and artistic objects of national importance", "Cultural identity, language, script, and educational institutions of minorities/citizens"],
                        ["Scope of Target", "Applies to monuments declared by PARLIAMENT by law to be of 'national importance'", "Applies to religious and linguistic minorities (Art 30) or any section of citizens (Art 29)"],
                        ["Authority / Enacting Agency", "Archaeological Survey of India (ASI 1861), AMASR Act 1958", "Minorities Educational Institutions Act, National Commission for Minorities"]
                    ],
                    "rows_ta": [
                        ["சட்டப்பூர்வ அந்தஸ்து", "தேசிய முக்கியத்துவம் வாய்ந்த நினைவிடங்களைப் பாதுகாக்க அரசுக்கு ஆணையிடும் அமல்படுத்த முடியாத கொள்கை வழிகாட்டுதல்", "உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தில் நேரடியாக அமல்படுத்தக்கூடிய அடிப்படை உரிமைகள்"],
                        ["பொருள் கவனம்", "தேசிய முக்கியத்துவம் வாய்ந்த பௌதிக வரலாற்று பாரம்பரியம், நினைவிடங்கள், இடங்கள் மற்றும் கலைப் பொருட்கள்", "சிறுபான்மையினர்/குடிமக்களின் பண்பாட்டு அடையாளம், மொழி, எழுத்து மற்றும் கல்வி நிறுவனங்கள்"],
                        ["இலக்கின் எல்லை", "நாடாளுமன்றச் சட்டத்தால் 'தேசிய முக்கியத்துவம் வாய்ந்தது' என அறிவிக்கப்பட்ட நினைவிடங்களுக்குப் பொருந்தும்", "மத மற்றும் மொழிச் சிறுபான்மையினருக்கு (உறுப்பு 30) அல்லது குடிமக்களின் பிரிவினருக்கு (உறுப்பு 29) பொருந்தும்"],
                        ["அதிகாரம் / முகமை", "இந்தியத் தொல்லியல் துறை (ASI 1861), AMASR சட்டம் 1958", "சிறுபான்மையினர் கல்வி நிறுவனங்கள் சட்டம், தேசிய சிறுபான்மையினர் ஆணையம்"]
                    ]
                },
                {
                    "title_en": "4. Article 50 (Judicial Separation DPSP) vs Rigid Separation of Powers Doctrine",
                    "title_ta": "4. உறுப்பு 50 (நீதித்துறை பிரிப்பு DPSP) vs கடுமையான அதிகாரப் பிரிப்புக் கோட்பாடு",
                    "headers_en": ["Aspect", "Article 50 (Indian Constitution)", "Rigid Separation of Powers (e.g. US Constitution)"],
                    "headers_ta": ["அம்சம்", "உறுப்பு 50 (இந்திய அரசியலமைப்பு)", "கடுமையான அதிகாரப் பிரிப்பு (எ.கா. அமெரிக்க அரசியலமைப்பு)"],
                    "rows_en": [
                        ["Constitutional Scope", "Directs separation of Judiciary from Executive specifically in public services of the State", "Strict compartmentalization between Executive, Legislature, and Judiciary organs"],
                        ["Executive-Legislature Relation", "India follows Parliamentary Democracy where Executive is part of & responsible to Legislature", "US follows Presidential system where Executive is completely separate from Congress"],
                        ["Judicial Independence Tool", "CrPC 1973 separated Judicial Magistrates from Executive Magistrates; High Court controls courts", "Judicial power vested exclusively in Supreme Court and Federal Courts"],
                        ["Checks & Balances", "System of checks and balances (Judicial Review of laws, Parliamentary impeachment of judges)", "Strict separation with veto powers and judicial review"]
                    ],
                    "rows_ta": [
                        ["அரசியலமைப்பு எல்லை", "மாநிலத்தின் பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைக் குறிப்பாகப் பிரிக்க வழிகாட்டுகிறது", "நிர்வாகம், சட்டமன்றம் மற்றும் நீதித்துறை அமைப்புகளுக்கு இடையே கடுமையான துறைப் பிரிப்பு"],
                        ["நிர்வாக-சட்டமன்ற உறவு", "இந்தியா நாடாளுமன்ற ஜனநாயகத்தைப் பின்பற்றுகிறது, இதில் நிர்வாகம் சட்டமன்றத்தின் பகுதியாகவும் பொறுப்பாகவும் உள்ளது", "அமெரிக்கா அதிபர் முறையைப் பின்பற்றுகிறது, இதில் நிர்வாகம் காங்கிரஸிலிருந்து முற்றிலும் தனித்து செயல்படுகிறது"],
                        ["நீதித்துறை சுயசார்புக் கருவி", "CrPC 1973 நீதித்துறை மேஜிஸ்திரேட்டுகளை நிர்வாக மேஜிஸ்திரேட்டுகளிடமிருந்து பிரித்தது; உயர் நீதிமன்றக் கட்டுப்பாடு", "நீதித்துறை அதிகாரம் உச்ச நீதிமன்றம் மற்றும் ஃபெடரல் நீதிமன்றங்களிடம் மட்டுமே உள்ளது"],
                        ["கட்டுப்பாடுகள் & சமநிலைகள்", "கட்டுப்பாடுகள் மற்றும் சமநிலைகள் அமைப்பு (சட்டங்களின் நீதித்துறை ஆய்வு, நீதிபதிகள் மீது நாடாளுமன்ற பதவி நீக்கம்)", "வீட்டோ அதிகாரங்கள் மற்றும் நீதித்துறை ஆய்வுடன் கூடிய கடுமையான பிரிப்பு"]
                    ]
                },
                {
                    "title_en": "5. Article 51 (Foreign Policy DPSP) vs Article 51A (Fundamental Duties)",
                    "title_ta": "5. உறுப்பு 51 (வெளியுறவுக் கொள்கை DPSP) vs உறுப்பு 51A (அடிப்படைக் கடமைகள்)",
                    "headers_en": ["Feature", "Article 51 (Part IV DPSP)", "Article 51A (Part IV-A Fundamental Duty)"],
                    "headers_ta": ["அம்சம்", "உறுப்பு 51 (பகுதி IV DPSP)", "உறுப்பு 51A (பகுதி IV-A அடிப்படைக் கடமை)"],
                    "rows_en": [
                        ["Target Entity", "Directs the STATE in framing India's Foreign Policy and international relations", "Directs EVERY CITIZEN of India regarding moral and civic duties"],
                        ["Core Content", "International peace, security, honourable national relations, treaty respect & arbitration", "Abiding by Constitution, respecting National Flag/Anthem, protecting sovereignty & environment"],
                        ["Part & Location", "Part IV (Last Article of DPSP, Articles 36–51)", "Part IV-A (Single Article 51A with 11 clauses, added 42nd CAA 1976)"],
                        ["Statutory Execution", "Treaty making under Art 253, UN Peacekeeping, International Arbitration Act 1996", "Prevention of Insults to National Honour Act 1971, Flag Code, Wildlife Protection Act"]
                    ],
                    "rows_ta": [
                        ["இலக்கு அமைப்பு", "இந்தியாவின் வெளியுறவுக் கொள்கை மற்றும் சர்வதேச உறவுகளை வகுப்பதில் அரசுக்கு வழிகாட்டுகிறது", "ஒழுக்க மற்றும் சிவில் கடமைகள் குறித்து இந்தியாவின் ஒவ்வொரு குடிமகனுக்கும் ஆணையிடுகிறது"],
                        ["முதன்மை உள்ளடக்கம்", "சர்வதேச அமைதி, பாதுகாப்பு, கெளரவமான தேசிய உறவுகள், ஒப்பந்த மரிப்பு & நடுவர் மன்றம்", "அரசியலமைப்புக்குக் கட்டுப்படுதல், தேசியக் கொடி/கீதத்தை மதித்தல், இறையாண்மை & சூழலைப் பாதுகாத்தல்"],
                        ["பகுதி & இடம்", "பகுதி IV (DPSP-ன் கடைசி உறுப்பு, உறுப்புகள் 36–51)", "பகுதி IV-A (11 உட்பிரிவுகளைக் கொண்ட ஒற்றை உறுப்பு 51A, 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது)"],
                        ["சட்டப்பூர்வ நிறைவேற்றம்", "உறுப்பு 253-ன் கீழ் ஒப்பந்தம் செய்தல், ஐ.நா அமைதிப்படை, சர்வதேச நடுவர் மன்றச் சட்டம் 1996", "தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டம் 1971, தேசியக் கொடி விதிமுறை, வனவிலங்கு பாதுகாப்புச் சட்டம்"]
                    ]
                },
                {
                    "title_en": "6. Socialist vs Gandhian vs Liberal-Intellectual DPSP Master Classification",
                    "title_ta": "6. சமதர்ம vs காந்திய vs தாராளமய-அறிவுசார் DPSP முதன்மை வகைப்பாடு",
                    "headers_en": ["Category", "Core Ideology & Objective", "Articles Covered (Parts 1–3)", "Key Constitutional Amendments"],
                    "headers_ta": ["பிரிவு", "முதன்மை தத்துவம் & நோக்கம்", "உள்ளடக்கப்பட்ட உறுப்புகள் (பகுதிகள் 1–3)", "முக்கிய அரசியலமைப்பு திருத்தங்கள்"],
                    "rows_en": [
                        ["Socialist Principles (சமதர்மக் கோட்பாடுகள்)", "Welfare state, socio-economic justice, income equality, worker/child protection", "Articles 38, 39(a)-(f), 39A, 41, 42, 43, 43A, 47", "42nd CAA 1976 (39A, 39(f), 43A), 44th CAA 1978 (38(2))"],
                        ["Gandhian Principles (காந்தியக் கோட்பாடுகள்)", "Gram Swaraj, self-governance, cottage industry, prohibition, SC/ST welfare, cow protection", "Articles 40, 43, 43B, 46, 47, 48", "73rd CAA 1992 (Art 40 / Part IX), 97th CAA 2011 (Art 43B)"],
                        ["Liberal-Intellectual Principles (தாராளமய-அறிவுசார்க் கோட்பாடுகள்)", "Uniform laws, early education, scientific agriculture, environment, monuments, judiciary separation, world peace", "Articles 44, 45, 48, 48A, 49, 50, 51", "42nd CAA 1976 (48A), 86th CAA 2002 (Art 45)"]
                    ],
                    "rows_ta": [
                        ["சமதர்மக் கோட்பாடுகள்", "நல அரசு, சமூக-பொருளாதார நீதி, வருமான சமத்துவம், தொழிலாளர்/குழந்தை பாதுகாப்பு", "உறுப்புகள் 38, 39(a)-(f), 39A, 41, 42, 43, 43A, 47", "42வது திருத்தம் 1976 (39A, 39(f), 43A), 44வது திருத்தம் 1978 (38(2))"],
                        ["காந்தியக் கோட்பாடுகள்", "கிராம சுயராஜ்யம், சுய ஆட்சி, குடில்தொழில், மதுவிலக்கு, எஸ்சி/எஸ்டி நலன், பசு பாதுகாப்பு", "உறுப்புகள் 40, 43, 43B, 46, 47, 48", "73வது திருத்தம் 1992 (உறுப்பு 40 / பகுதி IX), 97வது திருத்தம் 2011 (உறுப்பு 43B)"],
                        ["தாராளமய-அறிவுசார்க் கோட்பாடுகள்", "சீரான சட்டங்கள், முன்பருவக் கல்வி, அறிவியல் விவசாயம், சுற்றுச்சூழல், நினைவிடங்கள், நீதித்துறை பிரிப்பு, உலக அமைதி", "உறுப்புகள் 44, 45, 48, 48A, 49, 50, 51", "42வது திருத்தம் 1976 (48A), 86வது திருத்தம் 2002 (உறுப்பு 45)"]
                    ]
                },
                {
                    "title_en": "7. Fundamental Rights (Part III) vs Directive Principles (Part IV) Synthesis",
                    "title_ta": "7. அடிப்படை உரிமைகள் (பகுதி III) vs அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV) தொகுப்பு",
                    "headers_en": ["Dimension", "Fundamental Rights (Part III)", "Directive Principles (Part IV)"],
                    "headers_ta": ["பரிமாணம்", "அடிப்படை உரிமைகள் (பகுதி III)", "அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV)"],
                    "rows_en": [
                        ["Nature of Mandate", "Negative restrictions prohibiting State arbitrary action against individuals", "Positive directives commanding State to perform welfare & governance duties"],
                        ["Judicial Enforceability", "JUSTICIABLE (Supreme Court Art 32 & High Court Art 226 issue writs directly)", "NON-JUSTICIABLE (cannot be enforced by court writs under Art 37)"],
                        ["Democracy Goal", "Establishes POLITICAL DEMOCRACY in India", "Establishes SOCIAL AND ECONOMIC DEMOCRACY & Welfare State"],
                        ["Conflict Resolution", "FRs enjoy general primacy, EXCEPT laws implementing Art 39(b) & 39(c) prevail over Arts 14 & 19 (Art 31C)", "DPSP 39(b) & 39(c) take precedence over Arts 14 & 19; harmony is Basic Structure (Minerva Mills 1980)"]
                    ],
                    "rows_ta": [
                        ["கட்டளையின் இயல்பு", "தனிநபர்களுக்கு எதிரான அரசின் தன்னிச்சையான நடவடிக்கைகளைத் தடுக்கும் எதிர்மறைக் கட்டுப்பாடுகள்", "நலன் & ஆட்சிக் கடமைகளைச் செய்ய அரசுக்கு ஆணையிடும் நேர்மறை வழிகாட்டுதல்கள்"],
                        ["நீதிமன்ற அமலாக்கம்", "அமல்படுத்தக் கூடியவை (உச்ச நீதிமன்றம் உறுப்பு 32 & உயர் நீதிமன்றம் உறுப்பு 226 நேரடியாகப் பேராணை பிறப்பிக்கும்)", "அமல்படுத்த முடியாதவை (உறுப்பு 37-ன் கீழ் நீதிமன்றப் பேராணைகள் மூலம் அமல்படுத்த முடியாது)"],
                        ["ஜனநாயக இலக்கு", "இந்தியாவில் அரசியல் ஜனநாயகத்தை நிறுவுகிறது", "சமூக மற்றும் பொருளாதார ஜனநாயகம் & நல அரசை நிறுவுகிறது"],
                        ["மோதல் தீர்வு", "FR-களுக்கே பொதுவான முதன்மை உண்டு, ஆனால் உறுப்பு 39(b) & 39(c)-ஐ செயல்படுத்தும் சட்டங்கள் உறுப்புகள் 14 & 19-ஐ விட மேலோங்குகின்றன (உறுப்பு 31C)", "DPSP 39(b) & 39(c) உறுப்புகள் 14 & 19-ஐ விட முதன்மை பெறுகின்றன; இணக்கமே அடிப்படை அமைப்பு (மினர்வா மில்ஸ் 1980)"]
                    ]
                },
                {
                    "title_en": "8. Directive Principles (Part IV) vs Fundamental Duties (Part IV-A)",
                    "title_ta": "8. அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV) vs அடிப்படைக் கடமைகள் (பகுதி IV-A)",
                    "headers_en": ["Feature", "Directive Principles (Part IV)", "Fundamental Duties (Part IV-A)"],
                    "headers_ta": ["அம்சம்", "அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV)", "அடிப்படைக் கடமைகள் (பகுதி IV-A)"],
                    "rows_en": [
                        ["Target Entity", "Directives addressed to the STATE (Government, Parliament, Authorities)", "Directives addressed to EVERY CITIZEN of India"],
                        ["Constitutional Location", "Part IV (Articles 36 to 51)", "Part IV-A (Single Article 51A with 11 clauses)"],
                        ["Origin & Insertion", "Part of original 1950 Constitution text (Irish inspiration)", "Inserted by 42nd Amendment Act 1976 (Swaran Singh Committee / USSR inspiration)"],
                        ["Nature & Purpose", "Non-justiciable governance goals for establishing a Welfare State", "Non-justiciable civic/moral duties for national integration and citizenship discipline"]
                    ],
                    "rows_ta": [
                        ["இலக்கு அமைப்பு", "அரசுக்கு வழங்கப்பட்ட வழிகாட்டுதல்கள் (அரசாங்கம், நாடாளுமன்றம், அமைப்புகள்)", "இந்தியாவின் ஒவ்வொரு குடிமகனுக்கும் வழங்கப்பட்ட வழிகாட்டுதல்கள்"],
                        ["அரசியலமைப்பு இடம்", "பகுதி IV (உறுப்புகள் 36 முதல் 51 வரை)", "பகுதி IV-A (11 உட்பிரிவுகளைக் கொண்ட ஒற்றை உறுப்பு 51A)"],
                        ["தோற்றம் & இணைப்பு", "அசல் 1950 அரசியலமைப்பு உரையின் பகுதி (அயர்லாந்து ஈர்ப்பு)", "1976-ன் 42வது திருத்தச் சட்டத்தால் இணைக்கப்பட்டது (ஸ்வரன் சிங் குழு / யுஎஸ்எஸ்ஆர் ஈர்ப்பு)"],
                        ["இயல்பு & நோக்கம்", "நல அரசை நிறுவுவதற்கான அமல்படுத்த முடியாத ஆட்சிக் கோட்பாடுகள்", "தேசிய ஒருமைப்பாடு மற்றும் குடிமக்கள் ஒழுக்கத்திற்கான அமல்படுத்த முடியாத சிவில்/ஒழுக்கக் கடமைகள்"]
                    ]
                },
                {
                    "title_en": "9. Part III (FR) vs Part IV (DPSP) Constitutional Architecture",
                    "title_ta": "9. பகுதி III (FR) vs பகுதி IV (DPSP) அரசியலமைப்பு கட்டமைப்பு",
                    "headers_en": ["Architectural Element", "Part III (Articles 12–35)", "Part IV (Articles 36–51)"],
                    "headers_ta": ["அரசியலமைப்பு கட்டமைப்பு அம்சம்", "பகுதி III (உறுப்புகள் 12–35)", "பகுதி IV (உறுப்புகள் 36–51)"],
                    "rows_en": [
                        ["Title & Nomenclature", "Fundamental Rights (Magna Carta of India)", "Directive Principles of State Policy (Novel Features)"],
                        ["Definition of State Anchor", "Article 12 defines State for Part III", "Article 36 adopts Article 12 definition of State for Part IV"],
                        ["Enforcement / Application Anchor", "Article 13 declares inconsistent laws void; Article 32 guarantees writ remedies", "Article 37 declares DPSP non-enforceable by courts, but fundamental in governance"],
                        ["Basic Structure Balance", "Part III civil/political liberties balance Part IV socio-economic goals", "Minerva Mills (1980) held harmony between Part III & Part IV is Basic Feature"]
                    ],
                    "rows_ta": [
                        ["தலைப்பு & பெயர்", "அடிப்படை உரிமைகள் (இந்தியாவின் மகா சாசனம்)", "அரசு வழிகாட்டு நெறிமுறைகள் (நவீன அம்சங்கள்)"],
                        ["அரசு வரையறை நங்கூரம்", "உறுப்பு 12 பகுதி III-க்காக அரசை வரையறுக்கிறது", "உறுப்பு 36 பகுதி IV-க்காக உறுப்பு 12 அரசு வரையறையை ஏற்கிறது"],
                        ["அமலாக்கம் / பயன்பாடு நங்கூரம்", "உறுப்பு 13 முரணான சட்டங்களைச் செல்லாததாக்குகிறது; உறுப்பு 32 பேராணை பரிகாரங்களை உத்தரவாதம் செய்கிறது", "உறுப்பு 37 DPSP நீதிமன்றங்களால் அமல்படுத்த முடியாதது, ஆனால் ஆட்சியில் அடிப்படையானது என அறிவிக்கிறது"],
                        ["அடிப்படை அமைப்பு சமநிலை", "பகுதி III சிவில்/அரசியல் சுதந்திரங்கள் பகுதி IV சமூக-பொருளாதார இலக்குகளைச் சமநிலைப்படுத்துகின்றன", "பகுதி III & பகுதி IV இடையிலான இணக்கமே அடிப்படை அம்சம் என மினர்வா மில்ஸ் (1980) கூறியது"]
                    ]
                },
                {
                    "title_en": "10. Complete Articles 36–51 Master Quick Table",
                    "title_ta": "10. உறுப்புகள் 36–51 முழுமையான முதன்மை ஒப்பீட்டு அட்டவணை",
                    "headers_en": ["Article", "Keyword / Title", "Core Objective", "Category & Amendment"],
                    "headers_ta": ["உறுப்பு", "முக்கிய சொல் / தலைப்பு", "முதன்மை நோக்கம்", "பிரிவு & திருத்தம்"],
                    "rows_en": [
                        ["Art 36", "Definition of State", "Adopts Article 12 definition for Part IV", "General Foundation"],
                        ["Art 37", "Application of DPSP", "Non-justiciable in courts; Fundamental in Governance", "General Foundation"],
                        ["Art 38(1)", "Social Order", "Promote welfare of people via Social, Economic, Political Justice", "Socialist"],
                        ["Art 38(2)", "Minimising Inequalities", "Minimise inequalities in income, status, facilities, opportunities", "Socialist (44th CAA 1978)"],
                        ["Art 39(a)", "Livelihood", "Right to adequate means of livelihood for all citizens", "Socialist"],
                        ["Art 39(b)", "Material Resources", "Community material resources distributed for common good", "Socialist (Art 31C protection)"],
                        ["Art 39(c)", "Wealth Concentration", "Economic system preventing concentration of wealth/production means", "Socialist (Art 31C protection)"],
                        ["Art 39(d)", "Equal Pay", "Equal pay for equal work for men and women", "Socialist (Equal Remuneration Act)"],
                        ["Art 39(e)", "Worker Health", "Protect health/strength of workers and tender age of children", "Socialist"],
                        ["Art 39(f)", "Child Development", "Opportunities for healthy development of children", "Socialist (42nd CAA 1976)"],
                        ["Art 39A", "Free Legal Aid", "Equal justice and free legal aid to the poor", "Socialist (42nd CAA 1976 / NALSA)"],
                        ["Art 40", "Village Panchayats", "Organise village panchayats as units of self-government", "Gandhian (73rd CAA 1992 Part IX)"],
                        ["Art 41", "Work & Education", "Right to work, education & public assistance in undeserved want", "Socialist (Subject to economic capacity)"],
                        ["Art 42", "Humane Work Conditions", "Just & humane conditions of work and maternity relief", "Socialist (Maternity Act 1961)"],
                        ["Art 43", "Living Wage", "Living wage, decent standard of life, leisure, cottage industries", "Socialist / Gandhian (KVIC)"],
                        ["Art 43A", "Worker Management", "Participation of workers in management of industrial undertakings", "Socialist (42nd CAA 1976)"],
                        ["Art 43B", "Co-operatives", "Promote voluntary formation & autonomous functioning of co-operatives", "Gandhian (97th CAA 2011)"],
                        ["Art 44", "Uniform Civil Code", "Secure Uniform Civil Code for all citizens throughout India", "Liberal-Intellectual (Goa precedent)"],
                        ["Art 45", "Early Childhood Care", "Early childhood care and education for children below 6 years", "Liberal-Intellectual (86th CAA 2002)"],
                        ["Art 46", "SC/ST Welfare", "Promote educational & economic interests of SCs, STs & weaker sections", "Gandhian / Socialist"],
                        ["Art 47", "Nutrition & Prohibition", "Raise nutrition/living standards/public health & prohibition of liquor", "Socialist / Gandhian"],
                        ["Art 48", "Scientific Agriculture", "Scientific agriculture/animal husbandry, breed preservation, cow slaughter ban", "Gandhian / Scientific"],
                        ["Art 48A", "Environment Protection", "Protect and improve environment, safeguard forests and wildlife", "Liberal-Intellectual (42nd CAA 1976)"],
                        ["Art 49", "National Monuments", "Protect monuments, places & objects of national importance", "Liberal-Intellectual (ASI / AMASR)"],
                        ["Art 50", "Judicial Separation", "Separate judiciary from executive in public services of the State", "Liberal-Intellectual (CrPC 1973)"],
                        ["Art 51", "International Peace", "Promote international peace, security, treaty respect & arbitration", "Liberal-Intellectual (Foreign Policy)"]
                    ],
                    "rows_ta": [
                        ["உறுப்பு 36", "அரசின் வரையறை", "பகுதி IV-க்காக உறுப்பு 12 வரையறையை ஏற்கிறது", "பொதுவான அடித்தளம்"],
                        ["உறுப்பு 37", "DPSP பயன்பாடு", "நீதிமன்றங்களால் அமல்படுத்த முடியாதது; ஆட்சியில் அடிப்படையானது", "பொதுவான அடித்தளம்"],
                        ["உறுப்பு 38(1)", "சமூக ஒழுங்கு", "சமூக, பொருளாதார, அரசியல் நீதி மூலம் மக்கள் நலனை மேம்படுத்துதல்", "சமதர்மம்"],
                        ["உறுப்பு 38(2)", "சமத்துவமின்மையைக் குறைத்தல்", "வருமானம், அந்தஸ்து, வசதி, வாய்ப்புகளில் சமத்துவமின்மையைக் குறைத்தல்", "சமதர்மம் (44வது திருத்தம் 1978)"],
                        ["உறுப்பு 39(a)", "வாழ்வாதாரம்", "அனைத்துக் குடிமக்களுக்கும் போதுமான வாழ்வாதார வழிவகைகள் உரிமை", "சமதர்மம்"],
                        ["உறுப்பு 39(b)", "பொருள் வளங்கள்", "பொது நலனுக்காகச் சமூகத்தின் பொருள் வளங்களைப் பகிர்ந்தளித்தல்", "சமதர்மம் (உறுப்பு 31C பாதுகாப்பு)"],
                        ["உறுப்பு 39(c)", "செல்வக் குவிப்பு", "செல்வம்/உற்பத்தி சாதனங்கள் குவிவதைத் தடுக்கும் பொருளாதார அமைப்பு", "சமதர்மம் (உறுப்பு 31C பாதுகாப்பு)"],
                        ["உறுப்பு 39(d)", "சம ஊதியம்", "ஆண், பெண் இருபாலருக்கும் சம வேலைக்கு சம ஊதியம்", "சமதர்மம் (சம ஊதியச் சட்டம்)"],
                        ["உறுப்பு 39(e)", "தொழிலாளர் சுகாதாரம்", "தொழிலாளர்கள் மற்றும் குழந்தைகளின் ஆரோக்கியம்/வலிமை பாதுகாப்பு", "சமதர்மம்"],
                        ["உறுப்பு 39(f)", "குழந்தை வளர்ச்சி", "குழந்தைகள் ஆரோக்கியமான முறையில் வளர்வதற்கான வாய்ப்புகள்", "சமதர்மம் (42வது திருத்தம் 1976)"],
                        ["உறுப்பு 39A", "இலவச சட்ட உதவி", "ஏழைகளுக்குச் சம நீதியும் இலவச சட்ட உதவியும்", "சமதர்மம் (42வது திருத்தம் 1976 / NALSA)"],
                        ["உறுப்பு 40", "கிராம ஊராட்சிகள்", "கிராம ஊராட்சிகளை சுயஆட்சி அலகுகளாக அமைத்தல்", "காந்தியம் (73வது திருத்தம் 1992 பகுதி IX)"],
                        ["உறுப்பு 41", "வேலை & கல்வி", "தகுதியற்ற வறுமை நிலையில் வேலை, கல்வி & பொது உதவி பெறும் உரிமை", "சமதர்மம் (பொருளாதாரத் திறனுக்கு உட்பட்டது)"],
                        ["உறுப்பு 42", "மனிதத்தன்மை வேலை நிலைமை", "நியாயமான, மனிதத்தன்மையுள்ள வேலை நிலைமைகளும் பேறுகால உதவியும்", "சமதர்மம் (பேறுகால நலச் சட்டம் 1961)"],
                        ["உறுப்பு 43", "வாழ்வாதார ஊதியம்", "வாழ்வாதார ஊதியம், கண்ணியமான வாழ்க்கை முறை, ஓய்வு, குடில்தொழில்கள்", "சமதர்மம் / காந்தியம் (KVIC)"],
                        ["உறுப்பு 43A", "தொழிலாளர் மேலாண்மை", "தொழிற்சாலைகள் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பு", "சமதர்மம் (42வது திருத்தம் 1976)"],
                        ["உறுப்பு 43B", "கூட்டுறவுச் சங்கங்கள்", "கூட்டுறவுச் சங்கங்களின் தன்னாட்சி செயல்பாட்டை மேம்படுத்துதல்", "காந்தியம் (97வது திருத்தம் 2011)"],
                        ["உறுப்பு 44", "பொது சிவில் சட்டம்", "இந்தியா முழுவதும் குடிமக்களுக்கான பொது சிவில் சட்டத்தைப் பெறுதல்", "தாராளமயம் (கோவா முன்னுதாரணம்)"],
                        ["உறுப்பு 45", "முன்பருவக் கல்வி", "6 வயதுக்குட்பட்ட குழந்தைகளுக்கான முன்பருவக் பராமரிப்பும் கல்வியும்", "தாராளமயம் (86வது திருத்தம் 2002)"],
                        ["உறுப்பு 46", "எஸ்சி/எஸ்டி நலன்", "எஸ்சி, எஸ்டி & எளிய பிரிவினரின் கல்வி, பொருளாதார நலன்களை மேம்படுத்துதல்", "காந்தியம் / சமதர்மம்"],
                        ["உறுப்பு 47", "சத்துணவு & மதுவிலக்கு", "சத்துணவு/வாழ்க்கை முறை/பொது சுகாதாரத்தை உயர்த்துதல் & மதுவிலக்கு", "சமதர்மம் / காந்தியம்"],
                        ["உறுப்பு 48", "அறிவியல் விவசாயம்", "அறிவியல் விவசாயம்/கால்நடை வளர்ப்பு, இனம் பாதுகாப்பு, பசு வதை தடை", "காந்தியம் / அறிவியல்"],
                        ["உறுப்பு 48A", "சுற்றுச்சூழல் பாதுகாப்பு", "சுற்றுச்சூழல், காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாத்தல்", "தாராளமயம் (42வது திருத்தம் 1976)"],
                        ["உறுப்பு 49", "தேசிய நினைவிடங்கள்", "தேசிய முக்கியத்துவம் வாய்ந்த நினைவிடங்கள், இடங்களைப் பாதுகாத்தல்", "தாராளமயம் (ASI / AMASR)"],
                        ["உறுப்பு 50", "நீதித்துறை பிரிப்பு", "மாநிலத்தின் பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரித்தல்", "தாராளமயம் (CrPC 1973)"],
                        ["உறுப்பு 51", "சர்வதேச அமைதி", "சர்வதேச அமைதி, பாதுகாப்பு, ஒப்பந்த மரிப்பு & நடுவர் மன்றம் மேம்பாடு", "தாராளமயம் (வெளியுறவுக் கொள்கை)"]
                    ]
                }
            ],
            "important_facts": {
                "en": [
                    "Part IV of the Constitution comprises Articles 36 to 51 detailing the Directive Principles of State Policy.",
                    "Article 48 directs scientific agriculture/animal husbandry, cattle breed preservation, and prohibition of cow slaughter (Mirzapur Kureshi 2005).",
                    "Article 48A (Environment, Forests, Wildlife) was inserted by the 42nd Constitutional Amendment Act, 1976.",
                    "Article 48A is a State directive (Part IV); Article 51A(g) is a Citizen Fundamental Duty (Part IV-A).",
                    "Article 49 mandates protection of monuments and places of national importance declared by Parliament by law.",
                    "Article 50 directs separation of Judiciary from Executive in public services (statutorily executed via CrPC 1973).",
                    "Article 51 is the constitutional anchor for India's Foreign Policy (International Peace, Treaty Respect & Arbitration).",
                    "The 3-fold classification into Socialist, Gandhian, and Liberal principles is a CONVENTIONAL ACADEMIC division.",
                    "Champakam Dorairajan (1951) held FRs superior to DPSP; Minerva Mills (1980) established that HARMONY AND BALANCE between Part III and Part IV is a BASIC FEATURE of the Constitution.",
                    "Article 31C protects laws implementing Article 39(b) and Article 39(c) from invalidation under Article 14 and Article 19."
                ],
                "ta": [
                    "அரசியலமைப்பின் பகுதி IV அரசு வழிகாட்டு நெறிமுறைகளை விவரிக்கும் உறுப்புகள் 36 முதல் 51 வரை கொண்டுள்ளது.",
                    "உறுப்பு 48 அறிவியல் விவசாயம்/கால்நடை வளர்ப்பு, இனம் பாதுகாப்பு மற்றும் பசு வதை தடையை வழிகாட்டுகிறது (மிர்சாபூர் குரேஷி 2005).",
                    "உறுப்பு 48A (சுற்றுச்சூழல், காடுகள், வனவிலங்குகள்) 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இணைக்கப்பட்டது.",
                    "உறுப்பு 48A என்பது அரசு வழிகாட்டுதல் (பகுதி IV); உறுப்பு 51A(g) என்பது குடிமகன் அடிப்படைக் கடமை (பகுதி IV-A).",
                    "உறுப்பு 49 நாடாளுமன்றச் சட்டத்தால் தேசிய முக்கியத்துவம் வாய்ந்தது என அறிவிக்கப்பட்ட நினைவிடங்களைப் பாதுகாப்பதைக் கட்டாயமாக்குகிறது.",
                    "உறுப்பு 50 பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க வழிகாட்டுகிறது (CrPC 1973 மூலம் நிறைவேற்றப்பட்டது).",
                    "உறுப்பு 51 இந்தியாவின் வெளியுறவுக் கொள்கைக்கான அரசியலமைப்பு நங்கூரமாகும் (சர்வதேச அமைதி, ஒப்பந்த மரிப்பு & நடுவர் மன்றம்).",
                    "சமதர்ம, காந்திய மற்றும் தாராளமயப் பிரிவுகளாகப் பிரிப்பது ஒரு மரபுவழி கல்வி வகைபாடாகும்.",
                    "செண்பகம் துரைராஜன் (1951) FR-கள் DPSP-ஐ விட மேலானவை என்றது; மினர்வா மில்ஸ் (1980) பகுதி III மற்றும் பகுதி IV இடையிலான இணக்கமும் சமநிலையும் அடிப்படை அம்சம் என நிறுவியது.",
                    "உறுப்பு 31C உறுப்பு 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்களை உறுப்புகள் 14 மற்றும் 19-லிருந்து பாதுகாக்கிறது."
                ]
            },
            "tnpsc_traps": [
                {
                    "title": "1. Article 48 vs Article 48A Trap (உறுப்பு 48 vs 48A பொறி)",
                    "points": {
                        "en": [
                            "Article 48 (Agriculture, animal husbandry, cow slaughter prohibition) was in the ORIGINAL 1950 Constitution text.",
                            "Article 48A (Environment, forests, wildlife protection) was ADDED by the 42nd Constitutional Amendment Act, 1976."
                        ],
                        "ta": [
                            "உறுப்பு 48 (விவசாயம், கால்நடை வளர்ப்பு, பசு வதை தடை) அசல் 1950 அரசியலமைப்பு உரையில் இருந்தது.",
                            "உறுப்பு 48A (சுற்றுச்சூழல், காடுகள், வனவிலங்குகள் பாதுகாப்பு) 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது."
                        ]
                    }
                },
                {
                    "title": "2. Article 48A vs Article 51A(g) Trap (உறுப்பு 48A vs 51A(g) பொறி)",
                    "points": {
                        "en": [
                            "Article 48A is a DPSP under Part IV directing the STATE to protect environment and wildlife.",
                            "Article 51A(g) is a Fundamental Duty under Part IV-A directing EVERY CITIZEN to protect natural environment and wildlife."
                        ],
                        "ta": [
                            "உறுப்பு 48A என்பது பகுதி IV-ன் கீழ் உள்ள DPSP ஆகும், இது சுற்றுச்சூழலையும் வனவிலங்குகளையும் பாதுகாக்குமாறு அரசுக்கு ஆணையிடுகிறது.",
                            "உறுப்பு 51A(g) என்பது பகுதி IV-A-ன் கீழ் உள்ள அடிப்படைக் கடமை ஆகும், இது இயற்கைச் சூழலையும் வனவிலங்குகளையும் பாதுகாக்குமாறு ஒவ்வொரு குடிமகனுக்கும் ஆணையிடுகிறது."
                        ]
                    }
                },
                {
                    "title": "3. Article 50 Separation Trap (உறுப்பு 50 அதிகாரப் பிரிப்புப் பொறி)",
                    "points": {
                        "en": [
                            "Article 50 directs separation of judiciary from executive 'in the public services of the State'.",
                            "The Indian Constitution does NOT adopt a rigid, absolute separation of powers like the US Constitution; India follows Parliamentary Democracy with checks and balances!"
                        ],
                        "ta": [
                            "உறுப்பு 50 'மாநிலத்தின் பொது சேவைகளில்' நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க வழிகாட்டுகிறது.",
                            "இந்திய அரசியலமைப்பு அமெரிக்க அரசியலமைப்பு போன்ற கடுமையான, முற்றுமுழுதான அதிகாரப் பிரிப்பை ஏற்கவில்லை; இந்தியா கட்டுப்பாடுகள் மற்றும் சமநிலைகளுடன் கூடிய நாடாளுமன்ற ஜனநாயகத்தைப் பின்பற்றுகிறது!"
                        ]
                    }
                },
                {
                    "title": "4. Article 51 vs Article 51A Trap (உறுப்பு 51 vs 51A பொறி)",
                    "points": {
                        "en": [
                            "Article 51 is the LAST article of Part IV (DPSP), guiding State Foreign Policy & International Peace.",
                            "Article 51A is Part IV-A (Fundamental Duties of Citizens), added by 42nd Amendment 1976."
                        ],
                        "ta": [
                            "உறுப்பு 51 என்பது பகுதி IV-ன் (DPSP) கடைசி உறுப்பாகும், இது அரசின் வெளியுறவுக் கொள்கை & சர்வதேச அமைதியை வழிகாட்டுகிறது.",
                            "உறுப்பு 51A என்பது பகுதி IV-A (குடிமக்களின் அடிப்படைக் கடமைகள்), இது 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது."
                        ]
                    }
                },
                {
                    "title": "5. Minerva Mills Basic Structure Balance Trap (மினர்வா மில்ஸ் அடிப்படை அமைப்புப் பொறி)",
                    "points": {
                        "en": [
                            "Minerva Mills (1980) declared that HARMONY AND BALANCE between Part III (FRs) and Part IV (DPSP) is a Basic Feature of the Constitution.",
                            "Do NOT state that all DPSPs override Fundamental Rights! Only laws implementing Article 39(b) and 39(c) take precedence over Articles 14 and 19 under Article 31C."
                        ],
                        "ta": [
                            "பகுதி III (FR) மற்றும் பகுதி IV (DPSP) இடையிலான இணக்கமும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அம்சம் என மினர்வா மில்ஸ் (1980) அறிவித்தது.",
                            "அனைத்து DPSP-களும் அடிப்படை உரிமைகளை மிஞ்சுகின்றன என்று கூற வேண்டாம்! உறுப்பு 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்கள் மட்டுமே உறுப்பு 31C-ன் கீழ் உறுப்புகள் 14 மற்றும் 19-ஐ விட மேலோங்குகின்றன."
                        ]
                    }
                },
                {
                    "title": "6. DPSP Conventional Classification Trap (DPSP மரபுவழி வகைப்பாட்டுப் பொறி)",
                    "points": {
                        "en": [
                            "The division into Socialist, Gandhian, and Liberal-Intellectual categories is NOT explicitly written in the Constitution.",
                            "It is a conventional academic classification used by constitutional experts for systematic study."
                        ],
                        "ta": [
                            "DPSP-ஐ சமதர்ம, காந்திய மற்றும் தாராளமய-அறிவுசார் பிரிவுகளாகப் பிரிப்பது அரசியலமைப்பில் வெளிப்படையாக எழுதப்படவில்லை.",
                            "இது முறைப்படுத்தப்பட்ட படிப்பிற்காக அரசியலமைப்பு வல்லுநர்களால் பயன்படுத்தப்படும் ஒரு மரபுவழி கல்வி வகைபாடாகும்."
                        ]
                    }
                }
            ],
            "mind_map": [
                {
                    "title": "Directive Principles of State Policy – Complete Master Map (Part IV)",
                    "short_label": "DPSP Complete Map",
                    "children": [
                        {
                            "title": "Part 3 Directives (Articles 48 to 51)",
                            "short_label": "Arts 48-51",
                            "children": [
                                {
                                    "title": "Article 48: Agriculture, Animal Husbandry & Cattle Breed Preservation/Slaughter Ban",
                                    "short_label": "Art 48 Agriculture"
                                },
                                {
                                    "title": "Article 48A: Environment, Forests & Wildlife Protection (42nd CAA 1976)",
                                    "short_label": "Art 48A Environment"
                                },
                                {
                                    "title": "Article 49: National Monuments & Historic Places Protection (ASI / AMASR 1958)",
                                    "short_label": "Art 49 Monuments"
                                },
                                {
                                    "title": "Article 50: Separation of Judiciary from Executive in Public Services (CrPC 1973)",
                                    "short_label": "Art 50 Judiciary Sep"
                                },
                                {
                                    "title": "Article 51: International Peace, Security, Treaty Respect & Arbitration",
                                    "short_label": "Art 51 Foreign Policy"
                                }
                            ]
                        },
                        {
                            "title": "FR (Part III) vs DPSP (Part IV) Integration",
                            "short_label": "FR vs DPSP",
                            "children": [
                                {
                                    "title": "Champakam Dorairajan (1951): FRs Superior to DPSP",
                                    "short_label": "1951 Champakam"
                                },
                                {
                                    "title": "Re Kerala Education Bill (1958): Harmonious Construction",
                                    "short_label": "1958 Harmonious"
                                },
                                {
                                    "title": "Kesavananda Bharati (1973): Art 31C Part 1 Valid (Art 39b/c priority over 14/19)",
                                    "short_label": "1973 Kesavananda"
                                },
                                {
                                    "title": "Minerva Mills (1980): Harmony & Balance between Part III & IV is Basic Feature",
                                    "short_label": "1980 Minerva Mills"
                                }
                            ]
                        },
                        {
                            "title": "Master Ideological Classification (Articles 36–51)",
                            "short_label": "Ideologies",
                            "children": [
                                {
                                    "title": "Socialist: Arts 38, 39, 39A, 41, 42, 43, 43A, 47",
                                    "short_label": "Socialist"
                                },
                                {
                                    "title": "Gandhian: Arts 40, 43, 43B, 46, 47, 48",
                                    "short_label": "Gandhian"
                                },
                                {
                                    "title": "Liberal-Intellectual: Arts 44, 45, 48, 48A, 49, 50, 51",
                                    "short_label": "Liberal"
                                }
                            ]
                        }
                    ]
                }
            ],
            "quick_revision": {
                "en": [
                    "Part IV of the Constitution contains Articles 36 to 51 detailing the Directive Principles of State Policy, borrowed from the Irish Constitution of 1937.",
                    "Objective: To establish a Welfare State and secure Social and Economic Democracy.",
                    "Article 36 adopts the definition of 'State' from Article 12 (Part III).",
                    "Article 37 explicitly declares DPSP non-justiciable by courts, but FUNDAMENTAL in governance of the country.",
                    "Article 38 mandates a Social Order for welfare; Article 38(2) (added by 44th CAA 1978) directs minimising inequalities.",
                    "Article 39(a)-(f) commands adequate livelihood, material resources distribution, wealth concentration prevention, equal pay for equal work, worker health, and child development.",
                    "Article 39A (Free Legal Aid) was added by 42nd CAA 1976 (implemented statutorily via NALSA Act 1987).",
                    "Article 40 (Village Panchayats) received constitutional status via 73rd CAA 1992 (Part IX, 11th Schedule).",
                    "Article 41 (Right to work/education) is subject to State economic capacity; Article 42 mandates humane work conditions & maternity relief; Article 43 commands living wage & rural cottage industries.",
                    "Article 43A (Workers' participation in management) was added by 42nd CAA 1976; Article 43B (Co-operatives) was added by 97th CAA 2011.",
                    "Article 44 directs securing a Uniform Civil Code (UCC) for all citizens (Goa Civil Code 1867 precedent).",
                    "Article 45 was substituted by 86th CAA 2002 to cover early childhood care & education for children BELOW 6 YEARS (Age 6-14 education shifted to Art 21A FR).",
                    "Article 46 directs special care for educational/economic interests of SCs, STs & weaker sections.",
                    "Article 47 mandates raising nutrition/living standards/public health and prohibition of intoxicating drinks except medicinal use.",
                    "Article 48 directs scientific agriculture, animal husbandry, breed preservation & cow slaughter prohibition (Mirzapur Kureshi 2005).",
                    "Article 48A (Environment, forests, wildlife protection) was added by 42nd CAA 1976 (State duty, distinct from Art 51A(g) citizen duty).",
                    "Article 49 directs protection of national monuments declared by Parliament by law.",
                    "Article 50 directs separation of judiciary from executive in public services of the State (executed via CrPC 1973).",
                    "Article 51 directs promotion of international peace, security, treaty respect & arbitration (Foreign Policy DPSP anchor).",
                    "Minerva Mills (1980) established that the HARMONY AND BALANCE between Part III (FRs) and Part IV (DPSP) is a BASIC FEATURE of the Constitution."
                ],
                "ta": [
                    "அரசியலமைப்பின் பகுதி IV-ல் 1937 அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்ட அரசு வழிகாட்டு நெறிமுறைகளைக் கூறும் உறுப்புகள் 36 முதல் 51 வரை உள்ளன.",
                    "நோக்கம்: ஒரு நல அரசை நிறுவுவது மற்றும் சமூக மற்றும் பொருளாதார ஜனநாயகத்தைப் பாதுகாப்பது.",
                    "உறுப்பு 36 பகுதி III உறுப்பு 12-ல் கொடுக்கப்பட்ட 'அரசு' வரையறையை ஏற்கிறது.",
                    "உறுப்பு 37 DPSP நீதிமன்றங்களால் அமல்படுத்த முடியாதது, ஆனால் நாட்டின் ஆட்சியில் அடிப்படையானது என வெளிப்படையாக அறிவிக்கிறது.",
                    "உறுப்பு 38 நலனுக்கான சமூக ஒழுங்கை கட்டாயமாக்குகிறது; 44வது திருத்தம் 1978 மூலம் சேர்க்கப்பட்ட 38(2) சமத்துவமின்மையைக் குறைக்க ஆணையிடுகிறது.",
                    "உறுப்பு 39(a)-(f) போதுமான வாழ்வாதாரம், பொருள் வளப் பகிர்வு, செல்வக் குவிப்புத் தடை, சம வேலைக்கு சம ஊதியம், தொழிலாளர் சுகாதாரம் மற்றும் குழந்தை வளர்ச்சியை ஆணையிடுகிறது.",
                    "உறுப்பு 39A (இலவச சட்ட உதவி) 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது (1987 NALSA சட்டம் மூலம் செயல்படுத்தப்பட்டது).",
                    "உறுப்பு 40 (கிராம ஊராட்சிகள்) 1992-ன் 73வது திருத்தம் (பகுதி IX, 11வது அட்டவணை) மூலம் அரசியலமைப்பு அந்தஸ்தைப் பெற்றது.",
                    "உறுப்பு 41 (வேலை/கல்வி உரிமை) அரசின் பொருளாதாரத் திறனுக்கு உட்பட்டது; உறுப்பு 42 மனிதத்தன்மை வேலை நிலைமைகள் & பேறுகால உதவியைக் கட்டாயமாக்குகிறது; உறுப்பு 43 வாழ்வாதார ஊதியம் & குடில்தொழில்களைக் கட்டாயமாக்குகிறது.",
                    "உறுப்பு 43A (மேலாண்மையில் தொழிலாளர்கள் பங்கேற்பு) 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது; உறுப்பு 43B (கூட்டுறவு) 97வது திருத்தம் 2011 மூலம் சேர்க்கப்பட்டது.",
                    "உறுப்பு 44 இந்தியா முழுவதும் அனைத்துக் குடிமக்களுக்கும் ஒரு பொது சிவில் சட்டத்தைப் பெற வழிகாட்டுகிறது (கோவா முன்னுதாரணம்).",
                    "உறுப்பு 45 86வது திருத்தம் 2002 மூலம் மாற்றியமைக்கப்பட்டு 6 வயதுக்குட்பட்ட குழந்தைகளுக்கான முன்பருவக் பராமரிப்பை உள்ளடக்குகிறது (6-14 வயதுக் கல்வி உறுப்பு 21A FR-க்கு மாற்றப்பட்டது).",
                    "உறுப்பு 46 எஸ்சி, எஸ்டி & எளிய பிரிவினரின் கல்வி மற்றும் பொருளாதார நலன்களை மேம்படுத்த வழிகாட்டுகிறது.",
                    "உறுப்பு 47 சத்துணவு, வாழ்க்கை முறை, பொது சுகாதாரத்தை உயர்த்துவதையும் மருத்துவ பயன்பாடு தவிர போதைப் பானங்கள் மதுவிலக்கையும் கட்டாயமாக்குகிறது.",
                    "உறுப்பு 48 அறிவியல் விவசாயம், கால்நடை வளர்ப்பு, இனம் பாதுகாப்பு & பசு வதை தடையை வழிகாட்டுகிறது (மிர்சாபூர் குரேஷி 2005).",
                    "உறுப்பு 48A (சுற்றுச்சூழல், காடுகள், வனவிலங்குகள் பாதுகாப்பு) 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது (அரசு கடமை, குடிமகன் கடமையான 51A(g)-லிருந்து வேறுபட்டது).",
                    "உறுப்பு 49 நாடாளுமன்றச் சட்டத்தால் அறிவிக்கப்பட்ட தேசிய முக்கியத்துவம் வாய்ந்த நினைவிடங்களைப் பாதுகாப்ப வழிகாட்டுகிறது.",
                    "உறுப்பு 50 பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க வழிகாட்டுகிறது (CrPC 1973 மூலம் நிறைவேற்றப்பட்டது).",
                    "உறுப்பு 51 சர்வதேச அமைதி, பாதுகாப்பு, ஒப்பந்த மரிப்பு & நடுவர் மன்றம் மேம்பாட்டிற்கு வழிகாட்டுகிறது (வெளியுறவுக் கொள்கை DPSP).",
                    "பகுதி III (FR) மற்றும் பகுதி IV (DPSP) இடையிலான இணக்கமும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அம்சம் என மினர்வா மில்ஸ் (1980) நிறுவியது."
                ]
            }
        }
    }

    output_dir = "data/notes/polity"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "directive_principles_part_3.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(note_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated DPSP Part 3 Notes at {output_path}")

if __name__ == "__main__":
    create_dpsp_part3_notes()
