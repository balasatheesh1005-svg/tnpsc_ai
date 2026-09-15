# -*- coding: utf-8 -*-
"""
Co-operative Societies - Part 2B: Reasoning (Assertion-Reason) MCQs (25 Questions: CS_R_001 to CS_R_025)
TNPSC Nova AI Content Engine
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from cooperative_societies_mcq_helper import make_coop_q


def get_reasoning_raw_questions():
    return [
        # CS_R_001: 97th CAA and Article 368(2)
        {
            "subtopic": "Supreme Court Ruling in Rajendra N. Shah",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Supreme Court struck down Part IX-B of the Constitution in so far as it related to cooperative societies operating within a single State.\nReason (R): The 97th Constitutional Amendment Act curtailed the legislative competence of State Legislatures under List II Entry 32 without being ratified by at least half of the State Legislatures under Article 368(2) proviso.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஒரு மாநிலத்திற்குள் செயல்படும் கூட்டுறவு சங்கங்கள் தொடர்பான அரசியலமைப்பின் பகுதி IX-B-ன் பகுதிகளை உச்சநீதிமன்றம் ரத்து செய்தது.\nகாரணம் (R): 97-வது அரசியலமைப்புத் திருத்தச் சட்டம் உறுப்பு 368(2) வரம்புரையின் கீழ் குறைந்தபட்சம் பாதி மாநில சட்டமன்றங்களின் ஒப்புதலைப் பெறாமல் பட்டியல் II பதிவு 32-ன் கீழ் மாநிலங்களின் சட்டமியற்றும் அதிகாரத்தைக் கட்டுப்படுத்தியது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the exact constitutional ground upon which the Supreme Court in Union of India v. Rajendra N. Shah (2021) invalidated Part IX-B for state cooperatives. Because Entry 32 of List II was affected, ratification under Article 368(2) proviso was mandatory.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். மாநிலப் பட்டியல் பதிவு 32 பாதிக்கப்பட்டதால், உறுப்பு 368(2) வரம்புரையின் கீழ் 50% மாநிலங்களின் ஒப்புதல் பெறப்படாததே பகுதி IX-B ரத்து செய்யப்பட்டதற்கான நேரடிக் காரணமாகும்.",
            "why_a_en": "Correct. R is the precise ratio decidendi of the Supreme Court ruling in 2021.",
            "why_a_ta": "சரி. 2021 தீர்ப்பில் பகுதி IX-B ரத்து செய்யப்பட்டதற்கான காரணத்தை R துல்லியமாக விளக்குகிறது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-வை நேரடியாக விளக்குகிறது.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Assertion-Reason Tip: Always verify if R is the constitutional 'why' for A. Here lack of Art 368(2) ratification is the direct cause of invalidation.",
            "tip_ta": "குறிப்பு: கூற்று A நடப்பதற்கு காரணம் R தான் நேரடி காரணமா என்பதைச் சரிபார்க்கவும்.",
            "fact_en": "The judgment in Union of India v. Rajendra N. Shah was delivered on 20 July 2021.",
            "fact_ta": "இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா வழக்கின் தீர்ப்பு 2021 ஜூலை 20 அன்று வழங்கப்பட்டது."
        },

        # CS_R_002: Severability of Part IX-B
        {
            "subtopic": "Doctrine of Severability",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Part IX-B continues to remain valid and operative for Multi-State Co-operative Societies and Union Territories.\nReason (R): The Supreme Court applied the Doctrine of Severability, holding that Parliament possesses independent legislative competence over Multi-State Cooperatives (List I Entry 44) and Union Territories (Article 246(4)).\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): பகுதி IX-B பல மாநில கூட்டுறவு சங்கங்கள் மற்றும் யூனியன் பிரதேசங்களுக்கு தொடர்ந்து செல்லுபடியாகும் மற்றும் செயல்பாட்டில் உள்ளது.\nகாரணம் (R): பல மாநில கூட்டுறவுகள் (பட்டியல் I பதிவு 44) மற்றும் யூனியன் பிரதேசங்கள் (உறுப்பு 246(4)) மீது நாடாளுமன்றத்திற்கு சுயாதீன சட்டமியற்றும் அதிகாரம் உள்ளதால் உச்சநீதிமன்றம் பிரித்தெடுக்கும் கோட்பாட்டைப் பயன்படுத்தியது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains why Part IX-B survived for Multi-State Cooperatives and UTs under the Doctrine of Severability.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். பிரித்தெடுக்கும் கோட்பாட்டின் கீழ் பல மாநில கூட்டுறவு மற்றும் யூனியன் பிரதேசங்களுக்கு பகுதி IX-B எவ்வாறு தப்பியது என்பதை R விளக்குகிறது.",
            "why_a_en": "Correct. The majority bench severed the valid portions based on Parliament's constitutional power under List I Entry 44 and Art 246(4).",
            "why_a_ta": "சரி. மத்திய பட்டியல் பதிவு 44 மற்றும் உறுப்பு 246(4)-ன் கீழ் நாடாளுமன்ற அதிகாரத்தைக் கொண்டு செல்லுபடியாகும் பகுதிகள் பிரிக்கப்பட்டன.",
            "why_b_en": "Incorrect. Reason (R) is the direct explanation of Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Severability test: If the valid part can independently survive without the invalid part, courts uphold the valid portion.",
            "tip_ta": "பிரித்தெடுக்கும் சோதனை: செல்லாத பகுதி இல்லாமல் செல்லும் பகுதி தனித்து இயங்க முடியுமானால் நீதிமன்றம் அதனைப் பாதுகாக்கும்.",
            "fact_en": "Justice K.M. Joseph dissented on this point, arguing that Part IX-B formed an inseparable single scheme.",
            "fact_ta": "நீதிபதி கே.எம். ஜோசப் பகுதி IX-B பிரிக்க முடியாத ஒன்று என வாதிட்டு மாறுபட்ட தீர்ப்பு வழங்கினார்."
        },

        # CS_R_003: Article 19(1)(c) and 43B Preserved
        {
            "subtopic": "Fundamental Rights and DPSPs",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The right to form co-operative societies remains a Fundamental Right under Article 19(1)(c) and a Directive Principle under Article 43B.\nReason (R): Amendments to Part III and Part IV of the Constitution do not attract the mandatory state ratification proviso under Article 368(2).\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): கூட்டுறவு சங்கங்களை அமைக்கும் உரிமை உறுப்பு 19(1)(c)-ன் கீழ் ஓர் அடிப்படை உரிமையாகவும், உறுப்பு 43B-ன் கீழ் அரசு வழிகாட்டு நெறிமுறையாகவும் தொடர்கிறது.\nகாரணம் (R): அரசியலமைப்பின் பகுதி III மற்றும் பகுதி IV-ல் செய்யப்படும் திருத்தங்களுக்கு உறுப்பு 368(2) வரம்புரையின் கீழ் மாநிலங்களின் ஒப்புதல் கட்டாயமில்லை.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains why Articles 19(1)(c) and 43B survived challenge. Unlike Part IX-B which impacted Seventh Schedule List II Entry 32, amending Parts III and IV only requires a special majority in Parliament under Article 368(2) main clause, not state ratification.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். பகுதி III மற்றும் IV திருத்தப்படுவதற்கு நாடாளுமன்றத்தின் சிறப்புப் பெரும்பான்மை போதுமானது; ஏழாவது அட்டவணை பாதிக்கப்படாததால் மாநிலங்களின் ஒப்புதல் தேவையில்லை.",
            "why_a_en": "Correct. Articles 19(1)(c) and 43B survived because they did not violate Article 368(2) proviso.",
            "why_a_ta": "சரி. உறுப்புகள் 19(1)(c) மற்றும் 43B உறுப்பு 368(2) வரம்புரையை மீறாததால் தப்பித்தன.",
            "why_b_en": "Incorrect. Reason (R) directly explains why they remained valid.",
            "why_b_ta": "தவறு. அவை ஏன் செல்லுபடியாகின்றன என்பதை காரணம் (R) நேரடியாக விளக்குகிறது.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Only amendments affecting the specific federal provisions listed in Article 368(2) proviso require 50% state ratification.",
            "tip_ta": "உறுப்பு 368(2) வரம்புரையில் பட்டியலிடப்பட்ட குறிப்பிட்ட கூட்டாட்சி விதிகளைப் பாதிக்கும் திருத்தங்களுக்கு மட்டுமே மாநிலங்களின் ஒப்புதல் தேவை.",
            "fact_en": "Articles 19(1)(c) and 43B were never challenged even in the Gujarat High Court.",
            "fact_ta": "குஜராத் உயர் நீதிமன்றத்தில் கூட உறுப்புகள் 19(1)(c) மற்றும் 43B எதிர்க்கப்படவில்லை."
        },

        # CS_R_004: Co-opted Members Voting Rights
        {
            "subtopic": "Co-opted Members - Article 243ZJ",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Co-opted members on the board of a co-operative society cannot vote in the election of office bearers of the society.\nReason (R): The third proviso to Article 243ZJ(1) explicitly bars co-opted members from voting in any election of the co-operative society or being eligible to be elected as office bearers.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஒரு கூட்டுறவு சங்கத்தின் வாரியத்தில் உள்ள இணை உறுப்பினர்கள் (Co-opted members) சங்கத்தின் நிர்வாகிகளைத் தேர்ந்தெடுக்கும் தேர்தலில் வாக்களிக்க முடியாது.\nகாரணம் (R): உறுப்பு 243ZJ(1)-ன் மூன்றாவது வரம்புரை இணை உறுப்பினர்கள் சங்கத்தின் எந்தவொரு தேர்தலிலும் வாக்களிப்பதையோ அல்லது நிர்வாகிகளாகத் தேர்ந்தெடுக்கப்படுவதையோ வெளிப்படையாகத் தடை செய்கிறது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the explicit constitutional basis for (A) under the third proviso to Article 243ZJ(1).",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) உறுப்பு 243ZJ(1)-ன் மூன்றாவது வரம்புரையின் கீழ் கூற்று (A)-விற்கு நேரடி அரசியலமைப்பு விளக்கமாகும்.",
            "why_a_en": "Correct. Reason (R) accurately cites the constitutional text barring co-opted members from voting.",
            "why_a_ta": "சரி. காரணம் (R) இணை உறுப்பினர்கள் வாக்களிப்பதைத் தடை செய்யும் அரசியலமைப்பு விதியைத் துல்லியமாகக் குறிப்பிடுகிறது.",
            "why_b_en": "Incorrect. Reason (R) is the direct reason for Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Co-opted members provide professional advice but have zero electoral voting rights in cooperative governance.",
            "tip_ta": "இணை உறுப்பினர்கள் தொழில்முறை ஆலோசனை வழங்கலாம், ஆனால் தேர்தலில் எந்த வாக்குரிமையும் கிடையாது.",
            "fact_en": "The number of co-opted members cannot exceed two under Article 243ZJ(1).",
            "fact_ta": "உறுப்பு 243ZJ(1)-ன் படி இணை உறுப்பினர்களின் எண்ணிக்கை இரண்டுக்கு மிகாமல் இருக்க வேண்டும்."
        },

        # CS_R_005: Supersession Limitation
        {
            "subtopic": "Supersession of Board - Article 243ZL",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Constitution prohibits the indefinite supersession or suspension of elected cooperative boards by State authorities.\nReason (R): Article 243ZL prescribes that no board shall be superseded or kept under suspension for a period exceeding six months (or one year for banking societies).\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): தேர்ந்தெடுக்கப்பட்ட கூட்டுறவு வாரியங்களை மாநில அதிகாரிகள் காலவரையின்றி கலைப்பதையோ அல்லது இடைநீக்கம் செய்வதையோ அரசியலமைப்பு தடை செய்கிறது.\nகாரணம் (R): உறுப்பு 243ZL எந்தவொரு வாரியமும் ஆறு மாதங்களுக்கு மேல் (கூட்டுறவு வங்கிகளுக்கு 1 ஆண்டு) கலைக்கப்படவோ அல்லது இடைநீக்கத்தில் வைக்கப்படவோ கூடாது என்று விதிக்கிறது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the constitutional mechanism preventing prolonged executive takeover of cooperative management.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூட்டுறவு மேலாண்மையை அரசு அதிகாரிகள் நீண்ட காலம் ஆக்கிரமிப்பதைத் தடுக்கும் அரசியலமைப்பு விதியை விளக்குகிறது.",
            "why_a_en": "Correct. Article 243ZL's 6-month limit was specifically enacted to stop indefinite supersession.",
            "why_a_ta": "சரி. காலவரையற்ற வாரியக் கலைப்பைத் தடுக்கவே உறுப்பு 243ZL-ன் 6 மாத வரம்பு உருவாக்கப்பட்டது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Historical Context: Prior to 97th Amendment, states routinely superseded cooperative boards for decades through nominated administrators.",
            "tip_ta": "வரலாற்றுப் பின்னணி: 97வது திருத்தத்திற்கு முன், மாநில அரசுகள் தங்களுக்கு வேண்டிய சிறப்பு அதிகாரிகளை நியமித்து பல ஆண்டுகள் வாரியங்களைக் கலைத்து வைத்திருந்தன.",
            "fact_en": "Article 243ZL ensures democratic elections must be held within the 6-month window.",
            "fact_ta": "உறுப்பு 243ZL இந்த 6 மாத காலத்திற்குள் ஜனநாயக முறையில் தேர்தல் நடத்தப்படுவதை உறுதி செய்கிறது."
        },

        # CS_R_006: Cooperative Elections and SEC
        {
            "subtopic": "Elections - Article 243ZK",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Elections to cooperative societies are not conducted by the State Election Commission (SEC).\nReason (R): Article 243ZK provides that the superintendence, direction and control of elections shall vest in such authority or body as may be provided by the Legislature of a State, by law.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): கூட்டுறவு சங்கங்களுக்கான தேர்தல்கள் மாநிலத் தேர்தல் ஆணையத்தால் (SEC) நடத்தப்படுவதில்லை.\nகாரணம் (R): உறுப்பு 243ZK, தேர்தல்களை நடத்துவதைக் கண்காணித்தல் மற்றும் கட்டுப்படுத்துதல் மாநிலச் சட்டமன்றம் சட்டத்தால் உருவாக்கும் அதிகார அமைப்பிடம் ஒப்படைக்கப்படும் என்று கூறுகிறது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains why SEC does not conduct cooperative elections — Article 243ZK deliberately did not name the SEC, leaving it to State laws to create specialized authorities (like TNSCSEC in Tamil Nadu).",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். உறுப்பு 243ZK மாநிலத் தேர்தல் ஆணையத்தைக் குறிப்பிடாமல், மாநிலங்கள் தனி தேர்தல் அமைப்பை உருவாக்க அனுமதித்ததே இதற்குக் காரணமாகும்.",
            "why_a_en": "Correct. Article 243ZK delegates creation of the election authority to State law.",
            "why_a_ta": "சரி. உறுப்பு 243ZK தேர்தல் அமைப்பை உருவாக்கும் அதிகாரத்தை மாநில சட்டத்திற்கே வழங்குகிறது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "SEC conducts Panchayat (243K) and Municipality (243ZA) elections; separate State Cooperative Election Authorities conduct cooperative elections.",
            "tip_ta": "மாநிலத் தேர்தல் ஆணையம் உள்ளாட்சித் தேர்தல்களை மட்டுமே நடத்துகிறது; கூட்டுறவு தேர்தல்களை மாநிலக் கூட்டுறவு தேர்தல் ஆணையங்கள் நடத்துகின்றன.",
            "fact_en": "In Tamil Nadu, this authority is the Tamil Nadu State Co-operative Societies Election Commission (TNSCSEC).",
            "fact_ta": "தமிழ்நாட்டில் இவ்வமைப்பு தமிழ்நாடு மாநிலக் கூட்டுறவு சங்கங்களின் தேர்தல் ஆணையம் (TNSCSEC) ஆகும்."
        },

        # CS_R_007: PACS Exemption from BR Act
        {
            "subtopic": "Primary Agricultural Credit Societies",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Primary Agricultural Credit Societies (PACS) are exempt from licensing and regulation by the Reserve Bank of India.\nReason (R): Section 3 of the Banking Regulation Act, 1949 explicitly excludes Primary Agricultural Credit Societies from the application of the Act.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கங்களுக்கு (PACS) இந்திய ரிசர்வ் வங்கியின் உரிமம் பெறுவதிலிருந்தும் ஒழுங்குமுறையிலிருந்தும் விலக்கு அளிக்கப்பட்டுள்ளது.\nகாரணம் (R): வங்கி ஒழுங்குமுறைச் சட்டம் 1949-ன் பிரிவு 3, தொடக்க வேளாண் கடன் சங்கங்களுக்கு இச்சட்டம் பொருந்தாது என்று வெளிப்படையாக விலக்கு அளிக்கிறது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the exact statutory exemption clause in Section 3 of the BR Act 1949 that keeps PACS outside RBI's direct regulatory net.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) வங்கி ஒழுங்குமுறைச் சட்டத்தின் பிரிவு 3-ன் கீழ் PACS-க்கு அளிக்கப்பட்ட சட்டப்பூர்வ விலக்கை விளக்குகிறது.",
            "why_a_en": "Correct. Section 3 of BR Act expressly exempts PACS from RBI banking regulation.",
            "why_a_ta": "சரி. வங்கி ஒழுங்குமுறைச் சட்டத்தின் பிரிவு 3 PACS-க்கு ரிசர்வ் வங்கி விதிகளிலிருந்து விலக்கு அளிக்கிறது.",
            "why_b_en": "Incorrect. Reason (R) is the statutory justification for Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி சட்ட விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "PACS cannot use the word 'Bank' in their name and cannot accept deposits from the general public (only from members).",
            "tip_ta": "PACS தங்களின் பெயரில் 'வங்கி' என்ற சொல்லைப் பயன்படுத்த முடியாது, பொதுமக்களிடமிருந்து வைப்புத்தொகையைப் பெற முடியாது.",
            "fact_en": "PACS operate strictly on member-only transactions, which is why they are exempt from BR Act.",
            "fact_ta": "PACS உறுப்பினர்களுடன் மட்டுமே பரிவர்த்தனை செய்வதால் வங்கி ஒழுங்குமுறைச் சட்டத்திலிருந்து விலக்கு பெற்றுள்ளன."
        },

        # CS_R_008: UCBs and 2020 BR Amendment
        {
            "subtopic": "Urban Co-operative Banks - 2020 Amendment",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Banking Regulation (Amendment) Act, 2020 empowered the Reserve Bank of India to supersede the board of directors of Urban Co-operative Banks.\nReason (R): Dual regulation previously created regulatory blind spots and delays in taking prompt corrective action in troubled cooperative banks like PMC Bank.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): 2020-ஆம் ஆண்டின் வங்கி ஒழுங்குமுறை (திருத்தச்) சட்டம் நகர்ப்புற கூட்டுறவு வங்கிகளின் வாரியத்தைக் கலைக்கும் அதிகாரத்தை ரிசர்வ் வங்கிக்கு வழங்கியது.\nகாரணம் (R): முந்தைய இரட்டை ஒழுங்குமுறைக் கட்டுப்பாடு PMC வங்கி போன்ற பாதிக்கப்பட்ட கூட்டுறவு வங்கிகள் மீது உடனடி நடவடிக்கை எடுப்பதில் தாமதங்களையும் தடைகளையும் ஏற்படுத்தியது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains the policy objective behind the 2020 Amendment. The PMC Bank collapse highlighted systemic failures under dual regulation, prompting Parliament to empower RBI directly under Section 36AAA of the BR Act.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். PMC வங்கி வீழ்ச்சி இரட்டை ஒழுங்குமுறையின் பலவீனங்களை வெளிப்படுத்தியதால், ரிசர்வ் வங்கிக்கு நேரடியாக வாரியத்தைக் கலைக்கும் அதிகாரம் 2020 திருத்தம் மூலம் வழங்கப்பட்டது.",
            "why_a_en": "Correct. The 2020 amendment was directly necessitated by regulatory failures under dual control.",
            "why_a_ta": "சரி. இரட்டைக் கட்டுப்பாட்டு தோல்விகளை நீக்கவே 2020 திருத்தம் கொண்டுவரப்பட்டது.",
            "why_b_en": "Incorrect. Reason (R) explains the rationale for Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-வின் காரணத்தை விளக்குகிறது.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "2020 BR Amendment = Direct RBI power over UCB management, audit, and reconstruction without waiting for State RCS.",
            "tip_ta": "2020 திருத்தம் = மாநில பதிவாளருக்காகக் காத்திருக்காமல் ரிசர்வ் வங்கியே நேரடியாக நகர்ப்புற கூட்டுறவு வங்கிகள் மீது நடவடிக்கை எடுக்க அதிகாரம்.",
            "fact_en": "The Punjab and Maharashtra Co-operative (PMC) Bank scam involved over ₹6,500 crore in illicit advances.",
            "fact_ta": "PMC வங்கியில் ₹6,500 கோடிக்கும் அதிகமான நிதி முறைகேடு நடந்ததே இச்சட்டத் திருத்தத்திற்கு உடனடிக் காரணமானது."
        },

        # CS_R_009: Democratic Member Control
        {
            "subtopic": "Cooperative Principles",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): In a primary co-operative society, a member holding 50% of the share capital has only one vote in the general body.\nReason (R): Co-operative societies are democratic associations based on the principle of 'One Member, One Vote', not 'One Share, One Vote'.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஒரு தொடக்கக் கூட்டுறவு சங்கத்தில், பங்கு மூலதனத்தில் 50% வைத்துள்ள ஒரு உறுப்பினருக்கும் பொதுக்குழுவில் ஒரே ஒரு வாக்கு மட்டுமே உண்டு.\nகாரணம் (R): கூட்டுறவு சங்கங்கள் என்பது 'ஒரு பங்கு, ஒரு வாக்கு' என்பதற்குப் பதிலாக 'ஒரு உறுப்பினர், ஒரு வாக்கு' என்ற ஜனநாயகக் கோட்பாட்டின் அடிப்படையில் இயங்கும் சங்கங்களாகும்.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) directly explains (A). Under cooperative law and ICA Principle 2, democratic control ensures that voting power is equal and human-centric, regardless of economic contribution or capital invested.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். மூலதனத்தைப் பொருட்படுத்தாமல் அனைத்து உறுப்பினர்களுக்கும் சமமான வாக்குரிமை இருப்பதே கூட்டுறவு ஜனநாயகமாகும்.",
            "why_a_en": "Correct. 'One member, one vote' is the direct reason why capital does not dictate voting power.",
            "why_a_ta": "சரி. 'ஒரு உறுப்பினர், ஒரு வாக்கு' என்பதே மூலதனம் வாக்குரிமையைத் தீர்மானிக்காமல் இருக்கக் காரணமாகும்.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "In addition, cooperative laws place a ceiling on the maximum shareholding any individual can hold (e.g., 20% or ₹10,000 in TN).",
            "tip_ta": "மேலும் ஒரு தனிநபர் சங்கத்தில் வைத்திருக்கக்கூடிய அதிகபட்ச பங்குகளுக்கும் சட்ட வரம்பு உள்ளது (எ.கா. தமிழகத்தில் 20%).",
            "fact_en": "This democratic equality protects small and marginal farmers from being marginalized by wealthy members.",
            "fact_ta": "இந்த ஜனநாயக சமத்துவம் சிறு மற்றும் குறு விவசாயிகளை பணக்கார உறுப்பினர்களின் ஆதிக்கத்திலிருந்து பாதுகாக்கிறது."
        },

        # CS_R_010: Patronage Dividend
        {
            "subtopic": "Distribution of Surplus in Cooperatives",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): In a cooperative society, surplus is distributed primarily as patronage dividend rather than capital dividend.\nReason (R): The objective of a cooperative is mutual service to members in proportion to their participation, rather than maximizing return on invested equity.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஒரு கூட்டுறவு சங்கத்தில், உபரி லாபமானது மூலதன ஈவுத்தொகைக்கு பதிலாக பிரதானமாக ஆதரவு ஈவுத்தொகையாகவே (Patronage dividend) பகிர்ந்தளிக்கப்படுகிறது.\nகாரணம் (R): கூட்டுறவு சங்கத்தின் நோக்கம் முதலீடு செய்த மூலதனத்திற்கு அதிகபட்ச லாபம் ஈட்டுவதல்ல; மாறாக உறுப்பினர்களின் பயன்பாட்டிற்கு ஏற்ப அவர்களுக்கு பரஸ்பர சேவை வழங்குவதே ஆகும்.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the foundational philosophy behind patronage dividend — profits are returned to members based on how much business they did with the society (e.g., milk supplied to Aavin or goods bought from TUCS).",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். சங்கத்துடன் உறுப்பினர்கள் மேற்கொண்ட வணிகத்தின் அளவுக்கு ஏற்பவே உபரி திரும்ப அளிக்கப்படுகிறது.",
            "why_a_en": "Correct. Service orientation dictates the patronage distribution principle.",
            "why_a_ta": "சரி. சேவை நோக்கமே ஆதரவு ஈவுத்தொகை முறைக்கு அடிப்படையாகும்.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Patronage dividend = Rebate on purchases or bonus on supply of farm produce to the cooperative.",
            "tip_ta": "ஆதரவு ஈவுத்தொகை = சங்கத்தில் வாங்கிய பொருட்களுக்கான தள்ளுபடி அல்லது சப்ளை செய்த விளைபொருட்களுக்கான ஊக்கத்தொகை.",
            "fact_en": "Statutes restrict capital dividend to a modest maximum percentage (typically 12% to 14%).",
            "fact_ta": "மூலதனப் பங்குகளுக்கான ஈவுத்தொகைக்கு சட்டங்கள் குறைந்தபட்ச உச்சவரம்பை (12% முதல் 14%) நிர்ணயிக்கின்றன."
        },

        # CS_R_011: 1904 Act Limitation
        {
            "subtopic": "Historical Evolution - 1904 Act",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Co-operative Credit Societies Act, 1904 was replaced by the Co-operative Societies Act, 1912 within eight years.\nReason (R): The 1904 Act was defective as it permitted only credit societies and made no provision for non-credit societies or central cooperative unions.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): கூட்டுறவு கடன் சங்கங்கள் சட்டம் 1904 இயற்றப்பட்ட எட்டு ஆண்டுகளுக்குள் கூட்டுறவு சங்கங்கள் சட்டம் 1912-ஆல் மாற்றப்பட்டது.\nகாரணம் (R): 1904-ஆம் ஆண்டு சட்டம் கடன் சங்கங்களை மட்டுமே அனுமதித்தது; கடன் அல்லாத சங்கங்கள் அல்லது மத்திய கூட்டுறவு ஒன்றியங்களை அமைப்பதற்கு எந்த விதியையும் கொண்டிருக்கவில்லை.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains why the 1912 Act was urgently enacted — the 1904 Act's restriction solely to credit societies severely constrained marketing, purchase, and federated financing of cooperatives.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். 1904 சட்டம் கடன் சங்கங்களை மட்டுமே அனுமதித்த குறைபாட்டை நீக்கி, விற்பனைச் சங்கங்கள் மற்றும் மத்திய வங்கிகளை அனுமதிக்கவே 1912 சட்டம் கொண்டுவரப்பட்டது.",
            "why_a_en": "Correct. The limitation of the 1904 Act was the exact reason for the 1912 enactment.",
            "why_a_ta": "சரி. 1904 சட்டத்தின் குறைபாடே 1912 சட்டம் இயற்றப்பட நேரடிக் காரணமாகும்.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "1904 Act = Only Credit; 1912 Act = Credit + Non-Credit (Marketing/Consumer) + Central Banks/Unions.",
            "tip_ta": "1904 சட்டம் = கடன் மட்டும்; 1912 சட்டம் = கடன் + கடன் அல்லாதவை + மத்திய வங்கிகள்.",
            "fact_en": "The 1912 Act facilitated the formation of District Central Co-operative Banks (DCCBs).",
            "fact_ta": "1912 சட்டம் மாவட்ட மத்திய கூட்டுறவு வங்கிகள் (DCCB) உருவாக வழிகோலியது."
        },

        # CS_R_012: Universal PDS in Tamil Nadu
        {
            "subtopic": "Tamil Nadu PDS Model",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Tamil Nadu has achieved the lowest leakage and highest beneficiary satisfaction in the Public Distribution System (PDS) in India.\nReason (R): Over 90% of Fair Price Shops in Tamil Nadu are operated through democratic cooperative societies rather than private commercial licensees.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): இந்தியாவில் பொது விநியோகத் திட்டத்தில் (PDS) மிகக் குறைந்த கசிவு மற்றும் அதிகப் பயனாளி திருப்தியை தமிழ்நாடு அடைந்துள்ளது.\nகாரணம் (R): தமிழ்நாட்டில் 90%-க்கும் அதிகமான நியாயவிலைக் கடைகள் தனியார் உரிமமதாரர்களுக்குப் பதிலாக ஜனநாயகக் கூட்டுறவு சங்கங்கள் மூலமாகவே நடத்தப்படுகின்றன.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains (A). As documented by the Wadhwa Committee on PDS, Tamil Nadu eliminated private dealer cartels by entrusting ration shops to cooperatives (PACS and Consumer Stores), ensuring social accountability and low leakages.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். தனியார் வியாபாரிகளை நீக்கி கூட்டுறவு சங்கங்களிடம் ரேஷன் கடைகளை ஒப்படைத்ததே தமிழக PDS திட்டத்தின் வெற்றிக்கு முக்கியக் காரணமாகும் (வாத்வா குழு அறிக்கை).",
            "why_a_en": "Correct. Cooperative management is widely recognized as the structural reason for Tamil Nadu PDS success.",
            "why_a_ta": "சரி. கூட்டுறவு நிர்வாகமே தமிழக பொது விநியோகத் திட்டத்தின் வெற்றிக்கு அடிப்படைக் காரணமாகும்.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Tamil Nadu PDS: Universal (Not Targeted) + Run by Cooperatives (PACS & TUCS) = Model for India.",
            "tip_ta": "தமிழக PDS: அனைவருக்கும் பொதுவானது + கூட்டுறவு சங்கங்களால் நடத்தப்படுகிறது = இந்தியாவின் முன்மாதிரி.",
            "fact_en": "Justice Wadhwa Committee commended Tamil Nadu's cooperative PDS model in its Supreme Court report.",
            "fact_ta": "நீதிபதி வாத்வா குழு உச்சநீதிமன்றத்தில் தாக்கல் செய்த அறிக்கையில் தமிழக கூட்டுறவு ரேஷன் முறையைப் வெகுவாகப் பாராட்டியது."
        },

        # CS_R_013: Amul Three-Tier Anand Pattern
        {
            "subtopic": "Operation Flood and Dairy Cooperatives",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Operation Flood successfully transformed India from a milk-deficient nation into the world's largest milk producer.\nReason (R): The Anand Pattern vertically integrated smallholder dairy farmers with modern processing and urban markets, eliminating exploitative middlemen.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): வெண்மைப் புரட்சி (ஆபரேஷன் பிளட்) இந்தியாவை பால் பற்றாக்குறை நாட்டிலிருந்து உலகின் மிகப்பெரிய பால் உற்பத்தி நாடாக வெற்றிகரமாக மாற்றியது.\nகாரணம் (R): ஆனந்த் மாதிரி சிறு பால் விவசாயிகளை நவீன பதப்படுத்துதல் மற்றும் நகரச் சந்தைகளுடன் செங்குத்தாக ஒருங்கிணைத்து, சுரண்டல் இடைத்தரகர்களை நீக்கியது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains how Operation Flood achieved the White Revolution using the cooperative Anand pattern.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். இடைத்தரகர்களை நீக்கி விவசாயிகளுக்கு நியாயமான விலை வழங்கியதே வெண்மைப் புரட்சியின் வெற்றிக்குக் காரணம்.",
            "why_a_en": "Correct. Vertical integration under the Anand model was the engine of Operation Flood.",
            "why_a_ta": "சரி. ஆனந்த் மாதிரியின் செங்குத்து ஒருங்கிணைப்பே வெண்மைப் புரட்சியின் வெற்றிக்கான இயந்திரமாகும்.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Operation Flood: Launched in 1970 in 3 phases by NDDB under Dr. Verghese Kurien.",
            "tip_ta": "ஆபரேஷன் பிளட்: 1970-ல் டாக்டர் வர்கீஸ் குரியன் தலைமையில் NDDB-ஆல் 3 கட்டங்களாகத் தொடங்கப்பட்டது.",
            "fact_en": "India overtook the United States as the world's largest milk producer in 1998.",
            "fact_ta": "1998-ல் அமெரிக்காவைப் பின்னுக்குத் தள்ளி இந்தியா உலகின் மிகப்பெரிய பால் உற்பத்தி நாடானது."
        },

        # CS_R_014: State Partnership and Gorwala Report
        {
            "subtopic": "Committees on Cooperatives",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The All India Rural Credit Survey Committee (1954) strongly advocated State financial partnership in cooperative institutions.\nReason (R): Rural cooperatives faced fierce opposition from traditional rural moneylenders and needed powerful financial and institutional backing from the State to survive.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அகில இந்திய கிராமப்புற கடன் ஆய்வுக் குழு (1954) கூட்டுறவு நிறுவனங்களில் அரசின் நிதிப் பங்களிப்பை வலுவாக ஆதரித்தது.\nகாரணம் (R): கிராமப்புறக் கூட்டுறவுகள் பாரம்பரியக் கந்துவட்டிக்காரர்களின் கடுமையான போட்டியை எதிர்கொண்டதால், அவற்றைத் தற்காத்துக் கொள்ள அரசின் வலுவான நிதி மற்றும் நிறுவன ஆதரவு தேவைப்பட்டது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) represents the exact socio-economic rationale articulated by A.D. Gorwala in 1954: unassisted rural cooperatives could not compete against entrenched rural money-lending power without massive state partnership.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். கந்துவட்டிக்காரர்களின் ஆதிக்கத்தை முறியடிக்க கூட்டுறவுகளுக்கு அரசின் நேரடிப் பங்கு மூலதனமும் ஆதரவும் அவசியம் என கோர்வாலா குழு வாதிட்டது.",
            "why_a_en": "Correct. The economic weakness of rural cooperatives was the explicit rationale for proposing state partnership.",
            "why_a_ta": "சரி. கந்துவட்டிக்காரர்களின் சுரண்டலை முறியடிக்கவே அரசுப் பங்களிப்பு பரிந்துரைக்கப்பட்டது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Gorwala Philosophy: 'Cooperation has failed, but Cooperation must succeed' through State Partnership.",
            "tip_ta": "கோர்வாலா தத்துவம்: அரசுப் பங்களிப்பின் மூலம் 'கூட்டுறவு தோல்வியடைந்தது, ஆனால் கூட்டுறவு வெற்றி பெற்றே தீர வேண்டும்'.",
            "fact_en": "This led to state governments contributing up to 51% of share capital in cooperative banks in the 1950s and 60s.",
            "fact_ta": "இதன் விளைவாக 1950 மற்றும் 60-களில் கூட்டுறவு வங்கிகளில் மாநில அரசுகள் 51% வரை பங்கு மூலதனத்தை வழங்கின."
        },

        # CS_R_015: Vaidyanathan Committee Conditionality
        {
            "subtopic": "Vaidyanathan Committee 2004",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The financial recapitalization package under the Vaidyanathan Committee (2004) was made strictly conditional upon State legal reforms.\nReason (R): Providing unconditional financial bailouts without removing political and bureaucratic interference would lead to recurrent insolvency of cooperative credit institutions.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): வைத்தியநாதன் குழுவின் (2004) நிதி மறுமூலதனத் தொகுப்பு மாநிலங்களின் சட்டச் சீர்திருத்தங்களுக்குக் கடுமையான நிபந்தனையாக விதிக்கப்பட்டது.\nகாரணம் (R): அரசியல் மற்றும் அதிகாரவர்க்கத் தலையீடுகளை அகற்றாமல் நிபந்தனையற்ற நிதி மீட்பு வழங்குவது கூட்டுறவு கடன் நிறுவனங்களை மீண்டும் மீண்டும் திவால் நிலைக்குத் தள்ளிவிடும்.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains why the Vaidyanathan Committee insisted that states sign MoUs and amend their Cooperative Acts to grant functional autonomy before receiving central recapitalization funds.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். சட்ட திருத்தங்கள் செய்து தன்னாட்சி வழங்காத வரை நிதி உதவி மீண்டும் வீணாகிவிடும் என்பதால் வைத்தியநாதன் குழு நிபந்தனைகளை விதித்தது.",
            "why_a_en": "Correct. Legal autonomy was made a prerequisite for financial bailout to prevent moral hazard.",
            "why_a_ta": "சரி. தன்னாட்சி வழங்கி பொறுப்புடைமையை உறுதி செய்யவே நிபந்தனைகள் விதிக்கப்பட்டன.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Vaidyanathan Formula: Financial assistance + Institutional reforms (Freedom from government control).",
            "tip_ta": "வைத்தியநாதன் சூத்திரம்: நிதி உதவி + நிறுவன சீர்திருத்தங்கள் (அரசு தலையீடற்ற தன்னாட்சி).",
            "fact_en": "25 states signed the MoU to implement the Vaidyanathan revival package.",
            "fact_ta": "25 மாநிலங்கள் வைத்தியநாதன் மறுமலர்ச்சி திட்டத்தை செயல்படுத்த புரிந்துணர்வு ஒப்பந்தத்தில் கையெழுத்திட்டன."
        }
    ]


def get_reasoning_questions_batch2():
    return [
        # CS_R_016: Ministry of Cooperation Mandate
        {
            "subtopic": "Ministry of Cooperation Mandate",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Ministry of Cooperation was carved out as a dedicated central ministry in July 2021.\nReason (R): India's multi-tier cooperative movement required focused national policy support, digitisation of PACS, and ease of doing business for multi-state cooperatives.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஜூலை 2021-ல் ஒரு பிரத்யேக மத்திய அமைச்சகமாக கூட்டுறவு அமைச்சகம் உருவாக்கப்பட்டது.\nகாரணம் (R): இந்தியாவின் பல அடுக்கு கூட்டுறவு இயக்கத்திற்கு ஒருமுகப்படுத்தப்பட்ட தேசியக் கொள்கை ஆதரவு, PACS கணினிமயமாக்கல் மற்றும் பல மாநில கூட்டுறவுகளுக்கான வணிக எளிதாக்கல் ஆகியவை தேவைப்பட்டன.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) outlines the structural motivations for establishing the independent Ministry of Cooperation in 2021.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். கூட்டுறவுத் துறையை நவீனப்படுத்தவும் வலுப்படுத்தவுமே தனி அமைச்சகம் உருவாக்கப்பட்டது.",
            "why_a_en": "Correct. Reason (R) accurately captures the rationale for creating the new Ministry.",
            "why_a_ta": "சரி. காரணம் (R) தனி அமைச்சகம் உருவாக்கப்பட்டதற்கான காரணங்களைச் சரியாக விளக்குகிறது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Ministry of Cooperation vision: 'Sahakar se Samriddhi' through transparent and digitized cooperative networks.",
            "tip_ta": "கூட்டுறவு அமைச்சகத்தின் பார்வை: வெளிப்படையான கணினிமயமாக்கப்பட்ட கூட்டுறவு மூலம் 'சககார் சே சம்ரித்தி'.",
            "fact_en": "The Ministry coordinates with NABARD, NCDC, and State Registrar offices.",
            "fact_ta": "இவ்வமைச்சகம் நபார்டு, NCDC மற்றும் மாநில பதிவாளர் அலுவலகங்களுடன் இணைந்து செயல்படுகிறது."
        },

        # CS_R_017: SC/ST and Women Reservation in 243ZJ
        {
            "subtopic": "Reservation on Board - Article 243ZJ",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 243ZJ mandates reservation of one seat for SC/ST and two seats for women on the board of every individual-member cooperative society.\nReason (R): Historically, cooperative boards were disproportionately dominated by influential landed elites, marginalizing women and marginalized communities.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): தனிநபர் உறுப்பினர்களைக் கொண்ட ஒவ்வொரு கூட்டுறவு சங்க வாரியத்திலும் SC/ST பிரிவினருக்கு ஒரு இடமும், பெண்களுக்கு இரண்டு இடங்களும் ஒதுக்கப்பட வேண்டும் என்று உறுப்பு 243ZJ விதிக்கிறது.\nகாரணம் (R): வரலாற்று ரீதியாக, கூட்டுறவு வாரியங்கள் நிலப்பிரபுத்துவ ஆதிக்க சக்திகளால் ஆதிக்கம் செலுத்தப்பட்டு, பெண்களும் விளிம்புநிலை மக்களும் ஓரங்கட்டப்பட்டிருந்தனர்.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains the social justice objective of inserting mandatory reservations in Article 243ZJ through the 97th Amendment.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். கூட்டுறவில் சமூக நீதியை உறுதிசெய்து விளிம்புநிலை மக்கள் பிரதிநிதித்துவத்தை உருவாக்கவே இவ்விடஒதுக்கீடு கொண்டுவரப்பட்டது.",
            "why_a_en": "Correct. Elite capture of cooperatives was the driving social reason for constitutional board reservations.",
            "why_a_ta": "சரி. மேல்தட்டு ஆதிக்கத்தை உடைத்து சமத்துவத்தை உருவாக்கவே அரசமைப்பு இடஒதுக்கீடு கொண்டுவரப்பட்டது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Article 243ZJ Quota: 1 SC/ST + 2 Women. Must be on the board of every cooperative having individual members.",
            "tip_ta": "உறுப்பு 243ZJ இடஒதுக்கீடு: 1 SC/ST + 2 பெண்கள். தனிநபர் உறுப்பினர்களைக் கொண்ட அனைத்து சங்கங்களிலும் கட்டாயம்.",
            "fact_en": "Similar reservations were mandated in Panchayats (243D) and Municipalities (243T).",
            "fact_ta": "பஞ்சாயத்துகள் (243D) மற்றும் நகராட்சிகளிலும் (243T) இதே போன்ற இடஒதுக்கீடுகள் உள்ளன."
        },

        # CS_R_018: Producer Companies Advantage
        {
            "subtopic": "Producer Companies under Companies Act",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Many primary producers prefer establishing Producer Companies under the Companies Act rather than traditional Co-operative Societies under State Acts.\nReason (R): Producer Companies operate under a single central company law framework, free from the day-to-day administrative interference and audit controls of the State Registrar of Co-operative Societies.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): பல உற்பத்தியாளர்கள் மாநிலச் சட்டங்களின் கீழான பாரம்பரிய கூட்டுறவு சங்கங்களுக்குப் பதிலாக நிறுவனங்கள் சட்டத்தின் கீழ் உழவர் உற்பத்தியாளர் நிறுவனங்களைத் (FPO) தொடங்க விரும்புகின்றனர்.\nகாரணம் (R): உற்பத்தியாளர் நிறுவனங்கள் மாநில கூட்டுறவு பதிவாளரின் அன்றாட நிர்வாக தலையீடுகள் மற்றும் தணிக்கைக் கட்டுப்பாடுகள் இல்லாமல், ஒற்றை மத்திய நிறுவன சட்டக் கட்டமைப்பின் கீழ் இயங்குகின்றன.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains why the Producer Company model (Alagh Committee) gained popularity — it retains cooperative values while freeing producers from local political and bureaucratic interference by the RCS.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். பதிவாளரின் நிர்வாகத் தலையீடுகள் இன்றி சுதந்திரமாக வணிகம் செய்ய முடிவதாலேயே உற்பத்தியாளர் நிறுவனங்கள் பிரபலமடைந்துள்ளன.",
            "why_a_en": "Correct. Freedom from RCS bureaucracy is the primary driver of Producer Company adoption.",
            "why_a_ta": "சரி. பதிவாளரின் அதிகார தலையீடற்ற தன்னாட்சியே உற்பத்தியாளர் நிறுவனங்கள் விரும்பப்படக் காரணமாகும்.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Producer Companies = Chapter XXI-A of Companies Act 2013; Regulated by ROC (Registrar of Companies), NOT State RCS.",
            "tip_ta": "உற்பத்தியாளர் நிறுவனங்கள் = நிறுவனங்கள் சட்டம் 2013; ROC அமைப்பால் கட்டுப்படுத்தப்படுகின்றன, மாநில பதிவாளரால் அல்ல.",
            "fact_en": "India aims to establish 10,000 Farmer Producer Organizations (FPOs).",
            "fact_ta": "நாடு முழுவதும் 10,000 உழவர் உற்பத்தியாளர் நிறுவனங்களை அமைக்க மத்திய அரசு இலக்கு நிர்ணயித்துள்ளது."
        },

        # CS_R_019: Co-operative Federalism and Basic Structure
        {
            "subtopic": "Basic Structure and Federalism",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Parliament cannot bypass the proviso to Article 368(2) by using its constituent power under the guise of an ordinary constitutional amendment.\nReason (R): Federalism and the constitutional division of legislative powers between the Union and States form part of the Basic Structure of the Indian Constitution.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஒரு சாதாரண அரசியலமைப்பு திருத்தத்தின் போர்வையில் உறுப்பு 368(2) வரம்புரையை நாடாளுமன்றத்தால் புறக்கணிக்க முடியாது.\nகாரணம் (R): கூட்டாட்சி மற்றும் ஒன்றியம்-மாநிலங்களுக்கு இடையேயான சட்டமியற்றும் அதிகாரப் பகிர்வு இந்திய அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பின் (Basic Structure) ஒரு பகுதியாகும்.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains why the Supreme Court guarded the federal balance in Rajendra N. Shah (2021). The proviso to Article 368(2) is an entrenched constitutional safeguard designed to preserve federalism.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். கூட்டாட்சி அடிப்படைக் கட்டமைப்பு என்பதால், மாநிலங்களின் அதிகாரத்தைப் பாதிக்கும் திருத்தங்களுக்கு மாநிலங்களின் ஒப்புதல் கட்டாயமாகிறது.",
            "why_a_en": "Correct. Basic structure doctrine ensures federal safeguards like Art 368(2) proviso cannot be circumvented.",
            "why_a_ta": "சரி. கூட்டாட்சி அடிப்படைக் கட்டமைப்பு என்பதால் உறுப்பு 368(2) பாதுகாப்புகளை மீற முடியாது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "The proviso to Article 368(2) is the federal gatekeeper of the Indian Constitution.",
            "tip_ta": "உறுப்பு 368(2) வரம்புரை என்பது இந்திய அரசியலமைப்பின் கூட்டாட்சிக் காவலனாகும்.",
            "fact_en": "This principle was first strongly established in Kesavananda Bharati (1973) and reaffirmed in S.R. Bommai (1994).",
            "fact_ta": "இக்கோட்பாடு கேசவானந்த பாரதி (1973) வழக்கில் நிறுவப்பட்டு எஸ்.ஆர். பொம்மை (1994) வழக்கில் உறுதிப்படுத்தப்பட்டது."
        },

        # CS_R_020: DICGC Protection for UCBs
        {
            "subtopic": "Deposit Insurance Coverage",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Small depositors in licensed Urban Co-operative Banks enjoy deposit safety comparable to scheduled commercial banks.\nReason (R): Eligible Urban Co-operative Banks are covered under the Deposit Insurance and Credit Guarantee Corporation (DICGC) Act, protecting deposits up to ₹5 lakh per depositor.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உரிமம் பெற்ற நகர்ப்புற கூட்டுறவு வங்கிகளில் உள்ள சிறு வைப்புத்தொகையாளர்கள் வணிக வங்கிகளுக்கு இணையான வைப்புத்தொகைப் பாதுகாப்பைப் பெறுகின்றனர்.\nகாரணம் (R): தகுதியுடைய நகர்ப்புற கூட்டுறவு வங்கிகள் DICGC சட்டத்தின் கீழ் பாதுகாக்கப்பட்டு, ஒரு வைப்புத்தொகையாளருக்கு ₹5 லட்சம் வரை காப்பீடு வழங்கப்படுகிறது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the exact institutional guarantee explaining why small depositors in cooperative banks have parity of safety with commercial banks up to ₹5 lakh.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். DICGC ₹5 லட்சம் வரை காப்பீடு வழங்குவதாலேயே கூட்டுறவு வங்கிகளிலும் சிறு வைப்புத்தொகையாளர்களுக்கு முழுப் பாதுகாப்பு கிடைக்கிறது.",
            "why_a_en": "Correct. DICGC coverage is the direct reason for depositor parity.",
            "why_a_ta": "சரி. DICGC காப்பீடே வைப்புத்தொகை பாதுகாப்பிற்கான நேரடிக் காரணமாகும்.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "DICGC limit: ₹5 lakh covers over 98% of total deposit accounts in Indian cooperative banks.",
            "tip_ta": "DICGC வரம்பு: ₹5 லட்சம் என்பது கூட்டுறவு வங்கிகளில் உள்ள 98%-க்கும் அதிகமான கணக்குகளுக்கு முழுப் பாதுகாப்பு அளிக்கிறது.",
            "fact_en": "DICGC is a wholly owned subsidiary of the Reserve Bank of India.",
            "fact_ta": "DICGC என்பது இந்திய ரிசர்வ் வங்கியின் முழுமையான துணை அமைப்பாகும்."
        },

        # CS_R_021: Non-application of Supersession in Aided Societies
        {
            "subtopic": "Supersession Protections - Article 243ZL",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The board of a cooperative society having no government shareholding or financial assistance cannot be superseded on the general ground of supersession.\nReason (R): The first proviso to Article 243ZL(1) explicitly protects autonomous societies from supersession where there is no government shareholding, loan, financial assistance, or government guarantee.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அரசுப் பங்குகள் அல்லது நிதி உதவி இல்லாத ஒரு கூட்டுறவு சங்கத்தின் வாரியத்தைப் பொதுவான அடிப்படையில் அரசால் கலைக்க முடியாது.\nகாரணம் (R): உறுப்பு 243ZL(1)-ன் முதல் வரம்புரை, அரசுப் பங்கு, கடன் அல்லது நிதி உதவி இல்லாத தன்னாட்சி பெற்ற சங்கங்களை வாரியக் கலைப்பிலிருந்து வெளிப்படையாகப் பாதுகாக்கிறது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the constitutional protection embedded in the proviso to Article 243ZL(1) designed to prevent state encroachment into self-financed cooperatives.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) உறுப்பு 243ZL(1)-ன் கீழ் தன்னாட்சி சங்கங்களுக்கு வழங்கப்பட்ட அரசமைப்புப் பாதுகாப்பை விளக்குகிறது.",
            "why_a_en": "Correct. Proviso to 243ZL(1) insulates non-aided cooperatives from executive supersession.",
            "why_a_ta": "சரி. உறுப்பு 243ZL(1)-ன் வரம்புரை அரசு உதவி பெறாத சங்கங்களைக் கலைப்பிலிருந்து பாதுகாக்கிறது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Self-financed cooperatives enjoy high constitutional immunity from government supersession.",
            "tip_ta": "சொந்த நிதியில் இயங்கும் கூட்டுறவு சங்கங்கள் அரசுத் தலையீட்டிலிருந்து உயர் பாதுகாப்பைப் பெறுகின்றன.",
            "fact_en": "Exceptions exist only for deadlock or failure to conduct elections.",
            "fact_ta": "தேர்தல் முடக்கம் ஏற்பட்டால் மட்டுமே இத்தகைய சங்கங்கள் மீது நடவடிக்கை எடுக்க முடியும்."
        },

        # CS_R_022: Multi-State Cooperatives Authority 2023
        {
            "subtopic": "MSCS Amendment Act 2023",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Multi-State Co-operative Societies (Amendment) Act, 2023 established an independent Co-operative Election Authority.\nReason (R): Prior to the 2023 Amendment, incumbent boards of multi-state cooperatives appointed their own returning officers, creating serious conflicts of interest and electoral malpractice.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): பல மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டம் 2023 ஒரு சுதந்திரமான கூட்டுறவு தேர்தல் ஆணையத்தை நிறுவியது.\nகாரணம் (R): 2023 திருத்தத்திற்கு முன்பு, பல மாநில கூட்டுறவு சங்கங்களின் பதவியில் உள்ள வாரியங்களே தங்களுக்கு வேண்டிய தேர்தல் அதிகாரிகளை நியமித்ததால் நலன்சார் முரண்பாடுகளும் தேர்தல் முறைகேடுகளும் நிகழ்ந்தன.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) accurately states the mischief that the 2023 Parliament Amendment sought to remedy by creating an independent statutory Election Authority.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) 2023-ல் கூட்டுறவு தேர்தல் ஆணையம் உருவாக்கப்பட்டதன் உண்மையான நோக்கத்தை விளக்குகிறது.",
            "why_a_en": "Correct. Eliminating conflict of interest in elections was the primary motivation for creating the Authority.",
            "why_a_ta": "சரி. தேர்தல் முறைகேடுகளைத் தடுக்கவே சுதந்திரமான தேர்தல் ஆணையம் அமைக்கப்பட்டது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Co-operative Election Authority: Conducts, supervises, and certifies elections for all Multi-State Co-operatives.",
            "tip_ta": "கூட்டுறவு தேர்தல் ஆணையம்: அனைத்து பல மாநில கூட்டுறவு தேர்தல்களையும் நடத்தும் சட்டப்பூர்வ அமைப்பு.",
            "fact_en": "The Authority is headed by a Chairperson with the rank of Additional Secretary or higher.",
            "fact_ta": "கூடுதல் செயலாளர் அந்தஸ்திலான அதிகாரி இதன் தலைவராக நியமிக்கப்படுகிறார்."
        },

        # CS_R_023: Quasi-Judicial Power of Registrar
        {
            "subtopic": "Registrar Quasi-Judicial Role",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Registrar of Co-operative Societies functions as a quasi-judicial tribunal while adjudicating dispute claims under State Co-operative Acts.\nReason (R): While deciding disputes, the Registrar must observe the principles of natural justice, hear both parties, and pass reasoned speaking orders that are appealable before judicial tribunals.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மாநில கூட்டுறவு சங்கங்கள் சட்டங்களின் கீழ் தகராறுகளை விசாரிக்கும் போது கூட்டுறவு சங்கங்களின் பதிவாளர் ஓர் அரை-நீதித்துறை (Quasi-judicial) அமைப்பாகச் செயல்படுகிறார்.\nகாரணம் (R): தகராறுகளைத் தீர்மானிக்கும் போது, பதிவாளர் இயற்கை நீதி நெறிமுறைகளைப் பின்பற்றி, இரு தரப்பையும் விசாரித்து, கூட்டுறவு தீர்ப்பாயத்தில் மேல்முறையீடு செய்யக்கூடிய விரிவான உத்தரவுகளைப் பிறப்பிக்க வேண்டும்.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) defines the legal test for quasi-judicial functioning: duty to act judicially, follow natural justice, and issue reasoned orders subject to appeal.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். இயற்கை நீதியைப் பின்பற்றி உத்தரவு பிறப்பிப்பதாலேயே பதிவாளர் அரை-நீதித்துறை அதிகாரம் கொண்டவராகிறார்.",
            "why_a_en": "Correct. Observance of natural justice and reasoned adjudication qualifies the Registrar as a quasi-judicial body.",
            "why_a_ta": "சரி. இயற்கை நீதி மற்றும் தீர்ப்பாய உத்தரவுகள் பதிவாளரை அரை-நீதித்துறை அமைப்பாக மாற்றுகின்றன.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Registrar's Twin Roles: Executive / Administrative Head + Quasi-Judicial Arbitrator in disputes.",
            "tip_ta": "பதிவாளரின் இரட்டைப் பங்கு: நிர்வாகத் தலைவர் + தகராறுகளைத் தீர்க்கும் அரை-நீதித்துறை நடுவர்.",
            "fact_en": "Under Section 90 of TN Act 1983, the Registrar has powers of a civil court regarding summoning witnesses and discovery of documents.",
            "fact_ta": "தமிழக சட்டத்தின் பிரிவு 90-ன் கீழ் சாட்சிகளை அழைப்பதிலும் ஆவணங்களைப் பெறுவதிலும் பதிவாளருக்கு சிவில் நீதிமன்ற அதிகாரம் உண்டு."
        },

        # CS_R_024: NAFED and Price Support Scheme
        {
            "subtopic": "NAFED and Market Intervention",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): NAFED procures oilseeds and pulses from farmers when market prices fall below the Minimum Support Price (MSP).\nReason (R): NAFED is the designated central nodal agency for implementing the Government of India's Price Support Scheme (PSS).\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சந்தை விலையானது குறைந்தபட்ச ஆதரவு விலையை (MSP) விடக் குறையும் போது NAFED விவசாயிகளிடமிருந்து எண்ணெய் வித்துக்கள் மற்றும் பருப்பு வகைகளைக் கொள்முதல் செய்கிறது.\nகாரணம் (R): இந்திய அரசின் விலை ஆதரவுத் திட்டத்தை (PSS) செயல்படுத்துவதற்கான மத்திய ஒருங்கிணைப்பு முகமையாக NAFED அறிவிக்கப்பட்டுள்ளது.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) states the official statutory role of NAFED under the Price Support Scheme which triggers procurement when market rates slump below MSP.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். விலை ஆதரவுத் திட்டத்தின் கீழ் மத்திய முகமையாக செயல்படுவதாலேயே சந்தை விலை குறையும் போது NAFED கொள்முதல் செய்கிறது.",
            "why_a_en": "Correct. NAFED's procurement mandate stems directly from its PSS nodal agency status.",
            "why_a_ta": "சரி. PSS திட்டத்தின் முதன்மை முகமையாக இருப்பதாலேயே NAFED விளைபொருட்களைக் கொள்முதல் செய்கிறது.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "FCI handles wheat and paddy MSP procurement; NAFED handles pulses, oilseeds, and copra MSP procurement.",
            "tip_ta": "நெல் மற்றும் கோதுமையை FCI கொள்முதல் செய்கிறது; பருப்பு மற்றும் எண்ணெய் வித்துக்களை NAFED கொள்முதல் செய்கிறது.",
            "fact_en": "Procurement losses incurred by NAFED under PSS are fully reimbursed by the Central Government.",
            "fact_ta": "விலை ஆதரவுத் திட்டத்தில் NAFED-க்கு ஏற்படும் இழப்புகளை மத்திய அரசே முழுமையாக ஈடுசெய்கிறது."
        },

        # CS_R_025: Handloom Cooperatives Welfare Impact
        {
            "subtopic": "Handloom Cooperatives Welfare",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Handloom cooperatives in Tamil Nadu have played a transformative role in poverty alleviation among rural artisan communities.\nReason (R): Weavers' cooperative societies provide organized supply of subsidized yarn, protect artisans from usurious private master weavers, and ensure assured institutional buyback through Co-optex.\nIn the context of the above statements, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) மற்றொன்று காரணம் (R) எனக் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): தமிழ்நாட்டில் கைத்தறிக் கூட்டுறவு சங்கங்கள் கிராமப்புறக் கைவினைக் குடும்பங்களின் வறுமை ஒழிப்பில் ஒரு மாற்றத்தை ஏற்படுத்தியுள்ளன.\nகாரணம் (R): நெசவாளர் கூட்டுறவு சங்கங்கள் மானிய விலையில் நூல் வழங்கி, தனியார் இடைத்தரகர்களின் சுரண்டலிலிருந்து பாதுகாத்து, கோ-ஆப்லெக்ஸ் மூலம் உறுதியான கொள்முதலை உறுதி செய்கின்றன.\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்."),
                ("Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation of Assertion (A).", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) சரியானது, ஆனால் காரணம் (R) தவறானது."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியானது.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains how the institutional cooperative structure eliminated middleman exploitation, stabilizing rural weaver livelihoods across Tamil Nadu.",
            "exp_ta": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். மூலப்பொருள் வழங்கி கோ-ஆப்லெக்ஸ் மூலம் உற்பத்தியைக் கொள்முதல் செய்வதே நெசவாளர்களின் பொருளாதார வளர்ச்சிக்கு அடிப்படையானது.",
            "why_a_en": "Correct. Institutional supply and buyback under cooperation directly explains poverty reduction among weavers.",
            "why_a_ta": "சரி. கூட்டுறவு மூலம் வழங்கப்படும் உள்ளீடுகளும் கொள்முதலுமே நெசவாளர்களின் வறுமை ஒழிப்புக்குக் காரணமாகும்.",
            "why_b_en": "Incorrect. Reason (R) directly explains Assertion (A).",
            "why_b_ta": "தவறு. காரணம் (R) கூற்று (A)-விற்கு நேரடி விளக்கமாகும்.",
            "why_c_en": "Incorrect. Both statements are true.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
            "why_d_en": "Incorrect. Assertion (A) is true.",
            "why_d_ta": "தவறு. கூற்று (A) சரியானது.",
            "tip_en": "Co-optex + Primary Weavers' Societies = Backbone of Tamil Nadu's non-farm rural employment.",
            "tip_ta": "கோ-ஆப்லெக்ஸ் + தொடக்க நெசவாளர் சங்கங்கள் = தமிழ்நாட்டின் விவசாயம் அல்லாத கிராமப்புற வேலைவாய்ப்பின் முதுகெலும்பு.",
            "fact_en": "Tamil Nadu operates the Weavers' Contributory Pension Scheme to provide old-age security.",
            "fact_ta": "நெசவாளர்களுக்கு முதியோர் பாதுகாப்பு வழங்க தமிழ்நாடு நெசவாளர் ஓய்வூதியத் திட்டத்தை செயல்படுத்துகிறது."
        }
    ]


def build_reasoning_file():
    raw_list = get_reasoning_raw_questions() + get_reasoning_questions_batch2()
    print(f"Loaded {len(raw_list)} raw Reasoning questions.")
    assert len(raw_list) == 25, f"Expected 25 questions, got {len(raw_list)}"

    questions = []
    for idx, item in enumerate(raw_list, start=1):
        qid = f"CS_R_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_coop_q(
            qid=qid,
            diff="Hard" if idx % 2 == 0 else "Medium",
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
            tags=["polity", "cooperative_societies", "reasoning", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    # Randomize and balance answer keys: 6-7 per option, max run <= 2
    balanced = randomize_and_balance_dataset(questions, seed=303)
    key_dist = Counter(q["correct_answer"] for q in balanced)
    print(f"Balanced Key Distribution: {dict(key_dist)}")

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cooperative_societies_reasoning.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Reasoning MCQs to {out_path}")

    # Validation
    rep = ContentValidator.validate_file(out_path, expected_count=25, expected_prefix="CS_R_")
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
