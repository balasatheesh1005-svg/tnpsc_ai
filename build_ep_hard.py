# -*- coding: utf-8 -*-
"""
Generator for Emergency Provisions Hard MCQs (50 questions: EP_H_001 to EP_H_050)
Strictly adheres to:
1. 24-field schema verified by validator.py
2. Bilingual parity (English and Tamil)
3. Balanced answer distribution: A: 13, B: 12, C: 12, D: 13
4. Advanced constitutional doctrine, judicial precedents (Bommai, Rameshwar Prasad, Makhan Singh), intricate procedural rules, and critical analytical traps
"""

import json
import os
from collections import Counter
from ep_mcq_helper import make_ep_q
from tools.nova_content_engine.validator import ContentValidator

PREFIX = "EP_H_"
DIFF = "Hard"

def get_hard_questions():
    qs = []

    # 001 - Key A
    qs.append(make_ep_q(
        PREFIX, 1, DIFF, "Advanced Jurisprudence", "Judicial Precedents - Makhan Singh Case",
        "In the landmark pre-44th Amendment ruling Makhan Singh v. State of Punjab (1964), what crucial distinction did the Supreme Court draw regarding the suspension of Fundamental Rights under Article 359?",
        "44-வது திருத்தத்திற்கு முந்தைய வரலாற்றுச் சிறப்புமிக்க மாகன் சிங் எதிர் பஞ்சாப் அரசு (1964) வழக்கில், சரத்து 359-ன் கீழ் அடிப்படை உரிமைகள் இடைநிறுத்தம் செய்யப்படுவது குறித்து உச்ச நீதிமன்றம் வகுத்த முக்கியமான வேறுபாடு என்ன?",
        "Article 359 suspends only the remedial right of the citizen to move the court, while the substantive rights themselves remain theoretically valid though unenforceable", "சரத்து 359 குடிமக்கள் நீதிமன்றத்தை அணுகும் தீர்வை மட்டுமே இடைநிறுத்துகிறது, ஆனால் உரிமைகள் அமல்படுத்த முடியாதவையாக இருந்தாலும் கோட்பாட்டளவில் தொடர்ந்து உயிர்ப்புடன் இருக்கும்",
        "Article 359 automatically voids all fundamental rights guaranteed under Part III of the Constitution", "சரத்து 359 அரசியலமைப்பின் பகுதி III-ன் கீழ் உள்ள அனைத்து அடிப்படை உரிமைகளையும் தானாகவே செல்லாததாக்குகிறது",
        "Article 359 grants the Union executive unreviewable immunity to create any criminal offences retrospectively", "சரத்து 359 மத்திய நிர்வாகத்திற்கு பின்னோக்கி குற்றவியல் குற்றங்களை உருவாக்க மறுஆய்வு செய்ய முடியாத பாதுகாப்பை அளிக்கிறது",
        "Article 359 operates only if Parliament ratifies the presidential order by a two-thirds majority within 14 days", "சரத்து 359-ன் கீழான குடியரசுத் தலைவர் ஆணையை பாராளுமன்றம் 14 நாட்களுக்குள் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் அங்கீகரித்தால் மட்டுமே அது செயல்படும்",
        "A",
        "In Makhan Singh v. State of Punjab (1964), a Constitution Bench led by CJI P.B. Gajendragadkar ruled that Article 359(1) does not suspend the fundamental rights themselves, but only suspends the citizen's right to move any court for their enforcement. As soon as the order expires, the rights regain their full remedial force.",
        "மாகன் சிங் எதிர் பஞ்சாப் அரசு (1964) வழக்கில், தலைமை நீதிபதி பி.பி. கஜேந்திரகட்கர் தலைமையிலான அரசியலமைப்பு அமர்வு, சரத்து 359(1) அடிப்படை உரிமைகளையே இடைநிறுத்தவில்லை என்றும், அவற்றை அமல்படுத்துவதற்காக நீதிமன்றத்தை அணுகும் குடிமகனின் உரிமையை மட்டுமே இடைநிறுத்துகிறது என்றும் தீர்ப்பளித்தது. ஆணை காலாவதியானவுடன் உரிமைகள் மீண்டும் முழு பரிகார சக்தியைப் பெறுகின்றன.",
        "Option A precisely states the ratio decidendi laid down by the Supreme Court in Makhan Singh.", "விருப்பம் A மாகன் சிங் வழக்கில் உச்ச நீதிமன்றம் வகுத்த தீர்ப்பின் துல்லியமான சட்டக் கொள்கையைக் கூறுகிறது.",
        "Option B erroneously claims Part III is voided; rights are not voided.", "விருப்பம் B பகுதி III செல்லாததாகிறது என்று தவறாகக் கூறுகிறது; உரிமைகள் ரத்தாகவில்லை.",
        "Option C violates Article 20(1) protections against ex-post facto laws.", "விருப்பம் C பின்னோக்கிய குற்றவியல் சட்டங்களுக்கு எதிரான சரத்து 20(1) பாதுகாப்பை மீறுகிறது.",
        "Option D describes an imaginary ratification timeframe.", "விருப்பம் D கற்பனையான ஏற்புக் காலக்கெடுவை விவரிக்கிறது.",
        "Makhan Singh Distinction: Article 358 suspends the right; Article 359 suspends the remedy (locus standi to approach courts).",
        "மாகன் சிங் வேறுபாடு: சரத்து 358 உரிமையை இடைநிறுத்துகிறது; சரத்து 359 தீர்வை (நீதிமன்றத்தை அணுகும் உரிமையை) இடைநிறுத்துகிறது.",
        "This foundational distinction proved vital in evaluating executive detentions during the 1962 and 1965 national emergencies.",
        "இந்த அடிப்படைக் கட்டமைப்பு 1962 மற்றும் 1965 தேசிய அவசரநிலைகளின் போது நிர்வாகத் தடுப்புக் காவல்களை மதிப்பிடுவதில் மிகவும் முக்கியமானதாக அமைந்தது."
    ))

    # 002 - Key B
    qs.append(make_ep_q(
        PREFIX, 2, DIFF, "Constitutional Landmark", "Rameshwar Prasad Case (2006)",
        "In Rameshwar Prasad v. Union of India (2006), concerning the dissolution of the Bihar Legislative Assembly under Article 356, what was the Supreme Court's decisive ruling on the Governor's role?",
        "ராமேஷ்வர் பிரசாத் எதிர் இந்திய ஒன்றியம் (2006) வழக்கில், பீகார் சட்டமன்றம் சரத்து 356-ன் கீழ் கலைக்கப்பட்டது தொடர்பாக ஆளுநரின் பங்கு குறித்து உச்ச நீதிமன்றத்தின் தீர்க்கமான தீர்ப்பு என்ன?",
        "The Governor has absolute discretion to dissolve the Assembly without floor testing if subjective horse-trading is feared", "குதிரை பேரம் நடைபெறும் என்ற அச்சம் இருந்தால் நம்பிக்கை வாக்கெடுப்பின்றி சட்டமன்றத்தைக் கலைக்க ஆளுநருக்கு முழுமையான தன்னுரிமை அதிகாரம் உண்டு",
        "The Governor cannot recommend dissolution of the Assembly merely on the speculative apprehension of horse-trading or post-poll alliances to prevent a political party from staking claim", "ஒரு அரசியல் கட்சி ஆட்சி அமைக்க உரிமை கோருவதைத் தடுப்பதற்காக, குதிரை பேரம் நடக்கும் என்ற யூகத்தின் அடிப்படையிலோ அல்லது தேர்தலுக்குப் பிந்தைய கூட்டணிகளைக் காரணம்காட்டியோ ஆளுநர் சட்டமன்றத்தைக் கலைக்கப் பரிந்துரைக்க முடியாது",
        "The Governor is an agent of the Central Government and bound by telephonic instructions of the Union Home Minister", "ஆளுநர் மத்திய அரசின் பிரதிநிதி என்பதால் மத்திய உள்துறை அமைச்சரின் தொலைபேசி அறிவுறுத்தல்களுக்கு கட்டுப்பட்டவர்",
        "The Governor's report under Article 356 is a privileged state document completely exempt from judicial inspection", "சரத்து 356-ன் கீழான ஆளுநரின் அறிக்கை நீதித்துறை ஆய்விலிருந்து முற்றிலும் விலக்கு பெற்ற ஒரு தனிச்சலுகை ஆவணம்",
        "B",
        "In Rameshwar Prasad (2006), a 5-judge bench declared the dissolution of the Bihar Assembly under Article 356 unconstitutional and malafide. The Court held that the Governor (Buta Singh) acted with undue haste to prevent a political coalition from staking a claim to form government. The apprehension of horse-trading without holding a floor test cannot be a valid ground for dissolving an elected Assembly.",
        "ராமேஷ்வர் பிரசாத் (2006) வழக்கில், பீகார் சட்டமன்றம் சரத்து 356-ன் கீழ் கலைக்கப்பட்டது அரசியலமைப்பிற்கு எதிரானது மற்றும் தவறான உள்நோக்கம் கொண்டது என்று 5 நீதிபதிகள் கொண்ட அமர்வு தீர்ப்பளித்தது. ஓர் அரசியல் கூட்டணி ஆட்சி அமைக்க உரிமை கோருவதைத் தடுக்கவே ஆளுநர் (பூட்டா சிங்) அவசரப்பட்டு செயல்பட்டார் என்று நீதிமன்றம் கண்டித்தது. நம்பிக்கை வாக்கெடுப்பு நடத்தாமல் குதிரை பேரம் நடக்கும் என்ற அச்சம் சட்டமன்றத்தைக் கலைக்க சரியான காரணமாகாது.",
        "Option A is the exact unconstitutional reasoning used by the Governor that the Court struck down.", "விருப்பம் A என்பது நீதிமன்றத்தால் நிராகரிக்கப்பட்ட ஆளுநரின் அரசியலமைப்பிற்கு எதிரான வாதமாகும்.",
        "Option B is the precise landmark ruling establishing that preventing a party from staking claim via pre-emptive dissolution is unconstitutional.", "விருப்பம் B முன்கூட்டியே கலைப்பதன் மூலம் ஓர் கட்சி ஆட்சி அமைப்பதைத் தடுப்பது அரசியலமைப்பிற்கு எதிரானது என்பதை நிறுவிய தீர்ப்பாகும்.",
        "Option C directly violates the independent constitutional status of the Governor.", "விருப்பம் C ஆளுநரின் சுதந்திரமான அரசியலமைப்பு அந்தஸ்தை மீறுகிறது.",
        "Option D was rejected; the materials underlying the Governor's report are open to judicial scrutiny.", "விருப்பம் D நிராகரிக்கப்பட்டது; ஆளுநரின் அறிக்கைக்கான அடிப்படை ஆதாரங்கள் நீதித்துறை ஆய்வுக்கு உட்பட்டவை.",
        "Rameshwar Prasad Milestone: Pre-emptive dissolution to prevent post-poll coalition from staking claim is malafide and unconstitutional.",
        "ராமேஷ்வர் பிரசாத் மைல்கல்: தேர்தலுக்குப் பிந்தைய கூட்டணி ஆட்சி அமைப்பதைத் தடுக்க முன்கூட்டியே சட்டமன்றத்தைக் கலைப்பது உள்நோக்கம் கொண்டது மற்றும் அரசியலமைப்பிற்கு எதிரானது.",
        "Even though the dissolution was declared unconstitutional, the Court did not revive the Assembly because the election process had already begun.",
        "கலைப்பு அரசியலமைப்பிற்கு எதிரானது என அறிவிக்கப்பட்ட போதிலும், தேர்தல் நடவடிக்கைகள் ஏற்கனவே தொடங்கிவிட்டதால் பேரவையை நீதிமன்றம் மீண்டும் உயிர்ப்பிக்கவில்லை."
    ))

    # 003 - Key C
    qs.append(make_ep_q(
        PREFIX, 3, DIFF, "Constitutional Nuance", "Article 353 Proviso and Cross-Border Spillover",
        "Under the proviso to Article 353(a) and 353(b), when a National Emergency is declared in only one state or region, how can the executive and legislative powers of the Union be exercised in a non-emergency state?",
        "சரத்து 353(a) மற்றும் 353(b)-ன் நிபந்தனை விதிகளின் கீழ், நாட்டின் ஒரு மாநிலத்தில் அல்லது பகுதியில் மட்டும் தேசிய அவசரநிலை அறிவிக்கப்பட்டிருக்கும் போது, அவசரநிலை இல்லாத மற்றொரு மாநிலத்தில் மத்திய அரசின் நிர்வாக மற்றும் சட்ட அதிகாரங்கள் எவ்வாறு பயன்படுத்தப்படலாம்?",
        "Only if the non-emergency state legislature passes a ratifying resolution under Article 252", "அவசரநிலை இல்லாத மாநில சட்டமன்றம் சரத்து 252-ன் கீழ் ஏற்புத் தீர்மானம் நிறைவேற்றினால் மட்டுமே",
        "Only if the Inter-State Council gives prior unanimous consent", "மாநிலங்களுக்கு இடையேயான கவுன்சில் முன் ஒருமனதான ஒப்புதல் அளித்தால் மட்டுமே",
        "The Union can extend executive directions and legislative enactments to the non-emergency state if activities therein threaten the security of the emergency area", "அவசரநிலை இல்லாத மாநிலத்தில் நடக்கும் செயல்பாடுகள் அவசரநிலை அறிவிக்கப்பட்ட பகுதியின் பாதுகாப்பிற்கு அச்சுறுத்தலாக இருந்தால், மத்திய அரசு தனது நிர்வாக மற்றும் சட்ட அதிகாரங்களை அந்த மாநிலத்திற்கும் விரிவுபடுத்தலாம்",
        "The Union must first dismiss the Governor of the non-emergency state and declare President's Rule there under Article 356", "மத்திய அரசு முதலில் அவசரநிலை இல்லாத மாநில ஆளுநரை நீக்கிவிட்டு சரத்து 356-ன் கீழ் அங்கு குடியரசுத் தலைவர் ஆட்சியை அறிவிக்க வேண்டும்",
        "C",
        "The provisos to Article 353(a) and (b), added by the 42nd Amendment Act 1976 and retained by the 44th Amendment Act 1978, stipulate that where a Proclamation of Emergency is in operation only in any part of the territory of India, the executive power of the Union to give directions and Parliament's legislative powers extend to any other State if activities in that other State are prejudicial to the security of the territory where emergency operates.",
        "1976-ன் 42-வது திருத்தத்தால் சேர்க்கப்பட்டு 1978-ன் 44-வது திருத்தத்தால் தக்கவைக்கப்பட்ட சரத்து 353(a) மற்றும் (b)-ன் நிபந்தனைகளின்படி, அவசரநிலை நாட்டின் ஒரு குறிப்பிட்ட பகுதியில் மட்டும் அமலில் இருக்கும் போது, பிற மாநிலத்தின் நடவடிக்கைகள் அவசரநிலை உள்ள பகுதியின் பாதுகாப்பிற்கு ஊறு விளைவிப்பதாக இருந்தால், மத்திய அரசு தன் நிர்வாக மற்றும் சட்ட அதிகாரங்களை அந்த மற்றொரு மாநிலத்திற்கும் விரிவுபடுத்த முடியும்.",
        "Option A describes Article 252 (voluntary delegation by 2 or more states), not emergency spillover.", "விருப்பம் A சரத்து 252-ஐ விவரிக்கிறது, அவசரநிலை அதிகார நீட்டிப்பை அல்ல.",
        "Option B has no constitutional basis in emergency provisions.", "விருப்பம் B-க்கு அவசரநிலைப் பிரிவுகளில் எந்த அரசியலமைப்பு அடிப்படையும் இல்லை.",
        "Option C is the verbatim constitutional standard established by the proviso to Article 353.", "விருப்பம் C சரத்து 353-ன் நிபந்தனை விதியால் நிறுவப்பட்ட துல்லியமான அரசியலமைப்பு விதியாகும்.",
        "Option D is an unconstitutional and abusive path.", "விருப்பம் D அரசியலமைப்பிற்கு எதிரான தவறான வழியாகும்.",
        "Spillover Doctrine: Security nexus allows Union emergency powers to traverse state borders into non-emergency areas.",
        "பாதுகாப்பு இணைப்பு கோட்பாடு: பாதுகாப்பு அச்சுறுத்தல் காரணமாக மத்திய அவசரநிலை அதிகாரங்கள் அவசரநிலை இல்லாத மாநில எல்லைக்குள்ளும் செயல்பட அனுமதிக்கிறது.",
        "This ensures that logistics, communication lines, or cross-border militancy originating in safe states can be intercepted centrally.",
        "பாதுகாப்பான மாநிலங்களிலிருந்து உருவாகும் தளவாடங்கள், தகவல் தொடர்புகள் அல்லது எல்லை தாண்டிய வன்முறைகளை மத்திய அரசு நேரடியாகக் கட்டுப்படுத்த இது உதவுகிறது."
    ))

    # 004 - Key D
    qs.append(make_ep_q(
        PREFIX, 4, DIFF, "Constitutional Comparison", "Article 358 vs 359 Nexus Requirement",
        "Following the 44th Amendment Act 1978, which of the following is an absolute prerequisite for any law or executive action to claim immunity under Article 358 or Article 359?",
        "1978-ன் 44-வது திருத்தச் சட்டத்தைத் தொடர்ந்து, எந்தவொரு சட்டம் அல்லது நிர்வாக நடவடிக்கை சரத்து 358 அல்லது சரத்து 359-ன் கீழ் பாதுகாப்புப் பெற பின்வருவனவற்றில் எது ஒரு முழுமையான முன்நிபந்தனையாகும்?",
        "The law must be assented to by the Chief Justice of India before notification", "அறிவிக்கை செய்வதற்கு முன் அந்தச் சட்டம் இந்திய தலைமை நீதிபதியால் ஒப்புதல் அளிக்கப்பட வேண்டும்",
        "The executive order must be issued personally by the Governor under sealed warrant", "அந்த நிர்வாக ஆணை சீலிடப்பட்ட உத்தரவாதத்தின் கீழ் ஆளுநரால் நேரடியாகப் பிறப்பிக்கப்பட வேண்டும்",
        "The law must be reviewed by the Comptroller and Auditor General for fiscal propriety", "அந்தச் சட்டம் நிதிப் பொருத்தம் குறித்து மத்திய கணக்குத் தணிக்கையாளரால் ஆய்வு செய்யப்பட வேண்டும்",
        "The law must contain a specific recital stating that it is in relation to the Proclamation of Emergency in operation", "அந்தச் சட்டம் அமலில் உள்ள அவசரநிலைப் பிரகடனம் தொடர்புடையது என்ற குறிப்பிட்ட சட்ட அறிவிப்பைக் (recital) கொண்டிருக்க வேண்டும்",
        "D",
        "Under the amended Articles 358(2) and 359(1B) inserted by the 44th Amendment Act 1978, immunity from fundamental rights challenge applies ONLY to a law containing a recital that such law is in relation to the Proclamation of Emergency in operation, or to any executive action taken under a law containing such recital. All ordinary or unrelated laws remain subject to judicial challenge under fundamental rights.",
        "1978-ன் 44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்துகள் 358(2) மற்றும் 359(1B)-ன் படி, அடிப்படை உரிமைகள் மீறல் வழக்கிலிருந்து விலக்கு பெறுவதற்கு, அந்தச் சட்டம் அமலில் உள்ள அவசரநிலைப் பிரகடனத்துடன் தொடர்புடையது என்ற வெளிப்படையான அறிவிப்பைக் (recital) கொண்டிருக்க வேண்டும். அத்தகைய அறிவிப்பு இல்லாத சாதாரண அல்லது தொடர்பற்ற சட்டங்கள் நீதிமன்றத்தில் சவாலுக்கு உட்பட்டவையே.",
        "Option A violates the doctrine of separation of powers; the judiciary does not pre-assent to laws.", "விருப்பம் A அதிகாரப் பகிர்வுக் கோட்பாட்டை மீறுகிறது; நீதித்துறை சட்டங்களுக்கு முன் ஒப்புதல் அளிப்பதில்லை.",
        "Option B is irrelevant.", "விருப்பம் B தொடர்பற்றது.",
        "Option C relates to audit matters under Article 149.", "விருப்பம் C சரத்து 149-ன் கீழான தணிக்கை விவகாரங்கள் தொடர்பானது.",
        "Option D is the exact 'nexus requirement' enacted by the 44th Constitutional Amendment.", "விருப்பம் D என்பது 44-வது அரசியலமைப்பு திருத்தத்தால் கொண்டுவரப்பட்ட துல்லியமான 'தொடர்பு நிபந்தனை' ஆகும்.",
        "Statutory Recital Test: Without the explicit recital that the law is in relation to the emergency, no immunity exists against Fundamental Rights violations.",
        "சட்டப்பூர்வ அறிவிப்புத் தேர்வு: அந்தச் சட்டம் அவசரநிலையுடன் தொடர்புடையது என்ற தெளிவான அறிவிப்பு இல்லையெனில், அடிப்படை உரிமை மீறல்களுக்கு எதிராக எந்தப் பாதுகாப்பும் கிடைக்காது.",
        "This completely outlawed the pre-1978 executive malpractice of using emergency cover to shield regular administrative tyranny.",
        "அவசரநிலையின் போர்வையில் வழக்கமான நிர்வாக அடக்குமுறைகளைப் பாதுகாக்கும் 1978-க்கு முந்தைய நடைமுறையை இது முற்றிலும் தடுத்தது."
    ))

    # 005 - Key A
    qs.append(make_ep_q(
        PREFIX, 5, DIFF, "Constitutional Comparison", "Article 359 and Writ Jurisdiction of High Courts",
        "During the 1975-1977 Emergency, in the infamous A.D.M. Jabalpur v. Shivkant Shukla (1976) case, what did the 4:1 majority hold regarding Article 226 writ petitions?",
        "1975-1977 அவசரநிலையின் போது, புகழ்பெற்ற ஏ.டி.எம். ஜபல்பூர் எதிர் சிவகாந்த் சுக்லா (1976) வழக்கில், சரத்து 226-ன் கீழான நீதிப்பேராணை மனுக்கள் குறித்து 4:1 பெரும்பான்மை நீதிபதிகள் என்ன தீர்ப்பளித்தனர்?",
        "In view of the Presidential Order under Article 359, no person has any locus standi to move any writ petition under Article 226 before a High Court for Habeas Corpus to challenge illegal detention", "சரத்து 359-ன் கீழான குடியரசுத் தலைவர் ஆணையைக் கருத்தில் கொண்டு, சட்டவிரோத தடுப்புக் காவலை எதிர்த்து உயர் நீதிமன்றத்தில் சரத்து 226-ன் கீழ் ஆட்கொணர்வு மனு தாக்கல் செய்ய எந்த நபருக்கும் எந்தவித உரிமையும் இல்லை",
        "High Courts retain absolute jurisdiction under Article 226 because state powers cannot be touched by presidential orders", "மாநில அதிகாரங்களை குடியரசுத் தலைவர் ஆணை தொட முடியாது என்பதால் சரத்து 226-ன் கீழ் உயர் நீதிமன்றங்கள் முழு அதிகார வரம்பைத் தக்கவைத்துள்ளன",
        "Only the Supreme Court has jurisdiction under Article 32, but High Courts lose jurisdiction under Article 226", "உச்ச நீதிமன்றத்திற்கு மட்டுமே சரத்து 32-ன் கீழ் அதிகாரம் உண்டு, ஆனால் உயர் நீதிமன்றங்கள் சரத்து 226-ன் கீழான அதிகாரத்தை இழக்கின்றன",
        "Writ petitions can be entertained only if approved by the Attorney General of India", "இந்திய தலைமை வழக்கறிஞர் ஒப்புதல் அளித்தால் மட்டுமே நீதிப்பேராணை மனுக்களை விசாரிக்க முடியும்",
        "A",
        "In ADM Jabalpur (1976), Justices Ray, Beg, Chandrachud, and Bhagwati held that under the Article 359 presidential order suspending Article 21, no person had any locus standi to move any court under Article 226 for a writ of habeas corpus to challenge the legality of an order of detention, even if malafide or ultra vires. Justice H.R. Khanna famously dissented. This majority verdict was formally overruled by the Supreme Court in the K.S. Puttaswamy case (2017).",
        "ஏ.டி.எம். ஜபல்பூர் (1976) வழக்கில், சரத்து 21-ஐ இடைநிறுத்தும் சரத்து 359 குடியரசுத் தலைவர் ஆணையின் கீழ், ஒரு தடுப்புக் காவல் தவறான உள்நோக்கம் கொண்டதாகவோ அல்லது அதிகார வரம்பை மீறியதாகவோ இருந்தாலும் கூட, அதை எதிர்த்து உயர் நீதிமன்றத்தில் சரத்து 226-ன் கீழ் ஆட்கொணர்வு மனு தாக்கல் செய்ய யாருக்கும் உரிமையில்லை என்று நீதிபதிகள் ரே, பேக், சந்திரசூட், பகவதி ஆகியோர் தீர்ப்பளித்தனர். நீதிபதி எச்.ஆர். கண்ணா புகழ்பெற்ற மாறுபட்ட தீர்ப்பை வழங்கினார். இந்த பெரும்பான்மை தீர்ப்பு 2017 புட்டசுவாமி வழக்கில் உச்ச நீதிமன்றத்தால் முறையாக ரத்து செய்யப்பட்டது.",
        "Option A accurately quotes the tragic majority holding in ADM Jabalpur.", "விருப்பம் A ஏ.டி.எம். ஜபல்பூர் வழக்கின் பெரும்பான்மைத் தீர்ப்பைத் துல்லியமாகக் கூறுகிறது.",
        "Option B represents the courageous stance taken by several High Courts prior to being reversed by ADM Jabalpur.", "விருப்பம் B உச்ச நீதிமன்றத்தால் மாற்றப்படுவதற்கு முன்பு பல உயர் நீதிமன்றங்கள் எடுத்த தைரியமான நிலைப்பாட்டைக் குறிக்கிறது.",
        "Option C is legally distorted; Art 32 was equally barred.", "விருப்பம் C தவறானது; சரத்து 32-ம் சமமாகத் தடைபட்டிருந்தது.",
        "Option D has no legal standing.", "விருப்பம் D சட்டப்பூர்வமற்றது.",
        "Historic Dissent: Justice H.R. Khanna's lonely dissent declared that even without Article 21, the State cannot deprive a person of life or liberty without the authority of law.",
        "வரலாற்று மாறுபட்ட தீர்ப்பு: சரத்து 21 இல்லாவிட்டாலும் கூட, சட்டத்தின் அதிகாரமின்றி அரசு ஒரு நபரின் உயிர் அல்லது தனிநபர் சுதந்திரத்தைப் பறிக்க முடியாது என்று நீதிபதி எச்.ஆர். கண்ணா தீர்ப்பளித்தார்.",
        "Justice Khanna paid for his independence by being superseded for the office of Chief Justice of India in 1977.",
        "நீதிபதி கண்ணா தனது சுதந்திரமான நிலைப்பாட்டிற்காக 1977-ல் இந்திய தலைமை நீதிபதி பதவியில் மூப்பு நிலை புறக்கணிக்கப்பட்டு பாதிக்கப்பட்டார்."
    ))

    # 006 - Key B
    qs.append(make_ep_q(
        PREFIX, 6, DIFF, "Constitutional Landmark", "Puttaswamy Overruling ADM Jabalpur",
        "In which landmark Nine-Judge Constitution Bench decision in 2017 did the Supreme Court formally overrule the majority decision in A.D.M. Jabalpur v. Shivkant Shukla (1976)?",
        "2017-ஆம் ஆண்டின் எந்த வரலாற்றுச் சிறப்புமிக்க ஒன்பது நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு தீர்ப்பில், ஏ.டி.எம். ஜபல்பூர் எதிர் சிவகாந்த் சுக்லா (1976) வழக்கின் பெரும்பான்மைத் தீர்ப்பை உச்ச நீதிமன்றம் முறையாக ரத்து செய்தது?",
        "Navtej Singh Johar v. Union of India", "நவ்ேதேஜ் சிங் ஜோஹர் எதிர் இந்திய ஒன்றியம்",
        "Justice K.S. Puttaswamy (Retd.) v. Union of India", "நீதிபதி கே.எஸ். புட்டசுவாமி (ஓய்வு) எதிர் இந்திய ஒன்றியம்",
        "Shayara Bano v. Union of India", "ஷயாரா பானோ எதிர் இந்திய ஒன்றியம்",
        "National Legal Services Authority (NALSA) v. Union of India", "தேசிய சட்டப் பணிகள் ஆணைக்குழு (நல்சா) எதிர் இந்திய ஒன்றியம்",
        "B",
        "In Justice K.S. Puttaswamy (Retd.) v. Union of India (2017), the 9-judge Constitution Bench unanimously held that the right to privacy is a fundamental right under Article 21, and expressly overruled the 1976 ADM Jabalpur judgment, observing that the majority opinion was 'deeply flawed' and that Justice Khanna's dissent was the correct statement of law.",
        "நீதிபதி கே.எஸ். புட்டசுவாமி (ஓய்வு) எதிர் இந்திய ஒன்றியம் (2017) வழக்கில், 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு தனிஉரிமை (Privacy) என்பது சரத்து 21-ன் கீழ் ஓர் அடிப்படை உரிமை என்று ஒருமனதாக தீர்ப்பளித்ததோடு, 1976 ஏ.டி.எம். ஜபல்பூர் வழக்கின் பெரும்பான்மைத் தீர்ப்பு 'ஆழமான குறைபாடுடையது' என்றும் நீதிபதி கண்ணாவின் மாறுபட்ட தீர்ப்பே சரியான சட்ட நிலை என்றும் கூறி அதை முறையாக ரத்து செய்தது.",
        "Option A (Navtej Johar, 2018) decriminalized consensual adult homosexuality under Section 377.", "விருப்பம் A (நவ்தேஜ் ஜோஹர், 2018) பிரிவு 377-ன் கீழ் ஒருபால் உறவை குற்றமற்றதாக்கியது.",
        "Option B is the authoritative 9-judge bench ruling formally erasing the dark stain of ADM Jabalpur.", "விருப்பம் B ஏ.டி.எம். ஜபல்பூர் வழக்கின் கறையை முறையாக துடைத்தெறிந்த 9 நீதிபதிகள் கொண்ட அமர்வின் தீர்ப்பாகும்.",
        "Option C (Shayara Bano, 2017) held Instant Triple Talaq unconstitutional.", "விருப்பம் C (ஷயாரா பானோ, 2017) உடனடி முத்தலாக் அரசியலமைப்பிற்கு எதிரானது என தீர்ப்பளித்தது.",
        "Option D (NALSA, 2014) recognized transgender persons as a third gender.", "விருப்பம் D (நல்சா, 2014) திருநங்கைகளை மூன்றாம் பாலினத்தவராக அங்கீகரித்தது.",
        "Constitutional Correction: ADM Jabalpur (1976) was formally buried by the 9-judge bench in K.S. Puttaswamy (2017).",
        "அரசியலமைப்பு திருத்தம்: ஏ.டி.எம். ஜபல்பூர் (1976) தீர்ப்பு கே.எஸ். புட்டசுவாமி (2017) வழக்கில் 9 நீதிபதிகள் கொண்ட அமர்வால் முறையாகப் புதைக்கப்பட்டது.",
        "Justice D.Y. Chandrachud formally overruled the judgment authored by his own father, former CJI Y.V. Chandrachud.",
        "நீதிபதி டி.ஒய். சந்திரசூட் தனது சொந்த தந்தை முன்னாள் தலைமை நீதிபதி ஒய்.வி. சந்திரசூட் எழுதிய தீர்ப்பை இத்தீர்ப்பில் முறையாக ரத்து செய்தார்."
    ))

    # 007 - Key C
    qs.append(make_ep_q(
        PREFIX, 7, DIFF, "Constitutional Comparison", "Article 356 and State Ordinances",
        "During President's Rule in a State, can the Governor of that State promulgate an Ordinance under Article 213?",
        "ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி அமலில் இருக்கும் போது, அந்த மாநில ஆளுநர் சரத்து 213-ன் கீழ் அவசரச் சட்டத்தைப் பிறப்பிக்க முடியுமா?",
        "Yes, the Governor possesses unlimited powers to promulgate ordinances during President's Rule", "ஆம், குடியரசுத் தலைவர் ஆட்சியின் போது அவசரச் சட்டங்களைப் பிறப்பிக்க ஆளுநருக்கு வரம்பற்ற அதிகாரங்கள் உள்ளன",
        "Yes, but only with the prior written recommendation of the dismissed Chief Minister", "ஆம், ஆனால் பதவி நீக்கம் செய்யப்பட்ட முதலமைச்சரின் முன் எழுத்துப்பூர்வ பரிந்துரையுடன் மட்டுமே",
        "No, because the legislative powers of the State are declared to be exercisable by or under the authority of Parliament, rendering Article 213 inoperative", "முடியாது, ஏனெனில் மாநிலத்தின் சட்டமியற்றும் அதிகாரங்கள் பாராளுமன்றத்தால் பயன்படுத்தப்படும் என அறிவிக்கப்படுவதால், சரத்து 213 செயலிழந்து விடுகிறது",
        "Yes, provided the State High Court issues an advance judicial certificate", "ஆம், மாநில உயர் நீதிமன்றம் முன் நீதித்துறை சான்றிதழ் வழங்கினால் மட்டுமே",
        "C",
        "Under Article 213, the Governor can promulgate an ordinance only when the State Legislature (or either House) is not in session and the Governor is satisfied that circumstances exist requiring immediate action. However, when President's Rule is proclaimed under Article 356(1)(b), the powers of the Legislature of the State are declared to be exercisable by or under the authority of Parliament. Thus, the Governor CANNOT promulgate an ordinance under Article 213 during President's Rule. Instead, the President may issue an Ordinance under Article 123 when Parliament is not in session.",
        "சரத்து 213-ன் கீழ், மாநில சட்டமன்றம் அமர்வில் இல்லாத போது மட்டுமே ஆளுநர் அவசரச் சட்டம் பிறப்பிக்க முடியும். ஆனால், சரத்து 356(1)(b)-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி அமலில் இருக்கும் போது, மாநில சட்டமன்றத்தின் அதிகாரங்கள் பாராளுமன்றத்தின் அதிகார வரம்பிற்குள் கொண்டுவரப்படுகின்றன. எனவே, குடியரசுத் தலைவர் ஆட்சியின் போது ஆளுநர் சரத்து 213-ன் கீழ் அவசரச் சட்டம் பிறப்பிக்க முடியாது. மாறாக பாராளுமன்றம் அமர்வில் இல்லாத போது குடியரசுத் தலைவரே சரத்து 123-ன் கீழ் அவசரச் சட்டம் பிறப்பிக்கலாம்.",
        "Option A is false; Governor's ordinance power is suspended along with the assembly.", "விருப்பம் A தவறு; சட்டமன்றத்துடன் சேர்த்து ஆளுநரின் அவசரச் சட்ட அதிகாரமும் முடங்குகிறது.",
        "Option B is absurd as the Council of Ministers is already dismissed.", "விருப்பம் B தவறானது ஏனெனில் அமைச்சரவை ஏற்கனவே கலைக்கப்பட்டுவிட்டது.",
        "Option C accurately captures the jurisdictional transfer of legislative competence under Article 356(1)(b).", "விருப்பம் C சரத்து 356(1)(b)-ன் கீழான சட்டமன்ற அதிகார மாற்றத்தை துல்லியமாக விளக்குகிறது.",
        "Option D has no constitutional foundation.", "விருப்பம் D-க்கு அரசியலமைப்பு அடிப்படை இல்லை.",
        "Ordinance Powers during Art 356: Governor loses Art 213 powers entirely. President exercises ordinance powers under Art 123 for the State when Parliament is in recess.",
        "சரத்து 356-ன் போது அவசரச் சட்ட அதிகாரம்: ஆளுநர் சரத்து 213 அதிகாரத்தை முற்றிலும் இழக்கிறார். பாராளுமன்றம் கூடாத போது குடியரசுத் தலைவரே சரத்து 123-ன் கீழ் மாநிலத்திற்காக அவசரச் சட்டம் பிறப்பிக்கிறார்.",
        "This ensures that legislative authority over the state is unified under the national executive and legislature.",
        "இது மாநிலத்தின் மீதான சட்டமியற்றும் அதிகாரம் தேசிய நிர்வாகம் மற்றும் சட்டமன்றத்தின் கீழ் ஒருங்கிணைக்கப்படுவதை உறுதி செய்கிறது."
    ))

    # 008 - Key D
    qs.append(make_ep_q(
        PREFIX, 8, DIFF, "Constitutional Comparison", "National Emergency Effects on Union-State Financials",
        "Under Article 354, when the President modifies the distribution of revenues during a National Emergency, which of the following is an absolute constitutional limitation on such presidential orders?",
        "சரத்து 354-ன் கீழ், தேசிய அவசரநிலையின் போது மத்திய-மாநில வருவாய் பகிர்வை குடியரசுத் தலைவர் மாற்றியமைக்கும் போது, அத்தகைய குடியரசுத் தலைவரின் ஆணைகள் மீதான முழுமையான அரசியலமைப்பு வரம்பு எது?",
        "The order must be approved by the Finance Commission within 30 days", "அந்த ஆணை 30 நாட்களுக்குள் நிதி ஆணையத்தால் அங்கீகரிக்கப்பட வேண்டும்",
        "The order can reduce the state's share of taxes to zero permanently", "அந்த ஆணை மாநிலத்தின் வரிப் பங்கை நிரந்தரமாக பூஜ்ஜியமாகக் குறைக்க முடியும்",
        "The order requires the counter-signature of all State Governors", "அந்த ஆணைக்கு அனைத்து மாநில ஆளுநர்களின் எதிர் கையொப்பம் தேவை",
        "Every such order must be laid before each House of Parliament, and ceases to operate at the end of the financial year in which the emergency ceases", "அத்தகைய ஒவ்வொரு ஆணையும் பாராளுமன்றத்தின் இரு அவைகளிலும் வைக்கப்பட வேண்டும், மேலும் அவசரநிலை முடிவுக்கு வரும் நிதி ஆண்டின் இறுதியில் அது காலாவதியாகிவிடும்",
        "D",
        "Article 354(2) mandates two constitutional checks on presidential orders modifying the distribution of revenues: (1) Every such order shall, as soon as may be after it is made, be laid before each House of Parliament; and (2) No such order shall extend beyond the expiration of the financial year in which the Proclamation of Emergency ceases to operate.",
        "சரத்து 354(2) வருவாய் பகிர்வை மாற்றியமைக்கும் குடியரசுத் தலைவர் ஆணைகள் மீது இரண்டு அரசியலமைப்பு கட்டுப்பாடுகளை விதிக்கிறது: (1) அத்தகைய ஒவ்வொரு ஆணையும் இயற்றப்பட்ட உடனேயே பாராளுமன்றத்தின் இரு அவைகளிலும் சமர்ப்பிக்கப்பட வேண்டும்; மற்றும் (2) அவசரநிலைப் பிரகடனம் முடிவுக்கு வரும் நிதி ஆண்டு முடிவடைவதைத் தாண்டி அந்த ஆணை நீடிக்கக் கூடாது.",
        "Option A is false; Finance Commission has no veto over emergency orders.", "விருப்பம் A தவறு; அவசரநிலை ஆணைகள் மீது நிதி ஆணையத்திற்கு எந்த வீட்டோ அதிகாரமும் இல்லை.",
        "Option B is false; permanent alterations cannot be made under Article 354.", "விருப்பம் B தவறு; சரத்து 354-ன் கீழ் நிரந்தர மாற்றங்களைச் செய்ய முடியாது.",
        "Option C is fictitious.", "விருப்பம் C கற்பனையானது.",
        "Option D verbatim captures the twin mandatory conditions of Article 354(2).", "விருப்பம் D சரத்து 354(2)-ன் இரட்டை கட்டாய நிபந்தனைகளை அப்படியே கொண்டுள்ளது.",
        "Check Fiscal Sunset: Article 354 orders last only until the end of the financial year in which the emergency terminates.",
        "நிதி காலாவதியைச் சரிபார்க்கவும்: சரத்து 354 ஆணைகள் அவசரநிலை முடிவடையும் நிதி ஆண்டின் இறுதி வரை மட்டுமே நீடிக்கும்.",
        "This ensures that Parliament reviews the executive diversion of resources and that states regain their revenue predictability rapidly.",
        "நிர்வாகம் வளங்களை மாற்றுவதை பாராளுமன்றம் ஆய்வு செய்வதையும், மாநிலங்கள் விரைவாக தங்கள் வருவாய் கணிப்பை மீட்டெடுப்பதையும் இது உறுதி செய்கிறது."
    ))

    # 009 - Key A
    qs.append(make_ep_q(
        PREFIX, 9, DIFF, "Constitutional Comparison", "Article 356 - Dissolution vs Suspended Animation",
        "In the Bommai case (1994), what did the Supreme Court hold regarding the legal consequences if Parliament DOES NOT approve a proclamation of President's Rule within two months?",
        "பொம்மை வழக்கில் (1994), பாராளுமன்றம் இரண்டு மாதங்களுக்குள் குடியரசுத் தலைவர் ஆட்சிப் பிரகடனத்திற்கு ஒப்புதல் அளிக்கவில்லை என்றால் ஏற்படும் சட்ட விளைவுகள் குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "The proclamation lapses at the end of two months, the dismissed Council of Ministers revives, and the suspended Legislative Assembly becomes active again", "இரண்டு மாத முடிவில் பிரகடனம் காலாவதியாகிறது, பதவி நீக்கம் செய்யப்பட்ட அமைச்சரவை மீண்டும் உயிர்ப்பிக்கப்படுகிறது மற்றும் நிறுத்தி வைக்கப்பட்ட சட்டமன்றம் மீண்டும் செயல்படத் தொடங்குகிறது",
        "Fresh elections must be called within 30 days automatically by the Supreme Court", "உச்ச நீதிமன்றத்தால் 30 நாட்களுக்குள் தானாகவே புதிய தேர்தல்கள் நடத்தப்பட வேண்டும்",
        "The Governor assumes sovereign legislative powers to enact laws permanently", "ஆளுநர் நிரந்தரமாக சட்டங்களை இயற்றும் இறையாண்மை சட்டமியற்றும் அதிகாரத்தை ஏற்றுக்கொள்கிறார்",
        "The President can immediately issue an identical fresh proclamation without parliamentary approval", "பாராளுமன்ற ஒப்புதல் இன்றியே குடியரசுத் தலைவர் உடனடியாக அதேபோன்ற புதிய பிரகடனத்தை மீண்டும் வெளியிடலாம்",
        "A",
        "In S.R. Bommai (1994), the Supreme Court laid down that if Parliament fails to approve the proclamation under Article 356 within two months, the proclamation lapses. In such an event, the dismissed Ministry revives, and the Legislative Assembly (which could only be kept in suspended animation prior to approval) is reactivated. To enable this remedy, dissolution of the Assembly before parliamentary approval was held unconstitutional.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், சரத்து 356-ன் கீழான பிரகடனத்திற்கு பாராளுமன்றம் இரண்டு மாதங்களுக்குள் ஒப்புதல் அளிக்கத் தவறினால், பிரகடனம் காலாவதியாகிவிடும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. அத்தகைய சூழ்நிலையில், கலைக்கப்பட்ட அமைச்சரவை மீண்டும் உயிர்பெறும், மேலும் சட்டமன்றம் (ஒப்புதலுக்கு முன் தற்காலிகமாக மட்டுமே நிறுத்தி வைக்கப்பட வேண்டும்) மீண்டும் செயல்படும். இந்த நிவாரணத்தை சாத்தியமாக்கவே, பாராளுமன்ற ஒப்புதலுக்கு முன் சட்டமன்றத்தைக் கலைப்பது அரசியலமைப்பிற்கு எதிரானது எனப்பட்டது.",
        "Option A is the foundational restoration remedy established by the Bommai Constitution Bench.", "விருப்பம் A என்பது பொம்மை அரசியலமைப்பு அமர்வால் நிறுவப்பட்ட அடிப்படைக் கொள்கையாகும்.",
        "Option B is false; courts do not issue election schedules.", "விருப்பம் B தவறு; நீதிமன்றங்கள் தேர்தல் அட்டவணைகளை வெளியிடுவதில்லை.",
        "Option C is unconstitutional.", "விருப்பம் C அரசியலமைப்பிற்கு எதிரானது.",
        "Option D constitutes colorable exercise of power that courts will immediately strike down.", "விருப்பம் D அதிகார துஷ்பிரயோகமாகும், அதை நீதிமன்றங்கள் உடனடியாக ரத்து செய்யும்.",
        "Status Quo Ante Restoration: If Parliament rejects Article 356, the status quo ante is restored; the ministry and assembly revive automatically.",
        "பழைய நிலை மீட்பு: பாராளுமன்றம் சரத்து 356-ஐ நிராகரித்தால், பழைய நிலையே மீட்டெடுக்கப்படுகிறது; அமைச்சரவையும் சட்டமன்றமும் தானாகவே உயிர்பெறுகின்றன.",
        "This legal holding completely disincentivized the Union from using Article 356 for partisan short-term gains.",
        "இந்தச் சட்ட தீர்ப்பு குறுகிய கால அரசியல் லாபங்களுக்காக சரத்து 356-ஐ மத்திய அரசு தவறாகப் பயன்படுத்துவதை முற்றிலுமாகத் தடுத்தது."
    ))

    # 010 - Key B
    qs.append(make_ep_q(
        PREFIX, 10, DIFF, "Constitutional Comparison", "Article 355 Independent Enforceability",
        "Can the Union Government invoke Article 355 to deploy central armed police forces (CRPF, BSF) in a State WITHOUT the consent of that State Government?",
        "மத்திய அரசு ஒரு மாநில அரசின் ஒப்புதல் இன்றியே அந்த மாநிலத்தில் மத்திய ஆயுதக் காவல் படைகளை (CRPF, BSF) நிலைநிறுத்த சரத்து 355-ஐப் பயன்படுத்த முடியுமா?",
        "No, deployment of armed forces within a state always requires the prior unanimous resolution of the State Legislative Assembly", "முடியாது, ஒரு மாநிலத்திற்குள் ஆயுதப் படைகளை நிலைநிறுத்துவது எப்போதும் மாநில சட்டமன்றத்தின் முன் ஒருமனதான தீர்மானத்தைக் கோருகிறது",
        "Yes, the Union has an independent constitutional duty under Article 355 to protect every State against external aggression and internal disturbance, allowing autonomous troop deployment", "ஆம், ஒவ்வொரு மாநிலத்தையும் வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டுக் குழப்பங்களிலிருந்து பாதுகாக்க சரத்து 355-ன் கீழ் மத்திய அரசுக்கு சுதந்திரமான அரசியலமைப்பு கடமை உள்ளதால், தன்னிச்சையாகப் படைகளை நிலைநிறுத்த முடியும்",
        "Only if the President declares a Financial Emergency under Article 360", "சரத்து 360-ன் கீழ் குடியரசுத் தலைவர் நிதி அவசரநிலையை அறிவித்தால் மட்டுமே",
        "Only during war declared formally by the United Nations Security Council", "ஐக்கிய நாடுகள் பாதுகாப்பு சபையால் முறையாக அறிவிக்கப்பட்ட போரின் போது மட்டுமே",
        "B",
        "Under Article 355, it is the bounden duty of the Union to protect every State against external aggression and internal disturbance. The Central Government has taken the consistent legal view (supported by the Sarkaria Commission and administrative practice) that the Union can deploy central armed forces suo motu to protect central installations or quell grave disturbance, even if the State Government does not formally request or consent to it.",
        "சரத்து 355-ன் கீழ், ஒவ்வொரு மாநிலத்தையும் வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டுக் குழப்பங்களிலிருந்து பாதுகாப்பது ஒன்றியத்தின் கட்டாயக் கடமையாகும். மாநில அரசு முறையாகக் கோராவிட்டாலும் அல்லது ஒப்புதல் அளிக்காவிட்டாலும் கூட, மத்திய அரசு சொத்துக்களைப் பாதுகாக்கவும் அல்லது கடுமையான குழப்பங்களைத் தணிக்கவும் தன்னிச்சையாக மத்திய ஆயுதப் படைகளை நிலைநிறுத்த முடியும் என்ற சட்ட நிலைப்பாட்டை (சர்க்காரியா ஆணையம் மற்றும் நடைமுறைகளால் ஆதரிக்கப்பட்டது) மத்திய அரசு கொண்டுள்ளது.",
        "Option A is incorrect; state consent is not an absolute constitutional veto against Union duty under Art 355.", "விருப்பம் A தவறானது; சரத்து 355-ன் கீழான மத்திய கடமைக்கு மாநில ஒப்புதல் ஒரு முழுமையான தடையாக இருக்க முடியாது.",
        "Option B accurately represents the constitutional scope of Article 355.", "விருப்பம் B சரத்து 355-ன் அரசியலமைப்பு அதிகார வரம்பைத் துல்லியமாகக் குறிக்கிறது.",
        "Option C confuses financial emergency with security duties.", "விருப்பம் C நிதி அவசரநிலையையும் பாதுகாப்பு கடமைகளையும் குழப்புகிறது.",
        "Option D is fictitious.", "விருப்பம் D கற்பனையானது.",
        "Article 355 Autonomy: Article 355 is not merely a preface to Article 356; it is an active, standalone duty of the Union to ensure security across all states.",
        "சரத்து 355 தன்னாட்சி: சரத்து 355 என்பது சரத்து 356-க்கான வெறும் முன்னுரை மட்டுமல்ல; அனைத்து மாநிலங்களிலும் பாதுகாப்பை உறுதி செய்வதற்கான ஒன்றியத்தின் நேரடி கடமையாகும்.",
        "However, deployment without consultation often causes political friction between Centre and Opposition-ruled States.",
        "இருப்பினும், கலந்தாலோசிக்காமல் படைகளை நிலைநிறுத்துவது மத்திய மற்றும் எதிர்க்கட்சி ஆளும் மாநிலங்களுக்கு இடையே அரசியல் உராய்வுகளை ஏற்படுத்துகிறது."
    ))

    # 011 - Key C
    qs.append(make_ep_q(
        PREFIX, 11, DIFF, "Constitutional Landmark", "Minerva Mills Judgment (1980) on Article 352",
        "In Minerva Mills v. Union of India (1980), what did Chief Justice Y.V. Chandrachud observe regarding the judicial review of a National Emergency proclamation under Article 352?",
        "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980) வழக்கில், சரத்து 352-ன் கீழான தேசிய அவசரநிலைப் பிரகடனத்தின் நீதித்துறை மறுஆய்வு குறித்து தலைமை நீதிபதி ஒய்.வி. சந்திரசூட் என்ன கருத்து தெரிவித்தார்?",
        "Courts can evaluate the adequacy and sufficiency of the intelligence reports submitted to the President", "குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்பட்ட உளவுத்துறை அறிக்கைகளின் போதுமான தன்மை மற்றும் நம்பகத்தன்மையை நீதிமன்றங்கள் மதிப்பாய்வு செய்யலாம்",
        "Proclamations under Article 352 are non-justiciable political questions immune from any judicial scrutiny whatsoever", "சரத்து 352-ன் கீழான பிரகடனங்கள் எந்தவொரு நீதித்துறை ஆய்விலிருந்தும் முற்றிலும் விலக்கு பெற்ற நியாயப்படுத்த முடியாத அரசியல் கேள்விகள்",
        "The court cannot examine the sufficiency of grounds, but whether a proclamation was issued malafide or based on wholly extraneous and irrelevant grounds is within the court's review jurisdiction", "நீதிமன்றம் காரணங்களின் போதுமான தன்மையை ஆராய முடியாது, ஆனால் பிரகடனம் தவறான உள்நோக்கத்துடன் அல்லது முற்றிலும் தொடர்பற்ற காரணங்களின் அடிப்படையில் வெளியிடப்பட்டதா என்பதை ஆராயும் அதிகாரம் நீதிமன்றத்திற்கு உண்டு",
        "The court will issue a writ of mandamus directing the President to revoke the emergency within 7 days", "அவசரநிலையை 7 நாட்களுக்குள் திரும்பப் பெறுமாறு குடியரசுத் தலைவருக்கு உத்தரவிட்டு நீதிமன்றம் செயலுறுத்தும் நீதிப்பேராணையை பிறப்பிக்கும்",
        "C",
        "In Minerva Mills (1980), CJI Y.V. Chandrachud observed that the satisfaction of the President under Article 352 is subjective, and courts cannot substitute their opinion or examine the sufficiency of materials. However, if the proclamation is challenged on the ground that it was made malafide or was based on wholly extraneous or irrelevant facts, it is subject to judicial review, because constitutional limitations cannot be transgressed by the executive.",
        "மினர்வா மில்ஸ் (1980) வழக்கில், தலைமை நீதிபதி ஒய்.வி. சந்திரசூட், சரத்து 352-ன் கீழ் குடியரசுத் தலைவரின் திருப்தி அகநிலை சார்ந்தது என்றும், நீதிமன்றங்கள் தங்கள் கருத்தை மாற்றாக வைக்கவோ அல்லது ஆதாரங்களின் போதுமான தன்மையை ஆராயவோ முடியாது என்றும் கூறினார். இருப்பினும், பிரகடனம் தவறான உள்நோக்கத்துடன் அல்லது முற்றிலும் தொடர்பற்ற உண்மைகளின் அடிப்படையில் வெளியிடப்பட்டது என்று சவால் செய்யப்பட்டால், அது நீதித்துறை மறுஆய்வுக்கு உட்பட்டது; ஏனெனில் அரசியலமைப்பு வரம்புகளை நிர்வாகம் மீற முடியாது.",
        "Option A is incorrect; courts never review the 'sufficiency' or 'adequacy' of confidential intelligence materials.", "விருப்பம் A தவறானது; ரகசிய உளவுத்துறை ஆதாரங்களின் 'போதுமான தன்மையை' நீதிமன்றங்கள் ஒருபோதும் மறுஆய்வு செய்வதில்லை.",
        "Option B was the position under the 38th Amendment, which the 44th Amendment repealed.", "விருப்பம் B என்பது 38-வது திருத்தத்தின் கீழ் இருந்த நிலை, அதை 44-வது திருத்தம் ரத்து செய்தது.",
        "Option C is the exact legal doctrine formulated in Minerva Mills.", "விருப்பம் C என்பது மினர்வா மில்ஸ் வழக்கில் வகுக்கப்பட்ட துல்லியமான சட்டக் கோட்பாடாகும்.",
        "Option D violates Article 361 immunity of the President.", "விருப்பம் D குடியரசுத் தலைவரின் சரத்து 361 பாதுகாப்பை மீறுகிறது.",
        "Judicial Review Limits under Art 352: Malafide and extraneous facts are reviewable; sufficiency of material is NOT reviewable.",
        "சரத்து 352-ன் கீழ் நீதித்துறை மறுஆய்வு வரம்புகள்: உள்நோக்கம் மற்றும் தொடர்பற்ற காரணங்கள் மறுஆய்வுக்கு உட்பட்டவை; ஆதாரங்களின் போதுமான தன்மை மறுஆய்வுக்கு உட்படாது.",
        "This maintains a delicate constitutional balance between executive national security prerogatives and fundamental rights protection.",
        "இது நிர்வாகத்தின் தேசிய பாதுகாப்பு உரிமைகளுக்கும் அடிப்படை உரிமைகள் பாதுகாப்பிற்கும் இடையே ஒரு நுட்பமான அரசியலமைப்பு சமநிலையைப் பேணுகிறது."
    ))

    # 012 - Key D
    qs.append(make_ep_q(
        PREFIX, 12, DIFF, "Constitutional Comparison", "Article 356 and Dissolution of Council of Ministers",
        "When President's Rule is imposed in a State under Article 356, what happens constitutionally to the State Council of Ministers headed by the Chief Minister?",
        "சரத்து 356-ன் கீழ் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி அமல்படுத்தப்படும் போது, முதலமைச்சர் தலைமையிலான மாநில அமைச்சரவைக்கு அரசியலமைப்பு ரீதியாக என்ன நேரிடுகிறது?",
        "The Council of Ministers continues to govern, but under direct instructions from the Union Cabinet", "அமைச்சரவை தொடர்ந்து ஆட்சி செய்கிறது, ஆனால் மத்திய அமைச்சரவையின் நேரடி அறிவுறுத்தலின் கீழ் செயல்படுகிறது",
        "The Council of Ministers is put in suspended animation and receives half salary", "அமைச்சரவை தற்காலிகமாக நிறுத்தி வைக்கப்பட்டு பாதி ஊதியத்தைப் பெறுகிறது",
        "The Chief Minister becomes the Governor's chief advisor on security", "முதலமைச்சர் பாதுகாப்பில் ஆளுநரின் தலைமை ஆலோசகராக மாறுகிறார்",
        "The Council of Ministers is dismissed, and the President assumes the functions of the Government of the State", "அமைச்சரவை பதவி நீக்கம் செய்யப்படுகிறது, மேலும் மாநில அரசின் செயல்பாடுகளை குடியரசுத் தலைவர் ஏற்றுக்கொள்கிறார்",
        "D",
        "Under Article 356(1)(a), the President declares that he assumes to himself all or any of the functions of the Government of the State and all or any of the powers vested in or exercisable by the Governor. Consequently, the State Council of Ministers headed by the Chief Minister is DISMISSED immediately upon the issuance of the proclamation. (The Governor then administers the state on behalf of the President, assisted by advisors).",
        "சரத்து 356(1)(a)-ன் கீழ், மாநில அரசின் அனைத்து அல்லது ஏதேனும் செயல்பாடுகளையும், ஆளுநருக்கு உள்ள அதிகாரங்களையும் தமதாக்கிக் கொள்வதாக குடியரசுத் தலைவர் பிரகடனம் செய்கிறார். இதன் விளைவாக, முதலமைச்சர் தலைமையிலான மாநில அமைச்சரவை பிரகடனம் வெளியிடப்பட்ட உடனேயே பதவி நீக்கம் செய்யப்படுகிறது. (பின்னர் ஆளுநர் ஆலோசகர்களின் உதவியுடன் குடியரசுத் தலைவரின் சார்பில் மாநிலத்தை நிர்வகிக்கிறார்).",
        "Option A describes the situation under National Emergency (Article 353(a)), NOT President's Rule.", "விருப்பம் A தேசிய அவசரநிலையின் கீழ் (சரத்து 353(a)) உள்ள நிலையைக் குறிக்கிறது, குடியரசுத் தலைவர் ஆட்சியை அல்ல.",
        "Option B is false; the Assembly may be kept in suspended animation, but the Council of Ministers is dismissed outright.", "விருப்பம் B தவறு; சட்டமன்றம் இடைநிறுத்தி வைக்கப்படலாம், ஆனால் அமைச்சரவை உடனடியாக பதவி நீக்கம் செய்யப்படுகிறது.",
        "Option C is fictitious.", "விருப்பம் C கற்பனையானது.",
        "Option D is the precise constitutional and practical consequence under Article 356(1)(a).", "விருப்பம் D சரத்து 356(1)(a)-ன் கீழ் ஏற்படும் துல்லியமான அரசியலமைப்பு மற்றும் நடைமுறை விளைவாகும்.",
        "Crucial Contrast: In National Emergency, State Council of Ministers is NOT dismissed (it remains in office). In President's Rule, State Council of Ministers IS dismissed immediately.",
        "முக்கிய வேறுபாடு: தேசிய அவசரநிலையில் மாநில அமைச்சரவை பதவி நீக்கம் செய்யப்படுவதில்லை (பதவியில் நீடிக்கிறது). குடியரசுத் தலைவர் ஆட்சியில் மாநில அமைச்சரவை உடனடியாக பதவி நீக்கம் செய்யப்படுகிறது.",
        "The Assembly can be kept in suspended animation, but the executive ministry ceases to exist at once.",
        "சட்டமன்றம் தற்காலிகமாக நிறுத்தி வைக்கப்படலாம், ஆனால் நிர்வாக அமைச்சரவை உடனடியாக முடிவுக்கு வருகிறது."
    ))

    # 013 - Key A
    qs.append(make_ep_q(
        PREFIX, 13, DIFF, "Constitutional Comparison", "Article 357 and Validity of Laws after Emergency",
        "Before the 42nd Amendment Act of 1976, what was the constitutional rule regarding laws made by Parliament or the President during President's Rule in a State under Article 357(2)?",
        "1976-ன் 42-வது திருத்தச் சட்டத்திற்கு முன்பு, சரத்து 357(2)-ன் கீழ் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சியின் போது பாராளுமன்றம் அல்லது குடியரசுத் தலைவர் இயற்றிய சட்டங்கள் தொடர்பாக அரசியலமைப்பு விதி என்னவாக இருந்தது?",
        "They ceased to operate upon the expiration of one year after the proclamation had ceased to operate, unless sooner re-enacted by the State Legislature", "மாநில சட்டமன்றத்தால் முன்னரே மீண்டும் இயற்றப்படாவிட்டால், பிரகடனம் முடிவுக்கு வந்த ஒரு வருடம் முடிந்தவுடன் அவை செயல்படுவதை நிறுத்திவிட்டன",
        "They ceased to operate after six months, exactly like Article 250", "சரத்து 250-ஐப் போலவே அவை ஆறு மாதங்களுக்குப் பிறகு செயல்படுவதை நிறுத்திவிட்டன",
        "They remained in force permanently without any possibility of repeal by the State Legislature", "மாநில சட்டமன்றத்தால் ரத்து செய்ய எந்த வாய்ப்பும் இன்றி அவை நிரந்தரமாக அமலில் இருந்தன",
        "They lapsed immediately on the exact day the proclamation was revoked", "பிரகடனம் திரும்பப் பெறப்பட்ட அதே நாளில் அவை உடனடியாக காலாவதியாகிவிட்டன",
        "A",
        "Under the original Article 357(2) of the 1950 Constitution, any law made by Parliament or the President for a State during President's Rule ceased to have effect on the expiration of ONE YEAR after the proclamation ceased to operate, unless sooner repealed or re-enacted by the State Legislature. The 42nd Amendment Act 1976 amended this to state that such laws continue in force until altered, repealed, or amended by the competent legislature.",
        "1950 மூல அரசியலமைப்பின் சரத்து 357(2)-ன் கீழ், குடியரசுத் தலைவர் ஆட்சியின் போது பாராளுமன்றம் அல்லது குடியரசுத் தலைவர் இயற்றிய எந்தவொரு சட்டமும், மாநில சட்டமன்றத்தால் முன்னரே ரத்து செய்யப்படாவிட்டால் அல்லது மீண்டும் இயற்றப்படாவிட்டால், பிரகடனம் முடிந்து ஒரு வருடம் முடிந்தவுடன் காலாவதியானது. 1976-ன் 42-வது திருத்தச் சட்டம் இதை மாற்றி, மாநில சட்டமன்றம் ரத்து செய்யும் வரை அவை தொடர்ந்து அமலில் இருக்கும் என்று அமைத்தது.",
        "Option A accurately states the historic pre-1976 rule under Article 357(2).", "விருப்பம் A சரத்து 357(2)-ன் கீழ் 1976-க்கு முந்தைய வரலாற்று விதியைத் துல்லியமாகக் கூறுகிறது.",
        "Option B (6 months) is the Article 250 rule for National Emergency.", "விருப்பம் B (6 மாதங்கள்) தேசிய அவசரநிலைக்கான சரத்து 250 விதியாகும்.",
        "Option C is false; state legislatures can always repeal them.", "விருப்பம் C தவறு; மாநில சட்டமன்றங்கள் எப்போதும் அவற்றை ரத்து செய்யலாம்.",
        "Option D is false.", "விருப்பம் D தவறானது.",
        "Article 357 Evolution: Pre-1976: Lapsed after 1 year unless re-enacted. Post-1976: Continues indefinitely until altered/repealed by State Legislature.",
        "சரத்து 357 பரிணாமம்: 1976-க்கு முன்: மீண்டும் இயற்றப்படாவிட்டால் 1 ஆண்டில் காலாவதியானது. 1976-க்கு பின்: மாநில சட்டமன்றத்தால் மாற்றப்படும் வரை காலவரையின்றி தொடர்கிறது.",
        "This reform eliminated the legislative scramble where dozens of state laws suddenly lapsed after elections.",
        "தேர்தலுக்குப் பிறகு டஜன் கணக்கான மாநிலச் சட்டங்கள் திடீரென காலாவதியாகும் சட்ட நெருக்கடியை இந்த சீர்திருத்தம் நீக்கியது."
    ))

    # 014 - Key B
    qs.append(make_ep_q(
        PREFIX, 14, DIFF, "Constitutional Comparison", "Financial Emergency and Union Control over State Finances",
        "Under Article 360(3), during a Financial Emergency, the executive authority of the Union extends to giving directions to any State to observe which specific financial standards?",
        "சரத்து 360(3)-ன் கீழ், நிதி அவசரநிலையின் போது, எந்த குறிப்பிட்ட நிதித் தரங்களைப் பின்பற்றுமாறு எந்தவொரு மாநிலத்திற்கும் வழிகாட்டுதல்களை வழங்க மத்திய அரசின் நிர்வாக அதிகாரம் விரிவடைகிறது?",
        "Strict compliance with International Monetary Fund fiscal deficit caps", "சர்வதேச நாணய நிதியத்தின் நிதிப் பற்றாக்குறை வரம்புகளை கண்டிப்பாகப் பின்பற்றுதல்",
        "Such canons of financial propriety as may be specified in the central directions", "மத்திய அரசின் வழிகாட்டுதல்களில் குறிப்பிடப்படக்கூடிய நிதி ஒழுங்கு நெறிமுறைகள் (canons of financial propriety)",
        "Mandatory transfer of 50% of state sales tax revenues directly to the Reserve Bank of India", "மாநில விற்பனை வரி வருவாயில் 50%-ஐ நேரடியாக இந்திய ரிசர்வ் வங்கிக்கு கட்டாயமாக மாற்றுதல்",
        "Prohibition of all welfare expenditure on public education and health", "பொதுக் கல்வி மற்றும் சுகாதாரம் மீதான அனைத்து நலத்திட்டச் செலவுகளுக்கும் தடை விதித்தல்",
        "B",
        "Article 360(3) provides: 'During the period any such Proclamation is in operation, the executive authority of the Union shall extend to the giving of directions to any State to observe such canons of financial propriety as may be specified in the directions, and to the giving of such other directions as the President may deem necessary and adequate for the purpose.'",
        "சரத்து 360(3) கூறுகிறது: 'அத்தகைய பிரகடனம் அமலில் இருக்கும் காலத்தில், மத்திய அரசின் வழிகாட்டுதல்களில் குறிப்பிடப்படக்கூடிய நிதி ஒழுங்கு நெறிமுறைகளைப் (canons of financial propriety) பின்பற்றுமாறு எந்தவொரு மாநிலத்திற்கும் வழிகாட்டுதல்களை வழங்குவதற்கும், மற்றும் அக்குறிக்கோளுக்காக குடியரசுத் தலைவர் அவசியமெனக் கருதும் பிற வழிகாட்டுதல்களை வழங்குவதற்கும் ஒன்றியத்தின் நிர்வாக அதிகாரம் விரிவடையும்.'",
        "Option A is incorrect; foreign or international agencies have no constitutional mention.", "விருப்பம் A தவறானது; சர்வதேச அமைப்புகள் பற்றி அரசியலமைப்பில் குறிப்பிடப்படவில்லை.",
        "Option B verbatim captures the constitutional phrase 'canons of financial propriety' in Article 360(3).", "விருப்பம் B சரத்து 360(3)-ல் உள்ள 'நிதி ஒழுங்கு நெறிமுறைகள்' என்ற துல்லியமான அரசியலமைப்புச் சொல்லைக் கொண்டுள்ளது.",
        "Option C is baseless.", "விருப்பம் C அடிப்படையற்றது.",
        "Option D is an extreme and unconstitutional assumption.", "விருப்பம் D தீவிரமான மற்றும் அரசியலமைப்பிற்கு எதிரான அனுமானம்.",
        "Key Constitutional Phrase: 'Canons of financial propriety' under Article 360(3) empowers the Centre to dictate fiscal discipline to any state.",
        "முக்கிய அரசியலமைப்புச் சொல்: சரத்து 360(3)-ன் கீழான 'நிதி ஒழுங்கு நெறிமுறைகள்' எந்தவொரு மாநிலத்திற்கும் நிதி ஒழுக்கத்தை கட்டளையிட மத்திய அரசுக்கு அதிகாரம் அளிக்கிறது.",
        "This turns the federal fiscal structure completely unitary for the duration of the financial emergency.",
        "இது நிதி அவசரநிலையின் போது கூட்டாட்சி நிதி அமைப்பை முற்றிலும் ஒற்றையாட்சி அமைப்பாக மாற்றுகிறது."
    ))

    # 015 - Key C
    qs.append(make_ep_q(
        PREFIX, 15, DIFF, "Constitutional Landmark", "Article 356 and Dissolution of 9 Assemblies (1977 & 1980)",
        "In State of Rajasthan v. Union of India (1977), the Supreme Court upheld the wholesale dissolution of nine Congress-ruled State Assemblies by the Janata Party government primarily on what ground?",
        "ராஜஸ்தான் அரசு எதிர் இந்திய ஒன்றியம் (1977) வழக்கில், ஜனதா கட்சி அரசாங்கத்தால் ஒன்பது காங்கிரஸ் ஆளும் மாநில சட்டமன்றங்கள் மொத்தமாகக் கலைக்கப்பட்டதை உச்ச நீதிமன்றம் முதன்மையாக எந்த அடிப்படையில் உறுதி செய்தது?",
        "Failure of the nine States to pay income tax surcharges to the Union", "மத்திய அரசுக்கு ஒன்பது மாநிலங்கள் வருமான வரி கூடுதல் கட்டணங்களை செலுத்தத் தவறியமை",
        "A formal declaration of Financial Emergency under Article 360", "சரத்து 360-ன் கீழான நிதி அவசரநிலையின் முறையான பிரகடனம்",
        "The massive defeat of the ruling party in those states in the Lok Sabha elections demonstrated that the state governments had lost the confidence of the electorate, reflecting a breakdown of constitutional machinery", "மக்களவைத் தேர்தலில் அந்த மாநிலங்களில் ஆளும் கட்சி அடைந்த பெரும் தோல்வி, மாநில அரசுகள் வாக்காளர்களின் நம்பிக்கையை இழந்துவிட்டதை நிரூபித்தது, இது அரசியலமைப்பு இயந்திரத்தின் முறிவை வெளிப்படுத்தியது",
        "Unanimous recommendations submitted by the Election Commission of India under Article 324", "சரத்து 324-ன் கீழ் இந்திய தேர்தல் ஆணையத்தால் சமர்ப்பிக்கப்பட்ட ஒருமனதான பரிந்துரைகள்",
        "C",
        "In State of Rajasthan v. Union of India (1977), a 7-judge Constitution Bench held that the sweeping verdict in the 1977 Lok Sabha elections, where the Congress party suffered a complete rout in northern states, created an unprecedented situation where the state governments could be said to have lost the mandate of the electorate. The Court refused to interfere, holding that the satisfaction under Article 356 was largely a political question. (In 1980, Indira Gandhi reciprocated by dismissing nine non-Congress state governments on the exact same precedent).",
        "ராஜஸ்தான் அரசு எதிர் இந்திய ஒன்றியம் (1977) வழக்கில், 7 நீதிபதிகள் கொண்ட அமர்வு, 1977 மக்களவைத் தேர்தலில் வடக்கு மாநிலங்களில் காங்கிரஸ் கட்சி சந்தித்த படுதோல்வி காரணமாக, மாநில அரசுகள் மக்களின் நம்பிக்கையை இழந்துவிட்டதாகக் கருதக்கூடிய அசாதாரண சூழ்நிலை ஏற்பட்டதாக தீர்ப்பளித்தது. சரத்து 356-ன் கீழான திருப்தி ஒரு அரசியல் கேள்வி என்று கூறி நீதிமன்றம் தலையிட மறுத்தது. (1980-ல் இந்திரா காந்தி மீண்டும் ஆட்சிக்கு வந்ததும் இதே முன்னுதாரணத்தைப் பயன்படுத்தி ஒன்பது காங்கிரஸ் அல்லாத மாநில அரசுகளைக் கலைத்தார்).",
        "Option A is irrelevant.", "விருப்பம் A தொடர்பற்றது.",
        "Option B is false; financial emergency was never declared.", "விருப்பம் B தவறு; நிதி அவசரநிலை ஒருபோதும் அறிவிக்கப்படவில்லை.",
        "Option C is the exact legal rationale upheld in the 1977 Rajasthan judgment.", "விருப்பம் C என்பது 1977 ராஜஸ்தான் தீர்ப்பில் உறுதி செய்யப்பட்ட துல்லியமான சட்ட நியாயமாகும்.",
        "Option D is false.", "விருப்பம் D தவறானது.",
        "Pre-Bommai Precedent: In 1977 and 1980, wholesale dismissal of 9 state assemblies was justified on the basis of Lok Sabha election results. Bommai (1994) subsequently declared this unconstitutional.",
        "பொம்மைக்கு முந்தைய முன்னுதாரணம்: 1977 மற்றும் 1980-ல், மக்களவைத் தேர்தல் முடிவுகளின் அடிப்படையில் 9 மாநில சட்டமன்றங்கள் மொத்தமாகக் கலைக்கப்பட்டது நியாயப்படுத்தப்பட்டது. பின்னர் பொம்மை (1994) வழக்கு இதை அரசியலமைப்பிற்கு எதிரானது என அறிவித்தது.",
        "The Bommai judgment firmly decoupled national parliamentary election outcomes from state legislative mandates.",
        "பொம்மை தீர்ப்பு தேசிய பாராளுமன்ற தேர்தல் முடிவுகளை மாநில சட்டமன்ற அங்கீகாரத்திலிருந்து திட்டவட்டமாகப் பிரித்தது."
    ))

    # 016 - Key D
    qs.append(make_ep_q(
        PREFIX, 16, DIFF, "Constitutional Comparison", "59th Amendment Act 1988 (Punjab Emergency)",
        "The 59th Constitutional Amendment Act of 1988 made which radical, highly controversial change regarding Emergency Provisions in relation to the State of Punjab?",
        "1988-ஆம் ஆண்டின் 59-வது அரசியலமைப்பு திருத்தச் சட்டம், பஞ்சாப் மாநிலம் தொடர்பாக அவசரநிலைப் பிரிவுகளில் எந்த தீவிரமான மற்றும் சர்ச்சைக்குரிய மாற்றத்தைச் செய்தது?",
        "It abolished the High Court of Punjab and Haryana permanently", "அது பஞ்சாப் மற்றும் ஹரியானா உயர் நீதிமன்றத்தை நிரந்தரமாக ரத்து செய்தது",
        "It extended President's Rule in Punjab to an unlimited period of 10 years", "அது பஞ்சாபில் குடியரசுத் தலைவர் ஆட்சியை வரம்பற்ற 10 ஆண்டு காலத்திற்கு நீட்டித்தது",
        "It made Punjab a Union Territory without a legislature", "அது பஞ்சாபை சட்டமன்றம் இல்லாத ஒரு யூனியன் பிரதேசமாக மாற்றியது",
        "It allowed a National Emergency to be proclaimed in Punjab on the ground of 'internal disturbance' and permitted the suspension of Article 21 in Punjab", "அது 'உள்நாட்டுக் குழப்பம்' என்ற காரணத்தின் அடிப்படையில் பஞ்சாபில் தேசிய அவசரநிலையை அறிவிக்க அனுமதித்தது மற்றும் பஞ்சாபில் சரத்து 21-ஐ இடைநிறுத்த அனுமதித்தது",
        "D",
        "The 59th Amendment Act 1988 amended Article 352 to allow National Emergency to be declared in Punjab (or any part thereof) on the ground of 'internal disturbance' (which had been abolished by the 44th CAA) and, shockingly, amended Article 359 to permit the suspension of Article 21 in Punjab. This draconian amendment caused immense public outcry and was completely repealed by the 63rd Constitutional Amendment Act in 1989.",
        "1988-ன் 59-வது திருத்தச் சட்டம், சரத்து 352-ஐத் திருத்தி பஞ்சாபில் 'உள்நாட்டுக் குழப்பம்' என்ற காரணத்திற்காக தேசிய அவசரநிலையை அறிவிக்கவும் (இது 44-வது சட்டத்தால் நீக்கப்பட்டிருந்தது), மேலும் அதிர்ச்சிகரமாக சரத்து 359-ஐத் திருத்தி பஞ்சாபில் சரத்து 21-ஐ இடைநிறுத்தவும் அனுமதித்தது. இந்த கடுமையான திருத்தம் பெரும் மக்கள் எதிர்ப்பை ஏற்படுத்தியதால், 1989-ல் 63-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் முற்றிலும் ரத்து செய்யப்பட்டது.",
        "Option A is false.", "விருப்பம் A தவறானது.",
        "Option B confuses the 59th amendment with the subsequent 64th/67th/68th amendments which extended President's Rule to 5 years.", "விருப்பம் B குடியரசுத் தலைவர் ஆட்சியை 5 ஆண்டுகளாக நீட்டித்த 64, 67, 68-வது திருத்தங்களுடன் குழப்பிக் கொள்கிறது.",
        "Option C is false.", "விருப்பம் C தவறானது.",
        "Option D precisely captures the extraordinary and dangerous provisions of the 59th Amendment Act 1988.", "விருப்பம் D 1988-ன் 59-வது திருத்தச் சட்டத்தின் அசாதாரண மற்றும் ஆபத்தான விதிகளை துல்லியமாக விவரிக்கிறது.",
        "59th CAA (1988) vs 63rd CAA (1989): 59th CAA brought back 'internal disturbance' and suspension of Art 21 for Punjab; 63rd CAA repealed it entirely.",
        "59-வது திருத்தம் (1988) vs 63-வது திருத்தம் (1989): 59-வது திருத்தம் பஞ்சாபிற்கு 'உள்நாட்டுக் குழப்பம்' மற்றும் சரத்து 21 இடைநிறுத்தத்தை மீண்டும் கொண்டுவந்தது; 63-வது திருத்தம் அதை முற்றிலும் ரத்து செய்தது.",
        "This brief episode highlighted how fragile civil liberties can become under anti-terror legislative pressure.",
        "பயங்கரவாத எதிர்ப்பு சட்ட அழுத்தங்களின் கீழ் குடிமை உரிமைகள் எவ்வளவு பலவீனமடையக்கூடும் என்பதை இந்த குறுகிய கால நிகழ்வு எடுத்துக்காட்டியது."
    ))

    # 017 - Key A
    qs.append(make_ep_q(
        PREFIX, 17, DIFF, "Constitutional Comparison", "Article 356 - Floor Test Mandate",
        "According to S.R. Bommai (1994), when can a Governor legitimately recommend President's Rule without holding a floor test on the floor of the Assembly?",
        "எஸ்.ஆர். பொம்மை (1994) தீர்ப்பின்படி, சட்டமன்றத் தளத்தில் நம்பிக்கை வாக்கெடுப்பு நடத்தாமலேயே ஓர் ஆளுநர் எப்போது நியாயமாக குடியரசுத் தலைவர் ஆட்சிக்குப் பரிந்துரைக்க முடியும்?",
        "Only when all-pervasive violence, physical intimidation, or total breakdown makes it objectively impossible to convene a session of the Assembly", "அனைத்து இடங்களிலும் பரவிய வன்முறை, அச்சுறுத்தல் அல்லது முழுமையான முறிவு காரணமாக சட்டமன்றக் கூட்டத்தைக் கூட்டுவது முற்றிலும் சாத்தியமற்றதாக இருக்கும் போது மட்டுமே",
        "Whenever the Governor's personal intelligence source claims that ministers are taking bribes", "அமைச்சர்கள் லஞ்சம் வாங்குவதாக ஆளுநரின் தனிப்பட்ட உளவுத்துறை வட்டாரம் கூறும் போதெல்லாம்",
        "Whenever the ruling party in the State loses a municipal corporation election", "மாநிலத்தில் ஆளும் கட்சி மாநகராட்சித் தேர்தலில் தோல்வியடையும் போதெல்லாம்",
        "Whenever the Chief Minister belongs to a regional party that refuses to join the national ruling coalition", "முதலமைச்சர் தேசிய ஆளும் கூட்டணியில் இணைய மறுக்கும் பிராந்திய கட்சியைச் சேர்ந்தவராக இருக்கும் போதெல்லாம்",
        "A",
        "In S.R. Bommai (1994), the Supreme Court ruled that a floor test is mandatory and indispensable in all ordinary situations. The ONLY rare exception where a floor test can be dispensed with is where widespread violence, terror, or breakdown of physical security makes it objectively impossible to hold a session of the Assembly to test the majority.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், அனைத்து சாதாரண சூழ்நிலைகளிலும் நம்பிக்கை வாக்கெடுப்பு (Floor test) கட்டாயமானது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. பரவலான வன்முறை, பயங்கரவாதம் அல்லது பாதுகாப்பின்மை காரணமாக சட்டமன்றக் கூட்டத்தைக் கூட்டி பெரும்பான்மையைச் சோதிப்பது முற்றிலும் சாத்தியமற்றதாக இருக்கும் மிக அரிதான சூழ்நிலையில் மட்டுமே நம்பிக்கை வாக்கெடுப்பு இன்றி ஆளுநர் செயல்பட முடியும்.",
        "Option A is the singular, extreme constitutional exception recognized by the Supreme Court in Bommai.", "விருப்பம் A என்பது பொம்மை வழக்கில் உச்ச நீதிமன்றத்தால் அங்கீகரிக்கப்பட்ட ஒரே ஒரு தீவிர அரசியலமைப்பு விதிவிலக்காகும்.",
        "Option B is partisan and rejected by the Supreme Court.", "விருப்பம் B தன்னிச்சையானது மற்றும் உச்ச நீதிமன்றத்தால் நிராகரிக்கப்பட்டது.",
        "Option C is improper and condemned by the Supreme Court.", "விருப்பம் C தவறானது மற்றும் உச்ச நீதிமன்றத்தால் கண்டிக்கப்பட்டது.",
        "Option D is malafide and unconstitutional.", "விருப்பம் D உள்நோக்கம் கொண்டது மற்றும் அரசியலமைப்பிற்கு எதிரானது.",
        "Floor Test Rule: Floor test is mandatory. Dispensing with it is permissible ONLY when physical violence makes convening the Assembly impossible.",
        "நம்பிக்கை வாக்கெடுப்பு விதி: நம்பிக்கை வாக்கெடுப்பு கட்டாயம். சட்டமன்றத்தைக் கூட்டுவது வன்முறையால் சாத்தியமற்றதாக இருக்கும் போது மட்டுமே இதற்கு விதிவிலக்கு அனுமதிக்கப்படும்.",
        "The Governor's subjective assessment can never replace the objective counting of votes on the floor of the House.",
        "ஆளுநரின் அகநிலை மதிப்பீடு ஒருபோதும் அவையின் தளத்தில் வாக்குகளை எண்ணும் புறநிலை கணக்கீட்டிற்கு மாற்றாக முடியாது."
    ))

    # 018 - Key B
    qs.append(make_ep_q(
        PREFIX, 18, DIFF, "Constitutional Comparison", "Emergency Provisions - Article 361 Presidential Immunity",
        "Under Article 361, the President is not answerable to any court for the exercise and performance of the powers and duties of his office. How does the Supreme Court reconcile this immunity with the judicial review of a proclamation under Article 356 or Article 352?",
        "சரத்து 361-ன் கீழ், குடியரசுத் தலைவர் தனது அலுவலகத்தின் அதிகாரங்கள் மற்றும் கடமைகளைச் செயல்படுத்துவதற்கு எந்தவொரு நீதிமன்றத்திற்கும் பதிலளிக்க வேண்டியதில்லை. இந்த பாதுகாப்பை சரத்து 356 அல்லது 352-ன் கீழான பிரகடனத்தின் மீதான நீதித்துறை மறுஆய்வுடன் உச்ச நீதிமன்றம் எவ்வாறு ஒருங்கிணைக்கிறது?",
        "Courts cannot review emergency proclamations at all because the President's personal immunity bars all legal actions", "குடியரசுத் தலைவரின் தனிப்பட்ட பாதுகாப்பு அனைத்து சட்ட நடவடிக்கைகளையும் தடுப்பதால் நீதிமன்றங்களால் அவசரநிலைப் பிரகடனங்களை மறுஆய்வு செய்யவே முடியாது",
        "The President personally cannot be sued, but the Union Government is made party to the petition, and the validity of the proclamation issued on the Cabinet's advice is fully justiciable", "குடியரசுத் தலைவர் மீது தனிப்பட்ட முறையில் வழக்குத் தொடர முடியாது, ஆனால் மத்திய அரசு மனுவில் எதிர்மனுதாரராக சேர்க்கப்படுகிறது, மேலும் அமைச்சரவையின் ஆலோசனையின் பேரில் வெளியிடப்பட்ட பிரகடனத்தின் செல்லுபடியாகும் தன்மை முழுமையாக நீதித்துறை ஆய்வுக்கு உட்பட்டது",
        "Article 361 is automatically suspended whenever any proclamation of emergency is promulgated", "எந்தவொரு அவசரநிலைப் பிரகடனம் வெளியிடப்படும் போதெல்லாம் சரத்து 361 தானாகவே இடைநிறுத்தப்படும்",
        "Judicial review can take place only after the President's 5-year term ends and he leaves office", "குடியரசுத் தலைவரின் 5 ஆண்டு பதவிக்காலம் முடிந்து அவர் பதவியை விட்டு வெளியேறிய பிறகு மட்டுமே நீதித்துறை மறுஆய்வு செய்ய முடியும்",
        "B",
        "In S.R. Bommai (1994) and Rameshwar Prasad (2006), the Supreme Court clarified the relationship between Article 361 and judicial review: While Article 361 grants complete personal immunity to the President (he cannot be named as a respondent in court), the proclamation itself is issued on the binding advice of the Council of Ministers under Article 74. The Union of India is sued, and the court can examine the validity, legality, and bona fides of the Cabinet's advice and materials.",
        "பொம்மை (1994) மற்றும் ராமேஷ்வர் பிரசாத் (2006) வழக்குகளில், சரத்து 361 மற்றும் நீதித்துறை மறுஆய்வு ஆகியவற்றுக்கு இடையேயான தொடர்பை உச்ச நீதிமன்றம் தெளிவுபடுத்தியது: சரத்து 361 குடியரசுத் தலைவருக்கு தனிப்பட்ட பாதுகாப்பை அளித்தாலும் (அவரை நீதிமன்றத்தில் எதிர்மனுதாரராகச் சேர்க்க முடியாது), பிரகடனமே சரத்து 74-ன் கீழ் அமைச்சரவையின் கட்டாய ஆலோசனையின் பேரிலேயே வெளியிடப்படுகிறது. எனவே இந்திய ஒன்றியம் எதிர்மனுதாரராக சேர்க்கப்பட்டு, அமைச்சரவையின் ஆலோசனைகள் மற்றும் ஆதாரங்களின் சட்டப்பூர்வத்தன்மையை நீதிமன்றம் முழுமையாக ஆராய முடியும்.",
        "Option A is rejected constitutional jurisprudence.", "விருப்பம் A நிராகரிக்கப்பட்ட அரசியலமைப்பு வாதமாகும்.",
        "Option B is the precise constitutional doctrine harmonizing Article 361 immunity with Rule of Law and judicial review.", "விருப்பம் B சரத்து 361-ன் பாதுகாப்பை சட்டத்தின் ஆட்சி மற்றும் நீதித்துறை மறுஆய்வுடன் இணைக்கும் துல்லியமான கோட்பாடாகும்.",
        "Option C is false; Article 361 is never suspended.", "விருப்பம் C தவறு; சரத்து 361 ஒருபோதும் இடைநிறுத்தப்படுவதில்லை.",
        "Option D would render judicial remedies completely illusory.", "விருப்பம் D நீதித்துறை தீர்வுகளை முற்றிலும் பயனற்றதாக்கிவிடும்.",
        "Harmonious Principle: Article 361 protects the person of the President; it does NOT immunize the presidential proclamation or the Union Cabinet's action from judicial review.",
        "ஒருங்கிணைப்புக் கொள்கை: சரத்து 361 குடியரசுத் தலைவரின் தனிநபரைப் பாதுகாக்கிறது; அது குடியரசுத் தலைவரின் பிரகடனத்தையோ அல்லது மத்திய அமைச்சரவையின் நடவடிக்கையையோ நீதித்துறை மறுஆய்விலிருந்து பாதுகாக்காது.",
        "This ensures that executive accountability remains alive even when the formal order is signed by the Head of State.",
        "முறையான ஆணையில் நாட்டின் தலைவர் கையெழுத்திட்டாலும் கூட, நிர்வாகப் பொறுப்புடைமை நீடிப்பதை இது உறுதி செய்கிறது."
    ))

    # 019 - Key C
    qs.append(make_ep_q(
        PREFIX, 19, DIFF, "Constitutional Comparison", "Article 352 Effect on Seventh Schedule",
        "During a National Emergency, does the distribution of legislative powers between the Union and the States under the Seventh Schedule get suspended?",
        "தேசிய அவசரநிலையின் போது, ஏழாவது அட்டவணையின் கீழ் மத்திய மற்றும் மாநில அரசுகளுக்கு இடையேயான சட்டமியற்றும் அதிகாரப் பகிர்வு இடைநிறுத்தப்படுகிறதா?",
        "Yes, the State List is automatically deleted and merged into the Union List during the emergency", "ஆம், அவசரநிலையின் போது மாநிலப் பட்டியல் தானாகவே நீக்கப்பட்டு மத்தியப் பட்டியலுடன் இணைக்கப்படுகிறது",
        "Yes, State Legislatures are completely prohibited from introducing any bills during the emergency", "ஆம், அவசரநிலையின் போது மாநில சட்டமன்றங்கள் எந்தவொரு மசோதாவையும் அறிமுகப்படுத்த முற்றிலும் தடை விதிக்கப்படுகிறது",
        "No, the distribution of powers is not suspended; the State Legislature continues to have concurrent power to make laws on State List subjects, but in case of repugnancy, the law made by Parliament prevails under Article 251", "இல்லை, அதிகாரப் பகிர்வு இடைநிறுத்தப்படுவதில்லை; மாநில சட்டமன்றம் மாநிலப் பட்டியல் விவகாரங்களில் தொடர்ந்து சட்டம் இயற்றும் அதிகாரத்தைக் கொண்டுள்ளது, ஆனால் முரண்பாடு ஏற்பட்டால் சரத்து 251-ன் கீழ் பாராளுமன்றத்தின் சட்டமே மேலோங்கும்",
        "Yes, but only for the six subjects enumerated in the Concurrent List", "ஆம், ஆனால் பொதுப்பட்டியலில் உள்ள ஆறு விவகாரங்களுக்கு மட்டுமே",
        "C",
        "A vital TNPSC concept: During a National Emergency under Article 352, the legislative distribution is NOT suspended. The State Legislature is NOT dissolved or suspended; it continues to enact laws on State List subjects. However, Parliament acquires overriding concurrent power to make laws on any State List subject under Article 250. Under Article 251, if there is a conflict between a state law and a parliamentary law, the parliamentary law prevails to the extent of repugnancy.",
        "ஒரு முக்கியமான TNPSC கருத்து: சரத்து 352-ன் கீழான தேசிய அவசரநிலையின் போது, சட்டப் பகிர்வு இடைநிறுத்தப்படுவதில்லை. மாநில சட்டமன்றம் கலைக்கப்படவோ முடக்கப்படவோ மாட்டாது; அது மாநிலப் பட்டியல் விவகாரங்களில் தொடர்ந்து சட்டங்களை இயற்றலாம். இருப்பினும், சரத்து 250-ன் கீழ் மாநிலப் பட்டியல் மீது சட்டம் இயற்றும் மேலோங்கும் அதிகாரத்தை பாராளுமன்றம் பெறுகிறது. சரத்து 251-ன் படி, மாநில சட்டத்திற்கும் பாராளுமன்ற சட்டத்திற்கும் முரண்பாடு ஏற்பட்டால், பாராளுமன்ற சட்டமே மேலோங்கும்.",
        "Option A is false; Seventh Schedule is not altered textually.", "விருப்பம் A தவறு; ஏழாவது அட்டவணை எழுத்துப்பூர்வமாக மாற்றப்படுவதில்லை.",
        "Option B is false; state legislatures continue functioning normally.", "விருப்பம் B தவறு; மாநில சட்டமன்றங்கள் வழக்கம் போல் செயல்படுகின்றன.",
        "Option C is the accurate constitutional formulation governing legislative interplay under Articles 250 and 251.", "விருப்பம் C சரத்துகள் 250 மற்றும் 251-ன் கீழான சட்ட நடைமுறைகளை விளக்கும் சரியான அரசியலமைப்பு விதியாகும்.",
        "Option D is meaningless.", "விருப்பம் D அர்த்தமற்றது.",
        "Concurrent Co-existence: State legislatures retain law-making powers during National Emergency; Parliament gets parallel overriding power.",
        "இணை இயக்கம்: தேசிய அவசரநிலையின் போது மாநில சட்டமன்றங்கள் சட்டம் இயற்றும் அதிகாரத்தைத் தக்கவைத்துக் கொள்கின்றன; பாராளுமன்றம் கூடுதல் மேலோங்கும் அதிகாரத்தைப் பெறுகிறது.",
        "Contrast this with President's Rule, where the State Legislature's power is completely taken over by Parliament.",
        "குடியரசுத் தலைவர் ஆட்சியில் மாநில சட்டமன்றத்தின் அதிகாரம் பாராளுமன்றத்தால் முழுமையாக எடுத்துக் கொள்ளப்படுவதோடு இதை ஒப்பிட்டுப் பார்க்கவும்."
    ))

    # 020 - Key D
    qs.append(make_ep_q(
        PREFIX, 20, DIFF, "Constitutional Comparison", "Failure to Comply with Central Directions (Article 365)",
        "Under what specific circumstance does Article 365 create a constitutional presumption that the government of a State cannot be carried on in accordance with the Constitution?",
        "எந்தக் குறிப்பிட்ட சூழ்நிலையில் சரத்து 365, ஒரு மாநிலத்தின் ஆட்சி அரசியலமைப்பு விதிகளின்படி நடைபெற முடியாது என்ற அரசியலமைப்பு அனுமானத்தை உருவாக்குகிறது?",
        "When the State government fails to achieve 100% literacy within five years", "மாநில அரசு ஐந்து ஆண்டுகளுக்குள் 100% எழுத்தறிவை அடையத் தவறினால்",
        "When the State Cabinet fails to include at least one member from each recognized tribal community", "மாநில அமைச்சரவையில் அங்கீகரிக்கப்பட்ட ஒவ்வொரு பழங்குடியின சமூகத்திலிருந்தும் குறைந்தது ஒரு உறுப்பினராவது சேர்க்கத் தவறினால்",
        "When the State Legislative Assembly fails to pass the annual budget on the first day of the budget session", "சட்டமன்றப் பேரவை வரவுசெலவுத் திட்டக் கூட்டத்தொடரின் முதல் நாளிலேயே ஆண்டு வரவுசெலவுத் திட்டத்தை நிறைவேற்றத் தவறினால்",
        "When any State fails to comply with, or to give effect to, any directions given in the exercise of the executive power of the Union under any of the provisions of the Constitution", "அரசியலமைப்பின் எந்தவொரு விதியின் கீழும் ஒன்றியத்தின் நிர்வாக அதிகாரத்தைப் பயன்படுத்தி வழங்கப்படும் வழிகாட்டுதல்களை எந்தவொரு மாநிலமும் பின்பற்றவோ அல்லது செயல்படுத்தவோ தவறினால்",
        "D",
        "Article 365 provides: 'Where any State has failed to comply with, or to give effect to, any directions given in the exercise of the executive power of the Union under any of the provisions of this Constitution, it shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of this Constitution.' This deems a constitutional breakdown, empowering invocation of Article 356.",
        "சரத்து 365 கூறுகிறது: 'இந்த அரசியலமைப்பின் எந்தவொரு விதியின் கீழும் ஒன்றியத்தின் நிர்வாக அதிகாரத்தைப் பயன்படுத்தி வழங்கப்படும் வழிகாட்டுதல்களை ஒரு மாநிலம் பின்பற்றவோ அல்லது செயல்படுத்தவோ தவறினால், அந்த மாநில அரசு அரசியலமைப்பு விதிகளின்படி இயங்க முடியாத சூழ்நிலை ஏற்பட்டுவிட்டதாகக் கருதுவது குடியரசுத் தலைவருக்குச் சட்டப்பூர்வமானது.' இது அரசியலமைப்பு முறிவாகக் கருதப்பட்டு, சரத்து 356-ஐப் பயன்படுத்த அதிகாரம் அளிக்கிறது.",
        "Option A is a non-existent constitutional standard.", "விருப்பம் A அரசியலமைப்பில் இல்லாத ஒரு விதியாகும்.",
        "Option B is not required under the Constitution.", "விருப்பம் B அரசியலமைப்பின் கீழ் தேவையில்லை.",
        "Option C is false and fabricated.", "விருப்பம் C தவறானது மற்றும் கற்பனையானது.",
        "Option D verbatim quotes the foundational legal text of Article 365.", "விருப்பம் D சரத்து 365-ன் அடிப்படையான சட்ட உரையை அப்படியே மேற்கோள் காட்டுகிறது.",
        "Article 365 = Legal Trigger: Defiance of lawful Union executive directions triggers the deemed breakdown of constitutional machinery under Article 356.",
        "சரத்து 365 = சட்டப்பூர்வ தூண்டுதல்: சட்டப்பூர்வமான மத்திய நிர்வாக வழிகாட்டுதல்களை மீறுவது சரத்து 356-ன் கீழ் அரசியலமைப்பு இயந்திர முறிவைத் தூண்டுகிறது.",
        "Examples include directions under Article 256 (compliance with Union laws) and Article 257 (protection of railways, national highways).",
        "சரத்து 256 (மத்திய சட்டங்களைப் பின்பற்றுதல்) மற்றும் சரத்து 257 (ரயில்வே, தேசிய நெடுஞ்சாலைகளைப் பாதுகாத்தல்) ஆகியவற்றின் கீழான வழிகாட்டுதல்கள் இதில் அடங்கும்."
    ))

    # 021 - Key A
    qs.append(make_ep_q(
        PREFIX, 21, DIFF, "Constitutional Comparison", "Article 356 Proclamation Revocation",
        "How can a proclamation of President's Rule under Article 356 be revoked, and does such revocation require parliamentary approval?",
        "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சிப் பிரகடனம் எவ்வாறு திரும்பப் பெறப்படலாம், மேலும் அத்தகைய திரும்பப் பெறுதலுக்கு பாராளுமன்ற ஒப்புதல் தேவையா?",
        "It can be revoked by the President at any time by a subsequent proclamation, and such revoking proclamation DOES NOT require parliamentary approval", "குடியரசுத் தலைவர் எந்த நேரத்திலும் பிந்தைய பிரகடனம் மூலம் அதைத் திரும்பப் பெறலாம், மேலும் அத்தகைய திரும்பப் பெறும் பிரகடனத்திற்கு பாராளுமன்ற ஒப்புதல் தேவையில்லை",
        "It can be revoked only after a joint resolution is passed by both Houses of Parliament with a two-thirds majority", "பாராளுமன்றத்தின் இரு அவைகளும் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் கூட்டுத் தீர்மானம் நிறைவேற்றிய பிறகு மட்டுமே அதைத் திரும்பப் பெற முடியும்",
        "It can be revoked only if the State High Court certifies that normalcy has returned", "இயல்பு நிலை திரும்பிவிட்டது என்று மாநில உயர் நீதிமன்றம் சான்றளித்தால் மட்டுமே அதைத் திரும்பப் பெற முடியும்",
        "It can be revoked only by the Governor acting on the advice of the dismissed Chief Minister", "பதவி நீக்கம் செய்யப்பட்ட முதலமைச்சரின் ஆலோசனையின் பேரில் செயல்படும் ஆளுநரால் மட்டுமே அதைத் திரும்பப் பெற முடியும்",
        "A",
        "Under Article 356(2), any proclamation issued under Article 356 may be revoked or varied by a subsequent proclamation by the President. Unlike the initial proclamation or extension, a revoking proclamation does NOT require approval by Parliament.",
        "சரத்து 356(2)-ன் கீழ், சரத்து 356-ன் கீழ் வெளியிடப்பட்ட எந்தவொரு பிரகடனமும் குடியரசுத் தலைவரின் பிந்தைய பிரகடனம் மூலம் திரும்பப் பெறப்படலாம் அல்லது மாற்றப்படலாம். ஆரம்ப பிரகடனம் அல்லது நீட்டிப்பு போலல்லாமல், திரும்பப் பெறும் பிரகடனத்திற்கு பாராளுமன்ற ஒப்புதல் தேவையில்லை.",
        "Option A correctly states the constitutional rule under Article 356(2).", "விருப்பம் A சரத்து 356(2)-ன் கீழான அரசியலமைப்பு விதியைச் சரியாகக் கூறுகிறது.",
        "Option B is false; revocation does not require parliamentary resolutions.", "விருப்பம் B தவறு; திரும்பப் பெறுவதற்கு பாராளுமன்றத் தீர்மானம் தேவையில்லை.",
        "Option C is fictitious.", "விருப்பம் C கற்பனையானது.",
        "Option D is unconstitutional.", "விருப்பம் D அரசியலமைப்பிற்கு எதிரானது.",
        "Revocation Flexibility: The President can revoke President's Rule at any time unilaterally without going to Parliament.",
        "திரும்பப் பெறும் நெகிழ்வுத்தன்மை: பாராளுமன்றத்திற்குச் செல்லாமல் குடியரசுத் தலைவர் எந்த நேரத்திலும் குடியரசுத் தலைவர் ஆட்சியைத் தன்னிச்சையாகத் திரும்பப் பெறலாம்.",
        "This allows immediate restoration of popular government once political stability or election outcomes are achieved.",
        "அரசியல் ஸ்திரத்தன்மை அல்லது தேர்தல் முடிவுகள் வந்தவுடன் மக்களாட்சியை உடனடியாக மீட்டெடுக்க இது உதவுகிறது."
    ))

    # 022 - Key B
    qs.append(make_ep_q(
        PREFIX, 22, DIFF, "Constitutional Comparison", "Emergency Provisions - Article 358 vs 359 Retrospective Effect",
        "What is the constitutional position regarding executive acts committed without legislative authority during an emergency once the emergency ceases to operate?",
        "அவசரநிலை முடிவுக்கு வந்த பிறகு, அவசரநிலையின் போது சட்ட அங்கீகாரமின்றி நிர்வாகத்தால் செய்யப்பட்ட செயல்கள் குறித்த அரசியலமைப்பு நிலை என்ன?",
        "All executive acts committed during an emergency receive permanent immunity from any legal challenge forever", "அவசரநிலையின் போது செய்யப்பட்ட அனைத்து நிர்வாகச் செயல்களும் என்றென்றும் எந்தவொரு சட்ட சவாலிலிருந்தும் நிரந்தரப் பாதுகாப்புப் பெறுகின்றன",
        "No executive action taken without legislative authority can be protected, and once the emergency ceases, citizens can challenge unauthorized executive acts that violated fundamental rights", "சட்டப்பூர்வ அதிகாரமின்றி எடுக்கப்பட்ட எந்தவொரு நிர்வாக நடவடிக்கையும் பாதுகாக்கப்பட முடியாது, மேலும் அவசரநிலை முடிந்தவுடன், அடிப்படை உரிமைகளை மீறிய அங்கீகரிக்கப்படாத நிர்வாகச் செயல்களை குடிமக்கள் சவால் செய்யலாம்",
        "The President can issue a retrospective pardon to all civil servants under Article 72", "சரத்து 72-ன் கீழ் அனைத்து அரசு ஊழியர்களுக்கும் குடியரசுத் தலைவர் பின்னோக்கி பொதுமன்னிப்பு வழங்கலாம்",
        "Only the Supreme Court can grant indemnity to executive officers through Article 142", "சரத்து 142 மூலம் உச்ச நீதிமன்றம் மட்டுமே நிர்வாக அதிகாரிகளுக்கு இழப்பீட்டுப் பாதுகாப்பு வழங்க முடியும்",
        "B",
        "In Bennett Coleman (1973) and reaffirmed post-44th Amendment, the Supreme Court emphasized that Article 358 and Article 359 protect ONLY laws containing the emergency recital and executive action taken strictly UNDER such laws. Purely executive actions taken without legislative sanction do NOT enjoy emergency immunity, and citizens can sue the State for damages or remedies once the emergency ceases to operate.",
        "பென்னட் கோல்மன் (1973) வழக்கில் மற்றும் 44-வது திருத்தத்திற்குப் பின் மீண்டும் உறுதிப்படுத்தப்பட்டபடி, அவசரநிலை அறிவிப்பைக் கொண்டுள்ள சட்டங்கள் மற்றும் அத்தகைய சட்டங்களின் கீழ் கண்டிப்பாக எடுக்கப்பட்ட நிர்வாக நடவடிக்கைகள் மட்டுமே சரத்துகள் 358 மற்றும் 359-ன் கீழ் பாதுகாக்கப்படுகின்றன. சட்ட அங்கீகாரமின்றி எடுக்கப்பட்ட நிர்வாக நடவடிக்கைகள் அவசரநிலை பாதுகாப்பைப் பெற முடியாது; அவசரநிலை முடிந்தவுடன் இழப்பீடு அல்லது நிவாரணம் கோரி குடிமக்கள் அரசு மீது வழக்குத் தொடரலாம்.",
        "Option A is completely wrong; rule of law does not permit arbitrary administrative immunity.", "விருப்பம் A முற்றிலும் தவறு; சட்டத்தின் ஆட்சி தன்னிச்சையான நிர்வாகப் பாதுகாப்பை அனுமதிக்காது.",
        "Option B accurately articulates the limitation of emergency immunity to legally authorized actions.", "விருப்பம் B சட்டப்பூர்வமாக அங்கீகரிக்கப்பட்ட நடவடிக்கைகளுக்கு மட்டுமே அவசரநிலை பாதுகாப்பு உண்டு என்ற வரம்பை துல்லியமாக விளக்குகிறது.",
        "Option C misapplies Article 72 pardoning power.", "விருப்பம் C சரத்து 72-ன் மன்னிப்பு அதிகாரத்தை தவறாகப் பயன்படுத்துகிறது.",
        "Option D is incorrect; indemnity acts must be enacted by Parliament under Article 34 (martial law), not Article 142.", "விருப்பம் D தவறானது; இழப்பீட்டுச் சட்டங்கள் பாராளுமன்றத்தால் சரத்து 34-ன் கீழ் இயற்றப்பட வேண்டும்.",
        "Executive Accountability: Emergency shields ONLY valid laws and actions taken strictly under those laws. Pure executive overreach remains actionable post-emergency.",
        "நிர்வாகப் பொறுப்புடைமை: அவசரநிலை செல்லுபடியாகும் சட்டங்களையும் அவற்றின் கீழ் எடுக்கப்பட்ட நடவடிக்கைகளையும் மட்டுமே பாதுகாக்கிறது. சட்டத்திற்குப் புறம்பான நிர்வாக அத்துமீறல்கள் மீது அவசரநிலைக்குப் பின் வழக்குத் தொடரலாம்.",
        "This prevents officers from acting extra-legally under the assumption that emergency grants blanket personal immunity.",
        "அவசரநிலை தங்களுக்கு முழுப் பாதுகாப்பு அளிக்கிறது என்ற எண்ணத்தில் அதிகாரிகள் சட்டத்திற்குப் புறம்பாகச் செயல்படுவதை இது தடுக்கிறது."
    ))

    # 023 - Key C
    qs.append(make_ep_q(
        PREFIX, 23, DIFF, "Constitutional Comparison", "Article 356 - Governor's Report Disclosure",
        "In S.R. Bommai (1994), what did the Supreme Court rule regarding the Union Government's claim of privilege under Article 74(2) concerning the Governor's report and ministerial advice?",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், ஆளுநரின் அறிக்கை மற்றும் அமைச்சரவை ஆலோசனை தொடர்பாக சரத்து 74(2)-ன் கீழான சலுகைக் கோரிக்கை குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "Article 74(2) bars the court from examining ANY material whatsoever, including the Governor's report", "ஆளுநரின் அறிக்கை உட்பட எந்தவொரு ஆதாரத்தையும் நீதிமன்றம் ஆராய்வதை சரத்து 74(2) முற்றிலும் தடுக்கிறது",
        "The Union Cabinet must publish all intelligence reports in national newspapers prior to issuing Article 356", "சரத்து 356-ஐ வெளியிடுவதற்கு முன்பு மத்திய அமைச்சரவை அனைத்து உளவுத்துறை அறிக்கைகளையும் தேசிய செய்தித்தாள்களில் வெளியிட வேண்டும்",
        "While Article 74(2) bars enquiry into the advice tendered by Ministers to the President, it does NOT bar scrutiny of the material on the basis of which the advice was tendered, including the Governor's report", "அமைச்சர்கள் குடியரசுத் தலைவருக்கு வழங்கிய ஆலோசனையை விசாரிப்பதை சரத்து 74(2) தடுத்தாலும், ஆளுநரின் அறிக்கை உட்பட எந்த ஆதாரத்தின் அடிப்படையில் ஆலோசனை வழங்கப்பட்டதோ அந்த ஆதாரங்களை நீதிமன்றம் ஆய்வு செய்வதை அது தடுக்காது",
        "The Governor's report is automatically forwarded to the United Nations Human Rights Council for validation", "ஆளுநரின் அறிக்கை சரிபார்ப்பிற்காக ஐக்கிய நாடுகள் மனித உரிமைகள் பேரவைக்கு தானாகவே அனுப்பப்படுகிறது",
        "C",
        "In S.R. Bommai (1994), the Supreme Court held that Article 74(2) prohibits courts from inquiring into the actual advice tendered by Ministers to the President. However, Article 74(2) does NOT protect the background materials, reasons, or reports (such as the Governor's report) upon which that advice was based. The Government is bound to disclose the material to the court to demonstrate that relevant objective grounds existed.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், அமைச்சர்கள் குடியரசுத் தலைவருக்கு வழங்கிய உண்மையான ஆலோசனையை நீதிமன்றங்கள் விசாரிப்பதை சரத்து 74(2) தடுக்கிறது என்று உச்ச நீதிமன்றம் கூறியது. இருப்பினும், ஆளுநரின் அறிக்கை உட்பட அந்த ஆலோசனைக்கு அடிப்படையாக இருந்த பின்னணி ஆதாரங்கள் அல்லது காரணங்களை சரத்து 74(2) பாதுகாக்காது. பொருத்தமான புறநிலை ஆதாரங்கள் இருந்ததை நிரூபிக்க அந்த ஆவணங்களை நீதிமன்றத்தில் சமர்ப்பிக்க மத்திய அரசு கடமைப்பட்டுள்ளது.",
        "Option A is the Union's rejected argument.", "விருப்பம் A என்பது நிராகரிக்கப்பட்ட மத்திய அரசின் வாதமாகும்.",
        "Option B is absurd and breach of official secrets.", "விருப்பம் B தவறானது மற்றும் அரசு ரகசியங்களை மீறுவது.",
        "Option C accurately captures the distinction between 'advice' (confidential) and 'material underlying advice' (open to judicial review).", "விருப்பம் C 'ஆலோசனை' (ரகசியமானது) மற்றும் 'ஆலோசனைக்கு அடிப்படையான ஆதாரங்கள்' (நீதிமன்ற ஆய்வுக்கு உட்பட்டவை) ஆகியவற்றுக்கு இடையேயான வேறுபாட்டைத் துல்லியமாக விளக்குகிறது.",
        "Option D is fictitious.", "விருப்பம் D கற்பனையானது.",
        "Bommai Evidentiary Rule: The advice itself is confidential (Art 74(2)), but the MATERIAL on which it is based is fully open to judicial inspection.",
        "பொம்மை சாட்சிய விதி: ஆலோசனையே ரகசியமானது (சரத்து 74(2)), ஆனால் அதன் அடிப்படை ஆதாரங்கள் நீதிமன்ற ஆய்வுக்கு முழுமையாக திறக்கப்பட்டுள்ளன.",
        "If the Union refuses to disclose the material, the court can draw an adverse inference and strike down the proclamation.",
        "மத்திய அரசு ஆதாரங்களை வெளியிட மறுத்தால், நீதிமன்றம் பாதகமான அனுமானத்தை எடுத்துக்கொண்டு பிரகடனத்தை ரத்து செய்யலாம்."
    ))

    # 024 - Key D
    qs.append(make_ep_q(
        PREFIX, 24, DIFF, "Constitutional Landmark", "Article 356 and Misuse in Haryana (1967)",
        "The phenomenon of political defection ('Aaya Ram Gaya Ram') led to the dismissal of the Rao Birender Singh ministry in Haryana in November 1967 under Article 356, despite the ministry commanding a majority on the floor. On what ground did Governor B.N. Chakravarty justify this imposition?",
        "அரசியல் கட்சி தாவல் ('ஆயா ராம் கயா ராம்') காரணமாக, சட்டமன்றத்தில் பெரும்பான்மை இருந்தபோதிலும், நவம்பர் 1967-ல் ஹரியானாவில் ராவ் பிரேந்திர சிங் அமைச்சரவை சரத்து 356-ன் கீழ் பதவி நீக்கம் செய்யப்பட்டது. ஆளுநர் பி.என். சக்ரவர்த்தி எந்த அடிப்படையில் இதை நியாயப்படுத்தினார்?",
        "Failure to enforce Hindi as the official language", "இந்தியை ஆட்சி மொழியாக அமல்படுத்தத் தவறியமை",
        "Direct involvement of ministers in border clashes with Punjab", "பஞ்சாபுடனான எல்லை மோதல்களில் அமைச்சர்கள் நேரடியாக ஈடுபட்டமை",
        "Default on repayment of public debt to the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கிக்கு பொதுக் கடனை திருப்பிச் செலுத்துவதில் ஏற்பட்ட தவறுதல்",
        "Frequent floor-crossing and purchasing of MLAs had made a mockery of the democratic process, rendering stable governance impossible despite technical numerical majority", "சட்டமன்ற உறுப்பினர்களின் தொடர் கட்சி தாவல் மற்றும் குதிரை பேரம் ஜனநாயக நடைமுறையை கேலிக்கூத்தாக்கியதுடன், தொழில்முறை பெரும்பான்மை இருந்தபோதிலும் நிலையான நிர்வாகத்தை சாத்தியமற்றதாக்கியது",
        "D",
        "In November 1967, Haryana became the first state where Article 356 was invoked to tackle rampant defections. Governor B.N. Chakravarty reported that shifting loyalties by opportunistic MLAs (the origin of the phrase 'Aaya Ram, Gaya Ram') had made stable administration impossible and corrupted the democratic system, even though Chief Minister Rao Birender Singh technically enjoyed a legislative majority at that moment.",
        "நவம்பர் 1967-ல், தொடர் கட்சி தாவல்களைக் கட்டுப்படுத்த சரத்து 356 பயன்படுத்தப்பட்ட முதல் மாநிலமாக ஹரியானா உருவானது. முதலமைச்சர் ராவ் பிரேந்திர சிங் சட்டமன்றத்தில் தற்காலிக பெரும்பான்மையைக் கொண்டிருந்த போதிலும், சந்தர்ப்பவாத சட்டமன்ற உறுப்பினர்களின் தொடர் கட்சி தாவல்கள் ('ஆயா ராம், கயா ராம்' என்ற சொல்லின் தோற்றம்) நிலையான நிர்வாகத்தை சாத்தியமற்றதாக்கியதுடன் ஜனநாயக அமைப்பை சீரழித்துவிட்டதாக ஆளுநர் பி.என். சக்ரவர்த்தி அறிக்கை அளித்தார்.",
        "Option A is historically incorrect.", "விருப்பம் A வரலாற்று ரீதியாக தவறானது.",
        "Option B is false regarding border clashes.", "விருப்பம் B எல்லை மோதல்கள் சார்ந்து தவறானது.",
        "Option C is incorrect regarding debt default.", "விருப்பம் C கடன் தவறுதல் சார்ந்து தவறானது.",
        "Option D provides the accurate historical rationale documented in Indian parliamentary and constitutional records.", "விருப்பம் D இந்திய பாராளுமன்ற மற்றும் அரசியலமைப்பு ஆவணங்களில் உள்ள துல்லியமான வரலாற்று நியாயத்தை வழங்குகிறது.",
        "Historical Landmark: Haryana 1967 was the classic case where opportunistic defection ('Aaya Ram, Gaya Ram') triggered Article 356.",
        "வரலாற்று மைல்கல்: ஹரியானா 1967 என்பது சந்தர்ப்பவாத கட்சி தாவல் ('ஆயா ராம், கயா ராம்') சரத்து 356-ஐத் தூண்டிய உன்னதமான நிகழ்வாகும்.",
        "This historical abuse eventually led to the enactment of the Anti-Defection Law (52nd Amendment) in 1985.",
        "இந்த வரலாற்று முறைகேடு இறுதியில் 1985-ல் கட்சி தாவல் தடைச் சட்டம் (52-வது திருத்தம்) இயற்றப்படுவதற்கு வழிவகுத்தது."
    ))

    # 025 - Key A
    qs.append(make_ep_q(
        PREFIX, 25, DIFF, "Constitutional Comparison", "Article 356 - Sarkaria Commission on Pre-Warning",
        "What procedural safeguard did the Sarkaria Commission (1987) recommend that the Centre must mandatorily comply with before invoking Article 356, except in cases of extreme urgency?",
        "அவசர வழக்குகளைத் தவிர்த்து, சரத்து 356-ஐப் பயன்படுத்துவதற்கு முன்பு மத்திய அரசு எந்த நடைமுறைப் பாதுகாப்பை கட்டாயமாகப் பின்பற்ற வேண்டும் என்று சர்க்காரியா ஆணையம் (1987) பரிந்துரைத்தது?",
        "A formal warning should be issued to the errant State giving it a specific opportunity to correct itself and explain its stand", "தவறிழைக்கும் மாநிலத்திற்கு தன்னைத் திருத்திக் கொள்ளவும் தனது நிலைப்பாட்டை விளக்கவும் ஒரு குறிப்பிட்ட வாய்ப்பை வழங்கி முறையான எச்சரிக்கை விடுக்கப்பட வேண்டும்",
        "The President must consult the International Court of Justice", "குடியரசுத் தலைவர் சர்வதேச நீதிமன்றத்துடன் கலந்தாலோசிக்க வேண்டும்",
        "The Governor must be replaced by a retired Supreme Court judge", "ஆளுநருக்குப் பதிலாக ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதி நியமிக்கப்பட வேண்டும்",
        "The Union Cabinet must seek approval from a two-thirds majority of the Rajya Sabha in advance", "மத்திய அமைச்சரவை மாநிலங்களவையின் மூன்றில் இரண்டு பங்கு பெரும்பான்மையிடமிருந்து முன்கூட்டியே ஒப்புதல் பெற வேண்டும்",
        "A",
        "The Sarkaria Commission (1987) emphasized that Article 356 should not be used as an instrument of sudden political assassination. It recommended that a formal warning should be issued to the errant State, in specific terms, giving it an opportunity to explain and rectify the situation, except in cases of sudden, catastrophic emergency where prior warning would cause irreparable harm.",
        "சர்க்காரியா ஆணையம் (1987), சரத்து 356-ஐ திடீர் அரசியல் படுகொலைக்கான கருவியாகப் பயன்படுத்தக் கூடாது என்று வலியுறுத்தியது. முன் எச்சரிக்கை ஈடுசெய்ய முடியாத பாதிப்பை ஏற்படுத்தும் தீவிர அவசர நிலைகளைத் தவிர, தவறிழைக்கும் மாநிலத்திற்கு தனது நிலைப்பாட்டை விளக்கவும் நிலைமையைச் சரிசெய்யவும் ஒரு குறிப்பிட்ட வாய்ப்பை வழங்கி முறையான எச்சரிக்கை விடுக்கப்பட வேண்டும் என்று அது பரிந்துரைத்தது.",
        "Option A is the celebrated 'prior warning' recommendation of the Sarkaria Commission, endorsed in the Bommai judgment.", "விருப்பம் A என்பது பொம்மை தீர்ப்பில் ஏற்றுக்கொள்ளப்பட்ட சர்க்காரியா ஆணையத்தின் புகழ்பெற்ற 'முன் எச்சரிக்கை' பரிந்துரையாகும்.",
        "Option B is a fabricated procedural requirement.", "விருப்பம் B கற்பனையான ஒரு நடைமுறைத் தேவையாகும்.",
        "Option C is non-existent in the report.", "விருப்பம் C அறிக்கையில் இல்லாத ஒன்றாகும்.",
        "Option D is false.", "விருப்பம் D தவறானது.",
        "Sarkaria Safeguard: Prior specific warning to the State + Opportunity to rectify = Essential prerequisite before invoking Article 356.",
        "சர்க்காரியா பாதுகாப்பு: மாநிலத்திற்கு முன் குறிப்பிட்ட எச்சரிக்கை + சரிசெய்ய வாய்ப்பு = சரத்து 356-ஐப் பயன்படுத்துவதற்கு முந்தைய அத்தியாவசியத் தேவை.",
        "Failure to issue a warning can be cited before the courts as evidence of mala fides and arbitrariness.",
        "எச்சரிக்கை விடுக்கத் தவறியதை உள்நோக்கம் மற்றும் தன்னிச்சையான செயல்பாட்டின் சான்றாக நீதிமன்றங்களில் முன்வைக்க முடியும்."
    ))

    return qs

def get_hard_questions_part2():
    qs = []

    # 026 - Key A
    qs.append(make_ep_q(
        PREFIX, 26, DIFF, "Constitutional Comparison", "Emergency Provisions - Article 352 vs 356 State Legislatures",
        "During which of the following emergencies does the State Legislative Assembly lose its power to pass legislation on State subjects entirely to Parliament?",
        "பின்வரும் எந்த அவசரநிலையின் போது மாநில சட்டமன்றம் மாநிலப் பட்டியல் விவகாரங்களில் சட்டம் இயற்றும் தனது அதிகாரத்தை பாராளுமன்றத்திடம் முற்றிலும் இழக்கிறது?",
        "President's Rule under Article 356", "சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சி",
        "National Emergency under Article 352", "சரத்து 352-ன் கீழான தேசிய அவசரநிலை",
        "Financial Emergency under Article 360", "சரத்து 360-ன் கீழான நிதி அவசரநிலை",
        "Both National Emergency and Financial Emergency", "தேசிய அவசரநிலை மற்றும் நிதி அவசரநிலை ஆகிய இரண்டும்",
        "A",
        "Under President's Rule (Article 356), the legislative powers of the State are declared to be exercisable by or under the authority of Parliament (Article 356(1)(b)), and the Assembly is either dissolved or suspended, losing its legislative power completely. In contrast, under National Emergency (Article 352), the State Legislature continues to function and pass laws concurrently. Under Financial Emergency (Article 360), state legislative power is not transferred to Parliament at all.",
        "குடியரசுத் தலைவர் ஆட்சியின் கீழ் (சரத்து 356), மாநிலத்தின் சட்டமியற்றும் அதிகாரங்கள் பாராளுமன்றத்தால் பயன்படுத்தப்படும் என அறிவிக்கப்பட்டு (சரத்து 356(1)(b)), சட்டமன்றம் கலைக்கப்படுகிறது அல்லது முடக்கப்படுகிறது; இதனால் அது தனது சட்ட அதிகாரத்தை முற்றிலும் இழக்கிறது. மாறாக, தேசிய அவசரநிலையின் போது (சரத்து 352), மாநில சட்டமன்றம் தொடர்ந்து செயல்பட்டு இணையாக சட்டங்களை இயற்றுகிறது. நிதி அவசரநிலையின் போது (சரத்து 360), மாநில சட்ட அதிகாரம் பாராளுமன்றத்திற்கு மாற்றப்படுவதே இல்லை.",
        "Option A is correct; President's Rule alone completely divests the State Legislature of its law-making powers.", "விருப்பம் A சரியானது; குடியரசுத் தலைவர் ஆட்சி மட்டுமே மாநில சட்டமன்றத்தின் சட்டம் இயற்றும் அதிகாரங்களை முற்றிலும் பறிக்கிறது.",
        "Option B is incorrect because State Legislature retains concurrent legislative capacity during National Emergency.", "விருப்பம் B தவறானது ஏனெனில் தேசிய அவசரநிலையின் போது மாநில சட்டமன்றம் தனது இணை சட்ட அதிகாரத்தைத் தக்கவைத்துக் கொள்கிறது.",
        "Option C is incorrect because state legislatures function normally during Financial Emergency.", "விருப்பம் C தவறானது ஏனெனில் நிதி அவசரநிலையின் போது மாநில சட்டமன்றங்கள் வழக்கம் போல் இயங்குகின்றன.",
        "Option D is false.", "விருப்பம் D தவறானது.",
        "Legislative Transfer Trap: Parliament gains SOLE/DIRECT legislative takeover ONLY during President's Rule (Art 356). In National Emergency (Art 352), it is CONCURRENT.",
        "சட்ட அதிகார மாற்றப் பொறி: பாராளுமன்றம் நேரடி சட்டப் பறிப்பை குடியரசுத் தலைவர் ஆட்சியில் (சரத்து 356) மட்டுமே பெறுகிறது. தேசிய அவசரநிலையில் (சரத்து 352) அது இணை அதிகாரமாகும்.",
        "This distinction is vital for understanding federal autonomy preservation during different national crises.",
        "வெவ்வேறு தேசிய நெருக்கடிகளின் போது கூட்டாட்சி தன்னாட்சி பாதுகாக்கப்படுவதைப் புரிந்துகொள்ள இந்த வேறுபாடு மிக முக்கியமானது."
    ))

    # 027 - Key B
    qs.append(make_ep_q(
        PREFIX, 27, DIFF, "Constitutional Comparison", "National Emergency - Fundamental Rights Comparison",
        "Suppose a National Emergency is declared on the ground of 'armed rebellion' in 2026. Can the President issue an order under Article 359 suspending the right of citizens to move the Supreme Court for enforcement of Article 19 freedoms?",
        "2026-ஆம் ஆண்டில் 'ஆயுதமேந்திய கிளர்ச்சி' என்ற காரணத்தின் அடிப்படையில் தேசிய அவசரநிலை அறிவிக்கப்படுகிறது என வைத்துக் கொள்வோம். சரத்து 19 சுதந்திரங்களை அமல்படுத்துவதற்காக குடிமக்கள் உச்ச நீதிமன்றத்தை அணுகும் உரிமையை இடைநிறுத்தி சரத்து 359-ன் கீழ் குடியரசுத் தலைவர் ஆணை பிறப்பிக்க முடியுமா?",
        "No, Article 19 can never be touched during armed rebellion under any Article", "முடியாது, ஆயுதமேந்திய கிளர்ச்சியின் போது எந்த சரத்தின் கீழும் சரத்து 19-ஐ தொடவே முடியாது",
        "Yes, while Article 19 is not automatically suspended under Article 358 during armed rebellion, its enforcement remedy CAN be suspended under Article 359 by a specific Presidential Order", "ஆம், ஆயுதமேந்திய கிளர்ச்சியின் போது சரத்து 358-ன் கீழ் சரத்து 19 தானாக இடைநிறுத்தப்படாவிட்டாலும், குறிப்பிட்ட குடியரசுத் தலைவர் ஆணை மூலம் சரத்து 359-ன் கீழ் அதன் அமலாக்கத் தீர்வை இடைநிறுத்த முடியும்",
        "No, only Articles 14 and 21 can be suspended under Article 359", "முடியாது, சரத்து 359-ன் கீழ் சரத்துகள் 14 மற்றும் 21 மட்டுமே இடைநிறுத்தப்பட முடியும்",
        "Yes, but only if the Chief Justice of India countersigns the presidential order", "ஆம், ஆனால் இந்திய தலைமை நீதிபதி குடியரசுத் தலைவர் ஆணையில் எதிர் கையொப்பமிட்டால் மட்டுமே",
        "B",
        "A very common advanced TNPSC trap: The 44th Amendment Act 1978 restricted Article 358 so that Article 19 is NOT automatically suspended during armed rebellion. However, under Article 359, the President is empowered to suspend the right to move any court for the enforcement of ANY Fundamental Right EXCEPT Articles 20 and 21. Therefore, the enforcement of Article 19 CAN still be suspended under Article 359 by a specific Presidential Order even during armed rebellion!",
        "ஒரு மிக முக்கியமான மேம்பட்ட TNPSC பொறி: 1978-ன் 44-வது திருத்தச் சட்டம் சரத்து 358-ஐக் கட்டுப்படுத்தியதால், ஆயுதமேந்திய கிளர்ச்சியின் போது சரத்து 19 தானாகவே இடைநிறுத்தப்படாது. இருப்பினும், சரத்து 359-ன் கீழ், சரத்துகள் 20 மற்றும் 21 தவிர மற்ற எந்தவொரு அடிப்படை உரிமையையும் அமல்படுத்துவதற்காக நீதிமன்றத்தை அணுகும் உரிமையை இடைநிறுத்த குடியரசுத் தலைவருக்கு அதிகாரம் உண்டு. எனவே, ஆயுதமேந்திய கிளர்ச்சியின் போது கூட குறிப்பிட்ட குடியரசுத் தலைவர் ஆணை மூலம் சரத்து 19-ன் அமலாக்கத்தை சரத்து 359-ன் கீழ் இடைநிறுத்த முடியும்!",
        "Option A is the common misconception that confuses Article 358 with Article 359.", "விருப்பம் A என்பது சரத்து 358-ஐ சரத்து 359 உடன் குழப்பும் பொதுவான தவறான கருத்தாகும்.",
        "Option B is the precise, advanced constitutional reality post-44th CAA.", "விருப்பம் B 44-வது திருத்தத்திற்குப் பிந்தைய துல்லியமான, மேம்பட்ட அரசியலமைப்பு உண்மையாகும்.",
        "Option C is factually false; only Arts 20 and 21 are protected from Art 359.", "விருப்பம் C தவறானது; சரத்துகள் 20 மற்றும் 21 மட்டுமே சரத்து 359-லிருந்து விலக்கு பெற்றவை.",
        "Option D is fictitious.", "விருப்பம் D கற்பனையானது.",
        "Super Trap Clarified: Art 358 automatic suspension of Art 19 = ONLY War/External Aggression. Art 359 presidential order suspension of Art 19 remedy = CAN operate during Armed Rebellion as well!",
        "முக்கிய பொறி விளக்கம்: சரத்து 358-ன் தானியங்கி சரத்து 19 இடைநிறுத்தம் = போர்/வெளிநாட்டு ஆக்கிரமிப்பு மட்டுமே. சரத்து 359-ன் கீழ் சரத்து 19 அமலாக்க இடைநிறுத்தம் = ஆயுதமேந்திய கிளர்ச்சியின் போதும் செயல்படலாம்!",
        "The only rights that can NEVER be suspended under either Article 358 or Article 359 are Articles 20 and 21.",
        "சரத்து 358 அல்லது 359 ஆகிய இரண்டின் கீழும் ஒருபோதும் இடைநிறுத்தப்பட முடியாத ஒரே உரிமைகள் சரத்துகள் 20 மற்றும் 21 மட்டுமே."
    ))

    # 028 - Key C
    qs.append(make_ep_q(
        PREFIX, 28, DIFF, "Constitutional Comparison", "Article 356 - Governor's Discretionary Report",
        "Under Article 356(1), can the Governor of a State send a report recommending President's Rule WITHOUT consulting or seeking the advice of the State Council of Ministers?",
        "சரத்து 356(1)-ன் கீழ், மாநில அமைச்சரவையைக் கலந்தாலோசிக்காமலோ அல்லது அதன் ஆலோசனையைப் பெறாமலோ குடியரசுத் தலைவர் ஆட்சியைப் பரிந்துரைத்து மாநில ஆளுநர் அறிக்கை அனுப்ப முடியுமா?",
        "No, under Article 163(1), the Governor must compulsorily act on the aid and advice of the Council of Ministers in all matters without exception", "முடியாது, சரத்து 163(1)-ன் கீழ், விதிவிலக்கின்றி அனைத்து விவகாரங்களிலும் அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின் படியே ஆளுநர் செயல்பட வேண்டும்",
        "Only if the Speaker of the State Legislative Assembly gives prior written permission", "மாநில சட்டமன்ற சபாநாயகர் முன் எழுத்துப்பூர்வ அனுமதி அளித்தால் மட்டுமே",
        "Yes, reporting on the breakdown of constitutional machinery under Article 356 is a matter of the Governor's personal constitutional discretion, independent of the Council of Ministers", "ஆம், சரத்து 356-ன் கீழ் அரசியலமைப்பு இயந்திர முறிவு குறித்து அறிக்கை அளிப்பது அமைச்சரவையிலிருந்து சுதந்திரமான, ஆளுநரின் தனிப்பட்ட அரசியலமைப்பு தன்னுரிமை விவகாரமாகும்",
        "Only if the Chief Secretary of the State countersigns the report", "மாநில தலைமைச் செயலாளர் அந்த அறிக்கையில் எதிர் கையொப்பமிட்டால் மட்டுமே",
        "C",
        "Under Article 163(1) and (2), the Governor acts on aid and advice EXCEPT where the Constitution requires him to act in his discretion. Recommending President's Rule under Article 356 is inherently a report that the Council of Ministers itself has failed to function constitutionally; thus, seeking the advice of the very ministry that is failing is logically impossible. The Governor acts in his independent constitutional discretion.",
        "சரத்து 163(1) மற்றும் (2)-ன் படி, அரசியலமைப்பு தன்னுரிமையுடன் செயல்படக் கோரும் விவகாரங்களைத் தவிர பிறவற்றில் ஆளுநர் அமைச்சரவை ஆலோசனையின் படி செயல்படுகிறார். சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சிக்குப் பரிந்துரைப்பது என்பது அமைச்சரவையே அரசியலமைப்பு ரீதியாக இயங்கத் தவறிவிட்டது என்ற அறிக்கையாகும்; எனவே தவறான அமைச்சரவையிடமே ஆலோசனை கேட்பது தர்க்கரீதியாக சாத்தியமற்றது. ஆளுநர் தனது சுதந்திரமான அரசியலமைப்பு தன்னுரிமையில் செயல்படுகிறார்.",
        "Option A overlooks the constitutional exception of discretionary powers in Article 163.", "விருப்பம் A சரத்து 163-ல் உள்ள தன்னுரிமை அதிகாரங்களின் அரசியலமைப்பு விதிவிலக்கைக் கவனிக்கத் தவறுகிறது.",
        "Option B is false.", "விருப்பம் B தவறானது.",
        "Option C correctly explains the discretionary independence of the Governor under Article 356.", "விருப்பம் C சரத்து 356-ன் கீழ் ஆளுநரின் தன்னுரிமை சுதந்திரத்தைச் சரியாக விளக்குகிறது.",
        "Option D is legally baseless.", "விருப்பம் D சட்ட அடிப்படையற்றது.",
        "Gubernatorial Discretion: Preparing the Article 356 report is one of the clearest instances of the Governor's independent constitutional discretion.",
        "ஆளுநரின் தன்னுரிமை: சரத்து 356 அறிக்கையைத் தயாரிப்பது என்பது ஆளுநரின் சுதந்திரமான அரசியலமைப்பு தன்னுரிமைக்கான தெளிவான உதாரணங்களில் ஒன்றாகும்.",
        "However, this discretion must be exercised objectively and bona fide, supported by verifiable material, as held in Bommai.",
        "இருப்பினும், இந்த தன்னுரிமை பொம்மை வழக்கின்படி புறநிலையாகவும், சரிபார்க்கக்கூடிய ஆதாரங்களின் அடிப்படையிலும் பயன்படுத்தப்பட வேண்டும்."
    ))

    # 029 - Key D
    qs.append(make_ep_q(
        PREFIX, 29, DIFF, "Constitutional Comparison", "Article 360 - Federal Balance",
        "Why is Financial Emergency under Article 360 regarded as having the most drastic impact on the financial autonomy of the States in the Indian Constitution?",
        "இந்திய அரசியலமைப்பில் நிதி அவசரநிலை (சரத்து 360) மாநிலங்களின் நிதி தன்னாட்சியின் மீது மிகவும் கடுமையான தாக்கத்தை ஏற்படுத்துவதாக ஏன் கருதப்படுகிறது?",
        "Because it automatically cancels all state public debt owed to commercial banks", "ஏனெனில் அது வணிக வங்கிகளுக்கு மாநிலங்கள் செலுத்த வேண்டிய அனைத்து பொதுக் கடன்களையும் தானாகவே ரத்து செய்கிறது",
        "Because it converts the currency of the State into Union treasury vouchers", "ஏனெனில் அது மாநிலத்தின் நாணயத்தை மத்திய கருவூல வவுச்சர்களாக மாற்றுகிறது",
        "Because it abolishes all State Finance Commissions permanently", "ஏனெனில் அது அனைத்து மாநில நிதி ஆணையங்களையும் நிரந்தரமாக ரத்து செய்கிறது",
        "Because the Centre can dictate state budgetary allocations, reduce state employees' and judges' salaries, and require all State Money Bills to be reserved for the President", "ஏனெனில் மத்திய அரசு மாநில வரவுசெலவு ஒதுக்கீடுகளைக் கட்டளையிடலாம், மாநில ஊழியர்கள் மற்றும் நீதிபதிகளின் ஊதியத்தைக் குறைக்கலாம், மேலும் அனைத்து மாநிலப் பண மசோதாக்களையும் குடியரசுத் தலைவரின் பரிசீலனைக்கு நிறுத்தி வைக்கக் கோரலாம்",
        "D",
        "During Financial Emergency under Article 360, the federal division of financial powers is virtually obliterated: (1) The Centre can issue binding directions to states to observe canons of financial propriety; (2) The President can order reduction of salaries of all state civil servants and High Court judges; and (3) The President can require that ALL Money Bills and financial bills passed by the State Legislature be reserved for his assent under Article 360(4)(a)(ii).",
        "சரத்து 360-ன் கீழான நிதி அவசரநிலையின் போது, கூட்டாட்சி நிதிப் பகிர்வு முற்றிலும் தகர்க்கப்படுகிறது: (1) நிதி ஒழுங்கு நெறிமுறைகளைப் பின்பற்றுமாறு மாநிலங்களுக்கு மத்திய அரசு கட்டாய வழிகாட்டலாம்; (2) மாநில அரசு ஊழியர்கள் மற்றும் உயர் நீதிமன்ற நீதிபதிகளின் ஊதியத்தைக் குறைக்க குடியரசுத் தலைவர் உத்தரவிடலாம்; (3) மாநில சட்டமன்றத்தால் நிறைவேற்றப்படும் அனைத்து பண மசோதாக்களையும் தனது ஒப்புதலுக்கு நிறுத்தி வைக்கக் குடியரசுத் தலைவர் கோரலாம்.",
        "Option A is an incorrect and fictitious provision.", "விருப்பம் A தவறான மற்றும் கற்பனையான விதியாகும்.",
        "Option B is false regarding currency conversion.", "விருப்பம் B நாணய மாற்றம் சார்ந்து தவறானது.",
        "Option C is false; Finance Commissions are not abolished.", "விருப்பம் C தவறு; நிதி ஆணையங்கள் ரத்து செய்யப்படுவதில்லை.",
        "Option D comprehensively details the twin statutory levers of central financial hegemony under Article 360.", "விருப்பம் D சரத்து 360-ன் கீழான மத்திய அரசின் நிதி ஆதிக்கத்தின் முக்கிய வழிமுறைகளை விரிவாக விளக்குகிறது.",
        "Fiscal Unitary Switch: Financial Emergency converts the financial federalism of India into a completely unitary system without formal constitutional amendment.",
        "நிதி ஒற்றையாட்சி மாற்றம்: நிதி அவசரநிலை என்பது முறையான அரசியலமைப்பு திருத்தமின்றி இந்தியாவின் நிதி கூட்டாட்சியை முற்றிலும் ஒற்றையாட்சி அமைப்பாக மாற்றுகிறது.",
        "Fortunately, prudent macroeconomic stewardship has ensured Article 360 has never been invoked in India's history.",
        "அதிர்ஷ்டவசமாக, விவேகமான பொருளாதார நிர்வாகம் காரணமாக இந்தியாவின் வரலாற்றில் சரத்து 360 ஒருமுறை கூட பயன்படுத்தப்படவில்லை."
    ))

    # 030 - Key A
    qs.append(make_ep_q(
        PREFIX, 30, DIFF, "Constitutional Comparison", "National Emergency - Parliamentary Approval Timeline",
        "Suppose a proclamation of National Emergency is issued on 1 January 2026. The Lok Sabha was already dissolved on 20 December 2025. Rajya Sabha approves the proclamation on 20 January 2026. The new Lok Sabha holds its first sitting on 15 March 2026. What is the LAST DATE by which the new Lok Sabha must approve the proclamation for it to survive?",
        "1 ஜனவரி 2026 அன்று தேசிய அவசரநிலைப் பிரகடனம் வெளியிடப்படுகிறது என வைத்துக் கொள்வோம். மக்களவை ஏற்கனவே 20 டிசம்பர் 2025 அன்று கலைக்கப்பட்டுவிட்டது. மாநிலங்களவை 20 ஜனவரி 2026 அன்று பிரகடனத்திற்கு ஒப்புதல் அளிக்கிறது. புதிய மக்களவை தனது முதல் அமர்வை 15 மார்ச் 2026 அன்று நடத்துகிறது. அந்தப் பிரகடனம் நீடிக்க புதிய மக்களவை ஒப்புதல் அளிக்க வேண்டிய கடைசி தேதி எது?",
        "14 April 2026 (30 days from 15 March 2026)", "14 ஏப்ரல் 2026 (15 மார்ச் 2026-லிருந்து 30 நாட்கள்)",
        "15 May 2026 (60 days from 15 March 2026)", "15 மே 2026 (15 மார்ச் 2026-லிருந்து 60 நாட்கள்)",
        "31 January 2026 (1 month from date of proclamation)", "31 ஜனவரி 2026 (பிரகடனம் செய்யப்பட்ட நாளிலிருந்து 1 மாதம்)",
        "15 September 2026 (6 months from first sitting)", "15 செப்டம்பர் 2026 (முதல் அமர்விலிருந்து 6 மாதங்கள்)",
        "A",
        "Under Article 352(4), if the Lok Sabha is dissolved at the time of issuing the proclamation or dissolution occurs during the one-month period without approval, and Rajya Sabha has approved it within one month, the proclamation survives until the expiration of THIRTY DAYS from the date on which the Lok Sabha first sits after its reconstitution. Since the first sitting is 15 March 2026, 30 days ends on 14 April 2026 (or within 30 days).",
        "சரத்து 352(4)-ன் கீழ், பிரகடனம் வெளியிடப்படும் போது மக்களவை கலைக்கப்பட்டிருந்தாலோ அல்லது ஒரு மாதத்திற்குள் ஒப்புதல் அளிக்காமல் கலைக்கப்பட்டாலோ, மாநிலங்களவை ஒரு மாதத்திற்குள் ஒப்புதல் அளித்திருந்தால், புதிய மக்களவை கூடிய முதல் தேதியிலிருந்து முப்பது நாட்கள் வரை அந்தப் பிரகடனம் நீடிக்கும். முதல் அமர்வு 15 மார்ச் 2026 என்பதால், 30 நாட்கள் என்பது 14 ஏப்ரல் 2026 அன்று முடிகிறது.",
        "Option A is the exact date calculation based on the 30-day constitutional rule under Article 352(4).", "விருப்பம் A என்பது சரத்து 352(4)-ன் கீழான 30 நாள் அரசியலமைப்பு விதியின் அடிப்படையிலான துல்லியமான தேதி கணக்கீடாகும்.",
        "Option B applies the 60-day window, which is incorrect for Lok Sabha's first sitting rule.", "விருப்பம் B 60 நாள் காலக்கெடுவைப் பயன்படுத்துகிறது, இது தவறு.",
        "Option C applies the general 1-month rule ignoring the Lok Sabha dissolution exception.", "விருப்பம் C மக்களவை கலைப்பு விதிவிலக்கைப் புறக்கணித்து பொதுவான 1 மாத விதியைப் பயன்படுத்துகிறது.",
        "Option D confuses the 6-month validity period with the approval deadline.", "விருப்பம் D 6 மாத கால செல்லுபடியாகும் காலத்தை ஒப்புதல் காலக்கெடுவுடன் குழப்புகிறது.",
        "Application Formula: First sitting date of new Lok Sabha + 30 days = Final survival deadline for National Emergency.",
        "பயன்பாட்டு சூத்திரம்: புதிய மக்களவையின் முதல் அமர்வு தேதி + 30 நாட்கள் = தேசிய அவசரநிலை நீடிப்பதற்கான இறுதி காலக்கெடு.",
        "If the reconstituted Lok Sabha fails to pass the resolution within these 30 days, the emergency immediately lapses on the 30th day.",
        "புதிய மக்களவை இந்த 30 நாட்களுக்குள் தீர்மானத்தை நிறைவேற்றத் தவறினால், அவசரநிலை 30-வது நாளில் உடனடியாக காலாவதியாகிவிடும்."
    ))

    # 031 - Key B
    qs.append(make_ep_q(
        PREFIX, 31, DIFF, "Constitutional Comparison", "Article 356 - Dissolution of Assembly post-Bommai",
        "In S.R. Bommai (1994), what did the Supreme Court hold regarding the power of the President to dissolve the State Legislative Assembly before both Houses of Parliament approve the proclamation?",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், பாராளுமன்றத்தின் இரு அவைகளும் பிரகடனத்திற்கு ஒப்புதல் அளிப்பதற்கு முன்பாக, மாநில சட்டமன்றத்தைக் கலைக்க குடியரசுத் தலைவருக்கு உள்ள அதிகாரம் குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "The President has unfettered constitutional authority to dissolve the Assembly immediately upon issuing the proclamation", "பிரகடனம் வெளியிட்ட உடனேயே சட்டமன்றத்தைக் கலைக்க குடியரசுத் தலைவருக்கு வரம்பற்ற அரசியலமைப்பு அதிகாரம் உண்டு",
        "The President cannot dissolve the Assembly until both Houses of Parliament approve the proclamation; before approval, the Assembly can only be kept in suspended animation", "பாராளுமன்றத்தின் இரு அவைகளும் பிரகடனத்திற்கு ஒப்புதல் அளிக்கும் வரை குடியரசுத் தலைவர் சட்டமன்றத்தைக் கலைக்க முடியாது; ஒப்புதலுக்கு முன் சட்டமன்றத்தை தற்காலிகமாக மட்டுமே நிறுத்தி வைக்க முடியும்",
        "The President can dissolve the Assembly, but only if the Governor signs an affidavit of consent", "ஆளுநர் ஒப்புதல் பிரமாணப் பத்திரத்தில் கையெழுத்திட்டால் மட்டுமே குடியரசுத் தலைவர் சட்டமன்றத்தைக் கலைக்க முடியும்",
        "The Assembly is dissolved automatically by operation of law under Article 356(1) without any presidential order", "சரத்து 356(1)-ன் கீழ் எந்தவொரு குடியரசுத் தலைவர் ஆணையும் இன்றியே சட்டத்தின்படி சட்டமன்றம் தானாகவே கலைக்கப்படுகிறது",
        "B",
        "In S.R. Bommai (1994), the 9-judge Constitution Bench laid down that the power to dissolve the Legislative Assembly under Article 356(1) cannot be exercised until both Houses of Parliament approve the proclamation under Article 356(3). Prior to parliamentary approval, the President can only suspend the Assembly. This ensures that if Parliament rejects the proclamation, the Assembly can be seamlessly revived.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு, பாராளுமன்றத்தின் இரு அவைகளும் சரத்து 356(3)-ன் கீழ் ஒப்புதல் அளிக்கும் வரை சரத்து 356(1)-ன் கீழ் சட்டமன்றத்தைக் கலைக்கும் அதிகாரத்தைப் பயன்படுத்த முடியாது என்று தீர்ப்பளித்தது. பாராளுமன்ற ஒப்புதலுக்கு முன், குடியரசுத் தலைவர் சட்டமன்றத்தை தற்காலிகமாக மட்டுமே நிறுத்தி வைக்க முடியும். பாராளுமன்றம் பிரகடனத்தை நிராகரித்தால் சட்டமன்றத்தை மீண்டும் எளிதாக உயிர்ப்பிக்க இது வழிசெய்கிறது.",
        "Option A was the pre-Bommai abusive executive practice struck down by the Supreme Court.", "விருப்பம் A என்பது உச்ச நீதிமன்றத்தால் தடை செய்யப்பட்ட பொம்மை வழக்கிற்கு முந்தைய தவறான நிர்வாக நடைமுறையாகும்.",
        "Option B is the precise landmark principle formulated by the Supreme Court in Bommai.", "விருப்பம் B பொம்மை வழக்கில் உச்ச நீதிமன்றத்தால் வகுக்கப்பட்ட துல்லியமான கொள்கையாகும்.",
        "Option C has no constitutional standing.", "விருப்பம் C-க்கு அரசியலமைப்பு அந்தஸ்து இல்லை.",
        "Option D is legally false; dissolution is an executive act, not an automatic statutory consequence.", "விருப்பம் D தவறு; கலைப்பு என்பது ஒரு நிர்வாக நடவடிக்கை, தானியங்கி விளைவு அல்ல.",
        "Bommai Assembly Protection Rule: No dissolution before parliamentary approval! Suspended animation only.",
        "பொம்மை சட்டமன்றப் பாதுகாப்பு விதி: பாராளுமன்ற ஒப்புதலுக்கு முன் கலைப்பு கூடாது! தற்காலிக இடைநிறுத்தம் மட்டுமே.",
        "This prevents the Union from presenting Parliament with a fait accompli by dissolving the house beforehand.",
        "சட்டமன்றத்தை முன்கூட்டியே கலைத்துவிட்டு பாராளுமன்றத்திற்கு ஒரு தவிர்க்க முடியாத சூழலை மத்திய அரசு ஏற்படுத்துவதை இது தடுக்கிறது."
    ))

    # 032 - Key C
    qs.append(make_ep_q(
        PREFIX, 32, DIFF, "Constitutional Comparison", "National Emergency - High Courts Writ Jurisdiction",
        "Can a High Court entertain a writ petition challenging an executive action during a National Emergency if the action violates a fundamental right OTHER THAN Articles 20 and 21, and the President has issued an order under Article 359 suspending that right?",
        "சரத்துகள் 20 மற்றும் 21 தவிர்த்த பிற அடிப்படை உரிமையை மீறியதாகக் கூறி, அந்த உரிமையை இடைநிறுத்தி சரத்து 359-ன் கீழ் குடியரசுத் தலைவர் ஆணை பிறப்பித்துள்ள நிலையில், தேசிய அவசரநிலையின் போது நிர்வாக நடவடிக்கையை எதிர்த்து உயர் நீதிமன்றம் நீதிப்பேராணை மனுவை விசாரிக்க முடியுமா?",
        "Yes, High Courts can always ignore Article 359 orders because High Court powers under Article 226 are wider than Supreme Court powers under Article 32", "ஆம், சரத்து 32-ஐ விட சரத்து 226-ன் கீழான உயர் நீதிமன்ற அதிகாரங்கள் பரந்தவை என்பதால் உயர் நீதிமன்றங்கள் எப்போதும் சரத்து 359 ஆணைகளைப் புறக்கணிக்கலாம்",
        "Yes, provided the petitioner deposits a security bond of one lakh rupees in the High Court registry", "ஆம், மனுதாரர் உயர் நீதிமன்ற பதிவேட்டில் ஒரு லட்சம் ரூபாய் பிணைத் தொகையை டெபாசிட் செய்தால் மட்டுமே",
        "No, because the Article 359 Presidential Order suspends the right to move 'any court' (including High Courts under Article 226) for the enforcement of the specified fundamental right", "முடியாது, ஏனெனில் சரத்து 359 குடியரசுத் தலைவர் ஆணை குறிப்பிட்ட அடிப்படை உரிமையை அமல்படுத்துவதற்காக 'எந்தவொரு நீதிமன்றத்தையும்' (சரத்து 226-ன் கீழ் உயர் நீதிமன்றங்கள் உட்பட) அணுகும் உரிமையை இடைநிறுத்துகிறது",
        "Yes, but only if the action was committed by a municipal local body, not the Union government", "ஆம், ஆனால் அந்த நடவடிக்கை மத்திய அரசால் அல்லாமல் நகராட்சி உள்ளாட்சி அமைப்பால் செய்யப்பட்டிருந்தால் மட்டுமே",
        "C",
        "Under Article 359(1), the President may declare that the right to move 'any court' for the enforcement of specified fundamental rights (except Articles 20 and 21) remains suspended. The phrase 'any court' embraces both the Supreme Court under Article 32 and the High Courts under Article 226. Therefore, neither court can entertain a petition asserting the suspended right during the operation of the order (unless challenging the action on grounds outside the suspended rights, such as ultra vires or mala fides under an unnotified law).",
        "சரத்து 359(1)-ன் கீழ், குறிப்பிட்ட அடிப்படை உரிமைகளை (சரத்து 20 மற்றும் 21 தவிர) அமல்படுத்துவதற்காக 'எந்தவொரு நீதிமன்றத்தையும்' அணுகும் உரிமை இடைநிறுத்தப்படுவதாக குடியரசுத் தலைவர் அறிவிக்கலாம். 'எந்தவொரு நீதிமன்றமும்' என்ற சொல் சரத்து 32-ன் கீழ் உச்ச நீதிமன்றத்தையும் சரத்து 226-ன் கீழ் உயர் நீதிமன்றங்களையும் உள்ளடக்கியது. எனவே, ஆணை அமலில் இருக்கும் போது எந்த நீதிமன்றமும் இடைநிறுத்தப்பட்ட உரிமையைக் கோரும் மனுவை விசாரிக்க முடியாது.",
        "Option A misapplies the principle that Art 226 is wider; it cannot bypass an explicit constitutional bar under Art 359.", "விருப்பம் A சரத்து 226 பரந்தது என்ற விதியை தவறாகப் பயன்படுத்துகிறது; அது சரத்து 359-ன் தடையைத் தாண்ட முடியாது.",
        "Option B is fictitious.", "விருப்பம் B கற்பனையானது.",
        "Option C correctly explains the scope of 'any court' in Article 359(1).", "விருப்பம் C சரத்து 359(1)-ல் உள்ள 'எந்தவொரு நீதிமன்றமும்' என்ற சொல்லின் அதிகார வரம்பைச் சரியாக விளக்குகிறது.",
        "Option D has no constitutional relevance.", "விருப்பம் D-க்கு அரசியலமைப்பு பொருத்தம் இல்லை.",
        "Locus Standi Bar: Art 359 suspends the locus standi to move 'any court' (High Court or Supreme Court) for the enforcement of specified fundamental rights.",
        "நீதிமன்ற அணுகல் தடை: சரத்து 359 குறிப்பிட்ட அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக 'எந்தவொரு நீதிமன்றத்தையும்' (உயர் நீதிமன்றம் அல்லது உச்ச நீதிமன்றம்) அணுகும் உரிமையை இடைநிறுத்துகிறது.",
        "However, post-44th Amendment, Articles 20 and 21 can NEVER be included in an Article 359 order.",
        "இருப்பினும், 44-வது திருத்தத்திற்குப் பிறகு, சரத்துகள் 20 மற்றும் 21-ஐ ஒருபோதும் சரத்து 359 ஆணையில் சேர்க்க முடியாது."
    ))

    # 033 - Key D
    qs.append(make_ep_q(
        PREFIX, 33, DIFF, "Constitutional Comparison", "Article 356 - Governor's Discretionary Standards",
        "In which scenario would the imposition of President's Rule under Article 356 be considered PROPER and CONSTITUTIONAL according to the Bommai guidelines (1994)?",
        "பொம்மை வழிகாட்டுதல்களின்படி (1994), பின்வரும் எந்த சூழ்நிலையில் சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியை அமல்படுத்துவது சரியானதாகவும் அரசியலமைப்பு ரீதியாகவும் ஏற்றுக்கொள்ளக்கூடியதாகக் கருதப்படும்?",
        "Where the ruling party in the State suffered a severe defeat in the Lok Sabha general elections", "மக்களவைப் பொதுத் தேர்தலில் மாநிலத்தில் ஆளும் கட்சி படுதோல்வி அடைந்த போது",
        "Where a ministry resigns, and the Governor dissolves the Assembly without exploring the formation of an alternative ministry", "ஓர் அமைச்சரவை ராஜினாமா செய்தவுடன், மாற்று அமைச்சரவை அமைக்கும் வாய்ப்புகளை ஆராயாமல் ஆளுநர் சட்டமன்றத்தைக் கலைத்த போது",
        "Where the Governor recommends dissolution without giving the Chief Minister an opportunity to demonstrate majority on the floor of the House", "அவையின் தளத்தில் முதலமைச்சர் பெரும்பான்மையை நிரூபிக்க வாய்ப்பளிக்காமல் ஆளுநர் கலைப்பிற்குப் பரிந்துரைத்த போது",
        "Where a State Government deliberately flouts a binding constitutional directive of the Union or actively undermines the basic structure feature of Secularism", "ஒரு மாநில அரசு ஒன்றியத்தின் கட்டாய அரசியலமைப்பு வழிகாட்டுதலை வேண்டுமென்றே மீறும் போது அல்லது மதச்சார்பின்மை என்ற அடிப்படைக் கட்டமைப்பை தீவிரமாக சீர்குலைக்கும் போது",
        "D",
        "In S.R. Bommai (1994), the Supreme Court categorized situations where Article 356 invocation is PROPER vs IMPROPER. Proper situations include: (1) After general elections, no party secures a majority and no coalition can be formed; (2) A ministry resigns/loses majority and no alternative government can be formed; (3) A State Government deliberately acts against constitutional directives or foundational principles such as secularism. Situations A, B, and C were explicitly declared IMPROPER and unconstitutional.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், சரத்து 356-ஐப் பயன்படுத்துவது எப்போது சரியானது மற்றும் எப்போது தவறானது என்பதை உச்ச நீதிமன்றம் வகைப்படுத்தியது. சரியான சூழ்நிலைகள்: (1) தேர்தலுக்குப் பிறகு எந்தக் கட்சிக்கும் பெரும்பான்மை கிடைக்காமல் மாற்று அரசு அமைய முடியாத போது; (2) அமைச்சரவை ராஜினாமா செய்து மாற்று அரசு சாத்தியமற்ற போது; (3) ஒரு மாநில அரசு வேண்டுமென்றே அரசியலமைப்பு வழிகாட்டுதல்களுக்கு எதிராகவோ அல்லது மதச்சார்பின்மை போன்ற அடிப்படைக் கொள்கைகளுக்கு எதிராகவோ செயல்படும் போது. விருப்பங்கள் A, B மற்றும் C ஆகியவை தவறானவை மற்றும் அரசியலமைப்பிற்கு எதிரானவை என அறிவிக்கப்பட்டன.",
        "Option A was explicitly held improper in Bommai.", "விருப்பம் A பொம்மை வழக்கில் தவறானது என வெளிப்படையாகக் கூறப்பட்டது.",
        "Option B was declared improper and unconstitutional in Bommai.", "விருப்பம் B பொம்மை வழக்கில் அரசியலமைப்பிற்கு எதிரானது என அறிவிக்கப்பட்டது.",
        "Option C was held improper in Bommai.", "விருப்பம் C பொம்மை வழக்கில் தவறானது எனப்பட்டது.",
        "Option D represents a legitimate constitutional ground for intervention under Articles 356 and 365.", "விருப்பம் D என்பது சரத்துகள் 356 மற்றும் 365-ன் கீழ் தலையிடுவதற்கான சரியான அரசியலமைப்பு காரணமாகும்.",
        "Proper vs Improper Dichotomy: Bommai established definitive benchmarks preventing partisan misuse while preserving legitimate intervention for basic structure violations.",
        "சரியான vs தவறான பயன்பாட்டுப் பிரிவு: அடிப்படைக் கட்டமைப்பு மீறல்களுக்கான சட்டப்பூர்வ தலையீட்டைப் பாதுகாக்கும் அதே வேளையில் கட்சி சார்பான தவறான பயன்பாட்டைத் தடுக்கும் திட்டவட்டமான அளவுகோல்களை பொம்மை நிறுவியது.",
        "This judgment transformed Indian federalism by curbing the arbitrary dismissal of elected state governments.",
        "தேர்ந்தெடுக்கப்பட்ட மாநில அரசுகள் தன்னிச்சையாகக் கலைக்கப்படுவதைத் தடுத்து இந்தியக் கூட்டாட்சியை இந்தத் தீர்ப்பு மாற்றியமைத்தது."
    ))

    # 034 - Key A
    qs.append(make_ep_q(
        PREFIX, 34, DIFF, "Constitutional Comparison", "National Emergency - Impact on Federal System",
        "How did Dr. B.R. Ambedkar describe the transformation of the Indian Constitution during an Emergency in the Constituent Assembly debates?",
        "அரசியலமைப்பு நிர்ணய சபை விவாதங்களில் அவசரநிலையின் போது இந்திய அரசியலமைப்பு அடையும் மாற்றத்தை டாக்டர் பி.ஆர். அம்பேத்கர் எவ்வாறு விவரித்தார்?",
        "It is designed to work as a federal system in normal times, but can convert itself into an entirely unitary system during an emergency", "இது சாதாரண காலங்களில் ஒரு கூட்டாட்சி அமைப்பாக செயல்பட வடிவமைக்கப்பட்டுள்ளது, ஆனால் அவசரநிலையின் போது தன்னை முற்றிலும் ஒரு ஒற்றையாட்சி அமைப்பாக மாற்றிக்கொள்ள முடியும்",
        "It remains strictly federal at all times without any expansion of Union powers", "மத்திய அதிகாரங்களின் எந்தவொரு விரிவாக்கமும் இன்றி இது எப்போதும் கண்டிப்பாக கூட்டாட்சியாகவே இருக்கும்",
        "It suspends the Constitution entirely and reverts India to the Government of India Act 1919", "இது அரசியலமைப்பை முற்றிலும் இடைநிறுத்திவிட்டு இந்தியாவை 1919 இந்திய அரசுச் சட்டத்திற்கு மீண்டும் மாற்றுகிறது",
        "It abolishes the office of the President and makes the military Commander-in-Chief the supreme executive", "இது குடியரசுத் தலைவர் அலுவலகத்தை ரத்து செய்து இராணுவ தலைமைத் தளபதியை உச்ச நிர்வாகியாக மாற்றுகிறது",
        "A",
        "In the Constituent Assembly, Dr. B.R. Ambedkar famously remarked: 'All federal systems including the American are placed in a tight mould of federalism. No matter what the circumstances, it cannot change its form and shape. It can never be unitary. On the other hand, the Draft Constitution can be both unitary as well as federal according to the requirements of time and circumstances. In normal times, it is framed to work as a federal system. But in times of war, it is so designed as to make it work as though it was a unitary system.'",
        "அரசியலமைப்பு நிர்ணய சபையில் டாக்டர் அம்பேத்கர் புகழ்பெற்ற கருத்தை முன்வைத்தார்: 'அமெரிக்கா உட்பட அனைத்து கூட்டாட்சி அமைப்புகளும் கூட்டாட்சியின் இறுக்கமான கட்டமைப்பில் வைக்கப்பட்டுள்ளன. சூழ்நிலைகள் எதுவாக இருந்தாலும், அதன் வடிவத்தை மாற்ற முடியாது. அது ஒருபோதும் ஒற்றையாட்சியாக மாற முடியாது. ஆனால் இந்திய அரசியலமைப்பு காலத்தின் தேவைக்கேற்ப ஒற்றையாட்சியாகவும் கூட்டாட்சியாகவும் இயங்கக்கூடியது. சாதாரண காலங்களில் இது கூட்டாட்சியாக இயங்குகிறது. ஆனால் அவசரநிலையின் போது இது ஒரு ஒற்றையாட்சி அமைப்பாக மாறும் வகையில் வடிவமைக்கப்பட்டுள்ளது.'",
        "Option A is the verbatim essence of Dr. Ambedkar's celebrated speech in the Constituent Assembly.", "விருப்பம் A என்பது அரசியலமைப்பு நிர்ணய சபையில் டாக்டர் அம்பேத்கரின் புகழ்பெற்ற உரையின் துல்லியமான சாரமாகும்.",
        "Option B contradicts the unique flexibility of the Indian constitutional architecture.", "விருப்பம் B இந்திய அரசியலமைப்பின் நெகிழ்வுத்தன்மைக்கு எதிரானது.",
        "Option C is completely incorrect regarding reverting to 1919 Act.", "விருப்பம் C 1919 சட்டத்திற்கு திரும்புவது சார்ந்து முற்றிலும் தவறானது.",
        "Option D is false regarding military takeover.", "விருப்பம் D இராணுவ ஆட்சி சார்ந்து தவறானது.",
        "Ambedkar's Architectural Genius: Indian Constitution is federal in normal times, unitary in emergency without formal constitutional amendments.",
        "அம்பேத்கரின் கட்டமைப்பு சிறப்பு: இந்திய அரசியலமைப்பு சாதாரண காலங்களில் கூட்டாட்சி; அவசரநிலையின் போது முறையான சட்ட திருத்தமின்றி ஒற்றையாட்சி.",
        "This unique elasticity prevents national disintegration during severe existential threats.",
        "இந்த தனித்துவமான நெகிழ்வுத்தன்மை கடுமையான தேசிய அச்சுறுத்தல்களின் போது நாடு சிதைந்துவிடாமல் தடுக்கிறது."
    ))

    # 035 - Key B
    qs.append(make_ep_q(
        PREFIX, 35, DIFF, "Constitutional Comparison", "Article 356 - Governor's Report Suo Motu Imposition",
        "Under Article 356, what is the legal significance of the words 'or otherwise' in the opening phrase 'if the President, on receipt of a report from the Governor of a State or otherwise, is satisfied'?",
        "சரத்து 356-ன் தொடக்க வாக்கியமான 'மாநில ஆளுநரிடமிருந்து அறிக்கை பெறப்பட்டதன் பேரில் அல்லது வேறு விதமாக குடியரசுத் தலைவர் திருப்தியடைந்தால்' என்பதில் 'அல்லது வேறு விதமாக' (or otherwise) என்ற சொல்லின் சட்ட முக்கியத்துவம் என்ன?",
        "It means the President must take the written consent of all opposition parties", "அனைத்து எதிர்க்கட்சிகளின் எழுத்துப்பூர்வ ஒப்புதலை குடியரசுத் தலைவர் பெற வேண்டும் என்று பொருள்படும்",
        "It means the President can act suo motu without receiving any report from the Governor, based on central intelligence or other reliable information", "ஆளுநரிடமிருந்து எந்த அறிக்கையும் பெறாமலேயே, மத்திய உளவுத்துறை அல்லது பிற நம்பகமான தகவல்களின் அடிப்படையில் குடியரசுத் தலைவர் தானாக முன்வந்து (suo motu) செயல்பட முடியும் என்று பொருள்படும்",
        "It means the State High Court must submit an independent judicial report", "மாநில உயர் நீதிமன்றம் ஒரு சுதந்திரமான நீதித்துறை அறிக்கையை சமர்ப்பிக்க வேண்டும் என்று பொருள்படும்",
        "It means the Governor's report must be signed by at least 10 cabinet ministers", "ஆளுநரின் அறிக்கையில் குறைந்தது 10 அமைச்சரவை அமைச்சர்கள் கையெழுத்திட வேண்டும் என்று பொருள்படும்",
        "B",
        "The words 'or otherwise' in Article 356(1) are of immense constitutional consequence. They empower the President (acting on the advice of the Union Cabinet) to proclaim President's Rule in a State even if the Governor has NOT submitted a report recommending it, or even if the Governor has reported that constitutional machinery has NOT broken down. The Centre can act on its own information.",
        "சரத்து 356(1)-ல் உள்ள 'அல்லது வேறு விதமாக' என்ற சொல் மிகுந்த அரசியலமைப்பு முக்கியத்துவம் வாய்ந்தது. ஆளுநர் குடியரசுத் தலைவர் ஆட்சிக்குப் பரிந்துரைக்காத போதிலும், அல்லது அரசியலமைப்பு முறிவு ஏற்படவில்லை என்று ஆளுநர் அறிக்கை அளித்திருந்தாலும் கூட, மத்திய அரசு தனது சொந்த தகவல்களின் அடிப்படையில் தானாக முன்வந்து குடியரசுத் தலைவர் ஆட்சியைப் பிரகடனப்படுத்த இது அதிகாரம் அளிக்கிறது.",
        "Option A is false.", "விருப்பம் A தவறானது.",
        "Option B correctly explains the autonomous suo motu power created by 'or otherwise'.", "விருப்பம் B 'அல்லது வேறு விதமாக' என்ற சொல் உருவாக்கும் தன்னிச்சையான அதிகாரத்தைச் சரியாக விளக்குகிறது.",
        "Option C is false.", "விருப்பம் C தவறானது.",
        "Option D is fictitious.", "விருப்பம் D கற்பனையானது.",
        "Suo Motu Gate: 'Or otherwise' means the President is not bound to wait for the Governor's report to invoke Article 356.",
        "தன்னிச்சையான அதிகாரம்: 'அல்லது வேறு விதமாக' என்பது சரத்து 356-ஐப் பயன்படுத்த ஆளுநரின் அறிக்கைக்காக குடியரசுத் தலைவர் காத்திருக்க வேண்டிய கட்டாயமில்லை என்பதைக் குறிக்கிறது.",
        "However, in Bommai, the Supreme Court ruled that acting 'otherwise' requires objective, verifiable material demonstrating constitutional breakdown.",
        "இருப்பினும், அவ்வாறு செயல்படுவதற்கு அரசியலமைப்பு முறிவை நிரூபிக்கும் புறநிலை, சரிபார்க்கக்கூடிய ஆதாரங்கள் தேவை என்று பொம்மை வழக்கில் கூறப்பட்டது."
    ))

    # 036 - Key C
    qs.append(make_ep_q(
        PREFIX, 36, DIFF, "Constitutional Comparison", "National Emergency - Revocation Notice Mechanism",
        "Under Article 352(8), who is the constitutional authority to whom the 1/10th members of Lok Sabha must deliver their written notice requesting a special sitting to disapprove the emergency?",
        "சரத்து 352(8)-ன் கீழ், அவசரநிலையை நிராகரிக்க சிறப்பு அமர்வைக் கோரி மக்களவையின் 1/10 பங்கு உறுப்பினர்கள் தங்கள் எழுத்துப்பூர்வ அறிவிப்பை எந்த அரசியலமைப்பு அதிகாரியிடம் சமர்ப்பிக்க வேண்டும்?",
        "Always to the Prime Minister of India", "எப்போதும் இந்தியப் பிரதமரிடம்",
        "To the Chief Justice of India", "இந்திய தலைமை நீதிபதியிடம்",
        "To the Speaker if the House is in session, or to the President if the House is not in session", "அவை அமர்வில் இருந்தால் சபாநாயகரிடம், அல்லது அவை அமர்வில் இல்லாத போது குடியரசுத் தலைவரிடம்",
        "To the Chairman of the Rajya Sabha", "மாநிலங்களவைத் தலைவரிடம்",
        "C",
        "Under Article 352(8), the notice in writing signed by not less than one-tenth of the total members of the Lok Sabha expressing their intention to move a resolution disapproving the proclamation must be given to: (1) The SPEAKER, if the House is in session; or (2) The PRESIDENT, if the House is NOT in session. Thereupon, a special sitting must be convened within 14 days.",
        "சரத்து 352(8)-ன் படி, பிரகடனத்தை நிராகரிக்கும் தீர்மானத்தை கொண்டுவரும் நோக்கத்துடன் மக்களவையின் மொத்த உறுப்பினர்களில் 1/10 பங்குக்குக் குறையாதவர்கள் கையெழுத்திட்ட எழுத்துப்பூர்வ அறிவிப்பு: (1) அவை அமர்வில் இருந்தால் சபாநாயகரிடமும்; அல்லது (2) அவை அமர்வில் இல்லாத போது குடியரசுத் தலைவரிடமும் சமர்ப்பிக்கப்பட வேண்டும். பின்னர் 14 நாட்களுக்குள் சிறப்பு அமர்வு கூட்டப்பட வேண்டும்.",
        "Option A is incorrect; notice is not given to the Prime Minister.", "விருப்பம் A தவறானது; பிரதமரிடம் அறிவிப்பு அளிக்கப்படுவதில்லை.",
        "Option B is false; Chief Justice of India plays no role in convening the House.", "விருப்பம் B தவறு; அவையைக் கூட்டுவதில் இந்திய தலைமை நீதிபதிக்கு பங்கில்லை.",
        "Option C is the exact constitutional procedure established under Article 352(8).", "விருப்பம் C சரத்து 352(8)-ன் கீழ் உள்ள துல்லியமான அரசியலமைப்பு நடைமுறையாகும்.",
        "Option D is false; Chairman of Rajya Sabha is not the recipient of this notice.", "விருப்பம் D தவறு; மாநிலங்களவைத் தலைவர் இந்த அறிவிப்பைப் பெறுபவர் அல்ல.",
        "Remember the dual recipient rule: Speaker if in session; President if not in session. Sitting within 14 days.",
        "இரட்டை பெறுநர் விதியை நினைவில் கொள்க: அமர்வில் இருந்தால் சபாநாயகர்; அமர்வில் இல்லை என்றால் குடியரசுத் தலைவர். 14 நாட்களுக்குள் சிறப்பு அமர்வு.",
        "This prevents the ruling executive from avoiding a disapproval vote by simply not convening Parliament.",
        "பாராளுமன்றத்தைக் கூட்டாமல் தவிர்ப்பதன் மூலம் ஆளும் நிர்வாகம் நிராகரிப்பு வாக்கெடுப்பைத் தட்டிக்கழிப்பதை இது தடுக்கிறது."
    ))

    # 037 - Key D
    qs.append(make_ep_q(
        PREFIX, 37, DIFF, "Constitutional Comparison", "Article 356 - Dissolution of Tamil Nadu Assembly 1991",
        "In January 1991, the DMK government in Tamil Nadu headed by M. Karunanidhi was dismissed under Article 356 by the Chandra Shekhar government at the Centre. What was the unique, highly controversial aspect of Governor Surjit Singh Barnala's role in this imposition?",
        "ஜனவரி 1991-ல், தமிழ்நாட்டில் மு. கருணாநிதி தலைமையிலான திமுக அரசு மத்தியில் இருந்த சந்திரசேகர் அரசால் சரத்து 356-ன் கீழ் கலைக்கப்பட்டது. இந்த நிகழ்வில் ஆளுநர் சுர்ஜித் சிங் பர்னாலாவின் பங்கில் இருந்த தனித்துவமான மற்றும் மிகவும் சர்ச்சைக்குரிய அம்சம் எது?",
        "Governor Barnala dissolved the assembly without informing the President", "ஆளுநர் பர்னாலா குடியரசுத் தலைவருக்குத் தெரிவிக்காமலேயே சட்டமன்றத்தைக் கலைத்தார்",
        "Governor Barnala resigned from office to join the DMK ministry", "திமுக அமைச்சரவையில் இணைய ஆளுநர் பர்னாலா தனது பதவியை ராஜினாமா செய்தார்",
        "Governor Barnala declared martial law in the state using military powers", "இராணுவ அதிகாரங்களைப் பயன்படுத்தி மாநிலத்தில் ஆளுநர் பர்னாலா இராணுவச் சட்டத்தை அறிவித்தார்",
        "Governor Barnala refused to submit a report recommending dismissal, forcing the Union Government to invoke Article 356 using the words 'or otherwise'", "கலைப்பிற்குப் பரிந்துரைக்கும் அறிக்கையை சமர்ப்பிக்க ஆளுநர் பர்னாலா மறுத்துவிட்டார், இதனால் மத்திய அரசு 'அல்லது வேறு விதமாக' என்ற சொற்களைப் பயன்படுத்தி சரத்து 356-ஐ அமல்படுத்த வேண்டிய கட்டாயம் ஏற்பட்டது",
        "D",
        "In January 1991, Tamil Nadu Governor Surjit Singh Barnala took a principled stand and categorically refused to submit a report recommending the dismissal of the elected DMK government. The Chandra Shekhar government at the Centre (pressured by its ally AIADMK) bypassed the Governor and invoked Article 356 using the phrase 'or otherwise'. Barnala later resigned when transferred to Bihar.",
        "ஜனவரி 1991-ல், தேர்ந்தெடுக்கப்பட்ட திமுக அரசைக் கலைக்கப் பரிந்துரைக்கும் அறிக்கையை சமர்ப்பிக்க தமிழ்நாடு ஆளுநர் சுர்ஜித் சிங் பர்னாலா தனது கொள்கை நிலைப்பாட்டின்படி திட்டவட்டமாக மறுத்துவிட்டார். மத்தியில் இருந்த சந்திரசேகர் அரசு (கூட்டணிக் கட்சியான அதிமுகவின் அழுத்தத்தால்) ஆளுநரைத் தவிர்த்துவிட்டு, 'அல்லது வேறு விதமாக' என்ற சொற்றொடரைப் பயன்படுத்தி சரத்து 356-ஐ அமல்படுத்தியது. பின்னர் பீகாருக்கு மாற்றப்பட்ட போது பர்னாலா ராஜினாமா செய்தார்.",
        "Option A is historically untrue regarding assembly dissolution.", "விருப்பம் A சட்டமன்றக் கலைப்பு சார்ந்து உண்மையல்ல.",
        "Option B is false; Governor Barnala did not join DMK.", "விருப்பம் B தவறு; ஆளுநர் பர்னாலா திமுகவில் இணையவில்லை.",
        "Option C is fictitious regarding martial law.", "விருப்பம் C இராணுவச் சட்டம் சார்ந்து கற்பனையானது.",
        "Option D accurately captures this famous constitutional showdown between the Union executive and a principled State Governor.", "விருப்பம் D மத்திய நிர்வாகத்திற்கும் ஒரு கொள்கைப்பிடிப்புள்ள ஆளுநருக்கும் இடையே நடந்த இந்த புகழ்பெற்ற அரசியலமைப்பு மோதலை துல்லியமாக விவரிக்கிறது.",
        "Tamil Nadu 1991 Precedent: Historic instance where Article 356 was imposed 'otherwise' because Governor Barnala refused to recommend dismissal.",
        "தமிழ்நாடு 1991 முன்னுதாரணம்: ஆளுநர் பர்னாலா கலைப்பிற்குப் பரிந்துரைக்க மறுத்ததால் 'வேறு விதமாக' சரத்து 356 பயன்படுத்தப்பட்ட வரலாற்று நிகழ்வு.",
        "This episode served as a prime example of political abuse of Article 356 cited in the Bommai judgment.",
        "பொம்மை வழக்கில் மேற்கோள் காட்டப்பட்ட சரத்து 356-ன் அரசியல் முறைகேட்டிற்கு இந்த நிகழ்வு ஒரு முக்கிய உதாரணமாக அமைந்தது."
    ))

    # 038 - Key A
    qs.append(make_ep_q(
        PREFIX, 38, DIFF, "Constitutional Comparison", "Article 356 vs Article 352 Armed Forces Deployment",
        "During a National Emergency or President's Rule, under what constitutional authority can the Union Government utilize the Armed Forces in aid of the civil power in a State?",
        "தேசிய அவசரநிலை அல்லது குடியரசுத் தலைவர் ஆட்சியின் போது, எந்த அரசியலமைப்பு அதிகாரத்தின் கீழ் மத்திய அரசு ஒரு மாநிலத்தில் குடிமை நிர்வாகத்திற்கு உதவும் வகையில் ஆயுதப் படைகளைப் பயன்படுத்த முடியும்?",
        "Under Entry 2A of List I (Union List) read with Article 355", "சரத்து 355 உடன் இணைந்த பட்டியல் I-ன் (மத்தியப் பட்டியல்) பதிவு 2A-ன் கீழ்",
        "Under Entry 1 of List II (State List) exclusively", "பட்டியல் II-ன் (மாநிலப் பட்டியல்) பதிவு 1-ன் கீழ் மட்டுமே",
        "Under the United Nations Peacekeeping Protocol 1948", "ஐக்கிய நாடுகள் அமைதி காக்கும் நெறிமுறை 1948-ன் கீழ்",
        "Only after declaring Martial Law under Article 34 throughout the entire country", "நாடு முழுவதும் சரத்து 34-ன் கீழ் இராணுவச் சட்டத்தை அறிவித்த பிறகு மட்டுமே",
        "A",
        "Entry 2A of the Union List (inserted by the 42nd Amendment Act 1976) empowers Parliament regarding: 'Deployment of any armed force of the Union or any other force subject to the control of the Union or any contingent or unit thereof in any State in aid of the civil power; powers, jurisdiction, privileges and liabilities of the members of such forces while on such deployment.' Read with the Union's duty under Article 355, this provides clear authority for central troop deployment.",
        "மத்தியப் பட்டியலின் பதிவு 2A (1976-ன் 42-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது) பின்வருவன தொடர்பாக பாராளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது: 'குடிமை நிர்வாகத்திற்கு உதவும் வகையில் ஒன்றியத்தின் எந்தவொரு ஆயுதப் படையையும் அல்லது பிற படையையும் எந்தவொரு மாநிலத்திலும் நிலைநிறுத்துதல்; அவ்வாறு நிலைநிறுத்தப்படும் போது அப்படை உறுப்பினர்களின் அதிகாரங்கள், அதிகார வரம்பு, சலுகைகள் மற்றும் பொறுப்புகள்.' சரத்து 355-ன் கீழான ஒன்றியத்தின் கடமையுடன் இணைந்து, இது மத்திய படைகளை நிலைநிறுத்த தெளிவான அதிகாரத்தை வழங்குகிறது.",
        "Option A correctly identifies Entry 2A of List I and its nexus with Article 355.", "விருப்பம் A பட்டியல் I-ன் பதிவு 2A மற்றும் சரத்து 355 உடனான அதன் தொடர்பைச் சரியாக அடையாளம் காட்டுகிறது.",
        "Option B is false; public order in Entry 1 of List II explicitly excludes deployment of armed forces of the Union.", "விருப்பம் B தவறு; பட்டியல் II-ன் பதிவு 1 வெளிப்படையாக மத்திய ஆயுதப் படைகளை விலக்குகிறது.",
        "Option C is irrelevant.", "விருப்பம் C தொடர்பற்றது.",
        "Option D confuses ordinary aid to civil power with martial law.", "விருப்பம் D குடிமைப் பணிக்கான உதவியை இராணுவச் சட்டத்துடன் குழப்புகிறது.",
        "Constitutional Authority: Entry 2A, List I gives the Union sole constitutional power to deploy armed forces in aid of civil power in any State.",
        "அரசியலமைப்பு அதிகாரம்: எந்தவொரு மாநிலத்திலும் குடிமை நிர்வாகத்திற்கு உதவ ஆயுதப் படைகளை நிலைநிறுத்த மத்தியப் பட்டியலின் பதிவு 2A மத்திய அரசுக்கு மட்டுமே அதிகாரம் அளிக்கிறது.",
        "The state police remains under state jurisdiction, but deployed central forces remain under central operational command.",
        "மாநிலக் காவல்துறை மாநில அதிகார வரம்பிற்குள் இருக்கும், ஆனால் நிலைநிறுத்தப்பட்ட மத்தியப் படைகள் மத்திய கட்டுப்பாட்டிலேயே இயங்கும்."
    ))

    # 039 - Key B
    qs.append(make_ep_q(
        PREFIX, 39, DIFF, "Constitutional Comparison", "National Emergency - Financial Order Termination",
        "Under Article 354(1), what specific provisions of the Constitution governing revenue allocation can the President modify during a National Emergency?",
        "சரத்து 354(1)-ன் கீழ், தேசிய அவசரநிலையின் போது வருவாய் ஒதுக்கீடு தொடர்பான அரசியலமைப்பின் எந்த குறிப்பிட்ட விதிகளை குடியரசுத் தலைவர் மாற்றியமைக்க முடியும்?",
        "Articles 110 to 117 (Procedures regarding Money Bills and Financial Bills)", "சரத்துகள் 110 முதல் 117 வரை (பண மசோதாக்கள் மற்றும் நிதி மசோதாக்கள் தொடர்பான நடைமுறைகள்)",
        "Articles 268 to 279 (Distribution of revenues and taxes between Union and States)", "சரத்துகள் 268 முதல் 279 வரை (மத்திய மற்றும் மாநிலங்களுக்கு இடையேயான வருவாய் மற்றும் வரிப் பகிர்வு)",
        "Articles 148 to 151 (Duties and powers of Comptroller and Auditor General)", "சரத்துகள் 148 முதல் 151 வரை (கணக்குத் தணிக்கையாளரின் கடமைகள் மற்றும் அதிகாரங்கள்)",
        "Articles 280 and 281 (Constitution and recommendations of Finance Commission)", "சரத்துகள் 280 மற்றும் 281 (நிதி ஆணையத்தின் அமைப்பு மற்றும் பரிந்துரைகள்)",
        "B",
        "Article 354(1) explicitly provides: 'The President may, while a Proclamation of Emergency is in operation, by order direct that all or any of the provisions of articles 268 to 279 shall for such period, not extending beyond the expiration of the financial year in which such Proclamation ceases to operate, as may be specified in the order, have effect subject to such exceptions or modifications as he thinks fit.'",
        "சரத்து 354(1) வெளிப்படையாகக் கூறுகிறது: 'அவசரநிலைப் பிரகடனம் அமலில் இருக்கும் போது, சரத்துகள் 268 முதல் 279 வரையிலான அனைத்து அல்லது ஏதேனும் விதிகளும், அத்தகைய பிரகடனம் முடிவுக்கு வரும் நிதி ஆண்டின் இறுதிக்கு மிகாமல் ஆணையில் குறிப்பிடப்படக்கூடிய காலத்திற்கு, தாம் தகுதியெனக் கருதும் விதிவிலக்குகள் அல்லது மாற்றங்களுக்கு உட்பட்டு செயல்பட வேண்டும் என்று குடியரசுத் தலைவர் ஆணை மூலம் உத்தரவிடலாம்.'",
        "Option A deals with central legislative procedures for money bills.", "விருப்பம் A பண மசோதாக்களுக்கான மத்திய சட்ட நடைமுறைகள் தொடர்பானது.",
        "Option B verbatim quotes the specific constitutional range (Articles 268 to 279) governed by Article 354.", "விருப்பம் B சரத்து 354-ன் கீழ் ஆளப்படும் குறிப்பிட்ட அரசியலமைப்பு சரத்துகளை (268 முதல் 279 வரை) துல்லியமாகக் குறிப்பிடுகிறது.",
        "Option C deals with the CAG.", "விருப்பம் C மத்திய கணக்குத் தணிக்கையாளர் தொடர்பானது.",
        "Option D deals with the Finance Commission.", "விருப்பம் D நிதி ஆணையம் தொடர்பானது.",
        "Article 354 Target: Articles 268 to 279 (Union-State tax sharing and grants) are the exact provisions modifiable by the President.",
        "சரத்து 354 இலக்கு: சரத்துகள் 268 முதல் 279 வரை (மத்திய-மாநில வரிப் பகிர்வு மற்றும் மானியங்கள்) குடியரசுத் தலைவரால் மாற்றியமைக்கக்கூடிய துல்லியமான விதிகளாகும்.",
        "This allows the Union to redirect financial resources immediately toward defense and national security operations.",
        "இது நாட்டின் பாதுகாப்பு மற்றும் ராணுவ நடவடிக்கைகளுக்கு நிதி வளங்களை உடனடியாகத் திருப்பிவிட மத்திய அரசுக்கு உதவுகிறது."
    ))

    # 040 - Key C
    qs.append(make_ep_q(
        PREFIX, 40, DIFF, "Constitutional Comparison", "Article 356 and State Governor Dismissal",
        "In B.P. Singhal v. Union of India (2010), what did the Constitution Bench of the Supreme Court rule regarding the arbitrary removal of Governors when a new political party comes to power at the Centre?",
        "பி.பி. சிங்கால் எதிர் இந்திய ஒன்றியம் (2010) வழக்கில், மத்தியில் ஒரு புதிய அரசியல் கட்சி ஆட்சிக்கு வரும் போது ஆளுநர்கள் தன்னிச்சையாக நீக்கப்படுவது குறித்து உச்ச நீதிமன்றத்தின் அரசியலமைப்பு அமர்வு என்ன தீர்ப்பளித்தது?",
        "The Prime Minister has absolute, unreviewable discretion to remove any Governor without assigning any reason", "எந்தக் காரணமும் கூறாமல் எந்தவொரு ஆளுநரையும் பதவி நீக்கம் செய்ய பிரதமருக்கு முழுமையான, மறுஆய்வு செய்ய முடியாத அதிகாரம் உண்டு",
        "Governors can be removed only through a formal impeachment process in the State Legislative Assembly", "மாநில சட்டமன்றத்தில் முறையான பதவி நீக்கத் தீர்மானம் (இம்பீச்மென்ட்) நிறைவேற்றப்படுவதன் மூலம் மட்டுமே ஆளுநர்களை நீக்க முடியும்",
        "While the President can remove a Governor at pleasure under Article 156(1) without showing cause, this power cannot be exercised arbitrarily, malafide, or merely because the Governor has a different political ideology from the ruling party at the Centre", "சரத்து 156(1)-ன் கீழ் காரணத்தைக் கூறாமல் விருப்பத்தின் பேரில் குடியரசுத் தலைவர் ஆளுநரை நீக்க முடியும் என்றாலும், இந்த அதிகாரத்தை தன்னிச்சையாகவோ, தவறான உள்நோக்கத்துடனோ அல்லது ஆளுநர் மத்தியில் ஆளும் கட்சியின் கொள்கையிலிருந்து மாறுபட்டவர் என்பதற்காகவோ பயன்படுத்த முடியாது",
        "Governors automatically lose their office whenever a new Lok Sabha is elected", "புதிய மக்களவை தேர்ந்தெடுக்கப்படும் போதெல்லாம் ஆளுநர்கள் தானாகவே தங்கள் பதவியை இழக்கின்றனர்",
        "C",
        "In B.P. Singhal (2010), a 5-judge Constitution Bench held that the doctrine of pleasure under Article 156(1) is not unfettered. The Union Government cannot remove Governors in a wholesale manner simply because they do not share the ideology of the new party coming to power at the Centre. While the President is not required to give reasons in advance, if challenged, the Union must show valid, compelling reasons, and arbitrary removals are subject to judicial review.",
        "பி.பி. சிங்கால் (2010) வழக்கில், 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு, சரத்து 156(1)-ன் கீழான குடியரசுத் தலைவரின் விருப்புரிமைக் கோட்பாடு வரம்பற்றது அல்ல என்று தீர்ப்பளித்தது. மத்தியில் ஆட்சிக்கு வரும் புதிய கட்சியின் கொள்கையை ஏற்கவில்லை என்பதற்காக மட்டுமே ஆளுநர்களை மொத்தமாக நீக்க முடியாது. முன்கூட்டியே காரணங்களைக் கூறத் தேவையில்லை என்றாலும், சவால் செய்யப்பட்டால் சரியான காரணங்களை மத்திய அரசு நிரூபிக்க வேண்டும்; தன்னிச்சையான நீக்கங்கள் நீதித்துறை ஆய்வுக்கு உட்பட்டவை.",
        "Option A was the unchecked executive claim rejected by the Supreme Court.", "விருப்பம் A என்பது உச்ச நீதிமன்றத்தால் நிராகரிக்கப்பட்ட தன்னிச்சையான நிர்வாக வாதமாகும்.",
        "Option B is constitutionally false; Governors have no impeachment provision.", "விருப்பம் B தவறு; ஆளுநர்களுக்கு பதவி நீக்கத் தீர்மான முறை அரசியலமைப்பில் இல்லை.",
        "Option C is the balanced, landmark constitutional principle laid down in B.P. Singhal.", "விருப்பம் C பி.பி. சிங்கால் வழக்கில் வகுக்கப்பட்ட சமநிலையான, வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்பு விதியாகும்.",
        "Option D is fictitious.", "விருப்பம் D கற்பனையானது.",
        "Governor Tenure Security: B.P. Singhal curbed the abusive convention of mass dismissals of Governors following changes in central government.",
        "ஆளுநர் பதவிக்காலப் பாதுகாப்பு: மத்தியில் ஆட்சி மாறும் போது ஆளுநர்கள் மொத்தமாக நீக்கப்படும் தவறான வழக்கத்திற்கு பி.பி. சிங்கால் தீர்ப்பு முற்றுப்புள்ளி வைத்தது.",
        "This independence is critical because Governors must author impartial Article 356 reports without fear of sudden dismissal.",
        "திடீர் பணிநீக்க அச்சமின்றி ஆளுநர்கள் நடுநிலையான சரத்து 356 அறிக்கைகளைத் தயாரிக்க இந்த சுதந்திரம் மிக அவசியமானது."
    ))

    # 041 - Key D
    qs.append(make_ep_q(
        PREFIX, 41, DIFF, "Constitutional Comparison", "Article 352 - Proclamation Approval Special Majority Calculation",
        "For approving a proclamation of National Emergency under Article 352(6), what EXACT mathematical threshold must be achieved in each House of Parliament?",
        "சரத்து 352(6)-ன் கீழ் தேசிய அவசரநிலைப் பிரகடனத்திற்கு ஒப்புதல் அளிக்க, பாராளுமன்றத்தின் ஒவ்வொரு அவையிலும் சரியாக எந்த கணித வரம்பு எட்டப்பட வேண்டும்?",
        "A simple majority of members present and voting in each House", "ஒவ்வொரு அவையிலும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களின் எளிய பெரும்பான்மை",
        "A majority of 2/3rd of the total membership of each House", "ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மை",
        "A majority of not less than 3/4th of the members present and voting", "வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் 3/4 பங்குக்குக் குறையாத பெரும்பான்மை",
        "A majority of the total membership of that House AND a majority of not less than two-thirds of the members of that House present and voting", "அந்த அவையின் மொத்த உறுப்பினர் எண்ணிக்கையில் பெரும்பான்மை மற்றும் அந்த அவையில் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் மூன்றில் இரண்டு பங்குக்குக் குறையாத பெரும்பான்மை",
        "D",
        "Article 352(6), inserted by the 44th Constitutional Amendment Act 1978, defines the special majority required for approving or continuing a National Emergency: 'by a majority of the total membership of that House and by a majority of not less than two-thirds of the members of that House present and voting.' Both conditions must be simultaneously satisfied in BOTH Houses.",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 352(6), தேசிய அவசரநிலையை அங்கீகரிக்க அல்லது தொடரத் தேவையான சிறப்புப் பெரும்பான்மையை வரையறுக்கிறது: 'அந்த அவையின் மொத்த உறுப்பினர் எண்ணிக்கையில் பெரும்பான்மை மற்றும் அந்த அவையில் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் மூன்றில் இரண்டு பங்குக்குக் குறையாத பெரும்பான்மை.' இவ்விரு நிபந்தனைகளும் இரு அவைகளிலும் ஒரே நேரத்தில் பூர்த்தியாக வேண்டும்.",
        "Option A applies to President's Rule (Article 356) and Financial Emergency (Article 360).", "விருப்பம் A குடியரசுத் தலைவர் ஆட்சி (356) மற்றும் நிதி அவசரநிலைக்குப் (360) பொருந்தும்.",
        "Option B is an impossible hyper-standard required only for impeachment of the President under Article 61.", "விருப்பம் B சரத்து 61-ன் கீழ் குடியரசுத் தலைவரின் பதவி நீக்கத்திற்கு மட்டுமே தேவையான மிகக் கடினமான வரம்பாகும்.",
        "Option C is fictitious.", "விருப்பம் C கற்பனையானது.",
        "Option D is the exact two-tier special majority defined in Article 352(6).", "விருப்பம் D சரத்து 352(6)-ல் வரையறுக்கப்பட்டுள்ள துல்லியமான இரு அடுக்கு சிறப்புப் பெரும்பான்மையாகும்.",
        "Special Majority Formula: (1) > 50% of total strength + (2) >= 2/3 of members present and voting. Both required for Article 352.",
        "சிறப்புப் பெரும்பான்மை சூத்திரம்: (1) மொத்த பலத்தில் > 50% + (2) வருகை தந்து வாக்களிப்போரில் >= 2/3 பங்கு. சரத்து 352-க்கு இரண்டும் தேவை.",
        "This is the same majority required for amending the Constitution under Article 368.",
        "சரத்து 368-ன் கீழ் அரசியலமைப்பைத் திருத்துவதற்குத் தேவைப்படும் அதே பெரும்பான்மை இதுவாகும்."
    ))

    # 042 - Key A
    qs.append(make_ep_q(
        PREFIX, 42, DIFF, "Constitutional Comparison", "Emergency Provisions - Article 358 Self-Executing Nature",
        "Why is Article 358 characterized by constitutional scholars as 'self-executing', unlike Article 359?",
        "சரத்து 359 போலல்லாமல், சரத்து 358 அரசியலமைப்பு அறிஞர்களால் 'தானாகச் செயல்படக்கூடியது' (self-executing) என்று ஏன் விவரிக்கப்படுகிறது?",
        "Because as soon as a National Emergency is declared on grounds of war or external aggression, the restrictions of Article 19 are automatically suspended without requiring any separate presidential notification", "ஏனெனில் போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு என்ற காரணத்தின் அடிப்படையில் தேசிய அவசரநிலை அறிவிக்கப்பட்ட உடனேயே, தனியான குடியரசுத் தலைவர் அறிவிக்கையின்றி சரத்து 19-ன் கட்டுப்பாடுகள் தானாகவே இடைநிறுத்தப்படுகின்றன",
        "Because it operates even if the President refuses to sign the proclamation", "ஏனெனில் குடியரசுத் தலைவர் பிரகடனத்தில் கையெழுத்திட மறுத்தாலும் இது செயல்படும்",
        "Because it applies automatically to both civil and military personnel without distinction", "ஏனெனில் இது குடிமை மற்றும் இராணுவப் பணியாளர்கள் இருவருக்கும் வேறுபாடின்றி தானாகவே பொருந்தும்",
        "Because it executes all preventive detention orders within 24 hours without judicial magistrates", "ஏனெனில் இது நீதித்துறை நடுவர்கள் இன்றி 24 மணி நேரத்திற்குள் அனைத்து தடுப்புக் காவல் ஆணைகளையும் செயல்படுத்துகிறது",
        "A",
        "Article 358 is self-executing because the automatic suspension of Article 19 takes effect by constitutional operation the moment an external emergency is declared. No separate order, notification, or declaration is required from the President. In contrast, Article 359 is NOT self-executing; it requires the President to issue an express, specific Presidential Order specifying which fundamental rights and which territories are affected.",
        "சரத்து 358 தானாகச் செயல்படக்கூடியது, ஏனெனில் வெளிப்புற அவசரநிலை அறிவிக்கப்பட்ட தருணத்திலேயே அரசியலமைப்புச் செயல்பாட்டின் மூலம் சரத்து 19-ன் இடைநிறுத்தம் உடனடியாக நடைமுறைக்கு வருகிறது. இதற்கு குடியரசுத் தலைவரிடமிருந்து தனி ஆணை, அறிவிக்கை தேவையில்லை. மாறாக, சரத்து 359 தானாகச் செயல்படாது; எந்தெந்த அடிப்படை உரிமைகள் மற்றும் பகுதிகள் பாதிக்கப்படுகின்றன என்பதைக் குறிப்பிட்டு குடியரசுத் தலைவர் ஒரு வெளிப்படையான ஆணையைப் பிறப்பிக்க வேண்டும்.",
        "Option A accurately explains the legal meaning of self-executing in the context of Article 358.", "விருப்பம் A சரத்து 358-ன் பின்னணியில் தானாகச் செயல்படும் என்பதன் சட்ட அர்த்தத்தை துல்லியமாக விளக்குகிறது.",
        "Option B is false regarding presidential signature.", "விருப்பம் B குடியரசுத் தலைவர் கையொப்பம் சார்ந்து தவறானது.",
        "Option C is incorrect regarding personnel distinction.", "விருப்பம் C பணியாளர் வேறுபாடு சார்ந்து தவறானது.",
        "Option D is fictitious.", "விருப்பம் D கற்பனையானது.",
        "Self-Executing vs Order-Dependent: Article 358 is self-executing (automatic). Article 359 is order-dependent (requires presidential notification).",
        "தானியங்கி vs ஆணை சார்ந்தது: சரத்து 358 தானாகச் செயல்படக்கூடியது (தானியங்கி). சரத்து 359 ஆணை சார்ந்தது (குடியரசுத் தலைவர் அறிவிக்கை தேவை).",
        "Because Article 359 requires an order, Parliament has the opportunity to review and scrutinize that specific order.",
        "சரத்து 359-க்கு ஆணை தேவைப்படுவதால், அந்த குறிப்பிட்ட ஆணையை ஆய்வு செய்ய பாராளுமன்றத்திற்கு வாய்ப்பு கிடைக்கிறது."
    ))

    # 043 - Key B
    qs.append(make_ep_q(
        PREFIX, 43, DIFF, "Constitutional Comparison", "Article 359 Territorial Selectivity",
        "Unlike Article 358 which automatically extends across the entire nation, can a Presidential Order under Article 359 be restricted to a specific part or territory of India?",
        "நாடு முழுவதும் தானாகவே விரிவடையும் சரத்து 358 போலல்லாமல், சரத்து 359-ன் கீழான குடியரசுத் தலைவரின் ஆணையை இந்தியாவின் ஒரு குறிப்பிட்ட பகுதிக்கு அல்லது எல்லைக்கு மட்டும் மட்டுப்படுத்த முடியுமா?",
        "No, Article 359 orders must compulsorily apply to the entire territory of India without exception", "முடியாது, விதிவிலக்கின்றி இந்தியாவின் முழு எல்லைக்கும் சரத்து 359 ஆணைகள் கட்டாயமாகப் பொருந்த வேண்டும்",
        "Yes, Article 359(1) explicitly states that the order may extend to the whole or any part of the territory of India", "ஆம், சரத்து 359(1) அந்த ஆணை இந்தியாவின் முழு எல்லைக்கோ அல்லது ஏதேனும் ஒரு பகுதிக்குமோ நீட்டிக்கப்படலாம் என்று வெளிப்படையாகக் கூறுகிறது",
        "Only if the concerned State Governor issues a concurrent proclamation under Article 213", "சம்பந்தப்பட்ட மாநில ஆளுநர் சரத்து 213-ன் கீழ் இணை பிரகடனம் வெளியிட்டால் மட்டுமே",
        "Only if approved by a referendum of the citizens residing in that specific territory", "அந்த குறிப்பிட்ட பகுதியில் வாழும் குடிமக்களின் பொது வாக்கெடுப்பு மூலம் அங்கீகரிக்கப்பட்டால் மட்டுமே",
        "B",
        "Under Article 359(1), the President may by order declare that the right to move any court for the enforcement of specified rights shall remain suspended for such period as may be specified in the order 'in the whole or any part of the territory of India'. This gives the executive the flexibility to limit the suspension of remedies to border zones or disturbed areas without infringing civil liberties nationwide.",
        "சரத்து 359(1)-ன் படி, குறிப்பிட்ட உரிமைகளை அமல்படுத்துவதற்காக நீதிமன்றத்தை அணுகும் உரிமை 'இந்தியாவின் முழு எல்லைக்கோ அல்லது அதன் ஏதேனும் ஒரு பகுதிக்குமோ' ஆணையில் குறிப்பிடப்படக்கூடிய காலத்திற்கு இடைநிறுத்தப்படும் என்று குடியரசுத் தலைவர் அறிவிக்கலாம். இது நாடு முழுவதும் குடிமை உரிமைகளைப் பாதிக்காமல், எல்லைப் பகுதிகள் அல்லது பாதிக்கப்பட்ட பகுதிகளுக்கு மட்டும் பரிகார இடைநிறுத்தத்தை மட்டுப்படுத்தும் நெகிழ்வுத்தன்மையை நிர்வாகத்திற்கு அளிக்கிறது.",
        "Option A is false; territorial selectivity was explicitly introduced by the 42nd Amendment Act 1976.", "விருப்பம் A தவறு; பிராந்திய தேர்வு 1976-ன் 42-வது திருத்தச் சட்டத்தால் வெளிப்படையாக அறிமுகப்படுத்தப்பட்டது.",
        "Option B accurately cites the constitutional text of Article 359(1).", "விருப்பம் B சரத்து 359(1)-ன் அரசியலமைப்பு உரையை துல்லியமாக மேற்கோள் காட்டுகிறது.",
        "Option C confuses ordinance powers with fundamental rights suspension.", "விருப்பம் C அவசரச் சட்ட அதிகாரங்களை அடிப்படை உரிமைகள் இடைநிறுத்தத்துடன் குழப்புகிறது.",
        "Option D is non-existent in the Indian constitutional scheme.", "விருப்பம் D இந்திய அரசியலமைப்பு அமைப்பில் இல்லாத ஒன்று.",
        "Territorial Flexibility: Article 358 applies automatically to ALL India. Article 359 can be targeted specifically to WHOLE or ANY PART of India.",
        "பிராந்திய நெகிழ்வுத்தன்மை: சரத்து 358 தானாகவே முழு இந்தியாவிற்கும் பொருந்தும். சரத்து 359-ஐ இந்தியாவின் முழுமைக்கோ அல்லது குறிப்பிட்ட பகுதிக்குமோ மட்டுப்படுத்தலாம்.",
        "This geographic targeting ensures that residents in peaceful states retain their judicial remedies.",
        "இந்த புவியியல் இலக்கு அமைத்தல் அமைதியான மாநிலங்களில் உள்ள மக்கள் தங்கள் நீதித்துறை தீர்வுகளைத் தக்கவைத்துக்கொள்வதை உறுதி செய்கிறது."
    ))

    # 044 - Key C
    qs.append(make_ep_q(
        PREFIX, 44, DIFF, "Constitutional Comparison", "Article 356 and Speaker's Powers",
        "When the State Legislative Assembly is dissolved or suspended under President's Rule (Article 356), what is the constitutional status of the Speaker of the Legislative Assembly?",
        "குடியரசுத் தலைவர் ஆட்சியின் கீழ் (சரத்து 356) மாநில சட்டமன்றம் கலைக்கப்படும் போது அல்லது நிறுத்தி வைக்கப்படும் போது, சட்டமன்ற சபாநாயகரின் அரசியலமைப்பு நிலை என்னவாக இருக்கும்?",
        "The Speaker is dismissed immediately along with the Council of Ministers", "அமைச்சரவையுடன் சேர்த்து சபாநாயகரும் உடனடியாக பதவி நீக்கம் செய்யப்படுகிறார்",
        "The Speaker assumes the executive powers of the dismissed Chief Minister", "பதவி நீக்கம் செய்யப்பட்ட முதலமைச்சரின் நிர்வாக அதிகாரங்களை சபாநாயகர் ஏற்றுக்கொள்கிறார்",
        "The Speaker does NOT vacate his office; under Article 179 proviso, the Speaker continues in office until immediately before the first meeting of the newly reconstituted Assembly", "சபாநாயகர் தனது பதவியை உடனடியாக இழப்பதில்லை; சரத்து 179-ன் நிபந்தனை விதியின் கீழ், புதிதாக அமைக்கப்படும் சட்டமன்றத்தின் முதல் கூட்டத்திற்கு சற்று முன்பு வரை அவர் தொடர்ந்து பதவியில் இருப்பார்",
        "The Speaker is automatically transferred to become a member of the Union Cabinet", "சபாநாயகர் மத்திய அமைச்சரவையின் உறுப்பினராக தானாகவே மாற்றப்படுகிறார்",
        "C",
        "Under the second proviso to Article 179 of the Constitution, whenever the Legislative Assembly is dissolved, the Speaker does not vacate his office until immediately before the first meeting of the Assembly after the dissolution. Even when Article 356 is imposed, the office of the Speaker is protected, ensuring institutional continuity of the legislative head.",
        "அரசியலமைப்பின் சரத்து 179-ன் இரண்டாவது நிபந்தனை விதியின்படி, சட்டமன்றம் கலைக்கப்படும் போதெல்லாம், கலைப்பிற்குப் பிந்தைய சட்டமன்றத்தின் முதல் கூட்டத்திற்கு சற்று முன்பு வரை சபாநாயகர் தனது பதவியை காலி செய்வதில்லை. சரத்து 356 அமல்படுத்தப்படும் போது கூட சபாநாயகரின் பதவி பாதுகாக்கப்படுகிறது, இது சட்டத்துறை தலைவரின் நிறுவன தொடர்ச்சியை உறுதி செய்கிறது.",
        "Option A is a common trap; the Council of Ministers is dismissed, but the Speaker remains in office.", "விருப்பம் A ஒரு பொதுவான பொறி; அமைச்சரவை கலைக்கப்படுகிறது, ஆனால் சபாநாயகர் பதவியில் தொடர்கிறார்.",
        "Option B is unconstitutional.", "விருப்பம் B அரசியலமைப்பிற்கு எதிரானது.",
        "Option C is the exact constitutional protection provided by the proviso to Article 179.", "விருப்பம் C சரத்து 179-ன் நிபந்தனை விதியால் வழங்கப்பட்டுள்ள துல்லியமான அரசியலமைப்பு பாதுகாப்பாகும்.",
        "Option D is fictitious.", "விருப்பம் D கற்பனையானது.",
        "Speaker Continuity Rule: Dissolution of Assembly dismisses MLAs and Ministers, but the Speaker remains in office until the new Assembly meets.",
        "சபாநாயகர் தொடர்ச்சி விதி: சட்டமன்றக் கலைப்பு சட்டமன்ற உறுப்பினர்களையும் அமைச்சர்களையும் நீக்குகிறது, ஆனால் புதிய சட்டமன்றம் கூடும் வரை சபாநாயகர் பதவியில் நீடிக்கிறார்.",
        "This ensures that assembly property, records, and parliamentary secretariat remain under an impartial elected authority.",
        "இது சட்டமன்ற சொத்துக்கள், பதிவுகள் மற்றும் செயலகம் நடுநிலையான தேர்ந்தெடுக்கப்பட்ட அதிகாரியின் கீழ் இருப்பதை உறுதி செய்கிறது."
    ))

    # 045 - Key D
    qs.append(make_ep_q(
        PREFIX, 45, DIFF, "Constitutional Comparison", "Article 352 - Written Communication of Cabinet",
        "Under Article 352(3), what exact requirement must be fulfilled before the President can issue a proclamation of National Emergency?",
        "சரத்து 352(3)-ன் கீழ், குடியரசுத் தலைவர் தேசிய அவசரநிலைப் பிரகடனத்தை வெளியிடுவதற்கு முன்பு எந்த துல்லியமான நிபந்தனை பூர்த்தி செய்யப்பட வேண்டும்?",
        "The Prime Minister must make a televised address announcing the decision", "பிரதமர் முடிவை அறிவித்து தொலைக்காட்சியில் உரையாற்ற வேண்டும்",
        "The Chief of Defence Staff must submit a classified threat evaluation report", "பாதுகாப்புப் படைகளின் தலைமைத் தளபதி வகைப்படுத்தப்பட்ட அச்சுறுத்தல் மதிப்பீட்டு அறிக்கையை சமர்ப்பிக்க வேண்டும்",
        "The Supreme Court of India must issue an advance constitutional certification", "இந்திய உச்ச நீதிமன்றம் முன்கூட்டியே அரசியலமைப்பு சான்றிதழை வழங்க வேண்டும்",
        "The decision of the Union Cabinet (the Prime Minister and other Ministers of Cabinet rank) that such a proclamation may be issued has been communicated to the President in writing", "அத்தகைய பிரகடனம் வெளியிடப்படலாம் என்ற மத்திய அமைச்சரவையின் (பிரதமர் மற்றும் கேபினட் அந்தஸ்துள்ள பிற அமைச்சர்கள்) முடிவு குடியரசுத் தலைவருக்கு எழுத்துப்பூர்வமாகத் தெரிவிக்கப்பட வேண்டும்",
        "D",
        "Article 352(3), inserted by the 44th Constitutional Amendment Act 1978, provides: 'The President shall not issue a Proclamation under clause (1) or a Proclamation varying such Proclamation unless the decision of the Union Cabinet (that is to say, the Council consisting of the Prime Minister and other Ministers of Cabinet rank under article 75) that such a Proclamation may be issued has been communicated to him in writing.'",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 352(3) கூறுகிறது: 'அத்தகைய பிரகடனம் வெளியிடப்படலாம் என்ற மத்திய அமைச்சரவையின் (அதாவது பிரதமர் மற்றும் சரத்து 75-ன் கீழ் கேபினட் அந்தஸ்து கொண்ட பிற அமைச்சர்களைக் கொண்ட குழு) முடிவு தமக்கு எழுத்துப்பூர்வமாகத் தெரிவிக்கப்பட்டாலன்றி, குடியரசுத் தலைவர் பிரிவு (1)-ன் கீழ் பிரகடனத்தையோ அல்லது அதை மாற்றும் பிரகடனத்தையோ வெளியிடக்கூடாது.'",
        "Option A describes how Indira Gandhi announced the emergency on AIR in 1975, which was done unilaterally and is now unconstitutional.", "விருப்பம் A இந்திரா காந்தி 1975-ல் வானொலியில் அவசரநிலையை அறிவித்த முறையைக் குறிக்கிறது, இது தன்னிச்சையாகச் செய்யப்பட்டது மற்றும் இப்போது அரசியலமைப்பிற்கு எதிரானது.",
        "Option B is a non-constitutional suggestion regarding CDS.", "விருப்பம் B பாதுகாப்புத் தளபதி குறித்த அரசியலமைப்பில் இல்லாத ஒரு ஆலோசனையாகும்.",
        "Option C is false regarding Supreme Court pre-certification.", "விருப்பம் C உச்ச நீதிமன்ற முன் சான்றிதழ் சார்ந்து தவறானது.",
        "Option D verbatim quotes the mandatory written Cabinet advice clause of Article 352(3).", "விருப்பம் D சரத்து 352(3)-ன் கட்டாய எழுத்துப்பூர்வ அமைச்சரவை ஆலோசனை விதியை அப்படியே மேற்கோள் காட்டுகிறது.",
        "Written Advice Safeguard: Verbal or telephone advice by the Prime Minister alone is NULL AND VOID. Entire Cabinet must decide and communicate in writing.",
        "எழுத்துப்பூர்வ ஆலோசனைக் கட்டுப்பாடு: பிரதமரின் வாய்மொழி அல்லது தொலைபேசி ஆலோசனை முற்றிலும் செல்லாது. முழு அமைச்சரவையும் கூடி எழுத்துப்பூர்வமாகத் தெரிவிக்க வேண்டும்.",
        "This historic safeguard directly eliminates the possibility of single-person autocratic emergency declarations.",
        "இந்த வரலாற்றுப் பாதுகாப்பு ஒற்றை நபர் தன்னிச்சையாக அவசரநிலையை அறிவிக்கும் வாய்ப்பை முற்றிலுமாகத் தகர்க்கிறது."
    ))

    # 046 - Key A
    qs.append(make_ep_q(
        PREFIX, 46, DIFF, "Constitutional Comparison", "National Emergency - Financial Emergency Concurrence",
        "Can a National Emergency under Article 352 and a Financial Emergency under Article 360 operate simultaneously in the territory of India?",
        "இந்திய எல்லைக்குள் சரத்து 352-ன் கீழான தேசிய அவசரநிலையும் சரத்து 360-ன் கீழான நிதி அவசரநிலையும் ஒரே நேரத்தில் செயல்பட முடியுமா?",
        "Yes, the Constitution does not prohibit concurrent operation of different types of emergencies if their respective constitutional conditions are satisfied", "ஆம், அந்தந்த அரசியலமைப்பு நிபந்தனைகள் பூர்த்தி செய்யப்பட்டால் பல்வேறு வகையான அவசரநிலைகள் ஒரே நேரத்தில் செயல்படுவதை அரசியலமைப்பு தடை செய்யவில்லை",
        "No, Article 360 explicitly bars the invocation of Financial Emergency if National Emergency is already in force", "முடியாது, தேசிய அவசரநிலை ஏற்கனவே அமலில் இருந்தால் நிதி அவசரநிலையைப் பயன்படுத்துவதை சரத்து 360 வெளிப்படையாகத் தடுக்கிறது",
        "Only if the Finance Commission passes a unanimous constitutional resolution", "நிதி ஆணையம் ஒருமனதாக அரசியலமைப்புத் தீர்மானம் நிறைவேற்றினால் மட்டுமே",
        "Only if the Supreme Court merges both proclamations into a single composite decree", "உச்ச நீதிமன்றம் இரு பிரகடனங்களையும் ஒரே ஒருங்கிணைந்த ஆணையாக இணைத்தால் மட்டுமே",
        "A",
        "There is no constitutional bar preventing the concurrent operation of different emergencies. For example, between 1975 and 1977, two National Emergencies (1971 external and 1975 internal) operated simultaneously. Similarly, a severe war accompanied by financial collapse could theoretically justify both Article 352 and Article 360 operating concurrently.",
        "வெவ்வேறு அவசரநிலைகள் ஒரே நேரத்தில் செயல்படுவதைத் தடுக்கும் எந்தவொரு அரசியலமைப்புத் தடையும் இல்லை. எடுத்துக்காட்டாக, 1975 முதல் 1977 வரை இரண்டு தேசிய அவசரநிலைகள் (1971 வெளிப்புற மற்றும் 1975 உள்நாட்டு) ஒரே நேரத்தில் செயல்பட்டன. அதேபோல், நிதி வீழ்ச்சியுடன் கூடிய கடுமையான போரின் போது சரத்து 352 மற்றும் சரத்து 360 ஆகிய இரண்டும் ஒரே நேரத்தில் செயல்படுவது கோட்பாட்டளவில் சாத்தியமாகும்.",
        "Option A is correct; constitutional powers can operate concurrently when distinct crisis triggers coexist.", "விருப்பம் A சரியானது; தனித்துவமான நெருக்கடி காரணங்கள் இருக்கும் போது அரசியலமைப்பு அதிகாரங்கள் ஒரே நேரத்தில் செயல்பட முடியும்.",
        "Option B is false; no such bar exists in Article 360.", "விருப்பம் B தவறு; சரத்து 360-ல் அத்தகைய தடை எதுவும் இல்லை.",
        "Option C is fictitious.", "விருப்பம் C கற்பனையானது.",
        "Option D is legally invalid.", "விருப்பம் D சட்டப்பூர்வமாக செல்லாது.",
        "Emergency Concurrence: Multiple emergency proclamations can co-exist simultaneously if their legal grounds are distinct and satisfied.",
        "அவசரநிலை ஒருங்கிணைப்பு: சட்டப்பூர்வ காரணங்கள் தனித்துவமாகவும் பூர்த்தியாகவும் இருந்தால் பல அவசரநிலைப் பிரகடனங்கள் ஒரே நேரத்தில் நீடிக்க முடியும்.",
        "This principle was specifically affirmed when 1971 and 1975 emergencies overlapped.",
        "1971 மற்றும் 1975 அவசரநிலைகள் ஒன்றுடன் ஒன்று சேர்ந்த போது இந்தக் கொள்கை வெளிப்படையாக உறுதி செய்யப்பட்டது."
    ))

    # 047 - Key B
    qs.append(make_ep_q(
        PREFIX, 47, DIFF, "Constitutional Comparison", "Article 356 - Duration Rules and Approvals",
        "Under Article 356(4), what is the MAXIMUM period for which a single parliamentary resolution can extend the operation of President's Rule at any one time?",
        "சரத்து 356(4)-ன் கீழ், ஒரே ஒரு பாராளுமன்றத் தீர்மானம் எந்தவொரு ஒரு குறிப்பிட்ட முறையிலும் குடியரசுத் தலைவர் ஆட்சியை நீட்டிக்கக்கூடிய அதிகபட்ச காலம் என்ன?",
        "One year at a time", "ஒரு முறைக்கு ஒரு ஆண்டு",
        "Six months at a time", "ஒரு முறைக்கு ஆறு மாதங்கள்",
        "Three months at a time", "ஒரு முறைக்கு மூன்று மாதங்கள்",
        "Two years at a time", "ஒரு முறைக்கு இரண்டு ஆண்டுகள்",
        "B",
        "Under Article 356(4), every proclamation approved by Parliament shall, unless revoked, cease to operate on the expiration of a period of SIX MONTHS from the date of issue (or date of approval). It can be extended for further periods of SIX MONTHS AT A TIME, subject to the overall ceiling of three years (and the Article 356(5) one-year barrier). A single resolution can never grant an extension exceeding six months.",
        "சரத்து 356(4)-ன் படி, பாராளுமன்றத்தால் அங்கீகரிக்கப்பட்ட ஒவ்வொரு பிரகடனமும் திரும்பப் பெறப்படாவிட்டால், ஆறு மாத காலம் முடிந்தவுடன் செயல்படுவதை நிறுத்திவிடும். ஒட்டுமொத்த வரம்பான மூன்று ஆண்டுகளுக்கு உட்பட்டு (மற்றும் சரத்து 356(5)-ன் ஒரு ஆண்டு தடைக்கு உட்பட்டு) ஒரு முறைக்கு ஆறு மாதங்கள் வீதம் இதை நீட்டிக்க முடியும். ஒரே ஒரு தீர்மானம் ஒருபோதும் ஆறு மாதங்களுக்கு மேல் நீட்டிப்பு வழங்க முடியாது.",
        "Option A is incorrect; extension is 6 months at a time, not 1 year (unlike Lok Sabha extension under Art 83(2)).", "விருப்பம் A தவறானது; மக்களவை நீட்டிப்பு போலல்லாமல், இது ஒரு முறைக்கு 6 மாதங்கள் மட்டுமே, 1 ஆண்டு அல்ல.",
        "Option B is the precise statutory increment under Article 356(4).", "விருப்பம் B சரத்து 356(4)-ன் கீழான துல்லியமான கால அவகாசமாகும்.",
        "Option C is false.", "விருப்பம் C தவறானது.",
        "Option D is constitutionally prohibited.", "விருப்பம் D அரசியலமைப்பு ரீதியாக தடைசெய்யப்பட்டது.",
        "Extension Increment Rule: Both National Emergency (Art 352) and President's Rule (Art 356) extend in 6-MONTH INCREMENTS upon parliamentary approval.",
        "நீட்டிப்பு தவணை விதி: தேசிய அவசரநிலை (352) மற்றும் குடியரசுத் தலைவர் ஆட்சி (356) ஆகிய இரண்டும் பாராளுமன்ற ஒப்புதலில் 6 மாத தவணைகளாகவே நீட்டிக்கப்படுகின்றன.",
        "This forces the government to continually return to Parliament to justify continued direct central administration.",
        "இது தொடர்ச்சியான மத்திய நிர்வாகத்தை நியாயப்படுத்த அரசாங்கத்தை தொடர்ந்து பாராளுமன்றத்திற்கு வர வைக்கிறது."
    ))

    # 048 - Key C
    qs.append(make_ep_q(
        PREFIX, 48, DIFF, "Constitutional Comparison", "Article 358 vs 359 - Civil Court Suits post-Emergency",
        "Once a National Emergency is revoked, can a citizen file a suit against the government for compensation regarding an executive act committed during the emergency that violated Article 19, if that executive act was NOT authorized by any valid emergency law?",
        "தேசிய அவசரநிலை திரும்பப் பெறப்பட்ட பிறகு, அவசரநிலையின் போது செல்லுபடியாகும் அவசரநிலைச் சட்டம் எதனாலும் அங்கீகரிக்கப்படாமல், சரத்து 19-ஐ மீறி செய்யப்பட்ட ஒரு நிர்வாக நடவடிக்கைக்கு இழப்பீடு கோரி ஒரு குடிமகன் அரசாங்கத்தின் மீது வழக்குத் தொடர முடியுமா?",
        "No, all actions committed during an emergency receive blanket perpetual indemnity under Article 361", "முடியாது, அவசரநிலையின் போது செய்யப்பட்ட அனைத்து நடவடிக்கைகளும் சரத்து 361-ன் கீழ் நிரந்தரப் பாதுகாப்புப் பெறுகின்றன",
        "No, citizens can never sue the State for tortious acts under sovereign immunity", "முடியாது, இறையாண்மை அதிகாரப் பாதுகாப்பின் கீழ் அரசுக்கு எதிராக குடிமக்கள் இழப்பீட்டு வழக்குத் தொடரவே முடியாது",
        "Yes, because Article 358 protects only laws containing the emergency recital and executive actions taken under such laws; unauthorized executive actions enjoy no immunity and can be challenged post-emergency", "ஆம், ஏனெனில் சரத்து 358 அவசரநிலை அறிவிப்பைக் கொண்ட சட்டங்களையும் அவற்றின் கீழ் எடுக்கப்பட்ட நிர்வாக நடவடிக்கைகளையும் மட்டுமே பாதுகாக்கிறது; அங்கீகரிக்கப்படாத நிர்வாக நடவடிக்கைகளுக்கு எந்தப் பாதுகாப்பும் இல்லை, அவசரநிலைக்குப் பின் அவற்றை சவால் செய்யலாம்",
        "Only if the International Court of Justice grants leave to appeal", "சர்வதேச நீதிமன்றம் மேல்முறையீட்டுக்கு அனுமதி அளித்தால் மட்டுமே",
        "C",
        "Article 358(1) and (2) make it clear that as soon as the proclamation of emergency ceases to operate, Article 19 is fully restored. Crucially, things done or omitted to be done are protected ONLY if they were authorized by a law containing the emergency recital or executive action taken under that law. Purely unauthorized, ultra vires, or illegal executive actions receive no immunity, and citizens can claim damages or remedies in court once normalcy returns.",
        "சரத்து 358(1) மற்றும் (2) அவசரநிலைப் பிரகடனம் முடிவுக்கு வந்த உடனேயே சரத்து 19 முழுமையாக மீட்டெடுக்கப்படுவதை தெளிவாக்குகின்றன. மிக முக்கியமாக, அவசரநிலை அறிவிப்பைக் கொண்ட ஒரு சட்டத்தால் அங்கீகரிக்கப்பட்டிருந்தால் மட்டுமே செய்யப்பட்ட செயல்களுக்கு பாதுகாப்பு கிடைக்கும். சட்டப்பூர்வ அங்கீகாரமற்ற, அதிகார வரம்பை மீறிய அல்லது சட்டவிரோதமான நிர்வாக நடவடிக்கைகள் எந்தப் பாதுகாப்பையும் பெறாது; இயல்பு நிலை திரும்பியதும் குடிமக்கள் நீதிமன்றத்தில் இழப்பீடு அல்லது நிவாரணம் கோரலாம்.",
        "Option A is false; Article 361 protects the personal office of the President and Governors, not the illegal acts of administrative officers.", "விருப்பம் A தவறு; சரத்து 361 குடியரசுத் தலைவர்/ஆளுநரின் பதவியைப் பாதுகாக்கிறது, அதிகாரிகளின் சட்டவிரோத செயல்களை அல்ல.",
        "Option B is outdated sovereign immunity dogma largely dismantled by Kasturi Lal exceptions and modern fundamental rights jurisprudence (Nilabati Behera).", "விருப்பம் B என்பது நவீன அடிப்படை உரிமை சட்டங்களால் நிராகரிக்கப்பட்ட பழைய வாதமாகும்.",
        "Option C accurately represents the modern constitutional standard of post-emergency state liability.", "விருப்பம் C அவசரநிலைக்குப் பிந்தைய அரசுப் பொறுப்புடைமையின் நவீன அரசியலமைப்புத் தரத்தை துல்லியமாகக் குறிக்கிறது.",
        "Option D is irrelevant.", "விருப்பம் D தொடர்பற்றது.",
        "Post-Emergency Reckoning: Immunity is narrow and conditional. Arbitrary acts committed outside the cover of valid emergency laws face full civil and constitutional liability once the emergency ends.",
        "அவசரநிலைக்குப் பிந்தைய விசாரணை: அவசரநிலை பாதுகாப்பு குறுகியது மற்றும் நிபந்தனைக்கு உட்பட்டது. செல்லுபடியாகும் சட்டங்களின் வரம்பிற்கு வெளியே செய்யப்பட்ட தன்னிச்சையான செயல்கள் அவசரநிலை முடிந்தவுடன் முழு இழப்பீட்டுப் பொறுப்பை எதிர்கொள்ளும்.",
        "This ensures that individual bureaucrats cannot inflict lawless harm under the psychological shelter of an emergency.",
        "அவசரநிலையின் கீழ் தனிப்பட்ட அதிகாரிகள் சட்டவிரோத தீங்குகளை இழைக்க முடியாது என்பதை இது உறுதி செய்கிறது."
    ))

    # 049 - Key D
    qs.append(make_ep_q(
        PREFIX, 49, DIFF, "Constitutional Comparison", "Article 356 - Judicial Restitution Power",
        "In S.R. Bommai (1994), what unprecedented remedial power did the Supreme Court assert it possesses if it declares a proclamation of President's Rule unconstitutional?",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், குடியரசுத் தலைவர் ஆட்சிப் பிரகடனம் அரசியலமைப்பிற்கு எதிரானது என அறிவித்தால், தமக்கு உள்ளதாக உச்ச நீதிமன்றம் உறுதிப்படுத்திய முன்னோடியில்லாத பரிகார அதிகாரம் எது?",
        "The power to arrest the Union Cabinet ministers under contempt of court", "நீதிமன்ற அவமதிப்பின் கீழ் மத்திய அமைச்சரவை அமைச்சர்களைக் கைது செய்யும் அதிகாரம்",
        "The power to direct fresh parliamentary elections nationwide", "நாடு முழுவதும் புதிய பாராளுமன்றத் தேர்தல்களை நடத்த உத்தரவிடும் அதிகாரம்",
        "The power to suspend the Constitution of India and assume supreme executive control", "இந்திய அரசியலமைப்பை இடைநிறுத்தி உச்ச நிர்வாகக் கட்டுப்பாட்டை ஏற்கும் அதிகாரம்",
        "The power of restitution to restore the status quo ante by reviving the dismissed State Legislative Assembly and reinstating the dismissed Council of Ministers", "கலைக்கப்பட்ட மாநில சட்டமன்றத்தை மீண்டும் உயிர்ப்பிப்பதன் மூலமும், பதவி நீக்கம் செய்யப்பட்ட அமைச்சரவையை மீண்டும் பதவியில் அமர்த்துவதன் மூலமும் பழைய நிலையை (status quo ante) மீட்டெடுக்கும் அதிகாரம்",
        "D",
        "Prior to S.R. Bommai (1994), it was believed that once an Assembly was dissolved and President's Rule was declared, the court could not undo the dismissal. The Supreme Court in Bommai broke new ground by declaring that the court has the full constitutional power of RESTITUTION: if the proclamation is found unconstitutional and malafide, the court can restore the status quo ante, reviving the dissolved Legislative Assembly and reinstating the dismissed Ministry.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கிற்கு முன்பு, ஒருமுறை சட்டமன்றம் கலைக்கப்பட்டு குடியரசுத் தலைவர் ஆட்சி அறிவிக்கப்பட்டால், நீதிமன்றத்தால் அதை மாற்ற முடியாது என்றே கருதப்பட்டது. ஆனால் பொம்மை வழக்கில் உச்ச நீதிமன்றம் ஒரு புதிய வரலாற்று மைல்கல்லை நிறுவியது: பிரகடனம் அரசியலமைப்பிற்கு எதிரானது எனக் கண்டறியப்பட்டால், நீதிமன்றத்திற்கு முழுமையான மீட்பு அதிகாரம் (Restitution) உண்டு; அது கலைக்கப்பட்ட சட்டமன்றத்தை மீண்டும் உயிர்ப்பித்து, பதவி நீக்கம் செய்யப்பட்ட அமைச்சரவையை மீண்டும் பதவியில் அமர்த்த முடியும்.",
        "Option A is false.", "விருப்பம் A தவறானது.",
        "Option B is outside judicial purview.", "விருப்பம் B நீதித்துறை அதிகார வரம்பிற்கு அப்பாற்பட்டது.",
        "Option C is impossible under constitutional democracy.", "விருப்பம் C சாத்தியமற்றது.",
        "Option D is the historic doctrine of 'Restitution and Revival' established in S.R. Bommai.", "விருப்பம் D என்பது பொம்மை வழக்கில் நிறுவப்பட்ட வரலாற்றுச் சிறப்புமிக்க 'மீட்பு மற்றும் உயிர்ப்பித்தல்' கோட்பாடாகும்.",
        "Bommai Revival Power: If Article 356 is struck down, the court can literally resurrect the dissolved assembly and dismissed ministry back into power.",
        "பொம்மை உயிர்ப்பித்தல் அதிகாரம்: சரத்து 356 ரத்து செய்யப்பட்டால், கலைக்கப்பட்ட சட்டமன்றத்தையும் அமைச்சரவையையும் மீண்டும் அதிகாரத்திற்கு கொண்டுவரும் அதிகாரம் நீதிமன்றத்திற்கு உண்டு.",
        "This revolutionary remedy made executive abuse of Article 356 legally dangerous and politically self-defeating.",
        "இந்த புரட்சிகரமான நிவாரணம் சரத்து 356-ஐ நிர்வாகம் துஷ்பிரயோகம் செய்வதை சட்டரீதியாக ஆபத்தானதாகவும், அரசியல் ரீதியாக தோல்வியடையக்கூடியதாகவும் மாற்றியது."
    ))

    # 050 - Key D
    qs.append(make_ep_q(
        PREFIX, 50, DIFF, "Constitutional Comparison", "Emergency Provisions - Comprehensive Review",
        "Which of the following statements is entirely ACCURATE across all three types of emergencies in the Indian Constitution?",
        "இந்திய அரசியலமைப்பில் உள்ள மூன்று வகையான அவசரநிலைகளிலும் பின்வரும் கூற்றுகளில் எது முற்றிலும் சரியானது?",
        "All three emergencies require a special majority of Parliament for initial approval", "மூன்று அவசரநிலைகளுக்கும் ஆரம்ப ஒப்புதலுக்கு பாராளுமன்றத்தின் சிறப்புப் பெரும்பான்மை தேவைப்படுகிறது",
        "Fundamental rights under Articles 20 and 21 can be suspended in all three types of emergencies", "மூன்று வகையான அவசரநிலைகளிலும் சரத்துகள் 20 மற்றும் 21-ன் கீழான அடிப்படை உரிமைகள் இடைநிறுத்தப்படலாம்",
        "All three emergencies can continue indefinitely without any parliamentary periodic renewal", "மூன்று அவசரநிலைகளும் பாராளுமன்ற குறிப்பிட்ட கால புதுப்பித்தல் ஏதுமின்றி காலவரையின்றி தொடரலாம்",
        "National Emergency (Art 352) requires a special majority and has no upper time limit; President's Rule (Art 356) requires a simple majority and has a 3-year normal maximum limit; Financial Emergency (Art 360) requires a simple majority, has no upper time limit, and needs no periodic approval once approved", "தேசிய அவசரநிலைக்கு (352) சிறப்புப் பெரும்பான்மை தேவை மற்றும் உச்ச வரம்பு இல்லை; குடியரசுத் தலைவர் ஆட்சிக்கு (356) எளிய பெரும்பான்மை தேவை மற்றும் 3 ஆண்டு சாதாரண அதிகபட்ச வரம்பு உண்டு; நிதி அவசரநிலைக்கு (360) எளிய பெரும்பான்மை தேவை, உச்ச வரம்பு இல்லை மற்றும் ஒருமுறை ஒப்புதல் பெற்ற பின் குறிப்பிட்ட கால ஒப்புதல் தேவையில்லை",
        "D",
        "Statement D provides the flawless, master comparative summary of all three types of emergencies: (1) National Emergency (Art 352): Approved by Special Majority within 1 month, periodic approval every 6 months, no maximum limit; (2) President's Rule (Art 356): Approved by Simple Majority within 2 months, periodic approval every 6 months, maximum limit of 3 years; (3) Financial Emergency (Art 360): Approved by Simple Majority within 2 months, no maximum limit, no periodic re-approval required.",
        "கூற்று D மூன்று வகையான அவசரநிலைகளின் குறைபாடற்ற, முழுமையான ஒப்பீட்டுச் சுருக்கத்தை வழங்குகிறது: (1) தேசிய அவசரநிலை (352): 1 மாதத்திற்குள் சிறப்புப் பெரும்பான்மையால் ஒப்புதல், ஒவ்வொரு 6 மாதங்களுக்கும் மறு ஒப்புதல், அதிகபட்ச கால வரம்பு இல்லை; (2) குடியரசுத் தலைவர் ஆட்சி (356): 2 மாதங்களுக்குள் எளிய பெரும்பான்மையால் ஒப்புதல், ஒவ்வொரு 6 மாதங்களுக்கும் மறு ஒப்புதல், அதிகபட்ச வரம்பு 3 ஆண்டுகள்; (3) நிதி அவசரநிலை (360): 2 மாதங்களுக்குள் எளிய பெரும்பான்மையால் ஒப்புதல், அதிகபட்ச வரம்பு இல்லை, தொடர் மறு ஒப்புதல் தேவையில்லை.",
        "Option A is false; only Article 352 requires a special majority.", "விருப்பம் A தவறு; சரத்து 352 மட்டுமே சிறப்புப் பெரும்பான்மையைக் கோருகிறது.",
        "Option B is false; Articles 20 and 21 can NEVER be suspended under any emergency.", "விருப்பம் B தவறு; சரத்துகள் 20 மற்றும் 21 எந்த அவசரநிலையிலும் ஒருபோதும் இடைநிறுத்தப்பட முடியாது.",
        "Option C is false; Articles 352 and 356 require 6-month periodic approvals.", "விருப்பம் C தவறு; சரத்துகள் 352 மற்றும் 356-க்கு 6 மாத கால ஒப்புதல் தேவைப்படுகிறது.",
        "Option D is the master synthesis of constitutional emergency provisions.", "விருப்பம் D அவசரநிலைப் பிரிவுகளின் துல்லியமான ஒப்பீட்டு விளக்கமாகும்.",
        "Master Formula of Emergency Provisions: Master the differences in (1) Approval deadline, (2) Majority type, (3) Periodic renewal, and (4) Maximum duration across 352, 356, and 360.",
        "அவசரநிலைப் பிரிவுகளின் முதன்மை சூத்திரம்: சரத்துகள் 352, 356 மற்றும் 360-ல் உள்ள (1) ஒப்புதல் காலக்கெடு, (2) பெரும்பான்மை வகை, (3) குறிப்பிட்ட கால புதுப்பித்தல், மற்றும் (4) அதிகபட்ச கால அளவு ஆகியவற்றின் வேறுபாடுகளில் தேர்ச்சி பெறுங்கள்.",
        "This comprehensive analytical comparison represents the absolute pinnacle of TNPSC Group 1 Polity syllabus mastery.",
        "இந்த விரிவான ஒப்பீட்டு ஆய்வு TNPSC குரூப் 1 இந்திய ஆட்சியியல் பாடத்திட்டத்தின் முழுமையான தேர்ச்சியைக் குறிக்கிறது."
    ))

    return qs

def build_and_validate_hard():
    qs = get_hard_questions() + get_hard_questions_part2()
    print(f"[HARD] Total questions generated: {len(qs)}")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"

    # Check key balance
    dist = dict(Counter([q["correct_answer"] for q in qs]))
    print(f"[HARD] Key Distribution: {dist}")
    assert dist == {"A": 13, "B": 12, "C": 12, "D": 13}, f"Distribution mismatch: {dist}"

    # Check uniqueness
    stems = [q["question_en"].strip().lower() for q in qs]
    assert len(stems) == len(set(stems)), "Duplicate stems found in Hard set!"
    print("[HARD] Stems are 100% unique.")

    out_file = "data/questions/polity/emergency_provisions_hard.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"[HARD] Saved to {out_file}")

    rep = ContentValidator.validate_file(out_file, expected_count=50, expected_prefix=PREFIX)
    print(f"[HARD] Validator Status: {'PASS' if rep.is_valid else 'FAIL'} | Audited: {rep.total_audited}")
    if rep.issues:
        for iss in rep.issues:
            print(f"  [{iss.severity}] {iss.question_id}: {iss.message}")
        assert False, "Validation failed!"
    print("[HARD] Validation PASSED with 0 issues!")

if __name__ == "__main__":
    build_and_validate_hard()
