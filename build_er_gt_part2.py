# -*- coding: utf-8 -*-
"""
Grand Test Part 2 (Questions ER_GT_051 to ER_GT_100) for Electoral Reforms.
Covering:
- Political funding reforms & Electoral Bonds 2024 verdict
- Section 29C contribution reports & Section 182 Companies Act
- Foreign Contributions & FCRA 2010 rules
- Remote Voting Machine (RVM) prototype for domestic migrants
- Women's Reservation 106th Amendment Act 2023 (Articles 330A, 332A, 239AA)
- Simultaneous Elections / ONOE (Kovind High-Level Committee 2024)
- ECI Appointments Act 2023 & Anoop Baranwal jurisprudence
- Landmark Supreme Court cases (S.S. Dhanoa, T.N. Seshan, Kanhiya Lal Omar, etc.)
- Contemporary reforms (Aadhaar linkage, fake news, deepfakes, AI in elections)
"""
from er_mcq_helper import make_er_q

def get_gt_part2_questions():
    q_data = [
        # 51
        {
            "id": "ER_GT_051", "diff": "Medium", "sub": "Political Financing",
            "en": "Under Section 29C of the Representation of the People Act 1951, a political party must submit an annual contribution report to the ECI declaring donations exceeding what amount?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 29C-ன் கீழ், ஒரு அரசியல் கட்சி எந்தத் தொகைக்கு மேற்பட்ட நன்கொடைகளை தேர்தல் ஆணையத்திற்கு சமர்ப்பிக்கும் பங்களிப்பு அறிக்கையில் கட்டாயம் அறிவிக்க வேண்டும்?",
            "opts": [("Rs 5,000", "ரூ. 5,000"), ("Rs 10,000", "ரூ. 10,000"), ("Rs 20,000", "ரூ. 20,000"), ("Rs 50,000", "ரூ. 50,000")],
            "key": "C",
            "exp_en": "Under Section 29C of RPA 1951, the treasurer of every registered political party must submit a report before due date declaring all individual/company contributions received in excess of Rs 20,000 in that financial year.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 29C-ன் கீழ், ஒரு நிதியாண்டில் நபர்கள் அல்லது நிறுவனங்களிடமிருந்து பெறப்பட்ட ரூ. 20,000-க்கு மேற்பட்ட அனைத்து நன்கொடைகளையும் அரசியல் கட்சிகள் தேர்தல் ஆணையத்திடம் அறிக்கையாக அளிக்க வேண்டும்.",
            "tip": "Failure to submit Form 24A contribution report under Section 29C forfeits the party's 100% tax exemption under Section 13A of the Income Tax Act.",
            "fact": "The report must be submitted every year before the due date for furnishing the income tax return."
        },
        # 52
        {
            "id": "ER_GT_052", "diff": "Hard", "sub": "Corporate Donations",
            "en": "Under Section 182 of the Companies Act 2013 (prior to the Finance Act 2017 amendment struck down in 2024), what was the statutory cap on corporate political contributions?",
            "ta": "நிறுவனங்கள் சட்டம் 2013-ன் பிரிவு 182-ன் கீழ் (2017 திருத்தத்திற்கு முன்பு), நிறுவனங்கள் அரசியல் கட்சிகளுக்கு வழங்கக்கூடிய சட்டப்பூர்வ நிதி வரம்பு என்னவாக இருந்தது?",
            "opts": [("5% of average net profits of preceding 3 financial years", "முந்தைய 3 நிதியாண்டுகளின் சராசரி நிகர லாபத்தில் 5%"), ("7.5% of average net profits of preceding 3 financial years", "முந்தைய 3 நிதியாண்டுகளின் சராசரி நிகர லாபத்தில் 7.5%"), ("10% of total annual turnover", "மொத்த ஆண்டு விற்றுமுதலில் 10%"), ("No limit was ever imposed", "எந்த வரம்பும் விதிக்கப்பட்டதில்லை")],
            "key": "B",
            "exp_en": "Section 182(1) of the Companies Act 2013 originally capped political contributions by a company at 7.5% of its average net profits during the three immediately preceding financial years, and barred companies in existence for less than 3 years from contributing.",
            "exp_ta": "நிறுவனங்கள் சட்டம் 2013 பிரிவு 182(1)-ன் கீழ், முந்தைய மூன்று நிதியாண்டுகளின் சராசரி நிகர லாபத்தில் அதிகபட்சம் 7.5% மட்டுமே நிறுவனங்கள் அரசியல் நன்கொடையாக வழங்க முடியும் என்ற வரம்பு இருந்தது.",
            "tip": "The Finance Act 2017 removed this 7.5% cap; the Supreme Court struck down this removal in ADR (2024).",
            "fact": "Companies also had to name the specific political party and amount contributed in their Profit and Loss accounts."
        },
        # 53
        {
            "id": "ER_GT_053", "diff": "Hard", "sub": "Electoral Bonds Verdict 2024",
            "en": "In ADR v. Union of India (2024), which state-owned public sector bank had been designated as the sole authorized issuer of Electoral Bonds?",
            "ta": "ஏடிஆர் எதிர் இந்திய ஒன்றியம் (2024) வழக்கின்படி, தேர்தல் பத்திரங்களை வெளியிட அங்கீகரிக்கப்பட்ட ஒரே பொதுத்துறை வங்கி எது?",
            "opts": [("Reserve Bank of India (RBI)", "இந்திய ரிசர்வ் வங்கி (RBI)"), ("State Bank of India (SBI)", "பாரத ஸ்டேட் வங்கி (SBI)"), ("Punjab National Bank (PNB)", "பஞ்சாப் நேஷனல் வங்கி (PNB)"), ("Bank of Baroda", "பேங்க் ஆஃப் பரோடா")],
            "key": "B",
            "exp_en": "Under the Electoral Bond Scheme 2018, the State Bank of India (SBI) was the only bank authorized to issue, sell, and encash Electoral Bonds at designated main branches.",
            "exp_ta": "2018 தேர்தல் பத்திரத் திட்டத்தின் கீழ், பாரத ஸ்டேட் வங்கி (SBI) மட்டுமே குறிப்பிட்ட முக்கிய கிளைகள் மூலம் தேர்தல் பத்திரங்களை விற்கவும் மாற்றவும் அதிகாரம் பெற்ற ஒரே வங்கியாக இருந்தது.",
            "tip": "Electoral bonds were sold in denominations of Rs 1,000, Rs 10,000, Rs 1 Lakh, Rs 10 Lakhs, and Rs 1 Crore.",
            "fact": "The validity of an electoral bond was only 15 calendar days from the date of issue."
        },
        # 54
        {
            "id": "ER_GT_054", "diff": "Medium", "sub": "Electoral Bonds Verdict 2024",
            "en": "Under the 2018 Electoral Bond Scheme, what was the validity period of an Electoral Bond within which it had to be encashed by an eligible political party?",
            "ta": "2018 தேர்தல் பத்திரத் திட்டத்தின் கீழ், தகுதியுள்ள அரசியல் கட்சியால் தேர்தல் பத்திரம் மாற்றப்பட வேண்டிய செல்லுபடியாகும் கால வரம்பு என்ன?",
            "opts": [("7 days", "7 நாட்கள்"), ("15 calendar days", "15 காலண்டர் நாட்கள்"), ("30 days", "30 நாட்கள்"), ("90 days", "90 நாட்கள்")],
            "key": "B",
            "exp_en": "An Electoral Bond was valid for only 15 calendar days from the date of issuance. If not encashed within 15 days, the amount was deposited into the Prime Minister's National Relief Fund (PMNRF).",
            "exp_ta": "தேர்தல் பத்திரம் வழங்கப்பட்ட நாளிலிருந்து 15 நாட்களுக்கு மட்டுமே செல்லுபடியாகும்; 15 நாட்களுக்குள் மாற்றப்படாவிட்டால் அந்த நிதி பிரதமரின் தேசிய நிவாரண நிதிக்கு சென்றுவிடும்.",
            "tip": "Only parties securing at least 1% of votes polled in the last Lok Sabha or Assembly election were eligible to encash them.",
            "fact": "Over Rs 16,500 crore worth of electoral bonds were purchased between 2018 and 2024."
        },
        # 55
        {
            "id": "ER_GT_055", "diff": "Hard", "sub": "Foreign Contributions",
            "en": "Under Section 3 of the Foreign Contribution (Regulation) Act, 2010 (FCRA), which of the following entities is strictly prohibited from accepting foreign contributions?",
            "ta": "வெளிநாட்டு பங்களிப்பு (ஒழுங்குமுறை) சட்டம் 2010 (FCRA)-ன் பிரிவு 3-ன் கீழ், வெளிநாட்டு பங்களிப்புகளைப் பெற கீழ்க்கண்டவர்களில் யாருக்கு முற்றிலும் தடை விதிக்கப்பட்டுள்ளது?",
            "opts": [("Public limited commercial companies", "பொது வர்த்தக நிறுவனங்கள்"), ("Candidates for election, political parties, and members of any legislature", "தேர்தல் வேட்பாளர்கள், அரசியல் கட்சிகள் மற்றும் சட்டமன்ற/நாடாளுமன்ற உறுப்பினர்கள்"), ("Charitable non-governmental hospitals", "அரசு சாரா அறக்கட்டளை மருத்துவமனைகள்"), ("Universities and educational trusts", "பல்கலைக்கழகங்கள் மற்றும் கல்வி அறக்கட்டளைகள்")],
            "key": "B",
            "exp_en": "Section 3(1) of FCRA 2010 explicitly prohibits election candidates, political parties, party office-bearers, members of any Legislature, judges, and journalists from accepting any foreign contribution.",
            "exp_ta": "FCRA 2010 பிரிவு 3(1), தேர்தல் வேட்பாளர்கள், அரசியல் கட்சிகள், மக்கள் பிரதிநிதிகள் மற்றும் நீதிபதிகள் வெளிநாட்டு பங்களிப்பு அல்லது நிதியை பெறுவதை முற்றிலும் தடை செய்கிறது.",
            "tip": "Finance Act 2016 retrospectively amended FCRA to allow foreign companies with 50%+ foreign shareholding compliant with FEMA to donate.",
            "fact": "Violation of FCRA Section 3 is a cognizable penal offence."
        },
        # 56
        {
            "id": "ER_GT_056", "diff": "Medium", "sub": "Electoral Technology",
            "en": "In December 2022, the Election Commission developed a prototype of which device to enable domestic migrant electors to vote from their current places of residence?",
            "ta": "2022 டிசம்பரில், உள்நாட்டு புலம்பெயர்ந்த தொழிலாளர்கள் தங்களின் தற்போதைய வசிப்பிடத்திலிருந்தே வாக்களிக்க வசதியாக இந்திய தேர்தல் ஆணையம் எந்த முன்மாதிரி இயந்திரத்தை உருவாக்கியது?",
            "opts": [("Mobile Internet Voting App", "மொபைல் இணைய வாக்குப்பதிவு செயலி"), ("Remote Electronic Voting Machine (RVM)", "தொலைதூர மின்னணு வாக்குப்பதிவு இயந்திரம் (RVM)"), ("Blockchain Ballot Terminal", "பிளாக்செயின் வாக்கு முனையம்"), ("SMS Voting System", "எஸ்.எம்.எஸ் வாக்குப்பதிவு முறை")],
            "key": "B",
            "exp_en": "In December 2022, the ECI unveiled a prototype Multi-Constituency Remote Electronic Voting Machine (RVM) developed with ECIL and BEL that can handle up to 72 constituencies from a single remote polling station for domestic migrants.",
            "exp_ta": "2022 டிசம்பரில், உள்நாட்டு புலம்பெயர் வாக்காளர்களுக்காக ஒரே வாக்குச்சாவடியிலிருந்து 72 தொகுதிகளுக்கு வாக்களிக்கக்கூடிய தொலைதூர மின்னணு வாக்குப்பதிவு இயந்திர (RVM) முன்மாதிரியை தேர்தல் ஆணையம் அறிமுகப்படுத்தியது.",
            "tip": "RVM uses dynamic electronic display instead of a fixed printed paper ballot sheet.",
            "fact": "The prototype was demonstrated to recognized political parties in January 2023."
        },
        # 57
        {
            "id": "ER_GT_057", "diff": "Hard", "sub": "Remote Voting",
            "en": "How many constituencies can a single Multi-Constituency Remote Electronic Voting Machine (RVM) prototype cater to from a single remote polling booth?",
            "ta": "ஒற்றை தொலைதூர வாக்குச்சாவடியிலிருந்து ஒரு பல-தொகுதி தொலைதூர வாக்குப்பதிவு இயந்திர (RVM) முன்மாதிரி எத்தனை தொகுதிகளைக் கையாள முடியும்?",
            "opts": [("16 constituencies", "16 தொகுதிகள்"), ("36 constituencies", "36 தொகுதிகள்"), ("72 constituencies", "72 தொகுதிகள்"), ("100 constituencies", "100 தொகுதிகள்")],
            "key": "C",
            "exp_en": "The prototype Multi-Constituency RVM developed by BEL and ECIL can handle up to 72 different constituencies simultaneously using a dynamic digital display unit.",
            "exp_ta": "BEL மற்றும் ECIL இணைந்து உருவாக்கிய RVM முன்மாதிரி இயந்திரம், ஒரே நேரத்தில் 72 வெவ்வேறு தொகுதிகளைக் கையாளும் திறன் கொண்டது.",
            "tip": "Electors would scan their constituency card to load their specific candidate list on screen.",
            "fact": "RVM remains a standalone device without internet connectivity, adhering to the security architecture of standard EVMs."
        },
        # 58
        {
            "id": "ER_GT_058", "diff": "Medium", "sub": "Women's Representation",
            "en": "Which Article was newly inserted into the Constitution by the 106th Constitutional Amendment Act 2023 to provide 33% reservation for women in the House of the People (Lok Sabha)?",
            "ta": "மக்களவையில் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்க 106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023 மூலம் அரசியலமைப்பில் புதிதாக சேர்க்கப்பட்ட சரத்து எது?",
            "opts": [("Article 330", "சரத்து 330"), ("Article 330A", "சரத்து 330A"), ("Article 332A", "சரத்து 332A"), ("Article 334A", "சரத்து 334A")],
            "key": "B",
            "exp_en": "Article 330A was inserted by the 106th Amendment Act 2023 to reserve seats for women in the Lok Sabha, including one-third of seats reserved for SCs and STs under Article 330.",
            "exp_ta": "106-வது திருத்தச் சட்டம் 2023 மூலம் சேர்க்கப்பட்ட சரத்து 330A, மக்களவையில் பெண்களுக்கு 33% இடஒதுக்கீட்டை (SC/ST தனித்தொகுதிகளில் மூன்றில் ஒரு பங்கு உட்பட) வழங்குகிறது.",
            "tip": "Article 330A = Lok Sabha; Article 332A = State Assemblies; Article 334A = Sunset clause.",
            "fact": "Women's reservation will operate through rotation of seats after every delimitation."
        },
        # 59
        {
            "id": "ER_GT_059", "diff": "Medium", "sub": "Women's Representation",
            "en": "Which Article inserted by the 106th Constitutional Amendment Act 2023 provides 33% reservation for women in State Legislative Assemblies?",
            "ta": "மாநில சட்டமன்றங்களில் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்க 106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023 மூலம் சேர்க்கப்பட்ட சரத்து எது?",
            "opts": [("Article 331", "சரத்து 331"), ("Article 332", "சரத்து 332"), ("Article 332A", "சரத்து 332A"), ("Article 333", "சரத்து 333")],
            "key": "C",
            "exp_en": "Article 332A was inserted by the 106th Amendment Act 2023 to reserve one-third of the total seats in the Legislative Assembly of every State for women.",
            "exp_ta": "106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023 மூலம் சேர்க்கப்பட்ட சரத்து 332A, ஒவ்வொரு மாநில சட்டமன்றத்தின் மொத்த இடங்களில் மூன்றில் ஒரு பங்கை பெண்களுக்கு ஒதுக்குகிறது.",
            "tip": "Article 332 covers SC/ST reservation in Assemblies; Article 332A covers Women's reservation.",
            "fact": "Women will also be allocated one-third of seats reserved for SCs and STs in State Assemblies."
        },
        # 60
        {
            "id": "ER_GT_060", "diff": "Hard", "sub": "Women's Representation",
            "en": "Under Article 334A inserted by the 106th Constitutional Amendment Act 2023, when will the women's reservation provision come into operational effect?",
            "ta": "106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023-ல் சேர்க்கப்பட்ட சரத்து 334A-ன் கீழ், மகளிர் இடஒதுக்கீடு எப்போது நடைமுறைக்கு வரும்?",
            "opts": [("Immediately from the 2024 General Elections", "2024 பொதுத்தேர்தலில் இருந்து உடனடியாக"), ("After an exercise of delimitation is undertaken for this purpose after relevant figures for the first Census conducted post-commencement are published", "சட்டம் அமலுக்கு வந்த பிறகு எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பு புள்ளிவிவரங்கள் வெளியிடப்பட்ட பின் நடத்தப்படும் தொகுதி மறுவரையறைக்குப் பிறகு"), ("On 1 January 2030 automatically", "2030 ஜனவரி 1 அன்று தானாகவே"), ("When 50% of states pass resolutions", "50% மாநிலங்கள் தீர்மானம் நிறைவேற்றும்போது")],
            "key": "B",
            "exp_en": "Article 334A(1) specifies that the provisions relating to women's reservation shall come into effect after an exercise of delimitation is undertaken based on the relevant figures of the first Census taken after the commencement of the Act.",
            "exp_ta": "சரத்து 334A(1)-ன் படி, இந்த சட்டம் அமலுக்கு வந்த பிறகு நடத்தப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பு புள்ளிவிவரங்களின் அடிப்படையில் தொகுதி மறுவரையறை செய்யப்பட்ட பின்னரே மகளிர் இடஒதுக்கீடு நடைமுறைக்கு வரும்.",
            "tip": "Women's reservation is constitutionally tied to Census publication and delimitation.",
            "fact": "Article 334A also sets a sunset clause of 15 years from commencement, extendable by Parliament."
        },
        # 61
        {
            "id": "ER_GT_061", "diff": "Medium", "sub": "Women's Representation",
            "en": "What is the initial duration (sunset clause) specified in Article 334A for the operation of women's reservation in Lok Sabha and State Assemblies?",
            "ta": "மக்களவை மற்றும் சட்டமன்றங்களில் மகளிர் இடஒதுக்கீடு செயல்படுவதற்காக சரத்து 334A-ல் குறிப்பிடப்பட்டுள்ள ஆரம்ப கால அவகாசம் (Sunset clause) என்ன?",
            "opts": [("10 years", "10 ஆண்டுகள்"), ("15 years", "15 ஆண்டுகள்"), ("20 years", "20 ஆண்டுகள்"), ("25 years", "25 ஆண்டுகள்")],
            "key": "B",
            "exp_en": "Under Article 334A(1), the reservation of seats for women shall cease to have effect on the expiration of a period of 15 years from the date of its commencement, unless extended by law enacted by Parliament.",
            "exp_ta": "சரத்து 334A(1)-ன் படி, நாடாளுமன்றம் சட்டத்தின் மூலம் நீட்டிக்காவிட்டால், மகளிர் இடஒதுக்கீடு அமலுக்கு வந்த நாளிலிருந்து 15 ஆண்டுகள் முடிந்தவுடன் காலாவதியாகிவிடும்.",
            "tip": "Similar to original SC/ST reservation which was initially for 10 years and extended periodically.",
            "fact": "Parliament retains the constitutional power to extend the 15-year period by law."
        },
        # 62
        {
            "id": "ER_GT_062", "diff": "Medium", "sub": "Simultaneous Elections",
            "en": "The High-Level Committee on Simultaneous Elections (One Nation, One Election) which submitted its report in March 2024 was headed by whom?",
            "ta": "மார்ச் 2024-ல் தனது அறிக்கையை சமர்ப்பித்த ஒரே நாடு ஒரே தேர்தல் (Simultaneous Elections) உயர்மட்டக் குழு யாருடைய தலைமையில் அமைக்கப்பட்டது?",
            "opts": [("Justice Ranjan Gogoi", "நீதிபதி ரஞ்சன் கோகோய்"), ("Ram Nath Kovind (Former President of India)", "ராம் நாத் கோவிந்த் (முன்னாள் இந்திய குடியரசுத் தலைவர்)"), ("Justice B.S. Chauhan", "நீதிபதி பி.எஸ். சவுகான்"), ("N.K. Singh", "என்.கே. சிங்")],
            "key": "B",
            "exp_en": "The High-Level Committee on Simultaneous Elections was constituted by the Union Government in September 2023 under the chairmanship of former President of India Ram Nath Kovind and submitted its report on 14 March 2024.",
            "exp_ta": "ஒரே நாடு ஒரே தேர்தல் குறித்த உயர்மட்டக் குழு, முன்னாள் இந்திய குடியரசுத் தலைவர் ராம் நாத் கோவிந்த் தலைமையில் அமைக்கப்பட்டு 2024 மார்ச் 14 அன்று தனது அறிக்கையை சமர்ப்பித்தது.",
            "tip": "Members included Home Minister Amit Shah, Ghulam Nabi Azad, N.K. Singh, Subhash C. Kashyap, and Harish Salve.",
            "fact": "The committee submitted a comprehensive 18,626-page report to President Droupadi Murmu."
        },
        # 63
        {
            "id": "ER_GT_063", "diff": "Hard", "sub": "Simultaneous Elections",
            "en": "What two-step phased framework was recommended by the Ram Nath Kovind Committee to implement simultaneous elections in India?",
            "ta": "இந்தியாவில் ஒரே நேரத்தில் தேர்தல்களை நடத்த ராம் நாத் கோவிந்த் குழு பரிந்துரைத்த இரு-கட்ட கட்டமைப்பு எது?",
            "opts": [("Direct Presidential decree", "நேரடி குடியரசுத் தலைவர் ஆணை"), ("Step 1: Synchronize Lok Sabha and State Assemblies; Step 2: Hold Local Body (Panchayat/Municipality) elections within 100 days of General Elections", "படி 1: மக்களவை மற்றும் மாநில சட்டமன்ற தேர்தல்களை ஒருங்கிணைத்தல்; படி 2: பொதுத்தேர்தல் முடிந்த 100 நாட்களுக்குள் உள்ளாட்சித் தேர்தல்களை நடத்துதல்"), ("Abolishing state governments", "மாநில அரசுகளை ரத்து செய்தல்"), ("Holding elections state by state over 5 years", "5 ஆண்டுகளில் ஒவ்வொரு மாநிலமாக தேர்தல் நடத்துதல்")],
            "key": "B",
            "exp_en": "The Kovind Committee recommended a two-phase rollout: Phase 1 brings Lok Sabha and all State Legislative Assemblies into sync (requiring no state ratification); Phase 2 synchronizes local body elections within 100 days of national polls (requiring ratification by at least half the states).",
            "exp_ta": "கோவிந்த் குழு பரிந்துரை: முதற்கட்டமாக மக்களவை மற்றும் சட்டமன்ற தேர்தல்கள் ஒரே நேரத்தில் நடத்தப்படும்; இரண்டாம் கட்டமாக பொதுத்தேர்தல் முடிந்த 100 நாட்களுக்குள் உள்ளாட்சி தேர்தல்கள் நடத்தப்படும்.",
            "tip": "Phase 1 requires constitutional amendment under Article 83 and 172; Phase 2 requires Article 324A amendment.",
            "fact": "The committee proposed inserting Article 82A to notify an 'Appointed Date'."
        },
        # 64
        {
            "id": "ER_GT_064", "diff": "Hard", "sub": "Simultaneous Elections",
            "en": "What mechanism did the Kovind Committee recommend in the event of a hung House, no-confidence motion, or premature dissolution during a synchronized cycle?",
            "ta": "ஒருங்கிணைந்த தேர்தல் சுழற்சியின் போது தொங்கு நாடாளுமன்றம் அல்லது முன்கூட்டியே ஆட்சி கலைக்கப்பட்டால் என்ன செய்ய வேண்டும் என கோவிந்த் குழு பரிந்துரைத்தது?",
            "opts": [("Directly impose President's Rule until the next 5-year cycle", "அடுத்த 5 ஆண்டு சுழற்சி வரை நேரடியாக குடியரசுத் தலைவர் ஆட்சியை அமல்படுத்துவது"), ("Conduct fresh elections only for the unexpired remainder of the 5-year term (Unexpired Term)", "5 ஆண்டு காலத்தின் மீதமுள்ள காலத்திற்கு மட்டுமே புதிய தேர்தலை நடத்துவது (மீதமுள்ள காலம்)"), ("Abolish the legislature permanently", "சட்டமன்றத்தை நிரந்தரமாக ரத்து செய்வது"), ("Declare the second largest party elected", "இரண்டாவது பெரிய கட்சியை வெற்றி பெற்றதாக அறிவிப்பது")],
            "key": "B",
            "exp_en": "To maintain synchronization, the Kovind Committee recommended that in the event of premature dissolution, fresh elections will be held only for the 'unexpired portion of the term', so that all houses dissolve together at the end of the full cycle.",
            "exp_ta": "தேர்தல் சுழற்சி சிதையாமல் இருக்க, இடையில் ஆட்சி கலைக்கப்பட்டால் நடத்தப்படும் புதிய தேர்தல் 5 ஆண்டுகளுக்கு அல்லாமல் முந்தைய அவையின் 'மீதமுள்ள காலத்திற்கு மட்டுமே' செயல்படும் என கோவிந்த் குழு பரிந்துரைத்தது.",
            "tip": "Prevents mid-term elections from permanently desynchronizing the national calendar.",
            "fact": "This model mirrors municipal council provisions where bye-elected bodies serve only the remainder term."
        },
        # 65
        {
            "id": "ER_GT_065", "diff": "Medium", "sub": "Simultaneous Elections",
            "en": "What did the Kovind Committee recommend regarding the preparation of electoral rolls for Parliamentary, Assembly, and Local Body elections?",
            "ta": "நாடாளுமன்றம், சட்டமன்றம் மற்றும் உள்ளாட்சித் தேர்தல்களுக்கான வாக்காளர் பட்டியல் தயாரிப்பு குறித்து கோவிந்த் குழு என்ன பரிந்துரைத்தது?",
            "opts": [("Maintaining three completely separate rolls", "மூன்று முற்றிலும் தனித்தனி பட்டியல்களை பராமரிப்பது"), ("Preparation of a Single Common Electoral Roll and Single Photo Identity Card by ECI in consultation with SECs", "மாநில தேர்தல் ஆணையங்களுடன் கலந்தாலோசித்து ECI மூலம் ஒற்றை பொது வாக்காளர் பட்டியல் மற்றும் ஒற்றை அடையாள அட்டையை உருவாக்குவது"), ("Outsourcing voter rolls to private banks", "வாக்காளர் பட்டியலை தனியார் வங்கிகளுக்கு வழங்குவது"), ("Abolishing voter registration completely", "வாக்காளர் பதிவை முற்றிலும் ரத்து செய்வது")],
            "key": "B",
            "exp_en": "The committee recommended amending Article 325 to introduce a Single Common Electoral Roll and Single Elector Photo Identity Card (EPIC) prepared by the ECI in consultation with State Election Commissions, eliminating conflicting voter lists.",
            "exp_ta": "சரத்து 325-ஐ திருத்தி, மாநில தேர்தல் ஆணையங்களுடன் கலந்தாலோசித்து ECI மூலம் நாடாளுமன்ற, சட்டமன்ற மற்றும் உள்ளாட்சித் தேர்தல்களுக்கு ஒற்றை பொது வாக்காளர் பட்டியலை உருவாக்க பரிந்துரைத்தது.",
            "tip": "Currently, ECI prepares rolls for Parliament/Assemblies, while SECs prepare separate rolls for local bodies in many states.",
            "fact": "A common roll saves hundreds of crores and eliminates citizen confusion."
        },
        # 66
        {
            "id": "ER_GT_066", "diff": "Medium", "sub": "ECI Appointments",
            "en": "Who acts as the Chairperson of the Search Committee constituted under Section 6 of the Chief Election Commissioner and other Election Commissioners Act, 2023?",
            "ta": "2023 தலைமை தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்கள் சட்டத்தின் பிரிவு 6-ன் கீழ் அமைக்கப்பட்ட தேடல் குழுவின் தலைவராக செயல்படுபவர் யார்?",
            "opts": [("Cabinet Secretary", "மத்திய கேபினட் செயலாளர்"), ("Minister of Law and Justice", "மத்திய சட்டம் மற்றும் நீதித்துறை அமைச்சர்"), ("Home Minister of India", "மத்திய உள்துறை அமைச்சர்"), ("Attorney General of India", "இந்திய அட்டர்னி ஜெனரல்")],
            "key": "B",
            "exp_en": "Under Section 6 of the 2023 Act, the Search Committee is headed by the Minister of Law and Justice, with two other members not below the rank of Secretary to the Government of India, tasked with preparing a panel of 5 persons for the Selection Committee.",
            "exp_ta": "2023 சட்டத்தின் பிரிவு 6-ன் படி, தேடல் குழு மத்திய சட்டம் மற்றும் நீதித்துறை அமைச்சர் தலைமையில் செயல்பட்டு, தேர்வு குழுவின் பரிசீலனைக்கு 5 நபர்கள் கொண்ட குழுவை பரிந்துரைக்கிறது.",
            "tip": "Search Committee is headed by Law Minister; Selection Committee is headed by Prime Minister.",
            "fact": "The panel prepares names of persons who hold or have held a post equivalent to Secretary to the Government of India."
        },
        # 67
        {
            "id": "ER_GT_067", "diff": "Hard", "sub": "ECI Appointments",
            "en": "Under Section 8 of the Chief Election Commissioner and other ECs Act 2023, is the Selection Committee strictly restricted to recommending names from the Search Committee's panel?",
            "ta": "2023 தலைமை தேர்தல் ஆணையர் சட்டத்தின் பிரிவு 8-ன் கீழ், தேடல் குழு தயாரித்த பட்டியலிலிருந்து மட்டுமே தேர்வு குழு பெயர்களைப் பரிந்துரைக்க முடியுமா?",
            "opts": [("Yes, strictly limited to the panel of five names", "ஆம், 5 நபர்கள் கொண்ட பட்டியலிலிருந்து மட்டுமே தேர்ந்தெடுக்க முடியும்"), ("No, the Selection Committee may also consider any other person outside the panel prepared by the Search Committee", "இல்லை, தேடல் குழுவின் பட்டியலில் இல்லாத வேறு தகுதியான நபர்களையும் தேர்வு குழு பரிசீலிக்க முடியும்"), ("Only if the Chief Justice of India consents", "உச்ச நீதிமன்ற தலைமை நீதிபதி ஒப்புதல் அளித்தால் மட்டுமே"), ("Only during national emergency", "தேசிய அவசரநிலையின் போது மட்டுமே")],
            "key": "B",
            "exp_en": "Section 8(2) of the 2023 Act provides that the Selection Committee may also consider any other person who was not included in the panel prepared by the Search Committee, giving the executive full flexibility.",
            "exp_ta": "பிரிவு 8(2)-ன் படி, தேடல் குழுவின் பட்டியலில் இடம்பெறாத எந்தவொரு தகுதியான பிற நபரின் பெயரையும் தேர்வு குழு நேரடியாகப் பரிசீலித்து நியமிக்க அதிகாரம் உண்டு.",
            "tip": "This flexibility clause was one of the contentious points raised by petitioners in the Supreme Court.",
            "fact": "The Selection Committee regulates its own procedure in a transparent manner."
        },
        # 68
        {
            "id": "ER_GT_068", "diff": "Medium", "sub": "ECI Autonomy",
            "en": "Under the proviso to Article 324(5) of the Constitution, what is the procedure for removing the Chief Election Commissioner (CEC) from office?",
            "ta": "அரசியலமைப்பின் சரத்து 324(5)-ன் கீழ், தலைமை தேர்தல் ஆணையரை (CEC) பதவியிலிருந்து நீக்குவதற்கான நடைமுறை என்ன?",
            "opts": [("Simple order of the Prime Minister", "பிரதமரின் நேரடி உத்தரவு மூலம்"), ("In like manner and on the like grounds as a Judge of the Supreme Court (Parliamentary Impeachment)", "உச்ச நீதிமன்ற நீதிபதியை நீக்குவது போன்ற அதே நடைமுறை மற்றும் காரணங்களின் அடிப்படையில் (நாடாளுமன்ற கண்டனத் தீர்மானம்)"), ("By a resolution of the Rajya Sabha alone", "மாநிலங்களவையின் தீர்மானம் மூலம் மட்டுமே"), ("By the Union Cabinet passing a resolution", "மத்திய அமைச்சரவை தீர்மானம் நிறைவேற்றுவதன் மூலம்")],
            "key": "B",
            "exp_en": "Article 324(5) guarantees constitutional security of tenure to the CEC: he shall not be removed from his office except in like manner and on the like grounds as a Judge of the Supreme Court (proved misbehaviour or incapacity via special majority in both Houses).",
            "exp_ta": "சரத்து 324(5)-ன் கீழ், தலைமை தேர்தல் ஆணையரை உச்ச நீதிமன்ற நீதிபதியை நாடாளுமன்றத்தில் சிறப்பு பெரும்பான்மையுடன் நீக்குவதைப் போன்ற கண்டனத் தீர்மான நடைமுறை மூலமே நீக்க முடியும்.",
            "tip": "CEC has constitutional impeachment protection; however, other Election Commissioners can be removed by the President on the recommendation of the CEC.",
            "fact": "No Chief Election Commissioner has ever been removed from office by impeachment in India."
        },
        # 69
        {
            "id": "ER_GT_069", "diff": "Hard", "sub": "ECI Autonomy",
            "en": "In T.N. Seshan v. Union of India (1995), what did the 5-judge Constitution Bench rule regarding the relationship between the Chief Election Commissioner and other Election Commissioners?",
            "ta": "டி.என். சேஷன் எதிர் இந்திய ஒன்றியம் (1995) வழக்கில், தலைமை தேர்தல் ஆணையருக்கும் பிற தேர்தல் ஆணையர்களுக்கும் இடையிலான உறவு குறித்து 5 நீதிபதிகள் கொண்ட அமர்வு என்ன தீர்ப்பளித்தது?",
            "opts": [("CEC is the absolute hierarchical superior and can veto any decision", "தலைமை தேர்தல் ஆணையரே முழு அதிகாரம் கொண்டவர்; அவர் மற்றவர்களின் முடிவை நிராகரிக்கலாம்"), ("All three Commissioners are equal in power and status, and decisions must be made unanimously or by majority vote", "மூன்று ஆணையர்களும் சம அதிகாரமும் அந்தஸ்தும் கொண்டவர்கள்; முடிவுகள் ஒருமனதாகவோ அல்லது பெரும்பான்மை வாக்கு அடிப்படையிலோ எடுக்கப்பட வேண்டும்"), ("Election Commissioners act only as advisory clerks", "பிற ஆணையர்கள் வெறும் ஆலோசனை உதவியாளர்கள் மட்டுமே"), ("CEC holds two votes in every Commission meeting", "தலைமை தேர்தல் ஆணையருக்கு இரு வாக்குகள் உண்டு")],
            "key": "B",
            "exp_en": "In T.N. Seshan (1995), CJI A.M. Ahmadi's bench held that the Election Commission is an institution where the CEC and the two ECs are equal in status and voting power. Under Section 10 of the 1991 Act, all business must be transacted unanimously, or in case of dissent, decided by the majority.",
            "exp_ta": "டி.என். சேஷன் வழக்கில், தலைமை தேர்தல் ஆணையரும் பிற இரு ஆணையர்களும் சம அந்தஸ்து கொண்டவர்கள் என்றும், கருத்து வேறுபாடு ஏற்பட்டால் பெரும்பான்மை முடிவே இறுதியானது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "tip": "CEC is 'primus inter pares' (first among equals) in administrative protocol, but has equal voting power.",
            "fact": "This ruling upheld the validity of the 1993 ordinance multi-membering the Commission."
        },
        # 70
        {
            "id": "ER_GT_070", "diff": "Medium", "sub": "ECI History",
            "en": "In S.S. Dhanoa v. Union of India (1991), what was challenged before the Supreme Court following the abolition of the multi-member Commission in 1990?",
            "ta": "எஸ்.எஸ். தனோவா எதிர் இந்திய ஒன்றியம் (1991) வழக்கில், 1990-ல் பல உறுப்பினர் தேர்தல் ஆணையம் ரத்து செய்யப்பட்டதை எதிர்த்து தொடரப்பட்ட வழக்கில் உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "opts": [("The appointment of Sukumar Sen was invalid", "சுகுமார் சென் நியமனம் செல்லாது"), ("The abolition of the posts of Election Commissioners by the President under Article 324(2) was constitutionally valid", "சரத்து 324(2)-ன் கீழ் தேர்தல் ஆணையர் பதவிகளை குடியரசுத் தலைவர் ரத்து செய்தது அரசியலமைப்பு ரீதியாக செல்லுபடியாகும்"), ("The Chief Election Commissioner had been removed illegally", "தலைமை தேர்தல் ஆணையர் சட்டவிரோதமாக நீக்கப்பட்டார்"), ("EVMs could not be used", "EVM பயன்படுத்த முடியாது")],
            "key": "B",
            "exp_en": "In S.S. Dhanoa (1991), the Supreme Court upheld the Presidential notification abolishing the posts of the two Election Commissioners appointed in 1989, ruling that creating or abolishing multi-member posts is within the President's discretionary power under Article 324(2).",
            "exp_ta": "எஸ்.எஸ். தனோவா வழக்கில், சரத்து 324(2)-ன் கீழ் பிற தேர்தல் ஆணையர் பதவிகளை உருவாக்குவதும் ரத்து செய்வதும் குடியரசுத் தலைவரின் விருப்பத்திற்கு உட்பட்டது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "tip": "Multi-member Commission was first created in Oct 1989, abolished in Jan 1990, and permanently restored in Oct 1993.",
            "fact": "S.S. Dhanoa and V.S. Seigell were the first two Election Commissioners appointed alongside CEC R.V.S. Peri Sastri in 1989."
        },
        # 71
        {
            "id": "ER_GT_071", "diff": "Hard", "sub": "Election Commission Powers",
            "en": "In Kanhiya Lal Omar v. R.K. Trivedi (1985), what did the Supreme Court hold regarding the constitutional validity of the Election Symbols (Reservation and Allotment) Order, 1968?",
            "ta": "கன்ஹைய லால் ஓமர் எதிர் ஆர்.கே. திரிவேதி (1985) வழக்கில், 1968 தேர்தல் சின்னங்கள் உத்தரவின் அரசியலமைப்பு செல்லுபடியாகும் தன்மை குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "opts": [("The Symbols Order was unconstitutional for lack of Parliamentary statute", "நாடாளுமன்ற சட்டம் இல்லாததால் சின்னங்கள் உத்தரவு செல்லாது"), ("The Symbols Order is fully valid as Article 324 confers plenary power to issue subordinate orders on all election matters", "சரத்து 324-ன் கீழ் தேர்தல் ஆணையத்திற்கு உள்ள முழுமையான அதிகாரம் சின்னங்கள் ஒதுக்கீடு தொடர்பான உத்தரவுகளைப் பிறப்பிக்க போதுமானது"), ("Only State Governments can allot election symbols", "மாநில அரசுகள் மட்டுமே தேர்தல் சின்னங்களை ஒதுக்க முடியும்"), ("Symbols must be abolished and replaced with party photos", "சின்னங்கள் ரத்து செய்யப்பட்டு கட்சி புகைப்படங்கள் வைக்கப்பட வேண்டும்")],
            "key": "B",
            "exp_en": "In Kanhiya Lal Omar (1985), the Supreme Court ruled that Article 324 is plenary and wide enough to empower the Election Commission to issue statutory orders like the Election Symbols Order 1968 even in the absence of a specific parliamentary statute.",
            "exp_ta": "1985-ல் கன்ஹைய லால் ஓமர் வழக்கில், தேர்தல் சின்னங்கள் உத்தரவை பிறப்பிக்க சரத்து 324 தேர்தல் ஆணையத்திற்கு முழுமையான அதிகாரத்தை வழங்குகிறது என உச்ச நீதிமன்றம் உறுதி செய்தது.",
            "tip": "Reinforced the doctrine that Article 324 is self-executing.",
            "fact": "The Court observed that pictorial symbols are indispensable in a country with high illiteracy."
        },
        # 72
        {
            "id": "ER_GT_072", "diff": "Medium", "sub": "Election Petitions",
            "en": "Under Article 71(1) of the Constitution of India, all doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be inquired into and decided by whom?",
            "ta": "இந்திய அரசியலமைப்பின் சரத்து 71(1)-ன் கீழ், குடியரசுத் தலைவர் அல்லது துணை குடியரசுத் தலைவர் தேர்தல் தொடர்பான அனைத்து சந்தேகங்கள் மற்றும் சர்ச்சைகளை விசாரித்து முடிவெடுக்கும் அதிகாரம் யாருக்கு உள்ளது?",
            "opts": [("Election Commission of India exclusively", "இந்திய தேர்தல் ஆணையத்திற்கு மட்டுமே"), ("Supreme Court of India whose decision shall be final", "இந்திய உச்ச நீதிமன்றத்திற்கு மட்டுமே (அதன் முடிவே இறுதியானது)"), ("A Special Parliamentary Joint Committee", "நாடாளுமன்ற சிறப்புக் கூட்டுக்குழு"), ("High Court of Delhi", "தில்லி உயர்நீதிமன்றம்")],
            "key": "B",
            "exp_en": "Article 71(1) states: 'All doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be inquired into and decided by the Supreme Court whose decision shall be final.'",
            "exp_ta": "சரத்து 71(1)-ன் படி, குடியரசுத் தலைவர் மற்றும் துணை குடியரசுத் தலைவர் தேர்தல் தொடர்பான அனைத்து வழக்குகளையும் உச்ச நீதிமன்றம் மட்டுமே விசாரித்து இறுதி முடிவெடுக்க முடியும்.",
            "tip": "High Courts have jurisdiction over MP/MLA elections (Article 329); Supreme Court has exclusive jurisdiction over President/VP elections (Article 71).",
            "fact": "Under the Presidential and Vice-Presidential Elections Act 1952, an election petition can only be filed by a candidate or 20 electors."
        },
        # 73
        {
            "id": "ER_GT_073", "diff": "Hard", "sub": "Presidential Elections",
            "en": "Under Section 5B of the Presidential and Vice-Presidential Elections Act 1952, how many proposers and seconders are required on the nomination paper of a presidential candidate?",
            "ta": "1952 குடியரசுத் தலைவர் மற்றும் துணை குடியரசுத் தலைவர் தேர்தல் சட்டத்தின் பிரிவு 5B-ன் கீழ், குடியரசுத் தலைவர் வேட்பாளரின் வேட்புமனுவில் எத்தனை முன்மொழிபவர்களும் வழிமொழிபவர்களும் கையெழுத்திட வேண்டும்?",
            "opts": [("10 proposers and 10 seconders", "10 முன்மொழிபவர்கள் மற்றும் 10 வழிமொழிபவர்கள்"), ("50 proposers and 50 seconders", "50 முன்மொழிபவர்கள் மற்றும் 50 வழிமொழிபவர்கள்"), ("20 proposers and 20 seconders", "20 முன்மொழிபவர்கள் மற்றும் 20 வழிமொழிபவர்கள்"), ("100 proposers and 100 seconders", "100 முன்மொழிபவர்கள் மற்றும் 100 வழிமொழிபவர்கள்")],
            "key": "B",
            "exp_en": "Following the 1997 amendment to the Act, every candidate for election to the office of President must be subscribed by at least 50 electors as proposers and at least 50 electors as seconders (from the electoral college consisting of elected MPs and MLAs).",
            "exp_ta": "1997-ல் செய்யப்பட்ட திருத்தத்தின் மூலம், குடியரசுத் தலைவர் தேர்தலில் போட்டியிடும் வேட்பாளரின் மனுவை குறைந்தபட்சம் 50 வாக்காளர்கள் முன்மொழியவும், மேலும் 50 வாக்காளர்கள் வழிமொழியவும் வேண்டும்.",
            "tip": "For Vice-President, it is 20 proposers and 20 seconders.",
            "fact": "The security deposit for Presidential election was also raised from Rs 2,500 to Rs 15,000 in 1997."
        },
        # 74
        {
            "id": "ER_GT_074", "diff": "Medium", "sub": "Election Petitions",
            "en": "In N.P. Ponnuswami v. Returning Officer, Namakkal (1952), what fundamental doctrine did the 6-judge Constitution Bench lay down regarding Article 329(b)?",
            "ta": "என்.பி. பொன்னுசாமி எதிர் தேர்தல் நடத்தும் அதிகாரி, நாமக்கல் (1952) வழக்கில், சரத்து 329(b) குறித்து உச்ச நீதிமன்றம் வகுத்த அடிப்படை கோட்பாடு என்ன?",
            "opts": [("High Courts can stay elections at any stage under Article 226", "சரத்து 226-ன் கீழ் உயர்நீதிமன்றங்கள் எந்த கட்டத்திலும் தேர்தலை நிறுத்தலாம்"), ("Courts cannot intervene in intermediate stages of an election; elections can be challenged only after completion via an Election Petition", "தேர்தல் நடக்கும் இடைப்பட்ட காலத்தில் நீதிமன்றங்கள் தலையிட முடியாது; தேர்தல் முடிந்த பிறகே தேர்தல் மனு மூலம் மட்டுமே சவால் செய்ய முடியும்"), ("Returning Officer's decisions are immune from judicial review forever", "தேர்தல் அதிகாரியின் முடிவுகள் எப்போதும் நீதிமன்ற ஆய்வுக்கு அப்பாற்பட்டவை"), ("Nomination rejection cannot be appealed", "வேட்புமனு நிராகரிப்பை எதிர்த்து மேல்முறையீடு செய்ய முடியாது")],
            "key": "B",
            "exp_en": "In N.P. Ponnuswami (1952), the Supreme Court ruled that 'election' is a continuous process starting from the notification to the declaration of result. Under Article 329(b), the High Court cannot entertain writ petitions midway; disputes can be raised only via an Election Petition after the poll is concluded.",
            "exp_ta": "1952-ல் நாமக்கல் பொன்னுசாமி வழக்கில், தேர்தல் அறிவிப்பு முதல் முடிவு அறிவிக்கப்படும் வரை நீதிமன்றங்கள் தேர்தல் நடைமுறைகளில் தலையிட முடியாது என்றும், தேர்தல் முடிந்த பின் தேர்தல் மனு மூலமே முறையிட முடியும் என்றும் தீர்ப்பளிக்கப்பட்டது.",
            "tip": "Prevents endless litigation from stalling elections midway.",
            "fact": "This is one of the earliest and most frequently cited constitutional judgments on election law."
        },
        # 75
        {
            "id": "ER_GT_075", "diff": "Hard", "sub": "Election Petitions",
            "en": "In Indira Nehru Gandhi v. Raj Narain (1975), which Constitutional Amendment Act was struck down as violating the Basic Structure of the Constitution?",
            "ta": "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975) வழக்கில், அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பை மீறியதாகக் கூறி எந்த அரசியலமைப்பு திருத்தச் சட்டம் ரத்து செய்யப்பட்டது?",
            "opts": [("38th Amendment Act", "38-வது திருத்தச் சட்டம்"), ("39th Amendment Act (Clause 4 of Article 329A)", "39-வது திருத்தச் சட்டம் (சரத்து 329A-ன் உட்பிரிவு 4)"), ("42nd Amendment Act", "42-வது திருத்தச் சட்டம்"), ("44th Amendment Act", "44-வது திருத்தச் சட்டம்")],
            "key": "B",
            "exp_en": "In Indira Nehru Gandhi v. Raj Narain (1975), the Supreme Court struck down Clause 4 of Article 329A (inserted by 39th Amendment) which sought to place the election of the Prime Minister and Speaker outside the purview of judicial review, declaring 'free and fair elections' and 'judicial review' part of Basic Structure.",
            "exp_ta": "1975-ல் இந்திரா காந்தி வழக்கில், பிரதமர் மற்றும் சபாநாயகர் தேர்தலை நீதிமன்ற ஆய்வுக்கு அப்பாற்பட்டதாக மாற்றிய 39-வது திருத்தத்தின் சரத்து 329A(4)-ஐ, மக்களாட்சி மற்றும் நீதிமன்ற மறுஆய்வை மீறியதாகக் கூறி உச்ச நீதிமன்றம் ரத்து செய்தது.",
            "tip": "First time the Basic Structure doctrine (from Kesavananda Bharati) was applied to strike down a constitutional amendment.",
            "fact": "Justice H.R. Khanna, Justice K.K. Mathew, and Justice Y.V. Chandrachud delivered key concurring opinions."
        },
        # 76
        {
            "id": "ER_GT_076", "diff": "Medium", "sub": "Party Spending",
            "en": "In Kanwar Lal Gupta v. Amar Nath Chawla (1975), what did the Supreme Court rule regarding expenditure incurred by a political party on behalf of its candidate?",
            "ta": "கன்வர் லால் குப்தா எதிர் அமர் நாத் சாவ்லா (1975) வழக்கில், வேட்பாளருக்காக அரசியல் கட்சி செய்யும் தேர்தல் செலவு குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "opts": [("Political party spending has no relation to candidate spending", "கட்சி செய்யும் செலவுக்கும் வேட்பாளர் செலவுக்கும் எந்த தொடர்பும் இல்லை"), ("Party spending incurred with the knowledge and consent of the candidate must be included in the candidate's ceiling limit", "வேட்பாளரின் சம்மதத்துடனும் அறிவுடனும் கட்சி செய்யும் செலவுகள் வேட்பாளரின் தனிநபர் தேர்தல் செலவு வரம்பில் சேர்க்கப்பட வேண்டும்"), ("Parties cannot spend any money in elections", "கட்சிகள் தேர்தல்களில் எந்தப் பணத்தையும் செலவிட முடியாது"), ("Parties can spend up to Rs 100 Crore per candidate", "கட்சிகள் ஒரு வேட்பாளருக்கு ரூ.100 கோடி வரை செலவிடலாம்")],
            "key": "B",
            "exp_en": "In Kanwar Lal Gupta (1975), the Court held that expenditure incurred or authorized by a political party or friends for the candidate's election must be tagged to the candidate's statutory ceiling, otherwise ceiling limits would become a mockery.",
            "exp_ta": "1975-ல் கன்வர் லால் குப்தா வழக்கில், வேட்பாளரின் ஒப்புதலுடன் அரசியல் கட்சி செய்யும் செலவுகள் வேட்பாளரின் தேர்தல் செலவு உச்சவரம்பில் சேர்க்கப்பட வேண்டும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "tip": "Parliament overturned this in 1974/75 by inserting Explanation 1 to Section 77(1) excluding party spending.",
            "fact": "However, Supreme Court in Common Cause (1996) reintroduced scrutiny of party spending."
        },
        # 77
        {
            "id": "ER_GT_077", "diff": "Hard", "sub": "Star Campaigners",
            "en": "Under Section 77(1) of the Representation of the People Act 1951, what is the maximum number of 'Star Campaigners' permitted for a recognized political party versus an unrecognized registered party?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 77(1)-ன் கீழ், அங்கீகரிக்கப்பட்ட கட்சிக்கும் அங்கீகரிக்கப்படாத பதிவு செய்யப்பட்ட கட்சிக்கும் அனுமதிக்கப்பட்ட அதிகபட்ச 'நட்சத்திர பேச்சாளர்களின்' (Star Campaigners) எண்ணிக்கை என்ன?",
            "opts": [("20 for recognized; 10 for unrecognized", "அங்கீகரிக்கப்பட்ட கட்சிக்கு 20; அங்கீகரிக்கப்படாத கட்சிக்கு 10"), ("40 for recognized party; 20 for unrecognized registered party", "அங்கீகரிக்கப்பட்ட கட்சிக்கு 40; அங்கீகரிக்கப்படாத பதிவு செய்யப்பட்ட கட்சிக்கு 20"), ("50 for recognized; 25 for unrecognized", "அங்கீகரிக்கப்பட்ட கட்சிக்கு 50; அங்கீகரிக்கப்படாத கட்சிக்கு 25"), ("No limit for recognized parties", "அங்கீகரிக்கப்பட்ட கட்சிக்கு வரம்பு இல்லை")],
            "key": "B",
            "exp_en": "Under Explanation 2 to Section 77(1) of RPA 1951, a recognized National or State political party can nominate up to 40 Star Campaigners, while a Registered Unrecognized Political Party (RUPP) can nominate up to 20 Star Campaigners whose travel expenses are not debited to candidate accounts.",
            "exp_ta": "பிரிவு 77(1)-ன் கீழ், ஒரு அங்கீகரிக்கப்பட்ட அரசியல் கட்சி அதிகபட்சம் 40 நட்சத்திர பேச்சாளர்களையும், பதிவு செய்யப்பட்ட அங்கீகரிக்கப்படாத கட்சி 20 நட்சத்திர பேச்சாளர்களையும் நியமிக்கலாம் (இவர்களின் பயண செலவு வேட்பாளர் கணக்கில் சேராது).",
            "tip": "The list of Star Campaigners must be submitted to CEO/ECI within 7 days of election notification.",
            "fact": "If a Star Campaigner shares the dais and specifically campaigns for a candidate, the local rally cost is debited to that candidate."
        },
        # 78
        {
            "id": "ER_GT_078", "diff": "Medium", "sub": "Freebies & Manifestos",
            "en": "In S. Subramaniam Balaji v. State of Tamil Nadu (2013), what did the Supreme Court direct the Election Commission regarding promises of freebies in election manifestos?",
            "ta": "எஸ். சுப்பிரமணியம் பாலாஜி எதிர் தமிழ்நாடு அரசு (2013) வழக்கில், தேர்தல் அறிக்கைகளில் இலவசங்கள் அறிவிப்பது குறித்து தேர்தல் ஆணையத்திற்கு உச்ச நீதிமன்றம் என்ன உத்தரவிட்டது?",
            "opts": [("To ban all political parties promising welfare schemes", "நலத்திட்டங்களை அறிவிக்கும் அனைத்து கட்சிகளையும் தடை செய்ய"), ("To frame comprehensive guidelines governing election manifestos in consultation with political parties under the Model Code of Conduct", "அரசியல் கட்சிகளுடன் கலந்தாலோசித்து தேர்தல் நடத்தை விதிகளின் கீழ் தேர்தல் அறிக்கைகளை ஒழுங்குபடுத்த விரிவான வழிகாட்டுதல்களை உருவாக்க"), ("To abolish election manifestos permanently", "தேர்தல் அறிக்கைகளை நிரந்தரமாக ரத்து செய்ய"), ("To print official government manifestos", "அரசாங்கமே தேர்தல் அறிக்கையை அச்சிட")],
            "key": "B",
            "exp_en": "In S. Subramaniam Balaji (July 2013), the Supreme Court held that while manifesto promises cannot be termed 'corrupt practice' under Section 123, freebies shake the root of free and fair elections, directing the ECI to frame guidelines on manifestos in the Model Code of Conduct.",
            "exp_ta": "2013-ல் சுப்பிரமணியம் பாலாஜி வழக்கில், இலவச அறிவிப்புகள் தேர்தல் ஊழல் ஆகாது என்றாலும் அவை சமநிலையை பாதிக்கின்றன எனக் கூறி, தேர்தல் அறிக்கைகளை முறைப்படுத்த நடத்தை விதிகளில் வழிகாட்டுதல்களை சேர்க்க தேர்தல் ஆணையத்திற்கு உத்தரவிடப்பட்டது.",
            "tip": "Following this, Part VIII was added to the Model Code of Conduct covering guidelines on manifestos.",
            "fact": "Manifesto guidelines require parties to explain the rationale and financial viability of promised welfare schemes."
        },
        # 79
        {
            "id": "ER_GT_079", "diff": "Hard", "sub": "Electoral Rolls",
            "en": "In Lal Babu Hussein v. Electoral Registration Officer (1995), what did the Supreme Court rule regarding the deletion of voters on suspicions of being non-citizens (foreign nationals)?",
            "ta": "லால் பாபு ஹுசைன் எதிர் வாக்காளர் பதிவு அதிகாரி (1995) வழக்கில், வெளிநாட்டவர் என்ற சந்தேகத்தின் பேரில் வாக்காளர்களை நீக்குவது குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "opts": [("ERO can delete voters summarily without any notice", "எந்த முன்னறிவிப்பும் இன்றி ERO வாக்காளர்களை உடனடியாக நீக்கலாம்"), ("An elector whose name is already on the roll cannot be deleted without reasonable opportunity of hearing and following principles of natural justice", "ஏற்கனவே வாக்காளர் பட்டியலில் உள்ள ஒருவரை உரிய விசாரணை மற்றும் இயற்கை நீதிக் கோட்பாடுகளைப் பின்பற்றாமல் தன்னிச்சையாக நீக்க முடியாது"), ("Police certificate is final proof of citizenship", "காவல்துறை சான்றிதழே குடியுரிமைக்கான இறுதி ஆதாரம்"), ("Citizenship can be determined by local political agents", "உள்ளூர் அரசியல் முகவர்கள் குடியுரிமையை தீர்மானிக்கலாம்")],
            "key": "B",
            "exp_en": "In Lal Babu Hussein (1995), the Supreme Court held that once a person's name is enrolled, there is a presumption of citizenship; the Electoral Registration Officer cannot disenfranchise or delete names on suspicion of being illegal immigrants without issuing individual notice and conducting a fair inquiry.",
            "exp_ta": "1995-ல் லால் பாபு ஹுசைன் வழக்கில், வாக்காளர் பட்டியலில் ஏற்கனவே பெயர் உள்ள ஒருவரை இயற்கை நீதியின்படி தனிப்பட்ட விளக்கம் கேட்கும் வாய்ப்பு அளிக்காமல் வெளிநாட்டவர் எனக்கூறி நீக்க முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "tip": "Protecting genuine citizens from arbitrary mass deletion from voter rolls.",
            "fact": "The burden of proof lies on the person objecting to the inclusion under Rule 20 of Registration of Electors Rules."
        },
        # 80
        {
            "id": "ER_GT_080", "diff": "Medium", "sub": "Voter Turnout",
            "en": "What is the specialized division of the Election Commission of India established in 2009 to design flagship voter education, awareness, and electoral participation campaigns?",
            "ta": "வாக்காளர் கல்வி, விழிப்புணர்வு மற்றும் தேர்தலில் மக்கள் பங்களிப்பை அதிகரிப்பதற்காக 2009-ல் உருவாக்கப்பட்ட இந்திய தேர்தல் ஆணையத்தின் பிரத்யேக பிரிவு எது?",
            "opts": [("CPGRAMS", "CPGRAMS"), ("SVEEP (Systematic Voters' Education and Electoral Participation)", "ஸ்வீப் (SVEEP - முறையான வாக்காளர் கல்வி மற்றும் தேர்தல் பங்களிப்பு திட்டம்)"), ("NITI Aayog Cell", "நிதி ஆயோக் பிரிவு"), ("Electoral Vigilance Bureau", "தேர்தல் கண்காணிப்பு பணியகம்")],
            "key": "B",
            "exp_en": "SVEEP (Systematic Voters' Education and Electoral Participation) is the flagship program of the ECI launched in 2009 to educate citizens, increase voter turnout, and bridge gender and urban-youth gaps in voting.",
            "exp_ta": "2009-ல் தொடங்கப்பட்ட 'ஸ்வீப்' (SVEEP) என்பது வாக்காளர்களிடையே விழிப்புணர்வை ஏற்படுத்தவும், பெண்களின் வாக்குப்பதிவை அதிகரிக்கவும் தேர்தல் ஆணையத்தால் செயல்படுத்தப்படும் முதன்மை திட்டமாகும்.",
            "tip": "SVEEP organizes voter awareness clubs in schools and colleges and appoints National Icons.",
            "fact": "SVEEP activities have contributed to India recording historic voter turnouts in recent elections."
        },
        # 81
        {
            "id": "ER_GT_081", "diff": "Hard", "sub": "Voting Rights & Disqualification",
            "en": "In Chief Election Commissioner v. Saka Venkata Rao (1953), what constitutional principle did the Supreme Court establish regarding disqualification referrals under Article 192?",
            "ta": "தலைமை தேர்தல் ஆணையர் எதிர் சாகா வெங்கட ராவ் (1953) வழக்கில், சரத்து 192-ன் கீழ் தகுதிநீக்க பரிந்துரைகள் குறித்து உச்ச நீதிமன்றம் நிறுவிய அரசியலமைப்பு கொள்கை என்ன?",
            "opts": [("Article 192 applies only to disqualifications incurred after being elected, not pre-existing disqualifications", "சரத்து 192 என்பது தேர்ந்தெடுக்கப்பட்ட பிறகு ஏற்படும் தகுதிநீக்கங்களுக்கு மட்டுமே பொருந்தும்; தேர்தலுக்கு முந்தைய தகுதியின்மைகளுக்கு பொருந்தாது"), ("High Court has no power over election officials", "தேர்தல் அதிகாரிகள் மீது உயர்நீதிமன்றத்திற்கு அதிகாரம் இல்லை"), ("Governor can disqualify any MLA without consulting ECI", "தேர்தல் ஆணையத்தை கலந்தாலோசிக்காமல் ஆளுநர் எந்த எம்.எல்.ஏ-வையும் தகுதிநீக்கம் செய்யலாம்"), ("Election Commission can dissolve the State Assembly", "தேர்தல் ஆணையம் மாநில சட்டமன்றத்தை கலைக்கலாம்")],
            "key": "A",
            "exp_en": "In Saka Venkata Rao (1953), the Supreme Court ruled that Article 192 (and Article 103 for MPs) applies only to supervening disqualifications incurred by a member after election. Disqualifications existing prior to the election can only be challenged via an Election Petition under Article 329.",
            "exp_ta": "1953-ல் சாகா வெங்கட ராவ் வழக்கில், சரத்து 192 என்பது தேர்தலில் வெற்றிபெற்ற பின்னர் ஏற்படும் தகுதிநீக்கங்களுக்கு மட்டுமே பொருந்தும் என்றும், தேர்தலுக்கு முந்தைய தகுதியின்மையை தேர்தல் மனு மூலம் மட்டுமே சவால் செய்ய முடியும் என்றும் தீர்ப்பளிக்கப்பட்டது.",
            "tip": "Supervening disqualification = Article 103/192; Pre-existing disqualification = Election Petition.",
            "fact": "Delivered by Chief Justice Patanjali Sastri."
        },
        # 82
        {
            "id": "ER_GT_082", "diff": "Medium", "sub": "Disqualification",
            "en": "Under Section 8A of the Representation of the People Act 1951, what is the maximum period for which a person found guilty of a 'corrupt practice' by an order in an election petition may be disqualified?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 8A-ன் கீழ், தேர்தல் மனுவில் 'ஊழல் நடவடிக்கை' நிரூபிக்கப்பட்ட ஒருவருக்கு விதிக்கப்படக்கூடிய அதிகபட்ச தகுதிநீக்கக் காலம் என்ன?",
            "opts": [("3 years", "3 ஆண்டுகள்"), ("6 years", "6 ஆண்டுகள்"), ("10 years", "10 ஆண்டுகள்"), ("Permanent disqualification", "நிரந்தர தகுதிநீக்கம்")],
            "key": "B",
            "exp_en": "Under Section 8A of RPA 1951, the President determines the period of disqualification upon obtaining the opinion of the Election Commission, which shall not exceed 6 years from the date the order takes effect.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 8A-ன் கீழ், தேர்தல் ஊழல் நடவடிக்கையில் குற்றவாளி என நிரூபிக்கப்பட்ட ஒருவருக்கு தேர்தல் ஆணையத்தின் ஆலோசனையின் பேரில் அதிகபட்சமாக 6 ஆண்டுகள் தகுதிநீக்கம் விதிக்கப்படலாம்.",
            "tip": "Case is referred to the President who decides based on ECI's binding recommendation.",
            "fact": "Section 8A was amended in 1975 following the Raj Narain case."
        },
        # 83
        {
            "id": "ER_GT_083", "diff": "Hard", "sub": "Election Laws Amendment 2021",
            "en": "Which amendment made by the Election Laws (Amendment) Act 2021 made the language in statutory election provisions gender-neutral for service voters?",
            "ta": "2021 தேர்தல் சட்டங்கள் (திருத்த) சட்டத்தின் மூலம் இராணுவ/பணி வாக்காளர்களுக்கான சட்டப் பிரிவுகளில் பாலின சமத்துவத்தை கொண்டுவர செய்யப்பட்ட மாற்றம் எது?",
            "opts": [("Replacing the word 'wife' with 'spouse'", "'மனைவி' (Wife) என்ற வார்த்தைக்கு பதிலாக 'வாழ்க்கைத் துணை' (Spouse) என மாற்றப்பட்டது"), ("Abolishing service voting for women", "பெண்களுக்கான பணி வாக்குகளை ரத்து செய்தது"), ("Requiring women to register only via postal ballot", "பெண்கள் தபால் வாக்கு மூலம் மட்டுமே பதிவு செய்ய வேண்டும் என கட்டாயப்படுத்தியது"), ("Providing separate polling booths for spouses", "வாழ்க்கைத் துணைக்கு தனி வாக்குச்சாவடி அமைத்தது")],
            "key": "A",
            "exp_en": "The Election Laws (Amendment) Act 2021 replaced the word 'wife' with 'spouse' in Section 20 of RPA 1950 and Section 60 of RPA 1951, allowing the husband of a female service personnel to also register as a service voter (which was previously denied).",
            "exp_ta": "2021 தேர்தல் சட்டத் திருத்தம், 1950 மற்றும் 1951 சட்டங்களில் இருந்த 'மனைவி' (Wife) என்ற வார்த்தைக்கு பதிலாக 'வாழ்க்கைத் துணை' (Spouse) என மாற்றி, பெண் பாதுகாப்புப் படை வீரர்களின் கணவர்களுக்கும் பணி வாக்காளர் உரிமையை வழங்கியது.",
            "tip": "Major gender-neutral electoral reform ensuring equal rights for women in defence forces.",
            "fact": "Earlier, only the wife of a male service voter could be enrolled as a service voter."
        },
        # 84
        {
            "id": "ER_GT_084", "diff": "Medium", "sub": "Disqualification",
            "en": "Under Section 11 of the Representation of the People Act 1951, who possesses the statutory power to remove or reduce the period of any disqualification incurred under Chapter III (except Sec 8A)?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 11-ன் கீழ், ஒருவருக்கு விதிக்கப்பட்ட தகுதிநீக்கத்தை நீக்கவோ அல்லது அதன் காலத்தைக் குறைக்கவோ யாருக்கு சட்டப்பூர்வ அதிகாரம் உள்ளது?",
            "opts": [("President of India directly", "இந்திய குடியரசுத் தலைவருக்கு நேரடியாக"), ("Election Commission of India", "இந்திய தேர்தல் ஆணையம்"), ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"), ("Union Law Minister", "மத்திய சட்ட அமைச்சர்")],
            "key": "B",
            "exp_en": "Section 11 of RPA 1951 explicitly empowers the Election Commission of India to remove or reduce the period of any disqualification incurred under Chapter III of Part II (disqualifications under Sections 8, 9, 9A, 10, and 10A) for reasons to be recorded in writing.",
            "exp_ta": "1951 சட்டத்தின் பிரிவு 11, எழுத்துப்பூர்வ காரணங்களை பதிவு செய்து, சட்டப்பிரிவு 8, 9, 10A போன்றவற்றின் கீழ் விதிக்கப்பட்ட தகுதிநீக்க காலத்தை நீக்கவோ குறைக்கவோ இந்திய தேர்தல் ஆணையத்திற்கு அதிகாரம் அளிக்கிறது.",
            "tip": "ECI exercised this power in 2019 to reduce Sikkim CM Prem Singh Tamang's disqualification period.",
            "fact": "This power cannot be exercised arbitrarily and is subject to judicial review."
        },
        # 85
        {
            "id": "ER_GT_085", "diff": "Hard", "sub": "Disqualification",
            "en": "In Lok Prahari v. Election Commission of India (2018), what did the Supreme Court hold regarding the disqualification of a legislator whose conviction is stayed by an appellate court?",
            "ta": "லோக் பிரஹாரி எதிர் இந்திய தேர்தல் ஆணையம் (2018) வழக்கில், மேல்முறையீட்டு நீதிமன்றத்தால் தண்டனை நிறுத்தி வைக்கப்பட்ட (Stay) ஒரு மக்கள் பிரதிநிதியின் தகுதிநீக்கம் குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "opts": [("Disqualification continues regardless of stay", "தண்டனை நிறுத்தி வைக்கப்பட்டாலும் தகுதிநீக்கம் தொடரும்"), ("Once conviction is stayed under Section 389 CrPC, the disqualification under Section 8 of RPA 1951 ceases to operate", "பிரிவு 389 CrPC-ன் கீழ் குற்றத்தீர்ப்பு நிறுத்தி வைக்கப்பட்டால், பிரிவு 8-ன் கீழான தகுதிநீக்கமும் உடனடியாக செயலற்றதாகிவிடும்"), ("The member must contest a fresh bye-election", "அவர் மீண்டும் புதிய இடைத்தேர்தலில் போட்டியிட வேண்டும்"), ("President's permission is required to resume membership", "உறுப்பினர் பதவியை தொடர குடியரசுத் தலைவர் அனுமதி வேண்டும்")],
            "key": "B",
            "exp_en": "In Lok Prahari (September 2018), a 3-judge bench headed by CJI Dipak Misra clarified that when an appellate court stays the conviction of a sitting MP/MLA under Section 389 of CrPC, the disqualification under Section 8 of RPA 1951 also becomes inoperative during the pendency of the stay.",
            "exp_ta": "2018-ல் லோக் பிரஹாரி வழக்கில், ஒரு எம்.பி/எம்.எல்.ஏ-வின் குற்றத்தீர்ப்பை (Conviction) மேல்முறையீட்டு நீதிமன்றம் இடைக்காலமாக நிறுத்தி வைத்தால் (Stay), பிரிவு 8-ன் கீழான தகுதிநீக்கமும் செயலற்று போகும் என உச்ச நீதிமன்றம் தெளிவுபடுத்தியது.",
            "tip": "Mere suspension of sentence is not enough; the conviction itself must be stayed.",
            "fact": "This principle was subsequently applied in restoring the parliamentary membership of various MPs."
        },
        # 86
        {
            "id": "ER_GT_086", "diff": "Medium", "sub": "Electoral Technology",
            "en": "Which dedicated web portal and mobile app was upgraded by the ECI in 2024 to provide candidates with single-window digital clearances for election campaign rallies, vehicles, and permissions?",
            "ta": "வேட்பாளர்கள் பேரணிகள், வாகனங்கள் மற்றும் கூட்டங்களுக்கான அனுமதிகளை ஒற்றைச் சாளர முறையில் டிஜிட்டல் வடிவில் பெற 2024-ல் தேர்தல் ஆணையத்தால் மேம்படுத்தப்பட்ட தளம் எது?",
            "opts": [("cVIGIL 2.0", "சிவிஜில் 2.0"), ("Suvidha 2.0 Portal", "சுவிதா (Suvidha) 2.0 தளம்"), ("Garuda Portal", "கருடா தளம்"), ("Saksham Portal", "சாக்ஷம் தளம்")],
            "key": "B",
            "exp_en": "Suvidha 2.0 portal and mobile application was launched by the ECI to ensure transparent, first-come-first-served clearances for candidates seeking permission for public meetings, processions, helicopters, and campaign vehicles within time-bound SLAs.",
            "exp_ta": "வேட்பாளர்கள் தங்களின் தேர்தல் பிரச்சார கூட்டங்கள், வாகனங்கள் மற்றும் பேரணிகளுக்கான அனுமதியை முதலில் வருபவருக்கு முன்னுரிமை அடிப்படையில் பெற சுவிதா 2.0 (Suvidha 2.0) தளம் மேம்படுத்தப்பட்டது.",
            "tip": "Suvidha eliminates bureaucratic favoritism by time-stamping permission requests digitally.",
            "fact": "Permissions are processed within 24 to 48 hours under designated nodal officers."
        },
        # 87
        {
            "id": "ER_GT_087", "diff": "Hard", "sub": "Electoral Administration",
            "en": "Under Section 28A of the Representation of the People Act 1951, all returning officers, presiding officers, and police officers designated for election duties are deemed to be on what status?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 28A-ன் கீழ், தேர்தல் பணியில் ஈடுபடுத்தப்படும் தேர்தல் நடத்தும் அலுவலர்கள் மற்றும் காவல்துறை அதிகாரிகள் எந்த அந்தஸ்தில் இருப்பதாக கருதப்படுகிறார்கள்?",
            "opts": [("Regular state government employees under Home Ministry", "உள்துறை அமைச்சகத்தின் கீழ் வழக்கமான மாநில அரசு ஊழியர்கள்"), ("Deemed to be on deputation to the Election Commission of India and subject to its disciplinary control", "இந்திய தேர்தல் ஆணையத்திற்கு அயல்பணியில் (Deputation) இருப்பதாக கருதப்பட்டு, அதன் ஒழுங்கு நடவடிக்கைக் கட்டுப்பாட்டிற்கு உட்பட்டவர்கள்"), ("Temporary employees without service protection", "பணி பாதுகாப்பு இல்லாத தற்காலிக ஊழியர்கள்"), ("Independent statutory commissioners", "சுயாதீன சட்டப்பூர்வ ஆணையர்கள்")],
            "key": "B",
            "exp_en": "Section 28A of RPA 1951 (inserted in 1989) provides that all officers and police personnel deployed for election work are deemed to be on deputation to the ECI, and are subject to the control, superintendence, and disciplinary power of the Commission during the election period.",
            "exp_ta": "1989-ல் சேர்க்கப்பட்ட பிரிவு 28A-ன் படி, தேர்தல் பணியிலுள்ள அனைத்து அலுவலர்களும் காவல்துறையினரும் தேர்தல் ஆணையத்திற்கு அயல்பணியில் (Deputation) இருப்பதாக கருதப்பட்டு அதன் நேரடி ஒழுங்கு நடவடிக்கைக்கு உட்படுவார்கள்.",
            "tip": "Allows the ECI to suspend or transfer biased civil/police officers without seeking state government consent.",
            "fact": "This provision was introduced following recommendations of the Tarkunde and Goswami committees."
        },
        # 88
        {
            "id": "ER_GT_088", "diff": "Medium", "sub": "Electoral Rolls",
            "en": "Under Rule 13 of the Registration of Electors Rules 1960, which statutory form is used by a registered voter seeking transposition or correction of particulars in the electoral roll?",
            "ta": "1960 வாக்காளர் பதிவு விதிகளின் விதி 13-ன் கீழ், வாக்காளர் பட்டியலில் உள்ள விவரங்களைத் திருத்த அல்லது தொகுதிக்குள் முகவரி மாற்றம் செய்ய வாக்காளர் பயன்படுத்தும் படிவம் எது?",
            "opts": [("Form 6", "படிவம் 6"), ("Form 8", "படிவம் 8"), ("Form 7", "படிவம் 7"), ("Form 6A", "படிவம் 6A")],
            "key": "B",
            "exp_en": "Form 8 is the standardized multi-purpose form used for: (1) shifting of residence within or outside constituency, (2) correction of entries in existing roll, (3) replacement of EPIC without correction, and (4) marking of PwD status.",
            "exp_ta": "படிவம் 8 என்பது வாக்காளர் பட்டியலில் முகவரி மாற்றம், பெயர்/விவரங்கள் திருத்தம், புதிய அடையாள அட்டை கோருதல் மற்றும் மாற்றுத்திறனாளி என குறித்தல் ஆகியவற்றுக்கான படிவமாகும்.",
            "tip": "Form 8A was abolished in 2022 and merged entirely into Form 8.",
            "fact": "Form 8 can be filled completely online through the National Voters' Service Portal or Voter Helpline App."
        },
        # 89
        {
            "id": "ER_GT_089", "diff": "Hard", "sub": "Electoral Integrity",
            "en": "In People's Union for Civil Liberties (PUCL) v. Union of India (2003), what did the 3-judge Supreme Court bench hold regarding Parliament's attempt to dilute candidate disclosures via the 2002 RPA Amendment?",
            "ta": "பியுசிஎல் எதிர் இந்திய ஒன்றியம் (2003) வழக்கில், 2002 சட்டத் திருத்தத்தின் மூலம் வேட்பாளர் பிரகடனங்களை குறைக்க நாடாளுமன்றம் செய்த முயற்சியை உச்ச நீதிமன்றம் எவ்வாறு தீர்ப்பளித்தது?",
            "opts": [("Parliament's amendment was completely constitutional", "நாடாளுமன்ற திருத்தம் முற்றிலும் அரசியலமைப்புக்கு உட்பட்டது"), ("Section 33B of RPA 1951 which barred candidates from disclosing any information beyond the statute was declared unconstitutional and void", "சட்டத்திற்கு அப்பாற்பட்ட தகவல்களை வேட்பாளர்கள் வெளியிட தேவையில்லை என்ற பிரிவு 33B அரசியலமைப்பிற்கு எதிரானது என ரத்து செய்யப்பட்டது"), ("Candidate disclosures were made optional", "வேட்பாளர் விவரங்கள் அறிவிப்பது விருப்பத்தேர்வாக்கப்பட்டது"), ("Right to information does not apply to voters", "வாக்காளர்களுக்கு தகவல் அறியும் உரிமை பொருந்தாது")],
            "key": "B",
            "exp_en": "In PUCL (March 2003), the Supreme Court struck down Section 33B of RPA 1951 (enacted by Parliament to bypass the 2002 ADR ruling) as unconstitutional, holding that Parliament cannot abridge the voter's fundamental right to know candidates' backgrounds under Article 19(1)(a).",
            "exp_ta": "2003-ல் பியுசிஎல் வழக்கில், ஏடிஆர் தீர்ப்பை முடக்க நாடாளுமன்றம் கொண்டுவந்த பிரிவு 33B-ஐ உச்ச நீதிமன்றம் ரத்து செய்து, வாக்காளரின் அறியும் உரிமையை (சரத்து 19(1)(a)) நாடாளுமன்றத்தால் பறிக்க முடியாது என தீர்ப்பளித்தது.",
            "tip": "Established that the voter's right to information is a basic human and constitutional right.",
            "fact": "Justice P. Venkatarama Reddi and Justice M.B. Shah delivered key judgments."
        },
        # 90
        {
            "id": "ER_GT_090", "diff": "Medium", "sub": "Contemporary Challenges",
            "en": "In the context of modern elections, what is the 'Silent Window' challenge posed by Social Media platforms like WhatsApp, X, and Facebook during the 48-hour period before voting closes?",
            "ta": "நவீன தேர்தல்களில் வாக்குப்பதிவு முடிவதற்கு முந்தைய 48 மணி நேர அமைதிக்காலத்தில் வாட்ஸ்அப், ஃபேஸ்புக் போன்ற சமூக ஊடகங்கள் ஏற்படுத்தும் முக்கிய சவால் என்ன?",
            "opts": [("Complete lack of mobile internet networks", "மொபைல் இணைய நெட்வொர்க் முற்றிலும் இல்லாதது"), ("Viral spread of uncertified digital campaign videos, misinformation, and deepfakes across encrypted messaging platforms bypassing traditional Section 126 enforcement", "பிரிவு 126-ன் கீழ் வழமையான தடையை மீறி மறைகுறியாக்கப்பட்ட குறுஞ்செயலி மற்றும் சமூக ஊடகங்களில் போலி செய்திகள், டீப்ஃபேக் வீடியோக்கள் மற்றும் அரசியல் பிரச்சாரங்கள் வைரலாவது"), ("High data roaming charges", "அதிக டேட்டா ரோமிங் கட்டணங்கள்"), ("Overcrowding at telecom stores", "தொலைத்தொடர்பு கடைகளில் கூட்டம் கூடுவது")],
            "key": "B",
            "exp_en": "While Section 126 prohibits conventional broadcasting and public meetings during the 48-hour silent window, digital propaganda, targeted WhatsApp group messaging, and AI-generated deepfakes present major enforcement challenges, prompting ECI's Voluntary Code of Ethics with tech platforms.",
            "exp_ta": "பாரம்பரிய ஊடகங்கள் அமைதிக்காலத்தில் பிரச்சாரம் செய்ய தடை உள்ள நிலையில், சமூக ஊடகங்கள் மற்றும் வாட்ஸ்அப் குழுக்கள் மூலம் போலி செய்திகள், டீப்ஃபேக் வீடியோக்கள் பரவுவது தேர்தல் நேர்மைக்கு பெரும் சவாலாக உள்ளது.",
            "tip": "Internet and Mobile Association of India (IAMAI) agreed to a Voluntary Code of Ethics with ECI in 2019.",
            "fact": "A dedicated Social Media Cell operates 24/7 during elections to request takedowns under Section 79 of IT Act."
        },
        # 91
        {
            "id": "ER_GT_091", "diff": "Hard", "sub": "Contemporary Challenges",
            "en": "Under the ECI's 'Voluntary Code of Ethics' developed with major social media platforms during the 2019 Lok Sabha elections, within how many hours must platforms act on reported violations during the 48-hour silent period?",
            "ta": "2019 தேர்தலின் போது சமூக ஊடக தளங்களுடன் தேர்தல் ஆணையம் உருவாக்கிய 'தன்னார்வ நெறிமுறைக் குறியீட்டின்' கீழ், 48 மணி நேர அமைதிக்காலத்தில் புகாரளிக்கப்பட்ட விதிமீறல்கள் மீது எத்தனை மணி நேரத்திற்குள் தளங்கள் நடவடிக்கை எடுக்க வேண்டும்?",
            "opts": [("Within 1 hour", "1 மணி நேரத்திற்குள்"), ("Within 3 hours", "3 மணி நேரத்திற்குள்"), ("Within 24 hours", "24 மணி நேரத்திற்குள்"), ("Within 48 hours", "48 மணி நேரத்திற்குள்")],
            "key": "B",
            "exp_en": "Under the Voluntary Code of Ethics submitted by IAMAI to the ECI, social media platforms committed to acting on valid ECI notifications regarding violations during the 48-hour silent window (under Section 126) within a fast-tracked turnaround time of 3 hours.",
            "exp_ta": "தேர்தல் ஆணையத்தின் தன்னார்வ நெறிமுறைக் குறியீட்டின் கீழ், 48 மணி நேர அமைதிக்கால விதிமீறல்கள் குறித்து தேர்தல் ஆணையம் தெரிவித்தால் 3 மணி நேரத்திற்குள் சமூக ஊடக தளங்கள் அந்த பதிவை நீக்க வேண்டும்.",
            "tip": "Dedicated Grievance Officers and escalation channels operate between ECI and platforms.",
            "fact": "Covers Meta, Google, X (Twitter), ShareChat, and WhatsApp."
        },
        # 92
        {
            "id": "ER_GT_092", "diff": "Medium", "sub": "Electoral Systems",
            "en": "Which alternative electoral system involves voters ranking candidates in order of preference (1, 2, 3), where the lowest candidate is eliminated and preferences redistributed until a candidate crosses 50% quota?",
            "ta": "வாக்காளர்கள் வேட்பாளர்களை விருப்ப வரிசைப்படி (1, 2, 3) வரிசைப்படுத்தி, குறைந்த வாக்கு பெற்றவர் நீக்கப்பட்டு 50% வாக்குகளைப் பெறும் வரை வாக்குகள் மாற்றப்படும் தேர்தல் முறை எது?",
            "opts": [("First-Past-The-Post (FPTP)", "அதிக வாக்குகள் பெறும் நேரடி முறை"), ("Alternative Vote / Ranked-Choice Voting (Instant Runoff)", "மாற்று வாக்கு முறை / விருப்ப வரிசை வாக்கு முறை (Instant Runoff)"), ("Party List Proportional Representation", "கட்சி பட்டியல் விகிதாச்சார பிரதிநிதித்துவம்"), ("Mixed Member Proportional (MMP)", "கலப்பு உறுப்பினர் விகிதாச்சார முறை")],
            "key": "B",
            "exp_en": "The Alternative Vote (AV) system (also known as Instant-Runoff Voting) allows voters to rank candidates. If no candidate secures an absolute majority (>50%) on first preferences, the bottom candidate is eliminated and their second preferences transferred until someone wins a majority.",
            "exp_ta": "மாற்று வாக்கு முறை (Alternative Vote) என்பது வாக்காளர்கள் விருப்ப வரிசைப்படி வாக்களித்து, 50%-க்கு மேல் பெரும்பான்மை பெறும் வரை வாக்குகள் மாற்றப்படும் தேர்தல் முறையாகும்.",
            "tip": "Used in Australian House of Representatives elections; recommended by various election reform advocates for India.",
            "fact": "Ensures the winning candidate has the support of a genuine majority of voters in the constituency."
        },
        # 93
        {
            "id": "ER_GT_093", "diff": "Hard", "sub": "Electoral Systems",
            "en": "In which country's parliamentary electoral system is the 'Mixed-Member Proportional' (MMP) system used, where voters cast two votes—one for a local constituency MP and one for a political party?",
            "ta": "வாக்காளர்கள் இரண்டு வாக்குகளை (ஒரு வாக்கு உள்ளூர் தொகுதி வேட்பாளருக்கும், மற்றொரு வாக்கு அரசியல் கட்சிக்கும்) அளிக்கும் 'கலப்பு உறுப்பினர் விகிதாச்சார' (MMP) முறை எந்த நாட்டின் நாடாளுமன்றத் தேர்தலில் பயன்படுத்தப்படுகிறது?",
            "opts": [("United States", "அமெரிக்க ஐக்கிய நாடுகள்"), ("Germany (Bundestag)", "ஜெர்மனி (பன்டஸ்டாக்)"), ("United Kingdom", "ஐக்கிய இராச்சியம்"), ("Canada", "கனடா")],
            "key": "B",
            "exp_en": "Germany uses the Mixed-Member Proportional (MMP) system for electing the Bundestag. Each voter has two votes: Erststimme (first vote for local direct candidate) and Zweitstimme (second vote for a political party list, determining overall seat share).",
            "exp_ta": "ஜெர்மனி நாடு கலப்பு உறுப்பினர் விகிதாச்சார (MMP) முறையைப் பயன்படுத்துகிறது; இதில் வாக்காளர்கள் உள்ளூர் வேட்பாளருக்கு ஒரு வாக்கும், அரசியல் கட்சிக்கு ஒரு வாக்கும் என இரு வாக்குகளை அளிக்கின்றனர்.",
            "tip": "The Law Commission 170th Report recommended experimenting with an MMP-type model for Lok Sabha elections.",
            "fact": "New Zealand also adopted the MMP system following a national referendum in 1993."
        },
        # 94
        {
            "id": "ER_GT_094", "diff": "Medium", "sub": "Voting Franchise",
            "en": "Under Article 326 of the Constitution, which of the following is NOT an express constitutional ground on which a citizen may be disqualified from registration as a voter?",
            "ta": "அரசியலமைப்பின் சரத்து 326-ன் கீழ், ஒரு குடிமகனை வாக்காளர் பட்டியலில் பதிவு செய்வதிலிருந்து தகுதிநீக்கம் செய்ய கீழ்க்கண்டவற்றில் எது வெளிப்படையான அரசியலமைப்பு காரணம் அல்ல?",
            "opts": [("Non-residence", "வசிப்பிடம் இன்மை"), ("Unsoundness of mind", "மனநலமின்மை"), ("Illiteracy / Lack of formal education", "கல்வியறிவின்மை / முறையான கல்வி இல்லாமை"), ("Crime or corrupt or illegal practice", "குற்றச் செயல் அல்லது ஊழல் அல்லது சட்டவிரோத நடவடிக்கை")],
            "key": "C",
            "exp_en": "Article 326 explicitly lists four grounds of disqualification: non-residence, unsoundness of mind, crime, or corrupt or illegal practice. Illiteracy or lack of property/education is NOT a disqualification—India adopted universal adult suffrage from inception.",
            "exp_ta": "சரத்து 326 வசிப்பிடமின்மை, மனநலமின்மை, குற்றம் மற்றும் ஊழல் ஆகிய நான்கு காரணங்களை மட்டுமே தகுதியின்மையாகக் கூறுகிறது; கல்வியறிவின்மை அல்லது சொத்து இல்லாமை ஒருபோதும் தகுதியின்மை ஆகாது.",
            "tip": "India established universal adult franchise in 1950 without any literacy or property qualification.",
            "fact": "Over 85% of Indian voters were illiterate when the historic 1st General Election was held in 1951-52."
        },
        # 95
        {
            "id": "ER_GT_095", "diff": "Hard", "sub": "Election Laws Amendment 2021",
            "en": "Under the Election Laws (Amendment) Act 2021, on which grounds can premises and vehicles be requisitioned by the government for election purposes under Section 160 of RPA 1951?",
            "ta": "2021 தேர்தல் சட்டத் திருத்தத்தின் கீழ், 1951 சட்டத்தின் பிரிவு 160-ன் கீழ் தேர்தல் பணிகளுக்காக கட்டிடங்கள் மற்றும் வாகனங்களை அரசு கையகப்படுத்த அனுமதிக்கப்பட்ட காரணங்கள் யாவை?",
            "opts": [("Only for housing candidates", "வேட்பாளர்களுக்கு தங்குமிடம் வழங்க மட்டுமே"), ("For polling stations, counting centers, storage of ballot boxes/EVMs, and accommodation for security forces and polling personnel", "வாக்குச்சாவடிகள், வாக்கு எண்ணிக்கை மையங்கள், EVM சேமிப்பு மற்றும் பாதுகாப்புப் படை/தேர்தல் அலுவலர்கள் தங்குவதற்காக"), ("For holding political party conventions", "அரசியல் கட்சி மாநாடுகளை நடத்த"), ("For private candidate transport", "வேட்பாளரின் சொந்த போக்குவரத்துக்காக")],
            "key": "B",
            "exp_en": "The 2021 amendment expanded Section 160 of RPA 1951, allowing the requisition of premises not only for polling stations and counting halls, but explicitly for the storage of ballot boxes/voting machines and accommodation of security forces and polling personnel.",
            "exp_ta": "2021 திருத்தம் பிரிவு 160-ஐ விரிவுபடுத்தி, வாக்குச்சாவடிகள் மற்றும் எண்ணிக்கை மையங்கள் மட்டுமின்றி, EVM பாதுகாப்பு மற்றும் பாதுகாப்புப் படைகள் தங்குவதற்கும் வளாகங்களைக் கையகப்படுத்த அரசுக்கு அதிகாரமளித்தது.",
            "tip": "Compensation must be paid to owners of requisitioned premises and vehicles under Section 161.",
            "fact": "Premises used for religious worship cannot be requisitioned under Section 160."
        },
        # 96
        {
            "id": "ER_GT_096", "diff": "Medium", "sub": "Electoral Rolls",
            "en": "What is the legal punishment under Section 31 of the Representation of the People Act 1950 for making a false declaration in connection with inclusion or exclusion of names in an electoral roll?",
            "ta": "1950 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 31-ன் கீழ், வாக்காளர் பட்டியலில் பெயர் சேர்த்தல் அல்லது நீக்குதல் தொடர்பாக தவறான பிரகடனம் செய்பவருக்கு விதிக்கப்படும் சட்டப்பூர்வ தண்டனை என்ன?",
            "opts": [("Imprisonment up to 1 year, or fine, or both", "1 ஆண்டு வரை சிறை தண்டனை, அல்லது அபராதம், அல்லது இரண்டும்"), ("Simple warning from the ERO", "ERO-வின் எச்சரிக்கை மட்டுமே"), ("Imprisonment up to 5 years", "5 ஆண்டுகள் வரை சிறை தண்டனை"), ("Cancellation of passport", "பாஸ்போர்ட் ரத்து")],
            "key": "A",
            "exp_en": "Under Section 31 of RPA 1950, if any person makes in connection with the preparation, revision, or correction of an electoral roll any statement or declaration in writing which is false and which he knows or believes to be false, he shall be punishable with imprisonment up to 1 year, or with fine, or with both.",
            "exp_ta": "1950 சட்டத்தின் பிரிவு 31-ன் கீழ், வாக்காளர் பட்டியலில் பெயர் சேர்க்கும்போது அல்லது நீக்கும்போது வேண்டுமென்றே தவறான தகவல்களைத் தருபவருக்கு 1 ஆண்டு வரை சிறை தண்டனை அல்லது அபராதம் அல்லது இரண்டும் விதிக்கப்படலாம்.",
            "tip": "Prevents fraudulent bulk voter additions or malicious deletions.",
            "fact": "The ERO can file a criminal complaint in the court of a Judicial Magistrate."
        },
        # 97
        {
            "id": "ER_GT_097", "diff": "Hard", "sub": "Candidate Disclosures",
            "en": "Under ECI instructions following the Supreme Court's 2018 directive, candidates must declare their financial assets including those of whom in their Form 26 affidavit?",
            "ta": "உச்ச நீதிமன்றத்தின் 2018 உத்தரவைத் தொடர்ந்து தேர்தல் ஆணைய விதிகளின்படி, வேட்பாளர்கள் தங்களின் சொத்துக்களுடன் சேர்த்து யாருடைய சொத்து விவரங்களையும் படிவம் 26 பிரமாணப் பத்திரத்தில் கட்டாயம் அறிவிக்க வேண்டும்?",
            "opts": [("Self only", "தனது சொந்த சொத்துக்கள் மட்டுமே"), ("Self, spouse, and all dependent children", "சுய, வாழ்க்கைத் துணை மற்றும் அனைத்து சார்ந்திருக்கும் குழந்தைகளின் சொத்துக்கள்"), ("Parents and siblings", "பெற்றோர்கள் மற்றும் உடன்பிறப்புகள்"), ("Business partners only", "வணிக கூட்டாளிகள் மட்டுமே")],
            "key": "B",
            "exp_en": "Form 26 requires exhaustive disclosure of movable and immovable assets, bank deposits, jewelry, vehicles, investments, and liabilities for self, spouse, and all dependents (including children financially reliant on the candidate).",
            "exp_ta": "படிவம் 26-ல் வேட்பாளர் தனது சொந்த சொத்துக்கள், வாழ்க்கைத் துணையின் சொத்துக்கள் மற்றும் தன்னைச் சார்ந்துள்ள அனைத்து குழந்தைகளின் அசையும் மற்றும் அசையா சொத்துக்கள், கடன்களை முழுமையாக வெளியிட வேண்டும்.",
            "tip": "Hiding a spouse's or dependent's assets is a corrupt practice and offence under Section 125A.",
            "fact": "In Lok Prahari (2018), SC also mandated disclosing the sources of income of the candidate and spouse."
        },
        # 98
        {
            "id": "ER_GT_098", "diff": "Medium", "sub": "Electoral Administration",
            "en": "Who is the officer appointed under Section 20B of RPA 1951 by the ECI to oversee the counting of votes and ensure that results are declared strictly according to law?",
            "ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 20B-ன் கீழ், வாக்கு எண்ணிக்கையை மேற்பார்வையிடவும் தேர்தல் முடிவுகள் சட்டப்படி அறிவிக்கப்படுவதை உறுதி செய்யவும் தேர்தல் ஆணையத்தால் நியமிக்கப்படும் அதிகாரி யார்?",
            "opts": [("Returning Officer", "தேர்தல் நடத்தும் அதிகாரி"), ("Observer (General Observer)", "தேர்தல் பார்வையாளர் (பொதுப் பார்வையாளர்)"), ("District Magistrate", "மாவட்ட மேஜிஸ்திரேட்"), ("Chief Secretary", "தலைமைச் செயலாளர்")],
            "key": "B",
            "exp_en": "Section 20B of RPA 1951 empowers the ECI to nominate Observers (senior civil servants). The Returning Officer cannot declare the result or issue the Certificate of Election (Form 21C) without the formal written clearance of the General Observer.",
            "exp_ta": "பிரிவு 20B-ன் கீழ் நியமிக்கப்படும் தேர்தல் பொதுப் பார்வையாளரின் (Observer) எழுத்துப்பூர்வ ஒப்புதல் இல்லாமல் தேர்தல் நடத்தும் அதிகாரி தேர்தல் முடிவை அறிவிக்கவோ அல்லது வெற்றிச் சான்றிதழை வழங்கவோ முடியாது.",
            "tip": "Observers act as independent watchdogs directly accountable to the ECI, not the state government.",
            "fact": "Section 20B was inserted into the RPA 1951 in 1996."
        },
        # 99
        {
            "id": "ER_GT_099", "diff": "Hard", "sub": "Electoral Reforms Milestones",
            "en": "Which year marked the introduction of the photo-printed electoral roll (where electors' photographs appear on the official voter roll itself alongside their names) across the country?",
            "ta": "வாக்காளர் பட்டியலில் வாக்காளர்களின் பெயருடன் அவர்களின் புகைப்படமும் அச்சிடப்படும் 'புகைப்பட வாக்காளர் பட்டியல்' (Photo Electoral Roll) நாடு முழுவதும் எந்த ஆண்டு முதல் அறிமுகப்படுத்தப்பட்டது?",
            "opts": [("1993", "1993"), ("2000", "2000"), ("2008", "2008"), ("2014", "2014")],
            "key": "C",
            "exp_en": "Photo Electoral Rolls (PER), where voter photographs are printed directly onto the polling station voter list alongside their serial number and EPIC number, was rolled out nationwide ahead of the 2008-2009 election cycle to eliminate bogus voting.",
            "exp_ta": "வாக்காளர்களின் பெயருடன் அவர்களின் புகைப்படமும் அச்சிடப்படும் புகைப்பட வாக்காளர் பட்டியல் முறை (PER) நாடு முழுவதும் 2008-ல் தொடங்கப்பட்டு 2009 பொதுத்தேர்தலில் முழுமையாக செயல்படுத்தப்பட்டது.",
            "tip": "Photo rolls make it virtually impossible for an impersonator to cast another person's vote.",
            "fact": "Over 99% of electors in India currently have their photographs on the Photo Electoral Rolls."
        },
        # 100
        {
            "id": "ER_GT_100", "diff": "Hard", "sub": "Constitutional Philosophy of Elections",
            "en": "In which landmark case did the Supreme Court observe that 'Democracy is the basic structure of the Constitution and periodic, free and fair elections are the lifeblood of that democracy'?",
            "ta": "எந்த முக்கிய வழக்கில் உச்ச நீதிமன்றம் 'மக்களாட்சி என்பது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பு என்றும், குறிப்பிட்ட கால இடைவெளியில் சுதந்திரமாகவும் நேர்மையாகவும் நடத்தப்படும் தேர்தல்களே அம்மக்களாட்சியின் உயிர்நாடி' என்றும் குறிப்பிட்டது?",
            "opts": [("A.K. Gopalan v. State of Madras (1950)", "ஏ.கே. கோபாலன் எதிர் மெட்ராஸ் மாகாணம் (1950)"), ("Mohinder Singh Gill v. Chief Election Commissioner (1978)", "மொகிந்தர் சிங் கில் எதிர் தலைமை தேர்தல் ஆணையர் (1978)"), ("Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி எதிர் இந்திய ஒன்றியம் (1978)"), ("Golaknath v. State of Punjab (1967)", "கோலக்நாத் எதிர் பஞ்சாப் மாநிலம் (1967)")],
            "key": "B",
            "exp_en": "In Mohinder Singh Gill v. CEC (1978), Justice V.R. Krishna Iyer articulated the profound democratic ethos of Part XV, declaring that free, fair, and periodic elections are the heartbeat of the democratic republic and that Article 324 must be interpreted to advance that noble ideal.",
            "exp_ta": "1978-ல் மொகிந்தர் சிங் கில் வழக்கில், சுதந்திரமான, நேர்மையான மற்றும் குறிப்பிட்ட கால இடைவெளியிலான தேர்தல்களே ஜனநாயகத்தின் உயிர்நாடி என்றும், அதை நிலைநிறுத்தவே சரத்து 324 முழு அதிகாரங்களை தேர்தல் ஆணையத்திற்கு வழங்குகிறது என்றும் நீதிபதி கிருஷ்ண ஐயர் பிரகடனப்படுத்தினார்.",
            "tip": "One of the most eloquent and foundational judicial dissertations on democratic governance in Indian jurisprudence.",
            "fact": "The case arose out of the cancellation of poll in the Ferozepore parliamentary constituency due to booth capturing."
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
    qs = get_gt_part2_questions()
    print(f"Grand Test Part 2 generated {len(qs)} questions.")
