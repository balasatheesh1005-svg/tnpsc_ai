# -*- coding: utf-8 -*-
"""
Script to build production-ready bilingual TNPSC Group 1 Notes for:
Fundamental Duties - Part 1
Target File: data/notes/polity/fundamental_duties_part_1.json
"""

import json
import os

notes_data = {
    "meta": {
        "topic_id": "polity_fundamental_duties_part_1",
        "repository_id": "polity_fundamental_duties",
        "display_title": "Fundamental Duties – Part 1",
        "part": 1,
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
            "reading": "35 min",
            "revision": "15 min",
            "total": "50 min"
        }
    },
    "keywords": [
        "Fundamental Duties",
        "அடிப்படை கடமைகள்",
        "Part IVA Constitution",
        "பகுதி IVA அரசியலமைப்பு",
        "Article 51A",
        "உறுப்பு 51A",
        "Swaran Singh Committee",
        "ஸ்வரன் சிங் குழு",
        "42nd Constitutional Amendment 1976",
        "42வது அரசியலமைப்பு திருத்தம் 1976",
        "86th Constitutional Amendment 2002",
        "86வது அரசியலமைப்பு திருத்தம் 2002",
        "Original 10 Duties",
        "அசல் 10 கடமைகள்",
        "11th Duty Article 51Ak",
        "11வது கடமை உறுப்பு 51A(k)",
        "Article 51Aa Constitution Flag Anthem",
        "உறுப்பு 51A(a) அரசியலமைப்பு கொடி கீதம்",
        "Article 51Ab Freedom Ideals",
        "உறுப்பு 51A(b) சுதந்திரப் போராட்ட லட்சியங்கள்",
        "Article 51Ac Sovereignty Unity Integrity",
        "உறுப்பு 51A(c) இறையாண்மை ஒற்றுமை ஒருமைப்பாடு",
        "Article 51Ad Defend Country National Service",
        "உறுப்பு 51A(d) தேசத்தைப் பாதுகாத்தல் தேசிய சேவை",
        "Article 51Ae Harmony Brotherhood Womens Dignity",
        "உறுப்பு 51A(e) நல்லிணக்கம் சகோதரத்துவம் பெண்கள் கண்ணியம்",
        "Non-Justiciable Nature",
        "நீதிமன்றத்தால் அமல்படுத்த முடியாத இயல்பு",
        "Article 21A vs Article 51Ak",
        "உறுப்பு 21A vs உறுப்பு 51A(k)",
        "Bijoe Emmanuel Case National Anthem",
        "பிஜோய் இம்மானுவேல் வழக்கு தேசிய கீதம்"
    ],
    "learning_outcomes": {
        "Understand": {
            "en": [
                "Understand the origin, philosophy, and constitutional status of Fundamental Duties in Part IVA (Article 51A).",
                "Understand the recommendations of Swaran Singh Committee (1976) and distinguish between accepted and rejected proposals.",
                "Understand the impact of 42nd Amendment (1976) [added 10 duties] and 86th Amendment (2002) [added 11th duty].",
                "Understand the detailed breakdown of the first 5 Fundamental Duties: Article 51A(a) to 51A(e)."
            ],
            "ta": [
                "பகுதி IVA (உறுப்பு 51A) ல் உள்ள அடிப்படை கடமைகளின் தோற்றம், தத்துவம் மற்றும் அரசியலமைப்பு நிலையைப் புரிந்து கொள்ளுதல்.",
                "ஸ்வரன் சிங் குழுவின் (1976) பரிந்துரைகளைப் புரிந்து கொண்டு ஏற்றுக்கொள்ளப்பட்ட மற்றும் நிராகரிக்கப்பட்ட பரிந்துரைகளை வேறுபடுத்துதல்.",
                "42வது திருத்தம் (1976) [10 கடமைகள் சேர்க்கப்பட்டன] மற்றும் 86வது திருத்தம் (2002) [11வது கடமை சேர்க்கப்பட்டது] ஆகியவற்றின் தாக்கத்தைப் புரிந்து கொள்ளுதல்.",
                "முதல் 5 அடிப்படை கடமைகளின் விரிவான பிரிவைப் புரிந்து கொள்ளுதல்: உறுப்பு 51A(a) முதல் 51A(e) வரை."
            ]
        },
        "Remember": {
            "en": [
                "Remember that Fundamental Duties were NOT present in the original 1950 Constitution.",
                "Remember that Part IVA and Article 51A were inserted by the 42nd Constitutional Amendment Act, 1976.",
                "Remember that Swaran Singh Committee recommended 8 duties, but the 42nd CAA enacted 10 duties.",
                "Remember that the duty to pay taxes and penalties for non-performance were NOT included in Article 51A.",
                "Remember the exact distinction between Article 21A (FR - State duty) and Article 51A(k) (FD - Parent duty)."
            ],
            "ta": [
                "அசல் 1950 அரசியலமைப்பில் அடிப்படை கடமைகள் இடம்பெறவில்லை என்பதை நினைவில் கொள்ளுதல்.",
                "பகுதி IVA மற்றும் உறுப்பு 51A ஆகியவை 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டன என்பதை நினைவில் கொள்ளுதல்.",
                "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் 42வது திருத்தம் 10 கடமைகளை இயற்றியது என்பதை நினைவில் கொள்ளுதல்.",
                "வரி செலுத்தும் கடமை மற்றும் கடமை தவறியதற்கான தண்டனை ஆகியவை உறுப்பு 51A-ல் சேர்க்கப்படவில்லை என்பதை நினைவில் கொள்ளுதல்.",
                "உறுப்பு 21A (அடிப்படை உரிமை - அரசு கடமை) மற்றும் உறுப்பு 51A(k) (அடிப்படை கடமை - பெற்றோர் கடமை) இடையேயான சரியான வேறுபாட்டை நினைவில் கொள்ளுதல்."
            ]
        },
        "Analyze": {
            "en": [
                "Analyze the constitutional synergy between Fundamental Rights (Part III), DPSP (Part IV), and Fundamental Duties (Part IVA).",
                "Analyze the legal significance of non-justiciability and how Parliament enacts statutes to enforce duties.",
                "Analyze landmark judicial rulings like Bijoe Emmanuel (1986) and AIIMS Students Union (2002) regarding Article 51A(a).",
                "Analyze the conceptual difference between Sovereignty, Unity, and Integrity under Article 51A(c)."
            ],
            "ta": [
                "அடிப்படை உரிமைகள் (பகுதி III), DPSP (பகுதி IV) மற்றும் அடிப்படை கடமைகள் (பகுதி IVA) இடையேயான அரசியலமைப்பு ஒருங்கிணைப்பை பகுப்பாய்வு செய்தல்.",
                "நீதிமன்றத்தால் நேரடியாக அமல்படுத்த முடியாத இயல்பின் சட்ட முக்கியத்துவத்தையும் நாடாளுமன்றம் கடமைகளை அமல்படுத்த சட்டங்களை எவ்வாறு இயற்றுகிறது என்பதையும் பகுப்பாய்வு செய்தல்.",
                "பிஜோய் இம்மானுவேல் (1986) மற்றும் AIIMS மாணவர் சங்கம் (2002) போன்ற முக்கிய நீதிமன்றத் தீர்ப்புகளை பகுப்பாய்வு செய்தல்.",
                "உறுப்பு 51A(c)-ன் கீழ் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு இடையேயான தத்துவார்த்த வேறுபாட்டை பகுப்பாய்வு செய்தல்."
            ]
        },
        "Apply": {
            "en": [
                "Apply TNPSC trap points to correctly answer tricky MCQs on Swaran Singh recommendations vs 42nd Amendment text.",
                "Differentiate constitutional civic obligations from statutory civic duties in statement-based items.",
                "Accurately match Article 51A sub-clauses (a) to (e) with their core keywords in Match the Following questions."
            ],
            "ta": [
                "ஸ்வரன் சிங் பரிந்துரைகள் vs 42வது திருத்த உரை பற்றிய வினாக்களுக்குச் சரியாகப் பதிலளிக்க டிஎன்பிஎஸ்சி பொறி புள்ளிகளைப் பயன்படுத்துதல்.",
                "அரசியலமைப்பு குடிமைப் பொறுப்புகளையும் சட்டப்பூர்வ குடிமைப் பொறுப்புகளையும் கூற்று வினாக்களில் வேறுபடுத்துதல்.",
                "பொருத்துக வினாக்களில் உறுப்பு 51A உட்பிரிவுகள் (a) முதல் (e) வரையிலானவற்றை அவற்றின் முக்கிய வார்த்தைகளுடன் சரியாகப் பொருத்துதல்."
            ]
        }
    },
    "subject": "Polity",
    "topic": "Fundamental Duties – Part 1",
    "language": "bilingual",
    "ui_type": "polity",
    "sections": [
        {
            "id": "sec_fd_overview",
            "title_en": "1. Fundamental Duties: Overview, Purpose & Constitutional Location",
            "title_ta": "1. அடிப்படை கடமைகள்: கண்ணோட்டம், நோக்கம் & அரசியலமைப்பு இடம்",
            "type": "standard_topic"
        },
        {
            "id": "sec_constitutional_history",
            "title_en": "2. Constitutional History & Evolution (1950 to 2002)",
            "title_ta": "2. அரசியலமைப்பு வரலாறும் வளர்ச்சியும் (1950 முதல் 2002 வரை)",
            "type": "standard_topic"
        },
        {
            "id": "sec_swaran_singh",
            "title_en": "3. Swaran Singh Committee (Recommendations vs Actual Provisions)",
            "title_ta": "3. ஸ்வரன் சிங் குழு (பரிந்துரைகள் vs அசல் அரசியலமைப்பு விதிகள்)",
            "type": "standard_topic"
        },
        {
            "id": "sec_article_51a_structure",
            "title_en": "4. Article 51A Structure: First Group of Duties (51A(a) to 51A(e))",
            "title_ta": "4. உறுப்பு 51A அமைப்பு: முதற்கட்டக் கடமைகள் (51A(a) முதல் 51A(e) வரை)",
            "type": "standard_topic"
        },
        {
            "id": "sec_conceptual_distinctions",
            "title_en": "5. Important Conceptual Distinctions (FR vs DPSP vs FD)",
            "title_ta": "5. முக்கிய தத்துவார்த்த வேறுபாடுகள் (அடிப்படை உரிமைகள் vs DPSP vs அடிப்படை கடமைகள்)",
            "type": "standard_topic"
        },
        {
            "id": "sec_justiciability_enforcement",
            "title_en": "6. Justiciability, Legal Enforcement & Statutory Support",
            "title_ta": "6. நீதிமன்ற அமலாக்க இயல்பு, சட்டப்பூர்வ அமலாக்கம் & ஆதரவுச் சட்டங்கள்",
            "type": "standard_topic"
        },
        {
            "id": "sec_cases_legal_context",
            "title_en": "7. Landmark Judicial Cases & Constitutional Principles",
            "title_ta": "7. முக்கிய மைல்கல் வழக்குத் தீர்ப்புகள் & அரசியலமைப்பு தத்துவங்கள்",
            "type": "standard_topic"
        },
        {
            "id": "sec_amendments",
            "title_en": "8. Constitutional Amendments (42nd CAA 1976 & 86th CAA 2002)",
            "title_ta": "8. அரசியலமைப்பு திருத்தங்கள் (42வது திருத்தம் 1976 & 86வது திருத்தம் 2002)",
            "type": "standard_topic"
        },
        {
            "id": "sec_traps_revision",
            "title_en": "9. TNPSC Traps, Comparison Framework & High-Yield Revision",
            "title_ta": "9. டிஎன்பிஎஸ்சி பொறிகள், ஒப்பீட்டு அமைப்பும் முக்கிய திருப்புதலும்",
            "type": "standard_topic"
        }
    ],
    "content": {
        "definition": {
            "en": "Fundamental Duties are moral and civic obligations enshrined in Part IVA (Article 51A) of the Constitution of India, commanding citizens to respect national symbols, uphold national integrity, defend the country, promote brotherhood, and preserve national culture. Added by the 42nd Constitutional Amendment Act 1976 based on Swaran Singh Committee recommendations and expanded by the 86th Amendment Act 2002, they serve as non-justiciable reminders of responsible citizenship complementing Fundamental Rights.",
            "ta": "அடிப்படை கடமைகள் என்பது இந்திய அரசியலமைப்பின் பகுதி IVA (உறுப்பு 51A) ல் பொறிக்கப்பட்டுள்ள தர்ம நெறி மற்றும் குடிமைப் பொறுப்புகள் ஆகும். இவை தேசிய சின்னங்களைக் மதிப்பதோடு, தேசிய ஒருமைப்பாட்டைப் பேணவும், தேசத்தைப் பாதுகாக்கவும், சகோதரத்துவத்தை வளர்க்கவும், கலாச்சாரத்தைப் பாதுகாக்கவும் குடிமக்களுக்கு ஆணையிடுகின்றன. ஸ்வரன் சிங் குழுவின் பரிந்துரைகளின் அடிப்படையில் 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டு, 2002-ன் 86வது திருத்தத்தால் விரிவாக்கப்பட்ட இவை, அடிப்படை உரிமைகளுடன் இணைந்து பொறுப்பான குடியுரிமையை நினைவூட்டும் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாத கடமைகளாகச் செயல்படுகின்றன."
        },
        "introduction": {
            "en": "Part 1 of the Fundamental Duties series provides a comprehensive foundation of Part IVA of the Constitution of India. It exhaustively covers the conceptual framework of Article 51A, constitutional history from 1950 to 2002, Swaran Singh Committee recommendations vs actual 42nd Amendment provisions, detailed breakdown of Articles 51A(a) through 51A(e), legal enforcement mechanisms, landmark judicial decisions, 8 mandatory comparison tables, mind map, bilingual TNPSC trap points, and a 2-minute rapid revision module.",
            "ta": "அடிப்படை கடமைகள் தொடரின் பகுதி 1, இந்திய அரசியலமைப்பின் பகுதி IVA இன் முழுமையான அடித்தளத்தை வழங்குகிறது. இது உறுப்பு 51A இன் தத்துவார்த்த அமைப்பு, 1950 முதல் 2002 வரையிலான அரசியலமைப்பு வளர்ச்சி, ஸ்வரன் சிங் குழு பரிந்துரைகள் vs அசல் 42வது திருத்த விதிகள், உறுப்புகள் 51A(a) முதல் 51A(e) வரையிலான விரிவான விளக்கம், சட்டப்பூர்வ அமலாக்க வழிமுறைகள், முக்கிய நீதிமன்றத் தீர்ப்புகள், 8 கட்டாய ஒப்பீட்டு அட்டவணைகள், மன வரைபடம், இருமொழி டிஎன்பிஎஸ்சி பொறி புள்ளிகள் மற்றும் 2 நிமிட விரைவு திருப்புதல் தொகுதியை விரிவாக உள்ளடக்கியுள்ளது."
        },
        "sec_fd_overview": [
            {
                "title": "1. Meaning & Concept of Fundamental Duties (அடிப்படை கடமைகளின் பொருளும் தத்துவமும்)",
                "points": {
                    "en": [
                        "Definition: Fundamental Duties are moral and civic obligations expected from every citizen of India to foster constitutional patriotism, national discipline, and social harmony.",
                        "Constitutional Location: Enshrined in Part IVA, consisting of a single Article—Article 51A.",
                        "Inspiration: Inspired by the Constitution of the USSR (former Soviet Union). While most democratic constitutions (like USA, Canada, Australia) emphasize rights over duties, socialist constitutions emphasize duties equally. Exception: Japan is one of the very few democratic countries having explicit duties.",
                        "Nature & Scope: Fundamental Duties apply ONLY to citizens of India. Unlike certain Fundamental Rights (e.g., Art 14, Art 21) which extend to foreigners, Fundamental Duties DO NOT apply to aliens/foreigners.",
                        "Non-Justiciable Nature: FDs are non-justiciable in nature. There is no direct constitutional writ provision (like Art 32 or 226) to punish a citizen for simple non-performance of a Fundamental Duty, unless Parliament has enacted a specific law enforcing it."
                    ],
                    "ta": [
                        "வரையறை: அடிப்படை கடமைகள் என்பது அரசியலமைப்பு தேசபக்தி, தேசிய ஒழுக்கம் மற்றும் சமூக நல்லிணக்கத்தை வளர்ப்பதற்காக இந்தியாவின் ஒவ்வொரு குடிமகனிடமிருந்தும் எதிர்பார்க்கப்படும் தர்ம நெறி மற்றும் குடிமைப் பொறுப்புகள் ஆகும்.",
                        "அரசியலமைப்பு இடம்: பகுதி IVA-ல், உறுப்பு 51A என்ற ஒரே ஒரு உறுப்பைக் கொண்டு பொறிக்கப்பட்டுள்ளது.",
                        "அனுபவம்/தோற்றுவாய்: முன்னாள் சோவியத் யூனியன் (USSR) அரசியலமைப்பிலிருந்து ஈர்க்கப்பட்டது. பெரும்பாலான ஜனநாயக அரசியலமைப்புகள் (அமெரிக்கா, கனடா, ஆஸ்திரேலியா போன்றவை) கடமைகளை விட உரிமைகளுக்கே முக்கியத்துவம் அளிக்கும் நிலையில், சமதர்ம அரசியலமைப்புகள் கடமைகளுக்கும் சம முக்கியத்துவம் அளிக்கின்றன. விதிவிலக்கு: ஜப்பான் வெளிப்படையான கடமைகளைக் கொண்ட மிகச்சில ஜனநாயக நாடுகளில் ஒன்றாகும்.",
                        "இயல்பும் எல்லையும்: அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும். சில அடிப்படை உரிமைகள் (எ.கா. உறுப்பு 14, உறுப்பு 21) வெளிநாட்டினருக்கும் பொருந்தும் நிலையில், அடிப்படை கடமைகள் வெளிநாட்டினருக்குப் பொருந்தாது.",
                        "நீதிமன்றத்தால் அமல்படுத்த முடியாத இயல்பு: DPSP போலவே அடிப்படை கடமைகளும் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாதவை. நாடாளுமன்றம் ஒரு குறிப்பிட்ட சட்டத்தை இயற்றாவிட்டால், ஒரு குடிமகன் அடிப்படை கடமையை செய்யத் தவறினால் அவரைத் தண்டிக்க நேரடியாக அரசியலமைப்பு பேராணை வழிவகை இல்லை."
                    ]
                }
            },
            {
                "title": "2. Purpose & Importance of Fundamental Duties (அடிப்படை கடமைகளின் நோக்கமும் முக்கியத்துவமும்)",
                "points": {
                    "en": [
                        "Reminder to Citizens: While enjoying Fundamental Rights, citizens must remember that they also owe duties to their nation, society, and fellow citizens.",
                        "Warning Against Anti-National Activities: They serve as a warning against anti-national and unconstitutional activities such as burning the national flag or destroying public property.",
                        "Source of Inspiration: They inspire citizens and promote a sense of commitment and active participation in national building rather than being passive spectators.",
                        "Correlative Nature of Rights & Duties: Rights and duties are correlative and inseparable. As Mahatma Gandhi remarked: 'The true source of rights is duty. If we all discharge our duties, rights will not be far to seek.'",
                        "Role in Judicial Interpretation: Supreme Court ruled that FDs help courts in examining and determining the constitutional validity of any law. If a law seeks to give effect to a Fundamental Duty, it may be considered 'reasonable' under Art 19."
                    ],
                    "ta": [
                        "குடிமக்களுக்கு நினைவூட்டல்: அடிப்படை உரிமைகளை ಅನುபவிக்கும் போது, குடிமக்கள் தங்கள் தேசம், சமூகம் மற்றும் சக குடிமக்களுக்குக் கடமைப்பட்டுள்ளனர் என்பதை நினைவூட்டுகின்றன.",
                        "தேசவிரோத நடவடிக்கைகளுக்கு எச்சரிக்கை: தேசியக் கொடியை எரிப்பது அல்லது பொதுச் சொத்துக்களை சேதப்படுத்துவது போன்ற தேசவிரோத மற்றும் அரசியலமைப்பிற்கு எதிரான நடவடிக்கைகளுக்கு எதிரான எச்சரிக்கையாகச் செயல்படுகின்றன.",
                        "அனுபவ ஊக்கம்: குடிமக்களை வெறும் பார்வையாளர்களாக இல்லாமல், தேசத்தைக் கட்டியெழுப்புவதில் தீவிரமாகப் பங்கேற்கவும் அர்ப்பணிப்பு உணர்வை வளர்க்கவும் தூண்டுகின்றன.",
                        "உரிமைகள் & கடமைகளின் தொடர்பு: உரிமைகளும் கடமைகளும் ஒன்றோடொன்று தொடர்புடையவை மற்றும் பிரிக்க முடியாதவை. மகாத்மா காந்தி குறிப்பிட்டது போல: 'உரிமைகளின் உண்மையான ஊற்றுக்கண் கடமையாகும். நாம் அனைவரும் நம் கடமைகளைச் செய்தால், உரிமைகள் தொலைவில் இருக்காது.'",
                        "நீதிமன்ற விளக்கத்தில் பங்கு: எந்தவொரு சட்டத்தின் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை ஆராய்வதற்கும் தீர்மானிப்பதற்கும் FDs நீதிமன்றங்களுக்கு உதவுகின்றன என்று உச்ச நீதிமன்றம் தீர்ப்பளித்துள்ளது. ஒரு சட்டம் அடிப்படை கடமையைச் செயல்படுத்த முயன்றால், அது உறுப்பு 19-ன் கீழ் 'நியாயமானது' எனக் கருதப்படலாம்."
                    ]
                }
            }
        ],
        "sec_constitutional_history": [
            {
                "title": "1. Original Constitution & Absence of Duties (அசல் அரசியலமைப்பும் கடமைகள் இன்மையும்)",
                "points": {
                    "en": [
                        "1950 Original Constitution: Enacted on 26th January 1950, the original Constitution contained Part III (Fundamental Rights) and Part IV (DPSP), but NO separate chapter on Fundamental Duties.",
                        "Framers' Premise: Framers of the Constitution assumed that the citizens of free India would voluntarily perform their duties based on moral consciousness and patriotic values without needing constitutional enumeration.",
                        "Realization in 1970s: Over two decades of working the Constitution revealed that rights without duties led to indiscipline and disregard for national symbols and public order.",
                        "National Emergency Context: Internal Emergency (1975–1977) prompted the ruling government to introduce constitutional duties to stress civic discipline and national responsibility."
                    ],
                    "ta": [
                        "1950 அசல் அரசியலமைப்பு: 1950 ஜனவரி 26 அன்று நடைமுறைக்கு வந்த அசல் அரசியலமைப்பில் பகுதி III (அடிப்படை உரிமைகள்) மற்றும் பகுதி IV (DPSP) ஆகியவை இருந்தன, ஆனால் அடிப்படை கடமைகளுக்குத் தனிப் பகுதி எதுவும் இல்லை.",
                        "உருவாக்கியவர்களின் எண்ணம்: சுதந்திர இந்தியாவின் குடிமக்கள் அரசியலமைப்பில் பட்டியலிடத் தேவையில்லாமல் தார்மீக உணர்வு மற்றும் தேசபக்தி மதிப்புகளின் அடிப்படையில் தங்கள் கடமைகளைத் தாமாகவே செய்வார்கள் என்று அரசியலமைப்பை உருவாக்கியவர்கள் நம்பினர்.",
                        "1970களில் உணர்தல்: அரசியலமைப்பு செயல்பட்ட இரண்டு தசாப்தங்களில், கடமைகள் இல்லாத உரிமைகள் ஒழுங்கீனத்திற்கும் தேசிய சின்னங்கள் மற்றும் பொது ஒழுங்கை மதிக்காமைக்கும் வழிவகுத்தன என்பது உணரப்பட்டது.",
                        "தேசிய அவசரநிலை சூழல்: உள்நாட்டு அவசரநிலை (1975–1977) குடிமை ஒழுக்கம் மற்றும் தேசியப் பொறுப்பை வலியுறுத்த அரசியலமைப்பு கடமைகளை அறிமுகப்படுத்த அன்றைய அரசைத் தூண்டியது."
                    ]
                }
            },
            {
                "title": "2. Evolution from 10 to 11 Duties (10-லிருந்து 11 கடமைகளாக வளர்ச்சி)",
                "points": {
                    "en": [
                        "42nd Constitutional Amendment Act, 1976: Incorporated Part IVA and Article 51A into the Constitution, introducing the ORIGINAL 10 Fundamental Duties on 4th December 1976 (effective from 3rd January 1977).",
                        "86th Constitutional Amendment Act, 2002: Added the 11th Fundamental Duty [Article 51A(k)], commanding parents/guardians to provide education opportunities to children aged 6 to 14 years.",
                        "Present Count: Total 11 Fundamental Duties in Article 51A.",
                        "TNPSC Clarification: 42nd CAA 1976 → Added Part IVA & 10 Duties | 86th CAA 2002 → Added 11th Duty. Do NOT confuse the two amendments!"
                    ],
                    "ta": [
                        "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976: பகுதி IVA மற்றும் உறுப்பு 51A ஆகியவற்றை அரசியலமைப்பில் சேர்த்து, 1976 டிசம்பர் 4 அன்று அசல் 10 அடிப்படை கடமைகளை அறிமுகப்படுத்தியது (1977 ஜனவரி 3 முதல் அமலுக்கு வந்தது).",
                        "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002: 11வது அடிப்படை கடமையை [உறுப்பு 51A(k)] சேர்த்தது. இது 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்குக் கல்வி வாய்ப்புகளை வழங்குமாறு பெற்றோர்கள்/பாதுகாவலர்களுக்குக் கட்டளையிடுகிறது.",
                        "தற்போதைய எண்ணிக்கை: உறுப்பு 51A-ல் மொத்தம் 11 அடிப்படை கடமைகள் உள்ளன.",
                        "டிஎன்பிஎஸ்சி தெளிவுரை: 42வது திருத்தம் 1976 → பகுதி IVA & 10 கடமைகளைச் சேர்த்தது | 86வது திருத்தம் 2002 → 11வது கடமையைச் சேர்த்தது. இவ்விரண்டு திருத்தங்களையும் குழப்பிக் கொள்ள வேண்டாம்!"
                    ]
                }
            }
        ],
        "sec_swaran_singh": [
            {
                "title": "1. Swaran Singh Committee Background & Mandate (ஸ்வரன் சிங் குழு பின்னணியும் நோக்கமும்)",
                "points": {
                    "en": [
                        "Appointment: Appointed by Congress President D.K. Barooah in 1976 under the Chairmanship of Sardar Swaran Singh (former Union Cabinet Minister).",
                        "Objective: To study and recommend constitutional amendments regarding Fundamental Duties to ensure citizens perform duties alongside enjoying rights.",
                        "Recommendation Count: The Swaran Singh Committee recommended inclusion of EIGHT (8) Fundamental Duties in the Constitution.",
                        "Parliament Action: The 42nd Constitutional Amendment Act, 1976 accepted the core recommendations but enacted TEN (10) duties (adding duties not suggested by committee and modifying some)."
                    ],
                    "ta": [
                        "நியமனம்: சர்தார் ஸ்வரன் சிங் (முன்னாள் மத்திய அமைச்சரவை அமைச்சர்) தலைவராக்கப்பட்டு 1976-ல் காங்கிரஸ் தலைவர் டி.கே. பரூவாவால் நியமிக்கப்பட்டது.",
                        "நோக்கம்: குடிமக்கள் உரிமைகளை ಅನುபவிப்பதுடன் கடமைகளையும் செய்வதை உறுதி செய்வதற்கான அரசியலமைப்பு திருத்தங்களைப் படித்து பரிந்துரைப்பது.",
                        "பரிந்துரை எண்ணிக்கை: ஸ்வரன் சிங் குழு அரசியலமைப்பில் எட்டு (8) அடிப்படை கடமைகளைச் சேர்க்கப் பரிந்துரைத்தது.",
                        "நாடாளுமன்ற நடவடிக்கை: 42வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 முதன்மைப் பரிந்துரைகளை ஏற்றுக்கொண்டது, ஆனால் பத்து (10) கடமைகளை இயற்றியது (குழு பரிந்துரைக்காத கடமைகளைச் சேர்த்து சிலவற்றை மாற்றியமைத்தது)."
                    ]
                }
            },
            {
                "title": "2. Recommendations REJECTED / NOT Included (நிராகரிக்கப்பட்ட / சேர்க்கப்படாத பரிந்துரைகள்)",
                "points": {
                    "en": [
                        "Duty to Pay Taxes: Swaran Singh Committee recommended that 'Duty to pay taxes' should be a Fundamental Duty of citizens. This was REJECTED by Parliament and NOT included in Article 51A.",
                        "Penalty / Punishment for Non-Performance: Recommended that Parliament should be empowered to impose penalty or punishment for non-compliance with duties. REJECTED by Parliament.",
                        "Immunity of Penalty Laws: Recommended that no law imposing penalty for duty violation should be questioned in court on ground of infringement of Fundamental Rights (Arts 14, 19). REJECTED by Parliament.",
                        "TNPSC High-Yield Point: Paying taxes is NOT a constitutional Fundamental Duty under Article 51A! It is a statutory duty under Tax Laws."
                    ],
                    "ta": [
                        "வரி செலுத்தும் கடமை: 'வரி செலுத்துவது' குடிமக்களின் அடிப்படை கடமையாக இருக்க வேண்டும் என ஸ்வரன் சிங் குழு பரிந்துரைத்தது. இது நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டு உறுப்பு 51A-ல் சேர்க்கப்படவில்லை.",
                        "கடமை தவறியதற்கான தண்டனை: கடமைகளைச் செய்யத் தவறுபவர்களுக்குத் தண்டனை அல்லது அபராதம் விதிக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கப்பட வேண்டும் எனப் பரிந்துரைத்தது. நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டது.",
                        "தண்டனைச் சட்டங்களின் பாதுகாப்பு: கடமை மீறலுக்கான தண்டனைச் சட்டங்களை அடிப்படை உரிமைகள் (உறுப்புகள் 14, 19) மீறல் என்ற அடிப்படையில் நீதிமன்றத்தில் சவால் செய்ய முடியாது எனப் பரிந்துரைத்தது. நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டது.",
                        "டிஎன்பிஎஸ்சி முக்கிய குறிப்பு: உறுப்பு 51A-ன் கீழ் வரி செலுத்துவது ஒரு அரசியலமைப்பு அடிப்படை கடமை அல்ல! இது வரிச் சட்டங்களின் கீழ் உள்ள ஒரு சட்டப்பூர்வ கடமையாகும்."
                    ]
                }
            }
        ],
        "sec_article_51a_structure": [
            {
                "title": "1. Article 51A(a): Respect Constitution, National Flag & Anthem (உறுப்பு 51A(a): அரசியலமைப்பு, தேசியக் கொடி & கீதம் மதித்தல்)",
                "points": {
                    "en": [
                        "Constitutional Text: 'To abide by the Constitution and respect its ideals and institutions, the National Flag and the National Anthem.'",
                        "Key Directives: 1. Abide by Constitution, 2. Respect Constitutional Ideals (Democracy, Secularism, Justice), 3. Respect Constitutional Institutions (Parliament, Judiciary, Election Commission), 4. Respect National Flag, 5. Respect National Anthem.",
                        "Citizen Responsibility: Internalizing respect for national symbols and avoiding disrespect or insult.",
                        "Statutory Enforcement: Prevention of Insults to National Honour Act, 1971 punishes intentional insult or disrespect to the National Flag, Constitution, or National Anthem.",
                        "Flag Code of India 2002: Governs the display and usage of the National Flag by citizens."
                    ],
                    "ta": [
                        "அரசியலமைப்பு உரை: 'அரசியலமைப்புக்குக் கீழ்ப்படிந்து நடந்து கொள்ளுதலும், அதன் லட்சியங்கள், நிறுவனங்கள், தேசியக் கொடி மற்றும் தேசியக் கீதம் ஆகியவற்றை மதித்தலும்.'",
                        "முதன்மை வழிகாட்டுதல்கள்: 1. அரசியலமைப்புக்குக் கீழ்ப்படிதல், 2. அரசியலமைப்பு லட்சியங்களை மதித்தல் (ஜனநாயகம், மதச்சார்பின்மை, நீதி), 3. அரசியலமைப்பு நிறுவனங்களை மதித்தல் (நாடாளுமன்றம், நீதித்துறை, தேர்தல் ஆணையம்), 4. தேசியக் கொடியை மதித்தல், 5. தேசியக் கீதத்தை மதித்தல்.",
                        "குடிமகன் பொறுப்பு: தேசிய சின்னங்களை மதிப்பதை உள்வாங்குவதும் அவமதிப்பு அல்லது அவமரியாதையைத் தவிர்ப்பதும் ஆகும்.",
                        "சட்டப்பூர்வ அமலாக்கம்: 1971-ன் தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம் தேசியக் கொடி, அரசியலமைப்பு அல்லது தேசியக் கீதத்தை திட்டமிட்டு அவமதிப்பதைத் தண்டிக்கிறது.",
                        "இந்திய தேசியக் கொடி குறியீடு 2002: குடிமக்களால் தேசியக் கொடியைக் காட்சிப்படுத்துதலையும் பயன்படுத்துதலையும் நெறிப்படுத்துகிறது."
                    ]
                }
            },
            {
                "title": "2. Article 51A(b): Cherish & Follow Freedom Struggle Ideals (உறுப்பு 51A(b): சுதந்திரப் போராட்ட லட்சியங்களைப் பேணிப் பின்பற்றுதல்)",
                "points": {
                    "en": [
                        "Constitutional Text: 'To cherish and follow the noble ideals which inspired our national struggle for freedom.'",
                        "Noble Ideals Include: Ahimsa (non-violence), truth, secularism, national unity, democracy, equality, self-reliance, and anti-imperialism.",
                        "Meaning: Citizens should not take freedom for granted, but active cherish and live by the moral values espoused by freedom fighters (Mahatma Gandhi, Jawaharlal Nehru, Netaji, Bhagat Singh, V.O. Chidambaram Pillai, Subramania Bharati).",
                        "TNPSC Relevance: High-yield in statement MCQs regarding national integration and historical awareness."
                    ],
                    "ta": [
                        "அரசியலமைப்பு உரை: 'நமது தேசிய சுதந்திரப் போராட்டத்திற்கு ஊக்கமளித்த உயரிய லட்சியங்களைப் பேணிப் பின்பற்றுதல்.'",
                        "உயரிய லட்சியங்கள்: அகிம்சை (வன்முறையின்மை), உண்மை, மதச்சார்பின்மை, தேசிய ஒற்றுமை, ஜனநாயகம், சமத்துவம், சுயசார்பு மற்றும் ஏகாதிபத்திய எதிர்ப்பு.",
                        "பொருள்: குடிமக்கள் சுதந்திரத்தை அலட்சியமாகக் கருதாமல், சுதந்திரப் போராட்ட வீரர்கள் (மகாத்மா காந்தி, ஜவஹர்லால் நேரு, நேதாஜி, பகத் சிங், வ.உ.சிதம்பரனார், சுப்பிரமணிய பாரதியார்) போற்றிய தார்மீக மதிப்புகளை தீவிரமாகப் பேணி வாழ வேண்டும்.",
                        "டிஎன்பிஎஸ்சி முக்கியத்துவம்: தேசிய ஒருமைப்பாடு மற்றும் வரலாற்று விழிப்புணர்வு பற்றிய கூற்று வினாக்களில் மிகவும் முக்கியமானது."
                    ]
                }
            },
            {
                "title": "3. Article 51A(c): Uphold Sovereignty, Unity & Integrity of India (உறுப்பு 51A(c): இறையாண்மை, ஒற்றுமை & ஒருமைப்பாடு பேணுதல்)",
                "points": {
                    "en": [
                        "Constitutional Text: 'To uphold and protect the sovereignty, unity and integrity of India.'",
                        "Pre-eminent Duty: Considered one of the most paramount duties of an Indian citizen.",
                        "Conceptual Breakdown: 1. Sovereignty = Supreme independent authority of the nation, free from external control. 2. Unity = Emotional and social togetherness of diverse citizens. 3. Integrity = Territorial wholeness and inviolability of national boundaries.",
                        "Word 'Integrity': Added to Preamble by 42nd CAA 1976 and to 3rd Schedule Oaths by 16th CAA 1963.",
                        "Statutory Backing: Unlawful Activities (Prevention) Act (UAPA) 1967 and IPC Section 153B penalize actions challenging India's sovereignty or territorial integrity."
                    ],
                    "ta": [
                        "அரசியலமைப்பு உரை: 'இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணிப் பாதுகாத்தல்.'",
                        "முதன்மை கடமை: இந்தியக் குடிமகனின் மிக முக்கியமான கடமைகளில் ஒன்றாகக் கருதப்படுகிறது.",
                        "தத்துவார்த்தப் பிரிவு: 1. இறையாண்மை = வெளிநாட்டுக் கட்டுப்பாடற்ற தேசத்தின் உச்சகட்ட சுயாதீன அதிகாரம். 2. ஒற்றுமை = பல்வேறு குடிமக்களின் உணர்வுப்பூர்வமான மற்றும் சமூக இணக்கம். 3. ஒருமைப்பாடு = தேசிய எல்லைகளின் நிலப்பரப்பு முழுமை மற்றும் பிரிக்க முடியாத தன்மை.",
                        "'ஒருமைப்பாடு' என்ற வார்த்தை: 1976-ன் 42வது திருத்தத்தால் முகப்புரையிலும், 1963-ன் 16வது திருத்தத்தால் 3வது அட்டவணை உறுதிமொழிகளிலும் சேர்க்கப்பட்டது.",
                        "சட்டப்பூர்வ ஆதரவு: சட்டவிரோத நடவடிக்கைகள் தடுப்புச் சட்டம் (UAPA) 1967 மற்றும் IPC பிரிவு 153B ஆகியவை இந்தியாவின் இறையாண்மை அல்லது நிலப்பரப்பு ஒருமைப்பாட்டிற்குச் சவால் விடுக்கும் நடவடிக்கைகளைத் தண்டிக்கின்றன."
                    ]
                }
            },
            {
                "title": "4. Article 51A(d): Defend the Country & Render National Service (உறுப்பு 51A(d): தேசத்தைப் பாதுகாத்தல் & தேசிய சேவை ஆற்றுதல்)",
                "points": {
                    "en": [
                        "Constitutional Text: 'To defend the country and render national service when called upon to do so.'",
                        "Scope & Obligation: Commands citizens to take up arms or non-combatant civil defense roles whenever called by Parliament or Government during war or national emergency.",
                        "Conscription Capability: Provides constitutional foundation for military conscription (compulsory military service) if Parliament decides to introduce it.",
                        "Distinction: Ordinary civic duty is voluntary; Article 51A(d) becomes a mandatory civic obligation when legally summoned by the State."
                    ],
                    "ta": [
                        "அரசியலமைப்பு உரை: 'தேசத்தைப் பாதுகாத்தலும், தேவைப்படும்போது தேசிய சேவை ஆற்றுதலும்.'",
                        "எல்லையும் பொறுப்பும்: போர் அல்லது தேசிய அவசரநிலையின் போது நாடாளுமன்றம் அல்லது அரசால் அழைக்கப்படும் போது ஆயுதம் ஏந்தவோ அல்லது சிவில் பாதுகாப்புப் பணிகளை ஆற்றவோ குடிமக்களுக்கு ஆணையிடுகிறது.",
                        "கட்டாய ராணுவ சேவை அதிகாரம்: நாடாளுமன்றம் கட்டாய ராணுவ சேவையை அறிமுகப்படுத்த முடிவு செய்தால் அதற்கான அரசியலமைப்பு அடித்தளத்தை வழங்குகிறது.",
                        "வேறுபாடு: சாதாரண குடிமைப் பணி விருப்பத்தின் பேரிலானது; உறுப்பு 51A(d) அரசால் சட்டப்பூர்வமாக அழைக்கப்படும் போது கட்டாயக் குடிமைப் பொறுப்பாக மாறுகிறது."
                    ]
                }
            },
            {
                "title": "5. Article 51A(e): Promote Harmony, Brotherhood & Respect Women's Dignity (உறுப்பு 51A(e): நல்லிணக்கம், சகோதரத்துவம் & பெண்கள் கண்ணியம்)",
                "points": {
                    "en": [
                        "Constitutional Text: 'To promote harmony and the spirit of common brotherhood amongst all the people of India transcending religious, linguistic and regional or sectional diversities; to renounce practices derogatory to the dignity of women.'",
                        "Two Distinct Mandates: 1. Positive Mandate: Promote harmony and common brotherhood across all religions, languages, regions, and sections. 2. Negative Mandate: Renounce (give up) practices derogatory to the dignity of women.",
                        "Brotherhood Aspect: Reinforces the Preamble ideal of 'Fraternity' assuring individual dignity and national unity.",
                        "Women's Dignity Aspect: Commands giving up social evils against women (e.g., Sati, dowry, female foeticide, domestic violence, verbal or physical abuse).",
                        "Statutory Backing: Dowry Prohibition Act 1961, Protection of Women from Domestic Violence Act 2005, IPC Section 509 (insulting modesty of women)."
                    ],
                    "ta": [
                        "அரசியலமைப்பு உரை: 'மதம், மொழி, பிராந்தியம் அல்லது பிரிவு வேறுபாடுகளைக் கடந்து இந்திய மக்கள் அனைவரிடமும் நல்லிணக்கத்தையும் சகோதரத்துவ உணர்வையும் வளர்த்தல்; பெண்களின் கண்ணியத்திற்கு இழுக்கு விளைவிக்கும் பழக்கங்களை விட்டுத்தொழித்தல்.'",
                        "இரண்டு தனித்துவமான கட்டளைகள்: 1. நேர்மறைக் கட்டளை: மதம், மொழி, பிராந்தியம், பிரிவுகளைக் கடந்து நல்லிணக்கம் மற்றும் சகோதரத்துவத்தை வளர்த்தல். 2. எதிர்மறைக் கட்டளை: பெண்களின் கண்ணியத்தைக் குறைக்கும் பழக்கங்களை விட்டுத்தொழித்தல்.",
                        "சகோதரத்துவ அம்சம்: தனிநபர் கண்ணியத்தையும் தேசிய ஒருமைப்பாட்டையும் உறுதிப்படுத்தும் முகப்புரையின் 'சகோதரத்துவம்' என்ற லட்சியத்தை வலுப்படுத்துகிறது.",
                        "பெண்கள் கண்ணிய அம்சம்: பெண்களுக்கு எதிரான சமூகக் கொடுமைகளைக் கைவிட ஆணையிடுகிறது (எ.கா. உடன்கட்டை ஏறுதல், வரதட்சணை, பெண் சிசுக்கொலை, குடும்ப வன்முறை, வார்த்தை அல்லது உடல் ரீதியான துன்புறுத்தல்).",
                        "சட்டப்பூர்வ ஆதரவு: வரதட்சணை தடைச் சட்டம் 1961, குடும்ப வன்முறையிலிருந்து பெண்களைப் பாதுகாக்கும் சட்டம் 2005, IPC பிரிவு 509 (பெண்களின் அடக்கத்திற்கு இழுக்கு விளைவித்தல்)."
                    ]
                }
            }
        ],
        "sec_conceptual_distinctions": [
            {
                "title": "1. Tripartite Comparison: FR vs DPSP vs FD (மூன்று தரப்பு ஒப்பீடு: FR vs DPSP vs FD)",
                "points": {
                    "en": [
                        "Part III (Fundamental Rights): Addressed primarily to the State (prohibitions) and individuals. Justiciable in Supreme Court (Art 32) and High Court (Art 226). Ensures Political Democracy.",
                        "Part IV (DPSP): Addressed to the State as policy guidelines. Non-justiciable in courts. Ensures Social and Economic Democracy and Welfare State.",
                        "Part IVA (Fundamental Duties): Addressed exclusively to CITIZENS of India. Non-justiciable in courts without statutory backing. Promotes Responsible Citizenship and Civic Consciousness.",
                        "Key Constitutional Synergy: Fundamental Rights give liberties; DPSP guide State actions to make liberties meaningful; Fundamental Duties demand citizen discipline to protect democratic liberties."
                    ],
                    "ta": [
                        "பகுதி III (அடிப்படை உரிமைகள்): முதன்மையாக அரசுக்கு (தடைகள்) மற்றும் நபர்களுக்கு ஆணையிடுகிறது. உச்ச நீதிமன்றம் (உறுப்பு 32) மற்றும் உயர் நீதிமன்றத்தில் (உறுப்பு 226) அமல்படுத்தக்கூடியவை. அரசியல் ஜனநாயகத்தை உறுதி செய்கிறது.",
                        "பகுதி IV (DPSP): கொள்கை வழிகாட்டுதல்களாக அரசுக்கு ஆணையிடுகிறது. நீதிமன்றங்களால் அமல்படுத்த முடியாதவை. சமூக மற்றும் பொருளாதார ஜனநாயகம் மற்றும் நல அரசை உறுதி செய்கிறது.",
                        "பகுதி IVA (அடிப்படை கடமைகள்): இந்தியாவின் குடிமக்களுக்கு மட்டுமே ஆணையிடுகிறது. சட்டப்பூர்வ ஆதரவு இன்றி நீதிமன்றங்களால் அமல்படுத்த முடியாதவை. பொறுப்பான குடியுரிமை மற்றும் குடிமை விழிப்புணர்வை மேம்படுத்துகிறது.",
                        "அரசியலமைப்பு ஒருங்கிணைப்பு: அடிப்படை உரிமைகள் சுதந்திரங்களை வழங்குகின்றன; DPSP சுதந்திரங்களை அர்த்தமுள்ளதாக்க அரசு நடவடிக்கைகளை வழிநடத்துகிறது; அடிப்படை கடமைகள் ஜனநாயக சுதந்திரங்களைப் பாதுகாக்க குடிமக்களின் ஒழுக்கத்தைக் கோருகின்றன."
                    ]
                }
            },
            {
                "title": "2. Duties are NOT a Substitute for Rights (கடமைகள் உரிமைகளுக்குப் பகரமாகாது)",
                "points": {
                    "en": [
                        "No Abrogation of Rights: The inclusion of Fundamental Duties DOES NOT curtail, diminish, or take away any Fundamental Right guaranteed under Part III.",
                        "Harmonious Construction: Courts apply the doctrine of harmonious construction. A citizen cannot claim that performing a duty excuses a violation of law, nor can the State suspend Fundamental Rights arbitrarily on the pretext of enforcing duties.",
                        "Supreme Court Stance: Fundamental Rights and Fundamental Duties are two sides of the same coin. Neither overrides the other."
                    ],
                    "ta": [
                        "உரிமைகள் பறிக்கப்படுவதில்லை: அடிப்படை கடமைகளைச் சேர்ப்பது பகுதி III-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட எந்தவொரு அடிப்படை உரிமையையும் குறைக்கவோ, கட்டுப்படுத்தவோ அல்லது பறிக்கவோ செய்யாது.",
                        "இணக்கமான விளக்கம்: நீதிமன்றங்கள் இணக்கமான விளக்கக் கோட்பாட்டைப் பயன்படுத்துகின்றன. ஒரு கடமையைச் செய்வது சட்ட மீறலுக்குச் சாக்காகாது என்று குடிமகன் கோர முடியாது, அதே போல் கடமைகளை அமல்படுத்துவது என்ற போர்வையில் அரசு தன்னிச்சையாக அடிப்படை உரிமைகளை நிறுத்தி வைக்க முடியாது.",
                        "உச்ச நீதிமன்ற நிலைப்பாடு: அடிப்படை உரிமைகளும் அடிப்படை கடமைகளும் ஒரே நாணயத்தின் இரு பக்கங்கள். எதுவும் மற்றொன்றை விட உயர்ந்ததல்ல."
                    ]
                }
            }
        ],
        "sec_justiciability_enforcement": [
            {
                "title": "1. Non-Justiciable Nature & Judicial Role (நீதிமன்ற அமலாக்க இயல்பும் நீதிமன்றங்களின் பங்கும்)",
                "points": {
                    "en": [
                        "Non-Self-Executing: Fundamental Duties are non-self-executing. A court cannot issue a writ of mandamus directing a citizen to follow Article 51A duties directly.",
                        "Parliamentary Power: Parliament has the power to enact legislation to penalize non-compliance with any Fundamental Duty.",
                        "Judicial Utility: Supreme Court ruled that while evaluating the 'reasonableness' of restrictions on Fundamental Rights under Article 19, courts must consider Article 51A. Laws giving effect to Article 51A duties are presumed reasonable and valid.",
                        "Rule of Construction: If a statute is ambiguous, courts interpret it in a manner that aligns with Fundamental Duties."
                    ],
                    "ta": [
                        "தானாக அமலாகாத இயல்பு: அடிப்படை கடமைகள் தானாக அமலாகாதவை. உறுப்பு 51A கடமைகளைப் பின்பற்றுமாறு ஒரு குடிமகனுக்கு நேரடியாக நீதிமன்றம் பேராணை பிறப்பிக்க முடியாது.",
                        "நாடாளுமன்ற அதிகாரம்: எந்தவொரு அடிப்படை கடமையையும் மீறுவதற்குத் தண்டனை அளிக்கும் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு அதிகாரம் உள்ளது.",
                        "நீதிமன்றப் பயன்பாடு: உறுப்பு 19-ன் கீழ் அடிப்படை உரிமைகள் மீதான கட்டுப்பாடுகளின் 'நியாயத் தன்மையை' மதிப்பிடும் போது, நீதிமன்றங்கள் உறுப்பு 51A-ஐக் கருத்தில் கொள்ள வேண்டும் என உச்ச நீதிமன்றம் தீர்ப்பளித்துள்ளது. உறுப்பு 51A கடமைகளைச் செயல்படுத்தும் சட்டங்கள் நியாயமானவை மற்றும் செல்லுபடியாகும் எனக் கருதப்படுகின்றன.",
                        "விளக்க விதி: ஒரு சட்டம் தெளிவற்றதாக இருந்தால், நீதிமன்றங்கள் அதை அடிப்படை கடமைகளுடன் ஒத்துப்போகும் வகையில் விளக்குகின்றன."
                    ]
                }
            },
            {
                "title": "2. Existing Parliamentary Statutes Enforcing Duties (கடமைகளை அமல்படுத்தும் நிலவும் நாடாளுமன்றச் சட்டங்கள்)",
                "points": {
                    "en": [
                        "Prevention of Insults to National Honour Act, 1971: Enforces Article 51A(a) [National Flag, Anthem, Constitution].",
                        "Protection of Civil Rights Act, 1955: Enforces Article 51A(e) by punishing caste and untouchability-related offenses.",
                        "Unlawful Activities (Prevention) Act (UAPA), 1967: Enforces Article 51A(c) [Sovereignty and Integrity of India].",
                        "Representation of the People Act, 1951: Enforces Article 51A(e) by disqualifying candidates promoting communal hatred.",
                        "Indian Penal Code (IPC): Penalizes hate speech (Sec 153A), insulting women's modesty (Sec 509), and national disaffection."
                    ],
                    "ta": [
                        "1971-ன் தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம்: உறுப்பு 51A(a)-ஐ [தேசியக் கொடி, கீதம், அரசியலமைப்பு] அமல்படுத்துகிறது.",
                        "1955-ன் சிவில் உரிமைகள் பாதுகாப்புச் சட்டம்: சாதி மற்றும் தீண்டாமை தொடர்பான குற்றங்களைத் தண்டிப்பதன் மூலம் உறுப்பு 51A(e)-ஐ அமல்படுத்துகிறது.",
                        "1967-ன் சட்டவிரோத நடவடிக்கைகள் தடுப்புச் சட்டம் (UAPA): உறுப்பு 51A(c)-ஐ [இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு] அமல்படுத்துகிறது.",
                        "1951-ன் மக்கள் பிரதிநிதித்துவச் சட்டம்: மதவாத வெறுப்பைத் தூண்டும் வேட்பாளர்களைத் தகுதிநீக்கம் செய்வதன் மூலம் உறுப்பு 51A(e)-ஐ அமல்படுத்துகிறது.",
                        "இந்திய தண்டனைச் சட்டம் (IPC): வெறுப்புப் பேச்சு (பிரிவு 153A), பெண்களின் அடக்கத்திற்கு இழுக்கு விளைவித்தல் (பிரிவு 509) மற்றும் தேசிய விரோத நடவடிக்கைகளைத் தண்டிக்கிறது."
                    ]
                }
            }
        ],
        "sec_cases_legal_context": [
            {
                "title": "1. Landmark Judicial Verdicts on Article 51A (உறுப்பு 51A பற்றிய முக்கிய மைல்கல் வழக்குத் தீர்ப்புகள்)",
                "points": {
                    "en": [
                        "Bijoe Emmanuel v. State of Kerala (1986): Three Jehovah's Witnesses students refused to sing the National Anthem in school but stood up respectfully. Supreme Court held that standing respectfully during the anthem demonstrates proper respect under Art 51A(a). Forceful singing violates Right to Freedom of Speech & Religion (Art 19(1)(a) & Art 25). Right to silence is included.",
                        "Shyam Narayan Chouksey v. Union of India (2018): Supreme Court modified its 2016 interim order, holding that playing the National Anthem in cinema halls before movie shows is OPTIONAL, not mandatory. However, citizens present must show respect under Art 51A(a).",
                        "AIIMS Students Union v. AIIMS (2002): Supreme Court held that Fundamental Duties, though non-justiciable, are equally as important as Fundamental Rights. Duties cannot be ignored while interpreting statutes or evaluating state policies.",
                        "Mohan Kumar Singhania v. Union of India (1992): Supreme Court held that statutes enacted to give effect to Article 51A duties are considered reasonable restrictions under Articles 14, 19, and 21.",
                        "Verma Committee on Fundamental Duties (1999): Justice J.S. Verma Committee identified non-operationalized legal provisions and recommended teaching Fundamental Duties in schools and educational institutions."
                    ],
                    "ta": [
                        "பிஜோய் இம்மானுவேல் vs கேரளா மாநிலம் (1986): யெகோவாவின் சாட்சிகள் பிரிவைச் சேர்ந்த மூன்று மாணவர்கள் பள்ளியில் தேசியக் கீதம் பாட மறுத்தனர், ஆனால் மரியாதையுடன் எழுந்து நின்றனர். தேசியக் கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ன் கீழ் முறையான மரியாதையைக் காட்டுகிறது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. கட்டாயப்படுத்தி பாட வைப்பது பேச்சுரிமை மற்றும் மத சுதந்திரத்தை மீறுகிறது (உறுப்புகள் 19(1)(a) & 25). அமைதியாக இருக்கும் உரிமையும் இதில் அடங்கும்.",
                        "ஷியாம் நாராயண் சௌக்சே vs இந்திய யூனியன் (2018): திரையரங்குகளில் படம் திரையிடுவதற்கு முன்பு தேசியக் கீதம் இசைப்பது கட்டாயமில்லை, விருப்பத்திற்குரியது என்று உச்ச நீதிமன்றம் தனது 2016 இடைக்கால உத்தரவை மாற்றியமைத்தது. இருப்பினும், उपस्थित இருக்கும் குடிமக்கள் உறுப்பு 51A(a)-ன் கீழ் மரியாதை காட்ட வேண்டும்.",
                        "AIIMS மாணவர் சங்கம் vs AIIMS (2002): அடிப்படை கடமைகள் நீதிமன்றங்களால் அமல்படுத்த முடியாதவை என்றாலும், அவை அடிப்படை உரிமைகளுக்குச் சமமான முக்கியத்துவம் வாய்ந்தவை என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. சட்டங்களை விளக்கும் போதோ அல்லது அரசின் கொள்கைகளை மதிப்பிடும் போதோ கடமைகளைப் புறக்கணிக்க முடியாது.",
                        "மோகன் குமார் சிங்கானியா vs இந்திய யூனியன் (1992): உறுப்பு 51A கடமைகளைச் செயல்படுத்த இயற்றப்பட்ட சட்டங்கள் உறுப்புகள் 14, 19 மற்றும் 21-ன் கீழ் நியாயமான கட்டுப்பாடுகளாகக் கருதப்படுகின்றன என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
                        "அடிப்படை கடமைகள் பற்றிய வர்மா குழு (1999): நீதிபதி ஜே.எஸ். வர்மா குழு நிலவும் சட்ட விதிகளைக் கண்டறிந்து, பள்ளிகள் மற்றும் கல்வி நிறுவனங்களில் அடிப்படை கடமைகளைக் கற்பிக்கப் பரிந்துரைத்தது."
                    ]
                }
            }
        ],
        "sec_amendments": [
            {
                "title": "1. 42nd Constitutional Amendment Act, 1976 (42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976)",
                "points": {
                    "en": [
                        "Enactment: Passed during National Emergency under Prime Minister Indira Gandhi based on Swaran Singh Committee recommendations.",
                        "New Part: Inserted Part IVA ('FUNDAMENTAL DUTIES').",
                        "New Article: Inserted Article 51A.",
                        "Number of Duties: Enacted TEN (10) Fundamental Duties [Article 51A(a) to 51A(j)].",
                        "Date of Effect: Came into force on 3rd January 1977."
                    ],
                    "ta": [
                        "இயற்றப்பட்ட சூழல்: பிரதமர் இந்திரா காந்தி காலத்தில் ஸ்வரன் சிங் குழு பரிந்துரைகளின் அடிப்படையில் தேசிய அவசரநிலையின் போது நிறைவேற்றப்பட்டது.",
                        "புதிய பகுதி: பகுதி IVA ('அடிப்படை கடமைகள்') இணைக்கப்பட்டது.",
                        "புதிய உறுப்பு: உறுப்பு 51A இணைக்கப்பட்டது.",
                        "கடமைகளின் எண்ணிக்கை: பத்து (10) அடிப்படை கடமைகளை இயற்றியது [உறுப்பு 51A(a) முதல் 51A(j) வரை].",
                        "அமலுக்கு வந்த நாள்: 1977 ஜனவரி 3 முதல் நடைமுறைக்கு வந்தது."
                    ]
                }
            },
            {
                "title": "2. 86th Constitutional Amendment Act, 2002 (86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002)",
                "points": {
                    "en": [
                        "Enactment: Passed under Prime Minister Atal Bihari Vajpayee.",
                        "11th Duty Added: Added Article 51A(k)—'who is a parent or guardian to provide opportunities for education to his child or, as the case may be, ward between the age of six and fourteen years.'",
                        "Tripartite Educational Amendments: 1. Article 21A (Fundamental Right: State duty for free & compulsory education for 6-14 yrs). 2. Article 45 (DPSP: State directive for early childhood care below 6 yrs). 3. Article 51A(k) (Fundamental Duty: Parent/guardian duty for education for 6-14 yrs).",
                        "Crucial Distinction: Art 21A commands the STATE | Art 51A(k) commands the PARENT/GUARDIAN. Do NOT confuse the two!"
                    ],
                    "ta": [
                        "இயற்றப்பட்ட சூழல்: பிரதமர் அடல் பிஹாரி வாஜ்பாய் காலத்தில் நிறைவேற்றப்பட்டது.",
                        "11வது கடமை சேர்ப்பு: உறுப்பு 51A(k) சேர்க்கப்பட்டது—'ஆறு முதல் பதினான்கு வயது வரையிலான தனது குழந்தைக்கு அல்லது பாதுகாப்பில் உள்ளவருக்குக் கல்வி வாய்ப்புகளை வழங்குவது பெற்றோர் அல்லது பாதுகாவலரின் கடமையாகும்.'",
                        "மூன்று தரப்பு கல்வித் திருத்தங்கள்: 1. உறுப்பு 21A (அடிப்படை உரிமை: 6-14 வயது குழந்தைகளுக்கு இலவச கட்டாயக் கல்வி வழங்குவது அரசின் கடமை). 2. உறுப்பு 45 (DPSP: 6 வயதிற்குட்பட்ட குழந்தைகளுக்கு முன்பருவப் பராமரிப்பு வழங்குவது அரசின் வழிகாட்டுதல்). 3. உறுப்பு 51A(k) (அடிப்படை கடமை: 6-14 வயது குழந்தைக்குக் கல்வி வாய்ப்பு வழங்குவது பெற்றோரின் கடமை).",
                        "முக்கிய வேறுபாடு: உறுப்பு 21A அரசுக்கு ஆணையிடுகிறது | உறுப்பு 51A(k) பெற்றோர்/பாதுகாவலருக்கு ஆணையிடுகிறது. இவ்விரண்டையும் குழப்பிக் கொள்ள வேண்டாம்!"
                    ]
                }
            }
        ],
        "sec_traps_revision": [
            {
                "title": "TNPSC Traps, Comparison Framework & High-Yield Revision Summary (டிஎன்பிஎஸ்சி பொறிகள் & முக்கிய திருப்புதல் சுருக்கம்)",
                "points": {
                    "en": [
                        "Part IVA & Article 51A contain Fundamental Duties added by the 42nd Constitutional Amendment Act, 1976 based on Swaran Singh Committee recommendations.",
                        "Swaran Singh Committee recommended 8 duties, but Parliament enacted 10 duties. Duty to pay taxes and penalties for non-performance were REJECTED.",
                        "The 11th Fundamental Duty [Article 51A(k)] was added by the 86th Constitutional Amendment Act, 2002.",
                        "Fundamental Duties apply EXCLUSIVELY to Citizens of India and are non-justiciable in nature."
                    ],
                    "ta": [
                        "பகுதி IVA & உறுப்பு 51A ஆகியவை ஸ்வரன் சிங் குழு பரிந்துரைகளின் படி 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட அடிப்படை கடமைகளைக் கொண்டுள்ளன.",
                        "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் 10 கடமைகளை இயற்றியது. வரி செலுத்தும் கடமை மற்றும் கடமை தவறியதற்கான தண்டனை ஆகியவை நிராகரிக்கப்பட்டன.",
                        "11வது அடிப்படை கடமை [உறுப்பு 51A(k)] 2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது.",
                        "அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும் மற்றும் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாத இயல்புடையவை."
                    ]
                }
            }
        ],
        "tables": [
            {
                "id": "tbl_fr_vs_fd",
                "title_en": "1. Fundamental Rights (Part III) vs Fundamental Duties (Part IVA)",
                "title_ta": "1. அடிப்படை உரிமைகள் (பகுதி III) vs அடிப்படை கடமைகள் (பகுதி IVA)",
                "headers_en": ["Dimension / Feature", "Fundamental Rights (Part III)", "Fundamental Duties (Part IVA)"],
                "headers_ta": ["பரிமாணம் / அம்சம்", "அடிப்படை உரிமைகள் (பகுதி III)", "அடிப்படை கடமைகள் (பகுதி IVA)"],
                "rows_en": [
                    ["Constitutional Location", "Part III (Articles 12 to 35)", "Part IVA (Article 51A)"],
                    ["Original Count & Present Count", "Original: 7 | Present: 6", "Original (1950): 0 | 42nd CAA: 10 | Present: 11"],
                    ["Who it Addresses", "Primarily the State (prohibitions) & individuals", "Exclusively Citizens of India"],
                    ["Justiciability & Writs", "Justiciable (Enforceable by SC Art 32 & HC Art 226)", "Non-Justiciable (No direct writ enforcement)"],
                    ["Applicability to Foreigners", "Certain FRs apply to all persons (citizens & foreigners)", "Applies ONLY to Citizens of India"],
                    ["Primary Objective", "To establish Political Democracy & individual freedom", "To promote Responsible Citizenship & national discipline"]
                ],
                "rows_ta": [
                    ["அரசியலமைப்பு இடம்", "பகுதி III (உறுப்புகள் 12 முதல் 35 வரை)", "பகுதி IVA (உறுப்பு 51A)"],
                    ["அசல் & தற்போதைய எண்ணிக்கை", "அசல்: 7 | தற்போதைய: 6", "அசல் (1950): 0 | 42வது திருத்தம்: 10 | தற்போதைய: 11"],
                    ["யாருக்கு ஆணையிடுகிறது", "முதன்மையாக அரசுக்கு (தடைகள்) & நபர்களுக்கு", "இந்தியக் குடிமக்களுக்கு மட்டுமே"],
                    ["நீதிமன்ற அமலாக்கம் & பேராணைகள்", "அமல்படுத்தக்கூடியவை (உச்ச நீதிமன்றம் உறுப்பு 32 & உயர் நீதிமன்றம் 226)", "அமல்படுத்த முடியாதவை (நேரடி பேராணை அமலாக்கம் இல்லை)"],
                    ["வெளிநாட்டினருக்குப் பொருந்துமா", "சில உரிமைகள் அனைவருக்கும் பொருந்தும் (குடிமக்கள் & வெளிநாட்டினர்)", "இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்"],
                    ["முதன்மை நோக்கம்", "அரசியல் ஜனநாயகம் & தனிநபர் சுதந்திரத்தை நிறுவுதல்", "பொறுப்பான குடியுரிமை & தேசிய ஒழுங்கை வளர்த்தல்"]
                ]
            },
            {
                "id": "tbl_dpsp_vs_fd",
                "title_en": "2. Directive Principles (Part IV) vs Fundamental Duties (Part IVA)",
                "title_ta": "2. அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV) vs அடிப்படை கடமைகள் (பகுதி IVA)",
                "headers_en": ["Dimension / Feature", "Directive Principles of State Policy (Part IV)", "Fundamental Duties (Part IVA)"],
                "headers_ta": ["பரிமாணம் / அம்சம்", "அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV)", "அடிப்படை கடமைகள் (பகுதி IVA)"],
                "rows_en": [
                    ["Target Audience", "Addressed to the State (Union, State, Local bodies)", "Addressed to the Citizens of India"],
                    ["Constitutional Location", "Part IV (Articles 36 to 51)", "Part IVA (Article 51A)"],
                    ["Source of Inspiration", "Irish Constitution of 1937", "USSR Constitution (Soviet Union)"],
                    ["Nature of Obligation", "Positive duties of State for socio-economic welfare", "Moral & civic obligations of citizens"],
                    ["Sanction Behind", "Moral & Political sanction (public opinion & elections)", "Moral sanction & specific statutory laws (e.g. UAPA, Flag Code)"]
                ],
                "rows_ta": [
                    ["இலக்கு வாசகர்கள்", "அரசுக்கு ஆணையிடுகிறது (மத்திய, மாநில, உள்ளாட்சி அமைப்புகள்)", "இந்தியக் குடிமக்களுக்கு ஆணையிடுகிறது"],
                    ["அரசியலமைப்பு இடம்", "பகுதி IV (உறுப்புகள் 36 முதல் 51 வரை)", "பகுதி IVA (உறுப்பு 51A)"],
                    ["தோற்றுவாய் / அனுபவம்", "1937 அயர்லாந்து அரசியலமைப்பு", "முன்னாள் சோவியத் யூனியன் (USSR) அரசியலமைப்பு"],
                    ["பொறுப்பின் இயல்பு", "சமூக-பொருளாதார நலனுக்கான அரசின் நேர்மறைக் கடமைகள்", "குடிமக்களின் தர்ம நெறி & குடிமைப் பொறுப்புகள்"],
                    ["ஆதரவு அதிகாரம்", "தார்மீக & அரசியல் அதிகாரம் (பொதுமக்கள் கருத்து & தேர்தல்கள்)", "தார்மீக அதிகாரம் & குறிப்பிட்ட சட்டங்கள் (எ.கா. UAPA, கொடி குறியீடு)"]
                ]
            },
            {
                "id": "tbl_fr_dpsp_fd_tripartite",
                "title_en": "3. Tripartite Synthesis: Fundamental Rights vs DPSP vs Fundamental Duties",
                "title_ta": "3. மூன்று தரப்புத் தொகுப்பு: அடிப்படை உரிமைகள் vs DPSP vs அடிப்படை கடமைகள்",
                "headers_en": ["Feature", "Fundamental Rights (Part III)", "DPSP (Part IV)", "Fundamental Duties (Part IVA)"],
                "headers_ta": ["அம்சம்", "அடிப்படை உரிமைகள் (பகுதி III)", "DPSP (பகுதி IV)", "அடிப்படை கடமைகள் (பகுதி IVA)"],
                "rows_en": [
                    ["Enshrined Part", "Part III (Arts 12-35)", "Part IV (Arts 36-51)", "Part IVA (Art 51A)"],
                    ["Democracy Type", "Political Democracy", "Social & Economic Democracy", "Civic & Constitutional Democracy"],
                    ["Enforceability", "Direct Judicial Enforceability", "Non-justiciable Directive", "Non-justiciable Duty"],
                    ["Origin Country", "USA (Bill of Rights)", "Ireland (1937 Constitution)", "USSR (Soviet Union)"],
                    ["Key Example", "Art 14 (Equality before law)", "Art 39A (Free Legal Aid)", "Art 51A(a) (Respect National Flag)"]
                ],
                "rows_ta": [
                    ["பொறிக்கப்பட்டுள்ள பகுதி", "பகுதி III (உறுப்புகள் 12-35)", "பகுதி IV (உறுப்புகள் 36-51)", "பகுதி IVA (உறுப்பு 51A)"],
                    ["ஜனநாயக வகை", "அரசியல் ஜனநாயகம்", "சமூக & பொருளாதார ஜனநாயகம்", "குடிமை & அரசியலமைப்பு ஜனநாயகம்"],
                    ["நீதிமன்ற அமலாக்கம்", "நேரடி நீதிமன்ற அமலாக்கம்", "அமல்படுத்த முடியாத வழிகாட்டுதல்", "அமல்படுத்த முடியாத கடமை"],
                    ["தோற்றுவாய் நாடு", "அமெரிக்கா (Bill of Rights)", "அயர்லாந்து (1937 அரசியலமைப்பு)", "சோவியத் யூனியன் (USSR)"],
                    ["முக்கிய உதாரணம்", "உறுப்பு 14 (சட்டத்தின் முன் சமத்துவம்)", "உறுப்பு 39A (இலவச சட்ட உதவி)", "உறுப்பு 51A(a) (தேசியக் கொடியை மதித்தல்)"]
                ]
            },
            {
                "id": "tbl_42nd_vs_86th_caa",
                "title_en": "4. 42nd Amendment (1976) vs 86th Amendment (2002)",
                "title_ta": "4. 42வது திருத்தம் (1976) vs 86வது திருத்தம் (2002)",
                "headers_en": ["Dimension", "42nd Constitutional Amendment Act, 1976", "86th Constitutional Amendment Act, 2002"],
                "headers_ta": ["பரிமாணம்", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002"],
                "rows_en": [
                    ["Prime Minister", "Indira Gandhi", "Atal Bihari Vajpayee"],
                    ["Changes in FDs", "Inserted Part IVA & Article 51A with 10 Duties", "Added 11th Duty [Article 51A(k)]"],
                    ["Committee Inspiration", "Sardar Swaran Singh Committee", "M.N. Venkatachaliah Commission / Verma Committee"],
                    ["Core Subject Added", "Civic discipline, national symbols, sovereignty, harmony", "Childhood Education (6 to 14 years)"],
                    ["Related Articles Changed", "Added Arts 39A, 43A, 48A in DPSP", "Added Art 21A (FR) and modified Art 45 (DPSP)"]
                ],
                "rows_ta": [
                    ["பிரதமர்", "இந்திரா காந்தி", "அடல் பிஹாரி வாஜ்பாய்"],
                    ["அடிப்படை கடமை மாற்றங்கள்", "பகுதி IVA & உறுப்பு 51A உடன் 10 கடமைகளைச் சேர்த்தது", "11வது கடமையைச் சேர்த்தது [உறுப்பு 51A(k)]"],
                    ["குழுவின் தூண்டுதல்", "சர்தார் ஸ்வரன் சிங் குழு", "எம்.என். வெங்கடாசலையா ஆணையம் / வர்மா குழு"],
                    ["சேர்க்கப்பட்ட முதன்மை விஷயம்", "குடிமை ஒழுக்கம், தேசிய சின்னங்கள், இறையாண்மை, நல்லிணக்கம்", "குழந்தைகள் கல்வி (6 முதல் 14 வயது)"],
                    ["தொடர்புடைய உறுப்பு மாற்றங்கள்", "DPSP-ல் உறுப்புகள் 39A, 43A, 48A சேர்க்கப்பட்டன", "உறுப்பு 21A (FR) சேர்க்கப்பட்டு உறுப்பு 45 (DPSP) மாற்றப்பட்டது"]
                ]
            },
            {
                "id": "tbl_art21a_vs_51ak",
                "title_en": "5. Article 21A (Fundamental Right) vs Article 51A(k) (Fundamental Duty)",
                "title_ta": "5. உறுப்பு 21A (அடிப்படை உரிமை) vs உறுப்பு 51A(k) (அடிப்படை கடமை)",
                "headers_en": ["Feature / Aspect", "Article 21A (Fundamental Right)", "Article 51A(k) (Fundamental Duty)"],
                "headers_ta": ["அம்சம் / பகுதி", "உறுப்பு 21A (அடிப்படை உரிமை)", "உறுப்பு 51A(k) (அடிப்படை கடமை)"],
                "rows_en": [
                    ["Constitutional Category", "Part III (Fundamental Right)", "Part IVA (Fundamental Duty)"],
                    ["Duty Bearer", "The STATE (Government)", "Parent or Guardian"],
                    ["Target Beneficiary", "Children aged 6 to 14 years", "Child or Ward aged 6 to 14 years"],
                    ["Legal Nature", "Justiciable (Court can issue writ to State)", "Non-justiciable (Parent cannot be jailed directly under Art 51A)"],
                    ["Core Mandate", "Provide free & compulsory education", "Provide opportunities for education"]
                ],
                "rows_ta": [
                    ["அரசியலமைப்புப் பிரிவு", "பகுதி III (அடிப்படை உரிமை)", "பகுதி IVA (அடிப்படை கடமை)"],
                    ["கடமைப் பொறுப்பாளி", "அரசு (Government)", "பெற்றோர் அல்லது பாதுகாவலர்"],
                    ["பயனாளி", "6 முதல் 14 வயது வரையிலான குழந்தைகள்", "6 முதல் 14 வயது வரையிலான குழந்தை/பாதுகாப்பில் உள்ளவர்"],
                    ["சட்டப்பூர்வ இயல்பு", "அமல்படுத்தக் கூடியது (அரசுக்கு எதிராக நீதிமன்றம் பேராணை பிறப்பிக்கலாம்)", "அமல்படுத்த முடியாதது (உறுப்பு 51A-ன் கீழ் பெற்றோரைக் கைது செய்ய முடியாது)"],
                    ["முதன்மை கட்டளை", "இலவச மற்றும் கட்டாயக் கல்வி வழங்குதல்", "கல்விக்கான வாய்ப்புகளை வழங்குதல்"]
                ]
            },
            {
                "id": "tbl_51aa_vs_statutory_symbols",
                "title_en": "6. Article 51A(a) vs National Symbols Statutory Framework",
                "title_ta": "6. உறுப்பு 51A(a) vs தேசிய சின்னங்கள் சட்டப்பூர்வ அமைப்பு",
                "headers_en": ["Constitutional/Legal Instrument", "Scope / Provision", "Enforceability & Penalty"],
                "headers_ta": ["அரசியலமைப்பு/சட்டப்பூர்வ கருவி", "எல்லை / விதி", "அமலாக்கம் & தண்டனை"],
                "rows_en": [
                    ["Article 51A(a) (Constitutional Duty)", "Commands respect for Constitution, Flag, and Anthem", "Non-justiciable by itself"],
                    ["Prevention of Insults to National Honour Act 1971", "Penalizes burning, trampling, or disrespecting Flag/Anthem", "Statutory offense with imprisonment up to 3 years"],
                    ["Flag Code of India 2002", "Executive guidelines for display and hoisting of Flag", "Non-statutory code, but violations backed by 1971 Act"],
                    ["Emblems and Names Act 1950", "Prevents improper commercial use of State Emblem & Name", "Statutory prohibition with monetary fines"]
                ],
                "rows_ta": [
                    ["உறுப்பு 51A(a) (அரசியலமைப்பு கடமை)", "அரசியலமைப்பு, கொடி, கீதத்தை மதிக்க ஆணையிடுகிறது", "தானாக அமல்படுத்த முடியாதது"],
                    ["தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம் 1971", "கொடி/கீதத்தை எரிப்பது, மிதிப்பது, அவமதிப்பதைக் குற்றமாக்குகிறது", "3 ஆண்டுகள் வரை சிறைத்தண்டனை உள்ள சட்டப்பூர்வ குற்றம்"],
                    ["இந்திய தேசியக் கொடி குறியீடு 2002", "கொடியைக் காட்சிப்படுத்துதல் & ஏற்றுவதற்கான வழிகாட்டுதல்கள்", "சட்டப்பூர்வக் குறியீடு அல்ல, ஆனால் மீறல்கள் 1971 சட்டத்தால் தண்டிக்கப்படும்"],
                    ["சின்னங்கள் மற்றும் பெயர்கள் சட்டம் 1950", "அரசுச் சின்னம்/பெயரை வணிக ரீதியாகத் தவறாகப் பயன்படுத்துவதைத் தடுக்கிறது", "அபராதத்துடன் கூடிய சட்டப்பூர்வத் தடை"]
                ]
            },
            {
                "id": "tbl_51ac_sovereignty_unity_integrity",
                "title_en": "7. Article 51A(c): Sovereignty vs Unity vs Integrity of India",
                "title_ta": "7. உறுப்பு 51A(c): இறையாண்மை vs ஒற்றுமை vs ஒருமைப்பாடு",
                "headers_en": ["Term", "Core Meaning", "Constitutional / Statutory Context"],
                "headers_ta": ["சொல்", "முதன்மைப் பொருள்", "அரசியலமைப்பு / சட்டப்பூர்வ சூழல்"],
                "rows_en": [
                    ["Sovereignty (இறையாண்மை)", "Supreme independent authority free from external control", "Preamble key word; enforced by UAPA 1967"],
                    ["Unity (ஒற்றுமை)", "Social and emotional cohesion among diverse peoples", "Preamble ideal; enforced by IPC Sec 153A"],
                    ["Integrity (ஒருமைப்பாடு)", "Territorial wholeness and inviolability of national land", "Added by 42nd CAA to Preamble & 16th CAA to Oaths"]
                ],
                "rows_ta": [
                    ["இறையாண்மை (Sovereignty)", "வெளிநாட்டுக் கட்டுப்பாடற்ற உச்சகட்ட சுயாதீன அதிகாரம்", "முகப்புரை முக்கிய சொல்; UAPA 1967 மூலம் அமலாவது"],
                    ["ஒற்றுமை (Unity)", "பல்வேறு மக்களிடையே சமூக மற்றும் உணர்வுப்பூர்வ இணக்கம்", "முகப்புரை லட்சியம்; IPC பிரிவு 153A மூலம் அமலாவது"],
                    ["ஒருமைப்பாடு (Integrity)", "தேசிய நிலப்பரப்பின் முழுமை மற்றும் பிரிக்க முடியாத தன்மை", "42வது திருத்தத்தால் முகப்புரையிலும் 16வது திருத்தத்தால் உறுதிமொழிகளிலும் சேர்க்கப்பட்டது"]
                ]
            },
            {
                "id": "tbl_51ad_vs_ordinary_civic",
                "title_en": "8. Article 51A(d) (National Service Duty) vs Ordinary Civic Responsibilities",
                "title_ta": "8. உறுப்பு 51A(d) (தேசிய சேவை கடமை) vs சாதாரண குடிமைப் பொறுப்புகள்",
                "headers_en": ["Dimension", "Article 51A(d) National Defence Duty", "Ordinary Civic Responsibilities"],
                "headers_ta": ["பரிமாணம்", "உறுப்பு 51A(d) தேசியப் பாதுகாப்பு கடமை", "சாதாரண குடிமைப் பொறுப்புகள்"],
                "rows_en": [
                    ["Trigger Point", "When formally called upon by Government/Parliament", "Voluntary day-to-day civic behavior"],
                    ["Constitutional Backing", "Explicitly written in Article 51A(d)", "Implicit in democratic living"],
                    ["Conscription Power", "Provides foundation for mandatory military/civil service", "No conscription power"],
                    ["Examples", "Defending borders during war, emergency disaster relief duty", "Casting vote in elections, paying local taxes, keeping streets clean"]
                ],
                "rows_ta": [
                    ["தூண்டும் புள்ளி", "அரசு/நாடாளுமன்றத்தால் சட்டப்பூர்வமாக அழைக்கப்படும் போது", "அன்றாட விருப்பப்பூர்வ குடிமை நடத்தை"],
                    ["அரசியலமைப்பு ஆதரவு", "உறுப்பு 51A(d)-ல் வெளிப்படையாக எழுதப்பட்டுள்ளது", "ஜனநாயக வாழ்க்கையில் மறைமுகமாக உள்ளது"],
                    ["கட்டாய சேவை அதிகாரம்", "கட்டாய ராணுவ/சிவில் சேவைக்கான அடித்தளத்தை வழங்குகிறது", "கட்டாய சேவை அதிகாரம் இல்லை"],
                    ["உதாரணங்கள்", "போரின் போது எல்லையைப் பாதுகாத்தல், அவசர பேரிடர் நிவாரணப் பணி", "தேர்தலில் வாக்களிப்பது, உள்ளாட்சி வரி செலுத்துவது, தெருக்களைச் சுத்தமாக வைப்பது"]
                ]
            }
        ],
        "mind_map": [
            {
                "title": "Fundamental Duties (Part IVA - Article 51A)",
                "short_label": "Part IVA Core",
                "children": [
                    {
                        "title": "1. Evolution & Amendments",
                        "short_label": "History",
                        "children": [
                            {
                                "title": "Original 1950 Constitution: Absent",
                                "short_label": "1950"
                            },
                            {
                                "title": "Swaran Singh Committee 1976: Rec. 8 duties (Tax duty & Penalty REJECTED)",
                                "short_label": "Swaran Singh"
                            },
                            {
                                "title": "42nd CAA 1976: Added Part IVA & 10 Duties",
                                "short_label": "42nd CAA"
                            },
                            {
                                "title": "86th CAA 2002: Added 11th Duty Art 51A(k) (6-14 yrs Education)",
                                "short_label": "86th CAA"
                            }
                        ]
                    },
                    {
                        "title": "2. Constitutional Nature",
                        "short_label": "Nature",
                        "children": [
                            {
                                "title": "Applies ONLY to Citizens of India (Not Aliens)",
                                "short_label": "Citizens Only"
                            },
                            {
                                "title": "Non-Justiciable (No direct court writs)",
                                "short_label": "Non-Justiciable"
                            },
                            {
                                "title": "Enforceable via Parliamentary Statutes (UAPA, Flag Code, IPC)",
                                "short_label": "Statutory Laws"
                            }
                        ]
                    },
                    {
                        "title": "3. Article 51A Part 1 Group (51A(a) to 51A(e))",
                        "short_label": "Part 1 Duties",
                        "children": [
                            {
                                "title": "51A(a): Respect Constitution, National Flag & National Anthem",
                                "short_label": "51A(a) Symbols"
                            },
                            {
                                "title": "51A(b): Cherish and follow noble ideals of Freedom Struggle",
                                "short_label": "51A(b) Ideals"
                            },
                            {
                                "title": "51A(c): Uphold and protect Sovereignty, Unity & Integrity",
                                "short_label": "51A(c) Integrity"
                            },
                            {
                                "title": "51A(d): Defend the country and render national service when called",
                                "short_label": "51A(d) Defence"
                            },
                            {
                                "title": "51A(e): Promote Harmony, Brotherhood & Renounce practices derogatory to Women",
                                "short_label": "51A(e) Harmony & Women"
                            }
                        ]
                    },
                    {
                        "title": "4. Key Connections",
                        "short_label": "Connections",
                        "children": [
                            {
                                "title": "Art 51A(k) Parent Duty <---> Art 21A FR State Duty <---> Art 45 DPSP Early Childhood",
                                "short_label": "Education Trio"
                            },
                            {
                                "title": "Bijoe Emmanuel Case 1986: Standing respectfully during National Anthem fulfills Art 51A(a)",
                                "short_label": "Bijoe Case"
                            }
                        ]
                    }
                ]
            }
        ],
        "tnpsc_traps": [
            {
                "title": "1. Swaran Singh Committee Recommendation vs 42nd Amendment Trap (ஸ்வரன் சிங் குழு vs 42வது திருத்தப் பொறி)",
                "points": {
                    "en": [
                        "TRAP: Statements claiming Swaran Singh Committee recommended 10 duties or that Duty to Pay Taxes is in Article 51A.",
                        "FACT: Swaran Singh Committee recommended 8 duties. The 42nd CAA enacted 10 duties. 'Duty to Pay Taxes' was recommended by Swaran Singh Committee but REJECTED by Parliament and NOT included in Article 51A!"
                    ],
                    "ta": [
                        "பொறி: ஸ்வரன் சிங் குழு 10 கடமைகளைப் பரிந்துரைத்தது என்றோ அல்லது வரி செலுத்தும் கடமை உறுப்பு 51A-ல் உள்ளது என்றோ கூறும் கூற்றுகள்.",
                        "உண்மை: ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது. 42வது திருத்தம் 10 கடமைகளை இயற்றியது. 'வரி செலுத்தும் கடமை' ஸ்வரன் சிங் குழுவால் பரிந்துரைக்கப்பட்டது, ஆனால் நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டு உறுப்பு 51A-ல் சேர்க்கப்படவில்லை!"
                    ]
                }
            },
            {
                "title": "2. Applicable Scope Trap: Citizens vs Foreigners (பொருந்தும் எல்லைப் பொறி: குடிமக்கள் vs வெளிநாட்டினர்)",
                "points": {
                    "en": [
                        "TRAP: Statement claiming Fundamental Duties apply to all persons residing in India including foreigners.",
                        "FACT: Fundamental Duties apply EXCLUSIVELY to Citizens of India. Foreigners/aliens residing in India are not bound by Article 51A."
                    ],
                    "ta": [
                        "பொறி: வெளிநாட்டினர் உட்பட இந்தியாவில் வசிக்கும் அனைத்து நபர்களுக்கும் அடிப்படை கடமைகள் பொருந்தும் என்ற கூற்று.",
                        "உண்மை: அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும். இந்தியாவில் வசிக்கும் வெளிநாட்டினருக்கு உறுப்பு 51A பொருந்தாது."
                    ]
                }
            },
            {
                "title": "3. Original 10 vs Present 11 Duties Trap (அசல் 10 vs தற்போதைய 11 கடமைகள் பொறி)",
                "points": {
                    "en": [
                        "TRAP: Confusing 42nd CAA (1976) with 86th CAA (2002) regarding the number of duties.",
                        "FACT: 42nd CAA (1976) added the original 10 duties. The 11th duty [Art 51A(k)] was added by the 86th CAA in 2002."
                    ],
                    "ta": [
                        "பொறி: கடமைகளின் எண்ணிக்கையைப் பொறுத்து 42வது திருத்தத்தையும் (1976) 86வது திருத்தத்தையும் (2002) குழப்பிக் கொள்ளுதல்.",
                        "உண்மை: 42வது திருத்தம் (1976) அசல் 10 கடமைகளைச் சேர்த்தது. 11வது கடமை [உறுப்பு 51A(k)] 2002-ல் 86வது திருத்தத்தால் சேர்க்கப்பட்டது."
                    ]
                }
            },
            {
                "title": "4. Article 21A vs Article 51A(k) Duty Bearer Trap (உறுப்பு 21A vs 51A(k) கடமையாளி பொறி)",
                "points": {
                    "en": [
                        "TRAP: Saying Article 51A(k) makes free education a State responsibility.",
                        "FACT: Article 21A (Fundamental Right) makes free and compulsory education the responsibility of the STATE. Article 51A(k) (Fundamental Duty) makes providing education opportunities the responsibility of the PARENT or GUARDIAN."
                    ],
                    "ta": [
                        "பொறி: உறுப்பு 51A(k) இலவசக் கல்வியை அரசின் பொறுப்பாகாக்குகிறது என்ற கூற்று.",
                        "உண்மை: உறுப்பு 21A (அடிப்படை உரிமை) இலவச கட்டாயக் கல்வியை அரசின் பொறுப்பாகாக்குகிறது. உறுப்பு 51A(k) (அடிப்படை கடமை) கல்வி வாய்ப்புகளை வழங்குவதைப் பெற்றோர் அல்லது பாதுகாவலரின் பொறுப்பாகாக்குகிறது."
                    ]
                }
            },
            {
                "title": "5. Article 51A(a) National Anthem Case Trap (உறுப்பு 51A(a) தேசிய கீத வழக்கு பொறி)",
                "points": {
                    "en": [
                        "TRAP: Believing that non-singing of the National Anthem automatically constitutes a criminal offense under Art 51A(a).",
                        "FACT: In Bijoe Emmanuel (1986), Supreme Court ruled that standing respectfully during the anthem fulfills Art 51A(a). Forceful singing violates Art 19(1)(a) & Art 25 if non-singing is based on genuine religious faith."
                    ],
                    "ta": [
                        "பொறி: தேசியக் கீதம் பாடாமல் இருப்பது உறுப்பு 51A(a)-ன் கீழ் தானாகவே குற்றமாகும் என்று நம்புவது.",
                        "உண்மை: பிஜோய் இம்மானுவேல் (1986) வழக்கில், தேசியக் கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது என்றும், பாடாமல் இருப்பது உண்மையான மத நம்பிக்கையின் அடிப்படையில் இருந்தால் கட்டாயப்படுத்தி பாட வைப்பது உறுப்புகள் 19(1)(a) & 25-ஐ மீறுகிறது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
                    ]
                }
            },
            {
                "title": "6. Sovereignty, Unity & Integrity Sequence Trap (இறையாண்மை, ஒற்றுமை, ஒருமைப்பாடு வரிசைப் பொறி)",
                "points": {
                    "en": [
                        "TRAP: Incorrect ordering of terms in Article 51A(c).",
                        "FACT: The exact constitutional phrase in Article 51A(c) is 'Sovereignty, Unity and Integrity of India' (in that exact sequence)."
                    ],
                    "ta": [
                        "பொறி: உறுப்பு 51A(c)-ல் உள்ள சொற்களின் தவறான வரிசை.",
                        "உண்மை: உறுப்பு 51A(c)-ல் உள்ள சரியான அரசியலமைப்பு சொற்றொடர் 'இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு' (அதே சரியான வரிசையில்)."
                    ]
                }
            }
        ],
        "important_facts": {
            "en": [
                "Fundamental Duties were added by the 42nd Constitutional Amendment Act, 1976 based on Swaran Singh Committee recommendations.",
                "Part IVA consists of only one Article: Article 51A.",
                "Original 1950 Constitution contained NO Fundamental Duties; 42nd CAA added 10 duties; 86th CAA added the 11th duty.",
                "Fundamental Duties are borrowed from the USSR (Soviet Union) Constitution.",
                "Fundamental Duties apply EXCLUSIVELY to Citizens of India (not to foreigners).",
                "Fundamental Duties are non-justiciable; courts cannot issue writs directly for their violation without statutory laws.",
                "Swaran Singh Committee recommended 8 duties, including duty to pay taxes and penalty for non-performance, which were REJECTED by Parliament.",
                "Article 51A(a) mandates respect for the Constitution, National Flag, and National Anthem (enforced by Prevention of Insults to National Honour Act 1971).",
                "Article 51A(c) commands upholding Sovereignty, Unity, and Integrity of India.",
                "Article 51A(e) commands promoting brotherhood and renouncing practices derogatory to the dignity of women.",
                "Article 51A(k) added by 86th CAA 2002 commands parents/guardians to provide education opportunities to children aged 6–14 years.",
                "Bijoe Emmanuel (1986) case established that standing respectfully during National Anthem fulfills Article 51A(a)."
            ],
            "ta": [
                "ஸ்வரன் சிங் குழுவின் பரிந்துரைகளின் அடிப்படையில் 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் அடிப்படை கடமைகள் சேர்க்கப்பட்டன.",
                "பகுதி IVA உறுப்பு 51A என்ற ஒரே ஒரு உறுப்பைக் கொண்டுள்ளது.",
                "அசல் 1950 அரசியலமைப்பில் அடிப்படை கடமைகள் இல்லை; 42வது திருத்தம் 10 கடமைகளைச் சேர்த்தது; 86வது திருத்தம் 11வது கடமையைச் சேர்த்தது.",
                "அடிப்படை கடமைகள் முன்னாள் சோவியத் யூனியன் (USSR) அரசியலமைப்பிலிருந்து பெறப்பட்டவை.",
                "அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும் (வெளிநாட்டினருக்கு அல்ல).",
                "அடிப்படை கடமைகள் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாதவை; சட்டப்பூர்வ சட்டங்கள் இன்றி அவற்றின் மீறலுக்கு நீதிமன்றங்கள் பேராணை பிறப்பிக்க முடியாது.",
                "வரி செலுத்தும் கடமை மற்றும் கடமை தவறியதற்கான தண்டனை உட்பட 8 கடமைகளை ஸ்வரன் சிங் குழு பரிந்துரைத்தது, ஆனால் அவை நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டன.",
                "உறுப்பு 51A(a) அரசியலமைப்பு, தேசியக் கொடி மற்றும் தேசியக் கீதத்தை மதிக்க ஆணையிடுகிறது (1971 தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம் மூலம் அமலாகிறது).",
                "உறுப்பு 51A(c) இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேண ஆணையிடுகிறது.",
                "உறுப்பு 51A(e) சகோதரத்துவத்தை வளர்க்கவும் பெண்களின் கண்ணியத்திற்கு இழுக்கு விளைவிக்கும் பழக்கங்களைக் கைவிடவும் ஆணையிடுகிறது.",
                "2002-ன் 86வது திருத்தத்தால் சேர்க்கப்பட்ட உறுப்பு 51A(k) 6-14 வயது குழந்தைகளுக்குக் கல்வி வாய்ப்புகளை வழங்குமாறு பெற்றோர்/பாதுகாவலர்களுக்கு ஆணையிடுகிறது.",
                "பிஜோய் இம்மானுவேல் (1986) வழக்கு தேசிய கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது என நிறுவியது."
            ]
        },
        "quick_revision": {
            "en": [
                "Part IVA & Article 51A: Added by 42nd Amendment Act 1976 on Swaran Singh Committee recommendations (original 10 duties).",
                "86th Amendment Act 2002: Added 11th Duty [Article 51A(k)] for parent/guardian to provide education for children 6–14 yrs.",
                "Origin: Borrowed from USSR Constitution. Japan is the only major democracy with explicit duties.",
                "Scope: Applies ONLY to citizens. Non-justiciable in courts without parliamentary legislation.",
                "Swaran Singh Rejected Items: Duty to pay taxes & Penalties for non-performance were NOT included in Article 51A.",
                "Article 51A(a): Respect Constitution, National Flag & Anthem (Prevention of Insults to National Honour Act 1971).",
                "Article 51A(b): Cherish freedom struggle noble ideals (Ahimsa, secularism, unity).",
                "Article 51A(c): Uphold Sovereignty, Unity and Integrity of India (UAPA 1967).",
                "Article 51A(d): Defend country & render national service when called.",
                "Article 51A(e): Promote harmony/brotherhood & renounce practices derogatory to women's dignity.",
                "Article 21A (FR) = State Duty | Article 51A(k) (FD) = Parent Duty for child education (6-14 yrs).",
                "Bijoe Emmanuel Case 1986: Standing respectfully during National Anthem fulfills Art 51A(a); silent standing protected under Art 19(1)(a) & 25."
            ],
            "ta": [
                "பகுதி IVA & உறுப்பு 51A: ஸ்வரன் சிங் குழு பரிந்துரைகளின் படி 1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டது (அசல் 10 கடமைகள்).",
                "86வது திருத்தம் 2002: 6-14 வயது குழந்தைகளுக்குப் பெற்றோர்/பாதுகாவலர் கல்வி வாய்ப்பளிக்க 11வது கடமையை [உறுப்பு 51A(k)] சேர்த்தது.",
                "தோற்றுவாய்: USSR அரசியலமைப்பிலிருந்து பெறப்பட்டது. வெளிப்படையான கடமைகளைக் கொண்ட ஒரே முக்கிய ஜனநாயகம் ஜப்பான்.",
                "எல்லை: குடிமக்களுக்கு மட்டுமே பொருந்தும். நாடாளுமன்றச் சட்டங்கள் இன்றி நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாது.",
                "ஸ்வரன் சிங் நிராகரிக்கப்பட்டவை: வரி செலுத்தும் கடமை & தண்டனைகள் உறுப்பு 51A-ல் சேர்க்கப்படவில்லை.",
                "உறுப்பு 51A(a): அரசியலமைப்பு, தேசியக் கொடி & கீதத்தை மதித்தல் (1971 தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம்).",
                "உறுப்பு 51A(b): சுதந்திரப் போராட்ட உயரிய லட்சியங்களைப் பேணுதல் (அகிம்சை, மதச்சார்பின்மை, ஒற்றுமை).",
                "உறுப்பு 51A(c): இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணுதல் (UAPA 1967).",
                "உறுப்பு 51A(d): தேசத்தைப் பாதுகாத்தல் & தேவைப்படும்போது தேசிய சேவை ஆற்றுதல்.",
                "உறுப்பு 51A(e): நல்லிணக்கம்/சகோதரத்துவத்தை வளர்த்தல் & பெண்களின் கண்ணியத்திற்கு இழுக்கு விளைவிக்கும் பழக்கங்களைக் கைவிடுதல்.",
                "உறுப்பு 21A (FR) = அரசு கடமை | உறுப்பு 51A(k) (FD) = பெற்றோர் கடமை (6-14 வயது குழந்தைகள் கல்வி).",
                "பிஜோய் இம்மானுவேல் வழக்கு 1986: தேசிய கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது; அமைதியாக நிற்பது உறுப்புகள் 19(1)(a) & 25-ன் கீழ் பாதுகாக்கப்படுகிறது."
            ]
        },
        "revision_cards": [
            {
                "id": "card_1",
                "front_en": "Which Part and Article of the Constitution contain Fundamental Duties?",
                "front_ta": "அரசியலமைப்பின் எந்தப் பகுதி மற்றும் உறுப்பில் அடிப்படை கடமைகள் உள்ளன?",
                "back_en": "Part IVA and Article 51A (inserted by 42nd Amendment Act, 1976).",
                "back_ta": "பகுதி IVA மற்றும் உறுப்பு 51A (1976-ன் 42வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது)."
            },
            {
                "id": "card_2",
                "front_en": "Which committee recommended the inclusion of Fundamental Duties?",
                "front_ta": "அடிப்படை கடமைகளைச் சேர்க்கப் பரிந்துரைத்த குழு எது?",
                "back_en": "Sardar Swaran Singh Committee (1976). It recommended 8 duties.",
                "back_ta": "சர்தார் ஸ்வரன் சிங் குழு (1976). இது 8 கடமைகளைப் பரிந்துரைத்தது."
            },
            {
                "id": "card_3",
                "front_en": "Were Fundamental Duties present in the original 1950 Constitution?",
                "front_ta": "அசல் 1950 அரசியலமைப்பில் அடிப்படை கடமைகள் இருந்தனவா?",
                "back_en": "NO. They were added in 1976 by the 42nd CAA (10 duties) and expanded in 2002 by 86th CAA (11th duty).",
                "back_ta": "இல்லை. அவை 1976-ல் 42வது திருத்தத்தால் (10 கடமைகள்) சேர்க்கப்பட்டு, 2002-ல் 86வது திருத்தத்தால் (11வது கடமை) விரிவாக்கப்பட்டன."
            },
            {
                "id": "card_4",
                "front_en": "From which country's constitution were Fundamental Duties borrowed?",
                "front_ta": "அடிப்படை கடமைகள் எந்த நாட்டின் அரசியலமைப்பிலிருந்து பெறப்பட்டன?",
                "back_en": "USSR (former Soviet Union) Constitution.",
                "back_ta": "முன்னாள் சோவியத் யூனியன் (USSR) அரசியலமைப்பு."
            },
            {
                "id": "card_5",
                "front_en": "Is the 'Duty to Pay Taxes' a Fundamental Duty under Article 51A?",
                "front_ta": "'வரி செலுத்தும் கடமை' உறுப்பு 51A-ன் கீழ் ஒரு அடிப்படை கடமையா?",
                "back_en": "NO. Swaran Singh Committee recommended it, but Parliament REJECTED it. It is NOT in Article 51A.",
                "back_ta": "இல்லை. ஸ்வரன் சிங் குழு அதைப் பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் அதை நிராகரித்தது. அது உறுப்பு 51A-ல் இல்லை."
            },
            {
                "id": "card_6",
                "front_en": "Do Fundamental Duties apply to foreigners residing in India?",
                "front_ta": "இந்தியாவில் வசிக்கும் வெளிநாட்டினருக்கு அடிப்படை கடமைகள் பொருந்துமா?",
                "back_en": "NO. Fundamental Duties apply EXCLUSIVELY to Citizens of India.",
                "back_ta": "இல்லை. அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்."
            },
            {
                "id": "card_7",
                "front_en": "What is the difference between Article 21A and Article 51A(k)?",
                "front_ta": "உறுப்பு 21A மற்றும் உறுப்பு 51A(k) இடையே உள்ள வேறுபாடு என்ன?",
                "back_en": "Article 21A is a Fundamental Right making free education a STATE duty; Article 51A(k) is a Fundamental Duty making education opportunities a PARENT/GUARDIAN duty for 6-14 yr children.",
                "back_ta": "உறுப்பு 21A என்பது இலவசக் கல்வியை அரசின் கடமையாக்கும் அடிப்படை உரிமை; உறுப்பு 51A(k) என்பது 6-14 வயது குழந்தைகளுக்குக் கல்வி வாய்ப்பளிப்பதைப் பெற்றோர்/பாதுகாவலரின் கடமையாக்கும் அடிப்படை கடமை."
            },
            {
                "id": "card_8",
                "front_en": "What was the ruling in Bijoe Emmanuel v. State of Kerala (1986)?",
                "front_ta": "பிஜோய் இம்மானுவேல் vs கேரளா மாநிலம் (1986) வழக்கில் வழங்கப்பட்ட தீர்ப்பு என்ன?",
                "back_en": "Standing respectfully during the National Anthem fulfills Article 51A(a). Forceful singing violates Right to Freedom of Speech & Religion (Art 19(1)(a) & 25).",
                "back_ta": "தேசியக் கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது. கட்டாயப்படுத்தி பாட வைப்பது பேச்சுரிமை & மத சுதந்திரத்தை மீறுகிறது (உறுப்புகள் 19(1)(a) & 25)."
            }
        ]
    }
}

target_file = "data/notes/polity/fundamental_duties_part_1.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(notes_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {target_file}")
