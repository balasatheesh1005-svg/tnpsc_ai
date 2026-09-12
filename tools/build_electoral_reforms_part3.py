# -*- coding: utf-8 -*-
"""
Builder script for Electoral Reforms Part 3:
CONTEMPORARY REFORMS + JUDICIAL DEVELOPMENTS + CRITICAL ANALYSIS
Conforms strictly to the production Notes JSON schema (matching governor_part_1.json).
"""
import json
import os
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def build_part_3():
    data = {
        "subject": "polity",
        "topic": "Electoral Reforms",
        "language": "English + Tamil",
        "ui_type": "standard_notes",
        "reading_time": "32 mins",
        "completion_pct": 100,
        "difficulty": "Advanced",
        "metadata": {
            "topic_id": "electoral_reforms",
            "repository_id": "polity_electoral_reforms",
            "display_title": "Electoral Reforms — Part 3: Contemporary Reforms, Judicial Developments & Critical Analysis",
            "part": 3,
            "total_parts": 3,
            "subject": "polity",
            "chapter": "Electoral Reforms",
            "language": "English + Tamil",
            "schema_version": "2.0",
            "last_updated": "2026-09-05"
        },
        "meta": {
            "title": "Electoral Reforms — Part 3: Contemporary Reforms & Landmark Judgments",
            "sub_title": "Political Funding, Electoral Bonds Verdict 2024, Simultaneous Elections (ONOE), 106th Amendment (Women's Reservation), Landmark Supreme Court Verdicts & Critical Analysis",
            "syllabus_topic": "Electoral Reforms, Political Funding, Simultaneous Elections, Landmark Judgments, Criminalisation & ECI Independence"
        },
        "keywords": [
            "Electoral Reforms",
            "Electoral Bonds Verdict 2024",
            "ADR v. Union of India",
            "Simultaneous Elections",
            "One Nation One Election",
            "Kovind Committee 2024",
            "106th Constitutional Amendment Act 2023",
            "Nari Shakti Vandan Adhiniyam",
            "Article 330A",
            "Article 332A",
            "Article 334A",
            "Anoop Baranwal Case 2023",
            "CEC and EC Appointment Act 2023",
            "Remote Voting RVM",
            "ETPBS Postal Ballot",
            "Inner-Party Democracy",
            "Lily Thomas Case",
            "PUCL NOTA 2013",
            "VVPAT Verification 2024"
        ],
        "learning_outcomes": [
            "Analyze the landmark 2024 Supreme Court Constitution Bench verdict striking down the Electoral Bonds Scheme.",
            "Evaluate the constitutional, federal, and logistical facets of Simultaneous Elections (One Nation, One Election) and the Kovind Committee recommendations (2024).",
            "Master the constitutional framework of the 106th Constitutional Amendment Act 2023 (Nari Shakti Vandan Adhiniyam) and Articles 330A, 332A, 334A.",
            "Trace the evolution of ECI appointment mechanisms from Anoop Baranwal (2023) to the CEC and Other ECs Act 2023.",
            "Memorize all high-yield landmark Supreme Court judgments concerning electoral jurisprudence for TNPSC Prelims and Mains."
        ],
        "sections": [
            {
                "id": "sec_political_funding_bonds",
                "title_en": "1. Political Funding Reforms & Electoral Bonds Verdict 2024",
                "title_ta": "1. அரசியல் நிதி சீர்திருத்தங்கள் மற்றும் தேர்தல் பத்திரங்கள் தீர்ப்பு 2024",
                "type": "concept"
            },
            {
                "id": "sec_electoral_transparency",
                "title_en": "2. Electoral Transparency & Corporate Donations",
                "title_ta": "2. தேர்தல் வெளிப்படைத்தன்மை மற்றும் நிறுவன நன்கொடைகள்",
                "type": "concept"
            },
            {
                "id": "sec_inner_party_democracy",
                "title_en": "3. Inner-Party Democracy & Organizational Elections",
                "title_ta": "3. கட்சிகளுக்குள் மக்களாட்சி மற்றும் உட்கட்சித் தேர்தல்கள்",
                "type": "concept"
            },
            {
                "id": "sec_simultaneous_elections",
                "title_en": "4. Simultaneous Elections / One Nation, One Election (ONOE)",
                "title_ta": "4. ஒரே நாடு, ஒரே தேர்தல் / ஒரே நேரத்தில் தேர்தல்கள்",
                "type": "concept"
            },
            {
                "id": "sec_remote_voting_migrants",
                "title_en": "5. Remote Voting for Domestic Migrants (RVM)",
                "title_ta": "5. புலம் பெயர்ந்தோருக்கான தொலைதூர வாக்குப்பதிவு (RVM)",
                "type": "concept"
            },
            {
                "id": "sec_postal_ballots_accessibility",
                "title_en": "6. Postal Ballots, ETPBS & Home Voting Accessibility",
                "title_ta": "6. தபால் வாக்குகள், ETPBS மற்றும் இல்ல வாக்களிப்பு அணுகல்தன்மை",
                "type": "concept"
            },
            {
                "id": "sec_women_representation_106th",
                "title_en": "7. Women's Representation & 106th Constitutional Amendment Act, 2023",
                "title_ta": "7. மகளிர் பிரதிநிதித்துவம் மற்றும் 106-வது அரசியலமைப்பு திருத்தச் சட்டம், 2023",
                "type": "concept"
            },
            {
                "id": "sec_criminalisation_further_reforms",
                "title_en": "8. Criminalisation of Politics — Further Judicial Reforms",
                "title_ta": "8. அரசியலில் குற்றமயமாதல் — கூடுதல் நீதித்துறை சீர்திருத்தங்கள்",
                "type": "concept"
            },
            {
                "id": "sec_eci_independence_appointment",
                "title_en": "9. Independence of ECI & The Appointment Act 2023",
                "title_ta": "9. தேர்தல் ஆணையத்தின் தன்னாட்சி மற்றும் நியமனச் சட்டம் 2023",
                "type": "concept"
            },
            {
                "id": "sec_landmark_sc_judgments",
                "title_en": "10. Landmark Supreme Court Judgments on Elections (1978–2024)",
                "title_ta": "10. தேர்தல் தொடர்பான முக்கிய உச்சநீதிமன்றத் தீர்ப்புகள் (1978–2024)",
                "type": "concept"
            },
            {
                "id": "sec_challenges_way_forward",
                "title_en": "11. Contemporary Challenges, Way Forward & Critical Analysis",
                "title_ta": "11. தற்கால சவால்கள், முன்னோக்கிய பாதை மற்றும் முழுமையான ஆய்வு",
                "type": "concept"
            }
        ],
        "content": {
            "definition": {
                "en": "Contemporary electoral reforms in India encompass cutting-edge judicial rulings (such as the 2024 invalidation of Electoral Bonds and directions on candidate antecedents), legislative milestones (the 106th Constitutional Amendment reserving one-third seats for women and the 2023 ECI Appointment Act), technological adaptations (Remote Voting Machines and ETPBS), and major institutional debates including Simultaneous Elections (One Nation, One Election) to fortify constitutional morality, transparency, and federal democracy.",
                "ta": "இந்தியாவில் தற்கால தேர்தல் சீர்திருத்தங்கள் என்பது அதிமுக்கிய நீதித்துறை தீர்ப்புகள் (2024 தேர்தல் பத்திர திட்ட ரத்து மற்றும் வேட்பாளர் குற்றப்பின்னணி வழிகாட்டுதல்கள்), சட்டப்பூர்வ மைல்கற்கள் (மகளிருக்கு 33% இடஒதுக்கீடு வழங்கும் 106-வது திருத்தச் சட்டம் மற்றும் 2023 தேர்தல் ஆணையர் நியமனச் சட்டம்), தொழில்நுட்ப புதுமைகள் (தொலைதூர வாக்குப்பதிவு இயந்திரம் RVM, மின்னணு தபால் வாக்கு முறை ETPBS), மற்றும் மக்களாட்சி மாண்பு, வெளிப்படைத்தன்மை மற்றும் கூட்டாட்சியை வலுப்படுத்தும் 'ஒரே நாடு, ஒரே தேர்தல்' போன்ற நிறுவன விவாதங்களை உள்ளடக்கியதாகும்."
            },
            "sec_political_funding_bonds": [
                {
                    "title_en": "Electoral Bonds Scheme (2018): Genesis and Mechanics",
                    "title_ta": "தேர்தல் பத்திரங்கள் திட்டம் (2018): தோற்றம் மற்றும் செயல்முறை",
                    "points": {
                        "en": [
                            "Introduction: Announced in Union Budget 2017 and notified on January 2, 2018 under the Electoral Bond Scheme, 2018 via amendments through the Finance Act, 2017.",
                            "Instrument Character: Promissory notes / bearer instruments payable to the bearer on demand, without carrying the purchaser's name, interest-free, and available in denominations of Rs 1,000, Rs 10,000, Rs 1 Lakh, Rs 10 Lakhs, and Rs 1 Crore.",
                            "Authorized Bank: Exclusively sold through authorized branches of the State Bank of India (SBI) during specified 10-day windows in January, April, July, and October.",
                            "Eligibility: Only political parties registered under Section 29A of RPA 1951 that secured at least 1% of the votes polled in the last general election to Lok Sabha or State Legislative Assembly.",
                            "Validity Period: 15 calendar days from the date of issuance; uncashed bonds within this window were remitted to the Prime Minister's National Relief Fund."
                        ],
                        "ta": [
                            "அறிமுகம்: 2017 மத்திய பட்ஜெட்டில் அறிவிக்கப்பட்டு, 2017 நிதிச் சட்ட திருத்தங்கள் மூலம் 2018 ஜனவரி 2 அன்று தேர்தல் பத்திர திட்டம் 2018 என அறிவிக்கப்பட்டது.",
                            "கருவியின் தன்மை: வாங்குபவரின் பெயர் இல்லாத, வட்டியற்ற, கோரினால் பணம் செலுத்தக்கூடிய கடனுறுதிப் பத்திரங்கள் (Bearer instruments). ரூ.1,000, ரூ.10,000, ரூ.1 லட்சம், ரூ.10 லட்சம், ரூ.1 கோடி ஆகிய மதிப்புகளில் வெளியிடப்பட்டன.",
                            "அங்கீகரிக்கப்பட்ட வங்கி: பாரத ஸ்டேட் வங்கியின் (SBI) குறிப்பிட்ட கிளைகள் மூலம் மட்டுமே ஜனவரி, ஏப்ரல், ஜூலை, அக்டோபர் மாதங்களில் தலா 10 நாட்கள் விற்பனை செய்யப்பட்டன.",
                            "தகுதி: 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 29A-ன் கீழ் பதிவு செய்யப்பட்டு, முந்தைய மக்களவை அல்லது சட்டப்பேரவைத் தேர்தலில் குறைந்தது 1% வாக்குகள் பெற்ற கட்சிகள் மட்டுமே நிதி பெற தகுதியுடையவை.",
                            "செல்லுபடியாகும் காலம்: வழங்கப்பட்ட நாளிலிருந்து 15 நாள்களுக்குள் பணமாக்கப்பட வேண்டும்; தவறினால் அந்த தொகை பிரதமரின் தேசிய நிவாரண நிதிக்குச் சென்றுவிடும்."
                        ]
                    }
                },
                {
                    "title_en": "Landmark Supreme Court Verdict (February 15, 2024): ADR v. Union of India",
                    "title_ta": "வரலாற்றுச் சிறப்புமிக்க உச்சநீதிமன்றத் தீர்ப்பு (பிப்ரவரி 15, 2024): ADR எதிர் இந்திய ஒன்றியம்",
                    "points": {
                        "en": [
                            "Bench Composition: Unanimous 5-judge Constitution Bench headed by CJI D.Y. Chandrachud, alongside Justices Sanjiv Khanna, B.R. Gavai, J.B. Pardiwala, and Manoj Misra.",
                            "Core Constitutional Ruling: Struck down the Electoral Bonds Scheme 2018 and the related Finance Act 2017 amendments as unconstitutional, violating the fundamental 'Right to Information' of voters under Article 19(1)(a).",
                            "Section 29C RPA 1951 Struck Down: The amendment exempting political parties from declaring donations received through electoral bonds to the ECI was invalidated for undermining transparency.",
                            "Companies Act 2013 Section 182 Struck Down: Removed the amendment that eliminated the 7.5% profit cap on corporate donations and allowed loss-making / shell companies to make unlimited political contributions without disclosure.",
                            "Income Tax Act 1961 Section 13A: Invalidation of provisions exempting donor details for electoral bonds.",
                            "SBI Disclosure Directives: SBI was ordered to stop issuance immediately, submit full purchase and redemption details (including unique alphanumeric bond numbers) to ECI by March 2024, and ECI was directed to publish them on its official website."
                        ],
                        "ta": [
                            "அரசியலமைப்பு அமர்வு: தலைமை நீதிபதி டி.ஒய். சந்திரசூட், நீதிபதிகள் சஞ்சீவ் கன்னா, பி.ஆர். கவாய், ஜே.பி. பார்திவாலா, மனோஜ் மிஸ்ரா ஆகியோர் அடங்கிய 5 நீதிபதிகள் கொண்ட ஒருமனதான அமர்வு.",
                            "அடிப்படை தீர்ப்பு: தேர்தல் பத்திரத் திட்டம் மற்றும் 2017 நிதிச் சட்டத் திருத்தங்கள் வாக்காளர்களின் அடிப்படை உரிமையான பிரிவு 19(1)(a)-ன் கீழ் உள்ள 'தகவல் அறியும் உரிமை'யை மீறுவதால் அரசியலமைப்புக்கு முரணானது என ரத்து செய்யப்பட்டது.",
                            "மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 29C: தேர்தல் பத்திரங்கள் மூலம் பெற்ற நிதியை தேர்தல் ஆணையத்திடம் வெளியிட தேவையில்லை என்ற விலக்கு ரத்து செய்யப்பட்டது.",
                            "நிறுவனங்கள் சட்டம் 2013 பிரிவு 182: நிறுவனங்கள் தங்கள் நிகர லாபத்தில் 7.5% மட்டுமே வழங்கலாம் என்ற உச்சவரம்பை நீக்கியது மற்றும் நஷ்டத்தில் இயங்கும் போலி நிறுவனங்கள் வரம்பற்ற நன்கொடை வழங்க அனுமதித்த திருத்தம் ரத்து செய்யப்பட்டது.",
                            "வருமான வரிச் சட்டம் பிரிவு 13A: நன்கொடையாளர் விபரங்களை மறைக்கும் விலக்குகள் ரத்து செய்யப்பட்டன.",
                            "SBI-க்கு உத்தரவு: உடனடியாக விற்பனையை நிறுத்தவும், வாங்கியவர் மற்றும் பணமாக்கிய கட்சியின் முழு விபரங்கள் (தனித்துவமான எண்கள் உட்பட) தேர்தல் ஆணையத்திடம் ஒப்படைக்கவும், ஆணையம் அதை இணையதளத்தில் வெளியிடவும் உத்தரவிட்டது."
                        ]
                    }
                }
            ],
            "sec_electoral_transparency": [
                {
                    "title_en": "Statutory Framework for Political Donations & Cash Limits",
                    "title_ta": "அரசியல் நன்கொடைகளுக்கான சட்டக் கட்டமைப்பு மற்றும் ரொக்க வரம்புகள்",
                    "points": {
                        "en": [
                            "Section 29C of RPA 1951: Political parties must submit an annual Contribution Report to the ECI declaring all donations received in excess of Rs 20,000 from individuals and companies to claim income tax exemption under Section 13A of Income Tax Act, 1961.",
                            "Anonymous Cash Donation Cap: Amended in 2017 to reduce the limit for anonymous cash donations to political parties from Rs 20,000 down to Rs 2,000 per person.",
                            "Audited Annual Accounts: Recognized political parties must submit audited annual financial statements prepared by chartered accountants to the ECI within prescribed timelines.",
                            "Election Expenditure Statements: Parties must lodge separate statements of election expenditure within 75 days (for Assembly elections) and 90 days (for Lok Sabha elections) of completion of polls.",
                            "Electoral Trusts Scheme (2013): Notified by CBDT allowing non-profit companies registered under Section 8 of Companies Act to pool corporate donations and distribute at least 95% of total funds annually to registered political parties via transparent banking channels."
                        ],
                        "ta": [
                            "பிரிவு 29C (RPA 1951): தனிநபர்கள் மற்றும் நிறுவனங்களிடமிருந்து ரூ.20,000-க்கு மேல் பெறப்படும் அனைத்து நன்கொடைகளையும் ஆண்டு பங்களிப்பு அறிக்கையாக தேர்தல் ஆணையத்திடம் சமர்ப்பிக்க வேண்டும்; அப்போதுதான் 1961 வருமான வரிச் சட்டத்தின் பிரிவு 13A-ன் கீழ் வரிவிலக்கு கிடைக்கும்.",
                            "பெயர் குறிப்பிடப்படாத ரொக்க நன்கொடை வரம்பு: 2017 நிதிச் சட்டம் மூலம் பெயர் அறியப்படாத ரொக்க நன்கொடைக்கான வரம்பு ரூ.20,000-லிருந்து நபர் ஒருவருக்கு ரூ.2,000 ஆக குறைக்கப்பட்டது.",
                            "தணிக்கை செய்யப்பட்ட கணக்குகள்: பட்டயக் கணக்காளர்களால் தணிக்கை செய்யப்பட்ட ஆண்டு வரவு-செலவு கணக்குகளை தேர்தல் ஆணையத்திடம் அரசியல் கட்சிகள் குறிப்பிட்ட காலத்திற்குள் சமர்ப்பிக்க வேண்டும்.",
                            "தேர்தல் செலவு அறிக்கைகள்: தேர்தல் முடிந்த 75 நாட்களுக்குள் (சட்டமன்றம்) அல்லது 90 நாட்களுக்குள் (மக்களவை) தேர்தல் செலவு அறிக்கையை தேர்தல் ஆணையத்திடம் கட்சிகள் சமர்ப்பிக்க வேண்டும்.",
                            "தேர்தல் அறக்கட்டளைகள் திட்டம் (2013): நிறுவனங்கள் சட்டம் பிரிவு 8-ன் கீழ் உருவாக்கப்படும் லாப நோக்கற்ற அமைப்புகள் நிறுவன நன்கொடைகளைத் திரட்டி, 95% நிதியை பதிவு செய்யப்பட்ட கட்சிகளுக்கு வெளிப்படையான வங்கி பரிவர்த்தனைகள் மூலம் விநியோகிக்க CBDT வழிவகை செய்தது."
                        ]
                    }
                }
            ],
            "sec_inner_party_democracy": [
                {
                    "title_en": "Concept, Legal Limitations & Reform Imperatives",
                    "title_ta": "கருத்து, சட்டக் குறைபாடுகள் மற்றும் சீர்திருத்தத் தேவைகள்",
                    "points": {
                        "en": [
                            "Meaning: The practice of democratic governance, periodic internal elections, decentralized ticket distribution, and financial transparency within political party organizations.",
                            "Current Legal Basis: Section 29A(5) of RPA 1951 requires every association applying for registration as a political party to bear true faith and allegiance to the Constitution of India and principles of socialism, secularism, and democracy.",
                            "Judicial Limitation (INC v. Institute of Social Welfare, 2002): The Supreme Court held that the ECI does NOT possess statutory power under Section 29A to de-register a political party for violating inner-party democracy or constitutional principles, except under 3 narrow exceptions: (a) registration obtained by fraud, (b) party declared unlawful by central government, or (c) party amends constitution declaring it has ceased to follow the Indian Constitution.",
                            "170th Law Commission (1999) & 255th Report (2015): Recommended introducing a specific Part in RPA 1951 mandating regular, transparent internal organizational elections supervised by the ECI, with non-compliance leading to derecognition.",
                            "Dinesh Goswami Committee & 2nd ARC: Emphasized that political parties are constitutional instruments of democracy and cannot operate as private feudal fiefdoms."
                        ],
                        "ta": [
                            "பொருள்: அரசியல் கட்சிகளின் அமைப்புக்குள் ஜனநாயகக் கொள்கைகள், குறிப்பிட்ட கால இடைவெளியிலான உட்கட்சித் தேர்தல்கள், வெளிப்படையான வேட்பாளர் தேர்வு மற்றும் நிதி வெளிப்படைத்தன்மையை நடைமுறைப்படுத்துதல்.",
                            "தற்போதைய சட்ட நிலை: 1951 மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 29A(5)-ன் படி, பதிவு செய்யும் கட்சி இந்திய அரசியலமைப்பு, சோசலிசம், மதச்சார்பின்மை மற்றும் ஜனநாயகத்தின் மீது உண்மையான நம்பிக்கை கொண்டிருக்க உறுதிமொழி அளிக்க வேண்டும்.",
                            "உச்சநீதிமன்ற வரம்பு (INC எதிர் இன்ஸ்டிடியூட் ஆஃப் சோஷியல் வெல்ஃபேர், 2002): உட்கட்சித் தேர்தல் நடத்தாததற்காக அல்லது அரசியலமைப்பு விதிகளை மீறியதற்காக ஒரு கட்சியின் பதிவை ரத்து செய்யும் அதிகாரம் தேர்தல் ஆணையத்திற்கு இல்லை என உச்சநீதிமன்றம் தீர்ப்பளித்தது (3 விதிவிலக்குகள் தவிர: மோசடி பதிவு, மத்திய அரசால் தடை, கட்சியாக செயல்பட மறுப்பு).",
                            "சட்ட ஆணையப் பரிந்துரைகள் (170 மற்றும் 255-வது அறிக்கைகள்): தேர்தல் ஆணையத்தின் மேற்பார்வையில் கட்டாய உட்கட்சித் தேர்தல்களை நடத்துவதை சட்டப்பூர்வமாக்க RPA-வில் தனிப்பிரிவை சேர்க்கப் பரிந்துரைத்தன.",
                            "2-வது நிர்வாகச் சீர்திருத்த ஆணையம்: ஜனநாயகத்தின் அடித்தளமாக விளங்கும் அரசியல் கட்சிகள் தனிநபர் குடும்ப சொத்தாக அல்லது பிரபுத்துவ அமைப்புகளாக இயங்க முடியாது என வலியுறுத்தியது."
                        ]
                    }
                }
            ],
            "sec_simultaneous_elections": [
                {
                    "title_en": "Simultaneous Elections (One Nation, One Election) — History & Rationale",
                    "title_ta": "ஒரே நாடு, ஒரே தேர்தல் (ONOE) — வரலாறு மற்றும் அடிப்படை காரணங்கள்",
                    "points": {
                        "en": [
                            "Historical Context: Simultaneous elections were the norm in India during the first four general elections: 1952, 1957, 1962, and 1967.",
                            "Breakdown of Cycle: The cycle broke down due to premature dissolution of some State Legislative Assemblies under Article 356 (President's Rule) in 1968–1969 and the premature dissolution of the 4th Lok Sabha in 1970.",
                            "Arguments in Favour: (a) Substantial reduction in massive election expenditure incurred by government and candidates; (b) Prevention of policy paralysis caused by frequent imposition of Model Code of Conduct (MCC); (c) Uninterrupted administrative and security personnel deployment for core governance; (d) Reduction of voter fatigue and higher electoral turnout.",
                            "Arguments Against: (a) Threat to Federalism — national issues may overshadow vital regional and local concerns; (b) Premature dissolution conundrum — if a government falls mid-term via no-confidence, the synchronization collapses; (c) Massive initial demand for EVMs, VVPATs, and central armed police forces (CAPF); (d) May disadvantage smaller regional parties in multi-tier campaigns."
                        ],
                        "ta": [
                            "வரலாற்றுப் பின்னணி: சுதந்திர இந்தியாவில் முதல் நான்கு பொதுத்தேர்தல்கள் (1952, 1957, 1962 மற்றும் 1967) மக்களவைக்கும் மாநில சட்டமன்றங்களுக்கும் ஒரே நேரத்திலேயே நடைபெற்றன.",
                            "சுழற்சி முறிவு: 1968-1969ல் சில மாநிலங்களில் பிரிவு 356 (குடியரசுத் தலைவர் ஆட்சி) அமல்படுத்தப்பட்டு முன்கூட்டியே கலைக்கப்பட்டதாலும், 1970ல் 4-வது மக்களவை முன்கூட்டியே கலைக்கப்பட்டதாலும் இந்த சுழற்சி சிதைந்தது.",
                            "ஆதரவு வாதங்கள்: (அ) தேர்தல் செலவுகள் பெருமளவில் குறையும்; (ஆ) மாதிரி நடத்தை விதி (MCC) அடிக்கடி அமலாவதால் ஏற்படும் நிர்வாக முடக்கம் தவிர்க்கப்படும்; (இ) பாதுகாப்புப் படைகள் மற்றும் அரசு ஊழியர்கள் தொடர்ந்து தேர்தல் பணியில் ஈடுபடுவது தடுக்கப்பட்டு அரசுப் பணிகள் தடையின்றி நடக்கும்; (ஈ) வாக்காளர் சோர்வு நீங்கி வாக்குப்பதிவு அதிகரிக்கும்.",
                            "எதிர்ப்பு வாதங்கள்: (அ) கூட்டாட்சி தத்துவத்திற்கு அச்சுறுத்தல் — தேசிய விவகாரங்கள் மாநில அளவிலான முக்கிய பிரச்சனைகளை மறைத்துவிடும் அபாயம்; (ஆ) இடையில் ஆட்சி கவிழ்ந்தால் (நம்பிக்கையில்லா தீர்மானம்) மீண்டும் சுழற்சி பாதிக்கப்படும்; (இ) ஒரே நேரத்தில் லட்சக்கணக்கான EVM, VVPAT மற்றும் துணை ராணுவப் படைகள் தேவைப்படும்; (ஈ) சிறிய மாநிலக் கட்சிகள் வளப்பற்றாக்குறையால் பாதிக்கப்படலாம்."
                        ]
                    }
                },
                {
                    "title_en": "High-Level Committee on Simultaneous Elections (Kovind Committee 2024)",
                    "title_ta": "ஒரே தேர்தல் தொடர்பான உயர்நிலைக் குழு (கோவிந்த் குழு 2024)",
                    "points": {
                        "en": [
                            "Constitution & Leadership: Constituted in September 2023 under the chairmanship of former President of India Ram Nath Kovind; submitted its comprehensive 18,626-page report on March 14, 2024.",
                            "Two-Step Implementation Formula: (1) Step 1: Synchronize elections to Lok Sabha and all State Legislative Assemblies simultaneously. (2) Step 2: Synchronize local body elections (Panchayats and Municipalities) with Lok Sabha and Assemblies within 100 days of the first step.",
                            "Appointed Date Mechanism: Recommends introducing Article 82A; the President issues an 'Appointed Date' following a general election to Lok Sabha. All Legislative Assemblies elected after this date will have an unexpired term that ends automatically with the dissolution of Lok Sabha.",
                            "Constitutional Amendments: Amending Article 83 (Duration of Houses of Parliament), Article 85 (Dissolution of Lok Sabha), Article 172 (Duration of State Legislatures), Article 174 (Dissolution of Assemblies), and Article 356.",
                            "State Ratification Requirement: Step 1 (LS + Assemblies) does not alter federal balance and can be passed by Parliament under Article 368(2) without state ratification; Step 2 (Municipalities & Panchayats under Art 324A/325) touches Entry 5 of State List and requires ratification by not less than half the States.",
                            "Single Electoral Roll: Proposed Article 325 amendment enabling ECI in consultation with SECs to prepare a single unified electoral roll and voter ID card across all three tiers."
                        ],
                        "ta": [
                            "அமைப்பு மற்றும் தலைமை: முன்னாள் குடியரசுத் தலைவர் ராம் நாத் கோவிந்த் தலைமையில் செப்டம்பர் 2023-ல் அமைக்கப்பட்டு, மார்ச் 14, 2024 அன்று தனது விரிவான அறிக்கையை சமர்ப்பித்தது.",
                            "இரு-படிநிலை அமலாக்க முறை: (1) படிநிலை 1: மக்களவை மற்றும் அனைத்து மாநில சட்டப்பேரவைகளுக்கான தேர்தல்களை ஒரே நேரத்தில் நடத்துதல். (2) படிநிலை 2: மக்களவை தேர்தல் முடிந்த 100 நாட்களுக்குள் உள்ளாட்சி அமைப்புகளுக்கான (பஞ்சாயத்து & நகராட்சி) தேர்தல்களை ஒருங்கிணைத்தல்.",
                            "குறிப்பிடப்பட்ட நாள் (Appointed Date): புதிய பிரிவு 82A-ஐ பரிந்துரைத்தது; குடியரசுத் தலைவர் அறிவிக்கும் நாளுக்குப் பின் அமையும் சட்டமன்றங்களின் ஆயுட்காலம் மக்களவையின் ஆயுட்காலத்தோடு தானாகவே முடிவுக்கு வரும்.",
                            "தேவையான அரசியலமைப்பு திருத்தங்கள்: பிரிவு 83 (நாடாளுமன்றத்தின் ஆயுள்), பிரிவு 85 (மக்களவை கலைப்பு), பிரிவு 172 (சட்டமன்றங்களின் ஆயுள்), பிரிவு 174 (சட்டமன்ற கலைப்பு) மற்றும் பிரிவு 356.",
                            "மாநிலங்களின் ஏற்புரை: மக்களவை மற்றும் சட்டமன்றங்களுக்கான படிநிலை 1-க்கு மாநிலங்களின் ஒப்புதல் தேவையில்லை; ஆனால் உள்ளாட்சித் தேர்தல்களுக்கான படிநிலை 2-க்கு குறைந்தது பாதி மாநிலங்களின் சட்டமன்ற ஒப்புதல் (பிரிவு 368(2)) கட்டாயம்.",
                            "ஒற்றை வாக்காளர் பட்டியல்: பிரிவு 325-ல் திருத்தம் செய்து, மூன்று அடுக்கு தேர்தல்களுக்கும் ஒரே ஒருங்கிணைந்த வாக்காளர் பட்டியலை தேர்தல் ஆணையம் மாநில தேர்தல் ஆணையங்களுடன் இணைந்து தயாரித்தல்."
                        ]
                    }
                }
            ],
            "sec_remote_voting_migrants": [
                {
                    "title_en": "Remote Voting for Domestic Migrants (RVM Framework)",
                    "title_ta": "உள்நாட்டு புலம்பெயர்ந்தோருக்கான தொலைதூர வாக்குப்பதிவு (RVM கட்டமைப்பு)",
                    "points": {
                        "en": [
                            "Background & Problem: Census 2011 figures indicate over 45 crore domestic migrants in India. In the 2019 Lok Sabha elections, nearly 30 crore eligible voters (~32.6%) did not cast their vote, with domestic migration being a prime factor.",
                            "Prototype RVM (December 2022): ECI in collaboration with Bharat Electronics Limited (BEL) and Electronics Corporation of India Limited (ECIL) developed a prototype Remote Electronic Voting Machine (RVM).",
                            "Multi-Constituency Capacity: A single RVM unit at a designated remote polling station can handle up to 72 distinct constituencies simultaneously using dynamic digital ballot display screens.",
                            "Legal & Logistical Challenges: Defining 'domestic migrant', territorial jurisdiction of polling agents, remote counting, and political parties raising apprehensions regarding technical audit and transparency.",
                            "Current Status: ECI demonstrated the prototype to recognized political parties in January 2023; wide-scale deployment is currently on hold pending broader political consensus and statutory amendments to the Conduct of Elections Rules, 1961."
                        ],
                        "ta": [
                            "பின்னணி மற்றும் பிரச்சனை: 2011 மக்கள்தொகை கணக்கெடுப்பின்படி இந்தியாவில் 45 கோடிக்கும் அதிகமான உள்நாட்டு புலம்பெயர்ந்தோர் உள்ளனர். 2019 மக்களவைத் தேர்தலில் சுமார் 30 கோடி வாக்காளர்கள் (32.6%) வாக்களிக்கவில்லை, இதற்கு புலம்பெயர்வே முதன்மைக் காரணம்.",
                            "RVM முன்மாதிரி (டிசம்பர் 2022): தேர்தல் ஆணையம் BEL மற்றும் ECIL நிறுவனங்களுடன் இணைந்து தொலைதூர வாக்குப்பதிவு இயந்திர (RVM) முன்மாதிரியை உருவாக்கியது.",
                            "பல தொகுதிகளைக் கையாளும் திறன்: ஒரு தொலைதூர வாக்குச்சாவடியில் வைக்கப்படும் ஒரு RVM இயந்திரம், ஒரே நேரத்தில் 72 வெவ்வேறு தொகுதிகளின் வாக்குகளை மின்னணு திரை மூலம் பதிவு செய்யும் திறன் கொண்டது.",
                            "சட்ட மற்றும் நிர்வாக சவால்கள்: புலம்பெயர்ந்தோரை வரையறுத்தல், வாக்குச்சாவடி முகவர்களின் அதிகார வரம்பு, தொலைதூர வாக்கு எண்ணிக்கை மற்றும் கட்சிகள் எழுப்பிய நம்பகத்தன்மை கேள்விகள்.",
                            "தற்போதைய நிலை: 2023 ஜனவரியில் அனைத்து கட்சிகளுக்கும் செயல்விளக்கம் அளிக்கப்பட்டது; அரசியல் கட்சிகளின் ஒருமித்த கருத்து மற்றும் தேர்தல் நடத்தை விதிகளில் (1961) சட்டத் திருத்தங்கள் நிலுவையில் உள்ளதால் இதன் அமலாக்கம் ஒத்திவைக்கப்பட்டுள்ளது."
                        ]
                    }
                }
            ],
            "sec_postal_ballots_accessibility": [
                {
                    "title_en": "Modernization of Postal Ballots, ETPBS & Home Voting",
                    "title_ta": "தபால் வாக்குகள் நவீனமயமாக்கல், ETPBS மற்றும் இல்ல வாக்குப்பதிவு",
                    "points": {
                        "en": [
                            "Governing Provision: Section 60 of the Representation of the People Act, 1951 empowers special classes of voters to vote by postal ballot or proxy.",
                            "Electronically Transmitted Postal Ballot System (ETPBS): Fully rolled out in 2016 for Service Voters (armed forces, state police personnel serving outside state, and diplomatic staff posted abroad). Ballots are transmitted securely electronically and returned via physical post with encrypted QR codes.",
                            "Home Voting for Senior Citizens & PwD: ECI amended the Conduct of Elections Rules, 1961 to provide postal ballot voting at home via Form 12D for Persons with Disabilities (40%+ certified benchmark disability) and senior citizens.",
                            "Age Threshold Revision (March 2024): The Union Ministry of Law & Justice amended the rules in March 2024 to revise the eligibility age for senior citizens from 80 years to 85 years and above.",
                            "Integrity Safeguards: Voting at home is conducted by a two-member polling team accompanied by a micro-observer and videographer, after prior notification to candidates who may depute polling agents to observe."
                        ],
                        "ta": [
                            "சட்டப்பிரிவு: 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 60 குறிப்பிட்ட தகுதிபெற்ற வாக்காளர்களுக்கு தபால் வாக்கு அல்லது மாற்று வாக்கு (Proxy) அளிக்க உரிமை வழங்குகிறது.",
                            "ETPBS முறை: 2016-ல் பாதுகாப்புப் படை வீரர்கள், வெளிமாநிலத்தில் பணியாற்றும் ஆயுதப்படை மற்றும் வெளிநாட்டு தூதரக அதிகாரிகளுக்காக முழுமையாக அமல்படுத்தப்பட்டது. மின்னணு முறையில் தபால் வாக்குகள் அனுப்பப்பட்டு, QR குறியீட்டுடன் அஞ்சல் வழியாக திரும்பப் பெறப்படுகின்றன.",
                            "மூத்த குடிமக்கள் & மாற்றுத்திறனாளிகள் இல்ல வாக்களிப்பு: தேர்தல் நடத்தை விதிகளில் திருத்தம் செய்யப்பட்டு, படிவம் 12D மூலம் 40% மாற்றுத்திறனாளிகள் மற்றும் முதியவர்கள் வீட்டிலிருந்தே வாக்களிக்கும் வசதி ஏற்படுத்தப்பட்டது.",
                            "வயது வரம்பு மாற்றம் (மார்ச் 2024): சட்ட அமைச்சகம் தேர்தல் நடத்தை விதிகளில் திருத்தம் செய்து, முதியவர்களுக்கான இல்ல வாக்குப்பதிவு தகுதி வயதை 80-லிருந்து 85 வயதாக உயர்த்தியது.",
                            "பாதுகாப்பு ஏற்பாடுகள்: இரண்டு தேர்தல் அலுவலர்கள், ஒரு நுண் பார்வையாளர் மற்றும் வீடியோகிராபர் முன்னிலையில் வேட்பாளர்களின் முகவர்கள் முன்னிலையில் முழுமையான ரகசியத்தன்மையுடன் இல்ல வாக்களிப்பு பதிவு செய்யப்படுகிறது."
                        ]
                    }
                }
            ],
            "sec_women_representation_106th": [
                {
                    "title_en": "106th Constitutional Amendment Act, 2023 (Nari Shakti Vandan Adhiniyam)",
                    "title_ta": "106-வது அரசியலமைப்பு திருத்தச் சட்டம், 2023 (நாரி சக்தி வந்தன் அதினியம்)",
                    "points": {
                        "en": [
                            "Legislative Passage: Introduced as the Constitution (128th Amendment) Bill, 2023 in the Special Session of Parliament; unanimously/near-unanimously passed and received Presidential assent on September 28, 2023 to become the 106th Constitutional Amendment Act.",
                            "Article 330A (Reservation in Lok Sabha): Reserves one-third (33%) of the total seats in the House of the People (Lok Sabha) for women, including one-third of seats reserved for SCs and STs.",
                            "Article 332A (Reservation in State Assemblies): Reserves one-third (33%) of all seats in every State Legislative Assembly for women, including one-third of SC/ST reserved seats.",
                            "Article 239AA Amendment: Extends one-third reservation for women to the Legislative Assembly of the National Capital Territory (NCT) of Delhi.",
                            "Article 334A (Sunset Clause & Delimitation Linkage): The reservation will take effect only AFTER an exercise of delimitation is undertaken based on the relevant figures of the first Census conducted after the commencement of the 2023 Act. The reservation is granted for a duration of 15 years, with seats rotated after every subsequent delimitation."
                        ],
                        "ta": [
                            "சட்டத்தின் தோற்றம்: 2023 நாடாளுமன்ற சிறப்பு கூட்டத்தொடரில் 128-வது அரசியலமைப்பு திருத்த மசோதாவாக அறிமுகப்படுத்தப்பட்டு, இரு அவைகளிலும் நிறைவேற்றப்பட்டு 2023 செப்டம்பர் 28 அன்று குடியரசுத் தலைவர் ஒப்புதல் பெற்று 106-வது திருத்தச் சட்டமாக மாறியது.",
                            "பிரிவு 330A (மக்களவையில் இடஒதுக்கீடு): மக்களவையில் மொத்த இடங்களில் மூன்றில் ஒரு பங்கு (33%) பெண்களுக்கு இடஒதுக்கீடு செய்யப்படுகிறது (SC/ST பிரிவினருக்கான இடங்களில் மூன்றில் ஒரு பங்கு உட்பட).",
                            "பிரிவு 332A (சட்டமன்றங்களில் இடஒதுக்கீடு): அனைத்து மாநில சட்டப்பேரவைகளிலும் மொத்த இடங்களில் 33% இடங்கள் பெண்களுக்கு ஒதுக்கப்படுகிறது.",
                            "பிரிவு 239AA திருத்தம்: டெல்லி தேசிய தலைநகர் பிரதேச சட்டமன்றத்திலும் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்கப்படுகிறது.",
                            "பிரிவு 334A (செயல்பாட்டு நிபந்தனை & காலாவதி): இந்த இடஒதுக்கீடு சட்டம் நடைமுறைக்கு வந்தபின் எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பு மற்றும் அதன் அடிப்படையிலான தொகுதி மறுவரையறைக்கு (Delimitation) பிறகே நடைமுறைக்கு வரும். இதன் ஆயுட்காலம் 15 ஆண்டுகள் ஆகும்; ஒவ்வொரு தொகுதி மறுவரையறைக்குப் பிறகும் சுழற்சி முறையில் தொகுதிகள் மாற்றப்படும்."
                        ]
                    }
                }
            ],
            "sec_criminalisation_further_reforms": [
                {
                    "title_en": "Judicial Escalation against Criminalisation of Politics",
                    "title_ta": "அரசியல் குற்றமயமாதலுக்கு எதிரான நீதித்துறை தீவிர நடவடிக்கைகள்",
                    "points": {
                        "en": [
                            "Public Interest Foundation v. UOI (2018): 5-judge Constitution Bench directed that candidates and political parties must widely publicize criminal antecedents in newspapers, official websites, and television channels at least 3 times during campaign.",
                            "Rambabu Singh Thakur v. Sunil Arora (2020): SC mandated that political parties must publish details of candidates with criminal cases within 48 hours of candidate selection or at least 2 weeks before the first date for filing nominations, along with specific reasons explaining why individuals without criminal records could not be selected.",
                            "Brajesh Singh v. Sunil Arora (2021): SC imposed heavy financial penalties on major political parties (including BJP, Congress, CPI(M)) for contempt of court regarding non-compliance with candidate disclosure mandates.",
                            "Ashwini Kumar Upadhyay v. UOI: Supreme Court monitored the setup of Special Fast-Track Courts across states for expedited trial of criminal cases against sitting and former MPs/MLAs, prohibiting withdrawal of prosecution without High Court sanction.",
                            "Law Commission 244th Report Recommendation: Recommended debarring candidates from contesting elections upon framing of charges by a competent court for heinous offences punishable by 5 years imprisonment or more, provided charges are framed at least one year before elections."
                        ],
                        "ta": [
                            "பப்ளிக் இன்ட்ரஸ்ட் ஃபவுண்டேஷன் வழக்கு (2018): வேட்பாளர்கள் மற்றும் அரசியல் கட்சிகள் வேட்பாளர்களின் குற்றப்பின்னணியை பிரச்சார காலத்தில் செய்தித்தாள்கள், இணையதளம் மற்றும் தொலைக்காட்சிகளில் குறைந்தது 3 முறை விளம்பரம் செய்ய வேண்டும் என 5 நீதிபதிகள் அமர்வு உத்தரவிட்டது.",
                            "ராம்பாபு சிங் தாக்கூர் எதிர் சுனில் அரோரா (2020): வேட்பாளர் தேர்வு செய்யப்பட்ட 48 மணி நேரத்திற்குள் குற்றப்பின்னணி கொண்டவர்களை தேர்வு செய்ததற்கான குறிப்பிட்ட காரணங்களையும், குற்றப்பின்னணி இல்லாதவர்களை ஏன் தேர்வு செய்யவில்லை என்பதையும் கட்சிகள் ஊடகங்களில் வெளியிட வேண்டும் என உத்தரவிட்டது.",
                            "பிரிஜேஷ் சிங் வழக்கு (2021): உச்சநீதிமன்ற வழிகாட்டுதல்களைப் பின்பற்றாத முக்கிய அரசியல் கட்சிகளுக்கு நீதிமன்ற அவமதிப்பு தண்டனையாக அபராதம் விதித்து உச்சநீதிமன்றம் கண்டித்தது.",
                            "அஸ்வினி குமார் உபத்யாய வழக்கு: நாடாளுமன்ற மற்றும் சட்டமன்ற உறுப்பினர்கள் மீதான குற்ற வழக்குகளை விரைந்து முடிக்க சிறப்பு விரைவு நீதிமன்றங்களை அமைக்க உச்சநீதிமன்றம் உத்தரவிட்டது; உயர்நீதிமன்ற அனுமதியின்றி வழக்குகளை திரும்பப் பெறத் தடை விதித்தது.",
                            "சட்ட ஆணையத்தின் 244-வது அறிக்கை: 5 ஆண்டுகளுக்கு மேல் சிறை தண்டனைக்குரிய கொடிய குற்றங்களில், நீதிமன்றத்தால் குற்றச்சாட்டுகள் பதிவு செய்யப்பட்ட (Framing of charges) நபர்களை தேர்தலில் போட்டியிட தகுதிநீக்கம் செய்ய பரிந்துரைத்தது."
                        ]
                    }
                }
            ],
            "sec_eci_independence_appointment": [
                {
                    "title_en": "Evolution of ECI Appointment: From Anoop Baranwal to 2023 Act",
                    "title_ta": "தேர்தல் ஆணையர் நியமன பரிணாமம்: அனூப் பரன்வால் முதல் 2023 சட்டம் வரை",
                    "points": {
                        "en": [
                            "Constitutional Lacuna: Under Article 324(2), the President appointed the CEC and other Election Commissioners subject to any law made by Parliament. For over 73 years, no law was enacted, leaving appointments to the sole discretion of the Union Executive.",
                            "Anoop Baranwal v. Union of India (March 2, 2023): A unanimous 5-judge Constitution Bench held that a fiercely independent ECI is essential to the basic structure of the Constitution. It directed that until Parliament enacted a law, CEC and ECs must be appointed by the President on the advice of a 3-member Selection Committee: (1) Prime Minister, (2) Leader of Opposition in Lok Sabha (or leader of largest opposition party), and (3) Chief Justice of India (CJI).",
                            "Chief Election Commissioner and other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023: Passed by Parliament in December 2023, replacing the Supreme Court's interim arrangement.",
                            "Statutory Appointment Mechanism under 2023 Act: (a) Search Committee: Headed by Minister of Law and Justice, consisting of two other members not below rank of Secretary to Government of India, shortlists 5 candidates; (b) Selection Committee: Comprises the Prime Minister (Chairperson), Leader of Opposition / single largest opposition party leader in Lok Sabha, and a Union Cabinet Minister nominated by the PM.",
                            "Controversy & Legal Challenge: The exclusion of the Chief Justice of India (CJI) and substituting with a Cabinet Minister gave the Executive an automatic 2:1 majority, leading to petitions in the Supreme Court challenging the Act as violative of free, fair elections and institutional autonomy."
                        ],
                        "ta": [
                            "அரசியலமைப்பு இடைவெளி: பிரிவு 324(2)-ன் படி, நாடாளுமன்ற சட்டம் இயற்றும் வரை தலைமை தேர்தல் ஆணையர் மற்றும் பிற ஆணையர்களை குடியரசுத் தலைவர் நியமிப்பார் எனக் கூறப்பட்டிருந்தது. 73 ஆண்டுகளாக சட்டம் இயற்றப்படாததால் மத்திய அமைச்சரவையே முழுமையாக நியமித்து வந்தது.",
                            "அனூப் பரன்வால் வழக்கு (மார்ச் 2, 2023): சுதந்திரமான தேர்தல் ஆணையமே அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பு என 5 நீதிபதிகள் அமர்வு தீர்ப்பளித்தது. நாடாளுமன்ற சட்டம் இயற்றும் வரை: (1) பிரதமர், (2) மக்களவை எதிர்க்கட்சித் தலைவர் மற்றும் (3) உச்சநீதிமன்ற தலைமை நீதிபதி (CJI) அடங்கிய 3 நபர் குழுவின் பரிந்துரைப்படியே நியமனம் செய்ய வேண்டும் என உத்தரவிட்டது.",
                            "தலைமை தேர்தல் ஆணையர் மற்றும் பிற ஆணையர்கள் நியமனச் சட்டம் 2023: உச்சநீதிமன்றத்தின் தற்காலிக உத்தரவை மாற்றி டிசம்பர் 2023-ல் நாடாளுமன்றத்தால் இந்த புதிய சட்டம் இயற்றப்பட்டது.",
                            "2023 சட்டத்தின் கீழ் நியமனக் குழு: (அ) தேடுதல் குழு: மத்திய சட்ட அமைச்சர் தலைமையில் 5 பெயர்களைப் பரிந்துரைக்கும்; (ஆ) தேர்வுக் குழு: பிரதமர் (தலைவர்), மக்களவை எதிர்க்கட்சித் தலைவர் மற்றும் பிரதமரால் நியமிக்கப்படும் ஒரு மத்திய அமைச்சரவை அமைச்சர்.",
                            "சர்ச்சை மற்றும் வழக்குகள்: உச்சநீதிமன்ற தலைமை நீதிபதியை நீக்கிவிட்டு மத்திய அமைச்சரை சேர்த்ததன் மூலம் அரசுக்கு 2:1 என்ற பெரும்பான்மை கிடைப்பதால், தேர்தல் ஆணையத்தின் தன்னாட்சி பாதிக்கப்படுவதாகக் கூறி உச்சநீதிமன்றத்தில் வழக்குகள் தொடரப்பட்டன."
                        ]
                    }
                }
            ],
            "sec_landmark_sc_judgments": [
                {
                    "title_en": "Chronological Master Table of Landmark Supreme Court Judgments",
                    "title_ta": "தேர்தல் சீர்திருத்த வரலாற்று உச்சநீதிமன்றத் தீர்ப்புகளின் முழுமையான அட்டவணை",
                    "points": {
                        "en": [
                            "Mohinder Singh Gill v. CEC (1978): Ruled that Article 324 is a reservoir of vast plenary powers enabling ECI to act in the absence of legislation to ensure free and fair elections.",
                            "S.S. Dhanoa v. UOI (1991) & T.N. Seshan v. UOI (1995): Established that Election Commissioners are on par in power with the CEC; decisions in multi-member ECI must be taken by consensus or majority.",
                            "Union of India v. ADR (2002) & PUCL v. UOI (2003): Declared that the voter's right to know candidate antecedents is a fundamental right under Article 19(1)(a); mandated Form 26 affidavits for assets, liabilities, education, and criminal cases.",
                            "Lily Thomas v. UOI (2013): Struck down Section 8(4) of RPA 1951 as unconstitutional, establishing instantaneous disqualification of convicted MPs/MLAs sentenced to 2+ years imprisonment without the 3-month protection window.",
                            "PUCL v. UOI (2013 - NOTA): Directed introduction of 'None of the Above' (NOTA) on EVMs under Article 19(1)(a) to protect voter secrecy and register dissatisfaction.",
                            "Subramanian Swamy v. ECI (2013 - VVPAT): Ruled that a paper trail via VVPAT is indispensable for free and fair elections and transparency in electronic voting.",
                            "Abhiram Singh v. C.D. Commachen (2017): 7-judge Constitution Bench held that appealing to religion, race, caste, community or language of the candidate, rival, OR electors constitutes a corrupt practice under Section 123(3) of RPA 1951.",
                            "ADR v. UOI (Feb 15, 2024 - Electoral Bonds): 5-judge Constitution bench struck down Electoral Bonds Scheme as violative of Article 19(1)(a); ordered full public disclosure of transactions.",
                            "ADR v. ECI (April 26, 2024 - VVPAT Verification): Dismissed plea for 100% VVPAT counting; upheld sanctity of EVMs but allowed candidates securing 2nd and 3rd positions to request 5% EVM micro-controller verification post-results."
                        ],
                        "ta": [
                            "மொஹிந்தர் சிங் கில் வழக்கு (1978): சட்டங்கள் மௌனமாக இருக்கும் சூழலில் நியாயமான தேர்தலை நடத்த பிரிவு 324 தேர்தல் ஆணையத்திற்கு எல்லையற்ற முழு அதிகாரத்தை வழங்குகிறது எனத் தீர்ப்பளித்தது.",
                            "எஸ்.எஸ். தனோவா (1991) & டி.என். சேஷன் (1995): தலைமை தேர்தல் ஆணையரும் பிற ஆணையர்களும் சம அதிகாரமுடையவர்கள்; முடிவுகள் பெரும்பான்மை அடிப்படையிலேயே எடுக்கப்பட வேண்டும் என உறுதிப்படுத்தியது.",
                            "ADR வழக்கு (2002) & PUCL வழக்கு (2003): வேட்பாளர்களின் சொத்து, கல்வி, குற்றப்பின்னணியை அறியும் உரிமை பிரிவு 19(1)(a)-ன் கீழ் வாக்காளர்களின் அடிப்படை உரிமை என அறிவித்தது.",
                            "லில்லி தாமஸ் வழக்கு (2013): 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 8(4)-ஐ ரத்து செய்து, 2 ஆண்டுகளுக்கு மேல் சிறை தண்டனை பெற்ற நாடாளுமன்ற/சட்டமன்ற உறுப்பினர்கள் உடனடியாக தகுதிநீக்கம் செய்யப்படுவர் எனத் தீர்ப்பளித்தது.",
                            "PUCL வழக்கு (2013 - NOTA): வாக்காளர்களின் ரகசியத்தன்மையைப் பாதுகாக்கவும் அதிருப்தியைப் பதிவு செய்யவும் வாக்குப்பதிவு இயந்திரங்களில் நோட்டா (NOTA) பொத்தானை அறிமுகப்படுத்த உத்தரவிட்டது.",
                            "சுப்பிரமணியன் சுவாமி வழக்கு (2013 - VVPAT): மின்னணு வாக்குப்பதிவில் முழுமையான வெளிப்படைத்தன்மையை உறுதி செய்ய VVPAT காகித ரசீது முறை இன்றியமையாதது என தீர்ப்பளித்தது.",
                            "அபிராம் சிங் வழக்கு (2017): மதம், இனம், சாதி அல்லது மொழியின் பெயரால் வாக்கு சேகரிப்பது ஊழல் நடைமுறை (Corrupt Practice) என 7 நீதிபதிகள் அமர்வு தீர்ப்பளித்தது.",
                            "ADR தேர்தல் பத்திர வழக்கு (2024): தேர்தல் பத்திர திட்டத்தை ரத்து செய்து, வெளிப்படைத்தன்மை மற்றும் தகவல் அறியும் உரிமையை நிலைநாட்டியது.",
                            "ADR VVPAT சரிபார்ப்பு வழக்கு (ஏப்ரல் 26, 2024): 100% VVPAT தாள்களை எண்ணும் கோரிக்கையை நிராகரித்து, EVM பாதுகாப்பானது என உறுதிசெய்தது; ஆனால் 2 மற்றும் 3-ம் இடம் பெற்ற வேட்பாளர்கள் கோரினால் 5% இயந்திரங்களின் மென்பொருளை சரிபார்க்க அனுமதித்தது."
                        ]
                    }
                }
            ],
            "sec_challenges_way_forward": [
                {
                    "title_en": "Major Structural Challenges in Indian Electoral Architecture",
                    "title_ta": "இந்திய தேர்தல் கட்டமைப்பில் உள்ள முக்கிய கட்டமைப்பு சவால்கள்",
                    "points": {
                        "en": [
                            "Rampant Misuse of Money Power: Astronomical underground expenditures, cash distributions, and freebies for votes that escape formal expenditure ceilings.",
                            "Criminal-Political Nexus: Moneyed winnability prioritized by political parties over clean public service credentials, leading to rising percentage of lawmakers with pending criminal cases.",
                            "Information Ecosystem & Deepfakes: Rapid spread of AI-generated synthetic media, deepfakes, disinformation, and coordinated micro-targeted digital propaganda during election cycles.",
                            "Misuse of Official Machinery: Allegations of partisan bias in scheduling phases, unequal enforcement of MCC restrictions, and selective scrutiny of opposition campaigns.",
                            "Post-2026 Delimitation Dilemma: Severe federal friction between northern states with rapid population growth and southern states that successfully implemented family welfare policies."
                        ],
                        "ta": [
                            "பணபலத்தின் கடுமையான ஆதிக்கம்: சட்டப்பூர்வ தேர்தல் செலவு வரம்புகளைத் தாண்டி வாக்காளர்களுக்கு பணம், பரிசுப் பொருட்கள் விநியோகம் செய்யப்படுவது.",
                            "அரசியல்-குற்றக் கூட்டணி: வெற்றி வாய்ப்பை மட்டுமே கருதி குற்றப்பின்னணி கொண்ட பணக்கார வேட்பாளர்களுக்கு அரசியல் கட்சிகள் வாய்ப்பளிப்பது.",
                            "செயற்கை நுண்ணறிவு & போலிச் செய்திகள்: AI மூலம் உருவாக்கப்படும் போலி வீடியோக்கள் (Deepfakes) மற்றும் சமூக ஊடகங்கள் மூலமான திட்டமிட்ட பிரச்சாரங்கள்.",
                            "அதிகார துஷ்பிரயோகம்: மாதிரி நடத்தை விதியை பாரபட்சமாக செயல்படுத்துதல் மற்றும் தேர்தல் அட்டவணையை ஆளும் கட்சிக்கு சாதகமாக அமைப்பதாக எழும் குற்றச்சாட்டுகள்.",
                            "2026-க்குப் பிந்தைய தொகுதி மறுவரையறை சர்ச்சை: மக்கள் தொகையைக் கட்டுப்படுத்திய தென் மாநிலங்களுக்கும், மக்கள் தொகை அதிகம் உள்ள வட மாநிலங்களுக்கும் இடையே எழும் கூட்டாட்சி முரண்பாடுகள்."
                        ]
                    }
                },
                {
                    "title_en": "Holistic Way Forward & Strategic Reform Matrix",
                    "title_ta": "முழுமையான முன்னோக்கிய பாதை மற்றும் மூலோபாய சீர்திருத்த வரைவு",
                    "points": {
                        "en": [
                            "Equal Constitutional Protection for Election Commissioners: Amend Article 324(5) to provide the two Election Commissioners the exact same constitutional removal safeguard as the CEC (impeachment by Parliament).",
                            "ECI Financial Autonomy: Charge all expenditure of the Election Commission of India on the Consolidated Fund of India, eliminating executive budget dependence.",
                            "Cooling-off Period for Commissioners: Introduce a mandatory statutory cooling-off period barring retired CECs and ECs from accepting political appointments or governorships.",
                            "Enforce Statutory Inner-Party Democracy: Amend RPA 1951 to empower ECI to de-register political parties that fail to hold transparent internal elections or audit their financial donations.",
                            "Comprehensive State Funding in Kind: Implement Indrajit Gupta Committee recommendations by providing state funding in kind (free airtime, fuel, vehicles, printing facilities) to curb black money.",
                            "Strengthen Summary Adjudication of Disqualifications: Establish independent National Electoral Tribunals to dispose of election petitions within 6 months as intended by RPA 1951."
                        ],
                        "ta": [
                            "தேர்தல் ஆணையர்களுக்கு சமமான அரசியலமைப்பு பாதுகாப்பு: பிரிவு 324(5)-ல் திருத்தம் செய்து, பிற தேர்தல் ஆணையர்களுக்கும் தலைமை தேர்தல் ஆணையரைப் போன்றே பதவி நீக்க பாதுகாப்பை (நாடாளுமன்ற பதவிநீக்கம்) வழங்குதல்.",
                            "தேர்தல் ஆணையத்தின் நிதி தன்னாட்சி: தேர்தல் ஆணையத்தின் அனைத்து செலவினங்களையும் இந்திய ஒருங்கிணைந்த நிதியத்தின் (CFI) மீது சுமத்தப்பட்ட செலவினமாக (Charged expenditure) மாற்றுதல்.",
                            "ஆணையர்களுக்கு கட்டாய அமைதிக் காலம் (Cooling-off period): ஓய்வுபெறும் தேர்தல் ஆணையர்கள் அரசியல் பதவிகளையோ ஆளுநர் பதவிகளையோ உடனடியாக ஏற்பதைத் தடுக்கும் சட்டப்பூர்வ தடை.",
                            "உட்கட்சி ஜனநாயகத்தை கட்டாயமாக்குதல்: உட்கட்சித் தேர்தல்கள் நடத்தாத மற்றும் கணக்குகளை தணிக்கை செய்யாத கட்சிகளின் பதிவை ரத்து செய்யும் அதிகாரத்தை தேர்தல் ஆணையத்திற்கு வழங்குதல்.",
                            "பொருட்கள் வடிவிலான அரசு நிதியுதவி: இந்திரஜித் குப்தா குழு பரிந்துரைத்தபடி, கறுப்புப் பணப் புழக்கத்தைத் தடுக்க தகுதியுள்ள கட்சிகளுக்கு வாகனங்கள், எரிபொருள் மற்றும் விளம்பரங்களை அரசு இலவசமாக வழங்குதல்.",
                            "தேர்தல் வழக்குகளை விரைந்து முடித்தல்: தேர்தல் வழக்குகளை 6 மாதங்களுக்குள் விசாரித்து முடிக்க பிரத்யேக தேசிய தேர்தல் தீர்ப்பாயங்களை அமைத்தல்."
                        ]
                    }
                }
            ],
            "comparison_tables": [
                {
                    "id": "tbl_sc_landmark_judgments",
                    "title_en": "Master Matrix of Landmark Supreme Court Judgments on Electoral Reforms",
                    "title_ta": "தேர்தல் சீர்திருத்த வரலாற்று உச்சநீதிமன்றத் தீர்ப்புகளின் முழுமையான ஒப்பீட்டு அட்டவணை",
                    "headers_en": ["Case Name & Year", "Bench / Article", "Core Ruling & Principle", "Direct TNPSC Takeaway"],
                    "headers_ta": ["வழக்கின் பெயர் & ஆண்டு", "அமர்வு / சட்டப்பிரிவு", "முக்கிய தீர்ப்பு & கோட்பாடு", "TNPSC தேர்வு குறிப்பு"],
                    "rows_en": [
                        [
                            "Mohinder Singh Gill v. CEC (1978)",
                            "Art 324 (Constitution Bench)",
                            "Article 324 operates as a vast plenary reservoir of power where enacted law is silent, subject to natural justice.",
                            "ECI possesses inherent executive powers to ensure free & fair elections."
                        ],
                        [
                            "T.N. Seshan v. UOI (1995)",
                            "Art 324(2) (5-Judge Bench)",
                            "CEC is 'primus inter pares' (first among equals); ECs have co-equal powers, decisions by majority.",
                            "Removal protection under Art 324(5) applies only to CEC, not other ECs."
                        ],
                        [
                            "Union of India v. ADR (2002)",
                            "Art 19(1)(a) (3-Judge Bench)",
                            "Right to know candidate's assets, liabilities, education and criminal antecedents is a Fundamental Right.",
                            "Led to mandatory Form 26 affidavits for all candidates."
                        ],
                        [
                            "Lily Thomas v. UOI (2013)",
                            "Art 102 & 191; Sec 8(4) RPA",
                            "Section 8(4) of RPA 1951 struck down as unconstitutional; convicted MPs/MLAs disqualified immediately.",
                            "Eliminated the 3-month automatic appeal protection against disqualification."
                        ],
                        [
                            "PUCL v. UOI (2013 - NOTA)",
                            "Art 19(1)(a) & Sec 128 RPA",
                            "Directed inclusion of 'None of the Above' (NOTA) on EVMs to uphold secrecy of non-voting electors.",
                            "NOTA votes are non-electoral votes; candidate with highest valid votes wins."
                        ],
                        [
                            "Subramanian Swamy v. ECI (2013)",
                            "Art 324 & Conduct of Elections Rules",
                            "Paper trail via VVPAT is indispensable for voter verifiability, transparent voting, and EVM credibility.",
                            "VVPAT was formally introduced in 2013 by amending 1961 Rules."
                        ],
                        [
                            "Anoop Baranwal v. UOI (2023)",
                            "Art 324(2) (5-Judge Bench)",
                            "Directed appointment of CEC and ECs via 3-member collegium: PM, CJI, and Leader of Opposition.",
                            "Superseded by CEC and Other ECs Appointment Act 2023 replacing CJI with Cabinet Minister."
                        ],
                        [
                            "ADR v. Union of India (2024)",
                            "Art 19(1)(a) (5-Judge Bench)",
                            "Electoral Bonds Scheme struck down as unconstitutional; anonymous corporate funding violates right to information.",
                            "SBI ordered to disclose donor and redemption details to ECI for public display."
                        ]
                    ],
                    "rows_ta": [
                        [
                            "மொஹிந்தர் சிங் கில் வழக்கு (1978)",
                            "பிரிவு 324 (அரசியலமைப்பு அமர்வு)",
                            "சட்டம் மௌனமாக இருக்கும் இடங்களில் நியாயமான தேர்தலை நடத்த பிரிவு 324 தேர்தல் ஆணையத்திற்கு முழு அதிகாரம் வழங்குகிறது.",
                            "சுதந்திரமான தேர்தலை உறுதி செய்ய தேர்தல் ஆணையத்திற்கு உள்ளார்ந்த நிர்வாக அதிகாரம் உண்டு."
                        ],
                        [
                            "டி.என். சேஷன் வழக்கு (1995)",
                            "பிரிவு 324(2) (5 நீதிபதிகள்)",
                            "தலைமை தேர்தல் ஆணையர் சமமானவர்களில் முதன்மையானவர்; மற்ற ஆணையர்களுக்கு சம அதிகாரம் உண்டு, முடிவுகள் பெரும்பான்மைப்படி எடுக்கப்படும்.",
                            "பிரிவு 324(5) பதவி நீக்க பாதுகாப்பு CEC-க்கு மட்டுமே, பிற EC-களுக்கு பொருந்தாது."
                        ],
                        [
                            "ADR வழக்கு (2002)",
                            "பிரிவு 19(1)(a) (3 நீதிபதிகள்)",
                            "வேட்பாளர்களின் சொத்து, கல்வி, குற்றப்பின்னணியை அறியும் உரிமை வாக்காளர்களின் அடிப்படை உரிமை.",
                            "அனைத்து வேட்பாளர்களுக்கும் படிவம் 26 பிரமாணப் பத்திரம் கட்டாயமாக்கப்பட்டது."
                        ],
                        [
                            "லில்லி தாமஸ் வழக்கு (2013)",
                            "பிரிவு 102 & 191; பிரிவு 8(4) RPA",
                            "RPA 1951 பிரிவு 8(4) ரத்து செய்யப்பட்டது; 2+ ஆண்டுகள் தண்டனை பெற்ற எம்.பி./எம்.எல்.ஏ.க்கள் உடனடியாக தகுதிநீக்கம் செய்யப்படுவர்.",
                            "தகுதிநீக்கத்தைத் தள்ளிப்போடும் 3 மாத கால அவகாச சலுகை முற்றிலுமாக ரத்து செய்யப்பட்டது."
                        ],
                        [
                            "PUCL வழக்கு (2013 - NOTA)",
                            "பிரிவு 19(1)(a) & தேர்தல் நடத்தை விதிகள்",
                            "வாக்களிக்க விரும்பாத வாக்காளர்களின் ரகசியத்தன்மையைப் பாதுகாக்க EVM-ல் நோட்டா (NOTA) கொண்டுவர உத்தரவு.",
                            "நோட்டா அதிக வாக்கு பெற்றாலும், அடுத்த அதிக வாக்கு பெற்ற வேட்பாளரே வெற்றி பெற்றவராக அறிவிக்கப்படுவார்."
                        ],
                        [
                            "சுப்பிரமணியன் சுவாமி வழக்கு (2013)",
                            "பிரிவு 324 & தேர்தல் விதிகள் 1961",
                            "வாக்குப்பதிவின் நம்பகத்தன்மையை உறுதி செய்ய VVPAT காகித ரசீது முறை தேர்தல் நடைமுறைக்கு இன்றியமையாதது.",
                            "2013-ல் தேர்தல் நடத்தை விதிகளில் திருத்தம் செய்யப்பட்டு VVPAT முறை அறிமுகமானது."
                        ],
                        [
                            "அனூப் பரன்வால் வழக்கு (2023)",
                            "பிரிவு 324(2) (5 நீதிபதிகள்)",
                            "பிரதமர், தலைமை நீதிபதி (CJI) மற்றும் எதிர்க்கட்சித் தலைவர் அடங்கிய குழு தேர்தல் ஆணையர்களை நியமிக்க உத்தரவு.",
                            "2023 சட்டத்தின் மூலம் தலைமை நீதிபதி நீக்கப்பட்டு மத்திய அமைச்சர் சேர்க்கப்பட்டார்."
                        ],
                        [
                            "ADR தேர்தல் பத்திர வழக்கு (2024)",
                            "பிரிவு 19(1)(a) (5 நீதிபதிகள்)",
                            "தேர்தல் பத்திரத் திட்டம் தகவல் அறியும் உரிமையை மீறுவதால் அரசியலமைப்புக்கு முரணானது என ரத்து செய்யப்பட்டது.",
                            "நன்கொடையாளர் மற்றும் கட்சிகளின் முழுப் பணப் பரிவர்த்தனை விபரங்களையும் வெளியிட உத்தரவு."
                        ]
                    ]
                },
                {
                    "id": "tbl_simultaneous_elections_pros_cons",
                    "title_en": "Simultaneous Elections (One Nation, One Election) — Analytical Comparison",
                    "title_ta": "ஒரே நாடு, ஒரே தேர்தல் — வாதங்கள் மற்றும் சவால்கள் ஒப்பீட்டு அட்டவணை",
                    "headers_en": ["Dimension", "Arguments in Favour", "Arguments Against", "Kovind Committee Recommendation (2024)"],
                    "headers_ta": ["பரிமாணம்", "ஆதரவு வாதங்கள்", "எதிர்ப்பு வாதங்கள்", "கோவிந்த் குழுப் பரிந்துரை (2024)"],
                    "rows_en": [
                        [
                            "Governance & Policy",
                            "Stops recurrent policy paralysis caused by repetitive imposition of Model Code of Conduct (MCC).",
                            "Reduces democratic accountability as governments face voter scrutiny only once every 5 years.",
                            "Introduce Article 82A to align terms of State Assemblies with Lok Sabha until next general election."
                        ],
                        [
                            "Fiscal Expenditure",
                            "Saves thousands of crores of public funds spent separately on election machinery and logistics.",
                            "Initial massive expenditure required to procure millions of additional EVMs, VVPATs, and control units.",
                            "Consolidated procurement of EVMs and unified logistic planning across Election Commission of India."
                        ],
                        [
                            "Federalism & Politics",
                            "Allows political parties to focus on governance rather than perpetual campaigning mode.",
                            "National political narratives may overshadow vital regional and sub-regional state issues.",
                            "Two-tier process: Step 1 (LS + Assemblies) followed by Step 2 (Local Bodies within 100 days)."
                        ],
                        [
                            "Voter Turnout & Registration",
                            "Curbs voter fatigue, encourages higher participation, and prevents electoral roll duplication.",
                            "Complex dual-ballot voting on multiple machines may confuse less-educated rural electors.",
                            "Single unified electoral roll across Parliamentary, Assembly, and Panchayat/Municipal elections."
                        ]
                    ],
                    "rows_ta": [
                        [
                            "நிர்வாகம் மற்றும் கொள்கை",
                            "மாதிரி நடத்தை விதியால் (MCC) திட்டங்கள் அடிக்கடி தடைபடுவது முற்றிலுமாக தவிர்க்கப்படும்.",
                            "அரசாங்கங்கள் 5 ஆண்டுகளுக்கு ஒருமுறை மட்டுமே மக்களிடம் செல்வதால் அரசின் பொறுப்புடைமை குறையும் அபாயம்.",
                            "பிரிவு 82A-ஐ அறிமுகப்படுத்தி, மாநில சட்டப்பேரவைகளின் காலத்தை மக்களவையுடன் ஒரே நேரத்தில் ஒருங்கிணைத்தல்."
                        ],
                        [
                            "நிதிச் செலவினம்",
                            "மீண்டும் மீண்டும் தனித்தனியாக தேர்தல் நடத்துவதால் அரசுக்கு ஏற்படும் பல்லாயிரக்கணக்கான கோடி ரூபாய் மிச்சமாகும்.",
                            "லட்சக்கணக்கான புதிய EVM மற்றும் VVPAT இயந்திரங்களை வாங்க தொடக்கத்தில் பெருமளவு நிதி தேவைப்படும்.",
                            "தேர்தல் ஆணையம் மூலம் ஒருங்கிணைந்த கொள்முதல் மற்றும் தளவாட திட்டமிடல் மேற்கொள்ளுதல்."
                        ],
                        [
                            "கூட்டாட்சி & அரசியல்",
                            "கட்சிகள் தொடர் தேர்தல் பிரச்சாரத்தில் ஈடுபடாமல் ஆட்சி நிர்வாகத்தில் முழுமையாக கவனம் செலுத்த முடியும்.",
                            "தேசிய பிரச்சனைகள் மாநில அளவிலான உள்ளூர் பிரச்சனைகளை மறைத்துவிடக்கூடும்.",
                            "இரு கட்ட அணுகுமுறை: படிநிலை 1 (மக்களவை + சட்டமன்றம்), படிநிலை 2 (100 நாட்களில் உள்ளாட்சித் தேர்தல்)."
                        ],
                        [
                            "வாக்காளர் பங்களிப்பு & பட்டியல்",
                            "வாக்காளர் சோர்வு நீங்கி வாக்குப்பதிவு அதிகரிக்கும்; இரட்டை வாக்காளர் பட்டியல் குழப்பம் நீங்கும்.",
                            "ஒரே நேரத்தில் பல இயந்திரங்களில் வாக்களிப்பது கிராமப்புற வாக்காளர்களுக்கு குழப்பத்தை ஏற்படுத்தலாம்.",
                            "நாடாளுமன்றம், சட்டமன்றம் மற்றும் உள்ளாட்சி அமைப்புகளுக்கு ஒரே பொதுவான வாக்காளர் பட்டியல் தயாரித்தல்."
                        ]
                    ]
                }
            ],
            "mind_map": [
                {
                    "title": "Master Mind Map: Electoral Reforms in India (Parts 1, 2 & 3)",
                    "short_label": "Electoral Reforms Architecture",
                    "children": [
                        {
                            "title": "1. Constitutional Framework (Part 1)",
                            "short_label": "Constitutional Pillars",
                            "children": [
                                {"title": "Article 324: ECI Superintendence, Direction & Control"},
                                {"title": "Article 325: Single Non-Discriminatory Electoral Roll"},
                                {"title": "Article 326: Universal Adult Franchise (Voting age 21 -> 18 via 61st CAA)"},
                                {"title": "Articles 327 & 328: Powers of Parliament & State Legislatures"},
                                {"title": "Article 329: Bar to Interference by Courts in Electoral Matters"}
                            ]
                        },
                        {
                            "title": "2. Statutory Foundations (Part 1)",
                            "short_label": "Legal Architecture",
                            "children": [
                                {"title": "RPA 1950: Seat Allocation, Delimitation, Electoral Roll Preparation"},
                                {"title": "RPA 1951: Conduct of Elections, Disqualifications, Corrupt Practices"},
                                {"title": "Delimitation Commission: Redrawing boundaries without altering seat count (84th & 87th CAA)"},
                                {"title": "Reservation: Articles 330 & 332 SC/ST representation"}
                            ]
                        },
                        {
                            "title": "3. Committees & Innovations (Part 2)",
                            "short_label": "Committees & Technology",
                            "children": [
                                {"title": "Committees: Tarkunde (1974), Goswami (1990), Gupta (1998), Law Comm (1999 & 2015)"},
                                {"title": "EVM & VVPAT: Parur 1982 to 100% VVPAT 2019; standalone security safeguards"},
                                {"title": "Candidate Reforms: Form 26 Affidavit, NOTA, Disqualification under Lily Thomas (Sec 8(4))"},
                                {"title": "Conduct & Monitoring: Model Code of Conduct, cVIGIL app, Expenditure limits"}
                            ]
                        },
                        {
                            "title": "4. Contemporary Breakthroughs (Part 3)",
                            "short_label": "Contemporary & Judicial",
                            "children": [
                                {"title": "Electoral Bonds Struck Down: ADR v. UOI (2024) violates Article 19(1)(a)"},
                                {"title": "Women's Reservation: 106th CAA 2023 (Arts 330A, 332A, 334A - post-census delimitation)"},
                                {"title": "One Nation, One Election: Kovind Committee 2024 recommendations"},
                                {"title": "ECI Appointments: Anoop Baranwal (2023) to CEC & ECs Appointment Act 2023"},
                                {"title": "Voter Accessibility: ETPBS, RVM for migrants, Home voting for 85+ & PwD"}
                            ]
                        },
                        {
                            "title": "5. Way Forward & Reforms Matrix",
                            "short_label": "Future Trajectory",
                            "children": [
                                {"title": "Constitutional Parity: Art 324(5) removal protection for all Election Commissioners"},
                                {"title": "Financial Autonomy: Charge ECI expenditure on Consolidated Fund of India"},
                                {"title": "Inner-Party Democracy: Enforce internal elections and audit of party donations"},
                                {"title": "Electoral Tribunals: Time-bound 6-month disposal of election disputes"}
                            ]
                        }
                    ]
                }
            ],
            "tnpsc_traps": [
                {
                    "title": "1. Supreme Court Verdict on Electoral Bonds 2024 (தேர்தல் பத்திரங்கள் உச்சநீதிமன்ற தீர்ப்பு 2024)",
                    "points": {
                        "en": [
                            "TRAP: Assuming the Supreme Court struck down Electoral Bonds on grounds of Article 14 (Right to Equality).",
                            "FACT: The 5-judge Constitution Bench struck down the scheme specifically under Article 19(1)(a) (Right to Information), holding that anonymous political donations violate the voter's right to make an informed choice."
                        ],
                        "ta": [
                            "பொறி: தேர்தல் பத்திரங்களை உச்சநீதிமன்றம் சமத்துவ உரிமையின் கீழ் (உறுப்பு 14) ரத்து செய்தது என நினைப்பது.",
                            "உண்மை: 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு, வாக்காளர்களின் அடிப்படை தகவல் அறியும் உரிமையை (உறுப்பு 19(1)(a)) தேர்தல் பத்திரங்கள் மீறுவதாகக் கூறி ரத்து செய்தது."
                        ]
                    }
                },
                {
                    "title": "2. Implementation of 106th Constitutional Amendment Act, 2023 (106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023 அமலாக்கம்)",
                    "points": {
                        "en": [
                            "TRAP: Assuming the 33% reservation for women in Lok Sabha and State Legislative Assemblies came into immediate effect for the 2024 Lok Sabha elections.",
                            "FACT: Article 334A explicitly mandates that women's reservation shall take effect ONLY AFTER the first Census conducted after the commencement of the Act and the subsequent delimitation exercise."
                        ],
                        "ta": [
                            "பொறி: 2024 மக்களவைத் தேர்தலில் பெண்களுக்கு 33% இடஒதுக்கீடு உடனடியாக அமலுக்கு வந்துவிட்டது என நினைப்பது.",
                            "உண்மை: உறுப்பு 334A-ன் படி, இச்சட்டம் நடைமுறைக்கு வந்தபின் எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பு மற்றும் அதன் அடிப்படையிலான தொகுதி மறுவரையறைக்குப் பிறகே இந்த இடஒதுக்கீடு அமலுக்கு வரும்."
                        ]
                    }
                },
                {
                    "title": "3. Composition of ECI Selection Committee under 2023 Act (2023 சட்டத்தின் கீழ் தேர்தல் ஆணையர் தேர்வுக் குழுவின் கட்டமைப்பு)",
                    "points": {
                        "en": [
                            "TRAP: Assuming the statutory Selection Committee for appointing the CEC and Election Commissioners under the 2023 Act includes the Chief Justice of India (CJI).",
                            "FACT: The Supreme Court's March 2023 ruling in Anoop Baranwal included the CJI ONLY as an interim arrangement. The Parliament's 2023 Act replaced the CJI with a Union Cabinet Minister nominated by the Prime Minister."
                        ],
                        "ta": [
                            "பொறி: 2023 நியமனச் சட்டத்தின் கீழ் உள்ள தேர்வுக் குழுவில் உச்சநீதிமன்ற தலைமை நீதிபதி (CJI) இடம் பெற்றுள்ளார் என நினைப்பது.",
                            "உண்மை: அனூப் பரன்வால் வழக்கில் உச்சநீதிமன்றம் CJI-ஐ இடைக்கால ஏற்பாடாக மட்டுமே சேர்த்தது. நாடாளுமன்றத்தின் 2023 சட்டத்தில் தலைமை நீதிபதிக்கு பதிலாக ஒரு மத்திய அமைச்சரவை அமைச்சர் சேர்க்கப்பட்டுள்ளார்."
                        ]
                    }
                },
                {
                    "title": "4. Senior Citizens Home Voting Age Limit (முதியவர்கள் இல்ல வாக்குப்பதிவு வயது வரம்பு)",
                    "points": {
                        "en": [
                            "TRAP: Believing the eligibility age for senior citizens to cast home postal ballot remains at 80 years.",
                            "FACT: In March 2024, the Ministry of Law and Justice amended the Conduct of Elections Rules, 1961 to raise the senior citizen eligibility age from 80 years to 85 years and above."
                        ],
                        "ta": [
                            "பொறி: முதியவர்கள் வீட்டிலிருந்தே தபால் வாக்களிப்பதற்கான வயது வரம்பு 80 ஆண்டுகள் என நினைப்பது.",
                            "உண்மை: மார்ச் 2024-ல் தேர்தல் நடத்தை விதிகள் திருத்தப்பட்டு, முதியவர்களுக்கான தபால் வாக்கு பெறும் தகுதி வயது வரம்பு 80-லிருந்து 85 வயதாக உயர்த்தப்பட்டுள்ளது."
                        ]
                    }
                }
            ],
            "quick_revision": {
                "en": [
                    "ADR v. UOI (Feb 15, 2024): 5-judge Constitution Bench struck down Electoral Bonds Scheme 2018 and related amendments to RPA 1951, Companies Act 2013, and IT Act 1961 as unconstitutional under Article 19(1)(a).",
                    "106th Constitutional Amendment Act 2023: Inserted Articles 330A, 332A, and 334A reserving 33% seats for women in Lok Sabha and State Assemblies for 15 years, operational post-census delimitation.",
                    "Kovind Committee Report (March 2024): Recommended two-step Simultaneous Elections (LS + Assemblies first, local bodies within 100 days) and proposed Article 82A and single electoral roll under Article 325.",
                    "CEC & Other ECs Act 2023: Established statutory Selection Committee comprising PM (Chair), Leader of Opposition, and a Union Cabinet Minister, replacing executive-only discretion and omitting the CJI.",
                    "Lily Thomas v. UOI (2013): Struck down Section 8(4) of RPA 1951; convicted legislators sentenced to 2+ years imprisonment face immediate disqualification.",
                    "PUCL v. UOI (2013): Established voter's right to register dissent via NOTA button on EVMs under Article 19(1)(a).",
                    "RVM Prototype (Dec 2022): Developed by ECI with BEL and ECIL to enable remote voting for domestic migrants across up to 72 constituencies.",
                    "Home Voting (March 2024): Provided to Persons with 40%+ Disability and Senior Citizens aged 85 years and above via postal ballot Form 12D."
                ],
                "ta": [
                    "ADR வழக்கு (பிப்ரவரி 15, 2024): தேர்தல் பத்திரங்கள் திட்டம் 2018 மற்றும் அது தொடர்பான சட்டத் திருத்தங்கள் பிரிவு 19(1)(a)-ஐ மீறுவதாகக் கூறி 5 நீதிபதிகள் அமர்வு ஒருமனதாக ரத்து செய்தது.",
                    "106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023: மக்களவை மற்றும் சட்டமன்றங்களில் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்க புதிய பிரிவுகள் 330A, 332A மற்றும் 334A-ஐ சேர்த்தது.",
                    "கோவிந்த் குழு அறிக்கை (மார்ச் 2024): இரு கட்டங்களாக ஒரே தேர்தல் நடத்தப் பரிந்துரைத்தது (படி 1: மக்களவை + சட்டமன்றம், படி 2: 100 நாட்களில் உள்ளாட்சி); ஒற்றை வாக்காளர் பட்டியலை பரிந்துரைத்தது.",
                    "தேர்தல் ஆணையர் நியமனச் சட்டம் 2023: பிரதமர், எதிர்க்கட்சித் தலைவர் மற்றும் ஒரு மத்திய அமைச்சர் அடங்கிய தேர்வுக் குழுவை உருவாக்கியது (தலைமை நீதிபதி இதில் இல்லை).",
                    "லில்லி தாமஸ் வழக்கு (2013): 1951 RPA-வின் பிரிவு 8(4)-ஐ ரத்து செய்தது; 2 ஆண்டுகளுக்கு மேல் தண்டனை பெற்ற நாடாளுமன்ற, சட்டமன்ற உறுப்பினர்கள் உடனடியாக தகுதிநீக்கம் செய்யப்படுகின்றனர்.",
                    "PUCL வழக்கு (2013): பிரிவு 19(1)(a)-ன் கீழ் வாக்காளர்கள் அதிருப்தியை வெளிப்படுத்த நோட்டா (NOTA) முறையை அமல்படுத்த உத்தரவிட்டது.",
                    "RVM முன்மாதிரி (டிசம்பர் 2022): உள்நாட்டு புலம்பெயர்ந்தோருக்காக ஒரே வாக்குச்சாவடியில் 72 தொகுதிகளின் வாக்குகளைப் பதிவு செய்ய BEL & ECIL உதவியுடன் ECI உருவாக்கியது.",
                    "இல்ல வாக்குப்பதிவு (மார்ச் 2024): 40% மாற்றுத்திறனாளிகள் மற்றும் 85 வயதுக்கு மேற்பட்ட முதியவர்களுக்கு படிவம் 12D மூலம் வீட்டில் வாக்களிக்கும் வசதி வழங்கப்படுகிறது."
                ]
            },
            "important_facts": {
                "en": [
                    "The first four general elections in India (1952, 1957, 1962, and 1967) were simultaneous elections for both Lok Sabha and State Legislative Assemblies.",
                    "The 106th Constitutional Amendment Act, 2023 was introduced as the Constitution (128th Amendment) Bill, 2023 and received Presidential assent on September 28, 2023.",
                    "In February 2024, the Supreme Court struck down the amendment to Section 182 of the Companies Act, 2013 that had removed the 7.5% profit cap on corporate political donations.",
                    "The Supreme Court in INC v. Institute of Social Welfare (2002) confirmed that the Election Commission has no power under Section 29A of RPA 1951 to de-register a political party on internal democracy grounds.",
                    "The Supreme Court in April 2024 dismissed the plea for 100% VVPAT slip verification, but permitted candidates securing 2nd and 3rd positions to request micro-controller verification of 5% of EVMs per assembly segment."
                ],
                "ta": [
                    "சுதந்திர இந்தியாவில் முதல் நான்கு பொதுத்தேர்தல்கள் (1952, 1957, 1962 மற்றும் 1967) மக்களவைக்கும் மாநில சட்டமன்றங்களுக்கும் ஒரே நேரத்திலேயே நடைபெற்றன.",
                    "106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023, நாடாளுமன்றத்தில் 128-வது திருத்த மசோதாவாக அறிமுகப்படுத்தப்பட்டு, 2023 செப்டம்பர் 28 அன்று குடியரசுத் தலைவரின் ஒப்புதலைப் பெற்றது.",
                    "நிறுவனங்கள் தங்களின் நிகர லாபத்தில் 7.5% மட்டுமே அரசியல் நன்கொடை வழங்கலாம் என்ற வரம்பை நீக்கிய 2013 நிறுவனங்கள் சட்டப் பிரிவு 182 திருத்தத்தை பிப்ரவரி 2024-ல் உச்சநீதிமன்றம் ரத்து செய்தது.",
                    "உட்கட்சித் தேர்தல் நடத்தவில்லை என்பதற்காக அரசியல் கட்சிகளின் பதிவை ரத்து செய்யும் அதிகாரம் தேர்தல் ஆணையத்திற்கு இல்லை என 2002-ல் உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
                    "ஏப்ரல் 2024-ல் 100% VVPAT சரிபார்ப்பு கோரிக்கையை நிராகரித்த உச்சநீதிமன்றம், 2 மற்றும் 3-வது இடம் பெறும் வேட்பாளர்கள் கோரினால் தொகுதிக்கு 5% EVM நுண்செயலிகளை சரிபார்க்க அனுமதித்தது."
                ]
            },
            "revision_cards": [
                {
                    "title_en": "Electoral Bonds Supreme Court Ruling 2024",
                    "title_ta": "தேர்தல் பத்திரங்கள் உச்சநீதிமன்ற தீர்ப்பு 2024",
                    "front_en": "Which constitutional right was violated by the Electoral Bonds Scheme according to the Supreme Court Constitution Bench in February 2024?",
                    "front_ta": "பிப்ரவரி 2024-ல் உச்சநீதிமன்ற அரசியலமைப்பு அமர்வு வழங்கிய தீர்ப்பின்படி தேர்தல் பத்திரத் திட்டம் எந்த அடிப்படை உரிமையை மீறியது?",
                    "back_en": "Article 19(1)(a) — The Fundamental Right to Freedom of Speech and Expression, which encompasses the voter's Right to Information regarding the political funding of parties.",
                    "back_ta": "பிரிவு 19(1)(a) — வாக்காளர்களின் அடிப்படை உரிமையான தகவல் அறியும் உரிமை (Right to Information)."
                },
                {
                    "title_en": "Articles Added by 106th Constitutional Amendment",
                    "title_ta": "106-வது அரசியலமைப்பு திருத்தச் சட்டம் சேர்த்த புதிய பிரிவுகள்",
                    "front_en": "Which specific Articles were inserted into the Constitution by the 106th Amendment Act 2023?",
                    "front_ta": "106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023 மூலம் அரசியலமைப்பில் சேர்க்கப்பட்ட புதிய பிரிவுகள் எவை?",
                    "back_en": "Article 330A (Women's reservation in Lok Sabha), Article 332A (Women's reservation in State Assemblies), and Article 334A (Sunset clause & operationalization post-census delimitation). It also amended Article 239AA.",
                    "back_ta": "பிரிவு 330A (மக்களவை), பிரிவு 332A (சட்டமன்றங்கள்), பிரிவு 334A (மக்கள் தொகை கணக்கெடுப்பு மற்றும் தொகுதி மறுவரையறைக்கு பின் அமலாக்கம்). மேலும் பிரிவு 239AA திருத்தப்பட்டது."
                },
                {
                    "title_en": "Kovind Committee on Simultaneous Elections",
                    "title_ta": "கோவிந்த் குழு — ஒரே நாடு ஒரே தேர்தல்",
                    "front_en": "What was the two-step formula recommended by the Ram Nath Kovind High-Level Committee (March 2024)?",
                    "front_ta": "ராம் நாத் கோவிந்த் உயர்நிலைக் குழு (மார்ச் 2024) பரிந்துரைத்த இரு-படிநிலை முறை என்ன?",
                    "back_en": "Step 1: Synchronize Lok Sabha and all State Legislative Assembly elections simultaneously. Step 2: Synchronize local body elections (Panchayats & Municipalities) within 100 days of the first step.",
                    "back_ta": "படி 1: மக்களவை மற்றும் அனைத்து மாநில சட்டமன்ற தேர்தல்களையும் ஒரே நேரத்தில் நடத்துதல். படி 2: அதன் பிறகு 100 நாட்களுக்குள் உள்ளாட்சித் தேர்தல்களை நடத்துதல்."
                },
                {
                    "title_en": "Lily Thomas Case (2013) Disqualification Rule",
                    "title_ta": "லில்லி தாமஸ் வழக்கு (2013) தகுதிநீக்க விதி",
                    "front_en": "Which statutory provision was struck down in Lily Thomas v. Union of India (2013) to enforce immediate disqualification of convicted legislators?",
                    "front_ta": "குற்றவாளிகளாக அறிவிக்கப்பட்ட மக்கள் பிரதிநிதிகளை உடனடியாக தகுதிநீக்கம் செய்ய லில்லி தாமஸ் வழக்கில் ரத்து செய்யப்பட்ட சட்டப்பிரிவு எது?",
                    "back_en": "Section 8(4) of the Representation of the People Act, 1951, which previously allowed convicted MPs/MLAs a 3-month window to appeal and retain their seats.",
                    "back_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 8(4) ரத்து செய்யப்பட்டது (3 மாத கால மேல்முறையீட்டு சலுகை நீக்கப்பட்டது)."
                }
            ],
            "expected_questions": [
                {
                    "type": "prelims",
                    "question_en": "With reference to the Electoral Bonds Scheme, consider the following statements:\n1. The Supreme Court in February 2024 invalidated the scheme on the grounds that it violates Article 19(1)(a) of the Constitution.\n2. The Court restored the 7.5% limit on corporate donations under Section 182 of the Companies Act, 2013.\n3. The scheme was originally introduced through the Finance Act, 2017.\nWhich of the statements given above are correct?",
                    "question_ta": "தேர்தல் பத்திரங்கள் திட்டம் தொடர்பாக பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிப்ரவரி 2024-ல் உச்சநீதிமன்றம் இத்திட்டம் அரசியலமைப்பின் பிரிவு 19(1)(a)-ஐ மீறுவதாகக் கூறி ரத்து செய்தது.\n2. நிறுவனங்கள் சட்டம் 2013 பிரிவு 182-ன் கீழ் பெருநிறுவன நன்கொடைகளுக்கான 7.5% உச்சவரம்பை உச்சநீதிமன்றம் மீண்டும் கொண்டுவந்தது.\n3. இத்திட்டம் முதன்முதலில் 2017 நிதிச் சட்டம் மூலம் அறிமுகப்படுத்தப்பட்டது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
                    "options_en": [
                        "1 and 2 only",
                        "2 and 3 only",
                        "1 and 3 only",
                        "1, 2 and 3"
                    ],
                    "options_ta": [
                        "1 மற்றும் 2 மட்டும்",
                        "2 மற்றும் 3 மட்டும்",
                        "1 மற்றும் 3 மட்டும்",
                        "1, 2 மற்றும் 3"
                    ],
                    "answer_en": "1, 2 and 3",
                    "answer_ta": "1, 2 மற்றும் 3",
                    "explanation_en": "All three statements are correct. The 5-judge Constitution Bench in ADR v. Union of India (Feb 15, 2024) struck down the scheme under Article 19(1)(a), struck down the unlimited corporate funding amendment to Section 182 of Companies Act, and invalidated the Finance Act 2017 changes.",
                    "explanation_ta": "மூன்று கூற்றுகளும் சரியானவை. ADR வழக்கில் 5 நீதிபதிகள் அமர்வு தேர்தல் பத்திரங்களை பிரிவு 19(1)(a)-ன் கீழ் ரத்து செய்தது; நிறுவனங்கள் சட்டப் பிரிவு 182-ன் கீழ் 7.5% வரம்பை மீட்டெடுத்தது; 2017 நிதிச் சட்ட திருத்தங்களை செல்லாது என அறிவித்தது."
                },
                {
                    "type": "prelims",
                    "question_en": "The 106th Constitutional Amendment Act, 2023 provides 33% reservation for women in Lok Sabha and State Legislative Assemblies. Under Article 334A, this reservation shall come into effect:",
                    "question_ta": "106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023 மகளிருக்கு 33% இடஒதுக்கீடு வழங்குகிறது. பிரிவு 334A-ன் படி, இந்த இடஒதுக்கீடு எப்போது நடைமுறைக்கு வரும்?",
                    "options_en": [
                        "Immediately upon notification in the Official Gazette",
                        "From the 18th Lok Sabha general elections in 2024",
                        "After the delimitation exercise undertaken following the first Census conducted after the commencement of the Act",
                        "Only after ratification by all 28 State Legislatures"
                    ],
                    "options_ta": [
                        "அரசிதழில் வெளியிடப்பட்ட உடனே",
                        "2024-ல் நடைபெற்ற 18-வது மக்களவை பொதுத்தேர்தல் முதல்",
                        "இச்சட்டம் நடைமுறைக்கு வந்தபின் எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பு மற்றும் அதன் அடிப்படையிலான தொகுதி மறுவரையறைக்குப் பிறகு",
                        "அனைத்து 28 மாநில சட்டமன்றங்களும் ஒப்புதல் அளித்த பின் மட்டுமே"
                    ],
                    "answer_en": "After the delimitation exercise undertaken following the first Census conducted after the commencement of the Act",
                    "answer_ta": "இச்சட்டம் நடைமுறைக்கு வந்தபின் எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பு மற்றும் அதன் அடிப்படையிலான தொகுதி மறுவரையறைக்குப் பிறகு",
                    "explanation_en": "Article 334A explicitly provides that women's reservation shall take effect after an exercise of delimitation is undertaken for this purpose after the relevant figures for the first Census taken after the commencement of the Act have been published.",
                    "explanation_ta": "பிரிவு 334A-ன் படி, இச்சட்டம் நடைமுறைக்கு வந்தபின் நடத்தப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பின் புள்ளிவிவரங்கள் வெளியிடப்பட்டு, அதன் அடிப்படையில் மேற்கொள்ளப்படும் தொகுதி மறுவரையறைப் பணிகளுக்கு பிறகே இந்த இடஒதுக்கீடு அமலுக்கு வரும்."
                },
                {
                    "type": "mains",
                    "question_en": "Critically examine the constitutional, federal, and logistical challenges associated with holding Simultaneous Elections (One Nation, One Election) in India, in light of the High-Level Committee headed by Ram Nath Kovind (2024). (250 words, 15 marks)",
                    "question_ta": "ராம் நாத் கோவிந்த் தலைமையிலான உயர்நிலைக் குழுவின் (2024) பரிந்துரைகளின் அடிப்படையில், இந்தியாவில் ஒரே நேரத்தில் தேர்தல்கள் (ஒரே நாடு, ஒரே தேர்தல்) நடத்துவதில் உள்ள அரசியலமைப்பு, கூட்டாட்சி மற்றும் தளவாட சவால்களை விமர்சன ரீதியாக ஆராய்க. (250 சொற்கள், 15 மதிப்பெண்கள்)",
                    "model_answer_en": "Structure of Answer: 1. Introduction: Define Simultaneous Elections (ONOE) and cite the Ram Nath Kovind Committee report (March 2024) proposing a two-step formula. 2. Constitutional Hurdles: Amending Articles 83, 85, 172, 174, and proposed 82A; handling mid-term dissolution, hung assemblies, and no-confidence motions. 3. Federal Implications: Disproportionate focus on national narratives overshadowing state-specific issues; requirement of state ratification for Step 2 under Article 368(2). 4. Logistical & Technological Demands: Need for over 30 lakh EVMs/VVPATs, staggering deployment of CAPF forces, and unified voter roll compilation. 5. Arguments in Favour: Elimination of policy paralysis under MCC, curbing election expenditures, reducing voter fatigue. 6. Conclusion: Balanced way forward emphasizing broad federal consensus before legislative enactment.",
                    "model_answer_ta": "பதில் கட்டமைப்பு: 1. முன்னுரை: ONOE விளக்கம் மற்றும் கோவிந்த் குழுவின் இரு-படிநிலை பரிந்துரைகள் (மார்ச் 2024). 2. அரசியலமைப்பு சவால்கள்: பிரிவுகள் 83, 85, 172, 174 திருத்தங்கள்; புதிய பிரிவு 82A; நம்பிக்கையில்லா தீர்மானம் அல்லது தொங்கு சட்டமன்றம் ஏற்படும் போது எழும் சிக்கல்கள். 3. கூட்டாட்சி சவால்கள்: தேசிய விவகாரங்கள் மாநிலப் பிரச்சனைகளை மறைக்கும் அபாயம்; உள்ளாட்சித் தேர்தலுக்கான படிநிலை 2-ல் 50% மாநிலங்களின் ஒப்புதல் தேவை. 4. தளவாட சவால்கள்: லட்சக்கணக்கான கூடுதல் EVM/VVPAT தேவை, ராணுவப் படைகள் நகர்வு, ஒற்றை வாக்காளர் பட்டியல் தயாரிப்பு. 5. சாதகமான அம்சங்கள்: MCC-யால் அரசுப் பணிகள் முடங்குவது தவிர்ப்பு, ஆயிரக்கணக்கான கோடி செலவு மிச்சம். 6. முடிவுரை: அனைத்து அரசியல் கட்சிகள் மற்றும் மாநிலங்களின் ஒருமித்த கருத்துடன் மட்டுமே செயல்படுத்த வேண்டும்."
                }
            ],
            "pyq_references": [
                {
                    "exam": "TNPSC Group 1 Mains",
                    "year": "2019 / 2022",
                    "question_en": "Discuss the need for electoral reforms in India with special reference to State funding of elections and the decriminalisation of politics.",
                    "question_ta": "அரசியலில் குற்றமயமாதலைத் தடுத்தல் மற்றும் தேர்தல்களுக்கு அரசு நிதியுதவி வழங்குதல் ஆகியவற்றை மையமாகக் கொண்டு இந்தியாவில் தேர்தல் சீர்திருத்தங்களின் தேவையை விவாதிக்கவும்."
                },
                {
                    "exam": "UPSC Civil Services Mains (GS Paper II)",
                    "year": "2023",
                    "question_en": "'Simultaneous elections to the Lok Sabha and the State Assemblies will limit the amount of time and money spent in electioneering but it will reduce the government's accountability to the people.' Discuss.",
                    "question_ta": "'மக்களவை மற்றும் சட்டமன்றங்களுக்கு ஒரே நேரத்தில் தேர்தல் நடத்துவது பிரச்சார நேரத்தையும் பணத்தையும் குறைக்கும், ஆனால் அது மக்களுக்கு அரசாங்கத்தின் பொறுப்புடைமையைக் குறைக்கும்.' விவாதிக்கவும்."
                }
            ]
        }
    }

    output_path = os.path.abspath("data/notes/polity/electoral_reforms_part_3.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    size = os.path.getsize(output_path)
    print(f"✅ Part 3 generated successfully at {output_path} ({size} bytes)")

if __name__ == "__main__":
    build_part_3()
