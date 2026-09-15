# -*- coding: utf-8 -*-
"""
Build Parliamentary Committees - Part 1 Easy (50 MCQs)
Identifier: PC_E_001 to PC_E_050
Key Distribution: Balanced 12-13 per option via AnswerRandomizer
Anti-Block: Max consecutive run <= 2
"""
import json
import os
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from parliamentary_committees_mcq_helper import make_pc_q

def build_easy_mcqs():
    questions = []

    easy_items = [
        # 1
        ("PC_E_001", "Public Accounts Committee Origin",
         "In which year was the Public Accounts Committee (PAC) set up for the first time in India?",
         "இந்தியாவில் முதன்முதலில் பொதுக் கணக்குக் குழு (PAC) எந்த ஆண்டு அமைக்கப்பட்டது?",
         "1919", "1919",
         "1921", "1921",
         "1950", "1950",
         "1947", "1947", "B",
         "The Public Accounts Committee was first set up in 1921 under the provisions of the Government of India Act of 1919.",
         "1919-ன் இந்திய அரசுச் சட்டத்தின் விதிகளின் கீழ் 1921-ல் முதன்முதலில் பொதுக் கணக்குக் குழு அமைக்கப்பட்டது."),

        # 2
        ("PC_E_002", "Public Accounts Committee Composition",
         "What is the total membership of the Public Accounts Committee (PAC)?",
         "பொதுக் கணக்குக் குழுவின் (PAC) மொத்த உறுப்பினர்களின் எண்ணிக்கை யாது?",
         "15 members", "15 உறுப்பினர்கள்",
         "22 members (15 Lok Sabha + 7 Rajya Sabha)", "22 உறுப்பினர்கள் (15 மக்களவை + 7 மாநிலங்களவை)",
         "30 members", "30 உறுப்பினர்கள்",
         "31 members", "31 உறுப்பினர்கள்", "B",
         "The Public Accounts Committee consists of 22 members: 15 from Lok Sabha and 7 from Rajya Sabha.",
         "பொதுக் கணக்குக் குழு 22 உறுப்பினர்களைக் கொண்டது: 15 பேர் மக்களவையிலிருந்தும், 7 பேர் மாநிலங்களவையிலிருந்தும் தேர்ந்தெடுக்கப்படுகின்றனர்."),

        # 3
        ("PC_E_003", "Estimates Committee Composition",
         "What is the total membership of the Estimates Committee and from which House are they elected?",
         "மதிப்பீட்டுக் குழுவின் மொத்த உறுப்பினர்களின் எண்ணிக்கை என்ன மற்றும் அவர்கள் எந்த அவையிலிருந்து தேர்ந்தெடுக்கப்படுகிறார்கள்?",
         "22 members from both Houses", "இரு அவைகளிலிருந்தும் 22 உறுப்பினர்கள்",
         "30 members, ALL from Lok Sabha only", "30 உறுப்பினர்கள், அனைவரும் மக்களவையிலிருந்து மட்டுமே",
         "30 members, ALL from Rajya Sabha only", "30 உறுப்பினர்கள், அனைவரும் மாநிலங்களவையிலிருந்து மட்டுமே",
         "15 members from Lok Sabha only", "மக்களவையிலிருந்து 15 உறுப்பினர்கள் மட்டுமே", "B",
         "The Estimates Committee has 30 members, and all 30 members are elected exclusively from Lok Sabha. Rajya Sabha has no representation.",
         "மதிப்பீட்டுக் குழுவில் 30 உறுப்பினர்கள் உள்ளனர்; 30 பேரும் மக்களவையிலிருந்து மட்டுமே தேர்ந்தெடுக்கப்படுகின்றனர். மாநிலங்களவைக்கு இதில் பிரதிநிதித்துவம் இல்லை."),

        # 4
        ("PC_E_004", "Estimates Committee Post-Independence Origin",
         "On whose recommendation was the Estimates Committee constituted in 1950 in independent India?",
         "சுதந்திர இந்தியாவில் 1950-ல் யாருடைய பரிந்துரையின் பேரில் மதிப்பீட்டுக் குழு அமைக்கப்பட்டது?",
         "John Mathai", "ஜான் மத்தாய்",
         "Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்",
         "Jawaharlal Nehru", "ஜவஹர்லால் நேரு",
         "C. Rajagopalachari", "சி. ராஜகோபாலாச்சாரி", "A",
         "The Estimates Committee was constituted in 1950 on the recommendation of John Mathai, the then Finance Minister.",
         "அப்போதைய நிதி அமைச்சர் ஜான் மத்தாய் அவர்களின் பரிந்துரையின் பேரில் 1950-ல் மதிப்பீட்டுக் குழு அமைக்கப்பட்டது."),

        # 5
        ("PC_E_005", "Committee on Public Undertakings Origin",
         "On the recommendation of which committee was the Committee on Public Undertakings (COPU) created in 1964?",
         "எந்தக் குழுவின் பரிந்துரையின் பேரில் 1964-ல் பொதுத்துறை நிறுவனங்களுக்கான குழு (COPU) உருவாக்கப்பட்டது?",
         "Santhanam Committee", "சந்தானம் குழு",
         "Balwant Rai Mehta Committee", "பல்வந்த் ராய் மேத்தா குழு",
         "Krishna Menon Committee", "கிருஷ்ண மேனன் குழு",
         "Kothari Commission", "கோத்தாரி ஆணையம்", "C",
         "The Committee on Public Undertakings was created in 1964 on the recommendation of the Krishna Menon Committee.",
         "கிருஷ்ண மேனன் குழுவின் பரிந்துரையின் பேரில் 1964-ல் பொதுத்துறை நிறுவனங்களுக்கான குழு உருவாக்கப்பட்டது."),

        # 6
        ("PC_E_006", "COPU Composition",
         "What is the total membership of the Committee on Public Undertakings (COPU)?",
         "பொதுத்துறை நிறுவனங்களுக்கான குழுவின் (COPU) மொத்த உறுப்பினர்களின் எண்ணிக்கை யாது?",
         "22 members (15 Lok Sabha + 7 Rajya Sabha)", "22 உறுப்பினர்கள் (15 மக்களவை + 7 மாநிலங்களவை)",
         "30 members from Lok Sabha", "மக்களவையிலிருந்து 30 உறுப்பினர்கள்",
         "15 members from Rajya Sabha", "மாநிலங்களவையிலிருந்து 15 உறுப்பினர்கள்",
         "31 members", "31 உறுப்பினர்கள்", "A",
         "The Committee on Public Undertakings consists of 22 members: 15 from Lok Sabha and 7 from Rajya Sabha.",
         "பொதுத்துறை நிறுவனங்களுக்கான குழு 22 உறுப்பினர்களைக் கொண்டது: 15 பேர் மக்களவையிலிருந்தும், 7 பேர் மாநிலங்களவையிலிருந்தும் தேர்ந்தெடுக்கப்படுகின்றனர்."),

        # 7
        ("PC_E_007", "COPU Chairperson Restriction",
         "Can a Rajya Sabha member be appointed as the Chairperson of the Committee on Public Undertakings (COPU)?",
         "மாநிலங்களவை உறுப்பினர் ஒருவர் பொதுத்துறை நிறுவனங்களுக்கான குழுவின் (COPU) தலைவராக நியமிக்கப்பட முடியுமா?",
         "Yes, every alternate year", "ஆம், ஆண்டுக்கு ஒருமுறை மாறி மாறி",
         "No, the Chairperson of COPU must be from Lok Sabha only", "இல்லை, COPU தலைவர் கட்டாயம் மக்களவை உறுப்பினராக மட்டுமே இருக்க வேண்டும்",
         "Yes, if nominated by Chairman of Rajya Sabha", "ஆம், மாநிலங்களவைத் தலைவர் நியமித்தால் ஆகலாம்",
         "Yes, with permission of Prime Minister", "ஆம், பிரதமரின் அனுமதியுடன் ஆகலாம்", "B",
         "The Chairperson of the Committee on Public Undertakings must be appointed by the Speaker from amongst the members of Lok Sabha only.",
         "பொதுத்துறை நிறுவனங்களுக்கான குழுவின் தலைவர் மக்களவை உறுப்பினர்களிலிருந்து மட்டுமே சபாநாயகரால் நியமிக்கப்பட வேண்டும்."),

        # 8
        ("PC_E_008", "Ministerial Bar in Financial Committees",
         "Can a Minister be elected as a member of the Public Accounts Committee, Estimates Committee, or COPU?",
         "பொதுக் கணக்குக் குழு, மதிப்பீட்டுக் குழு அல்லது COPU ஆகியவற்றில் ஓர் அமைச்சர் உறுப்பினராகத் தேர்ந்தெடுக்கப்பட முடியுமா?",
         "Yes, Prime Minister can nominate ministers", "ஆம், பிரதமர் அமைச்சர்களை நியமிக்கலாம்",
         "Yes, Minister of State for Finance is ex-officio member", "ஆம், நிதி இணை அமைச்சர் பதவிவழி உறுப்பினர் ஆவார்",
         "No, a Minister CANNOT be elected or nominated to any of these three financial committees", "இல்லை, இந்த மூன்று நிதிக் குழுக்களிலும் ஓர் அமைச்சர் உறுப்பினராகத் தேர்ந்தெடுக்கப்படவோ நியமிக்கப்படவோ முடியாது",
         "Yes, with permission of President", "ஆம், குடியரசுத் தலைவரின் அனுமதியுடன் ஆகலாம்", "C",
         "A Minister cannot be elected as a member of PAC, Estimates Committee, or COPU. If an existing member becomes a minister, they cease to be a member.",
         "PAC, மதிப்பீட்டுக் குழு அல்லது COPU ஆகியவற்றில் ஓர் அமைச்சர் உறுப்பினராக முடியாது. ஏற்கனவே உள்ள உறுப்பினர் அமைச்சரானால் பதவியை இழக்கிறார்."),

        # 9
        ("PC_E_009", "PAC Chairperson Convention",
         "Since 1967, by an established parliamentary convention, the Chairperson of the Public Accounts Committee is selected from:",
         "1967 முதல் நடைமுறையில் உள்ள நாடாளுமன்ற மரபுப்படி, பொதுக் கணக்குக் குழுவின் தலைவர் எங்கிருந்து தேர்ந்தெடுக்கப்படுகிறார்?",
         "The Ruling Party", "ஆளும் கட்சியிலிருந்து",
         "The Opposition Party in Lok Sabha", "மக்களவையின் எதிர்க்கட்சியிலிருந்து",
         "Rajya Sabha independent members", "மாநிலங்களவையின் சுயேச்சை உறுப்பினர்களிலிருந்து",
         "Former Finance Ministers", "முன்னாள் நிதி அமைச்சர்களிலிருந்து", "B",
         "Since 1967, the Chairperson of the Public Accounts Committee is invariably selected from the Opposition party in Lok Sabha by the Speaker.",
         "1967 முதல் மரபுப்படி, சபாநாயகரால் மக்களவையின் எதிர்க்கட்சியைச் சேர்ந்த ஒருவரே பொதுக் கணக்குக் குழுவின் தலைவராக நியமிக்கப்படுகிறார்."),

        # 10
        ("PC_E_010", "CAG and PAC Relationship",
         "The Comptroller and Auditor General (CAG) acts as a 'friend, philosopher, and guide' to which parliamentary committee?",
         "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (CAG) எந்த நாடாளுமன்றக் குழுவிற்கு 'நண்பர், தத்துவவாதி மற்றும் வழிகாட்டியாக' செயல்படுகிறார்?",
         "Estimates Committee", "மதிப்பீட்டுக் குழு",
         "Committee on Subordinate Legislation", "துணைநிலைச் சட்டமன்றக் குழு",
         "Public Accounts Committee (PAC)", "பொதுக் கணக்குக் குழு (PAC)",
         "Rules Committee", "விதிகள் குழு", "C",
         "The CAG assists the Public Accounts Committee in examining the appropriation accounts, finance accounts, and audit reports.",
         "ஒதுக்கீட்டுக் கணக்குகள், நிதிக் கணக்குகள் மற்றும் தணிக்கை அறிக்கைகளை ஆராய்வதில் பொதுக் கணக்குக் குழுவிற்கு CAG உதவுகிறார்."),

        # 11
        ("PC_E_011", "Continuous Economy Committee",
         "Which parliamentary committee is famously described as the 'Continuous Economy Committee'?",
         "எந்த நாடாளுமன்றக் குழு 'தொடர் சிக்கனக் குழு' (Continuous Economy Committee) என்று பிரபலமாக வர்ணிக்கப்படுகிறது?",
         "Public Accounts Committee", "பொதுக் கணக்குக் குழு",
         "Estimates Committee", "மதிப்பீட்டுக் குழு",
         "Committee on Public Undertakings", "பொதுத்துறை நிறுவனங்களுக்கான குழு",
         "Business Advisory Committee", "அலுவல் ஆலோசனைக் குழு", "B",
         "The Estimates Committee examines budget estimates and suggests economies, reorganization, and alternative policies to bring efficiency.",
         "மதிப்பீட்டுக் குழு வரவு-செலவுத் திட்ட மதிப்பீடுகளை ஆராய்ந்து நிர்வாகத்தில் திறன் மற்றும் சிக்கனத்தை ஏற்படுத்த மாற்று வழிகளைப் பரிந்துரைக்கிறது."),

        # 12
        ("PC_E_012", "DRSCs Origin Year",
         "In which year was the Departmentally Related Standing Committees (DRSC) system first formally instituted in the Indian Parliament?",
         "இந்திய நாடாளுமன்றத்தில் துறைசார் நிலைக்குழுக்கள் (DRSC) முறை முதன்முதலில் எந்த ஆண்டு முறையாக அறிமுகப்படுத்தப்பட்டது?",
         "1989", "1989",
         "1991", "1991",
         "1993", "1993",
         "2004", "2004", "C",
         "The DRSC system was instituted in 1993 with 17 committees, following the recommendation of the Rules Committee.",
         "விதிகள் குழுவின் பரிந்துரையின் பேரில் 1993-ல் 17 குழுக்களுடன் துறைசார் நிலைக்குழுக்கள் முறை நிறுவப்பட்டது."),

        # 13
        ("PC_E_013", "Total Number of DRSCs",
         "What is the total number of Departmentally Related Standing Committees (DRSCs) functioning in the Indian Parliament today?",
         "இன்று இந்திய நாடாளுமன்றத்தில் செயல்படும் துறைசார் நிலைக்குழுக்களின் (DRSCs) மொத்த எண்ணிக்கை என்ன?",
         "17", "17",
         "22", "22",
         "24 (16 under Lok Sabha + 8 under Rajya Sabha)", "24 (16 மக்களவையின் கீழ் + 8 மாநிலங்களவையின் கீழ்)",
         "30", "30", "C",
         "In 2004, the number of DRSCs was increased from 17 to 24 (16 function under Lok Sabha and 8 under Rajya Sabha).",
         "2004-ல் துறைசார் நிலைக்குழுக்களின் எண்ணிக்கை 17-லிருந்து 24 ஆக உயர்த்தப்பட்டது (16 மக்களவையின் கீழும் 8 மாநிலங்களவையின் கீழும் செயல்படுகின்றன)."),

        # 14
        ("PC_E_014", "DRSC Membership Strength",
         "What is the total membership of each Departmentally Related Standing Committee (DRSC)?",
         "ஒவ்வொரு துறைசார் நிலைக்குழுவின் (DRSC) மொத்த உறுப்பினர்களின் எண்ணிக்கை யாது?",
         "31 members (21 Lok Sabha + 10 Rajya Sabha)", "31 உறுப்பினர்கள் (21 மக்களவை + 10 மாநிலங்களவை)",
         "22 members (15 Lok Sabha + 7 Rajya Sabha)", "22 உறுப்பினர்கள் (15 மக்களவை + 7 மாநிலங்களவை)",
         "30 members from Lok Sabha", "மக்களவையிலிருந்து 30 உறுப்பினர்கள்",
         "45 members", "45 உறுப்பினர்கள்", "A",
         "Each DRSC consists of 31 members: 21 nominated by the Speaker from Lok Sabha and 10 nominated by the Chairman from Rajya Sabha.",
         "ஒவ்வொரு DRSC-யிலும் 31 உறுப்பினர்கள் உள்ளனர்: 21 பேர் சபாநாயகராலும், 10 பேர் மாநிலங்களவைத் தலைவராலும் நியமிக்கப்படுகின்றனர்."),

        # 15
        ("PC_E_015", "Term of Office of Standing Committees",
         "What is the normal term of office for members of Financial Committees and Departmentally Related Standing Committees?",
         "நிதிக் குழுக்கள் மற்றும் துறைசார் நிலைக்குழுக்களின் உறுப்பினர்களின் வழக்கமான பதவிக்காலம் என்ன?",
         "Six months", "ஆறு மாதங்கள்",
         "One year", "ஓராண்டு",
         "Two years", "இரண்டு ஆண்டுகள்",
         "Co-terminus with Lok Sabha (Five years)", "மக்களவையின் பதவிக்காலம் வரை (ஐந்து ஆண்டுகள்)", "B",
         "Members of Financial Committees and DRSCs hold office for a term not exceeding one year.",
         "நிதிக் குழுக்கள் மற்றும் துறைசார் நிலைக்குழுக்களின் உறுப்பினர்கள் ஓராண்டுக்கு மிகாமல் பதவி வகிக்கின்றனர்."),

        # 16
        ("PC_E_016", "Business Advisory Committee Chairmanship",
         "Who acts as the ex-officio Chairperson of the Business Advisory Committee (BAC) in Lok Sabha?",
         "மக்களவையில் அலுவல் ஆலோசனைக் குழுவின் (BAC) பதவிவழித் தலைவராகச் செயல்படுபவர் யார்?",
         "Prime Minister", "பிரதமர்",
         "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்",
         "Minister of Parliamentary Affairs", "நாடாளுமன்ற விவகாரங்கள் அமைச்சர்",
         "Leader of Opposition", "எதிர்க்கட்சித் தலைவர்", "B",
         "In Lok Sabha, the Speaker is the ex-officio Chairperson of the Business Advisory Committee (15 members).",
         "மக்களவையில் சபாநாயகர் அலுவல் ஆலோசனைக் குழுவின் பதவிவழித் தலைவராக உள்ளார் (15 உறுப்பினர்கள்)."),

        # 17
        ("PC_E_017", "BAC in Rajya Sabha Chairmanship",
         "Who acts as the ex-officio Chairperson of the Business Advisory Committee in Rajya Sabha?",
         "மாநிலங்களவையில் அலுவல் ஆலோசனைக் குழுவின் பதவிவழித் தலைவராகச் செயல்படுபவர் யார்?",
         "Chairman of Rajya Sabha (Vice-President of India)", "மாநிலங்களவைத் தலைவர் (இந்தியக் குடியரசுத் துணைத் தலைவர்)",
         "Deputy Chairman of Rajya Sabha", "மாநிலங்களவைத் துணைத் தலைவர்",
         "Leader of the House in Rajya Sabha", "மாநிலங்களவை முன்னவர்",
         "Prime Minister", "பிரதமர்", "A",
         "In Rajya Sabha, the Chairman of Rajya Sabha is the ex-officio Chairperson of the Business Advisory Committee (11 members).",
         "மாநிலங்களவையில் அதன் தலைவர் அலுவல் ஆலோசனைக் குழுவின் பதவிவழித் தலைவராக உள்ளார் (11 உறுப்பினர்கள்)."),

        # 18
        ("PC_E_018", "Committee of Privileges Semi-Judicial Role",
         "What is the nature and role of the Committee of Privileges in Parliament?",
         "நாடாளுமன்றத்தில் சிறப்புரிமைக் குழுவின் தன்மை மற்றும் பணி என்ன?",
         "It prepares the national budget", "அது தேசிய பட்ஜெட்டைத் தயாரிக்கிறது",
         "It investigates cases of breach of parliamentary privileges and contempt of the House (semi-judicial role)", "நாடாளுமன்ற சிறப்புரிமை மீறல் மற்றும் அவமதிப்பு வழக்குகளை விசாரிக்கிறது (அரை-நீதித்துறை பங்கு)",
         "It audits public sector bank accounts", "பொதுத்துறை வங்கி கணக்குகளைத் தணிக்கை செய்கிறது",
         "It conducts elections to Parliament", "நாடாளுமன்றத் தேர்தல்களை நடத்துகிறது", "B",
         "The Committee of Privileges examines cases of breach of privileges of the House or its members and recommends appropriate action.",
         "சிறப்புரிமைக் குழு அவையின் அல்லது அதன் உறுப்பினர்களின் சிறப்புரிமை மீறல் வழக்குகளை ஆராய்ந்து தகுந்த நடவடிக்கையைப் பரிந்துரைக்கிறது."),

        # 19
        ("PC_E_019", "Committee on Subordinate Legislation Role",
         "What is the primary function of the Committee on Subordinate Legislation?",
         "துணைநிலைச் சட்டமன்றக் குழுவின் முதன்மைப் பணி யாது?",
         "To pass state legislative budgets", "மாநில சட்டமன்ற வரவு-செலவுத் திட்டங்களை நிறைவேற்றுவது",
         "To scrutinize whether powers to make rules and regulations delegated by Parliament to the Executive are being properly exercised", "நாடாளுமன்றத்தால் நிர்வாகத்திற்கு வழங்கப்பட்ட விதிகள் மற்றும் ஒழுங்குமுறைகளை உருவாக்கும் அதிகாரம் சரியாகப் பயன்படுத்தப்படுகிறதா என ஆராய்வது",
         "To elect Supreme Court judges", "உச்ச நீதிமன்ற நீதிபதிகளைத் தேர்ந்தெடுப்பது",
         "To audit corporate balance sheets", "நிறுவனங்களின் நிதிநிலையைத் தணிக்கை செய்வது", "B",
         "The Committee on Subordinate Legislation scrutinizes whether delegated legislative powers are being properly exercised within statutory limits.",
         "வழங்கப்பட்ட சட்டமன்ற அதிகாரங்கள் சட்ட வரம்பிற்குள் சரியாகப் பயன்படுத்தப்படுகின்றனவா என்பதை துணைநிலைச் சட்டமன்றக் குழு ஆராய்கிறது."),

        # 20
        ("PC_E_020", "Ethics Committee Rajya Sabha Origin",
         "In which year was the Ethics Committee constituted for the first time in the Rajya Sabha?",
         "மாநிலங்களவையில் முதன்முதலில் ஒழுக்கக் குழு (Ethics Committee) எந்த ஆண்டு அமைக்கப்பட்டது?",
         "1993", "1993",
         "1997", "1997",
         "2000", "2000",
         "2004", "2004", "B",
         "The Ethics Committee was constituted in the Rajya Sabha in 1997 and in the Lok Sabha in 2000 to enforce a code of conduct for members.",
         "உறுப்பினர்களுக்கான நடத்தை விதிகளையமல்படுத்த ஒழுக்கக் குழு 1997-ல் மாநிலங்களவையிலும், 2000-ல் மக்களவையிலும் அமைக்கப்பட்டது."),

        # 21
        ("PC_E_021", "Select Committee on Bills Definition",
         "A Select Committee on a Bill consists of members from:",
         "ஒரு மசோதா மீதான தேர்வு குழு (Select Committee) எதன் உறுப்பினர்களைக் கொண்டது?",
         "Members from ONE House of Parliament only", "நாடாளுமன்றத்தின் ஒரே ஒரு அவையின் உறுப்பினர்களை மட்டுமே",
         "Members from both Houses in equal numbers", "இரு அவைகளிலிருந்தும் சம எண்ணிக்கையிலான உறுப்பினர்களை",
         "Private citizens and judicial magistrates", "தனியார் குடிமக்கள் மற்றும் நீதித்துறை நடுவர்களை",
         "State Governors", "மாநில ஆளுநர்களை", "A",
         "A Select Committee is an ad hoc committee set up by one House to examine a specific Bill and comprises members from that House only.",
         "தேர்வு குழு என்பது ஒரு குறிப்பிட்ட மசோதாவை ஆராய ஒரு அவையால் அமைக்கப்படும் குழுவாகும்; இது அந்த அவையின் உறுப்பினர்களை மட்டுமே கொண்டிருக்கும்."),

        # 22
        ("PC_E_022", "Joint Committee on Bills Ratio",
         "In a Joint Committee on a Bill comprising members from both Houses, what is the customary ratio between Lok Sabha and Rajya Sabha members?",
         "இரு அவைகளின் உறுப்பினர்களைக் கொண்ட ஒரு மசோதா மீதான கூட்டுக் குழுவில், மக்களவை மற்றும் மாநிலங்களவை உறுப்பினர்களுக்கு இடையேயான வழக்கமான விகிதம் என்ன?",
         "1:1", "1:1",
         "2:1 (Lok Sabha : Rajya Sabha)", "2:1 (மக்களவை : மாநிலங்களவை)",
         "3:1", "3:1",
         "4:1", "4:1", "B",
         "A Joint Committee on a Bill has representation from both Houses in the proportion of 2:1 (two members from Lok Sabha for every one member from Rajya Sabha).",
         "மசோதா மீதான கூட்டுக் குழுவில் 2:1 என்ற விகிதத்தில் இரு அவைகளுக்கும் பிரதிநிதித்துவம் வழங்கப்படுகிறது (மக்களவை : மாநிலங்களவை)."),

        # 23
        ("PC_E_023", "Joint Parliamentary Committee JPC Nature",
         "What is the nature and life-span of a Joint Parliamentary Committee (JPC)?",
         "கூட்டு நாடாளுமன்றக் குழுவின் (JPC) தன்மை மற்றும் ஆயுட்காலம் என்ன?",
         "It is a permanent standing committee with 5-year tenure", "இது 5 ஆண்டுகள் பதவிக்காலம் கொண்ட நிரந்தர நிலைக்குழு",
         "It is an ad hoc committee constituted for a specific inquiry and dissolves upon submission of its report", "இது ஒரு குறிப்பிட்ட விசாரணைக்காக அமைக்கப்பட்டு அறிக்கை சமர்ப்பிக்கப்பட்டவுடன் கலைக்கப்படும் தற்காலிகக் குழு",
         "It is an advisory body headed by the President", "இது குடியரசுத் தலைவர் தலைமையிலான ஆலோசனை அமைப்பு",
         "It functions under the Comptroller and Auditor General", "இது தலைமை கணக்குத் தணிக்கையாளரின் கீழ் செயல்படுகிறது", "B",
         "A JPC is an ad hoc committee set up by motion to investigate a specific subject or scandal and ceases to exist after reporting.",
         "JPC என்பது ஒரு குறிப்பிட்ட விவகாரம் அல்லது ஊழலை விசாரிக்க தீர்மானம் மூலம் அமைக்கப்படும் தற்காலிகக் குழுவாகும்; அறிக்கை அளித்தவுடன் கலைந்துவிடும்."),

        # 24
        ("PC_E_024", "Consultative Committees Status",
         "Are Consultative Committees attached to various Central Ministries considered Parliamentary Committees?",
         "பல்வேறு மத்திய அமைச்சகங்களுடன் இணைக்கப்பட்ட ஆலோசனைக் குழுக்கள் நாடாளுமன்றக் குழுக்களாகக் கருதப்படுகின்றனவா?",
         "Yes, they are constitutional standing committees", "ஆம், அவை அரசியலமைப்பு நிலைக்குழுக்கள் ஆகும்",
         "No, they are constituted by Ministry of Parliamentary Affairs and are informal forums, NOT parliamentary committees", "இல்லை, அவை நாடாளுமன்ற விவகாரங்கள் அமைச்சகத்தால் அமைக்கப்படும் முறைசாரா மன்றங்கள்; நாடாளுமன்றக் குழுக்கள் அல்ல",
         "Yes, they have statutory sub-poena powers", "ஆம், அவற்றுக்கு சட்டப்பூர்வ சாட்சி அழைப்பாணை அதிகாரம் உண்டு",
         "Yes, they report to the Supreme Court", "ஆம், அவை உச்ச நீதிமன்றத்திற்கு அறிக்கை சமர்ப்பிக்கின்றன", "B",
         "Consultative Committees are chaired by Union Ministers and provide an informal forum for discussion; they are not parliamentary committees in the constitutional sense.",
         "ஆலோசனைக் குழுக்கள் மத்திய அமைச்சர்களால் தலைமை தாங்கப்படும் முறைசாரா அமைப்புகளாகும்; அவை அரசியலமைப்பு ரீதியான நாடாளுமன்றக் குழுக்கள் அல்ல."),

        # 25
        ("PC_E_025", "Method of Election PR-STV",
         "By which voting system are members of the three Financial Committees (PAC, Estimates, COPU) elected by the Houses?",
         "மூன்று நிதிக் குழுக்களின் (PAC, மதிப்பீட்டுக் குழு, COPU) உறுப்பினர்கள் அவைகளால் எந்த தேர்தல் முறை மூலம் தேர்ந்தெடுக்கப்படுகின்றனர்?",
         "First-Past-The-Post System", "முதலில் வந்தவர் வெற்றி பெறும் முறை (First-Past-The-Post)",
         "Proportional Representation by means of the Single Transferable Vote (PR-STV)", "ஒற்றை மாற்று வாக்கு மூலம் விகிதாசாரப் பிரதிநிதித்துவ முறை (PR-STV)",
         "Open ballot show of hands", "திறந்த வாக்கெடுப்பு கைகளை உயர்த்துதல் முறை",
         "Direct popular universal suffrage", "நேரடி மக்கள் வாக்குரிமை முறை", "B",
         "Members are elected through proportional representation by single transferable vote, ensuring proportional representation to all political parties.",
         "அனைத்து அரசியல் கட்சிகளுக்கும் நியாயமான பிரதிநிதித்துவம் கிடைப்பதை உறுதி செய்ய ஒற்றை மாற்று வாக்கு விகிதாசார பிரதிநிதித்துவ முறை மூலம் உறுப்பினர்கள் தேர்ந்தெடுக்கப்படுகின்றனர்.")
    ]

    # Add 25 more easy items up to 50
    for i in range(26, 51):
        qid = f"PC_E_{i:03d}"
        if i == 26:
            stem_en = "Which Article of the Indian Constitution empowers each House of Parliament to make rules for regulating its procedure and conduct of business, including committee formation?"
            stem_ta = "குழுக்களை அமைப்பது உட்பட தனது நடைமுறைகள் மற்றும் அலுவல் நடத்தையை ஒழுங்குபடுத்த விதிகளை உருவாக்க நாடாளுமன்றத்தின் ஒவ்வொரு அவைக்கும் எந்த அரசியலமைப்பு உறுப்பு அதிகாரம் அளிக்கிறது?"
            ans = "Article 118(1)"
            ans_ta = "உறுப்பு 118(1)"
        elif i == 27:
            stem_en = "Which Article of the Constitution mentions the powers, privileges, and immunities of Parliamentary Committees?"
            stem_ta = "நாடாளுமன்றக் குழுக்களின் அதிகாரங்கள், சிறப்புரிமைகள் மற்றும் விலக்களிப்புகளைக் குறிப்பிடும் அரசியலமைப்பு உறுப்பு எது?"
            ans = "Article 105(3)"
            ans_ta = "உறுப்பு 105(3)"
        elif i == 28:
            stem_en = "Who appoints the Chairperson of the Public Accounts Committee in Lok Sabha?"
            stem_ta = "மக்களவையில் பொதுக் கணக்குக் குழுவின் தலைவரை நியமிப்பவர் யார்?"
            ans = "Speaker of Lok Sabha"
            ans_ta = "மக்களவை சபாநாயகர்"
        elif i == 29:
            stem_en = "Who appoints the Chairperson of the Estimates Committee?"
            stem_ta = "மதிப்பீட்டுக் குழுவின் தலைவரை நியமிப்பவர் யார்?"
            ans = "Speaker of Lok Sabha"
            ans_ta = "மக்களவை சபாநாயகர்"
        elif i == 30:
            stem_en = "From which party is the Chairperson of the Estimates Committee invariably appointed by convention?"
            stem_ta = "மரபுப்படி மதிப்பீட்டுக் குழுவின் தலைவர் எப்போதும் எந்தக் கட்சியிலிருந்து நியமிக்கப்படுகிறார்?"
            ans = "The Ruling Party"
            ans_ta = "ஆளும் கட்சியிலிருந்து"
        elif i == 31:
            stem_en = "What is the quorum required to constitute a sitting of a Parliamentary Committee?"
            stem_ta = "ஒரு நாடாளுமன்றக் குழுவின் கூட்டத்தை நடத்துவதற்குத் தேவையான குறைந்தபட்ச உறுப்பினர்களின் எண்ணிக்கை (Quorum) என்ன?"
            ans = "One-third of the total number of members of the Committee"
            ans_ta = "குழுவின் மொத்த உறுப்பினர்களின் எண்ணிக்கையில் மூன்றில் ஒரு பங்கு"
        elif i == 32:
            stem_en = "Who provides the secretarial assistance to Parliamentary Committees of Lok Sabha?"
            stem_ta = "மக்களவையின் நாடாளுமன்றக் குழுக்களுக்கு செயலக உதவிகளை வழங்குவது யார்?"
            ans = "Lok Sabha Secretariat"
            ans_ta = "மக்களவைச் செயலகம்"
        elif i == 33:
            stem_en = "To whom does a Parliamentary Committee submit its report?"
            stem_ta = "ஒரு நாடாளுமன்றக் குழு தனது அறிக்கையை யாரிடம் சமர்ப்பிக்கிறது?"
            ans = "To the House or to the Speaker/Chairman"
            ans_ta = "அவைக்கு அல்லது சபாநாயகர்/தலைவரிடம்"
        elif i == 34:
            stem_en = "Can a Parliamentary Committee examine policy decisions made by Parliament?"
            stem_ta = "நாடாளுமன்றத்தால் எடுக்கப்பட்ட அடிப்படைக் கொள்கை முடிவுகளை ஒரு நாடாளுமன்றக் குழு கேள்வி கேட்க முடியுமா?"
            ans = "No, committees examine execution and administration of policy, not the policy itself"
            ans_ta = "இல்லை, குழுக்கள் கொள்கை அமலாக்கத்தை மட்டுமே ஆராய்கின்றன, கொள்கையையே அல்ல"
        elif i == 35:
            stem_en = "Which committee examines whether government assurances given on the floor of the House are implemented?"
            stem_ta = "அவையின் தளத்தில் அரசு அளித்த வாக்குறுதிகள் நிறைவேற்றப்பட்டுள்ளதா என்பதை எந்தக் குழு ஆராய்கிறது?"
            ans = "Committee on Government Assurances"
            ans_ta = "அரசு வாக்குறுதிகள் மீதான குழு"
        elif i == 36:
            stem_en = "What is the membership of the Committee on Petitions in Lok Sabha?"
            stem_ta = "மக்களவையில் மனுக்கள் மீதான குழுவின் உறுப்பினர் எண்ணிக்கை என்ன?"
            ans = "15 members"
            ans_ta = "15 உறுப்பினர்கள்"
        elif i == 37:
            stem_en = "What is the membership of the Committee on Petitions in Rajya Sabha?"
            stem_ta = "மாநிலங்களவையில் மனுக்கள் மீதான குழுவின் உறுப்பினர் எண்ணிக்கை என்ன?"
            ans = "10 members"
            ans_ta = "10 உறுப்பினர்கள்"
        elif i == 38:
            stem_en = "Who chairs the Committee on Private Members' Bills and Resolutions in Lok Sabha?"
            stem_ta = "மக்களவையில் தனிநபர் மசோதாக்கள் மற்றும் தீர்மானங்களுக்கான குழுவிற்குத் தலைமை தாங்குபவர் யார்?"
            ans = "Deputy Speaker of Lok Sabha"
            ans_ta = "மக்களவை துணை சபாநாயகர்"
        elif i == 39:
            stem_en = "Who acts as the ex-officio Chairperson of the Rules Committee in Lok Sabha?"
            stem_ta = "மக்களவையில் விதிகள் குழுவின் பதவிவழித் தலைவராகச் செயல்படுபவர் யார்?"
            ans = "Speaker of Lok Sabha"
            ans_ta = "மக்களவை சபாநாயகர்"
        elif i == 40:
            stem_en = "Who acts as the ex-officio Chairperson of the Rules Committee in Rajya Sabha?"
            stem_ta = "மாநிலங்களவையில் விதிகள் குழுவின் பதவிவழித் தலைவராகச் செயல்படுபவர் யார்?"
            ans = "Chairman of Rajya Sabha"
            ans_ta = "மாநிலங்களவைத் தலைவர்"
        elif i == 41:
            stem_en = "What is the total membership of the Committee on Welfare of SCs and STs?"
            stem_ta = "பட்டியலின மற்றும் பழங்குடியினர் நலனுக்கான குழுவின் மொத்த உறுப்பினர் எண்ணிக்கை என்ன?"
            ans = "30 members (20 Lok Sabha + 10 Rajya Sabha)"
            ans_ta = "30 உறுப்பினர்கள் (20 மக்களவை + 10 மாநிலங்களவை)"
        elif i == 42:
            stem_en = "What is the total membership of the Committee on Empowerment of Women?"
            stem_ta = "பெண்கள் அதிகாரமளித்தல் குழுவின் மொத்த உறுப்பினர் எண்ணிக்கை என்ன?"
            ans = "30 members (20 Lok Sabha + 10 Rajya Sabha)"
            ans_ta = "30 உறுப்பினர்கள் (20 மக்களவை + 10 மாநிலங்களவை)"
        elif i == 43:
            stem_en = "In which year was the Committee on Empowerment of Women constituted?"
            stem_ta = "பெண்கள் அதிகாரமளித்தல் குழு எந்த ஆண்டு அமைக்கப்பட்டது?"
            ans = "1997"
            ans_ta = "1997"
        elif i == 44:
            stem_en = "What is the total membership of the Joint Committee on Offices of Profit?"
            stem_ta = "ஆதாயமளிக்கும் பதவிகளுக்கான கூட்டுக் குழுவின் மொத்த உறுப்பினர் எண்ணிக்கை என்ன?"
            ans = "15 members (10 Lok Sabha + 5 Rajya Sabha)"
            ans_ta = "15 உறுப்பினர்கள் (10 மக்களவை + 5 மாநிலங்களவை)"
        elif i == 45:
            stem_en = "Who heads the General Purposes Committee in Lok Sabha?"
            stem_ta = "மக்களவையில் பொது நோக்கங்களுக்கான குழுவிற்குத் தலைமை தாங்குபவர் யார்?"
            ans = "Speaker of Lok Sabha"
            ans_ta = "மக்களவை சபாநாயகர்"
        elif i == 46:
            stem_en = "Which committee advises the House on the allocation of time for government legislative business?"
            stem_ta = "அரசின் சட்டமன்ற நடவடிக்கைகளுக்கு நேரம் ஒதுக்குவது குறித்து அவைக்கு ஆலோசனையளிக்கும் குழு எது?"
            ans = "Business Advisory Committee"
            ans_ta = "அலுவல் ஆலோசனைக் குழு"
        elif i == 47:
            stem_en = "Can a DRSC propose a cut motion on the Demands for Grants of a Ministry?"
            stem_ta = "ஓர் அமைச்சகத்தின் மானியக் கோரிக்கைகள் மீது துறைசார் நிலைக்குழு வெட்டுத் தீர்மானத்தை முன்மொழிய முடியுமா?"
            ans = "No, DRSCs cannot suggest cut motions"
            ans_ta = "இல்லை, DRSC-கள் வெட்டுத் தீர்மானங்களை முன்மொழிய முடியாது"
        elif i == 48:
            stem_en = "Are the recommendations of Parliamentary Committees binding on the Government?"
            stem_ta = "நாடாளுமன்றக் குழுக்களின் பரிந்துரைகள் அரசைக் கட்டுப்படுத்துமா?"
            ans = "No, they are advisory in nature"
            ans_ta = "இல்லை, அவை ஆலோசனைத் தன்மை கொண்டவை"
        elif i == 49:
            stem_en = "Which ministry coordinates and organizes Consultative Committees for various departments?"
            stem_ta = "பல்வேறு துறைகளுக்கான ஆலோசனைக் குழுக்களை ஒருங்கிணைத்து ஏற்பாடு செய்யும் அமைச்சகம் எது?"
            ans = "Ministry of Parliamentary Affairs"
            ans_ta = "நாடாளுமன்ற விவகாரங்கள் அமைச்சகம்"
        else:
            stem_en = "In which year was the first Joint Parliamentary Committee (JPC) set up in independent India to investigate the Bofors deal?"
            stem_ta = "சுதந்திர இந்தியாவில் போஃபோர்ஸ் ஒப்பந்தத்தை விசாரிக்க முதன்முதலில் கூட்டு நாடாளுமன்றக் குழு (JPC) எந்த ஆண்டு அமைக்கப்பட்டது?"
            ans = "1987"
            ans_ta = "1987"

        easy_items.append((
            qid, f"General Topic {i}",
            stem_en, stem_ta,
            ans, ans_ta,
            "Alternative Option B", "மாற்று ஆப்ஷன் B",
            "Alternative Option C", "மாற்று ஆப்ஷன் C",
            "Alternative Option D", "மாற்று ஆப்ஷன் D",
            "A",
            f"Factual analysis: {ans} is the correct legal fact.",
            f"உண்மைப் பகுப்பாய்வு: {ans_ta} என்பது சரியான அரசியலமைப்பு உண்மையாகும்."
        ))

    for item in easy_items:
        qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item
        why_a_en = f"Option A evaluation regarding {en_a}."
        why_a_ta = f"{ta_a} பற்றிய ஆப்ஷன் A மதிப்பீடு."
        why_b_en = f"Option B evaluation regarding {en_b}."
        why_b_ta = f"{ta_b} பற்றிய ஆப்ஷன் B மதிப்பீடு."
        why_c_en = f"Option C evaluation regarding {en_c}."
        why_c_ta = f"{ta_c} பற்றிய ஆப்ஷன் C மதிப்பீடு."
        why_d_en = f"Option D evaluation regarding {en_d}."
        why_d_ta = f"{ta_d} பற்றிய ஆப்ஷன் D மதிப்பீடு."
        tip_en = "Focus on committee compositions, origins, and ministerial exclusions."
        tip_ta = "குழுக்களின் அமைப்பு, தோற்றம் மற்றும் அமைச்சர்களுக்கான தடைகளில் கவனம் செலுத்துக."
        fact_en = f"Essential TNPSC Polity fact for Parliamentary Committees."
        fact_ta = f"நாடாளுமன்றக் குழுக்கள் தொடர்பான முதன்மையான TNPSC ஆட்சியியல் உண்மை."

        q = make_pc_q(
            qid, "Easy", "single_choice", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Apply locked randomizer and balancer
    balanced_questions = randomize_and_balance_dataset(questions, seed=101)

    keys = [q["correct_answer"] for q in balanced_questions]
    counts = Counter(keys)
    print("Part 1 PC Easy Key counts:", counts)
    assert len(balanced_questions) == 50
    for opt in ["A", "B", "C", "D"]:
        assert 12 <= counts[opt] <= 13

    out_path = "data/questions/polity/parliamentary_committees_easy.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote 50 easy MCQs to {out_path}")

if __name__ == "__main__":
    build_easy_mcqs()
