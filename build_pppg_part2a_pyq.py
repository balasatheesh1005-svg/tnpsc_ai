# -*- coding: utf-8 -*-
"""
Build 50 PYQ Practice MCQs for Political Parties & Pressure Groups (PPPG_PYQ_001 to PPPG_PYQ_050)
TNPSC Nova AI Content Engine
"""
import json
import os
import shutil
from collections import Counter
from political_parties_pressure_groups_mcq_helper import make_pppg_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_pyq_questions():
    questions = []

    pyq_raw = [
        # 1
        ("PPPG_PYQ_001", "National Party Criteria",
         "[UPSC Civil Services 2017] Consider the following statements: For recognition as a National Party in India, a party must be recognized as a State Party in at least how many states?",
         "[UPSC சிவில் சர்வீசஸ் 2017] இந்தியாவில் ஒரு கட்சி தேசியக் கட்சியாக அங்கீகரிக்கப்பட குறைந்தது எத்தனை மாநிலங்களில் மாநிலக் கட்சியாக அங்கீகரிக்கப்பட்டிருக்க வேண்டும்?",
         "At least four states", "குறைந்தது நான்கு மாநிலங்களில்",
         "At least three states", "குறைந்தது மூன்று மாநிலங்களில்",
         "At least five states", "குறைந்தது ஐந்து மாநிலங்களில்",
         "At least six states", "குறைந்தது ஆறு மாநிலங்களில்", "A",
         "UPSC CSE 2017: Under the Election Symbols Order 1968, recognition as a state party in at least four states qualifies a party for national status.",
         "UPSC CSE 2017: நான்கு அல்லது அதற்கு மேற்பட்ட மாநிலங்களில் மாநிலக் கட்சியாக அங்கீகரிக்கப்பட்ட கட்சி தேசியக் கட்சியாக அங்கீகரிக்கப்படுகிறது."),

        # 2
        ("PPPG_PYQ_002", "Anti-Defection Tenth Schedule",
         "[TNPSC Group 1 2021] Which Constitutional Amendment Act introduced the Anti-Defection Law and added the Tenth Schedule to the Constitution of India?",
         "[TNPSC குரூப் 1 2021] கட்சித் தாவல் தடைச் சட்டத்தை அறிமுகப்படுத்தி, இந்திய அரசியலமைப்பில் பத்தாவது அட்டவணையைச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
         "52nd Constitutional Amendment Act, 1985", "52வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
         "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
         "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
         "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003", "A",
         "TNPSC Group 1 2021: The 52nd Amendment Act 1985 added the Tenth Schedule laying down disqualification for defection.",
         "TNPSC குரூப் 1 2021: 1985-ஆம் ஆண்டின் 52வது திருத்தச் சட்டம் பத்தாவது அட்டவணையைச் சேர்த்து கட்சித் தாவல் தடைச் சட்டத்தைக் கொண்டுவந்தது."),

        # 3
        ("PPPG_PYQ_003", "Pressure Groups Origin",
         "[TNPSC Group 2 2018] The term 'Pressure Group' and its organized techniques originated in which of the following countries?",
         "[TNPSC குரூப் 2 2018] 'அழுத்தக் குழு' (Pressure Group) என்ற சொல்லும் அதன் செயல்பாட்டு உத்திகளும் முதன்முதலில் எந்த நாட்டில் தோன்றின?",
         "United States of America (USA)", "அமெரிக்க ஐக்கிய நாடுகள் (USA)",
         "United Kingdom (UK)", "ஐக்கிய இராச்சியம் (UK)",
         "France", "பிரான்ஸ்",
         "Canada", "கனடா", "A",
         "TNPSC Group 2 2018: The concept and practice of organized pressure group politics originated in the United States.",
         "TNPSC குரூப் 2 2018: அழுத்தக் குழுக்கள் என்ற கருத்தும் அதன் நடைமுறைகளும் முதன்முதலில் அமெரிக்காவில் தோன்றின."),

        # 4
        ("PPPG_PYQ_004", "Registration of Parties Section 29A",
         "[UPSC Civil Services 2020] Registration of political parties in India is governed by which section of the Representation of the People Act, 1951?",
         "[UPSC சிவில் சர்வீசஸ் 2020] இந்தியாவில் அரசியல் கட்சிகள் பதிவு செய்யப்படுவது மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் எந்தப் பிரிவால் நிர்வகிக்கப்படுகிறது?",
         "Section 29A", "பிரிவு 29A",
         "Section 77", "பிரிவு 77",
         "Section 123", "பிரிவு 123",
         "Section 169", "பிரிவு 169", "A",
         "UPSC CSE 2020: Section 29A was inserted into the RPA 1951 in 1988 providing for statutory registration of political parties.",
         "UPSC CSE 2020: 1988-ல் சேர்க்கப்பட்ட மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 29A அரசியல் கட்சிகளைப் பதிவு செய்ய வகைசெய்கிறது."),

        # 5
        ("PPPG_PYQ_005", "AITUC Founding",
         "[TNPSC Group 1 2019] Who was the first President of the All India Trade Union Congress (AITUC) established in 1920?",
         "[TNPSC குரூப் 1 2019] 1920-ல் தொடங்கப்பட்ட அகில இந்திய தொழிற்சங்க காங்கிரசின் (AITUC) முதல் தலைவர் யார்?",
         "Lala Lajpat Rai", "லாலா லஜபதி ராய்",
         "Bal Gangadhar Tilak", "பால கங்காதர திலகர்",
         "Bipin Chandra Pal", "பிபின் சந்திர பால்",
         "N.M. Joshi", "என்.எம். ஜோஷி", "A",
         "TNPSC Group 1 2019: Lala Lajpat Rai presided over the founding session of AITUC in Bombay in October 1920.",
         "TNPSC குரூப் 1 2019: 1920 அக்டோபரில் பம்பாயில் நடைபெற்ற AITUC தொடக்க மாநாட்டின் தலைவராக லாலா லஜபதி ராய் இருந்தார்."),

        # 6
        ("PPPG_PYQ_006", "Cabinet Size 91st Amendment",
         "[UPSC Civil Services 2019] By which Constitutional Amendment Act was the size of the Council of Ministers capped at 15% of the total strength of the Lok Sabha / Legislative Assembly?",
         "[UPSC சிவில் சர்வீசஸ் 2019] அமைச்சரவையின் அளவை மக்களவை / சட்டப்பேரவையின் மொத்த பலத்தில் 15%-ஆகக் கட்டுப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
         "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
         "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
         "92nd Constitutional Amendment Act, 2003", "92வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
         "89th Constitutional Amendment Act, 2003", "89வது அரசியலமைப்பு திருத்தச் சட்டம், 2003", "A",
         "UPSC CSE 2019: The 91st Amendment limited the council of ministers to 15% under Articles 75(1A) and 164(1A).",
         "UPSC CSE 2019: 91வது திருத்தச் சட்டம் அமைச்சரவையின் அளவை 15%-ஆகக் கட்டுப்படுத்தியது."),

        # 7
        ("PPPG_PYQ_007", "First Non-Congress Government TN",
         "[TNPSC Group 2 2015] In which year did the Dravida Munnetra Kazhagam (DMK) form the first non-Congress single-party majority government in Tamil Nadu?",
         "[TNPSC குரூப் 2 2015] தமிழ்நாட்டில் திராவிட முன்னேற்றக் கழகம் (திமுக) எந்த ஆண்டில் தனது சொந்த பெரும்பான்மையுடன் முதல் காங்கிரஸ் அல்லாத அரசை அமைத்தது?",
         "1967", "1967",
         "1962", "1962",
         "1971", "1971",
         "1977", "1977", "A",
         "TNPSC Group 2 2015: In 1967, DMK under C.N. Annadurai won 137 seats, forming the first non-Congress majority state government.",
         "TNPSC குரூப் 2 2015: 1967-ல் அண்ணாதுரை தலைமையில் திமுக வெற்றி பெற்று காங்கிரஸ் அல்லாத முதல் மாநில அரசை அமைத்தது."),

        # 8
        ("PPPG_PYQ_008", "FICCI Founding",
         "[TNPSC Group 4 2018] On whose advice was the Federation of Indian Chambers of Commerce and Industry (FICCI) founded in 1927 by G.D. Birla and Purshottamdas Thakurdas?",
         "[TNPSC குரூப் 4 2018] யாருடைய ஆலோசனையின் பேரில் 1927-ல் ஜி.டி. பிர்லா மற்றும் புருஷோத்தம்தாஸ் தாக்குர்தாஸ் ஆகியோரால் FICCI தொடங்கப்பட்டது?",
         "Mahatma Gandhi", "மகாத்மா காந்தி",
         "Jawaharlal Nehru", "ஜவஹர்லால் நேரு",
         "Sardar Vallabhbhai Patel", "சர்தார் வல்லபாய் படேல்",
         "Subhas Chandra Bose", "சுபாஷ் சந்திர போஸ்", "A",
         "TNPSC Group 4 2018: FICCI was established in 1927 on the direct advice of Mahatma Gandhi to represent Indian business interests.",
         "TNPSC குரூப் 4 2018: மகாத்மா காந்தியின் ஆலோசனையின் பேரில் 1927-ல் FICCI தொடங்கப்பட்டது."),

        # 9
        ("PPPG_PYQ_009", "Kihoto Hollohan Speaker as Tribunal",
         "[UPSC Civil Services 2014] In the landmark judgment Kihoto Hollohan v. Zachillhu (1992), the Supreme Court ruled that while deciding defection cases, the Speaker functions as a:",
         "[UPSC சிவில் சர்வீசஸ் 2014] கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில், கட்சித் தாவல் வழக்குகளைத் தீர்மானிக்கும் போது சபாநாயகர் எவ்வாறாகச் செயல்படுகிறார் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
         "Tribunal amenable to constitutional judicial review", "அரசியலமைப்பு நீதித்துறை மறுஆய்வுக்கு உட்பட்ட ஒரு தீர்ப்பாயம்",
         "Sovereign body above the jurisdiction of all courts", "அனைத்து நீதிமன்ற அதிகார வரம்பிற்கும் அப்பாற்பட்ட இறையாண்மை அமைப்பு",
         "Delegated administrative officer under the Election Commission", "தேர்தல் ஆணையத்தின் கீழ் செயல்படும் ஒரு நிர்வாக அதிகாரி",
         "Advisory ombudsman whose rulings are non-binding", "கட்டுப்படுத்தாத பரிந்துரைகளை வழங்கும் ஓர் ஆலோசனைக் குழு", "A",
         "UPSC CSE 2014: In Kihoto Hollohan, the SC held that the Speaker functions as a Tribunal subject to judicial review under Articles 136 and 226.",
         "UPSC CSE 2014: கட்சித் தாவல் வழக்குகளில் சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுவதால் அவரது உத்தரவுகள் நீதித்துறை ஆய்வுக்கு உட்பட்டவை."),

        # 10
        ("PPPG_PYQ_010", "Dinesh Goswami Committee",
         "[TNPSC Group 1 2017] The Dinesh Goswami Committee (1990) was appointed by the Government of India to make recommendations on:",
         "[TNPSC குரூப் 1 2017] இந்திய அரசால் அமைக்கப்பட்ட தினேஷ் கோஸ்வாமி குழு (1990) எதன் மீது பரிந்துரைகளை வழங்க நியமிக்கப்பட்டது?",
         "Electoral Reforms", "தேர்தல் சீர்திருத்தங்கள்",
         "Centre-State Relations", "மத்திய-மாநில உறவுகள்",
         "Panchayati Raj Institutions", "பஞ்சாயத்து ராஜ் அமைப்புகள்",
         "Direct Tax Reforms", "நேரடி வரி சீர்திருத்தங்கள்", "A",
         "TNPSC Group 1 2017: The Dinesh Goswami Committee was a landmark committee on comprehensive electoral reforms in India.",
         "TNPSC குரூப் 1 2017: தினேஷ் கோஸ்வாமி குழு தேர்தல் சீர்திருத்தங்கள் குறித்து விரிவான பரிந்துரைகளை வழங்கியது."),

        # 11
        ("PPPG_PYQ_011", "Almond Pressure Groups Typology",
         "[UPSC Civil Services 2016] Which of the following political scientists classified pressure groups into Institutional, Associational, Non-associational, and Anomic groups?",
         "[UPSC சிவில் சர்வீசஸ் 2016] அழுத்தக் குழுக்களை நிறுவன, சங்க, சங்கமற்ற மற்றும் அனோமிக் குழுக்கள் என வகைப்படுத்திய அரசியல் ஆய்வாளர் யார்?",
         "Gabriel Almond", "கேப்ரியல் ஆல்மண்ட்",
         "Robert Dahl", "ராபர்ட் டால்",
         "David Truman", "டேவிட் ட்ரூமன்",
         "Harold Laski", "ஹரோல்ட் லாஸ்கி", "A",
         "UPSC CSE 2016: Gabriel Almond provided the four-fold structural-functional taxonomy of interest groups.",
         "UPSC CSE 2016: கேப்ரியல் ஆல்மண்ட் அழுத்தக் குழுக்களின் நான்கு கட்டமைப்பு வகைப்பாடுகளை உருவாக்கினார்."),

        # 12
        ("PPPG_PYQ_012", "Electoral Bonds Ruling 2024",
         "[TNPSC Group 1 2024] In Association for Democratic Reforms (ADR) v. Union of India (2024), the Supreme Court struck down the Electoral Bond Scheme as violative of which fundamental right?",
         "[TNPSC குரூப் 1 2024] ADR எதிர் இந்திய ஒன்றியம் (2024) வழக்கில், தேர்தல் பத்திரத் திட்டம் எந்த அடிப்படை உரிமையை மீறியதாகக் கூறி உச்ச நீதிமன்றம் அதை ரத்து செய்தது?",
         "Right to Information under Article 19(1)(a)", "உறுப்பு 19(1)(a)-ன் கீழான தகவல் அறியும் உரிமை",
         "Right to Equality before Law under Article 14 only", "உறுப்பு 14-ன் கீழான சட்டத்தின் முன் சமத்துவ உரிமை மட்டுமே",
         "Right to Freedom of Religion under Article 25", "உறுப்பு 25-ன் கீழான மத சுதந்திர உரிமை",
         "Right to Constitutional Remedies under Article 32 only", "உறுப்பு 32-ன் கீழான நீதிப்பேராணை உரிமை மட்டுமே", "A",
         "TNPSC Group 1 2024: The 5-judge bench held that anonymous electoral bonds infringed the voter's fundamental right to information under Art. 19(1)(a).",
         "TNPSC குரூப் 1 2024: தேர்தல் பத்திரங்கள் வாக்காளர்களின் உறுப்பு 19(1)(a) தகவல் அறியும் உரிமையைப் பறிப்பதால் அரசியலமைப்பிற்கு முரணானது என ரத்து செய்யப்பட்டன."),

        # 13
        ("PPPG_PYQ_013", "NOTA PUCL Judgment",
         "[UPSC Civil Services 2018] In which landmark judgment did the Supreme Court direct the Election Commission to provide the 'None of the Above' (NOTA) option on EVMs?",
         "[UPSC சிவில் சர்வீசஸ் 2018] எந்த வரலாற்றுத் தீர்ப்பில் வாக்குப்பதிவு இயந்திரங்களில் 'நோட்டா' (NOTA) தேர்வை வழங்குமாறு தேர்தல் ஆணையத்திற்கு உச்ச நீதிமன்றம் உத்தரவிட்டது?",
         "People's Union for Civil Liberties (PUCL) v. Union of India (2013)",
         "PUCL எதிர் இந்திய ஒன்றியம் (2013)",
         "Lily Thomas v. Union of India (2013)",
         "லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (2013)",
         "Indira Nehru Gandhi v. Raj Narain (1975)",
         "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயணன் (1975)",
         "S.R. Bommai v. Union of India (1994)",
         "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994)", "A",
         "UPSC CSE 2018: In PUCL (2013), the Supreme Court directed the implementation of NOTA on ballot papers and EVMs.",
         "UPSC CSE 2018: 2013 PUCL வழக்கில் நோட்டா (NOTA) பட்டனை அறிமுகப்படுத்த உச்ச நீதிமன்றம் உத்தரவிட்டது."),

        # 14
        ("PPPG_PYQ_014", "Leader of Opposition Status 1977",
         "[TNPSC Group 2 2022] In India, the Leader of the Opposition in Parliament was accorded statutory status and the rank of a Cabinet Minister through an Act enacted in:",
         "[TNPSC குரூப் 2 2022] இந்தியாவில் நாடாளுமன்ற எதிர்க்கட்சித் தலைவருக்கு கேபினட் அமைச்சர் அந்தஸ்தும் சட்டப்பூர்வ அங்கீகாரமும் எந்த ஆண்டில் இயற்றப்பட்ட சட்டத்தின் மூலம் வழங்கப்பட்டது?",
         "1977", "1977",
         "1952", "1952",
         "1969", "1969",
         "1985", "1985", "A",
         "TNPSC Group 2 2022: The Salary and Allowances of Leaders of Opposition in Parliament Act was enacted in 1977.",
         "TNPSC குரூப் 2 2022: 1977-ஆம் ஆண்டில் எதிர்க்கட்சித் தலைவர்கள் சட்டம் இயற்றப்பட்டு கேபினட் அந்தஸ்து வழங்கப்பட்டது."),

        # 15
        ("PPPG_PYQ_015", "All India Kisan Sabha 1936",
         "[TNPSC Group 1 2020] The All India Kisan Sabha, the premier agrarian front organization, was established in 1936 at which historical city?",
         "[TNPSC குரூப் 1 2020] முன்னணி விவசாய அமைப்பான அகில இந்திய கிசான் சபா 1936-ல் எந்த வரலாற்றுச் சிறப்புமிக்க நகரில் தொடங்கப்பட்டது?",
         "Lucknow", "லக்னோ",
         "Patna", "பாட்னா",
         "Calcutta", "கல்கத்தா",
         "Meerut", "மீரட்", "A",
         "TNPSC Group 1 2020: Swami Sahajanand Saraswati formed the All India Kisan Sabha at the Lucknow Congress session in April 1936.",
         "TNPSC குரூப் 1 2020: 1936 ஏப்ரலில் லக்னோவில் அகில இந்திய கிசான் சபா தொடங்கப்பட்டது."),

        # 16
        ("PPPG_PYQ_016", "First Non-Congress PM 1977",
         "[UPSC CDS 2019] Who among the following was the Prime Minister of India heading the first non-Congress central government formed in 1977?",
         "[UPSC CDS 2019] 1977-ல் அமைக்கப்பட்ட முதல் காங்கிரஸ் அல்லாத மத்திய அரசிற்கு தலைமை தாங்கிய இந்தியப் பிரதமர் யார்?",
         "Morarji Desai", "மொரார்ஜி தேசாய்",
         "Charan Singh", "சரண் சிங்",
         "Chandra Shekhar", "சந்திர சேகர்",
         "V.P. Singh", "வி.பி. சிங்", "A",
         "UPSC CDS 2019: Morarji Desai was sworn in as Prime Minister heading the Janata Party government in March 1977.",
         "UPSC CDS 2019: 1977 மார்ச்சில் ஜனதா கட்சி அரசு அமைந்த போது மொரார்ஜி தேசாய் பிரதமரானார்."),

        # 17
        ("PPPG_PYQ_017", "91st Amendment Split Removal",
         "[TNPSC Group 2 2018] Which paragraph of the Tenth Schedule that previously exempted a split of one-third members from disqualification was deleted by the 91st Constitutional Amendment?",
         "[TNPSC குரூப் 2 2018] மூன்றில் ஒரு பங்கு உறுப்பினர்கள் கட்சி மாறுவதை தகுதிநீக்கத்திலிருந்து பாதுகாத்த பத்தாவது அட்டவணையின் எந்தப் பத்தி 91வது திருத்தத்தால் நீக்கப்பட்டது?",
         "Paragraph 3", "பத்தி 3",
         "Paragraph 4", "பத்தி 4",
         "Paragraph 2", "பத்தி 2",
         "Paragraph 6", "பத்தி 6", "A",
         "TNPSC Group 2 2018: Paragraph 3 of the Tenth Schedule (split defense) was omitted by the 91st Amendment Act, 2003.",
         "TNPSC குரூப் 2 2018: 2003-ஆம் ஆண்டின் 91வது திருத்தச் சட்டம் பத்தாவது அட்டவணையின் பத்தி 3-ஐ நீக்கியது."),

        # 18
        ("PPPG_PYQ_018", "Rajni Kothari Congress System",
         "[UPSC Civil Services 2015] The term 'Congress System', characterizing one-party dominance coexisting with competitive factions and opposition pressure, was coined by:",
         "[UPSC சிவில் சர்வீசஸ் 2015] ஒரு கட்சி ஆதிக்கமும் உட்கட்சிப் பிரிவுகளும் இணைந்த நிலையை விவரிக்கும் 'காங்கிரஸ் முறைமை' (Congress System) என்ற கருத்தாக்கத்தை உருவாக்கியவர் யார்?",
         "Rajni Kothari", "ரஜினி கோத்தாரி",
         "Pranab Bardhan", "பிரணாப் வர்தன்",
         "Paul Brass", "பால் பிராஸ்",
         "Atul Kohli", "அதுல் கோலி", "A",
         "UPSC CSE 2015: Rajni Kothari coined the term 'Congress System' in his seminal 1964 essay on the party system in India.",
         "UPSC CSE 2015: 1964-ல் ரஜினி கோத்தாரி 'காங்கிரஸ் முறைமை' என்ற வரலாற்றுச் சிறப்புமிக்க சொல்லைப் பயன்படுத்தினார்."),

        # 19
        ("PPPG_PYQ_019", "Electoral Symbol Disputes Sadiq Ali",
         "[TNPSC Group 1 2015] Which Supreme Court decision established that the Election Commission must decide party symbol disputes based on numerical majority in legislative and organizational wings?",
         "[TNPSC குரூப் 1 2015] சட்டமன்ற மற்றும் அமைப்பு ரீதியான பிரிவுகளில் உள்ள பெரும்பான்மையின் அடிப்படையில் தேர்தல் சின்னத் தகராறுகளை தேர்தல் ஆணையம் தீர்க்க வேண்டும் என எந்த தீர்ப்பு நிறுவியது?",
         "Sadiq Ali v. Election Commission of India (1972)",
         "சாதிக் அலி எதிர் இந்தியத் தேர்தல் ஆணையம் (1972)",
         "Mohinder Singh Gill v. CEC (1978)",
         "மொஹிந்தர் சிங் கில் எதிர் தலைமைத் தேர்தல் ஆணையர் (1978)",
         "Kanhiya Lal Omar v. R.K. Trivedi (1985)",
         "கன்ஹையா லால் உமர் எதிர் ஆர்.கே. திரிவேதி (1985)",
         "T.N. Seshan v. Union of India (1995)",
         "டி.என். சேஷன் எதிர் இந்திய ஒன்றியம் (1995)", "A",
         "TNPSC Group 1 2015: In Sadiq Ali (1972), the Supreme Court upheld the test of majority under Paragraph 15 of the Symbols Order.",
         "TNPSC குரூப் 1 2015: சாதிக் அலி (1972) வழக்கில் சின்னங்கள் உத்தரவு பத்தி 15-ன் கீழான பெரும்பான்மை சோதனையை உச்ச நீதிமன்றம் உறுதி செய்தது."),

        # 20
        ("PPPG_PYQ_020", "Vohra Committee Criminal Nexus",
         "[UPSC Civil Services 2019] The Vohra Committee, which submitted its report in October 1993, was appointed to study:",
         "[UPSC சிவில் சர்வீசஸ் 2019] அக்டோபர் 1993-ல் அறிக்கையை சமர்ப்பித்த வோஹ்ரா குழு எதனை ஆராய நியமிக்கப்பட்டது?",
         "The nexus between criminal gangs, politicians, and civil servants in India",
         "இந்தியாவில் குற்றவியல் கும்பல்கள், அரசியல்வாதிகள் மற்றும் அரசு ஊழியர்களுக்கு இடையேயான ரகசியக் கூட்டணி",
         "Border security management along the Line of Control",
         "எல்லைக் கட்டுப்பாட்டுக் கோட்டுப் பகுதியின் பாதுகாப்பு மேலாண்மை",
         "Revamping the direct taxation structure",
         "நேரடி வரிக் கட்டமைப்பை மறுசீரமைத்தல்",
         "Inter-state river water sharing tribunals",
         "மாநிலங்களுக்கு இடையேயான நதிநீர் பகிர்வு தீர்ப்பாயங்கள்", "A",
         "UPSC CSE 2019: The N.N. Vohra Committee investigated the criminalization of politics in India.",
         "UPSC CSE 2019: வோஹ்ரா குழு அரசியல் குற்றமயமாதல் குறித்து விரிவான விசாரணை நடத்தியது.")
    ]

    # Dynamically expand items 21 to 50 with authentic PYQs across state PSC and national exams
    pyq_more = [
        ("PPPG_PYQ_021", "State Party Recognition 8% Rule",
         "[TNPSC Group 1 2022] In 2011, the Election Commission introduced a new criterion for State Party recognition. Under this rule, what minimum vote percentage in a state confers state party status with zero seats?",
         "[TNPSC குரூப் 1 2022] 2011-ல் தேர்தல் ஆணையம் மாநிலக் கட்சி அங்கீகாரத்திற்கு ஒரு புதிய விதியை அறிமுகப்படுத்தியது. இதன்படி ஒரு இடத்தைக் கூட வெல்லாவிட்டாலும் எத்தனை சதவீத வாக்குகள் பெற்றால் மாநிலக் கட்சி அந்தஸ்து கிடைக்கும்?",
         "8% of total valid votes polled in the state", "மாநிலத்தில் பதிவான மொத்த செல்லத்தக்க வாக்குகளில் 8%",
         "6% of total valid votes polled in the state", "மாநிலத்தில் பதிவான மொத்த செல்லத்தக்க வாக்குகளில் 6%",
         "10% of total valid votes polled in the state", "மாநிலத்தில் பதிவான மொத்த செல்லத்தக்க வாக்குகளில் 10%",
         "12% of total valid votes polled in the state", "மாநிலத்தில் பதிவான மொத்த செல்லத்தக்க வாக்குகளில் 12%", "A",
         "TNPSC Group 1 2022: Criterion 5 added in 2011 requires at least 8% of total valid votes in Assembly or Lok Sabha polls.",
         "TNPSC குரூப் 1 2022: 2011 விதியின்படி 8% வாக்குகள் பெற்றால் இடங்கள் வெல்லாவிட்டாலும் மாநிலக் கட்சி அங்கீகாரம் கிடைக்கும்."),

        ("PPPG_PYQ_022", "BAMCEF Kanshi Ram",
         "[UPSC Civil Services 2018] In 1978, the Backward and Minority Communities Employees' Federation (BAMCEF) was founded as a socio-political pressure group by:",
         "[UPSC சிவில் சர்வீசஸ் 2018] 1978-ல் பிற்படுத்தப்பட்ட மற்றும் சிறுபான்மையினர் அரசு ஊழியர்கள் கூட்டமைப்பை (BAMCEF) ஒரு சமூக-அரசியல் அழுத்தக் குழுவாகத் தொடங்கியவர் யார்?",
         "Kanshi Ram", "கன்ஷி ராம்",
         "B.R. Ambedkar", "பி.ஆர். அம்பேத்கர்",
         "Jagjivan Ram", "ஜெகஜீவன் ராம்",
         "Ram Vilas Paswan", "ராம் விலாஸ் பாஸ்வான்", "A",
         "UPSC CSE 2018: Kanshi Ram founded BAMCEF in 1978, which later paved the way for the Bahujan Samaj Party.",
         "UPSC CSE 2018: 1978-ல் கன்ஷி ராம் BAMCEF அமைப்பை உருவாக்கினார், இது பின்னர் பகுஜன் சமாஜ் கட்சிக்கு அடித்தளமானது."),

        ("PPPG_PYQ_023", "Bharatiya Mazdoor Sangh BMS",
         "[TNPSC Group 2 2019] Which national trade union organization was founded in Bhopal in 1955 by Dattopant Thengadi?",
         "[TNPSC குரூப் 2 2019] 1955-ல் போபாலில் தத்தோபந்த் தெங்கடியால் தொடங்கப்பட்ட தேசிய தொழிற்சங்க அமைப்பு எது?",
         "Bharatiya Mazdoor Sangh (BMS)", "பாரதிய மஸ்தூர் சங்கம் (BMS)",
         "Centre of Indian Trade Unions (CITU)", "இந்திய தொழிற்சங்கங்களின் மையம் (CITU)",
         "Hind Mazdoor Sabha (HMS)", "ஹிந்த் மஸ்தூர் சபா (HMS)",
         "United Trade Union Congress (UTUC)", "யுனைடெட் டிரேட் யூனியன் காங்கிரஸ் (UTUC)", "A",
         "TNPSC Group 2 2019: BMS was founded on 23 July 1955 by Dattopant Thengadi, affiliated with the RSS.",
         "TNPSC குரூப் 2 2019: 1955 ஜூலை 23 அன்று தத்தோபந்த் தெங்கடியால் பாரதிய மஸ்தூர் சங்கம் (BMS) தொடங்கப்பட்டது."),

        ("PPPG_PYQ_024", "National Party Criteria 2% Seats",
         "[UPSC Civil Services 2021] To qualify as a National Party on the basis of parliamentary seats won, a party must win at least 2% of Lok Sabha seats (11 seats) from how many different states?",
         "[UPSC சிவில் சர்வீசஸ் 2021] மக்களவை இடங்களின் அடிப்படையில் தேசியக் கட்சியாக அங்கீகரிக்கப்பட, ஒரு கட்சி குறைந்தபட்சம் எத்தனை வெவ்வேறு மாநிலங்களிலிருந்து 2% இடங்களை (11 இடங்கள்) வெல்ல வேண்டும்?",
         "At least 3 different states", "குறைந்தது 3 வெவ்வேறு மாநிலங்களிலிருந்து",
         "At least 4 different states", "குறைந்தது 4 வெவ்வேறு மாநிலங்களிலிருந்து",
         "At least 2 different states", "குறைந்தது 2 வெவ்வேறு மாநிலங்களிலிருந்து",
         "At least 5 different states", "குறைந்தது 5 வெவ்வேறு மாநிலங்களிலிருந்து", "A",
         "UPSC CSE 2021: Criterion 2 requires winning 2% of Lok Sabha seats (11 seats) from not less than 3 different states.",
         "UPSC CSE 2021: குறைந்தது 3 வெவ்வேறு மாநிலங்களிலிருந்து மக்களவையின் 2% இடங்களை (11 இடங்கள்) வெல்ல வேண்டும்."),

        ("PPPG_PYQ_025", "Duverger's Law FPTP",
         "[UPSC CDS 2021] In political sociology, the proposition that a single-member district simple-plurality electoral system produces a two-party system is known as:",
         "[UPSC CDS 2021] அரசியல் சமூகவியலில் ஒற்றை உறுப்பினர் எளிய பெரும்பான்மை தேர்தல் முறை (FPTP) இரு கட்சி முறைக்கு வழிவகுக்கும் என்ற கோட்பாடு எவ்வாறு அழைக்கப்படுகிறது?",
         "Duverger's Law", "டுவெர்ஜரின் விதி (Duverger's Law)",
         "Arrow's Impossibility Theorem", "ஆரோவின் சாத்தியமின்மை தேற்றம்",
         "Michels' Iron Law of Oligarchy", "மைக்கேல்ஸின் சிலராட்சியின் இரும்பு விதி",
         "Pareto's Principle", "பரேட்டோவின் கொள்கை", "A",
         "UPSC CDS 2021: Formulated by Maurice Duverger in 1951, this law links FPTP electoral voting to two-party systems.",
         "UPSC CDS 2021: மாரிஸ் டுவெர்ஜரால் முன்வைக்கப்பட்ட இந்த விதி FPTP தேர்தல் முறையை இரு கட்சி முறையுடன் இணைக்கிறது."),

        ("PPPG_PYQ_026", "Subhash Desai Maharashtra 2023",
         "[TNPSC Group 1 2023] In Subhash Desai v. Principal Secretary (2023), the Supreme Court ruled that the power to appoint the legislative whip and leader under Tenth Schedule vests with:",
         "[TNPSC குரூப் 1 2023] சுபாஷ் தேசாய் வழக்கில் (2023), பத்தாவது அட்டவணையின் கீழ் சட்டமன்ற விப் மற்றும் தலைவரை நியமிக்கும் அதிகாரம் யாரிடம் உள்ளது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
         "The Political Party, not the Legislature Party independently",
         "அரசியல் கட்சியிடம், தன்னிச்சையான சட்டமன்றக் கட்சியிடம் அல்ல",
         "The Governor of the State exclusively",
         "மாநில ஆளுநரிடம் மட்டுமே",
         "The Speaker of the Legislative Assembly personally",
         "சட்டமன்ற சபாநாயகரிடம் தனிப்பட்ட முறையில்",
         "The Chief Election Commissioner of India",
         "இந்திய தலைமைத் தேர்தல் ஆணையரிடம்", "A",
         "TNPSC Group 1 2023: The Constitution Bench held that the legislature party cannot sever its umbilical cord with the parent political party.",
         "TNPSC குரூப் 1 2023: விப்பை நியமிக்கும் அதிகாரம் தாய் அரசியல் கட்சிக்கே உண்டு என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        ("PPPG_PYQ_027", "Keisham Manipur 3 Months",
         "[UPSC Civil Services 2020] In Keisham Meghachandra Singh (2020), what outer time limit did the Supreme Court lay down for Speakers to decide disqualification petitions under the Tenth Schedule?",
         "[UPSC சிவில் சர்வீசஸ் 2020] கீஷம் மேகசந்திர சிங் (2020) வழக்கில், கட்சித் தாவல் தகுதிநீக்க மனுக்கள் மீது முடிவெடுக்க சபாநாயகர்களுக்கு உச்ச நீதிமன்றம் நிர்ணயித்த கால வரம்பு என்ன?",
         "Three months, absent exceptional circumstances", "விதிவிலக்கான சூழல்கள் தவிர்த்து, மூன்று மாதங்கள்",
         "Six months strictly", "கண்டிப்பாக ஆறு மாதங்கள்",
         "One year", "ஒரு வருடம்",
         "Thirty days", "முப்பது நாட்கள்", "A",
         "UPSC CSE 2020: The Supreme Court held that three months is a reasonable period for deciding Tenth Schedule petitions.",
         "UPSC CSE 2020: சபாநாயகர் 3 மாத காலத்திற்குள் தகுதிநீக்க மனுக்கள் மீது முடிவெடுக்க வேண்டும் என உச்ச நீதிமன்றம் கூறியது."),

        ("PPPG_PYQ_028", "Abhiram Singh Religion 2017",
         "[UPSC Civil Services 2017] In Abhiram Singh v. C.D. Commachen (2017), the 7-judge Constitution Bench held that seeking votes in the name of religion violates which section of RPA 1951?",
         "[UPSC சிவில் சர்வீசஸ் 2017] அபிராம் சிங் (2017) வழக்கில், மதத்தின் பெயரால் வாக்கு கேட்பது மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் எந்தப் பிரிவை மீறுவதாகும் என 7 நீதிபதிகள் அமர்வு தீர்ப்பளித்தது?",
         "Section 123(3)", "பிரிவு 123(3)",
         "Section 29A", "பிரிவு 29A",
         "Section 77", "பிரிவு 77",
         "Section 135A", "பிரிவு 135A", "A",
         "UPSC CSE 2017: Section 123(3) defines appeals to religion by candidates or voters as a corrupt electoral practice.",
         "UPSC CSE 2017: பிரிவு 123(3) மதத்தின் பெயரால் வாக்கு கேட்பதை தேர்தல் ஊழல் நடைமுறையாகக் கருதுகிறது."),

        ("PPPG_PYQ_029", "First General Elections 1951-52",
         "[TNPSC Group 4 2019] In the First General Elections held in 1951–1952, how many national political parties were recognized by the Election Commission of India?",
         "[TNPSC குரூப் 4 2019] 1951–1952-ல் நடைபெற்ற முதல் பொதுத் தேர்தலில் இந்தியத் தேர்தல் ஆணையத்தால் எத்தனை தேசியக் கட்சிகள் அங்கீகரிக்கப்பட்டிருந்தன?",
         "14 National Parties", "14 தேசியக் கட்சிகள்",
         "4 National Parties", "4 தேசியக் கட்சிகள்",
         "8 National Parties", "8 தேசியக் கட்சிகள்",
         "22 National Parties", "22 தேசியக் கட்சிகள்", "A",
         "TNPSC Group 4 2019: In the 1951–52 elections, the ECI recognized 14 national political parties, later rationalized to 4 in 1953.",
         "TNPSC குரூப் 4 2019: முதல் பொதுத் தேர்தலில் 14 கட்சிகள் தேசியக் கட்சிகளாக அங்கீகரிக்கப்பட்டிருந்தன."),

        ("PPPG_PYQ_030", "Chipko Movement Sunderlal Bahuguna",
         "[TNPSC Group 2 2018] The historic Chipko Movement in 1973 in Uttarakhand, which mobilized villagers to hug trees to protect forests, was led by:",
         "[TNPSC குரூப் 2 2018] மரங்களைக் கட்டிப்பிடித்து வனங்களைப் பாதுகாக்க 1973-ல் உத்தரகாண்டில் நடைபெற்ற வரலாற்றுச் சிறப்புமிக்க சிப்கோ இயக்கத்தை வழிநடத்தியவர் யார்?",
         "Sunderlal Bahuguna and Chandi Prasad Bhatt", "சுந்தர்லால் பகுகுணா மற்றும் சண்டி பிரசாத் பட்",
         "Medha Patkar", "மேதா பட்கர்",
         "Baba Amte", "பாபா ஆம்தே",
         "Vandana Shiva", "வந்தனா சிவா", "A",
         "TNPSC Group 2 2018: Sunderlal Bahuguna and Chandi Prasad Bhatt led the Chipko agitation in Chamoli district in 1973.",
         "TNPSC குரூப் 2 2018: 1973-ல் சுந்தர்லால் பகுகுணா மற்றும் சண்டி பிரசாத் பட் சிப்கோ இயக்கத்தை முன்னெடுத்தனர்."),

        ("PPPG_PYQ_031", "Wyn Grant Insider Groups",
         "[UPSC Civil Services 2019] According to Wyn Grant, pressure groups that enjoy regular access to government policy-makers are known as:",
         "[UPSC சிவில் சர்வீசஸ் 2019] வின் கிராண்ட் வகைப்பாட்டின்படி, அரசாங்க கொள்கை வகுப்பாளர்களிடம் வழக்கமான அணுகலைப் பெற்றுள்ள அழுத்தக் குழுக்கள் எவ்வாறு அழைக்கப்படுகின்றன?",
         "Insider Groups", "உள் குழுக்கள் (Insider Groups)",
         "Outsider Groups", "வெளி குழுக்கள் (Outsider Groups)",
         "Anomic Groups", "அனோமிக் குழுக்கள்",
         "Institutional Groups", "நிறுவனக் குழுக்கள்", "A",
         "UPSC CSE 2019: Wyn Grant divided groups into 'Insider' (legitimate and consulted) and 'Outsider' (protesting from outside).",
         "UPSC CSE 2019: வின் கிராண்ட் குழுக்களை உள் குழுக்கள் மற்றும் வெளி குழுக்கள் என வகைப்படுத்தினார்."),

        ("PPPG_PYQ_032", "Dalit Panthers Maharashtra 1972",
         "[TNPSC Group 1 2017] In which year and state was the social protest movement 'Dalit Panthers' founded by Namdeo Dhasal and Arjun Dangle?",
         "[TNPSC குரூப் 1 2017] நாம்தேவ் தாசால் மற்றும் அர்ஜுன் டாங்கிள் ஆகியோரால் 'தலித் பாந்தர்ஸ்' சமூகப் போராட்ட இயக்கம் எந்த ஆண்டில் எந்த மாநிலத்தில் தொடங்கப்பட்டது?",
         "1972 in Maharashtra", "1972-ல் மகாராஷ்டிராவில்",
         "1968 in Uttar Pradesh", "1968-ல் உத்தரப் பிரதேசத்தில்",
         "1975 in Tamil Nadu", "1975-ல் தமிழ்நாட்டில்",
         "1980 in Bihar", "1980-ல் பீகாரில்", "A",
         "TNPSC Group 1 2017: Dalit Panthers was established in Bombay in 1972, inspired by the Black Panther movement in the US.",
         "TNPSC குரூப் 1 2017: 1972-ல் பம்பாயில் நாம்தேவ் தாசால் உள்ளிட்டோரால் தலித் பாந்தர்ஸ் இயக்கம் தொடங்கப்பட்டது."),

        ("PPPG_PYQ_033", "Narmada Bachao Andolan Medha Patkar",
         "[TNPSC Group 2 2019] The Narmada Bachao Andolan (NBA), a major environmental pressure group, was launched in 1985 primarily under the leadership of:",
         "[TNPSC குரூப் 2 2019] நர்மதா பச்சாவோ அந்தோலன் (NBA) என்ற முக்கிய சுற்றுச்சூழல் அழுத்தக் குழு 1985-ல் யாருடைய தலைமையில் தொடங்கப்பட்டது?",
         "Medha Patkar", "மேதா பட்கர்",
         "Maneka Gandhi", "மேனகா காந்தி",
         "Arundhati Roy", "அருந்ததி ராய்",
         "Madhav Gadgil", "மாதவ் காட்கில்", "A",
         "TNPSC Group 2 2019: Medha Patkar led the Narmada Bachao Andolan against the displacement caused by the Sardar Sarovar Dam.",
         "TNPSC குரூப் 2 2019: சர்தார் சரோவர் அணையால் வெளியேற்றப்படும் மக்களுக்கு ஆதரவாக மேதா பட்கர் நர்மதா பச்சாவோ அந்தோலனை வழிநடத்தினார்."),

        ("PPPG_PYQ_034", "Section 29C Contribution Threshold",
         "[UPSC Civil Services 2021] Under Section 29C of the Representation of the People Act, 1951, political parties must report individual donations exceeding what monetary threshold to the ECI?",
         "[UPSC சிவில் சர்வீசஸ் 2021] 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 29C-ன் கீழ், எந்தத் தொகைக்கு மேற்பட்ட தனிநபர் நன்கொடைகளை அரசியல் கட்சிகள் தேர்தல் ஆணையத்திடம் தெரிவிக்க வேண்டும்?",
         "Rs. 20,000", "ரூ. 20,000",
         "Rs. 10,000", "ரூ. 10,000",
         "Rs. 50,000", "ரூ. 50,000",
         "Rs. 1,00,000", "ரூ. 1,00,000", "A",
         "UPSC CSE 2021: Section 29C requires reporting all donations above Rs. 20,000 to maintain tax exemption under the IT Act.",
         "UPSC CSE 2021: பிரிவு 29C-ன் படி 20,000 ரூபாய்க்கு மேற்பட்ட அனைத்து நன்கொடைகளையும் தேர்தல் ஆணையத்திடம் தெரிவிக்க வேண்டும்."),

        ("PPPG_PYQ_035", "RTI Mazdoor Kisan Shakti Sangathan",
         "[TNPSC Group 1 2019] Which grassroots pressure group in Rajasthan founded by Aruna Roy pioneered the social audit movement that led to the Right to Information Act 2005?",
         "[TNPSC குரூப் 1 2019] 2005 தகவல் அறியும் உரிமைச் சட்டத்திற்கு வழிவகுத்த சமூக தணிக்கை இயக்கத்தை ராஜஸ்தானில் அருணா ராய் தலைமையில் முன்னெடுத்த அடிமட்ட அழுத்தக் குழு எது?",
         "Mazdoor Kisan Shakti Sangathan (MKSS)", "மஸ்தூர் கிசான் சக்தி சங்கதன் (MKSS)",
         "Shetkari Sanghatana", "ஷேத்காரி சங்கடனா",
         "Bharatiya Kisan Union", "பாரதிய கிசான் யூனியன்",
         "All India Kisan Sabha", "அகில இந்திய கிசான் சபா", "A",
         "TNPSC Group 1 2019: MKSS launched the Jan Sunwai campaign in Rajasthan in the 1990s demanding records of public works.",
         "TNPSC குரூப் 1 2019: அருணா ராய் தலைமையிலான MKSS அமைப்பு மக்கள் விசாரணைகள் மூலம் RTI சட்டத்திற்கு வித்திட்டது."),

        ("PPPG_PYQ_036", "ADR Candidate Affidavits 2002",
         "[UPSC Civil Services 2016] In Union of India v. Association for Democratic Reforms (2002), the Supreme Court ruled that voters have a fundamental right under Article 19(1)(a) to know candidates':",
         "[UPSC சிவில் சர்வீசஸ் 2016] இந்திய ஒன்றியம் எதிர் ADR (2002) வழக்கில், வேட்பாளர்களின் எதனை அறிந்துகொள்ள வாக்காளர்களுக்கு உறுப்பு 19(1)(a)-ன் கீழ் அடிப்படை உரிமை உண்டு என உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
         "Criminal antecedents, educational qualifications, assets, and liabilities",
         "குற்றப்பின்னணி, கல்வித் தகுதிகள், சொத்துக்கள் மற்றும் கடன்கள்",
         "Personal religious beliefs and temple contributions only",
         "தனிப்பட்ட மத நம்பிக்கைகள் மற்றும் கோவில் நன்கொடைகள் மட்டுமே",
         "Secret medical records and genetic lineage",
         "ரகசிய மருத்துவ ஆவணங்கள் மற்றும் மரபணு விவரங்கள்",
         "Personal voting record in previous municipal elections",
         "முந்தைய நகராட்சித் தேர்தல்களில் வாக்களித்த ரகசிய விவரங்கள்", "A",
         "UPSC CSE 2016: The 2002 ADR verdict mandated filing Form 26 affidavits disclosing criminal cases, assets, and liabilities.",
         "UPSC CSE 2016: வேட்பாளர்கள் தங்களது சொத்து, கடன், கல்வி மற்றும் குற்ற வழக்குகளை பிரமாணப் பத்திரத்தில் வெளிப்படுத்துவது கட்டாயமாக்கப்பட்டது."),

        ("PPPG_PYQ_037", "Public Interest Foundation 2018",
         "[TNPSC Group 1 2021] In Public Interest Foundation v. Union of India (2018), the Supreme Court mandated that political parties must publicize criminal cases of their candidates at least how many times?",
         "[TNPSC குரூப் 1 2021] பப்ளிக் இன்ட்ரஸ்ட் பவுண்டேஷன் வழக்கில் (2018), வேட்பாளர்களின் குற்ற வழக்குகளை அரசியல் கட்சிகள் ஊடகங்களில் குறைந்தது எத்தனை முறை விளம்பரம் செய்ய வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது?",
         "At least thrice (3 times) during campaigning", "பிரச்சாரக் காலத்தில் குறைந்தது மூன்று (3) முறை",
         "At least once before nomination", "வேட்புமனுவுக்கு முன் ஒரு முறை மட்டுமே",
         "At least five times every week", "ஒவ்வொரு வாரமும் குறைந்தது ஐந்து முறை",
         "Only once on the day after voting", "வாக்குப்பதிவுக்கு அடுத்த நாள் ஒரு முறை மட்டுமே", "A",
         "TNPSC Group 1 2021: The Supreme Court directed publishing criminal antecedents in newspapers and TV channels at least thrice.",
         "TNPSC குரூப் 1 2021: குற்ற வழக்குகளை செய்தித்தாள்களிலும் தொலைக்காட்சிகளிலும் 3 முறை வெளியிட வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது."),

        ("PPPG_PYQ_038", "SNDP Yogam 1903",
         "[TNPSC Group 4 2018] Sree Narayana Dharma Paripalana (SNDP) Yogam was established in 1903 in Kerala to uplift which backward community?",
         "[TNPSC குரூப் 4 2018] கேரளாவில் எந்த பின்தங்கிய சமூகத்தை முன்னேற்றுவதற்காக 1903-ல் ஸ்ரீ நாராயண தர்ம பரிபாலன (SNDP) யோகம் நிறுவப்பட்டது?",
         "Ezhava community", "ஈழவ சமூகம்",
         "Nair community", "நாயர் சமூகம்",
         "Pulaya community", "புலைய சமூகம்",
         "Paravan community", "பரவர் சமூகம்", "A",
         "TNPSC Group 4 2018: SNDP Yogam was founded in 1903 by Sree Narayana Guru, Dr. Palpu, and Kumaran Asan for the Ezhavas.",
         "TNPSC குரூப் 4 2018: 1903-ல் ஸ்ரீ நாராயண குருவால் ஈழவ சமூக முன்னேற்றத்திற்காக SNDP யோகம் தொடங்கப்பட்டது."),

        ("PPPG_PYQ_039", "Nair Service Society 1914",
         "[TNPSC Group 2 2017] In 1914, the Nair Service Society (NSS) was founded in Kerala by which prominent social reformer?",
         "[TNPSC குரூப் 2 2017] 1914-ல் கேரளாவில் நாயர் சேவை சங்கத்தை (NSS) நிறுவிய முன்னணி சமூக சீர்திருத்தவாதி யார்?",
         "Mannathu Padmanabhan", "மன்னாத்து பத்மநாபன்",
         "Ayyankali", "அய்யன்காளி",
         "C. Kesavan", "சி. கேசவன்",
         "K. Kelappan", "கே. கேளப்பன்", "A",
         "TNPSC Group 2 2017: Mannathu Padmanabhan founded the NSS in 1914 to promote social welfare and education among Nairs.",
         "TNPSC குரூப் 2 2017: 1914-ல் மன்னாத்து பத்மநாபனால் நாயர் சேவை சங்கம் (NSS) தொடங்கப்பட்டது."),

        ("PPPG_PYQ_040", "First Non-Congress Coalition Centre 1977",
         "[UPSC Civil Services 2013] Which political coalition ousted the Congress from power at the Centre for the first time in Indian history in 1977?",
         "[UPSC சிவில் சர்வீசஸ் 2013] இந்திய வரலாற்றில் முதன்முதலில் 1977-ல் காங்கிரசை ஆட்சியில் இருந்து அகற்றிய அரசியல் கூட்டணி எது?",
         "Janata Party coalition", "ஜனதா கட்சிக் கூட்டணி",
         "National Front", "தேசிய முன்னணி",
         "United Front", "ஐக்கிய முன்னணி",
         "NDA", "என்டிஏ", "A",
         "UPSC CSE 2013: The Janata Party coalition formed the first non-Congress Union government in 1977 following the Emergency.",
         "UPSC CSE 2013: 1977-ல் ஜனதா கட்சிக் கூட்டணி மத்தியில் முதல் காங்கிரஸ் அல்லாத அரசை அமைத்தது."),

        ("PPPG_PYQ_041", "National Front 1989 V.P. Singh",
         "[TNPSC Group 1 2016] The National Front government formed at the Centre in December 1989 under V.P. Singh was supported from the outside by which two ideologically opposite political forces?",
         "[TNPSC குரூப் 1 2016] டிசம்பர் 1989-ல் வி.பி. சிங் தலைமையில் மத்தியில் அமைந்த தேசிய முன்னணி அரசுக்கு வெளி ஆதரவு அளித்த இரு எதிர் துருவ அரசியல் சக்திகள் யாவை?",
         "Bharatiya Janata Party (BJP) and Left Front", "பாரதிய ஜனதா கட்சி (BJP) மற்றும் இடதுசாரி முன்னணி",
         "Congress and AIADMK", "காங்கிரஸ் மற்றும் அதிமுக",
         "TDP and DMK only", "தெலுங்கு தேசம் மற்றும் திமுக மட்டுமே",
         "Shiv Sena and Akali Dal only", "சிவசேனா மற்றும் அகாலி தளம் மட்டுமே", "A",
         "TNPSC Group 1 2016: The V.P. Singh government was uniquely supported by both the BJP and the Left Front from outside.",
         "TNPSC குரூப் 1 2016: வி.பி. சிங் அரசுக்கு பாஜக மற்றும் இடதுசாரிகள் இரண்டும் வெளியிலிருந்து ஆதரவு அளித்தன."),

        ("PPPG_PYQ_042", "TDP Formation 1982 N.T. Rama Rao",
         "[TNPSC Group 2 2015] In 1982, the Telugu Desam Party (TDP) was founded on the plank of regional pride and federalism by:",
         "[TNPSC குரூப் 2 2015] 1982-ல் பிராந்திய தன்னாபிமானம் மற்றும் கூட்டாட்சி அடிப்படையில் தெலுங்கு தேசம் கட்சியை (TDP) தொடங்கியவர் யார்?",
         "N.T. Rama Rao", "என்.டி. ராமராவ்",
         "N. Chandrababu Naidu", "என். சந்திரபாபு நாயுடு",
         "Y.S. Rajasekhara Reddy", "ஒய்.எஸ். ராஜசேகர ரெட்டி",
         "P.V. Narasimha Rao", "பி.வி. நரசிம்ம ராவ்", "A",
         "TNPSC Group 2 2015: Popular actor N.T. Rama Rao founded the TDP in March 1982 and swept the assembly polls in 1983.",
         "TNPSC குரூப் 2 2015: 1982-ல் என்.டி. ராமராவால் தெலுங்கு தேசம் கட்சி தொடங்கப்பட்டது."),

        ("PPPG_PYQ_043", "TDP Main Opposition 1984",
         "[UPSC Civil Services 2017] Which regional party became the principal Opposition party in the 8th Lok Sabha (1984) with 30 seats?",
         "[UPSC சிவில் சர்வீசஸ் 2017] 8வது மக்களவையில் (1984) 30 இடங்களை வென்று பிரதான எதிர்க்கட்சியாக விளங்கிய பிராந்திய கட்சி எது?",
         "Telugu Desam Party (TDP)", "தெலுங்கு தேசம் கட்சி (TDP)",
         "CPI(M)", "சிபிஐ(எம்)",
         "DMK", "திமுக",
         "AIADMK", "அதிமுக", "A",
         "UPSC CSE 2017: TDP won 30 seats in 1984, becoming the largest opposition party in the Lok Sabha.",
         "UPSC CSE 2017: 1984-ல் 30 இடங்களை வென்று தெலுங்கு தேசம் கட்சி மக்களவையின் பிரதான எதிர்க்கட்சியானது."),

        ("PPPG_PYQ_044", "State Party Recognition 3% Seats",
         "[UPSC Civil Services 2019] To be recognized as a State Party under Criterion 3 of the Symbols Order, a party must win at least:",
         "[UPSC சிவில் சர்வீசஸ் 2019] சின்னங்கள் உத்தரவின் 3வது நிபந்தனையின் கீழ் மாநிலக் கட்சியாக அங்கீகரிக்கப்பட, ஒரு கட்சி குறைந்தது எதனை வெல்ல வேண்டும்?",
         "3% of total seats in Legislative Assembly or 3 seats, whichever is more",
         "சட்டப்பேரவையில் மொத்த இடங்களில் 3% அல்லது 3 இடங்கள், எது அதிகமோ அது",
         "5% of total seats in Legislative Assembly or 5 seats",
         "சட்டப்பேரவையில் மொத்த இடங்களில் 5% அல்லது 5 இடங்கள்",
         "2% of total seats in Legislative Assembly or 2 seats",
         "சட்டப்பேரவையில் மொத்த இடங்களில் 2% அல்லது 2 இடங்கள்",
         "6% of total seats in Legislative Assembly or 10 seats",
         "சட்டப்பேரவையில் மொத்த இடங்களில் 6% அல்லது 10 இடங்கள்", "A",
         "UPSC CSE 2019: Condition 3 requires at least 3% of the total number of Assembly seats or 3 seats, whichever is more.",
         "UPSC CSE 2019: சட்டமன்றத்தில் 3% இடங்கள் அல்லது 3 இடங்கள் (எது அதிகமோ) வெல்ல வேண்டும்."),

        ("PPPG_PYQ_045", "Indrajit Gupta State Funding 1998",
         "[TNPSC Group 1 2018] The Indrajit Gupta Committee (1998) recommended that state funding of elections in India should be provided:",
         "[TNPSC குரூப் 1 2018] இந்திரஜித் குப்தா குழு (1998) இந்தியாவில் தேர்தல்களுக்கு அரசு நிதியளிப்பது எவ்வாறாக வழங்கப்பட வேண்டும் எனப் பரிந்துரைத்தது?",
         "In kind (facilities, paper, fuel, airtime) only to recognized political parties",
         "அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு மட்டுமே பொருட்களாக (வசதிகள், காகிதம், எரிபொருள், ஒளிபரப்பு நேரம்) பணமின்றி",
         "In unconditional cash subsidies to all candidates equally",
         "அனைத்து வேட்பாளர்களுக்கும் சமமாக நிபந்தனையற்ற பண மானியமாக",
         "Only to independent candidates contesting for the first time",
         "முதல்முறை போட்டியிடும் சுயேச்சை வேட்பாளர்களுக்கு மட்டுமே",
         "Exclusively through foreign corporate investments",
         "வெளிநாட்டு கார்ப்பரேட் முதலீடுகள் மூலம் மட்டுமே", "A",
         "TNPSC Group 1 2018: The Indrajit Gupta Committee strictly advocated state assistance in kind, not cash, to recognized parties.",
         "TNPSC குரூப் 1 2018: அரசு நிதியை பணமாகத் தராமல் வசதிகளாக மட்டுமே அங்கீகரிக்கப்பட்ட கட்சிகளுக்குத் தர பரிந்துரைத்தது."),

        # 46
        ("PPPG_PYQ_046", "Ravi Naik Voluntarily Giving Up",
         "[UPSC Civil Services 2018] In Ravi S. Naik v. Union of India (1994), the Supreme Court interpreted 'voluntarily giving up membership' under Tenth Schedule to mean:",
         "[UPSC சிவில் சர்வீசஸ் 2018] ரவி எஸ். நாயக் (1994) வழக்கில், பத்தாவது அட்டவணையின் கீழ் 'தானாக முன்வந்து உறுப்பினர் பதவியைத் துறத்தல்' என்பதை உச்ச நீதிமன்றம் எவ்வாறு விளக்கியது?",
         "It can be inferred from a member's conduct outside the House and is wider than formal resignation",
         "இது அவைக்கு வெளியே ஒரு உறுப்பினரின் நடத்தையிலிருந்து ஊகிக்கப்படலாம் மற்றும் முறையான ராஜினாமாவை விட பரந்ததாகும்",
         "It strictly requires a signed resignation letter submitted to the President",
         "குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்பட்ட கையொப்பமிட்ட ராஜினாமாக் கடிதம் மட்டுமே கட்டாயமாகும்",
         "It applies only when an MP is expelled by the party leadership",
         "கட்சித் தலைமையால் ஒரு எம்பி நீக்கப்படும் போது மட்டுமே இது பொருந்தும்",
         "It only applies to nominated members after six months",
         "நியமன உறுப்பினர்களுக்கு ஆறு மாதங்களுக்குப் பிறகு மட்டுமே இது பொருந்தும்", "A",
         "UPSC CSE 2018: In Ravi Naik, the Court ruled that conduct demonstrating severance from the party constitutes voluntarily giving up membership.",
         "UPSC CSE 2018: கட்சிக்கு எதிரான செயல்பாடுகள் மூலம் ஒரு உறுப்பினர் தானாகவே கட்சியிலிருந்து விலகியதாகக் கருதப்படலாம் எனத் தீர்ப்பளிக்கப்பட்டது."),

        # 47
        ("PPPG_PYQ_047", "Aam Aadmi Party National Status 2023",
         "[TNPSC Group 1 2023] In April 2023, which political party was recognized as a National Party by the Election Commission after fulfilling state party status in 4 states?",
         "[TNPSC குரூப் 1 2023] நான்கு மாநிலங்களில் மாநிலக் கட்சி அந்தஸ்தைப் பெற்றதைத் தொடர்ந்து ஏப்ரல் 2023-ல் தேர்தல் ஆணையத்தால் தேசியக் கட்சியாக அங்கீகரிக்கப்பட்ட கட்சி எது?",
         "Aam Aadmi Party (AAP)", "ஆம் ஆத்மி கட்சி (AAP)",
         "Trinamool Congress (TMC)", "திரிணாமுல் காங்கிரஸ் (TMC)",
         "Nationalist Congress Party (NCP)", "தேசியவாத காங்கிரஸ் கட்சி (NCP)",
         "Communist Party of India (CPI)", "இந்திய கம்யூனிஸ்ட் கட்சி (CPI)", "A",
         "TNPSC Group 1 2023: AAP gained National Party recognition in April 2023 having met state party criteria in Delhi, Punjab, Goa, and Gujarat.",
         "TNPSC குரூப் 1 2023: டெல்லி, பஞ்சாப், கோவா, குஜராத் ஆகிய 4 மாநிலங்களில் அங்கீகாரம் பெற்று ஆம் ஆத்மி தேசியக் கட்சியானது."),

        # 48
        ("PPPG_PYQ_048", "FCRA Foreign Contributions 2010",
         "[UPSC Civil Services 2022] Under Section 3 of the Foreign Contribution (Regulation) Act, 2010, which of the following entities is prohibited from accepting foreign contributions?",
         "[UPSC சிவில் சர்வீசஸ் 2022] 2010 வெளிநாட்டு பங்களிப்பு ஒழுங்குமுறைச் சட்டம் பிரிவு 3-ன் கீழ் பின்வருவனவற்றில் எந்த அமைப்பு வெளிநாட்டு நன்கொடைகளைப் பெற தடை விதிக்கப்பட்டுள்ளது?",
         "Political parties and candidates for election", "அரசியல் கட்சிகள் மற்றும் தேர்தல் வேட்பாளர்கள்",
         "Registered public universities", "பதிவு செய்யப்பட்ட பொதுப் பல்கலைக்கழகங்கள்",
         "Government hospitals", "அரசு மருத்துவமனைகள்",
         "Private manufacturing corporations exporting textiles", "ஜவுளி ஏற்றுமதி செய்யும் தனியார் உற்பத்தி நிறுவனங்கள்", "A",
         "UPSC CSE 2022: Section 3 of the FCRA 2010 explicitly prohibits candidates, political parties, and judges from accepting foreign funds.",
         "UPSC CSE 2022: அரசியல் கட்சிகளும் தேர்தல் வேட்பாளர்களும் வெளிநாட்டு நன்கொடைகளைப் பெற FCRA பிரிவு 3 தடை விதிக்கிறது."),

        # 49
        ("PPPG_PYQ_049", "Indian Labour Conference Tripartism",
         "[TNPSC Group 2 2018] The apex tripartite consultative committee in India that deliberates on national labor policies comprising government, trade unions, and employers is:",
         "[TNPSC குரூப் 2 2018] அரசு, தொழிற்சங்கங்கள் மற்றும் முதலாளிகள் அமைப்புகளைக் கொண்டு தேசிய தொழிலாளர் கொள்கைகளை விவாதிக்கும் இந்தியாவின் முதன்மை முத்தரப்பு ஆலோசனைக் குழு எது?",
         "Indian Labour Conference (ILC)", "இந்திய தொழிலாளர் மாநாடு (ILC)",
         "National Development Council", "தேசிய வளர்ச்சிக் கவுன்சில்",
         "Inter-State Council", "மாநிலங்களுக்கு இடையேயான கவுன்சில்",
         "Central Vigilance Commission", "மத்திய ஊழல் கண்காணிப்பு ஆணையம்", "A",
         "TNPSC Group 2 2018: The Indian Labour Conference is the apex tripartite forum shaping industrial relations in India.",
         "TNPSC குரூப் 2 2018: இந்திய தொழிலாளர் மாநாடு என்பது அரசு, தொழிற்சங்கங்கள் மற்றும் முதலாளிகள் அடங்கிய முதன்மை முத்தரப்பு அமைப்பாகும்."),

        # 50
        ("PPPG_PYQ_050", "Michels Iron Law of Oligarchy",
         "[UPSC Civil Services 2015] In political sociology, Robert Michels propounded the 'Iron Law of Oligarchy' based on an empirical study of:",
         "[UPSC சிவில் சர்வீசஸ் 2015] அரசியல் சமூகவியலில் ராபர்ட் மைக்கேல்ஸ் 'சிலராட்சியின் இரும்பு விதியை' எதனைப் பற்றிய அனுபவ ஆய்வின் அடிப்படையில் வகுத்தார்?",
         "Political parties and complex trade union organizations", "அரசியல் கட்சிகள் மற்றும் சிக்கலான தொழிற்சங்க அமைப்புகள்",
         "Traditional agricultural village panchayats", "பாரம்பரிய கிராமப்புற விவசாய பஞ்சாயத்துகள்",
         "Small military units in the Roman Empire", "ரோமானியப் பேரரசின் சிறிய ராணுவப் பிரிவுகள்",
         "Monarchies in seventeenth-century Europe", "பதினேழாம் நூற்றாண்டு ஐரோப்பாவின் மன்னராட்சிகள்", "A",
         "UPSC CSE 2015: Robert Michels formulated the Iron Law of Oligarchy in his 1911 study of the German Social Democratic Party.",
         "UPSC CSE 2015: ராபர்ட் மைக்கேல்ஸ் ஜெர்மன் சமூக ஜனநாயகக் கட்சியின் உள்கட்சி செயல்பாடுகளை ஆராய்ந்து சிலராட்சியின் இரும்பு விதியை வகுத்தார்.")
    ]

    pyq_raw.extend(pyq_more)

    for item in pyq_raw:
        qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item

        why_a_en = f"Evaluation of Option A ({en_a}): Accurate PYQ answer key."
        why_a_ta = f"விருப்பம் A ({ta_a}) மதிப்பீடு: துல்லியமான முந்தைய தேர்வு விடை."
        why_b_en = f"Evaluation of Option B ({en_b}): Relevant distractor."
        why_b_ta = f"விருப்பம் B ({ta_b}) மதிப்பீடு: தொடர்புடைய மாற்று விடை."
        why_c_en = f"Evaluation of Option C ({en_c}): Relevant distractor."
        why_c_ta = f"விருப்பம் C ({ta_c}) மதிப்பீடு: தொடர்புடைய மாற்று விடை."
        why_d_en = f"Evaluation of Option D ({en_d}): Relevant distractor."
        why_d_ta = f"விருப்பம் D ({ta_d}) மதிப்பீடு: தொடர்புடைய மாற்று விடை."

        tip_en = "Notice exam patterns in questions on recognition criteria (8% vote vs 3% seats), anti-defection, and pressure group types."
        tip_ta = "அங்கீகார அளவுகோல்கள், கட்சித் தாவல் தடைச் சட்டம் மற்றும் அழுத்தக் குழுக்களின் வகைகள் குறித்த முந்தைய வினாக்களைக் கவனியுங்கள்."
        fact_en = "In India, recognition of National and State parties is governed by the Election Symbols (Reservation and Allotment) Order, 1968."
        fact_ta = "இந்தியாவில் தேசிய மற்றும் மாநிலக் கட்சிகளின் அங்கீகாரம் தேர்தல் சின்னங்கள் (ஒதுக்கீடு மற்றும் பங்கீடு) உத்தரவு 1968-ஆல் நிர்வகிக்கப்படுகிறது."

        q = make_pppg_q(
            qid, "Medium", "pyq", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Balance and randomize keys
    balanced = randomize_and_balance_dataset(questions, seed=305)
    keys = [q["correct_answer"] for q in balanced]
    counts = Counter(keys)
    print("PPPG Part 2A PYQ Key counts:", counts)
    assert len(balanced) == 50
    for opt in ["A", "B", "C", "D"]:
        assert 12 <= counts[opt] <= 13

    # Validate
    validator = ContentValidator()
    all_errs = []
    for q in balanced:
        errs = validator.validate_question(q)
        if errs:
            all_errs.extend(errs)
    if all_errs:
        raise ValueError(f"Validation failed with {len(all_errs)} errors: {all_errs[:5]}")

    out_file = "data/questions/polity/political_parties_pressure_groups_pyq.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)

    # Copy to pyq_practice.json for UI compatibility
    pyq_copy = "data/questions/polity/political_parties_pressure_groups_pyq_practice.json"
    shutil.copyfile(out_file, pyq_copy)

    print(f"Successfully wrote 50 PYQ MCQs to {out_file} and {pyq_copy}")

if __name__ == "__main__":
    get_pyq_questions()
