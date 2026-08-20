# build_preamble_part2_notes.py
import json
import os
import shutil

def generate_preamble_part2_payload():
    note = {
        "meta": {
            "topic_id": "polity_preamble_part_2",
            "repository_id": "polity_preamble",
            "display_title": "Preamble of the Constitution of India – Part 2",
            "part": 2,
            "total_parts": 2,
            "subject": "polity",
            "chapter": "Preamble of the Constitution of India",
            "language": "English + Tamil"
        },
        "metadata": {
            "version": "1.0",
            "status": "approved",
            "review_status": "gold_standard",
            "difficulty": "intermediate",
            "estimated_study_time": {
                "reading": "25 min",
                "revision": "10 min",
                "total": "35 min"
            }
        },
        "keywords": [
            "Constitutional Status of Preamble",
            "முகவுரையின் அரசியலமைப்பு அந்தஸ்து",
            "Berubari Union Case 1960",
            "பெருபாரி யூனியன் வழக்கு 1960",
            "Kesavananda Bharati Case 1973",
            "கேசவாநந்த பாரதி வழக்கு 1973",
            "LIC of India Case 1995",
            "LIC வழக்கு 1995",
            "SR Bommai Case 1994",
            "எஸ் ஆர் பொம்மை வழக்கு 1994",
            "Basic Structure Doctrine",
            "அடிப்படை கட்டமைப்பு கோட்பாடு",
            "Amendability of Preamble",
            "முகவுரையின் திருத்தப்படும் தன்மை",
            "Article 368",
            "உறுப்பு 368",
            "42nd Amendment Act 1976",
            "42வது திருத்தச் சட்டம் 1976",
            "Non-Justiciable",
            "நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது",
            "Interpretive Guide",
            "விளக்கமளிக்கும் வழிகாட்டி"
        ],
        "learning_outcomes": {
            "Understand": {
                "en": [
                    "Understand the judicial evolution regarding whether the Preamble is a part of the Constitution.",
                    "Understand the contrast between Berubari Union Case (1960) and Kesavananda Bharati Case (1973).",
                    "Understand the amendability of the Preamble under Article 368 subject to the Basic Structure limitation.",
                    "Understand why the Preamble serves as an interpretive guide but is non-justiciable and non-enforceable."
                ],
                "ta": [
                    "முகவுரை அரசியலமைப்பின் ஒரு பகுதியா இல்லையா என்பது குறித்த நீதித்துறை வளர்ச்சியினைப் புரிந்துகொள்ளுதல்.",
                    "பெருபாரி யூனியன் வழக்கு (1960) மற்றும் கேசவாநந்த பாரதி வழக்கு (1973) இடையேயான வேறுபாட்டைப் புரிந்துகொள்ளுதல்.",
                    "அடிப்படை கட்டமைப்பு வரம்பிற்கு உட்பட்டு உறுப்பு 368 இன் கீழ் முகவுரையின் திருத்தப்படும் தன்மையைப் புரிந்துகொள்ளுதல்.",
                    "முகவுரை ஏன் ஒரு விளக்கமளிக்கும் வழிகாட்டியாக செயல்படுகிறது, ஆனால் நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது என்பதைப் புரிந்துகொள்ளுதல்."
                ]
            },
            "Remember": {
                "en": [
                    "Remember key case years: Berubari Union Case (1960), Kesavananda Bharati Case (1973), S.R. Bommai Case (1994), LIC of India Case (1995).",
                    "Remember that Preamble has been amended ONLY ONCE so far by the 42nd Constitutional Amendment Act, 1976.",
                    "Remember the 3 words added in 1976: 'Socialist', 'Secular', and 'Integrity'.",
                    "Remember that Preamble is NEITHER a source of power to legislature NOR a prohibition upon the powers of legislature."
                ],
                "ta": [
                    "முக்கிய வழக்கின் ஆண்டுகளை நினைவில் கொள்ளுதல்: பெருபாரி யூனியன் வழக்கு (1960), கேசவாநந்த பாரதி வழக்கு (1973), எஸ்.ஆர். பொம்மை வழக்கு (1994), எல்ஐசி வழக்கு (1995).",
                    "முகவுரை இதுவரை ஒரே ஒரு முறை மட்டுமே 1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் திருத்தப்பட்டது என்பதை நினைவில் கொள்ளுதல்.",
                    "1976 இல் சேர்க்கப்பட்ட 3 சொற்களை நினைவில் கொள்ளுதல்: 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு'.",
                    "முகவுரை சட்டமன்றத்திற்கு அதிகாரம் அளிக்கும் மூலமும் அல்ல, சட்டமன்ற அதிகாரங்கள் மீதான தடையும் அல்ல என்பதை நினைவில் கொள்ளுதல்."
                ]
            },
            "Analyze": {
                "en": [
                    "Analyze how the Supreme Court used the Preamble to construct the Basic Structure Doctrine in 1973.",
                    "Analyze the operational distinction between the Preamble and enforceable constitutional provisions (Part III vs Preamble).",
                    "Analyze the 9 core conceptual distinctions ('Do Not Confuse' section)."
                ],
                "ta": [
                    "1973 இல் அடிப்படை கட்டமைப்பு கோட்பாட்டை உருவாக்க உச்ச நீதிமன்றம் முகவுரையை எவ்வாறு பயன்படுத்தியது என்பதை பகுப்பாய்வு செய்தல்.",
                    "முகவுரை மற்றும் அமல்படுத்தக்கூடிய அரசியலமைப்பு விதிகளுக்கு இடையிலான நடைமுறை வேறுபாட்டை பகுப்பாய்வு செய்தல்.",
                    "9 முக்கிய கருத்து வேறுபாடுகளை பகுப்பாய்வு செய்தல் ('குழப்பிக் கொள்ளக்கூடாதவை' பகுதி)."
                ]
            },
            "Apply": {
                "en": [
                    "Resolve statement-based and assertion-reason questions on Preamble cases and amendability in TNPSC Group 1.",
                    "Avoid high-frequency TNPSC exam traps regarding non-justiciability and source of power."
                ],
                "ta": [
                    "டிஎன்பிஎஸ்சி குரூப் 1 தேர்வில் முகவுரை வழக்குகள் மற்றும் திருத்தப்படும் தன்மை பற்றிய கூற்று-காரணம் வினாக்களுக்குத் துல்லியமாக விடையளித்தல்.",
                    "நீதிமன்றத்தால் நிலைநிறுத்த முடியாத தன்மை மற்றும் அதிகார மூலம் தொடர்பான டிஎன்பிஎஸ்சி தேர்வுப் பொறிகளைத் தவிர்த்தல்."
                ]
            }
        },
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India – Part 2",
        "language": "bilingual",
        "ui_type": "polity",
        "sections": [
            {
                "id": "sec_constitutional_status",
                "title_en": "1. Constitutional Status of the Preamble",
                "title_ta": "1. முகவுரையின் அரசியலமைப்பு அந்தஸ்து",
                "type": "standard_topic"
            },
            {
                "id": "sec_berubari_case",
                "title_en": "2. Berubari Union Case (1960)",
                "title_ta": "2. பெருபாரி யூனியன் வழக்கு (1960)",
                "type": "standard_topic"
            },
            {
                "id": "sec_kesavananda_case",
                "title_en": "3. Kesavananda Bharati Case (1973)",
                "title_ta": "3. கேசவாநந்த பாரதி வழக்கு (1973)",
                "type": "standard_topic"
            },
            {
                "id": "sec_other_landmark_cases",
                "title_en": "4. Other Landmark Cases (LIC 1995 & SR Bommai 1994)",
                "title_ta": "4. பிற வரலாற்றுச் சிறப்புமிக்க வழக்குகள் (LIC 1995 & பொம்மை வழக்கு 1994)",
                "type": "standard_topic"
            },
            {
                "id": "sec_42nd_amendment",
                "title_en": "5. 42nd Constitutional Amendment Act, 1976",
                "title_ta": "5. 42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
                "type": "standard_topic"
            },
            {
                "id": "sec_amendability_art368",
                "title_en": "6. Can the Preamble be Amended under Article 368?",
                "title_ta": "6. உறுப்பு 368 இன் கீழ் முகவுரையைத் திருத்த முடியுமா?",
                "type": "standard_topic"
            },
            {
                "id": "sec_basic_structure_relation",
                "title_en": "7. Preamble and the Basic Structure Doctrine",
                "title_ta": "7. முகவுரையும் அடிப்படை கட்டமைப்பு கோட்பாடும்",
                "type": "standard_topic"
            },
            {
                "id": "sec_interpretive_guide",
                "title_en": "8. Preamble as an Interpretive Guide & Non-Justiciability",
                "title_ta": "8. விளக்கமளிக்கும் வழிகாட்டியாக முகவுரை & நிலைநிறுத்த முடியாத தன்மை",
                "type": "standard_topic"
            },
            {
                "id": "sec_preamble_fr_dpsp_fd",
                "title_en": "9. Inter-relationship with FRs, DPSPs, and Fundamental Duties",
                "title_ta": "9. அடிப்படை உரிமைகள், DPSP மற்றும் கடமைகளுடனான தொடர்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_do_not_confuse",
                "title_en": "10. Important Distinctions: 'Do Not Confuse'",
                "title_ta": "10. முக்கிய வேறுபாடுகள்: 'குழப்பிக் கொள்ளக்கூடாதவை'",
                "type": "standard_topic"
            },
            {
                "id": "sec_preamble_architecture_flow",
                "title_en": "11. Conceptual Flow & Timeline of Preamble Jurisprudence",
                "title_ta": "11. முகவுரை சட்டத்தின் கருத்து ஓட்டம் & காலவரிசை",
                "type": "standard_topic"
            }
        ],
        "content": {
            "definition": {
                "en": "Part 2 of the Preamble chapter examines the constitutional status, judicial evolution, amendability under Article 368, the 42nd Amendment Act 1976, its non-justiciable character, and its pivotal role as an interpretive compass for the Basic Structure Doctrine.",
                "ta": "முகவுரை அத்தியாயத்தின் பகுதி 2 அரசியலமைப்பு அந்தஸ்து, நீதித்துறை வளர்ச்சி, உறுப்பு 368 இன் கீழ் திருத்தப்படும் தன்மை, 1976 இன் 42வது திருத்தச் சட்டம், நீதிமன்றத்தால் நிலைநிறுத்த முடியாத தன்மை மற்றும் அடிப்படை கட்டமைப்பு கோட்பாட்டிற்கான விளக்கமளிக்கும் திசைகாட்டியாக இதன் முக்கிய பங்கினை ஆராய்கிறது."
            },
            "introduction": {
                "en": "For decades following independence, a fierce legal debate persisted over whether the Preamble is formally a part of the Constitution and whether Parliament possesses the power to amend it under Article 368. This part traces the historic shift from the Berubari Union Case (1960) to the landmark Kesavananda Bharati Case (1973) and LIC of India Case (1995), detailing the 42nd Amendment Act 1976 and the exact boundaries of constitutional interpretation.",
                "ta": "சுதந்திரத்திற்குப் பிந்தைய தசாப்தங்களில், முகவுரை முறையான அரசியலமைப்பின் ஒரு பகுதியா மற்றும் உறுப்பு 368 இன் கீழ் நாடாளுமன்றத்திற்கு அதைத் திருத்த அதிகாரம் உள்ளதா என்பது குறித்து ஒரு கடுமையான சட்ட விவாதம் நீடித்தது. இந்த பகுதி பெருபாரி யூனியன் வழக்கில் (1960) இருந்து வரலாற்றுச் சிறப்புமிக்க கேசவாநந்த பாரதி வழக்கு (1973) மற்றும் எல்ஐசி வழக்குகளுக்கு (1995) நீதித்துறை நிலைப்பாடு மாறியதைக் கண்டறிகிறது."
            },
            "sec_constitutional_status": [
                {
                    "title": "1. The Historical & Judicial Debate (அரசியலமைப்பு அந்தஸ்து விவாதம்)",
                    "points": {
                        "en": [
                            "Constitutional Issue: Is the Preamble an integral part of the Constitution of India, or is it merely an external key/preface?",
                            "Enactment Reality: In the Constituent Assembly, the Preamble was voted upon and passed AFTER the rest of the Constitution was already adopted, specifically to ensure that it was in complete conformity with the text passed by the Assembly.",
                            "President of Assembly Ruling: Dr. Rajendra Prasad explicitly declared: 'The question is that the Preamble stands part of the Constitution.' The motion was adopted by the Constituent Assembly.",
                            "Judicial Evolution: Despite this Constituent Assembly history, the Supreme Court initially took a restrictive view in 1960, which was later reversed in 1973."
                        ],
                        "ta": [
                            "அரசியலமைப்பு பிரச்சனை: முகவுரை என்பது இந்திய அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதியா, அல்லது அது வெறும் வெளிப்புற சாவி/முன்னுரையா?",
                            "இயற்றப்பட்ட உண்மை: அரசியலமைப்புச் சபையில், அரசியலமைப்பின் இதர பகுதிகள் ஏற்கனவே ஏற்றுக்கொள்ளப்பட்ட பின்னரே முகவுரையின் மீது வாக்களிக்கப்பட்டு நிறைவேற்றப்பட்டது, குறிப்பாக சபையால் நிறைவேற்றப்பட்ட உரையுடன் இது முற்றிலும் ஒத்துப்போவதை உறுதி செய்வதற்காக.",
                            "அரசியலமைப்புத் தலைவரின் தீர்ப்பு: டாக்டர் ராஜேந்திர பிரசாத் வெளிப்படையாக அறிவித்தார்: 'கேள்வி என்னவென்றால், முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது என்பதாகும்.' இந்த தீர்மானம் அரசியலமைப்புச் சபையால் ஏற்றுக்கொள்ளப்பட்டது.",
                            "நீதித்துறை வளர்ச்சி: இந்த அரசியலமைப்பு சபை வரலாறு இருந்தபோதிலும், உச்ச நீதிமன்றம் ஆரம்பத்தில் 1960 இல் ஒரு வரம்பிற்குட்பட்ட பார்வையை எடுத்தது, அது பின்னர் 1973 இல் மாற்றப்பட்டது."
                        ]
                    }
                }
            ],
            "sec_berubari_case": [
                {
                    "title": "1. Berubari Union Case, 1960 (பெருபாரி யூனியன் வழக்கு - 1960)",
                    "points": {
                        "en": [
                            "Case Context: Presidential Reference under Article 143(1) regarding the implementation of the Indo-Pakistan Agreement relating to the Berubari enclave exchange.",
                            "Supreme Court Ruling (1960): The 8-judge bench held that the Preamble is a key to open the mind of the makers and shows the general purpose for which provisions were made.",
                            "CRITICAL RULING: The Court explicitly concluded: 'The Preamble is NOT a part of the Constitution.'",
                            "Source of Power Distinction: The Court ruled that the Preamble can NEVER be regarded as a source of any substantive power conferred on the government or any of its departments.",
                            "No Limitation: Similarly, it cannot be regarded as a source of any prohibition or limitation on governmental powers.",
                            "Role in Ambiguity: The SC noted that where the terms of any article are key, clear, and unambiguous, the Preamble cannot override them. Only when terms are ambiguous can Preamble be referred for assistance."
                        ],
                        "ta": [
                            "வழக்கின் பின்னணி: பெருபாரி பகுதி பரிமாற்றம் தொடர்பான இந்திய-பாகிஸ்தான் ஒப்பந்தத்தை அமல்படுத்துவது குறித்து உறுப்பு 143(1) இன் கீழ் குடியரசுத் தலைவரின் ஆலோசனைக் கோரிக்கை.",
                            "உச்ச நீதிமன்றத் தீர்ப்பு (1960): 8 நீதிபதிகள் கொண்ட அமர்வு, முகவுரை என்பது அரசியலமைப்புச் சிற்பிகளின் சிந்தனையைத் திறக்கும் சாவி என்றும், விதிகள் உருவாக்கப்பட்ட பொதுவான நோக்கத்தைக் காட்டுகிறது என்றும் குறிப்பிட்டது.",
                            "முக்கிய தீர்ப்பு: நீதிமன்றம் வெளிப்படையாக முடிவாக்கியது: 'முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல.'",
                            "அதிகார மூல வேறுபாடு: முகவுரையை அரசாங்கத்திற்கோ அல்லது அதன் துறைகளுக்கோ வழங்கப்பட்ட எந்தவொரு உரிமையியல் அதிகாரத்தின் (substantive power) மூலமாகவும் கருத முடியாது என்று நீதிமன்றம் தீர்ப்பளித்தது.",
                            "தடை மூலம் அல்ல: அதேபோல, அரசாங்க அதிகாரங்கள் மீதான எந்தவொரு தடை அல்லது வரம்புகளின் மூலமாகவும் இதை கருத முடியாது.",
                            "தெளிவற்ற தன்மையில் பங்கு: எந்தவொரு சரத்தின் சொற்களும் தெளிவாகவும் சந்தேகத்திற்கு இடமின்றியும் இருக்கும் போது, முகவுரை அவற்றை மேலெழுத முடியாது. சொற்கள் தெளிவற்றதாக இருக்கும்போது மட்டுமே முகவுரையை உதவிக்கு பயன்படுத்த முடியும்."
                        ]
                    }
                },
                {
                    "title": "2. Historical Importance vs Later Reversal (வரலாற்று நிலையும் பின்னாளைய மாற்றமும்)",
                    "points": {
                        "en": [
                            "HISTORICAL POSITION (Berubari 1960): Preamble = NOT part of Constitution.",
                            "LATER POSITION (Kesavananda 1973): Preamble = PART of Constitution.",
                            "TNPSC Trap: Do NOT apply Berubari's ruling as current law! Berubari represents the HISTORICAL 1960 position, which was explicitly OVERRULED by Kesavananda Bharati in 1973."
                        ],
                        "ta": [
                            "வரலாற்று நிலை (பெருபாரி 1960): முகவுரை = அரசியலமைப்பின் பகுதி அல்ல.",
                            "பிந்தைய நிலை (கேசவாநந்தா 1973): முகவுரை = அரசியலமைப்பின் ஒரு பகுதி.",
                            "டிஎன்பிஎஸ்சி பொறி: பெருபாரியின் தீர்ப்பை தற்போதைய சட்டமாக பயன்படுத்த வேண்டாம்! பெருபாரி என்பது 1960 ஆம் ஆண்டின் வரலாற்று நிலையை குறிக்கிறது, அது 1973 இல் கேசவாநந்த பாரதி வழக்கில் வெளிப்படையாக ரத்து செய்யப்பட்டது."
                        ]
                    }
                }
            ],
            "sec_kesavananda_case": [
                {
                    "title": "1. Kesavananda Bharati Case, 1973 (கேசவாநந்த பாரதி வழக்கு - 1973)",
                    "points": {
                        "en": [
                            "Historic Bench: 13-judge Constitutional Bench (largest in Supreme Court history), decided by a 7-6 majority on 24th April 1973.",
                            "OVERRULING BERUBARI: The Supreme Court rejected the Berubari opinion and categorically held: 'The Preamble IS a part of the Constitution.'",
                            "Judicial Reasoning:\n1. The Preamble was voted upon and passed as part of the Constitution by the Constituent Assembly.\n2. The Preamble is of extreme importance and the Constitution should be read and interpreted in the light of the grand and noble vision expressed in the Preamble.",
                            "Basic Structure Doctrine Birth: The Court established that Parliament has wide amendment power under Article 368, but CANNOT alter or destroy the 'Basic Structure' or basic features of the Constitution.",
                            "Preamble as Basic Structure Guide: The Court observed that the noble objectives outlined in the Preamble (Sovereignty, Democracy, Republic, Secularism, Justice, Liberty, Equality) form the core elements of the Basic Structure."
                        ],
                        "ta": [
                            "வரலாற்றுச் சிறப்புமிக்க அமர்வு: 13 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு (உச்ச நீதிமன்ற வரலாற்றில் மிகப்பெரியது), ஏப்ரல் 24, 1973 அன்று 7-6 பெரும்பான்மையால் தீர்ப்பளித்தது.",
                            "பெருபாரியை ரத்து செய்தல்: உச்ச நீதிமன்றம் பெருபாரி அபிப்ராயத்தை நிராகரித்து, 'முகவுரை அரசியலமைப்பின் ஒரு பகுதி ஆகும்' என்று திட்டவட்டமாக அறிவித்தது.",
                            "நீதித்துறை தர்க்கம்:\n1. முகவுரை அரசியலமைப்புச் சபையால் வாக்களிக்கப்பட்டு அரசியலமைப்பின் ஒரு பகுதியாக நிறைவேற்றப்பட்டது.\n2. முகவுரை மிகுந்த முக்கியத்துவம் வாய்ந்தது, மேலும் முகவுரையில் வெளிப்படுத்தப்பட்டுள்ள பிரம்மாண்டமான மற்றும் உன்னதமான தொலைநோக்கின் வெளிச்சத்தில் அரசியலமைப்பு படிக்கப்பட்டு விளக்கப்பட வேண்டும்.",
                            "அடிப்படை கட்டமைப்பு கோட்பாட்டின் பிறப்பு: உறுப்பு 368 இன் கீழ் நாடாளுமன்றத்திற்கு பரந்த திருத்த அதிகாரம் உள்ளது, ஆனால் அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பு' அல்லது அடிப்படை அம்சங்களை மாற்றவோ அழிக்கவோ முடியாது என்பதை நீதிமன்றம் நிறுவியது.",
                            "அடிப்படை கட்டமைப்பு வழிகாட்டியாக முகவுரை: முகவுரையில் கோடிட்டுக் காட்டப்பட்டுள்ள உன்னதமான இலக்குகள் (இறையாண்மை, ஜனநாயகம், குடியரசு, மதச்சார்பின்மை, நீதி, சுதந்திரம், சமத்துவம்) அடிப்படை கட்டமைப்பின் முக்கிய கூறுகளை உருவாக்குகின்றன என்பதை நீதிமன்றம் குறிப்பிட்டது."
                        ]
                    }
                },
                {
                    "title": "2. Substantive Power Distinction Maintained (அதிகார மூலம் பற்றிய தீர்ப்பு)",
                    "points": {
                        "en": [
                            "CRITICAL DISTINCTION: While Kesavananda Bharati declared Preamble as PART of the Constitution, it REAFFIRMED that:\n1. Preamble is NOT an independent source of power for the legislature.\n2. Preamble is NOT a prohibition/limitation upon the powers of the legislature.\n3. Preamble is NON-JUSTICIABLE (its provisions are not enforceable in courts of law).",
                            "Key Revision Line: Preamble is PART of Constitution (Kesavananda 1973), but remains NON-JUSTICIABLE and NOT a source of power."
                        ],
                        "ta": [
                            "முக்கிய வேறுபாடு: கேசவாநந்த பாரதி முகவுரையை அரசியலமைப்பின் ஒரு பகுதி என்று அறிவித்தபோதிலும், அது பின்வருவனவற்றை மீண்டும் உறுதிப்படுத்தியது:\n1. முகவுரை சட்டமன்றத்திற்கான ஒரு சுதந்திரமான அதிகார மூலம் அல்ல.\n2. முகவுரை சட்டமன்ற அதிகாரங்கள் மீதான தடையோ வரம்போ அல்ல.\n3. முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது (non-justiciable - இதன் விதிகளை நீதிமன்றங்களில் நேரடியாக அமல்படுத்த முடியாது).",
                            "முக்கிய திருப்புதல் வரி: முகவுரை அரசியலமைப்பின் பகுதி (கேசவாநந்தா 1973), ஆனால் நீதிமன்றங்களால் நிலைநிறுத்த முடியாதது மற்றும் அதிகார மூலம் அல்ல."
                        ]
                    }
                }
            ],
            "sec_other_landmark_cases": [
                {
                    "title": "1. LIC of India Case (1995) & S.R. Bommai Case (1994) (பிற முக்கிய வழக்குகள்)",
                    "points": {
                        "en": [
                            "LIC of India Case (1995): Supreme Court once again held that 'The Preamble is an INTEGRAL PART of the Constitution.'",
                            "S.R. Bommai vs Union of India (1994): SC held that Secularism, Democracy, Federalism, and Social Justice mentioned in the Preamble are part of the Basic Structure of the Constitution. Imposition of President's Rule (Art 356) for anti-secular acts by state governments was upheld.",
                            "Minerva Mills Case (1980): SC held that harmony and balance between Fundamental Rights (Part III) and DPSP (Part IV) is an essential feature of the Basic Structure, fulfilling Preamble objectives.",
                            "Maneka Gandhi Case (1978): SC used Preamble's vision of 'Liberty' and 'Justice' to read 'Due Process of Law' into Article 21 (Personal Liberty)."
                        ],
                        "ta": [
                            "எல்ஐசி வழக்கு (1995): உச்ச நீதிமன்றம் மீண்டும் 'முகவுரை என்பது அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி' என்று தீர்ப்பளித்தது.",
                            "எஸ்.ஆர். பொம்மை vs யூனியன் ஆஃப் இந்தியா (1994): முகவுரையில் குறிப்பிடப்பட்டுள்ள மதச்சார்பின்மை, ஜனநாயகம், கூட்டாட்சி மற்றும் சமூக நீதி ஆகியவை அரசியலமைப்பின் அடிப்படை அமைப்பின் ஒரு பகுதி என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. மாநில அரசுகளின் மதச்சார்பற்ற எதிர்ப்பு நடவடிக்கைகளுக்காக குடியரசுத் தலைவர் ஆட்சி (உறுப்பு 356) விதிப்பது உறுதி செய்யப்பட்டது.",
                            "மினர்வா மில்ஸ் வழக்கு (1980): அடிப்படை உரிமைகள் (பகுதி III) மற்றும் DPSP (பகுதி IV) இடையேயான நல்லிணக்கமும் சமநிலையும் முகவுரை இலக்குகளை நிறைவேற்றும் அடிப்படை அமைப்பின் இன்றியமையாத அம்சமாகும் என்று உச்ச நீதிமன்றம் கூறியது.",
                            "மேனகா காந்தி வழக்கு (1978): உச்ச நீதிமன்றம் உறுப்பு 21 இல் (தனிநபர் சுதந்திரம்) 'சட்டத்தின் உரிய நடைமுறை' என்பதை இணைக்க முகவுரையின் 'சுதந்திரம்' மற்றும் 'நீதி' தொலைநோக்கைப் பயன்படுத்தியது."
                        ]
                    }
                }
            ],
            "sec_42nd_amendment": [
                {
                    "title": "1. Detailed Breakdown of 42nd Amendment Act, 1976 (42வது திருத்தச் சட்டம் விவரம்)",
                    "points": {
                        "en": [
                            "Sole Amendment: The Preamble has been amended ONLY ONCE in Indian constitutional history, by the 42nd Constitutional Amendment Act, 1976.",
                            "Enforcement Date: Passed in 1976, came into force on 3rd January 1977.",
                            "Three Words Added:\n1. 'SOCIALIST' (added to Nature of State)\n2. 'SECULAR' (added to Nature of State)\n3. 'INTEGRITY' (added to Fraternity section: 'Unity and Integrity of the Nation').",
                            "Prime Minister during Amendment: Mrs. Indira Gandhi (Swaran Singh Committee recommendations).",
                            "BEFORE vs AFTER Comparison:\n- Before 1976: 'SOVEREIGN DEMOCRATIC REPUBLIC'\n- After 1976: 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC'\n- Before 1976: 'unity of the Nation'\n- After 1976: 'unity and integrity of the Nation'"
                        ],
                        "ta": [
                            "ஒரே திருத்தம்: இந்திய அரசியலமைப்பு வரலாற்றில் முகவுரை இதுவரை ஒரே ஒரு முறை மட்டுமே 1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் திருத்தப்பட்டது.",
                            "அமல்படுத்தப்பட்ட நாள்: 1976 இல் நிறைவேற்றப்பட்டது, 1977 ஜனவரி 3 அன்று நடைமுறைக்கு வந்தது.",
                            "சேர்க்கப்பட்ட மூன்று சொற்கள்:\n1. 'சமதர்ம' (SOCIALIST - அரசின் தன்மையில் சேர்க்கப்பட்டது)\n2. 'மதச்சார்பற்ற' (SECULAR - அரசின் தன்மையில் சேர்க்கப்பட்டது)\n3. 'ஒருமைப்பாடு' (INTEGRITY - சகோதரத்துவப் பகுதியில் சேர்க்கப்பட்டது: 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்').",
                            "திருத்தத்தின் போது பிரதமர்: திருமதி இந்திரா காந்தி (ஸ்வரன் சிங் குழு பரிந்துரைகள்).",
                            "முன்பு vs பின்பு ஒப்பீடு:\n- 1976க்கு முன்பு: 'இறையாண்மை ஜனநாயகக் குடியரசு'\n- 1976க்கு பின்பு: 'இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயகக் குடியரசு'\n- 1976க்கு முன்பு: 'தேசத்தின் ஒற்றுமை'\n- 1976க்கு பின்பு: 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்'"
                        ]
                    }
                }
            ],
            "sec_amendability_art368": [
                {
                    "title": "1. Amendability under Article 368 & Basic Structure Limitation (உறுப்பு 368 இன் கீழ் திருத்தப்படும் தன்மை)",
                    "points": {
                        "en": [
                            "Constitutional Logic:\nArticle 368 (Amendment Power)\n  ↓\nCan Parliament amend the Preamble?\n  ↓\nYES! Because Preamble IS part of the Constitution (Kesavananda 1973)\n  ↓\nLIMITATION: Parliament CANNOT destroy/alter the Basic Structure elements embodied in the Preamble.",
                            "Practical Proof: The 42nd Amendment Act 1976 stands as historic proof that the Preamble CAN be amended under Article 368.",
                            "Harmonious Construction: Parliament can amend the Preamble to clarify, expand, or strengthen its noble goals (e.g. adding Socialist, Secular, Integrity), but cannot delete core principles like Democracy, Republic, or Secularism."
                        ],
                        "ta": [
                            "அரசியலமைப்பு தர்க்கம்:\nஉறுப்பு 368 (திருத்த அதிகாரம்)\n  ↓\nநாடாளுமன்றம் முகவுரையைத் திருத்த முடியுமா?\n  ↓\nஆம்! ஏனெனில் முகவுரை அரசியலமைப்பின் ஒரு பகுதி ஆகும் (கேசவாநந்தா 1973)\n  ↓\nவரம்பு: முகவுரையில் உள்ள அடிப்படை கட்டமைப்பு அம்சங்களை நாடாளுமன்றத்தால் அழிக்கவோ மாற்றவோ முடியாது.\nநடைமுறை ஆதாரம்: 1976 இன் 42வது திருத்தச் சட்டம் உறுப்பு 368 இன் கீழ் முகவுரையைத் திருத்த முடியும் என்பதற்கான வரலாற்றுச் சான்றாக நிற்கிறது.",
                            "சீரான விளக்கம்: நாடாளுமன்றம் முகவுரையின் உன்னதமான இலக்குகளைத் தெளிவுபடுத்தவோ, விரிவாக்கவோ அல்லது வலுப்படுத்தவோ திருத்தலாம் (எ.கா. சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு சேர்ப்பு), ஆனால் ஜனநாயகம், குடியரசு அல்லது மதச்சார்பின்மை போன்ற முக்கிய கோட்பாடுகளை நீக்க முடியாது."
                        ]
                    }
                }
            ],
            "sec_basic_structure_relation": [
                {
                    "title": "1. Relationship Between Preamble & Basic Structure (அடிப்படை கட்டமைப்பும் முகவுரையும்)",
                    "points": {
                        "en": [
                            "Reservoir of Basic Structure: The Preamble serves as the primary reservoir or catalog from which the judiciary identifies Basic Structure elements.",
                            "Basic Features Originating from Preamble:\n- Sovereign, Democratic, and Republican nature of Indian polity.\n- Secular character of the Constitution.\n- Freedom of thought, expression, belief, faith, and worship (Liberty).\n- Equality of status and opportunity.\n- Unity and Integrity of the Nation.\n- Welfare State (Social and Economic Justice).",
                            "CAUTION IN EXAM: Do NOT claim that every single word in the Preamble is automatically a separate Basic Structure element. The Supreme Court determines Basic Structure on a case-by-case basis using Preamble philosophy."
                        ],
                        "ta": [
                            "அடிப்படை கட்டமைப்பின் நீர்த்தேக்கம்: நீதித்துறை அடிப்படை கட்டமைப்பு கூறுகளை அடையாளம் காணும் முதன்மை நீர்த்தேக்கமாக அல்லது பட்டியலாக முகவுரை செயல்படுகிறது.",
                            "முகவுரையிலிருந்து உருவாகும் அடிப்படை அம்சங்கள்:\n- இந்திய அரசின் இறையாண்மை, ஜனநாயகம் மற்றும் குடியரசுத் தன்மை.\n- அரசியலமைப்பின் மதச்சார்பற்ற தன்மை.\n- சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம்.\n- தகுதி மற்றும் வாய்ப்பு சமத்துவம்.\n- தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்.\n- நலன்புரி அரசு (சமூக மற்றும் பொருளாதார நீதி).",
                            "தேர்வில் எச்சரிக்கை: முகவுரையில் உள்ள ஒவ்வொரு தனிச் சொல்லும் தானாகவே தனி அடிப்படை கட்டமைப்பு கூறு என்று கூற வேண்டாம். முகவுரை தத்துவத்தைப் பயன்படுத்தி உச்ச நீதிமன்றம் வழக்குக்கு வழக்கு அடிப்படை கட்டமைப்பைத் தீர்மானிக்கிறது."
                        ]
                    }
                }
            ],
            "sec_interpretive_guide": [
                {
                    "title": "1. Interpretive Guide vs Non-Justiciability (விளக்கமளிக்கும் வழிகாட்டி vs நிலைநிறுத்த முடியாத தன்மை)",
                    "points": {
                        "en": [
                            "Interpretive Aid: When the text of an Article is ambiguous or capable of two interpretations, courts adopt the interpretation that aligns with the noble objectives of the Preamble.",
                            "Non-Justiciable Nature: Provisions of the Preamble are NOT enforceable in courts of law. A citizen cannot file a writ petition under Article 32 or 226 seeking enforcement of the Preamble alone.",
                            "Not a Source of Substantive Power: Preamble does NOT grant any legislative or executive power, nor does it impose limitations on constitutional provisions.",
                            "Operative Provisions Prevail: If there is a direct conflict between an unambiguous constitutional provision and the Preamble, the operative constitutional provision prevails in court."
                        ],
                        "ta": [
                            "விளக்கமளிக்கும் உதவி: ஒரு சரத்தின் உரை தெளிவற்றதாக இருக்கும்போது அல்லது இரண்டு விளக்கங்களுக்கு இடம் தரும்போது, முகவுரையின் உன்னதமான இலக்குகளுடன் ஒத்துப்போகும் விளக்கத்தை நீதிமன்றங்கள் ஏற்றுக்கொள்கின்றன.",
                            "நீதிமன்றத்தால் நிலைநிறுத்த முடியாத தன்மை: முகவுரையின் விதிகளை நீதிமன்றங்களில் நேரடியாக அமல்படுத்த முடியாது. முகவுரையை மட்டும் அமல்படுத்தக் கோரி உறுப்பு 32 அல்லது 226 இன் கீழ் ஒரு குடிமகன் பேராணை மனு தாக்கல் செய்ய முடியாது.",
                            "உரிமையியல் அதிகார மூலம் அல்ல: முகவுரை எந்தவொரு சட்டமன்ற அல்லது நிர்வாக அதிகாரத்தையும் வழங்காது, அதேபோல அரசியலமைப்பு விதிகளின் மீது தடைகளையும் விதிக்காது.",
                            "செயல்படும் விதிகள் வெல்லும்: தெளிவான அரசியலமைப்பு விதிக்கும் முகவுரைக்கும் இடையே நேரடி மோதல் ஏற்பட்டால், நீதிமன்றத்தில் செயல்படும் அரசியலமைப்பு விதியே வெல்லும்."
                        ]
                    }
                }
            ],
            "sec_preamble_fr_dpsp_fd": [
                {
                    "title": "1. Organic Triad: Preamble, FRs, DPSPs, and FDs (அரசியலமைப்பு இணைப்பு)",
                    "points": {
                        "en": [
                            "Integrated Architecture:\n- Preamble = Declaration of Vision & Goals (Grand Blueprint)\n- Fundamental Rights (Part III) = Civil & Political Guarantee (Liberty & Equality)\n- Directive Principles (Part IV) = Social & Economic Mandate (Justice & Welfare State)\n- Fundamental Duties (Part IVA) = Citizen Responsibility (Fraternity & Integrity)",
                            "Judicial View: In Minerva Mills (1980), SC observed that Part III and Part IV are two wheels of a chariot; Preamble provides the direction for the journey."
                        ],
                        "ta": [
                            "ஒருங்கிணைந்த கட்டமைப்பு:\n- முகவுரை = தொலைநோக்கு & இலக்குகளின் பிரகடனம் (பெரும் நீலவரைபடம்)\n- அடிப்படை உரிமைகள் (பகுதி III) = குடிமை & அரசியல் உத்தரவாதம் (சுதந்திரம் & சமத்துவம்)\n- வழிகாட்டு நெறிமுறைகள் (பகுதி IV) = சமூக & பொருளாதார ஆணை (நீதி & நலன்புரி அரசு)\n- அடிப்படை கடமைகள் (பகுதி IVA) = குடிமகன் பொறுப்பு (சகோதரத்துவம் & ஒருமைப்பாடு)",
                            "நீதித்துறை பார்வை: மினர்வா மில்ஸ் (1980) வழக்கில், பகுதி III மற்றும் பகுதி IV ஆகியவை ஒரு ரதத்தின் இரு சக்கரங்கள்; முகவுரை பயணத்திற்கான திசையை வழங்குகிறது என்று உச்ச நீதிமன்றம் குறிப்பிட்டது."
                        ]
                    }
                }
            ],
            "sec_do_not_confuse": [
                {
                    "title": "1. Nine Critical Conceptual Distinctions (குழப்பிக் கொள்ளக்கூடாத 9 முக்கிய வேறுபாடுகள்)",
                    "points": {
                        "en": [
                            "1. Preamble ≠ Fundamental Rights (Preamble is non-justiciable; FRs are justiciable under Art 32).\n2. Preamble ≠ DPSP (Preamble is introductory vision; DPSPs are specific policy directives in Part IV).\n3. Preamble ≠ Source of Power (Preamble confers no legislative/executive power).\n4. Preamble ≠ Independent Legal Remedy (Cannot sue solely on Preamble breach).\n5. Democracy ≠ Republic (UK is Democratic but Monarchy; India is Democratic AND Republic).\n6. Secularism ≠ Anti-Religious Hostility (Indian secularism = Positive equal respect Sarva Dharma Sambhava).\n7. Socialism ≠ State Monopoly of All Property (Indian socialism = Democratic socialism & Mixed Economy).\n8. Fraternity ≠ Forced Cultural Uniformity (Fraternity = Brotherhood respecting individual dignity).\n9. Berubari 1960 ≠ Kesavananda 1973 (Berubari said NOT part; Kesavananda overruled and declared IS part)."
                        ],
                        "ta": [
                            "1. முகவுரை ≠ அடிப்படை உரிமைகள் (முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது; அடிப்படை உரிமைகள் உறுப்பு 32 இன் கீழ் நிலைநிறுத்தக்கூடியவை).\n2. முகவுரை ≠ DPSP (முகவுரை என்பது அறிமுகத் தொலைநோக்கு; DPSP என்பது பகுதி IV இல் உள்ள குறிப்பிட்ட கொள்கை வழிகாட்டுதல்கள்).\n3. முகவுரை ≠ அதிகார மூலம் (முகவுரை எந்த சட்டமன்ற/நிர்வாக அதிகாரத்தையும் வழங்காது).\n4. முகவுரை ≠ சுதந்திரமான சட்டத் தீர்வு (முகவுரை மீறலுக்காக மட்டும் வழக்கு தொடர முடியாது).\n5. ஜனநாயகம் ≠ குடியரசு (இங்கிலாந்து ஜனநாயகம் ஆனால் முடியாட்சி; இந்தியா ஜனநாயகம் மற்றும் குடியரசு).\n6. மதச்சார்பின்மை ≠ மத எதிர்ப்பு (இந்திய மதச்சார்பின்மை = நேர்மறை சம மரியாதை சர்வ தர்ம சம்பவ).\n7. சமதர்மம் ≠ அரசின் அனைத்து சொத்து ஆதிக்கம் (இந்திய சமதர்மம் = ஜனநாயக சமதர்மம் & கலப்பு பொருளாதாரம்).\n8. சகோதரத்துவம் ≠ கட்டாய கலாச்சார சீரான தன்மை (சகோதரத்துவம் = தனிமனித கண்ணியத்தை மதிக்கும் சகோதரத்துவம்).\n9. பெருபாரி 1960 ≠ கேசவாநந்தா 1973 (பெருபாரி பகுதி அல்ல என்றது; கேசவாநந்தா அதை ரத்து செய்து பகுதி தான் என்றது)."
                        ]
                    }
                }
            ],
            "sec_preamble_architecture_flow": [
                {
                    "title": "1. Conceptual Timeline & Revision Flow (காலவரிசையும் கருத்து ஓட்டமும்)",
                    "points": {
                        "en": [
                            "Chronological Evolution:\nDec 13, 1946: Objectives Resolution moved by Nehru\nJan 22, 1947: Objectives Resolution adopted by Assembly\nNov 26, 1949: Constitution & Preamble Adopted\nJan 26, 1950: Constitution Came into Force\n1960: Berubari Union Case (Preamble NOT part)\n1973: Kesavananda Bharati Case (Overruled Berubari; Preamble IS part; Basic Structure created)\n1976: 42nd Amendment Act (Added Socialist, Secular, Integrity)\n1994: S.R. Bommai Case (Secularism confirmed as Basic Structure)\n1995: LIC of India Case (Reaffirmed Integral Part)"
                        ],
                        "ta": [
                            "காலவரிசை வளர்ச்சி:\nடிசம்பர் 13, 1946: நேருவால் குறிக்கோள் தீர்மானம் முன்மொழியப்பட்டது\nஜனவரி 22, 1947: சபையால் குறிக்கோள் தீர்மானம் ஏற்றுக்கொள்ளப்பட்டது\nநவம்பர் 26, 1949: அரசியலமைப்பு & முகவுரை ஏற்றுக்கொள்ளப்பட்டது\nஜனவரி 26, 1950: அரசியலமைப்பு நடைமுறைக்கு வந்தது\n1960: பெருபாரி யூனியன் வழக்கு (முகவுரை பகுதி அல்ல)\n1973: கேசவாநந்த பாரதி வழக்கு (பெருபாரியை ரத்து செய்தது; முகவுரை பகுதி; அடிப்படை கட்டமைப்பு உருவாக்கப்பட்டது)\n1976: 42வது திருத்தச் சட்டம் (சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு சேர்க்கப்பட்டது)\n1994: எஸ்.ஆர். பொம்மை வழக்கு (மதச்சார்பின்மை அடிப்படை அமைப்பாக உறுதி செய்யப்பட்டது)\n1995: எல்ஐசி வழக்கு (ஒருங்கிணைந்த பகுதி என மீண்டும் உறுதிப்படுத்தப்பட்டது)"
                        ]
                    }
                }
            ]
        },
        "important_facts": {
            "en": [
                "Berubari Union Case (1960) held Preamble is NOT part of Constitution.",
                "Kesavananda Bharati Case (1973) OVERRULED Berubari and held Preamble IS part of Constitution.",
                "LIC of India Case (1995) reaffirmed Preamble is an INTEGRAL PART of Constitution.",
                "Preamble can be amended under Article 368 subject to Basic Structure limitation.",
                "Preamble amended ONLY ONCE so far by 42nd Constitutional Amendment Act, 1976.",
                "42nd Amendment added 3 words: Socialist, Secular, Integrity.",
                "Preamble is NON-JUSTICIABLE (cannot be enforced directly in courts).",
                "Preamble is NEITHER a source of power NOR a restriction on power of legislature."
            ],
            "ta": [
                "பெருபாரி யூனியன் வழக்கு (1960) முகவுரை அரசியலமைப்பின் பகுதி அல்ல என்று தீர்ப்பளித்தது.",
                "கேசவாநந்த பாரதி வழக்கு (1973) பெருபாரியை ரத்து செய்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்று தீர்ப்பளித்தது.",
                "எல்ஐசி வழக்கு (1995) முகவுரை ஒரு ஒருங்கிணைந்த பகுதி என்பதை மீண்டும் உறுதிப்படுத்தியது.",
                "அடிப்படை கட்டமைப்பு வரம்பிற்கு உட்பட்டு உறுப்பு 368 இன் கீழ் முகவுரையைத் திருத்த முடியும்.",
                "முகவுரை இதுவரை ஒரே ஒரு முறை மட்டுமே 1976 இன் 42வது திருத்தச் சட்டத்தால் திருத்தப்பட்டது.",
                "42வது திருத்தம் 3 சொற்களைச் சேர்த்தது: சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு.",
                "முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது (நீதிமன்றங்களில் நேரடியாக அமல்படுத்த முடியாது).",
                "முகவுரை சட்டமன்றத்திற்கு அதிகார மூலமும் அல்ல, அதிகாரத்தின் மீதான தடையும் அல்ல."
            ]
        },
        "tnpsc_traps": [
            "⚠️ TRAP 1: Do NOT confuse Berubari (1960) and Kesavananda Bharati (1973). Berubari said NOT part; Kesavananda declared IS part.",
            "⚠️ TRAP 2: Preamble CAN be amended under Article 368, provided Basic Structure is not destroyed (proven by 42nd Amendment 1976).",
            "⚠️ TRAP 3: Preamble is NON-JUSTICIABLE. You cannot approach Supreme Court solely for violation of Preamble.",
            "⚠️ TRAP 4: Preamble is NOT an independent source of power for Parliament or State Legislatures.",
            "⚠️ TRAP 5: The word 'Integrity' was added to Fraternity section ('Unity and Integrity of the Nation') in 1976.",
            "⚠️ TRAP 6: 42nd Amendment came into force on January 3, 1977 (enactment year 1976).",
            "⚠️ TRAP 7: Basic Structure Doctrine was introduced in Kesavananda Bharati case (April 24, 1973), NOT Berubari case.",
            "⚠️ TRAP 8: Preamble has been amended ONLY ONCE in history so far.",
            "⚠️ TRAP 9: Every single word in Preamble is NOT automatically a separate Basic Structure element; SC determines it case-by-case.",
            "⚠️ TRAP 10: Preamble acts as an Interpretive Aid only when constitutional provisions are ambiguous."
        ],
        "tables": [
            {
                "id": "tbl_preamble_vs_operative_provisions",
                "title_en": "Preamble vs Operative Constitutional Provisions",
                "title_ta": "முகவுரை vs செயல்படும் அரசியலமைப்பு விதிகள்",
                "headers_en": ["Feature", "Preamble", "Operative Provisions (Parts III, IV, V, etc.)"],
                "headers_ta": ["அம்சம்", "முகவுரை", "செயல்படும் விதிகள் (பகுதி III, IV, V போன்றவை)"],
                "rows_en": [
                    ["Nature", "Introductory preface expressing philosophy & vision", "Specific legal rules establishing governance structure"],
                    ["Justiciability", "Non-justiciable (cannot be enforced in court directly)", "Justiciable (FRs enforced via Art 32/226)"],
                    ["Source of Power", "NOT a source of power or restriction on legislature", "Grants specific legal powers and duty mandates"],
                    ["Role in Court", "Interpretive aid used when text is ambiguous", "Directly applied by courts to settle legal disputes"]
                ],
                "rows_ta": [
                    ["தன்மை", "தத்துவம் & தொலைநோக்கை வெளிப்படுத்தும் அறிமுக முன்னுரை", "ஆட்சி அமைப்பை நிறுவும் குறிப்பிட்ட சட்ட விதிகள்"],
                    ["நீதிமன்ற நிலைநிறுத்தம்", "நிலைநிறுத்த முடியாதது (நீதிமன்றத்தில் நேரடியாக அமல்படுத்த முடியாது)", "நிலைநிறுத்தக்கூடியது (அடிப்படை உரிமைகள் உறுப்பு 32/226 மூலம் அமல்)"],
                    ["அதிகார மூலம்", "சட்டமன்றத்திற்கு அதிகார மூலமோ அல்லது வரம்போ அல்ல", "குறிப்பிட்ட சட்ட அதிகாரங்கள் மற்றும் கடமைகளை வழங்குகிறது"],
                    ["நீதிமன்ற பங்கு", "உரை தெளிவற்றதாக இருக்கும்போது விளக்கமளிக்கும் உதவி", "சட்ட தகராறுகளைத் தீர்க்க நீதிமன்றங்களால் நேரடியாகப் பயன்படுத்தப்படுகிறது"]
                ]
            },
            {
                "id": "tbl_landmark_preamble_cases",
                "title_en": "High-Yield Landmark Preamble Case Table",
                "title_ta": "முகவுரை பற்றிய முக்கிய வரலாற்றுச் சிறப்புமிக்க வழக்குகள்",
                "headers_en": ["Case Name", "Year", "Supreme Court Holding", "TNPSC Takeaway"],
                "headers_ta": ["வழக்கின் பெயர்", "ஆண்டு", "உச்ச நீதிமன்றத் தீர்ப்பு", "டிஎன்பிஎஸ்சி குறிப்பு"],
                "rows_en": [
                    ["Berubari Union Case", "1960", "Preamble is NOT a part of the Constitution", "Historical 1960 view; later overruled"],
                    ["Kesavananda Bharati Case", "1973", "Overruled Berubari; Preamble IS a part of Constitution; Basic Structure born", "Landmark 13-judge bench decision"],
                    ["S.R. Bommai Case", "1994", "Secularism & Federalism in Preamble are Basic Structure", "Upheld Art 356 for anti-secular acts"],
                    ["LIC of India Case", "1995", "Preamble is an INTEGRAL PART of the Constitution", "Reaffirmed Kesavananda ruling"]
                ],
                "rows_ta": [
                    ["பெருபாரி யூனியன் வழக்கு", "1960", "முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல", "வரலாற்று 1960 பார்வை; பின்னர் ரத்து செய்யப்பட்டது"],
                    ["கேசவாநந்த பாரதி வழக்கு", "1973", "பெருபாரியை ரத்து செய்தது; முகவுரை பகுதி; அடிப்படை கட்டமைப்பு பிறந்தது", "வரலாற்று 13 நீதிபதிகள் அமர்வு தீர்ப்பு"],
                    ["எஸ்.ஆர். பொம்மை வழக்கு", "1994", "முகவுரையில் உள்ள மதச்சார்பின்மை & கூட்டாட்சி அடிப்படை அமைப்பாகும்", "மதச்சார்பற்ற எதிர்ப்பு நடவடிக்கைகளுக்கு உறுப்பு 356 உறுதிப்படுத்தப்பட்டது"],
                    ["எல்ஐசி வழக்கு", "1995", "முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதியாகும்", "கேசவாநந்தா தீர்ப்பு மீண்டும் உறுதிப்படுத்தப்பட்டது"]
                ]
            }
        ],
        "concept_map": [
            {
                "id": "mm_root",
                "parent_id": None,
                "title": "Preamble Status & Jurisprudence (முகவுரை அந்தஸ்து & வழக்கியல்)",
                "short_label": "Preamble Jurisprudence"
            },
            {
                "id": "mm_judicial_evolution",
                "parent_id": "mm_root",
                "title": "Judicial Evolution: Is Preamble Part of Constitution?",
                "short_label": "Judicial Evolution"
            },
            {
                "id": "mm_berubari",
                "parent_id": "mm_judicial_evolution",
                "title": "Berubari Union (1960): Preamble NOT part of Constitution",
                "short_label": "Berubari (1960): NOT Part"
            },
            {
                "id": "mm_kesavananda",
                "parent_id": "mm_judicial_evolution",
                "title": "Kesavananda Bharati (1973): OVERRULED Berubari; Preamble IS part + Basic Structure",
                "short_label": "Kesavananda (1973): IS Part"
            },
            {
                "id": "mm_lic",
                "parent_id": "mm_judicial_evolution",
                "title": "LIC of India (1995): Reaffirmed INTEGRAL PART of Constitution",
                "short_label": "LIC (1995): Integral Part"
            },
            {
                "id": "mm_amendability",
                "parent_id": "mm_root",
                "title": "Amendability & 42nd Amendment (1976)",
                "short_label": "Amendability"
            },
            {
                "id": "mm_art368",
                "parent_id": "mm_amendability",
                "title": "Art 368 Amendment: Permitted but bounded by Basic Structure Doctrine",
                "short_label": "Art 368 Bounded"
            },
            {
                "id": "mm_amendment_words",
                "parent_id": "mm_amendability",
                "title": "42nd Amendment 1976 Added: Socialist, Secular, Integrity",
                "short_label": "Socialist+Secular+Integrity"
            },
            {
                "id": "mm_legal_nature",
                "parent_id": "mm_root",
                "title": "Legal Nature: Non-Justiciable & Interpretive Guide",
                "short_label": "Legal Nature"
            },
            {
                "id": "mm_non_justiciable",
                "parent_id": "mm_legal_nature",
                "title": "Non-Justiciable: Cannot enforce Preamble directly in court",
                "short_label": "Non-Justiciable"
            },
            {
                "id": "mm_no_power_source",
                "parent_id": "mm_legal_nature",
                "title": "NOT Source of Substantive Power NOR Restriction on Legislature",
                "short_label": "NOT Power Source"
            }
        ],
        "revision_cards": [
            {
                "id": "RC_PRE2_001",
                "title": {
                    "en": "Judicial View: Is Preamble Part of Constitution?",
                    "ta": "நீதித்துறை பார்வை: முகவுரை அரசியலமைப்பின் பகுதியா?"
                },
                "front": {
                    "en": "Is the Preamble currently considered a part of the Indian Constitution?",
                    "ta": "முகவுரை தற்போது இந்திய அரசியலமைப்பின் ஒரு பகுதியாக கருதப்படுகிறதா?"
                },
                "back": {
                    "en": "YES. Kesavananda Bharati Case (1973) overruled Berubari Case (1960) and declared Preamble IS a part of the Constitution. Reaffirmed in LIC of India Case (1995).",
                    "ta": "ஆம். கேசவாநந்த பாரதி வழக்கு (1973) பெருபாரி வழக்கை (1960) ரத்து செய்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்று அறிவித்தது. எல்ஐசி வழக்கில் (1995) மீண்டும் உறுதிப்படுத்தப்பட்டது."
                },
                "one_line_revision": "Kesavananda Bharati (1973) = Preamble IS part of Constitution.",
                "type": "concept"
            },
            {
                "id": "RC_PRE2_002",
                "title": {
                    "en": "Berubari Union Case (1960)",
                    "ta": "பெருபாரி யூனியன் வழக்கு (1960)"
                },
                "front": {
                    "en": "What was the Supreme Court's ruling on Preamble in Berubari Union Case 1960?",
                    "ta": "பெருபாரி யூனியன் வழக்கு 1960 இல் முகவுரை பற்றிய உச்ச நீதிமன்றத் தீர்ப்பு என்ன?"
                },
                "back": {
                    "en": "SC held that Preamble is a key to framers' mind, but explicitly ruled it is NOT a part of the Constitution and NOT a source of substantive power. Overruled in 1973.",
                    "ta": "முகவுரை வரைவாளர்களின் மனதைத் திறக்கும் சாவி என்று கூறிய உச்ச நீதிமன்றம், ஆனால் அது அரசியலமைப்பின் பகுதி அல்ல மற்றும் அதிகார மூலம் அல்ல என்று வெளிப்படையாகத் தீர்ப்பளித்தது. 1973 இல் ரத்து செய்யப்பட்டது."
                },
                "one_line_revision": "Berubari (1960) = Historical view that Preamble is NOT part of Constitution.",
                "type": "fact"
            },
            {
                "id": "RC_PRE2_003",
                "title": {
                    "en": "Amendability under Article 368",
                    "ta": "உறுப்பு 368 இன் கீழ் திருத்தப்படும் தன்மை"
                },
                "front": {
                    "en": "Can the Preamble be amended under Article 368?",
                    "ta": "உறுப்பு 368 இன் கீழ் முகவுரையைத் திருத்த முடியுமா?"
                },
                "back": {
                    "en": "YES. Since Preamble is part of Constitution, it can be amended under Art 368, PROVIDED the Basic Structure features are not destroyed.",
                    "ta": "ஆம். முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்பதால், அடிப்படை கட்டமைப்பு அம்சங்கள் அழிக்கப்படாத வரையில் உறுப்பு 368 இன் கீழ் திருத்தப்படலாம்."
                },
                "one_line_revision": "Preamble CAN be amended under Art 368 (bounded by Basic Structure).",
                "type": "concept"
            },
            {
                "id": "RC_PRE2_004",
                "title": {
                    "en": "42nd Amendment Act 1976 Details",
                    "ta": "42வது திருத்தச் சட்டம் 1976 விவரங்கள்"
                },
                "front": {
                    "en": "How many times has the Preamble been amended, and what words were added?",
                    "ta": "முகவுரை எத்தனை முறை திருத்தப்பட்டுள்ளது, என்ன சொற்கள் சேர்க்கப்பட்டன?"
                },
                "back": {
                    "en": "Amended ONLY ONCE by 42nd Amendment Act 1976 (enforced Jan 3, 1977). Added 3 words: SOCIALIST, SECULAR, and INTEGRITY.",
                    "ta": "1976 இன் 42வது திருத்தச் சட்டத்தால் (ஜனவரி 3, 1977 இல் அமல்) ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டது. 3 சொற்கள் சேர்க்கப்பட்டன: சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு."
                },
                "one_line_revision": "Preamble amended ONLY ONCE (42nd Amend 1976: Socialist, Secular, Integrity).",
                "type": "fact"
            },
            {
                "id": "RC_PRE2_005",
                "title": {
                    "en": "Justiciability of Preamble",
                    "ta": "முகவுரையின் நீதிமன்ற நிலைநிறுத்தம்"
                },
                "front": {
                    "en": "Is the Preamble justiciable in courts of law?",
                    "ta": "முகவுரை நீதிமன்றங்களில் நிலைநிறுத்தக்கூடியதா?"
                },
                "back": {
                    "en": "NO. Preamble is NON-JUSTICIABLE and non-enforceable. It is NEITHER a source of legislative power NOR a restriction upon legislature.",
                    "ta": "இல்லை. முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது. இது சட்டமன்றத்தின் அதிகார மூலமும் அல்ல, சட்டமன்றத்தின் மீதான தடையும் அல்ல."
                },
                "one_line_revision": "Preamble = Non-justiciable & NOT an independent source of power.",
                "type": "trap"
            },
            {
                "id": "RC_PRE2_006",
                "title": {
                    "en": "Interpretive Role of Preamble",
                    "ta": "முகவுரையின் விளக்கமளிக்கும் பங்கு"
                },
                "front": {
                    "en": "What is the legal function of the Preamble in constitutional interpretation?",
                    "ta": "அரசியலமைப்பு விளக்கத்தில் முகவுரையின் சட்டப்பூர்வ பணி என்ன?"
                },
                "back": {
                    "en": "Acts as an Interpretive Aid. When an Article is ambiguous, courts use Preamble to determine framers' true intent and construct Basic Structure.",
                    "ta": "விளக்கமளிக்கும் உதவியாக செயல்படுகிறது. ஒரு சரத்து தெளிவற்றதாக இருக்கும்போது, வரைவாளர்களின் உண்மையான நோக்கத்தை தீர்மானிக்கவும் அடிப்படை அமைப்பை உருவாக்கவும் நீதிமன்றங்கள் முகவுரையைப் பயன்படுத்துகின்றன."
                },
                "one_line_revision": "Preamble = Interpretive Aid during ambiguity; key to framers' mind.",
                "type": "concept"
            }
        ]
    }
    return note

def build_notes_file():
    payload = generate_preamble_part2_payload()
    
    output_dir = r"c:\Users\Home\Desktop\tnpsc_ai\data\notes\polity"
    os.makedirs(output_dir, exist_ok=True)
    
    file_path1 = os.path.join(output_dir, "preamble_part_2.json")
    file_path2 = os.path.join(output_dir, "preamble_part2.json")

    with open(file_path1, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    with open(file_path2, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"SUCCESSFULLY SAVED PREAMBLE PART 2 NOTES AT:")
    print(f"  - {file_path1}")
    print(f"  - {file_path2}")

if __name__ == "__main__":
    build_notes_file()
