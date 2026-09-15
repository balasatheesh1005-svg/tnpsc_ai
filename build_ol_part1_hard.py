# -*- coding: utf-8 -*-
"""
Official Language - Part 1 Hard MCQs Generator (50 MCQs: OL_H_001 to OL_H_050)
Strictly adheres to:
- 24 required fields schema
- Authentic Tamil translations
- Specific why_not_others for A, B, C, D
- Balanced answer keys (12-13 per option)
- ContentValidator pass
"""
import json
import os
from official_language_mcq_helper import make_ol_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_hard_questions():
    raw_data = [
        # 1
        {
            "subtopic": "Article 350A Directive and Article 365 Sanction",
            "stem_en": "If a State Government consistently fails to comply with a binding directive issued by the President under Article 350A regarding mother-tongue primary instruction facilities, what constitutional consequence may arise under Article 365?",
            "stem_ta": "தாய்மொழி வழியிலான தொடக்கக் கல்வி வசதிகள் தொடர்பாக சரத்து 350A-ன் கீழ் குடியரசுத் தலைவரால் பிறப்பிக்கப்படும் கட்டாய உத்தரவுக்கு ஒரு மாநில அரசு தொடர்ந்து இணங்கத் தவறினால், சரத்து 365-ன் கீழ் எத்தகைய அரசியலமைப்பு விளைவு ஏற்படக்கூடும்?",
            "options": [
                ("The President may hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the Constitution, attracting Article 356 (President's Rule)", "மாநில அரசு அரசியலமைப்பு விதிகளின்படி நடைபெற முடியாத சூழ்நிலை உருவாகியுள்ளதாகக் கருதி, குடியரசுத் தலைவர் சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியை அமல்படுத்தலாம்"),
                ("The Supreme Court automatically dissolves the State Legislative Assembly without executive intervention", "உச்ச நீதிமன்றம் நிர்வாகத் தலையீடின்றி மாநில சட்டமன்றப் பேரவையைத் தானாகவே கலைத்துவிடும்"),
                ("The State loses its representation in the Rajya Sabha for a minimum period of five years", "மாநிலமானது மாநிலங்களவையில் தனது பிரதிநிதித்துவத்தை குறைந்தபட்சம் ஐந்து ஆண்டுகளுக்கு இழந்துவிடும்"),
                ("The official language of that State is automatically replaced with Hindi by the Union Cabinet", "அம்மாநிலத்தின் அதிகாரப்பூர்வ மொழி ஒன்றிய அமைச்சரவையால் தானாகவே இந்தியாக மாற்றப்படும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 350A empowers the President to issue such directives to any State as he considers necessary. Under Article 365, where any State fails to comply with any directions given in the exercise of the executive power of the Union, the President may hold that the State cannot be carried on in accordance with the Constitution (invoking Article 356).",
            "exp_ta": "சரத்து 350A குடியரசுத் தலைவர் தான் அவசியமெனக் கருதும் உத்தரவுகளை எந்தவொரு மாநிலத்திற்கும் பிறப்பிக்க அதிகாரமளிக்கிறது. சரத்து 365-ன் படி, ஒன்றியத்தின் நிர்வாக அதிகாரத்தின் கீழ் வழங்கப்படும் உத்தரவுகளுக்கு ஒரு மாநிலம் இணங்கத் தவறினால், அங்கு அரசியலமைப்பு இயந்திரம் முறிந்துவிட்டதாகக் கருதி சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியைப் பிரகடனப்படுத்தலாம்.",
            "why_a_en": "Article 365 links non-compliance with valid Union directives directly to the invocation of President's Rule under Article 356.",
            "why_a_ta": "சரத்து 365 செல்லுபடியாகும் ஒன்றிய உத்தரவுகளுக்கு இணங்கத் தவறுவதை சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சியுடன் நேரடியாக இணைக்கிறது.",
            "why_b_en": "The Supreme Court does not dissolve legislative assemblies under Article 350A/365.",
            "why_b_ta": "உச்ச நீதிமன்றம் சரத்து 350A/365-ன் கீழ் சட்டமன்றங்களைக் கலைப்பதில்லை.",
            "why_c_en": "Rajya Sabha representation is constitutionally fixed in the Fourth Schedule and cannot be suspended under Article 365.",
            "why_c_ta": "மாநிலங்களவை பிரதிநிதித்துவம் நான்காவது அட்டவணையில் நிர்ணயிக்கப்பட்டுள்ளது மற்றும் சரத்து 365-ன் கீழ் இடைநிறுத்தப்பட முடியாது.",
            "why_d_en": "The Union Cabinet cannot unilaterally replace a State's official language enacted under Article 345.",
            "why_d_ta": "சரத்து 345-ன் கீழ் இயற்றப்பட்ட ஒரு மாநிலத்தின் அதிகாரப்பூர்வ மொழியை ஒன்றிய அமைச்சரவை ஒருதலைப்பட்சமாக மாற்ற முடியாது.",
            "tip_en": "Constitutional Linkage: Article 350A (Directive) -> Article 365 (Failure to Comply) -> Article 356 (President's Rule).",
            "tip_ta": "அரசியலமைப்பு இணைப்பு: சரத்து 350A (உத்தரவு) -> சரத்து 365 (இணங்கத் தவறுதல்) -> சரத்து 356 (குடியரசுத் தலைவர் ஆட்சி).",
            "fact_en": "Dr. B.R. Ambedkar termed Article 365 as the necessary coercive machinery to enforce constitutional directives.",
            "fact_ta": "டாக்டர் அம்பேத்கர் சரத்து 365-ஐ அரசியலமைப்பு வழிகாட்டுதல்களைச் செயல்படுத்துவதற்கான இன்றியமையாத கட்டாயக் கருவி என்றார்."
        },
        # 2
        {
            "subtopic": "Section 3(3) Strict Liability on Signing Officer",
            "stem_en": "Under Rule 6 of the Official Languages Rules, 1976, who bears the personal administrative responsibility to ensure that documents specified under Section 3(3) of the Official Languages Act, 1963 are executed both in Hindi and English?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள், 1976-ன் விதி 6-ன் கீழ், அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 3(3)-ன் கீழ் குறிப்பிடப்பட்டுள்ள ஆவணங்கள் இந்தி மற்றும் ஆங்கிலம் ஆகிய இரண்டிலும் நிறைவேற்றப்படுவதை உறுதி செய்வதற்கான தனிப்பட்ட நிர்வாகப் பொறுப்பு யாருக்கு உரியது?",
            "options": [
                ("The person signing such documents", "அத்தகைய ஆவணங்களில் கையொப்பமிடும் நபர்"),
                ("The Minister in charge of the Department exclusively", "துறைக்கு பொறுப்பான அமைச்சர் மட்டுமே"),
                ("The Official Language Officer of the Ministry exclusively", "அமைச்சகத்தின் அதிகாரப்பூர்வ மொழி அலுவலர் மட்டுமே"),
                ("The Central Vigilance Commissioner", "மத்திய விழிப்புணர்வு ஆணையர்")
            ],
            "correct_key": "A",
            "exp_en": "Rule 6 of the Official Languages Rules, 1976 unequivocally lays down that it shall be the responsibility of the person signing such documents to ensure that they are made, issued, or sent both in Hindi and English.",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் விதி 6, அத்தகைய ஆவணங்களில் கையொப்பமிடும் நபரே அவை இந்தி மற்றும் ஆங்கிலம் ஆகிய இரண்டிலும் உருவாக்கப்படுவதையும், வெளியிடப்படுவதையும் அல்லது அனுப்பப்படுவதையும் உறுதி செய்ய வேண்டும் என்று திட்டவட்டமாகப் பொறுப்பை நிர்ணயிக்கிறது.",
            "why_a_en": "Rule 6 places strict liability on the individual signatory officer, preventing shifting of administrative blame.",
            "why_a_ta": "விதி 6 கையொப்பமிடும் அலுவலர் மீது நேரடிப் பொறுப்பைச் சுமத்துகிறது, நிர்வாகப் பழியைப் பிறர் மீது மாற்றுவதைத் தடுக்கிறது.",
            "why_b_en": "Ministers do not sign every tender, contract, and general order under Section 3(3).",
            "why_b_ta": "அமைச்சர்கள் பிரிவு 3(3)-ன் கீழான ஒவ்வொரு ஒப்பந்தம் மற்றும் பொது ஆணைகளிலும் கையொப்பமிடுவதில்லை.",
            "why_c_en": "Official Language Officers assist in translation, but the signatory bears legal responsibility.",
            "why_c_ta": "மொழி அலுவலர்கள் மொழிபெயர்ப்பில் உதவுகிறார்கள், ஆனால் கையொப்பமிடுபவரே சட்டப் பொறுப்பை ஏற்கிறார்.",
            "why_d_en": "The CVC investigates corruption, not document language formatting.",
            "why_d_ta": "மத்திய விழிப்புணர்வு ஆணையம் ஊழலை விசாரிக்கிறது, மொழி வடிவமைப்பை அல்ல.",
            "tip_en": "Rule 6: Personal liability for Section 3(3) bilingualism rests on the SIGNING OFFICER.",
            "tip_ta": "விதி 6: பிரிவு 3(3) இருமொழி இணக்கத்திற்கான தனிப்பட்ட பொறுப்பு கையொப்பமிடும் அலுவலரிடமே உள்ளது.",
            "fact_en": "An officer who issues a Section 3(3) document only in one language commits an actionable procedural violation.",
            "fact_ta": "பிரிவு 3(3) ஆவணத்தை ஒரே மொழியில் மட்டும் வெளியிடும் ஓர் அலுவலர் நடைமுறை விதிமீறல் செய்தவராகக் கருதப்படுவார்."
        },
        # 3
        {
            "subtopic": "Article 348(3) Deemed Status vs Vernacular Texts",
            "stem_en": "Where a State Legislature passes an Act in a regional language (e.g. Tamil) and publishes an English translation under Article 348(3), which text is authoritative in case of conflict before the Supreme Court?",
            "stem_ta": "ஒரு மாநில சட்டமன்றம் ஒரு வட்டார மொழியில் (எ.கா. தமிழ்) ஒரு சட்டத்தை நிறைவேற்றி, சரத்து 348(3)-ன் கீழ் அதன் ஆங்கில மொழிபெயர்ப்பை வெளியிடும் போது, உச்ச நீதிமன்றத்தின் முன் முரண்பாடு ஏற்படும் பட்சத்தில் எந்த வாசகம் அதிகாரப்பூர்வமானதாக மேலோங்கும்?",
            "options": [
                ("The English translation published under Article 348(3), as it is deemed to be the authoritative text", "சரத்து 348(3)-ன் கீழ் வெளியிடப்பட்ட ஆங்கில மொழிபெயர்ப்பு, ஏனெனில் அதுவே அதிகாரப்பூர்வ மூல வாசகமாகக் கருதப்படுகிறது"),
                ("The original regional language text passed by the Legislature", "சட்டமன்றத்தால் நிறைவேற்றப்பட்ட அசல் வட்டார மொழி வாசகம்"),
                ("The Hindi translation prepared by the Central Translation Bureau", "மத்திய மொழிபெயர்ப்பு பணியகத்தால் தயாரிக்கப்பட்ட இந்தி மொழிபெயர்ப்பு"),
                ("Neither text; the law is declared void for linguistic uncertainty", "இரண்டு வாசகங்களும் அல்ல; மொழி முரண்பாட்டிற்காக அந்தச் சட்டம் செல்லாததாக்கப்படும்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 348(3), the translation in the English language published under the authority of the Governor shall be deemed to be the authoritative text in the English language for that Act, and in superior courts, the English text prevails in case of divergence.",
            "exp_ta": "சரத்து 348(3)-ன் படி, ஆளுநரின் அதிகாரத்தின் கீழ் வெளியிடப்படும் ஆங்கில மொழிபெயர்ப்பு அந்தச் சட்டத்திற்கான அதிகாரப்பூர்வ மூல வாசகமாகக் கருதப்படும்; மேலும் உயர் நீதிமன்றங்கள் மற்றும் உச்ச நீதிமன்றத்தில் முரண்பாடு ஏற்படும் போது ஆங்கில வாசகமே மேலோங்கும்.",
            "why_a_en": "The constitutional deeming fiction in Article 348(3) makes the English translation the authoritative legal standard.",
            "why_a_ta": "சரத்து 348(3)-ன் அரசியலமைப்பு வாசகம் ஆங்கில மொழிபெயர்ப்பை அதிகாரப்பூர்வ சட்டத் தரநிலையாக ஆக்குகிறது.",
            "why_b_en": "The regional language text is subject to the authoritative English text requirement of Article 348(3).",
            "why_b_ta": "வட்டார மொழி வாசகம் சரத்து 348(3)-ன் அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்புத் தேவைக்கு உட்பட்டது.",
            "why_c_en": "Central Hindi translations have no constitutional standing over State legislative enactments.",
            "why_c_ta": "மாநில சட்டமன்ற மசோதாக்களின் மீது மத்திய இந்தி மொழிபெயர்ப்புகளுக்கு அரசியலமைப்பு மேலாதிக்கம் இல்லை.",
            "why_d_en": "Statutes are not invalidated for translation differences; the authoritative English text resolves the issue.",
            "why_d_ta": "மொழிபெயர்ப்பு வேறுபாடுகளுக்காகச் சட்டங்கள் செல்லாததாக்கப்படுவதில்லை; அதிகாரப்பூர்வ ஆங்கில உரையே சிக்கலைத் தீர்க்கிறது.",
            "tip_en": "Article 348(3): Regional Act text is valid domestically, but the ENGLISH translation is authoritative for judicial review.",
            "tip_ta": "சரத்து 348(3): வட்டார மொழிச் சட்டம் உள்ளூரில் செல்லுபடியாகும், ஆனால் நீதித்துறை மறுஆய்வுக்கு ஆங்கில மொழிபெயர்ப்பே மேலோங்கும்.",
            "fact_en": "In J.K. Jute Mills v. State of UP (1961), the Supreme Court affirmed the primacy of the Article 348(3) English text.",
            "fact_ta": "ஜே.கே. ஜூட் மில்ஸ் எதிர் உ.பி அரசு (1961) வழக்கில் உச்ச நீதிமன்றம் சரத்து 348(3) ஆங்கில உரையின் முதன்மையை உறுதிப்படுத்தியது."
        },
        # 4
        {
            "subtopic": "Article 349 Sunset and Desuetude",
            "stem_en": "Why has Article 349 of the Constitution of India become virtually redundant and inoperative in contemporary constitutional practice?",
            "stem_ta": "இந்திய அரசியலமைப்பின் சரத்து 349 சமகால அரசியலமைப்பு நடைமுறையில் நடைமுறையற்றதாகவும் செயலற்றதாகவும் மாறியிருப்பது ஏன்?",
            "options": [
                ("Because Article 349 applied strictly during the initial 15-year period from the commencement of the Constitution (1950–1965)", "ஏனெனில் சரத்து 349 அரசியலமைப்பு அமலுக்கு வந்த தொடக்க 15 ஆண்டு காலத்திற்கு (1950–1965) மட்டுமே திட்டவட்டமாகப் பொருந்தக்கூடியதாக இருந்தது"),
                ("Because it was formally repealed by the 44th Constitutional Amendment Act, 1978", "ஏனெனில் அது 1978-ன் 44-வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் முறையாக நீக்கப்பட்டது"),
                ("Because the Supreme Court struck it down in the Kesavananda Bharati case", "ஏனெனில் கேசவானந்த பாரதி வழக்கில் உச்ச நீதிமன்றம் அதனை ரத்து செய்துவிட்டது"),
                ("Because the President dissolved the Official Language Commission permanently", "ஏனெனில் குடியரசுத் தலைவர் அதிகாரப்பூர்வ மொழி ஆணையத்தை நிரந்தரமாகக் கலைத்துவிட்டார்")
            ],
            "correct_key": "A",
            "exp_en": "Article 349 opens with the words: 'During the period of fifteen years from the commencement of this Constitution, no Bill or amendment providing for the language... shall be introduced without the previous sanction of the President'. Once the 15-year period expired on January 25, 1965, Article 349 ceased to have prospective application.",
            "exp_ta": "சரத்து 349 'இந்த அரசியலமைப்பு அமலுக்கு வந்ததிலிருந்து பதினைந்து ஆண்டுகள் காலத்தில், குடியரசுத் தலைவரின் முன் அனுமதியின்றி மொழிக்கான எந்தவொரு மசோதாவும் அறிமுகப்படுத்தப்படக் கூடாது' என்ற வரிகளுடன் தொடங்குகிறது. 1965 ஜனவரி 25 அன்று 15 ஆண்டு காலம் காலாவதியானதால், சரத்து 349 தனது நடைமுறைப் பயன்பாட்டை இழந்துவிட்டது.",
            "why_a_en": "Article 349 had an inbuilt temporal limit of 15 years from January 26, 1950.",
            "why_a_ta": "சரத்து 349 1950 ஜனவரி 26 முதல் 15 ஆண்டுகள் என்ற உள்ளமைந்த கால வரம்பைக் கொண்டிருந்தது.",
            "why_b_en": "Article 349 remains on the statute book and has not been formally repealed.",
            "why_b_ta": "சரத்து 349 சட்டப் புத்தகத்தில் தொடர்ந்து உள்ளது, முறையாக நீக்கப்படவில்லை.",
            "why_c_en": "Kesavananda Bharati dealt with basic structure and Article 368, not Article 349.",
            "why_c_ta": "கேசவானந்த பாரதி அடிப்படை கட்டமைப்பு மற்றும் சரத்து 368 தொடர்பானது, சரத்து 349 அல்ல.",
            "why_d_en": "The Commission functions under Article 344 independently.",
            "why_d_ta": "ஆணையம் சரத்து 344-ன் கீழ் சுயாதீனமாகச் செயல்படுகிறது.",
            "tip_en": "Article 349: 15-year temporal restriction (1950-1965). Currently inoperative due to passage of time.",
            "tip_ta": "சரத்து 349: 15 ஆண்டு கால வரம்பு (1950-1965). காலாவதியானதன் காரணமாக தற்போது நடைமுறையில் இல்லை.",
            "fact_en": "Articles with built-in sunset clauses like Article 349 demonstrate the transitional architecture of Part XVII.",
            "fact_ta": "சரத்து 349 போன்ற குறிப்பிட்ட கால வரம்பு கொண்ட சரத்துகள் பகுதி XVII-ன் இடைக்கால வடிவமைப்பை விளக்குகின்றன."
        },
        # 5
        {
            "subtopic": "Eighth Schedule Language Families - Dravidian Core",
            "stem_en": "Which of the following statements is completely accurate regarding the representation of Dravidian languages in the Eighth Schedule?",
            "stem_ta": "எட்டாவது அட்டவணையில் திராவிட மொழிகளின் பிரதிநிதித்துவம் தொடர்பாக பின்வரும் கூற்றுகளில் எது முற்றிலும் சரியானது?",
            "options": [
                ("All four Dravidian languages currently in the Eighth Schedule (Tamil, Telugu, Kannada, Malayalam) were part of the original 14 languages in 1950 and all four have been declared Classical Languages", "தற்போது எட்டாவது அட்டவணையில் உள்ள நான்கு திராவிட மொழிகளும் (தமிழ், தெலுங்கு, கன்னடம், மலையாளம்) 1950-ல் அசல் 14 மொழிகளின் பகுதியாக இருந்தன மற்றும் நான்கும் செம்மொழிகளாக அறிவிக்கப்பட்டுள்ளன"),
                ("Malayalam was added to the Eighth Schedule only in 1992 by the 71st Amendment", "மலையாளம் 1992-ல் 71-வது திருத்தச் சட்டம் மூலமே எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது"),
                ("Telugu is the only Dravidian language not granted Classical status", "செம்மொழி அந்தஸ்து வழங்கப்படாத ஒரே திராவிட மொழி தெலுங்கு ஆகும்"),
                ("Tulu and Gondi were added as Dravidian languages by the 92nd Amendment in 2003", "துளு மற்றும் கோண்டி ஆகியவை 2003-ல் 92-வது திருத்தச் சட்டம் மூலம் திராவிட மொழிகளாகச் சேர்க்கப்பட்டன")
            ],
            "correct_key": "A",
            "exp_en": "Tamil, Telugu, Kannada, and Malayalam were all among the original 14 languages listed in the Eighth Schedule in 1950. Furthermore, all four have been declared Classical Languages: Tamil (2004), Telugu (2008), Kannada (2008), and Malayalam (2013).",
            "exp_ta": "தமிழ், தெலுங்கு, கன்னடம் மற்றும் மலையாளம் ஆகிய நான்கும் 1950-ல் எட்டாவது அட்டவணையில் இருந்த அசல் 14 மொழிகளிலும் இடம் பெற்றிருந்தன. மேலும், நான்கும் செம்மொழிகளாக அறிவிக்கப்பட்டுள்ளன: தமிழ் (2004), தெலுங்கு (2008), கன்னடம் (2008) மற்றும் மலையாளம் (2013).",
            "why_a_en": "All four major literary Dravidian languages share this dual distinction: original 1950 inclusion + Classical status.",
            "why_a_ta": "நான்கு முக்கிய திராவிட மொழிகளும் இந்த இரட்டைப் பெருமையைப் பகிர்ந்து கொள்கின்றன: அசல் 1950 சேர்க்கை + செம்மொழி அந்தஸ்து.",
            "why_b_en": "Malayalam was in the 1950 original list, not added in 1992.",
            "why_b_ta": "மலையாளம் 1950 அசல் பட்டியலில் இருந்தது, 1992-ல் சேர்க்கப்படவில்லை.",
            "why_c_en": "Telugu was declared a Classical Language in 2008.",
            "why_c_ta": "தெலுங்கு 2008-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_d_en": "Tulu and Gondi are not in the Eighth Schedule.",
            "why_d_ta": "துளு மற்றும் கோண்டி ஆகியவை எட்டாவது அட்டவணையில் இல்லை.",
            "tip_en": "Dravidian languages in 8th Schedule = exactly 4 (Tamil, Telugu, Kannada, Malayalam). All 4 are CLASSICAL.",
            "tip_ta": "8-வது அட்டவணையில் உள்ள திராவிட மொழிகள் = சரியாக 4 (தமிழ், தெலுங்கு, கன்னடம், மலையாளம்). நான்கும் செம்மொழிகள்.",
            "fact_en": "Non-literary Dravidian languages like Kurukh, Kui, and Tulu continue to seek inclusion.",
            "fact_ta": "குரூக், குய் மற்றும் துளு போன்ற பிற திராவிட மொழிகள் தொடர்ந்து சேர்க்கை கோரி வருகின்றன."
        },
        # 6
        {
            "subtopic": "Official Languages Rules 1976 - Rule 5 Mandatory Response",
            "stem_en": "Under Rule 5 of the Official Languages Rules, 1976, what is the mandatory requirement regarding communications received in Hindi by any Central Government office?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள், 1976-ன் விதி 5-ன் கீழ், எந்தவொரு மத்திய அரசு அலுவலகத்திற்கும் இந்தியில் பெறப்படும் தகவல்தொடர்புகள் குறித்த கட்டாயத் தேவை என்ன?",
            "options": [
                ("Notwithstanding anything contained in rules 3 and 4, communications from a Central Government office in reply to communications in Hindi shall be in Hindi", "விதிகள் 3 மற்றும் 4-ல் என்ன கூறப்பட்டிருப்பினும், இந்தியில் வரும் கடிதங்களுக்கு மத்திய அரசு அலுவலகத்திலிருந்து அனுப்பப்படும் பதில் கடிதம் கட்டாயமாக இந்தியில் மட்டுமே இருக்க வேண்டும்"),
                ("Replies must always be sent in English regardless of the incoming language", "வரும் மொழி எதுவாக இருந்தாலும் பதில்கள் எப்போதும் ஆங்கிலத்திலேயே அனுப்பப்பட வேண்டும்"),
                ("The office may ignore letters written in Hindi from non-Hindi states", "இந்தி பேசாத மாநிலங்களிலிருந்து இந்தியில் எழுதப்படும் கடிதங்களை அலுவலகம் நிராகரிக்கலாம்"),
                ("The recipient officer must be suspended if he does not know Hindi", "கடிதம் பெறும் அலுவலருக்கு இந்தி தெரியாவிட்டால் அவர் பணியிடை நீக்கம் செய்யப்பட வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Rule 5 of the Official Languages Rules, 1976 imposes an absolute requirement: Communications from a Central Government office in reply to communications in Hindi SHALL be in Hindi, irrespective of the region from which the communication was received.",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் விதி 5 ஒரு முழுமையான கட்டாயத்தை விதிக்கிறது: தகவல்தொடர்பு எந்த மண்டலத்திலிருந்து பெறப்பட்டிருந்தாலும், இந்தியில் வரும் கடிதங்களுக்கு மத்திய அரசு அலுவலகத்திலிருந்து அனுப்பப்படும் பதில் கடிதங்கள் கட்டாயமாக இந்தியில் இருக்க வேண்டும்.",
            "why_a_en": "Rule 5 mandates that any letter written in Hindi to a Central office must receive a reply in Hindi.",
            "why_a_ta": "விதி 5 மத்திய அலுவலகத்திற்கு இந்தியில் எழுதப்படும் எந்தவொரு கடிதத்திற்கும் பதிலளிக்கப்படும் கடிதம் இந்தியில் இருக்க வேண்டும் எனக் கட்டாயமாக்குகிறது.",
            "why_b_en": "English is not allowed as sole reply to a Hindi incoming letter under Rule 5.",
            "why_b_ta": "விதி 5-ன் கீழ் இந்திக் கடிதத்திற்கு ஆங்கிலத்தில் மட்டுமே பதிலளிப்பது அனுமதிக்கப்படாது.",
            "why_c_en": "Ignoring citizen letters is a dereliction of official duty.",
            "why_c_ta": "குடிமக்களின் கடிதங்களைப் புறக்கணிப்பது அலுவல் கடமை மீறலாகும்.",
            "why_d_en": "Lack of Hindi proficiency is not a ground for suspension.",
            "why_d_ta": "இந்தி புலமையின்மை என்பது இடைநீக்கத்திற்கான அடிப்படை அல்ல.",
            "tip_en": "Rule 5: Reply to Hindi communication MUST be in Hindi (Golden Rule of Official Language correspondence).",
            "tip_ta": "விதி 5: இந்தியில் வரும் கடிதத்திற்கான பதில் கட்டாயமாக இந்தியில் இருக்க வேண்டும்.",
            "fact_en": "This ensures that Hindi-speaking citizens do not receive replies in a language they may not understand.",
            "fact_ta": "இது இந்தி பேசும் குடிமக்கள் தங்களுக்குப் புரியாத மொழியில் பதில்களைப் பெறுவதைத் தடுக்கிறது."
        },
        # 7
        {
            "subtopic": "Official Languages Rules 1976 - Rule 8 Noting in Files",
            "stem_en": "What fundamental protection does Rule 8(1) of the Official Languages Rules, 1976 provide to an employee in a Central Government office regarding noting and drafting on files?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள், 1976-ன் விதி 8(1), கோப்புகளில் குறிப்புகள் மற்றும் வரைவுகள் எழுதுவது தொடர்பாக மத்திய அரசு அலுவலக ஊழியர் ஒருவருக்கு என்ன அடிப்படைப் பாதுகாப்பை வழங்குகிறது?",
            "options": [
                ("An employee may record a note or minute on a file in Hindi or in English without being himself required to furnish a translation thereof in the other language", "ஒரு ஊழியர் கோப்பில் தனது குறிப்பை இந்தி அல்லது ஆங்கிலத்தில் எழுதலாம்; அதற்காக அவர் மற்றொரு மொழியில் மொழிபெயர்ப்பை வழங்க வேண்டும் என்று கட்டாயப்படுத்தப்படக் கூடாது"),
                ("All employees must write notes in Devanagari Hindi exclusively", "அனைத்து ஊழியர்களும் கட்டாயமாக தேவநாகரி இந்தியில் மட்டுமே குறிப்புகளை எழுத வேண்டும்"),
                ("Non-Hindi employees must pay for their own official translation services", "இந்தி பேசாத ஊழியர்கள் தங்களது சொந்த செலவில் அதிகாரப்பூர்வ மொழிபெயர்ப்பு சேவைகளைப் பெற வேண்டும்"),
                ("Noting in English is strictly prohibited in all Central ministries", "அனைத்து மத்திய அமைச்சகங்களிலும் ஆங்கிலத்தில் குறிப்பு எழுதுவது முற்றிலுமாகத் தடை செய்யப்பட்டுள்ளது")
            ],
            "correct_key": "A",
            "exp_en": "Rule 8(1) provides that an employee may record a note or minute on a file in Hindi or in English without being himself required to furnish a translation thereof in the other language, protecting staff from translation burdens.",
            "exp_ta": "விதி 8(1)-ன் படி, ஓர் ஊழியர் ஒரு கோப்பில் இந்தி அல்லது ஆங்கிலத்தில் குறிப்பை எழுதலாம்; மேலும் அவர் மற்றொரு மொழியில் அதன் மொழிபெயர்ப்பை வழங்க வேண்டும் என்று கட்டாயப்படுத்தப்படக் கூடாது, இது ஊழியர்களை மொழிபெயர்ப்புச் சுமையிலிருந்து பாதுகாக்கிறது.",
            "why_a_en": "Rule 8(1) enshrines the liberty of the employee to use either Hindi or English without translating it personally.",
            "why_a_ta": "விதி 8(1) ஊழியர் தானே மொழிபெயர்க்க வேண்டிய கட்டாயமின்றி இந்தி அல்லது ஆங்கிலத்தைப் பயன்படுத்தும் உரிமையை உறுதி செய்கிறது.",
            "why_b_en": "Devanagari Hindi is not the exclusive compulsory noting language.",
            "why_b_ta": "தேவநாகரி இந்தி மட்டுமே கட்டாயக் குறிப்பு மொழி அல்ல.",
            "why_c_en": "Translation services are provided by the government through the official language cell, never at employee cost.",
            "why_c_ta": "மொழிபெயர்ப்பு சேவைகள் அரசு சார்பில் வழங்கப்படுகின்றன, ஊழியரின் சொந்த செலவில் அல்ல.",
            "why_d_en": "Noting in English remains fully lawful under Rule 8.",
            "why_d_ta": "விதி 8-ன் கீழ் ஆங்கிலத்தில் குறிப்பு எழுதுவது முற்றிலும் சட்டப்பூர்வமானது.",
            "tip_en": "Rule 8(1): Employee can note in Hindi OR English -> CANNOT be forced to provide a translation.",
            "tip_ta": "விதி 8(1): ஊழியர் இந்தி அல்லது ஆங்கிலத்தில் குறிப்பு எழுதலாம் -> மொழிபெயர்ப்பு வழங்கக் கட்டாயப்படுத்த முடியாது.",
            "fact_en": "Rule 8(2) prohibits penalizing or placing an employee at a disadvantage solely on language grounds.",
            "fact_ta": "விதி 8(2) மொழி அடிப்படையில் மட்டுமே ஓர் ஊழியரைப் பாதிப்பிற்குள்ளாக்குவதைத் தடை செய்கிறது."
        },
        # 8
        {
            "subtopic": "Proficiency vs Working Knowledge in Hindi",
            "stem_en": "Under Rule 9 and Rule 10 of the Official Languages Rules, 1976, what is the key distinction between an employee having 'proficiency in Hindi' and having 'working knowledge of Hindi'?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள், 1976-ன் விதி 9 மற்றும் விதி 10-ன் கீழ், ஓர் ஊழியர் 'இந்தியில் புலமை பெற்றவர்' என்பதற்கும் 'இந்தியில் பணி அறிவு கொண்டவர்' என்பதற்கும் இடையிலான முக்கிய வேறுபாடு என்ன?",
            "options": [
                ("Proficiency requires holding a degree/matriculation with Hindi medium or passing a declared high exam, whereas working knowledge requires passing matriculation with Hindi as a subject or passing Pragya exam", "புலமை என்பது இந்தி பயிற்றுமொழியில் பட்டம்/பத்தாம் வகுப்பு முடித்திருப்பது அல்லது குறிப்பிட்ட உயர் தேர்வில் தேர்ச்சி பெற்றிருப்பதைக் குறிக்கிறது; பணி அறிவு என்பது இந்தியை ஒரு பாடமாக எடுத்து பத்தாம் வகுப்பு முடித்திருப்பது அல்லது பிரக்யா தேர்வில் தேர்ச்சி பெற்றிருப்பதைக் குறிக்கிறது"),
                ("Proficiency applies only to IAS officers, while working knowledge applies to Group D staff", "புலமை என்பது ஐ.ஏ.எஸ் அதிகாரிகளுக்கு மட்டுமே பொருந்தும், பணி அறிவு என்பது குரூப் டி பணியாளர்களுக்குப் பொருந்தும்"),
                ("Working knowledge requires residing in Region A for at least 20 years", "பணி அறிவு என்பது மண்டலம் A-ல் குறைந்தபட்சம் 20 ஆண்டுகள் வசித்திருக்க வேண்டும்"),
                ("There is no statutory difference; both terms are legally synonymous", "எந்த சட்டப்பூர்வ வேறுபாடும் இல்லை; இரண்டு சொற்களும் சட்டப்படி ஒத்தவை")
            ],
            "correct_key": "A",
            "exp_en": "Under Rule 9, an employee is deemed to possess proficiency if they passed Matriculation/Degree with Hindi as medium of exam, or took Hindi as elective in degree. Under Rule 10, working knowledge is attained if they passed Matriculation with Hindi as a subject, passed the Pragya examination under the Hindi Teaching Scheme, or self-declared so.",
            "exp_ta": "விதி 9-ன் கீழ், ஒரு நபர் பத்தாம் வகுப்பு/பட்டப்படிப்பை இந்தி பயிற்றுமொழியில் முடித்திருந்தால் அல்லது பட்டத்தில் இந்தியை ஒரு விருப்பப்பாடமாக எடுத்திருந்தால் 'புலமை பெற்றவர்' ஆவார். விதி 10-ன் படி, பத்தாம் வகுப்பில் இந்தியை ஒரு பாடமாகப் படித்திருந்தால் அல்லது இந்தி கற்பித்தல் திட்டத்தின் கீழ் 'பிரக்யா' தேர்வில் தேர்ச்சி பெற்றிருந்தால் 'பணி அறிவு கொண்டவர்' ஆவார்.",
            "why_a_en": "Rule 9 establishes the higher threshold of educational medium; Rule 10 establishes functional working competency.",
            "why_a_ta": "விதி 9 பயிற்றுமொழி அடிப்படையிலான உயர் தகுதியையும், விதி 10 செயல்பாட்டுப் பணித் திறனையும் நிர்ணயிக்கிறது.",
            "why_b_en": "Rules 9 and 10 apply across all classes of Central Government employees.",
            "why_b_ta": "விதிகள் 9 மற்றும் 10 அனைத்து மத்திய அரசுப் பணியாளர்களுக்கும் பொருந்தும்.",
            "why_c_en": "Residential location does not determine proficiency under the Rules.",
            "why_c_ta": "வசிப்பிடம் விதிகளின் கீழ் புலமையைத் தீர்மானிப்பதில்லை.",
            "why_d_en": "The distinction is vital: staff with proficiency can be directed under Rule 8(4) to do specific work only in Hindi.",
            "why_d_ta": "இவ்வேறுபாடு முக்கியமானது: புலமை பெற்ற ஊழியர்களை விதி 8(4)-ன் கீழ் இந்தியில் மட்டுமே பணிகளைச் செய்யுமாறு பணிக்க முடியும்.",
            "tip_en": "Rule 9 = Proficiency (Degree/Matric in Hindi medium); Rule 10 = Working Knowledge (Hindi as subject / Pragya exam).",
            "tip_ta": "விதி 9 = புலமை (இந்தி வழிக் கல்வி); விதி 10 = பணி அறிவு (இந்தி ஒரு பாடம் / பிரக்யா தேர்வு).",
            "fact_en": "Under Rule 10(4), central offices where 80% of staff have working knowledge are notified in the Gazette.",
            "fact_ta": "விதி 10(4)-ன் கீழ், 80% ஊழியர்கள் பணி அறிவு பெற்றுள்ள மத்திய அலுவலகங்கள் அரசிதழில் அறிவிக்கப்படுகின்றன."
        },
        # 9
        {
            "subtopic": "Article 344(2) Mandatory Scope of Commission Duties",
            "stem_en": "Under Article 344(2), which of the following is NOT one of the constitutional duties of the Commission on Official Language?",
            "stem_ta": "சரத்து 344(2)-ன் கீழ், பின்வருவனவற்றில் எது அதிகாரப்பூர்வ மொழி ஆணையத்தின் அரசியலமைப்பு ரீதியான பணிகளில் ஒன்றாக இல்லாதது எது?",
            "options": [
                ("To determine the salaries and allowances of Supreme Court judges based on their linguistic proficiency", "நீதிபதிகளின் மொழிப் புலமையின் அடிப்படையில் உச்ச நீதிமன்ற நீதிபதிகளின் ஊதியம் மற்றும் படிகளைத் தீர்மானித்தல்"),
                ("The progressive use of the Hindi language for the official purposes of the Union", "ஒன்றியத்தின் அதிகாரப்பூர்வ பணிகளுக்காக இந்தி மொழியின் படிப்படியான பயன்பாடு"),
                ("Restrictions on the use of the English language for all or any of the official purposes of the Union", "ஒன்றியத்தின் அனைத்து அல்லது ஏதேனும் அதிகாரப்பூர்வ பணிகளுக்காக ஆங்கில மொழி பயன்பாட்டின் மீதான கட்டுப்பாடுகள்"),
                ("The language to be used for proceedings in the Supreme Court and every High Court", "உச்ச நீதிமன்றம் மற்றும் ஒவ்வொரு உயர் நீதிமன்ற நடவடிக்கைகளுக்கும் பயன்படுத்தப்பட வேண்டிய மொழி")
            ],
            "correct_key": "A",
            "exp_en": "Article 344(2) specifies five duties: (a) progressive use of Hindi, (b) restrictions on English, (c) language for Supreme Court and High Courts, (d) language of Bills, Acts, and rules, (e) any other matter referred by the President. Judicial salaries are governed by Article 125 and the Second Schedule, not language commissions.",
            "exp_ta": "சரத்து 344(2) ஐந்து பணிகளைக் குறிப்பிடுகிறது: (a) இந்தியின் படிப்படியான பயன்பாடு, (b) ஆங்கிலத்தின் மீதான கட்டுப்பாடுகள், (c) உச்ச மற்றும் உயர் நீதிமன்றங்களின் மொழி, (d) மசோதாக்கள், சட்டங்கள் மற்றும் விதிகளின் மொழி, (e) குடியரசுத் தலைவரால் குறிப்பிடப்படும் பிற விஷயங்கள். நீதிபதிகளின் ஊதியம் சரத்து 125 மற்றும் இரண்டாவது அட்டவணையால் ஆளப்படுகிறது.",
            "why_a_en": "Judicial salaries cannot be tied to language proficiency under the Constitution.",
            "why_a_ta": "அரசியலமைப்பின் கீழ் நீதிபதிகளின் ஊதியம் மொழிப் புலமையுடன் இணைக்கப்பட முடியாது.",
            "why_b_en": "Progressive use of Hindi is explicitly clause (a) of Article 344(2).",
            "why_b_ta": "இந்தியின் படிப்படியான பயன்பாடு சரத்து 344(2)-ன் பிரிவு (a)-ல் வெளிப்படையாக உள்ளது.",
            "why_c_en": "Restrictions on English is clause (b) of Article 344(2).",
            "why_c_ta": "ஆங்கிலத்தின் மீதான கட்டுப்பாடுகள் சரத்து 344(2)-ன் பிரிவு (b) ஆகும்.",
            "why_d_en": "Superior court languages is clause (c) of Article 344(2).",
            "why_d_ta": "உயர் நீதிமன்றங்களின் மொழி சரத்து 344(2)-ன் பிரிவு (c) ஆகும்.",
            "tip_en": "Article 344(2) 5 Duties: 1) Hindi progress, 2) English restriction, 3) Court language, 4) Law texts, 5) Referred matters.",
            "tip_ta": "சரத்து 344(2) 5 பணிகள்: 1) இந்தி வளர்ச்சி, 2) ஆங்கிலக் கட்டுப்பாடு, 3) நீதிமன்ற மொழி, 4) சட்ட வாசகங்கள், 5) பரிந்துரைக்கப்பட்டவை.",
            "fact_en": "The Commission must balance these duties against the advancement and non-Hindi interests in Article 344(3).",
            "fact_ta": "ஆணையம் இப்பணிகளை சரத்து 344(3)-ல் உள்ள நாட்டின் முன்னேற்றம் மற்றும் இந்தி பேசாத மக்களின் நலன்களுடன் சமப்படுத்த வேண்டும்."
        },
        # 10
        {
            "subtopic": "Tamil Nadu NCC Hindi Commands Abolition 1968",
            "stem_en": "In the landmark Tamil Nadu Assembly Resolution of January 23, 1968, what specific step was taken regarding the National Cadet Corps (NCC) in schools and colleges of Tamil Nadu?",
            "stem_ta": "1968 ஜனவரி 23 அன்று நிறைவேற்றப்பட்ட வரலாற்றுச் சிறப்புமிக்க தமிழ்நாடு சட்டமன்றத் தீர்மானத்தில், தமிழகப் பள்ளிகள் மற்றும் கல்லூரிகளில் உள்ள தேசிய மாணவர் படை (NCC) தொடர்பாக என்ன குறிப்பிட்ட நடவடிக்கை எடுக்கப்பட்டது?",
            "options": [
                ("The Assembly resolved that NCC training should be suspended until the Union Government agreed to replace Hindi words of command with Tamil or English", "மத்திய அரசு இந்தி கட்டளைச் சொற்களுக்குப் பதிலாக தமிழ் அல்லது ஆங்கிலத்தை ஏற்றுக்கொள்ளும் வரை என்.சி.சி பயிற்சி நிறுத்தி வைக்கப்பட வேண்டும் என சட்டமன்றம் தீர்மானித்தது"),
                ("NCC was permanently banned and all units were disbanded in Tamil Nadu", "என்.சி.சி நிரந்தரமாகத் தடை செய்யப்பட்டு அனைத்து பிரிவுகளும் தமிழ்நாட்டில் கலைக்கப்பட்டன"),
                ("NCC cadets were required to take all military exams in Sanskrit", "என்.சி.சி மாணவர்கள் அனைத்து ராணுவத் தேர்வுகளையும் சமஸ்கிருதத்தில் எழுத வேண்டும் எனக் கோரப்பட்டது"),
                ("NCC was handed over to private educational trusts", "என்.சி.சி தனியார் கல்வி அறக்கட்டளைகளிடம் ஒப்படைக்கப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "Clause 2 of the January 23, 1968 Tamil Nadu Assembly Resolution resolved that the National Cadet Corps (NCC) training in the State be suspended until the Central Government agreed to use Tamil or English words of command instead of Hindi.",
            "exp_ta": "1968 ஜனவரி 23 தமிழ்நாடு சட்டமன்றத் தீர்மானத்தின் பிரிவு 2, இந்தி கட்டளைச் சொற்களுக்குப் பதிலாக தமிழ் அல்லது ஆங்கிலத்தை மத்திய அரசு அனுமதிக்கும் வரை மாநிலத்தில் தேசிய மாணவர் படை (NCC) பயிற்சி நிறுத்தி வைக்கப்பட வேண்டும் எனத் தீர்மானித்தது.",
            "why_a_en": "The resolution specifically resisted Hindi commands in NCC, leading to temporary suspension of NCC in the State.",
            "why_a_ta": "இத்தீர்மானம் என்.சி.சி-யில் இந்தி கட்டளைகளை எதிர்த்தது, இது மாநிலத்தில் என்.சி.சி தற்காலிகமாக நிறுத்தப்பட வழிவகுத்தது.",
            "why_b_en": "NCC was not permanently banned; training resumed once English commands were retained/restored.",
            "why_b_ta": "என்.சி.சி நிரந்தரமாகத் தடை செய்யப்படவில்லை; ஆங்கிலக் கட்டளைகள் மீட்டெடுக்கப்பட்டவுடன் பயிற்சி மீண்டும் தொடங்கியது.",
            "why_c_en": "Sanskrit was never proposed for NCC commands.",
            "why_c_ta": "என்.சி.சி கட்டளைகளுக்கு சமஸ்கிருதம் ஒருபோதும் முன்மொழியப்படவில்லை.",
            "why_d_en": "NCC remains under the Ministry of Defence, not private trusts.",
            "why_d_ta": "என்.சி.சி பாதுகாப்பு அமைச்சகத்தின் கீழ் உள்ளது, தனியார் அறக்கட்டளைகள் கீழ் அல்ல.",
            "tip_en": "1968 Annadurai Resolution: 1) Two-Language Policy, 2) Abolition of Hindi in curriculum, 3) Suspension of NCC Hindi commands.",
            "tip_ta": "1968 அண்ணாதுரை தீர்மானம்: 1) இருமொழிக் கொள்கை, 2) பாடத்திட்டத்தில் இந்தி நீக்கம், 3) என்.சி.சி இந்தி கட்டளைகள் நிறுத்தம்.",
            "fact_en": "Chief Minister C.N. Annadurai famously declared: 'We are for all Indian languages, but against the hegemony of one language over others.'",
            "fact_ta": "முதலமைச்சர் சி.என். அண்ணாதுரை: 'நாங்கள் அனைத்து இந்திய மொழிகளுக்கும் ஆதரவானவர்கள், ஆனால் ஒரு மொழி மற்ற மொழிகளின் மீது ஆதிக்கம் செலுத்துவதற்கு எதிரானவர்கள்' என்றார்."
        },
        # 11
        {
            "subtopic": "Article 345 State Discretion on English",
            "stem_en": "Under the proviso to Article 345, until the Legislature of a State otherwise provides by law, what language is constitutionally authorized to be used for all official purposes of that State for which it was being used before?",
            "stem_ta": "சரத்து 345-ன் விதிவிலக்கின் கீழ், ஒரு மாநில சட்டமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக வகை செய்யும் வரை, அம்மாநிலத்தில் இதற்கு முன்னர் எந்த அதிகாரப்பூர்வ பணிகளுக்குப் பயன்படுத்தப்பட்டதோ அவற்றுக்குத் தொடர்ந்து பயன்படுத்த அரசியலமைப்பு ரீதியாக அங்கீகரிக்கப்பட்ட மொழி எது?",
            "options": [
                ("The English language", "ஆங்கில மொழி"),
                ("Hindi in Devanagari script exclusively", "தேவநாகரி வரிவடிவ இந்தி மட்டுமே"),
                ("The mother tongue of the Governor", "ஆளுநரின் தாய்மொழி"),
                ("Sanskrit", "சமஸ்கிருதம்")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 345 provides that until the Legislature of the State otherwise provides by law, the English language shall continue to be used for those official purposes within the State for which it was being used immediately before the commencement of this Constitution.",
            "exp_ta": "சரத்து 345-ன் விதிவிலக்கின் படி, மாநில சட்டமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக வகை செய்யும் வரை, அரசியலமைப்பு அமலுக்கு வருவதற்கு முன்பு எந்த அதிகாரப்பூர்வ பணிகளுக்கு ஆங்கிலம் பயன்படுத்தப்பட்டதோ அவற்றுக்கு ஆங்கில மொழியே தொடர்ந்து பயன்படுத்தப்படும்.",
            "why_a_en": "Article 345 proviso maintains seamless legal continuity by preserving English until the State Legislature enacts its own language law.",
            "why_a_ta": "சரத்து 345 விதிவிலக்கு மாநில சட்டமன்றம் தனது சொந்த மொழிச் சட்டத்தை இயற்றும் வரை ஆங்கிலத்தைப் பாதுகாப்பதன் மூலம் தடையற்ற சட்டத் தொடர்ச்சியைப் பராமரிக்கிறது.",
            "why_b_en": "Hindi does not automatically become the default language of non-Hindi States.",
            "why_b_ta": "இந்தி தானாகவே இந்தி பேசாத மாநிலங்களின் இயல்புநிலை மொழியாக மாறாது.",
            "why_c_en": "The personal mother tongue of the Governor is completely irrelevant.",
            "why_c_ta": "ஆளுநரின் தனிப்பட்ட தாய்மொழி முற்றிலும் தொடர்பற்றது.",
            "why_d_en": "Sanskrit was not the pre-1950 administrative language.",
            "why_d_ta": "1950-க்கு முந்தைய நிர்வாக மொழி சமஸ்கிருதம் அல்ல.",
            "tip_en": "Article 345 Proviso: Pre-1950 status quo of ENGLISH continues until the State passes its own Official Language Act.",
            "tip_ta": "சரத்து 345 விதிவிலக்கு: மாநிலம் தனது சொந்த மொழிச் சட்டத்தை இயற்றும் வரை 1950-க்கு முந்தைய ஆங்கிலத்தின் நிலையே தொடரும்.",
            "fact_en": "This prevented an administrative breakdown upon the adoption of the Constitution in 1950.",
            "fact_ta": "இது 1950-ல் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டபோது நிர்வாக முடக்கம் ஏற்படுவதைத் தடுத்தது."
        },
        # 12
        {
            "subtopic": "Languages of Eighth Schedule - Unofficial Languages Matrix",
            "stem_en": "Which of the following pairs contains TWO languages that are BOTH excluded from the Eighth Schedule of the Constitution of India?",
            "stem_ta": "பின்வரும் இணைகளில் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படாத இரண்டு மொழிகளைக் கொண்டுள்ள இணை எது?",
            "options": [
                ("Bhojpuri and Rajasthani", "போஜ்புரி மற்றும் ராஜஸ்தானி"),
                ("Bodo and Dogri", "போடோ மற்றும் டோக்ரி"),
                ("Manipuri and Nepali", "மணிப்பூரி மற்றும் நேபாளி"),
                ("Konkani and Maithili", "கொங்கணி மற்றும் மைதிலி")
            ],
            "correct_key": "A",
            "exp_en": "Both Bhojpuri and Rajasthani are excluded from the Eighth Schedule despite millions of speakers. In contrast, Bodo, Dogri, Manipuri, Nepali, Konkani, and Maithili are all included in the 22 scheduled languages.",
            "exp_ta": "கோடிக்கணக்கான மக்களால் பேசப்பட்டாலும் போஜ்புரி மற்றும் ராஜஸ்தானி ஆகிய இரண்டுமே எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை. மாறாக, போடோ, டோக்ரி, மணிப்பூரி, நேபாளி, கொங்கணி மற்றும் மைதிலி ஆகியவை 22 அட்டவணை மொழிகளிலும் சேர்க்கப்பட்டுள்ளன.",
            "why_a_en": "Bhojpuri and Rajasthani are both non-scheduled languages seeking inclusion.",
            "why_a_ta": "போஜ்புரி மற்றும் ராஜஸ்தானி ஆகிய இரண்டும் சேர்க்கை கோரும் அட்டவணையில் இல்லாத மொழிகளாகும்.",
            "why_b_en": "Bodo and Dogri were added in 2003 by the 92nd CAA.",
            "why_b_ta": "போடோ மற்றும் டோக்ரி 2003-ல் 92-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டன.",
            "why_c_en": "Manipuri and Nepali were added in 1992 by the 71st CAA.",
            "why_c_ta": "மணிப்பூரி மற்றும் நேபாளி 1992-ல் 71-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டன.",
            "why_d_en": "Konkani (1992) and Maithili (2003) are both Eighth Schedule languages.",
            "why_d_ta": "கொங்கணி (1992) மற்றும் மைதிலி (2003) இரண்டுமே எட்டாவது அட்டவணை மொழிகளாகும்.",
            "tip_en": "Non-scheduled Languages: Bhojpuri, Rajasthani, Tulu, Khasi, Garo, Mizo, Kokborok, Bhili.",
            "tip_ta": "அட்டவணையில் இல்லாத மொழிகள்: போஜ்புரி, ராஜஸ்தானி, துளு, காசி, காரோ, மிசோ, கோக்பொரோக், பிலி.",
            "fact_en": "Bhojpuri is an official language of Mauritius and Fiji, but not an Eighth Schedule language in India.",
            "fact_ta": "போஜ்புரி மொரிஷியஸ் மற்றும் பிஜியில் அங்கீகரிக்கப்பட்ட மொழி, ஆனால் இந்தியாவில் எட்டாவது அட்டவணையில் இல்லை."
        },
        # 13
        {
            "subtopic": "Section 3(4) Official Languages Act - No Discrimination",
            "stem_en": "What non-discrimination principle is enacted in Section 3(4) of the Official Languages Act, 1963 regarding Central Government employees?",
            "stem_ta": "மத்திய அரசு ஊழியர்கள் தொடர்பாக அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 3(4)-ல் இயற்றப்பட்டுள்ள பாகுபாடற்ற கொள்கை என்ன?",
            "options": [
                ("Staff who have not attained proficiency in Hindi shall not be discriminated against in terms of employment, career progression, or conditions of service", "இந்தியில் புலமை பெறாத பணியாளர்கள் வேலைவாய்ப்பு, பணி உயர்வு அல்லது சேவை நிபந்தனைகளில் பாகுபாட்டிற்கு உள்ளாக்கப்படக் கூடாது"),
                ("Only employees knowing both Hindi and Sanskrit shall be eligible for promotions", "இந்தி மற்றும் சமஸ்கிருதம் ஆகிய இரண்டையும் அறிந்த ஊழியர்கள் மட்டுமே பதவி உயர்வுக்குத் தகுதியானவர்கள்"),
                ("Employees who do not learn Hindi within two years shall have their salary deducted", "இரண்டு ஆண்டுகளுக்குள் இந்தி கற்காத ஊழியர்களின் ஊதியம் பிடித்தம் செய்யப்படும்"),
                ("All central staff must write examinations in Hindi to clear probation", "பயிற்சிக் காலத்தை முடிக்க அனைத்து மத்திய ஊழியர்களும் இந்தியில் தேர்வுகளை எழுத வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Section 3(4) explicitly provides that in framing rules under the Act, the Central Government shall ensure that staff having knowledge of only one language (Hindi or English) are not placed at a disadvantage on that ground alone.",
            "exp_ta": "பிரிவு 3(4) சட்டத்தின் கீழ் விதிகளை உருவாக்கும் போது, ஒரே ஒரு மொழியை (இந்தி அல்லது ஆங்கிலம்) மட்டுமே அறிந்த ஊழியர்கள் அந்த காரணத்திற்காக மட்டுமே பாதகமான நிலைக்கு ஆளாகாமல் இருப்பதை மத்திய அரசு உறுதி செய்ய வேண்டும் என்று வெளிப்படையாகக் கூறுகிறது.",
            "why_a_en": "Section 3(4) guarantees non-discrimination against non-Hindi speaking employees in promotions and conditions of service.",
            "why_a_ta": "பிரிவு 3(4) பதவி உயர்வு மற்றும் பணி நிலைமைகளில் இந்தி பேசாத ஊழியர்களுக்கு எதிரான பாகுபாடு காட்டப்படாது என்பதை உத்தரவாதம் செய்கிறது.",
            "why_b_en": "Sanskrit knowledge has never been a condition for promotion in Central services.",
            "why_b_ta": "மத்தியப் பணிகளில் பதவி உயர்வுக்கு சமஸ்கிருத அறிவு ஒருபோதும் நிபந்தனையாக இருந்ததில்லை.",
            "why_c_en": "Salary deductions for language grounds are unlawful and contrary to service rules.",
            "why_c_ta": "மொழி காரணங்களுக்காக ஊதியப் பிடித்தம் செய்வது சட்டவிரோதமானது மற்றும் பணி விதிகளுக்கு முரணானது.",
            "why_d_en": "Probation clearance does not require mandatory Hindi exam passing for non-Hindi cadres.",
            "why_d_ta": "இந்தி பேசாத பணியாளர்களுக்குப் பயிற்சிக் காலத்தை முடிக்க கட்டாய இந்தித் தேர்வுத் தேர்ச்சி தேவையில்லை.",
            "tip_en": "Section 3(4): Protection against language-based discrimination in central government service.",
            "tip_ta": "பிரிவு 3(4): மத்திய அரசுப் பணியில் மொழி அடிப்படையிலான பாகுபாட்டிற்கு எதிரான பாதுகாப்பு.",
            "fact_en": "This statutory shield prevents the backdoor imposition of Hindi as a barrier to bureaucratic promotions.",
            "fact_ta": "இந்த சட்டப்பூர்வ கவசம் இந்தியை அதிகாரத்துவ பதவி உயர்வுகளுக்குத் தடையாக மாற்றுவதைத் தடுக்கிறது."
        },
        # 14
        {
            "subtopic": "Languages of Eighth Schedule - Classical Status 2024 Additions",
            "stem_en": "Which of the following classical languages declared in October 2024 is the state official language of West Bengal?",
            "stem_ta": "அக்டோபர் 2024-ல் செம்மொழியாக அறிவிக்கப்பட்ட மொழிகளில் மேற்கு வங்காளத்தின் மாநில அதிகாரப்பூர்வ மொழி எது?",
            "options": [
                ("Bengali", "பெங்காலி"),
                ("Assamese", "அசாமி"),
                ("Marathi", "மராத்தி"),
                ("Prakrit", "பிராகிருதம்")
            ],
            "correct_key": "A",
            "exp_en": "Bengali (Bangla), the state official language of West Bengal and Tripura and the second most spoken language in India, was declared a Classical Language on October 3, 2024.",
            "exp_ta": "மேற்கு வங்காளம் மற்றும் திரிபுராவின் மாநில அதிகாரப்பூர்வ மொழியாகவும், இந்தியாவில் இரண்டாவது அதிகமாகப் பேசப்படும் மொழியாகவும் உள்ள பெங்காலி (பங்களா), 2024 அக்டோபர் 3 அன்று செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_a_en": "Bengali is the official language of West Bengal and one of the 5 newly designated classical languages.",
            "why_a_ta": "பெங்காலி மேற்கு வங்காளத்தின் அதிகாரப்பூர்வ மொழி மற்றும் புதிதாக அறிவிக்கப்பட்ட 5 செம்மொழிகளில் ஒன்றாகும்.",
            "why_b_en": "Assamese is the official language of Assam, not West Bengal.",
            "why_b_ta": "அசாமி அசாமின் அதிகாரப்பூர்வ மொழி, மேற்கு வங்காளத்திற்குரியது அல்ல.",
            "why_c_en": "Marathi is the official language of Maharashtra.",
            "why_c_ta": "மராத்தி மகாராஷ்டிராவின் அதிகாரப்பூர்வ மொழி.",
            "why_d_en": "Prakrit is an ancient classical language without state official status today.",
            "why_d_ta": "பிராகிருதம் இன்று எந்த மாநிலத்திலும் அதிகாரப்பூர்வ அந்தஸ்து இல்லாத ஒரு பண்டைய செவ்வியல் மொழியாகும்.",
            "tip_en": "Bengali = 2nd most spoken language in India (after Hindi) + Classical Language since Oct 2024.",
            "tip_ta": "பெங்காலி = இந்தியாவில் 2-வது அதிகமாகப் பேசப்படும் மொழி (இந்திக்கு அடுத்தபடியாக) + அக். 2024 முதல் செம்மொழி.",
            "fact_en": "Rabindranath Tagore won the Nobel Prize in Literature in 1913 for Gitanjali, composed originally in Bengali.",
            "fact_ta": "ரவீந்திரநாத் தாகூர் 1913-ல் முதன்முதலில் பெங்காலியில் இயற்றப்பட்ட கீதாஞ்சலிக்காக இலக்கியத்திற்கான நோபல் பரிசை வென்றார்."
        },
        # 15
        {
            "subtopic": "Official Languages Act Section 5 Authorized Hindi Translations",
            "stem_en": "Under Section 5(1) of the Official Languages Act, 1963, a translation in Hindi published under the authority of the President in the Official Gazette of any Central Act or Ordinance shall be deemed to be what?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 5(1)-ன் கீழ், எந்தவொரு மத்தியச் சட்டம் அல்லது அவசரச் சட்டத்தின் அதிகாரப்பூர்வ அரசிதழில் குடியரசுத் தலைவரின் அதிகாரத்தின் கீழ் வெளியிடப்படும் இந்தி மொழிபெயர்ப்பு என்னவாகக் கருதப்படும்?",
            "options": [
                ("The authoritative text thereof in Hindi", "அதன் அதிகாரப்பூர்வ இந்தி மூல வாசகம்"),
                ("The superior text overriding the original English Act", "அசல் ஆங்கிலச் சட்டத்தை மேலோங்கும் உயர் வாசகம்"),
                ("An informal administrative draft with no evidentiary value", "சான்றாதார மதிப்பு இல்லாத ஒரு முறைசாரா நிர்வாக வரைவு"),
                ("A document requiring unanimous ratification by all State Governors", "அனைத்து மாநில ஆளுநர்களின் ஒருமனதான ஒப்புதல் தேவைப்படும் ஓர் ஆவணம்")
            ],
            "correct_key": "A",
            "exp_en": "Section 5(1) provides that a translation in Hindi published under the authority of the President in the Official Gazette of any Central Act, Ordinance, or statutory rule shall be deemed to be the authoritative text thereof in Hindi.",
            "exp_ta": "பிரிவு 5(1)-ன் படி, எந்தவொரு மத்தியச் சட்டம், அவசரச் சட்டம் அல்லது சட்டப்பூர்வ விதியின் அதிகாரப்பூர்வ அரசிதழில் குடியரசுத் தலைவரின் அதிகாரத்தின் கீழ் வெளியிடப்படும் இந்தி மொழிபெயர்ப்பு, அதன் அதிகாரப்பூர்வ இந்தி மூல வாசகமாகக் கருதப்படும்.",
            "why_a_en": "Section 5(1) gives legal evidentiary status to the authorized Hindi translation.",
            "why_a_ta": "பிரிவு 5(1) அங்கீகரிக்கப்பட்ட இந்தி மொழிபெயர்ப்பிற்கு சட்டப்பூர்வ சான்றாதார அந்தஸ்தை வழங்குகிறது.",
            "why_b_en": "The Hindi text does not override the English text; Article 348(1)(b) English text remains supreme in case of doubt.",
            "why_b_ta": "இந்தி உரை ஆங்கில உரையை மேலோங்காது; முரண்பாட்டின் போது சரத்து 348(1)(b) ஆங்கில உரையே மேலோங்கும்.",
            "why_c_en": "It has full legal evidentiary value in courts.",
            "why_c_ta": "இது நீதிமன்றங்களில் முழு சட்டப்பூர்வ சான்றாதார மதிப்பைக் கொண்டுள்ளது.",
            "why_d_en": "State Governors' ratification is not required for Central Act translations.",
            "why_d_ta": "மத்தியச் சட்ட மொழிபெயர்ப்புகளுக்கு மாநில ஆளுநர்களின் ஒப்புதல் தேவையில்லை.",
            "tip_en": "Section 5(1): President publishes authorized Hindi text of Central Acts.",
            "tip_ta": "பிரிவு 5(1): குடியரசுத் தலைவர் மத்தியச் சட்டங்களின் அங்கீகரிக்கப்பட்ட இந்தி உரையை வெளியிடுகிறார்.",
            "fact_en": "Section 5(2) similarly applies to Bills introduced in Parliament in English, requiring a Hindi translation.",
            "fact_ta": "பிரிவு 5(2) நாடாளுமன்றத்தில் ஆங்கிலத்தில் அறிமுகப்படுத்தப்படும் மசோதாக்களுக்கும் இவ்வாறே இந்தி மொழிபெயர்ப்பைக் கோருகிறது."
        },
        # 16
        {
            "subtopic": "Article 344(4) Committee Reports to President",
            "stem_en": "Under Article 344(5), what is the specific duty of the 30-member Parliamentary Committee on Official Language?",
            "stem_ta": "சரத்து 344(5)-ன் கீழ், அதிகாரப்பூர்வ மொழிக்கான 30 உறுப்பினர்களைக் கொண்ட நாடாளுமன்றக் குழுவின் குறிப்பிட்ட பணி என்ன?",
            "options": [
                ("To examine the recommendations of the Commission constituted under clause (1) and to report to the President their opinion thereon", "பிரிவு (1)-ன் கீழ் அமைக்கப்பட்ட ஆணையத்தின் பரிந்துரைகளை ஆய்வு செய்து, அவற்றின் மீதான தங்களது கருத்தைக் குடியரசுத் தலைவரிடம் அறிக்கையாகச் சமர்ப்பித்தல்"),
                ("To draft criminal laws for violating official language guidelines", "அதிகாரப்பூர்வ மொழி வழிகாட்டுதல்களை மீறுபவர்களுக்கான குற்றவியல் சட்டங்களை வரைதல்"),
                ("To veto any legislation passed by State Assemblies on language", "மொழி தொடர்பாக மாநில சட்டமன்றங்கள் நிறைவேற்றும் எந்தவொரு சட்டத்தையும் ரத்து செய்தல்"),
                ("To inspect High Courts and dismiss judges who refuse to write judgments in Hindi", "உயர் நீதிமன்றங்களை ஆய்வு செய்து, இந்தியில் தீர்ப்புகளை எழுத மறுக்கும் நீதிபதிகளைப் பதவி நீக்கம் செய்தல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 344(5) explicitly states: 'It shall be the duty of the Committee to examine the recommendations of the Commission constituted under clause (1) and to report to the President their opinion thereon.'",
            "exp_ta": "சரத்து 344(5) வெளிப்படையாகக் கூறுகிறது: 'பிரிவு (1)-ன் கீழ் அமைக்கப்பட்ட ஆணையத்தின் பரிந்துரைகளை ஆய்வு செய்து, அவற்றின் மீதான தங்களது கருத்தைக் குடியரசுத் தலைவரிடம் அறிக்கையாகச் சமர்ப்பிப்பது அக்குழுவின் கடமையாகும்.'",
            "why_a_en": "Article 344(5) defines the precise constitutional duty of the Parliamentary Committee.",
            "why_a_ta": "சரத்து 344(5) நாடாளுமன்றக் குழுவின் துல்லியமான அரசியலமைப்புக் கடமையை வரையறுக்கிறது.",
            "why_b_en": "The Committee has no penal drafting or legislative enactment power.",
            "why_b_ta": "குழுவிற்கு குற்றவியல் சட்ட வரைவு அல்லது சட்டமியற்றும் அதிகாரம் இல்லை.",
            "why_c_en": "State legislative veto belongs to the Governor and President under Articles 200 and 201.",
            "why_c_ta": "மாநில சட்டமன்ற மசோதா மீதான அதிகாரம் சரத்துகள் 200 மற்றும் 201-ன் கீழ் ஆளுநர் மற்றும் குடியரசுத் தலைவரிடம் உள்ளது.",
            "why_d_en": "High Court judges can only be removed under Article 217/124(4) by parliamentary address, not by committees.",
            "why_d_ta": "உயர் நீதிமன்ற நீதிபதிகளை நாடாளுமன்றத் தீர்மானம் மூலம் மட்டுமே நீக்க முடியும், குழுக்களால் அல்ல.",
            "tip_en": "Article 344(5): Parliamentary Committee examines Commission's report -> Reports opinion to President.",
            "tip_ta": "சரத்து 344(5): நாடாளுமன்றக் குழு ஆணையத்தின் அறிக்கையை ஆய்வு செய்கிறது -> தனது கருத்தைக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கிறது.",
            "fact_en": "Under Article 344(6), the President issues binding directions based on this Parliamentary Committee report.",
            "fact_ta": "சரத்து 344(6)-ன் கீழ், குடியரசுத் தலைவர் இந்த நாடாளுமன்றக் குழு அறிக்கையின் அடிப்படையில் உத்தரவுகளைப் பிறப்பிக்கிறார்."
        },
        # 17
        {
            "subtopic": "Languages of Eighth Schedule - Kashmiri Script",
            "stem_en": "In which script is the Kashmiri language officially written in Jammu and Kashmir?",
            "stem_ta": "ஜம்மு மற்றும் காஷ்மீரில் காஷ்மீரி மொழி அதிகாரப்பூர்வமாக எந்த வரிவடிவத்தில் எழுதப்படுகிறது?",
            "options": [
                ("Perso-Arabic script (Nastaliq style)", "பாரசீக-அரபு வரிவடிவம் (நஸ்தலீக் பாணி)"),
                ("Sharada script exclusively", "சாரதா வரிவடிவம் மட்டுமே"),
                ("Devanagari script exclusively", "தேவநாகரி வரிவடிவம் மட்டுமே"),
                ("Roman script exclusively", "ரோமன் வரிவடிவம் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "The Kashmiri language is officially written in the Perso-Arabic script in the Nastaliq style by the Jammu and Kashmir government, although historically it was written in the ancient Sharada script and some groups use Devanagari.",
            "exp_ta": "காஷ்மீரி மொழி வரலாற்று ரீதியாக பண்டைய சாரதா வரிவடிவத்தில் எழுதப்பட்டிருந்தாலும், ஜம்மு-காஷ்மீர் அரசால் அதிகாரப்பூர்வமாக நஸ்தலீக் பாணியிலான பாரசீக-அரபு வரிவடிவத்திலேயே எழுதப்படுகிறது.",
            "why_a_en": "Perso-Arabic Nastaliq is the officially recognized script for Kashmiri administrative and educational use.",
            "why_a_ta": "பாரசீக-அரபு நஸ்தலீக் என்பது காஷ்மீரி நிர்வாக மற்றும் கல்விப் பயன்பாட்டிற்கான அதிகாரப்பூர்வ வரிவடிவமாகும்.",
            "why_b_en": "Sharada is the ancient ancestral script of Kashmiri, now mostly obsolete in daily administration.",
            "why_b_ta": "சாரதா காஷ்மீரியின் பண்டைய வரலாற்று வரிவடிவம், தற்போது தினசரி நிர்வாகத்தில் புழக்கத்தில் இல்லை.",
            "why_c_en": "Devanagari is used by Kashmiri Pandits, but is not the sole official state standard.",
            "why_c_ta": "தேவநாகரி காஷ்மீரி பண்டிட்டுகளால் பயன்படுத்தப்படுகிறது, ஆனால் ஒரே அதிகாரப்பூர்வ மாநில வடிவம் அல்ல.",
            "why_d_en": "Roman script is not the official standard for Kashmiri.",
            "why_d_ta": "ரோமன் வரிவடிவம் காஷ்மீரிக்கான அதிகாரப்பூர்வ வடிவம் அல்ல.",
            "tip_en": "Kashmiri: Historically = Sharada; Officially today = Perso-Arabic (Nastaliq).",
            "tip_ta": "காஷ்மீரி: வரலாற்று ரீதியாக = சாரதா; தற்போது அதிகாரப்பூர்வமாக = பாரசீக-அரபு (நஸ்தலீக்).",
            "fact_en": "Kashmiri is one of the five official languages of the UT of J&K since 2020.",
            "fact_ta": "2020 முதல் ஜம்மு-காஷ்மீர் ஒன்றியப் பகுதியின் ஐந்து அதிகாரப்பூர்வ மொழிகளில் காஷ்மீரியும் ஒன்றாகும்."
        },
        # 18
        {
            "subtopic": "Sindhi Addition - 21st Amendment Historical Context",
            "stem_en": "Why was Sindhi added to the Eighth Schedule in 1967 despite having no distinct contiguous territorial state in India?",
            "stem_ta": "இந்தியாவில் தனக்கென ஒரு தொடர்ச்சியான நிலப்பரப்பு மாநிலம் இல்லாத போதிலும், 1967-ல் எட்டாவது அட்டவணையில் சிந்தி மொழி சேர்க்கப்பட்டது ஏன்?",
            "options": [
                ("To protect and preserve the cultural and literary identity of the substantial partition-displaced Sindhi population residing across India", "இந்தியா முழுவதும் வசிக்கும் கணிசமான இந்தியப் பிரிவினை இடம்பெயர்ந்த சிந்தி மக்களின் கலாச்சார மற்றும் இலக்கிய அடையாளத்தைப் பாதுகாப்பதற்காக"),
                ("Because Sindh was annexed by India through military action in 1967", "1967-ல் ராணுவ நடவடிக்கை மூலம் சிந்து பகுதியை இந்தியா இணைத்துக் கொண்டதால்"),
                ("Because the United Nations passed a binding resolution requiring its inclusion", "ஐக்கிய நாடுகள் சபை அதைச் சேர்க்கக் கோரி ஒரு கட்டாயத் தீர்மானத்தை நிறைவேற்றியதால்"),
                ("Because Sindhi was declared the official language of Gujarat and Maharashtra", "சிந்தி குஜராத் மற்றும் மகாராஷ்டிராவின் அதிகாரப்பூர்வ மொழியாக அறிவிக்கப்பட்டதால்")
            ],
            "correct_key": "A",
            "exp_en": "Following the 1947 Partition, millions of Sindhi Hindus migrated to India and dispersed across Gujarat, Maharashtra, Rajasthan, and MP. In 1967, Parliament passed the 21st Amendment to give institutional recognition and cultural preservation to this dispersed linguistic community.",
            "exp_ta": "1947 பிரிவினையைத் தொடர்ந்து, லட்சக்கணக்கான சிந்தி மக்கள் இந்தியாவுக்கு இடம்பெயர்ந்து குஜராத், மகாராஷ்டிரா, ராஜஸ்தான் மற்றும் ம.பியில் பரவினர். 1967-ல், இந்த இடம்பெயர்ந்த மொழிச் சமூகத்திற்கு நிறுவன அங்கீகாரம் மற்றும் கலாச்சாரப் பாதுகாப்பை வழங்க நாடாளுமன்றம் 21-வது திருத்தச் சட்டத்தை நிறைவேற்றியது.",
            "why_a_en": "Sindhi inclusion recognized a diaspora linguistic community without a territorial homeland within the Union.",
            "why_a_ta": "சிந்திச் சேர்க்கையானது ஒன்றியத்திற்குள் ஒரு பிராந்தியத் தாயகம் இல்லாத புலம்பெயர் மொழிச் சமூகத்தை அங்கீகரித்தது.",
            "why_b_en": "Sindh was never annexed by India; it remains a province of Pakistan.",
            "why_b_ta": "சிந்து பகுதி ஒருபோதும் இந்தியாவால் இணைக்கப்படவில்லை; அது பாகிஸ்தானின் ஒரு மாகாணமாகவே உள்ளது.",
            "why_c_en": "The UN does not dictate domestic constitutional schedule inclusions.",
            "why_c_ta": "ஐ.நா உள்நாட்டு அரசியலமைப்பு அட்டவணைச் சேர்க்கைகளை ஆணையிடுவதில்லை.",
            "why_d_en": "Sindhi is not the official language of Gujarat or Maharashtra.",
            "why_d_ta": "சிந்தி குஜராத் அல்லது மகாராஷ்டிராவின் அதிகாரப்பூர்வ மொழி அல்ல.",
            "tip_en": "Eighth Schedule Non-Territorial Languages: SINDHI, SANSKRIT, URDU (spoken across multiple States without being limited to one homeland).",
            "tip_ta": "பிராந்திய எல்லை இல்லாத எட்டாவது அட்டவணை மொழிகள்: சிந்தி, சமஸ்கிருதம், உருது (ஒற்றைத் தாயகத்திற்குள் மட்டுப்படுத்தப்படாமல் பல மாநிலங்களில் பேசப்படுபவை).",
            "fact_en": "Sindhi became the 15th language in the Eighth Schedule on April 10, 1967.",
            "fact_ta": "1967 ஏப்ரல் 10 அன்று சிந்தி எட்டாவது அட்டவணையின் 15-வது மொழியானது."
        },
        # 19
        {
            "subtopic": "Languages of Eighth Schedule - Manipuri Script Issue",
            "stem_en": "Which ancient indigenous script has seen an official revival movement for writing the Manipuri (Meitei) language, recognized by the Manipur Legislative Assembly?",
            "stem_ta": "மணிப்பூரி (மெய்தேய்) மொழியை எழுதுவதற்காக மணிப்பூர் சட்டமன்றத்தால் அங்கீகரிக்கப்பட்டு, அதிகாரப்பூர்வமாகப் புத்துயிர் பெற்று வரும் பண்டைய பூர்வீக வரிவடிவம் எது?",
            "options": [
                ("Meitei Mayek script", "மெய்தேய் மயேக் வரிவடிவம்"),
                ("Bengali script exclusively", "பெங்காலி வரிவடிவம் மட்டுமே"),
                ("Devanagari script exclusively", "தேவநாகரி வரிவடிவம் மட்டுமே"),
                ("Brahmi script exclusively", "பிராமி வரிவடிவம் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "While Manipuri had been written in the Bengali-Assamese script since the 18th century, the Government of Manipur officially approved the phased re-introduction of the ancient indigenous 'Meitei Mayek' script in schools and administration starting in 2005.",
            "exp_ta": "18-ஆம் நூற்றாண்டு முதல் மணிப்பூரி பெங்காலி வரிவடிவத்தில் எழுதப்பட்டு வந்த போதிலும், 2005 முதல் பள்ளிகள் மற்றும் நிர்வாகத்தில் பண்டைய பூர்வீக 'மெய்தேய் மயேக்' வரிவடிவத்தை படிப்படியாக மீண்டும் அறிமுகப்படுத்துவதை மணிப்பூர் அரசு அதிகாரப்பூர்வமாக அங்கீகரித்தது.",
            "why_a_en": "Meitei Mayek is the indigenous script of Manipur undergoing state-sponsored revival.",
            "why_a_ta": "மெய்தேய் மயேக் என்பது அரசு ஆதரவுடன் புத்துயிர் பெற்று வரும் மணிப்பூரின் பூர்வீக வரிவடிவமாகும்.",
            "why_b_en": "Bengali script is being progressively phased out in favor of Meitei Mayek.",
            "why_b_ta": "பெங்காலி வரிவடிவம் மெய்தேய் மயேக்கிற்கு ஆதரவாகப் படிப்படியாக மாற்றப்பட்டு வருகிறது.",
            "why_c_en": "Devanagari is not the indigenous script of Manipuri.",
            "why_c_ta": "தேவநாகரி மணிப்பூரியின் பூர்வீக வரிவடிவம் அல்ல.",
            "why_d_en": "Brahmi is the ancient ancestral parent script of most Indian scripts, not the contemporary Manipuri revival script.",
            "why_d_ta": "பிராமி பெரும்பாலான இந்திய வரிவடிவங்களின் மூல வரிவடிவம், சமகால மணிப்பூரி வரிவடிவம் அல்ல.",
            "tip_en": "Manipuri (Meitei): Transitioning from Bengali script back to MEITEI MAYEK script.",
            "tip_ta": "மணிப்பூரி (மெய்தேய்): பெங்காலி வரிவடிவத்திலிருந்து மீண்டும் 'மெய்தேய் மயேக்' வரிவடிவத்திற்கு மாறுகிறது.",
            "fact_en": "Manipuri was added to the Eighth Schedule by the 71st CAA in 1992.",
            "fact_ta": "மணிப்பூரி 1992-ல் 71-வது திருத்தச் சட்டம் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது."
        },
        # 20
        {
            "subtopic": "Official Languages Act Section 6 State Acts Translations",
            "stem_en": "Under Section 6 of the Official Languages Act, 1963, what is required when a State Legislature passes an Act in a language other than Hindi?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 6-ன் கீழ், ஒரு மாநில சட்டமன்றம் இந்தி அல்லாத வேறு மொழியில் ஒரு சட்டத்தை நிறைவேற்றும்போது என்ன தேவைப்படுகிறது?",
            "options": [
                ("A translation thereof in Hindi, certified by the Governor, may be published in the Official Gazette of that State, alongside the mandatory English translation under Article 348(3)", "சரத்து 348(3)-ன் கீழான கட்டாய ஆங்கில மொழிபெயர்ப்புடன், ஆளுநரால் சான்றளிக்கப்பட்ட அதன் இந்தி மொழிபெயர்ப்பும் அம்மாநில அரசிதழில் வெளியிடப்படலாம்"),
                ("The State Act is automatically void unless it was introduced in Hindi first", "முதலில் இந்தியில் அறிமுகப்படுத்தப்படாவிட்டால் அந்த மாநிலச் சட்டம் தானாகவே செல்லாததாகிவிடும்"),
                ("The President must veto the Act under Article 201", "குடியரசுத் தலைவர் சரத்து 201-ன் கீழ் அந்தச் சட்டத்தை நிராகரிக்க வேண்டும்"),
                ("The State must adopt Hindi as its official language within six months", "அந்த மாநிலம் ஆறு மாதங்களுக்குள் இந்தியைத் தனது அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொள்ள வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Section 6 provides that where an Act is passed in any language other than Hindi by a State Legislature, an authorized translation thereof in Hindi may be published under the authority of the Governor, in addition to the authoritative English text required by Article 348(3).",
            "exp_ta": "பிரிவு 6-ன் படி, ஒரு மாநில சட்டமன்றத்தால் இந்தி அல்லாத வேறு ஏதேனும் மொழியில் சட்டம் நிறைவேற்றப்படும் போது, சரத்து 348(3)-ன் படி தேவைப்படும் அதிகாரப்பூர்வ ஆங்கில உரையுடன், ஆளுநரின் அதிகாரத்தின் கீழ் வெளியிடப்படும் அதன் அங்கீகரிக்கப்பட்ட இந்தி மொழிபெயர்ப்பும் வெளியிடப்படலாம்.",
            "why_a_en": "Section 6 provides an enabling framework for authorized Hindi translations of non-Hindi State Acts.",
            "why_a_ta": "பிரிவு 6 இந்தி அல்லாத மாநிலச் சட்டங்களின் அங்கீகரிக்கப்பட்ட இந்தி மொழிபெயர்ப்புகளுக்கான ஒரு சட்ட வசதியை வழங்குகிறது.",
            "why_b_en": "State Acts are fully valid in the State language and English.",
            "why_b_ta": "மாநிலச் சட்டங்கள் மாநில மொழி மற்றும் ஆங்கிலத்தில் முழுமையாகச் செல்லுபடியாகும்.",
            "why_c_en": "The President does not veto Acts merely because they are not in Hindi.",
            "why_c_ta": "இந்தியில் இல்லை என்பதற்காக மட்டுமே குடியரசுத் தலைவர் சட்டங்களை நிராகரிப்பதில்லை.",
            "why_d_en": "States have complete autonomy under Article 345 to choose their language.",
            "why_d_ta": "மாநிலங்கள் தங்கள் மொழியைத் தேர்வு செய்ய சரத்து 345-ன் கீழ் முழு சுயாட்சியைக் கொண்டுள்ளன.",
            "tip_en": "Section 6 = Authorized Hindi translation of State Acts (Permissive, alongside Article 348(3) English).",
            "tip_ta": "பிரிவு 6 = மாநிலச் சட்டங்களின் அங்கீகரிக்கப்பட்ட இந்தி மொழிபெயர்ப்பு (சரத்து 348(3) ஆங்கிலத்துடன் இணைந்து).",
            "fact_en": "This facilitates pan-Indian legal accessibility without superseding the English authoritative text.",
            "fact_ta": "இது ஆங்கில மூல வாசகத்தை மீறாமல் அகில இந்திய சட்ட அணுகலை எளிதாக்குகிறது."
        },
        # 21
        {
            "subtopic": "Languages of Eighth Schedule - Santhali Script",
            "stem_en": "What is the name of the indigenous script developed specifically for the Santhali language, which is now recognized on official currency notes and documents?",
            "stem_ta": "சந்தாலி மொழிக்காக பிரத்யேகமாக உருவாக்கப்பட்டு, தற்போது அதிகாரப்பூர்வ ரூபாய் நோட்டுகள் மற்றும் ஆவணங்களில் அங்கீகரிக்கப்பட்டுள்ள பூர்வீக வரிவடிவத்தின் பெயர் என்ன?",
            "options": [
                ("Ol Chiki script", "ஒல் சிக்கி வரிவடிவம்"),
                ("Kaithi script", "கைதி வரிவடிவம்"),
                ("Modi script", "மோடி வரிவடிவம்"),
                ("Grantha script", "கிரந்த வரிவடிவம்")
            ],
            "correct_key": "A",
            "exp_en": "The Ol Chiki script (also called Ol Cemet') was created by Pandit Raghunath Murmu in 1925 specifically for Santhali, and is officially used in West Bengal, Odisha, and Jharkhand for Santhali education.",
            "exp_ta": "ஒல் சிக்கி வரிவடிவம் 1925-ல் பண்டிட் ரகுநாத் முர்முவால் சந்தாலி மொழிக்காக பிரத்யேகமாக உருவாக்கப்பட்டது, மேலும் இது மேற்கு வங்கம், ஒடிசா மற்றும் ஜார்க்கண்டில் சந்தாலி கல்விக்காக அதிகாரப்பூர்வமாகப் பயன்படுத்தப்படுகிறது.",
            "why_a_en": "Ol Chiki is the distinct, authentic script of the Santhali language.",
            "why_a_ta": "ஒல் சிக்கி என்பது சந்தாலி மொழியின் தனித்துவமான, உண்மையான வரிவடிவமாகும்.",
            "why_b_en": "Kaithi was a historical cursive script used in Bihar and UP for Bhojpuri and Maithili.",
            "why_b_ta": "கைதி என்பது பீகார் மற்றும் உ.பியில் போஜ்புரி மற்றும் மைதிலிக்கு வரலாற்று ரீதியாகப் பயன்படுத்தப்பட்ட ஒரு வரிவடிவமாகும்.",
            "why_c_en": "Modi script was historically used for writing Marathi.",
            "why_c_ta": "மோடி வரிவடிவம் வரலாற்று ரீதியாக மராத்தி எழுதப் பயன்படுத்தப்பட்டது.",
            "why_d_en": "Grantha script was historically used in Tamil Nadu to write Sanskrit.",
            "why_d_ta": "கிரந்த வரிவடிவம் தமிழ்நாட்டில் சமஸ்கிருதம் எழுத வரலாற்று ரீதியாகப் பயன்படுத்தப்பட்டது.",
            "tip_en": "Santhali = Ol Chiki Script (invented by Pandit Raghunath Murmu in 1925).",
            "tip_ta": "சந்தாலி = ஒல் சிக்கி வரிவடிவம் (1925-ல் பண்டிட் ரகுநாத் முர்முவால் உருவாக்கப்பட்டது).",
            "fact_en": "Santhali was added to the Eighth Schedule by the 92nd Constitutional Amendment Act, 2003.",
            "fact_ta": "சந்தாலி 2003-ன் 92-வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது."
        },
        # 22
        {
            "subtopic": "Languages of Eighth Schedule - Maithili Script",
            "stem_en": "Before adopting the Devanagari script, in which historical script was Maithili traditionally written?",
            "stem_ta": "தேவநாகரி வரிவடிவத்தை ஏற்றுக்கொள்வதற்கு முன்பு, மைதிலி மொழி பாரம்பரியமாக எந்த வரலாற்று வரிவடிவத்தில் எழுதப்பட்டது?",
            "options": [
                ("Mithilakshar (Tirhuta) script", "மிதிலாக்சர் (திர்ஹுதா) வரிவடிவம்"),
                ("Sharada script", "சாரதா வரிவடிவம்"),
                ("Gurmukhi script", "குர்முகி வரிவடிவம்"),
                ("Vatteluttu script", "வட்டெழுத்து வரிவடிவம்")
            ],
            "correct_key": "A",
            "exp_en": "Maithili was historically written in the Mithilakshar (also known as Tirhuta or Kaithi) script, closely related to the Bengali and Assamese scripts, before transitioning predominantly to Devanagari in the 20th century.",
            "exp_ta": "20-ஆம் நூற்றாண்டில் முக்கியமாக தேவநாகரிக்கு மாறுவதற்கு முன்பு, மைதிலி வரலாற்று ரீதியாக பெங்காலி மற்றும் அசாமி வரிவடிவங்களுடன் நெருங்கிய தொடர்புடைய 'மிதிலாக்சர்' (திர்ஹுதா) வரிவடிவத்தில் எழுதப்பட்டது.",
            "why_a_en": "Mithilakshar/Tirhuta is the historical indigenous script of the Maithili language.",
            "why_a_ta": "மிதிலாக்சர்/திர்ஹுதா என்பது மைதிலி மொழியின் வரலாற்று பூர்வீக வரிவடிவமாகும்.",
            "why_b_en": "Sharada was the historical script of Kashmiri.",
            "why_b_ta": "சாரதா காஷ்மீரி மொழியின் வரலாற்று வரிவடிவமாகும்.",
            "why_c_en": "Gurmukhi is the script of Punjabi.",
            "why_c_ta": "குர்முகி என்பது பஞ்சாபி மொழியின் வரிவடிவமாகும்.",
            "why_d_en": "Vatteluttu was an ancient script used in Tamil Nadu and Kerala.",
            "why_d_ta": "வட்டெழுத்து என்பது தமிழ்நாடு மற்றும் கேரளாவில் பயன்படுத்தப்பட்ட ஒரு பண்டைய வரிவடிவமாகும்.",
            "tip_en": "Maithili: Traditional = Mithilakshar / Tirhuta; Contemporary = Devanagari.",
            "tip_ta": "மைதிலி: பாரம்பரியம் = மிதிலாக்சர் / திர்ஹுதா; சமகாலம் = தேவநாகரி.",
            "fact_en": "Maithili is spoken in North Bihar and the Terai region of Nepal.",
            "fact_ta": "மைதிலி வடக்கு பீகார் மற்றும் நேபாளத்தின் தெராய் பகுதிகளில் பேசப்படுகிறது."
        },
        # 23
        {
            "subtopic": "Official Language of Supreme Court Rule Framing",
            "stem_en": "Under Article 145, can the Supreme Court frame rules allowing arguments or petitions in Hindi without parliamentary legislation under Article 348(1)?",
            "stem_ta": "சரத்து 348(1)-ன் கீழான நாடாளுமன்றச் சட்டமின்றி, சரத்து 145-ன் கீழ் உச்ச நீதிமன்றம் இந்தியில் வாதங்கள் அல்லது மனுக்களை அனுமதிக்கும் விதிகளை உருவாக்க முடியுமா?",
            "options": [
                ("No, because Article 348(1) opens with a non-obstante clause that explicitly subordinates rule-making power to parliamentary legislation on language", "முடியாது, ஏனெனில் சரத்து 348(1) ஒரு தடையற்ற வாசகத்துடன் தொடங்குகிறது, இது மொழி மீதான நாடாளுமன்றச் சட்டத்திற்கு விதி உருவாக்கும் அதிகாரத்தை வெளிப்படையாகக் கீழ்ப்படுத்துகிறது"),
                ("Yes, because the Chief Justice of India has unlimited plenary powers under Article 145", "முடியும், ஏனெனில் இந்தியத் தலைமை நீதிபதிக்கு சரத்து 145-ன் கீழ் வரம்பற்ற முழு அதிகாரம் உள்ளது"),
                ("Yes, provided the President gives oral consent to the Chief Justice", "முடியும், குடியரசுத் தலைவர் தலைமை நீதிபதிக்கு வாய்மொழி ஒப்புதல் அளித்தால்"),
                ("Yes, by a simple resolution passed by the Bar Council of India", "முடியும், இந்திய பார் கவுன்சில் நிறைவேற்றும் எளிய தீர்மானம் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 145 rule-making power is expressly 'subject to the provisions of any law made by Parliament'. Moreover, Article 348(1) begins with 'Notwithstanding anything in the foregoing provisions of this Part, until Parliament by law otherwise provides... all proceedings... shall be in English'. Thus, the Supreme Court cannot alter its language by rules.",
            "exp_ta": "சரத்து 145-ன் விதி உருவாக்கும் அதிகாரம் 'நாடாளுமன்றத்தால் இயற்றப்படும் எந்தவொரு சட்டத்தின் விதிகளுக்கும் உட்பட்டது'. மேலும், சரத்து 348(1) 'நாடாளுமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக வகை செய்யும் வரை அனைத்து நடவடிக்கைகளும் ஆங்கிலத்தில் இருக்கும்' என்ற தடையற்ற வாசகத்தைக் கொண்டுள்ளது. எனவே, உச்ச நீதிமன்றம் தனது சொந்த விதிகளால் மொழியை மாற்ற முடியாது.",
            "why_a_en": "Article 348(1) binds the Supreme Court to English until Parliament passes an Act otherwise.",
            "why_a_ta": "நாடாளுமன்றம் சட்டம் இயற்றும் வரை உச்ச நீதிமன்றம் ஆங்கிலத்தைப் பயன்படுத்துவதற்கே சரத்து 348(1) கட்டுப்படுத்துகிறது.",
            "why_b_en": "Article 145 is expressly subject to parliamentary legislation.",
            "why_b_ta": "சரத்து 145 வெளிப்படையாக நாடாளுமன்றச் சட்டத்திற்கு உட்பட்டது.",
            "why_c_en": "Oral consent has no constitutional validity in public law.",
            "why_c_ta": "பொதுச் சட்டத்தில் வாய்மொழி ஒப்புதலுக்கு எந்த அரசியலமைப்புச் செல்லுபடியும் இல்லை.",
            "why_d_en": "The Bar Council of India has no authority over court procedural language.",
            "why_d_ta": "நீதிமன்ற நடைமுறை மொழியின் மீது இந்திய பார் கவுன்சிலுக்கு எந்த அதிகாரமும் இல்லை.",
            "tip_en": "Only PARLIAMENT BY LAW can authorize Hindi in the Supreme Court (Article 348(1)).",
            "tip_ta": "நாடாளுமன்றம் இயற்றும் சட்டம் மட்டுமே உச்ச நீதிமன்றத்தில் இந்தியை அனுமதிக்க முடியும் (சரத்து 348(1)).",
            "fact_en": "The Supreme Court dismissed public interest petitions seeking Hindi in Supreme Court proceedings as non-maintainable.",
            "fact_ta": "உச்ச நீதிமன்ற நடவடிக்கைகளில் இந்தியை அனுமதிக்கக் கோரிய பொதுநல மனுக்களை உச்ச நீதிமன்றம் ஏற்க மறுத்து தள்ளுபடி செய்தது."
        },
        # 24
        {
            "subtopic": "Languages of Eighth Schedule - Prakrit and Pali Status",
            "stem_en": "In what significant constitutional aspect do Pali and Prakrit differ from the other nine Classical Languages of India?",
            "stem_ta": "பாலி மற்றும் பிராகிருதம் ஆகிய மொழிகள் இந்தியாவின் மற்ற ஒன்பது செம்மொழிகளிலிருந்து எந்த முக்கியமான அரசியலமைப்பு அம்சத்தில் வேறுபடுகின்றன?",
            "options": [
                ("Pali and Prakrit are Classical Languages but are NOT included in the Eighth Schedule of the Constitution", "பாலி மற்றும் பிராகிருதம் செம்மொழிகள் ஆகும், ஆனால் அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை"),
                ("They are the only classical languages spoken outside Asia", "அவை ஆசியாவிற்கு வெளியே பேசப்படும் ஒரே செம்மொழிகள்"),
                ("They were recognized directly by a Constitutional Amendment Act", "அவை நேரடியாக ஓர் அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் அங்கீகரிக்கப்பட்டன"),
                ("They are the official languages of the Union Territories of Ladakh and Lakshadweep", "அவை லடாக் மற்றும் லட்சத்தீவு ஒன்றியப் பகுதிகளின் அதிகாரப்பூர்வ மொழிகள்")
            ],
            "correct_key": "A",
            "exp_en": "Among the 11 Classical Languages of India, nine (Tamil, Sanskrit, Telugu, Kannada, Malayalam, Odia, Assamese, Bengali, Marathi) are listed in the Eighth Schedule, while Pali and Prakrit are Classical Languages that do NOT feature in the Eighth Schedule.",
            "exp_ta": "இந்தியாவின் 11 செம்மொழிகளில், ஒன்பது மொழிகள் (தமிழ், சமஸ்கிருதம், தெலுங்கு, கன்னடம், மலையாளம், ஒடியா, அசாமி, பெங்காலி, மராத்தி) எட்டாவது அட்டவணையில் உள்ளன, அதே நேரத்தில் பாலி மற்றும் பிராகிருதம் எட்டாவது அட்டவணையில் இடம்பெறாத செம்மொழிகளாகும்.",
            "why_a_en": "This is a unique constitutional anomaly: Classical status without Eighth Schedule status.",
            "why_a_ta": "இது ஒரு தனித்துவமான அரசியலமைப்பு விசித்திரம்: எட்டாவது அட்டவணை அந்தஸ்து இல்லாத செம்மொழி அந்தஸ்து.",
            "why_b_en": "Both were ancient indigenous languages of the Indian subcontinent.",
            "why_b_ta": "இரண்டுமே இந்திய துணைக் கண்டத்தின் பண்டைய பூர்வீக மொழிகளாகும்.",
            "why_c_en": "Classical language status is conferred by executive Cabinet decision, not by Constitutional Amendment.",
            "why_c_ta": "செம்மொழி அந்தஸ்து அமைச்சரவையின் நிர்வாக முடிவால் வழங்கப்படுகிறது, அரசியலமைப்புத் திருத்தத்தால் அல்ல.",
            "why_d_en": "Ladakh uses Ladakhi/English/Urdu; Lakshadweep uses Malayalam/English.",
            "why_d_ta": "லடாக் லடாக்கி/ஆங்கிலம்/உருதுவைப் பயன்படுத்துகிறது; லட்சத்தீவு மலையாளம்/ஆங்கிலத்தைப் பயன்படுத்துகிறது.",
            "tip_en": "Classical Language count = 11; Eighth Schedule Languages = 22. Overlap = 9 languages.",
            "tip_ta": "செம்மொழிகள் எண்ணிக்கை = 11; எட்டாவது அட்டவணை மொழிகள் = 22. பொதுவானவை = 9 மொழிகள்.",
            "fact_en": "Ashoka's edicts across India were primarily inscribed in Prakrit in the Brahmi script.",
            "fact_ta": "இந்தியா முழுவதும் உள்ள அசோகரின் கல்வெட்டுகள் முதன்மையாக பிராமி வரிவடிவத்திலான பிராகிருதத்தில் பொறிக்கப்பட்டன."
        },
        # 25
        {
            "subtopic": "Language in Subordinate Courts",
            "stem_en": "Under Section 137 of the Code of Civil Procedure (CPC) and Section 272 of the Code of Criminal Procedure (CrPC), who determines the language of subordinate courts in a State?",
            "stem_ta": "உரிமையியல் நடைமுறைச் சட்டம் (CPC) பிரிவு 137 மற்றும் குற்றவியல் நடைமுறைச் சட்டம் (CrPC) பிரிவு 272-ன் கீழ், ஒரு மாநிலத்தில் உள்ள சார்பு நீதிமன்றங்களின் மொழியைத் தீர்மானிப்பது யார்?",
            "options": [
                ("The State Government", "மாநில அரசு"),
                ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
                ("The Union Ministry of Law and Justice", "ஒன்றிய சட்டம் மற்றும் நீதி அமைச்சகம்"),
                ("The Bar Council of the State", "மாநில பார் கவுன்சில்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 137 CPC and Section 272 CrPC, the State Government has the statutory power to determine what shall be the language of any court within the State other than the High Court (subordinate courts).",
            "exp_ta": "CPC பிரிவு 137 மற்றும் CrPC பிரிவு 272-ன் கீழ், உயர் நீதிமன்றம் தவிர மாநிலத்தில் உள்ள எந்தவொரு நீதிமன்றத்தின் (சார்நிலை நீதிமன்றங்கள்) மொழி என்னவாக இருக்க வேண்டும் என்பதைத் தீர்மானிக்கும் சட்டப்பூர்வ அதிகாரம் மாநில அரசுக்கே உள்ளது.",
            "why_a_en": "The State Government has statutory jurisdiction over the language of subordinate civil and criminal courts.",
            "why_a_ta": "சார்நிலை உரிமையியல் மற்றும் குற்றவியல் நீதிமன்றங்களின் மொழியின் மீது மாநில அரசுக்கே சட்டப்பூர்வ அதிகாரம் உள்ளது.",
            "why_b_en": "The Chief Justice of India regulates Supreme Court proceedings, not State subordinate courts.",
            "why_b_ta": "இந்தியத் தலைமை நீதிபதி உச்ச நீதிமன்றத்தை ஒழுங்குபடுத்துகிறார், மாநில சார்நிலை நீதிமன்றங்களை அல்ல.",
            "why_c_en": "Union Law Ministry has no jurisdiction over State subordinate court languages under CPC/CrPC.",
            "why_c_ta": "CPC/CrPC-ன் கீழ் மாநில சார்நிலை நீதிமன்ற மொழிகள் மீது ஒன்றிய சட்ட அமைச்சகத்திற்கு அதிகாரம் இல்லை.",
            "why_d_en": "Bar Councils regulate professional ethics of lawyers, not court languages.",
            "why_d_ta": "பார் கவுன்சில்கள் வழக்கறிஞர்களின் தொழில்முறை நெறிமுறைகளை ஒழுங்குபடுத்துகின்றன, நீதிமன்ற மொழிகளை அல்ல.",
            "tip_en": "Subordinate Courts Language = State Government (CPC Sec 137 / CrPC Sec 272); High Court = Governor + President (Art 348(2)).",
            "tip_ta": "சார்நிலை நீதிமன்றங்கள் மொழி = மாநில அரசு (CPC பிரிவு 137 / CrPC பிரிவு 272); உயர் நீதிமன்றம் = ஆளுநர் + குடியரசுத் தலைவர் (சரத்து 348(2)).",
            "fact_en": "In Tamil Nadu, Tamil is widely authorized and used in subordinate courts for evidence and judgments.",
            "fact_ta": "தமிழ்நாட்டில் சார்நிலை நீதிமன்றங்களில் சாட்சியங்கள் மற்றும் தீர்ப்புகளுக்குத் தமிழ் பரவலாக அங்கீகரிக்கப்பட்டு பயன்படுத்தப்படுகிறது."
        },
        # 26
        {
            "subtopic": "Languages of Eighth Schedule - Assamese Classical Milestone",
            "stem_en": "In October 2024, Assamese was recognized as a Classical Language. In which century do the earliest recorded literary works of the Assamese language (Charyapada and Kamrupi literature) originate?",
            "stem_ta": "அக்டோபர் 2024-ல் அசாமி மொழி செம்மொழியாக அங்கீகரிக்கப்பட்டது. அசாமி மொழியின் ஆரம்பகால இலக்கியப் படைப்புகள் (சர்யாபதம் மற்றும் காமரூபி இலக்கியம்) எந்த நூற்றாண்டைச் சேர்ந்தவை?",
            "options": [
                ("8th to 12th Century CE", "கி.பி. 8 முதல் 12-ஆம் நூற்றாண்டு"),
                ("18th Century CE", "கி.பி. 18-ஆம் நூற்றாண்டு"),
                ("20th Century CE", "கி.பி. 20-ஆம் நூற்றாண்டு"),
                ("2nd Century BCE", "கி.மு. 2-ஆம் நூற்றாண்டு")
            ],
            "correct_key": "A",
            "exp_en": "The antiquity of Assamese is traced back to the Charyapada (composed between the 8th and 12th centuries CE) and ancient Kamrupi inscriptions, satisfying the ancient literary criteria for classical language status in 2024.",
            "exp_ta": "அசாமி மொழியின் பழமை கி.பி. 8 முதல் 12-ஆம் நூற்றாண்டுகளுக்கு இடைப்பட்ட சர்யாபதம் மற்றும் பண்டைய காமரூபி கல்வெட்டுகளின் மூலம் அறியப்படுகிறது, இது 2024-ல் செம்மொழி அந்தஸ்திற்கான பண்டைய இலக்கிய அளவுகோல்களை நிறைவு செய்தது.",
            "why_a_en": "Charyapada Buddhist mystic songs represent the shared early heritage of Assamese, Bengali, and Odia.",
            "why_a_ta": "சர்யாபத பௌத்த பாடல்கள் அசாமி, பெங்காலி மற்றும் ஒடியா மொழிகளின் பகிரப்பட்ட ஆரம்பகால பாரம்பரியத்தைப் பிரதிபலிக்கின்றன.",
            "why_b_en": "18th century relates to modern Assamese under British colonial period.",
            "why_b_ta": "18-ஆம் நூற்றாண்டு என்பது பிரிட்டிஷ் காலத்து நவீன அசாமியுடன் தொடர்புடையது.",
            "why_c_en": "20th century is contemporary Assamese literature.",
            "why_c_ta": "20-ஆம் நூற்றாண்டு என்பது சமகால அசாமி இலக்கியமாகும்.",
            "why_d_en": "2nd Century BCE relates to early Sangam Tamil and Ashokan Prakrit, not Assamese.",
            "why_d_ta": "கி.மு. 2-ஆம் நூற்றாண்டு என்பது சங்கத் தமிழ் மற்றும் அசோகரின் பிராகிருதத்துடன் தொடர்புடையது, அசாமியுடன் அல்ல.",
            "tip_en": "Assamese Classical Status: October 2024; Earliest texts = Charyapada (8th-12th Century CE).",
            "tip_ta": "அசாமி செம்மொழி அந்தஸ்து: அக்டோபர் 2024; ஆரம்பகால நூல்கள் = சர்யாபதம் (கி.பி. 8-12 ஆம் நூற்றாண்டு).",
            "fact_en": "Assamese belongs to the Eastern branch of the Indo-Aryan language family.",
            "fact_ta": "அசாமி என்பது இந்தோ-ஆரிய மொழிக் குடும்பத்தின் கிழக்குப் பிரிவைச் சேர்ந்ததாகும்."
        },
        # 27
        {
            "subtopic": "Languages of Eighth Schedule - Dogri Language Heritage",
            "stem_en": "Under which Constitutional Amendment Act was Dogri (the language of Jammu region) added to the Eighth Schedule of the Constitution?",
            "stem_ta": "எந்த அரசியலமைப்புத் திருத்தச் சட்டத்தின் கீழ் டோக்ரி (ஜம்மு பிராந்தியத்தின் மொழி) அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது?",
            "options": [
                ("92nd Constitutional Amendment Act, 2003", "92-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"),
                ("71st Constitutional Amendment Act, 1992", "71-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992"),
                ("21st Constitutional Amendment Act, 1967", "21-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1967"),
                ("96th Constitutional Amendment Act, 2011", "96-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2011")
            ],
            "correct_key": "A",
            "exp_en": "Dogri was added to the Eighth Schedule by the 92nd Constitutional Amendment Act, 2003, along with Bodo, Maithili, and Santhali (BDMS).",
            "exp_ta": "போடோ, மைதிலி மற்றும் சந்தாலியுடன் (BDMS) இணைந்து, 2003-ன் 92-வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் டோக்ரி எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது.",
            "why_a_en": "Dogri was part of the 4 languages added by the 92nd CAA, 2003.",
            "why_a_ta": "டோக்ரி 2003-ன் 92-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்ட 4 மொழிகளில் ஒன்றாகும்.",
            "why_b_en": "71st CAA, 1992 added Konkani, Manipuri, and Nepali.",
            "why_b_ta": "71-வது திருத்தச் சட்டம், 1992 கொங்கணி, மணிப்பூரி மற்றும் நேபாளியைச் சேர்த்தது.",
            "why_c_en": "21st CAA, 1967 added Sindhi.",
            "why_c_ta": "21-வது திருத்தச் சட்டம், 1967 சிந்தியைச் சேர்த்தது.",
            "why_d_en": "96th CAA, 2011 changed Oriya to Odia.",
            "why_d_ta": "96-வது திருத்தச் சட்டம், 2011 ஒரியாவை ஒடியா என மாற்றியது.",
            "tip_en": "92nd CAA (2003) = Bodo + Dogri + Maithili + Santhali.",
            "tip_ta": "92-வது சட்டத்திருத்தம் (2003) = போடோ + டோக்ரி + மைதிலி + சந்தாலி.",
            "fact_en": "Dogri was historically written in the Takri script, but is now officially written in Devanagari.",
            "fact_ta": "டோக்ரி வரலாற்று ரீதியாக 'தாக்ரி' வரிவடிவத்தில் எழுதப்பட்டது, ஆனால் தற்போது அதிகாரப்பூர்வமாக தேவநாகரியில் எழுதப்படுகிறது."
        },
        # 28
        {
            "subtopic": "Official Language Commission 1955 - Dissenting Notes",
            "stem_en": "Who submitted famous dissenting minutes to the B.G. Kher Official Language Commission Report (1956), warning against the hasty replacement of English by Hindi?",
            "stem_ta": "பி.ஜி. கெர் அதிகாரப்பூர்வ மொழி ஆணைய அறிக்கைக்கு (1956) ஆங்கிலத்தை இந்தி கொண்டு அவசரமாக மாற்றுவதற்கு எதிராக எச்சரித்து புகழ்பெற்ற மாறுபட்ட கருத்துரைக்குறிப்புகளைச் சமர்ப்பித்தவர்கள் யார்?",
            "options": [
                ("Dr. Suniti Kumar Chatterji and Dr. P. Subbarayan", "டாக்டர் சுனிதி குமார் சட்டர்ஜி மற்றும் டாக்டர் பி. சுப்பராயன்"),
                ("C. Rajagopalachari and E.V. Ramasamy Periyar", "சி. ராஜகோபாலாச்சாரி மற்றும் ஈ.வெ.ரா. பெரியார்"),
                ("K. Kamaraj and C.N. Annadurai", "கே. காமராஜர் மற்றும் சி.என். அண்ணாதுரை"),
                ("Jawaharlal Nehru and Sardar Patel", "ஜவஹர்லால் நேரு மற்றும் சர்தார் படேல்")
            ],
            "correct_key": "A",
            "exp_en": "Dr. Suniti Kumar Chatterji (eminent linguist from Bengal) and Dr. P. Subbarayan (former Premier of Madras) submitted powerful notes of dissent to the 1956 Kher Commission report, protesting that the majority report was pushing Hindi too aggressively without considering non-Hindi sensitivities.",
            "exp_ta": "டாக்டர் சுனிதி குமார் சட்டர்ஜி (வங்காளத்தைச் சேர்ந்த பிரபல மொழியியலாளர்) மற்றும் டாக்டர் பி. சுப்பராயன் (மெட்ராஸ் முன்னாள் பிரதமர்) ஆகியோர் 1956 கெர் ஆணைய அறிக்கைக்கு வலுவான மாறுபட்ட கருத்துரைகளைச் சமர்ப்பித்தனர்; இந்தி பேசாத மக்களின் உணர்வுகளைக் கருத்தில் கொள்ளாமல் பெரும்பான்மை அறிக்கை இந்தியைத் தீவிரமாகத் திணிக்கிறது என்று அவர்கள் எதிர்த்தனர்.",
            "why_a_en": "Chatterji and Subbarayan were the two official dissenting members on the Kher Commission.",
            "why_a_ta": "சட்டர்ஜி மற்றும் சுப்பராயன் ஆகியோர் கெர் ஆணையத்தில் அதிகாரப்பூர்வமாக மாறுபட்ட கருத்து தெரிவித்த இரண்டு உறுப்பினர்களாவர்.",
            "why_b_en": "Rajaji and Periyar were external political leaders, not members of the Kher Commission.",
            "why_b_ta": "ராஜாஜி மற்றும் பெரியார் வெளிப்புற அரசியல் தலைவர்கள், கெர் ஆணையத்தின் உறுப்பினர்கள் அல்ல.",
            "why_c_en": "Kamaraj and Annadurai were active in state politics, not members of the 1955 commission.",
            "why_c_ta": "காமராஜர் மற்றும் அண்ணாதுரை மாநில அரசியலில் தீவிரமாக இருந்தனர், 1955 ஆணைய உறுப்பினர்கள் அல்ல.",
            "why_d_en": "Patel had passed away in 1950, and Nehru was Prime Minister.",
            "why_d_ta": "படேல் 1950-ல் மறைந்துவிட்டார், நேரு பிரதமராக இருந்தார்.",
            "tip_en": "1956 Kher Report Dissenters: Suniti Kumar Chatterji (Bengal) + P. Subbarayan (Madras).",
            "tip_ta": "1956 கெர் அறிக்கை எதிர்ப்பாளர்கள்: சுனிதி குமார் சட்டர்ஜி (வங்கம்) + பி. சுப்பராயன் (மெட்ராஸ்).",
            "fact_en": "Their dissent laid the intellectual foundation for the continued retention of English as an associate language.",
            "fact_ta": "அவர்களது மாறுபட்ட கருத்துக்கள் ஆங்கிலத்தைத் தொடர்ந்து இணை மொழியாகத் தக்கவைப்பதற்கான அறிவுசார் அடித்தளத்தை அமைத்தன."
        },
        # 29
        {
            "subtopic": "Nehru Assurance on Official Language",
            "stem_en": "In which year did Prime Minister Jawaharlal Nehru give his historic assurance in the Lok Sabha that English would continue as an associate official language as long as the non-Hindi speaking people wanted it?",
            "stem_ta": "இந்தி பேசாத மக்கள் விரும்பும் வரையில் ஆங்கிலம் கூடுதல் அதிகாரப்பூர்வ மொழியாகத் தொடரும் என்று பிரதமர் ஜவஹர்லால் நேரு மக்களவையில் தனது வரலாற்றுச் சிறப்புமிக்க உறுதிமொழியை எந்த ஆண்டில் அளித்தார்?",
            "options": [
                ("1959", "1959"),
                ("1950", "1950"),
                ("1967", "1967"),
                ("1976", "1976")
            ],
            "correct_key": "A",
            "exp_en": "On August 7 and September 4, 1959, Prime Minister Jawaharlal Nehru gave his famous solemn assurance in the Lok Sabha: 'English will continue as an associate additional language in the Central Government until the non-Hindi speaking people desire a change.'",
            "exp_ta": "1959 ஆகஸ்ட் 7 மற்றும் செப்டம்பர் 4 ஆகிய தேதிகளில், பிரதமர் ஜவஹர்லால் நேரு மக்களவையில் தனது புகழ்பெற்ற உறுதிமொழியை அளித்தார்: 'இந்தி பேசாத மக்கள் மாற்றத்தை விரும்பும் வரை மத்திய அரசில் ஆங்கிலம் ஒரு கூடுதல் இணை மொழியாகத் தொடரும்.'",
            "why_a_en": "1959 was the year of the Nehru Assurance on the floor of the Lok Sabha.",
            "why_a_ta": "1959 என்பது மக்களவையில் நேரு உறுதிமொழி அளித்த ஆண்டாகும்.",
            "why_b_en": "1950 was the commencement of the Constitution.",
            "why_b_ta": "1950 என்பது அரசியலமைப்பு அமலுக்கு வந்த ஆண்டாகும்.",
            "why_c_en": "1967 was the statutory enactment of the Nehru Assurance via the 1967 Amendment Act under Indira Gandhi.",
            "why_c_ta": "1967 என்பது இந்திரா காந்தியின் கீழ் திருத்தச் சட்டம் மூலம் நேரு உறுதிமொழிக்குச் சட்ட வடிவம் கொடுக்கப்பட்ட ஆண்டாகும்.",
            "why_d_en": "1976 was the Official Languages Rules year.",
            "why_d_ta": "1976 என்பது அதிகாரப்பூர்வ மொழிகள் விதிகள் ஆண்டாகும்.",
            "tip_en": "Nehru Assurance = 1959 (Spoken in Lok Sabha); Statutory Enactment = 1967 (Section 3(5) of 1963 Act).",
            "tip_ta": "நேரு உறுதிமொழி = 1959 (மக்களவையில் பேசப்பட்டது); சட்ட வடிவம் = 1967 (1963 சட்டத்தின் பிரிவு 3(5)).",
            "fact_en": "The assurance calmed anti-Hindi sentiments in South India temporarily until Nehru's death in 1964.",
            "fact_ta": "இவ்வுறுதிமொழி 1964-ல் நேரு இறக்கும் வரை தென்னிந்தியாவில் இந்தி எதிர்ப்பு உணர்வுகளைத் தற்காலிகமாகத் தணித்தது."
        },
        # 30
        {
            "subtopic": "Languages of Eighth Schedule - Sindhi Protection",
            "stem_en": "Under which Union Ministry does the National Council for Promotion of Sindhi Language (NCPSL) operate to promote this Eighth Schedule language?",
            "stem_ta": "எட்டாவது அட்டவணை மொழியான சிந்தியை மேம்படுத்துவதற்காக சிந்தி மொழி மேம்பாட்டிற்கான தேசிய கவுன்சில் (NCPSL) எந்த ஒன்றிய அமைச்சகத்தின் கீழ் செயல்படுகிறது?",
            "options": [
                ("Ministry of Education", "கல்வி அமைச்சகம்"),
                ("Ministry of Home Affairs", "உள்துறை அமைச்சகம்"),
                ("Ministry of Culture", "கலாச்சார அமைச்சகம்"),
                ("Ministry of External Affairs", "வெளியுறவு அமைச்சகம்")
            ],
            "correct_key": "A",
            "exp_en": "The National Council for Promotion of Sindhi Language (NCPSL) is an autonomous body established in 1994 under the Department of Higher Education, Ministry of Education, headquartered in New Delhi.",
            "exp_ta": "சிந்தி மொழி மேம்பாட்டிற்கான தேசிய கவுன்சில் (NCPSL) என்பது 1994-ல் கல்வி அமைச்சகத்தின் உயர் கல்வித் துறையின் கீழ் புது தில்லியைத் தலைமையிடமாகக் கொண்டு நிறுவப்பட்ட ஒரு தன்னாட்சி அமைப்பாகும்.",
            "why_a_en": "NCPSL functions under the Ministry of Education (Department of Higher Education).",
            "why_a_ta": "NCPSL கல்வி அமைச்சகத்தின் (உயர் கல்வித் துறை) கீழ் செயல்படுகிறது.",
            "why_b_en": "Home Affairs deals with Official Language implementation, not Sindhi literary development.",
            "why_b_ta": "உள்துறை அமைச்சகம் அதிகாரப்பூர்வ மொழிச் செயல்பாட்டைக் கண்காணிக்கிறது, சிந்தி இலக்கிய வளர்ச்சியை அல்ல.",
            "why_c_en": "Ministry of Culture oversees Sahitya Akademi, but NCPSL is under Education.",
            "why_c_ta": "கலாச்சார அமைச்சகம் சாகித்ய அகாதமியைக் கண்காணிக்கிறது, ஆனால் NCPSL கல்வி அமைச்சகத்தின் கீழ் உள்ளது.",
            "why_d_en": "External Affairs has no role in domestic scheduled language councils.",
            "why_d_ta": "உள்நாட்டு அட்டவணை மொழிக் கவுன்சில்களில் வெளியுறவு அமைச்சகத்திற்குப் பங்கு இல்லை.",
            "tip_en": "Autonomous Language Councils (Sindhi, Urdu) operate under the Ministry of Education.",
            "tip_ta": "தன்னாட்சி மொழிக் கவுன்சில்கள் (சிந்தி, உருது) கல்வி அமைச்சகத்தின் கீழ் செயல்படுகின்றன.",
            "fact_en": "Similarly, the National Council for Promotion of Urdu Language (NCPUL) also functions under the Ministry of Education.",
            "fact_ta": "இதேபோல், உருது மொழி மேம்பாட்டிற்கான தேசிய கவுன்சிலும் (NCPUL) கல்வி அமைச்சகத்தின் கீழேயே செயல்படுகிறது."
        },
        # 31
        {
            "subtopic": "Languages of Eighth Schedule - Classical Tamil Institution",
            "stem_en": "In which year was the Central Institute of Classical Tamil (CICT) established as an autonomous research institution in Chennai under the Ministry of Education?",
            "stem_ta": "செம்மொழித் தமிழாய்வு மத்திய நிறுவனம் (CICT) கல்வி அமைச்சகத்தின் கீழ் சென்னையில் ஒரு தன்னாட்சி ஆராய்ச்சி நிறுவனமாக எந்த ஆண்டில் நிறுவப்பட்டது?",
            "options": [
                ("2008", "2008"),
                ("2004", "2004"),
                ("2011", "2011"),
                ("2016", "2016")
            ],
            "correct_key": "A",
            "exp_en": "Following the declaration of Tamil as a Classical Language in 2004, the Central Institute of Classical Tamil (CICT) was established as an autonomous institute on May 19, 2008 (initially functioning from the Central Institute of Indian Languages, Mysuru).",
            "exp_ta": "2004-ல் தமிழ் செம்மொழியாக அறிவிக்கப்பட்டதைத் தொடர்ந்து, 2008 மே 19 அன்று செம்மொழித் தமிழாய்வு மத்திய நிறுவனம் (CICT) சென்னையில் ஒரு தன்னாட்சி அமைப்பாக நிறுவப்பட்டது (தொடக்கத்தில் மைசூரு மத்திய இந்திய மொழிகள் நிறுவனத்திலிருந்து செயல்பட்டது).",
            "why_a_en": "2008 was the year CICT Chennai was formally incorporated as an autonomous institution.",
            "why_a_ta": "2008 என்பது CICT சென்னை ஒரு தன்னாட்சி நிறுவனமாக முறையாக ஒருங்கிணைக்கப்பட்ட ஆண்டாகும்.",
            "why_b_en": "2004 was the notification of Tamil as a Classical Language, not the formal autonomous establishment of CICT.",
            "why_b_ta": "2004 தமிழ் செம்மொழியாக அறிவிக்கப்பட்ட ஆண்டு, CICT தன்னாட்சி அமைப்பாக நிறுவப்பட்ட ஆண்டு அல்ல.",
            "why_c_en": "2011 was later during its academic expansion.",
            "why_c_ta": "2011 என்பது பின்னர் அதன் கல்வி விரிவாக்கக் காலமாகும்.",
            "why_d_en": "2016 was not the founding year.",
            "why_d_ta": "2016 நிறுவன ஆண்டு அல்ல.",
            "tip_en": "Classical Tamil Declaration = 2004; CICT Autonomous Institute established = 2008 in Chennai.",
            "tip_ta": "செம்மொழித் தமிழ் அறிவிப்பு = 2004; CICT தன்னாட்சி நிறுவனம் நிறுவப்பட்டது = 2008 சென்னையில்.",
            "fact_en": "The permanent campus of CICT at Perumbakkam, Chennai was inaugurated by Prime Minister Narendra Modi in January 2022.",
            "fact_ta": "சென்னை பெரும்பாக்கத்தில் உள்ள CICT-ன் நிரந்தர வளாகம் 2022 ஜனவரியில் பிரதமர் நரேந்திர மோடியால் திறந்து வைக்கப்பட்டது."
        },
        # 32
        {
            "subtopic": "Languages of Eighth Schedule - Prakrit Classical Literature",
            "stem_en": "Which major ancient religious corpus is predominantly composed in the Prakrit language, justifying its Classical Language declaration in 2024?",
            "stem_ta": "2024-ல் செம்மொழியாக அறிவிக்கப்பட்டதற்கு நியாயமாக விளங்கும், பிராகிருத மொழியில் முதன்மையாக இயற்றப்பட்டுள்ள முக்கிய பண்டைய சமய இலக்கியத் தொகுப்பு எது?",
            "options": [
                ("The ancient Jain Agamas and canonical texts", "பண்டைய சமண ஆகமங்கள் மற்றும் சமய நெறி நூல்கள்"),
                ("The Vedic Samhitas", "வேத சம்ஹிதைகள்"),
                ("The Sangam anthologies", "சங்கத் தொகை நூல்கள்"),
                ("The Guru Granth Sahib", "குரு கிரந்த சாகிப்")
            ],
            "correct_key": "A",
            "exp_en": "The sacred canonical texts of Jainism (the Jain Agamas) were composed in Ardhamagadhi Prakrit and other Prakrit dialects (like Shauraseni and Maharashtri), representing a vast independent ancient philosophical literature.",
            "exp_ta": "சமண சமயத்தின் புனித ஆகம நூல்கள் அர்த்தமாகதி பிராகிருதம் மற்றும் பிற பிராகிருத வழக்குகளில் (சௌரசேனி மற்றும் மகாராஷ்டிரி) இயற்றப்பட்டன, இது ஒரு பரந்த சுயாதீனமான பண்டைய தத்துவ இலக்கியத்தைப் பிரதிபலிக்கிறது.",
            "why_a_en": "The Jain Agamas are the crowning literary glory of the Prakrit language.",
            "why_a_ta": "சமண ஆகமங்கள் பிராகிருத மொழியின் உன்னதமான இலக்கியப் பெருமையாகும்.",
            "why_b_en": "The Vedic Samhitas were composed in Vedic Sanskrit.",
            "why_b_ta": "வேத சம்ஹிதைகள் வேத சமஸ்கிருதத்தில் இயற்றப்பட்டன.",
            "why_c_en": "The Sangam anthologies were composed in Classical Tamil.",
            "why_c_ta": "சங்கத் தொகை நூல்கள் செவ்வியல் தமிழில் இயற்றப்பட்டன.",
            "why_d_en": "The Guru Granth Sahib is in Sant Bhasha (incorporating Punjabi, Braj, Lahnda).",
            "why_d_ta": "குரு கிரந்த சாகிப் சாந்த் பாஷாவில் (பஞ்சாபி, பிராஜ், லஹந்தா கலந்த மொழி) உள்ளது.",
            "tip_en": "Classical Religions & Languages: Buddhism = PALI; Jainism = PRAKRIT; Hinduism = SANSKRIT & TAMIL.",
            "tip_ta": "செவ்வியல் சமயங்கள் & மொழிகள்: பௌத்தம் = பாலி; சமணம் = பிராகிருதம்; இந்து சமயம் = சமஸ்கிருதம் & தமிழ்.",
            "fact_en": "Gunadhya's lost epic Brihatkatha was originally composed in the Paishachi dialect of Prakrit.",
            "fact_ta": "குணாட்டியரின் புகழ்பெற்ற பிருஹத்கதா காப்பியம் முதலில் பிராகிருதத்தின் பைசாசி வழக்கில் இயற்றப்பட்டது."
        },
        # 33
        {
            "subtopic": "Languages of Eighth Schedule - Pali Buddhist Canon",
            "stem_en": "Which foundational canonical collection of early Buddhist scriptures is preserved exclusively in the Pali language?",
            "stem_ta": "ஆரம்பகால பௌத்த புனித நூல்களின் எந்த அடிப்படைத் தொகுப்பு பாலி மொழியில் மட்டுமே பாதுகாக்கப்பட்டுள்ளது?",
            "options": [
                ("The Tipitaka (Three Baskets: Vinaya, Sutta, Abhidhamma)", "திபிடகம் / திரிபீடகம் (மூன்று கூடைகள்: வினய, சுத்த, அபிதம்ம)"),
                ("The Upanishads", "உபநிடதங்கள்"),
                ("The Epics Ramayana and Mahabharata", "இராமாயணம் மற்றும் மகாபாரத இதிகாசங்கள்"),
                ("The Silappadikaram and Manimekalai", "சிலப்பதிகாரம் மற்றும் மணிமேகலை")
            ],
            "correct_key": "A",
            "exp_en": "The Tipitaka (Pali Canon), consisting of the Vinaya Pitaka (monastic rules), Sutta Pitaka (discourses of the Buddha), and Abhidhamma Pitaka (philosophical analysis), is preserved in Pali, forming the basis of its Classical declaration in 2024.",
            "exp_ta": "வினய பீடகம் (துறவற விதிகள்), சுத்த பீடகம் (புத்தரின் போதனைகள்) மற்றும் அபிதம்ம பீடகம் (தத்துவ ஆய்வு) ஆகியவற்றைக் கொண்ட திபிடகம் (திரிபீடகம்) பாலி மொழியில் பாதுகாக்கப்பட்டுள்ளது, இதுவே 2024-ல் அதன் செம்மொழி அறிவிப்புக்கான அடிப்படையாகும்.",
            "why_a_en": "The Tipitaka is the monumental classical heritage of the Pali language.",
            "why_a_ta": "திரிபீடகம் என்பது பாலி மொழியின் மகத்தான செவ்வியல் பாரம்பரியமாகும்.",
            "why_b_en": "The Upanishads are Vedic Sanskrit texts.",
            "why_b_ta": "உபநிடதங்கள் வேத சமஸ்கிருத நூல்களாகும்.",
            "why_c_en": "The Epics are in Classical Sanskrit.",
            "why_c_ta": "இதிகாசங்கள் செவ்வியல் சமஸ்கிருதத்தில் உள்ளன.",
            "why_d_en": "Silappadikaram and Manimekalai are ancient Tamil epics.",
            "why_d_ta": "சிலப்பதிகாரமும் மணிமேகலையும் பண்டைய தமிழ்க் காப்பியங்களாகும்.",
            "tip_en": "Pali = Language of Theravada Buddhist Canon (Tipitaka); Declared Classical in Oct 2024.",
            "tip_ta": "பாலி = தேரவாத பௌத்த புனித நூல்களின் மொழி (திரிபீடகம்); அக். 2024-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
            "fact_en": "The Buddha chose to preach in the vernacular Pali/Magadhi rather than formal Vedic Sanskrit to reach common people.",
            "fact_ta": "சாதாரண மக்களைச் சென்றடைய புத்தர் முறையான வேத சமஸ்கிருதத்திற்குப் பதிலாக பாலி/மாகதி பேச்சு மொழியிலேயே போதித்தார்."
        },
        # 34
        {
            "subtopic": "Article 348 Judicial Pronouncements Rule",
            "stem_en": "What is the legal effect of a High Court delivering a judgment solely in Hindi or a regional language without an accompanying English translation, where Section 7 of the 1963 Act applies?",
            "stem_ta": "1963 சட்டத்தின் பிரிவு 7 பொருந்தும் இடங்களில், அதனுடன் ஆங்கில மொழிபெயர்ப்பு இல்லாமல் உயர் நீதிமன்றம் ஒன்று இந்தி அல்லது வட்டார மொழியில் மட்டுமே ஒரு தீர்ப்பை வழங்கினால் அதன் சட்டரீதியான விளைவு என்ன?",
            "options": [
                ("It is procedurally defective and contrary to the mandatory requirement of Section 7 of the Official Languages Act, 1963", "இது நடைமுறை குறைபாடுடையது மற்றும் அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 7-ன் கட்டாயத் தேவைக்கு முரணானது"),
                ("The judgment becomes a valid Supreme Court precedent automatically", "அந்தத் தீர்ப்பு தானாகவே ஒரு செல்லுபடியாகும் உச்ச நீதிமன்ற முன்னுதாரணமாக மாறும்"),
                ("The judge is dismissed immediately by the Governor", "நீதிபதி உடனடியாக ஆளுநரால் பதவி நீக்கம் செய்யப்படுகிறார்"),
                ("The judgment is completely valid without any translation ever needed", "எந்த மொழிபெயர்ப்பும் தேவையின்றி அந்தத் தீர்ப்பு முற்றிலும் செல்லுபடியாகும்")
            ],
            "correct_key": "A",
            "exp_en": "Section 7 of the Official Languages Act, 1963 explicitly mandates that judgments delivered in Hindi must be accompanied by an authoritative translation in English. Failing to provide this translation creates a procedural defect that impedes appeals to the Supreme Court under Article 348(1).",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 7, இந்தியில் வழங்கப்படும் தீர்ப்புகளுடன் கட்டாயமாக அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு இணைக்கப்பட வேண்டும் என்று விதிக்கிறது. இந்த மொழிபெயர்ப்பை வழங்கத் தவறுவது நடைமுறைக் குறைபாட்டை உருவாக்கி, சரத்து 348(1)-ன் கீழ் உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்வதைத் தடுக்கிறது.",
            "why_a_en": "The statutory requirement of an English translation under Section 7 is mandatory, not directory.",
            "why_a_ta": "பிரிவு 7-ன் கீழான ஆங்கில மொழிபெயர்ப்பின் சட்டப்பூர்வ தேவை கட்டாயமானது, விருப்பத்திற்குரியது அல்ல.",
            "why_b_en": "A High Court judgment never becomes a Supreme Court precedent.",
            "why_b_ta": "உயர் நீதிமன்றத் தீர்ப்பு ஒருபோதும் உச்ச நீதிமன்ற முன்னுதாரணமாக மாறாது.",
            "why_c_en": "Judges cannot be removed by Governors; removal requires parliamentary impeachment under Article 124(4).",
            "why_c_ta": "நீதிபதிகளை ஆளுநர்கள் நீக்க முடியாது; நீக்குவதற்கு நாடாளுமன்ற பதவிநீக்கத் தீர்மானம் தேவை.",
            "why_d_en": "Section 7 expressly forbids judgments without translation.",
            "why_d_ta": "பிரிவு 7 மொழிபெயர்ப்பு இல்லாத தீர்ப்புகளை வெளிப்படையாகத் தடை செய்கிறது.",
            "tip_en": "Section 7 Rule: High Court Hindi Judgment MUST have an authoritative English translation.",
            "tip_ta": "பிரிவு 7 விதி: உயர் நீதிமன்ற இந்தித் தீர்ப்புடன் கட்டாயமாக ஓர் அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு இருக்க வேண்டும்.",
            "fact_en": "Law Commission Report No. 216 (2008) highlighted that non-English judgments create extreme friction in the appellate hierarchy.",
            "fact_ta": "சட்ட ஆணையத்தின் அறிக்கை எண் 216 (2008), ஆங்கிலம் அல்லாத தீர்ப்புகள் மேல்முறையீட்டு முறையில் கடுமையான முரண்பாடுகளை ஏற்படுத்துகின்றன என்பதைச் சுட்டிக்காட்டியது."
        },
        # 35
        {
            "subtopic": "Languages of Eighth Schedule - Classical Marathi Landmark",
            "stem_en": "Under which committee report set up by the Maharashtra Government did Marathi establish its antiquity of over 2000 years, leading to its Classical status in 2024?",
            "stem_ta": "மகாராஷ்டிர அரசால் அமைக்கப்பட்ட எந்தக் குழுவின் அறிக்கையின் கீழ் மராத்தி மொழி தனது 2000 ஆண்டுகாலப் பழமையை நிரூபித்து, 2024-ல் செம்மொழி அந்தஸ்தைப் பெற்றது?",
            "options": [
                ("Ranganath Pathare Committee", "ரங்கநாத் பதாரே குழு"),
                ("Kelkar Committee", "கேல்கர் குழு"),
                ("Sukthankar Committee", "சுக்தங்கர் குழு"),
                ("Dandekar Committee", "தண்டேகர் குழு")
            ],
            "correct_key": "A",
            "exp_en": "The Maharashtra Government constituted an expert committee headed by eminent writer Prof. Ranganath Pathare in 2012, which submitted a comprehensive 1000-page dossier proving that Marathi evolved from Maharashtri Prakrit and possessed ancient inscriptions dating back over 2000 years.",
            "exp_ta": "மகாராஷ்டிர அரசு 2012-ல் பிரபல எழுத்தாளர் பேராசிரியர் ரங்கநாத் பதாரே தலைமையில் ஒரு நிபுணர் குழுவை அமைத்தது, அக்குழு மராத்தி மகாராஷ்டிரி பிராகிருதத்திலிருந்து உருவானது என்பதையும், 2000 ஆண்டுகளுக்கும் முந்தைய பண்டைய கல்வெட்டுகளைக் கொண்டுள்ளது என்பதையும் நிரூபிக்கும் 1000 பக்க விரிவான ஆவணத்தைச் சமர்ப்பித்தது.",
            "why_a_en": "The Ranganath Pathare Committee was the official expert body that established Marathi's classical claim.",
            "why_a_ta": "ரங்கநாத் பதாரே குழு என்பது மராத்தியின் செம்மொழி உரிமையை நிறுவிய அதிகாரப்பூர்வ நிபுணர் அமைப்பாகும்.",
            "why_b_en": "Kelkar Committee dealt with regional imbalances in Maharashtra, not language antiquity.",
            "why_b_ta": "கேல்கர் குழு மகாராஷ்டிராவின் பிராந்திய ஏற்றத்தாழ்வுகளைக் கையாண்டது, மொழிப் பழமையை அல்ல.",
            "why_c_en": "Sukthankar was an editor of the Critical Edition of Mahabharata.",
            "why_c_ta": "சுக்தங்கர் மகாபாரதத்தின் விமர்சனப் பதிப்பின் பதிப்பாசிரியர் ஆவார்.",
            "why_d_en": "Dandekar Committee was on regional development allocation.",
            "why_d_ta": "தண்டேகர் குழு பிராந்திய வளர்ச்சி ஒதுக்கீடு தொடர்பானது.",
            "tip_en": "Marathi Classical Dossier = Prof. Ranganath Pathare Committee (2012 -> approved Oct 2024).",
            "tip_ta": "மராத்தி செம்மொழி அறிக்கை = பேராசிரியர் ரங்கநாத் பதாரே குழு (2012 -> அக். 2024-ல் ஒப்புதல்).",
            "fact_en": "The Naneghat inscription (1st Century BCE) in Maharashtra was central to proving its antiquity.",
            "fact_ta": "மகாராஷ்டிராவில் உள்ள நானேகட் கல்வெட்டு (கி.மு. 1-ஆம் நூற்றாண்டு) அதன் பழமையை நிரூபிப்பதில் மையமாக இருந்தது."
        },
        # 36
        {
            "subtopic": "Article 351 Harmonious Synthesis Mandate",
            "stem_en": "What unique cultural role does Article 351 assign to the Hindi language in the constitutional scheme?",
            "stem_ta": "அரசியலமைப்புத் திட்டத்தில் இந்தி மொழிக்கு சரத்து 351 எந்த தனித்துவமான கலாச்சாரப் பங்கை ஒதுக்குகிறது?",
            "options": [
                ("To serve as a medium of expression for all the elements of the composite culture of India", "இந்தியாவின் கூட்டுப் பண்பாட்டின் அனைத்துக் கூறுகளையும் வெளிப்படுத்தும் ஊடகமாகச் செயல்படுதல்"),
                ("To extinguish all regional vernacular dialects completely", "அனைத்து வட்டார மொழி வழக்குகளையும் முழுமையாக அழித்தல்"),
                ("To replace English immediately in foreign embassies abroad", "வெளிநாடுகளில் உள்ள தூதரகங்களில் ஆங்கிலத்தை உடனடியாக மாற்றுதல்"),
                ("To establish a uniform monolithic religious tradition", "ஒரே மாதிரியான ஒற்றை மதப் பாரம்பரியத்தை நிறுவுதல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 351 states: 'It shall be the duty of the Union to promote the spread of the Hindi language, to develop it so that it may serve as a medium of expression for all the elements of the composite culture of India...'",
            "exp_ta": "சரத்து 351 கூறுகிறது: 'இந்தியாவின் கூட்டுப் பண்பாட்டின் அனைத்துக் கூறுகளையும் வெளிப்படுத்தும் ஊடகமாகத் திகழும் வகையில் இந்தி மொழியின் பரவலை ஊக்குவிப்பதும், அதனை வளர்ப்பதும் ஒன்றியத்தின் கடமையாகும்...'",
            "why_a_en": "The phrase 'composite culture of India' (Samasa Sanskriti) is the constitutional soul of Article 351.",
            "why_a_ta": "'இந்தியாவின் கூட்டுப் பண்பாடு' (சாமாச சமஸ்கிருதி) என்ற தொடர் சரத்து 351-ன் அரசியலமைப்பு ஆன்மாவாகும்.",
            "why_b_en": "Article 351 does not seek to extinguish regional languages; it directs assimilation from them.",
            "why_b_ta": "சரத்து 351 வட்டார மொழிகளை அழிக்க முனையவில்லை; அவற்றிலிருந்து உள்வாங்க வழிகாட்டுகிறது.",
            "why_c_en": "Foreign embassy languages are governed by diplomatic protocols, not Article 351.",
            "why_c_ta": "வெளிநாட்டுத் தூதரக மொழிகள் தூதரக நெறிமுறைகளால் நிர்வகிக்கப்படுகின்றன, சரத்து 351-ஆல் அல்ல.",
            "why_d_en": "India is a secular republic; language promotion has no religious homogenization goal.",
            "why_d_ta": "இந்தியா ஒரு மதச்சார்பற்ற குடியரசு; மொழி வளர்ச்சிக்கு மத ஒற்றைமயமாக்கல் நோக்கம் இல்லை.",
            "tip_en": "Article 351 Key Phrase: 'Medium of expression for all elements of the COMPOSITE CULTURE of India'.",
            "tip_ta": "சரத்து 351 முக்கியச் சொல்: 'இந்தியாவின் கூட்டுப் பண்பாட்டின் அனைத்துக் கூறுகளையும் வெளிப்படுத்தும் ஊடகம்'.",
            "fact_en": "The concept of 'composite culture' also appears in Fundamental Duty Article 51A(f).",
            "fact_ta": "'கூட்டுப் பண்பாடு' என்ற கருத்து அடிப்படைக் கடமையான சரத்து 51A(f)-லும் இடம்பெற்றுள்ளது."
        },
        # 37
        {
            "subtopic": "Languages of Eighth Schedule - Original 14 Languages Composition",
            "stem_en": "Which of the following languages was NOT one of the original 14 languages included in the Eighth Schedule in 1950?",
            "stem_ta": "பின்வரும் மொழிகளில் 1950-ல் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட அசல் 14 மொழிகளில் ஒன்றாக இல்லாதது எது?",
            "options": [
                ("Sindhi", "சிந்தி"),
                ("Kashmiri", "காஷ்மீரி"),
                ("Sanskrit", "சமஸ்கிருதம்"),
                ("Urdu", "உருது")
            ],
            "correct_key": "A",
            "exp_en": "Sindhi was added only in 1967 by the 21st Constitutional Amendment Act. Kashmiri, Sanskrit, and Urdu were all among the original 14 languages listed in the Eighth Schedule in 1950.",
            "exp_ta": "சிந்தி 1967-ல் 21-வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலமே சேர்க்கப்பட்டது. காஷ்மீரி, சமஸ்கிருதம் மற்றும் உருது ஆகிய மூன்றுமே 1950-ல் எட்டாவது அட்டவணையில் பட்டியலிடப்பட்ட அசல் 14 மொழிகளில் இருந்தன.",
            "why_a_en": "Sindhi was the 15th language added in 1967, not in 1950.",
            "why_a_ta": "சிந்தி 1967-ல் சேர்க்கப்பட்ட 15-வது மொழி, 1950-ல் இல்லை.",
            "why_b_en": "Kashmiri was in the original 1950 list.",
            "why_b_ta": "காஷ்மீரி அசல் 1950 பட்டியலில் இருந்தது.",
            "why_c_en": "Sanskrit was in the original 1950 list.",
            "why_c_ta": "சமஸ்கிருதம் அசல் 1950 பட்டியலில் இருந்தது.",
            "why_d_en": "Urdu was in the original 1950 list.",
            "why_d_ta": "உருது அசல் 1950 பட்டியலில் இருந்தது.",
            "tip_en": "Original 14 (1950): Assamese, Bengali, Gujarati, Hindi, Kannada, Kashmiri, Malayalam, Marathi, Odia, Punjabi, Sanskrit, Tamil, Telugu, Urdu.",
            "tip_ta": "அசல் 14 (1950): அசாமி, பெங்காலி, குஜராத்தி, இந்தி, கன்னடம், காஷ்மீரி, மலையாளம், மராத்தி, ஒடியா, பஞ்சாபி, சமஸ்கிருதம், தமிழ், தெலுங்கு, உருது.",
            "fact_en": "Sindhi, Konkani, Manipuri, Nepali, Bodo, Dogri, Maithili, and Santhali were added by amendments.",
            "fact_ta": "சிந்தி, கொங்கணி, மணிப்பூரி, நேபாளி, போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி ஆகியவை திருத்தங்கள் மூலம் சேர்க்கப்பட்டன."
        },
        # 38
        {
            "subtopic": "Article 346 Bilingual Communications in Hindi Belt",
            "stem_en": "When a State in Region A (e.g. Uttar Pradesh) communicates with a State in Region C (e.g. Tamil Nadu), what is required under the Official Languages Rules, 1976?",
            "stem_ta": "மண்டலம் A-ல் உள்ள ஒரு மாநிலம் (எ.கா. உத்தரப் பிரதேசம்) மண்டலம் C-ல் உள்ள ஒரு மாநிலத்துடன் (எ.கா. தமிழ்நாடு) தொடர்புகொள்ளும்போது, அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் கீழ் என்ன தேவைப்படுகிறது?",
            "options": [
                ("The communication shall be in English, or if sent in Hindi, it MUST be accompanied by an authoritative translation in English", "அத்தொடர்பு ஆங்கிலத்தில் இருக்க வேண்டும், அல்லது இந்தியில் அனுப்பப்பட்டால் கட்டாயமாக ஆங்கில மொழிபெயர்ப்புடன் இணைக்கப்பட வேண்டும்"),
                ("The communication must be written exclusively in Tamil", "அத்தொடர்பு கட்டாயமாக தமிழில் மட்டுமே எழுதப்பட வேண்டும்"),
                ("The communication must be in Devanagari Hindi with no translation permitted", "மொழிபெயர்ப்பு எதுவுமின்றி தேவநாகரி இந்தியில் மட்டுமே இருக்க வேண்டும்"),
                ("The communication is barred by law and must go through the Supreme Court", "அத்தகைய தொடர்பு சட்டத்தால் தடைசெய்யப்பட்டு உச்ச நீதிமன்றம் மூலமே செல்ல வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Under Rule 3(4) of the Official Languages Rules, 1976, communications between Region A and Region C must either be in English or, if sent in Hindi, must be accompanied by an authorized translation in English to ensure comprehensibility in non-Hindi recipient states.",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் விதி 3(4)-ன் படி, மண்டலம் A மற்றும் மண்டலம் C-க்கு இடையேயான தகவல்தொடர்புகள் ஆங்கிலத்தில் இருக்க வேண்டும், அல்லது இந்தியில் அனுப்பப்பட்டால், இந்தி பேசாத பெறும் மாநிலத்திற்குப் புரியும் வகையில் அதனுடன் அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு இணைக்கப்பட வேண்டும்.",
            "why_a_en": "Rule 3(4) protects Region C states from receiving unilingual Hindi communications.",
            "why_a_ta": "விதி 3(4) மண்டலம் C மாநிலங்கள் ஒற்றை மொழி இந்திக் கடிதங்களைப் பெறுவதிலிருந்து பாதுகாக்கிறது.",
            "why_b_en": "UP administration is not required to draft in Tamil.",
            "why_b_ta": "உ.பி நிர்வாகம் தமிழில் வரைவு செய்ய வேண்டிய கட்டாயமில்லை.",
            "why_c_en": "Sending Hindi-only letters to Region C violates the 1976 Rules.",
            "why_c_ta": "மண்டலம் C-க்கு இந்தி மட்டும் உள்ள கடிதங்களை அனுப்புவது 1976 விதிகளுக்கு எதிரானது.",
            "why_d_en": "Direct inter-state communication is standard administrative practice.",
            "why_d_ta": "நேரடி மாநிலங்களுக்கிடையேயான தொடர்பு என்பது நிலையான நிர்வாக நடைமுறையாகும்.",
            "tip_en": "Region A to Region C Rule: English or Hindi WITH English translation.",
            "tip_ta": "மண்டலம் A முதல் மண்டலம் C விதி: ஆங்கிலம் அல்லது ஆங்கில மொழிபெயர்ப்புடன் கூடிய இந்தி.",
            "fact_en": "In 2021, the Madurai Bench of Madras High Court reiterated that Central offices cannot send unilingual Hindi replies to Tamil Nadu MPs.",
            "fact_ta": "2021-ல் சென்னை உயர் நீதிமன்றத்தின் மதுரை அமர்வு, தமிழக எம்.பி.க்களுக்கு மத்திய அலுவலகங்கள் இந்தியில் மட்டுமே பதில் அனுப்பக் கூடாது என்பதை மீண்டும் உறுதி செய்தது."
        },
        # 39
        {
            "subtopic": "Languages of Eighth Schedule - Classical Status Chronology",
            "stem_en": "Which of the following correctly pairs each Classical Language with the EXACT year of its declaration?",
            "stem_ta": "பின்வருவனவற்றில் ஒவ்வொரு செம்மொழியையும் அது அறிவிக்கப்பட்ட சரியான ஆண்டுடன் சரியாக இணைக்கும் இணை எது?",
            "options": [
                ("Tamil (2004), Sanskrit (2005), Telugu (2008), Malayalam (2013), Odia (2014)", "தமிழ் (2004), சமஸ்கிருதம் (2005), தெலுங்கு (2008), மலையாளம் (2013), ஒடியா (2014)"),
                ("Tamil (2000), Sanskrit (2002), Telugu (2004), Kannada (2006), Odia (2008)", "தமிழ் (2000), சமஸ்கிருதம் (2002), தெலுங்கு (2004), கன்னடம் (2006), ஒடியா (2008)"),
                ("Sanskrit (2004), Tamil (2005), Malayalam (2008), Telugu (2013), Marathi (2014)", "சமஸ்கிருதம் (2004), தமிழ் (2005), மலையாளம் (2008), தெலுங்கு (2013), மராத்தி (2014)"),
                ("Tamil (2004), Kannada (2005), Sanskrit (2008), Odia (2013), Bengali (2014)", "தமிழ் (2004), கன்னடம் (2005), சமஸ்கிருதம் (2008), ஒடியா (2013), பெங்காலி (2014)")
            ],
            "correct_key": "A",
            "exp_en": "The correct years of declaration are: Tamil (2004), Sanskrit (2005), Telugu and Kannada (2008), Malayalam (2013), and Odia (2014), followed by Marathi, Pali, Prakrit, Assamese, and Bengali (2024).",
            "exp_ta": "அறிவிக்கப்பட்ட சரியான ஆண்டுகள்: தமிழ் (2004), சமஸ்கிருதம் (2005), தெலுங்கு மற்றும் கன்னடம் (2008), மலையாளம் (2013) மற்றும் ஒடியா (2014), தொடர்ந்து மராத்தி, பாலி, பிராகிருதம், அசாமி மற்றும் பெங்காலி (2024).",
            "why_a_en": "Option A lists the exact historical sequence and years for the first six classical languages.",
            "why_a_ta": "விருப்பம் A முதல் ஆறு செம்மொழிகளுக்கான துல்லியமான வரலாற்று வரிசை மற்றும் ஆண்டுகளைப் பட்டியலிடுகிறது.",
            "why_b_en": "Classical status was first created in 2004, not 2000.",
            "why_b_ta": "செம்மொழி அந்தஸ்து முதன்முதலில் 2004-ல் உருவாக்கப்பட்டது, 2000-ல் அல்ல.",
            "why_c_en": "Tamil was first in 2004, not Sanskrit.",
            "why_c_ta": "2004-ல் தமிழே முதலாவதாக அறிவிக்கப்பட்டது, சமஸ்கிருதம் அல்ல.",
            "why_d_en": "Kannada was declared in 2008, not 2005; Sanskrit was 2005.",
            "why_d_ta": "கன்னடம் 2008-ல் அறிவிக்கப்பட்டது, 2005-ல் அல்ல; சமஸ்கிருதம் 2005.",
            "tip_en": "Classical Timeline: 2004 (Tamil) -> 2005 (Sanskrit) -> 2008 (Telugu & Kannada) -> 2013 (Malayalam) -> 2014 (Odia) -> 2024 (5 languages).",
            "tip_ta": "செம்மொழி காலவரிசை: 2004 (தமிழ்) -> 2005 (சமஸ்கிருதம்) -> 2008 (தெலுங்கு & கன்னடம்) -> 2013 (மலையாளம்) -> 2014 (ஒடியா) -> 2024 (5 மொழிகள்).",
            "fact_en": "Tamil's recognition followed decades of sustained advocacy by Tamil scholars like V.G. Suryanarayana Sastri (Parithimar Kalaignar).",
            "fact_ta": "பரிதிமாற் கலைஞர் போன்ற தமிழறிஞர்களின் பல தசாப்த காலத் தொடர் முயற்சிகளுக்குப் பிறகே தமிழ் செம்மொழியாக அங்கீகரிக்கப்பட்டது."
        },
        # 40
        {
            "subtopic": "Languages of Eighth Schedule - Classical Criteria Continuity Discontinuity",
            "stem_en": "What does the Classical Language criterion regarding 'discontinuity between classical language and its later forms' specifically signify?",
            "stem_ta": "'செம்மொழிக்கும் அதன் பிந்தைய வடிவங்களுக்கும் இடையிலான தொடர்ச்சியற்ற தன்மை' தொடர்பான செம்மொழி அளவுகோல் குறிப்பாக எதனைக் குறிக்கிறது?",
            "options": [
                ("Classical language literature possesses a distinct archaic grammar and vocabulary such that its classical form may be distinct from its modern offshoots or dialects", "செவ்வியல் மொழி இலக்கியமானது ஒரு தனித்துவமான தொன்மையான இலக்கணம் மற்றும் சொல்லகராதியைக் கொண்டுள்ளது, இதனால் அதன் செவ்வியல் வடிவம் அதன் நவீன கிளை மொழிகள் அல்லது வழக்குகளிலிருந்து வேறுபட்டிருக்கலாம்"),
                ("The language must have ceased to be spoken completely for at least 1000 years", "அம்மொழி குறைந்தபட்சம் 1000 ஆண்டுகளுக்குப் பேசப்படுவதை முற்றிலுமாக நிறுத்தியிருக்க வேண்டும்"),
                ("The modern script must have no letters in common with the ancient script", "நவீன வரிவடிவம் பண்டைய வரிவடிவத்துடன் எந்த பொதுவான எழுத்துக்களையும் கொண்டிருக்கக் கூடாது"),
                ("The language cannot be used in modern newspapers or radio", "நவீன செய்தித்தாள்கள் அல்லது வானொலியில் அம்மொழி பயன்படுத்தப்பட முடியாது")
            ],
            "correct_key": "A",
            "exp_en": "The criteria state: 'The classical language and literature being distinct from modern, there may also be a discontinuity between the classical language and its later forms or its offshoots.' This distinguishes profound ancient literary classics from modern colloquial evolution.",
            "exp_ta": "அளவுகோல் கூறுகிறது: 'செவ்வியல் மொழியும் இலக்கியமும் நவீன வடிவங்களிலிருந்து வேறுபட்டவை, செவ்வியல் மொழிக்கும் அதன் பிந்தைய வடிவங்களுக்கும் அல்லது அதன் கிளைகளுக்கும் இடையே ஒரு தொடர்ச்சியற்ற தன்மையும் இருக்கலாம்.' இது பண்டைய செவ்வியல் இலக்கியங்களை நவீன பேச்சுவழக்கு வளர்ச்சியிலிருந்து வேறுபடுத்துகிறது.",
            "why_a_en": "This criterion explains why high ancient literature (like Sangam Tamil or Vedic Sanskrit) is distinct from modern colloquial speech.",
            "why_a_ta": "பண்டைய இலக்கியங்கள் (சங்கத் தமிழ் அல்லது வேத சமஸ்கிருதம் போன்றவை) ஏன் நவீன பேச்சுவழக்கிலிருந்து வேறுபடுகின்றன என்பதை இந்த அளவுகோல் விளக்குகிறது.",
            "why_b_en": "Classical languages are not required to be 'dead' or extinct tongues.",
            "why_b_ta": "செம்மொழிகள் 'மறைந்த' அல்லது அழிந்துபோன மொழிகளாக இருக்க வேண்டிய அவசியமில்லை.",
            "why_c_en": "Script evolution does not require total visual discontinuity.",
            "why_c_ta": "வரிவடிவ வளர்ச்சிக்கு முழுமையான காட்சித் துண்டிப்பு தேவையில்லை.",
            "why_d_en": "Living classical languages (like Tamil) flourish in modern digital and print media.",
            "why_d_ta": "வாழும் செம்மொழிகள் (தமிழ் போன்றவை) நவீன ஊடகங்களில் தழைத்தோங்குகின்றன.",
            "tip_en": "Discontinuity Criterion: Classical high literary language is distinct from later colloquial dialects.",
            "tip_ta": "தொடர்ச்சியற்ற தன்மை அளவுகோல்: செவ்வியல் உயர் இலக்கிய மொழி பிந்தைய வட்டார பேச்சுவழக்குகளிலிருந்து வேறுபட்டது.",
            "fact_en": "Tamil is celebrated globally as a living classical language with unbroken literary continuity for over two millennia.",
            "fact_ta": "தமிழ் இரண்டு மில்லினியங்களுக்கும் மேலாக தடையற்ற இலக்கியத் தொடர்ச்சியைக் கொண்ட ஒரு வாழும் செம்மொழியாக உலகளவில் போற்றப்படுகிறது."
        },
        # 41
        {
            "subtopic": "Languages of Eighth Schedule - Konkani Addition Amendment",
            "stem_en": "Along with Konkani and Manipuri, which language spoken in Sikkim and parts of West Bengal was added to the Eighth Schedule by the 71st Constitutional Amendment Act, 1992?",
            "stem_ta": "கொங்கணி மற்றும் மணிப்பூரியுடன் இணைந்து, 1992-ன் 71-வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட, சிக்கிம் மற்றும் மேற்கு வங்கத்தின் சில பகுதிகளில் பேசப்படும் மொழி எது?",
            "options": [
                ("Nepali", "நேபாளி"),
                ("Bhotia", "போட்டியா"),
                ("Lepcha", "லெப்சா"),
                ("Tibetan", "திபெத்தியன்")
            ],
            "correct_key": "A",
            "exp_en": "Nepali was added to the Eighth Schedule alongside Konkani and Manipuri by the 71st Constitutional Amendment Act, 1992, recognizing the prominent Gorkha/Nepali population of Sikkim, Darjeeling, and Assam.",
            "exp_ta": "சிக்கிம், டார்ஜிலிங் மற்றும் அசாமில் உள்ள கூர்க்கா/நேபாளி மக்களின் பிரதிநிதித்துவத்தை அங்கீகரிக்கும் வகையில், 1992-ன் 71-வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் கொங்கணி மற்றும் மணிப்பூரியுடன் நேபாளி எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது.",
            "why_a_en": "Nepali completed the 'KMN' trio added by the 71st Amendment in 1992.",
            "why_a_ta": "நேபாளி 1992-ல் 71-வது திருத்தத்தால் சேர்க்கப்பட்ட 'KMN' மூவர் குழுவை நிறைவு செய்தது.",
            "why_b_en": "Bhotia is not an Eighth Schedule language.",
            "why_b_ta": "போட்டியா எட்டாவது அட்டவணை மொழி அல்ல.",
            "why_c_en": "Lepcha is an official language of Sikkim, but not in the Eighth Schedule.",
            "why_c_ta": "லெப்சா சிக்கிமின் அதிகாரப்பூர்வ மொழி, ஆனால் எட்டாவது அட்டவணையில் இல்லை.",
            "why_d_en": "Tibetan is not an Eighth Schedule language.",
            "why_d_ta": "திபெத்தியன் எட்டாவது அட்டவணை மொழி அல்ல.",
            "tip_en": "71st CAA 1992: Konkani (Goa) + Manipuri (Manipur) + Nepali (Sikkim/Darjeeling).",
            "tip_ta": "71-வது திருத்தம் 1992: கொங்கணி (கோவா) + மணிப்பூரி (மணிப்பூர்) + நேபாளி (சிக்கிம்/டார்ஜிலிங்).",
            "fact_en": "Nepali is also an official cross-border language shared with the sovereign nation of Nepal.",
            "fact_ta": "நேபாளி அண்டை நாடான நேபாளத்துடன் பகிரப்படும் ஓர் அதிகாரப்பூர்வ எல்லையோர மொழியாகவும் உள்ளது."
        },
        # 42
        {
            "subtopic": "Languages of Eighth Schedule - Bodo Language Recognition",
            "stem_en": "The inclusion of Bodo in the Eighth Schedule by the 92nd Constitutional Amendment Act, 2003 was a direct outcome of which historic peace accord?",
            "stem_ta": "2003-ன் 92-வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் போடோ மொழி எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது எந்த வரலாற்றுச் சிறப்புமிக்க அமைதி ஒப்பந்தத்தின் நேரடி விளைவாகும்?",
            "options": [
                ("Bodo Accord of 2003 (Bodoland Territorial Council creation)", "2003 போடோ அமைதி ஒப்பந்தம் (போடோலாந்து பிராந்திய கவுன்சில் உருவாக்கம்)"),
                ("Mizo Peace Accord of 1986", "1986 மிசோ அமைதி ஒப்பந்தம்"),
                ("Assam Accord of 1985", "1985 அசாம் ஒப்பந்தம்"),
                ("Shillong Accord of 1975", "1975 ஷில்லாங் ஒப்பந்தம்")
            ],
            "correct_key": "A",
            "exp_en": "The inclusion of the Bodo language in the Eighth Schedule in 2003 was one of the core commitments fulfilled under the Memorandum of Settlement (Bodo Accord) signed on February 10, 2003 between the Union Government, Assam Government, and Bodo Liberation Tigers.",
            "exp_ta": "2003-ல் எட்டாவது அட்டவணையில் போடோ மொழி சேர்க்கப்பட்டது, 2003 பிப்ரவரி 10 அன்று மத்திய அரசு, அசாம் அரசு மற்றும் போடோ விடுதலைப் புலிகளுக்கு இடையே கையெழுத்தான போடோ அமைதி ஒப்பந்தத்தின் கீழ் நிறைவேற்றப்பட்ட முக்கிய உறுதிமொழிகளில் ஒன்றாகும்.",
            "why_a_en": "The 2003 Bodo Accord directly led to Sixth Schedule amendments and the 92nd Constitutional Amendment.",
            "why_a_ta": "2003 போடோ ஒப்பந்தம் நேரடியாக ஆறாவது அட்டவணைத் திருத்தங்களுக்கும் 92-வது அரசியலமைப்புத் திருத்தத்திற்கும் வழிவகுத்தது.",
            "why_b_en": "Mizo Accord 1986 led to statehood for Mizoram, not Bodo recognition.",
            "why_b_ta": "1986 மிசோ ஒப்பந்தம் மிசோரமிற்கு மாநில அந்தஸ்து வழங்கியது, போடோ அங்கீகாரத்தை அல்ல.",
            "why_c_en": "Assam Accord 1985 dealt with illegal immigration and Clause 6 safeguards.",
            "why_c_ta": "1985 அசாம் ஒப்பந்தம் சட்டவிரோத குடியேற்றம் மற்றும் பிரிவு 6 பாதுகாப்புகளைக் கையாண்டது.",
            "why_d_en": "Shillong Accord 1975 dealt with Naga underground groups.",
            "why_d_ta": "1975 ஷில்லாங் ஒப்பந்தம் நாகா குழுக்களுடன் தொடர்புடையது.",
            "tip_en": "Bodo in 8th Schedule = 92nd CAA 2003 (Direct outcome of 2003 Bodo Accord).",
            "tip_ta": "8-வது அட்டவணையில் போடோ = 92-வது திருத்தம் 2003 (2003 போடோ ஒப்பந்தத்தின் நேரடி விளைவு).",
            "fact_en": "Bodo is written officially in the Devanagari script in Assam.",
            "fact_ta": "போடோ அசாமில் அதிகாரப்பூர்வமாக தேவநாகரி வரிவடிவத்தில் எழுதப்படுகிறது."
        },
        # 43
        {
            "subtopic": "Languages of Eighth Schedule - Santhali Script Adoption",
            "stem_en": "Before the invention and official adoption of the Ol Chiki script, in which multiple scripts was Santhali literature historically written across different States?",
            "stem_ta": "ஒல் சிக்கி வரிவடிவம் உருவாக்கப்பட்டு அதிகாரப்பூர்வமாக ஏற்றுக்கொள்ளப்படுவதற்கு முன்பு, பல்வேறு மாநிலங்களில் சந்தாலி இலக்கியங்கள் வரலாற்று ரீதியாக எந்தெந்த வரிவடிவங்களில் எழுதப்பட்டன?",
            "options": [
                ("Bengali, Odia, Devanagari, and Roman scripts", "பெங்காலி, ஒடியா, தேவநாகரி மற்றும் ரோமன் வரிவடிவங்கள்"),
                ("Sharada, Grantha, and Brahmi scripts", "சாரதா, கிரந்தம் மற்றும் பிராமி வரிவடிவங்கள்"),
                ("Tamil and Malayalam scripts exclusively", "தமிழ் மற்றும் மலையாள வரிவடிவங்கள் மட்டுமே"),
                ("Perso-Arabic script exclusively", "பாரசீக-அரபு வரிவடிவம் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Because the Santhal tribe was geographically divided across West Bengal, Odisha, Bihar, and Assam, Christian missionaries and scholars wrote Santhali in Roman, Bengali, Odia, or Devanagari scripts, until Pandit Raghunath Murmu created the unified Ol Chiki script in 1925.",
            "exp_ta": "சந்தால் பழங்குடியினர் மேற்கு வங்கம், ஒடிசா, பீகார் மற்றும் அசாம் முழுவதும் புவியியல் ரீதியாகப் பிரிக்கப்பட்டிருந்ததால், பண்டிட் ரகுநாத் முர்மு 1925-ல் ஒருங்கிணைந்த ஒல் சிக்கி வரிவடிவத்தை உருவாக்கும் வரை சந்தாலி மொழி ரோமன், பெங்காலி, ஒடியா மற்றும் தேவநாகரி வரிவடிவங்களில் எழுதப்பட்டது.",
            "why_a_en": "Santhali was fragmented across four distinct regional scripts before Ol Chiki unified it.",
            "why_a_ta": "ஒல் சிக்கி ஒருங்கிணைப்பதற்கு முன்பு சந்தாலி நான்கு வெவ்வேறு பிராந்திய வரிவடிவங்களில் பிளவுபட்டிருந்தது.",
            "why_b_en": "Sharada, Grantha, and Brahmi were ancient scripts unrelated to tribal Santhali.",
            "why_b_ta": "சாரதா, கிரந்தம் மற்றும் பிராமி ஆகியவை பழங்குடியின சந்தாலியுடன் தொடர்பில்லாத பண்டைய வரிவடிவங்கள்.",
            "why_c_en": "Southern Dravidian scripts were not used in the Santhal belt.",
            "why_c_ta": "தெற்கு திராவிட வரிவடிவங்கள் சந்தால் பகுதியில் பயன்படுத்தப்படவில்லை.",
            "why_d_en": "Perso-Arabic was not used for Santhali tribal folklore.",
            "why_d_ta": "சந்தாலி பழங்குடி நாட்டுப்புற இலக்கியங்களுக்கு பாரசீக-அரபு பயன்படுத்தப்படவில்லை.",
            "tip_en": "Ol Chiki script resolved the 4-script fragmentation of Santhali (Bengali, Odia, Devanagari, Roman).",
            "tip_ta": "ஒல் சிக்கி வரிவடிவம் சந்தாலியின் 4-வரிவடிவப் பிளவைத் (பெங்காலி, ஒடியா, தேவநாகரி, ரோமன்) தீர்த்து வைத்தது.",
            "fact_en": "President Droupadi Murmu is the first Santhal tribal President of the Republic of India.",
            "fact_ta": "குடியரசுத் தலைவர் திரௌபதி முர்மு இந்தியக் குடியரசின் முதல் சந்தால் பழங்குடியினக் குடியரசுத் தலைவர் ஆவார்."
        },
        # 44
        {
            "subtopic": "Languages of Eighth Schedule - Dogri Script Transition",
            "stem_en": "What is the historical native script of the Dogri language called, which was replaced by Devanagari for official publication?",
            "stem_ta": "அதிகாரப்பூர்வ வெளியீடுகளுக்காக தேவநாகரியால் மாற்றப்பட்ட, டோக்ரி மொழியின் வரலாற்று பூர்வீக வரிவடிவத்தின் பெயர் என்ன?",
            "options": [
                ("Takri (Tankri) script", "தாக்ரி (டாக்ரி) வரிவடிவம்"),
                ("Modi script", "மோடி வரிவடிவம்"),
                ("Sharada script", "சாரதா வரிவடிவம்"),
                ("Kaithi script", "கைதி வரிவடிவம்")
            ],
            "correct_key": "A",
            "exp_en": "The original script of the Dogri language is the Takri (or Tankri) script, a sister script to Gurmukhi and Sharada used historically across Jammu, Himachal Pradesh, and Uttarakhand hill states.",
            "exp_ta": "டோக்ரி மொழியின் அசல் வரிவடிவம் 'தாக்ரி' (அல்லது டாக்ரி) வரிவடிவமாகும், இது ஜம்மு, இமாச்சலப் பிரதேசம் மற்றும் உத்தராகண்ட் மலை மாநிலங்களில் வரலாற்று ரீதியாகப் பயன்படுத்தப்பட்ட குர்முகி மற்றும் சாரதாவின் சகோதரி வரிவடிவமாகும்.",
            "why_a_en": "Takri is the documented indigenous historical script of Dogri.",
            "why_a_ta": "தாக்ரி என்பது டோக்ரி மொழியின் ஆவணப்படுத்தப்பட்ட வரலாற்றுப் பூர்வீக வரிவடிவமாகும்.",
            "why_b_en": "Modi script is the historical cursive script of Marathi.",
            "why_b_ta": "மோடி என்பது மராத்தி மொழியின் வரலாற்று சாய்ந்தெழுத்து வரிவடிவமாகும்.",
            "why_c_en": "Sharada was the ancestral script of Kashmiri, though closely related to Takri.",
            "why_c_ta": "சாரதா காஷ்மீரியின் பூர்வீக வரிவடிவம், இது தாக்ரியுடன் நெருங்கிய தொடர்புடையது.",
            "why_d_en": "Kaithi was used in Bihar and eastern UP.",
            "why_d_ta": "கைதி பீகார் மற்றும் கிழக்கு உ.பியில் பயன்படுத்தப்பட்டது.",
            "tip_en": "Script Matrix: Dogri = Takri; Santhali = Ol Chiki; Maithili = Mithilakshar; Manipuri = Meitei Mayek.",
            "tip_ta": "வரிவடிவ அட்டவணை: டோக்ரி = தாக்ரி; சந்தாலி = ஒல் சிக்கி; மைதிலி = மிதிலாக்சர்; மணிப்பூரி = மெய்தேய் மயேக்.",
            "fact_en": "Dogri literature was revived in the 20th century under the Dogri Sanstha in Jammu.",
            "fact_ta": "ஜம்முவில் உள்ள டோக்ரி சன்ஸ்தா அமைப்பின் கீழ் 20-ஆம் நூற்றாண்டில் டோக்ரி இலக்கியம் புத்துயிர் பெற்றது."
        },
        # 45
        {
            "subtopic": "Languages of Eighth Schedule - Konkani Script Plurality",
            "stem_en": "In how many different scripts is the Konkani language currently written across Goa, Maharashtra, Karnataka, and Kerala?",
            "stem_ta": "கோவா, மகாராஷ்டிரா, கர்நாடகா மற்றும் கேரளா முழுவதும் கொங்கணி மொழி தற்போது எத்தனை வெவ்வேறு வரிவடிவங்களில் எழுதப்படுகிறது?",
            "options": [
                ("Five scripts (Devanagari, Roman, Kannada, Malayalam, and Perso-Arabic)", "ஐந்து வரிவடிவங்கள் (தேவநாகரி, ரோமன், கன்னடம், மலையாளம் மற்றும் பாரசீக-அரபு)"),
                ("Only in Devanagari script exclusively", "தேவநாகரி வரிவடிவத்தில் மட்டுமே"),
                ("Only in Roman script exclusively", "ரோமன் வரிவடிவத்தில் மட்டுமே"),
                ("Two scripts (Tamil and Telugu)", "இரண்டு வரிவடிவங்கள் (தமிழ் மற்றும் தெலுங்கு)")
            ],
            "correct_key": "A",
            "exp_en": "Konkani is famous for its script plurality: it is written in five distinct scripts: Devanagari (official in Goa), Roman/Romi (Catholic community in Goa), Kannada (Karnataka Konkanis), Malayalam (Kochi Konkanis), and Perso-Arabic (Navayath Muslims of Bhatkal).",
            "exp_ta": "கொங்கணி அதன் பன்முக வரிவடிவத்திற்குப் புகழ்பெற்றது: இது ஐந்து வெவ்வேறு வரிவடிவங்களில் எழுதப்படுகிறது: தேவநாகரி (கோவாவில் அதிகாரப்பூர்வமானது), ரோமன் (கோவா கத்தோலிக்க சமூகம்), கன்னடம் (கர்நாடக கொங்கணிகள்), மலையாளம் (கொச்சி கொங்கணிகள்) மற்றும் பாரசீக-அரபு (பட்கல் நவாயத் முஸ்லிம்கள்).",
            "why_a_en": "Konkani has five living scripts across the Western coastal belt of India.",
            "why_a_ta": "இந்தியாவின் மேற்குக் கடற்கரைப் பகுதி முழுவதும் கொங்கணி ஐந்து வாழும் வரிவடிவங்களைக் கொண்டுள்ளது.",
            "why_b_en": "Devanagari is official in Goa, but millions read Konkani in Kannada or Roman script.",
            "why_b_ta": "கோவாவில் தேவநாகரி அதிகாரப்பூர்வமானது, ஆனால் லட்சக்கணக்கானோர் கன்னடம் அல்லது ரோமன் வடிவில் படிக்கின்றனர்.",
            "why_c_en": "Romi Konkani is widespread in Goa, but not the sole script.",
            "why_c_ta": "ரோமி கொங்கணி கோவாவில் பரவலாக உள்ளது, ஆனால் ஒரே வடிவம் அல்ல.",
            "why_d_en": "Tamil and Telugu are not traditional Konkani scripts.",
            "why_d_ta": "தமிழும் தெலுங்கும் பாரம்பரிய கொங்கணி வரிவடிவங்கள் அல்ல.",
            "tip_en": "Konkani: Recognized in 5 scripts! Official state script in Goa = Devanagari (1987 Act).",
            "tip_ta": "கொங்கணி: 5 வரிவடிவங்களில் அங்கீகரிக்கப்பட்டுள்ளது! கோவாவின் அதிகாரப்பூர்வ மாநில வடிவம் = தேவநாகரி.",
            "fact_en": "Sahitya Akademi gives awards in Konkani only for works in the Devanagari script since 1981.",
            "fact_ta": "சாகித்ய அகாதமி 1981 முதல் தேவநாகரி வரிவடிவில் உள்ள படைப்புகளுக்கு மட்டுமே கொங்கணி விருதுகளை வழங்குகிறது."
        },
        # 46
        {
            "subtopic": "Languages of Eighth Schedule - Odia Renaming Distinction",
            "stem_en": "Alongside the 96th Constitutional Amendment Act, 2011 which renamed 'Oriya' to 'Odia' in the Eighth Schedule, which statutory Act was passed to rename the State?",
            "stem_ta": "எட்டாவது அட்டவணையில் 'ஒரியா' என்பதை 'ஒடியா' எனப் பெயர் மாற்றிய 2011-ன் 96-வது அரசியலமைப்புத் திருத்தச் சட்டத்துடன் இணைந்து, மாநிலத்தின் பெயரை மாற்றுவதற்காக இயற்றப்பட்ட சட்டப்பூர்வ சட்டம் எது?",
            "options": [
                ("The Orissa (Alteration of Name) Act, 2011", "ஒரிசா (பெயர் மாற்றம்) சட்டம், 2011"),
                ("The States Reorganisation (Odisha) Act, 2011", "மாநில மறுசீரமைப்பு (ஒடிசா) சட்டம், 2011"),
                ("The Constitution (Ninety-Fifth Amendment) Act, 2010", "அரசியலமைப்பு (தொண்ணூற்று ஐந்தாவது திருத்தச்) சட்டம், 2010"),
                ("The Official Languages (Odisha Amendment) Act, 2011", "அதிகாரப்பூர்வ மொழிகள் (ஒடிசா திருத்தச்) சட்டம், 2011")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 3 of the Constitution, Parliament enacted the Orissa (Alteration of Name) Act, 2011 to change the name of the State from 'Orissa' to 'Odisha', while simultaneously enacting the 96th CAA to change the language entry in the Eighth Schedule from 'Oriya' to 'Odia'.",
            "exp_ta": "அரசியலமைப்பின் சரத்து 3-ன் கீழ், மாநிலத்தின் பெயரை 'ஒரிசா' என்பதிலிருந்து 'ஒடிசா' என மாற்ற நாடாளுமன்றம் ஒரிசா (பெயர் மாற்றம்) சட்டம் 2011-ஐ இயற்றியது; அதே நேரத்தில் எட்டாவது அட்டவணையில் மொழியின் பெயரை 'ஒரியா' என்பதிலிருந்து 'ஒடியா' என மாற்ற 96-வது திருத்தச் சட்டத்தையும் இயற்றியது.",
            "why_a_en": "The Orissa (Alteration of Name) Act, 2011 was the complementary ordinary statutory enactment under Article 3.",
            "why_a_ta": "ஒரிசா (பெயர் மாற்றம்) சட்டம் 2011 என்பது சரத்து 3-ன் கீழான துணைச் சட்டப்பூர்வ சட்டமாகும்.",
            "why_b_en": "States Reorganisation Act was enacted in 1956, not 2011.",
            "why_b_ta": "மாநில மறுசீரமைப்புச் சட்டம் 1956-ல் இயற்றப்பட்டது, 2011-ல் அல்ல.",
            "why_c_en": "The 95th CAA, 2009 extended SC/ST reservations in Parliament, unrelated to Odisha.",
            "why_c_ta": "95-வது திருத்தச் சட்டம், 2009 நாடாளுமன்றத்தில் SC/ST இடஒதுக்கீட்டை நீடித்தது.",
            "why_d_en": "The Official Languages Act of 1963 was not amended for Odisha's name change.",
            "why_d_ta": "1963-ன் அதிகாரப்பூர்வ மொழிகள் சட்டம் ஒடிசா பெயர் மாற்றத்திற்காகத் திருத்தப்படவில்லை.",
            "tip_en": "State name change: Orissa -> Odisha (Art 3 Ordinary Law); Language name change: Oriya -> Odia (96th CAA, 8th Schedule).",
            "tip_ta": "மாநிலப் பெயர் மாற்றம்: ஒரிசா -> ஒடிசா (சரத்து 3 எளிய சட்டம்); மொழிப் பெயர் மாற்றம்: ஒரியா -> ஒடியா (96-வது திருத்தம், 8-வது அட்டவணை).",
            "fact_en": "Both changes came into effect on November 1, 2011.",
            "fact_ta": "இரண்டு மாற்றங்களும் 2011 நவம்பர் 1 அன்று நடைமுறைக்கு வந்தன."
        },
        # 47
        {
            "subtopic": "Languages of Eighth Schedule - Sanskrit Antiquity",
            "stem_en": "What linguistic relationship does Vedic Sanskrit bear to the Indo-European family of languages, supporting its Classical Language recognition?",
            "stem_ta": "சமஸ்கிருதத்தின் செம்மொழி அங்கீகாரத்திற்கு ஆதரவளிக்கும் வகையில், இந்தோ-ஐரோப்பிய மொழிக் குடும்பத்துடன் வேத சமஸ்கிருதம் கொண்டுள்ள மொழியியல் தொடர்பு என்ன?",
            "options": [
                ("It is one of the oldest attested members of the Indo-European language family, preserving archaic phonological and grammatical structures shared with Avestan, Ancient Greek, and Latin", "இது இந்தோ-ஐரோப்பிய மொழிக் குடும்பத்தின் மிகப் பழமையான சான்றளிக்கப்பட்ட உறுப்பினர்களில் ஒன்றாகும், அவெஸ்தான், பண்டைய கிரேக்கம் மற்றும் லத்தீன் மொழிகளுடன் பகிரப்பட்ட தொன்மையான ஒலிப்பியல் மற்றும் இலக்கணக் கட்டமைப்புகளைப் பாதுகாக்கிறது"),
                ("It was invented artificially by Panini in the 4th Century BCE with no prior roots", "இது கி.மு. 4-ஆம் நூற்றாண்டில் பாணினியால் முந்தைய வேர்கள் எதுவுமின்றி செயற்கையாக உருவாக்கப்பட்டது"),
                ("It is a modern creole formed in the 17th century by British orientalists", "இது 17-ஆம் நூற்றாண்டில் பிரிட்டிஷ் கிழக்கத்திய அறிஞர்களால் உருவாக்கப்பட்ட ஒரு நவீன கலப்பு மொழியாகும்"),
                ("It belongs to the Austroasiatic Munda family", "இது ஆஸ்ட்ரோ-ஆசியாடிக் முண்டா குடும்பத்தைச் சேர்ந்தது")
            ],
            "correct_key": "A",
            "exp_en": "Vedic Sanskrit (Rigveda c. 1500 BCE) represents one of the oldest recorded branches of the Indo-European family. Sir William Jones' famous 1786 address highlighted its structural affinity to Greek and Latin, proving its high antiquity and classical status.",
            "exp_ta": "வேத சமஸ்கிருதம் (ரிக்வேதம் கி.மு. 1500) இந்தோ-ஐரோப்பிய குடும்பத்தின் மிகப் பழமையான பதிவு செய்யப்பட்ட கிளைகளில் ஒன்றாகும். சர் வில்லியம் ஜோன்ஸின் புகழ்பெற்ற 1786 உரை, கிரேக்கம் மற்றும் லத்தீன் மொழிகளுடனான அதன் கட்டமைப்பு ஒற்றுமையை எடுத்துரைத்து அதன் பழமையை நிரூபித்தது.",
            "why_a_en": "Sanskrit's antiquity of over 3500 years easily met the 1500-2000 year classical benchmark.",
            "why_a_ta": "சமஸ்கிருதத்தின் 3500 ஆண்டுகளுக்கும் மேலான பழமை 1500-2000 ஆண்டுகால செம்மொழி அளவுகோலை எளிதில் நிறைவு செய்தது.",
            "why_b_en": "Panini standardized classical grammar in Ashtadhyayi, but Vedic Sanskrit existed centuries earlier.",
            "why_b_ta": "பாணினி அஷ்டாத்யாயியில் இலக்கணத்தை முறைப்படுத்தினார், ஆனால் வேத சமஸ்கிருதம் பல நூற்றாண்டுகளுக்கு முன்பே இருந்தது.",
            "why_c_en": "Sanskrit is an ancient indigenous classical tongue, not a modern creole.",
            "why_c_ta": "சமஸ்கிருதம் ஒரு பண்டைய பூர்வீக செவ்வியல் மொழி, நவீன கலப்பு மொழி அல்ல.",
            "why_d_en": "Sanskrit is Indo-Aryan, not Austroasiatic.",
            "why_d_ta": "சமஸ்கிருதம் இந்தோ-ஆரிய மொழி, ஆஸ்ட்ரோ-ஆசியாடிக் அல்ல.",
            "tip_en": "Indo-European Core: Rigvedic Sanskrit + Avestan (Ancient Persian) + Homeric Greek + Classical Latin.",
            "tip_ta": "இந்தோ-ஐரோப்பிய மையம்: ரிக்வேத சமஸ்கிருதம் + அவெஸ்தான் + ஹோமரிக் கிரேக்கம் + கிளாசிக்கல் லத்தீன்.",
            "fact_en": "Sanskrit was declared the second Classical Language of India in 2005.",
            "fact_ta": "2005-ல் சமஸ்கிருதம் இந்தியாவின் இரண்டாவது செம்மொழியாக அறிவிக்கப்பட்டது."
        },
        # 48
        {
            "subtopic": "Article 344(6) Presidential Orders on Language",
            "stem_en": "Under Article 344(6), on what basis is the President empowered to issue directions after the Parliamentary Committee submits its report?",
            "stem_ta": "சரத்து 344(6)-ன் கீழ், நாடாளுமன்றக் குழு தனது அறிக்கையைச் சமர்ப்பித்த பிறகு எதன் அடிப்படையில் வழிகாட்டுதல்களை வெளியிடக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கப்பட்டுள்ளது?",
            "options": [
                ("After consideration of the report of the Committee, the President may issue directions in accordance with the whole or any part of that report", "குழுவின் அறிக்கையைப் பரிசீலித்த பிறகு, அவ்வறிக்கையின் முழுமைக்கும் அல்லது ஏதேனும் ஒரு பகுதிக்கு ஏற்ப குடியரசுத் தலைவர் உத்தரவுகளைப் பிறப்பிக்கலாம்"),
                ("The President must reject all recommendations that mention English", "ஆங்கிலத்தைக் குறிப்பிடும் அனைத்துப் பரிந்துரைகளையும் குடியரசுத் தலைவர் கட்டாயமாக நிராகரிக்க வேண்டும்"),
                ("The President must refer the report to the United Nations General Assembly", "குடியரசுத் தலைவர் அவ்வறிக்கையை ஐக்கிய நாடுகள் பொதுச் சபையின் பார்வைக்கு அனுப்ப வேண்டும்"),
                ("The directions must be ratified by an all-party referendum", "அவ்வழிகாட்டுதல்கள் அனைத்துக் கட்சி பொது வாக்கெடுப்பு மூலம் அங்கீகரிக்கப்பட வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 344(6) states: 'Notwithstanding anything in article 343, the President may, after consideration of the report referred to in clause (5), issue directions in accordance with the whole or any part of that report.'",
            "exp_ta": "சரத்து 344(6) கூறுகிறது: 'சரத்து 343-ல் என்ன கூறப்பட்டிருப்பினும், பிரிவு (5)-ல் குறிப்பிடப்பட்ட குழுவின் அறிக்கையைப் பரிசீலித்த பிறகு, அவ்வறிக்கையின் முழுமைக்கும் அல்லது ஏதேனும் ஒரு பகுதிக்கு ஏற்ப குடியரசுத் தலைவர் உத்தரவுகளைப் பிறப்பிக்கலாம்.'",
            "why_a_en": "Article 344(6) provides the executive mechanism to translate Parliamentary Committee recommendations into binding presidential orders.",
            "why_a_ta": "சரத்து 344(6) நாடாளுமன்றக் குழுவின் பரிந்துரைகளை நடைமுறைக்குரிய குடியரசுத் தலைவர் ஆணைகளாக மாற்றுவதற்கான நிர்வாக வழிமுறையை வழங்குகிறது.",
            "why_b_en": "The President is not mandated to reject recommendations mentioning English.",
            "why_b_ta": "ஆங்கிலத்தைக் குறிப்பிடும் பரிந்துரைகளை குடியரசுத் தலைவர் நிராகரிக்க வேண்டும் என்ற கட்டாயமில்லை.",
            "why_c_en": "UN referral is irrelevant to domestic constitutional governance.",
            "why_c_ta": "உள்நாட்டு அரசியலமைப்பு நிர்வாகத்தில் ஐ.நா குறிப்பு முற்றிலும் தேவையற்றது.",
            "why_d_en": "The Indian Constitution does not provide for popular referendums on policy.",
            "why_d_ta": "இந்திய அரசியலமைப்பு கொள்கைகள் மீதான மக்கள் பொது வாக்கெடுப்புகளுக்கு இடமளிக்கவில்லை.",
            "tip_en": "Presidential Order 1960 was issued under Article 344(6) after reviewing the G.B. Pant Committee report.",
            "tip_ta": "ஜி.பி. பந்த் குழு அறிக்கையை ஆய்வு செய்த பிறகு 1960-ன் குடியரசுத் தலைவர் ஆணை சரத்து 344(6)-ன் கீழ் பிறப்பிக்கப்பட்டது.",
            "fact_en": "President Dr. Rajendra Prasad issued the landmark 1960 Order preparing terminology and training for Hindi.",
            "fact_ta": "குடியரசுத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத் இந்திக்கான கலைச்சொற்கள் மற்றும் பயிற்சிகளைத் தயாரிக்கும் வரலாற்றுச் சிறப்புமிக்க 1960 ஆணையைப் பிறப்பித்தார்."
        },
        # 49
        {
            "subtopic": "Article 350 Grievance Petition Authority",
            "stem_en": "If a citizen in Tamil Nadu submits a petition in Tamil to a Central Government authority in New Delhi under Article 350, can the authority legally reject the petition on the ground that it is not in Hindi or English?",
            "stem_ta": "சரத்து 350-ன் கீழ் தமிழ்நாட்டில் உள்ள ஒரு குடிமகன் புது தில்லியில் உள்ள மத்திய அரசு அதிகாரியிடம் தமிழில் ஒரு மனுவைச் சமர்ப்பித்தால், அது இந்தி அல்லது ஆங்கிலத்தில் இல்லை என்ற காரணத்தைக் கூறி அந்த அதிகாரி சட்டப்பூர்வமாக அம்மனுவை நிராகரிக்க முடியுமா?",
            "options": [
                ("No, because Article 350 confers an absolute constitutional right to submit representations in any language used in the Union or State", "முடியாது, ஏனெனில் சரத்து 350 ஒன்றியம் அல்லது மாநிலத்தில் பயன்பாட்டில் உள்ள எந்த மொழியிலும் மனு அளிக்க முழுமையான அரசியலமைப்பு உரிமையை வழங்குகிறது"),
                ("Yes, because all central offices in New Delhi are governed only by Hindi", "முடியும், ஏனெனில் புது தில்லியில் உள்ள அனைத்து மத்திய அலுவலகங்களும் இந்தியால் மட்டுமே ஆளப்படுகின்றன"),
                ("Yes, unless the citizen pays an official translation penalty", "முடியும், குடிமகன் அதிகாரப்பூர்வ மொழிபெயர்ப்பு அபராதத்தை செலுத்தினாலன்றி"),
                ("Yes, because Article 350 applies only to State officers, not Union officers", "முடியும், ஏனெனில் சரத்து 350 மாநில அதிகாரிகளுக்கு மட்டுமே பொருந்தும், ஒன்றிய அதிகாரிகளுக்கு அல்ல")
            ],
            "correct_key": "A",
            "exp_en": "Article 350 explicitly protects the citizen: 'Every person shall be entitled to submit a representation for the redress of any grievance to any officer or authority of the Union or a State in any of the languages used in the Union or in the State'. The petition cannot be dismissed for language choice.",
            "exp_ta": "சரத்து 350 குடிமகனைத் தெளிவாகப் பாதுகாக்கிறது: 'ஒன்றியம் அல்லது மாநிலத்தில் பயன்படுத்தப்படும் எந்தவொரு மொழியிலும் ஒன்றியம் அல்லது மாநிலத்தின் எந்தவொரு அலுவலர் அல்லது அதிகாரியிடம் குறைகளைத் தீர்ப்பதற்கான மனுவைச் சமர்ப்பிக்க ஒவ்வொரு நபருக்கும் உரிமை உண்டு'. மொழித் தேர்வுக்காக மனுவை நிராகரிக்க முடியாது.",
            "why_a_en": "Article 350 creates an enforceable democratic safeguard against language-based dismissal of citizen grievances.",
            "why_a_ta": "சரத்து 350 மொழி அடிப்படையில் குடிமக்களின் மனுக்களை நிராகரிப்பதற்கு எதிரான சட்டப்பூர்வ ஜனநாயகப் பாதுகாப்பை உருவாக்குகிறது.",
            "why_b_en": "Central offices in New Delhi are bound by Article 350 constitutional supremacy.",
            "why_b_ta": "புது தில்லியில் உள்ள மத்திய அலுவலகங்கள் சரத்து 350-ன் அரசியலமைப்பு மேலாதிக்கத்திற்குக் கட்டுப்பட்டவை.",
            "why_c_en": "There is no translation penalty under the Constitution.",
            "why_c_ta": "அரசியலமைப்பின் கீழ் மொழிபெயர்ப்பு அபராதம் எதுவும் இல்லை.",
            "why_d_en": "Article 350 explicitly covers officers of BOTH the Union and the States.",
            "why_d_ta": "சரத்து 350 வெளிப்படையாக ஒன்றியம் மற்றும் மாநிலங்கள் இரண்டின் அதிகாரிகளையும் உள்ளடக்கியுள்ளது.",
            "tip_en": "Article 350: Covers 'any officer or authority of the Union or a State' -> in 'any language used'.",
            "tip_ta": "சரத்து 350: 'ஒன்றியம் அல்லது மாநிலத்தின் எந்தவொரு அலுவலர்' -> 'பயன்பாட்டில் உள்ள எந்த மொழியிலும்' மனு அளிக்கலாம்.",
            "fact_en": "Central ministries maintain translation units precisely to process regional language petitions received under Article 350.",
            "fact_ta": "மத்திய அமைச்சகங்கள் சரத்து 350-ன் கீழ் பெறப்படும் வட்டார மொழி மனுக்களைக் கையாளவே மொழிபெயர்ப்புப் பிரிவுகளைப் பராமரிக்கின்றன."
        },
        # 50
        {
            "subtopic": "Languages of Eighth Schedule - Classical Languages Matrix Summary",
            "stem_en": "As of 2024, how many total Classical Languages are there in India, and how many of them are listed in the Eighth Schedule of the Constitution?",
            "stem_ta": "2024 நிலவரப்படி, இந்தியாவில் மொத்தம் எத்தனை செம்மொழிகள் உள்ளன, அவற்றில் எத்தனை மொழிகள் அரசியலமைப்பின் எட்டாவது அட்டவணையில் பட்டியலிடப்பட்டுள்ளன?",
            "options": [
                ("Total 11 Classical Languages, of which 9 are in the Eighth Schedule and 2 (Pali and Prakrit) are not", "மொத்தம் 11 செம்மொழிகள், அவற்றில் 9 மொழிகள் எட்டாவது அட்டவணையில் உள்ளன மற்றும் 2 மொழிகள் (பாலி மற்றும் பிராகிருதம்) இல்லை"),
                ("Total 6 Classical Languages, all 6 in the Eighth Schedule", "மொத்தம் 6 செம்மொழிகள், 6 மொழிகளும் எட்டாவது அட்டவணையில் உள்ளன"),
                ("Total 14 Classical Languages, all 14 in the Eighth Schedule", "மொத்தம் 14 செம்மொழிகள், 14 மொழிகளும் எட்டாவது அட்டவணையில் உள்ளன"),
                ("Total 22 Classical Languages, corresponding to the entire Eighth Schedule", "மொத்தம் 22 செம்மொழிகள், முழு எட்டாவது அட்டவணைக்கும் இணையானது")
            ],
            "correct_key": "A",
            "exp_en": "Following the historic Cabinet decision of October 3, 2024, there are 11 Classical Languages: Tamil (2004), Sanskrit (2005), Telugu (2008), Kannada (2008), Malayalam (2013), Odia (2014), Marathi (2024), Pali (2024), Prakrit (2024), Assamese (2024), and Bengali (2024). Nine of these are in the Eighth Schedule, while Pali and Prakrit are non-scheduled languages.",
            "exp_ta": "2024 அக்டோபர் 3-ன் வரலாற்றுச் சிறப்புமிக்க அமைச்சரவை முடிவைத் தொடர்ந்து, 11 செம்மொழிகள் உள்ளன: தமிழ் (2004), சமஸ்கிருதம் (2005), தெலுங்கு (2008), கன்னடம் (2008), மலையாளம் (2013), ஒடியா (2014), மராத்தி (2024), பாலி (2024), பிராகிருதம் (2024), அசாமி (2024) மற்றும் பெங்காலி (2024). இவற்றில் ஒன்பது மொழிகள் எட்டாவது அட்டவணையில் உள்ளன, பாலி மற்றும் பிராகிருதம் அட்டவணையில் இல்லாத மொழிகளாகும்.",
            "why_a_en": "11 total (9 scheduled + 2 non-scheduled) is the authoritative contemporary breakdown.",
            "why_a_ta": "மொத்தம் 11 (9 அட்டவணை மொழிகள் + 2 அட்டவணையில் இல்லாதவை) என்பது துல்லியமான தற்காலப் பகுப்பாகும்.",
            "why_b_en": "6 was the count prior to October 2024.",
            "why_b_ta": "6 என்பது அக்டோபர் 2024-க்கு முந்தைய எண்ணிக்கையாகும்.",
            "why_c_en": "14 is the count of original 1950 Eighth Schedule languages, not classical languages.",
            "why_c_ta": "14 என்பது அசல் 1950 எட்டாவது அட்டவணை மொழிகளின் எண்ணிக்கை, செம்மொழிகள் அல்ல.",
            "why_d_en": "Not all 22 Eighth Schedule languages are classical languages.",
            "why_d_ta": "அனைத்து 22 எட்டாவது அட்டவணை மொழிகளும் செம்மொழிகள் அல்ல.",
            "tip_en": "Memorize: 11 Classical Languages = 6 Original (Tamil, Sanskrit, Telugu, Kannada, Malayalam, Odia) + 5 New in 2024 (Marathi, Pali, Prakrit, Assamese, Bengali).",
            "tip_ta": "நினைவில் கொள்க: 11 செம்மொழிகள் = முந்தைய 6 (தமிழ், சமஸ்கிருதம், தெலுங்கு, கன்னடம், மலையாளம், ஒடியா) + 2024-ல் 5 புதியவை (மராத்தி, பாலி, பிராகிருதம், அசாமி, பெங்காலி).",
            "fact_en": "Tamil was the vanguard that initiated the classical language categorization in India in 2004.",
            "fact_ta": "2004-ல் இந்தியாவில் செம்மொழி வகைப்பாட்டைத் தொடங்கி வைத்த முன்னோடி மொழியாகத் தமிழ் திகழ்கிறது."
        }
    ]

    questions = []
    for idx, item in enumerate(raw_data, start=1):
        qid = f"OL_H_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_ol_q(
            qid=qid,
            diff="Hard",
            qtype="conceptual",
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
            tags=["polity", "official_language", "hard", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_hard_file():
    qs = get_hard_questions()
    print(f"Generated {len(qs)} raw Hard questions for Official Language.")
    balanced = randomize_and_balance_dataset(qs, seed=44)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "official_language_hard.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Hard MCQs to {out_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="OL_H_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid

if __name__ == "__main__":
    build_hard_file()
