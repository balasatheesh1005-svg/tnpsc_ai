# -*- coding: utf-8 -*-
"""
State Election & Finance Commissions - Part 2B Reasoning MCQs Generator (25 MCQs: SEFC_R_001 to SEFC_R_025)
TNPSC Nova AI Content Engine
"""
import json
import os
from state_election_finance_commissions_mcq_helper import make_sefc_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator


def get_reasoning_questions():
    raw_data = [
        # 1
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The State Election Commission is an independent constitutional authority separate from the Election Commission of India.\nReason (R): Article 243K and Article 243ZA vest the superintendence, direction, and control of all elections to Panchayats and Municipalities exclusively in the State Election Commission.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மாநில தேர்தல் ஆணையம் என்பது இந்திய தேர்தல் ஆணையத்திலிருந்து தனித்த ஒரு சுதந்திரமான அரசியலமைப்பு அதிகார அமைப்பாகும்.\nகாரணம் (R): சரத்து 243K மற்றும் சரத்து 243ZA ஆகியவை பஞ்சாயத்துகள் மற்றும் நகராட்சிகளுக்கான அனைத்துத் தேர்தல்களின் மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாட்டை மாநில தேர்தல் ஆணையத்திடம் மட்டுமே ஒப்படைக்கின்றன.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct explanation of (A). The State Election Commission is an independent constitutional body created under Articles 243K and 243ZA specifically for local self-governments, completely independent of ECI's Article 324 jurisdiction.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். மாநில தேர்தல் ஆணையம் என்பது சரத்து 324-ன் கீழ் உள்ள இந்திய தேர்தல் ஆணையத்தின் அதிகார வரம்பிற்கு அப்பாற்பட்டு, உள்ளாட்சி அமைப்புகளுக்காக சரத்துகள் 243K மற்றும் 243ZA-ன் கீழ் உருவாக்கப்பட்ட ஒரு சுதந்திரமான அரசியலமைப்பு அமைப்பாகும்.",
            "why_a_en": "Both statements are correct and R provides the constitutional basis for A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் R என்பது A-க்கான அரசியலமைப்பு அடிப்படையை வழங்குகிறது.",
            "why_b_en": "R is indeed the direct constitutional justification for A.",
            "why_b_ta": "R என்பது உண்மையில் A-க்கான நேரடி அரசியலமைப்பு நியாயமாகும்.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "SEC and ECI are separate constitutional entities with distinct jurisdictions.",
            "tip_ta": "SEC மற்றும் ECI ஆகியவை வெவ்வேறு அதிகார வரம்புகளைக் கொண்ட தனித்தனி அரசியலமைப்பு அமைப்புகளாகும்.",
            "fact_en": "ECI conducts Parliament and State Assembly elections; SEC conducts local body elections.",
            "fact_ta": "ECI நாடாளுமன்றம் மற்றும் சட்டமன்றத் தேர்தல்களை நடத்துகிறது; SEC உள்ளாட்சித் தேர்தல்களை நடத்துகிறது."
        },

        # 2
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): A State Election Commissioner cannot be removed from office by an order of the State Council of Ministers.\nReason (R): Under Article 243K(2), the State Election Commissioner enjoys the same constitutional security of tenure as a Judge of a High Court.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மாநில அமைச்சரவையின் உத்தரவின் மூலம் மாநில தேர்தல் ஆணையரை பதவியில் இருந்து நீக்க முடியாது.\nகாரணம் (R): சரத்து 243K(2)-ன் கீழ், மாநில தேர்தல் ஆணையர் ஒரு உயர் நீதிமன்ற நீதிபதிக்கு இணையான அரசியலமைப்புப் பணிப் பாதுகாப்பை அனுபவிக்கிறார்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). Because the SEC can only be removed in like manner and on like grounds as a High Court Judge (impeachment by Parliament), the State Government or Cabinet lacks legal power to dismiss the Commissioner.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். உயர் நீதிமன்ற நீதிபதியைப் போன்ற முறையில் மட்டுமே (நாடாளுமன்ற பதவி நீக்கத் தீர்மானம்) SEC-ஐ நீக்க முடியும் என்பதால், ஆணையரை நீக்க மாநில அரசுக்கோ அல்லது அமைச்சரவைக்கோ சட்டப்பூர்வ அதிகாரம் இல்லை.",
            "why_a_en": "Both statements are correct and R provides the legal basis why the Cabinet cannot dismiss the SEC.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் அமைச்சரவை ஏன் SEC-ஐ நீக்க முடியாது என்பதற்கான சட்ட அடிப்படையை R வழங்குகிறது.",
            "why_b_en": "R is the direct explanation for A.",
            "why_b_ta": "R என்பது A-க்கான நேரடி விளக்கம் ஆகும்.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "High Court Judge removal requires special majority address in both Houses of Parliament.",
            "tip_ta": "உயர் நீதிமன்ற நீதிபதி நீக்கத்திற்கு நாடாளுமன்றத்தின் இரு அவைகளிலும் சிறப்புப் பெரும்பான்மைத் தீர்மானம் தேவை.",
            "fact_en": "Article 243K(2) Proviso 1 safeguards the SEC from political victimization.",
            "fact_ta": "சரத்து 243K(2) வரம்புரை 1 அரசியல் பழிவாங்கல்களிலிருந்து SEC-ஐப் பாதுகாக்கிறது."
        },

        # 3
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The State Finance Commission must review the financial position of both Panchayats and Municipalities.\nReason (R): Article 243Y explicitly provides that the Finance Commission constituted under Article 243-I shall also review the financial position of Municipalities.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மாநில நிதி ஆணையம் பஞ்சாயத்துகள் மற்றும் நகராட்சிகள் ஆகிய இரண்டின் நிதி நிலையையும் மறுஆய்வு செய்ய வேண்டும்.\nகாரணம் (R): சரத்து 243-I-ன் கீழ் அமைக்கப்பட்ட நிதி ஆணையம் நகராட்சிகளின் நிதி நிலையையும் மறுஆய்வு செய்ய வேண்டும் என்று சரத்து 243Y வெளிப்படையாக வகை செய்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the exact constitutional mandate behind (A). Article 243Y cross-applies the commission established under Article 243-I to urban local bodies to avoid duplicating commissions.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். தனித்தனி ஆணையங்களை அமைப்பதைத் தவிர்ப்பதற்காக சரத்து 243-I-ன் கீழ் அமைக்கப்பட்ட அதே ஆணையத்தை சரத்து 243Y நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கும் விரிவுபடுத்துகிறது.",
            "why_a_en": "Both statements are correct and R provides the textual reason for A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் R என்பது A-க்கான சரியான அரசியலமைப்பு விளக்கமாகும்.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "One unified State Finance Commission serves both Part IX (Panchayats) and Part IXA (Municipalities).",
            "tip_ta": "ஒரே ஒருங்கிணைந்த மாநில நிதி ஆணையம் பகுதி IX மற்றும் பகுதி IXA இரண்டிற்கும் சேவை செய்கிறது.",
            "fact_en": "This mirrors the single State Election Commission serving both 243K and 243ZA.",
            "fact_ta": "இது 243K மற்றும் 243ZA ஆகிய இரண்டிற்கும் சேவை செய்யும் ஒற்றை மாநில தேர்தல் ஆணையத்தைப் போன்றது."
        },

        # 4
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Central Finance Commission's recommendations for local bodies are tied to the recommendations of the State Finance Commissions.\nReason (R): Article 280(3)(bb) and Article 280(3)(c) mandate that the Central Finance Commission recommend measures 'on the basis of the recommendations made by the Finance Commission of the State'.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உள்ளாட்சி அமைப்புகளுக்கான மத்திய நிதி ஆணையத்தின் பரிந்துரைகள் மாநில நிதி ஆணையங்களின் பரிந்துரைகளுடன் பிணைக்கப்பட்டுள்ளன.\nகாரணம் (R): சரத்து 280(3)(bb) மற்றும் சரத்து 280(3)(c) ஆகியவை மத்திய நிதி ஆணையம் 'மாநில நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில்' நடவடிக்கைகளை பரிந்துரைக்க வேண்டும் என்று கட்டாயப்படுத்துகின்றன.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct constitutional explanation of (A). The 73rd and 74th Amendments linked the Central FC to the SFCs specifically through the phrase 'on the basis of the recommendations made by the Finance Commission of the State'.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். 73 மற்றும் 74வது திருத்தங்கள் 'மாநில நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில்' என்ற வாசகத்தின் மூலம் மத்திய FC-யை SFC-களுடன் இணைத்தன.",
            "why_a_en": "Both statements are correct and R provides the constitutional grounding for A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் R என்பது A-க்கான அரசியலமைப்பு விளக்கமாகும்.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Art 280(3)(bb) = Panchayats; Art 280(3)(c) = Municipalities.",
            "tip_ta": "சரத்து 280(3)(bb) = பஞ்சாயத்துகள்; சரத்து 280(3)(c) = நகராட்சிகள்.",
            "fact_en": "If an SFC is not constituted, the Central FC assesses state local body needs independently.",
            "fact_ta": "SFC அமைக்கப்படாவிட்டால், மத்திய FC உள்ளாட்சித் தேவைகளை சுயாதீனமாக மதிப்பிடுகிறது."
        },

        # 5
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): High Courts will not entertain writ petitions challenging election nominations once the local body election process has commenced.\nReason (R): Article 243-O(b) places an express constitutional bar on questioning local elections except by an election petition presented after the declaration of results.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உள்ளாட்சித் தேர்தல் செயல்முறை தொடங்கியவுடன் வேட்புமனுக்களை எதிர்த்து தாக்கல் செய்யப்படும் நீதிப்பேராணை மனுக்களை உயர் நீதிமன்றங்கள் விசாரிக்காது.\nகாரணம் (R): சரத்து 243-O(b) தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட பிறகு தாக்கல் செய்யப்படும் தேர்தல் மனு மூலமாகத் தவிர உள்ளாட்சித் தேர்தல்களைக் கேள்விக்குள்ளாக்குவதற்கு வெளிப்படையான அரசியலமைப்புத் தடையை விதிக்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct explanation of (A). Under Article 243-O(b) (and Article 329(b) for general elections), the Supreme Court held in NP Ponnuswami and Kishan Singh Tomar that election process is a continuous chain that cannot be stalled midway by writ petitions under Article 226.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்து 243-O(b)-ன் கீழ் பொன்னுசாமி மற்றும் கிஷன் சிங் தோமர் வழக்குகளில் உச்ச நீதிமன்றம் தேர்தல் என்பது ஒரு தொடர்ச்சியான செயல்முறை என்றும் சரத்து 226-ன் கீழ் நடுவழியில் அதை நிறுத்த முடியாது என்றும் தீர்ப்பளித்தது.",
            "why_a_en": "Both statements are correct and R explains the legal bar behind judicial self-restraint in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-ல் உள்ள நீதிமன்ற சுயக்கட்டுப்பாட்டிற்குப் பின்னால் உள்ள சட்டத் தடையை R விளக்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Interference bar: Challenge ONLY via election petition AFTER declaration of results.",
            "tip_ta": "தலையீட்டுத் தடை: முடிவுகள் அறிவிக்கப்பட்ட பின்னர் தேர்தல் மனு மூலமாக மட்டுமே சவால் செய்ய முடியும்.",
            "fact_en": "Only writ petitions that assist or expedite the holding of elections are entertained.",
            "fact_ta": "தேர்தலை நடத்துவதற்கு உதவும் அல்லது விரைவுபடுத்தும் நீதிப்பேராணை மனுக்கள் மட்டுமே விசாரிக்கப்படுகின்றன."
        },

        # 6
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): In State of AP v. N. Ramesh Kumar (2020), the ordinance reducing the tenure of the State Election Commissioner was declared unconstitutional.\nReason (R): An ordinance cannot be used to circumvent the second proviso to Article 243K(2), which protects the SEC's conditions of service from being varied to his disadvantage.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஆந்திரப் பிரதேச அரசு எதிர் என். ரமேஷ் குமார் (2020) வழக்கில், மாநில தேர்தல் ஆணையரின் பதவிக்காலத்தைக் குறைத்த அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது என அறிவிக்கப்பட்டது.\nகாரணம் (R): சரத்து 243K(2)-ன் இரண்டாவது வரம்புரையை புறக்கணிக்க அவசரச் சட்டத்தைப் பயன்படுத்த முடியாது, இது SEC-ன் பணி நிபந்தனைகள் அவருக்கு பாதகமாக மாற்றப்படுவதிலிருந்து பாதுகாக்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the exact ratio decidendi of (A). The High Court and Supreme Court held that shortening tenure mid-term to remove an incumbent violated the constitutional safeguard against variation of service conditions to disadvantage.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். பதவியில் உள்ளவரை நீக்குவதற்காக பதவிக்காலத்தை பாதியில் குறைப்பது பணி நிபந்தனைகளை பாதகமாக மாற்றக்கூடாது என்ற அரசியலமைப்புப் பாதுகாப்பை மீறுவதாக உயர் நீதிமன்றமும் உச்ச நீதிமன்றமும் தீர்ப்பளித்தன.",
            "why_a_en": "Both statements are correct and R provides the legal ratio of the judgment in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் R என்பது A-ல் உள்ள தீர்ப்பின் சட்ட அடிப்படையை வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Art 243K(2) Proviso 2 protects against indirect removal via tenure truncation.",
            "tip_ta": "சரத்து 243K(2) வரம்புரை 2 பதவிக்காலத்தைக் குறைப்பதன் மூலம் மறைமுகமாக நீக்கப்படுவதிலிருந்து பாதுகாக்கிறது.",
            "fact_en": "The Supreme Court dismissed the State of Andhra Pradesh's appeal and reinstated the Commissioner.",
            "fact_ta": "உச்ச நீதிமன்றம் ஆந்திரப் பிரதேச அரசின் மேல்முறையீட்டை தள்ளுபடி செய்து ஆணையரை மீண்டும் பணியில் அமர்த்தியது."
        },

        # 7
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Village Panchayat elections in Tamil Nadu are strictly non-party elections.\nReason (R): Under the Tamil Nadu Panchayats Act 1994, candidates contesting for Village Panchayat President and Ward Member cannot be allotted symbols reserved for recognized political parties.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): தமிழ்நாட்டில் கிராம பஞ்சாயத்து தேர்தல்கள் முற்றிலும் கட்சி சாரா தேர்தல்களாகும்.\nகாரணம் (R): 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் கீழ், கிராம பஞ்சாயத்து தலைவர் மற்றும் வார்டு உறுப்பினர் பதவிக்கு போட்டியிடும் வேட்பாளர்களுக்கு அங்கீகரிக்கப்பட்ட அரசியல் கட்சிகளுக்கு ஒதுக்கப்பட்ட சின்னங்களை ஒதுக்க முடியாது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct explanation of (A). The statutory mechanism ensuring non-party elections is the prohibition on using recognized political party symbols and allotting only free symbols to contestants.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். கட்சி சாரா தேர்தல்களை உறுதி செய்யும் சட்டப்பூர்வ வழிமுறை என்னவென்றால், அரசியல் கட்சி சின்னங்களைப் பயன்படுத்துவதைத் தடைசெய்து சுயேச்சை சின்னங்களை மட்டுமே போட்டியாளர்களுக்கு ஒதுக்குவதாகும்.",
            "why_a_en": "Both statements are correct and R explains how non-party status is enforced in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-ல் உள்ள கட்சி சாரா நிலை எவ்வாறு செயல்படுத்தப்படுகிறது என்பதை R விளக்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "In TN: Village Panchayat = Non-party. Panchayat Union & District Panchayat = Party-based.",
            "tip_ta": "TN-ல்: கிராம பஞ்சாயத்து = கட்சி சாராதது. ஒன்றியம் & மாவட்டம் = கட்சி சார்ந்தது.",
            "fact_en": "Candidates in Village Panchayat elections choose from a list of free symbols notified by the SEC.",
            "fact_ta": "கிராம பஞ்சாயத்துத் தேர்தலில் வேட்பாளர்கள் SEC அறிவித்த இலவச சின்னங்களின் பட்டியலிலிருந்து தேர்வு செய்கிறார்கள்."
        },

        # 8
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The 15th Finance Commission made online uploading of accounts a mandatory condition for releasing local body grants.\nReason (R): Double-entry accounting and public availability of audited accounts on AuditOnline strengthen financial accountability and eliminate ghost expenditures.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உள்ளாட்சி அமைப்புகளுக்கான மானியங்களை வழங்குவதற்கு இணையத்தில் கணக்குகளைப் பதிவேற்றுவதை 15வது நிதி ஆணையம் ஒரு கட்டாய நிபந்தனையாக்கியது.\nகாரணம் (R): இரட்டைப் பதிவு கணக்கு முறை மற்றும் AuditOnline-ல் தணிக்கை செய்யப்பட்ட கணக்குகள் பொதுமக்களுக்குக் கிடைப்பது நிதிப் பொறுப்புடைமையை வலுப்படுத்துகிறது மற்றும் போலி செலவினங்களை நீக்குகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct explanation of (A). To address poor record-keeping and diversion of funds, the 15th FC tied grant releases to uploaded audited accounts on platforms like AuditOnline and e-GramSwaraj.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். மோசமான கணக்கு பராமரிப்பு மற்றும் நிதி முறைகேடுகளைத் தடுக்க, AuditOnline மற்றும் e-GramSwaraj போன்ற தளங்களில் தணிக்கை செய்யப்பட்ட கணக்குகளைப் பதிவேற்றுவதுடன் மானியங்களை 15வது FC இணைத்தது.",
            "why_a_en": "Both statements are correct and R provides the policy rationale for the condition in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் R என்பது A-ல் உள்ள நிபந்தனைக்கான கொள்கை விளக்கத்தை வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "15th FC conditionality: Grants require timely online audited accounts.",
            "tip_ta": "15வது FC நிபந்தனை: மானியங்களுக்கு சரியான நேரத்தில் இணையத்தில் தணிக்கை செய்யப்பட்ட கணக்குகள் தேவை.",
            "fact_en": "AuditOnline is an initiative of the Ministry of Panchayati Raj.",
            "fact_ta": "AuditOnline என்பது பஞ்சாயத்து ராஜ் அமைச்சகத்தின் ஒரு முன்முயற்சியாகும்."
        },

        # 9
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The recommendations of the State Finance Commission are not legally binding as statutory decrees on the State Government.\nReason (R): Article 243-I(4) requires the State Government to submit an explanatory memorandum stating the action taken or reasons for non-acceptance before the State Legislature.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மாநில நிதி ஆணையத்தின் பரிந்துரைகள் மாநில அரசு மீது சட்டப்பூர்வ ஆணைகளாகக் கட்டுப்படுத்தாது.\nகாரணம் (R): சரத்து 243-I(4) எடுக்கப்பட்ட நடவடிக்கை அல்லது ஏற்காததற்கான காரணங்களைக் கூறும் விளக்கக் குறிப்பை மாநில சட்டமன்றத்தின் முன் மாநில அரசு சமர்ப்பிக்க வேண்டும் என்று கோருகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains (A). The constitutional requirement to submit an explanatory memorandum on action taken confirms that the recommendations are advisory, granting the Government discretion to modify or reject recommendations provided reasons are placed before the legislature.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். எடுக்கப்பட்ட நடவடிக்கை குறித்த விளக்கக் குறிப்பை சமர்ப்பிக்க வேண்டும் என்ற அரசியலமைப்புத் தேவை, பரிந்துரைகள் ஆலோசனைத் தன்மை கொண்டவை என்பதையும், சட்டமன்றத்தின் முன் காரணங்களை வைத்தால் அவற்றை மாற்றவோ அல்லது நிராகரிக்கவோ அரசுக்கு விருப்ப உரிமை உண்டு என்பதையும் உறுதிப்படுத்துகிறது.",
            "why_a_en": "Both statements are correct and R demonstrates the advisory nature described in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-ல் விவரிக்கப்பட்ட ஆலோசனைத் தன்மையை R நிரூபிக்கிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Finance Commission recommendations = Recommendatory. ATR = Mandatory democratic oversight.",
            "tip_ta": "நிதி ஆணையப் பரிந்துரைகள் = ஆலோசனை. ATR = கட்டாய ஜனநாயகக் கண்காணிப்பு.",
            "fact_en": "This structure is identical to Article 281 for the Central Finance Commission in Parliament.",
            "fact_ta": "இந்த கட்டமைப்பு நாடாளுமன்றத்தில் மத்திய நிதி ஆணையத்திற்கான சரத்து 281-ஐப் போன்றது."
        },

        # 10
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Delimitation of wards and rotation of reserved seats for local bodies must be completed prior to the formal issuance of the election notification.\nReason (R): Once the election notification is issued, Article 243-O and 243ZG completely bar judicial challenges that stall the election process.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உள்ளாட்சி அமைப்புகளுக்கான வார்டுகள் மறுவரையறை மற்றும் இடஒதுக்கீடு இடங்களின் சுழற்சி ஆகியவை தேர்தல் அறிவிப்பு முறையாக வெளியிடப்படுவதற்கு முன்பே முடிக்கப்பட வேண்டும்.\nகாரணம் (R): தேர்தல் அறிவிப்பு வெளியிடப்பட்டவுடன், தேர்தல் செயல்முறையை நிறுத்தும் நீதித்துறை சவால்களை சரத்துகள் 243-O மற்றும் 243ZG முழுமையாகத் தடை செய்கின்றன.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct explanation of (A). Because courts cannot intervene once the election is notified under Articles 243-O/243ZG, statutory pre-conditions like delimitation and reservation rotation must be lawfully finalized beforehand to avoid constitutional crises.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்துகள் 243-O/243ZG-ன் கீழ் தேர்தல் அறிவிக்கப்பட்டவுடன் நீதிமன்றங்கள் தலையிட முடியாது என்பதால், மறுவரையறை மற்றும் இடஒதுக்கீடு சுழற்சி போன்ற சட்டப்பூர்வ நிபந்தனைகள் அரசியலமைப்பு நெருக்கடிகளைத் தவிர்க்க முன்கூட்டியே முடிக்கப்பட வேண்டும்.",
            "why_a_en": "Both statements are correct and R explains why delimitation must precede notification.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் தேர்தல் அறிவிப்புக்கு முன் மறுவரையறை ஏன் முடிக்கப்பட வேண்டும் என்பதை R விளக்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Pre-notification: Delimitation challenges can be heard. Post-notification: Bar under 243-O becomes absolute.",
            "tip_ta": "அறிவிப்புக்கு முன்: மறுவரையறை சவால்கள் விசாரிக்கப்படலாம். அறிவிப்புக்கு பின்: 243-O தடை முழுமையாகிறது.",
            "fact_en": "This was reaffirmed in DMK v. State of Tamil Nadu (2020) by the Supreme Court.",
            "fact_ta": "திமுக எதிர் தமிழ்நாடு அரசு (2020) வழக்கில் உச்ச நீதிமன்றத்தால் இது மீண்டும் உறுதிப்படுத்தப்பட்டது."
        },

        # 11
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Governor is constitutionally obligated to provide staff to the State Election Commission upon request.\nReason (R): Article 243K(3) mandates that the Governor shall make available such staff as may be necessary for the discharge of functions conferred on the Commission.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): கோரிக்கையின் பேரில் மாநில தேர்தல் ஆணையத்திற்கு பணியாளர்களை வழங்க ஆளுநர் அரசியலமைப்பு ரீதியாக கடமைப்பட்டுள்ளார்.\nகாரணம் (R): சரத்து 243K(3) ஆணையத்திற்கு வழங்கப்பட்டுள்ள பணிகளைச் செய்வதற்குத் தேவையான பணியாளர்களை ஆளுநர் கிடைக்கச் செய்ய வேண்டும் என்று கட்டாயப்படுத்துகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the exact constitutional text establishing the obligation in (A). The SEC does not maintain a massive permanent staff and depends on requisitioned state personnel during elections.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான அரசியலமைப்பு வாசகமாகும். SEC ஒரு பெரிய நிரந்தர பணியாளர் படையைக் கொண்டிருக்கவில்லை மற்றும் தேர்தலின் போது பெறப்படும் மாநில அரசு ஊழியர்களையே நம்பியுள்ளது.",
            "why_a_en": "Both statements are correct and R provides the constitutional mandate for A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் R என்பது A-க்கான அரசியலமைப்பு கட்டளையை வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Article 243K(3) mirrors Article 324(6) of the Constitution.",
            "tip_ta": "சரத்து 243K(3) அரசியலமைப்பின் சரத்து 324(6)-ஐப் பிரதிபலிக்கிறது.",
            "fact_en": "Officers on election duty are deemed to be on deputation to the SEC and subject to its disciplinary control.",
            "fact_ta": "தேர்தல் பணியில் உள்ள அதிகாரிகள் SEC-க்கு அயல்பணியில் இருப்பதாகக் கருதப்பட்டு அதன் ஒழுங்கு நடவடிக்கைக் கட்டுப்பாட்டிற்கு உட்பட்டவர்கள்."
        },

        # 12
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Under the Tamil Nadu Panchayats Act 1994, the District Collector can initiate proceedings to remove a Village Panchayat President under Section 205.\nReason (R): The District Collector functions as the Inspector of Panchayats with supervisory oversight to check abuse of power and financial misconduct in village panchayats.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் கீழ், பிரிவு 205-ன் படி கிராம பஞ்சாயத்து தலைவரை நீக்கும் நடவடிக்கைகளை மாவட்ட ஆட்சியர் தொடங்க முடியும்.\nகாரணம் (R): கிராம பஞ்சாயத்துகளில் அதிகார துஷ்பிரயோகம் மற்றும் நிதி முறைகேடுகளைக் கண்காணிக்க மாவட்ட ஆட்சியர் பஞ்சாயத்துகளின் ஆய்வாளராக செயல்படுகிறார்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct statutory explanation of (A). Section 205 vests removal powers in the Inspector of Panchayats, who is designated by statutory notification as the District Collector.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். பிரிவு 205 பஞ்சாயத்துகளின் ஆய்வாளருக்கு பதவி நீக்க அதிகாரங்களை வழங்குகிறது, மேலும் மாவட்ட ஆட்சியரே பஞ்சாயத்துகளின் ஆய்வாளராக நியமிக்கப்பட்டுள்ளார்.",
            "why_a_en": "Both statements are correct and R explains the statutory role grounding A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-க்கான சட்டப்பூர்வ பங்கை R விளக்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Section 205 removal requires: Show-cause notice -> Panchayat views recorded by Tahsildar -> Gazette notification.",
            "tip_ta": "பிரிவு 205 பதவி நீக்கத்திற்கு தேவை: விளக்கம் கேட்கும் நோட்டீஸ் -> வட்டாட்சியரால் பஞ்சாயத்து கருத்து பதிவு -> அரசிதழ் அறிவிப்பு.",
            "fact_en": "The removal order of the Collector can be appealed before the State Government under Section 205(12).",
            "fact_ta": "ஆட்சியரின் பதவி நீக்க உத்தரவை எதிர்த்து பிரிவு 205(12)-ன் கீழ் மாநில அரசிடம் மேல்முறையீடு செய்யலாம்."
        },

        # 13
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): In Tamil Nadu's rural devolution pool, Village Panchayats receive a larger share than District Panchayats.\nReason (R): Village Panchayats are responsible for direct delivery of frontline basic civic amenities like street lighting, drinking water supply, and sanitation.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): தமிழ்நாட்டின் ஊரகப் பகிர்வுத் தொகுப்பில், மாவட்ட பஞ்சாயத்துகளை விட கிராம பஞ்சாயத்துகள் அதிகப் பங்கைப் பெறுகின்றன.\nகாரணம் (R): தெருவிளக்கு, குடிநீர் விநியோகம் மற்றும் சுகாதாரம் போன்ற நேரடி அடிப்படை குடிமை வசதிகளை வழங்குவதற்கு கிராம பஞ்சாயத்துகளே பொறுப்பாகும்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct functional explanation of (A). Village Panchayats bear daily operating costs for essential village services and hence receive ~55-60% of the rural devolution pool, while District Panchayats play mainly an advisory role and receive ~8-10%.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். கிராம பஞ்சாயத்துகள் அத்தியாவசிய கிராம சேவைகளுக்கான தினசரி செயல்பாட்டுச் செலவுகளைச் சுமப்பதால் அவை ஊரகப் பகிர்வில் ~55-60% பெறுகின்றன; மாவட்ட பஞ்சாயத்துகள் ஆலோசனைக் குழுக்களாக இருப்பதால் ~8-10% மட்டுமே பெறுகின்றன.",
            "why_a_en": "Both statements are correct and R provides the functional rationale for the financial distribution in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-ல் உள்ள நிதி விநியோகத்திற்கான செயல்பாட்டு காரணத்தை R வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Devolution follows functions: Village Panchayats (~60%) > Panchayat Unions (~32%) > District Panchayats (~8%).",
            "tip_ta": "பகிர்வு பணிகளைப் பின்பற்றுகிறது: கிராம பஞ்சாயத்துகள் (~60%) > ஒன்றியங்கள் (~32%) > மாவட்டங்கள் (~8%).",
            "fact_en": "District Panchayats do not levy taxes directly on citizens.",
            "fact_ta": "மாவட்ட பஞ்சாயத்துகள் நேரடியாக குடிமக்கள் மீது வரிகளை விதிப்பதில்லை."
        },

        # 14
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The total reservation for SCs, STs, and OBCs in local body seats cannot exceed an aggregate ceiling of 50%.\nReason (R): In K. Krishna Murthy (2010) and Vikas Kishanrao Gawali (2021), the Supreme Court ruled that the 50% vertical reservation limit laid down in Indra Sawhney applies strictly to local self-governments.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உள்ளாட்சி அமைப்புகளில் SC, ST மற்றும் OBC-களுக்கான மொத்த இடஒதுக்கீடு 50% என்ற ஒட்டுமொத்த உச்சவரம்பைத் தாண்டக்கூடாது.\nகாரணம் (R): கே. கிருஷ்ண மூர்த்தி (2010) மற்றும் விகாஸ் கிஷன்ராவ் கவாலி (2021) வழக்குகளில், இந்திரா சாஹ்னி வழக்கில் நிர்ணயிக்கப்பட்ட 50% செங்குத்து இடஒதுக்கீடு வரம்பு உள்ளாட்சி அமைப்புகளுக்கும் கண்டிப்பாகப் பொருந்தும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the authoritative constitutional jurisprudence behind (A). The Supreme Court held that political reservation in Panchayats and Municipalities under Articles 243D and 243T is bound by the 50% ceiling.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான நீதித்துறை விளக்கமாகும். சரத்துகள் 243D மற்றும் 243T-ன் கீழ் பஞ்சாயத்துகள் மற்றும் நகராட்சிகளில் உள்ள அரசியல் இடஒதுக்கீடு 50% உச்சவரம்பிற்கு கட்டுப்பட்டது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "Both statements are correct and R provides the judicial authority establishing A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-வை நிறுவிய நீதித்துறை அதிகாரத்தை R வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Local body OBC reservation requires satisfying the 'Triple Test' without breaching the 50% cap.",
            "tip_ta": "உள்ளாட்சி OBC இடஒதுக்கீட்டிற்கு 50% வரம்பை மீறாமல் 'மூன்று கட்ட சோதனையை' பூர்த்தி செய்ய வேண்டும்.",
            "fact_en": "Horizontal reservation for women (up to 50%) is permissible as it is not vertical reservation.",
            "fact_ta": "பெண்களுக்கான கிடைமட்ட இடஒதுக்கீடு (50% வரை) செங்குத்து இடஒதுக்கீடு அல்ல என்பதால் அனுமதிக்கப்படுகிறது."
        },

        # 15
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): State Finance Commissions are endowed with the powers of a Civil Court under the Code of Civil Procedure, 1908.\nReason (R): To determine fair devolution, the SFC must have legal authority to summon witnesses, examine documents on oath, and requisition verified public financial records.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மாநில நிதி ஆணையங்கள் சிவில் நடைமுறைச் சட்டம் 1908-ன் கீழ் ஒரு சிவில் நீதிமன்றத்தின் அதிகாரங்களைக் கொண்டுள்ளன.\nகாரணம் (R): நியாயமான நிதிப் பகிர்வை தீர்மானிக்க, சாட்சிகளை அழைக்கவும், சத்தியப்பிரமாணத்தின் கீழ் ஆவணங்களை ஆய்வு செய்யவும், சரிபார்க்கப்பட்ட பொது நிதிப் பதிவுகளை கோரவும் SFC-க்கு சட்டப்பூர்வ அதிகாரம் இருக்க வேண்டும்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains the rationale for (A). State Finance Commission statutes (such as Section 241 of TN Panchayats Act 1994) confer civil court powers so the commission can compel production of true local and state accounting data.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். மாநில நிதி ஆணையச் சட்டங்கள் (1994 TN பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 241 போன்றவை) உள்ளாட்சி மற்றும் மாநில கணக்குத் தரவுகளைப் பெறுவதை உறுதி செய்ய சிவில் நீதிமன்ற அதிகாரங்களை வழங்குகின்றன.",
            "why_a_en": "Both statements are correct and R justifies the grant of civil court powers in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-ல் சிவில் நீதிமன்ற அதிகாரங்கள் வழங்கப்பட்டதை R நியாயப்படுத்துகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "SFC has CPC 1908 civil court powers for inquiries and data discovery.",
            "tip_ta": "விசாரணைகள் மற்றும் தரவுகளைப் பெற SFC-க்கு CPC 1908 சிவில் நீதிமன்ற அதிகாரங்கள் உள்ளன.",
            "fact_en": "Proceedings before the SFC are deemed judicial proceedings under Section 193 of the IPC.",
            "fact_ta": "SFC-ன் முன் நடைபெறும் நடவடிக்கைகள் IPC பிரிவு 193-ன் கீழ் நீதித்துறை நடவடிக்கைகளாகக் கருதப்படுகின்றன."
        },

        # 16
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The State Election Commissioner is appointed by the Governor of the State.\nReason (R): The State Election Commissioner holds office during the pleasure of the Governor.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மாநில தேர்தல் ஆணையர் மாநில ஆளுநரால் நியமிக்கப்படுகிறார்.\nகாரணம் (R): மாநில தேர்தல் ஆணையர் ஆளுநரின் விருப்பம் உள்ளவரை பதவியில் இருப்பார்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is true because Article 243K(1) vests appointment in the Governor. Reason (R) is false because the SEC does NOT hold office during the pleasure of the Governor; under Article 243K(2), removal is only possible through Parliamentary impeachment like a High Court Judge.",
            "exp_ta": "கூற்று (A) உண்மை, ஏனெனில் சரத்து 243K(1) ஆளுநருக்கு நியமன அதிகாரத்தை வழங்குகிறது. காரணம் (R) தவறு, ஏனெனில் SEC ஆளுநரின் விருப்பம் உள்ளவரை பதவியில் இருக்க மாட்டார்; சரத்து 243K(2)-ன் கீழ், உயர் நீதிமன்ற நீதிபதியைப் போன்ற நாடாளுமன்ற பதவி நீக்கம் மூலமாக மட்டுமே அவரை நீக்க முடியும்.",
            "why_a_en": "Assertion is true under 243K(1), but Reason is false because pleasure doctrine does not apply to SEC.",
            "why_a_ta": "கூற்று 243K(1)-ன் கீழ் உண்மை, ஆனால் ஆளுநரின் விருப்பக் கோட்பாடு SEC-க்கு பொருந்தாது என்பதால் காரணம் தவறு.",
            "why_b_en": "Reason is false.",
            "why_b_ta": "காரணம் தவறு.",
            "why_c_en": "Reason is false.",
            "why_c_ta": "காரணம் தவறு.",
            "why_d_en": "Assertion is true.",
            "why_d_ta": "கூற்று உண்மை.",
            "tip_en": "SEC does NOT hold office during pleasure of Governor (enjoys fixed constitutional tenure).",
            "tip_ta": "SEC ஆளுநரின் விருப்பம் உள்ளவரை பதவியில் இருக்க மாட்டார் (நிலையான அரசியலமைப்புப் பதவிக்காலம்).",
            "fact_en": "Governor appoints, but cannot dismiss the SEC at will.",
            "fact_ta": "ஆளுநர் நியமிக்கிறார், ஆனால் விருப்பப்படி SEC-ஐ நீக்க முடியாது."
        },

        # 17
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Central Finance Commission grants to local bodies are paid as non-repayable grants-in-aid from the Consolidated Fund of India.\nReason (R): Local bodies are legally prohibited from borrowing funds or issuing municipal bonds in financial markets.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உள்ளாட்சி அமைப்புகளுக்கான மத்திய நிதி ஆணைய மானியங்கள் இந்திய தொகுப்பு நிதியிலிருந்து திருப்பிச் செலுத்தத் தேவையில்லாத உதவி மானியங்களாக வழங்கப்படுகின்றன.\nகாரணம் (R): நிதிச் சந்தைகளில் உள்ளாட்சி அமைப்புகள் கடன் வாங்கவோ அல்லது நகராட்சிப் பத்திரங்களை வெளியிடவோ சட்டப்படி தடை செய்யப்பட்டுள்ளது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is true because local body grants are non-repayable grants under Article 275(1). Reason (R) is false because creditworthy urban local bodies (like Ahmedabad, Pune, and Chennai) are legally permitted to issue Municipal Bonds under SEBI regulations to finance infrastructure.",
            "exp_ta": "கூற்று (A) உண்மை, ஏனெனில் உள்ளாட்சி மானியங்கள் சரத்து 275(1)-ன் கீழ் திருப்பிச் செலுத்தத் தேவையில்லாத மானியங்கள் ஆகும். காரணம் (R) தவறு, ஏனெனில் நிதி வலிமை கொண்ட நகர்ப்புற உள்ளாட்சிகள் உள்கட்டமைப்புக்காக SEBI விதிகளின் கீழ் நகராட்சிப் பத்திரங்களை வெளியிட சட்டப்படி அனுமதிக்கப்படுகின்றன.",
            "why_a_en": "A is true, but R is false because municipal bonds are legally permitted.",
            "why_a_ta": "A உண்மை, ஆனால் நகராட்சிப் பத்திரங்கள் சட்டப்படி அனுமதிக்கப்படுவதால் R தவறு.",
            "why_b_en": "R is false.",
            "why_b_ta": "R தவறு.",
            "why_c_en": "R is false.",
            "why_c_ta": "R தவறு.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Municipal bonds are a recognized innovative financing instrument under SEBI regulations.",
            "tip_ta": "நகராட்சிப் பத்திரங்கள் SEBI விதிகளின் கீழ் அங்கீகரிக்கப்பட்ட ஒரு புதுமையான நிதித் திரட்டும் கருவியாகும்.",
            "fact_en": "Bangalore was the first city in India to issue municipal bonds in 1997.",
            "fact_ta": "1997-ல் நகராட்சிப் பத்திரங்களை வெளியிட்ட இந்தியாவின் முதல் நகரம் பெங்களூரு ஆகும்."
        },

        # 18
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The State Election Commission can unilaterally cancel an election if booth capturing takes place in a polling station.\nReason (R): Article 243K vests the State Election Commission with plenary powers of superintendence, direction, and control over local elections.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஒரு வாக்குச்சாவடியில் வாக்குச்சாவடி கைப்பற்றப்பட்டால் மாநில தேர்தல் ஆணையம் ஒருதலைப்பட்சமாக தேர்தலை ரத்து செய்ய முடியும்.\nகாரணம் (R): சரத்து 243K உள்ளாட்சித் தேர்தல்களின் மீது மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாட்டின் முழுமையான அதிகாரங்களை மாநில தேர்தல் ஆணையத்திற்கு வழங்குகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct constitutional explanation of (A). The plenary power under Article 243K allows the SEC to adjourn polls, order fresh repolls, or countermand polluted elections to ensure purity of the ballot.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்து 243K-ன் கீழான முழுமையான அதிகாரம் வாக்குப்பதிவை ஒத்திவைக்கவும், மறுவாக்குப்பதிவுக்கு உத்தரவிடவும் அல்லது வாக்குப்பதிவின் தூய்மையை உறுதி செய்ய முறைகேடான தேர்தலை ரத்து செய்யவும் SEC-க்கு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Both statements are correct and R provides the constitutional source of power for A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-க்கான அரசியலமைப்பு அதிகாரத்தின் ஆதாரத்தை R வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Superintendence, direction, and control includes countermanding polls during violence.",
            "tip_ta": "மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாடு என்பது வன்முறையின் போது தேர்தலை ரத்து செய்வதையும் உள்ளடக்கியது.",
            "fact_en": "This power mirrors ECI's authority under Section 58A of the RPA 1951.",
            "fact_ta": "இந்த அதிகாரம் RPA 1951 பிரிவு 58A-ன் கீழ் ECI-ன் அதிகாரத்தைப் பிரதிபலிக்கிறது."
        },

        # 19
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Under the Tamil Nadu Panchayats Act 1994, election petitions challenging panchayat elections are tried by the Principal District Judge.\nReason (R): High Courts have no power under Article 226 to hear appeals against the final orders passed by the District Judge in election petitions.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் கீழ், பஞ்சாயத்து தேர்தல்களை எதிர்க்கும் தேர்தல் மனுக்கள் முதன்மை மாவட்ட நீதிபதியால் விசாரிக்கப்படுகின்றன.\nகாரணம் (R): தேர்தல் மனுக்களில் மாவட்ட நீதிபதி பிறப்பித்த இறுதி உத்தரவுகளுக்கு எதிரான மேல்முறையீடுகளை விசாரிக்க சரத்து 226-ன் கீழ் உயர் நீதிமன்றங்களுக்கு அதிகாரம் இல்லை.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is true under Section 258 of the TN Panchayats Act 1994. Reason (R) is false because High Courts possess constitutional supervisory and appellate powers under Article 226 and 227 to judicially review final decisions of election tribunals.",
            "exp_ta": "கூற்று (A) 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 258-ன் கீழ் உண்மை. காரணம் (R) தவறு, ஏனெனில் தேர்தல் தீர்ப்பாயங்களின் இறுதி முடிவுகளை மறுஆய்வு செய்ய சரத்துகள் 226 மற்றும் 227-ன் கீழ் உயர் நீதிமன்றங்களுக்கு அரசியலமைப்பு மேற்பார்வை மற்றும் மேல்முறையீட்டு அதிகாரங்கள் உள்ளன.",
            "why_a_en": "A is true under Section 258, but R is false because High Court writ jurisdiction over tribunals cannot be ousted.",
            "why_a_ta": "A பிரிவு 258-ன் கீழ் உண்மை, ஆனால் தீர்ப்பாயங்கள் மீதான உயர் நீதிமன்ற அதிகாரத்தை நீக்க முடியாது என்பதால் R தவறு.",
            "why_b_en": "R is false.",
            "why_b_ta": "R தவறு.",
            "why_c_en": "R is false.",
            "why_c_ta": "R தவறு.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Judicial review under Articles 226/227 is part of the basic structure and cannot be excluded.",
            "tip_ta": "சரத்துகள் 226/227-ன் கீழான நீதித்துறை மறுஆய்வு அடிப்படை கட்டமைப்பின் ஒரு பகுதியாகும், அதை விலக்க முடியாது.",
            "fact_en": "Section 258(8) explicitly provides for revisions/appeals before the High Court.",
            "fact_ta": "பிரிவு 258(8) உயர் நீதிமன்றத்தில் மேல்முறையீடுகளுக்கு வெளிப்படையாக வகை செய்கிறது."
        },

        # 20
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The State Finance Commission recommends taxes and duties that may be assigned to local bodies.\nReason (R): Local bodies lack any independent taxation powers unless explicitly authorized by the State Legislature by law.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உள்ளாட்சி அமைப்புகளுக்கு ஒதுக்கப்படக்கூடிய வரிகள் மற்றும் தீர்வைகளை மாநில நிதி ஆணையம் பரிந்துரைக்கிறது.\nகாரணம் (R): மாநில சட்டமன்றத்தால் சட்டத்தின் மூலம் வெளிப்படையாக அங்கீகரிக்கப்படாவிட்டால் உள்ளாட்சி அமைப்புகளுக்கு எந்தவொரு சுதந்திரமான வரிவிதிப்பு அதிகாரமும் இல்லை.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct explanation of (A). Under Articles 243H and 243X, local bodies derive all taxation powers from the State Legislature, which is why the SFC advises the Legislature on which specific taxes should be statutorily assigned to them.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்துகள் 243H மற்றும் 243X-ன் கீழ் உள்ளாட்சி அமைப்புகள் அனைத்து வரி அதிகாரங்களையும் மாநில சட்டமன்றத்திலிருந்தே பெறுகின்றன, அதனால்தான் எந்த குறிப்பிட்ட வரிகளை சட்டப்பூர்வமாக ஒதுக்க வேண்டும் என்று SFC சட்டமன்றத்திற்கு ஆலோசனை கூறுகிறது.",
            "why_a_en": "Both statements are correct and R provides the constitutional basis for the assignment function in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-ல் உள்ள ஒதுக்கீட்டுப் பணிக்கான அரசியலமைப்பு அடிப்படையை R வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Articles 243H (Panchayats) & 243X (Municipalities): Powers to impose taxes are delegated by State law.",
            "tip_ta": "சரத்துகள் 243H (பஞ்சாயத்துகள்) & 243X (நகராட்சிகள்): வரி விதிக்கும் அதிகாரங்கள் மாநில சட்டத்தால் வழங்கப்படுகின்றன.",
            "fact_en": "Assigned taxes include surcharges on stamp duty and entertainment tax.",
            "fact_ta": "ஒதுக்கப்பட்ட வரிகளில் முத்திரைத் தாள் கூடுதல் கட்டணம் மற்றும் கேளிக்கை வரி ஆகியவை அடங்கும்."
        },

        # 21
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The State Election Commission conducts elections to the offices of Mayor and Municipal Chairpersons.\nReason (R): Article 243ZA vests the conduct of all elections to Municipalities in the State Election Commission.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மேயர் மற்றும் நகராட்சித் தலைவர் பதவிகளுக்கான தேர்தல்களை மாநில தேர்தல் ஆணையம் நடத்துகிறது.\nகாரணம் (R): சரத்து 243ZA நகராட்சிகளுக்கான அனைத்துத் தேர்தல்களையும் நடத்தும் அதிகாரத்தை மாநில தேர்தல் ஆணையத்திடம் ஒப்படைக்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct constitutional explanation of (A). Article 243ZA mandates that all municipal elections (whether direct or indirect) fall under the exclusive jurisdiction of the SEC.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்து 243ZA அனைத்து நகராட்சித் தேர்தல்களும் (நேரடி அல்லது மறைமுக) SEC-ன் பிரத்யேக அதிகார வரம்பிற்குள் வருவதை கட்டாயப்படுத்துகிறது.",
            "why_a_en": "Both statements are correct and R provides the constitutional authority for A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-க்கான அரசியலமைப்பு அதிகாரத்தை R வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "All municipal elections = Article 243ZA -> SEC.",
            "tip_ta": "அனைத்து நகராட்சித் தேர்தல்களும் = சரத்து 243ZA -> SEC.",
            "fact_en": "Indirect elections for Mayors are supervised by Returning Officers authorized by the SEC.",
            "fact_ta": "மேயர்களுக்கான மறைமுகத் தேர்தல்கள் SEC-ஆல் அங்கீகரிக்கப்பட்ட தேர்தல் நடத்தும் அதிகாரிகளால் மேற்பார்வையிடப்படுகின்றன."
        },

        # 22
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): State Finance Commissions recommend creating dedicated Incentive Funds for local bodies.\nReason (R): Performance-linked grants encourage local bodies to mobilize their own tax revenues and achieve high property tax collection efficiency.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உள்ளாட்சி அமைப்புகளுக்காக பிரத்யேக ஊக்க நிதிகளை உருவாக்க மாநில நிதி ஆணையங்கள் பரிந்துரைக்கின்றன.\nகாரணம் (R): செயல்திறன் அடிப்படையிலான மானியங்கள் உள்ளாட்சி அமைப்புகள் தங்கள் சொந்த வரி வருவாயைத் திரட்டவும் அதிக சொத்து வரி வசூல் திறனை அடையவும் ஊக்குவிக்கின்றன.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct policy explanation of (A). Incentive funds prevent dependency on state handouts by rewarding panchayats and municipalities that actively revise assessments and collect own source revenues.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான கொள்கை விளக்கம். சொந்த வருவாயை தீவிரமாக திரட்டும் உள்ளாட்சி அமைப்புகளுக்கு வெகுமதி அளிப்பதன் மூலம் மாநில உதவியை மட்டுமே சார்ந்திருப்பதை ஊக்க நிதிகள் தடுக்கின்றன.",
            "why_a_en": "Both statements are correct and R provides the economic rationale for A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-க்கான பொருளாதார நியாயத்தை R வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Incentive Fund = Performance-based reward for local tax mobilization.",
            "tip_ta": "ஊக்க நிதி = உள்ளூர் வரி திரட்டலுக்கான செயல்திறன் அடிப்படையிலான வெகுமதி.",
            "fact_en": "Tamil Nadu SFCs allocate a portion of the devolution pool to an Incentive Fund.",
            "fact_ta": "தமிழ்நாடு SFC-கள் பகிர்வுத் தொகுப்பின் ஒரு பகுதியை ஊக்க நிதிக்கு ஒதுக்குகின்றன."
        },

        # 23
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The State Election Commissioner can be suspended by a written order of the District Collector.\nReason (R): District Collectors are designated as District Election Officers subordinate to the State Election Commission.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மாவட்ட ஆட்சியரின் எழுத்துப்பூர்வ உத்தரவின் மூலம் மாநில தேர்தல் ஆணையரை சஸ்பெண்ட் செய்ய முடியும்.\nகாரணம் (R): மாவட்ட ஆட்சியர்கள் மாநில தேர்தல் ஆணையத்திற்கு உட்பட்ட மாவட்ட தேர்தல் அதிகாரிகளாக நியமிக்கப்பட்டுள்ளனர்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is completely false because the SEC is a high constitutional authority protected under Article 243K(2) and cannot be suspended by any administrative officer. Reason (R) is true because District Collectors function as DEOs under the superintendence of the SEC.",
            "exp_ta": "கூற்று (A) முற்றிலும் தவறு, ஏனெனில் SEC என்பது சரத்து 243K(2)-ன் கீழ் பாதுகாக்கப்பட்ட ஒரு உயர் அரசியலமைப்பு அதிகாரம் மற்றும் எந்தவொரு நிர்வாக அதிகாரியாலும் அவரை சஸ்பெண்ட் செய்ய முடியாது. காரணம் (R) உண்மை, ஏனெனில் மாவட்ட ஆட்சியர்கள் SEC-ன் மேற்பார்வையின் கீழ் DEO-க்களாக செயல்படுகிறார்கள்.",
            "why_a_en": "A is false because SEC cannot be suspended by subordinate officers, while R is true.",
            "why_a_ta": "துணை அதிகாரிகளால் SEC-ஐ சஸ்பெண்ட் செய்ய முடியாது என்பதால் A தவறு, அதே சமயம் R உண்மை.",
            "why_b_en": "A is false.",
            "why_b_ta": "A தவறு.",
            "why_c_en": "A is false.",
            "why_c_ta": "A தவறு.",
            "why_d_en": "A is false.",
            "why_d_ta": "A தவறு.",
            "tip_en": "SEC enjoys High Court Judge status; subordinate civil servants report TO the SEC.",
            "tip_ta": "SEC உயர் நீதிமன்ற நீதிபதி அந்தஸ்தை அனுபவிக்கிறார்; அரசு அதிகாரிகள் SEC-க்கு அறிக்கை செய்கிறார்கள்.",
            "fact_en": "DEOs carry out the directions issued by the SEC during local elections.",
            "fact_ta": "உள்ளாட்சித் தேர்தல்களின் போது SEC பிறப்பிக்கும் உத்தரவுகளை DEO-க்கள் செயல்படுத்துகின்றனர்."
        },

        # 24
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): In Tamil Nadu, the term of the State Election Commissioner is fixed at two years by statutory rules.\nReason (R): The Commissioner is eligible for reappointment for two successive terms subject to the age limit of 65 years.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): தமிழ்நாட்டில் சட்ட விதிகளின்படி மாநில தேர்தல் ஆணையரின் பதவிக்காலம் இரண்டு ஆண்டுகள் என நிர்ணயிக்கப்பட்டுள்ளது.\nகாரணம் (R): 65 வயது வரம்பிற்கு உட்பட்டு ஆணையர் அடுத்தடுத்த இரண்டு முறை மறுநியமனம் செய்ய தகுதியுடையவர்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "B",
            "exp_en": "Both (A) and (R) are true, but (R) is not the causal explanation of (A). Both statements describe distinct statutory provisions of the Tamil Nadu State Election Commissioner Conditions of Service Rules, 1994 (initial 2-year tenure and reappointment clause up to age 65).",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல. இரண்டு கூற்றுகளும் 1994 தமிழ்நாடு மாநில தேர்தல் ஆணையர் பணி நிபந்தனைகள் விதிகளின் வெவ்வேறு சட்ட விதிகளை விவரிக்கின்றன (ஆரம்ப 2 ஆண்டு பதவிக்காலம் மற்றும் 65 வயது வரை மறுநியமன விதி).",
            "why_a_en": "Both are true, but R is an additional provision rather than the causal explanation of A.",
            "why_a_ta": "இரண்டும் உண்மை, ஆனால் R என்பது A-க்கான காரணம் அல்ல, கூடுதல் விதியாகும்.",
            "why_b_en": "Both statements are factually and legally true independently.",
            "why_b_ta": "இரண்டு கூற்றுகளும் தனித்தனியாக உண்மை.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "TN SEC tenure: 2 years initial term, renewable twice up to age 65.",
            "tip_ta": "TN SEC பதவிக்காலம்: தொடக்கத்தில் 2 ஆண்டுகள், 65 வயது வரை இரண்டு முறை புதுப்பிக்கத்தக்கது.",
            "fact_en": "Section 239 of TN Panchayats Act 1994 empowers framing these rules.",
            "fact_ta": "1994 TN பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 239 இந்த விதிகளை உருவாக்க அதிகாரம் அளிக்கிறது."
        },

        # 25
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Devolution of State's Own Tax Revenue (SOTR) creates greater revenue certainty for local bodies than discretionary grants.\nReason (R): Being linked to the aggregate tax collections of the State, SOTR transfers expand automatically with macroeconomic growth and are distributed through statutory formulas.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மாநிலத்தின் சொந்த வரி வருவாய் (SOTR) பகிர்வு விருப்ப மானியங்களை விட உள்ளாட்சி அமைப்புகளுக்கு அதிக வருவாய் நிச்சயத்தன்மையை உருவாக்குகிறது.\nகாரணம் (R): மாநிலத்தின் ஒட்டுமொத்த வரி வசூலுடன் இணைக்கப்பட்டுள்ளதால், SOTR பகிர்வுகள் பொருளாதார வளர்ச்சியுடன் தானாக விரிவடைகின்றன மற்றும் சட்டப்பூர்வ சூத்திரங்கள் மூலம் விநியோகிக்கப்படுகின்றன.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the economic rationale behind (A). Formula-based tax-sharing provides buoyancy and insulates local councils from unpredictable political favoritism in annual budget allocations.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான பொருளாதார விளக்கமாகும். சூத்திர அடிப்படையிலான வரிப் பகிர்வு நிதி விரிவாக்கத்தை வழங்குகிறது மற்றும் வருடாந்திர பட்ஜெட் ஒதுக்கீடுகளில் அரசியல் பாகுபாடுகளிலிருந்து உள்ளாட்சி அமைப்புகளைப் பாதுகாக்கிறது.",
            "why_a_en": "Both statements are correct and R explains the fiscal buoyancy principle in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் சரியானவை மற்றும் A-ல் உள்ள நிதி விரிவாக்கக் கொள்கையை R விளக்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Tax sharing = Buoyant, formulaic, predictable. Discretionary grants = Volatile, political, conditional.",
            "tip_ta": "வரிப் பகிர்வு = நிலையானது, கணிக்கக்கூடியது. விருப்ப மானியங்கள் = நிலையற்றது, அரசியல் சார்புடையது.",
            "fact_en": "In Tamil Nadu, the divisible pool consists of the total aggregate net SOTR.",
            "fact_ta": "தமிழ்நாட்டில், பகிர்வுத் தொகுப்பு மொத்த நிகர SOTR-ஐக் கொண்டுள்ளது."
        }
    ]

    questions = []
    for i, item in enumerate(raw_data, start=1):
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_sefc_q(
            qid=f"SEFC_R_{i:03d}",
            diff="hard" if i % 2 == 0 else "medium",
            qtype="reasoning",
            subtopic=item["subtopic"],
            en_stem=item["stem_en"],
            ta_stem=item["stem_ta"],
            en_a=opts[0][0],
            ta_a=opts[0][1],
            en_b=opts[1][0],
            ta_b=opts[1][1],
            en_c=opts[2][0],
            ta_c=opts[2][1],
            en_d=opts[3][0],
            ta_d=opts[3][1],
            correct_key=correct_key,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=item["why_a_en"],
            why_a_ta=item["why_a_ta"],
            why_b_en=item["why_b_en"],
            why_b_ta=item["why_b_ta"],
            why_c_en=item["why_c_en"],
            why_c_ta=item["why_c_ta"],
            why_d_en=item["why_d_en"],
            why_d_ta=item["why_d_ta"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "state_election_finance_commissions", "reasoning", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions


def build_reasoning_file():
    qs = get_reasoning_questions()
    print(f"Generated {len(qs)} raw Reasoning questions for State Election & Finance Commissions.")
    balanced = randomize_and_balance_dataset(qs, seed=44)

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "state_election_finance_commissions_reasoning.json")
    alias_path = os.path.join(out_dir, "state_election_finance_commissions_assertion_reason.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Reasoning MCQs to {out_path} and alias {alias_path}")

    rep = ContentValidator.validate_file(out_path, expected_count=25, expected_prefix="SEFC_R_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_reasoning_file()
    if not success:
        exit(1)
