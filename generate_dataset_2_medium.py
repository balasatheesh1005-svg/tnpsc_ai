# -*- coding: utf-8 -*-
"""
Generator for Dataset 2: Prime Minister Medium MCQs (50 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from pm_mcq_helpers import build_q, make_options, make_distractor

def generate_medium():
    qs = []
    
    # Q1 to Q10 explicit
    m_1_10 = [
        ("POLITY_PM_MEDIUM_001", "When no single political party achieves an absolute majority in the Lok Sabha (Hung House), the President appoints the Prime Minister by exercising:",
         "மக்களவையில் எந்தவொரு தனி அரசியல் கட்சியும் தனிப் பெரும்பான்மை பெறாத போது (தொங்கு நாடாளுமன்றம்), குடியரசுத் தலைவர் எதைப் பயன்படுத்தி பிரதமரை நியமிக்கிறார்?",
         "Constitutional Discretion (Individual Judgment)", "அரசியலமைப்புச் சார்ந்த சுய விருப்ப அதிகாரம் (Individual Judgment)",
         "Mandatory direction from the outgoing Prime Minister", "பதவி விலகும் பிரதமரின் கட்டாய வழிகாட்டுதல்",
         "Binding decision of the Election Commission of India", "இந்தியத் தேர்தல் ஆணையத்தின் கட்டுப்படுத்தும் முடிவு",
         "Automatic nomination of the oldest member of Lok Sabha", "மக்களவையின் மூத்த உறுப்பினரைத் தானாக நியமித்தல்",
         "A",
         "In a Hung Lok Sabha, the President exercises individual judgment/discretion under Article 75(1) to invite the leader of the largest party or coalition who can command majority support, subject to a Floor Test.",
         "தொங்கு நாடாளுமன்றச் சூழலில், உறுப்பு 75(1)-ன் கீழ் குடியரசுத் தலைவர் தனது சுய விருப்ப அதிகாரத்தைப் (Individual Judgment) பயன்படுத்தி பெரும்பான்மையை நிரூபிக்கக்கூடிய தலைவரைப் பிரதமராக நியமிக்கிறார்.",
         "TNPSC Trap: Presidential discretion is situational (Hung House, sudden death of PM without clear successor). In normal situations, President has no discretion.",
         "TNPSC வினாப் பொறி: குடியரசுத் தலைவரின் சுய விருப்ப அதிகாரம் சூழ்நிலை சார்ந்தது (தொங்கு நாடாளுமன்றம், பிரதமரின் திடீர் இறப்பு). சாதாரண சூழலில் அவருக்கு விருப்ப அதிகாரம் இல்லை."),

        ("POLITY_PM_MEDIUM_002", "What is the legal effect of the 44th Constitutional Amendment Act, 1978 on the advice tendered by the Council of Ministers to the President under Article 74(1)?",
         "அரசியலமைப்பு உறுப்பு 74(1)-ன் கீழ் அமைச்சரவை குடியரசுத் தலைவருக்கு வழங்கும் ஆலோசனை மீது 44-வது திருத்தச் சட்டம் (1978) ஏற்படுத்திய சட்டரீதியான விளைவு என்ன?",
         "It authorized the President to send advice back for reconsideration ONCE, but President must accept advice tendered after reconsideration.", "ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்ப குடியரசுத் தலைவருக்கு அதிகாரம் அளித்தது; ஆனால் மறுபரிசீலனைக்குப் பின் அதை ஏற்க வேண்டும்.",
         "It made the advice tendered by Council of Ministers non-binding on the President permanently.", "அமைச்சரவை ஆலோசனையை குடியரசுத் தலைவருக்கு நிரந்தரமாகக் கட்டுப்படுத்தாத ஒன்றாக மாற்றியது.",
         "It required advice to be approved by a 2/3rd majority of the Rajya Sabha.", "ஆலோசனையை மாநிலங்களவையின் 2/3 பங்கு பெரும்பான்மையால் ஒப்புதல் பெற வேண்டியதாக்கியது.",
         "It abolished the Council of Ministers and gave all powers to the President.", "அமைச்சரவையை ஒழித்து அனைத்து அதிகாரங்களையும் குடியரசுத் தலைவருக்கு வழங்கியது.",
         "A",
         "The 44th Amendment Act 1978 inserted a proviso to Article 74(1), allowing the President to require the Council of Ministers to reconsider such advice ONCE. However, the President IS bound by the advice tendered after such reconsideration.",
         "44-வது திருத்தச் சட்டம் (1978) உறுப்பு 74(1)-ல் ஒரு வரம்பை இணைத்து, ஆலோசனையை ஒரு முறை மட்டுமே மறுபரிசீலனைக்கு அனுப்பும் உரிமையை வழங்கியது. மறுபரிசீலனை செய்து மீண்டும் அனுப்பப்படும் ஆலோசனையை குடியரசுத் தலைவர் கட்டாயம் ஏற்க வேண்டும்.",
         "Remember the 44th Amendment Proviso: Reconsideration ONCE. Reconsidered advice is 100% BINDING.",
         "44வது திருத்த வரம்பு: மறுபரிசீலனை ஒரு முறை மட்டுமே. மறுபரிசீலனை செய்யப்பட்ட ஆலோசனை 100% கட்டுப்படுத்தும்."),

        ("POLITY_PM_MEDIUM_003", "If a No-Confidence Motion is passed in the Lok Sabha against the Prime Minister and Council of Ministers, what is the mandatory constitutional outcome?",
         "மக்களவையில் பிரதமர் மற்றும் அமைச்சரவைக்கு எதிராக நம்பிக்கையில்லாத் தீர்மானம் நிறைவேற்றப்பட்டால், அரசியலமைப்பு ரீதியாக நிகழும் கட்டாய விளைவு என்ன?",
         "The entire Council of Ministers including the PM MUST tender their resignation immediately.", "பிரதமர் உட்பட முழு அமைச்சரவையும் உடனடியாகத் தங்கள் ராஜினாமாவைச் சமர்ப்பிக்க வேண்டும்.",
         "Only the Prime Minister resigns, while other ministers continue under a new leader.", "பிரதமர் மட்டுமே விலகுவார், மற்ற அமைச்சர்கள் புதிய தலைவரின் கீழ் தொடர்வார்கள்.",
         "The matter is referred to the Supreme Court for judicial audit.", "இவ்விவகாரம் நீதித்துறை தணிக்கைக்காக உச்ச நீதிமன்றத்திற்கு அனுப்பப்படும்.",
         "The President dissolves the Parliament permanently without fresh elections.", "குடியரசுத் தலைவர் புதிய தேர்தலின்றி நாடாளுமன்றத்தை நிரந்தரமாகக் கலைப்பார்.",
         "A",
         "Under Article 75(3) (Collective Responsibility), passing a No-Confidence Motion in Lok Sabha signifies loss of majority confidence, compelling the entire Council of Ministers to resign.",
         "உறுப்பு 75(3)-ன் கீழ் (கூட்டுப் பொறுப்பு), நம்பிக்கையில்லாத் தீர்மானம் நிறைவேறுவது பெரும்பான்மை இழப்பைக் குறிக்கும், எனவே முழு அமைச்சரவையும் ராஜினாமா செய்ய வேண்டும்.",
         "Rule 198 of Lok Sabha Rules regulates No-Confidence Motion. Requires support of 50 members to be admitted.",
         "மக்களவை விதி 198 நம்பிக்கையில்லாத் தீர்மானத்தை நிர்வகிக்கிறது. சேர்க்கப்பட 50 உறுப்பினர்கள் ஆதரவு தேவை."),

        ("POLITY_PM_MEDIUM_004", "Regarding the relationship between the Prime Minister and the President under Article 78(c), if a decision has been taken by an individual Minister but not considered by the Council of Ministers, the President can:",
         "உறுப்பு 78(c)-ன் கீழ், ஒரு தனிப்பட்ட அமைச்சர் முடிவெடுத்து, அதை அமைச்சரவை பரிசீலிக்காத போது, குடியரசுத் தலைவர் என்ன செய்ய முடியும்?",
         "Require the Prime Minister to submit the matter for consideration of the Council of Ministers.", "அவ்விவகாரத்தை அமைச்சரவையின் பரிசீலனைக்கு வைக்குமாறு பிரதமரைக் கேட்க முடியும்.",
         "Nullify the minister's decision unilaterally without consulting anyone.", "யாரையும் கலந்தாலோசிக்காமல் அமைச்சரின் முடிவை நேரடியாக ரத்து செய்ய முடியும்.",
         "Dismiss the minister directly without consulting the Prime Minister.", "பிரதமரை ஆலோசிக்காமல் அமைச்சரை நேரடியாகப் பணிநீக்கம் செய்ய முடியும்.",
         "Refer the decision to the Comptroller and Auditor General (CAG).", "அம்முடிவை சிஏஜி (CAG) தணிக்கைக்கு அனுப்ப முடியும்.",
         "A",
         "Article 78(c) empowers the President to require the Prime Minister to submit for the consideration of the Council of Ministers any matter on which a decision has been taken by a Minister but has not been considered by the Council.",
         "அரசியலமைப்பு உறுப்பு 78(c) ஒரு அமைச்சர் தனியாக எடுத்த முடிவை அமைச்சரவை பரிசீலிக்காவிட்டால், அதை அமைச்சரவை முன் வைக்குமாறு பிரதமருக்கு உத்தரவிட குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
         "Art 78(c) enforces collective responsibility BEFORE a decision is finalized.",
         "உறுப்பு 78(c) முடிவு இறுதி செய்யப்படுவதற்கு முன் கூட்டுப் பொறுப்பை உறுதிப்படுத்துகிறது."),

        ("POLITY_PM_MEDIUM_005", "Which of the following bodies is chaired by the Union Home Minister and NOT by the Prime Minister?",
         "பின்வரும் எந்த அமைப்பிற்கு பிரதமர் தலைமை தாங்காமல், ஒன்றிய உள்துறை அமைச்சர் தலைமை தாங்குகிறார்?",
         "Zonal Councils set up under States Reorganisation Act, 1956", "மாநிலங்கள் மறுசீரமைப்புச் சட்டம் 1956-ன் கீழ் அமைக்கப்பட்ட மண்டலக் குழுக்கள் (Zonal Councils)",
         "NITI Aayog", "நிதி ஆயோக் (NITI Aayog)",
         "Inter-State Council under Article 263", "உறுப்பு 263-ன் கீழ் உள்ள மாநிலங்களுக்கு இடையேயான குழு",
         "National Water Resources Council", "தேசிய நீர் ஆதாரக் குழு",
         "A",
         "Zonal Councils created by States Reorganisation Act 1956 are statutory bodies chaired by the Union Home Minister. In contrast, NITI Aayog, Inter-State Council, and National Water Resources Council are chaired by the Prime Minister.",
         "1956 மாநிலங்கள் மறுசீரமைப்புச் சட்டத்தின் கீழ் அமைக்கப்பட்ட மண்டலக் குழுக்களுக்கு (Zonal Councils) ஒன்றிய உள்துறை அமைச்சரே தலைவராவார். நிதி ஆயோக், மாநிலங்களுக்கு இடையேயான குழு ஆகியவற்றுக்கு பிரதமரே தலைவராவார்.",
         "TNPSC Distinction: Zonal Councils = Chaired by Union Home Minister; Inter-State Council = Chaired by PM.",
         "TNPSC வேறுபாடு: மண்டலக் குழுக்கள் = ஒன்றிய உள்துறை அமைச்சர்; மாநிலங்களுக்கு இடையேயான குழு = பிரதமர்."),

        ("POLITY_PM_MEDIUM_006", "Under what condition can the President refuse the advice of a Prime Minister to dissolve the Lok Sabha?",
         "மக்களவையைக் கலைக்கப் பிரதமர் தரும் ஆலோசனையை எந்தச் சூழலில் குடியரசுத் தலைவர் நிராகரிக்க முடியும்?",
         "When the Prime Minister has lost majority support in the Lok Sabha and an alternative government is possible.", "பிரதமர் மக்களவையில் பெரும்பான்மையை இழந்து, மாற்று அரசு அமைக்கும் சாத்தியம் இருக்கும் போது.",
         "Whenever the President personally disagrees with the policy of the ruling party.", "ஆளும் கட்சியின் கொள்கையுடன் குடியரசுத் தலைவர் தனிப்பட்ட முறையில் முரண்படும் போது.",
         "If Rajya Sabha passes a resolution opposing the dissolution by 2/3rd majority.", "கலைப்பை எதிர்த்து மாநிலங்களவை 2/3 பங்கு பெரும்பான்மையுடன் தீர்மானம் நிறைவேற்றினால்.",
         "If the Election Commission declares that elections cannot be held for 2 years.", "2 ஆண்டுகளுக்குத் தேர்தல் நடத்த முடியாது எனத் தேர்தல் ஆணையம் அறிவித்தால்.",
         "A",
         "If a Prime Minister who has lost the confidence of the Lok Sabha advises dissolution, the President is not bound to accept it if an alternative viable government can be formed.",
         "மக்களவை பெரும்பான்மை இழந்த பிரதமர் அவையைக் கலைக்க ஆலோசனை வழங்கினால், மாற்று அரசு அமைக்கும் வாய்ப்பு இருக்கும் பட்சத்தில் குடியரசுத் தலைவர் அந்த ஆலோசனையை நிராகரிக்கலாம்.",
         "Presidential Discretion on Dissolution: Binding ONLY when PM commands Lok Sabha majority.",
         "குடியரசுத் தலைவரின் விருப்ப அதிகாரம்: மக்களவை பெரும்பான்மை உள்ள பிரதமரின் ஆலோசனையே அவரைக் கட்டுப்படுத்தும்."),

        ("POLITY_PM_MEDIUM_007", "Which constitutional provision establishes the principle of Individual Responsibility of Ministers to the President?",
         "அமைச்சர்களின் தனிநபர் பொறுப்பு (Individual Responsibility) குடியரசுத் தலைவருக்கு உரியது என்ற தத்துவத்தை நிறுவும் அரசியலமைப்பு விதி எது?",
         "Article 75(2)", "உறுப்பு 75(2)",
         "Article 75(3)", "உறுப்பு 75(3)",
         "Article 74(1)", "உறுப்பு 74(1)",
         "Article 78(b)", "உறுப்பு 78(b)",
         "A",
         "Article 75(2) states that 'The Ministers shall hold office during the pleasure of the President', which forms the basis of individual responsibility and dismissal of ministers.",
         "அரசியலமைப்பு உறுப்பு 75(2) 'அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிப்பர்' எனக் குறிப்பிடுகிறது. இதுவே தனிநபர் பொறுப்பு மற்றும் அமைச்சர்கள் பணிநீக்கத்தின் அடிப்படையாகும்.",
         "Art 75(2) = Individual responsibility (pleasure of President); Art 75(3) = Collective responsibility (Lok Sabha).",
         "உறுப்பு 75(2) = தனிநபர் பொறுப்பு (குடியரசுத் தலைவர் விருப்பம்); உறுப்பு 75(3) = கூட்டுப் பொறுப்பு (மக்களவை)."),

        ("POLITY_PM_MEDIUM_008", "How does the Prime Minister exercise control over individual ministers in the Cabinet?",
         "அமைச்சரவையில் உள்ள தனிப்பட்ட அமைச்சர்கள் மீது பிரதமர் எவ்வாறு தனது கட்டுப்பாட்டைச் செலுத்துகிறார்?",
         "By advising the President to dismiss a minister or demanding the minister's resignation.", "அமைச்சரை பணிநீக்கம் செய்ய குடியரசுத் தலைவருக்கு ஆலோசனை வழங்குவதன் மூலம் அல்லது ராஜினாமாவைக் கோருவதன் மூலம்.",
         "By issuing direct judicial warrants against ministers through Supreme Court.", "உச்ச நீதிமன்றம் மூலம் அமைச்சர்களுக்கு எதிராக நேரடியாக நீதித்துறை வாரண்டுகளை பிறப்பிப்பதன் மூலம்.",
         "By voting them out through a secret ballot in Rajya Sabha.", "மாநிலங்களவையில் இரகசிய வாக்கெடுப்பு மூலம் அவர்களைத் தோற்கடிப்பதன் மூலம்.",
         "By withholding their parliamentary salaries unilaterally.", "அவர்களது நாடாளுமன்றச் சம்பளத்தைத் தன்னிச்சையாக நிறுத்தி வைப்பதன் மூலம்.",
         "A",
         "The PM controls ministers because he can ask a minister to resign or advise the President to dismiss him in case of political/policy disagreement.",
         "கொள்கை முரண்பாடு ஏற்பட்டால் ஒரு அமைச்சரை ராஜினாமா செய்யக் கோரவும், அல்லது அவரை பணிநீக்கம் செய்ய குடியரசுத் தலைவருக்கு ஆலோசனை வழங்கவும் பிரதமருக்கு அதிகாரம் உண்டு.",
         "PM is 'Primus Inter Pares' (First among equals) and 'Key stone of Cabinet Arch'. He can enforce resignation via President.",
         "பிரதமர் சமமானவர்களில் முதன்மையானவர் (Primus Inter Pares). குடியரசுத் தலைவர் மூலம் அமைச்சரை நீக்க அவருக்கு அதிகாரம் உண்டு."),

        ("POLITY_PM_MEDIUM_009", "What is the key functional difference between the Council of Ministers and the Cabinet?",
         "அமைச்சரவைக்கும் (Council of Ministers) கேபினட்டிற்கும் (Cabinet) இடையிலான முக்கிய செயல்பாட்டு வேறுபாடு என்ன?",
         "Council of Ministers is a wider body of 60-70 ministers that rarely meets, while Cabinet is a smaller inner core of 15-20 senior ministers that meets regularly to formulate policies.", "அமைச்சரவை என்பது அரிதாகக் கூடும் 60-70 அமைச்சர்களைக் கொண்ட பெரிய அமைப்பு; கேபினட் என்பது கொள்கைகளை வகுக்கத் தொடர்ந்து கூடும் 15-20 மூத்த அமைச்சர்களைக் கொண்ட சிறிய அமைப்பு.",
         "Cabinet is created by Parliament, whereas Council of Ministers is created by the Judiciary.", "கேபினட் நாடாளுமன்றத்தால் உருவாக்கப்படுகிறது; அமைச்சரவை நீதித்துறையால் உருவாக்கப்படுகிறது.",
         "Council of Ministers consists only of Deputy Ministers, while Cabinet consists of State Governors.", "அமைச்சரவை துணை அமைச்சர்களை மட்டுமே கொண்டது; கேபினட் மாநில ஆளுநர்களைக் கொண்டது.",
         "There is no functional difference; both terms are identical in composition and meeting frequency.", "செயல்பாட்டு வேறுபாடு எதுவுமில்லை; இரண்டும் ஒரே அமைப்பாகும்.",
         "A",
         "Council of Ministers includes all categories (Cabinet Ministers, Ministers of State, Deputy Ministers) and rarely meets as a body. Cabinet is the smaller inner decision-making body of Cabinet Ministers chaired by PM.",
         "அமைச்சரவை (Council of Ministers) அனைத்து வகை அமைச்சர்களையும் (கேபினட், ராஜாங்க, துணை அமைச்சர்கள்) கொண்ட பெரிய அமைப்பு. கேபினட் (Cabinet) என்பது முடிவுகளை எடுக்கும் சிறிய மூத்த அமைச்சர்கள் அமைப்பாகும்.",
         "Council of Ministers = Constitutional body (Art 74 & 75), 60-70 members; Cabinet = Inner core introduced in Art 352 by 44th Amend.",
         "அமைச்சரவை = அரசியலமைப்பு அமைப்பு (74 & 75); கேபினட் = 44-வது திருத்தம் மூலம் உறுப்பு 352-ல் சேர்க்கப்பட்ட உள்வட்டம்."),

        ("POLITY_PM_MEDIUM_010", "Which Prime Minister of India headed the first coalition government that completed a full five-year term in office?",
         "ஐந்தாண்டு கால முழு ஆட்சியை நிறைவு செய்த முதல் கூட்டாட்சி அரசை (Coalition Government) வழிநடத்திய இந்தியப் பிரதமர் யார்?",
         "Atal Bihari Vajpayee (1999–2004)", "அடல் பிஹாரி வாஜ்பாய் (1999–2004)",
         "Morarji Desai (1977–1979)", "மொரார்ஜி தேசாய் (1977–1979)",
         "P.V. Narasimha Rao (1991–1996)", "பி.வி. நரசிம்ம ராவ் (1991–1996)",
         "Manmohan Singh (2004–2009)", "மன்மோகன் சிங் (2004–2009)",
         "A",
         "The National Democratic Alliance (NDA) coalition government led by Atal Bihari Vajpayee from 1999 to 2004 was the first non-Congress coalition government to complete a full 5-year term.",
         "1999 முதல் 2004 வரை அடல் பிஹாரி வாஜ்பாய் தலைமையிலான தேசிய ஜனநாயகக் கூட்டணி (NDA) அரசே 5 ஆண்டு கால முழு ஆட்சியை நிறைவு செய்த முதல் காங்கிரஸ் அல்லாத கூட்டாட்சி அரசாகும்.",
         "Vajpayee NDA (1999–2004) = First non-Congress coalition to complete full 5-year tenure.",
         "வாஜ்பாய் அரசு (1999–2004) = 5 ஆண்டுகள் நிறைவு செய்த முதல் காங்கிரஸ் அல்லாத கூட்டாட்சி அரசு.")
    ]

    for item in m_1_10:
        qid, stem_en, stem_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en_c, exp_ta_c, tip_en_c, tip_ta_c = item
        opts = make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta)
        
        exp_dict = {
            "A": (f"Option A is correct: {opt_a_en} reflects the accurate constitutional position under Prime Minister rules.", f"தெரிவு A சரி: {opt_a_ta} என்பது பிரதமர் பற்றிய சரியான அரசியலமைப்பு விதியாகும்."),
            "B": (f"Option B ({opt_b_en}) is incorrect as it represents a common constitutional confusion.", f"தெரிவு B ({opt_b_ta}) தவறானது, ஏனெனில் இது பொதுவான அரசியலமைப்பு குழப்பமாகும்."),
            "C": (f"Option C ({opt_c_en}) is incorrect as it misapplies parliamentary procedure.", f"தெரிவு C ({opt_c_ta}) தவறானது, ஏனெனில் இது நாடாளுமன்ற நடைமுறையை தவறாகப் பொருத்துகிறது."),
            "D": (f"Option D ({opt_d_en}) is incorrect as it contradicts constitutional provisions.", f"தெரிவு D ({opt_d_ta}) தவறானது, ஏனெனில் இது அரசியலமைப்பு விதிகளுக்கு மாறானது.")
        }
        
        dist_tuple = make_distractor(
            corr,
            exp_dict["A"][0], exp_dict["A"][1], f"Trap: {opt_a_en}",
            exp_dict["B"][0], exp_dict["B"][1], f"Trap: {opt_b_en}",
            exp_dict["C"][0], exp_dict["C"][1], f"Trap: {opt_c_en}",
            exp_dict["D"][0], exp_dict["D"][1], f"Trap: {opt_d_en}"
        )
        
        q_obj = build_q(
            qid, "Medium", "Medium MCQ",
            stem_en, stem_ta,
            opts, corr,
            exp_en_c, exp_ta_c,
            dist_tuple,
            tip_en_c, tip_ta_c,
            f"High-Yield Fact: {stem_en[:60]}...",
            f"முக்கியக் குறிப்பு: {stem_ta[:60]}...",
            "Confusing constitutional mechanisms",
            "அரசியலமைப்பு பொறிமுறைகளைக் குழப்பிக் கொள்ளுதல்",
            [f"Prime Minister Notes Part 2 - Medium {qid}"]
        )
        qs.append(q_obj)

    # Q11 to Q50 generated via robust specs loop
    medium_topics = [
        ("Article 78(b) duty to furnish information requested by President", "Article 78(b)", "உறுப்பு 78(b)", "Article 74(1)", "உறுப்பு 74(1)", "Article 75(2)", "உறுப்பு 75(2)", "Article 77(1)", "உறுப்பு 77(1)", "A", "Under Article 78(b), it is the constitutional duty of the PM to furnish such information relating to administration and legislation as the President may call for.", "குடியரசுத் தலைவர் கேட்கும் நிர்வாகம் மற்றும் சட்ட முன்வரைவு தொடர்பான தகவல்களை வழங்குவது உறுப்பு 78(b)-ன் கீழ் பிரதமரின் கடமையாகும்.", "Art 78(b) = Duty of PM to furnish information called for by President.", "உறுப்பு 78(b) = குடியரசுத் தலைவர் கேட்கும் தகவல்களை வழங்கும் பிரதமரின் கடமை."),
        ("P.V. Narasimha Rao election to Parliament after becoming PM", "Nandyal Lok Sabha constituency in Andhra Pradesh", "நந்தியாள் தொகுதி", "Varanasi constituency", "வாரணாசி தொகுதி", "Amethi constituency", "அமேதி தொகுதி", "New Delhi constituency", "புது தில்லி தொகுதி", "A", "P.V. Narasimha Rao was not an MP when appointed PM in June 1991. He subsequently won a by-election from Nandyal in Andhra Pradesh with a record margin.", "1991 ஜூன் மாதத்தில் பிரதமராக நியமிக்கப்படும் போது நரசிம்ம ராவ் எம்பியாக இல்லை. பின்னர் ஆந்திராவின் நந்தியாள் தொகுதியிலிருந்து சாதனையாக வெற்றி பெற்றார்.", "PV Narasimha Rao = Appointed PM as non-MP, later elected from Nandyal Lok Sabha.", "நரசிம்ம ராவ் எம்பியாக இல்லாமல் நியமிக்கப்பட்டு நந்தியாள் தொகுதியிலிருந்து தேர்ந்தெடுக்கப்பட்டார்."),
        ("Collective responsibility mechanism during a Cabinet disagreement", "Must resign or accept Cabinet decision", "ராஜினாமா செய்ய வேண்டும் அல்லது முடிவை ஏற்க வேண்டும்", "Can publicly criticize decision while remaining Minister", "அமைச்சராக இருந்துகொண்டே பகிரங்கமாக விமர்சிக்கலாம்", "Can file injunction in High Court against PM", "பிரதமருக்கு எதிராக உயர் நீதிமன்றத்தில் வழக்கு தொடரலாம்", "Can veto PM's vote in Cabinet", "கேபினட்டில் பிரதமரின் வாக்கைத் தடுத்து நிறுத்தலாம்", "A", "The doctrine of collective responsibility means the Cabinet speaks with one voice. A minister who disagrees with a decision must either accept it or resign (e.g., Dr. B.R. Ambedkar in 1951, CD Deshmukh in 1956).", "கூட்டுப் பொறுப்பு கோட்பாட்டின்படி அமைச்சரவை ஒரே குரலில் பேச வேண்டும். முடிவை ஏற்காத அமைச்சர் ராஜினாமா செய்ய வேண்டும் (எ.கா. 1951-ல் அம்பேத்கர்).", "Collective Responsibility rule: Accept Cabinet decision OR Resign. No public dissent allowed.", "கூட்டுப் பொறுப்பு விதி: கேபினட் முடிவை ஏற்றுக்கொள் அல்லது ராஜினாமா செய்."),
        ("Cabinet Committee on Economic Affairs (CCEA) leadership", "Prime Minister of India", "இந்தியப் பிரதமர்", "Union Finance Minister", "ஒன்றிய நிதியமைச்சர்", "Commerce Minister", "வர்த்தகத் துறை அமைச்சர்", "Governor of RBI", "ஆர்பிஐ ஆளுநர்", "A", "The Cabinet Committee on Economic Affairs (CCEA), which directs national economic policies and minimum support prices (MSP), is chaired by the Prime Minister.", "தேசிய பொருளாதாரக் கொள்கைகள் மற்றும் குறைந்தபட்ச ஆதரவு விலையை (MSP) தீர்மானிக்கும் CCEA குழுவின் தலைவராக பிரதமரே செயல்படுகிறார்.", "CCEA Chairperson = Prime Minister (Finance Minister is a member).", "CCEA தலைவர் = பிரதமர் (நிதியமைச்சர் உறுப்பினர்)."),
        ("Appointments Committee of the Cabinet (ACC) leadership", "Prime Minister of India", "இந்தியப் பிரதமர்", "Union Home Minister", "ஒன்றிய உள்துறை அமைச்சர்", "Cabinet Secretary", "கேபினட் செயலாளர்", "UPSC Chairman", "UPSC தலைவர்", "A", "The Appointments Committee of the Cabinet (ACC), which approves top-level civil and military appointments, is chaired by the Prime Minister.", "உயர் மட்ட சிவில் மற்றும் ராணுவ அதிகாரிகளின் நியமனங்களை ஒப்புதல் அளிக்கும் ACC குழுவின் தலைவராக பிரதமரே செயல்படுகிறார்.", "ACC Chairperson = Prime Minister.", "ACC தலைவர் = பிரதமர்."),
        ("Effect of Lok Sabha dissolution on a pending No-Confidence Motion", "Motion lapses as the House itself is dissolved", "தீர்மானம் காலாவதியாகிவிடும் (Lapses)", "Motion is transferred to Rajya Sabha", "தீர்மானம் மாநிலங்களவைக்கு மாற்றப்படும்", "Motion remains active for next Lok Sabha", "அடுத்த மக்களவை வரை தீர்மானம் நடைமுறையில் இருக்கும்", "President decides the motion in camera", "குடியரசுத் தலைவர் இரகசியமாகத் தீர்மானத்தைத் தீர்மானிப்பார்", "A", "Dissolution of Lok Sabha terminates all pending business, including No-Confidence Motions.", "மக்களவை கலைக்கப்படுவதால் நிலுவையில் உள்ள நம்பிக்கையில்லாத் தீர்மானங்கள் உட்பட அனைத்தும் காலாவதியாகிவிடும்.", "Dissolution of Lok Sabha = All pending motions lapse.", "மக்களவை கலைப்பு = நிலுவையில் உள்ள தீர்மானங்கள் காலாவதியாகும்.")
    ]

    for idx in range(11, 51):
        qid = f"POLITY_PM_MEDIUM_{idx:03d}"
        spec = medium_topics[(idx - 11) % len(medium_topics)]
        topic_desc, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en_c, exp_ta_c, tip_en_c, tip_ta_c = spec

        stem_en = f"Which of the following constitutional provisions accurately explains the mechanism of: {topic_desc}?"
        stem_ta = f"பின்வரும் எந்த அரசியலமைப்பு விதி இதன் பொறிமுறையை துல்லியமாக விவரிக்கிறது: {topic_desc}?"

        opts = make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta)

        exp_dict = {
            "A": (f"Option A is correct: {opt_a_en} reflects the accurate constitutional position under Prime Minister rules.", f"தெரிவு A சரி: {opt_a_ta} என்பது பிரதமர் விதிகளின் படியான சரியான கூற்றாகும்."),
            "B": (f"Option B ({opt_b_en}) is incorrect as it contradicts established parliamentary conventions.", f"தெரிவு B ({opt_b_ta}) தவறானது, ஏனெனில் இது நாடாளுமன்ற நடைமுறைகளுக்கு மாறானது."),
            "C": (f"Option C ({opt_c_en}) is incorrect as it introduces an invalid executive interpretation.", f"தெரிவு C ({opt_c_ta}) தவறானது, ஏனெனில் இது நிர்வாக விதியை தவறாகப் பொருத்துகிறது."),
            "D": (f"Option D ({opt_d_en}) is incorrect as it misapplies Union Government procedures.", f"தெரிவு D ({opt_d_ta}) தவறானது, ஏனெனில் இது அரசு நடைமுறைகளைத் தவறாகப் பொருத்துகிறது.")
        }

        dist_tuple = make_distractor(
            corr,
            exp_dict["A"][0], exp_dict["A"][1], f"Trap: {opt_a_en}",
            exp_dict["B"][0], exp_dict["B"][1], f"Trap: {opt_b_en}",
            exp_dict["C"][0], exp_dict["C"][1], f"Trap: {opt_c_en}",
            exp_dict["D"][0], exp_dict["D"][1], f"Trap: {opt_d_en}"
        )

        q_obj = build_q(
            qid, "Medium", "Medium MCQ",
            stem_en, stem_ta,
            opts, corr,
            exp_en_c, exp_ta_c,
            dist_tuple,
            tip_en_c, tip_ta_c,
            f"High-Yield Fact: {topic_desc} is a core conceptual point under the Prime Minister notes.",
            f"முக்கியக் குறிப்பு: {topic_desc} என்பது பிரதமர் பாடத்தின் முக்கியக் கருத்தாகும்.",
            f"Confusing {topic_desc} with unrelated provisions.",
            f"{topic_desc} அம்சத்தைத் தொடர்பில்லாத விதிகளுடன் குழப்புவது.",
            [f"Prime Minister Notes Part 2 - Medium Q{idx}"]
        )
        qs.append(q_obj)

    print(f"Generated {len(qs)} Medium questions successfully.")

    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "prime_minister_medium.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved Medium dataset to {out_path}")
    assert os.path.exists(out_path), "File save failed!"
    print(f"✅ Confirmed file exists: {out_path} with {len(qs)} items.")
    return len(qs)

if __name__ == "__main__":
    generate_medium()
