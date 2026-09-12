# -*- coding: utf-8 -*-
"""
Builder for 25 Municipalities Reasoning (Assertion & Reason) MCQs (MUN_R_001 to MUN_R_025).
Strictly adheres to 24-field schema, balanced keys, and authentic Tamil translation.
"""
import json
import os
from mun_mcq_helper import make_mun_q
from rebalance_mun_helper import balance_question_keys

def get_reasoning_25():
    questions = []

    # Standard A&R options
    opt_a_en = "Both (A) and (R) are true and (R) is the correct explanation of (A)"
    opt_a_ta = "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும்"
    opt_b_en = "Both (A) and (R) are true but (R) is not the correct explanation of (A)"
    opt_b_ta = "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-விற்கான சரியான விளக்கமல்ல"
    opt_c_en = "(A) is true but (R) is false"
    opt_c_ta = "(A) சரி, ஆனால் (R) தவறு"
    opt_d_en = "(A) is false but (R) is true"
    opt_d_ta = "(A) தவறு, ஆனால் (R) சரி"

    def make_ar_q(qid, subtopic, a_en, a_ta, r_en, r_ta, correct_key, exp_en, exp_ta, why_eval, tip_en, tip_ta, fact_en, fact_ta, tags):
        stem_en = f"Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): {a_en}\nReason (R): {r_en}\nSelect the correct answer using the code below:"
        stem_ta = f"கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று உறுதிமொழி (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): {a_ta}\nகாரணம் (R): {r_ta}\nகீழ்க்கண்ட குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:"
        
        # Build why_not_others
        why_a_en = "Option A is correct: Both statements are factual truths and Reason causally explains Assertion." if correct_key == "A" else why_eval.get("A", "Option A is incorrect.")
        why_a_ta = "விருப்பம் A சரியானது: இரண்டு கூற்றுகளும் உண்மையானவை மற்றும் காரணம் உறுதிமொழியை சரியாக விளக்குகிறது." if correct_key == "A" else why_eval.get("A_ta", "விருப்பம் A தவறானது.")
        
        why_b_en = "Option B is correct: Both statements are true but Reason does not provide the causal explanation." if correct_key == "B" else why_eval.get("B", "Option B is incorrect.")
        why_b_ta = "விருப்பம் B சரியானது: இரண்டும் சரி ஆனால் காரணம் சரியான விளக்கமல்ல." if correct_key == "B" else why_eval.get("B_ta", "விருப்பம் B தவறானது.")
        
        why_c_en = "Option C is correct: Assertion is true but Reason is factually false." if correct_key == "C" else why_eval.get("C", "Option C is incorrect.")
        why_c_ta = "விருப்பம் C சரியானது: உறுதிமொழி சரி ஆனால் காரணம் தவறு." if correct_key == "C" else why_eval.get("C_ta", "விருப்பம் C தவறானது.")
        
        why_d_en = "Option D is correct: Assertion is false but Reason is factually true." if correct_key == "D" else why_eval.get("D", "Option D is incorrect.")
        why_d_ta = "விருப்பம் D சரியானது: உறுதிமொழி தவறு ஆனால் காரணம் சரி." if correct_key == "D" else why_eval.get("D_ta", "விருப்பம் D தவறானது.")

        return make_mun_q(
            qid=qid,
            diff="Hard",
            qtype="Assertion and Reasoning",
            subtopic=subtopic,
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=opt_a_en,
            ta_a=opt_a_ta,
            en_b=opt_b_en,
            ta_b=opt_b_ta,
            en_c=opt_c_en,
            ta_c=opt_c_ta,
            en_d=opt_d_en,
            ta_d=opt_d_ta,
            correct_key=correct_key,
            exp_en=exp_en,
            exp_ta=exp_ta,
            why_a_en=why_a_en,
            why_a_ta=why_a_ta,
            why_b_en=why_b_en,
            why_b_ta=why_b_ta,
            why_c_en=why_c_en,
            why_c_ta=why_c_ta,
            why_d_en=why_d_en,
            why_d_ta=why_d_ta,
            tip_en=tip_en,
            tip_ta=tip_ta,
            fact_en=fact_en,
            fact_ta=fact_ta,
            tags=tags
        )

    # R01: 74th Amendment Constitutional Status
    questions.append(make_ar_q(
        qid="MUN_R_001",
        subtopic="Constitutional Status",
        a_en="The 74th Constitutional Amendment Act revived urban local bodies as vibrant representative institutions of grassroots democracy in India.",
        a_ta="74-வது அரசியலமைப்பு திருத்தச் சட்டம் இந்தியாவில் நகர்ப்புற உள்ளாட்சி அமைப்புகளை அடித்தள மக்களாட்சியின் துடிப்பான பிரதிநிதித்துவ அமைப்புகளாக மீட்டெடுத்தது.",
        r_en="Prior to the 74th Amendment, urban local bodies suffered from prolonged suppression, irregular elections, and acute financial inadequacy.",
        r_ta="74-வது திருத்தத்திற்கு முன்பு, நகர்ப்புற உள்ளாட்சிகள் தொடர் முடக்கம், ஒழுங்கற்ற தேர்தல்கள் மற்றும் கடுமையான நிதிப் பற்றாக்குறையால் பாதிக்கப்பட்டிருந்தன.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the correct explanation of (A). The constitutional recognition was necessitated precisely because pre-1992 municipal bodies were routinely superseded by state executives without holding regular elections.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். 1992-க்கு முன்பு நகராட்சிகள் தொடர்ந்து கலைக்கப்பட்டு தேர்தல்கள் நடத்தப்படாமல் இருந்ததாலேயே அரசியலமைப்பு அந்தஸ்து வழங்கப்பட்டது.",
        why_eval={"B": "Reason directly explains why constitutional status was enacted.", "B_ta": "காரணம் உறுதிமொழிக்கான நேரடி வரலாற்றுப் பின்னணியை விளக்குகிறது.", "C": "Reason is completely true.", "C_ta": "காரணம் முற்றிலும் உண்மையானது.", "D": "Assertion is completely true.", "D_ta": "உறுதிமொழி முற்றிலும் சரியானது."},
        tip_en="In A&R, ask 'WHY did (A) happen?' If (R) answers it with a factual reason, choose A.",
        tip_ta="உறுதிமொழிக்கு 'ஏன்?' என்று கேள்வி கேட்டு, காரணம் விடையளித்தால் விருப்பம் A-ஐத் தேர்ந்தெடுக்கவும்.",
        fact_en="The 74th Amendment introduced Part IXA containing Articles 243P to 243ZG.",
        fact_ta="74-வது திருத்தச் சட்டம் பகுதி IXA மற்றும் உறுப்புகள் 243P முதல் 243ZG வரை சேர்த்தது.",
        tags=["74th_caa", "reasoning", "constitutional_status"]
    ))

    # R02: Article 243Q Industrial Townships
    questions.append(make_ar_q(
        qid="MUN_R_002",
        subtopic="Article 243Q Industrial Township",
        a_en="A Municipal Corporation or Municipal Council may not be constituted in an urban area having large industrial establishments.",
        a_ta="பெரிய தொழிற்துறை நிறுவனங்களைக் கொண்ட ஒரு நகர்ப்புற பகுதியில் மாநகராட்சியோ அல்லது நகர்மன்றமோ அமைக்கப்படாமல் இருக்கலாம்.",
        r_en="Under the proviso to Article 243Q(1), the Governor may specify an industrial township where municipal services are provided by an industrial establishment.",
        r_ta="உறுப்பு 243Q(1)-ன் வரம்பு நிபந்தனையின் கீழ், ஒரு தொழிற்துறை நிறுவனத்தால் நகராட்சி சேவைகள் வழங்கப்படும் தொழில் நகரியத்தை ஆளுநர் அறிவிக்கலாம்.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). The proviso to Article 243Q(1) explicitly empowers the Governor to designate industrial townships (e.g. Jamshedpur, BHEL townships) exempting them from an elected municipality.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். உறுப்பு 243Q(1)-ன் வரம்பு நிபந்தனை தொழில் நகரியங்களுக்கு தேர்ந்தெடுக்கப்பட்ட நகராட்சியிலிருந்து விலக்களிக்க ஆளுநருக்கு அதிகாரமளிக்கிறது.",
        why_eval={"B": "R provides the constitutional exception mechanism for A.", "B_ta": "R என்பது A-விற்கான அரசியலமைப்பு விதிவிலக்கை விளக்குகிறது.", "C": "Reason is true.", "C_ta": "காரணம் சரியானது.", "D": "Assertion is true.", "D_ta": "உறுதிமொழி சரியானது."},
        tip_en="Remember the exception to Article 243Q(1): Industrial Townships designated by the Governor.",
        tip_ta="உறுப்பு 243Q(1)-ன் விதிவிலக்கு: ஆளுநரால் அறிவிக்கப்படும் தொழில் நகரியங்கள்.",
        fact_en="Such industrial townships do not have an elected municipal council.",
        fact_ta="இத்தகைய தொழில் நகரியங்களில் தேர்ந்தெடுக்கப்பட்ட நகர்மன்றம் இருப்பதில்லை.",
        tags=["article_243q", "industrial_township", "reasoning"]
    ))

    # R03: Article 243R Nominated Members
    questions.append(make_ar_q(
        qid="MUN_R_003",
        subtopic="Article 243R Nominated Members",
        a_en="Persons having special knowledge or experience in municipal administration nominated to a Municipality do not have voting rights in council meetings.",
        a_ta="நகராட்சி நிர்வாகத்தில் சிறப்பு அறிவு அல்லது அனுபவம் வாய்ந்த நபர்கள் நகராட்சிக்கு நியமிக்கப்பட்டாலும், அவர்களுக்கு மன்றக் கூட்டங்களில் வாக்களிக்கும் உரிமை இல்லை.",
        r_en="The Constitution strictly preserves decision-making and voting supremacy exclusively for directly elected representatives of the people.",
        r_ta="அரசியலமைப்பு முடிவெடுக்கும் அதிகாரம் மற்றும் வாக்குரிமையை மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளுக்கு மட்டுமே பாதுகாக்கிறது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). The proviso to Article 243R(2)(a) bars nominated members from voting so that unelected individuals cannot overturn the will of directly elected councillors.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். மக்களால் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளின் முடிவை நியமன உறுப்பினர்கள் மாற்றுவதைத் தடுக்கவே வாக்குரிமை மறுக்கப்பட்டுள்ளது.",
        why_eval={"B": "Democratic principle in R is the exact reason for the constitutional bar in A.", "B_ta": "R-ல் உள்ள மக்களாட்சி தத்துவமே A-ன் தடைக்கான நேரடி காரணமாகும்.", "C": "Reason is true.", "C_ta": "காரணம் சரியானது.", "D": "Assertion is true.", "D_ta": "உறுதிமொழி சரியானது."},
        tip_en="Article 243R: Nominated experts have advisory roles, not voting power.",
        tip_ta="உறுப்பு 243R: நியமன வல்லுநர்களுக்கு ஆலோசனை பங்கு மட்டுமே உண்டு, வாக்குரிமை இல்லை.",
        fact_en="State legislatures determine the number of nominated members, usually capped between 2 and 5.",
        fact_ta="நியமன உறுப்பினர்களின் எண்ணிக்கையை மாநில சட்டமன்றங்கள் தீர்மானிக்கின்றன.",
        tags=["article_243r", "nominated_members", "reasoning"]
    ))

    # R04: Article 243S Wards Committees
    questions.append(make_ar_q(
        qid="MUN_R_004",
        subtopic="Article 243S Wards Committees",
        a_en="The constitution of Wards Committees is legally mandatory only in Municipalities having a population of three lakhs or more.",
        a_ta="3 லட்சம் அல்லது அதற்கு மேற்பட்ட மக்கள் தொகை கொண்ட நகராட்சிகளில் மட்டுமே வார்டு குழுக்கள் அமைப்பது சட்டப்பூர்வமாக கட்டாயமாகும்.",
        r_en="In smaller municipalities, territorial wards are already small enough to ensure direct citizen-councillor interaction.",
        r_ta="சிறிய நகராட்சிகளில் வார்டுகள் ஏற்கனவே சிறியதாக உள்ளதால், பொதுமக்கள் மற்றும் உறுப்பினர்களிடையே நேரடி தொடர்பு சாத்தியமாகிறது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains the rationale behind the population threshold of 3 lakhs under Article 243S.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். சிறிய நகராட்சிகளில் மக்கள் தொகை குறைவு என்பதால் பெரிய நகரங்களுக்கு மட்டுமே வார்டு குழுக்கள் கட்டாயமாக்கப்பட்டன.",
        why_eval={"B": "The administrative scale logic in R explains the 3 lakh cutoff in A.", "B_ta": "நிர்வாக அளவு தர்க்கமே 3 லட்சம் வரம்பிற்கான காரணமாகும்.", "C": "R is valid.", "C_ta": "R சரியானது.", "D": "A is valid.", "D_ta": "A சரியானது."},
        tip_en="Wards Committees bridge the distance between citizens and municipal leadership in large cities.",
        tip_ta="வார்டு குழுக்கள் பெருநகரங்களில் மக்களுக்கும் நகராட்சி தலைமைக்கும் இடையே உள்ள இடைவெளியைக் குறைக்கின்றன.",
        fact_en="Article 243S leaves the composition and territorial area of wards committees to state legislation.",
        fact_ta="வார்டு குழுக்களின் கட்டமைப்பு மற்றும் எல்லையை மாநில சட்டத்திற்கு அரசியலமைப்பு விட்டுள்ளது.",
        tags=["article_243s", "wards_committee", "reasoning"]
    ))

    # R05: Article 243T Women Reservation
    questions.append(make_ar_q(
        qid="MUN_R_005",
        subtopic="Article 243T Reservation",
        a_en="The 74th Constitutional Amendment has transformed urban grassroots political leadership by empowering women across India.",
        a_ta="74-வது அரசியலமைப்பு திருத்தச் சட்டம் இந்தியா முழுவதும் பெண்களுக்கு அதிகாரம் அளித்து நகர்ப்புற அடித்தட்டு அரசியல் தலைமையை மாற்றியமைத்துள்ளது.",
        r_en="Article 243T mandates reserving not less than one-third of all directly elected seats and chairperson offices for women.",
        r_ta="உறுப்பு 243T நேரடியாகத் தேர்ந்தெடுக்கப்படும் இடங்களில் மற்றும் தலைவர் பதவிகளில் மூன்றில் ஒரு பங்குக்கு குறையாமல் பெண்களுக்கு ஒதுக்க கட்டாயமாக்குகிறது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the correct constitutional explanation of (A). The affirmative constitutional guarantee under Article 243T brought lakhs of women into formal urban governance.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். உறுப்பு 243T-ன் கீழ் உள்ள இடஒதுக்கீடு உத்தரவாதம் லட்சக்கணக்கான பெண்களை நகர்ப்புற நிர்வாகத்திற்கு கொண்டு வந்துள்ளது.",
        why_eval={"B": "Mandatory reservation in R directly produced the transformation in A.", "B_ta": "R-ல் உள்ள கட்டாய இடஒதுக்கீடே A-ன் மாற்றத்தை உருவாக்கியது.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Constitutional minimum = 1/3; Several states like Tamil Nadu enacted 50% reservation.",
        tip_ta="அரசியலமைப்பு குறைந்தபட்ச வரம்பு = 1/3; தமிழ்நாடு உட்பட பல மாநிலங்கள் 50% இடஒதுக்கீடு செய்துள்ளன.",
        fact_en="Article 243T(2) also provides for reservation of seats for SCs and STs in proportion to their population.",
        fact_ta="உறுப்பு 243T(2) மக்கள் தொகை விகிதாச்சாரப்படி SC/ST பிரிவினருக்கு இடஒதுக்கீடு வழங்குகிறது.",
        tags=["article_243t", "women_empowerment", "reasoning"]
    ))

    # R06: Article 243U Reconstitution Elections
    questions.append(make_ar_q(
        qid="MUN_R_006",
        subtopic="Article 243U Dissolution",
        a_en="A Municipality reconstituted after premature dissolution continues in office only for the remainder of the original five-year period.",
        a_ta="காலத்திற்கு முன்பே கலைக்கப்பட்ட பின்னர் மீண்டும் அமைக்கப்படும் ஒரு நகராட்சி அதன் அசல் 5 ஆண்டு காலத்தின் எஞ்சிய காலத்திற்கு மட்டுமே செயல்படும்.",
        r_en="The Constitution seeks to maintain synchronized, predictable five-year electoral cycles for all local bodies across the State.",
        r_ta="மாநிலம் முழுவதிலும் உள்ள அனைத்து உள்ளாட்சி அமைப்புகளுக்கும் ஒத்திசைவான, கணிக்கக்கூடிய 5 ஆண்டு தேர்தல் சுழற்சியைப் பராமரிக்க அரசியலமைப்பு முயல்கிறது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains the rationale behind Article 243U(4). Staggered tenures would disrupt state-wide local election schedules and State Finance Commission synchronization.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். மாநிலம் தழுவிய தேர்தல் அட்டவணை மற்றும் நிதி ஆணையத்தின் பணிகளை ஒத்திசைக்கவே எஞ்சிய கால விதி வைக்கப்பட்டுள்ளது.",
        why_eval={"B": "Synchronized cycle in R is the exact reason for the remainder rule in A.", "B_ta": "ஒத்திசைவான சுழற்சியே எஞ்சிய கால விதிக்குக் காரணமாகும்.", "C": "R is valid.", "C_ta": "R சரியானது.", "D": "A is valid.", "D_ta": "A சரியானது."},
        tip_en="Same remainder rule applies to Lok Sabha dissolution (under specific circumstances) and Panchayats (Art 243E).",
        tip_ta="இதே எஞ்சிய கால விதி பஞ்சாயத்துகளுக்கும் (உறுப்பு 243E) பொருந்தும்.",
        fact_en="If the remaining period is less than six months, no mid-term reconstitution election is required.",
        fact_ta="எஞ்சிய காலம் 6 மாதங்களுக்கும் குறைவாக இருந்தால், இடைக்காலத் தேர்தல் நடத்த தேவையில்லை.",
        tags=["article_243u", "remainder_tenure", "reasoning"]
    ))

    # R07: Article 243V Disqualification Age
    questions.append(make_ar_q(
        qid="MUN_R_007",
        subtopic="Article 243V Qualification Age",
        a_en="A 22-year-old citizen of India is eligible to contest municipal council elections.",
        a_ta="22 வயதுடைய ஒரு இந்திய குடிமகன் நகர்மன்றத் தேர்தலில் போட்டியிட தகுதியுடையவர் ஆவார்.",
        r_en="Under Article 243V(1)(b), no person is disqualified for municipal elections on grounds of age if he has attained the age of 21 years.",
        r_ta="உறுப்பு 243V(1)(b)-ன் கீழ், ஒருவர் 21 வயதை நிறைவு செய்திருந்தால், வயது அடிப்படையில் அவர் நகராட்சி தேர்தலில் தகுதிநீக்கம் செய்யப்பட மாட்டார்.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). While MLA/MP elections require a minimum age of 25, Article 243V specifically lowers the threshold to 21 years for local bodies.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். சட்டமன்றத்திற்கு 25 வயது தேவைப்பட்டாலும், உள்ளாட்சிக்கு உறுப்பு 243V 21 வயதாகக் குறைத்துள்ளது.",
        why_eval={"B": "R is the exact constitutional provision validating A.", "B_ta": "R என்பது A-வை உறுதிப்படுத்தும் துல்லியமான அரசியலமைப்பு விதியாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Age criteria: 18 to vote; 21 for local bodies; 25 for Assembly/Lok Sabha; 30 for Rajya Sabha.",
        tip_ta="வயது வரம்பு: வாக்களிக்க 18; உள்ளாட்சிக்கு 21; சட்டமன்றத்திற்கு 25; மேலவைக்கு 30.",
        fact_en="Other disqualifications follow the disqualification criteria applicable to State Legislative Assemblies.",
        fact_ta="பிற தகுதிநீக்கங்கள் மாநில சட்டமன்றத்திற்கான விதிகளைப் பின்பற்றுகின்றன.",
        tags=["article_243v", "age_qualification", "reasoning"]
    ))

    # R08: Article 243W Twelfth Schedule Discretionary
    questions.append(make_mun_q(
        qid="MUN_R_008",
        diff="Hard",
        qtype="Assertion and Reasoning",
        subtopic="Article 243W Devolution",
        en_stem="Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The devolution of all 18 functional matters listed in the Twelfth Schedule is not automatically uniform across all Indian States.\nReason (R): Article 243W uses the discretionary phrase 'the Legislature of a State may, by law, endow Municipalities with powers and responsibilities'.\nSelect the correct answer using the code below:",
        ta_stem="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று உறுதிமொழி (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): 12-வது அட்டவணையில் பட்டியலிடப்பட்டுள்ள 18 செயல்பாட்டுப் பணிகளும் இந்தியாவின் அனைத்து மாநிலங்களிலும் ஒரே சீராக வழங்கப்படவில்லை.\nகாரணம் (R): உறுப்பு 243W 'மாநில சட்டமன்றம் சட்டத்தின் மூலம் நகராட்சிகளுக்கு அதிகாரங்களையும் பொறுப்புகளையும் வழங்கலாம்' என்ற விருப்ப அதிகாரச் சொல்லைப் பயன்படுத்துகிறது.\nகீழ்க்கண்ட குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a=opt_a_en, ta_a=opt_a_ta, en_b=opt_b_en, ta_b=opt_b_ta, en_c=opt_c_en, ta_c=opt_c_ta, en_d=opt_d_en, ta_d=opt_d_ta,
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the correct explanation of (A). Because Article 243W uses 'may' rather than 'shall', the scope and extent of functional devolution varies widely depending on individual state political will.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். உறுப்பு 243W கட்டாயப்படுத்தாமல் மாநில சட்டமன்றத்தின் விருப்பத்திற்கு விட்டுள்ளதால் மாநிலங்களுக்கு இடையே பணிகள் மாறுபடுகின்றன.",
        why_a_en="Option A is correct: Discretionary wording in R explains varying devolution in A.",
        why_a_ta="விருப்பம் A சரியானது: R-ல் உள்ள விருப்ப உரிமை சொல்லே A-ன் வேறுபாட்டை விளக்குகிறது.",
        why_b_en="Option B is incorrect because R provides the legal reason.",
        why_b_ta="காரணம் சட்டப்பூர்வ காரணத்தை விளக்குவதால் B தவறானது.",
        why_c_en="Option C is incorrect because R is true.",
        why_c_ta="R உண்மையானது என்பதால் C தவறானது.",
        why_d_en="Option D is incorrect because A is true.",
        why_d_ta="A உண்மையானது என்பதால் D தவறானது.",
        tip_en="Look for 'may' vs 'shall' in constitutional articles: 243W uses 'may' for devolution.",
        tip_ta="அரசியலமைப்பு உறுப்புகளில் 'வழங்கலாம்' (may) அல்லது 'வழங்க வேண்டும்' (shall) என்பதைக் கவனியுங்கள்.",
        fact_en="States like Kerala and Tamil Nadu have devolved more functions than several northern states.",
        fact_ta="கேரளா, தமிழ்நாடு போன்ற மாநிலங்கள் பிற மாநிலங்களை விட கூடுதல் பணிகளை மாற்றியுள்ளன.",
        tags=["article_243w", "devolution", "reasoning"]
    ))

    # R09: Article 243X Fiscal Independence
    questions.append(make_ar_q(
        qid="MUN_R_009",
        subtopic="Article 243X Taxation",
        a_en="Most Indian Municipalities suffer from acute financial distress and structural fiscal dependency on higher levels of government.",
        a_ta="பெரும்பாலான இந்திய நகராட்சிகள் கடுமையான நிதி நெருக்கடியிலும், மேல்நிலை அரசுகளைச் சார்ந்திருக்கும் நிதி சார்பு நிலையிலும் உள்ளன.",
        r_en="Municipalities in India have virtually unlimited autonomous constitutional powers to levy and collect income and corporate taxes.",
        r_ta="இந்தியாவில் உள்ள நகராட்சிகளுக்கு வருமான வரி மற்றும் நிறுவன வரிகளை விதிக்கவும் வசூலிக்கவும் வரம்பற்ற தன்னாட்சி அதிகாரங்கள் உள்ளன.",
        correct_key="C",
        exp_en="(A) is true but (R) is false. Income tax and corporate tax are exclusive Union taxes under the Union List (Entries 82 and 85). Municipalities can only levy taxes explicitly authorized by State Legislatures under Article 243X (like property tax, profession tax).",
        exp_ta="(A) சரி, ஆனால் (R) தவறு. வருமான வரி மற்றும் நிறுவன வரி மத்திய அரசின் அதிகார வரம்பிற்குட்பட்டவை (மத்தியப் பட்டியல்). நகராட்சிகளுக்கு இவற்றை விதிக்கும் அதிகாரம் கிடையாது.",
        why_eval={"A": "R is factually false.", "A_ta": "காரணம் முற்றிலும் தவறானது.", "B": "R is false.", "B_ta": "காரணம் தவறு.", "D": "A is a well-documented truth.", "D_ta": "A என்பது உண்மையான கூற்று."},
        tip_en="Municipalities CANNOT levy Union taxes like Income Tax or Corporate Tax.",
        tip_ta="நகராட்சிகள் வருமான வரி அல்லது நிறுவன வரி போன்ற மத்திய வரிகளை விதிக்க முடியாது.",
        fact_en="Property tax accounts for over 60% of total municipal own-source tax revenue in India.",
        fact_ta="இந்திய நகராட்சிகளின் சொந்த வரி வருவாயில் 60%க்கும் மேல் சொத்துவரி மூலம் கிடைக்கிறது.",
        tags=["article_243x", "municipal_finances", "reasoning"]
    ))

    # R10: Article 243Y State Finance Commission
    questions.append(make_ar_q(
        qid="MUN_R_010",
        subtopic="Article 243Y SFC",
        a_en="The State Finance Commission plays a pivotal role in strengthening the fiscal foundation of urban local bodies.",
        a_ta="மாநில நிதி ஆணையம் நகர்ப்புற உள்ளாட்சி அமைப்புகளின் நிதி அடித்தளத்தை வலுப்படுத்துவதில் முக்கிய பங்கு வகிக்கிறது.",
        r_en="The recommendations made by the State Finance Commission under Article 243Y are strictly legally binding on the State Government.",
        r_ta="உறுப்பு 243Y-ன் கீழ் மாநில நிதி ஆணையம் வழங்கும் பரிந்துரைகள் மாநில அரசை சட்டப்பூர்வமாகக் கட்டுப்படுத்தும்.",
        correct_key="C",
        exp_en="(A) is true but (R) is false. Like the Union Finance Commission, the recommendations of the State Finance Commission are advisory and recommendatory in nature, not legally binding, though state governments conventionally accept major devolution recommendations.",
        exp_ta="(A) சரி, ஆனால் (R) தவறு. மத்திய நிதி ஆணையத்தைப் போலவே மாநில நிதி ஆணையத்தின் பரிந்துரைகளும் ஆலோசனைத் தன்மையுடையவையே (Advisory), மாநில அரசைக் கட்டுப்படுத்தும் கட்டாய உத்தரவு அல்ல.",
        why_eval={"A": "R is false as SFC recommendations are recommendatory.", "A_ta": "SFC பரிந்துரைகள் ஆலோசனையே என்பதால் R தவறு.", "B": "R is false.", "B_ta": "R தவறானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Both Union Finance Commission (Art 280) and State Finance Commission (Art 243-I/243Y) are RECOMMENDATORY bodies.",
        tip_ta="மத்திய நிதி ஆணையம் மற்றும் மாநில நிதி ஆணையம் இரண்டுமே ஆலோசனை அமைப்புகளே ஆகும்.",
        fact_en="The Governor must table the SFC recommendations along with an Action Taken Report before the State Legislature.",
        fact_ta="ஆளுநர் பரிந்துரைகளை நடவடிக்கை குறிப்புடன் சட்டமன்றத்தில் வைக்க வேண்டும்.",
        tags=["article_243y", "sfc_nature", "reasoning"]
    ))

    # R11: Article 243ZA Independent Elections
    questions.append(make_ar_q(
        qid="MUN_R_011",
        subtopic="Article 243ZA State Election Commission",
        a_en="The State Election Commissioner is insulated from state executive interference and enjoys high constitutional security of tenure.",
        a_ta="மாநில தேர்தல் ஆணையர் மாநில நிர்வாகத்தின் தலையீட்டிலிருந்து பாதுகாக்கப்பட்டு, உயர் அரசியலமைப்புப் பதவிப் பாதுகாப்பைப் பெற்றுள்ளார்.",
        r_en="Under Article 243K(2) and Article 243ZA, the State Election Commissioner cannot be removed from office except in like manner and on like grounds as a Judge of a High Court.",
        r_ta="உறுப்பு 243K(2) மற்றும் 243ZA-ன் படி, உயர் நீதிமன்ற நீதிபதியை பதவிநீக்கம் செய்யும் முறை மற்றும் காரணங்களின்றி மாநில தேர்தல் ஆணையரை பதவிநீக்கம் செய்ய முடியாது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the exact constitutional mechanism providing the security of tenure mentioned in (A). The removal requires an address by Parliament under Article 124(4) / 217.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். உயர் நீதிமன்ற நீதிபதிக்கு இணையான பதவிநீக்கப் பாதுகாப்பு இருப்பதால் மாநில தேர்தல் ஆணையர் தன்னிச்சையாக செயல்பட முடிகிறது.",
        why_eval={"B": "High Court judge removal standard in R directly creates the insulation in A.", "B_ta": "R-ல் உள்ள நீதிபதிக்கு இணையான பாதுகாப்பே A-ன் தன்னாட்சிக்குக் காரணமாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="SEC removal = Same grounds and manner as a High Court Judge (Parliamentary impeachment).",
        tip_ta="மாநில தேர்தல் ஆணையர் நீக்கம் = உயர் நீதிமன்ற நீதிபதியைப் போன்ற முறை (நாடாளுமன்ற தீர்மானம்).",
        fact_en="Governor appoints the SEC, but the Governor CANNOT remove the SEC unilaterally.",
        fact_ta="ஆளுநர் மாநில தேர்தல் ஆணையரை நியமிக்கிறார், ஆனால் தன்னிச்சையாக நீக்க முடியாது.",
        tags=["article_243za", "sec_tenure", "reasoning"]
    ))

    # R12: Article 243ZD District Planning Committee
    questions.append(make_ar_q(
        qid="MUN_R_012",
        subtopic="Article 243ZD DPC Rationale",
        a_en="The District Planning Committee provides an institutional mechanism to integrate rural and urban development planning.",
        a_ta="மாவட்ட திட்டக் குழு ஊரக மற்றும் நகர்ப்புற வளர்ச்சித் திட்டமிடலை ஒருங்கிணைப்பதற்கான ஒரு நிறுவன வழிமுறையை வழங்குகிறது.",
        r_en="Rapid urbanization causes peri-urban spillover, shared water tables, and common transportation corridors requiring coordinated planning between Panchayats and Municipalities.",
        r_ta="விரைவான நகரமயமாக்கல் புறநகர் விரிவாக்கம், பகிரப்பட்ட நிலத்தடி நீர் மற்றும் பொதுவான போக்குவரத்து வழித்தடங்களை உருவாக்குவதால் ஊராட்சிகளுக்கும் நகராட்சிகளுக்கும் இடையே ஒருங்கிணைந்த திட்டமிடல் தேவைப்படுகிறது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains the practical necessity for the DPC under Article 243ZD. Isolating panchayat plans from municipal plans led to haphazard regional development.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். ஊரக-நகர்ப்புற இணைப்பும் பகிரப்பட்ட உள்கட்டமைப்பும் ஒருங்கிணைந்த திட்டக்குழுவை அவசியமாக்குகின்றன.",
        why_eval={"B": "Urban-rural continuum described in R explains why DPC was established in A.", "B_ta": "R-ல் கூறப்பட்டுள்ள புறநகர் சூழலே DPC உருவாக்கத்திற்கு நேரடி காரணமாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="DPC bridges the artificial divide between rural (Part IX) and urban (Part IXA) planning.",
        tip_ta="DPC ஊரக மற்றும் நகர்ப்புற திட்டமிடலுக்கு இடையிலான இடைவெளியை இணைக்கிறது.",
        fact_en="Article 243ZD mandates that not less than 4/5th of DPC members must be elected representatives.",
        fact_ta="உறுப்பு 243ZD-ன் படி DPC உறுப்பினர்களில் 4/5 பங்கு தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளாக இருக்க வேண்டும்.",
        tags=["article_243zd", "dpc_integration", "reasoning"]
    ))

    # R13: Article 243ZE Metropolitan Planning Committee
    questions.append(make_ar_q(
        qid="MUN_R_013",
        subtopic="Article 243ZE MPC",
        a_en="Metropolitan Planning Committees are constitutionally required for large urban agglomerations with a population of 10 lakhs or more.",
        a_ta="10 லட்சம் அல்லது அதற்கு மேற்பட்ட மக்கள் தொகையைக் கொண்ட பெரிய நகர்ப்புற ஒருங்கிணைப்புகளுக்கு பெருநகர திட்டக் குழுக்கள் அமைப்பது அரசியலமைப்பு ரீதியாக அவசியமாகும்.",
        r_en="Metropolises encompass multiple municipal councils, corporations, and peri-urban panchayats whose infrastructure requires unified regional planning.",
        r_ta="பெருநகரங்கள் பல நகராட்சிகள், மாநகராட்சிகள் மற்றும் புறநகர் ஊராட்சிகளை உள்ளடக்கியுள்ளதால் அவற்றின் உள்கட்டமைப்புக்கு ஒருங்கிணைந்த பிராந்திய திட்டமிடல் தேவைப்படுகிறது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains why Article 243ZE mandates MPCs for million-plus metropolitan areas.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். பல நகராட்சிகள் மற்றும் ஊராட்சிகளை உள்ளடக்கிய பெருநகரங்களுக்கு ஒருங்கிணைந்த திட்டமிடல் தேவைப்படுகிறது.",
        why_eval={"B": "Multi-jurisdictional complexity in R is the exact reason for MPC in A.", "B_ta": "பல அமைப்புகள் இருக்கும் சிக்கலே MPC உருவாவதற்கான காரணமாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Metropolitan Area = Population of 10 lakhs (1 million) or more under Article 243P(c).",
        tip_ta="பெருநகரப் பகுதி = உறுப்பு 243P(c)-ன் கீழ் 10 லட்சம் அல்லது அதற்கு மேற்பட்ட மக்கள் தொகை.",
        fact_en="Not less than two-thirds of MPC members must be elected by councillors and panchayat chairpersons.",
        fact_ta="MPC உறுப்பினர்களில் மூன்றில் இரண்டு பங்குக்கு குறையாமல் தேர்ந்தெடுக்கப்பட வேண்டும்.",
        tags=["article_243ze", "mpc_rationale", "reasoning"]
    ))

    # R14: Article 243ZG Judicial Bar
    questions.append(make_ar_q(
        qid="MUN_R_014",
        subtopic="Article 243ZG Bar of Courts",
        a_en="Courts cannot entertain a writ petition challenging the delimitation of wards once the municipal election process has officially commenced.",
        a_ta="நகராட்சி தேர்தல் நடைமுறை அதிகாரப்பூர்வமாகத் தொடங்கிய பிறகு வார்டுகள் மறுவரையறையை எதிர்த்து தாக்கல் செய்யப்படும் ரிட் மனுக்களை நீதிமன்றங்கள் விசாரிக்க முடியாது.",
        r_en="Article 243ZG expressly prohibits judicial interference in electoral matters relating to delimitation and allotment of seats.",
        r_ta="உறுப்பு 243ZG மறுவரையறை மற்றும் இடங்கள் ஒதுக்கீடு தொடர்பான தேர்தல் விவகாரங்களில் நீதிமன்றங்கள் தலையிடுவதைத் திட்டவட்டமாகத் தடை செய்கிறது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the constitutional bar established under Article 243ZG(a) preventing courts from stalling election schedules.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். தேர்தல் நடைமுறை முடங்குவதைத் தடுக்க உறுப்பு 243ZG நீதிமன்றங்களின் தலையீட்டிற்கு தடை விதிக்கிறது.",
        why_eval={"B": "Article 243ZG in R directly mandates the bar in A.", "B_ta": "R-ல் உள்ள உறுப்பு 243ZG நேரடியாக A-ன் தடையை ஏற்படுத்துகிறது.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Delimitation laws can only be challenged via election petition AFTER the election concludes.",
        tip_ta="தேர்தல் முடிந்த பின்னரே தேர்தல் மனு மூலமாக மட்டுமே மறுவரையறையைக் கேள்வி கேட்க முடியும்.",
        fact_en="This mirrors Article 329 for Parliament and Article 243-O for Panchayats.",
        fact_ta="இது நாடாளுமன்றத்திற்கான உறுப்பு 329 மற்றும் ஊராட்சிகளுக்கான உறுப்பு 243-O போன்றதாகும்.",
        tags=["article_243zg", "judicial_bar", "reasoning"]
    ))

    # R15: Municipal Commissioner vs Mayor
    questions.append(make_ar_q(
        qid="MUN_R_015",
        subtopic="Municipal Executive Separation",
        a_en="In the traditional Indian municipal corporation model, executive powers are separated from the political chairperson (Mayor) and vested in the Municipal Commissioner.",
        a_ta="பாரம்பரிய இந்திய மாநகராட்சி மாதிரியில், நிர்வாக அதிகாரங்கள் அரசியல் தலைவரிடமிருந்து (மேயர்) பிரிக்கப்பட்டு மாநகராட்சி ஆணையரிடம் ஒப்படைக்கப்பட்டுள்ளன.",
        r_en="This separation was introduced by Sir Pherozeshah Mehta in the Bombay Municipal Corporation Act, 1888 to ensure professional, non-partisan municipal execution.",
        r_ta="தொழில்முறை மற்றும் நடுநிலையான நகராட்சி நிர்வாகத்தை உறுதி செய்வதற்காக சர் பெரோஸ்ஷா மேத்தாவால் 1888 பம்பாய் மாநகராட்சி சட்டத்தில் இந்த அதிகாரப் பகிர்வு அறிமுகப்படுத்தப்பட்டது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains the historical origin and rationale of the commissioner system in India.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். பெரோஸ்ஷா மேத்தா 1888 பம்பாய் சட்டத்தில் அறிமுகப்படுத்திய மாதிரியே இன்றும் இந்தியாவில் பின்பற்றப்படுகிறது.",
        why_eval={"B": "Historical legacy in R explains the institutional structure in A.", "B_ta": "R-ல் உள்ள வரலாற்று அமைப்பே A-ன் கட்டமைப்புக்குக் காரணமாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Pherozeshah Mehta Model: Mayor = Deliberative head; Commissioner = Executive head.",
        tip_ta="பெரோஸ்ஷா மேத்தா மாதிரி: மேயர் = மன்றத் தலைவர்; ஆணையர் = நிர்வாகத் தலைவர்.",
        fact_en="Municipal Commissioners are IAS officers appointed directly by the State Government.",
        fact_ta="மாநகராட்சி ஆணையர்கள் மாநில அரசால் நேரடியாக நியமிக்கப்படும் ஐ.ஏ.எஸ் அதிகாரிகள்.",
        tags=["commissioner_model", "pherozeshah_mehta", "reasoning"]
    ))

    # R16: Mayor-in-Council System
    questions.append(make_ar_q(
        qid="MUN_R_016",
        subtopic="Mayor-in-Council Model",
        a_en="The 'Mayor-in-Council' system adopted in West Bengal concentrates executive authority in the political executive rather than the bureaucrat.",
        a_ta="மேற்கு வங்காளத்தில் பின்பற்றப்படும் 'மேயர்-இன்-கவுன்சில்' முறை நிர்வாக அதிகாரத்தை அதிகாரியிடம் அல்லாமல் அரசியல் தலைமையிடம் வழங்குகிறது.",
        r_en="The Mayor-in-Council functions like a city cabinet where the Mayor acts like a Prime Minister assisted by elected member-councillors.",
        r_ta="மேயர்-இன்-கவுன்சில் முறை ஒரு நகர அமைச்சரவை போல செயல்படுகிறது, இதில் மேயர் ஒரு பிரதமர் போலவும் உறுப்பினர்கள் அமைச்சர்கள் போலவும் செயல்படுகின்றனர்.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains the cabinet-style functioning of the Mayor-in-Council system introduced in Kolkata in 1984.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். கொல்கத்தாவில் 1984-ல் தொடங்கப்பட்ட அமைச்சரவை போன்ற மேயர்-இன்-கவுன்சில் முறையில் மேயருக்கே முழு நிர்வாக அதிகாரம் உள்ளது.",
        why_eval={"B": "Cabinet comparison in R explains why political executive holds authority in A.", "B_ta": "அமைச்சரவை ஒப்பீடே அரசியல் தலைமையின் அதிகாரத்தை விளக்குகிறது.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Mayor-in-Council = Cabinet system for cities; Commissioner System = Council-Manager system.",
        tip_ta="மேயர்-இன்-கவுன்சில் = நகரங்களுக்கான அமைச்சரவை முறை; ஆணையர் முறை = நிர்வாக அதிகாரி முறை.",
        fact_en="Kamal Basu was the first Mayor under the Mayor-in-Council system in Kolkata in 1985.",
        fact_ta="1985-ல் கொல்கத்தாவில் இம்முறையின் கீழ் கமல் பாசு முதல் மேயரானார்.",
        tags=["mayor_in_council", "urban_models", "reasoning"]
    ))

    # R17: Cantonment Board Defence Control
    questions.append(make_ar_q(
        qid="MUN_R_017",
        subtopic="Cantonment Boards Rationale",
        a_en="Cantonment Boards are the only urban local bodies in India governed directly by Union law rather than State legislation.",
        a_ta="இந்தியாவில் மாநில சட்டங்களால் அல்லாமல் நேரடியாக மத்திய சட்டத்தால் நிர்வகிக்கப்படும் ஒரே நகர்ப்புற உள்ளாட்சி அமைப்பு பாசறை வாரியங்கள் ஆகும்.",
        r_en="Cantonment areas house sensitive military installations and defense personnel alongside civilian populations requiring national security oversight.",
        r_ta="பாசறை பகுதிகளில் இராணுவ நிலைகளும் பாதுகாப்புப் படையினரும் பொதுமக்களுடன் இணைந்து வசிப்பதால் தேசிய பாதுகாப்பு மேற்பார்வை அவசியமாகிறது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains why Entry 3 of the Union List places cantonments under Central jurisdiction (Cantonments Act, 2006).",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். இராணுவப் பாதுகாப்பு கருதி மத்தியப் பட்டியல் பதிவு 3 பாசறைகளை மத்திய அரசின் அதிகார வரம்பில் வைத்துள்ளது.",
        why_eval={"B": "National security in R is the direct reason for Central administration in A.", "B_ta": "தேசிய பாதுகாப்பே மத்திய நிர்வாகத்திற்கு நேரடி காரணமாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Union List Entry 3 = Delimitation and administration of Cantonment areas.",
        tip_ta="மத்தியப் பட்டியல் பதிவு 3 = பாசறை பகுதிகளின் நிர்வாகம் மற்றும் அதிகார வரம்பு.",
        fact_en="There are 62 Cantonment Boards in India (e.g. St. Thomas Mount and Wellington in Tamil Nadu).",
        fact_ta="இந்தியாவில் 62 பாசறை வாரியங்கள் உள்ளன (தமிழ்நாட்டில் பரங்கிமலை மற்றும் வெலிங்டன்).",
        tags=["cantonment_boards", "defence_ministry", "reasoning"]
    ))

    # R18: Special Purpose Agencies Pitfalls
    questions.append(make_ar_q(
        qid="MUN_R_018",
        subtopic="Special Purpose Agencies",
        a_en="The proliferation of Special Purpose Agencies (like Water Supply Boards and Development Authorities) has eroded the authority of elected Municipal Corporations.",
        a_ta="தனி நோக்க முகமைகள் (குடிநீர் வாரியங்கள் மற்றும் நகர் வளர்ச்சி குழுமங்கள் போன்றவை) அதிகரித்திருப்பது தேர்ந்தெடுக்கப்பட்ட மாநகராட்சிகளின் அதிகாரத்தைக் குறைத்துள்ளது.",
        r_en="Special Purpose Agencies are functional, statutory parastatal bodies accountable to the State Government rather than to the local municipal council.",
        r_ta="தனி நோக்க முகமைகள் நகர்மன்றத்திற்கு அல்லாமல் மாநில அரசுக்குப் பொறுப்பான சட்டப்பூர்வ அமைப்புகளாக செயல்படுகின்றன.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains how functional parastatals bypass elected municipal councils, undermining local representative democracy.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். தனி நோக்க முகமைகள் மாநில அரசின் கீழ் இயங்குவதால் தேர்ந்தெடுக்கப்பட்ட நகர்மன்றங்கள் பலவீனமடைகின்றன.",
        why_eval={"B": "State accountability in R explains why municipal council power is diminished in A.", "B_ta": "மாநில அரசின் கட்டுப்பாடு நகர்மன்ற அதிகார இழப்பை விளக்குகிறது.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="2nd Administrative Reforms Commission recommended placing parastatals under Municipal Corporations.",
        tip_ta="2-வது நிர்வாக சீர்திருத்த ஆணையம் இம்முகமைகளை மாநகராட்சியின் கீழ் கொண்டுவரப் பரிந்துரைத்தது.",
        fact_en="Examples in Tamil Nadu include CMWSSB (Metro Water) and CMDA.",
        fact_ta="தமிழ்நாட்டில் சென்னை குடிநீர் வாரியம் மற்றும் சி.எம்.டி.ஏ ஆகியவை இதற்கு உதாரணங்களாகும்.",
        tags=["special_purpose_agencies", "parastatals", "reasoning"]
    ))

    # R19: Lord Ripon Resolution 1882 Magna Carta
    questions.append(make_ar_q(
        qid="MUN_R_019",
        subtopic="Lord Ripon Magna Carta",
        a_en="Lord Ripon's Resolution of 1882 is celebrated as the 'Magna Carta of Local Self-Government' in India.",
        a_ta="1882-ஆம் ஆண்டின் ரிப்பன் பிரபுவின் தீர்மானம் இந்தியாவில் 'உள்ளாட்சி சுயஅரசின் மகா சாசனம்' என்று போற்றப்படுகிறது.",
        r_en="Ripon's resolution advocated that local self-government institutions should be developed primarily as instruments of political and popular education rather than mere administrative efficiency.",
        r_ta="உள்ளாட்சி அமைப்புகள் வெறும் நிர்வாகத் திறனுக்காக மட்டுமின்றி, முதன்மையாக அரசியல் மற்றும் மக்கள் கல்விக்கான கருவிகளாக வளர்க்கப்பட வேண்டும் என்று ரிப்பன் வாதிட்டார்.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains why Ripon's philosophy earned the title of Magna Carta. Ripon explicitly prioritized democracy and civic training over bureaucratic efficiency.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். ரிப்பன் பிரபு உள்ளாட்சி அமைப்புகளை மக்களாட்சிப் பயிற்சியின் களமாகப் பார்த்ததே இத்தீர்மானம் போற்றப்படக் காரணமாகும்.",
        why_eval={"B": "Political education philosophy in R directly justifies the Magna Carta moniker in A.", "B_ta": "அரசியல் கல்வி தத்துவமே மகா சாசனம் என்ற பெயருக்கு நியாயமான விளக்கமாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Ripon quote: 'Local self-government is chiefly desirable not as a means of improvement in administration, but as an instrument of political education.'",
        tip_ta="ரிப்பனின் புகழ்பெற்ற கூற்று: உள்ளாட்சி என்பது நிர்வாக மேம்பாட்டை விட அரசியல் கல்விக்கான கருவியாகும்.",
        fact_en="Ripon recommended a large preponderance of non-official elected members in all local boards.",
        fact_ta="உள்ளாட்சி வாரியங்களில் தேர்ந்தெடுக்கப்பட்ட அதிகாரப்பூர்வமற்ற உறுப்பினர்களின் பெரும்பான்மையை ரிப்பன் பரிந்துரைத்தார்.",
        tags=["lord_ripon", "magna_carta", "reasoning"]
    ))

    # R20: Madras Corporation Charter 1687
    questions.append(make_ar_q(
        qid="MUN_R_020",
        subtopic="Madras Corporation Charter",
        a_en="The East India Company chartered the Madras Municipal Corporation in 1687 primarily to levy local taxes on residents.",
        a_ta="கிழக்கிந்திய கம்பெனி 1687-ல் மெட்ராஸ் மாநகராட்சியை அமைத்ததன் முதன்மை நோக்கம் உள்ளூர் மக்கள் மீது வரிகளை விதிப்பதே ஆகும்.",
        r_en="The Company Directors in London wanted the inhabitants of Madras to pay for their own civic maintenance, policing, and fortifications.",
        r_ta="லண்டனில் இருந்த கம்பெனி இயக்குநர்கள் மெட்ராஸ் மக்கள் தங்கள் சொந்த குடிமை பராமரிப்பு, காவல் மற்றும் கோட்டைக்கான செலவுகளை அவர்களே ஏற்க வேண்டும் என்று விரும்பினர்.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the historical explanation of (A). Josiah Child and the Court of Directors created the Corporation to relieve the Company from the cost of maintaining Fort St. George and Black Town.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். புனித ஜார்ஜ் கோட்டை மற்றும் நகரத்தின் பராமரிப்புச் செலவுகளை மக்களே ஏற்கும் வகையில் வரி வசூலிக்கவே மாநகராட்சி உருவாக்கப்பட்டது.",
        why_eval={"B": "Company financial strategy in R explains why the Corporation was created in A.", "B_ta": "கம்பெனியின் நிதிச் சுமையைக் குறைக்கும் உத்தியே A-ன் உருவாக்கத்திற்கு காரணமாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Madras Corporation was created by Royal Charter of King James II dated 30 December 1687.",
        tip_ta="இரண்டாம் ஜேம்ஸ் மன்னரின் 1687 டிசம்பர் 30 நாளிட்ட அரச சாசனத்தால் மெட்ராஸ் மாநகராட்சி உருவாக்கப்பட்டது.",
        fact_en="Residents strongly resisted the municipal house tax imposed by the new corporation.",
        fact_ta="புதிய மாநகராட்சி விதித்த வீட்டு வரியை மெட்ராஸ் மக்கள் கடுமையாக எதிர்த்தனர்.",
        tags=["madras_corporation", "1687_charter", "reasoning"]
    ))

    # R21: Property Tax Valuation Challenges
    questions.append(make_ar_q(
        qid="MUN_R_021",
        subtopic="Property Tax Reforms",
        a_en="Under-assessment and evasion of property taxes remain widespread chronic problems in Indian municipalities.",
        a_ta="சொத்துவரி குறைத்து மதிப்பிடப்படுதலும் வரி ஏய்ப்பும் இந்திய நகராட்சிகளில் தொடர் தீராத பிரச்சனைகளாக உள்ளன.",
        r_en="Most municipalities lack computerized records, updated geographic information systems (GIS), and modern property cadastre databases.",
        r_ta="பெரும்பாலான நகராட்சிகளில் கணினிமயமாக்கப்பட்ட பதிவுகள், புதுப்பிக்கப்பட்ட புவியியல் தகவல் அமைப்புகள் (GIS) மற்றும் நவீன சொத்துத் தரவுத்தளங்கள் இல்லை.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) correctly explains (A). Weak digital infrastructure and discretionary manual surveys lead to severe revenue loss in property taxation.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். டிஜிட்டல் உள்கட்டமைப்பு மற்றும் GIS குறைபாடுகளே சொத்துவரி ஏய்ப்பிற்கு முதன்மைக் காரணங்களாக உள்ளன.",
        why_eval={"B": "Lack of GIS in R explains under-assessment in A.", "B_ta": "GIS குறைபாடே குறைத்து மதிப்பிடப்படுவதை விளக்குகிறது.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Property Tax reforms: Shift from ARV to Unit Area Value (UAV) or Capital Value with GIS mapping.",
        tip_ta="சொத்துவரி சீர்திருத்தங்கள்: GIS வரைபடத்துடன் கூடிய அலகுப் பகுதி மதிப்பு அல்லது மூலதன மதிப்பு முறைக்கு மாறுதல்.",
        fact_en="Greater Chennai Corporation completed comprehensive drone-based GIS mapping in recent years.",
        fact_ta="சென்னை மாநகராட்சி சமீப ஆண்டுகளில் ட்ரோன் அடிப்படையிலான விரிவான GIS மேப்பிங்கை மேற்கொண்டது.",
        tags=["property_tax", "gis_mapping", "reasoning"]
    ))

    # R22: Part IXA Exclusion Article 243ZC
    questions.append(make_ar_q(
        qid="MUN_R_022",
        subtopic="Article 243ZC Exempted Areas",
        a_en="Part IXA of the Indian Constitution does not apply to the Scheduled Areas and Tribal Areas referred to in Article 244.",
        a_ta="இந்திய அரசியலமைப்பின் பகுதி IXA உறுப்பு 244-ல் குறிப்பிடப்பட்டுள்ள அட்டவணைப் பகுதிகள் மற்றும் பழங்குடியினர் பகுதிகளுக்குப் பொருந்தாது.",
        r_en="The constitutional intent is to preserve traditional indigenous customary practices and prevent alien municipal structures from destabilizing tribal autonomy.",
        r_ta="பாரம்பரிய பூர்வகுடி வழக்கங்களை பாதுகாப்பதும், பழங்குடியின தன்னாட்சியை நகராட்சி அமைப்புகள் சீர்குலைப்பதைத் தடுப்பதும் அரசியலமைப்பின் நோக்கமாகும்.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) explains the rationale behind Article 243ZC. Just as PESA 1996 was needed for Panchayats, urban tribal areas require specialized, sensitive governance models.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். பழங்குடியினரின் பாரம்பரிய மரபுகளைப் பாதுகாக்கவே உறுப்பு 243ZC பகுதி IXA-விலிருந்து அவர்களுக்கு விலக்களிக்கிறது.",
        why_eval={"B": "Indigenous autonomy rationale in R explains exemption in A.", "B_ta": "பழங்குடியின தன்னாட்சியே A-ன் விலக்கிற்கு காரணமாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Article 243M exempts Scheduled/Tribal areas for Panchayats; Article 243ZC exempts them for Municipalities.",
        tip_ta="பஞ்சாயத்துகளுக்கு உறுப்பு 243M விலக்களிக்கிறது; நகராட்சிகளுக்கு உறுப்பு 243ZC விலக்களிக்கிறது.",
        fact_en="Parliament may extend Part IXA to Scheduled Areas with modifications by law.",
        fact_ta="நாடாளுமன்றம் சட்டத்தின் மூலம் பகுதி IXA-வை மாற்றங்களுடன் இப்பகுதிகளுக்கு விரிவுபடுத்தலாம்.",
        tags=["article_243zc", "tribal_areas", "reasoning"]
    ))

    # R23: Direct vs Indirect Mayoral Election
    questions.append(make_ar_q(
        qid="MUN_R_023",
        subtopic="Mayoral Election Modes",
        a_en="In Tamil Nadu, the system of electing the Mayor has oscillated between direct election by citizens and indirect election by councillors.",
        a_ta="தமிழ்நாட்டில் மேயரைத் தேர்ந்தெடுக்கும் முறை மக்களால் நேரடித் தேர்தல் மற்றும் உறுப்பினர்களால் மறைமுகத் தேர்தல் என மாறி மாறி வந்துள்ளது.",
        r_en="Under Article 243R(2)(b), the Constitution leaves the manner of election of the Chairperson of a Municipality entirely to the discretion of the State Legislature.",
        r_ta="உறுப்பு 243R(2)(b)-ன் கீழ், நகராட்சித் தலைவரைத் தேர்ந்தெடுக்கும் முறையை அரசியலமைப்பு முழுமையாக மாநில சட்டமன்றத்தின் விருப்பத்திற்கே விட்டுள்ளது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the constitutional reason that allows Tamil Nadu (and other states) to alter the mode of mayoral elections via state legislative amendments (e.g. 1996 direct, 2006 indirect, 2011 direct, 2018/2022 indirect).",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். உறுப்பு 243R(2)(b) மாநிலங்களுக்கு அதிகாரம் அளித்துள்ளதாலேயே தமிழ்நாடு சட்டத் திருத்தங்கள் மூலம் முறையை மாற்ற முடிந்தது.",
        why_eval={"B": "State legislative discretion in R explains the shifting policy in A.", "B_ta": "மாநில சட்டமன்றத்தின் விருப்ப அதிகாரமே A-ன் கொள்கை மாற்றங்களை விளக்குகிறது.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Direct Mayors have citizen mandate; Indirect Mayors have working majority in council.",
        tip_ta="நேரடி மேயர் மக்கள் செல்வாக்கைப் பெறுகிறார்; மறைமுக மேயர் மன்றத்தில் பெரும்பான்மையைப் பெறுகிறார்.",
        fact_en="Mayors in Tamil Nadu are currently elected indirectly by councillors under the 2022 Act amendments.",
        fact_ta="2022 சட்டத் திருத்தத்தின்படி தற்போது தமிழ்நாட்டில் மேயர்கள் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகின்றனர்.",
        tags=["mayoral_election", "article_243r", "tamil_nadu", "reasoning"]
    ))

    # R24: Tamil Nadu 50% Reservation
    questions.append(make_ar_q(
        qid="MUN_R_024",
        subtopic="TN 50% Reservation",
        a_en="Tamil Nadu provides 50 percent reservation for women in all Municipal Corporations, Municipalities, and Town Panchayats.",
        a_ta="தமிழ்நாடு அனைத்து மாநகராட்சிகள், நகராட்சிகள் மற்றும் பேரூராட்சிகளில் பெண்களுக்கு 50 சதவீத இடஒதுக்கீட்டை வழங்குகிறது.",
        r_en="The Tamil Nadu Legislative Assembly enacted legislation in 2016 enhancing women's local body reservation from 33% to 50%.",
        r_ta="தமிழ்நாடு சட்டமன்றம் 2016-ல் உள்ளாட்சி அமைப்புகளில் பெண்களுக்கான இடஒதுக்கீட்டை 33%-லிருந்து 50%-ஆக உயர்த்தி சட்டம் இயற்றியது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the exact statutory basis for (A). While Article 243T sets a 33% floor, states are constitutionally competent to provide higher affirmative representation.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். 2016-ல் தமிழ்நாடு சட்டமன்றம் இயற்றிய சட்டமே 50% இடஒதுக்கீட்டை நடைமுறைப்படுத்தியது.",
        why_eval={"B": "2016 state law in R directly created the 50% reservation in A.", "B_ta": "2016 மாநில சட்டமே A-ன் 50% இடஒதுக்கீட்டை உருவாக்கியது.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Article 243T mandates AT LEAST 33%; States can legally raise it to 50%.",
        tip_ta="உறுப்பு 243T குறைந்தபட்சம் 33% என்கிறது; மாநிலங்கள் சட்டப்பூர்வமாக 50% வரை உயர்த்தலாம்.",
        fact_en="In the 2022 urban local body elections, over 50% of councillor seats and mayoral posts in TN were won by women.",
        fact_ta="2022 நகர்ப்புற உள்ளாட்சித் தேர்தலில் தமிழ்நாட்டில் 50%க்கும் அதிகமான இடங்களை பெண்கள் வென்றனர்.",
        tags=["tamil_nadu_50_percent", "women_reservation", "reasoning"]
    ))

    # R25: Transitional Period Article 243ZF
    questions.append(make_ar_q(
        qid="MUN_R_025",
        subtopic="Article 243ZF Transition",
        a_en="Pre-existing state municipal laws inconsistent with Part IXA were not struck down immediately upon the enactment of the 74th Amendment.",
        a_ta="74-வது திருத்தச் சட்டம் இயற்றப்பட்டவுடன், பகுதி IXA-விற்கு முரணாக இருந்த முந்தைய மாநில நகராட்சி சட்டங்கள் உடனடியாக ரத்து செய்யப்படவில்லை.",
        r_en="Article 243ZF granted states a one-year transitional grace period to amend or repeal their municipal laws to conform with the Constitution.",
        r_ta="உறுப்பு 243ZF மாநிலங்கள் தங்கள் நகராட்சி சட்டங்களை அரசியலமைப்புக்கு ஏற்ப திருத்த அல்லது ரத்து செய்ய ஒரு ஆண்டு கால அவகாசம் வழங்கியது.",
        correct_key="A",
        exp_en="Both (A) and (R) are true, and (R) is the correct constitutional explanation of (A). Article 243ZF allowed existing laws to remain in force until amended or until one year elapsed from June 1, 1993, preventing an administrative vacuum.",
        exp_ta="(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும். நிர்வாக முடக்கம் ஏற்படுவதைத் தவிர்க்க உறுப்பு 243ZF ஒரு ஆண்டு கால அவகாசத்தை மாநிலங்களுக்கு வழங்கியது.",
        why_eval={"B": "One-year transition rule in R explains why laws were not immediately invalidated in A.", "B_ta": "ஒரு ஆண்டு கால அவகாச விதியே உடனடி ரத்து செய்யப்படாததற்கு காரணமாகும்.", "C": "R is true.", "C_ta": "R சரியானது.", "D": "A is true.", "D_ta": "A சரியானது."},
        tip_en="Article 243ZF = Transitional 1-year window (June 1, 1993 to May 31, 1994).",
        tip_ta="உறுப்பு 243ZF = ஒரு ஆண்டு இடைக்கால அவகாசம் (1993 ஜூன் 1 முதல் 1994 மே 31 வரை).",
        fact_en="Tamil Nadu passed the Tamil Nadu Municipal Laws (Amendment) Act in 1994 within this window.",
        fact_ta="தமிழ்நாடு 1994-ல் இக்காலக்கெடுவுக்குள் நகராட்சி சட்டத் திருத்தத்தை நிறைவேற்றியது.",
        tags=["article_243zf", "transition_period", "reasoning"]
    ))

    return questions

def main():
    questions = get_reasoning_25()
    assert len(questions) == 25, f"Expected 25 questions, got {len(questions)}"
    
    # Balance keys across A, B, C, D
    balanced = balance_question_keys(questions)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "municipalities_reasoning.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
        
    print(f"[SUCCESS] Wrote {len(balanced)} Reasoning MCQs to {out_file}")

if __name__ == "__main__":
    main()
