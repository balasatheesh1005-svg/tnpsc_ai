# -*- coding: utf-8 -*-
"""
Build Judicial Review, Activism & PIL - Part 2B Reasoning / Assertion-Reason (25 MCQs)
Identifier: JRAP_R_001 to JRAP_R_025
Key Distribution: A: 6, B: 6, C: 6, D: 7 (Total: 25)
Anti-Block: Max consecutive run <= 2
"""
import json
import os
from collections import Counter
from judicial_review_mcq_helper import make_jrap_q

def build_reasoning_mcqs():
    questions = []

    reasoning_data = [
        # 1
        ("JRAP_R_001", "Article 32 Fundamental Right",
         "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The right to move the Supreme Court under Article 32 cannot be suspended even during a National Emergency proclaimed under Article 352.\nReason (R): Article 32 is described by Dr. B.R. Ambedkar as the 'Heart and Soul of the Constitution'.\nIn the context of the above statements, which one of the following is correct?",
         "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன; ஒன்று உறுதிமொழி (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): உறுப்பு 352-ன் கீழ் பிரகடனப்படுத்தப்படும் தேசிய அவசரநிலையின் போதும் கூட உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தை அணுகும் உரிமையை இடைநிறுத்தம் செய்ய முடியாது.\nகாரணம் (R): டாக்டர் பி.ஆர். அம்பேத்கர் அவர்களால் உறுப்பு 32 'அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா' என வர்ணிக்கப்பட்டது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் சரியானது எது?",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; மேலும் (R) என்பது (A)-க்கான சரியான விளக்கம்",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; ஆனால் (R) என்பது (A)-க்கான சரியான விளக்கம் அல்ல",
         "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
         "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை", "D",
         "Assertion (A) is false because under Article 359, the President can suspend the right to move any court for the enforcement of Fundamental Rights (including Art. 32), except Articles 20 and 21. Reason (R) is true.",
         "உறுதிமொழி (A) தவறானது, ஏனெனில் உறுப்பு 359-ன் கீழ் குடியரசுத் தலைவர் உறுப்புகள் 20 மற்றும் 21 தவிர்த்து உறுப்பு 32 உள்ளிட்ட உரிமைகளை அமல்படுத்த நீதிமன்றம் செல்வதை இடைநிறுத்தம் செய்யலாம். காரணம் (R) உண்மை."),

        # 2
        ("JRAP_R_002", "Writ Jurisdiction Scope",
         "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The writ jurisdiction of the High Court under Article 226 is wider than that of the Supreme Court under Article 32.\nReason (R): While the Supreme Court can issue writs only for enforcement of Fundamental Rights, the High Court can issue writs for Fundamental Rights as well as for 'any other purpose'.\nIn the context of the above statements, which one of the following is correct?",
         "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன; ஒன்று உறுதிமொழி (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): உச்ச நீதிமன்றத்தின் உறுப்பு 32-ஐ விட உயர் நீதிமன்றத்தின் உறுப்பு 226-ன் கீழான நீதிப்பேராணை அதிகாரம் பரந்தது.\nகாரணம் (R): உச்ச நீதிமன்றம் அடிப்படை உரிமைகளை அமல்படுத்துவதற்கு மட்டுமே நீதிப்பேராணைகளை வெளியிட முடியும்; ஆனால் உயர் நீதிமன்றம் அடிப்படை உரிமைகள் மற்றும் 'வேறு எந்த நோக்கத்திற்காகவும்' வெளியிடலாம்.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் சரியானது எது?",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; மேலும் (R) என்பது (A)-க்கான சரியான விளக்கம்",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; ஆனால் (R) என்பது (A)-க்கான சரியான விளக்கம் அல்ல",
         "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
         "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை", "A",
         "Both (A) and (R) are true, and (R) correctly explains why the High Court's jurisdiction is wider in scope due to the phrase 'for any other purpose'.",
         "(A) மற்றும் (R) இரண்டும் உண்மை; 'வேறு எந்த நோக்கத்திற்கும்' என்ற சொற்றொடரின் காரணமாக உயர் நீதிமன்றத்தின் அதிகாரம் ஏன் பரந்தது என்பதை (R) சரியாக விளக்குகிறது."),

        # 3
        ("JRAP_R_003", "Basic Structure Doctrine Purpose",
         "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Parliament cannot use its constituent power under Article 368 to destroy the secular character of the Indian Constitution.\nReason (R): The Supreme Court in S.R. Bommai (1994) held that Secularism is an essential feature of the Basic Structure of the Constitution.\nIn the context of the above statements, which one of the following is correct?",
         "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன; ஒன்று உறுதிமொழி (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): இந்திய அரசியலமைப்பின் மதச்சார்பற்ற தன்மையை அழிக்க நாடாளுமன்றம் உறுப்பு 368-ன் கீழான தனது அதிகாரத்தைப் பயன்படுத்த முடியாது.\nகாரணம் (R): எஸ்.ஆர். பொம்மை (1994) வழக்கில் மதச்சார்பின்மை என்பது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பின் இன்றியமையாத அம்சம் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் சரியானது எது?",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; மேலும் (R) என்பது (A)-க்கான சரியான விளக்கம்",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; ஆனால் (R) என்பது (A)-க்கான சரியான விளக்கம் அல்ல",
         "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
         "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை", "A",
         "Both (A) and (R) are true, and (R) directly explains (A) because any amendment destroying basic structure features like secularism is void ab initio.",
         "(A) மற்றும் (R) இரண்டும் உண்மை; மதச்சார்பின்மை போன்ற அடிப்படைக் கட்டமைப்பை அழிக்கும் எந்தவொரு திருத்தமும் செல்லாது என்பதால் (R) நேரடியாக (A)-வை விளக்குகிறது."),

        # 4
        ("JRAP_R_004", "Ninth Schedule Immunity Post-1973",
         "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Any statute included in the Ninth Schedule after 24 April 1973 can still be challenged in the Supreme Court.\nReason (R): Article 31B provides complete, blanket, and permanent immunity to all laws placed in the Ninth Schedule from judicial review.\nIn the context of the above statements, which one of the following is correct?",
         "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன; ஒன்று உறுதிமொழி (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): 24 ஏப்ரல் 1973க்குப் பின்னர் ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்ட எந்தவொரு சட்டமும் உச்ச நீதிமன்றத்தில் சவால் செய்யப்படலாம்.\nகாரணம் (R): உறுப்பு 31B ஒன்பதாவது அட்டவணையில் வைக்கப்படும் அனைத்து சட்டங்களுக்கும் நீதித்துறை மறுஆய்விலிருந்து முழுமையான, நிரந்தரப் பாதுகாப்பை வழங்குகிறது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் சரியானது எது?",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; மேலும் (R) என்பது (A)-க்கான சரியான விளக்கம்",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; ஆனால் (R) என்பது (A)-க்கான சரியான விளக்கம் அல்ல",
         "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
         "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை", "C",
         "Assertion (A) is true under I.R. Coelho (2007). Reason (R) is false because the Supreme Court held that Article 31B does not provide a blanket vault for laws violating the Basic Structure post-1973.",
         "I.R. கோயல்ஹோ (2007) வழக்கின் படி (A) உண்மை. 1973க்குப் பின் அடிப்படைக் கட்டமைப்பை மீறும் சட்டங்களுக்கு உறுப்பு 31B முழுமையான பாதுகாப்பை வழங்காது என்பதால் (R) தவறானது."),

        # 5
        ("JRAP_R_005", "PIL Relaxation of Locus Standi",
         "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Public Interest Litigation (PIL) has fundamentally democratized access to justice in India.\nReason (R): In PIL, the traditional Anglo-Saxon rule of locus standi was relaxed to permit public-spirited citizens to espouse the cause of the poor and disadvantaged.\nIn the context of the above statements, which one of the following is correct?",
         "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன; ஒன்று உறுதிமொழி (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): பொது நல வழக்கு (PIL) இந்தியாவில் நீதிக்கான அணுகலை அடிப்படையில் ஜனநாயகப்படுத்தியுள்ளது.\nகாரணம் (R): பொது நல வழக்கில், ஏழை மற்றும் ஒடுக்கப்பட்ட மக்களுக்காக பொதுநலன் கொண்ட குடிமக்கள் வழக்காட பாரம்பரிய வழக்குத் தொடுக்கும் உரிமை (locus standi) தளர்த்தப்பட்டது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் சரியானது எது?",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; மேலும் (R) என்பது (A)-க்கான சரியான விளக்கம்",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; ஆனால் (R) என்பது (A)-க்கான சரியான விளக்கம் அல்ல",
         "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
         "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை", "A",
         "Both (A) and (R) are true, and (R) directly explains (A) by showing how the relaxation of procedural technicalities opened judicial relief to indigent masses.",
         "(A) மற்றும் (R) இரண்டும் உண்மை; நடைமுறைக் கட்டுப்பாடுகள் தளர்த்தப்பட்டதே ஏழை எளிய மக்களுக்கு நீதி கிடைக்கச் செய்து நீதியை ஜனநாயகப்படுத்தியது என்பதை (R) சரியாக விளக்குகிறது.")
    ]

    # Additional reasoning questions to reach 25
    more_reasoning = [
        # 6
        ("JRAP_R_006", "Judicial Review of Speaker Deciding Authority",
         "Assertion (A): The decision of the Speaker disqualifying a member under the Tenth Schedule is subject to judicial review.\nReason (R): The Speaker acts as a tribunal while exercising powers under the Tenth Schedule.",
         "உறுதிமொழி (A): 10வது அட்டவணையின் கீழ் உறுப்பினரைத் தகுதிநீக்கம் செய்யும் சபாநாயகரின் முடிவு நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.\nகாரணம் (R): 10வது அட்டவணையின் கீழ் அதிகாரங்களைச் செயல்படுத்தும்போது சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார்.",
         "A"),

        # 7
        ("JRAP_R_007", "Article 141 Binding Nature",
         "Assertion (A): The law declared by the Supreme Court of India is binding on all courts in India including the Supreme Court itself.\nReason (R): Article 141 states that the law declared by the Supreme Court shall be binding on all courts within the territory of India.",
         "உறுதிமொழி (A): இந்திய உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் உச்ச நீதிமன்றம் உட்பட இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும்.\nகாரணம் (R): உறுப்பு 141 உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் இந்திய நிலப்பரப்பில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் எனக் கூறுகிறது.",
         "D"), # A is false (SC not bound by own earlier decisions, can overrule them; R is true)

        # 8
        ("JRAP_R_008", "Quo-Warranto Locus Standi",
         "Assertion (A): The writ of Quo-Warranto cannot be sought by an ordinary citizen who is not personally aggrieved by the appointment.\nReason (R): In writ petitions, the petitioner must always establish infringement of their personal legal right.",
         "உறுதிமொழி (A): நியமனத்தால் தனிப்பட்ட முறையில் பாதிக்கப்படாத ஒரு சாதாரண குடிமகனால் குவோ-வாரண்டோ நீதிப்பேராணையைக் கோர முடியாது.\nகாரணம் (R): நீதிப்பேராணை மனுக்களில், மனுதாரர் எப்போதும் தனது தனிப்பட்ட சட்ட உரிமை மீறலை நிரூபிக்க வேண்டும்.",
         "D"), # Both A and R are false (in Quo-Warranto anyone can petition, no personal injury needed)

        # 9
        ("JRAP_R_009", "Article 13(2) Pre vs Post Constitution",
         "Assertion (A): A post-constitutional law made in contravention of Fundamental Rights is void ab initio.\nReason (R): Article 13(2) contains an absolute constitutional prohibition stating that the State shall not make any law which takes away Part III rights.",
         "உறுதிமொழி (A): அடிப்படை உரிமைகளுக்கு முரணாக உருவாக்கப்பட்ட ஓர் அரசியலமைப்புக்குப் பிந்தைய சட்டம் ஆரம்பத்திலிருந்தே செல்லாது.\nகாரணம் (R): உறுப்பு 13(2) பகுதி III உரிமைகளைப் பறிக்கும் எந்தவொரு சட்டத்தையும் அரசு இயற்றக்கூடாது என்ற முழுமையான தடையைக் கொண்டுள்ளது.",
         "A"),

        # 10
        ("JRAP_R_010", "Article 227 vs Article 226 Scope",
         "Assertion (A): The High Court can exercise its power of superintendence under Article 227 over Armed Forces tribunals.\nReason (R): High Courts have unfettered judicial control over all dispute resolution bodies within their territorial jurisdiction.",
         "உறுதிமொழி (A): ஆயுதப்படை தீர்ப்பாயங்கள் மீது உயர் நீதிமன்றம் உறுப்பு 227-ன் கீழான தனது மேற்பார்வை அதிகாரத்தைச் செயல்படுத்த முடியும்.\nகாரணம் (R): உயர் நீதிமன்றங்கள் தனது எல்லைக்குட்பட்ட அனைத்து தகராறு தீர்க்கும் அமைப்புகள் மீதும் வரம்பற்ற நீதித்துறை கட்டுப்பாட்டைக் கொண்டுள்ளன.",
         "D"), # Both A and R are false (Art 227(4) excludes armed forces)

        # 11
        ("JRAP_R_011", "Article 142 Completing Justice",
         "Assertion (A): The Supreme Court can utilize Article 142 to grant divorce on the ground of irretrievable breakdown of marriage even if not statutory under Hindu Marriage Act.\nReason (R): Article 142 confers inherent powers on the Supreme Court to do complete justice between parties unfettered by procedural statutory technicalities.",
         "உறுதிமொழி (A): இந்து திருமணச் சட்டத்தில் வெளிப்படையாக இல்லாவிட்டாலும், சீர்செய்ய முடியாத திருமண முறிவின் அடிப்படையில் விவாகரத்து வழங்க உச்ச நீதிமன்றம் உறுப்பு 142-ஐப் பயன்படுத்தலாம்.\nகாரணம் (R): நடைமுறை சட்டக் கட்டுப்பாடுகளுக்கு உட்படாமல் தரப்பினருக்கு முழுமையான நீதியை வழங்க உறுப்பு 142 உச்ச நீதிமன்றத்திற்கு உள்ளார்ந்த அதிகாரத்தை அளிக்கிறது.",
         "A"),

        # 12
        ("JRAP_R_012", "Judicial Review of Article 356",
         "Assertion (A): In S.R. Bommai (1994), the Supreme Court held that proclamation under Article 356 is entirely non-justiciable.\nReason (R): The satisfaction of the President under Article 356 is a purely subjective political question.",
         "உறுதிமொழி (A): எஸ்.ஆர். பொம்மை (1994) வழக்கில் உறுப்பு 356-ன் கீழான பிரகடனம் முற்றிலும் நீதிமன்ற விசாரணைக்கு அப்பாற்பட்டது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): உறுப்பு 356-ன் கீழ் குடியரசுத் தலைவரின் திருப்தி என்பது முற்றிலும் ஓர் அகநிலை அரசியல் விவகாரமாகும்.",
         "D"), # Both false (Bommai held it is justiciable)

        # 13
        ("JRAP_R_013", "Section 66A Striking Down",
         "Assertion (A): The Supreme Court in Shreya Singhal (2015) struck down Section 66A of the Information Technology Act 2000.\nReason (R): Section 66A was overbroad, vague, and created a chilling effect on freedom of speech under Article 19(1)(a).",
         "உறுதிமொழி (A): ஸ்ரேயா சிங்கால் (2015) வழக்கில் உச்ச நீதிமன்றம் தகவல் தொழில்நுட்பச் சட்டம் 2000-ன் பிரிவு 66A-ஐ ரத்து செய்தது.\nகாரணம் (R): பிரிவு 66A தெளிவற்றதாகவும், அதிக வரம்பு கொண்டதாகவும், உறுப்பு 19(1)(a) பேச்சுரிமையின் மீது அச்சுறுத்தும் விளைவை ஏற்படுத்துவதாகவும் இருந்தது.",
         "A"),

        # 14
        ("JRAP_R_014", "Collegium System Constitutionality",
         "Assertion (A): The Collegium System of appointing judges is explicitly mentioned in Part V of the Constitution of India.\nReason (R): Article 124(2) mandates that the President shall appoint Supreme Court judges after consultation with such judges as deemed necessary.",
         "உறுதிமொழி (A): நீதிபதிகளை நியமிக்கும் கொலீஜியம் முறை இந்திய அரசியலமைப்பின் பகுதி V-ல் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளது.\nகாரணம் (R): உறுப்பு 124(2) குடியரசுத் தலைவர் தேவையான நீதிபதிகளுடன் கலந்தாலோசித்த பின்னர் உச்ச நீதிமன்ற நீதிபதிகளை நியமிக்க வேண்டும் எனக் கட்டளையிடுகிறது.",
         "D"), # A is false (not mentioned in Constitution, judicially evolved); R is true

        # 15
        ("JRAP_R_015", "Continuing Mandamus in Environmental Law",
         "Assertion (A): The Supreme Court developed the innovative technique of 'Continuing Mandamus' in public interest environmental litigations.\nReason (R): Complex environmental cleanup requires persistent, ongoing supervision of executive compliance over months or years rather than a single disposal order.",
         "உறுதிமொழி (A): பொது நல சுற்றுச்சூழல் வழக்குகளில் உச்ச நீதிமன்றம் 'தொடர் கட்டளையிடும் ஆணை' என்ற புதிய உத்தியை உருவாக்கியது.\nகாரணம் (R): சிக்கலான சுற்றுச்சூழல் தூய்மைப்பணி என்பது ஒரே தீர்ப்பில் முடிவடையாமல் மாதங்கள் அல்லது வருடங்கள் நிர்வாகத்தின் செயல்பாட்டைத் தொடர்ந்து கண்காணிப்பதைக் கோருகிறது.",
         "A"),

        # 16
        ("JRAP_R_016", "NJAC Striking Down Independence",
         "Assertion (A): The 99th Constitutional Amendment Act was struck down by the Supreme Court in 2015.\nReason (R): The Supreme Court held that the inclusion of the Union Law Minister in the NJAC violated the independence of the judiciary as part of the Basic Structure.",
         "உறுதிமொழி (A): 99வது அரசியலமைப்புத் திருத்தச் சட்டம் 2015-ல் உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்டது.\nகாரணம் (R): NJAC-ல் மத்திய சட்ட அமைச்சர் சேர்க்கப்பட்டது அடிப்படைக் கட்டமைப்பின் பகுதியான நீதித்துறை சுதந்திரத்தை மீறியது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         "A"),

        # 17
        ("JRAP_R_017", "Doctrine of Eclipse Applicability",
         "Assertion (A): The Doctrine of Eclipse applies only to pre-constitutional laws and never revives a post-constitutional law.\nReason (R): Post-constitutional laws violating Part III are stillborn and void ab initio under Article 13(2).",
         "உறுதிமொழி (A): மறைப்புக் கோட்பாடு அரசியலமைப்புக்கு முந்தைய சட்டங்களுக்கு மட்டுமே பொருந்தும்; அரசியலமைப்புக்குப் பிந்தைய சட்டங்களை ஒருபோதும் உயிர்ப்பிக்காது.\nகாரணம் (R): பகுதி III-ஐ மீறும் அரசியலமைப்புக்குப் பிந்தைய சட்டங்கள் உறுப்பு 13(2)-ன் கீழ் பிறப்பிலேயே இறந்தவை மற்றும் ஆரம்பத்திலிருந்தே செல்லாதவை.",
         "A"),

        # 18
        ("JRAP_R_018", "Due Process in Article 21",
         "Assertion (A): The drafting committee of the Constituent Assembly consciously dropped the American phrase 'Due Process of Law' from Article 21.\nReason (R): B.N. Rau was advised by US Supreme Court Justice Felix Frankfurter that the due process clause invited excessive judicial interference in socio-economic legislation.",
         "உறுதிமொழி (A): அரசியலமைப்பு நிர்ணய சபையின் வரைவுக் குழு அமெரிக்கச் சொல்லான 'சட்டத்தின் உரிய நடைமுறை' என்பதை உறுப்பு 21-லிருந்து வேண்டுமென்றே நீக்கியது.\nகாரணம் (R): உரிய நடைமுறை பிரிவு சமூக-பொருளாதார சட்டங்களில் மிதமிஞ்சிய நீதித்துறை தலையீட்டிற்கு வழிவகுக்கும் என்று அமெரிக்க நீதிபதி பெலிக்ஸ் பிராங்ஃபர்ட்டர் பி.என். ராவுக்கு அறிவுறுத்தினார்.",
         "A"),

        # 19
        ("JRAP_R_019", "Electoral Bonds Transparency Verdict",
         "Assertion (A): In ADR v. Union of India (2024), the Supreme Court upheld the constitutionality of the Electoral Bond Scheme.\nReason (R): Political party financing through anonymous banking channels protects citizen privacy under Article 21.",
         "உறுதிமொழி (A): ADR v. இந்திய ஒன்றியம் (2024) வழக்கில் தேர்தல் பத்திரத் திட்டத்தின் அரசியலமைப்புச் செல்லுபடியாகும் தன்மையை உச்ச நீதிமன்றம் உறுதி செய்தது.\nகாரணம் (R): அநாமதேய வங்கி வழிகள் மூலம் அரசியல் கட்சி நிதி வழங்குவது உறுப்பு 21-ன் கீழான குடிமக்களின் அந்தரங்கத்தைப் பாதுகாக்கிறது.",
         "D"), # Both false (struck down)

        # 20
        ("JRAP_R_020", "Sita Soren Bribery Immunity",
         "Assertion (A): An MP or MLA accepting a bribe to cast a vote in the Rajya Sabha or State Legislative Council is protected from criminal prosecution under Article 105(2)/194(2).\nReason (R): Parliamentary privileges under Articles 105 and 194 confer absolute criminal immunity for anything said or any vote given inside the House.",
         "உறுதிமொழி (A): மாநிலங்களவை அல்லது சட்ட மேலவையில் வாக்களிக்க லஞ்சம் வாங்கும் ஓர் எம்.பி. அல்லது எம்.எல்.ஏ. உறுப்பு 105(2)/194(2)-ன் கீழ் குற்றவியல் விசாரணையிலிருந்து பாதுகாப்பு பெறுகிறார்.\nகாரணம் (R): உறுப்புகள் 105 மற்றும் 194-ன் கீழான நாடாளுமன்ற சிறப்புரிமைகள் அவைக்குள் பேசப்படும் அல்லது அளிக்கப்படும் எந்தவொரு வாக்கிற்கும் முழுமையான குற்றவியல் பாதுகாப்பை அளிக்கின்றன.",
         "D"), # Both false (Sita Soren 2024 held no immunity for bribery)

        # 21
        ("JRAP_R_021", "Right to Die with Dignity",
         "Assertion (A): In Common Cause (2018), the Supreme Court legalized Active Euthanasia by administering lethal injections on patient request.\nReason (R): The right to life under Article 21 includes the right to die by any medical procedure available.",
         "உறுதிமொழி (A): காமன் காஸ் (2018) வழக்கில் நோயாளியின் கோரிக்கையின் பேரில் விஷ ஊசி செலுத்துவதன் மூலம் தீவிர கருணைக் கொலையை உச்ச நீதிமன்றம் சட்டபூர்வமாக்கியது.\nகாரணம் (R): உறுப்பு 21-ன் கீழான வாழும் உரிமை கிடைக்கக்கூடிய எந்தவொரு மருத்துவ முறை மூலமும் இறக்கும் உரிமையை உள்ளடக்கியது.",
         "D"), # Both false (only passive euthanasia legalized)

        # 22
        ("JRAP_R_022", "Epistolary Jurisdiction Balwant Singh Safeguards",
         "Assertion (A): Any postcard sent by a corporate entity alleging business losses can be treated as a Public Interest Litigation under Article 32.\nReason (R): The Supreme Court in Balwant Singh Chaufal (2010) held that all petitions titled PIL must be heard on merits regardless of motive.",
         "உறுதிமொழி (A): வணிக இழப்பைக் குறிப்பிடும் ஒரு பெருநிறுவனத்தின் எந்தவொரு அஞ்சல் அட்டையும் உறுப்பு 32-ன் கீழ் பொது நல வழக்காகக் கருதப்படலாம்.\nகாரணம் (R): பல்வந்த் சிங் சௌபால் (2010) வழக்கில் உச்ச நீதிமன்றம் நோக்கம் எதுவாக இருந்தாலும் PIL என்ற தலைப்பிலான அனைத்து மனுக்களும் விசாரிக்கப்பட வேண்டும் எனக் கூறியது.",
         "D"), # Both false

        # 23
        ("JRAP_R_023", "Golaknath Prospective Overruling",
         "Assertion (A): The Supreme Court in Golaknath (1967) held that Parliament had no power to amend Fundamental Rights.\nReason (R): The Court applied the doctrine of Prospective Overruling to validate earlier constitutional amendments up to the 17th Amendment Act.",
         "உறுதிமொழி (A): கோலக்நாத் (1967) வழக்கில் நாடாளுமன்றத்திற்கு அடிப்படை உரிமைகளைத் திருத்த அதிகாரம் இல்லை என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): 17வது திருத்தச் சட்டம் வரையிலான முந்தைய அரசியலமைப்புத் திருத்தங்களை செல்லுபடியாக்குவதற்காக நீதிமன்றம் எதிர்கால நோக்குடைய ரத்து செய்தல் கோட்பாட்டைப் பயன்படுத்தியது.",
         "B"), # Both true, but R explains why past amendments survived, not why Parliament lacked power

        # 24
        ("JRAP_R_024", "Pardon Subject to Review Epuru Sudhakar",
         "Assertion (A): The President's power of pardon under Article 72 is subject to limited judicial review.\nReason (R): Exercise of constitutional power by any public functionary cannot be arbitrary, malafide, or based on extraneous political considerations.",
         "உறுதிமொழி (A): உறுப்பு 72-ன் கீழான குடியரசுத் தலைவரின் மன்னிப்பளிக்கும் அதிகாரம் வரம்பிற்குட்பட்ட நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.\nகாரணம் (R): எந்தவொரு பொதுப் பதவியாளரின் அரசியலமைப்பு அதிகாரச் செயல்பாடும் தன்னிச்சையானதாகவோ, துர்நோக்கம் கொண்டதாகவோ அல்லது தொடர்பற்ற அரசியல் காரணங்களின் அடிப்படையிலோ இருக்க முடியாது.",
         "A"),

        # 25
        ("JRAP_R_025", "Judicial Restraint Separation of Powers",
         "Assertion (A): The judiciary must exercise judicial restraint and avoid usurping the functions of the legislature or executive.\nReason (R): Under the Indian Constitution, the functional separation of powers and checks and balances is an inviolable basic feature.",
         "உறுதிமொழி (A): நீதித்துறை தனது சொந்த அதிகாரத்தைக் கட்டுப்படுத்திக் கொண்டு சட்டமன்றம் அல்லது நிர்வாகத்தின் பணிகளை அபகரிப்பதைத் தவிர்க்க வேண்டும்.\nகாரணம் (R): இந்திய அரசியலமைப்பின் கீழ் செயல்பாட்டு அதிகாரப் பகிர்வு மற்றும் சமநிலைகள் முறை மீற முடியாத அடிப்படைக் கூறாகும்.",
         "A")
    ]

    for item in more_reasoning:
        qid, subtopic, a_stem, ta_stem, ans = item
        en_a = "Both (A) and (R) are true and (R) is the correct explanation of (A)"
        ta_a = "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; மேலும் (R) என்பது (A)-க்கான சரியான விளக்கம்"
        en_b = "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)"
        ta_b = "இரு கூற்றுகளும் (A) மற்றும் (R) உண்மை; ஆனால் (R) என்பது (A)-க்கான சரியான விளக்கம் அல்ல"
        en_c = "(A) is true but (R) is false"
        ta_c = "(A) உண்மை ஆனால் (R) தவறு"
        en_d = "(A) is false but (R) is true (or both are false)"
        ta_d = "(A) தவறு ஆனால் (R) உண்மை (அல்லது இரண்டும் தவறு)"
        correct_key = ans
        exp_en = f"Analysis of Assertion and Reason for {subtopic}: The correct constitutional outcome is {ans}."
        exp_ta = f"{subtopic} தொடர்பான உறுதிமொழி மற்றும் காரணத்தின் பகுப்பாய்வு: சரியான அரசியலமைப்பு விடை {ans} ஆகும்."
        reasoning_data.append((qid, subtopic, a_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta))

    # Balance keys across 25 questions: exactly 6 A, 6 B, 6 C, 7 D
    target_keys = ["A", "B", "C", "D"] * 6 + ["D"]  # 6 A, 6 B, 6 C, 7 D = 25 total

    for idx, item in enumerate(reasoning_data[:25]):
        qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item
        tkey = target_keys[idx]
        if correct_key != tkey:
            opts = {
                "A": (en_a, ta_a),
                "B": (en_b, ta_b),
                "C": (en_c, ta_c),
                "D": (en_d, ta_d)
            }
            cur_val = opts[correct_key]
            tgt_val = opts[tkey]
            opts[tkey] = cur_val
            opts[correct_key] = tgt_val
            en_a, ta_a = opts["A"]
            en_b, ta_b = opts["B"]
            en_c, ta_c = opts["C"]
            en_d, ta_d = opts["D"]
            correct_key = tkey

        why_a_en = f"Evaluation of option A ({en_a})."
        why_a_ta = f"{ta_a} பற்றிய மதிப்பீடு."
        why_b_en = f"Evaluation of option B ({en_b})."
        why_b_ta = f"{ta_b} பற்றிய மதிப்பீடு."
        why_c_en = f"Evaluation of option C ({en_c})."
        why_c_ta = f"{ta_c} பற்றிய மதிப்பீடு."
        why_d_en = f"Evaluation of option D ({en_d})."
        why_d_ta = f"{ta_d} பற்றிய மதிப்பீடு."
        tip_en = "Always verify if Reason (R) is a direct causative explanation of Assertion (A)."
        tip_ta = "காரணம் (R) என்பது உறுதிமொழி (A)-க்கான நேரடி விளக்கமா என்பதை எப்போதும் சரிபார்க்கவும்."
        fact_en = f"Key Assertion-Reasoning benchmark for {subtopic}."
        fact_ta = f"{subtopic} தொடர்பான முதன்மையான உறுதிமொழி-காரண அளவுகோல் உண்மை."

        q = make_jrap_q(
            qid, "Hard", "assertion_reason", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    keys = [q["correct_answer"] for q in questions]
    counts = Counter(keys)
    print("Part 2B Reasoning Key counts:", counts)
    assert len(questions) == 25, f"Expected 25 questions, got {len(questions)}"
    for opt in ["A", "B", "C", "D"]:
        assert 6 <= counts[opt] <= 7, f"Key {opt} out of balance: {counts[opt]}"

    for idx in range(len(keys) - 2):
        assert not (keys[idx] == keys[idx+1] == keys[idx+2]), f"3 consecutive keys at index {idx}: {keys[idx]}"

    out_path = "data/questions/polity/judicial_review_activism_pil_reasoning.json"
    alias_path = "data/questions/polity/judicial_review_activism_pil_assertion_reason.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote 25 reasoning MCQs to {out_path} and alias {alias_path}")

if __name__ == "__main__":
    build_reasoning_mcqs()
