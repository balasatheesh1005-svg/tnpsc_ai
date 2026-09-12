# -*- coding: utf-8 -*-
"""
Builder for 25 Assertion & Reasoning MCQs on Union & Its Territory (polity_union_territory).
IDs: UT_R_001 to UT_R_025.
Strictly conforms to TNPSC 24-field schema, bilingual parity, audit rules.
"""
import json
import os
import sys
from ut_mcq_helper import make_ut_q, balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

def get_reasoning_questions():
    questions = []

    # Standard options format
    # A: Both (A) and (R) are true and (R) is the correct explanation of (A)
    # B: Both (A) and (R) are true but (R) is NOT the correct explanation of (A)
    # C: (A) is true but (R) is false
    # D: (A) is false but (R) is true

    # R01: Article 1 Union of States
    questions.append(make_ut_q(
        qid="UT_R_001", diff="Medium", qtype="Reasoning",
        subtopic="Article 1: Name and Territory of the Union",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Indian Constitution describes India as a 'Union of States' rather than a 'Federation of States'.\nReason (R): The Indian federation is not the result of an agreement among the constituent states, and no state has the right to secede from the Union.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): இந்திய அரசியலமைப்பு இந்தியாவை 'மாநிலங்களின் கூட்டமைப்பு' என்பதற்குப் பதிலாக 'மாநிலங்களின் ஒன்றியம்' என விவரிக்கிறது.\nகாரணம் (R): இந்தியக் கூட்டமைப்பு உறுப்பு மாநிலங்களுக்கிடையேயான ஓர் ஒப்பந்தத்தின் விளைவு அல்ல, மேலும் எந்தவொரு மாநிலத்திற்கும் ஒன்றியத்திலிருந்து பிரிந்து செல்லும் உரிமை இல்லை.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains why Dr. Ambedkar and the Drafting Committee preferred 'Union of States' over 'Federation of States'.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். வரைவுக்குழு 'ஒன்றியம்' என்ற சொல்லைப் பயன்படுத்தியதற்கான தெளிவான காரணம் இதுவே.",
        why_a_en="Both statements are true and (R) provides the constitutional justification for (A).",
        why_a_ta="இரு கூற்றுகளும் உண்மையானவை மற்றும் (R) கூற்று (A)-விற்கான சரியான விளக்கத்தை அளிக்கிறது.",
        why_b_en="(R) is indeed the direct explanation given by Dr. B.R. Ambedkar in the Constituent Assembly.",
        why_b_ta="(R) என்பது அரசியலமைப்பு நிர்ணய சபையில் டாக்டர் அம்பேத்கர் அளித்த நேரடி விளக்கமாகும்.",
        why_c_en="Reason (R) is completely true, not false.",
        why_c_ta="காரணம் (R) முற்றிலும் உண்மையானது, தவறானது அல்ல.",
        why_d_en="Assertion (A) is completely true as per Article 1(1).",
        why_d_ta="கூற்று (A) உறுப்பு 1(1)-ன் படி முற்றிலும் சரியானது.",
        tip_en="Ambedkar's speech: Indian federation is a Union because it is indestructible; states have no right to secede.",
        tip_ta="அம்பேத்கரின் உரை: இந்தியக் கூட்டமைப்பு அழியாதது என்பதால் அது ஓர் ஒன்றியம்; மாநிலங்களுக்குப் பிரியும் உரிமை இல்லை.",
        fact_en="The US Constitution provides no right to secession, affirmed by Texas v. White (1869).",
        fact_ta="அமெரிக்க அரசியலமைப்பிலும் மாநிலங்களுக்கு பிரியும் உரிமை இல்லை (டெக்சாஸ் எதிர் ஒயிட் 1869).",
        tags=["polity", "union_territory", "article_1", "reasoning"]
    ))

    # R02: Indestructible Union of Destructible States
    questions.append(make_ut_q(
        qid="UT_R_002", diff="Medium", qtype="Reasoning",
        subtopic="Article 3: Formation of New States and Alteration of Areas",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): India is characterized as an 'indestructible Union of destructible states'.\nReason (R): Parliament has the power under Article 3 to alter boundaries, diminish area, or abolish existing states without their consent, but states cannot break away from the Union.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): இந்தியா 'அழியக்கூடிய மாநிலங்களைக் கொண்ட ஓர் அழியாத ஒன்றியம்' என விவரிக்கப்படுகிறது.\nகாரணம் (R): மாநிலங்களின் ஒப்புதல் இன்றியே அவற்றின் எல்லைகளை மாற்றவோ, பரப்பளவைக் குறைக்கவோ அல்லது அவற்றை அழிக்கவோ உறுப்பு 3-ன் கீழ் நாடாளுமன்றத்திற்கு அதிகாரம் உண்டு, ஆனால் மாநிலங்கள் ஒன்றியத்தை விட்டுப் பிரிய முடியாது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the direct explanation of (A). The territorial integrity of any state is not guaranteed by the Indian Constitution, making states destructible, while the Union is indestructible.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். இந்திய அரசியலமைப்பு மாநிலங்களின் எல்லை ஒருமைப்பாட்டிற்கு உத்தரவாதம் அளிக்காததால் மாநிலங்கள் அழியக்கூடியவை; ஆனால் ஒன்றியம் நிரந்தரமானது.",
        why_a_en="States can be reorganised by Parliament unilaterally (destructible), but cannot secede (indestructible Union).",
        why_a_ta="நாடாளுமன்றம் மாநிலங்களை ஒருதலைப்பட்சமாக மாற்றியமைக்கலாம், ஆனால் மாநிலங்கள் பிரிய முடியாது.",
        why_b_en="(R) directly explains the phrase in (A).",
        why_b_ta="(R) கூற்று (A)-வில் உள்ள சொற்றொடரை நேரடியாக விளக்குகிறது.",
        why_c_en="Reason (R) is fully accurate under Article 3.",
        why_c_ta="காரணம் (R) உறுப்பு 3-ன் கீழ் முற்றிலும் சரியானது.",
        why_d_en="Assertion (A) is a well-established constitutional doctrine in Indian polity.",
        why_d_ta="கூற்று (A) இந்திய அரசியலமைப்பின் நன்கு நிறுவப்பட்ட கோட்பாடாகும்.",
        tip_en="Compare: USA is an 'indestructible Union of indestructible states'.",
        tip_ta="ஒப்பீடு: அமெரிக்கா 'அழியாத மாநிலங்களைக் கொண்ட ஓர் அழியாத ஒன்றியம்'.",
        fact_en="Article IV, Section 3 of the US Constitution prohibits forming a new state from existing states without their consent.",
        fact_ta="அமெரிக்க அரசியலமைப்பின் உறுப்பு IV பிரிவு 3 மாநிலங்களின் அனுமதியின்றி புதிய மாநிலங்களை உருவாக்குவதைத் தடை செய்கிறது.",
        tags=["polity", "union_territory", "article_3", "reasoning"]
    ))

    # R03: Article 2 vs Article 3
    questions.append(make_ut_q(
        qid="UT_R_003", diff="Hard", qtype="Reasoning",
        subtopic="Article 2: Admission or Establishment of New States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The admission of Sikkim into the Indian Union was carried out under Article 2 and not under Article 3 of the Constitution.\nReason (R): Article 2 deals with the admission or establishment of new states that were not part of the territory of India, whereas Article 3 deals with the reorganisation of existing states within the territory of India.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): சிக்கிம் இந்திய ஒன்றியத்தில் இணைக்கப்பட்டது அரசியலமைப்பின் உறுப்பு 2-ன் கீழ் மேற்கொள்ளப்பட்டதே தவிர உறுப்பு 3-ன் கீழ் அல்ல.\nகாரணம் (R): உறுப்பு 2 என்பது இந்தியாவின் நிலப்பரப்பில் முன்னதாக இல்லாத புதிய பகுதிகளை மாநிலங்களாக ஏற்பது தொடர்பானது; ஆனால் உறுப்பு 3 என்பது இந்திய நிலப்பரப்பிற்குள் ஏற்கனவே உள்ள மாநிலங்களை மறுசீரமைப்பது தொடர்பானது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains why Sikkim was admitted under Article 2. Sikkim was an independent protectorate and not an existing state of India, so Article 2 applied.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். சிக்கிம் ஒரு சுதந்திரமான பாதுகாக்கப்பட்ட பகுதியாக இருந்ததே தவிர இந்தியாவின் முந்தைய மாநிலம் அல்ல; எனவே உறுப்பு 2 பொருந்தியது.",
        why_a_en="Sikkim was external territory admitted under Article 2 power, precisely as defined in (R).",
        why_a_ta="சிக்கிம் வெளிப்புற நிலப்பரப்பாக இருந்து உறுப்பு 2-ன் கீழ் இணைக்கப்பட்டது, இது (R)-ல் துல்லியமாக விளக்கப்பட்டுள்ளது.",
        why_b_en="(R) is the exact constitutional rationale for (A).",
        why_b_ta="(R) என்பது (A)-விற்கான துல்லியமான அரசியலமைப்பு நியாயமாகும்.",
        why_c_en="(R) correctly distinguishes Article 2 from Article 3.",
        why_c_ta="(R) உறுப்பு 2 மற்றும் 3-ன் வேறுபாட்டைச் சரியாக விளக்குகிறது.",
        why_d_en="(A) is true; Sikkim was admitted under Article 2.",
        why_d_ta="(A) சரியானது; சிக்கிம் உறுப்பு 2-ன் கீழ் இணைக்கப்பட்டது.",
        tip_en="Article 2 = External territories admitted. Article 3 = Internal states reorganised.",
        tip_ta="உறுப்பு 2 = வெளிப்புற பகுதிகள் சேர்க்கை. உறுப்பு 3 = உள்நாட்டு மாநிலங்கள் மறுசீரமைப்பு.",
        fact_en="36th Constitutional Amendment Act 1975 made Sikkim the 22nd state of India.",
        fact_ta="36-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1975 சிக்கிமை இந்தியாவின் 22-வது மாநிலமாக்கியது.",
        tags=["polity", "union_territory", "sikkim", "article_2", "reasoning"]
    ))

    # R04: Article 3 - State Legislature Consultation
    questions.append(make_ut_q(
        qid="UT_R_004", diff="Medium", qtype="Reasoning",
        subtopic="Article 3: Formation of New States and Alteration of Areas",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The President of India must refer a state reorganisation Bill to the concerned State Legislature before it is introduced in Parliament.\nReason (R): The Parliament is constitutionally bound to accept and implement the views expressed by the State Legislature on the Bill.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): மாநில மறுசீரமைப்பு மசோதாவை நாடாளுமன்றத்தில் அறிமுகப்படுத்துவதற்கு முன்பு இந்தியக் குடியரசுத் தலைவர் அதனை சம்பந்தப்பட்ட மாநில சட்டமன்றத்தின் கருத்துக்காக அனுப்ப வேண்டும்.\nகாரணம் (R): அம்மசோதா மீது மாநில சட்டமன்றம் தெரிவிக்கும் கருத்துக்களை ஏற்றுச் செயல்படுத்துவதற்கு நாடாளுமன்றம் அரசியலமைப்பு ரீதியாகக் கட்டுப்பட்டுள்ளது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="C",
        exp_en="(A) is true under the proviso to Article 3, but (R) is false because the views of the state legislature are purely advisory and NOT binding on the President or Parliament.",
        exp_ta="(A) சரி, உறுப்பு 3-ன் நிபந்தனையின்படி மசோதா மாநில சட்டமன்றத்திற்கு அனுப்பப்பட வேண்டும். ஆனால் (R) தவறு, ஏனெனில் சட்டமன்றத்தின் கருத்து ஆலோசனையே அன்றி குடியரசுத் தலைவரையோ நாடாளுமன்றத்தையோ கட்டுப்படுத்தாது.",
        why_a_en="Reason (R) is false; Parliament is NOT bound by the state's views.",
        why_a_ta="காரணம் (R) தவறு; நாடாளுமன்றம் மாநிலத்தின் கருத்தை ஏற்கக் கட்டுப்பட்டதல்ல.",
        why_b_en="(R) is a false statement.",
        why_b_ta="(R) தவறான கூற்றாகும்.",
        why_c_en="(A) is true (reference is mandatory) and (R) is false (views are not binding).",
        why_c_ta="(A) சரி (கருத்து கேட்பது கட்டாயம்) மற்றும் (R) தவறு (கருத்து கட்டுப்படுத்தாது).",
        why_d_en="(A) is true, not false.",
        why_d_ta="(A) சரியானது, தவறல்ல.",
        tip_en="Reference to state is mandatory; accepting state's view is optional.",
        tip_ta="மாநிலத்திற்கு அனுப்புவது கட்டாயம்; அதன் கருத்தை ஏற்பது விருப்பத்திற்குட்பட்டது.",
        fact_en="If the state fails to express its views within the prescribed time, the bill can still be introduced.",
        fact_ta="குறிப்பிட்ட காலத்திற்குள் மாநிலம் கருத்தைத் தெரிவிக்கத் தவறினாலும் மசோதாவை அறிமுகப்படுத்தலாம்.",
        tags=["polity", "union_territory", "article_3", "state_legislature", "reasoning"]
    ))

    # R05: Article 4 and Article 368
    questions.append(make_ut_q(
        qid="UT_R_005", diff="Hard", qtype="Reasoning",
        subtopic="Article 4: Laws under Articles 2 and 3",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): A law creating a new State or altering the boundaries of an existing State can be passed by a simple majority in Parliament.\nReason (R): Article 4(2) of the Constitution expressly declares that laws made under Article 2 or Article 3 shall not be deemed to be an amendment of the Constitution for the purposes of Article 368.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): ஒரு புதிய மாநிலத்தை உருவாக்கும் அல்லது தற்போதைய மாநிலத்தின் எல்லைகளை மாற்றும் ஒரு சட்டத்தை நாடாளுமன்றத்தில் சாதாரண பெரும்பான்மை மூலம் நிறைவேற்ற முடியும்.\nகாரணம் (R): உறுப்பு 2 அல்லது உறுப்பு 3-ன் கீழ் இயற்றப்படும் சட்டங்கள் உறுப்பு 368-ன் நோக்கங்களுக்காக அரசியலமைப்பு திருத்தமாகக் கருதப்பட மாட்டாது என அரசியலமைப்பின் 4(2) பிரிவு வெளிப்படையாக அறிவிக்கிறது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the direct constitutional explanation of (A). Because Article 4(2) excludes Article 2 and 3 laws from Article 368, ordinary legislative procedure and simple majority apply.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு நேரடி அரசியலமைப்பு விளக்கமாகும். உறுப்பு 4(2) இச்சட்டங்களை உறுப்பு 368-லிருந்து விலக்குவதால் சாதாரண சட்டமன்ற நடைமுறையும் எளிய பெரும்பான்மையும் போதுமானது.",
        why_a_en="Article 4(2) is the exact constitutional provision that allows state reorganisation by simple majority.",
        why_a_ta="உறுப்பு 4(2) என்பது சாதாரண பெரும்பான்மை மூலம் மாநில மறுசீரமைப்பை அனுமதிக்கும் துல்லியமான அரசியலமைப்பு விதியாகும்.",
        why_b_en="(R) directly explains why only a simple majority is needed in (A).",
        why_b_ta="(R) கூற்று (A)-ல் சாதாரண பெரும்பான்மை ஏன் போதுமானது என்பதை நேரடியாக விளக்குகிறது.",
        why_c_en="(R) is true, not false.",
        why_c_ta="(R) சரியானது, தவறல்ல.",
        why_d_en="(A) is true as per established constitutional law.",
        why_d_ta="(A) அரசியலமைப்பு விதிகளின்படி சரியானது.",
        tip_en="State reorganisation laws need ONLY simple majority, not special majority under Article 368.",
        tip_ta="மாநில மறுசீரமைப்புச் சட்டங்களுக்கு சாதாரண பெரும்பான்மை மட்டுமே தேவை, உறுப்பு 368-ன் கீழ் சிறப்பு பெரும்பான்மை தேவையில்லை.",
        fact_en="Such laws also make necessary amendments to the First and Fourth Schedules automatically.",
        fact_ta="இத்தகைய சட்டங்கள் முதல் மற்றும் நான்காவது அட்டவணைகளில் தேவையான திருத்தங்களைத் தானாகவே செய்கின்றன.",
        tags=["polity", "union_territory", "article_4", "article_368", "reasoning"]
    ))

    # R06: Berubari Union Case
    questions.append(make_ut_q(
        qid="UT_R_006", diff="Hard", qtype="Reasoning",
        subtopic="Article 3: Formation of New States and Alteration of Areas",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): Cession of Indian territory to a foreign country cannot be carried out through an ordinary law enacted under Article 3 of the Constitution.\nReason (R): The Supreme Court in the Berubari Union Case (1960) ruled that Parliament's power under Article 3 to diminish state territory does not include the power to cede Indian territory to a foreign state.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): இந்திய நிலப்பகுதியை ஓர் அயல்நாட்டுக்கு விட்டுக் கொடுப்பதை அரசியலமைப்பின் உறுப்பு 3-ன் கீழ் இயற்றப்படும் சாதாரண சட்டம் மூலம் செயல்படுத்த முடியாது.\nகாரணம் (R): மாநில நிலப்பரப்பைக் குறைக்கும் நாடாளுமன்றத்தின் அதிகாரமானது இந்தியப் பகுதியை வெளிநாட்டுக்கு விட்டுக் கொடுக்கும் அதிகாரத்தை உள்ளடக்காது என்று பெருபாரி யூனியன் வழக்கில் (1960) உச்சநீதிமன்றம் தீர்ப்பளித்தது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). The Supreme Court held that cession of Indian territory can only be done by amending the Constitution under Article 368, which led to the 9th Constitutional Amendment Act, 1960.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். இந்திய நிலப்பரப்பை அயல்நாட்டுக்கு விட்டுக் கொடுக்க உறுப்பு 368-ன் கீழ் அரசியலமைப்பு திருத்தம் அவசியம் என உச்சநீதிமன்றம் கூறியதால் 9-வது திருத்தச் சட்டம் 1960 இயற்றப்பட்டது.",
        why_a_en="The Berubari ruling is the exact legal authority establishing that cession requires an Article 368 amendment.",
        why_a_ta="பெருபாரி தீர்ப்பே நிலப்பரப்பை விட்டுக்கொடுக்க உறுப்பு 368 திருத்தம் அவசியம் என்பதை நிலைநிறுத்திய சட்டப்பூர்வ அதிகாரமாகும்.",
        why_b_en="(R) is the exact explanation for the proposition in (A).",
        why_b_ta="(R) என்பது (A)-விற்கான நேரடி விளக்கமாகும்.",
        why_c_en="(R) is completely true.",
        why_c_ta="(R) முற்றிலும் சரியானது.",
        why_d_en="(A) is true as affirmed by constitutional jurisprudence.",
        why_d_ta="(A) அரசியலமைப்புச் சட்டத்தின்படி சரியானது.",
        tip_en="Diminishing state area within India = Article 3 (Simple majority). Ceding territory to foreign state = Article 368 amendment.",
        tip_ta="உள்நாட்டில் மாநில பரப்பைக் குறைத்தல் = உறுப்பு 3 (சாதாரண பெரும்பான்மை). வெளிநாட்டுக்கு நிலத்தை விடுதல் = உறுப்பு 368 திருத்தம்.",
        fact_en="The 100th Constitutional Amendment Act, 2015 was passed on this very principle to transfer enclaves to Bangladesh.",
        fact_ta="இக்கோட்பாட்டின் அடிப்படையிலேயே வங்கதேசத்திற்கு நிலப்பகுதிகளை மாற்ற 100-வது திருத்தச் சட்டம் 2015 இயற்றப்பட்டது.",
        tags=["polity", "union_territory", "berubari", "article_3", "reasoning"]
    ))

    # R07: Boundary Dispute Settlement 1969
    questions.append(make_ut_q(
        qid="UT_R_007", diff="Hard", qtype="Reasoning",
        subtopic="Article 3: Formation of New States and Alteration of Areas",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): Settlement of an international boundary dispute between India and another country does not require a Constitutional Amendment Act.\nReason (R): Demarcation of an existing boundary dispute does not involve cession of Indian territory and can therefore be effected by executive action alone.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): இந்தியாவுக்கும் மற்றொரு நாட்டுக்கும் இடையிலான சர்வதேச எல்லைத் தகராறைத் தீர்ப்பதற்கு அரசியலமைப்புத் திருத்தச் சட்டம் தேவையில்லை.\nகாரணம் (R): ஏற்கனவே உள்ள எல்லைத் தகராறை வரையறுப்பது என்பது இந்திய நிலப்பரப்பை விட்டுக் கொடுப்பதாகாது, எனவே அதனை நிர்வாக நடவடிக்கை மூலமே செயல்படுத்த முடியும்.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the correct explanation of (A). In 1969, the Supreme Court ruled that settlement of a boundary dispute does not amount to cession of territory; it merely identifies existing boundaries, hence executive action is sufficient.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். 1969-ல் உச்சநீதிமன்றம் எல்லைத் தகராறைத் தீர்ப்பது நிலத்தை விட்டுக் கொடுப்பதாகாது, அது எல்லையை அடையாளம் காண்பதே என்பதால் வெறும் நிர்வாக நடவடிக்கையே போதுமானது எனத் தீர்ப்பளித்தது.",
        why_a_en="The 1969 SC ruling directly supports both (A) and (R), with (R) explaining why no amendment is needed.",
        why_a_ta="1969 உச்சநீதிமன்றத் தீர்ப்பு (A) மற்றும் (R) இரண்டையும் ஆதரிக்கிறது, மேலும் (R) திருத்தம் தேவையில்லாத காரணத்தை விளக்குகிறது.",
        why_b_en="(R) is the exact ground articulated by the Supreme Court.",
        why_b_ta="(R) என்பது உச்சநீதிமன்றம் கூறிய துல்லியமான காரணமாகும்.",
        why_c_en="(R) is legally valid and true.",
        why_c_ta="(R) சட்டப்பூர்வமாக சரியானது.",
        why_d_en="(A) is true as per established law.",
        why_d_ta="(A) சரியானது.",
        tip_en="Cession of territory = Article 368 needed. Demarcation of boundary = Executive action suffices.",
        tip_ta="நிலத்தை விட்டுக் கொடுத்தல் = உறுப்பு 368 தேவை. எல்லை நிர்ணயம் = நிர்வாக நடவடிக்கை போதும்.",
        fact_en="This ruling arose during the implementation of the Kutch dispute tribunal award with Pakistan in 1969.",
        fact_ta="1969-ல் பாகிஸ்தானுடனான கட்ச் எல்லைத் தகராறு தீர்ப்பாய முடிவை செயல்படுத்தும்போது இத்தீர்ப்பு வழங்கப்பட்டது.",
        tags=["polity", "union_territory", "boundary_dispute", "supreme_court", "reasoning"]
    ))

    # R08: Dhar Commission Recommendation
    questions.append(make_ut_q(
        qid="UT_R_008", diff="Medium", qtype="Reasoning",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Linguistic Provinces Commission headed by Justice S.K. Dhar rejected the reorganisation of states on linguistic basis in 1948.\nReason (R): The Commission felt that linguistic reorganisation would threaten national unity and recommended reorganisation purely on the basis of administrative convenience.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): நீதிபதி எஸ்.கே. தார் தலைமையிலான மொழிவாரி மாகாணங்கள் ஆணையம் 1948-ல் மொழி அடிப்படையில் மாநிலங்களை மறுசீரமைப்பதை நிராகரித்தது.\nகாரணம் (R): மொழிவாரி மறுசீரமைப்பு தேசிய ஒற்றுமைக்கு அச்சுறுத்தலாக அமையும் என்று கருதிய ஆணையம், நிர்வாக வசதியின் அடிப்படையில் மட்டுமே மாநிலங்களை மறுசீரமைக்கப் பரிந்துரைத்தது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). The Dhar Commission (December 1948) strongly opposed linguistic provinces, arguing that national consolidation and administrative efficiency should take precedence.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். தார் ஆணையம் (டிசம்பர் 1948) மொழிவாரி மாகாணங்களை கடுமையாக எதிர்த்தது; தேசிய ஒருங்கிணைப்பும் நிர்வாக செயல்திறனுமே முதன்மையானதாக இருக்க வேண்டும் என வாதிட்டது.",
        why_a_en="Both statements accurately represent the historical findings and rationale of the Dhar Commission.",
        why_a_ta="இரு கூற்றுகளும் தார் ஆணையத்தின் வரலாற்று முடிவுகளையும் காரணங்களையும் துல்லியமாக பிரதிபலிக்கின்றன.",
        why_b_en="(R) directly explains the reason why the commission rejected linguistic division.",
        why_b_ta="(R) ஆணையம் ஏன் மொழிவாரி பிரிவினையை நிராகரித்தது என்பதை நேரடியாக விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Dhar Commission: Administrative convenience YES, Linguistic basis NO.",
        tip_ta="தார் ஆணையம்: நிர்வாக வசதி ஆம், மொழி அடிப்படை இல்லை.",
        fact_en="The intense resentment sparked by Dhar Commission report forced Congress to set up the JVP Committee in Dec 1948.",
        fact_ta="தார் ஆணைய அறிக்கையால் ஏற்பட்ட கடும் கொந்தளிப்பே டிசம்பர் 1948-ல் ஜே.வி.பி குழு அமையக் காரணமானது.",
        tags=["polity", "union_territory", "dhar_commission", "reasoning"]
    ))

    # R09: JVP Committee
    questions.append(make_ut_q(
        qid="UT_R_009", diff="Medium", qtype="Reasoning",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The JVP Committee (1948-49) formally rejected language as the basis for the reorganisation of states.\nReason (R): The committee believed that in the immediate post-partition period, the top priority of India must be security, unity, and economic prosperity rather than linguistic divisions.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): ஜே.வி.பி குழு (1948-49) மொழி அடிப்படையில் மாநிலங்களை மறுசீரமைப்பதை முறைப்படி நிராகரித்தது.\nகாரணம் (R): நாடு பிரிக்கப்பட்ட உடனடி சூழ்நிலையில், இந்தியாவின் முதன்மை நோக்கம் பாதுகாப்பு, ஒற்றுமை மற்றும் பொருளாதார முன்னேற்றமாக மட்டுமே இருக்க வேண்டும் என்றும் மொழிவாரி பிரிவினையாக இருக்கக்கூடாது என்றும் இக்குழு கருதியது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). The JVP report (April 1949) stated that the primary consideration should be security, unity, and economic development of India, hence postponing linguistic reorganisation.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். ஜே.வி.பி அறிக்கை (ஏப்ரல் 1949) இந்தியாவின் முதன்மையான நோக்கம் பாதுகாப்பு, ஒருமைப்பாடு மற்றும் பொருளாதார வளர்ச்சியே எனக் கூறி மொழிவாரி மாநிலங்களை ஒத்திவைத்தது.",
        why_a_en="Both statements are factually accurate and (R) provides the exact historical reasoning of the JVP report.",
        why_a_ta="இரு கூற்றுகளும் உண்மையே மற்றும் (R) ஜே.வி.பி அறிக்கையின் துல்லியமான வரலாற்று காரணத்தை விளக்குகிறது.",
        why_b_en="(R) directly explains (A).",
        why_b_ta="(R) நேரடியாக (A)-வை விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="JVP members: Jawaharlal Nehru, Vallabhbhai Patel, Pattabhi Sitaramayya.",
        tip_ta="JVP உறுப்பினர்கள்: ஜவஹர்லால் நேரு, வல்லபாய் படேல், பட்டாபி சீதாராமையா.",
        fact_en="Despite JVP's rejection, the death of Potti Sriramulu in 1952 forced the government to create Andhra State.",
        fact_ta="JVP நிராகரித்த போதிலும், 1952-ல் பொட்டி ஸ்ரீராமுலுவின் மறைவு ஆந்திர மாநிலத்தை உருவாக்க அரசை நிர்பந்தித்தது.",
        tags=["polity", "union_territory", "jvp_committee", "reasoning"]
    ))

    # R10: Fazl Ali Commission Theory of One Language One State
    questions.append(make_ut_q(
        qid="UT_R_010", diff="Hard", qtype="Reasoning",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The States Reorganisation Commission (Fazl Ali Commission) rejected the theory of 'one language, one state'.\nReason (R): The Commission held that the unity and security of India must remain the primary consideration in any redrawing of the country's political boundaries.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): மாநில மறுசீரமைப்பு ஆணையம் (பசல் அலி ஆணையம்) 'ஒரு மொழிக்கு ஒரு மாநிலம்' என்ற கோட்பாட்டை நிராகரித்தது.\nகாரணம் (R): நாட்டின் அரசியல் எல்லைகளை மாற்றி அமைக்கும் எந்தவொரு நடவடிக்கையிலும் இந்தியாவின் ஒற்றுமையும் பாதுகாப்பும் முதன்மையான காரணியாக இருக்க வேண்டும் என்று ஆணையம் கருதியது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains (A). While the Fazl Ali Commission accepted language as a major criterion, it explicitly rejected 'one language, one state' because national unity and security were deemed paramount.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். பசல் அலி ஆணையம் மொழியை ஒரு முக்கிய காரணியாக ஏற்றுக் கொண்ட போதிலும், 'ஒரு மொழிக்கு ஒரு மாநிலம்' என்ற விதியை நிராகரித்தது; நாட்டின் ஒற்றுமையே முதன்மையானது என்று கூறியது.",
        why_a_en="The commission identified preservation of unity and security as the first of four major factors.",
        why_a_ta="நாட்டின் ஒற்றுமை மற்றும் பாதுகாப்பை பாதுகாப்பதே நான்கு முக்கிய காரணிகளில் முதன்மையானது என ஆணையம் குறிப்பிட்டது.",
        why_b_en="(R) directly explains the rejection of the rigid 'one language, one state' theory.",
        why_b_ta="(R) 'ஒரு மொழி ஒரு மாநிலம்' கோட்பாட்டை நிராகரித்ததற்கான காரணத்தை நேரடியாக விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Fazl Ali Commission: Accepted language as a basis, but REJECTED 'one language, one state'.",
        tip_ta="பசல் அலி ஆணையம்: மொழியை அடிப்படையாக ஏற்றது, ஆனால் 'ஒரு மொழிக்கு ஒரு மாநிலம்' என்பதை நிராகரித்தது.",
        fact_en="The 4 factors identified: Unity & security, Linguistic & cultural homogeneity, Financial/economic viability, Welfare of people.",
        fact_ta="ஆணையம் கூறிய 4 காரணிகள்: ஒற்றுமை & பாதுகாப்பு, மொழி & கலாச்சார ஒற்றுமை, நிதி & பொருளாதார நிலைத்தன்மை, மக்கள் நலம்.",
        tags=["polity", "union_territory", "fazl_ali", "reasoning"]
    ))

    # R11: 7th Amendment 1956
    questions.append(make_ut_q(
        qid="UT_R_011", diff="Medium", qtype="Reasoning",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The 7th Constitutional Amendment Act, 1956 abolished the distinction between Part A and Part B states and completely replaced Part C states.\nReason (R): The States Reorganisation Commission found the four-fold classification of states to be complex, discriminatory, and administratively inefficient.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): 7-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1956, பகுதி A மற்றும் பகுதி B மாநிலங்களுக்கு இடையிலான வேறுபாட்டை நீக்கியதுடன் பகுதி C மாநிலங்களை முற்றிலும் மாற்றியமைத்தது.\nகாரணம் (R): மாநிலங்களின் நான்கு அடுக்கு வகைப்பாடு சிக்கலானது, பாகுபாடானது மற்றும் நிர்வாக ரீதியாகத் திறமையற்றது என மாநில மறுசீரமைப்பு ஆணையம் கண்டறிந்தது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains (A). The Fazl Ali Commission recommended repealing the Part A, B, C, D classification, leading to the 7th Amendment 1956 which created 14 States and 6 Union Territories.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். பசல் அலி ஆணையம் பகுதி A, B, C, D வகைப்பாட்டை ரத்து செய்யப் பரிந்துரைத்ததால் 7-வது திருத்தம் கொண்டுவரப்பட்டு 14 மாநிலங்கள் மற்றும் 6 UTகள் உருவாக்கப்பட்டன.",
        why_a_en="The 7th CAA implemented the SRC recommendation to abolish the four-fold classification.",
        why_a_ta="7-வது திருத்தம் நான்கு அடுக்கு வகைப்பாட்டை நீக்க வேண்டும் என்ற SRC-யின் பரிந்துரையை செயல்படுத்தியது.",
        why_b_en="(R) explains why the classification was abolished in (A).",
        why_b_ta="(R) இந்த வகைப்பாடு ஏன் நீக்கப்பட்டது என்பதை விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="7th CAA 1956 repealed Part VII of Constitution (Part B states).",
        tip_ta="7-வது திருத்தம் 1956 பகுதி VII-ஐ (பகுதி B மாநிலங்கள்) அரசியலமைப்பிலிருந்து நீக்கியது.",
        fact_en="Rajpramukhs of Part B states were also abolished by the 7th Amendment.",
        fact_ta="பகுதி B மாநிலங்களின் 'ராஜ் பிரமுகர்' பதவியும் 7-வது திருத்தத்தால் ஒழிக்கப்பட்டது.",
        tags=["polity", "union_territory", "7th_amendment", "reasoning"]
    ))

    # R12: Bombay Bifurcation 1960
    questions.append(make_ut_q(
        qid="UT_R_012", diff="Medium", qtype="Reasoning",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): In 1960, the bilingual State of Bombay was bifurcated into Maharashtra and Gujarat.\nReason (R): Intense agitations by the Samyukta Maharashtra Samiti and the Mahagujarat Andolan demanded separate linguistic states for Marathi and Gujarati speakers.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): 1960-ல், இருமொழி பேசிய பம்பாய் மாநிலம் மகாராஷ்டிரா மற்றும் குஜராத் என இரு மாநிலங்களாகப் பிரிக்கப்பட்டது.\nகாரணம் (R): சம்யுக்தா மகாராஷ்டிரா சமிதி மற்றும் மகா குஜராத் இயக்கம் ஆகியவை மராத்தி மற்றும் குஜராத்தி பேசுபவர்களுக்காக தனித்தனி மொழிவாரி மாநிலங்களைக் கோரி தீவிரப் போராட்டங்களை நடத்தின.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the correct explanation of (A). The popular agitations forced Parliament to pass the Bombay Reorganisation Act, 1960, effective May 1, 1960, creating Gujarat as the 15th State.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். இந்த மக்கள் போராட்டங்கள் காரணமாக நாடாளுமன்றம் பம்பாய் மறுசீரமைப்புச் சட்டம் 1960-ஐ இயற்றி, மே 1, 1960 முதல் குஜராத்தை 15-வது மாநிலமாக உருவாக்கியது.",
        why_a_en="The agitations mentioned in (R) were the primary driving force behind the bifurcation in (A).",
        why_a_ta="(R)-ல் குறிப்பிடப்பட்டுள்ள போராட்டங்களே (A)-வில் உள்ள பிரிவினைக்கு முதன்மைக் காரணமாக அமைந்தன.",
        why_b_en="(R) directly explains the political cause of the bifurcation.",
        why_b_ta="(R) பிரிவினையின் அரசியல் காரணத்தை நேரடியாக விளக்குகிறது.",
        why_c_en="(R) is historically true.",
        why_c_ta="(R) வரலாற்று ரீதியாக சரியானது.",
        why_d_en="(A) is historically true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Gujarat became the 15th state of independent India on May 1, 1960.",
        tip_ta="குஜராத் மே 1, 1960 அன்று சுதந்திர இந்தியாவின் 15-வது மாநிலமானது.",
        fact_en="Bombay city was retained as the capital of Maharashtra.",
        fact_ta="பம்பாய் நகரம் மகாராஷ்டிராவின் தலைநகரமாகத் தக்கவைக்கப்பட்டது.",
        tags=["polity", "union_territory", "bombay", "gujarat", "reasoning"]
    ))

    # R13: Punjab Reorganisation 1966
    questions.append(make_ut_q(
        qid="UT_R_013", diff="Medium", qtype="Reasoning",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): In 1966, the State of Haryana was carved out of Punjab, and Chandigarh was made a Union Territory.\nReason (R): The Shah Commission recommended the creation of a separate Punjabi-speaking state and a Hindi-speaking state following the Punjabi Suba agitation led by Sant Fateh Singh.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): 1966-ல், பஞ்சாபிலிருந்து ஹரியானா மாநிலம் பிரிக்கப்பட்டு, சண்டிகர் ஒரு யூனியன் பிரதேசமாக உருவாக்கப்பட்டது.\nகாரணம் (R): சாந்த் பதே சிங் தலைமையிலான பஞ்சாபி சுபா இயக்கத்தைத் தொடர்ந்து, மொழி அடிப்படையில் பஞ்சாபி பேசும் பகுதிக்கு பஞ்சாப்பையும், இந்தி பேசும் பகுதிக்கு ஹரியானாவையும் உருவாக்க ஷா ஆணையம் பரிந்துரைத்தது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). Under the Punjab Reorganisation Act, 1966 (based on the Shah Commission report), Haryana was created as the 17th State, Chandigarh became a UT, and hilly areas were merged with Himachal Pradesh.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். ஷா ஆணையத்தின் பரிந்துரையின்படி 1966 பஞ்சாப் மறுசீரமைப்புச் சட்டம் ஹரியானாவை 17-வது மாநிலமாகவும், சண்டிகரை யூனியன் பிரதேசமாகவும் உருவாக்கியது.",
        why_a_en="The Shah Commission report was the direct blueprint for the 1966 reorganisation of Punjab.",
        why_a_ta="ஷா ஆணையத்தின் அறிக்கையே 1966 பஞ்சாப் மறுசீரமைப்பிற்கான நேரடி வழிகாட்டியாக இருந்தது.",
        why_b_en="(R) explains the rationale and mechanism for the creation of Haryana in (A).",
        why_b_ta="(R) ஹரியானா உருவாக்கப்பட்டதற்கான காரணத்தை விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Punjab Reorganisation: Haryana (17th State), Chandigarh (UT & joint capital), Nov 1, 1966.",
        tip_ta="பஞ்சாப் மறுசீரமைப்பு: ஹரியானா (17-வது மாநிலம்), சண்டிகர் (UT & கூட்டுத் தலைநகரம்), நவம்பர் 1, 1966.",
        fact_en="Hilly areas of Punjab like Kangra and Shimla were transferred to the Union Territory of Himachal Pradesh.",
        fact_ta="காங்ரா, சிம்லா போன்ற பஞ்சாபின் மலைப்பகுதிகள் இமாச்சல பிரதேச யூனியன் பிரதேசத்துடன் இணைக்கப்பட்டன.",
        tags=["polity", "union_territory", "punjab", "haryana", "shah_commission", "reasoning"]
    ))

    # R14: Sikkim Associate Status (35th vs 36th Amendment)
    questions.append(make_ut_q(
        qid="UT_R_014", diff="Hard", qtype="Reasoning",
        subtopic="Article 2: Admission or Establishment of New States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The status of Sikkim as an 'Associate State' under the 35th Constitutional Amendment Act, 1974 was unprecedented in the Indian constitutional framework.\nReason (R): The original Constitution of India did not contemplate the category of an 'Associate State', necessitating the insertion of Article 2A and the Tenth Schedule.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): 35-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1974-ன் கீழ் சிக்கிமிற்கு வழங்கப்பட்ட 'இணை மாநில' (Associate State) அந்தஸ்தானது இந்திய அரசியலமைப்பு வரலாற்றில் முன் எப்போதும் இல்லாத ஒன்றாகும்.\nகாரணம் (R): இந்திய அசல் அரசியலமைப்பு 'இணை மாநிலம்' என்ற ஒரு பிரிவை கொண்டிருக்கவில்லை; இதனால் உறுப்பு 2A மற்றும் பத்தாவது அட்டவணையை புதிதாக சேர்க்க வேண்டியதாயிற்று.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). The concept of an Associate State was novel and foreign to the Constitution. It lasted only briefly until the 36th CAA 1975 repealed Article 2A and made Sikkim a full state.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். இணை மாநிலம் என்ற கருத்து அரசியலமைப்பிற்கு முற்றிலும் புதியது என்பதால் உறுப்பு 2A சேர்க்கப்பட்டது. பின்னர் 36-வது திருத்தம் மூலம் சிக்கிம் முழு மாநிலமாக்கப்பட்டு உறுப்பு 2A நீக்கப்பட்டது.",
        why_a_en="Both statements are true and (R) explains why it was unprecedented (novel category required amendment).",
        why_a_ta="இரு கூற்றுகளும் சரியானது மற்றும் (R) ஏன் இது முன் எப்போதும் இல்லாதது என்பதை விளக்குகிறது.",
        why_b_en="(R) directly explains the unprecedented nature of the status in (A).",
        why_b_ta="(R) இந்த விசித்திரமான அந்தஸ்தின் காரணத்தை நேரடியாக விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Associate State = 35th CAA 1974 (Article 2A). Full State = 36th CAA 1975 (repealed Article 2A, added Art 371F).",
        tip_ta="இணை மாநிலம் = 35-வது திருத்தம் 1974 (உறுப்பு 2A). முழு மாநிலம் = 36-வது திருத்தம் 1975 (உறுப்பு 371F சேர்க்கப்பட்டது).",
        fact_en="The current 10th Schedule deals with anti-defection (52nd CAA 1985), not the old repealed Sikkim schedule.",
        fact_ta="தற்போதைய 10-வது அட்டவணை கட்சித்தாவல் தடைச் சட்டம் (1985) தொடர்பானது, பழைய சிக்கிம் அட்டவணை நீக்கப்பட்டுவிட்டது.",
        tags=["polity", "union_territory", "sikkim", "35th_amendment", "reasoning"]
    ))

    # R15: Delhi Article 239AA Exclusion of State List entries
    questions.append(make_ut_q(
        qid="UT_R_015", diff="Hard", qtype="Reasoning",
        subtopic="Special Provisions for Delhi (Article 239AA)",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Legislative Assembly of the National Capital Territory of Delhi does not possess the power to legislate on Public Order, Police, and Land.\nReason (R): Article 239AA(3)(a) explicitly excludes Entries 1, 2, and 18 of the State List from the legislative competence of the Delhi Legislative Assembly.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): தில்லி தேசிய தலைநகர் பகுதியின் சட்டப்பேரவை பொது ஒழுங்கு, காவல்துறை மற்றும் நிலம் ஆகிய விவகாரங்கள் மீது சட்டமியற்றும் அதிகாரத்தைக் கொண்டிருக்கவில்லை.\nகாரணம் (R): அரசியலமைப்பின் 239AA(3)(a) பிரிவு மாநிலப் பட்டியலின் பதிவுகள் 1, 2 மற்றும் 18 ஆகியவற்றை தில்லி சட்டப்பேரவையின் அதிகார வரம்பிலிருந்து வெளிப்படையாக விலக்குகிறது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the exact constitutional provision that explains (A). Public Order (Entry 1), Police (Entry 2), and Land (Entry 18) are reserved for the Union Government.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு துல்லியமான அரசியலமைப்பு விளக்கமாகும். பொது ஒழுங்கு (1), காவல்துறை (2), நிலம் (18) ஆகியவை ஒன்றிய அரசின் நேரடிக் கட்டுப்பாட்டில் உள்ளன.",
        why_a_en="Both statements are factually and legally true, and (R) cites the exact constitutional authority for (A).",
        why_a_ta="இரு கூற்றுகளும் உண்மையானவை மற்றும் (R) இதற்கான நேரடி அரசியலமைப்பு பிரிவைக் குறிப்பிடுகிறது.",
        why_b_en="(R) directly explains (A).",
        why_b_ta="(R) நேரடியாக (A)-வை விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Delhi Assembly exclusion: Entries 1 (Public Order), 2 (Police), and 18 (Land) of State List.",
        tip_ta="தில்லி சட்டமன்றத்திற்கு விலக்கப்பட்டவை: மாநிலப் பட்டியல் 1 (பொது ஒழுங்கு), 2 (காவல்துறை), 18 (நிலம்).",
        fact_en="Parliament retains concurrent power to make laws on ANY subject for Delhi, including all State List subjects.",
        fact_ta="தில்லியைப் பொறுத்தவரை மாநிலப் பட்டியலில் உள்ள அனைத்து விவகாரங்கள் மீதும் சட்டமியற்றும் முழு அதிகாரம் நாடாளுமன்றத்திற்கு உண்டு.",
        tags=["polity", "union_territory", "delhi", "article_239aa", "reasoning"]
    ))

    # R16: Delhi Council of Ministers Size
    questions.append(make_ut_q(
        qid="UT_R_016", diff="Medium", qtype="Reasoning",
        subtopic="Special Provisions for Delhi (Article 239AA)",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Council of Ministers in the National Capital Territory of Delhi cannot exceed 7 members, including the Chief Minister.\nReason (R): Article 239AA(4) provides that the size of the Council of Ministers in Delhi shall not exceed 10% of the total number of members in the Legislative Assembly.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): தில்லி தேசிய தலைநகர் பகுதியின் அமைச்சரவை முதலமைச்சர் உட்பட 7 உறுப்பினர்களுக்கு மிகாமல் இருக்க வேண்டும்.\nகாரணம் (R): தில்லி சட்டப்பேரவையின் மொத்த உறுப்பினர்களின் எண்ணிக்கையில் அமைச்சரவையின் அளவு 10%-க்கு மிகாமல் இருக்க வேண்டும் என்று உறுப்பு 239AA(4) கூறுகிறது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains (A). The Delhi Assembly has 70 seats. 10% of 70 equals 7. Unlike states where the limit is 15% (Article 164(1A)), Delhi has a constitutional limit of 10%.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். தில்லி சட்டப்பேரவையில் 70 இடங்கள் உள்ளன. 70-ல் 10% என்பது 7 ஆகும். மாநிலங்களில் வரம்பு 15% ஆக இருக்கும் போது, தில்லியில் அரசியலமைப்பு வரம்பு 10% மட்டுமே.",
        why_a_en="Delhi Assembly strength is 70; 10% limit results in exactly 7 ministers, making (R) the direct mathematical and legal explanation of (A).",
        why_a_ta="தில்லி சட்டமன்ற பலம் 70; 10% வரம்பு என்பது சரியாக 7 அமைச்சர்களைக் குறிக்கிறது, எனவே (R) என்பது (A)-விற்கான சரியான விளக்கம்.",
        why_b_en="(R) explains why the maximum is 7.",
        why_b_ta="(R) அமைச்சர்களின் எண்ணிக்கை ஏன் 7 ஆக உள்ளது என்பதை விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Council of Ministers limits: States = 15% (min 12), Delhi = 10% (max 7).",
        tip_ta="அமைச்சரவை உச்ச வரம்பு: மாநிலங்கள் = 15% (குறைந்தது 12), தில்லி = 10% (அதிகபட்சம் 7).",
        fact_en="The Chief Minister of Delhi is appointed by the President of India, not by the Lieutenant Governor.",
        fact_ta="தில்லி முதலமைச்சரை துணைநிலை ஆளுநர் நியமிப்பதில்லை; இந்தியக் குடியரசுத் தலைவரே நியமிக்கிறார்.",
        tags=["polity", "union_territory", "delhi", "council_of_ministers", "reasoning"]
    ))

    # R17: Union Territories Executive Head
    questions.append(make_ut_q(
        qid="UT_R_017", diff="Medium", qtype="Reasoning",
        subtopic="Administration of Union Territories",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): An Administrator or Lieutenant Governor of a Union Territory is not a constitutional head of state in the same manner as a Governor of a State.\nReason (R): Under Article 239, an Administrator is an agent and delegate of the President of India and exercises executive powers subject to presidential control.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): ஒரு யூனியன் பிரதேசத்தின் நிர்வாகி அல்லது துணைநிலை ஆளுநர் ஒரு மாநில ஆளுநரைப் போன்ற அரசியலமைப்பு ரீதியான மாநிலத் தலைவர் அல்ல.\nகாரணம் (R): உறுப்பு 239-ன் கீழ், நிர்வாகி என்பவர் இந்தியக் குடியரசுத் தலைவரின் பிரதிநிதி மற்றும் முகவர் ஆவார்; அவர் குடியரசுத் தலைவரின் கட்டுப்பாட்டிற்கு உட்பட்டே நிர்வாக அதிகாரங்களைச் செலுத்துகிறார்.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). As affirmed in Shamsher Singh (1974) and Govt of NCT of Delhi (2018), an Administrator is an agent of the President and not an independent constitutional head like a Governor.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். சம்ஷேர் சிங் வழக்கு (1974) மற்றும் தில்லி அரசு வழக்கு (2018) ஆகியவற்றில் தெளிவுபடுத்தப்பட்டபடி, யூனியன் பிரதேச நிர்வாகி குடியரசுத் தலைவரின் முகவரே அன்றி ஆளுநரைப் போன்ற தனித்துவ அரசியலமைப்புத் தலைவர் அல்ல.",
        why_a_en="Both statements are true and (R) accurately explains why an Administrator lacks the constitutional status of a Governor.",
        why_a_ta="இரு கூற்றுகளும் உண்மையானவை மற்றும் (R) நிர்வாகிக்கு ஏன் ஆளுநரின் அரசியலமைப்பு அந்தஸ்து இல்லை என்பதை விளக்குகிறது.",
        why_b_en="(R) is the direct explanation of (A).",
        why_b_ta="(R) நேரடியாக (A)-வை விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Governor = Constitutional head of State. Administrator/LG = Agent/Delegate of President in UT.",
        tip_ta="ஆளுநர் = மாநிலத்தின் அரசியலமைப்புத் தலைவர். நிர்வாகி/துணைநிலை ஆளுநர் = UT-ல் குடியரசுத் தலைவரின் முகவர்.",
        fact_en="Article 239 allows the President to specify different designations such as Lieutenant Governor, Chief Commissioner, or Administrator.",
        fact_ta="உறுப்பு 239 குடியரசுத் தலைவர் துணைநிலை ஆளுநர் அல்லது நிர்வாகி எனப் பல்வேறு பெயர்களைக் குறிப்பிட அனுமதிக்கிறது.",
        tags=["polity", "union_territory", "administration", "lieutenant_governor", "reasoning"]
    ))

    # R18: High Courts for UTs (Article 241)
    questions.append(make_ut_q(
        qid="UT_R_018", diff="Medium", qtype="Reasoning",
        subtopic="Administration of Union Territories",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): Parliament can by law establish a separate High Court for any Union Territory or extend the jurisdiction of an existing High Court to a Union Territory.\nReason (R): Article 241 of the Constitution empowers Parliament to constitute a High Court for a Union Territory or declare any court in such territory to be a High Court.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): நாடாளுமன்றம் சட்டத்தின் மூலம் எந்தவொரு யூனியன் பிரதேசத்திற்கும் ஒரு தனி உயர்நீதிமன்றத்தை அமைக்கலாம் அல்லது தற்போதுள்ள ஒரு உயர்நீதிமன்றத்தின் அதிகார வரம்பை ஒரு யூனியன் பிரதேசத்திற்கு விரிவுபடுத்தலாம்.\nகாரணம் (R): அரசியலமைப்பின் 241-வது பிரிவு யூனியன் பிரதேசத்திற்கு ஒரு உயர்நீதிமன்றத்தை அமைக்க அல்லது அத்தகைய பிரதேசத்திலுள்ள எந்தவொரு நீதிமன்றத்தையும் உயர்நீதிமன்றமாக அறிவிக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the exact constitutional empowering provision for (A). Under Article 241, Parliament established the Delhi High Court in 1966.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு நேரடி அரசியலமைப்பு அதிகார விதியாகும். உறுப்பு 241-ன் கீழ் நாடாளுமன்றம் 1966-ல் தில்லி உயர்நீதிமன்றத்தை அமைத்தது.",
        why_a_en="Article 241 is the specific article that enables Parliament to create or extend High Courts for UTs.",
        why_a_ta="உறுப்பு 241 என்பது யூனியன் பிரதேசங்களுக்கு உயர்நீதிமன்றங்களை உருவாக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கும் குறிப்பிட்ட பிரிவாகும்.",
        why_b_en="(R) directly explains the legislative power in (A).",
        why_b_ta="(R) நாடாளுமன்றத்தின் அதிகாரத்தை நேரடியாக விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Article 241: High Courts for Union Territories.",
        tip_ta="உறுப்பு 241: யூனியன் பிரதேசங்களுக்கான உயர்நீதிமன்றங்கள்.",
        fact_en="Delhi is the only UT with a dedicated separate High Court; J&K and Ladakh share a common High Court.",
        fact_ta="தில்லி தனக்கென தனி உயர்நீதிமன்றத்தைக் கொண்ட ஒரே UT ஆகும்; ஜம்மு காஷ்மீர் மற்றும் லடாக் பொதுவான நீதிமன்றத்தைப் பகிர்ந்து கொள்கின்றன.",
        tags=["polity", "union_territory", "article_241", "high_court", "reasoning"]
    ))

    # R19: J&K Downgrading into UTs 2019
    questions.append(make_ut_q(
        qid="UT_R_019", diff="Hard", qtype="Reasoning",
        subtopic="Jammu & Kashmir Reorganisation (2019)",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Jammu and Kashmir Reorganisation Act, 2019 was historically unprecedented in the evolution of Indian federalism.\nReason (R): For the first time in independent India, a full-fledged State was downgraded and bifurcated into two Union Territories.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): ஜம்மு காஷ்மீர் மறுசீரமைப்புச் சட்டம் 2019, இந்தியக் கூட்டாட்சியின் பரிணாம வளர்ச்சியில் வரலாற்றில் முன் எப்போதும் நடந்திராத ஒரு நிகழ்வாகும்.\nகாரணம் (R): சுதந்திர இந்தியாவில் முதல்முறையாக, ஒரு முழு மாநிலமானது தரம் குறைக்கப்பட்டு இரண்டு யூனியன் பிரதேசங்களாகப் பிரிக்கப்பட்டது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). While several UTs had previously been upgraded into States (e.g., HP, Manipur, Goa), a State had never before been downgraded into Union Territories.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். இதற்கு முன்பு பல யூனியன் பிரதேசங்கள் முழு மாநிலங்களாக உயர்த்தப்பட்டிருந்தாலும் (எ.கா: இமாச்சலம், கோவா), ஒரு மாநிலம் யூனியன் பிரதேசங்களாகத் தரம் குறைக்கப்பட்டது இதுவே முதல் முறையாகும்.",
        why_a_en="Both statements are true and (R) provides the historical basis for why the 2019 Act was unprecedented.",
        why_a_ta="இரு கூற்றுகளும் உண்மையானவை மற்றும் 2019 சட்டம் ஏன் முன் எப்போதும் இல்லாதது என்பதை (R) விளக்குகிறது.",
        why_b_en="(R) directly explains the assertion.",
        why_b_ta="(R) கூற்றை நேரடியாக விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Previous trajectory was always UT -> State. 2019 J&K was the first State -> UT.",
        tip_ta="முன்பு எப்போதும் UT -> மாநிலம் என்றே இருந்தது. 2019 ஜம்மு காஷ்மீர் மட்டுமே முதல் முறையாக மாநிலம் -> UT ஆனது.",
        fact_en="The Supreme Court upheld the reorganisation and directed the Election Commission to conduct assembly polls in J&K by September 2024.",
        fact_ta="உச்சநீதிமன்றம் இந்த மறுசீரமைப்பை உறுதி செய்ததுடன், செப்டம்பர் 2024-க்குள் சட்டமன்றத் தேர்தலை நடத்த உத்தரவிட்டது.",
        tags=["polity", "union_territory", "jammu_kashmir", "2019", "reasoning"]
    ))

    # R20: Merger of DNH & DD 2020
    questions.append(make_ut_q(
        qid="UT_R_020", diff="Medium", qtype="Reasoning",
        subtopic="Merger of Dadra & Nagar Haveli and Daman & Diu (2020)",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): In January 2020, Dadra and Nagar Haveli and Daman and Diu were merged into a single Union Territory.\nReason (R): The merger was executed under Article 3 to eliminate administrative duplication, reduce government expenditure, and improve governance efficiency.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): ஜனவரி 2020-ல், தாத்ரா மற்றும் நகர் ஹவேலி மற்றும் தாமன் மற்றும் தியூ ஆகியவை ஒரே யூனியன் பிரதேசமாக இணைக்கப்பட்டன.\nகாரணம் (R): இரட்டை நிர்வாகச் செலவுகளைக் குறைக்கவும், அரசு நிர்வாகத் திறனை மேம்படுத்தவும் உறுப்பு 3-ன் கீழ் இந்த இணைப்பு மேற்கொள்ளப்பட்டது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains the rationale and constitutional basis (Article 3) for the merger that took effect on January 26, 2020.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். 2020 ஜனவரி 26 அன்று நடைமுறைக்கு வந்த இந்த இணைப்பு நிர்வாகச் செலவைக் குறைத்து செயல்திறனைக் கூட்ட உறுப்பு 3-ன் கீழ் மேற்கொள்ளப்பட்டது.",
        why_a_en="Both statements are true and (R) provides the administrative rationale stated in the Statement of Objects and Reasons of the Act.",
        why_a_ta="இரு கூற்றுகளும் உண்மையே மற்றும் (R) சட்டத்தின் நோக்கங்களில் கூறப்பட்ட நிர்வாகக் காரணத்தை விளக்குகிறது.",
        why_b_en="(R) explains why the two UTs were merged.",
        why_b_ta="(R) இரு UT-களும் ஏன் இணைக்கப்பட்டன என்பதை விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Merger effective: January 26, 2020. Reduced total UTs in India from 9 to 8.",
        tip_ta="இணைப்பு அமலானது: 26 ஜனவரி 2020. இந்தியாவின் மொத்த UT-களின் எண்ணிக்கை 9-லிருந்து 8 ஆகக் குறைந்தது.",
        fact_en="Daman serves as the administrative headquarters of the merged Union Territory.",
        fact_ta="இணைக்கப்பட்ட புதிய யூனியன் பிரதேசத்தின் நிர்வாகத் தலைமையகமாக தாமன் செயல்படுகிறது.",
        tags=["polity", "union_territory", "merger_2020", "reasoning"]
    ))

    # R21: Potti Sriramulu Fast and Government Action
    questions.append(make_ut_q(
        qid="UT_R_021", diff="Medium", qtype="Reasoning",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Government of India was compelled to create the first linguistic state (Andhra State) in October 1953.\nReason (R): Potti Sriramulu died on December 15, 1952, after a 56-day hunger strike demanding a separate state for Telugu-speaking people, sparking widespread unrest.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): அக்டோபர் 1953-ல் முதல் மொழிவாரி மாநிலமான ஆந்திர மாநிலத்தை உருவாக்க இந்திய அரசு நிர்பந்திக்கப்பட்டது.\nகாரணம் (R): தெலுங்கு பேசும் மக்களுக்கு தனி மாநிலம் கோரி 56 நாட்கள் உண்ணாவிரதம் இருந்த பொட்டி ஸ்ரீராமுலு 1952 டிசம்பர் 15 அன்று உயிர்நீத்ததால் பெரும் கலவரங்கள் வெடித்தன.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). The death of Potti Sriramulu caused immense public outrage, forcing PM Nehru to announce the creation of Andhra State, which was inaugurated on October 1, 1953.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு நேரடி விளக்கமாகும். பொட்டி ஸ்ரீராமுலுவின் தியாகமும் அதைத் தொடர்ந்து ஏற்பட்ட மக்கள் எழுச்சியுமே நேரு அரசை ஆந்திர மாநிலத்தை உடனடியாக உருவாக்க நிர்பந்தித்தது.",
        why_a_en="The martyrdom of Potti Sriramulu directly caused the immediate formation of Andhra State.",
        why_a_ta="பொட்டி ஸ்ரீராமுலுவின் உயிர் தியாகமே உடனடியாக ஆந்திர மாநிலம் உருவாவதற்கு நேரடிக் காரணமாக அமைந்தது.",
        why_b_en="(R) is the direct historical explanation for (A).",
        why_b_ta="(R) என்பது (A)-விற்கான நேரடி வரலாற்று விளக்கமாகும்.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Andhra was created on Oct 1, 1953, with Kurnool as capital and Guntur as HC seat.",
        tip_ta="1953 அக்டோபர் 1-ல் கர்னூலைத் தலைநகராகவும், குண்டூரை உயர்நீதிமன்றமாகவும் கொண்டு ஆந்திரா உருவானது.",
        fact_en="Tanguturi Prakasam Pantulu became the first Chief Minister of Andhra State.",
        fact_ta="ஆந்திர மாநிலத்தின் முதல் முதலமைச்சராக தங்குதூரி பிரகாசம் பந்துலு பொறுப்பேற்றார்.",
        tags=["polity", "union_territory", "andhra", "potti_sriramulu", "reasoning"]
    ))

    # R22: 18th Constitutional Amendment 1966
    questions.append(make_ut_q(
        qid="UT_R_022", diff="Hard", qtype="Reasoning",
        subtopic="Article 3: Formation of New States and Alteration of Areas",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The 18th Constitutional Amendment Act, 1966 clarified that the term 'State' in clauses (a) to (e) of Article 3 includes a 'Union Territory'.\nReason (R): Prior to 1966, there was legal ambiguity whether Parliament had the power under Article 3 to form a new Union Territory by uniting parts of states or other territories.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): 18-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1966, உறுப்பு 3-ன் உட்பிரிவுகள் (a) முதல் (e) வரையிலான 'மாநிலம்' என்ற சொல்லில் 'யூனியன் பிரதேசமும்' அடங்கும் என்பதைத் தெளிவுபடுத்தியது.\nகாரணம் (R): 1966-க்கு முன்பு, மாநிலங்களின் பகுதிகளை இணைத்து ஒரு புதிய யூனியன் பிரதேசத்தை உருவாக்கும் அதிகாரம் நாடாளுமன்றத்திற்கு உறுப்பு 3-ன் கீழ் உள்ளதா என்பதில் சட்ட ரீதியான தெளிவின்மை நிலவியது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains (A). The 18th CAA added Explanation I and II to Article 3, clarifying that while 'state' includes UTs for reorganisation, the proviso on consulting the legislature does not apply to UTs.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். 18-வது திருத்தம் உறுப்பு 3-ல் விளக்கங்களைச் சேர்த்து, மறுசீரமைப்பில் 'மாநிலம்' என்பதில் யூனியன் பிரதேசங்களும் அடங்கும் என்பதையும், அதேசமயம் யூனியன் பிரதேசங்களின் சட்டமன்ற கருத்தைக் கேட்க வேண்டிய அவசியமில்லை என்பதையும் தெளிவுபடுத்தியது.",
        why_a_en="The 18th CAA was enacted specifically during the Punjab reorganization to create Chandigarh as a UT.",
        why_a_ta="சண்டிகரை யூனியன் பிரதேசமாக உருவாக்க பஞ்சாப் மறுசீரமைப்பின் போது 18-வது திருத்தம் இயற்றப்பட்டது.",
        why_b_en="(R) is the exact rationale for enacting the 18th Amendment.",
        why_b_ta="(R) என்பது 18-வது திருத்தம் இயற்றப்பட்டதற்கான துல்லியமான காரணமாகும்.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="18th CAA 1966 added Explanation I & II to Article 3.",
        tip_ta="18-வது திருத்தம் 1966 உறுப்பு 3-ல் விளக்கம் I & II-ஐ சேர்த்தது.",
        fact_en="Explanation II clarifies that Parliament's power to form a new State includes forming a new Union Territory.",
        fact_ta="விளக்கம் II ஒரு புதிய மாநிலத்தை உருவாக்கும் அதிகாரத்தில் புதிய யூனியன் பிரதேசத்தை உருவாக்குவதும் அடங்கும் என்பதைத் தெளிவுபடுத்துகிறது.",
        tags=["polity", "union_territory", "18th_amendment", "article_3", "reasoning"]
    ))

    # R23: Integration of Junagadh by Plebiscite
    questions.append(make_ut_q(
        qid="UT_R_023", diff="Medium", qtype="Reasoning",
        subtopic="Integration of Princely States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The accession of the princely state of Junagadh to the Indian Union was formalized through a plebiscite in February 1948.\nReason (R): While the Muslim Nawab had acceded to Pakistan, the overwhelming majority of the population was Hindu and revolted, demanding merger with India.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): பிப்ரவரி 1948-ல் நடத்தப்பட்ட பொது வாக்கெடுப்பின் (Plebiscite) மூலமாக ஜூனாகத் சமஸ்தானத்தின் இந்திய இணைப்பு முறைப்படுத்தப்பட்டது.\nகாரணம் (R): முஸ்லிம் நவாப் பாகிஸ்தானுடன் இணைய முடிவு செய்த போதிலும், பெரும்பான்மை இந்து மக்கள் கிளர்ந்தெழுந்து இந்தியாவுடன் இணையக் கோரினர்.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains (A). The popular revolt forced the Nawab to flee, and India held a referendum in February 1948 where over 99% voted for merger with India.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். மக்களின் கிளர்ச்சியால் நவாப் பாகிஸ்தானுக்கு தப்பி ஓடிய நிலையில், பிப்ரவரி 1948-ல் நடத்தப்பட்ட வாக்கெடுப்பில் 99%-க்கும் அதிகமானோர் இந்தியாவுக்கு ஆதரவாக வாக்களித்தனர்.",
        why_a_en="The situation described in (R) directly explains why a democratic plebiscite was conducted in (A).",
        why_a_ta="(R)-ல் விவரிக்கப்பட்ட சூழலே (A)-ல் பொது வாக்கெடுப்பு நடத்தப்பட்டதற்கான நேரடிக் காரணமாகும்.",
        why_b_en="(R) directly explains (A).",
        why_b_ta="(R) நேரடியாக (A)-வை விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Princely States Integration: Junagadh (Plebiscite), Hyderabad (Police action), Kashmir (Instrument of Accession).",
        tip_ta="சமஸ்தானங்கள் இணைப்பு: ஜூனாகத் (வாக்கெடுப்பு), ஹைதராபாத் (காவல்துறை நடவடிக்கை), காஷ்மீர் (இணைப்பு ஒப்பந்தம்).",
        fact_en="Out of 190,870 registered voters, only 91 voted for Pakistan in the Junagadh plebiscite.",
        fact_ta="ஜூனாகத் வாக்கெடுப்பில் 1,90,870 வாக்காளர்களில் 91 பேர் மட்டுமே பாகிஸ்தானுக்கு ஆதரவாக வாக்களித்தனர்.",
        tags=["polity", "union_territory", "junagadh", "plebiscite", "reasoning"]
    ))

    # R24: French Territories Transfer (De facto vs De jure)
    questions.append(make_ut_q(
        qid="UT_R_024", diff="Hard", qtype="Reasoning",
        subtopic="Article 2: Admission or Establishment of New States",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): Puducherry was formally incorporated into the First Schedule of the Indian Constitution only in 1962, even though India took over its administration in 1954.\nReason (R): While the de facto transfer of power took place on November 1, 1954, the treaty of cession was ratified by the French Parliament (de jure transfer) only in May 1962.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): இந்தியா 1954-லேயே புதுச்சேரியின் நிர்வாகத்தை ஏற்றுக்கொண்ட போதிலும், 1962-ல் தான் இந்திய அரசியலமைப்பின் முதல் அட்டவணையில் புதுச்சேரி அதிகாரப்பூர்வமாக இணைக்கப்பட்டது.\nகாரணம் (R): நடைமுறை அதிகார மாற்றம் (De facto) 1954 நவம்பர் 1 அன்று நிகழ்ந்தாலும், பிரெஞ்சு நாடாளுமன்றம் நிலப்பரப்பு ஒப்படைப்பு ஒப்பந்தத்தை சட்டப்பூர்வமாக (De jure) மே 1962-ல் தான் ஏற்பளித்தது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains (A). Until the French Parliament ratified the treaty in 1962, Puducherry was administered as an acquired territory under Article 1(3)(c). After de jure transfer, the 14th CAA 1962 formally made it a Union Territory.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். 1962-ல் பிரெஞ்சு நாடாளுமன்றம் ஏற்பளிக்கும் வரை புதுச்சேரி உறுப்பு 1(3)(c)-ன் கீழ் கையகப்படுத்தப்பட்ட பகுதியாகவே நிர்வகிக்கப்பட்டது. 1962-ல் 14-வது திருத்தம் மூலம் அதிகாரப்பூர்வ UT ஆனது.",
        why_a_en="The constitutional delay between 1954 and 1962 is accurately explained by the difference between de facto and de jure transfer in (R).",
        why_a_ta="1954 முதல் 1962 வரையிலான காலதாமதத்திற்கு நடைமுறை மற்றும் சட்டப்பூர்வ மாற்றமே காரணம் என்பதை (R) விளக்குகிறது.",
        why_b_en="(R) directly explains the gap in (A).",
        why_b_ta="(R) கால இடைவெளியை நேரடியாக விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="De facto transfer = Nov 1, 1954. De jure transfer = Aug 16, 1962 (Treaty ratified May 1962).",
        tip_ta="நடைமுறை மாற்றம் = நவம்பர் 1, 1954. சட்டப்பூர்வ மாற்றம் = ஆகஸ்ட் 16, 1962 (ஒப்பந்த ஏற்பளிப்பு மே 1962).",
        fact_en="August 16 is celebrated as De Jure Transfer Day in Puducherry.",
        fact_ta="புதுச்சேரியில் ஆகஸ்ட் 16 'டி ஜூரே' (சட்டப்பூர்வ மாற்ற) தினமாகக் கொண்டாடப்படுகிறது.",
        tags=["polity", "union_territory", "puducherry", "14th_amendment", "reasoning"]
    ))

    # R25: President's Power to Make Regulations for UTs (Article 240)
    questions.append(make_ut_q(
        qid="UT_R_025", diff="Hard", qtype="Reasoning",
        subtopic="Administration of Union Territories",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The President of India can make regulations for the peace, progress, and good government of certain Union Territories which have the same force and effect as an Act of Parliament.\nReason (R): Under Article 240 of the Constitution, presidential regulations can repeal or amend any Act made by Parliament applicable to that Union Territory.\nSelect the correct answer using the codes given below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): குறிப்பிட்ட சில யூனியன் பிரதேசங்களின் அமைதி, முன்னேற்றம் மற்றும் நல்லாட்சிக்காக இந்தியக் குடியரசுத் தலைவர் விதிமுறைகளை (Regulations) உருவாக்கலாம்; இவை நாடாளுமன்றச் சட்டத்திற்கு இணையான வலிமையைக் கொண்டிருக்கும்.\nகாரணம் (R): அரசியலமைப்பின் 240-வது பிரிவின் கீழ், குடியரசுத் தலைவர் பிறப்பிக்கும் விதிமுறைகள் அந்த யூனியன் பிரதேசத்திற்குப் பொருந்தக்கூடிய நாடாளுமன்றத்தின் எந்தவொரு சட்டத்தையும் திருத்தவோ அல்லது ரத்து செய்யவோ அதிகாரம் கொண்டவை.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="Both (A) and (R) are true and (R) is the correct explanation of (A)",
        ta_a="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்",
        en_b="Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        ta_b="(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        en_c="(A) is true but (R) is false",
        ta_c="(A) சரி, ஆனால் (R) தவறு",
        en_d="(A) is false but (R) is true",
        ta_d="(A) தவறு, ஆனால் (R) சரி",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains the sweeping nature of presidential legislative power under Article 240. Article 240(2) explicitly provides that any regulation made by the President may repeal or amend any Act made by Parliament applicable to that territory.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். உறுப்பு 240(2) குடியரசுத் தலைவர் பிறப்பிக்கும் விதிமுறைகள் அக்குறிப்பிட்ட யூனியன் பிரதேசத்திற்குப் பொருந்தக்கூடிய நாடாளுமன்றச் சட்டத்தையே திருத்தவோ அல்லது ரத்து செய்யவோ அதிகாரம் கொண்டவை என வெளிப்படையாகக் கூறுகிறது.",
        why_a_en="Both statements accurately state the provisions of Article 240(1) and 240(2).",
        why_a_ta="இரு கூற்றுகளும் உறுப்பு 240(1) மற்றும் 240(2)-ன் விதிகளைத் துல்லியமாக விளக்குகின்றன.",
        why_b_en="(R) directly explains the legislative strength asserted in (A).",
        why_b_ta="(R) கூற்று (A)-ல் கூறப்பட்டுள்ள சட்ட வலிமையை நேரடியாக விளக்குகிறது.",
        why_c_en="(R) is true.",
        why_c_ta="(R) சரியானது.",
        why_d_en="(A) is true.",
        why_d_ta="(A) சரியானது.",
        tip_en="Article 240: Power of President to make regulations for peace, progress, and good government of certain UTs.",
        tip_ta="உறுப்பு 240: குறிப்பிட்ட UT-களின் அமைதி, வளர்ச்சி மற்றும் நல்லாட்சிக்காக விதிமுறைகளை உருவாக்க குடியரசுத் தலைவருக்கு உள்ள அதிகாரம்.",
        fact_en="When a legislature is constituted for Puducherry, the President cannot make regulations unless the assembly is dissolved or suspended.",
        fact_ta="புதுச்சேரியில் சட்டப்பேரவை செயல்படும் போது குடியரசுத் தலைவரால் விதிமுறைகளை உருவாக்க முடியாது; சபை முடக்கப்பட்டால் மட்டுமே முடியும்.",
        tags=["polity", "union_territory", "article_240", "president_regulations", "reasoning"]
    ))

    return questions

def main():
    questions = get_reasoning_questions()
    print(f"Generated {len(questions)} Reasoning questions.")
    
    for idx, q in enumerate(questions, 1):
        q["id"] = f"UT_R_{idx:03d}"
        
    balanced = balance_question_keys(questions)
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "union_territory_reasoning.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(balanced)} questions to {out_file}")
    
    res = ContentValidator.validate_file(out_file, expected_count=25, expected_prefix="UT_R_")
    print("\n--- ContentValidator Summary ---")
    print(res.summary())
    if not res.is_valid:
        print("Issues found:")
        for issue in res.issues:
            print(f" - [{issue.severity}] {issue.field}: {issue.message}")
        sys.exit(1)
    else:
        print("\nALL 25 REASONING QUESTIONS VALIDATED PERFECTLY! (PASS)")

if __name__ == "__main__":
    main()
