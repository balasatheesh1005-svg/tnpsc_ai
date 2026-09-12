# -*- coding: utf-8 -*-
"""
Builder script for Electoral Reforms Part 2: Reform Committees, Technological Innovations & Candidate Reforms.
Target: TNPSC Group 1 Standard.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def build_part2():
    part2_data = {
        "subject": "polity",
        "topic": "Electoral Reforms",
        "language": "English + Tamil",
        "ui_type": "standard_notes",
        "reading_time": "18 mins",
        "difficulty": "Medium",
        "completion_pct": 85,
        "metadata": {
            "topic_id": "electoral_reforms",
            "repository_id": "polity_electoral_reforms",
            "display_title": "Electoral Reforms – Part 2: Reform Committees, Technological Innovations & Candidate Reforms",
            "part": 2,
            "total_parts": 3,
            "subject": "polity",
            "chapter": "Electoral Reforms",
            "language": "English + Tamil",
            "schema_version": "2.0",
            "last_updated": "2026-09-05"
        },
        "meta": {
            "keywords": [
                "Electoral Reforms", "Tarkunde Committee", "Dinesh Goswami Committee", "Indrajit Gupta Committee",
                "Law Commission", "NCRWC", "EVM", "VVPAT", "NOTA", "Model Code of Conduct", "Criminalisation of Politics",
                "Lily Thomas Judgment", "Candidate Affidavit", "Paid News", "State Funding"
            ]
        },
        "keywords": [
            "Electoral Reforms", "Tarkunde Committee", "Dinesh Goswami Committee", "Indrajit Gupta Committee",
            "Law Commission", "NCRWC", "EVM", "VVPAT", "NOTA", "Model Code of Conduct", "Criminalisation of Politics",
            "Lily Thomas", "Candidate Disclosure", "Form 26", "State Funding", "cVIGIL"
        ],
        "learning_outcomes": {
            "Understand": {
                "en": [
                    "Master the landmark committees on electoral reforms and their high-yield recommendations.",
                    "Understand the technological architecture, legal basis, and security safeguards of EVMs and VVPATs.",
                    "Analyze the constitutional origin, scope, and enforcement mechanisms of the Model Code of Conduct (MCC).",
                    "Examine candidate disclosure mandates (Form 26), criminalisation disqualification framework under Section 8, and landmark SC verdicts."
                ],
                "ta": [
                    "தேர்தல் சீர்திருத்தங்கள் தொடர்பான வரலாற்று முக்கியத்துவம் வாய்ந்த குழுக்கள் மற்றும் அவற்றின் முக்கிய பரிந்துரைகளை அறிதல்.",
                    "EVM மற்றும் VVPAT-ன் தொழில்நுட்ப கட்டமைப்பு, சட்டப்பூர்வ அடிப்படை மற்றும் பாதுகாப்பு ஏற்பாடுகளைப் புரிந்துகொள்ளுதல்.",
                    "தேர்தல் நடத்தை விதிமுறைகளின் (MCC) அரசியலமைப்பு தோற்றம், வரம்பு மற்றும் அமலாக்க வழிமுறைகளை பகுப்பாய்வு செய்தல்.",
                    "படிவம் 26 பிரமாணப் பத்திரம், பிரிவு 8-ன் கீழ் குற்றவாளிகள் தகுதிநீக்கம் மற்றும் முக்கிய உச்ச நீதிமன்றத் தீர்ப்புகளை ஆராய்தல்."
                ]
            }
        },
        "sections": [
            {
                "id": "sec_reform_committees",
                "title_en": "1. Landmark Committees & Commissions on Electoral Reforms",
                "title_ta": "1. தேர்தல் சீர்திருத்தங்கள் குறித்த வரலாற்று முக்கியத்துவம் வாய்ந்த குழுக்கள் & ஆணையங்கள்",
                "type": "standard_topic"
            },
            {
                "id": "sec_evm_technology_safeguards",
                "title_en": "2. Electronic Voting Machines (EVM) — Evolution, Architecture & Safeguards",
                "title_ta": "2. மின்னணு வாக்குப்பதிவு இயந்திரங்கள் (EVM) — பரிணாமம், கட்டமைப்பு & பாதுகாப்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_vvpat_system",
                "title_en": "3. Voter Verifiable Paper Audit Trail (VVPAT) System",
                "title_ta": "3. வாக்காளர் சரிபார்க்கும் காகித தணிக்கைப் பதிவு (VVPAT) அமைப்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_nota_option",
                "title_en": "4. None of the Above (NOTA) — Legal Nature & Electoral Impact",
                "title_ta": "4. மேற்கண்ட எவருமில்லை (NOTA) — சட்ட வடிவம் & தேர்தல் தாக்கம்",
                "type": "standard_topic"
            },
            {
                "id": "sec_model_code_of_conduct",
                "title_en": "5. Model Code of Conduct (MCC) — Origin, Scope & Enforcement",
                "title_ta": "5. தேர்தல் நடத்தை நெறிமுறைகள் (MCC) — தோற்றம், வரம்பு & அமலாக்கம்",
                "type": "standard_topic"
            },
            {
                "id": "sec_candidate_disclosure_affidavits",
                "title_en": "6. Candidate Disclosure Mandates & Form 26 Affidavits",
                "title_ta": "6. வேட்பாளர் விவரங்களை வெளிப்படுத்துதல் & படிவம் 26 பிரமாணப் பத்திரங்கள்",
                "type": "standard_topic"
            },
            {
                "id": "sec_criminalisation_of_politics",
                "title_en": "7. Criminalisation of Politics & Disqualification Framework",
                "title_ta": "7. அரசியலில் குற்றமயமாதல் & தகுதிநீக்கச் சட்டக் கட்டமைப்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_money_power_and_expenditure",
                "title_en": "8. Money Power, Expenditure Limits & Monitoring Machinery",
                "title_ta": "8. பண பலம், தேர்தல் செலவு வரம்புகள் & கண்காணிப்பு அமைப்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_paid_news_phenomenon",
                "title_en": "9. Paid News Menace & Media Certification Monitoring Committees",
                "title_ta": "9. கட்டணச் செய்தி அச்சுறுத்தல் & ஊடக சான்றளிப்பு கண்காணிப்புக் குழுக்கள் (MCMC)",
                "type": "standard_topic"
            },
            {
                "id": "sec_state_funding_of_elections",
                "title_en": "10. State Funding of Elections — Concepts, Debates & Positions",
                "title_ta": "10. தேர்தல்களுக்கான அரசு நிதியுதவி — கோட்பாடுகள், விவாதங்கள் & தற்போதைய நிலை",
                "type": "standard_topic"
            },
            {
                "id": "sec_electoral_admin_technology",
                "title_en": "11. Modern Digital Electoral Administration & Citizen Portals",
                "title_ta": "11. நவீன டிஜிட்டல் தேர்தல் நிர்வாகம் & குடிமக்கள் செயலிகள் (cVIGIL, Suvidha)",
                "type": "standard_topic"
            }
        ],
        "content": {
            "definition": {
                "en": "Practical Electoral Reforms represent the concrete statutory amendments, judicial directives, technological applications, and administrative codes established to eliminate electoral malpractice, curb political criminalisation, enhance voter transparency, and modernize polling through secure electronic systems.",
                "ta": "நடைமுறை தேர்தல் சீர்திருத்தங்கள் என்பது தேர்தல் முறைகேடுகளை ஒழிக்கவும், அரசியலில் குற்றமயமாதலைக் கட்டுப்படுத்தவும், வாக்காளர் வெளிப்படைத்தன்மையை அதிகரிக்கவும், பாதுகாப்பான மின்னணு அமைப்புகள் மூலம் வாக்குப்பதிவை நவீனமயமாக்கவும் நிறுவப்பட்ட சட்டப்பூர்வ திருத்தங்கள், நீதித்துறை உத்தரவுகள், தொழில்நுட்பப் பயன்பாடுகள் மற்றும் நிர்வாக நெறிமுறைகளைக் குறிக்கிறது."
            },
            "introduction": {
                "en": "While the Constitution provided the sovereign framework, the operational integrity of Indian elections faced grave crises in the 1970s and 1980s due to booth capturing, muscle power, and illicit cash. Beginning with the Tarkunde Committee in 1974 and Dinesh Goswami Committee in 1990, a succession of expert bodies recommended profound institutional changes. Concurrently, technological breakthroughs such as the EVM and VVPAT revolutionized polling integrity, while historic Supreme Court rulings transformed the Model Code of Conduct and mandated transparency of candidate criminal and financial antecedents.",
                "ta": "அரசியலமைப்பு ஒரு இறையாண்மைமிக்க கட்டமைப்பை வழங்கிய போதிலும், 1970கள் மற்றும் 1980களில் வாக்குச்சாவடி கைப்பற்றுதல், தசை பலம் மற்றும் சட்டவிரோத பணத்தால் இந்தியத் தேர்தல்களின் செயல்பாட்டு ஒருமைப்பாடு கடுமையான நெருக்கடிகளை எதிர்கொண்டது. 1974-ல் தார்குண்டே குழு மற்றும் 1990-ல் தினேஷ் கோஸ்வாமி குழுவில் தொடங்கி பல நிபுணர் குழுக்கள் ஆழமான நிறுவன மாற்றங்களைப் பரிந்துரைத்தன. அதே நேரத்தில், EVM மற்றும் VVPAT போன்ற தொழில்நுட்ப கண்டுபிடிப்புகள் வாக்குப்பதிவை மாற்றியமைத்தன; வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்றத் தீர்ப்புகள் நடத்தை விதிகளுக்கு வலுவூட்டி, வேட்பாளர்களின் குற்ற மற்றும் நிதிப் பின்னணியை வெளிப்படுத்துவதைக் கட்டாயமாக்கின."
            },
            "sec_reform_committees": [
                {
                    "title_en": "Tarkunde Committee (1974–75) & Dinesh Goswami Committee (1990)",
                    "title_ta": "தார்குண்டே குழு (1974–75) & தினேஷ் கோஸ்வாமி குழு (1990)",
                    "points": {
                        "en": [
                            "Tarkunde Committee (1974–75): Appointed by Jayaprakash Narayan under Citizens for Democracy. Major recommendations: 1. Multi-member Election Commission; 2. Lowering voting age from 21 to 18; 3. Statutory recognition of Model Code of Conduct; 4. Use of radio/TV airtime for recognized political parties.",
                            "Dinesh Goswami Committee on Electoral Reforms (1990): Landmark government-appointed committee. Key recommendations: 1. Rapid introduction of EVMs to combat booth capturing; 2. State assistance in-kind (fuel, paper, electoral rolls) to candidates of recognized parties; 3. Ban on independent candidates from acquiring common symbols; 4. Re-examination of anti-defection disqualification to restrict it only to voting against party whip on confidence motions; 5. Fresh delimitation based on 1981 Census."
                        ],
                        "ta": [
                            "தார்குண்டே குழு (1974–75): ஜெயபிரகாஷ் நாராயணனால் 'மக்களாட்சிக்கான குடிமக்கள்' அமைப்பின் கீழ் அமைக்கப்பட்டது. முக்கிய பரிந்துரைகள்: 1. பல உறுப்பினர் தேர்தல் ஆணையம்; 2. வாக்களிக்கும் வயதை 21-லிருந்து 18 ஆகக் குறைத்தல்; 3. தேர்தல் நடத்தை விதிமுறைகளுக்கு சட்டப்பூர்வ அங்கீகாரம்; 4. அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு அரசு வானொலி/தொலைக்காட்சி ஒளிபரப்பு நேரம் ஒதுக்கீடு.",
                            "தினேஷ் கோஸ்வாமி தேர்தல் சீர்திருத்தக் குழு (1990): மிக முக்கியமான அரசு குழு. முக்கிய பரிந்துரைகள்: 1. வாக்குச்சாவடி கைப்பற்றுதலைத் தடுக்க EVM-களை விரைவாக அறிமுகப்படுத்துதல்; 2. அங்கீகரிக்கப்பட்ட கட்சி வேட்பாளர்களுக்கு பொருள் வடிவிலான அரசு நிதியுதவி (எரிபொருள், காகிதம், வாக்காளர் பட்டியல்); 3. சுயேச்சை வேட்பாளர்கள் பொதுச் சின்னங்களை பெறுவதைத் தடை செய்தல்; 4. கட்சித்தாவல் தடைச் சட்டத்தை நம்பிக்கை வாக்கெடுப்புகளில் கொறடாவுக்கு எதிராக வாக்களிப்பதற்கு மட்டுமே கட்டுப்படுத்துதல்; 5. 1981 மக்கள் தொகை கணக்கெடுப்பின்படி புதிய மறுவரைவு செய்தல்."
                        ]
                    }
                },
                {
                    "title_en": "Indrajit Gupta Committee (1998) & Law Commission Reports",
                    "title_ta": "இந்திரஜித் குப்தா குழு (1998) & சட்ட ஆணைய அறிக்கைகள்",
                    "points": {
                        "en": [
                            "Vohra Committee Report (1993): Chaired by former Home Secretary N.N. Vohra. Documented the dangerous nexus between mafia syndicates, corrupt bureaucrats, and politicians, urging systemic overhaul.",
                            "Indrajit Gupta Committee on State Funding of Elections (1998): 8-member parliamentary committee. Key recommendations: 1. State funding of elections is fully justified to establish fair competition; 2. State funding MUST be given ONLY IN-KIND (microphones, paper, petrol, voter slips), NEVER in cash; 3. State funding should be restricted to recognized national and state parties with past electoral performance; 4. Political parties must mandatorily submit audited annual accounts to ECI.",
                            "Law Commission 170th Report on Electoral Laws (1999, Justice B.P. Jeevan Reddy): Recommended: 1. Introduction of hybrid electoral system (combining First-Past-The-Post with 25% Proportional Representation List System); 2. Enactment of law to regulate internal party democracy; 3. Debarring candidates with criminal charges.",
                            "NCRWC (2000–2002, Justice M.N. Venkatachaliah): Recommended that persons charged with heinous offences carrying 5+ years imprisonment by a competent court should be debarred from contesting; appointment of CEC and ECs by a high-level committee.",
                            "Law Commission 255th Report on Electoral Reforms (2015, Justice A.P. Shah): Comprehensive proposals on political party regulation, capping cash donations to ₹2,000, regulating paid news, criminalising opinion poll leaks during silence period, and strengthening NOTA."
                        ],
                        "ta": [
                            "வோஹ்ரா குழு அறிக்கை (1993): முன்னாள் உள்துறை செயலாளர் என்.என். வோஹ்ரா தலைமையில் அமைக்கப்பட்டது. மாபியா குழுக்கள், ஊழல் அதிகாரிகள் மற்றும் அரசியல்வாதிகளுக்கு இடையிலான ஆபத்தான பிணைப்பை ஆவணப்படுத்தி அமைப்புசார் மாற்றத்தை வலியுறுத்தியது.",
                            "இந்திரஜித் குப்தா குழு (1998 - தேர்தல் அரசு நிதியுதவி): 1. சமமான போட்டியை உருவாக்க தேர்தல்களுக்கு அரசு நிதியுதவி செய்வது முற்றிலும் நியாயமானது; 2. அரசு நிதியுதவி பொருள் வடிவில் மட்டுமே (மைக்ரோஃபோன்கள், காகிதம், பெட்ரோல், வாக்காளர் சீட்டுகள்) வழங்கப்பட வேண்டும், ரொக்கமாக வழங்கவே கூடாது; 3. கடந்த கால தேர்தல் செயல்பாட்டைக் கொண்ட அங்கீகரிக்கப்பட்ட தேசிய மற்றும் மாநிலக் கட்சிகளுக்கு மட்டுமே இது வழங்கப்பட வேண்டும்; 4. அரசியல் கட்சிகள் தணிக்கை செய்யப்பட்ட வருடாந்திர கணக்குகளை ECI-யிடம் கட்டாயம் சமர்ப்பிக்க வேண்டும்.",
                            "சட்ட ஆணையத்தின் 170வது அறிக்கை (1999, நீதிபதி பி.பி. ஜீவன் ரெட்டி): கலப்பு தேர்தல் முறையை அறிமுகப்படுத்துதல் (First-Past-The-Post உடன் 25% விகிதாச்சார பட்டியல் முறை); கட்சிக்குள் உட்கட்சி ஜனநாயகத்தை ஒழுங்குபடுத்த சட்டம் இயற்றுதல்.",
                            "NCRWC (2000–2002, நீதிபதி எம்.என். வெங்கடாசலையா): 5 ஆண்டுகள் அல்லது அதற்கு மேற்பட்ட சிறைத் தண்டனைக்குரிய கொடூரக் குற்றங்களுக்காக நீதிமன்றத்தால் குற்றச்சாட்டுகள் பதிவு செய்யப்பட்ட நபர்கள் தேர்தலில் போட்டியிடத் தடை விதிக்க வேண்டும்; உயர்மட்டக் குழு மூலம் CEC நியமனம்.",
                            "சட்ட ஆணையத்தின் 255வது அறிக்கை (2015, நீதிபதி ஏ.பி. ஷா): அரசியல் கட்சி நிதி ஒழுங்குமுறை, ரொக்க நன்கொடைகளை ₹2,000 ஆகக் குறைத்தல், கட்டணச் செய்தியை ஒழுங்குபடுத்துதல் மற்றும் நோட்டாவை வலுப்படுத்துதல்."
                        ]
                    }
                }
            ],
            "sec_evm_technology_safeguards": [
                {
                    "title_en": "EVM Evolution, Legal Mandate & Technical Architecture",
                    "title_ta": "EVM பரிணாமம், சட்டப்பூர்வ ஆணை & தொழில்நுட்ப கட்டமைப்பு",
                    "points": {
                        "en": [
                            "Evolution: Invented by MB Hanifa in 1980; prototyped by ECI in collaboration with Bharat Electronics Limited (BEL, Bangalore) and Electronics Corporation of India Limited (ECIL, Hyderabad).",
                            "First Pilot Usage: Used for the first time in 50 polling stations of Paravur Assembly Constituency in Kerala in May 1982.",
                            "Legal Void & Supreme Court Ruling (1984): In A.C. Jose v. Sivan Pillai, SC set aside the election because RPA 1951 did not contain provisions authorizing voting machines.",
                            "Statutory Legal Basis (1988): Parliament inserted Section 61A into RPA 1951 in December 1988, empowering ECI to use Electronic Voting Machines.",
                            "Full Deployment: First used in all 543 Lok Sabha constituencies in the 2004 General Elections; used continuously in all general and state assembly elections ever since.",
                            "Technical Architecture: Standalone, non-networked battery-powered device. Consists of TWO interconnected units: 1. Control Unit (CU) kept with Presiding Officer; 2. Balloting Unit (BU) kept in voting compartment.",
                            "Tamper-Proof Hardware: Uses one-time programmable (OTP) micro-controller chips burned at manufacturing stage; NO operating system, NO internet, NO Wi-Fi, NO Bluetooth, NO wireless frequency reception capability."
                        ],
                        "ta": [
                            "பரிணாமம்: 1980-ல் எம்.பி. ஹனிபாவால் வடிவமைக்கப்பட்டது; ECI வழிகாட்டுதலில் பாரத் எலக்ட்ரானிக்ஸ் (BEL) மற்றும் எலக்ட்ரானிக்ஸ் கார்ப்பரேஷன் ஆஃப் இந்தியா (ECIL) இணைந்து உருவாக்கின.",
                            "முதல் சோதனைப் பயன்பாடு: 1982 மே மாதம் கேரளாவின் பரவூர் சட்டமன்றத் தொகுதியில் உள்ள 50 வாக்குச்சாவடிகளில் முதன்முறையாகப் பயன்படுத்தப்பட்டது.",
                            "நீதிமன்றத் தீர்ப்பு (1984): ஏ.சி. ஜோஸ் v. சிவன் பிள்ளை வழக்கில், RPA 1951 சட்டத்தில் இயந்திரங்களுக்கு அனுமதி இல்லாததால் தேர்தல் முடிவை உச்ச நீதிமன்றம் ரத்து செய்தது.",
                            "சட்டப்பூர்வ அங்கீகாரம் (1988): நாடாளுமன்றம் 1988 டிசம்பரில் RPA 1951-ல் பிரிவு 61A-ஐச் சேர்த்து, EVM-களைப் பயன்படுத்த ECI-க்கு முழு சட்ட அதிகாரம் அளித்தது.",
                            "முழுமையான பயன்பாடு: 2004 பொதுத்தேர்தலில் 543 மக்களவைத் தொகுதிகளிலும் முதன்முதலாக நாடு முழுவதும் முழுமையாகப் பயன்படுத்தப்பட்டது.",
                            "தொழில்நுட்ப கட்டமைப்பு: இணையம் அல்லது நெட்வொர்க் தொடர்பில்லாத, பேட்டரியால் இயங்கும் தனித்த சாதனம். இரண்டு இணைக்கப்பட்ட அலகுகள்: 1. கட்டுப்பாட்டு அலகு (CU - வாக்குச்சாவடி அலுவலரிடம் இருக்கும்); 2. வாக்குப்பதிவு அலகு (BU - ரகசிய வாக்குப்பதிவு அறையில் இருக்கும்).",
                            "பாதுகாப்பு வன்பொருள்: உற்பத்தி நிலையிலேயே ஒருமுறை மட்டுமே புரோகிராம் செய்யப்படும் (OTP) சிப்; இயங்குதளம் (OS) கிடையாது; இன்டர்நெட், வைஃபை, புளூடூத் போன்ற எவ்வித வெளிப்புற தகவல் தொடர்பு சாதனமும் கிடையாது."
                        ]
                    }
                },
                {
                    "title_en": "Multi-Layered Security Safeguards of EVMs",
                    "title_ta": "EVM-களின் பல அடுக்கு பாதுகாப்பு ஏற்பாடுகள்",
                    "points": {
                        "en": [
                            "1. First Level Checking (FLC): Conducted by authorized engineers in presence of recognized political party representatives several weeks prior to poll.",
                            "2. Two-Stage Randomization: Stage 1 randomizes EVMs to allocate them to assembly constituencies; Stage 2 randomizes them to specific polling stations, making it mathematically impossible to know in advance which machine goes where.",
                            "3. Mock Poll: Mandatorily conducted on poll day before actual voting begins in the presence of candidate polling agents; minimum 50 votes cast and tallied.",
                            "4. Physical Seals: Control Unit secured with Green Paper Seal, Special Tag, Outer Strip Seal, and signature of candidate polling agents.",
                            "5. Post-Poll Strong Rooms: Guarded by Central Armed Police Forces (CAPF) under double-lock system with 24/7 CCTV surveillance."
                        ],
                        "ta": [
                            "1. முதல் நிலை சரிபார்ப்பு (FLC): தேர்தலுக்கு பல வாரங்களுக்கு முன்பே அங்கீகரிக்கப்பட்ட கட்சி பிரதிநிதிகள் முன்னிலையில் பொறியாளர்களால் சரிபார்க்கப்படுகிறது.",
                            "2. இரண்டு அடுக்கு சீரற்ற ஒதுக்கீடு (Randomization): எந்த இயந்திரம் எந்த தொகுதிக்கு மற்றும் எந்த வாக்குச்சாவடிக்கு செல்லும் என்பதை முன்கூட்டியே அறிய முடியாத வகையில் கணினி மூலம் குலுக்கல் முறையில் ஒதுக்கப்படுகிறது.",
                            "3. மாதிரி வாக்குப்பதிவு (Mock Poll): தேர்தல் தொடங்குவதற்கு முன் வேட்பாளர்களின் முகவர்கள் முன்னிலையில் குறைந்தபட்சம் 50 மாதிரி வாக்குகள் பதிவு செய்யப்பட்டு சரிபார்க்கப்படுகிறது.",
                            "4. இயற்பியல் முத்திரைகள்: கட்டுப்பாட்டு அலகு பச்சை காகித முத்திரை, சிறப்பு டேக், ஸ்ட்ரிப் முத்திரை மற்றும் முகவர்களின் கையொப்பங்களுடன் சீல் வைக்கப்படுகிறது.",
                            "5. வாக்குப்பதிவுக்குப் பிந்தைய காப்பறை (Strong Room): மத்திய துணை ராணுவப் படையினரின் (CAPF) 24 மணி நேர சிசிடிவி கண்காணிப்புடன் கூடிய இரட்டைப் பூட்டு அமைப்பில் பாதுகாக்கப்படுகிறது."
                        ]
                    }
                }
            ],
            "sec_vvpat_system": [
                {
                    "title_en": "VVPAT — Concept, Legal Mandate & Counting Rules",
                    "title_ta": "VVPAT — கருத்து, சட்டப்பூர்வ ஆணை & வாக்கு எண்ணிக்கை விதிகள்",
                    "points": {
                        "en": [
                            "Meaning: Voter Verifiable Paper Audit Trail is an independent verification printer attached to the EVM Balloting Unit and Control Unit.",
                            "Functioning: When a voter presses a button on BU, VVPAT prints a paper slip displaying the candidate's serial number, name, and election symbol. The slip is visible to the voter behind a transparent glass window for 7 SECONDS before automatically cutting and falling into a sealed drop box.",
                            "Statutory Recognition: Conduct of Elections (Amendment) Rules, 2013 inserted Rules 49A and 49M.",
                            "Pilot Launch: Tested first in Noksen Assembly constituency of Nagaland in September 2013.",
                            "Subramanian Swamy v. ECI (2013): Landmark Supreme Court verdict declaring that 'paper trail is an indispensable requirement of free and fair elections' and directed government to provide financial support for nationwide rollout.",
                            "100% Rollout: Deployed in all polling stations across India in the 2019 Lok Sabha elections.",
                            "Mandatory VVPAT Verification Rule: In April 2019, Supreme Court directed ECI to mandatorily tally VVPAT paper slips of 5 randomly selected polling stations per assembly constituency/segment.",
                            "ADR v. ECI (April 2024): Supreme Court firmly rejected prayers for 100% VVPAT slip verification or reverting to paper ballots, upholding EVM sanctity while permitting candidate-funded 5% micro-controller verification."
                        ],
                        "ta": [
                            "பொருள்: வாக்காளர் சரிபார்க்கும் காகித தணிக்கைப் பதிவு (VVPAT) என்பது EVM-ன் வாக்குப்பதிவு மற்றும் கட்டுப்பாட்டு அலகுகளுடன் இணைக்கப்பட்ட ஒரு சுதந்திரமான அச்சுப்பொறியாகும்.",
                            "செயல்பாடு: வாக்காளர் பொத்தானை அழுத்தியவுடன், வேட்பாளரின் வரிசை எண், பெயர் மற்றும் சின்னம் அச்சிடப்பட்ட காகிதச் சீட்டு கண்ணாடி சாளரத்தின் பின்னால் 7 வினாடிகள் தெரியும், பின்னர் தானாகவே வெட்டப்பட்டு சீலிடப்பட்ட பெட்டிக்குள் விழும்.",
                            "சட்டப்பூர்வ அங்கீகாரம்: தேர்தல் நடத்தை விதிகள் 2013-ல் விதிகள் 49A மற்றும் 49M சேர்க்கப்பட்டன.",
                            "முதல் அறிமுகம்: 2013 செப்டம்பரில் நாகாலாந்தின் நோக்சென் சட்டமன்றத் தொகுதியில் முதன்முதலாக சோதிக்கப்பட்டது.",
                            "சுப்பிரமணியன் சுவாமி v. தேர்தல் ஆணையம் (2013): 'காகிதத் தணிக்கை என்பது சுதந்திரமான மற்றும் நியாயமான தேர்தல்களுக்கு இன்றியமையாத தேவையாகும்' என்று உச்ச நீதிமன்றம் தீர்ப்பளித்து, நாடு முழுவதும் VVPAT-ஐ அமல்படுத்த உத்தரவிட்டது.",
                            "100% பயன்பாடு: 2019 மக்களவைத் தேர்தலில் இந்தியாவின் அனைத்து வாக்குச்சாவடிகளிலும் முழுமையாகப் பயன்படுத்தப்பட்டது.",
                            "கட்டாய சரிபார்ப்பு விதி: ஒவ்வொரு சட்டமன்றத் தொகுதிக்கும் குலுக்கல் முறையில் தேர்ந்தெடுக்கப்படும் 5 வாக்குச்சாவடிகளில் VVPAT சீட்டுகளை முழுமையாக எண்ணி சரிபார்க்க வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது (2019).",
                            "ADR v. ECI (ஏப்ரல் 2024): 100% VVPAT சீட்டுகளை எண்ண வேண்டும் என்ற கோரிக்கையை உச்ச நீதிமன்றம் நிராகரித்து, EVM இயந்திரங்களின் பாதுகாப்பை உறுதி செய்தது."
                        ]
                    }
                }
            ],
            "sec_nota_option": [
                {
                    "title_en": "None of the Above (NOTA) — Constitutional Basis & Legal Effect",
                    "title_ta": "நோட்டா (NOTA) — அரசியலமைப்பு அடிப்படை & சட்டப்பூர்வ விளைவு",
                    "points": {
                        "en": [
                            "Meaning: NOTA allows a voter to formally exercise negative voting to reject all contesting candidates secretly.",
                            "Supreme Court Mandate (PUCL v. Union of India, Sept 2013): SC held that under Article 19(1)(a), the fundamental right to freedom of speech and expression includes the right of a voter to say 'none of the above' secretly without fear of victimization.",
                            "Symbol: Standard NOTA symbol designed by National Institute of Design (NID, Ahmedabad) approved by ECI in 2015.",
                            "CRITICAL TNPSC TRAP (Legal Effect): In Indian parliamentary and assembly elections, NOTA has NO ELECTORAL VETO POWER. Even if NOTA secures 99% of total votes in a constituency, the candidate who secures the highest number of valid non-NOTA votes is legally declared elected!",
                            "State SEC Exceptions: State Election Commissions of Haryana, Maharashtra, and Delhi for local municipal elections have recognized NOTA as a 'fictional candidate' (if NOTA gets highest votes, re-poll ordered); this rule does NOT apply to Parliament or Assemblies."
                        ],
                        "ta": [
                            "பொருள்: போட்டியிடும் அனைத்து வேட்பாளர்களையும் நிராகரிக்கும் உரிமையை ரகசியமாகப் பதிவு செய்ய வாக்காளருக்கு நோட்டா உதவுகிறது.",
                            "உச்ச நீதிமன்றத் தீர்ப்பு (PUCL v. இந்திய அரசு, செப் 2013): உறுப்பு 19(1)(a)-ன் கீழ் பேச்சு மற்றும் கருத்துச் சுதந்திரத்தில் ஒரு வாக்காளர் அனைத்து வேட்பாளர்களையும் நிராகரிக்கும் உரிமையும் அடங்கும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
                            "சின்னம்: தேசிய வடிவமைப்பு நிறுவனத்தால் (NID அகமதாபாத்) வடிவமைக்கப்பட்ட நோட்டா சின்னத்தை ECI 2015-ல் அங்கீகரித்தது.",
                            "முக்கிய TNPSC பொறி (சட்டப்பூர்வ விளைவு): நாடாளுமன்ற மற்றும் சட்டமன்றத் தேர்தல்களில் நோட்டாவுக்கு எந்தவொரு ரத்து அதிகாரமும் (Veto Power) இல்லை. ஒரு தொகுதியில் நோட்டா 99% வாக்குகளைப் பெற்றாலும், போட்டியிடும் வேட்பாளர்களில் அதிக வாக்கு பெற்றவரே வெற்றி பெற்றவராக அறிவிக்கப்படுவார்!",
                            "உள்ளாட்சி விதிவிலக்குகள்: ஹரியானா மற்றும் மகாராஷ்டிரா போன்ற சில மாநிலங்களில் உள்ளாட்சித் தேர்தல்களுக்கு மட்டும் நோட்டா அதிக வாக்குகள் பெற்றால் மறுதேர்தல் நடத்தப்படும் விதி உள்ளது; ஆனால் இது நாடாளுமன்ற/சட்டமன்றத் தேர்தல்களுக்குப் பொருந்தாது."
                        ]
                    }
                }
            ],
            "sec_model_code_of_conduct": [
                {
                    "title_en": "Model Code of Conduct (MCC) — Origin, Scope & Nature",
                    "title_ta": "தேர்தல் நடத்தை நெறிமுறைகள் (MCC) — தோற்றம், வரம்பு & தன்மை",
                    "points": {
                        "en": [
                            "Origin: First introduced in Kerala State Legislative Assembly elections in 1960 as a voluntary consensus among political parties; adopted nationally by ECI in 1968 and consolidated in 1979.",
                            "Legal Status (Crucial TNPSC Concept): The MCC is NON-STATUTORY. It is NOT an Act of Parliament. It evolved out of political consensus and moral commitment.",
                            "Enforceability: Enforced by ECI using its inherent constitutional powers under Article 324, backed by parallel penal provisions in the Indian Penal Code (IPC) and Representation of the People Act, 1951.",
                            "Operational Period: Comes into force with IMMEDIATE EFFECT from the date and hour the ECI announces the election schedule in its press conference, and remains in force until the completion of the election process (declaration of results).",
                            "Applicability: Binds political parties, contesting candidates, ministers, and the ruling government across the state/country."
                        ],
                        "ta": [
                            "தோற்றம்: 1960-ல் கேரள சட்டமன்றத் தேர்தலில் அரசியல் கட்சிகளுக்கு இடையேயான ஒருமித்த கருத்தின் அடிப்படையில் முதன்முதலில் அறிமுகப்படுத்தப்பட்டது; 1968 மற்றும் 1979-ல் தேசிய அளவில் ஏற்றுக்கொள்ளப்பட்டது.",
                            "சட்ட அந்தஸ்து (முக்கிய TNPSC கருத்து): MCC என்பது சட்டப்பூர்வமானது அல்ல (Non-Statutory). இது நாடாளுமன்றத்தால் இயற்றப்பட்ட சட்டம் அல்ல; அரசியல் கட்சிகளின் நெறிமுறை மற்றும் தார்மீக உறுதிப்பாடாகும்.",
                            "அமலாக்கம்: உறுப்பு 324-ன் கீழ் ECI தனது அரசியலமைப்பு அதிகாரத்தைப் பயன்படுத்தி இதை செயல்படுத்துகிறது; மேலும் IPC மற்றும் RPA 1951 சட்டப் பிரிவுகள் மூலம் தண்டனை நடவடிக்கைகள் எடுக்கப்படுகின்றன.",
                            "செயல்படும் காலம்: ECI பத்திரிகையாளர் சந்திப்பில் தேர்தல் தேதிகளை அறிவிக்கும் நாள் மற்றும் வினாடி முதலே உடனடியாக அமலுக்கு வருகிறது; தேர்தல் முடிவுகள் வெளியாகும் வரை நடைமுறையில் இருக்கும்.",
                            "பொருந்துதல்: அனைத்து அரசியல் கட்சிகள், வேட்பாளர்கள், அமைச்சர்கள் மற்றும் ஆளும் அரசாங்கத்திற்கு முழுமையாகப் பொருந்தும்."
                        ]
                    }
                },
                {
                    "title_en": "Major Prohibitions & Guidelines under MCC",
                    "title_ta": "MCC-ன் கீழ் விதிக்கப்படும் முக்கியத் தடைகள் & வழிகாட்டுதல்கள்",
                    "points": {
                        "en": [
                            "1. General Conduct: No party or candidate shall engage in any activity that aggravates existing differences, creates mutual hatred, or causes communal tension; no appeals to caste, communal, or religious feelings.",
                            "2. Places of Worship: Temples, mosques, churches, or other places of worship shall NOT be used as forums for election campaigning.",
                            "3. Ruling Party Restrictions: Ministers shall not combine official visits with electioneering; government aircraft, vehicles, and machinery shall not be used for party campaign; no financial grants, new schemes, or foundation stones announced after poll notification.",
                            "4. Election Manifestos: Chapter VIII added in 2014 following S. Subramaniam Balaji v. Govt of Tamil Nadu (2013): Manifestos must not contain promises that vitiate poll purity, and parties must explain the financial rationale for freebie commitments.",
                            "5. Silence Period: Campaigning must end 48 hours prior to the close of poll (Section 126 of RPA 1951)."
                        ],
                        "ta": [
                            "1. பொது நடத்தை: சாதி, மத, மொழி மோதல்களைத் தூண்டும் நடவடிக்கைகளில் ஈடுபடக்கூடாது; சாதி அல்லது மத உணர்வுகளைத் தூண்டி வாக்கு கேட்கக் கூடாது.",
                            "2. வழிபாட்டுத் தலங்கள்: கோவில்கள், மசூதிகள், தேவாலயங்கள் போன்ற வழிபாட்டுத் தலங்களை தேர்தல் பிரச்சார மேடைகளாகப் பயன்படுத்தக் கூடாது.",
                            "3. ஆளும் கட்சிக்கான கட்டுப்பாடுகள்: அமைச்சர்கள் அரசு பயணங்களுடன் தேர்தல் பிரச்சாரத்தை இணைக்கக் கூடாது; அரசு வாகனங்கள் மற்றும் விமானங்களைப் பிரச்சாரத்திற்குப் பயன்படுத்தக் கூடாது; புதிய அரசுத் திட்டங்களையோ அல்லது அடிக்கற்களையோ நாட்டக் கூடாது.",
                            "4. தேர்தல் அறிக்கைகள்: எஸ். சுப்பிரமணியம் பாலாஜி v. தமிழ்நாடு அரசு (2013) வழக்கைத் தொடர்ந்து அத்தியாயம் VIII சேர்க்கப்பட்டது: இலவச வாக்குறுதிகளுக்கான நிதி ஆதாரங்களை தேர்தல் அறிக்கையில் தெளிவாக விளக்க வேண்டும்.",
                            "5. அமைதிக் காலம்: வாக்குப்பதிவு முடிவடையும் நேரத்திற்கு 48 மணி நேரத்திற்கு முன்பாக அனைத்து வகையான பொதுப் பிரச்சாரங்களும் நிறுத்தப்பட வேண்டும்."
                        ]
                    }
                }
            ],
            "sec_candidate_disclosure_affidavits": [
                {
                    "title_en": "Candidate Disclosure Mandates & Form 26 Affidavits",
                    "title_ta": "வேட்பாளர் விவரங்களை வெளிப்படுத்துதல் & படிவம் 26 பிரமாணப் பத்திரங்கள்",
                    "points": {
                        "en": [
                            "Landmark Origin: ADR v. Union of India (2002) and PUCL v. Union of India (2003) — Supreme Court established that voters have a Fundamental Right to Information under Article 19(1)(a) regarding the background of contesting candidates.",
                            "Form 26 Affidavit: Candidates must mandatorily file a sworn affidavit disclosing: 1. Criminal antecedents (cases framed, convictions); 2. Assets & liabilities of self, spouse, and all dependents (movable & immovable); 3. Educational qualifications.",
                            "Lok Prahari v. UOI (2018): Supreme Court mandated that candidates must also disclose the SOURCES OF INCOME of themselves, spouses, and dependents to expose disproportionate asset growth.",
                            "Consequences of False Affidavit: Under Section 125A of RPA 1951, filing a false affidavit or concealing information is punishable with imprisonment up to 6 months, or fine, or both.",
                            "Kishan Shankar Kathore (2014): SC held that non-disclosure of material financial or criminal information constitutes a 'corrupt practice' and is grounds for setting aside the election."
                        ],
                        "ta": [
                            "வரலாற்றுப் பின்னணி: ADR v. இந்திய அரசு (2002) மற்றும் PUCL v. இந்திய அரசு (2003) வழக்குகளில், உறுப்பு 19(1)(a)-ன் கீழ் போட்டியிடும் வேட்பாளர்களின் பின்னணியை அறியும் அடிப்படை தகவல் உரிமை வாக்காளருக்கு உண்டு என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
                            "படிவம் 26 பிரமாணப் பத்திரம்: வேட்பாளர்கள் கட்டாயமாக தாக்கல் செய்ய வேண்டிய விவரங்கள்: 1. குற்றப் பின்னணி (பதிவு செய்யப்பட்ட வழக்குகள் மற்றும் தண்டனைகள்); 2. வேட்பாளர், மனைவி மற்றும் சார்ந்திருப்பவர்களின் அசையும், அசையா சொத்துக்கள் மற்றும் கடன்கள்; 3. கல்வித் தகுதி.",
                            "லோக் பிரஹாரி வழக்கு (2018): வருமானத்திற்கு அதிகமாக சொத்து சேர்ப்பதைத் தடுக்க, வேட்பாளர் மற்றும் குடும்பத்தினரின் வருமான ஆதாரங்களையும் வெளிப்படுத்துவது கட்டாயம் என உச்ச நீதிமன்றம் உத்தரவிட்டது.",
                            "தவறான தகவலின் விளைவு: RPA 1951 பிரிவு 125A-ன் கீழ் தவறான பிரமாணப் பத்திரம் தாக்கல் செய்வது அல்லது தகவல்களை மறைப்பது 6 மாதங்கள் வரை சிறைத் தண்டனை அல்லது அபராதம் விதிக்கத்தக்க குற்றமாகும்.",
                            "கிஷன் சங்கர் வழக்கு (2014): சொத்து அல்லது குற்றத் தகவல்களை மறைப்பது ஊழல் நடைமுறையாகக் கருதப்பட்டு, தேர்தல் செல்லாது என அறிவிக்கப்படலாம்."
                        ]
                    }
                }
            ],
            "sec_criminalisation_of_politics": [
                {
                    "title_en": "Statutory Disqualification Framework (Section 8 RPA 1951)",
                    "title_ta": "சட்டப்பூர்வ தகுதிநீக்க கட்டமைப்பு (பிரிவு 8 RPA 1951)",
                    "points": {
                        "en": [
                            "Section 8(1): Disqualification on conviction for specific listed offences (e.g. promoting enmity between classes, bribery, rape, untouchability offences, terror acts); disqualification continues for 6 years from date of conviction if fine, or period of sentence plus 6 years from release.",
                            "Section 8(2): Disqualification for conviction under food adulteration, dowry prohibition, or hoarding laws resulting in at least 6 months imprisonment.",
                            "Section 8(3): Blanket disqualification for ANY convicted offence resulting in imprisonment of NOT LESS THAN TWO YEARS. The person is disqualified from date of conviction and continues for 6 YEARS post-release.",
                            "Lily Thomas v. Union of India (2013): Landmark verdict striking down Section 8(4) of RPA 1951, which previously gave sitting MPs and MLAs a 3-month protection window to file an appeal and retain their seats. Sitting legislators now face IMMEDIATE disqualification upon conviction for 2+ years.",
                            "Public Interest Foundation v. UOI (2018): SC declined to disqualify candidates at the stage of charge-framing (held to be Parliament's prerogative), but mandated wide publicity of criminal cases by political parties.",
                            "Brajesh Singh v. Sunil Arora (2021): SC fined major political parties for contempt and mandated that parties MUST publish detailed reasons why a candidate with criminal antecedents was selected in preference to candidates without criminal background within 48 hours."
                        ],
                        "ta": [
                            "பிரிவு 8(1): லஞ்சம், பகைமை தூண்டுதல், தீண்டாமை, பயங்கரவாதம் போன்ற குறிப்பிட்ட சட்டப் பிரிவுகளின் கீழ் தண்டனை பெற்றால் 6 ஆண்டுகளுக்கு தகுதிநீக்கம்.",
                            "பிரிவு 8(2): உணவு கலப்படம், வரதட்சணை தடுப்புச் சட்டம் போன்ற சட்டங்களின் கீழ் குறைந்தது 6 மாத சிறைத் தண்டனை பெற்றால் தகுதிநீக்கம்.",
                            "பிரிவு 8(3): எந்தவொரு குற்றத்திற்காகவும் குறைந்தது 2 ஆண்டுகள் சிறைத் தண்டனை விதிக்கப்பட்டால், தீர்ப்பு வெளியான நாளிலிருந்து சிறைக்காலம் முடிந்து கூடுதலாக 6 ஆண்டுகள் வரை முழுமையான தகுதிநீக்கம்.",
                            "லில்லி தாமஸ் v. இந்திய அரசு (2013): பதவியில் இருக்கும் MP மற்றும் MLA-க்கள் மேல்முறையீடு செய்ய 3 மாத அவகாசம் வழங்கிய RPA 1951 பிரிவு 8(4)-ஐ உச்ச நீதிமன்றம் ரத்து செய்தது. இதனால் 2 ஆண்டுகள் தண்டனை பெற்ற எம்.பி./எம்.எல்.ஏ-க்கள் உடனடியாகப் பதவி இழக்க நேரிடும்.",
                            "பொது நல அறக்கட்டளை வழக்கு (2018): குற்றப்பத்திரிகை தாக்கல் செய்யப்பட்ட நிலையிலேயே வேட்பாளர்களை தகுதிநீக்கம் செய்ய முடியாது (நாடாளுமன்றமே சட்டம் இயற்ற வேண்டும்) என்று கூறியது, ஆனால் குற்றப் பின்னணியை பரவலாக விளம்பரம் செய்ய உத்தரவிட்டது.",
                            "பிரஜேஷ் சிங் வழக்கு (2021): குற்றப் பின்னணி கொண்ட வேட்பாளரை எந்த காரணத்திற்காக தேர்வு செய்தோம் என்பதை அரசியல் கட்சிகள் 48 மணி நேரத்திற்குள் செய்தித்தாட்கள் மற்றும் இணையதளத்தில் வெளியிட வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது."
                        ]
                    }
                }
            ],
            "sec_money_power_and_expenditure": [
                {
                    "title_en": "Expenditure Limits & Monitoring Framework",
                    "title_ta": "செலவு வரம்புகள் & கண்காணிப்பு கட்டமைப்பு",
                    "points": {
                        "en": [
                            "Statutory Basis: Governed by Section 77 of RPA 1951 and Rule 90 of Conduct of Elections Rules, 1961.",
                            "Revised Limits (2022 Revision): Lok Sabha (Major States: ₹95 Lakhs; Smaller States/UTs: ₹75 Lakhs); State Assemblies (Major States: ₹40 Lakhs; Smaller States/UTs: ₹28 Lakhs).",
                            "Candidate vs Party Loophole (Crucial Distinction): Expenditure limits apply ONLY to individual candidates. There is NO LEGAL CEILING on election expenditure by political parties (Kanwar Lal Gupta v. Amar Nath Chawla 1975 nullified by statutory amendment in 1974).",
                            "Monitoring Mechanisms: Mandatory separate bank account for all election transactions, Expenditure Observers appointed by ECI, Flying Squad Teams (FST), Static Surveillance Teams (SST), and Video Surveillance Teams (VST).",
                            "Submission of Accounts: Under Section 78 of RPA 1951, every candidate must submit an account of election expenses within 30 days from date of election result to DEO."
                        ],
                        "ta": [
                            "சட்டப்பூர்வ அடிப்படை: RPA 1951 பிரிவு 77 மற்றும் தேர்தல் நடத்தை விதிகள் 1961-ன் விதி 90 ஆகியவற்றால் நிர்வகிக்கப்படுகிறது.",
                            "திருத்தப்பட்ட செலவு வரம்புகள் (2022 திருத்தம்): மக்களவைத் தேர்தல் (பெரிய மாநிலங்கள்: ₹95 லட்சம்; சிறிய மாநிலங்கள்/யூனியன் பிரதேசங்கள்: ₹75 லட்சம்); சட்டமன்றத் தேர்தல் (பெரிய மாநிலங்கள்: ₹40 லட்சம்; சிறிய மாநிலங்கள்/யூனியன் பிரதேசங்கள்: ₹28 லட்சம்).",
                            "வேட்பாளர் vs கட்சி செலவு முரண்பாடு: தேர்தல் செலவு உச்சவரம்பு தனிப்பட்ட வேட்பாளர்களுக்கு மட்டுமே பொருந்தும். அரசியல் கட்சிகள் செலவு செய்வதற்கு எந்தவித சட்டப்பூர்வ உச்சவரம்பும் இல்லை!",
                            "கண்காணிப்பு முறைகள்: தேர்தல் செலவுகளுக்காக வங்கியில் தனிக் கணக்கு தொடங்குவது கட்டாயம், தேர்தல் செலவுப் பார்வையாளர்கள், பறக்கும் படைகள் (FST), நிலையான கண்காணிப்புக் குழுக்கள் (SST) மற்றும் வீடியோ கண்காணிப்புக் குழுக்கள்.",
                            "செலவு கணக்கு சமர்ப்பிப்பு: தேர்தல் முடிவுகள் வெளியான 30 நாட்களுக்குள் அனைத்து வேட்பாளர்களும் தங்களது தேர்தல் செலவு கணக்குகளை மாவட்டத் தேர்தல் அதிகாரியிடம் (DEO) சமர்ப்பிக்க வேண்டும் (பிரிவு 78)."
                        ]
                    }
                }
            ],
            "sec_paid_news_phenomenon": [
                {
                    "title_en": "Paid News Menace & Regulatory Response",
                    "title_ta": "கட்டணச் செய்தி அச்சுறுத்தல் & ஒழுங்குமுறை நடவடிக்கை",
                    "points": {
                        "en": [
                            "Definition: Paid News is defined by the Press Council of India (PCI) as 'any news or analysis appearing in any media (print or electronic) for a price in cash or kind as consideration.'",
                            "Impact: Misleads electors, subverts level-playing field, and bypasses candidate expenditure limits through undeclared campaign advertisements disguised as news.",
                            "MCMC Framework: ECI established Media Certification and Monitoring Committees (MCMC) at district and state levels to monitor print, electronic, and social media.",
                            "Expenditure Reckoning: If an MCMC confirms paid news, the commercial advertising value of that news space is officially added to the candidate's election expenditure account.",
                            "Law Commission Proposal: 255th Report recommended amending RPA 1951 to make paid news an explicit electoral offence punishable with minimum 2 years imprisonment."
                        ],
                        "ta": [
                            "வரையறை: இந்திய பத்திரிகை கவுன்சில் (PCI) கட்டணச் செய்தியை 'பணம் அல்லது பொருள் ஆதாயத்திற்காக அச்சு அல்லது மின்னணு ஊடகங்களில் செய்தியாக வெளியிடப்படும் விளம்பரம்' என வரையறுக்கிறது.",
                            "தாக்கம்: வாக்காளர்களை தவறாக வழிநடத்துகிறது, சமமான தேர்தல் களத்தை சீர்குலைக்கிறது மற்றும் தேர்தல் செலவு வரம்பை மறைமுகமாக மீறுகிறது.",
                            "MCMC கட்டமைப்பு: ஊடகங்களை கண்காணிக்க மாவட்ட மற்றும் மாநில அளவில் ஊடக சான்றளிப்பு மற்றும் கண்காணிப்புக் குழுக்களை (MCMC) ECI அமைத்துள்ளது.",
                            "செலவுக் கணக்கீடு: கட்டணச் செய்தி உறுதி செய்யப்பட்டால், அதற்கான விளம்பரக் கட்டணம் சம்பந்தப்பட்ட வேட்பாளரின் தேர்தல் செலவுக் கணக்கில் நேரடியாகச் சேர்க்கப்படும்.",
                            "சட்ட ஆணையப் பரிந்துரை: கட்டணச் செய்தியை குறைந்தபட்சம் 2 ஆண்டுகள் சிறைத் தண்டனைக்குரிய தேர்தல் குற்றமாக அறிவிக்க சட்டம் திருத்தப்பட வேண்டும் என 255வது அறிக்கை பரிந்துரைத்தது."
                        ]
                    }
                }
            ],
            "sec_state_funding_of_elections": [
                {
                    "title_en": "State Funding of Elections — Principles, Debates & Position",
                    "title_ta": "தேர்தல்களுக்கான அரசு நிதியுதவி — கோட்பாடுகள், விவாதங்கள் & நிலைப்பாடு",
                    "points": {
                        "en": [
                            "Concept: Government provides financial assistance to political parties or candidates to contest elections, either fully or partially, in cash or in kind.",
                            "Arguments in Favour: 1. Establishes genuine level-playing field for candidates without rich backers; 2. Weakens the corporate-politician funding nexus; 3. Enhances transparency and internal accountability.",
                            "Arguments Against: 1. Heavy fiscal burden on public exchequer; 2. Difficult to prevent parties from raising extra unaccounted cash on top of state funds; 3. Encourages non-serious candidates.",
                            "Committee Recommendations: 1. Dinesh Goswami (1990) & Indrajit Gupta (1998) explicitly recommended STATE FUNDING IN-KIND ONLY (paper, fuel, airtime, vehicles); 2. 2nd ARC (2007) recommended partial state funding to curb corruption.",
                            "Present Position: India provides limited in-kind assistance (free airtime on Doordarshan & All India Radio for recognized parties, subsidized electoral roll copies); NO direct cash funding exists."
                        ],
                        "ta": [
                            "கருத்து: அரசியல் கட்சிகள் அல்லது வேட்பாளர்கள் தேர்தலில் போட்டியிட அரசு முழுமையாகவோ அல்லது பகுதியாகவோ, ரொக்கமாகவோ அல்லது பொருள் வடிவிலோ நிதி உதவி வழங்குதல்.",
                            "ஆதரவு வாதங்கள்: 1. பணபலம் இல்லாத ஏழை வேட்பாளர்களுக்கும் சமமான களத்தை உருவாக்குகிறது; 2. கார்ப்பரேட்-அரசியல்வாதி பிணைப்பைத் தடுக்கிறது; 3. வெளிப்படைத்தன்மையை உறுதி செய்கிறது.",
                            "எதிர் வாதங்கள்: 1. அரசு கஜானாவிற்கு கடுமையான நிதிச் சுமை; 2. அரசு நிதிக்கு மேலாக கட்சிகள் கறுப்புப் பணத்தைப் பயன்படுத்துவதைத் தடுப்பது கடினம்; 3. தீவிரமில்லாத வேட்பாளர்கள் அதிகரிக்க வாய்ப்பு.",
                            "குழுக்களின் பரிந்துரைகள்: தினேஷ் கோஸ்வாமி (1990) மற்றும் இந்திரஜித் குப்தா (1998) குழுக்கள் பொருள் வடிவில் மட்டுமே அரசு உதவி வழங்கப்பட வேண்டும் எனப் பரிந்துரைத்தன.",
                            "தற்போதைய நிலை: தூர்தர்ஷன் மற்றும் அகில இந்திய வானொலியில் அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு இலவச ஒளிபரப்பு நேரம் மற்றும் வாக்காளர் பட்டியல் நகல்கள் போன்ற பொருள் வடிவிலான வரையறுக்கப்பட்ட உதவிகள் மட்டுமே நடைமுறையில் உள்ளன; நேரடி ரொக்க நிதியுதவி இல்லை."
                        ]
                    }
                }
            ],
            "sec_electoral_admin_technology": [
                {
                    "title_en": "Digital Electoral Architecture (cVIGIL, Suvidha & Voter Portals)",
                    "title_ta": "டிஜிட்டல் தேர்தல் கட்டமைப்பு (cVIGIL, சுவிதா & வாக்காளர் செயலிகள்)",
                    "points": {
                        "en": [
                            "cVIGIL App: Innovative mobile application for citizens to report Model Code of Conduct violations and money distribution in real-time. Automatically geotags violations with live photos/videos; ECI Flying Squad investigates within 100 MINUTES.",
                            "Suvidha Candidate Portal: Single-window digital platform for candidates to apply for rally permissions, vehicle permits, and public meeting approvals without bureaucratic delays.",
                            "Voters' Service Portal (voters.eci.gov.in) & Voter Helpline App: Citizen services for online registration, track application, locate polling booth, and download digital e-EPIC.",
                            "Accessible Elections (PwD & Senior Citizens): Braille ballot sheets on EVM units, wheelchair ramps, pick-and-drop facilities, and home postal voting for electors aged 85+ and benchmark PwDs (amended Conduct of Elections Rules 1961)."
                        ],
                        "ta": [
                            "cVIGIL செயலி: தேர்தல் நடத்தை விதிமீறல்கள் மற்றும் பணப் பட்டுவாடாவை பொதுமக்கள் புகைப்படம்/வீடியோ எடுத்து உடனுக்குடன் புகார் அளிக்கும் செயலி. ஜிபிஎஸ் இருப்பிடத்துடன் பதிவாகும் புகார்கள் மீது பறக்கும் படை 100 நிமிடங்களுக்குள் நடவடிக்கை எடுக்கிறது.",
                            "சுவிதா (Suvidha) இணையதளம்: தேர்தல் பேரணிகள், பொதுக்கூட்டங்கள் மற்றும் வாகன அனுமதிகளை வேட்பாளர்கள் பெறுவதற்கான ஒற்றைச் சாளர டிஜிட்டல் தளம்.",
                            "வாக்காளர் சேவை தளம் (Voters' Portal): ஆன்லைனில் வாக்காளர் பதிவு, முகவரி மாற்றம் மற்றும் டிஜிட்டல் e-EPIC கார்டை பதிவிறக்கம் செய்ய உதவுகிறது.",
                            "மாற்றுத்திறனாளிகளுக்கான வசதிகள்: EVM இயந்திரங்களில் பிரெய்லி எழுத்துக்கள், சாய்தளங்கள் மற்றும் 85 வயதுக்கு மேற்பட்ட முதியவர்கள் மற்றும் மாற்றுத்திறனாளிகளுக்கு வீட்டிலிருந்தே தபால் வாக்குப்பதிவு செய்யும் வசதி."
                        ]
                    }
                }
            ],
            "comparison_tables": [
                {
                    "id": "tbl_electoral_committees_summary",
                    "title_en": "Summary of Major Electoral Reform Committees",
                    "title_ta": "முக்கிய தேர்தல் சீர்திருத்தக் குழுக்களின் சுருக்க அட்டவணை",
                    "headers_en": ["Year", "Committee / Commission", "Chairperson", "Key Milestone Recommendation", "Implementation Status"],
                    "headers_ta": ["ஆண்டு", "குழு / ஆணையம்", "தலைவர்", "முக்கிய மைல்கல் பரிந்துரை", "செயல்படுத்தப்பட்ட நிலை"],
                    "rows_en": [
                        ["1974–75", "Tarkunde Committee", "V.M. Tarkunde", "Multi-member ECI; Lowering voting age to 18", "Voting age lowered in 1988; Multi-member ECI in 1993"],
                        ["1990", "Dinesh Goswami Committee", "Dinesh Goswami", "Introduction of EVMs; State assistance in-kind", "EVMs legalized under Sec 61A; In-kind airtime implemented"],
                        ["1993", "Vohra Committee", "N.N. Vohra", "Nexus between crime syndicates and politicians", "Triggered judicial interventions on candidate criminal records"],
                        ["1998", "Indrajit Gupta Committee", "Indrajit Gupta", "State funding of elections IN-KIND ONLY to recognized parties", "Free airtime on state media accepted; full in-kind pending"],
                        ["1999", "Law Commission (170th Report)", "Justice B.P. Jeevan Reddy", "Proportional list system; Internal party democracy", "Party democracy and list system still pending legislation"],
                        ["2002", "NCRWC", "Justice M.N. Venkatachaliah", "Disqualification on charge-framing; High-level selection panel", "Selection panel enacted in 2023; charge-framing pending"],
                        ["2015", "Law Commission (255th Report)", "Justice A.P. Shah", "Cap cash donations at ₹2,000; criminalise paid news", "Cash cap at ₹2,000 enacted in 2017; paid news criminalisation pending"]
                    ],
                    "rows_ta": [
                        ["1974–75", "தார்குண்டே குழு", "வி.எம். தார்குண்டே", "பல உறுப்பினர் ஆணையம்; வாக்குரிமை வயது 18 ஆகக் குறைப்பு", "1988-ல் வாக்குரிமை வயது குறைப்பு; 1993-ல் பல உறுப்பினர் ஆணையம் அமல்"],
                        ["1990", "தினேஷ் கோஸ்வாமி குழு", "தினேஷ் கோஸ்வாமி", "EVM இயந்திரங்கள் அறிமுகம்; பொருள் வடிவில் அரசு உதவி", "பிரிவு 61A-ன் கீழ் EVM-க்கு அங்கீகாரம்; இலவச ஒளிபரப்பு நேரம் அமல்"],
                        ["1993", "வோஹ்ரா குழு", "என்.என். வோஹ்ரா", "குற்றவாளிகள் மற்றும் அரசியல்வாதிகள் இடையிலான பிணைப்பு", "வேட்பாளர் குற்றப்பதிவு மீதான உச்ச நீதிமன்றத் தீர்ப்புகளுக்கு வித்திட்டது"],
                        ["1998", "இந்திரஜித் குப்தா குழு", "இந்திரஜித் குப்தா", "பொருள் வடிவில் மட்டுமே அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு அரசு நிதியுதவி", "அரசு ஊடகங்களில் இலவச ஒளிபரப்பு அமல்; பிற உதவிகள் பரிசீலனையில்"],
                        ["1999", "சட்ட ஆணையம் (170வது அறிக்கை)", "நீதிபதி பி.பி. ஜீவன் ரெட்டி", "விகிதாச்சார பட்டியல் முறை; கட்சிகளுக்குள் உட்கட்சி ஜனநாயகம்", "உட்கட்சி ஜனநாயகம் சட்டம் இன்னும் இயற்றப்படவில்லை"],
                        ["2002", "NCRWC அரசியலமைப்பு சீராய்வு", "நீதிபதி எம்.என். வெங்கடாசலையா", "குற்றப்பத்திரிகை நிலையிலேயே தகுதிநீக்கம்; தேர்வுக் குழு", "2023-ல் நியமனக் குழு சட்டம் அமல்; குற்றப்பத்திரிகை தகுதிநீக்கம் நிலுவை"],
                        ["2015", "சட்ட ஆணையம் (255வது அறிக்கை)", "நீதிபதி ஏ.பி. ஷா", "ரொக்க நன்கொடை ₹2,000 ஆகக் குறைப்பு; கட்டணச் செய்திக்கு சிறை", "2017-ல் ₹2,000 வரம்பு அமல்; கட்டணச் செய்தி சிறைத் தண்டனை நிலுவை"]
                    ]
                },
                {
                    "id": "tbl_evm_vs_vvpat",
                    "title_en": "EVM vs VVPAT Technical Comparison",
                    "title_ta": "EVM vs VVPAT தொழில்நுட்ப ஒப்பீடு",
                    "headers_en": ["Parameter", "Electronic Voting Machine (EVM)", "Voter Verifiable Paper Audit Trail (VVPAT)"],
                    "headers_ta": ["அளவுரு", "மின்னணு வாக்குப்பதிவு இயந்திரம் (EVM)", "காகித தணிக்கைப் பதிவு (VVPAT)"],
                    "rows_en": [
                        ["Core Function", "Records and tallies votes electronically", "Prints independent paper slip verifying the electronic vote"],
                        ["Components", "Control Unit (CU) + Balloting Unit (BU)", "Printer Unit with transparent viewing window & sealed drop box"],
                        ["Display to Voter", "Red LED glows against selected candidate and audio beep", "Paper slip displayed for 7 SECONDS before dropping into box"],
                        ["Legal Basis", "Section 61A of RPA 1951 (enacted 1988)", "Conduct of Elections (Amendment) Rules 2013 (Rules 49A/49M)"],
                        ["Counting Role", "Primary source of automated vote counting", "Audit verification (mandatory 5 polling stations per constituency)"]
                    ],
                    "rows_ta": [
                        ["முதன்மைப் பணி", "வாக்குகளை மின்னணு முறையில் பதிவு செய்து கணக்கிடுகிறது", "மின்னணு வாக்கை சரிபார்க்க சுதந்திரமான காகிதச் சீட்டை அச்சிடுகிறது"],
                        ["அலகுகள்", "கட்டுப்பாட்டு அலகு (CU) + வாக்குப்பதிவு அலகு (BU)", "கண்ணாடி சாளரம் மற்றும் சீலிடப்பட்ட பெட்டியுடன் கூடிய அச்சுப்பொறி"],
                        ["வாக்காளருக்குக் காட்சி", "சிவப்பு LED விளக்கு எரியும் மற்றும் பீப் ஒலி கேட்கும்", "காகிதச் சீட்டு 7 வினாடிகள் தெரியும், பின்னர் பெட்டியில் விழும்"],
                        ["சட்ட அடிப்படை", "RPA 1951 பிரிவு 61A (1988-ல் இயற்றப்பட்டது)", "தேர்தல் நடத்தை விதிகள் 2013 (விதிகள் 49A/49M)"],
                        ["எண்ணிக்கையில் பங்கு", "தானியங்கி வாக்கு எண்ணிக்கையின் முதன்மை ஆதாரம்", "தணிக்கை சரிபார்ப்பு (ஒரு தொகுதிக்கு 5 வாக்குச்சாவடிகள் கட்டாயம்)"]
                    ]
                },
                {
                    "id": "tbl_candidate_vs_party_expenditure",
                    "title_en": "Candidate Expenditure vs Political Party Expenditure",
                    "title_ta": "வேட்பாளர் செலவு vs அரசியல் கட்சி செலவு ஒப்பீடு",
                    "headers_en": ["Feature", "Candidate Expenditure", "Political Party Expenditure"],
                    "headers_ta": ["அம்சம்", "வேட்பாளர் செலவு", "அரசியல் கட்சி செலவு"],
                    "rows_en": [
                        ["Legal Ceiling", "Strict statutory limit (Lok Sabha: ₹95L/₹75L; Assembly: ₹40L/₹28L)", "NO LEGAL CEILING under Indian election law"],
                        ["Bank Account Mandate", "Mandatory dedicated separate bank account for all transactions", "Separate account maintained but unlimited general expenditure permitted"],
                        ["Filing Deadline", "Within 30 days of result declaration to DEO under Sec 78 RPA 1951", "Annual contribution & audit reports filed with ECI under Sec 29C"],
                        ["Consequence of Default", "Disqualification up to 3 years under Section 10A of RPA 1951", "Loss of tax exemption under Section 13A of Income Tax Act 1961"]
                    ],
                    "rows_ta": [
                        ["சட்டப்பூர்வ வரம்பு", "கட்டாய வரம்பு (மக்களவை: ₹95L/₹75L; சட்டமன்றம்: ₹40L/₹28L)", "எவ்வித சட்டப்பூர்வ உச்சவரம்பும் கிடையாது"],
                        ["வங்கிக் கணக்கு", "அனைத்து பரிவர்த்தனைகளுக்கும் பிரத்யேக தனிக் கணக்கு கட்டாயம்", "கட்சிக் கணக்கில் வரம்பற்ற பொது தேர்தல் செலவுகள் அனுமதிக்கப்படுகிறது"],
                        ["தாக்கல் காலக்கெடு", "தேர்தல் முடிவுகள் வெளியான 30 நாட்களுக்குள் DEO-விடம் தாக்கல் (பிரிவு 78)", "ஆண்டு தணிக்கை அறிக்கைகள் ECI-யிடம் தாக்கல் செய்யப்பட வேண்டும் (பிரிவு 29C)"],
                        ["மீறலின் விளைவு", "RPA 1951 பிரிவு 10A-ன் கீழ் 3 ஆண்டுகள் வரை தேர்தலில் போட்டியிட தகுதிநீக்கம்", "வருமான வரிச் சட்டம் 1961 பிரிவு 13A-ன் கீழ் வரி விலக்கு ரத்து செய்யப்படும்"]
                    ]
                }
            ],
            "important_facts": {
                "en": [
                    "EVMs were first used in Kerala (Paravur Assembly) in 1982; statutory backing provided via Section 61A of RPA 1951 in 1988.",
                    "Subramanian Swamy v. ECI (2013) made VVPAT mandatory for free and fair elections.",
                    "Lily Thomas v. UOI (2013) invalidated Section 8(4) of RPA 1951, ending the 3-month protection window for convicted lawmakers.",
                    "cVIGIL app guarantees response from ECI Flying Squads within 100 minutes of citizen complaint.",
                    "Indrajit Gupta Committee (1998) recommended state funding of elections in-kind only to recognized parties."
                ],
                "ta": [
                    "EVM இயந்திரங்கள் 1982-ல் கேரளாவில் (பரவூர்) முதன்முதலில் பயன்படுத்தப்பட்டன; 1988-ல் RPA 1951 பிரிவு 61A மூலம் சட்ட அங்கீகாரம் பெற்றது.",
                    "சுப்பிரமணியன் சுவாமி வழக்கில் (2013) VVPAT பயன்பாடு கட்டாயம் என உச்ச நீதிமன்றம் உத்தரவிட்டது.",
                    "லில்லி தாமஸ் தீர்ப்பு (2013) RPA பிரிவு 8(4)-ஐ ரத்து செய்து, தண்டனை பெற்ற எம்.பி./எம்.எல்.ஏ-க்களுக்கு இருந்த 3 மாத பாதுகாப்பை முடிவுக்குக் கொண்டுவந்தது.",
                    "cVIGIL செயலியில் பெறப்படும் தேர்தல் நடத்தை விதிமீறல் புகார்கள் மீது 100 நிமிடங்களுக்குள் பறக்கும் படை நடவடிக்கை எடுக்கிறது.",
                    "இந்திரஜித் குப்தா குழு (1998) அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு பொருள் வடிவில் மட்டுமே அரசு நிதியுதவி அளிக்க வேண்டும் எனப் பரிந்துரைத்தது."
                ]
            },
            "tnpsc_traps": [
                {
                    "title": "1. Model Code of Conduct Legal Status Trap (மாதிரி நடத்தை விதி சட்ட அந்தஸ்து பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Assuming the Model Code of Conduct (MCC) is an Act passed by Parliament with statutory criminal penalties.",
                            "FACT: The MCC is non-statutory; it evolved out of voluntary political consensus in 1968 and derives operational authority from ECI's plenary powers under Article 324."
                        ],
                        "ta": [
                            "பொறி: மாதிரி நடத்தை விதி (MCC) நாடாளுமன்றத்தால் இயற்றப்பட்ட சட்டப்பூர்வ சட்டம் என நினைப்பது.",
                            "உண்மை: MCC என்பது சட்டப்பூர்வமானது அல்ல; 1968-ல் அரசியல் கட்சிகளின் ஒருமித்த கருத்து மற்றும் உறுப்பு 324-ன் கீழ் தேர்தல் ஆணையத்திற்கு உள்ள முழு அதிகாரத்தின் அடிப்படையிலேயே செயல்படுத்தப்படுகிறது."
                        ]
                    }
                },
                {
                    "title": "2. NOTA Highest Votes Trap (நோட்டா அதிக வாக்குகள் பெற்றால் ஏற்படும் விளைவுப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing that if NOTA receives the maximum votes in a Parliamentary or Assembly constituency, the election is canceled and a fresh poll is called.",
                            "FACT: NOTA possesses NO negative veto power in general elections. The candidate securing the second highest (highest valid non-NOTA) votes is declared the winner."
                        ],
                        "ta": [
                            "பொறி: ஒரு தொகுதியில் நோட்டா அதிக வாக்குகள் பெற்றால், தேர்தல் ரத்து செய்யப்பட்டு மறுதேர்தல் நடத்தப்படும் என நினைப்பது.",
                            "உண்மை: பொதுத்தேர்தல்களில் நோட்டாவிற்கு நிராகரிக்கும் அதிகாரம் (Negative Veto) கிடையாது. நோட்டாவுக்கு அடுத்தபடியாக அதிக செல்லுபடியாகும் வாக்கு பெற்ற வேட்பாளரே வெற்றி பெற்றவராக அறிவிக்கப்படுவார்."
                        ]
                    }
                },
                {
                    "title": "3. Political Party Spending Ceiling Trap (அரசியல் கட்சி தேர்தல் செலவு உச்சவரம்புப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Assuming registered political parties face a statutory expenditure limit during general elections like individual candidates.",
                            "FACT: Expenditure limits under Rule 90 apply ONLY to individual contesting candidates (Rs 95 Lakhs / Rs 40 Lakhs). Political parties currently face NO statutory ceiling on their total election expenditure."
                        ],
                        "ta": [
                            "பொறி: வேட்பாளர்களைப் போல அரசியல் கட்சிகளுக்கும் தேர்தலில் செலவழிக்க சட்டப்பூர்வ உச்சவரம்பு உண்டு என நினைப்பது.",
                            "உண்மை: தேர்தல் செலவு உச்சவரம்பு தனிப்பட்ட வேட்பாளர்களுக்கு மட்டுமே பொருந்தும் (ரூ.95 லட்சம் / ரூ.40 லட்சம்). கட்சிகள் செலவு செய்வதற்கு தற்போதைக்கு சட்டப்பூர்வ உச்சவரம்பு எதுவும் இல்லை."
                        ]
                    }
                },
                {
                    "title": "4. Convicted Lawmakers 3-Month Protection Trap (குற்றவாளிகளான மக்கள் பிரதிநிதிகள் 3 மாத சலுகைப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing sitting MPs or MLAs have a 3-month protection period to file an appeal before facing disqualification upon conviction.",
                            "FACT: Section 8(4) of RPA 1951 was struck down as unconstitutional by the Supreme Court in Lily Thomas v. UOI (2013). Disqualification for a 2+ years prison sentence is INSTANTANEOUS."
                        ],
                        "ta": [
                            "பொறி: சிறைத்தண்டனை பெற்ற சட்டமன்ற, நாடாளுமன்ற உறுப்பினர்கள் தகுதிநீக்கத்திலிருந்து தப்பிக்க 3 மாத மேல்முறையீட்டு கால அவகாசம் உண்டு என நினைப்பது.",
                            "உண்மை: லில்லி தாமஸ் வழக்கில் (2013) உச்சநீதிமன்றம் பிரிவு 8(4)-ஐ ரத்து செய்ததால், 2 ஆண்டுகளுக்கு மேல் சிறை தண்டனை விதிக்கப்பட்ட மறுவினாடியே பதவி பறிபோகும்."
                        ]
                    }
                }
            ],
            "quick_revision": {
                "en": [
                    "Tarkunde Committee (1974): Multi-member Election Commission, lowering voting age to 18.",
                    "Dinesh Goswami Committee (1990): Statutory backing for EVMs, state assistance in kind, time limit for by-elections.",
                    "Indrajit Gupta Committee (1998): State funding of elections exclusively in kind to recognized political parties.",
                    "EVM Architecture: Standalone, battery-powered, non-networked device with Control Unit (CU) and Ballot Unit (BU) secured by One-Time Programmable (OTP) chips.",
                    "VVPAT: Mandated in Subramanian Swamy (2013); displays 7-second slip; mandatory counting of 5 polling stations per assembly constituency.",
                    "NOTA: Introduced in PUCL (2013); symbol designed by NID Ahmedabad; acts as symbolic protest with no veto power.",
                    "Lily Thomas (2013): Invalidated Section 8(4) of RPA 1951, enforcing instant disqualification on 2+ years conviction.",
                    "Expenditure Limits (2022): Lok Sabha: Rs 95 Lakhs (large states) / Rs 75 Lakhs (small states); Assembly: Rs 40 Lakhs / Rs 28 Lakhs."
                ],
                "ta": [
                    "தார்குண்டே குழு (1974): பல உறுப்பினர்களைக் கொண்ட தேர்தல் ஆணையம், வாக்களிக்கும் வயதை 18 ஆகக் குறைத்தல்.",
                    "தினேஷ் கோஸ்வாமி குழு (1990): EVM இயந்திரங்களுக்கு சட்ட அங்கீகாரம், அரசு சார்பில் பொருட்கள் வடிவிலான உதவி, இடைத்தேர்தல்களுக்கான கால வரம்பு.",
                    "இந்திரஜித் குப்தா குழு (1998): அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு மட்டுமே பொருள் வடிவிலான அரசு தேர்தல் நிதியுதவி வழங்குதல்.",
                    "EVM கட்டமைப்பு: இணைய தொடர்பு இல்லாத, பேட்டரியில் இயங்கும், கட்டுப்பாட்டுப் பிரிவு மற்றும் வாக்குப்பதிவுப் பிரிவு கொண்ட தனித்த சாதனம்.",
                    "VVPAT: சுப்பிரமணியன் சுவாமி வழக்கில் (2013) கட்டாயமாக்கப்பட்டது; 7 வினாடிகள் ரசீது காட்டும்; தொகுதிக்கு 5 வாக்குச்சாவடி தாள்கள் கட்டாயம் சரிபார்ப்பு.",
                    "நோட்டா (NOTA): PUCL வழக்கில் (2013) அறிமுகம்; அகமதாபாத் NID வடிவமைத்த சின்னம்; நிராகரிக்கும் அதிகாரம் இல்லாத குறியீட்டு எதிர்ப்பு வாக்கு.",
                    "லில்லி தாமஸ் வழக்கு (2013): பிரிவு 8(4)-ஐ ரத்து செய்து, 2+ ஆண்டுகள் சிறை தண்டனை விதிக்கப்பட்டால் உடனடி பதவி நீக்கம் அமல்.",
                    "செலவு உச்சவரம்பு (2022): மக்களவை: ரூ.95 லட்சம் / ரூ.75 லட்சம்; சட்டமன்றம்: ரூ.40 லட்சம் / ரூ.28 லட்சம்."
                ]
            },
            "expected_questions": [
                {
                    "type": "prelims",
                    "question_en": "Which landmark Supreme Court judgment struck down Section 8(4) of the RPA 1951 leading to immediate disqualification of convicted legislators?",
                    "question_ta": "குற்றவாளிகளான சட்டமன்ற, நாடாளுமன்ற உறுப்பினர்களின் உடனடி தகுதிநீக்கத்திற்கு வழிவகுத்த RPA 1951 பிரிவு 8(4)-ஐ ரத்து செய்த வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்றத் தீர்ப்பு எது?",
                    "answer_en": "Lily Thomas v. Union of India (2013).",
                    "answer_ta": "லில்லி தாமஸ் v. இந்திய அரசு (2013)."
                },
                {
                    "type": "prelims",
                    "question_en": "Which committee specifically recommended that State Funding of Elections should be provided ONLY IN-KIND and never in cash?",
                    "question_ta": "தேர்தல்களுக்கான அரசு நிதியுதவி ரொக்கமாக அல்லாமல் பொருள் வடிவில் மட்டுமே வழங்கப்பட வேண்டும் என்று குறிப்பாகப் பரிந்துரைத்த குழு எது?",
                    "answer_en": "Indrajit Gupta Committee on State Funding of Elections (1998).",
                    "answer_ta": "இந்திரஜித் குப்தா குழு (1998)."
                }
            ],
            "pyq_references": [
                {
                    "year": "2021",
                    "exam": "TNPSC Group 1 Mains",
                    "question": "Critically analyze the role of the Model Code of Conduct in ensuring free and fair elections in India.",
                    "question_en": "Critically analyze the role of the Model Code of Conduct in ensuring free and fair elections in India.",
                    "question_ta": "இந்தியாவில் சுதந்திரமான மற்றும் நியாயமான தேர்தல்களை உறுதி செய்வதில் தேர்தல் நடத்தை நெறிமுறைகளின் (MCC) பங்கை திறனாய்வு செய்க."
                }
            ],
            "revision_cards": [
                {
                    "id": "card_p2_1",
                    "front_en": "What is the legal status and operational timing of the Model Code of Conduct (MCC)?",
                    "front_ta": "தேர்தல் நடத்தை விதிமுறைகளின் (MCC) சட்ட அந்தஸ்து மற்றும் செயல்படும் காலம் என்ன?",
                    "back_en": "Non-statutory (evolved out of consensus, enforced under Art. 324). It operates from the exact date/hour of ECI's election announcement until the declaration of results.",
                    "back_ta": "சட்டப்பூர்வமற்றது (அரசியல் கட்சிகளின் ஒருமித்த கருத்து மற்றும் உறுப்பு 324-ன் கீழ் அமல்). தேர்தல் தேதிகள் அறிவிக்கப்பட்ட வினாடி முதல் தேர்தல் முடிவுகள் வெளியாகும் வரை நடைமுறையில் இருக்கும்."
                },
                {
                    "id": "card_p2_2",
                    "front_en": "What happens if NOTA secures the highest votes in a Lok Sabha constituency?",
                    "front_ta": "மக்களவைத் தொகுதியில் நோட்டா அதிக வாக்குகளைப் பெற்றால் என்ன நடக்கும்?",
                    "back_en": "The candidate who receives the highest number of valid non-NOTA votes is declared elected. NOTA does not trigger a re-election.",
                    "back_ta": "நோட்டாவுக்கு அடுத்தபடியாக அதிக வாக்குகள் பெற்ற வேட்பாளரே வெற்றி பெற்றவராக அறிவிக்கப்படுவார். நோட்டாவால் மறுதேர்தல் நடத்தப்படாது."
                },
                {
                    "id": "card_p2_3",
                    "front_en": "What is the consequence under Section 8(3) of RPA 1951 if an MP or MLA is convicted and sentenced to 2 years imprisonment?",
                    "front_ta": "ஓர் எம்.பி. அல்லது எம்.எல்.ஏ. 2 ஆண்டுகள் சிறைத் தண்டனை பெற்றால் RPA 1951 பிரிவு 8(3)-ன் கீழ் ஏற்படும் விளைவு என்ன?",
                    "back_en": "Immediate disqualification from the date of conviction, continuing for the duration of the sentence PLUS an additional 6 years after release (total 8+ years).",
                    "back_ta": "தீர்ப்பு வெளியான நாளிலிருந்து உடனடியாகப் பதவி இழப்பார்; தண்டனைக் காலம் முழுவதும் மற்றும் சிறையிலிருந்து வெளிவந்த பிறகு கூடுதலாக 6 ஆண்டுகள் தேர்தலில் போட்டியிட முடியாது."
                }
            ],
            "mind_map": [
                {
                    "title": "MAJOR ELECTORAL REFORMS (PART 2)",
                    "short_label": "Practical Reforms",
                    "children": [
                        {
                            "title": "Reform Committees",
                            "short_label": "Committees",
                            "children": [
                                {"title": "Tarkunde (1974): 18-yr vote, Multi-member ECI", "short_label": "Tarkunde"},
                                {"title": "Dinesh Goswami (1990): EVMs, In-kind help", "short_label": "Goswami"},
                                {"title": "Indrajit Gupta (1998): State Funding In-Kind Only", "short_label": "Gupta"},
                                {"title": "Law Commission 170th & 255th: Party Funds & Democracy", "short_label": "Law Comm"}
                            ]
                        },
                        {
                            "title": "Technological Revolution",
                            "short_label": "Tech",
                            "children": [
                                {"title": "EVM: Sec 61A RPA 1951, Standalone CU+BU", "short_label": "EVM"},
                                {"title": "VVPAT: 7-sec slip, Subramanian Swamy (2013)", "short_label": "VVPAT"},
                                {"title": "cVIGIL & Suvidha: 100-min response apps", "short_label": "cVIGIL"}
                            ]
                        },
                        {
                            "title": "Candidate & Transparency Reforms",
                            "short_label": "Integrity",
                            "children": [
                                {"title": "Form 26 Affidavit: Criminal, Assets, Education (ADR 2002)", "short_label": "Affidavit"},
                                {"title": "Sec 8 RPA: 2+ yrs sentence = Immediate disqualification (Lily Thomas)", "short_label": "Sec 8"},
                                {"title": "MCC: Non-statutory, effective on announcement", "short_label": "MCC"},
                                {"title": "NOTA: PUCL (2013), No veto power", "short_label": "NOTA"}
                            ]
                        }
                    ]
                }
            ]
        }
    }

    out_path = 'data/notes/polity/electoral_reforms_part_2.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(part2_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Part 2 generated successfully at {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == '__main__':
    build_part2()
