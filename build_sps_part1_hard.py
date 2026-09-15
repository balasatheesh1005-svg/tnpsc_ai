# -*- coding: utf-8 -*-
"""
Special Provisions for States - Part 1 Hard MCQs Generator (50 MCQs: SPS_H_001 to SPS_H_050)
TNPSC Nova AI Content Engine
"""
import json
import os
from special_provisions_states_mcq_helper import make_sps_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_hard_questions():
    raw = [
        # 1
        {
            "subtopic": "P. Sambamurthy Case Article 371D(5)",
            "stem_en": "In P. Sambamurthy v. State of Andhra Pradesh (1987), the Supreme Court struck down clause (5) of Article 371D as unconstitutional primarily on the grounds that:",
            "stem_ta": "பி. சாம்பமூர்த்தி எதிர் ஆந்திரப் பிரதேச அரசு (1987) வழக்கில், உச்ச நீதிமன்றம் சரத்து 371D-ன் உட்பிரிவு (5)-ஐ அரசியலமைப்பிற்கு முரணானது என ரத்து செய்ததற்கான முதன்மைக் காரணம் என்ன?",
            "options": [
                ("It conferred arbitrary power on the State Government to modify or annul orders of the Administrative Tribunal, violating the rule of law and judicial review as part of the Basic Structure", "நிர்வாகத் தீர்ப்பாயத்தின் உத்தரவுகளை மாற்றியமைக்க அல்லது ரத்து செய்ய மாநில அரசுக்கு தன்னிச்சையான அதிகாரத்தை வழங்கி, அடிப்படை அமைப்பின் பகுதியான சட்டத்தின் ஆட்சி மற்றும் நீதித்துறை மறுஆய்வை அது மீறியது"),
                ("It failed to provide 27 percent reservation for Other Backward Classes in the state", "மாநிலத்தில் இதர பிற்படுத்தப்பட்ட வகுப்பினருக்கு 27 சதவீத இடஒதுக்கீட்டை வழங்கத் தவறியது"),
                ("It was not ratified by half of the State Legislatures under Article 368", "சரத்து 368-ன் கீழ் பாதிக்கும் மேற்பட்ட மாநில சட்டமன்றங்களால் அது அங்கீகரிக்கப்படவில்லை"),
                ("It unlawfully transferred judicial powers from the District Munsif Courts to the Governor", "மாவட்ட முன்சீப் நீதிமன்றங்களிலிருந்து நீதித்துறை அதிகாரங்களை ஆளுநருக்கு சட்டவிரோதமாக மாற்றியது")
            ],
            "correct_key": "A",
            "exp_en": "In P. Sambamurthy (1987), the Constitution Bench struck down Article 371D(5) and its proviso, which had empowered the AP Government to modify or annul an order of the Administrative Tribunal before it became effective. The Court held that making the executive the judge of its own cause and nullifying judicial orders strikes at the root of the rule of law and judicial review, which are basic structure features.",
            "exp_ta": "சாம்பமூர்த்தி வழக்கில் (1987), நிர்வாகத் தீர்ப்பாயத்தின் உத்தரவை நடைமுறைக்கு வருவதற்கு முன்பே மாற்ற அல்லது ரத்து செய்ய ஆந்திர அரசுக்கு அதிகாரமளித்த சரத்து 371D(5)-ஐ உச்ச நீதிமன்றம் ரத்து செய்தது. நிர்வாகமே தனது வழக்கிற்கு நீதிபதியாக இருப்பதும் நீதிமன்ற உத்தரவுகளை ரத்து செய்வதும் அடிப்படை அமைப்பின் அம்சங்களான சட்டத்தின் ஆட்சி மற்றும் நீதித்துறை மறுஆய்வை பாதிக்கிறது என நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "Article 371D(5) violated the Basic Structure by making administrative orders subject to executive veto, violating judicial review.",
            "why_a_ta": "நீதிமன்ற உத்தரவுகளை ரத்து செய்யும் நிர்வாக வீடோ அதிகாரம் நீதித்துறை மறுஆய்வு மற்றும் அடிப்படை அமைப்பை மீறியது.",
            "why_b_en": "OBC reservation was not an issue in Sambamurthy.",
            "why_b_ta": "OBC இடஒதுக்கீடு சாம்பமூர்த்தி வழக்கின் விவகாரம் அல்ல.",
            "why_c_en": "Ratification under Art 368 was not the constitutional defect identified by the Court.",
            "why_c_ta": "மாநிலங்களின் ஒப்புதல் இன்மை என்பது நீதிமன்றம் சுட்டிக்காட்டிய குறைபாடு அல்ல.",
            "why_d_en": "Munsif court powers were not the subject of the clause.",
            "why_d_ta": "முன்சீப் நீதிமன்ற அதிகாரங்கள் இச்சரத்தின் பாடுபொருள் அல்ல.",
            "tip_en": "Sambamurthy established that even a constitutional amendment cannot subordinate an administrative court's orders to executive discretion.",
            "tip_ta": "ஓர் அரசியலமைப்புத் திருத்தத்தால்கூட தீர்ப்பாய உத்தரவுகளை நிர்வாகத்தின் விருப்பத்திற்குக் கீழ்ப்படுத்த முடியாது என்பதை சாம்பமூர்த்தி வழக்கு நிறுவியது.",
            "fact_en": "Clause (3) establishing the tribunal was upheld, while only clause (5) containing the executive veto was severed and invalidated.",
            "fact_ta": "தீர்ப்பாயத்தை அமைத்த உட்பிரிவு (3) உறுதி செய்யப்பட்டது, நிர்வாக வீட்டோ அதிகாரத்தைக் கொண்டிருந்த உட்பிரிவு (5) மட்டுமே நீக்கப்பட்டு ரத்து செய்யப்பட்டது."
        },
        # 2
        {
            "subtopic": "R.C. Poudyal Case Article 371F",
            "stem_en": "In R.C. Poudyal v. Union of India (1993), the challenge to the reservation of 12 seats for Bhutia-Lepchas and 1 seat for the Sangha in the Sikkim Assembly under Article 371F(f) was rejected by the Supreme Court because:",
            "stem_ta": "ஆர்.சி. பௌடியால் எதிர் இந்திய ஒன்றியம் (1993) வழக்கில், சரத்து 371F(f)-ன் கீழ் சிக்கிம் சட்டமன்றத்தில் பூட்டியா-லெப்சாக்களுக்கு 12 இடங்களும் சங்கத்திற்கு 1 இடமும் ஒதுக்கப்பட்டதை எதிர்த்த மனுவை உச்ச நீதிமன்றம் நிராகரித்ததன் காரணம் என்ன?",
            "options": [
                ("Historical compacts, treaty conditions of merger, and the unique political identity of indigenous inhabitants justify differential treatment within asymmetrical federalism", "வரலாற்று ஒப்பந்தங்கள், இணைப்பின் போதான ஒப்பந்த நிபந்தனைகள் மற்றும் பூர்வீக மக்களின் தனித்துவமான அரசியல் அடையாளம் ஆகியவை சமச்சீரற்ற கூட்டாட்சிக்குள் இவ்வேறுபாட்டை நியாயப்படுத்துகின்றன"),
                ("The Sangha seat was declared to be an absolute military requirement for Himalayan border defense", "இமயமலை எல்லைப் பாதுகாப்பிற்கான முழுமையான ராணுவத் தேவை என சங்கத் தொகுதி அறிவிக்கப்பட்டது"),
                ("Sikkim was exempted from the application of all Fundamental Rights under Article 371F", "சரத்து 371F-ன் கீழ் சிக்கிமிற்கு அனைத்து அடிப்படை உரிமைகளும் பொருந்துவதிலிருந்து விலக்களிக்கப்பட்டது"),
                ("The Chogyal had absolute hereditary authority to permanently dictate legislative quotas under international law", "சர்வதேச சட்டத்தின் கீழ் சட்டமன்ற ஒதுக்கீடுகளை நிரந்தரமாக நிர்ணயிக்க சோக்யாலுக்கு முழுமையான பரம்பரை அதிகாரம் இருந்தது")
            ],
            "correct_key": "A",
            "exp_en": "In R.C. Poudyal (1993), the Supreme Court ruled that Article 371F is a special provision facilitating the accession of a new territory with unique historical and political conditions. The reservation for Bhutia-Lepchas and the Buddhist Sangha was based on historical treaties and did not violate democracy or secularism, as the Sangha represented an indigenous social institution rather than a purely religious establishment.",
            "exp_ta": "பௌடியால் வழக்கில் (1993), புதிய பகுதியை இணைப்பதற்காக வரலாற்று மற்றும் அரசியல் நிலைமைகளுக்கு ஏற்ப உருவாக்கப்பட்ட சிறப்பு ஏற்பாடே சரத்து 371F என உச்ச நீதிமன்றம் கூறியது. பூட்டியா-லெப்சா மற்றும் பௌத்த சங்கத்திற்கான இடஒதுக்கீடு வரலாற்று ஒப்பந்தங்களை அடிப்படையாகக் கொண்டது; சங்கம் என்பது வெறும் மத அமைப்பு அல்லாமல் ஒரு பூர்வீக சமூக நிறுவனமாக இருந்ததால் இது ஜனநாயகம் அல்லது மதச்சார்பின்மையை மீறவில்லை.",
            "why_a_en": "The Supreme Court validated the historical and treaty basis of Sikkim's unique seat reservations.",
            "why_a_ta": "சிக்கிமின் தனித்துவமான இடஒதுக்கீட்டின் வரலாற்று மற்றும் ஒப்பந்த அடிப்படையை உச்ச நீதிமன்றம் உறுதி செய்தது.",
            "why_b_en": "The Sangha seat is religious-cultural, not a military defense requirement.",
            "why_b_ta": "சங்கத் தொகுதி என்பது மத-கலாச்சார அடிப்படையிலானது, ராணுவப் பாதுகாப்புத் தேவை அல்ல.",
            "why_c_en": "Fundamental rights apply to Sikkim; Article 371F does not suspend Part III.",
            "why_c_ta": "அடிப்படை உரிமைகள் சிக்கிமிற்குப் பொருந்தும்; பகுதி III இடைநிறுத்தப்படவில்லை.",
            "why_d_en": "The Chogyal's monarchy was abolished upon integration in 1975.",
            "why_d_ta": "1975 இணைப்பின் போது சோக்யாலின் முடியாட்சி ஒழிக்கப்பட்டது.",
            "tip_en": "R.C. Poudyal is the leading authority on how Article 2 (admission of new states) interacts with Article 371F.",
            "tip_ta": "புதிய மாநிலங்களை இணைக்கும் சரத்து 2, சரத்து 371F உடன் எவ்வாறு தொடர்பு கொள்கிறது என்பதற்கான முன்னணி தீர்ப்பு பௌடியால் வழக்காகும்.",
            "fact_en": "Justice L.M. Sharma delivered a dissenting opinion, arguing that the Sangha seat violated secularism, but the majority upheld it.",
            "fact_ta": "நீதிபதி எல்.எம். சர்மா சங்கத் தொகுதி மதச்சார்பின்மையை மீறுவதாக மாறுபட்ட தீர்ப்பளித்தார், ஆனால் பெரும்பான்மை அமர்வு அதை உறுதி செய்தது."
        },
        # 3
        {
            "subtopic": "Sub-classification of SCs/STs 2024",
            "stem_en": "In the landmark 7-judge Constitution Bench judgment in State of Punjab v. Davinder Singh (2024), the Supreme Court ruled that:",
            "stem_ta": "பஞ்சாப் அரசு எதிர் தேவிந்தர் சிங் (2024) என்ற வரலாற்று சிறப்புமிக்க 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு தீர்ப்பில் உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "options": [
                ("States have the constitutional authority to sub-classify Scheduled Castes and Scheduled Tribes for granting preferential reservation, provided it is based on quantifiable data and the Creamy Layer is excluded", "அளவிடக்கூடிய தரவுகளின் அடிப்படையிலும் கிரீமி லேயர் விலக்கப்படுவதற்கு உட்பட்டும், முன்னுரிமை இடஒதுக்கீடு வழங்குவதற்காக SC மற்றும் ST பிரிவினருக்குள் உட்பிரிவுகளை உருவாக்க மாநிலங்களுக்கு அரசியலமைப்பு அதிகாரம் உண்டு"),
                ("Scheduled Castes form a monolithic, indivisible whole that can never be sub-classified by any authority under any circumstances", "பட்டியலிடப்பட்ட சாதியினர் பிரிக்க முடியாத ஒரே தொகுதியாகும், அவர்களை எந்த சூழ்நிலையிலும் எந்த அதிகார அமைப்பும் உட்பிரிவு செய்ய முடியாது"),
                ("The power of sub-classification belongs exclusively to the Chief Justice of India", "உட்பிரிவு செய்யும் அதிகாரம் இந்தியத் தலைமை நீதிபதிக்கு மட்டுமே உரியது"),
                ("All reservations for SCs and STs must end immediately without legislative extension", "சட்டமன்ற நீட்டிப்பு இல்லாமல் SC மற்றும் ST-க்கான அனைத்து இடஒதுக்கீடுகளும் உடனடியாக முடிவுக்கு வர வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "On 1 August 2024, a 7-judge Constitution Bench headed by CJI D.Y. Chandrachud overruled the 2004 E.V. Chinnaiah judgment by a 6:1 majority, holding that Article 341 does not create a monolithic caste identity. States may create sub-classifications within SCs and STs to provide preferential quotas to more backward sub-castes (such as Arunthathiyars in Tamil Nadu and Valmikis/Mazhabi Sikhs in Punjab), provided it is backed by empirical quantifiable data.",
            "exp_ta": "2024 ஆகஸ்ட் 1 அன்று, தலைமை நீதிபதி டி.ஒய். சந்திரசூட் தலைமையிலான 7 நீதிபதிகள் அமர்வு 6:1 என்ற பெரும்பான்மையில் 2004 சின்னையா தீர்ப்பை ரத்து செய்தது. சரத்து 341 ஒரு பிரிக்க முடியாத ஒற்றை அடையாளத்தை உருவாக்கவில்லை என்றும், அதிகப் பின்தங்கிய உட்பிரிவுகளுக்கு (தமிழ்நாட்டில் அருந்ததியர், பஞ்சாப்பில் மஸ்ஹபி சீக்கியர் போன்றவை) முன்னுரிமை இடஒதுக்கீடு வழங்க மாநில அரசுகள் ஆய்வுத் தரவுகளின் அடிப்படையில் SC/ST-க்குள் உட்பிரிவு செய்யலாம் என்றும் தீர்ப்பளித்தது.",
            "why_a_en": "The 2024 Davinder Singh verdict authoritatively permitted state sub-classification within SCs/STs based on empirical data.",
            "why_a_ta": "2024 தேவிந்தர் சிங் தீர்ப்பு ஆய்வுத் தரவுகளின் அடிப்படையில் SC/ST உட்பிரிவு ஒதுக்கீட்டை மாநிலங்களுக்கு அனுமதித்தது.",
            "why_b_en": "The 'monolithic whole' doctrine of E.V. Chinnaiah (2004) was expressly overruled by this 7-judge bench.",
            "why_b_ta": "சின்னையா வழக்கின் 'ஒற்றைத் தொகுதி' கோட்பாட்டை இந்த 7 நீதிபதிகள் அமர்வு ரத்து செய்தது.",
            "why_c_en": "Sub-classification is an executive/legislative policy function, not CJI personal power.",
            "why_c_ta": "உட்பிரிவு செய்தல் என்பது அரசின் கொள்கை முடிவு, தலைமை நீதிபதியின் தனிப்பட்ட அதிகாரம் அல்ல.",
            "why_d_en": "The judgment expanded substantive equality and did not end SC/ST reservation.",
            "why_d_ta": "இத்தீர்ப்பு உள்ளடக்க சமத்துவத்தை விரிவுபடுத்தியது, இடஒதுக்கீட்டை முடிக்கவில்லை.",
            "tip_en": "Tamil Nadu had already enacted the Tamil Nadu Arunthathiyars (Special Reservation) Act, 2009 granting 3% internal reservation within the 18% SC quota, which was validated by this 2024 ruling.",
            "tip_ta": "தமிழ்நாடு ஏற்கனவே 2009-ல் 18% SC இடஒதுக்கீட்டிற்குள் அருந்ததியர்களுக்கு 3% உள் இடஒதுக்கீடு வழங்கி சட்டம் இயற்றியிருந்தது; இத்தீர்ப்பு அதை உறுதிப்படுத்தியது.",
            "fact_en": "Four of the seven judges also observed that the Creamy Layer principle should be identified and applied within SCs and STs.",
            "fact_ta": "ஏழு நீதிபதிகளில் நான்கு பேர் SC மற்றும் ST பிரிவினருக்குள்ளும் கிரீமி லேயர் கொள்கை அடையாளம் காணப்பட்டு பயன்படுத்தப்பட வேண்டும் என்றும் குறிப்பிட்டனர்."
        },
        # 4
        {
            "subtopic": "Jaishri Laxmanrao Patil Case 2021",
            "stem_en": "In Jaishri Laxmanrao Patil v. Chief Minister, Maharashtra (2021) (Maratha Reservation Case), the Supreme Court struck down the Maharashtra SEBC Act 2018 on which two primary grounds?",
            "stem_ta": "ஜெயஸ்ரீ லக்ஷ்மண்ராவ் பாட்டீல் எதிர் முதலமைச்சர், மகாராஷ்டிரா (2021) வழக்கில் (மராத்தா இடஒதுக்கீடு வழக்கு), எந்த இரண்டு முதன்மைக் காரணங்களுக்காக மகாராஷ்டிர SEBC சட்டம் 2018-ஐ உச்ச நீதிமன்றம் ரத்து செய்தது?",
            "options": [
                ("Breach of the 50 percent ceiling cap laid down in Indra Sawhney without extraordinary circumstances, and initial interpretation of the 102nd Amendment depriving States of the power to identify backward classes", "அசாதாரண சூழ்நிலைகள் இல்லாமல் இந்திரா சாவ்னி வழக்கின் 50% உச்ச வரம்பை மீறியது, மற்றும் 102வது திருத்தம் மாநிலங்களின் பிற்படுத்தப்பட்டோரை அடையாளம் காணும் அதிகாரத்தைப் பறித்ததாக நீதிமன்றத்தின் ஆரம்ப விளக்கம்"),
                ("The Maratha community was found to have zero population in rural Maharashtra", "கிராமப்புற மகாராஷ்டிராவில் மராத்தா சமூகத்தினரின் மக்கள் தொகை பூஜ்ஜியமாக இருந்தது"),
                ("The Act was passed without the presence of the Governor in the State Legislature", "மாநில சட்டமன்றத்தில் ஆளுநர் இல்லாத போது இச்சட்டம் நிறைவேற்றப்பட்டது"),
                ("The High Court had previously issued a stay order that was violated by the Chief Minister", "உயர் நீதிமன்றம் பிறப்பித்த தடையாணையை முதலமைச்சர் மீறினார்")
            ],
            "correct_key": "A",
            "exp_en": "In the Maratha case (2021), a 5-judge Constitution Bench unanimously held that: (1) The 50% ceiling rule established in Indra Sawhney is binding and cannot be breached without demonstrable extraordinary circumstances, which Marathas did not satisfy; and (2) by a 3:2 majority, held that the 102nd Amendment had concentrated the power to identify SEBCs exclusively in the President. This latter finding prompted Parliament to immediately pass the 105th Constitutional Amendment Act 2021 to restore State powers.",
            "exp_ta": "மராத்தா வழக்கில் (2021), 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு தீர்ப்பளித்தது: (1) இந்திரா சாவ்னி வழக்கின் 50% உச்ச வரம்பு அசாதாரண சூழ்நிலைகள் இன்றி மீறப்படக் கூடாது, மராத்தாக்களுக்கு அத்தகைய அசாதாரண சூழல் இல்லை; (2) 102வது திருத்தம் SEBC-யை அடையாளம் காணும் அதிகாரத்தை குடியரசுத் தலைவரிடம் மட்டுமே குவித்துள்ளது. இந்த இரண்டாவது முடிவே நாடாளுமன்றம் 105வது திருத்தச் சட்டம் 2021-ஐ இயற்றி மாநில அதிகாரங்களை மீட்டெடுக்கத் தூண்டியது.",
            "why_a_en": "Breach of the 50% cap and interpretation of 102nd Amendment were the twin core grounds.",
            "why_a_ta": "50% வரம்பு மீறல் மற்றும் 102வது திருத்தத்தின் விளக்கம் ஆகியவையே இரண்டு முக்கிய காரணங்கள்.",
            "why_b_en": "Marathas constitute roughly 30% of Maharashtra's population, far from zero.",
            "why_b_ta": "மராத்தாக்கள் மகாராஷ்டிர மக்கள் தொகையில் சுமார் 30% ஆவர்.",
            "why_c_en": "Governor presence inside the chamber is not required when passing state bills.",
            "why_c_ta": "சட்டங்கள் இயற்றும் போது ஆளுநர் அவையில் இருக்க வேண்டிய அவசியமில்லை.",
            "why_d_en": "High Court stay violations were not the constitutional invalidation ratio.",
            "why_d_ta": "உயர் நீதிமன்ற தடையாணை மீறல் அரசியலமைப்பு ரத்துக்கான காரணம் அல்ல.",
            "tip_en": "The Gaikwad Commission had recommended Maratha reservation, but the Supreme Court found its empirical methodology inadequate to prove exceptional circumstances.",
            "tip_ta": "கைக்வாட் ஆணையம் மராத்தா இடஒதுக்கீட்டைப் பரிந்துரைத்தது, ஆனால் விதிவிலக்கான சூழலை நிரூபிக்க அதன் ஆய்வு போதுமானதாக இல்லை என உச்ச நீதிமன்றம் கண்டறிந்தது.",
            "fact_en": "The 105th Constitutional Amendment restored State lists within four months of the Jaishri Patil verdict.",
            "fact_ta": "ஜெயஸ்ரீ பாட்டீல் தீர்ப்பு வந்த நான்கு மாதங்களுக்குள் 105வது அரசியலமைப்புத் திருத்தம் மாநிலப் பட்டியல்களை மீட்டெடுத்தது."
        },
        # 5
        {
            "subtopic": "Article 338B vs 105th CAA Harmonization",
            "stem_en": "How did the 105th Constitutional Amendment Act, 2021 amend Article 338B(9) to ensure administrative efficiency for State Governments?",
            "stem_ta": "மாநில அரசுகளின் நிர்வாகத் திறனை உறுதி செய்வதற்காக 105வது அரசியலமைப்புத் திருத்தச் சட்டம் 2021 சரத்து 338B(9)-ஐ எவ்வாறு திருத்தியது?",
            "options": [
                ("It inserted a proviso exempting State Governments from the requirement to consult the National Commission for Backward Classes (NCBC) when preparing their own State SEBC list", "மாநில அரசுகள் தங்களின் சொந்த SEBC பட்டியலைத் தயாரிக்கும் போது NCBC-ஐக் கலந்தாலோசிக்க வேண்டிய கட்டாயத்திலிருந்து விலக்களிக்கும் வரம்புரையைச் சேர்த்தது"),
                ("It completely abolished the National Commission for Backward Classes", "பிற்படுத்தப்பட்ட வகுப்பினருக்கான தேசிய ஆணையத்தை முற்றிலும் ஒழித்தது"),
                ("It made NCBC recommendations legally binding on all High Courts", "NCBC பரிந்துரைகளை அனைத்து உயர் நீதிமன்றங்களுக்கும் சட்டப்பூர்வமாகக் கட்டுப்படுத்தும் ஒன்றாக மாற்றியது"),
                ("It transferred all powers of the NCBC to the Central Bureau of Investigation", "NCBC-ன் அனைத்து அதிகாரங்களையும் மத்திய புலனாய்வுத் துறைக்கு (CBI) மாற்றியது")
            ],
            "correct_key": "A",
            "exp_en": "The 105th Amendment added a proviso to Article 338B(9) clarifying that the requirement for the Union and State Governments to consult the NCBC on all major policy matters affecting SEBCs 'shall not apply for the purposes of clause (3) of article 342A' (i.e. preparation and maintenance of State SEBC lists).",
            "exp_ta": "105வது திருத்தம் சரத்து 338B(9)-ல் ஒரு வரம்புரையைச் சேர்த்து, சரத்து 342A உட்பிரிவு (3)-ன் கீழ் மாநிலங்கள் தங்களின் சொந்த SEBC பட்டியலைத் தயாரித்துப் பராமரிக்கும் விவகாரத்திற்கு NCBC உடனான கட்டாய ஆலோசனை விதி பொருந்தாது எனத் தெளிவுபடுத்தியது.",
            "why_a_en": "A proviso to Art 338B(9) exempted state list preparation from mandatory NCBC consultation.",
            "why_a_ta": "சரத்து 338B(9)-ன் வரம்புரை மாநில பட்டியல் தயாரிப்பை NCBC கட்டாய ஆலோசனையிலிருந்து விடுவித்தது.",
            "why_b_en": "NCBC was preserved, not abolished.",
            "why_b_ta": "NCBC பாதுகாக்கப்பட்டது, ஒழிக்கப்படவில்லை.",
            "why_c_en": "NCBC recommendations remain advisory and do not bind courts.",
            "why_c_ta": "NCBC பரிந்துரைகள் ஆலோசனைக் கூறுகள் மட்டுமே.",
            "why_d_en": "CBI has criminal investigation powers, unrelated to backward class commission mandates.",
            "why_d_ta": "CBI குற்றப் புலனாய்வு அமைப்பு, இதற்கு தொடர்பற்றது.",
            "tip_en": "Without this proviso, every time a State wanted to add/modify an OBC caste, it would have had to seek central NCBC approval, crippling state federal autonomy.",
            "tip_ta": "இந்த வரம்புரை இல்லாவிட்டால், ஒவ்வொரு முறையும் மாநிலங்கள் OBC பட்டியலில் மாற்றங்கள் செய்யும்போது மத்திய NCBC ஒப்புதலைப் பெற வேண்டிய கட்டாயம் ஏற்பட்டு மாநில சுயாட்சி பாதிக்கப்பட்டிருக்கும்.",
            "fact_en": "Article 366(26C) was also amended to redefine Socially and Educationally Backward Classes for both Central and State lists.",
            "fact_ta": "மத்திய மற்றும் மாநிலப் பட்டியல்கள் இரண்டிற்கும் SEBC-ஐ மறுவரையறை செய்ய சரத்து 366(26C)-ம் திருத்தப்பட்டது."
        },
        # 6
        {
            "subtopic": "Fifth Schedule Governor Legislative Powers",
            "stem_en": "Under Paragraph 5(1) of the Fifth Schedule, what extraordinary legislative power is vested in the Governor of a State having Scheduled Areas?",
            "stem_ta": "ஐந்தாவது அட்டவணையின் பத்தி 5(1)-ன் கீழ், அட்டவணைப் பகுதிகளைக் கொண்ட மாநிலத்தின் ஆளுநருக்கு என்ன அசாதாரண சட்டமன்ற அதிகாரம் வழங்கப்பட்டுள்ளது?",
            "options": [
                ("Power to direct by public notification that any particular Act of Parliament or of the State Legislature shall not apply to a Scheduled Area, or shall apply with specified exceptions and modifications", "நாடாளுமன்றம் அல்லது மாநில சட்டமன்றத்தின் எந்தவொரு குறிப்பிட்ட சட்டமும் அட்டவணைப் பகுதிக்குப் பொருந்தாது என்றோ, அல்லது குறிப்பிட்ட விதிவிலக்குகள் மற்றும் மாற்றங்களுடன் பொருந்தும் என்றோ பொது அறிவிப்பின் மூலம் உத்தரவிடும் அதிகாரம்"),
                ("Power to declare war against an adjoining tribal territory", "அண்டை பழங்குடிப் பகுதிக்கு எதிராகப் போர் பிரகடனம் செய்யும் அதிகாரம்"),
                ("Power to dissolve the Lok Sabha if it passes laws adverse to tribal interests", "பழங்குடியினர் நலனுக்கு எதிரான சட்டங்களை நிறைவேற்றினால் மக்களவையைக் கலைக்கும் அதிகாரம்"),
                ("Power to personally try all criminal offenses committed in Scheduled Areas without courts", "நீதிமன்றங்கள் இல்லாமல் அட்டவணைப் பகுதிகளில் செய்யப்படும் அனைத்து குற்றங்களையும் தனிப்பட்ட முறையில் விசாரிக்கும் அதிகாரம்")
            ],
            "correct_key": "A",
            "exp_en": "Paragraph 5(1) of the Fifth Schedule confers plenary legislative power on the Governor to direct by public notification that any Act of Parliament or of the State Legislature shall either not apply to a Scheduled Area or shall apply subject to exceptions and modifications. This power can even be exercised retrospectively.",
            "exp_ta": "ஐந்தாவது அட்டவணையின் பத்தி 5(1), நாடாளுமன்றம் அல்லது மாநில சட்டமன்றத்தின் எந்தவொரு சட்டமும் அட்டவணைப் பகுதிக்குப் பொருந்தாது என்றோ, அல்லது மாற்றங்களுடன் பொருந்தும் என்றோ பொது அறிவிப்பின் மூலம் உத்தரவிட ஆளுநருக்கு முழுமையான சட்டமன்ற அதிகாரத்தை வழங்குகிறது. இந்த அதிகாரத்தை முன்செல்லும் தேதியிட்டும் பயன்படுத்தலாம்.",
            "why_a_en": "Para 5(1) of the Fifth Schedule explicitly grants the Governor this non-application/modification legislative power.",
            "why_a_ta": "பத்தி 5(1) ஆளுநருக்கு சட்டங்களை விலக்க அல்லது மாற்றியமைக்கும் அதிகாரத்தை தெளிவாக வழங்குகிறது.",
            "why_b_en": "War powers belong strictly to the President under Article 53(2) and Union List.",
            "why_b_ta": "போர் பிரகடன அதிகாரம் குடியரசுத் தலைவருக்கு மட்டுமே உரியது.",
            "why_c_en": "Only the President can dissolve the Lok Sabha under Article 85(2)(b).",
            "why_c_ta": "குடியரசுத் தலைவர் மட்டுமே மக்களவையைக் கலைக்க முடியும்.",
            "why_d_en": "Judicial powers remain with the judiciary; Governor cannot act as trial judge.",
            "why_d_ta": "நீதித்துறை அதிகாரங்களை நீதிமன்றங்களே பயன்படுத்துகின்றன.",
            "tip_en": "In Chebrolu Leela Prasad Rao v. State of AP (2020), the Supreme Court held that the Governor's power under Para 5(1) is legislative in character, but cannot override Fundamental Rights (Part III).",
            "tip_ta": "செப்ரோலு பிரசாத் ராவ் வழக்கில் (2020), ஆளுநரின் பத்தி 5(1) அதிகாரம் சட்டமன்றத் தன்மை கொண்டது என்றாலும், அது அடிப்படை உரிமைகளை (பகுதி III) மீற முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "fact_en": "Under Para 5(2), the Governor can also make regulations prohibiting or restricting the transfer of land by or among members of Scheduled Tribes.",
            "fact_ta": "பத்தி 5(2)-ன் கீழ் பழங்குடியினருக்கு இடையேயான நிலப் பரிமாற்றங்களைத் தடைசெய்ய ஒழுங்குமுறைகளை உருவாக்க ஆளுநருக்கு அதிகாரம் உண்டு."
        },
        # 7
        {
            "subtopic": "Samatha Case 1997",
            "stem_en": "In the landmark judgment Samatha v. State of Andhra Pradesh (1997), the Supreme Court interpreted Paragraph 5(2) of the Fifth Schedule to rule that:",
            "stem_ta": "வரலாற்று சிறப்புமிக்க சமதா எதிர் ஆந்திரப் பிரதேச அரசு (1997) வழக்கில், ஐந்தாவது அட்டவணையின் பத்தி 5(2)-ஐ விளக்கி உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "options": [
                ("Government land, tribal land, and forest land in Scheduled Areas cannot be leased to non-tribals or private mining companies, as 'person' includes the State Government", "அட்டவணைப் பகுதிகளில் உள்ள அரசு நிலம், பழங்குடியினர் நிலம் மற்றும் வன நிலங்களை பழங்குடியினர் அல்லாதவர்களுக்கோ அல்லது தனியார் சுரங்க நிறுவனங்களுக்கோ குத்தகைக்கு விட முடியாது, ஏனெனில் 'நபர்' என்பதில் மாநில அரசும் அடங்கும்"),
                ("All mineral resources in Scheduled Areas belong exclusively to multinational corporations", "அட்டவணைப் பகுதிகளில் உள்ள அனைத்து கனிம வளங்களும் பன்னாட்டு நிறுவனங்களுக்கு மட்டுமே சொந்தமானது"),
                ("The Fifth Schedule was void ab initio for violating freedom of trade under Article 19(1)(g)", "சரத்து 19(1)(g)-ன் கீழான வர்த்தக சுதந்திரத்தை மீறியதால் ஐந்தாவது அட்டவணையே ஆரம்பத்திலிருந்தே செல்லாது"),
                ("Tribal inhabitants can be evicted without rehabilitation if mineral wealth is detected", "கனிம வளம் கண்டறியப்பட்டால் பழங்குடி மக்களை மறுவாழ்வு இன்றியே வெளியேற்ற முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "In Samatha (1997), the Supreme Court held that the word 'person' in statutory regulations framed under Para 5(2) of the Fifth Schedule includes the State Government. Therefore, transfer of tribal land by the State Government to non-tribal private mining entities is prohibited. Mining can only be done by State instrumentalities or tribal cooperatives.",
            "exp_ta": "சமதா வழக்கில் (1997), ஐந்தாவது அட்டவணை பத்தி 5(2)-ன் கீழான ஒழுங்குமுறைகளில் 'நபர்' என்ற சொல்லில் மாநில அரசும் அடங்கும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. எனவே பழங்குடியினர் நிலத்தை தனியார் சுரங்க நிறுவனங்களுக்கு மாநில அரசு குத்தகைக்கு விடுவது தடைசெய்யப்பட்டுள்ளது. அரசு நிறுவனங்கள் அல்லது பழங்குடியினர் கூட்டுறவு சங்கங்கள் மட்டுமே சுரங்கத் தொழில் செய்ய முடியும்.",
            "why_a_en": "Samatha stopped private mining exploitation in Fifth Schedule areas by including the State within 'person'.",
            "why_a_ta": "'நபர்' என்பதில் அரசையும் உள்ளடக்கியதன் மூலம் தனியார் சுரங்கச் சுரண்டலை சமதா தீர்ப்பு தடுத்தது.",
            "why_b_en": "The judgment expressly barred private and multinational corporations.",
            "why_b_ta": "இத்தீர்ப்பு தனியார் நிறுவனங்களை வெளிப்படையாகத் தடுத்தது.",
            "why_c_en": "Constitutional schedules cannot be struck down under Article 19(1)(g).",
            "why_c_ta": "அரசியலமைப்பு அட்டவணைகளை சரத்து 19(1)(g)-ன் கீழ் ரத்து செய்ய முடியாது.",
            "why_d_en": "The judgment mandated tribal protection and socio-economic empowerment.",
            "why_d_ta": "இத்தீர்ப்பு பழங்குடியினரின் பாதுகாப்பு மற்றும் அதிகாரமளித்தலை கட்டாயமாக்கியது.",
            "tip_en": "Samatha judgment is regarded as the Magna Carta of tribal land rights in India.",
            "tip_ta": "இந்தியாவில் பழங்குடியினரின் நில உரிமைகளுக்கான மகா சாசனமாக சமதா தீர்ப்பு கருதப்படுகிறது.",
            "fact_en": "The judgment mandated that at least 20% of net profits from mining must be set aside for local tribal infrastructure and development.",
            "fact_ta": "சுரங்க நிகர லாபத்தில் குறைந்தது 20% உள்ளூர் பழங்குடியினரின் உள்கட்டமைப்பு மற்றும் வளர்ச்சிக்கு ஒதுக்கப்பட வேண்டும் என்று இத்தீர்ப்பு கட்டாயமாக்கியது."
        },
        # 8
        {
            "subtopic": "Sixth Schedule Autonomous District Council Powers",
            "stem_en": "Under Paragraph 3 of the Sixth Schedule, Autonomous District Councils (ADCs) have plenary legislative power to make laws with respect to which of the following subjects?",
            "stem_ta": "ஆறாவது அட்டவணையின் பத்தி 3-ன் கீழ், தன்னாட்சி மாவட்டக் குழுக்களுக்கு (ADC) பின்வரும் எந்த விவகாரங்கள் தொடர்பாக சட்டங்களை உருவாக்கும் முழுமையான அதிகாரம் உள்ளது?",
            "options": [
                ("Allotment, occupation, or use of land, management of unclassed forests, inheritance of property, marriage, and social customs", "நிலங்களை ஒதுக்கீடு செய்தல், ஆக்கிரமித்தல் அல்லது பயன்படுத்துதல், வகைப்படுத்தப்படாத காடுகளை நிர்வகித்தல், சொத்துரிமை, திருமணம் மற்றும் சமூகப் பழக்கவழக்கங்கள்"),
                ("Declaration of war and maintenance of an independent army", "போர் பிரகடனம் செய்தல் மற்றும் சுதந்திரமான ராணுவத்தைப் பராமரித்தல்"),
                ("Regulation of currency, stock exchanges, and foreign trade", "நாணயம், பங்குச் சந்தைகள் மற்றும் வெளிநாட்டு வர்த்தகத்தை ஒழுங்குபடுத்துதல்"),
                ("Imposition of railway freight rates across interstate borders", "மாநில எல்லைகளுக்கு இடையேயான ரயில்வே சரக்குக் கட்டணங்களை விதித்தல்")
            ],
            "correct_key": "A",
            "exp_en": "Paragraph 3(1) of the Sixth Schedule gives ADCs wide legislative powers over: land allocation (other than reserved forests), forest management, use of canals/water courses, shifting cultivation (jhum), town committees, village administration, inheritance, marriage and divorce, and social customs.",
            "exp_ta": "ஆறாவது அட்டவணையின் பத்தி 3(1) தன்னாட்சி மாவட்டக் குழுக்களுக்கு: நில ஒதுக்கீடு, வன நிர்வாகம், கால்வாய்கள்/நீர்நிலைகள் பயன்பாடு, இடப்பெயர்வு விவசாயம் (ஜூம்), கிராம நிர்வாகம், சொத்துரிமை, திருமணம் மற்றும் விவாகரத்து, மற்றும் சமூகப் பழக்கவழக்கங்கள் ஆகியவற்றின் மீது விரிவான சட்டமன்ற அதிகாரங்களை வழங்குகிறது.",
            "why_a_en": "Paragraph 3(1) explicitly lists these local customary, forest, and civil matters.",
            "why_a_ta": "பத்தி 3(1) உள்ளூர் மரபு, வனம் மற்றும் உரிமையியல் விவகாரங்களை தெளிவாகப் பட்டியலிடுகிறது.",
            "why_b_en": "Defense and military matters are exclusive Union subjects.",
            "why_b_ta": "பாதுகாப்பு மற்றும் ராணுவ விவகாரங்கள் ஒன்றியத்திற்கு மட்டுமே உரியவை.",
            "why_c_en": "Currency and foreign trade are federal under Union List Entries 36 and 41.",
            "why_c_ta": "நாணயம் மற்றும் வெளிநாட்டு வர்த்தகம் மத்தியப் பட்டியலின் கீழ் வருகின்றன.",
            "why_d_en": "Railways are governed exclusively by the Union under Union List Entry 22.",
            "why_d_ta": "ரயில்வே மத்தியப் பட்டியல் பதிவு 22-ன் கீழ் வருகிறது.",
            "tip_en": "Laws made by an ADC under Paragraph 3 have no effect until submitted to the Governor and receive his assent (Para 3(2)).",
            "tip_ta": "பத்தி 3-ன் கீழ் ADC இயற்றும் சட்டங்கள் ஆளுநருக்கு சமர்ப்பிக்கப்பட்டு அவரது ஒப்புதலைப் பெற்ற பிறகே நடைமுறைக்கு வரும் (பத்தி 3(2)).",
            "fact_en": "Sixth Schedule councils also possess judicial powers to constitute village courts to try customary disputes between tribals (Para 4).",
            "fact_ta": "ஆறாவது அட்டவணை குழுக்கள் பழங்குடியினருக்கு இடையேயான மரபுசார் வழக்குகளை விசாரிக்க கிராம நீதிமன்றங்களை அமைக்கும் நீதித்துறை அதிகாரங்களையும் கொண்டுள்ளன (பத்தி 4)."
        },
        # 9
        {
            "subtopic": "Sixth Schedule Paragraph 9 Mineral Royalties",
            "stem_en": "Under Paragraph 9 of the Sixth Schedule, how are royalties accruing from licenses or leases for prospecting or extracting minerals in an autonomous district shared?",
            "stem_ta": "ஆறாவது அட்டவணையின் பத்தி 9-ன் கீழ், ஒரு தன்னாட்சி மாவட்டத்தில் கனிமங்களை ஆய்வு செய்ய அல்லது வெட்டியெடுப்பதற்கான உரிமங்கள் அல்லது குத்தகைகளில் இருந்து கிடைக்கும் ராயல்டி எவ்வாறு பகிரப்படுகிறது?",
            "options": [
                ("Shared between the State Government and the District Council in such proportion as may be agreed upon, or determined by the Governor in case of dispute", "மாநில அரசுக்கும் மாவட்டக் குழுவிற்கும் இடையே ஒப்புக்கொள்ளப்பட்ட விகிதத்திலோ அல்லது தகராறு ஏற்பட்டால் ஆளுநரால் தீர்மானிக்கப்படும் விகிதத்திலோ பகிரப்படுகிறது"),
                ("Retained 100 percent by the Union Ministry of Mines in New Delhi", "புது தில்லியில் உள்ள மத்திய சுரங்க அமைச்சகத்தால் 100 சதவீதம் தக்கவைத்துக் கொள்ளப்படுகிறது"),
                ("Distributed equally among all Village Panchayats of the entire country", "நாடு முழுவதும் உள்ள அனைத்து கிராம ஊராட்சிகளுக்கும் சமமாகப் பகிர்ந்தளிக்கப்படுகிறது"),
                ("Paid directly to the United Nations Development Programme", "ஐக்கிய நாடுகள் வளர்ச்சித் திட்டத்திற்கு (UNDP) நேரடியாகச் செலுத்தப்படுகிறது")
            ],
            "correct_key": "A",
            "exp_en": "Paragraph 9(1) of the Sixth Schedule mandates that license fees or royalties on minerals shall be shared between the Government of the State and the District Council in such proportion as may be agreed upon between the Government of the State and the District Council; if dispute arises, it is referred to the Governor whose determination is final.",
            "exp_ta": "ஆறாவது அட்டவணையின் பத்தி 9(1), கனிமங்களுக்கான உரிமக் கட்டணம் அல்லது ராயல்டி மாநில அரசுக்கும் மாவட்டக் குழுவிற்கும் இடையே ஒப்புக்கொள்ளப்பட்ட விகிதத்தில் பகிரப்பட வேண்டும் என்றும்; தகராறு ஏற்பட்டால் அது ஆளுநரின் முடிவிற்கு விடப்பட்டு, அவரது முடிவே இறுதியானது என்றும் கூறுகிறது.",
            "why_a_en": "Paragraph 9 explicitly provides for revenue sharing agreed between State Government and ADC or decided by Governor.",
            "why_a_ta": "பத்தி 9 மாநில அரசும் மாவட்டக் குழுவும் ஒப்புக்கொண்டபடி அல்லது ஆளுநர் தீர்மானித்தபடி வருவாய் பகிர்வை தெளிவாகக் கூறுகிறது.",
            "why_b_en": "Mineral royalties in states belong to the State Government and ADC, not retained centrally.",
            "why_b_ta": "மாநில கனிம ராயல்டி மத்திய அரசால் முழுமையாகத் தக்கவைக்கப்படுவதில்லை.",
            "why_c_en": "Pan-India redistribution is not a Sixth Schedule mechanism.",
            "why_c_ta": "அகில இந்திய மறுபகிர்வு என்பது 6வது அட்டவணை முறை அல்ல.",
            "why_d_en": "UN has no constitutional role in sovereign domestic mineral royalties.",
            "why_d_ta": "கனிம ராயல்டியில் ஐ.நா-விற்கு எந்தப் பங்கும் இல்லை.",
            "tip_en": "This constitutional fiscal entitlement provides crucial autonomous revenue to the District Councils independently of state grants.",
            "tip_ta": "இந்த அரசியலமைப்பு நிதி உரிமை மாவட்டக் குழுக்களுக்கு மாநில மானியங்களைச் சாராத முக்கியமான தன்னாட்சி வருவாயை வழங்குகிறது.",
            "fact_en": "In Meghalaya, coal and limestone royalties under Para 9 have been a major source of revenue for the Khasi, Jaintia, and Garo Hills District Councils.",
            "fact_ta": "மேகாலயாவில் பத்தி 9-ன் கீழான நிலக்கரி மற்றும் சுண்ணாம்புக்கல் ராயல்டி தன்னாட்சி மாவட்டக் குழுக்களுக்கு முக்கிய வருவாய் ஆதாரமாக உள்ளது."
        },
        # 10
        {
            "subtopic": "Fifth vs Sixth Schedule Core Differences",
            "stem_en": "Which of the following represents the most fundamental constitutional difference between the Fifth Schedule and the Sixth Schedule?",
            "stem_ta": "ஐந்தாவது அட்டவணைக்கும் ஆறாவது அட்டவணைக்கும் இடையிலான மிகவும் அடிப்படையான அரசியலமைப்பு வேறுபாட்டை பின்வருவனவற்றில் எது குறிக்கிறது?",
            "options": [
                ("The Fifth Schedule provides for advisory bodies (Tribes Advisory Council) subordinate to state authority, whereas the Sixth Schedule creates autonomous legislative, executive, and judicial bodies (District Councils) operating as self-governing entities", "ஐந்தாவது அட்டவணை மாநில அதிகாரத்திற்கு உட்பட்ட ஆலோசனைக் குழுக்களை (TAC) வழங்குகிறது; ஆறாவது அட்டவணை தன்னாட்சி கொண்ட சட்டமன்ற, நிர்வாக, நீதித்துறை அமைப்புகளை (மாவட்டக் குழுக்கள்) சுயாட்சி அமைப்புகளாக உருவாக்குகிறது"),
                ("The Fifth Schedule applies only to Jammu and Kashmir, while the Sixth Schedule applies only to South India", "ஐந்தாவது அட்டவணை ஜம்மு-காஷ்மீருக்கு மட்டுமே பொருந்தும், ஆறாவது அட்டவணை தென்னிந்தியாவிற்கு மட்டுமே பொருந்தும்"),
                ("The Fifth Schedule was repealed in 1976, while the Sixth Schedule was added in 2019", "ஐந்தாவது அட்டவணை 1976-ல் ரத்து செய்யப்பட்டது, ஆறாவது அட்டவணை 2019-ல் சேர்க்கப்பட்டது"),
                ("The Fifth Schedule allows private corporate ownership of all forest lands, while the Sixth Schedule nationalizes all private lands", "ஐந்தாவது அட்டவணை அனைத்து வன நிலங்களையும் தனியாருக்கு அனுமதிக்கிறது, ஆறாவது அட்டவணை அனைத்து நிலங்களையும் அரசுடமையாக்குகிறது")
            ],
            "correct_key": "A",
            "exp_en": "Under the Fifth Schedule, tribal areas are administered through the regular state executive machinery, with the Governor exercising protective legislative control advised by a 20-member TAC. Under the Sixth Schedule, tribal areas are constituted into Autonomous Districts with elected District Councils that possess independent law-making, taxation, and judicial powers, functioning as 'states within a state'.",
            "exp_ta": "ஐந்தாவது அட்டவணையின் கீழ் பழங்குடிப் பகுதிகள் வழக்கமான மாநில நிர்வாக இயந்திரத்தின் மூலம் நிர்வகிக்கப்படுகின்றன; ஆளுநர் TAC ஆலோசனையுடன் சட்டப் பாதுகாப்பைப் பயன்படுத்துகிறார். ஆறாவது அட்டவணையின் கீழ் தன்னாட்சி மாவட்டக் குழுக்கள் தங்களின் சொந்த சட்டமன்ற, வரிவிதிப்பு மற்றும் நீதித்துறை அதிகாரங்களுடன் 'மாநிலத்திற்குள் ஒரு மாநிலம்' போல் சுயாட்சியுடன் செயல்படுகின்றன.",
            "why_a_en": "Accurately contrasts the advisory nature of Fifth Schedule with the legislative/self-governing autonomy of Sixth Schedule.",
            "why_a_ta": "5வது அட்டவணையின் ஆலோசனைக் கட்டமைப்பையும், 6வது அட்டவணையின் தன்னாட்சி சட்டமன்ற அமைப்பையும் துல்லியமாக ஒப்பிடுகிறது.",
            "why_b_en": "Fifth Schedule applies to 10 mainland states; Sixth Schedule applies to 4 NE states (AMTM).",
            "why_b_ta": "5வது அட்டவணை 10 முதன்மை மாநிலங்களுக்கும், 6வது அட்டவணை 4 வடகிழக்கு மாநிலங்களுக்கும் பொருந்தும்.",
            "why_c_en": "Both schedules have existed in the Constitution since 26 January 1950.",
            "why_c_ta": "இரு அட்டவணைகளும் 1950 ஜனவரி 26 முதல் அரசியலமைப்பில் உள்ளன.",
            "why_d_en": "Neither schedule privatizes forests; both protect indigenous communal tenure.",
            "why_d_ta": "இரண்டு அட்டவணைகளும் பூர்வீக சமூக நில உரிமைகளைப் பாதுகாக்கின்றன.",
            "tip_en": "B.R. Ambedkar explained in the Constituent Assembly that the hill tribes of Assam, unlike mainland tribes, had not assimilated with neighboring cultures and required local autonomy under the Sixth Schedule.",
            "tip_ta": "அசாமின் மலைவாழ் பழங்குடியினர் அண்டை கலாச்சாரங்களுடன் கலக்காமல் தனித்து இருந்ததால் அவர்களுக்கு சுயாட்சி தேவை என அம்பேத்கர் அரசியல் நிர்ணய சபையில் விளக்கினார்.",
            "fact_en": "The Sixth Schedule was drafted based on the recommendations of the Bordoloi Sub-Committee (headed by Gopinath Bordoloi).",
            "fact_ta": "கோபிநாத் போர்டோலோய் தலைமையிலான துணைக்குழுவின் பரிந்துரைகளின் அடிப்படையிலேயே ஆறாவது அட்டவணை வரைவு செய்யப்பட்டது."
        },
        # 11
        {
            "subtopic": "Article 371A Naga Women Representation Case",
            "stem_en": "In People's Union for Civil Liberties v. State of Nagaland (2023), regarding the conduct of urban local body elections with 33% reservation for women in Nagaland, what did the Supreme Court hold?",
            "stem_ta": "நாகாலாந்தில் பெண்களுக்கு 33% இடஒதுக்கீட்டுடன் நகர்ப்புற உள்ளாட்சித் தேர்தல்களை நடத்துவது தொடர்பான வழக்கில் (2023), உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "options": [
                ("Article 371A protecting Naga customary law cannot be used to defeat Part IXA (Article 243T) constitutional mandates for 33 percent women reservation in urban local bodies", "நாகா மரபுச் சட்டத்தைப் பாதுகாக்கும் சரத்து 371A-ஐ, நகர்ப்புற உள்ளாட்சி அமைப்புகளில் பெண்களுக்கு 33 சதவீத இடஒதுக்கீடு வழங்கும் பகுதி IXA-ன் (சரத்து 243T) அரசியலமைப்பு கட்டளையை முறியடிக்கப் பயன்படுத்த முடியாது"),
                ("Women are constitutionally prohibited from ever casting a vote in Nagaland municipal elections", "நாகாலாந்து நகராட்சித் தேர்தல்களில் பெண்கள் வாக்களிக்க அரசியலமைப்பு ரீதியாக தடை விதிக்கப்பட்டுள்ளது"),
                ("The Governor has absolute immunity to permanently suspend all municipal elections in the northeast", "வடகிழக்கில் அனைத்து நகராட்சித் தேர்தல்களையும் நிரந்தரமாக நிறுத்தி வைக்க ஆளுநருக்கு முழுமையான பாதுகாப்பு உள்ளது"),
                ("Article 371A completely nullifies the entirety of Part IXA across all Indian States", "அனைத்து இந்திய மாநிலங்களிலும் பகுதி IXA முழுவதையும் சரத்து 371A முற்றிலும் ரத்து செய்கிறது")
            ],
            "correct_key": "A",
            "exp_en": "In 2023, the Supreme Court ruled that 33% reservation for women in urban municipalities under Article 243T does not infringe upon Naga customary laws or social practices protected under Article 371A(1)(a), because modern municipal governance in towns is statutory and not a traditional customary village institution.",
            "exp_ta": "2023-ல் உச்ச நீதிமன்றம், சரத்து 243T-ன் கீழ் நகராட்சிகளில் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்குவது சரத்து 371A(1)(a)-ன் கீழான நாகா மரபுச் சட்டங்களை மீறாது என்று தீர்ப்பளித்தது; ஏனெனில் நகரங்களில் உள்ள நவீன நகராட்சி நிர்வாகம் சட்டப்பூர்வமானது, பாரம்பரிய கிராம அமைப்பு அல்ல.",
            "why_a_en": "The SC firmly held that customary law cannot block gender equality in municipal governance.",
            "why_a_ta": "நகராட்சி நிர்வாகத்தில் பாலின சமத்துவத்தை மரபுச் சட்டம் தடுக்க முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_b_en": "Universal adult suffrage applies under Article 326.",
            "why_b_ta": "சரத்து 326-ன் கீழ் வயதுவந்தோர் வாக்குரிமை அனைவருக்கும் பொருந்தும்.",
            "why_c_en": "Governor cannot suspend constitutional local election mandates.",
            "why_c_ta": "ஆளுநர் அரசியலமைப்பு உள்ளாட்சித் தேர்தல் விதியை இடைநிறுத்த முடியாது.",
            "why_d_en": "Article 371A applies only to Nagaland, not across all Indian states.",
            "why_d_ta": "சரத்து 371A நாகாலாந்திற்கு மட்டுமே பொருந்தும்.",
            "tip_en": "Following the Supreme Court's firm directives, Nagaland finally conducted ULB elections with 33% women quota in June 2024 for the first time in two decades.",
            "tip_ta": "உச்ச நீதிமன்றத்தின் உத்தரவைத் தொடர்ந்து, இரு தசாப்தங்களில் முதல்முறையாக 2024 ஜூன் மாதம் நாகாலாந்து 33% மகளிர் ஒதுக்கீட்டுடன் நகர்ப்புற உள்ளாட்சித் தேர்தலை நடத்தியது.",
            "fact_en": "Traditional Naga tribal organizations (Hohos) had historically opposed women quotas citing patriarchal village customs.",
            "fact_ta": "பாரம்பரிய நாகா பழங்குடி அமைப்புகள் (ஹோஹோக்கள்) தங்களின் ஆணாதிக்க கிராம மரபுகளைக் காரணம் காட்டி மகளிர் இடஒதுக்கீட்டை எதிர்த்து வந்தன."
        },
        # 12
        {
            "subtopic": "Article 371D Presidential Order Challenge",
            "stem_en": "In Chief Justice of Andhra Pradesh v. L.V.A. Dixitulu (1979), the Supreme Court considered the scope of Article 371D regarding the state judiciary and held that:",
            "stem_ta": "ஆந்திரப் பிரதேச தலைமை நீதிபதி எதிர் எல்.வி.ஏ. தீட்சிதுலு (1979) வழக்கில், மாநில நீதித்துறை தொடர்பான சரத்து 371D-ன் வரம்பை ஆய்வு செய்த உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "options": [
                ("The Administrative Tribunal under Article 371D has no jurisdiction over the officers and servants of the High Court or subordinate judiciary, as it would erode judicial independence", "நீதித்துறை சுதந்திரத்தைச் சீர்குலைக்கும் என்பதால், உயர் நீதிமன்ற அதிகாரிகள், ஊழியர்கள் அல்லது சார்பு நீதித்துறை மீது சரத்து 371D-ன் கீழான நிர்வாகத் தீர்ப்பாயத்திற்கு எந்த அதிகார வரம்பும் இல்லை"),
                ("The High Court is completely subordinate to the Administrative Tribunal in all administrative matters", "அனைத்து நிர்வாக விவகாரங்களிலும் உயர் நீதிமன்றம் நிர்வாகத் தீர்ப்பாயத்திற்குக் கீழ்ப்பட்டது"),
                ("The Chief Justice of the High Court must seek prior sanction from the Governor before appointing clerks", "எழுத்தர்களை நியமிப்பதற்கு முன் உயர் நீதிமன்றத் தலைமை நீதிபதி ஆளுநரிடம் முன் அனுமதி பெற வேண்டும்"),
                ("Article 371D dissolved all subordinate civil courts in Andhra Pradesh", "சரத்து 371D ஆந்திராவில் உள்ள அனைத்து சார்பு உரிமையியல் நீதிமன்றங்களையும் கலைத்தது")
            ],
            "correct_key": "A",
            "exp_en": "In L.V.A. Dixitulu (1979), the Supreme Court ruled that Article 371D does not apply to the staff of the High Court or judicial officers in the subordinate judiciary. The independence of the judiciary under Articles 229 and 235 cannot be impaired by administrative tribunals set up under Article 371D.",
            "exp_ta": "தீட்சிதுலு வழக்கில் (1979), சரத்து 371D உயர் நீதிமன்ற ஊழியர்கள் அல்லது சார்பு நீதித்துறை அதிகாரிகளுக்குப் பொருந்தாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. சரத்துகள் 229 மற்றும் 235-ன் கீழான நீதித்துறை சுதந்திரத்தை சரத்து 371D-ன் கீழ் அமைக்கப்பட்ட நிர்வாகத் தீர்ப்பாயங்களால் பாதிக்க முடியாது.",
            "why_a_en": "Judicial independence under Articles 229 and 235 excludes High Court staff from tribunal control under Art 371D.",
            "why_a_ta": "சரத்துகள் 229 மற்றும் 235-ன் கீழான நீதித்துறை சுதந்திரம் நீதிமன்ற ஊழியர்களை தீர்ப்பாயக் கட்டுப்பாட்டிலிருந்து விலக்குகிறது.",
            "why_b_en": "High Courts are constitutional courts superior to statutory administrative tribunals.",
            "why_b_ta": "உயர் நீதிமன்றங்கள் தீர்ப்பாயங்களை விட உயர்ந்த அரசியலமைப்பு நீதிமன்றங்கள்.",
            "why_c_en": "Chief Justice has independent powers of appointment under Article 229.",
            "why_c_ta": "தலைமை நீதிபதிக்கு சரத்து 229-ன் கீழ் தன்னாட்சி நியமன அதிகாரம் உண்டு.",
            "why_d_en": "Subordinate courts were not dissolved by Article 371D.",
            "why_d_ta": "சார்பு நீதிமன்றங்கள் கலைக்கப்படவில்லை.",
            "tip_en": "Harmonious construction: Article 371D applies to the executive civil services of the State, not the independent judicial wing.",
            "tip_ta": "இணக்கமான விளக்கம்: சரத்து 371D மாநில நிர்வாக சிவில் பணிகளுக்கு மட்டுமே பொருந்தும், தன்னாட்சி நீதித்துறைப் பிரிவுக்கு அல்ல.",
            "fact_en": "Articles 229 and 235 vest absolute administrative control of the court registry and subordinate judiciary in the High Court.",
            "fact_ta": "சரத்துகள் 229 மற்றும் 235 நீதிமன்றப் பதிவகம் மற்றும் சார்பு நீதித்துறையின் முழுக் கட்டுப்பாட்டையும் உயர் நீதிமன்றத்திடம் ஒப்படைக்கின்றன."
        },
        # 13
        {
            "subtopic": "Article 16(4) Inadequacy vs Numerical Proportion",
            "stem_en": "In R.K. Sabharwal v. State of Punjab (1995), the Supreme Court established the 'Post-Based Roster' principle. What was the central holding of this judgment?",
            "stem_ta": "ஆர்.கே. சபர்வால் எதிர் பஞ்சாப் அரசு (1995) வழக்கில், உச்ச நீதிமன்றம் 'பதவி அடிப்படையிலான சுழற்சி' (Post-Based Roster) கொள்கையை வகுத்தது. இத்தீர்ப்பின் மையக் கருத்து என்ன?",
            "options": [
                ("Reservation roster operates on the total number of posts in a cadre (cadre strength), and once the prescribed percentage quota is reached, reservation ceases and vacancies must be filled by replacement only", "இடஒதுக்கீட்டு சுழற்சி ஒரு பணியிடப் பிரிவில் உள்ள மொத்த பதவிகளின் அடிப்படையில் செயல்படுகிறது; நிர்ணயிக்கப்பட்ட சதவீத ஒதுக்கீடு எட்டப்பட்டவுடன், இடஒதுக்கீடு முடிவுக்கு வந்து காலிப் பணியிடங்கள் மாற்று முறையில் மட்டுமே நிரப்பப்பட வேண்டும்"),
                ("Reservation must apply afresh on every single retirement regardless of overall cadre percentage", "ஒட்டுமொத்தப் பதவி சதவீதத்தைப் பொருட்படுத்தாமல் ஒவ்வொரு ஓய்வின் போதும் புதிதாக இடஒதுக்கீடு பயன்படுத்தப்பட வேண்டும்"),
                ("General category candidates can be terminated from service if reservation percentages fall short", "இடஒதுக்கீடு சதவீதம் குறைந்தால் பொதுப்பிரிவு ஊழியர்களை பணியிலிருந்து நீக்க முடியும்"),
                ("The roster must be redesigned every six months by the State Public Service Commission", "ஒவ்வொரு ஆறு மாதங்களுக்கும் மாநில அரசுப் பணியாளர் தேர்வாணையத்தால் சுழற்சி முறை மாற்றி அமைக்கப்பட வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "In R.K. Sabharwal (1995), a Constitution Bench held that reservation operates against the cadre strength (posts) and not against vacancies. Once the prescribed reservation percentage (e.g. 15% SC, 7.5% ST) is achieved in the cadre, the roster stops operating, and vacancies occurring thereafter are filled by replacement (candidate of the same category that vacated the post).",
            "exp_ta": "சபர்வால் வழக்கில் (1995), இடஒதுக்கீடு என்பது காலிப் பணியிடங்களின் அடிப்படையில் அல்லாமல் மொத்த பதவிகளின் (கேடர் வலிமை) அடிப்படையில் செயல்படுகிறது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. நிர்ணயிக்கப்பட்ட இடஒதுக்கீடு சதவீதம் எட்டப்பட்டவுடன், சுழற்சி முறை செயல்படுவது நின்றுவிடும்; அதன் பிறகு ஏற்படும் காலிப் பணியிடங்கள் மாற்று முறையில் (பதவி விலகிய அதே பிரிவைச் சேர்ந்த நபரால்) நிரப்பப்பட வேண்டும்.",
            "why_a_en": "Sabharwal established the transition from vacancy-based roster to post-based roster.",
            "why_a_ta": "சபர்வால் தீர்ப்பு காலிப்பணியிட சுழற்சியிலிருந்து பதவி அடிப்படையிலான சுழற்சி முறைக்கு மாற்றத்தை ஏற்படுத்தியது.",
            "why_b_en": "Vacancy-based roster was specifically discarded because it led to over-representation exceeding the quota percentage.",
            "why_b_ta": "காலிப்பணியிட முறை ஒதுக்கீட்டு அளவை விட அதிக பிரதிநிதித்துவத்திற்கு வழிவகுத்ததால் அது கைவிடப்பட்டது.",
            "why_c_en": "Existing employees cannot be retrenched to adjust quotas.",
            "why_c_ta": "இடஒதுக்கீட்டைச் சரிசெய்ய பணியில் உள்ள ஊழியர்களை நீக்க முடியாது.",
            "why_d_en": "Roster is running continuously until filled, not redesigned semi-annually.",
            "why_d_ta": "சுழற்சி என்பது தொடர்ந்து செயல்படும் ஒன்று, ஆறு மாதங்களுக்கு ஒருமுறை மாற்றப்படுவதல்ல.",
            "tip_en": "Remember: Sabharwal (1995) = 'Post-Based Roster' (Cadre Strength, not vacancy numbers).",
            "tip_ta": "நினைவில் கொள்க: சபர்வால் (1995) = 'பதவி அடிப்படையிலான சுழற்சி' (பணியிட பலம், காலிப்பணியிட எண்ணிக்கை அல்ல).",
            "fact_en": "Following Sabharwal, the Department of Personnel and Training (DoPT) issued model 200-point post-based rosters for central government services in July 1997.",
            "fact_ta": "சபர்வால் தீர்ப்பைத் தொடர்ந்து, மத்திய பணியாளர் துறை 1997 ஜூலையில் 200-புள்ளி பதவி அடிப்படையிலான மாதிரி சுழற்சி முறையை வெளியிட்டது."
        },
        # 14
        {
            "subtopic": "Article 16(4) Open Competition Merit Rule",
            "stem_en": "Under settled constitutional law (Indra Sawhney, 1992 and Saurav Yadav, 2021), when a reserved category candidate (SC/ST/OBC) scores higher marks than the cut-off for the General/Unreserved category, what happens?",
            "stem_ta": "நிலையான அரசியலமைப்பு சட்டத்தின்படி (இந்திரா சாவ்னி 1992 மற்றும் சௌரவ் யாதவ் 2021), இடஒதுக்கீட்டுப் பிரிவு விண்ணப்பதாரர் (SC/ST/OBC) பொதுப்பிரிவு தகுதி மதிப்பெண்ணை விட அதிக மதிப்பெண் பெற்றால் என்ன நடக்கும்?",
            "options": [
                ("The candidate must be selected against the General/Unreserved open merit quota and cannot be counted against their reserved quota", "அவ்விண்ணப்பதாரர் பொது/திறந்தநிலை தகுதி இட ஒதுக்கீட்டில் தேர்ந்தெடுக்கப்பட வேண்டும், அவரது சொந்த இடஒதுக்கீட்டுப் பிரிவில் கணக்கிடப்படக் கூடாது"),
                ("The candidate must still be counted against their reserved quota to ensure general candidates are protected", "பொதுப்பிரிவினரைப் பாதுகாக்க அவ்விண்ணப்பதாரர் அவரது சொந்த இடஒதுக்கீட்டுப் பிரிவிலேயே கணக்கிடப்பட வேண்டும்"),
                ("The candidate's score is automatically reduced to the general cut-off mark", "அவ்விண்ணப்பதாரரின் மதிப்பெண் தானாக பொதுப்பிரிவு தகுதி மதிப்பெண்ணாகக் குறைக்கப்படும்"),
                ("The candidate must surrender their caste certificate before admission", "சேர்க்கைக்கு முன் அவ்விண்ணப்பதாரர் தனது சாதிச் சான்றிதழை அரசிடம் ஒப்படைக்க வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "In Indra Sawhney (1992) and reaffirmed in Saurav Yadav (2021), the Supreme Court ruled that the Open/Unreserved category is open to all on merit. If a meritorious reserved category candidate qualifies on their own merit without availing relaxations, they must be adjusted against the unreserved quota, leaving the reserved seats intact for other candidates of their category.",
            "exp_ta": "இந்திரா சாவ்னி மற்றும் சௌரவ் யாதவ் வழக்குகளில் உச்ச நீதிமன்றம் தீர்ப்பளித்தது: பொது/திறந்தநிலை பிரிவு என்பது தகுதி அடிப்படையில் அனைவருக்கும் பொதுவானது. இடஒதுக்கீட்டுப் பிரிவு மாணவர் எந்த தளர்வுகளையும் பெறாமல் தனது சொந்த தகுதியால் தேர்ச்சி பெற்றால், அவர் பொதுப்பிரிவு இடத்திலேயே நிரப்பப்பட வேண்டும்; இதனால் அவரது பிரிவுக்கான இடஒதுக்கீட்டு இடங்கள் பிற மாணவர்களுக்குக் கிடைக்கும்.",
            "why_a_en": "Meritorious reserved candidates taking open seats is a settled constitutional rule of vertical reservation.",
            "why_a_ta": "தகுதிவாய்ந்த இடஒதுக்கீட்டு மாணவர்கள் பொது இடங்களைப் பெறுவது செங்குத்து இடஒதுக்கீட்டின் நிலையான விதியாகும்.",
            "why_b_en": "Counting them in reserved quota would turn the open category into a reserved quota for general classes, which is unconstitutional.",
            "why_b_ta": "அவர்களை இடஒதுக்கீட்டில் சேர்த்தால் திறந்தநிலை பிரிவு பொதுப்பிரிவினருக்கான இடஒதுக்கீடாக மாறிவிடும், இது அரசியலமைப்பிற்கு எதிரானது.",
            "why_c_en": "Marks cannot be artificially reduced.",
            "why_c_ta": "மதிப்பெண்களை செயற்கையாகக் குறைக்க முடியாது.",
            "why_d_en": "Surrendering caste certificates is arbitrary and unlawful.",
            "why_d_ta": "சாதிச் சான்றிதழை ஒப்படைப்பது சட்டவிரோதமானது.",
            "tip_en": "Vertical Reservation (SC/ST/OBC) vs Horizontal Reservation (Women/PWD/Ex-Servicemen): Horizontal cuts across vertical compartments.",
            "tip_ta": "செங்குத்து இடஒதுக்கீடு (SC/ST/OBC) vs கிடைமட்ட இடஒதுக்கீடு (பெண்கள்/மாற்றுத்திறனாளிகள்): கிடைமட்ட ஒதுக்கீடு செங்குத்துப் பிரிவுகளை ஊடுருவுகிறது.",
            "fact_en": "In Saurav Yadav (2021), this rule was strictly enforced in the selection of police constables in Uttar Pradesh.",
            "fact_ta": "சௌரவ் யாதவ் வழக்கில் (2021) உத்தரப் பிரதேச காவலர் தேர்வில் இந்த விதி தீவிரமாக அமல்படுத்தப்பட்டது."
        },
        # 15
        {
            "subtopic": "Article 338 Functions on Anglo-Indians (Historical)",
            "stem_en": "Under former Article 338(10) prior to the 102nd Amendment, the National Commission for Scheduled Castes also had the constitutional mandate to investigate and monitor matters relating to:",
            "stem_ta": "102வது திருத்தத்திற்கு முந்தைய பழைய சரத்து 338(10)-ன் கீழ், SC பிரிவினருக்கான தேசிய ஆணையம் வேறு எந்த சமூகத்தின் விவகாரங்களையும் கண்காணிக்கும் அரசியலமைப்பு கடமையைக் கொண்டிருந்தது?",
            "options": [
                ("The Anglo-Indian community and Other Backward Classes", "ஆங்கிலோ-இந்திய சமூகம் மற்றும் இதர பிற்படுத்தப்பட்ட வகுப்பினர் (OBC)"),
                ("Religious minorities under Article 30 exclusively", "சரத்து 30-ன் கீழான மத சிறுபான்மையினர் மட்டுமே"),
                ("Non-Resident Indians (NRIs)", "வெளிநாடு வாழ் இந்தியர்கள் (NRI)"),
                ("Members of the Armed Forces serving in border regions", "எல்லைப் பகுதிகளில் பணியாற்றும் ராணுவப் படை வீரர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Under former Article 338(10), references to Scheduled Castes in Article 338 were construed as including the Anglo-Indian community and Other Backward Classes (until a separate NCBC was granted constitutional status via the 102nd Amendment in 2018).",
            "exp_ta": "பழைய சரத்து 338(10)-ன் கீழ், சரத்து 338-ல் உள்ள SC குறிப்புகள் ஆங்கிலோ-இந்திய சமூகம் மற்றும் பிற்படுத்தப்பட்ட வகுப்பினரையும் (2018-ல் NCBC அரசியலமைப்பு அந்தஸ்து பெறும் வரை) உள்ளடக்கியதாகக் கருதப்பட்டது.",
            "why_a_en": "Former Art 338(10) explicitly extended NCSC monitoring jurisdiction to Anglo-Indians and OBCs.",
            "why_a_ta": "பழைய சரத்து 338(10) NCSC கண்காணிப்பு அதிகார வரம்பை ஆங்கிலோ-இந்தியர் மற்றும் OBC-களுக்கும் நீட்டித்தது.",
            "why_b_en": "Religious minorities are monitored by the statutory National Commission for Minorities.",
            "why_b_ta": "மத சிறுபான்மையினர் சிறுபான்மையினர் தேசிய ஆணையத்தால் கண்காணிக்கப்படுகின்றனர்.",
            "why_c_en": "NRIs are handled by the Ministry of External Affairs.",
            "why_c_ta": "வெளிநாடு வாழ் இந்தியர்கள் வெளியுறவு அமைச்சகத்தால் கையாளப்படுகின்றனர்.",
            "why_d_en": "Armed forces personnel are governed by military tribunals and service acts.",
            "why_d_ta": "ராணுவ வீரர்கள் ராணுவச் சட்டங்களால் நிர்வகிக்கப்படுகின்றனர்.",
            "tip_en": "With the 102nd Amendment 2018, OBCs were moved to the new Article 338B (NCBC); Anglo-Indians remain covered under Art 338(10).",
            "tip_ta": "2018-ன் 102வது திருத்தத்தின் மூலம் OBC-கள் புதிய சரத்து 338B-க்கு மாற்றப்பட்டனர்; ஆங்கிலோ-இந்தியர்கள் தொடர்ந்து 338(10)-ன் கீழ் உள்ளனர்.",
            "fact_en": "Before 2004, STs were also monitored by the combined commission under Article 338 before NCST was bifurcated by the 89th Amendment.",
            "fact_ta": "2004-க்கு முன்பு 89வது திருத்தத்தால் NCST பிரிக்கப்படும் வரை ST-களும் சரத்து 338-ன் கீழேயே கண்காணிக்கப்பட்டனர்."
        },
        # 16
        {
            "subtopic": "Article 371D Six-Point Formula",
            "stem_en": "What was the political origin of Articles 371D and 371E inserted by the 32nd Amendment in 1973?",
            "stem_ta": "1973-ல் 32வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்துகள் 371D மற்றும் 371E-ன் அரசியல் தோற்றம் என்ன?",
            "options": [
                ("The Six-Point Formula agreed between leaders of Andhra and Telangana regions to settle the Mulki Rules agitation and Jai Andhra movement", "முல்கி விதி கிளர்ச்சி மற்றும் ஜெய் ஆந்திரா போராட்டத்தை முடிவுக்குக் கொண்டுவர ஆந்திரா மற்றும் தெலங்கானா தலைவர்களிடையே எட்டப்பட்ட ஆறு அம்ச சூத்திரம்"),
                ("The Panchsheel Treaty signed between India and China", "இந்தியாவுக்கும் சீனாவுக்கும் இடையே கையெழுத்தான பஞ்சசீல ஒப்பந்தம்"),
                ("The Tashkent Declaration signed following the 1965 Indo-Pak war", "1965 இந்திய-பாகிஸ்தான் போருக்குப் பிறகு கையெழுத்தான தாஷ்கண்ட் பிரகடனம்"),
                ("The Sarkaria Commission recommendations on Inter-State river water sharing", "மாநிலங்களுக்கு இடையேயான நதிநீர் பகிர்வு குறித்த சர்க்காரியா ஆணைய பரிந்துரைகள்")
            ],
            "correct_key": "A",
            "exp_en": "Articles 371D and 371E were born out of the 'Six-Point Formula' announced on 21 September 1973 by the Union Government to resolve violent agitations in Andhra Pradesh over 'Mulki Rules' (domicile quotas) and separate statehood demands (Jai Telangana and Jai Andhra movements).",
            "exp_ta": "முல்கி விதிகள் (இருப்பிட ஒதுக்கீடு) மற்றும் தனி மாநில கோரிக்கைகள் (ஜெய் தெலங்கானா மற்றும் ஜெய் ஆந்திரா இயக்கங்கள்) தொடர்பான வன்முறைப் போராட்டங்களைத் தீர்க்க மத்திய அரசால் 1973 செப்டம்பர் 21 அன்று அறிவிக்கப்பட்ட 'ஆறு அம்ச சூத்திரத்தின்' மூலமே சரத்துகள் 371D மற்றும் 371E உருவாக்கப்பட்டன.",
            "why_a_en": "The Six-Point Formula was the exact political basis for the 32nd Amendment 1973.",
            "why_a_ta": "ஆறு அம்ச சூத்திரமே 1973-ன் 32வது திருத்தத்திற்கான சரியான அரசியல் அடிப்படையாகும்.",
            "why_b_en": "Panchsheel was an international foreign policy pact (1954).",
            "why_b_ta": "பஞ்சசீலம் என்பது சர்வதேச வெளியுறவுக் கொள்கை ஒப்பந்தம் (1954).",
            "why_c_en": "Tashkent Declaration was a bilateral diplomatic accord in 1966.",
            "why_c_ta": "தாஷ்கண்ட் பிரகடனம் 1966-ன் இருதரப்பு இராஜதந்திர ஒப்பந்தம்.",
            "why_d_en": "Sarkaria Commission was appointed much later in 1983.",
            "why_d_ta": "சர்க்காரியா ஆணையம் பின்னர் 1983-ல் நியமிக்கப்பட்டது.",
            "tip_en": "The Supreme Court in Director of Industries v. Venkata Reddy (1973) had upheld Mulki Rules, triggering the Jai Andhra agitation that necessitated this constitutional compromise.",
            "tip_ta": "வெங்கட ரெட்டி வழக்கில் (1973) உச்ச நீதிமன்றம் முல்கி விதிகளை உறுதி செய்ததால் எழுந்த ஜெய் ஆந்திரா போராட்டத்தைத் தொடர்ந்து இந்த அரசியலமைப்பு சமரசம் ஏற்பட்டது.",
            "fact_en": "The Six-Point Formula abolished Mulki Rules while institutionalizing local educational zones and employment cadres under Article 371D.",
            "fact_ta": "ஆறு அம்ச சூத்திரம் முல்கி விதிகளை நீக்கிய அதே வேளையில், சரத்து 371D-ன் கீழ் உள்ளூர் கல்வி மண்டலங்களையும் பணிப் பிரிவுகளையும் முறைப்படுத்தியது."
        },
        # 17
        {
            "subtopic": "Article 371F Chogyal Adaptation Power",
            "stem_en": "Under Article 371F(l), the President was granted the power to adapt or modify any law in force in Sikkim for what specific duration from the appointed day?",
            "stem_ta": "சரத்து 371F(l)-ன் கீழ், சிக்கிமில் நடைமுறையில் உள்ள எந்தவொரு சட்டத்தையும் மாற்றியமைக்க குடியரசுத் தலைவருக்கு குறிப்பிட்ட நாளிலிருந்து எத்தனை ஆண்டு காலத்திற்கு அதிகாரம் வழங்கப்பட்டது?",
            "options": [
                ("Two years", "இரண்டு ஆண்டுகள்"),
                ("Five years", "ஐந்து ஆண்டுகள்"),
                ("Ten years", "பத்து ஆண்டுகள்"),
                ("Six months only", "ஆறு மாதங்கள் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Article 371F(l) provided that for the purpose of facilitating the application of any law in relation to the administration of the State of Sikkim, the President may, within two years from the appointed day, by order, make such adaptations and modifications of the law as may be necessary.",
            "exp_ta": "சரத்து 371F(l), சிக்கிம் மாநில நிர்வாகம் தொடர்பாக சட்டங்களைப் பயன்படுத்துவதை எளிதாக்குவதற்காக, குறிப்பிட்ட நாளிலிருந்து இரண்டு ஆண்டுகளுக்குள் குடியரசுத் தலைவர் ஆணையின் மூலம் சட்டங்களில் தேவையான மாற்றங்களைச் செய்யலாம் என்று கூறியது.",
            "why_a_en": "Article 371F(l) explicitly fixed a sunset period of two years for presidential law adaptation.",
            "why_a_ta": "சரத்து 371F(l) சட்ட மாற்றத்திற்கான அதிகாரத்திற்கு இரண்டு ஆண்டு கால வரம்பை தெளிவாக நிர்ணயித்தது.",
            "why_b_en": "Five years is incorrect.",
            "why_b_ta": "ஐந்து ஆண்டுகள் என்பது தவறானது.",
            "why_c_en": "Ten years was the period under Art 371A for Tuensang administration.",
            "why_c_ta": "பத்து ஆண்டுகள் என்பது டியூன்சாங் நிர்வாகத்திற்கான காலம்.",
            "why_d_en": "Six months is incorrect.",
            "why_d_ta": "ஆறு மாதங்கள் என்பது தவறானது.",
            "tip_en": "Similar adaptation powers were given under Article 372(2) for the whole of India when the Constitution commenced in 1950 (which was for 3 years).",
            "tip_ta": "1950-ல் அரசியலமைப்பு நடைமுறைக்கு வந்தபோது இந்தியா முழுமைக்கும் சரத்து 372(2)-ன் கீழ் இதே போன்ற சட்ட மாற்ற அதிகாரம் 3 ஆண்டுகளுக்கு வழங்கப்பட்டது.",
            "fact_en": "This power allowed the Indian Government to align Sikkim's penal and revenue administration with Indian federal standards.",
            "fact_ta": "இந்த அதிகாரம் சிக்கிமின் குற்றவியல் மற்றும் வருவாய் நிர்வாகத்தை இந்திய கூட்டாட்சித் தரங்களுடன் இணைக்க உதவியது."
        },
        # 18
        {
            "subtopic": "Article 371J Hyderabad-Karnataka History",
            "stem_en": "Why did the Hyderabad-Karnataka region require special provisions under Article 371J inserted in 2012?",
            "stem_ta": "2012-ல் சேர்க்கப்பட்ட சரத்து 371J-ன் கீழ் ஹைதராபாத்-கர்நாடகா பகுதிக்கு சிறப்பு ஏற்பாடுகள் ஏன் தேவைப்பட்டன?",
            "options": [
                ("Historical neglect under the Nizam's princely rule prior to 1948 and severe socio-economic and educational backwardness compared to South Karnataka (Old Mysore)", "1948-க்கு முன்பு நிஜாமின் சமஸ்தான ஆட்சியின் கீழான வரலாற்றுப் புறக்கணிப்பு மற்றும் தென் கர்நாடகாவோடு (பழைய மைசூர்) ஒப்பிடும்போது கடுமையான சமூக-பொருளாதார, கல்விப் பின்தங்கிய நிலை"),
                ("It was a Portuguese colony that refused to join the Indian Union until 2010", "2010 வரை இந்திய ஒன்றியத்தில் இணைய மறுத்த ஒரு போர்த்துகீசிய காலனியாக அது இருந்தது"),
                ("The region had zero natural water sources requiring international food aid", "சர்வதேச உணவு உதவி தேவைப்படும் அளவுக்கு அப்பகுதியில் இயற்கை நீர் ஆதாரங்கள் எதுவும் இல்லை"),
                ("The State Assembly had passed a resolution declaring independence from India", "இந்தியாவிலிருந்து சுதந்திரம் பிரகடனம் செய்து மாநில சட்டமன்றம் தீர்மானம் நிறைவேற்றியிருந்தது")
            ],
            "correct_key": "A",
            "exp_en": "The Hyderabad-Karnataka region was part of the feudal Hyderabad State until Police Action (Operation Polo, 1948) and was merged into Mysore State in 1956. The Nanjundappa Committee Report (2002) documented alarming regional imbalances between Hyderabad-Karnataka and the more developed Old Mysore region, prompting Article 371J.",
            "exp_ta": "ஹைதராபாத்-கர்நாடகா பகுதி 1948 வரை நிஜாம் சமஸ்தானத்தின் பகுதியாக இருந்து, 1956-ல் மைசூர் மாநிலத்துடன் இணைக்கப்பட்டது. நஞ்சுண்டப்பா கமிட்டி அறிக்கை (2002) பழைய மைசூர் பகுதியோடு ஒப்பிடுகையில் இப்பகுதி அடைந்திருந்த கடுமையான பிராந்திய ஏற்றத்தாழ்வுகளை ஆவணப்படுத்தியது; இதுவே சரத்து 371J உருவாகக் காரணமாக அமைந்தது.",
            "why_a_en": "Historical feudal neglect and modern regional disparity documented by the Nanjundappa Committee prompted Art 371J.",
            "why_a_ta": "வரலாற்றுப் புறக்கணிப்பு மற்றும் நஞ்சுண்டப்பா குழு ஆவணப்படுத்திய பிராந்திய ஏற்றத்தாழ்வே சரத்து 371J-க்கு வழிவகுத்தது.",
            "why_b_en": "Goa was Portuguese, not Hyderabad-Karnataka.",
            "why_b_ta": "கோவாவே போர்த்துகீசிய காலனி, ஹைதராபாத்-கர்நாடகா அல்ல.",
            "why_c_en": "The Krishna and Tungabhadra rivers flow through this region.",
            "why_c_ta": "கிருஷ்ணா மற்றும் துங்கபத்ரா நதிகள் இப்பகுதியில் பாய்கின்றன.",
            "why_d_en": "There was never any secessionist resolution by the Karnataka Assembly.",
            "why_d_ta": "பிரிவினைவாதத் தீர்மானம் எதுவும் நிறைவேற்றப்படவில்லை.",
            "tip_en": "Dr. D.M. Nanjundappa High Power Committee on Redressal of Regional Imbalances (2002) is the foundational blueprint for Article 371J.",
            "tip_ta": "பிராந்திய ஏற்றத்தாழ்வுகளைக் களைவதற்கான டாக்டர் டி.எம். நஞ்சுண்டப்பா உயர்மட்டக் குழுவே (2002) சரத்து 371J-க்கான அடித்தளமாகும்.",
            "fact_en": "The 98th Amendment was moved by then Union Home Minister Sushilkumar Shinde and received bipartisan parliamentary support.",
            "fact_ta": "98வது திருத்தத்தை அப்போதைய மத்திய உள்துறை அமைச்சர் சுஷில்குமார் ஷிண்டே தாக்கல் செய்தார்; அனைத்துக் கட்சிகளும் ஆதரித்தன."
        },
        # 19
        {
            "subtopic": "EWS Criteria Janhit Abhiyan",
            "stem_en": "In Janhit Abhiyan (2022), which constitutional doctrine was primarily used by the dissenting judges to argue against the exclusion of SCs, STs, and OBCs from the 10% EWS quota?",
            "stem_ta": "ஜன்ஹித் அபியான் (2022) வழக்கில், 10% EWS இடஒதுக்கீட்டிலிருந்து SC, ST மற்றும் OBC-களை விலக்குவதற்கு எதிராக வாதிட மாறுபட்ட தீர்ப்பளித்த நீதிபதிகளால் எந்த அரசியலமைப்பு கோட்பாடு முதன்மையாகப் பயன்படுத்தப்பட்டது?",
            "options": [
                ("The equality code under Articles 14, 15, and 16, which prohibits discriminatory exclusion of the poorest segments based on caste identity", "சாதி அடையாளத்தின் அடிப்படையில் ஏழ்மையான பிரிவினரை பாகுபாட்டுடன் விலக்குவதைத் தடை செய்யும் சரத்துகள் 14, 15 மற்றும் 16-ன் கீழான சமத்துவக் கோட்பாடு"),
                ("The Doctrine of Territorial Nexus under Article 245", "சரத்து 245-ன் கீழான பிராந்திய தொடர்பு கோட்பாடு"),
                ("The Doctrine of Severeance under Article 13", "சரத்து 13-ன் கீழான பிரித்தெடுக்கும் கோட்பாடு"),
                ("The Doctrine of Colorable Legislation under Entry 97", "பதிவு 97-ன் கீழான மறைமுக சட்டமியற்றல் கோட்பாடு")
            ],
            "correct_key": "A",
            "exp_en": "The dissenting minority (Justices S. Ravindra Bhat and CJI U.U. Lalit) held that excluding the poorest among the SCs, STs, and SEBCs from the economic criteria quota discriminates against them based on caste identity, violating the non-discrimination mandate of the equality code, which forms part of the Basic Structure.",
            "exp_ta": "மாறுபட்ட தீர்ப்பளித்த சிறுபான்மை நீதிபதிகள் (நீதிபதி எஸ். ரவீந்திர பட் மற்றும் தலைமை நீதிபதி யு.யு. லலித்), பொருளாதார அளவுகோல் ஒதுக்கீட்டிலிருந்து ஏழ்மையான SC, ST மற்றும் SEBC-களை விலக்குவது சாதி அடிப்படையில் அவர்களுக்கு எதிரான பாகுபாடாகும் என்றும், இது அடிப்படை அமைப்பின் பகுதியான சமத்துவக் கோட்பாட்டை மீறுகிறது என்றும் கூறினர்.",
            "why_a_en": "The equality code (non-discrimination under Articles 14-16) was the cornerstone of the dissenting opinion.",
            "why_a_ta": "சமத்துவக் கோட்பாடே (சரத்துகள் 14-16-ன் கீழான பாகுபாடின்மை) மாறுபட்ட தீர்ப்பின் மையக்கல்லாக இருந்தது.",
            "why_b_en": "Territorial nexus relates to extraterritorial operation of laws, not reservation.",
            "why_b_ta": "பிராந்திய தொடர்பு கோட்பாடு எல்லைக்கு அப்பாற்பட்ட சட்டங்களுக்குரியது.",
            "why_c_en": "Doctrine of severance deals with striking down unconstitutional parts of statutes.",
            "why_c_ta": "பிரித்தெடுக்கும் கோட்பாடு சட்டங்களின் முரணான பகுதிகளை நீக்குவதற்குரியது.",
            "why_d_en": "Colorable legislation deals with legislative competence.",
            "why_d_ta": "மறைமுக சட்டமியற்றல் சட்டமன்ற அதிகார வரம்பைக் கையாள்கிறது.",
            "tip_en": "The majority (3 judges), however, ruled that SC/ST/OBC are already provided compensatory benefits under Arts 15(4) and 16(4) and form a separate class, so their exclusion from EWS was reasonable.",
            "tip_ta": "இருப்பினும் பெரும்பான்மை நீதிபதிகள் (3 பேர்), SC/ST/OBC ஏற்கனவே 15(4) மற்றும் 16(4)-ன் கீழ் பலன்களைப் பெறுவதால் அவர்களை EWS-லிருந்து விலக்கியது நியாயமானது எனக் கூறினர்.",
            "fact_en": "Janhit Abhiyan confirmed that economic status alone can be a valid constitutional basis for affirmative classification.",
            "fact_ta": "பொருளாதார நிலை மட்டுமே ஆக்கப்பூர்வ வகைப்பாட்டிற்கான சரியான அரசியலமைப்பு அடிப்படையாக அமைய முடியும் என்பதை ஜன்ஹித் அபியான் உறுதி செய்தது."
        },
        # 20
        {
            "subtopic": "Article 330 ST Lok Sabha Exclusions",
            "stem_en": "Under Article 330(1)(b), seats are reserved in the Lok Sabha for Scheduled Tribes EXCEPT the Scheduled Tribes in:",
            "stem_ta": "சரத்து 330(1)(b)-ன் கீழ், எந்தப் பகுதியில் உள்ள பட்டியலிடப்பட்ட பழங்குடியினரைத் தவிர்த்து பிற பழங்குடியினருக்கு மக்களவையில் இடங்கள் ஒதுக்கப்படுகின்றன?",
            "options": [
                ("The autonomous districts of Assam (which have a separate reservation under sub-clause (c))", "அசாமின் தன்னாட்சி மாவட்டங்கள் (இதற்கு உட்பிரிவு (c)-ன் கீழ் தனி இடஒதுக்கீடு உள்ளது)"),
                ("The entire Union Territory of Lakshadweep", "லட்சத்தீவு யூனியன் பிரதேசம் முழுவதும்"),
                ("The State of Jharkhand", "ஜார்க்கண்ட் மாநிலம்"),
                ("The Scheduled Areas of Madhya Pradesh", "மத்தியப் பிரதேசத்தின் அட்டவணைப் பகுதிகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 330(1)(b) reserves seats for 'the Scheduled Tribes except the Scheduled Tribes in the autonomous districts of Assam'; and sub-clause (c) separately provides for 'the Scheduled Tribes in the autonomous districts of Assam'. This ensures that hill tribes of Assam's autonomous districts have independent constitutional representation.",
            "exp_ta": "சரத்து 330(1)(b) 'அசாமின் தன்னாட்சி மாவட்டங்களில் உள்ள பழங்குடியினர் தவிர்த்த பிற பழங்குடியினருக்கு' இடங்களை ஒதுக்குகிறது; மேலும் உட்பிரிவு (c) 'அசாமின் தன்னாட்சி மாவட்டங்களில் உள்ள பழங்குடியினருக்கு' தனியாக வகைசெய்கிறது. இது அசாம் மலைவாழ் பழங்குடியினருக்கு தனித்துவமான பிரதிநிதித்துவத்தை உறுதி செய்கிறது.",
            "why_a_en": "Article 330(1)(b) explicitly carves out the exception for the autonomous districts of Assam.",
            "why_a_ta": "சரத்து 330(1)(b) அசாமின் தன்னாட்சி மாவட்டங்களை தெளிவாக விதிவிலக்காகப் பிரிக்கிறது.",
            "why_b_en": "Lakshadweep has a reserved ST Lok Sabha seat under the general ST quota.",
            "why_b_ta": "லட்சத்தீவு பொது ST ஒதுக்கீட்டின் கீழ் ஒரு தனி மக்களவைத் தொகுதியைக் கொண்டுள்ளது.",
            "why_c_en": "Jharkhand STs are covered under the normal Article 330(1)(b) provision.",
            "why_c_ta": "ஜார்க்கண்ட் ST பிரிவினர் வழக்கமான சரத்து 330(1)(b)-ன் கீழ் வருகின்றனர்.",
            "why_d_en": "Madhya Pradesh STs are covered under Article 330(1)(b).",
            "why_d_ta": "மத்தியப் பிரதேச ST பிரிவினர் சரத்து 330(1)(b)-ன் கீழ் வருகின்றனர்.",
            "tip_en": "Assam has one Lok Sabha seat specifically reserved for Autonomous Districts (Diphu constituency).",
            "tip_ta": "அசாமில் தன்னாட்சி மாவட்டங்களுக்காக பிரத்யேகமாக ஒரு மக்களவைத் தொகுதி (திபு தொகுதி) ஒதுக்கப்பட்டுள்ளது.",
            "fact_en": "Article 330(3) sets demographic proportionality specifically for the autonomous districts of Assam.",
            "fact_ta": "சரத்து 330(3) அசாமின் தன்னாட்சி மாவட்டங்களுக்கு மக்கள் தொகை விகிதாசாரத்தை பிரத்யேகமாக நிர்ணயிக்கிறது."
        },
        # 21
        {
            "subtopic": "Fifth Schedule Tribal Land Non-Alienation",
            "stem_en": "Under Paragraph 5(2)(a) of the Fifth Schedule, regulations made by the Governor may prohibit or restrict the transfer of land by or among members of the Scheduled Tribes in a Scheduled Area. This power is intended to:",
            "stem_ta": "ஐந்தாவது அட்டவணையின் பத்தி 5(2)(a)-ன் கீழ், ஆளுநர் உருவாக்கும் ஒழுங்குமுறைகள் அட்டவணைப் பகுதியில் பழங்குடியினரின் நிலப் பரிமாற்றத்தைத் தடைசெய்யலாம் அல்லது கட்டுப்படுத்தலாம். இந்த அதிகாரம் எதற்காக வழங்கப்பட்டது?",
            "options": [
                ("Prevent tribal land alienation to non-tribals, moneylenders, and commercial speculators", "பழங்குடியினர் அல்லாதவர்கள், கந்துவட்டிக்காரர்கள் மற்றும் வணிக ஊக வணிகர்களிடம் பழங்குடியினர் நிலம் பறிபோவதைத் தடுக்க"),
                ("Facilitate the compulsory acquisition of all agricultural holdings for corporate farming", "கார்ப்பரேட் விவசாயத்திற்காக அனைத்து விவசாய நிலங்களையும் கட்டாயமாகக் கையகப்படுத்துவதை எளிதாக்க"),
                ("Abolish private ownership and convert all tribal holdings into crown land", "தனியார் உரிமையை ஒழித்து அனைத்து பழங்குடியினரின் நிலங்களையும் அரசு நிலமாக மாற்ற"),
                ("Authorize the sale of tribal heritage artifacts to international museums", "பழங்குடியினரின் பாரம்பரிய கலைப்பொருட்களை சர்வதேச அருங்காட்சியகங்களுக்கு விற்பனை செய்ய அனுமதிக்க")
            ],
            "correct_key": "A",
            "exp_en": "The primary objective of Paragraph 5(2)(a) is to preserve tribal culture and economic survival by preventing 'land alienation' (the predatory transfer of ancestral tribal lands to non-tribal moneylenders and landlords), as affirmed in landmark cases like P. Rami Reddy (1988) and Samatha (1997).",
            "exp_ta": "பத்தி 5(2)(a)-ன் முதன்மை நோக்கம், பாரம்பரிய பழங்குடியினரின் நிலங்கள் பழங்குடியினர் அல்லாத கந்துவட்டிக்காரர்கள் மற்றும் நிலப்பிரபுக்களால் அபகரிக்கப்படுவதைத் தடுத்து, பழங்குடி கலாச்சாரத்தையும் பொருளாதார வாழ்வாதாரத்தையும் பாதுகாப்பதாகும்.",
            "why_a_en": "Preventing land alienation is the core purpose of Fifth Schedule Para 5(2)(a).",
            "why_a_ta": "நிலம் பறிபோவதைத் தடுப்பதே ஐந்தாவது அட்டவணை பத்தி 5(2)(a)-ன் மைய நோக்கமாகும்.",
            "why_b_en": "It restricts corporate land grabs rather than facilitating them.",
            "why_b_ta": "இது கார்ப்பரேட் நில அபகரிப்பைத் தடுக்கிறது, ஆதரிக்கவில்லை.",
            "why_c_en": "It protects tribal ownership, not converts land to state ownership.",
            "why_c_ta": "இது பழங்குடியினரின் நில உரிமையைப் பாதுகாக்கிறது.",
            "why_d_en": "Heritage artifacts are not real estate land transactions.",
            "why_d_ta": "கலைப்பொருட்கள் நிலப் பரிவர்த்தனைகள் அல்ல.",
            "tip_en": "In P. Rami Reddy v. State of AP (1988), the SC held that a law prohibiting transfer of land even between tribals in Scheduled Areas to prevent benami transactions was constitutionally valid.",
            "tip_ta": "ராமி ரெட்டி வழக்கில் (1988), பினாமி பரிவர்த்தனைகளைத் தடுக்க பழங்குடியினருக்கு இடையேயான நில விற்பனையையும் கட்டுப்படுத்தும் சட்டம் செல்லும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "fact_en": "PESA Act 1996 section 4(m)(iii) further empowered Gram Sabhas to restore unlawfully alienated tribal lands.",
            "fact_ta": "1996 PESA சட்டம் சட்டவிரோதமாகப் பறிக்கப்பட்ட நிலங்களை மீட்கும் அதிகாரத்தை கிராம சபைகளுக்கு வழங்கியது."
        },
        # 22
        {
            "subtopic": "Article 371A Resource Ownership Doctrine",
            "stem_en": "The phrase 'ownership and transfer of land and its resources' in Article 371A(1)(a)(iv) has generated significant legal dispute between the Union and Nagaland regarding:",
            "stem_ta": "சரத்து 371A(1)(a)(iv)-ல் உள்ள 'நிலம் மற்றும் அதன் வளங்களின் உரிமை மற்றும் பரிமாற்றம்' என்ற சொற்றொடர் ஒன்றிய அரசுக்கும் நாகாலாந்திற்கும் இடையே எந்த விவகாரத்தில் குறிப்பிடத்தக்க சட்டத் தகராறை ஏற்படுத்தியுள்ளது?",
            "options": [
                ("Ownership, exploration, and licensing of mineral oil, petroleum, and natural gas in Nagaland", "நாகாலாந்தில் உள்ள கனிம எண்ணெய், பெட்ரோலியம் மற்றும் இயற்கை எரிவாயுவின் உரிமை, ஆய்வு மற்றும் உரிமம் வழங்குதல்"),
                ("Operation of national telecommunication satellites", "தேசிய தொலைத்தொடர்பு செயற்கைக்கோள்களின் செயல்பாடு"),
                ("Establishment of naval bases in the Brahmaputra basin", "பிரம்மபுத்திரா படுகையில் கடற்படை தளங்களை நிறுவுதல்"),
                ("Regulation of inter-state railways passing through Dimapur", "திமாபூர் வழியாகச் செல்லும் மாநிலங்களுக்கு இடையேயான ரயில்வே ஒழுங்குமுறை")
            ],
            "correct_key": "A",
            "exp_en": "While the Union Government contends that petroleum and natural gas are exclusive Union subjects under Entry 53 of the Union List (read with Article 297), the Nagaland Legislative Assembly enacted the Nagaland Petroleum and Natural Gas Regulations 2012 claiming that 'land and its resources' in Article 371A gives the State exclusive ownership over onshore hydrocarbon deposits.",
            "exp_ta": "மத்தியப் பட்டியல் பதிவு 53-ன் கீழ் பெட்ரோலியம் மற்றும் இயற்கை எரிவாயு ஒன்றியத்தின் தனிப்பட்ட அதிகாரம் என மத்திய அரசு கூறினாலும், சரத்து 371A-ல் உள்ள 'நிலம் மற்றும் அதன் வளங்கள்' என்ற சொல் பெட்ரோலியத்தின் மீதான முழு உரிமையையும் மாநிலத்திற்கே வழங்குகிறது எனக் கூறி நாகாலாந்து 2012-ல் தனி ஒழுங்குமுறைச் சட்டத்தை இயற்றியது.",
            "why_a_en": "Petroleum and oil resource licensing is the central constitutional contest under Article 371A.",
            "why_a_ta": "பெட்ரோலியம் மற்றும் எண்ணெய் வள உரிமமே சரத்து 371A-ன் கீழான முக்கிய அரசியலமைப்பு மோதலாகும்.",
            "why_b_en": "Telecommunications is Entry 31 of Union List, not a land resource.",
            "why_b_ta": "தொலைத்தொடர்பு மத்தியப் பட்டியல் பதிவு 31, நில வளம் அல்ல.",
            "why_c_en": "Naval bases are Union List Entry 1.",
            "why_c_ta": "கடற்படை தளங்கள் மத்தியப் பட்டியல் பதிவு 1.",
            "why_d_en": "Railways are Entry 22 of Union List.",
            "why_d_ta": "ரயில்வே மத்தியப் பட்டியல் பதிவு 22.",
            "tip_en": "The matter remains a classic example of conflict between general federal powers (Union List Entry 53) and specialized asymmetrical constitutional compacts (Article 371A).",
            "tip_ta": "பொதுவான கூட்டாட்சி அதிகாரங்களுக்கும் (மத்தியப் பட்டியல் 53) சிறப்பு சமச்சீரற்ற அரசியலமைப்பு ஒப்பந்தங்களுக்கும் (சரத்து 371A) இடையிலான முரண்பாட்டிற்கு இது ஒரு சிறந்த உதாரணமாகும்.",
            "fact_en": "Nagaland possesses an estimated 600 million metric tonnes of crude oil reserves, primarily in the Champang area of Wokha district.",
            "fact_ta": "நாகாலாந்தின் வோகா மாவட்டத்தின் சம்பாங் பகுதியில் சுமார் 600 மில்லியன் மெட்ரிக் டன் கச்சா எண்ணெய் வளம் இருப்பதாக மதிப்பிடப்பட்டுள்ளது."
        },
        # 23
        {
            "subtopic": "Sixth Schedule Para 12A Meghalaya/Assam Laws",
            "stem_en": "Under Paragraph 12A of the Sixth Schedule, if any provision of a law made by an Autonomous District Council in Meghalaya is repugnant to a law made by the State Legislature of Meghalaya, what is the rule of priority?",
            "stem_ta": "ஆறாவது அட்டவணையின் பத்தி 12A-ன் கீழ், மேகாலயாவில் உள்ள ஒரு தன்னாட்சி மாவட்டக் குழு இயற்றிய சட்டத்தின் விதி, மேகாலயா மாநில சட்டமன்றம் இயற்றிய சட்டத்திற்கு முரணாக இருந்தால், முன்னுரிமை விதி என்ன?",
            "options": [
                ("The law made by the State Legislature of Meghalaya shall prevail, and the District Council law shall be void to the extent of the repugnancy", "மேகாலயா மாநில சட்டமன்றம் இயற்றிய சட்டமே மேலோங்கும், மேலும் முரண்படும் வரையில் மாவட்டக் குழுவின் சட்டம் செல்லாததாகும்"),
                ("The District Council law shall automatically override the State law in all circumstances", "எல்லா சூழ்நிலைகளிலும் மாவட்டக் குழுவின் சட்டமே தானாக மாநிலச் சட்டத்தை விட மேலோங்கும்"),
                ("Both laws are automatically suspended until referred to the International Court of Justice", "சர்வதேச நீதிமன்றத்திற்கு அனுப்பப்படும் வரை இரு சட்டங்களும் தானாக இடைநிறுத்தப்படும்"),
                ("The Chief Justice of the Gauhati High Court casts the deciding vote", "குவஹாத்தி உயர் நீதிமன்றத் தலைமை நீதிபதி தீர்மானிக்கும் வாக்கை அளிக்கிறார்")
            ],
            "correct_key": "A",
            "exp_en": "Under Paragraph 12A(a) (inserted by the 22nd Amendment 1969), if any provision of a law made by a District or Regional Council in Meghalaya is repugnant to any provision of a law made by the Legislature of the State of Meghalaya, the law made by the Legislature of the State of Meghalaya shall prevail and the law made by the District or Regional Council shall, to the extent of the repugnancy, be void.",
            "exp_ta": "ஆறாவது அட்டவணையின் பத்தி 12A(a)-ன் படி, மேகாலயாவில் உள்ள மாவட்டக் குழுவின் சட்டம் மாநில சட்டமன்றத்தின் சட்டத்திற்கு முரணாக இருந்தால், மாநில சட்டமன்றம் இயற்றிய சட்டமே மேலோங்கும்; முரண்படும் அளவுக்கு மாவட்டக் குழுவின் சட்டம் செல்லாததாகும்.",
            "why_a_en": "Paragraph 12A explicitly establishes the supremacy of State Legislature laws over District Council laws in Meghalaya.",
            "why_a_ta": "பத்தி 12A மேகாலயாவில் மாவட்டக் குழு சட்டங்களை விட மாநில சட்டமன்ற சட்டங்களின் மேலாதிக்கத்தை தெளிவாக நிறுவுகிறது.",
            "why_b_en": "District Council laws do not possess supremacy over State enactments under Para 12A.",
            "why_b_ta": "மாவட்டக் குழு சட்டங்களுக்கு மாநில சட்டங்களை விட மேலாதிக்கம் இல்லை.",
            "why_c_en": "Domestic federal repugnancy rules (Article 254 principle) resolve the conflict, not the ICJ.",
            "why_c_ta": "உள்நாட்டு அரசியலமைப்பு விதிகளே முரண்பாட்டைத் தீர்க்கின்றன.",
            "why_d_en": "Judicial review determines repugnancy, but judges do not 'vote' on statutory validity.",
            "why_d_ta": "நீதிமன்றங்கள் சட்ட முரண்பாட்டைத் தீர்மானிக்கின்றன, வாக்களிப்பதில்லை.",
            "tip_en": "In Assam (Para 12), the Governor resolves repugnancy between State and Council laws; in Meghalaya (Para 12A), the State Legislature enjoys automatic constitutional priority.",
            "tip_ta": "அசாமில் (பத்தி 12) ஆளுநர் முரண்பாட்டைத் தீர்க்கிறார்; மேகாலயாவில் (பத்தி 12A) மாநில சட்டமன்றமே தானியங்கி அரசியலமைப்பு முன்னுரிமை பெறுகிறது.",
            "fact_en": "This provision was specifically negotiated during the creation of Meghalaya as an autonomous sub-state in 1969.",
            "fact_ta": "1969-ல் மேகாலயா தன்னாட்சி மாநிலமாக உருவாக்கப்பட்டபோது இந்த விதி பிரத்யேகமாக சேர்க்கப்பட்டது."
        },
        # 24
        {
            "subtopic": "Article 338B Constitutional Functions",
            "stem_en": "Which of the following is NOT a constitutional function of the National Commission for Backward Classes under Article 338B(5)?",
            "stem_ta": "சரத்து 338B(5)-ன் கீழ் பிற்படுத்தப்பட்ட வகுப்பினருக்கான தேசிய ஆணையத்தின் (NCBC) அரசியலமைப்புப் பணியாக இல்லாதது எது?",
            "options": [
                ("Passing binding judicial decrees of divorce and partition between OBC family members", "OBC குடும்ப உறுப்பினர்களுக்கு இடையே விவாகரத்து மற்றும் பாகப்பிரிவினைக்கான கட்டாய நீதித்துறைத் தீர்ப்புகளை வழங்குவது"),
                ("Investigating and monitoring all matters relating to the safeguards provided for the socially and educationally backward classes", "சமூக மற்றும் கல்வி ரீதியாக பிற்படுத்தப்பட்ட வகுப்பினருக்கு வழங்கப்பட்டுள்ள பாதுகாப்புகள் தொடர்பான அனைத்து விவகாரங்களையும் கண்காணித்தல் மற்றும் விசாரித்தல்"),
                ("Inquiring into specific complaints with respect to the deprivation of rights and safeguards of SEBCs", "SEBC பிரிவினரின் உரிமைகள் மற்றும் பாதுகாப்புகள் பறிக்கப்படுவது குறித்த குறிப்பிட்ட புகார்களை விசாரித்தல்"),
                ("Participating and advising on the socio-economic development of SEBCs and evaluating their progress", "SEBC பிரிவினரின் சமூக-பொருளாதார வளர்ச்சி குறித்து பங்கேற்று ஆலோசனை வழங்குதல் மற்றும் அவர்களின் முன்னேற்றத்தை மதிப்பீடு செய்தல்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 338B(5), NCBC investigates safeguards, inquires into rights deprivations, advises on socio-economic planning, and presents annual reports. It has civil court powers only for inquiry (summoning/documents), but does NOT have judicial authority to try matrimonial or civil partition suits.",
            "exp_ta": "சரத்து 338B(5)-ன் கீழ், NCBC பாதுகாப்புகளைக் கண்காணிக்கிறது, புகார்களை விசாரிக்கிறது மற்றும் ஆலோசனை வழங்குகிறது. விசாரணைக்கு மட்டுமே உரிமையியல் நீதிமன்ற அதிகாரம் உண்டு; குடும்ப விவாகரத்து அல்லது பாகப்பிரிவினை வழக்குகளை விசாரிக்கும் நீதித்துறை அதிகாரம் இதற்கு கிடையாது.",
            "why_a_en": "NCBC has no power to adjudicate civil family disputes or grant divorces.",
            "why_a_ta": "குடும்பத் தகராறுகளைத் தீர்க்கவோ விவாகரத்து வழங்கவோ NCBC-க்கு அதிகாரம் இல்லை.",
            "why_b_en": "Investigating safeguards is clause (a) of Article 338B(5).",
            "why_b_ta": "பாதுகாப்புகளைக் கண்காணிப்பது சரத்து 338B(5)(a)-ன் பணியாகும்.",
            "why_c_en": "Inquiring into complaints is clause (b) of Article 338B(5).",
            "why_c_ta": "புகார்களை விசாரிப்பது சரத்து 338B(5)(b)-ன் பணியாகும்.",
            "why_d_en": "Socio-economic planning advice is clause (c) of Article 338B(5).",
            "why_d_ta": "வளர்ச்சி ஆலோசனை வழங்குவது சரத்து 338B(5)(c)-ன் பணியாகும்.",
            "tip_en": "In All India Indian Overseas Bank SC/ST Employees Welfare Association (1996), the SC affirmed that these commissions cannot issue binding injunctions or court orders.",
            "tip_ta": "1996-ன் இந்தியன் ஓவர்சீஸ் வங்கி வழக்கில், இவ்வாணையங்கள் நீதிமன்றங்களைப் போல கட்டாயத் தடைக் கட்டளைகளைப் பிறப்பிக்க முடியாது என உச்ச நீதிமன்றம் உறுதி செய்தது.",
            "fact_en": "NCBC's powers were modeled directly on those of NCSC (Art 338) and NCST (Art 338A).",
            "fact_ta": "NCBC-ன் அதிகாரங்கள் NCSC (338) மற்றும் NCST (338A) ஆகியவற்றின் அதிகாரங்களை ஒட்டியே வடிவமைக்கப்பட்டுள்ளன."
        },
        # 25
        {
            "subtopic": "Article 15(6) and 16(6) EWS Income Ceiling",
            "stem_en": "Under the Explanations to Articles 15(6) and 16(6), who is empowered to notify the criteria for 'economically weaker sections' and on what basis?",
            "stem_ta": "சரத்துகள் 15(6) மற்றும் 16(6)-ன் விளக்கங்களின்படி, 'பொருளாதாரத்தில் நலிவடைந்த பிரிவினருக்கான' அளவுகோல்களை அறிவிக்கும் அதிகாரம் யாருக்கு உள்ளது மற்றும் எந்த அடிப்படையில்?",
            "options": [
                ("The State may notify the criteria from time to time on the basis of family income and other indicators of economic disadvantage", "குடும்ப வருமானம் மற்றும் பொருளாதாரப் பின்தங்கிய நிலையின் பிற குறிகாட்டிகளின் அடிப்படையில் அரசு அவ்வப்போது அளவுகோல்களை அறிவிக்கலாம்"),
                ("The Reserve Bank of India strictly on the basis of bank account balances", "வங்கிக் கணக்கு இருப்பின் அடிப்படையில் இந்திய ரிசர்வ் வங்கி மட்டுமே"),
                ("The Comptroller and Auditor General based on tax evasion statistics", "வரி ஏய்ப்பு புள்ளிவிவரங்களின் அடிப்படையில் கணக்காய்வாளர் மற்றும் தணிக்கைத் தலைவர்"),
                ("The International Monetary Fund on purchasing power parity criteria", "வாங்கும் திறன் சமநிலை அளவுகோலின் அடிப்படையில் சர்வதேச நாணய நிதியம்")
            ],
            "correct_key": "A",
            "exp_en": "The Explanation to Article 15 and Article 16 provides: 'For the purposes of this article and article 16, \"economically weaker sections\" shall be such as may be notified by the State from time to time on the basis of family income and other indicators of economic disadvantage.'",
            "exp_ta": "சரத்து 15 மற்றும் 16-ன் விளக்கம் கூறுகிறது: 'இச்சரத்து மற்றும் சரத்து 16-ன் நோக்கங்களுக்காக, \"பொருளாதாரத்தில் நலிவடைந்த பிரிவினர்\" என்பது குடும்ப வருமானம் மற்றும் பொருளாதாரப் பின்தங்கிய நிலையின் பிற குறிகாட்டிகளின் அடிப்படையில் அரசால் அவ்வப்போது அறிவிக்கப்படும் பிரிவினரைக் குறிக்கும்.'",
            "why_a_en": "The constitutional text explicitly empowers 'the State' to notify criteria based on family income and economic disadvantage.",
            "why_a_ta": "குடும்ப வருமானம் மற்றும் பொருளாதார நிலையின் அடிப்படையில் அரசு அறிவிக்கலாம் என அரசியலமைப்பு வாசகம் தெளிவாகக் கூறுகிறது.",
            "why_b_en": "RBI has no constitutional role in affirmative action criteria notifications.",
            "why_b_ta": "இடஒதுக்கீட்டு அளவுகோல் அறிவிப்பில் RBI-க்கு எந்தப் பங்கும் இல்லை.",
            "why_c_en": "CAG performs audit, not economic policy notification.",
            "why_c_ta": "CAG தணிக்கை அமைப்பாகும், கொள்கை அறிவிக்கும் அமைப்பு அல்ல.",
            "why_d_en": "IMF has no authority in domestic constitutional entitlements.",
            "why_d_ta": "உள்நாட்டு அரசியலமைப்பு விவகாரங்களில் IMF-க்கு அதிகாரம் இல்லை.",
            "tip_en": "Presently, the Central Government has fixed an annual family gross income limit of Rs. 8 lakh alongside land holding thresholds to define EWS.",
            "tip_ta": "தற்போது மத்திய அரசு EWS பிரிவை வரையறுக்க ஆண்டு மொத்த குடும்ப வருமான வரம்பாக ரூ. 8 லட்சத்தையும், குறிப்பிட்ட நில வரம்புகளையும் நிர்ணயித்துள்ளது.",
            "fact_en": "The Supreme Court in Neil Aurelio Nunes (2022) upheld the validity of the Rs. 8 lakh threshold for NEET admissions as a policy determination.",
            "fact_ta": "நீல் நூன்ஸ் வழக்கில் (2022) நீட் சேர்க்கைக்கான ரூ. 8 லட்சம் வருமான வரம்பை ஒரு கொள்கை முடிவாக உச்ச நீதிமன்றம் ஏற்றுக்கொண்டது."
        },
        # 26
        {
            "subtopic": "Articles 371 to 371J Constitutional Analysis",
            "stem_en": "Match the State with its governing constitutional article in Part XXI:\n1. Nagaland\n2. Manipur\n3. Sikkim\n4. Karnataka\nWhich of the following correct combinations represents the constitutional matching?",
            "stem_ta": "பகுதி XXI-ல் உள்ள அரசியலமைப்புச் சரத்துடன் மாநிலத்தைப் பொருத்துக:\n1. நாகாலாந்து\n2. மணிப்பூர்\n3. சிக்கிம்\n4. கர்நாடகா\nபின்வரும் சரியான சேர்க்கைகளில் எது அரசியலமைப்புப் பொருத்தத்தைக் குறிக்கிறது?",
            "options": [
                ("1-Article 371A, 2-Article 371C, 3-Article 371F, 4-Article 371J", "1-சரத்து 371A, 2-சரத்து 371C, 3-சரத்து 371F, 4-சரத்து 371J"),
                ("1-Article 371B, 2-Article 371A, 3-Article 371G, 4-Article 371I", "1-சரத்து 371B, 2-சரத்து 371A, 3-சரத்து 371G, 4-சரத்து 371I"),
                ("1-Article 371D, 2-Article 371E, 3-Article 371H, 4-Article 371F", "1-சரத்து 371D, 2-சரத்து 371E, 3-சரத்து 371H, 4-சரத்து 371F"),
                ("1-Article 371, 2-Article 371B, 3-Article 371C, 4-Article 371D", "1-சரத்து 371, 2-சரத்து 371B, 3-சரத்து 371C, 4-சரத்து 371D")
            ],
            "correct_key": "A",
            "exp_en": "Correct pairings: Nagaland = Article 371A (13th CAA 1962); Manipur = Article 371C (27th CAA 1971); Sikkim = Article 371F (36th CAA 1975); Karnataka = Article 371J (98th CAA 2012).",
            "exp_ta": "சரியான பொருத்தங்கள்: நாகாலாந்து = சரத்து 371A (13வது திருத்தம் 1962); மணிப்பூர் = சரத்து 371C (27வது திருத்தம் 1971); சிக்கிம் = சரத்து 371F (36வது திருத்தம் 1975); கர்நாடகா = சரத்து 371J (98வது திருத்தம் 2012).",
            "why_a_en": "Matches all four states to their exact governing constitutional articles.",
            "why_a_ta": "நான்கு மாநிலங்களையும் அவற்றின் துல்லியமான அரசியலமைப்பு சரத்துகளுடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "371B is Assam, not Nagaland.",
            "why_b_ta": "371B அசாம், நாகாலாந்து அல்ல.",
            "why_c_en": "371D is AP/Telangana, not Nagaland.",
            "why_c_ta": "371D ஆந்திரா/தெலங்கானா, நாகாலாந்து அல்ல.",
            "why_d_en": "371 is Maharashtra and Gujarat, not Nagaland.",
            "why_d_ta": "371 மகாராஷ்டிரா மற்றும் குஜராத், நாகாலாந்து அல்ல.",
            "tip_en": "Recall the mnemonic: A-Nagaland, B-Assam, C-Manipur, D/E-Andhra, F-Sikkim, G-Mizoram, H-Arunachal, I-Goa, J-Karnataka.",
            "tip_ta": "சுருக்குவழியை நினைவில் கொள்க: A-நாகா, B-அசாம், C-மணிப்பூர், D/E-ஆந்திரா, F-சிக்கிம், G-மிசோரம், H-அருணாச்சல், I-கோவா, J-கர்நாடகா.",
            "fact_en": "Articles 371 to 371J are a hallmark of India's dynamic asymmetrical constitutional design.",
            "fact_ta": "சரத்துகள் 371 முதல் 371J வரை இந்தியாவின் சமச்சீரற்ற அரசியலமைப்பு வடிவமைப்பின் அடையாளமாகும்."
        },
        # 27
        {
            "subtopic": "Article 334 Historical Intent",
            "stem_en": "During the Constituent Assembly debates, why was a 10-year sunset clause placed on legislative seat reservation under Article 334, while no such time limit was imposed on Articles 15 and 16?",
            "stem_ta": "அரசியல் நிர்ணய சபை விவாதங்களின் போது, சரத்துகள் 15 மற்றும் 16-க்கு கால வரம்பு விதிக்கப்படாத நிலையில், சரத்து 334-ன் கீழ் சட்டமன்ற இடஒதுக்கீட்டிற்கு மட்டும் 10 ஆண்டு கால வரம்பு ஏன் விதிக்கப்பட்டது?",
            "options": [
                ("Political reservation was viewed as a temporary transitional measure for integration, whereas socio-economic affirmative action was recognized as a continuous constitutional duty until structural equality is achieved", "அரசியல் இடஒதுக்கீடு என்பது ஒருங்கிணைப்பிற்கான ஒரு தற்காலிக இடைக்கால நடவடிக்கையாகக் கருதப்பட்டது; ஆனால் சமூக-பொருளாதார இடஒதுக்கீடு கட்டமைப்பு சமத்துவம் எட்டப்படும் வரை தொடர வேண்டிய ஒரு தொடர்ச்சியான அரசியலமைப்புக் கடமையாக அங்கீகரிக்கப்பட்டது"),
                ("The framers believed that all caste distinctions would be completely wiped out by legal enactment within exactly five years", "சட்டத்தின் மூலம் சரியாக ஐந்து ஆண்டுகளுக்குள் அனைத்து சாதி வேறுபாடுகளும் முற்றிலும் துடைத்தெறியப்படும் என்று நிறுவனர்கள் நம்பினர்"),
                ("The Government of India Act 1935 strictly prohibited affirmative action in employment beyond ten years", "1935 இந்திய அரசு சட்டம் வேலைவாய்ப்பில் 10 ஆண்டுகளுக்கு மேல் இடஒதுக்கீடு செய்வதைத் திட்டவட்டமாகத் தடை செய்தது"),
                ("The Privy Council had issued a mandatory binding order that legislative quotas must expire in 1960", "சட்டமன்ற இடஒதுக்கீடு 1960-ல் காலாவதியாக வேண்டும் என்று பிரிவி கவுன்சில் கட்டாய உத்தரவு பிறப்பித்திருந்தது")
            ],
            "correct_key": "A",
            "exp_en": "Dr. Ambedkar and the Advisory Committee intentionally bifurcated political reservation from educational and employment safeguards. Political reservation creates separate electoral identities that were meant to fade as backward communities gained democratic confidence. In contrast, Articles 15(4) and 16(4) are permanent enabling provisions realizing the Preamble's promise of equality of opportunity.",
            "exp_ta": "டாக்டர் அம்பேத்கரும் ஆலோசனைக் குழுவும் அரசியல் இடஒதுக்கீட்டை கல்வி மற்றும் வேலைவாய்ப்புப் பாதுகாப்புகளிலிருந்து வேண்டுமென்றே பிரித்தனர். அரசியல் இடஒதுக்கீடு என்பது தற்காலிகமானது; சமூகம் தன்னம்பிக்கை பெறும்போது அது மறைய வேண்டும் எனக் கருதப்பட்டது. மாறாக, சரத்துகள் 15(4) மற்றும் 16(4) ஆகியவை வாய்ப்பில் சமத்துவம் என்ற முகப்புரையின் வாக்குறுதியை நிறைவேற்றும் நிரந்தர வழிகாட்டு விதிகளாகும்.",
            "why_a_en": "Accurately articulates the philosophical distinction between temporary political quotas and permanent affirmative action.",
            "why_a_ta": "தற்காலிக அரசியல் ஒதுக்கீட்டிற்கும் நிரந்தர சமூக இடஒதுக்கீட்டிற்கும் இடையிலான தத்துவார்த்த வேறுபாட்டை துல்லியமாக விளக்குகிறது.",
            "why_b_en": "The framers were realists who understood that centuries of caste discrimination could not vanish in 5 years.",
            "why_b_ta": "நூற்றாண்டுகால சாதிப் பாகுபாடு 5 ஆண்டுகளில் மறையாது என்பதை நிறுவனர்கள் அறிந்திருந்தனர்.",
            "why_c_en": "1935 Act contained communal awards, not modern affirmative action.",
            "why_c_ta": "1935 சட்டம் வகுப்புவாத விருதுகளைக் கொண்டிருந்தது.",
            "why_d_en": "Privy Council jurisdiction was abolished by India prior to 1950.",
            "why_d_ta": "1950-க்கு முன்பே பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிக்கப்பட்டது.",
            "tip_en": "Article 334 covers political seats in Parliament and Assemblies; Articles 15(4) and 16(4) cover colleges and government jobs.",
            "tip_ta": "சரத்து 334 சட்டமன்ற இடங்களைக் கையாள்கிறது; சரத்துகள் 15(4) மற்றும் 16(4) கல்லூரிகள் மற்றும் அரசுப் பணிகளைக் கையாள்கின்றன.",
            "fact_en": "Despite the original 10-year vision, deep structural inequalities have necessitated successive decennial extensions of Article 334.",
            "fact_ta": "அசல் 10 ஆண்டு கால நோக்கம் இருந்தபோதிலும், சமூக ஏற்றத்தாழ்வுகள் நீடிப்பதால் சரத்து 334 தொடர்ந்து ஒவ்வொரு 10 ஆண்டுகளுக்கும் நீட்டிக்கப்பட்டு வருகிறது."
        },
        # 28
        {
            "subtopic": "Article 371D Presidential Power over Education",
            "stem_en": "Under Article 371D(2)(c)(i), the President may by order specify the parts of the State of Andhra Pradesh and Telangana to be treated as local areas for admission to:",
            "stem_ta": "சரத்து 371D(2)(c)(i)-ன் கீழ், ஆந்திரா மற்றும் தெலங்கானாவில் எதில் சேர்க்கை பெறுவதற்காக குறிப்பிட்ட பகுதிகளை உள்ளூர் பகுதிகளாகக் கருத குடியரசுத் தலைவர் ஆணை பிறப்பிக்கலாம்?",
            "options": [
                ("Any University or other educational institution which is subject to the control of the State Government", "மாநில அரசின் கட்டுப்பாட்டிற்கு உட்பட்ட எந்தவொரு பல்கலைக்கழகம் அல்லது பிற கல்வி நிறுவனம்"),
                ("All Indian Institutes of Technology (IITs) and IIMs across India", "இந்தியா முழுவதும் உள்ள அனைத்து IIT மற்றும் IIM நிறுவனங்கள்"),
                ("Private foreign universities operating in Singapore", "சிங்கப்பூரில் செயல்படும் தனியார் வெளிநாட்டுப் பல்கலைக்கழகங்கள்"),
                ("Military training academies under the Ministry of Defence", "பாதுகாப்பு அமைச்சகத்தின் கீழான ராணுவப் பயிற்சிக் கல்லூரிகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371D(2)(c)(i) explicitly authorizes the President to specify the parts of the State to be treated as local areas for the purpose of admission to any University or other educational institution which is subject to the control of the State Government.",
            "exp_ta": "சரத்து 371D(2)(c)(i), மாநில அரசின் கட்டுப்பாட்டிற்கு உட்பட்ட எந்தவொரு பல்கலைக்கழகம் அல்லது பிற கல்வி நிறுவனத்தில் சேர்க்கை பெறுவதற்காக, மாநிலத்தின் குறிப்பிட்ட பகுதிகளை உள்ளூர் பகுதிகளாகக் கருத குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Article 371D applies specifically to universities and colleges subject to the control of the State Government.",
            "why_a_ta": "சரத்து 371D குறிப்பாக மாநில அரசின் கட்டுப்பாட்டில் உள்ள பல்கலைக்கழகங்கள் மற்றும் கல்லூரிகளுக்குப் பொருந்தும்.",
            "why_b_en": "Institutions of national importance (IITs/IIMs) under Union List Entry 63/64 are exempt from state local area quotas.",
            "why_b_ta": "தேசிய முக்கியத்துவம் வாய்ந்த மத்திய நிறுவனங்களுக்கு (IIT/IIM) மாநில உள்ளூர் ஒதுக்கீடு பொருந்தாது.",
            "why_c_en": "Foreign universities are outside the territorial scope of the Constitution.",
            "why_c_ta": "வெளிநாட்டுப் பல்கலைக்கழகங்கள் எல்லைக்கு அப்பாற்பட்டவை.",
            "why_d_en": "Defense academies are exclusive Union defense institutions.",
            "why_d_ta": "ராணுவ அகாடமிகள் மத்திய அரசின் பாதுகாப்பு நிறுவனங்கள்.",
            "tip_en": "The 1974 Presidential Order created Andhra, Osmania, and Sri Venkateswara University zones to protect local students.",
            "tip_ta": "1974-ன் குடியரசுத் தலைவர் ஆணை உள்ளூர் மாணவர்களைப் பாதுகாக்க ஆந்திரா, உஸ்மானியா மற்றும் ஸ்ரீ வெங்கடேஸ்வரா பல்கலைக்கழக மண்டலங்களை உருவாக்கியது.",
            "fact_en": "Even after the 2014 bifurcation of Andhra Pradesh, Section 95 of the AP Reorganisation Act 2014 maintained this quota parity for 10 years.",
            "fact_ta": "2014 ஆந்திரப் பிரிவினைக்குப் பிறகும், 2014 சட்டத்தின் பிரிவு 95 இக்கல்வி ஒதுக்கீட்டு சமநிலையை 10 ஆண்டுகளுக்குத் தொடரச் செய்தது."
        },
        # 29
        {
            "subtopic": "Article 371F Subordinate Judiciary",
            "stem_en": "Under Article 371F(i), High Court and subordinate court judges holding office immediately before the merger of Sikkim became judges of the new High Court and subordinate courts, subject to:",
            "stem_ta": "சரத்து 371F(i)-ன் கீழ், சிக்கிம் இணைவதற்கு முன் பதவியில் இருந்த உயர் நீதிமன்ற மற்றும் சார்பு நீதிமன்ற நீதிபதிகள், எதற்கு உட்பட்டு புதிய உயர் நீதிமன்றம் மற்றும் சார்பு நீதிமன்ற நீதிபதிகளாக மாறினர்?",
            "options": [
                ("The provisions of the Constitution of India, including conditions of service and retirement age under Part VI", "பகுதி VI-ன் கீழான பணி நிபந்தனைகள் மற்றும் ஓய்வு வயது உட்பட இந்திய அரசியலமைப்பின் விதிகளுக்கு உட்பட்டு"),
                ("The continuing absolute pleasure of the hereditary Chogyal", "பரம்பரை சோக்யாலின் தொடர்ச்சியான விருப்பத்திற்கு உட்பட்டு"),
                ("Holding dual citizenship of both India and the United Kingdom", "இந்தியா மற்றும் இங்கிலாந்து ஆகிய இரு நாடுகளின் இரட்டைக் குடியுரிமைக்கு உட்பட்டு"),
                ("Taking a re-examination conducted by the Privy Council of London", "லண்டன் பிரிவி கவுன்சில் நடத்தும் மறு தேர்வை எழுதுவதற்கு உட்பட்டு")
            ],
            "correct_key": "A",
            "exp_en": "Article 371F(i) provided that High Court judges holding office in Sikkim immediately before the appointed day became judges of the High Court for the State of Sikkim under the Constitution, and their tenure, powers, and service conditions became subject to Chapter V of Part VI of the Constitution.",
            "exp_ta": "சரத்து 371F(i) இணைப்பிற்கு முன் பதவியில் இருந்த சிக்கிம் உயர் நீதிமன்ற நீதிபதிகள் அரசியலமைப்பின் கீழான சிக்கிம் உயர் நீதிமன்ற நீதிபதிகளாக மாறினர் என்றும்; அவர்களின் பதவிக்காலம், அதிகாரங்கள் மற்றும் பணி நிபந்தனைகள் பகுதி VI, அத்தியாயம் V-ன் விதிகளுக்கு உட்பட்டதாக மாறியது என்றும் கூறியது.",
            "why_a_en": "Judicial integration meant absorbing existing judges under Part VI constitutional framework.",
            "why_a_ta": "நீதித்துறை ஒருங்கிணைப்பு என்பது பழைய நீதிபதிகளை பகுதி VI அரசியலமைப்பு கட்டமைப்பின் கீழ் இணைப்பதாகும்.",
            "why_b_en": "Chogyal's royal pleasure was replaced by the Indian Constitution.",
            "why_b_ta": "சோக்யாலின் விருப்பம் இந்திய அரசியலமைப்பால் மாற்றியமைக்கப்பட்டது.",
            "why_c_en": "India does not permit dual citizenship under Article 9.",
            "why_c_ta": "சரத்து 9-ன் கீழ் இந்தியா இரட்டைக் குடியுரிமையை அனுமதிப்பதில்லை.",
            "why_d_en": "Privy Council has no standing in republican India.",
            "why_d_ta": "குடியரசு இந்தியாவில் பிரிவி கவுன்சிலுக்கு இடமில்லை.",
            "tip_en": "Sikkim High Court is one of the smallest High Courts in India, having a sanctioned strength of 3 judges.",
            "tip_ta": "சிக்கிம் உயர் நீதிமன்றம் இந்தியாவில் உள்ள மிகச் சிறிய உயர் நீதிமன்றங்களில் ஒன்றாகும்; இது 3 நீதிபதிகள் பலத்தைக் கொண்டுள்ளது.",
            "fact_en": "Article 371F(j) contained a parallel integration provision for all civil servants serving in Sikkim.",
            "fact_ta": "சரத்து 371F(j) சிக்கிமில் பணியாற்றிய அனைத்து அரசு ஊழியர்களுக்கும் இதே போன்ற இணைக்கும் விதியைக் கொண்டிருந்தது."
        },
        # 30
        {
            "subtopic": "Article 341 Religious Criteria",
            "stem_en": "Under Paragraph 3 of the Constitution (Scheduled Castes) Order, 1950 issued under Article 341, no person who professes a religion different from which three religions can be deemed to be a member of a Scheduled Caste?",
            "stem_ta": "சரத்து 341-ன் கீழ் வெளியிடப்பட்ட 1950 அரசியலமைப்பு (பட்டியலிடப்பட்ட சாதியினர்) ஆணையின் பத்தி 3-ன் படி, எந்த மூன்று மதங்களைத் தவிர்த்த பிற மதத்தைப் பின்பற்றும் எந்தவொரு நபரும் SC உறுப்பினராகக் கருதப்பட முடியாது?",
            "options": [
                ("Hindu, Sikh, or Buddhist religions", "இந்து, சீக்கிய அல்லது பௌத்த மதங்கள்"),
                ("Hindu, Muslim, or Christian religions", "இந்து, முஸ்லிம் அல்லது கிறிஸ்தவ மதங்கள்"),
                ("Jain, Parsi, or Jewish religions", "சமண, பார்சி அல்லது யூத மதங்கள்"),
                ("Any recognized religion across the world uniformly", "உலகில் உள்ள எந்தவொரு அங்கீகரிக்கப்பட்ட மதமும் ஒரே சீராக")
            ],
            "correct_key": "A",
            "exp_en": "Paragraph 3 of the Constitution (Scheduled Castes) Order, 1950 originally restricted SC status to Hindus. It was amended in 1956 to include Sikhs, and in 1990 to include Buddhists (Neo-Buddhists). Persons professing Islam, Christianity, or other religions are not eligible for SC status under current constitutional orders.",
            "exp_ta": "1950-ன் அரசியலமைப்பு (SC) ஆணை முதலில் SC அந்தஸ்தை இந்துக்களுக்கு மட்டுமே வழங்கியது. பின்னர் 1956-ல் சீக்கியர்களையும், 1990-ல் பௌத்தர்களையும் உள்ளடக்கும் வகையில் திருத்தப்பட்டது. தற்போதைய அரசியலமைப்பு ஆணைகளின் கீழ் இஸ்லாம், கிறிஸ்தவம் அல்லது பிற மதங்களைப் பின்பற்றுபவர்கள் SC அந்தஸ்திற்கு தகுதியற்றவர்கள்.",
            "why_a_en": "Currently, only persons professing Hinduism, Sikhism (added 1956), or Buddhism (added 1990) can be Scheduled Castes.",
            "why_a_ta": "தற்போது இந்து, சீக்கியர் (1956 சேர்க்கை) அல்லது பௌத்த (1990 சேர்க்கை) மதங்களைப் பின்பற்றுபவர்கள் மட்டுமே SC-யாக இருக்க முடியும்.",
            "why_b_en": "Muslims and Christians are not recognized as Scheduled Castes under the 1950 Order.",
            "why_b_ta": "1950 ஆணையின் கீழ் முஸ்லிம்களும் கிறிஸ்தவர்களும் SC-யாக அங்கீகரிக்கப்படவில்லை.",
            "why_c_en": "Jains, Parsis, Jews are not included in SC definitions.",
            "why_c_ta": "சமணர்கள், பார்சிகள், யூதர்கள் SC வரையறையில் இல்லை.",
            "why_d_en": "Scheduled Caste status has a specific statutory religious boundary unlike ST status.",
            "why_d_ta": "ST அந்தஸ்தைப் போலன்றி, SC அந்தஸ்திற்கு குறிப்பிட்ட சட்டப்பூர்வ மத எல்லை உள்ளது.",
            "tip_en": "Contrast: Scheduled Tribe (ST) status under Article 342 is completely religion-neutral (STs can belong to any religion or practice animism).",
            "tip_ta": "முக்கிய வேறுபாடு: சரத்து 342-ன் கீழான பழங்குடியினர் (ST) அந்தஸ்து முற்றிலும் மதச்சார்பற்றது (ST பிரிவினர் எந்த மதத்தையும் பின்பற்றலாம்).",
            "fact_en": "The Justice K.G. Balakrishnan Commission is currently examining the demand to extend SC status to Dalit converts to Christianity and Islam.",
            "fact_ta": "கிறிஸ்தவம் மற்றும் இஸ்லாத்திற்கு மாறிய தலித்துகளுக்கு SC அந்தஸ்து வழங்குவது குறித்து நீதிபதி கே.ஜி. பாலகிருஷ்ணன் ஆணையம் தற்போது ஆய்வு செய்து வருகிறது."
        },
        # 31
        {
            "subtopic": "Article 330/332 General Seats Contesting",
            "stem_en": "In V.V. Giri v. D. Suri Dora (1959), the Supreme Court ruled on whether a member of a Scheduled Tribe can contest and get elected from an unreserved (General) seat in the Lok Sabha. What did the Court hold?",
            "stem_ta": "வி.வி. கிரி எதிர் டி. சூரி டோரா (1959) வழக்கில், ஒரு பட்டியலிடப்பட்ட பழங்குடியினர் மக்களவையில் பொதுத் தொகுதியிலிருந்து போட்டியிட்டு தேர்ந்தெடுக்கப்பட முடியுமா என்பது குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "options": [
                ("A reserved category candidate (SC/ST) is fully entitled to contest and get elected from a General/Unreserved constituency, as reservation does not disable their common franchise rights", "பொது/ஒதுக்கப்படாத தொகுதியிலிருந்து போட்டியிட்டு தேர்ந்தெடுக்கப்பட SC/ST பிரிவினருக்கு முழு உரிமை உண்டு; ஏனெனில் இடஒதுக்கீடு அவர்களின் பொதுவான வாக்குரிமை மற்றும் போட்டி உரிமையைப் பறிக்காது"),
                ("Reserved category candidates are constitutionally barred from ever filing nominations in general constituencies", "பொதுத் தொகுதிகளில் வேட்புமனு தாக்கல் செய்ய இடஒதுக்கீட்டுப் பிரிவினருக்கு அரசியலமைப்பு ரீதியாக தடை விதிக்கப்பட்டுள்ளது"),
                ("A candidate from a reserved category can contest general seats only if no general candidates file nominations", "பொதுப்பிரிவு வேட்பாளர்கள் எவரும் வேட்புமனு தாக்கல் செய்யாத பட்சத்தில் மட்டுமே இடஒதுக்கீட்டுப் பிரிவினர் பொதுத் தொகுதிகளில் போட்டியிட முடியும்"),
                ("The President must issue an emergency proclamation before an ST member can contest a general seat", "ஒரு ST உறுப்பினர் பொதுத் தொகுதியில் போட்டியிடுவதற்கு முன் குடியரசுத் தலைவர் அவசரகால பிரகடனம் செய்ய வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "In V.V. Giri (1959), the Supreme Court held that Article 330 provides an additional safeguard by reserving seats for SC/STs, but does not take away their basic democratic right as citizens to contest from unreserved/general constituencies. If an ST candidate contests a general constituency or the general seat in a two-member constituency, their election to the general seat is completely valid.",
            "exp_ta": "வி.வி. கிரி வழக்கில் (1959), சரத்து 330 SC/ST பிரிவினருக்கு கூடுதல் பாதுகாப்பாகவே இடங்களை ஒதுக்குகிறது என்றும், அது குடிமக்கள் என்ற முறையில் பொதுத் தொகுதிகளில் போட்டியிடும் அவர்களின் அடிப்படை ஜனநாயக உரிமையைப் பறிக்காது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது. பொதுத் தொகுதியில் போட்டியிட்டு அவர்கள் வெற்றி பெறுவது முற்றிலும் செல்லுபடியாகும்.",
            "why_a_en": "The Supreme Court confirmed that SC/ST candidates retain the full right to contest open unreserved seats.",
            "why_a_ta": "SC/ST வேட்பாளர்கள் பொதுத் தொகுதிகளில் போட்டியிடும் முழு உரிமையைத் தக்க வைத்துள்ளனர் என உச்ச நீதிமன்றம் உறுதி செய்தது.",
            "why_b_en": "There is no constitutional bar preventing SC/ST candidates from contesting general seats.",
            "why_b_ta": "பொதுத் தொகுதிகளில் போட்டியிட எந்த அரசியலமைப்புத் தடையும் இல்லை.",
            "why_c_en": "General seats are open to all citizens irrespective of caste.",
            "why_c_ta": "பொதுத் தொகுதிகள் சாதி பாராமல் அனைத்து குடிமக்களுக்கும் பொதுவானவை.",
            "why_d_en": "Presidential proclamation is totally irrelevant to electoral nominations.",
            "why_d_ta": "தேர்தல் நியமனங்களில் குடியரசுத் தலைவர் பிரகடனத்திற்கு தொடர்பில்லை.",
            "tip_en": "This historic case arose from the Parvathipuram double-member parliamentary constituency in Andhra Pradesh in the 1957 elections.",
            "tip_ta": "1957 தேர்தலில் ஆந்திராவின் பார்வதிபுரம் இரட்டை உறுப்பினர் மக்களவைத் தொகுதியிலிருந்து இந்த வரலாற்று வழக்கு எழுந்தது.",
            "fact_en": "Former President V.V. Giri had lost the election in that constituency to an ST candidate who secured more votes for the general seat.",
            "fact_ta": "முன்னாள் குடியரசுத் தலைவர் வி.வி. கிரி அத்தொகுதியில் அதிக வாக்குகள் பெற்ற ஒரு ST வேட்பாளரிடம் பொது இடத்திற்கான போட்டியில் தோல்வியடைந்தார்."
        },
        # 32
        {
            "subtopic": "Article 371A Inner Line Permit Context",
            "stem_en": "Along with Article 371A, which colonial regulation continues to govern the entry of non-residents and non-indigenous persons into Nagaland, Mizoram, and Arunachal Pradesh via the Inner Line Permit (ILP)?",
            "stem_ta": "சரத்து 371A உடன் இணைந்து, உள்நுழைவு அனுமதிச் சீட்டு (ILP) மூலம் நாகாலாந்து, மிசோரம் மற்றும் அருணாச்சலப் பிரதேசத்திற்குள் வெளி நபர்கள் நுழைவதைக் கட்டுப்படுத்தும் காலனித்துவ ஒழுங்குமுறை எது?",
            "options": [
                ("Bengal Eastern Frontier Regulation, 1873", "வங்காள கிழக்கு எல்லைப்புற ஒழுங்குமுறை, 1873"),
                ("Government of India Act, 1919", "இந்திய அரசு சட்டம், 1919"),
                ("Rowlatt Act, 1919", "ரௌலட் சட்டம், 1919"),
                ("Regulating Act of 1773", "1773 ஒழுங்குமுறைச் சட்டம்")
            ],
            "correct_key": "A",
            "exp_en": "The Bengal Eastern Frontier Regulation (BEFR) of 1873 established the 'Inner Line' to protect British commercial tea and rubber interests, which post-independence was retained to protect indigenous tribal identities, cultures, and lands in Nagaland, Arunachal Pradesh, Mizoram, and subsequently Manipur (extended in 2019).",
            "exp_ta": "1873 ஆம் ஆண்டின் வங்காள கிழக்கு எல்லைப்புற ஒழுங்குமுறை (BEFR) 'உள் கோட்டை' (Inner Line) உருவாக்கியது; சுதந்திரத்திற்குப் பிறகு நாகாலாந்து, அருணாச்சல், மிசோரம் மற்றும் மணிப்பூரில் பூர்வீக பழங்குடி கலாச்சாரம், அடையாளம் மற்றும் நிலங்களைப் பாதுகாக்க இது தொடர்ந்து தக்கவைக்கப்பட்டுள்ளது.",
            "why_a_en": "BEFR 1873 is the statutory foundation of the Inner Line Permit (ILP) system.",
            "why_a_ta": "BEFR 1873 என்பது உள்நுழைவு அனுமதிச் சீட்டு (ILP) அமைப்பின் சட்டப்பூர்வ அடிப்படையாகும்.",
            "why_b_en": "1919 Act introduced dyarchy in provinces, not the Inner Line.",
            "why_b_ta": "1919 சட்டம் மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.",
            "why_c_en": "Rowlatt Act was an emergency preventive detention statute.",
            "why_c_ta": "ரௌலட் சட்டம் ஒரு தடுப்புக் காவல் சட்டமாகும்.",
            "why_d_en": "Regulating Act 1773 established the Supreme Court at Calcutta.",
            "why_d_ta": "1773 சட்டம் கல்கத்தாவில் உச்ச நீதிமன்றத்தை நிறுவியது.",
            "tip_en": "Currently, four states have ILP: Arunachal Pradesh, Nagaland, Mizoram, and Manipur (Manipur added in December 2019 via presidential order).",
            "tip_ta": "தற்போது 4 மாநிலங்கள் ILP முறையைக் கொண்டுள்ளன: அருணாச்சல், நாகாலாந்து, மிசோரம், மணிப்பூர் (மணிப்பூர் 2019 டிசம்பரில் சேர்க்கப்பட்டது).",
            "fact_en": "Citizenship Amendment Act (CAA) 2019 explicitly exempts all areas covered under the Inner Line Permit and the Sixth Schedule.",
            "fact_ta": "2019 குடியுரிமைத் திருத்தச் சட்டம் (CAA) ILP மற்றும் ஆறாவது அட்டவணையின் கீழ் உள்ள பகுதிகளுக்கு முழுமையாக விலக்கு அளித்துள்ளது."
        },
        # 33
        {
            "subtopic": "Article 371F Association History",
            "stem_en": "Before becoming the 22nd State under Article 371F, Sikkim had what unique constitutional relationship with India under the 35th Constitutional Amendment Act, 1974?",
            "stem_ta": "சரத்து 371F-ன் கீழ் 22வது மாநிலமாவதற்கு முன்பு, 1974-ன் 35வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் கீழ் சிக்கிம் இந்தியாவுடன் என்ன தனித்துவமான அரசியலமைப்பு உறவைக் கொண்டிருந்தது?",
            "options": [
                ("Associate State of the Indian Union (governed by Article 2A and the Tenth Schedule, later repealed)", "இந்திய ஒன்றியத்தின் இணை மாநிலம் (சரத்து 2A மற்றும் பத்தாவது அட்டவணையால் நிர்வகிக்கப்பட்டது, பின்னர் நீக்கப்பட்டது)"),
                ("A fully sovereign member state of the Commonwealth", "காமன்வெல்த்தின் முழு இறையாண்மை கொண்ட உறுப்பு நாடு"),
                ("A regular Union Territory without a legislative assembly", "சட்டமன்றம் இல்லாத ஒரு சாதாரண யூனியன் பிரதேசம்"),
                ("A Part C State under the direct administration of the Chief Commissioner", "தலைமை ஆணையரின் நேரடி நிர்வாகத்தின் கீழான பகுதி C மாநிலம்")
            ],
            "correct_key": "A",
            "exp_en": "The 35th Constitutional Amendment Act, 1974 introduced a novel constitutional experiment by inserting Article 2A and the Tenth Schedule, conferring on Sikkim the status of an 'Associate State' of the Indian Union, with one representative in each House of Parliament. This lasted for one year until the 36th Amendment 1975 made Sikkim a full state and repealed Art 2A.",
            "exp_ta": "1974-ன் 35வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 2A மற்றும் பத்தாவது அட்டவணையைச் சேர்த்து, சிக்கிமிற்கு இந்திய ஒன்றியத்தின் 'இணை மாநிலம்' என்ற புதிய அந்தஸ்தை அளித்து நாடாளுமன்றத்தின் இரு அவைகளிலும் தலா 1 பிரதிநிதியை வழங்கியது. இது ஒரு வருடம் மட்டுமே நீடித்தது; பின்னர் 1975-ன் 36வது திருத்தம் சிக்கிமை முழு மாநிலமாக்கி சரத்து 2A-ஐ நீக்கியது.",
            "why_a_en": "35th CAA 1974 created the unique 'Associate State' category via Article 2A.",
            "why_a_ta": "1974-ன் 35வது திருத்தம் சரத்து 2A மூலம் 'இணை மாநிலம்' என்ற புதிய வகையை உருவாக்கியது.",
            "why_b_en": "Sikkim was an Indian protectorate under the 1950 treaty, not a Commonwealth member.",
            "why_b_ta": "1950 ஒப்பந்தத்தின்படி சிக்கிம் இந்தியாவின் பாதுகாக்கப்பட்ட பகுதியாக இருந்தது.",
            "why_c_en": "Sikkim was never classified as a Union Territory.",
            "why_c_ta": "சிக்கிம் ஒருபோதும் யூனியன் பிரதேசமாக வகைப்படுத்தப்படவில்லை.",
            "why_d_en": "Part C states were abolished by the 7th Amendment 1956.",
            "why_d_ta": "பகுதி C மாநிலங்கள் 1956-ன் 7வது திருத்தத்தால் ஒழிக்கப்பட்டன.",
            "tip_en": "The original Tenth Schedule was used for Sikkim's associate terms; when repealed, the number 'Tenth Schedule' was later reused in 1985 for the Anti-Defection Law.",
            "tip_ta": "அசல் 10வது அட்டவணை சிக்கிமின் இணை மாநில விதிகளுக்காகப் பயன்பட்டது; பின்னர் அது நீக்கப்பட்டு 1985-ல் கட்சித்தாவல் தடைச் சட்டத்திற்காக மீண்டும் பயன்படுத்தப்பட்டது.",
            "fact_en": "Kazi Lhendup Dorjee became the first Chief Minister of the State of Sikkim.",
            "fact_ta": "காசி லெண்டுப் டோர்ஜி சிக்கிம் மாநிலத்தின் முதல் முதலமைச்சரானார்."
        },
        # 34
        {
            "subtopic": "Article 371G Land Protections vs Mizo Customary Law",
            "stem_en": "Under Article 371G, if the Union Parliament enacts a uniform national civil code covering marriage and divorce, what is its constitutional applicability to Mizoram?",
            "stem_ta": "சரத்து 371G-ன் கீழ், திருமணம் மற்றும் விவாகரத்து தொடர்பான பொதுவான தேசிய சிவில் சட்டத்தை நாடாளுமன்றம் இயற்றினால், மிசோரம் மாநிலத்திற்கு அதன் அரசியலமைப்புப் பொருந்தும் தன்மை என்ன?",
            "options": [
                ("It will not apply to Mizoram unless the Legislative Assembly of Mizoram by a resolution so decides", "மிசோரம் சட்டமன்றம் தீர்மானம் மூலம் அவ்வாறு முடிவு செய்யாவிட்டால் அது மிசோரமிற்குப் பொருந்தாது"),
                ("It automatically supersedes all Mizo customary laws without any state involvement", "மாநிலத்தின் எந்தத் தலையீடும் இன்றி தானாக அனைத்து மிசோ மரபுச் சட்டங்களையும் அது ரத்து செய்யும்"),
                ("It applies only to Christian inhabitants of Aizawl city", "ஐஸ்வால் நகரில் உள்ள கிறிஸ்தவ மக்களுக்கு மட்டுமே அது பொருந்தும்"),
                ("The Governor can unilaterally enforce it by declaring financial emergency", "நிதி அவசரநிலையைப் பிரகடனம் செய்வதன் மூலம் ஆளுநர் அதைத் தன்னிச்சையாக அமல்படுத்தலாம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 371G(a)(i) and (ii), no Act of Parliament in respect of religious or social practices of the Mizos, or Mizo customary law and procedure shall apply to the State of Mizoram unless the Legislative Assembly of the State of Mizoram by resolution so decides. A uniform civil code would touch customary marriage/divorce, requiring state assembly approval.",
            "exp_ta": "சரத்து 371G(a)(i) மற்றும் (ii)-ன் படி, மிசோக்களின் மத அல்லது சமூக நடைமுறைகள், அல்லது மிசோ மரபுச் சட்டம் மற்றும் நடைமுறை தொடர்பான எந்தவொரு நாடாளுமன்றச் சட்டமும், மிசோரம் சட்டமன்றம் தீர்மானம் மூலம் முடிவு செய்யாவிட்டால் பொருந்தாது. பொது சிவில் சட்டம் மரபுசார் திருமணத்தை பாதிக்கும் என்பதால் சட்டமன்ற ஒப்புதல் கட்டாயம்.",
            "why_a_en": "Article 371G explicitly shields customary family law from parliamentary override without an Assembly resolution.",
            "why_a_ta": "சரத்து 371G சட்டமன்றத் தீர்மானமின்றி மரபுசார் குடும்பச் சட்டங்களை மத்திய சட்டம் மாற்றுவதிலிருந்து பாதுகாக்கிறது.",
            "why_b_en": "Article 371G is a constitutional non-obstante clause preventing automatic supersession.",
            "why_b_ta": "சரத்து 371G தானியங்கி ரத்தை தடுக்கும் அரசியலமைப்பு விதியாகும்.",
            "why_c_en": "Constitutional exemptions are territory/community-wide, not limited to Aizawl city.",
            "why_c_ta": "அரசியலமைப்பு விலக்குகள் பகுதி தழுவியவை, ஐஸ்வால் நகருக்கு மட்டும் அல்ல.",
            "why_d_en": "Financial emergency under Art 360 has no connection to personal laws.",
            "why_d_ta": "நிதி அவசரநிலைக்கும் தனிநபர் சட்டங்களுக்கும் தொடர்பில்லை.",
            "tip_en": "In February 2023, the Mizoram Legislative Assembly unanimously passed a resolution opposing any move to implement a Uniform Civil Code in the country.",
            "tip_ta": "2023 பிப்ரவரியில், நாட்டில் பொது சிவில் சட்டத்தை அமல்படுத்தும் எந்தவொரு முயற்சிக்கும் எதிராக மிசோரம் சட்டமன்றம் ஒருமனதாகத் தீர்மானம் நிறைவேற்றியது.",
            "fact_en": "The Mizo customary code covers bride price, traditional divorce (Maak), and hereditary village chieftainship succession.",
            "fact_ta": "மிசோ மரபுச் சட்டம் மணமகள் விலை, பாரம்பரிய விவாகரத்து மற்றும் பரம்பரை கிராமத் தலைமை வாரிசுரிமை ஆகியவற்றை உள்ளடக்கியது."
        },
        # 35
        {
            "subtopic": "Article 371H Governor Special Responsibility Law and Order",
            "stem_en": "What is the constitutional rationale behind conferring special responsibility for law and order on the Governor in Arunachal Pradesh under Article 371H?",
            "stem_ta": "சரத்து 371H-ன் கீழ் அருணாச்சலப் பிரதேசத்தில் சட்டம் ஒழுங்கு தொடர்பான சிறப்புப் பொறுப்பை ஆளுநருக்கு வழங்குவதன் பின்னணியில் உள்ள அரசியலமைப்பு நியாயம் என்ன?",
            "options": [
                ("The sensitive strategic geopolitical location bordering China and historical insurgency threats along international frontiers", "சீனாவை எல்லையாகக் கொண்ட முக்கிய பூகோள-அரசியல் அமைவிடம் மற்றும் சர்வதேச எல்லைகளில் நிலவிய வரலாற்று கிளர்ச்சி அச்சுறுத்தல்கள்"),
                ("The complete absence of a democratically elected Legislative Assembly in the State", "மாநிலத்தில் ஜனநாயக ரீதியாக தேர்ந்தெடுக்கப்பட்ட சட்டமன்றம் முற்றிலும் இல்லாத நிலை"),
                ("The state having no police department requiring central military governors", "மாநிலத்தில் காவல் துறையே இல்லாததால் மத்திய ராணுவ ஆளுநர்கள் தேவைப்பட்டது"),
                ("A binding mandate from the International Court of Justice", "சர்வதேச நீதிமன்றத்தின் கட்டாய உத்தரவு")
            ],
            "correct_key": "A",
            "exp_en": "Arunachal Pradesh shares a sensitive 1,129-kilometer international border with China (the McMahon Line) and had internal security concerns following statehood in 1986. Article 371H provided a constitutional transition mechanism ensuring that the Governor, as a representative of the Union, maintains overriding oversight over law and order.",
            "exp_ta": "அருணாச்சலப் பிரதேசம் சீனாவுடன் 1,129 கி.மீ உணர்திறன் வாய்ந்த சர்வதேச எல்லையைப் (மக்மஹோன் கோடு) பகிர்ந்து கொள்கிறது. 1986-ல் மாநில அந்தஸ்து பெற்றதைத் தொடர்ந்து பாதுகாப்பு சவால்கள் இருந்ததால், ஒன்றியத்தின் பிரதிநிதியாக ஆளுநர் சட்டம் ஒழுங்கில் மேலாதிக்கக் கண்காணிப்பைப் பராமரிக்க சரத்து 371H வகைசெய்தது.",
            "why_a_en": "Strategic frontier defense and internal stability were the twin drivers of Article 371H.",
            "why_a_ta": "முக்கிய எல்லைப் பாதுகாப்பு மற்றும் உள்நாட்டு நிலைத்தன்மையே சரத்து 371H-ன் முக்கிய உந்துசக்தியாகும்.",
            "why_b_en": "Arunachal has a full-fledged elected Assembly under Article 371H(b).",
            "why_b_ta": "அருணாச்சலப் பிரதேசம் தேர்ந்தெடுக்கப்பட்ட முழு சட்டமன்றத்தைக் கொண்டுள்ளது.",
            "why_c_en": "Arunachal has its own State Police service under State List Entry 2.",
            "why_c_ta": "அருணாச்சலத்திற்கு தனியான மாநிலக் காவல் துறை உள்ளது.",
            "why_d_en": "ICJ has no jurisdiction over internal Indian statehood architecture.",
            "why_d_ta": "இந்திய உள்நாட்டு விவகாரங்களில் ICJ-க்கு அதிகார வரம்பு இல்லை.",
            "tip_en": "Similar law and order special responsibility was given to the Governor of Nagaland under Article 371A(1)(b).",
            "tip_ta": "சரத்து 371A(1)(b)-ன் கீழ் நாகாலாந்து ஆளுநருக்கும் இதே போன்ற சட்டம் ஒழுங்கு சிறப்புப் பொறுப்பு வழங்கப்பட்டது.",
            "fact_en": "China continues to dispute India's sovereignty over Arunachal Pradesh, referring to it illegitimately as 'South Tibet'.",
            "fact_ta": "சீனா அருணாச்சலப் பிரதேசத்தை சட்டவிரோதமாக 'தெற்கு திபெத்' என்று கூறி இந்தியாவின் இறையாண்மையை மறுத்து வருகிறது."
        },
        # 36
        {
            "subtopic": "Article 330/332 Single Member Constituencies",
            "stem_en": "Which Act of Parliament abolished double-member constituencies and introduced single-member reserved constituencies for Scheduled Castes and Scheduled Tribes across India?",
            "stem_ta": "இரட்டை உறுப்பினர் தொகுதிகளை ஒழித்து, இந்தியா முழுவதும் SC மற்றும் ST பிரிவினருக்கு ஒற்றை உறுப்பினர் இடஒதுக்கீட்டுத் தொகுதிகளை அறிமுகப்படுத்திய நாடாளுமன்றச் சட்டம் எது?",
            "options": [
                ("Two-Member Constituencies (Abolition) Act, 1961", "இரட்டை உறுப்பினர் தொகுதிகள் (ஒழிப்பு) சட்டம், 1961"),
                ("Representation of the People Act, 1951", "மக்கள் பிரதிநிதித்துவச் சட்டம், 1951"),
                ("Delimitation Commission Act, 1952", "தொகுதி மறுவரையறை ஆணைய சட்டம், 1952"),
                ("States Reorganisation Act, 1956", "மாநிலங்கள் மறுசீரமைப்புச் சட்டம், 1956")
            ],
            "correct_key": "A",
            "exp_en": "In the first two general elections (1951-52 and 1957), SC and ST seats were provided through two-member constituencies (where one seat was general and one reserved). Parliament enacted the Two-Member Constituencies (Abolition) Act in 1961, bifurcating them into single-member general constituencies and single-member reserved constituencies.",
            "exp_ta": "முதல் இரண்டு பொதுத் தேர்தல்களில் (1951-52 மற்றும் 1957), SC/ST இடங்கள் இரட்டை உறுப்பினர் தொகுதிகள் மூலம் வழங்கப்பட்டன (ஒரு பொது இடம், ஒரு இடஒதுக்கீட்டு இடம்). நாடாளுமன்றம் 1961-ல் இரட்டை உறுப்பினர் தொகுதிகள் (ஒழிப்பு) சட்டத்தை இயற்றி, அவற்றை ஒற்றை உறுப்பினர் பொதுத் தொகுதிகள் மற்றும் ஒற்றை உறுப்பினர் இடஒதுக்கீட்டுத் தொகுதிகள் எனப் பிரித்தது.",
            "why_a_en": "Two-Member Constituencies (Abolition) Act 1961 established single-member reserved constituencies.",
            "why_a_ta": "1961 இரட்டை உறுப்பினர் தொகுதிகள் (ஒழிப்பு) சட்டம் ஒற்றை உறுப்பினர் இடஒதுக்கீட்டுத் தொகுதிகளை உருவாக்கியது.",
            "why_b_en": "RPA 1951 conducted the original elections under the double-member system.",
            "why_b_ta": "RPA 1951 இரட்டை உறுப்பினர் முறையிலேயே தேர்தல்களை நடத்தியது.",
            "why_c_en": "Delimitation Commission Act 1952 demarcated the boundaries of the original double-member seats.",
            "why_c_ta": "1952 சட்டம் எல்லைகளை மட்டுமே மறுவரையறை செய்தது.",
            "why_d_en": "States Reorganisation Act 1956 redrew state boundaries on linguistic lines.",
            "why_d_ta": "1956 சட்டம் மொழிவாரி மாநில எல்லைகளை மாற்றியமைத்தது.",
            "tip_en": "Since the 1962 General Election, all parliamentary and assembly constituencies in India are strictly single-member constituencies.",
            "tip_ta": "1962 பொதுத் தேர்தல் முதல் இந்தியாவில் உள்ள அனைத்து நாடாளுமன்ற மற்றும் சட்டமன்றத் தொகுதிகளும் ஒற்றை உறுப்பினர் தொகுதிகளாகவே உள்ளன.",
            "fact_en": "V.V. Giri's election petition in 1957 against Suri Dora arose from one of these two-member constituencies.",
            "fact_ta": "1957-ல் சூரி டோராவுக்கு எதிரான வி.வி. கிரியின் தேர்தல் வழக்கு இந்த இரட்டை உறுப்பினர் தொகுதிகளில் ஒன்றிலிருந்தே எழுந்தது."
        },
        # 37
        {
            "subtopic": "Article 335 and Merit Harmony",
            "stem_en": "In modern Indian jurisprudence, how has the relationship between 'efficiency of administration' under Article 335 and affirmative action under Article 16 been reconciled by the Supreme Court?",
            "stem_ta": "நவீன இந்திய நீதித்துறையில், சரத்து 335-ன் கீழான 'நிர்வாகத் திறன்' மற்றும் சரத்து 16-ன் கீழான இடஒதுக்கீடு ஆகியவற்றிற்கு இடையிலான தொடர்பு உச்ச நீதிமன்றத்தால் எவ்வாறு இணக்கமாக விளக்கப்பட்டுள்ளது?",
            "options": [
                ("Efficiency is not narrowly defined by test marks alone, but includes diversity and inclusive representation of all social strata in administration", "நிர்வாகத் திறன் என்பது வெறும் தேர்வு மதிப்பெண்களால் மட்டுமே குறுகியதாக வரையறுக்கப்படுவதில்லை; மாறாக நிர்வாகத்தில் அனைத்து சமூகப் பிரிவினரின் பன்முகத்தன்மை மற்றும் உள்ளடக்கிய பிரதிநிதித்துவத்தையும் கொண்டுள்ளது"),
                ("Efficiency completely extinguishes the power of the State to grant any reservation whatsoever", "நிர்வாகத் திறன் என்பது எந்தவொரு இடஒதுக்கீட்டையும் வழங்கும் அரசின் அதிகாரத்தை முற்றிலும் நீக்குகிறது"),
                ("Efficiency requires terminating reserved candidates if they fail to publish research papers annually", "ஒதுக்கீட்டுப் பிரிவு ஊழியர்கள் ஆண்டுதோறும் ஆய்வுக் கட்டுரைகளை வெளியிடாவிட்டால் அவர்களை பணிநீக்கம் செய்வதை நிர்வாகத் திறன் கோருகிறது"),
                ("Efficiency mandates that all government departments must be privatized within ten years", "அனைத்து அரசுத் துறைகளும் பத்தாண்டுகளுக்குள் தனியார்மயமாக்கப்பட வேண்டும் என்று நிர்வாகத் திறன் கட்டாயமாக்குகிறது")
            ],
            "correct_key": "A",
            "exp_en": "In B.K. Pavitra (II) (2019), Justice D.Y. Chandrachud articulated that efficiency of administration under Article 335 cannot be viewed from a narrow, meritocratic perspective based on test scores. True efficiency requires a diverse administration that mirrors the pluralistic social structure of India, bringing lived experience and empathy into governance.",
            "exp_ta": "பவித்ரா (II) வழக்கின் (2019) தீர்ப்பில் நீதிபதி டி.ஒய். சந்திரசூட், சரத்து 335-ன் கீழான நிர்வாகத் திறன் என்பது தேர்வு மதிப்பெண்களை அடிப்படையாகக் கொண்ட குறுகிய தகுதிப் பார்வையில் பார்க்கப்படக் கூடாது என்று விளக்கினார். உண்மையான நிர்வாகத் திறன் என்பது இந்தியாவின் பன்முக சமூக அமைப்பைப் பிரதிபலிக்கும் பன்முகத்தன்மை கொண்ட நிர்வாகத்தைக் கோருகிறது.",
            "why_a_en": "Substantive equality embraces diversity as a core constituent of administrative efficiency.",
            "why_a_ta": "உள்ளடக்க சமத்துவம் என்பது பன்முகத்தன்மையை நிர்வாகத் திறனின் முக்கிய அங்கமாக ஏற்றுக்கொள்கிறது.",
            "why_b_en": "Efficiency does not negate affirmative action; they are harmonized.",
            "why_b_ta": "நிர்வாகத் திறன் இடஒதுக்கீட்டை ஒழிக்காது; இரண்டும் இணைக்கப்பட்டுள்ளன.",
            "why_c_en": "Publishing research papers is irrelevant to public service efficiency mandates.",
            "why_c_ta": "ஆய்வுக் கட்டுரை வெளியீடு அரசுப் பணித் திறனுடன் தொடர்பற்றது.",
            "why_d_en": "Privatization is an economic ideology, not an Article 335 doctrine.",
            "why_d_ta": "தனியார்மயம் என்பது சரத்து 335 கோட்பாடு அல்ல.",
            "tip_en": "Amartya Sen's critique of merit: Merit is a social construct; test scores reflect accumulated social capital rather than innate capability alone.",
            "tip_ta": "அமர்த்தியா சென்னின் தகுதி பற்றிய பார்வை: தகுதி என்பது ஒரு சமூகக் கட்டமைப்பு; தேர்வு மதிப்பெண்கள் உள்ளார்ந்த திறனை மட்டுமல்லாமல் சமூக வாய்ப்புகளையும் பிரதிபலிக்கின்றன.",
            "fact_en": "This broad definition of merit was applied in Neil Aurelio Nunes (2022) to uphold OBC reservation in All-India Quota medical seats.",
            "fact_ta": "அகில இந்திய மருத்துவ ஒதுக்கீட்டில் OBC இடஒதுக்கீட்டை உறுதி செய்ய 2022 நீல் நூன்ஸ் வழக்கில் இந்த விரிவான தகுதி வரையறை பயன்படுத்தப்பட்டது."
        },
        # 38
        {
            "subtopic": "AIQ Medical Seats OBC Reservation",
            "stem_en": "In Neil Aurelio Nunes v. Union of India (2022), the Supreme Court upheld 27% reservation for OBCs in the All-India Quota (AIQ) of state medical colleges on the ground that:",
            "stem_ta": "நீல் நூன்ஸ் எதிர் இந்திய ஒன்றியம் (2022) வழக்கில், மாநில மருத்துவக் கல்லூரிகளின் அகில இந்திய ஒதுக்கீட்டில் (AIQ) OBC-களுக்கு 27% இடஒதுக்கீட்டை உச்ச நீதிமன்றம் எந்த அடிப்படையில் உறுதி செய்தது?",
            "options": [
                ("The All-India Quota is a creature of judicial orders and cannot be kept immune from the constitutional policy of reservation under Article 15(5)", "அகில இந்திய ஒதுக்கீடு என்பது நீதிமன்ற உத்தரவுகளால் உருவாக்கப்பட்ட ஒரு அமைப்பாகும்; அதை சரத்து 15(5)-ன் கீழான அரசியலமைப்பு இடஒதுக்கீட்டுக் கொள்கையிலிருந்து விலக்கி வைக்க முடியாது"),
                ("Medical colleges are explicitly exempt from all provisions of the Indian Constitution", "மருத்துவக் கல்லூரிகளுக்கு இந்திய அரசியலமைப்பின் அனைத்து விதிகளிலிருந்தும் வெளிப்படையான விலக்கு அளிக்கப்பட்டுள்ளது"),
                ("State Governments have no power to run medical institutions under the Concurrent List", "பொதுப் பட்டியலின் கீழ் மருத்துவ நிறுவனங்களை நடத்த மாநில அரசுகளுக்கு அதிகாரம் இல்லை"),
                ("The Medical Council of India had enacted an unamendable constitutional treaty", "இந்திய மருத்துவக் கவுன்சில் திருத்த முடியாத அரசியலமைப்பு ஒப்பந்தத்தை இயற்றியிருந்தது")
            ],
            "correct_key": "A",
            "exp_en": "In Neil Aurelio Nunes (2022), the Supreme Court upheld the Central Government's notification providing 27% reservation for OBCs and 10% for EWS in the All India Quota (AIQ) for undergraduate and postgraduate medical admissions. The Court held that the AIQ, conceived in Pradeep Jain (1984) to eliminate domicile requirements, cannot become an enclave free from social justice mandates.",
            "exp_ta": "நீல் நூன்ஸ் வழக்கில் (2022), மருத்துவ சேர்க்கைக்கான அகில இந்திய ஒதுக்கீட்டில் (AIQ) OBC-களுக்கு 27% மற்றும் EWS-க்கு 10% இடஒதுக்கீடு வழங்கிய மத்திய அரசின் அறிவிப்பை உச்ச நீதிமன்றம் உறுதி செய்தது. இருப்பிடக் கட்டுப்பாடுகளை நீக்க பிரதீப் ஜெயின் வழக்கில் (1984) உருவாக்கப்பட்ட AIQ, சமூக நீதிக் கொள்கைகளிலிருந்து விலக்கு பெற்றதாக இருக்க முடியாது என நீதிமன்றம் கூறியது.",
            "why_a_en": "The Court held that AIQ seats must accommodate national reservation policies under Article 15(5).",
            "why_a_ta": "AIQ இடங்கள் சரத்து 15(5)-ன் கீழான தேசிய இடஒதுக்கீட்டுக் கொள்கைகளுக்கு இடமளிக்க வேண்டும் என நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_b_en": "Medical colleges are fully subject to Part III and Part IV of the Constitution.",
            "why_b_ta": "மருத்துவக் கல்லூரிகள் அரசியலமைப்பிற்கு முழுமையாகக் கட்டுப்பட்டவை.",
            "why_c_en": "Medical education is in the Concurrent List (Entry 25), so States run extensive medical networks.",
            "why_c_ta": "மருத்துவக் கல்வி பொதுப் பட்டியலில் (பதிவு 25) உள்ளதால் மாநிலங்கள் மருத்துவக் கல்லூரிகளை நடத்துகின்றன.",
            "why_d_en": "MCI (now NMC) is a statutory regulatory body, not a treaty-maker.",
            "why_d_ta": "NMC ஒரு சட்டப்பூர்வ ஒழுங்குமுறை அமைப்பு மட்டுமே.",
            "tip_en": "AIQ consists of 15% of undergraduate MBBS seats and 50% of postgraduate MD/MS seats contributed by states to a common pool.",
            "tip_ta": "AIQ என்பது மாநிலங்கள் பொதுத் தொகுப்பிற்கு வழங்கும் 15% இளங்கலை மற்றும் 50% முதுகலை மருத்துவ இடங்களைக் கொண்டுள்ளது.",
            "fact_en": "The DMK and Tamil Nadu Government had actively spearheaded the legal battle in Madras High Court and Supreme Court that secured this 27% OBC quota in AIQ.",
            "fact_ta": "சென்னை உயர் நீதிமன்றம் மற்றும் உச்ச நீதிமன்றத்தில் சட்டப் போராட்டம் நடத்தி AIQ-ல் 27% OBC இடஒதுக்கீட்டைப் பெறுவதில் தமிழ்நாடு அரசு முக்கியப் பங்காற்றியது."
        },
        # 39
        {
            "subtopic": "Article 371D Presidential Order Revocation Mechanism",
            "stem_en": "Under Article 371D(10), the provisions of Article 371D and of any order made by the President thereunder shall have effect notwithstanding anything in:",
            "stem_ta": "சரத்து 371D(10)-ன் படி, சரத்து 371D மற்றும் அதன் கீழ் குடியரசுத் தலைவர் பிறப்பிக்கும் எந்தவொரு ஆணையின் விதிகளும் எதில் என்ன கூறப்பட்டிருந்தாலும் மேலோங்கி நிற்கும்?",
            "options": [
                ("Any other provision of this Constitution or in any other law for the time being in force", "இந்த அரசியலமைப்பின் வேறு எந்த விதியிலும் அல்லது அப்போது நடைமுறையில் உள்ள வேறு எந்தச் சட்டத்திலும்"),
                ("The United Nations Universal Declaration of Human Rights only", "ஐக்கிய நாடுகளின் உலகளாவிய மனித உரிமைகள் பிரகடனத்தில் மட்டுமே"),
                ("The preamble to the Government of India Act 1919", "1919 இந்திய அரசு சட்டத்தின் முகப்புரையில்"),
                ("The Geneva Conventions of 1949 exclusively", "1949 ஜெனீவா ஒப்பந்தங்களில் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Article 371D(10) contains a sweeping non-obstante clause: 'The provisions of this article and of any order made by the President thereunder shall have effect notwithstanding anything in any other provision of this Constitution or in any other law for the time being in force.'",
            "exp_ta": "சரத்து 371D(10) ஒரு வலுவான விதிவிலக்கு வாசகத்தைக் கொண்டுள்ளது: 'இந்த அரசியலமைப்பின் வேறு எந்த விதியிலும் அல்லது அப்போது நடைமுறையில் உள்ள வேறு எந்தச் சட்டத்திலும் என்ன கூறப்பட்டிருந்தாலும், இச்சரத்தின் மற்றும் இதன் கீழ் குடியரசுத் தலைவரால் பிறப்பிக்கப்படும் ஆணையின் விதிகள் நடைமுறையில் இருக்கும்.'",
            "why_a_en": "Article 371D(10) explicitly gives the article and presidential orders overriding effect over the entire Constitution and other laws.",
            "why_a_ta": "சரத்து 371D(10) அரசியலமைப்பின் பிற விதிகள் மற்றும் சட்டங்களை விட இவ்வாணை மேலோங்கும் என வெளிப்படையாகக் கூறுகிறது.",
            "why_b_en": "UDHR is an international declaration, not the domestic text in 371D(10).",
            "why_b_ta": "UDHR என்பது சர்வதேச பிரகடனம், இந்திய அரசியலமைப்பு வாசகம் அல்ல.",
            "why_c_en": "1919 Act was repealed by Article 395.",
            "why_c_ta": "1919 சட்டம் சரத்து 395-ஆல் ரத்து செய்யப்பட்டது.",
            "why_d_en": "Geneva Conventions govern armed conflict conduct.",
            "why_d_ta": "ஜெனீவா ஒப்பந்தங்கள் போர்க்கால நடைமுறைகளை நிர்வகிக்கின்றன.",
            "tip_en": "This non-obstante clause shielded the local area reservation in AP from challenge under Article 16(2) and Article 16(3).",
            "tip_ta": "இந்த சிறப்பு விதி சரத்து 16(2) மற்றும் 16(3)-ன் கீழ் ஆந்திராவின் உள்ளூர் இடஒதுக்கீடு சவால் செய்யப்படுவதிலிருந்து பாதுகாத்தது.",
            "fact_en": "However, as Sambamurthy (1987) held, this non-obstante clause cannot override the unamendable Basic Structure of the Constitution.",
            "fact_ta": "இருப்பினும் சாம்பமூர்த்தி தீர்ப்பின்படி, இச்சிறப்பு விதியால்கூட அரசியலமைப்பின் திருத்த முடியாத அடிப்படை அமைப்பை மீற முடியாது."
        },
        # 40
        {
            "subtopic": "E.V. Chinnaiah v. State of Andhra Pradesh 2004",
            "stem_en": "In E.V. Chinnaiah v. State of Andhra Pradesh (2004), a 5-judge bench had held that Scheduled Castes form a single homogenous class and cannot be sub-divided. On what primary textual reading of Article 341 was this based?",
            "stem_ta": "இ.வி. சின்னையா எதிர் ஆந்திரப் பிரதேச அரசு (2004) வழக்கில், 5 நீதிபதிகள் கொண்ட அமர்வு பட்டியலிடப்பட்ட சாதியினர் ஒரே மாதிரியான ஒற்றை வகுப்பினர் என்றும் அவர்களை உட்பிரிவு செய்ய முடியாது என்றும் தீர்ப்பளித்தது. சரத்து 341-ன் எந்த முதன்மை வாசக விளக்கத்தின் அடிப்படையில் இது அமைந்தது?",
            "options": [
                ("Once castes are specified in the Presidential List under Article 341(1), they form a single composite caste group that only Parliament can alter under Article 341(2), precluding State Legislatures from creating sub-quotas", "சரத்து 341(1)-ன் கீழ் குடியரசுத் தலைவர் பட்டியலில் சாதிகள் குறிப்பிடப்பட்டுவிட்டால், அவை ஓர் ஒருங்கிணைந்த சாதித் தொகுதியாக மாறுகின்றன; சரத்து 341(2)-ன் கீழ் நாடாளுமன்றம் மட்டுமே அதில் மாற்றம் செய்ய முடியும் என்பதால் மாநில சட்டமன்றங்கள் உள்-ஒதுக்கீடுகளை உருவாக்க முடியாது"),
                ("The Supreme Court held that the caste system had completely ceased to exist in Andhra Pradesh", "ஆந்திரப் பிரதேசத்தில் சாதி அமைப்பே முற்றிலும் இல்லாமல் போய்விட்டது என உச்ச நீதிமன்றம் கருதியது"),
                ("The 2004 bench ruled that the Governor is the sole judicial authority to classify castes", "ஆளுநரே சாதிகளை வகைப்படுத்தும் ஒரே நீதித்துறை அதிகாரம் என 2004 அமர்வு தீர்ப்பளித்தது"),
                ("The bench held that Article 341 violated the United Nations Charter", "சரத்து 341 ஐக்கிய நாடுகள் சாசனத்தை மீறியதாக அமர்வு கூறியது")
            ],
            "correct_key": "A",
            "exp_en": "In E.V. Chinnaiah (2004), the Supreme Court took a formalistic view that the Presidential notification under Article 341(1) creates a single 'Scheduled Caste' class for the purposes of the Constitution, and allowing states to sub-classify into groups (A, B, C, D) would tamper with the Presidential list, which only Parliament has power to alter under Article 341(2). This formalistic reasoning was rejected and overruled in Davinder Singh (2024).",
            "exp_ta": "சின்னையா வழக்கில் (2004), சரத்து 341(1)-ன் கீழான குடியரசுத் தலைவர் அறிவிக்கை ஓர் ஒற்றை 'பட்டியலிடப்பட்ட சாதி' வகுப்பை உருவாக்குகிறது என்றும், மாநிலங்கள் அதற்குள் உட்பிரிவுகளை (A, B, C, D) உருவாக்குவது குடியரசுத் தலைவர் பட்டியலில் தலையிடுவதாகும் என்றும் நீதிமன்றம் கூறியது. சரத்து 341(2)-ன் கீழ் நாடாளுமன்றத்திற்கு மட்டுமே திருத்தம் செய்ய அதிகாரம் உள்ளது என்ற இவ்வாதம் 2024 தேவிந்தர் சிங் வழக்கில் நிராகரிக்கப்பட்டு ரத்து செய்யப்பட்டது.",
            "why_a_en": "Chinnaiah was anchored on the rigid doctrine that Art 341 list cannot be grouped or tinkered with by states.",
            "why_a_ta": "சரத்து 341 பட்டியலை மாநிலங்கள் மாற்றியமைக்க முடியாது என்ற கடுமையான வாதத்திலேயே சின்னையா தீர்ப்பு அமைந்திருந்தது.",
            "why_b_en": "The Court acknowledged caste realities, but ruled strictly on legislative competence.",
            "why_b_ta": "சட்டமன்ற அதிகார வரம்பின் அடிப்படையிலேயே நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_c_en": "The Governor was not given judicial classification power.",
            "why_c_ta": "ஆளுநருக்கு நீதித்துறை வகைப்பாடு அதிகாரம் வழங்கப்படவில்லை.",
            "why_d_en": "UN Charter was not the basis of the judgment.",
            "why_d_ta": "ஐ.நா சாசனம் தீர்ப்பின் அடிப்படை அல்ல.",
            "tip_en": "Davinder Singh (2024) overruled Chinnaiah by clarifying that sub-classification for affirmative action does NOT add or subtract castes from the Art 341 list, but merely arranges preferential opportunities within the existing list.",
            "tip_ta": "உள் இடஒதுக்கீடு என்பது சரத்து 341 பட்டியலில் சாதிகளைச் சேர்க்கவோ நீக்கவோ செய்யாது; பட்டியலில் உள்ளவர்களுக்குள்ளேயே முன்னுரிமை அளிக்கிறது என விளக்கி 2024 தீர்ப்பு சின்னையாவை ரத்து செய்தது.",
            "fact_en": "Andhra Pradesh's Justice P. Ramachandra Raju Commission had originally recommended the ABCD sub-categorization of Scheduled Castes in 1997.",
            "fact_ta": "1997-ல் ஆந்திராவின் நீதிபதி ராமச்சந்திர ராஜு ஆணையமே SC சாதிகளை ABCD என உட்பிரிவு செய்ய முதலில் பரிந்துரைத்தது."
        },
        # 41
        {
            "subtopic": "Article 371B & 371C Comparative Committee Role",
            "stem_en": "How do the legislative committees established under Article 371B (Assam) and Article 371C (Manipur) functionally compare in their constitutional scope?",
            "stem_ta": "சரத்து 371B (அசாம்) மற்றும் சரத்து 371C (மணிப்பூர்) ஆகியவற்றின் கீழ் அமைக்கப்பட்ட சட்டமன்றக் குழுக்கள் தங்களின் அரசியலமைப்பு வரம்பில் எவ்வாறு செயல்பட்டு ஒப்பிடப்படுகின்றன?",
            "options": [
                ("Both are specialized committees of the respective State Legislative Assemblies composed of MLAs from designated tribal/hill areas to safeguard regional autonomy within state legislation", "இரண்டுமே மாநில சட்டமியற்றலில் பிராந்திய சுயாட்சியைப் பாதுகாப்பதற்காக நியமிக்கப்பட்ட பழங்குடி/மலைப்பகுதி எம்.எல்.ஏ-க்களைக் கொண்ட அந்தந்த மாநில சட்டமன்றங்களின் சிறப்புப் பிரத்யேகக் குழுக்களாகும்"),
                ("Both are permanent military bodies under the control of the Chief of Defence Staff", "இரண்டுமே பாதுகாப்புத் தளபதியின் கட்டுப்பாட்டில் உள்ள நிரந்தர ராணுவ அமைப்புகள்"),
                ("Article 371B applies only to municipal wards, while Article 371C applies only to tea estates", "சரத்து 371B நகராட்சி வார்டுகளுக்கு மட்டுமே பொருந்தும், சரத்து 371C தேயிலைத் தோட்டங்களுக்கு மட்டுமே பொருந்தும்"),
                ("Both committees have the constitutional power to impeach the President of India", "இரு குழுக்களுக்கும் இந்தியக் குடியரசுத் தலைவரை பதவி நீக்கம் (இம்பீச்மென்ட்) செய்யும் அரசியலமைப்பு அதிகாரம் உள்ளது")
            ],
            "correct_key": "A",
            "exp_en": "Articles 371B and 371C both embody a unique institutional innovation: embedding mini-legislative committees inside state assemblies (Assam Tribal Committee and Manipur Hill Areas Committee) to ensure that bills affecting tribal/hill territories cannot be bulldozed by the valley/plains majority.",
            "exp_ta": "சரத்துகள் 371B மற்றும் 371C இரண்டும் ஒரு தனித்துவமான நிறுவன கண்டுபிடிப்பை வெளிப்படுத்துகின்றன: சமவெளிப் பெரும்பான்மையினரால் பழங்குடி/மலைப்பகுதி சட்டங்கள் தன்னிச்சையாக இயற்றப்படுவதைத் தடுக்க, மாநில சட்டமன்றத்திற்குள்ளேயே சிறிய சட்டமன்றக் குழுக்களை (அசாம் பழங்குடிக் குழு மற்றும் மணிப்பூர் மலைப்பகுதிகள் குழு) நிறுவுவதாகும்.",
            "why_a_en": "Accurately captures the structural design of these intra-assembly territorial committees.",
            "why_a_ta": "சட்டமன்றத்திற்குள்ளான இக்குழுக்களின் கட்டமைப்பு வடிவமைப்பை துல்லியமாக விளக்குகிறது.",
            "why_b_en": "They are legislative committees, not military formations.",
            "why_b_ta": "அவை சட்டமன்றக் குழுக்கள், ராணுவப் படைகள் அல்ல.",
            "why_c_en": "Both apply to tribal regions, not municipal wards or private tea estates.",
            "why_c_ta": "இரு குழுக்களும் பழங்குடிப் பகுதிகளுக்குப் பொருந்தும்.",
            "why_d_en": "Only Parliament can impeach the President under Article 61.",
            "why_d_ta": "நாடாளுமன்றம் மட்டுமே சரத்து 61-ன் கீழ் குடியரசுத் தலைவரை பதவி நீக்கம் செய்ய முடியும்.",
            "tip_en": "Under Article 371C, the Manipur Governor must also report annually to the President, giving the Union direct supervisory oversight (Art 371C(2)).",
            "tip_ta": "சரத்து 371C-ன் கீழ் மணிப்பூர் ஆளுநர் குடியரசுத் தலைவருக்கு ஆண்டு அறிக்கை அளிக்க வேண்டும்; இது மத்திய அரசுக்கு நேரடி மேற்பார்வை அதிகாரத்தை அளிக்கிறது.",
            "fact_en": "The Manipur Hill Areas Committee consists of all 20 MLAs elected from the hill districts (out of Manipur's total 60 seats).",
            "fact_ta": "மணிப்பூரின் மொத்தமுள்ள 60 இடங்களில் மலை மாவட்டங்களிலிருந்து தேர்ந்தெடுக்கப்பட்ட அனைத்து 20 எம்.எல்.ஏ-க்களும் மலைப்பகுதிகள் குழுவில் இடம்பெற்றுள்ளனர்."
        },
        # 42
        {
            "subtopic": "Creamy Layer Rationale Indra Sawhney",
            "stem_en": "Why did the Supreme Court mandate the exclusion of the 'Creamy Layer' from Other Backward Classes in Indra Sawhney (1992)?",
            "stem_ta": "இந்திரா சாவ்னி (1992) வழக்கில், இதர பிற்படுத்தப்பட்ட வகுப்பினரிடமிருந்து 'கிரீமி லேயரை' (முன்னேறிய பிரிவினர்) விலக்குவதை உச்ச நீதிமன்றம் ஏன் கட்டாயமாக்கியது?",
            "options": [
                ("To ensure that the benefits of affirmative action reach the truly disadvantaged and socially backward members of the class, preventing forward elements from cornering all benefits", "ஆக்கப்பூர்வ நடவடிக்கையின் பலன்கள் அclass-ன் உண்மையிலேயே பின்தங்கிய மற்றும் சமூக ரீதியாக நலிவடைந்த உறுப்பினர்களை சென்றடைவதை உறுதி செய்யவும், முன்னேறிய பிரிவினர் அனைத்து பலன்களையும் கைப்பற்றுவதைத் தடுக்கவும்"),
                ("To eliminate all reservations in India within a fixed period of three years", "மூன்று ஆண்டு காலத்திற்குள் இந்தியாவில் அனைத்து இடஒதுக்கீடுகளையும் ஒழிக்க"),
                ("To force all OBC citizens to pay a special luxury surcharge to the Union Treasury", "அனைத்து OBC குடிமக்களும் மத்திய கருவூலத்திற்கு சிறப்பு ஆடம்பர கூடுதல் வரி செலுத்த கட்டாயப்படுத்த"),
                ("To ensure that only millionaires can apply for civil service examinations", "கோடீஸ்வரர்கள் மட்டுமே குடிமைப் பணித் தேர்வுகளுக்கு விண்ணப்பிக்க முடியும் என்பதை உறுதி செய்ய")
            ],
            "correct_key": "A",
            "exp_en": "In Indra Sawhney (1992), the Supreme Court ruled that connecting backwardness with social reality requires that those individuals within backward classes who have achieved high social, educational, and economic advancement (the Creamy Layer) must be filtered out, so that reservation benefits trickle down to the truly depressed layers of the backward class.",
            "exp_ta": "இந்திரா சாவ்னி வழக்கில் (1992), பிற்படுத்தப்பட்ட வகுப்பினருக்குள் உயர் சமூக, கல்வி மற்றும் பொருளாதார முன்னேற்றத்தை அடைந்தவர்களை (கிரீமி லேயர்) வடிகட்ட வேண்டும் என்றும், அப்போதுதான் இடஒதுக்கீட்டுப் பலன்கள் உண்மையிலேயே பின்தங்கிய நிலையைச் சேர்ந்த மக்களை சென்றடையும் என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "Preventing cornering of benefits by the advanced elite is the core constitutional justification of Creamy Layer exclusion.",
            "why_a_ta": "முன்னேறிய உயரடுக்கினர் பலன்களைக் கைப்பற்றுவதைத் தடுப்பதே கிரீமி லேயர் விலக்கலின் முக்கிய அரசியலமைப்பு நியாயமாகும்.",
            "why_b_en": "Creamy Layer exclusion was to refine affirmative action, not abolish it.",
            "why_b_ta": "இது இடஒதுக்கீட்டைச் சீரமைக்க கொண்டுவரப்பட்டது, ஒழிப்பதற்கு அல்ல.",
            "why_c_en": "No luxury surcharge was conceived or mandated.",
            "why_c_ta": "ஆடம்பர வரி எதுவும் விதிக்கப்படவில்லை.",
            "why_d_en": "The ruling sought the exact opposite: helping the poor rather than millionaires.",
            "why_d_ta": "ஏழைகளுக்கு உதவுவதே இத்தீர்ப்பின் நோக்கம்.",
            "tip_en": "Justice Ram Nandan Prasad Committee (1993) formulated the criteria for identifying the Creamy Layer for OBCs (such as children of constitutional post holders, Group A/B officers, and income limits).",
            "tip_ta": "நீதிபதி ராம் நந்தன் பிரசாத் குழு (1993) OBC-களுக்கான கிரீமி லேயரை அடையாளம் காண்பதற்கான அளவுகோல்களை (அரசியலமைப்புப் பதவி வகிப்போர், குரூப் A/B அதிகாரிகள், வருமான வரம்பு) வகுத்தது.",
            "fact_en": "The income threshold for OBC Creamy Layer was originally set at Rs. 1 lakh in 1993, and was progressively raised to Rs. 8 lakh in 2017.",
            "fact_ta": "OBC கிரீமி லேயர் வருமான வரம்பு 1993-ல் ரூ. 1 லட்சமாக நிர்ணயிக்கப்பட்டு, 2017-ல் ரூ. 8 லட்சமாக உயர்த்தப்பட்டது."
        },
        # 43
        {
            "subtopic": "Article 371G Customary Land Ownership",
            "stem_en": "In the context of Article 371G, what does the term 'land and its resources' encompass under traditional Mizo land tenure systems?",
            "stem_ta": "சரத்து 371G-ன் பின்னணியில், பாரம்பரிய மிசோ நில அமைப்புகளின் கீழ் 'நிலம் மற்றும் அதன் வளங்கள்' என்ற சொல் எதை உள்ளடக்கியது?",
            "options": [
                ("Communal village land ownership historically managed by Village Councils, agricultural jhum plots, and surface natural resources", "வரலாற்று ரீதியாக கிராம சபைகளால் நிர்வகிக்கப்பட்ட சமூக கிராம நில உரிமை, விவசாய ஜூம் சாகுபடி நிலங்கள் மற்றும் மேற்பரப்பு இயற்கை வளங்கள்"),
                ("Only high-rise residential apartments built in municipal corporations", "மாநகராட்சிகளில் கட்டப்பட்ட அடுக்குமாடி குடியிருப்புகள் மட்டுமே"),
                ("Land held by foreign embassies in international territories", "சர்வதேச பிரதேசங்களில் உள்ள வெளிநாட்டு தூதரகங்களின் நிலங்கள்"),
                ("Private commercial airspaces above 30,000 feet", "30,000 அடிக்கு மேற்பட்ட தனியார் வணிக வான்வெளிகள்")
            ],
            "correct_key": "A",
            "exp_en": "Traditional Mizo land tenure is community-based, where land belongs to the village community and was historically allotted by the Chief (Lal) and later by elected Village Councils for rotational jhum (shifting) cultivation. Article 371G safeguards this unique communal ownership from standard central land acquisition statutes without state consent.",
            "exp_ta": "பாரம்பரிய மிசோ நில முறை சமூகம் சார்ந்தது; இங்கு நிலம் கிராமச் சமூகத்திற்குச் சொந்தமானது. வரலாற்று ரீதியாக கிராமத் தலைவராலும் (லால்) பின்னர் தேர்ந்தெடுக்கப்பட்ட கிராம சபைகளாலும் சுழற்சி முறை ஜூம் விவசாயத்திற்காக நிலம் ஒதுக்கப்பட்டது. சரத்து 371G இந்த சமூக நில உரிமையை மாநிலத்தின் ஒப்புதலின்றி மத்திய சட்டங்கள் கையகப்படுத்துவதிலிருந்து பாதுகாக்கிறது.",
            "why_a_en": "Communal village ownership and customary jhum allocation are central to Mizo land tenure under Art 371G.",
            "why_a_ta": "சமூக கிராம நில உரிமை மற்றும் பாரம்பரிய ஜூம் ஒதுக்கீடு ஆகியவை சரத்து 371G-ன் கீழ் மிசோ நில அமைப்பின் மையமாகும்.",
            "why_b_en": "Mizoram was largely non-urban when Art 371G was enacted in 1986.",
            "why_b_ta": "1986-ல் சரத்து 371G இயற்றப்பட்டபோது மிசோரம் பெரும்பாலும் கிராமப்புறமாகவே இருந்தது.",
            "why_c_en": "Embassy lands are governed by Vienna Convention on Diplomatic Relations 1961.",
            "why_c_ta": "தூதரக நிலங்கள் வியன்னா ஒப்பந்தத்தால் நிர்வகிக்கப்படுகின்றன.",
            "why_d_en": "Airspace is governed by international air law and Union List Entry 29.",
            "why_d_ta": "வான்வெளி மத்தியப் பட்டியல் பதிவு 29-ன் கீழ் வருகிறது.",
            "tip_en": "The Mizo District (Transfer of Land) Act 1963 complements Article 371G by strictly prohibiting transfer of land from a tribal to a non-tribal without executive permission.",
            "tip_ta": "1963-ன் மிசோ மாவட்ட (நிலப் பரிமாற்ற) சட்டம், பழங்குடியினர் அல்லாதவருக்கு நிலம் மாற்றப்படுவதைத் தடுத்து சரத்து 371G-க்கு துணைபுரிகிறது.",
            "fact_en": "Under Mizo customary law, land was not traditionally treated as a marketable commercial commodity.",
            "fact_ta": "மிசோ மரபுச் சட்டத்தின் கீழ் நிலம் ஒரு வணிகப் பொருளாகக் கருதப்படவில்லை."
        },
        # 44
        {
            "subtopic": "Fifth Schedule Paragraph 6 Presidential Boundaries",
            "stem_en": "Under Paragraph 6 of the Fifth Schedule, who is empowered to declare an area to be a Scheduled Area, or alter, increase, or rescind any Scheduled Area in a State?",
            "stem_ta": "ஐந்தாவது அட்டவணையின் பத்தி 6-ன் கீழ், ஒரு பகுதியை அட்டவணைப் பகுதி என அறிவிக்கவோ, அல்லது ஒரு மாநிலத்தில் உள்ள அட்டவணைப் பகுதியை மாற்றியமைக்கவோ, அதிகரிக்கவோ, ரத்து செய்யவோ யாருக்கு அதிகாரம் உள்ளது?",
            "options": [
                ("The President of India, by order made after consultation with the Governor of the State", "மாநில ஆளுநரைக் கலந்தாலோசித்த பிறகு பிறப்பிக்கும் ஆணை மூலம் இந்தியக் குடியரசுத் தலைவர்"),
                ("The Chief Minister of the State by executive gazette notification", "நிர்வாக அரசிதழ் அறிவிப்பு மூலம் மாநில முதலமைச்சர்"),
                ("The District Collector of the respective district acting independently", "தன்னிச்சையாக செயல்படும் அந்தந்த மாவட்ட ஆட்சித்தலைவர்"),
                ("The Comptroller and Auditor General of India", "இந்தியக் கணக்காய்வாளர் மற்றும் தணிக்கைத் தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "Paragraph 6(1) and (2) of the Fifth Schedule explicitly vests the power to declare an area to be a Scheduled Area, alter boundaries, or rescind scheduled status exclusively in the President by order, after consultation with the Governor of that State.",
            "exp_ta": "ஐந்தாவது அட்டவணையின் பத்தி 6(1) மற்றும் (2), ஒரு பகுதியை அட்டவணைப் பகுதியாக அறிவிக்க, எல்லைகளை மாற்ற அல்லது அந்தஸ்தை ரத்து செய்ய மாநில ஆளுநரைக் கலந்தாலோசித்த பிறகு ஆணை பிறப்பிக்கும் அதிகாரத்தை குடியரசுத் தலைவருக்கு மட்டுமே வழங்குகிறது.",
            "why_a_en": "Paragraph 6 specifies the President after consultation with the Governor.",
            "why_a_ta": "பத்தி 6 ஆளுநரைக் கலந்தாலோசித்த பிறகு குடியரசுத் தலைவரின் அதிகாரத்தை தெளிவாகக் குறிப்பிடுகிறது.",
            "why_b_en": "Chief Minister has no constitutional power to declare Scheduled Areas.",
            "why_b_ta": "முதலமைச்சருக்கு அட்டவணைப் பகுதிகளை அறிவிக்கும் அதிகாரம் இல்லை.",
            "why_c_en": "District Collectors are administrative officers without presidential constitutional prerogative.",
            "why_c_ta": "மாவட்ட ஆட்சியர் நிர்வாக அதிகாரி மட்டுமே.",
            "why_d_en": "CAG has audit duties under Articles 148-151, not territorial scheduling powers.",
            "why_d_ta": "CAG-க்கு தணிக்கை அதிகாரம் மட்டுமே உள்ளது.",
            "tip_en": "Criteria for declaring Scheduled Areas: Preponderance of tribal population, compactness and reasonable size, viable administrative entity, and economic backwardness.",
            "tip_ta": "அட்டவணைப் பகுதிகளை அறிவிப்பதற்கான அளவுகோல்கள்: பழங்குடி மக்கள் தொகை ஆதிக்கம், பரப்பளவு, நிர்வாக சாத்தியக்கூறு மற்றும் பொருளாதாரப் பின்தங்கிய நிலை.",
            "fact_en": "Scheduled Areas in India were initially notified under the Government of India (Excluded and Partially Excluded Areas) Order 1936 prior to independence.",
            "fact_ta": "சுதந்திரத்திற்கு முன்பு 1936 ஆம் ஆண்டின் ஆணையின் கீழேயே அட்டவணைப் பகுதிகள் முதலில் அறிவிக்கப்பட்டன."
        },
        # 45
        {
            "subtopic": "Article 371D Presidential Power over Service Cadres",
            "stem_en": "In Dr. B. Sudhakar v. Union of India, the interpretation of Article 371D confirmed that presidential orders establishing local cadres in Andhra Pradesh and Telangana:",
            "stem_ta": "டாக்டர் பி. சுதாகர் எதிர் இந்திய ஒன்றியம் வழக்கில், ஆந்திரா மற்றும் தெலங்கானாவில் உள்ளூர் பணியாளர் பிரிவுகளை நிறுவும் குடியரசுத் தலைவரின் ஆணைகள் தொடர்பான சரத்து 371D-ன் விளக்கம் எதை உறுதி செய்தது?",
            "options": [
                ("Constitute an overriding constitutional code that protects local residents from open competition across the entirety of the State's territory", "மாநிலத்தின் முழு நிலப்பரப்பிலும் உள்ளூர்வாசிகளை திறந்த போட்டிகளிலிருந்து பாதுகாக்கும் ஒரு மேலாதிக்க அரசியலமைப்புச் சட்டமாக அது விளங்குகிறது"),
                ("Are completely illegal and void for violating Article 14 of the Constitution", "சரத்து 14-ஐ மீறியதால் அவை முற்றிலும் சட்டவிரோதமானவை மற்றும் செல்லாதவை"),
                ("Apply only to central paramilitary personnel stationed in Hyderabad", "ஹைதராபாத்தில் நிலைநிறுத்தப்பட்டுள்ள மத்திய துணை ராணுவப் படையினருக்கு மட்டுமே அவை பொருந்தும்"),
                ("Can be repealed at any time by a simple resolution of the Greater Hyderabad Municipal Corporation", "கிரேட்டர் ஹைதராபாத் மாநகராட்சியின் சாதாரண தீர்மானத்தின் மூலம் எப்போது வேண்டுமானாலும் ரத்து செய்யப்படலாம்")
            ],
            "correct_key": "A",
            "exp_en": "Judicial interpretation has consistently recognized that Presidential Orders under Article 371D form a self-contained constitutional code for organizing public employment and education on a regional/zonal basis in Andhra Pradesh and Telangana, shielding local selections from all-state open competition.",
            "exp_ta": "சரத்து 371D-ன் கீழான குடியரசுத் தலைவர் ஆணைகள், ஆந்திரா மற்றும் தெலங்கானாவில் அரசு வேலைவாய்ப்பு மற்றும் கல்வியை பிராந்திய/மண்டல அடிப்படையில் ஒழுங்கமைப்பதற்கான ஒரு முழுமையான அரசியலமைப்பு குறியீடாகச் செயல்படுகின்றன என்றும், உள்ளூர் தேர்வுகளை மாநில அளவிலான திறந்த போட்டியிலிருந்து பாதுகாக்கின்றன என்றும் நீதிமன்றத் தீர்ப்புகள் தொடர்ந்து உறுதிப்படுத்தியுள்ளன.",
            "why_a_en": "Art 371D creates a self-contained constitutional exception to all-state competition.",
            "why_a_ta": "சரத்து 371D மாநில அளவிலான திறந்த போட்டிக்கு ஒரு முழுமையான அரசியலமைப்பு விதிவிலக்கை உருவாக்குகிறது.",
            "why_b_en": "Article 371D was held constitutionally valid in multiple Constitution Bench rulings.",
            "why_b_ta": "சரத்து 371D அரசியலமைப்பு ரீதியாக செல்லுபடியாகும் என பல அமர்வுகளால் உறுதி செய்யப்பட்டுள்ளது.",
            "why_c_en": "It applies to state civil posts and universities, not central paramilitary forces.",
            "why_c_ta": "இது மாநில சிவில் பதவிகளுக்கும் பல்கலைக்கழகங்களுக்கும் பொருந்தும்.",
            "why_d_en": "A municipal corporation cannot alter a presidential constitutional order.",
            "why_d_ta": "ஒரு மாநகராட்சி குடியரசுத் தலைவர் ஆணையை மாற்ற முடியாது.",
            "tip_en": "Following the creation of Telangana in 2014, the President issued a new Presidential Order in 2018 (Telangana Public Employment Order) creating 7 zones and 2 multi-zones.",
            "tip_ta": "2014-ல் தெலங்கானா உருவான பிறகு, 2018-ல் குடியரசுத் தலைவர் புதிய ஆணை பிறப்பித்து 7 மண்டலங்களையும் 2 பல-மண்டலங்களையும் உருவாக்கினார்.",
            "fact_en": "In the new Telangana model, 95% of direct recruitment in local cadres is reserved for local candidates of that district/zone.",
            "fact_ta": "புதிய தெலங்கானா முறையில், உள்ளூர் பணியாளர் பிரிவுகளில் நேரடி நியமனத்தில் 95% அந்தந்த மாவட்ட/மண்டல உள்ளூர் விண்ணப்பதாரர்களுக்கு ஒதுக்கப்பட்டுள்ளது."
        },
        # 46
        {
            "subtopic": "Article 371F Independence of Pre-merger Judiciary",
            "stem_en": "Under Article 371F(i), what was the status of the High Court functioning in Sikkim prior to the merger on 26 April 1975?",
            "stem_ta": "சரத்து 371F(i)-ன் கீழ், 1975 ஏப்ரல் 26 அன்று இணைவதற்கு முன்பு சிக்கிமில் செயல்பட்டு வந்த உயர் நீதிமன்றத்தின் நிலை என்னவாக இருந்தது?",
            "options": [
                ("It became the High Court for the State of Sikkim under the Indian Constitution", "அது இந்திய அரசியலமைப்பின் கீழான சிக்கிம் மாநிலத்திற்கான உயர் நீதிமன்றமாக மாறியது"),
                ("It was abolished and its records transferred to the Patna High Court", "அது கலைக்கப்பட்டு அதன் ஆவணங்கள் பாட்னா உயர் நீதிமன்றத்திற்கு மாற்றப்பட்டன"),
                ("It was converted into a subordinate district court under the Calcutta High Court", "அது கல்கத்தா உயர் நீதிமன்றத்தின் கீழான ஒரு சார்பு மாவட்ட நீதிமன்றமாக மாற்றப்பட்டது"),
                ("It was reconstituted as a specialized military court-martial bench", "அது ஒரு சிறப்பு ராணுவ நீதிமன்ற அமர்வாக மறுசீரமைக்கப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "Article 371F(i) provides that the High Court functioning as such immediately before the appointed day in the territories comprised in Sikkim shall, on and from the appointed day, be deemed to be the High Court for the State of Sikkim.",
            "exp_ta": "சரத்து 371F(i), குறிப்பிட்ட நாளுக்கு முன்பு வரை சிக்கிம் பகுதியில் செயல்பட்டு வந்த உயர் நீதிமன்றமானது, குறிப்பிட்ட நாள் முதல் சிக்கிம் மாநிலத்திற்கான உயர் நீதிமன்றமாகக் கருதப்படும் என்று கூறுகிறது.",
            "why_a_en": "Article 371F(i) directly recognized and continued the existing Sikkim High Court as a constitutional High Court under Part VI.",
            "why_a_ta": "சரத்து 371F(i) ஏற்கனவே இருந்த சிக்கிம் உயர் நீதிமன்றத்தை அரசியலமைப்பு உயர் நீதிமன்றமாக நேரடியாகத் தொடரச் செய்தது.",
            "why_b_en": "It was never merged into Patna High Court.",
            "why_b_ta": "அது பாட்னா உயர் நீதிமன்றத்துடன் இணைக்கப்படவில்லை.",
            "why_c_en": "Sikkim has its own independent High Court at Gangtok, not under Calcutta High Court.",
            "why_c_ta": "சிக்கிமிற்கு கேங்டாக்கில் தனியான தன்னாட்சி உயர் நீதிமன்றம் உள்ளது.",
            "why_d_en": "It became a regular civilian constitutional High Court, not a court-martial.",
            "why_d_ta": "அது வழக்கமான அரசியலமைப்பு சிவில் உயர் நீதிமன்றமாக மாறியது.",
            "tip_en": "Sikkim High Court initially had only one judge (the Chief Justice) upon statehood in 1975.",
            "tip_ta": "1975-ல் மாநில அந்தஸ்து பெற்ற போது சிக்கிம் உயர் நீதிமன்றம் தலைமை நீதிபதியை மட்டுமே ஒரே நீதிபதியாகக் கொண்டிருந்தது.",
            "fact_en": "Justice Man Mohan Singh Gujral was the first Chief Justice of the High Court of Sikkim.",
            "fact_ta": "நீதிபதி மன் மோகன் சிங் குஜ்ரால் சிக்கிம் உயர் நீதிமன்றத்தின் முதல் தலைமை நீதிபதியாவார்."
        },
        # 47
        {
            "subtopic": "Article 371G Border Trade Exemption",
            "stem_en": "While Article 371G provides legislative autonomy to Mizoram regarding customary practices and land ownership, which of the following is strictly a Union prerogative that applies directly to Mizoram?",
            "stem_ta": "சரத்து 371G மரபுசார் நடைமுறைகள் மற்றும் நில உரிமை தொடர்பாக மிசோரமிற்கு சட்டமன்ற சுயாட்சியை வழங்கினாலும், பின்வருவனவற்றில் நேரடியாக மிசோரமிற்குப் பொருந்தும் ஒன்றியத்தின் பிரத்யேக அதிகாரம் எது?",
            "options": [
                ("Defense, international border security, foreign affairs, and customs tariffs", "பாதுகாப்பு, சர்வதேச எல்லைப் பாதுகாப்பு, வெளியுறவு விவகாரங்கள் மற்றும் சுங்க வரிகள்"),
                ("Appointment of the village church pastors", "கிராம தேவாலய போதகர்களை நியமித்தல்"),
                ("Regulation of Mizo traditional folk dances", "மிசோ பாரம்பரிய நாட்டுப்புற நடனங்களை ஒழுங்குபடுத்துதல்"),
                ("Registration of traditional clan genealogies", "பாரம்பரிய குல வம்சாவளிகளைப் பதிவு செய்தல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371G only restricts Acts of Parliament on four specific customary subjects: (i) religious/social practices, (ii) customary law and procedure, (iii) civil/criminal customary justice, and (iv) ownership and transfer of land. All federal sovereign functions under the Union List (defense, foreign affairs, currency, customs, border trade) apply directly and with full force across Mizoram.",
            "exp_ta": "சரத்து 371G நான்கு குறிப்பிட்ட மரபுசார் துறைகளில் மட்டுமே நாடாளுமன்றச் சட்டங்களைக் கட்டுப்படுத்துகிறது: (i) மத/சமூக நடைமுறைகள், (ii) மரபுச் சட்டம், (iii) மரபுசார் நீதி, (iv) நில உரிமை மற்றும் பரிமாற்றம். மத்தியப் பட்டியலின் கீழான இறையாண்மை அதிகாரங்கள் (பாதுகாப்பு, வெளியுறவு, நாணயம், சுங்கம்) மிசோரம் முழுவதும் முழுமையாகப் பொருந்தும்.",
            "why_a_en": "Defense, border security, foreign affairs, and customs are national subjects outside Article 371G exemptions.",
            "why_a_ta": "பாதுகாப்பு, எல்லைப் பாதுகாப்பு மற்றும் வெளியுறவு ஆகியவை சரத்து 371G விலக்குகளுக்கு அப்பாற்பட்ட மத்திய விவகாரங்கள்.",
            "why_b_en": "Pastoral appointments are private religious affairs under Article 26.",
            "why_b_ta": "தேவாலய நியமனங்கள் சரத்து 26-ன் கீழான மத விவகாரங்கள்.",
            "why_c_en": "Folk dances are cultural matters under state jurisdiction.",
            "why_c_ta": "நாட்டுப்புற நடனங்கள் கலாச்சார விவகாரங்கள்.",
            "why_d_en": "Genealogies are internal social clan traditions.",
            "why_d_ta": "வம்சாவளிகள் சமூக குல மரபுகள்.",
            "tip_en": "The distinction: Asymmetrical federalism provides autonomy over cultural and territorial identity, but maintains undivided national sovereignty.",
            "tip_ta": "வேறுபாடு: சமச்சீரற்ற கூட்டாட்சி கலாச்சார சுயாட்சியை அளிக்கிறது, ஆனால் தேசிய இறையாண்மையைப் பிரிக்காமல் பாதுகாக்கிறது.",
            "fact_en": "Assam Rifles and Border Security Force (BSF) guard the 510-kilometer Indo-Myanmar border and 318-kilometer Indo-Bangladesh border in Mizoram.",
            "fact_ta": "அசாம் ரைபிள்ஸ் மற்றும் எல்லைப் பாதுகாப்புப் படை (BSF) மிசோரமில் உள்ள சர்வதேச எல்லைகளைப் பாதுகாக்கின்றன."
        },
        # 48
        {
            "subtopic": "Article 334 Decennial Pattern",
            "stem_en": "Which of the following Constitutional Amendment Acts is correctly paired with the decennial year to which it extended the SC/ST political reservation under Article 334?",
            "stem_ta": "பின்வரும் அரசியலமைப்புத் திருத்தச் சட்டங்களில் எது சரத்து 334-ன் கீழ் SC/ST அரசியல் இடஒதுக்கீட்டை நீட்டித்த பத்தாண்டு காலக்கெடுவோடு சரியாகப் பொருத்தப்பட்டுள்ளது?",
            "options": [
                ("79th Amendment Act, 1999 — Extended up to 2010", "79வது திருத்தச் சட்டம், 1999 — 2010 வரை நீட்டித்தது"),
                ("45th Amendment Act, 1980 — Extended up to 2020", "45வது திருத்தச் சட்டம், 1980 — 2020 வரை நீட்டித்தது"),
                ("95th Amendment Act, 2009 — Extended up to 2040", "95வது திருத்தச் சட்டம், 2009 — 2040 வரை நீட்டித்தது"),
                ("8th Amendment Act, 1959 — Extended up to 1990", "8வது திருத்தச் சட்டம், 1959 — 1990 வரை நீட்டித்தது")
            ],
            "correct_key": "A",
            "exp_en": "The correct pairings are: 8th CAA 1959 (to 1970); 23rd CAA 1969 (to 1980); 45th CAA 1980 (to 1990); 62nd CAA 1989 (to 2000); 79th CAA 1999 (to 2010); 95th CAA 2009 (to 2020); and 104th CAA 2019 (to 2030). Thus, pairing the 79th Amendment with 2010 is precisely accurate.",
            "exp_ta": "சரியான வரிசை: 8வது திருத்தம் 1959 (1970 வரை); 23வது திருத்தம் 1969 (1980 வரை); 45வது திருத்தம் 1980 (1990 வரை); 62வது திருத்தம் 1989 (2000 வரை); 79வது திருத்தம் 1999 (2010 வரை); 95வது திருத்தம் 2009 (2020 வரை); 104வது திருத்தம் 2019 (2030 வரை). எனவே 79வது திருத்தம் 2010 வரை என்பது மிகத் துல்லியமானது.",
            "why_a_en": "79th CAA 1999 extended reservation up to 60 years from the commencement of the Constitution (i.e. 2010).",
            "why_a_ta": "79வது திருத்தம் 1999 அரசியலமைப்பு தொடங்கியதிலிருந்து 60 ஆண்டுகள் வரை (2010 வரை) நீட்டித்தது.",
            "why_b_en": "45th CAA 1980 extended up to 1990, not 2020.",
            "why_b_ta": "45வது திருத்தம் 1990 வரை நீட்டித்தது, 2020 வரை அல்ல.",
            "why_c_en": "95th CAA 2009 extended up to 2020, not 2040.",
            "why_c_ta": "95வது திருத்தம் 2020 வரை நீட்டித்தது, 2040 வரை அல்ல.",
            "why_d_en": "8th CAA 1959 extended up to 1970, not 1990.",
            "why_d_ta": "8வது திருத்தம் 1970 வரை நீட்டித்தது, 1990 வரை அல்ல.",
            "tip_en": "Each amendment simply replaces the words 'X years' with '(X+10) years' in Article 334.",
            "tip_ta": "ஒவ்வொரு திருத்தமும் சரத்து 334-ல் உள்ள 'X ஆண்டுகள்' என்பதை '(X+10) ஆண்டுகள்' என மாற்றியமைக்கிறது.",
            "fact_en": "The 104th Amendment 2019 replaced 'seventy years' with 'eighty years' for SC/STs, while omitting any extension for Anglo-Indians.",
            "fact_ta": "104வது திருத்தம் SC/ST-க்கு 'எழுபது ஆண்டுகள்' என்பதை 'எண்பது ஆண்டுகள்' என மாற்றியது; ஆங்கிலோ-இந்தியர்களுக்கு நீட்டிக்கவில்லை."
        },
        # 49
        {
            "subtopic": "Article 335 Proviso Construction",
            "stem_en": "Under the proviso to Article 335 added by the 82nd Amendment 2000, relaxation in qualifying marks or lowering standards of evaluation is constitutionally permissible in respect of:",
            "stem_ta": "2000-ன் 82வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்து 335-ன் வரம்புரையின் கீழ், தகுதி மதிப்பெண்களில் தளர்வு அளிப்பது அல்லது மதிப்பீட்டுத் தரங்களைக் குறைப்பது எதற்கு அரசியலமைப்பு ரீதியாக அனுமதிக்கப்படுகிறது?",
            "options": [
                ("Any examination or other selection method for reservation in matters of promotion to any class or classes of services or posts for SCs and STs", "SC மற்றும் ST பிரிவினருக்கான எந்தவொரு பணி அல்லது பதவிகளில் பதவி உயர்வில் இடஒதுக்கீடு செய்வதற்கான எந்தவொரு தேர்வு அல்லது பிற தேர்வு முறை"),
                ("Appointments to the Union Council of Ministers", "மத்திய அமைச்சரவைக்கான நியமனங்கள்"),
                ("Selection of candidates to represent India in the Olympic Games", "ஒலிம்பிக் போட்டிகளில் இந்தியாவைப் பிரதிநிதித்துவப்படுத்துவதற்கான விளையாட்டு வீரர்கள் தேர்வு"),
                ("Recruitment of commercial pilots for international airlines", "சர்வதேச விமான நிறுவனங்களுக்கான வணிக விமானிகள் தேர்வு")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 335 explicitly restricts its scope to: 'relaxation in qualifying marks in any examination or lowering the standards of evaluation, for reservation in matters of promotion to any class or classes of services or posts in connection with the affairs of the Union or of a State in favour of the members of the Scheduled Castes and the Scheduled Tribes.'",
            "exp_ta": "சரத்து 335-ன் வரம்புரை அதன் வரம்பை தெளிவாகக் குறிப்பிடுகிறது: 'ஒன்றியத்தின் அல்லது ஒரு மாநிலத்தின் விவகாரங்கள் தொடர்பான பணிகள் அல்லது பதவிகளில் SC மற்றும் ST உறுப்பினர்களுக்கு பதவி உயர்வில் இடஒதுக்கீடு செய்வதற்கான தேர்வுகளில் தகுதி மதிப்பெண்களில் தளர்வு அளிப்பது அல்லது மதிப்பீட்டுத் தரங்களைக் குறைப்பது.'",
            "why_a_en": "Article 335 proviso specifically relates to promotion reservations in Union and State public services.",
            "why_a_ta": "சரத்து 335 வரம்புரை மத்திய மற்றும் மாநில அரசுப் பணிகளில் பதவி உயர்வு இடஒதுக்கீட்டுடன் தொடர்புடையது.",
            "why_b_en": "Cabinet appointments are governed by Article 75, not Art 335.",
            "why_b_ta": "அமைச்சரவை நியமனங்கள் சரத்து 75-ன் கீழ் வருகின்றன.",
            "why_c_en": "Sports team selection is not a civil service appointment under Part XIV.",
            "why_c_ta": "விளையாட்டுத் தேர்வு சிவில் பணி நியமனம் அல்ல.",
            "why_d_en": "Airline pilots are commercial/technical, not general state services covered by Art 335 proviso.",
            "why_d_ta": "விமானிகள் தேர்வு வணிகரீதியானது, சரத்து 335 வரம்புரையின் கீழ் வராது.",
            "tip_en": "This proviso nullified the judgment in S. Vinod Kumar (1996) which had prohibited lowering qualifying marks in promotional exams.",
            "tip_ta": "பதவி உயர்வுத் தேர்வுகளில் மதிப்பெண் தளர்வைத் தடை செய்த வினோத் குமார் வழக்கின் (1996) தீர்ப்பை இந்த வரம்புரை ரத்து செய்தது.",
            "fact_en": "The 82nd Amendment restored the pre-1996 policy of the Central Government allowing relaxed qualifying benchmarks for SC/ST employees.",
            "fact_ta": "82வது திருத்தம் 1996-க்கு முந்தைய மத்திய அரசின் தளர்வு அளிக்கும் கொள்கையை மீண்டும் நிலைநிறுத்தியது."
        },
        # 50
        {
            "subtopic": "Special Provisions & Basic Structure Synthesis",
            "stem_en": "Which of the following statements synthesizes the Supreme Court's jurisprudence regarding the relationship between the Basic Structure Doctrine and Articles 371 to 371J?",
            "stem_ta": "அடிப்படை அமைப்புக் கோட்பாட்டிற்கும் சரத்துகள் 371 முதல் 371J வரைக்கும் இடையிலான தொடர்பு குறித்த உச்ச நீதிமன்றத்தின் சட்டவியலை பின்வரும் கூற்றுகளில் எது துல்லியமாக ஒருங்கிணைத்துக் கூறுகிறது?",
            "options": [
                ("Special provisions under Articles 371 to 371J are valid constitutional adaptations of asymmetrical federalism, but any clause that completely ousts judicial review or destroys the democratic rule of law (such as Article 371D(5)) is unconstitutional for violating the Basic Structure", "சரத்துகள் 371 முதல் 371J வரையிலான சிறப்பு ஏற்பாடுகள் சமச்சீரற்ற கூட்டாட்சியின் சரியான அரசியலமைப்பு மாற்றங்களாகும்; ஆனால் நீதித்துறை மறுஆய்வை முற்றிலும் நீக்கும் அல்லது ஜனநாயகச் சட்டத்தின் ஆட்சியை அழிக்கும் எந்தவொரு உட்பிரிவும் (சரத்து 371D(5) போன்றவை) அடிப்படை அமைப்பை மீறுவதால் அரசியலமைப்பிற்கு முரணானதாகும்"),
                ("Articles 371 to 371J have completely destroyed the Basic Structure and must be wiped out from the Constitution", "சரத்துகள் 371 முதல் 371J வரை அடிப்படை அமைப்பை முற்றிலும் அழித்துவிட்டன, எனவே அவை அரசியலமைப்பிலிருந்து நீக்கப்பட வேண்டும்"),
                ("The Basic Structure Doctrine applies only to fundamental rights and has zero application to federalism or state special provisions", "அடிப்படை அமைப்புக் கோட்பாடு அடிப்படை உரிமைகளுக்கு மட்டுமே பொருந்தும், கூட்டாட்சி அல்லது மாநில சிறப்பு ஏற்பாடுகளுக்கு சிறிதும் பொருந்தாது"),
                ("The Supreme Court has surrendered all judicial review powers to the Governor in all 12 special provision states", "12 சிறப்பு ஏற்பாட்டு மாநிலங்களிலும் உச்ச நீதிமன்றம் தனது அனைத்து நீதித்துறை மறுஆய்வு அதிகாரங்களையும் ஆளுநரிடம் ஒப்படைத்துவிட்டது")
            ],
            "correct_key": "A",
            "exp_en": "In landmark rulings spanning Kesavananda Bharati (1973), Sambamurthy (1987), R.C. Poudyal (1993), and Bommai (1994), the Supreme Court affirmed that federalism and judicial review are core parts of the Basic Structure. Articles 371-371J are legitimate constitutional exercises of asymmetrical federalism designed to accommodate historical diversity, but they remain subject to the overarching scrutiny of judicial review.",
            "exp_ta": "கேசவானந்த பாரதி (1973), சாம்பமூர்த்தி (1987), பௌடியால் (1993) மற்றும் பொம்மை (1994) உள்ளிட்ட வரலாற்றுத் தீர்ப்புகளில், கூட்டாட்சி மற்றும் நீதித்துறை மறுஆய்வு ஆகியவை அடிப்படை அமைப்பின் முக்கிய தூண்கள் என உச்ச நீதிமன்றம் உறுதி செய்தது. சரத்துகள் 371-371J வரலாற்றுப் பன்முகத்தன்மையை இணைக்கும் சமச்சீரற்ற கூட்டாட்சியின் சரியான வெளிப்பாடாகும்; ஆனால் அவை நீதித்துறை மறுஆய்வின் மேற்பார்வைக்கு உட்பட்டவையே.",
            "why_a_en": "Harmonizes asymmetrical federalism with the non-negotiable primacy of the Basic Structure doctrine.",
            "why_a_ta": "சமச்சீரற்ற கூட்டாட்சியை அடிப்படை அமைப்புக் கோட்பாட்டின் மாறாத மேலாதிக்கத்துடன் இணக்கமாக ஒருங்கிணைக்கிறது.",
            "why_b_en": "Special provisions enhance national unity and federalism rather than destroying the basic structure.",
            "why_b_ta": "சிறப்பு ஏற்பாடுகள் தேசிய ஒருமைப்பாட்டையும் கூட்டாட்சியையும் மேம்படுத்துகின்றன.",
            "why_c_en": "Federalism and judicial review were specifically declared basic structure features in Kesavananda, Minerva Mills, and Bommai.",
            "why_c_ta": "கூட்டாட்சியும் நீதித்துறை மறுஆய்வும் அடிப்படை அமைப்பின் அம்சங்கள் என தீர்ப்பளிக்கப்பட்டுள்ளன.",
            "why_d_en": "Judicial review is a non-derogable constitutional power that cannot be surrendered to any governor.",
            "why_d_ta": "நீதித்துறை மறுஆய்வு என்பது கைவிட முடியாத அரசியலமைப்பு அதிகாரமாகும்.",
            "tip_en": "Master formula: Special provisions + Asymmetrical Federalism + Judicial Review = Constitutional Unity in Diversity.",
            "tip_ta": "முதன்மை சூத்திரம்: சிறப்பு ஏற்பாடுகள் + சமச்சீரற்ற கூட்டாட்சி + நீதித்துறை மறுஆய்வு = வேற்றுமையில் அரசியலமைப்பு ஒருமைப்பாடு.",
            "fact_en": "Chief Justice P.B. Gajendragadkar described Indian federalism as a dynamic organism capable of adopting flexible institutional arrangements to preserve national integrity.",
            "fact_ta": "தலைமை நீதிபதி கஜேந்திரகட்கர் இந்தியக் கூட்டாட்சியை தேசிய ஒருமைப்பாட்டைப் பேண நெகிழ்வான அமைப்புகளை ஏற்றுக்கொள்ளும் ஓர் உயிர்ப்புள்ள அமைப்பாக விவரித்தார்."
        }
    ]

    questions = []
    for idx, item in enumerate(raw, start=1):
        qid = f"SPS_H_{idx:03d}"
        opts = item["options"]
        q = make_sps_q(
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
            correct_key=item["correct_key"],
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
            tags=["polity", "special_provisions_states", "hard", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_hard_file():
    qs = get_hard_questions()
    print(f"Generated {len(qs)} raw Hard questions for Special Provisions for States.")
    balanced = randomize_and_balance_dataset(qs, seed=44)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "special_provisions_states_hard.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Hard MCQs to {out_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="SPS_H_")
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
