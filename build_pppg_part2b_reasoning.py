# -*- coding: utf-8 -*-
"""
Build 25 Reasoning (Assertion-Reason) MCQs for Political Parties & Pressure Groups (PPPG_R_001 to PPPG_R_025)
TNPSC Nova AI Content Engine
"""
import os
import json
import shutil
from collections import Counter
from political_parties_pressure_groups_mcq_helper import make_pppg_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_reasoning_questions():
    questions = []

    # Format: (num, subtopic, a_en, r_en, a_ta, r_ta, correct_key, exp_en, exp_ta)
    reasoning_data = [
        # 001
        ("001", "National Party Status",
         "A political party recognized as a State Party in four or more states is automatically recognized as a National Party across India.",
         "Recognition as a National Party grants the party the exclusive right to reserve its election symbol throughout the territory of India.",
         "நான்கு அல்லது அதற்கு மேற்பட்ட மாநிலங்களில் மாநிலக் கட்சியாக அங்கீகரிக்கப்பட்ட ஒரு கட்சி இந்தியா முழுவதும் தானாகவே தேசியக் கட்சியாக அங்கீகரிக்கப்படுகிறது.",
         "தேசியக் கட்சியாக அங்கீகரிக்கப்படுவது இந்தியா முழுவதும் தனது தேர்தல் சின்னத்தை பிரத்யேகமாக ஒதுக்கும் உரிமையை அக்கட்சிக்கு வழங்குகிறது.",
         "B",
         "Both (A) and (R) are true statements. However, (R) explains the consequence/privilege of being a national party, not the legal rationale why 4 states qualify it under Criterion 3.",
         "இரண்டு கூற்றுகளும் சரியானவை. ஆனால் (R) என்பது தேசியக் கட்சி அந்தஸ்தின் சலுகையைக் கூறுகிறதே தவிர, ஏன் 4 மாநிலங்கள் போதுமானது என்பதற்கான விளக்கம் அல்ல."),

        # 002
        ("002", "Pressure Groups vs Political Parties",
         "Pressure groups do not contest elections or seek direct capture of political office.",
         "Pressure groups are formed primarily to influence public policy, administrative decisions, and legislation from the outside in favor of their specific interests.",
         "அழுத்தக் குழுக்கள் தேர்தலில் போட்டியிடுவதில்லை அல்லது நேரடியாக அரசியல் பதவிகளைக் கைப்பற்ற முயற்சிப்பதில்லை.",
         "அழுத்தக் குழுக்கள் தங்களது குறிப்பிட்ட நலன்களுக்கு ஆதரவாக பொதுக் கொள்கைகள், நிர்வாக முடிவுகள் மற்றும் சட்டங்களில் வெளியில் இருந்து செல்வாக்கு செலுத்தவே உருவாக்கப்படுகின்றன.",
         "A",
         "Both (A) and (R) are true, and (R) correctly explains why pressure groups avoid contesting elections: their objective is policy influence rather than state governance.",
         "இரண்டும் சரியானவை, மேலும் (R) என்பது (A)-க்கான சரியான விளக்கமாகும்: அரசு ஆட்சியைப் பிடிப்பதை விட கொள்கை மாற்றமே அவற்றின் நோக்கம்."),

        # 003
        ("003", "Tenth Schedule Merger",
         "A member of a House shall not be disqualified under the Tenth Schedule where his original political party merges with another political party, if not less than two-thirds of the legislature party members agree to the merger.",
         "The 91st Constitutional Amendment Act, 2003 deleted the one-third split exception, making collective two-thirds merger the only statutory defense against defection.",
         "ஒரு சட்டமன்றக் கட்சியின் மூன்றில் இரண்டு பங்குக்கு குறையாத உறுப்பினர்கள் இணைப்பை ஏற்றுக்கொண்டால், தாய் அரசியல் கட்சி மற்றொரு கட்சியுடன் இணையும் போது பத்தாவது அட்டவணையின் கீழ் உறுப்பினர் தகுதிநீக்கம் செய்யப்பட மாட்டார்.",
         "2003-ஆம் ஆண்டின் 91வது அரசியலமைப்பு திருத்தச் சட்டம் மூன்றில் ஒரு பங்கு கட்சி பிளவு விதிவிலக்கை நீக்கி, மூன்றில் இரண்டு பங்கு இணைப்பை மட்டுமே கட்சித் தாவலுக்கு எதிரான பாதுகாப்பாக மாற்றியது.",
         "B",
         "Both (A) and (R) are correct constitutional facts, but (R) states the legislative history of the 91st Amendment rather than explaining why the 2/3rd merger threshold exists.",
         "இரண்டும் சரியான கூற்றுகள். (R) என்பது 91வது திருத்தத்தின் வரலாற்றைக் கூறுகிறதே தவிர, 2/3 இணைப்பு ஏன் அனுமதிக்கப்படுகிறது என்பதற்கான காரணமல்ல."),

        # 004
        ("004", "Electoral Bonds Unconstitutionality",
         "The Supreme Court in ADR v. Union of India (2024) struck down the Electoral Bond Scheme as unconstitutional.",
         "The scheme permitted unlimited anonymous corporate funding of political parties, violating the voter's fundamental right to information under Article 19(1)(a).",
         "ADR எதிர் இந்திய ஒன்றியம் (2024) வழக்கில் உச்ச நீதிமன்றம் தேர்தல் பத்திரத் திட்டத்தை அரசியலமைப்பிற்கு முரணானது என ரத்து செய்தது.",
         "இத்திட்டம் அரசியல் கட்சிகளுக்கு வரம்பற்ற பெயரற்ற கார்ப்பரேட் நிதியுதவியை அனுமதித்து, வாக்காளர்களின் உறுப்பு 19(1)(a) தகவல் அறியும் உரிமையை மீறியது.",
         "A",
         "Both (A) and (R) are true, and (R) is the exact constitutional ground upon which the Supreme Court based its verdict.",
         "இரண்டும் சரியானவை, மேலும் (R) என்பது (A)-க்கான நேரடி அரசியலமைப்பு விளக்கமாகும்."),

        # 005
        ("005", "Deregistration of Parties",
         "The Election Commission of India possesses unlimited statutory power under Section 29A of the RPA 1951 to cancel the registration of any political party at its discretion.",
         "Section 29A confers upon the Election Commission the quasi-judicial power to register associations as political parties.",
         "1951 மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 29A-ன் கீழ் எந்தவொரு அரசியல் கட்சியின் பதிவையும் தனது விருப்பப்படி ரத்து செய்ய இந்தியத் தேர்தல் ஆணையத்திற்கு வரம்பற்ற அதிகாரம் உள்ளது.",
         "பிரிவு 29A அரசியல் கட்சிகளாக சங்கங்களைப் பதிவு செய்வதற்கான பகுதி-நீதித்துறை அதிகாரத்தை தேர்தல் ஆணையத்திற்கு வழங்குகிறது.",
         "D",
         "(A) is false because in the 2002 Indian National Congress case, the Supreme Court held that the ECI has NO general power of deregistration. (R) is true.",
         "(A) தவறு, ஏனெனில் தேர்தல் ஆணையத்திற்கு கட்சிகளை ரத்து செய்யும் பொது அதிகாரம் இல்லை என உச்ச நீதிமன்றம் தீர்ப்பளித்துள்ளது. (R) சரியானது."),

        # 006
        ("006", "Model Code of Conduct Timing",
         "The Model Code of Conduct (MCC) comes into operation from the date of issuance of the statutory notification of elections by the President / Governor.",
         "The MCC derives its constitutional enforceability from the plenary superintendence powers of the Election Commission under Article 324.",
         "குடியரசுத் தலைவர் / ஆளுநரால் தேர்தலுக்கான சட்டப்பூர்வ அறிவிக்கை வெளியிடப்படும் தேதியிலிருந்தே மாதிரி நடத்தை விதிகள் (MCC) அமலுக்கு வருகின்றன.",
         "அரசியலமைப்பின் உறுப்பு 324-ன் கீழ் தேர்தல் ஆணையத்திற்கு உள்ள முழுமையான கண்காணிப்பு அதிகாரத்திலிருந்து மாதிரி நடத்தை விதிகள் தங்களது அமலாக்க வலிமையைப் பெறுகின்றன.",
         "D",
         "(A) is false because the MCC comes into force immediately when the Election Commission announces the poll schedule in a press conference, NOT when the formal notification is issued. (R) is true.",
         "(A) தவறு, ஏனெனில் தேர்தல் ஆணையம் தேர்தல் தேதியை செய்தியாளர் சந்திப்பில் அறிவித்த உடனேயே நடத்தை விதிகள் அமலுக்கு வந்துவிடுகின்றன. (R) சரியானது."),

        # 007
        ("007", "Speaker as Tribunal",
         "The decision of the Speaker disqualifying a member under the Tenth Schedule is subject to judicial review by the High Courts and Supreme Court.",
         "While adjudicating disqualification petitions under the Tenth Schedule, the Speaker acts as a Tribunal exercising quasi-judicial authority.",
         "பத்தாவது அட்டவணையின் கீழ் ஒரு உறுப்பினரை சபாநாயகர் தகுதிநீக்கம் செய்யும் முடிவு உயர் நீதிமன்றங்கள் மற்றும் உச்ச நீதிமன்றத்தின் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.",
         "பத்தாவது அட்டவணையின் கீழ் தகுதிநீக்க மனுக்களை விசாரிக்கும் போது, சபாநாயகர் பகுதி-நீதித்துறை அதிகாரம் கொண்ட ஒரு தீர்ப்பாயமாகச் (Tribunal) செயல்படுகிறார்.",
         "A",
         "Both (A) and (R) are true, and (R) is the precise reason established in Kihoto Hollohan (1992) why the Speaker's decisions are open to judicial review.",
         "இரண்டும் சரியானவை, மேலும் சபாநாயகர் தீர்ப்பாயமாகச் செயல்படுவதாலேயே அவரது முடிவுகள் நீதித்துறை மறுஆய்வுக்கு உட்படுகின்றன; எனவே (R) என்பது (A)-க்கான சரியான விளக்கமாகும்."),

        # 008
        ("008", "Free Broadcast Time on Prasar Bharati",
         "Recognized political parties are provided free broadcasting and telecasting time on Doordarshan and All India Radio during general elections.",
         "Section 39A of the Representation of the People Act, 1951 statutorily mandates equitable sharing of time on state electronic media for recognized parties.",
         "பொதுத் தேர்தல்களின் போது அங்கீகரிக்கப்பட்ட அரசியல் கட்சிகளுக்கு தூர்தர்ஷன் மற்றும் அகில இந்திய வானொலியில் இலவச ஒளிபரப்பு நேரம் வழங்கப்படுகிறது.",
         "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 39A அரசு மின்னணு ஊடகங்களில் அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு சமமான நேரப் பகிர்வை சட்டப்பூர்வமாகக் கட்டாயமாக்குகிறது.",
         "A",
         "Both (A) and (R) are true, and Section 39A of RPA 1951 is the direct statutory authority providing this facility.",
         "இரண்டும் சரியானவை, மேலும் மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 39A என்பது இதற்கான நேரடி சட்டப்பூர்வ ஆதாரமாகும்."),

        # 009
        ("009", "Section 123(3) Religious Appeals",
         "Appealing for votes in the name of religion, race, caste, community, or language constitutes a corrupt electoral practice under Indian law.",
         "Under Section 100(1)(b) of the Representation of the People Act, 1951, proving the commission of a corrupt practice by a returned candidate results in the High Court declaring his election void.",
         "மதம், இனம், சாதி, சமூகம் அல்லது மொழியின் பெயரால் வாக்கு கேட்பது இந்திய சட்டத்தின் கீழ் தேர்தல் ஊழல் நடைமுறையாகும்.",
         "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 100(1)(b)-ன் கீழ், வெற்றி பெற்ற வேட்பாளர் ஊழல் நடைமுறையில் ஈடுபட்டது நிரூபிக்கப்பட்டால் அவரது வெற்றி செல்லாது என உயர் நீதிமன்றம் அறிவிக்கும்.",
         "B",
         "Both (A) and (R) are true statements of election law, but (R) states the penalty under Section 100 rather than explaining why religious appeals constitute a corrupt practice under Section 123(3).",
         "இரண்டும் சரியானவை. ஆனால் (R) என்பது பிரிவு 100-ன் கீழான தண்டனையைக் கூறுகிறதே தவிர, ஏன் பிரிவு 123(3) கீழ் மதம் சார்ந்த முறையீடு ஊழலாகிறது என்பதற்கான விளக்கம் அல்ல."),

        # 010
        ("010", "Subhash Desai 2023 Ruling",
         "A faction of legislators commanding a majority within the Legislature Party can validly appoint a new Whip without the authorization of the Political Party.",
         "The Tenth Schedule expressly equates the Legislature Party with the Political Party, extinguishing the supremacy of the political party's organizational wing.",
         "சட்டமன்றக் கட்சிக்குள் பெரும்பான்மை பலம் கொண்ட ஒரு குழு, தாய் அரசியல் கட்சியின் அனுமதியின்றி புதிய விப்பை சட்டப்பூர்வமாக நியமிக்க முடியும்.",
         "பத்தாவது அட்டவணை சட்டமன்றக் கட்சியை அரசியல் கட்சியுடன் வெளிப்படையாக சமப்படுத்துகிறது, மற்றும் அரசியல் கட்சியின் நிறுவன மேலாதிக்கத்தை ஒழிக்கிறது.",
         "C",
         "Wait, both are FALSE! Let's check options for standard AR: if both are false, standard options don't fit! Let's make (A) true and (R) false for option C!",
         "In Subhash Desai (2023), the Supreme Court held that the Political Party, and not the Legislature Party, has the power to appoint the Whip.",
         "A faction of legislators cannot appoint a Whip without party authorization.",
         "A", # let's fix below
         "Correct", "சரி"),

        # Let's write all 25 with crystal-clear standard A, B, C, D distribution!
    ]

    # Clean standardized data with 25 distinct items:
    # A: Both true, R is correct explanation
    # B: Both true, R is NOT correct explanation
    # C: A is true, R is false
    # D: A is false, R is true
    # We will balance them evenly (6-7 of each)

    ar_items = [
        # AR 01 (Key: A)
        ("001", "Pressure Groups Nature",
         "Pressure groups do not contest elections or seek direct capture of political office.",
         "The primary objective of pressure groups is to influence governmental policy, legislation, and administrative decisions from the outside in favor of their sectional interests.",
         "அழுத்தக் குழுக்கள் தேர்தலில் போட்டியிடுவதில்லை அல்லது நேரடியாக அரசியல் பதவிகளைக் கைப்பற்ற முயற்சிப்பதில்லை.",
         "அரசாங்கக் கொள்கைகள், சட்டங்கள் மற்றும் நிர்வாக முடிவுகளில் வெளியில் இருந்து தங்களது பிரிவு நலன்களுக்கு ஆதரவாக செல்வாக்கு செலுத்துவதே அழுத்தக் குழுக்களின் முதன்மை நோக்கமாகும்.",
         "A",
         "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
         "இரண்டும் சரியானவை, மேலும் (R) என்பது (A)-க்கான சரியான விளக்கமாகும்."),

        # AR 02 (Key: A)
        ("002", "Electoral Bonds Unconstitutionality",
         "The Supreme Court in ADR v. Union of India (2024) struck down the Electoral Bond Scheme as unconstitutional.",
         "The scheme permitted unlimited anonymous funding of political parties, violating the voter's fundamental right to information under Article 19(1)(a).",
         "ADR எதிர் இந்திய ஒன்றியம் (2024) வழக்கில் உச்ச நீதிமன்றம் தேர்தல் பத்திரத் திட்டத்தை அரசியலமைப்பிற்கு முரணானது என ரத்து செய்தது.",
         "இத்திட்டம் அரசியல் கட்சிகளுக்கு வரம்பற்ற பெயரற்ற நிதியுதவியை அனுமதித்து, வாக்காளர்களின் உறுப்பு 19(1)(a) தகவல் அறியும் உரிமையை மீறியது.",
         "A",
         "Both (A) and (R) are true, and (R) correctly explains why the scheme was held unconstitutional.",
         "இரண்டும் சரியானவை, மேலும் (R) என்பது (A)-க்கான சரியான விளக்கமாகும்."),

        # AR 03 (Key: A)
        ("003", "Speaker as Tribunal",
         "The orders of the Speaker under the Tenth Schedule are subject to judicial review by High Courts and the Supreme Court.",
         "While deciding disqualification petitions under the Tenth Schedule, the Speaker functions as a Tribunal exercising quasi-judicial powers.",
         "பத்தாவது அட்டவணையின் கீழ் சபாநாயகர் பிறப்பிக்கும் உத்தரவுகள் உயர் நீதிமன்றங்கள் மற்றும் உச்ச நீதிமன்றத்தின் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை.",
         "பத்தாவது அட்டவணையின் கீழ் தகுதிநீக்க மனுக்களை விசாரிக்கும் போது, சபாநாயகர் பகுதி-நீதித்துறை அதிகாரம் கொண்ட ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார்.",
         "A",
         "Both (A) and (R) are true, and (R) is the correct explanation of (A) as laid down in Kihoto Hollohan (1992).",
         "இரண்டும் சரியானவை, மேலும் (R) என்பது (A)-க்கான சரியான விளக்கமாகும்."),

        # AR 04 (Key: A)
        ("004", "RTI Grassroots Movement",
         "The Mazdoor Kisan Shakti Sangathan (MKSS) spearheaded the public hearing movement (Jan Sunwai) in rural Rajasthan in the 1990s.",
         "MKSS demanded access to village employment muster rolls and expenditure records to expose local corruption in drought relief works.",
         "மஸ்தூர் கிசான் சக்தி சங்கதன் (MKSS) 1990-களில் கிராமப்புற ராஜஸ்தானில் மக்கள் விசாரணை இயக்கத்தை (Jan Sunwai) முன்னெடுத்தது.",
         "வறட்சி நிவாரணப் பணிகளில் நடந்த உள்ளூர் ஊழலை அம்பலப்படுத்த கிராமப்புற வேலைவாய்ப்பு வருகைப் பதிவேடுகள் மற்றும் செலவு ஆவணங்களைப் பார்க்க MKSS கோரியது.",
         "A",
         "Both (A) and (R) are true, and (R) correctly explains why MKSS initiated the Jan Sunwai movement.",
         "இரண்டும் சரியானவை, மேலும் (R) என்பது (A)-க்கான சரியான விளக்கமாகும்."),

        # AR 05 (Key: A)
        ("005", "Section 39A Media Access",
         "Recognized political parties are entitled to equitable free broadcasting and telecasting time on state-owned media during general elections.",
         "Section 39A of the Representation of the People Act, 1951 statutorily mandates allocation of equitable time on Doordarshan and All India Radio to recognized parties.",
         "பொதுத் தேர்தல்களின் போது அங்கீகரிக்கப்பட்ட அரசியல் கட்சிகளுக்கு அரசு ஊடகங்களில் இலவச ஒளிபரப்பு நேரம் சமமாக வழங்கப்படுகிறது.",
         "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 39A தூர்தர்ஷன் மற்றும் வானொலியில் அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு இலவச நேரப் பகிர்வை சட்டப்பூர்வமாகக் கட்டாயமாக்குகிறது.",
         "A",
         "Both (A) and (R) are true, and (R) is the correct statutory basis and explanation of (A).",
         "இரண்டும் சரியானவை, மேலும் (R) என்பது (A)-க்கான சரியான விளக்கமாகும்."),

        # AR 06 (Key: A)
        ("006", "Duverger's Law Mechanism",
         "Single-member district simple-majority electoral systems (FPTP) tend to produce a two-party system over time.",
         "Under FPTP, voters engage in strategic voting to avoid wasting votes on third-party candidates who have little chance of winning a plurality.",
         "ஒற்றை உறுப்பினர் எளிய பெரும்பான்மை தேர்தல் முறை (FPTP) காலப்போக்கில் இரு கட்சி ஆட்சி முறைக்கு வழிவகுக்கிறது.",
         "FPTP முறையின் கீழ், வெற்றி பெற வாய்ப்பில்லாத மூன்றாவது கட்சி வேட்பாளர்களுக்கு வாக்களித்து வாக்குகளை வீணடிப்பதைத் தவிர்க்க வாக்காளர்கள் உத்திசார் வாக்குகளைப் பயன்படுத்துகின்றனர்.",
         "A",
         "Both (A) and (R) are true, and (R) is the psychological factor explaining Duverger's Law.",
         "இரண்டும் சரியானவை, மேலும் (R) என்பது டுவெர்ஜரின் விதியை விளக்கும் சரியான காரணியாகும்."),

        # AR 07 (Key: B)
        ("007", "National Party Criteria",
         "A political party recognized as a State Party in four or more states is recognized as a National Party across India.",
         "A recognized National Party enjoys the exclusive reservation of its symbol across all States and Union Territories in India.",
         "நான்கு அல்லது அதற்கு மேற்பட்ட மாநிலங்களில் மாநிலக் கட்சியாக அங்கீகரிக்கப்பட்ட ஒரு கட்சி இந்தியா முழுவதும் தானாகவே தேசியக் கட்சியாக அங்கீகரிக்கப்படுகிறது.",
         "அங்கீகரிக்கப்பட்ட ஒரு தேசியக் கட்சி இந்தியாவின் அனைத்து மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களிலும் தனது சின்னத்தை பிரத்யேகமாக ஒதுக்கும் சலுகையை அனுபவிக்கிறது.",
         "B",
         "Both (A) and (R) are true, but (R) describes a privilege of national party status, not the legal explanation of Criterion 3.",
         "இரண்டும் சரியானவை, ஆனால் (R) என்பது தேசியக் கட்சி அந்தஸ்தின் சலுகையைக் கூறுகிறதே தவிர, (A)-க்கான விளக்கம் அல்ல."),

        # AR 08 (Key: B)
        ("008", "91st Amendment Capping",
         "The total number of Ministers including the Prime Minister in the Union Council of Ministers cannot exceed 15% of the total strength of the Lok Sabha.",
         "The 91st Constitutional Amendment Act, 2003 omitted Paragraph 3 of the Tenth Schedule to prevent defections disguised as splits.",
         "மத்திய அமைச்சரவையில் பிரதமர் உட்பட மொத்த அமைச்சர்களின் எண்ணிக்கை மக்களவையின் மொத்த பலத்தில் 15%-க்கு மிகாமல் இருக்க வேண்டும்.",
         "2003-ஆம் ஆண்டின் 91வது அரசியலமைப்பு திருத்தச் சட்டம் கட்சி பிளவு என்ற பெயரிலான கட்சித் தாவல்களைத் தடுக்க பத்தாவது அட்டவணையின் பத்தி 3-ஐ நீக்கியது.",
         "B",
         "Both (A) and (R) are correct constitutional facts enacted by the 91st Amendment, but (R) does not explain the 15% cabinet cap.",
         "இரண்டும் சரியானவை, ஆனால் (R) என்பது (A)-க்கான விளக்கம் அல்ல; இரண்டும் 91வது திருத்தத்தின் தனித்தனி ஏற்பாடுகள்."),

        # AR 09 (Key: B)
        ("009", "ASSOCHAM and FICCI",
         "ASSOCHAM is the oldest national apex business chamber in India, having been established in 1920.",
         "FICCI was established in 1927 by G.D. Birla and Purshottamdas Thakurdas on the advice of Mahatma Gandhi.",
         "1920-ல் நிறுவப்பட்ட ASSOCHAM இந்தியாவின் மிக மூத்த தேசிய முதன்மை வணிக அமைப்பாகும்.",
         "மகாத்மா காந்தியின் ஆலோசனையின் பேரில் ஜி.டி. பிர்லா மற்றும் புருஷோத்தம்தாஸ் தாக்குர்தாஸ் ஆகியோரால் 1927-ல் FICCI தொடங்கப்பட்டது.",
         "B",
         "Both (A) and (R) are true historical facts, but (R) concerns FICCI and does not explain ASSOCHAM's founding.",
         "இரண்டும் சரியான வரலாற்று உண்மைகள், ஆனால் (R) என்பது (A)-க்கான விளக்கம் அல்ல."),

        # AR 10 (Key: B)
        ("010", "Section 123 Corrupt Practice",
         "An appeal to vote or refrain from voting on the ground of religion, race, caste, community, or language is a corrupt practice under Section 123(3) of RPA 1951.",
         "Under Section 100(1)(b) of RPA 1951, the High Court can declare an election void if a corrupt practice has been committed by the returned candidate.",
         "மதம், இனம், சாதி, சமூகம் அல்லது மொழியின் பெயரால் வாக்கு கேட்பது மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 123(3)-ன் கீழ் ஊழல் நடைமுறையாகும்.",
         "மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 100(1)(b)-ன் கீழ் வெற்றி பெற்ற வேட்பாளர் ஊழல் நடைமுறையில் ஈடுபட்டது நிரூபிக்கப்பட்டால் உயர் நீதிமன்றம் அவரது வெற்றியை செல்லாது என அறிவிக்கலாம்.",
         "B",
         "Both (A) and (R) are true legal provisions, but (R) states the consequence of corrupt practices under Section 100 rather than explaining why Section 123(3) bars religious appeals.",
         "இரண்டும் சரியானவை, ஆனால் (R) என்பது (A)-க்கான விளக்கம் அல்ல; அது தண்டனை விதியைக் கூறுகிறது."),

        # AR 11 (Key: B)
        ("011", "Anti-Defection Merger Rule",
         "Under Paragraph 4 of the Tenth Schedule, a merger is recognized only if at least two-thirds of the legislature party members agree to it.",
         "Defection undermines representative democracy by subverting the electoral mandate given by the voters to a political party.",
         "பத்தாவது அட்டவணையின் பத்தி 4-ன் கீழ், சட்டமன்றக் கட்சியின் குறைந்தது மூன்றில் இரண்டு பங்கு உறுப்பினர்கள் ஒப்புக்கொண்டால் மட்டுமே இணைப்பு ஏற்றுக்கொள்ளப்படும்.",
         "வாக்காளர்கள் ஒரு அரசியல் கட்சிக்கு அளித்த தேர்தல் ஆணையை சீர்குலைப்பதன் மூலம் கட்சித் தாவல் பிரதிநிதித்துவ ஜனநாயகத்தை பலவீனப்படுத்துகிறது.",
         "B",
         "Both (A) and (R) are true statements, but (R) provides the general rationale against defection, not the mathematical explanation of the 2/3rd merger rule.",
         "இரண்டும் சரியானவை, ஆனால் (R) என்பது (A)-க்கான விளக்கம் அல்ல."),

        # AR 12 (Key: B)
        ("012", "Electoral Trust Scheme",
         "Under the Electoral Trusts Scheme 2013, an electoral trust must distribute at least 95% of contributions received to registered political parties.",
         "An Electoral Trust must be registered as a non-profit company under Section 8 of the Companies Act, 2013.",
         "2013 தேர்தல் அறக்கட்டளைகள் திட்டத்தின் கீழ், ஒரு தேர்தல் அறக்கட்டளை தனக்கு வந்த நன்கொடைகளில் குறைந்தது 95% தொகையை பதிவு செய்யப்பட்ட கட்சிகளுக்குப் பகிர்ந்தளிக்க வேண்டும்.",
         "தேர்தல் அறக்கட்டளை என்பது நிறுவனங்கள் சட்டம் 2013-ன் பிரிவு 8-ன் கீழ் அமைக்கப்பட்ட ஒரு லாப நோக்கற்ற நிறுவனமாக பதிவு செய்யப்பட வேண்டும்.",
         "B",
         "Both (A) and (R) are true legal features of the Electoral Trusts Scheme, but (R) is structural while (A) is financial distribution, so (R) does not explain (A).",
         "இரண்டும் சரியானவை, ஆனால் (R) என்பது (A)-க்கான விளக்கம் அல்ல."),

        # AR 13 (Key: C)
        ("013", "Subhash Desai Whip Authority",
         "In Subhash Desai (2023), the Supreme Court ruled that the power to appoint the legislative whip and leader vests in the Political Party.",
         "The Supreme Court held that the Legislature Party is completely sovereign and can appoint its own Whip independently of the Political Party.",
         "சுபாஷ் தேசாய் (2023) வழக்கில், சட்டமன்ற விப் மற்றும் தலைவரை நியமிக்கும் அதிகாரம் அரசியல் கட்சியிடமே உள்ளது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         "சட்டமன்றக் கட்சி முழு இறையாண்மை கொண்டது மற்றும் அரசியல் கட்சியைக் கலந்தாலோசிக்காமல் தன்னிச்சையாக விப்பை நியமிக்க முடியும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         "C",
         "(A) is true, but (R) is completely false as the Supreme Court explicitly rejected the autonomy of the legislature party.",
         "(A) சரியானது, ஆனால் (R) முற்றிலும் தவறானது."),

        # AR 14 (Key: C)
        ("014", "Section 29C Disclosure Mandate",
         "Political parties must report all contributions exceeding Rs. 20,000 received from individuals and companies to the Election Commission of India.",
         "Political parties that fail to submit their contribution report under Section 29C are immediately deregistered and banned from future elections.",
         "தனிநபர்கள் மற்றும் நிறுவனங்களிடமிருந்து பெறப்பட்ட 20,000 ரூபாய்க்கு மேற்பட்ட அனைத்து நன்கொடைகளையும் கட்சிகள் தேர்தல் ஆணையத்திடம் தெரிவிக்க வேண்டும்.",
         "பிரிவு 29C-ன் கீழ் பங்களிப்பு அறிக்கையை சமர்ப்பிக்கத் தவறும் அரசியல் கட்சிகள் உடனடியாக ரத்து செய்யப்பட்டு எதிர்காலத் தேர்தல்களில் போட்டியிடத் தடை செய்யப்படுகின்றன.",
         "C",
         "(A) is true under Section 29C of RPA 1951. (R) is false because failure results in loss of income tax exemption under Section 13A, NOT deregistration.",
         "(A) சரியானது, ஆனால் (R) தவறானது; அறிக்கை தராவிட்டால் வரி விலக்கு மட்டுமே பறிபோகும், கட்சி ரத்து செய்யப்படாது."),

        # AR 15 (Key: C)
        ("015", "Keisham Manipur 3 Months",
         "In Keisham Meghachandra Singh (2020), the Supreme Court held that the Speaker should decide Tenth Schedule disqualification petitions within three months.",
         "The Supreme Court held that the Speaker's delay in deciding disqualification petitions is completely immune from judicial review under Article 212.",
         "கீஷம் மேகசந்திர சிங் (2020) வழக்கில், சபாநாயகர் கட்சித் தாவல் மனுக்கள் மீது மூன்று மாதங்களுக்குள் முடிவெடுக்க வேண்டும் என உச்ச நீதிமன்றம் கூறியது.",
         "தகுதிநீக்க மனுக்கள் மீது முடிவெடுக்க சபாநாயகர் செய்யும் காலதாமதம் உறுப்பு 212-ன் கீழ் நீதிமன்ற மறுஆய்விலிருந்து முற்றிலும் விடுபட்டது என உச்ச நீதிமன்றம் கூறியது.",
         "C",
         "(A) is true. (R) is false because the Supreme Court held that inordinate delay by the Speaker is justiciable.",
         "(A) சரியானது, ஆனால் (R) தவறானது; சபாநாயகரின் தேவையற்ற காலதாமதத்தை நீதிமன்றங்கள் கேள்வி கேட்க முடியும்."),

        # AR 16 (Key: C)
        ("016", "NOTA Legal Effect",
         "The Supreme Court directed the introduction of the 'None of the Above' (NOTA) option on electronic voting machines in PUCL (2013).",
         "Under Indian election law, if NOTA secures the highest number of votes in a constituency, the election is legally cancelled and a re-poll is conducted with fresh candidates.",
         "PUCL (2013) வழக்கில் வாக்குப்பதிவு இயந்திரங்களில் 'நோட்டா' (NOTA) தேர்வை அறிமுகப்படுத்த உச்ச நீதிமன்றம் உத்தரவிட்டது.",
         "இந்திய தேர்தல் சட்டத்தின்படி ஒரு தொகுதியில் நோட்டா அதிக வாக்குகளைப் பெற்றால், அந்தத் தேர்தல் சட்டப்படி ரத்து செய்யப்பட்டு புதிய வேட்பாளர்களுடன் மறுதேர்தல் நடத்தப்படும்.",
         "C",
         "(A) is true. (R) is false because under the first-past-the-post rules, the candidate with the next highest votes is declared winner even if NOTA is higher.",
         "(A) சரியானது, ஆனால் (R) தவறானது; நோட்டா முதலிடம் பிடித்தாலும் அடுத்த அதிக வாக்கு பெற்ற வேட்பாளரே வெற்றி பெறுவார்."),

        # AR 17 (Key: C)
        ("017", "Candidate Criminal Disclosure",
         "In Public Interest Foundation (2018), the Supreme Court directed candidates and political parties to publish pending criminal cases in newspapers and TV channels thrice.",
         "Under current law, any candidate against whom a criminal FIR has been registered is automatically disqualified from contesting parliamentary elections.",
         "பப்ளிக் இன்ட்ரஸ்ட் பவுண்டேஷன் (2018) வழக்கில், வேட்பாளர்களின் குற்ற வழக்குகளை ஊடகங்களில் 3 முறை விளம்பரம் செய்ய வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது.",
         "தற்போதைய சட்டப்படி குற்றவியல் எஃப்.ஐ.ஆர் பதிவு செய்யப்பட்டுள்ள எந்தவொரு வேட்பாளரும் தானாகவே நாடாளுமன்றத் தேர்தலில் போட்டியிட தகுதிநீக்கம் செய்யப்படுகிறார்.",
         "C",
         "(A) is true. (R) is false because only conviction with a sentence of 2 years or more under Section 8 of RPA disqualifies a candidate, not mere registration of an FIR.",
         "(A) சரியானது, ஆனால் (R) தவறானது; 2 ஆண்டுகள் சிறைத் தண்டனை பெற்றால் மட்டுமே தகுதிநீக்கம் ஏற்படும், எஃப்.ஐ.ஆர்-ஆல் தகுதிநீக்கம் ஆகாது."),

        # AR 18 (Key: C)
        ("018", "Independent Member Tenth Schedule",
         "An independent member of a House stands disqualified under the Tenth Schedule if he joins any political party after election.",
         "An independent member is legally permitted to join a political party without penalty if he joins within six months of his election.",
         "சுயேச்சையாகத் தேர்ந்தெடுக்கப்பட்ட ஓர் உறுப்பினர் தேர்தலுக்குப் பிறகு ஏதேனும் அரசியல் கட்சியில் சேர்ந்தால் பத்தாவது அட்டவணையின் கீழ் தகுதிநீக்கம் செய்யப்படுவார்.",
         "சுயேச்சை உறுப்பினர் தேர்தலுக்குப் பிறகு ஆறு மாதங்களுக்குள் ஏதேனும் கட்சியில் சேர்ந்தால் அவர் மீது எந்த தகுதிநீக்க நடவடிக்கையும் எடுக்க முடியாது.",
         "C",
         "(A) is true under Paragraph 2(2) of the Tenth Schedule. (R) is false because the 6-month concession applies only to NOMINATED members under Paragraph 2(3), not independent members.",
         "(A) சரியானது, ஆனால் (R) தவறானது; 6 மாத சலுகை நியமன உறுப்பினர்களுக்கு மட்டுமே, சுயேச்சைகளுக்கு அல்ல."),

        # AR 19 (Key: D)
        ("019", "ECI Deregistration Powers",
         "The Election Commission of India possesses broad discretionary powers under Section 29A to cancel the registration of any political party that fails to win seats.",
         "The Supreme Court in Indian National Congress v. Institute of Social Welfare (2002) held that Section 29A does not confer general powers of deregistration upon the ECI.",
         "தேர்தலில் வெற்றி பெறத் தவறும் எந்தவொரு அரசியல் கட்சியின் பதிவையும் ரத்து செய்ய மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 29A-ன் கீழ் தேர்தல் ஆணையத்திற்கு வரம்பற்ற அதிகாரம் உண்டு.",
         "இந்திய தேசிய காங்கிரஸ் வழக்கில் (2002), அரசியல் கட்சிகளை ரத்து செய்யும் பொது அதிகாரம் பிரிவு 29A-ன் கீழ் தேர்தல் ஆணையத்திற்கு இல்லை என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         "D",
         "(A) is false because the ECI cannot deregister parties for electoral failure. (R) is true.",
         "(A) தவறு, ஆனால் (R) சரியானது."),

        # AR 20 (Key: D)
        ("020", "Model Code Notification Date",
         "The Model Code of Conduct comes into force on the date when the formal gazette notification for elections is issued by the Governor / President.",
         "The Model Code of Conduct comes into operation immediately from the moment the Election Commission announces the election schedule in a press conference.",
         "குடியரசுத் தலைவர் / ஆளுநரால் தேர்தலுக்கான அரசிதழ் அறிவிக்கை முறைப்படி வெளியிடப்படும் நாளிலிருந்தே மாதிரி நடத்தை விதிகள் அமலுக்கு வருகின்றன.",
         "தேர்தல் ஆணையம் பத்திரிகையாளர் சந்திப்பில் தேர்தல் அட்டவணையை அறிவிக்கும் அந்த தருணத்திலிருந்தே மாதிரி நடத்தை விதிகள் உடனடியாக அமலுக்கு வருகின்றன.",
         "D",
         "(A) is false. (R) is true as per established Supreme Court precedents and ECI guidelines.",
         "(A) தவறு, ஆனால் (R) சரியானது."),

        # AR 21 (Key: D)
        ("021", "FCRA Political Donations",
         "Under Indian law, registered political parties are free to accept foreign financial contributions from multinational foreign corporations without any restriction.",
         "Section 3 of the Foreign Contribution (Regulation) Act, 2010 strictly prohibits political parties and candidates for election from accepting any foreign contribution.",
         "இந்திய சட்டத்தின் கீழ் பதிவு செய்யப்பட்ட அரசியல் கட்சிகள் பன்னாட்டு வெளிநாட்டு நிறுவனங்களிடமிருந்து எந்தக் கட்டுப்பாடும் இன்றி நிதி நன்கொடைகளைப் பெறலாம்.",
         "2010 வெளிநாட்டு பங்களிப்பு ஒழுங்குமுறைச் சட்டம் (FCRA) பிரிவு 3 அரசியல் கட்சிகளும் தேர்தல் வேட்பாளர்களும் வெளிநாட்டு நன்கொடைகளைப் பெறுவதைக் கண்டிப்பாகத் தடைசெய்கிறது.",
         "D",
         "(A) is false because foreign political donations are barred. (R) is true.",
         "(A) தவறு, ஆனால் (R) சரியானது."),

        # AR 22 (Key: D)
        ("022", "Pressure Groups Electoral Nature",
         "Pressure groups in India seek to capture political power and form the government by fielding official candidates in general elections under reserved symbols.",
         "Political parties seek to capture government power through elections, whereas pressure groups seek to influence policy from the outside without holding office.",
         "இந்தியாவில் அழுத்தக் குழுக்கள் பொதுத் தேர்தல்களில் ஒதுக்கப்பட்ட சின்னங்களில் வேட்பாளர்களை நிறுத்தி அரசியல் அதிகாரத்தைக் கைப்பற்றி அரசாங்கத்தை அமைக்க முயல்கின்றன.",
         "அரசியல் கட்சிகள் தேர்தல்கள் மூலம் அரசாங்க அதிகாரத்தைக் கைப்பற்ற முயல்கின்றன, ஆனால் அழுத்தக் குழுக்கள் பதவிகளை ஏற்காமல் வெளியில் இருந்து கொள்கைகளில் செல்வாக்கு செலுத்த முயல்கின்றன.",
         "D",
         "(A) is false because pressure groups do not contest elections. (R) is true.",
         "(A) தவறு, ஆனால் (R) சரியானது."),

        # AR 23 (Key: D)
        ("023", "Cabinet Minimum Size",
         "The total number of Ministers including the Chief Minister in a State Legislative Assembly can be as low as five ministers.",
         "The proviso to Article 164(1A) of the Constitution mandates that the number of Ministers including the Chief Minister in a State shall not be less than twelve.",
         "ஒரு மாநில சட்டப்பேரவையில் முதலமைச்சர் உட்பட அமைச்சர்களின் மொத்த எண்ணிக்கை ஐந்து அமைச்சர்கள் வரை குறைவாக இருக்கலாம்.",
         "அரசியலமைப்பின் உறுப்பு 164(1A)-ன் நிபந்தனை, ஒரு மாநிலத்தில் முதலமைச்சர் உட்பட அமைச்சர்களின் எண்ணிக்கை 12-க்கு குறையாமல் இருக்க வேண்டும் என்று கட்டாயமாக்குகிறது.",
         "D",
         "(A) is false because the constitutional minimum is twelve. (R) is true.",
         "(A) தவறு, ஏனெனில் குறைந்தபட்ச எண்ணிக்கை 12 ஆகும். (R) சரியானது."),

        # AR 24 (Key: D)
        ("024", "National Party Seat Route",
         "Under the Lok Sabha seat route, a party can qualify as a National Party by winning 2% of total seats (11 seats) all from a single State.",
         "Criterion 2 of the Symbols Order mandates that the 2% Lok Sabha seats (11 seats) must be elected from not less than three different States.",
         "மக்களவை இடங்கள் வழியில், ஒரு கட்சி 2% இடங்களை (11 இடங்கள்) ஒரே ஒரு மாநிலத்திலிருந்து வென்றாலே தேசியக் கட்சியாக அங்கீகரிக்கப்படலாம்.",
         "சின்னங்கள் உத்தரவின் 2வது நிபந்தனை, அந்த 2% மக்களவை இடங்கள் (11 இடங்கள்) குறைந்தது மூன்று வெவ்வேறு மாநிலங்களிலிருந்து வெல்லப்பட வேண்டும் எனக் கட்டாயமாக்குகிறது.",
         "D",
         "(A) is false because winning from a single state does not qualify a party as National. (R) is true.",
         "(A) தவறு, ஏனெனில் குறைந்தது 3 வெவ்வேறு மாநிலங்கள் தேவை. (R) சரியானது."),

        # AR 25 (Key: D)
        ("025", "Mavalankar Opposition Rule",
         "Any registered political party with at least one member in Lok Sabha is entitled to claim the official status and perks of the Leader of the Opposition.",
         "Under the convention established by Speaker G.V. Mavalankar, an opposition party must possess at least 10% of the total strength of the House (55 seats) to be recognized as the Official Opposition.",
         "மக்களவையில் குறைந்தது ஒரு உறுப்பினரைக் கொண்ட எந்தவொரு பதிவு செய்யப்பட்ட கட்சியும் அதிகாரப்பூர்வ எதிர்க்கட்சித் தலைவர் அந்தஸ்தையும் சலுகைகளையும் கோரலாம்.",
         "சபாநாயகர் ஜி.வி. மாவலங்கர் நிறுவிய மரபின்படி, அதிகாரப்பூர்வ எதிர்க்கட்சியாக அங்கீகரிக்கப்பட ஒரு எதிர்க்கட்சி அவையின் மொத்த பலத்தில் குறைந்தது 10% (55 இடங்கள்) கொண்டிருக்க வேண்டும்.",
         "D",
         "(A) is false because single-member parties cannot claim the LoP post. (R) is true.",
         "(A) தவறு, ஆனால் (R) சரியானது.")
    ]

    for item in ar_items:
        qid_num, subtopic, a_en, r_en, a_ta, r_ta, correct_key, exp_en, exp_ta = item
        qid = f"PPPG_R_{qid_num}"

        en_stem = f"Given below are two statements, one labeled as Assertion (A) and the other labeled as Reason (R):\nAssertion (A): {a_en}\nReason (R): {r_en}\nIn the context of the statements above, which one of the following is correct?"
        ta_stem = f"கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): {a_ta}\nகாரணம் (R): {r_ta}\nமேற்கண்ட கூற்றுகளின் அடிப்படையில், பின்வருவனவற்றில் எது சரியானது?"

        en_a = "Both (A) and (R) are true and (R) is the correct explanation of (A)"
        ta_a = "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-க்கான சரியான விளக்கமாகும்"
        en_b = "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)"
        ta_b = "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-க்கான சரியான விளக்கம் அல்ல"
        en_c = "(A) is true but (R) is false"
        ta_c = "(A) உண்மை ஆனால் (R) பொய்"
        en_d = "(A) is false but (R) is true"
        ta_d = "(A) பொய் ஆனால் (R) உண்மை"

        why_a_en = "Option A evaluation: Both statements are true and causal linkage holds."
        why_a_ta = "ஆப்ஷன் A மதிப்பீடு: இரண்டு கூற்றுகளும் உண்மை மற்றும் காரண காரிய தொடர்பு பொருந்துகிறது."
        why_b_en = "Option B evaluation: Both statements are true but no direct explanatory link."
        why_b_ta = "ஆப்ஷன் B மதிப்பீடு: இரண்டு கூற்றுகளும் உண்மை ஆனால் நேரடி விளக்க தொடர்பு இல்லை."
        why_c_en = "Option C evaluation: Assertion is true while Reason is false."
        why_c_ta = "ஆப்ஷன் C மதிப்பீடு: கூற்று உண்மை ஆனால் காரணம் பொய்."
        why_d_en = "Option D evaluation: Assertion is false while Reason is true."
        why_d_ta = "ஆப்ஷன் D மதிப்பீடு: கூற்று பொய் ஆனால் காரணம் உண்மை."

        tip_en = "Assess truth value of Assertion and Reason independently before evaluating causal linkage."
        tip_ta = "கூற்று மற்றும் காரணத்தின் உண்மைத்தன்மையை தனித்தனியாக ஆராய்ந்த பின்னரே காரணத் தொடர்பை மதிப்பிடவும்."
        fact_en = "Under the Tenth Schedule, the Speaker acts as a Tribunal subject to judicial review (Kihoto Hollohan 1992)."
        fact_ta = "பத்தாவது அட்டவணையின் கீழ் சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார் மற்றும் அவரது முடிவுகள் நீதிமன்ற மறுஆய்வுக்கு உட்பட்டவை."

        q = make_pppg_q(
            qid, "Hard", "reasoning", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Balance and randomize keys
    balanced = randomize_and_balance_dataset(questions, seed=306)
    keys = [q["correct_answer"] for q in balanced]
    counts = Counter(keys)
    print("PPPG Part 2B Reasoning Key counts:", counts)
    assert len(balanced) == 25
    for opt in ["A", "B", "C", "D"]:
        assert 6 <= counts[opt] <= 7

    # Validate
    validator = ContentValidator()
    all_errs = []
    for q in balanced:
        errs = validator.validate_question(q)
        if errs:
            all_errs.extend(errs)
    if all_errs:
        raise ValueError(f"Validation failed with {len(all_errs)} errors: {all_errs[:5]}")

    out_file = "data/questions/polity/political_parties_pressure_groups_reasoning.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)

    # Copy to assertion_reason.json for UI compatibility
    ar_copy = "data/questions/polity/political_parties_pressure_groups_assertion_reason.json"
    shutil.copyfile(out_file, ar_copy)

    print(f"Successfully wrote 25 Reasoning MCQs to {out_file} and {ar_copy}")

if __name__ == "__main__":
    get_reasoning_questions()
