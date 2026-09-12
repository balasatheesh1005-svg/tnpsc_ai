# -*- coding: utf-8 -*-
"""
Grand Test Part 1 (Questions ER_GT_001 to ER_GT_050) for Electoral Reforms.
Covering:
- Constitutional framework (Part XV, Articles 324-329)
- RPA 1950 & RPA 1951 core provisions
- Electoral rolls, EPIC, and Delimitation
- Committees (Tarkunde, Goswami, Indrajit Gupta, Vohra, Law Commission)
- EVM architecture, security, and VVPAT safeguards
- NOTA and Model Code of Conduct
- Media Certification and Monitoring Committees (MCMC) & Paid News
"""
from er_mcq_helper import make_er_q

def get_gt_part1_questions():
    q_data = [
        # 1
        {
            "id": "ER_GT_001", "diff": "Easy", "sub": "Constitutional Framework",
            "en": "Under which Article of the Constitution does Parliament have the power to make provisions with respect to elections to either House of Parliament or to the House or either House of the Legislature of a State?",
            "ta": "நாடாளுமன்றத்தின் இரு அவைகளுக்கோ அல்லது மாநில சட்டமன்றத்திற்கோ நடைபெறும் தேர்தல்கள் குறித்து விதிகளை இயற்ற நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கும் அரசியலமைப்பு சரத்து எது?",
            "opts": [("Article 326", "சரத்து 326"), ("Article 327", "சரத்து 327"), ("Article 328", "சரத்து 328"), ("Article 325", "சரத்து 325")],
            "key": "B",
            "exp_en": "Article 327 empowers Parliament to enact laws regarding all matters relating to or in connection with elections to Parliament and State Legislatures, including the preparation of electoral rolls and delimitation.",
            "exp_ta": "சரத்து 327, வாக்காளர் பட்டியல் தயாரித்தல் மற்றும் தொகுதி மறுவரையறை உட்பட நாடாளுமன்ற மற்றும் மாநில சட்டமன்றத் தேர்தல்கள் தொடர்பான அனைத்து விவகாரங்களிலும் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
            "tip": "Article 327 = Parliament's power; Article 328 = State Legislature's power.",
            "fact": "Both the Representation of the People Acts (1950 and 1951) were enacted by Parliament under Article 327."
        },
        # 2
        {
            "id": "ER_GT_002", "diff": "Medium", "sub": "Constitutional Framework",
            "en": "Which Article of the Constitution confers power on the Legislature of a State to make laws with respect to elections to such Legislature, subject to Parliamentary laws?",
            "ta": "நாடாளுமன்ற சட்டங்களுக்கு உட்பட்டு, தனது மாநில சட்டமன்றத்திற்கான தேர்தல்கள் குறித்து சட்டங்களை இயற்ற மாநில சட்டமன்றத்திற்கு அதிகாரமளிக்கும் அரசியலமைப்பு சரத்து எது?",
            "opts": [("Article 325", "சரத்து 325"), ("Article 327", "சரத்து 327"), ("Article 328", "சரத்து 328"), ("Article 329", "சரத்து 329")],
            "key": "C",
            "exp_en": "Article 328 empowers State Legislatures to make provisions for elections to their own houses, in so far as provision in that behalf is not made by Parliament.",
            "exp_ta": "சரத்து 328, நாடாளுமன்றத்தால் விதிகள் உருவாக்கப்படாத இடங்களில், மாநில சட்டமன்றத் தேர்தல்கள் தொடர்பாக சட்டங்களை இயற்ற மாநில சட்டமன்றத்திற்கு அதிகாரமளிக்கிறது.",
            "tip": "Article 328 operates only in areas where Parliament has not legislated.",
            "fact": "Article 328 is subordinate to Article 327."
        },
        # 3
        {
            "id": "ER_GT_003", "diff": "Medium", "sub": "RPA 1950",
            "en": "Under the Representation of the People Act 1950, which statutory authority is responsible for the preparation and revision of electoral rolls in an assembly constituency?",
            "ta": "1950 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் கீழ், ஒரு சட்டமன்றத் தொகுதியில் வாக்காளர் பட்டியலைத் தயாரிப்பதற்கும் திருத்துவதற்கும் பொறுப்பான சட்டப்பூர்வ அதிகாரி யார்?",
            "opts": [("District Election Officer", "மாவட்ட தேர்தல் அதிகாரி"), ("Electoral Registration Officer", "வாக்காளர் பதிவு அதிகாரி"), ("Returning Officer", "தேர்தல் நடத்தும் அதிகாரி"), ("Chief Electoral Officer", "தலைமை தேர்தல் அதிகாரி")],
            "key": "B",
            "exp_en": "Under Section 22 of RPA 1950, the Electoral Registration Officer (ERO), appointed by the ECI in consultation with the state government, is statutorily responsible for preparing and revising electoral rolls.",
            "exp_ta": "1950 சட்டத்தின் பிரிவு 22-ன் கீழ், தேர்தல் ஆணையத்தால் நியமிக்கப்படும் வாக்காளர் பதிவு அதிகாரி (ERO), வாக்காளர் பட்டியலை தயாரிப்பதற்கும் திருத்துவதற்கும் சட்டப்பூர்வ பொறுப்பாவார்.",
            "tip": "ERO prepares rolls; Returning Officer (RO) conducts polls.",
            "fact": "An ERO is typically an officer of the rank of Sub-Divisional Magistrate (SDM) or Revenue Divisional Officer (RDO)."
        },
        # 4
        {
            "id": "ER_GT_004", "diff": "Hard", "sub": "RPA 1950",
            "en": "An appeal against an order of the Electoral Registration Officer under Section 22 or 23 of RPA 1950 lies to which authority?",
            "ta": "1950 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 22 அல்லது 23-ன் கீழ் வாக்காளர் பதிவு அதிகாரியின் உத்தரவுக்கு எதிரான மேல்முறையீடு எந்த அதிகாரியிடம் செய்யப்பட வேண்டும்?",
            "opts": [("Chief Electoral Officer", "தலைமை தேர்தல் அதிகாரி"), ("District Magistrate / District Election Officer", "மாவட்ட ஆட்சித் தலைவர் / மாவட்ட தேர்தல் அதிகாரி"), ("High Court", "உயர்நீதிமன்றம்"), ("Chief Election Commissioner", "தலைமை தேர்தல் ஆணையர்")],
            "key": "B",
            "exp_en": "Under Section 24 of RPA 1950, an appeal against an order of the ERO regarding inclusion or exclusion of names in the electoral roll lies to the District Magistrate or Additional District Magistrate.",
            "exp_ta": "1950 சட்டத்தின் பிரிவு 24-ன் கீழ், வாக்காளர் பட்டியலில் பெயர் சேர்த்தல் அல்லது நீக்குதல் தொடர்பான ERO-வின் உத்தரவுக்கு எதிரான மேல்முறையீடு மாவட்ட ஆட்சித் தலைவரிடம் (DM/DEO) செய்யப்படும்.",
            "tip": "A second appeal against the District Magistrate's order lies to the Chief Electoral Officer (CEO).",
            "fact": "Rule 27 of Registration of Electors Rules 1960 governs the detailed procedure for filing appeals."
        },
        # 5
        {
            "id": "ER_GT_005", "diff": "Easy", "sub": "Electoral Administration",
            "en": "At the state level, who supervises the preparation and revision of electoral rolls and the conduct of all elections under the overall superintendence of the ECI?",
            "ta": "மாநில அளவில், இந்திய தேர்தல் ஆணையத்தின் ஒட்டுமொத்த மேற்பார்வையின் கீழ் வாக்காளர் பட்டியல் தயாரித்தல் மற்றும் அனைத்து தேர்தல் பணிகளையும் மேற்பார்வையிடுபவர் யார்?",
            "opts": [("Chief Secretary of the State", "மாநில தலைமைச் செயலாளர்"), ("Chief Electoral Officer (CEO)", "தலைமை தேர்தல் அதிகாரி (CEO)"), ("State Election Commissioner", "மாநில தேர்தல் ஆணையர்"), ("Director General of Police", "காவல்துறை தலைமை இயக்குநர்")],
            "key": "B",
            "exp_en": "Under Section 13A of RPA 1950, the Chief Electoral Officer (CEO) of a State or Union Territory supervises the preparation, revision, and correction of all electoral rolls and the conduct of all Parliamentary and Assembly elections.",
            "exp_ta": "1950 சட்டத்தின் பிரிவு 13A-ன் கீழ், மாநில தலைமை தேர்தல் அதிகாரி (CEO) மாநில அளவில் வாக்காளர் பட்டியல் தயாரித்தல் மற்றும் நாடாளுமன்ற, சட்டமன்ற தேர்தல்களை மேற்பார்வையிடுகிறார்.",
            "tip": "Do not confuse Chief Electoral Officer (ECI's state head) with State Election Commissioner (Panchayat/Municipality elections head).",
            "fact": "The CEO is appointed by the Election Commission from a panel of senior IAS officers nominated by the State Government."
        },
        # 6
        {
            "id": "ER_GT_006", "diff": "Medium", "sub": "Electoral Administration",
            "en": "Who is designated as the District Election Officer (DEO) in most districts across India under Section 13AA of the Representation of the People Act 1950?",
            "ta": "1950 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 13AA-ன் கீழ் இந்தியாவின் பெரும்பாலான மாவட்டங்களில் மாவட்ட தேர்தல் அதிகாரியாக (DEO) நியமிக்கப்படுபவர் யார்?",
            "opts": [("Superintendent of Police", "காவல் கண்காணிப்பாளர்"), ("District Collector / District Magistrate", "மாவட்ட ஆட்சியர் / மாவட்ட மேஜிஸ்திரேட்"), ("Principal District Judge", "முதன்மை மாவட்ட நீதிபதி"), ("Sub-Collector", "சார்-ஆட்சியர்")],
            "key": "B",
            "exp_en": "Under Section 13AA of RPA 1950, the Election Commission in consultation with the State Government designates the District Magistrate / District Collector / Deputy Commissioner as the District Election Officer (DEO).",
            "exp_ta": "1950 சட்டத்தின் பிரிவு 13AA-ன் கீழ், தேர்தல் ஆணையம் மாநில அரசுடன் கலந்தாலோசித்து மாவட்ட ஆட்சியரை (Collector/DM) மாவட்ட தேர்தல் அதிகாரியாக (DEO) நியமிக்கிறது.",
            "tip": "The DEO coordinates and supervises all election work within the entire administrative district.",
            "fact": "Section 13AA was inserted into the 1950 Act by an amendment in 1966."
        },
        # 7
        {
            "id": "ER_GT_007", "diff": "Medium", "sub": "RPA 1951",
            "en": "Under Section 21 of the Representation of the People Act 1951, which officer is designated for each constituency to conduct elections and receive nominations?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 21-ன் கீழ், ஒவ்வொரு தொகுதிக்கும் தேர்தல்களை நடத்தவும் வேட்புமனுக்களைப் பெறவும் நியமிக்கப்படும் அதிகாரி யார்?",
            "opts": [("Electoral Registration Officer", "வாக்காளர் பதிவு அதிகாரி"), ("Returning Officer (RO)", "தேர்தல் நடத்தும் அதிகாரி (RO)"), ("Presiding Officer", "வாக்குச்சாவடி தலைமை அலுவலர்"), ("Zonal Officer", "மண்டல அலுவலர்")],
            "key": "B",
            "exp_en": "Section 21 of RPA 1951 provides that for every constituency, the ECI in consultation with the state government designates a Returning Officer (RO), who is in direct charge of receiving nominations, scrutinizing them, and declaring results.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 21-ன் கீழ், ஒவ்வொரு தொகுதிக்கும் தேர்தல் நடத்தும் அதிகாரி (Returning Officer) தேர்தல் ஆணையத்தால் நியமிக்கப்படுகிறார்; இவர் வேட்புமனுக்களை ஆய்வு செய்து முடிவுகளை அறிவிக்கிறார்.",
            "tip": "Returning Officer declares the final election result and issues Form 21C (Certificate of Election).",
            "fact": "For parliamentary constituencies, the District Collector usually acts as Returning Officer."
        },
        # 8
        {
            "id": "ER_GT_008", "diff": "Hard", "sub": "RPA 1951",
            "en": "Under Section 26 of the Representation of the People Act 1951, who has the statutory duty to preside over and conduct the poll at each individual polling station?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 26-ன் கீழ், ஒவ்வொரு வாக்குச்சாவடியிலும் தலைமை தாங்கி வாக்குப்பதிவை நடத்தும் சட்டப்பூர்வ கடமை கொண்டவர் யார்?",
            "opts": [("Sector Officer", "மண்டல அலுவலர்"), ("Presiding Officer (PRO)", "வாக்குச்சாவடி தலைமை அலுவலர் (PRO)"), ("Micro Observer", "மைக்ரோ பார்வையாளர்"), ("Polling Officer 1", "வாக்குப்பதிவு அலுவலர் 1")],
            "key": "B",
            "exp_en": "Under Section 26 of RPA 1951, the District Election Officer appoints a Presiding Officer for each polling station, who is in sole charge of maintaining order, conducting mock poll, and sealing EVMs.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 26-ன் கீழ், ஒவ்வொரு வாக்குச்சாவடிக்கும் ஒரு வாக்குச்சாவடி தலைமை அலுவலரை (Presiding Officer) மாவட்ட தேர்தல் அதிகாரி நியமிக்கிறார்.",
            "tip": "Presiding Officer maintains the Presiding Officer's Diary and issues Form 17C.",
            "fact": "A Presiding Officer must not be a person who has been employed by or on behalf of any candidate contesting the election."
        },
        # 9
        {
            "id": "ER_GT_009", "diff": "Medium", "sub": "Electoral Qualifications",
            "en": "What is the minimum age qualification prescribed under Article 84(b) of the Constitution to contest an election to the Council of States (Rajya Sabha)?",
            "ta": "அரசியலமைப்பின் சரத்து 84(b)-ன் கீழ் மாநிலங்களவை (ராஜ்யசபா) தேர்தலில் போட்டியிட நிர்ணயிக்கப்பட்டுள்ள குறைந்தபட்ச வயது என்ன?",
            "opts": [("25 years", "25 ஆண்டுகள்"), ("30 years", "30 ஆண்டுகள்"), ("35 years", "35 ஆண்டுகள்"), ("21 years", "21 ஆண்டுகள்")],
            "key": "B",
            "exp_en": "Under Article 84(b) of the Constitution, a person must not be less than 30 years of age to contest for a seat in the Rajya Sabha (and State Legislative Council under Article 173(b)). For Lok Sabha and Assembly, it is 25 years.",
            "exp_ta": "சரத்து 84(b)-ன் கீழ் மாநிலங்களவை தேர்தலில் போட்டியிட குறைந்தபட்சம் 30 வயது நிரம்பியவராக இருக்க வேண்டும். மக்களவை மற்றும் சட்டமன்றத்திற்கு 25 வயது.",
            "tip": "Panchayat/Municipality: 21; Lok Sabha/Assembly: 25; Rajya Sabha/Council: 30; President/VP/Governor: 35.",
            "fact": "The 18-year age applies to voting, not to contesting elections."
        },
        # 10
        {
            "id": "ER_GT_010", "diff": "Hard", "sub": "RPA 1951",
            "en": "Under Section 8(1) of the Representation of the People Act 1951, a conviction under which of the following Acts leads to mandatory 6-year disqualification regardless of the sentence imposed?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 8(1)-ன் கீழ், எந்தச் சட்டத்தின் கீழ் தண்டனை பெற்றால் விதிக்கப்பட்ட தண்டனைக் காலம் எதுவாக இருந்தாலும் 6 ஆண்டுகள் கட்டாய தகுதிநீக்கம் செய்யப்படும்?",
            "opts": [("Motor Vehicles Act", "மோட்டார் வாகனச் சட்டம்"), ("Protection of Civil Rights Act, 1955", "குடிமை உரிமைகள் பாதுகாப்புச் சட்டம், 1955"), ("Companies Act, 2013", "நிறுவனங்கள் சட்டம், 2013"), ("Consumer Protection Act, 2019", "நுகர்வோர் பாதுகாப்புச் சட்டம், 2019")],
            "key": "B",
            "exp_en": "Under Section 8(1) of RPA 1951, conviction for offences under the Protection of Civil Rights Act 1955 (promoting untouchability), Prevention of Corruption Act, or UAPA results in disqualification for 6 years from conviction date, even if only a fine is imposed.",
            "exp_ta": "பிரிவு 8(1)-ன் கீழ், தீண்டாமைக்கு எதிரான குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் 1955 அல்லது ஊழல் தடுப்புச் சட்டத்தின் கீழ் தண்டனை பெற்றால், அபராதம் மட்டுமே விதிக்கப்பட்டாலும் 6 ஆண்டுகள் தகுதிநீக்கம் ஏற்படும்.",
            "tip": "Section 8(1) lists specific heinous offences where mere conviction triggers disqualification.",
            "fact": "Section 8(1) also covers offences under the Prevention of Insults to National Honour Act, 1971."
        },
        # 11
        {
            "id": "ER_GT_011", "diff": "Medium", "sub": "RPA 1951",
            "en": "Under Section 9A of the Representation of the People Act 1951, a person is disqualified for membership of Parliament or State Legislature if they hold an existing contract with whom?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 9A-ன் கீழ், யாருடன் ஒப்பந்தம் வைத்துள்ள ஒரு நபர் நாடாளுமன்றம் அல்லது சட்டமன்ற உறுப்பினராக தகுதியற்றவர் ஆகிறார்?",
            "opts": [("A foreign corporation", "ஒரு வெளிநாட்டு நிறுவனம்"), ("The appropriate Government for supply of goods or execution of works", "பொருட்கள் விநியோகம் அல்லது பணிகளை மேற்கொள்வதற்காக சம்பந்தப்பட்ட அரசுடன்"), ("A private educational institution", "ஒரு தனியார் கல்வி நிறுவனம்"), ("A registered trade union", "ஒரு பதிவு செய்யப்பட்ட தொழிற்சங்கம்")],
            "key": "B",
            "exp_en": "Section 9A provides that a person shall be disqualified if there subsists a contract entered into by him in the course of his trade or business with the appropriate Government for the supply of goods to, or for the execution of any works undertaken by, that Government.",
            "exp_ta": "பிரிவு 9A-ன் கீழ், அரசுக்கு பொருட்கள் விநியோகம் செய்ய அல்லது அரசுப் பணிகளை மேற்கொள்ள சம்பந்தப்பட்ட அரசுடன் நேரடி ஒப்பந்தம் வைத்துள்ள நபர் தேர்தலில் போட்டியிட தகுதியற்றவர் ஆவார்.",
            "tip": "Prevents conflict of interest between business contracts with government and legislative duty.",
            "fact": "The contract must be ongoing and subsisting on the date of scrutiny of nominations."
        },
        # 12
        {
            "id": "ER_GT_012", "diff": "Medium", "sub": "Corrupt Practices",
            "en": "Under Section 123(1) of the Representation of the People Act 1951, which act is categorized as a 'corrupt practice' capable of voiding an election?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 123(1)-ன் கீழ், ஒரு தேர்தலை செல்லாததாக்கும் திறன் கொண்ட 'ஊழல் நடவடிக்கை' (Corrupt Practice) என வகைப்படுத்தப்படும் செயல் எது?",
            "opts": [("Bribery (giving gratification to induce voting)", "கையூட்டு / லஞ்சம் (வாக்களிக்கத் தூண்டுவதற்காக பணப்பயன் கொடுத்தல்)"), ("Door-to-door canvassing", "வீடு வீடாகச் சென்று வாக்கு சேகரித்தல்"), ("Issuing an election manifesto", "தேர்தல் அறிக்கை வெளியிடுதல்"), ("Deploying polling agents", "வாக்குச்சாவடி முகவர்களை நியமித்தல்")],
            "key": "A",
            "exp_en": "Under Section 123(1) of RPA 1951, Bribery—defined as any gift, offer or promise of gratification to any person with the object of inducing him to stand or not stand as a candidate or to vote or refrain from voting—is a statutory corrupt practice.",
            "exp_ta": "பிரிவு 123(1)-ன் கீழ், ஒருவரை போட்டியிட வைக்கவோ அல்லது குறிப்பிட்ட நபருக்கு வாக்களிக்க தூண்டவோ பணம் அல்லது பரிசுப் பொருட்களை வழங்குவது (கையூட்டு) சட்டப்பூர்வ ஊழல் நடவடிக்கையாகும்.",
            "tip": "Proving even a single corrupt practice in an Election Petition under Sec 100 will declare the election void.",
            "fact": "Section 123 contains 8 distinct clauses listing corrupt practices in Indian elections."
        },
        # 13
        {
            "id": "ER_GT_013", "diff": "Hard", "sub": "Corrupt Practices",
            "en": "In Abhiram Singh v. C.D. Commachen (2017), what did the 7-judge Constitution Bench rule regarding Section 123(3) of RPA 1951?",
            "ta": "அபிராம் சிங் எதிர் சி.டி. கொமாச்சன் (2017) வழக்கில், 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு 1951 சட்டத்தின் பிரிவு 123(3) குறித்து என்ன தீர்ப்பளித்தது?",
            "opts": [("Appeals to religion are valid if made by independent candidates", "சுயேச்சை வேட்பாளர்கள் மதத்தை வைத்து வாக்கு சேகரிக்கலாம்"), ("An appeal in the name of religion, race, caste, community or language of the candidate, rival, or voter is an illegal corrupt practice", "வேட்பாளர், எதிர்தரப்பு அல்லது வாக்காளரின் மதம், இனம், சாதி அல்லது மொழியின் பெயரால் வாக்கு கேட்பது சட்டவிரோத ஊழல் நடவடிக்கை"), ("Section 123(3) was struck down as unconstitutional", "பிரிவு 123(3) அரசியலமைப்பிற்கு எதிரானது என ரத்து செய்யப்பட்டது"), ("Caste appeals are permitted in reserved constituencies", "தனித்தொகுதிகளில் சாதி ரீதியான பிரச்சாரம் அனுமதிக்கப்படுகிறது")],
            "key": "B",
            "exp_en": "In Abhiram Singh (January 2017), a 4:3 majority bench ruled that the term 'his religion' in Section 123(3) includes the religion/caste of the candidate, his agent, the rival candidate, and the voters; secularism forbids any electoral appeal based on religious identity.",
            "exp_ta": "2017-ல் அபிராம் சிங் வழக்கில், வேட்பாளர், எதிர் வேட்பாளர் அல்லது வாக்காளர்களின் மதம் மற்றும் சாதியை பயன்படுத்தி வாக்கு கேட்பது பிரிவு 123(3)-ன் கீழ் முற்றிலும் சட்டவிரோத ஊழல் செயல் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "tip": "Secularism requires state and electoral process to be insulated from religious and caste appeals.",
            "fact": "Justice T.S. Thakur headed the historic 7-judge Constitution Bench."
        },
        # 14
        {
            "id": "ER_GT_014", "diff": "Medium", "sub": "Election Petitions",
            "en": "Under Section 80A of the Representation of the People Act 1951, which judicial forum has exclusive original jurisdiction to try an Election Petition?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 80A-ன் கீழ், ஒரு தேர்தல் மனுவை விசாரிக்கும் பிரத்யேக முதன்மை அதிகார வரம்பு எந்த நீதிமன்றத்திற்கு உள்ளது?",
            "opts": [("Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"), ("High Court of the State", "மாநில உயர்நீதிமன்றம்"), ("District Court", "மாவட்ட நீதிமன்றம்"), ("Central Administrative Tribunal", "மத்திய நிர்வாக தீர்ப்பாயம்")],
            "key": "B",
            "exp_en": "Section 80A of RPA 1951 explicitly confers exclusive jurisdiction to try election petitions on the High Court within whose local jurisdiction the election was held.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 80A, தேர்தல் நடைபெற்ற மாநிலத்தின் உயர்நீதிமன்றத்திற்கு தேர்தல் மனுக்களை விசாரிக்கும் பிரத்யேக அதிகார வரம்பை வழங்குகிறது.",
            "tip": "Prior to 1966, election petitions were heard by Election Tribunals; the 1966 amendment transferred jurisdiction to High Courts.",
            "fact": "An appeal from the High Court's final order lies directly to the Supreme Court under Section 116A."
        },
        # 15
        {
            "id": "ER_GT_015", "diff": "Medium", "sub": "Election Petitions",
            "en": "Under Section 116A of the Representation of the People Act 1951, what is the limitation period for filing an appeal to the Supreme Court against a High Court judgment in an Election Petition?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 116A-ன் கீழ், தேர்தல் மனு மீதான உயர்நீதிமன்ற தீர்ப்பை எதிர்த்து உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்வதற்கான கால வரம்பு என்ன?",
            "opts": [("15 days", "15 நாட்கள்"), ("30 days", "30 நாட்கள்"), ("60 days", "60 நாட்கள்"), ("90 days", "90 நாட்கள்")],
            "key": "B",
            "exp_en": "Under Section 116A(2) of RPA 1951, an appeal to the Supreme Court must be filed within a period of 30 days from the date of the order of the High Court.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 116A(2)-ன் கீழ், உயர்நீதிமன்ற தீர்ப்பு வெளியான தேதியிலிருந்து 30 நாட்களுக்குள் உச்ச நீதிமன்றத்தில் மேல்முறையீடு தாக்கல் செய்யப்பட வேண்டும்.",
            "tip": "Election petition in High Court: 45 days; Appeal to Supreme Court: 30 days.",
            "fact": "The Supreme Court may entertain an appeal after 30 days only if sufficient cause for delay is established."
        },
        # 16
        {
            "id": "ER_GT_016", "diff": "Easy", "sub": "Delimitation",
            "en": "Who is the ex-officio member of every Delimitation Commission constituted under the Delimitation Act?",
            "ta": "தொகுதி மறுவரையறைச் சட்டத்தின் கீழ் அமைக்கப்படும் ஒவ்வொரு தொகுதி மறுவரையறை ஆணையத்திலும் பதவிவழி உறுப்பினராக இருப்பவர் யார்?",
            "opts": [("Law Minister of India", "மத்திய சட்ட அமைச்சர்"), ("Chief Election Commissioner (or Election Commissioner nominated by CEC)", "தலைமை தேர்தல் ஆணையர் (அல்லது அவரால் பரிந்துரைக்கப்படும் தேர்தல் ஆணையர்)"), ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"), ("Cabinet Secretary", "மத்திய கேபினட் செயலாளர்")],
            "key": "B",
            "exp_en": "Under Section 3 of the Delimitation Act, the Delimitation Commission consists of three members: a retired or sitting Supreme Court judge (Chairperson), the Chief Election Commissioner (or an Election Commissioner), and the State Election Commissioner of the concerned state.",
            "exp_ta": "தொகுதி மறுவரையறை ஆணையச் சட்டத்தின் பிரிவு 3-ன் கீழ், உச்ச நீதிமன்ற ஓய்வுபெற்ற நீதிபதி (தலைவர்), தலைமை தேர்தல் ஆணையர் மற்றும் சம்பந்தப்பட்ட மாநில தேர்தல் ஆணையர் ஆகியோர் உறுப்பினர்களாக இருப்பர்.",
            "tip": "Delimitation Commission has 3 statutory members plus associate members (MPs/MLAs without voting rights).",
            "fact": "The orders of the Delimitation Commission are published in the Gazette and cannot be questioned in court under Article 329."
        },
        # 17
        {
            "id": "ER_GT_017", "diff": "Medium", "sub": "Delimitation",
            "en": "How many Delimitation Commissions have been constituted in India so far (under Acts of 1952, 1962, 1972, and 2002)?",
            "ta": "இந்தியாவில் இதுவரை எத்தனை தொகுதி மறுவரையறை ஆணையங்கள் அமைக்கப்பட்டுள்ளன (1952, 1962, 1972 மற்றும் 2002 சட்டங்களின் கீழ்)?",
            "opts": [("3 Commissions", "3 ஆணையங்கள்"), ("4 Commissions", "4 ஆணையங்கள்"), ("5 Commissions", "5 ஆணையங்கள்"), ("6 Commissions", "6 ஆணையங்கள்")],
            "key": "B",
            "exp_en": "Four Delimitation Commissions have been set up in independent India: 1952, 1962, 1972, and 2002. (A separate delimitation commission for Jammu & Kashmir and North-Eastern states was set up under Justice Ranjana Desai in 2020).",
            "exp_ta": "சுதந்திர இந்தியாவில் இதுவரை நான்கு முறை (1952, 1962, 1972 மற்றும் 2002) நாடாளுமன்ற சட்டங்களின் கீழ் நாடு தழுவிய தொகுதி மறுவரையறை ஆணையங்கள் அமைக்கப்பட்டுள்ளன.",
            "tip": "Delimitation was frozen after the 1972 commission until the 2002 commission was appointed.",
            "fact": "The 4th Delimitation Commission under Justice Kuldip Singh was constituted in July 2002."
        },
        # 18
        {
            "id": "ER_GT_018", "diff": "Medium", "sub": "Committees & Reports",
            "en": "Which committee on electoral reforms recommended that political parties should be brought under the Right to Information (RTI) Act and maintain audited accounts?",
            "ta": "அரசியல் கட்சிகள் தகவல் அறியும் உரிமைச் சட்டத்தின் (RTI) கீழ் கொண்டுவரப்பட வேண்டும் என்றும் தணிக்கை செய்யப்பட்ட கணக்குகளை பராமரிக்க வேண்டும் என்றும் பரிந்துரைத்த தேர்தல் சீர்திருத்தக் குழு எது?",
            "opts": [("Law Commission 170th Report (1999)", "170-வது சட்ட ஆணைய அறிக்கை (1999)"), ("Dinesh Goswami Committee (1990)", "தினேஷ் கோஸ்வாமி குழு (1990)"), ("Tarkunde Committee (1974)", "தர்குண்டே குழு (1974)"), ("K. Santhanam Committee (1964)", "கே. சந்தானம் குழு (1964)")],
            "key": "A",
            "exp_en": "The Law Commission of India in its 170th Report (1999) strongly recommended that internal democracy, transparent accounting, and disclosure of party finances under RTI are vital to prevent black money in elections.",
            "exp_ta": "1999-ல் சட்ட ஆணையத்தின் 170-வது அறிக்கை, அரசியல் கட்சிகள் தங்களின் வரவு-செலவு கணக்குகளை தணிக்கை செய்து பொது ஆய்வுக்கு வெளியிட வேண்டும் என்றும் உட்கட்சி ஜனநாயகம் வேண்டும் என்றும் வலியுறுத்தியது.",
            "tip": "In 2013, the Central Information Commission (CIC) also declared 6 national parties as public authorities under RTI.",
            "fact": "The 170th report also recommended a dedicated chapter on regulation of political parties in the RPA 1951."
        },
        # 19
        {
            "id": "ER_GT_019", "diff": "Hard", "sub": "Committees & Reports",
            "en": "What did the Justice V.S. Malimath Committee (2003) on Reforms of Criminal Justice System recommend regarding candidate qualifications?",
            "ta": "குற்றவியல் நீதி அமைப்பு சீர்திருத்தங்கள் குறித்த நீதிபதி வி.எஸ். மாலிமத் குழு (2003) வேட்பாளர் தகுதி குறித்து என்ன பரிந்துரைத்தது?",
            "opts": [("Lowering contesting age to 18", "போட்டியிடும் வயதை 18 ஆக குறைப்பது"), ("A candidate securing less than 50% plus one vote should not be declared elected (majority voting system)", "50% மற்றும் ஒரு வாக்குக்கு குறைவாகப் பெறும் வேட்பாளர் வெற்றி பெற்றவராக அறிவிக்கப்படக்கூடாது"), ("Abolishing secret ballot", "ரகசிய வாக்கு முறையை ரத்து செய்வது"), ("Banning political parties from rural areas", "ஊரகப் பகுதிகளில் அரசியல் கட்சிகளுக்கு தடை")],
            "key": "B",
            "exp_en": "The Malimath Committee recommended transitioning from the first-past-the-post (FPTP) system to a majority voting system where a candidate must secure 50% + 1 of valid votes polled to be elected, using run-off elections if necessary.",
            "exp_ta": "நீதிபதி மாலிமத் குழு, வெற்றி பெறும் வேட்பாளர் தொகுதியில் பதிவான வாக்குகளில் 50% + 1 வாக்கு பெற வேண்டும் என்ற பெரும்பான்மை வாக்கு முறையை (Majority Voting System) பரிந்துரைத்தது.",
            "tip": "In FPTP, candidates often win with as little as 30% vote share in multi-cornered contests.",
            "fact": "This recommendation aims to ensure that legislators truly represent the majority of their constituents."
        },
        # 20
        {
            "id": "ER_GT_020", "diff": "Medium", "sub": "EVM Technology",
            "en": "What type of memory chip is used in the Microcontroller of an Indian Electronic Voting Machine (EVM) to ensure that its firmware cannot be altered or hacked?",
            "ta": "இந்திய வாக்குப்பதிவு இயந்திரத்தின் (EVM) நுண்செயலியில் மென்பொருளை மாற்றவோ அல்லது ஹேக் செய்யவோ முடியாது என்பதை உறுதிப்படுத்த எந்த வகையான மெமரி சிப் பயன்படுத்தப்படுகிறது?",
            "opts": [("Flash EEPROM", "ஃபிளாஷ் EEPROM"), ("One-Time Programmable (OTP) Masked ROM", "ஒருமுறை மட்டுமே நிரலாக்கம் செய்யக்கூடிய (OTP) மாஸ்க்டு ரோம்"), ("Dynamic RAM", "டைனமிக் ரேம்"), ("Solid State Drive (SSD)", "சாலிட் ஸ்டேட் டிரைவ் (SSD)")],
            "key": "B",
            "exp_en": "Indian EVMs use a custom-manufactured Microcontroller with One-Time Programmable (OTP) Masked Read-Only Memory (ROM). Once the firmware code is burned during fabrication at BEL/ECIL, it can never be rewritten, read out, or altered.",
            "exp_ta": "இந்திய EVM-கள் ஒருமுறை மட்டுமே நிரலாக்கம் செய்யக்கூடிய (OTP Masked ROM) நுண்செயலியைப் பயன்படுத்துகின்றன; தொழிற்சாலையில் நிரல் பதிக்கப்பட்ட பிறகு அதை மீண்டும் எழுதவோ மாற்றவோ முடியாது.",
            "tip": "EVMs are completely standalone standalone computers with no Wi-Fi, Bluetooth, or internet connectivity.",
            "fact": "The microcontrollers are manufactured by NXP and Microchip in the USA under strict oversight."
        },
        # 21
        {
            "id": "ER_GT_021", "diff": "Hard", "sub": "EVM Architecture",
            "en": "What is the maximum number of votes that can be recorded in a single Control Unit (CU) of an Indian EVM (M3 model)?",
            "ta": "இந்திய EVM (M3 மாடல்) இயந்திரத்தின் ஒரு கட்டுப்பாட்டுப் பிரிவில் (Control Unit) அதிகபட்சமாக எத்தனை வாக்குகளைப் பதிவு செய்ய முடியும்?",
            "opts": [("1,500 votes", "1,500 வாக்குகள்"), ("2,000 votes", "2,000 வாக்குகள்"), ("3,840 votes", "3,840 வாக்குகள்"), ("5,000 votes", "5,000 வாக்குகள்")],
            "key": "B",
            "exp_en": "An Indian EVM (M3 model) Control Unit can store up to 2,000 votes. However, in practice, the Election Commission restricts the number of electors per polling station to a maximum of 1,500 (usually 1,000 to 1,200).",
            "exp_ta": "இந்திய M3 மாடல் EVM கட்டுப்பாட்டுப் பிரிவில் அதிகபட்சமாக 2,000 வாக்குகளைப் பதிவு செய்ய முடியும்; நடைமுறையில் ஒரு வாக்குச்சாவடியில் வாக்காளர் எண்ணிக்கை 1,500-க்குள் கட்டுப்படுத்தப்படுகிறது.",
            "tip": "M2 model could store 3,840 votes, but M3 standard capacity is 2,000 votes.",
            "fact": "A single M3 EVM can cater to up to 384 candidates (including NOTA) by daisy-chaining 24 Ballot Units."
        },
        # 22
        {
            "id": "ER_GT_022", "diff": "Medium", "sub": "VVPAT System",
            "en": "For how many seconds does the printed paper slip remain visible behind the transparent glass window of a VVPAT before dropping into the sealed drop box?",
            "ta": "விவிபேட் (VVPAT) இயந்திரத்தில் அச்சிடப்பட்ட காகித சீட்டு சீல் வைக்கப்பட்ட பெட்டிக்குள் விழுவதற்கு முன் எத்தனை விநாடிகள் கண்ணாடியின் பின்னால் வாக்காளருக்கு தெரியும்?",
            "opts": [("3 seconds", "3 விநாடிகள்"), ("5 seconds", "5 விநாடிகள்"), ("7 seconds", "7 விநாடிகள்"), ("10 seconds", "10 விநாடிகள்")],
            "key": "C",
            "exp_en": "Under Rule 49A of Conduct of Elections Rules 1961, the thermal printer in the VVPAT prints the candidate's serial number, name, and symbol, which is illuminated by an LED and remains visible to the elector through a transparent tinted window for exactly 7 seconds.",
            "exp_ta": "விவிபேட் இயந்திரத்தில் அச்சிடப்பட்ட சீட்டு (வரிசை எண், வேட்பாளர் பெயர், சின்னம்) வாக்காளர் சரிபார்ப்பதற்காக சரியாக 7 விநாடிகள் எல்இடி ஒளியில் தெரியும்; பின் தானாக பெட்டிக்குள் விழும்.",
            "tip": "7 seconds display allows the voter to verify that their vote went to their intended candidate.",
            "fact": "A beep sound is generated after the 7 seconds to confirm that the vote has been securely recorded."
        },
        # 23
        {
            "id": "ER_GT_023", "diff": "Hard", "sub": "VVPAT System",
            "en": "Under Rule 49MA of the Conduct of Elections Rules 1961, what happens if an elector alleges that the VVPAT paper slip displayed a candidate different from the one voted for?",
            "ta": "1961 தேர்தல் நடத்தை விதிகளின் விதி 49MA-ன் கீழ், தான் வாக்களித்த சின்னத்திற்கு பதிலாக வேறு சின்னத்தை VVPAT சீட்டு காட்டியதாக வாக்காளர் புகார் செய்தால் என்ன நடவடிக்கை எடுக்கப்படும்?",
            "opts": [("The entire polling station is countermanded immediately", "உடனடியாக அந்த வாக்குச்சாவடி தேர்தல் ரத்து செய்யப்படும்"), ("The elector is permitted to cast a Test Vote in the presence of candidates/agents after signing a written declaration under penalty of IPC Sec 177", "பொய் புகாருக்கு தண்டனை உண்டு என எழுத்துப்பூர்வ உறுதிமொழி பெற்ற பின் முகவர்கள் முன்னிலையில் மாதிரி சோதனை வாக்கு அளிக்க அனுமதிக்கப்படும்"), ("The EVM is seized and sent to forensic lab", "EVM பறிமுதல் செய்யப்பட்டு தடயவியல் ஆய்வுக்கு அனுப்பப்படும்"), ("The elector is disqualified from voting for 5 years", "வாக்காளர் 5 ஆண்டுகளுக்கு வாக்களிக்க தடை விதிக்கப்படுவார்")],
            "key": "B",
            "exp_en": "Under Rule 49MA, the Presiding Officer warns the voter of penal consequences under Section 177 of IPC (false information). If the voter insists, they sign a declaration and cast a test vote. If the allegation is false, the voter is handed over to police.",
            "exp_ta": "விதி 49MA-ன் கீழ், பொய் புகார் அளித்தால் ஐபிசி 177-ன் கீழ் தண்டனை என எச்சரிக்கப்பட்டு, மாதிரி சோதனை வாக்கு அளிக்க அனுமதிக்கப்படும்; குற்றச்சாட்டு பொய் எனத் தெரிந்தால் வாக்காளர் மீது காவல்துறை வழக்குப் பதிவு செய்யும்.",
            "tip": "Test vote details are entered in the Presiding Officer's diary and Form 17A.",
            "fact": "Under Section 177 IPC, furnishing false information to a public servant carries up to 6 months imprisonment."
        },
        # 24
        {
            "id": "ER_GT_024", "diff": "Medium", "sub": "Mock Poll Safeguards",
            "en": "During the mandatory Mock Poll conducted before actual polling begins on election day, what is the minimum number of votes that must be cast in the presence of polling agents?",
            "ta": "வாக்குப்பதிவு தொடங்குவதற்கு முன் முகவர்கள் முன்னிலையில் கட்டாயமாக நடத்தப்படும் மாதிரி வாக்குப்பதிவில் (Mock Poll) குறைந்தபட்சம் எத்தனை வாக்குகள் பதிவு செய்யப்பட வேண்டும்?",
            "opts": [("10 votes", "10 வாக்குகள்"), ("25 votes", "25 வாக்குகள்"), ("50 votes", "50 வாக்குகள்"), ("100 votes", "100 வாக்குகள்")],
            "key": "C",
            "exp_en": "According to ECI guidelines, a mandatory mock poll must be conducted at least 90 minutes before poll commences, casting at least 50 mock votes covering every candidate and NOTA. The CU is then cleared and VVPAT slip compartment emptied.",
            "exp_ta": "தேர்தல் ஆணைய விதிப்படி, வாக்குப்பதிவுக்கு 90 நிமிடங்களுக்கு முன் அனைத்து வேட்பாளர்கள் மற்றும் நோட்டாவை உள்ளடக்கி குறைந்தபட்சம் 50 மாதிரி வாக்குகள் பதிவு செய்து EVM சரியாக உள்ளதா என சரிபார்க்கப்பட வேண்டும்.",
            "tip": "Mock poll ensures both CU total and VVPAT paper slips tally exactly.",
            "fact": "A Mock Poll Certificate signed by the Presiding Officer and polling agents is mandatory."
        },
        # 25
        {
            "id": "ER_GT_025", "diff": "Hard", "sub": "NOTA Rules",
            "en": "Under the current electoral rules in India, what happens if NOTA (None of the Above) receives the highest number of votes in a Parliamentary or State Assembly constituency?",
            "ta": "இந்தியாவில் தற்போதைய தேர்தல் விதிகளின்படி, ஒரு நாடாளுமன்ற அல்லது சட்டமன்ற தொகுதியில் நோட்டா (NOTA) அதிக வாக்குகளைப் பெற்றால் என்ன நிகழும்?",
            "opts": [("Re-election is held with fresh candidates", "புதிய வேட்பாளர்களுடன் மறுதேர்தல் நடத்தப்படும்"), ("The candidate who secures the second highest number of valid votes is declared elected", "அடுத்தபடியாக இரண்டாவது அதிக செல்லுபடியாகும் வாக்குகளைப் பெற்ற வேட்பாளர் வெற்றி பெற்றவராக அறிவிக்கப்படுவார்"), ("The seat remains vacant until next general election", "அடுத்த பொதுத்தேர்தல் வரை அந்த தொகுதி காலியாக வைக்கப்படும்"), ("President's Rule is imposed in the constituency", "தொகுதியில் குடியரசுத் தலைவர் ஆட்சி அமல்படுத்தப்படும்")],
            "key": "B",
            "exp_en": "Under existing First-Past-The-Post rules in India, NOTA has only a symbolic/negative character. Even if NOTA secures 99% of votes, the candidate securing the next highest valid votes (even just 1 vote) is declared winner.",
            "exp_ta": "இந்தியாவின் தற்போதைய தேர்தல் சட்டப்படி நோட்டா குறியீட்டு மதிப்பையே கொண்டுள்ளது; நோட்டா அதிக வாக்குகளைப் பெற்றாலும் அதற்கு அடுத்தபடியாக அதிக வாக்கு பெற்ற வேட்பாளரே வெற்றி பெற்றவராக அறிவிக்கப்படுவார்.",
            "tip": "However, State Election Commissions in Maharashtra and Haryana have granted statutory power to reject candidates and hold re-elections if NOTA wins in local body elections.",
            "fact": "The Law Commission and various PILs have sought 'Right to Reject' with mandatory fresh elections."
        },
        # 26
        {
            "id": "ER_GT_026", "diff": "Medium", "sub": "Model Code of Conduct",
            "en": "From which precise moment does the Model Code of Conduct (MCC) come into operational force in an election?",
            "ta": "தேர்தல் நடத்தை விதிகள் (MCC) எந்த குறிப்பிட்ட தருணத்திலிருந்து உடனடியாக அமலுக்கு வருகின்றன?",
            "opts": [("From the date of Presidential notification", "குடியரசுத் தலைவர் அறிவிக்கை வெளியிடும் தேதியிலிருந்து"), ("From the moment the Election Commission announces the election schedule in a press conference", "தேர்தல் ஆணையம் பத்திரிகையாளர் சந்திப்பில் தேர்தல் அட்டவணையை அறிவிக்கும் அந்த நிமிடத்திலிருந்து"), ("From the date of filing of nominations", "வேட்புமனு தாக்கல் செய்யும் தேதியிலிருந்து"), ("From the last date of withdrawal of candidatures", "வேட்புமனு திரும்பப் பெறும் கடைசி தேதியிலிருந்து")],
            "key": "B",
            "exp_en": "The Model Code of Conduct comes into force immediately with the announcement of the election schedule by the Election Commission at its press conference, as affirmed by the Supreme Court in 2001.",
            "exp_ta": "தேர்தல் ஆணையம் பத்திரிகையாளர் சந்திப்பில் தேர்தல் தேதிகளை அறிவிக்கும் அந்த நொடியிலேயே தேர்தல் நடத்தை விதிகள் உடனடியாக முழுமையாக அமலுக்கு வருகின்றன.",
            "tip": "MCC remains in force until the completion of the election process (declaration of results).",
            "fact": "In 2001, the Union Government and ECI reached an agreement before the Supreme Court confirming this point."
        },
        # 27
        {
            "id": "ER_GT_027", "diff": "Hard", "sub": "Model Code of Conduct",
            "en": "Which of the following activities by the ruling government is strictly prohibited under Part VII ('Party in Power') of the Model Code of Conduct once elections are announced?",
            "ta": "தேர்தல் அறிவிக்கப்பட்டவுடன் தேர்தல் நடத்தை விதிகளின் பகுதி VII ('ஆளும் கட்சி')-ன் கீழ் ஆளும் அரசால் கீழ்க்கண்ட எந்த நடவடிக்கை முற்றிலும் தடை செய்யப்பட்டுள்ளது?",
            "opts": [("Presenting regular emergency medical treatment in hospitals", "மருத்துவமனைகளில் வழக்கமான அவசர சிகிச்சை அளிப்பது"), ("Laying foundation stones, announcing new financial grants, or promising public projects that influence voters", "அடிக்கல் நாட்டுவது, புதிய நிதி மானியங்களை அறிவிப்பது அல்லது வாக்காளர்களை ஈர்க்கும் வகையில் புதிய நலத்திட்டங்களை அறிவிப்பது"), ("Maintaining routine law and order through police", "காவல்துறை மூலம் சட்டம் ஒழுங்கை பராமரிப்பது"), ("Paying salaries to regular government employees", "வழக்கமான அரசு ஊழியர்களுக்கு ஊதியம் வழங்குவது")],
            "key": "B",
            "exp_en": "Part VII of the MCC explicitly bars Ministers and authorities from announcing financial grants, laying foundation stones, promising construction projects, or making ad-hoc appointments from the moment elections are announced.",
            "exp_ta": "நடத்தை விதிகளின் பகுதி VII, அமைச்சர்கள் மற்றும் ஆளும் கட்சியினர் புதிய நிதி மானியங்கள், திட்டங்கள், அடிக்கல் நாட்டுதல் மற்றும் புதிய பணிகளுக்கு ஒப்புதல் அளிப்பதை தேர்தல் முடியும் வரை தடை செய்கிறது.",
            "tip": "Prevents the ruling party from misusing state machinery or state funds to gain unfair electoral advantage.",
            "fact": "Government aircraft, vehicles, and official machinery cannot be used for election campaigning."
        },
        # 28
        {
            "id": "ER_GT_028", "diff": "Medium", "sub": "Media & Elections",
            "en": "What is the primary role of the Media Certification and Monitoring Committee (MCMC) constituted at district and state levels during elections?",
            "ta": "தேர்தல் காலங்களில் மாவட்ட மற்றும் மாநில அளவில் அமைக்கப்படும் ஊடக சான்றளிப்பு மற்றும் கண்காணிப்புக் குழுவின் (MCMC) முதன்மை பணி என்ன?",
            "opts": [("Issuing press passes for counting halls", "வாக்கு எண்ணிக்கை மையங்களுக்கு பத்திரிகையாளர் அனுமதி அட்டை வழங்குவது"), ("Pre-certification of political advertisements on electronic media and detecting/scrutinizing Paid News", "மின்னணு ஊடகங்களில் அரசியல் விளம்பரங்களுக்கு முன்-சான்றளிப்பு வழங்குதல் மற்றும் கட்டணச் செய்திகளை (Paid News) கண்டறிந்து கண்காணித்தல்"), ("Censoring newspaper editorials", "செய்தித்தாள் தலையங்கங்களை தணிக்கை செய்வது"), ("Conducting official opinion polls", "அரசு சார்பில் கருத்துக்கணிப்பு நடத்துவது")],
            "key": "B",
            "exp_en": "MCMC has a twin mandate: (1) mandatory pre-certification of all political advertisements on electronic media/social media, and (2) active scanning of print and electronic media to detect cases of Paid News and book expenditures against candidates.",
            "exp_ta": "MCMC-ன் முக்கிய பணி: மின்னணு ஊடக விளம்பரங்களை முன்கூட்டியே தணிக்கை செய்து சான்றளிப்பது மற்றும் ஊடகங்களில் வெளியாகும் கட்டணச் செய்திகளை (Paid News) கண்டறிந்து வேட்பாளர் கணக்கில் சேர்ப்பது.",
            "tip": "MCMC at district level is headed by the District Election Officer (DEO).",
            "fact": "MCMC includes an independent journalist or representative from the Press Council of India."
        },
        # 29
        {
            "id": "ER_GT_029", "diff": "Hard", "sub": "Media & Elections",
            "en": "How does the Press Council of India (PCI) officially define 'Paid News' in elections?",
            "ta": "தேர்தல்களில் 'கட்டணச் செய்தி' (Paid News) என்பதை இந்திய பத்திரிகை கவுன்சில் (PCI) அதிகாரப்பூர்வமாக எவ்வாறு வரையறுக்கிறது?",
            "opts": [("Any editorial criticizing a candidate", "ஒரு வேட்பாளரை விமர்சிக்கும் எந்தவொரு தலையங்கமும்"), ("Any news or analysis appearing in print or electronic media for price, in cash or kind, as consideration", "பணம் அல்லது பொருள் வடிவிலான ஆதாயத்திற்காக அச்சு அல்லது மின்னணு ஊடகங்களில் செய்தி அல்லது ஆய்வாக வெளியிடப்படும் விளம்பரம்"), ("Official government press releases", "அரசாங்கத்தின் அதிகாரப்பூர்வ செய்திக் குறிப்புகள்"), ("Live telecast of political rallies", "அரசியல் பேரணிகளின் நேரலை ஒளிபரப்பு")],
            "key": "B",
            "exp_en": "The Press Council of India defines Paid News as 'any news or analysis appearing in any media (print or electronic) for a price in cash or kind as consideration'. The candidate is issued notice and the cost is debited to their election expenditure account.",
            "exp_ta": "பணம் அல்லது பொருள் வடிவிலான பலனைப் பெற்றுக்கொண்டு, செய்தித்தாள்கள் அல்லது தொலைக்காட்சிகளில் செய்தி போல போலியாக வெளியிடப்படும் விளம்பரங்களே 'கட்டணச் செய்தி' என வரையறுக்கப்படுகிறது.",
            "tip": "Paid News misleads voters by disguising political advertisements as objective journalistic reporting.",
            "fact": "The Law Commission in its 255th Report recommended making Paid News an electoral offence under RPA 1951."
        },
        # 30
        {
            "id": "ER_GT_030", "diff": "Medium", "sub": "Expenditure Monitoring",
            "en": "What is the 'Shadow Observation Register' maintained by the Election Expenditure Monitoring cell during an election?",
            "ta": "தேர்தலின் போது தேர்தல் செலவு கண்காணிப்பு பிரிவால் பராமரிக்கப்படும் 'நிழல் கண்காணிப்பு பதிவேடு' (Shadow Observation Register) என்றால் என்ன?",
            "opts": [("A register of criminal suspects", "குற்றவாளிகளின் ரகசிய பட்டியல்"), ("An independent official record of a candidate's daily campaign events and expenses tracked by video surveillance teams", "வீடியோ கண்காணிப்புக் குழுக்களால் கண்காணிக்கப்பட்டு வேட்பாளரின் தினசரி தேர்தல் செலவுகளை தேர்தல் ஆணையம் பதிவு செய்யும் அதிகாரப்பூர்வ பதிவேடு"), ("A list of polling booths prone to violence", "வன்முறைக்கு வாய்ப்புள்ள வாக்குச்சாவடிகளின் பட்டியல்"), ("The register of registered postal voters", "பதிவு செய்யப்பட்ட தபால் வாக்காளர்களின் பதிவேடு")],
            "key": "B",
            "exp_en": "The Shadow Observation Register is maintained by the Accounting Team of ECI for every candidate, independently recording expenses on rallies, vehicles, banners, and loudspeakers using Video Surveillance Team logs to compare with the candidate's register.",
            "exp_ta": "நிழல் கண்காணிப்பு பதிவேடு என்பது வீடியோ கண்காணிப்புக் குழுவின் பதிவுகளை அடிப்படையாகக் கொண்டு, தேர்தல் ஆணையம் சுயாதீனமாக வேட்பாளரின் தினசரி செலவுகளைக் கணக்கிட்டு வைக்கும் பதிவேடாகும்.",
            "tip": "If there is a discrepancy between candidate's register and Shadow Register, a notice is served.",
            "fact": "The candidate must reconcile their expenditure account with the Shadow Register three times during the campaign."
        },
        # 31
        {
            "id": "ER_GT_031", "diff": "Hard", "sub": "Expenditure Monitoring",
            "en": "What is the standard threshold amount above which all campaign-related expenses must be paid exclusively by crossed account payee cheque / draft or online bank transfer from the candidate's dedicated bank account?",
            "ta": "வேட்பாளரின் பிரத்யேக தேர்தல் வங்கிக் கணக்கிலிருந்து காசோலை அல்லது வங்கிப் பரிவர்த்தனை மூலமாக மட்டுமே செலுத்தப்பட வேண்டும் என்ற வரம்புத் தொகை எவ்வளவு?",
            "opts": [("Rs 5,000", "ரூ. 5,000"), ("Rs 10,000", "ரூ. 10,000"), ("Rs 20,000", "ரூ. 20,000"), ("Rs 50,000", "ரூ. 50,000")],
            "key": "B",
            "exp_en": "Under ECI instructions, every candidate must open a separate dedicated bank account for elections at least one day before nomination. Any expenditure exceeding Rs 10,000 to a single person/entity must be paid via crossed cheque, draft, or electronic fund transfer.",
            "exp_ta": "தேர்தல் ஆணைய உத்தரவுப்படி, ரூ. 10,000-க்கு மேற்பட்ட எந்தவொரு தேர்தல் செலவும் ரொக்கமாக செலுத்தப்படக்கூடாது; அது காசோலை அல்லது ஆன்லைன் வங்கி பரிமாற்றம் மூலமே செலுத்தப்பட வேண்டும்.",
            "tip": "Candidates cannot make cash payments exceeding Rs 10,000.",
            "fact": "The separate election bank account must be opened in the name of the candidate exclusively."
        },
        # 32
        {
            "id": "ER_GT_032", "diff": "Easy", "sub": "Electoral Rolls",
            "en": "Every year, what is the nationwide flagship day observed across India on 25th January to promote electoral participation and registration of new voters?",
            "ta": "தேர்தல் விழிப்புணர்வு மற்றும் புதிய வாக்காளர்கள் பதிவை ஊக்குவிப்பதற்காக ஆண்டுதோறும் ஜனவரி 25 அன்று நாடு முழுவதும் அனுசரிக்கப்படும் நாள் எது?",
            "opts": [("National Governance Day", "தேசிய நல்லாட்சி தினம்"), ("National Voters' Day (NVD)", "தேசிய வாக்காளர் தினம் (NVD)"), ("National Panchayati Raj Day", "தேசிய பஞ்சாயத்து ராஜ் தினம்"), ("Constitution Day", "அரசியலமைப்பு தினம்")],
            "key": "B",
            "exp_en": "National Voters' Day has been celebrated across India on 25th January every year since 2011 to mark the foundation day of the Election Commission of India (established on 25 January 1950).",
            "exp_ta": "இந்திய தேர்தல் ஆணையம் தொடங்கப்பட்ட நாளான ஜனவரி 25-ஐ நினைவுகூரும் வகையில், 2011 முதல் ஆண்டுதோறும் ஜனவரி 25 'தேசிய வாக்காளர் தினம்' என கொண்டாடப்படுகிறது.",
            "tip": "First National Voters' Day was inaugurated by President Pratibha Patil on 25 January 2011.",
            "fact": "New electors are handed their EPIC badges along with a copy of the Voter Pledge on this day."
        },
        # 33
        {
            "id": "ER_GT_033", "diff": "Medium", "sub": "Voter Identification",
            "en": "In what year did Chief Election Commissioner T.N. Seshan make the possession of Elector Photo Identity Cards (EPIC) mandatory for voting in Indian elections?",
            "ta": "இந்திய தேர்தல்களில் வாக்களிப்பதற்கு வாக்காளர் புகைப்பட அடையாள அட்டை (EPIC) கட்டாயம் என்ற உத்தரவை தலைமை தேர்தல் ஆணையர் டி.என். சேஷன் எந்த ஆண்டு பிறப்பித்தார்?",
            "opts": [("1989", "1989"), ("1993", "1993"), ("1998", "1998"), ("2001", "2001")],
            "key": "B",
            "exp_en": "In 1993, CEC T.N. Seshan issued an ultimatum to state governments mandating the issuance and possession of Photo Identity Cards (EPIC) for electors to eliminate bogus voting and impersonation.",
            "exp_ta": "போலி வாக்குப்பதிவு மற்றும் ஆள்மாறாட்டத்தை ஒழிக்க 1993-ல் தலைமை தேர்தல் ஆணையர் டி.என். சேஷன் அனைத்து வாக்காளர்களுக்கும் புகைப்பட அடையாள அட்டை (EPIC) வழங்குவதை கட்டாயமாக்கினார்.",
            "tip": "Though EPIC was first conceived in 1979 in Sikkim, its strict nationwide enforcement began under T.N. Seshan in 1993.",
            "fact": "Alternative photo documents (Aadhaar, Passport, Driving License, PAN card) are also accepted if a voter lacks physical EPIC."
        },
        # 34
        {
            "id": "ER_GT_034", "diff": "Hard", "sub": "Electoral Registration",
            "en": "Under Section 20 of the Representation of the People Act 1950, which of the following categories of persons does NOT automatically qualify as having 'service qualification' for enrolment in home constituency?",
            "ta": "1950 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 20-ன் கீழ், கீழ்க்கண்டவர்களில் யார் தனது சொந்த தொகுதியில் வாக்காளராக பதிவு செய்ய 'பணித் தகுதி' (Service Qualification) தானாகப் பெறாதவர்?",
            "opts": [("A member of the armed forces of the Union", "மத்திய ஆயுதப் படைகளின் உறுப்பினர்"), ("A member of an armed police force of a State serving outside that State", "வெளி மாநிலத்தில் பணியாற்றும் ஒரு மாநிலத்தின் ஆயுதக் காவல் படை உறுப்பினர்"), ("A person employed under the Government of India in a post outside India", "இந்தியாவிற்கு வெளியே பணியாற்றும் இந்திய அரசு ஊழியர்"), ("An employee of a private multinational software company working abroad", "வெளிநாட்டில் பணியாற்றும் தனியார் பன்னாட்டு மென்பொருள் நிறுவன ஊழியர்")],
            "key": "D",
            "exp_en": "Under Section 20(8) of RPA 1950, 'service qualification' applies only to armed forces members, state armed police serving outside state, and personnel employed by Government of India posted abroad. Private company employees must enrol as overseas electors under Section 20A.",
            "exp_ta": "பிரிவு 20(8)-ன் கீழ், இராணுவத்தினர் மற்றும் அரசு பணி காரணமாக வெளியில் இருப்பவர்களுக்கு மட்டுமே சேவைத் தகுதி உண்டு; தனியார் நிறுவன ஊழியர்கள் பிரிவு 20A-ன் கீழ் வெளிநாடு வாழ் வாக்காளராகவே பதிவு செய்ய வேண்டும்.",
            "tip": "Service voters can cast votes through postal ballot or appoint a proxy.",
            "fact": "The wife of a service voter living with him is also entitled to be registered as a service voter."
        },
        # 35
        {
            "id": "ER_GT_035", "diff": "Medium", "sub": "Postal Voting",
            "en": "Which statutory form is used by eligible senior citizens (85+ years) and PwD voters to apply for Home Voting via Postal Ballot under amended election rules?",
            "ta": "திருத்தப்பட்ட தேர்தல் விதிகளின் கீழ் 85 வயதுக்கு மேற்பட்ட முதியவர்கள் மற்றும் மாற்றுத்திறனாளிகள் தபால் வாக்கு மூலம் வீட்டில் வாக்களிக்க விண்ணப்பிக்கப் பயன்படுத்தும் படிவம் எது?",
            "opts": [("Form 12", "படிவம் 12"), ("Form 12D", "படிவம் 12D"), ("Form 13A", "படிவம் 13A"), ("Form 17A", "படிவம் 17A")],
            "key": "B",
            "exp_en": "Form 12D is the prescribed application form submitted to the Returning Officer within 5 days of election notification to avail the postal ballot facility at home for absentee voters (senior citizens 85+ and benchmark PwDs).",
            "exp_ta": "85 வயதுக்கு மேற்பட்ட முதியவர்கள் மற்றும் மாற்றுத்திறனாளிகள் வீட்டிலிருந்தே தபால் வாக்கு செலுத்த தேர்தல் அறிவிப்பு வெளியான 5 நாட்களுக்குள் படிவம் 12D-ல் விண்ணப்பிக்க வேண்டும்.",
            "tip": "A mobile polling team visiting the voter's home consists of 2 polling officials, a videographer, and security.",
            "fact": "Voting takes place in complete secrecy behind a voting compartment installed inside the residence."
        },
        # 36
        {
            "id": "ER_GT_036", "diff": "Hard", "sub": "Candidate Qualifications",
            "en": "Under Section 34 of the Representation of the People Act 1951, what is the nomination security deposit required for an Assembly constituency contest in case of SC/ST candidates?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 34-ன் கீழ், சட்டமன்றத் தேர்தலில் போட்டியிடும் SC/ST வேட்பாளர்களுக்கான காப்புத்தொகை எவ்வளவு?",
            "opts": [("Rs 2,500", "ரூ. 2,500"), ("Rs 5,000", "ரூ. 5,000"), ("Rs 10,000", "ரூ. 10,000"), ("Rs 12,500", "ரூ. 12,500")],
            "key": "B",
            "exp_en": "Under Section 34(1)(b) of RPA 1951, the security deposit for an Assembly election is Rs 10,000 for general candidates and half that amount, i.e., Rs 5,000, for SC/ST candidates.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 34(1)(b)-ன் கீழ், சட்டமன்ற தேர்தலில் பொது வேட்பாளர்களுக்கு ரூ. 10,000-மும், SC/ST வேட்பாளர்களுக்கு அதில் பாதி தொகையான ரூ. 5,000-மும் காப்புத்தொகையாக நிர்ணயிக்கப்பட்டுள்ளது.",
            "tip": "Lok Sabha: General Rs 25,000 / SC-ST Rs 12,500; Assembly: General Rs 10,000 / SC-ST Rs 5,000.",
            "fact": "Security deposits were last increased in 2009 by an amendment to RPA 1951."
        },
        # 37
        {
            "id": "ER_GT_037", "diff": "Medium", "sub": "Candidate Nominations",
            "en": "How many electors of the constituency must subscribe as proposers on the nomination paper of a candidate set up by a recognized political party versus an independent candidate?",
            "ta": "அங்கீகரிக்கப்பட்ட அரசியல் கட்சியின் வேட்பாளருக்கும், சுயேச்சை வேட்பாளருக்கும் முறையே எத்தனை வாக்காளர்கள் முன்மொழிபவர்களாக கையெழுத்திட வேண்டும்?",
            "opts": [("1 proposer for recognized party candidate; 10 proposers for independent candidate", "அங்கீகரிக்கப்பட்ட கட்சி வேட்பாளருக்கு 1 முன்மொழிபவர்; சுயேச்சை வேட்பாளருக்கு 10 முன்மொழிபவர்கள்"), ("5 proposers for both", "இருவருக்கும் 5 முன்மொழிபவர்கள்"), ("10 proposers for both", "இருவருக்கும் 10 முன்மொழிபவர்கள்"), ("2 proposers for recognized party; 20 for independent", "அங்கீகரிக்கப்பட்ட கட்சிக்கு 2; சுயேச்சைக்கு 20")],
            "key": "A",
            "exp_en": "Under Section 33(1) of RPA 1951, a candidate sponsored by a recognized National or State party requires only 1 proposer (an elector of that constituency), whereas a candidate of an unrecognized party or an independent requires 10 proposers.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 33(1)-ன் கீழ், அங்கீகரிக்கப்பட்ட கட்சி வேட்பாளருக்கு 1 வாக்காளர் முன்மொழிந்தால் போதும்; சுயேச்சை அல்லது அங்கீகரிக்கப்படாத கட்சி வேட்பாளருக்கு 10 வாக்காளர்கள் முன்மொழிய வேண்டும்.",
            "tip": "The 10-proposer rule was introduced in 1996 to weed out non-serious independent candidatures.",
            "fact": "All proposers must be registered electors in the same constituency."
        },
        # 38
        {
            "id": "ER_GT_038", "diff": "Hard", "sub": "Candidate Scrutiny",
            "en": "Under Section 36 of the Representation of the People Act 1951, on which ground can a Returning Officer NOT reject a candidate's nomination paper?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 36-ன் கீழ், கீழ்க்கண்ட எந்தக் காரணத்திற்காக தேர்தல் நடத்தும் அதிகாரி ஒரு வேட்புமனுவை நிராகரிக்க முடியாது?",
            "opts": [("Candidate is not qualified under the Constitution", "வேட்பாளர் அரசியலமைப்பின் கீழ் தகுதி பெறவில்லை"), ("Nomination paper contains a clerical or technical defect of a non-substantial character", "வேட்புமனுவில் எழுத்தர் பிழை அல்லது கணிசமற்ற தொழில்நுட்ப குறைபாடு மட்டுமே இருப்பது"), ("Failure to deposit the required security deposit", "தேவையான காப்புத்தொகையை செலுத்தத் தவறுவது"), ("Signature of the candidate or proposer is not genuine", "வேட்பாளர் அல்லது முன்மொழிபவரின் கையொப்பம் போலியானது")],
            "key": "B",
            "exp_en": "Section 36(4) of RPA 1951 explicitly mandates that the Returning Officer shall not reject any nomination paper on the ground of any defect which is not of a substantial character (e.g., minor misspelling of name).",
            "exp_ta": "பிரிவு 36(4)-ன் கீழ், சிறிய எழுத்துப் பிழைகள் போன்ற அடிப்படையற்ற சாதாரண தொழில்நுட்பக் குறைபாடுகளுக்காக தேர்தல் அதிகாரி வேட்புமனுவை நிராகரிக்கக்கூடாது.",
            "tip": "Substantial defects include: blank affidavit columns, lack of oath, under-age, or no deposit.",
            "fact": "The Returning Officer must hold scrutiny in the presence of candidates and record reasons in writing if rejecting."
        },
        # 39
        {
            "id": "ER_GT_039", "diff": "Medium", "sub": "Death of Candidates",
            "en": "Following the 1996 amendment to Section 52 of RPA 1951, what happens to an election if a candidate dies before the commencement of the poll?",
            "ta": "1951 சட்டத்தின் பிரிவு 52-ல் 1996-ல் செய்யப்பட்ட திருத்தத்திற்குப் பிறகு, வாக்குப்பதிவுக்கு முன் ஒரு வேட்பாளர் இறந்துவிட்டால் என்ன நடவடிக்கை எடுக்கப்படும்?",
            "opts": [("The election is automatically countermanded in all cases", "அனைத்து நிகழ்வுகளிலும் தேர்தல் உடனடியாக ரத்து செய்யப்படும்"), ("The election is not countermanded unless the deceased candidate was set up by a recognized political party", "இறந்தவர் அங்கீகரிக்கப்பட்ட அரசியல் கட்சியின் வேட்பாளராக இருந்தால் மட்டுமே தேர்தல் ஒத்திவைக்கப்படும்; சுயேச்சை இறந்தால் தேர்தல் தொடரும்"), ("Polling proceeds normally without any postponement", "எந்த ஒத்திவைப்பும் இல்லாமல் வாக்குப்பதிவு வழக்கம் போல் நடைபெறும்"), ("The dead candidate's spouse is automatically declared elected", "இறந்த வேட்பாளரின் வாழ்க்கைத் துணை வெற்றி பெற்றவராக அறிவிக்கப்படுவார்")],
            "key": "B",
            "exp_en": "Prior to 1996, the death of any candidate countermanded the poll, leading to frequent assassinations of non-serious independents to derail elections. The 1996 amendment ensured that only the death of a recognized party candidate adjourns the poll to allow a replacement candidate.",
            "exp_ta": "1996 திருத்தத்திற்கு முன் சுயேச்சை இறந்தாலும் தேர்தல் ரத்தானது; ஆனால் 1996 முதல், அங்கீகரிக்கப்பட்ட கட்சியின் வேட்பாளர் இறந்தால் மட்டுமே தேர்தல் ஒத்திவைக்கப்பட்டு புதிய வேட்பாளருக்கு அவகாசம் தரப்படும்.",
            "tip": "Recognized party candidate death = adjournment; Independent candidate death = poll proceeds.",
            "fact": "The recognized party is given 7 days to field an alternative candidate under Section 52(2)."
        },
        # 40
        {
            "id": "ER_GT_040", "diff": "Hard", "sub": "Counting of Votes",
            "en": "Under Rule 56C of the Conduct of Elections Rules 1961, what is the procedure followed if an EVM Control Unit fails to display results on counting day?",
            "ta": "1961 தேர்தல் நடத்தை விதிகளின் விதி 56C-ன் கீழ், வாக்கு எண்ணிக்கை நாளில் ஒரு EVM கட்டுப்பாட்டுப் பிரிவு முடிவுகளைக் காட்டத் தவறினால் என்ன நடைமுறை பின்பற்றப்படும்?",
            "opts": [("The entire constituency votes again", "தொகுதி முழுவதும் மீண்டும் வாக்குப்பதிவு நடத்தப்படும்"), ("The VVPAT paper slips of that particular polling station are counted to determine the result", "அந்த குறிப்பிட்ட வாக்குச்சாவடியின் VVPAT காகிதச் சீட்டுகள் எண்ணப்பட்டு முடிவு தீர்மானிக்கப்படும்"), ("The votes of that polling booth are permanently discarded", "அந்த வாக்குச்சாவடியின் வாக்குகள் நிரந்தரமாக நிராகரிக்கப்படும்"), ("The winner is decided by toss of a coin", "நாணயம் சுண்டி வெற்றி தீர்மானிக்கப்படும்")],
            "key": "B",
            "exp_en": "Under Rule 56D and ECI operational guidelines, if a Control Unit displays an error or fails to power up, the physical VVPAT paper slips stored in its sealed drop box are retrieved and counted in the presence of the Returning Officer and candidate agents.",
            "exp_ta": "விதி 56D-ன் படி, வாக்கு எண்ணிக்கை நாளில் கட்டுப்பாட்டுப் பிரிவு பழுதடைந்தால், அதனுடன் இணைக்கப்பட்ட VVPAT பெட்டியிலுள்ள காகிதச் சீட்டுகள் முகவர்கள் முன்னிலையில் எண்ணப்பட்டு முடிவு கணக்கிடப்படும்.",
            "tip": "VVPAT slip count prevails over the electronic count in case of discrepancy under Rule 56D(4)(b).",
            "fact": "The slips are counted in a specially constructed VVPAT Counting Booth (VCB) inside the counting hall."
        },
        # 41
        {
            "id": "ER_GT_041", "diff": "Medium", "sub": "Equality of Votes",
            "en": "Under Section 65 of the Representation of the People Act 1951, how is an election decided if there is an equality of votes (tie) between two leading candidates?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 65-ன் கீழ், முன்னணி வேட்பாளர்களிடையே சம வாக்குகள் (டை) ஏற்பட்டால் தேர்தல் முடிவு எவ்வாறு தீர்மானிக்கப்படுகிறது?",
            "opts": [("By holding a fresh bye-election", "மறு இடைத்தேர்தல் நடத்துவதன் மூலம்"), ("By drawing of lots by the Returning Officer", "தேர்தல் நடத்தும் அதிகாரி குலுக்கல் (Lot) சீட்டு எடுப்பதன் மூலம்"), ("By seniority of age of the candidates", "வேட்பாளர்களின் வயது மூப்பு அடிப்படையில்"), ("By the decision of the Election Commission", "தேர்தல் ஆணையத்தின் முடிவின் மூலம்")],
            "key": "B",
            "exp_en": "Under Section 65 of RPA 1951, if an equality of votes is found between two candidates, the Returning Officer shall forthwith decide between those candidates by lot, and proceed as if the candidate on whom the lot falls had received an additional vote.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 65-ன் கீழ், சம வாக்குகள் பதிவானால் தேர்தல் நடத்தும் அதிகாரி குலுக்கல் முறையில் சீட்டு எடுத்து வெற்றிபெற்றவரை தீர்மானிக்க வேண்டும்.",
            "tip": "The winner of the draw of lots is statutorily treated as receiving one additional vote.",
            "fact": "This provision applies equally to Parliamentary and Assembly elections."
        },
        # 42
        {
            "id": "ER_GT_042", "diff": "Medium", "sub": "Electoral Offences",
            "en": "Under Section 131 of the Representation of the People Act 1951, who has the power to direct the arrest of a person committing disorderly conduct or using megaphones within 100 metres of a polling station?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 131-ன் கீழ், வாக்குச்சாவடியின் 100 மீட்டருக்குள் ஒலிபெருக்கி பயன்படுத்துபவர் அல்லது அமைதிக்கு குந்தகம் விளைவிப்பவரை கைது செய்ய உத்தரவிட யாருக்கு அதிகாரம் உண்டு?",
            "opts": [("Chief Electoral Officer", "தலைமை தேர்தல் அதிகாரி"), ("Presiding Officer of the Polling Station", "வாக்குச்சாவடி தலைமை அலுவலர் (Presiding Officer)"), ("Local Political Agent", "உள்ளூர் அரசியல் முகவர்"), ("Sector Magistrate only", "மண்டல மேஜிஸ்திரேட் மட்டுமே")],
            "key": "B",
            "exp_en": "Under Section 131(2) of RPA 1951, if any person misconducts himself or fails to obey the lawful directions of the Presiding Officer, the Presiding Officer may direct any police officer to remove him or take him into custody.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 131(2)-ன் கீழ், வாக்குச்சாவடி தலைமை அலுவலரின் உத்தரவுக்கு கீழ்ப்படியாத நபரை அப்புறப்படுத்தவோ அல்லது கைது செய்யவோ உத்தரவிடும் அதிகாரம் வாக்குச்சாவடி தலைமை அலுவலருக்கு உள்ளது.",
            "tip": "Presiding Officers exercise quasi-magisterial powers inside their designated polling booth.",
            "fact": "Disorderly conduct near a polling booth carries imprisonment up to 3 months or fine or both."
        },
        # 43
        {
            "id": "ER_GT_043", "diff": "Hard", "sub": "Electoral Offences",
            "en": "Under Section 135B of the Representation of the People Act 1951, inserted in 1996, what right is guaranteed to employees of business and industrial establishments on polling day?",
            "ta": "1996-ல் 1951 சட்டத்தில் சேர்க்கப்பட்ட பிரிவு 135B-ன் கீழ், வாக்குப்பதிவு நாளன்று வணிக மற்றும் தொழில் நிறுவன ஊழியர்களுக்கு உத்தரவாதம் அளிக்கப்பட்டுள்ள உரிமை எது?",
            "opts": [("Double daily wage", "இரட்டிப்பு தினசரி ஊதியம்"), ("Grant of a paid holiday to exercise their franchise", "வாக்களிப்பதற்காக ஊதியத்துடன் கூடிய விடுமுறை"), ("Free transport to the polling station", "வாக்குச்சாவடிக்கு இலவச போக்குவரத்து"), ("Compulsory overtime pay", "கட்டாய கூடுதல் நேர ஊதியம்")],
            "key": "B",
            "exp_en": "Section 135B mandates that every person employed in any business, trade, industrial undertaking, or establishment entitled to vote shall be granted a paid holiday on the day of poll, with no deduction of wages.",
            "exp_ta": "பிரிவு 135B, வாக்குப்பதிவு நாளன்று வாக்களிக்க தகுதியுள்ள அனைத்து வணிக மற்றும் தொழிற்துறை ஊழியர்களுக்கும் ஊதியத்துடன் கூடிய கட்டாய விடுமுறை வழங்கப்பட வேண்டும் என உத்தரவாதம் அளிக்கிறது.",
            "tip": "Violation of Section 135B is an offence punishable with a fine on the employer.",
            "fact": "This section does not apply to electors whose absence would cause danger or substantial loss in continuous employment."
        },
        # 44
        {
            "id": "ER_GT_044", "diff": "Medium", "sub": "Electoral Offences",
            "en": "Under Section 135C of the Representation of the People Act 1951, liquor and intoxicating substances cannot be sold or distributed within a polling area for how many hours ending with the close of poll?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 135C-ன் கீழ், வாக்குப்பதிவு முடிவடையும் நேரத்திற்கு முந்தைய எத்தனை மணி நேரத்திற்கு மதுபான விற்பனை மற்றும் விநியோகம் தடை செய்யப்படுகிறது?",
            "opts": [("24 hours", "24 மணி நேரம்"), ("48 hours", "48 மணி நேரம்"), ("72 hours", "72 மணி நேரம்"), ("36 hours", "36 மணி நேரம்")],
            "key": "B",
            "exp_en": "Section 135C prohibits the sale, distribution, or giving away of intoxicating liquors in hotels, shops, and eating places within the polling area during the period of 48 hours ending with the hour fixed for the conclusion of the poll ('Dry Days').",
            "exp_ta": "பிரிவு 135C-ன் கீழ், வாக்குப்பதிவு முடிவடையும் நேரத்திற்கு முந்தைய 48 மணி நேர அமைதிக்காலத்தில் மதுபான கடைகள் மற்றும் உணவகங்களில் மது விற்பனை செய்ய முழு தடை விதிக்கப்படுகிறது (Dry Days).",
            "tip": "Also applies on the day of counting of votes.",
            "fact": "Violation of Section 135C carries imprisonment up to 6 months or fine up to Rs 2,000 or both."
        },
        # 45
        {
            "id": "ER_GT_045", "diff": "Hard", "sub": "Electoral Offences",
            "en": "Under Section 125A of the Representation of the People Act 1951, what is the penalty prescribed for a candidate who fails to furnish required affidavit information or conceals facts?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 125A-ன் கீழ், வேட்புமனு பிரமாணப் பத்திரத்தில் விவரங்களை மறைக்கும் அல்லது தவறான தகவல்களைத் தரும் வேட்பாளருக்கு விதிக்கப்படும் தண்டனை என்ன?",
            "opts": [("Imprisonment up to 6 months, or fine, or both", "6 மாதங்கள் வரை சிறை தண்டனை, அல்லது அபராதம், அல்லது இரண்டும்"), ("Imprisonment up to 2 years mandatory", "கட்டாய 2 ஆண்டுகள் சிறை தண்டனை"), ("Permanent debarment from politics", "அரசியலில் இருந்து நிரந்தர தடை"), ("Fine of Rs 50,000 only", "ரூ. 50,000 அபராதம் மட்டுமே")],
            "key": "A",
            "exp_en": "Section 125A of RPA 1951 (inserted in 2002) provides that any candidate who fails to furnish information under Section 33A or provides false information or conceals information in Form 26 is punishable with imprisonment up to 6 months, or fine, or both.",
            "exp_ta": "2002-ல் சேர்க்கப்பட்ட பிரிவு 125A-ன் கீழ், படிவம் 26 பிரமாணப் பத்திரத்தில் உண்மைகளை மறைக்கும் அல்லது பொய்யான தகவல்களை வழங்கும் வேட்பாளருக்கு 6 மாதங்கள் வரை சிறைக்காவல் அல்லது அபராதம் அல்லது இரண்டும் விதிக்கப்படலாம்.",
            "tip": "The Law Commission has recommended increasing this penalty to a minimum of 2 years imprisonment to disqualify convicted candidates under Sec 8.",
            "fact": "Section 33A deals with candidate declarations regarding pending charges and convictions."
        },
        # 46
        {
            "id": "ER_GT_046", "diff": "Medium", "sub": "Disqualification",
            "en": "Under Article 103 of the Constitution of India, before deciding whether a sitting Member of Parliament has become subject to any disqualification under Article 102(1), the President of India must obtain the opinion of whom?",
            "ta": "அரசியலமைப்பின் சரத்து 103-ன் கீழ், நாடாளுமன்ற உறுப்பினர் ஒருவர் சரத்து 102(1)-ன் கீழ் தகுதிநீக்கத்திற்கு ஆளாகிவிட்டாரா என்பதை தீர்மானிக்கும் முன், குடியரசுத் தலைவர் யாருடைய கருத்தைப் பெற வேண்டும்?",
            "opts": [("Chief Justice of India", "இந்திய தலைமை நீதிபதி"), ("Election Commission of India (ECI)", "இந்திய தேர்தல் ஆணையம் (ECI)"), ("Lok Sabha Speaker", "மக்களவை சபாநாயகர்"), ("Attorney General of India", "இந்திய அட்டர்னி ஜெனரல்")],
            "key": "B",
            "exp_en": "Article 103(2) mandates that before giving any decision on disqualification of an MP under Article 102(1), the President shall obtain the opinion of the Election Commission and shall act according to such opinion.",
            "exp_ta": "சரத்து 103(2)-ன் படி, எம்.பி-க்களின் தகுதிநீக்கம் குறித்து முடிவெடுப்பதற்கு முன் குடியரசுத் தலைவர் இந்திய தேர்தல் ஆணையத்தின் கருத்தைப் பெற வேண்டும் மற்றும் அதன்படி செயல்பட வேண்டும்.",
            "tip": "The ECI's opinion under Article 103 is binding on the President.",
            "fact": "For State Legislature members, Article 192 requires the Governor to obtain and act on ECI's opinion."
        },
        # 47
        {
            "id": "ER_GT_047", "diff": "Hard", "sub": "Anti-Defection Law",
            "en": "Which landmark Constitution Bench judgment of the Supreme Court held that the decision of the Speaker under the Tenth Schedule (Anti-Defection Law) is subject to judicial review?",
            "ta": "பத்தாவது அட்டவணையின் (கட்சி தாவல் தடைச் சட்டம்) கீழ் சபாநாயகர் எடுக்கும் முடிவு நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என எந்த வரலாற்று சிறப்புமிக்க வழக்கில் உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
            "opts": [("Indira Gandhi v. Raj Narain (1975)", "இந்திரா காந்தி எதிர் ராஜ் நாராயண் (1975)"), ("Kihoto Hollohan v. Zachillhu (1992)", "கிகோட்டோ ஹோலோஹான் எதிர் ஜாச்சிலு (1992)"), ("S.R. Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994)"), ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)")],
            "key": "B",
            "exp_en": "In Kihoto Hollohan v. Zachillhu (1992), a 5-judge Constitution Bench upheld the validity of the Tenth Schedule but struck down Paragraph 7 (which barred court jurisdiction), holding that the Speaker acts as a Tribunal whose orders are amenable to judicial review under Articles 226 and 136.",
            "exp_ta": "1992-ல் கிகோட்டோ ஹோலோஹான் வழக்கில், சபாநாயகர் ஒரு தீர்ப்பாயமாக செயல்படுவதால் கட்சி தாவல் குறித்த அவரது உத்தரவுகள் நீதிமன்ற மறுஆய்வுக்கு உட்பட்டவை என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "tip": "Judicial review is available only after the Speaker makes a final order, not during intermediate proceedings.",
            "fact": "The 91st Constitutional Amendment Act 2003 deleted Paragraph 3 of Tenth Schedule (which allowed one-third split)."
        },
        # 48
        {
            "id": "ER_GT_048", "diff": "Medium", "sub": "Political Party Recognition",
            "en": "Under the Election Symbols (Reservation and Allotment) Order 1968, what is the consequence if a recognized political party is derecognized by failing to poll required vote thresholds?",
            "ta": "1968 தேர்தல் சின்னங்கள் உத்தரவின் கீழ், தேவையான வாக்கு வரம்பைப் பெறத் தவறி ஒரு அங்கீகரிக்கப்பட்ட கட்சி தனது அங்கீகாரத்தை இழந்தால் என்ன விளைவு ஏற்படும்?",
            "opts": [("The party is banned completely", "அக்கட்சி முற்றிலும் தடை செய்யப்படும்"), ("The party loses its exclusive reserved symbol, but retains status as a registered unrecognized party (RUPP)", "அக்கட்சி தனது ஒதுக்கப்பட்ட பிரத்யேக சின்னத்தை இழக்கும், ஆனால் பதிவு செய்யப்பட்ட அங்கீகரிக்கப்படாத கட்சியாக (RUPP) தொடரும்"), ("Party leaders are debarred from contesting for 6 years", "கட்சித் தலைவர்கள் 6 ஆண்டுகளுக்கு போட்டியிட தடை செய்யப்படுவர்"), ("Party assets are confiscated by the state", "கட்சி சொத்துக்கள் அரசால் பறிமுதல் செய்யப்படும்")],
            "key": "B",
            "exp_en": "When a party fails to satisfy recognition criteria in subsequent general elections, it loses its status as a recognized National/State party and its reserved symbol. However, it continues to exist as a Registered Unrecognized Political Party (RUPP).",
            "exp_ta": "அங்கீகாரத்தை இழக்கும் கட்சி தனது பிரத்யேக நிரந்தர சின்னத்தை இழக்கும்; ஆனால் அது பதிவு செய்யப்பட்ட அங்கீகரிக்கப்படாத கட்சியாக (RUPP) தொடர்ந்து செயல்பட முடியும்.",
            "tip": "In 2016, ECI amended rules allowing review of recognition status once in two consecutive elections (10 years) instead of every 5 years.",
            "fact": "RUPPs must choose symbols from the list of 'Free Symbols' notified by the ECI."
        },
        # 49
        {
            "id": "ER_GT_049", "diff": "Hard", "sub": "Election Symbols",
            "en": "In Sadiq Ali v. Election Commission of India (1972), what test did the Supreme Court lay down for resolving disputes when a political party splits into rival factions claiming the party symbol?",
            "ta": "சாதிக் அலி எதிர் இந்திய தேர்தல் ஆணையம் (1972) வழக்கில், ஒரு கட்சி உடையும் போது சின்னத்திற்கு உரிமை கோரும் பிரிவினரை தீர்மானிக்க உச்ச நீதிமன்றம் வகுத்த சோதனை எது?",
            "opts": [("Test of Seniority of party leaders", "கட்சித் தலைவர்களின் மூப்பு சோதனை"), ("Test of Numerical Majority (in both organizational wing and legislative wing)", "எண்ணிக்கை பெரும்பான்மை சோதனை (கட்சி அமைப்பு மற்றும் சட்டமன்ற/நாடாளுமன்ற பிரதிநிதிகள் இரு பிரிவுகளிலும்)"), ("Test of Financial Contribution", "கட்சிக்கு அளித்த நிதிப் பங்களிப்பு சோதனை"), ("Lottery system", "குலுக்கல் முறை")],
            "key": "B",
            "exp_en": "In Sadiq Ali (1972), the Supreme Court upheld the ECI's power under Paragraph 15 of Election Symbols Order 1968 to decide disputes among rival factions of a recognized party primarily based on the 'Test of Numerical Majority' among elected MPs/MLAs and party organizational bodies.",
            "exp_ta": "1972-ல் சாதிக் அலி வழக்கில், கட்சியில் பிளவு ஏற்பட்டால் நாடாளுமன்ற/சட்டமன்ற உறுப்பினர்கள் மற்றும் பொதுக்குழு உறுப்பினர்களிடையே யாருக்கு எண்ணிக்கை பலம் (Numerical Majority) உள்ளதோ அவர்களுக்கே சின்னம் என தேர்தல் ஆணையம் முடிவெடுக்கலாம் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "tip": "Paragraph 15 of the 1968 Symbols Order governs symbol disputes in recognized parties.",
            "fact": "This test was applied in the historic Indian National Congress split of 1969 between Congress (O) and Congress (R)."
        },
        # 50
        {
            "id": "ER_GT_050", "diff": "Medium", "sub": "Voting Rights of Prisoners",
            "en": "Under Section 62(5) of the Representation of the People Act 1951, which category of confined persons is explicitly permitted to cast their vote?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 62(5)-ன் கீழ், சிறை காவலில் உள்ளவர்களில் யாருக்கு வாக்களிக்க வெளிப்படையாக அனுமதி வழங்கப்பட்டுள்ளது?",
            "opts": [("Under-trial prisoners in lawful custody", "காவலில் உள்ள விசாரணைக் கைதிகள்"), ("Persons subjected to preventive detention under any law", "தடுப்புக் காவல் சட்டத்தின் கீழ் காவலில் வைக்கப்பட்டுள்ள நபர்கள்"), ("Convicts undergoing rigorous imprisonment", "கடுங்காவல் தண்டனை அனுபவிக்கும் குற்றவாளிகள்"), ("Persons released on regular bail", "வழக்கமான ஜாமீனில் விடுவிக்கப்பட்ட நபர்கள் மட்டுமே")],
            "key": "B",
            "exp_en": "Under the proviso to Section 62(5) of RPA 1951, while convicts and undertrials confined in prison or lawful custody are barred from voting, persons subjected to 'preventive detention' under any law are expressly exempt from this bar and are entitled to cast their vote via postal ballot.",
            "exp_ta": "பிரிவு 62(5)-ன் கீழ் சிறையிலுள்ள தண்டனைக் கைதிகள் மற்றும் விசாரணைக் கைதிகளுக்கு வாக்குரிமை இல்லை; ஆனால் தடுப்புக் காவல் சட்டத்தின் கீழ் (Preventive Detention) அடைக்கப்பட்டுள்ள நபர்கள் தபால் வாக்கு மூலம் வாக்களிக்க அனுமதிக்கப்படுகிறார்கள்.",
            "tip": "Anukul Chandra Pradhan v. UOI (1997) upheld the constitutional validity of Section 62(5).",
            "fact": "Rule 18(a)(ii) of Conduct of Elections Rules 1961 provides postal ballot facilities to preventive detainees."
        }
    ]

    questions = []
    for item in q_data:
        qid = item["id"]
        opts = item["opts"]
        key = item["key"]
        idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}
        c_idx = idx_map[key]
        
        why_en = {}
        why_ta = {}
        for opt_k in ["A", "B", "C", "D"]:
            o_idx = idx_map[opt_k]
            if opt_k == key:
                why_en[opt_k] = f"Option {opt_k} is the correct answer according to constitutional and statutory provisions."
                why_ta[opt_k] = f"அரசியலமைப்பு மற்றும் சட்ட விதிகளின்படி தெரிவு {opt_k} சரியான விடையாகும்."
            else:
                why_en[opt_k] = f"Option {opt_k} ({opts[o_idx][0]}) is incorrect."
                why_ta[opt_k] = f"தெரிவு {opt_k} ({opts[o_idx][1]}) தவறானது."
                
        q = make_er_q(
            qid=qid,
            diff=item["diff"],
            qtype="Single Choice",
            subtopic=item["sub"],
            en_stem=item["en"],
            ta_stem=item["ta"],
            en_a=opts[0][0],
            ta_a=opts[0][1],
            en_b=opts[1][0],
            ta_b=opts[1][1],
            en_c=opts[2][0],
            ta_c=opts[2][1],
            en_d=opts[3][0],
            ta_d=opts[3][1],
            correct_key=key,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=why_en["A"],
            why_a_ta=why_ta["A"],
            why_b_en=why_en["B"],
            why_b_ta=why_ta["B"],
            why_c_en=why_en["C"],
            why_c_ta=why_ta["C"],
            why_d_en=why_en["D"],
            why_d_ta=why_ta["D"],
            tip_en=item["tip"],
            tip_ta=f"நினைவில் கொள்க: {item['tip']}",
            fact_en=item["fact"],
            fact_ta=f"முக்கிய தகவல்: {item['fact']}",
            tags=["polity", "electoral_reforms", "grand_test"]
        )
        questions.append(q)
        
    return questions

if __name__ == "__main__":
    qs = get_gt_part1_questions()
    print(f"Grand Test Part 1 generated {len(qs)} questions.")
