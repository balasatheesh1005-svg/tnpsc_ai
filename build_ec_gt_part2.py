"""
Part 2 of Grand Test generator for Election Commission (EC_GT_026 to EC_GT_050).
"""

from ec_mcq_helper import make_ec_q

def get_gt_part2():
    qs = []

    # GT 026
    qs.append(make_ec_q(
        qid="EC_GT_026", diff="Medium", qtype="Single-Choice", subtopic="Section 29B Contributions",
        en_stem="Under Section 29B of the Representation of the People Act, 1951, a political party is prohibited from accepting voluntary contributions from which of the following sources?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 29B-ன் கீழ், ஒரு அரசியல் கட்சி பின்வரும் எந்த மூலங்களிலிருந்து தன்னார்வ நன்கொடைகளைப் பெறுவதற்கு தடை செய்யப்பட்டுள்ளது?",
        en_a="Government companies and foreign sources defined under the Foreign Contribution (Regulation) Act", ta_a="அரசு நிறுவனங்கள் மற்றும் வெளிநாட்டுப் பங்களிப்பு (ஒழுங்குமுறை) சட்டத்தின் கீழ் உள்ள வெளிநாட்டு மூலங்கள்",
        en_b="Indian private limited companies registered under the Companies Act", ta_b="நிறுவனங்கள் சட்டத்தின் கீழ் பதிவு செய்யப்பட்ட இந்திய தனியார் வரையறுக்கப்பட்ட நிறுவனங்கள்",
        en_c="Individual citizens of India residing within India", ta_c="இந்தியாவிற்குள் வசிக்கும் தனிப்பட்ட இந்திய குடிமக்கள்",
        en_d="Non-Resident Indians holding valid Indian passports", ta_d="செல்லுபடியாகும் இந்திய கடவுச்சீட்டு வைத்துள்ள வெளிநாடு வாழ் இந்தியர்கள்",
        correct_key="A",
        exp_en="Section 29B permits political parties to accept voluntary contributions from any person or company other than a government company and any foreign source as defined under Section 2(1)(j) of FCRA.",
        exp_ta="பிரிவு 29B, அரசு நிறுவனங்கள் மற்றும் FCRA சட்டத்தின் பிரிவு 2(1)(j)-ன் கீழ் வரையறுக்கப்பட்ட வெளிநாட்டு மூலங்களைத் தவிர, பிற தனிநபர்கள் மற்றும் நிறுவனங்களிடமிருந்து நன்கொடைகளைப் பெற கட்சிகளை அனுமதிக்கிறது.",
        why_a_en="Correct. Government companies and foreign sources are strictly barred under Section 29B.",
        why_a_ta="சரியானது. அரசு நிறுவனங்கள் மற்றும் வெளிநாட்டு நிதி பிரிவு 29B-ன் கீழ் தடை செய்யப்பட்டுள்ளன.",
        why_b_en="Incorrect. Private companies can contribute under Section 182 of the Companies Act.",
        why_b_ta="தவறானது. தனியார் நிறுவனங்கள் நன்கொடை அளிக்கலாம்.",
        why_c_en="Incorrect. Indian citizens can freely contribute.",
        why_c_ta="தவறானது. இந்திய குடிமக்கள் நன்கொடை அளிக்கலாம்.",
        why_d_en="Incorrect. NRIs holding Indian passports are citizens and may contribute.",
        why_d_ta="தவறானது. இந்திய பாஸ்போர்ட் உள்ள NRI-கள் நன்கொடை அளிக்கலாம்.",
        tip_en="Acceptance of foreign contributions by political parties violates Section 3 of FCRA 2010.",
        tip_ta="வெளிநாட்டு நன்கொடைகளைப் பெறுவது FCRA 2010 சட்டத்தின் பிரிவு 3-ஐ மீறுவதாகும்.",
        fact_en="Section 29B was inserted into RPA 1951 by the Election and Other Related Laws (Amendment) Act, 2003.",
        fact_ta="2003 தேர்தல் திருத்தச் சட்டம் மூலம் பிரிவு 29B மக்கள் பிரதிநிதித்துவச் சட்டத்தில் சேர்க்கப்பட்டது.",
        tags=["Section 29B", "Political Contributions", "FCRA Bar"]
    ))

    # GT 027
    qs.append(make_ec_q(
        qid="EC_GT_027", diff="Easy", qtype="Single-Choice", subtopic="Section 29C Threshold",
        en_stem="Under Section 29C of RPA 1951, political parties must prepare and submit an annual contribution report to the Election Commission for donations exceeding what financial threshold?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 29C-ன் கீழ், அரசியல் கட்சிகள் எந்த நிதி வரம்பிற்கு மேற்பட்ட நன்கொடைகளுக்கு ஆண்டு பங்களிப்பு அறிக்கையை தயாரித்து தேர்தல் ஆணையத்திடம் சமர்ப்பிக்க வேண்டும்?",
        en_a="Exceeding Rs. 20,000", ta_a="ரூ. 20,000-க்கு மேற்பட்ட நன்கொடைகள்",
        en_b="Exceeding Rs. 50,000", ta_b="ரூ. 50,000-க்கு மேற்பட்ட நன்கொடைகள்",
        en_c="Exceeding Rs. 10,000", ta_c="ரூ. 10,000-க்கு மேற்பட்ட நன்கொடைகள்",
        en_d="Exceeding Rs. 1,00,000", ta_d="ரூ. 1,00,000-க்கு மேற்பட்ட நன்கொடைகள்",
        correct_key="A",
        exp_en="Section 29C mandates that the treasurer of every political party must submit a report to the ECI declaring all individual/corporate donations in excess of Rs. 20,000 in each financial year.",
        exp_ta="பிரிவு 29C-ன் படி, ஒவ்வொரு நிதியாண்டிலும் ரூ. 20,000-க்கு அதிகமாகப் பெறப்பட்ட அனைத்து நன்கொடைகளையும் கட்சிகளின் பொருளாளர் அறிக்கை தயாரித்து தேர்தல் ஆணையத்திடம் சமர்ப்பிக்க வேண்டும்.",
        why_a_en="Correct. Donations exceeding Rs. 20,000 must be reported.",
        why_a_ta="சரியானது. ரூ. 20,000-க்கு மேற்பட்ட நன்கொடைகள் தெரிவிக்கப்பட வேண்டும்.",
        why_b_en="Incorrect. Rs. 50,000 is not the Section 29C threshold.",
        why_b_ta="தவறானது. ரூ. 50,000 என்பது தவறான வரம்பு.",
        why_c_en="Incorrect. Rs. 10,000 is not the reporting limit.",
        why_c_ta="தவறானது. ரூ. 10,000 அல்ல.",
        why_d_en="Incorrect. Rs. 1,00,000 is incorrect.",
        why_d_ta="தவறானது. ரூ. 1,00,000 தவறானது.",
        tip_en="Failure to submit the Section 29C report on time disqualifies the party from claiming 100% tax exemption under Section 13A of the Income Tax Act!",
        tip_ta="பிரிவு 29C அறிக்கையை சமர்ப்பிக்கத் தவறினால் வருமான வரிச் சட்டத்தின் பிரிவு 13A-ன் கீழ் 100% வரிவிலக்கை கட்சி இழக்க நேரிடும்!",
        fact_en="ECI publishes these contribution reports on its official website for public scrutiny.",
        fact_ta="பொதுமக்களின் பார்வைக்காக தேர்தல் ஆணையம் இந்த நன்கொடை அறிக்கைகளை இணையதளத்தில் வெளியிடுகிறது.",
        tags=["Section 29C", "Donation Reporting", "Rs 20000 Threshold"]
    ))

    # GT 028
    qs.append(make_ec_q(
        qid="EC_GT_028", diff="Medium", qtype="Single-Choice", subtopic="Star Campaigners Expenditure",
        en_stem="Under Explanation 1 to Section 77(1) of RPA 1951, the travel expenses incurred by a 'Star Campaigner' are excluded from the election expenditure account of the candidate, provided that:",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 77(1)-ன் விளக்கம் 1-ன் கீழ், ஒரு 'நட்சத்திர பேச்சாளரின்' பயணச் செலவுகள் வேட்பாளரின் தேர்தல் செலவுக் கணக்கிலிருந்து விலக்களிக்கப்பட வேண்டுமானால் என்ன நிபந்தனை பூர்த்தியாக வேண்டும்?",
        en_a="The star campaigner confines their campaigning to general party propaganda without sharing the dais or specifically soliciting votes for that individual candidate alone", ta_a="நட்சத்திர பேச்சாளர் பொதுவான கட்சி பிரச்சாரத்தை மட்டுமே மேற்கொள்ள வேண்டும் மற்றும் தனிப்பட்ட வேட்பாளருடன் மேடையைப் பகிர்ந்து கொள்ளவோ அவருக்காக மட்டும் குறிப்பாக வாக்கு கேட்கவோ கூடாது",
        en_b="The star campaigner is an elected Member of Parliament from the same state", ta_b="நட்சத்திர பேச்சாளர் அதே மாநிலத்தைச் சேர்ந்த தேர்ந்தெடுக்கப்பட்ட பாராளுமன்ற உறுப்பினராக இருக்க வேண்டும்",
        en_c="The total travel cost does not exceed Rs. 50 lakhs", ta_c="மொத்த பயணச் செலவு ரூ. 50 லட்சத்திற்கு மிகாமல் இருக்க வேண்டும்",
        en_d="The star campaigner travels exclusively by state government transport", ta_d="நட்சத்திர பேச்சாளர் மாநில அரசு வாகனங்களில் மட்டுமே பயணிக்க வேண்டும்",
        correct_key="A",
        exp_en="Under Section 77(1) Explanations 1 & 2, travel expenses of leaders of a political party (star campaigners) are deemed party expenses, not candidate expenses. However, if the star campaigner shares the dais with the candidate or specifically campaigns for them, 50% or full proportion of travel expenses is debited to the candidate's account.",
        exp_ta="பிரிவு 77(1)-ன் படி, நட்சத்திர பேச்சாளர்களின் பயணச் செலவு கட்சியின் செலவாகக் கருதப்படும்; ஆனால் அவர்கள் வேட்பாளருடன் மேடையைப் பகிர்ந்தாலோ அல்லது அவருக்காக மட்டுமே பிரச்சாரம் செய்தாலோ அந்த செலவு வேட்பாளரின் கணக்கில் சேர்க்கப்படும்.",
        why_a_en="Correct. Must be general party propaganda to remain exempt from candidate's expenditure cap.",
        why_a_ta="சரியானது. வேட்பாளரின் செலவு வரம்பில் சேராமல் இருக்க பொதுக் கட்சி பிரச்சாரமாக மட்டுமே இருக்க வேண்டும்.",
        why_b_en="Incorrect. Anyone nominated by the party can be a star campaigner.",
        why_b_ta="தவறானது. கட்சியால் நியமிக்கப்படும் எவரும் நட்சத்திர பேச்சாளராக இருக்கலாம்.",
        why_c_en="Incorrect. No monetary ceiling is fixed for party travel under Section 77.",
        why_c_ta="தவறானது. கட்சி பயணச் செலவுக்கு உச்ச வரம்பு இல்லை.",
        why_d_en="Incorrect. State transport cannot be used during campaigning under MCC.",
        why_d_ta="தவறானது. அரசு வாகனங்களை பிரச்சாரத்திற்கு பயன்படுத்த முடியாது.",
        tip_en="Recognized parties get 40 star campaigners; registered unrecognized parties get 20.",
        tip_ta="அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு 40; அங்கீகாரமற்ற கட்சிகளுக்கு 20 நட்சத்திர பேச்சாளர்கள் அனுமதிக்கப்படுவர்.",
        fact_en="The list of star campaigners must be submitted to the Chief Electoral Officer / ECI within 7 days of election notification.",
        fact_ta="தேர்தல் அறிவிப்பு வெளியான 7 நாட்களுக்குள் நட்சத்திர பேச்சாளர்கள் பட்டியலை ECI-விடம் அளிக்க வேண்டும்.",
        tags=["Section 77", "Star Campaigners", "Election Expenditure"]
    ))

    # GT 029
    qs.append(make_ec_q(
        qid="EC_GT_029", diff="Hard", qtype="Single-Choice", subtopic="Rule 49MA Test Vote",
        en_stem="Under Rule 49MA of the Conduct of Elections Rules, 1961, what procedure is initiated if an elector alleges that the paper slip generated by the VVPAT displayed a candidate or symbol different from the one they voted for?",
        ta_stem="1961 தேர்தல் நடத்தை விதிகளின் விதி 49MA-ன் கீழ், விவிபேட் (VVPAT) இயந்திரத்தில் அச்சிடப்பட்ட சீட்டு தான் வாக்களித்த வேட்பாளரை விட மாறுபட்ட சின்னத்தைக் காட்டியது என்று ஒரு வாக்காளர் கூறினால் என்ன நடைமுறை பின்பற்றப்படுகிறது?",
        en_a="The Presiding Officer takes a written declaration and permits a 'test vote' in the presence of polling agents", ta_a="வாக்குச்சாவடி தலைமை அலுவலர் எழுத்துப்பூர்வ உறுதிமொழியைப் பெற்றுக்கொண்டு, முகவர்கள் முன்னிலையில் ஒரு 'சோதனை வாக்கு' (test vote) செலுத்த அனுமதிக்கிறார்",
        en_b="The EVM is immediately sealed and an emergency repoll is ordered for the booth", ta_b="வாக்குப்பதிவு இயந்திரம் உடனடியாக சீல் வைக்கப்பட்டு வாக்குச்சாவடிக்கு மறுதேர்தல் அறிவிக்கப்படுகிறது",
        en_c="The elector's vote is immediately cancelled and deleted from the Control Unit memory", ta_c="வாக்காளரின் வாக்கு உடனடியாக ரத்து செய்யப்பட்டு கட்டுப்பாட்டு அலகிலிருந்து அழிக்கப்படுகிறது",
        en_d="The matter is summarily referred to the High Court by election petition", ta_d="இவ்விவகாரம் தேர்தல் மனு மூலம் உடனடியாக உயர் நீதிமன்றத்திற்கு அனுப்பப்படுகிறது",
        correct_key="A",
        exp_en="Under Rule 49MA, the Presiding Officer warns the elector about penalties for a false claim under Section 177 IPC, obtains a written declaration in Form prescribed, and allows the elector to cast a test vote in the presence of polling agents to verify the complaint.",
        exp_ta="விதி 49MA-ன் படி, தவறான புகாருக்கு IPC பிரிவு 177-ன் கீழ் தண்டனை உண்டு என எச்சரித்து, எழுத்துப்பூர்வ அறிவிப்பைப் பெற்ற பின், முகவர்கள் முன்னிலையில் மாதிரி சோதனை வாக்கு செலுத்த தலைமை அலுவலர் அனுமதிக்கிறார்.",
        why_a_en="Correct. Written declaration and test vote under Rule 49MA.",
        why_a_ta="சரியானது. விதி 49MA-ன் கீழ் எழுத்துப்பூர்வ அறிவிப்பு மற்றும் சோதனை வாக்கு.",
        why_b_en="Incorrect. Machine is not sealed unless test vote proves the complaint true.",
        why_b_ta="தவறானது. புகார் நிரூபிக்கப்பட்டால் மட்டுமே இயந்திரம் மாற்றப்படும்.",
        why_c_en="Incorrect. Cast votes cannot be selectively deleted from EVM.",
        why_c_ta="தவறானது. பதிவான வாக்குகளை நீக்க முடியாது.",
        why_d_en="Incorrect. Handled on the spot by Presiding Officer.",
        why_d_ta="தவறானது. வாக்குச்சாவடி தலைமை அலுவலரே உடனடி நடவடிக்கை எடுப்பார்.",
        tip_en="If the test vote proves the allegation true, the Presiding Officer immediately stops poll and reports to the Returning Officer.",
        tip_ta="புகார் உண்மையாக இருந்தால் வாக்குப்பதிவு உடனடியாக நிறுத்தப்பட்டு RO-வுக்கு தெரிவிக்கப்படும்.",
        fact_en="If the test vote proves the allegation FALSE, the elector can be prosecuted under Section 177 IPC (up to 6 months imprisonment or fine).",
        fact_ta="புகார் தவறானது எனத் தெரிந்தால் வாக்காளர் மீது IPC பிரிவு 177-ன் கீழ் 6 மாத சிறை தண்டனை விதிக்கப்படலாம்.",
        tags=["Rule 49MA", "Test Vote", "VVPAT Verification"]
    ))

    # GT 030
    qs.append(make_ec_q(
        qid="EC_GT_030", diff="Medium", qtype="Single-Choice", subtopic="Form 17A Register of Voters",
        en_stem="In the polling station sequence under Rule 49L of the Conduct of Elections Rules, what is the statutory purpose of 'Form 17A'?",
        ta_stem="1961 தேர்தல் நடத்தை விதிகளின் விதி 49L-ன் கீழ், வாக்குச்சாவடியில் 'படிவம் 17A'-ன் சட்டப்பூர்வ நோக்கம் என்ன?",
        en_a="Register of Voters in which the elector's serial number is recorded and signature or thumb impression obtained before voting", ta_a="வாக்காளர் வரிசை எண் பதிவு செய்யப்பட்டு, வாக்களிப்பதற்கு முன் கையொப்பம் அல்லது கைரேகை பெறப்படும் வாக்காளர் பதிவேடு (Register of Voters)",
        en_b="Certificate issued to polling agents authorizing their entry into counting centers", ta_b="வாக்கு எண்ணிக்கை மையங்களுக்குள் நுழைய முகவர்களுக்கு வழங்கப்படும் அனுமதிச் சான்றிதழ்",
        en_c="Sealing slip pasted on the outer cover of the Ballot Unit", ta_c="வாக்குப்பதிவு அலகின் வெளி அட்டையில் ஒட்டப்படும் சீலிடும் காகிதத் துண்டு",
        en_d="List of tendered votes cast by impersonated voters", ta_d="ஆள்மாறாட்ட வாக்காளர்களால் செலுத்தப்பட்ட tendered வாக்குகளின் பட்டியல்",
        correct_key="A",
        exp_en="Form 17A is the official 'Register of Voters' maintained by the Second Polling Officer, recording the elector's roll number and signature/thumb impression before they proceed to the voting compartment.",
        exp_ta="படிவம் 17A என்பது இரண்டாவது வாக்குச்சாவடி அலுவலரால் பராமரிக்கப்படும் அதிகாரப்பூர்வ 'வாக்காளர் பதிவேடு' ஆகும்; இதில் வாக்காளர் வரிசை எண் மற்றும் கையொப்பம்/கைரேகை பதிவு செய்யப்படுகிறது.",
        why_a_en="Correct. Form 17A is the statutory Register of Voters.",
        why_a_ta="சரியானது. படிவம் 17A என்பது வாக்காளர் பதிவேடு ஆகும்.",
        why_b_en="Incorrect. Polling agent entry is governed by Form 10.",
        why_b_ta="தவறானது. முகவர் அனுமதி படிவம் 10-ல் உள்ளது.",
        why_c_en="Incorrect. That is the green paper seal / special tag.",
        why_c_ta="தவறானது. அது பச்சை காகித முத்திரை ஆகும்.",
        why_d_en="Incorrect. Tendered votes are recorded in Form 17B.",
        why_d_ta="தவறானது. Tendered வாக்குகள் படிவம் 17B-ல் பதிவு செய்யப்படுகின்றன.",
        tip_en="Total votes recorded on Control Unit (Form 17C) must mathematically match the number of voters signed in Form 17A.",
        tip_ta="கட்டுப்பாட்டு அலகில் பதிவான வாக்குகளும் (படிவம் 17C), படிவம் 17A-ல் கையொப்பமிட்ட வாக்காளர்களின் எண்ணிக்கையும் சரியாக பொருந்த வேண்டும்.",
        fact_en="If a voter signs Form 17A but subsequently refuses to vote, a remark 'Refused to Vote' is entered under Rule 49O.",
        fact_ta="படிவம் 17A-ல் கையொப்பமிட்ட பின் வாக்களிக்க மறுத்தால் விதி 49O-ன் கீழ் 'வாக்களிக்க மறுத்துவிட்டார்' என குறிக்கப்படும்.",
        tags=["Form 17A", "Register of Voters", "Rule 49L"]
    ))

    # GT 031 to GT 050
    # GT 031
    qs.append(make_ec_q(
        qid="EC_GT_031", diff="Easy", qtype="Single-Choice", subtopic="Indelible Ink Application",
        en_stem="Under Rule 49K of the Conduct of Elections Rules, 1961, on which part of the body is indelible ink applied to prevent duplicate voting?",
        ta_stem="1961 தேர்தல் நடத்தை விதிகளின் விதி 49K-ன் கீழ், இரட்டை வாக்களிப்பைத் தடுக்க அழியாத மை உடலின் எந்தப் பகுதியில் வைக்கப்படுகிறது?",
        en_a="Left hand forefinger across the skin and nail", ta_a="இடது கையின் ஆள்காட்டி விரலில் தோல் மற்றும் நகத்தின் மீது",
        en_b="Right hand thumb impression on paper seal", ta_b="வலது கை பெருவிரல்",
        en_c="Right hand forefinger tip only", ta_c="வலது கை ஆள்காட்டி விரல் நுனி மட்டும்",
        en_d="Left hand palm center", ta_d="இடது கையின் உள்ளங்கை மையம்",
        correct_key="A",
        exp_en="Rule 49K mandates that indelible ink is applied with a glass rod/marker on the elector's left-hand forefinger from the root of the nail to the skin crease.",
        exp_ta="விதி 49K-ன் படி, வாக்காளரின் இடது கை ஆள்காட்டி விரலில் நகத்தின் அடியிலிருந்து தோல் வரை அழியாத மை வைக்கப்பட வேண்டும்.",
        why_a_en="Correct. Left hand forefinger is the statutory position.",
        why_a_ta="சரியானது. இடது கை ஆள்காட்டி விரலே சட்டப்பூர்வ இடமாகும்.",
        why_b_en="Incorrect. Thumb is used only if forefinger is missing.",
        why_b_ta="தவறானது. ஆள்காட்டி விரல் இல்லாத போது மட்டுமே பெருவிரல் பயன்படும்.",
        why_c_en="Incorrect. Left hand is standard, not right hand.",
        why_c_ta="தவறானது. இடது கையே வழக்கமான நிலையாகும்.",
        why_d_en="Incorrect. Palm is not used.",
        why_d_ta="தவறானது. உள்ளங்கையில் மை வைக்கப்படுவதில்லை.",
        tip_en="If the left forefinger is missing, ink is applied to the second finger, and so forth, until the right hand.",
        tip_ta="இடது ஆள்காட்டி விரல் இல்லையெனில் அடுத்த விரலில் மை வைக்கப்படும்.",
        fact_en="Indelible ink containing silver nitrate is manufactured exclusively by Mysore Paints and Varnish Limited (MPVL) since 1962.",
        fact_ta="சில்வர் நைட்ரேட் கலந்த அழியாத மை 1962 முதல் மைசூர் பெயிண்ட்ஸ் நிறுவனத்தால் மட்டுமே தயாரிக்கப்படுகிறது.",
        tags=["Indelible Ink", "Rule 49K", "MPVL"]
    ))

    # GT 032
    qs.append(make_ec_q(
        qid="EC_GT_032", diff="Medium", qtype="Single-Choice", subtopic="Tendered Votes Rule 49P",
        en_stem="What is a 'Tendered Ballot Paper' under Rule 49P of the Conduct of Elections Rules, 1961?",
        ta_stem="1961 தேர்தல் நடத்தை விதிகளின் விதி 49P-ன் கீழ் 'Tendered வாக்குச் சீட்டு' என்பது என்ன?",
        en_a="A physical paper ballot issued to a genuine elector when another person has already cast a fraudulent vote in their name", ta_a="ஒரு வாக்காளரின் பெயரில் ஏற்கனவே வேறொருவர் போலி வாக்களித்திருக்கும் போது, உண்மையான வாக்காளருக்கு வழங்கப்படும் அச்சிடப்பட்ட காகித வாக்குச் சீட்டு",
        en_b="A ballot paper mailed by postal service to government servants on election duty", ta_b="தேர்தல் பணியில் உள்ள அரசு ஊழியர்களுக்கு அஞ்சல் மூலம் அனுப்பப்படும் வாக்குச் சீட்டு",
        en_c="A ballot paper submitted by candidates along with their security deposit", ta_c="வேட்பாளர்கள் தங்களின் பிணைத்தொகையுடன் சமர்ப்பிக்கும் வாக்குச் சீட்டு",
        en_d="A defective electronic ballot unit that fails during the poll", ta_d="வாக்குப்பதிவின் போது பழுதடையும் ஒரு மின்னணு வாக்குப்பதிவு அலகு",
        correct_key="A",
        exp_en="Under Rule 49P, if an elector arrives and finds that another person has already voted in their name, the Presiding Officer satisfies himself of the elector's identity, gives him a serial-numbered 'Tendered Ballot Paper' (marked by arrow cross mark), and places it in a separate sealed envelope (not inside the EVM).",
        exp_ta="விதி 49P-ன் கீழ், தன் பெயரில் வேறொருவர் வாக்களித்துவிட்டதை அறியும் உண்மையான வாக்காளரின் அடையாளத்தை உறுதி செய்து, அவருக்கு காகித வாக்குச் சீட்டு வழங்கப்பட்டு சீலிடப்பட்ட கவரில் வைக்கப்படும் (EVM-ல் அல்ல).",
        why_a_en="Correct. Tendered ballot paper under Rule 49P protects genuine voters against impersonation.",
        why_a_ta="சரியானது. ஆள்மாறாட்டத்திற்கு எதிராக உண்மையான வாக்காளருக்கு வழங்கப்படும் காகித வாக்கு.",
        why_b_en="Incorrect. That is a postal ballot.",
        why_b_ta="தவறானது. அது தபால் வாக்கு ஆகும்.",
        why_c_en="Incorrect. Deposit is financial, not a ballot.",
        why_c_ta="தவறானது. பிணைத்தொகை நிதி சார்ந்தது.",
        why_d_en="Incorrect. A defective machine is a replacement unit.",
        why_d_ta="தவறானது. அது மாற்று இயந்திரம் ஆகும்.",
        tip_en="Tendered votes are recorded in Form 17B and are counted only on High Court orders during election petitions.",
        tip_ta="Tendered வாக்குகள் படிவம் 17B-ல் பதிவு செய்யப்பட்டு, நீதிமன்ற உத்தரவின் பேரில் மட்டுமே எண்ணப்படும்.",
        fact_en="Tendered votes are never entered into the EVM Control Unit.",
        fact_ta="Tendered வாக்குகள் EVM கட்டுப்பாட்டு அலகில் ஒருபோதும் செலுத்தப்படுவதில்லை.",
        tags=["Rule 49P", "Tendered Ballot Paper", "Form 17B"]
    ))

    # GT 033
    qs.append(make_ec_q(
        qid="EC_GT_033", diff="Medium", qtype="Single-Choice", subtopic="Rule 36 Challenged Vote",
        en_stem="Under Rule 36 of the Conduct of Elections Rules, 1961, what fee must a polling agent deposit with the Presiding Officer to challenge the identity of an elector?",
        ta_stem="1961 தேர்தல் நடத்தை விதிகளின் விதி 36-ன் கீழ், ஒரு வாக்காளரின் அடையாளத்தை சவாலுக்கு உட்படுத்த (challenged vote) ஒரு வாக்குச்சாவடி முகவர் தலைமை அலுவலரிடம் செலுத்த வேண்டிய கட்டணம் என்ன?",
        en_a="Rs. 2 in cash", ta_a="ரூ. 2 ரொக்கம்",
        en_b="Rs. 100 in cash", ta_b="ரூ. 100 ரொக்கம்",
        en_c="Rs. 50 in cash", ta_c="ரூ. 50 ரொக்கம்",
        en_d="Rs. 500 in cash", ta_d="ரூ. 500 ரொக்கம்",
        correct_key="A",
        exp_en="Rule 36(1) provides that any polling agent challenging the identity of an elector must deposit a sum of Rs. 2 in cash with the Presiding Officer for each challenge. If the challenge is frivolous, the deposit is forfeited.",
        exp_ta="விதி 36(1)-ன் படி, ஒரு வாக்காளரின் அடையாளத்தை சவால் செய்யும் முகவர் ஒவ்வொரு சவாலுக்கும் ரூ. 2 ரொக்கமாக தலைமை அலுவலரிடம் செலுத்த வேண்டும். சவால் பொய்யானது எனில் கட்டணம் பறிமுதல் செய்யப்படும்.",
        why_a_en="Correct. Statutorily fixed at Rs. 2 under Rule 36.",
        why_a_ta="சரியானது. விதி 36-ன் கீழ் ரூ. 2 என நிர்ணயிக்கப்பட்டுள்ளது.",
        why_b_en="Incorrect. Rs. 100 is incorrect.",
        why_b_ta="தவறானது. ரூ. 100 தவறானது.",
        why_c_en="Incorrect. Rs. 50 is incorrect.",
        why_c_ta="தவறானது. ரூ. 50 தவறானது.",
        why_d_en="Incorrect. Rs. 500 is incorrect.",
        why_d_ta="தவறானது. ரூ. 500 தவறானது.",
        tip_en="Challenged votes are entered in Form 14 (List of Challenged Votes).",
        tip_ta="சவால் செய்யப்பட்ட வாக்குகள் படிவம் 14-ல் பதிவு செய்யப்படுகின்றன.",
        fact_en="If the challenge is established as true, the impersonator is handed over to the police under Section 171F IPC.",
        fact_ta="சவால் உண்மை எனத் தெரிந்தால் ஆள்மாறாட்டம் செய்த நபர் காவல்துறையிடம் ஒப்படைக்கப்படுவார்.",
        tags=["Challenged Vote", "Rule 36", "Form 14"]
    ))

    # GT 034
    qs.append(make_ec_q(
        qid="EC_GT_034", diff="Easy", qtype="Single-Choice", subtopic="Counting Precedence",
        en_stem="Under Rule 54A of the Conduct of Elections Rules, 1961, which category of votes must be counted first before opening the EVMs?",
        ta_stem="1961 தேர்தல் நடத்தை விதிகளின் விதி 54A-ன் கீழ், EVM-களைத் திறந்து எண்ணுவதற்கு முன் எந்த வகை வாக்குகள் முதலில் எண்ணப்பட வேண்டும்?",
        en_a="Postal ballot papers", ta_a="தபால் வாக்குச் சீட்டுகள் (Postal ballot papers)",
        en_b="VVPAT paper slips from all constituencies", ta_b="அனைத்து தொகுதிகளின் விவிபேட் சீட்டுகள்",
        en_c="Tendered votes recorded in Form 17B", ta_c="படிவம் 17B-ல் பதிவு செய்யப்பட்ட tendered வாக்குகள்",
        en_d="Test votes cast under Rule 49MA", ta_d="விதி 49MA-ன் கீழ் செலுத்தப்பட்ட சோதனை வாக்குகள்",
        correct_key="A",
        exp_en="Rule 54A mandates that the Returning Officer shall first deal with the postal ballot papers. Counting of votes in EVMs can commence 30 minutes after postal ballot counting begins.",
        exp_ta="விதி 54A-ன் படி, தேர்தல் நடத்தும் அதிகாரி முதலில் தபால் வாக்குகளையே எண்ணத் தொடங்க வேண்டும். தபால் வாக்கு எண்ணிக்கை தொடங்கிய 30 நிமிடங்களுக்குப் பிறகே EVM வாக்கு எண்ணிக்கை தொடங்கலாம்.",
        why_a_en="Correct. Postal ballots are counted first under Rule 54A.",
        why_a_ta="சரியானது. விதி 54A-ன் படி தபால் வாக்குகளே முதலில் எண்ணப்படுகின்றன.",
        why_b_en="Incorrect. VVPAT slips are counted at the very end.",
        why_b_ta="தவறானது. விவிபேட் சீட்டுகள் இறுதியிலேயே எண்ணப்படும்.",
        why_c_en="Incorrect. Tendered votes are not opened on counting day.",
        why_c_ta="தவறானது. Tendered வாக்குகள் எண்ணிக்கை நாளில் திறக்கப்படுவதில்லை.",
        why_d_en="Incorrect. Test votes are accounted during mock poll.",
        why_d_ta="தவறானது. சோதனை வாக்குகள் மாதிரி வாக்கெடுப்பில் சரிபார்க்கப்படுகின்றன.",
        tip_en="If the victory margin is less than total rejected postal ballots, all rejected postal ballots must be reverified before declaring the result.",
        tip_ta="வெற்றி வித்தியாசம் நிராகரிக்கப்பட்ட தபால் வாக்குகளை விட குறைவாக இருந்தால், அவற்றை மீண்டும் சரிபார்ப்பது கட்டாயமாகும்.",
        fact_en="Postal ballots include votes of service personnel received via ETPBS and senior citizens home voting.",
        fact_ta="தபால் வாக்குகளில் ராணுவ வீரர்களின் ETPBS வாக்குகள் மற்றும் முதியோரின் தபால் வாக்குகள் அடங்கும்.",
        tags=["Counting Rules", "Rule 54A", "Postal Ballot First"]
    ))

    # GT 035
    qs.append(make_ec_q(
        qid="EC_GT_035", diff="Medium", qtype="Single-Choice", subtopic="Section 65 Tie Breaker",
        en_stem="Under Section 65 of the Representation of the People Act, 1951, how is a tie resolved when two candidates receive an equal number of votes?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 65-ன் கீழ், இரண்டு வேட்பாளர்கள் சம எண்ணிக்கையிலான வாக்குகளைப் பெற்றால் சமநிலை எவ்வாறு தீர்க்கப்படுகிறது?",
        en_a="The Returning Officer decides by drawing of lots, and the candidate on whom the lot falls gets an additional vote", ta_a="தேர்தல் நடத்தும் அதிகாரி குலுக்கல் முறை (draw of lots) மூலம் தீர்மானிக்கிறார், அதில் பெயர் வரும் வேட்பாளர் ஒரு கூடுதல் வாக்கை பெற்றவராகக் கருதப்படுவார்",
        en_b="The candidate who belongs to the ruling party is declared elected", ta_b="ஆளும் கட்சியைச் சேர்ந்த வேட்பாளர் வெற்றி பெற்றவராக அறிவிக்கப்படுவார்",
        en_c="An automatic repoll is conducted across the entire constituency within 7 days", ta_c="7 நாட்களுக்குள் தொகுதி முழுவதும் தானாகவே மறுதேர்தல் நடத்தப்படும்",
        en_d="The Election Commission of India nominates the winner by majority resolution", ta_d="இந்திய தேர்தல் ஆணையம் பெரும்பான்மை தீர்மானம் மூலம் வெற்றியாளரை நியமிக்கும்",
        correct_key="A",
        exp_en="Section 65 explicitly provides that if an equality of votes is found to exist between candidates, the Returning Officer shall decide between them by lot and proceed as if the candidate on whom the lot falls had received an additional vote.",
        exp_ta="பிரிவு 65-ன் படி, சம வாக்குகள் ஏற்படும் போது தேர்தல் நடத்தும் அதிகாரி குலுக்கல் முறையில் முடிவெடுக்க வேண்டும்; குலுக்கலில் பெயர் வரும் வேட்பாளர் ஒரு கூடுதல் வாக்கை பெற்றதாகக் கருதப்பட்டு வெற்றி அறிவிக்கப்படும்.",
        why_a_en="Correct. Drawing of lots under Section 65.",
        why_a_ta="சரியானது. பிரிவு 65-ன் கீழ் குலுக்கல் முறை மூலம் தீர்மானிக்கப்படுகிறது.",
        why_b_en="Incorrect. Ruling party affiliation has no legal relevance.",
        why_b_ta="தவறானது. ஆளும் கட்சி அந்தஸ்திற்கு சட்ட அங்கீகாரம் இல்லை.",
        why_c_en="Incorrect. A tie does not cause an automatic repoll.",
        why_c_ta="தவறானது. மறுதேர்தல் நடத்தப்படுவதில்லை.",
        why_d_en="Incorrect. ECI does not nominate winners.",
        why_d_ta="தவறானது. தேர்தல் ஆணையம் வெற்றியாளரை நியமிக்க முடியாது.",
        tip_en="The lucky draw must be conducted publicly in the presence of candidates and counting agents.",
        tip_ta="வேட்பாளர்கள் மற்றும் முகவர்கள் முன்னிலையில் வெளிப்படையாக இக்குலுக்கல் நடத்தப்பட வேண்டும்.",
        fact_en="Section 65 applies to both Lok Sabha and Assembly elections.",
        fact_ta="பிரிவு 65 மக்களவை மற்றும் சட்டமன்றத் தேர்தல்கள் இரண்டிற்கும் பொருந்தும்.",
        tags=["Section 65", "Tie Breaker", "Draw of Lots"]
    ))

    # GT 036
    qs.append(make_ec_q(
        qid="EC_GT_036", diff="Easy", qtype="Single-Choice", subtopic="Declaration Form 21C",
        en_stem="Which statutory certificate of election is issued by the Returning Officer to the winning candidate under Rule 66 of the Conduct of Elections Rules, 1961?",
        ta_stem="1961 தேர்தல் நடத்தை விதிகளின் விதி 66-ன் கீழ், வெற்றி பெற்ற வேட்பாளருக்கு தேர்தல் நடத்தும் அதிகாரியால் வழங்கப்படும் சட்டப்பூர்வ தேர்தல் சான்றிதழ் எது?",
        en_a="Form 22 (Certificate of Election)", ta_a="படிவம் 22 (தேர்தல் சான்றிதழ் - Certificate of Election)",
        en_b="Form 21C (Declaration of Result)", ta_b="படிவம் 21C (முடிவு அறிவிப்பு)",
        en_c="Form 7A (List of Contesting Candidates)", ta_c="படிவம் 7A (போட்டியிடும் வேட்பாளர்கள் பட்டியல்)",
        en_d="Form 17C (Account of Votes Recorded)", ta_d="படிவம் 17C (பதிவான வாக்குகள் கணக்கு)",
        correct_key="A",
        exp_en="Rule 66 provides that as soon as a candidate has been declared elected, the Returning Officer shall grant to such candidate a Certificate of Election in Form 22 and obtain from him an acknowledgment of receipt.",
        exp_ta="விதி 66-ன் படி, வெற்றி அறிவிக்கப்பட்ட உடனேயே தேர்தல் அதிகாரி படிவம் 22-ல் தேர்தல் சான்றிதழை வழங்கி அவரிடமிருந்து ஒப்புதல் பெற வேண்டும்.",
        why_a_en="Correct. Form 22 is the Certificate of Election granted to the winner.",
        why_a_ta="சரியானது. படிவம் 22 வெற்றியாளருக்கு வழங்கப்படும் தேர்தல் சான்றிதழ் ஆகும்.",
        why_b_en="Incorrect. Form 21C is the public declaration of result document.",
        why_b_ta="தவறானது. படிவம் 21C என்பது முடிவு அறிவிப்பு ஆவணம்.",
        why_c_en="Incorrect. Form 7A is the list of candidates contesting.",
        why_c_ta="தவறானது. படிவம் 7A போட்டியிடும் வேட்பாளர்கள் பட்டியல்.",
        why_d_en="Incorrect. Form 17C is poll day vote account.",
        why_d_ta="தவறானது. படிவம் 17C வாக்குப்பதிவு கணக்கு.",
        tip_en="A newly elected MP/MLA must present this Form 22 certificate to the Secretary-General of Parliament/Assembly to take the oath.",
        tip_ta="புதிதாக தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் பதவிப்பிரமாணம் செய்ய இந்த படிவம் 22 சான்றிதழை சமர்ப்பிக்க வேண்டும்.",
        fact_en="Form 22 is signed and sealed exclusively by the Returning Officer.",
        fact_ta="படிவம் 22 தேர்தல் நடத்தும் அதிகாரியால் மட்டுமே கையொப்பமிட்டு முத்திரையிடப்படுகிறது.",
        tags=["Form 22", "Certificate of Election", "Rule 66"]
    ))

    # GT 037
    qs.append(make_ec_q(
        qid="EC_GT_037", diff="Hard", qtype="Single-Choice", subtopic="Section 100 Voiding Election",
        en_stem="Under Section 100(1)(a) of the Representation of the People Act, 1951, the High Court shall declare the election of a returned candidate void if:",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 100(1)(a)-ன் கீழ், உயர் நீதிமன்றம் ஒரு வேட்பாளரின் தேர்தலை செல்லாதது என எப்போது அறிவிக்கும்?",
        en_a="On the date of his election, the returned candidate was not qualified, or was disqualified, to be chosen to fill the seat under the Constitution or this Act", ta_a="தேர்தல் தேதியன்று, வெற்றி பெற்ற வேட்பாளர் அரசியலமைப்பு அல்லது இச்சட்டத்தின் கீழ் தகுதியற்றவராகவோ அல்லது தகுதிநீக்கம் செய்யப்பட்டவராகவோ இருந்த போது",
        en_b="The voter turnout in the constituency was less than 40%", ta_b="தொகுதியில் வாக்குப்பதிவு 40%-க்கும் குறைவாக இருந்த போது",
        en_c="The margin of victory was fewer than 100 votes", ta_c="வெற்றி வித்தியாசம் 100 வாக்குகளுக்கும் குறைவாக இருந்த போது",
        en_d="The candidate spent less than 50% of the prescribed election expenditure ceiling", ta_d="வேட்பாளர் நிர்ணயிக்கப்பட்ட செலவு வரம்பில் 50%-க்கும் குறைவாக செலவு செய்த போது",
        correct_key="A",
        exp_en="Section 100(1)(a) mandates that if the High Court is of opinion that on the date of his election a returned candidate was not qualified, or was disqualified, under the Constitution or RPA 1951, the High Court SHALL declare the election void.",
        exp_ta="பிரிவு 100(1)(a)-ன் படி, தேர்தல் நாளன்று வெற்றி பெற்ற வேட்பாளர் அரசியலமைப்பு அல்லது சட்டப்படி தகுதியற்றவராகவோ அல்லது தகுதிநீக்கத்திற்கு ஆளானவராகவோ இருந்தார் என உயர்நீதிமன்றம் கருதினால், அத்தேர்தலை செல்லாது என அறிவிக்கும்.",
        why_a_en="Correct. Lack of qualification/disqualification on election date voids the election.",
        why_a_ta="சரியானது. தேர்தல் தேதியில் தகுதியின்மை தேர்தலை செல்லாததாக்கும்.",
        why_b_en="Incorrect. Turnout percentage has no bearing on validity.",
        why_b_ta="தவறானது. வாக்குப்பதிவு சதவீதம் தேர்தலை பாதிக்காது.",
        why_c_en="Incorrect. Victory by even 1 vote is valid.",
        why_c_ta="தவறானது. 1 வாக்கு வித்தியாசத்தில் வென்றாலும் செல்லுபடியாகும்.",
        why_d_en="Incorrect. Under-spending is completely legal.",
        why_d_ta="தவறானது. குறைவாக செலவு செய்வது குற்றமல்ல.",
        tip_en="Other grounds under Section 100 include corrupt practice (100(1)(b)) and improper acceptance/rejection of nomination (100(1)(c)).",
        tip_ta="பிரிவு 100-ன் பிற காரணங்களில் ஊழல் நடைமுறைகள் மற்றும் வேட்புமனுவை தவறாக ஏற்றல்/நிராகரித்தல் ஆகியவை அடங்கும்.",
        fact_en="Section 100 was famously invoked to void Indira Gandhi's election in Raj Narain v. State of UP (1975).",
        fact_ta="1975 ராஜ் நாராயணன் வழக்கில் இந்திரா காந்தியின் தேர்தலை ரத்து செய்ய பிரிவு 100 பயன்படுத்தப்பட்டது.",
        tags=["Section 100", "Void Election", "High Court Powers"]
    ))

    # GT 038
    qs.append(make_ec_q(
        qid="EC_GT_038", diff="Medium", qtype="Single-Choice", subtopic="Section 125A False Affidavit",
        en_stem="Under Section 125A of RPA 1951, what is the maximum punishment for a candidate who knowingly conceals information or provides false information in the nomination affidavit?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 125A-ன் கீழ், வேட்புமனு பிரமாணப் பத்திரத்தில் தகவல்களை வேண்டுமென்றே மறைக்கும் அல்லது தவறான தகவல்களை வழங்கும் வேட்பாளருக்கு விதிக்கப்படும் அதிகபட்ச தண்டனை என்ன?",
        en_a="Imprisonment for a term which may extend to six months, or with fine, or with both", ta_a="ஆறு மாதங்கள் வரை நீட்டிக்கப்படக்கூடிய சிறைத்தண்டனை, அல்லது அபராதம், அல்லது இரண்டும்",
        en_b="Rigorous imprisonment for up to 3 years and permanent debarment", ta_b="3 ஆண்டுகள் வரை கடுங்காவல் சிறை மற்றும் நிரந்தர தடை",
        en_c="A fine of Rs. 10,000 only without any imprisonment", ta_c="சிறைத் தண்டனையின்றி ரூ. 10,000 அபராதம் மட்டுமே",
        en_d="Disqualification for two consecutive legislative terms", ta_d="தொடர்ந்து இரண்டு சட்டமன்றப் பதவிக்காலங்களுக்கு தகுதிநீக்கம்",
        correct_key="A",
        exp_en="Section 125A provides that a candidate failing to furnish required information or giving false information in Form 26 affidavit shall be punishable with imprisonment up to 6 months, or fine, or both.",
        exp_ta="பிரிவு 125A-ன் கீழ், படிவம் 26 பிரமாணப் பத்திரத்தில் விவரங்களை அளிக்கத் தவறும் அல்லது பொய் தகவல் அளிக்கும் வேட்பாளருக்கு 6 மாதம் வரை சிறை அல்லது அபராதம் அல்லது இரண்டும் விதிக்கப்படலாம்.",
        why_a_en="Correct. Up to 6 months imprisonment, or fine, or both under Section 125A.",
        why_a_ta="சரியானது. பிரிவு 125A-ன் கீழ் 6 மாதம் வரை சிறை அல்லது அபராதம்.",
        why_b_en="Incorrect. 3 years is incorrect.",
        why_b_ta="தவறானது. 3 ஆண்டுகள் தவறானது.",
        why_c_en="Incorrect. Imprisonment is statutorily provided.",
        why_c_ta="தவறானது. சிறைத் தண்டனை சட்டத்தில் உள்ளது.",
        why_d_en="Incorrect. Disqualification requires separate judicial proceedings.",
        why_d_ta="தவறானது. தகுதிநீக்கத்திற்கு தனி நீதிமன்ற உத்தரவு தேவை.",
        tip_en="In Krishnamoorthy v. Sivakumar (2015), SC held that filing a false affidavit on criminal cases amounts to 'undue influence' under Section 123(2).",
        tip_ta="குற்றப்பின்னணியை மறைப்பது பிரிவு 123(2)-ன் கீழ் வாக்காளரை தவறாக வழிநடத்தும் ஊழல் செயலாகும் என உச்ச நீதிமன்றம் கூறியது.",
        fact_en="Section 125A was inserted in 2002 following the landmark ADR disclosure judgment.",
        fact_ta="2002 ADR தீர்ப்பைத் தொடர்ந்து பிரிவு 125A சட்டத்தில் சேர்க்கப்பட்டது.",
        tags=["Section 125A", "False Affidavit", "Punishment"]
    ))

    # GT 039
    qs.append(make_ec_q(
        qid="EC_GT_039", diff="Easy", qtype="Single-Choice", subtopic="Section 126A Exit Polls",
        en_stem="Under Section 126A of RPA 1951, what does the statutory ban on exit polls prohibit?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 126A-ன் கீழ், தேர்தலுக்குப் பிந்தைய கருத்துக் கணிப்புகள் (exit polls) மீதான சட்டப்பூர்வ தடை எதை உள்ளடக்கியது?",
        en_a="Conducting or publishing exit polls through print, electronic media, or any other manner from the commencement of poll in the first phase until half an hour after the close of poll in the last phase", ta_a="முதல் கட்ட வாக்குப்பதிவு தொடங்கும் நேரம் முதல் இறுதிக் கட்ட வாக்குப்பதிவு முடிந்து அரை மணி நேரம் வரை அச்சு, மின்னணு ஊடகங்களில் கருத்துக்கணிப்புகளை நடத்துவது அல்லது வெளியிடுவது",
        en_b="Conducting exit polls on counting day only", ta_b="வாக்கு எண்ணிக்கை நாளன்று மட்டும் கருத்துக்கணிப்புகளை நடத்துவது",
        en_c="Publishing exit polls by opposition parties while permitting ruling parties to broadcast them", ta_c="எதிர்க்கட்சிகள் வெளியிடுவதைத் தடுத்து ஆளும் கட்சி வெளியிட அனுமதிப்பது",
        en_d="Conducting exit polls inside universities and academic institutions", ta_d="பல்கலைக்கழகங்களுக்குள் கருத்துக்கணிப்பு நடத்துவது மட்டும்",
        correct_key="A",
        exp_en="Section 126A strictly bans conducting and publishing exit polls from the start of the poll in the first phase until half an hour after the conclusion of the poll in all phases.",
        exp_ta="பிரிவு 126A முதல் கட்ட வாக்குப்பதிவு தொடங்குவதிலிருந்து இறுதிக்கட்ட வாக்குப்பதிவு முடிந்த அரை மணி நேரம் வரை கருத்துக் கணிப்புகளை வெளியிட முற்றிலும் தடை விதிக்கிறது.",
        why_a_en="Correct. Complete ban from phase 1 poll start to 30 mins after final phase close.",
        why_a_ta="சரியானது. முதல் கட்டத் தொடக்கம் முதல் இறுதிக் கட்டம் முடிந்த 30 நிமிடம் வரை முழுத் தடை.",
        why_b_en="Incorrect. Ban covers the entire multi-phase polling period, not just counting day.",
        why_b_ta="தவறானது. அனைத்து கட்ட வாக்குப்பதிவு காலத்தையும் இத்தடை உள்ளடக்கும்.",
        why_c_en="Incorrect. The ban applies equally to all entities.",
        why_c_ta="தவறானது. அனைவருக்கும் சமமாகப் பொருந்தும்.",
        why_d_en="Incorrect. The ban is universal across all media.",
        why_d_ta="தவறானது. அனைத்து ஊடகங்களுக்கும் பொருந்தும்.",
        tip_en="Violation of Section 126A is punishable with imprisonment up to 2 years or fine, or both.",
        tip_ta="பிரிவு 126A-ஐ மீறினால் 2 ஆண்டுகள் வரை சிறை அல்லது அபராதம் விதிக்கப்படலாம்.",
        fact_en="Section 126A was inserted by the Representation of the People (Amendment) Act, 2009.",
        fact_ta="2009 திருத்தச் சட்டம் மூலம் பிரிவு 126A சேர்க்கப்பட்டது.",
        tags=["Section 126A", "Exit Polls Ban", "RPA 1951"]
    ))

    # GT 040
    qs.append(make_ec_q(
        qid="EC_GT_040", diff="Medium", qtype="Single-Choice", subtopic="SVEEP Program",
        en_stem="What is the primary mandate of 'SVEEP' launched by the Election Commission of India in 2009?",
        ta_stem="2009-ல் இந்திய தேர்தல் ஆணையத்தால் தொடங்கப்பட்ட 'SVEEP' திட்டத்தின் முதன்மை நோக்கம் என்ன?",
        en_a="Systematic Voters' Education and Electoral Participation for voter awareness and literacy", ta_a="வாக்காளர் விழிப்புணர்வு மற்றும் கல்விக்கான 'முறையான வாக்காளர் கல்வி மற்றும் தேர்தல் பங்கேற்பு' (SVEEP)",
        en_b="Single-window verification of Electronic Voting Machines by engineering experts", ta_b="பொறியியல் வல்லுநர்களால் மின்னணு வாக்குப்பதிவு இயந்திரங்களை ஒற்றைச் சாளர முறையில் சரிபார்த்தல்",
        en_c="Statutory vigilance and surveillance of illicit election expenditures", ta_c="சட்டவிரோத தேர்தல் செலவினங்களை சட்டப்பூர்வமாகக் கண்காணித்தல்",
        en_d="Software validation of electronic postal ballot systems", ta_d="மின்னணு தபால் வாக்கு அமைப்புகளின் மென்பொருள் சரிபார்ப்பு",
        correct_key="A",
        exp_en="SVEEP stands for 'Systematic Voters' Education and Electoral Participation', ECI's flagship program launched in 2009 to inform, educate, motivate, and facilitate citizens for active democratic participation.",
        exp_ta="SVEEP என்பது 'Systematic Voters Education and Electoral Participation' ஆகும்; குடிமக்களுக்கு விழிப்புணர்வு ஏற்படுத்தி தேர்தல் பங்கேற்பை அதிகரிக்க 2009-ல் ECI-ஆல் இது தொடங்கப்பட்டது.",
        why_a_en="Correct. Systematic Voters' Education and Electoral Participation.",
        why_a_ta="சரியானது. முறையான வாக்காளர் கல்வி மற்றும் தேர்தல் பங்கேற்பு திட்டம்.",
        why_b_en="Incorrect. That is First Level Checking (FLC).",
        why_b_ta="தவறானது. அது முதற்கட்ட சரிபார்ப்பு (FLC) ஆகும்.",
        why_c_en="Incorrect. That is the Expenditure Monitoring Division.",
        why_c_ta="தவறானது. அது செலவின கண்காணிப்புப் பிரிவு ஆகும்.",
        why_d_en="Incorrect. That is ETPBS.",
        why_d_ta="தவறானது. அது ETPBS ஆகும்.",
        tip_en="SVEEP engages National and State icons (e.g. sportspersons, artists) to inspire voter turnout.",
        tip_ta="வாக்குப்பதிவை அதிகரிக்க தேசிய மற்றும் மாநில தூதர்களை SVEEP பயன்படுத்துகிறது.",
        fact_en="Voter turnout crossed 67% in the 2019 Lok Sabha elections, the highest in India's history, partly attributed to SVEEP.",
        fact_ta="2019 மக்களவைத் தேர்தலில் நாட்டின் வரலாற்று உச்சமாக 67% வாக்குப்பதிவு பதிவானது.",
        tags=["SVEEP", "Voter Education", "Flagship Program"]
    ))

    # GT 041 to GT 050
    # GT 041
    qs.append(make_ec_q(
        qid="EC_GT_041", diff="Hard", qtype="Single-Choice", subtopic="Kamal Nath Star Campaigner Case",
        en_stem="In Election Commission of India v. Kamal Nath (2020), what did the Supreme Court hold regarding the ECI's power to revoke the 'star campaigner' status of a political leader?",
        ta_stem="இந்தியத் தேர்தல் ஆணையம் எதிர் கமல் நாத் (2020) வழக்கில், ஒரு அரசியல் தலைவரின் 'நட்சத்திர பேச்சாளர்' அந்தஸ்தை ரத்து செய்யும் தேர்தல் ஆணையத்தின் அதிகாரம் குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        en_a="The Election Commission has no statutory power under Section 77 of RPA 1951 to strip a leader of star campaigner status, as that power belongs solely to the political party", ta_a="பிரிவு 77-ன் கீழ் ஒரு தலைவரின் நட்சத்திர பேச்சாளர் அந்தஸ்தை நீக்க தேர்தல் ஆணையத்திற்கு சட்டப்பூர்வ அதிகாரம் இல்லை; அந்த அதிகாரம் அரசியல் கட்சிக்கே உரியது",
        en_b="The Election Commission possesses absolute plenary authority to remove any star campaigner without judicial review", ta_b="நீதிமன்ற ஆய்வின்றி எந்தவொரு நட்சத்திர பேச்சாளரையும் நீக்க தேர்தல் ஆணையத்திற்கு முழு அதிகாரம் உண்டு",
        en_c="The High Court alone has jurisdiction to delist star campaigners", ta_c="உயர் நீதிமன்றத்திற்கு மட்டுமே நட்சத்திர பேச்சாளரை நீக்கும் அதிகாரம் உண்டு",
        en_d="Star campaigners are automatically disqualified if they receive two MCC notices", ta_d="இரண்டு நடத்தை விதிமீறல் நோட்டீஸ்களைப் பெற்றால் நட்சத்திர பேச்சாளர்கள் தானாகவே தகுதிநீக்கம் செய்யப்படுவர்",
        correct_key="A",
        exp_en="In November 2020, CJI S.A. Bobde stayed the ECI's order revoking Kamal Nath's star campaigner status, holding that Section 77 vests the power to designate party leaders exclusively in the political party, not the Election Commission.",
        exp_ta="2020 நவம்பரில் உச்ச நீதிமன்றம், பிரிவு 77-ன் கீழ் நட்சத்திர பேச்சாளர்களை நியமிக்கும் அதிகாரம் கட்சிக்கே உரியது என்றும், தேர்தல் ஆணையத்திற்கு அதனை ரத்து செய்யும் சட்ட அதிகாரம் இல்லை என்றும் கூறி ECI உத்தரவுக்கு தடை விதித்தது.",
        why_a_en="Correct. ECI lacks statutory power under Section 77 to revoke star campaigner status.",
        why_a_ta="சரியானது. பிரிவு 77-ன் கீழ் நட்சத்திர பேச்சாளர் அந்தஸ்தை ரத்து செய்ய ECI-க்கு சட்ட அதிகாரம் இல்லை.",
        why_b_en="Incorrect. Supreme Court rejected ECI's claim of unbridled power.",
        why_b_ta="தவறானது. ஆணையத்தின் வரம்பற்ற அதிகாரக் கோரிக்கையை நீதிமன்றம் நிராகரித்தது.",
        why_c_en="Incorrect. High Court has no such administrative role.",
        why_c_ta="தவறானது. உயர் நீதிமன்றத்திற்கு இதில் தொடர்பில்லை.",
        why_d_en="Incorrect. There is no automatic disqualification rule.",
        why_d_ta="தவறானது. தானியங்கி தகுதிநீக்க விதி எதுவும் இல்லை.",
        tip_en="Section 77(1) Explanation 2 explicitly states that leaders of the party are determined by the political party itself.",
        tip_ta="பிரிவு 77(1) விளக்கம் 2, கட்சியின் தலைவர்களை அரசியல் கட்சியே தீர்மானிக்கிறது என தெளிவாகக் கூறுகிறது.",
        fact_en="While ECI cannot strip the title, it can bar any campaigner from addressing public rallies for specific durations under Article 324.",
        fact_ta="தலைப்பை நீக்க முடியாவிட்டாலும், குறிப்பிட்ட காலத்திற்கு பொதுக்கூட்டங்களில் பேச தடை விதிக்க ECI-க்கு சரத்து 324-ன் கீழ் அதிகாரம் உண்டு.",
        tags=["Kamal Nath Case", "Star Campaigner", "Section 77"]
    ))

    # GT 042
    qs.append(make_ec_q(
        qid="EC_GT_042", diff="Medium", qtype="Single-Choice", subtopic="Braille on EVMs",
        en_stem="To assist visually impaired voters, in which year did the Election Commission introduce Braille signage on Electronic Voting Machines (EVMs)?",
        ta_stem="பார்வையற்ற வாக்காளர்களுக்கு உதவும் வகையில், மின்னணு வாக்குப்பதிவு இயந்திரங்களில் (EVM) பிரெய்லி எழுத்து முறையை இந்திய தேர்தல் ஆணையம் எந்த ஆண்டு அறிமுகப்படுத்தியது?",
        en_a="2009 Lok Sabha elections", ta_a="2009 மக்களவைத் தேர்தல்",
        en_b="2004 Lok Sabha elections", ta_b="2004 மக்களவைத் தேர்தல்",
        en_c="2014 Lok Sabha elections", ta_c="2014 மக்களவைத் தேர்தல்",
        en_d="1998 Assembly elections", ta_d="1998 சட்டமன்றத் தேர்தல்",
        correct_key="A",
        exp_en="Braille signage on the right side of the candidate buttons on Ballot Units was introduced nationally during the 2009 Lok Sabha elections following pilots in 2006-2008.",
        exp_ta="வாக்குப்பதிவு அலகில் வேட்பாளர் பொத்தான்களுக்கு வலதுபுறத்தில் பிரெய்லி எண்கள் பொறிக்கும் வசதி 2009 மக்களவைத் தேர்தலில் நாடு முழுவதும் அறிமுகப்படுத்தப்பட்டது.",
        why_a_en="Correct. Introduced nationally in 2009.",
        why_a_ta="சரியானது. 2009 தேர்தலில் நாடு முழுவதும் அறிமுகப்படுத்தப்பட்டது.",
        why_b_en="Incorrect. 2004 did not have Braille signage on EVMs.",
        why_b_ta="தவறானது. 2004-ல் பிரெய்லி வசதி இல்லை.",
        why_c_en="Incorrect. 2014 was much later than introduction.",
        why_c_ta="தவறானது. 2014-க்கு முன்பே அறிமுகமானது.",
        why_d_en="Incorrect. 1998 had no Braille.",
        why_d_ta="தவறானது. 1998-ல் பிரெய்லி இல்லை.",
        tip_en="In addition, Braille ballot sheets are provided to visually impaired electors at every polling station.",
        tip_ta="மேலும் ஒவ்வொரு வாக்குச்சாவடியிலும் பார்வையற்றோருக்காக பிரெய்லி வாக்குச் சீட்டுகளும் வழங்கப்படுகின்றன.",
        fact_en="Rule 49N of Conduct of Elections Rules permits a companion to accompany a blind/infirm elector inside the voting compartment.",
        fact_ta="விதி 49N பார்வையற்ற வாக்காளர்களுக்கு உதவ ஒரு துணையாளர் உடன் செல்ல அனுமதிக்கிறது.",
        tags=["Braille on EVM", "Accessible Elections", "2009 Elections"]
    ))

    # GT 043
    qs.append(make_ec_q(
        qid="EC_GT_043", diff="Easy", qtype="Single-Choice", subtopic="Pink Booths",
        en_stem="What are 'Pink Booths' (Sakhi Booths) set up by the Election Commission during elections?",
        ta_stem="தேர்தல்களின் போது தேர்தல் ஆணையத்தால் அமைக்கப்படும் 'பிங்க் வாக்குச்சாவடிகள்' (சகி வாக்குச்சாவடிகள்) என்பவை யாவை?",
        en_a="Polling stations managed entirely by women polling personnel and security staff to encourage female voter turnout", ta_a="பெண் வாக்காளர்களின் வாக்குப்பதிவை ஊக்குவிக்க, முழுமையாக பெண் தேர்தல் பணியாளர்கள் மற்றும் பெண் காவலர்களால் மட்டுமே நிர்வகிக்கப்படும் வாக்குச்சாவடிகள்",
        en_b="Polling booths set up exclusively inside maternity hospitals", ta_b="மகப்பேறு மருத்துவமனைகளுக்குள் மட்டுமே அமைக்கப்படும் வாக்குச்சாவடிகள்",
        en_c="Booths reserved exclusively for first-time voters aged 18 to 21", ta_c="18 முதல் 21 வயதுடைய முதல்முறை வாக்காளர்களுக்கு மட்டுமே ஒதுக்கப்பட்ட வாக்குச்சாவடிகள்",
        en_d="Booths designated for receiving voluntary election contributions", ta_d="தன்னார்வ தேர்தல் நன்கொடைகளைப் பெறுவதற்காக அமைக்கப்பட்ட வாக்குச்சாவடிகள்",
        correct_key="A",
        exp_en="'Pink Booths' (also called Sakhi Booths) are all-women managed polling stations where all election officials (Presiding Officer, Polling Officers, police, and security) are women, aimed at gender empowerment and increasing female voter participation.",
        exp_ta="'பிங்க் வாக்குச்சாவடிகள்' என்பவை தலைமை அலுவலர், பணியாளர்கள், காவலர்கள் என அனைவரும் பெண்களாக மட்டுமே உள்ள வாக்குச்சாவடிகளாகும்; இது பெண் வாக்காளர்களின் பங்கேற்பை அதிகரிக்க உதவுகிறது.",
        why_a_en="Correct. Entirely managed by women personnel.",
        why_a_ta="சரியானது. முற்றிலும் பெண்களால் மட்டுமே நிர்வகிக்கப்படும் வாக்குச்சாவடிகள்.",
        why_b_en="Incorrect. Not located in hospitals.",
        why_b_ta="தவறானது. மருத்துவமனைகளில் அல்ல.",
        why_c_en="Incorrect. Youth booths are different from Pink booths.",
        why_c_ta="தவறானது. இளைஞர் வாக்குச்சாவடிகள் வேறுபட்டவை.",
        why_d_en="Incorrect. Polling booths cannot receive financial contributions.",
        why_d_ta="தவறானது. வாக்குச்சாவடிகளில் நன்கொடை பெற முடியாது.",
        tip_en="ECI also establishes PwD-managed booths where all staff are Persons with Disabilities.",
        tip_ta="அனைத்துப் பணியாளர்களும் மாற்றுத்திறனாளிகளாக உள்ள பிரத்யேக வாக்குச்சாவடிகளையும் ECI அமைக்கிறது.",
        fact_en="Pink booths were first piloted in the 2017 Assembly elections in Goa and Punjab.",
        fact_ta="2017 கோவா மற்றும் பஞ்சாப் சட்டமன்றத் தேர்தல்களில் முதன்முதலில் பிங்க் வாக்குச்சாவடிகள் அமைக்கப்பட்டன.",
        tags=["Pink Booths", "Sakhi Booths", "Gender Empowerment"]
    ))

    # GT 044
    qs.append(make_ec_q(
        qid="EC_GT_044", diff="Medium", qtype="Single-Choice", subtopic="Webcasting Threshold",
        en_stem="According to ECI guidelines for recent general elections, what minimum percentage of polling stations must be covered under live webcasting and CCTV monitoring?",
        ta_stem="சமீபத்திய பொதுத் தேர்தல்களுக்கான ECI வழிகாட்டுதல்களின்படி, குறைந்தபட்சம் எத்தனை சதவீத வாக்குச்சாவடிகள் நேரடி வலைபரப்பு (live webcasting) மற்றும் CCTV கண்காணிப்பின் கீழ் கொண்டுவரப்பட வேண்டும்?",
        en_a="At least 50% of all polling stations", ta_a="அனைத்து வாக்குச்சாவடிகளில் குறைந்தது 50%",
        en_b="100% of all polling stations", ta_b="அனைத்து வாக்குச்சாவடிகளில் 100%",
        en_c="At least 20% of all polling stations", ta_c="அனைத்து வாக்குச்சாவடிகளில் குறைந்தது 20%",
        en_d="Only polling stations with history of violence (critical booths)", ta_d="வன்முறை வரலாற்றைக் கொண்ட பதற்றமான வாக்குச்சாவடிகள் மட்டுமே",
        correct_key="A",
        exp_en="ECI mandates that live webcasting and CCTV monitoring must be deployed in at least 50% of all polling stations (including all critical and vulnerable polling stations) to enable real-time tracking by District Election Officers and CEOs.",
        exp_ta="மாவட்ட தேர்தல் அதிகாரிகள் மற்றும் தலைமை தேர்தல் அதிகாரியின் நேரடி கண்காணிப்பிற்காக, பதற்றமான வாக்குச்சாவடிகள் உட்பட குறைந்தபட்சம் 50% வாக்குச்சாவடிகளில் நேரடி வலைபரப்பு செய்யப்பட வேண்டும் என ECI கட்டாயமாக்கியுள்ளது.",
        why_a_en="Correct. Minimum 50% webcasting coverage.",
        why_a_ta="சரியானது. குறைந்தது 50% வலைபரப்பு கண்காணிப்பு வரம்பு.",
        why_b_en="Incorrect. 100% is not universally feasible due to hilly/remote connectivity gaps.",
        why_b_ta="தவறானது. இணைய வசதி இல்லாத இடங்களில் 100% சாத்தியமில்லை.",
        why_c_en="Incorrect. 20% is below the required standard.",
        why_c_ta="தவறானது. 20% நிர்ணயிக்கப்பட்ட அளவை விடக் குறைவு.",
        why_d_en="Incorrect. Not restricted solely to critical booths.",
        why_d_ta="தவறானது. பதற்றமான பூத்களுடன் பொது பூத்களும் இதில் அடங்கும்.",
        tip_en="Cameras are positioned behind the Presiding Officer to monitor the room without compromising secrecy of voting in the voting compartment.",
        tip_ta="வாக்கு ரகசியம் பாதிக்கப்படாத வகையில் கேமராக்கள் தலைமை அலுவலரின் பின்புறமாக வைக்கப்படுகின்றன.",
        fact_en="Control rooms set up at district and state levels monitor these live feeds simultaneously on poll day.",
        fact_ta="தேர்தல் நாளன்று மாவட்ட மற்றும் மாநில கட்டுப்பாட்டு அறைகள் இந்த நேரடி காட்சிகளை கண்காணிக்கின்றன.",
        tags=["Webcasting", "CCTV Monitoring", "50 Percent Rule"]
    ))

    # GT 045
    qs.append(make_ec_q(
        qid="EC_GT_045", diff="Hard", qtype="Single-Choice", subtopic="Flying Squads & SST",
        en_stem="What is the operational distinction between Flying Squad Teams (FST) and Static Surveillance Teams (SST) deployed during elections under ECI's expenditure monitoring framework?",
        ta_stem="ECI-ன் செலவின கண்காணிப்பு கட்டமைப்பின் கீழ் தேர்தலின் போது நிறுத்தப்படும் பறக்கும் படைகள் (FST) மற்றும் நிலையான கண்காணிப்புக் குழுக்களுக்கு (SST) இடையேயான செயல்பாட்டு வேறுபாடு என்ன?",
        en_a="FST is mobile and responds to complaints and MCC violations, while SST operates at fixed check-posts to monitor movement of bulk cash, liquor, and arms", ta_a="FST என்பது நடமாடும் குழுவாக புகார்கள் மற்றும் நடத்தை விதிமீறல்களுக்கு பதிலளிக்கிறது; SST என்பது மொத்தப் பணம், மதுபானம் மற்றும் ஆயுதங்களின் நடமாட்டத்தைக் கண்காணிக்க நிலையான சோதனைச் சாவடிகளில் செயல்படுகிறது",
        en_b="FST inspects candidate accounts, while SST audits bank accounts", ta_b="FST வேட்பாளர் கணக்குகளை ஆய்வு செய்கிறது; SST வங்கிக் கணக்குகளைத் தணிக்கை செய்கிறது",
        en_c="FST operates only in urban areas, while SST operates exclusively in rural areas", ta_c="FST நகர்ப்புறங்களில் மட்டுமே செயல்படுகிறது; SST கிராமப்புறங்களில் மட்டுமே செயல்படுகிறது",
        en_d="FST reports to the High Court, while SST reports to the State Election Commissioner", ta_d="FST உயர் நீதிமன்றத்திற்கு அறிக்கை அளிக்கிறது; SST மாநில தேர்தல் ஆணையரிடம் அறிக்கை அளிக்கிறது",
        correct_key="A",
        exp_en="Flying Squad Teams (FST) are mobile operational units with dedicated vehicles, a magistrate, police, and videographer that respond rapidly to cVIGIL/public complaints. Static Surveillance Teams (SST) set up round-the-clock check-posts on major roads to intercept illegal cash, narcotics, and distribution items.",
        exp_ta="பறக்கும் படைகள் (FST) என்பது மாஜிஸ்திரேட் மற்றும் காவல்துறையுடன் கூடிய நடமாடும் குழுவாகும்; நிலையான கண்காணிப்புக் குழுக்கள் (SST) முக்கிய சாலைகளில் சோதனைச் சாவடிகளை அமைத்து சட்டவிரோத பணம் மற்றும் பரிசுப் பொருட்களை பறிமுதல் செய்கின்றன.",
        why_a_en="Correct. FST is mobile/complaint-driven; SST is fixed/check-post interceptor.",
        why_a_ta="சரியானது. FST நடமாடும் புகார் பிரிவு; SST நிலையான சோதனைச் சாவடி பிரிவு.",
        why_b_en="Incorrect. Inspection of accounts is done by the Accounting Team under Assistant Expenditure Observers.",
        why_b_ta="தவறானது. கணக்குகளை ஆய்வு செய்வது கணக்குக் குழுவின் பணியாகும்.",
        why_c_en="Incorrect. Both operate across all constituencies.",
        why_c_ta="தவறானது. இரண்டுமே அனைத்து பகுதிகளிலும் செயல்படுகின்றன.",
        why_d_en="Incorrect. Both report to the District Election Officer and Expenditure Observer.",
        why_d_ta="தவறானது. இரண்டுமே மாவட்ட தேர்தல் அதிகாரியின் கீழ் இயங்குகின்றன.",
        tip_en="Cash seizures above Rs. 50,000 without supporting documents are intercepted by SST.",
        tip_ta="ஆவணங்களின்றி எடுத்துச் செல்லப்படும் ரூ. 50,000-க்கு மேற்பட்ட பணம் SST-யால் பறிமுதல் செய்யப்படுகிறது.",
        fact_en="A district-level Grievance Redressal Committee headed by a senior civil officer hears appeals from citizens whose legitimate cash was seized.",
        fact_ta="பொதுமக்களின் நியாயமான பணம் பறிமுதல் செய்யப்பட்டால் அதைத் திரும்பப் பெற மாவட்ட அளவில் மேல்முறையீட்டுக் குழு உள்ளது.",
        tags=["Flying Squads", "Static Surveillance", "Expenditure Monitoring"]
    ))

    # GT 046
    qs.append(make_ec_q(
        qid="EC_GT_046", diff="Medium", qtype="Single-Choice", subtopic="Section 128 Secrecy",
        en_stem="Under Section 128 of the Representation of the People Act, 1951, what penalty can be imposed on an election officer or agent for infringement of the secrecy of voting?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 128-ன் கீழ், வாக்கு ரகசியத்தை மீறும் தேர்தல் அதிகாரி அல்லது முகவர் மீது என்ன தண்டனை விதிக்கப்படலாம்?",
        en_a="Imprisonment for a term which may extend to three months, or with fine, or with both", ta_a="மூன்று மாதங்கள் வரை நீட்டிக்கப்படக்கூடிய சிறைத்தண்டனை, அல்லது அபராதம், அல்லது இரண்டும்",
        en_b="Imprisonment for not less than two years", ta_b="இரண்டு ஆண்டுகளுக்கு குறையாத சிறைத்தண்டனை",
        en_c="Fine of Rs. 50,000 without any imprisonment", ta_c="சிறைத் தண்டனையின்றி ரூ. 50,000 அபராதம்",
        en_d="Automatic termination from service and forfeiture of all assets", ta_d="பணியிலிருந்து தானாகவே நீக்கப்படுதல் மற்றும் அனைத்து சொத்துக்களையும் பறிமுதல் செய்தல்",
        correct_key="A",
        exp_en="Section 128(2) of RPA 1951 provides that any officer, clerk, agent, or other person who aids in maintaining or infringes the secrecy of voting shall be punished with imprisonment up to 3 months, or with fine, or with both.",
        exp_ta="பிரிவு 128(2)-ன் படி, வாக்கு ரகசியத்தைப் பாதுகாக்கத் தவறும் அல்லது அதனை மீறும் எந்தவொரு அதிகாரி அல்லது முகவருக்கு 3 மாதங்கள் வரை சிறை அல்லது அபராதம் அல்லது இரண்டும் விதிக்கப்படலாம்.",
        why_a_en="Correct. Up to 3 months imprisonment, or fine, or both under Section 128.",
        why_a_ta="சரியானது. பிரிவு 128-ன் கீழ் 3 மாதங்கள் வரை சிறை அல்லது அபராதம்.",
        why_b_en="Incorrect. 2 years is under Section 126A (exit polls).",
        why_b_ta="தவறானது. 2 ஆண்டுகள் என்பது பிரிவு 126A-ல் உள்ளது.",
        why_c_en="Incorrect. Statutory limit is not Rs. 50,000.",
        why_c_ta="தவறானது. ரூ. 50,000 அல்ல.",
        why_d_en="Incorrect. Asset forfeiture is not provided.",
        why_d_ta="தவறானது. சொத்து பறிமுதல் இதில் இல்லை.",
        tip_en="Secrecy of voting is a sacrosanct hallmark of free and fair elections in Indian jurisprudence.",
        tip_ta="வாக்கு ரகசியம் என்பது இந்திய தேர்தல் அமைப்பின் புனிதமான அடித்தளமாகும்.",
        fact_en="Even in court, a voter cannot be compelled to disclose for whom they voted under Section 94 of RPA 1951.",
        fact_ta="நீதிமன்றத்திலும் கூட தான் யாருக்கு வாக்களித்தோம் என்பதை வெளியிட வாக்காளரை கட்டாயப்படுத்த முடியாது (பிரிவு 94).",
        tags=["Section 128", "Secrecy of Voting", "Electoral Offences"]
    ))

    # GT 047
    qs.append(make_ec_q(
        qid="EC_GT_047", diff="Hard", qtype="Single-Choice", subtopic="Section 94 Elector Privilege",
        en_stem="What unique evidentiary privilege is conferred upon electors under Section 94 of the Representation of the People Act, 1951?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 94-ன் கீழ் வாக்காளர்களுக்கு வழங்கப்படும் தனித்துவமான சாட்சிய சிறப்புரிமை என்ன?",
        en_a="No person who has voted at an election shall be required to state for whom he has voted in any court or inquiry", ta_a="தேர்தலில் வாக்களித்த எந்தவொரு நபரும் தான் யாருக்கு வாக்களித்தார் என்பதை எந்த நீதிமன்றத்திலோ அல்லது விசாரணையிலோ தெரிவிக்க கட்டாயப்படுத்தப்படலாகாது",
        en_b="Electors are completely immune from arrest for any criminal offence on polling day", ta_b="தேர்தல் நாளன்று எந்தவொரு குற்றத்திற்காகவும் வாக்காளர்களைக் கைது செய்ய முழு விலக்கு உண்டு",
        en_c="Electors can vote twice if they declare a mistake on the first attempt", ta_c="முதல் முயற்சியில் தவறு நேர்ந்ததாகக் கூறினால் வாக்காளர்கள் இரண்டு முறை வாக்களிக்கலாம்",
        en_d="Electors have the right to demand manual recount of their specific ballot paper", ta_d="தங்களின் குறிப்பிட்ட வாக்குச் சீட்டை கைமுறையாக மறு எண்ணிக்கை செய்யக் கோரும் உரிமை வாக்காளர்களுக்கு உண்டு",
        correct_key="A",
        exp_en="Section 94 (Secrecy of voting not to be infringed) explicitly protects the secrecy of franchise by providing: 'No person who has voted at an election shall, in any proceeding, be required to state for whom he has voted.'",
        exp_ta="பிரிவு 94 (வாக்கு ரகசியத்தைப் பாதுகாத்தல்), 'தேர்தலில் வாக்களித்த எந்தவொரு நபரும் எந்தவொரு வழக்கிலும் தான் யாருக்கு வாக்களித்தார் என்பதைத் தெரிவிக்க கட்டாயப்படுத்தப்படக்கூடாது' என்று வாக்கு ரகசியத்தைப் பாதுகாக்கிறது.",
        why_a_en="Correct. Section 94 grants privilege of secrecy to electors.",
        why_a_ta="சரியானது. பிரிவு 94 வாக்காளர்களுக்கு வாக்கு ரகசிய சாட்சிய பாதுகாப்பை அளிக்கிறது.",
        why_b_en="Incorrect. No criminal immunity exists on poll day.",
        why_b_ta="தவறானது. குற்ற விலக்கு எதுவும் இல்லை.",
        why_c_en="Incorrect. Multiple voting is an offence under Section 62(4).",
        why_c_ta="தவறானது. ஒன்றுக்கு மேற்பட்ட முறை வாக்களிப்பது குற்றமாகும்.",
        why_d_en="Incorrect. Individual recount demand is not recognized.",
        why_d_ta="தவறானது. தனிப்பட்ட மறு எண்ணிக்கை கோர முடியாது.",
        tip_en="This privilege can only be waived voluntarily by the elector if there is no statutory prohibition.",
        tip_ta="வாக்காளரே சுயமாக முன்வந்து தெரிவித்தாலே தவிர எவரும் அவரை கட்டாயப்படுத்த முடியாது.",
        fact_en="Section 94 was upheld as an essential corollary to the purity of elections in S. Raghbir Singh Gill v. Gurcharan Singh Tohra (1980).",
        fact_ta="1980 உச்ச நீதிமன்ற தீர்ப்பில் தேர்தல் தூய்மையின் அவசியமான பகுதியாக பிரிவு 94 உறுதி செய்யப்பட்டது.",
        tags=["Section 94", "Secrecy Privilege", "Voter Protection"]
    ))

    # GT 048
    qs.append(make_ec_q(
        qid="EC_GT_048", diff="Medium", qtype="Single-Choice", subtopic="Section 129 Prohibitions",
        en_stem="Under Section 129 of RPA 1951, which of the following acts is strictly prohibited for any officer or staff performing election duty?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 129-ன் கீழ், தேர்தல் பணியில் ஈடுபடும் எந்தவொரு அதிகாரி அல்லது ஊழியருக்கும் பின்வரும் எந்த செயல் கண்டிப்பாகத் தடை செய்யப்பட்டுள்ளது?",
        en_a="Canvassing for any candidate, indicating how to vote, or attempting to influence the voting of any elector", ta_a="எந்தவொரு வேட்பாளருக்காகவும் வாக்கு சேகரித்தல், எவ்வாறு வாக்களிக்க வேண்டும் எனக் கூறுதல், அல்லது வாக்காளரை செல்வாக்கு செலுத்த முயற்சித்தல்",
        en_b="Travelling by public transport to reach the polling booth", ta_b="வாக்குச்சாவடியை அடைய பொது போக்குவரத்தில் பயணம் செய்தல்",
        en_c="Verifying the identity card of the voter", ta_c="வாக்காளரின் அடையாள அட்டையை சரிபார்த்தல்",
        en_d="Announcing the hourly poll turnout percentage to the media", ta_d="மணிநேர வாக்குப்பதிவு சதவீதத்தை ஊடகங்களுக்கு அறிவித்தல்",
        correct_key="A",
        exp_en="Section 129 prohibits returning officers, presiding officers, and polling staff from acting for any candidate, canvassing, or influencing the result. Violation is punishable with imprisonment up to 6 months, or fine, or both.",
        exp_ta="பிரிவு 129, தேர்தல் பணியாளர்கள் எந்தவொரு வேட்பாளருக்காகவும் செயல்படுவதையோ, பிரச்சாரம் செய்வதையோ அல்லது முடிவுகளை திசைதிருப்ப முயற்சிப்பதையோ தடை செய்கிறது; மீறினால் 6 மாதம் வரை சிறை தண்டனை உண்டு.",
        why_a_en="Correct. Canvassing or influencing electors by election staff is strictly barred.",
        why_a_ta="சரியானது. தேர்தல் பணியாளர்கள் பிரச்சாரம் செய்வது அல்லது செல்வாக்கு செலுத்துவது தடை செய்யப்பட்டுள்ளது.",
        why_b_en="Incorrect. Public transport is permitted.",
        why_b_ta="தவறானது. பொது போக்குவரத்து அனுமதிக்கப்படுகிறது.",
        why_c_en="Incorrect. Identity verification is a mandatory duty under Rule 49L.",
        why_c_ta="தவறானது. அடையாள சரிபார்ப்பு அவர்களின் சட்டப்பூர்வ கடமையாகும்.",
        why_d_en="Incorrect. Reporting turnout is lawful official duty.",
        why_d_ta="தவறானது. வாக்குப்பதிவு சதவீதத்தை தெரிவிப்பது உத்தியோகபூர்வ பணியாகும்.",
        tip_en="Officers violating Section 129 also face disciplinary suspension and departmental dismissal.",
        tip_ta="பிரிவு 129-ஐ மீறும் அதிகாரிகள் துறைசார் பணிநீக்கத்தையும் எதிர்கொள்வர்.",
        fact_en="Section 129 ensures absolute neutrality and non-partisanship of the civil administrative apparatus during polls.",
        fact_ta="தேர்தல் நேரத்தில் அரசு இயந்திரத்தின் நடுநிலைமையை பிரிவு 129 உறுதி செய்கிறது.",
        tags=["Section 129", "Officer Neutrality", "Canvassing Bar"]
    ))

    # GT 049
    qs.append(make_ec_q(
        qid="EC_GT_049", diff="Easy", qtype="Single-Choice", subtopic="Section 133 Vehicles",
        en_stem="Under Section 133 of RPA 1951, what is the penalty for illegally hiring or procuring vehicles for the conveyance of electors to or from polling stations?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 133-ன் கீழ், வாக்காளர்களை வாக்குச்சாவடிகளுக்கு அழைத்து வர அல்லது திருப்பி அனுப்ப சட்டவிரோதமாக வாகனங்களை வாடகைக்கு எடுப்பதற்கான தண்டனை என்ன?",
        en_a="Fine of up to Rs. 1,000 and imprisonment up to three months", ta_a="ரூ. 1,000 வரை அபராதம் மற்றும் மூன்று மாதங்கள் வரை சிறை",
        en_b="Fine of Rs. 100,000 only", ta_b="ரூ. 100,000 அபராதம் மட்டும்",
        en_c="Permanent seizure of the vehicle and auction by State Government", ta_c="வாகனத்தை நிரந்தரமாக பறிமுதல் செய்து மாநில அரசால் ஏலம் விடுதல்",
        en_d="Disqualification of the driver from driving for 10 years", ta_d="ஓட்டுநரை 10 ஆண்டுகளுக்கு வாகனம் ஓட்ட தடை விதித்தல்",
        correct_key="A",
        exp_en="Section 133 provides that if any person is guilty of any corrupt practice specified in clause (5) of Section 123 (hiring/conveying voters in vehicles), he shall be punishable with imprisonment up to 3 months and fine.",
        exp_ta="பிரிவு 133-ன் படி, வாக்காளர்களை வாகனங்களில் அழைத்து வரும் ஊழல் நடைமுறையில் ஈடுபடும் நபருக்கு 3 மாதங்கள் வரை சிறை மற்றும் அபராதம் விதிக்கப்படும்.",
        why_a_en="Correct. Section 133 penalizes conveyance of voters with imprisonment up to 3 months and fine.",
        why_a_ta="சரியானது. பிரிவு 133 வாக்காளர்களை வாகனங்களில் ஏற்றி வருவதற்கு 3 மாத சிறை மற்றும் அபராதம் விதிக்கிறது.",
        why_b_en="Incorrect. Rs. 100,000 is incorrect.",
        why_b_ta="தவறானது. ரூ. 100,000 அல்ல.",
        why_c_en="Incorrect. Permanent auction is not provided under Section 133.",
        why_c_ta="தவறானது. நிரந்தர ஏலம் இதில் இல்லை.",
        why_d_en="Incorrect. Driver suspension is under Motor Vehicles Act, not Section 133.",
        why_d_ta="தவறானது. இது மோட்டார் வாகனச் சட்டத்தின் கீழ் வராது.",
        tip_en="Candidates and their agents are permitted only a fixed quota of vehicles with official ECI permits on polling day.",
        tip_ta="வாக்குப்பதிவு நாளன்று வேட்பாளர்களுக்கு குறிப்பிட்ட எண்ணிக்கையிலான அனுமதிக்கப்பட்ட வாகனங்கள் மட்டுமே அனுமதிக்கப்படுகின்றன.",
        fact_en="Private vehicles conveying family members of the vehicle owner are exempt from this prohibition.",
        fact_ta="வாகன உரிமையாளரின் சொந்தக் குடும்ப உறுப்பினர்களை அழைத்து வர இதற்கு விலக்கு உண்டு.",
        tags=["Section 133", "Conveyance of Voters", "Illegal Vehicles"]
    ))

    # GT 050
    qs.append(make_ec_q(
        qid="EC_GT_050", diff="Hard", qtype="Single-Choice", subtopic="Section 135A Booth Capturing",
        en_stem="Under Section 135A of RPA 1951, what is the maximum imprisonment prescribed for a person in government service who commits the offence of booth capturing?",
        ta_stem="1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 135A-ன் கீழ், அரசுப் பணியில் உள்ள ஒருவர் வாக்குச்சாவடி கைப்பற்றுதல் குற்றத்தில் ஈடுபட்டால் விதிக்கப்படும் அதிகபட்ச சிறைத்தண்டனை என்ன?",
        en_a="Imprisonment for not less than three years, which may extend up to five years, and with fine", ta_a="மூன்று ஆண்டுகளுக்குக் குறையாத, ஐந்து ஆண்டுகள் வரை நீட்டிக்கப்படக்கூடிய சிறைத்தண்டனை மற்றும் அபராதம்",
        en_b="Imprisonment for not less than one year, extending up to three years", ta_b="ஒரு ஆண்டுக்குக் குறையாத, மூன்று ஆண்டுகள் வரை நீட்டிக்கப்படக்கூடிய சிறை",
        en_c="Simple imprisonment for six months only", ta_c="ஆறு மாதங்கள் எளிய சிறை மட்டுமே",
        en_d="Life imprisonment and forfeiture of all personal properties", ta_d="ஆயுள் சிறை மற்றும் அனைத்து சொத்துக்களையும் பறிமுதல் செய்தல்",
        correct_key="A",
        exp_en="Section 135A(1) provides that if booth capturing is committed by a person in the service of the Government, he shall be punishable with imprisonment for a term which shall not be less than 3 years but which may extend to 5 years, and with fine (for others, not less than 1 year up to 3 years).",
        exp_ta="பிரிவு 135A(1)-ன் படி, அரசு ஊழியர் வாக்குச்சாவடி கைப்பற்றுதலில் ஈடுபட்டால் 3 ஆண்டுகளுக்குக் குறையாத மற்றும் 5 ஆண்டுகள் வரை நீட்டிக்கப்படக்கூடிய சிறைத்தண்டனை விதிக்கப்படும் (பிற நபர்களுக்கு 1 முதல் 3 ஆண்டுகள்).",
        why_a_en="Correct. 3 to 5 years for government servants committing booth capturing.",
        why_a_ta="சரியானது. அரசு ஊழியருக்கு 3 முதல் 5 ஆண்டுகள் வரை சிறைத்தண்டனை.",
        why_b_en="Incorrect. 1 to 3 years applies to non-government citizens.",
        why_b_ta="தவறானது. 1 முதல் 3 ஆண்டுகள் என்பது சாதாரண நபர்களுக்குப் பொருந்தும்.",
        why_c_en="Incorrect. 6 months is far too low.",
        why_c_ta="தவறானது. 6 மாதம் மிகக் குறைவு.",
        why_d_en="Incorrect. Life imprisonment is not prescribed.",
        why_d_ta="தவறானது. ஆயுள் தண்டனை இதில் இல்லை.",
        tip_en="Section 135A was inserted in 1989 following pervasive booth capturing incidents in the 1980s.",
        tip_ta="1980-களில் நிகழ்ந்த வாக்குச்சாவடி கைப்பற்றல்களைத் தடுக்க 1989-ல் பிரிவு 135A கொண்டுவரப்பட்டது.",
        fact_en="Section 135A defines booth capturing broadly to include seizing polling stations, threatening electors, and preventing polling staff from performing duty.",
        fact_ta="வாக்குச்சாவடியைக் கைப்பற்றுவது, வாக்காளர்களை அச்சுறுத்துவது, அதிகாரிகளைத் தடுப்பது அனைத்தும் இக்குற்றத்தில் அடங்கும்.",
        tags=["Section 135A", "Booth Capturing", "Severe Penalties"]
    ))

    return qs
