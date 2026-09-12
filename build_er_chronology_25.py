# -*- coding: utf-8 -*-
"""
Generator for Electoral Reforms Chronology MCQs (25 Questions: ER_C_001 to ER_C_025).
Follows strict ChronologyValidator rules:
1. Four numbered events (1, 2, 3, 4) in stems presented in NON-chronological order.
2. Correct sequence != [1, 2, 3, 4].
3. Options are unique permutations of [1, 2, 3, 4].
4. Explanations teach chronology with 4-digit years and arrow sequence (->).
5. All 24 schema fields populated.
6. Balanced answer keys across A, B, C, D.
"""
import json
import os
from tools.nova_content_engine.chronology_validator import ChronologyValidator
from tools.nova_content_engine.validator import ContentValidator

raw_chronology_data = [
    # 1. Landmark Electoral Reform Committees
    {
        "id": "ER_C_001",
        "title": "Electoral Reform Committees",
        "events": [
            ("1. Indrajit Gupta Committee on State Funding of Elections", "1. தேர்தல் அரசு நிதி உதவி தொடர்பான இந்திரஜித் குப்தா குழு", 1998),
            ("2. V.M. Tarkunde Committee (JP Movement)", "2. வி.எம். தர்குண்டே குழு (ஜெயபிரகாஷ் நாராயண் இயக்கம்)", 1974),
            ("3. Law Commission 170th Report on Reform of Electoral Laws", "3. தேர்தல் சட்ட சீர்திருத்தங்கள் குறித்த 170-வது சட்ட ஆணைய அறிக்கை", 1999),
            ("4. Dinesh Goswami Committee on Electoral Reforms", "4. தேர்தல் சீர்திருத்தங்கள் குறித்த தினேஷ் கோஸ்வாமி குழு", 1990)
        ],
        # Chronological order: Tarkunde (1974) -> Goswami (1990) -> Indrajit Gupta (1998) -> Law Commission 170th (1999)
        # Sequence: 2 -> 4 -> 1 -> 3
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "explanation_en": "The correct chronological sequence of electoral reform committees is: 2. V.M. Tarkunde Committee (1974) -> 4. Dinesh Goswami Committee (1990) -> 1. Indrajit Gupta Committee (1998) -> 3. Law Commission 170th Report (1999).",
        "explanation_ta": "தேர்தல் சீர்திருத்தக் குழுக்களின் சரியான காலவரிசை: 2. வி.எம். தர்குண்டே குழு (1974) -> 4. தினேஷ் கோஸ்வாமி குழு (1990) -> 1. இந்திரஜித் குப்தா குழு (1998) -> 3. 170-வது சட்ட ஆணைய அறிக்கை (1999).",
        "tnpsc_tip": "Remember committee years: Tarkunde (1974), Goswami (1990), Gupta (1998), Law Commission (1999).",
        "revision_fact": "The Tarkunde Committee was appointed in 1974 by Jayaprakash Narayan under Citizens for Democracy.",
        "difficulty": "Medium"
    },

    # 2. Technology in Elections
    {
        "id": "ER_C_002",
        "title": "Introduction of Election Technology",
        "events": [
            ("1. Complete 100% EVM deployment in General Elections to Lok Sabha", "1. மக்களவை பொதுத்தேர்தலில் 100% வாக்குப்பதிவு இயந்திரங்கள் (EVM) பயன்பாடு", 2004),
            ("2. Pilot testing of EVMs in Paravur Assembly Constituency, Kerala", "2. கேரளாவின் பரவூர் சட்டமன்றத் தொகுதியில் EVM முதல் சோதனை பயன்பாடு", 1982),
            ("3. First pilot deployment of VVPAT in Noksen Constituency, Nagaland", "3. நாகாலாந்தின் நோக்சென் தொகுதியில் விவிபேட் (VVPAT) முதல் சோதனை பயன்பாடு", 2013),
            ("4. Legal backing for EVMs by insertion of Section 61A in RPA 1951", "4. 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தில் பிரிவு 61A சேர்த்து EVM-க்கு சட்ட அங்கீகாரம்", 1989)
        ],
        # Order: Paravur (1982) -> Sec 61A (1989) -> 100% EVM (2004) -> Noksen VVPAT (2013)
        # Sequence: 2 -> 4 -> 1 -> 3
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[2, 1, 4, 3], [4, 2, 1, 3], [1, 2, 4, 3]],
        "explanation_en": "The correct chronological sequence of electronic voting technology is: 2. Paravur EVM pilot (1982) -> 4. Section 61A legal backing in RPA (1989) -> 1. 100% EVM in Lok Sabha polls (2004) -> 3. Noksen VVPAT pilot (2013).",
        "explanation_ta": "தேர்தல் தொழில்நுட்ப வளர்ச்சியின் சரியான காலவரிசை: 2. பரவூர் EVM முன்னோடி திட்டம் (1982) -> 4. பிரிவு 61A சட்டப்பூர்வ அங்கீகாரம் (1989) -> 1. மக்களவைத் தேர்தலில் 100% EVM பயன்பாடு (2004) -> 3. நோக்சென் விவிபேட் முன்னோடி பயன்பாடு (2013).",
        "tnpsc_tip": "EVM was first used in 1982 (Paravur), given legal sanction in 1989, used nationwide in 2004, and VVPAT added in 2013.",
        "revision_fact": "Section 61A was inserted into the RPA 1951 with effect from 15 March 1989 to legalize electronic voting machines.",
        "difficulty": "Hard"
    },

    # 3. Landmark Supreme Court Judgments on Candidate Transparency & Criminalization
    {
        "id": "ER_C_003",
        "title": "Judicial Interventions on Electoral Transparency",
        "events": [
            ("1. PUCL v. Union of India (Directive to provide NOTA option)", "1. பியுசிஎல் எதிர் இந்திய ஒன்றியம் (நோட்டா விருப்பத்தை வழங்க உத்தரவு)", 2013),
            ("2. Union of India v. Association for Democratic Reforms (Mandatory asset & criminal disclosures)", "2. இந்திய ஒன்றியம் எதிர் ஏடிஆர் (சொத்து மற்றும் குற்றப்பின்னணி பிரகடனம் கட்டாயம்)", 2002),
            ("3. Public Interest Foundation v. Union of India (Publishing criminal antecedents in media)", "3. பப்ளிக் இன்ட்ரஸ்ட் ஃபவுண்டேஷன் எதிர் இந்திய ஒன்றியம் (குற்றப்பின்னணியை ஊடகங்களில் வெளியிட உத்தரவு)", 2018),
            ("4. Lily Thomas v. Union of India (Immediate disqualification of convicted legislators)", "4. லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (தண்டனை பெற்ற மக்கள் பிரதிநிதிகள் உடனடி தகுதிநீக்கம்)", 2013)
        ],
        # Note: ADR (2002) -> Lily Thomas (July 2013) -> PUCL NOTA (Sept 2013) -> Public Interest Foundation (2018)
        # Sequence: 2 -> 4 -> 1 -> 3
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[2, 1, 4, 3], [4, 2, 1, 3], [1, 2, 4, 3]],
        "explanation_en": "The correct chronological progression of electoral transparency judgments is: 2. ADR judgment on candidate disclosures (2002) -> 4. Lily Thomas case striking down Sec 8(4) (July 2013) -> 1. PUCL case introducing NOTA (September 2013) -> 3. Public Interest Foundation case on publishing antecedents (2018).",
        "explanation_ta": "தேர்தல் வெளிப்படைத்தன்மை குறித்த உச்ச நீதிமன்ற தீர்ப்புகளின் காலவரிசை: 2. ஏடிஆர் தீர்ப்பு (2002) -> 4. லில்லி தாமஸ் தீர்ப்பு (ஜூலை 2013) -> 1. பியுசிஎல் நோட்டா தீர்ப்பு (செப்டம்பர் 2013) -> 3. பப்ளிக் இன்ட்ரஸ்ட் ஃபவுண்டேஷன் தீர்ப்பு (2018).",
        "tnpsc_tip": "Lily Thomas was decided in July 2013, while NOTA (PUCL) was decided in September 2013.",
        "revision_fact": "Lily Thomas v. Union of India (2013) struck down Section 8(4) of RPA 1951 as unconstitutional.",
        "difficulty": "Hard"
    },

    # 4. Constitutional Amendments Related to Elections
    {
        "id": "ER_C_004",
        "title": "Constitutional Amendments on Elections",
        "events": [
            ("1. 87th Constitutional Amendment Act (Delimitation based on 2001 Census)", "1. 87-வது அரசியலமைப்பு திருத்தச் சட்டம் (2001 மக்கள் தொகை கணக்கெடுப்பு அடிப்படையிலான தொகுதி மறுவரையறை)", 2003),
            ("2. 61st Constitutional Amendment Act (Voting age lowered from 21 to 18)", "2. 61-வது அரசியலமைப்பு திருத்தச் சட்டம் (வாக்களிக்கும் வயது 21-லிருந்து 18 ஆக குறைப்பு)", 1988),
            ("3. 106th Constitutional Amendment Act (Nari Shakti Vandan Adhiniyam)", "3. 106-வது அரசியலமைப்பு திருத்தச் சட்டம் (நாரி சக்தி வந்தன் அதினியம் / மகளிர் இடஒதுக்கீடு)", 2023),
            ("4. 84th Constitutional Amendment Act (Freeze on Lok Sabha & Assembly seats till 2026)", "4. 84-வது அரசியலமைப்பு திருத்தச் சட்டம் (மக்களவை மற்றும் சட்டமன்ற இடங்கள் 2026 வரை முடக்கம்)", 2001)
        ],
        # Order: 61st (1988) -> 84th (2001) -> 87th (2003) -> 106th (2023)
        # Sequence: 2 -> 4 -> 1 -> 3
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "explanation_en": "The correct chronological sequence of constitutional amendments is: 2. 61st Amendment (1988) -> 4. 84th Amendment (2001) -> 1. 87th Amendment (2003) -> 3. 106th Amendment (2023).",
        "explanation_ta": "அரசியலமைப்பு திருத்தங்களின் சரியான காலவரிசை: 2. 61-வது திருத்தம் (1988) -> 4. 84-வது திருத்தம் (2001) -> 1. 87-வது திருத்தம் (2003) -> 3. 106-வது திருத்தம் (2023).",
        "tnpsc_tip": "61st (1988 - voting age 18), 84th (2001 - freeze till 2026), 87th (2003 - 2001 census), 106th (2023 - 33% women reservation).",
        "revision_fact": "The 106th Constitutional Amendment Act was the first bill passed in the new Parliament building in September 2023.",
        "difficulty": "Medium"
    },

    # 5. Evolution of Voter Enrolment & Voting Rights
    {
        "id": "ER_C_005",
        "title": "Evolution of Voter Rights and Enrolment Reforms",
        "events": [
            ("1. Introduction of four qualifying dates per year (Jan 1, Apr 1, Jul 1, Oct 1)", "1. ஆண்டுக்கு நான்கு தகுதி தேதிகள் அறிமுகம் (ஜன 1, ஏப் 1, ஜூலை 1, அக் 1)", 2021),
            ("2. Launch of Elector Photo Identity Cards (EPIC) nationwide", "2. நாடு முழுவதும் வாக்காளர் புகைப்பட அடையாள அட்டை (EPIC) அறிமுகம்", 1993),
            ("3. Grant of voting rights to Non-Resident Indians (NRIs) in person", "3. வெளிநாடு வாழ் இந்தியர்களுக்கு (NRI) நேரில் வாக்களிக்கும் உரிமை வழங்கல்", 2010),
            ("4. Launch of electronic Photo Identity Card (e-EPIC) program", "4. மின்னணு வாக்காளர் அடையாள அட்டை (e-EPIC) திட்டம் தொடக்கம்", 2021)
        ],
        # Order: EPIC (1993) -> NRI rights (2010) -> e-EPIC (Jan 2021) -> 4 Qualifying dates via Act (Dec 2021)
        # Note: 2 (1993) -> 3 (2010) -> 4 (Jan 2021) -> 1 (Dec 2021)
        # Sequence: 2 -> 3 -> 4 -> 1
        "correct_seq": [2, 3, 4, 1],
        "distractors": [[3, 2, 4, 1], [2, 4, 3, 1], [4, 2, 3, 1]],
        "explanation_en": "The correct chronological order is: 2. EPIC launch under CEC T.N. Seshan (1993) -> 3. NRI voting rights under Section 20A (2010) -> 4. e-EPIC launch on National Voters' Day (January 2021) -> 1. Election Laws (Amendment) Act providing 4 qualifying dates (December 2021).",
        "explanation_ta": "சரியான காலவரிசை: 2. புகைப்பட அடையாள அட்டை EPIC அறிமுகம் (1993) -> 3. என்.ஆர்.ஐ வாக்களிக்கும் உரிமை (2010) -> 4. மின்னணு e-EPIC வெளியீடு (ஜனவரி 2021) -> 1. 4 தகுதி தேதிகள் சட்டம் (டிசம்பர் 2021).",
        "tnpsc_tip": "T.N. Seshan introduced EPIC in 1993. 4 qualifying dates were introduced by the 2021 Amendment Act.",
        "revision_fact": "Section 20A was inserted into RPA 1950 by Act 36 of 2010 to confer voting rights on citizens living abroad.",
        "difficulty": "Hard"
    },

    # 6. Reforms in Political Financing
    {
        "id": "ER_C_006",
        "title": "Evolution of Political Financing and Transparency Rules",
        "events": [
            ("1. Supreme Court strikes down the Electoral Bond Scheme as unconstitutional", "1. தேர்தல் பத்திரத் திட்டத்தை அரசியலமைப்பிற்கு எதிரானது என உச்ச நீதிமன்றம் ரத்து செய்தது", 2024),
            ("2. Indrajit Gupta Committee submits comprehensive report on State Funding of Elections", "2. தேர்தல் அரசு நிதி உதவி குறித்து இந்திரஜித் குப்தா குழு விரிவான அறிக்கை சமர்ப்பித்தது", 1998),
            ("3. Introduction of Electoral Trusts Scheme by Central Government", "3. மத்திய அரசால் தேர்தல் அறக்கட்டளை திட்டம் (Electoral Trusts Scheme) அறிமுகம்", 2013),
            ("4. Notification and launch of the Electoral Bonds Scheme", "4. தேர்தல் பத்திரத் திட்டம் (Electoral Bonds Scheme) அறிவிக்கப்பட்டு தொடங்கப்பட்டது", 2018)
        ],
        # Order: Indrajit Gupta (1998) -> Electoral Trusts (2013) -> Electoral Bonds (2018) -> Bonds Struck Down (2024)
        # Sequence: 2 -> 3 -> 4 -> 1
        "correct_seq": [2, 3, 4, 1],
        "distractors": [[3, 2, 4, 1], [2, 4, 3, 1], [4, 2, 3, 1]],
        "explanation_en": "The correct chronological sequence of political finance milestones is: 2. Indrajit Gupta Committee report (1998) -> 3. Electoral Trusts Scheme notified (2013) -> 4. Electoral Bonds Scheme notified (2018) -> 1. Supreme Court strikes down Electoral Bonds Scheme (2024).",
        "explanation_ta": "அரசியல் நிதி சீர்திருத்தங்களின் சரியான காலவரிசை: 2. இந்திரஜித் குப்தா குழு அறிக்கை (1998) -> 3. தேர்தல் அறக்கட்டளை திட்டம் (2013) -> 4. தேர்தல் பத்திர திட்டம் அறிமுகம் (2018) -> 1. தேர்தல் பத்திர திட்டம் உச்ச நீதிமன்றத்தால் ரத்து (2024).",
        "tnpsc_tip": "Electoral Trusts Scheme was launched in 2013, Electoral Bonds in 2018, and struck down on 15 Feb 2024.",
        "revision_fact": "A 5-judge Constitution Bench headed by CJI D.Y. Chandrachud unanimously invalidated Electoral Bonds on 15 February 2024.",
        "difficulty": "Medium"
    },

    # 7. RPA 1951 Key Statutory Amendments
    {
        "id": "ER_C_007",
        "title": "Key Amendments to the Representation of the People Act 1951",
        "events": [
            ("1. Insertion of Section 126A banning exit polls during voting phases", "1. தேர்தல் கட்டங்களின் போது கருத்துக் கணிப்பு முடிவுகளை வெளியிட தடை விதிக்கும் பிரிவு 126A சேர்ப்பு", 2009),
            ("2. Insertion of Section 58A empowering ECI to adjourn/cancel polls for booth capturing", "2. வாக்குச்சாவடி கைப்பற்றப்பட்டால் தேர்தலை ஒத்திவைக்க/ரத்து செய்ய தேர்தல் ஆணையத்திற்கு அதிகாரமளிக்கும் பிரிவு 58A சேர்ப்பு", 1989),
            ("3. Insertion of Section 33(7) restricting a candidate to maximum two constituencies", "3. ஒரு வேட்பாளர் அதிகபட்சம் இரண்டு தொகுதிகளில் மட்டுமே போட்டியிட கட்டுப்படுத்தும் பிரிவு 33(7) சேர்ப்பு", 1996),
            ("4. Insertion of Section 29A providing statutory registration of political parties", "4. அரசியல் கட்சிகளின் சட்டப்பூர்வ பதிவை வழங்கும் பிரிவு 29A சேர்ப்பு", 1988)
        ],
        # Order: 29A (1988) -> 58A (1989) -> 33(7) (1996) -> 126A (2009)
        # Sequence: 4 -> 2 -> 3 -> 1
        "correct_seq": [4, 2, 3, 1],
        "distractors": [[2, 4, 3, 1], [4, 3, 2, 1], [3, 4, 2, 1]],
        "explanation_en": "The correct chronological sequence of key RPA amendments is: 4. Section 29A on political party registration (1988) -> 2. Section 58A on booth capturing (1989) -> 3. Section 33(7) limiting to two constituencies (1996) -> 1. Section 126A banning exit polls (2009).",
        "explanation_ta": "மக்கள் பிரதிநிதித்துவச் சட்ட திருத்தங்களின் சரியான காலவரிசை: 4. அரசியல் கட்சிகள் பதிவு பிரிவு 29A (1988) -> 2. பூத் கைப்பற்றல் பிரிவு 58A (1989) -> 3. அதிகபட்சம் இரு தொகுதிகள் பிரிவு 33(7) (1996) -> 1. எக்சிட் போல் தடை பிரிவு 126A (2009).",
        "tnpsc_tip": "Sec 29A (1988), Sec 58A (1989), Sec 33(7) (1996), Sec 126A (2009).",
        "revision_fact": "Section 33(7) was inserted in 1996; prior to this, a candidate could contest from any number of constituencies.",
        "difficulty": "Hard"
    },

    # 8. Supreme Court Jurisprudence on Basic Structure & Elections
    {
        "id": "ER_C_008",
        "title": "Constitutional Bench Rulings on Electoral Integrity",
        "events": [
            ("1. Kuldip Nayar v. Union of India (Upholding open ballot system in Rajya Sabha)", "1. குல்தீப் நய்யார் எதிர் இந்திய ஒன்றியம் (மாநிலங்களவையில் திறந்த வாக்குச்சீட்டு முறையை உறுதி செய்தது)", 2006),
            ("2. Indira Nehru Gandhi v. Raj Narain (Free and fair elections declared Basic Structure)", "2. இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (சுதந்திரமான மற்றும் நேர்மையான தேர்தல் அடிப்படை கட்டமைப்பு என பிரகடனம்)", 1975),
            ("3. Anoop Baranwal v. Union of India (Collegium system for appointment of CEC & ECs)", "3. அனூப் பரன்வால் எதிர் இந்திய ஒன்றியம் (தலைமை தேர்தல் ஆணையர் நியமனத்திற்கு கொலீஜியம் முறை பரிந்துரை)", 2023),
            ("4. Mohinder Singh Gill v. CEC (Article 324 is a reservoir of plenary inherent powers)", "4. மொகிந்தர் சிங் கில் எதிர் தலைமை தேர்தல் ஆணையர் (சரத்து 324 என்பது முழுமையான அதிகாரங்களின் தேக்கம்)", 1978)
        ],
        # Order: Indira Gandhi (1975) -> Mohinder Gill (1978) -> Kuldip Nayar (2006) -> Anoop Baranwal (2023)
        # Sequence: 2 -> 4 -> 1 -> 3
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "explanation_en": "The correct chronological sequence of constitutional bench decisions is: 2. Indira Nehru Gandhi v. Raj Narain (1975) -> 4. Mohinder Singh Gill v. CEC (1978) -> 1. Kuldip Nayar v. Union of India (2006) -> 3. Anoop Baranwal v. Union of India (2023).",
        "explanation_ta": "அரசியலமைப்பு அமர்வு தீர்ப்புகளின் சரியான காலவரிசை: 2. இந்திரா காந்தி எதிர் ராஜ் நாராயண் (1975) -> 4. மொகிந்தர் சிங் கில் எதிர் தலைமை தேர்தல் ஆணையர் (1978) -> 1. குல்தீப் நய்யார் தீர்ப்பு (2006) -> 3. அனூப் பரன்வால் தீர்ப்பு (2023).",
        "tnpsc_tip": "Indira Gandhi (1975) applied basic structure to elections; Mohinder Gill (1978) established plenary power under Art 324.",
        "revision_fact": "In Mohinder Singh Gill (1978), Justice V.R. Krishna Iyer observed that Article 324 operates in areas unprovided by legislation.",
        "difficulty": "Hard"
    },

    # 9. Delimitation Commissions of India
    {
        "id": "ER_C_009",
        "title": "Delimitation Commission Acts and Freezes",
        "events": [
            ("1. 42nd Constitutional Amendment Act imposing freeze on delimitation till 2000", "1. 2000 வரை தொகுதி மறுவரையறைக்கு தடை விதித்த 42-வது அரசியலமைப்பு திருத்தச் சட்டம்", 1976),
            ("2. Third Delimitation Commission Act enacted by Parliament", "2. பாராளுமன்றத்தால் இயற்றப்பட்ட மூன்றாவது தொகுதி மறுவரையறை ஆணையச் சட்டம்", 1972),
            ("3. Fourth Delimitation Commission Act under Justice Kuldip Singh", "3. நீதிபதி குல்தீப் சிங் தலைமையிலான நான்காவது தொகுதி மறுவரையறை ஆணையச் சட்டம்", 2002),
            ("4. Second Delimitation Commission Act following 1961 Census", "4. 1961 மக்கள் தொகை கணக்கெடுப்பைத் தொடர்ந்து இரண்டாவது தொகுதி மறுவரையறை ஆணையச் சட்டம்", 1962)
        ],
        # Order: 2nd Delimitation (1962) -> 3rd Delimitation (1972) -> 42nd Amendment freeze (1976) -> 4th Delimitation (2002)
        # Sequence: 4 -> 2 -> 1 -> 3
        "correct_seq": [4, 2, 1, 3],
        "distractors": [[2, 4, 1, 3], [4, 1, 2, 3], [1, 4, 2, 3]],
        "explanation_en": "The correct chronological sequence of delimitation milestones is: 4. Second Delimitation Act (1962) -> 2. Third Delimitation Act (1972) -> 1. 42nd Constitutional Amendment freeze (1976) -> 3. Fourth Delimitation Act (2002).",
        "explanation_ta": "தொகுதி மறுவரையறை மைல்கற்களின் சரியான காலவரிசை: 4. இரண்டாவது மறுவரையறைச் சட்டம் (1962) -> 2. மூன்றாவது மறுவரையறைச் சட்டம் (1972) -> 1. 42-வது திருத்த முடக்கம் (1976) -> 3. நான்காவது மறுவரையறைச் சட்டம் (2002).",
        "tnpsc_tip": "Delimitation Commissions were set up under Acts of 1952, 1962, 1972, and 2002.",
        "revision_fact": "The 4th Delimitation Commission completed its work in 2008 readjusting boundaries based on the 2001 Census without altering total seats.",
        "difficulty": "Medium"
    },

    # 10. NOTA Evolution & Milestones
    {
        "id": "ER_C_010",
        "title": "Evolution of None of the Above (NOTA) in India",
        "events": [
            ("1. Introduction of official NOTA symbol designed by National Institute of Design (NID)", "1. தேசிய வடிவமைப்பு நிறுவனத்தால் (NID) வடிவமைக்கப்பட்ட அதிகாரப்பூர்வ நோட்டா சின்னம் அறிமுகம்", 2015),
            ("2. Supreme Court ruling in PUCL v. UOI directing introduction of NOTA", "2. நோட்டாவை அறிமுகப்படுத்த உத்தரவிட்ட பியுசிஎல் வழக்கில் உச்ச நீதிமன்றத் தீர்ப்பு", 2013),
            ("3. Supreme Court ruling in Shailesh Parmar case removing NOTA from Rajya Sabha elections", "3. மாநிலங்களவைத் தேர்தல்களில் நோட்டா செல்லாது என தீர்ப்பளித்த சைலேஷ் பர்மர் வழக்கு", 2018),
            ("4. First implementation of NOTA across 5 state assembly elections", "4. 5 மாநில சட்டமன்றத் தேர்தல்களில் நோட்டா முதன்முதலில் நடைமுறைப்படுத்தப்பட்டது", 2013)
        ],
        # Note: PUCL verdict (Sept 2013) -> First used in Assembly polls (Nov-Dec 2013) -> NID Symbol (Sept 2015) -> Shailesh Parmar RS NOTA removed (Aug 2018)
        # Sequence: 2 -> 4 -> 1 -> 3
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "explanation_en": "The correct chronological sequence of NOTA evolution is: 2. Supreme Court verdict in PUCL (September 2013) -> 4. First implementation in 5 state assembly elections (November-December 2013) -> 1. Official NOTA symbol introduced (September 2015) -> 3. Shailesh Parmar judgment removing NOTA from Rajya Sabha (August 2018).",
        "explanation_ta": "நோட்டா பரிணாம வளர்ச்சியின் சரியான காலவரிசை: 2. பியுசிஎல் உச்ச நீதிமன்றத் தீர்ப்பு (செப்டம்பர் 2013) -> 4. 5 மாநில சட்டமன்றத் தேர்தல்களில் முதல் பயன்பாடு (டிசம்பர் 2013) -> 1. அதிகாரப்பூர்வ நோட்டா சின்னம் அறிமுகம் (2015) -> 3. மாநிலங்களவையில் நோட்டா நீக்கம் குறித்த தீர்ப்பு (2018).",
        "tnpsc_tip": "NOTA was introduced in Sept 2013, used in late 2013, got its official symbol in 2015, and was barred in Rajya Sabha in 2018.",
        "revision_fact": "The NOTA symbol was created by the National Institute of Design (NID), Ahmedabad, and introduced on 18 September 2015.",
        "difficulty": "Hard"
    },

    # 11. Model Code of Conduct (MCC) Milestones
    {
        "id": "ER_C_011",
        "title": "Evolution and Milestones of Model Code of Conduct",
        "events": [
            ("1. Supreme Court direction in S. Subramaniam Balaji case leading to ECI guidelines on election manifestos", "1. தேர்தல் தேர்தல் அறிக்கைகள் குறித்த வழிகாட்டுதல்களை தேர்தல் ஆணையம் சேர்க்க காரணமான எஸ். சுப்பிரமணியம் பாலாஜி வழக்கு", 2013),
            ("2. First experimental adoption of MCC in Kerala State Assembly elections", "2. கேரளா மாநில சட்டமன்றத் தேர்தலில் தேர்தல் நடத்தை விதிகள் முதன்முதலில் முன்னோடியாக அறிமுகம்", 1960),
            ("3. ECI issued comprehensive Model Code of Conduct including Party in Power rules", "3. ஆளும் கட்சிக்கான கட்டுப்பாடுகள் உட்பட முழுமையான தேர்தல் நடத்தை விதிகளை தேர்தல் ஆணையம் வெளியிட்டது", 1979),
            ("4. Consensus by political parties to adopt MCC for Lok Sabha general elections", "4. மக்களவை பொதுத்தேர்தலில் நடத்தை விதிகளை பின்பற்ற அனைத்து அரசியல் கட்சிகள் ஒப்புதல்", 1962)
        ],
        # Order: Kerala (1960) -> Lok Sabha (1962) -> Party in Power (1979) -> Balaji manifestos (2013)
        # Sequence: 2 -> 4 -> 3 -> 1
        "correct_seq": [2, 4, 3, 1],
        "distractors": [[4, 2, 3, 1], [2, 3, 4, 1], [3, 2, 4, 1]],
        "explanation_en": "The correct chronological sequence of MCC milestones is: 2. Experimental adoption in Kerala (1960) -> 4. Voluntary adoption for Lok Sabha polls (1962) -> 3. Comprehensive MCC including 'Party in Power' norms (1979) -> 1. ECI guidelines on election manifestos following Balaji case (2013).",
        "explanation_ta": "தேர்தல் நடத்தை விதிகளின் (MCC) சரியான காலவரிசை: 2. கேரளாவில் முதல் முன்னோடி பயன்பாடு (1960) -> 4. மக்களவை தேர்தலில் கட்சிகள் ஒப்புதல் (1962) -> 3. ஆளும் கட்சிக்கான விதிகள் சேர்ப்பு (1979) -> 1. சுப்பிரமணியம் பாலாஜி வழக்கைத் தொடர்ந்து தேர்தல் அறிக்கை வழிகாட்டுதல்கள் (2013).",
        "tnpsc_tip": "MCC originated in Kerala in 1960, spread to Lok Sabha in 1962, added Party in Power norms in 1979, and manifestos in 2013.",
        "revision_fact": "The MCC has no statutory backing; it is enforced by the ECI under its plenary powers under Article 324.",
        "difficulty": "Medium"
    },

    # 12. Modern Digital Portals & Citizen Apps
    {
        "id": "ER_C_012",
        "title": "Digital Innovations and Mobile Applications of ECI",
        "events": [
            ("1. Launch of Suvidha 2.0 portal for simplified candidate nominations & rally permissions", "1. வேட்புமனு மற்றும் பேரணி அனுமதிகளுக்கான சுவிதா 2.0 இணையதளம் அறிமுகம்", 2024),
            ("2. Nationwide rollout of cVIGIL application for reporting MCC violations", "2. தேர்தல் நடத்தை விதிமீறல்களைப் புகாரளிக்க சிவிஜில் (cVIGIL) செயலி நாடு முழுவதும் அறிமுகம்", 2019),
            ("3. Launch of National Voters' Service Portal (NVSP)", "3. தேசிய வாக்காளர் சேவை இணையதளம் (NVSP) தொடக்கம்", 2015),
            ("4. Launch of Saksham App for Persons with Disabilities (PwD) voters", "4. மாற்றுத்திறனாளி வாக்காளர்களுக்கான சாக்ஷம் (Saksham) செயலி அறிமுகம்", 2022)
        ],
        # Order: NVSP (2015) -> cVIGIL (2019) -> Saksham (2022) -> Suvidha 2.0 (2024)
        # Sequence: 3 -> 2 -> 4 -> 1
        "correct_seq": [3, 2, 4, 1],
        "distractors": [[2, 3, 4, 1], [3, 4, 2, 1], [4, 3, 2, 1]],
        "explanation_en": "The correct chronological sequence of digital election tools is: 3. Launch of NVSP (2015) -> 2. Rollout of cVIGIL app (2019) -> 4. Launch of Saksham App for PwD voters (2022) -> 1. Launch of upgraded Suvidha 2.0 portal (2024).",
        "explanation_ta": "தேர்தல் டிஜிட்டல் தளங்களின் சரியான காலவரிசை: 3. NVSP தளம் தொடக்கம் (2015) -> 2. சிவிஜில் செயலி அறிமுகம் (2019) -> 4. மாற்றுத்திறனாளிகளுக்கான சாக்ஷம் செயலி (2022) -> 1. சுவிதா 2.0 போர்டல் அறிமுகம் (2024).",
        "tnpsc_tip": "NVSP was launched on National Voters' Day 2015; cVIGIL was rolled out for the 2019 General Elections.",
        "revision_fact": "cVIGIL guarantees a response and resolution by election officials within 100 minutes of complaint submission.",
        "difficulty": "Medium"
    },

    # 13. Second Generation Committees & Law Commission Reports
    {
        "id": "ER_C_013",
        "title": "Second Generation Reform Reports and Commissions",
        "events": [
            ("1. Second Administrative Reforms Commission (ARC) 4th Report 'Ethics in Governance'", "1. இரண்டாவது நிர்வாக சீர்திருத்த ஆணையத்தின் (ARC) 4-வது அறிக்கை 'ஆளுகையில் நெறிமுறைகள்'", 2007),
            ("2. National Commission to Review the Working of the Constitution (NCRWC / Venkatachaliah Commission)", "2. அரசியலமைப்பின் செயல்பாட்டை மறுஆய்வு செய்வதற்கான தேசிய ஆணையம் (வெங்கடாசலையா ஆணையம்)", 2002),
            ("3. Law Commission 255th Report on 'Electoral Reforms'", "3. 'தேர்தல் சீர்திருத்தங்கள்' குறித்த சட்ட ஆணையத்தின் 255-வது அறிக்கை", 2015),
            ("4. Law Commission 244th Report on 'Electoral Disqualifications'", "4. 'தேர்தல் தகுதிநீக்கங்கள்' குறித்த சட்ட ஆணையத்தின் 244-வது அறிக்கை", 2014)
        ],
        # Order: NCRWC (2002) -> 2nd ARC (2007) -> Law Commission 244th (2014) -> Law Commission 255th (2015)
        # Sequence: 2 -> 1 -> 4 -> 3
        "correct_seq": [2, 1, 4, 3],
        "distractors": [[1, 2, 4, 3], [2, 4, 1, 3], [4, 2, 1, 3]],
        "explanation_en": "The correct chronological sequence of second-generation reform reports is: 2. NCRWC / Venkatachaliah Commission report (2002) -> 1. 2nd ARC 4th Report 'Ethics in Governance' (2007) -> 4. Law Commission 244th Report (2014) -> 3. Law Commission 255th Report on Electoral Reforms (2015).",
        "explanation_ta": "இரண்டாம் தலைமுறை சீர்திருத்த அறிக்கைகளின் காலவரிசை: 2. வெங்கடாசலையா ஆணைய அறிக்கை (2002) -> 1. இரண்டாவது நிர்வாக சீர்திருத்த ஆணைய அறிக்கை (2007) -> 4. 244-வது சட்ட ஆணைய அறிக்கை (2014) -> 3. 255-வது சட்ட ஆணைய அறிக்கை (2015).",
        "tnpsc_tip": "Law Commission 244th report dealt with disqualifications (2014), while 255th report dealt with overall electoral reforms (2015).",
        "revision_fact": "The 255th Law Commission report recommended stringent curbs on paid news, criminalization, and government-sponsored advertising.",
        "difficulty": "Hard"
    },

    # 14. VVPAT Evolution & Judicial Orders
    {
        "id": "ER_C_014",
        "title": "VVPAT Introduction and Verification Orders",
        "events": [
            ("1. Supreme Court directs verification of 5 VVPATs per assembly constituency (Chandrababu Naidu case)", "1. தொகுதிக்கு 5 விவிபேட்களை சரிபார்க்க உச்ச நீதிமன்றம் உத்தரவிட்டது (சந்திரபாபு நாயுடு வழக்கு)", 2019),
            ("2. Supreme Court in Subramanian Swamy v. ECI directs gradual introduction of paper trail", "2. சுப்பிரமணியன் சுவாமி வழக்கில் விவிபேட் முறையை படிப்படியாக அறிமுகப்படுத்த உச்ச நீதிமன்றம் உத்தரவு", 2013),
            ("3. Supreme Court rejects petition seeking 100% cross-verification of VVPAT slips (ADR v. ECI)", "3. 100% விவிபேட் சீட்டுகளை சரிபார்க்கக் கோரிய மனுவை உச்ச நீதிமன்றம் நிராகரித்தது (ஏடிஆர் வழக்கு)", 2024),
            ("4. ECI conducts first 100% VVPAT-equipped General Elections to Lok Sabha", "4. மக்களவை பொதுத்தேர்தலில் அனைத்து வாக்குச்சாவடிகளிலும் 100% விவிபேட் பயன்பாடு", 2019)
        ],
        # Note: Swamy (Oct 2013) -> Chandrababu Naidu 5 VVPATs order (April 2019) -> 100% VVPAT Lok Sabha election (April-May 2019) -> 100% verification rejected (April 2024)
        # Sequence: 2 -> 1 -> 4 -> 3
        "correct_seq": [2, 1, 4, 3],
        "distractors": [[1, 2, 4, 3], [2, 4, 1, 3], [4, 2, 1, 3]],
        "explanation_en": "The correct chronological progression of VVPAT jurisprudence is: 2. Subramanian Swamy v. ECI ruling mandating VVPAT (2013) -> 1. SC order increasing verification to 5 VVPATs per segment (April 2019) -> 4. 100% VVPAT deployment across all polling booths in Lok Sabha polls (April-May 2019) -> 3. SC rejection of 100% physical tally plea (April 2024).",
        "explanation_ta": "விவிபேட் நீதித்துறை உத்தரவுகளின் சரியான காலவரிசை: 2. சுப்பிரமணியன் சுவாமி வழக்கு தீர்ப்பு (2013) -> 1. தொகுதிக்கு 5 விவிபேட் சரிபார்ப்பு உத்தரவு (ஏப்ரல் 2019) -> 4. மக்களவைத் தேர்தலில் 100% விவிபேட் பயன்பாடு (மே 2019) -> 3. 100% சீட்டு சரிபார்ப்பு கோரிக்கை நிராகரிப்பு (ஏப்ரல் 2024).",
        "tnpsc_tip": "In April 2019, SC increased VVPAT counting from 1 to 5 per assembly segment.",
        "revision_fact": "On 26 April 2024, a two-judge bench of Sanjiv Khanna and Dipankar Datta rejected the plea for 100% counting of VVPAT slips.",
        "difficulty": "Hard"
    },

    # 15. Candidate Disqualification and Election Petitions Jurisprudence
    {
        "id": "ER_C_015",
        "title": "Key Judgments on Disqualification and Election Offences",
        "events": [
            ("1. Lok Prahari v. Union of India (Mandatory disclosure of sources of income for candidates & spouses)", "1. லோக் பிரஹாரி எதிர் இந்திய ஒன்றியம் (வேட்பாளர் மற்றும் வாழ்க்கைத் துணையின் வருமான ஆதாரங்களை வெளியிட கட்டாயம்)", 2018),
            ("2. Election Commission v. Saka Venkata Rao (Jurisdiction of High Courts over Election Commission)", "2. தேர்தல் ஆணையம் எதிர் சாகா வெங்கட ராவ் (தேர்தல் ஆணையத்தின் மீது உயர்நீதிமன்றங்களின் அதிகார வரம்பு)", 1953),
            ("3. Manoj Narula v. Union of India (Prime Minister and Chief Ministers should not appoint persons with criminal records)", "3. மனோஜ் நருலா எதிர் இந்திய ஒன்றியம் (குற்றப்பின்னணி உள்ளவர்களை பிரதமரும் முதல்வர்களும் அமைச்சர்களாக நியமிக்கக்கூடாது)", 2014),
            ("4. Resurgence India v. Election Commission of India (Voter's right to know - blank affidavits cannot be accepted)", "4. ரீசர்ஜன்ஸ் இந்தியா எதிர் தேர்தல் ஆணையம் (வெற்று பிரமாணப் பத்திரங்களை ஏற்கக்கூடாது - வாக்காளரின் அறியும் உரிமை)", 2013)
        ],
        # Order: Saka Venkata Rao (1953) -> Resurgence India (Sept 2013) -> Manoj Narula (Aug 2014) -> Lok Prahari (Feb 2018)
        # Sequence: 2 -> 4 -> 3 -> 1
        "correct_seq": [2, 4, 3, 1],
        "distractors": [[4, 2, 3, 1], [2, 3, 4, 1], [3, 2, 4, 1]],
        "explanation_en": "The correct chronological sequence of judgments is: 2. Saka Venkata Rao case (1953) -> 4. Resurgence India judgment barring blank affidavits (2013) -> 3. Manoj Narula case on constitutional morality in appointments (2014) -> 1. Lok Prahari judgment on source of income disclosure (2018).",
        "explanation_ta": "முக்கிய தீர்ப்புகளின் சரியான காலவரிசை: 2. சாகா வெங்கட ராவ் வழக்கு (1953) -> 4. ரீசர்ஜன்ஸ் இந்தியா தீர்ப்பு (2013) -> 3. மனோஜ் நருலா தீர்ப்பு (2014) -> 1. லோக் பிரஹாரி தீர்ப்பு (2018).",
        "tnpsc_tip": "Resurgence India (2013) made it mandatory to reject nomination papers if affidavit columns are left blank.",
        "revision_fact": "In Resurgence India (2013), the Supreme Court ruled that leaving blank columns in Form 26 violates voters' fundamental right under Article 19(1)(a).",
        "difficulty": "Hard"
    },

    # 16. Rajya Sabha Election Reforms
    {
        "id": "ER_C_016",
        "title": "Rajya Sabha Election System Reforms",
        "events": [
            ("1. Supreme Court strikes down applicability of NOTA in Rajya Sabha elections", "1. மாநிலங்களவைத் தேர்தலில் நோட்டா முறை பொருந்தாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது", 2018),
            ("2. Introduction of Open Ballot voting system for Rajya Sabha elections", "2. மாநிலங்களவைத் தேர்தல்களுக்கு திறந்த வாக்குச்சீட்டு முறை அறிமுகம்", 2003),
            ("3. Supreme Court upholds constitutionality of open ballot in Kuldip Nayar case", "3. குல்தீப் நய்யார் வழக்கில் திறந்த வாக்குச்சீட்டு முறையின் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை உச்ச நீதிமன்றம் உறுதி செய்தது", 2006),
            ("4. Removal of domicile/residence requirement for contesting Rajya Sabha elections", "4. மாநிலங்களவைத் தேர்தலில் போட்டியிட அந்தந்த மாநிலத்தில் வசிக்க வேண்டும் என்ற நிபந்தனை நீக்கம்", 2003)
        ],
        # Note: 2 & 4 happened in Representation of the People (Amendment) Act 2003 (enacted Aug 2003). Domicile removal & open ballot were enacted together, Kuldip Nayar (2006) -> Shailesh Parmar NOTA (2018).
        # Let's present: 4 (Domicile removed 2003) -> 2 (Open ballot 2003) -> 3 (Kuldip Nayar 2006) -> 1 (NOTA barred 2018)
        # Sequence: 4 -> 2 -> 3 -> 1
        "correct_seq": [4, 2, 3, 1],
        "distractors": [[2, 4, 3, 1], [4, 3, 2, 1], [3, 4, 2, 1]],
        "explanation_en": "The correct chronological sequence of Rajya Sabha election reforms is: 4. Domicile requirement removed (2003) -> 2. Open ballot introduced via same RPA Amendment (2003) -> 3. Constitutional challenge dismissed in Kuldip Nayar (2006) -> 1. NOTA removed from Rajya Sabha polls in Shailesh Parmar case (2018).",
        "explanation_ta": "மாநிலங்களவை தேர்தல் சீர்திருத்தங்களின் சரியான காலவரிசை: 4. இருப்பிடத் தகுதி நீக்கம் (2003) -> 2. திறந்த வாக்குச்சீட்டு அறிமுகம் (2003) -> 3. குல்தீப் நய்யார் வழக்கு தீர்ப்பு (2006) -> 1. மாநிலங்களவையில் நோட்டா ரத்து (2018).",
        "tnpsc_tip": "In 2003, domicile requirement was removed and open ballot was introduced for Rajya Sabha; upheld in 2006.",
        "revision_fact": "The Supreme Court in Shailesh Manubhai Parmar (2018) held that NOTA was meant only for direct universal adult suffrage elections.",
        "difficulty": "Medium"
    },

    # 17. Evolution of Voting Age and Electoral Roll Enrolment
    {
        "id": "ER_C_017",
        "title": "Evolution of Voting Franchise and Electoral Registration Milestones",
        "events": [
            ("1. Election Laws (Amendment) Act enabling voluntary linking of Electoral Roll with Aadhaar", "1. வாக்காளர் பட்டியலுடன் ஆதாரை விருப்பத்தின் பேரில் இணைக்க அனுமதிக்கும் தேர்தல் சட்டங்கள் (திருத்த) சட்டம்", 2021),
            ("2. Enactment of Representation of the People Act 1950 governing voter eligibility and registration", "2. வாக்காளர் தகுதி மற்றும் பதிவை ஒழுங்குபடுத்தும் 1950 மக்கள் பிரதிநிதித்துவச் சட்டம் இயற்றப்பட்டது", 1950),
            ("3. Notification of Constitution (61st Amendment) Act lowering voting age from 21 to 18", "3. வாக்களிக்கும் வயதை 21-லிருந்து 18 ஆக குறைக்கும் 61-வது அரசியலமைப்பு திருத்தச் சட்டம் அமலுக்கு வந்தது", 1989),
            ("4. Introduction of Form 6B for capturing Aadhaar authentication data voluntarily", "4. ஆதார் அங்கீகாரத் தரவை விருப்பத்தின் பேரில் பதிவு செய்வதற்கான படிவம் 6B அறிமுகம்", 2022)
        ],
        # Order: RPA 1950 (1950) -> 61st Amendment enforcement (March 1989) -> Election Laws Amendment (Dec 2021) -> Form 6B notified (Aug 2022)
        # Sequence: 2 -> 3 -> 1 -> 4
        "correct_seq": [2, 3, 1, 4],
        "distractors": [[3, 2, 1, 4], [2, 1, 3, 4], [1, 2, 3, 4]],
        "explanation_en": "The correct chronological sequence is: 2. RPA 1950 enacted (1950) -> 3. 61st Amendment comes into force (March 1989) -> 1. Election Laws (Amendment) Act passed (December 2021) -> 4. Form 6B introduced for Aadhaar linking (August 2022).",
        "explanation_ta": "சரியான காலவரிசை: 2. 1950 மக்கள் பிரதிநிதித்துவச் சட்டம் இயற்றப்பட்டது (1950) -> 3. 61-வது திருத்தச் சட்டம் அமலானது (1989) -> 1. தேர்தல் சட்டங்கள் (திருத்த) சட்டம் (2021) -> 4. படிவம் 6B அறிமுகம் (2022).",
        "tnpsc_tip": "61st Amendment was passed in 1988 and came into force on 28 March 1989.",
        "revision_fact": "The 61st Amendment Act amended Article 326 of the Constitution to replace 'twenty-one years' with 'eighteen years'.",
        "difficulty": "Medium"
    },

    # 18. Political Party Deregistration & Delisting Drives
    {
        "id": "ER_C_018",
        "title": "Party Registration Jurisprudence and Delisting Operations",
        "events": [
            ("1. Supreme Court rules ECI has no inherent power to deregister parties except in fraud/cessation (Indian National Congress v. Institute of Social Welfare)", "1. மோசடி அல்லது சட்டம் மீறல் தவிர கட்சிகளை பதிவுநீக்கம் செய்ய தேர்தல் ஆணையத்திற்கு அதிகாரம் இல்லை என உச்ச நீதிமன்றம் தீர்ப்பு", 2002),
            ("2. Insertion of Section 29A in RPA 1951 providing procedure for registration of political parties", "2. அரசியல் கட்சிகள் பதிவுக்கான நடைமுறையை வழங்கும் பிரிவு 29A சேர்க்கப்பட்டது", 1988),
            ("3. ECI launches massive nationwide clean-up drive delisting hundreds of inactive Registered Unrecognized Political Parties (RUPPs)", "3. செயல்படாத பதிவு செய்யப்பட்ட அங்கீகரிக்கப்படாத கட்சிகளை (RUPP) நீக்கும் பெரும் நடவடிக்கையை தேர்தல் ஆணையம் மேற்கொண்டது", 2022),
            ("4. ECI delists 255 dormant political parties from its official register for the first time", "4. தேர்தல் ஆணையம் முதன்முறையாக 255 செயல்படாத கட்சிகளை தனது அதிகாரப்பூர்வ பதிவேட்டில் இருந்து நீக்கியது", 2016)
        ],
        # Order: Sec 29A (1988) -> Indian National Congress v. ISW (2002) -> First delisting 255 parties (2016) -> Massive delisting drive (2022)
        # Sequence: 2 -> 1 -> 4 -> 3
        "correct_seq": [2, 1, 4, 3],
        "distractors": [[1, 2, 4, 3], [2, 4, 1, 3], [4, 2, 1, 3]],
        "explanation_en": "The correct chronological sequence is: 2. Section 29A inserted in RPA (1988) -> 1. SC ruling in Indian National Congress v. Institute of Social Welfare (2002) -> 4. First batch of 255 dormant parties delisted (2016) -> 3. Major clean-up drive delisting RUPPs (2022).",
        "explanation_ta": "சரியான காலவரிசை: 2. பிரிவு 29A சேர்க்கப்பட்டது (1988) -> 1. காங்கிரஸ் எதிர் இன்ஸ்டிடியூட் ஆஃப் சோஷியல் வெல்பேர் தீர்ப்பு (2002) -> 4. 255 கட்சிகள் முதல் கட்ட நீக்கம் (2016) -> 3. RUPP கட்சிகள் பெருமளவு நீக்க நடவடிக்கை (2022).",
        "tnpsc_tip": "ECI can register parties under Sec 29A, but lacks statutory power to deregister them (INC v. ISW, 2002).",
        "revision_fact": "The ECI overcomes the lack of deregistration power by exercising its power to 'delist' inactive parties from the list of recognized/registered entities.",
        "difficulty": "Hard"
    },

    # 19. Simultaneous Elections (One Nation One Election) Progression
    {
        "id": "ER_C_019",
        "title": "History and Progress of Simultaneous Elections in India",
        "events": [
            ("1. Law Commission of India 170th Report recommends holding simultaneous elections", "1. ஒரே நேரத்தில் தேர்தல் நடத்த இந்திய சட்ட ஆணையத்தின் 170-வது அறிக்கை பரிந்துரைத்தது", 1999),
            ("2. Disruption of simultaneous election cycle due to premature dissolution of Lok Sabha & State Assemblies", "2. மக்களவை மற்றும் மாநில சட்டமன்றங்கள் முன்கூட்டியே கலைக்கப்பட்டதால் ஒரே நேர தேர்தல் சுழற்சி சிதைந்தது", 1967),
            ("3. High-Level Committee on Simultaneous Elections under Ram Nath Kovind submits its report to President", "3. ராம் நாத் கோவிந்த் தலைமையிலான ஒரே நாடு ஒரே தேர்தல் உயர்மட்டக் குழு தனது அறிக்கையை குடியரசுத் தலைவரிடம் சமர்ப்பித்தது", 2024),
            ("4. Law Commission Working Draft Report under Justice B.S. Chauhan recommends constitutional framework for simultaneous polls", "4. நீதிபதி பி.எஸ். சவுகான் தலைமையிலான சட்ட ஆணைய வரைவு அறிக்கை ஒரே நேர தேர்தலுக்கான அரசியலமைப்பு கட்டமைப்பை பரிந்துரைத்தது", 2018)
        ],
        # Order: Disruption (1967-1970) -> 170th Report (1999) -> Chauhan Draft Report (2018) -> Kovind Committee (2024)
        # Sequence: 2 -> 1 -> 4 -> 3
        "correct_seq": [2, 1, 4, 3],
        "distractors": [[1, 2, 4, 3], [2, 4, 1, 3], [4, 2, 1, 3]],
        "explanation_en": "The correct chronological progression of simultaneous elections discourse is: 2. Disruption of initial synchronized cycle (1967) -> 1. Law Commission 170th Report recommendation (1999) -> 4. Law Commission Draft Report under Justice Chauhan (2018) -> 3. High-Level Committee report under Ram Nath Kovind (March 2024).",
        "explanation_ta": "ஒரே நாடு ஒரே தேர்தல் வரலாற்றின் காலவரிசை: 2. ஒரே நேர தேர்தல் சுழற்சி சிதைவு (1967) -> 1. 170-வது சட்ட ஆணைய அறிக்கை பரிந்துரை (1999) -> 4. நீதிபதி சவுகான் வரைவு அறிக்கை (2018) -> 3. ராம் நாத் கோவிந்த் உயர்மட்டக் குழு அறிக்கை சமர்ப்பிப்பு (2024).",
        "tnpsc_tip": "Simultaneous elections were held in 1952, 1957, 1962, and 1967.",
        "revision_fact": "The High-Level Committee on One Nation One Election submitted an 18,626-page report on 14 March 2024 proposing amendments to Article 83 and 172.",
        "difficulty": "Medium"
    },

    # 20. Postal Voting & Inclusive Ballot Reforms
    {
        "id": "ER_C_020",
        "title": "Expansion of Postal Ballot and Voting Accessibility",
        "events": [
            ("1. Extension of postal ballot facility to absentee senior citizens (above 85 years) and PwD voters at home", "1. 85 வயதுக்கு மேற்பட்ட முதியவர்கள் மற்றும் மாற்றுத்திறனாளிகளுக்கு வீட்டிலிருந்தே தபால் வாக்கு வசதி விரிவாக்கம்", 2024),
            ("2. Introduction of Electronically Transmitted Postal Ballot System (ETPBS) for service voters", "2. இராணுவ/பணி வாக்காளர்களுக்கான மின்னணு அஞ்சல் வாக்கு முறை (ETPBS) அறிமுகம்", 2016),
            ("3. Notification allowing Essential Services personnel to vote via postal ballot", "3. அத்தியாவசிய சேவைப் பணியாளர்கள் தபால் வாக்கு மூலம் வாக்களிக்க அனுமதிக்கும் அறிவிப்பு", 2019),
            ("4. Initial provision of postal ballot under Rule 18 of Conduct of Elections Rules 1961", "4. 1961 தேர்தல் நடத்தை விதிகள் விதி 18-ன் கீழ் தபால் வாக்களிப்பதற்கான ஆரம்ப ஏற்பாடு", 1961)
        ],
        # Order: Conduct of Election Rules (1961) -> ETPBS (2016) -> Essential Services (2019) -> 85+ Home voting (2024)
        # Sequence: 4 -> 2 -> 3 -> 1
        "correct_seq": [4, 2, 3, 1],
        "distractors": [[2, 4, 3, 1], [4, 3, 2, 1], [3, 4, 2, 1]],
        "explanation_en": "The correct chronological sequence of postal ballot accessibility is: 4. Initial provision in Conduct of Elections Rules (1961) -> 2. ETPBS introduced for service voters (2016) -> 3. Facility extended to essential services personnel (2019) -> 1. Home postal voting extended to senior citizens aged 85+ and PwDs (2024).",
        "explanation_ta": "தபால் வாக்கு வசதி விரிவாக்கத்தின் சரியான காலவரிசை: 4. 1961 விதிகளின் கீழ் ஆரம்ப ஏற்பாடு (1961) -> 2. ETPBS மின்னணு அஞ்சல் வாக்கு முறை (2016) -> 3. அத்தியாவசிய சேவைகளுக்கு விரிவாக்கம் (2019) -> 1. 85+ வயது முதியவர்களுக்கு வீட்டிலிருந்தே தபால் வாக்கு முறை (2024).",
        "tnpsc_tip": "ETPBS was launched in 2016. In 2024, the age threshold for home postal ballot was adjusted from 80 to 85 years.",
        "revision_fact": "Under the amended Conduct of Elections Rules in early 2024, the age eligibility for home voting for senior citizens was set at 85+.",
        "difficulty": "Hard"
    },

    # 21. Campaign Expenditure Ceiling Hikes
    {
        "id": "ER_C_021",
        "title": "Hikes in Parliamentary Election Expenditure Ceilings",
        "events": [
            ("1. Lok Sabha election expenditure limit raised to Rs 95 Lakhs for bigger states", "1. பெரிய மாநிலங்களில் மக்களவை தேர்தல் செலவு வரம்பு ரூ.95 லட்சமாக உயர்த்தப்பட்டது", 2022),
            ("2. Lok Sabha election expenditure limit raised to Rs 40 Lakhs for bigger states", "2. பெரிய மாநிலங்களில் மக்களவை தேர்தல் செலவு வரம்பு ரூ.40 லட்சமாக உயர்த்தப்பட்டது", 2011),
            ("3. Lok Sabha election expenditure limit raised to Rs 70 Lakhs for bigger states", "3. பெரிய மாநிலங்களில் மக்களவை தேர்தல் செலவு வரம்பு ரூ.70 லட்சமாக உயர்த்தப்பட்டது", 2014),
            ("4. 10% interim increase in expenditure ceiling due to COVID-19 pandemic protocols", "4. கோவிட் பெருந்தொற்று முன்னெச்சரிக்கைகள் காரணமாக தேர்தல் செலவு வரம்பில் 10% இடைக்கால உயர்வு", 2020)
        ],
        # Order: 40L (2011) -> 70L (2014) -> 10% COVID hike (2020) -> 95L Harish Kumar Committee (2022)
        # Sequence: 2 -> 3 -> 4 -> 1
        "correct_seq": [2, 3, 4, 1],
        "distractors": [[3, 2, 4, 1], [2, 4, 3, 1], [4, 2, 3, 1]],
        "explanation_en": "The correct chronological sequence of expenditure limit increases is: 2. Raised to Rs 40 Lakhs (2011) -> 3. Raised to Rs 70 Lakhs (2014) -> 4. 10% interim enhancement during COVID-19 (2020) -> 1. Raised to Rs 95 Lakhs based on Harish Kumar Committee (2022).",
        "explanation_ta": "தேர்தல் செலவு வரம்பு உயர்வின் சரியான காலவரிசை: 2. ரூ.40 லட்சமாக உயர்வு (2011) -> 3. ரூ.70 லட்சமாக உயர்வு (2014) -> 4. கோவிட் பெருந்தொற்று காலத்தில் 10% இடைக்கால உயர்வு (2020) -> 1. ரூ.95 லட்சமாக உயர்வு (2022).",
        "tnpsc_tip": "Current Lok Sabha limit for bigger states is Rs 95 Lakhs; for Assembly it is Rs 40 Lakhs (revised in Jan 2022).",
        "revision_fact": "The Harish Kumar and Umesh Sinha Committee set up by the ECI examined expenditure ceilings and recommended the 2022 revisions.",
        "difficulty": "Medium"
    },

    # 22. Women's Reservation Legislative Journey
    {
        "id": "ER_C_022",
        "title": "Legislative Milestones of Women's Reservation in India",
        "events": [
            ("1. Rajya Sabha passes the Constitution (108th Amendment) Bill for 33% women's reservation", "1. மகளிருக்கு 33% இடஒதுக்கீடு வழங்கும் 108-வது அரசியலமைப்பு திருத்த மசோதாவை மாநிலங்களவை நிறைவேற்றியது", 2010),
            ("2. Constitution 73rd and 74th Amendment Acts mandate 33% reservation for women in Panchayats & Municipalities", "2. ஊராட்சி மற்றும் நகராட்சிகளில் பெண்களுக்கு 33% இடஒதுக்கீடு கட்டாயமாக்கிய 73 மற்றும் 74-வது அரசியலமைப்பு திருத்தங்கள்", 1992),
            ("3. President gives assent to the Constitution (106th Amendment) Act (Nari Shakti Vandan Adhiniyam)", "3. நாரி சக்தி வந்தன் அதினியம் (106-வது அரசியலமைப்பு திருத்தச் சட்டம்) குடியரசுத் தலைவர் ஒப்புதல் பெற்றது", 2023),
            ("4. Geeta Mukherjee Joint Parliamentary Committee examines Women's Reservation Bill", "4. மகளிர் இடஒதுக்கீடு மசோதாவை ஆய்வு செய்த கீதா முகர்ஜி நாடாளுமன்றக் கூட்டுக்குழு", 1996)
        ],
        # Order: 73rd/74th (1992) -> Geeta Mukherjee (1996) -> Rajya Sabha passed 108th (2010) -> 106th Amendment (2023)
        # Sequence: 2 -> 4 -> 1 -> 3
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "explanation_en": "The correct chronological journey of women's political reservation is: 2. 73rd & 74th Amendments for local bodies (1992) -> 4. Geeta Mukherjee Committee report (1996) -> 1. Rajya Sabha passes 108th Bill (2010) -> 3. 106th Amendment Act enacted (September 2023).",
        "explanation_ta": "மகளிர் இடஒதுக்கீட்டு வரலாற்றின் சரியான காலவரிசை: 2. உள்ளாட்சி அமைப்புகளில் 33% இடஒதுக்கீடு 73/74 திருத்தங்கள் (1992) -> 4. கீதா முகர்ஜி குழு அறிக்கை (1996) -> 1. மாநிலங்களவையில் 108-வது மசோதா நிறைவேறியது (2010) -> 3. 106-வது சட்டத்திருத்தம் இயற்றப்பட்டது (2023).",
        "tnpsc_tip": "The Geeta Mukherjee Committee (1996) recommended 33% reservation for women including OBC reservation if possible.",
        "revision_fact": "Article 330A and Article 332A were inserted into the Constitution by the 106th Amendment Act 2023.",
        "difficulty": "Medium"
    },

    # 23. Candidate Form & Affidavit Reforms
    {
        "id": "ER_C_023",
        "title": "Evolution of Candidate Nomination Forms and Rules",
        "events": [
            ("1. Supreme Court mandates candidates publish criminal antecedents thrice in newspapers and TV channels", "1. வேட்பாளர்கள் தங்கள் குற்றப்பின்னணியை செய்தித்தாள்கள் மற்றும் தொலைக்காட்சிகளில் மூன்று முறை விளம்பரப்படுத்த உச்ச நீதிமன்றம் கட்டாயமாக்கியது", 2018),
            ("2. First introduction of statutory Form 26 under Conduct of Elections Rules for declaration of criminal cases", "2. குற்ற வழக்குகளை அறிவிப்பதற்காக தேர்தல் நடத்தை விதிகளின் கீழ் முதன்முதலில் சட்டப்பூர்வ படிவம் 26 அறிமுகம்", 2002),
            ("3. Notification amending Form 26 to include declaration of offshore assets and PAN status of foreign investments", "3. வெளிநாட்டு சொத்துக்கள் மற்றும் பான் அட்டை விவரங்களை அறிவிக்க படிவம் 26 திருத்தப்பட்டது", 2019),
            ("4. ECI mandates photographs of candidates to be printed alongside party symbol on EVM ballot units", "4. EVM வாக்கு இயந்திரங்களில் கட்சி சின்னத்துடன் வேட்பாளரின் புகைப்படத்தையும் அச்சிட தேர்தல் ஆணையம் உத்தரவு", 2015)
        ],
        # Order: Form 26 (2002) -> Photos on ballot (2015) -> 3x newspaper publishing (2018) -> Offshore assets in Form 26 (2019)
        # Sequence: 2 -> 4 -> 1 -> 3
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "explanation_en": "The correct chronological sequence of nomination reforms is: 2. Form 26 introduced following ADR verdict (2002) -> 4. Candidate photos on EVM ballot paper (May 2015) -> 1. Mandatory triple advertisement of criminal cases in media (September 2018) -> 3. Form 26 amended to include offshore assets (February 2019).",
        "explanation_ta": "வேட்புமனு சீர்திருத்தங்களின் சரியான காலவரிசை: 2. படிவம் 26 பிரமாணப் பத்திரம் அறிமுகம் (2002) -> 4. EVM வாக்குச்சீட்டில் வேட்பாளரின் புகைப்படம் (2015) -> 1. குற்றப்பின்னணியை ஊடகங்களில் 3 முறை விளம்பரப்படுத்த உத்தரவு (2018) -> 3. வெளிநாட்டு சொத்து விவரங்களை சேர்க்க படிவம் 26 திருத்தம் (2019).",
        "tnpsc_tip": "Candidate photographs on EVM ballot units were introduced in May 2015 to avoid confusion between namesakes.",
        "revision_fact": "Candidates with criminal cases must publish declarations in newspapers and television on three separate dates during the campaign period.",
        "difficulty": "Hard"
    },

    # 24. Exit Poll and Opinion Poll Regulations
    {
        "id": "ER_C_024",
        "title": "Milestones in Regulation of Pre-Poll and Exit Poll Media Broadcasts",
        "events": [
            ("1. Supreme Court stays ECI's administrative guidelines regulating pre-poll and exit surveys", "1. தேர்தலுக்கு முந்தைய மற்றும் பிந்தைய கருத்துக்கணிப்புகளை ஒழுங்குபடுத்திய தேர்தல் ஆணையத்தின் வழிகாட்டுதல்களுக்கு உச்ச நீதிமன்றம் இடைக்கால தடை விதித்தது", 1999),
            ("2. ECI issues initial guidelines prohibiting telecast of opinion polls and exit polls during election cycles", "2. தேர்தல் காலங்களில் கருத்துக் கணிப்புகளை ஒளிபரப்ப தடை விதித்து தேர்தல் ஆணையம் ஆரம்ப வழிகாட்டுதல்களை வெளியிட்டது", 1998),
            ("3. ECI prohibits display of election matters including opinion polls during 48-hour silent period under amended Sec 126", "3. திருத்தப்பட்ட பிரிவு 126-ன் கீழ் அமைதி காலத்தில் (48 மணி நேரம்) தொலைக்காட்சி உள்ளிட்ட மின்னணு ஊடகங்களில் கருத்துக்கணிப்பு வெளியிட தடை", 2014),
            ("4. Parliament inserts Section 126A into RPA 1951 permanently banning exit polls during all voting phases", "4. அனைத்து வாக்குப்பதிவு கட்டங்களிலும் எக்சிட் போல் நடத்த தடை விதிக்கும் பிரிவு 126A-ஐ நாடாளுமன்றம் 1951 சட்டத்தில் சேர்த்தது", 2009)
        ],
        # Order: ECI guidelines (1998) -> SC stay (1999) -> Sec 126A passed (2009) -> Sec 126 48-hour electronic media enforcement (2014)
        # Sequence: 2 -> 1 -> 4 -> 3
        "correct_seq": [2, 1, 4, 3],
        "distractors": [[1, 2, 4, 3], [2, 4, 1, 3], [4, 2, 1, 3]],
        "explanation_en": "The correct chronological sequence of polling regulation milestones is: 2. ECI guidelines on polls (1998) -> 1. Supreme Court stays ECI guidelines (1999) -> 4. Section 126A enacted by Parliament banning exit polls (2009) -> 3. Section 126 prohibition extended to all electronic media in 48-hour silent window (2014).",
        "explanation_ta": "கருத்துக்கணிப்பு ஒழுங்குமுறைகளின் சரியான காலவரிசை: 2. தேர்தல் ஆணைய வழிகாட்டுதல்கள் (1998) -> 1. உச்ச நீதிமன்ற தடை (1999) -> 4. எக்சிட் போல் தடை செய்யும் பிரிவு 126A சட்டம் (2009) -> 3. 48 மணி நேர அமைதிக்கால தடை மின்னணு ஊடகங்களுக்கும் நீட்டிப்பு (2014).",
        "tnpsc_tip": "Exit polls are banned under Section 126A of RPA 1951 from the beginning of voting in the first phase until half an hour after polling closes in the last phase.",
        "revision_fact": "Violation of Section 126A is punishable with imprisonment for a term up to two years or with fine or both.",
        "difficulty": "Hard"
    },

    # 25. High-Profile CEC & EC Appointment Reforms
    {
        "id": "ER_C_025",
        "title": "Reforms in the Appointment Process of Election Commissioners",
        "events": [
            ("1. Supreme Court Constitution Bench in Anoop Baranwal directs Collegium consisting of PM, CJI, and Leader of Opposition", "1. பிரதமர், உச்ச நீதிமன்ற தலைமை நீதிபதி, எதிர்க்கட்சித் தலைவர் அடங்கிய கொலீஜியம் முறைக்கு உத்தரவிட்ட அனூப் பரன்வால் தீர்ப்பு", 2023),
            ("2. Dinesh Goswami Committee recommends multi-member consultation for CEC appointment", "2. தலைமை தேர்தல் ஆணையர் நியமனத்திற்கு பலதரப்பு ஆலோசனை முறையை பரிந்துரைத்த தினேஷ் கோஸ்வாமி குழு", 1990),
            ("3. Parliament enacts Chief Election Commissioner and other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act replacing CJI with a Union Cabinet Minister", "3. கொலீஜியத்தில் உச்ச நீதிமன்ற தலைமை நீதிபதிக்கு பதிலாக மத்திய அமைச்சரை சேர்த்து நாடாளுமன்றம் புதிய சட்டத்தை இயற்றியது", 2023),
            ("4. Law Commission 255th Report reiterates three-member collegium for appointing Election Commissioners", "4. தேர்தல் ஆணையர்களை நியமிக்க மூன்று பேர் கொண்ட கொலீஜியத்தை மீண்டும் பரிந்துரைத்த சட்ட ஆணையத்தின் 255-வது அறிக்கை", 2015)
        ],
        # Order: Goswami Committee (1990) -> Law Commission 255th (2015) -> Anoop Baranwal ruling (March 2023) -> Parliament Act (December 2023)
        # Sequence: 2 -> 4 -> 1 -> 3
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "explanation_en": "The correct chronological progression of appointment reforms is: 2. Dinesh Goswami Committee recommendations (1990) -> 4. Law Commission 255th Report recommendation (2015) -> 1. Supreme Court ruling in Anoop Baranwal (March 2023) -> 3. Parliament enacts CEC and other ECs Act (December 2023).",
        "explanation_ta": "தேர்தல் ஆணையர்கள் நியமன சீர்திருத்தங்களின் காலவரிசை: 2. தினேஷ் கோஸ்வாமி குழு பரிந்துரை (1990) -> 4. 255-வது சட்ட ஆணைய அறிக்கை (2015) -> 1. அனூப் பரன்வால் உச்ச நீதிமன்ற தீர்ப்பு (மார்ச் 2023) -> 3. புதிய தலைமை தேர்தல் ஆணையர் மற்றும் தேர்தல் ஆணையர்கள் சட்டம் இயற்றப்பட்டது (டிசம்பர் 2023).",
        "tnpsc_tip": "Anoop Baranwal ruling was delivered in March 2023; the new Parliamentary Act replacing CJI with a Union Minister was passed in December 2023.",
        "revision_fact": "Under the 2023 Act, the Selection Committee consists of the Prime Minister (Chairperson), the Leader of the Opposition in Lok Sabha, and a Union Cabinet Minister.",
        "difficulty": "Hard"
    }
]

from er_mcq_helper import make_er_q

# desired key mapping:
# 25 questions: targets 6 A, 7 B, 6 C, 6 D
desired_keys = ['B', 'C', 'D', 'A'] * 6 + ['B']  # 7 B, 6 C, 6 D, 6 A

def build_chronology_questions():
    questions = []
    
    for i, item in enumerate(raw_chronology_data):
        qid = item["id"]
        desired_key = desired_keys[i]
        
        # Build stem: instruction + 4 numbered events
        events = item["events"]
        stem_en = f"Arrange the following milestones concerning {item['title'].lower()} in correct chronological order:\n"
        stem_en += "\n".join([e[0] for e in events]) + "\nSelect the correct answer using the codes given below:"
        
        stem_ta = f"கீழ்க்கண்ட {item['title']} தொடர்பான நிகழ்வுகளை சரியான காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        stem_ta += "\n".join([e[1] for e in events]) + "\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:"
        
        correct_seq_str = " - ".join(str(d) for d in item["correct_seq"])
        distractor_seq_strs = [" - ".join(str(d) for d in item["distractors"])]
        # Actually distractors has 3 items
        d_strs = [" - ".join(str(d) for d in d_seq) for d_seq in item["distractors"]]
        
        # Place correct_seq at desired_key
        key_index = {"A": 0, "B": 1, "C": 2, "D": 3}[desired_key]
        opt_texts = d_strs[:]
        opt_texts.insert(key_index, correct_seq_str)
        
        why_en = {}
        why_ta = {}
        for opt_id in ["A", "B", "C", "D"]:
            idx = {"A": 0, "B": 1, "C": 2, "D": 3}[opt_id]
            if opt_id == desired_key:
                why_en[opt_id] = f"Option {opt_id} is the correct chronological sequence ({correct_seq_str})."
                why_ta[opt_id] = f"தெரிவு {opt_id} சரியான காலவரிசை வரிசையாகும் ({correct_seq_str})."
            else:
                why_en[opt_id] = f"Option {opt_id} ({opt_texts[idx]}) is incorrect because the events did not occur in this sequential order."
                why_ta[opt_id] = f"தெரிவு {opt_id} ({opt_texts[idx]}) தவறானது, ஏனெனில் நிகழ்வுகள் இந்த வரிசையில் நிகழவில்லை."
        
        tip_en = item["tnpsc_tip"]
        tip_ta = f"நினைவில் கொள்க: {item['tnpsc_tip']}"
        fact_en = item["revision_fact"]
        fact_ta = f"முக்கிய தகவல்: {item['revision_fact']}"
        
        q = make_er_q(
            qid=qid,
            diff=item["difficulty"],
            qtype="Chronology",
            subtopic="Chronology of Electoral Reforms",
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=opt_texts[0],
            ta_a=opt_texts[0],
            en_b=opt_texts[1],
            ta_b=opt_texts[1],
            en_c=opt_texts[2],
            ta_c=opt_texts[2],
            en_d=opt_texts[3],
            ta_d=opt_texts[3],
            correct_key=desired_key,
            exp_en=item["explanation_en"],
            exp_ta=item["explanation_ta"],
            why_a_en=why_en["A"],
            why_a_ta=why_ta["A"],
            why_b_en=why_en["B"],
            why_b_ta=why_ta["B"],
            why_c_en=why_en["C"],
            why_c_ta=why_ta["C"],
            why_d_en=why_en["D"],
            why_d_ta=why_ta["D"],
            tip_en=tip_en,
            tip_ta=tip_ta,
            fact_en=fact_en,
            fact_ta=fact_ta,
            tags=["polity", "electoral_reforms", "chronology"]
        )
        questions.append(q)
        
    return questions

def main():
    questions = build_chronology_questions()
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "electoral_reforms_chronology.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Generated {len(questions)} chronology questions in {out_file}")
    
    # 1. Run ChronologyValidator
    report = ChronologyValidator.validate_questions(questions)
    print("--- Chronology Validator Report ---")
    print(report.format_final_report())
    if not report.is_valid:
        print("Issues found:")
        for iss in report.issues:
            print(" -", iss)
            
    # 2. Run ContentValidator
    content_validator = ContentValidator()
    c_report = content_validator.validate_file(out_file)
    print("--- Content Validator Report ---")
    print(f"PASS: {c_report.is_valid} | Total: {c_report.total_audited}")
    print(f"Key Distribution: {c_report.key_distribution}")
    if not c_report.is_valid:
        for iss in c_report.issues:
            print(" -", iss.message)

if __name__ == "__main__":
    main()
