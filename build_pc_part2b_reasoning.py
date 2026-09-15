# -*- coding: utf-8 -*-
"""
Build 25 Reasoning (Assertion-Reason) MCQs for Parliamentary Committees (PC_R_001 to PC_R_025)
TNPSC Nova AI Content Engine
"""
import json
from collections import Counter
from parliamentary_committees_mcq_helper import make_pc_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_reasoning_questions():
    questions = []

    reasoning_specs = [
        ("001", "Financial Committees", "Medium",
         "Assertion (A): The Chairman of the Public Accounts Committee is by convention chosen from the Opposition parties in Lok Sabha.\nReason (R): This convention ensures unbiased and rigorous financial scrutiny of the government's expenditures free from ruling party bias.",
         "கூற்று (A): பொதுக் கணக்குக் குழுவின் (PAC) தலைவர் மரபின்படி மக்களவை எதிர்க்கட்சிகளிலிருந்தே தேர்ந்தெடுக்கப்படுகிறார்.\nகாரணம் (R): இந்த மரபு ஆளும் கட்சியின் சார்பின்றி அரசின் செலவினங்களை நடுநிலையாகவும் தீவிரமாகவும் ஆய்வு செய்வதை உறுதி செய்கிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Since 1967, an opposition member is appointed Chairman of PAC to ensure independent, objective scrutiny of executive spending without partisan shielding.",
         "1967 முதல் ஆளும் கட்சி சார்பின்றி அரசின் செலவுகளை நடுநிலையாக ஆய்வு செய்யவே எதிர்க்கட்சி எம்பி தலைவராக நியமிக்கப்படுகிறார்; எனவே (R) என்பது (A)-வின் சரியான விளக்கமாகும்."),

        ("002", "Financial Committees", "Medium",
         "Assertion (A): The Estimates Committee consists exclusively of 30 members elected from the Lok Sabha alone.\nReason (R): The Rajya Sabha has no constitutional power to vote on the Demands for Grants in the annual budget under Article 113(2).",
         "கூற்று (A): மதிப்பீட்டுக் குழு மக்களவையிலிருந்து மட்டுமே தேர்ந்தெடுக்கப்பட்ட 30 உறுப்பினர்களைக் கொண்டுள்ளது.\nகாரணம் (R): சரத்து 113(2)-ன் கீழ் வருடாந்திர பட்ஜெட்டின் மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் அரசியலமைப்பு அதிகாரம் மாநிலங்களவைக்கு இல்லை.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Voting of demands is the exclusive prerogative of the directly elected Lok Sabha (Art. 113(2)), so the Estimates Committee examining these budget estimates comprises Lok Sabha members only.",
         "மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் அதிகாரம் மக்களவைக்கே உள்ளதால், பட்ஜெட் மதிப்பீடுகளை ஆய்வு செய்யும் மதிப்பீட்டுக் குழுவிலும் மக்களவை உறுப்பினர்கள் மட்டுமே இடம்பெறுகின்றனர்; (R) சரியான விளக்கம்."),

        ("003", "Financial Committees", "Hard",
         "Assertion (A): The Committee on Public Undertakings (COPU) is strictly barred from examining matters of day-to-day administration of government corporations.\nReason (R): Parliamentary oversight should not erode the commercial autonomy and operational flexibility essential for running business enterprises.",
         "கூற்று (A): பொதுத்துறை நிறுவனங்களின் அன்றாட நிர்வாக விவகாரங்களை ஆய்வு செய்ய பொதுத்துறை நிறுவனங்களுக்கான குழுவிற்கு (COPU) கடுமையான தடை விதிக்கப்பட்டுள்ளது.\nகாரணம் (R): வணிக நிறுவனங்களை நடத்துவதற்கு அவசியமான தன்னாட்சி மற்றும் செயல்பாட்டு நெகிழ்வுத்தன்மையை நாடாளுமன்றக் கண்காணிப்பு சீர்குலைக்கக் கூடாது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Under Rule 312A, COPU cannot examine day-to-day administration to preserve managerial initiative and commercial autonomy of PSUs while ensuring overall public accountability.",
         "பொதுத்துறை நிறுவனங்களின் வணிக தன்னாட்சி மற்றும் நிர்வாக முடிவெடுக்கும் திறனைப் பாதுகாக்கவே அன்றாட நிர்வாகத்தில் COPU தலையிடுவதில்லை (விதி 312A)."),

        ("004", "Parliamentary Committee Rules", "Medium",
         "Assertion (A): A Union Minister cannot be elected as a member of the Public Accounts Committee, Estimates Committee, or COPU.\nReason (R): Ministers belong to the Executive, and allowing them on scrutiny committees would create a direct conflict of interest between the overseer and the overseen.",
         "கூற்று (A): மத்திய அமைச்சர் ஒருவர் PAC, மதிப்பீட்டுக் குழு அல்லது COPU ஆகியவற்றில் உறுப்பினராகத் தேர்ந்தெடுக்கப்பட முடியாது.\nகாரணம் (R): அமைச்சர்கள் நிர்வாகத்துறையைச் சேர்ந்தவர்கள்; அவர்களைக் கண்காணிப்புக் குழுக்களில் அனுமதிப்பது கண்காணிப்பவருக்கும் கண்காணிக்கப்படுபவருக்கும் இடையே நேரடி நலன் முரண்பாட்டை உருவாக்கும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Ministers represent the executive accountable to Parliament; having them sit on committees that audit executive conduct violates the principle of separation and creates conflicts of interest.",
         "நிர்வாகம் நாடாளுமன்றத்திற்குக் கட்டுப்பட்டது; நிர்வாகத்தின் செயல்களை ஆய்வு செய்யும் குழுக்களில் அமைச்சர்களே அமர்வது நலன் முரண்பாட்டை ஏற்படுத்தும் என்பதால் தடை செய்யப்பட்டுள்ளது."),

        ("005", "Departmentally Related Standing Committees", "Medium",
         "Assertion (A): The creation of 24 Departmentally Related Standing Committees in 1993 helped mitigate the democratic deficit of the budgetary Guillotine.\nReason (R): During the 3-4 week parliamentary recess, DRSCs examine the Demands for Grants of all ministries, ensuring that even guillotined demands undergo detailed committee scrutiny.",
         "கூற்று (A): 1993-ல் 24 துறை சார்ந்த நிலைக்குழுக்கள் உருவாக்கப்பட்டமை பட்ஜெட் கில்லட்டின் முறையால் ஏற்படும் ஜனநாயகக் குறைபாட்டைத் தணிக்க உதவியது.\nகாரணம் (R): 3-4 வார நாடாளுமன்ற இடைவேளையின் போது DRSCs அனைத்து அமைச்சகங்களின் மானியக் கோரிக்கைகளையும் ஆய்வு செய்வதால், விவாதமின்றி நிறைவேற்றப்படும் கோரிக்கைகளும் குழு ஆய்வுக்கு உட்படுகின்றன.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The Guillotine passes remaining demands without floor debate due to time limits; DRSCs cure this deficit by subjecting all ministerial demands to committee scrutiny during recess.",
         "நேரமின்மையால் அவையில் விவாதிக்கப்படாமல் நிறைவேற்றப்படும் கோரிக்கைகளையும் இடைவேளையில் DRSCs முழுமையாக ஆய்வு செய்வதால் ஜனநாயகக் குறைபாடு தீர்க்கப்படுகிறது."),

        ("006", "Committees to Scrutinize and Control", "Medium",
         "Assertion (A): The Committee on Subordinate Legislation ensures that executive rule-making stays strictly within the boundaries delegated by the Parent Act.\nReason (R): Under the doctrine of separation of powers, the essential legislative function cannot be completely abdicated or exceeded by the administrative executive.",
         "கூற்று (A): நிர்வாகத்தின் விதி உருவாக்கம் முதன்மைச் சட்டத்தின் வரம்புகளுக்குள் செயல்படுவதை துணைச் சட்டங்களுக்கான குழு உறுதி செய்கிறது.\nகாரணம் (R): அதிகாரப் பகிர்வுக் கோட்பாட்டின் கீழ், நாடாளுமன்றத்தின் அடிப்படை சட்டமியற்றும் அதிகாரத்தை நிர்வாகத்துறைக்கு தாரைவார்த்துக் கொடுக்கவோ அல்லது வரம்பு மீறவோ முடியாது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The committee polices delegated legislation to ensure that executive regulations do not usurp essential legislative functions or violate ultra vires limits.",
         "அரசு இயற்றும் துணை விதிகள் முதன்மைச் சட்டத்தின் எல்லைகளை மீறாமல் இருப்பதை உறுதி செய்ய இக்குழு செயல்படுகிறது."),

        ("007", "Committees to Scrutinize and Control", "Medium",
         "Assertion (A): The Committee on Government Assurances was praised as a unique institutional contribution of the Indian Parliament.\nReason (R): The British House of Commons had no specialized standing committee to monitor ministerial assurances given on the floor of the House.",
         "கூற்று (A): அரசு உறுதிமொழிகளுக்கான குழு இந்திய நாடாளுமன்றத்தின் தனித்துவமான நிறுவனப் பங்களிப்பாகப் பாராட்டப்பட்டது.\nகாரணம் (R): அவையில் அமைச்சர்கள் அளித்த உறுதிமொழிகளைக் கண்காணிக்க பிரிட்டிஷ் பொது அவையில் இத்தகைய பிரத்யேக நிலைக்குழு எதுவும் இருக்கவில்லை.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "First created in 1953 in India, this committee institutionalized accountability for verbal promises made during debates, which did not exist in Westminster.",
         "1953-ல் இந்தியாவில் முதன்முதலில் உருவாக்கப்பட்ட இக்குழு, அவையில் அமைச்சர்கள் கூறிய வாய்மொழி வாக்குறுதிகளை நிறைவேற்றுவதைக் கட்டாயமாக்கியது; பிரிட்டிஷ் அவையில் இக்குழு இல்லை."),

        ("008", "Committees to Inquire", "Medium",
         "Assertion (A): The Committee of Privileges possesses a quasi-judicial character.\nReason (R): It investigates charges of breach of parliamentary privileges, examines witnesses on oath, and recommends punitive actions to the House.",
         "கூற்று (A): உரிமைகள் குழு ஒரு பாதி-நீதித்துறை (quasi-judicial) தன்மையைக் கொண்டுள்ளது.\nகாரணம் (R): இது நாடாளுமன்ற உரிமை மீறல் குற்றங்களை விசாரித்து, சாட்சிகளிடம் சத்தியப் பிரமாணம் பெற்று விசாரித்து, அவைக்குத் தண்டனைகளைப் பரிந்துரைக்கிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Exercising powers of summoning, examining evidence under oath, and recommending penal consequences gives the Privileges Committee its quasi-judicial character.",
         "சாட்சிகளை வரவழைத்து ஆவணங்களை ஆய்வு செய்து குற்றத்தை உறுதிப்படுத்தி தண்டனையைப் பரிந்துரைப்பதால் இது பாதி-நீதித்துறை தன்மையைப் பெறுகிறது."),

        ("009", "Committees on Day-to-Day Business", "Medium",
         "Assertion (A): The Speaker of the Lok Sabha serves as the ex-officio Chairman of the Business Advisory Committee.\nReason (R): The allocation of time for parliamentary business is intimately tied to the Speaker's duty to maintain order and conduct the proceedings of the House.",
         "கூற்று (A): மக்களவை சபாநாயகர் அலுவல் ஆலோசனைக் குழுவின் (BAC) அலுவல் வழித் தலைவராக செயல்படுகிறார்.\nகாரணம் (R): அவையின் நடவடிக்கைகளை ஒழுங்குபடுத்துவது மற்றும் அமைதியைப் பேணுவது சபாநாயகரின் கடமையுடன் நேரடியாகத் தொடர்புடையதாகும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The Speaker chairs BAC because regulating the legislative timetable is central to managing floor business and order.",
         "அவை நேரத்தை திட்டமிடுவதும் ஒழுங்குபடுத்துவதும் சபாநாயகரின் முதன்மைக் கடமையுடன் இணைந்திருப்பதால் அவரே BAC-க்கு தலைமை தாங்குகிறார்."),

        ("010", "Parliamentary Committee Rules", "Medium",
         "Assertion (A): Sittings of Parliamentary Committees are held in camera (in private).\nReason (R): Confidentiality allows members from different political parties to engage in candid, constructive dialogue and reach non-partisan consensus without media grandstanding.",
         "கூற்று (A): நாடாளுமன்றக் குழுக் கூட்டங்கள் ரகசியமாக (in camera) நடத்தப்படுகின்றன.\nகாரணம் (R): ரகசியத்தன்மை பல்வேறு கட்சிகளைச் சேர்ந்த உறுப்பினர்கள் ஊடக விளம்பரங்களின்றி வெளிப்படையாகவும் ஆக்கப்பூர்வமாகவும் விவாதித்து ஒருமித்த கருத்தை எட்ட உதவுகிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Closed-door proceedings remove partisan posturing, enabling objective fact-finding and consensual policy recommendations.",
         "ரகசிய கூட்டங்களே கட்சி வேறுபாடுகளைக் கடந்து நடுநிலையான உண்மைகளைக் கண்டறியவும் ஒருமித்த முடிவுகளை எடுக்கவும் உதவுகின்றன."),

        ("011", "Financial Committees", "Medium",
         "Assertion (A): The Public Accounts Committee's financial scrutiny is often characterized as 'post-mortem' in nature.\nReason (R): PAC examines public expenditures only after the money has already been spent and audited by the Comptroller and Auditor General.",
         "கூற்று (A): பொதுக் கணக்குக் குழுவின் (PAC) நிதி ஆய்வு பெரும்பாலும் 'பிரேதப் பரிசோதனை' போன்றது என்று விவரிக்கப்படுகிறது.\nகாரணம் (R): பணம் ஏற்கனவே செலவிடப்பட்டு CAG-ஆல் தணிக்கை செய்யப்பட்ட பின்னரே PAC அதை ஆய்வு செய்கிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Since PAC examines past audit reports, it cannot prevent wasteful spending as it happens; it can only conduct ex-post examination and suggest future safeguards.",
         "செலவுகள் நடந்து முடிந்த பின்பே CAG அறிக்கையை PAC ஆய்வு செய்வதால், விரயத்தை முன்கூட்டியே தடுக்க முடியாது; பிந்தைய ஆய்வாகவே அமைகிறது."),

        ("012", "Consultative Committees", "Medium",
         "Assertion (A): Consultative Committees attached to Union Ministries are technically not Parliamentary Committees.\nReason (R): They are not appointed by the Speaker/Chairman, do not work under their direction, and are serviced by the Ministry of Parliamentary Affairs rather than the Parliament Secretariat.",
         "கூற்று (A): மத்திய அமைச்சகங்களுடன் இணைக்கப்பட்டுள்ள ஆலோசனைக் குழுக்கள் முறைப்படி நாடாளுமன்றக் குழுக்கள் அல்ல.\nகாரணம் (R): அவை சபாநாயகர்/தலைவரால் நியமிக்கப்படுவதில்லை, அவர்களின் வழிகாட்டுதலில் இயங்குவதில்லை மற்றும் நாடாளுமன்ற செயலகத்திற்குப் பதிலாக நாடாளுமன்ற விவகார அமைச்சகத்தால் நிர்வகிக்கப்படுகின்றன.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "To be a Parliamentary Committee, four specific criteria under House rules must be satisfied; Consultative Committees fulfill none of them and are informal ministerial forums.",
         "நாடாளுமன்றக் குழுவிற்கான 4 முக்கிய விதிமுறைகளை ஆலோசனைக் குழுக்கள் கொண்டிருக்கவில்லை; அவை அமைச்சகங்களின் முறைசாரா மன்றங்கள் மட்டுமே."),

        ("013", "Parliamentary Committee Rules", "Medium",
         "Assertion (A): If the Deputy Speaker of the Lok Sabha is appointed a member of any parliamentary committee, he is automatically appointed its Chairman.\nReason (R): Under Rule 258 of the Lok Sabha, the constitutional stature of the Deputy Speaker requires that he cannot serve as a subordinate member under another MP.",
         "கூற்று (A): மக்களவைத் துணை சபாநாயகர் ஏதேனும் ஒரு நாடாளுமன்றக் குழுவில் உறுப்பினராக நியமிக்கப்பட்டால், அவர் தானாகவே அதன் தலைவராக நியமிக்கப்படுகிறார்.\nகாரணம் (R): மக்களவை விதி 258-ன் படி, துணை சபாநாயகரின் அரசியலமைப்பு மாண்பு மற்றொரு எம்பியின் கீழ் அவர் சாதாரண உறுப்பினராகப் பணியாற்றுவதை அனுமதிக்காது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Rule 258 proviso explicitly mandates that Deputy Speaker, if a member, must chair the committee to respect constitutional protocol.",
         "அரசியலமைப்பு மரபைப் பேண துணை சபாநாயகர் குழுவில் இருந்தால் அவரே தலைவராக நியமிக்கப்பட வேண்டும் என்று விதி 258 கூறுகிறது."),

        ("014", "Financial Committees", "Medium",
         "Assertion (A): The Estimates Committee is described as the largest committee of the Indian Parliament.\nReason (R): It has 30 members, whereas PAC and COPU have only 22 members each.",
         "கூற்று (A): மதிப்பீட்டுக் குழு இந்திய நாடாளுமன்றத்தின் மிகப்பெரிய குழு என்று விவரிக்கப்படுகிறது.\nகாரணம் (R): இதில் 30 உறுப்பினர்கள் உள்ளனர், ஆனால் PAC மற்றும் COPU ஆகியவற்றில் தலா 22 உறுப்பினர்கள் மட்டுமே உள்ளனர்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "With 30 MPs (all from Lok Sabha), the Estimates Committee has the single largest membership among all standing committees of Parliament.",
         "30 உறுப்பினர்களைக் கொண்டுள்ளதால் மதிப்பீட்டுக் குழுவே நாடாளுமன்றத்தின் மிகப்பெரிய நிலைக்குழுவாகும்."),

        ("015", "Parliamentary Committee Reports", "Medium",
         "Assertion (A): Parliamentary Committee recommendations are advisory and legally non-binding on the Executive.\nReason (R): Under the Constitution, the Council of Ministers is collectively responsible to the elected Lok Sabha as a whole, not to individual committees.",
         "கூற்று (A): நாடாளுமன்றக் குழுக்களின் பரிந்துரைகள் ஆலோசனைக் கூறுகளைக் கொண்டவை மற்றும் நிர்வாகத்தைக் கட்டுப்படுத்தாதவை.\nகாரணம் (R): அரசியலமைப்பின் கீழ், அமைச்சரவை ஒட்டுமொத்த மக்களவைக்கே கூட்டுப் பொறுப்பானது, தனித்தனி குழுக்களுக்கு அல்ல.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Collective ministerial responsibility under Article 75(3) lies to the full Lok Sabha, preserving sovereign cabinet decision-making subject to floor accountability.",
         "சரத்து 75(3)-ன் கீழ் அமைச்சரவை முழு மக்களவைக்கே பொறுப்பானது என்பதால் குழுக்களின் பரிந்துரைகள் ஆலோசனையாகவே உள்ளன."),

        ("016", "Constitutional Framework", "Hard",
         "Assertion (A): In *Kalpana Mehta v. Union of India* (2018), the Supreme Court ruled that parliamentary committee reports can be used as factual evidence in court.\nReason (R): Parliamentary reports are public documents under Section 74 of the Indian Evidence Act, though courts cannot question the correctness of their findings.",
         "கூற்று (A): *கல்பனா மேத்தா* (2018) வழக்கில் நாடாளுமன்றக் குழு அறிக்கைகளை நீதிமன்றத்தில் ஆதாரமாகப் பயன்படுத்தலாம் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): குழு அறிக்கைகள் சாட்சியச் சட்டத்தின் கீழ் பொது ஆவணங்கள் ஆகும்; ஆனால் அவற்றின் சரியை நீதிமன்றங்கள் கேள்வி கேட்க முடியாது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The Constitution Bench held that reports are admissible for factual context without breaching Article 105 parliamentary privilege.",
         "அறிக்கைகளை வரலாற்று ஆதாரமாக நீதிமன்றம் ஏற்கலாம் ஆனால் நாடாளுமன்ற சலுகைகளில் தலையிட முடியாது என தீர்ப்பளிக்கப்பட்டது."),

        ("017", "Committees to Scrutinize and Control", "Medium",
         "Assertion (A): The Joint Committee on Offices of Profit plays a vital role in protecting parliamentary independence.\nReason (R): It prevents the Executive from co-opting MPs into lucrative government offices and undermining their legislative objectivity.",
         "கூற்று (A): ஆதாயம் தரும் பதவிகளுக்கான கூட்டுக் குழு நாடாளுமன்றத்தின் சுதந்திரத்தைப் பாதுகாப்பதில் முக்கியப் பங்கு வகிக்கிறது.\nகாரணம் (R): நிர்வாகத்துறை எம்பிக்களுக்கு ஆதாயம் தரும் அரசுப் பதவிகளை வழங்கி அவர்களது நடுநிலையை சீர்குலைப்பதைத் தடுக்கிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The doctrine of office of profit prevents the executive from buying parliamentary support through state appointments and patronage.",
         "அரசுப் பதவிகள் மற்றும் சலுகைகள் மூலம் எம்பிக்களின் சுதந்திரத்தை அரசு விலைக்கு வாங்குவதைத் தடுக்க ஆதாயப் பதவி தகுதிநீக்கம் உதவுகிறது."),

        ("018", "Ad Hoc Committees", "Medium",
         "Assertion (A): A Joint Parliamentary Committee (JPC) has the authority to summon private individuals and corporate heads for questioning.\nReason (R): Parliamentary committees are vested with powers akin to a civil court under the Code of Civil Procedure regarding enforcing attendance of witnesses and production of documents.",
         "கூற்று (A): தனியார் நபர்கள் மற்றும் பெருநிறுவனத் தலைவர்களை விசாரணைக்கு வரவழைக்கும் அதிகாரம் JPC-க்கு உண்டு.\nகாரணம் (R): சாட்சிகளை வரவழைப்பது மற்றும் ஆவணங்களைப் பெறுவதில் சிவில் நடைமுறைச் சட்டத்தின் கீழ் சிவில் நீதிமன்றத்திற்கு இணையான அதிகாரங்கள் குழுக்களுக்கு வழங்கப்பட்டுள்ளன.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Under Rule 270 and parliamentary privilege powers, JPCs can compel witness attendance and document production under penalty of contempt.",
         "விதி 270-ன் கீழ் சாட்சிகளை வரவழைக்கவும் ஆவணங்களை ஆய்வு செய்யவும் சிவில் நீதிமன்ற அதிகாரங்கள் குழுக்களுக்கு உள்ளன."),

        ("019", "Committees on Day-to-Day Business", "Medium",
         "Assertion (A): The Committee on Private Members' Bills and Resolutions is special to the Lok Sabha.\nReason (R): In the Rajya Sabha, private members' business is regulated directly by its Business Advisory Committee.",
         "கூற்று (A): தனிநபர் மசோதாக்கள் மற்றும் தீர்மானங்களுக்கான குழு மக்களவைக்கு மட்டுமே உரியது.\nகாரணம் (R): மாநிலங்களவையில் தனிநபர் விவகாரங்கள் அதன் அலுவல் ஆலோசனைக் குழுவால் (BAC) நேரடியாக ஒழுங்குபடுத்தப்படுகின்றன.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Rajya Sabha does not have a separate private members' committee; its BAC allocates time for Friday afternoon private members' business.",
         "மாநிலங்களவையில் தனிக்குழு இல்லை; அதன் BAC-யே தனிநபர் விவாதங்களுக்கு நேரம் ஒதுக்குகிறது."),

        ("020", "Financial Committees", "Medium",
         "Assertion (A): The Comptroller and Auditor General (CAG) attends the meetings of the Public Accounts Committee.\nReason (R): The technical complexity of accounting and auditing records requires the CAG to assist members in understanding irregularities.",
         "கூற்று (A): பொதுக் கணக்குக் குழுவின் (PAC) கூட்டங்களில் இந்தியக் கணக்குத் தணிக்கைத் தலைவர் (CAG) கலந்துகொள்கிறார்.\nகாரணம் (R): கணக்கு பதிவேடுகளின் தொழில்நுட்ப சிக்கல்களைப் புரிந்துகொள்ள எம்பிக்களுக்கு உதவ CAG அக்கூட்டங்களில் பங்கேற்கிறார்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "CAG acts as technical guide to PAC members during oral examination of departmental secretaries on audit paragraphs.",
         "தணிக்கைப் பத்திகளை ஆய்வு செய்யும் போது துறைச் செயலாளர்களை விசாரிக்க CAG குழு உறுப்பினர்களுக்கு தொழில்நுட்ப வழிகாட்டுதல் வழங்குகிறார்."),

        ("021", "Financial Committees", "Medium",
         "Assertion (A): The Estimates Committee cannot examine the estimates of all Union ministries in a single year.\nReason (R): The vast scale of central government expenditure requires the committee to select only a few ministries each year on a rotational basis.",
         "கூற்று (A): மதிப்பீட்டுக் குழு ஒரே ஆண்டில் அனைத்து மத்திய அமைச்சகங்களின் மதிப்பீடுகளையும் ஆய்வு செய்ய முடியாது.\nகாரணம் (R): மத்திய அரசின் செலவினங்கள் மிகப்பெரியவை என்பதால் ஆண்டுதோறும் சில குறிப்பிட்ட அமைச்சகங்களை மட்டுமே சுழற்சி முறையில் தேர்ந்தெடுக்க முடிகிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Due to massive governmental operations, the Estimates Committee examines selected departments each year, completing the cycle over multiple years.",
         "அமைச்சகங்களின் எண்ணிக்கை அதிகமாக இருப்பதால் ஆண்டுதோறும் சிலவற்றை மட்டுமே மதிப்பீட்டுக் குழு ஆய்வு செய்ய முடிகிறது."),

        ("022", "Departmentally Related Standing Committees", "Medium",
         "Assertion (A): Reports of Departmentally Related Standing Committees are presented simultaneously to both Houses of Parliament.\nReason (R): Each DRSC has members from both the Lok Sabha and the Rajya Sabha (21 LS + 10 RS).",
         "கூற்று (A): DRSC குழுக்களின் அறிக்கைகள் நாடாளுமன்றத்தின் இரு அவைகளிலும் ஒரே நேரத்தில் சமர்ப்பிக்கப்படுகின்றன.\nகாரணம் (R): ஒவ்வொரு DRSC குழுவிலும் இரு அவைகளின் உறுப்பினர்களும் (21 LS + 10 RS) இடம்பெற்றுள்ளனர்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Since DRSCs are joint bicameral bodies, their reports belong to both Houses and are tabled simultaneously in both chambers.",
         "இரு அவைகளின் கூட்டு அமைப்பாக DRSCs செயல்படுவதால், அவற்றின் அறிக்கைகள் இரு அவைகளிலும் ஒரே நேரத்தில் வைக்கப்படுகின்றன."),

        ("023", "Committees to Scrutinize and Control", "Medium",
         "Assertion (A): The Committee on Papers Laid on the Table checks delays in placing statutory annual reports.\nReason (R): If reports are delayed beyond nine months from the close of the financial year, the concerned ministry must explain the reasons for delay.",
         "கூற்று (A): அவை மேசையில் வைக்கப்படும் ஆவணங்களுக்கான குழு சட்டப்பூர்வ ஆண்டறிக்கைகளை வைப்பதில் ஏற்படும் தாமதங்களைச் சரிபார்க்கிறது.\nகாரணம் (R): நிதியாண்டு முடிந்து 9 மாதங்களுக்கு மேல் தாமதமானால் அமைச்சகம் அதற்கான காரணங்களை விளக்க வேண்டும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The committee enforces the 9-month norm to ensure Parliament receives timely financial accounting from executive departments.",
         "நிர்வாகத் துறைகள் குறித்த நேரத்தில் கணக்குகளை சமர்ப்பிக்க 9 மாத கால வரம்பை இக்குழு தீவிரமாக அமல்படுத்துகிறது."),

        ("024", "Parliamentary Committee Rules", "Medium",
         "Assertion (A): A member of a parliamentary committee who disagrees with the majority view has the right to attach a Minute of Dissent.\nReason (R): Democratic deliberative bodies must record and respect minority viewpoints to present a balanced perspective to the sovereign House.",
         "கூற்று (A): பெரும்பான்மை கருத்தை ஏற்காத ஒரு குழு உறுப்பினர் மாறுபட்ட கருத்து அறிக்கையை (Minute of Dissent) இணைக்கும் உரிமையைக் கொண்டுள்ளார்.\nகாரணம் (R): ஜனநாயக அமைப்புகள் சிறுபான்மை பார்வைகளை மதித்து அவைக்கு சமநிலையான பார்வையை வழங்க வேண்டும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Minutes of Dissent preserve democratic debate and alert the House to contentious clauses and counter-proposals.",
         "மாறுபட்ட கருத்து அறிக்கை ஜனநாயக விவாதங்களைப் பாதுகாத்து மாற்றுப் பார்வைகளை அவைக்குத் தெரியப்படுத்துகிறது."),

        ("025", "Parliamentary Committees Overview", "Medium",
         "Assertion (A): Parliamentary standing committees are often described as 'mini-parliaments' working away from the limelight.\nReason (R): They replicate the party composition of the House in miniature, conducting rigorous clause-by-clause legislative and financial examination in closed committee rooms.",
         "கூற்று (A): நாடாளுமன்ற நிலைக்குழுக்கள் வெளிச்சத்திற்கு அப்பால் பணியாற்றும் 'குட்டி நாடாளுமன்றங்கள்' (mini-parliaments) என்று அழைக்கப்படுகின்றன.\nகாரணம் (R): அவை அவையின் கட்சி அமைப்பை சிறிய அளவில் பிரதிபலித்து, குழு அறைகளில் ஒவ்வொரு பிரிவாக விரிவான சட்ட மற்றும் நிதி ஆய்வை மேற்கொள்கின்றன.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Proportional party representation and detailed behind-the-scenes legislative and oversight work make committees true mini-parliaments.",
         "கட்சி விகிதாசார கட்டமைப்பு மற்றும் தீவிர விவாதங்கள் நாடாளுமன்றக் குழுக்களை 'குட்டி நாடாளுமன்றங்களாக' ஆக்குகின்றன.")
    ]

    for qid, sub, diff, en_s, ta_s, en_a, en_b, en_c, en_d, corr, exp_e, exp_t in reasoning_specs:
        full_qid = f"PC_R_{qid}"
        ta_a = "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்"
        ta_b = "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"
        ta_c = "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு"
        ta_d = "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி"

        questions.append(make_pc_q(
            qid=full_qid,
            diff=diff,
            qtype="assertion_reason",
            subtopic=sub,
            en_stem=en_s,
            ta_stem=ta_s,
            en_a=en_a,
            ta_a=ta_a,
            en_b=en_b,
            ta_b=ta_b,
            en_c=en_c,
            ta_c=ta_c,
            en_d=en_d,
            ta_d=ta_d,
            correct_key=corr,
            exp_en=exp_e,
            exp_ta=exp_t,
            why_a_en="Correct. Assertion and Reason are both true, and the Reason correctly explains the Assertion.",
            why_a_ta="சரி. கூற்று மற்றும் காரணம் இரண்டும் உண்மை, மேலும் காரணம் கூற்றை சரியாக விளக்குகிறது.",
            why_b_en="Incorrect. The Reason is directly causal to the Assertion.",
            why_b_ta="தவறு. காரணம் கூற்றுடன் நேரடி காரண-காரியத் தொடர்பு கொண்டது.",
            why_c_en="Incorrect. Reason is factually correct.",
            why_c_ta="தவறு. காரணம் உண்மையானது.",
            why_d_en="Incorrect. Assertion is factually correct.",
            why_d_ta="தவறு. கூற்று உண்மையானது.",
            tip_en="In Assertion-Reason questions, connect the Assertion and Reason with 'BECAUSE' to test causality.",
            tip_ta="கூற்று-காரண வினாக்களில் 'ஏனென்றால்' என்ற சொல்லை இணைத்து காரணத் தொடர்பை சரிபார்க்கவும்.",
            fact_en="Parliamentary committees are vital institutional safeguards for democratic accountability.",
            fact_ta="நாடாளுமன்றக் குழுக்கள் ஜனநாயகப் பொறுப்புடைமையை நிலைநிறுத்தும் முக்கிய அமைப்புகளாகும்."
        ))

    return questions

def main():
    qs = get_reasoning_questions()
    print(f"Generated {len(qs)} Reasoning questions.")
    balanced_qs = randomize_and_balance_dataset(qs, seed=2030)
    keys = [q["correct_answer"] for q in balanced_qs]
    print("Part 2B PC Reasoning Key counts:", Counter(keys))

    validator = ContentValidator()
    all_errors = []
    for q in balanced_qs:
        errs = validator.validate_question(q)
        if errs:
            all_errors.extend(errs)

    if all_errors:
        print(f"Validation failed with {len(all_errors)} errors:")
        for err in all_errors[:10]:
            print(f"  - {err}")
        raise ValueError("Validation failed!")

    out_file1 = "data/questions/polity/parliamentary_committees_reasoning.json"
    out_file2 = "data/questions/polity/parliamentary_committees_assertion_reason.json"

    with open(out_file1, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    with open(out_file2, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)

    print(f"Successfully wrote {len(balanced_qs)} reasoning MCQs to {out_file1} and alias {out_file2}")

if __name__ == "__main__":
    main()
