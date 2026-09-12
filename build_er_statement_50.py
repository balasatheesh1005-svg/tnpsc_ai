# -*- coding: utf-8 -*-
"""
Builder for Electoral Reforms Statement-Based 50 MCQs (ER_S_001 to ER_S_050).
Strictly adheres to the 24-field TNPSC Nova AI schema.
"""

import json
import os
from er_mcq_helper import make_er_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

OUTPUT_PATH = os.path.join("data", "questions", "polity", "electoral_reforms_statement_based.json")
ALIAS_PATH = os.path.join("data", "questions", "polity", "electoral_reforms_statement.json")

def get_statement_questions():
    qs = []

    # ER_S_001
    qs.append(make_er_q(
        qid="ER_S_001", diff="Medium", qtype="Multi-Statement", subtopic="Electoral Bonds Judgment 2024",
        en_stem="Consider the following statements regarding the Supreme Court's unanimous judgment in Association for Democratic Reforms (ADR) v. Union of India (February 2024):\n1. The 5-judge Constitution Bench held that the Electoral Bonds Scheme violated the voters' Right to Information under Article 19(1)(a).\n2. The court upheld the unlimited corporate political donation provisions introduced in Section 182 of the Companies Act, 2013.\n3. State Bank of India was directed to submit all details of bonds purchased and redeemed to the Election Commission of India for public disclosure.\nWhich of the statements given above are correct?",
        ta_stem="ஜனநாயக சீர்திருத்தங்களுக்கான சங்கம் (ADR) எதிர் இந்திய ஒன்றியம் (பிப்ரவரி 2024) வழக்கில் உச்ச நீதிமன்றம் வழங்கிய ஒருமனதான தீர்ப்பு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தல் பத்திரங்கள் திட்டம் சரத்து 19(1)(a)-ன் கீழான வாக்காளர்களின் தகவல் அறியும் உரிமையை மீறுகிறது என 5 நீதிபதிகள் அமர்வு தீர்ப்பளித்தது.\n2. கம்பெனிகள் சட்டம் 2013 பிரிவு 182-ல் நிறுவனங்கள் வரம்பற்ற அரசியல் நன்கொடைகளை வழங்க அனுமதிக்கப்பட்ட திருத்தத்தை நீதிமன்றம் உறுதி செய்தது.\n3. தேர்தல் பத்திரங்கள் வாங்கப்பட்ட மற்றும் பணமாக்கப்பட்ட அனைத்து விவரங்களையும் தேர்தல் ஆணையத்திடம் பொதுமக்களின் பார்வைக்காக சமர்ப்பிக்க பாரத ஸ்டேட் வங்கிக்கு (SBI) உத்தரவிடப்பட்டது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 3 only", ta_a="1 மற்றும் 3 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 3 are correct. Statement 2 is incorrect because the court struck down the amendment to Section 182 of the Companies Act that had removed the 7.5% profit cap on corporate donations, holding it to be manifestly arbitrary and violative of Article 14.",
        exp_ta="கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது; ஏனெனில் கம்பெனிகள் சட்டம் பிரிவு 182-ல் கார்ப்பரேட் நன்கொடைகளுக்கான 7.5% லாப வரம்பை நீக்கிய திருத்தத்தை தன்னிச்சையானது மற்றும் சரத்து 14-க்கு எதிரானது எனக் கூறி உச்ச நீதிமன்றம் ரத்து செய்தது.",
        why_a_en="Correct. Statements 1 and 3 accurately describe the February 2024 verdict.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 3 பிப்ரவரி 2024 தீர்ப்பை சரியாக விவரிக்கின்றன.",
        why_b_en="Incorrect. Statement 2 is false as the corporate amendment was struck down.",
        why_b_ta="தவறானது. கூற்று 2 தவறானது.",
        why_c_en="Incorrect. Statement 2 is false.",
        why_c_ta="தவறானது. கூற்று 2 தவறானது.",
        why_d_en="Incorrect. Statement 2 is false.",
        why_d_ta="தவறானது. கூற்று 2 தவறானது.",
        tip_en="The bench was headed by CJI D.Y. Chandrachud and delivered two concurrent concurring opinions on 15 February 2024.",
        tip_ta="தலைமை நீதிபதி டி.ஒய். சந்திரசூட் தலைமையிலான அமர்வு 2024 பிப்ரவரி 15 அன்று இத்தீர்ப்பை வழங்கியது.",
        fact_en="Amendments to the RBI Act, RPA 1951, Companies Act, and Income Tax Act were all declared unconstitutional.",
        fact_ta="ரிசர்வ் வங்கி சட்டம், மக்கள் பிரதிநிதித்துவச் சட்டம், கம்பெனிகள் சட்டம் மற்றும் வருமான வரிச் சட்டம் ஆகியவற்றில் செய்யப்பட்ட திருத்தங்கள் அனைத்தும் ரத்து செய்யப்பட்டன.",
        tags=["Electoral Bonds 2024", "ADR Case", "Multi-Statement"]
    ))

    # ER_S_002
    qs.append(make_er_q(
        qid="ER_S_002", diff="Medium", qtype="Multi-Statement", subtopic="VVPAT Verification Guidelines",
        en_stem="Consider the following statements regarding the Voter Verifiable Paper Audit Trail (VVPAT) system in India:\n1. The Conduct of Elections Rules, 1961 were amended in 2013 to provide statutory sanction for VVPAT.\n2. In Chandrababu Naidu (2019), the Supreme Court mandated physical verification of VVPAT slips in 5 polling stations per assembly segment.\n3. In April 2024, the Supreme Court ordered 100% physical counting of all VVPAT slips in all general elections.\nWhich of the statements given above is/are correct?",
        ta_stem="இந்தியாவில் வாக்காளர் சரிபார்க்கும் காகித தணிக்கைத் தடம் (VVPAT) அமைப்பு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. VVPAT-க்கு சட்டப்பூர்வ அங்கீகாரம் வழங்க 2013-ல் தேர்தல் நடத்தை விதிகள் 1961 திருத்தப்பட்டன.\n2. சந்திரபாபு நாயுடு (2019) வழக்கில், ஒரு சட்டமன்ற தொகுதிக்கு 5 வாக்குச்சாவடிகளில் VVPAT சீட்டுகளை எண்ணி சரிபார்க்க உச்ச நீதிமன்றம் உத்தரவிட்டது.\n3. 2024 ஏப்ரலில், அனைத்து பொதுத்தேர்தல்களிலும் அனைத்து வாக்குச்சாவடிகளிலும் 100% VVPAT சீட்டுகளையும் எண்ண வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because on 26 April 2024, the Supreme Court explicitly REJECTED the prayer for 100% VVPAT slip verification, upholding the integrity of EVMs while issuing directions on sealing Symbol Loading Units (SLUs) and permitting 5% microcontroller verification for runners-up.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் 2024 ஏப்ரல் 26 அன்று உச்ச நீதிமன்றம் 100% VVPAT சீட்டுகளை எண்ணும் கோரிக்கையை வெளிப்படையாக நிராகரித்தது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 உண்மை; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Remember: 100% VVPAT count was rejected by Supreme Court in both 2019 and April 2024.",
        tip_ta="நினைவில் கொள்க: 100% VVPAT எண்ணும் கோரிக்கையை உச்ச நீதிமன்றம் 2019 மற்றும் 2024 ஆகிய இரு முறையும் நிராகரித்தது.",
        fact_en="The paper slip contains the candidate's serial number, name, and election symbol, visible for 7 seconds.",
        fact_ta="VVPAT சீட்டில் வேட்பாளரின் வரிசை எண், பெயர், சின்னம் ஆகியவை 7 வினாடிகள் தெரியும்.",
        tags=["VVPAT", "Chandrababu Naidu 2019", "Supreme Court 2024"]
    ))

    # ER_S_003
    qs.append(make_er_q(
        qid="ER_S_003", diff="Hard", qtype="Multi-Statement", subtopic="Lily Thomas vs Ramesh Dalal",
        en_stem="Consider the following statements regarding disqualification of convicted legislators:\n1. In Ramesh Dalal v. Union of India (2005), the Supreme Court ruled that sitting MPs and MLAs do not enjoy constitutional immunity from disqualification on conviction.\n2. In Lily Thomas v. Union of India (2013), Section 8(4) of RPA 1951 was declared unconstitutional, ending the 3-month protection window for sitting legislators.\n3. Under the current law, even if an appellate court stays the conviction under Section 389 CrPC, the disqualification of an MP continues permanently.\nWhich of the statements given above are correct?",
        ta_stem="குற்றத்தண்டனை பெற்ற மக்கள் பிரதிநிதிகளின் தகுதிநீக்கம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ரமேஷ் தலால் எதிர் இந்திய ஒன்றியம் (2005) வழக்கில், குற்றத்தண்டனை பெறும்போது பதவியில் உள்ள எம்.பி., எம்.எல்.ஏ-க்களுக்கு அரசியலமைப்பு விலக்கு ஏதுமில்லை என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n2. லில்லி தாமஸ் (2013) வழக்கில், மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 8(4) ரத்து செய்யப்பட்டு, பதவியில் உள்ள உறுப்பினர்களுக்கான 3 மாத கால பாதுகாப்பு முடிவுக்கு வந்தது.\n3. தற்போதைய சட்டத்தின் கீழ், குற்றவியல் நடைமுறைச் சட்டம் பிரிவு 389-ன் கீழ் மேல்முறையீட்டு நீதிமன்றம் குற்றத்தண்டனைக்கு தடை விதித்தாலும், நாடாளுமன்ற உறுப்பினரின் தகுதிநீக்கம் நிரந்தரமாகத் தொடரும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because in Lok Prahari v. ECI (2018), the Supreme Court clarified that a stay of CONVICTION by an appellate court removes the disqualification under Section 8 of RPA 1951, restoring their legislative seat.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் லோக் பிரஹாரி (2018) வழக்கில், குற்றத்தீர்ப்பிற்கு (Stay of conviction) தடை விதிக்கப்பட்டால் தகுதிநீக்கம் நீக்கப்பட்டு அவரது பதவி மீண்டும் மீட்டெடுக்கப்படும் என தெளிவுபடுத்தப்பட்டது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is incorrect.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is incorrect.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is incorrect.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is incorrect.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Stay of sentence = bail (no effect on disqualification); Stay of conviction = wipes out disqualification.",
        tip_ta="தண்டனை நிறுத்தம் = ஜாமீன் (தகுதிநீக்கம் நீங்காது); குற்றத்தீர்ப்பிற்கு தடை = தகுதிநீக்கம் நீங்கும்.",
        fact_en="Section 8(4) had allowed convicted legislators to continue in office simply by filing an appeal within 3 months.",
        fact_ta="பழைய பிரிவு 8(4) 3 மாதங்களுக்குள் மேல்முறையீடு செய்வதன் மூலம் பதவியில் தொடர அனுமதித்திருந்தது.",
        tags=["Lily Thomas 2013", "Ramesh Dalal 2005", "Stay of Conviction"]
    ))

    # ER_S_004
    qs.append(make_er_q(
        qid="ER_S_004", diff="Hard", qtype="Multi-Statement", subtopic="Committees on Electoral Reforms",
        en_stem="Consider the following pairs of Committees on Electoral Reforms and their key recommendations:\n1. Tarkunde Committee (1974) – Recommended lowering the voting age from 21 to 18 years.\n2. Indrajit Gupta Committee (1998) – Recommended complete cash funding of all contesting independent candidates by the Central Government.\n3. Dinesh Goswami Committee (1990) – Recommended introduction of EVMs and rapid state assistance in kind.\nWhich of the pairs given above are correctly matched?",
        ta_stem="தேர்தல் சீர்திருத்தங்களுக்கான குழுக்கள் மற்றும் அவற்றின் முக்கிய பரிந்துரைகள் குறித்த பின்வரும் இணைகளைக் கவனியுங்கள்:\n1. தர்குண்டே குழு (1974) – வாக்களிக்கும் வயதை 21-லிருந்து 18 ஆகக் குறைக்க பரிந்துரைத்தது.\n2. இந்திரஜித் குப்தா குழு (1998) – போட்டியிடும் அனைத்து சுயேச்சை வேட்பாளர்களுக்கும் மத்திய அரசு முழு ரொக்க நிதியுதவி அளிக்க வேண்டும் என பரிந்துரைத்தது.\n3. தினேஷ் கோஸ்வாமி குழு (1990) – EVM பயன்பாட்டை அறிமுகப்படுத்தவும், அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு பொருளுதவி வழங்கவும் பரிந்துரைத்தது.\nமேற்கண்ட இணைகளில் சரியாகப் பொருந்தியுள்ளது எது/எவை?",
        en_a="1 and 3 only", ta_a="1 மற்றும் 3 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Pairs 1 and 3 are correctly matched. Pair 2 is incorrectly matched because the Indrajit Gupta Committee strictly rejected cash funding and explicitly excluded independent candidates, recommending state funding ONLY in kind and ONLY to recognized political parties.",
        exp_ta="இணைகள் 1 மற்றும் 3 சரியாகப் பொருந்தியுள்ளன. இணை 2 தவறானது; ஏனெனில் இந்திரஜித் குப்தா குழு ரொக்க நிதியுதவியையும், சுயேச்சை வேட்பாளர்களையும் திட்டவட்டமாக நிராகரித்து, அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு மட்டும் பொருளுதவி வடிவில் நிதியளிக்க பரிந்துரைத்தது.",
        why_a_en="Correct. Pairs 1 and 3 are historically accurate; Pair 2 is false.",
        why_a_ta="சரியானது. இணைகள் 1 மற்றும் 3 சரி; இணை 2 தவறு.",
        why_b_en="Incorrect. Pair 2 is incorrect.",
        why_b_ta="தவறானது. இணை 2 தவறு.",
        why_c_en="Incorrect. Pair 2 is incorrect.",
        why_c_ta="தவறானது. இணை 2 தவறு.",
        why_d_en="Incorrect. Pair 2 is incorrect.",
        why_d_ta="தவறானது. இணை 2 தவறு.",
        tip_en="Indrajit Gupta formula = In kind only + Recognized parties only + Ban on corporate donations.",
        tip_ta="இந்திரஜித் குப்தா சூத்திரம் = பொருளுதவி மட்டுமே + அங்கீகரிக்கப்பட்ட கட்சிகள் மட்டுமே + கார்ப்பரேட் நன்கொடை தடை.",
        fact_en="Tarkunde Committee was appointed in 1974 under the JP Movement on behalf of Citizens for Democracy.",
        fact_ta="தர்குண்டே குழு 1974-ல் ஜெயபிரகாஷ் நாராயணனின் ஜேபி இயக்கத்தின் போது அமைக்கப்பட்டது.",
        tags=["Committees Matching", "Tarkunde", "Indrajit Gupta", "Dinesh Goswami"]
    ))

    # ER_S_005
    qs.append(make_er_q(
        qid="ER_S_005", diff="Hard", qtype="Multi-Statement", subtopic="106th Amendment Act 2023",
        en_stem="Consider the following statements regarding the 106th Constitutional Amendment Act, 2023 (Nari Shakti Vandan Adhiniyam):\n1. It provides 33% reservation for women in the Lok Sabha, State Legislative Assemblies, and the Legislative Assembly of the National Capital Territory of Delhi.\n2. It includes a sub-quota of one-third seats reserved for Scheduled Caste and Scheduled Tribe women within their reserved quotas.\n3. The reservation came into operational effect immediately for the 2024 Lok Sabha general elections.\nWhich of the statements given above are correct?",
        ta_stem="106-வது அரசியலமைப்புச் சட்டத்திருத்தம் 2023 (நாரி சக்தி வந்தன் அதினியம்) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மக்களவை, மாநில சட்டமன்றங்கள் மற்றும் டெல்லி தேசிய தலைநகர் பிரதேச சட்டசபையில் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்குகிறது.\n2. இது SC மற்றும் ST பிரிவினருக்கு ஒதுக்கப்பட்ட இடங்களில் மூன்றில் ஒரு பங்கை அப்பிரிவு பெண்களுக்கு உள்-ஒதுக்கீடாக வழங்குகிறது.\n3. இந்த இடஒதுக்கீடு 2024 மக்களவைப் பொதுத்தேர்தலில் உடனடியாக நடைமுறைக்கு வந்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under Article 334A, the reservation will take effect only after a delimitation exercise is conducted based on the first population census published after the commencement of the Act. Hence, it was not operational in the 2024 elections.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் சரத்து 334A-ன் படி, இச்சட்டம் நடைமுறைக்கு வந்த பின் எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையில் தொகுதி மறுவரையறை செய்யப்பட்ட பிறகே இது நடைமுறைக்கு வரும். எனவே 2024 தேர்தலில் இது அமலாகவில்லை.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 உண்மை; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Article 330A = Lok Sabha; Article 332A = State Assemblies; Article 239AA(2)(ba) = Delhi; Article 334A = Commencement & 15-year sunset clause.",
        tip_ta="சரத்து 330A = மக்களவை; 332A = மாநில சட்டசபைகள்; 239AA = டெல்லி; 334A = தொடக்கம் மற்றும் 15 ஆண்டு கால வரம்பு.",
        fact_en="There is NO sub-quota for Other Backward Classes (OBC) women in the 106th Amendment.",
        fact_ta="106-வது திருத்தத்தில் இதர பிற்படுத்தப்பட்ட (OBC) பெண்களுக்கு தனி உள்-ஒதுக்கீடு எதுவும் வழங்கப்படவில்லை.",
        tags=["106th Amendment", "Women Reservation", "Article 334A", "Census Condition"]
    ))

    # ER_S_006
    qs.append(make_er_q(
        qid="ER_S_006", diff="Hard", qtype="Multi-Statement", subtopic="Delimitation Constitutional Framework",
        en_stem="Consider the following statements regarding the delimitation of constituencies in India:\n1. The 42nd Constitutional Amendment Act, 1976 originally froze the allocation of seats to the states until the year 2000.\n2. The 84th Amendment Act, 2001 extended this freeze until the first census taken after the year 2026.\n3. Under Article 329(a), orders issued by the Delimitation Commission cannot be challenged in any court of law once published in the Gazette of India.\nWhich of the statements given above are correct?",
        ta_stem="இந்தியாவில் தொகுதி மறுவரையறை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 42-வது அரசியலமைப்புச் சட்டத்திருத்தம் 1976, மாநிலங்களுக்கான இடங்களின் ஒதுக்கீட்டை 2000 ஆம் ஆண்டு வரை முதலில் முடக்கியது.\n2. 84-வது திருத்தச் சட்டம் 2001, இந்த முடக்கத்தை 2026 ஆம் ஆண்டிற்குப் பிறகு எடுக்கப்படும் முதல் கணக்கெடுப்பு வரை நீட்டித்தது.\n3. சரத்து 329(a)-ன் கீழ், தொகுதி மறுவரையறை ஆணையத்தின் ஆணைகள் அரசிதழில் வெளியிடப்பட்டவுடன் அவற்றை எந்த நீதிமன்றத்திலும் எதிர்த்து கேள்வி கேட்க முடியாது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. 42nd Amendment froze seats till 2000; 84th Amendment extended the freeze till post-2026 census; and Article 329(a) completely bars judicial interference in delimitation orders, as upheld in Meghraj Kothari (1967).",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. 42-வது திருத்தம் 2000 வரை முடக்கியது; 84-வது திருத்தம் அதை 2026-க்குப் பிந்தைய கணக்கெடுப்பு வரை நீட்டித்தது; சரத்து 329(a) மறுவரையறை ஆணைகள் மீது நீதிமன்ற தலையீட்டை முழுமையாக தடை செய்கிறது (மேக்ராஜ் கோத்தாரி வழக்கு).",
        why_a_en="Correct. All three statements are accurate constitutional facts.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் துல்லியமான அரசியலமைப்பு உண்மைகள்.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="Constitutional articles on delimitation: Article 82 (Readjustment after census for Lok Sabha) and Article 170(3) (for State Assemblies).",
        tip_ta="மறுவரையறை தொடர்பான சரத்துகள்: சரத்து 82 (மக்களவைக்கான மறுசீரமைப்பு) மற்றும் சரத்து 170(3) (மாநில சட்டசபைகளுக்கானது).",
        fact_en="The 87th Amendment in 2003 allowed internal delimitation based on 2001 census without changing total state seats.",
        fact_ta="2003-ன் 87-வது திருத்தம் மாநிலத்திற்குள் எல்லைகளை மாற்ற 2001 கணக்கெடுப்பை அடிப்படையாகக் கொள்ள அனுமதித்தது.",
        tags=["Delimitation", "42nd Amendment", "84th Amendment", "Article 329(a)"]
    ))

    # ER_S_007
    qs.append(make_er_q(
        qid="ER_S_007", diff="Medium", qtype="Multi-Statement", subtopic="Election Laws Amendment 2021",
        en_stem="Consider the following statements regarding the Election Laws (Amendment) Act, 2021:\n1. It amended Section 14(b) of RPA 1950 to introduce four qualifying dates in a year (Jan 1, Apr 1, Jul 1, Oct 1) for voter enrollment.\n2. It made the linking of Aadhaar number with the electoral roll through Form 6B strictly compulsory, canceling the voting rights of non-linkers.\n3. It substituted the word 'wife' with 'spouse' in Section 20 of RPA 1950, making service voter provisions gender-neutral.\nWhich of the statements given above are correct?",
        ta_stem="தேர்தல் சட்டங்கள் (திருத்தச்) சட்டம், 2021 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது வாக்காளர் சேர்க்கைக்காக ஆண்டிற்கு நான்கு தகுதி தேதிகளை (ஜனவரி 1, ஏப்ரல் 1, ஜூலை 1, அக்டோபர் 1) அறிமுகப்படுத்த RPA 1950 பிரிவு 14(b)-ஐத் திருத்தியது.\n2. இது படிவம் 6B மூலம் ஆதார் எண்ணை வாக்காளர் பட்டியலுடன் இணைப்பதை கட்டாயமாக்கியதுடன், இணைக்காதவர்களின் வாக்குரிமையை ரத்து செய்தது.\n3. இது பிரிவு 20-ல் 'மனைவி' என்ற சொல்லுக்குப் பதிலாக 'துணைவர்' (Spouse) என்று மாற்றி பணி வாக்காளர் விதிகளை பாலின நடுநிலையாக்கியது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 3 only", ta_a="1 மற்றும் 3 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 3 are correct. Statement 2 is incorrect because the linking of Aadhaar with electoral rolls (Form 6B) is purely VOLUNTARY. The law explicitly provides that no person's name shall be deleted or omitted from the electoral roll for failure to submit an Aadhaar number.",
        exp_ta="கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது; ஏனெனில் ஆதார் எண்ணை வாக்காளர் பட்டியலுடன் இணைப்பது (படிவம் 6B) முற்றிலும் தன்னார்வமானது (Voluntary). ஆதார் எண் தராத காரணத்திற்காக வாக்காளர் பட்டியலில் இருந்து பெயர் நீக்கப்படக் கூடாது என சட்டம் தெளிவாகக் கூறுகிறது.",
        why_a_en="Correct. Statements 1 and 3 are true; statement 2 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 3 உண்மை; கூற்று 2 தவறு.",
        why_b_en="Incorrect. Statement 2 is false as Aadhaar linking is voluntary.",
        why_b_ta="தவறானது. ஆதார் இணைப்பு கட்டாயமல்ல.",
        why_c_en="Incorrect. Statement 2 is false.",
        why_c_ta="தவறானது. கூற்று 2 தவறு.",
        why_d_en="Incorrect. Statement 2 is false.",
        why_d_ta="தவறானது. கூற்று 2 தவறு.",
        tip_en="Supreme Court in September 2023 reaffirmed ECI's undertaking that Aadhaar submission is strictly optional.",
        tip_ta="2023 செப்டம்பரில் உச்ச நீதிமன்றம் ஆதார் சமர்ப்பிப்பது விருப்பத்தேர்வே என ECI அளித்த வாக்குறுதியை உறுதிப்படுத்தியது.",
        fact_en="The Act also empowered registration officers to requisition premises for polling and voting machine storage.",
        fact_ta="வாக்குப்பதிவு மற்றும் இயந்திரப் பாதுகாப்பிற்காக வளாகங்களை கையகப்படுத்தும் அதிகாரத்தையும் இச்சட்டம் வழங்கியது.",
        tags=["Election Laws 2021", "Aadhaar Voluntary", "Gender Neutral", "4 Qualifying Dates"]
    ))

    # ER_S_008
    qs.append(make_er_q(
        qid="ER_S_008", diff="Hard", qtype="Multi-Statement", subtopic="CEC Appointment Act 2023 vs Anoop Baranwal",
        en_stem="Consider the following statements regarding the appointment mechanism of the Chief Election Commissioner and other Election Commissioners:\n1. In Anoop Baranwal (March 2023), the Supreme Court directed an interim committee of the PM, Leader of Opposition, and Chief Justice of India.\n2. The CEC and other ECs Act, 2023 replaced the Chief Justice of India with a Union Cabinet Minister nominated by the Prime Minister.\n3. The 2023 Act downgraded the salary, perks, and status of the CEC and ECs to that of the Cabinet Secretary.\nWhich of the statements given above are correct?",
        ta_stem="தலைமைத் தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்களின் நியமன முறை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அனூப் பரன்வால் (மார்ச் 2023) வழக்கில், பிரதமர், எதிர்க்கட்சித் தலைவர் மற்றும் தலைமை நீதிபதி அடங்கிய இடைக்காலக் குழுவை உச்ச நீதிமன்றம் அமைத்தது.\n2. 2023 நாடாளுமன்ற சட்டம் தலைமை நீதிபதிக்குப் பதிலாக பிரதமரால் நியமிக்கப்படும் ஒரு மத்திய கேபினட் அமைச்சரை குழுவில் சேர்த்தது.\n3. 2023 சட்டம் தேர்தல் ஆணையர்களின் ஊதியம், படிகள் மற்றும் அந்தஸ்தை கேபினட் செயலாளரின் நிலைக்குக் குறைத்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because although the original draft Bill sought to equate their salary with the Cabinet Secretary, Parliament amended it during passage to maintain their salary, perks, and conditions of service equal to a Judge of the Supreme Court under Section 8 of the enacted Act.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் மசோதாவின் ஆரம்ப வரைவில் கேபினட் செயலாளருக்கு சமமாக ஊதியம் குறைக்க முன்மொழியப்பட்ட போதிலும், நாடாளுமன்றத்தில் நிறைவேற்றப்பட்ட இறுதிச் சட்டத்தில் உச்ச நீதிமன்ற நீதிபதிக்கு இணையான ஊதியம் மற்றும் அந்தஸ்தே நீட்டிக்கப்பட்டது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 உண்மை; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="The Search Committee is headed by the Minister of Law and Justice and shortlists 5 candidates.",
        tip_ta="தேடுதல் குழு மத்திய சட்ட அமைச்சர் தலைமையில் செயல்பட்டு 5 நபர்களைப் பரிந்துரைக்கும்.",
        fact_en="The Selection Committee can regulate its own procedure and consider persons outside the Search Committee's panel.",
        fact_ta="தேடுதல் குழுவின் பட்டியலுக்கு வெளியேயும் உள்ள தகுதியான நபர்களை தேர்வுக் குழு பரிசீலிக்க அதிகாரம் உண்டு.",
        tags=["CEC Act 2023", "Anoop Baranwal", "Selection Committee", "Supreme Court Judge Status"]
    ))

    # ER_S_009
    qs.append(make_er_q(
        qid="ER_S_009", diff="Hard", qtype="Multi-Statement", subtopic="Kovind Committee on Simultaneous Elections",
        en_stem="Consider the following statements regarding the recommendations of the High-Level Committee on Simultaneous Elections (Kovind Committee, 2024):\n1. It recommended inserting Article 82A to empower the President to notify an 'Appointed Date' bringing simultaneous elections into force.\n2. It recommended amending Article 325 to create a single electoral roll and single EPIC card for Lok Sabha, Assembly, and Local Body elections.\n3. It recommended that single electoral roll amendments would not require ratification by any State Legislatures.\nWhich of the statements given above are correct?",
        ta_stem="'ஒரே நாடு, ஒரே தேர்தல்' குறித்த உயர்நிலைக் குழுவின் (கோவிந்த் குழு, 2024) பரிந்துரைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பொதுத்தேர்தலுக்குப் பின் ஒரே நேரத்தில் தேர்தலை அமல்படுத்த 'நியமிக்கப்பட்ட தேதியை' அறிவிக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்க சரத்து 82A-ஐ இணைக்க பரிந்துரைத்தது.\n2. மக்களவை, சட்டமன்றம் மற்றும் உள்ளாட்சித் தேர்தல்கள் அனைத்திற்கும் ஒரே வாக்காளர் பட்டியல் மற்றும் ஒரே வாக்காளர் அட்டையை உருவாக்க சரத்து 325-ஐத் திருத்த பரிந்துரைத்தது.\n3. ஒரே வாக்காளர் பட்டியல் திருத்தத்திற்கு எந்தவொரு மாநில சட்டமன்றங்களின் ஒப்புதலும் (Ratification) தேவையில்லை என்று பரிந்துரைத்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the Kovind Committee explicitly stated that amending Article 325 to create a unified electoral roll for local bodies falls within the federal domain and WILL require ratification by at least half of the State Legislatures under Article 368(2).",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் உள்ளாட்சி அமைப்புகள் மாநிலப் பட்டியலில் வருவதால், சரத்து 325-ன் கீழான ஒருங்கிணைந்த வாக்காளர் பட்டியல் திருத்தத்திற்கு குறைந்தபட்சம் பாதி மாநில சட்டமன்றங்களின் ஒப்புதல் (Ratification) கட்டாயம் தேவை என கோவிந்த் குழு தெளிவுபடுத்தியது.",
        why_a_en="Correct. Statements 1 and 2 are accurate; statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Article 82A (Lok Sabha + Assemblies) does NOT need state ratification; Article 325 (Single Roll for Local Bodies) DOES need state ratification.",
        tip_ta="சரத்து 82A-க்கு மாநில ஒப்புதல் தேவையில்லை; சரத்து 325 (உள்ளாட்சி பட்டியல்)-க்கு மாநில ஒப்புதல் கட்டாயம் தேவை.",
        fact_en="The committee also recommended that local body elections should be held within 100 days of simultaneous general elections under Article 324A.",
        fact_ta="சரத்து 324A-ன் கீழ் பொதுத்தேர்தல் முடிந்த 100 நாட்களுக்குள் உள்ளாட்சித் தேர்தல்களை நடத்தவும் பரிந்துரைக்கப்பட்டது.",
        tags=["Kovind Committee 2024", "Article 82A", "Single Electoral Roll", "State Ratification"]
    ))

    # ER_S_010
    qs.append(make_er_q(
        qid="ER_S_010", diff="Hard", qtype="Multi-Statement", subtopic="Tenth Schedule Anti-Defection",
        en_stem="Consider the following statements regarding the Anti-Defection Law (Tenth Schedule):\n1. A nominated member of a House becomes disqualified if they join any political party after the expiry of 6 months from the date of taking their seat.\n2. An independent member becomes disqualified if they join any political party at any time after election.\n3. In Kihoto Hollohan (1992), the Supreme Court struck down Paragraph 7 of the Tenth Schedule, establishing that the Speaker's decisions are subject to judicial review.\nWhich of the statements given above are correct?",
        ta_stem="கட்சித் தாவல் தடைச் சட்டம் (10-வது அட்டவணை) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒரு நியமன உறுப்பினர் பதவியேற்ற நாளிலிருந்து 6 மாதங்கள் முடிந்த பிறகு ஏதேனும் ஒரு அரசியல் கட்சியில் சேர்ந்தால் தகுதிநீக்கம் செய்யப்படுவார்.\n2. ஒரு சுயேச்சை உறுப்பினர் தேர்தலுக்குப் பிறகு எப்போது ஒரு கட்சியில் சேர்ந்தாலும் தகுதிநீக்கம் செய்யப்படுவார்.\n3. கிகோட்டோ ஹோல்லோஹான் (1992) வழக்கில், உச்ச நீதிமன்றம் 10-வது அட்டவணையின் பத்தி 7-ஐ ரத்து செய்து, சபாநாயகரின் முடிவுகள் நீதிப் புனராய்வுக்கு உட்பட்டவை என நிறுவியது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Paragraph 2(3) disqualifies nominated members who join a party after 6 months; Paragraph 2(2) disqualifies independent members who join ANY party after election; and Kihoto Hollohan (1992) struck down Paragraph 7 to establish judicial review over the Speaker.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பத்தி 2(3)-ன் படி நியமன உறுப்பினர் 6 மாதத்திற்குப் பின் கட்சியில் சேர்ந்தால் தகுதிநீக்கம் செய்யப்படுவார்; பத்தி 2(2)-ன் படி சுயேச்சை உறுப்பினர் கட்சியில் சேர்ந்தால் தகுதிநீக்கம் செய்யப்படுவார்; கிகோட்டோ வழக்கில் பத்தி 7 ரத்து செய்யப்பட்டு நீதிப் புனராய்வு நிலைநாட்டப்பட்டது.",
        why_a_en="Correct. All three statements are accurate legal provisions of the 10th Schedule.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் பத்தாவது அட்டவணையின் துல்லியமான சட்ட விதிகள்.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="Nominated member CAN join a party within the first 6 months without incurring disqualification.",
        tip_ta="நியமன உறுப்பினர் முதல் 6 மாதங்களுக்குள் ஒரு கட்சியில் சேர்ந்தால் தகுதிநீக்கம் ஆக மாட்டார்.",
        fact_en="Independent members can support a government from outside without joining the party.",
        fact_ta="சுயேச்சை உறுப்பினர்கள் கட்சியில் சேராமல் வெளியில் இருந்து அரசுக்கு ஆதரவு அளிக்கலாம்.",
        tags=["10th Schedule", "Nominated Member", "Independent Member", "Kihoto Hollohan"]
    ))

    # ER_S_011 to ER_S_050: Systematic continuation covering all facets of Electoral Reforms
    # Let's generate questions 11 to 50 systematically with rich pedagogical rigor

    # ER_S_011
    qs.append(make_er_q(
        qid="ER_S_011", diff="Medium", qtype="Multi-Statement", subtopic="Section 123 Corrupt Practices",
        en_stem="Consider the following statements regarding 'Corrupt Practices' under Section 123 of RPA 1951:\n1. Bribery is defined as a corrupt practice under Section 123(1).\n2. Appealing for votes on grounds of religion, race, caste, community, or language is barred under Section 123(3).\n3. Any public declaration of government policy or promises of public infrastructure by a candidate is treated as illegal undue influence.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 123-ன் கீழான 'ஊழல் நடைமுறைகள்' குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. லஞ்சம் கொடுப்பது அல்லது பெறுவது பிரிவு 123(1)-ன் கீழ் ஊழல் நடைமுறையாக வரையறுக்கப்பட்டுள்ளது.\n2. மதம், இனம், ஜாதி, சமூகம் அல்லது மொழியின் அடிப்படையில் வாக்குக் கேட்பது பிரிவு 123(3)-ன் கீழ் தடை செய்யப்பட்டுள்ளது.\n3. அரசு கொள்கை அறிவிப்புகள் அல்லது பொது உள்கட்டமைப்பு வாக்குறுதிகளை அளிப்பது சட்டவிரோத தவறான செல்வாக்காகக் கருதப்படுகிறது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because proviso (b) to Section 123(2) explicitly protects declarations of public policy and promises of public action from being treated as undue influence.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 123(2) வரம்புரை (b), பொதுக் கொள்கை அறிவிப்புகள் அல்லது மக்கள் நல திட்ட வாக்குறுதிகள் தவறான செல்வாக்காகக் கருதப்படாது என விலக்களிக்கிறது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is explicitly exempted by statute.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 உண்மை; கூற்று 3 சட்டப்படி விலக்கு பெற்றது.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Policy promises are legitimate political competition; private pecuniary inducements to voters constitute bribery.",
        tip_ta="பொதுக்கொள்கை வாக்குறுதிகள் ஜனநாயக போட்டி; ஆனால் வாக்காளர்களுக்கு பணம் கொடுப்பது லஞ்சமாகும்.",
        fact_en="Booth capturing is codified as a corrupt practice under Section 123(8).",
        fact_ta="வாக்குச்சாவடி பிடிப்பு பிரிவு 123(8)-ன் கீழ் ஊழல் நடைமுறையாக சேர்க்கப்பட்டுள்ளது.",
        tags=["Section 123", "Corrupt Practices", "Bribery", "Public Policy Exemption"]
    ))

    # ER_S_012
    qs.append(make_er_q(
        qid="ER_S_012", diff="Medium", qtype="Multi-Statement", subtopic="Model Code of Conduct Provisions",
        en_stem="Consider the following statements regarding the Model Code of Conduct (MCC):\n1. It was first adopted voluntarily in Kerala during the 1960 state assembly elections.\n2. It has been codified into an Act of Parliament and is enforced directly by criminal courts.\n3. It becomes effective immediately upon the announcement of election dates by the ECI.\nWhich of the statements given above are correct?",
        ta_stem="மாதிரி தேர்தல் நடத்தை விதிகள் (MCC) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது முதன்முதலில் 1960 கேரள சட்டமன்றத் தேர்தலின் போது தன்னார்வ அடிப்படையில் ஏற்றுக்கொள்ளப்பட்டது.\n2. இது நாடாளுமன்றச் சட்டமாக இயற்றப்பட்டு, குற்றவியல் நீதிமன்றங்களால் நேரடியாக அமல்படுத்தப்படுகிறது.\n3. தேர்தல் ஆணையம் தேர்தல் தேதிகளை அறிவித்த உடனேயே இது உடனடியாக அமலுக்கு வருகிறது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 3 only", ta_a="1 மற்றும் 3 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 3 are correct. Statement 2 is incorrect because the MCC has NO statutory backing; it is not an Act of Parliament, but a voluntary code enforced through ECI's constitutional powers under Article 324.",
        exp_ta="கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது; ஏனெனில் MCC-க்கு சட்டப்பூர்வ அந்தஸ்து இல்லை. இது நாடாளுமன்ற சட்டம் அல்ல; சரத்து 324-ன் கீழ் ECI-ன் அதிகாரத்தால் அமல்படுத்தப்படும் நிர்வாக நடத்தை நெறியாகும்.",
        why_a_en="Correct. Statements 1 and 3 are true; statement 2 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 3 உண்மை; கூற்று 2 தவறு.",
        why_b_en="Incorrect. Statement 2 is false as MCC is non-statutory.",
        why_b_ta="தவறானது. MCC சட்டப்பூர்வமானது அல்ல.",
        why_c_en="Incorrect. Statement 2 is false.",
        why_c_ta="தவறானது. கூற்று 2 தவறு.",
        why_d_en="Incorrect. Statement 2 is false.",
        why_d_ta="தவறானது. கூற்று 2 தவறு.",
        tip_en="Supreme Court in Ashok Kumar (2000) upheld ECI's authority to enforce MCC from date of announcement.",
        tip_ta="அசோக் குமார் (2000) வழக்கில் அறிவிக்கப்பட்ட தேதியிலிருந்து MCC-ஐ அமல்படுத்தும் ECI-ன் அதிகாரம் உறுதி செய்யப்பட்டது.",
        fact_en="Part VIII on Election Manifestos was added in 2014 following the Subramaniam Balaji verdict.",
        fact_ta="சுப்பிரமணியம் பாலாஜி தீர்ப்பைத் தொடர்ந்து 2014-ல் தேர்தல் அறிக்கை பகுதி சேர்க்கப்பட்டது.",
        tags=["MCC", "Non-Statutory", "Kerala Origin", "Announcement Date"]
    ))

    # ER_S_013
    qs.append(make_er_q(
        qid="ER_S_013", diff="Hard", qtype="Multi-Statement", subtopic="Section 62 Right to Vote Conditions",
        en_stem="Consider the following statements regarding the Right to Vote under Section 62 of the Representation of the People Act, 1951:\n1. Every person whose name is entered in the electoral roll of a constituency is entitled to vote in that constituency.\n2. No person can vote at a general election in more than one constituency.\n3. Undertrial prisoners lodged in lawful police or judicial custody are permitted to vote via postal ballot.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 62-ன் கீழான வாக்களிக்கும் உரிமை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒரு தொகுதியின் வாக்காளர் பட்டியலில் பெயர் உள்ள ஒவ்வொரு நபரும் அத்தொகுதியில் வாக்களிக்க தகுதியுடையவர்.\n2. பொதுத்தேர்தலில் எந்தவொரு நபரும் ஒன்றுக்கு மேற்பட்ட தொகுதிகளில் வாக்களிக்க முடியாது.\n3. காவல் அல்லது நீதிமன்றக் காவலில் உள்ள விசாரணைக் கைதிகள் தபால் வாக்கு மூலம் வாக்களிக்க அனுமதிக்கப்படுகிறார்கள்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under Section 62(5) of RPA 1951, all persons confined in prison (whether convicted or undertrials) or in lawful police custody are completely barred from voting; only persons under PREVENTIVE detention can vote via postal ballot.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 62(5)-ன் படி, சிறையிலுள்ள விசாரணைக் கைதிகளுக்கும் வாக்களிக்க முழு தடை உள்ளது. தடுப்புக் காவலில் (Preventive detention) உள்ளவர்களுக்கு மட்டுமே தபால் வாக்கு வசதி உண்டு.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is legally false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 உண்மை; கூற்று 3 சட்டப்படி தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="If a person votes in more than one constituency, all their votes become void under Section 62(3).",
        tip_ta="ஒருவர் ஒன்றுக்கு மேற்பட்ட தொகுதிகளில் வாக்களித்தால் அவரது அனைத்து வாக்குகளும் செல்லாது (பிரிவு 62(3)).",
        fact_en="Section 62(4) bars a person from voting more than once in the SAME constituency.",
        fact_ta="பிரிவு 62(4) ஒரே தொகுதியில் ஒருவர் இருமுறை வாக்களிப்பதைத் தடை செய்கிறது.",
        tags=["Section 62", "Right to Vote", "Prisoners Disenfranchised", "RPA 1951"]
    ))

    # ER_S_014
    qs.append(make_er_q(
        qid="ER_S_014", diff="Hard", qtype="Multi-Statement", subtopic="Section 10A Disqualification",
        en_stem="Consider the following statements regarding Section 10A of the Representation of the People Act, 1951:\n1. It empowers the Election Commission to disqualify a candidate for failure to lodge an account of election expenses within the prescribed 30-day time limit.\n2. The period of disqualification under Section 10A is 3 years from the date of the order.\n3. The power to remove or reduce the disqualification period under Section 10A is vested in the President acting on the advice of the Prime Minister.\nWhich of the statements given above is/are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 10A குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நிர்ணயிக்கப்பட்ட 30 நாட்களுக்குள் தேர்தல் செலவுக் கணக்குகளை தாக்கல் செய்யத் தவறும் வேட்பாளரை தகுதிநீக்கம் செய்ய இது தேர்தல் ஆணையத்திற்கு அதிகாரம் அளிக்கிறது.\n2. பிரிவு 10A-ன் கீழான தகுதிநீக்கக் காலம் உத்தரவு பிறப்பிக்கப்பட்ட நாளிலிருந்து 3 ஆண்டுகள் ஆகும்.\n3. பிரிவு 10A-ன் கீழான தகுதிநீக்கத்தை நீக்க அல்லது குறைக்க பிரதமரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவருக்கு அதிகாரம் உண்டு.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under Section 11 of RPA 1951, the power to remove or reduce any disqualification under Section 10A is vested directly in the ELECTION COMMISSION, not the President.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 11-ன் கீழ் தகுதிநீக்கத்தை நீக்க அல்லது அதன் காலத்தைக் குறைக்க தேர்தல் ஆணையத்திற்கே (ECI) முழு அதிகாரம் உண்டு, குடியரசுத் தலைவருக்கு அல்ல.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 உண்மை; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Corrupt practices disqualification (Sec 8A) = President on ECI opinion. Expense default disqualification (Sec 10A) = ECI directly.",
        tip_ta="ஊழல் நடைமுறை தகுதிநீக்கம் (8A) = ECI ஆலோசனையின்படி குடியரசுத் தலைவர்; செலவுக் கணக்கு தகுதிநீக்கம் (10A) = ECI நேரடியாக.",
        fact_en="Notice is issued by ECI giving 20 days to explain before invoking Section 10A.",
        fact_ta="பிரிவு 10A-ஐ அமல்படுத்துவதற்கு முன் விளக்கமளிக்க 20 நாட்கள் அவகாசம் வழங்கி ECI நோட்டீஸ் அனுப்பும்.",
        tags=["Section 10A", "Expense Default", "3 Years", "Section 11 Powers"]
    ))

    # ER_S_015
    qs.append(make_er_q(
        qid="ER_S_015", diff="Hard", qtype="Multi-Statement", subtopic="Section 29A Political Party Registration",
        en_stem="Consider the following statements regarding registration of political parties under Section 29A of RPA 1951:\n1. An association seeking registration must apply to the Election Commission within 30 days following the date of its formation.\n2. The party constitution must declare true faith and allegiance to the Constitution of India and principles of socialism, secularism, and democracy.\n3. The Supreme Court in Indian National Congress v. Institute of Social Welfare (2002) ruled that ECI has inherent power to cancel or deregister a party at its discretion.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 29A-ன் கீழ் அரசியல் கட்சிகள் பதிவு செய்வது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கட்சியாக பதிவு செய்ய விரும்பும் ஓர் அமைப்பு உருவான தேதியிலிருந்து 30 நாட்களுக்குள் தேர்தல் ஆணையத்திடம் விண்ணப்பிக்க வேண்டும்.\n2. கட்சி விதிகள் இந்திய அரசியலமைப்பிற்கும் சோசலிசம், மதச்சார்பின்மை, ஜனநாயகம் ஆகியவற்றிற்கும் உண்மையான விசுவாசம் செலுத்துவதாக உறுதியளிக்க வேண்டும்.\n3. 2002 காங்கிரஸ் வழக்கில், தன் விருப்பப்படி கட்சிகளின் பதிவை ரத்து செய்யும் உள்ளார்ந்த அதிகாரம் தேர்தல் ஆணையத்திற்கு உண்டு என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the Supreme Court in that very judgment held that ECI has NO general statutory power to deregister a political party once registered, except in 3 narrow exceptions (fraud, self-dissolution, or disloyalty to Constitution).",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் 2002 காங்கிரஸ் வழக்கில், 3 அரிய விதிவிலக்குகள் தவிர கட்சிகளின் பதிவை ரத்து செய்ய தேர்தல் ஆணையத்திற்கு பொதுவான சட்ட அதிகாரம் இல்லை என்றே உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is the opposite of the court ruling.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 உண்மை; கூற்று 3 நீதிமன்ற தீர்ப்பிற்கு எதிரானது.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="An application under Section 29A must be signed by at least 100 registered electors who are members of the association.",
        tip_ta="பிரிவு 29A விண்ணப்பத்தில் குறைந்தது 100 வாக்காளர்கள் உறுப்பினர்களாக கையொப்பமிட வேண்டும்.",
        fact_en="Registration gives political parties the right to accept voluntary corporate donations under Section 29B and common symbols.",
        fact_ta="பதிவு செய்யப்பட்ட கட்சிகளுக்கு மட்டுமே பிரிவு 29B-ன் கீழ் நன்கொடைகளைப் பெறவும் பொது சின்னம் பெறவும் உரிமை உண்டு.",
        tags=["Section 29A", "Party Registration", "Deregistration Bar", "Supreme Court 2002"]
    ))

    # ER_S_016
    qs.append(make_er_q(
        qid="ER_S_016", diff="Medium", qtype="Multi-Statement", subtopic="State Funding of Elections",
        en_stem="Consider the following statements regarding the debate on State Funding of Elections in India:\n1. The Indrajit Gupta Committee (1998) recommended partial state funding exclusively in kind to recognized political parties.\n2. The 170th Law Commission Report (1999) endorsed state funding of elections on the precondition that political parties practice inner-party democracy.\n3. The Second Administrative Reforms Commission (2007) recommended complete abolition of all private corporate donations without any state funding.\nWhich of the statements given above are correct?",
        ta_stem="இந்தியாவில் தேர்தல்களுக்கான அரசு நிதியுதவி (State Funding) குறித்த விவாதம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திரஜித் குப்தா குழு (1998) அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு மட்டும் பொருளுதவி வடிவிலான பகுதி அரசு நிதியுதவியை பரிந்துரைத்தது.\n2. 170-வது சட்ட ஆணைய அறிக்கை (1999), அரசியல் கட்சிகள் உள்கட்சி ஜனநாயகத்தைக் கடைப்பிடிக்க வேண்டும் என்ற முன்நிபந்தனையுடன் அரசு நிதியுதவியை ஆதரித்தது.\n3. இரண்டாவது நிர்வாக சீர்திருத்த ஆணையம் (2007) அரசு நிதியுதவி ஏதுமின்றி அனைத்து தனியார் கார்ப்பரேட் நன்கொடைகளையும் முழுமையாக ஒழிக்க பரிந்துரைத்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the Second ARC (4th Report, Ethics in Governance) actually RECOMMENDED partial state funding of elections to reduce the illegitimate use of black money, rather than opposing state funding.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் இரண்டாவது நிர்வாக சீர்திருத்த ஆணையம் (4-வது அறிக்கை) கறுப்புப் பணப் பயன்பாட்டைக் குறைக்க தேர்தல்களுக்கு பகுதி அரசு நிதியுதவி வழங்க வேண்டும் என்றே பரிந்துரைத்தது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 misstates 2nd ARC recommendation.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Inner-party democracy (regular organizational elections and accounts audit) was highlighted by the Law Commission as an indispensable prerequisite for state aid.",
        tip_ta="உள்கட்சி ஜனநாயகமும் தணிக்கை செய்யப்பட்ட கணக்குகளும் அரசு நிதியுதவி பெறுவதற்கான கட்டாய முன்நிபந்தனைகளாக சட்ட ஆணையத்தால் வலியுறுத்தப்பட்டன.",
        fact_en="Currently, state assistance in India exists in limited form: free airtime on Doordarshan/AIR and free copies of electoral rolls.",
        fact_ta="தற்போது இந்தியாவில் தூர்தர்ஷன் இலவச பிரச்சார நேரம் மற்றும் இலவச வாக்காளர் பட்டியல் நகல் வடிவில் வரையறுக்கப்பட்ட பொருளுதவி நடைமுறையில் உள்ளது.",
        tags=["State Funding", "Indrajit Gupta", "170th Law Commission", "Second ARC"]
    ))

    # ER_S_017
    qs.append(make_er_q(
        qid="ER_S_017", diff="Hard", qtype="Multi-Statement", subtopic="Section 126 and Silence Period",
        en_stem="Consider the following statements regarding the campaign silence period under Section 126 of RPA 1951:\n1. It prohibits holding public meetings and processions during the period of 48 hours ending with the conclusion of the poll.\n2. It explicitly prohibits display of election matter by means of cinematograph, television, or similar electronic apparatus.\n3. The prohibition applies equally to door-to-door campaigning by candidates accompanied by up to 5 persons.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 126-ன் கீழான பிரச்சார அமைதிக்காலம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வாக்குப்பதிவு முடிவடையும் நேரத்திற்கு முந்தைய 48 மணி நேரத்தில் பொதுக்கூட்டங்கள் மற்றும் ஊர்வலங்கள் நடத்துவது தடை செய்யப்பட்டுள்ளது.\n2. திரைப்படம், தொலைக்காட்சி அல்லது ஒத்த மின்னணு சாதனங்கள் மூலம் தேர்தல் விஷயங்களைக் காட்சிப்படுத்துவது தெளிவாகத் தடை செய்யப்பட்டுள்ளது.\n3. வேட்பாளருடன் 5 பேர் வரை சென்று மேற்கொள்ளும் அமைதியான வீடு வீடான வாக்கு சேகரிப்பிற்கும் இத்தடை சமமாகப் பொருந்தும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 126 prohibits PUBLIC meetings, rallies, loudspeakers, and broadcast media, but does NOT bar quiet door-to-door canvassing by a candidate accompanied by a few persons (maximum 5 as per ECI guidelines).",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 126 பொதுக்கூட்டங்கள், ஊர்வலங்கள் மற்றும் ஊடக பிரச்சாரங்களை மட்டுமே தடை செய்கிறது; ஆனால் வேட்பாளர் 5 பேருக்கு மிகாமல் சென்று அமைதியாக வீடு வீடாக வாக்கு சேகரிப்பதற்கு தடையில்லை.",
        why_a_en="Correct. Statements 1 and 2 are true; quiet door-to-door canvassing is permitted.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; அமைதியான வீடு வீடான பிரச்சாரம் அனுமதிக்கப்படுகிறது.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Violation of Section 126 is punishable with imprisonment up to 2 years or fine or both under Section 126(2).",
        tip_ta="பிரிவு 126-ஐ மீறினால் 2 ஆண்டுகள் வரை சிறைத்தண்டனை அல்லது அபராதம் விதிக்கப்படும்.",
        fact_en="Section 126 applies constituency-wise based on the polling schedule of each respective phase.",
        fact_ta="பிரிவு 126 ஒவ்வொரு கட்ட வாக்குப்பதிவு அட்டவணைக்கு ஏற்ப தொகுதி வாரியாகப் பொருந்தும்.",
        tags=["Section 126", "48 Hours Silence", "Door-to-door Exemption"]
    ))

    # ER_S_018
    qs.append(make_er_q(
        qid="ER_S_018", diff="Medium", qtype="Multi-Statement", subtopic="Candidate Affidavits Form 26",
        en_stem="Consider the following statements regarding candidate affidavits filed in Form 26:\n1. It was mandated pursuant to the Supreme Court judgments in the ADR (2002) and PUCL (2003) cases.\n2. A candidate must disclose pending criminal cases where charges have been framed by a court for offences punishable with 2+ years imprisonment.\n3. If any column is left blank in Form 26, the Returning Officer must automatically accept the nomination without raising any objection.\nWhich of the statements given above are correct?",
        ta_stem="படிவம் 26-ல் தாக்கல் செய்யப்படும் வேட்பாளர் உறுதிமொழிப் பத்திரம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ADR (2002) மற்றும் PUCL (2003) உச்ச நீதிமன்ற தீர்ப்புகளின் அடிப்படையில் இது கட்டாயமாக்கப்பட்டது.\n2. 2 அல்லது அதற்கு மேற்பட்ட ஆண்டுகள் சிறைத் தண்டனைக்குரிய குற்றங்களில் நீதிமன்றத்தால் குற்றச்சாட்டுகள் பதிவு செய்யப்பட்ட நிலுவை வழக்குகளை வேட்பாளர் வெளிப்படுத்த வேண்டும்.\n3. படிவம் 26-ல் ஏதேனும் ஒரு பத்தி காலியாக விடப்பட்டிருந்தால், தேர்தல் நடத்தும் அலுவலர் எவ்வித ஆட்சேபனையுமின்றி வேட்புமனுவை தானாக ஏற்றுக்கொள்ள வேண்டும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under the Supreme Court's ruling in Resurgence India v. ECI (2013), leaving any column blank in Form 26 despite notice by the Returning Officer renders the nomination paper liable to be REJECTED.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் ரீசர்ஜன்ஸ் இந்தியா (2013) தீர்ப்பின்படி படிவம் 26-ல் பத்திகளை காலியாக விட்டால் அந்த வேட்புமனு நிராகரிக்கப்பட வேண்டும்.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 உண்மை; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Section 33A of RPA 1951 gives statutory force to candidate criminal disclosures.",
        tip_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 33A வேட்பாளர் குற்ற வெளிப்பாட்டிற்கு சட்டப்பூர்வ அங்கீகாரம் அளிக்கிறது.",
        fact_en="Candidates must also disclose convictions where they were sentenced to imprisonment for 1 year or more under Section 33A(1)(ii).",
        fact_ta="1 ஆண்டு அல்லது அதற்கு மேற்பட்ட சிறைத்தண்டனை பெற்ற வழக்குகளையும் பிரிவு 33A-ன் கீழ் வேட்பாளர் வெளியிட வேண்டும்.",
        tags=["Form 26", "ADR Judgment", "Resurgence India", "Section 33A"]
    ))

    # ER_S_019
    qs.append(make_er_q(
        qid="ER_S_019", diff="Hard", qtype="Multi-Statement", subtopic="Election Petitions Procedural Nuances",
        en_stem="Consider the following statements regarding Election Petitions in India:\n1. An election petition can only be filed before the High Court within 45 days from the date of declaration of results.\n2. An election petition can be filed by any candidate who contested or by any elector entitled to vote at that election.\n3. The decision of the High Court on an election petition cannot be appealed to the Supreme Court under any circumstances.\nWhich of the statements given above are correct?",
        ta_stem="இந்தியாவில் தேர்தல் வழக்குகள் (Election Petitions) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட நாளிலிருந்து 45 நாட்களுக்குள் உயர் நீதிமன்றத்தில் மட்டுமே தேர்தல் மனு தாக்கல் செய்யப்பட முடியும்.\n2. தேர்தலில் போட்டியிட்ட எந்தவொரு வேட்பாளராலும் அல்லது அந்த தேர்தலில் வாக்களிக்க தகுதியுள்ள எந்தவொரு வாக்காளராலும் தேர்தல் மனு தாக்கல் செய்யப்படலாம்.\n3. தேர்தல் மனு மீதான உயர் நீதிமன்றத்தின் தீர்ப்பை எதிர்த்து எந்த சூழ்நிலையிலும் உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்ய முடியாது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 116A of RPA 1951 explicitly provides for a statutory appeal to the Supreme Court on any question of law or fact from every order made by a High Court on an election petition.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 116A, உயர் நீதிமன்றத்தின் தேர்தல் மனு தீர்ப்பை எதிர்த்து உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்ய நேரடி சட்டப்பூர்வ உரிமையை வழங்குகிறது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is legally incorrect.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 சட்டப்படி தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Appeals under Section 116A must be filed before the Supreme Court within 30 days from the High Court's order.",
        tip_ta="பிரிவு 116A-ன் கீழான மேல்முறையீடு உயர் நீதிமன்ற உத்தரவு வந்த 30 நாட்களுக்குள் உச்ச நீதிமன்றத்தில் தாக்கல் செய்யப்பட வேண்டும்.",
        fact_en="Section 81 governs who can file an election petition (candidates or electors of that constituency).",
        fact_ta="பிரிவு 81 யார் தேர்தல் மனு தாக்கல் செய்யலாம் (வேட்பாளர் அல்லது அத்தொகுதி வாக்காளர்) என்பதைக் கூறுகிறது.",
        tags=["Election Petitions", "Section 81", "Section 116A", "High Court Supreme Court"]
    ))

    # ER_S_020
    qs.append(make_er_q(
        qid="ER_S_020", diff="Hard", qtype="Multi-Statement", subtopic="Security Deposit Provisions",
        en_stem="Consider the following statements regarding the forfeiture of security deposits under Section 158 of RPA 1951:\n1. A candidate forfeits their deposit if they secure less than or equal to one-sixth (1/6th) of the total valid votes polled.\n2. The security deposit for a Scheduled Caste candidate contesting a Lok Sabha election is ₹12,500.\n3. If a candidate wins the election, their deposit is always returned even if they somehow secured less than 1/6th of votes.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 158-ன் கீழான தேர்தல் வைப்புத்தொகை பறிமுதல் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பதிவான மொத்த செல்லுபடியாகும் வாக்குகளில் ஆறில் ஒரு பங்கிற்கு (1/6) சமமாகவோ அல்லது குறைவாகவோ பெற்றால் வேட்பாளரின் வைப்புத்தொகை பறிமுதல் செய்யப்படும்.\n2. மக்களவைத் தேர்தலில் போட்டியிடும் ஒரு பட்டியல் சாதி (SC) வேட்பாளருக்கான வைப்புத்தொகை ₹12,500 ஆகும்.\n3. ஒரு வேட்பாளர் தேர்தலில் வெற்றி பெற்றால், அவர் 1/6 பங்கை விட குறைவான வாக்குகள் பெற்றிருந்தாலும் கூட அவரது வைப்புத்தொகை எப்போதும் திருப்பித் தரப்படும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Under Section 158(4), a deposit is forfeited unless the candidate receives more than 1/6th of total valid votes. Lok Sabha deposit for SC/ST is half of ₹25,000, i.e., ₹12,500 under Section 34. And under Section 158(1), the deposit of the elected candidate is always returned.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பிரிவு 158(4)-ன் படி 1/6 பங்குக்கு மேல் பெறாவிட்டால் வைப்புத்தொகை பறிபோகும். பிரிவு 34-ன் படி மக்களவைக்கு SC/ST வேட்பாளரின் வைப்புத்தொகை ₹12,500. மேலும் வெற்றி பெற்ற வேட்பாளருக்கு பிரிவு 158(1)-ன் படி வைப்புத்தொகை எப்போதும் திருப்பியளிக்கப்படும்.",
        why_a_en="Correct. All three statements accurately state the statutory rules.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் சட்ட விதிகளை துல்லியமாகக் கூறுகின்றன.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="For Assembly elections: General = ₹10,000; SC/ST = ₹5,000.",
        tip_ta="சட்டமன்றத் தேர்தலுக்கு: பொது = ₹10,000; SC/ST = ₹5,000.",
        fact_en="If an elector contests multiple seats and secures >1/6th in all, only ONE deposit is returned and the rest are forfeited under Section 158(6).",
        fact_ta="ஒருவர் இரு தொகுதிகளில் நின்று இரண்டிலும் 1/6 வாக்குகள் பெற்றாலும், ஒரு வைப்புத்தொகை மட்டுமே திருப்பித் தரப்படும், மற்றொன்று பறிமுதலாகும்.",
        tags=["Section 158", "Security Deposit", "1/6th Rule", "SC ST Concession"]
    ))

    # Let's generate statements 21 to 50 systematically
    # ER_S_021
    qs.append(make_er_q(
        qid="ER_S_021", diff="Medium", qtype="Multi-Statement", subtopic="Exit and Opinion Polls",
        en_stem="Consider the following statements regarding poll surveys during elections:\n1. Section 126A of RPA 1951 prohibits exit polls from the start of the first phase until 30 minutes after the close of the final phase.\n2. Opinion polls are prohibited during the period of 48 hours ending with the conclusion of the poll under Section 126(1)(b).\n3. Foreign news organizations are exempt from the prohibition on broadcasting exit polls in India.\nWhich of the statements given above are correct?",
        ta_stem="தேர்தல் கால கருத்துக்கணிப்புகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 126A முதற்கட்ட வாக்குப்பதிவு தொடங்கி இறுதிக்கட்டம் முடிந்து 30 நிமிடங்கள் வரை வாக்குக்கணிப்புகளுக்கு (Exit Polls) தடை விதிக்கிறது.\n2. பிரிவு 126(1)(b)-ன் கீழ் வாக்குப்பதிவு முடிவடையும் முந்தைய 48 மணி நேரத்தில் தேர்தலுக்கு முந்தைய கருத்துக் கணிப்புகளுக்கு (Opinion Polls) தடை விதிக்கப்பட்டுள்ளது.\n3. இந்தியாவில் தேர்தல் வாக்குக்கணிப்புகளை ஒளிபரப்புவதிலிருந்து வெளிநாட்டு ஊடக நிறுவனங்களுக்கு முழு விலக்கு உண்டு.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the statutory ban applies universally to all entities, domestic or foreign, disseminating exit poll results within Indian territory.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் இந்திய எல்லைக்குள் முடிவுகளை வெளியிடும் அனைத்து உள்நாட்டு மற்றும் வெளிநாட்டு ஊடகங்களுக்கும் இத்தடை சமமாகப் பொருந்தும்.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Opinion polls = Banned 48 hours before poll. Exit polls = Banned across ALL phases until 30 mins after the last phase.",
        tip_ta="கருத்துக்கணிப்பு = தேர்தலுக்கு முந்தைய 48 மணி நேரம் தடை. வாக்குக்கணிப்பு = அனைத்து கட்டங்களும் முடியும் வரை முழு தடை.",
        fact_en="The Law Commission's 255th report recommended banning opinion polls from the date of notification of elections.",
        fact_ta="தேர்தல் அறிவிக்கை வெளியான நாளிலிருந்தே கருத்துக்கணிப்புகளை தடை செய்ய சட்ட ஆணையம் பரிந்துரைத்தது.",
        tags=["Section 126A", "Exit Polls", "Opinion Polls", "Multi-Statement"]
    ))

    # ER_S_022
    qs.append(make_er_q(
        qid="ER_S_022", diff="Hard", qtype="Multi-Statement", subtopic="Office of Profit Framework",
        en_stem="Consider the following statements regarding the 'Office of Profit' under Articles 102(1)(a) and 191(1)(a):\n1. The Constitution does not define the expression 'Office of Profit'.\n2. Parliament is constitutionally empowered to declare by law that certain offices shall not disqualify their holders.\n3. In Jaya Bachchan (2006), the Supreme Court ruled that an office is an office of profit only if the holder actually collected the monetary salary.\nWhich of the statements given above are correct?",
        ta_stem="சரத்து 102(1)(a) மற்றும் 191(1)(a)-ன் கீழான 'ஆதாயப் பதவி' குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அரசியலமைப்புச் சட்டம் 'ஆதாயப் பதவி' என்ற சொற்றொடரை எங்கும் வரையறுக்கவில்லை.\n2. குறிப்பிட்ட சில பதவிகள் தகுதிநீக்கத்தை ஏற்படுத்தாது என்று சட்டத்தின் மூலம் அறிவிக்க நாடாளுமன்றத்திற்கு அரசியலமைப்பு அதிகாரம் உண்டு.\n3. ஜெயா பச்சன் (2006) வழக்கில், பதவி வகிப்பவர் உண்மையில் பண ஊதியத்தைப் பெற்றிருந்தால் மட்டுமே அது ஆதாயப் பதவியாகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the Supreme Court in Jaya Bachchan held that actual receipt of profit is irrelevant; what matters is whether the office is CAPABLE of yielding profit or pecuniary gain.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் ஜெயா பச்சன் வழக்கில், உண்மையில் பணத்தைப் பெற்றாரா என்பது முக்கியமல்ல, அப்பதவி நிதி ஆதாயம் தரும் சாத்தியக்கூறைக் கொண்டிருந்தாலே அது ஆதாயப் பதவி எனத் தீர்ப்பளிக்கப்பட்டது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 misstates the ratio of Jaya Bachchan.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தீர்ப்பின் பொருளை தவறாகக் கூறுகிறது.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Parliament enacted the Parliament (Prevention of Disqualification) Act, 1959 to protect ministers, leaders of opposition, and certain committee members.",
        tip_ta="அமைச்சர்கள், எதிர்க்கட்சித் தலைவர்கள் போன்றோருக்கு விலக்கு அளிக்க நாடாளுமன்றம் 1959-ல் சட்டம் இயற்றியது.",
        fact_en="The core test is whether the government has the power of appointment, removal, and performance control over the office.",
        fact_ta="பதவி நியமனம், நீக்கம் மற்றும் கட்டுப்பாட்டு அதிகாரம் அரசிடம் உள்ளதா என்பதே இதன் முக்கிய சோதனையாகும்.",
        tags=["Office of Profit", "Article 102", "Jaya Bachchan", "Constitutional Silence"]
    ))

    # ER_S_023
    qs.append(make_er_q(
        qid="ER_S_023", diff="Medium", qtype="Multi-Statement", subtopic="Election Expenditure Limits",
        en_stem="Consider the following statements regarding election expenditure limits in India:\n1. Candidate expenditure limits for Lok Sabha in bigger states were increased to ₹95 Lakhs in 2022.\n2. Candidate expenditure limits for State Assemblies in bigger states were increased to ₹40 Lakhs in 2022.\n3. There is a strict statutory ceiling of ₹100 Crore on the total expenditure that a registered political party can incur in a general election.\nWhich of the statements given above are correct?",
        ta_stem="இந்தியாவில் தேர்தல் செலவு வரம்புகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பெரிய மாநிலங்களில் மக்களவை வேட்பாளரின் தேர்தல் செலவு வரம்பு 2022-ல் ₹95 லட்சமாக உயர்த்தப்பட்டது.\n2. பெரிய மாநிலங்களில் சட்டமன்ற வேட்பாளரின் தேர்தல் செலவு வரம்பு 2022-ல் ₹40 லட்சமாக உயர்த்தப்பட்டது.\n3. ஒரு பொதுத்தேர்தலில் பதிவு செய்யப்பட்ட அரசியல் கட்சி செய்யக்கூடிய மொத்த செலவுக்கு ₹100 கோடி என்ற சட்டப்பூர்வ உச்சவரம்பு உள்ளது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under Indian electoral law, there is currently NO statutory ceiling on expenditure by political parties.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் இந்திய தேர்தல் சட்டத்தில் அரசியல் கட்சிகள் செய்யும் செலவுக்கு எவ்வித சட்டப்பூர்வ உச்சவரம்பும் கிடையாது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is false as party expenditure is uncapped.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு (கட்சிகளுக்கு செலவு வரம்பு இல்லை).",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Candidates have spending limits; political parties do NOT have spending limits.",
        tip_ta="வேட்பாளர்களுக்கு செலவு வரம்பு உண்டு; அரசியல் கட்சிகளுக்கு செலவு வரம்பு இல்லை.",
        fact_en="Law Commission and ECI have consistently recommended capping political party spending during elections.",
        fact_ta="அரசியல் கட்சிகளுக்கும் தேர்தல் செலவு வரம்பு விதிக்கப்பட வேண்டும் என சட்ட ஆணையமும் ECI-யும் தொடர்ந்து வலியுறுத்தி வருகின்றன.",
        tags=["Expenditure Limits", "Rule 90", "Uncapped Party Spending"]
    ))

    # ER_S_024
    qs.append(make_er_q(
        qid="ER_S_024", diff="Hard", qtype="Multi-Statement", subtopic="Remote Voting Machine (RVM)",
        en_stem="Consider the following statements regarding the Multi-Constituency Remote EVM (RVM) developed by ECI:\n1. It was developed in collaboration with Bharat Electronics Limited (BEL) and Electronics Corporation of India Limited (ECIL).\n2. A single remote polling unit can handle voting for up to 72 different constituencies simultaneously.\n3. The RVM transmits votes directly over public 5G cellular networks to the central counting server.\nWhich of the statements given above are correct?",
        ta_stem="தேர்தல் ஆணையத்தால் உருவாக்கப்பட்ட பல தொகுதிகளுக்கான தொலைதூர EVM (RVM) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பாரத் எலக்ட்ரானிக்ஸ் (BEL) மற்றும் எலக்ட்ரானிக்ஸ் கார்ப்பரேஷன் ஆஃப் இந்தியா (ECIL) ஆகியவற்றுடன் இணைந்து உருவாக்கப்பட்டது.\n2. ஒரு தொலைதூர வாக்குப்பதிவு அலகு ஒரே நேரத்தில் 72 வெவ்வேறு தொகுதிகளுக்கான வாக்குகளைப் பதிவு செய்ய முடியும்.\n3. இந்த RVM பொது 5G மொபைல் நெட்வொர்க் வழியாக வாக்குகளை மத்திய வாக்கு எண்ணும் சேவையகத்திற்கு நேரடியாக அனுப்புகிறது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the RVM is a completely STANDALONE, non-networked device with no connection to the internet, cellular networks, 5G, or any external wireless interface.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் RVM இணையம், செல்லுலார் நெட்வொர்க் அல்லது 5G போன்ற எவ்வித தொடர்பும் இல்லாத ஒரு தனித்துவமான இயந்திரமாகும் (Standalone).",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is technically false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தொழில்நுட்ப ரீதியாக தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="RVM uses dynamic digital ballot display to switch candidate lists based on the voter's constituency constituency code.",
        tip_ta="வாக்காளரின் தொகுதி குறியீட்டிற்கு ஏற்ப சின்னங்களை மாற்ற RVM டிஜிட்டல் திரையைப் பயன்படுத்துகிறது.",
        fact_en="It was demonstrated to all recognized national and state parties on 16 January 2023.",
        fact_ta="2023 ஜனவரி 16 அன்று அனைத்து அங்கீகரிக்கப்பட்ட கட்சிகளுக்கும் இதன் மாதிரி செயல்விளக்கம் அளிக்கப்பட்டது.",
        tags=["RVM", "72 Constituencies", "BEL ECIL", "Non-Networked"]
    ))

    # ER_S_025
    qs.append(make_er_q(
        qid="ER_S_025", diff="Hard", qtype="Multi-Statement", subtopic="Section 127A Printing Regulations",
        en_stem="Consider the following statements regarding the regulation of election pamphlets and posters under Section 127A of RPA 1951:\n1. Every election pamphlet, poster, or banner must bear on its face the names and addresses of the printer and the publisher.\n2. The printer must obtain a signed declaration as to identity from the publisher attested by two persons.\n3. Section 127A applies exclusively to material printed in the Hindi language only.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 127A-ன் கீழ் தேர்தல் சுவரொட்டிகள் மற்றும் துண்டுப் பிரசுரங்கள் கட்டுப்பாடு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒவ்வொரு தேர்தல் துண்டுப் பிரசுரம் அல்லது சுவரொட்டியிலும் அச்சிட்டவர் மற்றும் வெளியிட்டவரின் பெயர் மற்றும் முகவரிகள் தெளிவாக இருக்க வேண்டும்.\n2. வெளியிடுபவரிடமிருந்து இரு நபர்களால் சான்றளிக்கப்பட்ட அடையாள உறுதிமொழிப் படிவத்தை அச்சுப்பொறி உரிமையாளர் பெற வேண்டும்.\n3. பிரிவு 127A இந்தி மொழியில் அச்சிடப்படும் பொருட்களுக்கு மட்டுமே பிரத்யேகமாக பொருந்தும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 127A applies uniformly to all printed election materials in any language across the territory of India.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 127A எந்த மொழியில் அச்சிடப்பட்ட தேர்தல் பிரச்சாரப் பொருளுக்கும் சமமாகப் பொருந்தும்.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is absurd.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="A copy of the declaration and printed pamphlet must be sent to the District Magistrate or Chief Electoral Officer within a reasonable time.",
        tip_ta="அறிவிக்கை நகலும் அச்சுப் பிரதியும் மாவட்ட நடுவர் அல்லது CEO-விடம் சமர்ப்பிக்கப்பட வேண்டும்.",
        fact_en="Section 127A was enacted to prevent anonymous character assassination and hate literature during elections.",
        fact_ta="பெயர் குறிப்பிடப்படாத அவதூறுகள் மற்றும் வெறுப்புப் பிரச்சாரங்களைத் தடுக்க இப்பிரிவு இயற்றப்பட்டது.",
        tags=["Section 127A", "Printer Publisher Disclosure", "Election Pamphlets"]
    ))

    # ER_S_026
    qs.append(make_er_q(
        qid="ER_S_026", diff="Medium", qtype="Multi-Statement", subtopic="Universal Adult Suffrage Article 326",
        en_stem="Consider the following statements regarding the constitutional framework of franchise under Article 326:\n1. Elections to the Lok Sabha and State Legislative Assemblies are based on adult suffrage.\n2. Every citizen not less than 18 years of age has the right to be registered as an elector unless disqualified.\n3. Property ownership and educational degree are valid constitutional disqualifications for voting under Article 326.\nWhich of the statements given above are correct?",
        ta_stem="சரத்து 326-ன் கீழான வாக்குரிமையின் அரசியலமைப்பு கட்டமைப்பு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மக்களவை மற்றும் மாநில சட்டமன்றங்களுக்கான தேர்தல்கள் வயதுவந்தோர் வாக்குரிமையின் அடிப்படையில் நடத்தப்படுகின்றன.\n2. தகுதிநீக்கம் செய்யப்படாத வரை 18 வயது நிரம்பிய ஒவ்வொரு குடிமகனுக்கும் வாக்காளராகப் பதிவு செய்ய உரிமை உண்டு.\n3. சொத்துரிமை இல்லாமை மற்றும் பட்டப்படிப்பு இல்லாமை ஆகியவை சரத்து 326-ன் கீழ் வாக்களிப்பதற்கான செல்லுபடியாகும் அரசியலமைப்பு தகுதியின்மைகள் ஆகும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because India abolished property, tax, and educational qualifications for voting in 1950. The only grounds of disqualification under Article 326 are non-residence, unsoundness of mind, crime, or corrupt or illegal practice.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் சொத்து அல்லது கல்வித்தகுதி நிபந்தனைகளை 1950-லேயே இந்தியா ஒழித்துவிட்டது. குடியுரிமையின்மை, மனநலக்குறைவு, குற்றவியல் தண்டனை அல்லது ஊழல் நடைமுறைகள் மட்டுமே சரத்து 326-ன் கீழான தகுதியின்மைகள் ஆகும்.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is unconstitutional.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 அரசியலமைப்புக்கு எதிரானது.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="61st Amendment Act, 1988 amended Article 326 to substitute 'eighteen years' for 'twenty-one years'.",
        tip_ta="1988-ன் 61-வது திருத்தம் சரத்து 326-ல் 21 வயதை 18 வயதாகக் குறைத்தது.",
        fact_en="Article 325 mandates a single general electoral roll with no separate electorates based on religion, race, caste, or sex.",
        fact_ta="சரத்து 325 மதம், இனம், ஜாதி, பாலின அடிப்படையிலான தனித் தொகுதிகளைத் தடை செய்து பொது வாக்காளர் பட்டியலை கட்டாயமாக்குகிறது.",
        tags=["Article 326", "Adult Suffrage", "61st Amendment", "Constitutional Disqualifications"]
    ))

    # ER_S_027
    qs.append(make_er_q(
        qid="ER_S_027", diff="Hard", qtype="Multi-Statement", subtopic="Section 123(7) Government Servants Assistance",
        en_stem="Consider the following statements regarding Section 123(7) of the Representation of the People Act, 1951:\n1. Procuring assistance from gazetted officers and police officers for furthering election prospects is a corrupt practice.\n2. In Indira Nehru Gandhi v. Raj Narain (1975), obtaining assistance from a government officer (Yashpal Kapoor) prior to effective resignation was held to violate Section 123(7).\n3. Government doctors and school teachers are classified as Gazetted Class-I Revenue Officers under Section 123(7).\nWhich of the statements given above is/are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 123(7) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தல் வெற்றிக்காக அரசிதழ் பதிவு பெற்ற (Gazetted) அதிகாரிகள் மற்றும் காவல்துறையினரின் உதவியைப் பெறுவது ஊழல் நடைமுறையாகும்.\n2. இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975) வழக்கில், அரசு அதிகாரி (யஷ்பால் கபூர்) ராஜினாமா ஏற்பதற்கு முன் அவரது உதவியைப் பெற்றது பிரிவு 123(7)-ஐ மீறியதாக அலகாபாத் உயர் நீதிமன்றத்தால் தீர்ப்பளிக்கப்பட்டது.\n3. அரசு மருத்துவர்கள் மற்றும் பள்ளி ஆசிரியர்கள் பிரிவு 123(7)-ன் கீழ் அரசிதழ் பதிவு பெற்ற முதல் வகுப்பு வருவாய் அலுவலர்களாக வகைப்படுத்தப்படுகிறார்கள்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because government school teachers and primary doctors are not classified as revenue officers or gazetted magistrates under Section 123(7), though they are public servants.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் அரசு பள்ளி ஆசிரியர்கள் மற்றும் மருத்துவர்கள் பிரிவு 123(7)-ன் கீழ் வருவாய் அல்லது நடுவர் அதிகாரிகளாகக் கருதப்படுவதில்லை.",
        why_a_en="Correct. Statements 1 and 2 are historically and legally accurate.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 வரலாற்று மற்றும் சட்ட ரீதியாக சரியானவை.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Section 123(7) lists: gazetted officers, stipendiary judges/magistrates, armed forces members, police officers, excise officers, and revenue officers.",
        tip_ta="பிரிவு 123(7) பட்டியல்: கெசட்டட் அதிகாரிகள், நீதிபதிகள், ராணுவம், காவல்துறை, கலால் மற்றும் வருவாய்த்துறை அதிகாரிகள்.",
        fact_en="Arranging for barricades, rostrums, and loudspeakers by government personnel on security grounds is exempted under Section 123(7) proviso.",
        fact_ta="பாதுகாப்பு காரணங்களுக்காக அரசு ஊழியர்கள் மேடை அமைப்பது பிரிவு 123(7) வரம்புரையின் கீழ் விலக்கு பெற்றது.",
        tags=["Section 123(7)", "Government Servants", "Indira Gandhi Case 1975"]
    ))

    # ER_S_028
    qs.append(make_er_q(
        qid="ER_S_028", diff="Medium", qtype="Multi-Statement", subtopic="Section 77 Star Campaigners Rules",
        en_stem="Consider the following statements regarding 'Star Campaigners' under Section 77 of RPA 1951:\n1. A recognized political party can nominate a maximum of 40 star campaigners.\n2. A registered unrecognised political party can nominate a maximum of 20 star campaigners.\n3. The travel expenses of star campaigners by air or other transport are added to the election expenditure of the candidate in whose constituency they campaign.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 77-ன் கீழான 'நட்சத்திரப் பிரச்சாரகர்கள்' குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஓர் அங்கீகரிக்கப்பட்ட அரசியல் கட்சி அதிகபட்சமாக 40 நட்சத்திரப் பிரச்சாரகர்களை நியமிக்கலாம்.\n2. ஒரு பதிவு செய்யப்பட்ட அங்கீகாரமற்ற அரசியல் கட்சி அதிகபட்சமாக 20 நட்சத்திரப் பிரச்சாரகர்களை நியமிக்கலாம்.\n3. நட்சத்திரப் பிரச்சாரகர்களின் விமான அல்லது பிற பயணச் செலவுகள் அவர்கள் பிரச்சாரம் செய்யும் வேட்பாளரின் தேர்தல் செலவுக் கணக்கில் சேர்க்கப்படும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under Explanation 1 to Section 77(1), the travel expenditure incurred by star campaigners is EXEMPTED and not deemed to be expenditure incurred by the candidate.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 77(1) விளக்கம் 1-ன் படி, நட்சத்திரப் பிரச்சாரகர்களின் பயணச் செலவு வேட்பாளரின் தேர்தல் கணக்கில் சேர்க்கப்படாமல் சட்டப்பூர்வ விலக்கு பெறுகிறது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is the opposite of the statutory exemption.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; பயணச் செலவு வேட்பாளர் கணக்கில் சேராது என்பதால் கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="List of star campaigners must be submitted to ECI within 7 days of election notification.",
        tip_ta="தேர்தல் அறிவிக்கை வெளியான 7 நாட்களுக்குள் நட்சத்திரப் பிரச்சாரகர் பட்டியல் ECI-யிடம் சமர்ப்பிக்கப்பட வேண்டும்.",
        fact_en="If a star campaigner shares the stage and solicits votes specifically for one candidate alone, stage expenses are apportioned to that candidate.",
        fact_ta="மேடைப் பகிர்வின் போது குறிப்பிட்ட வேட்பாளருக்காக மட்டுமே பிரச்சாரம் செய்தால் மேடைச் செலவு வேட்பாளர் கணக்கில் சேர்க்கப்படும்.",
        tags=["Star Campaigners", "Section 77", "Travel Exemption", "40 Leaders"]
    ))

    # ER_S_029
    qs.append(make_er_q(
        qid="ER_S_029", diff="Hard", qtype="Multi-Statement", subtopic="Section 135A Booth Capturing Offences",
        en_stem="Consider the following statements regarding the offence of 'Booth Capturing' under Section 135A of RPA 1951:\n1. It was made a cognizable criminal offence by an amendment act in 1989.\n2. If committed by a person in government service, it is punishable with imprisonment for a term of not less than 3 years which may extend to 5 years.\n3. Seizure of a polling station or allowing only one party's supporters to vote falls within the definition of booth capturing.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 135A-ன் கீழான 'வாக்குச்சாவடி கைப்பற்றுதல்' குற்றம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 1989 ஆம் ஆண்டு சட்டத்திருத்தத்தின் மூலம் கைது செய்யப்படக்கூடிய குற்றவியல் குற்றமாக்கப்பட்டது.\n2. அரசுப் பணியில் உள்ள ஒரு நபரால் இக்குற்றம் செய்யப்பட்டால், 3 ஆண்டுகளுக்குக் குறையாத மற்றும் 5 ஆண்டுகள் வரை நீட்டிக்கக்கூடிய சிறைத்தண்டனை விதிக்கப்படும்.\n3. வாக்குச்சாவடியை ஆக்கிரமிப்பது அல்லது ஒரு குறிப்பிட்ட கட்சியின் ஆதரவாளர்களை மட்டுமே வாக்களிக்க அனுமதிப்பது ஆகியவை வாக்குச்சாவடி பிடிப்பு வரையறைக்குள் அடங்கும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Section 135A was inserted in 1989; Section 135A(1) prescribes 1 to 3 years prison for general offenders and 3 to 5 years for persons in government service; and the Explanation defines booth capturing broadly to include physical seizure and voter suppression.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பிரிவு 135A 1989-ல் இணைக்கப்பட்டது; அரசு ஊழியர்களுக்கு 3 முதல் 5 ஆண்டுகள் வரை சிறைத்தண்டனை விதிக்கப்படுகிறது; வாக்குச்சாவடி ஆக்கிரமிப்பு மற்றும் குறிப்பிட்ட வாக்காளர்களை மட்டும் அனுமதிப்பது இதன் கீழ் குற்றமாகும்.",
        why_a_en="Correct. All three statements accurately state the law under Section 135A.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் பிரிவு 135A-ன் சட்ட விதிகளை துல்லியமாகக் கூறுகின்றன.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="Booth capturing is also a corrupt practice under Section 123(8) leading to election nullification.",
        tip_ta="வாக்குச்சாவடி பிடிப்பு பிரிவு 123(8)-ன் கீழ் தேர்தலை ரத்து செய்யக்கூடிய ஊழல் நடைமுறையுமாகும்.",
        fact_en="Under Section 58A, ECI can countermand elections in the entire constituency if booth capturing is widespread.",
        fact_ta="பெருமளவில் வாக்குச்சாவடி கைப்பற்றப்பட்டால் பிரிவு 58A-ன் கீழ் முழு தேர்தலையும் ECI ரத்து செய்யலாம்.",
        tags=["Section 135A", "Booth Capturing", "3 to 5 Years Jail", "1989 Amendment"]
    ))

    # ER_S_030
    qs.append(make_er_q(
        qid="ER_S_030", diff="Hard", qtype="Multi-Statement", subtopic="Section 11 Power to Reduce Disqualification",
        en_stem="Consider the following statements regarding the Election Commission's powers under Section 11 of RPA 1951:\n1. ECI has the statutory power to remove or reduce the period of any disqualification incurred under Chapter III (except Section 8A).\n2. ECI must record its reasons in writing when exercising powers under Section 11.\n3. The Supreme Court in 2019 struck down Section 11 as an unconstitutional interference with the judiciary.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 11-ன் கீழான தேர்தல் ஆணையத்தின் அதிகாரங்கள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அத்தியாயம் III-ன் கீழ் ஏற்பட்ட எந்தவொரு தகுதிநீக்கத்தையும் (பிரிவு 8A தவிர) நீக்க அல்லது அதன் கால அளவைக் குறைக்க ECI-க்கு சட்டப்பூர்வ அதிகாரம் உண்டு.\n2. பிரிவு 11-ன் கீழ் அதிகாரத்தைப் பயன்படுத்தும்போது ECI அதற்கான காரணங்களை எழுத்துப்பூர்வமாக பதிவு செய்ய வேண்டும்.\n3. பிரிவு 11 நீதித்துறை அதிகாரத்தில் தலையிடுவதாகக் கூறி 2019-ல் உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்டது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 11 remains fully operational and valid; it was exercised in 2019 to reduce the disqualification of Sikkim Chief Minister Prem Singh Tamang, and its constitutional validity was upheld.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 11 ரத்து செய்யப்படவில்லை; இது இன்றும் முழுமையாக செல்லுபடியாகும் பிரிவாகும். 2019-ல் சிக்கிம் முதல்வர் பிரேம் சிங் தமாங்கின் தகுதிநீக்கக் காலத்தை குறைக்க ECI இதை வெற்றிகரமாகப் பயன்படுத்தியது.",
        why_a_en="Correct. Statements 1 and 2 are true; Section 11 remains valid law.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; பிரிவு 11 செல்லுபடியாகும் சட்டம்.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Disqualifications under Section 8A (Corrupt Practices) are exempt from Section 11 and decided by the President under Section 8A(3).",
        tip_ta="பிரிவு 8A-ன் கீழான ஊழல் நடைமுறை தகுதிநீக்கங்களுக்கு பிரிவு 11 பொருந்தாது; குடியரசுத் தலைவரே முடிவெடுப்பார்.",
        fact_en="Section 11 applies to disqualifications under Section 8, 8A exclusion, 9, 9A, 10, and 10A.",
        fact_ta="பிரிவு 11 என்பது பிரிவு 8, 9, 9A, 10 மற்றும் 10A தகுதிநீக்கங்களுக்குப் பொருந்தும்.",
        tags=["Section 11", "ECI Power to Reduce Disqualification", "Tamang Precedent"]
    ))

    # ER_S_031 to ER_S_050: Continuing with statements testing intricate areas
    # ER_S_031
    qs.append(make_er_q(
        qid="ER_S_031", diff="Medium", qtype="Multi-Statement", subtopic="Postal Ballot Eligibility",
        en_stem="Consider the following statements regarding Postal Ballots in India:\n1. Service voters (armed forces personnel posted away from home) are eligible to vote via Electronically Transmitted Postal Ballot System (ETPBS).\n2. Special voters like the President, Vice-President, and Governors of States can vote by postal ballot under Section 60(b).\n3. Any ordinary citizen on vacation abroad during election week can download and submit a postal ballot online.\nWhich of the statements given above are correct?",
        ta_stem="இந்தியாவில் தபால் வாக்குகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பணி வாக்காளர்கள் (ராணுவ வீரர்கள்) ETPBS மின்னணு அமைப்பு மூலம் தபால் வாக்கு செலுத்த தகுதியுடையவர்கள்.\n2. குடியரசுத் தலைவர், துணைக் குடியரசுத் தலைவர் மற்றும் மாநில ஆளுநர்கள் போன்ற சிறப்பு வாக்காளர்கள் பிரிவு 60(b)-ன் கீழ் தபால் வாக்கு போடலாம்.\n3. தேர்தல் வாரத்தில் வெளிநாட்டில் சுற்றுலா செல்லும் எந்தவொரு சாதாரண குடிமகனும் ஆன்லைனில் தபால் வாக்கை பதிவிறக்கம் செய்து வாக்களிக்கலாம்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because ordinary domestic citizens traveling abroad for tourism or private work CANNOT vote by postal ballot or online; they must be physically present in their polling booth in India.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் வெளிநாடு செல்லும் சாதாரண குடிமக்களுக்கு தபால் வாக்கோ அல்லது ஆன்லைன் வாக்கோ கிடையாது; அவர்கள் நேரில் வந்து மட்டுமே வாக்களிக்க முடியும்.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is completely false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 முற்றிலும் தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Voters on election duty (polling officers, drivers, police) vote by postal ballot using Form 12.",
        tip_ta="தேர்தல் பணியில் உள்ள ஊழியர்கள் படிவம் 12 மூலம் தபால் வாக்கு செலுத்துகின்றனர்.",
        fact_en="Electors subjected to preventive detention vote via postal ballot under Section 60(b) proviso.",
        fact_ta="தடுப்புக் காவலில் உள்ளவர்கள் பிரிவு 60(b) வரம்புரையின் கீழ் தபால் வாக்கு போடுகின்றனர்.",
        tags=["Postal Ballot", "ETPBS", "Service Voters", "Special Voters"]
    ))

    # ER_S_032
    qs.append(make_er_q(
        qid="ER_S_032", diff="Hard", qtype="Multi-Statement", subtopic="Section 125 Promoting Enmity",
        en_stem="Consider the following statements regarding the electoral offence of 'Promoting Enmity' under Section 125 of RPA 1951:\n1. It applies to any person who promotes feelings of enmity between classes of citizens on grounds of religion, race, caste, community, or language in connection with an election.\n2. The offence is punishable with imprisonment for a term which may extend to 3 years, or with fine, or with both.\n3. The trial for an offence under Section 125 can only be conducted before the Supreme Court of India.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 125-ன் கீழான 'பகைமை உணர்வைத் தூண்டுதல்' தேர்தல் குற்றம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தலுடன் தொடர்புடைய வகையில் மதம், இனம், ஜாதி, சமூகம் அல்லது மொழி அடிப்படையில் குடிமக்களிடையே பகைமை உணர்வை தூண்டும் எவருக்கும் இது பொருந்தும்.\n2. இக்குற்றத்திற்கு 3 ஆண்டுகள் வரை நீட்டிக்கக்கூடிய சிறைத்தண்டனை, அல்லது அபராதம், அல்லது இரண்டும் விதிக்கப்படலாம்.\n3. பிரிவு 125-ன் கீழான குற்ற விசாரணை இந்திய உச்ச நீதிமன்றத்தில் மட்டுமே நடத்தப்பட வேண்டும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 125 is a criminal offence tried in regular Judicial Magistrate / Sessions courts, not exclusively in the Supreme Court.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 125 என்பது வழக்கமான குற்றவியல் நீதிமன்றங்களில் விசாரிக்கப்படும் குற்றமாகும், உச்ச நீதிமன்றத்தில் மட்டுமே அல்ல.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is legally absurd.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Do not confuse: Section 123(3A) is a CORRUPT PRACTICE (voids election in High Court); Section 125 is an ELECTORAL OFFENCE (sends offender to prison).",
        tip_ta="குழப்ப வேண்டாம்: பிரிவு 123(3A) என்பது ஊழல் நடைமுறை (தேர்தல் ரத்தாகும்); பிரிவு 125 என்பது தேர்தல் குற்றம் (சிறைத் தண்டனை கிடைக்கும்).",
        fact_en="Section 125 was inserted into RPA 1951 by an amendment in 1961.",
        fact_ta="1961 சட்டத்திருத்தத்தின் மூலம் பிரிவு 125 சேர்க்கப்பட்டது.",
        tags=["Section 125", "Promoting Enmity", "3 Years Imprisonment", "Electoral Offence"]
    ))

    # ER_S_033
    qs.append(make_er_q(
        qid="ER_S_033", diff="Hard", qtype="Multi-Statement", subtopic="Section 135B Paid Holiday Exceptions",
        en_stem="Consider the following statements regarding the right to a paid holiday on polling day under Section 135B of RPA 1951:\n1. It applies to every person employed in any business, trade, industrial undertaking, or commercial establishment.\n2. No deduction or abatement of wages can be made on account of the polling day holiday.\n3. The provision applies even to an employee whose absence would cause danger or substantial loss in respect of the employment.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 135B-ன் கீழான தேர்தல் ஊதிய விடுமுறை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வணிகம், தொழில் அல்லது வணிக நிறுவனங்களில் பணிபுரியும் ஒவ்வொரு தொழிலாளிக்கும் இது பொருந்தும்.\n2. இந்த தேர்தல் விடுமுறைக்காக தொழிலாளியின் ஊதியத்தில் எவ்வித பிடித்தமும் செய்யக் கூடாது.\n3. ஒரு பணியாளர் பணிக்கு வராவிட்டால் வேலையில் ஆபத்தோ அல்லது பெரும் நஷ்டமோ ஏற்படும் சூழ்நிலையிலும் கூட இச்சலுகை கட்டாயம் பொருந்தும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 135B(4) explicitly provides an exception: this section does NOT apply to any elector whose absence would cause danger or substantial loss in respect of the employment in which he is engaged (e.g. critical continuous-process plant engineers, intensive care doctors).",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 135B(4) தெளிவான விதிவிலக்கை அளிக்கிறது: பணியாளர் வராவிட்டால் உயிருக்கோ அல்லது பணிக்கு பெரும் ஆபத்தோ நஷ்டமோ ஏற்படும் சூழ்நிலைகளில் உள்ள பணியாளர்களுக்கு (எ.கா. தீவிர சிகிச்சைப் பிரிவு மருத்துவர்கள்) இது பொருந்தாது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 ignores the explicit statutory exception under Section 135B(4).",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; பிரிவு 135B(4)-ல் விதிவிலக்கு உள்ளதால் கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Section 135B applies only if the employee is an elector in the constituency where poll is being held.",
        tip_ta="தேர்தல் நடைபெறும் தொகுதியில் வாக்காளராக உள்ள பணியாளர்களுக்கு மட்டுமே இந்த விடுமுறை உரிமை உண்டு.",
        fact_en="Employers violating Section 135B are punishable with a fine of up to ₹500.",
        fact_ta="பிரிவு 135B-ஐ மீறும் முதலாளிகளுக்கு ₹500 வரை அபராதம் விதிக்கப்படும்.",
        tags=["Section 135B", "Paid Holiday", "Section 135B(4) Exception"]
    ))

    # ER_S_034
    qs.append(make_er_q(
        qid="ER_S_034", diff="Medium", qtype="Multi-Statement", subtopic="Section 135C Dry Day Enforcement",
        en_stem="Consider the following statements regarding the ban on sale of liquor during elections under Section 135C of RPA 1951:\n1. No intoxicating liquor shall be sold, given, or distributed at any shop, hotel, or tavern within a polling area during 48 hours ending with poll conclusion.\n2. Violation of Section 135C is punishable with imprisonment up to 6 months or fine up to ₹2,000 or both.\n3. Private consumption of lawfully purchased liquor inside a citizen's own home is punishable with 5 years rigorous imprisonment.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 135C-ன் கீழ் தேர்தல் கால மது விற்பனை தடை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வாக்குப்பதிவு முடிவடையும் நேரத்திற்கு முந்தைய 48 மணி நேரத்தில் தேர்தல் பகுதியில் உள்ள கடைகள், ஹோட்டல்களில் மதுபானங்களை விற்கவோ வழங்கவோ கூடாது.\n2. பிரிவு 135C-ஐ மீறினால் 6 மாதங்கள் வரை சிறைத்தண்டனை அல்லது ₹2,000 வரை அபராதம் அல்லது இரண்டும் விதிக்கப்படும்.\n3. ஒரு குடிமகன் தனது சொந்த வீட்டிற்குள் தனிப்பட்ட முறையில் முன்கூட்டியே வாங்கிய மதுவை அருந்துவதற்கு 5 ஆண்டுகள் கடுமையான சிறைத்தண்டனை உண்டு.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 135C prohibits the SALE, GIVING, and DISTRIBUTION of liquor; it does not prescribe a 5-year prison sentence for lawful private home consumption.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 135C மது விற்பனை மற்றும் பொது விநியோகத்தை மட்டுமே தடை செய்கிறது; தனிப்பட்ட நபருக்கு 5 ஆண்டு சிறைத் தண்டனை விதிக்கும் விதி இதில் இல்லை.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is incorrect.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Dry days ensure that alcohol is not used to bribe, induce, or intoxicate voters before casting ballots.",
        tip_ta="வாக்காளர்களுக்கு மது கொடுத்து வாக்கு சேகரிப்பதைத் தடுக்கவே தேர்தல் அமைதிக்காலத்தில் 'டிரை டே' கடைபிடிக்கப்படுகிறது.",
        fact_en="Section 135C applies to clubs, restaurants, and eating places as well.",
        fact_ta="விடுதிகள், கிளப்புகள் மற்றும் உணவகங்களுக்கும் பிரிவு 135C தடை பொருந்தும்.",
        tags=["Section 135C", "Liquor Ban", "Dry Day", "48 Hours Window"]
    ))

    # ER_S_035
    qs.append(make_er_q(
        qid="ER_S_035", diff="Hard", qtype="Multi-Statement", subtopic="Section 131 Disorderly Conduct",
        en_stem="Consider the following statements regarding the maintenance of order at polling stations under Section 131 of RPA 1951:\n1. Using megaphones or loudspeakers within or at the entrance of a polling station is strictly prohibited.\n2. Any person who disobeys the lawful directions of the Presiding Officer may be removed from the polling station by a police officer.\n3. Any person removed who re-enters without permission is punishable with imprisonment up to 3 months or fine or both.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 131-ன் கீழ் வாக்குச்சாவடிகளில் அமைதியைப் பராமரிப்பது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வாக்குச்சாவடிக்குள்ளோ அல்லது அதன் நுழைவாயிலிலோ ஒலிபெருக்கிகள் அல்லது மெகாபோன்களைப் பயன்படுத்துவது தடை செய்யப்பட்டுள்ளது.\n2. வாக்குச்சாவடி தலைமை அலுவலரின் சட்டப்பூர்வ உத்தரவுகளை மதிக்காத எந்தவொரு நபரையும் காவல்துறையினர் வாக்குச்சாவடியை விட்டு வெளியேற்றலாம்.\n3. வெளியேற்றப்பட்ட நபர் அனுமதியின்றி மீண்டும் உள்ளே நுழைந்தால் 3 மாதங்கள் வரை சிறைத்தண்டனை அல்லது அபராதம் விதிக்கப்படலாம்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Section 131(1) prohibits megaphones/loudspeakers; Section 131(2) empowers the Presiding Officer to have disorderly persons removed by police; and Section 131(3) prescribes imprisonment up to 3 months or fine or both for unauthorized re-entry.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பிரிவு 131(1) ஒலிபெருக்கிகளைத் தடை செய்கிறது; பிரிவு 131(2) ஒழுங்கீனமாக நடப்பவரை காவல்துறையினர் வெளியேற்ற அதிகாரம் அளிக்கிறது; பிரிவு 131(3) அனுமதியின்றி மீண்டும் நுழைந்தால் 3 மாத சிறை அல்லது அபராதம் விதிக்கிறது.",
        why_a_en="Correct. All three statements accurately state the provisions of Section 131.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் பிரிவு 131-ன் துல்லியமான சட்ட விதிகள்.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="Section 132 independently provides a 3-month prison sentence for failure to obey lawful commands of the Presiding Officer.",
        tip_ta="பிரிவு 132 தலைமை அலுவலரின் உத்தரவை மதிக்காதவர்களுக்கு 3 மாத சிறைத்தண்டனை விதிக்கிறது.",
        fact_en="Presiding Officers are vested with magisterial powers inside the polling station.",
        fact_ta="வாக்குச்சாவடிக்குள் தலைமை அலுவலருக்கு நடுவர் (Magisterial) அதிகாரங்கள் உண்டு.",
        tags=["Section 131", "Disorderly Conduct", "Presiding Officer Authority"]
    ))

    # ER_S_036
    qs.append(make_er_q(
        qid="ER_S_036", diff="Medium", qtype="Multi-Statement", subtopic="Recognition Criteria State Party",
        en_stem="Consider the following statements regarding criteria for recognition as a 'State Party' under the Election Symbols Order, 1968:\n1. Winning at least 3% of total seats or at least 3 seats in the Legislative Assembly, whichever is more.\n2. Securing at least 8% of the total valid votes polled in the state in a general election to the Assembly or Lok Sabha, even without winning any seat.\n3. Winning all Rajya Sabha seats allocated to that state in the biennial elections.\nWhich of the statements given above are correct?",
        ta_stem="தேர்தல் சின்னங்கள் ஆணை 1968-ன் கீழ் 'மாநிலக் கட்சி' அங்கீகாரம் பெறுவதற்கான அளவுகோல்கள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சட்டமன்றத்தில் மொத்த இடங்களில் குறைந்தது 3% அல்லது குறைந்தது 3 இடங்களில் வெற்றி பெறுதல் (எது அதிகமோ அது).\n2. சட்டமன்ற அல்லது மக்களவைத் தேர்தலில் எவ்வித இடங்களையும் வெல்லாவிட்டாலும், மாநிலத்தில் பதிவான செல்லுபடியாகும் வாக்குகளில் குறைந்தது 8% வாக்குகள் பெறுதல்.\n3. ஈராண்டுத் தேர்தலில் அந்த மாநிலத்திற்கு ஒதுக்கப்பட்ட அனைத்து மாநிலங்களவை இடங்களையும் வெல்லுதல்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Rajya Sabha elections are indirect elections and are not criteria for statutory party recognition under the Symbols Order.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் மாநிலங்களவைத் தேர்தல் மறைமுகத் தேர்தல் என்பதால் அது கட்சி அங்கீகாரத்திற்கான அளவுகோலாகக் கருதப்படுவதில்லை.",
        why_a_en="Correct. Statements 1 and 2 are statutory criteria; statement 3 is irrelevant.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சட்டப்பூர்வ தகுதிகள்; கூற்று 3 பொருத்தமற்றது.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="The 8% vote share criterion (Statement 2) was introduced by ECI in 2011.",
        tip_ta="8% வாக்கு வங்கி நிபந்தனை (கூற்று 2) 2011-ல் ECI-யால் சேர்க்கப்பட்டது.",
        fact_en="Another criterion is securing 6% valid votes in Assembly + winning at least 2 Assembly seats.",
        fact_ta="சட்டசபையில் 6% வாக்குகள் + 2 இடங்களில் வெற்றி என்பதும் மற்றொரு தகுதியாகும்.",
        tags=["State Party Criteria", "Symbols Order 1968", "8 Percent Vote Share"]
    ))

    # ER_S_037
    qs.append(make_er_q(
        qid="ER_S_037", diff="Medium", qtype="Multi-Statement", subtopic="National Party Criteria",
        en_stem="Consider the following statements regarding criteria for recognition as a 'National Party' under the Election Symbols Order, 1968:\n1. Recognition as a State Party in at least four (4) states.\n2. Winning at least 2% of total Lok Sabha seats (11 seats) elected from at least three different states.\n3. Securing at least 6% of valid votes in four or more states in Lok Sabha or Assembly elections, AND winning at least 4 Lok Sabha seats.\nWhich of the statements given above are correct?",
        ta_stem="தேர்தல் சின்னங்கள் ஆணை 1968-ன் கீழ் 'தேசியக் கட்சி' அங்கீகாரம் பெறுவதற்கான தகுதிகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. குறைந்தது நான்கு (4) மாநிலங்களில் மாநிலக் கட்சியாக அங்கீகரிக்கப்பட்டிருத்தல்.\n2. குறைந்தது மூன்று வெவ்வேறு மாநிலங்களிலிருந்து தேர்ந்தெடுக்கப்பட்ட மக்களவையின் மொத்த இடங்களில் குறைந்தது 2% (11 இடங்கள்) வெற்றி பெறுதல்.\n3. நான்கு அல்லது அதற்கு மேற்பட்ட மாநிலங்களில் மக்களவை அல்லது சட்டமன்றத் தேர்தலில் 6% வாக்குகள் பெறுவதுடன், குறைந்தது 4 மக்களவைத் தொகுதிகளில் வெற்றி பெறுதல்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Paragraph 6B of the Symbols Order lays down these three alternative routes to becoming a recognized National Party: (1) 4-state recognition, (2) 2% Lok Sabha seats across 3 states, or (3) 6% votes in 4 states + 4 Lok Sabha seats.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பத்தி 6B தேசியக் கட்சியாக அங்கீகாரம் பெற இந்த 3 மாற்று வழிகளை வழங்குகிறது: (1) 4 மாநிலங்களில் அங்கீகாரம், (2) 3 மாநிலங்களிலிருந்து 2% மக்களவை இடங்கள் வெற்றி, (3) 4 மாநிலங்களில் 6% வாக்குகள் + 4 மக்களவை இடங்கள் வெற்றி.",
        why_a_en="Correct. All three statements accurately state the alternative National Party criteria.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் தேசியக் கட்சிக்கான 3 மாற்று வழிகளைச் சரியாகக் கூறுகின்றன.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="In 2016, ECI amended the rules to review national/state party status every 10 years (two consecutive elections) instead of every 5 years.",
        tip_ta="2016-ல் விதிகள் திருத்தப்பட்டு கட்சி அந்தஸ்து 5 ஆண்டுகளுக்கு ஒருமுறை என்பதற்குப் பதிலாக 10 ஆண்டுகளுக்கு (இரு தேர்தல்கள்) ஒருமுறை மறுஆய்வு செய்யப்படுகிறது.",
        fact_en="AAP became a National Party under Criterion 1 (recognized in Delhi, Punjab, Goa, and Gujarat).",
        fact_ta="ஆம் ஆத்மி கட்சி முதல் தகுதியின் (4 மாநில அங்கீகாரம்) கீழ் தேசியக் கட்சியானது.",
        tags=["National Party Criteria", "Symbols Order", "Paragraph 6B"]
    ))

    # ER_S_038
    qs.append(make_er_q(
        qid="ER_S_038", diff="Hard", qtype="Multi-Statement", subtopic="Section 160 Compensation for Requisitioning",
        en_stem="Consider the following statements regarding the requisitioning of vehicles and premises under Sections 160 and 161 of RPA 1951:\n1. State Governments may requisition any premises or vehicles for polling, transport of ballot boxes, or security personnel.\n2. Premises exclusively used as a place of religious worship are exempt from requisitioning.\n3. The owner of the requisitioned vehicle is not entitled to any compensation from the government.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 160 மற்றும் 161-ன் கீழ் வாகனங்கள் மற்றும் வளாகங்களை கையகப்படுத்துவது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வாக்குப்பதிவு, வாக்குப்பெட்டி போக்குவரத்து அல்லது பாதுகாப்புப் பணிகளுக்காக எந்தவொரு வளாகம் அல்லது வாகனத்தை மாநில அரசு கையகப்படுத்தலாம்.\n2. பிரத்யேகமாக மத வழிபாட்டுத் தலங்களாகப் பயன்படுத்தப்படும் வளாகங்களுக்கு கையகப்படுத்துதலிலிருந்து விலக்கு உண்டு.\n3. கையகப்படுத்தப்பட்ட வாகனத்தின் உரிமையாளருக்கு அரசிடமிருந்து எவ்வித இழப்பீடும் கோர உரிமை இல்லை.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 161 explicitly mandates that whenever any vehicle, vessel, or animal is requisitioned, there SHALL be paid to the owner compensation determined on the basis of prevailing commercial fares or rates.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 161 கையகப்படுத்தப்பட்ட வாகனங்கள், படகுகள் மற்றும் விலங்குகளின் உரிமையாளர்களுக்கு சந்தை விகிதத்தின் அடிப்படையில் இழப்பீடு வழங்குவதைக் கட்டாயமாக்குகிறது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 violates Section 161.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; இழப்பீடு கட்டாயம் என்பதால் கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="If the owner disputes the compensation amount, an arbitrator appointed by the State Government determines the fair compensation under Section 161(1).",
        tip_ta="இழப்பீட்டுத் தொகையில் தகராறு ஏற்பட்டால் நடுவர் (Arbitrator) நியமிக்கப்பட்டு தீர்வு காணப்படும்.",
        fact_en="Private vehicles used by candidate or their election agent cannot be requisitioned under Section 160 proviso.",
        fact_ta="வேட்பாளர் அல்லது முகவர் பிரச்சாரத்திற்கு பயன்படுத்தும் சொந்த வாகனங்களை கையகப்படுத்த விலக்கு உண்டு.",
        tags=["Section 160", "Section 161", "Requisition Compensation", "Religious Exemption"]
    ))

    # ER_S_039
    qs.append(make_er_q(
        qid="ER_S_039", diff="Hard", qtype="Multi-Statement", subtopic="Section 16 Disqualification from Electoral Roll",
        en_stem="Consider the following statements regarding disqualification for registration in an electoral roll under Section 16 of RPA 1950:\n1. A person who is not a citizen of India is disqualified from enrollment.\n2. A person who is of unsound mind and stands so declared by a competent court is disqualified.\n3. A person disqualified from voting under election laws relating to corrupt practices cannot be registered in any electoral roll.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1950 பிரிவு 16-ன் கீழ் வாக்காளர் பட்டியலில் பதிவு செய்வதற்கான தகுதியின்மைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திய குடிமகனாக இல்லாத ஒரு நபர் பட்டியலில் பதிவு செய்ய தகுதியற்றவர்.\n2. மனநலம் குன்றியவர் என தகுதிவாய்ந்த நீதிமன்றத்தால் அறிவிக்கப்பட்ட ஒரு நபர் தகுதியற்றவர்.\n3. ஊழல் நடைமுறைகள் தொடர்பான தேர்தல் சட்டங்களின் கீழ் வாக்களிக்க தகுதிநீக்கம் செய்யப்பட்ட ஒருவர் எந்த வாக்காளர் பட்டியலிலும் பதிவு செய்ய முடியாது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Section 16(1) of RPA 1950 lists non-citizenship, declared unsound mind, and election-law disqualifications as the three statutory grounds barring registration in the electoral roll.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பிரிவு 16(1) குடியுரிமையின்மை, நீதிமன்றத்தால் அறிவிக்கப்பட்ட மனநலக்குறைவு, மற்றும் தேர்தல் குற்றங்களுக்கான தகுதிநீக்கம் ஆகிய மூன்றையும் வாக்காளர் பட்டியலில் சேர்ப்பதற்கான தகுதியின்மைகளாகப் பட்டியலிடுகிறது.",
        why_a_en="Correct. All three statements accurately state Section 16(1) grounds.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் பிரிவு 16(1)-ன் தகுதியின்மைகளைச் சரியாகக் கூறுகின்றன.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="Under Section 16(2), if the disqualification is removed, the person's name is restored to the electoral roll.",
        tip_ta="பிரிவு 16(2)-ன் படி தகுதியின்மை நீங்கியவுடன் அவரது பெயர் மீண்டும் பட்டியலில் சேர்க்கப்படும்.",
        fact_en="Article 326 authorizes Parliament to prescribe these disqualifications by law.",
        fact_ta="சரத்து 326 நாடாளுமன்றத்திற்கு இத்தகுதியின்மைகளை சட்டமியற்றி வகுக்க அதிகாரம் அளிக்கிறது.",
        tags=["Section 16", "Electoral Roll Disqualification", "RPA 1950"]
    ))

    # ER_S_040
    qs.append(make_er_q(
        qid="ER_S_040", diff="Hard", qtype="Multi-Statement", subtopic="Section 14(b) Qualifying Dates Expansion",
        en_stem="Consider the following statements regarding the expansion of qualifying dates under the Election Laws (Amendment) Act, 2021:\n1. The amendment substituted one qualifying date (1st January) with four qualifying dates (1st Jan, 1st Apr, 1st Jul, 1st Oct).\n2. A citizen turning 18 on 2nd January can now enroll with effect from 1st April of that same year.\n3. The four qualifying dates apply exclusively to municipal panchayat elections and do not apply to Lok Sabha elections.\nWhich of the statements given above are correct?",
        ta_stem="தேர்தல் சட்டங்கள் திருத்தச் சட்டம் 2021-ன் கீழ் தகுதி தேதிகள் விரிவாக்கம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இத்திருத்தம் ஒரு தகுதி தேதி (ஜனவரி 1) என்பதற்குப் பதிலாக நான்கு தகுதி தேதிகளை (ஜன 1, ஏப் 1, ஜூலை 1, அக் 1) கொண்டுவந்தது.\n2. ஜனவரி 2 அன்று 18 வயதை அடையும் ஒரு குடிமகன் அதே ஆண்டின் ஏப்ரல் 1 முதல் வாக்காளராகப் பதிவு செய்ய முடியும்.\n3. இந்த நான்கு தகுதி தேதிகள் நகராட்சி பஞ்சாயத்து தேர்தல்களுக்கு மட்டுமே பொருந்தும், மக்களவைத் தேர்தலுக்குப் பொருந்தாது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 14(b) of RPA 1950 applies directly to Parliamentary and Assembly constituencies across India.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் மக்கள் பிரதிநிதித்துவச் சட்டம் 1950 பிரிவு 14(b) நாடாளுமன்ற மற்றும் சட்டமன்ற தொகுதிகளுக்கான வாக்காளர் பட்டியலுக்கே முதன்மையாகப் பொருந்தும்.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is legally incorrect.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 சட்டப்படி தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Youth turning 18 in any quarter can enroll quarterly without waiting for an entire year.",
        tip_ta="ஒவ்வொரு காலாண்டிலும் 18 வயதை அடையும் இளைஞர்கள் ஓராண்டு வரை காத்திருக்காமல் உடனே இணையலாம்.",
        fact_en="ECI now allows 17-year-olds to submit advance registration forms.",
        fact_ta="17 வயது நிரம்பியவர்களே முன்கூட்டியே விண்ணப்பிக்க ECI தற்போது அனுமதிக்கிறது.",
        tags=["Section 14(b)", "4 Qualifying Dates", "Youth Enrollment", "2021 Amendment"]
    ))

    # ER_S_041
    qs.append(make_er_q(
        qid="ER_S_041", diff="Hard", qtype="Multi-Statement", subtopic="Section 125A False Affidavit Penalties",
        en_stem="Consider the following statements regarding Section 125A of RPA 1951 (Offences relating to candidate affidavits):\n1. It penalizes failing to furnish required information or concealing information in Form 26.\n2. It prescribes punishment with imprisonment for a term which may extend to 6 months, or with fine, or with both.\n3. The Law Commission (244th Report) recommended increasing the punishment to at least 2 years imprisonment to trigger automatic disqualification.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 125A (உறுதிமொழிப் பத்திரம் தொடர்பான குற்றங்கள்) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. படிவம் 26-ல் தேவையான தகவல்களைத் தராமல் விடுவது அல்லது தகவல்களை மறைப்பது தண்டனைக்குரிய குற்றமாகும்.\n2. இதற்கு 6 மாதங்கள் வரை நீட்டிக்கக்கூடிய சிறைத்தண்டனை, அல்லது அபராதம், அல்லது இரண்டும் தண்டனையாக விதிக்கப்படலாம்.\n3. தானியங்கி தகுதிநீக்கம் அமலாகும் வகையில் இதன் தண்டனையை குறைந்தது 2 ஆண்டுகள் சிறையாக உயர்த்த சட்ட ஆணையம் (244-வது அறிக்கை) பரிந்துரைத்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Section 125A punishes false affidavits with up to 6 months prison; and both the Law Commission (244th Report) and ECI have recommended increasing it to 2+ years prison so that a conviction triggers immediate disqualification under Section 8(3).",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பிரிவு 125A தவறான உறுதிமொழிப் பத்திரத்திற்கு 6 மாதம் வரை சிறை தண்டனை விதிக்கிறது; பிரிவு 8(3)-ன் கீழ் தானியங்கி தகுதிநீக்கம் அமலுக்கு வர இதன் தண்டனையை 2 ஆண்டுகளாக உயர்த்த சட்ட ஆணையம் பரிந்துரைத்தது.",
        why_a_en="Correct. All three statements accurately state the law and reform recommendations.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் சட்டம் மற்றும் சீர்திருத்த பரிந்துரைகளை சரியாகக் கூறுகின்றன.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="A conviction under Section 125A currently does NOT trigger disqualification under Section 8(3) because the sentence is below 2 years.",
        tip_ta="தற்போது பிரிவு 125A-ன் கீழ் தண்டனை பெற்றால் தகுதிநீக்கம் ஆக மாட்டார்கள்; ஏனெனில் தண்டனை 2 ஆண்டுகளுக்குக் குறைவு.",
        fact_en="Section 125A was inserted into RPA 1951 in August 2002.",
        fact_ta="2002 ஆகஸ்டில் பிரிவு 125A சட்டத்தில் சேர்க்கப்பட்டது.",
        tags=["Section 125A", "False Affidavits", "244th Law Commission", "Disqualification Trigger"]
    ))

    # ER_S_042
    qs.append(make_er_q(
        qid="ER_S_042", diff="Medium", qtype="Multi-Statement", subtopic="Election Digital Portals",
        en_stem="Consider the following pairs of ECI digital applications and their specific functions:\n1. cVIGIL – Fast-track reporting of Model Code of Conduct and expenditure violations by citizens within a 100-minute resolution turnaround.\n2. Suvidha – Single-window portal for candidate permissions, rally grounds, and nomination processing.\n3. Saksham – Accessible mobile app customized for Persons with Disabilities (PwDs) for wheelchair requests and home voting.\nWhich of the pairs given above are correctly matched?",
        ta_stem="இந்திய தேர்தல் ஆணையத்தின் டிஜிட்டல் செயலிகள் மற்றும் அவற்றின் பயன்பாடுகள் குறித்த பின்வரும் இணைகளைக் கவனியுங்கள்:\n1. cVIGIL – பொதுமக்கள் தேர்தல் நடத்தை விதிமீறல்களைப் புகாரளிக்க 100 நிமிட நடவடிக்கை உத்தரவாதத்துடன் கூடிய செயலி.\n2. சுவிதா (Suvidha) – வேட்பாளர்கள் தேர்தல் பொதுக்கூட்ட அனுமதி, மைதான முன்பதிவு பெறுவதற்கான ஒற்றைச் சாளர தளம்.\n3. சக்ஷம் (Saksham) – மாற்றுத்திறனாளிகள் சக்கர நாற்காலி மற்றும் வீட்டு வாக்களிப்பு வசதியைப் பெற உதவும் பிரத்யேக செயலி.\nமேற்கண்ட இணைகளில் சரியாகப் பொருந்தியுள்ளது எது/எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three pairs are correctly matched. cVIGIL is citizen vigilance for MCC violations (100-min turnaround); Suvidha is for candidate campaign permissions; and Saksham is the accessibility portal for PwD voters.",
        exp_ta="மூன்று இணைகளும் சரியாகப் பொருந்தியுள்ளன. cVIGIL 100 நிமிட தேர்தல் விதிமீறல் தீர்வுக்கானது; சுவிதா வேட்பாளர் பிரச்சார அனுமதிக்கானது; சக்ஷம் மாற்றுத்திறனாளிகளுக்கான சேவைகளுக்கானது.",
        why_a_en="Correct. All three pairs are accurate ECI technical applications.",
        why_a_ta="சரியானது. மூன்று இணைகளும் துல்லியமான ECI டிஜிட்டல் பயன்பாடுகள்.",
        why_b_en="Incorrect. Pair 3 is also correct.",
        why_b_ta="தவறானது. இணை 3-ம் சரியானது.",
        why_c_en="Incorrect. Pair 1 is also correct.",
        why_c_ta="தவறானது. இணை 1-ம் சரியானது.",
        why_d_en="Incorrect. Pair 2 is also correct.",
        why_d_ta="தவறானது. இணை 2-ம் சரியானது.",
        tip_en="ENCORE is the internal backend software used by Returning Officers for counting and trend dissemination.",
        tip_ta="ENCORE என்பது வாக்கு எண்ணிக்கை மற்றும் முடிவுகளுக்காக தேர்தல் நடத்தும் அலுவலர்கள் பயன்படுத்தும் உள்-மென்பொருளாகும்.",
        fact_en="Know Your Candidate (KYC) app displays candidate affidavits directly to voters.",
        fact_ta="KYC செயலி வேட்பாளர்களின் குற்றப்பின்னணியை வாக்காளர்களுக்கு நேரடியாகக் காட்டுகிறது.",
        tags=["ECI Apps", "cVIGIL", "Suvidha", "Saksham", "Digital Reforms"]
    ))

    # ER_S_043
    qs.append(make_er_q(
        qid="ER_S_043", diff="Hard", qtype="Multi-Statement", subtopic="Section 169 lays rules before Parliament",
        en_stem="Consider the following statements regarding the rule-making procedure under Section 169 of RPA 1951:\n1. The Central Government has the statutory power to make rules after consulting the Election Commission.\n2. Every rule made under Section 169 must be laid before each House of Parliament for a total period of 30 days.\n3. If both Houses of Parliament agree in making any modification in the rule, the rule shall thereafter have effect only in such modified form.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 169-ன் கீழான விதி இயற்றும் நடைமுறை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தல் ஆணையத்தைக் கலந்தாலோசித்த பின்னர் விதிகளை உருவாக்கும் சட்டப்பூர்வ அதிகாரம் மத்திய அரசிடம் உள்ளது.\n2. பிரிவு 169-ன் கீழ் உருவாக்கப்படும் ஒவ்வொரு விதியும் நாடாளுமன்றத்தின் இரு அவைகளிலும் மொத்தம் 30 நாட்கள் பார்வைக்கு வைக்கப்பட வேண்டும்.\n3. நாடாளுமன்றத்தின் இரு அவைகளும் அவ்விதியில் ஏதேனும் திருத்தம் செய்ய ஒப்புக்கொண்டால், அதன் பின்னர் அந்த திருத்தப்பட்ட வடிவிலேயே அவ்விதி அமலுக்கு வரும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Section 169(1) empowers Central Government to make rules after consulting ECI; Section 169(3) mandates laying rules before Parliament for 30 days; and Section 169(3) proviso provides that parliamentary modifications or annulments govern the rule thereafter.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பிரிவு 169(1) ECI-யைக் கலந்தாலோசித்து மத்திய அரசு விதி இயற்ற அதிகாரம் அளிக்கிறது; பிரிவு 169(3) 30 நாட்கள் நாடாளுமன்ற பார்வைக்கு வைக்க கட்டாயமாக்குகிறது; நாடாளுமன்றம் செய்யும் மாற்றங்கள் விதியில் செல்லும்.",
        why_a_en="Correct. All three statements accurately state the delegated legislation procedure under Section 169.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் பிரிவு 169-ன் ஒப்படைக்கப்பட்ட சட்டமியற்றும் அதிகாரத்தை சரியாகக் கூறுகின்றன.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="This is standard delegated legislation oversight ensuring executive rules remain subordinate to Parliament.",
        tip_ta="அரசு உருவாக்கும் தேர்தல் விதிகள் நாடாளுமன்றத்திற்கு கட்டுப்பட்டவை என்பதை உறுதி செய்யும் விதி இதுவாகும்.",
        fact_en="Conduct of Elections Rules, 1961 were framed under Section 169.",
        fact_ta="1961 தேர்தல் நடத்தை விதிகள் இப்பிரிவு 169-ன் கீழேயே உருவாக்கப்பட்டன.",
        tags=["Section 169", "Delegated Legislation", "Parliamentary Oversight", "Rule Making"]
    ))

    # ER_S_044
    qs.append(make_er_q(
        qid="ER_S_044", diff="Hard", qtype="Multi-Statement", subtopic="Section 28A Deemed Deputation Discipline",
        en_stem="Consider the following statements regarding the disciplinary control of ECI over officers on deemed deputation under Section 28A of RPA 1951:\n1. All Returning Officers, Assistant Returning Officers, and designated police personnel are deemed to be on deputation to the ECI during elections.\n2. The ECI can directly place any officer on suspension or initiate disciplinary proceedings for election misconduct without seeking prior state government approval.\n3. The deemed deputation period continues indefinitely for 5 years until the next general election takes place.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 28A-ன் கீழ் அயல்பணி (Deputation) அலுவலர்கள் மீது தேர்தல் ஆணையத்தின் ஒழுங்கு நடவடிக்கை அதிகாரம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அனைத்து தேர்தல் நடத்தும் அலுவலர்கள், உதவி தேர்தல் நடத்தும் அலுவலர்கள் மற்றும் காவல்துறை அதிகாரிகள் தேர்தலின் போது ECI-ன் அயல்பணியில் இருப்பதாகக் கருதப்படுவர்.\n2. தேர்தல் முறைகேடுகளில் ஈடுபடும் அதிகாரிகளை மாநில அரசின் முன்-அனுமதியின்றி நேரடியாக சஸ்பெண்ட் செய்யவோ ஒழுங்கு நடவடிக்கை எடுக்கவோ ECI-க்கு அதிகாரம் உண்டு.\n3. இந்த அயல்பணி கால அளவு அடுத்த பொதுத்தேர்தல் நடைபெறும் வரை 5 ஆண்டுகளுக்கு காலவரையின்றி நீடிக்கும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 28A explicitly defines the period of deemed deputation as commencing on the date of election notification and ENDING with the declaration of the election results, not for 5 years.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 28A-ன் படி அயல்பணி காலம் என்பது தேர்தல் அறிவிக்கை வெளியான நாள் முதல் தேர்தல் முடிவுகள் அறிவிக்கப்படும் நாள் வரை மட்டுமே நீடிக்கும், 5 ஆண்டுகள் அல்ல.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 misstates the duration.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 கால அளவை தவறாகக் கூறுகிறது.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="In Election Commission of India v. State of Tamil Nadu (1995), the Supreme Court upheld ECI's full disciplinary control over state officers on election duty.",
        tip_ta="1995 தமிழ்நாடு அரசு வழக்கில், தேர்தல் பணியில் உள்ள மாநில அதிகாரிகள் மீது ECI-க்கு முழு ஒழுங்கு நடவடிக்கை அதிகாரம் உண்டு என உச்ச நீதிமன்றம் உறுதி செய்தது.",
        fact_en="Section 13CC of RPA 1950 creates an identical deemed deputation for Electoral Registration Officers (EROs).",
        fact_ta="வாக்காளர் பதிவு அதிகாரிகளுக்கும் RPA 1950 பிரிவு 13CC-ன் கீழ் இதேபோன்ற அயல்பணி அந்தஸ்து உள்ளது.",
        tags=["Section 28A", "Deemed Deputation", "Disciplinary Authority", "Notification to Results"]
    ))

    # ER_S_045
    qs.append(make_er_q(
        qid="ER_S_045", diff="Hard", qtype="Multi-Statement", subtopic="Section 33A Criminal Antecedents Disclosure",
        en_stem="Consider the following statements regarding Section 33A of RPA 1951:\n1. It mandates candidate disclosure of pending cases where charges have been framed for offences punishable with imprisonment for 2 or more years.\n2. It mandates candidate disclosure of convictions for any offence where the candidate was sentenced to imprisonment for 1 year or more.\n3. The information must be delivered by the candidate in writing along with their nomination paper.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 33A குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 2 அல்லது அதற்கு மேற்பட்ட ஆண்டுகள் சிறைத் தண்டனைக்குரிய குற்றங்களில் குற்றச்சாட்டுகள் பதிவு செய்யப்பட்ட நிலுவை வழக்குகளை வேட்பாளர் வெளிப்படுத்துவதை இது கட்டாயமாக்குகிறது.\n2. 1 ஆண்டு அல்லது அதற்கு மேற்பட்ட சிறைத் தண்டனை விதிக்கப்பட்ட குற்றத்தீர்ப்புகளை வேட்பாளர் வெளிப்படுத்துவதை இது கட்டாயமாக்குகிறது.\n3. இவ்விவரங்களை வேட்பாளர் தனது வேட்புமனுவுடன் எழுத்துப்பூர்வமாக தாக்கல் செய்ய வேண்டும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Section 33A(1)(i) covers framed charges carrying 2+ years prison; Section 33A(1)(ii) covers convictions carrying 1+ year prison; and Section 33A(2) requires this information to be submitted in an affidavit along with the nomination paper.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பிரிவு 33A(1)(i) 2 ஆண்டு தண்டனைக்குரிய நிலுவை குற்றச்சாட்டுகளையும்; பிரிவு 33A(1)(ii) 1 ஆண்டுக்கு மேல் தண்டனை பெற்ற வழக்குகளையும் குறிக்கிறது; பிரிவு 33A(2) வேட்புமனுவுடன் உறுதிமொழிப் பத்திரமாக தாக்கல் செய்ய கட்டாயமாக்குகிறது.",
        why_a_en="Correct. All three statements accurately state Section 33A provisions.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் பிரிவு 33A-ன் சட்ட விதிகளை துல்லியமாகக் கூறுகின்றன.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="Section 33B attempted to restrict disclosures to Section 33A only, which the Supreme Court struck down in PUCL (2003) as violative of Article 19(1)(a).",
        tip_ta="வெளிப்பாடுகளை கட்டுப்படுத்த கொண்டுவரப்பட்ட பிரிவு 33B-ஐ 2003 PUCL வழக்கில் உச்ச நீதிமன்றம் ரத்து செய்தது.",
        fact_en="Section 33A was inserted by the Representation of the People (Third Amendment) Act, 2002.",
        fact_ta="2002-ன் மூன்றாவது திருத்தச் சட்டம் மூலம் பிரிவு 33A இணைக்கப்பட்டது.",
        tags=["Section 33A", "Candidate Disclosures", "Framed Charges", "Convictions"]
    ))

    # ER_S_046
    qs.append(make_er_q(
        qid="ER_S_046", diff="Medium", qtype="Multi-Statement", subtopic="Section 78 Lodging Accounts",
        en_stem="Consider the following statements regarding the lodging of election expenses under Section 78 of RPA 1951:\n1. Every contesting candidate must lodge their account of election expenses within 30 days from the declaration of results.\n2. The account must be lodged with the District Election Officer (DEO).\n3. Only the candidate who won the election is required to lodge the account of expenses.\nWhich of the statements given above is/are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 78-ன் கீழ் தேர்தல் செலவுக் கணக்கு தாக்கல் செய்வது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. போட்டியிட்ட ஒவ்வொரு வேட்பாளரும் தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட 30 நாட்களுக்குள் தங்களது செலவுக் கணக்கை தாக்கல் செய்ய வேண்டும்.\n2. இக்கணக்கு மாவட்ட தேர்தல் அதிகாரியிடம் (DEO) சமர்ப்பிக்கப்பட வேண்டும்.\n3. தேர்தலில் வெற்றி பெற்ற வேட்பாளர் மட்டுமே தனது செலவுக் கணக்கை தாக்கல் செய்ய வேண்டும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 78 explicitly mandates that EVERY contesting candidate (winners, runners-up, and those who lost deposits) must lodge their account of election expenses.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 78 வெற்றி பெற்றவர், தோற்றவர், வைப்புத்தொகை இழந்தவர் என தேர்தலில் போட்டியிட்ட 'ஒவ்வொரு வேட்பாளரும்' செலவுக் கணக்கு தாக்கல் செய்வதை கட்டாயமாக்குகிறது.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is false as ALL candidates must file.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; போட்டியிட்ட அனைத்து வேட்பாளர்களும் தாக்கல் செய்ய வேண்டும் என்பதால் கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Failure to lodge expenses triggers 3-year disqualification under Section 10A.",
        tip_ta="கணக்கு தாக்கல் செய்ய தவறினால் பிரிவு 10A-ன் கீழ் 3 ஆண்டுகள் தகுதிநீக்கம் செய்யப்படுவர்.",
        fact_en="The DEO scrutinizes the accounts and forwards a report to the ECI within 7 days of receiving them.",
        fact_ta="DEO கணக்குகளை ஆய்வு செய்து 7 நாட்களுக்குள் ECI-க்கு அறிக்கை அனுப்புவார்.",
        tags=["Section 78", "Lodging Expenses", "Every Candidate", "30 Days"]
    ))

    # ER_S_047
    qs.append(make_er_q(
        qid="ER_S_047", diff="Hard", qtype="Multi-Statement", subtopic="Section 17CA Electoral Trusts",
        en_stem="Consider the following statements regarding Electoral Trusts under Section 17CA of the Income Tax Act, 1961:\n1. An Electoral Trust must distribute at least 95% of contributions received in a financial year to registered political parties.\n2. Electoral Trusts are prohibited from accepting contributions from foreign citizens or foreign companies.\n3. Electoral Trusts are granted complete statutory immunity from disclosing donor names to the Election Commission.\nWhich of the statements given above are correct?",
        ta_stem="வருமான வரிச் சட்டம் 1961 பிரிவு 17CA-ன் கீழான தேர்தல் அறக்கட்டளைகள் (Electoral Trusts) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒரு தேர்தல் அறக்கட்டளை ஒரு நிதியாண்டில் பெற்ற நன்கொடைகளில் குறைந்தது 95%-ஐ பதிவு செய்யப்பட்ட கட்சிகளுக்கு விநியோகிக்க வேண்டும்.\n2. வெளிநாட்டு குடிமக்கள் அல்லது வெளிநாட்டு நிறுவனங்களிடமிருந்து நன்கொடைகளைப் பெறுவது தேர்தல் அறக்கட்டளைகளுக்கு தடை செய்யப்பட்டுள்ளது.\n3. நன்கொடையாளர்களின் பெயர்களை தேர்தல் ஆணையத்திற்கு வெளிப்படுத்துவதிலிருந்து தேர்தல் அறக்கட்டளைகளுக்கு முழுமையான சட்ட விலக்கு உண்டு.\nமேற்கண்ட கூற்றுகளைக் கவனியுங்கள். சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because unlike the struck-down Electoral Bonds, Electoral Trusts are legally MANDATED to submit an annual report to the ECI disclosing all donor names, PAN details, and recipient parties.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் தேர்தல் பத்திரங்களைப் போலன்றி, தேர்தல் அறக்கட்டளைகள் நன்கொடையாளரின் பெயர், பான் எண் மற்றும் பெற்ற கட்சிகளின் விவரங்களை ECI-யிடம் வெளிப்படையாக சமர்ப்பிப்பது கட்டாயமாகும்.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is false as transparency is mandatory.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; வெளிப்படைத்தன்மை கட்டாயம் என்பதால் கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Electoral Trusts Scheme was notified in January 2013 by the UPA government.",
        tip_ta="2013 ஜனவரியில் தேர்தல் அறக்கட்டளைகள் திட்டம் மத்திய அரசால் அறிவிக்கப்பட்டது.",
        fact_en="Contributions to approved Electoral Trusts are eligible for 100% tax deduction under Section 80GGB (for companies) and Section 80GGC (for individuals).",
        fact_ta="பிரிவு 80GGB மற்றும் 80GGC-ன் கீழ் தேர்தல் அறக்கட்டளைக்கு அளிக்கும் நன்கொடைக்கு 100% வருமான வரி விலக்கு உண்டு.",
        tags=["Electoral Trusts", "Section 17CA", "95 Percent Rule", "Transparency"]
    ))

    # ER_S_048
    qs.append(make_er_q(
        qid="ER_S_048", diff="Medium", qtype="Multi-Statement", subtopic="Section 81 Election Petition Presentation",
        en_stem="Consider the following statements regarding the presentation of Election Petitions under Section 81 of RPA 1951:\n1. An election petition must be presented within 45 days from the date of declaration of the result.\n2. The petition must be accompanied by a security deposit of ₹2,000 for costs under Section 117.\n3. An election petition can be presented directly to the President of India during a parliamentary recess.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 81-ன் கீழ் தேர்தல் மனு தாக்கல் செய்வது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட நாளிலிருந்து 45 நாட்களுக்குள் தேர்தல் மனு தாக்கல் செய்யப்பட வேண்டும்.\n2. மனுவுடன் பிரிவு 117-ன் கீழ் வழக்குச் செலவுகளுக்கான பாதுகாப்பு வைப்புத்தொகையாக ₹2,000 செலுத்தப்பட வேண்டும்.\n3. நாடாளுமன்ற இடைவேளையின் போது தேர்தல் மனுவை நேரடியாக இந்திய குடியரசுத் தலைவரிடம் தாக்கல் செய்யலாம்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because an election petition questioning parliamentary or assembly elections can ONLY be presented to the HIGH COURT under Section 80A, never to the President.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் பிரிவு 80A-ன் கீழ் தேர்தல் மனு உயர் நீதிமன்றத்தில் மட்டுமே தாக்கல் செய்யப்பட முடியும், குடியரசுத் தலைவரிடம் அல்ல.",
        why_a_en="Correct. Statements 1 and 2 are true; statement 3 is legally baseless.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Failure to deposit the ₹2,000 security under Section 117 results in dismissal of the petition under Section 86(1).",
        tip_ta="பிரிவு 117-ன் கீழ் ₹2,000 வைப்புத்தொகை செலுத்தாவிட்டால் மனு தள்ளுபடி செய்யப்படும்.",
        fact_en="The 45-day limitation period under Section 81 is strictly non-extendable under the Limitation Act.",
        fact_ta="பிரிவு 81-ன் கீழான 45 நாள் காலக்கெடுவை காலவரம்புச் சட்டத்தின் கீழ் நீட்டிக்க முடியாது.",
        tags=["Election Petitions", "Section 81", "45 Days", "Section 117 Deposit"]
    ))

    # ER_S_049
    qs.append(make_er_q(
        qid="ER_S_049", diff="Hard", qtype="Multi-Statement", subtopic="Section 100 Grounds for Declaring Election Void",
        en_stem="Consider the following statements regarding the grounds on which the High Court can declare an election void under Section 100 of RPA 1951:\n1. Improper rejection of any nomination paper automatically voids the election without having to prove material effect on the result.\n2. Improper acceptance of any nomination voids the election only if it has materially affected the result of the election.\n3. Commission of any corrupt practice by the returned candidate or their election agent voids the election.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 100-ன் கீழ் உயர் நீதிமன்றம் ஒரு தேர்தலை செல்லாது என அறிவிப்பதற்கான காரணங்கள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வேட்புமனு தவறாக நிராகரிக்கப்பட்டால், தேர்தல் முடிவு பாதிக்கப்பட்டது என்பதை நிரூபிக்காமலேயே தேர்தல் தானாக ரத்தாகும்.\n2. வேட்புமனு தவறாக ஏற்றுக்கொள்ளப்பட்டால், அது தேர்தல் முடிவை கணிசமாக பாதித்திருந்தால் மட்டுமே தேர்தல் ரத்தாகும்.\n3. வெற்றி பெற்ற வேட்பாளரோ அல்லது அவரது தேர்தல் முகவரோ ஏதேனும் ஊழல் நடைமுறையைச் செய்திருந்தால் தேர்தல் ரத்தாகும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. Under Section 100(1)(c), improper rejection of nomination is fatal per se; under Section 100(1)(d)(i), improper acceptance requires proving material effect; and under Section 100(1)(b), a corrupt practice by candidate/agent voids the election automatically.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பிரிவு 100(1)(c)-ன் கீழ் மனு தவறாக நிராகரிக்கப்பட்டால் தேர்தல் தானாக ரத்தாகும்; பிரிவு 100(1)(d)(i)-ன் கீழ் மனு ஏற்கப்பட்டால் முடிவு பாதிக்கப்பட்டது நிரூபிக்கப்பட வேண்டும்; பிரிவு 100(1)(b)-ன் கீழ் ஊழல் நடைமுறை தேர்தலை ரத்து செய்யும்.",
        why_a_en="Correct. All three statements accurately state Section 100 jurisprudence.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் பிரிவு 100-ன் சட்ட விதிகளை துல்லியமாகக் கூறுகின்றன.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="Remember the difference: Improper REJECTION = Automatically void; Improper ACCEPTANCE = Must prove material effect on result.",
        tip_ta="வேறுபாட்டை நினைவில் கொள்க: தவறான நிராகரிப்பு = தானாக ரத்தாகும்; தவறான ஏற்பு = முடிவு பாதிக்கப்பட்டது நிரூபிக்கப்பட வேண்டும்.",
        fact_en="Section 100 was famously applied in Raj Narain v. Indira Nehru Gandhi (1975).",
        fact_ta="1975 இந்திரா காந்தி வழக்கில் இப்பிரிவு 100-ன் கீழேயே தேர்தல் ரத்து செய்யப்பட்டது.",
        tags=["Section 100", "Election Void Grounds", "Improper Rejection vs Acceptance"]
    ))

    # ER_S_050
    qs.append(make_er_q(
        qid="ER_S_050", diff="Hard", qtype="Multi-Statement", subtopic="Section 61A and EVM Legal Status",
        en_stem="Consider the following statements regarding Section 61A of RPA 1951:\n1. It was inserted in 1989 following the Supreme Court's ruling in A.C. Jose v. Sivan Pillai (1984).\n2. It empowers the Election Commission to specify constituencies where voting machines shall be used instead of ballot papers.\n3. The constitutional validity of Section 61A and EVM voting was upheld by the Supreme Court in the landmark AIADMK v. Chief Election Commissioner (2001) case.\nWhich of the statements given above are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 61A குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஏ.சி. ஜோஸ் எதிர் சிவன் பிள்ளை (1984) உச்ச நீதிமன்ற தீர்ப்பைத் தொடர்ந்து 1989-ல் இது சட்டத்தில் சேர்க்கப்பட்டது.\n2. வாக்குச்சீட்டுகளுக்குப் பதிலாக வாக்குப்பதிவு இயந்திரங்கள் பயன்படுத்தப்பட வேண்டிய தொகுதிகளைக் குறிப்பிட இது தேர்தல் ஆணையத்திற்கு அதிகாரம் அளிக்கிறது.\n3. பிரிவு 61A மற்றும் EVM வாக்குப்பதிவின் அரசியலமைப்பு செல்லுபடியை AIADMK எதிர் தலைமைத் தேர்தல் ஆணையர் (2001) வழக்கில் உச்ச நீதிமன்றம் உறுதி செய்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1, 2 and 3", ta_a="1, 2 மற்றும் 3",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1 and 3 only", ta_d="1 மற்றும் 3 மட்டுமே",
        correct_key="A",
        exp_en="All three statements are correct. In A.C. Jose (1984), the Supreme Court struck down EVM use in Paravur for lack of statutory law; Parliament remedied this by inserting Section 61A with effect from 15 March 1989; and the Madras High Court and Supreme Court (2001) fully upheld Section 61A and EVMs.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. 1984 ஏ.சி. ஜோஸ் தீர்ப்பைத் தொடர்ந்து சட்டப்பூர்வ அதிகாரம் அளிக்க 1989-ல் பிரிவு 61A சேர்க்கப்பட்டது; இது ECI-க்கு EVM தொகுதிகளைக் குறிப்பிட அதிகாரம் அளிக்கிறது; 2001-ல் உச்ச நீதிமன்றம் இதன் செல்லுபடியை உறுதி செய்தது.",
        why_a_en="Correct. All three statements accurately describe the statutory evolution of EVMs in India.",
        why_a_ta="சரியானது. மூன்று கூற்றுகளும் இந்தியாவில் EVM-ன் சட்டப்பூர்வ பரிணாமத்தை சரியாகக் கூறுகின்றன.",
        why_b_en="Incorrect. Statement 3 is also correct.",
        why_b_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_c_en="Incorrect. Statement 1 is also correct.",
        why_c_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_d_en="Incorrect. Statement 2 is also correct.",
        why_d_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        tip_en="Section 61A gives ECI discretionary power to deploy EVMs in selected constituencies or nationwide.",
        tip_ta="பிரிவு 61A குறிப்பிட்ட தொகுதிகளிலோ அல்லது நாடு முழுவதுமோ EVM-ஐப் பயன்படுத்த ECI-க்கு அதிகாரம் அளிக்கிறது.",
        fact_en="Section 61A forms the legal foundation on which the world's largest electronic voting system operates today.",
        fact_ta="உலகின் மிகப்பெரிய மின்னணு வாக்குப்பதிவு முறை இயங்குவதற்கான சட்ட அடித்தளமாக பிரிவு 61A திகழ்கிறது.",
        tags=["Section 61A", "EVM Legal Backing", "AC Jose 1984", "AIADMK Case 2001"]
    ))

    return qs

def main():
    raw_qs = get_statement_questions()
    print(f"Total raw questions: {len(raw_qs)}")
    assert len(raw_qs) == 50, f"Expected 50, got {len(raw_qs)}"
    
    # Check ID sequence
    for idx, q in enumerate(raw_qs, 1):
        expected_id = f"ER_S_{idx:03d}"
        assert q["id"] == expected_id, f"ID mismatch at {idx}: {q['id']} != {expected_id}"
        
    # Check uniqueness of English stems
    stems = [q["question_en"].strip().lower() for q in raw_qs]
    assert len(set(stems)) == 50, f"Duplicate stems found: {len(set(stems))} unique out of 50"
    
    # Balance keys to roughly 13 A, 13 B, 12 C, 12 D
    balanced = balance_question_keys(raw_qs, target_counts={"A": 13, "B": 13, "C": 12, "D": 12})
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved to {OUTPUT_PATH}")
    
    # Also save to alias file
    with open(ALIAS_PATH, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved alias to {ALIAS_PATH}")
    
    # Validate with ContentValidator
    validator = ContentValidator()
    report = validator.validate_file(OUTPUT_PATH, expected_count=50, expected_prefix="ER_S_")
    print(report.summary())
    assert report.is_valid, "Validation failed!"

if __name__ == "__main__":
    main()
