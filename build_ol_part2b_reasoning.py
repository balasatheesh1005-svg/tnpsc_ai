# -*- coding: utf-8 -*-
"""
Official Language - Part 2B Reasoning MCQs Generator (25 MCQs: OL_R_001 to OL_R_025)
Strictly adheres to:
- 24 required fields schema
- Assertion (A) and Reason (R) structure
- Authentic Tamil translations
- Specific why_not_others for A, B, C, D
- Balanced answer keys (6-7 per option)
- ContentValidator & Audit pass
"""
import json
import os
from official_language_mcq_helper import make_ol_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_reasoning_questions():
    raw_data = [
        # 1
        {
            "subtopic": "Article 343 Union Language & Script",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Constitution of India declares Hindi in Devanagari script as the official language of the Union.\nReason (R): The Constituent Assembly intended to establish Hindi as the sole national language immediately from 26 January 1950.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): இந்திய அரசியலமைப்பு தேவநாகரி வரிவடிவத்திலான இந்தியை ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியாக அறிவிக்கிறது.\nகாரணம் (R): அரசியலமைப்பு நிர்ணய சபை இந்தியை 26 ஜனவரி 1950 முதல் உடனடியாக ஒரே தேசிய மொழியாக நிலைநிறுத்த விரும்பியது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is true under Article 343(1). Reason (R) is false because the Munshi-Ayyangar formula avoided declaring Hindi as a 'national language' and explicitly provided a 15-year transition period for English.",
            "exp_ta": "சரத்து 343(1)-ன் கீழ் கூற்று (A) உண்மை. காரணம் (R) தவறு, ஏனெனில் முன்ஷி-அய்யங்கார் சமரச சூத்திரம் இந்தியை 'தேசிய மொழி' என அறிவிப்பதைத் தவிர்த்து, ஆங்கிலத்திற்கு 15 ஆண்டு கால இடைக்கால அவகாசத்தை வழங்கியது.",
            "why_a_en": "A is correct per Article 343(1); R is incorrect as English was retained and no 'national language' was declared.",
            "why_a_ta": "சரத்து 343(1)-ன் படி A சரி; ஆங்கிலம் தொடர அனுமதிக்கப்பட்டதாலும் 'தேசிய மொழி' என அறிவிக்கப்படாததாலும் R தவறு.",
            "why_b_en": "R is false because India has no constitutional national language.",
            "why_b_ta": "இந்தியாவிற்கு அரசியலமைப்பு ரீதியான தேசிய மொழி இல்லாததால் R தவறு.",
            "why_c_en": "R is historically and constitutionally false.",
            "why_c_ta": "R வரலாற்று ரீதியாகவும் அரசியலமைப்பு ரீதியாகவும் தவறானது.",
            "why_d_en": "A is true under Article 343(1).",
            "why_d_ta": "சரத்து 343(1)-ன் படி A உண்மை.",
            "tip_en": "Constituent Assembly adopted the 'Munshi-Ayyangar formula' as a compromise.",
            "tip_ta": "அரசியலமைப்பு நிர்ணய சபை ஒரு சமரச முடிவாக 'முன்ஷி-அய்யங்கார் சூத்திரத்தை' ஏற்றுக்கொண்டது.",
            "fact_en": "The term 'Official Language' (Rajbhasha) was deliberately preferred over 'National Language' (Rashtrabhasha).",
            "fact_ta": "'தேசிய மொழி' (ராஷ்டிரபாஷா) என்ற சொல்லுக்குப் பதிலாக 'அதிகாரப்பூர்வ மொழி' (ராஜ்பாஷா) என்ற சொல்லே வேண்டுமென்றே முன்னுரிமை அளிக்கப்பட்டது."
        },
        # 2
        {
            "subtopic": "English Continuance Act 1963",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Parliament enacted the Official Languages Act, 1963 providing for the continued use of English after 26 January 1965.\nReason (R): Article 343(3) of the Constitution empowers Parliament to provide by law for the continued use of English beyond the initial 15-year period.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): 26 ஜனவரி 1965-க்குப் பிறகும் ஆங்கிலத்தின் பயன்பாட்டைத் தொடர வகை செய்யும் அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ஐ நாடாளுமன்றம் இயற்றியது.\nகாரணம் (R): அரசியலமைப்பின் சரத்து 343(3) தொடக்க 15 ஆண்டுகளுக்குப் பிறகும் ஆங்கிலத்தைத் தொடர்ந்து பயன்படுத்த சட்டத்தின் மூலம் ஏற்பாடு செய்ய நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). Parliament exercised its specific constitutional power under Article 343(3) to enact the Official Languages Act 1963, preventing an administrative crisis when the 15-year deadline expired.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். 15 ஆண்டு காலக்கெடு முடிவடையும் போது நிர்வாக முடக்கத்தைத் தடுக்க, சரத்து 343(3)-ன் கீழான குறிப்பிட்ட அரசியலமைப்பு அதிகாரத்தைப் பயன்படுத்தி நாடாளுமன்றம் அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ஐ இயற்றியது.",
            "why_a_en": "R directly provides the constitutional authority for A.",
            "why_a_ta": "A-விற்கான அரசியலமைப்பு அதிகாரத்தை R நேரடியாக வழங்குகிறது.",
            "why_b_en": "R is indeed the direct legal basis and correct explanation of A.",
            "why_b_ta": "R என்பது உண்மையில் A-விற்கான நேரடி சட்ட அடிப்படையாகவும் சரியான விளக்கமாகவும் உள்ளது.",
            "why_c_en": "R is completely true under Article 343(3).",
            "why_c_ta": "சரத்து 343(3)-ன் படி R முற்றிலும் உண்மை.",
            "why_d_en": "A is a historical and statutory fact.",
            "why_d_ta": "A என்பது வரலாற்று மற்றும் சட்டப்பூர்வ உண்மை.",
            "tip_en": "Article 343(3) gave Parliament unlimited discretion regarding English continuation.",
            "tip_ta": "சரத்து 343(3) ஆங்கில நீட்டிப்பு தொடர்பாக நாடாளுமன்றத்திற்கு வரம்பற்ற அதிகாரத்தை வழங்கியது.",
            "fact_en": "Section 3 of the 1963 Act authorized the use of English alongside Hindi for all Union official purposes.",
            "fact_ta": "1963 சட்டத்தின் பிரிவு 3 அனைத்து ஒன்றியப் பணிகளுக்கும் இந்தியுடன் ஆங்கிலத்தையும் பயன்படுத்த அனுமதியளித்தது."
        },
        # 3
        {
            "subtopic": "1967 Amendment Non-Hindi Veto",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Official Languages (Amendment) Act, 1967 gives non-Hindi speaking States a virtual veto power over the discontinuation of English.\nReason (R): Under Section 3(5) of the Act, English cannot be discontinued until resolutions to that effect are passed by the legislatures of all non-Hindi States and by both Houses of Parliament.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அதிகாரப்பூர்வ மொழிகள் (திருத்தச்) சட்டம் 1967 ஆங்கிலத்தை நிறுத்துவது தொடர்பாக இந்தி பேசாத மாநிலங்களுக்கு ஒரு நடைமுறை மறுப்புரிமை (veto) அதிகாரத்தை வழங்குகிறது.\nகாரணம் (R): அச்சட்டத்தின் பிரிவு 3(5)-ன் படி, இந்தி பேசாத அனைத்து மாநிலங்களின் சட்டமன்றங்களும் நாடாளுமன்றத்தின் இரு அவைகளும் அதற்கான தீர்மானங்களை நிறைவேற்றும் வரை ஆங்கிலத்தின் பயன்பாடு நிறுத்தப்பட முடியாது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the exact explanation of (A). Section 3(5) mandates unanimity among all non-Hindi states, meaning even if one state (like Tamil Nadu) refuses to pass the resolution, English cannot be discontinued.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் துல்லியமான விளக்கம். பிரிவு 3(5) இந்தி பேசாத அனைத்து மாநிலங்களின் ஒருமனதான ஒப்புதலைக் கட்டாயமாக்குகிறது; அதாவது தமிழ்நாடு போன்ற ஒரு மாநிலம் தீர்மானம் நிறைவேற்ற மறுத்தாலும் கூட ஆங்கிலத்தை நிறுத்த முடியாது.",
            "why_a_en": "R is the statutory mechanism establishing the veto asserted in A.",
            "why_a_ta": "A-ல் கூறப்பட்டுள்ள மறுப்புரிமையை நிறுவும் சட்டப்பூர்வ பொறிமுறையே R ஆகும்.",
            "why_b_en": "R is the exact reason why non-Hindi states hold a veto.",
            "why_b_ta": "இந்தி பேசாத மாநிலங்கள் மறுப்புரிமை கொண்டிருப்பதற்கான துல்லியமான காரணமே R ஆகும்.",
            "why_c_en": "R is a verbatim statutory provision of the 1967 Amendment.",
            "why_c_ta": "R என்பது 1967 திருத்தச் சட்டத்தின் அசல் சட்டப்பிரிவாகும்.",
            "why_d_en": "A is true as widely recognized in constitutional jurisprudence.",
            "why_d_ta": "அரசியலமைப்புச் சட்டத்தில் பரவலாக அங்கீகரிக்கப்பட்டபடி A உண்மை.",
            "tip_en": "Section 3(5) gave statutory permanence to Jawaharlal Nehru's 1959 assurance in Parliament.",
            "tip_ta": "பிரிவு 3(5) 1959-ல் ஜவஹர்லால் நேரு நாடாளுமன்றத்தில் அளித்த உறுதிமொழிக்கு சட்டப்பூர்வ நிரந்தரத்தை அளித்தது.",
            "fact_en": "Passed under Prime Minister Indira Gandhi following the intense 1965 anti-Hindi agitations in Madras State.",
            "fact_ta": "மதராஸ் மாகாணத்தில் 1965-ல் நடந்த தீவிர இந்தி எதிர்ப்புப் போராட்டங்களைத் தொடர்ந்து பிரதமர் இந்திரா காந்தியால் நிறைவேற்றப்பட்டது."
        },
        # 4
        {
            "subtopic": "Supreme Court Language Monolingualism",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Proceedings in the Supreme Court of India are conducted exclusively in English.\nReason (R): Article 348(1)(a) provides that until Parliament by law otherwise provides, all proceedings in the Supreme Court shall be in the English language.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): இந்திய உச்ச நீதிமன்றத்தின் அனைத்து நடவடிக்கைகளும் ஆங்கிலத்தில் மட்டுமே நடத்தப்படுகின்றன.\nகாரணம் (R): நாடாளுமன்றம் சட்டத்தின் மூலம் வேறு ஏற்பாடு செய்யும் வரை, உச்ச நீதிமன்றத்தின் அனைத்து நடவடிக்கைகளும் ஆங்கில மொழியிலேயே இருக்க வேண்டும் என்று சரத்து 348(1)(a) விதிக்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct constitutional explanation. As Parliament has not enacted any law providing for other languages in the Supreme Court, Article 348(1)(a) continues to mandate English exclusively.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது சரியான அரசியலமைப்பு விளக்கம். உச்ச நீதிமன்றத்தில் பிற மொழிகளைப் பயன்படுத்த நாடாளுமன்றம் எந்தச் சட்டமும் இயற்றாததால், சரத்து 348(1)(a) ஆங்கிலத்தை மட்டுமே தொடர்ந்து கட்டாயமாக்குகிறது.",
            "why_a_en": "R directly quotes Article 348(1)(a) which explains the reality stated in A.",
            "why_a_ta": "A-ல் கூறப்பட்டுள்ள நிலையை விளக்கும் சரத்து 348(1)(a)-வை R நேரடியாக மேற்கோள் காட்டுகிறது.",
            "why_b_en": "R is the direct cause of A.",
            "why_b_ta": "A-விற்கான நேரடிக் காரணம் R ஆகும்.",
            "why_c_en": "R accurately cites the constitutional text.",
            "why_c_ta": "அரசியலமைப்பு உரையை R துல்லியமாக மேற்கோள் காட்டுகிறது.",
            "why_d_en": "A is true; Hindi is not permitted in Supreme Court oral hearings.",
            "why_d_ta": "A உண்மை; உச்ச நீதிமன்ற வாய்மொழி வாதங்களில் இந்தி அனுமதிக்கப்படுவதில்லை.",
            "tip_en": "Unlike High Courts (Art 348(2)), the Supreme Court cannot be granted regional language use by Governor/President consent.",
            "tip_ta": "உயர் நீதிமன்றங்களைப் போலல்லாமல் (சரத்து 348(2)), உச்ச நீதிமன்றத்திற்கு ஆளுநர்/குடியரசுத் தலைவர் ஒப்புதல் மூலம் வட்டார மொழி பயன்பாட்டை வழங்க முடியாது.",
            "fact_en": "Only an Act of Parliament can introduce another language to the Supreme Court.",
            "fact_ta": "நாடாளுமன்றத்தின் சட்டம் மட்டுமே உச்ச நீதிமன்றத்தில் மற்றொரு மொழியை அறிமுகப்படுத்த முடியும்."
        },
        # 5
        {
            "subtopic": "High Court Judgments English Translation Requirement",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Even when a High Court is authorized to deliver judgments in Hindi, an authoritative English translation must accompany them.\nReason (R): Section 7 of the Official Languages Act, 1963 requires an English translation so that judicial precedents remain accessible across the unified national judiciary.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஒரு உயர் நீதிமன்றம் இந்தியில் தீர்ப்புகளை வழங்க அங்கீகரிக்கப்பட்டிருந்தாலும் கூட, அதனுடன் அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு கட்டாயம் இணைக்கப்பட வேண்டும்.\nகாரணம் (R): அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 7, ஒருங்கிணைந்த தேசிய நீதித்துறை முழுவதும் தீர்ப்பு முன்னுதாரணங்கள் பயன்பாட்டில் இருப்பதை உறுதி செய்ய ஆங்கில மொழிபெயர்ப்பைக் கோருகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). Section 7 of the 1963 Act ensures that all High Court rulings can be reviewed by the Supreme Court and cited in other High Courts through the mandatory English text.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். 1963 சட்டத்தின் பிரிவு 7, கட்டாய ஆங்கில உரை மூலம் அனைத்து உயர் நீதிமன்றத் தீர்ப்புகளும் உச்ச நீதிமன்றத்தால் ஆய்வு செய்யப்படுவதையும் பிற உயர் நீதிமன்றங்களில் மேற்கோள் காட்டப்படுவதையும் உறுதி செய்கிறது.",
            "why_a_en": "Section 7 of the 1963 Act mandates English text for pan-Indian judicial coordination.",
            "why_a_ta": "அகில இந்திய நீதித்துறை ஒருங்கிணைப்பிற்காக 1963 சட்டத்தின் பிரிவு 7 ஆங்கில உரையை கட்டாயமாக்குகிறது.",
            "why_b_en": "R is the direct legal reason for A.",
            "why_b_ta": "A-விற்கான நேரடி சட்டப்பூர்வ காரணம் R ஆகும்.",
            "why_c_en": "R is completely true.",
            "why_c_ta": "R முற்றிலும் உண்மை.",
            "why_d_en": "A is statutory law.",
            "why_d_ta": "A என்பது சட்டப்பூர்வ விதியாகும்.",
            "tip_en": "Article 348(2) proviso also provides that judgments, decrees, or orders cannot be in Hindi unless authorized, and Section 7 of 1963 Act mandates the English translation.",
            "tip_ta": "சரத்து 348(2) வரம்புரை தீர்ப்புகள் ஆங்கிலத்தில் இருக்க வேண்டும் என்கிறது, 1963 சட்டத்தின் பிரிவு 7 ஆங்கில மொழிபெயர்ப்பை கட்டாயமாக்குகிறது.",
            "fact_en": "Four High Courts currently use Hindi optionally: Allahabad, Patna, Rajasthan, and Madhya Pradesh.",
            "fact_ta": "அலகாபாத், பாட்னா, ராஜஸ்தான் மற்றும் மத்தியப் பிரதேசம் ஆகிய நான்கு உயர் நீதிமன்றங்கள் தற்போது விருப்பத்தேர்வாக இந்தியைப் பயன்படுத்துகின்றன."
        },
        # 6
        {
            "subtopic": "Tamil Nadu 1976 Rules Exemption",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Official Languages (Use for Official Purposes of the Union) Rules, 1976 do not apply to the State of Tamil Nadu.\nReason (R): Rule 1(2) of the said Rules explicitly excludes Tamil Nadu to honor the state's longstanding Two-Language Policy and anti-imposition consensus.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அதிகாரப்பூர்வ மொழிகள் (ஒன்றியத்தின் அதிகாரப்பூர்வ நோக்கங்களுக்கான பயன்பாடு) விதிகள் 1976 தமிழ்நாடு மாநிலத்திற்குப் பொருந்தாது.\nகாரணம் (R): மாநிலத்தின் நீண்டகால இருமொழிக் கொள்கை மற்றும் இந்தி திணிப்பு எதிர்ப்பு ஒருமித்த கருத்தை மதிக்கும் வகையில் அவ்விதிகளின் விதி 1(2) தமிழ்நாட்டை வெளிப்படையாக விலக்குகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). Under Rule 1(2), Tamil Nadu is the sole Indian state entirely exempted from the 1976 Official Languages Rules, preserving the exclusive use of English in central communications.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். விதி 1(2)-ன் கீழ், 1976 அதிகாரப்பூர்வ மொழி விதிகளிலிருந்து முழுமையாக விலக்களிக்கப்பட்ட ஒரே இந்திய மாநிலம் தமிழ்நாடு மட்டுமே; இது மத்திய அரசுத் தொடர்புகளில் ஆங்கிலத்தின் பயன்பாட்டைப் பாதுகாக்கிறது.",
            "why_a_en": "Rule 1(2) explicitly grants Tamil Nadu exemption due to historical political consensus.",
            "why_a_ta": "வரலாற்று ரீதியான அரசியல் ஒருமித்த கருத்தின் காரணமாக விதி 1(2) வெளிப்படையாக தமிழ்நாட்டிற்கு விலக்கு அளிக்கிறது.",
            "why_b_en": "R is the direct explanation of the exemption in A.",
            "why_b_ta": "A-ல் உள்ள விலக்கின் நேரடி விளக்கம் R ஆகும்.",
            "why_c_en": "R is a legally and historically valid reason.",
            "why_c_ta": "R சட்டப்பூர்வமாகவும் வரலாற்று ரீதியாகவும் செல்லுபடியாகும் காரணமாகும்.",
            "why_d_en": "A is explicitly stated in Rule 1(2).",
            "why_d_ta": "விதி 1(2)-ல் A வெளிப்படையாகக் கூறப்பட்டுள்ளது.",
            "tip_en": "No other State in Region C has a statutory exemption clause like Tamil Nadu.",
            "tip_ta": "பிராந்தியம் C-ல் உள்ள வேறு எந்த மாநிலத்திற்கும் தமிழ்நாடு போன்ற சட்டப்பூர்வ விலக்கு விதி இல்லை.",
            "fact_en": "Central offices in Tamil Nadu are not subjected to the Hindi correspondence quotas prescribed for other regions.",
            "fact_ta": "தமிழ்நாட்டில் உள்ள மத்திய அலுவலகங்கள் பிற பிராந்தியங்களுக்கு நிர்ணயிக்கப்பட்டுள்ள இந்தி கடிதப் போக்குவரத்து ஒதுக்கீடுகளுக்கு உட்பட்டவை அல்ல."
        },
        # 7
        {
            "subtopic": "Tamil Nadu 1968 Two-Language Policy Resolution",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Tamil Nadu Legislative Assembly resolved in 1968 to eliminate Hindi from all schools in the State.\nReason (R): Chief Minister C.N. Annadurai argued that the Three-Language Formula placed non-Hindi students at an unfair structural disadvantage compared to native Hindi speakers.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): 1968-ல் தமிழ்நாடு சட்டமன்றம் மாநிலத்தில் உள்ள அனைத்துப் பள்ளிகளிலிருந்தும் இந்தியை நீக்கத் தீர்மானித்தது.\nகாரணம் (R): மும்மொழிக் கொள்கை தாய்மொழியாக இந்தி பேசுபவர்களுடன் ஒப்பிடும்போது இந்தி பேசாத மாணவர்களுக்கு அநீதியான கட்டமைப்பு குறைபாட்டை ஏற்படுத்துகிறது என்று முதலமைச்சர் சி.என். அண்ணாதுரை வாதிட்டார்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). Annadurai contended that while Hindi speakers studied Hindi, English, and an optional Indian language (rarely practiced), non-Hindi students were burdened with learning two completely foreign languages (Hindi and English).",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். இந்தி பேசுபவர்கள் இந்தி மற்றும் ஆங்கிலம் மட்டுமே படிக்கையில், இந்தி பேசாத மாணவர்கள் இரண்டு புதிய மொழிகளைக் (இந்தி மற்றும் ஆங்கிலம்) கற்கும் கூடுதல் சுமைக்கு ஆளாகிறார்கள் என்று அண்ணா வாதிட்டார்.",
            "why_a_en": "The academic burden and inequality cited in R led directly to the resolution in A.",
            "why_a_ta": "R-ல் கூறப்பட்டுள்ள கல்விச் சுமை மற்றும் சமத்துவமின்மையே A-ல் உள்ள தீர்மானத்திற்கு நேரடிக் காரணமாக அமைந்தது.",
            "why_b_en": "R directly explains the rationale of the policy.",
            "why_b_ta": "கொள்கையின் பின்னணி நியாயத்தை R நேரடியாக விளக்குகிறது.",
            "why_c_en": "R is factually documented in the 1968 Assembly debates.",
            "why_c_ta": "1968 சட்டமன்ற விவாதங்களில் R உண்மையாகப் பதிவு செய்யப்பட்டுள்ளது.",
            "why_d_en": "A is an established historical decision.",
            "why_d_ta": "A என்பது நிறுவப்பட்ட வரலாற்று முடிவாகும்.",
            "tip_en": "Annadurai's famous allegory: 'Why make a big hole for the big cat and a small hole for the small kitten when both can pass through the big hole?' (Big hole = English).",
            "tip_ta": "அண்ணாவின் புகழ்பெற்ற உவமை: 'பெரிய பூனைக்கு ஒரு பெரிய துவாரமும், சிறிய பூனைக்கு ஒரு சிறிய துவாரமும் எதற்கு? பெரிய துவாரத்தின் வழியே இரு பூனைகளும் செல்ல முடியுமே!' (பெரிய துவாரம் = ஆங்கிலம்).",
            "fact_en": "The Two-Language Policy of Tamil Nadu continues uninterrupted across successive DMK and AIADMK governments.",
            "fact_ta": "தமிழ்நாட்டின் இருமொழிக் கொள்கை அடுத்தடுத்த திமுக மற்றும் அதிமுக அரசுகளால் தடையின்றித் தொடர்கிறது."
        },
        # 8
        {
            "subtopic": "Article 350 Grievance Redressal Right",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): A petition for grievance redressal submitted to a Central Government officer in Tamil cannot be rejected on grounds of language.\nReason (R): Article 350 guarantees every person the right to submit a representation in any of the languages used in the Union or State.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மத்திய அரசு அதிகாரியிடம் தமிழில் சமர்ப்பிக்கப்படும் குறைதீர்ப்பு மனுவை மொழி காரணமாக நிராகரிக்க முடியாது.\nகாரணம் (R): சரத்து 350 ஒவ்வொரு நபருக்கும் ஒன்றியம் அல்லது மாநிலத்தில் பயன்பாட்டிலுள்ள எந்தவொரு மொழியிலும் மனு சமர்ப்பிக்கும் உரிமையை உறுதி செய்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the exact constitutional guarantee providing for (A). Article 350 prevents linguistic exclusion in citizen interactions with public authorities.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வை வழங்கும் துல்லியமான அரசியலமைப்பு உத்தரவாதமாகும். சரத்து 350 அரசு அதிகாரிகளுடனான குடிமக்களின் தொடர்பில் மொழிப் புறக்கணிப்பைத் தடுக்கிறது.",
            "why_a_en": "Article 350 in R directly justifies and protects the citizen's right in A.",
            "why_a_ta": "R-ல் உள்ள சரத்து 350, A-ல் உள்ள குடிமகனின் உரிமையை நேரடியாக நியாயப்படுத்திப் பாதுகாக்கிறது.",
            "why_b_en": "R is the exact constitutional foundation for A.",
            "why_b_ta": "A-விற்கான துல்லியமான அரசியலமைப்பு அடித்தளம் R ஆகும்.",
            "why_c_en": "R is verbatim constitutional law.",
            "why_c_ta": "R என்பது அசல் அரசியலமைப்புச் சட்டமாகும்.",
            "why_d_en": "A is correct under Article 350.",
            "why_d_ta": "சரத்து 350-ன் படி A சரியானது.",
            "tip_en": "Citizens cannot be compelled to translate their petitions into Hindi or English before submission.",
            "tip_ta": "மனுக்களை சமர்ப்பிப்பதற்கு முன் அவற்றை இந்தி அல்லது ஆங்கிலத்தில் மொழிபெயர்க்க குடிமக்களைக் கட்டாயப்படுத்த முடியாது.",
            "fact_en": "Article 350 falls under Part XVII Chapter IV (Special Directives).",
            "fact_ta": "சரத்து 350 பகுதி XVII அத்தியாயம் IV-ன் கீழ் (சிறப்பு வழிகாட்டுதல்கள்) வருகிறது."
        },
        # 9
        {
            "subtopic": "Article 350A Linguistic Minorities Mother Tongue",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 350A was inserted by the 7th Constitutional Amendment Act, 1956 to protect linguistic minority children.\nReason (R): The States Reorganisation Commission (1955) recommended constitutional safeguards for linguistic minorities created by the reorganisation of states on a linguistic basis.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மொழிச் சிறுபான்மையினக் குழந்தைகளைப் பாதுகாக்க 1956-ன் 7வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சரத்து 350A சேர்க்கப்பட்டது.\nகாரணம் (R): மொழிவாரி மாநில மறுசீரமைப்பால் உருவான மொழிச் சிறுபான்மையினருக்கு அரசியலமைப்புப் பாதுகாப்புகளை வழங்குமாறு மாநில மறுசீரமைப்பு ஆணையம் (1955) பரிந்துரைத்தது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the historical and policy explanation for (A). The Fazal Ali Commission warned that redrawing state boundaries linguistically would create substantial internal linguistic minorities who needed mother-tongue primary education protections.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-விற்கான வரலாற்று மற்றும் கொள்கை விளக்கமாகும். மாநிலங்களை மொழிவாரியாக மறுசீரமைப்பது கணிசமான உள்ளூர் மொழிச் சிறுபான்மையினரை உருவாக்கும் என்பதால், அவர்களுக்கு தாய்மொழி வழிக் கல்விப் பாதுகாப்பு தேவை என்று பசல் அலி ஆணையம் எச்சரித்தது.",
            "why_a_en": "SRC recommendations directly led to 7th CAA inserting Articles 350A and 350B.",
            "why_a_ta": "மாநில மறுசீரமைப்பு ஆணையப் பரிந்துரைகளே 7வது திருத்தம் மூலம் சரத்துகள் 350A மற்றும் 350B சேர்க்கப்பட நேரடியாக வழிவகுத்தது.",
            "why_b_en": "R is the direct cause of A.",
            "why_b_ta": "A-விற்கான நேரடிக் காரணம் R ஆகும்.",
            "why_c_en": "R is historical fact.",
            "why_c_ta": "R ஒரு வரலாற்று உண்மை.",
            "why_d_en": "A is constitutional law.",
            "why_d_ta": "A அரசியலமைப்புச் சட்டமாகும்.",
            "tip_en": "Both Articles 350A and 350B were added simultaneously by the 7th Amendment in 1956.",
            "tip_ta": "சரத்துகள் 350A மற்றும் 350B ஆகிய இரண்டும் 1956-ன் 7வது திருத்தத்தால் ஒரே நேரத்தில் சேர்க்கப்பட்டன.",
            "fact_en": "Article 350A covers the primary stage of education exclusively.",
            "fact_ta": "சரத்து 350A தொடக்கக் கல்வி நிலையை மட்டுமே உள்ளடக்கியது."
        },
        # 10
        {
            "subtopic": "Article 351 Composite Culture vs Sanskrit Primacy",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 351 directs that the Hindi language should be developed as a medium of expression for all elements of the composite culture of India.\nReason (R): Article 351 mandates that Hindi must draw its vocabulary exclusively from Persian and Arabic without relying on Sanskrit.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): இந்தியாவின் கூட்டுப் பண்பாட்டின் அனைத்துக் கூறுகளையும் வெளிப்படுத்தும் ஊடகமாக இந்தி மொழி உருவாக்கப்பட வேண்டும் என்று சரத்து 351 வழிகாட்டுகிறது.\nகாரணம் (R): இந்தி மொழி தனது சொல்வளத்தை சமஸ்கிருதத்தைச் சாராமல் பாரசீக மற்றும் அரபு மொழிகளிலிருந்து மட்டுமே பெற வேண்டும் என்று சரத்து 351 கட்டாயமாக்குகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is true as per the text of Article 351. Reason (R) is false because Article 351 explicitly mandates that Hindi should draw its vocabulary primarily from Sanskrit, and secondarily from other languages specified in the Eighth Schedule.",
            "exp_ta": "சரத்து 351-ன் வாசகங்களின்படி கூற்று (A) உண்மை. காரணம் (R) தவறு, ஏனெனில் இந்தி தனது சொல்வளத்தை முதன்மையாக சமஸ்கிருதத்திலிருந்தும், இரண்டாம் பட்சமாக எட்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள பிற மொழிகளிலிருந்தும் பெற வேண்டும் என்று சரத்து 351 வெளிப்படையாகக் கூறுகிறது.",
            "why_a_en": "A is true; R is completely opposite to the constitutional text of Article 351.",
            "why_a_ta": "A உண்மை; R சரத்து 351-ன் அரசியலமைப்பு வாசகத்திற்கு முற்றிலும் எதிரானது.",
            "why_b_en": "R is false because Sanskrit is primary, not Persian/Arabic.",
            "why_b_ta": "சமஸ்கிருதமே முதன்மையானது, பாரசீகம்/அரபு அல்ல என்பதால் R தவறு.",
            "why_c_en": "R is factually incorrect.",
            "why_c_ta": "R உண்மைகளின்படி தவறானது.",
            "why_d_en": "A is accurate text of Article 351.",
            "why_d_ta": "சரத்து 351-ன் துல்லியமான உரை A ஆகும்.",
            "tip_en": "Article 351 keyword: 'primarily on Sanskrit and secondarily on other languages'.",
            "tip_ta": "சரத்து 351 முதன்மைச் சொல்: 'முதன்மையாக சமஸ்கிருதம், இரண்டாம் பட்சமாக பிற மொழிகள்'.",
            "fact_en": "Critics pointed out that relying heavily on Sanskrit created a highly artificial, sanskritized register of Hindi.",
            "fact_ta": "சமஸ்கிருதத்தை அதிகமாகச் சார்ந்தது ஒரு செயற்கையான, சமஸ்கிருதமயமாக்கப்பட்ட இந்தி நடையை உருவாக்கியதாக விமர்சகர்கள் சுட்டிக்காட்டினர்."
        },
        # 11
        {
            "subtopic": "Pali and Prakrit Classical Status vs Eighth Schedule",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): In October 2024, Pali and Prakrit were declared Classical Languages by the Union Cabinet.\nReason (R): Any language declared as a Classical Language automatically gets included in the Eighth Schedule of the Constitution of India.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அக்டோபர் 2024-ல் பாலி மற்றும் பிராகிருதம் ஆகிய மொழிகள் மத்திய அமைச்சரவையால் செம்மொழிகளாக அறிவிக்கப்பட்டன.\nகாரணம் (R): செம்மொழியாக அறிவிக்கப்படும் எந்தவொரு மொழியும் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் தானாகவே சேர்க்கப்பட்டுவிடும்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is true; Pali and Prakrit were declared Classical Languages on 3 October 2024. Reason (R) is false because Classical status is an executive classification by the Ministry of Culture, whereas inclusion in the Eighth Schedule requires a Constitutional Amendment Act under Article 368.",
            "exp_ta": "கூற்று (A) உண்மை; 3 அக்டோபர் 2024 அன்று பாலி மற்றும் பிராகிருதம் செம்மொழிகளாக அறிவிக்கப்பட்டன. காரணம் (R) தவறு, ஏனெனில் செம்மொழித் தகுதி என்பது பண்பாட்டு அமைச்சகத்தின் நிர்வாக வகைப்பாடு, ஆனால் எட்டாவது அட்டவணையில் சேர்க்கப்படுவதற்கு சரத்து 368-ன் கீழ் அரசியலமைப்பு திருத்தச் சட்டம் அவசியம்.",
            "why_a_en": "A is true; R is false because classical recognition does not amend the 8th Schedule.",
            "why_a_ta": "A உண்மை; செம்மொழி அங்கீகாரம் 8வது அட்டவணையைத் திருத்தாது என்பதால் R தவறு.",
            "why_b_en": "R is false; there is no automatic constitutional inclusion.",
            "why_b_ta": "தானாக அரசியலமைப்பில் சேர்க்கப்படும் விதி இல்லாததால் R தவறு.",
            "why_c_en": "R is a constitutional misconception.",
            "why_c_ta": "R ஒரு தவறான புரிதல்.",
            "why_d_en": "A is a documented 2024 decision.",
            "why_d_ta": "A என்பது ஆவணப்படுத்தப்பட்ட 2024 முடிவு.",
            "tip_en": "Eighth Schedule currently has 22 languages; Classical Languages are 11. Pali & Prakrit are classical but NOT in 8th Schedule.",
            "tip_ta": "எட்டாவது அட்டவணையில் 22 மொழிகள் உள்ளன; செம்மொழிகள் 11. பாலி & பிராகிருதம் செம்மொழிகள் ஆனால் 8வது அட்டவணையில் இல்லை.",
            "fact_en": "Classical language recognition entitles the language to central research centers and annual international awards.",
            "fact_ta": "செம்மொழி அங்கீகாரம் மத்திய ஆராய்ச்சி மையங்கள் மற்றும் வருடாந்திர சர்வதேச விருதுகளைப் பெற தகுதி அளிக்கிறது."
        },
        # 12
        {
            "subtopic": "English Omission from Eighth Schedule",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): English is the official language of Nagaland, yet it is not included in the Eighth Schedule of the Constitution of India.\nReason (R): Under Article 345, a State Legislature is not restricted to choosing only Eighth Schedule languages as its official language.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஆங்கிலம் நாகாலாந்தின் அதிகாரப்பூர்வ மொழியாக உள்ளது, இருப்பினும் அது இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை.\nகாரணம் (R): சரத்து 345-ன் கீழ், ஒரு மாநில சட்டமன்றம் எட்டாவது அட்டவணை மொழிகளை மட்டுமே தனது அதிகாரப்பூர்வ மொழியாகத் தேர்ந்தெடுக்க வேண்டும் என்ற கட்டுப்பாடு இல்லை.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains why Nagaland could legally choose English without English being in the Eighth Schedule. Article 345 gives plenary power to State legislatures to adopt any language in use.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் ஆங்கிலம் எட்டாவது அட்டவணையில் இல்லாதபோதும் நாகாலாந்து அதை சட்டப்பூர்வமாக எவ்வாறு தேர்வு செய்ய முடிந்தது என்பதை (R) விளக்குகிறது. பயன்பாட்டிலுள்ள எந்த மொழியையும் ஏற்க மாநில சட்டமன்றங்களுக்கு சரத்து 345 முழு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "R provides the legal explanation for how A is constitutionally valid.",
            "why_a_ta": "A அரசியலமைப்பு ரீதியாக எவ்வாறு செல்லுபடியாகும் என்பதற்கான சட்ட விளக்கத்தை R வழங்குகிறது.",
            "why_b_en": "R directly explains the constitutional mechanics behind A.",
            "why_b_ta": "A-ன் பின்னணியில் உள்ள அரசியலமைப்பு இயக்கவியலை R நேரடியாக விளக்குகிறது.",
            "why_c_en": "R is the exact constitutional law under Article 345.",
            "why_c_ta": "சரத்து 345-ன் கீழான துல்லியமான அரசியலமைப்புச் சட்டம் R ஆகும்.",
            "why_d_en": "A is an established fact.",
            "why_d_ta": "A என்பது நிறுவப்பட்ட உண்மை.",
            "tip_en": "Eighth Schedule listing is NOT a prerequisite for a language to become a State's official language.",
            "tip_ta": "ஒரு மொழி ஒரு மாநிலத்தின் அதிகாரப்பூர்வ மொழியாவதற்கு எட்டாவது அட்டவணைப் பதிவு ஒரு முன்நிபந்தனை அல்ல.",
            "fact_en": "Meghalaya, Mizoram, and Arunachal Pradesh also use English extensively in state administration.",
            "fact_ta": "மேகாலயா, மிசோரம் மற்றும் அருணாச்சலப் பிரதேசம் ஆகியவையும் மாநில நிர்வாகத்தில் ஆங்கிலத்தை விரிவாகப் பயன்படுத்துகின்றன."
        },
        # 13
        {
            "subtopic": "National Language Constitutional Myth",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Hindi cannot be legally enforced as the 'National Language' (Rashtrabhasha) of India.\nReason (R): The Constitution of India contains no provision declaring any language as the National Language of the country.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): இந்தியை இந்தியாவின் 'தேசிய மொழி' (ராஷ்டிரபாஷா) என்று சட்டப்பூர்வமாகக் கட்டாயப்படுத்த முடியாது.\nகாரணம் (R): இந்திய அரசியலமைப்பில் எந்தவொரு மொழியையும் நாட்டின் தேசிய மொழியாக அறிவிக்கும் விதி எதுவும் இல்லை.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). The Gujarat High Court in Suresh Kachhadia case (2010) explicitly held that the Constitution merely designated Hindi as an 'Official Language' of the Union, not the 'National Language'.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். சுரேஷ் கச்சாடியா வழக்கில் (2010) குஜராத் உயர் நீதிமன்றம் அரசியலமைப்பு இந்தியை ஒன்றியத்தின் 'அதிகாரப்பூர்வ மொழி' என்றே குறிப்பிட்டுள்ளதே தவிர, 'தேசிய மொழி' என அறிவிக்கவில்லை என்று வெளிப்படையாகத் தீர்ப்பளித்தது.",
            "why_a_en": "R is the constitutional reality that makes A legally correct.",
            "why_a_ta": "A-வை சட்டப்படி சரியானதாக்கும் அரசியலமைப்பு யதார்த்தமே R ஆகும்.",
            "why_b_en": "R is the direct justification for A.",
            "why_b_ta": "A-விற்கான நேரடி நியாயம் R ஆகும்.",
            "why_c_en": "R is factually affirmed by judicial precedent.",
            "why_c_ta": "நீதிமன்றத் தீர்ப்புகளால் R உண்மை என உறுதிப்படுத்தப்பட்டுள்ளது.",
            "why_d_en": "A is legally true.",
            "why_d_ta": "A சட்டப்படி உண்மையானது.",
            "tip_en": "Key takeaway: India has 22 officially scheduled languages, NO national language.",
            "tip_ta": "முக்கிய கருத்து: இந்தியாவில் 22 அட்டவணைப்படுத்தப்பட்ட மொழிகள் உள்ளன, தேசிய மொழி என்று எதுவும் இல்லை.",
            "fact_en": "Article 343 specifically uses the phrase 'The official language of the Union', deliberately omitting the word 'national'.",
            "fact_ta": "சரத்து 343 'ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி' என்ற சொற்றொடரையே குறிப்பாகப் பயன்படுத்துகிறது, 'தேசிய' என்ற சொல்லை வேண்டுமென்றே தவிர்த்துள்ளது."
        },
        # 14
        {
            "subtopic": "Official Language Commission Mandatory Appointment",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The President was constitutionally bound to appoint an Official Language Commission five years after the Constitution's commencement.\nReason (R): Article 344(1) used the mandatory phrase 'The President shall... constitute a Commission' at the expiration of five years and ten years.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அரசியலமைப்பு அமலுக்கு வந்த ஐந்து ஆண்டுகளுக்குப் பிறகு அதிகாரப்பூர்வ மொழி ஆணையத்தை நியமிக்கக் குடியரசுத் தலைவர் அரசியலமைப்பு ரீதியாகக் கடமைப்பட்டிருந்தார்.\nகாரணம் (R): சரத்து 344(1) ஐந்து மற்றும் பத்து ஆண்டுகள் முடிவில் 'குடியரசுத் தலைவர் ஓர் ஆணையத்தை அமைக்க வேண்டும்' (shall constitute) என்ற கட்டாயச் சொற்றொடரைப் பயன்படுத்தியது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). The word 'shall' in Article 344(1) made the appointment of the Commission at the 5-year and 10-year milestones an imperative constitutional obligation, leading to the B.G. Kher Commission in 1955.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்து 344(1)-ல் உள்ள 'shall' (வேண்டும்) என்ற சொல் 5 மற்றும் 10 ஆண்டு மைல்கற்களில் ஆணையத்தை அமைப்பதை ஒரு கட்டாய அரசியலமைப்புக் கடமையாக்கியது; இதுவே 1955-ல் பி.ஜி. கேர் ஆணையம் அமைக்கப்பட வழிவகுத்தது.",
            "why_a_en": "The mandatory wording 'shall' in R created the constitutional duty in A.",
            "why_a_ta": "R-ல் உள்ள கட்டாயச் சொல்லான 'shall' A-ல் உள்ள அரசியலமைப்புக் கடமையை உருவாக்கியது.",
            "why_b_en": "R directly explains why the obligation existed.",
            "why_b_ta": "ஏன் அக்கடமை இருந்தது என்பதை R நேரடியாக விளக்குகிறது.",
            "why_c_en": "R is accurate constitutional text.",
            "why_c_ta": "R துல்லியமான அரசியலமைப்பு வாசகமாகும்.",
            "why_d_en": "A was fulfilled in 1955.",
            "why_d_ta": "A 1955-ல் நிறைவேற்றப்பட்டது.",
            "tip_en": "Contrast: Article 344(1) had 'shall' (mandatory), whereas Article 343(3) gave Parliament enabling discretion ('may').",
            "tip_ta": "வேறுபாடு: சரத்து 344(1) 'shall' (கட்டாயம்) என்ற சொல்லையும், சரத்து 343(3) நாடாளுமன்றத்திற்கு 'may' (விருப்ப அதிகாரம்) என்ற சொல்லையும் பயன்படுத்தியது.",
            "fact_en": "The Kher Commission was appointed on 7 June 1955.",
            "fact_ta": "கேர் ஆணையம் 7 ஜூன் 1955 அன்று நியமிக்கப்பட்டது."
        },
        # 15
        {
            "subtopic": "Section 3(3) Strict Bilingualism",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Central Government tender notices and contracts published solely in Hindi without an English version are legally defective.\nReason (R): Section 3(3) of the Official Languages Act, 1963 makes the concurrent use of both Hindi and English mandatory for specified categories of documents.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஆங்கிலப் பதிப்பு இல்லாமல் இந்தியில் மட்டுமே வெளியிடப்படும் மத்திய அரசின் டெண்டர் அறிவிப்புகளும் ஒப்பந்தங்களும் சட்டப்படி குறைபாடுடையவை.\nகாரணம் (R): அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 3(3), குறிப்பிட்ட வகை ஆவணங்களுக்கு இந்தி மற்றும் ஆங்கிலம் ஆகிய இரண்டையும் ஒரே நேரத்தில் பயன்படுத்துவதைக் கட்டாயமாக்குகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). Section 3(3) mandates that both Hindi and English must be used simultaneously for contracts, tenders, notifications, and general orders. Non-compliance renders the issuance procedurally defective.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். ஒப்பந்தங்கள், டெண்டர்கள், அறிவிக்கைகள் மற்றும் பொது ஆணைகளுக்கு இந்தி மற்றும் ஆங்கிலம் இரண்டும் ஒரே நேரத்தில் பயன்படுத்தப்பட வேண்டும் என்று பிரிவு 3(3) கட்டாயமாக்குகிறது. இதைப் பின்பற்றத் தவறினால் நடைமுறை குறைபாடு ஏற்படும்.",
            "why_a_en": "Section 3(3) in R is the exact statutory provision violated in A.",
            "why_a_ta": "A-ல் மீறப்படும் துல்லியமான சட்டப்பிரிவே R-ல் உள்ள பிரிவு 3(3) ஆகும்.",
            "why_b_en": "R is the direct cause of the defect in A.",
            "why_b_ta": "A-ல் உள்ள குறைபாட்டின் நேரடிக் காரணம் R ஆகும்.",
            "why_c_en": "R is statutory law.",
            "why_c_ta": "R ஒரு சட்டப்பூர்வ விதியாகும்.",
            "why_d_en": "A is legally true.",
            "why_d_ta": "A சட்டப்படி உண்மையானது.",
            "tip_en": "Section 3(3) is an absolute statutory obligation; executive instructions cannot override it.",
            "tip_ta": "பிரிவு 3(3) என்பது ஒரு முழுமையான சட்டப்பூர்வக் கடமையாகும்; நிர்வாக உத்தரவுகள் அதை மீற முடியாது.",
            "fact_en": "Rule 12 of the Official Languages Rules 1976 holds the signing authority personally accountable.",
            "fact_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் விதி 12 கையொப்பமிடும் அதிகாரியை தனிப்பட்ட முறையில் பொறுப்பாக்குகிறது."
        },
        # 16
        {
            "subtopic": "Article 346 Proviso Bilateral Hindi Choice",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Uttar Pradesh and Bihar can lawfully communicate with each other exclusively in Hindi.\nReason (R): The proviso to Article 346 permits two or more States to agree that Hindi shall be the official language for communication between them.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உத்தரப் பிரதேசமும் பீகாரும் தங்களுக்குள் சட்டப்பூர்வமாக இந்தியில் மட்டுமே தொடர்பு கொள்ள முடியும்.\nகாரணம் (R): சரத்து 346-ன் வரம்புரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் தங்களுக்கு இடையேயான தொடர்பாடலுக்கு இந்தி அதிகாரப்பூர்வ மொழியாக இருக்க வேண்டும் என்று உடன்பட அனுமதிக்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the constitutional sanction for (A). While default inter-state communication is in the Union language (with English translation for non-Hindi states), agreeing Hindi states can adopt Hindi under Article 346 proviso.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-விற்கான அரசியலமைப்பு அனுமதியை வழங்குகிறது. இயல்புநிலை மாநிலங்களுக்கிடையேயான தொடர்பு ஒன்றிய மொழியில் இருந்தாலும், ஒப்புக்கொள்ளும் இந்தி மாநிலங்கள் சரத்து 346 வரம்புரையின் கீழ் இந்தியை ஏற்கலாம்.",
            "why_a_en": "The proviso to Article 346 in R directly enables the practice in A.",
            "why_a_ta": "R-ல் உள்ள சரத்து 346-ன் வரம்புரை A-ல் உள்ள நடைமுறையை நேரடியாகச் செயல்படுத்துகிறது.",
            "why_b_en": "R is the direct explanation of A.",
            "why_b_ta": "A-வின் நேரடி விளக்கம் R ஆகும்.",
            "why_c_en": "R is text of Article 346 proviso.",
            "why_c_ta": "R என்பது சரத்து 346 வரம்புரையின் வாசகமாகும்.",
            "why_d_en": "A is constitutionally permissible.",
            "why_d_ta": "A அரசியலமைப்பு ரீதியாக அனுமதிக்கப்பட்டது.",
            "tip_en": "This bilateral freedom cannot be forced upon non-consenting states like Tamil Nadu or West Bengal.",
            "tip_ta": "இந்த இருதரப்பு சுதந்திரத்தை தமிழ்நாடு அல்லது மேற்கு வங்காளம் போன்ற ஒப்புக்கொள்ளாத மாநிலங்கள் மீது திணிக்க முடியாது.",
            "fact_en": "The states of Region A have entered into mutual agreements under this proviso.",
            "fact_ta": "பிராந்தியம் A-வைச் சேர்ந்த மாநிலங்கள் இந்த வரம்புரையின் கீழ் பரஸ்பர ஒப்பந்தங்களைச் செய்துள்ளன."
        },
        # 17
        {
            "subtopic": "Article 347 Presidential Power Context",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The President of India can direct a State Government to recognize Urdu as an official language in certain districts of that State.\nReason (R): Article 347 empowers the President, on demand, to officially recognize a language spoken by a substantial proportion of a State's population throughout the State or any part thereof.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஒரு மாநிலத்தின் குறிப்பிட்ட மாவட்டங்களில் உருதுவை ஓர் அதிகாரப்பூர்வ மொழியாக அங்கீகரிக்குமாறு அம்மாநில அரசுக்கு இந்தியக் குடியரசுத் தலைவர் உத்தரவிட முடியும்.\nகாரணம் (R): ஒரு மாநிலத்தின் மக்கள் தொகையில் கணிசமான பகுதியினரால் பேசப்படும் மொழியை மாநிலம் முழுவதும் அல்லது ஏதேனும் ஒரு பகுதியில் அதிகாரப்பூர்வமாக அங்கீகரிக்குமாறு உத்தரவிட சரத்து 347 குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). Article 347 was specifically designed to protect sizable linguistic minorities from majoritarian neglect by empowering the President to direct official recognition for specific administrative units.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். பெரும்பான்மை ஆதிக்கப் புறக்கணிப்பிலிருந்து கணிசமான மொழிச் சிறுபான்மையினரைப் பாதுகாக்க குறிப்பிட்ட நிர்வாகப் பிரிவுகளுக்கு அதிகாரப்பூர்வ அங்கீகாரம் வழங்க குடியரசுத் தலைவருக்கு அதிகாரமளிக்கும் வகையில் சரத்து 347 வடிவமைக்கப்பட்டது.",
            "why_a_en": "R directly provides the legal power exercised in A.",
            "why_a_ta": "A-ல் பயன்படுத்தப்படும் சட்டப்பூர்வ அதிகாரத்தை R நேரடியாக வழங்குகிறது.",
            "why_b_en": "R is the direct constitutional foundation for A.",
            "why_b_ta": "A-விற்கான நேரடி அரசியலமைப்பு அடித்தளம் R ஆகும்.",
            "why_c_en": "R is verbatim Article 347.",
            "why_c_ta": "R அசல் சரத்து 347 ஆகும்.",
            "why_d_en": "A is constitutionally valid.",
            "why_d_ta": "A அரசியலமைப்பு ரீதியாக செல்லுபடியாகும்.",
            "tip_en": "Keyword: 'substantial proportion of the population' and 'throughout that State or any part thereof'.",
            "tip_ta": "முக்கியச் சொற்கள்: 'மக்கள் தொகையில் கணிசமான பகுதியினர்' மற்றும் 'மாநிலம் முழுவதும் அல்லது ஏதேனும் ஒரு பகுதியில்'.",
            "fact_en": "This power has been invoked to give second official language status to Urdu in parts of UP, Bihar, and Telangana.",
            "fact_ta": "உ.பி, பீகார் மற்றும் தெலுங்கானாவின் சில பகுதிகளில் உருதுவிற்கு இரண்டாவது அதிகாரப்பூர்வ மொழி தகுதியை வழங்க இந்த அதிகாரம் பயன்படுத்தப்பட்டுள்ளது."
        },
        # 18
        {
            "subtopic": "Original 14 Languages vs Sindhi Addition",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Sindhi was not part of the original Eighth Schedule when the Constitution of India commenced in 1950.\nReason (R): The original Eighth Schedule contained only 14 languages, and Sindhi was added 17 years later by the 21st Constitutional Amendment Act, 1967.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): 1950-ல் இந்திய அரசியலமைப்பு அமலுக்கு வந்தபோது சிந்தி மொழி தொடக்க எட்டாவது அட்டவணையின் ஒரு பகுதியாக இருக்கவில்லை.\nகாரணம் (R): தொடக்க எட்டாவது அட்டவணையில் 14 மொழிகள் மட்டுமே இருந்தன, மேலும் சிந்தி 17 ஆண்டுகளுக்குப் பிறகு 1967-ன் 21வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). The 1950 Constitution recognized 14 languages. Following the partition of India and persistent advocacy by Sindhi refugees, the 21st Amendment added Sindhi in 1967.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். 1950 அரசியலமைப்பு 14 மொழிகளை அங்கீகரித்தது. இந்தியப் பிரிவினை மற்றும் சிந்தி மக்களின் தொடர் கோரிக்கைகளைத் தொடர்ந்து 21வது திருத்தம் 1967-ல் சிந்தியைச் சேர்த்தது.",
            "why_a_en": "R explains why Sindhi was not originally in the list and how it was added later.",
            "why_a_ta": "சிந்தி ஏன் தொடக்கத்தில் பட்டியலில் இல்லை மற்றும் பின்னர் எவ்வாறு சேர்க்கப்பட்டது என்பதை R விளக்குகிறது.",
            "why_b_en": "R directly justifies A.",
            "why_b_ta": "A-வை R நேரடியாக நியாயப்படுத்துகிறது.",
            "why_c_en": "R is historically accurate.",
            "why_c_ta": "R வரலாற்று ரீதியாக துல்லியமானது.",
            "why_d_en": "A is fact.",
            "why_d_ta": "A ஒரு உண்மை.",
            "tip_en": "Sindhi has no specific linguistic state in India, unlike Marathi, Gujarati, or Tamil.",
            "tip_ta": "மராத்தி, குஜராத்தி அல்லது தமிழ் போலன்றி இந்தியாவில் சிந்தி மொழிக்கு குறிப்பிட்ட மொழிவாரி மாநிலம் எதுவும் இல்லை.",
            "fact_en": "Sindhi is written in both Arabic-derived Sindhi script and Devanagari script.",
            "fact_ta": "சிந்தி அரபு மூலத்திலிருந்து வந்த சிந்தி வரிவடிவம் மற்றும் தேவநாகரி வரிவடிவம் ஆகிய இரண்டிலும் எழுதப்படுகிறது."
        },
        # 19
        {
            "subtopic": "71st Amendment Konkani Manipuri Nepali",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The 71st Constitutional Amendment Act, 1992 raised the total number of Eighth Schedule languages from 15 to 18.\nReason (R): The 71st Amendment added three languages—Konkani, Manipuri, and Nepali—to the Eighth Schedule.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): 1992-ன் 71வது அரசியலமைப்பு திருத்தச் சட்டம் எட்டாவது அட்டவணை மொழிகளின் மொத்த எண்ணிக்கையை 15-லிருந்து 18 ஆக உயர்த்தியது.\nகாரணம் (R): 71வது திருத்தம் கொங்கணி, மணிப்பூரி மற்றும் நேபாளி ஆகிய மூன்று மொழிகளை எட்டாவது அட்டவணையில் சேர்த்தது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct mathematical and statutory explanation for (A). Adding 3 languages (Konkani, Manipuri, Nepali) to the existing 15 (14 original + Sindhi) made the total 18.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-விற்கான சரியான கணித மற்றும் சட்ட விளக்கமாகும். ஏற்கனவே இருந்த 15 மொழிகளுடன் (14 அசல் + சிந்தி) 3 மொழிகளைச் (கொங்கணி, மணிப்பூரி, நேபாளி) சேர்த்ததன் மூலம் மொத்த எண்ணிக்கை 18 ஆனது.",
            "why_a_en": "Addition of 3 languages in R directly explains the increase from 15 to 18 in A.",
            "why_a_ta": "R-ல் உள்ள 3 மொழிகள் சேர்க்கையே A-ல் உள்ள 15-லிருந்து 18 ஆக அதிகரித்ததை நேரடியாக விளக்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "A-வை R நேரடியாக விளக்குகிறது.",
            "why_c_en": "R is completely true.",
            "why_c_ta": "R முற்றிலும் உண்மை.",
            "why_d_en": "A is factually correct.",
            "why_d_ta": "A உண்மைகளின்படி சரியானது.",
            "tip_en": "Remember the formula: 15 + 3 (71st CAA) = 18.",
            "tip_ta": "சூத்திரத்தை நினைவில் கொள்க: 15 + 3 (71வது திருத்தம்) = 18.",
            "fact_en": "Konkani is the official language of Goa; Manipuri (Meitei) is the official language of Manipur.",
            "fact_ta": "கொங்கணி கோவாவின் அதிகாரப்பூர்வ மொழி; மணிப்பூரி (மெய்தேய்) மணிப்பூரின் அதிகாரப்பூர்வ மொழியாகும்."
        },
        # 20
        {
            "subtopic": "92nd Amendment BDMS Languages",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Santhali is the only tribal language from the Austroasiatic language family included in the Eighth Schedule.\nReason (R): The 92nd Constitutional Amendment Act, 2003 added Bodo, Dogri, Maithili, and Santhali to the Eighth Schedule.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சந்தாலி எட்டாவது அட்டவணையில் சேர்க்கப்பட்டுள்ள ஆஸ்ட்ரோ-ஆசியாட்டிக் மொழிக் குடும்பத்தைச் சேர்ந்த ஒரே பழங்குடியின மொழியாகும்.\nகாரணம் (R): 2003-ன் 92வது அரசியலமைப்பு திருத்தச் சட்டம் போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி ஆகிய மொழிகளை எட்டாவது அட்டவணையில் சேர்த்தது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, but (R) is not the explanation of why Santhali is Austroasiatic. Santhali's linguistic classification is a feature of historical comparative linguistics, whereas its inclusion was an act of Parliament under the 92nd Amendment.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் சந்தாலி ஏன் ஆஸ்ட்ரோ-ஆசியாட்டிக் மொழியாக இருக்கிறது என்பதற்கு (R) விளக்கம் அல்ல. சந்தாலியின் மொழி வகைப்பாடு என்பது வரலாற்று ஒப்பீட்டு மொழியியலின் அம்சம், ஆனால் அதன் சேர்க்கை 92வது திருத்தத்தின் கீழ் நாடாளுமன்றத்தால் செய்யப்பட்ட சட்டமாகும்.",
            "why_a_en": "Both statements are factually true independently, but R does not explain why Santhali belongs to the Austroasiatic family.",
            "why_a_ta": "இரு கூற்றுகளும் தனித்தனியாக உண்மை, ஆனால் சந்தாலி ஏன் ஆஸ்ட்ரோ-ஆசியாட்டிக் குடும்பத்தைச் சேர்ந்தது என்பதை R விளக்கவில்லை.",
            "why_b_en": "Constitutional amendment does not cause a language's genealogical family affiliation.",
            "why_b_ta": "அரசியலமைப்புத் திருத்தம் ஒரு மொழியின் மரபணு மொழிக்குடும்ப இணைப்பை உருவாக்காது.",
            "why_c_en": "R is factually true.",
            "why_c_ta": "R உண்மையானது.",
            "why_d_en": "A is scientifically and constitutionally true.",
            "why_d_ta": "A அறிவியல் ரீதியாகவும் அரசியலமைப்பு ரீதியாகவும் உண்மை.",
            "tip_en": "TNPSC Classic: Distinguish between 'both true and explanation' vs 'both true but NOT explanation'.",
            "tip_ta": "TNPSC சிறப்பு: 'இரண்டும் உண்மை மற்றும் விளக்கம்' என்பதற்கும் 'இரண்டும் உண்மை ஆனால் விளக்கம் அல்ல' என்பதற்கும் இடையிலான வேறுபாட்டைக் கவனியுங்கள்.",
            "fact_en": "Santhali is written in the Ol Chiki script, created by Pandit Raghunath Murmu in 1925.",
            "fact_ta": "சந்தாலி 1925-ல் பண்டிட் ரகுநாத் முர்முவால் உருவாக்கப்பட்ட 'ஒல் சிக்கி' வரிவடிவத்தில் எழுதப்படுகிறது."
        },
        # 21
        {
            "subtopic": "Article 348(1)(b) Language of Bills and Acts",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The authoritative text of all Bills introduced in Parliament must be in the English language.\nReason (R): Article 348(1)(b) provides that all Bills, Acts, ordinances, orders, rules, regulations, and bye-laws issued under the Constitution or by Parliament shall be in English until Parliament provides otherwise.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): நாடாளுமன்றத்தில் அறிமுகப்படுத்தப்படும் அனைத்து மசோதாக்களின் அதிகாரப்பூர்வ உரையும் ஆங்கில மொழியிலேயே இருக்க வேண்டும்.\nகாரணம் (R): நாடாளுமன்றம் வேறுவிதமாக ஏற்பாடு செய்யும் வரை, அரசியலமைப்பின் கீழ் அல்லது நாடாளுமன்றத்தால் வெளியிடப்படும் அனைத்து மசோதாக்கள், சட்டங்கள், அவசரச் சட்டங்கள், ஆணைகள், விதிகள் ஆகியவை ஆங்கிலத்திலேயே இருக்க வேண்டும் என்று சரத்து 348(1)(b) கூறுகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). Under Article 348(1)(b), the authoritative legal text for statutory interpretation by courts is always the English text.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்து 348(1)(b)-ன் கீழ், நீதிமன்றங்களின் சட்ட விளக்கத்திற்கான அதிகாரப்பூர்வ சட்ட உரை எப்போதும் ஆங்கில உரையாகவே இருக்கும்.",
            "why_a_en": "Article 348(1)(b) in R directly mandates the English legal text asserted in A.",
            "why_a_ta": "R-ல் உள்ள சரத்து 348(1)(b) A-ல் கூறப்பட்டுள்ள ஆங்கிலச் சட்ட உரையை நேரடியாகக் கட்டாயமாக்குகிறது.",
            "why_b_en": "R is the direct explanation of A.",
            "why_b_ta": "A-ன் நேரடி விளக்கம் R ஆகும்.",
            "why_c_en": "R is authentic constitutional text.",
            "why_c_ta": "R அசல் அரசியலமைப்பு உரையாகும்.",
            "why_d_en": "A is true under Article 348(1)(b).",
            "why_d_ta": "சரத்து 348(1)(b)-ன் கீழ் A உண்மை.",
            "tip_en": "In case of conflict between Hindi and English texts of an Act of Parliament, the English text prevails.",
            "tip_ta": "நாடாளுமன்றச் சட்டத்தின் இந்தி மற்றும் ஆங்கில உரைகளுக்கு இடையே முரண்பாடு ஏற்பட்டால், ஆங்கில உரையே மேலோங்கும்.",
            "fact_en": "Under Section 5(1) of the Official Languages Act 1963, a Hindi translation is published alongside in the Official Gazette.",
            "fact_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 5(1)-ன் கீழ், அதிகாரப்பூர்வ வர்த்தமானியில் இதனுடன் இந்தி மொழிபெயர்ப்பும் வெளியிடப்படுகிறது."
        },
        # 22
        {
            "subtopic": "First Language Commission vs Parliamentary Committee",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Parliamentary Committee on Official Language constituted in 1957 was chaired by Union Home Minister Govind Ballabh Pant, not B.G. Kher.\nReason (R): B.G. Kher had headed the Official Language Commission appointed in 1955, whereas the 1957 committee was a separate parliamentary body under Article 344(4) to examine Kher's report.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): 1957-ல் அமைக்கப்பட்ட அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழுவிற்கு மத்திய உள்துறை அமைச்சர் கோவிந்த் வல்லப் பந்த் தலைமை தாங்கினார், பி.ஜி. கேர் அல்ல.\nகாரணம் (R): பி.ஜி. கேர் 1955-ல் நியமிக்கப்பட்ட அதிகாரப்பூர்வ மொழி ஆணையத்திற்குத் தலைமை தாங்கினார், அதே நேரத்தில் 1957 குழு என்பது கேரின் அறிக்கையை ஆய்வு செய்வதற்காக சரத்து 344(4)-ன் கீழ் அமைக்கப்பட்ட ஒரு தனி நாடாளுமன்ற அமைப்பாகும்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains the institutional distinction in (A). The 1955 Commission was an executive commission under Art 344(1) headed by Kher; the 1957 Committee was an elected parliamentary body under Art 344(4) chaired by Pant.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-ல் உள்ள நிறுவன ரீதியான வேறுபாட்டை விளக்குகிறது. 1955 ஆணையம் என்பது கேர் தலைமையில் சரத்து 344(1)-ன் கீழான நிர்வாக ஆணையம்; 1957 குழு என்பது பந்த் தலைமையில் சரத்து 344(4)-ன் கீழான தேர்ந்தெடுக்கப்பட்ட நாடாளுமன்ற அமைப்பாகும்.",
            "why_a_en": "R explains the two distinct bodies and their respective heads mentioned in A.",
            "why_a_ta": "A-ல் குறிப்பிடப்பட்டுள்ள இருவேறு அமைப்புகளையும் அவற்றின் தலைவர்களையும் R விளக்குகிறது.",
            "why_b_en": "R directly resolves the distinction.",
            "why_b_ta": "வேறுபாட்டை R நேரடியாகத் தீர்க்கிறது.",
            "why_c_en": "R is factually and constitutionally accurate.",
            "why_c_ta": "R உண்மைகளின்படியும் அரசியலமைப்புப் படியும் துல்லியமானது.",
            "why_d_en": "A is factually correct.",
            "why_d_ta": "A உண்மைகளின்படி சரியானது.",
            "tip_en": "Never confuse the 1955 Commission (Kher) with the 1957 Parliamentary Committee (Pant).",
            "tip_ta": "1955 ஆணையத்தையும் (கேர்) 1957 நாடாளுமன்றக் குழுவையும் (பந்த்) எப்போதும் குழப்பிக் கொள்ளாதீர்கள்.",
            "fact_en": "The Pant Committee consisted of 30 MPs elected by proportional representation.",
            "fact_ta": "பந்த் குழு விகிதாச்சார பிரதிநிதித்துவ முறையில் தேர்ந்தெடுக்கப்பட்ட 30 நாடாளுமன்ற உறுப்பினர்களைக் கொண்டிருந்தது."
        },
        # 23
        {
            "subtopic": "Article 350B Commissioner for Linguistic Minorities Function",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Special Officer for Linguistic Minorities has the power to strike down State executive orders that violate linguistic minority rights.\nReason (R): Under Article 350B, the Special Officer is an investigatory and reporting authority whose findings are submitted to the President, not a judicial court.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மொழிச் சிறுபான்மையினரின் உரிமைகளை மீறும் மாநில நிர்வாக உத்தரவுகளை ரத்து செய்யும் அதிகாரம் மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலருக்கு உண்டு.\nகாரணம் (R): சரத்து 350B-ன் கீழ், சிறப்பு அலுவலர் என்பவர் ஒரு புலனாய்வு மற்றும் அறிக்கை சமர்ப்பிக்கும் அதிகார அமைப்பே தவிர, நீதித்துறை நீதிமன்றம் அல்ல; அவரது கண்டுபிடிப்புகள் குடியரசுத் தலைவரிடமே சமர்ப்பிக்கப்படுகின்றன.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is false because the Special Officer (Commissioner for Linguistic Minorities) has no judicial power to strike down laws or executive orders. Reason (R) is true because Article 350B strictly confines the officer's role to investigating safeguards and submitting reports to the President.",
            "exp_ta": "கூற்று (A) தவறு, ஏனெனில் சட்டங்களையோ அல்லது நிர்வாக உத்தரவுகளையோ ரத்து செய்யும் நீதித்துறை அதிகாரம் சிறப்பு அலுவலருக்கு (மொழிச் சிறுபான்மையினர் ஆணையர்) இல்லை. காரணம் (R) உண்மை, ஏனெனில் சரத்து 350B இவ்வலுவலரின் பணியை பாதுகாப்புகளை ஆய்வு செய்து குடியரசுத் தலைவரிடம் அறிக்கை சமர்ப்பிப்பதோடு மட்டுமே கண்டிப்பாகக் கட்டுப்படுத்துகிறது.",
            "why_a_en": "A is false (no striking-down power); R is true (purely investigative and reporting body).",
            "why_a_ta": "A தவறு (ரத்து செய்யும் அதிகாரம் இல்லை); R உண்மை (வெறும் புலனாய்வு மற்றும் அறிக்கை சமர்ப்பிக்கும் அமைப்பு மட்டுமே).",
            "why_b_en": "A is false, so both cannot be true.",
            "why_b_ta": "A தவறு என்பதால் இரண்டும் உண்மை என்பது பொருந்தாது.",
            "why_c_en": "A is false.",
            "why_c_ta": "A தவறானது.",
            "why_d_en": "A is false and R is true.",
            "why_d_ta": "A தவறு மற்றும் R உண்மை.",
            "tip_en": "Only the Supreme Court (Article 32) and High Courts (Article 226) can strike down unconstitutional state orders.",
            "tip_ta": "உச்ச நீதிமன்றமும் (சரத்து 32) உயர் நீதிமன்றங்களும் (சரத்து 226) மட்டுமே அரசியலமைப்பிற்கு முரணான மாநில உத்தரவுகளை ரத்து செய்ய முடியும்.",
            "fact_en": "The Commissioner for Linguistic Minorities works under the administrative control of the Ministry of Minority Affairs.",
            "fact_ta": "மொழிச் சிறுபான்மையினர் ஆணையர் சிறுபான்மையினர் விவகார அமைச்சகத்தின் நிர்வாகக் கட்டுப்பாட்டின் கீழ் செயல்படுகிறார்."
        },
        # 24
        {
            "subtopic": "Tamil Nadu 1956 Official Language Act",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Tamil was declared the official language of the State of Madras (now Tamil Nadu) in 1956.\nReason (R): Article 345 empowers the State Legislature to adopt by law any one or more of the languages in use in the State for all or any official purposes.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மதராஸ் மாநிலத்தின் (தற்போது தமிழ்நாடு) அதிகாரப்பூர்வ மொழியாக தமிழ் 1956-ல் அறிவிக்கப்பட்டது.\nகாரணம் (R): சரத்து 345 மாநில சட்டமன்றத்திற்கு சட்டத்தின் மூலம் மாநிலத்தில் பயன்பாட்டிலுள்ள ஏதேனும் ஒன்று அல்லது அதற்கு மேற்பட்ட மொழிகளை அதிகாரப்பூர்வ நோக்கங்களுக்காக ஏற்றுக்கொள்ள அதிகாரமளிக்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the constitutional power under which the Madras Official Language Act, 1956 was enacted, formally declaring Tamil as the official language of the State.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது மதராஸ் அதிகாரப்பூர்வ மொழிச் சட்டம் 1956 இயற்றப்பட்டு, தமிழை மாநிலத்தின் அதிகாரப்பூர்வ மொழியாக முறையாக அறிவித்த அரசியலமைப்பு அதிகாரமாகும்.",
            "why_a_en": "Article 345 in R is the direct constitutional authorization for the 1956 State Act in A.",
            "why_a_ta": "R-ல் உள்ள சரத்து 345, A-ல் உள்ள 1956 மாநிலச் சட்டத்திற்கான நேரடி அரசியலமைப்பு அங்கீகாரமாகும்.",
            "why_b_en": "R directly explains the source of authority for A.",
            "why_b_ta": "A-விற்கான அதிகார மூலத்தை R நேரடியாக விளக்குகிறது.",
            "why_c_en": "R is verbatim constitutional text.",
            "why_c_ta": "R அசல் அரசியலமைப்பு உரையாகும்.",
            "why_d_en": "A is a historical statute.",
            "why_d_ta": "A ஒரு வரலாற்றுச் சட்டமாகும்.",
            "tip_en": "Enacted during the Chief Ministership of K. Kamaraj in December 1956 (Act XXXIX of 1956).",
            "tip_ta": "டிசம்பர் 1956-ல் பெருந்தலைவர் காமராஜர் முதலமைச்சராக இருந்தபோது இயற்றப்பட்டது (1956-ன் சட்டம் 39).",
            "fact_en": "Tamil Development Directorate was subsequently created to implement Tamil in administrative drafting.",
            "fact_ta": "நிர்வாக வரைவுகளில் தமிழை நடைமுறைப்படுத்த பின்னர் தமிழ் வளர்ச்சி இயக்ககம் உருவாக்கப்பட்டது."
        },
        # 25
        {
            "subtopic": "Classical Language Status Financial Benefits",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Confertment of Classical Language status upon a language triggers specific institutional and financial support from the Union Government.\nReason (R): Benefits include two major annual international awards for scholars, setting up a Centre of Excellence for Studies in the language, and dedicated professional Chairs in Central Universities.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஒரு மொழிக்கு செம்மொழித் தகுதி வழங்கப்படுவது மத்திய அரசிடமிருந்து குறிப்பிட்ட நிறுவன மற்றும் நிதி ஆதரவைத் தூண்டுகிறது.\nகாரணம் (R): அறிஞர்களுக்கான இரண்டு முக்கிய சர்வதேச வருடாந்திர விருதுகள், மொழி ஆய்வுகளுக்கான சிறப்பு மையம் அமைத்தல் மற்றும் மத்தியப் பல்கலைக்கழகங்களில் பிரத்யேக ஆய்வு இருக்கைகள் அமைத்தல் ஆகியவை இதன் நன்மைகளில் அடங்கும்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) details the exact institutional benefits summarized in (A). The Ministry of Culture and Ministry of Education extend these three specific privileges to every designated Classical Language.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (A)-ல் சுருக்கமாகக் கூறப்பட்டுள்ள துல்லியமான நிறுவன நன்மைகளை (R) விவரிக்கிறது. பண்பாட்டு அமைச்சகம் மற்றும் கல்வி அமைச்சகம் இந்த மூன்று குறிப்பிட்ட சலுகைகளை ஒவ்வொரு செம்மொழிக்கும் வழங்குகின்றன.",
            "why_a_en": "R enumerates the specific central benefits that substantiate the claim in A.",
            "why_a_ta": "A-ல் உள்ள கூற்றை உறுதிப்படுத்தும் குறிப்பிட்ட மத்திய நன்மைகளை R பட்டியலிடுகிறது.",
            "why_b_en": "R is the direct elaboration and justification of A.",
            "why_b_ta": "A-வின் நேரடி விரிவாக்கமும் நியாயப்படுத்தலும் R ஆகும்.",
            "why_c_en": "R is officially notified policy.",
            "why_c_ta": "R அதிகாரப்பூர்வமாக அறிவிக்கப்பட்ட கொள்கையாகும்.",
            "why_d_en": "A is factually correct.",
            "why_d_ta": "A உண்மைகளின்படி சரியானது.",
            "tip_en": "Central Institute of Classical Tamil (CICT) in Chennai is the premier example of this benefit scheme.",
            "tip_ta": "சென்னையில் உள்ள செம்மொழித் தமிழாய்வு மத்திய நிறுவனம் (CICT) இந்த நலத் திட்டத்தின் முதன்மையான எடுத்துக்காட்டாகும்.",
            "fact_en": "Presidential Awards of Classical Languages are conferred annually on distinguished scholars of classical tongues.",
            "fact_ta": "செம்மொழி அறிஞர்களுக்கு ஆண்டுதோறும் மதிப்புமிக்க குடியரசுத் தலைவர் விருதுகள் வழங்கப்படுகின்றன."
        }
    ]

    questions = []
    for idx, item in enumerate(raw_data, start=1):
        qid = f"OL_R_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        
        q = make_ol_q(
            qid=qid,
            diff="Medium" if idx <= 15 else "Hard",
            qtype="Assertion and Reason",
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
            tags=["polity", "official_language", "reasoning", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_reasoning_file():
    qs = get_reasoning_questions()
    print(f"Generated {len(qs)} raw Reasoning questions for Official Language.")
    balanced = randomize_and_balance_dataset(qs, seed=52)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "official_language_reasoning.json")
    alias_path = os.path.join(out_dir, "official_language_assertion_reason.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Reasoning MCQs to {out_path} and alias {alias_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=25, expected_prefix="OL_R_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid

if __name__ == "__main__":
    build_reasoning_file()
