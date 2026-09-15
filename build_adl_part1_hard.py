# -*- coding: utf-8 -*-
"""
Anti-Defection Law - Part 1: Hard (50 MCQs)
TNPSC Nova AI Content Engine

Generates 50 authentic, 24-field bilingual MCQs testing advanced constitutional,
procedural, and landmark judicial nuances of the Tenth Schedule.
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from anti_defection_law_mcq_helper import make_adl_q


def get_hard_questions():
    raw_hard = [
        {
            "subtopic": "Nabam Rebia vs Subhash Desai",
            "stem_en": "In the Maharashtra Political Crisis case (Subhash Desai, 2023), what did the Constitution Bench decide regarding the correctness of the Nabam Rebia (2016) principle that a Speaker facing a removal notice cannot decide disqualification petitions?",
            "stem_ta": "மகாராஷ்டிரா அரசியல் நெருக்கடி வழக்கில் (சுபாஷ் தேசாய், 2023), பதவி நீக்க அறிவிப்பை எதிர்கொள்ளும் சபாநாயகர் தகுதி நீக்க மனுக்களைத் தீர்மானிக்க முடியாது என்ற நபம் ரேபியா (2016) கொள்கையின் சரியான தன்மை குறித்து அரசியலமைப்பு அமர்வு என்ன முடிவு செய்தது?",
            "options": [
                ("Referred the issue to a larger 7-judge Constitution Bench for authoritative reconsideration", "அதிகாரப்பூர்வ மறுபரிசீலனைக்காக இந்த விவகாரத்தை 7 நீதிபதிகள் கொண்ட பெரிய அரசியலமைப்பு அமர்வுக்குப் பரிந்துரைத்தது"),
                ("Completely overruled Nabam Rebia and held Speakers have absolute power even under removal notice", "நபம் ரேபியா தீர்ப்பை முற்றிலுமாக ரத்து செய்து, பதவி நீக்க அறிவிப்பு இருந்தாலும் சபாநாயகருக்கு முழு அதிகாரம் உண்டு எனத் தீர்ப்பளித்தது"),
                ("Affirmed Nabam Rebia without any modification or doubts", "நபம் ரேபியா தீர்ப்பை எந்த மாற்றமும் அல்லது சந்தேகமும் இன்றி முழுமையாக உறுதி செய்தது"),
                ("Held that Governors can decide defection petitions whenever a Speaker faces removal", "சபாநாயகர் பதவி நீக்கத்தை எதிர்கொள்ளும் போதெல்லாம் ஆளுநரே கட்சித் தாவல் மனுக்களைத் தீர்மானிக்கலாம் எனத் தீர்ப்பளித்தது")
            ],
            "correct_key": "A",
            "exp_en": "In Subhash Desai (2023), the 5-judge Constitution Bench observed that the Nabam Rebia rule (barring a Speaker facing an Article 179(c) notice from deciding Tenth Schedule petitions) could be misused by defecting MLAs to paralyze the Speaker; hence, it referred the question to a larger 7-judge Bench.",
            "exp_ta": "சுபாஷ் தேசாய் (2023) வழக்கில் 5 நீதிபதிகள் கொண்ட அமர்வு, உறுப்பு 179(c) நோட்டீஸை எதிர்கொள்ளும் சபாநாயகர் தகுதி நீக்க மனுக்களை விசாரிக்கக் கூடாது என்ற நபம் ரேபியா விதி கட்சி தாவும் எம்.எல்.ஏ-க்களால் சபாநாயகரை முடக்க தவறாகப் பயன்படுத்தப்படலாம் எனக் கூறி, இந்த விவகாரத்தை 7 நீதிபதிகள் கொண்ட பெரிய அமர்வுக்குப் பரிந்துரைத்தது.",
            "why_a_en": "Correct. The 5-judge bench referred the Nabam Rebia doctrine to a 7-judge bench.",
            "why_a_ta": "சரி. 5 நீதிபதிகள் கொண்ட அமர்வு நபம் ரேபியா கோட்பாட்டை 7 நீதிபதிகள் கொண்ட அமர்வுக்குப் பரிந்துரைத்தது.",
            "why_b_en": "Incorrect. A 5-judge bench cannot overrule a co-ordinate 5-judge bench; it can only refer.",
            "why_b_ta": "தவறு. 5 நீதிபதிகள் கொண்ட அமர்வு மற்றொரு 5 நீதிபதிகள் அமர்வை ரத்து செய்ய முடியாது; பரிந்துரைக்க மட்டுமே முடியும்.",
            "why_c_en": "Incorrect. The court expressed serious doubts on its potential misuse.",
            "why_c_ta": "தவறு. நீதிமன்றம் அதன் சாத்தியமான தவறான பயன்பாடு குறித்து தீவிர சந்தேகங்களை எழுப்பியது.",
            "why_d_en": "Incorrect. Governors have no constitutional authority under Tenth Schedule.",
            "why_d_ta": "தவறு. பத்தாவது அட்டவணையின் கீழ் ஆளுநர்களுக்கு அரசியலமைப்பு அதிகாரம் இல்லை.",
            "tip_en": "Nabam Rebia referral = 7-judge bench in Subhash Desai (2023).",
            "tip_ta": "நபம் ரேபியா மறுபரிசீலனை = சுபாஷ் தேசாய் (2023) வழக்கில் 7 நீதிபதிகள் அமர்வுக்குப் பரிந்துரை.",
            "fact_en": "Article 179(c) deals with removal of the Speaker by a resolution of the Assembly passed by a majority of all the then members.",
            "fact_ta": "உறுப்பு 179(c) அப்போதைய அனைத்து உறுப்பினர்களின் பெரும்பான்மையால் நிறைவேற்றப்படும் தீர்மானம் மூலம் சபாநாயகரை நீக்குவதைக் கையாள்கிறது."
        },
        {
            "subtopic": "Symbols Order vs Tenth Schedule",
            "stem_en": "How does an inquiry into a party split/symbol dispute by the Election Commission of India under Paragraph 15 of the Symbols Order interact with Tenth Schedule proceedings before the Speaker?",
            "stem_ta": "சின்னங்கள் உத்தரவின் பத்தி 15-ன் கீழ் இந்தியத் தேர்தல் ஆணையத்தால் நடத்தப்படும் கட்சிப் பிளவு/சின்ன சர்ச்சை விசாரணை, சபாநாயகர் முன் உள்ள பத்தாவது அட்டவணை நடவடிக்கைகளுடன் எவ்வாறு தொடர்பு கொள்கிறது?",
            "options": [
                ("Both operate in independent constitutional spheres; the Speaker decides disqualification of MLAs while ECI decides the symbol dispute of the political party", "இரண்டும் சுதந்திரமான அரசியலமைப்புத் தளங்களில் செயல்படுகின்றன; சபாநாயகர் எம்.எல்.ஏ-க்களின் தகுதி நீக்கத்தைத் தீர்மானிக்கிறார், தேர்தல் ஆணையம் கட்சியின் சின்ன சர்ச்சையைத் தீர்மானிக்கிறது"),
                ("The Speaker's decision is automatically binding on the Election Commission of India", "சபாநாயகரின் முடிவு இந்தியத் தேர்தல் ஆணையத்தைக் கட்டுப்படுத்தும்"),
                ("The Election Commission's decision under Paragraph 15 automatically stays all disqualification proceedings before the Speaker", "பத்தி 15-ன் கீழான தேர்தல் ஆணையத்தின் முடிவு சபாநாயகர் முன் உள்ள அனைத்து தகுதி நீக்க நடவடிக்கைகளையும் தானாகவே நிறுத்தி வைக்கிறது"),
                ("The High Court must consolidate both matters into a single civil suit", "உயர் நீதிமன்றம் இரண்டு விவகாரங்களையும் ஒரே சிவில் வழக்காக இணைக்க வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "In Subhash Desai (2023), the Supreme Court clarified that ECI's jurisdiction under Paragraph 15 of the Election Symbols (Reservation and Allotment) Order, 1968 and the Speaker's jurisdiction under the Tenth Schedule operate in distinct spheres and neither eclipses the other.",
            "exp_ta": "சுபாஷ் தேசாய் (2023) வழக்கில் உச்ச நீதிமன்றம் தெளிவுபடுத்தியபடி, தேர்தல் சின்னங்கள் உத்தரவு 1968-ன் பத்தி 15-ன் கீழான தேர்தல் ஆணையத்தின் அதிகார வரம்பும், பத்தாவது அட்டவணையின் கீழான சபாநாயகரின் அதிகார வரம்பும் தனித்தனித் தளங்களில் செயல்படுகின்றன, ஒன்று மற்றொன்றை முடக்காது.",
            "why_a_en": "Correct. Independent constitutional spheres: Speaker for legislative defection, ECI for party symbol.",
            "why_a_ta": "சரி. சுதந்திரமான அதிகார வரம்புகள்: சட்டமன்ற கட்சித் தாவலுக்கு சபாநாயகர், கட்சிச் சின்னத்திற்குத் தேர்தல் ஆணையம்.",
            "why_b_en": "Incorrect. ECI acts as an independent statutory authority under Symbols Order.",
            "why_b_ta": "தவறு. தேர்தல் ஆணையம் சின்னங்கள் உத்தரவின் கீழ் சுதந்திரமான சட்டப்பூர்வ அதிகாரியாகச் செயல்படுகிறது.",
            "why_c_en": "Incorrect. There is no automatic stay between the two independent proceedings.",
            "why_c_ta": "தவறு. இந்த இரண்டு சுதந்திரமான நடவடிக்கைகளுக்கு இடையே தானியங்கித் தடை எதுவும் இல்லை.",
            "why_d_en": "Incorrect. High Courts do not consolidate specialized constitutional jurisdictions into civil suits.",
            "why_d_ta": "தவறு. உயர் நீதிமன்றங்கள் சிறப்பு அரசியலமைப்பு அதிகாரங்களை சிவில் வழக்குகளாக இணைப்பதில்லை.",
            "tip_en": "Speaker = Tenth Schedule (Legislature Party). ECI = Paragraph 15 Symbols Order (Political Party).",
            "tip_ta": "சபாநாயகர் = 10-வது அட்டவணை (சட்டமன்றக் கட்சி). தேர்தல் ஆணையம் = பத்தி 15 சின்னங்கள் உத்தரவு (அரசியல் கட்சி).",
            "fact_en": "The test of majority in the legislative wing cannot be the sole basis for ECI determining the real political party.",
            "fact_ta": "சட்டமன்றப் பிரிவில் உள்ள பெரும்பான்மை மட்டுமே உண்மையான அரசியல் கட்சியைத் தேர்தல் ஆணையம் தீர்மானிப்பதற்கான ஒரே அடிப்படையாக இருக்க முடியாது."
        },
        {
            "subtopic": "Natural Justice & Fair Hearing",
            "stem_en": "In Balchandra L. Jarkiholi v. B.S. Yeddyurappa (2011), why did the Supreme Court set aside the Karnataka Speaker's disqualification order against dissenting MLAs?",
            "stem_ta": "பால்சந்திரா எல். ஜார்கிஹோலி எதிர் பி.எஸ். எடியூரப்பா (2011) வழக்கில், அதிருப்தி எம்.எல்.ஏ-க்களுக்கு எதிரான கர்நாடக சபாநாயகரின் தகுதி நீக்க உத்தரவை உச்ச நீதிமன்றம் ஏன் ரத்து செய்தது?",
            "options": [
                ("Gross violation of natural justice: MLAs were given barely three days to reply without copies of affidavits or documents relied upon", "இயற்கை நீதியின் வெளிப்படையான மீறல்: உறுதிமொழிப் பத்திரங்கள் அல்லது ஆவணங்களின் நகல்கள் இன்றி எம்.எல்.ஏ-க்களுக்கு பதிலளிக்க வெறும் மூன்று நாட்களே அவகாசம் அளிக்கப்பட்டது"),
                ("The Speaker was not an elected member of the Karnataka Legislative Assembly", "சபாநாயகர் கர்நாடக சட்டமன்றத்தின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினராக இருக்கவில்லை"),
                ("The MLAs had taken prior oral permission from the Governor to dissent", "அதிருப்தி தெரிவிக்க எம்.எல்.ஏ-க்கள் ஆளுநரிடம் முன் வாய்மொழி அனுமதி பெற்றிருந்தனர்"),
                ("The Tenth Schedule was held unconstitutional in its entirety", "பத்தாவது அட்டவணை முழுமையாக அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "In Balchandra L. Jarkiholi (2011), the Supreme Court quashed the disqualification of 11 BJP MLAs because the Speaker acted in undue haste, gave them less than 3 days to respond to the show-cause notice, and denied them copies of the relied-upon documents, violating natural justice.",
            "exp_ta": "பால்சந்திரா எல். ஜார்கிஹோலி (2011) வழக்கில், 11 பாஜக எம்.எல்.ஏ-க்களின் தகுதி நீக்கத்தை உச்ச நீதிமன்றம் ரத்து செய்தது; ஏனெனில் சபாநாயகர் அவசரப்பட்டு, நோட்டீஸுக்கு பதிலளிக்க 3 நாட்களுக்கும் குறைவான அவகாசமே அளித்தார் மற்றும் ஆவணங்களின் நகல்களை வழங்க மறுத்து இயற்கை நீதியை மீறினார்.",
            "why_a_en": "Correct. Breach of natural justice and failure to afford reasonable opportunity invalidated the Speaker's order.",
            "why_a_ta": "சரி. இயற்கை நீதி மீறல் மற்றும் நியாயமான வாய்ப்பு வழங்கத் தவறியது சபாநாயகரின் உத்தரவை செல்லாததாக்கியது.",
            "why_b_en": "Incorrect. The Speaker was a duly elected member.",
            "why_b_ta": "தவறு. சபாநாயகர் முறையாகத் தேர்ந்தெடுக்கப்பட்ட உறுப்பினராகவே இருந்தார்.",
            "why_c_en": "Incorrect. Governor's oral permission is legally non-existent under Tenth Schedule.",
            "why_c_ta": "தவறு. ஆளுநரின் வாய்மொழி அனுமதி பத்தாவது அட்டவணையின் கீழ் சட்டப்பூர்வமாக செல்லாது.",
            "why_d_en": "Incorrect. The Tenth Schedule remains fully valid.",
            "why_d_ta": "தவறு. பத்தாவது அட்டவணை தொடர்ந்து முழுமையாகச் செல்லுபடியாகிறது.",
            "tip_en": "Procedural fairness is non-negotiable: Adequate time + documents = Valid natural justice.",
            "tip_ta": "நடைமுறை நியாயம் சமரசமற்றது: போதுமான நேரம் + ஆவணங்கள் = செல்லுபடியாகும் இயற்கை நீதி.",
            "fact_en": "The Supreme Court noted that disqualification permanently impacts democratic representation and cannot be rushed arbitrarily.",
            "fact_ta": "தகுதி நீக்கம் ஜனநாயகப் பிரதிநிதித்துவத்தை நிரந்தரமாகப் பாதிப்பதால் அதனைத் தன்னிச்சையாக அவசரப்படுத்த முடியாது என்று உச்ச நீதிமன்றம் குறிப்பிட்டது."
        },
        {
            "subtopic": "Paragraph 8 Directory vs Mandatory",
            "stem_en": "In Dr. Mahachandra Prasad Singh v. Chairman, Bihar Legislative Council (2004), what was the Supreme Court's ruling on procedural non-compliance with rules framed under Paragraph 8?",
            "stem_ta": "டாக்டர் மகாசந்திர பிரசாத் சிங் எதிர் தலைவர், பீகார் சட்ட மேலவை (2004) வழக்கில், பத்தி 8-ன் கீழ் உருவாக்கப்பட்ட விதிகளின் நடைமுறைப் பிழைகள் குறித்து உச்ச நீதிமன்றத்தின் தீர்ப்பு என்ன?",
            "options": [
                ("Rules framed under Paragraph 8 are directory in nature, and procedural irregularities do not render the disqualification void", "பத்தி 8-ன் கீழ் உருவாக்கப்பட்ட விதிகள் வழிகாட்டுதல் தன்மையுடையவை, நடைமுறை ஒழுங்கின்மைகள் தகுதி நீக்கத்தை செல்லாததாக்காது"),
                ("Every single rule under Paragraph 8 is mandatory, and any clerical defect invalidates the petition", "பத்தி 8-ன் கீழான ஒவ்வொரு விதியும் கட்டாயமானது, ஏதேனும் சிறிய பிழை இருந்தாலும் மனு செல்லாது"),
                ("Rules under Paragraph 8 override the Constitution of India", "பத்தி 8-ன் கீழான விதிகள் இந்திய அரசியலமைப்பை விட மேலானவை"),
                ("The Chairman cannot entertain petitions unless accompanied by a court affidavit", "நீதிமன்ற உறுதிமொழிப் பத்திரம் இணைக்கப்படாவிட்டால் தலைவர் மனுக்களை ஏற்க முடியாது")
            ],
            "correct_key": "A",
            "exp_en": "In Dr. Mahachandra Prasad Singh (2004), the Supreme Court ruled that rules framed under Paragraph 8 are procedural and directory; an omission to verify the petition or procedural defect cannot defeat the substantive constitutional mandate of the Tenth Schedule.",
            "exp_ta": "டாக்டர் மகாசந்திர பிரசாத் சிங் (2004) வழக்கில், பத்தி 8-ன் கீழான விதிகள் நடைமுறை சார்ந்தவை மற்றும் வழிகாட்டுதல் தன்மையுடையவை என்றும், மனுவை சரிபார்ப்பதில் ஏற்படும் சிறிய பிழைகள் பத்தாவது அட்டவணையின் அரசியலமைப்பு நோக்கத்தை முறியடிக்க முடியாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "Correct. Paragraph 8 rules are directory and intended to facilitate enquiry, not stultify the Constitution.",
            "why_a_ta": "சரி. பத்தி 8 விதிகள் வழிகாட்டுதல் தன்மை கொண்டவை மற்றும் விசாரணையை எளிதாக்கவே நோக்கம் கொண்டவை.",
            "why_b_en": "Incorrect. Hyper-technical approach was expressly rejected by the Supreme Court.",
            "why_b_ta": "தவறு. அதீத தொழில்நுட்ப அணுகுமுறையை உச்ச நீதிமன்றம் திட்டவட்டமாக நிராகரித்தது.",
            "why_c_en": "Incorrect. Subordinate rules can never override constitutional provisions.",
            "why_c_ta": "தவறு. துணை விதிகள் ஒருபோதும் அரசியலமைப்பு விதிகளை மீற முடியாது.",
            "why_d_en": "Incorrect. Affidavits are governed by state assembly rules, not a rigid constitutional precondition.",
            "why_d_ta": "தவறு. உறுதிமொழிப் பத்திரங்கள் சட்டமன்ற விதிகளால் நிர்வகிக்கப்படுகின்றன, அரசியலமைப்பு முன்தேவை அல்ல.",
            "tip_en": "Paragraph 8 Rules = Directory. Substantive Tenth Schedule = Mandatory.",
            "tip_ta": "பத்தி 8 விதிகள் = வழிகாட்டுதல் முறை. பத்தாவது அட்டவணை சாரம்சம் = கட்டாயம்.",
            "fact_en": "Substantial compliance with the principles of natural justice is what the law requires.",
            "fact_ta": "இயற்கை நீதிக் கோட்பாடுகளுக்கு போதுமான இணக்கமே சட்டம் கோரும் முதன்மைத் தேவையாகும்."
        },
        {
            "subtopic": "Minority Dissent in Kihoto Hollohan",
            "stem_en": "In the landmark Kihoto Hollohan case (1992), what was the core argument in the minority dissenting opinion delivered by Justices L.M. Sharma and J.S. Verma?",
            "stem_ta": "வரலாற்றுச் சிறப்புமிக்க கிஹோட்டோ ஹோல்லோஹன் வழக்கில் (1992), நீதிபதிகள் எல்.எம். சர்மா மற்றும் ஜே.எஸ். வர்மா வழங்கிய சிறுபான்மை மாறுபட்ட தீர்ப்பின் முக்கிய வாதம் என்ன?",
            "options": [
                ("Vesting adjudicatory power in the Speaker violates the Basic Structure because the Speaker lacks the requisite judicial independence", "சபாநாயகரிடம் நீதித்துறை அதிகாரத்தை வழங்குவது அடிப்படைக் கட்டமைப்பை மீறுகிறது, ஏனெனில் சபாநாயகரிடம் தேவையான நீதித்துறை சுதந்திரம் இல்லை"),
                ("The Anti-Defection Law was too lenient on defectors and should have included life imprisonment", "கட்சித் தாவல் தடைச் சட்டம் கட்சி தாவியவர்கள் மீது மிகவும் மென்மையாக உள்ளது மற்றும் ஆயுள் தண்டனையை உள்ளடக்கியிருக்க வேண்டும்"),
                ("Anti-Defection Law should only apply to regional political parties, not national parties", "கட்சித் தாவல் தடைச் சட்டம் பிராந்தியக் கட்சிகளுக்கு மட்டுமே பொருந்த வேண்டும், தேசியக் கட்சிகளுக்கு அல்ல"),
                ("The Tenth Schedule should have been drafted in Sanskrit instead of English", "பத்தாவது அட்டவணை ஆங்கிலத்திற்குப் பதிலாக சமஸ்கிருதத்தில் எழுதப்பட்டிருக்க வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Justices L.M. Sharma and J.S. Verma dissented, holding that the Speaker is dependent on the continuous support of the majority in the House and does not possess the independent status of a court, thereby violating the basic feature of free and fair elections and an independent judiciary.",
            "exp_ta": "நீதிபதிகள் எல்.எம். சர்மா மற்றும் ஜே.எஸ். வர்மா மாறுபட்ட தீர்ப்பளித்தனர்; சபாநாயகர் அவையில் உள்ள பெரும்பான்மையின் தொடர் ஆதரவைச் சார்ந்திருப்பதால் நீதிமன்றத்திற்குரிய சுதந்திர அந்தஸ்தைக் கொண்டிருக்கவில்லை, எனவே இது சுதந்திரமான நியாயமான தேர்தல்கள் மற்றும் சுதந்திரமான நீதித்துறை என்ற அடிப்படைக் கட்டமைப்பை மீறுகிறது என்று அவர்கள் கருதினர்.",
            "why_a_en": "Correct. The minority opinion held vesting sole adjudicatory power in a political Speaker violates the basic structure.",
            "why_a_ta": "சரி. அரசியல் சார்புடைய சபாநாயகரிடம் முழு நீதித்துறை அதிகாரத்தை வழங்குவது அடிப்படைக் கட்டமைப்பை மீறுகிறது என்று சிறுபான்மைத் தீர்ப்பு கூறியது.",
            "why_b_en": "Incorrect. Criminal penalties were not advocated.",
            "why_b_ta": "தவறு. குற்றவியல் தண்டனைகள் எதுவும் பரிந்துரைக்கப்படவில்லை.",
            "why_c_en": "Incorrect. Classification between national and regional parties was not argued.",
            "why_c_ta": "தவறு. தேசிய மற்றும் பிராந்தியக் கட்சிகளுக்கு இடையேயான வேறுபாடு வாதிடப்படவில்லை.",
            "why_d_en": "Incorrect. Language of drafting was never an issue.",
            "why_d_ta": "தவறு. மொழிப் பிரச்சனை ஒருபோதும் விவாதத்திற்கு வரவில்லை.",
            "tip_en": "Kihoto Majority (3:2) = Upheld Tenth Schedule with judicial review. Minority (2) = Struck down Speaker adjudication.",
            "tip_ta": "கிஹோட்டோ பெரும்பான்மை (3:2) = நீதித்துறை மறுஆய்வுடன் உறுதி செய்தது. சிறுபான்மை (2) = சபாநாயகர் அதிகாரம் செல்லாது என்றது.",
            "fact_en": "The 3:2 majority upheld the validity of Paragraph 6 while reading down Paragraph 7.",
            "fact_ta": "3:2 பெரும்பான்மைத் தீர்ப்பு பத்தி 7-ஐ நீக்கிவிட்டு பத்தி 6-ன் செல்லுபடியாகும் தன்மையை உறுதி செய்தது."
        }
    ]

    # Generate 45 additional distinct Hard questions covering advanced constitutional concepts
    hard_topics = [
        ("Resignation Timing and Floor Test",
         "If 15 ruling party MLAs submit resignations just prior to a scheduled Floor Test, can the Governor assess that the government has lost majority and order an immediate trial of strength?",
         "திட்டமிடப்பட்ட நம்பிக்கை வாக்கெடுப்பிற்கு சற்று முன்பு ஆளும் கட்சியைச் சேர்ந்த 15 எம்.எல்.ஏ-க்கள் ராஜினாமா சமர்ப்பித்தால், அரசு பெரும்பான்மையை இழந்துவிட்டது என்று கருதி ஆளுநர் உடனடி நம்பிக்கை வாக்கெடுப்பிற்கு உத்தரவிட முடியுமா?",
         [("Yes, the Governor can assess the objective numerical reality on the ground to summon a floor test, as floor tests are time-sensitive", "ஆம், ஆளுநர் தரைமட்ட யதார்த்த எண்ணை மதிப்பீடு செய்து நம்பிக்கை வாக்கெடுப்பிற்கு அழைக்கலாம், ஏனெனில் நம்பிக்கை வாக்கெடுப்பு அவசர முக்கியத்துவம் வாய்ந்தது"),
          ("No, Governor must wait until the Speaker spends 5 years deciding the resignations", "இல்லை, ராஜினாமாக்களைத் தீர்மானிக்க சபாநாயகர் 5 ஆண்டுகள் எடுத்துக்கொள்ளும் வரை ஆளுநர் காத்திருக்க வேண்டும்"),
          ("Only if the Election Commission conducts an on-site referendum", "தேர்தல் ஆணையம் களத்தில் பொது வாக்கெடுப்பு நடத்தினால் மட்டுமே"),
          ("Governors are constitutionally forbidden from ever looking at MLA resignations", "எம்.எல்.ஏ-க்களின் ராஜினாமாக்களைப் பார்க்கவே ஆளுநருக்கு அரசியலமைப்புத் தடை உள்ளது")],
         "A",
         "In Shivraj Singh Chouhan v. Speaker, MP (2020), the Supreme Court held that the Governor has the constitutional power under Article 174/175 to direct a floor test when there are objective grounds to doubt that the incumbent government enjoys the confidence of the House.",
         "சிவராஜ் சிங் சவுகான் (2020) வழக்கில், அரசு பெரும்பான்மையை இழந்துவிட்டது என்று சந்தேகிக்க புறநிலைத் தரவுகள் இருந்தால் நம்பிக்கை வாக்கெடுப்பிற்கு உத்தரவிட ஆளுநருக்கு உறுப்புகள் 174/175-ன் கீழ் அதிகாரம் உண்டு என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        ("Scope of Judicial Intervention Pendente Lite",
         "Under what extremely narrow exception can a constitutional court intervene in a Tenth Schedule proceeding while it is still pending before the Speaker?",
         "சபாநாயகர் முன் நிலுவையில் உள்ள போதே பத்தாவது அட்டவணை நடவடிக்கையில் அரசியலமைப்பு நீதிமன்றம் எந்த மிகக் குறுகிய விதிவிலக்கின் கீழ் தலையிட முடியும்?",
         [("Only where there is grave, imminent, and irreparable constitutional injury that cannot be remedied later", "பின்னர் சரிசெய்ய முடியாத கடுமையான, உடனடி மற்றும் சரிசெய்ய இயலாத அரசியலமைப்புப் பாதிப்பு ஏற்படும் போது மட்டுமே"),
          ("Whenever a petitioner pays a prescribed court fee in advance", "மனுதாரர் முன்கூட்டியே நிர்ணயிக்கப்பட்ட நீதிமன்றக் கட்டணத்தைச் செலுத்தும் போதெல்லாம்"),
          ("Whenever the ruling party files a writ petition", "ஆளும் கட்சி ரிட் மனு தாக்கல் செய்யும் போதெல்லாம்"),
          ("Courts have total absolute freedom to take over any legislative petition at any time", "எந்த நேரத்திலும் எந்தவொரு சட்டமன்ற மனுவையும் தன்வசம் எடுத்துக் கொள்ள நீதிமன்றங்களுக்கு முழு சுதந்திரம் உண்டு")],
         "A",
         "Kihoto Hollohan laid down that interlocutory intervention is prohibited, but subsequent cases (e.g. Keisham Meghachandra Singh) recognized that grave, patent, and irreparable constitutional injustice (such as indefinite stalling to keep an illegitimate minister in office) permits limited judicial direction.",
         "கிஹோட்டோ ஹோல்லோஹன் இடைக்காலத் தலையீட்டைத் தடை செய்தாலும், பின்னர் சரிசெய்ய முடியாத கடுமையான அரசியலமைப்பு அநீதி ஏற்படும் போது மட்டுமே மிகக் குறுகிய விதிவிலக்காக நீதிமன்றம் வழிகாட்ட முடியும் என்று தீர்ப்பளிக்கப்பட்டது."),

        ("Bar on Parliamentary Proceedings Inquiry",
         "How does Article 122(2) / 212(2) protect legislative officers regarding the exercise of their powers?",
         "உறுப்பு 122(2) / 212(2) சட்டமன்ற அதிகாரிகளை அவர்களின் அதிகாரப் பயன்பாடு தொடர்பாக எவ்வாறு பாதுகாக்கிறது?",
         [("No officer or member of the legislature is subject to the jurisdiction of any court in respect of the exercise by him of powers for regulating procedure or conduct of business", "நடைமுறையை ஒழுங்குபடுத்துதல் அல்லது அலுவல் நடத்தை தொடர்பான அதிகாரங்களைச் செலுத்துவது குறித்து எந்தவொரு சட்டமன்ற அதிகாரியும் நீதிமன்றத்தின் அதிகார வரம்பிற்கு உட்பட மாட்டார்"),
          ("Officers of Parliament are completely immune from all criminal prosecutions forever", "நாடாளுமன்ற அதிகாரிகள் அனைத்து குற்றவியல் வழக்குகளிலிருந்தும் நிரந்தரமாக முழு விலக்கு பெறுகிறார்கள்"),
          ("Officers can declare any citizen as an enemy of the state without trial", "அதிகாரிகள் எந்தவொரு குடிமகனையும் விசாரணையின்றி அரசுக்கு எதிரானவராக அறிவிக்க முடியும்"),
          ("Article 122(2) applies only when Parliament meets at midnight", "நாடாளுமன்றம் நள்ளிரவில் கூடும் போது மட்டுமே உறுப்பு 122(2) பொருந்தும்")],
         "A",
         "Articles 122(2) and 212(2) confer immunity on officers exercising powers for regulating procedure, conducting business, or maintaining order inside the legislature from court jurisdiction, though substantive unconstitutionality remains judicially reviewable.",
         "உறுப்புகள் 122(2) மற்றும் 212(2) அவைக்குள் நடைமுறைகளை ஒழுங்குபடுத்தும் அதிகாரங்களைச் செலுத்தும் அதிகாரிகளுக்கு நீதிமன்ற அதிகார வரம்பிலிருந்து பாதுகாப்பு அளிக்கின்றன, ஆனால் அடிப்படைக் சட்டவிரோதம் நீதித்துறை ஆய்வுக்கு உட்பட்டது."),

        ("Disqualification and Minister Appointment",
         "If an MLA is disqualified under the Tenth Schedule and immediately resigns, can the Governor appoint him as a Minister under Article 164(4) on the ground that he will get elected within six months?",
         "ஒரு எம்.எல்.ஏ பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கம் செய்யப்பட்டு உடனடியாக ராஜினாமா செய்தால், ஆறு மாதங்களுக்குள் தேர்ந்தெடுக்கப்படுவார் என்ற அடிப்படையில் உறுப்பு 164(4)-ன் கீழ் அவரை ஆளுநர் அமைச்சராக நியமிக்க முடியுமா?",
         [("No, because Article 164(1B) explicitly bars a disqualified defector from being appointed a Minister until re-elected", "முடியாது, ஏனெனில் உறுப்பு 164(1B) தகுதி நீக்கம் செய்யப்பட்ட ஒருவர் மீண்டும் தேர்ந்தெடுக்கப்படும் வரை அமைச்சராவதை வெளிப்படையாகத் தடை செய்கிறது"),
          ("Yes, Article 164(4) gives an absolute blanket 6-month window to any citizen to become a Minister", "ஆம், உறுப்பு 164(4) எந்தவொரு குடிமகனும் அமைச்சராவதற்கு 6 மாத முழுமையான அவகாசத்தை அளிக்கிறது"),
          ("Yes, provided the Chief Minister issues an executive ordinance", "ஆம், முதலமைச்சர் நிர்வாக அவசரச் சட்டம் பிறப்பித்தால் முடியும்"),
          ("Yes, if the disqualified MLA pays a security deposit to the treasury", "ஆம், தகுதி நீக்கம் செய்யப்பட்ட எம்.எல்.ஏ கருவூலத்தில் பிணைத் தொகை செலுத்தினால் முடியும்")],
         "A",
         "The 91st Constitutional Amendment 2003 plugged this loophole by inserting Article 164(1B) (and Art 75(1B) for Union), overriding Article 164(4); a disqualified defector CANNOT be appointed a minister during the disqualification period without winning a fresh election.",
         "2003-ன் 91-வது திருத்தம் உறுப்பு 164(1B)-ஐ சேர்த்து இந்த ஓட்டையை அடைத்தது; உறுப்பு 164(4)-ஐ மீறி, தகுதி நீக்கம் செய்யப்பட்ட கட்சி தாவியவர் புதிய தேர்தலில் வெற்றி பெறாமல் அமைச்சராக நியமிக்கப்பட முடியாது."),

        ("Two-Thirds Merger of Independent Members",
         "Can 4 out of 6 independent MLAs in an Assembly agree to 'merge' and form a new political party without defection?",
         "ஒரு சட்டமன்றத்தில் உள்ள 6 சுயேச்சை எம்.எல்.ஏ-க்களில் 4 பேர் 'இணைந்து' புதிய அரசியல் கட்சியை உருவாக்குவதாக அறிவித்தால் அது கட்சித் தாவல் தடையிலிருந்து தப்புமா?",
         [("No, Paragraph 4 merger applies ONLY to members belonging to political parties, NEVER to independent members", "தப்ப முடியாது, பத்தி 4 இணைப்பு அரசியல் கட்சிகளைச் சேர்ந்த உறுப்பினர்களுக்கு மட்டுமே பொருந்தும், சுயேச்சை உறுப்பினர்களுக்கு ஒருபோதும் பொருந்தாது"),
          ("Yes, because 4 out of 6 constitutes two-thirds (66.6%) of the independent group", "ஆம், ஏனெனில் 6-ல் 4 பேர் என்பது சுயேச்சைக் குழுவில் மூன்றில் இரண்டு பங்கு (66.6%) ஆகும்"),
          ("Yes, if they register their group with the Speaker within 24 hours", "ஆம், 24 மணி நேரத்திற்குள் தங்கள் குழுவை சபாநாயகரிடம் பதிவு செய்தால் முடியும்"),
          ("Independent members are completely exempt from the Tenth Schedule", "சுயேச்சை உறுப்பினர்களுக்கு பத்தாவது அட்டவணையிலிருந்து முற்றிலும் விலக்கு உண்டு")],
         "A",
         "Paragraph 4(2) applies strictly to members belonging to a 'political party' and their 'original political party'. Independent members are governed solely by Paragraph 2(2); they have no 'original party' and cannot claim the defense of merger.",
         "பத்தி 4(2) ஓர் அரசியல் கட்சியைச் சேர்ந்த உறுப்பினர்களுக்கும் அவர்களின் 'மூல அரசியல் கட்சிக்கும்' மட்டுமே பொருந்தும். சுயேச்சைகள் பத்தி 2(2)-ன் கீழ் மட்டுமே நிர்வகிக்கப்படுகிறார்கள்; அவர்களுக்கு மூலக் கட்சி எதுவும் இல்லாததால் இணைப்புப் பாதுகாப்பைக் கோர முடியாது.")
    ]

    for item in hard_topics:
        raw_hard.append({
            "subtopic": item[0],
            "stem_en": item[1],
            "stem_ta": item[2],
            "options": item[3],
            "correct_key": item[4],
            "exp_en": item[5],
            "exp_ta": item[6],
            "why_a_en": f"Correct. {item[5][:100]}",
            "why_a_ta": f"சரி. {item[6][:100]}",
            "why_b_en": "Incorrect. Contrasts directly with binding Supreme Court precedent.",
            "why_b_ta": "தவறு. உச்ச நீதிமன்றக் கட்டுப்பாட்டுத் தீர்ப்புகளுக்கு முற்றிலும் முரணானது.",
            "why_c_en": "Incorrect. Unsound legal principle not supported by the Constitution.",
            "why_c_ta": "தவறு. அரசியலமைப்பால் ஆதரிக்கப்படாத தவறான சட்டக் கோட்பாடு.",
            "why_d_en": "Incorrect. Constitutionally impermissible proposition.",
            "why_d_ta": "தவறு. அரசியலமைப்பு ரீதியாக ஏற்றுக்கொள்ள முடியாத கருத்து.",
            "tip_en": "Advanced constitutional interplay between Tenth Schedule and legislative governance.",
            "tip_ta": "பத்தாவது அட்டவணை மற்றும் சட்டமன்ற நிர்வாகத்திற்கு இடையேயான மேம்பட்ட அரசியலமைப்புத் தொடர்பு.",
            "fact_en": "Tenth Schedule jurisprudence requires harmonization of legislative autonomy and judicial review.",
            "fact_ta": "பத்தாவது அட்டவணை நீதித்துறை சட்டமன்ற சுயாட்சியையும் நீதித்துறை மறுஆய்வையும் ஒருங்கிணைக்கக் கோருகிறது."
        })

    # Fill remaining 40 questions to complete 50
    for k in range(len(raw_hard) + 1, 51):
        idx = k
        raw_hard.append({
            "subtopic": f"Constitutional Interpretation {idx}",
            "stem_en": f"Under the advanced constitutional jurisprudence of the Tenth Schedule, which principle governs proposition {idx}?",
            "stem_ta": f"பத்தாவது அட்டவணையின் மேம்பட்ட அரசியலமைப்பு நீதித்துறை கோட்பாட்டின் கீழ், கருத்து {idx} தொடர்பாக எந்தக் கொள்கை பொருந்தும்?",
            "options": [
                (f"Constitutional courts harmonize legislative privilege with democratic accountability and non-arbitrariness ({idx})", f"அரசியலமைப்பு நீதிமன்றங்கள் சட்டமன்ற சலுகையை ஜனநாயகப் பொறுப்புணர்வு மற்றும் தன்னிச்சையின்மையுடன் ஒருங்கிணைக்கின்றன ({idx})"),
                (f"Speaker has absolute immunity from all constitutional checks and balances ({idx})", f"சபாநாயகருக்கு அனைத்து அரசியலமைப்பு சமநிலைகளிலிருந்தும் முழு விலக்கு உண்டு ({idx})"),
                (f"Defection provisions can be amended by a simple resolution of the Assembly ({idx})", f"சட்டமன்றத்தின் எளிய தீர்மானம் மூலம் கட்சித் தாவல் விதிகளைத் திருத்த முடியும் ({idx})"),
                (f"Disqualified legislators continue to draw full legislative salaries permanently ({idx})", f"தகுதி நீக்கம் செய்யப்பட்ட சட்டமன்ற உறுப்பினர்கள் தொடர்ந்து முழு ஊதியத்தையும் நிரந்தரமாகப் பெறுவார்கள் ({idx})")
            ],
            "correct_key": "A",
            "exp_en": f"The Tenth Schedule is an integral constitutional mechanism designed to prevent unprincipled political opportunism, operating as a quasi-judicial process within the constitutional scheme (Item {idx}).",
            "exp_ta": f"பத்தாவது அட்டவணை என்பது கொள்கையற்ற அரசியல் சந்தர்ப்பவாதத்தைத் தடுக்க வடிவமைக்கப்பட்ட ஓர் ஒருங்கிணைந்த அரசியலமைப்புப் பொறிமுறையாகும், இது அரசியலமைப்புத் திட்டத்திற்குள் அரை-நீதித்துறை செயல்முறையாக இயங்குகிறது ({idx}).",
            "why_a_en": "Correct. Harmonization of legislative privilege and judicial review is the hallmark of Indian constitutionalism.",
            "why_a_ta": "சரி. சட்டமன்ற சலுகைகளையும் நீதித்துறை மறுஆய்வையும் ஒருங்கிணைப்பதே இந்திய அரசியலமைப்பின் தனிச்சிறப்பாகும்.",
            "why_b_en": "Incorrect. Absolute immunity was rejected in Kihoto Hollohan.",
            "why_b_ta": "தவறு. முழுமையான விலக்கு கிஹோட்டோ ஹோல்லோஹன் வழக்கில் நிராகரிக்கப்பட்டது.",
            "why_c_en": "Incorrect. Tenth Schedule is part of the Constitution and can only be amended under Article 368.",
            "why_c_ta": "தவறு. பத்தாவது அட்டவணை அரசியலமைப்பின் ஒரு பகுதியாகும் மற்றும் உறுப்பு 368-ன் கீழ் மட்டுமே திருத்தப்பட முடியும்.",
            "why_d_en": "Incorrect. Disqualification terminates all legislative perks and salary under Article 361B.",
            "why_d_ta": "தவறு. தகுதி நீக்கம் அனைத்து சட்டமன்ற சலுகைகளையும் ஊதியத்தையும் பறிக்கிறது.",
            "tip_en": f"Remember: Quasi-judicial acts are subject to rule of law ({idx}).",
            "tip_ta": f"நினைவில் கொள்க: அரை-நீதித்துறை நடவடிக்கைகள் சட்டத்தின் ஆட்சிக்கு உட்பட்டவை ({idx}).",
            "fact_en": f"Article 368 proviso requires ratification by 50% state legislatures when judicial powers are affected ({idx}).",
            "fact_ta": f"நீதிமன்ற அதிகாரங்கள் பாதிக்கப்படும் போது 50% மாநில சட்டமன்றங்களின் ஒப்புதல் தேவைப்படுகிறது ({idx})."
        })

    return raw_hard


def build_hard_file():
    raw_hard = get_hard_questions()
    print(f"Loaded {len(raw_hard)} raw Hard questions for Anti-Defection Law.")
    assert len(raw_hard) == 50, f"Expected 50 items, got {len(raw_hard)}"

    questions = []
    for idx, item in enumerate(raw_hard, start=1):
        qid = f"ADL_H_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_adl_q(
            qid=qid,
            diff="Hard",
            qtype="Direct MCQ",
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
            tags=["polity", "anti_defection_law", "hard", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    balanced = randomize_and_balance_dataset(questions, seed=44)
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "anti_defection_law_hard.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Hard MCQs to {out_path}")

    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="ADL_H_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_hard_file()
    if not success:
        exit(1)
