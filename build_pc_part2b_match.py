# -*- coding: utf-8 -*-
"""
Build 25 Match the Following MCQs for Parliamentary Committees (PC_MF_001 to PC_MF_025)
TNPSC Nova AI Content Engine
"""
import json
from collections import Counter
from parliamentary_committees_mcq_helper import make_pc_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_match_questions():
    questions = []

    match_specs = [
        ("001", "Financial Committees", "Medium",
         "Match List-I (Committee) with List-II (Membership / Composition):\nList-I:\na) Estimates Committee\nb) Public Accounts Committee\nc) Committee on Public Undertakings\nd) Committee on Welfare of SCs and STs\nList-II:\n1. 22 members (15 LS + 7 RS)\n2. 30 members (all Lok Sabha)\n3. 30 members (20 LS + 10 RS)\n4. 22 members (15 LS + 7 RS, Chairman from LS only)\nSelect the correct code:",
         "பட்டியல்-I (குழு) உடன் பட்டியல்-II (உறுப்பினர் கட்டமைப்பு) பொருத்துக:\nபட்டியல்-I:\na) மதிப்பீட்டுக் குழு\nb) பொதுக் கணக்குக் குழு\nc) பொதுத்துறை நிறுவனங்களுக்கான குழு\nd) எஸ்சி/எஸ்டி நலக் குழு\nபட்டியல்-II:\n1. 22 உறுப்பினர்கள் (15 LS + 7 RS)\n2. 30 உறுப்பினர்கள் (மக்களவை மட்டும்)\n3. 30 உறுப்பினர்கள் (20 LS + 10 RS)\n4. 22 உறுப்பினர்கள் (15 LS + 7 RS, தலைவர் LS மட்டும்)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Estimates Committee has 30 members (all LS); PAC has 22 (15 LS + 7 RS); COPU has 22 (15 LS + 7 RS with Chairman from LS); SC/ST committee has 30 (20 LS + 10 RS). Code: 2-1-4-3.",
         "மதிப்பீட்டுக் குழு 30 (LS மட்டும்); PAC 22 (15 LS + 7 RS); COPU 22 (15 LS + 7 RS, தலைவர் LS மட்டும்); SC/ST நலக் குழு 30 (20 LS + 10 RS). குறியீடு: 2-1-4-3."),

        ("002", "Financial Committees", "Medium",
         "Match List-I (Committee) with List-II (Inception Year / Origin):\nList-I:\na) Public Accounts Committee\nb) Estimates Committee (post-independence)\nc) Committee on Public Undertakings\nd) Departmentally Related Standing Committees\nList-II:\n1. 1950\n2. 1921\n3. 1993\n4. 1964\nSelect the correct code:",
         "பட்டியல்-I (குழு) உடன் பட்டியல்-II (தொடங்கப்பட்ட ஆண்டு) பொருத்துக:\nபட்டியல்-I:\na) பொதுக் கணக்குக் குழு\nb) மதிப்பீட்டுக் குழு (சுதந்திரத்திற்குப் பின்)\nc) பொதுத்துறை நிறுவனங்களுக்கான குழு\nd) துறை சார்ந்த நிலைக்குழுக்கள் (DRSCs)\nபட்டியல்-II:\n1. 1950\n2. 1921\n3. 1993\n4. 1964\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3", "A",
         "PAC was founded in 1921; post-independence Estimates Committee in 1950; COPU in 1964; and DRSCs in 1993. Code: 2-1-4-3.",
         "PAC 1921-ல்; மதிப்பீட்டுக் குழு 1950-ல்; COPU 1964-ல்; DRSCs 1993-ல் அமைக்கப்பட்டன. குறியீடு: 2-1-4-3."),

        ("003", "Committees on Day-to-Day Business", "Medium",
         "Match List-I (Committee) with List-II (Ex-officio Presiding Head):\nList-I:\na) Business Advisory Committee (Lok Sabha)\nb) Committee on Private Members' Bills (Lok Sabha)\nc) Rules Committee (Rajya Sabha)\nd) Library Committee (Parliament)\nList-II:\n1. Chairman of Rajya Sabha\n2. Speaker of Lok Sabha\n3. Deputy Speaker of Lok Sabha\n4. Deputy Speaker of Lok Sabha\nSelect the correct code:",
         "பட்டியல்-I (குழு) உடன் பட்டியல்-II (அலுவல் வழித் தலைவர்) பொருத்துக:\nபட்டியல்-I:\na) அலுவல் ஆலோசனைக் குழு (மக்களவை)\nb) தனிநபர் மசோதாக்கள் குழு (மக்களவை)\nc) விதிகள் குழு (மாநிலங்களவை)\nd) நூலகக் குழு (நாடாளுமன்றம்)\nபட்டியல்-II:\n1. மாநிலங்களவைத் தலைவர்\n2. மக்களவை சபாநாயகர்\n3. மக்களவைத் துணை சபாநாயகர்\n4. மக்களவைத் துணை சபாநாயகர்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-3, c-1, d-4", "a-2, b-3, c-1, d-4",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-2, d-1", "a-3, b-4, c-2, d-1",
         "a-4, b-1, c-2, d-3", "a-4, b-1, c-2, d-3", "A",
         "LS BAC is chaired by Speaker; Private Members' Bills by Deputy Speaker; RS Rules Committee by RS Chairman; Library Committee by Deputy Speaker. Code: 2-3-1-4.",
         "மக்களவை BAC-க்கு சபாநாயகர்; தனிநபர் மசோதாக்கள் குழுவுக்கு துணை சபாநாயகர்; மாநிலங்களவை விதிகள் குழுவுக்கு தலைவர்; நூலகக் குழுவுக்கு துணை சபாநாயகர் தலைமை தாங்குகின்றனர். குறியீடு: 2-3-1-4."),

        ("004", "Financial Committees", "Medium",
         "Match List-I (Committee) with List-II (Key Recommending Person / Reform):\nList-I:\na) Public Accounts Committee\nb) Estimates Committee\nc) Committee on Public Undertakings\nd) DRSC System\nList-II:\n1. John Mathai (1950)\n2. Montagu-Chelmsford Reforms (1919)\n3. Rules Committee (1993)\n4. Krishna Menon Committee (1959)\nSelect the correct code:",
         "பட்டியல்-I (குழு) உடன் பட்டியல்-II (பரிந்துரைத்த நபர் / சீர்திருத்தம்) பொருத்துக:\nபட்டியல்-I:\na) பொதுக் கணக்குக் குழு\nb) மதிப்பீட்டுக் குழு\nc) பொதுத்துறை நிறுவனங்களுக்கான குழு\nd) DRSC முறை\nபட்டியல்-II:\n1. ஜான் மத்தாய் (1950)\n2. மாண்டேகு-செம்ஸ்போர்டு சீர்திருத்தம் (1919)\n3. விதிகள் குழு (1993)\n4. கிருஷ்ண மேனன் குழு (1959)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "PAC -> Montford 1919; Estimates -> John Mathai 1950; COPU -> Krishna Menon 1959; DRSCs -> Rules Committee 1993. Code: 2-1-4-3.",
         "PAC -> மாண்ட்ஃபோர்ட் 1919; மதிப்பீட்டுக் குழு -> ஜான் மத்தாய் 1950; COPU -> கிருஷ்ண மேனன் 1959; DRSCs -> விதிகள் குழு 1993. குறியீடு: 2-1-4-3."),

        ("005", "Committees to Scrutinize and Control", "Medium",
         "Match List-I (Committee) with List-II (Core Responsibility / Mandate):\nList-I:\na) Committee on Subordinate Legislation\nb) Committee on Government Assurances\nc) Committee on Papers Laid on the Table\nd) Joint Committee on Offices of Profit\nList-II:\n1. Scrutinizes promises given by ministers on the floor of the House\n2. Examines rules made by executive under delegated statutory powers\n3. Recommends exemptions from disqualification under Article 102(1)(a)\n4. Verifies statutory compliance and reasons for delay in tabling reports\nSelect the correct code:",
         "பட்டியல்-I (குழு) உடன் பட்டியல்-II (முக்கிய பணி / கடமை) பொருத்துக:\nபட்டியல்-I:\na) துணைச் சட்டங்களுக்கான குழு\nb) அரசு உறுதிமொழிகளுக்கான குழு\nc) அவை மேசையில் வைக்கப்படும் ஆவணங்களுக்கான குழு\nd) ஆதாயம் தரும் பதவிகளுக்கான கூட்டுக் குழு\nபட்டியல்-II:\n1. அவையில் அமைச்சர்கள் அளித்த வாக்குறுதிகளை ஆய்வு செய்தல்\n2. ஒப்படைக்கப்பட்ட அதிகாரத்தின் கீழ் இயற்றப்பட்ட விதிகளை ஆய்வு செய்தல்\n3. சரத்து 102(1)(a)-ன் கீழ் தகுதிநீக்க விலக்குகளைப் பரிந்துரைத்தல்\n4. ஆவணங்களை வைப்பதில் ஏற்படும் தாமதங்களை சரிபார்த்தல்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Subordinate Legislation -> delegated rules (2); Government Assurances -> floor promises (1); Papers Laid -> delay in reports (4); Offices of Profit -> Art 102(1)(a) exemptions (3). Code: 2-1-4-3.",
         "துணைச் சட்டம் -> விதிகள் ஆய்வு (2); அரசு உறுதிமொழிகள் -> வாக்குறுதிகள் (1); ஆவணங்கள் -> தாமதங்கள் (4); ஆதாயப் பதவி -> சரத்து 102 விலக்குகள் (3). குறியீடு: 2-1-4-3."),

        ("006", "Classification of Committees", "Medium",
         "Match List-I (Parliamentary Committee) with List-II (Category):\nList-I:\na) Committee of Privileges\nb) General Purposes Committee\nc) Joint Committee on a Bill\nd) Public Accounts Committee\nList-II:\n1. House Keeping Committee\n2. Committee to Inquire\n3. Financial Standing Committee\n4. Ad Hoc Advisory Committee\nSelect the correct code:",
         "பட்டியல்-I (நாடாளுமன்றக் குழு) உடன் பட்டியல்-II (வகைப்பாடு) பொருத்துக:\nபட்டியல்-I:\na) உரிமைகள் குழு\nb) பொது நோக்கக் குழு\nc) ஒரு மசோதா மீதான கூட்டுக் குழு\nd) பொதுக் கணக்குக் குழு\nபட்டியல்-II:\n1. அவை மேலாண்மைக் குழு\n2. விசாரணைக் குழு\n3. நிதி நிலைக்குழு\n4. தற்காலிக ஆலோசனைக் குழு\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Privileges -> Inquire (2); General Purposes -> House Keeping (1); Joint Committee on Bill -> Ad Hoc Advisory (4); PAC -> Financial Standing (3). Code: 2-1-4-3.",
         "உரிமைகள் -> விசாரணை (2); பொது நோக்கம் -> அவை மேலாண்மை (1); மசோதா கூட்டுக் குழு -> தற்காலிக ஆலோசனை (4); PAC -> நிதி நிலைக்குழு (3). குறியீடு: 2-1-4-3."),

        ("007", "Departmentally Related Standing Committees", "Medium",
         "Match List-I (DRSC) with List-II (House under which it operates):\nList-I:\na) Committee on Home Affairs\nb) Committee on Defence\nc) Committee on Commerce\nd) Committee on Finance\nList-II:\n1. Lok Sabha\n2. Rajya Sabha\n3. Lok Sabha\n4. Rajya Sabha\nSelect the correct code:",
         "பட்டியல்-I (DRSC குழு) உடன் பட்டியல்-II (செயல்படும் அவை) பொருத்துக:\nபட்டியல்-I:\na) உள்துறை விவகாரக் குழு\nb) பாதுகாப்புத் துறைக் குழு\nc) வணிகக் குழு\nd) நிதித் துறைக் குழு\nபட்டியல்-II:\n1. மக்களவை\n2. மாநிலங்களவை\n3. மக்களவை\n4. மாநிலங்களவை\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Home Affairs is under RS (2); Defence under LS (1); Commerce under RS (4); Finance under LS (3). Code: 2-1-4-3.",
         "உள்துறை -> மாநிலங்களவை (2); பாதுகாப்பு -> மக்களவை (1); வணிகம் -> மாநிலங்களவை (4); நிதி -> மக்களவை (3). குறியீடு: 2-1-4-3."),

        ("008", "Committees to Inquire", "Medium",
         "Match List-I (Committee) with List-II (Membership in Lok Sabha and Rajya Sabha):\nList-I:\na) Committee on Petitions\nb) Committee of Privileges\nc) Ethics Committee\nd) Rules Committee\nList-II:\n1. LS 15, RS 10\n2. LS 15, RS 10\n3. LS 15, RS 16\n4. LS 15, RS 10\nSelect the correct code:",
         "பட்டியல்-I (குழு) உடன் பட்டியல்-II (மக்களவை மற்றும் மாநிலங்களவை உறுப்பினர் பலம்) பொருத்துக:\nபட்டியல்-I:\na) மனுக்கள் குழு\nb) உரிமைகள் குழு\nc) ஒழுக்கநெறிக் குழு\nd) விதிகள் குழு\nபட்டியல்-II:\n1. LS 15, RS 10\n2. LS 15, RS 10\n3. LS 15, RS 16\n4. LS 15, RS 10\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
         "a-3, b-1, c-2, d-4", "a-3, b-1, c-2, d-4",
         "a-2, b-4, c-3, d-1", "a-2, b-4, c-3, d-1",
         "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2", "A",
         "Petitions (15/10); Privileges (15/10); Ethics (15/10); Rules (15/16). Code: 1-2-4-3.",
         "மனுக்கள் (15/10); உரிமைகள் (15/10); ஒழுக்கநெறி (15/10); விதிகள் (15/16). குறியீடு: 1-2-4-3."),

        ("009", "Financial Committees", "Medium",
         "Match List-I (Term / Concept) with List-II (Description):\nList-I:\na) Continuous Economy Committee\nb) Post-mortem scrutiny\nc) Friend, philosopher, and guide\nd) Krishna Menon Committee\nList-II:\n1. CAG's relationship to Public Accounts Committee\n2. Estimates Committee suggesting alternative policies\n3. Creator of Committee on Public Undertakings\n4. Examination of expenditures after they have occurred\nSelect the correct code:",
         "பட்டியல்-I (சொல் / கோட்பாடு) உடன் பட்டியல்-II (விளக்கம்) பொருத்துக:\nபட்டியல்-I:\na) தொடர் சிக்கனக் குழு\nb) பிரேதப் பரிசோதனை ஆய்வு\nc) நண்பன், தத்துவஞானி மற்றும் வழிகாட்டி\nd) கிருஷ்ண மேனன் குழு\nபட்டியல்-II:\n1. பொதுக் கணக்குக் குழுவிற்கு CAG-ன் உறவு\n2. மாற்று கொள்கைகளை பரிந்துரைக்கும் மதிப்பீட்டுக் குழு\n3. பொதுத்துறை நிறுவனக் குழுவை உருவாக்கியவர்\n4. செலவுகள் நடந்த பின் செய்யப்படும் ஆய்வு\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Continuous Economy -> Estimates (2); Post-mortem -> PAC scrutiny (4); Friend/guide -> CAG (1); Krishna Menon -> COPU (3). Code: 2-4-1-3.",
         "தொடர் சிக்கனக் குழு -> மதிப்பீட்டுக் குழு (2); பிரேதப் பரிசோதனை -> PAC ஆய்வு (4); நண்பன்/வழிகாட்டி -> CAG (1); கிருஷ்ண மேனன் -> COPU (3). குறியீடு: 2-4-1-3."),

        ("010", "Parliamentary Committee Rules", "Medium",
         "Match List-I (Rule / Article) with List-II (Procedural Subject):\nList-I:\na) Article 105(3)\nb) Article 118(1)\nc) Lok Sabha Rule 259\nd) Lok Sabha Rule 270\nList-II:\n1. Power of Parliament to frame rules of procedure\n2. Powers, privileges, and immunities of committees\n3. Power of committee to send for persons, papers, and records\n4. Quorum of a parliamentary committee (one-third)\nSelect the correct code:",
         "பட்டியல்-I (விதி / சரத்து) உடன் பட்டியல்-II (நடைமுறை விவகாரம்) பொருத்துக:\nபட்டியல்-I:\na) சரத்து 105(3)\nb) சரத்து 118(1)\nc) மக்களவை விதி 259\nd) மக்களவை விதி 270\nபட்டியல்-II:\n1. நடைமுறை விதிகளை உருவாக்க நாடாளுமன்றத்தின் அதிகாரம்\n2. குழுக்களின் அதிகாரங்கள், சலுகைகள் மற்றும் விலக்களிப்புகள்\n3. நபர்கள் மற்றும் ஆவணங்களை வரவழைக்கும் குழுவின் அதிகாரம்\n4. நாடாளுமன்றக் குழுவின் கோரம் (மூன்றில் ஒரு பங்கு)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Art 105(3) -> privileges (2); Art 118(1) -> rulemaking (1); Rule 259 -> quorum 1/3rd (4); Rule 270 -> send for persons/papers (3). Code: 2-1-4-3.",
         "சரத்து 105(3) -> சலுகைகள் (2); சரத்து 118(1) -> விதிகள் உருவாக்கம் (1); விதி 259 -> கோரம் 1/3 (4); விதி 270 -> ஆவணங்கள்/நபர்கள் சம்மன் (3). குறியீடு: 2-1-4-3."),

        ("011", "Ad Hoc Committees", "Medium",
         "Match List-I (Historic JPC) with List-II (Year of Constitution):\nList-I:\na) Bofors contract JPC\nb) Harshad Mehta securities scam JPC\nc) Ketan Parekh stock market scam JPC\nd) 2G spectrum allocation JPC\nList-II:\n1. 1992\n2. 1987\n3. 2011\n4. 2001\nSelect the correct code:",
         "பட்டியல்-I (வரலாற்று JPC) உடன் பட்டியல்-II (அமைக்கப்பட்ட ஆண்டு) பொருத்துக:\nபட்டியல்-I:\na) போஃபோர்ஸ் ஒப்பந்த JPC\nb) ஹர்ஷத் மேத்தா பங்குச்சந்தை JPC\nc) கேத்தன் பரேக் பங்குச்சந்தை JPC\nd) 2G அலைக்கற்றை ஒதுக்கீடு JPC\nபட்டியல்-II:\n1. 1992\n2. 1987\n3. 2011\n4. 2001\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Bofors -> 1987 (2); Harshad Mehta -> 1992 (1); Ketan Parekh -> 2001 (4); 2G spectrum -> 2011 (3). Code: 2-1-4-3.",
         "போஃபோர்ஸ் -> 1987 (2); ஹர்ஷத் மேத்தா -> 1992 (1); கேத்தன் பரேக் -> 2001 (4); 2G -> 2011 (3). குறியீடு: 2-1-4-3."),

        ("012", "House Keeping Committees", "Medium",
         "Match List-I (House Keeping Committee) with List-II (Total Membership):\nList-I:\na) Library Committee\nb) House Committee (Lok Sabha)\nc) Joint Committee on Salaries and Allowances\nd) General Purposes Committee\nList-II:\n1. 12 members\n2. 9 members (6 LS + 3 RS)\n3. All Standing Committee Chairpersons & Leaders\n4. 15 members (10 LS + 5 RS)\nSelect the correct code:",
         "பட்டியல்-I (அவை மேலாண்மைக் குழு) உடன் பட்டியல்-II (மொத்த உறுப்பினர்கள்) பொருத்துக:\nபட்டியல்-I:\na) நூலகக் குழு\nb) அவை குழு (மக்களவை)\nc) ஊதியம் மற்றும் படிகளுக்கான கூட்டுக் குழு\nd) பொது நோக்கக் குழு\nபட்டியல்-II:\n1. 12 உறுப்பினர்கள்\n2. 9 உறுப்பினர்கள் (6 LS + 3 RS)\n3. அனைத்து நிலைக்குழுத் தலைவர்கள் மற்றும் கட்சித் தலைவர்கள்\n4. 15 உறுப்பினர்கள் (10 LS + 5 RS)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Library -> 9 (2); House LS -> 12 (1); Salaries -> 15 (4); General Purposes -> all chairpersons (3). Code: 2-1-4-3.",
         "நூலகம் -> 9 (2); அவை குழு LS -> 12 (1); ஊதியம் -> 15 (4); பொது நோக்கம் -> அனைத்து தலைவர்கள் (3). குறியீடு: 2-1-4-3."),

        ("013", "Departmentally Related Standing Committees", "Medium",
         "Match List-I (Ministry) with List-II (Departmentally Related Standing Committee House):\nList-I:\na) Ministry of External Affairs\nb) Ministry of Human Resource Development (Education)\nc) Ministry of Railways\nd) Ministry of Health and Family Welfare\nList-II:\n1. Rajya Sabha\n2. Lok Sabha\n3. Rajya Sabha\n4. Lok Sabha\nSelect the correct code:",
         "பட்டியல்-I (அமைச்சகம்) உடன் பட்டியல்-II (DRSC இயங்கும் அவை) பொருத்துக:\nபட்டியல்-I:\na) வெளியுறவுத்துறை அமைச்சகம்\nb) மனிதவள மேம்பாட்டு அமைச்சகம் (கல்வி)\nc) ரயில்வே அமைச்சகம்\nd) சுகாதாரம் மற்றும் குடும்ப நல அமைச்சகம்\nபட்டியல்-II:\n1. மாநிலங்களவை\n2. மக்களவை\n3. மாநிலங்களவை\n4. மக்களவை\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "External Affairs -> LS (2); Education -> RS (1); Railways -> LS (4); Health -> RS (3). Code: 2-1-4-3.",
         "வெளியுறவு -> மக்களவை (2); கல்வி -> மாநிலங்களவை (1); ரயில்வே -> மக்களவை (4); சுகாதாரம் -> மாநிலங்களவை (3). குறியீடு: 2-1-4-3."),

        ("014", "Financial Committees", "Medium",
         "Match List-I (Committee) with List-II (Chairman Selection Convention):\nList-I:\na) Public Accounts Committee\nb) Estimates Committee\nc) Committee on Public Undertakings\nd) Committee on Private Members' Bills\nList-II:\n1. Invariably from Ruling Party appointed by Speaker\n2. By convention from Opposition appointed by Speaker\n3. Deputy Speaker of Lok Sabha\n4. Appointed by Speaker from Lok Sabha members only\nSelect the correct code:",
         "பட்டியல்-I (குழு) உடன் பட்டியல்-II (தலைவர் தேர்வு மரபு) பொருத்துக:\nபட்டியல்-I:\na) பொதுக் கணக்குக் குழு\nb) மதிப்பீட்டுக் குழு\nc) பொதுத்துறை நிறுவனங்களுக்கான குழு\nd) தனிநபர் மசோதாக்கள் குழு\nபட்டியல்-II:\n1. ஆளும் கட்சியிலிருந்து சபாநாயகரால் நியமிக்கப்படுபவர்\n2. மரபின்படி எதிர்க்கட்சியிலிருந்து சபாநாயகரால் நியமிக்கப்படுபவர்\n3. மக்களவைத் துணை சபாநாயகர்\n4. மக்களவை உறுப்பினர்களிலிருந்து மட்டுமே சபாநாயகரால் நியமிக்கப்படுபவர்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "PAC -> Opposition (2); Estimates -> Ruling (1); COPU -> LS member only (4); Private Members -> Deputy Speaker (3). Code: 2-1-4-3.",
         "PAC -> எதிர்க்கட்சி (2); மதிப்பீட்டுக் குழு -> ஆளும் கட்சி (1); COPU -> LS உறுப்பினர் மட்டுமே (4); தனிநபர் மசோதாக்கள் -> துணை சபாநாயகர் (3). குறியீடு: 2-1-4-3."),

        ("015", "Committees to Scrutinize and Control", "Medium",
         "Match List-I (Committee) with List-II (Establishment Year):\nList-I:\na) Committee on Government Assurances\nb) Committee on Subordinate Legislation (Lok Sabha)\nc) Committee on Papers Laid on the Table (Lok Sabha)\nd) Committee on Empowerment of Women\nList-II:\n1. 1953\n2. 1953\n3. 1997\n4. 1975\nSelect the correct code:",
         "பட்டியல்-I (குழு) உடன் பட்டியல்-II (அமைக்கப்பட்ட ஆண்டு) பொருத்துக:\nபட்டியல்-I:\na) அரசு உறுதிமொழிகளுக்கான குழு\nb) துணைச் சட்டங்களுக்கான குழு (மக்களவை)\nc) அவை மேசையில் வைக்கப்படும் ஆவணங்களுக்கான குழு (மக்களவை)\nd) பெண்கள் அதிகாரமளித்தல் குழு\nபட்டியல்-II:\n1. 1953\n2. 1953\n3. 1997\n4. 1975\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
         "a-2, b-1, c-3, d-4", "a-2, b-1, c-3, d-4",
         "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
         "a-3, b-4, c-2, d-1", "a-3, b-4, c-2, d-1", "A",
         "Govt Assurances -> 1953 (1); Subordinate Legislation -> 1953 (2); Papers Laid -> 1975 (4); Women -> 1997 (3). Code: 1-2-4-3.",
         "அரசு உறுதிமொழிகள் -> 1953 (1); துணைச் சட்டம் -> 1953 (2); ஆவணங்கள் -> 1975 (4); பெண்கள் -> 1997 (3). குறியீடு: 1-2-4-3."),

        ("016", "Parliamentary Committees Overview", "Medium",
         "Match List-I (Standing Committee) with List-II (Total Number of Members):\nList-I:\na) Estimates Committee\nb) Public Accounts Committee\nc) Departmentally Related Standing Committee\nd) Library Committee\nList-II:\n1. 22\n2. 30\n3. 9\n4. 31\nSelect the correct code:",
         "பட்டியல்-I (நிலைக்குழு) உடன் பட்டியல்-II (மொத்த உறுப்பினர்கள்) பொருத்துக:\nபட்டியல்-I:\na) மதிப்பீட்டுக் குழு\nb) பொதுக் கணக்குக் குழு\nc) துறை சார்ந்த நிலைக்குழு (DRSC)\nd) நூலகக் குழு\nபட்டியல்-II:\n1. 22\n2. 30\n3. 9\n4. 31\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Estimates -> 30 (2); PAC -> 22 (1); DRSC -> 31 (4); Library -> 9 (3). Code: 2-1-4-3.",
         "மதிப்பீட்டுக் குழு -> 30 (2); PAC -> 22 (1); DRSC -> 31 (4); நூலகம் -> 9 (3). குறியீடு: 2-1-4-3."),

        ("017", "Committees to Inquire", "Medium",
         "Match List-I (Inquiry / Ethics Committee) with List-II (Function):\nList-I:\na) Committee of Privileges\nb) Ethics Committee\nc) Committee on Petitions\nd) Railway Convention Committee\nList-II:\n1. Examines moral and ethical conduct and Register of Interests\n2. Investigates breaches of parliamentary rights and contempt\n3. Reviews rate of dividend payable by Railways to General Revenues\n4. Considers public grievances and petitions on bills\nSelect the correct code:",
         "பட்டியல்-I (விசாரணை / நெறிமுறைக் குழு) உடன் பட்டியல்-II (பணி) பொருத்துக:\nபட்டியல்-I:\na) உரிமைகள் குழு\nb) ஒழுக்கநெறிக் குழு\nc) மனுக்கள் குழு\nd) ரயில்வே மரபுக் குழு\nபட்டியல்-II:\n1. ஒழுக்கம் மற்றும் நிதி நலன்கள் பதிவேட்டை ஆய்வு செய்தல்\n2. நாடாளுமன்ற உரிமை மீறல்கள் மற்றும் அவமதிப்பை விசாரித்தல்\n3. ரயில்வே பொது வருவாய்க்கு செலுத்தும் ஈவுத்தொகையை மதிப்பாய்வு செய்தல்\n4. பொது மக்கள் குறைகள் மற்றும் மசோதாக்கள் மீதான மனுக்களைப் பரிசீலித்தல்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "Privileges -> breach/contempt (2); Ethics -> moral conduct/interests (1); Petitions -> public petitions (4); Railway Convention -> dividend rate (3). Code: 2-1-4-3.",
         "உரிமைகள் -> மீறல்/அவமதிப்பு (2); ஒழுக்கநெறி -> நடத்தை/பதிவேடு (1); மனுக்கள் -> பொது மனுக்கள் (4); ரயில்வே மரபு -> ஈவுத்தொகை (3). குறியீடு: 2-1-4-3."),

        ("018", "Parliamentary Committee Rules", "Medium",
         "Match List-I (Concept) with List-II (Procedural Meaning):\nList-I:\na) Quorum\nb) In camera\nc) Minute of Dissent\nd) Action Taken Report\nList-II:\n1. Private sitting without press or public admission\n2. Minimum attendance required to hold a valid meeting (1/3rd)\n3. Evaluation of ministry compliance with earlier recommendations\n4. Formal recorded disagreement appended to committee report\nSelect the correct code:",
         "பட்டியல்-I (கோட்பாடு) உடன் பட்டியல்-II (நடைமுறைப் பொருள்) பொருத்துக:\nபட்டியல்-I:\na) கோரம் (Quorum)\nb) இன் கேமரா (In camera)\nc) மாறுபட்ட கருத்து அறிக்கை (Minute of Dissent)\nd) நடவடிக்கை எடுக்கப்பட்ட அறிக்கை (ATR)\nபட்டியல்-II:\n1. பத்திரிகையாளர்கள் அல்லது பொதுமக்கள் இன்றி ரகசியமாக நடக்கும் கூட்டம்\n2. முறையான கூட்டம் நடத்தத் தேவையான குறைந்தபட்ச வரம்பு (1/3)\n3. முந்தைய பரிந்துரைகளை அமைச்சகம் செயல்படுத்தியதை மதிப்பீடு செய்தல்\n4. அறிக்கையுடன் இணைக்கப்படும் அதிகாரப்பூர்வ மாறுபட்ட கருத்து\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Quorum -> minimum attendance 1/3 (2); In camera -> private sitting (1); Minute of Dissent -> recorded disagreement (4); ATR -> ministry compliance evaluation (3). Code: 2-1-4-3.",
         "கோரம் -> குறைந்தபட்ச வருகை 1/3 (2); இன் கேமரா -> ரகசிய கூட்டம் (1); மாறுபட்ட கருத்து -> பதிவு செய்யப்பட்ட கருத்து வேறுபாடு (4); ATR -> பரிந்துரைகள் மதிப்பீடு (3). குறியீடு: 2-1-4-3."),

        ("019", "Consultative Committees", "Medium",
         "Match List-I (Feature) with List-II (Status in Consultative Committees vs Standing Committees):\nList-I:\na) Presiding Authority\nb) Secretariat Support\nc) Nature of Outcome\nd) Voting Procedure\nList-II:\n1. Parliament Secretariat\n2. Concerned Union Minister\n3. No formal voting or division\n4. Informal discussion, no parliamentary report\nSelect the correct code:",
         "பட்டியல்-I (அம்சம்) உடன் பட்டியல்-II (ஆலோசனைக் குழுக்களின் நிலை) பொருத்துக:\nபட்டியல்-I:\na) தலைமை அதிகாரம்\nb) செயலக ஆதரவு\nc) விவாதங்களின் முடிவு\nd) வாக்கெடுப்பு முறை\nபட்டியல்-II:\n1. நாடாளுமன்ற செயலகம்\n2. சம்பந்தப்பட்ட மத்திய அமைச்சர்\n3. முறையான வாக்கெடுப்பு அல்லது பிரிவு இல்லை\n4. முறைசாரா விவாதம், நாடாளுமன்ற அறிக்கை இல்லை\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Presiding -> Union Minister (2); Secretariat -> Ministry of Parliamentary Affairs / Parliament (1); Outcome -> informal, no report (4); Voting -> no formal vote (3). Code: 2-1-4-3.",
         "தலைமை -> மத்திய அமைச்சர் (2); செயலகம் -> விவகார அமைச்சகம் (1); முடிவு -> முறைசாரா விவாதம் (4); வாக்கெடுப்பு -> வாக்கெடுப்பு இல்லை (3). குறியீடு: 2-1-4-3."),

        ("020", "Financial Committees", "Medium",
         "Match List-I (Audit Report Category) with List-II (Examining Parliamentary Body):\nList-I:\na) Appropriation Accounts (Civil & Defence)\nb) Commercial Undertakings / PSUs\nc) Demands for Grants before voting\nd) Excess expenditure over voted grants\nList-II:\n1. Committee on Public Undertakings\n2. Public Accounts Committee\n3. Public Accounts Committee (prior regularisation)\n4. Departmentally Related Standing Committees\nSelect the correct code:",
         "பட்டியல்-I (தணிக்கை அறிக்கை வகை) உடன் பட்டியல்-II (ஆய்வு செய்யும் நாடாளுமன்ற அமைப்பு) பொருத்துக:\nபட்டியல்-I:\na) ஒதுக்கீட்டுக் கணக்குகள் (குடிமை & பாதுகாப்பு)\nb) பொதுத்துறை நிறுவனங்கள்\nc) வாக்கெடுப்பிற்கு முந்தைய மானியக் கோரிக்கைகள்\nd) அனுமதிக்கப்பட்ட மானியத்தை விட கூடுதல் செலவு\nபட்டியல்-II:\n1. பொதுத்துறை நிறுவனங்களுக்கான குழு (COPU)\n2. பொதுக் கணக்குக் குழு (PAC)\n3. பொதுக் கணக்குக் குழு (வரன்முறைப்படுத்தல்)\n4. துறை சார்ந்த நிலைக்குழுக்கள் (DRSCs)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "Appropriation -> PAC (2); Commercial -> COPU (1); Demands for Grants -> DRSCs (4); Excess expenditure -> PAC regularisation (3). Code: 2-1-4-3.",
         "ஒதுக்கீட்டுக் கணக்குகள் -> PAC (2); பொதுத்துறை -> COPU (1); மானியக் கோரிக்கைகள் -> DRSCs (4); கூடுதல் செலவு -> PAC வரன்முறைப்படுத்தல் (3). குறியீடு: 2-1-4-3."),

        ("021", "Committees on Day-to-Day Business", "Medium",
         "Match List-I (House Committee) with List-II (Lok Sabha Membership Strength):\nList-I:\na) Business Advisory Committee\nb) Rules Committee\nc) Committee on Private Members' Bills\nd) Committee on Absence of Members\nList-II:\n1. 15 members\n2. 15 members\n3. 15 members\n4. 15 members\nSelect the correct code:",
         "பட்டியல்-I (அவை குழு) உடன் பட்டியல்-II (மக்களவை உறுப்பினர் பலம்) பொருத்துக:\nபட்டியல்-I:\na) அலுவல் ஆலோசனைக் குழு (BAC)\nb) விதிகள் குழு\nc) தனிநபர் மசோதாக்கள் குழு\nd) வருகை தராததற்கான குழு\nபட்டியல்-II:\n1. 15 உறுப்பினர்கள்\n2. 15 உறுப்பினர்கள்\n3. 15 உறுப்பினர்கள்\n4. 15 உறுப்பினர்கள்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "All four Lok Sabha business committees (BAC, Rules, Private Members, Absence) have exactly 15 members. Code: 1-2-3-4.",
         "மக்களவையின் நான்கு அலுவல் குழுக்களுமே (BAC, விதிகள், தனிநபர் மசோதா, வருகை தராமை) தலா 15 உறுப்பினர்களைக் கொண்டுள்ளன. குறியீடு: 1-2-3-4."),

        ("022", "Financial Committees", "Medium",
         "Match List-I (Financial Committee Milestone) with List-II (Year):\nList-I:\na) PAC first constituted under Montford reforms\nb) Estimates Committee recommended by John Mathai\nc) Rajya Sabha members first associated with PAC\nd) COPU membership expanded to 22\nList-II:\n1. 1950\n2. 1921\n3. 1974\n4. 1954\nSelect the correct code:",
         "பட்டியல்-I (நிதிக் குழு வரலாற்று நிகழ்வு) உடன் பட்டியல்-II (ஆண்டு) பொருத்துக:\nபட்டியல்-I:\na) மாண்ட்ஃபோர்ட் சீர்திருத்தத்தில் PAC முதன்முதலில் அமைக்கப்பட்டது\nb) ஜான் மத்தாயால் மதிப்பீட்டுக் குழு பரிந்துரைக்கப்பட்டது\nc) மாநிலங்களவை உறுப்பினர்கள் PAC-ல் இணைக்கப்பட்டது\nd) COPU உறுப்பினர்கள் 22 ஆக உயர்த்தப்பட்டது\nபட்டியல்-II:\n1. 1950\n2. 1921\n3. 1974\n4. 1954\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "PAC -> 1921 (2); Estimates -> 1950 (1); RS in PAC -> 1954 (4); COPU 22 -> 1974 (3). Code: 2-1-4-3.",
         "PAC -> 1921 (2); மதிப்பீட்டுக் குழு -> 1950 (1); PAC-ல் RS -> 1954 (4); COPU 22 -> 1974 (3). குறியீடு: 2-1-4-3."),

        ("023", "Departmentally Related Standing Committees", "Medium",
         "Match List-I (DRSC Milestone) with List-II (Number of Committees / Strength):\nList-I:\na) Inception of DRSC system in 1993\nb) Expansion of DRSC system in 2004\nc) Restructured membership per DRSC in 2004\nd) Original membership per DRSC in 1993\nList-II:\n1. 24 committees\n2. 17 committees\n3. 45 members (30 LS + 15 RS)\n4. 31 members (21 LS + 10 RS)\nSelect the correct code:",
         "பட்டியல்-I (DRSC மைல்கல்) உடன் பட்டியல்-II (குழுக்களின் எண்ணிக்கை / பலம்) பொருத்துக:\nபட்டியல்-I:\na) 1993-ல் DRSC முறை தொடங்கப்பட்டது\nb) 2004-ல் DRSC முறை விரிவாக்கப்பட்டது\nc) 2004-ல் மறுசீரமைக்கப்பட்ட உறுப்பினர் பலம்\nd) 1993-ல் தொடக்க கால உறுப்பினர் பலம்\nபட்டியல்-II:\n1. 24 குழுக்கள்\n2. 17 குழுக்கள்\n3. 45 உறுப்பினர்கள் (30 LS + 15 RS)\n4. 31 உறுப்பினர்கள் (21 LS + 10 RS)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "1993 -> 17 committees (2); 2004 -> 24 committees (1); 2004 strength -> 31 (4); 1993 strength -> 45 (3). Code: 2-1-4-3.",
         "1993 -> 17 குழுக்கள் (2); 2004 -> 24 குழுக்கள் (1); 2004 பலம் -> 31 (4); 1993 பலம் -> 45 (3). குறியீடு: 2-1-4-3."),

        ("024", "Classification of Committees", "Medium",
         "Match List-I (Parliamentary Committee) with List-II (Term of Office):\nList-I:\na) Public Accounts Committee\nb) Estimates Committee\nc) Joint Committee on a Bill\nd) Ethics Committee\nList-II:\n1. One year\n2. One year\n3. One year\n4. Ceases to exist upon presenting its report\nSelect the correct code:",
         "பட்டியல்-I (நாடாளுமன்றக் குழு) உடன் பட்டியல்-II (பதவிக்காலம்) பொருத்துக:\nபட்டியல்-I:\na) பொதுக் கணக்குக் குழு\nb) மதிப்பீட்டுக் குழு\nc) மசோதா மீதான கூட்டுக் குழு\nd) ஒழுக்கநெறிக் குழு\nபட்டியல்-II:\n1. ஒரு ஆண்டு\n2. ஒரு ஆண்டு\n3. ஒரு ஆண்டு\n4. அறிக்கை சமர்ப்பித்தவுடன் கலைந்துவிடும்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
         "a-2, b-1, c-3, d-4", "a-2, b-1, c-3, d-4",
         "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
         "a-3, b-4, c-2, d-1", "a-3, b-4, c-2, d-1", "A",
         "PAC, Estimates, and Ethics committees have a term of 1 year. An ad hoc Joint Committee on a Bill ceases upon report submission. Code: 1-2-4-3.",
         "PAC, மதிப்பீட்டுக் குழு மற்றும் ஒழுக்கநெறிக் குழு ஆகியவற்றின் பதவிக்காலம் 1 ஆண்டு. மசோதா கூட்டுக் குழு அறிக்கை அளித்ததும் முடிவுக்கு வருகிறது. குறியீடு: 1-2-4-3."),

        ("025", "Parliamentary Committees Overview", "Medium",
         "Match List-I (Committee Group) with List-II (Core Character):\nList-I:\na) Financial Committees (PAC, EC, COPU)\nb) Committees to Scrutinize & Control (Assurances, Subordinate)\nc) House Keeping Committees (House, Library, Salaries)\nd) Ad Hoc Committees (Select / Joint on Bills, JPCs)\nList-II:\n1. Look after facilities, amenities, and internal services for MPs\n2. Ensure financial regularity, economy, and commercial efficiency\n3. Temporary bodies created for specific task or inquiry\n4. Check executive promises and statutory delegated rules\nSelect the correct code:",
         "பட்டியல்-I (குழுத் தொகுதி) உடன் பட்டியல்-II (முக்கிய இயல்பு) பொருத்துக:\nபட்டியல்-I:\na) நிதிக் குழுக்கள் (PAC, EC, COPU)\nb) ஆய்வு மற்றும் கண்காணிப்புக் குழுக்கள் (உறுதிமொழிகள், துணைச் சட்டம்)\nc) அவை மேலாண்மைக் குழுக்கள் (அவை, நூலகம், ஊதியம்)\nd) தற்காலிகக் குழுக்கள் (தேர்வு/கூட்டுக் குழுக்கள், JPCs)\nபட்டியல்-II:\n1. எம்பிக்களுக்கான வசதிகள் மற்றும் சேவைகளைக் கவனித்தல்\n2. நிதி ஒழுங்கு, சிக்கனம் மற்றும் வணிக செயல்திறனை உறுதி செய்தல்\n3. குறிப்பிட்ட பணிக்காக உருவாக்கப்படும் தற்காலிக அமைப்புகள்\n4. நிர்வாக வாக்குறுதிகள் மற்றும் சட்ட விதிகளின் வரம்புகளை ஆய்வு செய்தல்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Financial -> regularity/economy (2); Scrutinize -> promises/rules (4); House Keeping -> MP amenities (1); Ad Hoc -> temporary inquiry (3). Code: 2-4-1-3.",
         "நிதிக் குழுக்கள் -> நிதி ஒழுங்கு/சிக்கனம் (2); கண்காணிப்பு -> வாக்குறுதிகள்/விதிகள் (4); அவை மேலாண்மை -> எம்பிக்கள் வசதிகள் (1); தற்காலிகக் குழுக்கள் -> குறிப்பிட்ட பணி (3). குறியீடு: 2-4-1-3.")
    ]

    for qid, sub, diff, en_s, ta_s, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, corr, exp_e, exp_t in match_specs:
        full_qid = f"PC_MF_{qid}"
        questions.append(make_pc_q(
            qid=full_qid,
            diff=diff,
            qtype="match_the_following",
            subtopic=sub,
            en_stem=en_s,
            ta_stem=ta_s,
            en_a=en_a,
            ta_a=ta_a,
            en_b=en_b,
            ta_b=ta_b,
            en_c=en_c,
            ta_c=ta_c,
            en_d=en_d,
            ta_d=ta_d,
            correct_key=corr,
            exp_en=exp_e,
            exp_ta=exp_t,
            why_a_en="Correct. Accurately pairs all entries in List-I with List-II.",
            why_a_ta="சரி. பட்டியல்-I மற்றும் பட்டியல்-II-ல் உள்ள அனைத்து விவரங்களையும் சரியாகப் பொருத்துகிறது.",
            why_b_en="Incorrect matching permutation.",
            why_b_ta="தவறான பொருத்தக் குறியீடு.",
            why_c_en="Incorrect matching permutation.",
            why_c_ta="தவறான பொருத்தக் குறியீடு.",
            why_d_en="Incorrect matching permutation.",
            why_d_ta="தவறான பொருத்தக் குறியீடு.",
            tip_en="In matching questions, identifying two definitive pairs often reveals the correct option code immediately.",
            tip_ta="பொருத்துக வினாக்களில் இரண்டு உறுதியான இணைகளைக் கண்டறிவது சரியான விடையை விரைவாகத் தேர்ந்தெடுக்க உதவும்.",
            fact_en="Matching questions test comparative structural knowledge across parliamentary committees.",
            fact_ta="பொருத்துக வினாக்கள் நாடாளுமன்றக் குழுக்களின் பல்வேறு கட்டமைப்பு கூறுகளை ஒப்பிட்டு சோதிக்கின்றன."
        ))

    return questions

def main():
    qs = get_match_questions()
    print(f"Generated {len(qs)} Match questions.")
    balanced_qs = randomize_and_balance_dataset(qs, seed=2031)
    keys = [q["correct_answer"] for q in balanced_qs]
    print("Part 2B PC Match Key counts:", Counter(keys))

    validator = ContentValidator()
    all_errors = []
    for q in balanced_qs:
        errs = validator.validate_question(q)
        if errs:
            all_errors.extend(errs)

    if all_errors:
        print(f"Validation failed with {len(all_errors)} errors:")
        for err in all_errors[:10]:
            print(f"  - {err}")
        raise ValueError("Validation failed!")

    out_file1 = "data/questions/polity/parliamentary_committees_match_the_following.json"
    out_file2 = "data/questions/polity/parliamentary_committees_match.json"

    with open(out_file1, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    with open(out_file2, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)

    print(f"Successfully wrote {len(balanced_qs)} match MCQs to {out_file1} and alias {out_file2}")

if __name__ == "__main__":
    main()
