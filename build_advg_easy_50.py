# -*- coding: utf-8 -*-
"""
Builder for Advocate General of a State - Easy Level (50 MCQs: ADVG_E_001 to ADVG_E_050).
Strict 24-field schema, fully bilingual, high-yield TNPSC standards.
Target Key Distribution: ~12-13 each of A, B, C, D.
"""
import json
import os
from advg_mcq_helper import make_advg_q
from tools.nova_content_engine.validator import ContentValidator

def get_easy_questions():
    qs = []
    
    # Template helper
    def add_q(qid, subtopic, en_stem, ta_stem,
              en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
              correct_key, exp_en, exp_ta,
              why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
              tip_en, tip_ta, fact_en, fact_ta):
        qs.append(make_advg_q(
            qid=qid, diff="Easy", qtype="Single Choice", subtopic=subtopic,
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
        "ADVG_E_001", "Constitutional Basis",
        "Which Article of the Constitution of India provides for the office of the Advocate General of a State?",
        "இந்திய அரசியலமைப்பின் எந்த உறுப்பு மாநில தலைமை வழக்கறிஞர் அலுவலகத்தை வழங்குகிறது?",
        "Article 165", "உறுப்பு 165",
        "Article 76", "உறுப்பு 76",
        "Article 177", "உறுப்பு 177",
        "Article 194", "உறுப்பு 194",
        "A",
        "Article 165 in Part VI of the Constitution explicitly provides for the office of the Advocate General for each State.",
        "அரசியலமைப்பின் பகுதி VI-ல் உள்ள உறுப்பு 165 ஒவ்வொரு மாநிலத்திற்கும் தலைமை வழக்கறிஞர் பதவியை தெளிவாக வழங்குகிறது.",
        "Correct. Article 165 provides for the Advocate General for the State.", "சரி. உறுப்பு 165 மாநில தலைமை வழக்கறிஞரை வழங்குகிறது.",
        "Incorrect. Article 76 provides for the Attorney General of India.", "தவறு. உறுப்பு 76 இந்திய தலைமை வழக்கறிஞரை வழங்குகிறது.",
        "Incorrect. Article 177 deals with rights of Ministers and Advocate General in State Legislature.", "தவறு. உறுப்பு 177 சட்டமன்றத்தில் அமைச்சர்கள் மற்றும் தலைமை வழக்கறிஞரின் உரிமைகள் பற்றியது.",
        "Incorrect. Article 194 deals with powers and privileges of State Legislatures and their members.", "தவறு. உறுப்பு 194 சட்டமன்றங்கள் மற்றும் அவற்றின் உறுப்பினர்களின் அதிகாரங்கள் மற்றும் சிறப்புரிமைகள் பற்றியது.",
        "Remember: Art 76 = Union (Attorney General), Art 165 = State (Advocate General).",
        "நினைவில் கொள்க: உறுப்பு 76 = ஒன்றியம் (அட்டர்னி ஜெனரல்), உறுப்பு 165 = மாநிலம் (அட்வகேட் ஜெனரல்).",
        "Article 165 is located in Part VI (The States) of the Indian Constitution.",
        "உறுப்பு 165 இந்திய அரசியலமைப்பின் பகுதி VI-ல் (மாநிலங்கள்) அமைந்துள்ளது."
    )

    # Q2 (B)
    add_q(
        "ADVG_E_002", "Appointment Authority",
        "Who appoints the Advocate General of a State in India?",
        "இந்தியாவில் ஒரு மாநிலத்தின் தலைமை வழக்கறிஞரை நியமிப்பவர் யார்?",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "The Governor of the State", "மாநில ஆளுநர்",
        "The Chief Justice of the High Court", "உயர் நீதிமன்றத் தலைமை நீதிபதி",
        "The Chief Minister of the State", "மாநில முதலமைச்சர்",
        "B",
        "Under Article 165(1), the Governor of each State appoints a person who is qualified to be appointed as a Judge of a High Court to be Advocate General for the State.",
        "உறுப்பு 165(1)-ன் கீழ், உயர் நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுள்ள ஒருவரை மாநில ஆளுநர் தலைமை வழக்கறிஞராக நியமிக்கிறார்.",
        "Incorrect. The President appoints the Attorney General of India, not the Advocate General of a State.", "தவறு. குடியரசுத் தலைவர் அட்டர்னி ஜெனரலை நியமிக்கிறார், அட்வகேட் ஜெனரலை அல்ல.",
        "Correct. The Governor appoints the Advocate General under Article 165(1).", "சரி. உறுப்பு 165(1)-ன் கீழ் ஆளுநர் தலைமை வழக்கறிஞரை நியமிக்கிறார்.",
        "Incorrect. The High Court Chief Justice has no constitutional role in appointing the Advocate General.", "தவறு. அட்வகேட் ஜெனரல் நியமனத்தில் உயர் நீதிமன்ற தலைமை நீதிபதிக்கு அரசியலமைப்பு பங்கு இல்லை.",
        "Incorrect. The Governor makes the formal appointment, though on the advice of the State Cabinet headed by the Chief Minister.", "தவறு. முதலமைச்சர் தலைமையிலான அமைச்சரவையின் ஆலோசனையின்படி ஆளுநரே முறையான நியமனத்தை செய்கிறார்.",
        "The Governor appoints the Advocate General on the aid and advice of the Council of Ministers headed by the CM.",
        "முதலமைச்சர் தலைமையிலான அமைச்சரவையின் ஆலோசனையின் பேரில் ஆளுநர் தலைமை வழக்கறிஞரை நியமிக்கிறார்.",
        "Appointment of Advocate General is an executive act under Article 165(1).",
        "தலைமை வழக்கறிஞர் நியமனம் உறுப்பு 165(1)-ன் கீழ் ஒரு நிர்வாக நடவடிக்கையாகும்."
    )

    # Q3 (C)
    add_q(
        "ADVG_E_003", "Qualifications",
        "To be appointed as the Advocate General of a State, a person must be qualified to be appointed as a:",
        "ஒரு மாநிலத்தின் தலைமை வழக்கறிஞராக நியமிக்கப்படுவதற்கு, ஒருவர் எப்பதவிக்கு நியமிக்கப்பட தகுதியுடையவராக இருக்க வேண்டும்?",
        "Judge of the Supreme Court", "உச்ச நீதிமன்ற நீதிபதி",
        "District Judge", "மாவட்ட நீதிபதி",
        "Judge of a High Court", "உயர் நீதிமன்ற நீதிபதி",
        "Senior Advocate of Bar Council of India", "இந்திய பார் கவுன்சிலின் மூத்த வழக்கறிஞர்",
        "C",
        "Article 165(1) states that the person appointed as Advocate General must be qualified to be appointed as a Judge of a High Court.",
        "உறுப்பு 165(1) தலைமை வழக்கறிஞராக நியமிக்கப்படும் நபர் உயர் நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுடையவராக இருக்க வேண்டும் என்று கூறுகிறது.",
        "Incorrect. Supreme Court Judge qualification applies to the Attorney General of India (Article 76(1)).", "தவறு. உச்ச நீதிமன்ற நீதிபதி தகுதி இந்திய அட்டர்னி ஜெனரலுக்குப் பொருந்தும் (உறுப்பு 76(1)).",
        "Incorrect. District Judge qualification is lower than the constitutional requirement of HC Judge.", "தவறு. மாவட்ட நீதிபதி தகுதி உயர் நீதிமன்ற நீதிபதி என்ற அரசியலமைப்பு தேவையை விட குறைவானது.",
        "Correct. Must be qualified to be appointed as a Judge of a High Court.", "சரி. உயர் நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுடையவராக இருக்க வேண்டும்.",
        "Incorrect. Senior Advocate designation alone is not the constitutional benchmark.", "தவறு. மூத்த வழக்கறிஞர் அந்தஸ்து மட்டுமே அரசியலமைப்பு தகுதி வரம்பாகாது.",
        "Compare: AG = HC Judge qualifications; Attorney General = Supreme Court Judge qualifications.",
        "ஒப்பிடுக: அட்வகேட் ஜெனரல் = உயர் நீதிமன்ற நீதிபதி தகுதி; அட்டர்னி ஜெனரல் = உச்ச நீதிமன்ற நீதிபதி தகுதி.",
        "The qualifications for HC judge are prescribed in Article 217(2).",
        "உயர் நீதிமன்ற நீதிபதிக்கான தகுதிகள் உறுப்பு 217(2)-ல் குறிப்பிடப்பட்டுள்ளன."
    )

    # Q4 (D)
    add_q(
        "ADVG_E_004", "Tenure",
        "What is the tenure of office of the Advocate General of a State as prescribed by the Constitution?",
        "அரசியலமைப்பால் நிர்ணயிக்கப்பட்ட மாநில தலைமை வழக்கறிஞரின் பதவிக்காலம் என்ன?",
        "5 years", "5 ஆண்டுகள்",
        "6 years or up to 65 years of age", "6 ஆண்டுகள் அல்லது 65 வயது வரை",
        "3 years", "3 ஆண்டுகள்",
        "Not fixed by the Constitution; holds office during the pleasure of the Governor", "அரசியலமைப்பால் நிர்ணயிக்கப்படவில்லை; ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிப்பார்",
        "D",
        "Article 165(3) specifies that the Advocate General holds office during the pleasure of the Governor. The Constitution does not fix a term.",
        "உறுப்பு 165(3) தலைமை வழக்கறிஞர் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிப்பார் என்று குறிப்பிடுகிறது. அரசியலமைப்பு எந்தக் குறிப்பிட்ட காலத்தையும் நிர்ணயிக்கவில்லை.",
        "Incorrect. 5 years is not fixed by the Constitution.", "தவறு. 5 ஆண்டுகள் அரசியலமைப்பால் நிர்ணயிக்கப்படவில்லை.",
        "Incorrect. 6 years / 65 years is typical for CAG or PSC members, not Advocate General.", "தவறு. 6 ஆண்டுகள் / 65 வயது என்பது CAG அல்லது PSC உறுப்பினர்களுக்கு உரியது, அட்வகேட் ஜெனரலுக்கு அல்ல.",
        "Incorrect. 3 years is not a constitutional tenure.", "தவறு. 3 ஆண்டுகள் அரசியலமைப்பு பதவிக்காலம் அல்ல.",
        "Correct. The Constitution does not fix any specific tenure; tenure depends on the pleasure of the Governor.", "சரி. அரசியலமைப்பு எந்த ஒரு குறிப்பிட்ட பதவிக்காலத்தையும் நிர்ணயிக்கவில்லை; ஆளுநரின் விருப்பத்திற்கு உட்பட்டது.",
        "Tenure during the 'pleasure of the Governor' means the AG conventionally resigns when the government resigns.",
        "'ஆளுநரின் விருப்பம் வரை' என்பது நடைமுறையில் அரசு பதவி விலகும்போது தலைமை வழக்கறிஞரும் பதவி விலகுவார் என்பதாகும்.",
        "Conventionally, the Advocate General resigns when the Council of Ministers which recommended his appointment resigns.",
        "வழக்கமாக, தனது நியமனத்தைப் பரிந்துரைத்த அமைச்சரவை பதவி விலகும்போது தலைமை வழக்கறிஞரும் பதவி விலகுவார்."
    )

    # Q5 (A)
    add_q(
        "ADVG_E_005", "Highest Law Officer",
        "Who is the highest law officer in a State in India?",
        "இந்தியாவில் ஒரு மாநிலத்தின் மிக உயர்ந்த சட்ட அதிகாரி யார்?",
        "Advocate General of the State", "மாநில தலைமை வழக்கறிஞர் (அட்வகேட் ஜெனரல்)",
        "Law Minister of the State", "மாநில சட்ட அமைச்சர்",
        "Chief Justice of the High Court", "உயர் நீதிமன்ற தலைமை நீதிபதி",
        "Director General of Police", "காவல்துறை தலைமை இயக்குநர்",
        "A",
        "The Advocate General is the first and highest law officer of the State, corresponding to the Attorney General at the Union level.",
        "ஒன்றிய அளவில் அட்டர்னி ஜெனரலைப் போலவே, மாநில அளவில் தலைமை வழக்கறிஞரே முதன்மை மற்றும் மிக உயர்ந்த சட்ட அதிகாரி ஆவார்.",
        "Correct. The Advocate General is the highest law officer of the State.", "சரி. மாநில தலைமை வழக்கறிஞரே மாநிலத்தின் மிக உயர்ந்த சட்ட அதிகாரி ஆவார்.",
        "Incorrect. The Law Minister is a political executive, not the constitutional law officer.", "தவறு. சட்ட அமைச்சர் ஓர் அரசியல் நிர்வாகி, அரசியலமைப்பு சட்ட அதிகாரி அல்ல.",
        "Incorrect. The Chief Justice is the head of the State Judiciary, not a government law officer.", "தவறு. தலைமை நீதிபதி மாநில நீதித்துறையின் தலைவர், அரசு சட்ட அதிகாரி அல்ல.",
        "Incorrect. DGP is the head of the police force, not a legal officer.", "தவறு. டிஜிபி காவல் துறையின் தலைவர், சட்ட அதிகாரி அல்ல.",
        "Advocate General = Highest Law Officer of State; Attorney General = Highest Law Officer of India.",
        "அட்வகேட் ஜெனரல் = மாநிலத்தின் தலைமை சட்ட அதிகாரி; அட்டர்னி ஜெனரல் = இந்தியாவின் தலைமை சட்ட அதிகாரி.",
        "The Advocate General represents the State Government in legal matters and advises on legal questions.",
        "தலைமை வழக்கறிஞர் சட்ட விவகாரங்களில் மாநில அரசைப் பிரதிநிதித்துவப்படுத்துகிறார் மற்றும் சட்ட ஆலோசனைகளை வழங்குகிறார்."
    )

    # Q6 (B)
    add_q(
        "ADVG_E_006", "Right to Speak in Legislature",
        "Under which Article does the Advocate General have the right to speak and take part in the proceedings of the State Legislature?",
        "எந்த உறுப்பின் கீழ் மாநில சட்டமன்ற நடவடிக்கைகளில் பேசவும் பங்கேற்கவும் தலைமை வழக்கறிஞருக்கு உரிமை உண்டு?",
        "Article 88", "உறுப்பு 88",
        "Article 177", "உறுப்பு 177",
        "Article 194", "உறுப்பு 194",
        "Article 213", "உறுப்பு 213",
        "B",
        "Article 177 grants the Advocate General the right to speak and take part in the proceedings of both Houses of the State Legislature (where bicameral) or any legislative committee of which he is named a member.",
        "உறுப்பு 177 தலைமை வழக்கறிஞருக்கு மாநில சட்டமன்றத்தின் இரு அவைகளிலும் (ஈரவை உள்ள இடங்களில்) அல்லது அவர் உறுப்பினராக பெயரிடப்பட்ட சட்டமன்றக் குழுவிலும் பேசவும் பங்கேற்கவும் உரிமையளிக்கிறது.",
        "Incorrect. Article 88 gives similar rights to the Attorney General in Parliament.", "தவறு. உறுப்பு 88 நாடாளுமன்றத்தில் அட்டர்னி ஜெனரலுக்கு இதேபோன்ற உரிமைகளை வழங்குகிறது.",
        "Correct. Article 177 gives the Advocate General rights in the State Legislature.", "சரி. உறுப்பு 177 மாநில சட்டமன்றத்தில் தலைமை வழக்கறிஞருக்கு உரிமைகளை வழங்குகிறது.",
        "Incorrect. Article 194 deals with powers, privileges, and immunities.", "தவறு. உறுப்பு 194 அதிகாரங்கள், சிறப்புரிமைகள் மற்றும் விலக்களிப்புகள் பற்றியது.",
        "Incorrect. Article 213 deals with Governor's ordinance-making power.", "தவறு. உறுப்பு 213 ஆளுநரின் அவசரச் சட்டம் பிறப்பிக்கும் அதிகாரம் பற்றியது.",
        "Rule of thumb: Union rights = Art 88; State rights = Art 177 (difference of 89).",
        "விதி: ஒன்றிய உரிமைகள் = உறுப்பு 88; மாநில உரிமைகள் = உறுப்பு 177 (89 வித்தியாசம்).",
        "Under Article 177, the Advocate General cannot vote in the State Legislature.",
        "உறுப்பு 177-ன் கீழ் தலைமை வழக்கறிஞருக்கு சட்டமன்றத்தில் வாக்களிக்கும் உரிமை கிடையாது."
    )

    # Q7 (C)
    add_q(
        "ADVG_E_007", "Voting Rights Bar",
        "Does the Advocate General of a State have the right to vote in the State Legislative Assembly?",
        "மாநில சட்டப் பேரவையில் வாக்களிக்கும் உரிமை மாநில தலைமை வழக்கறிஞருக்கு உண்டா?",
        "Yes, on all bills", "ஆம், அனைத்து மசோதாக்களிலும் உண்டு",
        "Yes, but only in case of a tie (casting vote)", "ஆம், ஆனால் சமநிலை ஏற்படும் போது மட்டுமே (முடிவு வாக்கு)",
        "No, he has no right to vote under any circumstances", "இல்லை, எச்சூழலிலும் அவருக்கு வாக்களிக்கும் உரிமை இல்லை",
        "Yes, but only on constitutional amendment bills", "ஆம், ஆனால் அரசியலமைப்பு திருத்த மசோதாக்களில் மட்டுமே",
        "C",
        "Article 177 expressly states that the Advocate General shall not by virtue of this article be entitled to vote.",
        "உறுப்பு 177 இவ்வுறுப்பின் காரணமாக தலைமை வழக்கறிஞர் வாக்களிக்க உரிமை பெறமாட்டார் என்று வெளிப்படையாகக் கூறுகிறது.",
        "Incorrect. He has no voting rights on any bill.", "தவறு. எந்த மசோதாவிலும் அவருக்கு வாக்களிக்கும் உரிமை இல்லை.",
        "Incorrect. The Speaker exercises casting vote, not the Advocate General.", "தவறு. சபாநாயகரே முடிவு வாக்கை செலுத்துகிறார், தலைமை வழக்கறிஞர் அல்ல.",
        "Correct. There is an absolute constitutional prohibition against the Advocate General voting.", "சரி. தலைமை வழக்கறிஞர் வாக்களிப்பதற்கு அரசியலமைப்பில் முழுமையான தடை உள்ளது.",
        "Incorrect. He cannot vote on constitutional or ordinary bills.", "தவறு. அவரால் அரசியலமைப்பு திருத்த மசோதாவிலோ அல்லது சாதாரண மசோதாவிலோ வாக்களிக்க முடியாது.",
        "Remember: Both the AG at Union (Art 88) and Advocate General at State (Art 177) can speak and take part, but CANNOT vote.",
        "நினைவில் கொள்க: ஒன்றிய அட்டர்னி ஜெனரல் (உறுப்பு 88) மற்றும் மாநில அட்வகேட் ஜெனரல் (உறுப்பு 177) இருவரும் பேசலாம், பங்கேற்கலாம், ஆனால் வாக்களிக்க முடியாது.",
        "The right to vote belongs exclusively to elected/nominated members of the House.",
        "வாக்களிக்கும் உரிமை அவையின் தேர்ந்தெடுக்கப்பட்ட/நியமிக்கப்பட்ட உறுப்பினர்களுக்கு மட்டுமே உரியது."
    )

    # Q8 (D)
    add_q(
        "ADVG_E_008", "Remuneration",
        "Who determines the remuneration of the Advocate General of a State?",
        "மாநில தலைமை வழக்கறிஞரின் ஊதியத்தை தீர்மானிப்பவர் யார்?",
        "The State Legislative Assembly by law", "சட்டமன்றப் பேரவை சட்டத்தின் மூலம்",
        "The High Court Chief Justice", "உயர் நீதிமன்ற தலைமை நீதிபதி",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "The Governor of the State", "மாநில ஆளுநர்",
        "D",
        "Under Article 165(3), the Advocate General receives such remuneration as the Governor may determine.",
        "உறுப்பு 165(3)-ன் படி, ஆளுநர் தீர்மானிக்கும் ஊதியத்தை தலைமை வழக்கறிஞர் பெறுவார்.",
        "Incorrect. The State Legislature does not fix the Advocate General's remuneration by law.", "தவறு. மாநில சட்டமன்றம் சட்டத்தின் மூலம் தலைமை வழக்கறிஞரின் ஊதியத்தை நிர்ணயிப்பதில்லை.",
        "Incorrect. High Court Chief Justice has no role in determining AG's remuneration.", "தவறு. தலைமை வழக்கறிஞரின் ஊதியத்தை நிர்ணயிப்பதில் உயர் நீதிமன்ற தலைமை நீதிபதிக்கு எந்தப் பங்கும் இல்லை.",
        "Incorrect. The President determines the Attorney General's remuneration, not the Advocate General's.", "தவறு. குடியரசுத் தலைவர் அட்டர்னி ஜெனரலின் ஊதியத்தை தீர்மானிக்கிறார், அட்வகேட் ஜெனரலின் ஊதியத்தை அல்ல.",
        "Correct. Article 165(3) states that the Governor determines the remuneration.", "சரி. உறுப்பு 165(3) ஆளுநரே ஊதியத்தை தீர்மானிக்கிறார் என்று கூறுகிறது.",
        "AG remuneration is not fixed by the Constitution nor charged on the Consolidated Fund.",
        "தலைமை வழக்கறிஞரின் ஊதியம் அரசியலமைப்பால் நிர்ணயிக்கப்படவில்லை மற்றும் ஒருங்கிணைந்த நிதியிலிருந்து சுமத்தப்பட்ட செலவினமும் அல்ல.",
        "The remuneration of the Advocate General is an executive determination under Article 165(3).",
        "தலைமை வழக்கறிஞரின் ஊதியம் உறுப்பு 165(3)-ன் கீழ் ஒரு நிர்வாக முடிவாகும்."
    )

    # Q9 (A)
    add_q(
        "ADVG_E_009", "Resignation",
        "To whom does the Advocate General of a State submit his resignation?",
        "மாநில தலைமை வழக்கறிஞர் தனது பதவி விலகல் கடிதத்தை யாரிடம் சமர்ப்பிக்கிறார்?",
        "The Governor of the State", "மாநில ஆளுநர்",
        "The Chief Minister of the State", "மாநில முதலமைச்சர்",
        "The Chief Justice of the High Court", "உயர் நீதிமன்ற தலைமை நீதிபதி",
        "The Speaker of the Legislative Assembly", "சட்டப் பேரவைத் தலைவர் (சபாநாயகர்)",
        "A",
        "Since the Governor is the appointing authority, the Advocate General addresses his resignation letter to the Governor.",
        "ஆளுநரே நியமன அதிகாரி என்பதால், தலைமை வழக்கறிஞர் தனது பதவி விலகல் கடிதத்தை ஆளுநருக்கே அனுப்புகிறார்.",
        "Correct. The Advocate General submits his resignation to the Governor.", "சரி. தலைமை வழக்கறிஞர் தனது பதவி விலகல் கடிதத்தை ஆளுநரிடம் சமர்ப்பிக்கிறார்.",
        "Incorrect. While the CM may receive intimation, formally resignation is addressed to the Governor.", "தவறு. முதல்வருக்கு தகவல் தெரிவிக்கப்பட்டாலும், முறையாக ஆளுநரிடமே சமர்ப்பிக்கப்பட வேண்டும்.",
        "Incorrect. High Court Chief Justice is judicial head, not appointing authority.", "தவறு. உயர் நீதிமன்ற தலைமை நீதிபதி நீதித்துறைத் தலைவர், நியமன அதிகாரி அல்ல.",
        "Incorrect. The Speaker receives resignations of MLAs, not the Advocate General.", "தவறு. சபாநாயகர் எம்.எல்.ஏக்களின் பதவி விலகலைப் பெறுகிறார், அட்வகேட் ஜெனரலின் கடிதத்தை அல்ல.",
        "Rule: Resignation is always submitted to the constitutional appointing authority (Governor).",
        "விதி: பதவி விலகல் எப்போதும் அரசியலமைப்பு நியமன அதிகாரியிடமே (ஆளுநர்) சமர்ப்பிக்கப்படுகிறது.",
        "Under general administrative law, an officer appointed by the Governor resigns to the Governor.",
        "பொது நிர்வாகச் சட்டத்தின்படி, ஆளுநரால் நியமிக்கப்பட்ட அதிகாரி ஆளுநரிடமே பதவி விலகுகிறார்."
    )

    # Q10 (B)
    add_q(
        "ADVG_E_010", "Privileges and Immunities",
        "Under which Article does the Advocate General enjoy all powers, privileges, and immunities of a member of the State Legislature?",
        "எந்த உறுப்பின் கீழ் மாநில தலைமை வழக்கறிஞர் சட்டமன்ற உறுப்பினரின் அனைத்து அதிகாரங்கள், சிறப்புரிமைகள் மற்றும் விலக்களிப்புகளை அனுபவிக்கிறார்?",
        "Article 105(4)", "உறுப்பு 105(4)",
        "Article 194(4)", "உறுப்பு 194(4)",
        "Article 165(2)", "உறுப்பு 165(2)",
        "Article 202(3)", "உறுப்பு 202(3)",
        "B",
        "Article 194(4) extends the powers, privileges, and immunities of members of a State Legislature to all persons who have the right to speak in and otherwise take part in the proceedings of a House or committee, including the Advocate General.",
        "உறுப்பு 194(4) மாநில சட்டமன்றத்தின் ஓர் அவையில் அல்லது குழுவில் பேசவும் பங்கேற்கவும் உரிமை கொண்ட அனைவருக்கும் (தலைமை வழக்கறிஞர் உட்பட) சட்டமன்ற உறுப்பினரின் அதிகாரங்கள், சிறப்புரிமைகள் மற்றும் விலக்களிப்புகளை நீட்டிக்கிறது.",
        "Incorrect. Article 105(4) applies to the Attorney General of India in Parliament.", "தவறு. உறுப்பு 105(4) நாடாளுமன்றத்தில் இந்திய அட்டர்னி ஜெனரலுக்குப் பொருந்தும்.",
        "Correct. Article 194(4) provides legislative privileges to the Advocate General.", "சரி. உறுப்பு 194(4) தலைமை வழக்கறிஞருக்கு சட்டமன்ற சிறப்புரிமைகளை வழங்குகிறது.",
        "Incorrect. Article 165(2) describes duties of the Advocate General.", "தவறு. உறுப்பு 165(2) தலைமை வழக்கறிஞரின் கடமைகளை விவரிக்கிறது.",
        "Incorrect. Article 202(3) deals with expenditures charged on the Consolidated Fund of the State.", "தவறு. உறுப்பு 202(3) மாநில ஒருங்கிணைந்த நிதியிலிருந்து சுமத்தப்படும் செலவுகள் பற்றியது.",
        "Parallel: Attorney General = Art 105(4); Advocate General = Art 194(4).",
        "இணையான விதி: அட்டர்னி ஜெனரல் = உறுப்பு 105(4); அட்வகேட் ஜெனரல் = உறுப்பு 194(4).",
        "Freedom of speech in the legislature and immunity from court proceedings for statements made are protected under Art 194.",
        "சட்டமன்றத்தில் பேச்சு சுதந்திரம் மற்றும் அங்கு பேசியதற்காக நீதிமன்ற நடவடிக்கைகளிலிருந்து விலக்களிப்பு உறுப்பு 194-ன் கீழ் பாதுகாக்கப்படுகிறது."
    )

    # --- 11 to 20 ---
    # Q11 (C)
    add_q(
        "ADVG_E_011", "Right of Audience",
        "In which courts does the Advocate General have the right of audience in performance of his official duties?",
        "தனது அலுவல் பணிகளைச் செய்வதில் தலைமை வழக்கறிஞருக்கு எந்த நீதிமன்றங்களில் முன்னிலையாகி வாதாடும் உரிமை உண்டு?",
        "Only in the High Court of the State", "மாநில உயர் நீதிமன்றத்தில் மட்டுமே",
        "Only in the Supreme Court of India", "இந்திய உச்ச நீதிமன்றத்தில் மட்டுமே",
        "In any court within the State", "மாநில எல்லைக்குள் உள்ள எந்தவொரு நீதிமன்றத்திலும்",
        "In all courts throughout the territory of India without restriction", "எந்தக் கட்டுப்பாடும் இன்றி இந்திய எல்லைக்குள் உள்ள அனைத்து நீதிமன்றங்களிலும்",
        "C",
        "The Advocate General has the right of audience in any court within the State in performance of his duties, whereas the Attorney General has right of audience in all courts throughout India (Art 76(3)).",
        "அட்டர்னி ஜெனரல் இந்தியா முழுவதும் உள்ள அனைத்து நீதிமன்றங்களிலும் வாதாடும் உரிமை பெற்றிருக்கும் வேளையில் (உறுப்பு 76(3)), தலைமை வழக்கறிஞர் தனது பணிகளைச் செய்வதில் மாநிலத்திற்குள் உள்ள எந்தவொரு நீதிமன்றத்திலும் வாதாடும் உரிமை கொண்டுள்ளார்.",
        "Incorrect. Not restricted solely to the High Court; includes subordinate courts within the State.", "தவறு. உயர் நீதிமன்றத்திற்கு மட்டுமே மட்டுப்படுத்தப்படவில்லை; மாநிலத்தின் கீழ்மை நீதிமன்றங்களும் அடங்கும்.",
        "Incorrect. Advocate General represents the State in the SC when briefed, but right of audience as of constitutional right is within the State.", "தவறு. உச்ச நீதிமன்றத்தில் வாதாட பணிக்கப்படலாம், ஆனால் அரசியலமைப்பு ரீதியான உரிமை மாநில எல்லைக்குள் உள்ளது.",
        "Correct. The Advocate General has the right of audience in any court within the territory of the State.", "சரி. மாநில எல்லைக்குள் உள்ள எந்தவொரு நீதிமன்றத்திலும் வாதாடும் உரிமை தலைமை வழக்கறிஞருக்கு உண்டு.",
        "Incorrect. Audience throughout all courts in India belongs to the Attorney General under Article 76(3).", "தவறு. இந்தியா முழுவதும் உள்ள அனைத்து நீதிமன்றங்களிலும் வாதாடும் உரிமை உறுப்பு 76(3)-ன் கீழ் அட்டர்னி ஜெனரலுக்குரியது.",
        "AG = right of audience within the State; AGI = right of audience across all India.",
        "அட்வகேட் ஜெனரல் = மாநில எல்லைக்குள் உரிமை; அட்டர்னி ஜெனரல் = இந்தியா முழுமைக்குமான உரிமை.",
        "This right of audience ensures the State is represented effectively in any court of first instance or appeal within the State.",
        "இந்த முன்னிலையாகும் உரிமை மாநிலத்திற்குள் எந்த நீதிமன்றத்திலும் அரசு திறம்பட பிரதிநிதித்துவப்படுத்தப்படுவதை உறுதி செய்கிறது."
    )

    # Q12 (D)
    add_q(
        "ADVG_E_012", "Part of Constitution",
        "In which Part of the Indian Constitution is the office of the Advocate General of a State dealt with?",
        "இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் மாநில தலைமை வழக்கறிஞர் அலுவலகம் கையாளப்படுகிறது?",
        "Part IV", "பகுதி IV",
        "Part V", "பகுதி V",
        "Part IX", "பகுதி IX",
        "Part VI", "பகுதி VI",
        "D",
        "The Advocate General is covered in Part VI of the Constitution ('The States'), specifically under Chapter II (The Executive), Article 165.",
        "தலைமை வழக்கறிஞர் அரசியலமைப்பின் பகுதி VI-ல் ('மாநிலங்கள்'), குறிப்பாக அத்தியாயம் II (நிர்வாகம்), உறுப்பு 165-ன் கீழ் கையாளப்படுகிறார்.",
        "Incorrect. Part IV deals with Directive Principles of State Policy.", "தவறு. பகுதி IV அரசு நெறிமுறைக் கோட்பாடுகள் பற்றியது.",
        "Incorrect. Part V deals with the Union (including Attorney General under Art 76).", "தவறு. பகுதி V ஒன்றியம் பற்றியது (உறுப்பு 76-ன் கீழ் அட்டர்னி ஜெனரல் உட்பட).",
        "Incorrect. Part IX deals with The Panchayats.", "தவறு. பகுதி IX பஞ்சாயத்துகள் பற்றியது.",
        "Correct. Part VI covers The States, including the Advocate General under Article 165.", "சரி. பகுதி VI மாநிலங்களை உள்ளடக்கியது, உறுப்பு 165-ன் கீழ் அட்வகேட் ஜெனரல் உட்பட.",
        "Part V = The Union; Part VI = The States.",
        "பகுதி V = ஒன்றியம்; பகுதி VI = மாநிலங்கள்.",
        "Articles 153 to 167 in Part VI deal with the State Executive (Governor, CM, Council of Ministers, and Advocate General).",
        "பகுதி VI-ல் உள்ள உறுப்புகள் 153 முதல் 167 வரை மாநில நிர்வாகத்தைக் கையாள்கின்றன (ஆளுநர், முதலமைச்சர், அமைச்சரவை மற்றும் தலைமை வழக்கறிஞர்)."
    )

    # Q13 (A)
    add_q(
        "ADVG_E_013", "State Executive Component",
        "Which of the following is an integral constitutional part of the State Executive in India?",
        "பின்வருவனவற்றில் இந்தியாவில் மாநில நிர்வாகத்தின் ஒருங்கிணைந்த அரசியலமைப்பு அங்கம் எது?",
        "Advocate General of the State", "மாநில தலைமை வழக்கறிஞர்",
        "State Election Commissioner", "மாநில தேர்தல் ஆணையர்",
        "State Information Commissioner", "மாநில தகவல் ஆணையர்",
        "Chairman of State Human Rights Commission", "மாநில மனித உரிமைகள் ஆணையத்தின் தலைவர்",
        "A",
        "The State Executive under Part VI of the Constitution consists of the Governor, the Chief Minister, the Council of Ministers, and the Advocate General of the State.",
        "அரசியலமைப்பின் பகுதி VI-ன் கீழ் மாநில நிர்வாகம் என்பது ஆளுநர், முதலமைச்சர், அமைச்சரவை மற்றும் மாநில தலைமை வழக்கறிஞரைக் கொண்டுள்ளது.",
        "Correct. The Advocate General is an integral part of the State Executive (Articles 153-167).", "சரி. தலைமை வழக்கறிஞர் மாநில நிர்வாகத்தின் ஒருங்கிணைந்த அங்கம் (உறுப்புகள் 153-167).",
        "Incorrect. State Election Commissioner is an independent constitutional body under Art 243K.", "தவறு. மாநில தேர்தல் ஆணையர் உறுப்பு 243K-ன் கீழ் ஒரு சுதந்திரமான அரசியலமைப்பு அமைப்பு.",
        "Incorrect. State Information Commissioner is a statutory authority under RTI Act 2005.", "தவறு. மாநில தகவல் ஆணையர் RTI சட்டம் 2005-ன் கீழ் ஒரு சட்டப்பூர்வ அதிகாரி.",
        "Incorrect. SHRC Chairman is a statutory authority under Protection of Human Rights Act 1993.", "தவறு. மாநில மனித உரிமைகள் ஆணைய தலைவர் மனித உரிமைகள் பாதுகாப்பு சட்டம் 1993-ன் கீழ் ஒரு சட்டப்பூர்வ அதிகாரி.",
        "State Executive = Governor + Chief Minister + Council of Ministers + Advocate General.",
        "மாநில நிர்வாகம் = ஆளுநர் + முதலமைச்சர் + அமைச்சரவை + தலைமை வழக்கறிஞர்.",
        "Just as the Attorney General is part of the Union Executive, the Advocate General is part of the State Executive.",
        "அட்டர்னி ஜெனரல் ஒன்றிய நிர்வாகத்தின் அங்கமாக இருப்பது போலவே, அட்வகேட் ஜெனரல் மாநில நிர்வாகத்தின் அங்கம் ஆவார்."
    )

    # Q14 (B)
    add_q(
        "ADVG_E_014", "Pre-audience in High Court",
        "Under Section 23 of the Advocates Act, 1961, the Advocate General has the right of pre-audience over:",
        "வழக்கறிஞர்கள் சட்டம் 1961-ன் பிரிவு 23-ன் கீழ், தலைமை வழக்கறிஞர் யாருக்கு மேல் முன்னுரிமை பெற்று வாதாடும் உரிமை கொண்டுள்ளார்?",
        "The Attorney General of India", "இந்திய தலைமை வழக்கறிஞர் (அட்டர்னி ஜெனரல்)",
        "All other advocates appearing in the High Court of the State", "மாநில உயர் நீதிமன்றத்தில் முன்னிலையாகும் மற்ற அனைத்து வழக்கறிஞர்கள்",
        "The Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்",
        "Additional Solicitor General of India", "இந்திய கூடுதல் சொலிசிட்டர் ஜெனரல்",
        "B",
        "Under Section 23 of the Advocates Act, 1961, the Advocate General has the right of pre-audience over all other advocates appearing before the High Court, ranking after the Attorney General and Solicitor General.",
        "வழக்கறிஞர்கள் சட்டம் 1961-ன் பிரிவு 23-ன் கீழ், உயர் நீதிமன்றத்தின் முன் தோன்றும் மற்ற அனைத்து வழக்கறிஞர்களுக்கும் மேலாக அட்வகேட் ஜெனரல் முன்னுரிமை பெற்றுள்ளார் (அட்டர்னி ஜெனரல் மற்றும் சொலிசிட்டர் ஜெனரலுக்குப் பிறகு).",
        "Incorrect. Attorney General ranks highest in pre-audience across India.", "தவறு. இந்தியா முழுவதும் அட்டர்னி ஜெனரலே முதல் முன்னுரிமை பெறுகிறார்.",
        "Correct. The Advocate General has pre-audience over all ordinary and senior advocates in the State.", "சரி. மாநிலத்தில் உள்ள மற்ற அனைத்து வழக்கறிஞர்களுக்கும் மேலாக தலைமை வழக்கறிஞர் முன்னுரிமை கொண்டுள்ளார்.",
        "Incorrect. Solicitor General ranks above the Advocate General in Section 23.", "தவறு. பிரிவு 23-ல் சொலிசிட்டர் ஜெனரல் அட்வகேட் ஜெனரலுக்கு மேல் தரவரிசைப்படுத்தப்பட்டுள்ளார்.",
        "Incorrect. Additional Solicitor General also has pre-audience at the Union level.", "தவறு. கூடுதல் சொலிசிட்டர் ஜெனரலும் ஒன்றிய அளவில் முன்னுரிமை பெற்றுள்ளார்.",
        "Order under Sec 23 Advocates Act 1961: 1. AGI, 2. SG, 3. Addl SG, 4. AGs of States.",
        "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 23 வரிசை: 1. அட்டர்னி ஜெனரல், 2. சொலிசிட்டர் ஜெனரல், 3. கூடுதல் சொலிசிட்டர் ஜெனரல், 4. மாநில அட்வகேட் ஜெனரல்கள்.",
        "Pre-audience gives the law officer the right to be heard before other advocates on any day's cause list.",
        "முன்னுரிமை என்பது அன்றைய வழக்குப் பட்டியலில் மற்ற வழக்கறிஞர்களுக்கு முன்பாக வாதாட சட்ட அதிகாரிக்கு உரிமை அளிக்கிறது."
    )

    # Q15 (C)
    add_q(
        "ADVG_E_015", "Private Practice Permissibility",
        "Is the Advocate General of a State permitted to engage in private legal practice?",
        "மாநில தலைமை வழக்கறிஞர் தனியாராக வழக்கறிஞர் தொழில் (Private Practice) செய்ய அனுமதிக்கப்படுகிறாரா?",
        "No, private practice is completely prohibited by the Constitution", "இல்லை, அரசியலமைப்பால் தனியார் வழக்கறிஞர் தொழில் முற்றிலும் தடை செய்யப்பட்டுள்ளது",
        "Yes, but only in subordinate district courts", "ஆம், ஆனால் கீழ்மை மாவட்ட நீதிமன்றங்களில் மட்டுமே",
        "Yes, private practice is permitted, subject to certain restrictions", "ஆம், சில கட்டுப்பாடுகளுக்கு உட்பட்டு தனியார் தொழில் அனுமதிக்கப்படுகிறது",
        "Yes, without any restrictions whatsoever", "ஆம், எந்தவொரு கட்டுப்பாடும் இன்றி அனுமதிக்கப்படுகிறது",
        "C",
        "The Advocate General is not a full-time government servant and is not debarred from private legal practice. However, he cannot advise or appear against the State Government.",
        "தலைமை வழக்கறிஞர் முழுநேர அரசு ஊழியர் அல்ல, எனவே தனியார் வழக்கறிஞர் தொழில் செய்வதிலிருந்து தடுக்கப்படவில்லை. எனினும், மாநில அரசுக்கு எதிராக ஆலோசனையோ அல்லது வாதாடவோ முடியாது.",
        "Incorrect. Private practice is not completely prohibited.", "தவறு. தனியார் தொழில் முற்றிலும் தடை செய்யப்படவில்லை.",
        "Incorrect. Not restricted to subordinate courts; can practice in HC and SC.", "தவறு. கீழ்மை நீதிமன்றங்களுக்கு மட்டும் மட்டுப்படுத்தப்படவில்லை; உயர் மற்றும் உச்ச நீதிமன்றங்களிலும் வாதாடலாம்.",
        "Correct. Permitted to practice privately subject to ethical and conflict-of-interest restrictions.", "சரி. நெறிமுறை மற்றும் நலன் முரண்பாடு கட்டுப்பாடுகளுக்கு உட்பட்டு தனியார் தொழில் செய்ய அனுமதிக்கப்படுகிறார்.",
        "Incorrect. Cannot appear against the State Government or defend criminals without permission.", "தவறு. மாநில அரசுக்கு எதிராக வாதாடவோ அல்லது அனுமதியின்றி குற்றவாளிகளை ஆதரிக்கவோ முடியாது.",
        "Advocate General is a professional law officer, not a salaried full-time civil servant.",
        "அட்வகேட் ஜெனரல் ஒரு தொழில்முறை சட்ட அதிகாரி, முழுநேர ஊதியம் பெறும் அரசு ஊழியர் அல்ல.",
        "Because he is not a government servant, the Advocate General retains his advocate status on the Bar rolls.",
        "அவர் அரசு ஊழியர் அல்லாததால், வழக்கறிஞர் பட்டியலில் தனது வழக்கறிஞர் நிலையைத் தக்க வைத்துக் கொள்கிறார்."
    )

    # Q16 (D)
    add_q(
        "ADVG_E_016", "Restrictions on Practice",
        "Which of the following acts is the Advocate General of a State strictly prohibited from doing without government permission?",
        "அரசு அனுமதியின்றி மாநில தலைமை வழக்கறிஞர் பின்வருவனவற்றில் எதைச் செய்வது கண்டிப்பாக தடை செய்யப்பட்டுள்ளது?",
        "Appearing before the High Court in civil disputes between private parties", "தனியார் தரப்பினருக்கு இடையேயான சிவில் வழக்குகளில் உயர் நீதிமன்றத்தில் ஆஜராவது",
        "Writing academic books or legal commentaries", "கல்வி சார்ந்த புத்தகங்கள் அல்லது சட்ட விளக்கவுரைகள் எழுதுவது",
        "Delivering lectures in law colleges", "சட்டக் கல்லூரிகளில் விரிவுரைகள் ஆற்றுவது",
        "Defending an accused person in a criminal prosecution", "குற்றவியல் வழக்கில் குற்றம் சாட்டப்பட்ட நபருக்காக ஆஜராகி வாதாடுவது",
        "D",
        "The Advocate General cannot defend accused persons in criminal prosecutions without the permission of the State Government, nor can he advise or hold brief against the State Government.",
        "மாநில அரசின் அனுமதியின்றி தலைமை வழக்கறிஞர் குற்றவியல் வழக்குகளில் குற்றம் சாட்டப்பட்ட நபர்களை ஆதரிக்க முடியாது, அதேபோல் அரசுக்கு எதிராக வாதாடவோ ஆலோசிக்கவோ முடியாது.",
        "Incorrect. Can appear in private civil disputes as long as the State is not an opposing party.", "தவறு. அரசு எதிர் தரப்பாக இல்லாத வரை தனியார் சிவில் வழக்குகளில் ஆஜராகலாம்.",
        "Incorrect. Writing legal books is permitted.", "தவறு. சட்டப் புத்தகங்கள் எழுதுவது அனுமதிக்கப்படுகிறது.",
        "Incorrect. Academic lectures are permitted.", "தவறு. கல்வி விரிவுரைகள் வழங்குவது அனுமதிக்கப்படுகிறது.",
        "Correct. Defending an accused in criminal prosecution without State sanction is prohibited.", "சரி. மாநில அரசின் அனுமதியின்றி குற்றவியல் வழக்கில் குற்றவாளியை ஆதரிப்பது தடை செய்யப்பட்டுள்ளது.",
        "Since the State is the prosecutor in criminal cases, defending the accused creates an inherent conflict of interest.",
        "குற்றவியல் வழக்குகளில் அரசே வழக்கைத் தொடுப்பதால், குற்றவாளியை ஆதரிப்பது நேரடி நலன் முரண்பாட்டை உருவாக்குகிறது.",
        "He also cannot accept appointment as director in any company without government permission.",
        "அரசு அனுமதியின்றி எந்தவொரு நிறுவனத்திலும் இயக்குநராக நியமிக்கப்படுவதையும் அவர் ஏற்க முடியாது."
    )

    # Q17 (A)
    add_q(
        "ADVG_E_017", "Cabinet Membership",
        "Is the Advocate General of a State a member of the State Cabinet?",
        "மாநில தலைமை வழக்கறிஞர் மாநில அமைச்சரவையின் (State Cabinet) ஓர் உறுப்பினரா?",
        "No, he is not a member of the Cabinet", "இல்லை, அவர் அமைச்சரவையின் உறுப்பினர் அல்ல",
        "Yes, he is an ex-officio Cabinet Minister", "ஆம், அவர் பதவிவழி அமைச்சரவை அமைச்சர் ஆவார்",
        "Yes, but without voting power in the Cabinet", "ஆம், ஆனால் அமைச்சரவையில் வாக்குரிமை இல்லாத உறுப்பினர்",
        "Yes, whenever legal bills are introduced", "ஆம், சட்ட மசோதாக்கள் அறிமுகப்படுத்தப்படும் போது மட்டும்",
        "A",
        "The Advocate General is not a member of the State Cabinet. The legal minister in the Council of Ministers deals with legal matters at the political/cabinet level.",
        "தலைமை வழக்கறிஞர் மாநில அமைச்சரவையின் உறுப்பினர் அல்ல. அமைச்சரவையில் உள்ள சட்ட அமைச்சர் அரசியல்/அமைச்சரவை மட்டத்தில் சட்ட விவகாரங்களைக் கையாள்கிறார்.",
        "Correct. The Advocate General is not a member of the State Cabinet or Council of Ministers.", "சரி. தலைமை வழக்கறிஞர் அமைச்சரவையின் அல்லது அமைச்சர்கள் குழுவின் உறுப்பினர் அல்ல.",
        "Incorrect. He has no cabinet rank or ex-officio ministerial status.", "தவறு. அவருக்கு அமைச்சரவை அந்தஸ்தோ அல்லது பதவிவழி அமைச்சர் நிலையோ இல்லை.",
        "Incorrect. Cabinet meetings are attended only by Ministers, though AG may be invited for legal counsel.", "தவறு. அமைச்சரவைக் கூட்டங்களில் அமைச்சர்கள் மட்டுமே பங்கேற்பர், எனினும் சட்ட ஆலோசனைக்காக AG அழைக்கப்படலாம்.",
        "Incorrect. Introduction of bills is done by ministers.", "தவறு. மசோதாக்களை அறிமுகப்படுத்துவது அமைச்சர்களால் செய்யப்படுகிறது.",
        "Advocate General = Top Law Officer; Law Minister = Member of Cabinet handling Ministry of Law.",
        "அட்வகேட் ஜெனரல் = தலைமை சட்ட அதிகாரி; சட்ட அமைச்சர் = சட்டத்துறையை நிர்வகிக்கும் அமைச்சரவை உறுப்பினர்.",
        "This separation maintains the independent professional status of the Advocate General.",
        "இந்தப் பிரிப்பு தலைமை வழக்கறிஞரின் சுதந்திரமான தொழில்முறை நிலையைப் பாதுகாக்கிறது."
    )

    # Q18 (B)
    add_q(
        "ADVG_E_018", "Legislative Committee Membership",
        "Can the Advocate General of a State be named a member of a committee of the State Legislature?",
        "மாநில சட்டமன்றத்தின் ஒரு குழுவில் தலைமை வழக்கறிஞர் ஓர் உறுப்பினராக நியமிக்கப்படலாமா?",
        "No, only elected members of the assembly can be committee members", "இல்லை, தேர்ந்தெடுக்கப்பட்ட சட்டமன்ற உறுப்பினர்கள் மட்டுமே குழு உறுப்பினர்களாக இருக்க முடியும்",
        "Yes, under Article 177, if so named, but he cannot vote", "ஆம், உறுப்பு 177-ன் கீழ் அவ்வாறு பெயரிடப்பட்டால் உறுப்பினராகலாம், ஆனால் வாக்களிக்க முடியாது",
        "Yes, and he gets full voting rights in the committee", "ஆம், மற்றும் அக்குழுவில் முழு வாக்குரிமையையும் பெறுவார்",
        "Only if he is also an elected MLC", "அவர் தேர்ந்தெடுக்கப்பட்ட சட்ட மேலவை உறுப்பினராக இருந்தால் மட்டுமே",
        "B",
        "Article 177 provides that the Advocate General has the right to speak and take part in any committee of the Legislature of which he may be named a member, but without the right to vote.",
        "உறுப்பு 177 தலைமை வழக்கறிஞர் சட்டமன்றத்தின் எந்தவொரு குழுவிலும் உறுப்பினராக பெயரிடப்பட்டால் அதில் பேசவும் பங்கேற்கவும் உரிமையளிக்கிறது, ஆனால் வாக்களிக்கும் உரிமை இன்றி.",
        "Incorrect. Article 177 specifically permits naming the Advocate General as a committee member.", "தவறு. உறுப்பு 177 தலைமை வழக்கறிஞரை குழு உறுப்பினராக நியமிக்க வெளிப்படையாக அனுமதிக்கிறது.",
        "Correct. Can be named a member and take part in proceedings, but cannot vote.", "சரி. உறுப்பினராக பெயரிடப்பட்டு பங்கேற்கலாம், ஆனால் வாக்களிக்க முடியாது.",
        "Incorrect. The prohibition on voting applies to committees as well.", "தவறு. வாக்களிப்பதற்கான தடை குழுக்களுக்கும் பொருந்தும்.",
        "Incorrect. Does not need to be an MLC or MLA.", "தவறு. சட்ட மேலவை அல்லது பேரவை உறுப்பினராக இருக்க வேண்டிய அவசியமில்லை.",
        "Art 177 covers: (1) Legislative Assembly, (2) Legislative Council (if any), (3) Any committee thereof.",
        "உறுப்பு 177 உள்ளடக்குவது: (1) சட்டப் பேரவை, (2) சட்ட மேலவை (இருந்தால்), (3) சட்டமன்றத்தின் குழுக்கள்.",
        "His committee participation enables legislative committees to receive immediate expert legal guidance on bills.",
        "குழுவில் அவரது பங்களிப்பு மசோதாக்கள் மீது சட்டமன்றக் குழுக்களுக்கு உடனடி சட்ட வழிகாட்டுதலைப் பெற உதவுகிறது."
    )

    # Q19 (C)
    add_q(
        "ADVG_E_019", "Judicial Office Qualification",
        "Under Article 217(2)(a), what is the minimum duration of holding a judicial office required to qualify for appointment as an Advocate General?",
        "உறுப்பு 217(2)(a)-ன் கீழ், தலைமை வழக்கறிஞராக நியமிக்கப்படுவதற்குத் தேவையான தகுதியாக குறைந்தபட்சம் எத்தனை ஆண்டுகள் நீதித்துறைப் பதவியை வகித்திருக்க வேண்டும்?",
        "5 years", "5 ஆண்டுகள்",
        "7 years", "7 ஆண்டுகள்",
        "10 years", "10 ஆண்டுகள்",
        "15 years", "15 ஆண்டுகள்",
        "C",
        "Under Article 217(2)(a), a person qualifies for HC Judge (and thus Advocate General) if he has for at least ten years held a judicial office in the territory of India.",
        "உறுப்பு 217(2)(a)-ன் கீழ், இந்தியாவில் குறைந்தபட்சம் பத்து ஆண்டுகள் நீதித்துறைப் பதவியை வகித்திருந்தால் உயர் நீதிமன்ற நீதிபதியாக (எனவே அட்வகேட் ஜெனரலாக) தகுதி பெறுகிறார்.",
        "Incorrect. 5 years is the HC judge tenure requirement for Supreme Court judge.", "தவறு. 5 ஆண்டுகள் என்பது உச்ச நீதிமன்ற நீதிபதிக்கான உயர் நீதிமன்ற நீதிபதி பணிக்காலம்.",
        "Incorrect. 7 years is the practice requirement for appointment as District Judge under Art 233.", "தவறு. 7 ஆண்டுகள் என்பது உறுப்பு 233-ன் கீழ் மாவட்ட நீதிபதியாக நியமிக்கப்பட தேவையான வழக்கறிஞர் பயிற்சி காலம்.",
        "Correct. At least 10 years holding a judicial office in India.", "சரி. இந்தியாவில் குறைந்தபட்சம் 10 ஆண்டுகள் நீதித்துறைப் பதவியை வகித்திருக்க வேண்டும்.",
        "Incorrect. 15 years is not a constitutional qualification threshold.", "தவறு. 15 ஆண்டுகள் அரசியலமைப்பு தகுதி வரம்பு அல்ல.",
        "10 years judicial office OR 10 years advocate of High Court = HC Judge eligibility = AG eligibility.",
        "10 ஆண்டுகள் நீதித்துறை பதவி அல்லது 10 ஆண்டுகள் உயர் நீதிமன்ற வழக்கறிஞர் = உயர் நீதிமன்ற நீதிபதி தகுதி = தலைமை வழக்கறிஞர் தகுதி.",
        "Holding judicial office means functioning within the organized judicial hierarchy of India.",
        "நீதித்துறை பதவியை வகித்தல் என்பது இந்தியாவின் ஒழுங்கமைக்கப்பட்ட நீதித்துறை படிநிலைக்குள் பணியாற்றுவதைக் குறிக்கிறது."
    )

    # Q20 (D)
    add_q(
        "ADVG_E_020", "Advocacy Qualification",
        "Under Article 217(2)(b), what is the minimum period of practice as an advocate of a High Court required to be eligible as Advocate General?",
        "உறுப்பு 217(2)(b)-ன் கீழ், தலைமை வழக்கறிஞராக தகுதி பெற குறைந்தபட்சம் எத்தனை ஆண்டுகள் உயர் நீதிமன்ற வழக்கறிஞராகப் பணியாற்றியிருக்க வேண்டும்?",
        "5 years", "5 ஆண்டுகள்",
        "7 years", "7 ஆண்டுகள்",
        "8 years", "8 ஆண்டுகள்",
        "10 years", "10 ஆண்டுகள்",
        "D",
        "Article 217(2)(b) requires at least ten years as an advocate of a High Court or of two or more such courts in succession.",
        "உறுப்பு 217(2)(b) குறைந்தபட்சம் பத்து ஆண்டுகள் உயர் நீதிமன்றத்தில் அல்லது அடுத்தடுத்து இரண்டு அல்லது அதற்கு மேற்பட்ட அத்தகைய நீதிமன்றங்களில் வழக்கறிஞராகப் பணியாற்றியிருக்க வேண்டும் என்று கோருகிறது.",
        "Incorrect. 5 years is insufficient for HC Judge / AG eligibility.", "தவறு. உயர் நீதிமன்ற நீதிபதி / அட்வகேட் ஜெனரல் தகுதிக்கு 5 ஆண்டுகள் போதாது.",
        "Incorrect. 7 years applies to District Judges under Article 233(2).", "தவறு. 7 ஆண்டுகள் என்பது உறுப்பு 233(2)-ன் கீழ் மாவட்ட நீதிபதிகளுக்குப் பொருந்தும்.",
        "Incorrect. 8 years is not a constitutional criterion.", "தவறு. 8 ஆண்டுகள் அரசியலமைப்பு அளவுகோல் அல்ல.",
        "Correct. At least 10 years as an advocate of a High Court.", "சரி. குறைந்தபட்சம் 10 ஆண்டுகள் உயர் நீதிமன்ற வழக்கறிஞராகப் பணியாற்றியிருக்க வேண்டும்.",
        "Both branches of Article 217(2) require a 10-year benchmark: 10 years judicial office OR 10 years HC advocate.",
        "உறுப்பு 217(2)-ன் இரு பிரிவுகளுமே 10 ஆண்டுகளை வரம்பாகக் கொண்டுள்ளன: 10 ஆண்டுகள் நீதித்துறை பதவி அல்லது 10 ஆண்டுகள் வழக்கறிஞர் பணி.",
        "Continuous practice or succession in multiple High Courts is counted towards the 10-year requirement.",
        "ஒன்றுக்கு மேற்பட்ட உயர் நீதிமன்றங்களில் அடுத்தடுத்து பணியாற்றிய காலமும் 10 ஆண்டுத் தேவைக்கு கணக்கிடப்படும்."
    )

    # --- 21 to 30 ---
    # Q21 (A)
    add_q(
        "ADVG_E_021", "Distinguished Jurist Rule",
        "Can a 'distinguished jurist in the opinion of the President' be appointed as the Advocate General of a State?",
        "குடியரசுத் தலைவரின் பார்வையில் 'சிறந்த சட்ட நிபுணர்' (Distinguished Jurist) என்ற தகுதியின் அடிப்படையில் ஒருவர் மாநில தலைமை வழக்கறிஞராக நியமிக்கப்பட முடியுமா?",
        "No, because Article 217(2) does not contain a 'distinguished jurist' category", "முடியாது, ஏனெனில் உறுப்பு 217(2)-ல் 'சிறந்த சட்ட நிபுணர்' என்ற வகைப்பாடு இல்லை",
        "Yes, the Governor has discretionary power to appoint a jurist", "ஆம், சட்ட நிபுணரை நியமிக்க ஆளுநருக்கு விருப்புரிமை உண்டு",
        "Yes, with the prior approval of the Supreme Court", "ஆம், உச்ச நீதிமன்றத்தின் முன் அனுமதியுடன் நியமிக்கலாம்",
        "Yes, if the State Legislature passes a special resolution", "ஆம், மாநில சட்டமன்றம் சிறப்புத் தீர்மானம் நிறைவேற்றினால் நியமிக்கலாம்",
        "A",
        "Unlike the Supreme Court (Art 124(3)(c)), Article 217(2) for High Court Judges does NOT provide for the appointment of a 'distinguished jurist'. Since the AG requires HC Judge qualifications, a distinguished jurist cannot be appointed AG.",
        "உச்ச நீதிமன்றத்தைப் போலன்றி (உறுப்பு 124(3)(c)), உயர் நீதிமன்ற நீதிபதிக்கான உறுப்பு 217(2)-ல் 'சிறந்த சட்ட நிபுணர்' என்ற வகைப்பாடு இல்லை. அட்வகேட் ஜெனரலுக்கு உயர் நீதிமன்ற நீதிபதி தகுதி தேவைப்படுவதால், சிறந்த சட்ட நிபுணரை அட்வகேட் ஜெனரலாக நியமிக்க முடியாது.",
        "Correct. 'Distinguished jurist' exists only for SC Judges (Art 124(3)(c)) / Attorney General, not for HC Judges (Art 217(2)) / Advocate General.", "சரி. 'சிறந்த சட்ட நிபுணர்' என்பது உச்ச நீதிமன்ற நீதிபதி (உறுப்பு 124(3)(c)) / அட்டர்னி ஜெனரலுக்கு மட்டுமே உண்டு, உயர் நீதிமன்ற நீதிபதி (உறுப்பு 217(2)) / அட்வகேட் ஜெனரலுக்கு இல்லை.",
        "Incorrect. The Governor has no constitutional power to invent qualifications outside Article 217(2).", "தவறு. உறுப்பு 217(2)-க்கு வெளியே தகுதிகளை உருவாக்க ஆளுநருக்கு எந்த அதிகாரமும் இல்லை.",
        "Incorrect. Supreme Court approval cannot alter constitutional eligibility requirements.", "தவறு. உச்ச நீதிமன்ற அனுமதி அரசியலமைப்பு தகுதித் தேவைகளை மாற்ற முடியாது.",
        "Incorrect. State Legislature cannot modify constitutional qualifications via resolution.", "தவறு. தீர்மானத்தின் மூலம் மாநில சட்டமன்றம் அரசியலமைப்பு தகுதிகளை மாற்ற முடியாது.",
        "Classic Trap: A distinguished jurist can be Attorney General, but CANNOT be Advocate General.",
        "முக்கிய பொறி: சிறந்த சட்ட நிபுணர் அட்டர்னி ஜெனரலாக நியமிக்கப்படலாம், ஆனால் அட்வகேட் ஜெனரலாக முடியாது.",
        "This is one of the most frequently tested comparative questions in TNPSC and UPSC exams.",
        "இது டிஎன்பிஎஸ்சி மற்றும் யுபிஎஸ்சி தேர்வுகளில் அதிகம் கேட்கப்படும் ஒப்பீட்டுக் கேள்விகளில் ஒன்றாகும்."
    )

    # Q22 (B)
    add_q(
        "ADVG_E_022", "Retirement Age Trap",
        "What is the retirement age of the Advocate General of a State as per the Constitution of India?",
        "இந்திய அரசியலமைப்பின்படி மாநில தலைமை வழக்கறிஞரின் ஓய்வு பெறும் வயது என்ன?",
        "62 years", "62 ஆண்டுகள்",
        "No retirement age is prescribed in the Constitution", "அரசியலமைப்பில் எந்த ஓய்வு வயதும் குறிப்பிடப்படவில்லை",
        "65 years", "65 ஆண்டுகள்",
        "60 years", "60 ஆண்டுகள்",
        "B",
        "The Constitution does not specify any retirement age for the Advocate General. He holds office during the pleasure of the Governor (Article 165(3)). In G.D. Karkare v. T.L. Shevde, the court held that the age limit of 62 for HC judges does not apply to AG.",
        "தலைமை வழக்கறிஞருக்கு அரசியலமைப்பு எந்த ஓய்வு வயதையும் குறிப்பிடவில்லை. அவர் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார் (உறுப்பு 165(3)). ஜி.டி. கார்கரே வழக்கில், உயர் நீதிமன்ற நீதிபதிகளுக்கான 62 வயது வரம்பு அட்வகேட் ஜெனரலுக்குப் பொருந்தாது என்று தீர்ப்பளிக்கப்பட்டது.",
        "Incorrect. 62 is the retirement age of High Court Judges, not the Advocate General.", "தவறு. 62 என்பது உயர் நீதிமன்ற நீதிபதிகளின் ஓய்வு வயது, அட்வகேட் ஜெனரலுக்கு அல்ல.",
        "Correct. The Constitution prescribes no retirement age; holds office during Governor's pleasure.", "சரி. அரசியலமைப்பு எந்த ஓய்வு வயதையும் குறிப்பிடவில்லை; ஆளுநரின் விருப்பம் வரை பதவி வகிப்பார்.",
        "Incorrect. 65 is the retirement age of Supreme Court Judges and CAG.", "தவறு. 65 என்பது உச்ச நீதிமன்ற நீதிபதிகள் மற்றும் சிஏஜியின் ஓய்வு வயது.",
        "Incorrect. 60 is general state government servant retirement age, not applicable to AG.", "தவறு. 60 என்பது பொதுவான அரசு ஊழியர் ஓய்வு வயது, அட்வகேட் ஜெனரலுக்குப் பொருந்தாது.",
        "The qualification requirement is 'qualified to be appointed', which refers to competence and experience, not the age bar.",
        "தகுதித் தேவை என்பது 'நியமிக்கப்பட தகுதியுடையவராக' இருத்தல் மட்டுமே; இது அனுபவத்தையும் திறமையையும் குறிக்கிறது, வயது வரம்பை அல்ல.",
        "A person who has crossed 62 years can legally be appointed as the Advocate General of a State.",
        "62 வயதைக் கடந்த ஒருவரை சட்டப்பூர்வமாக ஒரு மாநிலத்தின் தலைமை வழக்கறிஞராக நியமிக்க முடியும்."
    )

    # Q23 (C)
    add_q(
        "ADVG_E_023", "Historical Predecessor",
        "Under which British-era enactment was the office of the Advocate General for Provinces first formally established?",
        "பிரிட்டிஷ் காலத்தின் எந்தச் சட்டத்தின் கீழ் முதன்முதலில் மாகாணங்களுக்கான தலைமை வழக்கறிஞர் (Advocate General) பதவி முறைப்படி நிறுவப்பட்டது?",
        "Indian Councils Act, 1861", "இந்தியக் கவுன்சில்கள் சட்டம், 1861",
        "Government of India Act, 1919", "இந்திய அரசுச் சட்டம், 1919",
        "Government of India Act, 1935", "இந்திய அரசுச் சட்டம், 1935",
        "Regulating Act, 1773", "ஒழுங்குமுறைச் சட்டம், 1773",
        "C",
        "Section 55 of the Government of India Act, 1935 provided for an Advocate-General for each Province, appointed by the Governor of the Province.",
        "இந்திய அரசுச் சட்டம் 1935-ன் பிரிவு 55 ஒவ்வொரு மாகாணத்திற்கும் மாகாண ஆளுநரால் நியமிக்கப்படும் தலைமை வழக்கறிஞர் பதவியை வழங்கியது.",
        "Incorrect. 1861 Act added non-official members to Councils, did not establish provincial AG framework.", "தவறு. 1861 சட்டம் கவுன்சில்களில் அலுவல்சாரா உறுப்பினர்களைச் சேர்த்தது, மாகாண அட்வகேட் ஜெனரல் கட்டமைப்பை உருவாக்கவில்லை.",
        "Incorrect. 1919 Act introduced dyarchy in provinces.", "தவறு. 1919 சட்டம் மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.",
        "Correct. Government of India Act, 1935 Section 55 formally provided for the Advocate-General for each Province.", "சரி. இந்திய அரசுச் சட்டம் 1935-ன் பிரிவு 55 ஒவ்வொரு மாகாணத்திற்கும் தலைமை வழக்கறிஞர் பதவியை முறைப்படி வழங்கியது.",
        "Incorrect. Regulating Act 1773 established Supreme Court at Calcutta, not provincial Advocate Generals.", "தவறு. ஒழுங்குமுறைச் சட்டம் 1773 கல்கத்தாவில் உச்ச நீதிமன்றத்தை நிறுவியது, மாகாண அட்வகேட் ஜெனரல்களை அல்ல.",
        "Section 55 of the 1935 Act served as the direct textual model for Article 165 of the Indian Constitution.",
        "1935 சட்டத்தின் பிரிவு 55, இந்திய அரசியலமைப்பின் உறுப்பு 165-க்கு நேரடி மாதிரியாக செயல்பட்டது.",
        "Prior to 1935, Advocate Generals existed in Presidency towns (Madras, Bombay, Bengal) dating back to the East India Company.",
        "1935-க்கு முன்பே, கிழக்கிந்திய கம்பெனி காலத்தில் இருந்தே மாகாணத் தலைநகரங்களில் (சென்னை, பம்பாய், வங்கம்) அட்வகேட் ஜெனரல்கள் இருந்தனர்."
    )

    # Q24 (D)
    add_q(
        "ADVG_E_024", "Duties Specification",
        "Which clause of Article 165 enumerates the constitutional duties of the Advocate General of a State?",
        "உறுப்பு 165-ன் எந்தப் பிரிவு மாநில தலைமை வழக்கறிஞரின் அரசியலமைப்பு கடமைகளை வரிசைப்படுத்துகிறது?",
        "Clause (4)", "பிரிவு (4)",
        "Clause (1)", "பிரிவு (1)",
        "Clause (3)", "பிரிவு (3)",
        "Clause (2)", "பிரிவு (2)",
        "D",
        "Article 165(2) outlines the duties of the Advocate General: to advise the Government of the State upon legal matters and perform other legal duties referred or assigned to him by the Governor.",
        "உறுப்பு 165(2) தலைமை வழக்கறிஞரின் கடமைகளை கோடிட்டுக் காட்டுகிறது: மாநில அரசுக்கு சட்ட விவகாரங்களில் ஆலோசனை வழங்குவது மற்றும் ஆளுநரால் ஒப்படைக்கப்படும் பிற சட்டப் பணிகளைச் செய்வது.",
        "Incorrect. Article 165 has only 3 clauses; Clause (4) does not exist.", "தவறு. உறுப்பு 165-ல் 3 பிரிவுகள் மட்டுமே உள்ளன; பிரிவு (4) என்று ஒன்று இல்லை.",
        "Incorrect. Clause (1) deals with appointment and qualifications.", "தவறு. பிரிவு (1) நியமனம் மற்றும் தகுதிகள் பற்றியது.",
        "Incorrect. Clause (3) deals with tenure and remuneration.", "தவறு. பிரிவு (3) பதவிக்காலம் மற்றும் ஊதியம் பற்றியது.",
        "Correct. Clause (2) specifically enumerates the duties of the Advocate General.", "சரி. பிரிவு (2) தலைமை வழக்கறிஞரின் கடமைகளை வெளிப்படையாகக் குறிப்பிடுகிறது.",
        "Article 165 Breakdown: (1) Appointment & Qualifications, (2) Duties, (3) Pleasure tenure & Remuneration.",
        "உறுப்பு 165 கட்டமைப்பு: (1) நியமனம் & தகுதிகள், (2) கடமைகள், (3) விருப்பப் பதவிக்காலம் & ஊதியம்.",
        "Notice that Article 165 has exactly three clauses, whereas Article 76 (Attorney General) has four clauses.",
        "கவனிக்க: உறுப்பு 165 சரியாக மூன்று பிரிவுகளைக் கொண்டுள்ளது, ஆனால் உறுப்பு 76 (அட்டர்னி ஜெனரல்) நான்கு பிரிவுகளைக் கொண்டுள்ளது."
    )

    # Q25 (A)
    add_q(
        "ADVG_E_025", "Advice Recipient",
        "To whom does the Advocate General of a State render constitutional legal advice under Article 165(2)?",
        "உறுப்பு 165(2)-ன் கீழ் மாநில தலைமை வழக்கறிஞர் யாருக்கு அரசியலமைப்பு ரீதியான சட்ட ஆலோசனைகளை வழங்குகிறார்?",
        "The Government of the State", "மாநில அரசு",
        "The High Court Judges", "உயர் நீதிமன்ற நீதிபதிகள்",
        "The Speaker of the Assembly solely in his personal capacity", "சபாநாயகருக்கு அவரது தனிப்பட்ட முறையில் மட்டும்",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "A",
        "Article 165(2) mandates that it shall be the duty of the Advocate General to give advice to the Government of the State upon such legal matters as may be referred to him by the Governor.",
        "உறுப்பு 165(2) ஆளுநரால் தன்னிடம் அனுப்பப்படும் சட்ட விவகாரங்களில் மாநில அரசுக்கு சட்ட ஆலோசனை வழங்குவது தலைமை வழக்கறிஞரின் கடமையாகும் என்று ஆணையிடுகிறது.",
        "Correct. The Advocate General advises the Government of the State.", "சரி. தலைமை வழக்கறிஞர் மாநில அரசுக்கு சட்ட ஆலோசனை வழங்குகிறார்.",
        "Incorrect. The Advocate General cannot advise judges; judiciary is independent.", "தவறு. தலைமை வழக்கறிஞர் நீதிபதிகளுக்கு ஆலோசனை வழங்க முடியாது; நீதித்துறை சுதந்திரமானது.",
        "Incorrect. Advises the government, not individual legislative officers in personal capacity.", "தவறு. அரசுக்கே ஆலோசனை வழங்குகிறார், தனிப்பட்ட முறையில் சட்டமன்ற அதிகாரிகளுக்கு அல்ல.",
        "Incorrect. Advising the President / Union Government is the duty of the Attorney General under Art 76(2).", "தவறு. குடியரசுத் தலைவர் / ஒன்றிய அரசுக்கு ஆலோசனை வழங்குவது உறுப்பு 76(2)-ன் கீழ் அட்டர்னி ஜெனரலின் கடமையாகும்.",
        "Advocate General is the chief legal adviser to the State Government.",
        "தலைமை வழக்கறிஞர் மாநில அரசின் முதன்மை சட்ட ஆலோசகர் ஆவார்.",
        "The advice tendered by the Advocate General is advisory in nature and not binding on the State Cabinet.",
        "தலைமை வழக்கறிஞர் வழங்கும் ஆலோசனை வழிகாட்டும் தன்மை கொண்டதே தவிர, மாநில அமைச்சரவையைக் கட்டுப்படுத்தாது."
    )

    # Q26 (B)
    add_q(
        "ADVG_E_026", "Consolidated Fund Status",
        "Is the remuneration of the Advocate General of a State charged upon the Consolidated Fund of the State?",
        "மாநில தலைமை வழக்கறிஞரின் ஊதியம் மாநில ஒருங்கிணைந்த நிதியிலிருந்து சுமத்தப்படும் (Charged) செலவினமா?",
        "Yes, under Article 202(3)(a)", "ஆம், உறுப்பு 202(3)(a)-ன் கீழ்",
        "No, it is not charged on the Consolidated Fund; it is voted by the State Legislature", "இல்லை, இது ஒருங்கிணைந்த நிதியிலிருந்து சுமத்தப்பட்ட செலவு அல்ல; சட்டமன்றத்தால் வாக்களிக்கப்படுகிறது",
        "Yes, but only during emergencies", "ஆம், ஆனால் அவசரநிலைக் காலங்களில் மட்டுமே",
        "Yes, if approved by the High Court", "ஆம், உயர் நீதிமன்றத்தால் அங்கீகரிக்கப்பட்டால்",
        "B",
        "Under Article 202(3), the remuneration of the Advocate General is NOT charged upon the Consolidated Fund of the State. It is determined by the Governor and voted by the State Legislature as part of budget demands.",
        "உறுப்பு 202(3)-ன் கீழ், தலைமை வழக்கறிஞரின் ஊதியம் மாநில ஒருங்கிணைந்த நிதியில் சுமத்தப்பட்ட செலவு அல்ல. இது ஆளுநரால் தீர்மானிக்கப்பட்டு, பட்ஜெட் மானியக் கோரிக்கைகளின் ஒரு பகுதியாக சட்டமன்றத்தால் வாக்களிக்கப்படுகிறது.",
        "Incorrect. Article 202(3) lists Governor's emoluments, HC judges' salaries, etc., but NOT Advocate General.", "தவறு. உறுப்பு 202(3) ஆளுநரின் படிகள், உயர் நீதிமன்ற நீதிபதிகளின் சம்பளம் ஆகியவற்றை பட்டியலிடுகிறது, ஆனால் அட்வகேட் ஜெனரலை அல்ல.",
        "Correct. Remuneration of the AG is NOT a charged expenditure; it is subject to voting by the Legislature.", "சரி. தலைமை வழக்கறிஞரின் ஊதியம் சுமத்தப்பட்ட செலவு அல்ல; சட்டமன்றத்தின் வாக்கெடுப்புக்கு உட்பட்டது.",
        "Incorrect. Emergency provisions do not convert it into a charged expenditure.", "தவறு. அவசரநிலை விதிகள் இதை சுமத்தப்பட்ட செலவாக மாற்றாது.",
        "Incorrect. High Court has no authority to charge expenditures on Consolidated Fund.", "தவறு. ஒருங்கிணைந்த நிதியில் செலவினங்களை சுமத்த உயர் நீதிமன்றத்திற்கு அதிகாரம் இல்லை.",
        "Non-charged status reflects that the Advocate General serves during the pleasure of the executive.",
        "சுமத்தப்படாத நிலை என்பது தலைமை வழக்கறிஞர் நிர்வாகத்தின் விருப்பத்தின் அடிப்படையில் பணியாற்றுகிறார் என்பதை பிரதிபலிக்கிறது.",
        "HC Judges' salaries are charged on State Consolidated Fund, but Advocate General's remuneration is not.",
        "உயர் நீதிமன்ற நீதிபதிகளின் சம்பளம் மாநில ஒருங்கிணைந்த நிதியில் சுமத்தப்படுகிறது, ஆனால் அட்வகேட் ஜெனரலின் ஊதியம் அவ்வாறு இல்லை."
    )

    # Q27 (C)
    add_q(
        "ADVG_E_027", "Number of Advocate Generals",
        "According to the Constitution of India and Supreme Court rulings, how many Advocate Generals can be appointed for a single State under Article 165?",
        "இந்திய அரசியலமைப்பு மற்றும் உச்ச நீதிமன்றத் தீர்ப்புகளின்படி, உறுப்பு 165-ன் கீழ் ஒரு மாநிலத்திற்கு எத்தனை தலைமை வழக்கறிஞர்கள் நியமிக்கப்படலாம்?",
        "Two (One for civil and one for criminal)", "இருவர் (ஒருவர் சிவில் மற்றும் ஒருவர் கிரிமினல் விவகாரங்களுக்கு)",
        "As many as the Governor determines necessary", "ஆளுநர் அவசியமென்று கருதும் எண்ணிக்கையில்",
        "Only ONE Advocate General", "ஒரு தலைமை வழக்கறிஞர் மட்டுமே",
        "Up to three, including Additional Advocate Generals", "கூடுதல் தலைமை வழக்கறிஞர்கள் உட்பட மூவர் வரை",
        "C",
        "In M.T. Khan v. Government of Andhra Pradesh (2004), the Supreme Court ruled that Article 165 contemplates only ONE Advocate General for a State. The post of Additional Advocate General is created under executive power, not Article 165.",
        "எம்.டி. கான் எதிர் ஆந்திரப் பிரதேச அரசு (2004) வழக்கில், உறுப்பு 165 ஒரு மாநிலத்திற்கு ஒரு தலைமை வழக்கறிஞரை மட்டுமே கருதுகிறது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. கூடுதல் அட்வகேட் ஜெனரல் பதவி நிர்வாக அதிகாரத்தின் கீழ் உருவாக்கப்படுகிறதே தவிர உறுப்பு 165-ன் கீழ் அல்ல.",
        "Incorrect. The Constitution does not permit dual Advocate Generals for separate branches of law.", "தவறு. சட்டப் பிரிவுகளுக்காக இரு தலைமை வழக்கறிஞர்களை நியமிக்க அரசியலமைப்பு அனுமதிக்கவில்லை.",
        "Incorrect. Governor cannot multiply constitutional offices under Article 165.", "தவறு. உறுப்பு 165-ன் கீழ் அரசியலமைப்பு பதவிகளை ஆளுநர் பெருக்க முடியாது.",
        "Correct. The Constitution contemplates only ONE Advocate General for each State.", "சரி. அரசியலமைப்பு ஒவ்வொரு மாநிலத்திற்கும் ஒரே ஒரு தலைமை வழக்கறிஞரை மட்டுமே கருதுகிறது.",
        "Incorrect. Additional AGs are non-constitutional executive appointments.", "தவறு. கூடுதல் தலைமை வழக்கறிஞர்கள் அரசியலமைப்பு சாராத நிர்வாக நியமனங்கள் ஆவர்.",
        "Landmark Judgment: M.T. Khan v. Govt of AP (2004) — Article 165 envisions a singular office.",
        "வரலாற்றுத் தீர்ப்பு: எம்.டி. கான் எதிர் ஆந்திர அரசு (2004) — உறுப்பு 165 ஒற்றைப் பதவியையே கருதுகிறது.",
        "Constitutional duties under Article 165 cannot be delegated to Additional Advocate Generals.",
        "உறுப்பு 165-ன் கீழ் உள்ள அரசியலமைப்பு கடமைகளை கூடுதல் தலைமை வழக்கறிஞர்களுக்கு பிரதிநிதித்துவப்படுத்த முடியாது."
    )

    # Q28 (D)
    add_q(
        "ADVG_E_028", "Citizenship Criterion",
        "Which of the following is a mandatory qualification for appointment as the Advocate General of a State?",
        "மாநில தலைமை வழக்கறிஞராக நியமிக்கப்படுவதற்கு பின்வருவனவற்றில் எது கட்டாயத் தகுதியாகும்?",
        "Must have been born in that specific State", "அக்குறிப்பிட்ட மாநிலத்திலேயே பிறந்தவராக இருக்க வேண்டும்",
        "Must be proficient in the official language of the State", "மாநிலத்தின் அதிகாரப்பூர்வ மொழியில் தேர்ச்சி பெற்றிருக்க வேண்டும்",
        "Must have served as a government pleader for at least 5 years", "குறைந்தபட்சம் 5 ஆண்டுகள் அரசு வழக்கறிஞராக பணியாற்றியிருக்க வேண்டும்",
        "Must be a citizen of India", "இந்தியக் குடிமகனாக இருக்க வேண்டும்",
        "D",
        "Under Article 217(2), to be qualified as a High Court Judge (and hence Advocate General), the candidate must be a citizen of India. There is no domicile or state-birth requirement.",
        "உறுப்பு 217(2)-ன் படி, உயர் நீதிமன்ற நீதிபதியாக (எனவே தலைமை வழக்கறிஞராக) தகுதி பெற இந்தியக் குடிமகனாக இருக்க வேண்டும். மாநில இருப்பிடச் சான்றோ அல்லது மாநிலத்தில் பிறந்திருக்க வேண்டும் என்ற தேவையோ இல்லை.",
        "Incorrect. There is no requirement of birth in the specific State.", "தவறு. குறிப்பிட்ட மாநிலத்தில் பிறந்திருக்க வேண்டும் என்ற தேவை இல்லை.",
        "Incorrect. Language proficiency is not a constitutional eligibility requirement.", "தவறு. மொழித் தேர்ச்சி அரசியலமைப்பு தகுதித் தேவை அல்ல.",
        "Incorrect. Government pleader service is not mandatory; private HC practice suffices.", "தவறு. அரசு வழக்கறிஞர் பணி கட்டாயமல்ல; உயர் நீதிமன்ற வழக்கறிஞர் பயிற்சியே போதுமானது.",
        "Correct. Must be a citizen of India under Article 217(2).", "சரி. உறுப்பு 217(2)-ன் கீழ் கட்டாயம் இந்தியக் குடிமகனாக இருக்க வேண்டும்.",
        "Constitutional qualification: Citizen of India + (10 yrs judicial office OR 10 yrs HC advocate).",
        "அரசியலமைப்புத் தகுதி: இந்தியக் குடிமகன் + (10 ஆண்டுகள் நீதித்துறை பதவி அல்லது 10 ஆண்டுகள் உயர் நீதிமன்ற வழக்கறிஞர்).",
        "A lawyer from another State can be appointed Advocate General if the State Government so decides.",
        "மாநில அரசு விரும்பினால் மற்றொரு மாநிலத்தைச் சேர்ந்த வழக்கறிஞரையும் தலைமை வழக்கறிஞராக நியமிக்கலாம்."
    )

    # Q29 (A)
    add_q(
        "ADVG_E_029", "Contempt of Courts Act",
        "Under Section 15 of the Contempt of Courts Act, 1971, whose motion or written consent is required for the High Court to take cognizance of a criminal contempt brought by a private individual?",
        "நீதிமன்ற அவமதிப்புச் சட்டம் 1971-ன் பிரிவு 15-ன் கீழ், ஒரு தனிநபர் கொண்டுவரும் குற்றவியல் அவமதிப்பை உயர் நீதிமன்றம் விசாரணைக்கு ஏற்க யாருடைய முறையீடு அல்லது எழுத்துப்பூர்வ இசைவு தேவை?",
        "The Advocate General of the State", "மாநில தலைமை வழக்கறிஞர்",
        "The Chief Secretary of the State", "மாநில தலைமைச் செயலாளர்",
        "The Director of Public Prosecutions", "பொது வழக்குத் துறை இயக்குநர்",
        "The Home Minister of the State", "மாநில உள்துறை அமைச்சர்",
        "A",
        "Section 15(1)(b) of the Contempt of Courts Act, 1971 provides that the High Court may take action on a motion made by the Advocate General or by any other person with the consent in writing of the Advocate General.",
        "நீதிமன்ற அவமதிப்புச் சட்டம் 1971 பிரிவு 15(1)(b)-ன் படி, உயர் நீதிமன்றம் தலைமை வழக்கறிஞரின் முறையீட்டின் பேரிலோ அல்லது தலைமை வழக்கறிஞரின் எழுத்துப்பூர்வ இசைவு பெற்ற பிற நபரால் கொண்டுவரப்படும் போது மட்டுமே குற்றவியல் அவமதிப்பு நடவடிக்கையை எடுக்க முடியும்.",
        "Correct. Written consent of the Advocate General is mandatory under Section 15.", "சரி. பிரிவு 15-ன் கீழ் தலைமை வழக்கறிஞரின் எழுத்துப்பூர்வ இசைவு கட்டாயமாகும்.",
        "Incorrect. Chief Secretary has no statutory role in granting consent for criminal contempt.", "தவறு. குற்றவியல் அவமதிப்புக்கு இசைவு வழங்க தலைமைச் செயலாளருக்கு சட்டப்பூர்வ பங்கு இல்லை.",
        "Incorrect. Director of Public Prosecutions does not exercise Section 15 contempt powers.", "தவறு. பொது வழக்குத் துறை இயக்குநர் பிரிவு 15 அதிகாரங்களைப் பயன்படுத்துவதில்லை.",
        "Incorrect. Home Minister has no role in contempt proceedings.", "தவறு. அவமதிப்பு நடவடிக்கைகளில் உள்துறை அமைச்சருக்கு எந்தப் பங்கும் இல்லை.",
        "Supreme Court (Sec 15) = Attorney General / Solicitor General consent; High Court (Sec 15) = Advocate General consent.",
        "உச்ச நீதிமன்றம் (பிரிவு 15) = அட்டர்னி ஜெனரல் / சொலிசிட்டர் ஜெனரல் இசைவு; உயர் நீதிமன்றம் (பிரிவு 15) = அட்வகேட் ஜெனரல் இசைவு.",
        "This consent acts as a filter to prevent frivolous or vexatious contempt petitions against courts.",
        "இந்த இசைவு நீதிமன்றங்களுக்கு எதிராக வீண் அல்லது பழிவாங்கும் அவமதிப்பு மனுக்கள் வருவதைத் தடுக்கும் வடிகட்டியாகச் செயல்படுகிறது."
    )

    # Q30 (B)
    add_q(
        "ADVG_E_030", "CPC Public Nuisance",
        "Under Section 91 of the Code of Civil Procedure (CPC), 1908, who has the statutory authority to institute a suit for public nuisance without showing any special damage?",
        "சிவில் நடைமுறைச் சட்டம் (CPC) 1908-ன் பிரிவு 91-ன் கீழ், எந்தவொரு குறிப்பிட்ட பாதிப்பையும் நிரூபிக்காமல் பொதுத் தொல்லைக்கு (Public Nuisance) எதிராக வழக்குத் தொடர யாருக்கு சட்டப்பூர்வ அதிகாரம் உள்ளது?",
        "The District Collector", "மாவட்ட ஆட்சியர்",
        "The Advocate General of the State", "மாநில தலைமை வழக்கறிஞர்",
        "The Law Secretary", "சட்டத்துறைச் செயலாளர்",
        "The Superintendent of Police", "காவல்துறை கண்காணிப்பாளர்",
        "B",
        "Section 91 of the CPC authorizes the Advocate General, or two or more persons with the leave of the court, to institute a suit in the case of a public nuisance, even though no special damage has been caused.",
        "சிவில் நடைமுறைச் சட்டம் பிரிவு 91, எந்தவொரு குறிப்பிட்ட பாதிப்பும் ஏற்படாத போதிலும், பொதுத் தொல்லைக்கு எதிராக வழக்குத் தொடர தலைமை வழக்கறிஞருக்கு அல்லது நீதிமன்ற அனுமதியுடன் இரண்டு அல்லது அதற்கு மேற்பட்ட நபர்களுக்கு அதிகாரம் அளிக்கிறது.",
        "Incorrect. District Collector does not institute civil suits under Section 91 CPC.", "தவறு. மாவட்ட ஆட்சியர் CPC பிரிவு 91-ன் கீழ் சிவில் வழக்குகளைத் தொடுப்பதில்லை.",
        "Correct. Section 91 explicitly empowers the Advocate General as protector of the public interest.", "சரி. பிரிவு 91 பொது நலனின் பாதுகாவலராக தலைமை வழக்கறிஞருக்கு வெளிப்படையாக அதிகாரம் அளிக்கிறது.",
        "Incorrect. Law Secretary is an administrative officer, not authorized under Section 91.", "தவறு. சட்டச் செயலாளர் ஓர் நிர்வாக அதிகாரி, பிரிவு 91-ன் கீழ் அதிகாரமளிக்கப்படவில்லை.",
        "Incorrect. Superintendent of Police deals with law enforcement, not Section 91 civil suits.", "தவறு. காவல் கண்காணிப்பாளர் சட்டம் ஒழுங்கைக் கையாள்கிறார், சிவில் வழக்குகளை அல்ல.",
        "Advocate General acts as 'parens patriae' (guardian of public rights) under Sections 91 and 92 of CPC.",
        "CPC பிரிவு 91 மற்றும் 92-ன் கீழ் தலைமை வழக்கறிஞர் பொது உரிமைகளின் பாதுகாவலராகச் செயல்படுகிறார்.",
        "Section 92 similarly covers public trusts and charities.",
        "பிரிவு 92 இதேபோல் பொது அறக்கட்டளைகள் மற்றும் தொண்டு நிறுவனங்களை உள்ளடக்கியது."
    )

    # --- 31 to 40 ---
    # Q31 (C)
    add_q(
        "ADVG_E_031", "CPC Public Charities",
        "Under Section 92 of the Code of Civil Procedure, 1908, relating to public charities, a suit can be instituted by:",
        "பொது அறக்கட்டளைகள் தொடர்பான சிவில் நடைமுறைச் சட்டம் 1908-ன் பிரிவு 92-ன் கீழ், வழக்கை யார் தொடரலாம்?",
        "The Charity Commissioner exclusively", "தொண்டு நிறுவனங்களின் ஆணையர் மட்டுமே",
        "Any registered NGO", "பதிவுசெய்யப்பட்ட எந்தவொரு அரசு சாரா அமைப்பும்",
        "The Advocate General, or two or more persons having an interest in the trust with leave of the court", "தலைமை வழக்கறிஞர், அல்லது அறக்கட்டளையில் ஆர்வமுள்ள இருவர் அல்லது அதற்கு மேற்பட்ட நபர்கள் நீதிமன்ற அனுமதியுடன்",
        "The Governor of the State directly", "மாநில ஆளுநர் நேரடியாக",
        "C",
        "Section 92 of CPC provides that in cases of alleged breach of any express or constructive trust for public charitable purposes, the Advocate General or two or more persons with interest and leave of the court may institute a suit.",
        "சிவில் நடைமுறைச் சட்டம் பிரிவு 92 பொது அறக்கட்டளையின் விதிமீறல் வழக்குகளில், தலைமை வழக்கறிஞர் அல்லது அறக்கட்டளையில் ஆர்வமுள்ள இருவர் நீதிமன்ற அனுமதியுடன் வழக்குத் தொடரலாம் என்று வழங்குகிறது.",
        "Incorrect. Not exclusive to Charity Commissioner.", "தவறு. அறக்கட்டளை ஆணையருக்கு மட்டுமேயானது அல்ல.",
        "Incorrect. NGOs cannot file directly under Sec 92 without complying with statutory conditions.", "தவறு. அரசு சாரா அமைப்புகள் சட்டப்பூர்வ நிபந்தனைகளின்றி நேரடியாக தொடர முடியாது.",
        "Correct. The Advocate General or two interested persons with court leave can institute the suit.", "சரி. தலைமை வழக்கறிஞர் அல்லது நீதிமன்ற அனுமதியுடன் ஆர்வமுள்ள இரு நபர்கள் வழக்குத் தொடரலாம்.",
        "Incorrect. Governor does not institute civil litigation directly.", "தவறு. ஆளுநர் நேரடியாக சிவில் வழக்குகளைத் தொடுப்பதில்லை.",
        "Sec 91 CPC = Public Nuisance; Sec 92 CPC = Public Charities / Trusts.",
        "சிபிசி பிரிவு 91 = பொதுத் தொல்லை; சிபிசி பிரிவு 92 = பொது அறக்கட்டளைகள்.",
        "This function preserves public trusts from mismanagement or diversion of dedicated assets.",
        "இப்பணி பொது அறக்கட்டளைகள் தவறாக நிர்வகிக்கப்படுவதில் இருந்தும் சொத்துக்கள் விரயமாவதில் இருந்தும் பாதுகாக்கிறது."
    )

    # Q32 (D)
    add_q(
        "ADVG_E_032", "Quorum in Assembly",
        "Does the presence of the Advocate General count towards the quorum required to constitute a meeting of the State Legislative Assembly?",
        "மாநில சட்டப் பேரவையின் கூட்டத்தை நடத்துவதற்குத் தேவையான குறைந்தபட்ச உறுப்பினர்களின் எண்ணிக்கையில் (Quorum) தலைமை வழக்கறிஞரின் இருப்பு கணக்கிடப்படுமா?",
        "Yes, whenever he is present in the chamber", "ஆம், அவர் அவையில் இருக்கும் போதெல்லாம் கணக்கிடப்படும்",
        "Yes, if permitted by the Speaker", "ஆம், சபாநாயகர் அனுமதித்தால் கணக்கிடப்படும்",
        "Yes, on legal discussion days", "ஆம், சட்ட விவாத நாட்களில் கணக்கிடப்படும்",
        "No, his presence does not count towards the quorum of the House", "இல்லை, அவையின் குறைந்தபட்ச உறுப்பினர் எண்ணிக்கையில் அவரது இருப்பு கணக்கிடப்படாது",
        "D",
        "Under Article 189(3), quorum is calculated based on the total number of members of the House. Since the Advocate General is not a member of the Legislative Assembly, his presence does not count toward the quorum.",
        "உறுப்பு 189(3)-ன் படி, அவையின் மொத்த உறுப்பினர்களின் அடிப்படையில் கோரம் கணக்கிடப்படுகிறது. தலைமை வழக்கறிஞர் சட்டமன்ற உறுப்பினர் அல்ல என்பதால், அவரது இருப்பு கோரத்திற்கு கணக்கிடப்படாது.",
        "Incorrect. He is not an MLA; therefore, his presence does not count for quorum.", "தவறு. அவர் ஒரு எம்.எல்.ஏ அல்ல; எனவே, அவரது வருகை கோரத்திற்கு கணக்கில் வராது.",
        "Incorrect. Speaker has no power to count non-members towards quorum.", "தவறு. உறுப்பினரல்லாதவர்களை கோரத்திற்கு கணக்கிட சபாநாயகருக்கு அதிகாரம் இல்லை.",
        "Incorrect. Legal debate days do not alter constitutional quorum rules.", "தவறு. சட்ட விவாத நாட்கள் அரசியலமைப்பு கோரம் விதிகளை மாற்றாது.",
        "Correct. The Advocate General's presence does not count towards quorum under Article 189(3).", "சரி. உறுப்பு 189(3)-ன் கீழ் தலைமை வழக்கறிஞரின் வருகை கோரத்திற்கு கணக்கிடப்படாது.",
        "Quorum for State Legislature under Art 189(3) is 10 members or one-tenth of total membership, whichever is greater.",
        "உறுப்பு 189(3)-ன் கீழ் சட்டமன்றக் கூட்டத்திற்கான கோரம் 10 உறுப்பினர்கள் அல்லது மொத்த உறுப்பினர்களில் பத்தில் ஒரு பங்கு ஆகும்.",
        "Though entitled to speak under Art 177, he remains a non-member for all legislative counts.",
        "உறுப்பு 177-ன் கீழ் பேச உரிமை பெற்றிருந்தாலும், சட்டமன்ற வாக்கெடுப்பு மற்றும் எண்ணிக்கை விவகாரங்களில் அவர் ஓர் உறுப்பினர் அல்லர்."
    )

    # Q33 (A)
    add_q(
        "ADVG_E_033", "Constitutional Amendment Article Link",
        "Which pair of Articles shows the correct Union-State parallel regarding legislative participation of the first law officer without the right to vote?",
        "வாக்குரிமை இன்றி சட்டத்துறையில் பங்கேற்கும் முதன்மை சட்ட அதிகாரியின் உரிமையில் சரியான ஒன்றியம்-மாநில இணையான உறுப்புகளைக் காட்டும் இணை எது?",
        "Union: Article 88 | State: Article 177", "ஒன்றியம்: உறுப்பு 88 | மாநிலம்: உறுப்பு 177",
        "Union: Article 76 | State: Article 165", "ஒன்றியம்: உறுப்பு 76 | மாநிலம்: உறுப்பு 165",
        "Union: Article 105 | State: Article 194", "ஒன்றியம்: உறுப்பு 105 | மாநிலம்: உறுப்பு 194",
        "Union: Article 143 | State: Article 213", "ஒன்றியம்: உறுப்பு 143 | மாநிலம்: உறுப்பு 213",
        "A",
        "Article 88 gives the Attorney General the right to speak and take part in Parliament without voting; Article 177 gives identical rights to the Advocate General in the State Legislature.",
        "உறுப்பு 88 நாடாளுமன்றத்தில் வாக்குரிமையின்றி பேசவும் பங்கேற்கவும் அட்டர்னி ஜெனரலுக்கு உரிமையளிக்கிறது; உறுப்பு 177 மாநில சட்டமன்றத்தில் தலைமை வழக்கறிஞருக்கு அதே உரிமைகளை அளிக்கிறது.",
        "Correct. Art 88 (Union) and Art 177 (State) are the exact parallel provisions for legislative participation.", "சரி. உறுப்பு 88 (ஒன்றியம்) மற்றும் உறுப்பு 177 (மாநிலம்) சட்டமன்ற பங்கேற்பிற்கான இணையான விதிகளாகும்.",
        "Incorrect. Articles 76 and 165 deal with appointment and office, not legislative participation.", "தவறு. உறுப்புகள் 76 மற்றும் 165 நியமனம் மற்றும் அலுவலகம் பற்றியவை, சட்டமன்றப் பங்கேற்பு பற்றியவை அல்ல.",
        "Incorrect. Articles 105 and 194 deal with privileges, not the right to speak itself.", "தவறு. உறுப்புகள் 105 மற்றும் 194 சிறப்புரிமைகள் பற்றியவை, பேசும் உரிமை பற்றியவை அல்ல.",
        "Incorrect. Article 143 is SC advisory jurisdiction; Article 213 is Governor ordinance power.", "தவறு. உறுப்பு 143 உச்ச நீதிமன்ற ஆலோசனை வரம்பு; உறுப்பு 213 ஆளுநரின் அவசரச் சட்ட அதிகாரம்.",
        "Mnemonic: 88 + 89 = 177 (The 89-rule links many Union provisions to State provisions).",
        "நினைவுக்குறிப்பு: 88 + 89 = 177 (89-விதி ஒன்றியத்தின் பல விதிகளை மாநில விதிகளோடு இணைக்கிறது).",
        "Similarly, Art 76 + 89 = 165 (Office) and Art 105 + 89 = 194 (Privileges).",
        "இதேபோல், உறுப்பு 76 + 89 = 165 (அலுவலகம்) மற்றும் உறுப்பு 105 + 89 = 194 (சிறப்புரிமைகள்)."
    )

    # Q34 (B)
    add_q(
        "ADVG_E_034", "Civil Services Protection Exemption",
        "Are the constitutional safeguards under Article 311 (dismissal, removal, reduction in rank) available to the Advocate General of a State?",
        "உறுப்பு 311-ன் கீழ் உள்ள அரசியலமைப்புப் பாதுகாப்புகள் (பணிநீக்கம், பதவியிறக்கம்) மாநில தலைமை வழக்கறிஞருக்குக் கிடைக்குமா?",
        "Yes, he is a civil servant of the State", "ஆம், அவர் மாநிலத்தின் குடிமைப் பணி ஊழியர் ஆவார்",
        "No, because he is not a member of a civil service or holding a civil post", "இல்லை, ஏனெனில் அவர் ஒரு குடிமைப் பணியின் உறுப்பினரோ அல்லது குடிமைப் பதவியை வகிப்பவரோ அல்ல",
        "Yes, but only after completing 5 years of service", "ஆம், ஆனால் 5 ஆண்டுகள் பணி முடித்த பிறகு மட்டுமே",
        "Yes, with the prior approval of the High Court", "ஆம், உயர் நீதிமன்றத்தின் முன் அனுமதியுடன்",
        "B",
        "The Advocate General is a constitutional appointee holding office during the pleasure of the Governor. He does not hold a 'civil post' under the State and is not entitled to the protection of Article 311.",
        "தலைமை வழக்கறிஞர் ஆளுநரின் விருப்பத்தின் பேரில் பதவி வகிக்கும் அரசியலமைப்பு நியமனப் பொறுப்பாளர் ஆவார். அவர் அரசின் கீழ் 'குடிமைப் பதவியை' வகிக்கவில்லை, எனவே உறுப்பு 311-ன் பாதுகாப்புக்கு உரிமையற்றவர்.",
        "Incorrect. He is not a civil servant; he is a professional lawyer holding a constitutional office.", "தவறு. அவர் அரசு ஊழியர் அல்ல; அவர் ஓர் அரசியலமைப்பு பதவியை வகிக்கும் தொழில்முறை வழக்கறிஞர்.",
        "Correct. Article 311 does not apply to the Advocate General.", "சரி. உறுப்பு 311 தலைமை வழக்கறிஞருக்குப் பொருந்தாது.",
        "Incorrect. Tenure is during pleasure, not subject to a 5-year security threshold.", "தவறு. பதவிக்காலம் ஆளுநரின் விருப்பத்திற்கு உட்பட்டது, 5 ஆண்டு பணிப் பாதுகாப்புக்கு உட்பட்டதல்ல.",
        "Incorrect. High Court approval is not required for termination under pleasure doctrine.", "தவறு. விருப்பக் கோட்பாட்டின் கீழ் பதவிநீக்கம் செய்ய உயர் நீதிமன்ற அனுமதி தேவையில்லை.",
        "Because Article 311 does not apply, the Governor can terminate the AG's appointment without a formal departmental inquiry.",
        "உறுப்பு 311 பொருந்தாது என்பதால், ஆளுநர் முறையான துறைசார் விசாரணை இன்றி அட்வகேட் ஜெனரலின் பதவியை முடிக்க முடியும்.",
        "His relationship with the State Government is fundamentally that of counsel and client, overlaid with public duties.",
        "அரசுடனான அவரது உறவு அடிப்படையில் வழக்கறிஞர் மற்றும் வாடிக்கையாளர் என்ற உறவாகும், அத்துடன் பொதுக் கடமைகளும் இணைக்கப்பட்டுள்ளன."
    )

    # Q35 (C)
    add_q(
        "ADVG_E_035", "Representation in Supreme Court",
        "Can the Advocate General of a State appear before the Supreme Court of India on behalf of his State?",
        "தனது மாநிலத்தின் சார்பாக இந்திய உச்ச நீதிமன்றத்தின் முன் மாநில தலைமை வழக்கறிஞர் முன்னிலையாகி வாதாட முடியுமா?",
        "No, he can only appear in the High Court of his State", "இல்லை, அவர் தனது மாநில உயர் நீதிமன்றத்தில் மட்டுமே ஆஜராக முடியும்",
        "Only if he is designated as a Senior Advocate by the Supreme Court", "அவர் உச்ச நீதிமன்றத்தால் மூத்த வழக்கறிஞராக நியமிக்கப்பட்டிருந்தால் மட்டுமே",
        "Yes, when instructed and briefed by the State Government to represent it", "ஆம், மாநில அரசால் அறிவுறுத்தப்பட்டு வழக்குப் பொறுப்பு ஒப்படைக்கப்படும் போது",
        "No, only the Attorney General of India can represent States in the Supreme Court", "இல்லை, இந்திய அட்டர்னி ஜெனரல் மட்டுமே உச்ச நீதிமன்றத்தில் மாநிலங்களைப் பிரதிநிதித்துவப்படுத்த முடியும்",
        "C",
        "The Advocate General frequently represents his State Government before the Supreme Court in important constitutional matters, inter-state disputes, and statutory appeals when briefed by the State.",
        "முக்கிய அரசியலமைப்பு விவகாரங்கள், மாநிலங்களுக்கு இடையேயான தாவாக்கள் மற்றும் சட்டப்பூர்வ மேல்முறையீடுகளில் மாநில அரசு அறிவுறுத்தும் போது, தலைமை வழக்கறிஞர் உச்ச நீதிமன்றத்தில் தனது மாநிலத்தை பிரதிநிதித்துவப்படுத்துகிறார்.",
        "Incorrect. His appearance is not legally restricted to the High Court.", "தவறு. அவரது முன்னிலையாகும் உரிமை உயர் நீதிமன்றத்திற்கு மட்டுமே மட்டுப்படுத்தப்படவில்லை.",
        "Incorrect. Designation by SC specifically is not a prerequisite for appearing for the State.", "தவறு. உச்ச நீதிமன்றத்தால் மூத்த வழக்கறிஞராக நியமிக்கப்படுவது மாநிலத்திற்காக ஆஜராவதற்கான முன்நிபந்தனை அல்ல.",
        "Correct. Can appear in the Supreme Court when instructed by the State Government.", "சரி. மாநில அரசு அறிவுறுத்தும் போது உச்ச நீதிமன்றத்தில் ஆஜராக முடியும்.",
        "Incorrect. Attorney General represents the Union of India, not individual State Governments.", "தவறு. அட்டர்னி ஜெனரல் இந்திய ஒன்றியத்தைப் பிரதிநிதித்துவப்படுத்துகிறார், மாநில அரசுகளை அல்ல.",
        "In Article 131 original suits between Union and State or between States, the respective Advocate Generals often lead the State legal teams.",
        "உறுப்பு 131-ன் கீழ் ஒன்றியம்-மாநிலம் இடையிலான அசல் வழக்குகளில் அந்தந்த மாநில அட்வகேட் ஜெனரல்களே மாநில சட்டக் குழுவிற்கு தலைமை தாங்குகின்றனர்.",
        "State Advocates General are enrolled advocates entitled to practice in the Supreme Court under the Advocates Act 1961.",
        "மாநில தலைமை வழக்கறிஞர்கள் வழக்கறிஞர்கள் சட்டம் 1961-ன் கீழ் உச்ச நீதிமன்றத்தில் பயிற்சி செய்ய தகுதியுள்ள பதிவுபெற்ற வழக்கறிஞர்கள் ஆவர்."
    )

    # Q36 (D)
    add_q(
        "ADVG_E_036", "Bar Council Role",
        "What is the statutory role of the Advocate General in the State Bar Council under the Advocates Act, 1961?",
        "வழக்கறிஞர்கள் சட்டம் 1961-ன் கீழ் மாநில பார் கவுன்சிலில் தலைமை வழக்கறிஞரின் சட்டப்பூர்வ பங்கு என்ன?",
        "He is the permanent elected Chairman of the Bar Council", "அவர் பார் கவுன்சிலின் நிரந்தர தேர்ந்தெடுக்கப்பட்ட தலைவர் ஆவார்",
        "He has no connection with the Bar Council", "அவருக்கு பார் கவுன்சிலுடன் எந்த தொடர்பும் இல்லை",
        "He is the Secretary of the Bar Council", "அவர் பார் கவுன்சிலின் செயலாளர் ஆவார்",
        "He is an ex-officio member of the State Bar Council", "அவர் மாநில பார் கவுன்சிலின் பதவிவழி (Ex-officio) உறுப்பினர் ஆவார்",
        "D",
        "Under Section 3(2)(a) of the Advocates Act, 1961, the Advocate General of the State is an ex-officio member of the State Bar Council.",
        "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 3(2)(a)-ன் கீழ், மாநில தலைமை வழக்கறிஞர் மாநில பார் கவுன்சிலின் பதவிவழி உறுப்பினர் ஆவார்.",
        "Incorrect. The Chairman of the State Bar Council is elected from among its members.", "தவறு. மாநில பார் கவுன்சில் தலைவர் அதன் உறுப்பினர்களிலிருந்து தேர்ந்தெடுக்கப்படுகிறார்.",
        "Incorrect. He is an integral statutory member.", "தவறு. அவர் ஒரு சட்டப்பூர்வ உறுப்பினர் ஆவார்.",
        "Incorrect. Secretary is a full-time administrative employee.", "தவறு. செயலாளர் முழுநேர நிர்வாக ஊழியர் ஆவார்.",
        "Correct. Section 3(2)(a) makes the Advocate General an ex-officio member of the State Bar Council.", "சரி. பிரிவு 3(2)(a) தலைமை வழக்கறிஞரை மாநில பார் கவுன்சிலின் பதவிவழி உறுப்பினராக்குகிறது.",
        "Similarly, the Attorney General of India and Solicitor General of India are ex-officio members of the Bar Council of India.",
        "இதேபோல், இந்திய அட்டர்னி ஜெனரல் மற்றும் சொலிசிட்டர் ஜெனரல் ஆகியோர் இந்திய பார் கவுன்சிலின் பதவிவழி உறுப்பினர்கள் ஆவர்.",
        "The Advocate General is traditionally regarded as the leader of the State Bar.",
        "தலைமை வழக்கறிஞர் பாரம்பரியமாக மாநில வழக்கறிஞர் சங்கத்தின் (State Bar) தலைவராக மதிக்கப்படுகிறார்."
    )

    # Q37 (A)
    add_q(
        "ADVG_E_037", "Comparison with Attorney General Tenure",
        "Both the Attorney General of India and the Advocate General of a State hold office during the pleasure of their respective appointing authorities. Who exercises this pleasure for the Advocate General?",
        "இந்திய அட்டர்னி ஜெனரல் மற்றும் மாநில அட்வகேட் ஜெனரல் ஆகிய இருவரும் தத்தமது நியமன அதிகாரிகளின் விருப்பம் உள்ளவரை பதவி வகிக்கின்றனர். அட்வகேட் ஜெனரலுக்கு இந்த விருப்ப அதிகாரத்தைப் பயன்படுத்துபவர் யார்?",
        "The Governor of the State", "மாநில ஆளுநர்",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "The State Legislative Assembly", "மாநில சட்டப் பேரவை",
        "The Chief Justice of the High Court", "உயர் நீதிமன்ற தலைமை நீதிபதி",
        "A",
        "Article 165(3) clearly provides: 'The Advocate General shall hold office during the pleasure of the Governor'.",
        "உறுப்பு 165(3) தெளிவாகக் கூறுகிறது: 'தலைமை வழக்கறிஞர் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிப்பார்'.",
        "Correct. The Governor exercises the pleasure doctrine under Article 165(3).", "சரி. உறுப்பு 165(3)-ன் கீழ் ஆளுநர் இந்த விருப்ப அதிகாரத்தைப் பயன்படுத்துகிறார்.",
        "Incorrect. The President exercises pleasure for the Attorney General under Art 76(4).", "தவறு. உறுப்பு 76(4)-ன் கீழ் அட்டர்னி ஜெனரலுக்கு குடியரசுத் தலைவர் விருப்ப அதிகாரத்தைப் பயன்படுத்துகிறார்.",
        "Incorrect. State Legislature has no removal or pleasure power over the AG.", "தவறு. அட்வகேட் ஜெனரல் மீது சட்டமன்றத்திற்கு பதவிநீக்க அதிகாரமோ அல்லது விருப்ப அதிகாரமோ இல்லை.",
        "Incorrect. Judiciary does not exercise pleasure over executive law officers.", "தவறு. நீதித்துறை நிர்வாக சட்ட அதிகாரிகள் மீது விருப்ப அதிகாரத்தைப் பயன்படுத்துவதில்லை.",
        "Union: Pleasure of President (Art 76(4)); State: Pleasure of Governor (Art 165(3)).",
        "ஒன்றியம்: குடியரசுத் தலைவரின் விருப்பம் (உறுப்பு 76(4)); மாநிலம்: ஆளுநரின் விருப்பம் (உறுப்பு 165(3)).",
        "The Governor exercises this pleasure on the advice of the State Cabinet headed by the Chief Minister.",
        "முதலமைச்சர் தலைமையிலான மாநில அமைச்சரவையின் ஆலோசனையின் பேரிலேயே ஆளுநர் இந்த விருப்ப அதிகாரத்தைப் பயன்படுத்துகிறார்."
    )

    # Q38 (B)
    add_q(
        "ADVG_E_038", "Precedence among States",
        "When Advocate Generals of different States appear before the Supreme Court, how is their mutual precedence determined under the Advocates Act, 1961?",
        "பல்வேறு மாநிலங்களின் தலைமை வழக்கறிஞர்கள் உச்ச நீதிமன்றத்தில் முன்னிலையாகும் போது, வழக்கறிஞர்கள் சட்டம் 1961-ன் படி அவர்களுக்கிடையேயான முன்னுரிமை எவ்வாறு தீர்மானிக்கப்படுகிறது?",
        "Alphabetical order of the State names", "மாநிலப் பெயர்களின் அகரவரிசைப்படி",
        "Seniority according to their respective dates of appointment as Advocate General", "தலைமை வழக்கறிஞராக நியமிக்கப்பட்ட தேதிகளின் அடிப்படையிலான பணி மூப்புப்படி",
        "Population of their respective States", "அவர்களின் மாநிலங்களின் மக்கள் தொகை அடிப்படையில்",
        "Discretion of the Chief Justice of India", "இந்தியத் தலைமை நீதிபதியின் விருப்புரிமைப்படி",
        "B",
        "Under Section 23(4) of the Advocates Act, 1961, the Advocate Generals of different States have seniority and precedence inter se according to the dates of their respective appointments.",
        "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 23(4)-ன் கீழ், பல்வேறு மாநிலங்களின் தலைமை வழக்கறிஞர்கள் அவர்கள் நியமிக்கப்பட்ட தேதிகளின் அடிப்படையிலான பணி மூப்பின்படியே தங்களுக்குள் முன்னுரிமை பெறுகின்றனர்.",
        "Incorrect. Alphabetical order of States is not used.", "தவறு. மாநிலங்களின் அகரவரிசை பயன்படுத்தப்படுவதில்லை.",
        "Correct. Precedence among Advocate Generals is determined by the date of appointment.", "சரி. தலைமை வழக்கறிஞர்களுக்கு இடையேயான முன்னுரிமை அவர்கள் நியமிக்கப்பட்ட தேதியின்படி தீர்மானிக்கப்படுகிறது.",
        "Incorrect. Population has no legal relevance in bar seniority.", "தவறு. வழக்கறிஞர் மூப்புக்கு மக்கள் தொகைக்கு எந்த சட்டப்பூர்வ பொருத்தமும் இல்லை.",
        "Incorrect. CJI does not determine statutory precedence under Section 23.", "தவறு. பிரிவு 23-ன் கீழ் சட்டப்பூர்வ முன்னுரிமையை CJI தீர்மானிப்பதில்லை.",
        "Section 23 of the Advocates Act, 1961 lays down the complete code of pre-audience at the Indian Bar.",
        "வழக்கறிஞர்கள் சட்டம் 1961-ன் பிரிவு 23 இந்திய வழக்கறிஞர் சங்கத்தின் முழுமையான முன்னுரிமை விதியை வகுத்துள்ளது.",
        "Earlier appointment date gives higher precedence among State Advocate Generals.",
        "முந்தைய நியமனத் தேதி மாநில தலைமை வழக்கறிஞர்களுக்கு இடையே அதிக முன்னுரிமையை அளிக்கிறது."
    )

    # Q39 (C)
    add_q(
        "ADVG_E_039", "Company Directorship Restriction",
        "Can the Advocate General of a State accept an appointment as a director in any company or corporation without government permission?",
        "அரசு அனுமதியின்றி எந்தவொரு நிறுவனம் அல்லது கார்ப்பரேஷனில் இயக்குநராக நியமிக்கப்படுவதை மாநில தலைமை வழக்கறிஞர் ஏற்க முடியுமா?",
        "Yes, without any restrictions as he is not a civil servant", "ஆம், அவர் அரசு ஊழியர் அல்ல என்பதால் எந்தக் கட்டுப்பாடும் இன்றி ஏற்கலாம்",
        "Yes, but only in government corporations", "ஆம், ஆனால் அரசு நிறுவனங்களில் மட்டுமே",
        "No, he should not accept appointment as a director in any company without the permission of the State Government", "இல்லை, மாநில அரசின் அனுமதியின்றி எந்தவொரு நிறுவனத்திலும் இயக்குநராக நியமிக்கப்படுவதை அவர் ஏற்கக்கூடாது",
        "Yes, if permitted by the Registrar of Companies", "ஆம், நிறுவனங்களின் பதிவாளர் அனுமதித்தால் ஏற்கலாம்",
        "C",
        "To prevent conflict of interest, the rules governing law officers explicitly mandate that the Advocate General should not accept appointment as a director in any company without the permission of the State Government.",
        "நலன் முரண்பாட்டைத் தடுப்பதற்காக, சட்ட அதிகாரிகளை நிர்வகிக்கும் விதிகள் தலைமை வழக்கறிஞர் மாநில அரசின் அனுமதியின்றி எந்தவொரு நிறுவனத்திலும் இயக்குநராக நியமிக்கப்படுவதை ஏற்கக்கூடாது என்று தெளிவாக ஆணையிடுகின்றன.",
        "Incorrect. Being a public law officer entails fiduciary duties restricting private directorships.", "தவறு. ஒரு பொது சட்ட அதிகாரியாக இருப்பது தனிப்பட்ட இயக்குநர் பதவிகளைக் கட்டுப்படுத்தும் பொறுப்பைக் கொண்டுள்ளது.",
        "Incorrect. Prior government permission is necessary for any company directorship.", "தவறு. எந்தவொரு நிறுவன இயக்குநர் பதவிக்கும் அரசின் முன் அனுமதி அவசியம்.",
        "Correct. Cannot accept directorship in any company without the State Government's permission.", "சரி. மாநில அரசின் அனுமதியின்றி எந்த நிறுவனத்திலும் இயக்குநர் பதவியை ஏற்க முடியாது.",
        "Incorrect. RoC has no role in approving law officers' directorships.", "தவறு. சட்ட அதிகாரிகளின் இயக்குநர் பதவிகளுக்கு ஒப்புதல் அளிப்பதில் RoC-க்கு எந்தப் பங்கும் இல்லை.",
        "Key Restrictions on AG: 1. No brief against State; 2. No criminal defense without sanction; 3. No company directorship without sanction.",
        "தலைமை வழக்கறிஞருக்கான முக்கிய கட்டுப்பாடுகள்: 1. அரசுக்கு எதிராக வாதாடக்கூடாது; 2. அனுமதியின்றி குற்றவாளிகளை ஆதரிக்கக்கூடாது; 3. அனுமதியின்றி நிறுவன இயக்குநர் பதவி ஏற்கக்கூடாது.",
        "These restrictions maintain the integrity and public trust associated with the constitutional office.",
        "இக்கட்டுப்பாடுகள் அரசியலமைப்பு பதவியுடன் தொடர்புடைய நாணயத்தையும் பொது நம்பிக்கையையும் பாதுகாக்கின்றன."
    )

    # Q40 (D)
    add_q(
        "ADVG_E_040", "Legal Advice Binding Nature",
        "Is the legal advice tendered by the Advocate General legally binding on the State Government?",
        "மாநில தலைமை வழக்கறிஞர் வழங்கும் சட்ட ஆலோசனை மாநில அரசைக் கட்டுப்படுத்துமா?",
        "Yes, it is legally binding and has the status of law", "ஆம், அது சட்டப்பூர்வமாகக் கட்டுப்படுத்துவதோடு சட்ட அந்தஸ்தையும் கொண்டது",
        "Yes, unless overruled by the High Court", "ஆம், உயர் நீதிமன்றத்தால் ரத்து செய்யப்படாத வரை கட்டுப்படுத்தும்",
        "Yes, if approved by the Governor in writing", "ஆம், ஆளுநரால் எழுத்துப்பூர்வமாக அங்கீகரிக்கப்பட்டால் கட்டுப்படுத்தும்",
        "No, the advice is advisory in nature and not binding on the State Government", "இல்லை, அந்த ஆலோசனை வழிகாட்டும் தன்மை கொண்டதே தவிர மாநில அரசைக் கட்டுப்படுத்தாது",
        "D",
        "The legal advice tendered by the Advocate General under Article 165(2) is advisory in nature. The State Government is free to accept, modify, or reject it, though in practice it carries immense persuasive authority.",
        "உறுப்பு 165(2)-ன் கீழ் தலைமை வழக்கறிஞர் வழங்கும் சட்ட ஆலோசனை வழிகாட்டும் தன்மை கொண்டதே ஆகும். மாநில அரசு அதை ஏற்கவோ, மாற்றியமைக்கவோ அல்லது நிராகரிக்கவோ சுதந்திரம் கொண்டது, எனினும் நடைமுறையில் அதற்கு பெரும் மதிப்பு உண்டு.",
        "Incorrect. Advice of counsel is not binding legislation or judicial decree.", "தவறு. வழக்கறிஞரின் ஆலோசனை கட்டுப்படுத்தும் சட்டமோ அல்லது நீதிமன்றத் தீர்ப்போ அல்ல.",
        "Incorrect. It is not an order requiring judicial overruling.", "தவறு. இது நீதிமன்ற மறுப்பு தேவைப்படும் உத்தரவு அல்ல.",
        "Incorrect. Executive approval does not make advisory counsel legally binding.", "தவறு. நிர்வாக ஒப்புதல் ஆலோசனை வழிகாட்டலை சட்டப்பூர்வமாக கட்டுப்படுத்துவதாக மாற்றாது.",
        "Correct. The advice is advisory and not binding on the State Government.", "சரி. ஆலோசனை வழிகாட்டும் தன்மை கொண்டதே அன்றி மாநில அரசைக் கட்டுப்படுத்தாது.",
        "Just as Attorney General's advice is not binding on the Union Cabinet, Advocate General's advice is not binding on the State Cabinet.",
        "அட்டர்னி ஜெனரலின் ஆலோசனை ஒன்றிய அமைச்சரவையைக் கட்டுப்படுத்தாது என்பதைப் போலவே, அட்வகேட் ஜெனரலின் ஆலோசனை மாநில அமைச்சரவையைக் கட்டுப்படுத்தாது.",
        "However, acting contrary to the AG's formal written advice requires strong justification on record.",
        "எனினும், தலைமை வழக்கறிஞரின் முறையான எழுத்துப்பூர்வ ஆலோசனைக்கு மாறாக செயல்பட வலுவான காரணங்கள் ஆவணத்தில் இருக்க வேண்டும்."
    )

    # --- 41 to 50 ---
    # Q41 (A)
    add_q(
        "ADVG_E_041", "High Court Judge Age Bar Rule",
        "Can a retired High Court Judge be appointed as the Advocate General of a State?",
        "ஓய்வு பெற்ற உயர் நீதிமன்ற நீதிபதி ஒருவர் ஒரு மாநிலத்தின் தலைமை வழக்கறிஞராக நியமிக்கப்பட முடியுமா?",
        "Yes, because retirement from judicial service does not disqualify a person from holding office under the pleasure doctrine", "ஆம், ஏனெனில் நீதித்துறைப் பணியிலிருந்து ஓய்வு பெறுவது விருப்பக் கோட்பாட்டின் கீழ் பதவி வகிப்பதற்கான தகுதியை இழக்கச் செய்யாது",
        "No, Article 220 completely debars retired HC judges from holding any government office", "இல்லை, உறுப்பு 220 ஓய்வு பெற்ற உயர் நீதிமன்ற நீதிபதிகள் எந்த அரசு பதவியையும் வகிப்பதை முற்றிலும் தடை செய்கிறது",
        "No, because the age limit of 62 years applies strictly to the Advocate General", "இல்லை, ஏனெனில் 62 வயது வரம்பு தலைமை வழக்கறிஞருக்கும் கண்டிப்பாகப் பொருந்தும்",
        "Only with the special recommendation of the Chief Justice of India", "இந்திய தலைமை நீதிபதியின் சிறப்புப் பரிந்துரையுடன் மட்டுமே நியமிக்கப்படலாம்",
        "A",
        "In G.D. Karkare v. T.L. Shevde (1952) and Atlas Cycle Industries case, it was settled that a person who has crossed the HC retirement age of 62 (or a retired HC judge) can be appointed as Advocate General, as Article 165 prescribes qualification to be appointed, not tenure/age limitations of a sitting judge.",
        "ஜி.டி. கார்கரே எதிர் டி.எல். ஷேவ்டே (1952) மற்றும் அட்லஸ் சைக்கிள் இண்டஸ்ட்ரீஸ் வழக்குகளில், 62 வயதைக் கடந்த ஒருவர் (அல்லது ஓய்வு பெற்ற நீதிபதி) தலைமை வழக்கறிஞராக நியமிக்கப்படலாம் என்பது உறுதி செய்யப்பட்டது. ஏனெனில் உறுப்பு 165 நியமிக்கப்படுவதற்கான தகுதியை மட்டுமே குறிப்பிடுகிறது, நீதிபதியின் வயது வரம்பை அல்ல.",
        "Correct. A retired High Court judge or person over 62 can be appointed Advocate General.", "சரி. ஓய்வு பெற்ற உயர் நீதிமன்ற நீதிபதி அல்லது 62 வயதைக் கடந்த ஒருவர் தலைமை வழக்கறிஞராக நியமிக்கப்படலாம்.",
        "Incorrect. Article 220 restricts pleading in certain courts, but does not bar constitutional office of Advocate General.", "தவறு. உறுப்பு 220 சில நீதிமன்றங்களில் வாதாடுவதைக் கட்டுப்படுத்துகிறது, ஆனால் அட்வகேட் ஜெனரல் பதவியை அல்ல.",
        "Incorrect. 62 age limit applies to serving judges, not Advocate General.", "தவறு. 62 வயது வரம்பு பணியில் உள்ள நீதிபதிகளுக்குப் பொருந்தும், தலைமை வழக்கறிஞருக்கு அல்ல.",
        "Incorrect. CJI recommendation is not constitutionally required.", "தவறு. CJI-ன் பரிந்துரை அரசியலமைப்பு ரீதியாக அவசியமில்லை.",
        "Crucial Principle: Competence to be appointed (Art 217(2)) is required, not youth under 62.",
        "முக்கிய கோட்பாடு: நியமிக்கப்படுவதற்கான தகுதி (உறுப்பு 217(2)) மட்டுமே தேவை, 62 வயதுக்கு உட்பட்டவராக இருக்க வேண்டும் என்ற அவசியமில்லை.",
        "Several eminent jurists in Indian legal history served as Advocate General after retiring from the High Court bench.",
        "இந்திய சட்ட வரலாற்றில் பல புகழ்பெற்ற சட்ட வல்லுநர்கள் உயர் நீதிமன்றத்திலிருந்து ஓய்வு பெற்ற பின்னர் தலைமை வழக்கறிஞராக பணியாற்றியுள்ளனர்."
    )

    # Q42 (B)
    add_q(
        "ADVG_E_042", "Resignation Convention",
        "By convention, when does the Advocate General of a State usually submit his resignation?",
        "வழக்கப்படி (By convention), ஒரு மாநிலத்தின் தலைமை வழக்கறிஞர் எப்போது தனது பதவி விலகல் கடிதத்தை சமர்ப்பிக்கிறார்?",
        "When the High Court Chief Justice retires", "உயர் நீதிமன்ற தலைமை நீதிபதி ஓய்வு பெறும் போது",
        "When the State Council of Ministers resigns or is replaced", "மாநில அமைச்சரவை பதவி விலகும் போது அல்லது மாற்றப்படும் போது",
        "Every 3 years automatically", "ஒவ்வொரு 3 ஆண்டுகளுக்கும் தானாகவே",
        "When the financial year ends", "நிதியாண்டு முடிவடையும் போது",
        "B",
        "Conventionally, the Advocate General resigns when the Council of Ministers (the government) resigns or is replaced, as he is appointed on its recommendation.",
        "வழக்கமாக, அமைச்சரவை (அரசு) பதவி விலகும் போது அல்லது மாற்றப்படும் போது தலைமை வழக்கறிஞரும் பதவி விலகுகிறார், ஏனெனில் அவர் அதன் பரிந்துரையின் பேரிலேயே நியமிக்கப்படுகிறார்.",
        "Incorrect. Retirement of Chief Justice has no bearing on the Advocate General's tenure.", "தவறு. தலைமை நீதிபதியின் ஓய்வு தலைமை வழக்கறிஞரின் பதவிக்காலத்தில் எந்த தாக்கத்தையும் ஏற்படுத்தாது.",
        "Correct. By convention, the AG resigns when the government that appointed him falls or resigns.", "சரி. வழக்கப்படி, தன்னை நியமித்த அரசு வீழும் போது அல்லது பதவி விலகும் போது AG-யும் பதவி விலகுகிறார்.",
        "Incorrect. There is no 3-year automatic resignation rule.", "தவறு. 3 ஆண்டு தானியங்கி பதவி விலகல் விதி என்று எதுவும் இல்லை.",
        "Incorrect. Financial year closing has no connection to tenure.", "தவறு. நிதியாண்டு முடிவிற்கும் பதவிக்காலத்திற்கும் எந்த தொடர்பும் இல்லை.",
        "This convention ensures that the incoming government can appoint a law officer of its own confidence.",
        "இந்த மரபு புதிய அரசு தனக்கு நம்பிக்கையான ஒரு சட்ட அதிகாரியை நியமிக்க முடியும் என்பதை உறுதி செய்கிறது.",
        "However, a new government may choose to reappoint or continue the existing Advocate General.",
        "எனினும், ஒரு புதிய அரசு ஏற்கனவே உள்ள தலைமை வழக்கறிஞரையே மீண்டும் நியமிக்கவோ அல்லது தொடரவோ முடிவு செய்யலாம்."
    )

    # Q43 (C)
    add_q(
        "ADVG_E_043", "Removal Procedure",
        "What is the procedure required for removing the Advocate General of a State from office?",
        "மாநில தலைமை வழக்கறிஞரை பதவியில் இருந்து நீக்குவதற்குத் தேவையான நடைமுறை என்ன?",
        "Impeachment by the State Legislature with a special majority", "மாநில சட்டமன்றத்தில் சிறப்பு பெரும்பான்மையுடன் குற்றவியல் தீர்மானம் (இம்பீச்மெண்ட்)",
        "An inquiry by a sitting Supreme Court Judge under the Judges Inquiry Act", "நீதிபதிகள் விசாரணைச் சட்டத்தின் கீழ் உச்ச நீதிமன்ற நீதிபதியின் விசாரணை",
        "No formal procedure is required; the Governor can remove him at any time under the pleasure doctrine", "எந்த முறையான நடைமுறையும் தேவையில்லை; விருப்பக் கோட்பாட்டின் கீழ் ஆளுநர் அவரை எந்நேரமும் நீக்கலாம்",
        "A resolution approved by two-thirds of the High Court Collegium", "உயர் நீதிமன்ற கொலீஜியத்தின் மூன்றில் இரண்டு பங்கு பெரும்பான்மை தீர்மானம்",
        "C",
        "Under Article 165(3), the Advocate General holds office during the pleasure of the Governor. There is no constitutional procedure or ground (like misbehaviour or incapacity) required for his removal.",
        "உறுப்பு 165(3)-ன் கீழ் தலைமை வழக்கறிஞர் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார். அவரைப் பதவி நீக்கம் செய்ய எந்தவொரு அரசியலமைப்பு நடைமுறையோ அல்லது காரணங்களோ (தவறான நடத்தை அல்லது திறமையின்மை போன்றவை) தேவையில்லை.",
        "Incorrect. Impeachment applies to Judges and President, not Advocate General.", "தவறு. இம்பீச்மெண்ட் என்பது நீதிபதிகள் மற்றும் குடியரசுத் தலைவருக்குரியது, அட்வகேட் ஜெனரலுக்கு அல்ல.",
        "Incorrect. Judges Inquiry Act does not apply to law officers.", "தவறு. நீதிபதிகள் விசாரணைச் சட்டம் சட்ட அதிகாரிகளுக்குப் பொருந்தாது.",
        "Correct. Can be removed at any time by the Governor without procedural formalities.", "சரி. எந்தவொரு நடைமுறைச் சடங்குகளும் இன்றி ஆளுநரால் எந்நேரமும் நீக்கப்படலாம்.",
        "Incorrect. High Court Collegium has no authority over executive appointments or removals.", "தவறு. நிர்வாக நியமனங்கள் அல்லது நீக்கங்கள் மீது உயர் நீதிமன்ற கொலீஜியத்திற்கு எந்த அதிகாரமும் இல்லை.",
        "AG does not have security of tenure; his office is subject to the pleasure of the Governor (exercised on Cabinet advice).",
        "அட்வகேட் ஜெனரலுக்கு பதவிக் காலப் பாதுகாப்பு கிடையாது; அவரது பதவி ஆளுநரின் விருப்பத்திற்கு உட்பட்டது (அமைச்சரவை ஆலோசனையின்படி).",
        "In B.P. Singhal v. Union of India (2010), the Supreme Court affirmed the executive's wide discretion under pleasure doctrine.",
        "பி.பி. சிங்கால் வழக்கில் (2010), விருப்பக் கோட்பாட்டின் கீழ் நிர்வாகத்தின் பரந்த அதிகாரத்தை உச்ச நீதிமன்றம் உறுதி செய்தது."
    )

    # Q44 (D)
    add_q(
        "ADVG_E_044", "Oath of Office",
        "Who administers the oath of office to the Advocate General of a State?",
        "மாநில தலைமை வழக்கறிஞருக்கு பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?",
        "The Chief Justice of the High Court", "உயர் நீதிமன்ற தலைமை நீதிபதி",
        "The Law Secretary of the State", "மாநில சட்டத்துறைச் செயலாளர்",
        "The Speaker of the State Legislative Assembly", "சட்டப் பேரவைத் தலைவர்",
        "The Governor or some person appointed on that behalf by him", "ஆளுநர் அல்லது அவரால் இதற்கென நியமிக்கப்பட்ட ஒருவர்",
        "D",
        "The Governor or a person designated by him administers the oath of office to constitutional appointees of the State, including the Advocate General.",
        "ஆளுநர் அல்லது அவரால் நியமிக்கப்பட்ட ஒருவர் தலைமை வழக்கறிஞர் உட்பட மாநிலத்தின் அரசியலமைப்புப் பொறுப்பாளர்களுக்கு பதவிப் பிரமாணம் செய்து வைக்கிறார்.",
        "Incorrect. High Court Chief Justice administers oath to the Governor and HC Judges, not the Advocate General.", "தவறு. உயர் நீதிமன்ற தலைமை நீதிபதி ஆளுநருக்கும் நீதிபதிகளுக்கும் பதவிப் பிரமாணம் செய்கிறார், அட்வகேட் ஜெனரலுக்கு அல்ல.",
        "Incorrect. Law Secretary is an administrative officer.", "தவறு. சட்டச் செயலாளர் ஓர் நிர்வாக அதிகாரி.",
        "Incorrect. Speaker administers oath to newly elected MLAs.", "தவறு. சபாநாயகர் புதிதாக தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏக்களுக்கு பதவிப் பிரமாணம் செய்கிறார்.",
        "Correct. The Governor or his designated representative administers the oath.", "சரி. ஆளுநர் அல்லது அவரால் நியமிக்கப்பட்ட பிரதிநிதி பதவிப் பிரமாணம் செய்து வைக்கிறார்.",
        "The Advocate General takes an oath to bear true faith and allegiance to the Constitution of India.",
        "தலைமை வழக்கறிஞர் இந்திய அரசியலமைப்பிற்கு உண்மையான விசுவாசத்தையும் பற்றுதலையும் கொண்டிருப்பதாக உறுதிமொழி ஏற்கிறார்.",
        "He undertakes to uphold the sovereignty and integrity of India and perform duties without fear or favour.",
        "அவர் இந்தியாவின் இறையாண்மையையும் ஒருமைப்பாட்டையும் நிலைநிறுத்தவும், பயமோ ஆதரவோ இன்றி கடமைகளை ஆற்றவும் உறுதியளிக்கிறார்."
    )

    # Q45 (A)
    add_q(
        "ADVG_E_045", "Bicameral Legislature Right",
        "In States with a bicameral legislature (both Legislative Assembly and Legislative Council), in which House does the Advocate General have the right to speak and take part in proceedings?",
        "ஈரவை சட்டமன்றம் (சட்டப் பேரவை மற்றும் சட்ட மேலவை) உள்ள மாநிலங்களில், எந்த அவையில் தலைமை வழக்கறிஞருக்குப் பேசவும் விவாதங்களில் பங்கேற்கவும் உரிமை உண்டு?",
        "In both Houses (Legislative Assembly and Legislative Council)", "இரு அவைகளிலும் (சட்டப் பேரவை மற்றும் சட்ட மேலவை)",
        "Only in the Legislative Assembly", "சட்டப் பேரவையில் மட்டுமே",
        "Only in the Legislative Council", "சட்ட மேலவையில் மட்டுமே",
        "Only in joint sittings of both Houses", "இரு அவைகளின் கூட்டுக் கூட்டத்தில் மட்டுமே",
        "A",
        "Article 177 explicitly confers the right to speak and participate in 'the Legislative Assembly of the State or, in the case of a State having a Legislative Council, both Houses'.",
        "உறுப்பு 177 'மாநில சட்டப் பேரவை அல்லது சட்ட மேலவை உள்ள மாநிலங்களில் இரு அவைகளிலும்' பேசவும் பங்கேற்கவும் உரிமையை வெளிப்படையாக வழங்குகிறது.",
        "Correct. Article 177 grants the right to speak and take part in both Houses of a bicameral legislature.", "சரி. உறுப்பு 177 ஈரவை சட்டமன்றத்தில் இரு அவைகளிலும் பேசவும் பங்கேற்கவும் உரிமையளிக்கிறது.",
        "Incorrect. Not restricted solely to the Assembly.", "தவறு. சட்டப் பேரவைக்கு மட்டுமே மட்டுப்படுத்தப்படவில்லை.",
        "Incorrect. Not restricted to the Council.", "தவறு. சட்ட மேலவைக்கு மட்டுமே மட்டுப்படுத்தப்படவில்லை.",
        "Incorrect. He can attend separate sittings of either House as well as joint meetings.", "தவறு. அவர் தனித்தனி அவைக் கூட்டங்களிலும் கூட்டுக் கூட்டங்களிலும் கலந்து கொள்ளலாம்.",
        "In Tamil Nadu currently, there is a unicameral legislature (Assembly only), but where bicameral exists (e.g., UP, Bihar, Maharashtra, Karnataka), AG can attend both.",
        "தமிழ்நாட்டில் தற்போது ஓரவை (சட்டப் பேரவை மட்டும்) உள்ளது; ஆனால் ஈரவை உள்ள மாநிலங்களில் (உ.பி., பீகார், மகாராஷ்டிரா, கர்நாடகா) AG இரு அவைகளிலும் பங்கேற்கலாம்.",
        "In neither House can the Advocate General vote.",
        "எந்த அவையிலும் தலைமை வழக்கறிஞரால் வாக்களிக்க முடியாது."
    )

    # Q46 (B)
    add_q(
        "ADVG_E_046", "Annual Report Rule",
        "Does the Advocate General of a State submit an annual performance or administrative report to the State Legislature or Governor?",
        "மாநில தலைமை வழக்கறிஞர் தனது வருடாந்திர செயல்பாட்டு அல்லது நிர்வாக அறிக்கையை சட்டமன்றத்திலோ அல்லது ஆளுநரிடமோ சமர்ப்பிக்கிறாரா?",
        "Yes, an annual report must be tabled in the Assembly within 30 days of the financial year", "ஆம், நிதியாண்டின் 30 நாட்களுக்குள் ஆண்டு அறிக்கை பேரவையில் சமர்ப்பிக்கப்பட வேண்டும்",
        "No, the Constitution does not mandate any annual report submission by the Advocate General", "இல்லை, தலைமை வழக்கறிஞர் ஆண்டு அறிக்கை சமர்ப்பிக்க வேண்டும் என்று அரசியலமைப்பு கட்டாயப்படுத்தவில்லை",
        "Yes, to the High Court Chief Justice annually", "ஆம், ஆண்டுதோறும் உயர் நீதிமன்ற தலைமை நீதிபதியிடம் சமர்ப்பிக்க வேண்டும்",
        "Yes, to the Union Ministry of Law", "ஆம், ஒன்றிய சட்ட அமைச்சகத்திடம் சமர்ப்பிக்க வேண்டும்",
        "B",
        "Unlike the Comptroller and Auditor General (Article 151) or State Public Service Commission (Article 323), the Advocate General is not required by the Constitution to submit any annual report.",
        "தலைமை கணக்குத் தணிக்கையாளர் (உறுப்பு 151) அல்லது மாநில அரசுப் பணியாளர் தேர்வாணையம் (உறுப்பு 323) போலன்றி, தலைமை வழக்கறிஞர் எந்தவொரு வருடாந்திர அறிக்கையையும் சமர்ப்பிக்க வேண்டும் என்று அரசியலமைப்பு கோரவில்லை.",
        "Incorrect. No constitutional annual report requirement exists for the Advocate General.", "தவறு. தலைமை வழக்கறிஞருக்கு அரசியலமைப்பு ரீதியான ஆண்டு அறிக்கை தேவை எதுவும் இல்லை.",
        "Correct. The Constitution does not require the Advocate General to submit an annual report.", "சரி. தலைமை வழக்கறிஞர் ஆண்டு அறிக்கை சமர்ப்பிக்க அரசியலமைப்பு கட்டாயப்படுத்தவில்லை.",
        "Incorrect. No reporting to High Court Chief Justice.", "தவறு. உயர் நீதிமன்ற தலைமை நீதிபதியிடம் அறிக்கை சமர்ப்பிப்பதில்லை.",
        "Incorrect. The Advocate General is a State constitutional authority, not subordinate to Union Law Ministry.", "தவறு. தலைமை வழக்கறிஞர் ஒரு மாநில அரசியலமைப்பு அதிகாரி, ஒன்றிய சட்ட அமைச்சகத்திற்கு உட்பட்டவர் அல்ல.",
        "Contrast: CAG (Art 151) and SPSC (Art 323) submit annual reports; AG and Advocate General do NOT.",
        "ஒப்பீடு: CAG (உறுப்பு 151) மற்றும் SPSC (உறுப்பு 323) ஆண்டு அறிக்கைகளை சமர்ப்பிக்கின்றன; அட்டர்னி ஜெனரலும் அட்வகேட் ஜெனரலும் சமர்ப்பிப்பதில்லை.",
        "The Advocate General's work is continuous and transactional, advising on individual cases and references as they arise.",
        "தலைமை வழக்கறிஞரின் பணி தொடர்ச்சியானது மற்றும் அவ்வப்போது எழும் தனித்தனி வழக்குகள் மற்றும் விவகாரங்களுக்கு ஆலோசனை வழங்குவதாகும்."
    )

    # Q47 (C)
    add_q(
        "ADVG_E_047", "Subordinate Law Officers",
        "Which of the following law officers is the supreme constitutional law officer of a State Government, ranking above all others?",
        "பின்வரும் சட்ட அதிகாரிகளில் மற்ற அனைவரையும் விட உயர்ந்த இடத்தில் உள்ள மாநில அரசின் உச்ச அரசியலமைப்பு சட்ட அதிகாரி யார்?",
        "Government Pleader", "அரசு வழக்கறிஞர் (Government Pleader)",
        "Public Prosecutor", "பொது வழக்குத் தொடருநர் (Public Prosecutor)",
        "Advocate General", "தலைமை வழக்கறிஞர் (Advocate General)",
        "Additional Government Pleader", "கூடுதல் அரசு வழக்கறிஞர்",
        "C",
        "The Advocate General is the sole constitutional law officer of the State under Article 165. All other state law officers (Additional Advocate General, Government Pleader, Public Prosecutor) are statutory or executive appointments subordinate to him.",
        "உறுப்பு 165-ன் கீழ் மாநிலத்தின் ஒரே அரசியலமைப்பு சட்ட அதிகாரி தலைமை வழக்கறிஞரே ஆவார். மற்ற அனைத்து மாநில சட்ட அதிகாரிகளும் (கூடுதல் AG, அரசு வழக்கறிஞர், அரசு தலைமை வழக்கறிஞர்) அவருக்குக் கீழ் பணிபுரியும் சட்டப்பூர்வ அல்லது நிர்வாக நியமனங்கள் ஆவர்.",
        "Incorrect. Government Pleaders represent the State in civil matters under the Advocate General's lead.", "தவறு. அரசு வழக்கறிஞர்கள் தலைமை வழக்கறிஞரின் வழிகாட்டுதலின் கீழ் சிவில் வழக்குகளில் அரசைப் பிரதிநிதித்துவப்படுத்துகின்றனர்.",
        "Incorrect. Public Prosecutor conducts criminal prosecutions under CrPC/BNSS.", "தவறு. அரசுத் தரப்பு வழக்கறிஞர் குற்றவியல் வழக்குகளை நடத்துகிறார்.",
        "Correct. The Advocate General is the supreme constitutional law officer of the State.", "சரி. தலைமை வழக்கறிஞரே மாநிலத்தின் உச்ச அரசியலமைப்பு சட்ட அதிகாரி ஆவார்.",
        "Incorrect. Additional Government Pleader is a subordinate law officer.", "தவறு. கூடுதல் அரசு வழக்கறிஞர் ஒரு கீழ்நிலை சட்ட அதிகாரி.",
        "Hierarchy in State: 1. Advocate General (Constitutional - Art 165), 2. Additional AG (Executive), 3. GP / PP (Statutory).",
        "மாநில படிநிலை: 1. தலைமை வழக்கறிஞர் (அரசியலமைப்பு - உறுப்பு 165), 2. கூடுதல் AG (நிர்வாகம்), 3. அரசு வழக்கறிஞர் / அரசுத் தரப்பு வழக்கறிஞர் (சட்டப்பூர்வ).",
        "The Advocate General allocates work, oversees major litigation, and settles pleadings in sensitive state matters.",
        "தலைமை வழக்கறிஞர் பணிகளைப் பகிர்ந்தளிக்கிறார், முக்கிய வழக்குகளை மேற்பார்வையிடுகிறார் மற்றும் உணர்வுப்பூர்வமான விவகாரங்களில் அரசு வாதங்களை இறுதி செய்கிறார்."
    )

    # Q48 (D)
    add_q(
        "ADVG_E_048", "Ordinance Role",
        "Does the Advocate General have the constitutional power to promulgate ordinances in a State?",
        "மாநிலத்தில் அவசரச் சட்டங்களை (Ordinances) பிறப்பிக்கும் அரசியலமைப்பு அதிகாரம் தலைமை வழக்கறிஞருக்கு உண்டா?",
        "Yes, during judicial recess", "ஆம், நீதிமன்ற விடுமுறை காலத்தில் உண்டு",
        "Yes, in consultation with the High Court", "ஆம், உயர் நீதிமன்றத்துடன் கலந்தாலோசித்து செய்யலாம்",
        "Yes, when the State Assembly is dissolved", "ஆம், மாநில சட்டப் பேரவை கலைக்கப்பட்டிருக்கும் போது உண்டு",
        "No, ordinance-making power is an executive-legislative power vested exclusively in the Governor under Article 213", "இல்லை, அவசரச் சட்டம் பிறப்பிக்கும் அதிகாரம் உறுப்பு 213-ன் கீழ் ஆளுநருக்கு மட்டுமே வழங்கப்பட்ட நிர்வாக-சட்டமன்ற அதிகாரமாகும்",
        "D",
        "Under Article 213, only the Governor has the power to promulgate ordinances when the State Legislature is not in session. The Advocate General merely provides legal advice on the constitutional validity of draft ordinances.",
        "உறுப்பு 213-ன் கீழ், மாநில சட்டமன்றம் கூடாத போது அவசரச் சட்டங்களை பிறப்பிக்கும் அதிகாரம் ஆளுநருக்கு மட்டுமே உண்டு. தலைமை வழக்கறிஞர் வரைவு அவசரச் சட்டங்களின் அரசியலமைப்பு செல்லுபடி தன்மை குறித்து சட்ட ஆலோசனை மட்டுமே வழங்குகிறார்.",
        "Incorrect. Judicial recess does not give ordinance power to the Advocate General.", "தவறு. நீதிமன்ற விடுமுறைக்காலம் அட்வகேட் ஜெனரலுக்கு அவசரச் சட்ட அதிகாரத்தை வழங்காது.",
        "Incorrect. High Court consultation does not confer legislative powers on the AG.", "தவறு. உயர் நீதிமன்ற ஆலோசனை அட்வகேட் ஜெனரலுக்கு சட்டமன்ற அதிகாரங்களை அளிக்காது.",
        "Incorrect. Dissolution of Assembly activates Governor's ordinance power, not the AG's.", "தவறு. சட்டப் பேரவை கலைக்கப்படுவது ஆளுநரின் அதிகாரத்தை செயல்படுத்துகிறது, அட்வகேட் ஜெனரலின் அதிகாரத்தை அல்ல.",
        "Correct. Ordinance-making belongs exclusively to the Governor under Article 213.", "சரி. அவசரச் சட்டம் பிறப்பிப்பது உறுப்பு 213-ன் கீழ் ஆளுநருக்கு மட்டுமே உரியது.",
        "The Advocate General is an advisor, not an ordinance-promulgating authority.",
        "தலைமை வழக்கறிஞர் ஓர் ஆலோசகரே தவிர, அவசரச் சட்டம் பிறப்பிக்கும் அதிகாரி அல்ல.",
        "Draft ordinances are vetted by the Law Department and the Advocate General before being submitted to the Governor.",
        "வரைவு அவசரச் சட்டங்கள் ஆளுநரிடம் சமர்ப்பிக்கப்படுவதற்கு முன்பு சட்டத்துறை மற்றும் தலைமை வழக்கறிஞரால் சரிபார்க்கப்படுகின்றன."
    )

    # Q49 (A)
    add_q(
        "ADVG_E_049", "Article 165 Heading",
        "What is the marginal heading (title) of Article 165 in the Constitution of India?",
        "இந்திய அரசியலமைப்பில் உறுப்பு 165-ன் தலைப்பு (Marginal Heading) என்ன?",
        "Advocate-General for the State", "மாநில தலைமை வழக்கறிஞர் (Advocate-General for the State)",
        "Law Officers of the State", "மாநில சட்ட அதிகாரிகள்",
        "Duties of the State Counsel", "மாநில வழக்கறிஞரின் கடமைகள்",
        "Chief Legal Adviser to the Governor", "ஆளுநரின் முதன்மை சட்ட ஆலோசகர்",
        "A",
        "The exact constitutional marginal heading of Article 165 is 'Advocate-General for the State'.",
        "உறுப்பு 165-ன் துல்லியமான அரசியலமைப்புத் தலைப்பு 'மாநில தலைமை வழக்கறிஞர்' (Advocate-General for the State) என்பதாகும்.",
        "Correct. 'Advocate-General for the State' is the marginal heading of Article 165.", "சரி. 'மாநில தலைமை வழக்கறிஞர்' என்பதே உறுப்பு 165-ன் தலைப்பாகும்.",
        "Incorrect. 'Law Officers of the State' is not an Article title in the Constitution.", "தவறு. 'மாநில சட்ட அதிகாரிகள்' என்பது அரசியலமைப்பு உறுப்பின் தலைப்பு அல்ல.",
        "Incorrect. Not titled 'Duties of the State Counsel'.", "தவறு. 'மாநில வழக்கறிஞரின் கடமைகள்' என்ற தலைப்பு இல்லை.",
        "Incorrect. Not titled 'Chief Legal Adviser to the Governor'.", "தவறு. 'ஆளுநரின் முதன்மை சட்ட ஆலோசகர்' என்ற தலைப்பு இல்லை.",
        "Parallel Marginal Headings: Article 76 = 'Attorney-General for India'; Article 165 = 'Advocate-General for the State'.",
        "இணையான தலைப்புகள்: உறுப்பு 76 = 'இந்திய தலைமை வழக்கறிஞர்'; உறுப்பு 165 = 'மாநில தலைமை வழக்கறிஞர்'.",
        "The Constitution uses the hyphenated form 'Advocate-General' in the official text.",
        "அரசியலமைப்பு அதன் அதிகாரப்பூர்வ உரையில் 'அட்வகேட்-ஜெனரல்' என்றே பயன்படுத்துகிறது."
    )

    # Q50 (B)
    add_q(
        "ADVG_E_050", "Core Function Summary",
        "In summary, what is the primary constitutional function of the Advocate General under Article 165(2)?",
        "சுருக்கமாக, உறுப்பு 165(2)-ன் கீழ் மாநில தலைமை வழக்கறிஞரின் முதன்மையான அரசியலமைப்பு செயல்பாடு என்ன?",
        "To preside over criminal trials in the High Court", "உயர் நீதிமன்றத்தில் குற்றவியல் வழக்குகளுக்கு தலைமை தாங்குவது",
        "To advise the State Government on legal matters and perform other legal duties referred by the Governor", "சட்ட விவகாரங்களில் மாநில அரசுக்கு ஆலோசனை வழங்குவது மற்றும் ஆளுநரால் ஒப்படைக்கப்படும் பிற சட்டப் பணிகளை ஆற்றுவது",
        "To draft and enact legislation on behalf of the Governor", "ஆளுநரின் சார்பில் சட்டங்களை வரைவு செய்து நிறைவேற்றுவது",
        "To manage the administrative affairs of all district courts", "அனைத்து மாவட்ட நீதிமன்றங்களின் நிர்வாக விவகாரங்களை நிர்வகிப்பது",
        "B",
        "Under Article 165(2), the primary constitutional duty of the Advocate General is to give advice to the Government of the State upon legal matters and perform other duties of a legal character assigned by the Governor.",
        "உறுப்பு 165(2)-ன் கீழ் தலைமை வழக்கறிஞரின் முதன்மை அரசியலமைப்பு கடமை, சட்ட விவகாரங்களில் மாநில அரசுக்கு ஆலோசனை வழங்குவதும், ஆளுநரால் ஒப்படைக்கப்படும் சட்டப் பணிகளை ஆற்றுவதும் ஆகும்.",
        "Incorrect. AG does not preside over trials; judges preside.", "தவறு. AG வழக்குகளுக்கு தலைமை தாங்குவதில்லை; நீதிபதிகளே தலைமை தாங்குகின்றனர்.",
        "Correct. Advising the State Government on legal matters and performing duties referred by the Governor is his core function.", "சரி. சட்ட விவகாரங்களில் அரசுக்கு ஆலோசனை வழங்குவதும் ஆளுநரால் ஒப்படைக்கப்படும் பணிகளைச் செய்வதும் அவரது முதன்மைப் பணியாகும்.",
        "Incorrect. Drafting and enacting legislation is done by the Law Department and State Legislature.", "தவறு. சட்டங்களை வரைவு செய்வதும் நிறைவேற்றுவதும் சட்டத்துறை மற்றும் சட்டமன்றத்தால் செய்யப்படுகிறது.",
        "Incorrect. Managing district courts is the administrative function of the High Court under Article 235.", "தவறு. மாவட்ட நீதிமன்றங்களை நிர்வகிப்பது உறுப்பு 235-ன் கீழ் உயர் நீதிமன்றத்தின் நிர்வாகப் பணியாகும்.",
        "Article 165(2) defines the functional mandate of the Advocate General.",
        "உறுப்பு 165(2) தலைமை வழக்கறிஞரின் செயல்பாட்டு அதிகார வரம்பை வரையறுக்கிறது.",
        "His role combines advisory counsel, court representation, and upholding constitutional legality in governance.",
        "அவரது பங்கு சட்ட ஆலோசனை, நீதிமன்ற பிரதிநிதித்துவம் மற்றும் ஆளுகையில் அரசியலமைப்பு சட்டபூர்வ தன்மையை நிலைநிறுத்துதல் ஆகியவற்றை ஒருங்கிணைக்கிறது."
    )

    return qs

def main():
    questions = get_easy_questions()
    print(f"Total Easy questions generated: {len(questions)}")
    
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "advocate_general_easy.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")
    
    # Validate file
    validator = ContentValidator()
    report = validator.validate_file(out_file, expected_count=50, expected_prefix="ADVG_E_")
    print(f"Validation Result: {'PASS' if report.is_valid else 'FAIL'} | Audited: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
    if not report.is_valid:
        for iss in report.issues:
            print("Issue:", iss.severity, iss.field, iss.message)

if __name__ == "__main__":
    main()
