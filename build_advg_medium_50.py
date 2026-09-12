# -*- coding: utf-8 -*-
"""
Builder for Advocate General of a State - Medium Level (50 MCQs: ADVG_M_001 to ADVG_M_050).
Strict 24-field schema, fully bilingual, high-yield TNPSC standards.
Target Key Distribution: ~12-13 each of A, B, C, D.
"""
import json
import os
from advg_mcq_helper import make_advg_q
from tools.nova_content_engine.validator import ContentValidator

def get_medium_questions():
    qs = []
    
    def add_q(qid, subtopic, en_stem, ta_stem,
              en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
              correct_key, exp_en, exp_ta,
              why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
              tip_en, tip_ta, fact_en, fact_ta):
        qs.append(make_advg_q(
            qid=qid, diff="Medium", qtype="Single Choice", subtopic=subtopic,
            en_stem=en_stem, ta_stem=ta_stem,
            en_a=en_a, ta_a=ta_a, en_b=en_b, ta_b=ta_b, en_c=en_c, ta_c=ta_c, en_d=en_d, ta_d=ta_d,
            correct_key=correct_key, exp_en=exp_en, exp_ta=exp_ta,
            why_a_en=why_a_en, why_a_ta=why_a_ta, why_b_en=why_b_en, why_b_ta=why_b_ta,
            why_c_en=why_c_en, why_c_ta=why_c_ta, why_d_en=why_d_en, why_d_ta=why_d_ta,
            tip_en=tip_en, tip_ta=tip_ta, fact_en=fact_en, fact_ta=fact_ta
        ))

    # --- 1 to 10 ---
    # Q1 (A)
    add_q(
        "ADVG_M_001", "Third Schedule Trap",
        "Which of the following constitutional functionaries does NOT have a prescribed form of oath or affirmation listed in the Third Schedule of the Constitution of India?",
        "பின்வரும் அரசியலமைப்பு பொறுப்பாளர்களில் யாருக்கு இந்திய அரசியலமைப்பின் மூன்றாவது அட்டவணையில் பதவிப் பிரமாணப் படிவம் பட்டியலிடப்படவில்லை?",
        "Advocate General of a State", "மாநில தலைமை வழக்கறிஞர்",
        "Judges of the High Court", "உயர் நீதிமன்ற நீதிபதிகள்",
        "Ministers for a State", "மாநில அமைச்சர்கள்",
        "Comptroller and Auditor-General of India", "இந்திய தலைமை கணக்குத் தணிக்கையாளர் (CAG)",
        "A",
        "The Third Schedule of the Constitution prescribes oaths for Union Ministers, MPs, SC Judges, CAG, State Ministers, MLAs, and HC Judges. Neither the Attorney General nor the Advocate General has an oath prescribed in the Third Schedule.",
        "அரசியலமைப்பின் மூன்றாவது அட்டவணை ஒன்றிய அமைச்சர்கள், நாடாளுமன்ற உறுப்பினர்கள், உச்ச நீதிமன்ற நீதிபதிகள், சிஏஜி, மாநில அமைச்சர்கள், சட்டமன்ற உறுப்பினர்கள் மற்றும் உயர் நீதிமன்ற நீதிபதிகளுக்கு மட்டுமே உறுதிமொழி படிவங்களை வழங்குகிறது. அட்டர்னி ஜெனரல் மற்றும் அட்வகேட் ஜெனரல் இருவருக்குமே மூன்றாவது அட்டவணையில் உறுதிமொழி படிவம் இல்லை.",
        "Correct. Neither the Advocate General nor the Attorney General is listed in the Third Schedule.", "சரி. அட்வகேட் ஜெனரல் மற்றும் அட்டர்னி ஜெனரல் இருவருமே மூன்றாவது அட்டவணையில் பட்டியலிடப்படவில்லை.",
        "Incorrect. High Court Judges take oath under Form VIII of the Third Schedule.", "தவறு. உயர் நீதிமன்ற நீதிபதிகள் மூன்றாவது அட்டவணையின் படிவம் VIII-ன் கீழ் உறுதிமொழி ஏற்கின்றனர்.",
        "Incorrect. State Ministers take oath under Form V and Form VI of the Third Schedule.", "தவறு. மாநில அமைச்சர்கள் மூன்றாவது அட்டவணையின் படிவம் V மற்றும் VI-ன் கீழ் உறுதிமொழி ஏற்கின்றனர்.",
        "Incorrect. The CAG takes oath under Form IV of the Third Schedule.", "தவறு. சிஏஜி மூன்றாவது அட்டவணையின் படிவம் IV-ன் கீழ் உறுதிமொழி ஏற்கிறார்.",
        "Major Trap: Third Schedule lists oaths for 8 constitutional offices; Law Officers (AG & Advocate General) are NOT among them.",
        "முக்கிய பொறி: மூன்றாவது அட்டவணை 8 பதவிகளுக்கான உறுதிமொழிகளை பட்டியலிடுகிறது; சட்ட அதிகாரிகள் (AG & அட்வகேட் ஜெனரல்) அதில் இல்லை.",
        "The Advocate General takes an administrative oath of allegiance upon assumption of office as regulated by executive notifications.",
        "தலைமை வழக்கறிஞர் நிர்வாக அறிவிப்புகளால் ஒழுங்குபடுத்தப்படும் விசுவாசப் பிரமாணத்தை பதவியேற்பின் போது ஏற்கிறார்."
    )

    # Q2 (B)
    add_q(
        "ADVG_M_002", "Union Territory Law Officers",
        "Does the Constitution of India provide for an Advocate General under Article 165 for Union Territories with a Legislative Assembly (e.g., Puducherry or NCT of Delhi)?",
        "சட்டமன்றம் கொண்ட ஒன்றிய பிரதேசங்களுக்கு (எ.கா. புதுச்சேரி அல்லது தில்லி) உறுப்பு 165-ன் கீழ் தலைமை வழக்கறிஞர் பதவியை இந்திய அரசியலமைப்பு வழங்குகிறதா?",
        "Yes, under Article 165 read with Article 239A", "ஆம், உறுப்பு 239A-உடன் இணைந்த உறுப்பு 165-ன் கீழ்",
        "No, Article 165 applies strictly to 'States' in Part VI; UTs are governed by Government of Union Territories Act / GNCTD Act and have Government Counsel, not a constitutional AG", "இல்லை, உறுப்பு 165 பகுதி VI-ல் உள்ள 'மாநிலங்களுக்கு' மட்டுமே பொருந்தும்; ஒன்றிய பிரதேசங்கள் சட்டப்பூர்வ அரசு வழக்கறிஞர்களைக் கொண்டுள்ளனவே தவிர அரசியலமைப்பு அட்வகேட் ஜெனரலை அல்ல",
        "Yes, appointed directly by the President of India", "ஆம், இந்தியக் குடியரசுத் தலைவரால் நேரடியாக நியமிக்கப்படுகிறார்",
        "Yes, but with tenure limited strictly to 1 year", "ஆம், ஆனால் பதவிக்காலம் கண்டிப்பாக 1 ஆண்டுக்கு மட்டுமே",
        "B",
        "Part VI of the Constitution, which contains Article 165, applies only to the States. Union Territories are governed under Part VIII (Articles 239 to 241). The Government of UTs Act, 1963 and GNCTD Act do not create an office of Advocate General under Article 165; they appoint Standing Counsel / Additional Standing Counsel.",
        "அரசியலமைப்பின் பகுதி VI (உறுப்பு 165 உள்ளடக்கியது) மாநிலங்களுக்கு மட்டுமே பொருந்தும். ஒன்றிய பிரதேசங்கள் பகுதி VIII-ன் கீழ் (உறுப்புகள் 239-241) நிர்வகிக்கப்படுகின்றன. யூனியன் பிரதேசங்கள் சட்டம் 1963 மற்றும் GNCTD சட்டம் உறுப்பு 165-ன் கீழ் அட்வகேட் ஜெனரல் பதவியை உருவாக்கவில்லை; அவை அரசு வழக்கறிஞர்களையே (Standing Counsel) நியமிக்கின்றன.",
        "Incorrect. Article 239A enables creation of legislatures in UTs, but does not extend Article 165.", "தவறு. உறுப்பு 239A சட்டமன்றங்களை உருவாக்க அனுமதிக்கிறது, ஆனால் உறுப்பு 165-ஐ நீட்டிக்கவில்லை.",
        "Correct. Article 165 applies strictly to States; UTs do not have a constitutional Advocate General under Article 165.", "சரி. உறுப்பு 165 மாநிலங்களுக்கு மட்டுமே பொருந்தும்; யூனியன் பிரதேசங்களுக்கு உறுப்பு 165-ன் கீழ் அரசியலமைப்பு அட்வகேட் ஜெனரல் இல்லை.",
        "Incorrect. The President appoints law officers for Union Government, not State AGs under 165 for UTs.", "தவறு. குடியரசுத் தலைவர் ஒன்றிய அரசுக்கு சட்ட அதிகாரிகளை நியமிக்கிறார், UT-களுக்கு அட்வகேட் ஜெனரலை அல்ல.",
        "Incorrect. There is no 1-year constitutional AG post in UTs.", "தவறு. யூனியன் பிரதேசங்களில் 1 ஆண்டு கால அரசியலமைப்பு அட்வகேட் ஜெனரல் பதவி எதுவும் இல்லை.",
        "Constitutional nuance: Part VI is titled 'The States'. Article 165 explicitly says 'Advocate-General for the State'.",
        "அரசியலமைப்பு நுணுக்கம்: பகுதி VI 'மாநிலங்கள்' என்ற தலைப்பைக் கொண்டது. உறுப்பு 165 தெளிவாக 'மாநிலத்திற்கான தலைமை வழக்கறிஞர்' என்றே கூறுகிறது.",
        "Legal representation for Delhi and Puducherry is handled by Standing Counsel and nominated Senior Advocates.",
        "தில்லி மற்றும் புதுச்சேரிக்கான சட்டப் பிரதிநிதித்துவம் அரசு வழக்கறிஞர்கள் மற்றும் நியமிக்கப்பட்ட மூத்த வழக்கறிஞர்களால் கையாளப்படுகிறது."
    )

    # Q3 (C)
    add_q(
        "ADVG_M_003", "Joint Sitting Trap",
        "Can the Advocate General of a State address a 'Joint Sitting' of the State Legislative Assembly and State Legislative Council?",
        "மாநில சட்டப் பேரவை மற்றும் சட்ட மேலவையின் 'கூட்டுக் கூட்டத்தில்' (Joint Sitting) மாநில தலைமை வழக்கறிஞர் உரையாற்ற முடியுமா?",
        "Yes, whenever a deadlock occurs over ordinary legislation", "ஆம், சாதாரண சட்ட மசோதாவில் முட்டுக்கட்டை ஏற்படும் போதெல்லாம் முடியும்",
        "Yes, with the prior written permission of the Governor", "ஆம், ஆளுநரின் முன் எழுத்துப்பூர்வ அனுமதியுடன் முடியும்",
        "There is no provision for a Joint Sitting of the two Houses of a State Legislature in the Constitution of India", "இந்திய அரசியலமைப்பில் மாநில சட்டமன்றத்தின் இரு அவைகளின் கூட்டுக் கூட்டத்திற்கு (Joint Sitting) எந்த விதியும் இல்லை",
        "Yes, but he must cast a vote if the Houses are equally divided", "ஆம், ஆனால் அவைகள் சமமாகப் பிரிந்தால் அவர் வாக்களிக்க வேண்டும்",
        "C",
        "Unlike Parliament (Article 108), the Indian Constitution provides NO mechanism for a joint sitting of both Houses of a State Legislature to resolve a legislative deadlock. Under Article 197, the Legislative Assembly has ultimate supremacy over the Legislative Council. Therefore, the question of addressing a joint sitting does not arise.",
        "நாடாளுமன்றத்தைப் போலன்றி (உறுப்பு 108), மசோதா முட்டுக்கட்டையைத் தீர்க்க மாநில சட்டமன்றத்தின் இரு அவைகளின் கூட்டுக் கூட்டத்திற்கு இந்திய அரசியலமைப்பில் எந்த வழியும் இல்லை. உறுப்பு 197-ன் கீழ் சட்டமன்றப் பேரவைக்கே மேலவையை விட இறுதி மேலாதிக்கம் உண்டு. எனவே கூட்டுக் கூட்டத்தில் உரையாற்றும் கேள்விக்கே இடமில்லை.",
        "Incorrect. Joint sitting does not exist in State Legislatures under the Indian Constitution.", "தவறு. இந்திய அரசியலமைப்பில் மாநில சட்டமன்றங்களில் கூட்டுக் கூட்டம் என்ற நடைமுறை இல்லை.",
        "Incorrect. Governor cannot convene a joint sitting not provided for by the Constitution.", "தவறு. அரசியலமைப்பில் இல்லாத கூட்டுக் கூட்டத்தை ஆளுநரால் கூட்ட முடியாது.",
        "Correct. The Constitution of India does NOT provide for a joint sitting of the two Houses of a State Legislature.", "சரி. இந்திய அரசியலமைப்பு மாநில சட்டமன்றத்தின் இரு அவைகளின் கூட்டுக் கூட்டத்திற்கு வழிவகை செய்யவில்லை.",
        "Incorrect. Advocate General cannot vote under any circumstances under Article 177.", "தவறு. உறுப்பு 177-ன் கீழ் தலைமை வழக்கறிஞர் எந்த சூழலிலும் வாக்களிக்க முடியாது.",
        "Classic Polity Trap: Parliament has Joint Sittings (Art 108); State Legislature NEVER has Joint Sittings (Art 197 prevails).",
        "முக்கிய பாலிட்டி பொறி: நாடாளுமன்றத்தில் கூட்டுக் கூட்டம் உண்டு (உறுப்பு 108); மாநில சட்டமன்றத்தில் ஒருபோதும் கூட்டுக் கூட்டம் கிடையாது (உறுப்பு 197 பொருந்தும்).",
        "The Advocate General addresses each House separately under Article 177.",
        "தலைமை வழக்கறிஞர் உறுப்பு 177-ன் கீழ் ஒவ்வொரு அவையிலும் தனித்தனியாகவே உரையாற்றுகிறார்."
    )

    # Q4 (D)
    add_q(
        "ADVG_M_004", "Contempt Consent Quasi-Judicial Nature",
        "In P.N. Duda v. P. Shiv Shanker (1988), what did the Supreme Court observe regarding the nature of power exercised by the Advocate General when granting or refusing consent for criminal contempt under Section 15 of the Contempt of Courts Act?",
        "பி.என். துதா எதிர் பி. சிவ் சங்கர் (1988) வழக்கில், நீதிமன்ற அவமதிப்புச் சட்டம் பிரிவு 15-ன் கீழ் குற்றவியல் அவமதிப்புக்கு இசைவு வழங்கும் போது அல்லது மறுக்கும் போது தலைமை வழக்கறிஞர் பயன்படுத்தும் அதிகாரத்தின் தன்மை குறித்து உச்ச நீதிமன்றம் என்ன கூறியது?",
        "It is a purely political power exercised on cabinet directions", "இது அமைச்சரவையின் வழிகாட்டுதலின் பேரில் பயன்படுத்தப்படும் முற்றிலும் அரசியல் அதிகாரம்",
        "It is an administrative act not open to any legal standards", "இது எந்தவொரு சட்டத் தரங்களுக்கும் உட்படாத ஒரு நிர்வாக நடவடிக்கை",
        "It is an executive prerogative that cannot be questioned in court", "இது நீதிமன்றத்தில் கேள்வி கேட்க முடியாத ஒரு நிர்வாக தனியுரிமை",
        "It is a quasi-judicial function where the Advocate General acts independently without executive interference", "இது ஒரு நீதித்துறை போன்ற (Quasi-judicial) பணியாகும், இதில் தலைமை வழக்கறிஞர் நிர்வாக தலையீடின்றி சுதந்திரமாக செயல்படுகிறார்",
        "D",
        "In P.N. Duda v. P. Shiv Shanker (1988), the Supreme Court held that the grant or refusal of consent under Section 15 of the Contempt of Courts Act is a quasi-judicial function. The Advocate General must exercise this statutory power independently and objectively, free from executive influence.",
        "பி.என். துதா எதிர் பி. சிவ் சங்கர் (1988) வழக்கில், பிரிவு 15-ன் கீழ் இசைவு வழங்குவது அல்லது மறுப்பது ஒரு நீதித்துறை போன்ற (Quasi-judicial) பணியாகும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. தலைமை வழக்கறிஞர் இந்த சட்டப்பூர்வ அதிகாரத்தை நிர்வாக தலையீடின்றி சுதந்திரமாகவும் புறநிலையாகவும் பயன்படுத்த வேண்டும்.",
        "Incorrect. The power is statutory and quasi-judicial, not subject to cabinet direction.", "தவறு. இந்த அதிகாரம் சட்டப்பூர்வமானது மற்றும் நீதித்துறை போன்றது, அமைச்சரவை வழிகாட்டுதலுக்கு உட்பட்டதல்ல.",
        "Incorrect. Must adhere to legal principles of natural justice and fairness.", "தவறு. இயற்கை நீதி மற்றும் நியாயத்தின் சட்டக் கோட்பாடுகளுக்கு கட்டுப்பட வேண்டும்.",
        "Incorrect. Not an unreviewable executive prerogative.", "தவறு. மறுபரிசீலனை செய்ய முடியாத நிர்வாக தனியுரிமை அல்ல.",
        "Correct. It is a quasi-judicial function exercised independently by the Advocate General.", "சரி. இது தலைமை வழக்கறிஞரால் சுதந்திரமாகப் பயன்படுத்தப்படும் ஒரு நீதித்துறை போன்ற பணியாகும்.",
        "Consent under Section 15 is required to filter out vexatious petitions and protect the dignity of the judiciary.",
        "வீண் மனுக்களை வடிகட்டவும் நீதித்துறையின் கண்ணியத்தைப் பாதுகாக்கவும் பிரிவு 15-ன் கீழ் இசைவு அவசியமாகிறது.",
        "If the Advocate General refuses consent arbitrarily, a petitioner may bring the facts directly to the High Court's suo motu notice.",
        "தலைமை வழக்கறிஞர் தன்னிச்சையாக இசைவு மறுத்தால், மனுதாரர் உண்மைகளை நேரடியாக உயர் நீதிமன்றத்தின் தானாக முன்வந்து விசாரிக்கும் (Suo motu) கவனத்திற்கு கொண்டு செல்லலாம்."
    )

    # Q5 (A)
    add_q(
        "ADVG_M_005", "Article 217(2) Judicial Office Interpretation",
        "Under Article 217(2)(a), what constitutes 'holding a judicial office in the territory of India' for the purpose of qualification as an Advocate General?",
        "உறுப்பு 217(2)(a)-ன் கீழ், தலைமை வழக்கறிஞருக்கான தகுதியின் நோக்கில் 'இந்திய எல்லைக்குள் நீதித்துறை பதவியை வகித்தல்' என்பது எதைக் குறிக்கிறது?",
        "Holding an office in the subordinate judiciary (such as District Judge, Subordinate Judge, or Magistrate) forming part of the regular judicial service", "வழக்கமான நீதித்துறை பணியின் ஒரு பகுதியாக உள்ள கீழ்மை நீதித்துறை பதவிகளை (மாவட்ட நீதிபதி, சார்பு நீதிபதி அல்லது நடுவர் போன்ற) வகித்தல்",
        "Holding any ministerial legal advisor post in a government department", "அரசுத் துறையில் ஏதேனும் சட்ட ஆலோசகர் பதவியை வகித்தல்",
        "Serving as a police officer with magisterial powers", "நடுவர் அதிகாரங்களுடன் கூடிய காவல் துறை அதிகாரியாகப் பணியாற்றுதல்",
        "Working as a legal officer in an insurance corporation", "காப்பீட்டு நிறுவனத்தில் சட்ட அதிகாரியாகப் பணியாற்றுதல்",
        "A",
        "The Supreme Court has clarified that 'judicial office' in Article 217(2)(a) means an office within the judicial hierarchy of the State exercising civil or criminal judicial powers, forming part of the judicial service under Chapter VI of Part VI.",
        "உறுப்பு 217(2)(a)-ல் உள்ள 'நீதித்துறை பதவி' என்பது பகுதி VI-ன் அத்தியாயம் VI-ன் கீழ் உள்ள நீதித்துறை பணியின் ஒரு பகுதியாக சிவில் அல்லது குற்றவியல் அதிகாரங்களைப் பயன்படுத்தும் மாநில நீதித்துறை படிநிலைக்குள் உள்ள பதவியைக் குறிக்கிறது என்று உச்ச நீதிமன்றம் தெளிவுபடுத்தியுள்ளது.",
        "Correct. Judicial office means holding an office in the organized subordinate judiciary / judicial service.", "சரி. நீதித்துறை பதவி என்பது ஒழுங்கமைக்கப்பட்ட கீழ்மை நீதித்துறை / நீதிப் பணியில் உள்ள பதவியை வகிப்பதைக் குறிக்கும்.",
        "Incorrect. Purely administrative legal advisor posts do not count as judicial office.", "தவறு. முற்றிலும் நிர்வாக சட்ட ஆலோசகர் பதவிகள் நீதித்துறை பதவியாக கணக்கிடப்படாது.",
        "Incorrect. Police officer posts do not qualify as judicial office under Art 217(2).", "தவறு. காவல் துறை அதிகாரி பதவிகள் உறுப்பு 217(2)-ன் கீழ் நீதித்துறை பதவியாக தகுதி பெறாது.",
        "Incorrect. Corporate legal officers do not hold a constitutional judicial office.", "தவறு. கார்ப்பரேட் சட்ட அதிகாரிகள் அரசியலமைப்பு நீதித்துறை பதவியை வகிப்பவர்கள் அல்ல.",
        "Judicial office entails discharging judicial functions within the State's judicial branch.",
        "நீதித்துறை பதவி என்பது மாநிலத்தின் நீதித்துறையின் கீழ் நீதித்துறை பணிகளை ஆற்றுவதைக் குறிக்கிறது.",
        "In computing the 10-year period, any period during which a person has been an advocate is also added if subsequently he held judicial office.",
        "10 ஆண்டு காலத்தைக் கணக்கிடுவதில், ஒருவர் வழக்கறிஞராக இருந்த காலமும், பின்னர் நீதித்துறை பதவியை வகித்திருந்தால் அதனுடன் சேர்க்கப்படும்."
    )

    # Q6 (B)
    add_q(
        "ADVG_M_006", "Right of Pre-audience Ranking",
        "According to Section 23 of the Advocates Act, 1961, what is the precise order of pre-audience among the following law officers?",
        "வழக்கறிஞர்கள் சட்டம் 1961-ன் பிரிவு 23-ன் படி, பின்வரும் சட்ட அதிகாரிகளுக்கு இடையேயான துல்லியமான முன்னுரிமை வரிசை என்ன?",
        "1. Advocate General -> 2. Attorney General -> 3. Solicitor General", "1. அட்வகேட் ஜெனரல் -> 2. அட்டர்னி ஜெனரல் -> 3. சொலிசிட்டர் ஜெனரல்",
        "1. Attorney General -> 2. Solicitor General -> 3. Additional Solicitor General -> 4. Advocate General of a State", "1. அட்டர்னி ஜெனரல் -> 2. சொலிசிட்டர் ஜெனரல் -> 3. கூடுதல் சொலிசிட்டர் ஜெனரல் -> 4. மாநில அட்வகேட் ஜெனரல்",
        "1. Chief Justice -> 2. Advocate General -> 3. Attorney General", "1. தலைமை நீதிபதி -> 2. அட்வகேட் ஜெனரல் -> 3. அட்டர்னி ஜெனரல்",
        "1. Advocate General -> 2. Additional Advocate General -> 3. Public Prosecutor", "1. அட்வகேட் ஜெனரல் -> 2. கூடுதல் அட்வகேட் ஜெனரல் -> 3. அரசு வழக்கறிஞர்",
        "B",
        "Section 23 of the Advocates Act, 1961 lays down the order of pre-audience: (1) Attorney General of India, (2) Solicitor General of India, (3) Additional Solicitor General of India, (4) Advocate General of any State. Within the High Court of a State, the Advocate General has pre-audience over all advocates except the Attorney General and Solicitor General.",
        "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 23 முன்னுரிமை வரிசையை வகுக்கிறது: (1) இந்திய அட்டர்னி ஜெனரல், (2) இந்திய சொலிசிட்டர் ஜெனரல், (3) இந்திய கூடுதல் சொலிசிட்டர் ஜெனரல், (4) மாநில அட்வகேட் ஜெனரல். உயர் நீதிமன்றத்தில், அட்டர்னி ஜெனரல் மற்றும் சொலிசிட்டர் ஜெனரலைத் தவிர மற்ற அனைத்து வழக்கறிஞர்களுக்கும் மேலாக அட்வகேட் ஜெனரல் முன்னுரிமை பெறுகிறார்.",
        "Incorrect. Advocate General does not rank above Attorney General or Solicitor General.", "தவறு. அட்வகேட் ஜெனரல் அட்டர்னி ஜெனரல் அல்லது சொலிசிட்டர் ஜெனரலை விட உயர்ந்த இடத்தில் இல்லை.",
        "Correct. The exact statutory hierarchy is Attorney General, Solicitor General, Additional Solicitor General, followed by Advocate General.", "சரி. துல்லியமான சட்டப்பூர்வ படிநிலை: அட்டர்னி ஜெனரல், சொலிசிட்டர் ஜெனரல், கூடுதல் சொலிசிட்டர் ஜெனரல், பின்னர் மாநில அட்வகேட் ஜெனரல்.",
        "Incorrect. Chief Justice is a judge, not an advocate in the bar cause list.", "தவறு. தலைமை நீதிபதி ஒரு நீதிபதி, வழக்குப் பட்டியலில் உள்ள வழக்கறிஞர் அல்ல.",
        "Incorrect. Option D shows state officers but misses the all-India statutory precedence under Section 23.", "தவறு. விருப்பம் D மாநில அதிகாரிகளைக் காட்டுகிறது, ஆனால் பிரிவு 23-ன் அகில இந்திய முன்னுரிமையை விடுத்துள்ளது.",
        "Advocate General is 4th in all-India hierarchy, but 1st among state advocates in the High Court.",
        "அகில இந்திய படிநிலையில் அட்வகேட் ஜெனரல் 4-வது இடத்தில் உள்ளார், ஆனால் உயர் நீதிமன்றத்தில் மாநில வழக்கறிஞர்களில் முதலிடம் வகிக்கிறார்.",
        "This ranking determines whose cases are called first when multiple senior law officers appear before the court.",
        "பல மூத்த சட்ட அதிகாரிகள் நீதிமன்றத்தின் முன் தோன்றும் போது யாருடைய வழக்குகள் முதலில் அழைக்கப்பட வேண்டும் என்பதை இந்த தரவரிசை தீர்மானிக்கிறது."
    )

    # Q7 (C)
    add_q(
        "ADVG_M_007", "Fiduciary Character of Law Office",
        "In State of Uttar Pradesh v. U.P. State Law Officers Association (1994), what fundamental character of government law officers was underscored by the Supreme Court?",
        "உத்தரப் பிரதேச அரசு எதிர் உ.பி. மாநில சட்ட அதிகாரிகள் சங்கம் (1994) வழக்கில், அரசு சட்ட அதிகாரிகளின் எந்த அடிப்படைக் குணாதிசயத்தை உச்ச நீதிமன்றம் அடிக்கோடிட்டுக் காட்டியது?",
        "They are permanent employees entitled to pension and gratuity", "அவர்கள் ஓய்வூதியம் மற்றும் பணிக்கொடைக்கு தகுதியுடைய நிரந்தர ஊழியர்கள்",
        "They can be appointed solely based on political patronage without regard to competence", "திறமையைக் கவனத்தில் கொள்ளாமல் அரசியல் ஆதரவின் அடிப்படையில் மட்டுமே அவர்களை நியமிக்க முடியும்",
        "Their office is a public office held in a fiduciary capacity for public good, requiring professional competence and integrity", "அவர்களின் அலுவலகம் பொது நலனுக்காக நம்பிக்கைப் பொறுப்பில் (Fiduciary capacity) வகிக்கப்படும் ஒரு பொது அலுவலகமாகும், அதற்கு தொழில்முறைத் திறனும் நாணயமும் தேவை",
        "They have trade union rights to strike against the government", "அரசுக்கு எதிராக வேலைநிறுத்தம் செய்ய அவர்களுக்கு தொழிற்சங்க உரிமைகள் உண்டு",
        "C",
        "The Supreme Court held that the office of the Advocate General and government law officers is a 'public office' held in trust for the public. Appointment must be based on merit and professional competence rather than arbitrary political patronage.",
        "தலைமை வழக்கறிஞர் மற்றும் அரசு சட்ட அதிகாரிகளின் பதவி என்பது பொதுமக்களுக்கான நம்பிக்கைப் பொறுப்பில் (Fiduciary capacity) வகிக்கப்படும் ஒரு 'பொது அலுவலகம்' என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. நியமனம் தன்னிச்சையான அரசியல் ஆதரவை விட தகுதி மற்றும் தொழில்முறை திறனின் அடிப்படையிலேயே இருக்க வேண்டும்.",
        "Incorrect. They are not permanent pensionable employees.", "தவறு. அவர்கள் நிரந்தர ஓய்வூதிய ஊழியர்கள் அல்ல.",
        "Incorrect. Arbitrary patronage without merit was specifically condemned by the court.", "தவறு. தகுதியற்ற தன்னிச்சையான அரசியல் ஆதரவை நீதிமன்றம் வெளிப்படையாகக் கண்டித்தது.",
        "Correct. The office is held in a fiduciary capacity for public good requiring high competence.", "சரி. இப்பொறுப்பு பொது நலனுக்காக நம்பிக்கைப் பொறுப்பில் வகிக்கப்படும் உயர் தகுதி தேவைப்படும் பொது அலுவலகமாகும்.",
        "Incorrect. Law officers have no trade union rights or right to strike.", "தவறு. சட்ட அதிகாரிகளுக்கு தொழிற்சங்க உரிமைகளோ அல்லது வேலைநிறுத்த உரிமையோ கிடையாது.",
        "Law officers represent the public interest, not merely the partisan political interest of the ruling party.",
        "சட்ட அதிகாரிகள் ஆளும் கட்சியின் அரசியல் நலனை மட்டுமல்லாது, பரந்த பொது நலனையே பிரதிநிதித்துவப்படுத்துகின்றனர்.",
        "The Advocate General must fearlessly advise the government on the legality and constitutionality of its proposed policies.",
        "அரசு முன்மொழியும் கொள்கைகளின் சட்டப்பூர்வ தன்மை மற்றும் அரசியலமைப்பு செல்லுபடி தன்மை குறித்து தலைமை வழக்கறிஞர் அஞ்சாமல் அரசுக்கு ஆலோசனை வழங்க வேண்டும்."
    )

    # Q8 (D)
    add_q(
        "ADVG_M_008", "Inter-State Water Disputes Tribunal",
        "Before an Inter-State River Water Disputes Tribunal constituted under the 1956 Act, who typically leads the legal arguments on behalf of the State?",
        "1956-ஆம் ஆண்டு சட்டத்தின் கீழ் அமைக்கப்பட்ட மாநிலங்களுக்கு இடையேயான நதிநீர் தாவா தீர்ப்பாயத்தின் முன், பொதுவாக மாநிலத்தின் சார்பில் சட்ட வாதங்களை முன்னின்று நடத்துபவர் யார்?",
        "The Union Law Minister", "ஒன்றிய சட்ட அமைச்சர்",
        "The Central Water Commission Chairman", "மத்திய நீர் ஆணைய தலைவர்",
        "The Chief Secretary of the State", "மாநில தலைமைச் செயலாளர்",
        "The Advocate General of the State assisted by Senior Counsel", "மூத்த வழக்கறிஞர்களின் உதவியுடன் மாநில தலைமை வழக்கறிஞர்",
        "D",
        "In complex inter-state river water disputes (e.g., Cauvery, Krishna, Godavari tribunals), the Advocate General of the State, as the chief constitutional law officer, leads the State's legal team before the Tribunal.",
        "சிக்கலான மாநிலங்களுக்கு இடையேயான நதிநீர் தாவாக்களில் (எ.கா. காவிரி, கிருஷ்ணா, கோதாவரி தீர்ப்பாயங்கள்), மாநில தலைமை வழக்கறிஞரே முதன்மை அரசியலமைப்பு சட்ட அதிகாரியாக தீர்ப்பாயத்தின் முன் மாநில சட்டக் குழுவிற்கு தலைமை தாங்குகிறார்.",
        "Incorrect. Union Law Minister has no standing to represent individual disputing States.", "தவறு. வழக்காடும் தனிப்பட்ட மாநிலங்களைப் பிரதிநிதித்துவப்படுத்த ஒன்றிய சட்ட அமைச்சருக்கு உரிமை இல்லை.",
        "Incorrect. CWC Chairman is a technical expert and witness, not an advocate.", "தவறு. மத்திய நீர் ஆணையத் தலைவர் ஒரு தொழில்நுட்ப நிபுணர் மற்றும் சாட்சி, வழக்கறிஞர் அல்ல.",
        "Incorrect. Chief Secretary provides administrative affidavits, but does not argue legal cases.", "தவறு. தலைமைச் செயலாளர் நிர்வாகப் பிரமாணப் பத்திரங்களை வழங்குகிறார், ஆனால் சட்ட வாதங்களை முன்வைப்பதில்லை.",
        "Correct. The Advocate General leads the State legal team before the Water Disputes Tribunal.", "சரி. நதிநீர் தீர்ப்பாயத்தின் முன் தலைமை வழக்கறிஞரே மாநில சட்டக் குழுவிற்கு தலைமை தாங்குகிறார்.",
        "River water disputes involve critical constitutional questions under Article 262 and Entry 17 of the State List.",
        "நதிநீர் தாவாக்கள் உறுப்பு 262 மற்றும் மாநிலப் பட்டியலின் பதிவு 17-ன் கீழ் முக்கியமான அரசியலமைப்பு வினாக்களை உள்ளடக்கியவை.",
        "The Advocate General coordinates with technical engineers and legal experts to protect the State's riparian rights.",
        "மாநிலத்தின் நதிநீர் உரிமைகளைப் பாதுகாக்க தலைமை வழக்கறிஞர் தொழில்நுட்பப் பொறியாளர்கள் மற்றும் சட்ட வல்லுநர்களுடன் இணைந்து செயல்படுகிறார்."
    )

    # Q9 (A)
    add_q(
        "ADVG_M_009", "Article 163 Aid and Advice",
        "When appointing the Advocate General under Article 165(1), does the Governor act in his personal discretion or on the aid and advice of the Council of Ministers?",
        "உறுப்பு 165(1)-ன் கீழ் தலைமை வழக்கறிஞரை நியமிக்கும் போது, ஆளுநர் தனது தனிப்பட்ட விருப்புரிமையின்படி செயல்படுகிறாரா அல்லது அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின்படி செயல்படுகிறாரா?",
        "On the aid and advice of the Council of Ministers headed by the Chief Minister under Article 163", "உறுப்பு 163-ன் கீழ் முதலமைச்சர் தலைமையிலான அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின்படி",
        "In his unfettered personal discretion under special constitutional powers", "சிறப்பு அரசியலமைப்பு அதிகாரங்களின் கீழ் தனது கட்டுப்பாடற்ற தனிப்பட்ட விருப்புரிமையின்படி",
        "Solely on the binding direction of the High Court Chief Justice", "உயர் நீதிமன்ற தலைமை நீதிபதியின் கட்டுப்படுத்தும் உத்தரவின்படி மட்டுமே",
        "On the recommendation of the Union Home Ministry", "ஒன்றிய உள்துறை அமைச்சகத்தின் பரிந்துரையின்படி",
        "A",
        "Under the parliamentary system established by the Constitution (Article 163), the Governor is a constitutional head and must act on the aid and advice of the Council of Ministers headed by the Chief Minister in appointing the Advocate General.",
        "அரசியலமைப்பால் நிறுவப்பட்ட நாடாளுமன்ற ஆட்சி அமைப்பின் கீழ் (உறுப்பு 163), ஆளுநர் ஓர் அரசியலமைப்புத் தலைவராவார், மேலும் தலைமை வழக்கறிஞரை நியமிப்பதில் முதலமைச்சர் தலைமையிலான அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின்படியே செயல்பட வேண்டும்.",
        "Correct. The Governor acts on the aid and advice of the State Council of Ministers under Article 163.", "சரி. உறுப்பு 163-ன் கீழ் மாநில அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின்படியே ஆளுநர் செயல்படுகிறார்.",
        "Incorrect. Appointment of Advocate General is not a discretionary power of the Governor.", "தவறு. தலைமை வழக்கறிஞர் நியமனம் ஆளுநரின் விருப்புரிமை அதிகாரம் அல்ல.",
        "Incorrect. High Court Chief Justice has no constitutional say in the appointment of the Advocate General.", "தவறு. தலைமை வழக்கறிஞர் நியமனத்தில் உயர் நீதிமன்ற தலைமை நீதிபதிக்கு எந்த அரசியலமைப்புப் பங்கும் இல்லை.",
        "Incorrect. Union Home Ministry has no role in appointing State Advocate Generals.", "தவறு. மாநில தலைமை வழக்கறிஞர்களை நியமிப்பதில் ஒன்றிய உள்துறை அமைச்சகத்திற்கு எந்தப் பங்கும் இல்லை.",
        "Since the AG represents the elected State Government, the Cabinet chooses the counsel in whom it reposes trust.",
        "தலைமை வழக்கறிஞர் தேர்ந்தெடுக்கப்பட்ட மாநில அரசைப் பிரதிநிதித்துவப்படுத்துவதால், அமைச்சரவை தான் நம்பும் வழக்கறிஞரையே தேர்ந்தெடுக்கிறது.",
        "In Samsher Singh v. State of Punjab (1974), the Supreme Court confirmed that the Governor acts on Cabinet advice in all executive functions.",
        "ஷம்ஷேர் சிங் வழக்கில் (1974), ஆளுநர் அனைத்து நிர்வாகப் பணிகளிலும் அமைச்சரவை ஆலோசனையின்படியே செயல்படுகிறார் என்பதை உச்ச நீதிமன்றம் உறுதிப்படுத்தியது."
    )

    # Q10 (B)
    add_q(
        "ADVG_M_010", "Article 194(2) Immunity for Speeches",
        "What constitutional immunity is granted to the Advocate General under Article 194(2) for anything said in the State Legislature?",
        "மாநில சட்டமன்றத்தில் பேசிய எதற்காகவும் உறுப்பு 194(2)-ன் கீழ் தலைமை வழக்கறிஞருக்கு என்ன அரசியலமைப்பு விலக்களிப்பு (Immunity) வழங்கப்படுகிறது?",
        "He can be prosecuted for defamation only with the Governor's sanction", "ஆளுநரின் அனுமதியுடன் மட்டுமே அவர் மீது அவதூறு வழக்குத் தொடர முடியும்",
        "No proceedings can be instituted against him in any court in respect of anything said by him in the Legislature or any committee thereof", "சட்டமன்றத்திலோ அல்லது அதன் எந்தவொரு குழுவிலோ அவர் பேசிய எதற்காகவும் எந்தவொரு நீதிமன்றத்திலும் அவருக்கு எதிராக எந்த நடவடிக்கையும் எடுக்க முடியாது",
        "He is immune only from civil suits, but not from criminal defamation", "அவருக்கு சிவில் வழக்குகளிலிருந்து மட்டுமே விலக்களிப்பு உண்டு, குற்றவியல் அவதூறிலிருந்து அல்ல",
        "He enjoys no immunity; he is subject to ordinary court processes like any other citizen", "அவருக்கு எந்த விலக்களிப்பும் இல்லை; மற்ற குடிமக்களைப் போலவே அவரும் சாதாரண நீதிமன்ற நடைமுறைகளுக்கு உட்பட்டவர்",
        "B",
        "Under Article 194(2) read with Article 194(4), no person entitled to speak in the Legislature (including the Advocate General) shall be liable to any proceedings in any court in respect of anything said or any vote given by him in the Legislature or any committee thereof.",
        "உறுப்பு 194(4)-உடன் இணைந்த உறுப்பு 194(2)-ன் படி, சட்டமன்றத்தில் பேச உரிமை உள்ள எவரும் (தலைமை வழக்கறிஞர் உட்பட) சட்டமன்றத்திலோ அல்லது அதன் குழுவிலோ பேசிய எதற்காகவும் எந்த நீதிமன்றத்திலும் எந்த நடவடிக்கைக்கும் ஆளாக மாட்டார்.",
        "Incorrect. There is absolute immunity; Governor cannot sanction prosecution for legislative speeches.", "தவறு. முழுமையான விலக்களிப்பு உள்ளது; சட்டமன்றப் பேச்சுக்காக ஆளுநர் வழக்குத் தொடர அனுமதி அளிக்க முடியாது.",
        "Correct. Article 194(2) provides absolute immunity from court proceedings for statements made in the Legislature.", "சரி. உறுப்பு 194(2) சட்டமன்றத்தில் பேசிய கருத்துகளுக்காக நீதிமன்ற நடவடிக்கைகளிலிருந்து முழுமையான பாதுகாப்பை வழங்குகிறது.",
        "Incorrect. The immunity covers both civil and criminal proceedings.", "தவறு. இந்த விலக்களிப்பு சிவில் மற்றும் குற்றவியல் ஆகிய இரு நடவடிக்கைகளையும் உள்ளடக்கியது.",
        "Incorrect. Enjoys identical parliamentary privileges as elected members under Article 194(4).", "தவறு. உறுப்பு 194(4)-ன் கீழ் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களுக்கு இணையான சட்டமன்ற சிறப்புரிமைகளை அவர் அனுபவிக்கிறார்.",
        "This absolute immunity ensures fearless, candid legal advice can be given on the floor of the House.",
        "இந்த முழுமையான பாதுகாப்பு சட்டமன்றத்தில் அச்சமின்றி, வெளிப்படையான சட்ட ஆலோசனையை வழங்க உதவுகிறது.",
        "The internal discipline of the House is maintained solely by the Speaker under House rules.",
        "அவையின் உள் ஒழுங்கு சபாநாயகரால் மட்டுமே சபை விதிகளின் கீழ் பராமரிக்கப்படுகிறது."
    )

    # --- 11 to 20 ---
    # Q11 (C)
    add_q(
        "ADVG_M_011", "Article 254 President's Assent Role",
        "In resolving an inconsistency between a State law and a Central law on a Concurrent List subject under Article 254, what is the role of the Advocate General?",
        "உறுப்பு 254-ன் கீழ் பொதுப் பட்டியல் விவகாரத்தில் மாநில சட்டத்திற்கும் மத்திய சட்டத்திற்கும் இடையிலான முரண்பாட்டைத் தீர்ப்பதில் தலைமை வழக்கறிஞரின் பங்கு என்ன?",
        "The Advocate General can overrule the Central law directly", "தலைமை வழக்கறிஞர் மத்திய சட்டத்தை நேரடியாக ரத்து செய்யலாம்",
        "He has the authority to grant Presidential assent himself", "குடியரசுத் தலைவரின் ஒப்புதலை அவரே வழங்கும் அதிகாரம் கொண்டுள்ளார்",
        "He advises the State Cabinet on drafting the state law and reserving it for the consideration and assent of the President under Article 254(2)", "மாநில சட்டத்தை வரைவு செய்வதிலும், உறுப்பு 254(2)-ன் கீழ் குடியரசுத் தலைவரின் பரிசீலனை மற்றும் ஒப்புதலுக்காக அதை நிறுத்தி வைப்பதிலும் மாநில அமைச்சரவைக்கு ஆலோசனை வழங்குகிறார்",
        "He has no role in matters involving Central-State legislative relations", "மத்திய-மாநில சட்டமன்ற உறவுகள் தொடர்பான விவகாரங்களில் அவருக்கு எந்தப் பங்கும் இல்லை",
        "C",
        "Under Article 254(2), a State law on a Concurrent subject repugnant to an earlier Central law prevails in that State only if it receives the assent of the President. The Advocate General advises the State on identifying repugnancies and seeking Presidential assent.",
        "உறுப்பு 254(2)-ன் கீழ், முந்தைய மத்திய சட்டத்திற்கு முரணான பொதுப் பட்டியல் மீதான மாநில சட்டம், குடியரசுத் தலைவரின் ஒப்புதலைப் பெற்றால் மட்டுமே அந்த மாநிலத்தில் நிலைத்து நிற்கும். முரண்பாடுகளைக் கண்டறிவதிலும், குடியரசுத் தலைவரின் ஒப்புதலைப் பெறுவதிலும் தலைமை வழக்கறிஞர் மாநிலத்திற்கு ஆலோசனை வழங்குகிறார்.",
        "Incorrect. Law officers cannot overrule legislation.", "தவறு. சட்ட அதிகாரிகளால் சட்டத்தை ரத்து செய்ய முடியாது.",
        "Incorrect. Only the President of India can grant assent under Article 254(2).", "தவறு. உறுப்பு 254(2)-ன் கீழ் குடியரசுத் தலைவர் மட்டுமே ஒப்புதல் அளிக்க முடியும்.",
        "Correct. Advises on drafting, constitutional repugnancy, and securing Presidential assent under Article 254(2).", "சரி. உறுப்பு 254(2)-ன் கீழ் சட்ட வரைவு, முரண்பாடுகள் மற்றும் குடியரசுத் தலைவர் ஒப்புதல் பெறுதல் ஆகியவற்றில் ஆலோசனை வழங்குகிறார்.",
        "Incorrect. AG plays a central role in all federal-state constitutional disputes.", "தவறு. அனைத்து கூட்டாட்சி-மாநில அரசியலமைப்பு விவகாரங்களிலும் தலைமை வழக்கறிஞர் முக்கியப் பங்கு வகிக்கிறார்.",
        "Article 254 is the paramount constitutional mechanism governing Union-State legislative supremacy on List III.",
        "பட்டியல் III-ல் மத்திய-மாநில சட்டமன்ற மேலாதிக்கத்தை நிர்வகிக்கும் மிக முக்கியமான அரசியலமைப்பு விதி உறுப்பு 254 ஆகும்.",
        "When the State law is challenged in the Supreme Court, the Advocate General defends its constitutional validity.",
        "மாநில சட்டம் உச்ச நீதிமன்றத்தில் சவாலுக்கு உள்ளாகும் போது, தலைமை வழக்கறிஞரே அதன் அரசியலமைப்பு செல்லுபடி தன்மையை பாதுகாக்கிறார்."
    )

    # Q12 (D)
    add_q(
        "ADVG_M_012", "Section 321 CrPC Withdrawal Role",
        "Under Section 321 of the Code of Criminal Procedure (CrPC), 1973 (and Section 360 of Bharatiya Nagarik Suraksha Sanhita), who is legally empowered to withdraw from a criminal prosecution?",
        "குற்றவியல் நடைமுறைச் சட்டம் 1973 பிரிவு 321-ன் கீழ் (மற்றும் பாரதிய நகரிக் சுரக்ஷா சன்ஹிதா பிரிவு 360), குற்றவியல் வழக்கைத் திரும்பப் பெற சட்டப்பூர்வமாக அதிகாரம் பெற்றவர் யார்?",
        "The Governor of the State alone", "மாநில ஆளுநர் மட்டுமே",
        "The Advocate General alone without court permission", "நீதிமன்ற அனுமதியின்றி தலைமை வழக்கறிஞர் மட்டுமே",
        "The Chief Minister through an executive order", "ஒரு நிர்வாக உத்தரவின் மூலம் முதலமைச்சர்",
        "The Public Prosecutor or Assistant Public Prosecutor in charge of the case, with the consent of the court", "நீதிமன்றத்தின் ஒப்புதலுடன் அவ்வழக்கை நடத்தும் அரசு வழக்கறிஞர் (Public Prosecutor) அல்லது உதவி அரசு வழக்கறிஞர்",
        "D",
        "Under Section 321 CrPC / Section 360 BNSS, only the Public Prosecutor or Assistant Public Prosecutor in charge of a case can apply to withdraw from prosecution, and that too only with the consent of the court. While the State Government or Advocate General may advise, the legal act belongs to the Prosecutor.",
        "பிரிவு 321 CrPC / பிரிவு 360 BNSS-ன் கீழ், வழக்கை நடத்தும் அரசு வழக்கறிஞர் அல்லது உதவி அரசு வழக்கறிஞர் மட்டுமே வழக்கைத் திரும்பப் பெற விண்ணப்பிக்க முடியும், அதுவும் நீதிமன்றத்தின் ஒப்புதலுடன் மட்டுமே. மாநில அரசோ அல்லது தலைமை வழக்கறிஞரோ ஆலோசனை வழங்கினாலும், சட்டப்பூர்வ நடவடிக்கை அரசு வழக்கறிஞருக்கே உரியது.",
        "Incorrect. Governor exercises pardon under Art 161, not withdrawal under Section 321.", "தவறு. ஆளுநர் உறுப்பு 161-ன் கீழ் மன்னிப்பளிக்கிறார், பிரிவு 321-ன் கீழ் வழக்கை திரும்பப் பெறுவதில்லை.",
        "Incorrect. Advocate General cannot bypass the Public Prosecutor in charge of the trial court.", "தவறு. விசாரணை நீதிமன்ற அரசு வழக்கறிஞரை மீறி தலைமை வழக்கறிஞரால் செயல்பட முடியாது.",
        "Incorrect. Chief Minister cannot unilaterally withdraw cases by executive decree.", "தவறு. முதலமைச்சர் நிர்வாக ஆணை மூலம் தன்னிச்சையாக வழக்குகளைத் திரும்பப் பெற முடியாது.",
        "Correct. The Public Prosecutor in charge of the case, with the consent of the court, exercises this statutory power.", "சரி. வழக்கை நடத்தும் அரசு வழக்கறிஞர் நீதிமன்றத்தின் ஒப்புதலுடன் இந்த சட்டப்பூர்வ அதிகாரத்தைப் பயன்படுத்துகிறார்.",
        "In Sheonandan Paswan v. State of Bihar (1987), the Supreme Court reiterated that the Public Prosecutor must apply his own independent mind.",
        "ஷிவநந்தன் பாஸ்வான் வழக்கில் (1987), அரசு வழக்கறிஞர் தனது சொந்த சுதந்திரமான சிந்தனையைப் பயன்படுத்த வேண்டும் என்று உச்ச நீதிமன்றம் மீண்டும் வலியுறுத்தியது.",
        "The Advocate General's legal opinion is frequently sought by the Home Department before directing the Public Prosecutor.",
        "அரசு வழக்கறிஞருக்கு வழிகாட்டுவதற்கு முன்பு உள்துறை தலைமை வழக்கறிஞரின் சட்ட ஆலோசனையை அடிக்கடி கோருகிறது."
    )

    # Q13 (A)
    add_q(
        "ADVG_M_013", "Article 161 Pardon Legal Advice",
        "When the Governor exercises the power to grant pardons, reprieves, respites, or remissions of punishment under Article 161 of the Constitution, whose legal guidance is typically sought by the State Government?",
        "அரசியலமைப்பின் உறுப்பு 161-ன் கீழ் மன்னிப்பு, தண்டனைக் குறைப்பு அல்லது நிறுத்திவைப்பு ஆகிய அதிகாரங்களை ஆளுநர் பயன்படுத்தும் போது, மாநில அரசு பொதுவாக யாருடைய சட்ட வழிகாட்டுதலைப் பெறுகிறது?",
        "The Advocate General of the State", "மாநில தலைமை வழக்கறிஞர்",
        "The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
        "The Union Home Secretary", "ஒன்றிய உள்துறைச் செயலாளர்",
        "The Director of the Central Bureau of Investigation", "மத்திய புலனாய்வுத் துறையின் (CBI) இயக்குநர்",
        "A",
        "In high-profile clemency petitions and remission policies under Article 161, the State Cabinet routinely consults the Advocate General to ensure that proposed remissions comply with constitutional standards and Supreme Court precedents (e.g., Maru Ram, Kehar Singh, Perarivalan).",
        "உறுப்பு 161-ன் கீழ் முக்கிய கருணை மனுக்கள் மற்றும் தண்டனைக் குறைப்புக் கொள்கைகளில், முன்மொழியப்பட்ட முடிவுகள் அரசியலமைப்புத் தரநிலைகள் மற்றும் உச்ச நீதிமன்றத் தீர்ப்புகளுக்கு (எ.கா. மாரு ராம், கேஹர் சிங், பேரறிவாளன்) இணங்குவதை உறுதி செய்ய மாநில அமைச்சரவை தலைமை வழக்கறிஞரைக் கலந்தாலோசிக்கிறது.",
        "Correct. The Advocate General provides expert legal guidance to the State Government on Article 161 powers.", "சரி. உறுப்பு 161 அதிகாரங்கள் குறித்து மாநில அரசுக்கு தலைமை வழக்கறிஞர் நிபுணத்துவ சட்ட வழிகாட்டுதலை வழங்குகிறார்.",
        "Incorrect. CJI does not advise state governments on executive clemency.", "தவறு. நிர்வாக மன்னிப்பு குறித்து மாநில அரசுகளுக்கு இந்திய தலைமை நீதிபதி ஆலோசனை வழங்குவதில்லை.",
        "Incorrect. Article 161 is purely a State executive power; Union Home Secretary does not advise State Governors.", "தவறு. உறுப்பு 161 முற்றிலும் ஒரு மாநில நிர்வாக அதிகாரம்; ஒன்றிய உள்துறைச் செயலாளர் மாநில ஆளுநர்களுக்கு ஆலோசனை வழங்குவதில்லை.",
        "Incorrect. CBI Director has no role in advising on constitutional clemency.", "தவறு. அரசியலமைப்பு கருணை மனுக்கள் குறித்து ஆலோசனை வழங்குவதில் சிபிஐ இயக்குநருக்கு எந்தப் பங்கும் இல்லை.",
        "In A.G. Perarivalan v. State (2022), the Supreme Court held that the Governor is bound by the advice of the State Cabinet under Article 161.",
        "பேரறிவாளன் வழக்கில் (2022), உறுப்பு 161-ன் கீழ் ஆளுநர் மாநில அமைச்சரவையின் ஆலோசனைக்கு கட்டுப்பட்டவர் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "The Advocate General drafts the legal submissions defending the State's remission decisions before the courts.",
        "நீதிமன்றங்களின் முன் மாநிலத்தின் தண்டனைக் குறைப்பு முடிவுகளை ஆதரிக்கும் சட்ட வாதங்களை தலைமை வழக்கறிஞர் வரைகிறார்."
    )

    # Q14 (B)
    add_q(
        "ADVG_M_014", "Article 134A Certificate Role",
        "Can the Advocate General of a State grant a Certificate of Fitness for appeal to the Supreme Court under Article 134A?",
        "உறுப்பு 134A-ன் கீழ் உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்வதற்கான தகுதிச் சான்றிதழை (Certificate of Fitness) மாநில தலைமை வழக்கறிஞர் வழங்க முடியுமா?",
        "Yes, on his own authority in constitutional matters", "ஆம், அரசியலமைப்பு விவகாரங்களில் தனது சொந்த அதிகாரத்தின் கீழ் வழங்கலாம்",
        "No, the Certificate of Fitness under Article 134A can only be granted by the High Court", "இல்லை, உறுப்பு 134A-ன் கீழ் தகுதிச் சான்றிதழை உயர் நீதிமன்றம் மட்டுமே வழங்க முடியும்",
        "Yes, jointly with the State Law Minister", "ஆம், மாநில சட்ட அமைச்சருடன் இணைந்து வழங்கலாம்",
        "Yes, but only if the dispute involves another State", "ஆம், ஆனால் வழக்கு மற்றொரு மாநிலத்தை உள்ளடக்கியதாக இருந்தால் மட்டுமே",
        "B",
        "Article 134A provides that the High Court may, on its own motion or on an oral application made by or on behalf of any party, determine whether a certificate of fitness for appeal to the Supreme Court (under Arts 132, 133, 134) should be granted. It is an exclusive judicial function of the High Court, not an executive power of the Advocate General.",
        "உறுப்பு 134A உயர் நீதிமன்றம் தனது சொந்த முயற்சியிலோ அல்லது ஒரு தரப்பினரின் விண்ணப்பத்தின் பேரிலோ உச்ச நீதிமன்றத்திற்கு மேல்முறையீடு செய்வதற்கான தகுதிச் சான்றிதழை (உறுப்புகள் 132, 133, 134-ன் கீழ்) வழங்கலாமா என்பதை தீர்மானிக்கலாம் என்று கூறுகிறது. இது உயர் நீதிமன்றத்தின் பிரத்தியேக நீதித்துறை பணியாகும், அட்வகேட் ஜெனரலின் நிர்வாக அதிகாரம் அல்ல.",
        "Incorrect. The Advocate General can only apply for a certificate as counsel, but cannot grant it.", "தவறு. தலைமை வழக்கறிஞர் ஒரு வழக்கறிஞராக சான்றிதழுக்கு விண்ணப்பிக்க மட்டுமே முடியும், அதை வழங்க முடியாது.",
        "Correct. Under Article 134A, only the High Court has the judicial authority to grant a Certificate of Fitness.", "சரி. உறுப்பு 134A-ன் கீழ் தகுதிச் சான்றிதழை வழங்கும் நீதித்துறை அதிகாரம் உயர் நீதிமன்றத்திற்கு மட்டுமே உண்டு.",
        "Incorrect. The Law Minister has no judicial certification power.", "தவறு. சட்ட அமைச்சருக்கு நீதித்துறை சான்றிதழ் அளிக்கும் அதிகாரம் இல்லை.",
        "Incorrect. Inter-state status does not change the judicial nature of Article 134A certification.", "தவறு. மாநிலங்களுக்கு இடையேயான சர்ச்சை உறுப்பு 134A சான்றிதழின் நீதித்துறை தன்மையை மாற்றாது.",
        "If the High Court refuses a certificate under Article 134A, the Advocate General advises the State on filing a Special Leave Petition (SLP) under Article 136.",
        "உயர் நீதிமன்றம் உறுப்பு 134A-ன் கீழ் சான்றிதழை மறுத்தால், உறுப்பு 136-ன் கீழ் சிறப்பு விடுப்பு மனுவை (SLP) தாக்கல் செய்ய தலைமை வழக்கறிஞர் மாநிலத்திற்கு ஆலோசனை வழங்குகிறார்.",
        "Article 134A was inserted by the 44th Constitutional Amendment Act, 1978.",
        "உறுப்பு 134A 1978-ஆம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டது."
    )

    # Q15 (C)
    add_q(
        "ADVG_M_015", "RTI Act Public Authority Status",
        "Is the office of the Advocate General of a State considered a 'Public Authority' under Section 2(h) of the Right to Information (RTI) Act, 2005?",
        "தகவல் அறியும் உரிமைச் சட்டம் (RTI) 2005-ன் பிரிவு 2(h)-ன் கீழ் மாநில தலைமை வழக்கறிஞர் அலுவலகம் ஒரு 'பொது அதிகாரம் கொண்ட அமைப்பாக' (Public Authority) கருதப்படுகிறதா?",
        "No, constitutional offices are completely exempt from RTI Act", "இல்லை, அரசியலமைப்பு அலுவலகங்கள் RTI சட்டத்திலிருந்து முற்றிலும் விலக்களிக்கப்பட்டுள்ளன",
        "No, because the Advocate General is an independent professional advocate", "இல்லை, ஏனெனில் தலைமை வழக்கறிஞர் ஒரு சுதந்திரமான தொழில்முறை வழக்கறிஞர் ஆவார்",
        "Yes, because it is an authority or body established by the Constitution of India under Article 165", "ஆம், ஏனெனில் இது இந்திய அரசியலமைப்பின் உறுப்பு 165-ன் கீழ் நிறுவப்பட்ட ஓர் அமைப்பாகும்",
        "Only during sessions of the State Legislative Assembly", "மாநில சட்டமன்ற கூட்டத்தொடர் நடைபெறும் போது மட்டுமே",
        "C",
        "Under Section 2(h)(a) of the RTI Act, 2005, 'public authority' means any authority or body or institution established or constituted by or under the Constitution. Since the Advocate General is established by Article 165, various High Courts (e.g., Kerala, Madras) have affirmed that his office is a Public Authority, though professional communications are protected by legal privilege under Section 8(1)(e).",
        "RTI சட்டம் 2005 பிரிவு 2(h)(a)-ன் படி, அரசியலமைப்பால் அல்லது அதன் கீழ் நிறுவப்பட்ட எந்தவொரு அதிகார அமைப்பும் 'பொது அதிகாரம் கொண்ட அமைப்பாகும்'. உறுப்பு 165-ன் கீழ் தலைமை வழக்கறிஞர் பதவி நிறுவப்பட்டுள்ளதால், அவரது அலுவலகம் ஒரு பொது அதிகாரம் கொண்ட அமைப்பாகும் என்று பல்வேறு உயர் நீதிமன்றங்கள் (எ.கா. கேரளா, சென்னை) உறுதிப்படுத்தியுள்ளன, எனினும் தொழில்முறை தகவல்தொடர்புகள் பிரிவு 8(1)(e)-ன் கீழ் பாதுகாக்கப்படுகின்றன.",
        "Incorrect. Constitutional offices (President, Governor, CAG, AG) are not exempt from the definition of Public Authority.", "தவறு. அரசியலமைப்பு அலுவலகங்கள் பொது அதிகாரம் கொண்ட அமைப்பு என்ற வரையறையிலிருந்து விலக்களிக்கப்படவில்லை.",
        "Incorrect. Professional status does not negate constitutional establishment under Art 165.", "தவறு. தொழில்முறை நிலை என்பது உறுப்பு 165-ன் கீழ் அரசியலமைப்பு ரீதியாக நிறுவப்பட்டதை ரத்து செய்யாது.",
        "Correct. It is a Public Authority under Section 2(h)(a) of RTI Act 2005.", "சரி. இது RTI சட்டம் 2005-ன் பிரிவு 2(h)(a)-ன் கீழ் ஒரு பொது அதிகாரம் கொண்ட அமைப்பாகும்.",
        "Incorrect. Legislative session status has no relevance to RTI applicability.", "தவறு. சட்டமன்ற கூட்டத்தொடர் நிலைக்கும் RTI பயன்பாட்டிற்கும் எந்த தொடர்பும் இல்லை.",
        "While the office is a Public Authority, client-advocate communications between the State Government and the AG are protected under Section 126/129 Evidence Act and Sec 8(1)(e) RTI.",
        "அலுவலகம் பொது அமைப்பாக இருந்தாலும், அரசுக்கும் AG-க்கும் இடையிலான வழக்கறிஞர்-வாடிக்கையாளர் தகவல்தொடர்புகள் சட்டப்பூர்வமாக பாதுகாக்கப்படுகின்றன.",
        "Administrative records, staff appointments, and expenditure of the AG's office are disclosable under RTI.",
        "தலைமை வழக்கறிஞர் அலுவலகத்தின் நிர்வாக ஆவணங்கள், பணியாளர் நியமனங்கள் மற்றும் செலவினங்கள் RTI-ன் கீழ் வெளிப்படுத்தப்படக் கூடியவை."
    )

    # Q16 (D)
    add_q(
        "ADVG_M_016", "Difference from Law Secretary",
        "What is the key administrative and constitutional distinction between the Advocate General and the State Law Secretary?",
        "மாநில தலைமை வழக்கறிஞருக்கும் மாநில சட்டத்துறைச் செயலாளருக்கும் இடையிலான முக்கிய நிர்வாக மற்றும் அரசியலமைப்பு வேறுபாடு என்ன?",
        "The Law Secretary is a constitutional post under Article 165; the Advocate General is a statutory post", "சட்டச் செயலாளர் உறுப்பு 165-ன் கீழ் ஒரு அரசியலமைப்புப் பதவி; தலைமை வழக்கறிஞர் ஒரு சட்டப்பூர்வப் பதவி",
        "The Advocate General is an IAS officer; the Law Secretary is a senior advocate", "தலைமை வழக்கறிஞர் ஒரு ஐஏஎஸ் அதிகாரி; சட்டச் செயலாளர் ஒரு மூத்த வழக்கறிஞர்",
        "The Law Secretary appears in court to argue all cases, while the Advocate General works only in the Secretariat", "சட்டச் செயலாளர் நீதிமன்றத்தில் வழக்குகளை வாதிடுகிறார், தலைமை வழக்கறிஞர் தலைமைச் செயலகத்தில் மட்டுமே பணியாற்றுகிறார்",
        "The Advocate General is an independent constitutional law officer under Article 165; the Law Secretary is a full-time civil servant heading the Law Department", "தலைமை வழக்கறிஞர் உறுப்பு 165-ன் கீழ் ஒரு சுதந்திரமான அரசியலமைப்பு சட்ட அதிகாரி; சட்டச் செயலாளர் சட்டத்துறையின் தலைவராக உள்ள முழுநேர அரசு ஊழியர் ஆவார்",
        "D",
        "The Advocate General is a constitutional functionary under Article 165 who advises the State and represents it in court. The Law Secretary is a full-time civil servant (typically a senior district judge on deputation) who heads the administrative Law Department in the Secretariat.",
        "தலைமை வழக்கறிஞர் உறுப்பு 165-ன் கீழ் அரசுக்கு ஆலோசனை வழங்கும் மற்றும் நீதிமன்றத்தில் வாதாடும் அரசியலமைப்புப் பொறுப்பாளர் ஆவார். சட்டச் செயலாளர் என்பவர் தலைமைச் செயலகத்தில் உள்ள நிர்வாக சட்டத்துறையை வழிநடத்தும் முழுநேர அரசு ஊழியர் (வழக்கமாக அயல்பணியில் உள்ள மூத்த மாவட்ட நீதிபதி) ஆவார்.",
        "Incorrect. The reverse is true: AG is constitutional (Art 165), while Law Secretary is an administrative civil post.", "தவறு. தலைகீழானது உண்மை: AG அரசியலமைப்புப் பதவி (உறுப்பு 165), சட்டச் செயலாளர் நிர்வாகப் பதவி.",
        "Incorrect. The Advocate General is drawn from the Bar, not IAS.", "தவறு. தலைமை வழக்கறிஞர் வழக்கறிஞர் சங்கத்திலிருந்து தேர்வு செய்யப்படுகிறார், ஐஏஎஸ் அல்ல.",
        "Incorrect. Law Secretary manages administrative files; the Advocate General argues in court.", "தவறு. சட்டச் செயலாளர் நிர்வாகக் கோப்புகளை நிர்வகிக்கிறார்; தலைமை வழக்கறிஞர் நீதிமன்றத்தில் வாதாடுகிறார்.",
        "Correct. The Advocate General is a constitutional officer, while the Law Secretary is a career civil servant.", "சரி. தலைமை வழக்கறிஞர் ஓர் அரசியலமைப்பு அதிகாரி, சட்டச் செயலாளர் பணியில் உள்ள அரசு ஊழியர்.",
        "The Law Secretary processes files, drafts government orders, and coordinates with the Advocate General's office.",
        "சட்டச் செயலாளர் கோப்புகளைச் செயல்படுத்துகிறார், அரசாணைகளை வரைகிறார் மற்றும் தலைமை வழக்கறிஞர் அலுவலகத்துடன் ஒருங்கிணைந்து செயல்படுகிறார்.",
        "The Advocate General provides external, independent legal counsel on complex constitutional questions.",
        "சிக்கலான அரசியலமைப்பு வினாக்களில் தலைமை வழக்கறிஞர் வெளிப்புற, சுதந்திரமான சட்ட ஆலோசனையை வழங்குகிறார்."
    )

    # Q17 (A)
    add_q(
        "ADVG_M_017", "Privilege from Arrest",
        "Does the Advocate General enjoy freedom from arrest in civil cases under parliamentary/legislative privileges during sessions of the State Legislature?",
        "மாநில சட்டமன்ற கூட்டத்தொடரின் போது, சட்டமன்ற சிறப்புரிமைகளின் கீழ் சிவில் வழக்குகளில் கைது செய்யப்படுவதிலிருந்து விலக்களிப்பை தலைமை வழக்கறிஞர் அனுபவிக்கிறாரா?",
        "Yes, under Article 194(4) read with Section 135A of the Code of Civil Procedure, during legislative sessions and 40 days before and after", "ஆம், உறுப்பு 194(4) மற்றும் சிவில் நடைமுறைச் சட்டம் பிரிவு 135A-ன் கீழ், சட்டமன்ற கூட்டத்தொடர் நடைபெறும் போதும் மற்றும் அதற்கு 40 நாட்களுக்கு முன்னும் பின்னும்",
        "No, freedom from arrest is exclusively restricted to elected MLAs", "இல்லை, கைது செய்யப்படுவதிலிருந்து விலக்களிப்பு தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏக்களுக்கு மட்டுமே உரியது",
        "Yes, but only inside the Legislative Assembly chamber", "ஆம், ஆனால் சட்டமன்றப் பேரவை அறைக்குள் மட்டுமே",
        "Yes, and this protection extends unconditionally to criminal offenses and preventive detention", "ஆம், மேலும் இந்த பாதுகாப்பு குற்றவியல் குற்றங்கள் மற்றும் தடுப்புக் காவலுக்கும் நிபந்தனையின்றி நீட்டிக்கப்படுகிறது",
        "A",
        "By virtue of Article 194(4), the Advocate General enjoys the same powers, privileges, and immunities as a member of the State Legislature. Under Section 135A CPC, members enjoy freedom from arrest in civil cases during the continuance of a meeting of the House or committee and for 40 days before and after.",
        "உறுப்பு 194(4)-ன் படி, தலைமை வழக்கறிஞர் சட்டமன்ற உறுப்பினரின் அதே அதிகாரங்கள், சிறப்புரிமைகள் மற்றும் விலக்களிப்புகளை அனுபவிக்கிறார். CPC பிரிவு 135A-ன் கீழ், உறுப்பினர்கள் அவைக் கூட்டம் அல்லது குழுக்கூட்டம் நடைபெறும் போதும், அதற்கு 40 நாட்களுக்கு முன்னும் பின்னும் சிவில் வழக்குகளில் கைது செய்யப்படுவதிலிருந்து பாதுகாப்பு பெறுகின்றனர்.",
        "Correct. Enjoys civil arrest immunity for 40 days before, during, and 40 days after legislative sessions under Art 194(4) / Sec 135A CPC.", "சரி. உறுப்பு 194(4) / CPC பிரிவு 135A-ன் கீழ் கூட்டத்தொடருக்கு 40 நாட்களுக்கு முன், பின் மற்றும் தொடரின் போது சிவில் கைது விலக்களிப்பைப் பெறுகிறார்.",
        "Incorrect. Article 194(4) explicitly extends member privileges to all persons entitled to speak in the House, including the AG.", "தவறு. உறுப்பு 194(4) அவையில் பேச உரிமை கொண்ட அனைவருக்கும் (AG உட்பட) உறுப்பினர் சிறப்புரிமைகளை வெளிப்படையாக நீட்டிக்கிறது.",
        "Incorrect. The 40-day temporal protection extends outside the chamber as well.", "தவறு. 40 நாள் காலப் பாதுகாப்பு அவைக்கு வெளியேயும் நீட்டிக்கப்படுகிறது.",
        "Incorrect. Parliamentary privilege does not protect against criminal offenses, preventive detention, or contempt of court.", "தவறு. நாடாளுமன்ற சிறப்புரிமை குற்றவியல் குற்றங்கள், தடுப்புக் காவல் அல்லது நீதிமன்ற அவமதிப்பு ஆகியவற்றிற்கு எதிராகப் பாதுகாக்காது.",
        "Crucial distinction: Immunity from arrest applies ONLY to civil matters, NEVER to criminal charges or preventive detention.",
        "முக்கிய வேறுபாடு: கைது விலக்களிப்பு சிவில் விவகாரங்களுக்கு மட்டுமே பொருந்தும், குற்றவியல் குற்றச்சாட்டுகளுக்கோ அல்லது தடுப்புக் காவலுக்கோ ஒருபோதும் பொருந்தாது.",
        "This is identical to the privilege enjoyed by Members of Parliament under Article 105.",
        "இது உறுப்பு 105-ன் கீழ் நாடாளுமன்ற உறுப்பினர்கள் அனுபவிக்கும் சிறப்புரிமைக்கு முற்றிலும் இணையானது."
    )

    # Q18 (B)
    add_q(
        "ADVG_M_018", "Legal Opinion Confidentiality BSA",
        "Under Section 126 and Section 129 of the Indian Evidence Act, 1872 (now covered under Bharatiya Sakshya Adhiniyam, 2023), how is the legal communication between the State Government and the Advocate General classified?",
        "இந்திய சாட்சியச் சட்டம் 1872 பிரிவு 126 மற்றும் 129-ன் கீழ் (தற்போது பாரதிய சாக்ஷிய அதினியம் 2023-ல் உள்ளபடி), மாநில அரசுக்கும் தலைமை வழக்கறிஞருக்கும் இடையிலான சட்டப்பூர்வ தகவல்தொடர்பு எவ்வாறு வகைப்படுத்தப்படுகிறது?",
        "As open public records disclosable to any litigant on demand", "கோரிக்கையின் பேரில் எந்தவொரு வழக்காடிக்கும் வெளிப்படுத்தக்கூடிய திறந்த பொது ஆவணங்களாக",
        "As privileged professional communication protected from disclosure without the client's (State Government's) express consent", "வாடிக்கையாளரின் (மாநில அரசின்) வெளிப்படையான இசைவின்றி வெளிப்படுத்துவதிலிருந்து பாதுகாக்கப்பட்ட தொழில்முறை ரகசியத் தகவல்தொடர்பாக",
        "As secret military documents governed by the Official Secrets Act", "அரசு ரகசியங்கள் சட்டத்தால் நிர்வகிக்கப்படும் ரகசிய இராணுவ ஆவணங்களாக",
        "As judicial orders binding on all civil courts", "அனைத்து சிவில் நீதிமன்றங்களையும் கட்டுப்படுத்தும் நீதித்துறை உத்தரவுகளாக",
        "B",
        "Communications between an advocate and his client are protected under attorney-client privilege (Sections 126 and 129 Evidence Act / BSA). The Advocate General cannot be compelled to disclose the advice tendered by him to the State Government without the government's consent.",
        "வழக்கறிஞருக்கும் அவரது வாடிக்கையாளருக்கும் இடையிலான தகவல்தொடர்புகள் வழக்கறிஞர்-வாடிக்கையாளர் சிறப்புரிமையின் கீழ் பாதுகாக்கப்படுகின்றன (சாட்சியச் சட்டம் / BSA பிரிவு 126 மற்றும் 129). அரசின் அனுமதியின்றி தலைமை வழக்கறிஞர் அரசுக்கு வழங்கிய ஆலோசனையை வெளிப்படுத்த நீதிமன்றங்களால் கட்டாயப்படுத்த முடியாது.",
        "Incorrect. Legal advice to client is not an open public document.", "தவறு. வாடிக்கையாளருக்கான சட்ட ஆலோசனை திறந்த பொது ஆவணம் அல்ல.",
        "Correct. Protected as privileged professional communication under Section 126 Evidence Act / BSA.", "சரி. சாட்சியச் சட்டம் / BSA பிரிவு 126-ன் கீழ் தொழில்முறை ரகசியத் தகவல்தொடர்பாக பாதுகாக்கப்படுகிறது.",
        "Incorrect. Not classified as military secrets.", "தவறு. இராணுவ ரகசியங்களாக வகைப்படுத்தப்படுவதில்லை.",
        "Incorrect. Legal opinions are advisory communications, not judicial orders.", "தவறு. சட்டக் கருத்துகள் ஆலோசனைத் தகவல்தொடர்புகளே தவிர, நீதித்துறை உத்தரவுகள் அல்ல.",
        "This privilege enables the State Government to receive honest, unvarnished legal opinions on sensitive policy issues.",
        "இந்த சிறப்புரிமை மாநில அரசு உணர்வுப்பூர்வமான கொள்கை விவகாரங்களில் நேர்மையான, அஞ்சாத சட்டக் கருத்துகளைப் பெற உதவுகிறது.",
        "However, if the State Government waives this privilege, the opinion may be produced in court.",
        "எனினும், மாநில அரசு இந்த சிறப்புரிமையை கைவிட்டால், அந்த ஆலோசனையை நீதிமன்றத்தில் சமர்ப்பிக்கலாம்."
    )

    # Q19 (C)
    add_q(
        "ADVG_M_019", "Article 356 President's Rule Effect",
        "When President's Rule is imposed in a State under Article 356 and the State Council of Ministers is dismissed, what usually happens to the Advocate General?",
        "உறுப்பு 356-ன் கீழ் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி அமல்படுத்தப்பட்டு, மாநில அமைச்சரவை பதவிநீக்கம் செய்யப்படும் போது, வழக்கமாக தலைமை வழக்கறிஞருக்கு என்ன நேரிடுகிறது?",
        "He automatically becomes the Governor of the State", "அவர் தானாகவே மாநிலத்தின் ஆளுநராக ஆகிவிடுகிறார்",
        "He is granted a permanent 5-year tenure by the President", "குடியரசுத் தலைவரால் அவருக்கு நிரந்தர 5 ஆண்டு பதவிக்காலம் வழங்கப்படுகிறது",
        "He conventionally tenders his resignation, or the Governor / President may appoint a new Advocate General or allow him to continue during the transition", "வழக்கமாக அவர் தனது பதவி விலகல் கடிதத்தை வழங்குகிறார், அல்லது ஆளுநர்/குடியரசுத் தலைவர் புதிய தலைமை வழக்கறிஞரை நியமிக்கலாம் அல்லது மாற்றுக் காலத்தில் அவரைத் தொடர அனுமதிக்கலாம்",
        "He assumes the powers of the Speaker of the Legislative Assembly", "அவர் சட்டப் பேரவைத் தலைவரின் அதிகாரங்களை ஏற்கிறார்",
        "C",
        "Because the Advocate General holds office during the pleasure of the Governor and is appointed on the advice of the Council of Ministers, when the Council of Ministers is dismissed upon imposition of President's Rule (Article 356), the AG conventionally submits his resignation. The Governor (administering on behalf of the President) may accept it and appoint a new AG or request him to continue.",
        "தலைமை வழக்கறிஞர் ஆளுநரின் விருப்பத்தின் பேரில் பதவி வகிப்பதாலும், அமைச்சரவையின் ஆலோசனையின்படி நியமிக்கப்படுவதாலும், உறுப்பு 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி விதிக்கப்பட்டு அமைச்சரவை கலைக்கப்படும் போது, வழக்கமாக தலைமை வழக்கறிஞர் பதவி விலகுகிறார். ஆளுநர் புதியவரை நியமிக்கலாம் அல்லது அவரைத் தொடரக் கோரலாம்.",
        "Incorrect. AG cannot become Governor.", "தவறு. தலைமை வழக்கறிஞர் ஆளுநராக முடியாது.",
        "Incorrect. President's rule does not confer permanent tenure.", "தவறு. குடியரசுத் தலைவர் ஆட்சி நிரந்தர பதவிக்காலத்தை வழங்காது.",
        "Correct. Conventionally tenders resignation, or executive arrangements are made during President's Rule.", "சரி. வழக்கமாக பதவி விலகல் கடிதத்தை சமர்ப்பிக்கிறார், அல்லது நிர்வாக ஏற்பாடுகள் செய்யப்படுகின்றன.",
        "Incorrect. Speaker's powers are legislative, which AG cannot assume.", "தவறு. சபாநாயகரின் அதிகாரங்கள் சட்டமன்றத்திற்குரியவை, அவற்றை AG ஏற்க முடியாது.",
        "During President's Rule, the Governor exercises executive power with the assistance of appointed Advisors.",
        "குடியரசுத் தலைவர் ஆட்சியின் போது, ஆளுநர் நியமிக்கப்பட்ட ஆலோசகர்களின் உதவியுடன் நிர்வாக அதிகாரத்தைப் பயன்படுத்துகிறார்.",
        "The office of the Advocate General remains a constitutional necessity to conduct State litigation before the High Court.",
        "உயர் நீதிமன்றத்தில் மாநில வழக்குகளை நடத்த தலைமை வழக்கறிஞர் அலுவலகம் தொடர்ந்து ஓர் அரசியலமைப்புத் தேவையாகவே நீடிக்கிறது."
    )

    # Q20 (D)
    add_q(
        "ADVG_M_020", "Arbitration Proceedings",
        "Can the Advocate General of a State represent the State Government in international or domestic commercial arbitration proceedings?",
        "சர்வதேச அல்லது உள்நாட்டு வணிக நடுவர் தீர்ப்பாய (Arbitration) நடவடிக்கைகளில் மாநில அரசின் சார்பில் தலைமை வழக்கறிஞர் முன்னிலையாகி வாதாட முடியுமா?",
        "No, the Advocate General can only appear in constitutional courts (HC and SC)", "இல்லை, தலைமை வழக்கறிஞர் அரசியலமைப்பு நீதிமன்றங்களில் (HC மற்றும் SC) மட்டுமே ஆஜராக முடியும்",
        "No, commercial arbitration is strictly handled by private corporate lawyers", "இல்லை, வணிக நடுவர் மன்றங்கள் தனியார் கார்ப்பரேட் வழக்கறிஞர்களால் மட்டுமே கையாளப்படுகின்றன",
        "Only if appointed as the sole arbitrator by the parties", "தரப்பினரால் ஒரே நடுவராக (Sole Arbitrator) நியமிக்கப்பட்டால் மட்டுமே",
        "Yes, the State Government can engage the Advocate General to lead its case before domestic or international arbitration tribunals", "ஆம், உள்நாட்டு அல்லது சர்வதேச நடுவர் தீர்ப்பாயங்களில் தனது வழக்கிற்கு தலைமை தாங்க மாநில அரசு தலைமை வழக்கறிஞரை ஈடுபடுத்தலாம்",
        "D",
        "The State Government frequently entrusts high-stakes infrastructure, public-private partnership (PPP), and commercial arbitrations under the Arbitration and Conciliation Act, 1996 to the Advocate General to safeguard the public exchequer.",
        "பொது நிதி மற்றும் மாநில நலன்களைப் பாதுகாக்க, 1996-ஆம் ஆண்டின் நடுவர் மற்றும் சமரசச் சட்டத்தின் கீழ் உள்ள முக்கிய உள்கட்டமைப்பு, பொது-தனியார் கூட்டு (PPP) மற்றும் வணிக நடுவர் வழக்குகளை தலைமை வழக்கறிஞரிடம் மாநில அரசு அடிக்கடி ஒப்படைக்கிறது.",
        "Incorrect. AG's appearance is not restricted to constitutional courts.", "தவறு. தலைமை வழக்கறிஞரின் முன்னிலையாகும் உரிமை அரசியலமைப்பு நீதிமன்றங்களுக்கு மட்டுமேயானது அல்ல.",
        "Incorrect. State can instruct any competent law officer, especially the Advocate General.", "தவறு. அரசு எந்தவொரு தகுதியான சட்ட அதிகாரியையும், குறிப்பாக தலைமை வழக்கறிஞரை ஈடுபடுத்தலாம்.",
        "Incorrect. He appears as counsel for the State, not as arbitrator (acting as arbitrator for the State might create a conflict).", "தவறு. அவர் அரசின் வழக்கறிஞராக ஆஜராகிறார், நடுவராக அல்ல.",
        "Correct. Can represent the State in domestic or international arbitrations when instructed.", "சரி. அறிவுறுத்தப்படும் போது உள்நாட்டு அல்லது சர்வதேச நடுவர் மன்றங்களில் மாநிலத்தைப் பிரதிநிதித்துவப்படுத்தலாம்.",
        "Arbitration awards have direct financial implications on the Consolidated Fund of the State.",
        "நடுவர் தீர்ப்பாயத்தின் முடிவுகள் மாநில ஒருங்கிணைந்த நிதியின் மீது நேரடி நிதித் தாக்கத்தை ஏற்படுத்துகின்றன.",
        "Leading commercial arbitrations requires extensive expertise in contract law and commercial jurisprudence.",
        "வணிக நடுவர் மன்றங்களை வழிநடத்துவது ஒப்பந்தச் சட்டம் மற்றும் வணிக நீதித்துறையில் விரிவான நிபுணத்துவத்தைக் கோருகிறது."
    )

    # --- 21 to 30 ---
    # Q21 (A)
    add_q(
        "ADVG_M_021", "Lokayukta Representation",
        "Can the Advocate General of a State appear before the State Lokayukta to defend a Minister accused of corruption in his personal capacity?",
        "மாநில லோக்ஆயுக்தாவின் முன் தனிப்பட்ட முறையில் ஊழல் குற்றம் சாட்டப்பட்ட ஓர் அமைச்சரைப் பாதுகாப்பதற்காக தலைமை வழக்கறிஞர் ஆஜராக முடியுமா?",
        "No, the Advocate General cannot defend a public functionary in his personal capacity against corruption charges brought by the State / Lokayukta", "முடியாது, அரசு/லோக்ஆயுக்தா கொண்டுவரும் ஊழல் குற்றச்சாட்டுகளுக்கு எதிராக ஒரு பொதுப் பொறுப்பாளரின் தனிப்பட்ட முறையில் தலைமை வழக்கறிஞரால் வாதாட முடியாது",
        "Yes, he is bound to defend all Ministers under all circumstances", "ஆம், அனைத்து சூழ்நிலைகளிலும் அனைத்து அமைச்சர்களையும் பாதுகாக்க அவர் கடமைப்பட்டுள்ளார்",
        "Yes, if the Chief Minister gives an oral instruction", "ஆம், முதலமைச்சர் வாய்மொழி உத்தரவு பிறப்பித்தால் செய்யலாம்",
        "Yes, provided he charges private professional fees", "ஆம், தனிப்பட்ட தொழில்முறை கட்டணம் வசூலித்தால் செய்யலாம்",
        "A",
        "The Advocate General represents the State, not the personal interests of individual politicians. Appearing against anti-corruption bodies like Lokayukta to defend individual ministers creates a direct conflict of interest with his public duty.",
        "தலைமை வழக்கறிஞர் அரசைப் பிரதிநிதித்துவப்படுத்துகிறாரே தவிர, தனிப்பட்ட அரசியல்வாதிகளின் சுயநலனை அல்ல. தனிப்பட்ட அமைச்சர்களைப் பாதுகாக்க லோக்ஆயுக்தா போன்ற ஊழல் எதிர்ப்பு அமைப்புகளுக்கு எதிராக ஆஜராவது அவரது பொதுக் கடமையுடன் நேரடி நலன் முரண்பாட்டை உருவாக்குகிறது.",
        "Correct. Cannot defend public servants in personal corruption cases against the State.", "சரி. அரசுக்கு எதிரான தனிப்பட்ட ஊழல் வழக்குகளில் பொது ஊழியர்களை தலைமை வழக்கறிஞரால் ஆதரிக்க முடியாது.",
        "Incorrect. He is counsel for the State Government as an entity, not personal counsel for politicians.", "தவறு. அவர் ஒட்டுமொத்த மாநில அரசின் வழக்கறிஞர், அரசியல்வாதிகளின் தனிப்பட்ட வழக்கறிஞர் அல்ல.",
        "Incorrect. Oral instruction cannot override legal ethics and professional conduct rules.", "தவறு. வாய்மொழி உத்தரவு சட்ட நெறிமுறைகளையும் தொழில்முறை நடத்தை விதிகளையும் மீற முடியாது.",
        "Incorrect. Charging private fees compounds the conflict of interest.", "தவறு. தனியாக கட்டணம் வசூலிப்பது நலன் முரண்பாட்டை மேலும் அதிகரிக்கும்.",
        "Advocate General represents the crown / public interest; defending graft undermines the constitutional office.",
        "தலைமை வழக்கறிஞர் பொது நலனைப் பிரதிநிதித்துவப்படுத்துகிறார்; ஊழலை ஆதரிப்பது அரசியலமைப்பு பதவியின் கண்ணியத்தைக் குறைக்கும்.",
        "In such cases, the accused Minister must engage private defense counsel at his own expense.",
        "அத்தகைய வழக்குகளில், குற்றம் சாட்டப்பட்ட அமைச்சர் தனது சொந்த செலவில் தனிப்பட்ட வழக்கறிஞரையே நியமித்துக் கொள்ள வேண்டும்."
    )

    # Q22 (B)
    add_q(
        "ADVG_M_022", "Legal Opinion on Money Bills",
        "Under Article 199, if a dispute arises as to whether a Bill is a 'Money Bill' or not, whose decision is final, and what is the role of the Advocate General?",
        "உறுப்பு 199-ன் கீழ், ஒரு மசோதா 'நிதி மசோதா' (Money Bill) தானா என்பதில் சர்ச்சை எழுந்தால், யாருடைய முடிவு இறுதியானது, மற்றும் இதில் தலைமை வழக்கறிஞரின் பங்கு என்ன?",
        "The Advocate General's decision is final and unappealable", "தலைமை வழக்கறிஞரின் முடிவே இறுதியானது மற்றும் மேல்முறையீடு செய்ய முடியாதது",
        "The decision of the Speaker of the Legislative Assembly is final; the Advocate General can only tender legal advice if requested by the Speaker or Government", "சட்டப் பேரவைத் தலைவரின் (Speaker) முடிவே இறுதியானது; சபாநாயகரோ அல்லது அரசோ கோரினால் மட்டுமே தலைமை வழக்கறிஞர் சட்ட ஆலோசனை வழங்க முடியும்",
        "The High Court Chief Justice decides on the reference of the Advocate General", "தலைமை வழக்கறிஞரின் பரிந்துரையின் பேரில் உயர் நீதிமன்ற தலைமை நீதிபதி தீர்மானிக்கிறார்",
        "The State Finance Minister determines the status of Money Bills", "மாநில நிதி அமைச்சரே நிதி மசோதாவின் நிலையை தீர்மானிக்கிறார்",
        "B",
        "Under Article 199(3), if any question arises whether a Bill introduced in the Legislature of a State having a Legislative Council is a Money Bill or not, the decision of the Speaker of the Legislative Assembly thereon shall be final. The Advocate General may provide an advisory opinion on the bill's clauses if consulted.",
        "உறுப்பு 199(3)-ன் படி, ஒரு மசோதா நிதி மசோதாவா இல்லையா என்ற கேள்வி எழுந்தால், சட்டப் பேரவைத் தலைவரின் முடிவே இறுதியானது. ஆலோசனை கோரப்பட்டால் மட்டுமே மசோதாவின் பிரிவுகள் குறித்து தலைமை வழக்கறிஞர் வழிகாட்டும் சட்டக் கருத்தை வழங்க முடியும்.",
        "Incorrect. The Advocate General has no decision-making power over legislative classification of bills.", "தவறு. மசோதாக்களை வகைப்படுத்துவதில் தலைமை வழக்கறிஞருக்கு எந்த முடிவெடுக்கும் அதிகாரமும் இல்லை.",
        "Correct. Under Article 199(3), the Speaker's decision is final; AG's role is purely advisory upon request.", "சரி. உறுப்பு 199(3)-ன் கீழ் சபாநாயகரின் முடிவே இறுதியானது; AG-யின் பங்கு கோரப்படும் போது ஆலோசனை வழங்குவது மட்டுமே.",
        "Incorrect. High Court does not decide Money Bill classification during legislative passage.", "தவறு. சட்டமன்றத்தில் நிறைவேறும் போது உயர் நீதிமன்றம் நிதி மசோதாவை வகைப்படுத்துவதில்லை.",
        "Incorrect. Finance Minister introduces the budget but does not possess constitutional certification power.", "தவறு. நிதி அமைச்சர் பட்ஜெட்டை அறிமுகப்படுத்துகிறார், ஆனால் அரசியலமைப்பு சான்றளிக்கும் அதிகாரம் கொண்டிருக்கவில்லை.",
        "Parallel provision at the Centre: Article 110(3) — Speaker of Lok Sabha decides finally.",
        "மத்தியில் இணையான விதி: உறுப்பு 110(3) — மக்களவை சபாநாயகரின் முடிவே இறுதியானது.",
        "Judicial review of Speaker's certification of Money Bills has been examined by Constitution Benches in Aadhaar case and Roger Mathew case.",
        "நிதி மசோதாக்கள் குறித்த சபாநாயகரின் சான்றளிப்பு மீதான நீதித்துறை மறுஆய்வு ஆதார் மற்றும் ரோஜர் மேத்யூ வழக்குகளில் அரசியலமைப்பு அமர்வுகளால் ஆராயப்பட்டது."
    )

    # Q23 (C)
    add_q(
        "ADVG_M_023", "Remuneration Components",
        "How is the financial compensation of the Advocate General typically structured by the State Government under executive rules?",
        "நிர்வாக விதிகளின் கீழ் மாநில அரசால் தலைமை வழக்கறிஞரின் நிதியீட்டு இழப்பீடு பொதுவாக எவ்வாறு கட்டமைக்கப்படுகிறது?",
        "A flat monthly salary equal to that of a Supreme Court Judge without any hearing fees", "எந்தவொரு வாதாட்டக் கட்டணமும் இன்றி உச்ச நீதிமன்ற நீதிபதிக்கு சமமான நிலையான மாதச் சம்பளம்",
        "A percentage share of the court fees collected by the High Court", "உயர் நீதிமன்றத்தால் வசூலிக்கப்படும் நீதிமன்றக் கட்டணத்தின் ஒரு குறிப்பிட்ட சதவீதப் பங்கு",
        "A monthly retainer fee plus case appearance fees, drafting fees, and conference fees as prescribed by State Law Officers Rules", "மாநில சட்ட அதிகாரிகள் விதிகளில் பரிந்துரைக்கப்பட்ட மாதாந்திர தக்கவைப்புக் கட்டணம் (Retainer fee) மற்றும் வழக்கு வாதாட்டக் கட்டணம், வரைவுக் கட்டணம் மற்றும் ஆலோசனைக் கட்டணங்கள்",
        "Daily wages based on the state minimum wage act", "மாநில குறைந்தபட்ச ஊதியச் சட்டத்தின் அடிப்படையிலான தினசரி கூலி",
        "C",
        "Unlike judges who receive a fixed consolidated salary, the Advocate General's remuneration under Article 165(3) is regulated by State Law Officers Rules. It typically consists of a monthly retainer fee for advisory work plus scheduled appearance fees for hearings in the High Court, Supreme Court, or tribunals.",
        "நிலையான சம்பளத்தைப் பெறும் நீதிபதிகளைப் போலன்றி, உறுப்பு 165(3)-ன் கீழ் தலைமை வழக்கறிஞரின் ஊதியம் மாநில சட்ட அதிகாரிகள் விதிகளால் ஒழுங்குபடுத்தப்படுகிறது. இது பொதுவாக ஆலோசனைப் பணிகளுக்கான மாதாந்திர தக்கவைப்புக் கட்டணம் மற்றும் உயர் நீதிமன்றம், உச்ச நீதிமன்றம் அல்லது தீர்ப்பாயங்களில் ஆஜராவதற்கான வழக்காட்டக் கட்டணங்களைக் கொண்டுள்ளது.",
        "Incorrect. Not a fixed judicial salary equal to SC judges.", "தவறு. உச்ச நீதிமன்ற நீதிபதிகளுக்கு இணையான நிலையான நீதித்துறை சம்பளம் அல்ல.",
        "Incorrect. Court fees go to the State exchequer, not to law officers.", "தவறு. நீதிமன்றக் கட்டணம் அரசு கருவூலத்திற்கு செல்கிறது, சட்ட அதிகாரிகளுக்கு அல்ல.",
        "Correct. Structured as monthly retainer fee plus scheduled appearance, drafting, and consultation fees.", "சரி. மாதாந்திர தக்கவைப்புக் கட்டணம் மற்றும் வாதாடல், வரைவு மற்றும் ஆலோசனைக் கட்டணங்களாக கட்டமைக்கப்பட்டுள்ளது.",
        "Incorrect. Minimum wage legislation does not apply to constitutional law officers.", "தவறு. குறைந்தபட்ச ஊதியச் சட்டம் அரசியலமைப்பு சட்ட அதிகாரிகளுக்குப் பொருந்தாது.",
        "The retainer covers routine advice to administrative departments.",
        "தக்கவைப்புக் கட்டணம் நிர்வாகத் துறைகளுக்கான வழக்கமான ஆலோசனைகளை உள்ளடக்கியது.",
        "Separate scheduled fees are billed for appearances in outstation courts or the Supreme Court.",
        "வெளிவட்டார நீதிமன்றங்கள் அல்லது உச்ச நீதிமன்றத்தில் ஆஜராவதற்கு தனித்தனியாக நிர்ணயிக்கப்பட்ட கட்டணங்கள் பெறப்படுகின்றன."
    )

    # Q24 (D)
    add_q(
        "ADVG_M_024", "Special Public Prosecutor Consultation",
        "Under Section 24(8) of the Code of Criminal Procedure, 1973 (and corresponding Section 18(8) BNSS), what is the role of the Advocate General when the State Government appoints a Special Public Prosecutor for a sensitive trial?",
        "குற்றவியல் நடைமுறைச் சட்டம் 1973 பிரிவு 24(8)-ன் கீழ் (மற்றும் BNSS பிரிவு 18(8)), ஒரு முக்கிய வழக்கில் சிறப்பு அரசு வழக்கறிஞரை (Special Public Prosecutor) அரசு நியமிக்கும் போது தலைமை வழக்கறிஞரின் பங்கு என்ன?",
        "The Advocate General must personally conduct the trial as the sole prosecutor", "தலைமை வழக்கறிஞரே ஒரே வழக்கறிஞராக தனிப்பட்ட முறையில் விசாரணையை நடத்த வேண்டும்",
        "The Advocate General has the sole constitutional authority to issue the appointment order without the Government", "அரசு இன்றி நியமன ஆணையை வெளியிடும் ஒரே அரசியலமைப்பு அதிகாரம் தலைமை வழக்கறிஞருக்கு மட்டுமே உண்டு",
        "He is barred from having any knowledge of criminal prosecution appointments", "குற்றவியல் அரசு வழக்கறிஞர் நியமனங்கள் குறித்து எந்த தகவலும் தெரிந்து கொள்வதிலிருந்து அவர் தடுக்கப்பட்டுள்ளார்",
        "The State Government frequently consults the Advocate General to assess the competence of candidate advocates and determine fee structures", "பொருத்தமான வழக்கறிஞர்களின் தகுதியை மதிப்பிடவும் கட்டணக் கட்டமைப்பைத் தீர்மானிக்கவும் மாநில அரசு தலைமை வழக்கறிஞரைக் கலந்தாலோசிக்கிறது",
        "D",
        "When appointing a Special Public Prosecutor (SPP) under Section 24(8) CrPC (minimum 10 years practice), the State Government often seeks the recommendation or concurrence of the Advocate General to ensure that an advocate of high caliber and integrity is entrusted with the prosecution.",
        "குற்றவியல் நடைமுறைச் சட்டம் பிரிவு 24(8)-ன் கீழ் (குறைந்தபட்சம் 10 ஆண்டுகள் வழக்கறிஞர் பணி) ஒரு சிறப்பு அரசு வழக்கறிஞரை நியமிக்கும் போது, உயர் திறமையும் நாணயமும் கொண்ட வழக்கறிஞரிடம் விசாரணை ஒப்படைக்கப்படுவதை உறுதி செய்ய மாநில அரசு தலைமை வழக்கறிஞரின் பரிந்துரையை அல்லது ஒப்புதலைப் பெறுகிறது.",
        "Incorrect. The AG does not personally conduct every subordinate court criminal trial.", "தவறு. ஒவ்வொரு கீழ்மை நீதிமன்ற குற்றவியல் விசாரணையையும் AG தனிப்பட்ட முறையில் நடத்துவதில்லை.",
        "Incorrect. The appointment is an executive order issued by the Home/Law Department.", "தவறு. இந்நியமனம் உள்துறை/சட்டத்துறையால் வெளியிடப்படும் ஒரு நிர்வாக உத்தரவாகும்.",
        "Incorrect. The AG is the chief legal officer and frequently advises on prosecution policies.", "தவறு. AG தலைமை சட்ட அதிகாரி என்பதால் அரசுத் தரப்பு கொள்கைகள் குறித்து அடிக்கடி ஆலோசனை வழங்குகிறார்.",
        "Correct. The State Government consults the Advocate General regarding candidate competence and fees.", "சரி. வேட்பாளர்களின் தகுதி மற்றும் கட்டணம் குறித்து மாநில அரசு தலைமை வழக்கறிஞரைக் கலந்தாலோசிக்கிறது.",
        "An SPP is engaged in cases of grave public importance, such as major financial frauds, communal violence, or high-profile homicides.",
        "பெரிய நிதி மோசடிகள், வகுப்புவாத வன்முறைகள் அல்லது முக்கிய கொலை வழக்குகள் போன்ற தீவிர பொது முக்கியத்துவம் வாய்ந்த வழக்குகளில் SPP ஈடுபடுத்தப்படுகிறார்.",
        "Section 24(8) requires at least 10 years of practice as an advocate for eligibility as an SPP.",
        "பிரிவு 24(8) SPP-யாக நியமிக்கப்பட வழக்கறிஞராக குறைந்தபட்சம் 10 ஆண்டுகள் பயிற்சி பெற்றிருக்க வேண்டும் என்று கோருகிறது."
    )

    # Q25 (A)
    add_q(
        "ADVG_M_025", "Right of Pre-audience Meaning",
        "What is the precise legal effect of having the 'Right of Pre-audience' under Section 23 of the Advocates Act, 1961?",
        "வழக்கறிஞர்கள் சட்டம் 1961-ன் பிரிவு 23-ன் கீழ் 'முன்னுரிமை பெற்று வாதாடும் உரிமை' (Right of Pre-audience) கொண்டிருப்பதன் துல்லியமான சட்டப்பூர்வ விளைவு என்ன?",
        "The right to be heard before other advocates on the cause list when multiple counsel appear in court", "நீதிமன்றத்தில் பல வழக்கறிஞர்கள் தோன்றும் போது வழக்குப் பட்டியலில் மற்ற வழக்கறிஞர்களுக்கு முன்பாக வாதாடக் கேட்கப்படும் உரிமை",
        "The right to dictate the final judgment to the presiding judge", "வழக்கை விசாரிக்கும் நீதிபதிக்கு இறுதித் தீர்ப்பை ஆணையிடும் உரிமை",
        "The right to cross-examine witnesses before the magistrate can speak", "நடுவர் பேசுவதற்கு முன்பாகவே சாட்சிகளை குறுக்கு விசாரணை செய்யும் உரிமை",
        "The right to grant bail directly to an accused without judicial intervention", "நீதிமன்ற தலையீடின்றி குற்றவாளிக்கு நேரடியாக ஜாமீன் வழங்கும் உரிமை",
        "A",
        "The 'Right of Pre-audience' is a procedural seniority right under Section 23 of the Advocates Act, 1961. It confers upon the law officer the privilege of being called upon and heard by the court before other advocates when matters are called for hearing.",
        "'முன்னுரிமை பெற்று வாதாடும் உரிமை' என்பது வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 23-ன் கீழ் உள்ள ஒரு நடைமுறை மூப்பு உரிமையாகும். வழக்குகள் விசாரணைக்கு அழைக்கப்படும் போது மற்ற வழக்கறிஞர்களுக்கு முன்பாக நீதிமன்றத்தால் அழைக்கப்பட்டு வாதாடுவதற்கான சலுகையை இது சட்ட அதிகாரிக்கு வழங்குகிறது.",
        "Correct. It is the right to be heard before other advocates on the cause list.", "சரி. வழக்குப் பட்டியலில் உள்ள மற்ற வழக்கறிஞர்களுக்கு முன்பாக தனது வாதத்தை முன்வைக்கும் உரிமையாகும்.",
        "Incorrect. Judges decide cases independently; advocates cannot dictate judgments.", "தவறு. நீதிபதிகள் வழக்குகளை சுதந்திரமாக தீர்மானிக்கின்றனர்; வழக்கறிஞர்கள் தீர்ப்புகளை ஆணையிட முடியாது.",
        "Incorrect. Procedure for examining witnesses is governed by Evidence Act / BSA and court control.", "தவறு. சாட்சிகளை விசாரிக்கும் நடைமுறை சாட்சியச் சட்டம் மற்றும் நீதிமன்றக் கட்டுப்பாட்டிற்கு உட்பட்டது.",
        "Incorrect. Bail is an exclusive judicial power of courts.", "தவறு. ஜாமீன் வழங்குவது நீதிமன்றங்களின் பிரத்தியேக நீதித்துறை அதிகாரமாகும்.",
        "Pre-audience reflects the court's institutional respect for the sovereign state's chief law officer.",
        "முன்னுரிமை என்பது இறையாண்மை கொண்ட அரசின் தலைமை சட்ட அதிகாரிக்கு நீதிமன்றம் அளிக்கும் நிறுவன ரீதியான மரியாதையை பிரதிபலிக்கிறது.",
        "In practical terms, it allows urgent government mentions to be addressed first during motion hearings.",
        "நடைமுறை ரீதியாக, அவசர அரசாங்க விவகாரங்களை நீதிமன்ற விசாரணைகளின் போது முதலில் முறையிட இது அனுமதிக்கிறது."
    )

    # Q26 (B)
    add_q(
        "ADVG_M_026", "Subordinate Legislation Scrutiny",
        "What is the Advocate General's role regarding subordinate legislation (rules, regulations, statutory notifications) framed by State Government departments?",
        "மாநில அரசுத் துறைகளால் உருவாக்கப்படும் துணைச் சட்டங்கள் (விதிகள், ஒழுங்குமுறைகள், சட்டப்பூர்வ அறிவிப்புகள்) தொடர்பாக தலைமை வழக்கறிஞரின் பங்கு என்ன?",
        "Subordinate rules automatically become void unless signed personally by the Advocate General", "தலைமை வழக்கறிஞர் தனிப்பட்ட முறையில் கையொப்பமிடாத வரை துணை விதிகள் தானாகவே செல்லாததாகிவிடும்",
        "He is consulted to examine whether the proposed rules exceed the rule-making power conferred by the parent Act (ultra vires) or violate constitutional provisions", "முன்மொழியப்பட்ட விதிகள் மூலச் சட்டம் வழங்கிய அதிகாரத்தை மீறுகின்றனவா (Ultra vires) அல்லது அரசியலமைப்பு விதிகளை மீறுகின்றனவா என்பதை ஆராய அவர் கலந்தாலோசிக்கப்படுகிறார்",
        "The Advocate General enacts all departmental regulations without legislative oversight", "சட்டமன்ற மேற்பார்வையின்றி அனைத்து துறைசார் ஒழுங்குமுறைகளையும் தலைமை வழக்கறிஞரே இயற்றுகிறார்",
        "He has no constitutional or advisory connection with statutory rules", "சட்டப்பூர்வ விதிகளுடன் அவருக்கு எந்தவொரு அரசியலமைப்பு அல்லது ஆலோசனை தொடர்பும் இல்லை",
        "B",
        "Under Article 165(2), departments refer complex draft rules to the Advocate General to ensure that the subordinate legislation is intra vires the parent statute, satisfies the test of reasonable classification under Article 14, and does not suffer from excessive delegation.",
        "உறுப்பு 165(2)-ன் கீழ், சிக்கலான வரைவு விதிகள் மூலச் சட்டத்தின் அதிகார வரம்பிற்குள் (Intra vires) உள்ளனவா, உறுப்பு 14-ன் கீழ் நியாயமான வகைப்பாட்டுத் தேர்வை பூர்த்தி செய்கின்றனவா மற்றும் அதிகப்படியான அதிகாரப் பகிர்வால் பாதிக்கப்படவில்லை என்பதை உறுதிப்படுத்த துறைகள் தலைமை வழக்கறிஞரிடம் ஆலோசிக்கின்றன.",
        "Incorrect. Rules are signed by Departmental Secretaries and published in the Gazette, not signed by AG.", "தவறு. விதிகள் துறைச் செயலாளர்களால் கையொப்பமிடப்பட்டு அரசிதழில் வெளியிடப்படுகின்றன, AG கையொப்பமிடுவதில்லை.",
        "Correct. Consulted to ensure rules are not ultra vires the parent Act or Constitution.", "சரி. விதிகள் மூலச் சட்டத்திற்கோ அல்லது அரசியலமைப்பிற்கோ முரணாக இல்லை என்பதை உறுதி செய்ய அவர் கலந்தாலோசிக்கப்படுகிறார்.",
        "Incorrect. Executive rules cannot be enacted directly by law officers.", "தவறு. சட்ட அதிகாரிகளால் நேரடியாக நிர்வாக விதிகளை இயற்ற முடியாது.",
        "Incorrect. Advisory role on statutory rules is a core function under Article 165(2).", "தவறு. சட்டப்பூர்வ விதிகள் மீதான ஆலோசனைப் பணி உறுப்பு 165(2)-ன் கீழ் ஒரு முதன்மைப் பணியாகும்.",
        "Subordinate legislation must strictly conform to the parent enabling statute.",
        "துணைச் சட்டங்கள் மூல அதிகாரச் சட்டத்திற்கு கண்டிப்பாக இணங்க வேண்டும்.",
        "A rule declared ultra vires by the High Court can lead to the invalidation of major administrative actions.",
        "உயர் நீதிமன்றத்தால் ஒரு விதி அதிகார வரம்பை மீறியதாக (ultra vires) அறிவிக்கப்பட்டால், அது முக்கிய நிர்வாக நடவடிக்கைகளை செல்லாததாக்க வழிவகுக்கும்."
    )

    # Q27 (C)
    add_q(
        "ADVG_M_027", "Article 165 vs Article 76 Textual Differences",
        "Which of the following is a textual difference between Article 76 (Attorney General) and Article 165 (Advocate General)?",
        "உறுப்பு 76 (அட்டர்னி ஜெனரல்) மற்றும் உறுப்பு 165 (அட்வகேட் ஜெனரல்) ஆகியவற்றுக்கு இடையேயான உரைக் கட்டமைப்பு வேறுபாடு பின்வருவனவற்றில் எது?",
        "Article 76 mentions Governor, while Article 165 mentions President", "உறுப்பு 76 ஆளுநரைக் குறிப்பிடுகிறது, உறுப்பு 165 குடியரசுத் தலைவரைக் குறிப்பிடுகிறது",
        "Article 165 contains 5 clauses, whereas Article 76 contains only 2 clauses", "உறுப்பு 165-ல் 5 பிரிவுகள் உள்ளன, ஆனால் உறுப்பு 76-ல் 2 பிரிவுகள் மட்டுமே உள்ளன",
        "Article 76 explicitly includes Clause (3) conferring right of audience in all courts throughout India; Article 165 does NOT contain a corresponding audience clause in its constitutional text", "உறுப்பு 76(3) இந்தியா முழுவதும் உள்ள அனைத்து நீதிமன்றங்களிலும் வாதாடும் உரிமையை வெளிப்படையாகக் கொண்டுள்ளது; ஆனால் உறுப்பு 165-ன் அரசியலமைப்பு உரையில் அத்தகைய வாதாடும் உரிமைப் பிரிவு இல்லை",
        "Article 76 prescribes a fixed 6-year tenure, while Article 165 prescribes a 3-year tenure", "உறுப்பு 76 நிலையான 6 ஆண்டு பதவிக்காலத்தை நிர்ணயிக்கிறது, உறுப்பு 165 3 ஆண்டு பதவிக்காலத்தை நிர்ணயிக்கிறது",
        "C",
        "Article 76 contains four clauses, including Clause (3): 'In the performance of his duties the Attorney-General shall have right of audience in all courts in the territory of India'. In contrast, Article 165 contains only three clauses and lacks an express right of audience clause; the Advocate General's right of audience within the State derives from common law, procedural statutes (CPC/CrPC), and Section 23 of the Advocates Act, 1961.",
        "உறுப்பு 76 நான்கு பிரிவுகளைக் கொண்டுள்ளது, அதில் பிரிவு (3): 'தனது பணிகளை ஆற்றுவதில் அட்டர்னி ஜெனரல் இந்தியா முழுவதும் உள்ள அனைத்து நீதிமன்றங்களிலும் வாதாடும் உரிமை கொண்டிருப்பார்' என்று கூறுகிறது. மாறாக, உறுப்பு 165 மூன்று பிரிவுகளை மட்டுமே கொண்டுள்ளது மற்றும் வெளிப்படையான வாதாடும் உரிமைப் பிரிவைக் கொண்டிருக்கவில்லை; அட்வகேட் ஜெனரலின் வாதாடும் உரிமை பொதுச் சட்டம், நடைமுறைச் சட்டங்கள் (CPC/CrPC) மற்றும் வழக்கறிஞர்கள் சட்டம் 1961-ன் பிரிவு 23 ஆகியவற்றிலிருந்து பெறப்படுகிறது.",
        "Incorrect. Article 76 mentions President; Article 165 mentions Governor.", "தவறு. உறுப்பு 76 குடியரசுத் தலைவரையும், உறுப்பு 165 ஆளுநரையும் குறிப்பிடுகிறது.",
        "Incorrect. Article 76 has 4 clauses; Article 165 has 3 clauses.", "தவறு. உறுப்பு 76-ல் 4 பிரிவுகளும், உறுப்பு 165-ல் 3 பிரிவுகளும் உள்ளன.",
        "Correct. Art 76(3) explicitly grants right of audience throughout India; Article 165 has no explicit audience clause in its constitutional text.", "சரி. உறுப்பு 76(3) இந்தியா முழுவதும் வாதாடும் உரிமையை வெளிப்படையாகக் கூறுகிறது; உறுப்பு 165-ல் அத்தகைய பிரிவு இல்லை.",
        "Incorrect. Neither article prescribes a fixed tenure; both hold office during pleasure.", "தவறு. எந்தவொரு உறுப்பும் நிலையான பதவிக்காலத்தை நிர்ணயிக்கவில்லை; இருவருமே விருப்பக் கோட்பாட்டின் கீழ் பதவி வகிக்கின்றனர்.",
        "This subtle textual difference is a favorite question in advanced constitutional law examinations.",
        "இந்த நுட்பமான உரை வேறுபாடு உயர்நிலை அரசியலமைப்புச் சட்டத் தேர்வுகளில் கேட்கப்படும் ஒரு விருப்பமான கேள்வியாகும்.",
        "The Advocate General's right of audience is statutory under Advocates Act Sec 23, whereas AGI's right of audience is constitutional under Art 76(3).",
        "அட்வகேட் ஜெனரலின் வாதாடும் உரிமை வழக்கறிஞர்கள் சட்டம் பிரிவு 23-ன் கீழ் சட்டப்பூர்வமானது, ஆனால் அட்டர்னி ஜெனரலின் வாதாடும் உரிமை உறுப்பு 76(3)-ன் கீழ் அரசியலமைப்பு ரீதியானது."
    )

    # Q28 (D)
    add_q(
        "ADVG_M_028", "Disqualification from Voting Rationale",
        "What is the constitutional rationale for granting the Advocate General the right to speak in the State Legislature under Article 177 while strictly prohibiting him from voting?",
        "உறுப்பு 177-ன் கீழ் தலைமை வழக்கறிஞருக்கு சட்டமன்றத்தில் பேசும் உரிமையை வழங்கி, அதே நேரத்தில் வாக்களிப்பதை கண்டிப்பாக தடை செய்வதற்கான அரசியலமைப்பு நோக்கம் என்ன?",
        "To punish the law officer for not being an elected politician", "தேர்ந்தெடுக்கப்பட்ட அரசியல்வாதியாக இல்லாததற்காக சட்ட அதிகாரியை தண்டிப்பது",
        "Because the Speaker exercises all voting rights on behalf of the Advocate General", "சபாநாயகர் தலைமை வழக்கறிஞரின் சார்பில் அனைத்து வாக்குரிமைகளையும் பயன்படுத்துவதால்",
        "Because the Advocate General votes in the High Court instead", "தலைமை வழக்கறிஞர் அதற்குப் பதிலாக உயர் நீதிமன்றத்தில் வாக்களிப்பதால்",
        "To enable the Legislature to benefit from expert legal guidance on bills while preserving the democratic principle that only elected representatives can enact laws", "மசோதாக்கள் மீது நிபுணத்துவ சட்ட வழிகாட்டுதலை சட்டமன்றம் பெற உதவுவதோடு, மக்களால் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகள் மட்டுமே சட்டங்களை இயற்ற முடியும் என்ற ஜனநாயகக் கோட்பாட்டைப் பாதுகாப்பது",
        "D",
        "The design of Article 177 balances expert legal assistance with democratic legitimacy. The Advocate General's presence allows the House to clarify complex constitutional points, but voting is preserved exclusively for elected representatives accountable to the electorate.",
        "உறுப்பு 177-ன் கட்டமைப்பு நிபுணத்துவ சட்ட உதவியை ஜனநாயக சட்டபூர்வ தன்மையோடு சமநிலைப்படுத்துகிறது. தலைமை வழக்கறிஞரின் இருப்பு சிக்கலான அரசியலமைப்பு விவகாரங்களை அவை தெளிவுபடுத்த உதவுகிறது, ஆனால் வாக்களிப்பது வாக்காளர்களுக்குப் பொறுப்பான தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளுக்கு மட்டுமே ஒதுக்கப்பட்டுள்ளது.",
        "Incorrect. It is a functional privilege, not a punitive measure.", "தவறு. இது ஒரு செயல்பாட்டுச் சலுகை, தண்டனை நடவடிக்கை அல்ல.",
        "Incorrect. Speaker cannot vote on behalf of anyone else.", "தவறு. சபாநாயகர் மற்றவர்கள் சார்பில் வாக்களிக்க முடியாது.",
        "Incorrect. High Court is a judicial court, not a voting forum for law officers.", "தவறு. உயர் நீதிமன்றம் ஒரு நீதித்துறை மன்றம், சட்ட அதிகாரிகளுக்கான வாக்கெடுப்பு தளம் அல்ல.",
        "Correct. Preserves democratic legitimacy (only elected members vote) while securing expert legal input on legislation.", "சரி. சட்டங்கள் மீது நிபுணத்துவ சட்ட ஆலோசனையைப் பெறும் அதே வேளையில், தேர்ந்தெடுக்கப்பட்டவர்கள் மட்டுமே வாக்களிக்க முடியும் என்ற ஜனநாயக மாண்பையும் பாதுகாக்கிறது.",
        "This principle applies identically to the Attorney General in Parliament under Article 88.",
        "இக்கோட்பாடு உறுப்பு 88-ன் கீழ் நாடாளுமன்றத்தில் அட்டர்னி ஜெனரலுக்கும் முற்றிலும் ஒரே மாதிரியாகப் பொருந்தும்.",
        "It prevents unelected appointees from deciding political outcomes in the legislative chamber.",
        "தேர்ந்தெடுக்கப்படாத நியமனப் பொறுப்பாளர்கள் சட்டமன்ற அவையில் அரசியல் முடிவுகளைத் தீர்மானிப்பதை இது தடுக்கிறது."
    )

    # Q29 (A)
    add_q(
        "ADVG_M_029", "Inter-State Dispute Article 131",
        "When an original suit is filed by one State against another State or against the Union of India under Article 131 of the Constitution, who typically signs and verifies the pleadings and represents the plaintiff State?",
        "அரசியலமைப்பின் உறுப்பு 131-ன் கீழ் ஒரு மாநிலம் மற்றொரு மாநிலத்திற்கு எதிராகவோ அல்லது இந்திய ஒன்றியத்திற்கு எதிராகவோ அசல் வழக்கைத் தாக்கல் செய்யும் போது, வாதங்களைச் சரிபார்த்து வாதி மாநிலத்தைப் பிரதிநிதித்துவப்படுத்துபவர் யார்?",
        "The Advocate General of the State, assisted by the Advocate-on-Record in the Supreme Court", "உச்ச நீதிமன்றத்தில் பதிவுபெற்ற வழக்கறிஞரின் (AoR) உதவியுடன் மாநில தலைமை வழக்கறிஞர்",
        "The Governor in his personal capacity", "தனிப்பட்ட முறையில் ஆளுநர்",
        "The Chief Justice of the State High Court", "மாநில உயர் நீதிமன்ற தலைமை நீதிபதி",
        "The Director General of Police", "காவல்துறை தலைமை இயக்குநர்",
        "A",
        "Article 131 confers exclusive original jurisdiction on the Supreme Court in inter-governmental disputes. The Advocate General leads the legal team, settles the plaint, and argues the case for the State, while procedural filings are made through an Advocate-on-Record (AoR).",
        "உறுப்பு 131 அரசுகளுக்கு இடையேயான தாவாக்களில் உச்ச நீதிமன்றத்திற்கு பிரத்தியேக அசல் அதிகார வரம்பை வழங்குகிறது. தலைமை வழக்கறிஞர் சட்டக் குழுவிற்கு தலைமை தாங்குகிறார், வழக்குப் புகாரை இறுதி செய்கிறார் மற்றும் மாநிலத்திற்காக வாதாடுகிறார்; அதே நேரத்தில் நடைமுறைத் தாக்கல்கள் AoR மூலம் செய்யப்படுகின்றன.",
        "Correct. The Advocate General leads the State legal representation in Article 131 original suits.", "சரி. உறுப்பு 131 அசல் வழக்குகளில் தலைமை வழக்கறிஞரே மாநில சட்டப் பிரதிநிதித்துவத்தை வழிநடத்துகிறார்.",
        "Incorrect. The Governor enjoys constitutional immunity under Article 361 and does not sign pleadings.", "தவறு. ஆளுநர் உறுப்பு 361-ன் கீழ் அரசியலமைப்பு பாதுகாப்பு பெறுகிறார், அவர் மனுக்களில் கையொப்பமிடுவதில்லை.",
        "Incorrect. The High Court Chief Justice is a judge, not a litigant or advocate.", "தவறு. உயர் நீதிமன்ற தலைமை நீதிபதி ஒரு நீதிபதி, வழக்காடியோ அல்லது வழக்கறிஞரோ அல்ல.",
        "Incorrect. DGP handles police administration, not inter-state constitutional litigation.", "தவறு. டிஜிபி காவல் நிர்வாகத்தைக் கையாள்கிறார், மாநிலங்களுக்கு இடையேயான அரசியலமைப்பு வழக்குகளை அல்ல.",
        "Examples of Article 131 suits: Tamil Nadu challenging Kerala over the Mullaperiyar Dam issue, or States challenging Central laws like CAA.",
        "உறுப்பு 131 வழக்குகளுக்கான எடுத்துக்காட்டுகள்: முல்லைப் பெரியாறு விவகாரத்தில் கேரளாவுக்கு எதிராக தமிழ்நாடு தொடர்ந்த வழக்கு அல்லது CAA போன்ற மத்திய சட்டங்களை எதிர்த்து மாநிலங்கள் தொடர்ந்த வழக்குகள்.",
        "Pleadings are brought in the name of the State (e.g., 'State of Tamil Nadu v. Union of India').",
        "வழக்கு வாதங்கள் மாநிலத்தின் பெயரிலேயே கொண்டு வரப்படுகின்றன (எ.கா. 'தமிழ்நாடு அரசு எதிர் இந்திய ஒன்றியம்')."
    )

    # Q30 (B)
    add_q(
        "ADVG_M_030", "Tenure and Pleasure Judicial Review",
        "Can a decision of the Governor terminating the appointment of an Advocate General under the pleasure doctrine be subjected to judicial review?",
        "விருப்பக் கோட்பாட்டின் கீழ் தலைமை வழக்கறிஞரின் நியமனத்தை முடிவுக்குக் கொண்டுவரும் ஆளுநரின் முடிவு நீதித்துறை மறுஆய்வுக்கு உட்படக் கூடியதா?",
        "No, the pleasure of the Governor is completely outside the scope of judicial scrutiny under all circumstances", "இல்லை, ஆளுநரின் விருப்பம் என்பது எச்சூழலிலும் நீதித்துறை பரிசீலனைக்கு முற்றிலும் அப்பாற்பட்டது",
        "Yes, on extremely limited grounds such as mala fides, arbitrariness, or violation of fundamental constitutional principles", "ஆம், உள்நோக்கம் (mala fides), தன்னிச்சைத் தன்மை அல்லது அடிப்படை அரசியலமைப்பு கோட்பாடுகளை மீறுதல் போன்ற மிகக் குறைந்த காரணங்களின் அடிப்படையில் மட்டுமே",
        "Yes, automatically by the High Court within 7 days of removal", "ஆம், பதவிநீக்கம் செய்யப்பட்ட 7 நாட்களுக்குள் உயர் நீதிமன்றத்தால் தானாகவே மறுஆய்வு செய்யப்படும்",
        "Only if approved by the State Legislative Assembly by a two-thirds resolution", "சட்டமன்றப் பேரவை மூன்றில் இரண்டு பங்கு தீர்மானத்தால் அங்கீகரித்தால் மட்டுமே",
        "B",
        "In B.P. Singhal v. Union of India (2010), the Supreme Court ruled that while the doctrine of pleasure gives wide discretion to the executive, the power cannot be exercised arbitrarily, whimsically, or for extraneous reasons. Judicial review is available, though on very limited grounds of mala fides or patent arbitrariness.",
        "பி.பி. சிங்கால் எதிர் இந்திய ஒன்றியம் (2010) வழக்கில், விருப்பக் கோட்பாடு நிர்வாகத்திற்கு பரந்த அதிகாரத்தை அளித்தாலும், அந்த அதிகாரத்தை தன்னிச்சையாகவோ அல்லது தொடர்பில்லாத காரணங்களுக்காகவோ பயன்படுத்த முடியாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. உள்நோக்கம் அல்லது அப்பட்டமான தன்னிச்சைத் தன்மை போன்ற மிகக் குறைந்த காரணங்களின் அடிப்படையில் நீதித்துறை மறுஆய்வு சாத்தியமே.",
        "Incorrect. Pleasure doctrine is not completely immune from judicial review in modern public law.", "தவறு. நவீன பொதுச் சட்டத்தில் விருப்பக் கோட்பாடு நீதித்துறை மறுஆய்விலிருந்து முற்றிலும் விலக்களிக்கப்படவில்லை.",
        "Correct. Judicial review is permissible on limited grounds of mala fides, arbitrariness, or extraneous considerations.", "சரி. உள்நோக்கம், தன்னிச்சைத் தன்மை போன்ற மிகக் குறுகிய காரணங்களின் அடிப்படையில் நீதித்துறை மறுஆய்வு அனுமதிக்கப்படுகிறது.",
        "Incorrect. There is no automatic High Court review process.", "தவறு. தானியங்கி உயர் நீதிமன்ற மறுஆய்வு நடைமுறை என்று எதுவும் இல்லை.",
        "Incorrect. Legislative resolution is not required to invoke judicial review under Article 226.", "தவறு. உறுப்பு 226-ன் கீழ் நீதித்துறை மறுஆய்வைப் பெற சட்டமன்றத் தீர்மானம் தேவையில்லை.",
        "However, because the AG serves at pleasure, courts are extremely reluctant to interfere unless bad faith is proven.",
        "இருப்பினும், தலைமை வழக்கறிஞர் விருப்பத்தின் பேரில் பணியாற்றுவதால், கடுமையான உள்நோக்கம் நிரூபிக்கப்பட்டால் அன்றி நீதிமன்றங்கள் தலையிடுவதில்லை.",
        "The loss of confidence by the political executive is generally considered a valid ground for termination.",
        "அரசியல் நிர்வாகத்தின் நம்பிக்கையை இழப்பது என்பது பதவி முடிவுக்குக் கொண்டுவர பொதுவாக செல்லுபடியாகும் காரணமாகக் கருதப்படுகிறது."
    )

    # --- 31 to 40 ---
    # Q31 (C)
    add_q(
        "ADVG_M_031", "Bar on Conflicting Retainers",
        "Under the Bar Council of India Rules and State Law Officers Rules, if an Advocate General has advised a private party on a legal matter prior to his appointment, can he subsequently represent the State against that party in the same matter?",
        "இந்திய பார் கவுன்சில் விதிகள் மற்றும் மாநில சட்ட அதிகாரிகள் விதிகளின் கீழ், நியமனத்திற்கு முன்பு ஒரு விவகாரத்தில் தனியார் தரப்பினருக்கு ஆலோசனை வழங்கியிருந்தால், பின்னர் அதே விவகாரத்தில் அத்தரப்பினருக்கு எதிராக தலைமை வழக்கறிஞர் அரசைப் பிரதிநிதித்துவப்படுத்த முடியுமா?",
        "Yes, without any limitation, as government interest always takes precedence", "ஆம், எந்தக் கட்டுப்பாடும் இன்றி செய்யலாம், ஏனெனில் அரசு நலனுக்கே எப்போதும் முன்னுரிமை",
        "Yes, if the State Cabinet passes a waiver order", "ஆம், மாநில அமைச்சரவை விலக்கு ஆணை பிறப்பித்தால் செய்யலாம்",
        "No, professional ethics prohibit an advocate from appearing in any matter where he has previously advised or held brief for the opposing party", "முடியாது, தான் முன்னர் எதிர் தரப்பினருக்கு ஆலோசனை வழங்கிய அல்லது வாதாடிய எந்தவொரு விவகாரத்திலும் ஆஜராவதை தொழில்முறை நெறிமுறைகள் தடை செய்கின்றன",
        "Yes, provided he charges double the standard appearance fee", "ஆம், வழக்கமான வாதாட்டக் கட்டணத்தை விட இருமடங்கு கட்டணம் வசூலித்தால் செய்யலாம்",
        "C",
        "The Bar Council of India Rules (Standards of Professional Conduct and Etiquette) explicitly prohibit an advocate from accepting a brief or appearing in any matter in which he has advised or held a brief for the opposite side. An Advocate General must recuse himself in such matters, and an Additional Advocate General or Special Counsel will be briefed instead.",
        "இந்திய பார் கவுன்சில் விதிகள் (தொழில்முறை நடத்தை மற்றும் நெறிமுறைத் தரநிலைகள்) ஒரு வழக்கறிஞர் தான் முன்னர் எதிர் தரப்பிற்கு ஆலோசனை வழங்கிய அல்லது வாதாடிய எந்தவொரு விவகாரத்திலும் ஆஜராவதை வெளிப்படையாகத் தடை செய்கின்றன. அத்தகைய வழக்குகளில் தலைமை வழக்கறிஞர் விலகிக் கொள்ள வேண்டும்; அவருக்குப் பதிலாக கூடுதல் தலைமை வழக்கறிஞர் வழக்கை நடத்துவார்.",
        "Incorrect. Government interest does not supersede fundamental rules of professional legal ethics.", "தவறு. தொழில்முறை சட்ட நெறிமுறைகளின் அடிப்படை விதிகளை அரசு நலன் மீற முடியாது.",
        "Incorrect. Executive waiver cannot override Bar Council rules on conflict of interest.", "தவறு. நலன் முரண்பாடு குறித்த பார் கவுன்சில் விதிகளை நிர்வாக விலக்கு ரத்து செய்ய முடியாது.",
        "Correct. Prohibited from appearing where he previously advised or represented the opposing party.", "சரி. முன்னர் எதிர் தரப்பினருக்கு ஆலோசனை வழங்கிய வழக்குகளில் ஆஜராவது தொழில்முறை நெறிமுறைகளால் தடை செய்யப்பட்டுள்ளது.",
        "Incorrect. Fee adjustments have no bearing on ethical disqualification.", "தவறு. கட்டண மாற்றங்களுக்கும் நெறிமுறைத் தகுதியிழப்பிற்கும் எந்த தொடர்பும் இல்லை.",
        "Recusal preserves the integrity of the judicial process and prevents breach of client confidentiality.",
        "வழக்கிலிருந்து விலகுவது (Recusal) நீதித்துறை நடைமுறையின் நாணயத்தைப் பாதுகாக்கிறது மற்றும் வாடிக்கையாளர் ரகசியத்தன்மை மீறப்படுவதைத் தடுக்கிறது.",
        "In such cases, the Advocate General submits a formal note of recusal to the Law Department.",
        "அத்தகைய சூழ்நிலைகளில், தலைமை வழக்கறிஞர் சட்டத்துறைக்கு முறையான விலகல் குறிப்பைச் சமர்ப்பிக்கிறார்."
    )

    # Q32 (D)
    add_q(
        "ADVG_M_032", "Constitutional Validity Defence",
        "When a State enactment is challenged as unconstitutional before the High Court or Supreme Court, who is the principal constitutional officer tasked with defending its validity?",
        "ஒரு மாநில சட்டம் அரசியலமைப்பிற்கு முரணானது என்று உயர் நீதிமன்றத்திலோ அல்லது உச்ச நீதிமன்றத்திலோ சவால் செய்யப்படும் போது, அதன் செல்லுபடி தன்மையை ஆதரித்து வாதிடும் முதன்மை அரசியலமைப்பு அதிகாரி யார்?",
        "The Speaker of the State Legislative Assembly", "சட்டப் பேரவைத் தலைவர் (சபாநாயகர்)",
        "The Chief Justice of the High Court", "உயர் நீதிமன்ற தலைமை நீதிபதி",
        "The Chairman of the State Law Commission", "மாநில சட்ட ஆணையத்தின் தலைவர்",
        "The Advocate General of the State", "மாநில தலைமை வழக்கறிஞர்",
        "D",
        "Whenever the constitutional validity of a State statute or statutory rule is challenged under Article 226 or Article 32, notice is issued to the Advocate General under Order XXVII-A of the Code of Civil Procedure, 1908. The Advocate General defends the competence and constitutionality of the State Legislature's enactments.",
        "உறுப்பு 226 அல்லது உறுப்பு 32-ன் கீழ் மாநில சட்டம் அல்லது விதியின் செல்லுபடி தன்மை சவால் செய்யப்படும் போதெல்லாம், சிவில் நடைமுறைச் சட்டம் 1908-ன் கட்டளை XXVII-A-ன் கீழ் தலைமை வழக்கறிஞருக்கு அறிவிப்பு அனுப்பப்படுகிறது. மாநில சட்டமன்றத்தின் அதிகாரத்தையும் அரசியலமைப்பு செல்லுபடி தன்மையையும் தலைமை வழக்கறிஞரே பாதுகாக்கிறார்.",
        "Incorrect. The Speaker presides over the House and does not enter the court arena to defend statutes.", "தவறு. சபாநாயகர் அவைக்கு தலைமை தாங்குகிறார், சட்டங்களை ஆதரித்து வாதிட நீதிமன்றத்திற்கு வருவதில்லை.",
        "Incorrect. Chief Justice adjudicates the constitutional challenge as an impartial judge.", "தவறு. தலைமை நீதிபதி அரசியலமைப்பு வழக்கை நடுநிலையான நீதிபதியாக விசாரிக்கிறார்.",
        "Incorrect. Law Commission recommends legal reforms; it does not defend litigation in court.", "தவறு. சட்ட ஆணையம் சீர்திருத்தங்களைப் பரிந்துரைக்கிறது; நீதிமன்றத்தில் வழக்குகளை வாதிடுவதில்லை.",
        "Correct. The Advocate General is the primary constitutional officer who defends the validity of State laws.", "சரி. மாநில சட்டங்களின் செல்லுபடி தன்மையை ஆதரித்து வாதிடும் முதன்மை அரசியலமைப்பு அதிகாரி தலைமை வழக்கறிஞரே ஆவார்.",
        "Under Order XXVII-A Rule 1 CPC, the court cannot invalidate a State Act without giving notice to the Advocate General.",
        "CPC கட்டளை XXVII-A விதி 1-ன் கீழ், தலைமை வழக்கறிஞருக்கு நோட்டீஸ் அனுப்பாமல் நீதிமன்றம் ஒரு மாநில சட்டத்தை செல்லாததாக்க முடியாது.",
        "This gives the State Government full opportunity to substantiate the constitutional nexus and legislative competence.",
        "இது மாநில அரசுக்கு தனது சட்டமன்ற அதிகாரத்தையும் நியாயமான நோக்கத்தையும் நிரூபிக்க முழு வாய்ப்பளிக்கிறது."
    )

    # Q33 (A)
    add_q(
        "ADVG_M_033", "Order XXVII-A CPC Mandatory Notice",
        "Under Order XXVII-A of the Code of Civil Procedure, 1908, what is the mandatory requirement whenever the constitutional validity of a State Act is questioned in a court?",
        "சிவில் நடைமுறைச் சட்டம் 1908-ன் கட்டளை XXVII-A-ன் கீழ், ஒரு நீதிமன்றத்தில் மாநில சட்டத்தின் அரசியலமைப்பு செல்லுபடி தன்மை கேள்விக்குள்ளாக்கப்படும் போதெல்லாம் எது கட்டாயத் தேவையாகும்?",
        "The court must issue notice to the Advocate General of the State and allow him an opportunity to be heard", "நீதிமன்றம் மாநில தலைமை வழக்கறிஞருக்கு நோட்டீஸ் அனுப்பி, அவரது வாதத்தைக் கேட்க வாய்ப்பளிக்க வேண்டும்",
        "The court must dismiss the case immediately without hearing the petitioner", "மனுதாரரை விசாரிக்காமல் நீதிமன்றம் உடனடியாக வழக்கை தள்ளுபடி செய்ய வேண்டும்",
        "The State Legislature must immediately pass the bill again", "மாநில சட்டமன்றம் உடனடியாக அந்த மசோதாவை மீண்டும் நிறைவேற்ற வேண்டும்",
        "The Governor must suspend the High Court Bench", "ஆளுநர் உயர் நீதிமன்ற அமர்வை இடைநீக்கம் செய்ய வேண்டும்",
        "A",
        "Order XXVII-A Rule 1 of the CPC explicitly mandates that in any suit where a substantial question of law as to the interpretation of the Constitution is involved, if the question relates to a State law, the court shall issue notice to the Advocate General of the State, who may appear and take part in the proceedings.",
        "CPC கட்டளை XXVII-A விதி 1, அரசியலமைப்பு விளக்கம் தொடர்பான சட்ட வினா ஒரு மாநில சட்டத்தைப் பற்றியதாக இருந்தால், நீதிமன்றம் தலைமை வழக்கறிஞருக்கு நோட்டீஸ் அனுப்ப வேண்டும் என்றும், அவர் வழக்கில் தோன்றி பங்கேற்கலாம் என்றும் தெளிவாக ஆணையிடுகிறது.",
        "Correct. Mandatory notice must be issued to the Advocate General under Order XXVII-A CPC.", "சரி. CPC கட்டளை XXVII-A-ன் கீழ் தலைமை வழக்கறிஞருக்கு கட்டாய நோட்டீஸ் அனுப்பப்பட வேண்டும்.",
        "Incorrect. Judicial review requires hearing the petitioner on merits.", "தவறு. நீதித்துறை மறுஆய்வு மனுதாரரின் வாதங்களை விசாரிக்க வேண்டும் என்று கோருகிறது.",
        "Incorrect. Legislative re-passage is not a response to court notice.", "தவறு. நீதிமன்ற நோட்டீஸுக்கு சட்டமன்ற மறுநிறைவேற்றம் பதில் நடவடிக்கை அல்ல.",
        "Incorrect. The Governor has no constitutional power to suspend judicial benches.", "தவறு. நீதித்துறை அமர்வுகளை இடைநீக்கம் செய்ய ஆளுநருக்கு எந்த அதிகாரமும் இல்லை.",
        "Order XXVII-A Rule 1 ensures that the State's viewpoint is heard before any legislation is struck down.",
        "கட்டளை XXVII-A விதி 1, எந்தவொரு சட்டமும் ரத்து செய்யப்படுவதற்கு முன்பு மாநிலத்தின் வாதம் கேட்கப்படுவதை உறுதி செய்கிறது.",
        "For Central statutes, a similar mandatory notice is issued to the Attorney General of India.",
        "மத்திய சட்டங்களுக்கு, இதேபோன்ற கட்டாய நோட்டீஸ் இந்திய அட்டர்னி ஜெனரலுக்கு அனுப்பப்படுகிறது."
    )

    # Q34 (B)
    add_q(
        "ADVG_M_034", "Civil Litigation Representation Rule",
        "Under Order XXVII Rule 2 of the Code of Civil Procedure, 1908, who represents the Government of the State as its recognized agent in civil litigation?",
        "சிவில் நடைமுறைச் சட்டம் 1908 கட்டளை XXVII விதி 2-ன் கீழ், சிவில் வழக்குகளில் மாநில அரசின் அங்கீகரிக்கப்பட்ட முகவராக அரசைப் பிரதிநிதித்துவப்படுத்துபவர் யார்?",
        "Any registered voter of the State", "மாநிலத்தின் பதிவுபெற்ற எந்தவொரு வாக்காளரும்",
        "Persons authorized by the State Government, led by the Advocate General and Government Pleaders", "தலைமை வழக்கறிஞர் மற்றும் அரசு வழக்கறிஞர்கள் தலைமையில் மாநில அரசால் அதிகாரமளிக்கப்பட்ட நபர்கள்",
        "The Chief Justice of the High Court", "உயர் நீதிமன்ற தலைமை நீதிபதி",
        "The Leader of the Opposition in the Assembly", "சட்டமன்ற எதிர்க்கட்சித் தலைவர்",
        "B",
        "Order XXVII of the CPC deals with suits by or against the Government. Persons authorized by the State Government by general or special order (led by the Advocate General and appointed Government Pleaders) act as recognized agents to receive processes and conduct litigation on behalf of the State.",
        "சிவில் நடைமுறைச் சட்டத்தின் கட்டளை XXVII அரசுக்கு எதிரான அல்லது அரசால் தொடரப்படும் வழக்குகளைக் கையாள்கிறது. தலைமை வழக்கறிஞர் மற்றும் அரசு வழக்கறிஞர்கள் தலைமையில் பொது அல்லது சிறப்பு உத்தரவு மூலம் மாநில அரசால் அங்கீகரிக்கப்பட்ட நபர்களே அரசின் அங்கீகரிக்கப்பட்ட முகவர்களாகச் செயல்படுகின்றனர்.",
        "Incorrect. Private citizens cannot represent the sovereign State without statutory authority.", "தவறு. சட்டப்பூர்வ அதிகாரமின்றி சாதாரண குடிமக்கள் அரசைப் பிரதிநிதித்துவப்படுத்த முடியாது.",
        "Correct. The Advocate General and authorized Government Pleaders act as recognized agents for the State under Order XXVII CPC.", "சரி. CPC கட்டளை XXVII-ன் கீழ் தலைமை வழக்கறிஞர் மற்றும் அரசு வழக்கறிஞர்கள் அரசின் முகவர்களாக செயல்படுகின்றனர்.",
        "Incorrect. Judiciary is separate from executive representation.", "தவறு. நீதித்துறை நிர்வாகப் பிரதிநிதித்துவத்திலிருந்து தனித்தன்மை வாய்ந்தது.",
        "Incorrect. Opposition Leader has no role in representing the State Executive.", "தவறு. மாநில நிர்வாகத்தைப் பிரதிநிதித்துவப்படுத்துவதில் எதிர்க்கட்சித் தலைவருக்கு எந்தப் பங்கும் இல்லை.",
        "Under Order XXVII, the State is always sued in the name of the 'State of [Name]' as prescribed by Article 300.",
        "கட்டளை XXVII-ன் கீழ், உறுப்பு 300-ல் பரிந்துரைக்கப்பட்டவாறு அரசு எப்போதும் 'மாநிலத்தின் பெயர்' என்ற பெயரிலேயே வழக்கில் சேர்க்கப்படுகிறது.",
        "The Advocate General oversees the entire litigation machinery defending the State in civil courts.",
        "சிவில் நீதிமன்றங்களில் அரசைப் பாதுகாக்கும் முழுமையான வழக்கு நிர்வாகத்தை தலைமை வழக்கறிஞர் மேற்பார்வையிடுகிறார்."
    )

    # Q35 (C)
    add_q(
        "ADVG_M_035", "Subordinate Legislation Ultra Vires Grounds",
        "On which of the following grounds can the Advocate General advise the State Government that a draft departmental regulation is legally vulnerable before the High Court?",
        "பின்வரும் எந்த காரணங்களின் அடிப்படையில் ஒரு வரைவு ஒழுங்குமுறை உயர் நீதிமன்றத்தின் முன் சட்டப்பூர்வமாக செல்லாததாகக் கூடும் என்று தலைமை வழக்கறிஞர் மாநில அரசுக்கு ஆலோசனை வழங்க முடியும்?",
        "If the regulation is printed in black ink instead of blue ink", "ஒழுங்குமுறை நீல நிறத்திற்கு பதிலாக கருப்பு மையினால் அச்சிடப்பட்டிருந்தால்",
        "If the regulation has fewer than 10 clauses", "ஒழுங்குமுறையில் 10-க்கும் குறைவான பிரிவுகள் இருந்தால்",
        "If the regulation exceeds the statutory scope of the parent Act, violates fundamental rights, or is arbitrary under Article 14", "ஒழுங்குமுறை மூலச் சட்டத்தின் அதிகார வரம்பை மீறினால், அடிப்படை உரிமைகளை மீறினால் அல்லது உறுப்பு 14-ன் கீழ் தன்னிச்சையானதாக இருந்தால்",
        "If the regulation is introduced on a Monday", "ஒழுங்குமுறை திங்கட்கிழமை அறிமுகப்படுத்தப்பட்டால்",
        "C",
        "Subordinate legislation is judicially reviewable on well-established grounds: (1) lack of legislative competence; (2) violation of constitutional provisions (e.g., Articles 14, 19, 21); (3) being ultra vires the enabling parent Act; and (4) manifest arbitrariness. The Advocate General vets draft rules against these precise legal benchmarks.",
        "துணைச் சட்டங்கள் நன்கு நிறுவப்பட்ட காரணங்களின் அடிப்படையில் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை: (1) சட்டமன்ற அதிகாரமின்மை; (2) அரசியலமைப்பு விதிகளை (உறுப்புகள் 14, 19, 21) மீறுதல்; (3) மூலச் சட்டத்தின் வரம்பை மீறுதல் (ultra vires); மற்றும் (4) வெளிப்படையான தன்னிச்சைத் தன்மை. தலைமை வழக்கறிஞர் இந்த சட்ட அளவுகோல்களின்படியே வரைவு விதிகளை ஆய்வு செய்கிறார்.",
        "Incorrect. Printing ink color has no legal relevance.", "தவறு. அச்சிடும் மை நிறத்திற்கு எந்த சட்டப் பொருத்தமும் இல்லை.",
        "Incorrect. Clause count does not affect legality.", "தவறு. பிரிவுகளின் எண்ணிக்கை சட்டபூர்வ தன்மையை பாதிக்காது.",
        "Correct. Exceeding statutory scope (ultra vires), violating fundamental rights, or manifest arbitrariness are the standard legal grounds.", "சரி. மூலச் சட்ட வரம்பை மீறுதல், அடிப்படை உரிமைகளை மீறுதல் அல்லது வெளிப்படையான தன்னிச்சைத் தன்மை ஆகியவையே நிலையான சட்டக் காரணங்கள் ஆகும்.",
        "Incorrect. Day of introduction has no legal bearing.", "தவறு. அறிமுகப்படுத்தும் நாளுக்கு எந்த சட்டப் பொருத்தமும் இல்லை.",
        "In Cellular Operators Association v. TRAI (2016), the Supreme Court confirmed that subordinate rules can be struck down for manifest arbitrariness.",
        "செல்லுலார் ஆபரேட்டர்ஸ் வழக்கில் (2016), வெளிப்படையான தன்னிச்சைத் தன்மைக்காக துணை விதிகளையும் ரத்து செய்ய முடியும் என்பதை உச்ச நீதிமன்றம் உறுதி செய்தது.",
        "Pre-notification vetting by the Advocate General helps avoid embarrassing legal defeats for the State Government.",
        "தலைமை வழக்கறிஞரின் முன் பரிசீலனை அரசுக்கு நீதிமன்றங்களில் ஏற்படும் சட்டப் பின்னடைவுகளைத் தவிர்க்க உதவுகிறது."
    )

    # Q36 (D)
    add_q(
        "ADVG_M_036", "Additional Advocate General Constitutional Status",
        "What is the precise constitutional status of an 'Additional Advocate General' in a State according to the Supreme Court judgment in M.T. Khan v. Govt of AP (2004)?",
        "எம்.டி. கான் எதிர் ஆந்திர அரசு (2004) வழக்கின் உச்ச நீதிமன்றத் தீர்ப்பின்படி, மாநிலத்தில் உள்ள 'கூடுதல் தலைமை வழக்கறிஞரின்' (Additional Advocate General) துல்லியமான அரசியலமைப்பு நிலை என்ன?",
        "It is a constitutional post co-equal to the Advocate General under Article 165", "இது உறுப்பு 165-ன் கீழ் தலைமை வழக்கறிஞருக்கு சமமான ஓர் அரசியலமைப்புப் பதவியாகும்",
        "It is a post created under the Third Schedule of the Constitution", "இது அரசியலமைப்பின் மூன்றாவது அட்டவணையின் கீழ் உருவாக்கப்பட்ட பதவியாகும்",
        "It is a post appointed by the President of India under Article 76", "இது உறுப்பு 76-ன் கீழ் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படும் பதவியாகும்",
        "It is NOT a constitutional office under Article 165; it is an executive appointment created under Article 162 to assist the Advocate General", "இது உறுப்பு 165-ன் கீழ் ஓர் அரசியலமைப்பு பதவி அல்ல; இது உறுப்பு 162-ன் கீழ் தலைமை வழக்கறிஞருக்கு உதவ உருவாக்கப்பட்ட ஓர் நிர்வாக நியமனமாகும்",
        "D",
        "In M.T. Khan v. Government of Andhra Pradesh (2004), a two-judge bench of the Supreme Court categorically ruled that Article 165 permits only ONE Advocate General for a State. The office of Additional Advocate General is not a constitutional post under Article 165, but an office created under the executive power of the State under Article 162.",
        "எம்.டி. கான் எதிர் ஆந்திரப் பிரதேச அரசு (2004) வழக்கில், உறுப்பு 165 ஒரு மாநிலத்திற்கு ஒரு தலைமை வழக்கறிஞரை மட்டுமே அனுமதிக்கிறது என்று உச்ச நீதிமன்றம் திட்டவட்டமாக தீர்ப்பளித்தது. கூடுதல் தலைமை வழக்கறிஞர் பதவி உறுப்பு 165-ன் கீழ் அரசியலமைப்புப் பதவி அல்ல, மாறாக உறுப்பு 162-ன் கீழ் மாநிலத்தின் நிர்வாக அதிகாரத்தால் உருவாக்கப்பட்ட ஒரு பதவியாகும்.",
        "Incorrect. Article 165 contemplates only a singular Advocate General, not co-equal Additional AGs.", "தவறு. உறுப்பு 165 ஒற்றைத் தலைமை வழக்கறிஞரையே கருதுகிறது, சம அந்தஸ்துள்ள கூடுதல் தலைமை வழக்கறிஞர்களை அல்ல.",
        "Incorrect. Third Schedule does not create posts; it only lists oaths for specified offices.", "தவறு. மூன்றாவது அட்டவணை பதவிகளை உருவாக்கவில்லை; குறிப்பிட்ட பதவிகளுக்கான உறுதிமொழிகளை மட்டுமே பட்டியலிடுகிறது.",
        "Incorrect. The President appoints Union law officers under Article 76, not Additional AGs.", "தவறு. குடியரசுத் தலைவர் உறுப்பு 76-ன் கீழ் ஒன்றிய அதிகாரிகளை நியமிக்கிறார், கூடுதல் AG-யை அல்ல.",
        "Correct. Additional Advocate General is an executive appointment under Article 162, NOT a constitutional post under Article 165.", "சரி. கூடுதல் தலைமை வழக்கறிஞர் என்பது உறுப்பு 162-ன் கீழான நிர்வாக நியமனமே தவிர உறுப்பு 165-ன் கீழான அரசியலமைப்பு பதவி அல்ல.",
        "Consequence: Exclusive constitutional or statutory powers vested in the Advocate General (e.g., Section 15 Contempt consent) cannot be exercised by an Additional AG unless specifically authorized by statute.",
        "விளைவு: அட்வகேட் ஜெனரலுக்கு வழங்கப்பட்ட பிரத்தியேக அரசியலமைப்பு அல்லது சட்ட அதிகாரங்களை (எ.கா. அவமதிப்பு இசைவு) சட்டப்பூர்வமாக அங்கீகரிக்கப்படாவிட்டால் கூடுதல் AG பயன்படுத்த முடியாது.",
        "Additional Advocate Generals primarily represent the State in designated courtrooms or subject portfolios.",
        "கூடுதல் தலைமை வழக்கறிஞர்கள் குறிப்பிட்ட நீதிமன்ற அறைகளில் அல்லது குறிப்பிட்ட துறை வழக்குகளில் அரசைப் பிரதிநிதித்துவப்படுத்துகின்றனர்."
    )

    # Q37 (A)
    add_q(
        "ADVG_M_037", "Contempt of Courts Section 15 Distinction",
        "Why did Parliament require the written consent of the Advocate General under Section 15 of the Contempt of Courts Act, 1971 before a private citizen can file a criminal contempt motion in the High Court?",
        "ஒரு தனிநபர் உயர் நீதிமன்றத்தில் குற்றவியல் அவமதிப்பு மனுவைத் தாக்கல் செய்வதற்கு முன்பு, நீதிமன்ற அவமதிப்புச் சட்டம் 1971 பிரிவு 15-ன் கீழ் தலைமை வழக்கறிஞரின் எழுத்துப்பூர்வ இசைவை நாடாளுமன்றம் ஏன் கட்டாயமாக்கியது?",
        "To act as a filter against frivolous, vexatious, or malicious contempt petitions and prevent abuse of judicial time", "வீணான, பழிவாங்கும் அல்லது உள்நோக்கம் கொண்ட அவமதிப்பு மனுக்களை வடிகட்டவும், நீதிமன்ற நேரத்தை வீணடிப்பதைத் தடுக்கவும் ஒரு வடிகட்டியாக செயல்பட",
        "To ensure that all contempt fines are paid directly to the Advocate General", "அனைத்து அவமதிப்பு அபராதங்களும் நேரடியாக தலைமை வழக்கறிஞருக்கே செலுத்தப்படுவதை உறுதி செய்ய",
        "Because the Advocate General decides the punishment in contempt cases instead of judges", "நீதிபதிகளுக்குப் பதிலாக தலைமை வழக்கறிஞரே அவமதிப்பு வழக்குகளில் தண்டனையைத் தீர்மானிப்பதால்",
        "To prevent judges from knowing who filed the contempt petition", "அவமதிப்பு மனுவை யார் தாக்கல் செய்தது என்பதை நீதிபதிகள் அறியாமல் தடுக்க",
        "A",
        "In Conサempt of Courts Act jurisprudence (e.g., Bal Thackrey case, P.N. Duda case), the Supreme Court emphasized that the requirement of the Advocate General's consent serves as an essential gatekeeper mechanism to protect the court from being inundated with frivolous petitions brought for personal publicity or vendetta.",
        "நீதிமன்ற அவமதிப்புச் சட்டத் தீர்ப்புகளில், தனிப்பட்ட விளம்பரத்திற்காகவோ அல்லது பழிவாங்கும் நோக்கத்திலோ கொண்டுவரப்படும் தேவையற்ற மனுக்களிலிருந்து நீதிமன்றத்தைப் பாதுகாக்கும் ஒரு முக்கியமான கதவுக் காவலர் (Gatekeeper) அமைப்பாக தலைமை வழக்கறிஞரின் இசைவு செயல்படுகிறது என்பதை உச்ச நீதிமன்றம் வலியுறுத்தியுள்ளது.",
        "Correct. Designed as a statutory filter against vexatious petitions and misuse of court processes.", "சரி. வீண் மனுக்கள் மற்றும் நீதிமன்ற நடைமுறைகளை தவறாகப் பயன்படுத்துவதற்கு எதிரான சட்டப்பூர்வ வடிகட்டியாக வடிவமைக்கப்பட்டுள்ளது.",
        "Incorrect. Contempt fines go to the court/state exchequer, not to law officers.", "தவறு. அவமதிப்பு அபராதங்கள் அரசு கருவூலத்திற்கு செல்கின்றன, சட்ட அதிகாரிகளுக்கு அல்ல.",
        "Incorrect. Sentencing in contempt is exclusively a judicial power of judges under Section 12.", "தவறு. பிரிவு 12-ன் கீழ் அவமதிப்பு தண்டனை வழங்குவது முற்றிலும் நீதிபதிகளின் நீதித்துறை அதிகாரமாகும்.",
        "Incorrect. Litigant identities are always public on court records.", "தவறு. வழக்காடிகளின் விவரங்கள் எப்போதும் நீதிமன்ற ஆவணங்களில் பகிரங்கமாக இருக்கும்.",
        "If the Advocate General refuses consent, the petitioner cannot appeal that refusal to the court, but the court may initiate suo motu action if it independently finds merit.",
        "தலைமை வழக்கறிஞர் இசைவை மறுத்தால், அந்த மறுப்பை எதிர்த்து மனுதாரர் மேல்முறையீடு செய்ய முடியாது; எனினும் நீதிமன்றம் விரும்பினால் தானாக முன்வந்து வழக்கை எடுக்கலாம்.",
        "The Advocate General exercises this gatekeeping function as a dispassionate constitutional officer.",
        "தலைமை வழக்கறிஞர் இந்த வடிகட்டும் பணியை விருப்பு வெறுப்பற்ற ஓர் அரசியலமைப்பு அதிகாரியாகச் செய்கிறார்."
    )

    # Q38 (B)
    add_q(
        "ADVG_M_038", "Election Petitions Role",
        "Can the Advocate General of a State appear as private counsel for a candidate in an election petition challenging the election of an MLA to the State Legislative Assembly?",
        "மாநில சட்டப் பேரவைக்கு ஒரு எம்.எல்.ஏ தேர்ந்தெடுக்கப்பட்டதை எதிர்த்து தொடரப்படும் தேர்தல் மனுவில் (Election Petition), வேட்பாளரின் தனிப்பட்ட வழக்கறிஞராக தலைமை வழக்கறிஞர் ஆஜராக முடியுமா?",
        "Yes, without any restriction, because election petitions are purely political disputes", "ஆம், எந்தக் கட்டுப்பாடும் இன்றி ஆஜராகலாம், ஏனெனில் தேர்தல் மனுக்கள் முற்றிலும் அரசியல் தாவாக்கள்",
        "No, appearing in partisan election disputes between rival candidates is contrary to the public character of his constitutional office", "முடியாது, இரு வேட்பாளர்களுக்கு இடையேயான தேர்தல் வழக்கில் ஒருதலைப்பட்சமாக ஆஜராவது அவரது அரசியலமைப்பு பதவியின் பொது மாண்பிற்கு முரணானது",
        "Yes, but only if the candidate belongs to the ruling party", "ஆம், ஆனால் வேட்பாளர் ஆளும் கட்சியைச் சேர்ந்தவராக இருந்தால் மட்டுமே",
        "Yes, if permitted by the Election Commission of India", "ஆம், இந்தியத் தேர்தல் ஆணையம் அனுமதித்தால் செய்யலாம்",
        "B",
        "By established conventions of professional conduct and state law officers rules, the Advocate General does not appear for private candidates in election petitions before the High Court. Because election petitions involve inter-party political rivalry, the chief law officer of the State must maintain strict impartiality.",
        "தொழில்முறை நடத்தை மற்றும் மாநில சட்ட அதிகாரிகள் விதிகளின்படி, உயர் நீதிமன்றத்தில் உள்ள தேர்தல் மனுக்களில் தலைமை வழக்கறிஞர் தனிப்பட்ட வேட்பாளர்களுக்காக ஆஜராவதில்லை. தேர்தல் மனுக்கள் அரசியல் கட்சிகளுக்கு இடையேயான போட்டியை உள்ளடக்கியிருப்பதால், மாநிலத்தின் முதன்மை சட்ட அதிகாரி கடுமையான நடுநிலையைக் கடைப்பிடிக்க வேண்டும்.",
        "Incorrect. Election petitions are judicial proceedings under Representation of the People Act 1951.", "தவறு. தேர்தல் மனுக்கள் மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் கீழான நீதித்துறை நடவடிக்கைகள் ஆகும்.",
        "Correct. Prohibited by established convention and ethics to preserve institutional impartiality.", "சரி. நிறுவன நடுநிலையைப் பாதுகாக்க நிறுவப்பட்ட மரபுகள் மற்றும் நெறிமுறைகளால் இது தடுக்கப்படுகிறது.",
        "Incorrect. Appearing for ruling party candidates would flagrantly violate constitutional neutrality.", "தவறு. ஆளும் கட்சி வேட்பாளர்களுக்காக ஆஜராவது அரசியலமைப்பு நடுநிலையை அப்பட்டமாக மீறுவதாகும்.",
        "Incorrect. Election Commission does not regulate private appearances of State law officers.", "தவறு. தேர்தல் ஆணையம் மாநில சட்ட அதிகாரிகளின் தனிப்பட்ட ஆஜராகுதல்களை ஒழுங்குபடுத்துவதில்லை.",
        "The Advocate General represents the State, and the State must remain neutral in electoral contests between candidates.",
        "தலைமை வழக்கறிஞர் அரசைப் பிரதிநிதித்துவப்படுத்துகிறார், மேலும் வேட்பாளர்களுக்கு இடையேயான தேர்தல் போட்டிகளில் அரசு நடுநிலையாக இருக்க வேண்டும்.",
        "If the validity of a statutory provision of the election law is challenged, the AG may appear in his official capacity to defend the statute.",
        "தேர்தல் சட்டத்தின் சட்டப்பூர்வ செல்லுபடி தன்மை சவால் செய்யப்பட்டால் மட்டுமே, சட்டத்தை ஆதரிக்க AG தனது அலுவல் முறையில் ஆஜராகலாம்."
    )

    # Q39 (C)
    add_q(
        "ADVG_M_039", "Nolle Prosequi Comparison",
        "In English common law, the Attorney General has the prerogative power of entering a 'nolle prosequi' (staying/discontinuing criminal prosecution). In India, how is this power regulated in State courts?",
        "ஆங்கிலேய பொதுச் சட்டத்தில், தலைமை வழக்கறிஞர் குற்றவியல் வழக்கை நிறுத்தி வைக்கும் 'Nolle Prosequi' அதிகாரத்தைக் கொண்டுள்ளார். இந்தியாவில் மாநில நீதிமன்றங்களில் இந்த அதிகாரம் எவ்வாறு ஒழுங்குபடுத்தப்படுகிறது?",
        "The Advocate General possesses absolute personal power to enter nolle prosequi at will", "தலைமை வழக்கறிஞர் தனது விருப்பப்படி nolle prosequi செய்யும் முழுமையான தனிப்பட்ட அதிகாரத்தைக் கொண்டுள்ளார்",
        "The power has been abolished completely and no prosecution can ever be withdrawn", "இந்த அதிகாரம் முற்றிலும் ஒழிக்கப்பட்டுவிட்டது மற்றும் எந்த வழக்கையும் திரும்பப் பெற முடியாது",
        "The common law prerogative has been replaced by Section 321 of the Code of Criminal Procedure, where withdrawal is made by the Public Prosecutor with the court's consent", "பொதுச் சட்ட தனியுரிமைக்கு மாற்றாக குற்றவியல் நடைமுறைச் சட்டம் பிரிவு 321 கொண்டுவரப்பட்டுள்ளது, இதில் நீதிமன்ற அனுமதியுடன் அரசு வழக்கறிஞரால் மட்டுமே வழக்கு திரும்பப் பெறப்படுகிறது",
        "The Chief Justice of the High Court enters nolle prosequi upon executive request", "நிர்வாகக் கோரிக்கையின் பேரில் உயர் நீதிமன்ற தலைமை நீதிபதி வழக்கை நிறுத்துகிறார்",
        "C",
        "In India, the ancient English common law prerogative of 'nolle prosequi' by the Attorney General / Advocate General has been codified and modified by statute. Under Section 321 CrPC / Section 360 BNSS, withdrawal from prosecution can only be initiated by the Public Prosecutor in charge of the case and must be approved by the trial court.",
        "இந்தியாவில், தலைமை வழக்கறிஞரின் பழமையான ஆங்கிலேய பொதுச் சட்ட 'Nolle Prosequi' அதிகாரம் சட்டத்தால் மாற்றியமைக்கப்பட்டுள்ளது. பிரிவு 321 CrPC / பிரிவு 360 BNSS-ன் கீழ், வழக்கை நடத்தும் அரசு வழக்கறிஞர் மட்டுமே வழக்கை திரும்பப் பெற விண்ணப்பிக்க முடியும் மற்றும் அதற்கு நீதிமன்றத்தின் ஒப்புதல் கட்டாயமாகும்.",
        "Incorrect. Unfettered common law prerogative does not survive statutory codification in CrPC.", "தவறு. கட்டுப்பாடற்ற பொதுச் சட்ட தனியுரிமை CrPC சட்டத் தொகுப்பிற்குப் பிறகு நீடிக்கவில்லை.",
        "Incorrect. Withdrawal is permissible under Section 321 CrPC.", "தவறு. பிரிவு 321 CrPC-ன் கீழ் வழக்கை திரும்பப் பெற அனுமதி உண்டு.",
        "Correct. Codified under Section 321 CrPC: Public Prosecutor applies, and Court must consent.", "சரி. CrPC பிரிவு 321-ன் கீழ் முறைப்படுத்தப்பட்டுள்ளது: அரசு வழக்கறிஞர் விண்ணப்பிக்கிறார், நீதிமன்றம் ஒப்புதல் அளிக்க வேண்டும்.",
        "Incorrect. Chief Justice does not exercise trial withdrawal powers.", "தவறு. தலைமை நீதிபதி விசாரணை திரும்பப் பெறும் அதிகாரத்தைப் பயன்படுத்துவதில்லை.",
        "In State of Bihar v. Ram Naresh Pandey (1957), the Supreme Court detailed the transition from nolle prosequi to Section 494 (now 321) CrPC.",
        "ராம் நரேஷ் பாண்டே வழக்கில் (1957), nolle prosequi-யிலிருந்து CrPC பிரிவு 321-க்கான மாற்றத்தை உச்ச நீதிமன்றம் விரிவாக விளக்கியது.",
        "The court's consent is a judicial act to ensure that the withdrawal is in the interest of public justice, not political favoritism.",
        "நீதிமன்றத்தின் ஒப்புதல் என்பது வழக்குத் திரும்பப் பெறுதல் அரசியல் ஆதரவிற்காக அன்றி, பொது நீதிக்காகவே செய்யப்படுகிறது என்பதை உறுதி செய்யும் ஒரு நீதித்துறை நடவடிக்கையாகும்."
    )

    # Q40 (D)
    add_q(
        "ADVG_M_040", "Subordinate Courts Appearance",
        "Can the Advocate General of a State personally appear in a District Munsif Court or Court of Judicial Magistrate to argue a case on behalf of the State?",
        "மாநில அரசின் சார்பில் ஒரு வழக்கில் வாதாட மாவட்ட முன்சீப் நீதிமன்றத்திலோ அல்லது நீதித்துறை நடுவர் நீதிமன்றத்திலோ தலைமை வழக்கறிஞர் தனிப்பட்ட முறையில் ஆஜராக முடியுமா?",
        "No, his constitutional right of audience is strictly limited to High Courts", "இல்லை, அவரது அரசியலமைப்பு வாதாடும் உரிமை உயர் நீதிமன்றத்திற்கு மட்டுமே கண்டிப்பாக மட்டுப்படுத்தப்பட்டுள்ளது",
        "No, appearing in lower courts is considered contempt of the High Court", "இல்லை, கீழ் நீதிமன்றங்களில் ஆஜராவது உயர் நீதிமன்ற அவமதிப்பாகக் கருதப்படுகிறது",
        "Only if the Supreme Court grants a special ad-hoc license", "உச்ச நீதிமன்றம் சிறப்பு தற்காலிக உரிமம் வழங்கினால் மட்டுமே",
        "Yes, the Advocate General has the right of audience in any court within the State, from the highest to the lowest subordinate court", "ஆம், மாநிலத்தில் உள்ள மிக உயர்ந்த நீதிமன்றம் முதல் மிகக் கீழ்நிலை நீதிமன்றம் வரை எந்தவொரு நீதிமன்றத்திலும் வாதாடும் உரிமை தலைமை வழக்கறிஞருக்கு உண்டு",
        "D",
        "Under the constitutional scheme and the Advocates Act, 1961, the Advocate General has the right of audience in ALL courts within the territory of the State. While he routinely appears in the High Court and Supreme Court, there is no legal bar preventing him from appearing before a District Court or Magistrate's Court when a case is of vital public significance.",
        "அரசியலமைப்பு கட்டமைப்பு மற்றும் வழக்கறிஞர்கள் சட்டம் 1961-ன் கீழ், மாநில எல்லைக்குள் உள்ள அனைத்து நீதிமன்றங்களிலும் வாதாடும் உரிமை தலைமை வழக்கறிஞருக்கு உண்டு. அவர் வழக்கமாக உயர் மற்றும் உச்ச நீதிமன்றங்களில் ஆஜரானாலும், முக்கிய பொது விவகாரங்களில் மாவட்ட நீதிமன்றத்திலோ அல்லது நடுவர் நீதிமன்றத்திலோ ஆஜராவதற்கு எந்த சட்டத் தடையும் இல்லை.",
        "Incorrect. Not restricted solely to High Courts.", "தவறு. உயர் நீதிமன்றத்திற்கு மட்டுமே மட்டுப்படுத்தப்படவில்லை.",
        "Incorrect. It is a lawful exercise of his right of audience, not contempt.", "தவறு. இது அவரது சட்டப்பூர்வ வாதாடும் உரிமையாகும், நீதிமன்ற அவமதிப்பு அல்ல.",
        "Incorrect. No Supreme Court license is required within the State.", "தவறு. மாநில எல்லைக்குள் உச்ச நீதிமன்ற உரிமம் எதுவும் தேவையில்லை.",
        "Correct. He has the right of audience in any court within the State, including subordinate courts.", "சரி. கீழ்மை நீதிமன்றங்கள் உட்பட மாநில எல்லைக்குள் உள்ள எந்த நீதிமன்றத்திலும் அவருக்கு வாதாடும் உரிமை உண்டு.",
        "In historic cases involving sensitive border clashes or major public inquiries, Advocate Generals have occasionally appeared in subordinate courts.",
        "முக்கிய எல்லை மோதல்கள் அல்லது பெரிய பொது விசாரணைகள் தொடர்பான வரலாற்று நிகழ்வுகளில், தலைமை வழக்கறிஞர்கள் கீழ்மை நீதிமன்றங்களிலும் ஆஜராகியுள்ளனர்.",
        "When he appears in a subordinate court, he enjoys pre-audience over all other advocates present in that courtroom.",
        "அவர் கீழ்மை நீதிமன்றத்தில் ஆஜராகும் போது, அந்த நீதிமன்ற அறையில் உள்ள மற்ற அனைத்து வழக்கறிஞர்களுக்கும் மேலாக முன்னுரிமை பெறுகிறார்."
    )

    # --- 41 to 50 ---
    # Q41 (A)
    add_q(
        "ADVG_M_041", "Civil Disobedience / Strike by Bar",
        "When the State Bar Association calls for a strike or court boycott, what is the professional and constitutional duty of the Advocate General?",
        "மாநில வழக்கறிஞர் சங்கம் வேலைநிறுத்தம் அல்லது நீதிமன்றப் புறக்கணிப்புக்கு அழைப்பு விடுக்கும் போது, தலைமை வழக்கறிஞரின் தொழில்முறை மற்றும் அரசியலமைப்பு கடமை என்ன?",
        "To ensure that the courts continue to function and the State Government's cases are represented, as strike by lawyers is illegal", "நீதிமன்றங்கள் தொடர்ந்து செயல்படுவதையும் அரசின் வழக்குகள் பிரதிநிதித்துவப்படுத்தப்படுவதையும் உறுதி செய்வது, ஏனெனில் வழக்கறிஞர்களின் வேலைநிறுத்தம் சட்டவிரோதமானது",
        "To personally lead the strike and lock the doors of the High Court", "வேலைநிறுத்தத்திற்கு தனிப்பட்ட முறையில் தலைமை தாங்கி உயர் நீதிமன்ற கதவுகளைப் பூட்டுவது",
        "To suspend all judges who attend court during the strike", "வேலைநிறுத்தத்தின் போது நீதிமன்றத்திற்கு வரும் அனைத்து நீதிபதிகளையும் இடைநீக்கம் செய்வது",
        "To resign immediately in solidarity with the Bar Association", "வழக்கறிஞர் சங்கத்திற்கு ஆதரவாக உடனடியாக தனது பதவியை ராஜினாமா செய்வது",
        "A",
        "In Ex-Capt. Harish Uppal v. Union of India (2003), the Supreme Court declared that advocates have no right to go on strike or give a call for boycott of courts. As the leader of the Bar and the chief law officer of the State, the Advocate General's duty is to uphold the administration of justice and ensure that the State's cases are not neglected.",
        "ஹரிஷ் உப்பால் வழக்கில் (2003), வழக்கறிஞர்களுக்கு வேலைநிறுத்தம் செய்யவோ அல்லது நீதிமன்றங்களைப் புறக்கணிக்கவோ எந்த உரிமையும் இல்லை என்று உச்ச நீதிமன்றம் அறிவித்தது. வழக்கறிஞர் சங்கத்தின் தலைவர் மற்றும் மாநிலத்தின் முதன்மை சட்ட அதிகாரி என்ற முறையில், நீதி நிர்வாகத்தை நிலைநிறுத்துவதும் அரசின் வழக்குகள் புறக்கணிக்கப்படாமல் இருப்பதை உறுதி செய்வதும் தலைமை வழக்கறிஞரின் கடமையாகும்.",
        "Correct. Duty is to ensure administration of justice continues and State representation is maintained.", "சரி. நீதி நிர்வாகம் தொடர்வதையும் அரசின் பிரதிநிதித்துவம் பராமரிக்கப்படுவதையும் உறுதி செய்வதே அவரது கடமையாகும்.",
        "Incorrect. Law officers cannot participate in illegal court boycotts.", "தவறு. சட்ட அதிகாரிகளால் சட்டவிரோத நீதிமன்றப் புறக்கணிப்புகளில் பங்கேற்க முடியாது.",
        "Incorrect. Has no authority over judges.", "தவறு. நீதிபதிகள் மீது எந்த அதிகாரமும் இல்லை.",
        "Incorrect. The AG represents the constitutional government, not a striking trade body.", "தவறு. AG அரசியலமைப்பு அரசைப் பிரதிநிதித்துவப்படுத்துகிறார், வேலைநிறுத்தம் செய்யும் தொழிற்சங்கத்தை அல்ல.",
        "Law officers (AG, Additional AGs, Government Pleaders) routinely appear in court even during Bar boycotts to protect public cases.",
        "சட்ட அதிகாரிகள் (AG, கூடுதல் AG, அரசு வழக்கறிஞர்கள்) பொது வழக்குகளைப் பாதுகாக்க புறக்கணிப்பு நாட்களிலும் கூட நீதிமன்றங்களில் ஆஜராகின்றனர்.",
        "Failure to appear on behalf of the State could result in adverse ex-parte orders damaging public interest.",
        "அரசுக்காக ஆஜராகத் தவறினால், பொது நலனைப் பாதிக்கும் ஒருதலைப்பட்ச பாதகமான உத்தரவுகள் பிறப்பிக்கப்பட வாய்ப்புள்ளது."
    )

    # Q42 (B)
    add_q(
        "ADVG_M_042", "Article 217(2) Ten Years Count Rule",
        "Under Explanation (a) to Article 217(2), how is the 10-year period computed if an advocate has also held a judicial office for some years?",
        "உறுப்பு 217(2)-ன் விளக்கம் (a)-ன் கீழ், ஒரு வழக்கறிஞர் சில ஆண்டுகள் நீதித்துறை பதவியையும் வகித்திருந்தால், அந்த 10 ஆண்டு காலம் எவ்வாறு கணக்கிடப்படுகிறது?",
        "Only the period as an advocate is counted; judicial service is completely ignored", "வழக்கறிஞராக இருந்த காலம் மட்டுமே கணக்கிடப்படும்; நீதித்துறைப் பணி முற்றிலும் புறக்கணிக்கப்படும்",
        "In computing the period, there shall be included any period during which the person has held judicial office or the office of a member of a tribunal after he became an advocate", "அக்காலத்தைக் கணக்கிடுவதில், அவர் வழக்கறிஞரான பிறகு நீதித்துறை பதவியையோ அல்லது தீர்ப்பாய உறுப்பினராகவோ வகித்த காலமும் சேர்த்துக்கொள்ளப்படும்",
        "The periods are multiplied by two", "அக்காலங்கள் இரண்டால் பெருக்கப்படும்",
        "He must complete 10 years in each category separately (total 20 years)", "ஒவ்வொரு பிரிவிலும் தனித்தனியாக 10 ஆண்டுகளை அவர் முடிக்க வேண்டும் (மொத்தம் 20 ஆண்டுகள்)",
        "B",
        "Explanation (a) to Article 217(2) provides that in computing the period during which a person has been an advocate of a High Court, there shall be included any period during which the person has held judicial office or the office of a member of a tribunal or any post under the Union or a State requiring special knowledge of law after he became an advocate.",
        "உறுப்பு 217(2)-ன் விளக்கம் (a) உயர் நீதிமன்ற வழக்கறிஞராக இருந்த காலத்தைக் கணக்கிடுவதில், ஒருவர் வழக்கறிஞரான பிறகு நீதித்துறை பதவியை அல்லது தீர்ப்பாய உறுப்பினராக அல்லது சட்ட அறிவு தேவைப்படும் அரசுப் பதவியை வகித்த காலமும் சேர்த்துக்கொள்ளப்படும் என்று வழங்குகிறது.",
        "Incorrect. Judicial service is not ignored; it is explicitly added.", "தவறு. நீதித்துறைப் பணி புறக்கணிக்கப்படுவதில்லை; அது வெளிப்படையாகச் சேர்க்கப்படுகிறது.",
        "Correct. Article 217(2) Explanation (a) allows combining advocacy and judicial/tribunal tenure.", "சரி. உறுப்பு 217(2) விளக்கம் (a) வழக்கறிஞர் பணி மற்றும் நீதித்துறை/தீர்ப்பாய பணிக் காலத்தை இணைக்க அனுமதிக்கிறது.",
        "Incorrect. There is no multiplication formula.", "தவறு. பெருக்கல் வாய்ப்பாடு எதுவும் இல்லை.",
        "Incorrect. Total combined benchmark is 10 years, not 20 years.", "தவறு. மொத்த ஒருங்கிணைந்த வரம்பு 10 ஆண்டுகள் மட்டுமே, 20 ஆண்டுகள் அல்ல.",
        "This integration allows experienced legal minds with mixed service (Bar + Bench) to qualify for constitutional appointments.",
        "இந்த இணைப்பு கலப்புப் பணி (வழக்கறிஞர் + நீதித்துறை) அனுபவம் கொண்ட தகுதியான நபர்கள் அரசியலமைப்பு நியமனங்களுக்கு தகுதி பெற உதவுகிறது.",
        "The 44th Amendment Act, 1978 also clarified the inclusion of tribunal membership.",
        "1978-ஆம் ஆண்டின் 44-வது திருத்தச் சட்டம் தீர்ப்பாய உறுப்பினர் காலத்தையும் சேர்ப்பதை தெளிவுபடுத்தியது."
    )

    # Q43 (C)
    add_q(
        "ADVG_M_043", "Private Retainer against State Undertakings",
        "Can the Advocate General of a State accept a private brief from a multinational corporation to challenge an environmental regulation issued by the State Pollution Control Board?",
        "மாநில மாசுக்கட்டுப்பாட்டு வாரியம் வெளியிட்ட சுற்றுச்சூழல் ஒழுங்குமுறையை எதிர்த்து ஒரு பன்னாட்டு நிறுவனத்தின் சார்பில் தனிப்பட்ட முறையில் வழக்காட தலைமை வழக்கறிஞர் அந்த வழக்கை ஏற்க முடியுமா?",
        "Yes, because the Pollution Control Board is an independent statutory board, not the State itself", "ஆம், ஏனெனில் மாசுக்கட்டுப்பாட்டு வாரியம் ஒரு சுதந்திரமான சட்டப்பூர்வ வாரியம், அரசே அல்ல",
        "Yes, provided he obtains permission from the multinational corporation", "ஆம், பன்னாட்டு நிறுவனத்திடம் அனுமதி பெற்றால் ஏற்கலாம்",
        "No, the Advocate General cannot advise or appear against any department, board, or statutory corporation of the State Government", "முடியாது, மாநில அரசின் எந்தவொரு துறை, வாரியம் அல்லது சட்டப்பூர்வ நிறுவனத்திற்கு எதிராக தலைமை வழக்கறிஞர் ஆலோசிக்கவோ அல்லது ஆஜராகவோ முடியாது",
        "Yes, if he charges a subsidized rate of fee", "ஆம், குறைந்த கட்டணம் வசூலித்தால் செய்யலாம்",
        "C",
        "The Advocate General represents the entire governmental apparatus of the State. Accepting a brief against a state statutory body like the Pollution Control Board, State Electricity Board, or Transport Corporation creates an impermissible direct conflict of interest with his duty to uphold State policies.",
        "தலைமை வழக்கறிஞர் மாநிலத்தின் ஒட்டுமொத்த அரசு இயந்திரத்தையும் பிரதிநிதித்துவப்படுத்துகிறார். மாசுக்கட்டுப்பாட்டு வாரியம், மின்சார வாரியம் அல்லது போக்குவரத்துக் கழகம் போன்ற அரசு சட்டப்பூர்வ அமைப்புகளுக்கு எதிராக வாதாடுவது மாநிலக் கொள்கைகளை நிலைநிறுத்தும் அவரது கடமையோடு நேரடி முரண்பாட்டை உருவாக்குகிறது.",
        "Incorrect. Statutory boards are instrumentalities of the State under Article 12.", "தவறு. சட்டப்பூர்வ வாரியங்கள் உறுப்பு 12-ன் கீழ் அரசின் உறுப்புகள் ஆகும்.",
        "Incorrect. Corporation permission does not remove the conflict with the State.", "தவறு. நிறுவனத்தின் அனுமதி அரசுடனான முரண்பாட்டை நீக்காது.",
        "Correct. Strictly prohibited from advising or holding briefs against any State instrumentality or board.", "சரி. அரசின் எந்தவொரு அமைப்பு அல்லது வாரியத்திற்கு எதிராக வாதாடுவதோ அல்லது ஆலோசிப்பதோ கண்டிப்பாகத் தடை செய்யப்பட்டுள்ளது.",
        "Incorrect. Fee discounts do not cure ethical illegality.", "தவறு. கட்டணச் சலுகைகள் நெறிமுறைச் சட்டவிரோதத்தை சரிசெய்யாது.",
        "The prohibition extends to appearing against state public sector undertakings (PSUs) and universities established by state acts.",
        "இத்தடை மாநில பொதுத்துறை நிறுவனங்கள் (PSU) மற்றும் மாநில சட்டங்களால் நிறுவப்பட்ட பல்கலைக்கழகங்களுக்கு எதிராகவும் நீட்டிக்கப்படுகிறது.",
        "If a conflict arises between two state corporations, the AG acts as an impartial arbiter or advises on amicable settlement.",
        "இரு அரசு நிறுவனங்களுக்கு இடையே மோதல் ஏற்பட்டால், தலைமை வழக்கறிஞர் நடுநிலையான மத்தியஸ்தராகச் செயல்படுகிறார்."
    )

    # Q44 (D)
    add_q(
        "ADVG_M_044", "Bar Council Disciplinary Committee",
        "What is the Advocate General's function regarding disciplinary proceedings against advocates under Section 35 and 36 of the Advocates Act, 1961?",
        "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 35 மற்றும் 36-ன் கீழ் வழக்கறிஞர்களுக்கு எதிரான ஒழுங்கு நடவடிக்கைகளில் தலைமை வழக்கறிஞரின் செயல்பாடு என்ன?",
        "He personally decides all disciplinary punishments without the Bar Council", "பார் கவுன்சில் இன்றி அனைத்து ஒழுங்கு தண்டனைகளையும் அவர் தனிப்பட்ட முறையில் தீர்மானிக்கிறார்",
        "He cannot participate in any disciplinary proceedings under any circumstances", "எந்த சூழ்நிலையிலும் எந்த ஒழுங்கு நடவடிக்கைகளிலும் அவர் பங்கேற்க முடியாது",
        "He acts as the criminal prosecutor to send advocates to prison", "வழக்கறிஞர்களை சிறைக்கு அனுப்பும் குற்றவியல் வழக்கறிஞராக செயல்படுகிறார்",
        "Notice of every disciplinary proceeding before the Disciplinary Committee is served on the Advocate General, who has the right to appear and be heard", "ஒழுங்கு நடவடிக்கைக் குழுவின் முன் உள்ள ஒவ்வொரு ஒழுங்கு நடவடிக்கையின் அறிவிப்பும் தலைமை வழக்கறிஞருக்கு வழங்கப்படுகிறது, மேலும் அதில் ஆஜராகி வாதத்தை முன்வைக்க அவருக்கு உரிமை உண்டு",
        "D",
        "Under Section 35(2) and Section 36(3) of the Advocates Act, 1961, the Disciplinary Committee of the Bar Council must issue notice of the hearing date to the Advocate General. The Advocate General may appear personally or through an advocate instructed by him to assist the committee as an amicus curiae representing the public interest.",
        "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 35(2) மற்றும் 36(3)-ன் படி, பார் கவுன்சிலின் ஒழுங்கு நடவடிக்கைக் குழு விசாரணை தேதியை தலைமை வழக்கறிஞருக்கு தெரிவிக்க வேண்டும். தலைமை வழக்கறிஞர் தனிப்பட்ட முறையிலோ அல்லது தனது பிரதிநிதி மூலமாகவோ ஆஜராகி பொது நலனைப் பிரதிநிதித்துவப்படுத்தும் வகையில் குழுவுக்கு உதவ முடியும்.",
        "Incorrect. The Disciplinary Committee of the Bar Council decides disciplinary matters, not the AG alone.", "தவறு. பார் கவுன்சிலின் ஒழுங்கு நடவடிக்கைக் குழுவே ஒழுங்கு விவகாரங்களை தீர்மானிக்கிறது, AG மட்டுமே அல்ல.",
        "Incorrect. The statute explicitly provides for notice and right to appear.", "தவறு. சட்டம் வெளிப்படையாக நோட்டீஸ் மற்றும் ஆஜராகும் உரிமையை வழங்குகிறது.",
        "Incorrect. Disciplinary proceedings are professional conduct hearings, not criminal trials.", "தவறு. ஒழுங்கு நடவடிக்கைகள் தொழில்முறை நடத்தை விசாரணைகளே தவிர, குற்றவியல் விசாரணைகள் அல்ல.",
        "Correct. Notice must be served on the Advocate General, who has the statutory right to appear and be heard.", "சரி. தலைமை வழக்கறிஞருக்கு நோட்டீஸ் அனுப்பப்பட வேண்டும், மேலும் அவர் ஆஜராகி வாதாட சட்டப்பூர்வ உரிமை கொண்டுள்ளார்.",
        "The Advocate General represents the broader public interest in maintaining ethical standards in the legal profession.",
        "சட்டத் தொழிலில் நெறிமுறைத் தரங்களைப் பராமரிப்பதில் பரந்த பொது நலனை தலைமை வழக்கறிஞர் பிரதிநிதித்துவப்படுத்துகிறார்.",
        "His submissions assist the committee in distinguishing between genuine professional misconduct and frivolous client grievances.",
        "உண்மையான தொழில்முறை தவறான நடத்தைக்கும் அற்பமான வாடிக்கையாளர் புகார்களுக்கும் இடையே உள்ள வேறுபாட்டை அறிய அவரது வாதங்கள் குழுவுக்கு உதவுகின்றன."
    )

    # Q45 (A)
    add_q(
        "ADVG_M_045", "Public Prosecutor Hierarchy CrPC",
        "What is the statutory relationship between the Advocate General and the Director of Prosecution / Public Prosecutors appointed under Section 24 and 25A of CrPC (Sections 18 & 20 BNSS)?",
        "CrPC பிரிவு 24 மற்றும் 25A-ன் கீழ் (BNSS 18 & 20) நியமிக்கப்பட்ட வழக்குத் தொடருநர் இயக்குநர் / அரசு வழக்கறிஞர்களுக்கும் தலைமை வழக்கறிஞருக்கும் இடையிலான சட்டப்பூர்வ உறவு என்ன?",
        "The Advocate General is the supreme constitutional law officer of the State; all government law officers and prosecutors function under his overall supervisory guidance", "தலைமை வழக்கறிஞர் மாநிலத்தின் உச்ச அரசியலமைப்பு சட்ட அதிகாரி; அனைத்து அரசு சட்ட அதிகாரிகளும் அரசுத் தரப்பு வழக்கறிஞர்களும் அவரது ஒட்டுமொத்த மேற்பார்வை வழிகாட்டுதலின் கீழேயே செயல்படுகின்றனர்",
        "The Director of Prosecution is senior to the Advocate General in constitutional rank", "வழக்குத் தொடருநர் இயக்குநர் அரசியலமைப்பு அந்தஸ்தில் தலைமை வழக்கறிஞரை விட மூத்தவர்",
        "They operate in mutually exclusive jurisdictions with zero interaction", "அவர்கள் எந்த தொடர்பும் இன்றி முற்றிலும் தனித்தனி அதிகார வரம்புகளில் செயல்படுகின்றனர்",
        "The Advocate General is an employee of the Director of Prosecution", "தலைமை வழக்கறிஞர் வழக்குத் தொடருநர் இயக்குநரின் கீழ் பணிபுரியும் ஒரு ஊழியர் ஆவார்",
        "A",
        "While the Directorate of Prosecution under Section 25A CrPC handles the administrative functioning of subordinate prosecutors, the Advocate General remains the supreme constitutional law officer of the State. On all critical policy and legal questions, prosecutors take guidance from the Advocate General.",
        "CrPC பிரிவு 25A-ன் கீழான வழக்குத் தொடருநர் இயக்ககம் கீழ்மை வழக்கறிஞர்களின் நிர்வாகப் பணிகளைக் கையாண்டாலும், தலைமை வழக்கறிஞரே மாநிலத்தின் உச்ச அரசியலமைப்பு சட்ட அதிகாரியாக நீடிக்கிறார். அனைத்து முக்கிய கொள்கை மற்றும் சட்ட விவகாரங்களிலும் அரசு வழக்கறிஞர்கள் தலைமை வழக்கறிஞரிடமிருந்தே வழிகாட்டுதலைப் பெறுகின்றனர்.",
        "Correct. The Advocate General is the supreme constitutional law officer exercising overall guidance.", "சரி. தலைமை வழக்கறிஞரே ஒட்டுமொத்த வழிகாட்டுதலையும் வழங்கும் உச்ச அரசியலமைப்பு சட்ட அதிகாரி ஆவார்.",
        "Incorrect. Director of Prosecution is a statutory/administrative post, subordinate in status to the constitutional AG.", "தவறு. வழக்குத் தொடருநர் இயக்குநர் ஓர் நிர்வாகப் பதவி, அரசியலமைப்பு AG-யை விட கீழ்நிலையானது.",
        "Incorrect. They collaborate closely on state criminal appeals and capital cases.", "தவறு. மாநில குற்றவியல் மேல்முறையீடுகள் மற்றும் தூக்கு தண்டனை வழக்குகளில் அவர்கள் நெருக்கமாக இணைந்து செயல்படுகின்றனர்.",
        "Incorrect. The AG is a constitutional functionary, not an employee of any directorate.", "தவறு. AG ஓர் அரசியலமைப்பு அதிகாரி, எந்தவொரு இயக்ககத்தின் ஊழியரும் அல்ல.",
        "When capital murder appeals or constitutional criminal petitions reach the High Court, the Advocate General personally leads the argument.",
        "தூக்கு தண்டனை மேல்முறையீடுகள் அல்லது அரசியலமைப்பு குற்றவியல் மனுக்கள் உயர் நீதிமன்றத்தை அடையும் போது, தலைமை வழக்கறிஞரே வாதத்தை முன்னின்று நடத்துகிறார்.",
        "The Directorate of Prosecution ensures files and witness statements are properly compiled for the Advocate General's team.",
        "தலைமை வழக்கறிஞரின் குழுவிற்காக ஆவணங்கள் மற்றும் சாட்சி வாக்குமூலங்கள் சரியாக தொகுக்கப்படுவதை வழக்குத் தொடருநர் இயக்ககம் உறுதி செய்கிறது."
    )

    # Q46 (B)
    add_q(
        "ADVG_M_046", "Article 177 Meaning of 'Take Part'",
        "In Article 177, what does the phrase 'to take part in the proceedings' entitle the Advocate General to do in the State Legislative Assembly?",
        "உறுப்பு 177-ல், 'நடவடிக்கைகளில் பங்கேற்பது' (to take part in the proceedings) என்ற சொற்றொடர் மாநில சட்டமன்றத்தில் தலைமை வழக்கறிஞருக்கு என்ன செய்ய உரிமையளிக்கிறது?",
        "To introduce money bills as a minister", "ஓர் அமைச்சராக நிதி மசோதாக்களை அறிமுகப்படுத்த",
        "To participate in debates, answer legal queries raised by legislators, and explain the legal implications of proposed legislation", "விவாதங்களில் பங்கேற்க, சட்டமன்ற உறுப்பினர்கள் எழுப்பும் சட்டக் கேள்விகளுக்கு பதிலளிக்க மற்றும் முன்மொழியப்பட்ட சட்டங்களின் சட்டப்பூர்வ தாக்கங்களை விளக்க",
        "To cast the deciding vote when the House is tied", "அவையில் வாக்குகள் சமநிலையை அடையும் போது தீர்க்கமான வாக்கை செலுத்த",
        "To adjourn the Legislative Assembly if disorder breaks out", "அவையில் அமளி ஏற்பட்டால் சட்டப் பேரவையை ஒத்திவைக்க",
        "B",
        "The right 'to take part in the proceedings' allows the Advocate General to participate in legislative debates, clarify constitutional ambiguities, explain judicial precedents affecting draft bills, and respond to legal inquiries from members, while strictly maintaining non-voting status.",
        "'நடவடிக்கைகளில் பங்கேற்பது' என்பது தலைமை வழக்கறிஞருக்கு விவாதங்களில் கலந்து கொள்ளவும், அரசியலமைப்பு தெளிவின்மைகளை விளக்கவும், வரைவு மசோதாக்களைப் பாதிக்கும் தீர்ப்புகளை தெளிவுபடுத்தவும் மற்றும் உறுப்பினர்களின் சட்ட வினாக்களுக்கு பதிலளிக்கவும் உரிமையளிக்கிறது, அதே நேரத்தில் வாக்களிக்காத நிலையை கண்டிப்பாக கடைப்பிடிக்கிறது.",
        "Incorrect. Only ministers can introduce government bills.", "தவறு. அமைச்சர்கள் மட்டுமே அரசு மசோதாக்களை அறிமுகப்படுத்த முடியும்.",
        "Correct. Entitles him to participate in debates, explain legal mechanics, and answer constitutional questions.", "சரி. விவாதங்களில் பங்கேற்கவும், சட்ட நுணுக்கங்களை விளக்கவும், அரசியலமைப்பு கேள்விகளுக்கு பதிலளிக்கவும் அவருக்கு உரிமையளிக்கிறது.",
        "Incorrect. Voting is absolutely barred under Article 177.", "தவறு. உறுப்பு 177-ன் கீழ் வாக்களிப்பது முற்றிலும் தடை செய்யப்பட்டுள்ளது.",
        "Incorrect. Only the Speaker has the power to adjourn the House under legislative procedure rules.", "தவறு. சட்டமன்ற நடைமுறை விதிகளின் கீழ் அவையை ஒத்திவைக்கும் அதிகாரம் சபாநாயகருக்கு மட்டுமே உண்டு.",
        "The Advocate General sits in a designated seat on the floor of the House during legislative debates.",
        "சட்டமன்ற விவாதங்களின் போது தலைமை வழக்கறிஞர் அவையில் தனக்கென ஒதுக்கப்பட்ட இருக்கையில் அமர்கிறார்.",
        "His contributions ensure that legislative enactments withstand future judicial scrutiny under Part III.",
        "அவரது பங்களிப்பு சட்டமன்ற சட்டங்கள் எதிர்காலத்தில் பகுதி III-ன் கீழான நீதித்துறை மறுஆய்வில் நிலைத்து நிற்பதை உறுதி செய்கிறது."
    )

    # Q47 (C)
    add_q(
        "ADVG_M_047", "Inter-State Border Disputes",
        "In inter-state territorial or boundary disputes between neighbouring States (e.g., Maharashtra-Karnataka border dispute or Assam-Meghalaya dispute), what is the Advocate General's role?",
        "அண்டை மாநிலங்களுக்கு இடையேயான எல்லை அல்லது நிலப்பரப்பு தாவாக்களில் (எ.கா. மகாராஷ்டிரா-கர்நாடகா எல்லைப் பிரச்சனை அல்லது அசாம்-மேகாலயா பிரச்சனை), தலைமை வழக்கறிஞரின் பங்கு என்ன?",
        "To deploy the State police force across the border unilaterally", "எல்லைக்கு அப்பால் மாநில காவல் துறையை தன்னிச்சையாக நிலைநிறுத்துவது",
        "To redraw the map of India under Article 3", "உறுப்பு 3-ன் கீழ் இந்திய வரைபடத்தை மாற்றி அமைப்பது",
        "To formulate the historical and constitutional legal claims of the State and argue its boundary suit under Article 131 before the Supreme Court", "மாநிலத்தின் வரலாற்று மற்றும் அரசியலமைப்பு ரீதியான சட்ட உரிமைகளை வடிவமைத்து, உச்ச நீதிமன்றத்தில் உறுப்பு 131-ன் கீழ் எல்லை வழக்கை வாதிடுவது",
        "To merge the disputed territory into a Union Territory", "தகராறுக்குரிய பகுதியை ஒன்றிய பிரதேசமாக இணைப்பது",
        "C",
        "Inter-state boundary disputes are litigated under the original jurisdiction of the Supreme Court under Article 131. The Advocate General formulates the legal arguments based on historical treaties, States Reorganisation Act 1956 provisions, linguistic survey data, and administrative maps.",
        "மாநிலங்களுக்கு இடையேயான எல்லைத் தாவாக்கள் உறுப்பு 131-ன் கீழ் உச்ச நீதிமன்றத்தின் அசல் அதிகார வரம்பில் வழக்காடப்படுகின்றன. வரலாற்று ஒப்பந்தங்கள், மாநில மறுசீரமைப்புச் சட்டம் 1956, மொழிவாரி கணக்கெடுப்பு மற்றும் நிர்வாக வரைபடங்களின் அடிப்படையில் தலைமை வழக்கறிஞர் சட்ட வாதங்களை உருவாக்குகிறார்.",
        "Incorrect. Police deployment is an executive home department function, not a legal officer's role.", "தவறு. காவல் துறையை நிலைநிறுத்துவது உள்துறையின் நிர்வாகப் பணி, சட்ட அதிகாரியின் பங்கு அல்ல.",
        "Incorrect. Altering state boundaries under Article 3 is an exclusive power of Parliament by law.", "தவறு. உறுப்பு 3-ன் கீழ் மாநில எல்லைகளை மாற்றுவது நாடாளுமன்றத்தின் பிரத்தியேக சட்டமன்ற அதிகாரமாகும்.",
        "Correct. Formulates legal claims and leads the State boundary litigation under Article 131 before the Supreme Court.", "சரி. உச்ச நீதிமன்றத்தில் உறுப்பு 131-ன் கீழ் எல்லை வழக்கில் மாநில சட்டக் கோரிக்கைகளை வடிவமைத்து வாதத்தை வழிநடத்துகிறார்.",
        "Incorrect. Creating or merging Union Territories is a parliamentary function.", "தவறு. யூனியன் பிரதேசங்களை உருவாக்குவது அல்லது இணைப்பது நாடாளுமன்றத்தின் பணியாகும்.",
        "In the Belagavi dispute between Maharashtra and Karnataka, the respective Advocate Generals have spearheaded multi-decade litigation.",
        "மகாராஷ்டிரா மற்றும் கர்நாடகா இடையேயான பெலகாவி சர்ச்சையில், அந்தந்த மாநில அட்வகேட் ஜெனரல்களே பல தசாப்த கால வழக்கை வழிநடத்தியுள்ளனர்.",
        "The Advocate General coordinates with the Boundary Cell in the State Revenue Department to gather archival evidence.",
        "ஆவண ஆதாரங்களைச் சேகரிக்க தலைமை வழக்கறிஞர் மாநில வருவாய்த் துறையின் எல்லைப் பிரிவோடு இணைந்து செயல்படுகிறார்."
    )

    # Q48 (D)
    add_q(
        "ADVG_M_048", "Special Leave Petition Filing Advice",
        "When an adverse judgment is rendered against the State Government by a Division Bench of the High Court, what is the formal procedure followed by the Advocate General?",
        "உயர் நீதிமன்றத்தின் இரு நீதிபதிகள் கொண்ட அமர்வு மாநில அரசுக்கு எதிராக ஒரு பாதகமான தீர்ப்பை வழங்கும் போது, தலைமை வழக்கறிஞர் பின்பற்றும் முறையான நடைமுறை என்ன?",
        "He orders the High Court to retract its judgment immediately", "உயர் நீதிமன்றம் தனது தீர்ப்பை உடனடியாக திரும்பப் பெற வேண்டும் என்று அவர் உத்தரவிடுகிறார்",
        "He issues an ordinance nullifying the judgment within 24 hours", "24 மணி நேரத்திற்குள் தீர்ப்பை ரத்து செய்யும் அவசரச் சட்டத்தை அவர் பிறப்பிக்கிறார்",
        "He files an appeal before the Governor for executive cancellation", "நிர்வாக ரத்துக்காக ஆளுநரிடம் அவர் மேல்முறையீடு செய்கிறார்",
        "He renders a written legal opinion analyzing the merits of the judgment and advising the State whether to file a Special Leave Petition (SLP) under Article 136 in the Supreme Court", "தீர்ப்பின் சட்ட நுணுக்கங்களை ஆய்வு செய்து, உச்ச நீதிமன்றத்தில் உறுப்பு 136-ன் கீழ் சிறப்பு விடுப்பு மனு (SLP) தாக்கல் செய்யலாமா என்பது குறித்து மாநில அரசுக்கு எழுத்துப்பூர்வ சட்ட ஆலோசனையை வழங்குகிறார்",
        "D",
        "When the State loses a matter in the High Court, the concerned department sends the certified copy of the judgment to the Advocate General. The AG examines whether there is a substantial question of law or miscarriage of justice and submits a formal legal opinion advising whether an SLP under Article 136 should be preferred in the Supreme Court.",
        "உயர் நீதிமன்றத்தில் அரசு வழக்கில் தோற்கும் போது, சம்பந்தப்பட்ட துறை தீர்ப்பின் சான்றளிக்கப்பட்ட நகலை தலைமை வழக்கறிஞருக்கு அனுப்புகிறது. முக்கிய சட்ட வினா உள்ளதா அல்லது நீதி வழுவியுள்ளதா என்பதை ஆராய்ந்து, உச்ச நீதிமன்றத்தில் உறுப்பு 136-ன் கீழ் SLP தாக்கல் செய்யலாமா என்பது குறித்து AG முறையான சட்ட ஆலோசனையை வழங்குகிறார்.",
        "Incorrect. Law officers cannot order courts to retract judgments.", "தவறு. தீர்ப்புகளை திரும்பப் பெற நீதிமன்றங்களுக்கு சட்ட அதிகாரிகளால் உத்தரவிட முடியாது.",
        "Incorrect. Ordinances are promulgated by the Governor under Article 213, not by the AG.", "தவறு. அவசரச் சட்டங்கள் உறுப்பு 213-ன் கீழ் ஆளுநரால் பிறப்பிக்கப்படுகின்றன, AG-யால் அல்ல.",
        "Incorrect. The Governor has no appellate judicial power over High Court judgments.", "தவறு. உயர் நீதிமன்றத் தீர்ப்புகள் மீது ஆளுநருக்கு எந்த மேல்முறையீட்டு அதிகாரமும் இல்லை.",
        "Correct. Renders formal legal opinion on the feasibility and grounds for filing an SLP under Article 136.", "சரி. உறுப்பு 136-ன் கீழ் SLP தாக்கல் செய்வதற்கான சாத்தியக்கூறுகள் மற்றும் காரணங்கள் குறித்து முறையான சட்ட ஆலோசனையை வழங்குகிறார்.",
        "If the Advocate General advises that the judgment is sound on facts and law, the State usually complies with the order.",
        "தீர்ப்பு சட்டப்படி சரியானது என்று தலைமை வழக்கறிஞர் ஆலோசனை கூறினால், அரசு வழக்கமாக அந்த உத்தரவை நடைமுறைப்படுத்துகிறது.",
        "This prevents wasteful expenditure on unmerited litigation before the apex court.",
        "இது உச்ச நீதிமன்றத்தில் தகுதியற்ற வழக்குகளில் அரசு நிதி வீணாவதைத் தடுக்கிறது."
    )

    # Q49 (A)
    add_q(
        "ADVG_M_049", "Section 92 CPC Leave Mechanism",
        "In a suit regarding public charities under Section 92 of the CPC, what is the primary purpose of requiring the Advocate General's consent (or court leave)?",
        "சிவில் நடைமுறைச் சட்டம் பிரிவு 92-ன் கீழ் பொது அறக்கட்டளைகள் தொடர்பான வழக்கில், தலைமை வழக்கறிஞரின் இசைவு (அல்லது நீதிமன்ற அனுமதி) தேவைப்படுவதன் முதன்மை நோக்கம் என்ன?",
        "To prevent public charitable trusts from being harassed by frivolous and malicious suits brought by busybodies with ulterior motives", "உள்நோக்கம் கொண்ட வீணான நபர்களால் தொடரப்படும் பழிவாங்கும் வழக்குகளால் பொது அறக்கட்டளைகள் துன்புறுத்தப்படுவதைத் தடுப்பது",
        "To allow the Advocate General to take over ownership of the trust properties", "அறக்கட்டளை சொத்துக்களின் உரிமையை தலைமை வழக்கறிஞர் தனது கட்டுப்பாட்டில் எடுக்க அனுமதிப்பது",
        "To dissolve all public charities and merge them into the State treasury", "அனைத்து பொது அறக்கட்டளைகளையும் கலைத்து அரசு கருவூலத்தில் இணைப்பது",
        "To appoint government officials as trustees of all religious temples", "அனைத்து சமயக் கோயில்களின் அறங்காவலர்களாக அரசு அதிகாரிகளை நியமிப்பது",
        "A",
        "Section 92 of the CPC is designed to protect public trusts from mismanagement while simultaneously shielding genuine trustees from vexatious litigation. The requirement of obtaining the Advocate General's consent (or the leave of the court) acts as a protective shield against speculative and harassing suits.",
        "CPC பிரிவு 92 பொது அறக்கட்டளைகள் தவறாக நிர்வகிக்கப்படுவதில் இருந்து பாதுகாப்பதோடு, அதே நேரத்தில் உண்மையான அறங்காவலர்கள் வீண் வழக்குகளால் துன்புறுத்தப்படுவதில் இருந்தும் பாதுகாக்கும் வகையில் வடிவமைக்கப்பட்டுள்ளது. தலைமை வழக்கறிஞரின் இசைவு (அல்லது நீதிமன்ற அனுமதி) வீண் வழக்குகளுக்கு எதிரான ஒரு பாதுகாப்புக் கவசமாக செயல்படுகிறது.",
        "Correct. Acts as a protective filter preventing harassment of genuine public trusts by malicious litigants.", "சரி. தீய நோக்கம் கொண்ட வழக்காடிகளால் உண்மையான பொது அறக்கட்டளைகள் துன்புறுத்தப்படுவதைத் தடுக்கும் பாதுகாப்புக் கவசமாக செயல்படுகிறது.",
        "Incorrect. Section 92 does not confer ownership of trust properties on the AG.", "தவறு. பிரிவு 92 அறக்கட்டளை சொத்துக்களின் உரிமையை AG-க்கு வழங்கவில்லை.",
        "Incorrect. Section 92 preserves charities, not dissolves them.", "தவறு. பிரிவு 92 தொண்டு நிறுவனங்களைப் பாதுகாக்கிறது, கலைப்பதில்லை.",
        "Incorrect. Religious endowment appointments are governed by specific state legislation, not Section 92 CPC.", "தவறு. சமய அறநிலைய நியமனங்கள் குறிப்பிட்ட மாநில சட்டங்களால் நிர்வகிக்கப்படுகின்றன, CPC பிரிவு 92-ஆல் அல்ல.",
        "The Advocate General exercises this parens patriae power to ensure the trust's public charitable objects are fulfilled.",
        "அறக்கட்டளையின் பொது தொண்டு நோக்கங்கள் நிறைவேற்றப்படுவதை உறுதி செய்ய தலைமை வழக்கறிஞர் இந்த 'பெற்றோர் போன்ற' (parens patriae) அதிகாரத்தைப் பயன்படுத்துகிறார்.",
        "In 1976, the CPC was amended to allow two or more interested persons to obtain 'leave of the court' directly if the AG consent route is bypassed.",
        "1976-ல், AG இசைவு முறைக்கு மாற்றாக ஆர்வமுள்ள இருவர் நேரடியாக 'நீதிமன்ற அனுமதியைப்' பெறவும் CPC திருத்தப்பட்டது."
    )

    # Q50 (B)
    add_q(
        "ADVG_M_050", "Medium Conceptual Synthesis",
        "Which of the following statements correctly synthesizes the constitutional nature of the Advocate General of a State?",
        "மாநில தலைமை வழக்கறிஞரின் அரசியலமைப்புத் தன்மையை பின்வரும் கூற்றுகளில் எது சரியாக ஒருங்கிணைத்து விளக்குகிறது?",
        "The Advocate General is an elected political executive holding cabinet rank with full legislative voting rights", "தலைமை வழக்கறிஞர் முழு சட்டமன்ற வாக்குரிமையுடன் கூடிய அமைச்சரவை அந்தஸ்தைக் கொண்ட தேர்ந்தெடுக்கப்பட்ட அரசியல் நிர்வாகி ஆவார்",
        "The Advocate General is an independent constitutional functionary under Article 165 who serves as the chief legal adviser to the State, represents it before courts, and participates in legislative debates without voting, holding office during the Governor's pleasure", "தலைமை வழக்கறிஞர் உறுப்பு 165-ன் கீழ் ஒரு சுதந்திரமான அரசியலமைப்புப் பொறுப்பாளர் ஆவார், இவர் மாநிலத்தின் முதன்மை சட்ட ஆலோசகராக செயல்படுகிறார், நீதிமன்றங்களில் அரசைப் பிரதிநிதித்துவப்படுத்துகிறார், வாக்களிக்கும் உரிமையின்றி சட்டமன்ற விவாதங்களில் பங்கேற்கிறார் மற்றும் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார்",
        "The Advocate General is a permanent judicial officer subordinate to the High Court Chief Justice with guaranteed tenure until age 65", "தலைமை வழக்கறிஞர் 65 வயது வரை உத்தரவாதமான பதவிக்காலத்துடன் உயர் நீதிமன்ற தலைமை நீதிபதிக்குக் கீழ் உள்ள நிரந்தர நீதித்துறை அதிகாரி ஆவார்",
        "The Advocate General is a civil servant recruited by the State Public Service Commission under Article 315", "தலைமை வழக்கறிஞர் உறுப்பு 315-ன் கீழ் மாநில அரசுப் பணியாளர் தேர்வாணையத்தால் தேர்ந்தெடுக்கப்படும் ஓர் அரசு ஊழியர் ஆவார்",
        "B",
        "Statement B captures all essential constitutional characteristics of the Advocate General: constitutional origin (Art 165), chief legal adviser to the State Government, representative before courts, non-voting participant in the Legislature (Art 177), and tenure during the pleasure of the Governor (Art 165(3)).",
        "கூற்று B தலைமை வழக்கறிஞரின் அனைத்து அத்தியாவசிய அரசியலமைப்பு அம்சங்களையும் உள்ளடக்கியுள்ளது: அரசியலமைப்பு தோற்றம் (உறுப்பு 165), மாநில அரசின் முதன்மை சட்ட ஆலோசகர், நீதிமன்றப் பிரதிநிதி, சட்டமன்றத்தில் வாக்களிக்காத பங்கேற்பாளர் (உறுப்பு 177), மற்றும் ஆளுநரின் விருப்பத்திற்கு உட்பட்ட பதவிக்காலம் (உறுப்பு 165(3)).",
        "Incorrect. He is not an elected politician and has no voting rights.", "தவறு. அவர் தேர்ந்தெடுக்கப்பட்ட அரசியல்வாதி அல்ல மற்றும் வாக்குரிமை அற்றவர்.",
        "Correct. Comprehensive and accurate synthesis of the Advocate General's constitutional status.", "சரி. தலைமை வழக்கறிஞரின் அரசியலமைப்பு அந்தஸ்தின் விரிவான மற்றும் துல்லியமான ஒருங்கிணைப்பு.",
        "Incorrect. He is not a judicial officer and has no 65-year guaranteed tenure.", "தவறு. அவர் நீதித்துறை அதிகாரி அல்ல மற்றும் 65 வயது உத்தரவாத பதவிக்காலம் கிடையாது.",
        "Incorrect. Not recruited by TNPSC/SPSC; appointed by the Governor under Article 165.", "தவறு. TNPSC-ஆல் தேர்ந்தெடுக்கப்படுபவர் அல்ல; உறுப்பு 165-ன் கீழ் ஆளுநரால் நியமிக்கப்படுபவர்.",
        "This balanced synthesis covers the three core dimensions: Advisory role, Litigation role, and Legislative role.",
        "இந்த சமநிலையான ஒருங்கிணைப்பு மூன்று முக்கிய பரிமாணங்களை உள்ளடக்கியது: ஆலோசனைப் பங்கு, வழக்காடும் பங்கு மற்றும் சட்டமன்றப் பங்கு.",
        "Understanding this multifaceted role is essential for mastering TNPSC Group 1 and Group 2 mains and prelims.",
        "இந்த பன்முகப் பங்கை புரிந்துகொள்வது டிஎன்பிஎஸ்சி குரூப் 1 மற்றும் குரூப் 2 முதல்நிலை மற்றும் முதன்மைத் தேர்வுகளுக்கு மிகவும் அவசியமானது."
    )

    return qs

def main():
    questions = get_medium_questions()
    print(f"Total Medium questions generated: {len(questions)}")
    
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "advocate_general_medium.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")
    
    # Validate file
    validator = ContentValidator()
    report = validator.validate_file(out_file, expected_count=50, expected_prefix="ADVG_M_")
    print(f"Validation Result: {'PASS' if report.is_valid else 'FAIL'} | Audited: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
    if not report.is_valid:
        for iss in report.issues:
            print("Issue:", iss.severity, iss.field, iss.message)

if __name__ == "__main__":
    main()
