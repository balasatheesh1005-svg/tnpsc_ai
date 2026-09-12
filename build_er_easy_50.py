# -*- coding: utf-8 -*-
"""
Builder for Electoral Reforms Easy 50 MCQs (ER_E_001 to ER_E_050).
Strictly adheres to the 24-field TNPSC Nova AI schema.
"""

import json
import os
from er_mcq_helper import make_er_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

OUTPUT_PATH = os.path.join("data", "questions", "polity", "electoral_reforms_easy.json")

def get_easy_questions():
    qs = []

    # ER_E_001
    qs.append(make_er_q(
        qid="ER_E_001", diff="Easy", qtype="Single-Choice", subtopic="Voting Age Reform",
        en_stem="Which Constitutional Amendment Act reduced the minimum voting age in India from 21 years to 18 years?",
        ta_stem="இந்தியாவில் வாக்களிக்கும் குறைந்தபட்ச வயதை 21-லிருந்து 18 ஆகக் குறைத்த அரசியலமைப்புச் சட்டத் திருத்தம் எது?",
        en_a="61st Constitutional Amendment Act, 1988", ta_a="61-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1988",
        en_b="42nd Constitutional Amendment Act, 1976", ta_b="42-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1976",
        en_c="44th Constitutional Amendment Act, 1978", ta_c="44-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1978",
        en_d="73rd Constitutional Amendment Act, 1992", ta_d="73-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1992",
        correct_key="A",
        exp_en="The 61st Constitutional Amendment Act, 1988 amended Article 326 to reduce the voting age for Lok Sabha and State Legislative Assemblies from 21 to 18 years. It came into force on 28 March 1989.",
        exp_ta="61-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1988 சரத்து 326-ஐத் திருத்தி, மக்களவை மற்றும் மாநில சட்டசபைத் தேர்தல்களுக்கான வாக்களிக்கும் வயதை 21-லிருந்து 18 ஆகக் குறைத்தது. இது 1989 மார்ச் 28 அன்று நடைமுறைக்கு வந்தது.",
        why_a_en="Correct. 61st Amendment Act, 1988 reduced the voting age to 18.",
        why_a_ta="சரியானது. 61-வது திருத்தச் சட்டம் வாக்களிக்கும் வயதை 18 ஆகக் குறைத்தது.",
        why_b_en="Incorrect. 42nd Amendment Act, 1976 is the Mini-Constitution that froze delimitation until 2000.",
        why_b_ta="தவறானது. 42-வது திருத்தம் தொகுதி மறுவரையறையை 2000 வரை முடக்கியது.",
        why_c_en="Incorrect. 44th Amendment Act, 1978 restored various democratic safeguards after the Emergency.",
        why_c_ta="தவறானது. 44-வது திருத்தம் அவசரநிலைக்குப் பிந்தைய ஜனநாயக பாதுகாப்புகளை மீட்டெடுத்தது.",
        why_d_en="Incorrect. 73rd Amendment Act, 1992 gave constitutional status to Panchayati Raj.",
        why_d_ta="தவறானது. 73-வது திருத்தம் பஞ்சாயத்து அமைப்புகளுக்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
        tip_en="Remember: 61st Amendment was passed in 1988 but came into force on March 28, 1989 during Rajiv Gandhi's tenure.",
        tip_ta="நினைவில் கொள்க: 61-வது திருத்தம் 1988-ல் நிறைவேற்றப்பட்டு, 1989 மார்ச் 28 முதல் நடைமுறைக்கு வந்தது.",
        fact_en="Article 326 deals with adult suffrage for elections to the Lok Sabha and Legislative Assemblies.",
        fact_ta="சரத்து 326 மக்களவை மற்றும் மாநில சட்டசபைகளுக்கான வயதுவந்தோர் வாக்குரிமையைக் கையாள்கிறது.",
        tags=["61st Amendment", "Voting Age", "Article 326"]
    ))

    # ER_E_002
    qs.append(make_er_q(
        qid="ER_E_002", diff="Easy", qtype="Single-Choice", subtopic="Committees on Electoral Reforms",
        en_stem="The Tarkunde Committee (1974) on electoral reforms was appointed by which prominent national leader?",
        ta_stem="தேர்தல் சீர்திருத்தங்கள் குறித்த தர்குண்டே குழு (1974) எந்த முக்கிய தேசியத் தலைவரால் நியமிக்கப்பட்டது?",
        en_a="Jayaprakash Narayan", ta_a="ஜெயபிரகாஷ் நாராயணன்",
        en_b="Morarji Desai", ta_b="மொரார்ஜி தேசாய்",
        en_c="Indira Gandhi", ta_c="இந்திரா காந்தி",
        en_d="Charan Singh", ta_d="சரண் சிங்",
        correct_key="A",
        exp_en="The Tarkunde Committee (Committee on Electoral Reforms) was set up in 1974 by Loknayak Jayaprakash Narayan on behalf of the 'Citizens for Democracy'. It submitted its report in 1975 recommending reducing the voting age to 18 and an independent multi-member Election Commission.",
        exp_ta="தர்குண்டே குழு (தேர்தல் சீர்திருத்தக் குழு) 1974-ல் லோக்நாயக் ஜெயபிரகாஷ் நாராயணனால் 'மக்களாட்சிக்கான குடிமக்கள்' (Citizens for Democracy) அமைப்பின் சார்பில் அமைக்கப்பட்டது. இது 1975-ல் அறிக்கை சமர்ப்பித்தது.",
        why_a_en="Correct. Appointed by Jayaprakash Narayan in 1974.",
        why_a_ta="சரியானது. 1974-ல் ஜெயபிரகாஷ் நாராயணனால் நியமிக்கப்பட்டது.",
        why_b_en="Incorrect. Morarji Desai was Prime Minister from 1977-1979.",
        why_b_ta="தவறானது. மொரார்ஜி தேசாய் 1977-1979 வரை பிரதமராக இருந்தார்.",
        why_c_en="Incorrect. Indira Gandhi was the ruling Prime Minister opposed by the JP Movement.",
        why_c_ta="தவறானது. இந்திரா காந்தி அக்காலகட்டத்தில் பிரதமராக இருந்தார்.",
        why_d_en="Incorrect. Charan Singh was PM in 1979.",
        why_d_ta="தவறானது. சரண் சிங் 1979-ல் பிரதமராகப் பணியாற்றினார்.",
        tip_en="Tarkunde Committee was the first committee to formally recommend lowering voting age to 18 and a 3-member ECI.",
        tip_ta="வாக்களிக்கும் வயதை 18 ஆகக் குறைக்கவும், 3 நபர் தேர்தல் ஆணையத்தை அமைக்கவும் முதன்முதலில் பரிந்துரைத்தது தர்குண்டே குழு.",
        fact_en="Justice V.M. Tarkunde was a distinguished civil liberties activist and retired High Court judge.",
        fact_ta="நீதிபதி வி.எம். தர்குண்டே மனித உரிமைப் போராளியாகவும் உயர் நீதிமன்ற ஓய்வுபெற்ற நீதிபதியாகவும் இருந்தவர்.",
        tags=["Tarkunde Committee", "Jayaprakash Narayan", "Electoral Reforms"]
    ))

    # ER_E_003
    qs.append(make_er_q(
        qid="ER_E_003", diff="Easy", qtype="Single-Choice", subtopic="Committees on Electoral Reforms",
        en_stem="The Dinesh Goswami Committee, appointed in 1990 by the National Front government, submitted recommendations primarily on which subject?",
        ta_stem="1990-ல் தேசிய முன்னணி அரசாங்கத்தால் நியமிக்கப்பட்ட தினேஷ் கோஸ்வாமி குழு முக்கியமாக எதன் மீது பரிந்துரைகளை வழங்கியது?",
        en_a="Electoral Reforms and EVMs", ta_a="தேர்தல் சீர்திருத்தங்கள் மற்றும் வாக்குப்பதிவு இயந்திரங்கள் (EVM)",
        en_b="Centre-State Financial Relations", ta_b="மத்திய-மாநில நிதி உறவுகள்",
        en_c="Panchayati Raj 3-tier system", ta_c="பஞ்சாயத்து ராஜ் 3 அடுக்கு முறை",
        en_d="Reorganization of North-Eastern States", ta_d="வடகிழக்கு மாநிலங்கள் மறுசீரமைப்பு",
        correct_key="A",
        exp_en="The Dinesh Goswami Committee on Electoral Reforms (1990) recommended the introduction of EVMs, state assistance in kind to recognized political parties, and disqualification rules under anti-defection.",
        exp_ta="தேர்தல் சீர்திருத்தங்களுக்கான தினேஷ் கோஸ்வாமி குழு (1990) மின்னணு வாக்குப்பதிவு இயந்திரங்கள் (EVM) பயன்பாடு, அங்கீகரிக்கப்பட்ட கட்சிகளுக்குப் பொருளுதவி வழங்குதல் போன்றவற்றை பரிந்துரைத்தது.",
        why_a_en="Correct. Dinesh Goswami Committee was a landmark committee on Electoral Reforms.",
        why_a_ta="சரியானது. தினேஷ் கோஸ்வாமி குழு தேர்தல் சீர்திருத்தங்களுக்கான முக்கிய குழுவாகும்.",
        why_b_en="Incorrect. Centre-State relations were addressed by Sarkaria Commission.",
        why_b_ta="தவறானது. மத்திய-மாநில உறவுகளை சர்க்காரியா ஆணையம் ஆராய்ந்தது.",
        why_c_en="Incorrect. Panchayati Raj was studied by Balwant Rai Mehta and Ashok Mehta committees.",
        why_c_ta="தவறானது. பஞ்சாயத்து ராஜ் அமைப்பை பல்வந்த்ராய் மேத்தா குழு ஆராய்ந்தது.",
        why_d_en="Incorrect. State reorganization was dealt with by Fazal Ali Commission.",
        why_d_ta="தவறானது. மாநில மறுசீரமைப்பை ஃபசல் அலி ஆணையம் கையாண்டது.",
        tip_en="Dinesh Goswami was Union Law Minister in the V.P. Singh government in 1990.",
        tip_ta="1990-ல் வி.பி. சிங் தலைமையிலான அரசில் தினேஷ் கோஸ்வாமி மத்திய சட்ட அமைச்சராக இருந்தார்.",
        fact_en="The committee's recommendations led to the statutory sanction for EVMs under Section 61A of RPA 1951.",
        fact_ta="இக்குழுவின் பரிந்துரையே மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 61A-ன் கீழ் EVM-க்கு சட்டப்பூர்வ அங்கீகாரம் கிடைக்க வழிவகுத்தது.",
        tags=["Dinesh Goswami Committee", "Electoral Reforms", "1990"]
    ))

    # ER_E_004
    qs.append(make_er_q(
        qid="ER_E_004", diff="Easy", qtype="Single-Choice", subtopic="State Funding of Elections",
        en_stem="Which committee was exclusively appointed in 1998 to examine the issue of State Funding of Elections?",
        ta_stem="தேர்தல்களுக்கான அரசு நிதியுதவி (State Funding of Elections) குறித்து ஆராய 1998-ல் பிரத்யேகமாக அமைக்கப்பட்ட குழு எது?",
        en_a="Indrajit Gupta Committee", ta_a="இந்திரஜித் குப்தா குழு",
        en_b="Vohra Committee", ta_b="வோஹ்ரா குழு",
        en_c="Santhanam Committee", ta_c="சந்தானம் குழு",
        en_d="Kothari Commission", ta_d="கோத்தாரி ஆணையம்",
        correct_key="A",
        exp_en="The Indrajit Gupta Committee on State Funding of Elections (1998) recommended partial state funding in kind (facilities, paper, fuel, airtime) exclusively to recognized political parties.",
        exp_ta="அரசு தேர்தல் நிதியுதவி குறித்த இந்திரஜித் குப்தா குழு (1998), அங்கீகரிக்கப்பட்ட அரசியல் கட்சிகளுக்கு மட்டும் பொருளுதவி வடிவிலான பகுதி அரசு நிதியுதவியை பரிந்துரைத்தது.",
        why_a_en="Correct. Indrajit Gupta Committee (1998) dealt with state funding of elections.",
        why_a_ta="சரியானது. இந்திரஜித் குப்தா குழு (1998) தேர்தல்களுக்கான அரசு நிதியுதவி குறித்து ஆராய்ந்தது.",
        why_b_en="Incorrect. Vohra Committee (1993) dealt with the nexus between politicians and criminals.",
        why_b_ta="தவறானது. வோஹ்ரா குழு (1993) குற்றவாளிகள்-அரசியல்வாதிகள் தொடர்பை ஆராய்ந்தது.",
        why_c_en="Incorrect. Santhanam Committee (1964) recommended the Central Vigilance Commission (CVC).",
        why_c_ta="தவறானது. சந்தானம் குழு (1964) மத்திய ஊழல் கண்காணிப்பு ஆணையத்தை பரிந்துரைத்தது.",
        why_d_en="Incorrect. Kothari Commission (1964-66) dealt with national education reforms.",
        why_d_ta="தவறானது. கோத்தாரி ஆணையம் (1964-66) கல்விச் சீர்திருத்தங்களை ஆராய்ந்தது.",
        tip_en="Indrajit Gupta was a veteran parliamentarian and former Union Home Minister.",
        tip_ta="இந்திரஜித் குப்தா மூத்த நாடாளுமன்றவாதியும் முன்னாள் மத்திய உள்துறை அமைச்சருமாவார்.",
        fact_en="Indrajit Gupta Committee clearly rejected cash funding and restricted state aid strictly to kind.",
        fact_ta="பண வடிவிலான நிதியுதவியை இக்குழு நிராகரித்து, பொருளுதவி வடிவில் மட்டுமே வழங்கப்பட வேண்டும் என வலியுறுத்தியது.",
        tags=["Indrajit Gupta Committee", "State Funding", "1998"]
    ))

    # ER_E_005
    qs.append(make_er_q(
        qid="ER_E_005", diff="Easy", qtype="Single-Choice", subtopic="Criminal-Politician Nexus",
        en_stem="The Vohra Committee (1993) was constituted by the Government of India to investigate which dangerous nexus in the country?",
        ta_stem="இந்திய அரசால் அமைக்கப்பட்ட வோஹ்ரா குழு (1993), நாட்டில் நிலவும் எந்த ஆபத்தான தொடர்பை ஆராய அமைக்கப்பட்டது?",
        en_a="Nexus between crime syndicates, bureaucrats, and politicians", ta_a="குற்றக் கும்பல்கள், அரசு அதிகாரிகள் மற்றும் அரசியல்வாதிகளுக்கிடையேயான தொடர்பு",
        en_b="Nexus between banks and non-performing assets", ta_b="வங்கிகள் மற்றும் வாராக்கடன்களுக்கிடையேயான தொடர்பு",
        en_c="Nexus between private hospitals and pharmaceutical companies", ta_c="தனியார் மருத்துவமனைகள் மற்றும் மருந்து நிறுவனங்களுக்கிடையேயான தொடர்பு",
        en_d="Nexus between judiciary and civil service transfers", ta_d="நீதித்துறை மற்றும் குடிமைப்பணி இடமாற்றங்களுக்கிடையேயான தொடர்பு",
        correct_key="A",
        exp_en="The N.N. Vohra Committee submitted its report in October 1993 on the criminalisation of politics and the unholy nexus between criminals, politicians, and bureaucrats following the 1993 Mumbai serial blasts.",
        exp_ta="1993 மும்பை குண்டுவெடிப்பைத் தொடர்ந்து, என்.என். வோஹ்ரா குழு 1993 அக்டோபரில் அரசியல் குற்றமயமாதல் மற்றும் குற்றவாளிகள், அரசியல்வாதிகள், அரசு அதிகாரிகளுக்கிடையேயான ஆபத்தான தொடர்பு குறித்து அறிக்கை அளித்தது.",
        why_a_en="Correct. Vohra Committee investigated the criminal-politician-bureaucrat nexus.",
        why_a_ta="சரியானது. குற்றவாளிகள்-அரசியல்வாதிகள்-அதிகாரிகள் தொடர்பை வோஹ்ரா குழு ஆராய்ந்தது.",
        why_b_en="Incorrect. Narasimham Committee dealt with banking sector reforms.",
        why_b_ta="தவறானது. நரசிம்மம் குழு வங்கித்துறை சீர்திருத்தங்களை ஆராய்ந்தது.",
        why_c_en="Incorrect. Not related to health or pharmaceuticals.",
        why_c_ta="தவறானது. மருத்துவத் துறையுடன் தொடர்புடையது அல்ல.",
        why_d_en="Incorrect. Not related to judicial transfers.",
        why_d_ta="தவறானது. நீதித்துறை இடமாற்றங்களுடன் தொடர்புடையது அல்ல.",
        tip_en="N.N. Vohra was the Union Home Secretary when the committee was formed.",
        tip_ta="இக்குழு அமைக்கப்பட்டபோது என்.என். வோஹ்ரா மத்திய உள்துறைச் செயலாளராக இருந்தார்.",
        fact_en="The Vohra Committee report was one of the strongest triggers for judicial intervention against criminalisation of politics.",
        fact_ta="அரசியல் குற்றமயமாதலுக்கு எதிரான நீதித்துறை தலையீடுகளுக்கு வோஹ்ரா குழு அறிக்கை முக்கிய தூண்டுகோலாக அமைந்தது.",
        tags=["Vohra Committee", "Criminalisation of Politics", "1993"]
    ))

    # ER_E_006
    qs.append(make_er_q(
        qid="ER_E_006", diff="Easy", qtype="Single-Choice", subtopic="Electronic Voting Machines",
        en_stem="Electronic Voting Machines (EVMs) were first used on an experimental basis in which state during a 1982 assembly by-election?",
        ta_stem="மின்னணு வாக்குப்பதிவு இயந்திரங்கள் (EVM) 1982-ல் நடைபெற்ற சட்டசபை இடைத்தேர்தலின் போது சோதனை அடிப்படையில் முதன்முதலில் எந்த மாநிலத்தில் பயன்படுத்தப்பட்டன?",
        en_a="Kerala (Paravur Constituency)", ta_a="கேரளா (பறவூர் தொகுதி)",
        en_b="Tamil Nadu (Saidapet Constituency)", ta_b="தமிழ்நாடு (சைதாப்பேட்டை தொகுதி)",
        en_c="Karnataka (Shantinagar Constituency)", ta_c="கர்நாடகா (சாந்திநகர் தொகுதி)",
        en_d="Goa (Panaji Constituency)", ta_d="கோவா (பனாஜி தொகுதி)",
        correct_key="A",
        exp_en="EVMs were used for the first time in India in May 1982 in the by-election to the Paravur Assembly Constituency in Ernakulam district of Kerala across 50 polling stations.",
        exp_ta="இந்தியாவில் முதன்முதலில் 1982 மே மாதத்தில் கேரள மாநிலம் எர்ணாகுளம் மாவட்டத்திலுள்ள பறவூர் சட்டமன்றத் தொகுதி இடைத்தேர்தலில் 50 வாக்குச்சாவடிகளில் EVM பயன்படுத்தப்பட்டது.",
        why_a_en="Correct. Kerala's Paravur constituency was the first site of EVM usage in 1982.",
        why_a_ta="சரியானது. 1982-ல் கேரளாவின் பறவூர் தொகுதியில் முதன்முதலில் EVM பயன்படுத்தப்பட்டது.",
        why_b_en="Incorrect. Tamil Nadu used EVMs widely in later years, not in 1982.",
        why_b_ta="தவறானது. தமிழ்நாட்டில் பிற்காலத்தில் பயன்படுத்தப்பட்டது.",
        why_c_en="Incorrect. Karnataka was not the first state.",
        why_c_ta="தவறானது. கர்நாடகா முதல் மாநிலம் அல்ல.",
        why_d_en="Incorrect. Goa was the first state to conduct an entire assembly election using EVMs in 1999.",
        why_d_ta="தவறானது. கோவா 1999-ல் முழு சட்டசபைத் தேர்தலையும் EVM மூலம் நடத்திய முதல் மாநிலமாகும்.",
        tip_en="Do not confuse: First experimental use was Paravur, Kerala (1982); first entire state election using EVMs was Goa (1999).",
        tip_ta="குழப்ப வேண்டாம்: முதல் சோதனை பயன்பாடு பறவூர், கேரளா (1982); மாநிலம் முழுவதும் EVM பயன்படுத்திய முதல் மாநிலம் கோவா (1999).",
        fact_en="The Supreme Court in A.C. Jose v. Sivan Pillai (1984) initially struck down the 1982 election because EVMs lacked statutory backing at that time.",
        fact_ta="1984-ல் ஏ.சி. ஜோஸ் வழக்கில் உச்ச நீதிமன்றம் சட்ட அங்கீகாரம் இல்லாததால் 1982 பறவூர் தேர்தல் முடிவை ரத்து செய்தது.",
        tags=["EVM", "Kerala", "Paravur", "1982"]
    ))

    # ER_E_007
    qs.append(make_er_q(
        qid="ER_E_007", diff="Easy", qtype="Single-Choice", subtopic="Electronic Voting Machines",
        en_stem="Which state became the first in India to conduct general elections to its entire Legislative Assembly using only EVMs in 1999?",
        ta_stem="1999-ல் தனது மாநில சட்டசபை பொதுத்தேர்தல் முழுவதையும் EVM மூலம் மட்டுமே நடத்திய இந்தியாவின் முதல் மாநிலம் எது?",
        en_a="Goa", ta_a="கோவா",
        en_b="Kerala", ta_b="கேரளா",
        en_c="Sikkim", ta_c="சிக்கிம்",
        en_d="Delhi", ta_d="டெல்லி",
        correct_key="A",
        exp_en="In June 1999, Goa became the first state in India where elections to the entire 40-member State Legislative Assembly were conducted exclusively using EVMs.",
        exp_ta="1999 ஜூன் மாதம் நடைபெற்ற சட்டமன்றத் தேர்தலில், 40 தொகுதிகள் கொண்ட தனது முழு சட்டசபைக்கும் EVM மூலம் மட்டுமே தேர்தலை நடத்திய முதல் மாநிலமாக கோவா திகழ்கிறது.",
        why_a_en="Correct. Goa conducted the entire assembly election using EVMs in June 1999.",
        why_a_ta="சரியானது. 1999 ஜூன் மாதம் கோவா மாநிலம் முழுவதும் EVM மூலம் தேர்தல் நடத்தியது.",
        why_b_en="Incorrect. Kerala used it first experimentally in 1982 for one constituency.",
        why_b_ta="தவறானது. கேரளா 1982-ல் ஒரு தொகுதியில் மட்டுமே சோதனை முறையில் பயன்படுத்தியது.",
        why_c_en="Incorrect. Sikkim was not the first state.",
        why_c_ta="தவறானது. சிக்கிம் முதல் மாநிலம் அல்ல.",
        why_d_en="Incorrect. Delhi used EVMs in select constituencies in 1998.",
        why_d_ta="தவறானது. டெல்லி 1998-ல் குறிப்பிட்ட சில தொகுதிகளில் பயன்படுத்தியது.",
        tip_en="Goa 1999 = First entire State Assembly; 2004 Lok Sabha = First nationwide General Election using EVMs.",
        tip_ta="கோவா 1999 = முழு சட்டசபைத் தேர்தல்; 2004 மக்களவைத் தேர்தல் = நாடு தழுவிய முதல் EVM தேர்தல்.",
        fact_en="All 543 parliamentary constituencies used EVMs for the first time in the 14th Lok Sabha elections in 2004.",
        fact_ta="2004-ல் நடைபெற்ற 14-வது மக்களவைத் தேர்தலில் அனைத்து 543 தொகுதிகளிலும் EVM முதன்முறையாக முழுமையாகப் பயன்படுத்தப்பட்டது.",
        tags=["Goa", "EVM", "1999", "First State"]
    ))

    # ER_E_008
    qs.append(make_er_q(
        qid="ER_E_008", diff="Easy", qtype="Single-Choice", subtopic="Electronic Voting Machines",
        en_stem="Which section was inserted into the Representation of the People Act, 1951 to give statutory sanction for the use of EVMs in elections?",
        ta_stem="தேர்தல்களில் EVM பயன்பாட்டிற்கு சட்டப்பூர்வ அங்கீகாரம் வழங்குவதற்காக மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ல் சேர்க்கப்பட்ட பிரிவு எது?",
        en_a="Section 61A", ta_a="பிரிவு 61A",
        en_b="Section 29A", ta_b="பிரிவு 29A",
        en_c="Section 77", ta_c="பிரிவு 77",
        en_d="Section 123", ta_d="பிரிவு 123",
        correct_key="A",
        exp_en="Section 61A was inserted into the Representation of the People Act, 1951 by Parliament with effect from 15 March 1989, empowering the Election Commission to specify constituencies where voting machines may be used.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ல் 1989 மார்ச் 15 முதல் அமலுக்கு வரும் வகையில் பிரிவு 61A சேர்க்கப்பட்டு, வாக்குப்பதிவு இயந்திரங்களைப் பயன்படுத்த தேர்தல் ஆணையத்திற்கு சட்டப்பூர்வ அதிகாரம் அளிக்கப்பட்டது.",
        why_a_en="Correct. Section 61A provides statutory backing for EVMs.",
        why_a_ta="சரியானது. பிரிவு 61A EVM பயன்பாட்டிற்கு சட்ட அங்கீகாரம் அளிக்கிறது.",
        why_b_en="Incorrect. Section 29A provides for registration of political parties.",
        why_b_ta="தவறானது. பிரிவு 29A அரசியல் கட்சிகளின் பதிவு பற்றியது.",
        why_c_en="Incorrect. Section 77 deals with maintenance of election expenditure accounts.",
        why_c_ta="தவறானது. பிரிவு 77 தேர்தல் செலவுக் கணக்குகளைப் பராமரிப்பது பற்றியது.",
        why_d_en="Incorrect. Section 123 defines corrupt practices in elections.",
        why_d_ta="தவறானது. பிரிவு 123 ஊழல் மற்றும் முறைகேடான நடைமுறைகளை வரையறுக்கிறது.",
        tip_en="Section 61A was introduced by the Rajiv Gandhi government via an amendment act in December 1988.",
        tip_ta="1988 டிசம்பர் சட்டத்திருத்தத்தின் மூலம் பிரிவு 61A சேர்க்கப்பட்டது.",
        fact_en="Before Section 61A, the Supreme Court had ruled that the word 'ballot' in RPA 1951 referred only to paper ballots.",
        fact_ta="பிரிவு 61A வருவதற்கு முன் 'வாக்குச்சீட்டு' என்பது காகித வாக்குச்சீட்டை மட்டுமே குறிக்கும் என உச்ச நீதிமன்றம் தீர்ப்பளித்திருந்தது.",
        tags=["Section 61A", "RPA 1951", "EVM Legal Backing"]
    ))

    # ER_E_009
    qs.append(make_er_q(
        qid="ER_E_009", diff="Easy", qtype="Single-Choice", subtopic="VVPAT",
        en_stem="What does the acronym 'VVPAT' stand for in the Indian electoral system?",
        ta_stem="இந்திய தேர்தல் அமைப்பில் 'VVPAT' என்ற சுருக்கத்தின் விரிவாக்கம் என்ன?",
        en_a="Voter Verifiable Paper Audit Trail", ta_a="Voter Verifiable Paper Audit Trail (வாக்காளர் சரிபார்க்கும் காகித தணிக்கைத் தடம்)",
        en_b="Voting Verification Paper Action Track", ta_b="Voting Verification Paper Action Track",
        en_c="Valid Voter Paper Assessment Tool", ta_c="Valid Voter Paper Assessment Tool",
        en_d="Verified Voter Polling Audit Terminal", ta_d="Verified Voter Polling Audit Terminal",
        correct_key="A",
        exp_en="VVPAT stands for Voter Verifiable Paper Audit Trail. It is an independent verification printer system attached to the EVM that generates a paper slip confirming the candidate and symbol for which the vote was cast.",
        exp_ta="VVPAT என்பதன் விரிவாக்கம் 'Voter Verifiable Paper Audit Trail' ஆகும். இது EVM உடன் இணைக்கப்பட்ட ஒரு காகித அச்சு அமைப்பாகும்; வாக்காளர் யாருக்கு வாக்களித்தார் என்பதை சின்னத்துடன் அச்சிட்டுக் காட்டும்.",
        why_a_en="Correct. Voter Verifiable Paper Audit Trail.",
        why_a_ta="சரியானது. Voter Verifiable Paper Audit Trail.",
        why_b_en="Incorrect. Action Track is incorrect.",
        why_b_ta="தவறானது. தவறான விரிவாக்கம்.",
        why_c_en="Incorrect. Assessment Tool is incorrect.",
        why_c_ta="தவறானது. தவறான விரிவாக்கம்.",
        why_d_en="Incorrect. Polling Audit Terminal is incorrect.",
        why_d_ta="தவறானது. தவறான விரிவாக்கம்.",
        tip_en="VVPAT displays the printed slip to the voter for precisely 7 seconds behind a transparent window.",
        tip_ta="VVPAT இயந்திரம் அச்சிடப்பட்ட சீட்டை 7 வினாடிகள் கண்ணாடித் திரைக்குப் பின்னால் வாக்காளருக்குக் காட்டும்.",
        fact_en="After 7 seconds, the slip automatically cuts and falls into the sealed drop box of the VVPAT.",
        fact_ta="7 வினாடிகளுக்குப் பிறகு சீட்டு தானாக துண்டிக்கப்பட்டு VVPAT-ன் சீலிடப்பட்ட பெட்டிக்குள் விழும்.",
        tags=["VVPAT", "Definition", "Electoral Reforms"]
    ))

    # ER_E_010
    qs.append(make_er_q(
        qid="ER_E_010", diff="Easy", qtype="Single-Choice", subtopic="VVPAT",
        en_stem="In which constituency was VVPAT used for the very first time in India during a September 2013 by-election?",
        ta_stem="2013 செப்டம்பரில் நடைபெற்ற இடைத்தேர்தலின் போது இந்தியாவில் முதன்முதலில் VVPAT பயன்படுத்தப்பட்ட சட்டமன்றத் தொகுதி எது?",
        en_a="Noksen (Nagaland)", ta_a="நோக்சென் (நாகாலாந்து)",
        en_b="Aravakurichi (Tamil Nadu)", ta_b="அரவக்குறிச்சி (தமிழ்நாடு)",
        en_c="Nanded (Maharashtra)", ta_c="நாந்தேடு (மகாராஷ்டிரா)",
        en_d="Bellary (Karnataka)", ta_d="பெல்லாரி (கர்நாடகா)",
        correct_key="A",
        exp_en="VVPAT was first introduced in India in the by-election to the Noksen Assembly Constituency in Tuensang district of Nagaland in September 2013.",
        exp_ta="2013 செப்டம்பர் மாதம் நாகாலாந்து மாநிலத்தின் துயென்சாங் மாவட்டத்திலுள்ள நோக்சென் சட்டமன்றத் தொகுதி இடைத்தேர்தலில் முதன்முதலில் VVPAT பயன்படுத்தப்பட்டது.",
        why_a_en="Correct. Noksen assembly constituency in Nagaland (2013).",
        why_a_ta="சரியானது. நாகாலாந்தின் நோக்சென் சட்டமன்றத் தொகுதி (2013).",
        why_b_en="Incorrect. Aravakurichi used VVPAT in later elections.",
        why_b_ta="தவறானது. அரவக்குறிச்சியில் பிற்காலத்தில் பயன்படுத்தப்பட்டது.",
        why_c_en="Incorrect. Nanded was not the first.",
        why_c_ta="தவறானது. நாந்தேடு முதன்மையானது அல்ல.",
        why_d_en="Incorrect. Bellary was not the first.",
        why_d_ta="தவறானது. பெல்லாரி முதன்மையானது அல்ல.",
        tip_en="Remember the sequence: First EVM = Paravur (Kerala, 1982); First VVPAT = Noksen (Nagaland, 2013).",
        tip_ta="வரிசையை நினைவில் கொள்க: முதல் EVM = பறவூர் (கேரளா, 1982); முதல் VVPAT = நோக்சென் (நாகாலாந்து, 2013).",
        fact_en="The Conduct of Elections Rules, 1961 were amended on 14 August 2013 to legally introduce VVPAT.",
        fact_ta="1961 தேர்தல் நடத்தை விதிகள் 2013 ஆகஸ்ட் 14 அன்று திருத்தப்பட்டு VVPAT சட்டப்பூர்வமாக அறிமுகப்படுத்தப்பட்டது.",
        tags=["VVPAT", "Noksen", "Nagaland", "2013"]
    ))

    # ER_E_011
    qs.append(make_er_q(
        qid="ER_E_011", diff="Easy", qtype="Single-Choice", subtopic="VVPAT",
        en_stem="For how many seconds does the printed paper slip remain visible to the voter in a VVPAT machine before falling into the sealed compartment?",
        ta_stem="VVPAT இயந்திரத்தில் அச்சிடப்பட்ட காகித சீட்டு சீலிடப்பட்ட பெட்டிக்குள் விழுவதற்கு முன் எத்தனை வினாடிகள் வாக்காளருக்குத் தெரியும் வகையில் காட்சிப்படுத்தப்படுகிறது?",
        en_a="7 seconds", ta_a="7 வினாடிகள்",
        en_b="3 seconds", ta_b="3 வினாடிகள்",
        en_c="15 seconds", ta_c="15 வினாடிகள்",
        en_d="10 seconds", ta_d="10 வினாடிகள்",
        correct_key="A",
        exp_en="The printed VVPAT paper slip remains visible through a transparent glass viewing window for exactly 7 seconds, showing the candidate's serial number, name, and symbol, after which it is cut and dropped into the collection box.",
        exp_ta="அச்சிடப்பட்ட VVPAT சீட்டு வெளிப்படையான கண்ணாடித் திரை வழியாக வேட்பாளரின் வரிசை எண், பெயர், சின்னம் ஆகியவற்றுடன் சரியாக 7 வினாடிகள் காட்சியளிக்கும். பின்னர் அது வெட்டப்பட்டு பெட்டியில் விழும்.",
        why_a_en="Correct. Exactly 7 seconds.",
        why_a_ta="சரியானது. சரியாக 7 வினாடிகள்.",
        why_b_en="Incorrect. 3 seconds is too short.",
        why_b_ta="தவறானது. 3 வினாடிகள் மிகவும் குறைவு.",
        why_c_en="Incorrect. 15 seconds is incorrect.",
        why_c_ta="தவறானது. 15 வினாடிகள் தவறானது.",
        why_d_en="Incorrect. 10 seconds is incorrect.",
        why_d_ta="தவறானது. 10 வினாடிகள் தவறானது.",
        tip_en="7 seconds is an exact technical specification mandated by the Technical Expert Committee (TEC) of ECI.",
        tip_ta="7 வினாடிகள் என்பது தேர்தல் ஆணையத்தின் தொழில்நுட்ப வல்லுநர் குழுவால் (TEC) நிர்ணயிக்கப்பட்ட அளவாகும்.",
        fact_en="The slip contains three vital details: Serial Number, Name of Candidate, and Party/Election Symbol.",
        fact_ta="அச்சீட்டில் வேட்பாளரின் வரிசை எண், பெயர் மற்றும் தேர்தல் சின்னம் ஆகிய 3 தகவல்கள் இருக்கும்.",
        tags=["VVPAT", "7 seconds", "Technical Specification"]
    ))

    # ER_E_012
    qs.append(make_er_q(
        qid="ER_E_012", diff="Easy", qtype="Single-Choice", subtopic="NOTA",
        en_stem="In which landmark judgment did the Supreme Court of India direct the Election Commission to introduce the 'None of the Above' (NOTA) option on EVMs?",
        ta_stem="எந்த வரலாற்று சிறப்புமிக்க தீர்ப்பில் இந்திய உச்ச நீதிமன்றம் EVM இயந்திரங்களில் 'மேற்கண்ட எவருமில்லை' (NOTA) பொத்தானை அறிமுகப்படுத்த தேர்தல் ஆணையத்திற்கு உத்தரவிட்டது?",
        en_a="PUCL v. Union of India (2013)", ta_a="PUCL எதிர் இந்திய ஒன்றியம் (2013)",
        en_b="Lily Thomas v. Union of India (2013)", ta_b="லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (2013)",
        en_c="Indira Nehru Gandhi v. Raj Narain (1975)", ta_c="இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975)",
        en_d="S.R. Bommai v. Union of India (1994)", ta_d="எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994)",
        correct_key="A",
        exp_en="In People's Union for Civil Liberties (PUCL) v. Union of India (September 27, 2013), the Supreme Court bench headed by CJI P. Sathasivam directed ECI to provide a NOTA option on ballot papers and EVMs to uphold the voter's right to express rejection secretly under Article 19(1)(a).",
        exp_ta="மக்கள் சிவில் உரிமைகள் சங்கம் (PUCL) எதிர் இந்திய ஒன்றியம் (27 செப்டம்பர் 2013) வழக்கில், தலைமை நீதிபதி ப. சதாசிவம் தலைமையிலான அமர்வு, வாக்காளரின் ரகசிய நிராகரிப்பு உரிமையைப் பாதுகாக்க NOTA பொத்தானை வழங்க உத்தரவிட்டது.",
        why_a_en="Correct. PUCL v. Union of India (2013) introduced NOTA.",
        why_a_ta="சரியானது. PUCL எதிர் இந்திய ஒன்றியம் (2013) NOTA-வை அறிமுகப்படுத்தியது.",
        why_b_en="Incorrect. Lily Thomas (2013) struck down Section 8(4) of RPA 1951 (convicted legislators disqualification).",
        why_b_ta="தவறானது. லில்லி தாமஸ் வழக்கு குற்றவாளிகளான மக்கள் பிரதிநிதிகள் தகுதிநீக்கம் பற்றியது.",
        why_c_en="Incorrect. Indira Gandhi case (1975) established free and fair elections as part of the Basic Structure.",
        why_c_ta="தவறானது. இந்திரா காந்தி வழக்கு சுதந்திரமான நியாயமான தேர்தலை அடிப்படை கட்டமைப்பு என அறிவித்தது.",
        why_d_en="Incorrect. S.R. Bommai case (1994) dealt with Article 356 (President's Rule).",
        why_d_ta="தவறானது. எஸ்.ஆர். பொம்மை வழக்கு குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) பற்றியது.",
        tip_en="CJI P. Sathasivam authored the landmark NOTA judgment in 2013.",
        tip_ta="2013-ல் வரலாற்று சிறப்புமிக்க NOTA தீர்ப்பை வழங்கியவர் தலைமை நீதிபதி ப. சதாசிவம்.",
        fact_en="Prior to NOTA, voters who wished to reject all candidates had to record it openly in Form 17A under Rule 49-O, violating secrecy.",
        fact_ta="NOTA வருவதற்கு முன், விதி 49-O-ன் கீழ் படிவம் 17A-ல் கையொப்பமிட்டு பகிரங்கமாக பதிவு செய்ய வேண்டியிருந்தது, இது ரகசியத்தன்மையை பாதித்தது.",
        tags=["NOTA", "PUCL Case", "Supreme Court 2013"]
    ))

    # ER_E_013
    qs.append(make_er_q(
        qid="ER_E_013", diff="Easy", qtype="Single-Choice", subtopic="NOTA",
        en_stem="Who designed the official symbol for NOTA ('None of the Above') introduced by the Election Commission of India in 2015?",
        ta_stem="2015-ல் இந்திய தேர்தல் ஆணையத்தால் அறிமுகப்படுத்தப்பட்ட NOTA-வுக்கான அதிகாரப்பூர்வ சின்னத்தை வடிவமைத்த நிறுவனம் எது?",
        en_a="National Institute of Design (NID), Ahmedabad", ta_a="தேசிய வடிவமைப்பு நிறுவனம் (NID), அகமதாபாத்",
        en_b="IIT Bombay (IDC)", ta_b="ஐஐடி பம்பாய் (IDC)",
        en_c="National Institute of Fashion Technology (NIFT), New Delhi", ta_c="தேசிய பேஷன் தொழில்நுட்ப நிறுவனம் (NIFT), புது தில்லி",
        en_d="National School of Drama (NSD), New Delhi", ta_d="தேசிய நாடகப் பள்ளி (NSD), புது தில்லி",
        correct_key="A",
        exp_en="The official NOTA symbol, featuring a ballot paper with a black cross mark across it, was designed by the National Institute of Design (NID), Ahmedabad, and introduced by ECI on 18 September 2015.",
        exp_ta="வாக்குச்சீட்டின் மீது கருப்பு பெருக்கல் குறி இடப்பட்ட அதிகாரப்பூர்வ NOTA சின்னம், அகமதாபாத்திலுள்ள தேசிய வடிவமைப்பு நிறுவனத்தால் (NID) வடிவமைக்கப்பட்டு, 2015 செப்டம்பர் 18 அன்று ECI-யால் அறிமுகப்படுத்தப்பட்டது.",
        why_a_en="Correct. NID Ahmedabad designed the official NOTA symbol.",
        why_a_ta="சரியானது. அகமதாபாத் NID நிறுவனம் NOTA சின்னத்தை வடிவமைத்தது.",
        why_b_en="Incorrect. IIT Bombay designed the Rupee symbol (D. Udaya Kumar).",
        why_b_ta="தவறானது. ஐஐடி பம்பாய் ரூபாய் சின்னத்தை வடிவமைத்தது (உதய குமார்).",
        why_c_en="Incorrect. NIFT was not involved.",
        why_c_ta="தவறானது. NIFT இதில் சம்பந்தப்படவில்லை.",
        why_d_en="Incorrect. NSD is a theatre institute.",
        why_d_ta="தவறானது. NSD நாடகப் பள்ளியாகும்.",
        tip_en="NOTA symbol shows a rectangular ballot paper with an 'X' mark.",
        tip_ta="NOTA சின்னம் செவ்வக வாக்குச்சீட்டில் 'X' குறி கொண்டதாக இருக்கும்.",
        fact_en="NOTA is positioned as the very last option on the ballot unit of the EVM.",
        fact_ta="EVM வாக்குப்பதிவு இயந்திரத்தில் கடைசியாக NOTA பொத்தான் அமைக்கப்பட்டிருக்கும்.",
        tags=["NOTA Symbol", "NID Ahmedabad", "2015"]
    ))

    # ER_E_014
    qs.append(make_er_q(
        qid="ER_E_014", diff="Easy", qtype="Single-Choice", subtopic="NOTA",
        en_stem="What is the legal effect if NOTA secures the highest number of votes in a parliamentary or assembly constituency in India?",
        ta_stem="இந்தியாவில் ஒரு நாடாளுமன்ற அல்லது சட்டமன்றத் தொகுதியில் NOTA அதிக வாக்குகளைப் பெற்றால் ஏற்படும் சட்டப்பூர்வ விளைவு என்ன?",
        en_a="The candidate securing the second highest valid votes is declared elected", ta_a="இரண்டாவது அதிக செல்லுபடியாகும் வாக்குகளைப் பெற்ற வேட்பாளர் வெற்றி பெற்றவராக அறிவிக்கப்படுவார்",
        en_b="The election is automatically cancelled and fresh polls are held", ta_b="தேர்தல் தானாக ரத்து செய்யப்பட்டு மறுதேர்தல் நடத்தப்படும்",
        en_c="The seat is kept vacant until the next general election", ta_c="அடுத்த பொதுத்தேர்தல் வரை அந்த தொகுதி காலியாக வைக்கப்படும்",
        en_d="President's rule is imposed on the entire state", ta_d="மாநிலம் முழுவதும் குடியரசுத் தலைவர் ஆட்சி அமல்படுத்தப்படும்",
        correct_key="A",
        exp_en="Under the existing First-Past-The-Post system in India, NOTA votes have only symbolic/expressive value and are treated as invalid/non-transferable for determining the winner. The candidate who secures the highest number of valid votes among the contesting candidates is declared elected.",
        exp_ta="இந்தியாவின் தற்போதைய தேர்தல் நடைமுறையின்படி, NOTA வாக்குகளுக்கு குறியீட்டு மதிப்பு மட்டுமே உண்டு. போட்டியிடும் வேட்பாளர்களில் அதிக செல்லுபடியாகும் வாக்குகளைப் பெற்ற வேட்பாளரே வெற்றி பெற்றவராக அறிவிக்கப்படுவார்.",
        why_a_en="Correct. Under FPTP, candidate with most votes among contenders wins, regardless of NOTA count.",
        why_a_ta="சரியானது. அதிக வாக்குகளைப் பெற்ற அடுத்த போட்டியாளரே வெற்றியாளராக அறிவிக்கப்படுகிறார்.",
        why_b_en="Incorrect. Re-elections are not held under Central law (only some state SECs like Maharashtra/Haryana mandate it for local bodies).",
        why_b_ta="தவறானது. மத்திய சட்டத்தின் கீழ் தேர்தல் ரத்து செய்யப்படுவதில்லை.",
        why_c_en="Incorrect. The seat cannot remain vacant.",
        why_c_ta="தவறானது. தொகுதி காலியாக வைக்கப்படாது.",
        why_d_en="Incorrect. President's rule cannot be imposed for this.",
        why_d_ta="தவறானது. இதற்கு குடியரசுத் தலைவர் ஆட்சி அமல்படுத்த முடியாது.",
        tip_en="NOTA currently acts as a 'Right to Register a Negative Opinion', not an electoral veto.",
        tip_ta="தற்போது NOTA எதிர்மறை கருத்தை பதிவு செய்யும் உரிமையாக மட்டுமே செயல்படுகிறது, தேர்தல் தடையாக அல்ல.",
        fact_en="State Election Commissions of Maharashtra and Haryana treat NOTA as a 'fictional candidate' in local body elections, ordering re-polls if NOTA wins.",
        fact_ta="மகாராஷ்டிரா மற்றும் ஹரியானா மாநில தேர்தல் ஆணையங்கள் உள்ளாட்சித் தேர்தல்களில் NOTA வெற்றி பெற்றால் மறுதேர்தல் நடத்துகின்றன.",
        tags=["NOTA Impact", "First-Past-The-Post", "Electoral Law"]
    ))

    # ER_E_015
    qs.append(make_er_q(
        qid="ER_E_015", diff="Easy", qtype="Single-Choice", subtopic="Candidate Disclosures",
        en_stem="Under which Supreme Court judgment became mandatory for contesting candidates to disclose their criminal records, assets, liabilities, and educational qualifications via Form 26?",
        ta_stem="எந்த உச்ச நீதிமன்றத் தீர்ப்பின்படி போட்டியிடும் வேட்பாளர்கள் தங்கள் குற்றப்பின்னணி, சொத்துக்கள், கடன்கள் மற்றும் கல்வித்தகுதியை படிவம் 26 மூலம் வெளிப்படுத்துவது கட்டாயமாக்கப்பட்டது?",
        en_a="Union of India v. Association for Democratic Reforms (ADR) (2002)", ta_a="இந்திய ஒன்றியம் எதிர் ஜனநாயக சீர்திருத்தங்களுக்கான சங்கம் (ADR) (2002)",
        en_b="Kesavananda Bharati v. State of Kerala (1973)", ta_b="கேசவானந்த பாரதி எதிர் கேரள அரசு (1973)",
        en_c="Maneka Gandhi v. Union of India (1978)", ta_c="மேனகா காந்தி எதிர் இந்திய ஒன்றியம் (1978)",
        en_d="Minerva Mills v. Union of India (1980)", ta_d="மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
        correct_key="A",
        exp_en="In Union of India v. Association for Democratic Reforms (ADR) (2002) and PUCL v. UOI (2003), the Supreme Court ruled that voters have a fundamental 'Right to Know' candidate antecedents under Article 19(1)(a). Form 26 affidavit was consequently mandated.",
        exp_ta="இந்திய ஒன்றியம் எதிர் ADR (2002) மற்றும் PUCL வழக்கில் (2003), சரத்து 19(1)(a)-ன் கீழ் வாக்காளர்களுக்கு வேட்பாளரைப் பற்றி 'அறியும் உரிமை' அடிப்படை உரிமை என உச்ச நீதிமன்றம் தீர்ப்பளித்து, படிவம் 26 உறுதிமொழிப் பத்திரத்தைக் கட்டாயமாக்கியது.",
        why_a_en="Correct. ADR case (2002) established the voter's Right to Know under Art 19(1)(a).",
        why_a_ta="சரியானது. ADR வழக்கு (2002) வாக்காளரின் அறியும் உரிமையை உறுதி செய்தது.",
        why_b_en="Incorrect. Kesavananda Bharati established the Basic Structure Doctrine.",
        why_b_ta="தவறானது. கேசவானந்த பாரதி அடிப்படை கட்டமைப்பு கோட்பாட்டை நிறுவியது.",
        why_c_en="Incorrect. Maneka Gandhi expanded Article 21 (Personal Liberty).",
        why_c_ta="தவறானது. மேனகா காந்தி வழக்கு சரத்து 21-ன் எல்லையை விரிவுபடுத்தியது.",
        why_d_en="Incorrect. Minerva Mills strengthened judicial review and basic structure.",
        why_d_ta="தவறானது. மினர்வா மில்ஸ் நீதிப் புனராய்வை உறுதிப்படுத்தியது.",
        tip_en="Form 26 is the legal affidavit filed along with nomination papers under Rule 4A of Conduct of Elections Rules.",
        tip_ta="படிவம் 26 என்பது தேர்தல் நடத்தை விதிகள் 4A-ன் கீழ் வேட்புமனுவுடன் தாக்கல் செய்யப்படும் உறுதிமொழிப் பத்திரமாகும்.",
        fact_en="Section 33A of RPA 1951 was inserted following this judgment to mandate criminal disclosures.",
        fact_ta="இத்தீர்ப்பைத் தொடர்ந்து மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ல் பிரிவு 33A சேர்க்கப்பட்டது.",
        tags=["ADR Case 2002", "Form 26", "Right to Know", "Article 19(1)(a)"]
    ))

    # ER_E_016
    qs.append(make_er_q(
        qid="ER_E_016", diff="Easy", qtype="Single-Choice", subtopic="Criminalisation of Politics",
        en_stem="In the landmark Lily Thomas v. Union of India (2013) case, which section of the Representation of the People Act, 1951 was struck down as unconstitutional?",
        ta_stem="வரலாற்று சிறப்புமிக்க லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (2013) வழக்கில், மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் எந்தப் பிரிவு அரசியலமைப்புக்கு முரணானது என ரத்து செய்யப்பட்டது?",
        en_a="Section 8(4)", ta_a="பிரிவு 8(4)",
        en_b="Section 8(1)", ta_b="பிரிவு 8(1)",
        en_c="Section 29A", ta_c="பிரிவு 29A",
        en_d="Section 123(3)", ta_d="பிரிவு 123(3)",
        correct_key="A",
        exp_en="The Supreme Court in Lily Thomas (2013) struck down Section 8(4) of RPA 1951, which previously allowed convicted MPs and MLAs a 3-month window to appeal and retain their seats without immediate disqualification.",
        exp_ta="லில்லி தாமஸ் (2013) வழக்கில் உச்ச நீதிமன்றம் மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 8(4)-ஐ ரத்து செய்தது. அப்பிரிவு குற்றவாளியாகத் தீர்ப்பளிக்கப்பட்ட எம்.பி., எம்.எல்.ஏ-க்கள் மேல்முறையீடு செய்ய 3 மாத கால அவகாசம் வழங்கி தகுதிநீக்கத்திலிருந்து தற்காலிக விலக்கு அளித்திருந்தது.",
        why_a_en="Correct. Section 8(4) was struck down by the Supreme Court.",
        why_a_ta="சரியானது. பிரிவு 8(4) உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்டது.",
        why_b_en="Incorrect. Section 8(1) lists disqualification on specific offences like promoting enmity.",
        why_b_ta="தவறானது. பிரிவு 8(1) குறிப்பிட்ட சில குற்றங்களுக்கான தகுதிநீக்கத்தைப் பட்டியலிடுகிறது.",
        why_c_en="Incorrect. Section 29A relates to registration of political parties.",
        why_c_ta="தவறானது. பிரிவு 29A கட்சிகள் பதிவு பற்றியது.",
        why_d_en="Incorrect. Section 123(3) deals with appeal on grounds of religion or caste.",
        why_d_ta="தவறானது. பிரிவு 123(3) மதம்/ஜாதி அடிப்படையில் வாக்குக் கேட்பது பற்றியது.",
        tip_en="Post-Lily Thomas, disqualification takes effect immediately upon conviction and sentencing of 2 or more years.",
        tip_ta="லில்லி தாமஸ் தீர்ப்பிற்குப் பின், 2 அல்லது அதற்கு மேற்பட்ட ஆண்டுகள் சிறைத் தண்டனை விதிக்கப்பட்ட உடனேயே தகுதிநீக்கம் அமலுக்கு வரும்.",
        fact_en="Justice A.K. Patnaik and Justice S.J. Mukhopadhaya delivered this historic verdict on 10 July 2013.",
        fact_ta="நீதிபதிகள் ஏ.கே. பட்நாயக் மற்றும் எஸ்.ஜே. முகோபாத்யாயா 2013 ஜூலை 10 அன்று இத்தீர்ப்பை வழங்கினர்.",
        tags=["Lily Thomas 2013", "Section 8(4)", "Immediate Disqualification"]
    ))

    # ER_E_017
    qs.append(make_er_q(
        qid="ER_E_017", diff="Easy", qtype="Single-Choice", subtopic="Criminalisation of Politics",
        en_stem="Under Section 8(3) of the Representation of the People Act, 1951, a person convicted of an offence and sentenced to imprisonment for not less than 2 years is disqualified for what total period?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 8(3)-ன் கீழ், 2 ஆண்டுகளுக்கு குறையாமல் சிறைத்தண்டனை விதிக்கப்பட்ட ஒரு நபர் மொத்தம் எத்தனை ஆண்டுகள் தகுதிநீக்கம் செய்யப்படுவார்?",
        en_a="The period of imprisonment plus an additional 6 years from release", ta_a="சிறைத் தண்டனைக் காலம் மற்றும் சிறையிலிருந்து விடுதலையான நாளிலிருந்து மேலும் 6 ஆண்டுகள்",
        en_b="Only during the period of imprisonment", ta_b="சிறைத் தண்டனைக் காலம் வரை மட்டுமே",
        en_c="Permanently for life", ta_c="வாழ்நாள் முழுவதும் நிரந்தரமாக",
        en_d="For 3 years from the date of conviction", ta_d="தண்டனை விதிக்கப்பட்ட நாளிலிருந்து 3 ஆண்டுகள் மட்டும்",
        correct_key="A",
        exp_en="Under Section 8(3) of RPA 1951, a person convicted and sentenced to imprisonment for not less than 2 years is disqualified from the date of conviction and continues to be disqualified for a further period of 6 years since release.",
        exp_ta="பிரிவு 8(3)-ன் படி, 2 அல்லது அதற்கு மேற்பட்ட ஆண்டுகள் சிறைத்தண்டனை பெற்ற நபர், தண்டனை விதிக்கப்பட்ட நாளிலிருந்து சிறைக்காலம் முழுவதும் மற்றும் விடுதலையான நாளிலிருந்து மேலும் 6 ஆண்டுகளுக்கு தகுதிநீக்கம் செய்யப்படுகிறார்.",
        why_a_en="Correct. Imprisonment period + 6 additional years post-release.",
        why_a_ta="சரியானது. சிறைத் தண்டனைக் காலம் + விடுதலையான நாளிலிருந்து மேலும் 6 ஆண்டுகள்.",
        why_b_en="Incorrect. The disqualification extends far beyond the prison term.",
        why_b_ta="தவறானது. சிறைக்காலத்திற்குப் பிறகும் தகுதிநீக்கம் தொடரும்.",
        why_c_en="Incorrect. Life ban is not currently provided under Indian law (though recommended by ECI).",
        why_c_ta="தவறானது. தற்போதைய இந்திய சட்டத்தில் வாழ்நாள் தடை இல்லை.",
        why_d_en="Incorrect. 3 years is incorrect.",
        why_d_ta="தவறானது. 3 ஆண்டுகள் என்பது தவறானது.",
        tip_en="Example: If convicted to 2 years prison, total disqualification is 2 + 6 = 8 years.",
        tip_ta="உதாரணம்: 2 ஆண்டுகள் சிறை தண்டனை பெற்றால், மொத்த தகுதிநீக்கக் காலம் 2 + 6 = 8 ஆண்டுகள் ஆகும்.",
        fact_en="The ECI has repeatedly submitted affidavits to the Supreme Court supporting a lifetime ban for convicted legislators.",
        fact_ta="குற்றவாளிகளான அரசியல்வாதிகளுக்கு வாழ்நாள் தடை விதிக்க வேண்டும் என ECI உச்ச நீதிமன்றத்தில் வலியுறுத்தி வருகிறது.",
        tags=["Section 8(3)", "Disqualification Period", "6 Years Post Release"]
    ))

    # ER_E_018
    qs.append(make_er_q(
        qid="ER_E_018", diff="Easy", qtype="Single-Choice", subtopic="National Voters Day",
        en_stem="On which date is 'National Voters' Day' (Rashtriya Matdata Diwas) celebrated annually across India since 2011?",
        ta_stem="2011 முதல் ஆண்டுதோறும் இந்தியா முழுவதும் 'தேசிய வாக்காளர் தினம்' எந்த தேதியில் கொண்டாடப்படுகிறது?",
        en_a="January 25", ta_a="ஜனவரி 25",
        en_b="January 26", ta_b="ஜனவரி 26",
        en_c="November 26", ta_c="நவம்பர் 26",
        en_d="October 2", ta_d="அக்டோபர் 2",
        correct_key="A",
        exp_en="National Voters' Day has been celebrated on January 25 every year since 2011 to mark the foundation day of the Election Commission of India (established on 25 January 1950) and encourage youth electoral participation.",
        exp_ta="இந்திய தேர்தல் ஆணையம் நிறுவப்பட்ட தினத்தை (1950 ஜனவரி 25) நினைவுகூரும் வகையிலும், இளைஞர்களின் வாக்களிக்கும் ஆர்வத்தை ஊக்குவிக்கவும் 2011 முதல் ஆண்டுதோறும் ஜனவரி 25 அன்று தேசிய வாக்காளர் தினம் கொண்டாடப்படுகிறது.",
        why_a_en="Correct. January 25 marks the foundation day of ECI (1950).",
        why_a_ta="சரியானது. ஜனவரி 25 ECI நிறுவப்பட்ட தினமாகும் (1950).",
        why_b_en="Incorrect. January 26 is Republic Day.",
        why_b_ta="தவறானது. ஜனவரி 26 குடியரசு தினம்.",
        why_c_en="Incorrect. November 26 is Constitution Day (Samvidhan Diwas).",
        why_c_ta="தவறானது. நவம்பர் 26 அரசியலமைப்பு தினம்.",
        why_d_en="Incorrect. October 2 is Gandhi Jayanti.",
        why_d_ta="தவறானது. அக்டோபர் 2 காந்தி ஜெயந்தி.",
        tip_en="First initiated under the tenure of CEC S.Y. Quraishi in 2011.",
        tip_ta="2011-ல் தலைமை தேர்தல் ஆணையர் எஸ்.ஒய். குரேஷி காலத்தில் முதன்முதலில் தொடங்கப்பட்டது.",
        fact_en="The primary motto of National Voters' Day is 'Nothing Like Voting, I Vote for Sure'.",
        fact_ta="தேசிய வாக்காளர் தினத்தின் தாரக மந்திரம் 'வாக்களிப்பது போல் எதுவும் இல்லை, நான் நிச்சயமாக வாக்களிப்பேன்' என்பதாகும்.",
        tags=["National Voters Day", "January 25", "ECI Foundation"]
    ))

    # ER_E_019
    qs.append(make_er_q(
        qid="ER_E_019", diff="Easy", qtype="Single-Choice", subtopic="Electoral Photo Identity Card",
        en_stem="In which year was the Electors Photo Identity Card (EPIC) introduced in India under the leadership of CEC T.N. Seshan?",
        ta_stem="தலைமை தேர்தல் ஆணையர் டி.என். சேஷன் தலைமையில் இந்தியாவில் வாக்காளர் புகைப்பட அடையாள அட்டை (EPIC) எந்த ஆண்டு அறிமுகப்படுத்தப்பட்டது?",
        en_a="1993", ta_a="1993",
        en_b="1982", ta_b="1982",
        en_c="2001", ta_c="2001",
        en_d="2014", ta_d="2014",
        correct_key="A",
        exp_en="The Electors Photo Identity Card (EPIC) was introduced by Chief Election Commissioner T.N. Seshan in 1993 to eliminate bogus voting, impersonation, and fraudulent electoral roll entries.",
        exp_ta="வாக்காளர் ஆள்மாறாட்டம் மற்றும் கள்ள ஓட்டுகளைத் தடுப்பதற்காக 1993-ல் தலைமை தேர்தல் ஆணையர் டி.என். சேஷன் அவர்களால் வாக்காளர் புகைப்பட அடையாள அட்டை (EPIC) அறிமுகப்படுத்தப்பட்டது.",
        why_a_en="Correct. Introduced in 1993 under T.N. Seshan.",
        why_a_ta="சரியானது. 1993-ல் டி.என். சேஷனால் அறிமுகப்படுத்தப்பட்டது.",
        why_b_en="Incorrect. 1982 was the year EVMs were first piloted in Kerala.",
        why_b_ta="தவறானது. 1982-ல் கேரளாவில் முதன்முதலில் EVM சோதனை செய்யப்பட்டது.",
        why_c_en="Incorrect. 2001 is too late.",
        why_c_ta="தவறானது. 2001 தவறானது.",
        why_d_en="Incorrect. 2014 is the 16th Lok Sabha election year.",
        why_d_ta="தவறானது. 2014-ல் 16-வது மக்களவைத் தேர்தல் நடைபெற்றது.",
        tip_en="T.N. Seshan served as the 10th CEC from 1990 to 1996 and revolutionized Indian elections.",
        tip_ta="டி.என். சேஷன் 1990 முதல் 1996 வரை 10-வது தலைமை தேர்தல் ஆணையராகப் பணியாற்றினார்.",
        fact_en="Today, digital e-EPIC is also available in non-editable PDF format on the NVSP / ECI portal.",
        fact_ta="தற்போது NVSP போர்ட்டல் மூலம் டிஜிட்டல் e-EPIC பதிவிறக்கம் செய்யும் வசதியும் உள்ளது.",
        tags=["EPIC Card", "TN Seshan", "1993", "Voter ID"]
    ))

    # ER_E_020
    qs.append(make_er_q(
        qid="ER_E_020", diff="Easy", qtype="Single-Choice", subtopic="Model Code of Conduct",
        en_stem="In which state assembly election was the Model Code of Conduct (MCC) first introduced on a voluntary basis in 1960?",
        ta_stem="1960-ல் எந்த மாநில சட்டமன்றத் தேர்தலின் போது மாதிரி தேர்தல் நடத்தை விதிகள் (MCC) முதன்முதலில் தன்னார்வ அடிப்படையில் அறிமுகப்படுத்தப்பட்டன?",
        en_a="Kerala", ta_a="கேரளா",
        en_b="Tamil Nadu", ta_b="தமிழ்நாடு",
        en_c="West Bengal", ta_c="மேற்கு வங்காளம்",
        en_d="Punjab", ta_d="பஞ்சாப்",
        correct_key="A",
        exp_en="The Model Code of Conduct (MCC) originated in Kerala during the February 1960 Assembly elections, where the state administration formulated a voluntary code of conduct for political parties.",
        exp_ta="மாதிரி தேர்தல் நடத்தை விதிகள் (MCC) முதன்முதலில் 1960 பிப்ரவரியில் கேரள சட்டமன்றத் தேர்தலின் போது அரசியல் கட்சிகளுக்கான தன்னார்வ நடத்தை நெறியாக மாநில நிர்வாகத்தால் உருவாக்கப்பட்டது.",
        why_a_en="Correct. First introduced in Kerala in 1960.",
        why_a_ta="சரியானது. 1960-ல் கேரளாவில் முதன்முதலில் அறிமுகப்படுத்தப்பட்டது.",
        why_b_en="Incorrect. Tamil Nadu adopted it in subsequent elections.",
        why_b_ta="தவறானது. தமிழ்நாடு பிற்காலத்தில் ஏற்றுக்கொண்டது.",
        why_c_en="Incorrect. West Bengal was not the origin state.",
        why_c_ta="தவறானது. மேற்கு வங்காளம் முதல் மாநிலம் அல்ல.",
        why_d_en="Incorrect. Punjab was not the origin state.",
        why_d_ta="தவறானது. பஞ்சாப் முதல் மாநிலம் அல்ல.",
        tip_en="ECI circulated the MCC nationally to all recognized political parties for the first time in 1968 for mid-term elections.",
        tip_ta="1968 இடைக்காலத் தேர்தலின் போது ECI தேசிய அளவில் நடத்தை விதிகளை அனைத்து அங்கீகரிக்கப்பட்ட கட்சிகளுக்கும் சுற்றறிக்கையாக அனுப்பியது.",
        fact_en="The Model Code of Conduct has no statutory backing; it is enforced through the constitutional authority of ECI under Article 324.",
        fact_ta="தேர்தல் நடத்தை விதிகளுக்கு சட்டப்பூர்வ அந்தஸ்து இல்லை; சரத்து 324-ன் கீழ் ECI-ன் அதிகாரத்தால் அமல்படுத்தப்படுகிறது.",
        tags=["Model Code of Conduct", "Kerala", "1960", "MCC Origin"]
    ))

    # ER_E_021
    qs.append(make_er_q(
        qid="ER_E_021", diff="Easy", qtype="Single-Choice", subtopic="Model Code of Conduct",
        en_stem="At what exact point in time does the Model Code of Conduct (MCC) come into operational force?",
        ta_stem="மாதிரி தேர்தல் நடத்தை விதிகள் (MCC) எந்த குறிப்பிட்ட தருணத்தில் உடனடியாக நடைமுறைக்கு வருகின்றன?",
        en_a="Immediately upon the announcement of election schedule by the ECI", ta_a="தேர்தல் ஆணையம் தேர்தல் தேதிகளை அறிவித்த உடனேயே",
        en_b="On the date of gazette notification of the election", ta_b="தேர்தல் குறித்த அரசிதழ் அறிவிக்கை வெளியாகும் நாளில்",
        en_c="From the last date of withdrawal of candidatures", ta_c="வேட்புமனுக்களை திரும்பப் பெறுவதற்கான கடைசி நாளிலிருந்து",
        en_d="Exactly 48 hours before the start of polling", ta_d="வாக்குப்பதிவு தொடங்குவதற்கு சரியாக 48 மணி நேரத்திற்கு முன்",
        correct_key="A",
        exp_en="The Model Code of Conduct comes into operational effect immediately upon the announcement of the election schedule by the Election Commission at its press conference, and remains in force until the completion of the election process.",
        exp_ta="தேர்தல் ஆணையம் செய்தியாளர் சந்திப்பில் தேர்தல் தேதிகளை அறிவித்த உடனேயே மாதிரி நடத்தை விதிகள் உடனடியாக அமலுக்கு வந்து, தேர்தல் முடிவுகள் அறிவிக்கப்படும் வரை நீடிக்கும்.",
        why_a_en="Correct. Comes into force immediately upon announcement by ECI.",
        why_a_ta="சரியானது. ECI தேர்தல் அட்டவணையை அறிவித்த நொடியிலேயே நடைமுறைக்கு வரும்.",
        why_b_en="Incorrect. Gazette notification occurs several days after the press conference.",
        why_b_ta="தவறானது. அரசிதழ் அறிவிக்கை சில நாட்களுக்குப் பின்னரே வெளியாகும்.",
        why_c_en="Incorrect. Withdrawal date is much later.",
        why_c_ta="தவறானது. வேட்புமனு திரும்பப் பெறும் நாள் மிகவும் பிந்தையதாகும்.",
        why_d_en="Incorrect. 48 hours before polling refers to the 'silence period' under Section 126.",
        why_d_ta="தவறானது. 48 மணி நேரத்திற்கு முன் என்பது அமைதிக்காலம் (பிரிவு 126).",
        tip_en="Supreme Court upheld ECI's authority to enforce MCC from the date of announcement in Election Commission v. Ashok Kumar (2000).",
        tip_ta="அறிவிக்கப்பட்ட நாளிலிருந்தே MCC அமலுக்கு வரும் ECI-ன் அதிகாரத்தை அசோக் குமார் (2000) வழக்கில் உச்ச நீதிமன்றம் உறுதி செய்தது.",
        fact_en="During MCC, ruling parties cannot announce new schemes, financial grants, or lay foundation stones.",
        fact_ta="MCC அமலில் உள்ள போது ஆளும் கட்சி புதிய திட்டங்களை அறிவிக்கவோ அடிக்கல் நாட்டவோ நிதி மானியங்களை வழங்கவோ முடியாது.",
        tags=["MCC Enforcement", "Announcement Date", "ECI Power"]
    ))

    # ER_E_022
    qs.append(make_er_q(
        qid="ER_E_022", diff="Easy", qtype="Single-Choice", subtopic="Women Reservation",
        en_stem="Which Constitutional Amendment Act passed in 2023 provides 33% reservation for women in the Lok Sabha and State Legislative Assemblies?",
        ta_stem="2023-ல் நிறைவேற்றப்பட்ட எந்த அரசியலமைப்புச் சட்டத்திருத்தம் மக்களவை மற்றும் மாநில சட்டமன்றங்களில் பெண்களுக்கு 33% இடஒதுக்கீட்டை வழங்குகிறது?",
        en_a="106th Constitutional Amendment Act, 2023", ta_a="106-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2023",
        en_b="103rd Constitutional Amendment Act, 2019", ta_b="103-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2019",
        en_c="104th Constitutional Amendment Act, 2019", ta_c="104-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2019",
        en_d="105th Constitutional Amendment Act, 2021", ta_d="105-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2021",
        correct_key="A",
        exp_en="The 106th Constitutional Amendment Act, 2023 (popularly known as Nari Shakti Vandan Adhiniyam) provides one-third (33%) reservation for women in Lok Sabha, State Legislative Assemblies, and the Legislative Assembly of Delhi.",
        exp_ta="106-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2023 ('நாரி சக்தி வந்தன் அதினியம்') மக்களவை, மாநில சட்டமன்றங்கள் மற்றும் டெல்லி யூனியன் பிரதேச சட்டசபையில் பெண்களுக்கு 33% (மூன்றில் ஒரு பங்கு) இடஒதுக்கீடு வழங்குகிறது.",
        why_a_en="Correct. 106th Amendment Act, 2023 enacted women's reservation.",
        why_a_ta="சரியானது. 106-வது திருத்தச் சட்டம் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்கியது.",
        why_b_en="Incorrect. 103rd Amendment (2019) provided 10% EWS reservation.",
        why_b_ta="தவறானது. 103-வது திருத்தம் EWS பிரிவினருக்கு 10% இடஒதுக்கீடு வழங்கியது.",
        why_c_en="Incorrect. 104th Amendment (2019) extended SC/ST reservation and abolished Anglo-Indian nominations.",
        why_c_ta="தவறானது. 104-வது திருத்தம் ஆங்கிலோ-இந்தியர் நியமனத்தை நீக்கியது.",
        why_d_en="Incorrect. 105th Amendment (2021) restored state powers to identify SEBCs/OBCs.",
        why_d_ta="தவறானது. 105-வது திருத்தம் OBC பட்டியலை தயாரிக்கும் மாநில அதிகாரத்தை மீட்டெடுத்தது.",
        tip_en="It was introduced as the 128th Constitutional Amendment Bill in the new Parliament building.",
        tip_ta="இது புதிய நாடாளுமன்றக் கட்டடத்தில் 128-வது அரசியலமைப்பு திருத்த மசோதாவாக அறிமுகப்படுத்தப்பட்டது.",
        fact_en="It inserted new Articles 330A, 332A, and 334A into the Indian Constitution.",
        fact_ta="இது இந்திய அரசியலமைப்பில் புதிய சரத்துகள் 330A, 332A மற்றும் 334A ஆகியவற்றை இணைத்தது.",
        tags=["106th Amendment", "Women Reservation", "Nari Shakti Vandan"]
    ))

    # ER_E_023
    qs.append(make_er_q(
        qid="ER_E_023", diff="Easy", qtype="Single-Choice", subtopic="Women Reservation",
        en_stem="Under Article 334A inserted by the 106th Amendment Act, 2023, for what initial period will women's reservation remain in force from its commencement?",
        ta_stem="106-வது திருத்தச் சட்டம் 2023 மூலம் சேர்க்கப்பட்ட சரத்து 334A-ன் கீழ், நடைமுறைக்கு வந்த நாளிலிருந்து தொடக்கத்தில் எத்தனை ஆண்டுகளுக்கு மகளிர் இடஒதுக்கீடு அமலில் இருக்கும்?",
        en_a="15 years", ta_a="15 ஆண்டுகள்",
        en_b="10 years", ta_b="10 ஆண்டுகள்",
        en_c="20 years", ta_c="20 ஆண்டுகள்",
        en_d="25 years", ta_d="25 ஆண்டுகள்",
        correct_key="A",
        exp_en="Article 334A provides that the reservation of seats for women in the Lok Sabha and State Legislative Assemblies shall cease to have effect on the expiration of a period of 15 years from the date of its commencement, unless extended by Parliament by law.",
        exp_ta="சரத்து 334A-ன் படி, நாடாளுமன்றம் சட்டத்தின் மூலம் நீட்டிக்காவிட்டால், மகளிர் இடஒதுக்கீடு நடைமுறைக்கு வந்த நாளிலிருந்து 15 ஆண்டுகள் வரை மட்டுமே அமலில் இருக்கும்.",
        why_a_en="Correct. 15 years sunset clause under Article 334A.",
        why_a_ta="சரியானது. சரத்து 334A-ன் கீழ் 15 ஆண்டுகள் வரை அமலில் இருக்கும்.",
        why_b_en="Incorrect. 10 years was the initial limit for SC/ST reservations under Article 334.",
        why_b_ta="தவறானது. 10 ஆண்டுகள் என்பது SC/ST இடஒதுக்கீட்டின் தொடக்க கால வரம்பாகும்.",
        why_c_en="Incorrect. 20 years is incorrect.",
        why_c_ta="தவறானது. 20 ஆண்டுகள் தவறானது.",
        why_d_en="Incorrect. 25 years is incorrect.",
        why_d_ta="தவறானது. 25 ஆண்டுகள் தவறானது.",
        tip_en="Article 334A explicitly states the 15-year sunset clause, which can be extended by a simple law made by Parliament.",
        tip_ta="சரத்து 334A தெளிவான 15 ஆண்டு கால வரம்பைக் கொண்டுள்ளது; நாடாளுமன்றம் சட்டமியற்றி இதை நீட்டிக்கலாம்.",
        fact_en="Women's reservation will take effect only after delimitation is conducted based on the first census taken after the commencement of the Act.",
        fact_ta="இச்சட்டம் தொடங்கிய பின் எடுக்கப்படும் முதல் மக்கள்தொகை கணக்கெடுப்பின் அடிப்படையில் தொகுதி மறுவரையறை செய்யப்பட்ட பிறகே இது நடைமுறைக்கு வரும்.",
        tags=["Article 334A", "15 Years", "Sunset Clause"]
    ))

    # ER_E_024
    qs.append(make_er_q(
        qid="ER_E_024", diff="Easy", qtype="Single-Choice", subtopic="Delimitation",
        en_stem="Which Constitutional Amendment Act froze the allocation of seats in the Lok Sabha and State Assemblies until the year 2026 based on the 1971 census?",
        ta_stem="1971 மக்கள்தொகை கணக்கெடுப்பின் அடிப்படையில் மக்களவை மற்றும் மாநில சட்டமன்ற தொகுதிகளின் எண்ணிக்கையை 2026 ஆம் ஆண்டு வரை முடக்கிய அரசியலமைப்புச் சட்டத்திருத்தம் எது?",
        en_a="84th Constitutional Amendment Act, 2001", ta_a="84-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2001",
        en_b="42nd Constitutional Amendment Act, 1976", ta_b="42-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1976",
        en_c="87th Constitutional Amendment Act, 2003", ta_c="87-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2003",
        en_d="91st Constitutional Amendment Act, 2003", ta_d="91-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2003",
        correct_key="A",
        exp_en="The 84th Constitutional Amendment Act, 2001 extended the freeze on the total number of seats in the Lok Sabha and State Legislative Assemblies up to the year 2026 (first census after 2026). It was enacted to motivate family planning measures.",
        exp_ta="84-வது அரசியலமைப்புச் சட்டத்திருத்தம் 2001, குடும்பக் கட்டுப்பாடு திட்டங்களை ஊக்குவிப்பதற்காக, மக்களவை மற்றும் மாநில சட்டமன்றங்களின் மொத்த தொகுதிகள் எண்ணிக்கையை 2026-க்குப் பிறகு எடுக்கப்படும் முதல் கணக்கெடுப்பு வரை முடக்கியது.",
        why_a_en="Correct. 84th Amendment Act, 2001 froze total seat allocation until 2026.",
        why_a_ta="சரியானது. 84-வது திருத்தச் சட்டம் 2026 வரை தொகுதி எண்ணிக்கையை முடக்கியது.",
        why_b_en="Incorrect. 42nd Amendment (1976) originally froze seats up to the year 2000.",
        why_b_ta="தவறானது. 42-வது திருத்தம் (1976) 2000 ஆம் ஆண்டு வரை முதலில் முடக்கியது.",
        why_c_en="Incorrect. 87th Amendment (2003) allowed delimitation within states based on 2001 census without changing total seats.",
        why_c_ta="தவறானது. 87-வது திருத்தம் 2001 கணக்கெடுப்பின்படி உள்-மறுவரையறை செய்ய அனுமதித்தது.",
        why_d_en="Incorrect. 91st Amendment (2003) limited the size of Council of Ministers to 15% and strengthened anti-defection.",
        why_d_ta="தவறானது. 91-வது திருத்தம் அமைச்சரவை அளவை 15% ஆகக் கட்டுப்படுத்தியது.",
        tip_en="42nd Amendment froze seats till 2000; 84th Amendment extended the freeze till 2026.",
        tip_ta="42-வது திருத்தம் 2000 வரை முடக்கியது; 84-வது திருத்தம் அதை 2026 வரை நீட்டித்தது.",
        fact_en="Delimitation Commission of 2002 was headed by retired Supreme Court Justice Kuldip Singh.",
        fact_ta="2002-ல் அமைக்கப்பட்ட தொகுதி மறுவரையறை ஆணையத்தின் தலைவர் ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதி குல்தீப் சிங் ஆவார்.",
        tags=["84th Amendment", "Delimitation Freeze", "Year 2026"]
    ))

    # ER_E_025
    qs.append(make_er_q(
        qid="ER_E_025", diff="Easy", qtype="Single-Choice", subtopic="Delimitation",
        en_stem="The 87th Constitutional Amendment Act, 2003 permitted the delimitation and readjustment of territorial constituencies within states on the basis of which census?",
        ta_stem="87-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2003 எந்த மக்கள்தொகை கணக்கெடுப்பின் அடிப்படையில் மாநிலங்களுக்குள் தொகுதிகளை மறுவரையறை செய்ய அனுமதித்தது?",
        en_a="2001 Census", ta_a="2001 மக்கள் தொகை கணக்கெடுப்பு",
        en_b="1991 Census", ta_b="1991 மக்கள் தொகை கணக்கெடுப்பு",
        en_c="1971 Census", ta_c="1971 மக்கள் தொகை கணக்கெடுப்பு",
        en_d="2011 Census", ta_d="2011 மக்கள் தொகை கணக்கெடுப்பு",
        correct_key="A",
        exp_en="The 87th Constitutional Amendment Act, 2003 amended Articles 81, 82, 170, and 330 to substitute '2001 census' in place of '1991 census' for the purpose of readjusting territorial constituencies without altering total seats allocated to any state.",
        exp_ta="87-வது திருத்தச் சட்டம் 2003, மாநிலங்களுக்கான மொத்த தொகுதிகளின் எண்ணிக்கையை மாற்றாமல், மாநிலத்திற்குள் உள்ள தொகுதிகளை மறுசீரமைக்க '1991 கணக்கெடுப்பு' என்பதற்குப் பதிலாக '2001 கணக்கெடுப்பு' என்பதை மாற்றியது.",
        why_a_en="Correct. 87th Amendment substituted 2001 census for internal delimitation.",
        why_a_ta="சரியானது. 87-வது திருத்தம் 2001 கணக்கெடுப்பை அடிப்படையாகக் கொண்டது.",
        why_b_en="Incorrect. 1991 census was originally adopted in the 84th Amendment 2001.",
        why_b_ta="தவறானது. 1991 கணக்கெடுப்பு 84-வது திருத்தத்தில் இருந்தது.",
        why_c_en="Incorrect. 1971 census remains the basis for total seat allocation among states.",
        why_c_ta="தவறானது. மாநிலங்களுக்கான மொத்த தொகுதி எண்ணிக்கைக்கு 1971 கணக்கெடுப்பே அடிப்படையாகும்.",
        why_d_en="Incorrect. 2011 census was not used.",
        why_d_ta="தவறானது. 2011 கணக்கெடுப்பு பயன்படுத்தப்படவில்லை.",
        tip_en="Total seats per state = 1971 Census; Boundaries within state = 2001 Census.",
        tip_ta="மாநிலங்களின் மொத்த தொகுதிகள் = 1971 கணக்கெடுப்பு; மாநிலத்திற்குள் எல்லைகள் = 2001 கணக்கெடுப்பு.",
        fact_en="The Kuldip Singh Delimitation Commission redrew boundaries across all states (except J&K and four NE states) based on the 2001 census.",
        fact_ta="நீதிபதி குல்தீப் சிங் ஆணையம் 2001 கணக்கெடுப்பின்படி நாட்டின் பெரும்பாலான மாநிலங்களில் எல்லைகளை மாற்றியமைத்தது.",
        tags=["87th Amendment", "2001 Census", "Delimitation"]
    ))

    # ER_E_026
    qs.append(make_er_q(
        qid="ER_E_026", diff="Easy", qtype="Single-Choice", subtopic="Registration of Political Parties",
        en_stem="Under which section of the Representation of the People Act, 1951 are political parties in India registered with the Election Commission?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் எந்தப் பிரிவின் கீழ் இந்தியாவில் அரசியல் கட்சிகள் தேர்தல் ஆணையத்தில் பதிவு செய்யப்படுகின்றன?",
        en_a="Section 29A", ta_a="பிரிவு 29A",
        en_b="Section 123", ta_b="பிரிவு 123",
        en_c="Section 77", ta_c="பிரிவு 77",
        en_d="Section 10A", ta_d="பிரிவு 10A",
        correct_key="A",
        exp_en="Section 29A of the Representation of the People Act, 1951 provides for the registration of associations and bodies of individual citizens as political parties with the Election Commission of India.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 29A, குடிமக்களின் சங்கங்கள் மற்றும் அமைப்புகளை அரசியல் கட்சிகளாக இந்திய தேர்தல் ஆணையத்தில் பதிவு செய்வதற்கான நடைமுறையை வழங்குகிறது.",
        why_a_en="Correct. Section 29A governs political party registration.",
        why_a_ta="சரியானது. பிரிவு 29A கட்சிகள் பதிவு செய்வதைக் கையாள்கிறது.",
        why_b_en="Incorrect. Section 123 defines corrupt practices.",
        why_b_ta="தவறானது. பிரிவு 123 ஊழல் நடைமுறைகளை வரையறுக்கிறது.",
        why_c_en="Incorrect. Section 77 deals with election expenditure accounts.",
        why_c_ta="தவறானது. பிரிவு 77 தேர்தல் செலவுக் கணக்குகள் பற்றியது.",
        why_d_en="Incorrect. Section 10A deals with disqualification for failure to lodge expenditure accounts.",
        why_d_ta="தவறானது. பிரிவு 10A செலவுக் கணக்கு தாக்கல் செய்யாததற்கான தகுதிநீக்கம் பற்றியது.",
        tip_en="Section 29A was inserted into RPA 1951 by an amendment act in 1989.",
        tip_ta="1989 ஆம் ஆண்டு சட்டத்திருத்தத்தின் மூலம் பிரிவு 29A இணைக்கப்பட்டது.",
        fact_en="Registered parties must declare allegiance to the Constitution of India, socialism, secularism, and democracy under Section 29A(5).",
        fact_ta="பிரிவு 29A(5)-ன் கீழ் பதிவு செய்யும் கட்சிகள் இந்திய அரசியலமைப்பு, சோசலிசம், மதச்சார்பின்மை, ஜனநாயகம் ஆகியவற்றிற்கு விசுவாசமாக இருப்பதாக உறுதியளிக்க வேண்டும்.",
        tags=["Section 29A", "RPA 1951", "Party Registration"]
    ))

    # ER_E_027
    qs.append(make_er_q(
        qid="ER_E_027", diff="Easy", qtype="Single-Choice", subtopic="Political Funding",
        en_stem="In February 2024, a 5-judge Constitution Bench of the Supreme Court declared the Electoral Bonds Scheme unconstitutional for violating which fundamental right?",
        ta_stem="2024 பிப்ரவரியில், உச்ச நீதிமன்றத்தின் 5 நீதிபதிகள் கொண்ட அரசியல் சாசன அமர்வு தேர்தல் பத்திரங்கள் திட்டத்தை எந்த அடிப்படை உரிமையை மீறுவதாகக் கூறி ரத்து செய்தது?",
        en_a="Article 19(1)(a) – Right to Freedom of Speech and Expression (Right to Information)", ta_a="சரத்து 19(1)(a) – பேச்சு மற்றும் கருத்துச் சுதந்திர உரிமை (தகவல் அறியும் உரிமை)",
        en_b="Article 21 – Right to Life and Personal Liberty", ta_b="சரத்து 21 – வாழ்வு மற்றும் தனிநபர் சுதந்திர உரிமை",
        en_c="Article 25 – Freedom of Religion", ta_c="சரத்து 25 – மத சுதந்திர உரிமை",
        en_d="Article 32 – Right to Constitutional Remedies", ta_d="சரத்து 32 – அரசியலமைப்பு தீர்வுக்கான உரிமை",
        correct_key="A",
        exp_en="In Association for Democratic Reforms (ADR) v. Union of India (February 15, 2024), a unanimous 5-judge bench headed by CJI D.Y. Chandrachud struck down the Electoral Bonds Scheme as violative of the voters' Right to Information under Article 19(1)(a).",
        exp_ta="ஜனநாயக சீர்திருத்தங்களுக்கான சங்கம் (ADR) எதிர் இந்திய ஒன்றியம் (15 பிப்ரவரி 2024) வழக்கில், தலைமை நீதிபதி டி.ஒய். சந்திரசூட் தலைமையிலான 5 நீதிபதிகள் அமர்வு, சரத்து 19(1)(a)-ன் கீழான வாக்காளர்களின் தகவல் அறியும் உரிமையை மீறுவதாகக் கூறி தேர்தல் பத்திரங்கள் திட்டத்தை ரத்து செய்தது.",
        why_a_en="Correct. Electoral Bonds violated Article 19(1)(a) voter's right to information.",
        why_a_ta="சரியானது. தேர்தல் பத்திரங்கள் திட்டம் சரத்து 19(1)(a)-ன் கீழான தகவல் அறியும் உரிமையை மீறியது.",
        why_b_en="Incorrect. Primary ground was Article 19(1)(a), not Article 21.",
        why_b_ta="தவறானது. முக்கிய காரணம் சரத்து 19(1)(a) ஆகும்.",
        why_c_en="Incorrect. Freedom of religion was not involved.",
        why_c_ta="தவறானது. மத சுதந்திரத்துடன் தொடர்புடையது அல்ல.",
        why_d_en="Incorrect. Article 32 was the writ petition mechanism used to approach the court.",
        why_d_ta="தவறானது. சரத்து 32 என்பது நீதிமன்றத்தை அணுகிய வழியாகும்.",
        tip_en="The court also struck down amendments made to the Companies Act, 2013 and RPA 1951 by the Finance Act, 2017.",
        tip_ta="2017 நிதிச் சட்டம் மூலம் கம்பெனிகள் சட்டம் மற்றும் RPA 1951-ல் செய்யப்பட்ட திருத்தங்களையும் நீதிமன்றம் ரத்து செய்தது.",
        fact_en="SBI was directed to immediately stop issuing bonds and disclose all purchase and redemption details to ECI.",
        fact_ta="பத்திரங்களை வழங்குவதை உடனடியாக நிறுத்தி, வாங்கிய மற்றும் பணமாக்கிய விவரங்களை ECI-யிடம் வழங்க SBI-க்கு உத்தரவிடப்பட்டது.",
        tags=["Electoral Bonds 2024", "Article 19(1)(a)", "ADR Case", "Supreme Court"]
    ))

    # ER_E_028
    qs.append(make_er_q(
        qid="ER_E_028", diff="Easy", qtype="Single-Choice", subtopic="Election Laws Amendment 2021",
        en_stem="The Election Laws (Amendment) Act, 2021 increased the number of qualifying dates in a year for voter registration from one (1st January) to how many dates?",
        ta_stem="தேர்தல் சட்டங்கள் (திருத்தச்) சட்டம், 2021 வாக்காளர் பட்டியலில் பெயர் சேர்க்க தகுதிபெறும் தேதிகளின் எண்ணிக்கையை ஆண்டிற்கு ஒன்று (ஜனவரி 1) என்பதிலிருந்து எத்தனையாக அதிகரித்தது?",
        en_a="4 qualifying dates", ta_a="4 தகுதி தேதிகள்",
        en_b="2 qualifying dates", ta_b="2 தகுதி தேதிகள்",
        en_c="6 qualifying dates", ta_c="6 தகுதி தேதிகள்",
        en_d="12 qualifying dates", ta_d="12 தகுதி தேதிகள்",
        correct_key="A",
        exp_en="The Election Laws (Amendment) Act, 2021 amended Section 14(b) of RPA 1950 to introduce four qualifying dates in a calendar year: January 1, April 1, July 1, and October 1, enabling youth turning 18 to enroll quarterly.",
        exp_ta="தேர்தல் சட்டங்கள் திருத்தச் சட்டம் 2021, மக்கள் பிரதிநிதித்துவச் சட்டம் 1950 பிரிவு 14(b)-ஐத் திருத்தி, ஆண்டிற்கு நான்கு தகுதி தேதிகளை (ஜனவரி 1, ஏப்ரல் 1, ஜூலை 1, அக்டோபர் 1) அறிமுகப்படுத்தியது.",
        why_a_en="Correct. Four qualifying dates: Jan 1, Apr 1, Jul 1, Oct 1.",
        why_a_ta="சரியானது. நான்கு தகுதி தேதிகள்: ஜனவரி 1, ஏப்ரல் 1, ஜூலை 1, அக்டோபர் 1.",
        why_b_en="Incorrect. 2 dates is incorrect.",
        why_b_ta="தவறானது. 2 தேதிகள் தவறானது.",
        why_c_en="Incorrect. 6 dates is incorrect.",
        why_c_ta="தவறானது. 6 தேதிகள் தவறானது.",
        why_d_en="Incorrect. 12 dates is incorrect.",
        why_d_ta="தவறானது. 12 தேதிகள் தவறானது.",
        tip_en="Previously, a citizen turning 18 on January 2 had to wait an entire year until the next January 1 to enroll.",
        tip_ta="முன்பு ஜனவரி 2 அன்று 18 வயதை அடைந்தவர் அடுத்த ஆண்டு ஜனவரி 1 வரை காத்திருக்க வேண்டியிருந்தது.",
        fact_en="This amendment also allowed voluntary linking of Aadhaar with the electoral roll (Form 6B).",
        fact_ta="இத்திருத்தம் ஆதார் எண்ணை வாக்காளர் பட்டியலுடன் இணைக்கும் தன்னார்வ வசதியையும் (படிவம் 6B) வழங்கியது.",
        tags=["Election Laws Amendment 2021", "4 Qualifying Dates", "RPA 1950"]
    ))

    # ER_E_029
    qs.append(make_er_q(
        qid="ER_E_029", diff="Easy", qtype="Single-Choice", subtopic="Electoral Roll Forms",
        en_stem="Which application form is used by an Indian citizen for new voter registration / inclusion of name in the electoral roll?",
        ta_stem="ஒரு இந்திய குடிமகன் வாக்காளர் பட்டியலில் புதிதாக பெயர் சேர்க்க / புதிய வாக்காளராக பதிவு செய்ய எந்த விண்ணப்பப் படிவத்தைப் பயன்படுத்த வேண்டும்?",
        en_a="Form 6", ta_a="படிவம் 6 (Form 6)",
        en_b="Form 7", ta_b="படிவம் 7 (Form 7)",
        en_c="Form 8", ta_c="படிவம் 8 (Form 8)",
        en_d="Form 6A", ta_d="படிவம் 6A (Form 6A)",
        correct_key="A",
        exp_en="Form 6 is the statutory application form prescribed under the Registration of Electors Rules, 1960 for inclusion of name in the electoral roll for first-time / new voters.",
        exp_ta="1960 வாக்காளர் பதிவு விதிகளின் கீழ் வாக்காளர் பட்டியலில் புதிதாக பெயர் சேர்க்க / முதல்முறை வாக்காளர்கள் பதிவு செய்ய படிவம் 6 பயன்படுகிறது.",
        why_a_en="Correct. Form 6 is for new voter enrollment.",
        why_a_ta="சரியானது. புதிய வாக்காளர் பதிவுக்கு படிவம் 6 பயன்படுகிறது.",
        why_b_en="Incorrect. Form 7 is for objection to inclusion or deletion of a name.",
        why_b_ta="தவறானது. படிவம் 7 பெயர் நீக்கம் அல்லது ஆட்சேபனைக்கானது.",
        why_c_en="Incorrect. Form 8 is for correction of particulars or shifting of residence.",
        why_c_ta="தவறானது. படிவம் 8 முகவரி மாற்றம் அல்லது திருத்தங்களுக்கானது.",
        why_d_en="Incorrect. Form 6A is exclusively for Overseas (NRI) electors.",
        why_d_ta="தவறானது. படிவம் 6A வெளிநாடு வாழ் இந்தியர்களுக்கானது (NRI).",
        tip_en="Summary: Form 6 = New voter; Form 6A = NRI; Form 7 = Deletion; Form 8 = Correction/Shifting.",
        tip_ta="சுருக்கம்: படிவம் 6 = புதிய வாக்காளர்; 6A = NRI; படிவம் 7 = நீக்கம்; படிவம் 8 = திருத்தம்/முகவரி மாற்றம்.",
        fact_en="Form 6B was newly introduced in 2022 for voluntary submission of Aadhaar number by electors.",
        fact_ta="வாக்காளர்கள் தங்கள் ஆதார் எண்ணை தாமாக முன்வந்து வழங்க 2022-ல் படிவம் 6B அறிமுகப்படுத்தப்பட்டது.",
        tags=["Form 6", "Voter Registration", "Forms"]
    ))

    # ER_E_030
    qs.append(make_er_q(
        qid="ER_E_030", diff="Easy", qtype="Single-Choice", subtopic="Electoral Roll Forms",
        en_stem="Which application form must be submitted by an Overseas (NRI) elector to get enrolled in the Indian electoral roll?",
        ta_stem="வெளிநாடு வாழ் இந்தியர் (NRI) ஒருவர் இந்திய வாக்காளர் பட்டியலில் பெயர் பதிவு செய்ய எந்த விண்ணப்பப் படிவத்தை சமர்ப்பிக்க வேண்டும்?",
        en_a="Form 6A", ta_a="படிவம் 6A (Form 6A)",
        en_b="Form 6", ta_b="படிவம் 6 (Form 6)",
        en_c="Form 8A", ta_c="படிவம் 8A (Form 8A)",
        en_d="Form 12D", ta_d="படிவம் 12D (Form 12D)",
        correct_key="A",
        exp_en="Under the Representation of the People (Amendment) Act, 2010 and the Registration of Electors Rules, an Overseas (NRI) citizen holding a valid Indian passport who has not acquired citizenship of another country must apply in Form 6A.",
        exp_ta="மக்கள் பிரதிநிதித்துவ திருத்தச் சட்டம் 2010-ன் படி, இந்திய குடியுரிமை கொண்ட வெளிநாடு வாழ் இந்தியர் (NRI) வாக்காளர் பட்டியலில் பதிவு செய்ய படிவம் 6A-ஐ சமர்ப்பிக்க வேண்டும்.",
        why_a_en="Correct. Form 6A is for Overseas electors.",
        why_a_ta="சரியானது. படிவம் 6A வெளிநாடு வாழ் இந்தியர் பதிவிற்கானது.",
        why_b_en="Incorrect. Form 6 is for resident domestic electors.",
        why_b_ta="தவறானது. படிவம் 6 இந்தியாவில் வசிக்கும் வாக்காளர்களுக்கானது.",
        why_c_en="Incorrect. Form 8A was previously for transposition within a constituency (now merged into Form 8).",
        why_c_ta="தவறானது. படிவம் 8A தற்போது பயன்பாட்டில் இல்லை.",
        why_d_en="Incorrect. Form 12D is for postal ballot facility for senior citizens (85+) and PwD voters.",
        why_d_ta="தவறானது. படிவம் 12D மூத்த குடிமக்கள் மற்றும் மாற்றுத்திறனாளிகளுக்கான தபால் வாக்கு படிவமாகும்.",
        tip_en="Overseas electors can enroll using Form 6A, but under present law they must vote in person at the polling booth in India.",
        tip_ta="NRI வாக்காளர்கள் படிவம் 6A மூலம் பதிவு செய்யலாம்; ஆனால் தற்போது நேரில் வந்து மட்டுமே வாக்களிக்க முடியும்.",
        fact_en="The 2010 amendment inserted Section 20A in RPA 1950 granting voting rights to NRIs.",
        fact_ta="2010 திருத்தச் சட்டம் RPA 1950-ல் பிரிவு 20A-ஐ இணைத்து NRI-களுக்கு வாக்குரிமை வழங்கியது.",
        tags=["Form 6A", "NRI Voting", "Overseas Electors"]
    ))

    # ER_E_031
    qs.append(make_er_q(
        qid="ER_E_031", diff="Easy", qtype="Single-Choice", subtopic="Security Deposit",
        en_stem="What percentage of the total valid votes polled must a candidate secure in an election to save their security deposit from being forfeited?",
        ta_stem="ஒரு தேர்தலில் போட்டியிடும் வேட்பாளர் தனது தேர்தல் வைப்புத்தொகையை (Security Deposit) இழக்காமல் திரும்பப் பெற பதிவான மொத்த செல்லுபடியாகும் வாக்குகளில் எத்தனை சதவீதத்தைப் பெற வேண்டும்?",
        en_a="More than one-sixth (1/6th or ~16.67%) of valid votes", ta_a="செல்லுபடியாகும் வாக்குகளில் ஆறில் ஒரு பங்கிற்கு மேல் (1/6 அல்லது ~16.67%)",
        en_b="More than one-tenth (1/10th or 10%) of valid votes", ta_b="செல்லுபடியாகும் வாக்குகளில் பத்தில் ஒரு பங்கிற்கு மேல் (1/10 அல்லது 10%)",
        en_c="More than one-fourth (1/4th or 25%) of valid votes", ta_c="செல்லுபடியாகும் வாக்குகளில் நான்கில் ஒரு பங்கிற்கு மேல் (1/4 அல்லது 25%)",
        en_d="More than one-third (1/3rd or ~33.33%) of valid votes", ta_d="செல்லுபடியாகும் வாக்குகளில் மூன்றில் ஒரு பங்கிற்கு மேல் (1/3 அல்லது ~33.33%)",
        correct_key="A",
        exp_en="Under Section 158 of the Representation of the People Act, 1951, a candidate forfeits their security deposit if they fail to secure more than one-sixth (1/6th) of the total number of valid votes polled in the constituency.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 158-ன் படி, ஒரு வேட்பாளர் அத்தொகுதியில் பதிவான மொத்த செல்லுபடியாகும் வாக்குகளில் ஆறில் ஒரு பங்கிற்கு மேல் (1/6) பெறத் தவறினால், அவரது வைப்புத்தொகை பறிமுதல் செய்யப்படும்.",
        why_a_en="Correct. More than 1/6th (one-sixth) of valid votes.",
        why_a_ta="சரியானது. செல்லுபடியாகும் வாக்குகளில் ஆறில் ஒரு பங்கிற்கு (1/6) மேல் பெற வேண்டும்.",
        why_b_en="Incorrect. 1/10th is the quorum for parliamentary sittings.",
        why_b_ta="தவறானது. 1/10 என்பது நாடாளுமன்ற கூட்டங்களுக்கான கோரம்.",
        why_c_en="Incorrect. 1/4th is incorrect.",
        why_c_ta="தவறானது. 1/4 என்பது தவறானது.",
        why_d_en="Incorrect. 1/3rd is the reservation percentage for women.",
        why_d_ta="தவறானது. 1/3 என்பது பெண்களுக்கான இடஒதுக்கீடு.",
        tip_en="For Lok Sabha: General deposit is ₹25,000 (SC/ST: ₹12,500). For Assembly: General is ₹10,000 (SC/ST: ₹5,000).",
        tip_ta="மக்களவை வைப்புத்தொகை: பொது ₹25,000 (SC/ST ₹12,500). சட்டசபை: பொது ₹10,000 (SC/ST ₹5,000).",
        fact_en="Even if a candidate wins the election, if they somehow get less than 1/6th (in multi-member seats historically), they could forfeit deposit; but the winning candidate always gets the deposit returned.",
        fact_ta="வெற்றி பெறும் வேட்பாளருக்கு எப்போதும் வைப்புத்தொகை திருப்பித் தரப்படும்.",
        tags=["Security Deposit", "1/6th Valid Votes", "Section 158"]
    ))

    # ER_E_032
    qs.append(make_er_q(
        qid="ER_E_032", diff="Easy", qtype="Single-Choice", subtopic="Security Deposit",
        en_stem="What is the current security deposit amount required for a general category candidate contesting a Lok Sabha election?",
        ta_stem="மக்களவைத் தேர்தலில் போட்டியிடும் ஒரு பொதுப்பிரிவு வேட்பாளருக்கு நிர்ணயிக்கப்பட்டுள்ள தற்போதைய தேர்தல் வைப்புத்தொகை எவ்வளவு?",
        en_a="₹25,000", ta_a="₹25,000",
        en_b="₹10,000", ta_b="₹10,000",
        en_c="₹50,000", ta_c="₹50,000",
        en_d="₹5,000", ta_d="₹5,000",
        correct_key="A",
        exp_en="Under Section 34 of RPA 1951 (amended in 2009), the security deposit for a Lok Sabha election candidate is ₹25,000 for general category candidates and ₹12,500 for Scheduled Caste (SC) and Scheduled Tribe (ST) candidates.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 34-ன் படி (2009-ல் திருத்தப்பட்டது), மக்களவைத் தேர்தலுக்கு பொதுப்பிரிவு வேட்பாளர்களுக்கு ₹25,000 மற்றும் SC/ST பிரிவு வேட்பாளர்களுக்கு ₹12,500 வைப்புத்தொகையாக நிர்ணயிக்கப்பட்டுள்ளது.",
        why_a_en="Correct. ₹25,000 for Lok Sabha general category.",
        why_a_ta="சரியானது. மக்களவை பொதுப்பிரிவுக்கு ₹25,000.",
        why_b_en="Incorrect. ₹10,000 is the deposit for State Legislative Assembly elections.",
        why_b_ta="தவறானது. ₹10,000 என்பது சட்டசபைத் தேர்தலுக்கான வைப்புத்தொகை.",
        why_c_en="Incorrect. ₹50,000 is incorrect.",
        why_c_ta="தவறானது. ₹50,000 தவறானது.",
        why_d_en="Incorrect. ₹5,000 is the SC/ST deposit for Assembly elections.",
        why_d_ta="தவறானது. ₹5,000 என்பது சட்டசபைத் தேர்தலில் SC/ST பிரிவினருக்கான தொகை.",
        tip_en="Prior to 2009, the deposit was ₹10,000 for Lok Sabha and ₹5,000 for Assembly.",
        tip_ta="2009-க்கு முன்பு மக்களவை வைப்புத்தொகை ₹10,000 ஆகவும் சட்டசபைக்கு ₹5,000 ஆகவும் இருந்தது.",
        fact_en="The deposit was increased to discourage non-serious and frivolous candidates.",
        fact_ta="தேவையற்ற, தீவிரமற்ற வேட்பாளர்களின் எண்ணிக்கையைக் குறைப்பதற்காக இத்தொகை உயர்த்தப்பட்டது.",
        tags=["Security Deposit Amount", "Lok Sabha", "Section 34"]
    ))

    # ER_E_033
    qs.append(make_er_q(
        qid="ER_E_033", diff="Easy", qtype="Single-Choice", subtopic="Exit Polls",
        en_stem="Under Section 126A of the Representation of the People Act, 1951, what is the legal prohibition regarding Exit Polls?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 126A-ன் கீழ், தேர்தல் பிந்தைய கருத்துக் கணிப்புகள் (Exit Polls) தொடர்பாக உள்ள சட்டப்பூர்வ தடை என்ன?",
        en_a="Exit polls cannot be conducted or published during the entire voting period across all phases", ta_a="அனைத்து கட்ட வாக்குப்பதிவுகளும் முடியும் வரை வாக்குக்கணிப்பு நடத்தவோ முடிவுகளை வெளியிடவோ முடியாது",
        en_b="Exit polls can be broadcast live as soon as each individual phase concludes", ta_b="ஒவ்வொரு கட்ட வாக்குப்பதிவு முடிந்த உடனேயே முடிவுகளை நேரடியாக ஒளிபரப்பலாம்",
        en_c="Exit polls are completely permitted without any restrictions", ta_c="எவ்வித கட்டுப்பாடுகளும் இன்றி எப்போதும் வெளியிட முழு அனுமதி உண்டு",
        en_d="Exit polls are permanently banned in India for all time", ta_d="இந்தியாவில் வாக்குக்கணிப்புகளுக்கு வாழ்நாள் முழுதும் நிரந்தர தடை விதிக்கப்பட்டுள்ளது",
        correct_key="A",
        exp_en="Section 126A of RPA 1951 (inserted in 2009) prohibits the conduct of exit polls and dissemination of their results through print or electronic media from the beginning of polling in the first phase until half an hour after the close of polling in the final phase.",
        exp_ta="2009-ல் சேர்க்கப்பட்ட பிரிவு 126A-ன் படி, முதல் கட்ட வாக்குப்பதிவு தொடங்கும் நேரம் முதல் இறுதிக்கட்ட வாக்குப்பதிவு நிறைவடைந்த அரை மணி நேரம் வரை வாக்குக்கணிப்புகளை நடத்துவதோ அல்லது ஊடகங்களில் வெளியிடுவதோ சட்டப்படி தடை செய்யப்பட்டுள்ளது.",
        why_a_en="Correct. Banned from start of phase 1 until 30 mins after final phase ends.",
        why_a_ta="சரியானது. முதல் கட்டம் தொடங்கி இறுதிக் கட்டம் முடியும் வரை வாக்குக்கணிப்புக்கு தடை உள்ளது.",
        why_b_en="Incorrect. Broadcaster cannot publish phase-by-phase exit polls.",
        why_b_ta="தவறானது. கட்டம் வாரியாக வெளியிட அனுமதி இல்லை.",
        why_c_en="Incorrect. Strict statutory prohibition applies.",
        why_c_ta="தவறானது. சட்டப்பூர்வ தடை உள்ளது.",
        why_d_en="Incorrect. Not a permanent lifetime ban; results can be published after the final phase closes.",
        why_d_ta="தவறானது. இறுதிக்கட்டம் முடிந்த பின் வெளியிடலாம்.",
        tip_en="Violation of Section 126A attracts imprisonment up to 2 years or fine or both.",
        tip_ta="பிரிவு 126A-ஐ மீறினால் 2 ஆண்டுகள் வரை சிறைத்தண்டனை அல்லது அபராதம் விதிக்கப்படும்.",
        fact_en="Section 126 prohibits public campaign meetings and display of election matter 48 hours before polling ends.",
        fact_ta="பிரிவு 126 வாக்குப்பதிவு முடிவதற்கு 48 மணி நேரத்திற்கு முன் பொதுக்கூட்டங்கள் மற்றும் தேர்தல் பிரச்சாரங்களை தடை செய்கிறது.",
        tags=["Exit Polls", "Section 126A", "RPA 1951"]
    ))

    # ER_E_034
    qs.append(make_er_q(
        qid="ER_E_034", diff="Easy", qtype="Single-Choice", subtopic="Campaign Silence Period",
        en_stem="Under Section 126 of the Representation of the People Act, 1951, election campaigning must stop how many hours prior to the conclusion of polling?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 126-ன் கீழ், வாக்குப்பதிவு முடிவடைவதற்கு எத்தனை மணி நேரத்திற்கு முன்பாக தேர்தல் பிரச்சாரம் நிறுத்தப்பட வேண்டும்?",
        en_a="48 hours", ta_a="48 மணி நேரம்",
        en_b="24 hours", ta_b="24 மணி நேரம்",
        en_c="72 hours", ta_c="72 மணி நேரம்",
        en_d="36 hours", ta_d="36 மணி நேரம்",
        correct_key="A",
        exp_en="Section 126 of the Representation of the People Act, 1951 prohibits holding public meetings, processions, and propaganda during the period of 48 hours ending with the hour fixed for the conclusion of the poll (known as the 'campaign silence period').",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 126-ன் படி, வாக்குப்பதிவு முடிவடைவதற்காக நிர்ணயிக்கப்பட்ட நேரத்திற்கு முந்தைய 48 மணி நேரக் காலத்தில் பொதுக்கூட்டங்கள், ஊர்வலங்கள் மற்றும் தேர்தல் பிரச்சாரங்கள் நடத்துவது தடை செய்யப்பட்டுள்ளது (அமைதிக்காலம்).",
        why_a_en="Correct. 48 hours ending with the hour fixed for the conclusion of the poll.",
        why_a_ta="சரியானது. வாக்குப்பதிவு முடிவடையும் நேரத்திற்கு முந்தைய 48 மணி நேரம்.",
        why_b_en="Incorrect. 24 hours is incorrect.",
        why_b_ta="தவறானது. 24 மணி நேரம் தவறானது.",
        why_c_en="Incorrect. 72 hours is incorrect.",
        why_c_ta="தவறானது. 72 மணி நேரம் தவறானது.",
        why_d_en="Incorrect. 36 hours is incorrect.",
        why_d_ta="தவறானது. 36 மணி நேரம் தவறானது.",
        tip_en="Remember: 48 hours is counted backwards from the END of the poll, not the START of the poll.",
        tip_ta="நினைவில் கொள்க: வாக்குப்பதிவு முடியும் நேரத்திலிருந்து பின்னோக்கி 48 மணி நேரம் கணக்கிடப்படுகிறது.",
        fact_en="Television and electronic media are also prohibited from displaying election matter during these 48 hours.",
        fact_ta="இந்த 48 மணி நேரத்தில் தொலைக்காட்சி மற்றும் சமூக ஊடகங்களிலும் தேர்தல் பிரச்சாரங்களை ஒளிபரப்ப தடை விதிக்கப்பட்டுள்ளது.",
        tags=["Section 126", "48 Hours Silence", "Campaign Ban"]
    ))

    # ER_E_035
    qs.append(make_er_q(
        qid="ER_E_035", diff="Easy", qtype="Single-Choice", subtopic="Election Petitions",
        en_stem="Under Article 329(b) and the Representation of the People Act, 1951, which judicial forum has the original jurisdiction to try an Election Petition calling in question an election to Parliament or State Legislature?",
        ta_stem="சரத்து 329(b) மற்றும் மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் கீழ், நாடாளுமன்றம் அல்லது மாநில சட்டமன்றத் தேர்தலை எதிர்த்து தொடரப்படும் தேர்தல் வழக்குகளை (Election Petition) விசாரிக்கும் அசல் அதிகார வரம்பு எந்த நீதிமன்றத்திற்கு உள்ளது?",
        en_a="High Court", ta_a="உயர் நீதிமன்றம்",
        en_b="Supreme Court exclusively", ta_b="உச்ச நீதிமன்றத்திற்கு மட்டுமே",
        en_c="District and Sessions Court", ta_c="மாவட்ட மற்றும் அமர்வு நீதிமன்றம்",
        en_d="Central Administrative Tribunal", ta_d="மத்திய தீர்ப்பாயம்",
        correct_key="A",
        exp_en="By the 19th Constitutional Amendment Act, 1966, Election Tribunals were abolished, and the original jurisdiction to try election petitions questioning parliamentary and assembly elections was vested in the High Court under Section 80A of RPA 1951.",
        exp_ta="1966-ல் கொண்டுவரப்பட்ட 19-வது அரசியலமைப்புத் திருத்தத்தின் மூலம் தேர்தல் தீர்ப்பாயங்கள் ஒழிக்கப்பட்டு, நாடாளுமன்ற மற்றும் சட்டமன்றத் தேர்தல் வழக்குகளை விசாரிக்கும் அசல் அதிகார வரம்பு மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 80A-ன் கீழ் உயர் நீதிமன்றத்திற்கு வழங்கப்பட்டது.",
        why_a_en="Correct. High Court has original jurisdiction to try election petitions.",
        why_a_ta="சரியானது. உயர் நீதிமன்றத்திற்கு தேர்தல் வழக்குகளை விசாரிக்கும் அசல் அதிகார வரம்பு உண்டு.",
        why_b_en="Incorrect. Supreme Court hears appeals from High Court judgments under Section 116A, and has original jurisdiction only for Presidential/Vice-Presidential elections (Art 71).",
        why_b_ta="தவறானது. குடியரசுத் தலைவர்/துணைக் குடியரசுத் தலைவர் தேர்தல் வழக்குகளை மட்டுமே உச்ச நீதிமன்றம் நேரடியாக விசாரிக்கும் (சரத்து 71).",
        why_c_en="Incorrect. District courts have no jurisdiction over parliamentary/assembly election petitions.",
        why_c_ta="தவறானது. மாவட்ட நீதிமன்றங்களுக்கு அதிகார வரம்பு இல்லை.",
        why_d_en="Incorrect. CAT deals only with civil servant service matters.",
        why_d_ta="தவறானது. CAT அரசுப் பணியாளர் சேவை விவகாரங்களை மட்டுமே கையாள்கிறது.",
        tip_en="An election petition must be presented within 45 days from the date of declaration of the election result.",
        tip_ta="தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட நாளிலிருந்து 45 நாட்களுக்குள் தேர்தல் மனு தாக்கல் செய்யப்பட வேண்டும்.",
        fact_en="The 19th Amendment Act 1966 abolished the earlier system of Election Tribunals.",
        fact_ta="1966-ன் 19-வது சட்டத்திருத்தம் முந்தைய தேர்தல் தீர்ப்பாயங்களை ஒழித்தது.",
        tags=["Election Petitions", "High Court", "Article 329(b)", "Section 80A"]
    ))

    # ER_E_036
    qs.append(make_er_q(
        qid="ER_E_036", diff="Easy", qtype="Single-Choice", subtopic="Election Petitions",
        en_stem="Within how many days from the date of declaration of the election result must an Election Petition be filed before the High Court?",
        ta_stem="தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட நாளிலிருந்து எத்தனை நாட்களுக்குள் உயர் நீதிமன்றத்தில் தேர்தல் மனு (Election Petition) தாக்கல் செய்யப்பட வேண்டும்?",
        en_a="45 days", ta_a="45 நாட்கள்",
        en_b="30 days", ta_b="30 நாட்கள்",
        en_c="60 days", ta_c="60 நாட்கள்",
        en_d="90 days", ta_d="90 நாட்கள்",
        correct_key="A",
        exp_en="Under Section 81 of the Representation of the People Act, 1951, an election petition calling in question any election may be presented within 45 days, but not earlier than the date of election of the returned candidate.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 81-ன் படி, தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட நாளிலிருந்து 45 நாட்களுக்குள் தேர்தல் மனு உயர் நீதிமன்றத்தில் தாக்கல் செய்யப்பட வேண்டும்.",
        why_a_en="Correct. Exactly 45 days under Section 81 of RPA 1951.",
        why_a_ta="சரியானது. பிரிவு 81-ன் படி சரியாக 45 நாட்கள்.",
        why_b_en="Incorrect. 30 days is the deadline for lodging election expense accounts.",
        why_b_ta="தவறானது. 30 நாட்கள் என்பது தேர்தல் செலவுக் கணக்கு தாக்கல் செய்வதற்கான காலக்கெடுவாகும்.",
        why_c_en="Incorrect. 60 days is incorrect.",
        why_c_ta="தவறானது. 60 நாட்கள் தவறானது.",
        why_d_en="Incorrect. 90 days is incorrect.",
        why_d_ta="தவறானது. 90 நாட்கள் தவறானது.",
        tip_en="Section 86(7) provides that the High Court shall endeavor to conclude the trial within 6 months.",
        tip_ta="பிரிவு 86(7)-ன் படி உயர் நீதிமன்றம் 6 மாதங்களுக்குள் வழக்கின் விசாரணையை முடிக்க முயற்சி செய்ய வேண்டும்.",
        fact_en="Failure to file within 45 days results in automatic dismissal of the petition under Section 86(1).",
        fact_ta="45 நாட்களுக்குள் தாக்கல் செய்யத் தவறினால் மனு பிரிவு 86(1)-ன் கீழ் தானாக தள்ளுபடி செய்யப்படும்.",
        tags=["Election Petition Deadline", "45 Days", "Section 81"]
    ))

    # ER_E_037
    qs.append(make_er_q(
        qid="ER_E_037", diff="Easy", qtype="Single-Choice", subtopic="Election Expenses",
        en_stem="Within how many days from the date of declaration of the election results must every contesting candidate lodge an account of their election expenses with the District Election Officer?",
        ta_stem="தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட நாளிலிருந்து எத்தனை நாட்களுக்குள் போட்டியிட்ட ஒவ்வொரு வேட்பாளரும் தங்கள் தேர்தல் செலவுக் கணக்குகளை மாவட்ட தேர்தல் அதிகாரியிடம் சமர்ப்பிக்க வேண்டும்?",
        en_a="30 days", ta_a="30 நாட்கள்",
        en_b="15 days", ta_b="15 நாட்கள்",
        en_c="45 days", ta_c="45 நாட்கள்",
        en_d="60 days", ta_d="60 நாட்கள்",
        correct_key="A",
        exp_en="Under Section 78 of the Representation of the People Act, 1951, every contesting candidate must, within 30 days from the date of declaration of the result, lodge an account of election expenses with the District Election Officer (DEO).",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 78-ன் படி, தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட நாளிலிருந்து 30 நாட்களுக்குள் போட்டியிட்ட ஒவ்வொரு வேட்பாளரும் தங்கள் தேர்தல் செலவுக் கணக்கை மாவட்ட தேர்தல் அதிகாரியிடம் சமர்ப்பிக்க வேண்டும்.",
        why_a_en="Correct. 30 days under Section 78.",
        why_a_ta="சரியானது. பிரிவு 78-ன் கீழ் 30 நாட்கள்.",
        why_b_en="Incorrect. 15 days is too short.",
        why_b_ta="தவறானது. 15 நாட்கள் மிகவும் குறைவு.",
        why_c_en="Incorrect. 45 days is for filing an election petition.",
        why_c_ta="தவறானது. 45 நாட்கள் என்பது தேர்தல் மனு தாக்கல் செய்வதற்கான காலக்கெடு.",
        why_d_en="Incorrect. 60 days is incorrect.",
        why_d_ta="தவறானது. 60 நாட்கள் தவறானது.",
        tip_en="Failure to lodge expenses within 30 days without good reason leads to 3-year disqualification under Section 10A.",
        tip_ta="தக்க காரணமின்றி 30 நாட்களுக்குள் கணக்கு தாக்கல் செய்யாவிட்டால் பிரிவு 10A-ன் கீழ் 3 ஆண்டுகள் தகுதிநீக்கம் செய்யப்படுவர்.",
        fact_en="Section 77 mandates maintaining day-to-day accounts from nomination date to result date.",
        fact_ta="பிரிவு 77 வேட்புமனு தாக்கல் செய்தது முதல் முடிவு அறிவிக்கப்படும் வரை தினசரி செலவுக் கணக்குகளைப் பராமரிப்பதை கட்டாயமாக்குகிறது.",
        tags=["Election Expenses", "30 Days", "Section 78", "DEO"]
    ))

    # ER_E_038
    qs.append(make_er_q(
        qid="ER_E_038", diff="Easy", qtype="Single-Choice", subtopic="Disqualification for Expense Default",
        en_stem="Under Section 10A of the Representation of the People Act, 1951, what is the maximum period of disqualification imposed by the ECI for failure to lodge an account of election expenses?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 10A-ன் கீழ், தேர்தல் செலவுக் கணக்குகளை தாக்கல் செய்யத் தவறியதற்காக தேர்தல் ஆணையத்தால் விதிக்கப்படும் அதிகபட்ச தகுதிநீக்கக் காலம் என்ன?",
        en_a="3 years from the date of the order", ta_a="உத்தரவு பிறப்பிக்கப்பட்ட நாளிலிருந்து 3 ஆண்டுகள்",
        en_b="6 years from the date of election", ta_b="தேர்தல் நாளிலிருந்து 6 ஆண்டுகள்",
        en_c="5 years", ta_c="5 ஆண்டுகள்",
        en_d="1 year", ta_d="1 ஆண்டு",
        correct_key="A",
        exp_en="Section 10A of RPA 1951 empowers the Election Commission to disqualify a person from being chosen as, and from being, a member of Parliament or State Legislature for a period of 3 years from the date of the order if they fail to lodge election expenses within time without good cause.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 10A, சரியான காரணமின்றி உரிய காலத்திற்குள் தேர்தல் செலவுக் கணக்குகளைத் தாக்கல் செய்யத் தவறும் நபரை, உத்தரவு பிறப்பிக்கப்பட்ட நாளிலிருந்து 3 ஆண்டுகளுக்கு தகுதிநீக்கம் செய்ய தேர்தல் ஆணையத்திற்கு அதிகாரம் அளிக்கிறது.",
        why_a_en="Correct. 3 years under Section 10A.",
        why_a_ta="சரியானது. பிரிவு 10A-ன் கீழ் 3 ஆண்டுகள்.",
        why_b_en="Incorrect. 6 years is the post-release disqualification under Section 8(3).",
        why_b_ta="தவறானது. 6 ஆண்டுகள் என்பது பிரிவு 8(3)-ன் கீழ் சிறை விடுதலையான பின்னரான தகுதிநீக்கம்.",
        why_c_en="Incorrect. 5 years is incorrect.",
        why_c_ta="தவறானது. 5 ஆண்டுகள் தவறானது.",
        why_d_en="Incorrect. 1 year is incorrect.",
        why_d_ta="தவறானது. 1 ஆண்டு தவறானது.",
        tip_en="Remember: Criminal conviction (Sec 8) = 6 years post release; Expense default (Sec 10A) = 3 years.",
        tip_ta="நினைவில் கொள்க: குற்றவியல் தண்டனை (பிரிவு 8) = விடுதலைக்கு பின் 6 ஆண்டுகள்; செலவுக் கணக்கு பாக்கி (பிரிவு 10A) = 3 ஆண்டுகள்.",
        fact_en="In Umlesh Yadav case (2011), an MLA was disqualified under Section 10A for 3 years for failing to declare paid news expenditure.",
        fact_ta="2011-ல் உம்லேஷ் யாதவ் என்ற எம்.எல்.ஏ ஊதியச் செய்தி (Paid News) செலவை மறைத்ததற்காக பிரிவு 10A-ன் கீழ் 3 ஆண்டுகள் தகுதிநீக்கம் செய்யப்பட்டார்.",
        tags=["Section 10A", "3 Years Disqualification", "Expense Default"]
    ))

    # ER_E_039
    qs.append(make_er_q(
        qid="ER_E_039", diff="Easy", qtype="Single-Choice", subtopic="Two Constituencies Restriction",
        en_stem="Under Section 33(7) of the Representation of the People Act, 1951 (amended in 1996), a person cannot contest a general election from more than how many constituencies?",
        ta_stem="1996-ல் திருத்தப்பட்ட மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 33(7)-ன் கீழ், ஒருவர் பொதுத்தேர்தலில் எத்தனைக்கு மேற்பட்ட தொகுதிகளில் போட்டியிட முடியாது?",
        en_a="More than 2 constituencies", ta_a="2 தொகுதிகளுக்கு மேல்",
        en_b="More than 1 constituency", ta_b="1 தொகுதிக்கு மேல்",
        en_c="More than 3 constituencies", ta_c="3 தொகுதிகளுக்கு மேல்",
        en_d="More than 4 constituencies", ta_d="4 தொகுதிகளுக்கு மேல்",
        correct_key="A",
        exp_en="By an amendment in 1996, Section 33(7) of RPA 1951 restricted a candidate from contesting from more than two constituencies simultaneously in a general election or by-elections to the Lok Sabha or State Assembly.",
        exp_ta="1996-ல் செய்யப்பட்ட சட்டத்திருத்தத்தின் மூலம், மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 33(7), ஒரு வேட்பாளர் மக்களவை அல்லது சட்டமன்றத் தேர்தலில் இரண்டுக்கு மேற்பட்ட தொகுதிகளில் ஒரே நேரத்தில் போட்டியிடுவதைத் தடை செய்தது.",
        why_a_en="Correct. Restricted to a maximum of 2 constituencies under Section 33(7).",
        why_a_ta="சரியானது. பிரிவு 33(7)-ன் கீழ் அதிகபட்சம் 2 தொகுதிகளில் மட்டுமே போட்டியிட முடியும்.",
        why_b_en="Incorrect. The Law Commission and ECI have recommended restricting it to 1 constituency, but the current law allows 2.",
        why_b_ta="தவறானது. 1 தொகுதி என மாற்ற தேர்தல் ஆணையம் பரிந்துரைத்துள்ளது, ஆனால் தற்போதைய சட்டம் 2 தொகுதிகளை அனுமதிக்கிறது.",
        why_c_en="Incorrect. Prior to 1996, candidates could contest from any number of constituencies.",
        why_c_ta="தவறானது. 1996-க்கு முன் எத்தனை தொகுதிகளிலும் போட்டியிட முடிந்தது.",
        why_d_en="Incorrect. 4 constituencies is incorrect.",
        why_d_ta="தவறானது. 4 தொகுதிகள் தவறானது.",
        tip_en="If a candidate wins both seats, they must vacate one seat within 10 days under Section 70, leading to a by-election.",
        tip_ta="ஒருவர் 2 தொகுதிகளிலும் வெற்றி பெற்றால், பிரிவு 70-ன் படி 10 நாட்களுக்குள் ஒரு தொகுதியை ராஜினாமா செய்ய வேண்டும்.",
        fact_en="ECI has proposed amending Section 33(7) to 'one candidate, one constituency' or making candidates pay the cost of the subsequent by-election.",
        fact_ta="ஒரு வேட்பாளர் ஒரு தொகுதியில் மட்டுமே போட்டியிட வேண்டும் அல்லது இடைத்தேர்தல் செலவை வேட்பாளரே ஏற்க வேண்டும் என ECI பரிந்துரைத்துள்ளது.",
        tags=["Section 33(7)", "Two Seats Limit", "1996 Amendment"]
    ))

    # ER_E_040
    qs.append(make_er_q(
        qid="ER_E_040", diff="Easy", qtype="Single-Choice", subtopic="Braille on EVMs",
        en_stem="In which year did the Election Commission of India introduce Braille signage on EVMs across all polling booths nationwide to assist visually impaired voters?",
        ta_stem="பார்வையற்ற வாக்காளர்களுக்கு உதவும் வகையில் நாடு முழுவதும் உள்ள அனைத்து வாக்குச்சாவடிகளிலும் EVM இயந்திரங்களில் பிரெய்லி (Braille) குறியீடுகளை தேர்தல் ஆணையம் எந்த ஆண்டு அறிமுகப்படுத்தியது?",
        en_a="2009", ta_a="2009",
        en_b="1999", ta_b="1999",
        en_c="2004", ta_c="2004",
        en_d="2019", ta_d="2019",
        correct_key="A",
        exp_en="The Election Commission introduced Braille signage on the ballot unit of EVMs nationwide during the 2009 Parliamentary Elections to empower visually impaired voters to cast their votes independently and secretly.",
        exp_ta="பார்வையற்ற வாக்காளர்கள் யாருடைய உதவியும் இன்றி ரகசியமாக வாக்களிக்க உதவும் வகையில், 2009 நாடாளுமன்றப் பொதுத்தேர்தலின் போது நாடு முழுவதும் உள்ள EVM இயந்திரங்களின் வாக்குப்பதிவு அலகில் பிரெய்லி குறியீடுகள் அறிமுகப்படுத்தப்பட்டன.",
        why_a_en="Correct. Introduced nationwide in the 2009 Lok Sabha elections.",
        why_a_ta="சரியானது. 2009 மக்களவைத் தேர்தலில் நாடு முழுவதும் அறிமுகப்படுத்தப்பட்டது.",
        why_b_en="Incorrect. 1999 was too early.",
        why_b_ta="தவறானது. 1999 தவறானது.",
        why_c_en="Incorrect. 2004 had first nationwide EVMs, but Braille was not universally standard then.",
        why_c_ta="தவறானது. 2004-ல் அனைத்து தொகுதிகளிலும் EVM வந்தது, ஆனால் பிரெய்லி முழுமையாக அப்போது வரவில்லை.",
        why_d_en="Incorrect. 2019 was the year of 100% VVPAT deployment.",
        why_d_ta="தவறானது. 2019-ல் 100% VVPAT பயன்படுத்தப்பட்டது.",
        tip_en="Braille embossed serial numbers (1 to 16) are embossed on the right side of the blue voting buttons.",
        tip_ta="நீல நிற வாக்கு பொத்தான்களின் வலதுபுறத்தில் பிரெய்லி வரிசை எண்கள் (1 முதல் 16 வரை) பொறிக்கப்பட்டுள்ளன.",
        fact_en="ECI also provides companion assistance under Rule 49N of Conduct of Elections Rules for electors with physical disabilities.",
        fact_ta="விதி 49N-ன் கீழ் உடல் குறைபாடுள்ள வாக்காளர்களுக்கு துணையாளர் உதவிக்கான விதியும் தேர்தல் விதிகளில் உள்ளது.",
        tags=["Braille on EVM", "2009", "Accessible Elections"]
    ))

    # ER_E_041
    qs.append(make_er_q(
        qid="ER_E_041", diff="Easy", qtype="Single-Choice", subtopic="C-Vigil App",
        en_stem="Which mobile application was launched by the Election Commission of India to allow citizens to report violations of the Model Code of Conduct directly with geo-tagged photos and videos?",
        ta_stem="மாதிரி தேர்தல் நடத்தை விதிகள் மீறப்படுவதை பொதுமக்கள் புகைப்படம் மற்றும் வீடியோவுடன் நேரடியாகப் புகாரளிக்க இந்திய தேர்தல் ஆணையத்தால் தொடங்கப்பட்ட மொபைல் செயலி எது?",
        en_a="cVIGIL", ta_a="cVIGIL (சி-விஜில்)",
        en_b="Suvidha", ta_b="சுவிதா (Suvidha)",
        en_c="Garuda", ta_c="கருடா (Garuda)",
        en_d="Saksham", ta_d="சக்ஷம் (Saksham)",
        correct_key="A",
        exp_en="cVIGIL (Citizen Vigilance) is a mobile app launched by ECI that enables fast-track reporting of Model Code of Conduct and expenditure violations. Once a citizen uploads a geotagged photo/video, flying squads are mandated to investigate within 100 minutes.",
        exp_ta="cVIGIL செயலி தேர்தல் நடத்தை விதிமீறல்கள் மற்றும் பணப்பட்டுவாடா புகார்களை பொதுமக்கள் எளிதாகப் பதிவு செய்ய ECI-யால் தொடங்கப்பட்டது. புகார் அளித்த 100 நிமிடங்களுக்குள் பறக்கும் படையினர் சம்பவ இடத்திற்குச் சென்று நடவடிக்கை எடுக்க வேண்டும்.",
        why_a_en="Correct. cVIGIL allows citizens to report MCC violations within a 100-minute turnaround.",
        why_a_ta="சரியானது. cVIGIL செயலி 100 நிமிடங்களில் நடவடிக்கை எடுக்கும் வகையில் செயல்படுகிறது.",
        why_b_en="Incorrect. Suvidha is a single-window portal for candidate campaign permissions.",
        why_b_ta="தவறானது. சுவிதா என்பது வேட்பாளர்கள் பிரச்சார அனுமதி பெறும் ஒற்றைச் சாளர இணையமாகும்.",
        why_c_en="Incorrect. Garuda was introduced for Booth Level Officers (BLOs) mapping.",
        why_c_ta="தவறானது. கருடா என்பது வாக்குச்சாவடி நிலை அதிகாரிகளுக்கான (BLO) செயலியாகும்.",
        why_d_en="Incorrect. Saksham app is designed specifically for Persons with Disabilities (PwDs).",
        why_d_ta="தவறானது. சக்ஷம் மாற்றுத்திறனாளிகளுக்கான பிரத்யேக செயலியாகும்.",
        tip_en="Remember the 100-minute benchmark: cVIGIL mandates grievance resolution and response within 100 minutes.",
        tip_ta="100 நிமிட காலக்கெடுவை நினைவில் கொள்க: cVIGIL-ல் புகார் மீது 100 நிமிடங்களுக்குள் தீர்வு காணப்பட வேண்டும்.",
        fact_en="cVIGIL automatically captures the GIS coordinates to direct the nearest Flying Squad (FST).",
        fact_ta="cVIGIL தானாகவே புவியியல் இருப்பிடத்தைக் (GIS) கண்டறிந்து அருகில் உள்ள பறக்கும் படையை சம்பவ இடத்திற்கு அனுப்புகிறது.",
        tags=["cVIGIL", "MCC Reporting", "Citizen App"]
    ))

    # ER_E_042
    qs.append(make_er_q(
        qid="ER_E_042", diff="Easy", qtype="Single-Choice", subtopic="Saksham App",
        en_stem="Which mobile application was launched by the Election Commission of India specifically to facilitate wheelchair requests, pick-and-drop, and registration for Persons with Disabilities (PwDs)?",
        ta_stem="மாற்றுத்திறனாளி (PwD) வாக்காளர்களுக்கு சக்கர நாற்காலி, வாகன வசதி மற்றும் வாக்காளர் பதிவு உதவிகளை வழங்க இந்திய தேர்தல் ஆணையத்தால் பிரத்யேகமாக தொடங்கப்பட்ட செயலி எது?",
        en_a="Saksham App", ta_a="சக்ஷம் செயலி (Saksham App)",
        en_b="cVIGIL App", ta_b="சி-விஜில் செயலி (cVIGIL)",
        en_c="KNOW YOUR CANDIDATE (KYC) App", ta_c="KYC செயலி",
        en_d="Voter Helpline App", ta_d="வாக்காளர் உதவி செயலி (Voter Helpline)",
        correct_key="A",
        exp_en="Saksham App is an initiative by the Election Commission of India designed specifically for Persons with Disabilities (PwD) to access customized electoral services, including wheelchair booking and home voting requests.",
        exp_ta="சக்ஷம் (Saksham) செயலி மாற்றுத்திறனாளி வாக்காளர்களுக்கு சக்கர நாற்காலி முன்பதிவு, தபால் வாக்கு மற்றும் வீட்டு வாக்களிப்பு போன்ற சிறப்பு வசதிகளை வழங்க தேர்தல் ஆணையத்தால் தொடங்கப்பட்டது.",
        why_a_en="Correct. Saksham App is dedicated to Persons with Disabilities.",
        why_a_ta="சரியானது. சக்ஷம் மாற்றுத்திறனாளிகளுக்கான பிரத்யேக செயலியாகும்.",
        why_b_en="Incorrect. cVIGIL is for reporting MCC violations.",
        why_b_ta="தவறானது. cVIGIL தேர்தல் விதிமீறல்களைப் புகாரளிக்க பயன்படுகிறது.",
        why_c_en="Incorrect. KYC app is for checking criminal antecedents of contesting candidates.",
        why_c_ta="தவறானது. KYC செயலி வேட்பாளர்களின் குற்றப்பின்னணியை அறிய உதவுகிறது.",
        why_d_en="Incorrect. Voter Helpline App is for general electors.",
        why_d_ta="தவறானது. Voter Helpline பொதுவான வாக்காளர்களுக்கானது.",
        tip_en="'Saksham' in Hindi means capable/empowered; it manifests ECI's motto 'No Voter to be Left Behind'.",
        tip_ta="'எந்த ஒரு வாக்காளரும் விடுபடக்கூடாது' என்ற தேர்தல் ஆணையத்தின் குறிக்கோளுக்கு சக்ஷம் செயலி ஒரு சிறந்த சான்றாகும்.",
        fact_en="It features high contrast colors, screen readers, and text-to-speech for accessibility.",
        fact_ta="பார்வைக் குறைபாடுள்ளவர்களுக்கு உதவும் வகையில் உயர் வண்ண வேறுபாடு மற்றும் திரைப் படிக்கும் வசதிகளை இது கொண்டுள்ளது.",
        tags=["Saksham App", "PwD Voters", "Accessible Elections"]
    ))

    # ER_E_043
    qs.append(make_er_q(
        qid="ER_E_043", diff="Easy", qtype="Single-Choice", subtopic="Candidate Disclosure",
        en_stem="Which mobile application was introduced by ECI to enable voters to view the criminal antecedents and assets of contesting candidates directly on their smartphones?",
        ta_stem="போட்டியிடும் வேட்பாளர்களின் குற்றப்பின்னணி மற்றும் சொத்து விவரங்களை வாக்காளர்கள் தங்களது ஸ்மார்ட்போனில் நேரடியாகப் பார்க்க தேர்தல் ஆணையம் அறிமுகப்படுத்திய செயலி எது?",
        en_a="Know Your Candidate (KYC) App", ta_a="நோ யுவர் கேண்டிடேட் (KYC) செயலி",
        en_b="cVIGIL", ta_b="சி-விஜில் (cVIGIL)",
        en_c="ENCORE", ta_c="என்கோர் (ENCORE)",
        en_d="Suvidha", ta_d="சுவிதா (Suvidha)",
        correct_key="A",
        exp_en="The 'Know Your Candidate' (KYC) App enables citizens to browse through the list of candidates contesting in their constituency and inspect their criminal antecedents, educational qualifications, and Form 26 affidavits.",
        exp_ta="'Know Your Candidate' (KYC) செயலி வாக்காளர்கள் தங்கள் தொகுதியில் போட்டியிடும் வேட்பாளர்களின் குற்றப்பின்னணி, கல்வித்தகுதி மற்றும் படிவம் 26 உறுதிமொழிப் பத்திர விவரங்களை எளிதாகப் பார்க்க உதவுகிறது.",
        why_a_en="Correct. KYC app displays candidate affidavits and criminal records.",
        why_a_ta="சரியானது. KYC செயலி வேட்பாளர்களின் உறுதிமொழிப் பத்திர விவரங்களைக் காட்டுகிறது.",
        why_b_en="Incorrect. cVIGIL is for reporting violations.",
        why_b_ta="தவறானது. cVIGIL விதிமீறல்களைப் புகாரளிக்க பயன்படுகிறது.",
        why_c_en="Incorrect. ENCORE is the internal software portal used by Returning Officers.",
        why_c_ta="தவறானது. ENCORE என்பது தேர்தல் நடத்தும் அலுவலர்களின் உள்-செயல்பாட்டு மென்பொருளாகும்.",
        why_d_en="Incorrect. Suvidha is candidate permission portal.",
        why_d_ta="தவறானது. சுவிதா என்பது வேட்பாளர் அனுமதி பெறுவதற்கான போர்ட்டலாகும்.",
        tip_en="KYC app implements the Supreme Court's mandate on candidate transparency under Article 19(1)(a).",
        tip_ta="KYC செயலி வேட்பாளர்களின் வெளிப்படைத்தன்மை குறித்த உச்ச நீதிமன்றத்தின் உத்தரவுகளை நடைமுறைப்படுத்துகிறது.",
        fact_en="Political parties must also upload reasons why they selected a candidate with criminal antecedents instead of a person without crime records.",
        fact_ta="குற்றப்பின்னணி கொண்ட வேட்பாளரை ஏன் தேர்வு செய்தனர் என்ற காரணத்தையும் அரசியல் கட்சிகள் வெளியிட வேண்டும்.",
        tags=["KYC App", "Candidate Disclosure", "Transparency"]
    ))

    # ER_E_044
    qs.append(make_er_q(
        qid="ER_E_044", diff="Easy", qtype="Single-Choice", subtopic="Paid News",
        en_stem="Which committee is established at the district level to scrutinize and detect instances of 'Paid News' during elections?",
        ta_stem="தேர்தல்களின் போது 'ஊதியச் செய்தி' (Paid News) முறைகேடுகளைக் கண்காணித்துக் கண்டறிய மாவட்ட அளவில் அமைக்கப்படும் குழு எது?",
        en_a="Media Certification and Monitoring Committee (MCMC)", ta_a="ஊடகச் சான்றளிப்பு மற்றும் கண்காணிப்புக் குழு (MCMC)",
        en_b="District Vigilance Commission", ta_b="மாவட்ட ஊழல் கண்காணிப்பு ஆணையம்",
        en_c="Press Council District Bench", ta_c="பிரஸ் கவுன்சில் மாவட்ட அமர்வு",
        en_d="District Consumer Protection Forum", ta_d="மாவட்ட நுகர்வோர் பாதுகாப்பு மன்றம்",
        correct_key="A",
        exp_en="The Media Certification and Monitoring Committee (MCMC) functions at district and state levels to preview political advertisements, certify media content, and detect and track instances of Paid News for addition to candidate expenditure.",
        exp_ta="ஊடகச் சான்றளிப்பு மற்றும் கண்காணிப்புக் குழு (MCMC) மாவட்ட மற்றும் மாநில அளவில் செயல்பட்டு, அரசியல் விளம்பரங்களுக்கு முன்-சான்றளிப்பதுடன், ஊதியச் செய்திகளைக் (Paid News) கண்டறிந்து வேட்பாளரின் தேர்தல் செலவுக் கணக்கில் சேர்க்கிறது.",
        why_a_en="Correct. MCMC monitors and certifies media content and flags paid news.",
        why_a_ta="சரியானது. MCMC ஊடகச் செய்திகளையும் விளம்பரங்களையும் கண்காணிக்கிறது.",
        why_b_en="Incorrect. Not the vigilance commission.",
        why_b_ta="தவறானது. ஊழல் கண்காணிப்பு ஆணையம் அல்ல.",
        why_c_en="Incorrect. Press Council has no district benches.",
        why_c_ta="தவறானது. பிரஸ் கவுன்சிலுக்கு மாவட்ட அமர்வுகள் இல்லை.",
        why_d_en="Incorrect. Consumer forum deals with consumer disputes.",
        why_d_ta="தவறானது. நுகர்வோர் மன்றம் நுகர்வோர் வழக்குகளை மட்டுமே கையாள்கிறது.",
        tip_en="MCMC is headed at the district level by the District Election Officer (District Collector/DM).",
        tip_ta="மாவட்ட அளவில் MCMC குழு மாவட்ட தேர்தல் அதிகாரி (மாவட்ட ஆட்சியர்) தலைமையில் இயங்குகிறது.",
        fact_en="Paid News was first extensively defined by the Press Council of India in its 2010 report.",
        fact_ta="2010-ல் இந்திய பிரஸ் கவுன்சில் 'ஊதியச் செய்தி' குறித்த விரிவான அறிக்கையை வெளியிட்டது.",
        tags=["Paid News", "MCMC", "Media Monitoring"]
    ))

    # ER_E_045
    qs.append(make_er_q(
        qid="ER_E_045", diff="Easy", qtype="Single-Choice", subtopic="Postal Ballot Reforms",
        en_stem="What is the full form of 'ETPBS', the electronic system introduced by the ECI for service voters such as armed forces personnel?",
        ta_stem="ராணுவ வீரர்கள் போன்ற பணி வாக்காளர்களுக்கு (Service Voters) தபால் வாக்குகளை அனுப்ப ECI அறிமுகப்படுத்திய 'ETPBS' அமைப்பின் விரிவாக்கம் என்ன?",
        en_a="Electronically Transmitted Postal Ballot System", ta_a="Electronically Transmitted Postal Ballot System (மின்னணு முறையில் கடத்தப்படும் தபால் வாக்கு அமைப்பு)",
        en_b="Electronic Terminal Polling Ballot Scheme", ta_b="Electronic Terminal Polling Ballot Scheme",
        en_c="Electors Transmission Postal Booth Software", ta_c="Electors Transmission Postal Booth Software",
        en_d="Emergency Tracked Postal Ballot Service", ta_d="Emergency Tracked Postal Ballot Service",
        correct_key="A",
        exp_en="ETPBS stands for Electronically Transmitted Postal Ballot System. Developed by ECI with C-DAC, it transmits postal ballots electronically to registered service voters (armed forces, paramilitary, diplomatic missions), who print, mark, and return them by post.",
        exp_ta="ETPBS என்பதன் விரிவாக்கம் 'Electronically Transmitted Postal Ballot System' ஆகும். இது ராணுவ வீரர்கள் மற்றும் தூதரக அதிகாரிகளுக்கு மின்னணு முறையில் தபால் வாக்குகளை அனுப்பி, அவர்கள் வாக்கை அச்சிட்டு தபால் மூலம் திருப்பி அனுப்ப உதவுகிறது.",
        why_a_en="Correct. Electronically Transmitted Postal Ballot System.",
        why_a_ta="சரியானது. Electronically Transmitted Postal Ballot System.",
        why_b_en="Incorrect. Polling Ballot Scheme is incorrect.",
        why_b_ta="தவறானது. தவறான விரிவாக்கம்.",
        why_c_en="Incorrect. Postal Booth Software is incorrect.",
        why_c_ta="தவறானது. தவறான விரிவாக்கம்.",
        why_d_en="Incorrect. Emergency Tracked Service is incorrect.",
        why_d_ta="தவறானது. தவறான விரிவாக்கம்.",
        tip_en="The Conduct of Elections Rules, 1961 were amended in October 2016 to enable ETPBS.",
        tip_ta="ETPBS-ஐ அமல்படுத்த 2016 அக்டோபரில் தேர்தல் நடத்தை விதிகள் 1961 திருத்தப்பட்டன.",
        fact_en="Over 18 lakh service voters used ETPBS in the 2019 Lok Sabha elections, recording an unprecedented 60%+ turnout among defense personnel.",
        fact_ta="2019 மக்களவைத் தேர்தலில் 18 லட்சத்திற்கும் மேற்பட்ட ராணுவ வாக்காளர்கள் ETPBS மூலம் வாக்களித்தனர்.",
        tags=["ETPBS", "Service Voters", "Postal Ballot"]
    ))

    # ER_E_046
    qs.append(make_er_q(
        qid="ER_E_046", diff="Easy", qtype="Single-Choice", subtopic="Home Voting Facility",
        en_stem="Under the recent election rules amendment, what is the age threshold for Senior Citizens to avail the optional 'Home Voting' facility via postal ballot?",
        ta_stem="சமீபத்திய தேர்தல் விதிமுறைத் திருத்தத்தின்படி, மூத்த குடிமக்கள் தபால் வாக்கு மூலம் விருப்பத்தின் பேரில் 'வீட்டிலிருந்தே வாக்களிக்கும்' வசதியைப் பெற குறைந்தபட்ச வயது வரம்பு என்ன?",
        en_a="85 years and above", ta_a="85 வயது மற்றும் அதற்கு மேற்பட்டோர்",
        en_b="80 years and above", ta_b="80 வயது மற்றும் அதற்கு மேற்பட்டோர்",
        en_c="75 years and above", ta_c="75 வயது மற்றும் அதற்கு மேற்பட்டோர்",
        en_d="65 years and above", ta_d="65 வயது மற்றும் அதற்கு மேற்பட்டோர்",
        correct_key="A",
        exp_en="In March 2024, the Ministry of Law and Justice amended Rule 27A of the Conduct of Elections Rules, 1961, raising the eligibility age for senior citizens to avail the home voting postal ballot facility from 80 years to 85 years.",
        exp_ta="2024 மார்ச் மாதம் தேர்தல் நடத்தை விதிகள் 1961-ன் விதி 27A திருத்தப்பட்டு, மூத்த குடிமக்கள் வீட்டிலிருந்தே தபால் வாக்களிக்கும் வசதிக்கான குறைந்தபட்ச வயது வரம்பு 80 வயதிலிருந்து 85 வயதாக உயர்த்தப்பட்டது.",
        why_a_en="Correct. 85 years is the amended threshold as of 2024.",
        why_a_ta="சரியானது. 2024 திருத்தத்தின்படி 85 வயது தகுதி வரம்பாகும்.",
        why_b_en="Incorrect. 80 years was the previous threshold introduced in 2020 during Covid-19, amended in 2024.",
        why_b_ta="தவறானது. 80 வயது என்பது 2020-ல் கொண்டுவரப்பட்டு, 2024-ல் 85 ஆக உயர்த்தப்பட்டது.",
        why_c_en="Incorrect. 75 years is incorrect.",
        why_c_ta="தவறானது. 75 வயது தவறானது.",
        why_d_en="Incorrect. 65 years was initially proposed but never notified.",
        why_d_ta="தவறானது. 65 வயது தவறானது.",
        tip_en="Voters aged 85+ and Persons with Disabilities (PwD 40%+) can opt for Home Voting using Form 12D.",
        tip_ta="85 வயதுக்கு மேற்பட்டவர்கள் மற்றும் 40% மேல் மாற்றுத்திறன் கொண்டவர்கள் படிவம் 12D மூலம் வீட்டிலிருந்தே வாக்களிக்கலாம்.",
        fact_en="Polling teams visit the voter's home with video-recording to ensure complete secrecy and integrity.",
        fact_ta="முழு ரகசியத்தன்மையை உறுதி செய்ய வாக்குச்சாவடி குழுவினர் வீடியோ பதிவுடன் வாக்காளரின் வீட்டிற்குச் செல்கின்றனர்.",
        tags=["Home Voting", "85 Years", "Form 12D", "Senior Citizens"]
    ))

    # ER_E_047
    qs.append(make_er_q(
        qid="ER_E_047", diff="Easy", qtype="Single-Choice", subtopic="CEC and ECs Appointment Act 2023",
        en_stem="Who acts as the Chairperson of the 3-member Selection Committee for appointing the Chief Election Commissioner and other Election Commissioners under the 2023 Act?",
        ta_stem="2023 சட்டத்தின் கீழ் தலைமைத் தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்களை நியமிப்பதற்கான 3 உறுப்பினர்கள் கொண்ட தேர்வுக் குழுவின் தலைவராக யார் செயல்படுகிறார்?",
        en_a="Prime Minister", ta_a="பிரதமர்",
        en_b="Chief Justice of India", ta_b="இந்திய தலைமை நீதிபதி",
        en_c="Speaker of Lok Sabha", ta_c="மக்களவைத் தலைவர் (சபாநாயகர்)",
        en_d="Union Home Minister", ta_d="மத்திய உள்துறை அமைச்சர்",
        correct_key="A",
        exp_en="Under Section 7(1) of the Chief Election Commissioner and other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023, the Selection Committee is chaired by the Prime Minister of India.",
        exp_ta="தலைமைத் தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்கள் (நியமனம், சேவை நிபந்தனைகள் மற்றும் பதவிக்காலம்) சட்டம், 2023 பிரிவு 7(1)-ன் படி, தேர்வுக் குழுவின் தலைவராக இந்தியப் பிரதமர் செயல்படுகிறார்.",
        why_a_en="Correct. Prime Minister is the Chairperson of the Selection Committee.",
        why_a_ta="சரியானது. தேர்வுக் குழுவின் தலைவராக பிரதமர் செயல்படுகிறார்.",
        why_b_en="Incorrect. CJI was included by Supreme Court in Anoop Baranwal (2023) as an interim measure until Parliament enacted law, but Parliament's 2023 Act replaced CJI with a Union Cabinet Minister.",
        why_b_ta="தவறானது. உச்ச நீதிமன்றத்தின் இடைக்கால தீர்ப்பில் CJI இருந்தார், ஆனால் 2023 நாடாளுமன்ற சட்டம் தலைமை நீதிபதிக்குப் பதிலாக மத்திய அமைச்சரை சேர்த்தது.",
        why_c_en="Incorrect. Speaker is not in the Selection Committee.",
        why_c_ta="தவறானது. சபாநாயகர் இக்குழுவில் இல்லை.",
        why_d_en="Incorrect. Union Home Minister is not ex-officio chair.",
        why_d_ta="தவறானது. மத்திய உள்துறை அமைச்சர் தலைவர் அல்ல.",
        tip_en="The 3 members are: (1) Prime Minister (Chair), (2) Leader of Opposition / Largest Opposition Party in Lok Sabha, (3) a Union Cabinet Minister nominated by the PM.",
        tip_ta="3 உறுப்பினர்கள்: (1) பிரதமர் (தலைவர்), (2) எதிர்க்கட்சித் தலைவர் / தனிப்பெரும் எதிர்க்கட்சித் தலைவர், (3) பிரதமரால் நியமிக்கப்படும் ஒரு மத்திய கேபினட் அமைச்சர்.",
        fact_en="A Search Committee headed by the Minister of Law and Justice prepares a panel of 5 persons for the Selection Committee.",
        fact_ta="மத்திய சட்ட அமைச்சர் தலைமையிலான தேடுதல் குழு 5 பேர் கொண்ட பட்டியலை தேர்வுக் குழுவிற்கு பரிந்துரைக்கும்.",
        tags=["ECI Appointment Act 2023", "Selection Committee", "Prime Minister"]
    ))

    # ER_E_048
    qs.append(make_er_q(
        qid="ER_E_048", diff="Easy", qtype="Single-Choice", subtopic="CEC and ECs Appointment Act 2023",
        en_stem="Under the Chief Election Commissioner and other Election Commissioners Act, 2023, who heads the 3-member Search Committee that prepares a panel of candidates?",
        ta_stem="தலைமைத் தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்கள் சட்டம், 2023-ன் கீழ், தகுதியான நபர்களின் பட்டியலைத் தயாரிக்கும் 3 நபர் தேடுதல் குழுவுக்கு (Search Committee) யார் தலைமை தாங்குகிறார்?",
        en_a="Minister of Law and Justice", ta_a="மத்திய சட்டம் மற்றும் நீதித்துறை அமைச்சர்",
        en_b="Cabinet Secretary", ta_b="மத்திய அமைச்சரவைச் செயலாளர் (கேபினட் செயலாளர்)",
        en_c="Home Minister", ta_c="மத்திய உள்துறை அமைச்சர்",
        en_d="Attorney General of India", ta_d="இந்திய தலைமை வழக்கறிஞர் (அட்டர்னி ஜெனரல்)",
        correct_key="A",
        exp_en="Under Section 6 of the 2023 Act, the Search Committee is headed by the Minister of Law and Justice and comprises two other members not below the rank of Secretary to the Government of India.",
        exp_ta="2023 சட்டத்தின் பிரிவு 6-ன் படி, தேடுதல் குழுவிற்கு மத்திய சட்டம் மற்றும் நீதித்துறை அமைச்சர் தலைமை தாங்குவார்; இந்திய அரசின் செயலாளர் அந்தஸ்துக்குக் குறையாத இரண்டு உறுப்பினர்கள் இதில் இடம்பெறுவர்.",
        why_a_en="Correct. Minister of Law and Justice heads the Search Committee.",
        why_a_ta="சரியானது. மத்திய சட்ட அமைச்சர் தேடுதல் குழுவிற்கு தலைமை தாங்குவார்.",
        why_b_en="Incorrect. Cabinet Secretary is not the chair.",
        why_b_ta="தவறானது. கேபினட் செயலாளர் தலைவர் அல்ல.",
        why_c_en="Incorrect. Home Minister is not the chair.",
        why_c_ta="தவறானது. உள்துறை அமைச்சர் தலைவர் அல்ல.",
        why_d_en="Incorrect. Attorney General is not part of this committee.",
        why_d_ta="தவறானது. அட்டர்னி ஜெனரல் இதில் இல்லை.",
        tip_en="Search Committee prepares a panel of 5 persons for consideration by the Selection Committee.",
        tip_ta="தேடுதல் குழு 5 நபர்கள் கொண்ட பட்டியலை தயாரித்து தேர்வுக் குழுவின் பரிசீலனைக்கு அனுப்பும்.",
        fact_en="The Selection Committee may also consider candidates outside the panel prepared by the Search Committee.",
        fact_ta="தேடுதல் குழு பரிந்துரைத்த 5 பேரைத் தவிர வேறு தகுதியான நபர்களையும் தேர்வுக் குழு பரிசீலிக்க அதிகாரம் உண்டு.",
        tags=["Search Committee", "Law Minister", "ECI Appointment Act 2023"]
    ))

    # ER_E_049
    qs.append(make_er_q(
        qid="ER_E_049", diff="Easy", qtype="Single-Choice", subtopic="Simultaneous Elections",
        en_stem="Who served as the Chairman of the High-Level Committee on 'One Nation, One Election' (Simultaneous Elections) that submitted its report in March 2024?",
        ta_stem="2024 மார்ச்சில் அறிக்கை சமர்ப்பித்த 'ஒரே நாடு, ஒரே தேர்தல்' (Simultaneous Elections) குறித்த உயர்நிலைக் குழுவின் தலைவராகப் பணியாற்றியவர் யார்?",
        en_a="Ram Nath Kovind", ta_a="ராம் நாத் கோவிந்த்",
        en_b="Pranab Mukherjee", ta_b="பிரணாப் முகர்ஜி",
        en_c="M. Venkaiah Naidu", ta_c="எம். வெங்கையா நாயுடு",
        en_d="Justice Ranjan Gogoi", ta_d="நீதிபதி ரஞ்சன் கோகோய்",
        correct_key="A",
        exp_en="Former President of India Ram Nath Kovind headed the 8-member High-Level Committee (HLC) on Simultaneous Elections constituted by the Central Government in September 2023, which submitted its report to President Droupadi Murmu on 14 March 2024.",
        exp_ta="முன்னாள் இந்திய குடியரசுத் தலைவர் ராம் நாத் கோவிந்த் தலைமையில் 2023 செப்டம்பரில் அமைக்கப்பட்ட 8 உறுப்பினர்கள் கொண்ட உயர்நிலைக் குழு, 2024 மார்ச் 14 அன்று குடியரசுத் தலைவர் திரௌபதி முர்முவிடம் தனது விரிவான அறிக்கையை சமர்ப்பித்தது.",
        why_a_en="Correct. Ram Nath Kovind chaired the committee on simultaneous elections.",
        why_a_ta="சரியானது. ராம் நாத் கோவிந்த் இக்குழுவின் தலைவராகப் பணியாற்றினார்.",
        why_b_en="Incorrect. Former President Pranab Mukherjee passed away in 2020.",
        why_b_ta="தவறானது. பிரணாப் முகர்ஜி 2020-ல் மறைந்தார்.",
        why_c_en="Incorrect. Former VP Venkaiah Naidu was not the chair.",
        why_c_ta="தவறானது. வெங்கையா நாயுடு தலைவர் அல்ல.",
        why_d_en="Incorrect. Former CJI Ranjan Gogoi was not the chair.",
        why_d_ta="தவறானது. ரஞ்சன் கோகோய் தலைவர் அல்ல.",
        tip_en="The Kovind Committee recommended a two-step approach: simultaneous elections to Lok Sabha and State Assemblies first, followed by Municipalities and Panchayats within 100 days.",
        tip_ta="கோவிந்த் குழு இரு-படி அணுகுமுறையை பரிந்துரைத்தது: முதலில் மக்களவை மற்றும் சட்டமன்றங்களுக்கு ஒரே நேரத்தில் தேர்தல்; அடுத்த 100 நாட்களுக்குள் உள்ளாட்சித் தேர்தல்கள்.",
        fact_en="It recommended introducing Article 82A to empower the President to bring simultaneous elections into force.",
        fact_ta="குடியரசுத் தலைவர் ஒரே தேர்தல் முறையை நடைமுறைப்படுத்த சரத்து 82A-ஐ இணைக்க பரிந்துரைத்தது.",
        tags=["Kovind Committee", "Simultaneous Elections", "ONOE 2024"]
    ))

    # ER_E_050
    qs.append(make_er_q(
        qid="ER_E_050", diff="Easy", qtype="Single-Choice", subtopic="Universal Adult Franchise",
        en_stem="Which Article of the Constitution of India provides that elections to the House of the People (Lok Sabha) and the Legislative Assembly of every State shall be on the basis of adult suffrage?",
        ta_stem="மக்களவை மற்றும் ஒவ்வொரு மாநிலத்தின் சட்டப் பேரவைக்கான தேர்தல்கள் வயதுவந்தோர் வாக்குரிமையின் அடிப்படையில் நடத்தப்பட வேண்டும் என்று கூறும் இந்திய அரசியலமைப்புச் சரத்து எது?",
        en_a="Article 326", ta_a="சரத்து 326",
        en_b="Article 324", ta_b="சரத்து 324",
        en_c="Article 325", ta_c="சரத்து 325",
        en_d="Article 327", ta_d="சரத்து 327",
        correct_key="A",
        exp_en="Article 326 of the Constitution provides that elections to the Lok Sabha and State Legislative Assemblies shall be on the basis of adult suffrage, entitling every citizen not less than 18 years of age (originally 21) who is not disqualified to vote.",
        exp_ta="இந்திய அரசியலமைப்பின் சரத்து 326, மக்களவை மற்றும் மாநில சட்டமன்றங்களுக்கான தேர்தல்கள் வயதுவந்தோர் வாக்குரிமையின் அடிப்படையில் நடத்தப்பட வேண்டும் என்றும், 18 வயது நிரம்பிய தகுதியான ஒவ்வொரு குடிமகனுக்கும் வாக்களிக்கும் உரிமை உண்டு என்றும் கூறுகிறது.",
        why_a_en="Correct. Article 326 guarantees universal adult suffrage.",
        why_a_ta="சரியானது. சரத்து 326 வயதுவந்தோர் வாக்குரிமைக்கு உத்தரவாதம் அளிக்கிறது.",
        why_b_en="Incorrect. Article 324 deals with superintendence, direction, and control of elections by ECI.",
        why_b_ta="தவறானது. சரத்து 324 தேர்தல் ஆணையத்தின் அதிகாரங்களைக் கையாள்கிறது.",
        why_c_en="Incorrect. Article 325 bars discrimination in electoral rolls on grounds of religion, race, caste, or sex.",
        why_c_ta="தவறானது. சரத்து 325 வாக்காளர் பட்டியலில் மதம், இனம், ஜாதி, பாலின பாகுபாட்டைத் தடை செய்கிறது.",
        why_d_en="Incorrect. Article 327 empowers Parliament to make laws regarding elections.",
        why_d_ta="தவறானது. சரத்து 327 நாடாளுமன்றத்தின் தேர்தல் சட்டமியற்றும் அதிகாரம் பற்றியது.",
        tip_en="Article 326 is the bedrock of democratic franchise in India; amended by the 61st Amendment in 1988.",
        tip_ta="சரத்து 326 இந்திய ஜனநாயகத்தின் வாக்குரிமைக்கான அடித்தளமாகும்; 1988-ல் 61-வது திருத்தத்தால் திருத்தப்பட்டது.",
        fact_en="India adopted Universal Adult Suffrage directly with the commencement of the Constitution on 26 January 1950, without any property or educational qualifications.",
        fact_ta="1950 ஜனவரி 26 அன்று அரசியலமைப்பு நடைமுறைக்கு வந்தபோதே எவ்வித சொத்து அல்லது கல்வித்தகுதி நிபந்தனைகளும் இன்றி வயதுவந்தோர் வாக்குரிமை வழங்கப்பட்டது.",
        tags=["Article 326", "Adult Suffrage", "Constitutional Basis"]
    ))

    return qs

def main():
    raw_qs = get_easy_questions()
    print(f"Total raw questions: {len(raw_qs)}")
    assert len(raw_qs) == 50, f"Expected 50, got {len(raw_qs)}"
    
    # Check ID sequence
    for idx, q in enumerate(raw_qs, 1):
        expected_id = f"ER_E_{idx:03d}"
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
    report = validator.validate_file(OUTPUT_PATH, expected_count=50, expected_prefix="ER_E_")
    print(report.summary())
    assert report.is_valid, "Validation failed!"

if __name__ == "__main__":
    main()
