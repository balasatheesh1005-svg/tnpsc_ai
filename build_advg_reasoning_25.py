# -*- coding: utf-8 -*-
"""
Builder for Advocate General of a State - Reasoning / Assertion-Reason (25 MCQs: ADVG_R_001 to ADVG_R_025).
Strict 24-field schema, fully bilingual, high-yield TNPSC format.
Target Key Distribution: 7 A, 6 B, 6 C, 6 D.
"""
import json
import os
import shutil
from advg_mcq_helper import make_advg_q
from tools.nova_content_engine.validator import ContentValidator

def get_reasoning_questions():
    qs = []
    
    std_a_en = "Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A)"
    std_a_ta = "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்"
    
    std_b_en = "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A)"
    std_b_ta = "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கம் அல்ல"
    
    std_c_en = "Assertion (A) is true, but Reason (R) is false"
    std_c_ta = "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு"
    
    std_d_en = "Assertion (A) is false, but Reason (R) is true"
    std_d_ta = "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி"

    def add_ar(qid, subtopic, a_en, a_ta, r_en, r_ta, correct_key,
               exp_en, exp_ta, why_a_en, why_a_ta, why_b_en, why_b_ta,
               why_c_en, why_c_ta, why_d_en, why_d_ta, tip_en, tip_ta, fact_en, fact_ta):
        en_stem = f"Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): {a_en}\nReason (R): {r_en}\nIn the context of the above statements, which of the following is correct?"
        ta_stem = f"கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): {a_ta}\nகாரணம் (R): {r_ta}\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?"
        
        qs.append(make_advg_q(
            qid=qid, diff="Medium", qtype="Assertion-Reason", subtopic=subtopic,
            en_stem=en_stem, ta_stem=ta_stem,
            en_a=std_a_en, ta_a=std_a_ta, en_b=std_b_en, ta_b=std_b_ta,
            en_c=std_c_en, ta_c=std_c_ta, en_d=std_d_en, ta_d=std_d_ta,
            correct_key=correct_key, exp_en=exp_en, exp_ta=exp_ta,
            why_a_en=why_a_en, why_a_ta=why_a_ta, why_b_en=why_b_en, why_b_ta=why_b_ta,
            why_c_en=why_c_en, why_c_ta=why_c_ta, why_d_en=why_d_en, why_d_ta=why_d_ta,
            tip_en=tip_en, tip_ta=tip_ta, fact_en=fact_en, fact_ta=fact_ta
        ))

    # --- 7 Questions with Key 'A' ---
    add_ar(
        "ADVG_R_001", "Tenure and Resignation",
        "The Advocate General of a State conventionally tenders his resignation whenever the State Ministry resigns or is replaced.",
        "மாநில அமைச்சரவை பதவி விலகும் போதோ அல்லது மாற்றப்படும் போதோ வழக்கமாக தலைமை வழக்கறிஞரும் தனது பதவி விலகல் கடிதத்தை சமர்ப்பிக்கிறார்.",
        "He is appointed by the Governor on the advice of the Council of Ministers, and the government is entitled to have counsel in whom it reposes trust.",
        "அமைச்சரவையின் ஆலோசனையின் பேரில் ஆளுநரால் அவர் நியமிக்கப்படுகிறார், மேலும் தான் நம்பும் ஒரு வழக்கறிஞரைக் கொண்டிருக்க அரசுக்கு முழு உரிமை உண்டு.",
        "A",
        "Both (A) and (R) are true, and (R) correctly explains why the Advocate General conventionally resigns with the fall of the Ministry.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் அமைச்சரவை வீழும் போது தலைமை வழக்கறிஞர் ஏன் பதவி விலகுகிறார் என்பதற்கு (R) சரியான விளக்கமாகும்.",
        "Correct. (A) and (R) are true, and (R) is the valid explanation.", "சரி. (A) மற்றும் (R) சரி, மேலும் (R) சரியான விளக்கமாகும்.",
        "Incorrect. (R) directly explains the rationale for the convention.", "தவறு. (R) மரபுக்கான காரணத்தை நேரடியாக விளக்குகிறது.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Convention: AG resigns when government falls so the new regime can appoint its trusted counsel.",
        "மரபு: புதிய அரசு தனக்கு நம்பிக்கையான வழக்கறிஞரை நியமிக்க ஏதுவாக அரசு வீழும் போது AG பதவி விலகுகிறார்.",
        "Article 165(3) provides tenure during pleasure, enabling this convention.",
        "உறுப்பு 165(3) விருப்பப் பதவிக்காலத்தை வழங்கி இந்த மரபை செயல்படுத்துகிறது."
    )

    add_ar(
        "ADVG_R_002", "Article 177 Legislative Presence",
        "Under Article 177, the Advocate General has the right to speak and take part in the proceedings of the State Legislature, but cannot vote.",
        "உறுப்பு 177-ன் கீழ் சட்டமன்ற நடவடிக்கைகளில் பேசவும் பங்கேற்கவும் தலைமை வழக்கறிஞருக்கு உரிமை உண்டு, ஆனால் வாக்களிக்க முடியாது.",
        "The constitutional scheme permits the Legislature to benefit from his expert legal guidance while preserving the democratic principle that only elected representatives can enact laws.",
        "அரசியலமைப்பு கட்டமைப்பு சட்டமன்றம் அவரது நிபுணத்துவ சட்ட ஆலோசனையைப் பெற அனுமதிக்கும் அதே வேளையில், தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகள் மட்டுமே சட்டங்களை இயற்ற முடியும் என்ற ஜனநாயகக் கோட்பாட்டையும் பாதுகாக்கிறது.",
        "A",
        "Both (A) and (R) are true, and (R) correctly explains the democratic rationale behind Article 177.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் உறுப்பு 177-ன் பின்னணியில் உள்ள ஜனநாயகக் காரணத்தை (R) சரியாக விளக்குகிறது.",
        "Correct. (A) and (R) are true, and (R) explains (A).", "சரி. (A) மற்றும் (R) சரி, மேலும் (R) விளக்குகிறது.",
        "Incorrect. (R) is the direct constitutional explanation.", "தவறு. (R) நேரடி அரசியலமைப்பு விளக்கமாகும்.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Art 177 balances legal expertise with democratic legitimacy: Speak = Yes, Vote = No.",
        "உறுப்பு 177 சட்ட நிபுணத்துவத்தை ஜனநாயக சட்டபூர்வ தன்மையோடு சமநிலைப்படுத்துகிறது: பேசலாம் = ஆம், வாக்களிக்கலாம் = இல்லை.",
        "This applies equally to both Assembly and Council.",
        "இது பேரவை மற்றும் மேலவை ஆகிய இரண்டிற்கும் சமமாகப் பொருந்தும்."
    )

    add_ar(
        "ADVG_R_003", "Criminal Defense Conflict",
        "The Advocate General cannot defend an accused person in a criminal prosecution without the permission of the State Government.",
        "மாநில அரசின் அனுமதியின்றி குற்றவியல் வழக்கில் குற்றம் சாட்டப்பட்ட நபருக்காக தலைமை வழக்கறிஞரால் ஆஜராகி வாதாட முடியாது.",
        "In criminal cases, the State itself is the prosecuting authority, and defending an accused creates an inherent conflict of interest with his public duties.",
        "குற்றவியல் வழக்குகளில் அரசே வழக்கை நடத்தும் அதிகார அமைப்பாகும், மேலும் குற்றவாளியை ஆதரிப்பது அவரது பொதுக் கடமைகளோடு நேரடி நலன் முரண்பாட்டை உருவாக்குகிறது.",
        "A",
        "Both (A) and (R) are true, and (R) correctly explains why defending an accused requires prior State sanction.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் குற்றவாளியை ஆதரிக்க அரசின் முன் அனுமதி ஏன் தேவை என்பதற்கு (R) சரியான விளக்கமாகும்.",
        "Correct. (A) and (R) are true, and (R) explains (A).", "சரி. (A) மற்றும் (R) சரி, மேலும் (R) விளக்குகிறது.",
        "Incorrect. (R) is the precise reason for the restriction.", "தவறு. (R) இக்கட்டுப்பாட்டிற்கான துல்லியமான காரணமாகும்.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Conflict of interest: State prosecutes crimes; hence AG cannot defend the accused without state consent.",
        "நலன் முரண்பாடு: அரசு குற்றவியல் வழக்குகளைத் தொடுக்கிறது; எனவே அரசு அனுமதியின்றி AG குற்றவாளியை ஆதரிக்க முடியாது.",
        "Similarly, he cannot accept company directorships without government sanction.",
        "இதேபோல், அரசு அனுமதியின்றி நிறுவன இயக்குநர் பதவிகளையும் அவர் ஏற்க முடியாது."
    )

    add_ar(
        "ADVG_R_004", "Private Practice Permissibility",
        "The Advocate General of a State is permitted to engage in private legal practice.",
        "மாநில தலைமை வழக்கறிஞர் தனியாராக வழக்கறிஞர் தொழில் செய்ய அனுமதிக்கப்படுகிறார்.",
        "The Advocate General is a professional law officer holding office during pleasure, and is not a full-time salaried government servant holding a civil post.",
        "தலைமை வழக்கறிஞர் விருப்பக் கோட்பாட்டின் கீழ் பதவி வகிக்கும் ஒரு தொழில்முறை சட்ட அதிகாரி ஆவார், அவர் ஒரு குடிமைப் பதவியை வகிக்கும் முழுநேர சம்பள அரசு ஊழியர் அல்ல.",
        "A",
        "Both (A) and (R) are true, and (R) correctly explains why private practice is not barred.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் தனியார் தொழில் ஏன் தடை செய்யப்படவில்லை என்பதற்கு (R) சரியான விளக்கமாகும்.",
        "Correct. (A) and (R) are true, and (R) explains (A).", "சரி. (A) மற்றும் (R) சரி, மேலும் (R) விளக்குகிறது.",
        "Incorrect. (R) is the constitutional explanation.", "தவறு. (R) அரசியலமைப்பு ரீதியான விளக்கமாகும்.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "He is counsel for the government, not an administrative civil servant under Article 311.",
        "அவர் அரசின் வழக்கறிஞர், உறுப்பு 311-ன் கீழான நிர்வாக அரசு ஊழியர் அல்ல.",
        "He retains his enrolment as an advocate on the Bar Council rolls.",
        "பார் கவுன்சில் பதிவேட்டில் வழக்கறிஞராக தனது பதிவை அவர் தக்க வைத்துக் கொள்கிறார்."
    )

    add_ar(
        "ADVG_R_005", "M.T. Khan Additional AG Status",
        "The post of Additional Advocate General is not a constitutional office under Article 165.",
        "கூடுதல் தலைமை வழக்கறிஞர் பதவி உறுப்பு 165-ன் கீழ் ஓர் அரசியலமைப்பு பதவி அல்ல.",
        "Article 165 of the Constitution contemplates only ONE Advocate General for each State.",
        "அரசியலமைப்பின் உறுப்பு 165 ஒவ்வொரு மாநிலத்திற்கும் ஒரே ஒரு தலைமை வழக்கறிஞரையே கருதுகிறது.",
        "A",
        "Both (A) and (R) are true, and (R) is the core constitutional reasoning laid down in M.T. Khan v. Govt of AP (2004).",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் எம்.டி. கான் வழக்கில் (2004) வகுக்கப்பட்ட முக்கிய அரசியலமைப்பு விளக்கம் (R) ஆகும்.",
        "Correct. (A) and (R) are true, and (R) explains (A).", "சரி. (A) மற்றும் (R) சரி, மேலும் (R) விளக்குகிறது.",
        "Incorrect. (R) directly explains the non-constitutional status of Additional AGs.", "தவறு. (R) கூடுதல் AG-ன் அரசியலமைப்பற்ற நிலையை நேரடியாக விளக்குகிறது.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "M.T. Khan (2004): Article 165 is singular; Additional AGs are created under executive power (Art 162).",
        "எம்.டி. கான் (2004): உறுப்பு 165 ஒற்றையானது; கூடுதல் AG-க்கள் நிர்வாக அதிகாரத்தின் கீழ் (உறுப்பு 162) உருவாக்கப்படுகின்றனர்.",
        "Constitutional duties of the AG cannot be delegated to Additional AGs.",
        "AG-ன் அரசியலமைப்பு கடமைகளை கூடுதல் AG-க்களுக்கு மாற்ற முடியாது."
    )

    add_ar(
        "ADVG_R_006", "Distinguished Jurist Exclusion",
        "An eminent jurist who has never held judicial office or practiced in a High Court cannot be appointed as Advocate General.",
        "நீதித்துறை பதவியை வகிக்காத அல்லது உயர் நீதிமன்றத்தில் பணியாற்றாத ஒரு புகழ்பெற்ற சட்ட நிபுணரை தலைமை வழக்கறிஞராக நியமிக்க முடியாது.",
        "Article 217(2) prescribing qualifications for High Court Judges does not contain a 'distinguished jurist' category, unlike Article 124(3)(c) for the Supreme Court.",
        "உச்ச நீதிமன்றத்திற்கான உறுப்பு 124(3)(c) போலன்றி, உயர் நீதிமன்ற நீதிபதிகளுக்கான தகுதிகளைக் கூறும் உறுப்பு 217(2)-ல் 'சிறந்த சட்ட நிபுணர்' என்ற வகைப்பாடு இல்லை.",
        "A",
        "Both (A) and (R) are true, and (R) correctly explains why a distinguished jurist cannot be appointed as Advocate General.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் ஒரு சட்ட நிபுணரை ஏன் அட்வகேட் ஜெனரலாக நியமிக்க முடியாது என்பதற்கு (R) சரியான விளக்கமாகும்.",
        "Correct. (A) and (R) are true, and (R) explains (A).", "சரி. (A) மற்றும் (R) சரி, மேலும் (R) விளக்குகிறது.",
        "Incorrect. (R) is the precise constitutional reason.", "தவறு. (R) துல்லியமான அரசியலமைப்பு காரணமாகும்.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Supreme Court (Art 124(3)(c)) = Jurist eligible; High Court (Art 217(2)) = Jurist NOT eligible.",
        "உச்ச நீதிமன்றம் (உறுப்பு 124(3)(c)) = சட்ட நிபுணர் தகுதி உண்டு; உயர் நீதிமன்றம் (உறுப்பு 217(2)) = சட்ட நிபுணர் தகுதி இல்லை.",
        "AG requires HC Judge qualifications, so jurists are ineligible for AG.",
        "AG-க்கு உயர் நீதிமன்ற நீதிபதி தகுதி தேவைப்படுவதால், சட்ட நிபுணர்கள் AG-க்கு தகுதியற்றவர்கள்."
    )

    add_ar(
        "ADVG_R_007", "Contempt Consent Quasi-Judicial",
        "A Writ of Mandamus cannot be issued by a High Court commanding the Advocate General to grant his consent under Section 15 of the Contempt of Courts Act, 1971.",
        "நீதிமன்ற அவமதிப்புச் சட்டம் 1971 பிரிவு 15-ன் கீழ் இசைவு வழங்குமாறு தலைமை வழக்கறிஞருக்கு உத்தரவிட்டு உயர் நீதிமன்றத்தால் மாண்டமஸ் பேராணையை பிறப்பிக்க முடியாது.",
        "The grant or refusal of consent under Section 15 is a quasi-judicial statutory discretion, and Mandamus cannot compel a quasi-judicial authority to exercise its discretion in a particular manner.",
        "பிரிவு 15-ன் கீழ் இசைவு வழங்குவது அல்லது மறுப்பது ஒரு நீதித்துறை போன்ற சட்டப்பூர்வ விருப்புரிமையாகும்; தனது விருப்புரிமையை ஒரு குறிப்பிட்ட வழியில் பயன்படுத்துமாறு நீதித்துறை போன்ற ஓர் அதிகார அமைப்பை மாண்டமஸ் கட்டாயப்படுத்த முடியாது.",
        "A",
        "Both (A) and (R) are true, and (R) correctly explains the jurisdictional limitation on Mandamus established in P.N. Duda v. P. Shiv Shanker.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் பி.என். துதா வழக்கில் நிறுவப்பட்ட மாண்டமஸ் பேராணை மீதான அதிகார வரம்பு வரம்பை (R) சரியாக விளக்குகிறது.",
        "Correct. (A) and (R) are true, and (R) explains (A).", "சரி. (A) மற்றும் (R) சரி, மேலும் (R) விளக்குகிறது.",
        "Incorrect. (R) is the established legal ground.", "தவறு. (R) நிலைநாட்டப்பட்ட சட்டக் காரணமாகும்.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Mandamus can direct the AG to 'consider and decide', but cannot direct him to 'grant consent'.",
        "மாண்டமஸ் AG-ஐ 'பரிசீலித்து முடிவெடுக்குமாறு' உத்தரவிடலாமே தவிர, 'இசைவு வழங்குமாறு' உத்தரவிட முடியாது.",
        "This protects the quasi-judicial independence of the Advocate General.",
        "இது தலைமை வழக்கறிஞரின் நீதித்துறை போன்ற சுதந்திரத்தைப் பாதுகாக்கிறது."
    )

    # --- 6 Questions with Key 'B' ---
    add_ar(
        "ADVG_R_008", "Privileges and Remuneration Independence",
        "The Advocate General enjoys all the powers, privileges, and immunities of a member of the State Legislature under Article 194(4).",
        "உறுப்பு 194(4)-ன் கீழ் தலைமை வழக்கறிஞர் சட்டமன்ற உறுப்பினரின் அனைத்து அதிகாரங்கள், சிறப்புரிமைகள் மற்றும் விலக்களிப்புகளை அனுபவிக்கிறார்.",
        "The remuneration of the Advocate General is determined by the Governor under Article 165(3) and is not fixed by the Constitution.",
        "தலைமை வழக்கறிஞரின் ஊதியம் உறுப்பு 165(3)-ன் கீழ் ஆளுநரால் தீர்மானிக்கப்படுகிறது மற்றும் அரசியலமைப்பால் நிர்ணயிக்கப்படவில்லை.",
        "B",
        "Both (A) and (R) are true constitutional statements, but (R) deals with remuneration and does NOT explain why or how he enjoys legislative privileges under Article 194(4).",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியான அரசியலமைப்பு கூற்றுகள், ஆனால் (R) ஊதியம் பற்றியது மற்றும் உறுப்பு 194(4)-ன் கீழ் அவர் ஏன் சட்டமன்ற சிறப்புரிமைகளைப் பெறுகிறார் என்பதை விளக்கவில்லை.",
        "Incorrect. (R) is not the explanation of (A).", "தவறு. (R) என்பது (A)-வின் விளக்கம் அல்ல.",
        "Correct. Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).", "சரி. (A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-விற்கு சரியான விளக்கம் அல்ல.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Assertion deals with Article 194(4); Reason deals with Article 165(3). Separate constitutional concepts.",
        "கூற்று உறுப்பு 194(4) பற்றியது; காரணம் உறுப்பு 165(3) பற்றியது. தனித்தனி அரசியலமைப்பு விவகாரங்கள்.",
        "Both are true facts about the Advocate General.",
        "இரண்டுமே தலைமை வழக்கறிஞர் குறித்த உண்மையான விபரங்கள்."
    )

    add_ar(
        "ADVG_R_009", "Pre-audience and Appointment Independence",
        "Under Section 23 of the Advocates Act, 1961, the Advocate General has the right of pre-audience over all other advocates appearing in the High Court.",
        "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 23-ன் கீழ், உயர் நீதிமன்றத்தில் முன்னிலையாகும் மற்ற அனைத்து வழக்கறிஞர்களுக்கும் மேலாக தலைமை வழக்கறிஞர் முன்னுரிமை பெற்றுள்ளார்.",
        "The Governor appoints the Advocate General on the aid and advice of the Council of Ministers headed by the Chief Minister.",
        "முதலமைச்சர் தலைமையிலான அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின் பேரில் ஆளுநர் தலைமை வழக்கறிஞரை நியமிக்கிறார்.",
        "B",
        "Both statements are true. Pre-audience derives from Section 23 of the Advocates Act, 1961, while appointment is made under Article 165(1) read with Article 163. The method of appointment does not explain the statutory rule of pre-audience.",
        "இரண்டு கூற்றுகளுமே சரியானவை. முன்னுரிமை வழக்கறிஞர்கள் சட்டம் பிரிவு 23-லிருந்து பெறப்படுகிறது, நியமனம் உறுப்பு 165(1) மற்றும் 163-ன் கீழ் செய்யப்படுகிறது. நியமன முறை முன்னுரிமை விதியை விளக்கவில்லை.",
        "Incorrect. (R) does not explain the statutory pre-audience in (A).", "தவறு. (R) என்பது (A)-ல் உள்ள சட்டப்பூர்வ முன்னுரிமையை விளக்கவில்லை.",
        "Correct. Both are true, but (R) is NOT the explanation of (A).", "சரி. இரண்டும் சரி, ஆனால் (R) என்பது (A)-விற்கு விளக்கம் அல்ல.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Statutory pre-audience (Sec 23) vs Executive appointment (Art 165/163).",
        "சட்டப்பூர்வ முன்னுரிமை (பிரிவு 23) vs நிர்வாக நியமனம் (உறுப்பு 165/163).",
        "Both are established features of the office.",
        "இரண்டுமே இப்பொறுப்பின் நிறுவப்பட்ட அம்சங்கள்."
    )

    add_ar(
        "ADVG_R_010", "Article 131 Representation and Oath",
        "The Advocate General leads the legal representation of the State in original suits filed under Article 131 before the Supreme Court.",
        "உச்ச நீதிமன்றத்தில் உறுப்பு 131-ன் கீழ் தாக்கல் செய்யப்படும் அசல் வழக்குகளில் தலைமை வழக்கறிஞரே மாநிலத்தின் சட்டப் பிரதிநிதித்துவத்தை வழிநடத்துகிறார்.",
        "The Advocate General takes an administrative oath of allegiance upon assuming office as regulated by executive notifications.",
        "நிர்வாக அறிவிப்புகளால் ஒழுங்குபடுத்தப்படும் விசுவாசப் பிரமாணத்தை தலைமை வழக்கறிஞர் பதவியேற்பின் போது ஏற்கிறார்.",
        "B",
        "Both (A) and (R) are true statements. However, taking an oath of office is an administrative formality and does not explain why the AG leads original suits under Article 131 (which is based on his status as chief law officer).",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை. எனினும், உறுதிமொழி ஏற்பது ஒரு நிர்வாக நடைமுறையே தவிர, உறுப்பு 131 அசல் வழக்குகளை AG ஏன் வழிநடத்துகிறார் என்பதை விளக்கவில்லை.",
        "Incorrect. (R) is unrelated to Article 131 litigation.", "தவறு. (R) உறுப்பு 131 வழக்குடன் தொடர்புடையது அல்ல.",
        "Correct. Both statements are true, but (R) is NOT the explanation of (A).", "சரி. இரண்டு கூற்றுகளுமே சரி, ஆனால் (R) என்பது (A)-விற்கு விளக்கம் அல்ல.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Article 131 suits are inter-state or Union-State disputes in the apex court.",
        "உறுப்பு 131 வழக்குகள் உச்ச நீதிமன்றத்தில் உள்ள மாநிலங்களுக்கு இடையேயான அல்லது மத்திய-மாநில தாவாக்கள் ஆகும்.",
        "Oath is an administrative act upon assumption of charge.",
        "உறுதிமொழி என்பது பொறுப்பேற்பின் போது செய்யப்படும் ஓர் நிர்வாக நடவடிக்கை."
    )

    add_ar(
        "ADVG_R_011", "Article 177 Non-Voting and Pleasure Tenure",
        "The Advocate General cannot vote on any bill in the State Legislative Assembly under Article 177.",
        "உறுப்பு 177-ன் கீழ் மாநில சட்டப் பேரவையில் எந்தவொரு மசோதாவிலும் தலைமை வழக்கறிஞரால் வாக்களிக்க முடியாது.",
        "The Advocate General holds office during the pleasure of the Governor under Article 165(3).",
        "உறுப்பு 165(3)-ன் கீழ் தலைமை வழக்கறிஞர் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார்.",
        "B",
        "Both statements are true. However, holding office during pleasure is a feature of his executive tenure under Article 165(3), which does not explain why Article 177 bars him from voting (which is based on non-membership in the elected House).",
        "இரண்டு கூற்றுகளுமே சரியானவை. எனினும், விருப்பத்தின் பேரில் பதவி வகிப்பது உறுப்பு 165(3)-ன் கீழான அவரது நிர்வாகப் பதவிக்கால அம்சம்; உறுப்பு 177 அவரை ஏன் வாக்களிக்கத் தடை செய்கிறது (அவர் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் அல்ல என்பதால்) என்பதை இது விளக்கவில்லை.",
        "Incorrect. (R) does not explain the voting prohibition in (A).", "தவறு. (R) என்பது (A)-ல் உள்ள வாக்குரிமைத் தடையை விளக்கவில்லை.",
        "Correct. Both statements are true, but (R) is NOT the correct explanation of (A).", "சரி. இரண்டு கூற்றுகளுமே சரி, ஆனால் (R) என்பது (A)-விற்கு சரியான விளக்கம் அல்ல.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Voting prohibition is based on democratic legitimacy; pleasure tenure is based on executive discretion.",
        "வாக்குரிமைத் தடை ஜனநாயக சட்டபூர்வ தன்மையை அடிப்படையாகக் கொண்டது; விருப்பப் பதவிக்காலம் நிர்வாக விருப்புரிமையை அடிப்படையாகக் கொண்டது.",
        "Both are distinct constitutional rules.",
        "இரண்டுமே தனித்தனி அரசியலமைப்பு விதிகள்."
    )

    add_ar(
        "ADVG_R_012", "Bar Council Role and Part VI Location",
        "The Advocate General of a State is an ex-officio member of the State Bar Council under Section 3(2)(a) of the Advocates Act, 1961.",
        "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 3(2)(a)-ன் கீழ் மாநில தலைமை வழக்கறிஞர் மாநில பார் கவுன்சிலின் பதவிவழி உறுப்பினர் ஆவார்.",
        "The office of the Advocate General is dealt with in Part VI of the Constitution of India under Article 165.",
        "இந்திய அரசியலமைப்பின் பகுதி VI-ல் உள்ள உறுப்பு 165-ன் கீழ் தலைமை வழக்கறிஞர் அலுவலகம் கையாளப்படுகிறது.",
        "B",
        "Both statements are true. Ex-officio membership is a statutory provision under the Advocates Act, 1961, while Part VI is the constitutional location of Article 165. The constitutional chapter location does not explain statutory bar council membership.",
        "இரண்டு கூற்றுகளுமே சரியானவை. பதவிவழி உறுப்பினர் நிலை என்பது வழக்கறிஞர்கள் சட்டத்தின் கீழான சட்டப்பூர்வ விதி, பகுதி VI என்பது உறுப்பு 165-ன் அரசியலமைப்பு அமைவிடம். பகுதி VI என்பது பார் கவுன்சில் உறுப்பினர் நிலையை விளக்கவில்லை.",
        "Incorrect. (R) does not explain statutory Bar Council membership in (A).", "தவறு. (R) என்பது (A)-ல் உள்ள சட்டப்பூர்வ பார் கவுன்சில் உறுப்பினர் நிலையை விளக்கவில்லை.",
        "Correct. Both statements are true, but (R) is NOT the explanation of (A).", "சரி. இரண்டு கூற்றுகளுமே சரி, ஆனால் (R) என்பது (A)-விற்கு விளக்கம் அல்ல.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Statutory bar role vs Constitutional chapter location.",
        "சட்டப்பூர்வ வழக்கறிஞர் சங்கப் பங்கு vs அரசியலமைப்பு அத்தியாய அமைவிடம்.",
        "Both are true facts.",
        "இரண்டுமே உண்மையான தகவல்கள்."
    )

    add_ar(
        "ADVG_R_013", "Subordinate Courts and Advisory Nature",
        "The Advocate General has the right of audience in any court within the territory of the State, including subordinate district courts.",
        "கீழ்மை மாவட்ட நீதிமன்றங்கள் உட்பட மாநில எல்லைக்குள் உள்ள எந்தவொரு நீதிமன்றத்திலும் முன்னிலையாகி வாதாடும் உரிமை தலைமை வழக்கறிஞருக்கு உண்டு.",
        "The legal advice tendered by the Advocate General is advisory in nature and not legally binding on the State Government.",
        "தலைமை வழக்கறிஞர் வழங்கும் சட்ட ஆலோசனை வழிகாட்டும் தன்மை கொண்டதே தவிர மாநில அரசை சட்டப்பூர்வமாகக் கட்டுப்படுத்தாது.",
        "B",
        "Both statements are true. Right of audience in all state courts derives from his status as chief law officer, while the advisory nature of his counsel is a principle of executive governance. The advisory nature of advice does not explain right of audience in courts.",
        "இரண்டு கூற்றுகளுமே சரியானவை. மாநில நீதிமன்றங்களில் வாதாடும் உரிமை முதன்மை சட்ட அதிகாரி என்ற நிலையிலிருந்து பெறப்படுகிறது; ஆலோசனையின் வழிகாட்டும் தன்மை நிர்வாக ஆளுகையின் கோட்பாடு ஆகும். ஆலோசனையின் தன்மை நீதிமன்ற வாதாடும் உரிமையை விளக்கவில்லை.",
        "Incorrect. (R) is unrelated to courtroom audience rights.", "தவறு. (R) நீதிமன்ற வாதாடும் உரிமையோடு தொடர்புடையது அல்ல.",
        "Correct. Both statements are true, but (R) is NOT the explanation of (A).", "சரி. இரண்டு கூற்றுகளுமே சரி, ஆனால் (R) என்பது (A)-விற்கு விளக்கம் அல்ல.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளுமே சரியானவை.",
        "Audience in subordinate courts = Procedural litigation right; Advisory advice = Executive counsel principle.",
        "கீழ் நீதிமன்றங்களில் வாதாடுதல் = நடைமுறை வழக்கு உரிமை; வழிகாட்டும் ஆலோசனை = நிர்வாக சட்டக் கோட்பாடு.",
        "Both are independently true.",
        "இரண்டுமே தனித்தனியாக உண்மையானவை."
    )

    # --- 6 Questions with Key 'C' ---
    add_ar(
        "ADVG_R_014", "Committee Voting False",
        "Under Article 177, the Advocate General can be named as a member of any committee of the State Legislature.",
        "உறுப்பு 177-ன் கீழ் மாநில சட்டமன்றத்தின் எந்தவொரு குழுவிலும் தலைமை வழக்கறிஞர் ஓர் உறுப்பினராக பெயரிடப்படலாம்.",
        "When named as a committee member, the Advocate General acquires full constitutional voting rights in that committee.",
        "குழு உறுப்பினராக பெயரிடப்படும் போது, அக்குழுவில் தலைமை வழக்கறிஞர் முழு அரசியலமைப்பு வாக்குரிமையைப் பெறுகிறார்.",
        "C",
        "Assertion (A) is true under Article 177. Reason (R) is false because Article 177 explicitly states that he shall not be entitled to vote, which applies to both the House and any committee thereof.",
        "கூற்று (A) சரி (உறுப்பு 177). காரணம் (R) தவறு, ஏனெனில் உறுப்பு 177 அவர் வாக்களிக்க உரிமை பெறமாட்டார் என்று தெளிவாகக் கூறுகிறது; இது அவைக்கும் அதன் குழுவிற்கும் பொருந்தும்.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Correct. Assertion (A) is true, but Reason (R) is false.", "சரி. கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு.",
        "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
        "Art 177 bar applies to committees: He can speak and participate in committee, but CANNOT vote.",
        "உறுப்பு 177 தடை குழுக்களுக்கும் பொருந்தும்: குழுவில் பேசலாம், பங்கேற்கலாம், ஆனால் வாக்களிக்க முடியாது.",
        "This is an absolute prohibition.",
        "இது ஒரு முழுமையான தடையாகும்."
    )

    add_ar(
        "ADVG_R_015", "Nagpur HC Retirement Age False",
        "A retired High Court Judge can legally be appointed as the Advocate General of a State.",
        "ஓய்வுபெற்ற உயர் நீதிமன்ற நீதிபதி ஒருவரை சட்டப்பூர்வமாக ஒரு மாநிலத்தின் தலைமை வழக்கறிஞராக நியமிக்க முடியும்.",
        "The Constitution of India prescribes that the Advocate General must retire upon completing 62 years of age.",
        "தலைமை வழக்கறிஞர் 62 வயதை நிறைவு செய்தவுடன் ஓய்வு பெற வேண்டும் என்று இந்திய அரசியலமைப்பு பரிந்துரைக்கிறது.",
        "C",
        "Assertion (A) is true (settled in G.D. Karkare and Atlas Cycle cases). Reason (R) is false because the Constitution prescribes NO retirement age for the Advocate General.",
        "கூற்று (A) சரி (கார்கரே மற்றும் அட்லஸ் சைக்கிள் வழக்குகள்). காரணம் (R) தவறு, ஏனெனில் தலைமை வழக்கறிஞருக்கு அரசியலமைப்பு எந்த ஓய்வு வயதையும் குறிப்பிடவில்லை.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Correct. Assertion (A) is true, but Reason (R) is false.", "சரி. கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு.",
        "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
        "G.D. Karkare v. T.L. Shevde (1952): 62-year retirement age does not apply to the Advocate General.",
        "ஜி.டி. கார்கரே வழக்கு (1952): 62 வயது ஓய்வு வரம்பு தலைமை வழக்கறிஞருக்குப் பொருந்தாது.",
        "Article 165(3) leaves tenure entirely to the pleasure of the Governor.",
        "உறுப்பு 165(3) பதவிக்காலத்தை முழுமையாக ஆளுநரின் விருப்பத்திற்கே விட்டுவிடுகிறது."
    )

    add_ar(
        "ADVG_R_016", "Cabinet Rank False",
        "The Advocate General is the first and highest law officer of the State Government.",
        "தலைமை வழக்கறிஞரே மாநில அரசின் முதன்மை மற்றும் மிக உயர்ந்த சட்ட அதிகாரி ஆவார்.",
        "The Advocate General is an ex-officio Cabinet Minister in the State Council of Ministers.",
        "தலைமை வழக்கறிஞர் மாநில அமைச்சரவையில் ஒரு பதவிவழி அமைச்சரவை அமைச்சர் ஆவார்.",
        "C",
        "Assertion (A) is true. Reason (R) is false because the Advocate General is NOT a member of the Cabinet or Council of Ministers.",
        "கூற்று (A) சரி. காரணம் (R) தவறு, ஏனெனில் தலைமை வழக்கறிஞர் அமைச்சரவையின் அல்லது அமைச்சர்கள் குழுவின் உறுப்பினர் அல்ல.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Correct. Assertion (A) is true, but Reason (R) is false.", "சரி. கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு.",
        "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
        "Advocate General = Top Law Officer; Law Minister = Cabinet Member.",
        "அட்வகேட் ஜெனரல் = தலைமை சட்ட அதிகாரி; சட்ட அமைச்சர் = அமைச்சரவை உறுப்பினர்.",
        "He does not hold political or ministerial office.",
        "அவர் அரசியல் அல்லது அமைச்சர் பதவியை வகிப்பதில்லை."
    )

    add_ar(
        "ADVG_R_017", "Mandamus for Consent False",
        "A private citizen wishing to move a motion for criminal contempt in the High Court must obtain the written consent of the Advocate General under Section 15 of the Contempt of Courts Act, 1971.",
        "உயர் நீதிமன்றத்தில் குற்றவியல் அவமதிப்பு மனுவைத் தாக்கல் செய்ய விரும்பும் ஒரு தனிநபர், நீதிமன்ற அவமதிப்புச் சட்டம் 1971 பிரிவு 15-ன் கீழ் தலைமை வழக்கறிஞரின் எழுத்துப்பூர்வ இசைவைப் பெற வேண்டும்.",
        "If the Advocate General refuses consent, the High Court will issue a Writ of Mandamus compelling him to grant consent within 30 days.",
        "தலைமை வழக்கறிஞர் இசைவை மறுத்தால், 30 நாட்களுக்குள் இசைவு வழங்குமாறு அவரை கட்டாயப்படுத்தி உயர் நீதிமன்றம் ஒரு மாண்டமஸ் பேராணையை பிறப்பிக்கும்.",
        "C",
        "Assertion (A) is true under Section 15(1)(b) of the Contempt of Courts Act. Reason (R) is false because the High Court cannot issue a mandamus commanding the AG to exercise his quasi-judicial discretion in a specific way (P.N. Duda v. P. Shiv Shanker).",
        "கூற்று (A) சரி (அவமதிப்புச் சட்டம் பிரிவு 15(1)(b)). காரணம் (R) தவறு, ஏனெனில் தனது நீதித்துறை போன்ற விருப்புரிமையை ஒரு குறிப்பிட்ட வழியில் பயன்படுத்துமாறு AG-க்கு உயர் நீதிமன்றம் மாண்டமஸ் பிறப்பிக்க முடியாது (பி.என். துதா வழக்கு).",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Correct. Assertion (A) is true, but Reason (R) is false.", "சரி. கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு.",
        "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
        "Mandamus cannot dictate quasi-judicial outcomes; the High Court can take suo motu action instead.",
        "மாண்டமஸ் நீதித்துறை போன்ற முடிவுகளை ஆணையிட முடியாது; உயர் நீதிமன்றம் தானாக முன்வந்து வழக்கை எடுக்கலாம்.",
        "This maintains statutory independence.",
        "இது சட்டப்பூர்வ சுதந்திரத்தைப் பாதுகாக்கிறது."
    )

    add_ar(
        "ADVG_R_018", "Consolidated Fund Charged False",
        "The Advocate General represents the State Government in commercial and constitutional arbitrations when instructed.",
        "அறிவுறுத்தப்படும் போது வணிக மற்றும் அரசியலமைப்பு நடுவர் மன்றங்களில் தலைமை வழக்கறிஞர் மாநில அரசைப் பிரதிநிதித்துவப்படுத்துகிறார்.",
        "The remuneration and allowances of the Advocate General are charged upon the Consolidated Fund of the State under Article 202(3).",
        "தலைமை வழக்கறிஞரின் ஊதியம் மற்றும் படிகள் உறுப்பு 202(3)-ன் கீழ் மாநில ஒருங்கிணைந்த நிதியில் சுமத்தப்பட்ட செலவினமாகும்.",
        "C",
        "Assertion (A) is true. Reason (R) is false because the remuneration of the Advocate General is NOT charged on the Consolidated Fund; it is an executive expenditure determined by the Governor and voted by the Legislature.",
        "கூற்று (A) சரி. காரணம் (R) தவறு, ஏனெனில் தலைமை வழக்கறிஞரின் ஊதியம் ஒருங்கிணைந்த நிதியில் சுமத்தப்பட்ட செலவு அல்ல; அது ஆளுநரால் தீர்மானிக்கப்பட்டு சட்டமன்றத்தால் வாக்களிக்கப்படும் செலவாகும்.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Correct. Assertion (A) is true, but Reason (R) is false.", "சரி. கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு.",
        "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
        "Article 202(3) lists HC judges' salaries as charged, but NOT the Advocate General's remuneration.",
        "உறுப்பு 202(3) உயர் நீதிமன்ற நீதிபதிகளின் சம்பளத்தை சுமத்தப்பட்டதாக பட்டியலிடுகிறது, அட்வகேட் ஜெனரலின் ஊதியத்தை அல்ல.",
        "Non-charged status reflects executive pleasure tenure.",
        "சுமத்தப்படாத நிலை நிர்வாக விருப்பப் பதவிக்காலத்தைப் பிரதிபலிக்கிறது."
    )

    add_ar(
        "ADVG_R_019", "Article 311 Protection False",
        "The Advocate General is an integral constitutional component of the State Executive under Part VI of the Constitution.",
        "அரசியலமைப்பின் பகுதி VI-ன் கீழ் தலைமை வழக்கறிஞர் மாநில நிர்வாகத்தின் ஒருங்கிணைந்த அரசியலமைப்பு அங்கம் ஆவார்.",
        "The Advocate General enjoys the constitutional protections against dismissal and reduction in rank under Article 311.",
        "பணிநீக்கம் மற்றும் பதவியிறக்கத்திற்கு எதிரான உறுப்பு 311-ன் கீழான அரசியலமைப்புப் பாதுகாப்புகளை தலைமை வழக்கறிஞர் அனுபவிக்கிறார்.",
        "C",
        "Assertion (A) is true under Articles 153-167 of Part VI. Reason (R) is false because the Advocate General holds office during pleasure, does not hold a 'civil post', and is NOT entitled to Article 311 protection.",
        "கூற்று (A) சரி (பகுதி VI உறுப்புகள் 153-167). காரணம் (R) தவறு, ஏனெனில் தலைமை வழக்கறிஞர் விருப்பத்தின் பேரில் பதவி வகிக்கிறார், அவர் ஒரு 'குடிமைப் பதவியை' வகிக்கவில்லை, எனவே உறுப்பு 311 பாதுகாப்புக்கு உரிமையற்றவர்.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Incorrect. (R) is false.", "தவறு. (R) தவறானது.",
        "Correct. Assertion (A) is true, but Reason (R) is false.", "சரி. கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு.",
        "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
        "Article 311 applies strictly to members of civil services and civil posts, not constitutional law officers.",
        "உறுப்பு 311 குடிமைப் பணி உறுப்பினர்களுக்கும் குடிமைப் பதவிகளுக்கும் மட்டுமே கண்டிப்பாகப் பொருந்தும், அரசியலமைப்பு சட்ட அதிகாரிகளுக்கு அல்ல.",
        "He can be removed without a formal departmental inquiry.",
        "துறைசார் விசாரணையின்றி அவரை நீக்க முடியும்."
    )

    # --- 6 Questions with Key 'D' ---
    add_ar(
        "ADVG_R_020", "High Court CJ Appointment False",
        "The Advocate General of a State is appointed by the Chief Justice of the High Court.",
        "மாநில தலைமை வழக்கறிஞர் உயர் நீதிமன்ற தலைமை நீதிபதியால் நியமிக்கப்படுகிறார்.",
        "Under Article 165(1), the person appointed must be qualified to be appointed as a Judge of a High Court.",
        "உறுப்பு 165(1)-ன் கீழ், நியமிக்கப்படும் நபர் உயர் நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுடையவராக இருக்க வேண்டும்.",
        "D",
        "Assertion (A) is false because the Governor appoints the Advocate General under Article 165(1). Reason (R) is true as Article 165(1) prescribes the qualification of being qualified to be an HC Judge.",
        "கூற்று (A) தவறு, ஏனெனில் உறுப்பு 165(1)-ன் கீழ் ஆளுநரே தலைமை வழக்கறிஞரை நியமிக்கிறார். காரணம் (R) சரி, ஏனெனில் உறுப்பு 165(1) உயர் நீதிமன்ற நீதிபதி தகுதியை பரிந்துரைக்கிறது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Correct. Assertion (A) is false, but Reason (R) is true.", "சரி. கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி.",
        "Governor appoints the AG on Cabinet advice; High Court Chief Justice has no appointment power under Art 165.",
        "அமைச்சரவை ஆலோசனையின்படி ஆளுநரே AG-யை நியமிக்கிறார்; உறுப்பு 165-ன் கீழ் தலைமை நீதிபதிக்கு நியமன அதிகாரம் இல்லை.",
        "Article 217(2) qualifications apply.",
        "உறுப்பு 217(2) தகுதிகள் பொருந்தும்."
    )

    add_ar(
        "ADVG_R_021", "Fixed 5-Year Tenure False",
        "The Constitution of India prescribes a fixed tenure of 5 years for the Advocate General of a State.",
        "இந்திய அரசியலமைப்பு மாநில தலைமை வழக்கறிஞருக்கு 5 ஆண்டுகள் என்ற நிலையான பதவிக்காலத்தை நிர்ணயிக்கிறது.",
        "Under Article 165(3), the Advocate General holds office during the pleasure of the Governor.",
        "உறுப்பு 165(3)-ன் கீழ், தலைமை வழக்கறிஞர் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார்.",
        "D",
        "Assertion (A) is false because the Constitution does not fix any term of office. Reason (R) is true as Article 165(3) expressly provides that he holds office during the pleasure of the Governor.",
        "கூற்று (A) தவறு, ஏனெனில் அரசியலமைப்பு எந்த பதவிக்காலத்தையும் நிர்ணயிக்கவில்லை. காரணம் (R) சரி, ஏனெனில் அவர் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிப்பார் என்று உறுப்பு 165(3) தெளிவாகக் கூறுகிறது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Correct. Assertion (A) is false, but Reason (R) is true.", "சரி. கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி.",
        "No fixed term: Governed by the pleasure doctrine under Article 165(3).",
        "நிலையான பதவிக்காலம் இல்லை: உறுப்பு 165(3)-ன் கீழான விருப்பக் கோட்பாட்டால் நிர்வகிக்கப்படுகிறது.",
        "Conventionally resigns when the government resigns.",
        "அரசு பதவி விலகும் போது வழக்கமாக பதவி விலகுகிறார்."
    )

    add_ar(
        "ADVG_R_022", "Quorum Counting False",
        "The physical presence of the Advocate General in the Assembly chamber counts towards the quorum of the House under Article 189(3).",
        "சட்டமன்ற அவையில் தலைமை வழக்கறிஞரின் இருப்பு உறுப்பு 189(3)-ன் கீழ் அவையின் குறைந்தபட்ச உறுப்பினர் எண்ணிக்கையில் (Quorum) கணக்கிடப்படுகிறது.",
        "Under Article 177, the Advocate General has the right to speak and take part in the proceedings of the Legislative Assembly.",
        "உறுப்பு 177-ன் கீழ், சட்டப் பேரவை நடவடிக்கைகளில் பேசவும் பங்கேற்கவும் தலைமை வழக்கறிஞருக்கு உரிமை உண்டு.",
        "D",
        "Assertion (A) is false because the Advocate General is not a member of the House, and only elected/nominated members count towards the quorum under Article 189(3). Reason (R) is true under Article 177.",
        "கூற்று (A) தவறு, ஏனெனில் தலைமை வழக்கறிஞர் அவையின் உறுப்பினர் அல்ல, தேர்ந்தெடுக்கப்பட்ட/நியமிக்கப்பட்ட உறுப்பினர்கள் மட்டுமே உறுப்பு 189(3)-ன் கீழ் கோரத்திற்கு கணக்கிடப்படுவர். காரணம் (R) சரி (உறுப்பு 177).",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Correct. Assertion (A) is false, but Reason (R) is true.", "சரி. கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி.",
        "Presence under Art 177 does NOT make him a member for quorum or voting.",
        "உறுப்பு 177-ன் கீழான இருப்பு அவரை கோரத்திற்கோ அல்லது வாக்கெடுப்பிற்கோ ஓர் உறுப்பினராக மாற்றாது.",
        "Quorum is 10 members or one-tenth of total membership under Art 189(3).",
        "உறுப்பு 189(3)-ன் கீழ் கோரம் என்பது 10 உறுப்பினர்கள் அல்லது பத்தில் ஒரு பங்கு ஆகும்."
    )

    add_ar(
        "ADVG_R_023", "Ordinance Promulgation Power False",
        "The Advocate General of a State has the constitutional power to promulgate ordinances under Article 213 when the Assembly is in recess.",
        "சட்டமன்றம் கூடாத போது உறுப்பு 213-ன் கீழ் அவசரச் சட்டங்களை பிறப்பிக்கும் அரசியலமைப்பு அதிகாரம் தலைமை வழக்கறிஞருக்கு உண்டு.",
        "Under Article 165(2), it is the duty of the Advocate General to advise the State Government upon legal matters referred to him by the Governor.",
        "உறுப்பு 165(2)-ன் கீழ், ஆளுநரால் தன்னிடம் அனுப்பப்படும் சட்ட விவகாரங்களில் மாநில அரசுக்கு ஆலோசனை வழங்குவது தலைமை வழக்கறிஞரின் கடமையாகும்.",
        "D",
        "Assertion (A) is false because ordinance-making power under Article 213 is an executive power vested exclusively in the Governor. Reason (R) is true as it accurately reproduces Article 165(2).",
        "கூற்று (A) தவறு, ஏனெனில் உறுப்பு 213-ன் கீழான அவசரச் சட்ட அதிகாரம் ஆளுநருக்கு மட்டுமே வழங்கப்பட்ட நிர்வாக அதிகாரமாகும். காரணம் (R) சரி, ஏனெனில் அது உறுப்பு 165(2)-ஐ துல்லியமாக விவரிக்கிறது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Correct. Assertion (A) is false, but Reason (R) is true.", "சரி. கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி.",
        "Ordinance promulgation is an exclusive power of the Governor under Art 213.",
        "அவசரச் சட்டம் பிறப்பிப்பது உறுப்பு 213-ன் கீழ் ஆளுநரின் பிரத்தியேக அதிகாரமாகும்.",
        "The AG merely advises on the constitutionality of draft ordinances.",
        "வரைவு அவசரச் சட்டங்களின் அரசியலமைப்பு செல்லுபடி தன்மை குறித்து AG ஆலோசனை மட்டுமே கூறுகிறார்."
    )

    add_ar(
        "ADVG_R_024", "Private Retainer Against PCB False",
        "The Advocate General can accept a private professional brief to challenge an environmental regulation framed by the State Pollution Control Board.",
        "மாநில மாசுக்கட்டுப்பாட்டு வாரியம் உருவாக்கிய சுற்றுச்சூழல் ஒழுங்குமுறையை எதிர்த்து வழக்காட தலைமை வழக்கறிஞர் ஒரு தனியார் வழக்கை ஏற்க முடியும்.",
        "Under the standards of professional conduct, an advocate is prohibited from appearing in any matter where he has a direct conflict of interest with his client (the State).",
        "தொழில்முறை நடத்தை விதிகளின் கீழ், தனது வாடிக்கையாளரோடு (அரசு) நேரடி நலன் முரண்பாடு உள்ள எந்தவொரு விவகாரத்திலும் ஒரு வழக்கறிஞர் ஆஜராவது தடை செய்யப்பட்டுள்ளது.",
        "D",
        "Assertion (A) is false because the Advocate General cannot advise or hold briefs against any department, board, or statutory corporation of the State Government. Reason (R) is true under Bar Council Rules and state law officers rules.",
        "கூற்று (A) தவறு, ஏனெனில் மாநில அரசின் எந்தவொரு துறை, வாரியம் அல்லது சட்டப்பூர்வ நிறுவனத்திற்கு எதிராக தலைமை வழக்கறிஞர் ஆலோசிக்கவோ வழக்காடவோ முடியாது. காரணம் (R) சரி (பார் கவுன்சில் விதிகள்).",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Correct. Assertion (A) is false, but Reason (R) is true.", "சரி. கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி.",
        "No briefs against the State: Covers government departments, boards, and public corporations.",
        "அரசுக்கு எதிராக வாதாடத் தடை: அரசுத் துறைகள், வாரியங்கள் மற்றும் பொது நிறுவனங்களை உள்ளடக்கியது.",
        "Ethical rules require complete avoidance of conflicts of interest.",
        "நெறிமுறை விதிகள் நலன் முரண்பாடுகளை முற்றிலும் தவிர்ப்பதைக் கோருகின்றன."
    )

    add_ar(
        "ADVG_R_025", "Union Territory AG False",
        "The Constitution of India provides for an Advocate General under Article 165 for every Union Territory having a Legislative Assembly.",
        "சட்டமன்றம் கொண்ட ஒவ்வொரு ஒன்றிய பிரதேசத்திற்கும் உறுப்பு 165-ன் கீழ் தலைமை வழக்கறிஞர் பதவியை இந்திய அரசியலமைப்பு வழங்குகிறது.",
        "Part VI of the Constitution, which contains Article 165, applies strictly to the States and does not govern Union Territories.",
        "உறுப்பு 165-ஐ உள்ளடக்கிய அரசியலமைப்பின் பகுதி VI மாநிலங்களுக்கு மட்டுமே கண்டிப்பாகப் பொருந்தும், ஒன்றிய பிரதேசங்களை நிர்வகிக்காது.",
        "D",
        "Assertion (A) is false because Article 165 applies strictly to States; UTs are governed by Part VIII and do not have an Advocate General under Article 165. Reason (R) is true as Part VI is titled 'The States' and excludes Union Territories.",
        "கூற்று (A) தவறு, ஏனெனில் உறுப்பு 165 மாநிலங்களுக்கு மட்டுமே பொருந்தும்; ஒன்றிய பிரதேசங்கள் பகுதி VIII-ஆல் நிர்வகிக்கப்படுகின்றன மற்றும் உறுப்பு 165 அட்வகேட் ஜெனரலைக் கொண்டிருக்கவில்லை. காரணம் (R) சரி, ஏனெனில் பகுதி VI 'மாநிலங்கள்' என்ற தலைப்பைக் கொண்டு யூனியன் பிரதேசங்களை விலக்கியுள்ளது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Incorrect. Assertion (A) is false.", "தவறு. கூற்று (A) தவறானது.",
        "Correct. Assertion (A) is false, but Reason (R) is true.", "சரி. கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி.",
        "UTs (Part VIII) have Standing Counsel / Government Counsel, not constitutional Advocate Generals.",
        "ஒன்றிய பிரதேசங்கள் (பகுதி VIII) அரசு வழக்கறிஞர்களைக் கொண்டுள்ளனவே தவிர, அரசியலமைப்பு அட்வகேட் ஜெனரலை அல்ல.",
        "Article 165 is strictly confined to Part VI (The States).",
        "உறுப்பு 165 பகுதி VI-க்கு (மாநிலங்கள்) மட்டுமே கண்டிப்பாக வரையறுக்கப்பட்டுள்ளது."
    )

    return qs

def main():
    questions = get_reasoning_questions()
    print(f"Total Reasoning questions generated: {len(questions)}")
    
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "advocate_general_reasoning.json")
    alias_file = os.path.join(out_dir, "advocate_general_assertion_reason.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")
    
    shutil.copyfile(out_file, alias_file)
    print(f"Created alias copy at {alias_file}")
    
    # Validate file
    validator = ContentValidator()
    report = validator.validate_file(out_file, expected_count=25, expected_prefix="ADVG_R_")
    print(f"Validation Result: {'PASS' if report.is_valid else 'FAIL'} | Audited: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
    if not report.is_valid:
        for iss in report.issues:
            print("Issue:", iss.severity, iss.field, iss.message)

if __name__ == "__main__":
    main()
