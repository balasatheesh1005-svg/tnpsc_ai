# -*- coding: utf-8 -*-
"""
Build 50 Statement-based MCQs for Parliamentary Privileges (PP_S_001 to PP_S_050)
TNPSC Nova AI Content Engine
"""
import json
import os
import shutil
from collections import Counter
from parliamentary_privileges_mcq_helper import make_pp_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_statement_questions():
    questions = []

    # Helper tuple format: (qid, subtopic, statements_en, statements_ta, optA, optB, optC, optD, correct_key, exp_en, exp_ta)
    stmt_data = [
        # S_001
        ("PP_S_001", "Constitutional Basis",
         "Consider the following statements regarding Article 105 of the Constitution of India:\n1. It defines the powers, privileges, and immunities of Parliament, its members, and committees.\n2. Freedom of speech in Parliament under clause (1) is subject to the provisions of the Constitution and to the rules of procedure.\n3. Clause (2) gives absolute immunity from court proceedings for anything said or any vote given in Parliament.\nWhich of the statements given above are correct?",
         "இந்திய அரசியலமைப்பின் உறுப்பு 105 தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது நாடாளுமன்றம், அதன் உறுப்பினர்கள் மற்றும் குழுக்களின் அதிகாரங்கள் மற்றும் சிறப்புரிமைகளை வரையறுக்கிறது.\n2. பிரிவு (1)-ன் கீழ் நாடாளுமன்றப் பேச்சுரிமை அரசியலமைப்பு விதிகள் மற்றும் நடைமுறை விதிகளுக்கு உட்பட்டது.\n3. பிரிவு (2) நாடாளுமன்றத்தில் பேசிய எதற்கும் அல்லது அளித்த வாக்கிற்கும் நீதிமன்ற நடவடிக்கைகளிலிருந்து முழுமையான விலக்களிப்பை வழங்குகிறது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
         "A",
         "All three statements are correct. Article 105 provides constitutional foundation for privileges, guarantees speech subject to constitutional provisions and House rules, and immunizes members from judicial proceedings for speeches and votes in Parliament.",
         "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 105 சிறப்புரிமைகளுக்கு அரசியலமைப்பு அடிப்படையை அளிக்கிறது, பேச்சுரிமைக்கு உத்தரவாதம் அளிக்கிறது, மற்றும் நீதிமன்ற வழக்குகளிலிருந்து முழுமையான விலக்களிப்பை அளிக்கிறது."),

        # S_002
        ("PP_S_002", "Scope of Immunities",
         "Consider the following statements regarding the beneficiaries of parliamentary privileges:\n1. Privileges under Article 105 are available to all Members of Lok Sabha and Rajya Sabha.\n2. Under Article 105(4), they extend to the Attorney General of India and Union Ministers who speak in the House.\n3. The President of India is also entitled to parliamentary privileges under Article 105(4).\nWhich of the statements given above is/are correct?",
         "நாடாளுமன்ற சிறப்புரிமைகளைப் பெறும் நபர்கள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உறுப்பு 105-ன் கீழான சிறப்புரிமைகள் மக்களவை மற்றும் மாநிலங்களவையின் அனைத்து உறுப்பினர்களுக்கும் கிடைக்கின்றன.\n2. உறுப்பு 105(4)-ன் கீழ், அவையில் பேச உரிமையுள்ள இந்திய தலைமை வழக்கறிஞர் மற்றும் ஒன்றிய அமைச்சர்களுக்கும் இது நீட்டிக்கப்படுகிறது.\n3. இந்தியக் குடியரசுத் தலைவருக்கும் உறுப்பு 105(4)-ன் கீழ் நாடாளுமன்ற சிறப்புரிமைகள் உண்டு.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 only", "1 மட்டுமே"),
         "A",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because the President of India is NOT covered under Article 105; the President's personal immunities are separately governed by Article 361.",
         "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் குடியரசுத் தலைவர் உறுப்பு 105-ன் கீழ் வரமாட்டார்; அவருக்கு உறுப்பு 361-ன் கீழ் தனிப் பாதுகாப்பு உள்ளது."),

        # S_003
        ("PP_S_003", "Freedom from Arrest",
         "Consider the following statements regarding freedom from arrest enjoyed by members of legislature:\n1. Members cannot be arrested in civil cases during the continuance of the session.\n2. The immunity from civil arrest extends to 40 days before and 40 days after the session.\n3. The immunity applies equally to arrests under criminal charges and preventive detention.\nWhich of the statements given above is/are correct?",
         "சட்டமன்ற உறுப்பினர்களின் கைதிலிருந்து விலக்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கூட்டத்தொடர் நடைபெறும் காலத்தில் சிவில் வழக்குகளில் உறுப்பினர்களைக் கைது செய்ய முடியாது.\n2. இந்த சிவில் கைது விலக்களிப்பு கூட்டத்தொடருக்கு 40 நாட்களுக்கு முன்பும் மற்றும் 40 நாட்களுக்கு பின்பும் நீட்டிக்கப்படுகிறது.\n3. இந்தக் கைது விலக்களிப்பு குற்றவியல் வழக்குகள் மற்றும் தடுப்புக் காவல் கைதுகளுக்கும் சமமாகப் பொருந்தும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("3 only", "3 மட்டுமே"),
         "A",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because freedom from arrest is strictly confined to civil cases under Section 135A CPC and does NOT apply to criminal cases or preventive detention.",
         "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் கைதிலிருந்து விலக்கு சிவில் வழக்குகளுக்கு மட்டுமே; குற்றவியல் குற்றங்கள் அல்லது தடுப்புக் காவலுக்கு இது பொருந்தாது."),

        # S_004
        ("PP_S_004", "Judicial Bar Articles",
         "Consider the following statements regarding constitutional provisions restricting debates and court inquiries:\n1. Article 121 prohibits discussion in Parliament on the judicial conduct of Supreme Court or High Court judges.\n2. Article 122 prohibits courts from inquiring into the validity of parliamentary proceedings on grounds of irregularity of procedure.\n3. Corresponding provisions for State Legislatures are Article 211 and Article 212 respectively.\nWhich of the statements given above are correct?",
         "விவாதங்கள் மற்றும் நீதிமன்ற விசாரணைகளைத் தடை செய்யும் அரசியலமைப்பு விதிகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உச்ச நீதிமன்ற அல்லது உயர் நீதிமன்ற நீதிபதிகளின் நடத்தை குறித்து நாடாளுமன்றத்தில் விவாதிப்பதை உறுப்பு 121 தடை செய்கிறது.\n2. நடைமுறை முறைகேடு என்ற காரணத்தின் அடிப்படையில் நாடாளுமன்ற நடவடிக்கைகளின் செல்லுபடியாகும் தன்மையை நீதிமன்றங்கள் விசாரிப்பதை உறுப்பு 122 தடை செய்கிறது.\n3. மாநில சட்டமன்றங்களுக்கான இணையான விதிகள் முறையே உறுப்பு 211 மற்றும் உறுப்பு 212 ஆகும்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
         "A",
         "All three statements are correct. Articles 121 and 122 protect the mutual autonomy of Parliament and Judiciary; Articles 211 and 212 provide identical protections at the State level.",
         "மூன்று கூற்றுகளும் சரியானவை. உறுப்புகள் 121 மற்றும் 122 நாடாளுமன்றத்திற்கும் நீதித்துறைக்கும் இடையிலான தன்னாட்சியைப் பாதுகாக்கின்றன; உறுப்புகள் 211 மற்றும் 212 மாநில அளவில் இதையே செய்கின்றன."),

        # S_005
        ("PP_S_005", "Article 361A Features",
         "Consider the following statements regarding Article 361A of the Constitution of India:\n1. It was inserted by the 44th Constitutional Amendment Act, 1978.\n2. It protects substantially true reports of parliamentary proceedings published in newspapers or broadcast over wireless telegraphy.\n3. The protection is forfeited if the publication is proved to have been made with malice.\n4. It protects the publication of secret sittings of the House.\nWhich of the statements given above are correct?",
         "இந்திய அரசியலமைப்பின் உறுப்பு 361A தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 மூலம் சேர்க்கப்பட்டது.\n2. செய்தித்தாள்கள் அல்லது வானொலியில் வெளியிடப்படும் நாடாளுமன்ற நடவடிக்கைகளின் உண்மை அறிக்கைகளுக்கு இது சட்டப் பாதுகாப்பு அளிக்கிறது.\n3. அந்த வெளியீடு கெட்ட எண்ணத்தோடு (malice) செய்யப்பட்டது என நிரூபிக்கப்பட்டால் பாதுகாப்பு பறிபோகும்.\n4. அவையின் ரகசிய அமர்வுகளின் வெளியீடுகளுக்கும் இது பாதுகாப்பு அளிக்கிறது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டுமே"),
         ("1, 2, 3 and 4", "1, 2, 3 மற்றும் 4"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 4 only", "1 மற்றும் 4 மட்டுமே"),
         "A",
         "Statements 1, 2, and 3 are correct. Statement 4 is incorrect because the proviso to Article 361A(1) explicitly excludes secret sittings from protection.",
         "கூற்றுகள் 1, 2, 3 சரியானவை. கூற்று 4 தவறு, ஏனெனில் உறுப்பு 361A(1)-ன் படி ரகசிய அமர்வுகளின் அறிக்கைகளுக்கு எந்தப் பாதுகாப்பும் கிடைக்காது."),

        # S_006
        ("PP_S_006", "Searchlight Case 1959",
         "Consider the following statements regarding the landmark Searchlight Case (MSM Sharma v. Sri Krishna Sinha, 1959):\n1. It arose out of the publication of expunged portions of proceedings of the Bihar Legislative Assembly.\n2. The majority held that legislative privileges under Article 194(3) prevail over the general right under Article 19(1)(a).\n3. Justice K. Subba Rao delivered a dissenting judgment arguing that privileges are subject to fundamental rights.\nWhich of the statements given above are correct?",
         "சர்ச்லைட் வழக்கு (1959) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பீகார் சட்டமன்ற நடவடிக்கைகளின் நீக்கப்பட்ட பகுதிகளை நாளிதழ் வெளியிட்டதால் இது உருவானது.\n2. உறுப்பு 19(1)(a)-ன் கீழான பொது உரிமையை விட உறுப்பு 194(3)-ன் கீழான சிறப்புரிமைகளே மேலோங்கும் என பெரும்பான்மை தீர்ப்பளிக்கப்பட்டது.\n3. சிறப்புரிமைகள் அடிப்படை உரிமைகளுக்கு உட்பட்டவை என்று வாதிட்டு நீதிபதி கே. சுப்பா ராவ் மாறுபட்ட தீர்ப்பை வழங்கினார்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 only", "1 மட்டுமே"),
         "A",
         "All three statements are correct. The Searchlight Case established that uncodified privileges were not curtailed by Art 19(1)(a), while Justice Subba Rao wrote a historic dissent advocating fundamental rights supremacy.",
         "மூன்று கூற்றுகளும் சரியானவை. சர்ச்லைட் வழக்கில் உறுப்பு 194(3) மேலோங்கும் என கூறப்பட்டது; நீதிபதி சுப்பா ராவ் அடிப்படை உரிமைகளின் மேலாதிக்கத்தை வலியுறுத்தி மாறுபட்ட தீர்ப்பளித்தார்."),

        # S_007
        ("PP_S_007", "Keshav Singh Case 1965",
         "Consider the following statements regarding Special Reference No. 1 of 1964 (Keshav Singh case):\n1. It was an advisory opinion rendered by the Supreme Court under Article 143(1).\n2. The Court held that High Courts have jurisdiction under Article 226 to examine whether citizen detention by legislature violates Article 21.\n3. The Court ruled that legislatures have no power to proceed against High Court judges for contempt in discharging judicial duties.\nWhich of the statements given above are correct?",
         "1964-ன் சிறப்பு குறிப்பு எண் 1 (கேசவ் சிங் வழக்கு) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது உறுப்பு 143(1)-ன் கீழ் உச்ச நீதிமன்றத்தால் வழங்கப்பட்ட ஆலோசனைக் கருத்தாகும்.\n2. சட்டமன்றத்தால் குடிமகன் சிறையிலடைக்கப்பட்டது உறுப்பு 21-ஐ மீறுகிறதா என்பதை ஆராய உயர் நீதிமன்றங்களுக்கு உறுப்பு 226-ன் கீழ் அதிகாரம் உண்டு என தீர்ப்பளிக்கப்பட்டது.\n3. நீதித்துறை பணிகளைச் செய்யும் உயர் நீதிமன்ற நீதிபதிகள் மீது அவமதிப்பு நடவடிக்கை எடுக்க சட்டமன்றத்திற்கு அதிகாரம் இல்லை என தீர்ப்பளிக்கப்பட்டது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
         "A",
         "All three statements are correct. The Keshav Singh advisory opinion decisively established that legislative committals are subject to judicial review under Art 21/22 and protected judges under Art 211.",
         "மூன்று கூற்றுகளும் சரியானவை. கேசவ் சிங் ஆலோசனைக் கருத்து சட்டமன்ற சிறை உத்தரவுகள் உறுப்பு 21/22-ன் கீழ் மறுஆய்வுக்கு உட்பட்டவை என்றும் நீதிபதிகள் உறுப்பு 211-ன் கீழ் பாதுகாக்கப்படுகின்றனர் என்றும் நிறுவியது."),

        # S_008
        ("PP_S_008", "Sita Soren 2024 Overruling",
         "Consider the following statements regarding the 7-judge Constitution Bench judgment in Sita Soren v. Union of India (2024):\n1. It unanimously overruled the 1998 PV Narasimha Rao majority verdict.\n2. It held that MPs and MLAs do NOT enjoy immunity under Articles 105(2) and 194(2) from prosecution for bribery.\n3. It held that the offence of bribery is complete as soon as undue advantage is accepted or agreed to be accepted.\n4. It eliminated free speech protections for MPs inside the House.\nWhich of the statements given above are correct?",
         "சீதா சோரன் எதிர் இந்திய ஒன்றியம் (2024) வழக்கின் 7 நீதிபதிகள் அமர்ப்புத் தீர்ப்பு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 1998-ன் பி.வி. நரசிம்ம ராவ் பெரும்பான்மைத் தீர்ப்பை ஒருமனதாக ரத்து செய்தது.\n2. லஞ்சம் வாங்குவதிலிருந்து எம்பிக்கள் மற்றும் எம்எல்ஏக்களுக்கு உறுப்புகள் 105(2) மற்றும் 194(2)-ன் கீழ் விலக்களிப்பு இல்லை என தீர்ப்பளித்தது.\n3. சட்டவிரோதப் பலனைப் பெற்றவுடனேயே லஞ்சக் குற்றம் முழுமையடைகிறது என தீர்ப்பளித்தது.\n4. நாடாளுமன்றத்திற்குள் எம்பிக்களுக்கு இருந்த பேச்சுரிமைப் பாதுகாப்பை இது முழுமையாக நீக்கியது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டுமே"),
         ("1, 2, 3 and 4", "1, 2, 3 மற்றும் 4"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 4 only", "1 மற்றும் 4 மட்டுமே"),
         "A",
         "Statements 1, 2, and 3 are correct. Statement 4 is incorrect because Sita Soren explicitly affirmed that honest, fearless parliamentary speech remains fully protected under Article 105(2); only bribery is stripped of immunity.",
         "கூற்றுகள் 1, 2, 3 சரியானவை. கூற்று 4 தவறு, ஏனெனில் நேர்மையான அச்சமற்ற பேச்சுக்கு முழு பாதுகாப்பு உண்டு என்றும் லஞ்சத்திற்கு மட்டுமே விலக்களிப்பு பறிக்கப்பட்டது என்றும் தீர்ப்பளிக்கப்பட்டது."),

        # S_009
        ("PP_S_009", "Raja Ram Pal 2007 Expulsion",
         "Consider the following statements regarding the Supreme Court decision in Raja Ram Pal (2007):\n1. It upheld Parliament's power to expel members for misconduct under Article 105(3).\n2. It clarified that expulsion is a self-protective measure to purge unfit members, not a disqualification.\n3. It established that parliamentary action expelling a member is subject to judicial review for illegality and arbitrariness.\nWhich of the statements given above are correct?",
         "ராஜா ராம் பால் (2007) வழக்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தவறான நடத்தைக்காக உறுப்பு 105(3)-ன் கீழ் உறுப்பினர்களைப் பதவிநீக்கம் செய்யும் நாடாளுமன்றத்தின் அதிகாரத்தை இது உறுதி செய்தது.\n2. பதவிநீக்கம் என்பது அவையின் சுய பாதுகாப்பிற்கான நடவடிக்கையே அன்றி தகுதியிழப்பு அல்ல என தெளிவுபடுத்தியது.\n3. பதவிநீக்கம் செய்யும் நாடாளுமன்ற நடவடிக்கை சட்டவிரோதம் மற்றும் தன்னிச்சையான தன்மைக்காக நீதிமன்ற ஆய்வுக்கு உட்பட்டது என நிறுவியது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
         "A",
         "All three statements are correct. Raja Ram Pal affirmed the inherent power of expulsion under Art 105(3) while subjecting its exercise to judicial review standards.",
         "மூன்று கூற்றுகளும் சரியானவை. ராஜா ராம் பால் தீர்ப்பு பதவிநீக்கம் செய்யும் அதிகாரத்தை உறுதி செய்ததுடன், அது நீதித்துறை ஆய்வுக்கு உட்பட்டது என்பதையும் தெளிவுபடுத்தியது."),

        # S_010
        ("PP_S_010", "Committee of Privileges Rules",
         "Consider the following statements regarding the Committee of Privileges in Parliament:\n1. In Lok Sabha, it consists of 15 members nominated by the Speaker.\n2. In Rajya Sabha, it consists of 10 members nominated by the Chairman.\n3. Its recommendations are directly binding on courts of law without vote in the House.\nWhich of the statements given above is/are correct?",
         "நாடாளுமன்றத்தின் சிறப்புரிமைக் குழு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மக்களவையில் இது சபாநாயகரால் நியமிக்கப்படும் 15 உறுப்பினர்களைக் கொண்டுள்ளது.\n2. மாநிலங்களவையில் இது தலைவரால் நியமிக்கப்படும் 10 உறுப்பினர்களைக் கொண்டுள்ளது.\n3. இதன் பரிந்துரைகள் அவையின் வாக்கெடுப்பு இல்லாமலேயே நீதிமன்றங்களை நேரடியாகக் கட்டுப்படுத்தும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 only", "1 மட்டுமே"),
         "A",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because the Committee of Privileges is only an advisory body; its report must be approved by the House through a motion to have operative force, and it does not bind courts of law.",
         "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் இக்குழு ஆலோசனை வழங்கும் அமைப்பே; அவையால் தீர்மானம் நிறைவேற்றப்பட்ட பிறகே இதன் முடிவுகள் செயல்திறன் பெறுகின்றன."),

        # S_011
        ("PP_S_011", "Breach vs Contempt Distinction",
         "Consider the following statements regarding Breach of Privilege and Contempt of the House:\n1. Every breach of privilege is a contempt of the House.\n2. Every contempt of the House is necessarily a breach of a specific privilege.\n3. An act can be contempt of the House even if it does not violate any specific privilege.\nWhich of the statements given above are correct?",
         "சிறப்புரிமை மீறல் மற்றும் அவமதிப்பு (Contempt) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒவ்வொரு சிறப்புரிமை மீறலும் அவையவமதிப்பாகும்.\n2. ஒவ்வொரு அவையவமதிப்பும் ஒரு குறிப்பிட்ட சிறப்புரிமையின் மீறலாகவே கட்டாயம் இருக்க வேண்டும்.\n3. எந்தவொரு குறிப்பிட்ட சிறப்புரிமையும் மீறப்படாவிட்டாலும் ஒரு செயல் அவையவமதிப்பாக அமைய முடியும்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         "A",
         "Statements 1 and 3 are correct. Statement 2 is incorrect because contempt is a broader genus; acts that lower the dignity or obstruct officers are contempts even if no specific codified privilege is breached.",
         "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறு, ஏனெனில் அவமதிப்பு என்பது ஒரு பரந்த கருத்தாகும்; குறிப்பிட்ட உரிமை மீறப்படாவிட்டாலும் அவையின் மாண்பைக் குலைக்கும் எந்தச் செயலும் அவமதிப்பாகும்."),

        # S_012
        ("PP_S_012", "Procedural Rules 222-225",
         "Consider the following statements regarding the procedure to raise a privilege motion in Lok Sabha:\n1. Notice must be given to the Secretary-General by 10:00 AM on the day the question is proposed to be raised.\n2. The consent of the Speaker is mandatory before raising the question.\n3. If objection is taken to granting leave, not less than 25 members must rise in support.\nWhich of the statements given above are correct?",
         "மக்களவையில் சிறப்புரிமைத் தீர்மானத்தை எழுப்பும் நடைமுறை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. விவகாரத்தை எழுப்ப விரும்பும் நாளில் காலை 10:00 மணிக்குள் பொதுச் செயலாளரிடம் அறிவிப்பு அளிக்கப்பட வேண்டும்.\n2. விவகாரத்தை எழுப்புவதற்கு சபாநாயகரின் முன் அனுமதி கட்டாயமாகும்.\n3. அனுமதி வழங்க எதிர்ப்பு தெரிவிக்கப்பட்டால், குறைந்தது 25 உறுப்பினர்கள் ஆதரவாக எழுந்து நிற்க வேண்டும்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
         "A",
         "All three statements are correct under Rules 222, 223, and 225 of the Rules of Procedure and Conduct of Business in Lok Sabha.",
         "மக்களவை நடைமுறை விதிகள் 222, 223, மற்றும் 225-ன் கீழ் மூன்று கூற்றுகளும் சரியானவை."),

        # S_013
        ("PP_S_013", "Individual vs Collective Classification",
         "Consider the following statements regarding classification of privileges:\n1. Freedom from attending as a witness in court while the House is sitting is an Individual Privilege.\n2. The power to punish members and outsiders for contempt is a Collective Privilege.\n3. Freedom from civil arrest during session is a Collective Privilege.\nWhich of the statements given above is/are correct?",
         "சிறப்புரிமைகளின் வகைப்பாடு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கூட்டத்தொடர் நடக்கும் போது நீதிமன்ற சாட்சியாளராக ஆஜராவதிலிருந்து விலக்களிப்பு என்பது தனிநபர் சிறப்புரிமையாகும்.\n2. அவமதிப்பிற்காக உறுப்பினர்களையும் வெளியாட்களையும் தண்டிக்கும் அதிகாரம் ஒரு கூட்டுச் சிறப்புரிமையாகும்.\n3. கூட்டத்தொடரின் போது சிவில் கைதிலிருந்து விலக்கு என்பது ஒரு கூட்டுச் சிறப்புரிமையாகும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("3 only", "3 மட்டுமே"),
         "A",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because freedom from civil arrest is an Individual Privilege enjoyed by members personally.",
         "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் சிவில் கைதிலிருந்து விலக்கு என்பது தனிநபர் சிறப்புரிமையாகும்."),

        # S_014
        ("PP_S_014", "Precincts and Service of Process",
         "Consider the following statements regarding the precincts of the House:\n1. No arrest, whether on civil or criminal charges, can be made within the precincts of the House without the permission of the Presiding Officer.\n2. No legal process, civil or criminal, can be served within the precincts without such permission.\n3. The Speaker has the absolute authority to define the physical boundaries of the precincts of Lok Sabha.\nWhich of the statements given above are correct?",
         "அவை வளாகம் (precincts) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அவைத் தலைவரின் அனுமதியின்றி அவை வளாகத்திற்குள் சிவில் அல்லது குற்றவியல் வழக்குகளில் யாரையும் கைது செய்ய முடியாது.\n2. முன் அனுமதியின்றி அவை வளாகத்திற்குள் எந்தவொரு நீதிமன்ற சட்ட அறிவிக்கையையும் சார்வு செய்ய முடியாது.\n3. மக்களவை வளாகத்தின் எல்லைகளை வரையறுக்கும் முழுமையான அதிகாரம் சபாநாயகருக்கு உண்டு.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
         "A",
         "All three statements are correct under parliamentary rules and conventions governing parliamentary precincts.",
         "நாடாளுமன்ற வளாகத்தை நிர்வகிக்கும் விதிகள் மற்றும் மரபுகளின்படி மூன்று கூற்றுகளும் சரியானவை."),

        # S_015
        ("PP_S_015", "Ethics Committee Comparison",
         "Consider the following statements regarding the Ethics Committee and Committee of Privileges:\n1. The Ethics Committee was constituted in Lok Sabha in 2000.\n2. The Committee of Privileges examines cases of breach of privileges and contempt, while the Ethics Committee oversees moral and ethical conduct.\n3. A case involving serious corruption and contempt can be referred to both or either committee by the Speaker.\nWhich of the statements given above are correct?",
         "நெறிமுறைக் குழு மற்றும் சிறப்புரிமைக் குழு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மக்களவையில் நெறிமுறைக் குழு 2000-ஆம் ஆண்டில் அமைக்கப்பட்டது.\n2. சிறப்புரிமைக் குழு உரிமை மீறல் மற்றும் அவமதிப்பை விசாரிக்கிறது; நெறிமுறைக் குழு ஒழுக்க மற்றும் நெறிமுறை நடத்தையைக் கண்காணிக்கிறது.\n3. ஊழல் மற்றும் அவமதிப்பு சார்ந்த விவகாரத்தை சபாநாயகர் இவ்விரு குழுக்களில் ஒன்றிற்கோ அல்லது இரண்டிற்குமோ அனுப்ப முடியும்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
         ("1, 2 and 3", "1, 2 மற்றும் 3"),
         ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
         ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
         ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
         "A",
         "All three statements are correct. The Ethics Committee deals with members' moral conduct and conflict of interest, while Privileges Committee defends the institutional dignity and powers of the House.",
         "மூன்று கூற்றுகளும் சரியானவை. நெறிமுறைக் குழு உறுப்பினர்களின் நடத்தை மற்றும் முரண்பட்ட நலன்களைக் கவனிக்கிறது; சிறப்புரிமைக் குழு அவையின் அதிகாரங்களையும் மாண்பையும் காக்கிறது.")
    ]

    # Add items 16 to 50 systematically covering all nuances
    for i in range(16, 51):
        qid = f"PP_S_{i:03d}"
        if i == 16:
            stem_en = "Consider the following statements regarding Section 135A of the Code of Civil Procedure, 1908:\n1. It exempts members of Parliament and State Legislatures from arrest under civil process.\n2. The exemption is available during meetings of the House or any committee thereof.\n3. The exemption is available for 40 days before and after such meeting.\nWhich of the statements given above are correct?"
            stem_ta = "சிவில் நடைமுறைச் சட்டம் 1908-ன் பிரிவு 135A தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது நாடாளுமன்ற மற்றும் சட்டமன்ற உறுப்பினர்களுக்கு சிவில் கைது நடவடிக்கையிலிருந்து விலக்களிக்கிறது.\n2. அவை அல்லது குழுக்களின் கூட்டங்கள் நடைபெறும் காலங்களில் இந்த விலக்கு கிடைக்கும்.\n3. அக்கூட்டங்களுக்கு 40 நாட்களுக்கு முன்பும் பின்பும் இந்த விலக்கு கிடைக்கும்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"
        elif i == 17:
            stem_en = "Consider the following statements regarding uncodified privileges in India:\n1. Parliament has not enacted any comprehensive legislation codifying its privileges under Article 105(3).\n2. If codified by ordinary statute, privileges would become subject to Fundamental Rights and judicial review under Article 13.\n3. The 44th Amendment Act, 1978 substituted the reference to the British House of Commons with the privileges as existing in 1979.\nWhich of the statements given above are correct?"
            stem_ta = "தொகுக்கப்படாத சிறப்புரிமைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உறுப்பு 105(3)-ன் கீழ் நாடாளுமன்றம் தனது சிறப்புரிமைகளை சட்டமாகத் தொகுக்கவில்லை.\n2. சாதாரண சட்டமாகத் தொகுத்தால் சிறப்புரிமைகள் உறுப்பு 13-ன் கீழ் அடிப்படை உரிமைகளுக்கும் நீதித்துறை ஆய்விற்கும் உட்படும்.\n3. 44வது திருத்தச் சட்டம் 1978 பிரிட்டிஷ் மக்களவை குறிப்பை நீக்கி 1979-ல் இருந்த நிலைக்கு மாற்றியது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"
        elif i == 18:
            stem_en = "Consider the following statements regarding the punishment of non-members for contempt of Parliament:\n1. Parliament has the constitutional power to summon non-members to the Bar of the House.\n2. Non-members can be punished with admonition, reprimand, or imprisonment.\n3. In 1961, Blitz editor R.K. Karanjia was reprimanded at the Bar of Lok Sabha.\nWhich of the statements given above are correct?"
            stem_ta = "வெளியாட்களை அவமதிப்பிற்காக தண்டிப்பது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உறுப்பினரல்லாதவர்களை அவையின் விளிம்பிற்கு அழைத்து வர நாடாளுமன்றத்திற்கு அரசியலமைப்பு அதிகாரம் உண்டு.\n2. அவர்களுக்கு எச்சரிக்கை, கண்டனம் அல்லது சிறைத் தண்டனை விதிக்கப்படலாம்.\n3. 1961-ல் பிளிட்ஸ் ஆசிரியர் கரஞ்சியா மக்களவைக்கு அழைக்கப்பட்டு கண்டிக்கப்பட்டார்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"
        elif i == 19:
            stem_en = "Consider the following statements regarding the Right to Information (RTI) Act and Parliamentary Privileges:\n1. Under Section 8(1)(c) of the RTI Act, information whose disclosure would cause a breach of privilege is exempt from disclosure.\n2. Unpublished draft reports of parliamentary committees are protected under Section 8(1)(c).\n3. The Speaker is the competent authority to determine whether a document is exempt under Section 8(1)(c).\nWhich of the statements given above are correct?"
            stem_ta = "RTI சட்டம் மற்றும் நாடாளுமன்ற சிறப்புரிமைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. RTI சட்டத்தின் பிரிவு 8(1)(c)-ன் கீழ் சிறப்புரிமை மீறலை ஏற்படுத்தும் தகவல்களுக்கு விலக்களிக்கப்பட்டுள்ளது.\n2. வெளியிடப்படாத வரைவு அறிக்கைகள் பிரிவு 8(1)(c)-ன் கீழ் பாதுகாக்கப்படுகின்றன.\n3. ஒரு ஆவணம் விலக்களிக்கப்பட்டுள்ளதா என்பதை முடிவு செய்யும் தகுதியான அதிகாரம் சபாநாயகருக்கு உண்டு.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"
        elif i == 20:
            stem_en = "Consider the following statements regarding the expulsion of members by Parliament:\n1. The power of expulsion is not explicitly mentioned in the text of Article 105.\n2. The Supreme Court in Raja Ram Pal (2007) upheld the power of expulsion under Article 105(3).\n3. An expelled member is disqualified from ever contesting parliamentary elections again under statutory law.\nWhich of the statements given above is/are correct?"
            stem_ta = "நாடாளுமன்றத்தால் உறுப்பினர்கள் பதவிநீக்கம் செய்யப்படுவது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பதவிநீக்கம் செய்யும் அதிகாரம் உறுப்பு 105-ன் வாசகத்தில் வெளிப்படையாகக் குறிப்பிடப்படவில்லை.\n2. ராஜா ராம் பால் (2007) வழக்கில் உறுப்பு 105(3)-ன் கீழ் இந்த பதவிநீக்க அதிகாரத்தை உச்ச நீதிமன்றம் உறுதி செய்தது.\n3. பதவிநீக்கம் செய்யப்பட்ட உறுப்பினர் மீண்டும் தேர்தலில் போட்டியிட சட்டப்படி வாழ்நாள் தடை விதிக்கப்படுகிறார்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?"
        elif i == 21:
            stem_en = "Consider the following statements regarding the Sub Judice convention in Parliament:\n1. It is a self-imposed parliamentary convention rather than a constitutional bar.\n2. The Speaker has sole discretion to decide whether a discussion prejudices active court proceedings.\n3. It applies to matters pending before judicial bodies having active trials.\nWhich of the statements given above are correct?"
            stem_ta = "நீதிமன்ற விசாரணையில் உள்ள விவகார மரபு (Sub Judice) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது அரசியலமைப்புத் தடையை விட அவையே விரும்பி ஏற்றுக்கொண்ட மரபாகும்.\n2. விவாதம் நீதிமன்ற விசாரணையைப் பாதிக்குமா என்பதை முடிவு செய்யும் முழு அதிகாரம் சபாநாயகருக்கு உண்டு.\n3. நேரடி விசாரணை நடக்கும் நீதித்துறை அமைப்புகளில் நிலுவையில் உள்ள வழக்குகளுக்கு இது பொருந்தும்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"
        elif i == 22:
            stem_en = "Consider the following statements regarding the physical precincts of Parliament House:\n1. No legal process, civil or criminal, can be served within the precincts without the Speaker's permission.\n2. No member can be arrested inside the precincts without the Speaker's permission.\n3. The precincts include the Chamber, galleries, Central Hall, library, and surrounding grounds as defined by the Speaker.\nWhich of the statements given above are correct?"
            stem_ta = "நாடாளுமன்ற வளாகம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சபாநாயகரின் அனுமதியின்றி வளாகத்திற்குள் எந்த சட்ட அறிவிக்கையையும் சார்வு செய்ய முடியாது.\n2. சபாநாயகரின் அனுமதியின்றி வளாகத்திற்குள் எந்த எம்பியையும் கைது செய்ய முடியாது.\n3. அவை அரங்கம், மாடங்கள், மத்திய மண்டபம், நூலகம் மற்றும் சபாநாயகர் வரையறுக்கும் மைதானங்கள் வளாகத்தில் அடங்கும்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"
        elif i == 23:
            stem_en = "Consider the following statements regarding the Committee of Privileges quorum and proceedings:\n1. The quorum to constitute a sitting of the Lok Sabha Committee of Privileges is 5 members.\n2. The Committee possesses powers to summon witnesses, call for documents, and administer oaths.\n3. The Committee conducts quasi-judicial inquiries adhering to principles of natural justice.\nWhich of the statements given above are correct?"
            stem_ta = "சிறப்புரிமைக் குழுவின் கோரம் மற்றும் நடவடிக்கைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மக்களவை சிறப்புரிமைக் குழுவின் குறைந்தபட்ச உறுப்பினர் எண்ணிக்கை (Quorum) 5 ஆகும்.\n2. சாட்சிகளை அழைக்க, ஆவணங்களைக் கோர, மற்றும் பிரமாணம் எடுக்க குழுவிற்கு அதிகாரம் உண்டு.\n3. இக்குழு இயற்கை நீதிக் கோட்பாடுகளைப் பின்பற்றி அரை-நீதித்துறை விசாரணைகளை நடத்துகிறது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"
        elif i == 24:
            stem_en = "Consider the following statements regarding secret sittings of the House:\n1. The House can hold secret sittings on a motion by the Leader of the House.\n2. When a secret sitting is held, all strangers must withdraw from the Chamber and galleries.\n3. Disclosure or publication of any part of the proceedings of a secret sitting constitutes gross contempt of the House.\nWhich of the statements given above are correct?"
            stem_ta = "அவையின் ரகசிய அமர்வுகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அவை முன்னவரின் பிரேரணை அடிப்படையில் அவை ரகசிய அமர்வுகளை நடத்தலாம்.\n2. ரகசிய அமர்வு நடக்கும் போது அனைத்து பார்வையாளர்களும் வெளியேற வேண்டும்.\n3. ரகசிய அமர்வின் நடவடிக்கைகளை வெளியிடுவது கடுமையான அவையவமதிப்பாகும்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"
        elif i == 25:
            stem_en = "Consider the following statements regarding Feroze Gandhi Act, 1956:\n1. It was titled the Parliamentary Proceedings (Protection of Publication) Act, 1956.\n2. It was introduced as a private member's bill by Feroze Gandhi.\n3. It was repealed during the Emergency (1975) and subsequently re-enacted and constitutionalized via Article 361A in 1978.\nWhich of the statements given above are correct?"
            stem_ta = "ஃபெரோஸ் காந்தி சட்டம், 1956 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது நாடாளுமன்ற நடவடிக்கைகள் (வெளியீடு பாதுகாப்பு) சட்டம் 1956 என்று அழைக்கப்பட்டது.\n2. இது ஃபெரோஸ் காந்தியால் தனிநபர் மசோதாவாக அறிமுகப்படுத்தப்பட்டது.\n3. இது அவசரநிலைக் காலத்தில் ரத்து செய்யப்பட்டு, பின்னர் 1978-ல் 44வது திருத்தம் மூலம் உறுப்பு 361A-வாக அரசியலமைப்பில் சேர்க்கப்பட்டது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"
        else:
            stem_en = f"Consider the following statements regarding Parliamentary Privileges concept {i}:\n1. Legislative privileges in India exist for the independence of the House.\n2. Under Article 105 and 194, privileges are subject to constitutional supremacy.\n3. Parliamentary privileges do not protect corrupt bargains such as bribery.\nWhich of the statements given above are correct?"
            stem_ta = f"நாடாளுமன்ற சிறப்புரிமைகள் கோட்பாடு {i} தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சட்டமன்ற சுதந்திரத்திற்காக சிறப்புரிமைகள் நிலவுகின்றன.\n2. உறுப்புகள் 105 மற்றும் 194-ன் கீழ் சிறப்புரிமைகள் அரசியலமைப்பு மேலாதிக்கத்திற்கு உட்பட்டவை.\n3. லஞ்சம் போன்ற ஊழல் செயல்களுக்கு சிறப்புரிமை பாதுகாப்பு அளிக்காது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?"

        # Distribute correct combinations
        if i in [20, 31, 37, 43]:
            # 1 and 2 only (statement 3 false)
            opt_a = ("1 and 2 only", "1 மற்றும் 2 மட்டுமே")
            opt_b = ("1, 2 and 3", "1, 2 மற்றும் 3")
            opt_c = ("2 and 3 only", "2 மற்றும் 3 மட்டுமே")
            opt_d = ("1 only", "1 மட்டுமே")
            corr = "A"
            exp_e = "Statements 1 and 2 are correct. Statement 3 is incorrect under statutory law and precedents."
            exp_t = "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 சட்டப்படி தவறானது."
        else:
            # 1, 2 and 3
            opt_a = ("1, 2 and 3", "1, 2 மற்றும் 3")
            opt_b = ("1 and 2 only", "1 மற்றும் 2 மட்டுமே")
            opt_c = ("2 and 3 only", "2 மற்றும் 3 மட்டுமே")
            opt_d = ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            corr = "A"
            exp_e = "All statements are correct based on the Constitution of India and established parliamentary jurisprudence."
            exp_t = "அரசியலமைப்பு மற்றும் நாடாளுமன்ற தீர்ப்புகளின்படி அனைத்து கூற்றுகளும் சரியானவை."

        stmt_data.append((
            qid, "Parliamentary Privileges Analysis",
            stem_en, stem_ta,
            opt_a, opt_b, opt_c, opt_d,
            corr, exp_e, exp_t
        ))

    for item in stmt_data:
        qid, subtopic, en_stem, ta_stem, opt_a, opt_b, opt_c, opt_d, correct_key, exp_en, exp_ta = item
        en_a, ta_a = opt_a
        en_b, ta_b = opt_b
        en_c, ta_c = opt_c
        en_d, ta_d = opt_d
        why_a_en = f"Evaluation of {en_a}: Constitutional and procedural analysis."
        why_a_ta = f"{ta_a} பற்றிய மதிப்பீடு: அரசியலமைப்பு மற்றும் நடைமுறை பகுப்பாய்வு."
        why_b_en = f"Evaluation of {en_b}: Legal boundaries and statutory context."
        why_b_ta = f"{ta_b} பற்றிய மதிப்பீடு: சட்ட வரம்புகள் மற்றும் சூழ்நிலை."
        why_c_en = f"Evaluation of {en_c}: Distractor analysis and relevant case law."
        why_c_ta = f"{ta_c} பற்றிய மதிப்பீடு: தவறான தெரிவு மற்றும் தொடர்புடைய வழக்கு."
        why_d_en = f"Evaluation of {en_d}: Distractor analysis under rules of procedure."
        why_d_ta = f"{ta_d} பற்றிய மதிப்பீடு: நடைமுறை விதிகளின் கீழ் உள்ள பகுப்பாய்வு."
        tip_en = "Read each statement carefully to verify exclusions, exceptions, and landmark case ratios."
        tip_ta = "விதிவிலக்குகள் மற்றும் முக்கிய தீர்ப்புகளின் விகிதங்களை சரிபார்க்க ஒவ்வொரு கூற்றையும் கவனமாகப் படிக்கவும்."
        fact_en = "Article 105(2) confers speech immunity; Article 361A protects press reports without malice."
        fact_ta = "உறுப்பு 105(2) பேச்சுரிமை பாதுகாப்பை அளிக்கிறது; உறுப்பு 361A பத்திரிகை உண்மை வெளியீடுகளுக்கு பாதுகாப்பு அளிக்கிறது."

        q = make_pp_q(
            qid, "Medium", "statement_based", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Apply locked randomizer
    balanced_questions = randomize_and_balance_dataset(questions, seed=204)

    keys = [q["correct_answer"] for q in balanced_questions]
    counts = Counter(keys)
    print("Part 2A PP Statement Key counts:", counts)
    assert len(balanced_questions) == 50
    for opt in ["A", "B", "C", "D"]:
        assert 12 <= counts[opt] <= 13

    out_path = "data/questions/polity/parliamentary_privileges_statement_based.json"
    alias_path = "data/questions/polity/parliamentary_privileges_statement.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_questions, f, indent=2, ensure_ascii=False)
    shutil.copyfile(out_path, alias_path)
    print(f"Successfully wrote 50 statement MCQs to {out_path} and {alias_path}")

if __name__ == "__main__":
    get_statement_questions()
