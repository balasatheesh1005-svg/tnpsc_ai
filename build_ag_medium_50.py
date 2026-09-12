# -*- coding: utf-8 -*-
"""
Generator for Attorney General of India Medium MCQs (50 Questions: AG_M_001 to AG_M_050).
Strictly adheres to:
- Full 24-field TNPSC Nova AI schema
- Balanced answer keys (13 B, 12 C, 12 D, 13 A)
- Fully bilingual (English and authentic Tamil)
- M. Laxmikanth, Constitution of India, Samacheer Kalvi, Law Officers Rules 1987
"""
import json
import os
from ag_mcq_helper import make_ag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_medium_data = [
    # 1
    {
        "stem_en": "Under Article 88 of the Constitution, which of the following rights is explicitly denied to the Attorney General of India during Parliamentary proceedings?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 88-ன் கீழ், நாடாளுமன்ற நடவடிக்கைகளின் போது இந்திய தலைமை வழக்கறிஞருக்கு வெளிப்படையாக மறுக்கப்பட்டுள்ள உரிமை எது?",
        "options": [
            ("Right to speak in either House", "இரு அவைகளிலும் பேசும் உரிமை"),
            ("Right to vote in any House or committee", "எந்த அவையிலோ அல்லது குழுவிலோ வாக்களிக்கும் உரிமை"),
            ("Right to take part in joint sittings", "கூட்டு அமர்வுகளில் பங்கேற்கும் உரிமை"),
            ("Right to address a parliamentary committee", "நாடாளுமன்றக் குழுவில் உரையாற்றும் உரிமை")
        ],
        "correct_idx": 1,
        "exp_en": "Article 88 explicitly provides that the Attorney General has the right to speak and take part in proceedings, but 'shall not by virtue of this Article be entitled to vote'.",
        "exp_ta": "சரத்து 88, தலைமை வழக்கறிஞர் பேசவும் பங்கேற்கவும் உரிமை உண்டு என்று கூறினாலும், அவர் 'வாக்களிக்க உரிமை பெற்றவர் அல்ல' என்று திட்டவட்டமாக மறுக்கிறது.",
        "tip": "Voting in Parliament is an exclusive democratic privilege of elected/nominated Members of Parliament.",
        "fact": "Even when the AG is named a member of a Joint Parliamentary Committee, he cannot vote."
    },
    # 2
    {
        "stem_en": "How does the constitutional status of the Attorney General of India differ from that of the Solicitor General of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞரின் அரசியலமைப்பு அந்தஸ்து, இந்திய சொலிசிட்டர் ஜெனரலின் அந்தஸ்திலிருந்து எவ்வாறு வேறுபடுகிறது?",
        "options": [
            ("Both are constitutional offices created under Article 76", "இருவரும் சரத்து 76-ன் கீழ் உருவாக்கப்பட்ட அரசியலமைப்பு அலுவலகங்கள்"),
            ("The Attorney General is a constitutional office under Article 76, while the Solicitor General is a statutory / executive office not mentioned in the Constitution", "தலைமை வழக்கறிஞர் சரத்து 76-ன் கீழான அரசியலமைப்பு அலுவலகம்; சொலிசிட்டர் ஜெனரல் அரசியலமைப்பில் குறிப்பிடப்படாத சட்டப்பூர்வ/நிர்வாக அலுவலகம்"),
            ("The Solicitor General is superior in hierarchy to the Attorney General", "சொலிசிட்டர் ஜெனரல் தலைமை வழக்கறிஞரை விட உயர் பதவியில் உள்ளார்"),
            ("The Attorney General is appointed by the Prime Minister, whereas the Solicitor General is appointed by the President", "தலைமை வழக்கறிஞரை பிரதமரும், சொலிசிட்டர் ஜெனரலை குடியரசுத் தலைவரும் நியமிக்கின்றனர்")
        ],
        "correct_idx": 1,
        "exp_en": "Article 76 creates only the office of the Attorney General. The Solicitor General and Additional Solicitors General are non-constitutional law officers created under administrative rules to assist the AG.",
        "exp_ta": "சரத்து 76 தலைமை வழக்கறிஞர் அலுவலகத்தை மட்டுமே உருவாக்குகிறது. சொலிசிட்டர் ஜெனரல் மற்றும் கூடுதல் சொலிசிட்டர் ஜெனரல்கள் அரசியலமைப்பில் இடம்பெறாத, அவருக்கு உதவ நிர்வாக விதிகளின் கீழ் நியமிக்கப்படும் அதிகாரிகள்.",
        "tip": "Only ONE constitutional law officer exists at the Union level: the Attorney General of India.",
        "fact": "Solicitor General is considered the Second Law Officer of the Government of India."
    },
    # 3
    {
        "stem_en": "Under Article 76(4), the Attorney General holds office during the pleasure of the President. What does this 'pleasure of the President' practically mean in constitutional law?",
        "stem_ta": "சரத்து 76(4)-ன் கீழ், தலைமை வழக்கறிஞர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிக்கிறார். அரசியலமைப்பு சட்டத்தில் 'குடியரசுத் தலைவரின் விருப்பம்' என்பது நடைமுறையில் எதைக் குறிக்கிறது?",
        "options": [
            ("Discretion of the Chief Justice of India", "இந்திய தலைமை நீதிபதியின் தனிப்பட்ட விருப்பம்"),
            ("Advice of the Union Council of Ministers headed by the Prime Minister under Article 74", "சரத்து 74-ன் கீழ் பிரதமரைத் தலைவராகக் கொண்ட மத்திய அமைச்சரவையின் ஆலோசனை"),
            ("Approval of the Speaker of Lok Sabha", "மக்களவை சபாநாயகரின் ஒப்புதல்"),
            ("Resolution passed by both Houses of Parliament", "நாடாளுமன்றத்தின் இரு அவைகளும் நிறைவேற்றும் தீர்மானம்")
        ],
        "correct_idx": 1,
        "exp_en": "Under Article 74, the President exercises all executive powers on the aid and advice of the Council of Ministers headed by the PM. Hence, 'pleasure of the President' means he holds office as long as the Union Cabinet desires.",
        "exp_ta": "சரத்து 74-ன் கீழ் குடியரசுத் தலைவர் அமைச்சரவையின் ஆலோசனையின் பேரிலேயே செயல்படுவதால், தலைமை வழக்கறிஞர் மத்திய அமைச்சரவையின் நம்பிக்கையைப் பெற்றுள்ள வரை மட்டுமே பதவியில் இருப்பார்.",
        "tip": "The AG can be removed at any time without assigning reasons or holding an inquiry.",
        "fact": "Article 311 civil service protections do not apply to the Attorney General."
    },
    # 4
    {
        "stem_en": "Which of the following is a key institutional difference between the Attorney General of India and the Comptroller and Auditor General (CAG) of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞருக்கும் (AG), இந்திய தலைமை கணக்கு தணிக்கையாளருக்கும் (CAG) இடையிலான முக்கிய கட்டமைப்பு வேறுபாடு எது?",
        "options": [
            ("The AG has security of tenure like a SC Judge, whereas the CAG holds office during pleasure", "AG உச்ச நீதிமன்ற நீதிபதியைப் போல பதவிப் பாதுகாப்பு கொண்டவர்; CAG குடியரசுத் தலைவரின் விருப்பப்படி பதவியில் இருப்பவர்"),
            ("The CAG has security of tenure and removal by impeachment like a SC Judge, whereas the AG has no fixed tenure and holds office during the pleasure of the President", "CAG உச்ச நீதிமன்ற நீதிபதியைப் போல பதவிப் பாதுகாப்பும் கண்டனத் தீர்மான நீக்கமும் கொண்டவர்; ஆனால் AG-க்கு நிலையான பதவிக்காலம் இல்லை, குடியரசுத் தலைவர் விருப்பப்படி இருப்பவர்"),
            ("The CAG is appointed by the Prime Minister, whereas the AG is appointed by the President", "CAG பிரதமரால் நியமிக்கப்படுகிறார்; AG குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்"),
            ("The AG represents the State Governments, whereas the CAG represents the Union", "AG மாநில அரசுகளைப் பிரதிநிதித்துவப்படுத்துகிறார்; CAG மத்திய அரசைப் பிரதிநிதித்துவப்படுத்துகிறார்")
        ],
        "correct_idx": 1,
        "exp_en": "The CAG enjoys constitutional security of tenure (6 years or 65 years) and can only be removed via impeachment under Article 148(1). The Attorney General has no security of tenure and holds office at pleasure under Article 76(4).",
        "exp_ta": "CAG சரத்து 148(1)-ன் கீழ் 6 ஆண்டுகள் அல்லது 65 வயது வரை பதவிப் பாதுகாப்பும் கண்டனத் தீர்மான நீக்கமும் கொண்டவர்; ஆனால் தலைமை வழக்கறிஞருக்கு நிலையான பதவிக்காலம் இன்றி குடியரசுத் தலைவரின் விருப்பப்படி நீடிக்கிறார்.",
        "tip": "CAG is an independent constitutional watchdog; AG is the government's chief legal counsel.",
        "fact": "CAG salary is charged on the Consolidated Fund of India; AG remuneration is not."
    },
    # 5
    {
        "stem_en": "In what manner does the Attorney General of India differ from the Attorney General in the United Kingdom?",
        "stem_ta": "பிரிட்டனில் உள்ள தலைமை வழக்கறிஞரிடமிருந்து (UK AG) இந்திய தலைமை வழக்கறிஞர் எந்த வகையில் வேறுபடுகிறார்?",
        "options": [
            ("In the UK, the AG is a non-political civil servant, whereas in India he is a Cabinet Minister", "பிரிட்டனில் AG ஓர் அரசியல் சார்பற்ற அரசு ஊழியர்; இந்தியாவில் அவர் கேபினட் அமைச்சர்"),
            ("In the UK, the AG is an elected Member of Parliament and a member of the political Ministry, whereas in India he is a non-political jurist and NOT a member of the Cabinet", "பிரிட்டனில் AG தேர்ந்தெடுக்கப்பட்ட நாடாளுமன்ற உறுப்பினர் மற்றும் அமைச்சரவை உறுப்பினர்; இந்தியாவில் அவர் ஓர் அரசியல் சார்பற்ற சட்ட நிபுணர், கேபினட்டில் உறுப்பினர் அல்ல"),
            ("In the UK, the AG has no right to appear in court", "பிரிட்டனில் AG-க்கு நீதிமன்றத்தில் ஆஜராகும் உரிமை இல்லை"),
            ("In India, the AG cannot practice law privately, whereas in the UK he can", "இந்தியாவில் AG தனியார் தொழில் செய்ய முடியாது; பிரிட்டனில் முடியும்")
        ],
        "correct_idx": 1,
        "exp_en": "In Britain, the Attorney General is a politician, an elected MP, and a member of the Ministry/Cabinet. In India, following the Constitution, the AG is an independent non-political jurist and not a member of the Cabinet.",
        "exp_ta": "பிரிட்டனில் தலைமை வழக்கறிஞர் ஆளும் கட்சியின் நாடாளுமன்ற உறுப்பினர் மற்றும் அமைச்சரவை அமைச்சர் ஆவார்; இந்தியாவில் அவர் அரசியல் சார்பற்ற வழக்கறிஞர் ஆவார் மற்றும் கேபினட்டில் உறுப்பினர் அல்ல.",
        "tip": "In India, political executive leadership of the legal portfolio belongs to the Union Minister of Law and Justice.",
        "fact": "This separation ensures that independent constitutional advice is available to the President."
    },
    # 6
    {
        "stem_en": "Under Section 15 of the Contempt of Courts Act 1971, in which famous recent controversy did the Attorney General of India grant statutory consent to initiate criminal contempt proceedings against a public figure?",
        "stem_ta": "1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் பிரிவு 15-ன் கீழ், எந்த பிரபல சர்ச்சையில் உச்ச நீதிமன்றத்தில் குற்றவியல் அவமதிப்பு வழக்கை தொடர தலைமை வழக்கறிஞர் சட்டப்பூர்வ ஒப்புதல் அளித்தார்?",
        "options": [
            ("Against Prashant Bhushan in 2020", "2020-ல் பிரசாந்த் பூஷனுக்கு எதிராக"),
            ("Against stand-up comedian Kunal Kamra for tweets criticizing the Supreme Court (2020)", "உச்ச நீதிமன்றத்தை விமர்சித்து பதிவிட்டதற்காக நகைச்சுவை நடிகர் குணால் கம்ராவுக்கு எதிராக (2020)"),
            ("Against the Union Law Minister", "மத்திய சட்ட அமைச்சருக்கு எதிராக"),
            ("Against the Chief Election Commissioner", "தலைமை தேர்தல் ஆணையருக்கு எதிராக")
        ],
        "correct_idx": 1,
        "exp_en": "In November 2020, Attorney General K.K. Venugopal granted statutory consent under Section 15 of the Contempt of Courts Act 1971 to multiple petitioners to initiate criminal contempt against stand-up comedian Kunal Kamra.",
        "exp_ta": "2020 நவம்பரில், உச்ச நீதிமன்றத்தை விமர்சித்த வழக்கில் நகைச்சுவை நடிகர் குணால் கம்ரா மீது குற்றவியல் நீதிமன்ற அவமதிப்பு வழக்கை தொடர தலைமை வழக்கறிஞர் கே.கே. வேணுகோபால் சட்டப்பூர்வ ஒப்புதல் அளித்தார்.",
        "tip": "The AG acts as an impartial statutory gatekeeper under Section 15 to filter out frivolous contempt pleas.",
        "fact": "If the AG refuses consent, the petitioner cannot file a private criminal contempt petition in the Supreme Court."
    },
    # 7
    {
        "stem_en": "Under Section 23 of the Advocates Act 1961, what is the exact hierarchical order of pre-audience among Law Officers in Indian courts?",
        "stem_ta": "1961 வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 23-ன் கீழ், இந்திய நீதிமன்றங்களில் சட்ட அதிகாரிகளிடையே வழக்குகளில் வாதிடுவதற்கான முன்னுரிமை வரிசை (Pre-audience) என்ன?",
        "options": [
            ("Solicitor General -> Attorney General -> Additional Solicitors General", "சொலிசிட்டர் ஜெனரல் -> தலைமை வழக்கறிஞர் -> கூடுதல் சொலிசிட்டர் ஜெனரல்கள்"),
            ("Attorney General of India -> Solicitor General of India -> Additional Solicitors General", "இந்திய தலைமை வழக்கறிஞர் -> இந்திய சொலிசிட்டர் ஜெனரல் -> கூடுதல் சொலிசிட்டர் ஜெனரல்கள்"),
            ("Advocate General -> Attorney General -> Solicitor General", "மாநில தலைமை வழக்கறிஞர் -> இந்திய தலைமை வழக்கறிஞர் -> சொலிசிட்டர் ஜெனரல்"),
            ("Senior Advocates -> Attorney General -> Solicitor General", "மூத்த வழக்கறிஞர்கள் -> தலைமை வழக்கறிஞர் -> சொலிசிட்டர் ஜெனரல்")
        ],
        "correct_idx": 1,
        "exp_en": "Section 23 of the Advocates Act 1961 lays down the statutory order of pre-audience: (1) Attorney General of India, (2) Solicitor General of India, (3) Additional Solicitors General, followed by Advocates General of States.",
        "exp_ta": "1961 வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 23, நீதிமன்றங்களில் முன்னுரிமை வரிசையை வகுக்கிறது: (1) இந்திய தலைமை வழக்கறிஞர், (2) இந்திய சொலிசிட்டர் ஜெனரல், (3) கூடுதல் சொலிசிட்டர் ஜெனரல்கள், அதனைத் தொடர்ந்து மாநில தலைமை வழக்கறிஞர்கள்.",
        "tip": "Attorney General has absolute first precedence over every single lawyer in India.",
        "fact": "In Supreme Court hearings, the Attorney General is always given priority by the bench."
    },
    # 8
    {
        "stem_en": "Under Article 76(2), what kinds of legal duties can be assigned to the Attorney General of India?",
        "stem_ta": "சரத்து 76(2)-ன் கீழ், இந்திய தலைமை வழக்கறிஞருக்கு என்ன வகையான சட்டப் பணிகள் ஒப்படைக்கப்படலாம்?",
        "options": [
            ("Only drafting parliamentary speeches for ministers", "அமைச்சர்களுக்கு நாடாளுமன்ற உரைகளை வரைவது மட்டுமே"),
            ("Giving advice to GoI on legal matters, performing legal duties assigned by the President, and discharging functions conferred by the Constitution or any law", "சட்ட விவகாரங்களில் அரசுக்கு ஆலோசனை வழங்குதல், குடியரசுத் தலைவர் ஒப்படைக்கும் சட்டப் பணிகளை நிறைவேற்றுதல் மற்றும் அரசியலமைப்பு அல்லது பிற சட்டங்கள் வழங்கும் பணிகளை ஆற்றுதல்"),
            ("Appointing High Court judges", "உயர்நீதிமன்ற நீதிபதிகளை நியமிப்பது"),
            ("Auditing ministry expenditures", "அமைச்சகங்களின் செலவுகளை தணிக்கை செய்வது")
        ],
        "correct_idx": 1,
        "exp_en": "Article 76(2) defines three categories of duties: (1) advising GoI upon legal matters referred by President, (2) performing legal duties assigned by President, and (3) discharging functions conferred by the Constitution or enactments.",
        "exp_ta": "சரத்து 76(2) மூன்று கடமைகளை வரையறுக்கிறது: (1) குடியரசுத் தலைவர் அனுப்பும் சட்ட விவகாரங்களில் ஆலோசனை, (2) குடியரசுத் தலைவர் ஒப்படைக்கும் சட்டப் பணிகள், (3) அரசியலமைப்பு அல்லது பிற சட்டங்கள் வழங்கும் செயல்பாடுகளை ஆற்றுதல்.",
        "tip": "The President has specified duties under the Law Officers (Assignment of Duties) Rules.",
        "fact": "The AG represents the Government in cases of extraordinary constitutional importance."
    },
    # 9
    {
        "stem_en": "In which circumstance can the Attorney General of India represent a private client in a court of law?",
        "stem_ta": "எந்த சூழ்நிலையில் இந்திய தலைமை வழக்கறிஞர் நீதிமன்றத்தில் ஒரு தனியார் வாடிக்கையாளருக்காக ஆஜராகி வாதாட முடியும்?",
        "options": [
            ("In any civil dispute, provided the case is not against the Government of India and does not conflict with GoI's interests", "இந்திய அரசாங்கத்திற்கு எதிராக இல்லாத மற்றும் அரசின் நலன்களுக்கு முரண்படாத எந்தவொரு சிவில் வழக்கிலும்"),
            ("Never, private practice is completely prohibited by the Constitution", "எப்போதும் முடியாது, தனியார் தொழில் அரசியலமைப்பால் முற்றிலும் தடை செய்யப்பட்டுள்ளது"),
            ("Only in criminal appeals against the State", "அரசுக்கு எதிரான குற்றவியல் மேல்முறையீடுகளில் மட்டுமே"),
            ("Only when appointed as an arbitrator by the Supreme Court", "உச்ச நீதிமன்றத்தால் நடுவராக நியமிக்கப்படும் போது மட்டுமே")
        ],
        "correct_idx": 0,
        "exp_en": "The Attorney General is not barred from private legal practice. He can represent private clients in civil disputes as long as the Government of India is not an opposing party and his appearance does not conflict with Union interests.",
        "exp_ta": "தலைமை வழக்கறிஞருக்கு தனியார் தொழில் செய்ய தடை இல்லை. இந்திய அரசு எதிர் தரப்பாக இல்லாத மற்றும் அரசு நலன்களுக்கு முரண்படாத சிவில் வழக்குகளில் அவர் தனியார் வாடிக்கையாளர்களுக்காக ஆஜராகலாம்.",
        "tip": "Must not advise or hold brief against GoI; must not defend criminal accused without permission.",
        "fact": "Many illustrious AGs, including M.C. Setalvad and Soli Sorabjee, maintained distinguished private practices."
    },
    # 10
    {
        "stem_en": "What happens if a conflict of interest arises between the Attorney General's private practice and a matter concerning the Government of India?",
        "stem_ta": "தலைமை வழக்கறிஞரின் தனியார் வழக்கறிஞர் தொழிலுக்கும் இந்திய அரசாங்கம் தொடர்பான ஒரு விவகாரத்திற்கும் இடையே நலன் முரண்பாடு (Conflict of Interest) எழுந்தால் என்ன நிகழும்?",
        "options": [
            ("He must resign from the post of Attorney General immediately", "அவர் உடனடியாக தலைமை வழக்கறிஞர் பதவியை ராஜினாமா செய்ய வேண்டும்"),
            ("He must recuse himself from advising the government or appearing in that specific matter, and the matter is entrusted to the Solicitor General", "அவர் அந்த குறிப்பிட்ட வழக்கில் ஆஜராவதிலிருந்தோ அல்லது அரசுக்கு ஆலோசனை வழங்குவதிலிருந்தோ விலக வேண்டும்; அந்த விவகாரம் சொலிசிட்டர் ஜெனரலிடம் ஒப்படைக்கப்படும்"),
            ("The Government of India is barred from contesting the case", "இந்திய அரசாங்கம் அந்த வழக்கை நடத்த தடை விதிக்கப்படும்"),
            ("The private case is automatically dismissed by the court", "தனியார் வழக்கை நீதிமன்றம் தானாக தள்ளுபடி செய்யும்")
        ],
        "correct_idx": 1,
        "exp_en": "By professional ethics and Law Officers Rules, if a conflict of interest arises, the Attorney General recuses himself from the case, and the matter is conducted by the Solicitor General or an Additional Solicitor General.",
        "exp_ta": "நலன் முரண்பாடு ஏற்படும் சூழலில், தலைமை வழக்கறிஞர் அந்த வழக்கிலிருந்து தன்னை விடுவித்துக்கொள்வார் (Recusal); அந்த வழக்கை சொலிசிட்டர் ஜெனரல் அல்லது கூடுதல் சொலிசிட்டர் ஜெனரல் நடத்துவர்.",
        "tip": "Standard legal ethics doctrine of recusal applies to all law officers.",
        "fact": "This occurred during the 2G spectrum case and Coal allocation case in the Supreme Court."
    },
    # 11
    {
        "stem_en": "Which landmark historical case established that the opinion given by the Attorney General to the Government of India is protected by professional privilege under the Indian Evidence Act 1872?",
        "stem_ta": "இந்திய சாட்சியச் சட்டம் 1872-ன் கீழ், தலைமை வழக்கறிஞர் இந்திய அரசுக்கு அளிக்கும் சட்ட ஆலோசனை தொழில்முறை சிறப்புரிமைப் பாதுகாப்பு (Professional Privilege) பெற்றது என எந்த வழக்கு உறுதிப்படுத்தியது?",
        "options": [
            ("ADM Jabalpur case (1976)", "ஏடிஎம் ஜபல்பூர் வழக்கு (1976)"),
            ("State of Uttar Pradesh v. Raj Narain (1975)", "உத்தரப் பிரதேச அரசு எதிர் ராஜ் நாராயண் (1975)"),
            ("S.P. Gupta v. Union of India (1981)", "எஸ்.பி. குப்தா எதிர் இந்திய ஒன்றியம் (1981)"),
            ("Minerva Mills case (1980)", "மினர்வா மில்ஸ் வழக்கு (1980)")
        ],
        "correct_idx": 1,
        "exp_en": "In State of UP v. Raj Narain (1975) and subsequent rulings, legal advice given by the Attorney General to the Government is recognized as confidential privileged communication between counsel and client under Section 126 of the Evidence Act.",
        "exp_ta": "1975-ல் ராஜ் நாராயண் வழக்கில், சாட்சியச் சட்டம் பிரிவு 126-ன் கீழ் அரசுக்கும் தலைமை வழக்கறிஞருக்கும் இடையிலான சட்ட ஆலோசனைகள் தொழில்முறை சிறப்புரிமைப் பாதுகாப்பு கொண்டவை என உறுதிப்படுத்தப்பட்டது.",
        "tip": "Section 126 of Indian Evidence Act protects attorney-client privileged communications.",
        "fact": "However, under RTI Act, legal advice may be disclosed if larger public interest warrants it."
    },
    # 12
    {
        "stem_en": "Under Article 88, can the Attorney General of India be appointed as the Chairman of a Parliamentary Committee?",
        "stem_ta": "சரத்து 88-ன் கீழ், இந்திய தலைமை வழக்கறிஞர் ஒரு நாடாளுமன்றக் குழுவின் தலைவராக நியமிக்கப்பட முடியுமா?",
        "options": [
            ("Yes, of any committee including Public Accounts Committee", "ஆம், பொதுக் கணக்குக் குழு உட்பட எந்தக் குழுவிற்கும்"),
            ("No, he can only be named a member to participate and speak, but cannot be Chairman or cast a vote", "இல்லை, அவர் பங்கேற்கவும் பேசவும் மட்டுமே உறுப்பினராக நியமிக்கப்படலாம்; தலைவராகவோ அல்லது வாக்களிக்கவோ முடியாது"),
            ("Only with the consent of the Chief Justice of India", "தலைமை நீதிபதியின் ஒப்புதலுடன் மட்டுமே"),
            ("Only in Joint Parliamentary Committees on finance", "நிதி தொடர்பான நாடாளுமன்றக் கூட்டுக்குழுக்களில் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Since the AG is not a Member of Parliament and lacks voting rights under Article 88, he cannot be appointed Chairman of a parliamentary committee. He participates purely in an advisory, non-voting capacity.",
        "exp_ta": "தலைமை வழக்கறிஞர் நாடாளுமன்ற உறுப்பினர் அல்ல என்பதாலும் அவருக்கு வாக்குரிமை இல்லை என்பதாலும், அவர் நாடாளுமன்றக் குழுவின் தலைவராக நியமிக்கப்பட முடியாது; வெறும் ஆலோசனை உறுப்பினராகவே செயல்பட முடியும்.",
        "tip": "Committee Chairmen must be Members of Parliament who hold voting power.",
        "fact": "Parliamentary rules (Rule 258 of Lok Sabha Rules) require Committee Chairmen to be members of the House."
    },
    # 13
    {
        "stem_en": "Who among the following Attorneys General of India served during the landmark Kesavananda Bharati case (1973) and the Emergency-era ADM Jabalpur case (1976)?",
        "stem_ta": "வரலாற்று சிறப்புமிக்க கேசவானந்த பாரதி வழக்கு (1973) மற்றும் அவசரநிலைக் கால ஏடிஎம் ஜபல்பூர் வழக்கு (1976) ஆகிய இரண்டிலும் ஆஜரான இந்திய தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Niren De", "நிரேன் டே"),
            ("C.K. Daphtary", "சி.கே. தப்தாரி"),
            ("S.V. Gupte", "எஸ்.வி. குப்தே")
        ],
        "correct_idx": 1,
        "exp_en": "Niren De served as the 3rd Attorney General of India from November 1968 to March 1977, appearing for the Government of India in both Kesavananda Bharati (1973) and ADM Jabalpur (1976).",
        "exp_ta": "நிரேன் டே 1968 முதல் 1977 வரை இந்தியாவின் 3-வது தலைமை வழக்கறிஞராக பணியாற்றி, கேசவானந்த பாரதி (1973) மற்றும் ஏடிஎம் ஜபல்பூர் (1976) ஆகிய இரு முக்கிய வழக்குகளிலும் அரசுக்காக ஆஜரானார்.",
        "tip": "Niren De had earlier served as Additional Solicitor General and Solicitor General.",
        "fact": "He resigned immediately after the defeat of the Indira Gandhi government in March 1977."
    },
    # 14
    {
        "stem_en": "In 1962, what proposal was mooted by Prime Minister Jawaharlal Nehru regarding the office of the Attorney General, which was ultimately dropped due to widespread opposition?",
        "stem_ta": "1962-ல் பிரதமர் ஜவஹர்லால் நேருவால் தலைமை வழக்கறிஞர் பதவி குறித்து முன்வைக்கப்பட்டு, கடும் எதிர்ப்பு காரணமாக கைவிடப்பட்ட திட்டம் என்ன?",
        "options": [
            ("Abolishing the office of Attorney General completely", "தலைமை வழக்கறிஞர் பதவியை முற்றிலும் ரத்து செய்வது"),
            ("Merging the office of the Attorney General with that of the Union Minister of Law", "தலைமை வழக்கறிஞர் பதவியை மத்திய சட்ட அமைச்சர் பதவியுடன் இணைப்பது"),
            ("Making the Chief Justice of India the ex-officio Attorney General", "இந்திய தலைமை நீதிபதியை பதவிவழி தலைமை வழக்கறிஞராக மாற்றுவது"),
            ("Restricting the AG's audience to High Courts only", "தலைமை வழக்கறிஞரை உயர்நீதிமன்றங்களுக்கு மட்டுமே மட்டுப்படுத்துவது")
        ],
        "correct_idx": 1,
        "exp_en": "In late 1962, the Nehru government proposed merging the office of the Attorney General with the Union Law Minister (mirroring the British model). However, following fierce opposition from the Bar and Parliament, the proposal was dropped.",
        "exp_ta": "1962-ல் பிரிட்டன் மாதிரியைப் போல தலைமை வழக்கறிஞர் பதவியை மத்திய சட்ட அமைச்சர் பதவியுடன் இணைக்க நேரு அரசு திட்டமிட்டது; ஆனால் வழக்கறிஞர்கள் மற்றும் நாடாளுமன்றத்தின் கடும் எதிர்ப்பால் அது கைவிடப்பட்டது.",
        "tip": "M.C. Setalvad opposed this merger, asserting that the AG must remain an independent professional counsel.",
        "fact": "Setalvad resigned in March 1963 following the controversy."
    },
    # 15
    {
        "stem_en": "Can the Attorney General of India initiate suo motu criminal contempt proceedings in the Supreme Court without any petition?",
        "stem_ta": "எந்த மனுவும் இன்றி உச்ச நீதிமன்றத்தில் தலைமை வழக்கறிஞர் தானாக முன்வந்து (Suo Motu) குற்றவியல் நீதிமன்ற அவமதிப்பு நடவடிக்கையை தொடங்க முடியுமா?",
        "options": [
            ("No, only private citizens can file contempt petitions", "இல்லை, தனிநபர்கள் மட்டுமே அவமதிப்பு மனு தாக்கல் செய்ய முடியும்"),
            ("Yes, under Section 15(1)(a) of the Contempt of Courts Act 1971, the AG can make a motion on his own relation", "ஆம், 1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் பிரிவு 15(1)(a)-ன் கீழ் தலைமை வழக்கறிஞர் தானாக முன்வந்து மனு தாக்கல் செய்யலாம்"),
            ("Only after prior permission of the President", "குடியரசுத் தலைவரின் முன்அனுமதி பெற்ற பிறகு மட்டுமே"),
            ("Only during vacation sittings", "நீதிமன்ற விடுமுறை காலங்களில் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Section 15(1)(a) of the Contempt of Courts Act 1971 explicitly authorizes the Attorney General to bring a motion for criminal contempt in the Supreme Court on his own relation, without needing any private petitioner.",
        "exp_ta": "1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் பிரிவு 15(1)(a), தலைமை வழக்கறிஞர் யாருடைய மனுவும் இன்றி தானாக முன்வந்து உச்ச நீதிமன்றத்தில் குற்றவியல் அவமதிப்பு நடவடிக்கையை தொடங்க முழு அதிகாரம் அளிக்கிறது.",
        "tip": "AG is the guardian of the court's dignity as leader of the Bar.",
        "fact": "The Advocate General of a State enjoys identical powers before the High Court under Section 15(1)(a)."
    },
    # 16
    {
        "stem_en": "Who among the following served as the Attorney General of India during the Prime Ministership of Atal Bihari Vajpayee and argued the landmark Presidential Reference on Special Courts?",
        "stem_ta": "அடல் பிகாரி வாஜ்பாய் பிரதமராக இருந்த காலத்தில் தலைமை வழக்கறிஞராக பணியாற்றியவர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Soli Sorabjee", "சோலி சோராப்ஜி"),
            ("Niren De", "நிரேன் டே"),
            ("C.K. Daphtary", "சி.கே. தப்தாரி")
        ],
        "correct_idx": 1,
        "exp_en": "Soli Sorabjee served as the 11th Attorney General of India during the entire tenure of the NDA government led by Prime Minister Atal Bihari Vajpayee from April 1998 to June 2004.",
        "exp_ta": "சோலி சோராப்ஜி 1998 ஏப்ரல் முதல் 2004 ஜூன் வரை பிரதமர் வாஜ்பாய் தலைமையிலான தேசிய ஜனநாயகக் கூட்டணி ஆட்சிக் காலம் முழுவதும் 11-வது தலைமை வழக்கறிஞராக பணியாற்றினார்.",
        "tip": "Soli Sorabjee was renowned internationally as a champion of human rights and free expression.",
        "fact": "He was appointed Special Rapporteur for Nigeria by the United Nations Human Rights Commission in 1997."
    },
    # 17
    {
        "stem_en": "Under the Law Officers (Conditions of Service) Rules 1987, who is the administrative disciplinary authority governing the conduct of the Attorney General of India?",
        "stem_ta": "1987 சட்ட அதிகாரிகள் விதிகளின் கீழ், தலைமை வழக்கறிஞரின் நடத்தை மற்றும் பணிகளை ஒழுங்குபடுத்தும் நிர்வாக ஒழுங்கு நடவடிக்கை அதிகாரம் யாருக்கு உள்ளது?",
        "options": [
            ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("Government of India (Ministry of Law and Justice)", "இந்திய அரசாங்கம் (மத்திய சட்டம் மற்றும் நீதித்துறை அமைச்சகம்)"),
            ("Bar Council of India exclusively", "இந்திய பார் கவுன்சிலுக்கு மட்டுமே"),
            ("Speaker of Lok Sabha", "மக்களவை சபாநாயகர்")
        ],
        "correct_idx": 1,
        "exp_en": "The Ministry of Law and Justice (Department of Legal Affairs) is the administrative ministry that regulates the conditions of service, assignments, and retainership of the Attorney General.",
        "exp_ta": "மத்திய சட்டம் மற்றும் நீதித்துறை அமைச்சகம் (சட்ட விவகாரங்கள் துறை), தலைமை வழக்கறிஞரின் பணி நிபந்தனைகள், பணிகள் மற்றும் கட்டணங்களை நிர்வகிக்கும் நிர்வாக அமைச்சகமாகும்.",
        "tip": "Law Officers Rules 1987 are executive rules framed by the central government.",
        "fact": "The AG coordinates through the Law Secretary on government litigation matters."
    },
    # 18
    {
        "stem_en": "In the landmark Third Judges Case (Special Reference 1 of 1998), who represented the Union of India as the Attorney General before the 9-judge Supreme Court Bench?",
        "stem_ta": "மூன்றாவது நீதிபதிகள் வழக்கில் (சிறப்பு ஆலோசனைக் குறிப்பு 1998), 9 நீதிபதிகள் கொண்ட உச்ச நீதிமன்ற அமர்வின் முன் இந்திய அரசுக்காக ஆஜரான தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Soli Sorabjee", "சோலி சோராப்ஜி"),
            ("K. Parasaran", "கே. பராசரன்"),
            ("Ashok Desai", "அசோக் தேசாய்")
        ],
        "correct_idx": 1,
        "exp_en": "Attorney General Soli Sorabjee represented the Government of India in the Third Judges Case (1998), where President K.R. Narayanan sought an advisory opinion under Article 143 on the collegium system.",
        "exp_ta": "குடியரசுத் தலைவர் கே.ஆர். நாராயணன் கொலீஜியம் முறை குறித்து சரத்து 143-ன் கீழ் ஆலோசனை கோரிய மூன்றாவது நீதிபதிகள் வழக்கில் (1998), அரசுக்காக தலைமை வழக்கறிஞர் சோலி சோராப்ஜி ஆஜரானார்.",
        "tip": "Third Judges case expanded the CJI collegium to CJI + 4 senior-most judges.",
        "fact": "The AG argued that the executive must have an effective voice in judicial appointments."
    },
    # 19
    {
        "stem_en": "What is the constitutional significance of Article 105(4) with respect to the Attorney General of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞரைப் பொறுத்தவரை அரசியலமைப்பின் சரத்து 105(4)-ன் அரசியலமைப்பு முக்கியத்துவம் என்ன?",
        "options": [
            ("It confers voting rights in parliamentary divisions", "நாடாளுமன்ற வாக்கெடுப்பில் அவருக்கு வாக்குரிமை வழங்குகிறது"),
            ("It extends all parliamentary privileges, freedom of speech, and immunities enjoyed by MPs to the Attorney General while participating in Parliament", "நாடாளுமன்றத்தில் பங்கேற்கும் போது, எம்.பி-க்களுக்கு உள்ள பேச்சு சுதந்திரம் மற்றும் சிறப்புரிமைகளை தலைமை வழக்கறிஞருக்கும் நீட்டிக்கிறது"),
            ("It makes the AG immune from criminal trial permanently", "அவரை குற்றவியல் விசாரணையிலிருந்து நிரந்தரமாக விடுவிக்கிறது"),
            ("It grants him the salary of a Cabinet Minister", "அவருக்கு கேபினட் அமைச்சரின் ஊதியத்தை வழங்குகிறது")
        ],
        "correct_idx": 1,
        "exp_en": "Article 105(4) extends parliamentary privileges—including absolute freedom of speech in Parliament under Article 105(1) and immunity from court proceedings under Article 105(2)—to persons who have the right to speak, including the AG.",
        "exp_ta": "சரத்து 105(4), நாடாளுமன்றத்தில் பேச உரிமையுள்ள தலைமை வழக்கறிஞருக்கும் சரத்து 105(1) மற்றும் 105(2)-ன் கீழ் எம்.பி-க்களுக்கு உள்ள முழுமையான பேச்சு சுதந்திரம் மற்றும் நீதிமன்ற பாதுகாப்பை வழங்குகிறது.",
        "tip": "He cannot be questioned in any court for statements made on the floor of the House.",
        "fact": "However, he is bound by the rules of procedure and conduct of business enforced by the Speaker/Chairman."
    },
    # 20
    {
        "stem_en": "Can the Attorney General of India advise any statutory public corporation or autonomous agency against the Government of India?",
        "stem_ta": "இந்திய அரசாங்கத்திற்கு எதிராக ஏதேனும் ஒரு சட்டப்பூர்வ பொதுத்துறை நிறுவனம் அல்லது தன்னாட்சி அமைப்புக்கு இந்திய தலைமை வழக்கறிஞர் ஆலோசனை வழங்க முடியுமா?",
        "options": [
            ("Yes, public corporations are independent legal entities", "ஆம், பொதுத்துறை நிறுவனங்கள் சுயாதீன சட்ட அமைப்புகள் என்பதால்"),
            ("No, he cannot advise any party or entity where the interests of the Government of India are adverse or likely to be affected", "இல்லை, இந்திய அரசாங்கத்தின் நலன்கள் பாதிக்கப்படக்கூடிய அல்லது முரண்படக்கூடிய எந்தவொரு தரப்பிற்கும் அவர் ஆலோசனை வழங்க முடியாது"),
            ("Only if permitted by the Supreme Court", "உச்ச நீதிமன்றம் அனுமதித்தால் மட்டுமே"),
            ("Only in arbitration matters", "நடுவர் மன்ற விவகாரங்களில் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "The Attorney General is barred from advising any ministry, public statutory corporation, or private entity against the Government of India, maintaining undivided loyalty to the Union executive.",
        "exp_ta": "இந்திய அரசாங்கத்திற்கு எதிராக எந்தவொரு அமைச்சகத்திற்கோ, பொதுத்துறை நிறுவனத்திற்கோ அல்லது தனியார் அமைப்பிற்கோ தலைமை வழக்கறிஞர் ஆலோசனை வழங்க முடியாது.",
        "tip": "Undivided loyalty to the Union of India is the cornerstone of the Attorney General's office.",
        "fact": "If two government departments have a dispute, the AG advises through the Cabinet Secretariat."
    },
    # 21
    {
        "stem_en": "Under Article 76, can an advocate who has practiced in High Courts for 9 years and 11 months be appointed as the Attorney General of India?",
        "stem_ta": "சரத்து 76-ன் கீழ், உயர்நீதிமன்றங்களில் 9 ஆண்டுகள் 11 மாதங்கள் வழக்கறிஞராகப் பணியாற்றிய ஒருவரை இந்திய தலைமை வழக்கறிஞராக நியமிக்க முடியுமா?",
        "options": [
            ("Yes, because 10 years is only an approximate guideline", "ஆம், 10 ஆண்டுகள் என்பது தோராயமான வழிகாட்டுதல் மட்டுமே என்பதால்"),
            ("No, unless he is an eminent jurist in the opinion of the President or has 5 years experience as a High Court judge, because the 10-year advocate requirement is strict", "குடியரசுத் தலைவரின் பார்வையில் சிறந்த சட்ட அறிஞராகவோ அல்லது 5 ஆண்டு உயர்நீதிமன்ற நீதிபதியாகவோ இருந்தாலன்றி முடியாது; ஏனெனில் 10 ஆண்டு வழக்கறிஞர் அனுபவம் கட்டாயமாகும்"),
            ("Yes, with the approval of the Bar Council", "ஆம், பார் கவுன்சிலின் ஒப்புதலுடன்"),
            ("Yes, with Chief Justice of India's relaxation", "ஆம், தலைமை நீதிபதியின் தளர்வு மூலம்")
        ],
        "correct_idx": 1,
        "exp_en": "Under Article 124(3)(b), the requirement of being an advocate of a High Court for 'at least ten years' is a strict constitutional threshold. A person with 9 years 11 months is ineligible unless qualified under the 5-year judge or 'eminent jurist' clause.",
        "exp_ta": "சரத்து 124(3)(b)-ன் கீழ் 'குறைந்தது பத்து ஆண்டுகள்' வழக்கறிஞர் அனுபவம் என்பது கட்டாய வரம்பாகும். எனவே 5 ஆண்டு நீதிபதி அனுபவம் அல்லது 'சிறந்த சட்ட அறிஞர்' பிரிவில் தகுதி பெற்றாலன்றி 9 ஆண்டுகள் 11 மாதங்கள் அனுபவம் கொண்டவரை நியமிக்க முடியாது.",
        "tip": "Constitutional qualification thresholds are strict and cannot be relaxed administratively.",
        "fact": "Cumulative practice across two or more High Courts in succession is counted towards the 10-year period."
    },
    # 22
    {
        "stem_en": "Who was the Attorney General of India during the tenure of Prime Minister Rajiv Gandhi who argued the Union Carbide Bhopal Gas Disaster litigation?",
        "stem_ta": "பிரதமர் ராஜீவ் காந்தியின் ஆட்சிக் காலத்தில் போபால் விஷவாயு கசிவு வழக்கில் மத்திய அரசுக்காக வாதிட்ட இந்திய தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("K. Parasaran", "கே. பராசரன்"),
            ("Niren De", "நிரேன் டே"),
            ("G.E. Vahanvati", "ஜி.இ. வாகனவதி")
        ],
        "correct_idx": 1,
        "exp_en": "Senior Advocate K. Parasaran served as Attorney General of India from 1983 to 1989, leading the Government of India's legal battle in the Bhopal Gas Leak disaster and defending the Bhopal Gas Leak Disaster (Processing of Claims) Act 1985.",
        "exp_ta": "கே. பராசரன் 1983 முதல் 1989 வரை தலைமை வழக்கறிஞராக பணியாற்றி, போபால் விஷவாயு பேரழிவு வழக்கில் இந்திய அரசாங்கத்தின் சார்பில் முன்னின்று வாதாடினார்.",
        "tip": "The Supreme Court upheld the constitutional validity of the Bhopal Gas Act in Charan Lal Sahu v. UOI (1989).",
        "fact": "K. Parasaran also successfully represented the Union in the famous Indian Express newspapers case."
    },
    # 23
    {
        "stem_en": "What is the primary difference between the constitutional functions of the Attorney General of India and the Advocate General of a State regarding territorial right of audience?",
        "stem_ta": "நீதிமன்றங்களில் முன்னிலையாகும் பிராந்திய வரம்பு (Territorial Right of Audience) தொடர்பாக அட்டர்னி ஜெனரலுக்கும் அட்வகேட் ஜெனரலுக்கும் இடையிலான முக்கிய வேறுபாடு என்ன?",
        "options": [
            ("The AG of India has the right of audience in all courts in India, whereas the Advocate General has the right of audience in all courts within that State", "இந்திய AG-க்கு இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் முன்னிலையாகும் உரிமை உண்டு; ஆனால் அட்வகேட் ஜெனரலுக்கு அந்த மாநில எல்லைக்குள் உள்ள நீதிமன்றங்களில் மட்டுமே முன்னிலையாகும் உரிமை உண்டு"),
            ("Neither has any territorial right of audience", "இருவருக்கும் நீதிமன்றங்களில் முன்னிலையாகும் உரிமை இல்லை"),
            ("Advocate General has wider jurisdiction than the Attorney General", "அட்வகேட் ஜெனரலுக்கு AG-யை விட விரிவான அதிகார வரம்பு உண்டு"),
            ("The AG of India can only appear in the Supreme Court", "இந்திய AG உச்ச நீதிமன்றத்தில் மட்டுமே ஆஜராக முடியும்")
        ],
        "correct_idx": 0,
        "exp_en": "Under Article 76(3), the Attorney General has the right of audience in all courts across the entire territory of India. Under Article 165(3), the Advocate General's constitutional right of audience is restricted to courts within that State.",
        "exp_ta": "சரத்து 76(3)-ன் படி இந்திய தலைமை வழக்கறிஞருக்கு நாடு முழுவதும் உள்ள அனைத்து நீதிமன்றங்களிலும் உரிமை உண்டு; ஆனால் சரத்து 165(3)-ன் படி மாநில தலைமை வழக்கறிஞருக்கு அந்த மாநில எல்லைக்குட்பட்ட நீதிமன்றங்களிலேயே முன்னுரிமை உண்டு.",
        "tip": "AG = Pan-India jurisdiction; Advocate General = Intra-State jurisdiction.",
        "fact": "However, an Advocate General can be specially briefed to appear in the Supreme Court in New Delhi for the State."
    },
    # 24
    {
        "stem_en": "Can the Attorney General of India appear in the Supreme Court on behalf of a State Government without the permission of the Government of India?",
        "stem_ta": "இந்திய அரசாங்கத்தின் அனுமதியின்றி உச்ச நீதிமன்றத்தில் ஒரு மாநில அரசாங்கத்தின் சார்பில் தலைமை வழக்கறிஞர் ஆஜராகி வாதாட முடியுமா?",
        "options": [
            ("Yes, States are part of the Union", "ஆம், மாநிலங்கள் ஒன்றியத்தின் ஒரு பகுதி என்பதால்"),
            ("No, he cannot appear for any State Government or entity in matters where the interests of the Union and the State may conflict without GoI consent", "இல்லை, மத்திய அரசின் நலன்களுக்கு முரண்படக்கூடிய விவகாரங்களில் மத்திய அரசின் அனுமதியின்றி எந்த மாநில அரசுக்காகவும் அவர் ஆஜராக முடியாது"),
            ("Only in water dispute tribunals", "நதிநீர் தீர்ப்பாயங்களில் மட்டுமே"),
            ("Only if the State Chief Minister requests in writing", "மாநில முதல்வர் எழுத்துப்பூர்வமாக கோரினால் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under executive guidelines, the Attorney General cannot hold a brief for any State Government against the Union of India or in any matter where the Union's interests may be compromised, without prior approval.",
        "exp_ta": "மத்திய அரசின் நலன்களுக்கு முரண்படக்கூடிய வழக்குகளில் அல்லது மத்திய அரசுக்கு எதிரான விவகாரங்களில் முன்அனுமதி இன்றி எந்தவொரு மாநில அரசுக்காகவும் தலைமை வழக்கறிஞர் ஆஜராக முடியாது.",
        "tip": "His primary client and constitutional master is the Government of India.",
        "fact": "If Union and State have identical interests, the AG may represent both with consent."
    },
    # 25
    {
        "stem_en": "In the historic S.R. Bommai v. Union of India (1994) case concerning Article 356, who represented the Union of India as the Attorney General?",
        "stem_ta": "சரத்து 356 (குடியரசுத் தலைவர் ஆட்சி) தொடர்பான வரலாற்று சிறப்புமிக்க எஸ்.ஆர். பொம்மை வழக்கில் (1994) மத்திய அரசுக்காக ஆஜரான இந்திய தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Milon K. Banerjee", "மிலன் கே. பானர்ஜி"),
            ("K. Parasaran", "கே. பராசரன்"),
            ("Soli Sorabjee", "சோலி சோராப்ஜி")
        ],
        "correct_idx": 1,
        "exp_en": "Senior Advocate Milon K. Banerjee served as Attorney General of India from 1992 to 1996 under Prime Minister P.V. Narasimha Rao and represented the Union of India in the 9-judge bench ruling in S.R. Bommai (1994).",
        "exp_ta": "மிலன் கே. பானர்ஜி 1992 முதல் 1996 வரை நரசிம்ம ராவ் ஆட்சியில் தலைமை வழக்கறிஞராக பணியாற்றி, 9 நீதிபதிகள் கொண்ட எஸ்.ஆர். பொம்மை வழக்கில் (1994) மத்திய அரசுக்காக ஆஜரானார்.",
        "tip": "S.R. Bommai established that federalism and secularism are part of the Basic Structure.",
        "fact": "Milon K. Banerjee later served a second term as AG from 2004 to 2009 under Dr. Manmohan Singh."
    },
    # 26
    {
        "stem_en": "Who was the first Attorney General of India belonging to the Parsi community, who served two landmark terms?",
        "stem_ta": "இரு முக்கிய காலகட்டங்களில் இந்திய தலைமை வழக்கறிஞராக பணியாற்றிய பார்சி சமூகத்தைச் சேர்ந்த முதல் சட்ட நிபுணர் யார்?",
        "options": [
            ("Fali S. Nariman", "பாலி எஸ். நாரிமன்"),
            ("Soli J. Sorabjee", "சோலி ஜே. சோராப்ஜி"),
            ("Nanabhoy Palkhivala", "நானாபாய் பால்கிவாலா"),
            ("C.K. Daphtary", "சி.கே. தப்தாரி")
        ],
        "correct_idx": 1,
        "exp_en": "Soli J. Sorabjee was the distinguished jurist from the Parsi community who served as the Attorney General of India twice (1989-1990 and 1998-2004).",
        "exp_ta": "பார்சி சமூகத்தைச் சேர்ந்த புகழ்பெற்ற சட்ட வல்லுநரான சோலி ஜே. சோராப்ஜி, இருமுறை (1989-1990 மற்றும் 1998-2004) இந்திய தலைமை வழக்கறிஞராக பணியாற்றினார்.",
        "tip": "Fali S. Nariman served as Additional Solicitor General but never served as Attorney General.",
        "fact": "Nani Palkhivala declined offers to serve as Attorney General and Supreme Court Judge."
    },
    # 27
    {
        "stem_en": "Who among the following was the first person to hold the office of Solicitor General of India upon its creation in 1950?",
        "stem_ta": "1950-ல் இந்திய சொலிசிட்டர் ஜெனரல் அலுவலகம் உருவாக்கப்பட்டபோது, அப்பதவியை வகித்த முதல் நபர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("C.K. Daphtary", "சி.கே. தப்தாரி"),
            ("H.N. Sanyal", "ஹெச்.என். சன்யால்"),
            ("S.V. Gupte", "எஸ்.வி. குப்தே")
        ],
        "correct_idx": 1,
        "exp_en": "Chander Kishan Daphtary (C.K. Daphtary) was the first Solicitor General of India from 1950 to 1963, and subsequently became the 2nd Attorney General of India (1963-1968) succeeding M.C. Setalvad.",
        "exp_ta": "சந்தர் கிஷன் தப்தாரி (சி.கே. தப்தாரி) 1950 முதல் 1963 வரை இந்தியாவின் முதல் சொலிசிட்டர் ஜெனரலாக பணியாற்றினார்; பின்னர் செதல்வாட்டுக்கு பிறகு 2-வது தலைமை வழக்கறிஞராக (1963-1968) உயர்ந்தார்.",
        "tip": "C.K. Daphtary served as 1st Solicitor General and then 2nd Attorney General.",
        "fact": "He was awarded the Padma Vibhushan in 1967."
    },
    # 28
    {
        "stem_en": "Which Attorney General of India appeared for the Central Government in the Aadhaar constitutional challenge (Justice K.S. Puttaswamy case)?",
        "stem_ta": "ஆதார் சட்டத்தின் அரசியலமைப்பு செல்லுபடியை எதிர்த்த புட்டசுவாமி வழக்கில் மத்திய அரசுக்காக ஆஜரான இந்திய தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("Mukul Rohatgi and K.K. Venugopal", "முகுல் ரோஹத்கி மற்றும் கே.கே. வேணுகோபால்"),
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("G.E. Vahanvati", "ஜி.இ. வாகனவதி"),
            ("Milon Banerjee", "மிலன் பானர்ஜி")
        ],
        "correct_idx": 0,
        "exp_en": "Mukul Rohatgi argued the preliminary privacy reference (2015-2017), and K.K. Venugopal argued the final Aadhaar constitutional validity case before the 5-judge bench in 2017-2018.",
        "exp_ta": "ஆதார் வழக்கின் ஆரம்ப கட்டத்தில் முகுல் ரோஹத்கியும், பின்னர் 5 நீதிபதிகள் கொண்ட அமர்வின் இறுதி விசாரணையில் கே.கே. வேணுகோபாலும் மத்திய அரசுக்காக தலைமை வழக்கறிஞராக ஆஜரானார்கள்.",
        "tip": "9-judge bench declared Right to Privacy a fundamental right under Article 21 in August 2017.",
        "fact": "The 5-judge bench upheld the Aadhaar Act with certain struck-down provisions in September 2018."
    },
    # 29
    {
        "stem_en": "Can the Attorney General of India be called upon by the Supreme Court to act as 'Amicus Curiae' in matters of grave public importance?",
        "stem_ta": "பொது முக்கியத்துவம் வாய்ந்த விவகாரங்களில் உச்ச நீதிமன்றத்திற்கு உதவும் 'நீதிமன்றத் தோழராக' (Amicus Curiae) தலைமை வழக்கறிஞரை நீதிமன்றம் அழைக்க முடியுமா?",
        "options": [
            ("No, the AG can only represent the Government of India", "இல்லை, தலைமை வழக்கறிஞர் அரசுக்காக மட்டுமே ஆஜராக முடியும்"),
            ("Yes, the Supreme Court frequently requests the Attorney General to assist the Court as Amicus Curiae in complex constitutional issues", "ஆம், சிக்கலான அரசியலமைப்பு விவகாரங்களில் நீதிமன்றத்திற்கு உதவ அமிக்கஸ் கியூரியாக ஆஜராகுமாறு உச்ச நீதிமன்றம் அடிக்கடி கேட்டுக்கொள்கிறது"),
            ("Only in civil appeals from High Courts", "உயர்நீதிமன்ற சிவில் மேல்முறையீடுகளில் மட்டுமே"),
            ("Only if permitted by Parliament", "நாடாளுமன்றம் அனுமதித்தால் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "The Supreme Court often requests the Attorney General as the leader of the Bar to assist the court as an independent 'Amicus Curiae' (friend of the court) on intricate constitutional questions.",
        "exp_ta": "பார் கவுன்சிலின் தலைவர் என்ற முறையில், சிக்கலான அரசியலமைப்பு மற்றும் சட்டப் பிரச்சனைகளில் நீதிமன்றத்திற்கு உதவ 'அமிக்கஸ் கியூரி'யாக (நீதிமன்றத் தோழர்) ஆஜராகுமாறு உச்ச நீதிமன்றம் தலைமை வழக்கறிஞரை அழைக்கிறது.",
        "tip": "Amicus Curiae means 'friend of the court' who acts impartially.",
        "fact": "In such cases, the AG assists the court independently of the party positions."
    },
    # 30
    {
        "stem_en": "Under Article 76(1), can a person who has NEVER practiced as an advocate in any High Court be appointed as the Attorney General of India?",
        "stem_ta": "சரத்து 76(1)-ன் கீழ், எந்த உயர்நீதிமன்றத்திலும் வழக்கறிஞராகப் பணியாற்றாத ஒருவரை இந்திய தலைமை வழக்கறிஞராக நியமிக்க முடியுமா?",
        "options": [
            ("No, 10 years practice as an advocate is an absolute requirement", "இல்லை, 10 ஆண்டுகள் வழக்கறிஞர் தொழில் கட்டாயத் தேவை"),
            ("Yes, if he has served as a Judge of a High Court for at least 5 years, or is an eminent jurist in the opinion of the President", "ஆம், அவர் குறைந்தது 5 ஆண்டுகள் உயர்நீதிமன்ற நீதிபதியாக பணியாற்றியிருந்தால் அல்லது குடியரசுத் தலைவரின் பார்வையில் சிறந்த சட்ட அறிஞராக இருந்தால்"),
            ("Only if he is a retired Chief Justice of India", "அவர் ஓய்வுபெற்ற இந்திய தலைமை நீதிபதியாக இருந்தால் மட்டுமே"),
            ("Only if he has a doctorate in law from abroad", "அவர் வெளிநாட்டில் சட்ட முனைவர் பட்டம் பெற்றிருந்தால் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under Article 124(3), the qualifications for a Supreme Court judge are in the alternative: (a) 5 years HC judge, OR (b) 10 years HC advocate, OR (c) eminent jurist. Hence, a person who was a HC judge for 5 years or an eminent jurist can be appointed even without 10 years Bar practice.",
        "exp_ta": "சரத்து 124(3)-ன் படி உச்ச நீதிமன்ற நீதிபதிக்குரிய தகுதிகள் ஒன்றுக்கொன்று மாற்றுத் தகுதிகளாகும்: (a) 5 ஆண்டு உயர்நீதிமன்ற நீதிபதி அல்லது (b) 10 ஆண்டு வழக்கறிஞர் அல்லது (c) சிறந்த சட்ட அறிஞர். எனவே வழக்கறிஞராக இல்லாத ஒரு உயர்நீதிமன்ற நீதிபதியையும் AG-யாக நியமிக்க முடியும்.",
        "tip": "High-yield conceptual trap: 10 years advocate is NOT the only pathway.",
        "fact": "All three alternative routes qualify a person for appointment as Attorney General under Article 76(1)."
    },
    # 31
    {
        "stem_en": "What is the status of the Attorney General of India when the President seeks an advisory opinion from the Supreme Court under Article 143?",
        "stem_ta": "சரத்து 143-ன் கீழ் உச்ச நீதிமன்றத்திடம் குடியரசுத் தலைவர் ஆலோசனை கேட்கும் போது இந்திய தலைமை வழக்கறிஞரின் நிலை என்ன?",
        "options": [
            ("He acts as the Judge of the reference bench", "அவர் ஆலோசனைக் குழுவின் நீதிபதியாக செயல்படுகிறார்"),
            ("He represents the Union Government to present the legal background and arguments supporting the reference", "ஆலோசனைக் குறிப்பை ஆதரிக்கும் சட்டப் பின்னணி மற்றும் வாதங்களை முன்வைக்க அவர் மத்திய அரசின் சார்பில் ஆஜராகிறார்"),
            ("He remains neutral and cannot speak", "அவர் நடுநிலையாக இருந்து பேச முடியாது"),
            ("He drafts the Supreme Court's advisory judgment", "அவர் உச்ச நீதிமன்றத்தின் ஆலோசனைக் குறிப்பை வரைகிறார்")
        ],
        "correct_idx": 1,
        "exp_en": "In any Presidential Reference under Article 143, the Attorney General appears on behalf of the Union of India to explain the constitutional necessity of the reference and argue the legal questions framed by the President.",
        "exp_ta": "சரத்து 143 குறிப்புகளில், குடியரசுத் தலைவரால் எழுப்பப்பட்ட சட்டக் கேள்விகளுக்கு ஆதரவாக வாதங்களை முன்வைக்க இந்திய அரசின் சார்பில் தலைமை வழக்கறிஞர் முன்னிலையாகிறார்.",
        "tip": "Article 143 references are heard by a Constitution Bench of at least 5 judges.",
        "fact": "The AG coordinates with the Law Ministry to prepare the written submissions."
    },
    # 32
    {
        "stem_en": "Who was the Attorney General of India who served during the historic 1992 Ram Janmabhoomi / Babri Masjid dispute developments and Presidential Reference under Article 143?",
        "stem_ta": "1992-ல் அயோத்தி விவகாரம் மற்றும் சரத்து 143 குடியரசுத் தலைவர் ஆலோசனைக் குறிப்பின் போது இந்தியாவின் தலைமை வழக்கறிஞராக இருந்தவர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Milon K. Banerjee", "மிலன் கே. பானர்ஜி"),
            ("G.E. Vahanvati", "ஜி.இ. வாகனவதி"),
            ("K.K. Venugopal", "கே.கே. வேணுகோபால்")
        ],
        "correct_idx": 1,
        "exp_en": "Milon K. Banerjee was the Attorney General from 1992 to 1996 and represented the Union Government during the Special Reference on the Ram Janmabhoomi dispute in 1993 (Ismail Faruqui case).",
        "exp_ta": "மிலன் கே. பானர்ஜி 1992 முதல் 1996 வரை தலைமை வழக்கறிஞராக பணியாற்றி, 1993-ல் அயோத்தி விவகாரம் தொடர்பான சிறப்பு ஆலோசனைக் குறிப்பில் (இஸ்மாயில் ஃபரூக்கி வழக்கு) மத்திய அரசுக்காக ஆஜரானார்.",
        "tip": "Milon Banerjee served during the Prime Ministership of P.V. Narasimha Rao.",
        "fact": "The Supreme Court declined to answer the historical question in the 1993 reference."
    },
    # 33
    {
        "stem_en": "Does the Attorney General of India have the right to inspect any file or document of any Union Ministry when preparing legal advice for the Government?",
        "stem_ta": "அரசாங்கத்திற்கு சட்ட ஆலோசனை தயாரிக்கும் போது எந்தவொரு மத்திய அமைச்சகத்தின் கோப்புகளையும் ஆவணங்களையும் ஆய்வு செய்யும் உரிமை தலைமை வழக்கறிஞருக்கு உண்டா?",
        "options": [
            ("No, ministries can deny files under Official Secrets Act", "இல்லை, உத்தியோகபூர்வ ரகசியங்கள் சட்டத்தின் கீழ் அமைச்சகங்கள் மறுக்கலாம்"),
            ("Yes, all relevant government files, departmental records, and confidential notes are made available to the AG to enable sound legal counsel", "ஆம், சிறந்த சட்ட ஆலோசனையை வழங்க ஏதுவாக அனைத்து தொடர்புடைய அரசு கோப்புகள், துறை பதிவுகள் மற்றும் ரகசிய குறிப்புகள் AG-க்கு வழங்கப்படுகின்றன"),
            ("Only after Cabinet Secretary approves in each instance", "ஒவ்வொரு முறையும் கேபினட் செயலாளர் அனுமதித்தால் மட்டுமே"),
            ("Only files older than 30 years", "30 ஆண்டுகளுக்கு முந்தைய கோப்புகள் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "To render competent and comprehensive legal advice, the Attorney General is provided with all relevant files, departmental notes, and background records by the referring ministry through the Ministry of Law and Justice.",
        "exp_ta": "முழுமையான மற்றும் துல்லியமான சட்ட ஆலோசனையை வழங்க ஏதுவாக, சம்பந்தப்பட்ட அமைச்சகத்தின் அனைத்து கோப்புகள் மற்றும் ஆவணங்கள் சட்ட அமைச்சகத்தின் வழியாக தலைமை வழக்கறிஞரின் ஆய்வுக்கு வழங்கப்படுகின்றன.",
        "tip": "The AG is under an ethical duty of confidentiality regarding all government briefs.",
        "fact": "Privileged communication between Government and AG is protected under Section 126 of Evidence Act."
    },
    # 34
    {
        "stem_en": "In which year was the office of Attorney General of India established under the Constitution?",
        "stem_ta": "இந்திய அரசியலமைப்பின் கீழ் இந்திய தலைமை வழக்கறிஞர் அலுவலகம் எந்த ஆண்டு நிறுவப்பட்டது?",
        "options": [
            ("1947", "1947"),
            ("1950", "1950"),
            ("1952", "1952"),
            ("1955", "1955")
        ],
        "correct_idx": 1,
        "exp_en": "The office of the Attorney General of India was established on 26 January 1950 with the commencement of the Constitution of India, and the first AG M.C. Setalvad assumed office on 28 January 1950.",
        "exp_ta": "இந்திய அரசியலமைப்பு அமலுக்கு வந்த 1950 ஜனவரி 26 அன்று தலைமை வழக்கறிஞர் அலுவலகம் நிறுவப்பட்டது; முதல் AG எம்.சி. செதல்வாட் 1950 ஜனவரி 28 அன்று பொறுப்பேற்றார்.",
        "tip": "Established concurrently with the Supreme Court of India (inaugurated 28 January 1950).",
        "fact": "Prior to 1950, the Government of India Act 1935 provided for an 'Advocate-General for the Federation'."
    },
    # 35
    {
        "stem_en": "Under the Government of India Act 1935, what was the predecessor office to the Attorney General of India called?",
        "stem_ta": "1935 இந்திய அரசுச் சட்டத்தின் கீழ், இந்திய தலைமை வழக்கறிஞர் பதவிக்கு முன்னோடியாக இருந்த பதவி எது?",
        "options": [
            ("Attorney General of the Empire", "பேரரசின் தலைமை வழக்கறிஞர்"),
            ("Advocate-General for the Federation", "கூட்டாட்சிக்கான அட்வகேட்-ஜெனரல் (Advocate-General for the Federation)"),
            ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்"),
            ("Crown Prosecutor", "கிரவுன் வழக்கறிஞர்")
        ],
        "correct_idx": 1,
        "exp_en": "Section 16 of the Government of India Act 1935 provided for the appointment of an 'Advocate-General for the Federation' by the Governor-General, which was the direct historical predecessor of the Attorney General under Article 76.",
        "exp_ta": "1935 இந்திய அரசுச் சட்டத்தின் பிரிவு 16, கவர்னர் ஜெனரலால் நியமிக்கப்படும் 'கூட்டாட்சிக்கான அட்வகேட்-ஜெனரல்' பதவிக்கு வகை செய்தது; இதுவே சரத்து 76-ன் கீழான அட்டர்னி ஜெனரல் பதவிக்கு முன்னோடியாகும்.",
        "tip": "Sir Brojendra Lal Mitter was the first Advocate-General for the Federation under the 1935 Act.",
        "fact": "The nomenclature 'Attorney General' was adopted from the Anglo-American legal tradition in 1950."
    },
    # 36
    {
        "stem_en": "Who among the following was the first Indian to be appointed as Advocate-General for the Federation under the Government of India Act 1935?",
        "stem_ta": "1935 சட்டத்தின் கீழ் கூட்டாட்சிக்கான அட்வகேட்-ஜெனரலாக நியமிக்கப்பட்ட முதல் இந்தியர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Sir Brojendra Lal Mitter", "சர் பிரோஜேந்திர லால் மிட்டர்"),
            ("Sir Alladi Krishnaswamy Iyer", "சர் அல்லாடி கிருஷ்ணசாமி ஐயர்"),
            ("Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்")
        ],
        "correct_idx": 1,
        "exp_en": "Sir Brojendra Lal Mitter was appointed as the first Advocate-General for the Federation under the Government of India Act 1935 in 1937.",
        "exp_ta": "சர் பிரோஜேந்திர லால் மிட்டர் 1937-ல் 1935 இந்திய அரசுச் சட்டத்தின் கீழ் கூட்டாட்சிக்கான முதல் அட்வகேட்-ஜெனரலாக நியமிக்கப்பட்டார்.",
        "tip": "He was succeeded by Sir Noshirwan Engineer in 1945.",
        "fact": "M.C. Setalvad succeeded Sir Noshirwan Engineer when India became a Republic in 1950."
    },
    # 37
    {
        "stem_en": "Under Article 88, can the Attorney General of India be called to the floor of Parliament to clarify a legal or constitutional doubt regarding a pending Bill?",
        "stem_ta": "சரத்து 88-ன் கீழ், நிலுவையிலுள்ள ஒரு மசோதா குறித்த சட்ட அல்லது அரசியலமைப்பு சந்தேகங்களை தெளிவுபடுத்த தலைமை வழக்கறிஞரை நாடாளுமன்றத்திற்கு அழைக்க முடியுமா?",
        "options": [
            ("No, ministers alone can speak on bills", "இல்லை, அமைச்சர்கள் மட்டுமே மசோதாக்கள் மீது பேச முடியும்"),
            ("Yes, Parliament or the Speaker/Chairman can request the Attorney General to address the House to clarify complex constitutional questions", "ஆம், சிக்கலான அரசியலமைப்பு கேள்விகளை தெளிவுபடுத்த அவையில் உரையாற்றுமாறு தலைமை வழக்கறிஞரை நாடாளுமன்றம் அல்லது சபாநாயகர் அழைக்கலாம்"),
            ("Only after the bill is passed", "மசோதா நிறைவேறிய பிறகு மட்டுமே"),
            ("Only during budget presentation", "பட்ஜெட் தாக்கலின் போது மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under Article 88, the Attorney General can be requested by the House or Speaker to address MPs and clarify legal complexities on pending legislative bills (e.g., M.C. Setalvad addressed Parliament on the Preventive Detention Bill).",
        "exp_ta": "சரத்து 88-ன் கீழ், நிலுவையிலுள்ள மசோதாக்கள் மீதான சட்டக் கருத்துக்களை தெளிவுபடுத்த தலைமை வழக்கறிஞரை அவையில் உரையாற்ற நாடாளுமன்றம் அழைக்க முடியும் (எ.கா. தடுப்புக் காவல் மசோதா குறித்து செதல்வாட் உரையாற்றினார்).",
        "tip": "AG has the right to speak in both Lok Sabha and Rajya Sabha under Article 88.",
        "fact": "He sits on the Treasury Benches during such parliamentary appearances."
    },
    # 38
    {
        "stem_en": "Which of the following is true regarding the tenure of Mukul Rohatgi as the 14th Attorney General of India?",
        "stem_ta": "இந்தியாவின் 14-வது தலைமை வழக்கறிஞராக முகுல் ரோஹத்கியின் பதவிக்காலம் குறித்து கீழ்க்கண்டவற்றில் எது சரியானது?",
        "options": [
            ("He served from 1998 to 2004", "அவர் 1998 முதல் 2004 வரை பணியாற்றினார்"),
            ("He was appointed in June 2014 by the NDA government and served a full 3-year term till June 2017", "அவர் ஜூன் 2014-ல் தேசிய ஜனநாயகக் கூட்டணி அரசால் நியமிக்கப்பட்டு ஜூன் 2017 வரை 3 ஆண்டுகள் பணியாற்றினார்"),
            ("He was removed by Parliamentary impeachment", "அவர் நாடாளுமன்ற கண்டனத் தீர்மானத்தால் நீக்கப்பட்டார்"),
            ("He declined private practice after retirement", "ஓய்வுக்குப் பிறகு அவர் தனியார் தொழிலை மறுத்தார்")
        ],
        "correct_idx": 1,
        "exp_en": "Senior Advocate Mukul Rohatgi served as the 14th Attorney General of India from 19 June 2014 to 18 June 2017, representing the Narendra Modi government in the NJAC case and Triple Talaq case.",
        "exp_ta": "மூத்த வழக்கறிஞர் முகுல் ரோஹத்கி 2014 ஜூன் முதல் 2017 ஜூன் வரை 14-வது தலைமை வழக்கறிஞராக பணியாற்றி, NJAC வழக்கு மற்றும் முத்தலாக் வழக்கில் மத்திய அரசுக்காக ஆஜரானார்.",
        "tip": "Mukul Rohatgi stepped down after completing his 3-year term to resume private practice.",
        "fact": "He was succeeded by K.K. Venugopal in July 2017."
    },
    # 39
    {
        "stem_en": "In the National Judicial Appointments Commission (NJAC) case (Supreme Court Advocates-on-Record Association v. UOI, 2015), who was the Attorney General who defended the 99th Constitutional Amendment Act?",
        "stem_ta": "தேசிய நீதிபதிகள் நியமன ஆணைய (NJAC) வழக்கில் (2015), 99-வது அரசியலமைப்பு திருத்தச் சட்டத்தை ஆதரித்து வாதாடிய தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("G.E. Vahanvati", "ஜி.இ. வாகனவதி"),
            ("Mukul Rohatgi", "முகுல் ரோஹத்கி"),
            ("K.K. Venugopal", "கே.கே. வேணுகோபால்"),
            ("Soli Sorabjee", "சோலி சோராப்ஜி")
        ],
        "correct_idx": 1,
        "exp_en": "Attorney General Mukul Rohatgi led the Union Government's robust legal defense of the 99th Constitutional Amendment Act and the NJAC Act before the 5-judge Constitution Bench in 2015.",
        "exp_ta": "2015-ல் 5 நீதிபதிகள் கொண்ட அமர்வின் முன் 99-வது அரசியலமைப்பு திருத்தச் சட்டம் மற்றும் NJAC சட்டத்தை ஆதரித்து மத்திய அரசுக்காக தலைமை வழக்கறிஞர் முகுல் ரோஹத்கி வாதாடினார்.",
        "tip": "The Supreme Court struck down the 99th Amendment by a 4:1 majority (Justice Chelameswar dissenting).",
        "fact": "The Court ruled that executive participation in judicial appointments violates the Basic Structure."
    },
    # 40
    {
        "stem_en": "Can the Attorney General of India be appointed to represent India in international courts and arbitrations abroad (such as ICJ or Permanent Court of Arbitration)?",
        "stem_ta": "சர்வதேச நீதிமன்றங்கள் அல்லது வெளிநாட்டு நடுவர் மன்றங்களில் (ICJ அல்லது PCA) இந்தியாவை பிரதிநிதித்துவப்படுத்த தலைமை வழக்கறிஞர் நியமிக்கப்பட முடியுமா?",
        "options": [
            ("No, his jurisdiction is strictly domestic", "இல்லை, அவரது அதிகார வரம்பு உள்நாட்டிற்கு மட்டுமே"),
            ("Yes, the Government of India frequently instructs the Attorney General to lead the legal delegation in international disputes involving the Union", "ஆம், ஒன்றிய அரசு சம்பந்தப்பட்ட சர்வதேச தகராறுகளில் சட்டக் குழுவை வழிநடத்த தலைமை வழக்கறிஞரை அரசு அடிக்கடி நியமிக்கிறது"),
            ("Only with the approval of the United Nations Security Council", "ஐக்கிய நாடுகள் பாதுகாப்பு கவுன்சிலின் ஒப்புதலுடன் மட்டுமே"),
            ("Only in border demarcation cases", "எல்லை வரையறை வழக்குகளில் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under presidential assignment of duties, the Attorney General represents the Republic of India in international courts, tribunals, and arbitrations (e.g., M.C. Setalvad represented India before the International Court of Justice in the Right of Passage over Indian Territory case against Portugal).",
        "exp_ta": "குடியரசுத் தலைவரின் பணி ஒதுக்கீட்டின் கீழ், சர்வதேச நீதிமன்றங்கள் மற்றும் நடுவர் மன்றங்களில் இந்தியாவை பிரதிநிதித்துவப்படுத்த தலைமை வழக்கறிஞருக்கு அதிகாரம் உண்டு (எ.கா. போர்த்துக்கல்லுக்கு எதிரான வழக்கில் ICJ-ல் செதல்வாட் ஆஜரானார்).",
        "tip": "Right of Passage case (1960) was India's first major case in the International Court of Justice.",
        "fact": "The AG coordinates closely with the Ministry of External Affairs in international litigation."
    },
    # 41
    {
        "stem_en": "Under the Constitution of India, if the President removes the Attorney General, is the Government required to state the grounds of removal?",
        "stem_ta": "இந்திய அரசியலமைப்பின் கீழ், தலைமை வழக்கறிஞரை குடியரசுத் தலைவர் பதவியிலிருந்து நீக்கினால் அதற்கான காரணங்களை அரசாங்கம் தெரிவிக்க வேண்டியது அவசியமா?",
        "options": [
            ("Yes, mandatory under Article 311", "ஆம், சரத்து 311-ன் கீழ் கட்டாயம்"),
            ("No, because the office is held during the pleasure of the President without specified grounds or tenure under Article 76(4)", "இல்லை, ஏனெனில் சரத்து 76(4)-ன் கீழ் பதவிக்காலமோ அல்லது காரணங்களோ இன்றி குடியரசுத் தலைவரின் விருப்பப்படி பதவி வகிக்கப்படுகிறது"),
            ("Yes, with prior notice of 3 months", "ஆம், 3 மாத முன்அறிவிப்புடன்"),
            ("Yes, subject to parliamentary resolution", "ஆம், நாடாளுமன்ற தீர்மானத்திற்கு உட்பட்டு")
        ],
        "correct_idx": 1,
        "exp_en": "Under Article 76(4), the doctrine of pleasure applies without qualification. The President (acting on cabinet advice) can remove the Attorney General at any time without assigning any cause or holding an inquiry.",
        "exp_ta": "சரத்து 76(4)-ன் கீழ் விருப்பக் கோட்பாடு (Pleasure doctrine) நிபந்தனையின்றி செயல்படுகிறது. எனவே எந்த காரணத்தையும் தெரிவிக்காமலும் அல்லது விசாரணையின்றியும் தலைமை வழக்கறிஞரை அரசு நீக்க முடியும்.",
        "tip": "Article 311 protects civil servants, but does NOT protect the Attorney General.",
        "fact": "This preserves the government's right to change its chief counsel whenever it deems necessary."
    },
    # 42
    {
        "stem_en": "Which of the following describes the relationship between the Attorney General of India and the Ministry of Law and Justice?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞருக்கும் மத்திய சட்டம் மற்றும் நீதித்துறை அமைச்சகத்திற்கும் இடையிலான உறவை கீழ்க்கண்டவற்றில் எது விவரிக்கிறது?",
        "options": [
            ("The AG is an employee subordinated to the Law Secretary", "AG சட்ட செயலாளருக்கு கீழ்ப்பட்ட ஒரு ஊழியர்"),
            ("The AG is an independent constitutional law officer whose advice is routed to ministries through the Department of Legal Affairs of the Law Ministry", "AG ஓர் சுயாதீன அரசியலமைப்பு சட்ட அதிகாரி; அவரது ஆலோசனைகள் சட்ட அமைச்சகத்தின் சட்ட விவகாரங்கள் துறை வழியாக அமைச்சகங்களுக்கு அனுப்பப்படுகின்றன"),
            ("The AG heads the Law Ministry as its Minister", "AG சட்ட அமைச்சராக அமைச்சகத்தை வழிநடத்துகிறார்"),
            ("The Law Ministry has no administrative connection with the AG", "சட்ட அமைச்சகத்திற்கு AG-யுடன் எந்த நிர்வாக தொடர்பும் இல்லை")
        ],
        "correct_idx": 1,
        "exp_en": "The Department of Legal Affairs in the Ministry of Law and Justice acts as the administrative nodal agency coordinating with the Attorney General, processing requests for legal opinions and references from various Union ministries.",
        "exp_ta": "சட்ட அமைச்சகத்தின் சட்ட விவகாரங்கள் துறை தலைமை வழக்கறிஞருடன் ஒருங்கிணைந்து செயல்படும் நிர்வாக அமைப்பாகும்; பல்வேறு அமைச்சகங்களின் சட்ட ஆலோசனைக் கோரிக்கைகள் இதன் வழியாகவே AG-க்கு அனுப்பப்படுகின்றன.",
        "tip": "Ministries do not contact the AG directly; files are routed through the Law Ministry.",
        "fact": "The Law Officers (Conditions of Service) Rules 1987 are administered by this department."
    },
    # 43
    {
        "stem_en": "Can the Attorney General of India represent a private party in a criminal trial as defense counsel if the Union Ministry of Law gives written permission?",
        "stem_ta": "மத்திய சட்ட அமைச்சகம் எழுத்துப்பூர்வ அனுமதி அளித்தால், ஒரு குற்றவியல் வழக்கில் குற்றம் சாட்டப்பட்டவருக்காக தலைமை வழக்கறிஞர் ஆஜராக முடியுமா?",
        "options": [
            ("No, criminal defense is completely forbidden under all circumstances", "இல்லை, எந்த சூழ்நிலையிலும் குற்றவியல் வாதாடல் முற்றிலும் தடை செய்யப்பட்டுள்ளது"),
            ("Yes, under Rule 8(1)(b) of the Law Officers Rules 1987, he may defend an accused person with the prior permission of the Government", "ஆம், 1987 சட்ட அதிகாரிகள் விதிகளின் விதி 8(1)(b)-ன் கீழ் அரசாங்கத்தின் முன்அனுமதியுடன் குற்றம் சாட்டப்பட்டவருக்காக ஆஜராகலாம்"),
            ("Only in military court martials", "இராணுவ நீதிமன்ற விசாரணைகளில் மட்டுமே"),
            ("Only if the Chief Justice of India consents", "இந்திய தலைமை நீதிபதி ஒப்புதல் அளித்தால் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under Rule 8(1)(b) of the Law Officers (Conditions of Service) Rules 1987, the Attorney General shall not defend an accused person in a criminal prosecution without the permission of the Government. With written permission, he can appear.",
        "exp_ta": "1987 சட்ட அதிகாரிகள் விதிகளின் விதி 8(1)(b)-ன் படி, அரசாங்கத்தின் முன்அனுமதி பெற்றால் மட்டுமே ஒரு குற்றவியல் வழக்கில் குற்றம் சாட்டப்பட்டவருக்காக தலைமை வழக்கறிஞர் ஆஜராக முடியும்.",
        "tip": "Permission is rarely granted to preserve public trust in the chief law officer.",
        "fact": "In civil cases, no government permission is required as long as GoI is not a party."
    },
    # 44
    {
        "stem_en": "What is the constitutional procedure if the Attorney General of India delivers a speech in Parliament that contains defamatory statements against a citizen?",
        "stem_ta": "நாடாளுமன்றத்தில் தலைமை வழக்கறிஞர் பேசும்போது ஒரு குடிமகனுக்கு எதிராக அவதூறான கருத்துக்களைக் கூறினால் அரசியலமைப்பு ரீதியான நடைமுறை என்ன?",
        "options": [
            ("The citizen can immediately file a defamation suit against the AG in the High Court", "அந்த குடிமகன் உடனடியாக உயர்நீதிமன்றத்தில் AG மீது அவதூறு வழக்கு தொடரலாம்"),
            ("Under Article 105(2) read with Article 105(4), no person is liable to any proceedings in any court in respect of anything said in Parliament, but the Speaker/Chairman can regulate his speech under House rules", "சரத்து 105(2) மற்றும் 105(4)-ன் கீழ் நாடாளுமன்றத்தில் பேசிய எதற்கும் நீதிமன்றத்தில் வழக்கு தொடர முடியாது; ஆனால் சபாநாயகர்/தலைவர் அவை விதிகளின் கீழ் நடவடிக்கை எடுக்கலாம்"),
            ("The AG is automatically dismissed by the President", "AG குடியரசுத் தலைவரால் தானாக பணிநீக்கம் செய்யப்படுவார்"),
            ("The Supreme Court will expunge the speech", "உச்ச நீதிமன்றம் அந்த உரையை நீக்கும்")
        ],
        "correct_idx": 1,
        "exp_en": "Under Article 105(2) and 105(4), the AG enjoys full parliamentary immunity: no court can question anything said by him on the floor of Parliament. However, the Presiding Officer (Speaker/Chairman) controls the debate and can order remarks expunged.",
        "exp_ta": "சரத்து 105(2) மற்றும் 105(4)-ன் கீழ் தலைமை வழக்கறிஞருக்கு முழு நாடாளுமன்ற பாதுகாப்பு உண்டு; அவர் பேசியதற்காக எந்த நீதிமன்றத்திலும் வழக்கு தொடர முடியாது. ஆனால் சபாநாயகர் அந்த அவதூறு வார்த்தைகளை அவைக் குறிப்பிலிருந்து நீக்க முடியும்.",
        "tip": "Parliamentary privilege protects free debate from judicial interference.",
        "fact": "Article 105(2) states that 'no member of Parliament shall be liable to any proceedings in any court in respect of anything said or any vote given by him in Parliament'."
    },
    # 45
    {
        "stem_en": "Who among the following was the Attorney General of India during the landmark Indira Nehru Gandhi v. Raj Narain (1975) election case in the Supreme Court?",
        "stem_ta": "உச்ச நீதிமன்றத்தில் இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975) தேர்தல் வழக்கில் தலைமை வழக்கறிஞராக இருந்தவர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Niren De", "நிரேன் டே"),
            ("C.K. Daphtary", "சி.கே. தப்தாரி"),
            ("K. Parasaran", "கே. பராசரன்")
        ],
        "correct_idx": 1,
        "exp_en": "Attorney General Niren De represented the Union of India in the landmark Indira Gandhi v. Raj Narain (1975) case where the 39th Constitutional Amendment (Clause 4 of Article 329A) was struck down by the Supreme Court.",
        "exp_ta": "39-வது அரசியலமைப்பு திருத்தம் ரத்து செய்யப்பட்ட இந்திரா காந்தி எதிர் ராஜ் நாராயண் (1975) வழக்கில் மத்திய அரசுக்காக தலைமை வழக்கறிஞர் நிரேன் டே ஆஜரானார்.",
        "tip": "Niren De served throughout the peak political and legal crises of the 1970s.",
        "fact": "This judgment reaffirmed that democracy and judicial review are basic features of the Constitution."
    },
    # 46
    {
        "stem_en": "Which distinguished jurist, who later became the Attorney General of India, served as the Advocate General of Maharashtra from 1988 to 1990?",
        "stem_ta": "பின்னர் இந்திய தலைமை வழக்கறிஞரான எந்த சிறந்த சட்ட வல்லுநர், 1988 முதல் 1990 வரை மகாராஷ்டிர மாநில தலைமை வழக்கறிஞராக (Advocate General) பணியாற்றினார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Goolam E. Vahanvati", "குலாம் இ. வாகனவதி"),
            ("S.V. Gupte", "எஸ்.வி. குப்தே"),
            ("Mukul Rohatgi", "முகுல் ரோஹத்கி")
        ],
        "correct_idx": 1,
        "exp_en": "G.E. Vahanvati served as Advocate General of Maharashtra (1999-2004), then Solicitor General of India (2004-2009), and finally became the 13th Attorney General of India (2009-2014).",
        "exp_ta": "ஜி.இ. வாகனவதி மகாராஷ்டிர அட்வகேட் ஜெனரலாகவும் (1999-2004), பின்னர் இந்திய சொலிசிட்டர் ஜெனரலாகவும் (2004-2009), இறுதியாக 13-வது இந்திய தலைமை வழக்கறிஞராகவும் (2009-2014) பணியாற்றினார்.",
        "tip": "G.E. Vahanvati was the first Muslim to be appointed as Attorney General of India.",
        "fact": "He passed away in September 2014, shortly after stepping down as Attorney General."
    },
    # 47
    {
        "stem_en": "Who was the first Muslim jurist to be appointed as the Attorney General of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞராக நியமிக்கப்பட்ட முதல் முஸ்லிம் சட்ட வல்லுநர் யார்?",
        "options": [
            ("Milon K. Banerjee", "மிலன் கே. பானர்ஜி"),
            ("Goolam Essaji Vahanvati", "குலாம் எசாஜி வாகனவதி"),
            ("Fali S. Nariman", "பாலி எஸ். நாரிமன்"),
            ("Syed Mahmud", "சையத் மஹ்மூத்")
        ],
        "correct_idx": 1,
        "exp_en": "Goolam Essaji Vahanvati was appointed as the 13th Attorney General of India in June 2009 under the UPA government, becoming the first Muslim to hold the high constitutional office.",
        "exp_ta": "2009 ஜூன் மாதம் UPA அரசால் 13-வது தலைமை வழக்கறிஞராக நியமிக்கப்பட்ட குலாம் எசாஜி வாகனவதி, இப்பதவியை வகித்த முதல் முஸ்லிம் சட்ட வல்லுநராவார்.",
        "tip": "Served from June 2009 to May 2014 under Prime Minister Dr. Manmohan Singh.",
        "fact": "He represented the Union in landmark cases including the 2G spectrum allocation and Right to Education Act challenge."
    },
    # 48
    {
        "stem_en": "Can the Attorney General of India appear before a Parliamentary Committee without being named as a member of that committee?",
        "stem_ta": "நாடாளுமன்றக் குழுவில் உறுப்பினராக நியமிக்கப்படாமல் அக்குழுவின் முன் இந்திய தலைமை வழக்கறிஞர் ஆஜராக முடியுமா?",
        "options": [
            ("No, never under any circumstances", "இல்லை, எந்த சூழ்நிலையிலும் முடியாது"),
            ("Yes, a Parliamentary Committee can summon or invite the Attorney General to tender expert legal opinion on a subject under inquiry", "ஆம், ஒரு நாடாளுமன்றக் குழு தனது ஆய்வில் உள்ள விவகாரம் குறித்து நிபுணர் சட்ட ஆலோசனை வழங்க தலைமை வழக்கறிஞரை அழைக்கலாம் அல்லது வரவழைக்கலாம்"),
            ("Only in the Public Accounts Committee", "பொதுக் கணக்குக் குழுவில் மட்டுமே"),
            ("Only during budget sessions", "பட்ஜெட் கூட்டத்தொடரின் போது மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under parliamentary procedure and committee rules, any Parliamentary Standing or Select Committee has the power to invite or summon the Attorney General as an expert constitutional witness to clarify legal questions.",
        "exp_ta": "நாடாளுமன்ற நடைமுறை விதிகளின்படி, எந்தவொரு நிலைக்குழுவோ அல்லது தேர்வுக் குழுவோ தலைமை வழக்கறிஞரை நிபுணர் சாட்சியாக அழைத்து சட்ட ஆலோசனையைப் பெற முடியும்.",
        "tip": "He appears as an expert legal advisor to assist Parliament in lawmaking.",
        "fact": "His statements before the committee are recorded in the committee's official proceedings."
    },
    # 49
    {
        "stem_en": "Under Article 76, who determines the fees paid to the Attorney General of India for appearances in courts outside Delhi?",
        "stem_ta": "சரத்து 76-ன் கீழ், தில்லிக்கு வெளியே உள்ள நீதிமன்றங்களில் ஆஜராவதற்காக தலைமை வழக்கறிஞருக்கு வழங்கப்படும் கட்டணங்களை தீர்மானிப்பது யார்?",
        "options": [
            ("Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"),
            ("Government of India under the Law Officers (Conditions of Service) Rules", "சட்ட அதிகாரிகள் விதிகளின் கீழ் இந்திய அரசாங்கம்"),
            ("State Bar Council of Delhi", "தில்லி மாநில பார் கவுன்சில்"),
            ("The opposing private party", "எதிர் தரப்பு தனியார் நபர்")
        ],
        "correct_idx": 1,
        "exp_en": "Under Article 76(4), the President determines the remuneration of the AG. The specific daily appearance fees, daily allowances, and travel expenses for outstation appearances are laid down in the Law Officers (Conditions of Service) Rules 1987 by the Central Government.",
        "exp_ta": "சரத்து 76(4)-ன் கீழ் குடியரசுத் தலைவர் ஊதியத்தை தீர்மானிக்கிறார். வெளிமாநில நீதிமன்றங்களில் ஆஜராவதற்கான தினசரி கட்டணம் மற்றும் படிகளை மத்திய அரசின் 1987 சட்ட அதிகாரிகள் விதிகள் நிர்ணயிக்கின்றன.",
        "tip": "The AG is provided executive air travel and accommodation entitlement equivalent to a Union Cabinet Minister.",
        "fact": "He submits itemized fee bills to the Ministry of Law and Justice."
    },
    # 50
    {
        "stem_en": "What is the effect on pending government litigation when an Attorney General of India resigns or is replaced by a new Attorney General?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞர் பதவி விலகும் போதோ அல்லது புதிய தலைமை வழக்கறிஞர் பொறுப்பேற்கும் போதோ நிலுவையிலுள்ள அரசு வழக்குகளின் நிலை என்ன?",
        "options": [
            ("All pending government cases must be refiled from the beginning", "நிலுவையிலுள்ள அனைத்து அரசு வழக்குகளும் மீண்டும் முதலிலிருந்து தாக்கல் செய்யப்பட வேண்டும்"),
            ("Litigation continues uninterrupted; the office is a continuous constitutional entity and the new AG or other law officers take over the briefs", "வழக்குகள் தடையின்றி தொடரும்; இவ்வலுவலகம் ஒரு தொடர்ச்சியான அரசியலமைப்பு அமைப்பாகும், புதிய AG அல்லது பிற சட்ட அதிகாரிகள் வழக்குகளை தொடர்ந்து நடத்துவர்"),
            ("Cases are automatically dismissed for want of prosecution", "வழக்குகள் தானாக தள்ளுபடி செய்யப்படும்"),
            ("The Supreme Court appoints an interim advocate for 6 months", "உச்ச நீதிமன்றம் 6 மாதங்களுக்கு இடைக்கால வழக்கறிஞரை நியமிக்கும்")
        ],
        "correct_idx": 1,
        "exp_en": "The office of the Attorney General is a permanent continuous constitutional institution. Change of personnel does not affect the validity or continuation of pending litigation on behalf of the Union of India.",
        "exp_ta": "தலைமை வழக்கறிஞர் அலுவலகம் ஒரு நிரந்தர தொடர்ச்சியான அரசியலமைப்பு அமைப்பாகும். தனிநபர் மாற்றம் நிலுவையிலுள்ள வழக்குகளை பாதிக்காது; புதிய தலைமை வழக்கறிஞர் அல்லது பிற சட்ட அதிகாரிகள் அவ்வழக்குகளை தொடர்ந்து நடத்துவர்.",
        "tip": "Institutional continuity is maintained through the Central Agency Section of the Ministry of Law.",
        "fact": "All briefs remain government property and are transferred to the incoming law officer."
    }
]

def build_ag_medium():
    questions = []
    for i, item in enumerate(raw_medium_data):
        qid = f"AG_M_{i+1:03d}"
        opts = item["options"]
        correct_idx = item["correct_idx"]
        correct_key = ["A", "B", "C", "D"][correct_idx]
        
        why_en = {}
        why_ta = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if idx == correct_idx:
                why_en[key] = f"Option {key} is the correct constitutional and statutory position."
                why_ta[key] = f"அரசியலமைப்பு மற்றும் சட்ட விதிகளின்படி தெரிவு {key} சரியான விடையாகும்."
            else:
                why_en[key] = f"Option {key} ({opts[idx][0]}) is incorrect."
                why_ta[key] = f"தெரிவு {key} ({opts[idx][1]}) தவறானது."
                
        q = make_ag_q(
            qid=qid,
            diff="Medium",
            qtype="Single Choice",
            subtopic="Powers, Privileges & Limitations of Attorney General",
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
            why_a_en=why_en["A"],
            why_a_ta=why_ta["A"],
            why_b_en=why_en["B"],
            why_b_ta=why_ta["B"],
            why_c_en=why_en["C"],
            why_c_ta=why_ta["C"],
            why_d_en=why_en["D"],
            why_d_ta=why_ta["D"],
            tip_en=item["tip"],
            tip_ta=f"நினைவில் கொள்க: {item['tip']}",
            fact_en=item["fact"],
            fact_ta=f"முக்கிய தகவல்: {item['fact']}",
            tags=["polity", "attorney_general_of_india", "medium"]
        )
        questions.append(q)
    return questions

def main():
    questions = build_ag_medium()
    print(f"Generated {len(questions)} raw Medium questions.")
    
    # Balance keys to 13 B, 12 C, 12 D, 13 A
    balanced = balance_question_keys(questions, {"A": 13, "B": 13, "C": 12, "D": 12})
    
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "attorney_general_medium.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, indent=2, ensure_ascii=False)
        
    print(f"Saved balanced Medium MCQs to {out_file}")
    
    validator = ContentValidator()
    report = validator.validate_file(out_file, expected_count=50, expected_prefix="AG_M_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
    if not report.is_valid:
        for iss in report.issues:
            print("Issue:", iss.message)

if __name__ == "__main__":
    main()
