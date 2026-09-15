# -*- coding: utf-8 -*-
"""
Official Language - Part 1 Medium MCQs Generator (50 MCQs: OL_M_001 to OL_M_050)
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

def get_medium_questions():
    raw_data = [
        # 1
        {
            "subtopic": "Article 344(3) Safeguards for Non-Hindi Areas",
            "stem_en": "Under Article 344(3), what specific consideration must the Official Language Commission have due regard to while making its recommendations?",
            "stem_ta": "சரத்து 344(3)-ன் கீழ், தனது பரிந்துரைகளைச் செய்யும்போது அதிகாரப்பூர்வ மொழி ஆணையம் பின்வரும் எதற்கு உரிய கவனம் செலுத்த வேண்டும்?",
            "options": [
                ("The just claims and interests of persons belonging to the non-Hindi speaking areas in regard to public services", "பொதுப்பணிகள் தொடர்பாக இந்தி பேசாத பகுதிகளைச் சேர்ந்த நபர்களின் நியாயமான கோரிக்கைகள் மற்றும் நலன்கள்"),
                ("The complete replacement of English within five years without exception", "எந்த விதிவிலக்கும் இன்றி ஐந்து ஆண்டுகளுக்குள் ஆங்கிலத்தை முழுமையாக மாற்றுவது"),
                ("The compulsory imposition of Hindi on all State administrations", "அனைத்து மாநில நிர்வாகங்களின் மீதும் இந்தியை கட்டாயமாக திணிப்பது"),
                ("The restriction of competitive exams to Hindi medium exclusively", "போட்டித் தேர்வுகளை இந்தி வழியில் மட்டுமே மட்டுப்படுத்துவது")
            ],
            "correct_key": "A",
            "exp_en": "Article 344(3) explicitly mandates that the Commission shall have due regard to the industrial, cultural, and scientific advancement of India, and the just claims and interests of persons belonging to non-Hindi speaking areas in regard to public services.",
            "exp_ta": "சரத்து 344(3) இந்தியாவின் தொழில், கலாச்சார மற்றும் அறிவியல் முன்னேற்றம் மற்றும் பொதுப்பணிகள் தொடர்பாக இந்தி பேசாத பகுதிகளைச் சேர்ந்த மக்களின் நியாயமான கோரிக்கைகள் மற்றும் நலன்களை ஆணையம் கருத்தில் கொள்ள வேண்டும் எனக் கட்டாயமாக்குகிறது.",
            "why_a_en": "Article 344(3) contains the explicit constitutional guarantee protecting non-Hindi public service candidates.",
            "why_a_ta": "சரத்து 344(3) இந்தி பேசாத பொதுப்பணித் தேர்வர்களைப் பாதுகாக்கும் வெளிப்படையான அரசியலமைப்பு உத்தரவாதத்தைக் கொண்டுள்ளது.",
            "why_b_en": "The Constitution did not mandate sudden complete replacement without transition.",
            "why_b_ta": "அரசியலமைப்பு இடைக்காலமின்றி திடீரென முழுமையாக மாற்றுவதை கட்டாயப்படுத்தவில்லை.",
            "why_c_en": "States decide their own official languages under Article 345.",
            "why_c_ta": "மாநிலங்கள் சரத்து 345-ன் கீழ் தங்கள் சொந்த அதிகாரப்பூர்வ மொழிகளைத் தீர்மானிக்கின்றன.",
            "why_d_en": "Exams were protected to prevent discrimination against non-Hindi candidates.",
            "why_d_ta": "இந்தி பேசாத தேர்வர்களுக்கு எதிரான பாகுபாட்டைத் தடுக்க தேர்வுகள் பாதுகாக்கப்பட்டன.",
            "tip_en": "Article 344(3) is the primary constitutional shield for non-Hindi public employment aspirants.",
            "tip_ta": "சரத்து 344(3) என்பது இந்தி பேசாத பொது வேலைவாய்ப்பு விரும்பிகளுக்கான முதன்மை அரசியலமைப்பு கவசமாகும்.",
            "fact_en": "This clause was championed by delegates from Madras, Bengal, and Mysore in the Constituent Assembly.",
            "fact_ta": "அரசியல் நிர்ணய சபையில் மெட்ராஸ், வங்கம் மற்றும் மைசூர் பிரதிநிதிகளால் இச்சரத்துப் பிரிவு கடுமையாக ஆதரிக்கப்பட்டது."
        },
        # 2
        {
            "subtopic": "Kher Commission and Pant Committee",
            "stem_en": "Which Parliamentary Committee was constituted in 1957 to examine the recommendations of the First Official Language Commission (Kher Commission)?",
            "stem_ta": "முதலாவது அதிகாரப்பூர்வ மொழி ஆணையத்தின் (கெர் ஆணையம்) பரிந்துரைகளை ஆய்வு செய்வதற்காக 1957-ல் அமைக்கப்பட்ட நாடாளுமன்றக் குழு எது?",
            "options": [
                ("Committee chaired by Gobind Ballabh Pant", "கோவிந்த் வல்லப் பந்த் தலைமையிலான குழு"),
                ("Committee chaired by B.R. Ambedkar", "பி.ஆர். அம்பேத்கர் தலைமையிலான குழு"),
                ("Committee chaired by Jawaharlal Nehru", "ஜவஹர்லால் நேரு தலைமையிலான குழு"),
                ("Committee chaired by Morarji Desai", "மொரார்ஜி தேசாய் தலைமையிலான குழு")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 344(4), a 30-member Parliamentary Committee was constituted in September 1957 under the chairmanship of Union Home Minister Gobind Ballabh Pant to examine the Kher Commission report.",
            "exp_ta": "சரத்து 344(4)-ன் கீழ், கெர் ஆணைய அறிக்கையை ஆய்வு செய்வதற்காக ஒன்றிய உள்துறை அமைச்சர் கோவிந்த் வல்லப் பந்த் தலைமையில் 1957 செப்டம்பரில் 30 உறுப்பினர்களைக் கொண்ட நாடாளுமன்றக் குழு அமைக்கப்பட்டது.",
            "why_a_en": "G.B. Pant chaired the Parliamentary Committee constituted pursuant to Article 344(4).",
            "why_a_ta": "சரத்து 344(4)-ன் படி அமைக்கப்பட்ட நாடாளுமன்றக் குழுவிற்கு ஜி.பி. பந்த் தலைமை தாங்கினார்.",
            "why_b_en": "Dr. Ambedkar had resigned from the Cabinet in 1951 and passed away in 1956.",
            "why_b_ta": "டாக்டர் அம்பேத்கர் 1951-ல் அமைச்சரவையிலிருந்து விலகி 1956-ல் காலமானார்.",
            "why_c_en": "PM Nehru was not the chairman of this specialized legislative committee.",
            "why_c_ta": "பிரதமர் நேரு இந்த பிரத்யேக சட்டமன்றக் குழுவின் தலைவர் அல்ல.",
            "why_d_en": "Morarji Desai was Union Finance Minister later, not chairman of this 1957 committee.",
            "why_d_ta": "மொரார்ஜி தேசாய் பின்னர் நிதி அமைச்சராக இருந்தார், இந்த 1957 குழுவின் தலைவர் அல்ல.",
            "tip_en": "Sequence: 1955 B.G. Kher Commission -> 1957 G.B. Pant Committee -> 1960 Presidential Order.",
            "tip_ta": "வரிசை: 1955 பி.ஜி. கெர் ஆணையம் -> 1957 ஜி.பி. பந்த் குழு -> 1960 குடியரசுத் தலைவர் ஆணை.",
            "fact_en": "The Pant Committee recommended that Hindi should become the primary official language, with English continuing as a subsidiary language.",
            "fact_ta": "பந்த் குழு இந்தியை முதன்மை அதிகாரப்பூர்வ மொழியாகவும், ஆங்கிலத்தை துணை மொழியாகவும் தொடர பரிந்துரைத்தது."
        },
        # 3
        {
            "subtopic": "Section 4 of Official Languages Act 1963",
            "stem_en": "Under Section 4 of the Official Languages Act, 1963, when was the Committee of Parliament on Official Language required to be constituted?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம், 1963-ன் பிரிவு 4-ன் கீழ், அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழு எப்போது அமைக்கப்பட வேண்டும் என விதிக்கப்பட்டது?",
            "options": [
                ("After the expiration of 10 years from the date on which Section 3 came into force (i.e. after January 26, 1975)", "பிரிவு 3 அமலுக்கு வந்த தேதியிலிருந்து 10 ஆண்டுகள் முடிந்த பிறகு (அதாவது 1975 ஜனவரி 26-க்குப் பிறகு)"),
                ("Immediately on the passing of the Act in 1963", "1963-ல் சட்டம் நிறைவேற்றப்பட்ட உடனடியாக"),
                ("After 25 years from the commencement of the Constitution", "அரசியலமைப்பு அமலுக்கு வந்ததிலிருந்து 25 ஆண்டுகளுக்குப் பிறகு"),
                ("Only when requested by three-fourths of State Assemblies", "மாநில சட்டமன்றங்களில் நான்கில் மூன்று பங்கு கோரும்போது மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Section 4(1) of the 1963 Act mandated that after the expiration of 10 years from January 26, 1965, a Committee on Official Language consisting of 30 members (20 LS, 10 RS) shall be constituted upon a resolution passed by both Houses. It was thus set up in 1976.",
            "exp_ta": "1963-ன் சட்டப் பிரிவு 4(1)-ன் படி, 1965 ஜனவரி 26 முதல் 10 ஆண்டுகள் முடிந்த பிறகு, இரு அவைகளிலும் தீர்மானம் நிறைவேற்றப்பட்டு 30 உறுப்பினர்களைக் கொண்ட (20 மக்களவை, 10 மாநிலங்களவை) அதிகாரப்பூர்வ மொழிக் குழு அமைக்கப்பட வேண்டும். அதன்படி 1976-ல் இக்குழு அமைக்கப்பட்டது.",
            "why_a_en": "Section 4 explicitly timed the creation 10 years after Section 3's commencement.",
            "why_a_ta": "பிரிவு 4 பிரிவு 3 அமலுக்கு வந்த 10 ஆண்டுகளுக்குப் பிறகு இதை வெளிப்படையாக அமைத்தது.",
            "why_b_en": "It was not constituted immediately in 1963.",
            "why_b_ta": "இது 1963-ல் உடனடியாக அமைக்கப்படவில்லை.",
            "why_c_en": "The statutory formula was 10 years from 1965, not 25 years from 1950.",
            "why_c_ta": "சட்டப்பூர்வ சூத்திரம் 1965-லிருந்து 10 ஆண்டுகள், 1950-லிருந்து 25 ஆண்டுகள் அல்ல.",
            "why_d_en": "State Assembly resolutions were not required to constitute this Parliamentary Committee.",
            "why_d_ta": "இந்த நாடாளுமன்றக் குழுவை அமைக்க மாநில சட்டமன்றத் தீர்மானங்கள் தேவையில்லை.",
            "tip_en": "Section 4 Committee: 30 members (20 LS + 10 RS), set up in 1976, reviews progressive use of Hindi.",
            "tip_ta": "பிரிவு 4 குழு: 30 உறுப்பினர்கள் (20 மக்களவை + 10 மாநிலங்களவை), 1976-ல் அமைக்கப்பட்டு, இந்தி பயன்பாட்டை ஆய்வு செய்கிறது.",
            "fact_en": "The Committee submits periodic reports to the President, who lays them before Parliament.",
            "fact_ta": "இக்குழு அவ்வப்போது குடியரசுத் தலைவரிடம் அறிக்கைகளை சமர்ப்பிக்கிறது, அவர் அவற்றை நாடாளுமன்றத்தில் வைக்கிறார்."
        },
        # 4
        {
            "subtopic": "High Court Judgments under Official Languages Act",
            "stem_en": "Under Section 7 of the Official Languages Act, 1963, judgments and decrees may be passed in Hindi or the State official language by a High Court provided that which mandatory condition is fulfilled?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம், 1963-ன் பிரிவு 7-ன் கீழ், உயர் நீதிமன்றத்தால் தீர்ப்புகள் மற்றும் கட்டளைகள் இந்தி அல்லது மாநில அதிகாரப்பூர்வ மொழியில் வழங்கப்படலாம், எனினும் எந்த கட்டாய நிபந்தனை பூர்த்தி செய்யப்பட வேண்டும்?",
            "options": [
                ("They must be accompanied by an authoritative translation in the English language published under the authority of the High Court", "அவற்றுடன் உயர் நீதிமன்றத்தின் அதிகாரத்தின் கீழ் வெளியிடப்பட்ட அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு இணைக்கப்பட வேண்டும்"),
                ("The Supreme Court must give written prior approval for every judgment", "ஒவ்வொரு தீர்ப்புக்கும் உச்ச நீதிமன்றம் எழுத்துப்பூர்வ முன் அனுமதி அளிக்க வேண்டும்"),
                ("The Governor must personally sign every judgment delivered", "வழங்கப்படும் ஒவ்வொரு தீர்ப்பிலும் ஆளுநர் தனிப்பட்ட முறையில் கையொப்பமிட வேண்டும்"),
                ("No appeal can lie to the Supreme Court against such judgments", "அத்தகைய தீர்ப்புகளுக்கு எதிராக உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்ய முடியாது")
            ],
            "correct_key": "A",
            "exp_en": "Section 7 of the 1963 Act permits the Governor, with the previous consent of the President, to authorize Hindi or a State language for judgments/decrees, but requires that they be accompanied by an authoritative translation in English.",
            "exp_ta": "1963 சட்டத்தின் பிரிவு 7, குடியரசுத் தலைவரின் முன் அனுமதியுடன் தீர்ப்புகளுக்கு இந்தி அல்லது மாநில மொழியை அனுமதிக்க ஆளுநருக்கு அதிகாரமளிக்கிறது, ஆனால் அவற்றுடன் அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு கட்டாயமாக இணைக்கப்பட வேண்டும்.",
            "why_a_en": "Section 7 mandates an authoritative English translation to preserve appellate review in the Supreme Court.",
            "why_a_ta": "உச்ச நீதிமன்றத்தில் மேல்முறையீட்டு மறுஆய்வைப் பாதுகாப்பதற்காக பிரிவு 7 அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "Case-by-case Supreme Court approval is not required.",
            "why_b_ta": "வழக்கு வாரியாக உச்ச நீதிமன்ற அனுமதி தேவையில்லை.",
            "why_c_en": "The Governor does not sign judicial judgments due to separation of powers (Article 50).",
            "why_c_ta": "அதிகாரப் பகிர்வு (சரத்து 50) காரணமாக ஆளுநர் நீதிமன்றத் தீர்ப்புகளில் கையொப்பமிடுவதில்லை.",
            "why_d_en": "Appeals to the Supreme Court remain fully available under Articles 132-136.",
            "why_d_ta": "சரத்துகள் 132-136-ன் கீழ் உச்ச நீதிமன்றத்திற்கான மேல்முறையீட்டு உரிமைகள் முழுமையாக உள்ளன.",
            "tip_en": "Section 7 bridges Article 348(2) proviso by allowing regional judgments provided an English translation exists.",
            "tip_ta": "பிரிவு 7 ஆங்கில மொழிபெயர்ப்பு இருக்கும் பட்சத்தில் வட்டார மொழித் தீர்ப்புகளை அனுமதிப்பதன் மூலம் சரத்து 348(2) விதிவிலக்கை சமன் செய்கிறது.",
            "fact_en": "Allahabad, Patna, Rajasthan, and Madhya Pradesh High Courts have utilized Section 7 for Hindi.",
            "fact_ta": "அலகாபாத், பாட்னா, ராஜஸ்தான் மற்றும் மத்தியப் பிரதேச உயர் நீதிமன்றங்கள் இந்திக்காக பிரிவு 7-ஐப் பயன்படுத்தியுள்ளன."
        },
        # 5
        {
            "subtopic": "Languages in Eighth Schedule - Linguistic Families",
            "stem_en": "Which of the following Eighth Schedule languages belongs to the Austroasiatic (Munda) linguistic family?",
            "stem_ta": "பின்வரும் எட்டாவது அட்டவணை மொழிகளில் ஆஸ்ட்ரோ-ஆசியாடிக் (முண்டா) மொழிக் குடும்பத்தைச் சேர்ந்த மொழி எது?",
            "options": [
                ("Santhali", "சந்தாலி"),
                ("Bodo", "போடோ"),
                ("Manipuri", "மணிப்பூரி"),
                ("Konkani", "கொங்கணி")
            ],
            "correct_key": "A",
            "exp_en": "Santhali (added by the 92nd CAA, 2003) is the only Eighth Schedule language belonging to the Austroasiatic (Munda sub-family) language family.",
            "exp_ta": "சந்தாலி (2003-ன் 92-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டது) எட்டாவது அட்டவணையில் ஆஸ்ட்ரோ-ஆசியாடிக் (முண்டா துணைக் குடும்பம்) மொழிக் குடும்பத்தைச் சேர்ந்த ஒரே மொழியாகும்.",
            "why_a_en": "Santhali is unique as the sole Austroasiatic language in the 8th Schedule.",
            "why_a_ta": "எட்டாவது அட்டவணையில் உள்ள ஒரே ஆஸ்ட்ரோ-ஆசியாடிக் மொழியாக சந்தாலி தனித்துவமானது.",
            "why_b_en": "Bodo belongs to the Tibeto-Burman family.",
            "why_b_ta": "போடோ திபெத்தோ-பர்மியக் குடும்பத்தைச் சேர்ந்தது.",
            "why_c_en": "Manipuri (Meitei) belongs to the Tibeto-Burman family.",
            "why_c_ta": "மணிப்பூரி (மெய்தேய்) திபெத்தோ-பர்மியக் குடும்பத்தைச் சேர்ந்தது.",
            "why_d_en": "Konkani is an Indo-Aryan language.",
            "why_d_ta": "கொங்கணி என்பது இந்தோ-ஆரிய மொழியாகும்.",
            "tip_en": "Eighth Schedule Language Families: Indo-Aryan (14), Dravidian (4: Tamil, Telugu, Kannada, Malayalam), Tibeto-Burman (2: Bodo, Manipuri), Austroasiatic (1: Santhali).",
            "tip_ta": "8-வது அட்டவணை மொழிக் குடும்பங்கள்: இந்தோ-ஆரியம் (14), திராவிடம் (4: தமிழ், தெலுங்கு, கன்னடம், மலையாளம்), திபெத்தோ-பர்மியம் (2: போடோ, மணிப்பூரி), ஆஸ்ட்ரோ-ஆசியாடிக் (1: சந்தாலி).",
            "fact_en": "Santhali is written in the Ol Chiki script, invented by Pandit Raghunath Murmu.",
            "fact_ta": "சந்தாலி பண்டிட் ரகுநாத் முர்முவால் உருவாக்கப்பட்ட 'ஒல் சிக்கி' வரிவடிவத்தில் எழுதப்படுகிறது."
        },
        # 6
        {
            "subtopic": "Tibeto-Burman Languages in Eighth Schedule",
            "stem_en": "Which two languages listed in the Eighth Schedule of the Constitution belong to the Tibeto-Burman language family?",
            "stem_ta": "அரசியலமைப்பின் எட்டாவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள மொழிகளில் திபெத்தோ-பர்மிய மொழிக் குடும்பத்தைச் சேர்ந்த இரண்டு மொழிகள் எவை?",
            "options": [
                ("Bodo and Manipuri", "போடோ மற்றும் மணிப்பூரி"),
                ("Santhali and Nepali", "சந்தாலி மற்றும் நேபாளி"),
                ("Assamese and Bengali", "அசாமி மற்றும் பெங்காலி"),
                ("Kashmiri and Dogri", "காஷ்மீரி மற்றும் டோக்ரி")
            ],
            "correct_key": "A",
            "exp_en": "Bodo (spoken in Assam) and Manipuri/Meitei (spoken in Manipur) are the two languages in the Eighth Schedule belonging to the Tibeto-Burman linguistic group.",
            "exp_ta": "போடோ (அசாமில் பேசப்படுவது) மற்றும் மணிப்பூரி/மெய்தேய் (மணிப்பூரில் பேசப்படுவது) ஆகியவை எட்டாவது அட்டவணையில் திபெத்தோ-பர்மிய மொழிக் குழுவைச் சேர்ந்த இரண்டு மொழிகளாகும்.",
            "why_a_en": "Bodo and Manipuri are classified under the Tibeto-Burman branch of Sino-Tibetan languages.",
            "why_a_ta": "போடோ மற்றும் மணிப்பூரி ஆகியவை சீன-திபெத்திய மொழிகளின் திபெத்தோ-பர்மிய கிளையின் கீழ் வகைப்படுத்தப்பட்டுள்ளன.",
            "why_b_en": "Santhali is Austroasiatic; Nepali is Indo-Aryan.",
            "why_b_ta": "சந்தாலி ஆஸ்ட்ரோ-ஆசியாடிக்; நேபாளி இந்தோ-ஆரியம்.",
            "why_c_en": "Assamese and Bengali are Eastern Indo-Aryan languages.",
            "why_c_ta": "அசாமி மற்றும் பெங்காலி ஆகியவை கிழக்கு இந்தோ-ஆரிய மொழிகளாகும்.",
            "why_d_en": "Kashmiri and Dogri belong to the Dardic/Indo-Aryan groups.",
            "why_d_ta": "காஷ்மீரி மற்றும் டோக்ரி ஆகியவை இந்தோ-ஆரியக் குழுவைச் சேர்ந்தவை.",
            "tip_en": "North-East 8th Schedule languages: Assamese (Indo-Aryan), Bodo & Manipuri (Tibeto-Burman).",
            "tip_ta": "வடகிழக்கு 8-வது அட்டவணை மொழிகள்: அசாமி (இந்தோ-ஆரியம்), போடோ & மணிப்பூரி (திபெத்தோ-பர்மியம்).",
            "fact_en": "Bodo was added in 2003 (92nd CAA); Manipuri was added in 1992 (71st CAA).",
            "fact_ta": "போடோ 2003-லும் (92-வது திருத்தம்); மணிப்பூரி 1992-லும் (71-வது திருத்தம்) சேர்க்கப்பட்டன."
        },
        # 7
        {
            "subtopic": "Classical Language Distinction Criteria",
            "stem_en": "Which of the following is an established criterion for declaring a language as a Classical Language in India?",
            "stem_ta": "இந்தியாவில் ஒரு மொழியைச் செம்மொழியாக அறிவிப்பதற்கான நிறுவப்பட்ட அளவுகோல்களில் சரியானது எது?",
            "options": [
                ("The literary tradition must be original and not borrowed from another speech community", "இலக்கிய மரபு அசலானதாக இருக்க வேண்டும் மற்றும் மற்றொரு மொழிக் குழுவிலிருந்து பெறப்பட்டதாக இருக்கக் கூடாது"),
                ("The language must be spoken by at least 100 million people", "அம்மொழி குறைந்தபட்சம் 10 கோடி மக்களால் பேசப்பட வேண்டும்"),
                ("The language must currently be the official language of at least three States", "அம்மொழி தற்போது குறைந்தபட்சம் மூன்று மாநிலங்களின் அதிகாரப்பூர்வ மொழியாக இருக்க வேண்டும்"),
                ("The script must be derived directly from Devanagari", "அதன் வரிவடிவம் நேரடியாக தேவநாகரியிலிருந்து பெறப்பட்டிருக்க வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "One of the cardinal criteria set by the Ministry of Culture is that the literary tradition must be original and not borrowed from another speech community, alongside 1500-2000 years of antiquity.",
            "exp_ta": "கலாச்சார அமைச்சகம் நிர்ணயித்துள்ள முக்கிய அளவுகோல்களில் ஒன்று, அதன் இலக்கிய மரபு அசலானதாக இருக்க வேண்டும் மற்றும் மற்றொரு மொழிக் குழுவிலிருந்து பெறப்பட்டதாக இருக்கக் கூடாது, அத்துடன் 1500-2000 ஆண்டுகள் பழமை கொண்டிருக்க வேண்டும்.",
            "why_a_en": "Originality of literary tradition is an explicit criterion distinguishing classical languages.",
            "why_a_ta": "இலக்கிய மரபின் அசல் தன்மை என்பது செம்மொழிகளை வேறுபடுத்தும் வெளிப்படையான அளவுகோலாகும்.",
            "why_b_en": "Population size is irrelevant; Sanskrit has very few native speakers but is Classical.",
            "why_b_ta": "மக்கள்தொகை பொருத்தமற்றது; சமஸ்கிருதத்திற்கு மிகக் குறைந்த பேச்சாளர்களே உள்ளனர், ஆனால் அது செம்மொழியாகும்.",
            "why_c_en": "State official language status is not a prerequisite for classical recognition.",
            "why_c_ta": "மாநில அதிகாரப்பூர்வ மொழி அந்தஸ்து செம்மொழி அங்கீகாரத்திற்கான முன்நிபந்தனை அல்ல.",
            "why_d_en": "Script origin from Devanagari is not required; Tamil has its own distinct script.",
            "why_d_ta": "தேவநாகரியிலிருந்து வரிவடிவம் பெறப்பட வேண்டிய அவசியமில்லை; தமிழுக்குத் தனித்துவமான வரிவடிவம் உள்ளது.",
            "tip_en": "Classical Language Criteria: 1. Antiquity (1500-2000 yrs), 2. Ancient valuable literature, 3. Original literary tradition, 4. Distinction from modern forms.",
            "tip_ta": "செம்மொழி அளவுகோல்கள்: 1. பழமை (1500-2000 ஆண்டுகள்), 2. பண்டைய இலக்கியம், 3. அசல் மரபு, 4. நவீன வடிவங்களிலிருந்து வேறுபாடு.",
            "fact_en": "The Expert Committee on Classical Languages operates under the Sahitya Akademi.",
            "fact_ta": "செம்மொழிகளுக்கான நிபுணர் குழு சாகித்ய அகாதமியின் கீழ் செயல்படுகிறது."
        },
        # 8
        {
            "subtopic": "Benefits of Classical Language Status",
            "stem_en": "Which of the following benefits is conferred by the Government of India upon a language being declared a Classical Language?",
            "stem_ta": "ஒரு மொழி செம்மொழியாக அறிவிக்கப்படும் போது இந்திய அரசால் வழங்கப்படும் நன்மைகளில் பின்வருவனவற்றில் எது அடங்கும்?",
            "options": [
                ("Two major annual international awards for scholars of eminence in classical languages, and setup of a Centre of Excellence", "செம்மொழி அறிஞர்களுக்கான இரண்டு பெரிய ஆண்டு சர்வதேச விருதுகள் மற்றும் சிறப்பு ஆய்வு மையம் அமைத்தல்"),
                ("Automatic designation as the official language of the Supreme Court", "தானாகவே உச்ச நீதிமன்றத்தின் அதிகாரப்பூர்வ மொழியாக நியமிக்கப்படுதல்"),
                ("Mandatory teaching of the language in all Central Government schools nationwide", "நாடு முழுவதும் உள்ள அனைத்து மத்திய அரசுப் பள்ளிகளிலும் கட்டாயக் கற்பித்தல்"),
                ("Reservation of 10% seats in Parliament for speakers of that language", "அம்மொழி பேசுபவர்களுக்கு நாடாளுமன்றத்தில் 10% இடஒதுக்கீடு")
            ],
            "correct_key": "A",
            "exp_en": "Classical Language benefits include: 1) Two major annual international awards for eminent scholars, 2) Establishment of a Centre of Excellence for studies in that language, 3) UGC funding for dedicated Professional Chairs in Central Universities.",
            "exp_ta": "செம்மொழி அந்தஸ்தின் நன்மைகளில் அடங்குபவை: 1) சிறந்த அறிஞர்களுக்கு இரண்டு சர்வதேச விருதுகள், 2) மொழிக்கான சிறப்பு ஆய்வு மையம் அமைத்தல், 3) மத்தியப் பல்கலைக்கழகங்களில் பிரத்யேகப் பேராசிரியர் பணியிடங்களை (Chairs) ஏற்படுத்த UGC நிதி.",
            "why_a_en": "These financial and academic benefits are explicitly outlined in the Ministry of Culture guidelines.",
            "why_a_ta": "இந்த நிதி மற்றும் கல்வி நன்மைகள் கலாச்சார அமைச்சக வழிகாட்டுதல்களில் வெளிப்படையாக விவரிக்கப்பட்டுள்ளன.",
            "why_b_en": "Classical status does not alter court proceedings under Article 348.",
            "why_b_ta": "செம்மொழி அந்தஸ்து சரத்து 348-ன் கீழான நீதிமன்ற நடவடிக்கைகளை மாற்றுவதில்லை.",
            "why_c_en": "It does not mandate nationwide compulsory school curriculum inclusion.",
            "why_c_ta": "இது நாடு தழுவிய கட்டாயப் பள்ளிப் பாடத்திட்ட சேர்க்கையைக் கட்டாயப்படுத்துவதில்லை.",
            "why_d_en": "Language status confers no political or parliamentary reservations.",
            "why_d_ta": "மொழி அந்தஸ்து எந்த அரசியல் அல்லது நாடாளுமன்ற இடஒதுக்கீட்டையும் வழங்காது.",
            "tip_en": "Centres of Excellence: Central Institute of Classical Tamil (CICT) in Chennai is the prime example.",
            "tip_ta": "சிறப்பு ஆய்வு மையங்கள்: சென்னையில் உள்ள செம்மொழித் தமிழாய்வு மத்திய நிறுவனம் (CICT) இதற்கு முதன்மை எடுத்துக்காட்டாகும்.",
            "fact_en": "The President of India confers the Presidential Awards for Classical Tamil annually.",
            "fact_ta": "இந்தியக் குடியரசுத் தலைவர் ஆண்டுதோறும் செம்மொழித் தமிழுக்கான குடியரசுத் தலைவர் விருதுகளை வழங்குகிறார்."
        },
        # 9
        {
            "subtopic": "Official Languages Rules 1976 - Region A States",
            "stem_en": "Under Rule 2(f) of the Official Languages Rules, 1976, which of the following States is classified under 'Region A'?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள், 1976-ன் விதி 2(f)-ன் கீழ், பின்வரும் எந்த மாநிலம் 'மண்டலம் A'-ன் கீழ் வகைப்படுத்தப்பட்டுள்ளது?",
            "options": [
                ("Rajasthan", "ராஜஸ்தான்"),
                ("Punjab", "பஞ்சாப்"),
                ("Gujarat", "குஜராத்"),
                ("Maharashtra", "மகாராஷ்டிரா")
            ],
            "correct_key": "A",
            "exp_en": "Region A includes States where Hindi is the official and predominant language: Bihar, Haryana, Himachal Pradesh, Madhya Pradesh, Chhattisgarh, Jharkhand, Rajasthan, Uttar Pradesh, Uttarakhand, and the UT of Delhi and Andaman & Nicobar Islands.",
            "exp_ta": "மண்டலம் A என்பது இந்தி அதிகாரப்பூர்வ மற்றும் முதன்மை மொழியாக உள்ள மாநிலங்களை உள்ளடக்கியது: பீகார், ஹரியானா, இமாச்சலப் பிரதேசம், மத்தியப் பிரதேசம், சத்தீஸ்கர், ஜார்க்கண்ட், ராஜஸ்தான், உத்தரப் பிரதேசம், உத்தராகண்ட், தில்லி மற்றும் அந்தமான் நிக்கோபார் தீவுகள்.",
            "why_a_en": "Rajasthan is a core Hindi-speaking State classified under Region A.",
            "why_a_ta": "ராஜஸ்தான் என்பது மண்டலம் A-ன் கீழ் வகைப்படுத்தப்பட்ட முதன்மை இந்தி பேசும் மாநிலமாகும்.",
            "why_b_en": "Punjab is categorized under Region B.",
            "why_b_ta": "பஞ்சாப் மண்டலம் B-ன் கீழ் வகைப்படுத்தப்பட்டுள்ளது.",
            "why_c_en": "Gujarat is categorized under Region B.",
            "why_c_ta": "குஜராத் மண்டலம் B-ன் கீழ் வகைப்படுத்தப்பட்டுள்ளது.",
            "why_d_en": "Maharashtra is categorized under Region B.",
            "why_d_ta": "மகாராஷ்டிரா மண்டலம் B-ன் கீழ் வகைப்படுத்தப்பட்டுள்ளது.",
            "tip_en": "Region A = Pure Hindi states; Region B = Gujarat, Maharashtra, Punjab, Chandigarh; Region C = All other states.",
            "tip_ta": "மண்டலம் A = முழு இந்தி மாநிலங்கள்; மண்டலம் B = குஜராத், மகாராஷ்டிரா, பஞ்சாப், சண்டிகர்; மண்டலம் C = மற்ற அனைத்து மாநிலங்களும்.",
            "fact_en": "Communications between Central Government and Region A must ordinarily be in Hindi.",
            "fact_ta": "மத்திய அரசிற்கும் மண்டலம் A-க்கும் இடையேயான தகவல்தொடர்புகள் பொதுவாக இந்தியில் இருக்க வேண்டும்."
        },
        # 10
        {
            "subtopic": "Official Languages Rules 1976 - Region B States",
            "stem_en": "Which of the following groups of States/UTs is classified under 'Region B' in the Official Languages Rules, 1976?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள், 1976-ல் 'மண்டலம் B'-ன் கீழ் வகைப்படுத்தப்பட்டுள்ள மாநிலங்கள்/யூனியன் பிரதேசங்களின் குழு எது?",
            "options": [
                ("Gujarat, Maharashtra, Punjab, and Chandigarh", "குஜராத், மகாராஷ்டிரா, பஞ்சாப் மற்றும் சண்டிகர்"),
                ("Tamil Nadu, Kerala, Karnataka, and Andhra Pradesh", "தமிழ்நாடு, கேரளா, கர்நாடகா மற்றும் ஆந்திரப் பிரதேசம்"),
                ("Uttar Pradesh, Madhya Pradesh, Bihar, and Rajasthan", "உத்தரப் பிரதேசம், மத்தியப் பிரதேசம், பீகார் மற்றும் ராஜஸ்தான்"),
                ("Assam, Meghalaya, Nagaland, and Mizoram", "அசாம், மேகாலயா, நாகாலாந்து மற்றும் மிசோரம்")
            ],
            "correct_key": "A",
            "exp_en": "Region B comprises States and UTs that have substantial Hindi usage alongside their state official languages: Gujarat, Maharashtra, Punjab, and the UTs of Chandigarh, Daman & Diu, and Dadra & Nagar Haveli.",
            "exp_ta": "மண்டலம் B என்பது தங்கள் மாநில மொழிகளுடன் கணிசமான இந்திப் பயன்பாட்டைக் கொண்டுள்ள மாநிலங்கள் மற்றும் ஒன்றியப் பகுதிகளை உள்ளடக்கியது: குஜராத், மகாராஷ்டிரா, பஞ்சாப் மற்றும் சண்டிகர், டாமன் & டையூ, தாத்ரா & நகர் ஹவேலி.",
            "why_a_en": "Gujarat, Maharashtra, Punjab, and Chandigarh constitute the statutory Region B.",
            "why_a_ta": "குஜராத், மகாராஷ்டிரா, பஞ்சாப் மற்றும் சண்டிகர் ஆகியவை சட்டப்பூர்வ மண்டலம் B ஆகும்.",
            "why_b_en": "Southern States belong to Region C (Tamil Nadu is exempted).",
            "why_b_ta": "தென்மாநிலங்கள் மண்டலம் C-ஐச் சேர்ந்தவை (தமிழ்நாட்டிற்கு விலக்கு அளிக்கப்பட்டுள்ளது).",
            "why_c_en": "These are Region A states.",
            "why_c_ta": "இவை மண்டலம் A மாநிலங்கள்.",
            "why_d_en": "North-Eastern states belong to Region C.",
            "why_d_ta": "வடகிழக்கு மாநிலங்கள் மண்டலம் C-ஐச் சேர்ந்தவை.",
            "tip_en": "Communications to Region B are ordinarily in Hindi, but can be in English if accompanied by Hindi translation.",
            "tip_ta": "மண்டலம் B-க்கான தகவல்தொடர்புகள் பொதுவாக இந்தியில் இருக்கும், ஆனால் இந்தி மொழிபெயர்ப்புடன் ஆங்கிலத்திலும் இருக்கலாம்.",
            "fact_en": "Region B acts as a bilingual buffer between Region A and Region C.",
            "fact_ta": "மண்டலம் B மண்டலம் A மற்றும் மண்டலம் C-க்கு இடையே ஒரு இருமொழி இடையகமாகச் செயல்படுகிறது."
        },
        # 11
        {
            "subtopic": "Official Languages Rules 1976 - Region C Communications",
            "stem_en": "Under Rule 3(3) of the Official Languages Rules, 1976, communications from a Central Government office to State Governments or offices in 'Region C' shall be in which language?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள், 1976-ன் விதி 3(3)-ன் கீழ், மத்திய அரசு அலுவலகத்திலிருந்து 'மண்டலம் C'-ல் உள்ள மாநில அரசுகள் அல்லது அலுவலகங்களுக்கு அனுப்பப்படும் தகவல்தொடர்புகள் எந்த மொழியில் இருக்க வேண்டும்?",
            "options": [
                ("In the English language", "ஆங்கில மொழியில்"),
                ("In Hindi language exclusively", "இந்தி மொழியில் மட்டுமே"),
                ("In the regional language of each recipient State", "ஒவ்வொரு பெறும் மாநிலத்தின் வட்டார மொழியில்"),
                ("In Sanskrit with Hindi translation", "இந்தி மொழிபெயர்ப்புடன் கூடிய சமஸ்கிருதத்தில்")
            ],
            "correct_key": "A",
            "exp_en": "Rule 3(3) provides that communications from a Central Government office to a State Government in Region C or to any office therein shall be in English, unless Hindi is specifically agreed upon.",
            "exp_ta": "விதி 3(3)-ன் படி, மத்திய அரசு அலுவலகத்திலிருந்து மண்டலம் C-ல் உள்ள ஒரு மாநில அரசுக்கு அல்லது அங்குள்ள எந்தவொரு அலுவலகத்திற்கும் அனுப்பப்படும் தகவல்தொடர்புகள் ஆங்கிலத்திலேயே இருக்க வேண்டும்.",
            "why_a_en": "English is the statutory communication medium mandated for Region C.",
            "why_a_ta": "மண்டலம் C-க்கு கட்டாயமாக்கப்பட்ட சட்டப்பூர்வ தொடர்பு ஊடகம் ஆங்கிலம் ஆகும்.",
            "why_b_en": "Hindi cannot be imposed on Region C without agreement.",
            "why_b_ta": "ஒப்பந்தமின்றி மண்டலம் C மீது இந்தியைத் திணிக்க முடியாது.",
            "why_c_en": "Central offices are not equipped to correspond in all 22 regional languages directly.",
            "why_c_ta": "அனைத்து 22 வட்டார மொழிகளிலும் நேரடியாகத் தொடர்புகொள்ளும் வசதி மத்திய அலுவலகங்களில் இல்லை.",
            "why_d_en": "Sanskrit is not an administrative correspondence language.",
            "why_d_ta": "சமஸ்கிருதம் நிர்வாகத் தொடர்பு மொழி அல்ல.",
            "tip_en": "Region C = Southern and Eastern/NE non-Hindi States -> English is mandatory.",
            "tip_ta": "மண்டலம் C = தெற்கு மற்றும் கிழக்கு/வடகிழக்கு இந்தி பேசாத மாநிலங்கள் -> ஆங்கிலம் கட்டாயமாகும்.",
            "fact_en": "If a letter is sent in Hindi to Region C, an English translation must accompany it.",
            "fact_ta": "மண்டலம் C-க்கு இந்தியில் கடிதம் அனுப்பப்பட்டால், அதனுடன் ஆங்கில மொழிபெயர்ப்பும் இணைக்கப்பட வேண்டும்."
        },
        # 12
        {
            "subtopic": "Language of Union Public Service Exams",
            "stem_en": "Following the Official Language Resolution of 1968, in which languages are candidates permitted to write the Civil Services (Main) Examination conducted by the UPSC?",
            "stem_ta": "1968-ன் அதிகாரப்பூர்வ மொழித் தீர்மானத்தைத் தொடர்ந்து, UPSC நடத்தும் குடிமைப்பணிகள் (முதன்மைத்) தேர்வை எழுத தேர்வர்கள் எந்த மொழிகளில் அனுமதிக்கப்படுகிறார்கள்?",
            "options": [
                ("English, Hindi, or any of the languages included in the Eighth Schedule", "ஆங்கிலம், இந்தி அல்லது எட்டாவது அட்டவணையில் உள்ள ஏதேனும் ஒரு மொழி"),
                ("In English exclusively", "ஆங்கிலத்தில் மட்டுமே"),
                ("In Hindi exclusively", "இந்தியில் மட்டுமே"),
                ("Only in the official languages of the Union and classical languages", "ஒன்றியத்தின் அதிகாரப்பூர்வ மொழிகள் மற்றும் செம்மொழிகளில் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "In accordance with the 1968 Parliamentary Resolution and Kothari Committee recommendations (1976), candidates can write non-language papers in English, Hindi, or any of the 22 languages specified in the Eighth Schedule.",
            "exp_ta": "1968-ன் நாடாளுமன்றத் தீர்மானம் மற்றும் கோத்தாரி குழுவின் பரிந்துரைகளின்படி (1976), தேர்வர்கள் மொழி அல்லாத தாள்களை ஆங்கிலம், இந்தி அல்லது எட்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள 22 மொழிகளில் ஏதேனும் ஒன்றில் எழுதலாம்.",
            "why_a_en": "Candidates have the full freedom to write in English, Hindi, or any Eighth Schedule language.",
            "why_a_ta": "தேர்வர்கள் ஆங்கிலம், இந்தி அல்லது ஏதேனும் ஓர் எட்டாவது அட்டவணை மொழியில் எழுத முழு சுதந்திரம் பெற்றுள்ளனர்.",
            "why_b_en": "Prior to 1969, it was English only; since 1979 Kothari reform, all scheduled languages are allowed.",
            "why_b_ta": "1969-க்கு முன் ஆங்கிலம் மட்டுமே இருந்தது; 1979 கோத்தாரி சீர்திருத்தத்திற்குப் பிறகு அனைத்து அட்டவணை மொழிகளும் அனுமதிக்கப்படுகின்றன.",
            "why_c_en": "UPSC has never restricted the Main examination solely to Hindi.",
            "why_c_ta": "UPSC முதன்மைத் தேர்வை ஒருபோதும் இந்திக்கு மட்டுமே மட்டுப்படுத்தியதில்லை.",
            "why_d_en": "Classical status is separate from Eighth Schedule eligibility.",
            "why_d_ta": "செம்மொழி அந்தஸ்து என்பது எட்டாவது அட்டவணைத் தகுதியிலிருந்து வேறுபட்டது.",
            "tip_en": "UPSC Mains: All 22 Eighth Schedule languages + English are allowed as medium of examination.",
            "tip_ta": "UPSC முதன்மைத் தேர்வு: 22 எட்டாவது அட்டவணை மொழிகள் + ஆங்கிலம் தேர்வு ஊடகமாக அனுமதிக்கப்படுகின்றன.",
            "fact_en": "Candidates can also choose any Eighth Schedule language as an optional literature subject.",
            "fact_ta": "தேர்வர்கள் எந்தவொரு எட்டாவது அட்டவணை மொழியையும் விருப்பப் பாட இலக்கியமாகவும் தேர்ந்தெடுக்கலாம்."
        },
        # 13
        {
            "subtopic": "States Reorganisation Commission on Language",
            "stem_en": "Which Commission recommended the insertion of constitutional safeguards for linguistic minorities, leading to Articles 350A and 350B?",
            "stem_ta": "சரத்துகள் 350A மற்றும் 350B சேர்க்கப்படுவதற்கு வழிவகுத்த, மொழிச் சிறுபான்மையினருக்கான அரசியலமைப்புப் பாதுகாப்புகளைப் பரிந்துரைத்த ஆணையம் எது?",
            "options": [
                ("States Reorganisation Commission (Fazl Ali Commission)", "மாநில மறுசீரமைப்பு ஆணையம் (பசல் அலி ஆணையம்)"),
                ("Sarkaria Commission", "சர்க்காரியா ஆணையம்"),
                ("First Administrative Reforms Commission", "முதலாவது நிர்வாகச் சீர்திருத்த ஆணையம்"),
                ("Punchhi Commission", "பூஞ்சி ஆணையம்")
            ],
            "correct_key": "A",
            "exp_en": "The States Reorganisation Commission (headed by Justice Fazl Ali, with H.N. Kunzru and K.M. Panikkar) recommended institutional safeguards for linguistic minorities in newly reorganized linguistic states, resulting in the 7th CAA, 1956.",
            "exp_ta": "மாநில மறுசீரமைப்பு ஆணையம் (நீதிபதி பசல் அலி தலைமையில், எச்.என். குன்ஸ்ரு மற்றும் கே.எம். பணிக்கர் ஆகியோருடன்) புதிய மொழிவாரி மாநிலங்களில் மொழிச் சிறுபான்மையினருக்கான நிறுவனப் பாதுகாப்புகளைப் பரிந்துரைத்தது, இதன் விளைவாக 1956-ன் 7-வது அரசியலமைப்புத் திருத்தம் இயற்றப்பட்டது.",
            "why_a_en": "The Fazl Ali Commission directly authored the recommendations for Articles 350A and 350B.",
            "why_a_ta": "பசல் அலி ஆணையம் நேரடியாக சரத்துகள் 350A மற்றும் 350B-க்கான பரிந்துரைகளை வழங்கியது.",
            "why_b_en": "Sarkaria Commission (1983-1988) examined Centre-State relations decades later.",
            "why_b_ta": "சர்க்காரியா ஆணையம் (1983-1988) பல தசாப்தங்களுக்குப் பிறகு மத்திய-மாநில உறவுகளை ஆய்வு செய்தது.",
            "why_c_en": "First ARC (1966) dealt with public administration machinery.",
            "why_c_ta": "முதல் ARC (1966) பொது நிர்வாகக் கட்டமைப்பைக் கையாண்டது.",
            "why_d_en": "Punchhi Commission (2007-2010) was on Centre-State relations.",
            "why_d_ta": "பூஞ்சி ஆணையம் (2007-2010) மத்திய-மாநில உறவுகள் தொடர்பானது.",
            "tip_en": "SRC 1955 -> 7th CAA 1956 -> Articles 350A & 350B inserted.",
            "tip_ta": "SRC 1955 -> 7-வது திருத்தம் 1956 -> சரத்துகள் 350A & 350B சேர்க்கப்பட்டன.",
            "fact_en": "SRC emphasized that linguistic reorganizations must not create second-class citizenship for minorities.",
            "fact_ta": "மொழிவாரி மறுசீரமைப்பு சிறுபான்மையினருக்கு இரண்டாம் தரக் குடியுரிமையை உருவாக்கிவிடக் கூடாது என SRC வலியுறுத்தியது."
        },
        # 14
        {
            "subtopic": "Primary Education in Mother Tongue Norm",
            "stem_en": "Under Article 350A, what obligation is placed upon every State and local authority?",
            "stem_ta": "சரத்து 350A-ன் கீழ், ஒவ்வொரு மாநிலம் மற்றும் உள்ளாட்சி அதிகார அமைப்பின் மீது சுமத்தப்பட்டுள்ள கடமை என்ன?",
            "options": [
                ("To provide adequate facilities for instruction in the mother tongue at the primary stage of education to children belonging to linguistic minority groups", "மொழிச் சிறுபான்மைப் பிரிவு குழந்தைகளுக்குத் தொடக்கக் கல்வி நிலையில் தாய்மொழியில் கற்பிப்பதற்கான போதுமான வசதிகளை வழங்குதல்"),
                ("To make Hindi the compulsory medium of instruction in all primary schools", "அனைத்து தொடக்கப் பள்ளிகளிலும் இந்தியை கட்டாயப் பயிற்று மொழியாக்குதல்"),
                ("To abolish all minority language schools within ten years", "பத்து ஆண்டுகளுக்குள் அனைத்து சிறுபான்மை மொழிப் பள்ளிகளையும் மூடுதல்"),
                ("To ensure that only English is used at the secondary stage", "இடைநிலைக் கல்வி நிலையில் ஆங்கிலம் மட்டுமே பயன்படுத்தப்படுவதை உறுதி செய்தல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 350A mandates that it shall be the endeavor of every State and of every local authority within the State to provide adequate facilities for instruction in the mother tongue at the primary stage of education to children belonging to linguistic minority groups.",
            "exp_ta": "சரத்து 350A-ன் படி, மொழிச் சிறுபான்மைப் பிரிவைச் சேர்ந்த குழந்தைகளுக்குத் தொடக்கக் கல்வி நிலையில் தாய்மொழியில் கற்பிப்பதற்கான போதுமான வசதிகளைச் செய்து தருவது ஒவ்வொரு மாநிலத்தின் மற்றும் உள்ளாட்சி அமைப்பின் முயற்சியாக இருக்க வேண்டும்.",
            "why_a_en": "Article 350A uses the phrase 'adequate facilities for instruction in the mother tongue at the primary stage'.",
            "why_a_ta": "சரத்து 350A 'தொடக்கக் கல்வி நிலையில் தாய்மொழியில் கற்பிப்பதற்கான போதுமான வசதிகள்' என்ற தொடரைப் பயன்படுத்துகிறது.",
            "why_b_en": "Hindi is not prescribed as a compulsory primary medium in Article 350A.",
            "why_b_ta": "சரத்து 350A-ல் இந்தி கட்டாயத் தொடக்கக் கல்வி ஊடகமாகப் பரிந்துரைக்கப்படவில்லை.",
            "why_c_en": "Article 30 guarantees the right to establish and administer minority educational institutions.",
            "why_c_ta": "சரத்து 30 சிறுபான்மையினர் கல்வி நிறுவனங்களை நிறுவி நிர்வகிக்கும் உரிமையை உத்தரவாதம் செய்கிறது.",
            "why_d_en": "Article 350A specifically targets primary stage education, not secondary English.",
            "why_d_ta": "சரத்து 350A குறிப்பாக தொடக்கக் கல்வியை இலக்காகக் கொண்டது, இடைநிலை ஆங்கிலத்தை அல்ல.",
            "tip_en": "Target group of Article 350A: Linguistic minority children at PRIMARY stage.",
            "tip_ta": "சரத்து 350A-ன் இலக்குக் குழு: தொடக்கக் கல்வி நிலையில் உள்ள மொழிச் சிறுபான்மைக் குழந்தைகள்.",
            "fact_en": "The Supreme Court has clarified that Article 350A is an enabling provision, but parents retain school medium choice.",
            "fact_ta": "சரத்து 350A என்பது ஒரு வசதியளிக்கும் விதி, ஆனால் பெற்றோரே பள்ளியின் பயிற்றுமொழித் தேர்வைத் தீர்மானிக்கிறார்கள் என உச்ச நீதிமன்றம் தெளிவுபடுத்தியுள்ளது."
        },
        # 15
        {
            "subtopic": "Official Language Resolution 1968 Three-Language Formula",
            "stem_en": "Under the Three-Language Formula articulated in the Official Language Resolution of 1968, what languages are to be studied in non-Hindi speaking States?",
            "stem_ta": "1968-ன் அதிகாரப்பூர்வ மொழித் தீர்மானத்தில் விவரிக்கப்பட்டுள்ள மும்மொழிக் கொள்கையின் கீழ், இந்தி பேசாத மாநிலங்களில் எந்த மொழிகள் பயிலப்பட வேண்டும்?",
            "options": [
                ("The regional language, English, and Hindi", "வட்டார மொழி, ஆங்கிலம் மற்றும் இந்தி"),
                ("Hindi, English, and Sanskrit exclusively", "இந்தி, ஆங்கிலம் மற்றும் சமஸ்கிருதம் மட்டுமே"),
                ("English and two foreign languages", "ஆங்கிலம் மற்றும் இரண்டு வெளிநாட்டு மொழிகள்"),
                ("Only the regional language and classical language", "வட்டார மொழி மற்றும் செம்மொழி மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "In non-Hindi speaking States, the 1968 formula prescribed: 1) Regional language/mother tongue, 2) English, and 3) Hindi. In Hindi-speaking States: 1) Hindi, 2) English, and 3) a modern Indian language (preferably a South Indian language).",
            "exp_ta": "இந்தி பேசாத மாநிலங்களில் 1968 கொள்கை பரிந்துரைத்தது: 1) வட்டார மொழி/தாய்மொழி, 2) ஆங்கிலம், மற்றும் 3) இந்தி. இந்தி பேசும் மாநிலங்களில்: 1) இந்தி, 2) ஆங்கிலம், மற்றும் 3) ஒரு நவீன இந்திய மொழி (முன்னுரிமையாக ஒரு தென்னிந்திய மொழி).",
            "why_a_en": "Regional language + English + Hindi was the formula for non-Hindi States.",
            "why_a_ta": "வட்டார மொழி + ஆங்கிலம் + இந்தி என்பது இந்தி பேசாத மாநிலங்களுக்கான சூத்திரமாகும்.",
            "why_b_en": "Sanskrit was often substituted in Hindi states, but was not the intended formula.",
            "why_b_ta": "இந்தி மாநிலங்களில் சமஸ்கிருதம் மாற்றாக வைக்கப்பட்டது, ஆனால் அது கொள்கையின் அசல் நோக்கம் அல்ல.",
            "why_c_en": "Foreign languages other than English were not part of the primary three-language formula.",
            "why_c_ta": "ஆங்கிலம் தவிர பிற வெளிநாட்டு மொழிகள் முதன்மை மும்மொழிக் கொள்கையின் பகுதியாக இல்லை.",
            "why_d_en": "The formula aimed at trilingualism incorporating Hindi and English.",
            "why_d_ta": "இக்கொள்கை இந்தி மற்றும் ஆங்கிலத்தை உள்ளடக்கிய மும்மொழித் திறனை நோக்கமாகக் கொண்டது.",
            "tip_en": "Hindi States: Hindi + English + South Indian language; Non-Hindi States: Regional + English + Hindi.",
            "tip_ta": "இந்தி மாநிலங்கள்: இந்தி + ஆங்கிலம் + தென்னிந்திய மொழி; இந்தி பேசாத மாநிலங்கள்: வட்டார மொழி + ஆங்கிலம் + இந்தி.",
            "fact_en": "Tamil Nadu rejected this in 1968 because Hindi States failed to implement South Indian languages.",
            "fact_ta": "இந்தி பேசும் மாநிலங்கள் தென்னிந்திய மொழிகளைப் பயிற்றுவிக்கத் தவறியதால் தமிழ்நாடு 1968-ல் இதை நிராகரித்தது."
        },
        # 16
        {
            "subtopic": "States with English as Official Language",
            "stem_en": "Which of the following North-Eastern States of India has English as its sole official language under Article 345?",
            "stem_ta": "சரத்து 345-ன் கீழ் ஆங்கிலத்தைத் தனது ஒரே அதிகாரப்பூர்வ மொழியாகக் கொண்டுள்ள வடகிழக்கு மாநிலம் எது?",
            "options": [
                ("Nagaland", "நாகாலாந்து"),
                ("Assam", "அசாம்"),
                ("Tripura", "திரிபுரா"),
                ("Manipur", "மணிப்பூர்")
            ],
            "correct_key": "A",
            "exp_en": "Nagaland adopted English as its sole official language in 1967. Meghalaya and Mizoram also use English as their primary official language for state administration.",
            "exp_ta": "நாகாலாந்து 1967-ல் ஆங்கிலத்தைத் தனது ஒரே அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொண்டது. மேகாலயா மற்றும் மிசோரமும் தங்கள் மாநில நிர்வாகத்திற்கு ஆங்கிலத்தையே முதன்மை மொழியாகப் பயன்படுத்துகின்றன.",
            "why_a_en": "Nagaland famously uses English as its sole official language despite English not being in the 8th Schedule.",
            "why_a_ta": "ஆங்கிலம் 8-வது அட்டவணையில் இல்லாத போதிலும் நாகாலாந்து அதைத் தனது ஒரே அதிகாரப்பூர்வ மொழியாகப் பயன்படுத்துகிறது.",
            "why_b_en": "Assam has Assamese as official language (and Bengali in Barak Valley).",
            "why_b_ta": "அசாமில் அசாமி அதிகாரப்பூர்வ மொழியாக உள்ளது (மற்றும் பராக் பள்ளத்தாக்கில் பெங்காலி).",
            "why_c_en": "Tripura uses Bengali and Kokborok.",
            "why_c_ta": "திரிபுரா பெங்காலி மற்றும் கோக்பொரோக் மொழிகளைப் பயன்படுத்துகிறது.",
            "why_d_en": "Manipur uses Manipuri (Meitei).",
            "why_d_ta": "மணிப்பூர் மணிப்பூரி (மெய்தேய்) மொழியைப் பயன்படுத்துகிறது.",
            "tip_en": "States with English as official language: Nagaland, Meghalaya, Arunachal Pradesh.",
            "tip_ta": "ஆங்கிலத்தை அதிகாரப்பூர்வ மொழியாகக் கொண்ட மாநிலங்கள்: நாகாலாந்து, மேகாலயா, அருணாச்சலப் பிரதேசம்.",
            "fact_en": "Article 345 does NOT require a State to adopt only Eighth Schedule languages.",
            "fact_ta": "சரத்து 345 ஒரு மாநிலம் எட்டாவது அட்டவணை மொழிகளை மட்டுமே ஏற்க வேண்டும் எனக் கட்டாயப்படுத்தவில்லை."
        },
        # 17
        {
            "subtopic": "Languages of Jammu and Kashmir",
            "stem_en": "Under the Jammu and Kashmir Official Languages Act, 2020, how many official languages does the Union Territory of Jammu and Kashmir have?",
            "stem_ta": "ஜம்மு மற்றும் காஷ்மீர் அதிகாரப்பூர்வ மொழிகள் சட்டம், 2020-ன் கீழ், ஜம்மு-காஷ்மீர் ஒன்றியப் பகுதி எத்தனை அதிகாரப்பூர்வ மொழிகளைக் கொண்டுள்ளது?",
            "options": [
                ("Five languages (Kashmiri, Dogri, Urdu, Hindi, English)", "ஐந்து மொழிகள் (காஷ்மீரி, டோக்ரி, உருது, இந்தி, ஆங்கிலம்)"),
                ("Only Urdu", "உருது மட்டுமே"),
                ("Two languages (Urdu and English)", "இரண்டு மொழிகள் (உருது மற்றும் ஆங்கிலம்)"),
                ("Three languages (Kashmiri, Urdu, English)", "மூன்று மொழிகள் (காஷ்மீரி, உருது, ஆங்கிலம்)")
            ],
            "correct_key": "A",
            "exp_en": "The Jammu and Kashmir Official Languages Act, 2020 established five official languages: Kashmiri, Dogri, Urdu, Hindi, and English (prior to 2020, Urdu was the sole official language).",
            "exp_ta": "ஜம்மு மற்றும் காஷ்மீர் அதிகாரப்பூர்வ மொழிகள் சட்டம், 2020 ஐந்து அதிகாரப்பூர்வ மொழிகளை நிறுவியது: காஷ்மீரி, டோக்ரி, உருது, இந்தி மற்றும் ஆங்கிலம் (2020-க்கு முன் உருது மட்டுமே ஒரே அதிகாரப்பூர்வ மொழியாக இருந்தது).",
            "why_a_en": "The 2020 enactment added Kashmiri, Dogri, and Hindi alongside Urdu and English.",
            "why_a_ta": "2020 சட்டமானது உருது மற்றும் ஆங்கிலத்துடன் காஷ்மீரி, டோக்ரி மற்றும் இந்தியைச் சேர்த்தது.",
            "why_b_en": "Urdu was the sole language until the 2020 reform.",
            "why_b_ta": "2020 சீர்திருத்தம் வரை உருது மட்டுமே ஒரே மொழியாக இருந்தது.",
            "why_c_en": "Two languages is incorrect following the 2020 Act.",
            "why_c_ta": "2020 சட்டத்திற்குப் பிறகு இரண்டு மொழிகள் என்பது தவறானது.",
            "why_d_en": "Dogri and Hindi are also included, making it five.",
            "why_d_ta": "டோக்ரி மற்றும் இந்தியும் சேர்க்கப்பட்டு மொத்தம் ஐந்து மொழிகளாக உள்ளன.",
            "tip_en": "J&K has 5 official languages since 2020: Kashmiri + Dogri + Urdu + Hindi + English.",
            "tip_ta": "2020 முதல் ஜம்மு-காஷ்மீரில் 5 அதிகாரப்பூர்வ மொழிகள் உள்ளன: காஷ்மீரி + டோக்ரி + உருது + இந்தி + ஆங்கிலம்.",
            "fact_en": "Kashmiri and Dogri are both Eighth Schedule languages.",
            "fact_ta": "காஷ்மீரி மற்றும் டோக்ரி ஆகிய இரண்டுமே எட்டாவது அட்டவணை மொழிகளாகும்."
        },
        # 18
        {
            "subtopic": "Associate Official Language of States",
            "stem_en": "Which language was declared as the second official language of undivided Andhra Pradesh in 1989 and continues in Telangana today?",
            "stem_ta": "1989-ல் ஒருங்கிணைந்த ஆந்திரப் பிரதேசத்தின் இரண்டாவது அதிகாரப்பூர்வ மொழியாக அறிவிக்கப்பட்டு இன்று தெலங்கானாவிலும் தொடரும் மொழி எது?",
            "options": [
                ("Urdu", "உருது"),
                ("Hindi", "இந்தி"),
                ("Tamil", "தமிழ்"),
                ("Marathi", "மராத்தி")
            ],
            "correct_key": "A",
            "exp_en": "Urdu was recognized as the second official language in Andhra Pradesh in 1989 under Article 345, and Telangana declared Urdu as its second official language across all districts in 2017.",
            "exp_ta": "சரத்து 345-ன் கீழ் 1989-ல் ஆந்திரப் பிரதேசத்தில் உருது இரண்டாவது அதிகாரப்பூர்வ மொழியாக அங்கீகரிக்கப்பட்டது, மேலும் தெலங்கானா 2017-ல் அனைத்து மாவட்டங்களிலும் உருதுவை தனது இரண்டாவது அதிகாரப்பூர்வ மொழியாக அறிவித்தது.",
            "why_a_en": "Urdu is the constitutionally enacted second official language of Telangana and parts of AP.",
            "why_a_ta": "உருது தெலங்கானா மற்றும் ஆந்திராவின் சில பகுதிகளில் சட்டப்பூர்வ இரண்டாவது அதிகாரப்பூர்வ மொழியாகும்.",
            "why_b_en": "Hindi is not the second official language of Andhra Pradesh or Telangana.",
            "why_b_ta": "இந்தி ஆந்திரா அல்லது தெலங்கானாவின் இரண்டாவது அதிகாரப்பூர்வ மொழி அல்ல.",
            "why_c_en": "Tamil is an official language in Puducherry and Tamil Nadu, not AP/Telangana.",
            "why_c_ta": "தமிழ் புதுச்சேரி மற்றும் தமிழ்நாட்டின் அதிகாரப்பூர்வ மொழி, ஆந்திரா/தெலங்கானாவின் மொழி அல்ல.",
            "why_d_en": "Marathi is spoken in border areas but is not the State second official language.",
            "why_d_ta": "மராத்தி எல்லைப் பகுதிகளில் பேசப்படுகிறது, ஆனால் மாநில இரண்டாவது அதிகாரப்பூர்வ மொழி அல்ல.",
            "tip_en": "States with Urdu as second official language: Bihar (1980, first), UP (1989), Telangana (2017).",
            "tip_ta": "உருதுவை இரண்டாவது அதிகாரப்பூர்வ மொழியாகக் கொண்ட மாநிலங்கள்: பீகார் (1980, முதல்), உ.பி (1989), தெலங்கானா (2017).",
            "fact_en": "Bihar was the first State in India to declare Urdu as its second official language in 1980.",
            "fact_ta": "1980-ல் உருதுவை இரண்டாவது அதிகாரப்பூர்வ மொழியாக அறிவித்த இந்தியாவின் முதல் மாநிலம் பீகார் ஆகும்."
        },
        # 19
        {
            "subtopic": "Puducherry Official Languages",
            "stem_en": "Which of the following languages is NOT an official language of the Union Territory of Puducherry under the Puducherry Official Languages Act, 1965?",
            "stem_ta": "புதுச்சேரி அதிகாரப்பூர்வ மொழிகள் சட்டம் 1965-ன் கீழ், புதுச்சேரி ஒன்றியப் பகுதியின் அதிகாரப்பூர்வ மொழி அல்லாதது எது?",
            "options": [
                ("Hindi", "இந்தி"),
                ("Tamil", "தமிழ்"),
                ("Malayalam", "மலையாளம்"),
                ("Telugu", "தெலுங்கு")
            ],
            "correct_key": "A",
            "exp_en": "Under the Puducherry Official Languages Act, 1965, the official languages are Tamil (Puducherry and Karaikal), Malayalam (Mahe), Telugu (Yanam), along with English and French. Hindi is NOT an official language of Puducherry.",
            "exp_ta": "புதுச்சேரி அதிகாரப்பூர்வ மொழிகள் சட்டம் 1965-ன் கீழ், தமிழ் (புதுச்சேரி மற்றும் காரைக்கால்), மலையாளம் (மாஹே), தெலுங்கு (ஏனாம்) ஆகியவற்றுடன் ஆங்கிலம் மற்றும் பிரெஞ்சு அதிகாரப்பூர்வ மொழிகளாக உள்ளன. இந்தி புதுச்சேரியின் அதிகாரப்பூர்வ மொழி அல்ல.",
            "why_a_en": "Hindi is not designated as an official language in Puducherry.",
            "why_a_ta": "புதுச்சேரியில் இந்தி ஓர் அதிகாரப்பூர்வ மொழியாக அறிவிக்கப்படவில்லை.",
            "why_b_en": "Tamil is the primary official language of Puducherry and Karaikal enclaves.",
            "why_b_ta": "புதுச்சேரி மற்றும் காரைக்கால் பகுதிகளுக்குத் தமிழ் முதன்மை அதிகாரப்பூர்வ மொழியாகும்.",
            "why_c_en": "Malayalam is the official language for Mahe enclave.",
            "why_c_ta": "மாஹே பகுதிக்கு மலையாளம் அதிகாரப்பூர்வ மொழியாகும்.",
            "why_d_en": "Telugu is the official language for Yanam enclave.",
            "why_d_ta": "ஏனாம் பகுதிக்கு தெலுங்கு அதிகாரப்பூர்வ மொழியாகும்.",
            "tip_en": "Puducherry reflects French colonial enclaves: Tamil (Puducherry/Karaikal), Malayalam (Mahe), Telugu (Yanam).",
            "tip_ta": "புதுச்சேரி பிரெஞ்சு காலனித்துவ பகுதிகளைப் பிரதிபலிக்கிறது: தமிழ் (புதுச்சேரி/காரைக்கால்), மலையாளம் (மாஹே), தெலுங்கு (ஏனாம்).",
            "fact_en": "French also enjoys recognized status in Puducherry under the Treaty of Cession, 1956.",
            "fact_ta": "1956-ன் அதிகார மாற்ற உடன்படிக்கையின் கீழ் பிரெஞ்சு மொழியும் புதுச்சேரியில் அங்கீகரிக்கப்பட்ட அந்தஸ்தைப் பெற்றுள்ளது."
        },
        # 20
        {
            "subtopic": "Section 3(3) Mandatory Bilingual Documents",
            "stem_en": "Which of the following documents is legally required under Section 3(3) of the Official Languages Act, 1963 to be issued bilingually in both Hindi and English?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 3(3)-ன் கீழ், பின்வரும் ஆவணங்களில் எது இந்தி மற்றும் ஆங்கிலம் ஆகிய இரு மொழிகளிலும் கட்டாயமாக வெளியிடப்பட வேண்டும்?",
            "options": [
                ("General orders, notifications, contracts, and press communiques issued by the Central Government", "மத்திய அரசால் வெளியிடப்படும் பொது ஆணைகள், அறிவிப்புகள், ஒப்பந்தங்கள் மற்றும் செய்திக் குறிப்புகள்"),
                ("Internal handwritten personal notes of government employees", "அரசு ஊழியர்களின் உள் அலுவலகக் கையெழுத்துக் குறிப்புகள்"),
                ("Private business communications between commercial firms", "வணிக நிறுவனங்களுக்கு இடையேயான தனியார் வர்த்தகத் தகவல்தொடர்புகள்"),
                ("Judgments delivered by District Munsif Courts", "மாவட்ட உரிமையியல் நீதிமன்றங்களால் வழங்கப்படும் தீர்ப்புகள்")
            ],
            "correct_key": "A",
            "exp_en": "Section 3(3) lists 14 specific categories of documents (resolutions, general orders, rules, notifications, administrative reports, press communiques, contracts, tenders, etc.) that must be published bilingually in both Hindi and English.",
            "exp_ta": "பிரிவு 3(3) மத்திய அரசின் 14 வகையான ஆவணங்களை (தீர்மானங்கள், பொது ஆணைகள், விதிகள், அறிவிப்புகள், அறிக்கைகள், ஒப்பந்தங்கள், ஒப்பந்தப்புள்ளிகள் போன்றவை) இந்தி மற்றும் ஆங்கிலம் ஆகிய இரு மொழிகளிலும் வெளியிடப்பட வேண்டும் எனக் கட்டாயமாக்குகிறது.",
            "why_a_en": "Section 3(3) explicitly enumerates general orders, notifications, and contracts.",
            "why_a_ta": "பிரிவு 3(3) பொது ஆணைகள், அறிவிப்புகள் மற்றும் ஒப்பந்தங்களை வெளிப்படையாகப் பட்டியலிடுகிறது.",
            "why_b_en": "Internal informal drafts are governed by Rule 8, not Section 3(3).",
            "why_b_ta": "உள் அலுவலக வரைவுகள் விதி 8-ஆல் ஆளப்படுகின்றன, பிரிவு 3(3)-ஆல் அல்ல.",
            "why_c_en": "Private businesses are completely outside the scope of Section 3(3).",
            "why_c_ta": "தனியார் நிறுவனங்கள் பிரிவு 3(3)-ன் வரம்பிற்கு முற்றிலும் அப்பாற்பட்டவை.",
            "why_d_en": "District courts are subordinate judiciary governed by State Acts under CrPC/CPC.",
            "why_d_ta": "மாவட்ட நீதிமன்றங்கள் மாநிலச் சட்டங்களால் நிர்வகிக்கப்படும் சார்நிலை நீதிமன்றங்களாகும்.",
            "tip_en": "Section 3(3) = 14 categories of central documents MUST be bilingual (NO exceptions).",
            "tip_ta": "பிரிவு 3(3) = 14 வகையான மத்திய ஆவணங்கள் கட்டாயமாக இருமொழிகளிலும் இருக்க வேண்டும் (விதிவிலக்கு இல்லை).",
            "fact_en": "The responsibility for ensuring compliance rests with the person signing the document under Rule 6.",
            "fact_ta": "விதி 6-ன் கீழ் ஆவணத்தில் கையொப்பமிடும் நபரே இருமொழி இணக்கத்தை உறுதி செய்வதற்கான பொறுப்பைக் கொண்டுள்ளார்."
        },
        # 21
        {
            "subtopic": "Judicial Precedent - Union of India v. Murasoli Maran",
            "stem_en": "In the landmark case 'Union of India v. Murasoli Maran (1977)', what did the Supreme Court of India uphold regarding Hindi in-service training?",
            "stem_ta": "'யூனியன் ஆஃப் இந்தியா எதிர் முரசொலி மாறன் (1977)' என்ற முக்கிய வழக்கில், பணியிடை இந்திப் பயிற்சி தொடர்பாக இந்திய உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "options": [
                ("Presidential orders providing in-service Hindi training for Central Government employees are valid and do not violate parliamentary assurances", "மத்திய அரசு ஊழியர்களுக்கு பணியிடை இந்திப் பயிற்சி அளிக்கும் குடியரசுத் தலைவரின் ஆணைகள் செல்லுபடியாகும் மற்றும் அவை நாடாளுமன்ற உறுதிமொழிகளை மீறவில்லை"),
                ("All in-service language training was declared unconstitutional", "அனைத்துப் பணியிடை மொழிப் பயிற்சிகளும் அரசியலமைப்புக்கு எதிரானவை என அறிவிக்கப்பட்டது"),
                ("Hindi training was made compulsory for all State government staff", "அனைத்து மாநில அரசு ஊழியர்களுக்கும் இந்திப் பயிற்சி கட்டாயமாக்கப்பட்டது"),
                ("English was declared abolished from Central Secretariat", "மத்தியச் செயலகத்திலிருந்து ஆங்கிலம் நீக்கப்பட்டதாக அறிவிக்கப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "In Union of India v. Murasoli Maran (1977), the Supreme Court ruled that Presidential orders providing for Hindi training to central employees under Article 344(6) were valid promotional measures, and did not conflict with the continued use of English under the 1963 Act.",
            "exp_ta": "யூனியன் ஆஃப் இந்தியா எதிர் முரசொலி மாறன் (1977) வழக்கில், சரத்து 344(6)-ன் கீழ் மத்திய அரசு ஊழியர்களுக்கு இந்திப் பயிற்சி வழங்கும் குடியரசுத் தலைவர் ஆணைகள் செல்லுபடியாகும் என்றும், அவை 1963 சட்டத்தின் கீழ் ஆங்கிலம் தொடர்வதற்கு முரணானவை அல்ல என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "The Supreme Court upheld the constitutional validity of promotional Hindi training for central staff.",
            "why_a_ta": "மத்திய அரசுப் பணியாளர்களுக்கான இந்திப் பயிற்சியின் அரசியலமைப்புச் செல்லுபடியை உச்ச நீதிமன்றம் உறுதி செய்தது.",
            "why_b_en": "Training was not struck down; it was upheld.",
            "why_b_ta": "பயிற்சி ரத்து செய்யப்படவில்லை; அது உறுதி செய்யப்பட்டது.",
            "why_c_en": "The order applied strictly to Central employees, never to State government staff.",
            "why_c_ta": "இவ்வாணை மத்திய ஊழியர்களுக்கு மட்டுமே பொருந்தும், மாநில ஊழியர்களுக்குப் பொருந்தாது.",
            "why_d_en": "English continued as an associate official language.",
            "why_d_ta": "ஆங்கிலம் கூடுதல் அதிகாரப்பூர்வ மொழியாகத் தொடர்ந்தது.",
            "tip_en": "Murasoli Maran Case (1977): Promotional Hindi training for central staff is constitutional under Article 344(6).",
            "tip_ta": "முரசொலி மாறன் வழக்கு (1977): மத்தியப் பணியாளர்களுக்கு இந்திப் பயிற்சி அளிப்பது சரத்து 344(6)-ன் கீழ் அரசியலமைப்பு ரீதியாகச் செல்லுபடியாகும்.",
            "fact_en": "The petition was filed by DMK leader Murasoli Maran challenging Hindi training incentives.",
            "fact_ta": "இந்திப் பயிற்சி ஊக்கத்தொகைகளை எதிர்த்து திமுக தலைவர் முரசொலி மாறனால் இந்த வழக்கு தொடரப்பட்டது."
        },
        # 22
        {
            "subtopic": "Judicial Precedent - R.R. Dalavai v. State of Tamil Nadu",
            "stem_en": "In 'R.R. Dalavai v. State of Tamil Nadu (1976)', why did the Supreme Court strike down the State Government's scheme of granting pension to anti-Hindi agitators?",
            "stem_ta": "'ஆர்.ஆர். தளவாய் எதிர் தமிழ்நாடு அரசு (1976)' வழக்கில், இந்தி எதிர்ப்புப் போராளிகளுக்கு ஓய்வூதியம் வழங்கும் மாநில அரசின் திட்டத்தை உச்ச நீதிமன்றம் ஏன் ரத்து செய்தது?",
            "options": [
                ("Because granting pension for agitation against a constitutional provision (Part XVII) undermines the Constitution and public exchequer", "அரசியலமைப்பு விதிக்கு (பகுதி XVII) எதிரான போராட்டத்திற்கு ஓய்வூதியம் வழங்குவது அரசியலமைப்பையும் பொதுக் கருவூலத்தையும் சீர்குலைக்கும் என்பதால்"),
                ("Because the State Government had no funds in the treasury", "மாநில அரசிடம் கருவூலத்தில் நிதி இல்லாததால்"),
                ("Because pensions can only be granted to military veterans", "ஓய்வூதியம் ராணுவ வீரர்களுக்கு மட்டுமே வழங்கப்பட முடியும் என்பதால்"),
                ("Because Tamil was declared the national language", "தமிழ் தேசிய மொழியாக அறிவிக்கப்பட்டதால்")
            ],
            "correct_key": "A",
            "exp_en": "The Supreme Court held that pensioning persons who agitated against the implementation of a constitutional provision (Part XVII) was unconstitutional, as the State cannot use public funds to reward agitation against constitutional mandates.",
            "exp_ta": "அரசியலமைப்பு விதியை (பகுதி XVII) செயல்படுத்துவதற்கு எதிராகப் போராடிய நபர்களுக்கு ஓய்வூதியம் வழங்குவது அரசியலமைப்புக்கு எதிரானது என்று உச்ச நீதிமன்றம் கூறியது; அரசியலமைப்பு விதிகளுக்கு எதிரான போராட்டத்திற்கு வெகுமதி அளிக்க அரசு பொது நிதியைப் பயன்படுத்த முடியாது.",
            "why_a_en": "Rewarding resistance against a constitutional provision was held contrary to the rule of law.",
            "why_a_ta": "அரசியலமைப்பு விதிக்கு எதிரான போராட்டத்திற்கு வெகுமதி அளிப்பது சட்டத்தின் ஆட்சிக்கு முரணானது எனத் தீர்ப்பளிக்கப்பட்டது.",
            "why_b_en": "Financial inadequacy was not the constitutional ground of invalidation.",
            "why_b_ta": "நிதிப் பற்றாக்குறை என்பது தீர்ப்பின் அரசியலமைப்பு அடிப்படை அல்ல.",
            "why_c_en": "States have power to grant welfare pensions, but not for unconstitutional purposes.",
            "why_c_ta": "மாநிலங்களுக்கு நல ஓய்வூதியம் வழங்கும் அதிகாரம் உண்டு, ஆனால் அரசியலமைப்பிற்கு எதிரான நோக்கங்களுக்காக அல்ல.",
            "why_d_en": "Tamil was not declared national language.",
            "why_d_ta": "தமிழ் தேசிய மொழியாக அறிவிக்கப்படவில்லை.",
            "tip_en": "R.R. Dalavai Case (1976): Public funds cannot reward agitation against constitutional Part XVII provisions.",
            "tip_ta": "ஆர்.ஆர். தளவாய் வழக்கு (1976): அரசியலமைப்பு பகுதி XVII விதிகளுக்கு எதிரான போராட்டங்களுக்குப் பொது நிதியிலிருந்து ஓய்வூதியம் வழங்க முடியாது.",
            "fact_en": "Justice A.N. Ray authored the judgment striking down the Pension Scheme.",
            "fact_ta": "நீதிபதி ஏ.என். ரே ஓய்வூதியத் திட்டத்தை ரத்து செய்து தீர்ப்பளித்தார்."
        },
        # 23
        {
            "subtopic": "Judicial Precedent - State of Karnataka v. Associated Management",
            "stem_en": "In the landmark Constitution Bench judgment 'State of Karnataka v. Associated Management of Primary and Secondary Schools (2014)', what was held regarding medium of instruction?",
            "stem_ta": "'கர்நாடக அரசு எதிர் தொடக்க மற்றும் இடைநிலைப் பள்ளிகளின் கூட்டமைப்பு (2014)' என்ற முக்கிய அரசியல் சாசன அமர்வுத் தீர்ப்பில், பயிற்றுமொழி தொடர்பாக என்ன தீர்ப்பளிக்கப்பட்டது?",
            "options": [
                ("The State cannot compel private unaided schools to teach only in the mother tongue against the choice of the child or parents", "குழந்தை அல்லது பெற்றோரின் விருப்பத்திற்கு மாறாக, தனியார் உதவிபெறாத பள்ளிகளில் தாய்மொழியில் மட்டுமே கற்பிக்க வேண்டும் என்று அரசு கட்டாயப்படுத்த முடியாது"),
                ("Mother tongue must be the exclusive medium of instruction in all universities", "அனைத்துப் பல்கலைக்கழகங்களிலும் தாய்மொழி மட்டுமே ஒரே பயிற்றுமொழியாக இருக்க வேண்டும்"),
                ("English medium schools were declared unlawful across India", "இந்தியா முழுவதும் ஆங்கில வழிக் கல்விப் பள்ளிகள் சட்டவிரோதமானவை என அறிவிக்கப்பட்டது"),
                ("Article 350A confers an absolute right on States to prohibit English", "சரத்து 350A ஆங்கிலத்தைத் தடை செய்ய மாநிலங்களுக்கு முழுமையான உரிமையை வழங்குகிறது")
            ],
            "correct_key": "A",
            "exp_en": "A 5-judge Constitution Bench held that the choice of medium of instruction in schools is facet of freedom of expression under Article 19(1)(a). The State cannot compel children or parents to study only in mother tongue/regional language in private unaided schools.",
            "exp_ta": "5 நீதிபதிகள் கொண்ட அரசியல் சாசன அமர்வு, பள்ளிகளில் பயிற்றுமொழியைத் தேர்ந்தெடுப்பது சரத்து 19(1)(a)-ன் கீழான கருத்துச் சுதந்திரத்தின் ஒரு பகுதி என்று தீர்ப்பளித்தது. தனியார் உதவிபெறாத பள்ளிகளில் தாய்மொழி/வட்டார மொழியில் மட்டுமே படிக்க வேண்டும் என்று அரசு குழந்தைகளையோ அல்லது பெற்றோரையோ கட்டாயப்படுத்த முடியாது.",
            "why_a_en": "Choice of educational medium is protected under Article 19(1)(a) freedom of speech and expression.",
            "why_a_ta": "பயிற்றுமொழித் தேர்வு என்பது சரத்து 19(1)(a) பேச்சு மற்றும் கருத்துச் சுதந்திரத்தின் கீழ் பாதுகாக்கப்படுகிறது.",
            "why_b_en": "Higher education medium was not the subject of this school-level dispute.",
            "why_b_ta": "உயர்கல்வி பயிற்றுமொழி இத்தீர்ப்பின் மையப் பொருள் அல்ல.",
            "why_c_en": "English medium schools are constitutionally valid and protected.",
            "why_c_ta": "ஆங்கில வழிக் கல்விப் பள்ளிகள் அரசியலமைப்பு ரீதியாகச் செல்லுபடியாகும் மற்றும் பாதுகாக்கப்பட்டவை.",
            "why_d_en": "Article 350A is an enabling provision for minorities, not a restrictive ban on English.",
            "why_d_ta": "சரத்து 350A என்பது சிறுபான்மையினருக்கான ஒரு வசதியளிக்கும் விதி, ஆங்கிலத்தின் மீதான தடையல்ல.",
            "tip_en": "Associated Management Case (2014): Medium of instruction choice is protected under Article 19(1)(a).",
            "tip_ta": "அசோசியேட்டட் மேனேஜ்மென்ட் வழக்கு (2014): பயிற்றுமொழித் தேர்வு சரத்து 19(1)(a)-ன் கீழ் பாதுகாக்கப்படுகிறது.",
            "fact_en": "Karnataka's 1994 Language Policy mandating Kannada medium in primary grades was partially struck down.",
            "fact_ta": "தொடக்க வகுப்புகளில் கன்னட மொழியைக் கட்டாயமாக்கிய கர்நாடகத்தின் 1994 மொழிக் கொள்கை பகுதியளவு ரத்து செய்யப்பட்டது."
        },
        # 24
        {
            "subtopic": "Languages in Eighth Schedule - Script Matching",
            "stem_en": "Which of the following Eighth Schedule languages is traditionally written in the Perso-Arabic (Nastaliq) script?",
            "stem_ta": "பின்வரும் எட்டாவது அட்டவணை மொழிகளில் பாரம்பரியமாக பாரசீக-அரபு (நஸ்தலீக்) வரிவடிவத்தில் எழுதப்படும் மொழி எது?",
            "options": [
                ("Urdu", "உருது"),
                ("Sindhi", "சிந்தி"),
                ("Kashmiri", "காஷ்மீரி"),
                ("Punjabi", "பஞ்சாபி")
            ],
            "correct_key": "A",
            "exp_en": "Urdu is traditionally and officially written in the Perso-Arabic script in the calligraphic Nastaliq style. (Note: Kashmiri and Sindhi also use Perso-Arabic variants, but Urdu is the classic archetype; Punjabi is written in Gurmukhi in India).",
            "exp_ta": "உருது பாரம்பரியமாகவும் அதிகாரப்பூர்வமாகவும் நஸ்தலீக் பாணியிலான பாரசீக-அரபு வரிவடிவத்தில் எழுதப்படுகிறது (இந்தியாவில் பஞ்சாபி குர்முகி வரிவடிவத்தில் எழுதப்படுகிறது).",
            "why_a_en": "Urdu's standard constitutional script in India is the Perso-Arabic Nastaliq script.",
            "why_a_ta": "இந்தியாவில் உருதுவின் நிலையான அரசியலமைப்பு வரிவடிவம் பாரசீக-அரபு நஸ்தலீக் வரிவடிவமாகும்.",
            "why_b_en": "Sindhi is written in Arabic script in Pakistan and both Arabic and Devanagari in India.",
            "why_b_ta": "சிந்தி பாகிஸ்தானில் அரபு வரிவடிவத்திலும், இந்தியாவில் அரபு மற்றும் தேவநாகரி ஆகிய இரண்டிலும் எழுதப்படுகிறது.",
            "why_c_en": "Kashmiri uses a modified Perso-Arabic script, but Urdu is the foremost Perso-Arabic standard.",
            "why_c_ta": "காஷ்மீரி மாற்றியமைக்கப்பட்ட பாரசீக-அரபு வரிவடிவத்தைப் பயன்படுத்துகிறது, ஆனால் உருதுவே முதன்மையான நிலையான வடிவமாகும்.",
            "why_d_en": "Punjabi in India is written in Gurmukhi script (Shahmukhi is used in Pakistani Punjab).",
            "why_d_ta": "இந்தியாவில் பஞ்சாபி குர்முகி வரிவடிவத்தில் எழுதப்படுகிறது (பாகிஸ்தானில் ஷாமுகி பயன்படுத்தப்படுகிறது).",
            "tip_en": "Script Check: Punjabi = Gurmukhi; Dogri = Devanagari; Santhali = Ol Chiki; Urdu = Perso-Arabic.",
            "tip_ta": "வரிவடிவ சரிபார்ப்பு: பஞ்சாபி = குர்முகி; டோக்ரி = தேவநாகரி; சந்தாலி = ஒல் சிக்கி; உருது = பாரசீக-அரபு.",
            "fact_en": "Urdu was born out of the linguistic fusion of Shauraseni Prakrit, Khariboli, Persian, and Arabic.",
            "fact_ta": "சௌரசேனி பிராகிருதம், கரிபோலி, பாரசீகம் மற்றும் அரபு மொழிகளின் கலப்பால் உருது உருவானது."
        },
        # 25
        {
            "subtopic": "Languages with Dual Scripts in India",
            "stem_en": "For which Eighth Schedule language did the Government of India officially recognize both the Devanagari script and the Perso-Arabic script?",
            "stem_ta": "எந்த எட்டாவது அட்டவணை மொழிக்கு இந்திய அரசு தேவநாகரி மற்றும் பாரசீக-அரபு ஆகிய இரண்டு வரிவடிவங்களையும் அதிகாரப்பூர்வமாக அங்கீகரித்துள்ளது?",
            "options": [
                ("Sindhi", "சிந்தி"),
                ("Urdu", "உருது"),
                ("Kashmiri", "காஷ்மீரி"),
                ("Nepali", "நேபாளி")
            ],
            "correct_key": "A",
            "exp_en": "The Ministry of Education officially recognizes both the Arabic-Sindhi script and the Devanagari script for the Sindhi language in India, reflecting partition displacement.",
            "exp_ta": "இந்தியாவில் சிந்தி மொழிக்கு அரபு-சிந்தி வரிவடிவம் மற்றும் தேவநாகரி வரிவடிவம் ஆகிய இரண்டையும் கல்வி அமைச்சகம் அதிகாரப்பூர்வமாக அங்கீகரித்துள்ளது.",
            "why_a_en": "Sindhi is unique in having an official dual-script policy in India.",
            "why_a_ta": "இந்தியாவில் அதிகாரப்பூர்வ இரட்டை வரிவடிவக் கொள்கையைக் கொண்ட தனித்துவமான மொழி சிந்தி ஆகும்.",
            "why_b_en": "Urdu is officially recognized primarily in the Perso-Arabic script.",
            "why_b_ta": "உருது அதிகாரப்பூர்வமாக முதன்மையாக பாரசீக-அரபு வரிவடிவத்திலேயே அங்கீகரிக்கப்பட்டுள்ளது.",
            "why_c_en": "Kashmiri officially uses the Nastaliq Perso-Arabic script.",
            "why_c_ta": "காஷ்மீரி அதிகாரப்பூர்வமாக நஸ்தலீக் பாரசீக-அரபு வரிவடிவத்தைப் பயன்படுத்துகிறது.",
            "why_d_en": "Nepali is written in Devanagari script.",
            "why_d_ta": "நேபாளி தேவநாகரி வரிவடிவத்தில் எழுதப்படுகிறது.",
            "tip_en": "Sindhi Dual Script: Devanagari + Arabic-Sindhi.",
            "tip_ta": "சிந்தி இரட்டை வரிவடிவம்: தேவநாகரி + அரபு-சிந்தி.",
            "fact_en": "The Sindhi Language Bill controversy was resolved by permitting both scripts.",
            "fact_ta": "சிந்தி மொழி வரிவடிவ சர்ச்சை இரண்டு வரிவடிவங்களையும் அனுமதிப்பதன் மூலம் தீர்க்கப்பட்டது."
        },
        # 26
        {
            "subtopic": "Article 350 vs Article 350A vs Article 350B",
            "stem_en": "Which Article of the Constitution of India deals specifically with the 'Language to be used in representations for redress of grievances'?",
            "stem_ta": "இந்திய அரசியலமைப்பின் எந்தச் சரத்து குறிப்பாக 'குறைகளைத் தீர்ப்பதற்கான மனுக்களில் பயன்படுத்தப்பட வேண்டிய மொழி'யைக் கையாள்கிறது?",
            "options": [
                ("Article 350", "சரத்து 350"),
                ("Article 350A", "சரத்து 350A"),
                ("Article 350B", "சரத்து 350B"),
                ("Article 351", "சரத்து 351")
            ],
            "correct_key": "A",
            "exp_en": "Article 350 is dedicated to representations for redress of grievances in any language used in the Union or State. Article 350A is for primary mother tongue instruction, and Article 350B is for the Special Officer for Linguistic Minorities.",
            "exp_ta": "சரத்து 350 ஒன்றியம் அல்லது மாநிலத்தில் பயன்பாட்டில் உள்ள எந்த மொழியிலும் குறைகளைத் தீர்ப்பதற்கான மனுக்களைக் கையாள்கிறது. சரத்து 350A தாய்மொழி தொடக்கக் கல்விக்கானது, மற்றும் சரத்து 350B மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலருக்கானது.",
            "why_a_en": "Article 350 is the unlettered, original article specifically dealing with citizen grievances.",
            "why_a_ta": "சரத்து 350 என்பது குடிமக்களின் குறைகளை நேரடியாகக் கையாளும் அசல் சரத்தாகும்.",
            "why_b_en": "Article 350A deals with primary education in mother tongue.",
            "why_b_ta": "சரத்து 350A தாய்மொழியில் தொடக்கக் கல்வியைக் கையாள்கிறது.",
            "why_c_en": "Article 350B deals with the Commissioner for Linguistic Minorities.",
            "why_c_ta": "சரத்து 350B மொழிச் சிறுபான்மையினர் ஆணையரைக் கையாள்கிறது.",
            "why_d_en": "Article 351 contains the directive for development of Hindi.",
            "why_d_ta": "சரத்து 351 இந்தி வளர்ச்சிக்கான வழிகாட்டுதலைக் கொண்டுள்ளது.",
            "tip_en": "Chapter IV Directives: 350 (Grievance Representation) -> 350A (Mother Tongue Primary) -> 350B (Special Officer) -> 351 (Hindi Development).",
            "tip_ta": "அத்தியாயம் IV வழிகாட்டுதல்கள்: 350 (குறைதீர்ப்பு மனு) -> 350A (தாய்மொழித் தொடக்கக் கல்வி) -> 350B (சிறப்பு அலுவலர்) -> 351 (இந்தி வளர்ச்சி).",
            "fact_en": "Article 350 was part of the original 1950 text, whereas 350A and 350B were inserted in 1956.",
            "fact_ta": "சரத்து 350 அசல் 1950 உரையின் ஒரு பகுதியாகும், ஆனால் 350A மற்றும் 350B ஆகியவை 1956-ல் சேர்க்கப்பட்டன."
        },
        # 27
        {
            "subtopic": "Article 348 Authoritative Translation Clause",
            "stem_en": "Under Article 348(3), if a State Legislature prescribes any language other than English for use in Bills or Acts passed by it, what must be published in the Official Gazette of that State?",
            "stem_ta": "சரத்து 348(3)-ன் கீழ், ஒரு மாநில சட்டமன்றம் தான் நிறைவேற்றும் மசோதாக்கள் அல்லது சட்டங்களில் ஆங்கிலம் அல்லாத வேறு ஏதேனும் மொழியைப் பயன்படுத்த பரிந்துரைத்தால், அம்மாநிலத்தின் அதிகாரப்பூர்வ அரசிதழில் எது வெளியிடப்பட வேண்டும்?",
            "options": [
                ("A translation of the same in the English language published under the authority of the Governor, which shall be deemed to be the authoritative text", "ஆளுநரின் அதிகாரத்தின் கீழ் வெளியிடப்பட்ட அதன் ஆங்கில மொழிபெயர்ப்பு, அதுவே அதிகாரப்பூர்வ மூல வாசகமாகக் கருதப்படும்"),
                ("A translation in Hindi verified by the Union Law Ministry", "ஒன்றிய சட்ட அமைச்சகத்தால் சரிபார்க்கப்பட்ட இந்தி மொழிபெயர்ப்பு"),
                ("A summary in all Eighth Schedule languages", "அனைத்து எட்டாவது அட்டவணை மொழிகளிலும் ஒரு சுருக்கம்"),
                ("No translation is legally required", "எந்த மொழிபெயர்ப்பும் சட்டப்படி தேவையில்லை")
            ],
            "correct_key": "A",
            "exp_en": "Article 348(3) mandates that where a State Legislature prescribes a regional language for Bills/Acts, a translation of the same in the English language published under the authority of the Governor shall be deemed to be the authoritative text in the English language.",
            "exp_ta": "சரத்து 348(3)-ன் படி, ஒரு மாநில சட்டமன்றம் மசோதாக்கள்/சட்டங்களுக்கு வட்டார மொழியைப் பரிந்துரைக்கும் போது, ஆளுநரின் அதிகாரத்தின் கீழ் வெளியிடப்பட்ட அதன் ஆங்கில மொழிபெயர்ப்பு, ஆங்கில மொழியிலான அதிகாரப்பூர்வ மூல வாசகமாகக் கருதப்படும்.",
            "why_a_en": "Article 348(3) establishes the authoritative English text requirement for State legislation.",
            "why_a_ta": "சரத்து 348(3) மாநிலச் சட்டங்களுக்கான அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்புத் தேவையை நிறுவுகிறது.",
            "why_b_en": "Hindi translation is not mandated by Article 348(3).",
            "why_b_ta": "சரத்து 348(3)-ல் இந்தி மொழிபெயர்ப்பு கட்டாயமாக்கப்படவில்லை.",
            "why_c_en": "Summaries in all 22 languages are never required for State Acts.",
            "why_c_ta": "மாநிலச் சட்டங்களுக்கு அனைத்து 22 மொழிகளிலும் சுருக்கங்கள் தேவையில்லை.",
            "why_d_en": "The translation is mandatory for legal certainty and judicial review.",
            "why_d_ta": "சட்ட ரீதியான உறுதிப்பாடு மற்றும் நீதித்துறை மறுஆய்வுக்கு மொழிபெயர்ப்பு கட்டாயமாகும்.",
            "tip_en": "Article 348(3): State Act in Tamil -> Authoritative text in ENGLISH must be published by Governor.",
            "tip_ta": "சரத்து 348(3): தமிழில் மாநிலச் சட்டம் -> ஆளுநரால் ஆங்கிலத்தில் அதிகாரப்பூர்வ மூல வாசகம் வெளியிடப்பட வேண்டும்.",
            "fact_en": "In case of doubt between the Tamil and English texts, the English translation prevails in constitutional courts.",
            "fact_ta": "தமிழ் மற்றும் ஆங்கில உரைகளுக்கு இடையே சந்தேகம் ஏற்பட்டால், அரசியலமைப்பு நீதிமன்றங்களில் ஆங்கில மொழிபெயர்ப்பே மேலோங்கும்."
        },
        # 28
        {
            "subtopic": "Central Hindi Directorate",
            "stem_en": "In which year was the Central Hindi Directorate (Kendriya Hindi Nideshalaya) established under the Ministry of Education to implement the directives of Article 351?",
            "stem_ta": "சரத்து 351-ன் வழிகாட்டுதல்களைச் செயல்படுத்துவதற்காகக் கல்வி அமைச்சகத்தின் கீழ் மத்திய இந்தி இயக்ககம் (கேந்திரிய இந்தி நிதேஷாலயா) எந்த ஆண்டில் நிறுவப்பட்டது?",
            "options": [
                ("1960", "1960"),
                ("1950", "1950"),
                ("1975", "1975"),
                ("1986", "1986")
            ],
            "correct_key": "A",
            "exp_en": "The Central Hindi Directorate was established on March 1, 1960 under the Department of Higher Education, Ministry of Education, to promote and propagate Hindi in accordance with Article 351.",
            "exp_ta": "சரத்து 351-க்கு இணங்க இந்தியைப் பரப்பவும் வளர்க்கவும் கல்வி அமைச்சகத்தின் உயர் கல்வித் துறையின் கீழ் 1960 மார்ச் 1 அன்று மத்திய இந்தி இயக்ககம் நிறுவப்பட்டது.",
            "why_a_en": "March 1, 1960 is the official founding date of the Central Hindi Directorate.",
            "why_a_ta": "1960 மார்ச் 1 என்பது மத்திய இந்தி இயக்ககத்தின் அதிகாரப்பூர்வ நிறுவன தேதியாகும்.",
            "why_b_en": "1950 was the commencement of the Constitution.",
            "why_b_ta": "1950 என்பது அரசியலமைப்பு அமலுக்கு வந்த ஆண்டாகும்.",
            "why_c_en": "1975 was the launch of Department of Official Language in Home Ministry.",
            "why_c_ta": "1975 என்பது உள்துறை அமைச்சகத்தில் அதிகாரப்பூர்வ மொழித் துறை தொடங்கப்பட்ட ஆண்டாகும்.",
            "why_d_en": "1986 was the National Policy on Education year.",
            "why_d_ta": "1986 என்பது தேசியக் கல்விக் கொள்கை ஆண்டாகும்.",
            "tip_en": "Central Hindi Directorate = 1960 (Ministry of Education); Department of Official Language = 1975 (Ministry of Home Affairs).",
            "tip_ta": "மத்திய இந்தி இயக்ககம் = 1960 (கல்வி அமைச்சகம்); அதிகாரப்பூர்வ மொழித் துறை = 1975 (உள்துறை அமைச்சகம்).",
            "fact_en": "The Directorate publishes standard bilingual and trilingual glossaries and dictionaries.",
            "fact_ta": "இயக்ககம் நிலையான இருமொழி மற்றும் மும்மொழி கலைச்சொல் அகராதிகளை வெளியிடுகிறது."
        },
        # 29
        {
            "subtopic": "Department of Official Language Setup",
            "stem_en": "Under which Union Ministry was the Department of Official Language (Rajbhasha Vibhag) set up in June 1975?",
            "stem_ta": "1975 ஜூன் மாதம் அதிகாரப்பூர்வ மொழித் துறை (ராஜ்பாஷா விபாக்) எந்த ஒன்றிய அமைச்சகத்தின் கீழ் அமைக்கப்பட்டது?",
            "options": [
                ("Ministry of Home Affairs", "உள்துறை அமைச்சகம்"),
                ("Ministry of Culture", "கலாச்சார அமைச்சகம்"),
                ("Ministry of Law and Justice", "சட்டம் மற்றும் நீதி அமைச்சகம்"),
                ("Ministry of Parliamentary Affairs", "நாடாளுமன்ற விவகாரங்கள் அமைச்சகம்")
            ],
            "correct_key": "A",
            "exp_en": "The Department of Official Language was created in June 1975 as an independent department under the Ministry of Home Affairs to oversee the implementation of constitutional provisions and the Official Languages Act.",
            "exp_ta": "அரசியலமைப்பு விதிகள் மற்றும் அதிகாரப்பூர்வ மொழிகள் சட்டத்தைச் செயல்படுத்துவதைக் கண்காணிக்க 1975 ஜூன் மாதம் உள்துறை அமைச்சகத்தின் கீழ் ஒரு சுயாதீனத் துறையாக அதிகாரப்பூர்வ மொழித் துறை உருவாக்கப்பட்டது.",
            "why_a_en": "The Department of Official Language operates under the Ministry of Home Affairs.",
            "why_a_ta": "அதிகாரப்பூர்வ மொழித் துறை உள்துறை அமைச்சகத்தின் கீழ் செயல்படுகிறது.",
            "why_b_en": "Ministry of Culture oversees Classical Languages, not Union official language administration.",
            "why_b_ta": "கலாச்சார அமைச்சகம் செம்மொழிகளைக் கண்காணிக்கிறது, ஒன்றிய அதிகாரப்பூர்வ மொழி நிர்வாகத்தை அல்ல.",
            "why_c_en": "Ministry of Law handles legislative drafting and translations.",
            "why_c_ta": "சட்ட அமைச்சகம் சட்ட வரைவு மற்றும் மொழிபெயர்ப்புகளைக் கையாள்கிறது.",
            "why_d_en": "Parliamentary Affairs coordinates legislative business.",
            "why_d_ta": "நாடாளுமன்ற விவகாரங்கள் துறை சட்டமன்றப் பணிகளை ஒருங்கிணைக்கிறது.",
            "tip_en": "Rajbhasha Vibhag = Ministry of Home Affairs (1975).",
            "tip_ta": "ராஜ்பாஷா விபாக் = உள்துறை அமைச்சகம் (1975).",
            "fact_en": "It issues the Annual Programme for the progressive use of Hindi in central offices.",
            "fact_ta": "இது மத்திய அலுவலகங்களில் இந்தி பயன்பாட்டிற்கான வருடாந்திர திட்டத்தை வெளியிடுகிறது."
        },
        # 30
        {
            "subtopic": "Kendriya Hindi Samiti",
            "stem_en": "Who is the Chairman of the Kendriya Hindi Samiti (Central Hindi Committee), the supreme policy-making body for official language guidelines?",
            "stem_ta": "அதிகாரப்பூர்வ மொழி வழிகாட்டுதல்களுக்கான உச்சபட்ச கொள்கை வகுக்கும் அமைப்பான கேந்திரிய இந்தி சமிதியின் (மத்திய இந்தி குழு) தலைவர் யார்?",
            "options": [
                ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
                ("The Union Home Minister", "ஒன்றிய உள்துறை அமைச்சர்"),
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Speaker of Lok Sabha", "மக்களவைத் தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "The Kendriya Hindi Samiti, constituted in 1967, is the apex committee that frames guidelines for the propagation and progressive use of Hindi, and is chaired by the Prime Minister of India.",
            "exp_ta": "1967-ல் அமைக்கப்பட்ட கேந்திரிய இந்தி சமிதி, இந்தி பயன்பாட்டை மேம்படுத்துவதற்கான வழிகாட்டுதல்களை வகுக்கும் உச்ச அமைப்பாகும், இதன் தலைவராக இந்தியப் பிரதமர் உள்ளார்.",
            "why_a_en": "The Prime Minister is the ex-officio Chairman of the Kendriya Hindi Samiti.",
            "why_a_ta": "கேந்திரிய இந்தி சமிதியின் பதவி வழித் தலைவராக இந்தியப் பிரதமர் இருக்கிறார்.",
            "why_b_en": "The Union Home Minister is the Deputy Chairman, not Chairman.",
            "why_b_ta": "ஒன்றிய உள்துறை அமைச்சர் துணைத் தலைவராக உள்ளார், தலைவர் அல்ல.",
            "why_c_en": "The President is the recipient of Committee reports, not committee chairman.",
            "why_c_ta": "குடியரசுத் தலைவர் குழு அறிக்கைகளைப் பெறுபவர், குழுவின் தலைவர் அல்ல.",
            "why_d_en": "The Speaker presides over Lok Sabha.",
            "why_d_ta": "மக்களவைத் தலைவர் மக்களவையை வழிநடத்துபவர்.",
            "tip_en": "Kendriya Hindi Samiti: Chairman = PRIME MINISTER; Deputy Chairman = HOME MINISTER.",
            "tip_ta": "கேந்திரிய இந்தி சமிதி: தலைவர் = பிரதமர்; துணைத் தலைவர் = உள்துறை அமைச்சர்.",
            "fact_en": "It includes key Union Cabinet ministers, Chief Ministers on rotation, and eminent literary figures.",
            "fact_ta": "இதில் முக்கிய ஒன்றிய அமைச்சர்கள், சுழற்சி முறையில் முதலமைச்சர்கள் மற்றும் பிரபல எழுத்தாளர்கள் இடம் பெற்றுள்ளனர்."
        },
        # 31
        {
            "subtopic": "Official Language of Supreme Court Enactments",
            "stem_en": "Has the Parliament of India ever enacted any law under Article 348(1) authorizing the use of Hindi in the Supreme Court of India?",
            "stem_ta": "இந்திய உச்ச நீதிமன்றத்தில் இந்தியைப் பயன்படுத்த அங்கீகரித்து சரத்து 348(1)-ன் கீழ் இந்திய நாடாளுமன்றம் எப்போதாவது ஏதேனும் சட்டத்தை இயற்றியுள்ளதா?",
            "options": [
                ("No, Parliament has never enacted any law authorizing Hindi in the Supreme Court", "இல்லை, உச்ச நீதிமன்றத்தில் இந்தியை அனுமதித்து நாடாளுமன்றம் எந்தச் சட்டத்தையும் இயற்றவில்லை"),
                ("Yes, by the Official Languages Act, 1963", "ஆம், அதிகாரப்பூர்வ மொழிகள் சட்டம், 1963-ன் மூலம்"),
                ("Yes, by the 42nd Constitutional Amendment Act", "ஆம், 42-வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம்"),
                ("Yes, by the Supreme Court Rules, 2013", "ஆம், உச்ச நீதிமன்ற விதிகள் 2013-ன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Parliament has NOT enacted any law under Article 348(1)(a) altering the language of the Supreme Court. Consequently, proceedings in the Supreme Court must be conducted exclusively in English.",
            "exp_ta": "சரத்து 348(1)(a)-ன் கீழ் உச்ச நீதிமன்றத்தின் மொழியை மாற்றி நாடாளுமன்றம் எந்தச் சட்டத்தையும் இயற்றவில்லை. இதன் காரணமாக, உச்ச நீதிமன்றத்தின் நடவடிக்கைகள் கட்டாயமாக ஆங்கிலத்தில் மட்டுமே நடத்தப்பட வேண்டும்.",
            "why_a_en": "English remains the sole lawful language of proceedings and judgments in the Supreme Court.",
            "why_a_ta": "உச்ச நீதிமன்றத்தின் நடவடிக்கைகள் மற்றும் தீர்ப்புகளுக்கான ஒரே சட்டப்பூர்வ மொழியாக ஆங்கிலம் நீடிக்கிறது.",
            "why_b_en": "The 1963 Act authorized Hindi for High Courts (Section 7), NOT for the Supreme Court.",
            "why_b_ta": "1963 சட்டம் உயர் நீதிமன்றங்களுக்கு மட்டுமே இந்தியை அனுமதித்தது (பிரிவு 7), உச்ச நீதிமன்றத்திற்கு அல்ல.",
            "why_c_en": "The 42nd Amendment did not modify Article 348.",
            "why_c_ta": "42-வது திருத்தம் சரத்து 348-ஐ மாற்றியமைக்கவில்லை.",
            "why_d_en": "Supreme Court Rules 2013 cannot override constitutional Article 348(1).",
            "why_d_ta": "உச்ச நீதிமன்ற விதிகள் 2013 அரசியலமைப்புச் சரத்து 348(1)-ஐ மீற முடியாது.",
            "tip_en": "Supreme Court Language: ENGLISH ONLY. Section 7 of 1963 Act applies ONLY to High Courts.",
            "tip_ta": "உச்ச நீதிமன்ற மொழி: ஆங்கிலம் மட்டுமே. 1963 சட்டத்தின் பிரிவு 7 உயர் நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும்.",
            "fact_en": "In 2014, the Full Court of the Supreme Court rejected a proposal to introduce Hindi in Supreme Court proceedings.",
            "fact_ta": "2014-ல் உச்ச நீதிமன்றத்தின் முழு அமர்வு, உச்ச நீதிமன்ற நடவடிக்கைகளில் இந்தியை அறிமுகப்படுத்தும் திட்டத்தை நிராகரித்தது."
        },
        # 32
        {
            "subtopic": "State High Courts Authorized for Hindi",
            "stem_en": "In which four High Courts of India has the use of Hindi been authorized under Article 348(2) and Section 7 of the Official Languages Act, 1963?",
            "stem_ta": "சரத்து 348(2) மற்றும் அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 7-ன் கீழ், இந்தியாவின் எந்த நான்கு உயர் நீதிமன்றங்களில் இந்தி பயன்பாடு அங்கீகரிக்கப்பட்டுள்ளது?",
            "options": [
                ("Allahabad, Patna, Madhya Pradesh, and Rajasthan High Courts", "அலகாபாத், பாட்னா, மத்தியப் பிரதேசம் மற்றும் ராஜஸ்தான் உயர் நீதிமன்றங்கள்"),
                ("Madras, Bombay, Calcutta, and Delhi High Courts", "சென்னை, பம்பாய், கல்கத்தா மற்றும் தில்லி உயர் நீதிமன்றங்கள்"),
                ("Karnataka, Kerala, Andhra Pradesh, and Telangana High Courts", "கர்நாடகா, கேரளா, ஆந்திரப் பிரதேசம் மற்றும் தெலங்கானா உயர் நீதிமன்றங்கள்"),
                ("Punjab & Haryana, Gujarat, Orissa, and Gauhati High Courts", "பஞ்சாப் & ஹரியானா, குஜராத், ஒரிசா மற்றும் குவஹாத்தி உயர் நீதிமன்றங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "The Governors of Uttar Pradesh, Bihar, Madhya Pradesh, and Rajasthan have, with the prior consent of the President, authorized the use of Hindi in the proceedings of Allahabad, Patna, MP, and Rajasthan High Courts.",
            "exp_ta": "உத்தரப் பிரதேசம், பீகார், மத்தியப் பிரதேசம் மற்றும் ராஜஸ்தான் ஆளுநர்கள் குடியரசுத் தலைவரின் முன் அனுமதியுடன், அலகாபாத், பாட்னா, ம.பி மற்றும் ராஜஸ்தான் உயர் நீதிமன்றங்களின் நடவடிக்கைகளில் இந்தியைப் பயன்படுத்த அனுமதித்துள்ளனர்.",
            "why_a_en": "These four Hindi-belt High Courts have officially authorized Hindi under Article 348(2).",
            "why_a_ta": "இந்த நான்கு இந்தி மண்டல உயர் நீதிமன்றங்கள் சரத்து 348(2)-ன் கீழ் அதிகாரப்பூர்வமாக இந்தியை அனுமதித்துள்ளன.",
            "why_b_en": "Madras, Bombay, and Calcutta High Courts function exclusively in English.",
            "why_b_ta": "சென்னை, பம்பாய் மற்றும் கல்கத்தா உயர் நீதிமன்றங்கள் ஆங்கிலத்தில் மட்டுமே செயல்படுகின்றன.",
            "why_c_en": "Southern High Courts have not authorized Hindi.",
            "why_c_ta": "தென்மாநில உயர் நீதிமன்றங்கள் இந்தியை அனுமதிக்கவில்லை.",
            "why_d_en": "Gujarat and Gauhati High Courts conduct proceedings in English.",
            "why_d_ta": "குஜராத் மற்றும் குவஹாத்தி உயர் நீதிமன்றங்கள் ஆங்கிலத்திலேயே நடவடிக்கைகளை நடத்துகின்றன.",
            "tip_en": "High Courts with authorized Hindi = UP, Bihar, MP, Rajasthan (4 High Courts).",
            "tip_ta": "இந்தி அங்கீகரிக்கப்பட்ட உயர் நீதிமன்றங்கள் = உ.பி, பீகார், ம.பி, ராஜஸ்தான் (4 உயர் நீதிமன்றங்கள்).",
            "fact_en": "Tamil Nadu's proposal to authorize Tamil in Madras High Court was returned by the Supreme Court collegium in 2012.",
            "fact_ta": "சென்னை உயர் நீதிமன்றத்தில் தமிழை அனுமதிக்கும் தமிழ்நாட்டின் முன்மொழிவு 2012-ல் உச்ச நீதிமன்ற கொலீஜியத்தால் திருப்பி அனுப்பப்பட்டது."
        },
        # 33
        {
            "subtopic": "Article 343(2) Proviso Presidential Orders",
            "stem_en": "During the 15-year period under Article 343(2), what was the President empowered to authorize by order?",
            "stem_ta": "சரத்து 343(2)-ன் கீழான 15 ஆண்டு காலத்தில், குடியரசுத் தலைவர் தனது ஆணை மூலம் எதனை அங்கீகரிக்க அதிகாரம் பெற்றிருந்தார்?",
            "options": [
                ("The use of the Hindi language in addition to English, and of the Devanagari form of numerals in addition to the international form", "ஆங்கிலத்துடன் கூடுதலாக இந்தி மொழியையும், பன்னாட்டு வடிவத்துடன் கூடுதலாக தேவநாகரி எண்களையும் பயன்படுத்துதல்"),
                ("The total prohibition of English in all government departments", "அனைத்து அரசுத் துறைகளிலும் ஆங்கிலத்தை முழுமையாகத் தடை செய்தல்"),
                ("The replacement of High Court judges who did not know Hindi", "இந்தி தெரியாத உயர் நீதிமன்ற நீதிபதிகளை மாற்றுதல்"),
                ("The declaration of Sanskrit as the sole medium of instruction", "சமஸ்கிருதத்தை ஒரே பயிற்றுமொழியாக அறிவித்தல்")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 343(2) empowered the President, during the 15-year period, to authorize by order the use of the Hindi language in addition to English, and of Devanagari numerals in addition to international numerals, for specified official purposes.",
            "exp_ta": "சரத்து 343(2)-ன் விதிவிலக்கு, 15 ஆண்டு காலத்தில், குறிப்பிட்ட பணிகளுக்காக ஆங்கிலத்துடன் கூடுதலாக இந்தியையும், பன்னாட்டு எண்களுடன் கூடுதலாக தேவநாகரி எண்களையும் பயன்படுத்த ஆணை பிறப்பிக்க குடியரசுத் தலைவருக்கு அதிகாரமளித்தது.",
            "why_a_en": "The proviso provided for gradual presidential authorization of Hindi and Devanagari numerals alongside English.",
            "why_a_ta": "இவ்விதிவிலக்கு ஆங்கிலத்துடன் கூடுதலாக இந்தி மற்றும் தேவநாகரி எண்களை குடியரசுத் தலைவர் படிப்படியாக அங்கீகரிக்க வகை செய்தது.",
            "why_b_en": "The President had no power to prohibit English prematurely.",
            "why_b_ta": "காலத்திற்கு முன்பே ஆங்கிலத்தைத் தடை செய்யும் அதிகாரம் குடியரசுத் தலைவருக்கு இல்லை.",
            "why_c_en": "Judicial appointments were governed by Article 217, not language provisos.",
            "why_c_ta": "நீதிமன்ற நியமனங்கள் சரத்து 217-ஆல் நிர்வகிக்கப்பட்டன, மொழி விதிகளால் அல்ல.",
            "why_d_en": "Sanskrit was not the subject of Article 343(2).",
            "why_d_ta": "சமஸ்கிருதம் சரத்து 343(2)-ன் பொருள் அல்ல.",
            "tip_en": "Presidential Orders under 343(2) proviso: 1952 (warrants, treaties in Hindi), 1955 (Hindi for specific purposes).",
            "tip_ta": "சரத்து 343(2) விதிவிலக்கின் கீழான குடியரசுத் தலைவர் ஆணைகள்: 1952 (ஆணைகள், ஒப்பந்தங்கள் இந்தியில்), 1955 (குறிப்பிட்ட பணிகளுக்கு இந்தி).",
            "fact_en": "These presidential orders enabled Hindi to be introduced progressively without violating the transition clause.",
            "fact_ta": "இக்குடியரசுத் தலைவர் ஆணைகள் இடைக்கால விதியை மீறாமல் இந்தியைப் படிப்படியாக அறிமுகப்படுத்த உதவின."
        },
        # 34
        {
            "subtopic": "Article 344 Commission Report Recipient",
            "stem_en": "To whom does the Official Language Commission submit its report under Article 344, and who examines that report?",
            "stem_ta": "சரத்து 344-ன் கீழ் அதிகாரப்பூர்வ மொழி ஆணையம் தனது அறிக்கையை யாரிடம் சமர்ப்பிக்கிறது, மேலும் அவ்வறிக்கையை ஆய்வு செய்வது யார்?",
            "options": [
                ("Submits to the President; examined by the 30-member Parliamentary Committee", "குடியரசுத் தலைவரிடம் சமர்ப்பிக்கிறது; 30 உறுப்பினர்களைக் கொண்ட நாடாளுமன்றக் குழு ஆய்வு செய்கிறது"),
                ("Submits to the Chief Justice of India; examined by the Law Commission", "தலைமை நீதிபதியிடம் சமர்ப்பிக்கிறது; சட்ட ஆணையம் ஆய்வு செய்கிறது"),
                ("Submits to the Speaker of Lok Sabha; examined by the Estimates Committee", "மக்களவைத் தலைவரிடம் சமர்ப்பிக்கிறது; மதிப்பீட்டுக் குழு ஆய்வு செய்கிறது"),
                ("Submits to the Prime Minister; examined by NITI Aayog", "பிரதமரிடம் சமர்ப்பிக்கிறது; நிதி ஆயோக் ஆய்வு செய்கிறது")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 344, the Commission submits its recommendations to the President. The President causes the report to be examined by the Committee of Parliament on Official Language (Article 344(4)-(5)), which then reports its opinion to the President.",
            "exp_ta": "சரத்து 344-ன் கீழ், ஆணையம் தனது பரிந்துரைகளைக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கிறது. குடியரசுத் தலைவர் அவ்வறிக்கையை அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழுவின் (சரத்து 344(4)-(5)) ஆய்வுக்கு உட்படுத்துகிறார், அக்குழு தனது கருத்தைக் குடியரசுத் தலைவருக்குத் தெரிவிக்கிறது.",
            "why_a_en": "The constitutional procedure is: Commission -> President -> Parliamentary Committee -> President.",
            "why_a_ta": "அரசியலமைப்பு நடைமுறை: ஆணையம் -> குடியரசுத் தலைவர் -> நாடாளுமன்றக் குழு -> குடியரசுத் தலைவர்.",
            "why_b_en": "The Chief Justice and Law Commission have no role in this process.",
            "why_b_ta": "தலைமை நீதிபதி மற்றும் சட்ட ஆணையத்திற்கு இதில் எந்தப் பங்கும் இல்லை.",
            "why_c_en": "The Estimates Committee examines budget estimates, not language policy.",
            "why_c_ta": "மதிப்பீட்டுக் குழு வரவுசெலவுத் திட்ட மதிப்பீடுகளை ஆய்வு செய்கிறது, மொழிக் கொள்கையை அல்ல.",
            "why_d_en": "NITI Aayog has no constitutional role in language governance.",
            "why_d_ta": "மொழி நிர்வாகத்தில் நிதி ஆயோக்கிற்கு அரசியலமைப்பு ரீதியான பங்கு இல்லை.",
            "tip_en": "Article 344 Flow: Commission (experts) recommends -> Committee (MPs) reviews -> President issues directions.",
            "tip_ta": "சரத்து 344 படிநிலை: ஆணையம் (நிபுணர்கள்) பரிந்துரைக்கிறது -> குழு (எம்.பி.க்கள்) ஆய்வு செய்கிறது -> குடியரசுத் தலைவர் வழிகாட்டுகிறார்.",
            "fact_en": "Presidential orders under Article 344(6) can only be issued after considering the Parliamentary Committee's report.",
            "fact_ta": "நாடாளுமன்றக் குழுவின் அறிக்கையைப் பரிசீலித்த பிறகே சரத்து 344(6)-ன் கீழ் குடியரசுத் தலைவர் ஆணைகளைப் பிறப்பிக்க முடியும்."
        },
        # 35
        {
            "subtopic": "Article 347 Criteria for Minority Languages",
            "stem_en": "Under Article 347, what condition must be satisfied before the President directs that a minority language be officially recognized in a State?",
            "stem_ta": "சரத்து 347-ன் கீழ், ஒரு மாநிலத்தில் சிறுபான்மையினர் மொழியை அதிகாரப்பூர்வமாக அங்கீகரிக்க குடியரசுத் தலைவர் உத்தரவிடுவதற்கு முன் எந்த நிபந்தனை பூர்த்தி செய்யப்பட வேண்டும்?",
            "options": [
                ("A demand must be made, and the President must be satisfied that a substantial proportion of the population desire its use", "ஒரு கோரிக்கை விடுக்கப்பட வேண்டும், மற்றும் மக்கட்தொகையில் கணிசமான பகுதியினர் அதன் பயன்பாட்டை விரும்புகின்றனர் என்பதில் குடியரசுத் தலைவர் திருப்தியடைய வேண்டும்"),
                ("The Governor of the State must unanimously approve the measure", "மாநில ஆளுநர் ஒருமனதாக இம்முடிவுக்கு ஒப்புதல் அளிக்க வேண்டும்"),
                ("All members of the State Assembly must sign a joint memorandum", "மாநில சட்டமன்றத்தின் அனைத்து உறுப்பினர்களும் ஒரு கூட்டு மனுவில் கையொப்பமிட வேண்டும்"),
                ("The language must have at least 500 published classical books", "அம்மொழியில் குறைந்தபட்சம் 500 வெளியிடப்பட்ட செவ்வியல் நூல்கள் இருக்க வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 347 states: 'On a demand being made in that behalf the President may, if he is satisfied that a substantial proportion of the population of a State desire the use of any language spoken by them, direct that such language shall also be officially recognized...'",
            "exp_ta": "சரத்து 347 கூறுகிறது: 'அது தொடர்பாகக் கோரிக்கை விடுக்கப்படும்போது, ஒரு மாநிலத்தின் மக்கட்தொகையில் கணிசமான பகுதியினர் தாங்கள் பேசும் மொழியைப் பயன்படுத்த விரும்புகின்றனர் என்பதில் குடியரசுத் தலைவர் திருப்தியடைந்தால், அந்த மொழியும் அதிகாரப்பூர்வமாக அங்கீகரிக்கப்பட வேண்டும் என்று உத்தரவிடலாம்...'",
            "why_a_en": "Article 347 expressly requires: 1) Demand being made, and 2) President's satisfaction of substantial proportion.",
            "why_a_ta": "சரத்து 347 வெளிப்படையாகக் கோருவது: 1) கோரிக்கை விடுக்கப்படுவது, மற்றும் 2) கணிசமான பகுதியினர் என்ற குடியரசுத் தலைவரின் திருப்தி.",
            "why_b_en": "The Governor's unanimous approval is not required; this is an independent Presidential power.",
            "why_b_ta": "ஆளுநரின் ஒருமனதான ஒப்புதல் தேவையில்லை; இது ஒரு சுயாதீனமான குடியரசுத் தலைவர் அதிகாரமாகும்.",
            "why_c_en": "State Assembly signatures are not mandated.",
            "why_c_ta": "மாநில சட்டமன்ற உறுப்பினர்களின் கையொப்பங்கள் கட்டாயமில்லை.",
            "why_d_en": "Literary book counts are not a constitutional condition under Article 347.",
            "why_d_ta": "இலக்கிய நூல்களின் எண்ணிக்கை சரத்து 347-ன் கீழான அரசியலமைப்பு நிபந்தனை அல்ல.",
            "tip_en": "Article 347 Keywords: 'On demand' + 'Substantial proportion desires' -> President directs official recognition.",
            "tip_ta": "சரத்து 347 முக்கியச் சொற்கள்: 'கோரிக்கையின் பேரில்' + 'கணிசமான பகுதியினர் விரும்புவது' -> குடியரசுத் தலைவர் அங்கீகார உத்தரவு.",
            "fact_en": "This provision was used to support Urdu in Bihar and UP, and Bengali in Tripura and Assam (Cachar).",
            "fact_ta": "பீகார், உ.பியில் உருதுவிற்கும், திரிபுரா மற்றும் அசாமில் பெங்காலிக்கும் ஆதரவளிக்க இவ்விதி பயன்படுத்தப்பட்டது."
        },
        # 36
        {
            "subtopic": "Languages of Eighth Schedule - Classical Status Overlap",
            "stem_en": "Which of the following Classical Languages is NOT listed in the Eighth Schedule of the Constitution of India?",
            "stem_ta": "பின்வரும் செம்மொழிகளில் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் பட்டியலிடப்படாத மொழி எது?",
            "options": [
                ("Pali", "பாலி"),
                ("Tamil", "தமிழ்"),
                ("Sanskrit", "சமஸ்கிருதம்"),
                ("Odia", "ஒடியா")
            ],
            "correct_key": "A",
            "exp_en": "Pali and Prakrit (granted Classical Language status in October 2024) are NOT listed in the Eighth Schedule of the Constitution of India. All original six classical languages (Tamil, Sanskrit, Telugu, Kannada, Malayalam, Odia) and Assamese, Bengali, Marathi are in the 8th Schedule.",
            "exp_ta": "பாலி மற்றும் பிராகிருதம் (அக்டோபர் 2024-ல் செம்மொழி அந்தஸ்து வழங்கப்பட்டது) இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் பட்டியலிடப்படவில்லை. முதல் ஆறு செம்மொழிகள் மற்றும் அசாமி, பெங்காலி, மராத்தி ஆகியவை 8-வது அட்டவணையில் உள்ளன.",
            "why_a_en": "Pali is a classical language recognized for its ancient Buddhist canon, but absent from the 8th Schedule.",
            "why_a_ta": "பாலி பௌத்த இலக்கியங்களுக்காக அங்கீகரிக்கப்பட்ட செம்மொழி, ஆனால் 8-வது அட்டவணையில் இல்லை.",
            "why_b_en": "Tamil is in the Eighth Schedule.",
            "why_b_ta": "தமிழ் எட்டாவது அட்டவணையில் உள்ளது.",
            "why_c_en": "Sanskrit is in the Eighth Schedule.",
            "why_c_ta": "சமஸ்கிருதம் எட்டாவது அட்டவணையில் உள்ளது.",
            "why_d_en": "Odia is in the Eighth Schedule.",
            "why_d_ta": "ஒடியா எட்டாவது அட்டவணையில் உள்ளது.",
            "tip_en": "Crucial TNPSC Distinction: Classical Languages NOT in 8th Schedule = PALI and PRAKRIT.",
            "tip_ta": "முக்கிய டிஎன்பிஎஸ்சி வேறுபாடு: 8-வது அட்டவணையில் இல்லாத செம்மொழிகள் = பாலி மற்றும் பிராகிருதம்.",
            "fact_en": "There are now 11 Classical Languages, of which 9 are in the Eighth Schedule and 2 are not.",
            "fact_ta": "தற்போது 11 செம்மொழிகள் உள்ளன, அவற்றில் 9 மொழிகள் எட்டாவது அட்டவணையில் உள்ளன, 2 மொழிகள் இல்லை."
        },
        # 37
        {
            "subtopic": "Munshi-Ayyangar Formula Concept",
            "stem_en": "What was the core compromise embodied in the famous 'Munshi-Ayyangar Formula' adopted by the Constituent Assembly in September 1949?",
            "stem_ta": "1949 செப்டம்பரில் அரசியல் நிர்ணய சபையால் ஏற்றுக்கொள்ளப்பட்ட புகழ்பெற்ற 'முன்ஷி-அய்யங்கார் சூத்திரத்தில்' பொதிந்துள்ள முக்கிய சமரசம் என்ன?",
            "options": [
                ("Hindi in Devanagari script would be the official language of the Union, but English would continue for 15 years and international numerals would be used", "தேவநாகரி வரிவடிவ இந்தி ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியாக இருக்கும், ஆனால் ஆங்கிலம் 15 ஆண்டுகளுக்குத் தொடரும் மற்றும் பன்னாட்டு எண்கள் பயன்படுத்தப்படும்"),
                ("Sanskrit would be made the sole national language immediately", "சமஸ்கிருதம் உடனடியாக ஒரே தேசிய மொழியாக ஆக்கப்படும்"),
                ("English would be completely banned from January 26, 1950", "1950 ஜனவரி 26 முதல் ஆங்கிலம் முழுமையாகத் தடை செய்யப்படும்"),
                ("All 14 regional languages would be declared Union official languages concurrently", "அனைத்து 14 வட்டார மொழிகளும் ஒரே நேரத்தில் ஒன்றிய அதிகாரப்பூர்வ மொழிகளாக அறிவிக்கப்படும்")
            ],
            "correct_key": "A",
            "exp_en": "Drafted by K.M. Munshi and N. Gopalaswami Ayyangar, the formula reached a delicate compromise: Hindi was named official (not national) language, international numerals were adopted, and English was granted a 15-year continuation with parliamentary power to extend.",
            "exp_ta": "கே.எம். முன்ஷி மற்றும் என். கோபாலசுவாமி அய்யங்காரால் வரையப்பட்ட இச்சூத்திரம் ஒரு நுட்பமான சமரசத்தை எட்டியது: இந்தி அதிகாரப்பூர்வ மொழியாக (தேசிய மொழி அல்ல) அறிவிக்கப்பட்டது, பன்னாட்டு எண்கள் ஏற்றுக்கொள்ளப்பட்டன, மேலும் ஆங்கிலத்திற்கு 15 ஆண்டுகால நீட்டிப்பும், அதை நீட்டிக்க நாடாளுமன்றத்திற்கு அதிகாரமும் வழங்கப்பட்டது.",
            "why_a_en": "The Munshi-Ayyangar Formula is the foundational compromise of Part XVII of the Constitution.",
            "why_a_ta": "முன்ஷி-அய்யங்கார் சூத்திரம் என்பது அரசியலமைப்பின் பகுதி XVII-ன் அடிப்படைக் சமரசமாகும்.",
            "why_b_en": "Sanskrit was not adopted as national language.",
            "why_b_ta": "சமஸ்கிருதம் தேசிய மொழியாக ஏற்றுக்கொள்ளப்படவில்லை.",
            "why_c_en": "English was not banned; it was preserved for 15 years.",
            "why_c_ta": "ஆங்கிலம் தடை செய்யப்படவில்லை; அது 15 ஆண்டுகளுக்குப் பாதுகாக்கப்பட்டது.",
            "why_d_en": "All 14 were placed in the Eighth Schedule, not made Union official languages.",
            "why_d_ta": "14 மொழிகளும் எட்டாவது அட்டவணையில் வைக்கப்பட்டன, ஒன்றிய அதிகாரப்பூர்வ மொழிகளாக்கப்படவில்லை.",
            "tip_en": "Munshi-Ayyangar Formula: Hindi (Union Language) + English (15 yrs transition) + International Numerals.",
            "tip_ta": "முன்ஷி-அய்யங்கார் சூத்திரம்: இந்தி (ஒன்றிய மொழி) + ஆங்கிலம் (15 ஆண்டு இடைக்காலம்) + பன்னாட்டு எண்கள்.",
            "fact_en": "It was adopted on September 14, 1949, which is why September 14 is celebrated as 'Hindi Diwas'.",
            "fact_ta": "இது 1949 செப்டம்பர் 14 அன்று ஏற்றுக்கொள்ளப்பட்டது, அதனால்தான் செப்டம்பர் 14 'இந்தி தினம்' எனக் கொண்டாடப்படுகிறது."
        },
        # 38
        {
            "subtopic": "Special Officer for Linguistic Minorities Headquarters",
            "stem_en": "Where is the permanent headquarters of the Commissioner for Linguistic Minorities located?",
            "stem_ta": "மொழிச் சிறுபான்மையினருக்கான ஆணையரின் நிரந்தரத் தலைமையகம் எங்கு அமைந்துள்ளது?",
            "options": [
                ("Prayagraj (Allahabad), Uttar Pradesh", "பிரயாக்ராஜ் (அலகாபாத்), உத்தரப் பிரதேசம்"),
                ("New Delhi", "புது தில்லி"),
                ("Chennai, Tamil Nadu", "சென்னை, தமிழ்நாடு"),
                ("Kolkata, West Bengal", "கொல்கத்தா, மேற்கு வங்காளம்")
            ],
            "correct_key": "A",
            "exp_en": "In accordance with the 7th Constitutional Amendment Act, 1956, the office of the Commissioner for Linguistic Minorities was established in 1957 with its permanent headquarters at Prayagraj (Allahabad), Uttar Pradesh.",
            "exp_ta": "1956-ன் 7-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின்படி, மொழிச் சிறுபான்மையினருக்கான ஆணையர் அலுவலகம் 1957-ல் உத்தரப் பிரதேசத்தின் பிரயாக்ராஜில் (அலகாபாத்) தனது நிரந்தரத் தலைமையகத்துடன் நிறுவப்பட்டது.",
            "why_a_en": "Prayagraj has been the constitutional headquarters since its inception in 1957.",
            "why_a_ta": "பிரயாக்ராஜ் 1957-ல் தொடங்கப்பட்டதிலிருந்து அதன் அரசியலமைப்புத் தலைமையகமாக இருந்து வருகிறது.",
            "why_b_en": "New Delhi houses the Ministry of Minority Affairs, but the Commissioner's headquarters is in Prayagraj.",
            "why_b_ta": "புது தில்லியில் சிறுபான்மையினர் விவகார அமைச்சகம் உள்ளது, ஆனால் ஆணையரின் தலைமையகம் பிரயாக்ராஜில் உள்ளது.",
            "why_c_en": "Chennai is a regional office, not the headquarters.",
            "why_c_ta": "சென்னை ஒரு மண்டல அலுவலகம், தலைமையகம் அல்ல.",
            "why_d_en": "Kolkata is a regional office, not the headquarters.",
            "why_d_ta": "கொல்கத்தா ஒரு மண்டல அலுவலகம், தலைமையகம் அல்ல.",
            "tip_en": "CLM: Headquarters = PRAYAGRAJ; Regional Offices = Belgaum, Chennai, Kolkata.",
            "tip_ta": "CLM: தலைமையகம் = பிரயாக்ராஜ்; மண்டல அலுவலகங்கள் = பெல்காம், சென்னை, கொல்கத்தா.",
            "fact_en": "The Commissioner is assisted by a Deputy Commissioner and Assistant Commissioners.",
            "fact_ta": "ஆணையருக்கு ஒரு துணை ஆணையர் மற்றும் உதவி ஆணையர்கள் உதவுகிறார்கள்."
        },
        # 39
        {
            "subtopic": "Article 346 Proviso Mechanism",
            "stem_en": "If two non-Hindi States communicate with each other, what language must they use unless they mutually agree otherwise?",
            "stem_ta": "இரண்டு இந்தி பேசாத மாநிலங்கள் தங்களுக்குள் தொடர்புகொள்ளும்போது, அவை பரஸ்பரம் வேறுவிதமாக ஒப்புக்கொள்ளாத வரையில் எந்த மொழியைப் பயன்படுத்த வேண்டும்?",
            "options": [
                ("English", "ஆங்கிலம்"),
                ("Hindi in Devanagari script", "தேவநாகரி வரிவடிவ இந்தி"),
                ("The language of the recipient State exclusively", "பெறும் மாநிலத்தின் மொழியில் மட்டுமே"),
                ("Sanskrit", "சமஸ்கிருதம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 346 and Section 3 of the 1963 Act, English is the authorized language for inter-State communication between non-Hindi speaking States (e.g. Tamil Nadu and Kerala), unless both States agree to use Hindi under the proviso.",
            "exp_ta": "சரத்து 346 மற்றும் 1963 சட்டத்தின் பிரிவு 3-ன் கீழ், இந்தி பேசாத மாநிலங்களுக்கு இடையே (எ.கா. தமிழ்நாடு மற்றும் கேரளா) தொடர்புக்கான அங்கீகரிக்கப்பட்ட மொழி ஆங்கிலமாகும், இரு மாநிலங்களும் விதிவிலக்கின் கீழ் இந்தியைப் பயன்படுத்த ஒப்புக்கொண்டால் தவிர.",
            "why_a_en": "English is the default inter-State link language for non-Hindi States.",
            "why_a_ta": "இந்தி பேசாத மாநிலங்களுக்கு இடையேயான இயல்புநிலை தொடர்பு மொழி ஆங்கிலமாகும்.",
            "why_b_en": "Hindi requires voluntary mutual agreement under the proviso to Article 346.",
            "why_b_ta": "சரத்து 346-ன் விதிவிலக்கின் கீழ் இந்திக்கு பரஸ்பர தன்னார்வ உடன்படிக்கை தேவைப்படுகிறது.",
            "why_c_en": "One State cannot mandate its regional language on another State.",
            "why_c_ta": "ஒரு மாநிலம் தனது வட்டார மொழியை மற்றொரு மாநிலத்தின் மீது கட்டாயப்படுத்த முடியாது.",
            "why_d_en": "Sanskrit is not an inter-state administrative language.",
            "why_d_ta": "சமஸ்கிருதம் மாநிலங்களுக்கு இடையேயான நிர்வாக மொழி அல்ல.",
            "tip_en": "Inter-State Default = ENGLISH; Hindi requires mutual agreement (Art 346 Proviso).",
            "tip_ta": "மாநிலங்களுக்கிடையேயான இயல்புநிலை = ஆங்கிலம்; இந்திக்கு பரஸ்பர ஒப்பந்தம் தேவை (சரத்து 346 விதிவிலக்கு).",
            "fact_en": "Between a Hindi state and a non-Hindi state, communications from Hindi state must be accompanied by English translation.",
            "fact_ta": "இந்தி மாநிலத்திற்கும் இந்தி பேசாத மாநிலத்திற்கும் இடையில், இந்தி மாநிலத்திலிருந்து வரும் கடிதங்களுடன் ஆங்கில மொழிபெயர்ப்பு இணைக்கப்பட வேண்டும்."
        },
        # 40
        {
            "subtopic": "Official Language Act Section 3(5) Text",
            "stem_en": "Under Section 3(5) of the Official Languages Act, 1963, whose consent is required before English can be discontinued for official purposes of the Union?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம், 1963-ன் பிரிவு 3(5)-ன் கீழ், ஒன்றியத்தின் அதிகாரப்பூர்வ பணிகளிலிருந்து ஆங்கிலத்தை நிறுத்துவதற்கு முன் யாருடைய ஒப்புதல் தேவை?",
            "options": [
                ("Resolutions passed by the Legislatures of all non-Hindi States AND by each House of Parliament", "அனைத்து இந்தி பேசாத மாநிலங்களின் சட்டமன்றங்கள் மற்றும் நாடாளுமன்றத்தின் இரு அவைகளும் நிறைவேற்றும் தீர்மானங்கள்"),
                ("Only a simple majority resolution in Lok Sabha", "மக்களவையில் ஒரு எளிய பெரும்பான்மைத் தீர்மானம் மட்டுமே"),
                ("An executive notification issued by the Prime Minister", "பிரதமரால் வெளியிடப்படும் நிர்வாக அறிவிக்கை"),
                ("A unanimous judgment of the Supreme Court Constitution Bench", "உச்ச நீதிமன்ற அரசியல் சாசன அமர்வின் ஒருமனதான தீர்ப்பு")
            ],
            "correct_key": "A",
            "exp_en": "Section 3(5) provides that English shall not cease to be used until resolutions for its discontinuance have been passed by the Legislatures of all the States which have not adopted Hindi as their official language and until a resolution has been passed by each House of Parliament.",
            "exp_ta": "பிரிவு 3(5)-ன் படி, இந்தியைத் தங்கள் அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொள்ளாத அனைத்து மாநிலங்களின் சட்டமன்றங்களும் தீர்மானம் நிறைவேற்றும் வரையிலும், நாடாளுமன்றத்தின் இரு அவைகளிலும் தீர்மானம் நிறைவேற்றப்படும் வரையிலும் ஆங்கிலத்தின் பயன்பாடு நிறுத்தப்பட மாட்டாது.",
            "why_a_en": "This is the famous double-lock guarantee: All non-Hindi State Assemblies + Both Houses of Parliament.",
            "why_a_ta": "இது புகழ்பெற்ற இரட்டைப் பூட்டு உத்தரவாதம்: அனைத்து இந்தி பேசாத மாநில சட்டமன்றங்கள் + நாடாளுமன்றத்தின் இரு அவைகள்.",
            "why_b_en": "Lok Sabha cannot unilaterally abolish English under Section 3(5).",
            "why_b_ta": "பிரிவு 3(5)-ன் கீழ் மக்களவை தன்னிச்சையாக ஆங்கிலத்தை ரத்து செய்ய முடியாது.",
            "why_c_en": "Executive notifications cannot override Section 3(5).",
            "why_c_ta": "நிர்வாக அறிவிக்கைகள் பிரிவு 3(5)-ஐ மீற முடியாது.",
            "why_d_en": "The Supreme Court interprets the law, but does not grant legislative discontinuance consent.",
            "why_d_ta": "உச்ச நீதிமன்றம் சட்டத்தை விளக்குகிறது, ஆனால் சட்டப்பூர்வ முடிவுக்கு ஒப்புதல் அளிப்பதில்லை.",
            "tip_en": "Statutory Non-Hindi Lock: Even if 1 non-Hindi State (e.g. Tamil Nadu) objects, English CANNOT be discontinued.",
            "tip_ta": "சட்டப்பூர்வ இந்தி அல்லாத பூட்டு: ஒரே ஒரு இந்தி பேசாத மாநிலம் (எ.கா. தமிழ்நாடு) எதிர்த்தாலும், ஆங்கிலத்தை நிறுத்த முடியாது.",
            "fact_en": "This statutory lock was introduced by the 1967 Amendment Act under Prime Minister Indira Gandhi.",
            "fact_ta": "பிரதமர் இந்திரா காந்தியின் கீழ் 1967 திருத்தச் சட்டத்தால் இந்த சட்டப்பூர்வ பூட்டு அறிமுகப்படுத்தப்பட்டது."
        },
        # 41
        {
            "subtopic": "Languages of Eighth Schedule - Classical Groupings",
            "stem_en": "Which Dravidian languages have been accorded Classical Language status by the Government of India?",
            "stem_ta": "இந்திய அரசால் செம்மொழி அந்தஸ்து வழங்கப்பட்டுள்ள திராவிட மொழிகள் எவை?",
            "options": [
                ("Tamil, Telugu, Kannada, and Malayalam", "தமிழ், தெலுங்கு, கன்னடம் மற்றும் மலையாளம்"),
                ("Tamil and Telugu only", "தமிழ் மற்றும் தெலுங்கு மட்டுமே"),
                ("Tamil and Kannada only", "தமிழ் மற்றும் கன்னடம் மட்டுமே"),
                ("All South Indian languages including Tulu and Badaga", "துளு மற்றும் படகா உள்ளிட்ட அனைத்து தென்னிந்திய மொழிகளும்")
            ],
            "correct_key": "A",
            "exp_en": "All four major literary Dravidian languages have been declared Classical Languages: Tamil (2004), Telugu (2008), Kannada (2008), and Malayalam (2013).",
            "exp_ta": "நான்கு முக்கிய இலக்கியத் திராவிட மொழிகளுக்கும் செம்மொழி அந்தஸ்து வழங்கப்பட்டுள்ளது: தமிழ் (2004), தெலுங்கு (2008), கன்னடம் (2008) மற்றும் மலையாளம் (2013).",
            "why_a_en": "These four major literary Dravidian languages all hold classical status.",
            "why_a_ta": "இந்த நான்கு முக்கிய இலக்கியத் திராவிட மொழிகளும் செம்மொழி அந்தஸ்தைப் பெற்றுள்ளன.",
            "why_b_en": "Kannada and Malayalam are also classical languages.",
            "why_b_ta": "கன்னடமும் மலையாளமும் கூட செம்மொழிகளாகும்.",
            "why_c_en": "Telugu and Malayalam are also classical languages.",
            "why_c_ta": "தெலுங்கும் மலையாளமும் கூட செம்மொழிகளாகும்.",
            "why_d_en": "Tulu and Badaga have not been granted classical language status.",
            "why_d_ta": "துளு மற்றும் படகா மொழிகளுக்குச் செம்மொழி அந்தஸ்து வழங்கப்படவில்லை.",
            "tip_en": "All 4 major literary Dravidian languages = CLASSICAL (Tamil 2004, Kannada & Telugu 2008, Malayalam 2013).",
            "tip_ta": "4 முக்கிய திராவிட மொழிகளும் = செம்மொழிகள் (தமிழ் 2004, கன்னடம் & தெலுங்கு 2008, மலையாளம் 2013).",
            "fact_en": "Tamil was the very first classical language recognized in India in 2004.",
            "fact_ta": "2004-ல் இந்தியாவில் அங்கீகரிக்கப்பட்ட முதல் செம்மொழி தமிழ் ஆகும்."
        },
        # 42
        {
            "subtopic": "Article 351 Vocabulary Guidance",
            "stem_en": "In enriching Hindi under Article 351, which languages are designated as the secondary source of vocabulary?",
            "stem_ta": "சரத்து 351-ன் கீழ் இந்தியைச் செறிவூட்டுவதில், சொல்லகராதிக்கான இரண்டாம் நிலை ஆதாரமாக எந்த மொழிகள் குறிப்பிடப்பட்டுள்ளன?",
            "options": [
                ("The languages specified in the Eighth Schedule", "எட்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள மொழிகள்"),
                ("Foreign European languages", "ஐரோப்பிய வெளிநாட்டு மொழிகள்"),
                ("Only classical Persian and Arabic", "செவ்வியல் பாரசீகம் மற்றும் அரபு மட்டுமே"),
                ("Tribal dialects exclusively", "பழங்குடியின வட்டார வழக்குகள் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Article 351 directs that Hindi should draw its vocabulary primarily on Sanskrit and secondarily on 'the other languages of India specified in the Eighth Schedule'.",
            "exp_ta": "சரத்து 351 இந்தி தனது சொல்லகராதியை முதன்மையாக சமஸ்கிருதத்திலிருந்தும், இரண்டாவதாக 'எட்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள இந்தியாவின் பிற மொழிகளிலிருந்தும்' பெற வேண்டும் என்று வழிகாட்டுகிறது.",
            "why_a_en": "Article 351 expressly cites the languages of the Eighth Schedule as the secondary source.",
            "why_a_ta": "சரத்து 351 எட்டாவது அட்டவணை மொழிகளை இரண்டாம் நிலை ஆதாரமாக வெளிப்படையாகக் குறிப்பிடுகிறது.",
            "why_b_en": "Foreign languages are not promoted in Article 351.",
            "why_b_ta": "சரத்து 351-ல் வெளிநாட்டு மொழிகள் ஊக்குவிக்கப்படவில்லை.",
            "why_c_en": "Persian and Arabic are not designated as constitutional sources under Article 351.",
            "why_c_ta": "சரத்து 351-ன் கீழ் பாரசீகமும் அரபும் அரசியலமைப்பு ஆதாரங்களாக நியமிக்கப்படவில்லை.",
            "why_d_en": "Tribal dialects are not specified in Article 351.",
            "why_d_ta": "பழங்குடியின வழக்குகள் சரத்து 351-ல் குறிப்பிடப்படவில்லை.",
            "tip_en": "Article 351: Primary = Sanskrit; Secondary = Eighth Schedule Languages.",
            "tip_ta": "சரத்து 351: முதன்மை = சமஸ்கிருதம்; இரண்டாம் நிலை = எட்டாவது அட்டவணை மொழிகள்.",
            "fact_en": "This was intended to assimilate words from Tamil, Telugu, Bengali, Marathi into standard Hindi.",
            "fact_ta": "தமிழ், தெலுங்கு, பெங்காலி, மராத்தி போன்ற மொழிகளிலிருந்து சொற்களைத் தரப்படுத்தப்பட்ட இந்தியில் இணைப்பதே இதன் நோக்கமாகும்."
        },
        # 43
        {
            "subtopic": "Languages of Eighth Schedule - Total Count Progression",
            "stem_en": "What was the chronological sequence of total language counts in the Eighth Schedule of the Constitution?",
            "stem_ta": "அரசியலமைப்பின் எட்டாவது அட்டவணையில் உள்ள மொத்த மொழிகளின் எண்ணிக்கையின் காலவரிசை என்ன?",
            "options": [
                ("14 (1950) -> 15 (1967) -> 18 (1992) -> 22 (2003)", "14 (1950) -> 15 (1967) -> 18 (1992) -> 22 (2003)"),
                ("10 (1950) -> 14 (1967) -> 18 (1992) -> 22 (2003)", "10 (1950) -> 14 (1967) -> 18 (1992) -> 22 (2003)"),
                ("14 (1950) -> 16 (1967) -> 20 (1992) -> 22 (2003)", "14 (1950) -> 16 (1967) -> 20 (1992) -> 22 (2003)"),
                ("14 (1950) -> 15 (1967) -> 19 (1992) -> 22 (2003)", "14 (1950) -> 15 (1967) -> 19 (1992) -> 22 (2003)")
            ],
            "correct_key": "A",
            "exp_en": "The sequence is: 14 original (1950) -> 15 with Sindhi (21st CAA, 1967) -> 18 with Konkani, Manipuri, Nepali (71st CAA, 1992) -> 22 with Bodo, Dogri, Maithili, Santhali (92nd CAA, 2003).",
            "exp_ta": "சரியான காலவரிசை: தொடக்கத்தில் 14 (1950) -> சிந்தியுடன் 15 (21-வது திருத்தம், 1967) -> கொங்கணி, மணிப்பூரி, நேபாளியுடன் 18 (71-வது திருத்தம், 1992) -> போடோ, டோக்ரி, மைதிலி, சந்தாலியுடன் 22 (92-வது திருத்தம், 2003).",
            "why_a_en": "14 -> 15 -> 18 -> 22 is the exact historical constitutional sequence.",
            "why_a_ta": "14 -> 15 -> 18 -> 22 என்பது துல்லியமான வரலாற்று அரசியலமைப்பு வரிசையாகும்.",
            "why_b_en": "The starting count was 14, not 10.",
            "why_b_ta": "தொடக்க எண்ணிக்கை 14, 10 அல்ல.",
            "why_c_en": "1967 added only 1 language (Sindhi), making it 15, not 16.",
            "why_c_ta": "1967-ல் 1 மொழி மட்டுமே சேர்க்கப்பட்டது, 16 அல்ல.",
            "why_d_en": "1992 added 3 languages, making it 18, not 19.",
            "why_d_ta": "1992-ல் 3 மொழிகள் சேர்க்கப்பட்டு 18 ஆனது, 19 அல்ல.",
            "tip_en": "Eighth Schedule additions: +1 (21st CAA) -> +3 (71st CAA) -> +4 (92nd CAA). Total = 22.",
            "tip_ta": "8-வது அட்டவணைச் சேர்க்கைகள்: +1 (21-வது திருத்தம்) -> +3 (71-வது திருத்தம்) -> +4 (92-வது திருத்தம்). மொத்தம் = 22.",
            "fact_en": "The 96th CAA in 2011 altered the spelling of Oriya to Odia without changing the total count.",
            "fact_ta": "2011-ன் 96-வது திருத்தம் எண்ணிக்கையை மாற்றாமல் ஒரியாவின் எழுத்துக்கூட்டலை ஒடியா என மாற்றியது."
        },
        # 44
        {
            "subtopic": "Article 348 Authoritative Texts Scope",
            "stem_en": "Under Article 348(1)(b), which of the following instruments does NOT fall within the mandatory requirement of having an authoritative English text?",
            "stem_ta": "சரத்து 348(1)(b)-ன் கீழ், அதிகாரப்பூர்வ ஆங்கில மூல வாசகத்தைக் கொண்டிருக்க வேண்டும் என்ற கட்டாயத் தேவையின் கீழ் வராதது எது?",
            "options": [
                ("Informal inter-departmental telephone conversations", "துறைகளுக்கு இடையேயான முறைசாரா தொலைபேசி உரையாடல்கள்"),
                ("All Bills introduced in Parliament", "நாடாளுமன்றத்தில் அறிமுகப்படுத்தப்படும் அனைத்து மசோதாக்கள்"),
                ("All Acts passed by Parliament or State Legislatures", "நாடாளுமன்றம் அல்லது மாநில சட்டமன்றங்களால் நிறைவேற்றப்படும் அனைத்துச் சட்டங்கள்"),
                ("All Ordinances promulgated by the President or Governors", "குடியரசுத் தலைவர் அல்லது ஆளுநர்களால் பிறப்பிக்கப்படும் அனைத்து அவசரச் சட்டங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 348(1)(b) applies strictly to formal legal instruments: Bills, Acts, Ordinances, Orders, Rules, Regulations, and Bye-laws. Informal oral telephone communications are completely outside its scope.",
            "exp_ta": "சரத்து 348(1)(b) முறையான சட்ட ஆவணங்களுக்கு மட்டுமே பொருந்தும்: மசோதாக்கள், சட்டங்கள், அவசரச் சட்டங்கள், ஆணைகள், விதிகள், ஒழுங்குமுறைகள் மற்றும் துணை விதிகள். முறைசாரா வாய்மொழி உரையாடல்கள் இதன் வரம்பிற்கு அப்பாற்பட்டவை.",
            "why_a_en": "Oral informal communications are not legislative instruments under Article 348(1)(b).",
            "why_a_ta": "வாய்மொழி முறைசாரா உரையாடல்கள் சரத்து 348(1)(b)-ன் கீழான சட்டமியற்றும் ஆவணங்கள் அல்ல.",
            "why_b_en": "Bills are explicitly enumerated in Article 348(1)(b)(i).",
            "why_b_ta": "மசோதாக்கள் சரத்து 348(1)(b)(i)-ல் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளன.",
            "why_c_en": "Acts are explicitly enumerated in Article 348(1)(b)(ii).",
            "why_c_ta": "சட்டங்கள் சரத்து 348(1)(b)(ii)-ல் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளன.",
            "why_d_en": "Ordinances are explicitly enumerated in Article 348(1)(b)(iii).",
            "why_d_ta": "அவசரச் சட்டங்கள் சரத்து 348(1)(b)(iii)-ல் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளன.",
            "tip_en": "Article 348(1)(b) covers: Bills, Acts, Ordinances, Orders, Rules, Regulations, Bye-laws.",
            "tip_ta": "சரத்து 348(1)(b) உள்ளடக்குபவை: மசோதாக்கள், சட்டங்கள், அவசரச் சட்டங்கள், ஆணைகள், விதிகள், ஒழுங்குமுறைகள்.",
            "fact_en": "This requirement ensures legal certainty and uniform interpretation across High Courts and the Supreme Court.",
            "fact_ta": "இத்தேவை உயர் நீதிமன்றங்கள் மற்றும் உச்ச நீதிமன்றத்தில் சட்டப்பூர்வ உறுதிப்பாடு மற்றும் சீரான விளக்கத்தை உறுதி செய்கிறது."
        },
        # 45
        {
            "subtopic": "Languages of Goa",
            "stem_en": "Under the Goa, Daman and Diu Official Language Act, 1987, which language was declared as the sole official language of the State of Goa?",
            "stem_ta": "கோவா, டாமன் மற்றும் டையூ அதிகாரப்பூர்வ மொழிச் சட்டம் 1987-ன் கீழ், கோவா மாநிலத்தின் ஒரே அதிகாரப்பூர்வ மொழியாக அறிவிக்கப்பட்ட மொழி எது?",
            "options": [
                ("Konkani in Devanagari script", "தேவநாகரி வரிவடிவத்திலான கொங்கணி"),
                ("Marathi in Devanagari script", "தேவநாகரி வரிவடிவத்திலான மராத்தி"),
                ("Portuguese", "போர்த்துகீசியம்"),
                ("English exclusively", "ஆங்கிலம் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "The Goa, Daman and Diu Official Language Act, 1987 declared Konkani in Devanagari script as the sole official language of Goa, while providing that Marathi could also be used for all or any official purposes.",
            "exp_ta": "கோவா, டாமன் மற்றும் டையூ அதிகாரப்பூர்வ மொழிச் சட்டம் 1987 தேவநாகரி வரிவடிவத்திலான கொங்கணியை கோவாவின் ஒரே அதிகாரப்பூர்வ மொழியாக அறிவித்தது, அதே நேரத்தில் மராத்தியும் அதிகாரப்பூர்வ பணிகளுக்குப் பயன்படுத்தப்படலாம் என வகை செய்தது.",
            "why_a_en": "Konkani in Devanagari script is the sole official language of Goa under the 1987 Act.",
            "why_a_ta": "1987 சட்டத்தின் கீழ் தேவநாகரி வரிவடிவத்திலான கொங்கணி கோவாவின் அதிகாரப்பூர்வ மொழியாகும்.",
            "why_b_en": "Marathi has associate status in Goa, but is not the primary official language.",
            "why_b_ta": "மராத்திக்கு கோவாவில் கூடுதல் அந்தஸ்து உண்டு, ஆனால் முதன்மை அதிகாரப்பூர்வ மொழி அல்ல.",
            "why_c_en": "Portuguese ceased to be the official language after liberation in 1961.",
            "why_c_ta": "1961 விடுதலைக்குப் பிறகு போர்த்துகீசியம் அதிகாரப்பூர்வ மொழியாக நீடிக்கவில்லை.",
            "why_d_en": "English is used for administrative continuity, but Konkani is the designated official language.",
            "why_d_ta": "நிர்வாகத் தொடர்ச்சிக்கு ஆங்கிலம் பயன்படுகிறது, ஆனால் கொங்கணியே அதிகாரப்பூர்வ மொழியாகும்.",
            "tip_en": "Goa Official Language = Konkani (Devanagari script); Marathi has associate use rights.",
            "tip_ta": "கோவா அதிகாரப்பூர்வ மொழி = கொங்கணி (தேவநாகரி வரிவடிவம்); மராத்திக்குக் கூடுதல் பயன்பாட்டு உரிமை உண்டு.",
            "fact_en": "Konkani was later added to the Eighth Schedule by the 71st CAA in 1992.",
            "fact_ta": "கொங்கணி பின்னர் 1992-ல் 71-வது திருத்தச் சட்டம் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது."
        },
        # 46
        {
            "subtopic": "Languages of Sikkim",
            "stem_en": "Which of the following is an official language of the State of Sikkim alongside English under the Sikkim Official Languages Act, 1977?",
            "stem_ta": "சிக்கிம் அதிகாரப்பூர்வ மொழிகள் சட்டம் 1977-ன் கீழ், ஆங்கிலத்துடன் இணைந்த சிக்கிம் மாநிலத்தின் அதிகாரப்பூர்வ மொழி எது?",
            "options": [
                ("Nepali, Bhutia, and Lepcha", "நேபாளி, பூட்டியா மற்றும் லெப்சா"),
                ("Hindi exclusively", "இந்தி மட்டுமே"),
                ("Tibetan and Chinese", "திபெத்தியன் மற்றும் சீனம்"),
                ("Assamese and Bengali", "அசாமி மற்றும் பெங்காலி")
            ],
            "correct_key": "A",
            "exp_en": "Under the Sikkim Official Languages Act, 1977 and subsequent amendments, Nepali, Bhutia, Lepcha, and Limboo are recognized official languages alongside English.",
            "exp_ta": "சிக்கிம் அதிகாரப்பூர்வ மொழிகள் சட்டம் 1977 மற்றும் அதன் தொடர் திருத்தங்களின் கீழ், நேபாளி, பூட்டியா, லெப்சா மற்றும் லிம்பு ஆகியவை ஆங்கிலத்துடன் இணைந்து அதிகாரப்பூர்வ மொழிகளாக அங்கீகரிக்கப்பட்டுள்ளன.",
            "why_a_en": "Nepali, Bhutia, and Lepcha represent the indigenous and predominant ethnic communities of Sikkim.",
            "why_a_ta": "நேபாளி, பூட்டியா மற்றும் லெப்சா ஆகியவை சிக்கிமின் பூர்வீக மற்றும் முதன்மை இனச் சமூகங்களைப் பிரதிநிதித்துவப்படுத்துகின்றன.",
            "why_b_en": "Hindi is not the primary state official language in Sikkim.",
            "why_b_ta": "இந்தி சிக்கிமின் முதன்மை மாநில அதிகாரப்பூர்வ மொழி அல்ல.",
            "why_c_en": "Chinese has no constitutional or official status in India.",
            "why_c_ta": "சீன மொழிக்கு இந்தியாவில் எந்த அரசியலமைப்பு அல்லது அதிகாரப்பூர்வ அந்தஸ்தும் இல்லை.",
            "why_d_en": "Assamese and Bengali belong to Assam and West Bengal respectively.",
            "why_d_ta": "அசாமி மற்றும் பெங்காலி ஆகியவை முறையே அசாம் மற்றும் மேற்கு வங்காளத்திற்குரியவை.",
            "tip_en": "Sikkim Official Languages include: Nepali, Bhutia, Lepcha, Limbu, English.",
            "tip_ta": "சிக்கிமின் அதிகாரப்பூர்வ மொழிகளில் அடங்குபவை: நேபாளி, பூட்டியா, லெப்சா, லிம்பு, ஆங்கிலம்.",
            "fact_en": "Nepali is the lingua franca spoken by over 60% of Sikkim's population.",
            "fact_ta": "நேபாளி சிக்கிமின் 60%-க்கும் அதிகமான மக்களால் பேசப்படும் பொதுத் தொடர்பு மொழியாகும்."
        },
        # 47
        {
            "subtopic": "Special Provisions for Mother Tongue Inspection",
            "stem_en": "Under the scheme of Article 350B, what is the primary constitutional function of the Special Officer for Linguistic Minorities?",
            "stem_ta": "சரத்து 350B-ன் திட்டத்தின் கீழ், மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலரின் முதன்மை அரசியலமைப்புப் பணி என்ன?",
            "options": [
                ("To investigate all matters relating to the safeguards provided for linguistic minorities under the Constitution", "அரசியலமைப்பின் கீழ் மொழிச் சிறுபான்மையினருக்காக வழங்கப்பட்டுள்ள பாதுகாப்புகள் தொடர்பான அனைத்து விஷயங்களையும் விசாரித்தல்"),
                ("To impose fines on schools that fail to teach in Hindi", "இந்தியில் கற்பிக்கத் தவறும் பள்ளிகளுக்கு அபராதம் விதித்தல்"),
                ("To conduct competitive examinations for Central services", "மத்தியப் பணிகளுக்கான போட்டித் தேர்வுகளை நடத்துதல்"),
                ("To appoint judges to the High Courts and Supreme Court", "உயர் நீதிமன்றம் மற்றும் உச்ச நீதிமன்ற நீதிபதிகளை நியமித்தல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 350B(2) clearly states: 'It shall be the duty of the Special Officer to investigate all matters relating to the safeguards provided for linguistic minorities under this Constitution and report to the President upon those matters...'",
            "exp_ta": "சரத்து 350B(2) தெளிவாகக் குறிப்பிடுகிறது: 'இந்த அரசியலமைப்பின் கீழ் மொழிச் சிறுபான்மையினருக்காக வழங்கப்பட்டுள்ள பாதுகாப்புகள் தொடர்பான அனைத்து விஷயங்களையும் விசாரிப்பதும், அந்த விஷயங்கள் குறித்து குடியரசுத் தலைவரிடம் அறிக்கை சமர்ப்பிப்பதும் சிறப்பு அலுவலரின் கடமையாகும்...'",
            "why_a_en": "Investigation and reporting on linguistic minority safeguards is the sole constitutional mandate.",
            "why_a_ta": "மொழிச் சிறுபான்மையினர் பாதுகாப்புகளை விசாரிப்பதும் அறிக்கை அளிப்பதும் மட்டுமே அரசியலமைப்பு கட்டளையாகும்.",
            "why_b_en": "The Special Officer has no penal or fine-imposing power.",
            "why_b_ta": "சிறப்பு அலுவலருக்கு தண்டனை வழங்கும் அல்லது அபராதம் விதிக்கும் அதிகாரம் இல்லை.",
            "why_c_en": "Examinations are conducted by UPSC and SSC.",
            "why_c_ta": "தேர்வுகள் UPSC மற்றும் SSC அமைப்புகளால் நடத்தப்படுகின்றன.",
            "why_d_en": "Judicial appointments are governed by Articles 124 and 217.",
            "why_d_ta": "நீதிமன்ற நியமனங்கள் சரத்துகள் 124 மற்றும் 217-ஆல் நிர்வகிக்கப்படுகின்றன.",
            "tip_en": "Article 350B: Investigate safeguards + Report to President -> Laid before Parliament & States.",
            "tip_ta": "சரத்து 350B: பாதுகாப்புகளை விசாரித்தல் + குடியரசுத் தலைவரிடம் அறிக்கை -> நாடாளுமன்றம் மற்றும் மாநிலங்களில் சமர்ப்பித்தல்.",
            "fact_en": "The Commissioner submits an annual report documenting minority grievances across all States.",
            "fact_ta": "ஆணையர் அனைத்து மாநிலங்களிலும் உள்ள சிறுபான்மையினரின் குறைகளை ஆவணப்படுத்தும் வருடாந்திர அறிக்கையை சமர்ப்பிக்கிறார்."
        },
        # 48
        {
            "subtopic": "Languages of Eighth Schedule - Unofficial Languages with Demands",
            "stem_en": "Which of the following widely-spoken languages is NOT included in the Eighth Schedule of the Constitution of India despite persistent demands?",
            "stem_ta": "தொடர்ச்சியான கோரிக்கைகள் இருந்தபோதிலும் பின்வரும் பரவலாகப் பேசப்படும் மொழிகளில் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படாத மொழி எது?",
            "options": [
                ("Bhojpuri", "போஜ்புரி"),
                ("Maithili", "மைதிலி"),
                ("Bodo", "போடோ"),
                ("Dogri", "டோக்ரி")
            ],
            "correct_key": "A",
            "exp_en": "Bhojpuri (spoken by over 50 million people in Bihar and eastern UP) is NOT included in the Eighth Schedule, whereas Maithili, Bodo, and Dogri were added in 2003 by the 92nd Constitutional Amendment Act.",
            "exp_ta": "பீகார் மற்றும் கிழக்கு உ.பியில் 5 கோடிக்கும் அதிகமான மக்களால் பேசப்படும் போஜ்புரி எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை; அதே சமயம் மைதிலி, போடோ மற்றும் டோக்ரி ஆகியவை 2003-ல் 92-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டன.",
            "why_a_en": "Bhojpuri remains one of the prominent pending demands for 8th Schedule inclusion.",
            "why_a_ta": "எட்டாவது அட்டவணைச் சேர்க்கைக்கான முக்கிய நிலுவைக் கோரிக்கைகளில் போஜ்புரி ஒன்றாகும்.",
            "why_b_en": "Maithili is an Eighth Schedule language (added by 92nd CAA).",
            "why_b_ta": "மைதிலி எட்டாவது அட்டவணை மொழி (92-வது திருத்தம் மூலம் சேர்க்கப்பட்டது).",
            "why_c_en": "Bodo is an Eighth Schedule language (92nd CAA).",
            "why_c_ta": "போடோ எட்டாவது அட்டவணை மொழி (92-வது திருத்தம்).",
            "why_d_en": "Dogri is an Eighth Schedule language (92nd CAA).",
            "why_d_ta": "டோக்ரி எட்டாவது அட்டவணை மொழி (92-வது திருத்தம்).",
            "tip_en": "Prominent languages NOT in 8th Schedule: Bhojpuri, Rajasthani, Tulu, Bhili, Gondi, Garhwali, Kumaoni.",
            "tip_ta": "8-வது அட்டவணையில் இல்லாத முக்கிய மொழிகள்: போஜ்புரி, ராஜஸ்தானி, துளு, பிலி, கோண்டி, கர்வாலி, குமாவோனி.",
            "fact_en": "There are currently 38 languages demanding inclusion in the Eighth Schedule.",
            "fact_ta": "தற்போது எட்டாவது அட்டவணையில் சேர்ப்பதற்காக 38 மொழிகள் கோரிக்கை விடுத்து வருகின்றன."
        },
        # 49
        {
            "subtopic": "Article 348(1) Non-Obstante Clause Power",
            "stem_en": "The opening words of Article 348(1) contain which constitutional formula governing the language of the Supreme Court and High Courts?",
            "stem_ta": "உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களின் மொழியை ஒழுங்குபடுத்தும் சரத்து 348(1)-ன் தொடக்க வரிகள் எந்த அரசியலமைப்பு சூத்திரத்தைக் கொண்டுள்ளன?",
            "options": [
                ("'Notwithstanding anything in the foregoing provisions of this Part, until Parliament by law otherwise provides...'", "'இப்பகுதியின் முந்தைய விதிகளில் என்ன கூறப்பட்டிருப்பினும், நாடாளுமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக வகை செய்யும் வரை...'"),
                ("'Subject to the unanimous decision of the Chief Justice of India...'", "'இந்தியத் தலைமை நீதிபதியின் ஒருமனதான முடிவுக்கு உட்பட்டு...'"),
                ("'In consultation with the Union Public Service Commission...'", "'மத்திய அரசுப் பணியாளர் தேர்வாணையத்துடன் கலந்தாலோசித்து...'"),
                ("'With the concurrence of all State Governors...'", "'அனைத்து மாநில ஆளுநர்களின் ஒப்புதலுடன்...'")
            ],
            "correct_key": "A",
            "exp_en": "Article 348(1) begins with a powerful non-obstante clause: 'Notwithstanding anything in the foregoing provisions of this Part, until Parliament by law otherwise provides— (a) all proceedings in the Supreme Court and in every High Court... shall be in the English language.'",
            "exp_ta": "சரத்து 348(1) ஒரு சக்திவாய்ந்த தடையற்ற வாசகத்துடன் (non-obstante clause) தொடங்குகிறது: 'இப்பகுதியின் முந்தைய விதிகளில் என்ன கூறப்பட்டிருப்பினும், நாடாளுமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக வகை செய்யும் வரை— (a) உச்ச நீதிமன்றம் மற்றும் ஒவ்வொரு உயர் நீதிமன்றத்தின் அனைத்து நடவடிக்கைகளும் ஆங்கில மொழியிலேயே இருக்கும்.'",
            "why_a_en": "The non-obstante clause overrides Articles 343 and 345, making English supreme in superior courts.",
            "why_a_ta": "இத்தடையற்ற வாசகம் சரத்துகள் 343 மற்றும் 345-ஐ மேலோங்கி, உயர் நீதிமன்றங்கள் மற்றும் உச்ச நீதிமன்றத்தில் ஆங்கிலத்தை முதன்மையாக்குகிறது.",
            "why_b_en": "The Chief Justice's decision is not part of the opening text of Article 348(1).",
            "why_b_ta": "தலைமை நீதிபதியின் முடிவு சரத்து 348(1)-ன் தொடக்க வாசகத்தில் இல்லை.",
            "why_c_en": "UPSC consultation has no relevance to Article 348 judicial language.",
            "why_c_ta": "UPSC ஆலோசனையானது சரத்து 348 நீதித்துறை மொழியுடன் தொடர்பற்றது.",
            "why_d_en": "State Governors' concurrence is not in Article 348(1).",
            "why_d_ta": "மாநில ஆளுநர்களின் ஒப்புதல் சரத்து 348(1)-ல் இல்லை.",
            "tip_en": "Article 348(1) overrides Chapter I (Union) and Chapter II (Regional) regarding superior court languages.",
            "tip_ta": "சரத்து 348(1) உயர் நீதிமன்றங்கள் மற்றும் உச்ச நீதிமன்ற மொழிகள் தொடர்பாக அத்தியாயம் I மற்றும் II-ஐ மேலோங்குகிறது.",
            "fact_en": "This non-obstante clause ensures that superior courts across India maintain a single unified legal language (English).",
            "fact_ta": "இத்தடையற்ற வாசகம் இந்தியா முழுவதும் உள்ள உயர் நீதிமன்றங்கள் ஒற்றை ஒருங்கிணைந்த சட்ட மொழியை (ஆங்கிலம்) பராமரிப்பதை உறுதி செய்கிறது."
        },
        # 50
        {
            "subtopic": "Sanskrit Promotion under Article 351",
            "stem_en": "Under Article 351, why was Sanskrit specifically designated as the primary source of vocabulary for Hindi?",
            "stem_ta": "சரத்து 351-ன் கீழ், இந்தி மொழிக்கான சொல்லகராதியின் முதன்மை ஆதாரமாக சமஸ்கிருதம் ஏன் குறிப்பாக நியமிக்கப்பட்டது?",
            "options": [
                ("Because Sanskrit provides a pan-Indian classical lexical base shared across major linguistic families", "ஏனெனில் சமஸ்கிருதம் முக்கிய மொழிக் குடும்பங்கள் முழுவதும் பகிரப்பட்ட அகில இந்திய செவ்வியல் சொல் ஆதாரத்தை வழங்குகிறது"),
                ("Because Sanskrit was the most widely spoken spoken tongue in 1950", "ஏனெனில் 1950-ல் சமஸ்கிருதம் மிகவும் பரவலாகப் பேசப்பட்ட பேச்சு மொழியாக இருந்தது"),
                ("Because all other Eighth Schedule languages were derived directly from English", "ஏனெனில் மற்ற அனைத்து எட்டாவது அட்டவணை மொழிகளும் நேரடியாக ஆங்கிலத்திலிருந்து பெறப்பட்டவை என்பதால்"),
                ("Because Sanskrit is the sole official language of the United Nations", "ஏனெனில் சமஸ்கிருதம் ஐக்கிய நாடுகள் சபையின் ஒரே அதிகாரப்பூர்வ மொழியாக இருப்பதால்")
            ],
            "correct_key": "A",
            "exp_en": "Sanskrit was designated in Article 351 as the primary lexical source because its root-words (dhatus) and prefixes/suffixes have historically influenced both Indo-Aryan and Dravidian vocabularies, providing a bridge across linguistic regions.",
            "exp_ta": "சரத்து 351-ல் சமஸ்கிருதம் முதன்மை சொல் ஆதாரமாக நியமிக்கப்பட்டது, ஏனெனில் அதன் வேர்ச்சொற்கள் இந்தோ-ஆரிய மற்றும் திராவிட மொழிச் சொல்லகராதிகளை வரலாற்று ரீதியாக வளப்படுத்தி, மொழி எல்லைகளைக் கடந்து ஒரு பாலத்தை வழங்குகின்றன.",
            "why_a_en": "Sanskrit's classical root-words offered a common lexical reservoir for coining modern scientific and administrative terms.",
            "why_a_ta": "சமஸ்கிருதத்தின் வேர்ச்சொற்கள் நவீன அறிவியல் மற்றும் நிர்வாகக் கலைச்சொற்களை உருவாக்குவதற்கான பொதுவான களஞ்சியத்தை வழங்கின.",
            "why_b_en": "Sanskrit was not a mass spoken tongue in 1950; its role was classical and literary.",
            "why_b_ta": "1950-ல் சமஸ்கிருதம் பரவலாகப் பேசப்பட்ட மக்கள் மொழி அல்ல; அதன் பங்கு செவ்வியல் மற்றும் இலக்கியம் சார்ந்தது.",
            "why_c_en": "Indian languages are ancient and not derived from English.",
            "why_c_ta": "இந்திய மொழிகள் பழமையானவை, அவை ஆங்கிலத்திலிருந்து பெறப்பட்டவை அல்ல.",
            "why_d_en": "Sanskrit is not a UN official language (UN official languages are 6: Arabic, Chinese, English, French, Russian, Spanish).",
            "why_d_ta": "சமஸ்கிருதம் ஐ.நா அதிகாரப்பூர்வ மொழி அல்ல (ஐ.நா மொழிகள் 6: அரபு, சீனம், ஆங்கிலம், பிரெஞ்சு, ரஷியன், ஸ்பானிஷ்).",
            "tip_en": "Article 351 vocabulary: Primarily = Sanskrit; Secondarily = Other Eighth Schedule Languages.",
            "tip_ta": "சரத்து 351 சொல்லகராதி: முதன்மையாக = சமஸ்கிருதம்; இரண்டாவதாக = பிற எட்டாவது அட்டவணை மொழிகள்.",
            "fact_en": "Commission for Scientific and Technical Terminology (CSTT), created in 1961, uses this principle to coin pan-Indian technical words.",
            "fact_ta": "1961-ல் உருவாக்கப்பட்ட அறிவியல் மற்றும் தொழில்நுட்பக் கலைச்சொல் ஆணையம் (CSTT) அகில இந்திய கலைச்சொற்களை உருவாக்க இக்கோட்பாட்டைப் பயன்படுத்துகிறது."
        }
    ]

    questions = []
    for idx, item in enumerate(raw_data, start=1):
        qid = f"OL_M_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_ol_q(
            qid=qid,
            diff="Medium",
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
            tags=["polity", "official_language", "medium", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_medium_file():
    qs = get_medium_questions()
    print(f"Generated {len(qs)} raw Medium questions for Official Language.")
    balanced = randomize_and_balance_dataset(qs, seed=43)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "official_language_medium.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Medium MCQs to {out_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="OL_M_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid

if __name__ == "__main__":
    build_medium_file()
