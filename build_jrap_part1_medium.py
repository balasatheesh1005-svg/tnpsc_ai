# -*- coding: utf-8 -*-
"""
Build Judicial Review, Activism & PIL - Part 1 Medium (50 MCQs)
Identifier: JRAP_M_001 to JRAP_M_050
Key Distribution: A: 13, B: 12, C: 13, D: 12 (Total: 50)
Anti-Block: Max consecutive run <= 2
"""
import json
import os
from collections import Counter
from judicial_review_mcq_helper import make_jrap_q

def build_medium_mcqs():
    questions = []

    medium_data = [
        # 1 - A
        ("JRAP_M_001", "Scope of Judicial Review",
         "Which of the following constitutional provisions explicitly defines the scope of 'Law' subject to Fundamental Rights under Article 13?",
         "பின்வரும் எந்த அரசியலமைப்பு விதி உறுப்பு 13-ன் கீழ் அடிப்படை உரிமைகளுக்கு உட்பட்ட 'சட்டம்' என்பதன் வரம்பை வெளிப்படையாக வரையறுக்கிறது?",
         "Article 13(3)(a)", "உறுப்பு 13(3)(a)",
         "Article 13(1)", "உறுப்பு 13(1)",
         "Article 13(2)", "உறுப்பு 13(2)",
         "Article 13(4)", "உறுப்பு 13(4)", "A",
         "Article 13(3)(a) defines 'law' to include any Ordinance, order, bye-law, rule, regulation, notification, custom or usage having in the territory of India the force of law.",
         "உறுப்பு 13(3)(a) 'சட்டம்' என்பதை அவசரச்சட்டம், உத்தரவு, துணைச்சட்டம், விதி, நெறிமுறை, அறிவிக்கை, வழக்கம் ஆகியவற்றை உள்ளடக்கியதாக வரையறுக்கிறது."),

        # 2 - C
        ("JRAP_M_002", "Constitutional Amendment as Law",
         "In which case did the Supreme Court hold for the first time that a Constitutional Amendment is 'Law' within the meaning of Article 13(2) and cannot abridge Fundamental Rights?",
         "எந்த வழக்கில் உச்ச நீதிமன்றம் முதன்முதலில் ஓர் அரசியலமைப்புத் திருத்தம் உறுப்பு 13(2)-ன் பொருளில் 'சட்டம்' ஆகும் என்றும் அது அடிப்படை உரிமைகளைக் குறைக்க முடியாது என்றும் தீர்ப்பளித்தது?",
         "Shankari Prasad (1951)", "சங்கரி பிரசாத் (1951)",
         "Sajjan Singh (1965)", "சஜ்ஜன் சிங் (1965)",
         "I.C. Golaknath v. State of Punjab (1967)", "ஐ.சி. கோலக்நாத் v. பஞ்சாப் மாநிலம் (1967)",
         "Kesavananda Bharati (1973)", "கேசவாநந்த பாரதி (1973)", "C",
         "In Golaknath (1967), an 11-judge bench by a 6:5 majority ruled that an amendment under Art. 368 is an ordinary 'law' under Art. 13(2), thereby overruling Shankari Prasad and Sajjan Singh.",
         "கோலக்நாத் (1967) வழக்கில் 11 நீதிபதிகள் அமர்வு 6:5 பெரும்பான்மையில் உறுப்பு 368-ன் கீழ் வரும் திருத்தம் உறுப்பு 13(2)-ன் கீழ் 'சட்டம்' ஆகும் எனத் தீர்ப்பளித்தது."),

        # 3 - B
        ("JRAP_M_003", "Article 13(4) Insertion",
         "Which Constitutional Amendment Act inserted clause (4) in Article 13 to state that 'Nothing in this article shall apply to any amendment of this Constitution made under article 368'?",
         "எந்த அரசியலமைப்புத் திருத்தச் சட்டம் 'உறுப்பு 368-ன் கீழ் செய்யப்படும் எந்தவொரு திருத்தத்திற்கும் இவ்வுறுப்பில் உள்ள எதுவும் பொருந்தாது' என்று உறுப்பு 13-ல் உட்பிரிவு (4)-ஐ சேர்த்தது?",
         "42nd Amendment Act 1976", "42வது திருத்தச் சட்டம் 1976",
         "24th Amendment Act 1971", "24வது திருத்தச் சட்டம் 1971",
         "25th Amendment Act 1971", "25வது திருத்தச் சட்டம் 1971",
         "44th Amendment Act 1978", "44வது திருத்தச் சட்டம் 1978", "B",
         "The 24th Amendment Act 1971 was passed by Parliament to nullify the effect of the Golaknath judgment by inserting Article 13(4) and amending Article 368.",
         "கோலக்நாத் தீர்ப்பின் விளைவை ரத்து செய்வதற்காக 1971-ல் 24வது திருத்தச் சட்டம் இயற்றப்பட்டு உறுப்பு 13(4) சேர்க்கப்பட்டது மற்றும் உறுப்பு 368 திருத்தப்பட்டது."),

        # 4 - D
        ("JRAP_M_004", "Prospective Overruling",
         "The legal doctrine of 'Prospective Overruling' was introduced into Indian constitutional jurisprudence in which landmark case?",
         "'எதிர்கால நோக்குடைய ரத்து செய்தல்' (Prospective Overruling) என்ற சட்டக் கோட்பாடு எந்த வரலாற்று வழக்கில் இந்திய அரசியலமைப்புச் சட்டத்தில் அறிமுகப்படுத்தப்பட்டது?",
         "A.K. Gopalan Case (1950)", "ஏ.கே. கோபாலன் வழக்கு (1950)",
         "Kesavananda Bharati Case (1973)", "கேசவாநந்த பாரதி வழக்கு (1973)",
         "Minerva Mills Case (1980)", "மினர்வா மில்ஸ் வழக்கு (1980)",
         "I.C. Golaknath v. State of Punjab (1967)", "ஐ.சி. கோலக்நாத் v. பஞ்சாப் மாநிலம் (1967)", "D",
         "Chief Justice K. Subba Rao in Golaknath (1967) applied the American doctrine of 'Prospective Overruling', clarifying that the ruling would apply only to future amendments and not invalidate past ones.",
         "தலைமை நீதிபதி சுப்பா ராவ் கோலக்நாத் (1967) வழக்கில் அமெரிக்கக் கோட்பாடான 'எதிர்கால நோக்குடைய ரத்து செய்தல்' கொள்கையைப் புகுத்தினார்."),

        # 5 - A
        ("JRAP_M_005", "Article 32 vs Article 226 Discretion",
         "Why is the writ jurisdiction under Article 226 considered wider than the writ jurisdiction under Article 32?",
         "உறுப்பு 32-ன் கீழ் உள்ள அதிகாரத்தை விட உறுப்பு 226-ன் கீழ் உள்ள நீதிப்பேராணை அதிகாரம் ஏன் பரந்ததாகக் கருதப்படுகிறது?",
         "Article 226 can be invoked for Fundamental Rights as well as ordinary legal rights ('for any other purpose')", "உறுப்பு 226 அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்ட உரிமைகளுக்காகவும் ('வேறு எந்த நோக்கத்திற்கும்') பயன்படுத்தப்படலாம்",
         "Article 226 decisions cannot be appealed to the Supreme Court", "உறுப்பு 226 தீர்ப்புகளுக்கு எதிராக உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்ய முடியாது",
         "Article 226 applies to foreign nationals only", "உறுப்பு 226 வெளிநாட்டுப் பிரஜைகளுக்கு மட்டுமே பொருந்தும்",
         "Article 226 is outside Part VI of the Constitution", "உறுப்பு 226 அரசியலமைப்பின் பகுதி VI-க்கு வெளியே உள்ளது", "A",
         "While Article 32 can be invoked ONLY for Fundamental Rights enforcement, Article 226 covers both Fundamental Rights and any other legal right.",
         "உறுப்பு 32 அடிப்படை உரிமைகளை அமல்படுத்துவதற்கு மட்டுமே பயன்படுத்தப்படும் நிலையில், உறுப்பு 226 அடிப்படை உரிமைகள் மற்றும் எந்தவொரு சட்ட உரிமைக்கும் பொருந்தும்."),

        # 6 - C
        ("JRAP_M_006", "Refusal of Writ Petition",
         "Can the Supreme Court refuse to exercise its writ jurisdiction under Article 32 if a Fundamental Right is clearly violated?",
         "அடிப்படை உரிமை தெளிவாக மீறப்பட்டிருக்கும் போது, உறுப்பு 32-ன் கீழ் தனது நீதிப்பேராணை அதிகாரத்தைச் செயல்படுத்த உச்ச நீதிமன்றம் மறுக்க முடியுமா?",
         "Yes, the Supreme Court has absolute discretion to refuse any writ petition", "ஆம், எந்தவொரு மனுவையும் நிராகரிக்க உச்ச நீதிமன்றத்திற்கு முழுமையான விவேக அதிகாரம் உண்டு",
         "Only if the President directs the Court not to hear it", "குடியரசுத் தலைவர் விசாரிக்க வேண்டாம் என உத்தரவிட்டால் மட்டுமே",
         "No, because Article 32 is itself a Fundamental Right and the Supreme Court is the guarantor of FRs", "இல்லை, ஏனெனில் உறுப்பு 32 தானே ஓர் அடிப்படை உரிமை மற்றும் உச்ச நீதிமன்றமே அடிப்படை உரிமைகளின் உத்தரவாததாரர்",
         "Yes, if the petitioner has not approached the District Court first", "ஆம், மனுதாரர் முதலில் மாவட்ட நீதிமன்றத்தை அணுகவில்லை என்றால் மறுக்கலாம்", "C",
         "In Romesh Thappar (1950), SC ruled that Article 32 is a guaranteed right, making the Supreme Court the protector and guarantor of Fundamental Rights; it cannot refuse relief.",
         "ரமேஷ் தப்பார் (1950) வழக்கில் உச்ச நீதிமன்றம் உறுப்பு 32 உத்தரவாதம் அளிக்கப்பட்ட உரிமை என்பதால் நிவாரணம் வழங்க மறுக்க முடியாது எனத் தீர்ப்பளித்தது."),

        # 7 - B
        ("JRAP_M_007", "Article 226 Discretionary Remedy",
         "Unlike Article 32, a remedy under Article 226 of the Constitution before the High Court is:",
         "உறுப்பு 32 போலன்றி, உயர் நீதிமன்றத்தின் முன் அரசியலமைப்பு உறுப்பு 226-ன் கீழ் உள்ள பரிகாரம் என்பது:",
         "A mandatory fundamental right of the citizen", "குடிமகனின் கட்டாய அடிப்படை உரிமை",
         "A discretionary equitable remedy", "ஒரு விவேகத்திற்குட்பட்ட சமத்துவப் பரிகாரம் (Discretionary Remedy)",
         "An unconstitutional power", "அரசியலமைப்புக்கு முரணான ஓர் அதிகாரம்",
         "Subject to approval by the State Governor", "மாநில ஆளுநரின் ஒப்புதலுக்கு உட்பட்டது", "B",
         "A High Court may refuse relief under Article 226 on grounds such as delay/laches, availability of an adequate alternative remedy, or suppression of material facts.",
         "காலதாமதம், மாற்றுப் பரிகாரம் இருத்தல் அல்லது உண்மைகளை மறைத்தல் போன்ற காரணங்களுக்காக உறுப்பு 226-ன் கீழ் நிவாரணத்தை உயர் நீதிமன்றம் மறுக்கலாம்."),

        # 8 - D
        ("JRAP_M_008", "Writ of Prohibition Target",
         "Against which of the following authorities can the writ of Prohibition NOT be issued?",
         "பின்வரும் எந்த அதிகாரிகளுக்கு எதிராக தடையுறுத்தும் நீதிப்பேராணையை (Prohibition) வெளியிட முடியாது?",
         "Subordinate Judicial Courts", "சார்நிலை நீதித்துறை நீதிமன்றங்கள்",
         "Quasi-judicial Tribunals", "அரை-நீதித்துறை தீர்ப்பாயங்கள்",
         "Arbitrators exercising statutory judicial functions", "சட்டரீதியான நீதித்துறை பணிகளைச் செய்யும் மத்தியஸ்தர்கள்",
         "Administrative authorities, legislative bodies, and private individuals", "நிர்வாக அதிகாரிகள், சட்டமன்ற அமைப்புகள் மற்றும் தனிநபர்கள்", "D",
         "The writ of Prohibition lies only against judicial and quasi-judicial authorities to prevent excess of jurisdiction; it is not available against administrative, legislative, or private bodies.",
         "தடையுறுத்தும் பேராணை நீதித்துறை மற்றும் அரை-நீதித்துறை அமைப்புகளுக்கு எதிராக மட்டுமே வரம்பு மீறலைத் தடுக்க வெளியிடப்படும்; நிர்வாக, சட்டமன்ற அல்லது தனியார் அமைப்புகளுக்கு எதிராக வராது."),

        # 9 - A
        ("JRAP_M_009", "Certiorari Against Administrative Authorities",
         "Prior to 1991, Certiorari was issued only against judicial and quasi-judicial bodies. Which landmark Supreme Court judgment expanded Certiorari against administrative authorities affecting rights?",
         "1991-க்கு முன்னர் வரை செர்சியோராரி நீதி மற்றும் அரை-நீதி அமைப்புகளுக்கு மட்டுமே பிறப்பிக்கப்பட்டது. உரிமைகளைப் பாதிக்கும் நிர்வாக அதிகாரிகளுக்கு எதிராகவும் செர்சியோராரியை விரிவாக்கிய முக்கிய உச்ச நீதிமன்றத் தீர்ப்பு எது?",
         "Province of Bombay v. Khushaldas Advani (1950) & A.K. Kraipak (1969)", "பாம்பே மாகாணம் v. குஷால்தாஸ் அத்வானி (1950) & ஏ.கே. கிரைபக் (1969)",
         "Kesavananda Bharati Case (1973)", "கேசவாநந்த பாரதி வழக்கு (1973)",
         "Golaknath Case (1967)", "கோலக்நாத் வழக்கு (1967)",
         "Shankari Prasad Case (1951)", "சங்கரி பிரசாத் வழக்கு (1951)", "A",
         "In A.K. Kraipak (1969), the Supreme Court obliterated the rigid distinction between quasi-judicial and administrative inquiries, extending natural justice and certiorari to administrative actions.",
         "ஏ.கே. கிரைபக் (1969) வழக்கில் அரை-நீதி மற்றும் நிர்வாக விசாரணைகளுக்கு இடையேயான வேறுபாட்டை நீக்கி, நிர்வாக நடவடிக்கைகளுக்கும் இயற்கை நீதி மற்றும் செர்சியோராரியை உச்ச நீதிமன்றம் விரிவுபடுத்தியது."),

        # 10 - C
        ("JRAP_M_010", "Writ of Quo-Warranto Condition",
         "Which of the following is an indispensable legal condition for the issuance of the writ of Quo-Warranto?",
         "தகுதிமுறை வினவும் நீதிப்பேராணையை (Quo-Warranto) பிறப்பிப்பதற்கு பின்வருவனவற்றில் இன்றியமையாத சட்ட நிபந்தனை எது?",
         "The office must be created by a private commercial contract", "அப்பதவி ஒரு தனியார் வணிக ஒப்பந்தத்தால் உருவாக்கப்பட்டிருக்க வேண்டும்",
         "The petitioner must prove personal pecuniary loss", "மனுதாரர் தனிப்பட்ட பண இழப்பை நிரூபிக்க வேண்டும்",
         "The office must be a substantive public office of a permanent character created by statute or Constitution", "அப்பதவி சட்டம் அல்லது அரசியலமைப்பால் உருவாக்கப்பட்ட நிரந்தரத் தன்மை கொண்ட முக்கிய பொதுப் பதவியாக இருக்க வேண்டும்",
         "The holder must be a member of the Union Cabinet", "பதவி வகிப்பவர் மத்திய அமைச்சரவை உறுப்பினராக இருக்க வேண்டும்", "C",
         "Quo-Warranto lies only in respect of a substantive public office created by the Constitution or a statute, not for private or purely ministerial employment.",
         "குவோ-வாரண்டோ என்பது அரசியலமைப்பு அல்லது சட்டத்தால் உருவாக்கப்பட்ட முக்கியமான பொதுப் பதவிக்கு மட்டுமே பொருந்தும்; தனியார் அல்லது தற்காலிக ஊழியத்திற்குப் பொருந்தாது."),

        # 11 - B
        ("JRAP_M_011", "Article 227 vs Article 226 Nature",
         "What is the fundamental difference between the power of High Court under Article 226 and Article 227?",
         "உறுப்பு 226 மற்றும் உறுப்பு 227-ன் கீழ் உயர் நீதிமன்றத்தின் அதிகாரத்திற்கு இடையேயான அடிப்படை வேறுபாடு என்ன?",
         "Article 226 is administrative, while Article 227 is purely legislative", "உறுப்பு 226 நிர்வாக ரீதியானது, உறுப்பு 227 முற்றிலும் சட்டமன்ற ரீதியானது",
         "Article 226 is remedial writ power on petition, while Article 227 is supervisory superintendence (both judicial and administrative) which can be exercised suo motu", "உறுப்பு 226 மனுவின் மீதான நீதிப்பேராணைப் பரிகாரம்; உறுப்பு 227 தாமாக முன்வந்து செயல்படுத்தக்கூடிய மேற்பார்வை அதிகாரம் (நீதி மற்றும் நிர்வாகம் இரண்டும்)",
         "Article 227 applies only to High Court staff", "உறுப்பு 227 உயர் நீதிமன்ற ஊழியர்களுக்கு மட்டுமே பொருந்தும்",
         "Article 226 can be exercised only during national emergency", "உறுப்பு 226 தேசிய அவசரநிலையின் போது மட்டுமே செயல்படுத்தப்பட முடியும்", "B",
         "Article 227 confers supervisory superintendence (both administrative and judicial) over all subordinate courts and tribunals, which can be exercised suo motu, unlike Art. 226.",
         "உறுப்பு 227 அனைத்து சார்நிலை நீதிமன்றங்கள் மற்றும் தீர்ப்பாயங்கள் மீது மேற்பார்வை அதிகாரத்தை வழங்குகிறது; இது உறுப்பு 226 போலன்றி தாமாக முன்வந்தும் செயல்படுத்தப்படலாம்."),

        # 12 - D
        ("JRAP_M_012", "Armed Forces Tribunal Excluded from Art. 227",
         "Which courts or tribunals are explicitly excluded from the superintendence of High Courts under Article 227(4)?",
         "உறுப்பு 227(4)-ன் கீழ் உயர் நீதிமன்றங்களின் மேற்பார்வை அதிகாரத்திலிருந்து வெளிப்படையாக விலக்கப்பட்ட நீதிமன்றங்கள் அல்லது தீர்ப்பாயங்கள் எவை?",
         "Labour Courts and Industrial Tribunals", "தொழிலாளர் நீதிமன்றங்கள் மற்றும் தொழில் தீர்ப்பாயங்கள்",
         "Income Tax Appellate Tribunal", "வருமான வரி மேல்முறையீட்டுத் தீர்ப்பாயம்",
         "Central Administrative Tribunal (CAT)", "மத்திய நிர்வாகத் தீர்ப்பாயம் (CAT)",
         "Any court or tribunal constituted by or under any law relating to the Armed Forces", "ஆயுதப் படைகள் தொடர்பான சட்டத்தின் கீழ் அமைக்கப்பட்ட எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயம்", "D",
         "Article 227(4) explicitly provides: 'Nothing in this article shall be deemed to confer on a High Court powers of superintendence over any court or tribunal constituted by or under any law relating to the Armed Forces.'",
         "உறுப்பு 227(4) ஆயுதப் படைகள் தொடர்பான சட்டத்தின் கீழ் அமைக்கப்பட்ட எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்தின் மீதும் உயர் நீதிமன்றத்திற்கு மேற்பார்வை அதிகாரம் இல்லை எனத் தெளிவாகக் கூறுகிறது."),

        # 13 - A
        ("JRAP_M_013", "Article 131 Federal Disputes",
         "The exclusive original jurisdiction of the Supreme Court to decide legal disputes between the Government of India and one or more States is conferred by:",
         "இந்திய அரசுக்கும் ஒன்று அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கும் இடையிலான சட்டரீதியான சிக்கல்களைத் தீர்க்க உச்ச நீதிமன்றத்திற்கு வழங்கப்பட்டுள்ள பிரத்யேக அசல் அதிகார வரம்பு எது?",
         "Article 131", "உறுப்பு 131",
         "Article 132", "உறுப்பு 132",
         "Article 133", "உறுப்பு 133",
         "Article 134", "உறுப்பு 134", "A",
         "Article 131 confers exclusive original jurisdiction on the Supreme Court for federal disputes involving questions of legal right between the Union and States.",
         "உறுப்பு 131 மத்திய-மாநிலங்களுக்கு இடையே சட்ட உரிமை சம்பந்தப்பட்ட கூட்டாட்சிச் சிக்கல்களில் உச்ச நீதிமன்றத்திற்கு பிரத்யேக அசல் அதிகார வரம்பை வழங்குகிறது."),

        # 14 - C
        ("JRAP_M_014", "Article 131 Limitation",
         "Which category of dispute is expressly excluded from the Supreme Court's original jurisdiction under the proviso to Article 131?",
         "உறுப்பு 131-ன் வரம்பு நிபந்தனையின் கீழ் உச்ச நீதிமன்றத்தின் அசல் அதிகார வரம்பிலிருந்து வெளிப்படையாக விலக்கப்பட்ட தகராறு வகை எது?",
         "Boundary disputes between States", "மாநிலங்களுக்கு இடையேயான எல்லைத் தகராறுகள்",
         "Tax sharing disputes between Union and State", "மத்திய மற்றும் மாநிலத்திற்கு இடையேயான வரிப் பகிர்வுத் தகராறுகள்",
         "Disputes arising out of any pre-Constitution treaty, agreement, covenant, or engagement", "அரசியலமைப்புக்கு முந்தைய உடன்படிக்கை, ஒப்பந்தம் அல்லது பிரகடனத்திலிருந்து எழும் தகராறுகள்",
         "Disputes regarding GST compensation", "GST இழப்பீடு தொடர்பான தகராறுகள்", "C",
         "The proviso to Article 131 excludes disputes arising out of any pre-Constitution treaty, agreement, covenant, or engagement from the Supreme Court's original jurisdiction.",
         "அரசியலமைப்புக்கு முந்தைய உடன்படிக்கைகள் அல்லது ஒப்பந்தங்கள் தொடர்பான தகராறுகளை உச்ச நீதிமன்றத்தின் அசல் வரம்பிலிருந்து உறுப்பு 131-ன் நிபந்தனை விலக்குகிறது."),

        # 15 - B
        ("JRAP_M_015", "Article 143 Advisory Opinion Binding Nature",
         "Is the advisory opinion delivered by the Supreme Court under Article 143 on a reference made by the President binding on the President?",
         "குடியரசுத் தலைவரின் குறிப்பின் பேரில் உறுப்பு 143-ன் கீழ் உச்ச நீதிமன்றம் வழங்கும் ஆலோசனை கருத்து குடியரசுத் தலைவரைக் கட்டுப்படுத்துமா?",
         "Yes, it has the force of a judicial decree", "ஆம், இது ஒரு நீதித்துறை ஆணையின் பலத்தைக் கொண்டுள்ளது",
         "No, it is purely advisory in nature and not binding on the President or the Government", "இல்லை, இது முற்றிலும் ஆலோசனைத் தன்மை கொண்டது மற்றும் குடியரசுத் தலைவரையோ அல்லது அரசையோ கட்டுப்படுத்தாது",
         "Binding only if delivered by a 7-judge bench", "7 நீதிபதிகள் அமர்வால் வழங்கப்பட்டால் மட்டுமே கட்டுப்படுத்தும்",
         "Binding only on state governors", "மாநில ஆளுநர்களை மட்டுமே கட்டுப்படுத்தும்", "B",
         "The opinion under Article 143 is not a judgment or decree; it is advisory and not binding on the President, nor is it 'law declared by Supreme Court' under Article 141.",
         "உறுப்பு 143-ன் கீழான கருத்து தீர்ப்பு அல்ல; அது ஆலோசனையே தவிர குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது; உறுப்பு 141-ன் கீழான சட்டமும் அல்ல."),

        # 16 - D
        ("JRAP_M_016", "Supreme Court Declining Reference",
         "Can the Supreme Court decline to answer a presidential reference made under Article 143(1)?",
         "உறுப்பு 143(1)-ன் கீழ் குடியரசுத் தலைவர் அனுப்பும் குறிப்புக்கு பதிலளிக்க உச்ச நீதிமன்றம் மறுக்க முடியுமா?",
         "No, the Supreme Court must answer every reference", "இல்லை, உச்ச நீதிமன்றம் ஒவ்வொரு குறிப்பிற்கும் பதிலளிக்க வேண்டும்",
         "Only if the reference is signed by the Prime Minister", "பிரதமரால் கையெழுத்திடப்பட்டிருந்தால் மட்டுமே மறுக்கலாம்",
         "Only during a financial emergency", "நிதி அவசரநிலையின் போது மட்டுமே",
         "Yes, under Art. 143(1) the Court has discretion to decline to give its opinion for valid reasons", "ஆம், உறுப்பு 143(1)-ன் கீழ் தகுந்த காரணங்களுக்காக கருத்தைத் தெரிவிக்க மறுக்க நீதிமன்றத்திற்கு விவேக அதிகாரம் உண்டு", "D",
         "In Special Reference No. 1 of 1993 (Ayodhya Reference), the Supreme Court refused to answer the reference under Article 143(1), stating it was superfluous and political.",
         "1993-ன் அயோத்தி விவகாரத்தில் உறுப்பு 143(1)-ன் கீழான குறிப்புக்கு பதிலளிக்க உச்ச நீதிமன்றம் மறுத்தது; இது விவேக அதிகாரத்திற்கு உட்பட்டது."),

        # 17 - A
        ("JRAP_M_017", "Doctrine of Severability Application",
         "In A.K. Gopalan v. State of Madras (1950), which section of the Preventive Detention Act 1950 was severed and declared void, saving the rest of the Act?",
         "ஏ.கே. கோபாலன் v. மெட்ராஸ் மாநிலம் (1950) வழக்கில் 1950-ன் தடுப்புக் காவல் சட்டத்தின் எந்தப் பிரிவு பிரிக்கப்பட்டு செல்லாததாக்கப்பட்டு, சட்டத்தின் எஞ்சிய பகுதி காப்பாற்றப்பட்டது?",
         "Section 14", "பிரிவு 14",
         "Section 3", "பிரிவு 3",
         "Section 7", "பிரிவு 7",
         "Section 11", "பிரிவு 11", "A",
         "Section 14 prevented the detainee from disclosing the grounds of detention to the court. SC held Section 14 void, but severed it, upholding the rest of the Act under the Doctrine of Severability.",
         "பிரிவு 14 கைதி நீதிமன்றத்தில் காரணங்களை வெளிப்படுத்துவதைத் தடுத்தது. உச்ச நீதிமன்றம் பிரிவு 14-ஐ மட்டும் செல்லாது எனப் பிரித்து நீக்கி, எஞ்சிய சட்டத்தை உறுதி செய்தது."),

        # 18 - C
        ("JRAP_M_018", "Doctrine of Eclipse Post-Constitutional Laws",
         "Does the Doctrine of Eclipse apply to post-constitutional laws that violate Fundamental Rights?",
         "அடிப்படை உரிமைகளை மீறும் அரசியலமைப்புக்குப் பிந்தைய சட்டங்களுக்கு மறைப்புக் கோட்பாடு பொருந்துமா?",
         "Yes, to all post-constitutional laws universally", "ஆம், அனைத்து அரசியலமைப்புக்குப் பிந்தைய சட்டங்களுக்கும் பொதுவாகப் பொருந்தும்",
         "Yes, but only for foreign corporations", "ஆம், ஆனால் வெளிநாட்டு நிறுவனங்களுக்கு மட்டுமே",
         "Generally NO; a post-constitutional law violating Part III is void ab initio (stillborn) under Art. 13(2)", "பொதுவாக இல்லை; பகுதி III-ஐ மீறும் அரசியலமைப்புக்குப் பிந்தைய சட்டம் உறுப்பு 13(2)-ன் கீழ் ஆரம்பத்திலிருந்தே செல்லாது (பிறப்பிலேயே இறந்தது)",
         "Only if passed during an emergency", "அவசரநிலையின் போது நிறைவேற்றப்பட்டால் மட்டுமே", "C",
         "In Deep Chand (1959) and Mahendra Lal Jaini (1963), SC held that post-constitutional laws contravening Part III are stillborn and cannot be revived by constitutional amendment under Doctrine of Eclipse.",
         "தீப் சந்த் (1959) வழக்கில் பகுதி III-ஐ மீறும் அரசியலமைப்புக்குப் பிந்தைய சட்டங்கள் பிறப்பிலேயே இறந்தவை என்றும் அவற்றுக்கு மறைப்புக் கோட்பாடு பொருந்தாது என்றும் தீர்ப்பளிக்கப்பட்டது."),

        # 19 - B
        ("JRAP_M_019", "Doctrine of Colourable Legislation",
         "The constitutional maxim 'What cannot be done directly, cannot also be done indirectly' forms the essence of which doctrine?",
         "'நேரடியாகச் செய்ய முடியாத ஒன்றை மறைமுகமாகவும் செய்ய முடியாது' என்ற அரசியலமைப்புப் பழமொழி எந்தக் கோட்பாட்டின் சாராம்சமாகும்?",
         "Doctrine of Severability", "பிரித்தெடுக்கும் கோட்பாடு",
         "Doctrine of Colourable Legislation", "போலிச் சட்டமியற்றல் கோட்பாடு (Colourable Legislation)",
         "Doctrine of Eclipse", "மறைப்புக் கோட்பாடு",
         "Doctrine of Pith and Substance", "அடிநாதக் கோட்பாடு", "B",
         "The Doctrine of Colourable Legislation tests legislative competence: when a legislature has no power to make a law upon a particular subject, it cannot cloister its transgression under the guise of another power.",
         "போலிச் சட்டமியற்றல் கோட்பாடு சட்டமன்ற அதிகார வரம்பை சோதிக்கிறது: ஒரு பொருளின் மீது சட்டம் இயற்ற அதிகாரம் இல்லாதபோது, மற்றொரு அதிகாரத்தின் போர்வையில் அதைச் செய்ய முடியாது."),

        # 20 - D
        ("JRAP_M_020", "Indira Gandhi v. Raj Narain 1975",
         "In Indira Gandhi v. Raj Narain (1975), which constitutional provision inserted by the 39th Amendment Act 1975 was invalidated under the Basic Structure Doctrine?",
         "இந்திரா காந்தி v. ராஜ் நாராயண் (1975) வழக்கில் 39வது திருத்தச் சட்டம் 1975 மூலம் சேர்க்கப்பட்ட எந்த அரசியலமைப்பு விதி அடிப்படைக் கட்டமைப்புக் கோட்பாட்டின் கீழ் ரத்து செய்யப்பட்டது?",
         "Article 31C", "உறுப்பு 31C",
         "Article 356(5)", "உறுப்பு 356(5)",
         "Article 368(4)", "உறுப்பு 368(4)",
         "Article 329A Clause (4)", "உறுப்பு 329A உட்பிரிவு (4)", "D",
         "Clause (4) of Article 329A placed the election of Prime Minister and Speaker beyond judicial scrutiny. The Supreme Court struck it down as violative of democracy, rule of law, and free & fair elections.",
         "உறுப்பு 329A-ன் உட்பிரிவு (4) பிரதமர் மற்றும் சபாநாயகர் தேர்தலை நீதித்துறை ஆய்வுக்கு அப்பாற்பட்டதாக மாற்றியது. இது ஜனநாயகம் மற்றும் சுதந்திரத் தேர்தலை மீறியதால் ரத்து செய்யப்பட்டது."),

        # 21 - A
        ("JRAP_M_021", "Waman Rao Case 1981",
         "In Waman Rao v. Union of India (1981), what vital rule regarding the Basic Structure Doctrine and the Ninth Schedule was established by the Supreme Court?",
         "வாமன் ராவ் v. இந்திய ஒன்றியம் (1981) வழக்கில் அடிப்படைக் கட்டமைப்புக் கோட்பாடு மற்றும் 9வது அட்டவணை தொடர்பாக உச்ச நீதிமன்றத்தால் எந்த முக்கிய விதி நிறுவப்பட்டது?",
         "24 April 1973 was affirmed as the demarcation line for applying the Basic Structure test to Ninth Schedule laws", "9வது அட்டவணைச் சட்டங்களுக்கு அடிப்படைக் கட்டமைப்பு சோதனையைப் பயன்படுத்த 24 ஏப்ரல் 1973 எல்லைக் கோடாக உறுதி செய்யப்பட்டது",
         "All Ninth Schedule laws were declared completely unconstitutional", "அனைத்து 9வது அட்டவணைச் சட்டங்களும் முற்றிலும் அரசியலமைப்புக்கு முரணானவை என அறிவிக்கப்பட்டது",
         "Parliament lost all amending power under Article 368", "நாடாளுமன்றம் உறுப்பு 368 கீழ் அனைத்து திருத்தும் அதிகாரத்தையும் இழந்தது",
         "Basic structure applies only to the Preamble", "அடிப்படைக் கட்டமைப்பு முகப்புரைக்கு மட்டுமே பொருந்தும்", "A",
         "Waman Rao (1981) drew the crucial line of demarcation: amendments to the Constitution made before 24 April 1973 were valid, but those enacted after were subject to the Basic Structure challenge.",
         "வாமன் ராவ் (1981) வழக்கில் 24 ஏப்ரல் 1973-க்கு முந்தைய திருத்தங்கள் பாதுகாக்கப்பட்டவை என்றும், அதற்குப் பிந்தைய திருத்தங்கள் அடிப்படைக் கட்டமைப்பு ஆய்வுக்கு உட்பட்டவை என்றும் கோடு வரையப்பட்டது."),

        # 22 - C
        ("JRAP_M_022", "L. Chandra Kumar 1997",
         "In L. Chandra Kumar v. Union of India (1997), what was the landmark constitutional ruling concerning Articles 323A and 323B?",
         "எல். சந்திர குமார் v. இந்திய ஒன்றியம் (1997) வழக்கில் உறுப்புகள் 323A மற்றும் 323B தொடர்பாக வழங்கப்பட்ட வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்புத் தீர்ப்பு என்ன?",
         "Tribunals were abolished entirely", "தீர்ப்பாயங்கள் முற்றிலும் ஒழிக்கப்பட்டன",
         "Tribunals were placed above High Courts", "தீர்ப்பாயங்கள் உயர் நீதிமன்றங்களுக்கு மேலே வைக்கப்பட்டன",
         "Power of Judicial Review of High Courts under Art. 226/227 and Supreme Court under Art. 32 over tribunals is part of Basic Structure and cannot be excluded", "தீர்ப்பாயங்கள் மீது உயர் நீதிமன்றங்கள் (226/227) மற்றும் உச்ச நீதிமன்றத்திற்கு (32) உள்ள மறுஆய்வு அதிகாரம் அடிப்படைக் கட்டமைப்பின் பகுதி மற்றும் விலக்கப்பட முடியாது",
         "CAT decisions can only be appealed to the President", "CAT தீர்ப்புகளுக்கு எதிராக குடியரசுத் தலைவரிடம் மட்டுமே முறையிட முடியும்", "C",
         "A 7-judge bench ruled that the power of judicial review over tribunals under Articles 226, 227, and 32 is an inviolable basic feature. All tribunal orders are subject to scrutiny by a Division Bench of the High Court.",
         "தீர்ப்பாயங்களின் உத்தரவுகள் மீதான நீதித்துறை மறுஆய்வு அதிகாரம் அடிப்படைக் கட்டமைப்பின் பகுதியாகும்; தீர்ப்பாயங்களின் உத்தரவுகள் அனைத்தும் உயர் நீதிமன்ற இருவர் அமர்வின் ஆய்வுக்கு உட்பட்டவை எனப்பட்டது."),

        # 23 - B
        ("JRAP_M_023", "First Judges Case 1981",
         "In the First Judges Case (S.P. Gupta, 1981), how did the Supreme Court interpret the word 'Consultation' in Articles 124(2) and 217(1)?",
         "முதல் நீதிபதிகள் வழக்கில் (எஸ்.பி. குப்தா, 1981) உறுப்புகள் 124(2) மற்றும் 217(1)-ல் உள்ள 'கலந்தாலோசித்தல்' (Consultation) என்ற சொல்லை உச்ச நீதிமன்றம் எவ்வாறு விளக்கியது?",
         "Consultation means concurrence of the Chief Justice of India", "கலந்தாலோசித்தல் என்பது இந்திய தலைமை நீதிபதியின் உடன்பாட்டைக் குறிக்கிறது",
         "Consultation does NOT mean concurrence; the Executive has primacy in judicial appointments", "கலந்தாலோசித்தல் என்பது உடன்பாடு அல்ல; நீதிபதிகள் நியமனத்தில் நிர்வாகத்திற்கே முதன்மை அதிகாரம் உண்டு",
         "Consultation is optional and not required", "கலந்தாலோசித்தல் விருப்பத்திற்குரியது, கட்டாயமில்லை",
         "Consultation requires a referendum", "கலந்தாலோசித்தல் பொது வாக்கெடுப்பைக் கோருகிறது", "B",
         "In SP Gupta (1981), the Supreme Court held that 'consultation' does not mean 'concurrence' and that the executive has the ultimate power in appointment of judges.",
         "எஸ்.பி. குப்தா (1981) வழக்கில் 'கலந்தாலோசித்தல்' என்பது 'உடன்பாடு' அல்ல என்றும், நீதிபதிகள் நியமனத்தில் நிர்வாகத்திற்கே இறுதி அதிகாரம் உண்டு என்றும் கூறப்பட்டது."),

        # 24 - D
        ("JRAP_M_024", "Second Judges Case 1993",
         "Which historic verdict overruled the First Judges Case and established the 'Collegium System' for appointment of Supreme Court and High Court judges?",
         "முதல் நீதிபதிகள் வழக்கின் தீர்ப்பை ரத்து செய்து, உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்ற நீதிபதிகள் நியமனத்திற்கான 'கொலீஜியம் முறையை' நிறுவிய வரலாற்றுத் தீர்ப்பு எது?",
         "Kesavananda Bharati (1973)", "கேசவாநந்த பாரதி (1973)",
         "Minerva Mills (1980)", "மினர்வா மில்ஸ் (1980)",
         "Maneka Gandhi (1978)", "மேனகா காந்தி (1978)",
         "Second Judges Case (Supreme Court Advocates-on-Record Association v. UOI, 1993)", "இரண்டாவது நீதிபதிகள் வழக்கு (உச்ச நீதிமன்ற வழக்கறிஞர்கள் சங்கம் v. UOI, 1993)", "D",
         "A 9-judge bench in the Second Judges Case (1993) ruled that 'consultation' means 'concurrence' and created the Collegium system consisting of CJI and two senior-most judges.",
         "இரண்டாவது நீதிபதிகள் வழக்கில் (1993) 9 நீதிபதிகள் அமர்வு 'கலந்தாலோசித்தல்' என்பது 'உடன்பாடு' எனத் தீர்ப்பளித்து, தலைமை நீதிபதி மற்றும் இரண்டு மூத்த நீதிபதிகள் கொண்ட கொலீஜியம் முறையை உருவாக்கியது."),

        # 25 - A
        ("JRAP_M_025", "Third Judges Case 1998",
         "In the Third Judges Case (Special Reference 1 of 1998 under Article 143), what was the expanded composition of the Supreme Court Collegium for appointing SC judges?",
         "மூன்றாவது நீதிபதிகள் வழக்கில் (உறுப்பு 143 கீழ் சிறப்பு குறிப்பு 1/1998) உச்ச நீதிமன்ற நீதிபதிகளை நியமிப்பதற்கான கொலீஜியத்தின் விரிவாக்கப்பட்ட அமைப்பு என்ன?",
         "Chief Justice of India and four senior-most puisne judges of the Supreme Court", "இந்திய தலைமை நீதிபதி மற்றும் உச்ச நீதிமன்றத்தின் நான்கு மிக மூத்த நீதிபதிகள்",
         "Chief Justice of India and Union Law Minister", "இந்திய தலைமை நீதிபதி மற்றும் மத்திய சட்ட அமைச்சர்",
         "Chief Justice of India and two senior-most judges", "இந்திய தலைமை நீதிபதி மற்றும் இரண்டு மிக மூத்த நீதிபதிகள்",
         "President, Prime Minister and CJI", "குடியரசுத் தலைவர், பிரதமர் மற்றும் தலைமை நீதிபதி", "A",
         "The Third Judges Case (1998) expanded the Collegium for Supreme Court appointments to CJI plus 4 senior-most judges, and for High Court appointments to CJI plus 2 senior-most judges.",
         "மூன்றாவது நீதிபதிகள் வழக்கில் (1998) உச்ச நீதிமன்ற நியமனங்களுக்கு தலைமை நீதிபதி + 4 மூத்த நீதிபதிகள் எனவும், உயர் நீதிமன்ற நியமனங்களுக்கு தலைமை நீதிபதி + 2 மூத்த நீதிபதிகள் எனவும் விரிவுபடுத்தப்பட்டது."),

        # 26 - C
        ("JRAP_M_026", "Judicial Review of Speaker Certification",
         "In the Aadhaar Case (K.S. Puttaswamy v. Union of India, 2018), did the Supreme Court hold that the Speaker's certification of a bill as a 'Money Bill' under Article 110(3) is open to Judicial Review?",
         "ஆதார் வழக்கில் (2018), உறுப்பு 110(3)-ன் கீழ் ஒரு மசோதாவை 'பண மசோதா' என சபாநாயகர் சான்றளிப்பது நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்ததா?",
         "No, Speaker's decision is absolute and final without exception", "இல்லை, சபாநாயகரின் முடிவு விதிவிலக்கின்றி முழுமையானதும் இறுதியானதுமாகும்",
         "Only if the Rajya Sabha unanimously objects", "மாநிலங்களவை ஏகமனதாக ஆட்சேபித்தால் மட்டுமே",
         "Yes, Speaker's decision as to whether a Bill is a Money Bill is subject to judicial review if it violates constitutional provisions", "ஆம், அரசியலமைப்பு விதிகளை மீறினால் மசோதா பண மசோதாவா என்பது குறித்த சபாநாயகரின் முடிவு மறுஆய்வுக்கு உட்பட்டது",
         "Only if referred by the Election Commission", "தேர்தல் ஆணையத்தால் பரிந்துரைக்கப்பட்டால் மட்டுமே", "C",
         "The Constitution Bench in the Aadhaar judgment (2018) held that the finality attached to the Speaker's certificate under Article 110(3) does not exclude judicial review if constitutional mandates are bypassed.",
         "ஆதார் தீர்ப்பில் (2018) உறுப்பு 110(3)-ன் கீழ் சபாநாயகர் சான்றிதழின் இறுதித்தன்மை, அரசியலமைப்பு விதிகளை மீறும் பட்சத்தில் நீதித்துறை மறுஆய்வைத் தடுக்காது எனப்பட்டது."),

        # 27 - B
        ("JRAP_M_027", "Speedy Trial Fundamental Right",
         "In Hussainara Khatoon (1979), the Supreme Court derived the 'Right to Speedy Trial' as a fundamental right implicit under which Article?",
         "ஹுசைனாரா காதுன் (1979) வழக்கில் உச்ச நீதிமன்றம் எந்த உறுப்பின் கீழ் 'விரைவான விசாரணைக்கான உரிமையை' உள்ளார்ந்த அடிப்படை உரிமையாகப் பெற்றது?",
         "Article 14", "உறுப்பு 14",
         "Article 21", "உறுப்பு 21",
         "Article 19", "உறுப்பு 19",
         "Article 22", "உறுப்பு 22", "B",
         "Justice P.N. Bhagwati held that an expeditious trial is an integral and essential part of the fundamental right to life and liberty enshrined in Article 21.",
         "நீதிபதி பி.என். பகவதி, விரைவான விசாரணை என்பது உறுப்பு 21-ல் பொறிக்கப்பட்டுள்ள வாழ்வு மற்றும் சுதந்திரத்திற்கான அடிப்படை உரிமையின் இன்றியமையாத பகுதி எனத் தீர்ப்பளித்தார்."),

        # 28 - D
        ("JRAP_M_028", "Free Legal Aid Fundamental Right",
         "In M.H. Hoskot v. State of Maharashtra (1978) and Khatri v. State of Bihar (1981), the Supreme Court held that providing free legal aid to an indigent accused is a mandatory constitutional duty of the State under:",
         "எம்.எச். ஹோஸ்காட் (1978) மற்றும் கத்ரி (1981) வழக்குகளில் ஏழை குற்றஞ்சாட்டப்பட்டவருக்கு இலவச சட்ட உதவி வழங்குவது அரசின் கட்டாய அரசியலமைப்பு கடமை என எந்த உறுப்பின் கீழ் தீர்ப்பளிக்கப்பட்டது?",
         "Article 368", "உறுப்பு 368",
         "Article 31", "உறுப்பு 31",
         "Article 19(1)(g)", "உறுப்பு 19(1)(g)",
         "Article 21 read with Article 39A", "உறுப்பு 21 உடன் உறுப்பு 39A", "D",
         "The Supreme Court declared that free legal services to the poor accused is an essential element of reasonable, fair, and just procedure under Article 21, reinforcing DPSP Article 39A.",
         "ஏழைகளுக்கு இலவச சட்ட சேவை வழங்குவது உறுப்பு 21-ன் கீழான நியாயமான நடைமுறையின் இன்றியமையாத கூறு எனவும், உறுப்பு 39A-ஐ வலுப்படுத்துவதாகவும் உச்ச நீதிமன்றம் அறிவித்தது."),

        # 29 - A
        ("JRAP_M_029", "Bhagalpur Blinding Case",
         "The infamous 'Bhagalpur Blinding Case' (Khatri v. State of Bihar, 1981) is a watershed moment in judicial activism because the Supreme Court for the first time awarded:",
         "புகழ்பெற்ற 'பாகல்பூர் கண் குருடாக்கல் வழக்கு' (கத்ரி v. பீகார் மாநிலம், 1981) நீதித்துறை செயல்பாட்டில் ஒரு திருப்புமுனையாக அமைந்தது, ஏனெனில் உச்ச நீதிமன்றம் முதன்முதலில் எதனை வழங்கியது?",
         "Monetary compensation by the State for violation of Fundamental Right under Article 21", "உறுப்பு 21 அடிப்படை உரிமை மீறலுக்காக அரசால் பண இழப்பீடு",
         "Capital punishment for police officers", "காவல்துறை அதிகாரிகளுக்கு மரண தண்டனை",
         "Abolition of police remand", "காவல்துறை காவலை ஒழித்தல்",
         "Permanent reservation for victims", "பாதிக்கப்பட்டோருக்கு நிரந்தர இடஒதுக்கீடு", "A",
         "In Khatri (1981) and later Rudul Sah (1983), the Supreme Court pioneered constitutional tort jurisprudence, ordering the State to pay monetary compensation for police brutality violating Article 21.",
         "கத்ரி (1981) மற்றும் ருதுல் சா (1983) வழக்குகளில் உறுப்பு 21-ஐ மீறிய காவல் அட்டூழியத்திற்காக அரசே பாதிக்கப்பட்டோருக்கு பண இழப்பீடு வழங்க வேண்டும் என்ற அரசியலமைப்பு இழப்பீட்டு விதியை உச்ச நீதிமன்றம் உருவாக்கியது."),

        # 30 - C
        ("JRAP_M_030", "Rudul Sah Illegal Detention Compensation",
         "In Rudul Sah v. State of Bihar (1983), why did the Supreme Court order the State to pay Rs. 35,000 compensation to the petitioner under Article 32?",
         "ருதுல் சா v. பீகார் மாநிலம் (1983) வழக்கில் உறுப்பு 32-ன் கீழ் மனுதாரருக்கு ரூ.35,000 இழப்பீடு வழங்க பீகார் அரசுக்கு உச்ச நீதிமன்றம் ஏன் உத்தரவிட்டது?",
         "For loss of agricultural land", "விவசாய நில இழப்பிற்காக",
         "For wrongful dismissal from service", "பணியிலிருந்து முறையற்ற பணிநீக்கத்திற்காக",
         "For keeping him illegally incarcerated in jail for 14 years after his acquittal", "நீதிமன்றத்தால் விடுவிக்கப்பட்ட பிறகும் அவரை 14 ஆண்டுகள் சட்டவிரோதமாக சிறையில் அடைத்து வைத்திருந்ததற்காக",
         "For medical negligence in government hospital", "அரசு மருத்துவமனையில் மருத்துவ அலட்சியத்திற்காக", "C",
         "Chief Justice Y.V. Chandrachud ruled that Article 32 power is not merely preventive but also remedial, empowering the court to grant monetary compensation for grave violation of personal liberty.",
         "தலைமை நீதிபதி சந்திரசூட், உறுப்பு 32 அதிகாரம் தடுப்பது மட்டுமல்ல தீர்வளிப்பதும் ஆகும் எனக் கூறி, தனிநபர் சுதந்திர மீறலுக்கு இழப்பீடு வழங்க உத்தரவிட்டார்."),

        # 31 - B
        ("JRAP_M_031", "Taj Trapezium Environmental Case",
         "In the Taj Trapezium Case (M.C. Mehta v. Union of India, 1996), which environmental principle was applied by the Supreme Court to order polluting industries around the Taj Mahal to shift or switch to natural gas?",
         "தாஜ் ட்ரெபீசியம் வழக்கில் (1996) தாஜ்மஹாலைச் சுற்றியுள்ள மாசுபடுத்தும் தொழிற்சாலைகள் வெளியேற அல்லது இயற்கை எரிவாயுவுக்கு மாற உச்ச நீதிமன்றம் எந்த சுற்றுச்சூழல் கொள்கையைப் பயன்படுத்தியது?",
         "Doctrine of Laches", "காலதாமதக் கோட்பாடு",
         "Precautionary Principle and Polluter Pays Principle", "முன்னெச்சரிக்கைக் கோட்பாடு மற்றும் மாசுபடுத்தியவரே ஈடுசெய்யும் கோட்பாடு (Polluter Pays)",
         "Doctrine of Sovereign Immunity", "இறையாண்மை விலக்களிப்புக் கோட்பாடு",
         "Doctrine of Colourable Legislation", "போலிச் சட்டமியற்றல் கோட்பாடு", "B",
         "The Supreme Court applied the 'Precautionary Principle' and 'Polluter Pays Principle' as part of the environmental law of the land under Article 21, protecting the white marble of the Taj Mahal from acid rain.",
         "உறுப்பு 21-ன் கீழ் உச்ச நீதிமன்றம் 'முன்னெச்சரிக்கைக் கோட்பாடு' மற்றும் 'மாசுபடுத்தியவரே ஈடுசெய்யும் கொள்கையை' நடைமுறைப்படுத்தி அமில மழையிலிருந்து தாஜ்மஹாலைப் பாதுகாத்தது."),

        # 32 - D
        ("JRAP_M_032", "Absolute Liability Oleum Gas Leak",
         "In M.C. Mehta v. Union of India (1987), famously known as the 'Oleum Gas Leak Case', the Supreme Court propounded which pathbreaking doctrine of strict civil liability?",
         "ஓலியம் வாயு கசிவு வழக்கு என அழைக்கப்படும் எம்.சி. மேத்தா v. இந்திய ஒன்றியம் (1987) வழக்கில் உச்ச நீதிமன்றம் எந்த புரட்சிகரமான சிவில் பொறுப்புக் கோட்பாட்டை முன்வைத்தது?",
         "Rule of Negligence", "அலட்சிய விதி",
         "Rule of Contributory Negligence", "பங்களிப்பு அலட்சிய விதி",
         "Rule of Rylands v. Fletcher (Strict Liability with exceptions)", "ரைலண்ட்ஸ் v. பிளெட்சர் விதி (விதிவிலக்குகளுடன் கூடிய கடுமையான பொறுப்பு)",
         "Doctrine of Absolute Liability (no exceptions)", "முழுமையான பொறுப்புக் கோட்பாடு (Absolute Liability - விதிவிலக்குகள் அற்றது)", "D",
         "Chief Justice P.N. Bhagwati held that an enterprise engaged in a hazardous or inherently dangerous industry owes an 'absolute and non-delegable duty' to the community, with no exceptions.",
         "நீதிபதி பி.என். பகவதி, ஆபத்தான தொழிலில் ஈடுபடும் நிறுவனம் எந்த விதிவிலக்குகளும் இன்றி சமுதாயத்திற்கு 'முழுமையான பொறுப்பைக்' கொண்டுள்ளது என்ற புதிய கோட்பாட்டை உருவாக்கினார்."),

        # 33 - A
        ("JRAP_M_033", "Right to Die vs Right to Life",
         "In Gian Kaur v. State of Punjab (1996), a 5-judge Constitution Bench held that the 'Right to Life' under Article 21:",
         "கியான் கவுர் v. பஞ்சாப் மாநிலம் (1996) வழக்கில் 5 நீதிபதிகள் அரசியலமைப்பு அமர்வு உறுப்பு 21-ன் கீழான 'வாழும் உரிமை' என்பது:",
         "Does NOT include the 'Right to Die' (overruling P. Rathinam)", "'இறக்கும் உரிமையை' உள்ளடக்காது (பி. ரத்தினம் தீர்ப்பை ரத்து செய்தது)",
         "Includes active euthanasia on demand", "கோரிக்கையின் பேரில் தீவிர கருணைக் கொலையை உள்ளடக்கும்",
         "Allows suicide as a fundamental right", "தற்கொலையை ஓர் அடிப்படை உரிமையாக அனுமதிக்கும்",
         "Is subordinate to Article 19", "உறுப்பு 19-க்கு உட்பட்டது", "A",
         "The Constitution Bench held that 'Right to Life' is a natural right embodying life with dignity; suicide is an unnatural termination of life and is not included in Article 21.",
         "அரசியலமைப்பு அமர்வு 'வாழும் உரிமை' என்பது கண்ணியத்துடன் வாழ்வதைக் குறிக்கும் இயற்கை உரிமை என்றும், தற்கொலை என்பது இயற்கைக்கு மாறானது என்பதால் உறுப்பு 21-ல் சேராது என்றும் தீர்ப்பளித்தது."),

        # 34 - C
        ("JRAP_M_034", "Passive Euthanasia and Living Will",
         "In Common Cause v. Union of India (2018), the Supreme Court recognized which crucial right under Article 21, permitting 'Living Wills'?",
         "காமன் காஸ் v. இந்திய ஒன்றியம் (2018) வழக்கில் 'வாழும் விருப்ப ஆவணங்களை' (Living Wills) அனுமதித்து, உறுப்பு 21-ன் கீழ் உச்ச நீதிமன்றம் எந்த முக்கிய உரிமையை அங்கீகரித்தது?",
         "Right to Commit Suicide", "தற்கொலை செய்து கொள்ளும் உரிமை",
         "Right to Capital Punishment", "மரண தண்டனை பெறும் உரிமை",
         "Right to Die with Dignity through Passive Euthanasia", "மறைமுகக் கருணைக் கொலை மூலம் கண்ணியமாக இறக்கும் உரிமை (Right to Die with Dignity)",
         "Right to refuse all taxes", "அனைத்து வரிகளையும் மறுக்கும் உரிமை", "C",
         "A 5-judge bench led by CJI Dipak Misra recognized that the right to die with dignity is a fundamental right under Article 21, legalizing passive euthanasia and Advance Medical Directives (Living Wills).",
         "தலைமை நீதிபதி தீபக் மிஸ்ரா தலைமையிலான 5 நீதிபதிகள் அமர்வு கண்ணியமாக இறக்கும் உரிமை உறுப்பு 21-ன் கீழ் அடிப்படை உரிமை என அங்கீகரித்து, மறைமுக கருணைக் கொலையை சட்டபூர்வமாக்கியது."),

        # 35 - B
        ("JRAP_M_035", "Decriminalization of Section 377",
         "In Navtej Singh Johar v. Union of India (2018), which colonial penal provision was struck down by the Supreme Court to protect LGBTQ+ equality under Articles 14, 15, 19, and 21?",
         "நவ்தேஜ் சிங் ஜோஹர் v. இந்திய ஒன்றியம் (2018) வழக்கில் உறுப்புகள் 14, 15, 19, மற்றும் 21-ன் கீழ் LGBTQ+ சமத்துவத்தைப் பாதுகாக்க உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்ட காலனித்துவ தண்டனைப் பிரிவு எது?",
         "Section 302 IPC", "IPC பிரிவு 302",
         "Section 377 IPC (consensual adult sexual acts)", "IPC பிரிவு 377 (வயது வந்தோரின் பரஸ்பர சம்மதத்துடன் கூடிய உறவு)",
         "Section 497 IPC", "IPC பிரிவு 497",
         "Section 124A IPC", "IPC பிரிவு 124A", "B",
         "A unanimous 5-judge bench held that Section 377, insofar as it criminalizes consensual sexual acts between adults in private, is irrational, unconstitutional, and violative of Articles 14, 15, 19, and 21.",
         "வயது வந்தோரின் சம்மதத்துடன் கூடிய தனிப்பட்ட உறவைக் குற்றமாக்கும் வகையில் IPC பிரிவு 377 அரசியலமைப்புக்கு முரணானது மற்றும் உறுப்புகள் 14, 15, 19, 21-ஐ மீறுகிறது என உச்ச நீதிமன்றம் ரத்து செய்தது."),

        # 36 - D
        ("JRAP_M_036", "Striking Down Adultery Section 497",
         "In Joseph Shine v. Union of India (2018), the Supreme Court struck down Section 497 of the IPC (Adultery) primarily on the ground that:",
         "ஜோசப் ஷைன் v. இந்திய ஒன்றியம் (2018) வழக்கில் உச்ச நீதிமன்றம் IPC பிரிவு 497-ஐ (விபச்சாரம்) ரத்து செய்ததற்கு முதன்மைக் காரணம் என்ன?",
         "It reduced the revenue of the government", "அது அரசின் வருவாயைக் குறைத்தது",
         "It violated Article 368", "அது உறுப்பு 368-ஐ மீறியது",
         "It was not ratified by the States", "அது மாநிலங்களால் அங்கீகரிக்கப்படவில்லை",
         "It treated women as chattel/property of husbands, violating gender equality (Art. 14) and dignity (Art. 21)", "அது பெண்களை கணவரின் உடைமையாகக் கருதி பாலின சமத்துவம் (உறுப்பு 14) மற்றும் கண்ணியத்தை (உறுப்பு 21) மீறியது", "D",
         "The Supreme Court unanimously struck down Section 497 IPC as manifestly arbitrary and unconstitutional, emphasizing that treating a wife as property of her husband is an archaic denial of dignity.",
         "மனைவியைக் கணவனின் சொத்தாகக் கருதும் காலாவதியான முறை பாலின சமத்துவம் மற்றும் கண்ணியத்தை மறுக்கிறது எனக் கூறி உச்ச நீதிமன்றம் IPC 497-ஐ ரத்து செய்தது."),

        # 37 - A
        ("JRAP_M_037", "Right to Shelter Under Art. 21",
         "In Olga Tellis v. Bombay Municipal Corporation (1985), famously known as the 'Pavement Dwellers Case', what major constitutional right was linked to the Right to Life?",
         "நடைபாதை வாசிகள் வழக்கு என அறியப்படும் ஓல்கா டெல்லிஸ் v. பாம்பே மாநகராட்சி (1985) வழக்கில் வாழும் உரிமையுடன் இணைக்கப்பட்ட முக்கிய அரசியலமைப்பு உரிமை எது?",
         "Right to Livelihood and Shelter", "வாழ்வாதாரம் மற்றும் தங்குமிடத்திற்கான உரிமை (Right to Livelihood)",
         "Right to free air travel", "இலவச விமானப் பயண உரிமை",
         "Right to commercial contracts", "வணிக ஒப்பந்தங்களுக்கான உரிமை",
         "Right to strike work", "வேலைநிறுத்தம் செய்யும் உரிமை", "A",
         "Chief Justice Y.V. Chandrachud held that the 'Right to Livelihood' is an integral part of the 'Right to Life' under Article 21, as no person can live without the means of living.",
         "தலைமை நீதிபதி சந்திரசூட், வாழ்வாதாரம் இன்றி எவரும் வாழ முடியாது என்பதால் 'வாழ்வாதார உரிமை' என்பது உறுப்பு 21-ன் கீழான வாழும் உரிமையின் ஒருங்கிணைந்த பகுதி எனத் தீர்ப்பளித்தார்."),

        # 38 - C
        ("JRAP_M_038", "Voter's Right to Know",
         "In Union of India v. Association for Democratic Reforms (ADR, 2002), the Supreme Court held that the voter's right to know the criminal antecedents and assets of candidates is part of:",
         "அசோசியேஷன் ஃபார் டெமாக்ரடிக் ரிஃபார்ம்ஸ் (ADR, 2002) வழக்கில் வேட்பாளர்களின் குற்றப் பின்னணி மற்றும் சொத்துக்களை அறிய வாக்காளருக்கு உள்ள உரிமை எதன் பகுதி என உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
         "Article 326", "உறுப்பு 326",
         "Article 324", "உறுப்பு 324",
         "Freedom of Speech and Expression under Article 19(1)(a)", "உறுப்பு 19(1)(a)-ன் கீழான பேச்சு மற்றும் கருத்து சுதந்திரம்",
         "Article 14 only", "உறுப்பு 14 மட்டுமே", "C",
         "The Supreme Court held that a voter has a constitutional right under Article 19(1)(a) to know the antecedents, qualifications, and assets/liabilities of candidates seeking election.",
         "தேர்தலில் போட்டியிடும் வேட்பாளர்களின் சொத்துக்கள் மற்றும் குற்றப் பின்னணியை அறிந்து கொள்ளும் உரிமை உறுப்பு 19(1)(a)-ன் கீழ் வாக்காளரின் அடிப்படை உரிமை என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 39 - B
        ("JRAP_M_039", "Disqualification of Convicted Legislators",
         "In Lily Thomas v. Union of India (2013), which statutory provision was struck down by the Supreme Court, ensuring immediate disqualification of convicted MPs/MLAs sentenced to 2+ years?",
         "லில்லி தாமஸ் v. இந்திய ஒன்றியம் (2013) வழக்கில் 2+ ஆண்டுகள் தண்டனை பெற்ற எம்.பி./எம்.எல்.ஏ.க்கள் உடனடியாக தகுதிநீக்கம் செய்யப்படுவதை உறுதி செய்ய உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்ட சட்டப்பிரிவு எது?",
         "Section 8(1) of RPA 1951", "RPA 1951-ன் பிரிவு 8(1)",
         "Section 8(4) of the Representation of the People Act 1951", "மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் பிரிவு 8(4)",
         "Section 123 of RPA 1951", "RPA 1951-ன் பிரிவு 123",
         "Section 29A of RPA 1951", "RPA 1951-ன் பிரிவு 29A", "B",
         "Section 8(4) allowed convicted legislators a 3-month protection window to appeal without getting disqualified. The Supreme Court struck it down as ultra vires Articles 102(1)(e) and 191(1)(e).",
         "பிரிவு 8(4) தண்டனை பெற்ற எம்.பி./எம்.எல்.ஏ.க்கள் தகுதிநீக்கம் பெறாமல் 3 மாதங்களுக்கு மேல்முறையீடு செய்ய பாதுகாப்பளித்தது. உச்ச நீதிமன்றம் இப்பிரிவை அரசியலமைப்புக்கு முரணானது என ரத்து செய்தது."),

        # 40 - D
        ("JRAP_M_040", "NOTA Option Introduction",
         "In People's Union for Civil Liberties (PUCL) v. Union of India (2013), the Supreme Court directed the Election Commission to introduce which option on EVMs under Article 19(1)(a)?",
         "PUCL v. இந்திய ஒன்றியம் (2013) வழக்கில் உறுப்பு 19(1)(a)-ன் கீழ் மின்னணு வாக்குப்பதிவு இயந்திரங்களில் எந்த தேர்வை அறிமுகப்படுத்த உச்ச நீதிமன்றம் தேர்தல் ஆணையத்திற்கு உத்தரவிட்டது?",
         "Recall Option", "திரும்பப் பெறும் தேர்வு",
         "Postal Vote Option", "அஞ்சல் வாக்குத் தேர்வு",
         "Secret Ballot Exclusion", "ரகசிய வாக்கு விலக்கு",
         "None of the Above (NOTA)", "மேற்கண்ட எவருமில்லை (NOTA - None of the Above)", "D",
         "The Supreme Court recognized the voter's right to express disapproval and negative opinion by introducing NOTA, derived from freedom of speech and expression under Article 19(1)(a).",
         "உறுப்பு 19(1)(a) பேச்சுரிமையிலிருந்து எதிர்மறை வாக்களிக்கும் உரிமையைப் பெற்று, வேட்பாளர்களை நிராகரிக்க வாக்காளர்களுக்கு NOTA பொத்தானை வழங்க உச்ச நீதிமன்றம் உத்தரவிட்டது."),

        # 41 - A
        ("JRAP_M_041", "Doctrine of Ultra Vires",
         "When an administrative body exercises powers beyond the limits granted to it by the parent statute, its action is declared void under which legal doctrine?",
         "ஒரு நிர்வாக அமைப்பு தாய் சட்டம் தனக்கு வழங்கிய அதிகார வரம்புகளுக்கு அப்பால் செயல்படும் போது, அதன் செயல் எந்த சட்டக் கோட்பாட்டின் கீழ் செல்லாது என அறிவிக்கப்படுகிறது?",
         "Doctrine of Substantive Ultra Vires", "பொருளாதார அதிகார வரம்பு மீறல் கோட்பாடு (Substantive Ultra Vires)",
         "Doctrine of Res Judicata", "முன் தீர்ப்புத் தடை கோட்பாடு",
         "Doctrine of Promissory Estoppel", "வாக்குறுதி முட்டுக்கட்டைக் கோட்பாடு",
         "Doctrine of Stare Decisis", "முன் தீர்ப்பு நிலைப்பாட்டுக் கோட்பாடு", "A",
         "Ultra vires literally means 'beyond powers'. Substantive ultra vires occurs when delegated or administrative action acts beyond the boundaries of statutory competence.",
         "அல்ட்ரா வைரஸ் என்றால் 'அதிகாரத்திற்கு அப்பால்' என்று பொருள். தாய் சட்டம் அளித்த அதிகார வரம்பை மீறி நிர்வாகம் செயல்படும்போது அந்த நடவடிக்கை செல்லாததாகிறது."),

        # 42 - C
        ("JRAP_M_042", "Wednesbury Unreasonableness",
         "The principle of 'Wednesbury Unreasonableness' widely used in judicial review of administrative action originates from which jurisdiction?",
         "நிர்வாக நடவடிக்கைகளின் நீதித்துறை மறுஆய்வில் பரவலாகப் பயன்படுத்தப்படும் 'வெட்னஸ்பரி நியாயமற்ற தன்மை' (Wednesbury Unreasonableness) என்ற கோட்பாடு எந்த நாட்டு சட்ட அமைப்பிலிருந்து உருவானது?",
         "United States of America", "அமெரிக்க ஐக்கிய நாடுகள்",
         "France", "பிரான்ஸ்",
         "England (UK Court of Appeal)", "இங்கிலாந்து (UK மேல்முறையீட்டு நீதிமன்றம்)",
         "Germany", "ஜெர்மனி", "C",
         "The principle was formulated in Associated Provincial Picture Houses v. Wednesbury Corporation (1948) in England, meaning a decision so unreasonable that no sensible authority could ever make it.",
         "இக்கோட்பாடு 1948-ல் இங்கிலாந்தில் வெட்னஸ்பரி வழக்கில் உருவாக்கப்பட்டது; எந்தவொரு விவேகமான அதிகாரியும் எடுக்க முடியாத அளவிற்கு முற்றிலும் நியாயமற்ற முடிவை இது குறிக்கிறது."),

        # 43 - B
        ("JRAP_M_043", "Doctrine of Proportionality",
         "The modern European doctrine of 'Proportionality' applied in Indian judicial review means that:",
         "இந்திய நீதித்துறை மறுஆய்வில் பயன்படுத்தப்படும் நவீன ஐரோப்பிய 'விகிதாசாரக் கோட்பாடு' (Proportionality) எதனைக் குறிக்கிறது?",
         "The court should decide budget allocations proportionally", "நீதிமன்றமே பட்ஜெட் ஒதுக்கீடுகளை விகிதாசாரப்படி தீர்மானிக்க வேண்டும்",
         "The administrative measure taken must not be more drastic than necessary for attaining the legitimate objective", "சட்டபூர்வமான நோக்கத்தை அடைவதற்கு எடுக்கப்பட்ட நிர்வாக நடவடிக்கை அவசியமானதை விடக் கடுமையானதாக இருக்கக்கூடாது",
         "Judges must be appointed in proportion to population", "மக்கள் தொகைக்கு ஏற்ப விகிதாசார அடிப்படையில் நீதிபதிகள் நியமிக்கப்பட வேண்டும்",
         "All statutes must have proportional representation clauses", "அனைத்து சட்டங்களிலும் விகிதாசார பிரதிநிதித்துவப் பிரிவுகள் இருக்க வேண்டும்", "B",
         "Proportionality balances the means used with the end pursued: an administrative or legislative restriction on a fundamental right must be the least intrusive means to achieve the objective.",
         "விகிதாசாரக் கோட்பாடு என்பது பயன்படுத்தப்படும் வழிமுறையையும் நோக்கத்தையும் சமன் செய்கிறது: ஓர் அடிப்படை உரிமை மீதான கட்டுப்பாடு நோக்கத்தை அடைய மிகக் குறைந்த பாதிப்பை ஏற்படுத்துவதாக இருக்க வேண்டும்."),

        # 44 - D
        ("JRAP_M_044", "Prakash Singh Police Reforms",
         "In Prakash Singh v. Union of India (2006), the Supreme Court issued 7 binding directives on:",
         "பிரகாஷ் சிங் v. இந்திய ஒன்றியம் (2006) வழக்கில் உச்ச நீதிமன்றம் எதன் மீது 7 கட்டாய உத்தரவுகளைப் பிறப்பித்தது?",
         "Educational institutions reservation", "கல்வி நிறுவனங்கள் இடஒதுக்கீடு",
         "Electoral bonds transparency", "தேர்தல் பத்திரங்கள் வெளிப்படைத்தன்மை",
         "Judicial appointments transparency", "நீதித்துறை நியமனங்கள் வெளிப்படைத்தன்மை",
         "Police Reforms and operational autonomy of police forces from political interference", "காவல்துறை சீர்திருத்தங்கள் மற்றும் அரசியல் தலையீடற்ற தன்னாட்சி", "D",
         "The Supreme Court laid down 7 directives including fixed tenures for DGP/SPs, establishment of State Security Commissions, Police Establishment Boards, and Police Complaints Authorities.",
         "DGP/SP-க்களுக்கு நிலையான பதவிக்காலம், மாநில பாதுகாப்புக் குழு, காவல்துறை புகார் ஆணையம் உள்ளிட்ட 7 வழிகாட்டுதல்களை உச்ச நீதிமன்றம் பிறப்பித்தது."),

        # 45 - A
        ("JRAP_M_045", "Judicial Overreach Examples",
         "Which of the following judicial interventions has been criticized by jurists as an instance of 'Judicial Overreach' rather than legitimate activism?",
         "பின்வரும் எந்த நீதித்துறை தலையீடு முறையான செயல்பாடாக இல்லாமல் 'நீதித்துறை மிதமிஞ்சிய செயல்பாடாக' (Judicial Overreach) சட்ட அறிஞர்களால் விமர்சிக்கப்பட்டது?",
         "Ordering liquor shops to shut down within 500 metres of all National and State Highways", "தேசிய மற்றும் மாநில நெடுஞ்சாலைகளின் 500 மீட்டருக்குள் உள்ள அனைத்து மதுக்கடைகளையும் மூட உத்தரவிட்டது",
         "Releasing bonded labourers in Bandhua Mukti Morcha", "பந்துவா முக்தி மோர்ச்சாவில் கொத்தடிமைகளை விடுவித்தது",
         "Ordering speedy trial in Hussainara Khatoon", "ஹுசைனாரா காதுனில் விரைவான விசாரணைக்கு உத்தரவிட்டது",
         "Enforcing POCSO guidelines", "POCSO வழிகாட்டுதல்களை அமல்படுத்தியது", "A",
         "The Supreme Court's ban on liquor shops on highways was widely criticized as entering the policy and administrative domain without considering economic and legislative repercussions.",
         "நெடுஞ்சாலை மதுக்கடைகள் மீதான உச்ச நீதிமன்றத் தடை, பொருளாதார மற்றும் சட்டமன்ற விளைவுகளைக் கருதாமல் நிர்வாகக் கொள்கை எல்லைக்குள் நுழைந்ததாக விமர்சிக்கப்பட்டது."),

        # 46 - C
        ("JRAP_M_046", "National Anthem Case",
         "In Shyam Narayan Chouksey v. Union of India (2016), the Supreme Court initially mandated the playing of the National Anthem in cinema halls, but later in 2018 modified it to be:",
         "ஷ்யாம் நாராயண் சௌக்சி வழக்கில் (2016) உச்ச நீதிமன்றம் முதலில் திரையரங்குகளில் தேசிய கீதம் இசைப்பதை கட்டாயமாக்கியது; பின்னர் 2018-ல் அதை எவ்வாறு மாற்றியமைத்தது?",
         "Permanently banned", "நிரந்தரமாகத் தடை செய்தது",
         "Mandatory only in educational institutions", "கல்வி நிறுவனங்களில் மட்டுமே கட்டாயம்",
         "Optional / Non-mandatory, deferring to the discretion of the Union Government", "கட்டாயமில்லை / விருப்பத்திற்குரியது என மத்திய அரசின் முடிவிற்கே விட்டது",
         "Mandatory on railway stations", "ரயில் நிலையங்களில் கட்டாயம்", "C",
         "In 2018, the Supreme Court modified its earlier order, accepting the government's stance and ruling that playing the national anthem in cinema halls was optional, illustrating judicial self-correction.",
         "2018-ல் உச்ச நீதிமன்றம் தனது முந்தைய உத்தரவை மாற்றி, திரையரங்குகளில் தேசிய கீதம் இசைப்பது கட்டாயமில்லை எனக் கூறி நீதித்துறை சுயதிருத்தத்தை வெளிப்படுத்தியது."),

        # 47 - B
        ("JRAP_M_047", "Subhash Kumar Pollution Free Environment",
         "In Subhash Kumar v. State of Bihar (1991), what fundamental principle regarding environmental protection under Article 21 was laid down?",
         "சுபாஷ் குமார் v. பீகார் மாநிலம் (1991) வழக்கில் உறுப்பு 21-ன் கீழ் சுற்றுச்சூழல் பாதுகாப்பு தொடர்பாக எந்த அடிப்படைக் கொள்கை வகுக்கப்பட்டது?",
         "Pollution control is only an international treaty obligation", "மாசு கட்டுப்பாடு என்பது சர்வதேச ஒப்பந்த கடமை மட்டுமே",
         "Right to life includes the right of enjoyment of pollution-free water and air for full enjoyment of life", "வாழும் உரிமை என்பது முழுமையான வாழ்வை அனுபவிக்க மாசற்ற நீர் மற்றும் காற்றை அனுபவிக்கும் உரிமையை உள்ளடக்கியது",
         "Only State governments have the right to clean water", "மாநில அரசுகளுக்கு மட்டுமே சுத்தமான நீருக்கான உரிமை உண்டு",
         "Industries have an absolute right to discharge effluents", "கழிவுநீரை வெளியேற்ற தொழிற்சாலைகளுக்கு முழு உரிமை உண்டு", "B",
         "The Supreme Court explicitly declared that the right to live is a fundamental right under Article 21 and includes the right of enjoyment of pollution-free water and air.",
         "வாழும் உரிமை என்பது உறுப்பு 21-ன் கீழ் மாசற்ற நீர் மற்றும் காற்றை அனுபவிக்கும் உரிமையை உள்ளடக்கியது என உச்ச நீதிமன்றம் வெளிப்படையாக அறிவித்தது."),

        # 48 - D
        ("JRAP_M_048", "Article 31C Struck Down Part",
         "In Kesavananda Bharati (1973), which specific part of Article 31C inserted by the 25th Amendment Act 1971 was struck down as unconstitutional?",
         "கேசவாநந்த பாரதி (1973) வழக்கில் 1971-ன் 25வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்ட உறுப்பு 31C-ன் எந்த குறிப்பிட்ட பகுதி அரசியலமைப்புக்கு முரணானது என ரத்து செய்யப்பட்டது?",
         "The declaration giving primacy to Directive Principles 39(b) and (c)", "வழிகாட்டு நெறிமுறைகள் 39(b) மற்றும் (c)-க்கு முதன்மை அளித்த பிரகடனம்",
         "The entire Article 31C", "உறுப்பு 31C முழுமையாக",
         "The preamble of Article 31C", "உறுப்பு 31C-ன் முன்னுரை",
         "The clause stating 'and no law containing a declaration that it is for giving effect to such policy shall be called in question in any court'", "'அத்தகைய கொள்கையை நடைமுறைப்படுத்துவதற்கான பிரகடனத்தைக் கொண்ட எந்தவொரு சட்டமும் எந்த நீதிமன்றத்திலும் கேள்வி கேட்கப்படக்கூடாது' என்ற பிரிவு", "D",
         "The Supreme Court struck down the second half of Article 31C which barred judicial review, holding that Parliament cannot insulate a law from judicial scrutiny.",
         "நீதித்துறை மறுஆய்வைத் தடுத்த உறுப்பு 31C-ன் இரண்டாம் பகுதியை உச்ச நீதிமன்றம் ரத்து செய்தது; எந்தவொரு சட்டத்தையும் நீதித்துறை ஆய்விலிருந்து நாடாளுமன்றம் பாதுகாக்க முடியாது என்றது."),

        # 49 - A
        ("JRAP_M_049", "Separation of Powers in Indian Constitution",
         "Unlike the US Constitution, which has a rigid separation of powers, the Indian Constitution follows:",
         "கடுமையான அதிகாரப் பகிர்வைக் கொண்ட அமெரிக்க அரசியலமைப்பு போலன்றி, இந்திய அரசியலமைப்பு எதனைப் பின்பற்றுகிறது?",
         "A system of functional checks and balances without rigid separation between Legislature and Executive", "சட்டமன்றம் மற்றும் நிர்வாகத்திற்கு இடையே கடுமையான பிரிவின்றி செயல்பாட்டுச் சமநிலைகள் மற்றும் கட்டுப்பாடுகள் கொண்ட முறை",
         "Complete union of judicial and executive powers", "நீதித்துறை மற்றும் நிர்வாக அதிகாரங்களின் முழுமையான ஒருங்கிணைப்பு",
         "Total dominance of the Prime Minister over the judiciary", "நீதித்துறையின் மீது பிரதமரின் முழுமையான ஆதிக்கம்",
         "Military supremacy over civilian authorities", "பொதுமக்கள் நிர்வாகத்தின் மீது ராணுவ மேலாதிக்கம்", "A",
         "In Ram Jawaya Kapur (1955), Supreme Court held that the Indian Constitution does not recognize a rigid separation of powers, but differentiates organs while maintaining a system of checks and balances.",
         "ராம் ஜவாயா கபூர் (1955) வழக்கில் இந்திய அரசியலமைப்பு கடுமையான அதிகாரப் பகிர்வை ஏற்கவில்லை; மாறாக உறுப்புகளை வேறுபடுத்தி சமநிலைகள் மற்றும் கட்டுப்பாட்டு முறையைப் பராமரிக்கிறது எனப்பட்டது."),

        # 50 - C
        ("JRAP_M_050", "Transcendental Position of FRs",
         "The doctrine that Fundamental Rights occupy a 'transcendental and immutable position' beyond the reach of parliamentary amendment was declared by Chief Justice Subba Rao in:",
         "அடிப்படை உரிமைகள் நாடாளுமன்றத் திருத்தத்திற்கு அப்பாற்பட்ட 'உயர்ந்த மற்றும் மாற்ற முடியாத நிலையை' வகிக்கின்றன என்ற கோட்பாட்டை தலைமை நீதிபதி சுப்பா ராவ் எதில் அறிவித்தார்?",
         "Shankari Prasad (1951)", "சங்கரி பிரசாத் (1951)",
         "Sajjan Singh (1965)", "சஜ்ஜன் சிங் (1965)",
         "I.C. Golaknath v. State of Punjab (1967)", "ஐ.சி. கோலக்நாத் v. பஞ்சாப் மாநிலம் (1967)",
         "Minerva Mills (1980)", "மினர்வா மில்ஸ் (1980)", "C",
         "In Golaknath (1967), the majority held that Fundamental Rights are given a transcendental position by the Constitution makers, and Parliament cannot take them away via Article 368.",
         "கோலக்நாத் (1967) வழக்கில் அரசியலமைப்பு உருவாக்கியவர்களால் அடிப்படை உரிமைகளுக்கு உயர்ந்த நிலை அளிக்கப்பட்டுள்ளது; நாடாளுமன்றம் உறுப்பு 368 மூலம் அவற்றைப் பறிக்க முடியாது எனப்பட்டது.")
    ]

    for item in medium_data:
        qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item
        why_a_en = f"Option A evaluation regarding {en_a}."
        why_a_ta = f"{ta_a} பற்றிய ஆப்ஷன் A மதிப்பீடு."
        why_b_en = f"Option B evaluation regarding {en_b}."
        why_b_ta = f"{ta_b} பற்றிய ஆப்ஷன் B மதிப்பீடு."
        why_c_en = f"Option C evaluation regarding {en_c}."
        why_c_ta = f"{ta_c} பற்றிய ஆப்ஷன் C மதிப்பீடு."
        why_d_en = f"Option D evaluation regarding {en_d}."
        why_d_ta = f"{ta_d} பற்றிய ஆப்ஷன் D மதிப்பீடு."
        tip_en = "Scrutinize constitutional bench majorities, Article sub-clauses, and judicial doctrines."
        tip_ta = "அரசியலமைப்பு அமர்வு பெரும்பான்மை, உறுப்புகளின் உட்பிரிவுகள் மற்றும் நீதித்துறை கோட்பாடுகளை உன்னிப்பாகக் கவனிக்கவும்."
        fact_en = f"High-yield factual benchmark on {subtopic} for TNPSC Group 1/2 exams."
        fact_ta = f"TNPSC குரூப் 1/2 தேர்வுகளுக்கான {subtopic} தொடர்பான முதன்மையான உண்மை அளவுகோல்."

        q = make_jrap_q(
            qid, "Medium", "single_choice", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Key distribution audit
    keys = [q["correct_answer"] for q in questions]
    counts = Counter(keys)
    print("Part 1 Medium Key counts:", counts)
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    for opt in ["A", "B", "C", "D"]:
        assert 12 <= counts[opt] <= 13, f"Key {opt} out of balance: {counts[opt]}"

    # Anti-block check: max consecutive <= 2
    for idx in range(len(keys) - 2):
        assert not (keys[idx] == keys[idx+1] == keys[idx+2]), f"3 consecutive keys at index {idx}: {keys[idx]}"

    out_path = "data/questions/polity/judicial_review_activism_pil_medium.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote 50 medium MCQs to {out_path}")

if __name__ == "__main__":
    build_medium_mcqs()
