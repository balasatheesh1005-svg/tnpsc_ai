# -*- coding: utf-8 -*-
"""
Builder for Electoral Reforms Hard 50 MCQs (ER_H_001 to ER_H_050).
Strictly adheres to the 24-field TNPSC Nova AI schema.
"""

import json
import os
from er_mcq_helper import make_er_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

OUTPUT_PATH = os.path.join("data", "questions", "polity", "electoral_reforms_hard.json")

def get_hard_questions():
    qs = []

    # ER_H_001
    qs.append(make_er_q(
        qid="ER_H_001", diff="Hard", qtype="Single-Choice", subtopic="NOTA in Rajya Sabha",
        en_stem="In which case did the Supreme Court hold that the 'None of the Above' (NOTA) option cannot be applied to elections to the Council of States (Rajya Sabha)?",
        ta_stem="மாநிலங்களவைத் (Rajya Sabha) தேர்தல்களுக்கு 'மேற்கண்ட எவருமில்லை' (NOTA) வாய்ப்பைப் பயன்படுத்த முடியாது என்று உச்ச நீதிமன்றம் எந்த வழக்கில் தீர்ப்பளித்தது?",
        en_a="Shailesh Manubhai Parmar v. Election Commission of India (2018)", ta_a="சைலேஷ் மனுபாய் பார்மர் எதிர் இந்திய தேர்தல் ஆணையம் (2018)",
        en_b="Kuldip Nayar v. Union of India (2006)", ta_b="குல்தீப் நய்யார் எதிர் இந்திய ஒன்றியம் (2006)",
        en_c="PUCL v. Union of India (2013)", ta_c="PUCL எதிர் இந்திய ஒன்றியம் (2013)",
        en_d="Lily Thomas v. Union of India (2013)", ta_d="லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (2013)",
        correct_key="A",
        exp_en="In Shailesh Manubhai Parmar v. ECI (2018), a 3-judge bench headed by CJI Dipak Misra held that NOTA was conceived for direct elections by individual voters exercising universal adult suffrage, and cannot be introduced into Rajya Sabha elections which are conducted under proportional representation by single transferable vote via an open ballot system under the 10th Schedule.",
        exp_ta="சைலேஷ் மனுபாய் பார்மர் (2018) வழக்கில், நேரடி பொதுத்தேர்தல்களுக்காக மட்டுமே NOTA உருவாக்கப்பட்டது என்றும், ஒற்றை மாற்று வாக்கு விகிதாச்சார பிரதிநிதித்துவம் மற்றும் திறந்த வாக்குச்சீட்டு முறையில் நடைபெறும் மாநிலங்களவைத் தேர்தல்களுக்கு NOTA பொருந்தாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        why_a_en="Correct. Shailesh Manubhai Parmar (2018) invalidated NOTA for Rajya Sabha elections.",
        why_a_ta="சரியானது. சைலேஷ் மனுபாய் பார்மர் வழக்கு மாநிலங்களவைத் தேர்தலில் NOTA செல்லாது என அறிவித்தது.",
        why_b_en="Incorrect. Kuldip Nayar (2006) upheld the open ballot system and removal of domicile requirement for Rajya Sabha.",
        why_b_ta="தவறானது. குல்தீப் நய்யார் வழக்கு மாநிலங்களவைத் தேர்தலில் திறந்த வாக்குச்சீட்டு முறையை உறுதி செய்தது.",
        why_c_en="Incorrect. PUCL (2013) introduced NOTA for direct Lok Sabha and Assembly elections.",
        why_c_ta="தவறானது. PUCL வழக்கு நேரடித் தேர்தல்களுக்கு NOTA-வை அறிமுகப்படுத்தியது.",
        why_d_en="Incorrect. Lily Thomas (2013) dealt with disqualification of convicted legislators.",
        why_d_ta="தவறானது. லில்லி தாமஸ் தண்டனை பெற்ற மக்கள் பிரதிநிதிகள் தகுதிநீக்கம் பற்றியது.",
        tip_en="Open ballot in Rajya Sabha ensures party discipline and curbs cross-voting; NOTA would encourage defiance of the party whip without anti-defection consequences.",
        tip_ta="மாநிலங்களவைத் தேர்தலில் திறந்த வாக்குச்சீட்டு முறை கட்சி தாவலைத் தடுக்கிறது; அங்கு NOTA-வை அனுமதித்தால் அது கட்சி கொறடாவை மீற வழிவகுக்கும்.",
        fact_en="ECI had issued circulars in 2014 and 2015 introducing NOTA in Rajya Sabha, which the Supreme Court quashed in this verdict.",
        fact_ta="2014 மற்றும் 2015-ல் மாநிலங்களவைத் தேர்தலில் NOTA-வை அறிமுகப்படுத்தி ECI வெளியிட்ட சுற்றறிக்கைகளை உச்ச நீதிமன்றம் ரத்து செய்தது.",
        tags=["NOTA", "Rajya Sabha", "Shailesh Parmar 2018", "Open Ballot"]
    ))

    # ER_H_002
    qs.append(make_er_q(
        qid="ER_H_002", diff="Hard", qtype="Single-Choice", subtopic="Rajya Sabha Open Ballot",
        en_stem="In Kuldip Nayar v. Union of India (2006), on what constitutional ground did the 5-judge Constitution Bench uphold the introduction of the 'Open Ballot' system in Rajya Sabha elections?",
        ta_stem="குல்தீப் நய்யார் எதிர் இந்திய ஒன்றியம் (2006) வழக்கில், மாநிலங்களவைத் தேர்தல்களில் 'திறந்த வாக்குச்சீட்டு' (Open Ballot) முறையை அறிமுகப்படுத்தியதை 5 நீதிபதிகள் அரசியல் சாசன அமர்வு எந்த அரசியலமைப்பு அடிப்படையில் உறுதி செய்தது?",
        en_a="Secrecy of the ballot is not an absolute fundamental principle, and open ballot effectively combats corruption, cross-voting, and horse-trading", ta_a="வாக்களிப்பின் ரகசியத்தன்மை என்பது முழுமையான தத்துவமல்ல; திறந்த வாக்குச்சீட்டு முறை ஊழல், குதிரை பேரம் மற்றும் கட்சித் துரோகத்தை திறம்படத் தடுக்கிறது",
        en_b="The Constitution explicitly requires all parliamentary elections to be non-secret in nature", ta_b="அனைத்து நாடாளுமன்றத் தேர்தல்களும் ரகசியமற்ற முறையில் நடத்தப்பட வேண்டும் என அரசியலமைப்பு தெளிவாகக் கூறியுள்ளது",
        en_c="Political parties have a fundamental right under Article 21 to inspect every vote cast by their members", ta_c="உறுப்பினர்கள் செலுத்தும் வாக்குகளை ஆய்வு செய்ய அரசியல் கட்சிகளுக்கு சரத்து 21-ன் கீழ் அடிப்படை உரிமை உண்டு",
        en_d="State Legislative Assemblies do not form part of the constitutional structure of India", ta_d="மாநில சட்டமன்றங்கள் இந்திய அரசியலமைப்பு கட்டமைப்பின் பகுதியாக இல்லை என்பதால்",
        correct_key="A",
        exp_en="In Kuldip Nayar v. UOI (2006), CJI Y.K. Sabharwal writing for a unanimous Constitution Bench held that the secrecy of the ballot is a statutory privilege, not an absolute constitutional mandate. The Parliament was well within its legislative competence to amend RPA 1951 in 2003 to introduce an open ballot in Rajya Sabha to ensure transparency and eradicate horse-trading.",
        exp_ta="குல்தீப் நய்யார் வழக்கில் (2006), ரகசிய வாக்கெடுப்பு என்பது சட்டப்பூர்வ விதியே தவிர முழுமையான அரசியலமைப்பு உரிமை அல்ல என்றும், குதிரை பேரம் மற்றும் ஊழலைத் தடுக்க நாடாளுமன்றம் 2003-ல் மக்கள் பிரதிநிதித்துவச் சட்டத்தைத் திருத்தி திறந்த வாக்குச்சீட்டை கொண்டுவந்தது செல்லும் என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        why_a_en="Correct. Secrecy is a statutory privilege, and open ballot combats corrupt horse-trading.",
        why_a_ta="சரியானது. ரகசிய வாக்கு சட்டப்பூர்வ சலுகையே தவிர முழுமையானது அல்ல; திறந்த வாக்கு குதிரை பேரத்தைத் தடுக்கிறது.",
        why_b_en="Incorrect. The Constitution does not require non-secret voting generally.",
        why_b_ta="தவறானது. அரசியலமைப்பு அத்தகைய பொது விதியைக் கொண்டிருக்கவில்லை.",
        why_c_en="Incorrect. Article 21 is right to life and personal liberty, not party inspection.",
        why_c_ta="தவறானது. சரத்து 21 தனிநபர் வாழ்வுரிமை பற்றியது.",
        why_d_en="Incorrect. State legislatures are foundational constitutional bodies under Part VI.",
        why_d_ta="தவறானது. சட்டமன்றங்கள் பகுதி VI-ன் கீழான அரசியலமைப்பு அமைப்புகள்.",
        tip_en="The same judgment also upheld deleting the requirement that a candidate for Rajya Sabha must be an elector in that particular state.",
        tip_ta="அதே தீர்ப்பில், மாநிலங்களவை வேட்பாளர் அந்த மாநில வாக்காளராக இருக்க வேண்டும் என்ற நிபந்தனையை நீக்கிய சட்டத்திருத்தத்தையும் உச்ச நீதிமன்றம் உறுதி செய்தது.",
        fact_en="An elector in Rajya Sabha must show their marked ballot to the authorized polling agent of their political party before inserting it into the ballot box.",
        fact_ta="மாநிலங்களவை தேர்தலில் வாக்களிக்கும் எம்.எல்.ஏ தனது கட்சியின் அங்கீகரிக்கப்பட்ட முகவரிடம் வாக்கை காட்டிய பிறகே பெட்டியில் போட வேண்டும்.",
        tags=["Kuldip Nayar 2006", "Open Ballot", "Rajya Sabha Reform", "Anti-Corruption"]
    ))

    # ER_H_003
    qs.append(make_er_q(
        qid="ER_H_003", diff="Hard", qtype="Single-Choice", subtopic="Removal of Disqualification Powers",
        en_stem="Under Section 11 of the Representation of the People Act, 1951, what exclusive power is vested in the Election Commission regarding disqualifications (except those for corrupt practices)?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 11-ன் கீழ், தகுதிநீக்கங்கள் தொடர்பாக (ஊழல் நடைமுறைகள் தவிர்த்து) தேர்தல் ஆணையத்திற்கு வழங்கப்பட்டுள்ள தனித்துவமான அதிகாரம் எது?",
        en_a="Power to remove or reduce the period of any disqualification for reasons recorded in writing", ta_a="காரணங்களை எழுத்துப்பூர்வமாக பதிவு செய்து, எந்தவொரு தகுதிநீக்கத்தையும் நீக்க அல்லது அதன் கால அளவைக் குறைக்க அதிகாரம்",
        en_b="Power to enhance the disqualification period up to a lifetime ban without judicial review", ta_b="நீதிமன்ற மறுஆய்வின்றி தகுதிநீக்கக் காலத்தை வாழ்நாள் தடையாக அதிகரிக்க அதிகாரம்",
        en_c="Power to pardon criminal convicts and commute their prison sentences", ta_c="குற்றவாளிகளுக்கு மன்னிப்பு வழங்கி அவர்களது சிறைத்தண்டனையை குறைக்கும் அதிகாரம்",
        en_d="Power to dissolve any legislative assembly where disqualified members are sitting", ta_d="தகுதிநீக்கம் செய்யப்பட்ட உறுப்பினர்கள் உள்ள சட்டமன்றத்தை கலைக்கும் அதிகாரம்",
        correct_key="A",
        exp_en="Section 11 of RPA 1951 empowers the Election Commission of India, for reasons to be recorded by it, to remove any disqualification (except disqualification under Section 8A for corrupt practices) or reduce the period of any such disqualification.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 11, எழுத்துப்பூர்வமாக காரணங்களைப் பதிவு செய்து, பிரிவு 8A-ன் கீழான ஊழல் நடைமுறை தகுதிநீக்கம் தவிர்த்த பிற தகுதிநீக்கங்களை நீக்கவோ அல்லது அதன் காலத்தைக் குறைக்கவோ தேர்தல் ஆணையத்திற்கு அதிகாரம் அளிக்கிறது.",
        why_a_en="Correct. ECI can remove or reduce the period of disqualification under Section 11.",
        why_a_ta="சரியானது. பிரிவு 11-ன் கீழ் ECI தகுதிநீக்கத்தை நீக்கவோ குறைக்கவோ முடியும்.",
        why_b_en="Incorrect. ECI cannot unilaterally enhance penalties.",
        why_b_ta="தவறானது. தகுதிநீக்கக் காலத்தை உயர்த்த முடியாது.",
        why_c_en="Incorrect. Pardon and commutation belong exclusively to the President (Art 72) and Governor (Art 161).",
        why_c_ta="தவறானது. மன்னிப்பளிக்கும் அதிகாரம் குடியரசுத் தலைவர் மற்றும் ஆளுநருக்கே உண்டு.",
        why_d_en="Incorrect. ECI cannot dissolve legislatures.",
        why_d_ta="தவறானது. சட்டமன்றத்தை கலைக்க அதிகாரம் இல்லை.",
        tip_en="In September 2019, ECI exercised Section 11 to reduce the disqualification period of Sikkim Chief Minister Prem Singh Tamang (Golay) from 6 years to 1 year and 1 month, enabling him to contest by-elections.",
        tip_ta="2019-ல் சிக்கிம் முதல்வர் பிரேம் சிங் தமாங்கின் தகுதிநீக்கக் காலத்தை 6 ஆண்டிலிருந்து 1 ஆண்டாக குறைக்க ECI இப்பிரிவு 11-ஐப் பயன்படுத்தியது.",
        fact_en="Disqualifications for corrupt practices under Section 8A are governed separately under Section 8A(3) by the President acting on ECI's opinion.",
        fact_ta="பிரிவு 8A-ன் கீழான ஊழல் நடைமுறை தகுதிநீக்கங்களை குறைக்க குடியரசுத் தலைவரே ECI ஆலோசனையின் பேரில் முடிவு செய்வார்.",
        tags=["Section 11", "ECI Power to Reduce Disqualification", "Prem Singh Tamang"]
    ))

    # ER_H_004
    qs.append(make_er_q(
        qid="ER_H_004", diff="Hard", qtype="Single-Choice", subtopic="Corrupt Practice Disqualification Procedure",
        en_stem="Under Section 8A of the Representation of the People Act, 1951, who determines whether a person found guilty of a corrupt practice by the High Court shall be disqualified and for what period?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 8A-ன் கீழ், உயர் நீதிமன்றத்தால் ஊழல் நடைமுறையில் குற்றவாளி எனத் தீர்ப்பளிக்கப்பட்ட ஒரு நபர் தகுதிநீக்கம் செய்யப்பட வேண்டுமா மற்றும் எத்தனை ஆண்டுகளுக்கு என்பதை தீர்மானிப்பவர் யார்?",
        en_a="The President of India, acting according to the binding opinion of the Election Commission (for a period up to 6 years)", ta_a="தேர்தல் ஆணையத்தின் கட்டுப்படுத்தும் கருத்தின்படி செயல்படும் இந்திய குடியரசுத் தலைவர் (6 ஆண்டுகள் வரையிலான காலத்திற்கு)",
        en_b="The Chief Justice of India acting in his administrative discretion", ta_b="தனது சொந்த நிர்வாக விருப்புரிமையின் கீழ் செயல்படும் இந்திய தலைமை நீதிபதி",
        en_c="The Speaker of the Lok Sabha upon a resolution passed by Parliament", ta_c="நாடாளுமன்ற தீர்மானத்தின் அடிப்படையில் மக்களவை சபாநாயகர்",
        en_d="The Governor of the State where the corrupt practice was committed", ta_d="ஊழல் நடைமுறை நடைபெற்ற மாநிலத்தின் ஆளுநர்",
        correct_key="A",
        exp_en="Under Section 8A of RPA 1951, whenever a case of corrupt practice is found by the High Court, the matter is submitted to the President. The President shall decide whether the person shall be disqualified and for what period (not exceeding 6 years), and before deciding, the President SHALL obtain the opinion of the Election Commission and act according to such opinion.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 8A-ன் படி, உயர் நீதிமன்றம் ஊழல் நடைமுறையை உறுதி செய்தால், அது குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்படும். குடியரசுத் தலைவர் ECI-ன் கருத்தைப் பெற்று அதன்படி செயல்பட்டு, அதிகபட்சம் 6 ஆண்டுகள் வரை தகுதிநீக்கம் குறித்து உத்தரவிடுவார்.",
        why_a_en="Correct. President acts according to the opinion of ECI under Section 8A.",
        why_a_ta="சரியானது. ECI-ன் கருத்தின்படி குடியரசுத் தலைவர் உத்தரவிடுவார்.",
        why_b_en="Incorrect. CJI does not determine administrative disqualification periods.",
        why_b_ta="தவறானது. தலைமை நீதிபதி தீர்மானிப்பதில்லை.",
        why_c_en="Incorrect. Speaker has no role under Section 8A.",
        why_c_ta="தவறானது. சபாநாயகருக்கு இதில் பங்கில்லை.",
        why_d_en="Incorrect. Governor does not decide Section 8A cases.",
        why_d_ta="தவறானது. ஆளுநர் முடிவெடுப்பதில்லை.",
        tip_en="Compare with Article 103: President decides disqualification of sitting MPs acting according to ECI opinion.",
        tip_ta="சரத்து 103-உடன் ஒப்பிடுக: எம்.பி.க்களின் தகுதிநீக்கத்தை ECI ஆலோசனையின்படி குடியரசுத் தலைவர் முடிவு செய்கிறார்.",
        fact_en="Section 8A was heavily amended in 1975 after Indira Gandhi's election case.",
        fact_ta="1975-ல் இந்திரா காந்தி தேர்தல் வழக்கிற்குப் பிறகு பிரிவு 8A பெருமளவில் திருத்தப்பட்டது.",
        tags=["Section 8A", "Corrupt Practices Disqualification", "President and ECI"]
    ))

    # ER_H_005
    qs.append(make_er_q(
        qid="ER_H_005", diff="Hard", qtype="Single-Choice", subtopic="Technical EVM Architecture",
        en_stem="Which technical safeguard embedded in Indian EVMs ensures that no external malicious software or virus can be introduced into the machine?",
        ta_stem="இந்திய EVM இயந்திரங்களில் எந்தவொரு வெளிப்புற தீங்கிழைக்கும் மென்பொருளோ அல்லது வைரஸோ நுழைக்கப்பட முடியாது என்பதை உறுதி செய்யும் தொழில்நுட்ப பாதுகாப்பு அம்சம் எது?",
        en_a="The micro-controller contains firmware burnt onto a One-Time Programmable (OTP) Masked ROM during chip manufacture that can never be rewritten", ta_a="நுண்கட்டுப்படுத்தியில் உள்ள ஃபார்ம்வேர் (Firmware) சில்லு தயாரிப்பின் போதே ஒருமுறை மட்டுமே எழுதக்கூடிய (OTP) Masked ROM-ல் பொறிக்கப்படுவதால் அதை ஒருபோதும் மாற்றியமைக்க முடியாது",
        en_b="The EVMs are connected via a dedicated quantum-encrypted satellite link to ECI servers", ta_b="EVM-கள் பிரத்யேக குவாண்டம் மறைகுறியீட்டு செயற்கைக்கோள் இணைப்பு மூலம் ECI சேவையகத்துடன் இணைக்கப்பட்டுள்ளன",
        en_c="The machines run on open-source Linux with weekly automatic internet updates", ta_c="இயந்திரங்கள் வாராந்திர தானியங்கி இணைய புதுப்பிப்புகளுடன் கூடிய லினக்ஸ் அமைப்பில் இயங்குகின்றன",
        en_d="The ballot unit uses Bluetooth Low Energy (BLE) paired exclusively with the Returning Officer's phone", ta_d="வாக்குப்பதிவு அலகு புளூடூத் மூலம் தேர்தல் நடத்தும் அலுவலரின் தொலைபேசியுடன் மட்டுமே இணைக்கப்பட்டுள்ளது",
        correct_key="A",
        exp_en="Indian EVMs use microcontrollers manufactured by NXP/Microchip where the machine code is permanently etched onto a One-Time Programmable (OTP) Masked ROM at the semiconductor fab. Once etched, the code can neither be modified, overwritten, nor read back. EVMs have zero wireless/wired networking capability.",
        exp_ta="இந்திய EVM இயந்திரங்கள் ஒருமுறை மட்டுமே எழுதக்கூடிய (OTP) Masked ROM சில்லுகளைப் பயன்படுத்துகின்றன. சிப் தயாரிக்கும் போதே நிரல்கள் பொறிக்கப்படுவதால், அதை மீண்டும் மாற்றி எழுதவோ, படிக்கவோ முடியாது. மேலும் இவ்வியந்திரங்களில் வைஃபை, புளூடூத் போன்ற எவ்வித தொலைத்தொடர்பு வசதிகளும் இல்லை.",
        why_a_en="Correct. OTP Masked ROM hardware ensures firmware cannot be rewritten or modified.",
        why_a_ta="சரியானது. OTP Masked ROM வன்பொருள் ஃபார்ம்வேரை மாற்றியமைக்க முடியாதவாறு பாதுகாக்கிறது.",
        why_b_en="Incorrect. EVMs are completely standalone and have zero satellite or network connectivity.",
        why_b_ta="தவறானது. EVM எந்தவொரு நெட்வொர்க் அல்லது செயற்கைக்கோளுடனும் இணைக்கப்படவில்லை.",
        why_c_en="Incorrect. EVMs do not run operating systems like Linux and have no internet connection.",
        why_c_ta="தவறானது. EVM-ல் லினக்ஸ் போன்ற இயங்குதளமோ இணைய இணைப்போ இல்லை.",
        why_d_en="Incorrect. EVMs contain NO Bluetooth, Wi-Fi, or radio-frequency components.",
        why_d_ta="தவறானது. EVM-ல் புளூடூத் அல்லது வயர்லெஸ் கருவிகள் எதுவும் இல்லை.",
        tip_en="EVMs are manufactured exclusively by two defense public sector undertakings: Bharat Electronics Limited (BEL) and Electronics Corporation of India Limited (ECIL).",
        tip_ta="EVM-கள் பாரத் எலக்ட்ரானிக்ஸ் (BEL) மற்றும் எலக்ட்ரானிக்ஸ் கார்ப்பரேஷன் ஆஃப் இந்தியா (ECIL) ஆகிய இரு பொதுத்துறை நிறுவனங்களால் மட்டுமே தயாரிக்கப்படுகின்றன.",
        fact_en="M3 generation EVMs also feature mutual authentication between the Control Unit, Ballot Unit, and VVPAT through encrypted handshake signals.",
        fact_ta="M3 தலைமுறை EVM-கள் கட்டுப்பாட்டு அலகு, வாக்குப்பதிவு அலகு மற்றும் VVPAT இடையே மறைகுறியாக்கப்பட்ட டிஜிட்டல் அங்கீகார சமிக்ஞைகளைப் பயன்படுத்துகின்றன.",
        tags=["EVM Architecture", "OTP Masked ROM", "BEL ECIL", "Cybersecurity"]
    ))

    # ER_H_006
    qs.append(make_er_q(
        qid="ER_H_006", diff="Hard", qtype="Single-Choice", subtopic="EVM M3 Generation Features",
        en_stem="What automated security mechanism is incorporated into the latest 'M3' generation EVMs introduced by ECI from 2013 onwards?",
        ta_stem="2013 முதல் ECI அறிமுகப்படுத்திய அதிநவீன 'M3' தலைமுறை EVM இயந்திரங்களில் இணைக்கப்பட்டுள்ள தானியங்கி பாதுகாப்பு அம்சம் எது?",
        en_a="Self-diagnostic digital certificate verification and automated permanent deactivation if any physical tampering is detected", ta_a="சுய-கண்டறிதல் டிஜிட்டல் சான்றிதழ் சரிபார்ப்பு மற்றும் இயந்திரத்தை திறக்கவோ முறைகேடு செய்யவோ முயன்றால் தானாகவே நிரந்தரமாக முடங்கும் வசதி",
        en_b="Facial recognition camera scanning each voter against Aadhaar database", ta_b="ஆதார் தரவுத்தளத்திற்கு எதிராக ஒவ்வொரு வாக்காளரையும் முகம் அடையாளம் காணும் கேமரா வசதி",
        en_c="Automatic remote erasing of all votes via cellular SMS command", ta_c="மொபைல் எஸ்எம்எஸ் கட்டளை மூலம் அனைத்து வாக்குகளையும் தொலைவிலிருந்து அழிக்கும் வசதி",
        en_d="Automated thermal printing of candidate bank account numbers", ta_d="வேட்பாளர்களின் வங்கிக் கணக்கு எண்களை தானாக அச்சிடும் வசதி",
        correct_key="A",
        exp_en="The M3 generation EVM incorporates advanced tamper-detection features: (1) Mutual authentication where each unit validates the digital certificate of connected units, (2) automated self-diagnostics at every boot-up, and (3) a physical tamper-detection circuit that renders the machine permanently inoperative if any unauthorized attempt is made to open the casing.",
        exp_ta="M3 தலைமுறை EVM இயந்திரங்கள் மேம்பட்ட முறைகேடு தடுப்பு அமைப்புகளைக் கொண்டுள்ளன: இணைக்கப்பட்ட கருவிகளை டிஜிட்டல் சான்றிதழ் மூலம் பரஸ்பரம் சரிபார்த்தல் மற்றும் இயந்திரத்தை அங்கீகாரமின்றி திறக்க முயன்றால் உடனடியாக இயந்திரம் தானாகவே நிரந்தரமாக முடங்கிவிடும் (Inoperative) பாதுகாப்பு சுற்றுகள் இதில் உள்ளன.",
        why_a_en="Correct. Automated tamper response circuit and mutual authentication.",
        why_a_ta="சரியானது. தானியங்கி முறைகேடு கண்டறிதல் மற்றும் பரஸ்பர டிஜிட்டல் அங்கீகாரம்.",
        why_b_en="Incorrect. EVMs have no cameras or Aadhaar facial biometric scanners.",
        why_b_ta="தவறானது. கேமரா அல்லது ஆதார் ஸ்கேனர் எதுவும் இல்லை.",
        why_c_en="Incorrect. Remote cellular connectivity is completely absent.",
        why_c_ta="தவறானது. செல்லுலார் வசதி கிடையாது.",
        why_d_en="Incorrect. Irrelevant option.",
        why_d_ta="தவறானது. பொருத்தமற்றது.",
        tip_en="M3 machines can support up to 24 Ballot Units connected together, accommodating up to 384 candidates (including NOTA).",
        tip_ta="M3 இயந்திரங்களில் 24 வாக்குப்பதிவு அலகுகளை இணைத்து அதிகபட்சமாக 384 வேட்பாளர்கள் (NOTA உட்பட) வரை போட்டியிட வைக்க முடியும்.",
        fact_en="M1 was manufactured until 2006, M2 between 2006 and 2012, and M3 from 2013 onwards.",
        fact_ta="M1 இயந்திரங்கள் 2006 வரையிலும், M2 இயந்திரங்கள் 2006-2012 வரையிலும், M3 இயந்திரங்கள் 2013 முதல் தயாரிக்கப்படுகின்றன.",
        tags=["M3 EVM", "Tamper Detection", "Mutual Authentication"]
    ))

    # ER_H_007
    qs.append(make_er_q(
        qid="ER_H_007", diff="Hard", qtype="Single-Choice", subtopic="Section 33(7) RPA 1951",
        en_stem="Why did the Law Commission of India in its 255th Report (2015) and the Election Commission recommend amending Section 33(7) of RPA 1951 to permit contesting from only ONE constituency?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 33(7)-ஐத் திருத்தி, ஒரு வேட்பாளர் ஒரே ஒரு தொகுதியில் மட்டுமே போட்டியிட அனுமதிக்க வேண்டும் என்று சட்ட ஆணையமும் (255-வது அறிக்கை) தேர்தல் ஆணையமும் பரிந்துரைத்தது ஏன்?",
        en_a="Because when a candidate wins from two seats, one seat must be vacated, causing an unnecessary, costly by-election imposing a financial burden on the public exchequer", ta_a="வேட்பாளர் இரு தொகுதிகளிலும் வெற்றி பெற்றால் ஒரு தொகுதியை ராஜினாமா செய்ய நேரிடுவதால், தேவையற்ற அரசுப் பண விரயத்துடன் கூடிய இடைத்தேர்தல் சுமை ஏற்படுவதைத் தவிர்க்க",
        en_b="Because contesting from two seats is an explicit violation of the Right to Equality under Article 14 as per Supreme Court rulings", ta_b="இரண்டு தொகுதிகளில் போட்டியிடுவது சரத்து 14-ன் கீழான சமத்துவ உரிமையை மீறுவதாகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்துள்ளதால்",
        en_c="Because EVMs do not have the technical memory capacity to print a candidate's name twice", ta_c="வேட்பாளரின் பெயரை இருமுறை பதிவு செய்யும் தொழில்நுட்ப நினைவக திறன் EVM-ல் இல்லை என்பதால்",
        en_d="Because political parties lose their registration automatically if their leader contests two seats", ta_d="தலைவர் இரு இடங்களில் போட்டியிட்டால் அரசியல் கட்சியின் பதிவு தானாக ரத்தாகிவிடும் என்பதால்",
        correct_key="A",
        exp_en="Under Section 70 of RPA 1951, if a candidate wins from both constituencies, they must resign from one seat within 10 days, triggering an inevitable by-election that wastes public administrative machinery and causes avoidable taxpayer expenditure. ECI and the Law Commission thus recommended 'one candidate, one constituency' or requiring candidates vacating a seat to reimburse the by-election cost (₹5 lakh for Assembly, ₹10 lakh for Lok Sabha).",
        exp_ta="பிரிவு 70-ன் படி, ஒருவர் இரு தொகுதிகளிலும் வெற்றி பெற்றால் 10 நாட்களுக்குள் ஒரு தொகுதியை ராஜினாமா செய்ய வேண்டும். இதனால் ஏற்படும் தவிர்க்கக்கூடிய இடைத்தேர்தல் அரசு கஜானாவிற்கு நிதி இழப்பையும் நிர்வாக சுமையையும் ஏற்படுத்துவதால், 'ஒரு வேட்பாளர், ஒரு தொகுதி' முறையைக் கொண்டுவர பரிந்துரைக்கப்பட்டது.",
        why_a_en="Correct. Prevents avoidable by-elections and wasteful public expenditure.",
        why_a_ta="சரியானது. தவிர்க்கக்கூடிய இடைத்தேர்தல்கள் மற்றும் மக்கள் வரிப்பண விரயத்தைத் தடுக்கிறது.",
        why_b_en="Incorrect. Supreme Court in Ashwini Upadhyay (2023) actually upheld the validity of Section 33(7), leaving amendment to Parliament.",
        why_b_ta="தவறானது. உச்ச நீதிமன்றம் பிரிவு 33(7)-ன் சட்ட செல்லுபடியை உறுதி செய்து, நாடாளுமன்றத்தின் பரிசீலனைக்கு விட்டது.",
        why_c_en="Incorrect. EVM memory has no such limitation.",
        why_c_ta="தவறானது. EVM நினைவகத்திற்கு தொடர்பில்லை.",
        why_d_en="Incorrect. Party registration is unaffected.",
        why_d_ta="தவறானது. கட்சி பதிவு பாதிக்கப்படாது.",
        tip_en="In Ashwini Kumar Upadhyay v. UOI (February 2023), the Supreme Court declined to strike down Section 33(7), holding it is a matter of legislative policy.",
        tip_ta="2023 அஸ்வினி உபாத்யாய் வழக்கில், பிரிவு 33(7)-ஐ ரத்து செய்ய மறுத்த உச்ச நீதிமன்றம், இது நாடாளுமன்ற கொள்கை முடிவு என்று கூறியது.",
        fact_en="Prior to 1996, there was no limit on the number of constituencies a person could contest; stalwarts like Atal Bihari Vajpayee and Devi Lal contested from 3+ seats.",
        fact_ta="1996-க்கு முன் எத்தனை தொகுதிகளிலும் போட்டியிட முடிந்தது; வாஜ்பாய், தேவிலால் போன்றோர் பல தொகுதிகளில் ஒரே நேரத்தில் போட்டியிட்டுள்ளனர்.",
        tags=["Section 33(7)", "One Candidate One Seat", "255th Law Commission", "By-election Cost"]
    ))

    # ER_H_008
    qs.append(make_er_q(
        qid="ER_H_008", diff="Hard", qtype="Single-Choice", subtopic="Lily Thomas Doctrine",
        en_stem="On what core constitutional doctrine did the Supreme Court base its judgment in Lily Thomas v. Union of India (2013) striking down Section 8(4) of the Representation of the People Act, 1951?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 8(4)-ஐ ரத்து செய்த லில்லி தாமஸ் (2013) தீர்ப்பில், உச்ச நீதிமன்றம் பயன்படுத்திய முக்கிய அரசியலமைப்பு கோட்பாடு எது?",
        en_a="Lack of legislative competence of Parliament to create a differential disqualification regime for sitting members versus candidates under Articles 102(1)(e) and 191(1)(e)", ta_a="சரத்து 102(1)(e) மற்றும் 191(1)(e)-ன் கீழ் புதிய வேட்பாளர்களுக்கும் பதவியில் உள்ள உறுப்பினர்களுக்கும் இடையே வேறுபட்ட தகுதிநீக்க விதிகளை உருவாக்க நாடாளுமன்றத்திற்கு சட்டமியற்றும் அதிகார வரம்பு இல்லை",
        en_b="Violation of the doctrine of separation of powers between the President and the Prime Minister", ta_b="குடியரசுத் தலைவர் மற்றும் பிரதமருக்கு இடையேயான அதிகாரப் பகிர்வு கோட்பாட்டை மீறியது",
        en_c="Violation of the right to property under Article 300A for loss of legislative salary", ta_c="சட்டமன்ற ஊதிய இழப்பிற்காக சரத்து 300A-ன் கீழான சொத்துரிமை மீறப்பட்டது",
        en_d="Violation of the international covenants on civil and political rights without treaty ratification", ta_d="சர்வதேச சிவில் மற்றும் அரசியல் உரிமைகள் உடன்படிக்கையை மீறியது",
        correct_key="A",
        exp_en="In Lily Thomas (2013), the Supreme Court ruled that Articles 102(1)(e) and 191(1)(e) empower Parliament to lay down disqualifications for 'being chosen as' AND 'for being' a member. The Constitution does not permit Parliament to create two different disqualification standards—disqualifying ordinary candidates immediately while shielding sitting MPs/MLAs under Section 8(4). Hence, Section 8(4) was ultra vires the Constitution.",
        exp_ta="லில்லி தாமஸ் வழக்கில், சரத்து 102(1)(e) மற்றும் 191(1)(e)-ன் படி ஒரு நபர் 'தேர்ந்தெடுக்கப்படுவதற்கும்' மற்றும் 'உறுப்பினராக நீடிப்பதற்கும்' ஒரே மாதிரியான தகுதிநீக்கங்களை மட்டுமே நாடாளுமன்றம் உருவாக்க முடியும் என்றும், பதவியில் உள்ள எம்.பி., எம்.எல்.ஏ-க்களுக்கு மட்டும் தகுதிநீக்கத்திலிருந்து விலக்கு அளிக்க நாடாளுமன்றத்திற்கு அதிகாரமில்லை என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        why_a_en="Correct. Parliament lacks competence to create unequal disqualification criteria under Articles 102 and 191.",
        why_a_ta="சரியானது. சரத்து 102 மற்றும் 191-ன் கீழ் வேறுபட்ட தகுதிநீக்க விதிகளை உருவாக்க நாடாளுமன்றத்திற்கு அதிகார வரம்பு இல்லை.",
        why_b_en="Incorrect. Separation of powers was not the ratio.",
        why_b_ta="தவறானது. அதிகாரப் பகிர்வு தீர்ப்பின் அடிப்படை அல்ல.",
        why_c_en="Incorrect. Right to property was completely irrelevant.",
        why_c_ta="தவறானது. சொத்துரிமைக்கு தொடர்பில்லை.",
        why_d_en="Incorrect. International treaties were not the ground.",
        why_d_ta="தவறானது. சர்வதேச ஒப்பந்தங்கள் காரணம் அல்ல.",
        tip_en="Section 8(4) gave convicted legislators a 3-month protection window to file an appeal and stay their disqualification.",
        tip_ta="பிரிவு 8(4) தண்டனை பெற்ற உறுப்பினர்கள் மேல்முறையீடு செய்ய 3 மாத கால அவகாசம் வழங்கி தகுதிநீக்கத்தைத் தள்ளிப்போட்டது.",
        fact_en="Following Lily Thomas, an ordinance attempted by the UPA government in 2013 to overturn the verdict was famously torn up and subsequently withdrawn.",
        fact_ta="லில்லி தாமஸ் தீர்ப்பை மாற்றியமைக்க 2013-ல் கொண்டுவரப்பட்ட அவசரச் சட்டம் கடும் எதிர்ப்பால் திரும்பப் பெறப்பட்டது.",
        tags=["Lily Thomas 2013", "Section 8(4)", "Article 102", "Legislative Competence"]
    ))

    # ER_H_009
    qs.append(make_er_q(
        qid="ER_H_009", diff="Hard", qtype="Single-Choice", subtopic="Disqualification Reversal on Stay",
        en_stem="In Lok Prahari v. Election Commission of India (2018), what did the Supreme Court clarify regarding the effect of an appellate court staying a conviction of a disqualified legislator?",
        ta_stem="லோக் பிரஹாரி எதிர் இந்திய தேர்தல் ஆணையம் (2018) வழக்கில், தகுதிநீக்கம் செய்யப்பட்ட ஒரு சட்டமன்ற உறுப்பினரின் குற்றத்தண்டனைக்கு மேல்முறையீட்டு நீதிமன்றம் தடை விதித்தால் (Stay of conviction) ஏற்படும் விளைவு குறித்து உச்ச நீதிமன்றம் என்ன தெளிவுபடுத்தியது?",
        en_a="A stay of conviction wipes out the disqualification under Section 8 of RPA 1951 from the date of the stay order, restoring their legislative status", ta_a="குற்றத்தண்டனைக்கு இடைக்கால தடை விதிக்கப்பட்டால், தடை ஆணை வெளியான தேதியிலிருந்து பிரிவு 8-ன் கீழான தகுதிநீக்கம் நீக்கப்பட்டு அவரது பதவி மீண்டும் மீட்டெடுக்கப்படும்",
        en_b="A stay of conviction has no legal effect; only a full acquittal can ever restore membership", ta_b="தண்டனைக்கு தடை விதிப்பது எவ்வித பலனையும் தராது; முழுமையான விடுதலை மட்டுமே பதவியை மீட்க முடியும்",
        en_c="The disqualified member must immediately face a fresh general election in their constituency", ta_c="தகுதிநீக்கம் செய்யப்பட்ட உறுப்பினர் உடனடியாக அத்தொகுதியில் புதிய பொதுத்தேர்தலை சந்திக்க வேண்டும்",
        en_d="The stay of conviction can only be granted by the President of India under Article 72", ta_d="சரத்து 72-ன் கீழ் குடியரசுத் தலைவரால் மட்டுமே தண்டனைக்கு தடை விதிக்க முடியும்",
        correct_key="A",
        exp_en="In Lok Prahari v. ECI (2018), a 3-judge bench led by CJI Dipak Misra clarified that once a stay of conviction (not merely suspension of sentence/bail) is granted by an appellate court under Section 389(1) of CrPC, the disqualification under Section 8 of RPA 1951 ceases to operate from that date, restoring membership.",
        exp_ta="லோக் பிரஹாரி (2018) வழக்கில், மேல்முறையீட்டு நீதிமன்றம் குற்றவியல் நடைமுறைச் சட்டம் பிரிவு 389(1)-ன் கீழ் குற்றத் தீர்ப்பிற்கு (Stay of conviction) இடைக்காலத் தடை விதித்தால், தடை விதிக்கப்பட்ட நாளிலிருந்து பிரிவு 8-ன் கீழான தகுதிநீக்கம் செயல்படாது என்றும், அவரது பதவி மீண்டும் தொடரும் என்றும் உச்ச நீதிமன்றம் தெளிவுபடுத்தியது.",
        why_a_en="Correct. Stay of conviction removes the disqualification under Section 8.",
        why_a_ta="சரியானது. தண்டனைக்கு இடைக்காலத் தடை விதிக்கப்பட்டால் தகுதிநீக்கம் நீங்கும்.",
        why_b_en="Incorrect. Suspension/stay of conviction is legally sufficient under Ravikant Patil and Lok Prahari.",
        why_b_ta="தவறானது. ரவிகாந்த் பாட்டீல் மற்றும் லோக் பிரஹாரி தீர்ப்புகளின்படி தண்டனைக்குத் தடையே போதுமானது.",
        why_c_en="Incorrect. By-elections are stayed if conviction is stayed.",
        why_c_ta="தவறானது. மறுதேர்தல் நடத்தப்படாது.",
        why_d_en="Incorrect. Appellate courts grant stays under Section 389 CrPC.",
        why_d_ta="தவறானது. நீதிமன்றங்களே தடையாணை பிறப்பிக்கின்றன.",
        tip_en="Critical legal distinction: Suspension of SENTENCE (getting bail) does NOT remove disqualification; only a stay of CONVICTION removes disqualification.",
        tip_ta="முக்கிய சட்ட வேறுபாடு: தண்டனை நிறுத்திவைப்பு (ஜாமீன் பெறுவது) தகுதிநீக்கத்தை நீக்காது; குற்றத்தீர்ப்பிற்கே தடை (Stay of conviction) பெற்றால் மட்டுமே தகுதிநீக்கம் நீங்கும்.",
        fact_en="This principle was applied in Rahul Gandhi v. Purnesh Modi (2023), where the Supreme Court stayed the conviction, leading to the immediate restoration of his Lok Sabha membership.",
        fact_ta="2023 ராகுல் காந்தி வழக்கில் உச்ச நீதிமன்றம் குற்றத்தீர்ப்பிற்கு தடை விதித்ததைத் தொடர்ந்து அவரது மக்களவை உறுப்பினர் பதவி மீண்டும் மீட்டெடுக்கப்பட்டது.",
        tags=["Lok Prahari 2018", "Stay of Conviction", "Section 8 RPA", "Section 389 CrPC"]
    ))

    # ER_H_010
    qs.append(make_er_q(
        qid="ER_H_010", diff="Hard", qtype="Single-Choice", subtopic="Social Media Silence Period",
        en_stem="Which high-level committee appointed by the ECI in 2018 under Senior Deputy Election Commissioner Umesh Sinha submitted recommendations on modifying Section 126 of RPA 1951 to regulate social media during the silence period?",
        ta_stem="அமைதிக்காலத்தில் (Silence period) சமூக ஊடகங்களை முறைப்படுத்துவதற்காக மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 126-ஐத் திருத்த பரிந்துரைகளை வழங்க 2018-ல் ECI-யால் அமைக்கப்பட்ட உமேஷ் சின்ஹா குழு சமர்ப்பித்த அறிக்கை எது?",
        en_a="Committee on Review of Section 126 of RPA 1951 in the Context of Digital and Social Media (2019)", ta_a="டிஜிட்டல் மற்றும் சமூக ஊடக பின்னணியில் மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 126-ஐ மறுஆய்வு செய்யும் குழு (2019)",
        en_b="National Cyber Security Action Taskforce for Elections", ta_b="தேர்தல்களுக்கான தேசிய இணையப் பாதுகாப்பு செயல் பணிக்குழு",
        en_c="Special Committee on Artificial Intelligence and Voter Suppression", ta_c="செயற்கை நுண்ணறிவு மற்றும் வாக்காளர் ஒழிப்பு குறித்த சிறப்புக் குழு",
        en_d="Joint Parliamentary Committee on Data Protection in Elections", ta_d="தேர்தல் தரவுப் பாதுகாப்பு குறித்த கூட்டு நாடாளுமன்றக் குழு",
        correct_key="A",
        exp_en="The Umesh Sinha Committee submitted its report in January 2019 recommending amendments to Section 126 of RPA 1951 to bring intermediaries and digital platforms under the 48-hour campaign silence period, leading to the formulation of the 'Voluntary Code of Ethics' by IAMAI and major tech platforms (Google, Meta, Twitter) for Indian elections.",
        exp_ta="உமேஷ் சின்ஹா குழு 2019 ஜனவரியில் தனது அறிக்கையை சமர்ப்பித்து, 48 மணி நேர அமைதிக்கால கட்டுப்பாட்டிற்குள் சமூக ஊடகங்கள் மற்றும் டிஜிட்டல் தளங்களையும் கொண்டுவர பிரிவு 126-ஐ திருத்த பரிந்துரைத்தது. இதன் விளைவாக சமூக ஊடக நிறுவனங்கள் தேர்தலுக்கான 'தன்னார்வ நடத்தை நெறியை' (Voluntary Code of Ethics) உருவாக்கின.",
        why_a_en="Correct. Umesh Sinha Committee on Section 126 and social media.",
        why_a_ta="சரியானது. பிரிவு 126 மற்றும் சமூக ஊடகங்கள் குறித்த உமேஷ் சின்ஹா குழு.",
        why_b_en="Incorrect. Taskforce was not the committee name.",
        why_b_ta="தவறானது. தவறான பெயர்.",
        why_c_en="Incorrect. AI committee is not the title.",
        why_c_ta="தவறானது. தவறான பெயர்.",
        why_d_en="Incorrect. JPC was on the PDP Bill.",
        why_d_ta="தவறானது. JPC தனிநபர் தரவுப் பாதுகாப்பு மசோதா பற்றியது.",
        tip_en="Under the Voluntary Code of Ethics, social media platforms committed to taking down reported MCC violations within 3 hours during the 48-hour silence period.",
        tip_ta="தன்னார்வ நடத்தை நெறியின் கீழ், 48 மணி நேர அமைதிக்காலத்தில் பெறப்படும் தேர்தல் விதிமீறல் புகார்களை 3 மணி நேரத்திற்குள் நீக்க சமூக ஊடக நிறுவனங்கள் உறுதியளித்தன.",
        fact_en="Platforms also set up dedicated high-priority grievance channels for ECI.",
        fact_ta="தேர்தல் ஆணையத்தின் புகார்களுக்கு முன்னுரிமை அளித்து தீர்க்க சிறப்பு சேனல்களை நிறுவனங்கள் அமைத்தன.",
        tags=["Umesh Sinha Committee", "Section 126 Review", "Social Media Silence Period", "IAMAI"]
    ))

    # ER_H_011
    qs.append(make_er_q(
        qid="ER_H_011", diff="Hard", qtype="Single-Choice", subtopic="Constitutional Morality and Ministers",
        en_stem="In Manoj Narula v. Union of India (2014), what did the 5-judge Constitution Bench rule regarding whether a court can issue a writ of mandamus restraining the Prime Minister or Chief Minister from appointing a person facing serious criminal charges as a Minister?",
        ta_stem="மனோஜ் நருலா எதிர் இந்திய ஒன்றியம் (2014) வழக்கில், கடுமையான குற்றச்சாட்டுகளை எதிர்கொள்ளும் ஒரு நபரை அமைச்சராக நியமிக்கக் கூடாது என்று பிரதமர் அல்லது முதல்வருக்கு நீதிமன்றம் உத்தரவிட (Writ of Mandamus) முடியுமா என்பது குறித்து 5 நீதிபதிகள் அமர்வு என்ன தீர்ப்பளித்தது?",
        en_a="Courts cannot issue a writ of mandamus to the PM/CM as Articles 75(1) and 164(1) do not impose such disqualification, but constitutional morality and good governance expect the PM/CM not to appoint tainted persons", ta_a="சரத்து 75(1) மற்றும் 164(1)-ல் அத்தகைய தகுதிநீக்கம் இல்லாததால் நீதிமன்றம் கட்டளை நீதிப்பேராணை பிறப்பிக்க முடியாது; எனினும் அரசியலமைப்பு தர்மம் மற்றும் நல்லாட்சியின் அடிப்படையில் களங்கப்பட்ட நபர்களை நியமிக்காமல் இருப்பது பிரதமர்/முதல்வரின் கடமையாகும்",
        en_b="Courts have absolute power to remove any Minister under Article 226 without consulting the Chief Minister", ta_b="முதல்வரைக் கலந்தாலோசிக்காமல் சரத்து 226-ன் கீழ் எந்தவொரு அமைச்சரையும் நீக்க நீதிமன்றங்களுக்கு முழு அதிகாரம் உண்டு",
        en_c="The Governor must automatically dismiss any Minister against whom a police FIR is lodged", ta_c="காவல்துறை எஃப்.ஐ.ஆர் பதிவு செய்த உடனேயே ஆளுநர் அமைச்சரை தானாக பதவி நீக்கம் செய்ய வேண்டும்",
        en_d="Ministers facing criminal charges must surrender their legislative seats immediately to the High Court", ta_d="குற்றப்பின்னணி கொண்ட அமைச்சர்கள் தங்களது சட்டமன்ற உறுப்பினர் பதவியை உடனே உயர் நீதிமன்றத்திடம் ஒப்படைக்க வேண்டும்",
        correct_key="A",
        exp_en="In Manoj Narula v. UOI (2014), a Constitution Bench headed by CJI R.M. Lodha held that courts cannot add disqualifications to Articles 75(1) and 164(1) through judicial interpretation by barring tainted persons from ministerial office. However, the court appealed to 'constitutional morality', 'constitutional trust', and good governance, reposing faith in the Prime Minister and Chief Ministers not to induct persons with criminal antecedents into the council of ministers.",
        exp_ta="மனோஜ் நருலா வழக்கில் (2014), நீதிமன்றம் சட்டமியற்றும் அதிகாரத்தை கையில் எடுத்துக்கொண்டு அமைச்சர்களுக்கான தகுதிகளில் புதிய கட்டுப்பாடுகளை சேர்க்க முடியாது என்பதால் கட்டளை நீதிப்பேராணை பிறப்பிக்க முடியாது என தீர்ப்பளிக்கப்பட்டது. எனினும் 'அரசியலமைப்பு தர்மம்' (Constitutional Morality) மற்றும் நல்லாட்சியின் அடிப்படையில் களங்கமான நபர்களை அமைச்சராக்காமல் இருப்பது பிரதமர்/முதல்வரின் பொறுப்பாகும் என நீதிமன்றம் அறிவுறுத்தியது.",
        why_a_en="Correct. No mandamus can be issued, but constitutional morality expects PM/CM to act responsibly.",
        why_a_ta="சரியானது. கட்டளை நீதிப்பேராணை பிறப்பிக்க முடியாது; ஆனால் அரசியலமைப்பு தர்மத்தை பிரதமர்/முதல்வர் நிலைநிறுத்த வேண்டும்.",
        why_b_en="Incorrect. Courts cannot directly sack ministers.",
        why_b_ta="தவறானது. நீதிமன்றங்கள் அமைச்சர்களை நேரடியாக நீக்க முடியாது.",
        why_c_en="Incorrect. Mere FIR does not trigger dismissal.",
        why_c_ta="தவறானது. வெறும் எஃப்.ஐ.ஆர் பதவி நீக்கத்திற்கு வழிவகுக்காது.",
        why_d_en="Incorrect. No surrender of seat to High Court.",
        why_d_ta="தவறானது. நீதிமன்றத்திடம் பதவியை ஒப்படைக்க தேவையில்லை.",
        tip_en="Constitutional Morality was strongly emphasized by Justice Dipak Misra in this verdict.",
        tip_ta="நீதிபதி தீபக் மிஸ்ரா தனது தீர்ப்பில் 'அரசியலமைப்பு தர்மம்' என்ற கோட்பாட்டை மிக ஆழமாக வலியுறுத்தினார்.",
        fact_en="Ministers hold office during the pleasure of the President / Governor under Articles 75(2) and 164(2).",
        fact_ta="சரத்து 75(2) மற்றும் 164(2)-ன் படி அமைச்சர்கள் குடியரசுத் தலைவர் / ஆளுநரின் விருப்பம் உள்ளவரை பதவியில் நீடிப்பர்.",
        tags=["Manoj Narula 2014", "Constitutional Morality", "Tainted Ministers", "Article 75"]
    ))

    # ER_H_012
    qs.append(make_er_q(
        qid="ER_H_012", diff="Hard", qtype="Single-Choice", subtopic="Section 9A RPA 1951",
        en_stem="Under Section 9A of the Representation of the People Act, 1951, on what specific ground is a person disqualified for membership of Parliament or State Legislature?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 9A-ன் கீழ், எந்த குறிப்பிட்ட காரணத்திற்காக ஒருவர் நாடாளுமன்ற அல்லது சட்டமன்ற உறுப்பினர் பதவிக்கு தகுதிநீக்கம் செய்யப்படுகிறார்?",
        en_a="Having a subsisting contract with the appropriate Government for the supply of goods to, or for the execution of any works undertaken by, that Government", ta_a="சம்பந்தப்பட்ட அரசுக்கு பொருட்களை வழங்குவதற்காக அல்லது அரசுப் பணிகளை மேற்கொள்வதற்காக அரசுடன் தற்போது நடைமுறையில் உள்ள ஒப்பந்தத்தைக் (Subsisting contract) கொண்டிருப்பது",
        en_b="Failing to pay municipal water and property taxes for more than 2 consecutive years", ta_b="தொடர்ந்து 2 ஆண்டுகளுக்கு மேல் நகராட்சி குடிநீர் மற்றும் சொத்து வரிகளை செலுத்தத் தவறியது",
        en_c="Holding shares in any publicly listed private Indian commercial company", ta_c="பங்குச்சந்தையில் பட்டியலிடப்பட்ட தனியார் நிறுவனங்களில் பங்குகளை வைத்திருப்பது",
        en_d="Being related by blood or marriage to any sitting High Court Judge", ta_d="பதவியில் உள்ள உயர் நீதிமன்ற நீதிபதியுடன் இரத்த அல்லது திருமண உறவு கொண்டிருப்பது",
        correct_key="A",
        exp_en="Section 9A of RPA 1951 provides that a person shall be disqualified if, and for so long as, there subsists a contract entered into by him in the course of his trade or business with the appropriate Government for the supply of goods to, or for the execution of any works undertaken by, that Government. This prevents conflict of interest between public duty and private commercial contracts.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 9A-ன் படி, சம்பந்தப்பட்ட அரசுக்கு பொருட்கள் விநியோகம் செய்ய அல்லது அரசுப் பணிகளை செய்து முடிக்க அரசுடன் நடைமுறையில் உள்ள வணிக ஒப்பந்தங்களை வைத்துள்ள ஒரு நபர், அந்த ஒப்பந்தம் நடைமுறையில் இருக்கும் வரை சட்டமன்ற/நாடாளுமன்ற உறுப்பினராக இருக்க முடியாது (ஆதாய மோதல் தடுப்பு).",
        why_a_en="Correct. Subsisting government contracts for goods or works under Section 9A.",
        why_a_ta="சரியானது. அரசுடன் நடைமுறையில் உள்ள வணிக அல்லது பணி ஒப்பந்தங்கள் பிரிவு 9A-ன் கீழ் தகுதிநீக்கத்திற்கு வழிவகுக்கும்.",
        why_b_en="Incorrect. Municipal tax arrears are not a Section 9A ground.",
        why_b_ta="தவறானது. நகராட்சி வரி பாக்கிகள் பிரிவு 9A-ல் இல்லை.",
        why_c_en="Incorrect. Owning commercial shares is not a disqualification.",
        why_c_ta="தவறானது. பங்குகள் வைத்திருப்பது தகுதிநீக்கம் அல்ல.",
        why_d_en="Incorrect. Relationship to judges is irrelevant.",
        why_d_ta="தவறானது. நீதிபதிகளின் உறவினர் என்பது தகுதியின்மை அல்ல.",
        tip_en="The disqualification ends immediately once the contract is fully performed and discharged by both parties.",
        tip_ta="ஒப்பந்தப் பணிகள் முடிவடைந்து கணக்குகள் நேர் செய்யப்பட்ட உடன் இத்தகுதிநீக்கம் தானாக நீங்கிவிடும்.",
        fact_en="Section 9 disqualifies persons dismissed from government service for corruption or disloyalty for a period of 5 years.",
        fact_ta="பிரிவு 9 ஊழல் அல்லது அரசு துரோகத்திற்காக பணிநீக்கம் செய்யப்பட்ட அரசு ஊழியர்களை 5 ஆண்டுகளுக்கு தகுதிநீக்கம் செய்கிறது.",
        tags=["Section 9A", "Government Contracts", "Conflict of Interest", "RPA 1951"]
    ))

    # ER_H_013
    qs.append(make_er_q(
        qid="ER_H_013", diff="Hard", qtype="Single-Choice", subtopic="Office of Profit",
        en_stem="In Jaya Bachchan v. Union of India (2006), what definitive test was laid down by the Supreme Court to determine whether an office is an 'Office of Profit' under Article 102(1)(a)?",
        ta_stem="ஜெயா பச்சன் எதிர் இந்திய ஒன்றியம் (2006) வழக்கில், ஒரு பதவி சரத்து 102(1)(a)-ன் கீழான 'ஆதாயப் பதவி' (Office of Profit) தானா என்பதைத் தீர்மானிக்க உச்ச நீதிமன்றம் வகுத்த திட்டவட்டமான அளவுகோல் என்ன?",
        en_a="The decisive test is whether the office is capable of yielding a profit or pecuniary gain, regardless of whether the holder actually received or claimed the profit", ta_a="அந்தப் பதவி நிதி ஆதாயம் அல்லது லாபம் தரக்கூடிய சாத்தியக்கூறைக் கொண்டுள்ளதா என்பதே முக்கிய அளவுகோல்; அப்பதவியை வகிப்பவர் உண்மையில் அந்த லாபத்தைப் பெற்றாரா அல்லது விட்டுக்கொடுத்தாரா என்பது முக்கியமல்ல",
        en_b="An office is an office of profit only if the holder draws a monthly salary exceeding ₹1 Lakh", ta_b="பதவி வகிப்பவர் மாதத்திற்கு ₹1 லட்சத்திற்கும் அதிகமான ஊதியம் பெற்றால் மட்டுமே அது ஆதாயப் பதவியாகும்",
        en_c="An office is exempt from being an office of profit if established under state legislation", ta_c="மாநில சட்டத்தின் கீழ் உருவாக்கப்பட்ட பதவிகள் ஆதாயப் பதவி வரையறையிலிருந்து தானாக விலக்கு பெறும்",
        en_d="Only offices with cabinet minister rank qualify as offices of profit", ta_d="கேபினட் அமைச்சர் அந்தஸ்து கொண்ட பதவிகள் மட்டுமே ஆதாயப் பதவிகளாகக் கருதப்படும்",
        correct_key="A",
        exp_en="In Jaya Bachchan v. UOI (2006), the Supreme Court held that an 'office of profit' is an office which is capable of yielding a profit or pecuniary gain. If the office carries pecuniary gain or perquisites, it is an office of profit; it is irrelevant whether the holder chose not to draw the salary or actually received pecuniary benefits.",
        exp_ta="ஜெயா பச்சன் (2006) வழக்கில், ஒரு பதவி பண பலனையோ அல்லது நிதி ஆதாயத்தையோ தரக்கூடிய சாத்தியக்கூறு கொண்டதாக இருந்தாலே அது 'ஆதாயப் பதவி' ஆகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. அப்பதவியை வகிப்பவர் சம்பளத்தை சுயமாக விட்டுக்கொடுத்தாரா அல்லது உண்மையில் பணத்தைப் பெற்றாரா என்பது இதில் முக்கியமல்ல.",
        why_a_en="Correct. Potential/capability of yielding pecuniary gain is the decisive test.",
        why_a_ta="சரியானது. நிதி ஆதாயம் தரும் சாத்தியக்கூறு இருப்பதே ஆதாயப் பதவியை நிர்ணயிக்கும் அளவுகோல்.",
        why_b_en="Incorrect. No ₹1 Lakh numerical threshold exists.",
        why_b_ta="தவறானது. ₹1 லட்சம் என்ற வரம்பு இல்லை.",
        why_c_en="Incorrect. State legislation cannot arbitrarily exempt offices unless Parliament enacts an exemption law under Article 102(1)(a).",
        why_c_ta="தவறானது. நாடாளுமன்ற விதிவிலக்கு சட்டம் இயற்றினால் மட்டுமே விலக்கு கிடைக்கும்.",
        why_d_en="Incorrect. Applies to any office under government.",
        why_d_ta="தவறானது. அரசின் கீழான அனைத்து பதவிகளுக்கும் பொருந்தும்.",
        tip_en="Under Article 102(1)(a), Parliament has enacted the Parliament (Prevention of Disqualification) Act, 1959 listing exempt offices.",
        tip_ta="சரத்து 102(1)(a)-ன் கீழ் நாடாளுமன்றம் 1959-ல் தகுதிநீக்கத் தடுப்புச் சட்டத்தை இயற்றி சில குறிப்பிட்ட பதவிகளுக்கு விலக்கு அளித்துள்ளது.",
        fact_en="Jaya Bachchan was disqualified as a Rajya Sabha MP because she held the office of Chairperson of the UP Film Development Council.",
        fact_ta="உத்தரபிரதேச திரைப்பட வளர்ச்சிக் கழகத்தின் தலைவராக இருந்ததால் ஜெயா பச்சன் மாநிலங்களவை உறுப்பினர் பதவியிலிருந்து தகுதிநீக்கம் செய்யப்பட்டார்.",
        tags=["Office of Profit", "Jaya Bachchan 2006", "Article 102(1)(a)", "Pecuniary Gain Test"]
    ))

    # ER_H_014
    qs.append(make_er_q(
        qid="ER_H_014", diff="Hard", qtype="Single-Choice", subtopic="Section 123(3A) RPA 1951",
        en_stem="Under Section 123(3A) of the Representation of the People Act, 1951, what specific conduct is categorized as a corrupt practice?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 123(3A)-ன் கீழ், எந்த குறிப்பிட்ட செயல் ஊழல் நடைமுறையாக (Corrupt Practice) வகைப்படுத்தப்பட்டுள்ளது?",
        en_a="Promoting or attempting to promote feelings of enmity or hatred between different classes of citizens on grounds of religion, race, caste, community, or language for electoral prospects", ta_a="தேர்தல் வெற்றிக்காக மதம், இனம், ஜாதி, சமூகம் அல்லது மொழியின் அடிப்படையில் குடிமக்களிடையே பகையுணர்வை அல்லது வெறுப்பைத் தூண்டுவது அல்லது தூண்ட முயற்சிப்பது",
        en_b="Filing nomination papers in more than two different languages", ta_b="இரண்டுக்கும் மேற்பட்ட மொழிகளில் வேட்புமனுவைத் தாக்கல் செய்வது",
        en_c="Criticizing the economic policies of the incumbent Union Government during election rallies", ta_c="தேர்தல் கூட்டங்களில் ஆளும் மத்திய அரசின் பொருளாதாரக் கொள்கைகளை விமர்சிப்பது",
        en_d="Distributing party manifestos printed on recycled eco-friendly paper", ta_d="மறுசுழற்சி செய்யப்பட்ட காகிதத்தில் அச்சிடப்பட்ட தேர்தல் அறிக்கைகளை விநியோகிப்பது",
        correct_key="A",
        exp_en="Section 123(3A) was inserted into RPA 1951 in 1961, making the promotion of, or attempt to promote, feelings of enmity or hatred between different classes of the citizens of India on grounds of religion, race, caste, community, or language, by a candidate or his agent for the furtherance of election prospects, a corrupt practice.",
        exp_ta="1961-ல் சேர்க்கப்பட்ட பிரிவு 123(3A)-ன் படி, தேர்தல் ஆதாயத்திற்காக வேட்பாளரோ அவரது முகவரோ மதம், இனம், ஜாதி, சமூகம் அல்லது மொழி அடிப்படையில் மக்களிடையே பகைமை அல்லது வெறுப்புணர்வைத் தூண்டுவது கடுமையான ஊழல் நடைமுறையாகும்.",
        why_a_en="Correct. Promoting enmity on communal/linguistic lines under Section 123(3A).",
        why_a_ta="சரியானது. பிரிவு 123(3A)-ன் கீழ் மக்களிடையே பகைமை மற்றும் வெறுப்பைத் தூண்டுவது ஊழல் நடைமுறை.",
        why_b_en="Incorrect. Language of nomination forms is governed by statutory rules.",
        why_b_ta="தவறானது. மனு மொழியுடன் தொடர்புடையது அல்ல.",
        why_c_en="Incorrect. Legitimate policy criticism is protected under Article 19(1)(a).",
        why_c_ta="தவறானது. அரசின் கொள்கைகளை விமர்சிப்பது ஜனநாயக உரிமை.",
        why_d_en="Incorrect. Eco-friendly manifestos are encouraged.",
        why_d_ta="தவறானது. சூழல் நட்பு பிரச்சாரம் வரவேற்கத்தக்கது.",
        tip_en="Section 125 of RPA 1951 makes the same act an ELECTORAL OFFENCE punishable with imprisonment up to 3 years or fine or both.",
        tip_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 125 இதே செயலை 3 ஆண்டுகள் வரை சிறைத்தண்டனைக்குரிய 'தேர்தல் குற்றமாகவும்' ஆக்குகிறது.",
        fact_en="Section 123(3A) mirrors Section 153A of the Indian Penal Code.",
        fact_ta="பிரிவு 123(3A) இந்திய தண்டனைச் சட்டம் பிரிவு 153A-ன் தேர்தல் வடிவமாகும்.",
        tags=["Section 123(3A)", "Promoting Enmity", "Corrupt Practice", "Hate Speech"]
    ))

    # ER_H_015
    qs.append(make_er_q(
        qid="ER_H_015", diff="Hard", qtype="Single-Choice", subtopic="Section 126A Exit Polls Constitutional Validity",
        en_stem="In which year was Section 126A inserted into the Representation of the People Act, 1951, imposing a blanket ban on exit polls during multi-phase elections?",
        ta_stem="பல கட்டங்களாக நடைபெறும் தேர்தல்களின் போது தேர்தல் பிந்தைய வாக்குக்கணிப்புகளுக்கு (Exit Polls) முழுமையான தடை விதிக்கும் பிரிவு 126A மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ல் எந்த ஆண்டு சேர்க்கப்பட்டது?",
        en_a="2009", ta_a="2009",
        en_b="1989", ta_b="1989",
        en_c="1996", ta_c="1996",
        en_d="2019", ta_d="2019",
        correct_key="A",
        exp_en="Section 126A was inserted into the Representation of the People Act, 1951 by the Representation of the People (Amendment) Act, 2009 (effective from 1 February 2010), prohibiting conduct and dissemination of exit polls from the start of the first phase of polling until 30 minutes after the close of the final phase.",
        exp_ta="மக்கள் பிரதிநிதித்துவ திருத்தச் சட்டம் 2009 மூலம் பிரிவு 126A இணைக்கப்பட்டு (2010 பிப்ரவரி 1 முதல் அமல்), முதற்கட்ட வாக்குப்பதிவு தொடங்கி இறுதிக்கட்ட வாக்குப்பதிவு முடிந்து 30 நிமிடங்கள் வரை வாக்குக்கணிப்புகளை நடத்துவதற்கும் வெளியிடுவதற்கும் முழுமையான தடை விதிக்கப்பட்டது.",
        why_a_en="Correct. Inserted by the 2009 Amendment Act.",
        why_a_ta="சரியானது. 2009 திருத்தச் சட்டம் மூலம் இணைக்கப்பட்டது.",
        why_b_en="Incorrect. 1989 was Section 61A (EVMs) and Section 29A (party registration).",
        why_b_ta="தவறானது. 1989-ல் EVM மற்றும் கட்சி பதிவு விதிகள் வந்தன.",
        why_c_en="Incorrect. 1996 was the major electoral reforms package under Indrajit Gupta/Goswami follow-up.",
        why_c_ta="தவறானது. 1996-ல் முக்கிய தேர்தல் சீர்திருத்தங்கள் செய்யப்பட்டன.",
        why_d_en="Incorrect. 2019 was the year of 100% VVPAT deployment.",
        why_d_ta="தவறானது. 2019-ல் 100% VVPAT அறிமுகமானது.",
        tip_en="Punishment under Section 126A is imprisonment for a term which may extend to 2 years, or with fine, or with both.",
        tip_ta="பிரிவு 126A மீறலுக்கு 2 ஆண்டுகள் வரை சிறை அல்லது அபராதம் விதிக்கப்படலாம்.",
        fact_en="Before this statutory ban, ECI had tried to restrict exit polls via guidelines, which the Supreme Court had struck down in 1999 for lack of legislative authority.",
        fact_ta="இச்சட்டத்திற்கு முன் ECI வழிகாட்டுதல்கள் மூலம் தடை செய்ய முயன்றது; ஆனால் சட்ட அதிகாரம் இல்லாததால் 1999-ல் நீதிமன்றம் அதை ரத்து செய்திருந்தது.",
        tags=["Section 126A", "Exit Polls Ban", "2009 Amendment"]
    ))

    # ER_H_016
    qs.append(make_er_q(
        qid="ER_H_016", diff="Hard", qtype="Single-Choice", subtopic="Section 160 Requisitioning Premises",
        en_stem="Under Section 160 of the Representation of the People Act, 1951, which category of premises is explicitly EXEMPT from being requisitioned by the State Government for election purposes?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 160-ன் கீழ், தேர்தல் பணிகளுக்காக மாநில அரசால் கையகப்படுத்தப்படுவதிலிருந்து (Requisitioning) வெளிப்படையாக விலக்கு அளிக்கப்பட்டுள்ள வளாகம் எது?",
        en_a="Premises being used as a place of religious worship, or as a school other than an educational institution aided by the State", ta_a="மத வழிபாட்டுத் தலங்களாகப் பயன்படுத்தப்படும் வளாகங்கள் அல்லது அரசு உதவி பெறாத தனியார் பள்ளிகள்",
        en_b="Government collectorate offices and circuit houses", ta_b="அரசு மாவட்ட ஆட்சியர் அலுவலகங்கள் மற்றும் சுற்றுலா மாளிகைகள்",
        en_c="Private commercial transport buses licensed for inter-state travel", ta_c="மாநிலங்களுக்கு இடையே இயங்கும் தனியார் வணிக பேருந்துகள்",
        en_d="Public university examination halls and college auditoriums", ta_d="பொதுப் பல்கலைக்கழக தேர்வுக்கூடங்கள் மற்றும் கல்லூரி அரங்குகள்",
        correct_key="A",
        exp_en="Section 160(1) proviso of RPA 1951 explicitly provides that no premises or part thereof which is being used exclusively as a place of religious worship, or as a school (other than an educational institution aided by the State) shall be requisitioned for election polling, counting, or vehicle storage.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 160(1) வரம்புரையின்படி, பிரத்யேகமாக மத வழிபாட்டுத் தலங்களாகப் பயன்படுத்தப்படும் இடங்கள் மற்றும் அரசு உதவி பெறாத தனியார் கல்வி நிறுவனங்கள் தேர்தல் பணிகளுக்காக கையகப்படுத்தப்படக் கூடாது என விலக்களிக்கப்பட்டுள்ளது.",
        why_a_en="Correct. Religious places of worship and unaided schools are exempt under Section 160 proviso.",
        why_a_ta="சரியானது. வழிபாட்டுத் தலங்கள் மற்றும் அரசு உதவி பெறாத பள்ளிகளுக்கு பிரிவு 160-ல் விலக்கு உண்டு.",
        why_b_en="Incorrect. Government premises are routinely requisitioned.",
        why_b_ta="தவறானது. அரசு வளாகங்கள் தேர்தல் பணிகளுக்குப் பயன்படுகின்றன.",
        why_c_en="Incorrect. Vehicles can be requisitioned under Section 160(1)(b) subject to compensation.",
        why_c_ta="தவறானது. இழப்பீடு வழங்கி தனியார் வாகனங்களைக் கையகப்படுத்தலாம்.",
        why_d_en="Incorrect. Aided colleges and public universities are routinely requisitioned for counting centers.",
        why_d_ta="தவறானது. கல்லூரிகள் வாக்கு எண்ணும் மையங்களாகப் பயன்படுகின்றன.",
        tip_en="Section 161 guarantees payment of reasonable compensation to the owner of requisitioned premises or vehicles.",
        tip_ta="பிரிவு 161 கையகப்படுத்தப்பட்ட வாகனங்கள் மற்றும் வளாகங்களுக்கு நியாயமான இழப்பீடு வழங்குவதை உறுதி செய்கிறது.",
        fact_en="Section 167 makes refusal to comply with a requisition order a penal offence punishable with imprisonment up to 1 year.",
        fact_ta="கையகப்படுத்தும் உத்தரவை மதிக்கத் தவறினால் பிரிவு 167-ன் கீழ் 1 ஆண்டு வரை சிறைத்தண்டனை விதிக்கப்படலாம்.",
        tags=["Section 160", "Requisitioning Premises", "Religious Worship Exemption"]
    ))

    # ER_H_017
    qs.append(make_er_q(
        qid="ER_H_017", diff="Hard", qtype="Single-Choice", subtopic="Section 58A Adjournment of Poll",
        en_stem="Under Section 58A of the Representation of the People Act, 1951, what exceptional power can the Election Commission exercise if large-scale booth capturing takes place in a constituency?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 58A-ன் கீழ், ஒரு தொகுதியில் பெருமளவிலான வாக்குச்சாவடி கைப்பற்றுதல் நடைபெற்றால் தேர்தல் ஆணையம் பயன்படுத்தக்கூடிய விதிவிலக்கான அதிகாரம் எது?",
        en_a="Declare the poll at that polling station or in that entire constituency to be void, and direct a fresh poll or countermand the election", ta_a="அந்த வாக்குச்சாவடியில் அல்லது அத்தொகுதி முழுவதிலும் நடைபெற்ற வாக்கெடுப்பை செல்லாது என அறிவித்து மறுவாக்குப்பதிவு நடத்த அல்லது தேர்தலையே முழுமையாக ரத்து செய்ய உத்தரவிடுவது",
        en_b="Direct the immediate imposition of financial emergency under Article 360", ta_b="சரத்து 360-ன் கீழ் உடனடி நிதி அவசரநிலையை அறிவிக்க உத்தரவிடுவது",
        en_c="Dissolve the State Public Service Commission with immediate effect", ta_c="மாநில அரசுப் பணியாளர் தேர்வாணையத்தை உடனடியாக கலைப்பது",
        en_d="Deprive the entire electorate of that district from voting for the next 10 years", ta_d="அடுத்த 10 ஆண்டுகளுக்கு அந்த மாவட்ட வாக்காளர்களின் வாக்குரிமையை பறிப்பது",
        correct_key="A",
        exp_en="Section 58A of RPA 1951 (inserted in 1989) empowers the Election Commission, upon receiving a report from the Returning Officer or Election Observer regarding large-scale booth capturing, to declare the poll at the affected polling stations or across the ENTIRE constituency void, and appoint a day for taking a fresh poll, or countermand the election entirely.",
        exp_ta="1989-ல் சேர்க்கப்பட்ட பிரிவு 58A, பெருமளவில் வாக்குச்சாவடிகள் கைப்பற்றப்பட்டால், பாதிக்கப்பட்ட வாக்குச்சாவடிகள் அல்லது முழு தொகுதியின் தேர்தலையும் செல்லாது என அறிவித்து மறுதேர்தல் நடத்தவோ அல்லது தேர்தலை முற்றிலுமாக ரத்து செய்யவோ தேர்தல் ஆணையத்திற்கு முழு அதிகாரம் அளிக்கிறது.",
        why_a_en="Correct. Section 58A empowers ECI to void the poll and order fresh polling or countermand the election.",
        why_a_ta="சரியானது. தேர்தலை ரத்து செய்து மறுவாக்குப்பதிவு நடத்த பிரிவு 58A அதிகாரம் அளிக்கிறது.",
        why_b_en="Incorrect. Article 360 is the President's financial emergency power.",
        why_b_ta="தவறானது. சரத்து 360 நிதி அவசரநிலை பற்றியது.",
        why_c_en="Incorrect. State PSC is unrelated.",
        why_c_ta="தவறானது. டிஎன்பிஎஸ்சி போன்ற அமைப்புகளுக்கு தொடர்பில்லை.",
        why_d_en="Incorrect. Collective disenfranchisement is unconstitutional.",
        why_d_ta="தவறானது. மொத்த வாக்காளர்களையும் வாக்களிக்க விடாமல் தடுக்க முடியாது.",
        tip_en="Section 58 deals with destruction of ballot boxes/EVMs at individual stations; Section 58A deals specifically with booth capturing.",
        tip_ta="பிரிவு 58 வாக்குப்பெட்டி சேதமடைதலைக் கையாள்கிறது; பிரிவு 58A வாக்குச்சாவடி கைப்பற்றுதலைக் கையாள்கிறது.",
        fact_en="Section 58A was famously deployed in the 1990s by CEC T.N. Seshan to countermand rigged elections in Bihar and UP.",
        fact_ta="1990-களில் பீகார் மற்றும் உ.பி-யில் முறைகேடுகள் நடந்த தேர்தல்களை ரத்து செய்ய டி.என். சேஷன் இப்பிரிவு 58A-ஐ பரவலாகப் பயன்படுத்தினார்.",
        tags=["Section 58A", "Booth Capturing", "Countermanding Election", "ECI Power"]
    ))

    # ER_H_018
    qs.append(make_er_q(
        qid="ER_H_018", diff="Hard", qtype="Single-Choice", subtopic="Section 20A Overseas Electors",
        en_stem="Under Section 20A of the Representation of the People Act, 1950 (inserted in 2010), what condition must an Overseas Elector fulfill to be enrolled in the electoral roll of a constituency?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1950 பிரிவு 20A-ன் கீழ் (2010-ல் சேர்க்கப்பட்டது), ஒரு வெளிநாடு வாழ் இந்தியர் ஒரு தொகுதியின் வாக்காளர் பட்டியலில் பதிவு செய்ய பூர்த்தி செய்ய வேண்டிய நிபந்தனை என்ன?",
        en_a="Must be an Indian citizen living abroad who has not acquired citizenship of any other country, registered at the address mentioned in their valid Indian passport", ta_a="வேறு எந்த நாட்டின் குடியுரிமையையும் பெறாமல் வெளிநாட்டில் வசிக்கும் இந்திய குடிமகனாக இருக்க வேண்டும்; தனது செல்லுபடியாகும் இந்திய பாஸ்போர்ட்டில் உள்ள முகவரியில் பதிவு செய்யப்பட வேண்டும்",
        en_b="Must have resided physically in the Indian constituency for at least 180 days in the previous year", ta_b="கடந்த ஆண்டில் அந்த இந்திய தொகுதியில் குறைந்தது 180 நாட்கள் நேரில் வசித்திருக்க வேண்டும்",
        en_c="Must renounce all financial assets and property owned in foreign countries", ta_c="வெளிநாடுகளில் உள்ள அனைத்து சொத்துக்களையும் நிதி முதலீடுகளையும் துறந்திருக்க வேண்டும்",
        en_d="Must hold an Overseas Citizen of India (OCI) card issued by the Ministry of Home Affairs", ta_d="மத்திய உள்துறை அமைச்சகத்தால் வழங்கப்பட்ட OCI அட்டை வைத்திருக்க வேண்டும்",
        correct_key="A",
        exp_en="Section 20A of RPA 1950 (inserted by the 2010 Amendment Act) provides that a citizen of India residing outside India, who has not acquired the citizenship of any other country and is not disqualified, is eligible to be registered in the electoral roll in the constituency in which his place of residence in India as mentioned in his passport is located.",
        exp_ta="2010 சட்டத்திருத்தத்தால் சேர்க்கப்பட்ட பிரிவு 20A-ன் படி, வெளிநாட்டு குடியுரிமை பெறாத இந்திய பாஸ்போர்ட் வைத்துள்ள இந்திய குடிமகன், தனது பாஸ்போர்ட்டில் குறிப்பிடப்பட்டுள்ள இந்திய முகவரியைக் கொண்ட சட்டமன்ற/நாடாளுமன்ற தொகுதியில் வாக்காளராக பதிவு செய்யலாம்.",
        why_a_en="Correct. Indian passport holder without foreign citizenship registered at passport address.",
        why_a_ta="சரியானது. பாஸ்போர்ட்டில் உள்ள முகவரியில் பதிவு செய்யப்படும் வெளிநாட்டு குடியுரிமை பெறாத இந்தியர்.",
        why_b_en="Incorrect. The ordinary residence requirement is explicitly waived for overseas electors under Section 20A.",
        why_b_ta="தவறானது. 180 நாட்கள் வசிக்க வேண்டும் என்ற நிபந்தனையிலிருந்து பிரிவு 20A விலக்கு அளிக்கிறது.",
        why_c_en="Incorrect. Asset ownership is unrestricted.",
        why_c_ta="தவறானது. சொத்துக்களை துறக்க வேண்டிய அவசியமில்லை.",
        why_d_en="Incorrect. OCI cardholders are foreign citizens and have NO voting rights in India.",
        why_d_ta="தவறானது. OCI அட்டைதாரர்கள் வெளிநாட்டு குடிமக்கள்; அவர்களுக்கு இந்தியாவில் வாக்குரிமை கிடையாது.",
        tip_en="OCI / PIO cardholders are NOT Indian citizens and CANNOT vote. Only NRI citizens holding Indian passports can vote.",
        tip_ta="OCI / PIO அட்டைதாரர்களுக்கு வாக்குரிமை இல்லை; இந்திய பாஸ்போர்ட் கொண்ட NRI-களுக்கு மட்டுமே வாக்குரிமை உண்டு.",
        fact_en="Overseas electors apply online using Form 6A to the Electoral Registration Officer (ERO).",
        fact_ta="வெளிநாடு வாழ் இந்திய வாக்காளர்கள் படிவம் 6A மூலம் ஆன்லைனில் விண்ணப்பிக்கலாம்.",
        tags=["Section 20A", "NRI Voting", "Form 6A", "Indian Passport"]
    ))

    # ER_H_019
    qs.append(make_er_q(
        qid="ER_H_019", diff="Hard", qtype="Single-Choice", subtopic="Section 16 RPA 1950",
        en_stem="Under Section 16(1) of the Representation of the People Act, 1950, which of the following is a statutory ground for disqualification from registration in an electoral roll?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1950 பிரிவு 16(1)-ன் கீழ், ஒரு வாக்காளர் பட்டியலில் பதிவு செய்யப்படுவதற்கான சட்டப்பூர்வ தகுதியின்மை எது?",
        en_a="If the person is not a citizen of India, is of unsound mind and stands so declared by a competent court, or is disqualified under law relating to corrupt practices/electoral offences", ta_a="ஒருவர் இந்திய குடிமகனாக இல்லாதிருத்தல், மனநலம் குன்றியவர் என தகுதிவாய்ந்த நீதிமன்றத்தால் அறிவிக்கப்பட்டிருத்தல், அல்லது ஊழல் நடைமுறை/தேர்தல் குற்றங்களுக்காக சட்டப்படி தகுதிநீக்கம் செய்யப்பட்டிருத்தல்",
        en_b="If the person does not own any immovable agricultural land or residential property in the state", ta_b="மாநிலத்தில் அசையா விவசாய நிலமோ அல்லது குடியிருப்பு வீடோ சொந்தமாக இல்லாதிருத்தல்",
        en_c="If the person has not completed a minimum of 10 years of formal school education", ta_c="குறைந்தது 10 ஆண்டுகள் பள்ளிப் படிப்பை முடித்திருக்காதிருத்தல்",
        en_d="If the person is in default of paying state electricity and utility dues", ta_d="மாநில மின்சார கட்டணம் மற்றும் பயன்பாட்டுக் கட்டணங்களை செலுத்தாமல் பாக்கி வைத்திருத்தல்",
        correct_key="A",
        exp_en="Section 16(1) of RPA 1950 lays down three grounds of disqualification from registration in an electoral roll: (a) is not a citizen of India; (b) is of unsound mind and stands so declared by a competent court; or (c) is for the time being disqualified from voting under the provisions of any law relating to corrupt practices and other offences in connection with elections.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1950 பிரிவு 16(1)-ன் படி, வாக்காளர் பட்டியலில் சேர்ப்பதற்கான தகுதியின்மைகள்: (a) இந்திய குடிமகனாக இல்லாதிருத்தல்; (b) மனநலம் குன்றியவர் என நீதிமன்றத்தால் அறிவிக்கப்பட்டிருத்தல்; (c) தேர்தல் குற்றங்கள் அல்லது ஊழல் நடைமுறைகளுக்காக தகுதிநீக்கம் செய்யப்பட்டிருத்தல்.",
        why_a_en="Correct. Non-citizenship, declared unsound mind, and election offence disqualification under Section 16.",
        why_a_ta="சரியானது. வெளிநாட்டினர், மனநலக்குறைபாடு மற்றும் தேர்தல் குற்ற தகுதிநீக்கம் பிரிவு 16-ன் கீழ் வாக்காளர் பதிவை ரத்து செய்யும்.",
        why_b_en="Incorrect. Property qualifications were eliminated in 1950.",
        why_b_ta="தவறானது. சொத்து தகுதி 1950-ல் ஒழிக்கப்பட்டது.",
        why_c_en="Incorrect. Educational qualification is not required for voting.",
        why_c_ta="தவறானது. கல்வித்தகுதி தேவையில்லை.",
        why_d_en="Incorrect. Utility bill defaults do not affect franchise.",
        why_d_ta="தவறானது. மின்கட்டண பாக்கி வாக்குரிமையைப் பாதிக்காது.",
        tip_en="If a registered person incurs any of these disqualifications, their name is immediately struck off the electoral roll under Section 16(2).",
        tip_ta="பதிவு செய்த பிறகு மேற்கண்ட தகுதியின்மை ஏற்பட்டால், பிரிவு 16(2)-ன் கீழ் பெயர் வாக்காளர் பட்டியலிலிருந்து உடனே நீக்கப்படும்.",
        fact_en="Section 16 directly operationalizes the constitutional mandate of Article 326.",
        fact_ta="பிரிவு 16 அரசியலமைப்பின் சரத்து 326-ன் விதிகளை சட்டப்பூர்வமாக செயல்படுத்துகிறது.",
        tags=["Section 16", "Disqualification from Electoral Roll", "RPA 1950"]
    ))

    # ER_H_020
    qs.append(make_er_q(
        qid="ER_H_020", diff="Hard", qtype="Single-Choice", subtopic="Statutory Forms",
        en_stem="Under the Conduct of Elections Rules, 1961, which statutory form contains the 'Account of Votes Recorded' and is handed over to the polling agents of all candidates at the close of poll?",
        ta_stem="தேர்தல் நடத்தை விதிகள் 1961-ன் கீழ், வாக்குப்பதிவு முடிந்ததும் 'பதிவான வாக்குகளின் கணக்கு' (Account of Votes Recorded) விவரங்களை அனைத்து வேட்பாளர்களின் முகவர்களுக்கும் வழங்கப்படும் சட்டப்பூர்வ படிவம் எது?",
        en_a="Form 17C", ta_a="படிவம் 17C (Form 17C)",
        en_b="Form 17A", ta_b="படிவம் 17A (Form 17A)",
        en_c="Form 20", ta_c="படிவம் 20 (Form 20)",
        en_d="Form 21E", ta_d="படிவம் 21E (Form 21E)",
        correct_key="A",
        exp_en="Form 17C (Part I) is the statutory 'Account of Votes Recorded' prepared by the Presiding Officer under Rule 49S and Rule 56C. An attested copy is mandatorily handed over to the polling agent of every candidate at the close of poll. On counting day, the votes found in the Control Unit are matched with Form 17C.",
        exp_ta="படிவம் 17C (பகுதி I) என்பது விதி 49S மற்றும் 56C-ன் கீழ் வாக்குச்சாவடி தலைமை அலுவலரால் தயாரிக்கப்படும் 'பதிவான வாக்குகளின் கணக்கு' ஆகும். இதன் சான்றளிக்கப்பட்ட நகல் வாக்குப்பதிவு முடிந்ததும் முகவர்களிடம் வழங்கப்படுகிறது. வாக்கு எண்ணிக்கையின் போது EVM வாக்குகளுடன் இது ஒப்பிடப்படுகிறது.",
        why_a_en="Correct. Form 17C is the Account of Votes Recorded.",
        why_a_ta="சரியானது. பதிவான வாக்குகளின் கணக்கு படிவம் 17C ஆகும்.",
        why_b_en="Incorrect. Form 17A is the Register of Voters signed by electors before casting their vote.",
        why_b_ta="தவறானது. படிவம் 17A என்பது வாக்காளர் பதிவேடு (கையொப்பம் இடும் பதிவேடு).",
        why_c_en="Incorrect. Form 20 is the Final Result Sheet prepared after counting is complete.",
        why_c_ta="தவறானது. படிவம் 20 என்பது வாக்கு எண்ணிக்கைக்குப் பின் தயாரிக்கப்படும் இறுதி முடிவு தாள்.",
        why_d_en="Incorrect. Form 21E is the Return of Election (Certificate of Election handed to the winner).",
        why_d_ta="தவறானது. படிவம் 21E என்பது வெற்றிச் சான்றிதழ் படிவமாகும்.",
        tip_en="Master the sequence: Form 17A = Voter Register -> Form 17C = Account of Votes -> Form 20 = Result Sheet -> Form 21E = Winner Certificate.",
        tip_ta="வரிசையை நினைவில் கொள்க: படிவம் 17A = வாக்காளர் பதிவேடு -> படிவம் 17C = வாக்குக் கணக்கு -> படிவம் 20 = முடிவு தாள் -> படிவம் 21E = வெற்றிச் சான்றிதழ்.",
        fact_en="Matching the total votes in the Control Unit with Form 17C is the primary check against post-poll vote manipulation.",
        fact_ta="EVM வாக்குகளை படிவம் 17C-உடன் ஒப்பிட்டுப் பார்ப்பதே தேர்தல் முறைகேடுகளைத் தடுக்கும் முதன்மைப் பாதுகாப்பாகும்.",
        tags=["Form 17C", "Account of Votes Recorded", "Conduct of Elections Rules"]
    ))

    # ER_H_021
    qs.append(make_er_q(
        qid="ER_H_021", diff="Hard", qtype="Single-Choice", subtopic="Statutory Forms",
        en_stem="Which statutory document signed by electors before pressing the button on the EVM was central to the controversy in the NOTA vs Rule 49-O debate?",
        ta_stem="EVM பொத்தானை அழுத்துவதற்கு முன் வாக்காளர்கள் கையொப்பமிடும் எந்த சட்டப்பூர்வ ஆவணம், NOTA மற்றும் விதி 49-O விவாதத்தின் மையமாக அமைந்தது?",
        en_a="Form 17A (Register of Voters)", ta_a="படிவம் 17A (வாக்காளர் பதிவேடு)",
        en_b="Form 17C (Account of Votes)", ta_b="படிவம் 17C (வாக்குக் கணக்கு)",
        en_c="Form 7 (Objection Form)", ta_c="படிவம் 7 (ஆட்சேபனை படிவம்)",
        en_d="Form 24A (Donation Report)", ta_d="படிவம் 24A (நன்கொடை அறிக்கை)",
        correct_key="A",
        exp_en="Form 17A is the Register of Voters maintained under Rule 49L. Under the old Rule 49-O, if an elector decided not to vote for any candidate, an entry had to be made in Form 17A and signed by the elector, which exposed their identity and violated the secrecy of the ballot. This was replaced by NOTA on the EVM following PUCL (2013).",
        exp_ta="படிவம் 17A என்பது வாக்காளர் கையொப்பமிடும் பதிவேடாகும். பழைய விதி 49-O-ன் கீழ் யாருக்கும் வாக்களிக்க விரும்பாதவர் படிவம் 17A-ல் கையொப்பமிட்டு பகிரங்கமாக பதிவு செய்ய வேண்டியிருந்தது; இது ரகசியத்தை மீறியதால், உச்ச நீதிமன்றம் EVM-லேயே NOTA பொத்தானைக் கொண்டுவர உத்தரவிட்டது.",
        why_a_en="Correct. Form 17A is the Register of Voters.",
        why_a_ta="சரியானது. வாக்காளர் கையொப்பமிடும் படிவம் 17A ஆகும்.",
        why_b_en="Incorrect. Form 17C is the summary of recorded votes.",
        why_b_ta="தவறானது. படிவம் 17C என்பது வாக்குக் கணக்கு தாள்.",
        why_c_en="Incorrect. Form 7 is for voter deletion.",
        why_c_ta="தவறானது. படிவம் 7 பெயர் நீக்கத்திற்கான படிவம்.",
        why_d_en="Incorrect. Form 24A is for political party contribution reporting under Section 29C.",
        why_d_ta="தவறானது. படிவம் 24A கட்சிகள் நன்கொடை அறிக்கையை தாக்கல் செய்யும் படிவம்.",
        tip_en="Every voter who enters the polling booth is numbered sequentially in Form 17A.",
        tip_ta="வாக்குச்சாவடிக்குள் நுழையும் ஒவ்வொரு வாக்காளருக்கும் படிவம் 17A-ல் வரிசை எண் வழங்கப்படுகிறது.",
        fact_en="The total number of voters entered in Form 17A must match the total votes polled in the EVM (plus any tendered votes/test votes accounted for).",
        fact_ta="படிவம் 17A-ல் பதிவான மொத்த வாக்காளர்களின் எண்ணிக்கை EVM-ல் பதிவான மொத்த வாக்குகளுடன் சரியாகப் பொருந்த வேண்டும்.",
        tags=["Form 17A", "Register of Voters", "Rule 49-O", "NOTA Origin"]
    ))

    # ER_H_022
    qs.append(make_er_q(
        qid="ER_H_022", diff="Hard", qtype="Single-Choice", subtopic="Tendered Votes",
        en_stem="Under Rule 49P of the Conduct of Elections Rules, 1961, when a genuine voter arrives at a polling station and discovers that someone has already fraudulently cast their vote, in what manner is their vote cast?",
        ta_stem="தேர்தல் நடத்தை விதிகள் 1961 விதி 49P-ன் கீழ், ஒரு உண்மையான வாக்காளர் வாக்குச்சாவடிக்கு வரும்போது அவரது வாக்கை வேறொருவர் கள்ள ஓட்டாக போட்டுவிட்டது தெரியவந்தால், அவர் தனது வாக்கை எவ்வாறு செலுத்த அனுமதிக்கப்படுகிறார்?",
        en_a="By marking a specially serialized paper ballot paper (called a Tendered Ballot Paper) which is placed in a separate sealed envelope, NOT on the EVM", ta_a="EVM-ல் இல்லாமல், தனி முத்திரையிடப்பட்ட உறைக்குள் வைக்கப்படும் 'ஒப்படைக்கப்பட்ட வாக்குச்சீட்டு' (Tendered Ballot Paper) என்ற சிறப்பு காகித வாக்குச்சீட்டு மூலம்",
        en_b="By pressing the NOTA button twice on the EVM to cancel the duplicate vote", ta_b="இரட்டை வாக்கை ரத்து செய்ய EVM-ல் NOTA பொத்தானை இருமுறை அழுத்துவதன் மூலம்",
        en_c="By an oral declaration made before the police officer on election duty", ta_c="தேர்தல் பணியில் உள்ள காவல் அதிகாரியிடம் வாய்மொழி வாக்குமூலம் அளிப்பதன் மூலம்",
        en_d="The genuine voter is permanently turned away without being allowed to vote", ta_d="உண்மையான வாக்காளர் வாக்களிக்க அனுமதிக்கப்படாமல் திருப்பி அனுப்பப்படுகிறார்",
        correct_key="A",
        exp_en="Under Rule 49P, if a person representing himself to be a particular elector applies for a ballot paper after another person has already voted as such elector, the Presiding Officer, upon satisfying himself of their identity, issues a 'Tendered Ballot Paper' (Form 17B). The elector marks their vote secretly on paper and places it in a specially sealed cover; tendered votes are not counted unless ordered by the High Court in an election petition.",
        exp_ta="விதி 49P-ன் படி, ஆள்மாறாட்டம் செய்யப்பட்டு ஏற்கெனவே வாக்கு பதிவாகிவிட்ட நிலையில் உண்மையான வாக்காளர் வந்தால், தலைமை அலுவலர் அடையாளம் கண்டு அவருக்கு 'ஒப்படைக்கப்பட்ட வாக்குச்சீட்டை' (Tendered Ballot) வழங்குவார். இது காகித வாக்குச்சீட்டில் செலுத்தப்பட்டு தனி உறையில் வைக்கப்படும்; தேர்தல் வழக்கில் உயர் நீதிமன்றம் உத்தரவிட்டால் மட்டுமே இது எண்ணப்படும்.",
        why_a_en="Correct. Tendered vote is cast on a paper ballot and sealed under Rule 49P.",
        why_a_ta="சரியானது. காகித வாக்குச்சீட்டு மூலம் செலுத்தப்பட்டு சீலிடப்பட்ட உறையில் வைக்கப்படும்.",
        why_b_en="Incorrect. Duplicate voting cannot be cancelled on EVM.",
        why_b_ta="தவறானது. EVM-ல் ரத்து செய்ய முடியாது.",
        why_c_en="Incorrect. Oral voting is unknown to Indian law.",
        why_c_ta="தவறானது. வாய்மொழி வாக்கு செல்லாது.",
        why_d_en="Incorrect. The law explicitly protects the voter via the tendered ballot mechanism.",
        why_d_ta="தவறானது. சட்டம் அவர்களுக்கு ஒப்படைக்கப்பட்ட வாக்கு வசதியை வழங்குகிறது.",
        tip_en="Tendered votes are recorded in Form 17B (List of Tendered Votes).",
        tip_ta="ஒப்படைக்கப்பட்ட வாக்குகள் படிவம் 17B-ல் பதிவு செய்யப்படுகின்றன.",
        fact_en="If the victory margin in an election is less than the number of tendered votes, the High Court will open and inspect the tendered votes in an election petition.",
        fact_ta="வெற்றி வித்தியாசம் ஒப்படைக்கப்பட்ட வாக்குகளின் எண்ணிக்கையை விட குறைவாக இருந்தால், தேர்தல் வழக்கில் உயர் நீதிமன்றம் அவற்றை திறந்து எண்ணும்.",
        tags=["Rule 49P", "Tendered Votes", "Form 17B", "Impersonation"]
    ))

    # ER_H_023
    qs.append(make_er_q(
        qid="ER_H_023", diff="Hard", qtype="Single-Choice", subtopic="Challenged Votes",
        en_stem="Under Rule 49J (and Rule 36) of the Conduct of Elections Rules, 1961, what deposit amount must be paid in cash by a polling agent to challenge the identity of a person claiming to be a voter?",
        ta_stem="தேர்தல் நடத்தை விதிகள் 1961-ன் கீழ், ஒரு வாக்காளரின் அடையாளத்தை சந்தேகித்து ஆட்சேபனை செய்ய (Challenged Vote) ஒரு வாக்குச்சாவடி முகவர் தலைமை அலுவலரிடம் செலுத்த வேண்டிய ரொக்க வைப்புத்தொகை எவ்வளவு?",
        en_a="₹2", ta_a="₹2 (இரண்டு ரூபாய்)",
        en_b="₹100", ta_b="₹100 (நூறு ரூபாய்)",
        en_c="₹500", ta_c="₹500 (ஐந்நூறு ரூபாய்)",
        en_d="₹1,000", ta_d="₹1,000 (ஆயிரம் ரூபாய்)",
        correct_key="A",
        exp_en="Under Rule 36 and Rule 49J of the Conduct of Elections Rules, 1961, any polling agent may challenge the identity of a person claiming to be a particular elector by depositing a sum of ₹2 in cash with the Presiding Officer for each challenge. If the challenge is frivolous, the ₹2 is forfeited; if upheld, it is refunded and the impostor is handed to the police.",
        exp_ta="தேர்தல் நடத்தை விதிகள் 1961 விதி 36 மற்றும் 49J-ன் படி, ஒரு போலியான வாக்காளரின் அடையாளத்தை ஆட்சேபிக்க முகவர் தலைமை அலுவலரிடம் ₹2 ரொக்க வைப்புத்தொகை செலுத்த வேண்டும். ஆட்சேபனை பொய் எனில் ₹2 பறிமுதல் செய்யப்படும்; உண்மை எனில் பணம் திருப்பித் தரப்பட்டு போலி வாக்காளர் காவல்துறையிடம் ஒப்படைக்கப்படுவார்.",
        why_a_en="Correct. Exactly ₹2 under Rule 36(1).",
        why_a_ta="சரியானது. விதி 36(1)-ன் படி சரியாக ₹2.",
        why_b_en="Incorrect. ₹100 is incorrect.",
        why_b_ta="தவறானது. ₹100 தவறானது.",
        why_c_en="Incorrect. ₹500 is incorrect.",
        why_c_ta="தவறானது. ₹500 தவறானது.",
        why_d_en="Incorrect. ₹1,000 is incorrect.",
        why_d_ta="தவறானது. ₹1,000 தவறானது.",
        tip_en="This historical statutory amount of ₹2 has remained unamended since the 1961 rules were originally drafted!",
        tip_ta="1961-ல் விதிகள் உருவாக்கப்பட்ட போது நிர்ணயிக்கப்பட்ட இந்த ₹2 தொகை இன்றும் திருத்தப்படாமல் அப்படியே உள்ளது!",
        fact_en="Challenged votes are entered in Form 14 (List of Challenged Votes).",
        fact_ta="ஆட்சேபிக்கப்பட்ட வாக்குகள் படிவம் 14-ல் பதிவு செய்யப்படுகின்றன.",
        tags=["Challenged Votes", "₹2 Deposit", "Rule 36", "Form 14"]
    ))

    # ER_H_024
    qs.append(make_er_q(
        qid="ER_H_024", diff="Hard", qtype="Single-Choice", subtopic="Section 127A Election Pamphlets",
        en_stem="Under Section 127A of the Representation of the People Act, 1951, what mandatory requirement is imposed on the printing and publishing of election pamphlets, posters, and handbills?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 127A-ன் கீழ், தேர்தல் துண்டுப் பிரசுரங்கள், சுவரொட்டிகள் மற்றும் விளம்பரங்களை அச்சிட்டு வெளியிடுவதில் உள்ள கட்டாய விதிமுறை என்ன?",
        en_a="It must bear on its face the names and addresses of the printer and the publisher, and a signed declaration must be submitted to the District Magistrate", ta_a="அதில் அச்சிடுபவர் மற்றும் வெளியிடுபவரின் பெயர்கள் மற்றும் முகவரிகள் தெளிவாக இருக்க வேண்டும்; கையொப்பமிட்ட உறுதிமொழி மாவட்ட ஆட்சியரிடம் சமர்ப்பிக்கப்பட வேண்டும்",
        en_b="It must be printed exclusively on government-supplied bond paper certified by the ECI", ta_b="ECI-யால் சான்றளிக்கப்பட்ட அரசு வழங்கிய பிரத்யேக காகிதத்தில் மட்டுமே அச்சிடப்பட வேண்டும்",
        en_c="It must be translated into all 22 official languages listed in the 8th Schedule", ta_c="8-வது அட்டவணையில் உள்ள 22 அதிகாரப்பூர்வ மொழிகளிலும் மொழிபெயர்க்கப்பட வேண்டும்",
        en_d="It can only be distributed by registered speed post via the postal department", ta_d="தபால் துறை மூலம் விரைவுத் தபாலில் மட்டுமே விநியோகிக்கப்பட வேண்டும்",
        correct_key="A",
        exp_en="Section 127A of RPA 1951 imposes restrictions on the printing of election pamphlets and posters: (1) it must bear on its face the names and addresses of the printer and the publisher, and (2) the printer must obtain a signed declaration from the publisher and send a copy of the pamphlet and declaration to the District Magistrate / Chief Electoral Officer.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 127A, தேர்தல் துண்டுப் பிரசுரங்கள் மற்றும் சுவரொட்டிகளில் அச்சிட்டவர் மற்றும் வெளியிட்டவரின் பெயர் மற்றும் முழு முகவரி இடம்பெறுவதைக் கட்டாயமாக்குகிறது. மேலும் அச்சுப் பிரதியுடன் கூடிய உறுதிமொழி படிவத்தை மாவட்ட நடுவரிடம் (District Magistrate) அச்சுப்பொறி உரிமையாளர் சமர்ப்பிக்க வேண்டும்.",
        why_a_en="Correct. Mandatory printer and publisher name/address and declaration under Section 127A.",
        why_a_ta="சரியானது. அச்சிட்டவர் மற்றும் வெளியிட்டவர் பெயர், முகவரி மற்றும் உறுதிமொழி கட்டாயம் இருக்க வேண்டும்.",
        why_b_en="Incorrect. Any standard paper can be used.",
        why_b_ta="தவறானது. அரசு காகிதம் தேவையில்லை.",
        why_c_en="Incorrect. Translation into 22 languages is not required.",
        why_c_ta="தவறானது. 22 மொழிகளில் மொழிபெயர்க்க தேவையில்லை.",
        why_d_en="Incorrect. Any lawful physical distribution is permitted.",
        why_d_ta="தவறானது. தபால் மூலமாக மட்டுமே அனுப்ப வேண்டும் என்பதில்லை.",
        tip_en="Violation of Section 127A is punishable with imprisonment up to 6 months or fine up to ₹2,000 or both.",
        tip_ta="பிரிவு 127A-ஐ மீறினால் 6 மாதம் வரை சிறை அல்லது ₹2,000 அபராதம் விதிக்கப்படும்.",
        fact_en="This section prevents anonymous smear campaigns, fake pamphlets, and hate literature during elections.",
        fact_ta="தேர்தல் காலத்தில் யார் வெளியிட்டது எனத் தெரியாத அவதூறு துண்டுப் பிரசுரங்கள் பரப்பப்படுவதைத் தடுக்க இது பயன்படுகிறது.",
        tags=["Section 127A", "Election Pamphlets", "Printer Publisher Disclosure"]
    ))

    # ER_H_025
    qs.append(make_er_q(
        qid="ER_H_025", diff="Hard", qtype="Single-Choice", subtopic="Section 77 Election Expenses Timeline",
        en_stem="Under Section 77(1) of the Representation of the People Act, 1951, what is the exact legal duration for which a candidate is required to maintain a separate and correct account of all election expenses?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 77(1)-ன் கீழ், ஒரு வேட்பாளர் தனது அனைத்து தேர்தல் செலவுக் கணக்குகளையும் தனிப் பதிவேட்டில் துல்லியமாகப் பராமரிக்க வேண்டிய சட்டப்பூர்வ கால அளவு எது?",
        en_a="From the date on which the candidate was nominated to the date of declaration of the result thereof, both dates inclusive", ta_a="வேட்பாளர் வேட்புமனு தாக்கல் செய்த நாளிலிருந்து தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட நாள் வரை (இரு நாட்களும் உட்பட)",
        en_b="From the date of the announcement of the election schedule by ECI to the date of polling", ta_b="தேர்தல் ஆணையம் தேர்தல் தேதியை அறிவித்த நாளிலிருந்து வாக்குப்பதிவு நாள் வரை",
        en_c="For the entire calendar year in which the general election took place", ta_c="பொதுத்தேர்தல் நடைபெற்ற முழு காலண்டர் ஆண்டு முழுவதும்",
        en_d="From the date of scrutiny of nominations to the first sitting of the new Parliament", ta_d="வேட்புமனு பரிசீலனை நாளிலிருந்து புதிய நாடாளுமன்றத்தின் முதல் கூட்டத்தொடர் வரை",
        correct_key="A",
        exp_en="Section 77(1) of RPA 1951 explicitly mandates that every candidate shall keep a separate and correct account of all expenditure in connection with the election incurred or authorized by him or by his election agent between the date on which he has been NOMINATED and the date of DECLARATION of the result thereof, both dates inclusive.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 77(1), ஒரு வேட்பாளர் தான் வேட்புமனு தாக்கல் செய்த (Nomination) நாளிலிருந்து தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட (Declaration of result) நாள் வரையிலான (இரு நாட்களும் உட்பட) அனைத்து செலவுகளையும் துல்லியமாக பராமரிக்க வேண்டும் எனக் கட்டளையிடுகிறது.",
        why_a_en="Correct. From nomination date to result declaration date (both inclusive).",
        why_a_ta="சரியானது. வேட்புமனு தாக்கல் செய்த நாள் முதல் தேர்தல் முடிவு அறிவிக்கப்பட்ட நாள் வரை.",
        why_b_en="Incorrect. Expenditure incurred prior to nomination is not counted in the candidate's statutory account under Section 77.",
        why_b_ta="தவறானது. மனு தாக்கலுக்கு முந்தைய செலவுகள் வேட்பாளர் கணக்கில் சேர்க்கப்படுவதில்லை.",
        why_c_en="Incorrect. Not the entire calendar year.",
        why_c_ta="தவறானது. ஆண்டு முழுவதும் அல்ல.",
        why_d_en="Incorrect. Scrutiny date is too late; it starts from nomination.",
        why_d_ta="தவறானது. வேட்புமனு நாளிலிருந்தே கணக்கீடு தொடங்குகிறது.",
        tip_en="This is a frequent trick question in TNPSC: Candidates are NOT accountable under Section 77 for money spent before filing nomination papers!",
        tip_ta="இது TNPSC-ல் அடிக்கடி கேட்கப்படும் தந்திரமான கேள்வி: மனு தாக்கல் செய்வதற்கு முன் செய்யப்பட்ட செலவுகளுக்கு பிரிவு 77-ன் கீழ் கணக்கு காட்ட தேவையில்லை!",
        fact_en="Candidates must open a separate dedicated bank account at least one day before filing nominations exclusively for election transactions.",
        fact_ta="தேர்தல் செலவுகளுக்காகவே மனு தாக்கல் செய்வதற்கு குறைந்தது ஒரு நாளைக்கு முன் வேட்பாளர் தனி வங்கிக் கணக்கைத் தொடங்க வேண்டும்.",
        tags=["Section 77", "Election Expenditure Period", "Nomination to Result"]
    ))

    # ER_H_026
    qs.append(make_er_q(
        qid="ER_H_026", diff="Hard", qtype="Single-Choice", subtopic="Delimitation 84th and 87th Amendments",
        en_stem="Why did the 84th (2001) and 87th (2003) Constitutional Amendments maintain the freeze on the total allocation of Lok Sabha seats among states based on the 1971 census, while permitting internal boundary readjustment within states based on the 2001 census?",
        ta_stem="84-வது (2001) மற்றும் 87-வது (2003) அரசியலமைப்புத் திருத்தங்கள் மாநிலங்களுக்கு இடையேயான மக்களவை மொத்த இடங்களை 1971 கணக்கெடுப்பிலேயே முடக்கி வைத்துவிட்டு, மாநிலத்திற்குள் தொகுதிகளை மறுசீரமைக்க மட்டும் 2001 கணக்கெடுப்பை அனுமதித்தது ஏன்?",
        en_a="To avoid penalizing southern states that successfully implemented national family planning programs, while correcting population imbalances between constituencies within a state", ta_a="தேசிய குடும்பக் கட்டுப்பாடு திட்டங்களை சிறப்பாகச் செயல்படுத்திய தென் மாநிலங்கள் இடங்களை இழந்து தண்டிக்கப்படுவதைத் தடுக்கவும், அதே நேரம் மாநிலத்திற்குள் உள்ள தொகுதி மக்கள் தொகை சமநிலையின்மையை சரிசெய்யவும்",
        en_b="Because the Registrar General of India refused to release state-wise total population tables for southern states", ta_b="தென் மாநிலங்களுக்கான மக்கள்தொகை அட்டவணையை வெளியிட பதிவாளர் மறுத்ததால்",
        en_c="Because the Constitution prohibits changing Lok Sabha seat numbers under any circumstances", ta_c="எந்த சூழ்நிலையிலும் மக்களவை இடங்களின் எண்ணிக்கையை மாற்ற அரசியலமைப்பு தடை விதித்துள்ளதால்",
        en_d="Because EVMs could not accommodate more than 543 total parliamentary seats across the country", ta_d="நாடு முழுவதும் 543 இடங்களுக்கு மேல் EVM இயந்திரங்களால் கையாள முடியாது என்பதால்",
        correct_key="A",
        exp_en="If total Lok Sabha seats were reallocated based on current population, southern states (Tamil Nadu, Kerala, Karnataka, Andhra) with lower fertility rates would lose representation, while northern states with rapid population growth (UP, Bihar, MP) would gain massively, effectively penalizing states that controlled population. Hence, the total state-wise seat quota was frozen till 2026, while internal boundaries were equalized using the 2001 census.",
        exp_ta="மக்கள்தொகை அடிப்படையில் மொத்த இடங்களை மாற்றியமைத்தால், குடும்பக் கட்டுப்பாட்டை வெற்றிகரமாக அமல்படுத்திய தமிழ்நாடு, கேரளா உள்ளிட்ட தென் மாநிலங்களின் நாடாளுமன்ற பிரதிநிதித்துவம் குறையும்; மக்கள் தொகையைக் கட்டுப்படுத்தாத வட மாநிலங்கள் கூடுதல் இடங்களைப் பெறும். இந்த அநீதியைத் தவிர்க்கவே மாநிலங்களுக்கான மொத்த இடங்கள் 1971 கணக்கெடுப்பின்படி 2026 வரை முடக்கப்பட்டது.",
        why_a_en="Correct. Protects family planning performing states while addressing intra-state constituency distortions.",
        why_a_ta="சரியானது. குடும்பக் கட்டுப்பாட்டை அமல்படுத்திய மாநிலங்களைப் பாதுகாக்கவும், உள்-மாநில தொகுதி சமநிலையின்மையை நீக்கவும்.",
        why_b_en="Incorrect. Census data was fully published.",
        why_b_ta="தவறானது. மக்கள்தொகை தரவு வெளியிடப்பட்டது.",
        why_c_en="Incorrect. Parliament has amended seat allocations multiple times historically.",
        why_c_ta="தவறானது. நாடாளுமன்றத்திற்கு திருத்த அதிகாரம் உண்டு.",
        why_d_en="Incorrect. EVMs are used per polling station, not globally.",
        why_d_ta="தவறானது. EVM திறன் இதற்குக் காரணம் அல்ல.",
        tip_en="Article 82 governs readjustment of seats after each census; amended by 42nd, 84th, and 87th Amendments.",
        tip_ta="சரத்து 82 மக்கள் தொகை கணக்கெடுப்பிற்குப் பின் தொகுதி மறுசீரமைப்பைக் கையாள்கிறது; 42, 84 மற்றும் 87-வது திருத்தங்களால் திருத்தப்பட்டது.",
        fact_en="Tamil Nadu's Lok Sabha seats were reduced from 41 to 39 in the 1967 delimitation following the 1961 census, prior to the freeze.",
        fact_ta="தொகுதி முடக்கத்திற்கு முன், 1961 கணக்கெடுப்பைத் தொடர்ந்து 1967-ல் தமிழ்நாட்டின் மக்களவை இடங்கள் 41-லிருந்து 39 ஆகக் குறைக்கப்பட்டன.",
        tags=["Delimitation Freeze", "84th Amendment", "87th Amendment", "Family Planning Safeguard"]
    ))

    # ER_H_027
    qs.append(make_er_q(
        qid="ER_H_027", diff="Hard", qtype="Single-Choice", subtopic="Delimitation 2026 Controversy",
        en_stem="Under the proviso to Article 82 inserted by the 84th Amendment Act, 2001, after which specific event will the next freeze on the total number of seats in the Lok Sabha expire?",
        ta_stem="84-வது திருத்தச் சட்டம் 2001 மூலம் சரத்து 82-ல் சேர்க்கப்பட்ட வரம்புரையின்படி, எந்த குறிப்பிட்ட நிகழ்வுக்குப் பிறகு மக்களவை மொத்த இடங்களுக்கான தற்போதைய முடக்கம் காலாவதியாகும்?",
        en_a="Until the relevant figures for the first census taken after the year 2026 have been published", ta_a="2026 ஆம் ஆண்டுக்குப் பிறகு எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பின் புள்ளிவிவரங்கள் வெளியிடப்படும் வரை",
        en_b="On 31 December 2026 at midnight automatically", ta_b="2026 டிசம்பர் 31 நள்ளிரவில் தானாகவே",
        en_c="Immediately after the completion of the 2024 Lok Sabha elections", ta_c="2024 மக்களவைத் தேர்தல் முடிந்த உடனேயே",
        en_d="When the Supreme Court issues a writ directing a new delimitation commission", ta_d="புதிய மறுவரையறை ஆணையத்தை அமைக்க உச்ச நீதிமன்றம் உத்தரவிடும் போது",
        correct_key="A",
        exp_en="The proviso to Article 82 explicitly states: 'Provided that until the relevant figures for the first census taken after the year 2026 have been published, it shall not be necessary to readjust the allocation of seats in the House of the People to the States'. Thus, the freeze does not expire on 31 Dec 2026, but only when the census taken AFTER 2026 is officially published.",
        exp_ta="சரத்து 82-ன் வரம்புரை, '2026 ஆம் ஆண்டிற்குப் பிறகு எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பின் தொடர்புடைய புள்ளிவிவரங்கள் வெளியிடப்படும் வரை' மாநிலங்களுக்கான மக்களவை இடங்களை மறுசீரமைக்க வேண்டிய அவசியமில்லை என்று கூறுகிறது. எனவே 2026-க்குப் பிந்தைய கணக்கெடுப்பு வெளியாகும் வரை முடக்கம் நீடிக்கும்.",
        why_a_en="Correct. Publication of figures of the first census taken AFTER the year 2026.",
        why_a_ta="சரியானது. 2026-க்குப் பிறகு எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பு வெளியாகும் வரை.",
        why_b_en="Incorrect. It does not expire on a fixed calendar date in 2026.",
        why_b_ta="தவறானது. 2026 டிசம்பர் 31 அன்று தானாக காலாவதியாகாது.",
        why_c_en="Incorrect. The freeze remains fully operational through 2024.",
        why_c_ta="தவறானது. 2024 தேர்தலிலும் முடக்கம் அமலில் இருந்தது.",
        why_d_en="Incorrect. Supreme Court cannot issue a writ overriding the constitutional proviso.",
        why_d_ta="தவறானது. அரசியலமைப்பு வரம்பை மீறி நீதிமன்றம் உத்தரவிட முடியாது.",
        tip_en="If the census is conducted in 2027 or 2031, the readjustment will take place only based on that census data.",
        tip_ta="2027 அல்லது 2031-ல் கணக்கெடுப்பு நடத்தப்பட்டால், அந்தத் தரவுகள் வெளியான பிறகே மறுவரையறை சாத்தியமாகும்.",
        fact_en="The new Parliament building's Lok Sabha chamber has been built with 888 seats to accommodate future expansion after delimitation.",
        fact_ta="புதிய நாடாளுமன்ற மக்களவை அரங்கம் எதிர்கால மறுவரையறை விரிவாக்கத்தைக் கருதி 888 இருக்கைகளுடன் கட்டப்பட்டுள்ளது.",
        tags=["Article 82 Proviso", "Delimitation 2026", "Census Trigger"]
    ))

    # ER_H_028
    qs.append(make_er_q(
        qid="ER_H_028", diff="Hard", qtype="Single-Choice", subtopic="106th Amendment Ratification",
        en_stem="Why did the 106th Constitutional Amendment Act, 2023 (Women's Reservation) NOT require ratification by at least half of the State Legislatures under the proviso to Article 368(2)?",
        ta_stem="106-வது அரசியலமைப்புச் சட்டத்திருத்தம் 2023 (மகளிர் இடஒதுக்கீடு), சரத்து 368(2)-ன் வரம்புரையின் கீழ் குறைந்தபட்சம் பாதி மாநில சட்டமன்றங்களின் ஒப்புதலைப் (Ratification) பெற வேண்டிய அவசியமில்லாமல் போனது ஏன்?",
        en_a="Because it did not amend any of the entrenched provisions listed in the proviso to Article 368(2) (such as representation of states in Parliament or Chapter III of Part VI)", ta_a="சரத்து 368(2) வரம்புரையில் குறிப்பிடப்பட்டுள்ள உட்பிரிவுகளை (நாடாளுமன்றத்தில் மாநிலங்களின் பிரதிநிதித்துவம் அல்லது பகுதி VI அத்தியாயம் III போன்றவை) அது திருத்தவில்லை என்பதால்",
        en_b="Because it was passed by a 100% unanimous vote in both Houses of Parliament", ta_b="நாடாளுமன்றத்தின் இரு அவைகளிலும் 100% ஒருமனதாக நிறைவேற்றப்பட்டதால்",
        en_c="Because women constitute half of the population and are exempt from constitutional amendment procedures", ta_c="பெண்கள் மக்கள்தொகையில் பாதி என்பதால் திருத்த நடைமுறையிலிருந்து விலக்கு உண்டு என்பதால்",
        en_d="Because the President issued an emergency ordinance suspending state ratification", ta_d="குடியரசுத் தலைவர் அவசரச் சட்டம் மூலம் மாநில ஒப்புதலை நிறுத்தி வைத்ததால்",
        correct_key="A",
        exp_en="Article 368(2) proviso specifies entrenched provisions requiring ratification by half of the states: election of President (Arts 54, 55), executive powers of Union/States (Arts 73, 162), Supreme Court/High Courts (Part V Ch IV, Part VI Ch V), 7th Schedule lists, and representation of States in Parliament (meaning Rajya Sabha). Since the 106th Amendment inserted Articles 330A and 332A in Part XVI (Special Provisions Relating to Certain Classes) and Article 239AA, state ratification was legally not required.",
        exp_ta="சரத்து 368(2)-ன் வரம்புரையின் கீழ் குடியரசுத் தலைவர் தேர்தல், 7-வது அட்டவணை, உச்ச/உயர் நீதிமன்றங்கள் மற்றும் நாடாளுமன்றத்தில் மாநிலங்களின் பிரதிநிதித்துவம் (மாநிலங்களவை இடங்கள்) ஆகியவற்றை திருத்தினால் மட்டுமே மாநில சட்டமன்றங்களின் ஒப்புதல் தேவை. 106-வது திருத்தம் பகுதி XVI-ல் சரத்து 330A, 332A ஆகியவற்றை மட்டுமே இணைத்ததால் மாநிலங்களின் ஒப்புதல் சட்டப்படி தேவைப்படவில்லை.",
        why_a_en="Correct. Did not amend entrenched articles listed in Article 368(2) proviso.",
        why_a_ta="சரியானது. சரத்து 368(2) வரம்புரையில் உள்ள சிறப்புப் பிரிவுகளை அது திருத்தவில்லை.",
        why_b_en="Incorrect. Voting margin does not alter the requirement of state ratification.",
        why_b_ta="தவறானது. ஒருமனதாக நிறைவேற்றப்பட்டாலும் சட்ட விதியை மாற்ற முடியாது.",
        why_c_en="Incorrect. Gender demographics do not alter Article 368 procedure.",
        why_c_ta="தவறானது. மக்கள்தொகை சதவீதம் திருத்த நடைமுறையை மாற்றாது.",
        why_d_en="Incorrect. Ordinances cannot suspend constitutional amendment procedures.",
        why_d_ta="தவறானது. அவசரச் சட்டத்தால் அரசியலமைப்பு நடைமுறையை மாற்ற முடியாது.",
        tip_en="In contrast, the Kovind Committee's proposal for a Single Electoral Roll WILL require state ratification because local bodies fall under State List (List II Entry 5).",
        tip_ta="இதற்கு மாறாக, ஒரே வாக்காளர் பட்டியல் திட்டத்திற்கு மாநிலங்களின் ஒப்புதல் கட்டாயம் தேவைப்படும்; ஏனெனில் உள்ளாட்சி அமைப்புகள் மாநிலப் பட்டியலில் உள்ளன.",
        fact_en="The 106th Amendment was passed with only 2 dissenting votes in Lok Sabha and unanimously (0 dissenting) in Rajya Sabha.",
        fact_ta="மக்களவையில் 2 எதிர்ப்புகளுடன், மாநிலங்களவையில் எதிர்ப்பின்றி ஒருமனதாக 106-வது திருத்தம் நிறைவேறியது.",
        tags=["106th Amendment", "Article 368 Ratification", "Constitutional Procedure"]
    ))

    # ER_H_029
    qs.append(make_er_q(
        qid="ER_H_029", diff="Hard", qtype="Single-Choice", subtopic="Simultaneous Elections Kovind Recommendations",
        en_stem="Which constitutional provision was recommended by the Kovind Committee (2024) to be inserted to introduce the 'Appointed Date' concept for synchronizing Lok Sabha and State Assembly tenures?",
        ta_stem="மக்களவை மற்றும் மாநில சட்டமன்றங்களின் பதவிக்காலங்களை ஒருங்கிணைக்க 'நியமிக்கப்பட்ட தேதி' (Appointed Date) என்ற கருத்தை அறிமுகப்படுத்த கோவிந்த் குழு (2024) பரிந்துரைத்த புதிய அரசியலமைப்புச் சரத்து எது?",
        en_a="Article 82A", ta_a="சரத்து 82A",
        en_b="Article 324A", ta_b="சரத்து 324A",
        en_c="Article 83A", ta_c="சரத்து 83A",
        en_d="Article 172A", ta_d="சரத்து 172A",
        correct_key="A",
        exp_en="The Kovind High-Level Committee recommended inserting Article 82A, under which the President, on the date of the first sitting of the Lok Sabha after a general election, shall issue a notification bringing the Article into force ('Appointed Date'). All State Legislative Assemblies constituted thereafter will automatically dissolve alongside the Lok Sabha at the end of its 5-year term.",
        exp_ta="கோவிந்த் உயர்நிலைக் குழு புதிய சரத்து 82A-ஐ இணைக்க பரிந்துரைத்தது. இதன் கீழ், பொதுத்தேர்தலுக்குப் பின் மக்களவையின் முதல் கூட்டம் கூடும் நாளில் குடியரசுத் தலைவர் ஓர் அறிவிக்கையை வெளியிட்டு அதை 'நியமிக்கப்பட்ட தேதி' (Appointed Date) என அறிவிப்பார். அதன் பிறகு தேர்ந்தெடுக்கப்படும் அனைத்து மாநில சட்டமன்றங்களும் மக்களவையின் 5 ஆண்டு பதவிக்காலம் முடியும் போதே தானாக கலைக்கப்படும்.",
        why_a_en="Correct. Article 82A introduces the Appointed Date mechanism.",
        why_a_ta="சரியானது. சரத்து 82A நியமிக்கப்பட்ட தேதி பொறிமுறையை அறிமுகப்படுத்துகிறது.",
        why_b_en="Incorrect. Article 324A was recommended for Municipalities and Panchayats elections within 100 days.",
        why_b_ta="தவறானது. சரத்து 324A என்பது 100 நாட்களுக்குள் உள்ளாட்சித் தேர்தல் நடத்துவதற்கானது.",
        why_c_en="Incorrect. Article 83 deals with duration of Houses.",
        why_c_ta="தவறானது. சரத்து 83 நாடாளுமன்ற அவைகளின் பதவிக்காலம் பற்றியது.",
        why_d_en="Incorrect. Article 172 deals with duration of State Legislatures.",
        why_d_ta="தவறானது. சரத்து 172 சட்டமன்றங்களின் பதவிக்காலம் பற்றியது.",
        tip_en="Article 82A does NOT require ratification by states because it does not affect federal legislative powers under Article 368(2).",
        tip_ta="சரத்து 82A-க்கு மாநில சட்டமன்றங்களின் ஒப்புதல் தேவையில்லை என கோவிந்த் குழு குறிப்பிட்டது.",
        fact_en="Article 82A(2) provides that any state assembly constituted after the Appointed Date will serve only until the full term of the Lok Sabha.",
        fact_ta="சரத்து 82A(2)-ன் படி நியமிக்கப்பட்ட தேதிக்கு பின் தேர்ந்தெடுக்கப்படும் சட்டமன்றங்கள் மக்களவையின் எஞ்சிய காலம் வரை மட்டுமே செயல்படும்.",
        tags=["Article 82A", "Appointed Date", "Kovind Committee 2024", "Simultaneous Elections"]
    ))

    # ER_H_030
    qs.append(make_er_q(
        qid="ER_H_030", diff="Hard", qtype="Single-Choice", subtopic="Simultaneous Elections Unexpired Term",
        en_stem="Under the constitutional framework recommended by the Kovind Committee (2024), what happens if a State Legislative Assembly is dissolved prematurely due to a no-confidence motion or hung assembly?",
        ta_stem="கோவிந்த் குழு (2024) பரிந்துரைத்த அரசியலமைப்பு கட்டமைப்பின் கீழ், நம்பிக்கையில்லாத் தீர்மானம் அல்லது தொங்கு சட்டமன்றம் காரணமாக ஒரு மாநில சட்டமன்றம் முன்கூட்டியே கலைக்கப்பட்டால் என்ன நிகழும்?",
        en_a="Fresh elections will be held only for the remainder of the unexpired term of the original House ('Unexpired Term')", ta_a="முதன்மை அவையின் எஞ்சிய காலத்திற்கு மட்டுமே புதிய தேர்தல் நடத்தப்பட்டு புதிய சட்டமன்றம் செயல்படும் ('எஞ்சிய காலம்')",
        en_b="Fresh elections will immediately grant the newly elected assembly a full 5-year fresh term", ta_b="புதிதாக தேர்ந்தெடுக்கப்படும் சட்டமன்றத்திற்கு உடனடியாக முழுமையான 5 ஆண்டுகள் புதிய பதவிக்காலம் வழங்கப்படும்",
        en_c="President's rule is permanently imposed on that state until the next national census", ta_c="அடுத்த தேசிய மக்கள் தொகை கணக்கெடுப்பு வரை அந்த மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி நிரந்தரமாக நீடிக்கும்",
        en_d="The State is automatically merged into an adjoining Union Territory", ta_d="அம்மாநிலம் தானாகவே அருகில் உள்ள யூனியன் பிரதேசத்துடன் இணைக்கப்படும்",
        correct_key="A",
        exp_en="To maintain synchronization without breaking the simultaneous election cycle, the Kovind Committee recommended amending Article 83 and Article 172 to provide that if Parliament or a State Assembly dissolves mid-term, fresh elections will be held only for the 'unexpired term' (remainder of the original 5-year period) until the next synchronized general election.",
        exp_ta="ஒரே நேர தேர்தல் சுழற்சி பாதிக்கப்படாமல் இருக்க, சரத்து 83 மற்றும் 172-ஐத் திருத்தி, இடையில் ஆட்சி கவிழ்ந்து முன்கூட்டியே கலைக்கப்பட்டால், அடுத்த பொதுத்தேர்தல் வரையிலான எஞ்சிய காலத்திற்கு (Unexpired Term) மட்டுமே புதிய சட்டமன்றம் தேர்ந்தெடுக்கப்படும் என கோவிந்த் குழு பரிந்துரைத்தது.",
        why_a_en="Correct. Serves only for the remainder of the unexpired term to protect cycle alignment.",
        why_a_ta="சரியானது. தேர்தல் சுழற்சியைப் பாதுகாக்க எஞ்சிய காலத்திற்கு மட்டுமே புதிய அவை நீடிக்கும்.",
        why_b_en="Incorrect. Granting a full 5 years would permanently de-synchronize the election cycle.",
        why_b_ta="தவறானது. முழு 5 ஆண்டுகள் வழங்கினால் தேர்தல் ஒருங்கிணைப்பு சீர்குலைந்துவிடும்.",
        why_c_en="Incorrect. Democratic elections must be held, not permanent President's rule.",
        why_c_ta="தவறானது. நிரந்தர குடியரசுத் தலைவர் ஆட்சி ஜனநாயகத்திற்கு எதிரானது.",
        why_d_en="Incorrect. States cannot be dissolved into UTs for this reason.",
        why_d_ta="தவறானது. மாநிலங்களை இணைக்க முடியாது.",
        tip_en="This mechanism is modeled on municipal bodies and panchayats under Article 243E(4) and 243U(4), where mid-term dissolved bodies serve only the remainder of the term.",
        tip_ta="இம்முறை சரத்து 243E(4) மற்றும் 243U(4)-ன் கீழான நகராட்சி மற்றும் பஞ்சாயத்துகளின் இடைக்கால தேர்தல் முறையை அடிப்படையாகக் கொண்டது.",
        fact_en="This was also previously recommended by the 170th Law Commission Report in 1999.",
        fact_ta="1999-ல் 170-வது சட்ட ஆணைய அறிக்கையும் இதே 'எஞ்சிய கால' முறையை பரிந்துரைத்திருந்தது.",
        tags=["Unexpired Term", "Article 172 Amendment", "Kovind Committee", "Hung Assembly Solution"]
    ))

    # ER_H_031
    qs.append(make_er_q(
        qid="ER_H_031", diff="Hard", qtype="Single-Choice", subtopic="CEC Appointment Act Protection",
        en_stem="Under Section 15 of the Chief Election Commissioner and other Election Commissioners Act, 2023, what special legal protection was granted to the CEC and ECs against judicial proceedings?",
        ta_stem="தலைமைத் தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்கள் சட்டம், 2023 பிரிவு 15-ன் கீழ், நீதிமன்ற நடவடிக்கைகளுக்கு எதிராக CEC மற்றும் EC-களுக்கு வழங்கப்பட்டுள்ள சிறப்பு சட்டப் பாதுகாப்பு என்ன?",
        en_a="No court shall entertain or continue any civil or criminal proceedings against any serving or former CEC or EC for any act, thing or word said in the discharge of official duty", ta_a="அலுவல் ரீதியான கடமைகளைச் செய்வதில் செய்த எந்தவொரு செயலுக்காகவும் தற்போதைய அல்லது முன்னாள் CEC அல்லது EC மீது எந்த நீதிமன்றமும் உரிமையியல் அல்லது குற்றவியல் வழக்குகளைத் தொடரவோ விசாரிக்கவோ கூடாது",
        en_b="They are permanently exempt from paying Indian income taxes on all personal property", ta_b="அவர்களது தனிப்பட்ட சொத்துக்கள் மீதான வருமான வரிகளை செலுத்துவதிலிருந்து நிரந்தர விலக்கு",
        en_c="They can never be questioned by any parliamentary standing committee under any circumstances", ta_c="எந்தவொரு சூழ்நிலையிலும் நாடாளுமன்ற நிலைக்குழுக்களால் அவர்களை விசாரிக்கவே முடியாது",
        en_d="They enjoy diplomatic immunity under the Geneva Convention within Indian territory", ta_d="இந்திய எல்லைக்குள் ஜெனிவா உடன்படிக்கையின் கீழான தூதரகப் பாதுகாப்பைப் பெறுகின்றனர்",
        correct_key="A",
        exp_en="Section 15 of the 2023 Act provides comprehensive immunity to the Chief Election Commissioner and other Election Commissioners: no court shall entertain or continue any civil or criminal proceedings against them for any act, thing, or word done, said, or omitted to be done in the discharge of their official functions or duty.",
        exp_ta="2023 சட்டத்தின் பிரிவு 15, தேர்தல் ஆணையர்களுக்கு விரிவான சட்டப் பாதுகாப்பை வழங்குகிறது: தங்களது அலுவல்சார் கடமைகளைச் செய்வதில் செய்த அல்லது பேசிய எதற்காகவும் தற்போதைய அல்லது முன்னாள் தலைமைத் தேர்தல் ஆணையர் மற்றும் தேர்தல் ஆணையர்கள் மீது எந்த நீதிமன்றமும் சிவில் அல்லது குற்றவியல் வழக்குகளை விசாரிக்கக் கூடாது.",
        why_a_en="Correct. Complete protection from civil and criminal proceedings for official actions.",
        why_a_ta="சரியானது. அலுவல் ரீதியான செயல்களுக்கு சிவில் மற்றும் குற்றவியல் வழக்குகளிலிருந்து முழுமையான பாதுகாப்பு.",
        why_b_en="Incorrect. Commissioners pay income tax like all citizens.",
        why_b_ta="தவறானது. வரிவிலக்கு எதுவும் இல்லை.",
        why_c_en="Incorrect. Parliamentary accountability is maintained.",
        why_c_ta="தவறானது. நாடாளுமன்றப் பொறுப்புக்கூறல் உண்டு.",
        why_d_en="Incorrect. Geneva Convention applies to foreign diplomats, not domestic officials.",
        why_d_ta="தவறானது. ஜெனிவா உடன்படிக்கை வெளிநாட்டு தூதர்களுக்கானது.",
        tip_en="This clause was inserted to shield commissioners from vexatious litigation and intimidation by disgruntled politicians after leaving office.",
        tip_ta="பதவி முடிந்த பிறகு அதிருப்தியடைந்த அரசியல்வாதிகள் பழிவாங்கும் நோக்கில் வழக்குகள் தொடுப்பதைத் தடுக்க இப்பிரிவு சேர்க்கப்பட்டது.",
        fact_en="Similar protections exist for Supreme Court Judges under the Judges (Protection) Act, 1985.",
        fact_ta="1985 நீதிபதிகள் பாதுகாப்புச் சட்டத்தின் கீழ் உச்ச நீதிமன்ற நீதிபதிகளுக்கும் இதேபோன்ற பாதுகாப்பு உள்ளது.",
        tags=["Section 15", "CEC Act 2023", "Judicial Immunity", "Official Duty Protection"]
    ))

    # ER_H_032
    qs.append(make_er_q(
        qid="ER_H_032", diff="Hard", qtype="Single-Choice", subtopic="Section 29C Income Tax Interplay",
        en_stem="What happens to the 100% income tax exemption enjoyed by a registered political party under Section 13A of the Income Tax Act if it fails to submit its contribution report to the ECI within the prescribed deadline?",
        ta_stem="அரசியல் கட்சிகள் நிர்ணயிக்கப்பட்ட காலக்கெடுவிற்குள் தங்கள் நன்கொடை அறிக்கையை (Contribution Report) ECI-யிடம் சமர்ப்பிக்கத் தவறினால், வருமான வரிச் சட்டம் பிரிவு 13A-ன் கீழ் அவை அனுபவிக்கும் 100% வருமான வரி விலக்கிற்கு என்ன நேரிடும்?",
        en_a="The party completely forfeits its tax exemption for that financial year and must pay full income tax on its entire income", ta_a="அந்த நிதியாண்டிற்கான வரிவிலக்கு சலுகையை கட்சி முழுமையாக இழந்து, தனது மொத்த வருமானத்திற்கும் முழு வருமான வரியை செலுத்த வேண்டும்",
        en_b="The ECI imposes a mandatory 1% nominal administrative penalty and waives the default", ta_b="தேர்தல் ஆணையம் 1% பெயரளவு அபராதம் விதித்து தவறை மன்னித்துவிடும்",
        en_c="The party treasurer is automatically sentenced to 7 years rigorous imprisonment by CBDT", ta_c="கட்சியின் பொருளாளருக்கு CBDT மூலம் தானாக 7 ஆண்டுகள் சிறைத்தண்டனை விதிக்கப்படும்",
        en_d="The income tax exemption is permanently revoked for the next 25 financial years", ta_d="அடுத்த 25 நிதியாண்டுகளுக்கு வருமான வரி விலக்கு நிரந்தரமாக ரத்து செய்யப்படும்",
        correct_key="A",
        exp_en="Under the third proviso to Section 13A of the Income Tax Act, 1961 (inserted in 2003), a political party is entitled to tax exemption on voluntary contributions ONLY IF it submits its Section 29C contribution report to the ECI on or before the due date for filing its income tax return under Section 139(4B). Failure to do so results in complete loss of tax exemption for that assessment year.",
        exp_ta="வருமான வரிச் சட்டம் பிரிவு 13A-ன் 3-வது வரம்புரையின்படி, வருமான வரி தாக்கல் செய்யும் தேதிக்குள் பிரிவு 29C நன்கொடை அறிக்கையை ECI-யிடம் சமர்ப்பித்தால் மட்டுமே கட்சிகளுக்கு வரிவிலக்கு கிடைக்கும். தவறினால், அந்த மதிப்பீட்டு ஆண்டிற்கான முழு வரிவிலக்கும் ரத்தாகி, மொத்த வருமானத்திற்கும் கட்சி வரி செலுத்த வேண்டும்.",
        why_a_en="Correct. 100% forfeiture of tax exemption for that assessment year under Section 13A.",
        why_a_ta="சரியானது. அந்த ஆண்டிற்கான முழு வரிவிலக்கும் பறிபோகும்.",
        why_b_en="Incorrect. ECI has no statutory power to condone default or waive tax penalties.",
        why_b_ta="தவறானது. ECI-க்கு வரிவிலக்கு அபராதத்தை ரத்து செய்ய அதிகாரம் இல்லை.",
        why_c_en="Incorrect. CBDT cannot sentence treasurers to prison directly.",
        why_c_ta="தவறானது. CBDT நேரடியாக சிறைத்தண்டனை விதிக்க முடியாது.",
        why_d_en="Incorrect. The penalty is year-specific, not a 25-year ban.",
        why_d_ta="தவறானது. அந்த குறிப்பிட்ட நிதியாண்டிற்கு மட்டுமே பொருந்தும்.",
        tip_en="In 2017, the Supreme Court in Common Cause reaffirmed that strict adherence to Section 13A and Section 29C deadlines is mandatory for claiming political tax benefits.",
        tip_ta="காமன் காஸ் வழக்கில் உச்ச நீதிமன்றம் இக்காலக்கெடுவை கண்டிப்புடன் பின்பற்ற வேண்டும் என உறுதி செய்தது.",
        fact_en="Parties must also get their accounts audited by a qualified Chartered Accountant under Section 13A(b).",
        fact_ta="கணக்குகளை பட்டயக் கணக்காளர் (CA) மூலம் தணிக்கை செய்வதும் வரிவிலக்கிற்கு கட்டாய நிபந்தனையாகும்.",
        tags=["Section 13A Income Tax", "Section 29C RPA", "Loss of Tax Exemption"]
    ))

    # ER_H_033
    qs.append(make_er_q(
        qid="ER_H_033", diff="Hard", qtype="Single-Choice", subtopic="Law Commission 255th Report on Paid News",
        en_stem="Which specific legal reform did the 255th Law Commission Report (2015) propose to tackle the menace of 'Paid News' effectively?",
        ta_stem="'ஊதியச் செய்தி' (Paid News) முறைகேட்டை திறம்பட சமாளிக்க 255-வது சட்ட ஆணைய அறிக்கை (2015) முன்மொழிந்த குறிப்பிட்ட சட்டச் சீர்திருத்தம் எது?",
        en_a="Inserting Section 127B in RPA 1951 to define Paid News as an electoral offence punishable with imprisonment, and inserting Section 123(9) as a corrupt practice", ta_a="பிரிவு 127B-ஐ இணைத்து ஊதியச் செய்தியை சிறைத்தண்டனைக்குரிய தேர்தல் குற்றமாகவும், பிரிவு 123(9)-ன் கீழ் ஊழல் நடைமுறையாகவும் அறிவிப்பது",
        en_b="Nationalizing all private television channels and print newspapers during elections", ta_b="தேர்தல் காலத்தில் அனைத்து தனியார் தொலைக்காட்சிகளையும் செய்தித்தாள்களையும் அரசுடைமையாக்குவது",
        en_c="Permanently shutting down internet access across the entire state on polling days", ta_c="வாக்குப்பதிவு நாளன்று மாநிலம் முழுவதும் இணைய சேவையை நிரந்தரமாக முடக்குவது",
        en_d="Banning journalists from interviewing politicians without prior police permission", ta_d="காவல்துறை அனுமதியின்றி பத்திரிகையாளர்கள் அரசியல்வாதிகளை பேட்டி காண தடை விதிப்பது",
        correct_key="A",
        exp_en="The 255th Law Commission Report (2015) recommended: (1) inserting Section 127B into RPA 1951 to make paying or receiving consideration for news/analysis an electoral offence punishable with imprisonment up to 2 years, (2) adding Paid News as a corrupt practice under Section 123, and (3) disqualification under Section 8A for candidates indulging in paid news.",
        exp_ta="255-வது சட்ட ஆணைய அறிக்கை (2015), ஊதியச் செய்திக்காக பணம் கொடுப்பது அல்லது பெறுவதை 2 ஆண்டுகள் சிறைத் தண்டனைக்குரிய தேர்தல் குற்றமாக அறிவிக்க பிரிவு 127B-ஐ சேர்க்கவும், அதை பிரிவு 123-ன் கீழ் ஊழல் நடைமுறையாக்கவும் பரிந்துரைத்தது.",
        why_a_en="Correct. Creation of statutory offence Section 127B and corrupt practice Section 123(9).",
        why_a_ta="சரியானது. பிரிவு 127B குற்றவியல் பிரிவையும், பிரிவு 123(9) ஊழல் நடைமுறையையும் உருவாக்குதல்.",
        why_b_en="Incorrect. Nationalizing media is completely unconstitutional under Article 19(1)(a).",
        why_b_ta="தவறானது. ஊடகங்களை அரசுடைமையாக்குவது பேச்சு சுதந்திரத்திற்கு எதிரானது.",
        why_c_en="Incorrect. Internet shutdown was rejected as disproportionate.",
        why_c_ta="தவறானது. இணைய முடக்கம் பரிந்துரைக்கப்படவில்லை.",
        why_d_en="Incorrect. Police permission for press interviews is authoritarian and illegal.",
        why_d_ta="தவறானது. பத்திரிகை சுதந்திரத்திற்கு எதிரானது.",
        tip_en="Currently, Paid News is not a direct statutory offence under RPA 1951; ECI handles it indirectly by adding the deemed cost of the advertisement to the candidate's election expenditure account under Section 77/10A.",
        tip_ta="தற்போது ஊதியச் செய்தி சட்டப்பூர்வ குற்றமாக இல்லை; ECI அதை விளம்பரச் செலவாகக் கருதி வேட்பாளரின் கணக்கில் சேர்க்கிறது.",
        fact_en="In Umlesh Yadav v. ECI (2011), the first ever disqualification for paid news was imposed on an MLA under Section 10A for failing to disclose the expenditure.",
        fact_ta="2011-ல் உம்லேஷ் யாதவ் என்ற எம்.எல்.ஏ ஊதியச் செய்தி செலவை மறைத்ததற்காக பிரிவு 10A-ன் கீழ் 3 ஆண்டுகள் தகுதிநீக்கம் செய்யப்பட்டார்.",
        tags=["Paid News Reform", "255th Law Commission", "Section 127B Proposal"]
    ))

    # ER_H_034
    qs.append(make_er_q(
        qid="ER_H_034", diff="Hard", qtype="Single-Choice", subtopic="Section 123(2) Undue Influence",
        en_stem="In the context of Section 123(2) of the Representation of the People Act, 1951 (Undue Influence), which of the following actions constitutes an illegal interference with the free exercise of electoral rights?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 123(2)-ன் (தவறான செல்வாக்கு - Undue Influence) கீழ், வாக்காளரின் சுதந்திரமான தேர்தல் உரிமையில் சட்டவிரோதமாக தலையிடும் செயலாக எது கருதப்படுகிறது?",
        en_a="Threatening an elector with injury of any kind, social ostracism, expulsion from any caste/community, or spiritual censure / divine displeasure", ta_a="வாக்காளரை அச்சுறுத்துவது, சமூக புறக்கணிப்பு, ஜாதி/சமூகத்திலிருந்து விலக்கி வைப்பது, அல்லது மத சாபம் / கடவுளின் கோபத்திற்கு ஆளாவாய் என்று மிரட்டுவது",
        en_b="Promising to build roads, bridges, and infrastructure in the constituency if elected", ta_b="தேர்ந்தெடுக்கப்பட்டால் தொகுதியில் சாலைகள், பாலங்கள் மற்றும் உள்கட்டமைப்புகளை உருவாக்குவதாக வாக்குறுதி அளிப்பது",
        en_c="Publishing comparative statistical data analyzing inflation rates under different governments", ta_c="பல்வேறு அரசுகளின் கீழான பணவீக்க விகிதங்களை ஒப்பிடும் புள்ளிவிவரங்களை வெளியிடுவது",
        en_d="Holding peaceful door-to-door visits to explain party manifesto promises", ta_d="கட்சியின் தேர்தல் வாக்குறுதிகளை விளக்க அமைதியான முறையில் வீடு வீடாகச் சென்று சந்திப்பது",
        correct_key="A",
        exp_en="Under the proviso to Section 123(2) of RPA 1951, declaring that an elector or candidate will become an object of divine displeasure or spiritual censure, or threatening social ostracism, expulsion from caste or community, or physical injury constitutes 'Undue Influence', which is a corrupt practice voiding the election.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 123(2) வரம்புரையின்படி, ஒரு குறிப்பிட்ட வேட்பாளருக்கு வாக்களிக்காவிட்டால் கடவுளின் கோபத்திற்கு ஆளாவாய் என அச்சுறுத்துவது, மத சாபம் இடுவது, சமூக புறக்கணிப்பு அல்லது ஜாதி நீக்கம் செய்வதாக மிரட்டுவது 'தவறான செல்வாக்கு' (Undue Influence) என்ற ஊழல் நடைமுறையாகும்.",
        why_a_en="Correct. Threat of divine displeasure or social ostracism is undue influence under Section 123(2).",
        why_a_ta="சரியானது. தெய்வ குற்றம் சாட்டுதல் அல்லது சமூக புறக்கணிப்பு அச்சுறுத்தல் பிரிவு 123(2)-ன் கீழ் தவறான செல்வாக்காகும்.",
        why_b_en="Incorrect. Declaration of public policy or promise of public action is explicitly protected under proviso (b) to Section 123(2).",
        why_b_ta="தவறானது. பொதுக்கொள்கை அல்லது திட்டங்களை வாக்குறுதியாக அளிப்பது தவறான செல்வாக்கு அல்ல (விலக்கு உண்டு).",
        why_c_en="Incorrect. Economic critique is legitimate campaigning.",
        why_c_ta="தவறானது. பொருளாதார விமர்சனம் ஜனநாயக உரிமை.",
        why_d_en="Incorrect. Door-to-door canvassing is completely lawful.",
        why_d_ta="தவறானது. வீடு வீடாக வாக்கு சேகரிப்பது சட்டப்பூர்வமானது.",
        tip_en="Proviso (b) to Section 123(2) explicitly protects a declaration of public policy or a promise of public action from being treated as undue influence.",
        tip_ta="பிரிவு 123(2) வரம்புரை (b) பொதுக்கொள்கை அல்லது திட்ட வாக்குறுதிகள் தவறான செல்வாக்காகக் கருதப்படாது எனத் தெளிவுபடுத்துகிறது.",
        fact_en="Appealing to religious threats violates both Section 123(2) (Undue Influence) and Section 123(3) (Religious appeal).",
        fact_ta="மத அச்சுறுத்தல்களை விடுப்பது பிரிவு 123(2) மற்றும் பிரிவு 123(3) ஆகிய இரண்டையுமே மீறுவதாகும்.",
        tags=["Section 123(2)", "Undue Influence", "Divine Displeasure", "Corrupt Practices"]
    ))

    # ER_H_035
    qs.append(make_er_q(
        qid="ER_H_035", diff="Hard", qtype="Single-Choice", subtopic="Tarkunde Committee Multi-Member Recommendation",
        en_stem="The Tarkunde Committee (1974) and Dinesh Goswami Committee (1990) both recommended transforming the Election Commission into a multi-member body. In which year was the first Presidential notification issued temporarily making the ECI a 3-member body?",
        ta_stem="தர்குண்டே குழு (1974) மற்றும் தினேஷ் கோஸ்வாமி குழு (1990) ஆகிய இரண்டும் தேர்தல் ஆணையத்தை பல உறுப்பினர்கள் கொண்ட அமைப்பாக மாற்ற பரிந்துரைத்தன. எந்த ஆண்டு முதன்முதலில் தேர்தல் ஆணையத்தை 3 நபர் அமைப்பாக மாற்றி தற்காலிக குடியரசுத் தலைவர் அறிவிக்கை வெளியானது?",
        en_a="1989", ta_a="1989",
        en_b="1993", ta_b="1993",
        en_c="1977", ta_c="1977",
        en_d="2001", ta_d="2001",
        correct_key="A",
        exp_en="On 16 October 1989, President R. Venkataraman issued a notification under Article 324(2) appointing two Election Commissioners (S.S. Dhanoa and V.S. Seigell) alongside CEC R.V.S. Peri Sastri, making the ECI a 3-member body for the first time. However, this multi-member body was rescinded in January 1990 by the National Front government, before being permanently restored in October 1993.",
        exp_ta="1989 அக்டோபர் 16 அன்று குடியரசுத் தலைவர் ஆர். வெங்கட்ராமன் சரத்து 324(2)-ன் கீழ் இரு தேர்தல் ஆணையர்களை நியமித்து முதன்முதலில் ECI-ஐ 3 நபர் அமைப்பாக மாற்றினார். ஆனால் 1990 ஜனவரியில் இது ரத்து செய்யப்பட்டு, மீண்டும் 1993 அக்டோபரில் நிரந்தரமாக 3 நபர் ஆணையமாக மாற்றப்பட்டது.",
        why_a_en="Correct. First made multi-member on 16 October 1989.",
        why_a_ta="சரியானது. முதன்முதலில் 1989 அக்டோபர் 16 அன்று பல நபர் அமைப்பாக மாற்றப்பட்டது.",
        why_b_en="Incorrect. October 1993 was when the multi-member Commission was permanently re-established under CEC T.N. Seshan.",
        why_b_ta="தவறானது. 1993 அக்டோபரில் நிரந்தரமாக மீண்டும் பல நபர் அமைப்பானது.",
        why_c_en="Incorrect. 1977 was single-member.",
        why_c_ta="தவறானது. 1977-ல் ஒரு நபர் அமைப்பாகவே இருந்தது.",
        why_d_en="Incorrect. 2001 was much later.",
        why_d_ta="தவறானது. 2001 மிக பிந்தையது.",
        tip_en="Timeline: 1950 to Oct 1989: Single member -> Oct 1989 to Jan 1990: 3 members -> Jan 1990 to Oct 1993: Single member -> Oct 1993 to present: 3 members.",
        tip_ta="காலக்கோடு: 1950 - அக் 1989: 1 நபர் -> அக் 1989 - ஜன 1990: 3 நபர் -> ஜன 1990 - அக் 1993: 1 நபர் -> அக் 1993 முதல் இன்று வரை: 3 நபர்.",
        fact_en="In S.S. Dhanoa v. Union of India (1991), the Supreme Court upheld the President's power to abolish the posts of Election Commissioners.",
        fact_ta="1991 தனோவா வழக்கில் தேர்தல் ஆணையர் பதவிகளை நீக்கும் குடியரசுத் தலைவரின் அதிகாரத்தை உச்ச நீதிமன்றம் உறுதி செய்தது.",
        tags=["ECI Multi-Member Evolution", "1989 Notification", "Tarkunde Goswami"]
    ))

    # ER_H_036
    qs.append(make_er_q(
        qid="ER_H_036", diff="Hard", qtype="Single-Choice", subtopic="Section 10A Jurisprudence",
        en_stem="In Umlesh Yadav v. Election Commission of India (2011), what historic precedent was established by the ECI regarding the disqualification of an elected legislator under Section 10A of RPA 1951?",
        ta_stem="உம்லேஷ் யாதவ் எதிர் இந்திய தேர்தல் ஆணையம் (2011) வழக்கில், மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 10A-ன் கீழ் ஒரு சட்டமன்ற உறுப்பினரை தகுதிநீக்கம் செய்ததில் தேர்தல் ஆணையம் நிலைநாட்டிய வரலாற்று முன்மாதிரி என்ன?",
        en_a="First ever disqualification of a sitting legislator for suppressing expenditure incurred on 'Paid News' in their election expense account", ta_a="தேர்தல் செலவுக் கணக்கில் 'ஊதியச் செய்தி' (Paid News) செலவை மறைத்ததற்காக ஒரு மக்கள் பிரதிநிதி தகுதிநீக்கம் செய்யப்பட்ட முதல் வரலாற்று நிகழ்வு",
        en_b="Disqualification of a candidate for possessing assets worth more than ₹100 Crore", ta_b="₹100 கோடிக்கும் அதிகமான சொத்துக்களை வைத்திருந்ததற்காக ஒரு வேட்பாளர் தகுதிநீக்கம் செய்யப்பட்டது",
        en_c="Disqualification for giving election campaign speeches exclusively in English", ta_c="ஆங்கிலத்தில் மட்டுமே தேர்தல் பிரச்சார உரைகளை ஆற்றியதற்காக தகுதிநீக்கம் செய்யப்பட்டது",
        en_d="Disqualification for voting in favor of a rival party candidate in the Rajya Sabha", ta_d="மாநிலங்களவையில் எதிர்த்தரப்பு வேட்பாளருக்கு வாக்களித்ததற்காக தகுதிநீக்கம் செய்யப்பட்டது",
        correct_key="A",
        exp_en="On 20 October 2011, CEC S.Y. Quraishi disqualified sitting Uttar Pradesh MLA Umlesh Yadav for 3 years under Section 10A of RPA 1951. She had published paid advertisements disguised as news in two Hindi dailies during the 2007 Assembly elections but failed to account for the ₹21,250 expenditure in her statutory election expenses.",
        exp_ta="2011 அக்டோபர் 20 அன்று, தலைமை தேர்தல் ஆணையர் எஸ்.ஒய். குரேஷி, உத்தரபிரதேச சட்டமன்ற உறுப்பினர் உம்லேஷ் யாதவை 3 ஆண்டுகளுக்கு தகுதிநீக்கம் செய்தார். அவர் 2007 தேர்தலில் செய்தித்தாள்களில் ஊதியச் செய்திகளை வெளியிட்டுவிட்டு, அதற்கான ₹21,250 செலவை தனது அதிகாரப்பூர்வ கணக்கில் மறைத்ததற்காக இந்நடவடிக்கை எடுக்கப்பட்டது.",
        why_a_en="Correct. First disqualification for hiding paid news expenses under Section 10A.",
        why_a_ta="சரியானது. ஊதியச் செய்தி செலவை மறைத்ததற்காக பிரிவு 10A-ன் கீழ் செய்யப்பட்ட முதல் தகுதிநீக்கம்.",
        why_b_en="Incorrect. High net worth is not a disqualification.",
        why_b_ta="தவறானது. சொத்து மதிப்பு தகுதியின்மை அல்ல.",
        why_c_en="Incorrect. Language of speech is unrestricted under free speech.",
        why_c_ta="தவறானது. பிரச்சார மொழிக்கு தடை இல்லை.",
        why_d_en="Incorrect. Cross-voting in Rajya Sabha is governed by party discipline, not Section 10A.",
        why_d_ta="தவறானது. மாநிலங்களவை வாக்களிப்பு பிரிவு 10A-ல் வராது.",
        tip_en="Section 10A disqualifies for failure to lodge an account of election expenses 'in the manner required by or under this Act'. Filing an untrue or falsified account violates this section.",
        tip_ta="பிரிவு 10A-ன் கீழ் தவறான அல்லது பொய்யான செலவுக் கணக்கை தாக்கல் செய்வதும் கணக்கு தாக்கல் செய்யாத குற்றமாகவே கருதப்படும்.",
        fact_en="The Press Council of India corroborated that the news articles in Amar Ujala and Dainik Jagran were identical and constituted Paid News.",
        fact_ta="அமர் உஜாலா மற்றும் தைனிக் ஜாக்ரான் நாளிதழ்களில் வெளியான கட்டுரைகள் ஒரே மாதிரியானவை என்றும் அவை ஊதியச் செய்தியே என்றும் பிரஸ் கவுன்சில் உறுதி செய்தது.",
        tags=["Umlesh Yadav 2011", "Section 10A", "Paid News Disqualification", "SY Quraishi"]
    ))

    # ER_H_037
    qs.append(make_er_q(
        qid="ER_H_037", diff="Hard", qtype="Single-Choice", subtopic="Section 123(3) Secularism Scope",
        en_stem="In the 1996 Hindutva judgments (Ramesh Yeshwant Prabhoo v. Prabhakar Kashinath Kunte), how did the 3-judge bench of the Supreme Court interpret the term 'Hindutva' or 'Hinduism' in the context of Section 123(3)?",
        ta_stem="1996 இந்துத்துவா தீர்ப்புகளில் (ரமேஷ் யஷ்வந்த் பிரபு வழக்கு), மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 123(3)-ன் பின்னணியில் 'இந்துத்துவா' அல்லது 'இந்து மதம்' என்ற சொல்லை உச்ச நீதிமன்றத்தின் 3 நீதிபதிகள் அமர்வு எவ்வாறு விளக்கியது?",
        en_a="It was held to mean a way of life or state of mind, and not equated automatically with narrow religious fundamentalism, though abusive communal speeches were held corrupt", ta_a="இது ஒரு வாழ்க்கை முறை (Way of life) அல்லது மனநிலை என விளக்கப்பட்டது; மேலும் வெறும் சொற்பயன்பாடு மத அடிப்படைவாதமாகாது என்றாலும், வகுப்புவாத துவேஷ பேச்சுக்கள் ஊழல் நடைமுறையாகும் எனப்பட்டது",
        en_b="It was declared to be the mandatory official state religion of all contesting political parties", ta_b="அனைத்து அரசியல் கட்சிகளுக்கும் இது கட்டாய அதிகாரப்பூர்வ மதமாக அறிவிக்கப்பட்டது",
        en_c="The court completely exempted all religious appeals from the purview of Section 123(3)", ta_c="அனைத்து மதப் பிரச்சாரங்களுக்கும் பிரிவு 123(3)-லிருந்து நீதிமன்றம் முழு விலக்கு அளித்தது",
        en_d="The court abolished the Representation of the People Act, 1951 as unconstitutional", ta_d="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ஐ அரசியலமைப்புக்கு எதிரானது என ரத்து செய்தது",
        correct_key="A",
        exp_en="In Ramesh Yeshwant Prabhoo (1996), Justice J.S. Verma observed that 'Hindutva' or 'Hinduism' may be used to depict a way of life of the people of the subcontinent and is not necessarily to be understood and construed as meaning strict Hindu religion. However, the court upheld the High Court's finding that the candidate's actual derogatory speeches against Muslims constituted a corrupt practice under Section 123(3).",
        exp_ta="ரமேஷ் யஷ்வந்த் பிரபு (1996) வழக்கில் நீதிபதி ஜே.எஸ். வர்மா, 'இந்துத்துவா' என்பது இத்துணைக்கண்ட மக்களின் ஒரு வாழ்க்கை முறை (Way of life) என்றும், அது குறுகிய மதவாதத்தைக் குறிக்க வேண்டியதில்லை என்றும் கூறினார். எனினும் குறிப்பிட்ட வழக்கில் முஸ்லிம்களுக்கு எதிராக பேசிய துவேஷப் பேச்சுக்கள் பிரிவு 123(3)-ன் கீழ் ஊழல் நடைமுறை என தீர்ப்பளிக்கப்பட்டு தேர்தல் ரத்து செய்யப்பட்டது.",
        why_a_en="Correct. Way of life doctrine, while actual hate speech remained corrupt.",
        why_a_ta="சரியானது. வாழ்க்கை முறை விளக்கம்; அதே வேளையில் துவேஷப் பேச்சு ஊழல் நடைமுறையாகவே தண்டிக்கப்பட்டது.",
        why_b_en="Incorrect. India is a secular republic under the Preamble.",
        why_b_ta="தவறானது. இந்தியா ஒரு மதச்சார்பற்ற குடியரசு.",
        why_c_en="Incorrect. Religious appeals remain strictly barred under Section 123(3).",
        why_c_ta="தவறானது. மதத்தின் பெயரால் வாக்குக் கேட்பது தடை செய்யப்பட்டுள்ளது.",
        why_d_en="Incorrect. RPA 1951 remains fully valid.",
        why_d_ta="தவறானது. சட்டம் முழு செல்லுபடியுடன் உள்ளது.",
        tip_en="In 2017 (Abhiram Singh), the 7-judge Constitution Bench declined to reconsider the 'way of life' definition, focusing instead on the broader interpretation of 'his religion'.",
        tip_ta="2017 அபிராம் சிங் வழக்கில் 7 நீதிபதிகள் அமர்வு 'வாழ்க்கை முறை' விளக்கத்தை மறுபரிசீலனை செய்யாமல், 'மதம்' என்பதன் விரிவான எல்லையை வரையறுத்தது.",
        fact_en="Bal Thackeray was disenfranchised for 6 years following this judgment for corrupt practices during that 1987 by-election campaign.",
        fact_ta="இத்தீர்ப்பைத் தொடர்ந்து பால் தாக்கரேவின் வாக்குரிமை பிரிவு 8A-ன் கீழ் 6 ஆண்டுகளுக்கு பறிக்கப்பட்டது.",
        tags=["Hindutva Judgment 1996", "Ramesh Prabhoo", "Way of Life", "Section 123(3)"]
    ))

    # ER_H_038
    qs.append(make_er_q(
        qid="ER_H_038", diff="Hard", qtype="Single-Choice", subtopic="Postal Ballot Category Expansion",
        en_stem="Under Rule 27A of the Conduct of Elections Rules, 1961, which newly added category of citizens was notified as 'absentee voters' eligible for postal ballots during the Covid-19 pandemic and subsequent elections?",
        ta_stem="தேர்தல் நடத்தை விதிகள் 1961 விதி 27A-ன் கீழ், கோவிட் பெருந்தொற்று மற்றும் தொடர்ந்த தேர்தல்களில் தபால் வாக்கு பெற தகுதியான 'வராத வாக்காளர்கள்' (Absentee Voters) என புதிதாக அறிவிக்கப்பட்ட பிரிவு எது?",
        en_a="Persons employed in essential services, senior citizens (85+), Persons with Disabilities (PwD 40%+), and Covid-19 suspect or affected persons", ta_a="அத்தியாவசியப் பணிகளில் உள்ள பணியாளர்கள், மூத்த குடிமக்கள் (85+), மாற்றுத்திறனாளிகள் (40%+) மற்றும் கோவிட் தொற்றால் பாதிக்கப்பட்டவர்கள்",
        en_b="All college students enrolled in accredited distance education universities", ta_b="அங்கீகரிக்கப்பட்ட தொலைதூரக் கல்வி பல்கலைக்கழகங்களில் படிக்கும் அனைத்து கல்லூரி மாணவர்கள்",
        en_c="All income-tax payers filing returns above ₹10 Lakhs", ta_c="₹10 லட்சத்திற்கு மேல் வரி செலுத்தும் அனைத்து வருமான வரி செலுத்துவோர்",
        en_d="All commercial airline pilots flying domestic passenger flights", ta_d="உள்நாட்டு விமானங்களை இயக்கும் அனைத்து வணிக விமான ஓட்டிகள்",
        correct_key="A",
        exp_en="In 2019 and 2020, the Ministry of Law amended Rule 27A to introduce the category of 'Absentee Voter' entitled to vote by postal ballot (Form 12D). This encompasses: (1) Senior Citizens (initially 80+, revised to 85+ in 2024), (2) Persons with benchmark disabilities (PwD 40%+), (3) COVID-19 suspect or affected persons, and (4) Essential Service Personnel (police, fire, healthcare, media, transport) notified by ECI.",
        exp_ta="2019 மற்றும் 2020-ல் தேர்தல் விதிகள் திருத்தப்பட்டு 'வராத வாக்காளர்' (Absentee Voter) என்ற புதிய பிரிவு உருவாக்கப்பட்டது. இதன் மூலம் (1) மூத்த குடிமக்கள் (85+), (2) மாற்றுத்திறனாளிகள் (40%+), (3) கோவிட் தொற்றுடையோர், (4) அத்தியாவசிய சேவைப் பணியாளர்கள் (காவல்துறை, மருத்துவம், தீயணைப்பு, ஊடகம்) படிவம் 12D மூலம் தபால் வாக்கு போட அனுமதிக்கப்பட்டனர்.",
        why_a_en="Correct. Essential services, senior citizens (85+), PwDs, and Covid affected voters.",
        why_a_ta="சரியானது. அத்தியாவசிய பணியாளர்கள், மூத்த குடிமக்கள், மாற்றுத்திறனாளிகள் மற்றும் கோவிட் நோயாளிகள்.",
        why_b_en="Incorrect. College students are not absentee voters.",
        why_b_ta="தவறானது. கல்லூரி மாணவர்களுக்கு இச்சலுகை இல்லை.",
        why_c_en="Incorrect. Income tax slabs do not confer postal voting rights.",
        why_c_ta="தவறானது. வரி செலுத்துவோருக்கு தபால் வாக்கு இல்லை.",
        why_d_en="Incorrect. Airline pilots as a class are not separate absentee voters unless notified.",
        why_d_ta="தவறானது. விமானிகளுக்கு தனியாக இச்சலுகை இல்லை.",
        tip_en="Home voting teams visit the voter's residence twice; if absent on both visits, the voter can only vote at the polling station.",
        tip_ta="வீட்டு வாக்களிப்பு குழுவினர் இருமுறை இல்லத்திற்கு செல்வர்; இருமுறையும் இல்லாவிட்டால் அவர்கள் நேரடியாக வாக்குச்சாவடிக்குச் சென்றுதான் வாக்களிக்க முடியும்.",
        fact_en="Over 5.8 lakh senior citizens and PwD electors exercised home voting in the 2024 Lok Sabha elections.",
        fact_ta="2024 மக்களவைத் தேர்தலில் 5.8 லட்சத்திற்கும் மேற்பட்ட மூத்த குடிமக்கள் மற்றும் மாற்றுத்திறனாளிகள் வீட்டிலிருந்தே வாக்களித்தனர்.",
        tags=["Absentee Voters", "Rule 27A", "Home Voting", "Postal Ballot Expansion"]
    ))

    # ER_H_039
    qs.append(make_er_q(
        qid="ER_H_039", diff="Hard", qtype="Single-Choice", subtopic="Section 29A Registration Conditions",
        en_stem="Under Section 29A(5) of the Representation of the People Act, 1951, what specific constitutional declaration must be explicitly incorporated into the memorandum, constitution, or rules of an association seeking registration as a political party?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 29A(5)-ன் கீழ், அரசியல் கட்சியாக பதிவு செய்ய விரும்பும் ஓர் அமைப்பு தனது சட்டதிட்டங்களில் (Constitution/Rules) வெளிப்படையாக இணைக்க வேண்டிய அரசியலமைப்பு உறுதிமொழி என்ன?",
        en_a="True faith and allegiance to the Constitution of India as by law established, and to the principles of socialism, secularism, and democracy, and upholding the sovereignty, unity, and integrity of India", ta_a="சட்டப்படி நிறுவப்பட்ட இந்திய அரசியலமைப்பிற்கும், சோசலிசம், மதச்சார்பின்மை, ஜனநாயகம் ஆகிய கொள்கைகளுக்கும் உண்மையான விசுவாசம் செலுத்துவதுடன், இந்தியாவின் இறையாண்மை, ஒற்றுமை, ஒருமைப்பாட்டை நிலைநிறுத்துதல்",
        en_b="Unconditional adherence to the economic policies formulated by NITI Aayog", ta_b="நிதி ஆயோக் வகுக்கும் பொருளாதாரக் கொள்கைகளை நிபந்தனையின்றி பின்பற்றுதல்",
        en_c="Pledge to contest at least 50% of parliamentary seats in every general election", ta_c="ஒவ்வொரு பொதுத்தேர்தலிலும் குறைந்தது 50% நாடாளுமன்றத் தொகுதிகளில் போட்டியிடுவதாக உறுதிமொழி",
        en_d="Affidavit declaring that no member of the party owns private agricultural land", ta_d="கட்சியின் எந்த உறுப்பினருக்கும் தனியார் விவசாய நிலம் சொந்தமாக இல்லை என்ற உறுதிமொழி",
        correct_key="A",
        exp_en="Section 29A(5) of RPA 1951 mandates that the application for party registration must be accompanied by a copy of the party's memorandum/rules which MUST contain a specific provision declaring that the party shall bear true faith and allegiance to the Constitution of India as by law established, and to the principles of socialism, secularism, and democracy, and would uphold the sovereignty, unity, and integrity of India.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 29A(5), ஒரு கட்சி தனது விதிமுறைகளில், 'சட்டப்படி நிறுவப்பட்ட இந்திய அரசியலமைப்பின் மீதும், சோசலிசம், மதச்சார்பின்மை, ஜனநாயகம் ஆகிய கொள்கைகளின் மீதும் உண்மையான நம்பிக்கையும் விசுவாசமும் கொண்டிருப்பதாகவும், இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டை நிலைநிறுத்துவதாகவும்' தெளிவான விதியை இணைக்க வேண்டும் எனக் கட்டாயமாக்குகிறது.",
        why_a_en="Correct. Allegiance to Constitution, socialism, secularism, democracy, and national integrity.",
        why_a_ta="சரியானது. அரசியலமைப்பு, சோசலிசம், மதச்சார்பின்மை, ஜனநாயகம் மற்றும் இறையாண்மை மீதான விசுவாசம்.",
        why_b_en="Incorrect. NITI Aayog policy adherence is not required.",
        why_b_ta="தவறானது. நிதி ஆயோக் கொள்கைக்கு தொடர்பில்லை.",
        why_c_en="Incorrect. No minimum contest requirement exists for registration.",
        why_c_ta="தவறானது. 50% இடங்களில் போட்டியிட வேண்டிய அவசியமில்லை.",
        why_d_en="Incorrect. Private land ownership is completely irrelevant.",
        why_d_ta="தவறானது. நில உடைமைக்கு தொடர்பில்லை.",
        tip_en="This statutory provision directly imports the values of the Preamble (as amended by the 42nd Amendment) into the governance of political parties.",
        tip_ta="இப்பிரிவு முகப்புரையின் விழுமியங்களை (சோசலிசம், மதச்சார்பின்மை, ஜனநாயகம்) அரசியல் கட்சிகளின் நிர்வாகத்தில் நேரடியாக புகுத்துகிறது.",
        fact_en="Refusal to include this declaration results in automatic rejection of the registration application by the ECI under Section 29A(7).",
        fact_ta="இவ்வுறுதிமொழியை விதிமுறைகளில் சேர்க்க மறுத்தால் தேர்தல் ஆணையம் கட்சி பதிவை உடனடியாக நிராகரிக்கும்.",
        tags=["Section 29A(5)", "Party Registration", "Constitutional Allegiance", "Secularism"]
    ))

    # ER_H_040
    qs.append(make_er_q(
        qid="ER_H_040", diff="Hard", qtype="Single-Choice", subtopic="Rule 56D VVPAT Slip Count Recount",
        en_stem="Under Rule 56D of the Conduct of Elections Rules, 1961, what procedure governs a candidate's application for the physical counting of VVPAT paper slips in a polling station?",
        ta_stem="தேர்தல் நடத்தை விதிகள் 1961 விதி 56D-ன் கீழ், ஒரு வாக்குச்சாவடியில் VVPAT காகித சீட்டுகளை எண்ணி சரிபார்க்க வேட்பாளர் மனு அளிக்கும் நடைமுறை என்ன?",
        en_a="The candidate/agent must apply in writing stating grounds to the Returning Officer after EVM count is completed; the Returning Officer may allow or reject with recorded reasons", ta_a="EVM வாக்கு எண்ணிக்கை முடிந்த பின், வேட்பாளர்/முகவர் காரணங்களைக் குறிப்பிட்டு தேர்தல் நடத்தும் அலுவலரிடம் எழுத்துப்பூர்வமாக விண்ணப்பிக்க வேண்டும்; அலுவலர் காரணங்களை பதிவு செய்து அதை ஏற்கலாம் அல்லது நிராகரிக்கலாம்",
        en_b="The Returning Officer is legally bound to accept every request and must order a 100% recount automatically", ta_b="தேர்தல் நடத்தும் அலுவலர் அனைத்து கோரிக்கைகளையும் கட்டாயம் ஏற்று 100% மறுவாக்கு எண்ணிக்கைக்கு உத்தரவிட வேண்டும்",
        en_c="The application can only be filed by the Governor of the State after consultation with the High Court", ta_c="உயர் நீதிமன்றத்தைக் கலந்தாலோசித்த பின் மாநில ஆளுநர் மட்டுமே இத்தகைய மனுவை அளிக்க முடியும்",
        en_d="The application must be accompanied by a non-refundable cash deposit of ₹10 Lakhs", ta_d="இம்மனுவுடன் ₹10 லட்சம் திரும்பப் பெற முடியாத ரொக்க வைப்புத்தொகை செலுத்தப்பட வேண்டும்",
        correct_key="A",
        exp_en="Under Rule 56D(1), after the results of all EVM rounds have been announced, a candidate or their election agent may apply in writing to the Returning Officer to count the printed paper slips of VVPAT in any polling station, stating the grounds. Under Rule 56D(2), the Returning Officer decides whether to allow the recount in whole or part, or reject it for being frivolous or unreasonable, recording written reasons.",
        exp_ta="விதி 56D(1)-ன் படி, EVM வாக்கு எண்ணிக்கை முடிந்த பிறகு, வேட்பாளர் காரணங்களைக் குறிப்பிட்டு VVPAT சீட்டுகளை எண்ணக் கோரி தேர்தல் நடத்தும் அலுவலரிடம் மனு அளிக்கலாம். அலுவலர் தனது எழுத்துப்பூர்வ காரணங்களைப் பதிவு செய்து, மனுவை ஏற்கவோ அல்லது வீண் கோரிக்கை என நிராகரிக்கவோ முழு உரிமை கொண்டுள்ளார்.",
        why_a_en="Correct. Written application stating grounds; RO decides with recorded reasons.",
        why_a_ta="சரியானது. காரணங்களுடன் கூடிய எழுத்துப்பூர்வ மனு; தேர்தல் நடத்தும் அலுவலர் காரணங்களை பதிவு செய்து முடிவெடுப்பார்.",
        why_b_en="Incorrect. RO is not bound to accept frivolous applications.",
        why_b_ta="தவறானது. அலுவலர் தானாக ஏற்க வேண்டிய கட்டாயமில்லை.",
        why_c_en="Incorrect. Candidate or agent applies, not the Governor.",
        why_c_ta="தவறானது. வேட்பாளரே மனு அளிக்கிறார், ஆளுநர் அல்ல.",
        why_d_en="Incorrect. No ₹10 Lakh statutory deposit is prescribed in Rule 56D.",
        why_d_ta="தவறானது. அத்தகைய கட்டணம் விதியில் இல்லை.",
        tip_en="If the RO allows the application, the VVPAT paper slip count supersedes the EVM electronic count under Rule 56D(4)(b).",
        tip_ta="மனு ஏற்கப்பட்டு VVPAT சீட்டுகள் எண்ணப்பட்டால், EVM கணக்கீட்டை விட VVPAT சீட்டுகளின் எண்ணிக்கையே இறுதியானது (விதி 56D(4)(b)).",
        fact_en="This physical recount under Rule 56D is in addition to the mandatory 5-polling-station random verification ordered by the Supreme Court.",
        fact_ta="உச்ச நீதிமன்றம் உத்தரவிட்ட 5 வாக்குச்சாவடி கட்டாய சரிபார்ப்புக்கு கூடுதலாக இந்த தனிநபர் மறுவாக்கு எண்ணிக்கை வாய்ப்பு உள்ளது.",
        tags=["Rule 56D", "VVPAT Slip Recount", "Returning Officer Discretion"]
    ))

    # ER_H_041
    qs.append(make_er_q(
        qid="ER_H_041", diff="Hard", qtype="Single-Choice", subtopic="Section 128 Maintenance of Secrecy",
        en_stem="Under Section 128 of the Representation of the People Act, 1951, what penalty is imposed on any election officer, polling agent, or person who violates the maintenance of secrecy of voting?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 128-ன் கீழ், வாக்களிப்பின் ரகசியத்தன்மையை மீறும் தேர்தல் அலுவலர், முகவர் அல்லது எந்தவொரு நபருக்கும் விதிக்கப்படும் தண்டனை என்ன?",
        en_a="Imprisonment for a term which may extend to 3 months, or fine, or both", ta_a="3 மாதங்கள் வரை நீட்டிக்கக்கூடிய சிறைத்தண்டனை, அல்லது அபராதம், அல்லது இரண்டும்",
        en_b="Imprisonment for a mandatory term of 7 years without bail", ta_b="ஜாமீனில் வெளிவர முடியாத 7 ஆண்டுகள் கட்டாய சிறைத்தண்டனை",
        en_c="A flat administrative fine of ₹50 without any prison sentence", ta_c="சிறைத்தண்டனை இன்றி வெறும் ₹50 நிர்வாக அபராதம் மட்டும்",
        en_d="Immediate termination of Indian citizenship", ta_d="இந்திய குடியுரிமை உடனடியாக ரத்து செய்யப்படுவது",
        correct_key="A",
        exp_en="Section 128 of RPA 1951 mandates that every officer, clerk, agent, or other person who performs any duty in connection with the recording or counting of votes shall maintain and aid in maintaining the secrecy of voting. Any person who contravenes this provision is punishable with imprisonment for a term which may extend to 3 months, or with fine, or with both.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 128, வாக்குப்பதிவு அல்லது வாக்கு எண்ணிக்கையில் ஈடுபடும் அனைத்து அலுவலர்கள் மற்றும் முகவர்கள் வாக்களிப்பின் ரகசியத்தை கட்டாயம் பாதுகாக்க வேண்டும் எனக் கூறுகிறது. இதை மீறி ரகசியத்தை வெளியிடும் எவருக்கும் 3 மாதங்கள் வரை சிறைத்தண்டனை அல்லது அபராதம் அல்லது இரண்டும் விதிக்கப்படும்.",
        why_a_en="Correct. Up to 3 months imprisonment or fine or both under Section 128.",
        why_a_ta="சரியானது. பிரிவு 128-ன் கீழ் 3 மாதங்கள் வரை சிறை அல்லது அபராதம்.",
        why_b_en="Incorrect. 7 years is for major heinous offences.",
        why_b_ta="தவறானது. 7 ஆண்டுகள் கடுமையான குற்றங்களுக்கானது.",
        why_c_en="Incorrect. Prison sentence is explicitly provided.",
        why_c_ta="தவறானது. சிறைத்தண்டனை சட்டத்தில் உள்ளது.",
        why_d_en="Incorrect. Citizenship cannot be revoked for this.",
        why_d_ta="தவறானது. குடியுரிமை பறிக்கப்படாது.",
        tip_en="Section 128 applies to booth officers, candidates, counting agents, and any observer witnessing the vote recording.",
        tip_ta="பிரிவு 128 வாக்குச்சாவடி அதிகாரிகள், வேட்பாளர்கள், முகவர்கள் அனைவருக்கும் பொருந்தும்.",
        fact_en="Section 130 independently prohibits canvassing within a 100-meter radius of any polling station.",
        fact_ta="பிரிவு 130 வாக்குச்சாவடியின் 100 மீட்டர் எல்லைக்குள் வாக்கு சேகரிப்பதை தடை செய்கிறது.",
        tags=["Section 128", "Secrecy of Voting", "3 Months Imprisonment", "Penal Safeguard"]
    ))

    # ER_H_042
    qs.append(make_er_q(
        qid="ER_H_042", diff="Hard", qtype="Single-Choice", subtopic="Section 130 100-Meter Perimeter",
        en_stem="Under Section 130 of the Representation of the People Act, 1951, within what distance from a polling station is electioneering, soliciting votes, and displaying campaign posters strictly prohibited on polling day?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 130-ன் கீழ், வாக்குப்பதிவு நாளன்று வாக்குச்சாவடியிலிருந்து எத்தனை மீட்டர் சுற்றளவிற்குள் தேர்தல் பிரச்சாரம் செய்வதும், வாக்கு சேகரிப்பதும், சுவரொட்டிகளை வைப்பதும் திட்டவட்டமாக தடை செய்யப்பட்டுள்ளது?",
        en_a="Within a distance of 100 meters", ta_a="100 மீட்டர் சுற்றளவிற்குள்",
        en_b="Within a distance of 500 meters", ta_b="500 மீட்டர் சுற்றளவிற்குள்",
        en_c="Within a distance of 50 meters", ta_c="50 மீட்டர் சுற்றளவிற்குள்",
        en_d="Within a distance of 1 kilometer", ta_d="1 கிலோமீட்டர் சுற்றளவிற்குள்",
        correct_key="A",
        exp_en="Section 130(1) of RPA 1951 states that no person shall, on the date of polling, commit any of the following acts within the polling station or in any public or private place within a distance of 100 meters of the polling station: (a) canvassing for votes; (b) soliciting the vote of any elector; (c) persuading any elector not to vote for any candidate; (d) exhibiting any notice or sign relating to the election.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 130(1)-ன் படி, வாக்குப்பதிவு நாளன்று வாக்குச்சாவடியிலிருந்து 100 மீட்டர் சுற்றளவிற்குள் வாக்கு சேகரிப்பது, பிரச்சாரம் செய்வது, கட்சிக் கொடி அல்லது சின்னங்களை காட்சிப்படுத்துவது ஆகியவை தடை செய்யப்பட்ட குற்றமாகும்.",
        why_a_en="Correct. Exactly 100 meters from the polling station.",
        why_a_ta="சரியானது. வாக்குச்சாவடியிலிருந்து 100 மீட்டர் சுற்றளவிற்குள்.",
        why_b_en="Incorrect. 500 meters is incorrect.",
        why_b_ta="தவறானது. 500 மீட்டர் தவறானது.",
        why_c_en="Incorrect. 50 meters is too narrow.",
        why_c_ta="தவறானது. 50 மீட்டர் தவறானது.",
        why_d_en="Incorrect. 1 km is too wide.",
        why_d_ta="தவறானது. 1 கி.மீ தவறானது.",
        tip_en="Violation of Section 130 is a cognizable offence punishable with fine up to ₹250 under Section 130(2).",
        tip_ta="பிரிவு 130-ஐ மீறுவது ₹250 வரை அபராதம் விதிக்கப்படக்கூடிய குற்றமாகும்.",
        fact_en="Section 131 prohibits disorderly conduct and use of cellular phones, megaphones, or loudspeakers within this 100-meter perimeter.",
        fact_ta="பிரிவு 131 இந்த 100 மீட்டர் எல்லைக்குள் ஒலிபெருக்கிகள் மற்றும் செல்போன்கள் பயன்படுத்துவதைத் தடை செய்கிறது.",
        tags=["Section 130", "100 Meters Perimeter", "Canvassing Ban", "Polling Station"]
    ))

    # ER_H_043
    qs.append(make_er_q(
        qid="ER_H_043", diff="Hard", qtype="Single-Choice", subtopic="Section 134 Breach of Official Duty",
        en_stem="Under Section 134 of the Representation of the People Act, 1951, what penalty applies to any government official (such as a District Election Officer, RO, or Presiding Officer) who is guilty of any act or omission in breach of their official duty without reasonable cause?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 134-ன் கீழ், நியாயமான காரணமின்றி தனது தேர்தல் கடமையைச் செய்யத் தவறும் அல்லது விதிமீறும் அரசு அலுவலருக்கு (DEO, RO, வாக்குச்சாவடி தலைமை அலுவலர்) விதிக்கப்படும் தண்டனை என்ன?",
        en_a="Fine which may extend to ₹500, and cognizable without police warrant upon formal complaint by ECI", ta_a="₹500 வரை அபராதம் விதிக்கப்படும்; ECI-ன் புகாரின் பேரில் வாரண்ட் இன்றியே கைது செய்யப்படலாம்",
        en_b="Permanent forfeiture of government pension rights and dismissal from service", ta_b="அரசு ஓய்வூதிய உரிமைகள் நிரந்தர பறிமுதல் மற்றும் பணியிலிருந்து நீக்கம்",
        en_c="Mandatory life imprisonment under anti-treason statutes", ta_c="தேசத்துரோக சட்டங்களின் கீழ் கட்டாய வாழ்நாள் சிறைத்தண்டனை",
        en_d="No penalty can ever be imposed on civil servants while in service", ta_d="பணியில் இருக்கும் போது அரசு ஊழியர்கள் மீது எந்த தண்டனையும் விதிக்க முடியாது",
        correct_key="A",
        exp_en="Section 134(1) of RPA 1951 provides that if any person to whom this section applies (ROs, AROs, Presiding Officers, Polling Officers, EROs) is without reasonable cause guilty of any act or omission in breach of his official duty, he shall be punishable with fine which may extend to ₹500. Under Section 134(3), no court takes cognizance of such offence except upon complaint made by or under the authority of ECI or CEO.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 134(1)-ன் படி, தேர்தல் கடமையில் உள்ள அலுவலர்கள் நியாயமான காரணமின்றி கடமை தவறி செயல்பட்டால், அவர்களுக்கு ₹500 வரை அபராதம் விதிக்கப்படும். தேர்தல் ஆணையம் அல்லது தலைமைத் தேர்தல் அதிகாரியின் புகாரின் பேரில் மட்டுமே நீதிமன்றம் இதை விசாரிக்க முடியும்.",
        why_a_en="Correct. Fine up to ₹500 under Section 134(1).",
        why_a_ta="சரியானது. பிரிவு 134(1)-ன் கீழ் ₹500 வரை அபராதம்.",
        why_b_en="Incorrect. Pension forfeiture is governed by departmental service rules, not Section 134 directly.",
        why_b_ta="தவறானது. ஓய்வூதிய பறிமுதல் சேவை விதிகளுக்குட்பட்டது.",
        why_c_en="Incorrect. Treason laws do not apply to simple breach of election duty.",
        why_c_ta="தவறானது. தேசத்துரோக சட்டம் பொருந்தாது.",
        why_d_en="Incorrect. Civil servants are fully subject to penal sanctions under RPA 1951.",
        why_d_ta="தவறானது. அரசு ஊழியர்கள் சட்டத்திற்கு உட்பட்டவர்களே.",
        tip_en="All civil servants and police personnel placed on election duty are deemed to be on deputation to the Election Commission under Section 28A of RPA 1951 and Section 13CC of RPA 1950.",
        tip_ta="தேர்தல் பணியில் உள்ள அனைத்து அதிகாரிகளும் ECI-ன் அயல்பணியில் (Deputation) இருப்பதாக பிரிவு 28A-ன் கீழ் கருதப்படுகிறது.",
        fact_en="During this deputation period, ECI has full disciplinary control over them, including the power to suspend or transfer them.",
        fact_ta="இக்காலகட்டத்தில் அதிகாரிகளை பணியிடை நீக்கம் செய்ய அல்லது மாற்ற ECI-க்கு முழு ஒழுங்கு நடவடிக்கை அதிகாரம் உண்டு.",
        tags=["Section 134", "Breach of Official Duty", "₹500 Fine", "Deemed Deputation"]
    ))

    # ER_H_044
    qs.append(make_er_q(
        qid="ER_H_044", diff="Hard", qtype="Single-Choice", subtopic="Section 135B Paid Holiday on Polling Day",
        en_stem="Which section was inserted into the Representation of the People Act, 1951 in 1996 granting every person employed in any business, trade, industrial undertaking, or other establishment a paid holiday on the day of poll?",
        ta_stem="வாக்குப்பதிவு நாளன்று வணிகம், தொழில் அல்லது தனியார் நிறுவனங்களில் பணிபுரியும் ஒவ்வொரு தொழிலாளிக்கும் ஊதியத்துடன் கூடிய விடுமுறை (Paid Holiday) அளிப்பதை கட்டாயமாக்க 1996-ல் மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ல் சேர்க்கப்பட்ட பிரிவு எது?",
        en_a="Section 135B", ta_a="பிரிவு 135B",
        en_b="Section 135A", ta_b="பிரிவு 135A",
        en_c="Section 135C", ta_c="பிரிவு 135C",
        en_d="Section 126", ta_d="பிரிவு 126",
        correct_key="A",
        exp_en="Section 135B was inserted into RPA 1951 by an amendment in 1996. It mandates that every person employed in any business, trade, industrial undertaking, or other establishment entitled to vote in an election shall be granted a holiday on the day of poll, with no deduction or abatement of wages. Violation by an employer attracts a fine up to ₹500.",
        exp_ta="1996-ல் சேர்க்கப்பட்ட பிரிவு 135B, தொழில், வணிகம் மற்றும் தனியார் நிறுவனங்களில் பணிபுரியும் தகுதியான வாக்காளர்களுக்கு வாக்குப்பதிவு நாளன்று ஊதிய பிடித்தம் இல்லாத முழு ஊதியத்துடன் கூடிய விடுமுறை அளிக்கப்பட வேண்டும் என கட்டாயமாக்குகிறது. இதை மீறும் முதலாளிக்கு ₹500 வரை அபராதம் விதிக்கப்படும்.",
        why_a_en="Correct. Section 135B mandates paid holiday on polling day.",
        why_a_ta="சரியானது. பிரிவு 135B ஊதியத்துடன் கூடிய தேர்தல் விடுமுறையை கட்டாயமாக்குகிறது.",
        why_b_en="Incorrect. Section 135A deals with booth capturing.",
        why_b_ta="தவறானது. பிரிவு 135A வாக்குச்சாவடி கைப்பற்றுதல் பற்றியது.",
        why_c_en="Incorrect. Section 135C deals with prohibition of sale of liquor on polling day (dry day).",
        why_c_ta="தவறானது. பிரிவு 135C தேர்தல் நாளில் மது விற்பனை தடை (டிரை டே) பற்றியது.",
        why_d_en="Incorrect. Section 126 deals with 48-hour campaign silence.",
        why_d_ta="தவறானது. பிரிவு 126 அமைதிக்காலம் பற்றியது.",
        tip_en="Remember the trio of 1996 sections: 135A = Booth Capturing (1989), 135B = Paid Holiday (1996), 135C = Dry Day liquor ban (1996).",
        tip_ta="நினைவு உத்தி: 135A = வாக்குச்சாவடி பிடிப்பு (1989), 135B = ஊதிய விடுமுறை (1996), 135C = மது தடை (1996).",
        fact_en="Even daily-wage and casual workers are covered under Section 135B and cannot have their wages cut for exercising their vote.",
        fact_ta="தினக்கூலி தொழிலாளர்களுக்கும் இப்பிரிவு 135B பொருந்தும்; வாக்களிக்கச் சென்றதற்காக கூலியை குறைக்க முடியாது.",
        tags=["Section 135B", "Paid Holiday", "Voters Rights", "1996 Amendment"]
    ))

    # ER_H_045
    qs.append(make_er_q(
        qid="ER_H_045", diff="Hard", qtype="Single-Choice", subtopic="Section 135C Dry Days During Elections",
        en_stem="Under Section 135C of the Representation of the People Act, 1951, for what duration is the sale, distribution, or giving away of intoxicating liquors or substances prohibited within a polling area?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 135C-ன் கீழ், தேர்தல் பகுதியில் மதுபானங்கள் மற்றும் போதைப்பொருட்களை விற்பனை செய்வது அல்லது வழங்குவது எத்தனை காலத்திற்கு தடை செய்யப்பட்டுள்ளது?",
        en_a="During the period of 48 hours ending with the hour fixed for the conclusion of the poll", ta_a="வாக்குப்பதிவு முடிவடைவதற்காக நிர்ணயிக்கப்பட்ட நேரத்திற்கு முந்தைய 48 மணி நேரக் காலம் முழுவதும்",
        en_b="For 7 days prior to the first date of filing nominations", ta_b="வேட்புமனு தாக்கல் தொடங்குவதற்கு 7 நாட்களுக்கு முன்",
        en_c="Exclusively for 12 hours on the day of counting only", ta_c="வாக்கு எண்ணிக்கை நாளில் 12 மணி நேரம் மட்டுமே",
        en_d="Throughout the 3 months following the declaration of results", ta_d="தேர்தல் முடிவுகள் வெளியான பின் 3 மாதங்கள் முழுவதும்",
        correct_key="A",
        exp_en="Section 135C of RPA 1951 (inserted in 1996) provides that no intoxicating liquor or substances shall be sold, given, or distributed at any hotel, tavern, shop, or public/private place within a polling area during the period of 48 hours ending with the hour fixed for the conclusion of the poll. Violation attracts imprisonment up to 6 months or fine up to ₹2,000 or both.",
        exp_ta="1996-ல் சேர்க்கப்பட்ட பிரிவு 135C, வாக்குப்பதிவு முடிவடையும் நேரத்திற்கு முந்தைய 48 மணி நேர காலத்தில் ஹோட்டல்கள், கடைகள் அல்லது எந்தவொரு இடத்திலும் மதுபானங்களை விற்பதோ, வழங்குவதோ முற்றிலுமாக தடை செய்யப்பட்டுள்ளது (Dry Day). மீறினால் 6 மாதம் வரை சிறை அல்லது ₹2,000 அபராதம் விதிக்கப்படும்.",
        why_a_en="Correct. 48 hours ending with the conclusion of the poll.",
        why_a_ta="சரியானது. வாக்குப்பதிவு முடியும் நேரத்திற்கு முந்தைய 48 மணி நேரம்.",
        why_b_en="Incorrect. Nomination period does not mandate dry days.",
        why_b_ta="தவறானது. மனு தாக்கலின் போது மதுவிலக்கு இல்லை.",
        why_c_en="Incorrect. Counting day dry day is an additional ECI administrative measure, but statutory Section 135C explicitly specifies the 48 hours ending with poll conclusion.",
        why_c_ta="தவறானது. சட்டப்பூர்வ பிரிவு 135C வாக்குப்பதிவு முடியும் முந்தைய 48 மணி நேரத்தைக் குறிக்கிறது.",
        why_d_en="Incorrect. Post-election 3 months is false.",
        why_d_ta="தவறானது. 3 மாத தடை இல்லை.",
        tip_en="Section 135C runs parallel with Section 126 (campaign silence period), both spanning the exact same 48-hour window before poll conclusion.",
        tip_ta="பிரிவு 135C (மது தடை) மற்றும் பிரிவு 126 (பிரச்சார தடை) ஆகிய இரண்டும் ஒரே 48 மணி நேர கால எல்லையைக் கொண்டவை.",
        fact_en="ECI also administratively declares counting day as a Dry Day across the constituency.",
        fact_ta="வாக்கு எண்ணிக்கை நாளையும் தேர்தல் ஆணையம் தனது நிர்வாக அதிகாரத்தால் 'டிரை டே' ஆக அறிவிக்கிறது.",
        tags=["Section 135C", "Dry Day", "48 Hours Liquor Ban", "Election Law"]
    ))

    # ER_H_046
    qs.append(make_er_q(
        qid="ER_H_046", diff="Hard", qtype="Single-Choice", subtopic="Section 169 Rule Making Powers",
        en_stem="Under Section 169 of the Representation of the People Act, 1951, who holds the statutory power to make rules (such as the Conduct of Elections Rules) for carrying out the purposes of the Act, and after consultation with whom?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 169-ன் கீழ், சட்டத்தின் நோக்கங்களை நிறைவேற்றுவதற்கான விதிகளை (தேர்தல் நடத்தை விதிகள் போன்றவை) உருவாக்கும் சட்டப்பூர்வ அதிகாரம் யாரிடம் உள்ளது, மற்றும் யாரைக் கலந்தாலோசித்த பிறகு உருவாக்க வேண்டும்?",
        en_a="The Central Government, after consulting the Election Commission", ta_a="மத்திய அரசு, இந்திய தேர்தல் ஆணையத்தைக் கலந்தாலோசித்த பிறகு",
        en_b="The Election Commission exclusively, without needing any government approval", ta_b="தேர்தல் ஆணையத்திற்கு மட்டுமே, அரசாங்க ஒப்புதல் எதுவும் தேவையின்றி",
        en_c="The Supreme Court of India, under Article 145", ta_c="இந்திய உச்ச நீதிமன்றத்திற்கு, சரத்து 145-ன் கீழ்",
        en_d="The Speaker of the Lok Sabha and Chairman of the Rajya Sabha jointly", ta_d="மக்களவை சபாநாயகர் மற்றும் மாநிலங்களவைத் தலைவர் இணைந்து",
        correct_key="A",
        exp_en="Under Section 169(1) of RPA 1951 (and Section 28 of RPA 1950), the Central Government may, after consulting the Election Commission, by notification in the Official Gazette, make rules for carrying out the purposes of this Act. All rules made must be laid before each House of Parliament for 30 days under Section 169(3).",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 169(1)-ன் படி, தேர்தல் ஆணையத்தைக் கலந்தாலோசித்த பின்னர் மத்திய அரசு அரசிதழில் அறிவிக்கை வெளியிட்டு தேர்தல் விதிகளை உருவாக்கலாம். அவ்வாறு உருவாக்கப்பட்ட விதிகள் நாடாளுமன்றத்தின் இரு அவைகளிலும் 30 நாட்கள் பார்வைக்கு வைக்கப்பட வேண்டும்.",
        why_a_en="Correct. Central Government makes rules in consultation with ECI.",
        why_a_ta="சரியானது. மத்திய அரசு ECI-யைக் கலந்தாலோசித்து விதிகளை இயற்றுகிறது.",
        why_b_en="Incorrect. ECI does not have independent statutory rule-making power; it can only recommend rules to the Law Ministry.",
        why_b_ta="தவறானது. ECI-க்கு சுயமாக விதிகளை இயற்றும் அதிகாரம் இல்லை; பரிந்துரை மட்டுமே செய்ய முடியும்.",
        why_c_en="Incorrect. Article 145 relates to Supreme Court rules for its own procedure.",
        why_c_ta="தவறானது. சரத்து 145 உச்ச நீதிமன்றத்தின் சொந்த நடைமுறை விதிகள் பற்றியது.",
        why_d_en="Incorrect. Presiding officers do not make election conduct rules.",
        why_d_ta="தவறானது. சபாநாயகருக்கு இதில் அதிகாரமில்லை.",
        tip_en="This is why amendments to election rules (like introducing VVPAT, raising expenditure limits, or home voting) are notified by the Union Ministry of Law and Justice.",
        tip_ta="இதனால்தான் VVPAT அறிமுகம், செலவு வரம்பு உயர்வு போன்ற தேர்தல் விதி மாற்றங்களை மத்திய சட்ட அமைச்சகம் அறிவிக்கையாக வெளியிடுகிறது.",
        fact_en="ECI has repeatedly sought independent rule-making powers under Article 324 similar to the Supreme Court under Article 145.",
        fact_ta="உச்ச நீதிமன்றத்தைப் போல தங்களுக்கும் சுயமாக விதி இயற்றும் அதிகாரம் வேண்டும் என ECI அரசிடம் கோரி வருகிறது.",
        tags=["Section 169", "Rule Making Power", "Central Government and ECI", "Conduct of Elections Rules"]
    ))

    # ER_H_047
    qs.append(make_er_q(
        qid="ER_H_047", diff="Hard", qtype="Single-Choice", subtopic="Section 28A Deemed Deputation",
        en_stem="What is the legal significance of Section 28A of the Representation of the People Act, 1951, inserted by Parliament in 1989?",
        ta_stem="1989-ல் நாடாளுமன்றத்தால் சேர்க்கப்பட்ட மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 28A-ன் சட்டப்பூர்வ முக்கியத்துவம் என்ன?",
        en_a="Returning Officers, Presiding Officers, and police on election duty are deemed to be on deputation to the ECI and subject to its direct control, superintendence, and discipline", ta_a="தேர்தல் நடத்தும் அலுவலர்கள் மற்றும் காவல்துறையினர் ECI-ன் நேரடி அயல்பணியில் (Deputation) இருப்பதாகக் கருதப்பட்டு, அதன் கட்டுப்பாடு மற்றும் ஒழுங்கு நடவடிக்கைக்கு உட்படுவர்",
        en_b="Political parties are deemed to be public sector undertakings owned by the President", ta_b="அரசியல் கட்சிகள் அனைத்தும் குடியரசுத் தலைவருக்குச் சொந்தமான பொதுத்துறை நிறுவனங்களாகக் கருதப்படும்",
        en_c="Election Commissioners are deemed to be Members of Parliament entitled to vote in debates", ta_c="தேர்தல் ஆணையர்கள் விவாதங்களில் வாக்களிக்கும் உரிமை கொண்ட நாடாளுமன்ற உறுப்பினர்களாகக் கருதப்படுவர்",
        en_d="All electronic media channels are deemed to be branch offices of Prasar Bharati", ta_d="அனைத்து தனியார் மின்னணு ஊடகங்களும் பிரசார் பாரதியின் கிளை அலுவலகங்களாகக் கருதப்படும்",
        correct_key="A",
        exp_en="Section 28A of RPA 1951 provides that the Returning Officer, Assistant Returning Officer, Presiding Officer, Polling Officer, and any police officer designated for election duties shall be deemed to be on deputation to the Election Commission for the period commencing on the date of notification and ending with declaration of results, and shall be subject to the control, superintendence, and discipline of the Commission.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 28A, தேர்தல் அறிவிக்கை வெளியானது முதல் முடிவுகள் அறிவிக்கப்படும் வரை, அனைத்து தேர்தல் நடத்தும் அலுவலர்கள், வாக்குச்சாவடி ஊழியர்கள் மற்றும் காவல்துறையினர் தேர்தல் ஆணையத்தின் அயல்பணியில் (Deputation) இருப்பதாகக் கருதி, ஆணையத்தின் நேரடி கண்காணிப்பு மற்றும் ஒழுங்கு நடவடிக்கைக்கு உட்பட்டவர்களாக ஆக்குகிறது.",
        why_a_en="Correct. Deemed deputation to ECI with disciplinary authority.",
        why_a_ta="சரியானது. ஒழுங்கு நடவடிக்கை அதிகாரத்துடன் கூடிய ECI அயல்பணி அந்தஸ்து.",
        why_b_en="Incorrect. Political parties are private voluntary associations.",
        why_b_ta="தவறானது. கட்சிகள் பொதுத்துறை நிறுவனங்கள் அல்ல.",
        why_c_en="Incorrect. Commissioners are constitutional executive authorities, not MPs.",
        why_c_ta="தவறானது. ஆணையர்கள் எம்.பி.க்கள் அல்ல.",
        why_d_en="Incorrect. Private media remains independent.",
        why_d_ta="தவறானது. ஊடகங்கள் பிரசார் பாரதியின் கிளை அல்ல.",
        tip_en="Section 28A enables ECI to suspend biased collectors, police superintendents, or returning officers without needing prior permission from state governments.",
        tip_ta="பிரிவு 28A-ன் மூலமே ஒருதலைப்பட்சமாக செயல்படும் மாவட்ட ஆட்சியர்கள் அல்லது காவல்துறை அதிகாரிகளை மாநில அரசின் அனுமதியின்றி ECI-யால் நேரடியாக சஸ்பெண்ட் செய்ய முடிகிறது.",
        fact_en="Section 13CC of RPA 1950 provides an identical deemed deputation provision for Electoral Registration Officers (EROs) preparing electoral rolls.",
        fact_ta="வாக்காளர் பட்டியல் தயாரிக்கும் அதிகாரிகளுக்கும் RPA 1950 பிரிவு 13CC-ன் கீழ் இதேபோன்ற அயல்பணி அந்தஸ்து வழங்கப்பட்டுள்ளது.",
        tags=["Section 28A", "Deemed Deputation", "ECI Disciplinary Control", "1989 Amendment"]
    ))

    # ER_H_048
    qs.append(make_er_q(
        qid="ER_H_048", diff="Hard", qtype="Single-Choice", subtopic="Section 14(b) RPA 1950 Qualifying Dates",
        en_stem="Prior to the 2021 amendment to Section 14(b) of the Representation of the People Act, 1950, what was the sole qualifying date in a calendar year for being registered as a voter?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1950 பிரிவு 14(b)-ல் 2021-ல் செய்யப்பட்ட திருத்தத்திற்கு முன்பு, வாக்காளராகப் பதிவு செய்வதற்கான ஒரே தகுதி தேதியாக ஆண்டின் எந்த நாள் இருந்தது?",
        en_a="1st day of January", ta_a="ஜனவரி 1-ஆம் நாள்",
        en_b="1st day of April", ta_b="ஏப்ரல் 1-ஆம் நாள்",
        en_c="1st day of July", ta_c="ஜூலை 1-ஆம் நாள்",
        en_d="26th day of January", ta_d="ஜனவரி 26-ஆம் நாள்",
        correct_key="A",
        exp_en="Prior to the Election Laws (Amendment) Act, 2021, Section 14(b) of RPA 1950 defined 'qualifying date' strictly as 'the 1st day of January of the year in which the electoral roll is prepared or revised'. The 2021 amendment expanded this single date to four dates: 1st January, 1st April, 1st July, and 1st October.",
        exp_ta="2021 திருத்தத்திற்கு முன், பிரிவு 14(b) 'தகுதி தேதி' என்பதை 'வாக்காளர் பட்டியல் தயாரிக்கப்படும் அல்லது திருத்தப்படும் ஆண்டின் ஜனவரி 1-ஆம் நாள்' என்று மட்டுமே வரையறுத்திருந்தது. 2021 சட்டத்திருத்தம் இதை 4 தேதிகளாக (ஜனவரி 1, ஏப்ரல் 1, ஜூலை 1, அக்டோபர் 1) விரிவுபடுத்தியது.",
        why_a_en="Correct. 1st day of January was the sole qualifying date previously.",
        why_a_ta="சரியானது. முன்பு ஜனவரி 1 மட்டுமே ஒரே தகுதி தேதியாக இருந்தது.",
        why_b_en="Incorrect. April 1 was added in 2021.",
        why_b_ta="தவறானது. ஏப்ரல் 1 2021-ல் சேர்க்கப்பட்டது.",
        why_c_en="Incorrect. July 1 was added in 2021.",
        why_c_ta="தவறானது. ஜூலை 1 2021-ல் சேர்க்கப்பட்டது.",
        why_d_en="Incorrect. January 26 is Republic Day, never a qualifying date.",
        why_d_ta="தவறானது. ஜனவரி 26 குடியரசு தினம்.",
        tip_en="Four qualifying dates ensure that young citizens turning 18 don't have to wait up to an entire year to enroll, drastically reducing disenfranchisement of youth.",
        tip_ta="நான்கு தகுதி தேதிகள் 18 வயதை அடையும் இளைஞர்கள் வாக்காளர் பட்டியலில் சேர ஓராண்டு வரை காத்திருக்க வேண்டிய நிலையை மாற்றியது.",
        fact_en="Advance applications can now be submitted by 17-year-olds in Form 6 before turning 18.",
        fact_ta="தற்போது 17 வயது நிரம்பியவர்களே படிவம் 6 மூலம் முன்கூட்டியே விண்ணப்பிக்க வழிவகை செய்யப்பட்டுள்ளது.",
        tags=["Section 14(b)", "Qualifying Date", "1st January", "2021 Amendment"]
    ))

    # ER_H_049
    qs.append(make_er_q(
        qid="ER_H_049", diff="Hard", qtype="Single-Choice", subtopic="Section 125A Penalties for False Affidavits",
        en_stem="Under Section 125A of the Representation of the People Act, 1951 (inserted in 2002), what is the maximum penalty for a candidate who fails to furnish information in Form 26 or provides false information regarding their criminal antecedents?",
        ta_stem="2002-ல் சேர்க்கப்பட்ட மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 125A-ன் கீழ், படிவம் 26-ல் தகவல்களை மறைக்கும் அல்லது தனது குற்றப்பின்னணி குறித்து தவறான பொய்யான தகவல்களை அளிக்கும் வேட்பாளருக்கு விதிக்கப்படும் அதிகபட்ச தண்டனை என்ன?",
        en_a="Imprisonment for a term which may extend to 6 months, or with fine, or with both", ta_a="6 மாதங்கள் வரை நீட்டிக்கக்கூடிய சிறைத்தண்டனை, அல்லது அபராதம், அல்லது இரண்டும்",
        en_b="Imprisonment for 7 years and a fine of ₹5 Lakhs", ta_b="7 ஆண்டுகள் சிறைத்தண்டனை மற்றும் ₹5 லட்சம் அபராதம்",
        en_c="Immediate lifetime disqualification from contesting any public election", ta_c="எந்தவொரு பொதுத்தேர்தலிலும் போட்டியிட உடனடி வாழ்நாள் தகுதிநீக்கம்",
        en_d="A written apology published at the candidate's expense without any penal sanction", ta_d="எவ்வித குற்றவியல் தண்டனையுமின்றி வேட்பாளர் செலவில் எழுத்துப்பூர்வ மன்னிப்புக் கோருதல்",
        correct_key="A",
        exp_en="Section 125A of RPA 1951 was inserted in 2002 following the Supreme Court's ADR judgment. It provides that a candidate who fails to furnish required affidavit information, conceals information, or gives false information shall be punishable with imprisonment for a term which may extend to 6 months, or with fine, or with both.",
        exp_ta="2002 ADR தீர்ப்பைத் தொடர்ந்து சேர்க்கப்பட்ட பிரிவு 125A, படிவம் 26 உறுதிமொழிப் பத்திரத்தில் தகவல்களை மறைக்கும், பொய்யான தகவல்களை அளிக்கும் வேட்பாளர்களுக்கு 6 மாதம் வரை சிறைத்தண்டனை அல்லது அபராதம் அல்லது இரண்டும் விதிக்கப்படும் என்று கூறுகிறது.",
        why_a_en="Correct. Imprisonment up to 6 months or fine or both under Section 125A.",
        why_a_ta="சரியானது. பிரிவு 125A-ன் கீழ் 6 மாதங்கள் வரை சிறை அல்லது அபராதம்.",
        why_b_en="Incorrect. 7 years is incorrect.",
        why_b_ta="தவறானது. 7 ஆண்டுகள் தவறானது.",
        why_c_en="Incorrect. Lifetime ban does not apply under current law.",
        why_c_ta="தவறானது. தற்போதைய சட்டத்தில் வாழ்நாள் தடை இல்லை.",
        why_d_en="Incorrect. A criminal penalty is explicitly prescribed.",
        why_d_ta="தவறானது. குற்றவியல் தண்டனை உள்ளது.",
        tip_en="ECI and the 244th Law Commission Report recommended enhancing the punishment under Section 125A from 6 months to at least 2 years imprisonment, which would trigger automatic disqualification under Section 8(3).",
        tip_ta="பிரிவு 125A-ன் தண்டனையை 6 மாதத்திலிருந்து 2 ஆண்டாக உயர்த்த வேண்டும் என தேர்தல் ஆணையம் கோரி வருகிறது; அப்போதுதான் பிரிவு 8(3)-ன் கீழ் தானியங்கி தகுதிநீக்கம் அமலாகும்.",
        fact_en="Section 125A offences are tried by the Magistrate's court upon a private complaint or police FIR.",
        fact_ta="பிரிவு 125A குற்றங்கள் மாஜிஸ்திரேட் நீதிமன்றத்தில் விசாரிக்கப்படுகின்றன.",
        tags=["Section 125A", "False Affidavits", "6 Months Penalty", "Form 26 Offence"]
    ))

    # ER_H_050
    qs.append(make_er_q(
        qid="ER_H_050", diff="Hard", qtype="Single-Choice", subtopic="Special Provisions for North Eastern Delimitation",
        en_stem="Under Section 8A of the Representation of the People Act, 1950 (inserted in 2008), which four North-Eastern States had their delimitation postponed due to law and order concerns, requiring a separate presidential order to resume?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1950 பிரிவு 8A-ன் கீழ் (2008-ல் சேர்க்கப்பட்டது), சட்டம்-ஒழுங்கு பிரச்சனைகள் காரணமாக தொகுதி மறுவரையறை ஒத்திவைக்கப்பட்டு, அதை மீண்டும் தொடங்க தனி குடியரசுத் தலைவர் ஆணை தேவைப்படும் நான்கு வடகிழக்கு மாநிலங்கள் எவை?",
        en_a="Assam, Arunachal Pradesh, Manipur, and Nagaland", ta_a="அசாம், அருணாச்சலப் பிரதேசம், மணிப்பூர் மற்றும் நாகாலாந்து",
        en_b="Sikkim, Mizoram, Tripura, and Meghalaya", ta_b="சிக்கிம், மிசோரம், திரிபுரா மற்றும் மேகாலயா",
        en_c="West Bengal, Odisha, Jharkhand, and Bihar", ta_c="மேற்கு வங்காளம், ஒடிசா, ஜார்க்கண்ட் மற்றும் பீகார்",
        en_d="Goa, Puducherry, Delhi, and Chandigarh", ta_d="கோவா, புதுச்சேரி, டெல்லி மற்றும் சண்டிகர்",
        correct_key="A",
        exp_en="Section 8A of RPA 1950 (inserted by the Delimitation Amendment Act, 2008) provided that delimitation in the four north-eastern states of Assam, Arunachal Pradesh, Manipur, and Nagaland was deferred due to local opposition and public order concerns. In February 2020, the Central Government rescinded the deferment orders, and delimitation for Assam was completed in August 2023.",
        exp_ta="2008-ல் சேர்க்கப்பட்ட பிரிவு 8A-ன் கீழ், அசாம், அருணாச்சலப் பிரதேசம், மணிப்பூர் மற்றும் நாகாலாந்து ஆகிய நான்கு வடகிழக்கு மாநிலங்களில் சட்டம் ஒழுங்கு பிரச்சனைகள் காரணமாக தொகுதி மறுவரையறை ஒத்திவைக்கப்பட்டது. பின்னர் 2020-ல் தடை நீக்கப்பட்டு, அசாம் மாநிலத்திற்கான மறுவரையறை 2023 ஆகஸ்டில் நிறைவுற்றது.",
        why_a_en="Correct. Assam, Arunachal Pradesh, Manipur, and Nagaland.",
        why_a_ta="சரியானது. அசாம், அருணாச்சலப் பிரதேசம், மணிப்பூர் மற்றும் நாகாலாந்து.",
        why_b_en="Incorrect. Sikkim and Mizoram completed regular delimitation.",
        why_b_ta="தவறானது. சிக்கிம் மற்றும் மிசோரமில் வழக்கமான மறுவரையறை நடந்தது.",
        why_c_en="Incorrect. Eastern states completed delimitation under the 2002 Commission.",
        why_c_ta="தவறானது. கிழக்கு மாநிலங்கள் 2002 ஆணையத்தால் முடிக்கப்பட்டன.",
        why_d_en="Incorrect. Union territories are not the four NE states.",
        why_d_ta="தவறானது. யூனியன் பிரதேசங்கள் அல்ல.",
        tip_en="Delimitation for the Union Territory of Jammu and Kashmir was conducted separately under a Commission headed by Justice Ranjana Prakash Desai and notified in May 2022.",
        tip_ta="ஜம்மு-காஷ்மீர் மறுவரையறை நீதிபதி ரஞ்சனா பிரகாஷ் தேசாய் தலைமையில் தனியாக நடத்தப்பட்டு 2022 மே மாதம் அறிவிக்கப்பட்டது.",
        fact_en="Section 8A empowers the President to order delimitation in these states as and when normalcy is restored.",
        fact_ta="பிரிவு 8A இயல்பு நிலை திரும்பிய பின் இம்மாநிலங்களில் மறுவரையறை நடத்த குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
        tags=["Section 8A RPA 1950", "North East Delimitation", "Assam Arunachal Manipur Nagaland"]
    ))

    return qs

def main():
    raw_qs = get_hard_questions()
    print(f"Total raw questions: {len(raw_qs)}")
    assert len(raw_qs) == 50, f"Expected 50, got {len(raw_qs)}"
    
    # Check ID sequence
    for idx, q in enumerate(raw_qs, 1):
        expected_id = f"ER_H_{idx:03d}"
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
    
    # Validate with ContentValidator
    validator = ContentValidator()
    report = validator.validate_file(OUTPUT_PATH, expected_count=50, expected_prefix="ER_H_")
    print(report.summary())
    assert report.is_valid, "Validation failed!"

if __name__ == "__main__":
    main()
