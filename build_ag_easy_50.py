# -*- coding: utf-8 -*-
"""
Generator for Attorney General of India Easy MCQs (50 Questions: AG_E_001 to AG_E_050).
Strictly adheres to:
- Full 24-field TNPSC Nova AI schema
- Balanced answer keys (13 B, 12 C, 12 D, 13 A)
- Fully bilingual (English and authentic Tamil)
- M. Laxmikanth, Constitution of India (Art 76, 88, 105), Samacheer Kalvi
"""
import json
import os
from ag_mcq_helper import make_ag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_easy_data = [
    # 1
    {
        "stem_en": "Which Article of the Constitution of India provides for the office of the Attorney General of India?",
        "stem_ta": "இந்திய அரசியலமைப்பின் எந்த சரத்து இந்திய தலைமை வழக்கறிஞர் (அட்டர்னி ஜெனரல்) அலுவலகத்திற்கு வகை செய்கிறது?",
        "options": [("Article 72", "சரத்து 72"), ("Article 76", "சரத்து 76"), ("Article 148", "சரத்து 148"), ("Article 165", "சரத்து 165")],
        "correct_idx": 1,
        "exp_en": "Article 76 in Part V of the Constitution provides for the office of the Attorney General of India, who is the highest law officer in the country.",
        "exp_ta": "அரசியலமைப்பின் பகுதி V-ல் உள்ள சரத்து 76, நாட்டின் மிக உயர்ந்த சட்ட அதிகாரியான இந்திய தலைமை வழக்கறிஞர் (அட்டர்னி ஜெனரல்) அலுவலகத்திற்கு வகை செய்கிறது.",
        "tip": "Article 76 deals with Attorney General; Article 165 deals with Advocate General of a State.",
        "fact": "The Attorney General is the chief legal adviser to the Government of India."
    },
    # 2
    {
        "stem_en": "Who appoints the Attorney General of India under Article 76 of the Constitution?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 76-ன் கீழ் இந்திய தலைமை வழக்கறிஞரை நியமிப்பவர் யார்?",
        "options": [("Chief Justice of India", "இந்திய தலைமை நீதிபதி"), ("President of India", "இந்திய குடியரசுத் தலைவர்"), ("Prime Minister of India", "இந்தியப் பிரதமர்"), ("Union Law Minister", "மத்திய சட்ட அமைச்சர்")],
        "correct_idx": 1,
        "exp_en": "Article 76(1) states that the President of India shall appoint a person who is qualified to be appointed a Judge of the Supreme Court to be Attorney General for India.",
        "exp_ta": "சரத்து 76(1)-ன் படி, உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுள்ள ஒரு நபரை இந்திய குடியரசுத் தலைவர் இந்திய தலைமை வழக்கறிஞராக நியமிக்கிறார்.",
        "tip": "Appointed by the President on the advice of the Union Cabinet headed by the Prime Minister.",
        "fact": "The warrant of appointment is signed by the President under his hand and seal."
    },
    # 3
    {
        "stem_en": "To be appointed as the Attorney General of India, a person must possess the qualifications required to become which of the following?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞராக நியமிக்கப்படுவதற்கு, ஒருவர் கீழ்க்கண்ட எப்பதவிக்குரிய தகுதிகளைக் கொண்டிருக்க வேண்டும்?",
        "options": [("Judge of the High Court", "உயர்நீதிமன்ற நீதிபதி"), ("Judge of the Supreme Court", "உச்ச நீதிமன்ற நீதிபதி"), ("Member of Parliament", "நாடாளுமன்ற உறுப்பினர்"), ("Cabinet Secretary", "மத்திய அமைச்சரவை செயலாளர்")],
        "correct_idx": 1,
        "exp_en": "According to Article 76(1), the Attorney General must be a person qualified to be appointed a Judge of the Supreme Court.",
        "exp_ta": "சரத்து 76(1)-ன் படி, தலைமை வழக்கறிஞராக நியமிக்கப்படுபவர் உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தேவையான தகுதிகளைப் பெற்றிருக்க வேண்டும்.",
        "tip": "Supreme Court judge qualification requires being a citizen of India and (a) 5 years HC judge OR (b) 10 years HC advocate OR (c) eminent jurist.",
        "fact": "By contrast, an Advocate General of a State must be qualified to be a High Court judge (Article 165)."
    },
    # 4
    {
        "stem_en": "What is the tenure of office of the Attorney General of India as fixed by the Constitution?",
        "stem_ta": "அரசியலமைப்பால் நிர்ணயிக்கப்பட்ட இந்திய தலைமை வழக்கறிஞரின் பதவிக்காலம் என்ன?",
        "options": [("5 years", "5 ஆண்டுகள்"), ("Not fixed by the Constitution (holds office during the pleasure of the President)", "அரசியலமைப்பால் நிர்ணயிக்கப்படவில்லை (குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் இருப்பார்)"), ("6 years or age of 65 years", "6 ஆண்டுகள் அல்லது 65 வயது"), ("3 years", "3 ஆண்டுகள்")],
        "correct_idx": 1,
        "exp_en": "The Constitution does not fix the tenure of the Attorney General. Under Article 76(4), he holds office during the pleasure of the President.",
        "exp_ta": "தலைமை வழக்கறிஞரின் பதவிக்காலத்தை அரசியலமைப்பு நிர்ணயிக்கவில்லை. சரத்து 76(4)-ன் கீழ் அவர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை (Pleasure of the President) பதவியில் நீடிக்கிறார்.",
        "tip": "Pleasure of President means he can be removed by the President at any time without constitutional impeachment.",
        "fact": "Conventionally, he resigns when the Council of Ministers resigns or is replaced."
    },
    # 5
    {
        "stem_en": "To whom does the Attorney General of India submit his letter of resignation?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞர் தனது ராஜினாமா கடிதத்தை யாரிடம் சமர்ப்பிக்கிறார்?",
        "options": [("Prime Minister", "பிரதமர்"), ("President of India", "இந்திய குடியரசுத் தலைவர்"), ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"), ("Speaker of Lok Sabha", "மக்களவை சபாநாயகர்")],
        "correct_idx": 1,
        "exp_en": "The Attorney General of India can resign from his office at any time by addressing his resignation letter in writing to the President of India.",
        "exp_ta": "இந்திய தலைமை வழக்கறிஞர் தனது ராஜினாமா கடிதத்தை இந்திய குடியரசுத் தலைவரிடம் எழுத்துப்பூர்வமாக அளித்து எந்நேரத்திலும் பதவி விலகலாம்.",
        "tip": "Appointed by President -> Submits resignation to President.",
        "fact": "Article 76 does not prescribe any specific notice period for resignation."
    },
    # 6
    {
        "stem_en": "Who determines the remuneration and allowances of the Attorney General of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞரின் ஊதியம் மற்றும் படிகளை தீர்மானிப்பவர் யார்?",
        "options": [("Parliament by law", "சட்டத்தின் மூலம் நாடாளுமன்றம்"), ("President of India", "இந்திய குடியரசுத் தலைவர்"), ("Supreme Court Collegium", "உச்ச நீதிமன்ற கொலீஜியம்"), ("Union Finance Ministry", "மத்திய நிதி அமைச்சகம்")],
        "correct_idx": 1,
        "exp_en": "Under Article 76(4) of the Constitution, the Attorney General receives such remuneration as the President may determine.",
        "exp_ta": "அரசியலமைப்பின் சரத்து 76(4)-ன் படி, தலைமை வழக்கறிஞர் குடியரசுத் தலைவர் தீர்மானிக்கும் ஊதியத்தைப் பெறுகிறார்.",
        "tip": "Remuneration is not fixed by Parliament or the Constitution; it is determined by the President under Law Officers Rules 1987.",
        "fact": "He receives appearance fees and retainership, rather than a fixed civil service salary."
    },
    # 7
    {
        "stem_en": "Who is recognized as the First Law Officer of the Government of India?",
        "stem_ta": "இந்திய அரசாங்கத்தின் முதல் சட்ட அதிகாரி என்று அங்கீகரிக்கப்படுபவர் யார்?",
        "options": [("Chief Justice of India", "இந்திய தலைமை நீதிபதி"), ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"), ("Union Law Minister", "மத்திய சட்ட அமைச்சர்"), ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்")],
        "correct_idx": 1,
        "exp_en": "The Attorney General of India is the highest legal authority and the First Law Officer of the Government of India.",
        "exp_ta": "இந்திய தலைமை வழக்கறிஞர் (அட்டர்னி ஜெனரல்) நாட்டின் உச்ச சட்ட அதிகாரியாகவும், இந்திய அரசாங்கத்தின் முதல் சட்ட அதிகாரியாகவும் கருதப்படுகிறார்.",
        "tip": "1st Law Officer = Attorney General; 2nd Law Officer = Solicitor General.",
        "fact": "Union Law Minister is a political executive, whereas the Attorney General is a constitutional law officer."
    },
    # 8
    {
        "stem_en": "Under Article 76(3) of the Constitution, in the performance of his duties, the Attorney General has the right of audience in:",
        "stem_ta": "அரசியலமைப்பின் சரத்து 76(3)-ன் கீழ், தனது பணிகளை ஆற்றுவதில் தலைமை வழக்கறிஞருக்கு எங்கு முன்னிலையாகும் உரிமை (Right of Audience) உண்டு?",
        "options": [("Only in the Supreme Court of India", "இந்திய உச்ச நீதிமன்றத்தில் மட்டுமே"), ("All courts in the territory of India", "இந்திய எல்லைக்குள் உள்ள அனைத்து நீதிமன்றங்களிலும்"), ("Only High Courts and Supreme Court", "உயர்நீதிமன்றங்கள் மற்றும் உச்ச நீதிமன்றத்தில் மட்டுமே"), ("Only Central Administrative Tribunals", "மத்திய நிர்வாக தீர்ப்பாயங்களில் மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "Article 76(3) explicitly states that in the performance of his duties, the Attorney General shall have the right of audience in all courts in the territory of India.",
        "exp_ta": "சரத்து 76(3)-ன் படி, தலைமை வழக்கறிஞர் தனது கடமைகளை நிறைவேற்றுவதில் இந்தியாவின் எல்லைக்குட்பட்ட அனைத்து நீதிமன்றங்களிலும் முன்னிலையாகும் உரிமை கொண்டுள்ளார்.",
        "tip": "Right of audience in ALL courts in India is an exclusive constitutional privilege of the Attorney General.",
        "fact": "He has precedence over all other advocates in all courts under the Advocates Act 1961."
    },
    # 9
    {
        "stem_en": "Which Article of the Constitution gives the Attorney General the right to speak and take part in the proceedings of Parliament without the right to vote?",
        "stem_ta": "வாக்களிக்கும் உரிமை இல்லாமல் நாடாளுமன்றக் கூட்டத்தொடர்களில் பேசவும் பங்கேற்கவும் தலைமை வழக்கறிஞருக்கு உரிமை அளிக்கும் அரசியலமைப்பு சரத்து எது?",
        "options": [("Article 76", "சரத்து 76"), ("Article 88", "சரத்து 88"), ("Article 105", "சரத்து 105"), ("Article 110", "சரத்து 110")],
        "correct_idx": 1,
        "exp_en": "Article 88 of the Constitution gives the Attorney General the right to speak in, and take part in the proceedings of, either House of Parliament, any joint sitting, and any parliamentary committee of which he is named a member, but without the right to vote.",
        "exp_ta": "சரத்து 88, நாடாளுமன்றத்தின் இரு அவைகளிலும், கூட்டு அமர்விலும், தான் உறுப்பினராக நியமிக்கப்பட்ட குழுவிலும் பேசவும் பங்கேற்கவும் தலைமை வழக்கறிஞருக்கு உரிமை அளிக்கிறது; ஆனால் அவருக்கு வாக்களிக்கும் உரிமை இல்லை.",
        "tip": "Article 88 = Right to speak and participate; NO right to vote.",
        "fact": "This right is shared by Union Ministers and the Attorney General under Article 88."
    },
    # 10
    {
        "stem_en": "Under Article 105(4) of the Constitution, what privileges and immunities does the Attorney General enjoy while taking part in Parliamentary proceedings?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 105(4)-ன் கீழ், நாடாளுமன்ற நடவடிக்கைகளில் பங்கேற்கும்போது தலைமை வழக்கறிஞர் என்ன சலுகைகளையும் பாதுகாப்புகளையும் பெறுகிறார்?",
        "options": [("Immunity from all civil and criminal laws permanently", "அனைத்து சிவில் மற்றும் குற்றவியல் சட்டங்களிலிருந்து நிரந்தர விலக்கு"), ("All privileges and immunities available to a Member of Parliament", "நாடாளுமன்ற உறுப்பினருக்கு (MP) கிடைக்கக்கூடிய அனைத்து சலுகைகள் மற்றும் பாதுகாப்புகள்"), ("Only diplomatic immunity", "தூதரக பாதுகாப்பு மட்டுமே"), ("No privileges at all", "எந்த சலுகைகளும் இல்லை")],
        "correct_idx": 1,
        "exp_en": "Under Article 105(4), the provisions regarding powers, privileges, and immunities of Parliament and its members apply equally to persons who have the right to speak in Parliament, including the Attorney General.",
        "exp_ta": "சரத்து 105(4)-ன் கீழ், நாடாளுமன்ற உறுப்பினர்களுக்கு உரித்தான அனைத்து அதிகாரங்கள், சிறப்புரிமைகள் மற்றும் பாதுகாப்புகள் நாடாளுமன்றத்தில் பேச உரிமையுள்ள தலைமை வழக்கறிஞருக்கும் பொருந்தும்.",
        "tip": "Enjoys MP privileges under Article 105(4), but cannot vote (Article 88).",
        "fact": "He cannot be sued in any court for anything said in Parliament."
    },
    # 11
    {
        "stem_en": "Who was the first Attorney General of Independent India?",
        "stem_ta": "சுதந்திர இந்தியாவின் முதல் தலைமை வழக்கறிஞர் (அட்டர்னி ஜெனரல்) யார்?",
        "options": [("C.K. Daphtary", "சி.கே. தப்தாரி"), ("M.C. Setalvad", "எம்.சி. செதல்வாட்"), ("Niren De", "நிரேன் டே"), ("K. Parasaran", "கே. பராசரன்")],
        "correct_idx": 1,
        "exp_en": "Motilal Chimanlal Setalvad (M.C. Setalvad) was the first Attorney General of India, serving from 28 January 1950 to 1 March 1963.",
        "exp_ta": "மோதிலால் சிமன்லால் செதல்வாட் (எம்.சி. செதல்வாட்) இந்தியாவின் முதல் தலைமை வழக்கறிஞராவார் (1950 ஜனவரி 28 முதல் 1963 மார்ச் 1 வரை பணியாற்றினார்).",
        "tip": "M.C. Setalvad also served as the first Chairman of the Law Commission of India (1955-1958).",
        "fact": "He holds the record for the longest tenure as Attorney General of India (over 13 years)."
    },
    # 12
    {
        "stem_en": "Who holds the record for the longest tenure as the Attorney General of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞராக மிக நீண்ட காலம் பணியாற்றிய சாதனைக்குரியவர் யார்?",
        "options": [("Soli Sorabjee", "சோலி சோராப்ஜி"), ("M.C. Setalvad", "எம்.சி. செதல்வாட்"), ("K.K. Venugopal", "கே.கே. வேணுகோபால்"), ("Milon K. Banerjee", "மிலன் கே. பானர்ஜி")],
        "correct_idx": 1,
        "exp_en": "M.C. Setalvad held the office of Attorney General of India for over 13 continuous years (1950 to 1963), the longest in Indian history.",
        "exp_ta": "எம்.சி. செதல்வாட் 13 ஆண்டுகளுக்கும் மேலாக (1950 முதல் 1963 வரை) தலைமை வழக்கறிஞராக தொடர்ந்து பணியாற்றினார்; இதுவே இந்திய வரலாற்றில் மிக நீண்ட பதவிக்காலமாகும்.",
        "tip": "Longest tenure = M.C. Setalvad (13+ years); Shortest tenure = Soli Sorabjee (first term, 1989-1990).",
        "fact": "He worked closely with Prime Minister Jawaharlal Nehru on post-independence legal foundations."
    },
    # 13
    {
        "stem_en": "Who was appointed as the 16th Attorney General of India in October 2022?",
        "stem_ta": "அக்டோபர் 2022-ல் இந்தியாவின் 16-வது தலைமை வழக்கறிஞராக நியமிக்கப்பட்டவர் யார்?",
        "options": [("Mukul Rohatgi", "முகுல் ரோஹத்கி"), ("R. Venkataramani", "ஆர். வெங்கடரமணி"), ("K.K. Venugopal", "கே.கே. வேணுகோபால்"), ("Tushar Mehta", "துஷார் மேத்தா")],
        "correct_idx": 1,
        "exp_en": "Senior Advocate R. Venkataramani was appointed as the 16th Attorney General of India by the President of India on 28 September 2022, assuming office on 1 October 2022.",
        "exp_ta": "மூத்த வழக்கறிஞர் ஆர். வெங்கடரமணி 2022 செப்டம்பர் 28 அன்று குடியரசுத் தலைவரால் இந்தியாவின் 16-வது தலைமை வழக்கறிஞராக நியமிக்கப்பட்டு அக்டோபர் 1 அன்று பொறுப்பேற்றார்.",
        "tip": "Succeeded veteran jurist K.K. Venugopal.",
        "fact": "R. Venkataramani is a designated Senior Advocate of the Supreme Court and was a member of the Law Commission."
    },
    # 14
    {
        "stem_en": "Whom did R. Venkataramani succeed as the Attorney General of India in October 2022?",
        "stem_ta": "அக்டோபர் 2022-ல் யாருக்குப் பிறகு ஆர். வெங்கடரமணி இந்திய தலைமை வழக்கறிஞராகப் பொறுப்பேற்றார்?",
        "options": [("Mukul Rohatgi", "முகுல் ரோஹத்கி"), ("K.K. Venugopal", "கே.கே. வேணுகோபால்"), ("Ashok Desai", "அசோக் தேசாய்"), ("G.E. Vahanvati", "ஜி.இ. வாகனவதி")],
        "correct_idx": 1,
        "exp_en": "R. Venkataramani succeeded veteran Senior Advocate K.K. Venugopal, who served as the 15th Attorney General from July 2017 to September 2022.",
        "exp_ta": "2017 ஜூலை முதல் 2022 செப்டம்பர் வரை 15-வது தலைமை வழக்கறிஞராக பணியாற்றிய கே.கே. வேணுகோபாலுக்குப் பிறகு ஆர். வெங்கடரமணி பொறுப்பேற்றார்.",
        "tip": "K.K. Venugopal served till the age of 91 before retiring.",
        "fact": "K.K. Venugopal had replaced Mukul Rohatgi in 2017."
    },
    # 15
    {
        "stem_en": "Is the Attorney General of India a member of the Union Cabinet?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞர் மத்திய அமைச்சரவையில் (Cabinet) ஓர் உறுப்பினரா?",
        "options": [("Yes, he is an ex-officio Cabinet Minister", "ஆம், அவர் பதவிவழி கேபினட் அமைச்சர்"), ("No, he is not a member of the Union Cabinet", "இல்லை, அவர் மத்திய அமைச்சரவையில் உறுப்பினர் அல்ல"), ("Yes, but only for legal matters", "ஆம், ஆனால் சட்ட விவகாரங்களுக்கு மட்டுமே"), ("Only during national emergency", "தேசிய அவசரநிலையின் போது மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "Unlike the Attorney General in the United Kingdom who is a political minister and cabinet member, the Attorney General of India is NOT a member of the Union Cabinet.",
        "exp_ta": "பிரிட்டன் தலைமை வழக்கறிஞர் கேபினட் அமைச்சராக இருக்கும் நிலையில், இந்திய தலைமை வழக்கறிஞர் மத்திய அமைச்சரவையில் உறுப்பினர் அல்ல.",
        "tip": "Legal matters in the Union Cabinet are represented by the Union Minister of Law and Justice.",
        "fact": "He participates in parliamentary debates as a constitutional officer, not as a political party member."
    },
    # 16
    {
        "stem_en": "Is the Attorney General of India classified as a full-time government servant?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞர் முழுநேர அரசு ஊழியராக வகைப்படுத்தப்படுகிறாரா?",
        "options": [("Yes, under Article 311 of the Constitution", "ஆம், அரசியலமைப்பின் சரத்து 311-ன் கீழ்"), ("No, he is not a whole-time government servant and is not debarred from private legal practice", "இல்லை, அவர் முழுநேர அரசு ஊழியர் அல்ல, மேலும் தனியார் வழக்கறிஞர் தொழில் செய்ய தடை இல்லை"), ("Yes, drawing salary from the Consolidated Fund of India as an employee", "ஆம், ஊழியராக இந்திய தொகுப்பு நிதியிலிருந்து ஊதியம் பெறுகிறார்"), ("Only when assigned cases by the Supreme Court", "உச்ச நீதிமன்றம் வழக்குகளை ஒப்படைக்கும் போது மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "The Attorney General is not a whole-time counsel for the Government nor is he a government servant. Therefore, he is not debarred from private legal practice, subject to certain professional restrictions.",
        "exp_ta": "தலைமை வழக்கறிஞர் முழுநேர அரசு வழக்கறிஞரோ அல்லது அரசு ஊழியரோ அல்ல. எனவே சில தொழில்முறை கட்டுப்பாடுகளுக்கு உட்பட்டு அவர் தனியார் வழக்கறிஞர் தொழில் செய்ய தடை விதிக்கப்படவில்லை.",
        "tip": "He does not fall in the category of civil servants under Article 311.",
        "fact": "He cannot advise or hold a brief against the Government of India."
    },
    # 17
    {
        "stem_en": "Which of the following restrictions applies to the private legal practice of the Attorney General of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞரின் தனியார் வழக்கறிஞர் தொழில் மீது கீழ்க்கண்ட எந்த கட்டுப்பாடு விதிக்கப்பட்டுள்ளது?",
        "options": [("He cannot practice law in any High Court", "அவர் எந்த உயர்நீதிமன்றத்திலும் வாதாட முடியாது"), ("He should not advise or hold briefs against the Government of India", "அவர் இந்திய அரசாங்கத்திற்கு எதிராக ஆலோசனை வழங்கவோ வழக்குகளில் ஆஜராகவோ கூடாது"), ("He cannot charge any legal fees from any client", "எந்த வாடிக்கையாளரிடமிருந்தும் கட்டணம் வசூலிக்க முடியாது"), ("He can only handle family disputes", "குடும்ப வழக்குகளை மட்டுமே நடத்த முடியும்")],
        "correct_idx": 1,
        "exp_en": "The Attorney General should not advise or hold briefs against the Government of India, nor should he advise in cases where he is likely to be called upon to advise or appear for the Government.",
        "exp_ta": "தலைமை வழக்கறிஞர் இந்திய அரசாங்கத்திற்கு எதிராக ஆலோசனை வழங்கவோ அல்லது அரசுக்கு எதிரான வழக்குகளில் ஆஜராகவோ கூடாது.",
        "tip": "Also cannot defend accused in criminal cases without permission of Government of India.",
        "fact": "Cannot accept appointment as director in any company without government permission."
    },
    # 18
    {
        "stem_en": "Can the Attorney General of India defend an accused person in a criminal prosecution?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞர் ஒரு குற்றவியல் வழக்கில் குற்றம் சாட்டப்பட்டவருக்காக ஆஜராகி வாதாட முடியுமா?",
        "options": [("Never under any circumstances", "எந்த சூழ்நிலையிலும் முடியாது"), ("Yes, but only with the permission of the Government of India", "ஆம், ஆனால் இந்திய அரசாங்கத்தின் முன்அனுமதியுடன் மட்டுமே முடியும்"), ("Yes, freely without any permission", "ஆம், எந்த அனுமதியும் இன்றி தாராளமாக"), ("Only in Sessions Courts", "செஷன்ஸ் நீதிமன்றங்களில் மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "Under the Law Officers (Conditions of Service) Rules 1987, the Attorney General shall not defend an accused person in criminal prosecutions without the prior permission of the Government of India.",
        "exp_ta": "1987 சட்ட அதிகாரிகள் விதிகளின்படி, இந்திய அரசாங்கத்தின் முன்அனுமதி இல்லாமல் குற்றவியல் வழக்குகளில் குற்றம் சாட்டப்பட்டவருக்காக தலைமை வழக்கறிஞர் ஆஜராகக்கூடாது.",
        "tip": "Government permission is mandatory for criminal defence briefs.",
        "fact": "This restriction prevents conflict with the State's prosecutorial interest."
    },
    # 19
    {
        "stem_en": "Are the offices of the Solicitor General of India and Additional Solicitors General created by the Constitution of India?",
        "stem_ta": "இந்திய சொலிசிட்டர் ஜெனரல் மற்றும் கூடுதல் சொலிசிட்டர் ஜெனரல்கள் அலுவலகங்கள் இந்திய அரசியலமைப்பால் உருவாக்கப்பட்டவையா?",
        "options": [("Yes, under Article 76(2)", "ஆம், சரத்து 76(2)-ன் கீழ்"), ("No, they are non-constitutional / statutory and executive offices not mentioned in Article 76", "இல்லை, அவை சரத்து 76-ல் குறிப்பிடப்படாத அரசியலமைப்பு சாராத சட்டப்பூர்வ மற்றும் நிர்வாக அலுவலகங்கள்"), ("Yes, under Article 88", "ஆம், சரத்து 88-ன் கீழ்"), ("Yes, under Article 143", "ஆம், சரத்து 143-ன் கீழ்")],
        "correct_idx": 1,
        "exp_en": "Article 76 mentions only the Attorney General of India. It does not mention the Solicitor General or Additional Solicitor General. They are appointed under executive rules to assist the Attorney General.",
        "exp_ta": "சரத்து 76 தலைமை வழக்கறிஞரை மட்டுமே குறிப்பிடுகிறது; சொலிசிட்டர் ஜெனரல் மற்றும் கூடுதல் சொலிசிட்டர் ஜெனரல்கள் குறித்து அரசியலமைப்பில் குறிப்பிடப்படவில்லை. அவர்கள் தலைமை வழக்கறிஞருக்கு உதவ நியமிக்கப்படும் சட்டப்பூர்வ/நிர்வாக அதிகாரிகள்.",
        "tip": "Constitutional Law Officer = Attorney General only. Solicitor General is NOT a constitutional office.",
        "fact": "Solicitor General is the Second Law Officer of the Government of India."
    },
    # 20
    {
        "stem_en": "Who assists the Attorney General of India in the fulfillment of his official legal responsibilities?",
        "stem_ta": "தனது அதிகாரப்பூர்வ சட்டப் பொறுப்புகளை நிறைவேற்றுவதில் இந்திய தலைமை வழக்கறிஞருக்கு உதவுபவர்கள் யார்?",
        "options": [("Chief Justice of India and Supreme Court Judges", "இந்திய தலைமை நீதிபதி மற்றும் உச்ச நீதிமன்ற நீதிபதிகள்"), ("Solicitor General of India and Additional Solicitors General", "இந்திய சொலிசிட்டர் ஜெனரல் மற்றும் கூடுதல் சொலிசிட்டர் ஜெனரல்கள்"), ("Union Home Secretary and Law Secretary", "மத்திய உள்துறை செயலாளர் மற்றும் சட்ட செயலாளர்"), ("Comptroller and Auditor General", "தலைமை கணக்கு தணிக்கையாளர்")],
        "correct_idx": 1,
        "exp_en": "In addition to the Attorney General, there are other law officers of the Government of India—the Solicitor General of India and Additional Solicitors General—who assist the AG in official duties.",
        "exp_ta": "தலைமை வழக்கறிஞருக்கு அவரது அதிகாரப்பூர்வ பணிகளில் உதவ இந்திய சொலிசிட்டர் ஜெனரல் மற்றும் கூடுதல் சொலிசிட்டர் ஜெனரல்கள் நியமிக்கப்படுகிறார்கள்.",
        "tip": "Solicitor General and Additional Solicitors General appear in court on behalf of GoI alongside the AG.",
        "fact": "Appointments are cleared by the Appointments Committee of the Cabinet (ACC)."
    },
    # 21
    {
        "stem_en": "In which Part and Chapter of the Constitution of India is Article 76 located?",
        "stem_ta": "இந்திய அரசியலமைப்பின் எந்த பகுதி மற்றும் அத்தியாயத்தில் சரத்து 76 அமைந்துள்ளது?",
        "options": [("Part III, Chapter I", "பகுதி III, அத்தியாயம் I"), ("Part V, Chapter I (The Executive)", "பகுதி V, அத்தியாயம் I (மத்திய நிர்வாகம்)"), ("Part VI, Chapter II", "பகுதி VI, அத்தியாயம் II"), ("Part XII, Chapter I", "பகுதி XII, அத்தியாயம் I")],
        "correct_idx": 1,
        "exp_en": "Article 76 is located in Part V (The Union), Chapter I (The Executive) of the Constitution of India, comprising the President, Vice-President, Prime Minister, Council of Ministers, and Attorney General.",
        "exp_ta": "சரத்து 76 இந்திய அரசியலமைப்பின் பகுதி V (மத்திய அரசு), அத்தியாயம் I (நிர்வாகம்) என்பதன் கீழ் அமைந்துள்ளது.",
        "tip": "Union Executive consists of: President, VP, PM, Council of Ministers, and Attorney General.",
        "fact": "The Attorney General is constitutionally an integral part of the Union Executive."
    },
    # 22
    {
        "stem_en": "Under Article 143 of the Constitution, who represents the Government of India in any advisory reference made by the President to the Supreme Court?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 143-ன் கீழ் குடியரசுத் தலைவர் உச்ச நீதிமன்றத்திடம் கேட்கும் ஆலோசனைக் குறிப்பில் இந்திய அரசாங்கத்தின் சார்பில் ஆஜராகி வாதாடுபவர் யார்?",
        "options": [("Union Law Minister", "மத்திய சட்ட அமைச்சர்"), ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"), ("Speaker of Lok Sabha", "மக்களவை சபாநாயகர்"), ("Chief Justice of India", "இந்திய தலைமை நீதிபதி")],
        "correct_idx": 1,
        "exp_en": "Under the President's allocation of legal duties, the Attorney General represents the Government of India in any reference made by the President to the Supreme Court under Article 143 (Advisory Jurisdiction).",
        "exp_ta": "குடியரசுத் தலைவர் சரத்து 143-ன் கீழ் உச்ச நீதிமன்றத்திடம் ஆலோசனை கோரும் குறிப்புகளில் இந்திய அரசாங்கத்தின் சார்பில் தலைமை வழக்கறிஞர் ஆஜராகி வாதாடுகிறார்.",
        "tip": "Article 143 = Advisory jurisdiction of the Supreme Court.",
        "fact": "The AG also appears on behalf of GoI in any suit in the Supreme Court where the Union is a party."
    },
    # 23
    {
        "stem_en": "Can the Attorney General of India accept an appointment as a director in any commercial company or corporation without permission?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞர் அனுமதியின்றி ஏதேனும் வணிக நிறுவனம் அல்லது கார்ப்பரேஷனில் இயக்குநராக (Director) நியமிக்கப்படுவதை ஏற்க முடியுமா?",
        "options": [("Yes, without any restriction", "ஆம், எந்த கட்டுப்பாடும் இன்றி"), ("No, he cannot accept any directorship without the prior permission of the Government of India", "இல்லை, இந்திய அரசாங்கத்தின் முன்அனுமதி இல்லாமல் அவர் எந்த நிறுவனத்திலும் இயக்குநர் பதவியை ஏற்க முடியாது"), ("Yes, but only in public sector undertakings", "ஆம், ஆனால் பொதுத்துறை நிறுவனங்களில் மட்டுமே"), ("Only if nominated by the President", "குடியரசுத் தலைவர் பரிந்துரைத்தால் மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "Under the Law Officers (Conditions of Service) Rules 1987, the Attorney General shall not accept appointment to a directorship in any company without the prior permission of the Government.",
        "exp_ta": "சட்ட அதிகாரிகள் விதிகள் 1987-ன் கீழ், அரசாங்கத்தின் முன்அனுமதி இல்லாமல் தலைமை வழக்கறிஞர் எந்தவொரு நிறுவனத்திலும் இயக்குநர் பதவியை ஏற்கக்கூடாது.",
        "tip": "Prevents conflict of interest with corporate entities.",
        "fact": "This rule applies equally to the Solicitor General and Additional Solicitors General."
    },
    # 24
    {
        "stem_en": "Under the Advocates Act 1961, what is the statutory right of precedence given to the Attorney General of India at the Bar?",
        "stem_ta": "1961 வழக்கறிஞர்கள் சட்டத்தின் கீழ், பார் கவுன்சிலில் இந்திய தலைமை வழக்கறிஞருக்கு வழங்கப்பட்டுள்ள சட்டப்பூர்வ முன்னுரிமை (Precedence) என்ன?",
        "options": [
            ("Precedence after the Solicitor General", "சொலிசிட்டர் ஜெனரலுக்குப் பின் முன்னுரிமை"),
            ("Precedence over all other advocates in all courts in India", "இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் மற்ற அனைத்து வழக்கறிஞர்களுக்கும் மேலான முதல் முன்னுரிமை"),
            ("Equal precedence with senior advocates of High Courts", "உயர்நீதிமன்ற மூத்த வழக்கறிஞர்களுடன் சம முன்னுரிமை"),
            ("No statutory precedence", "சட்டப்பூர்வ முன்னுரிமை எதுவும் இல்லை")
        ],
        "correct_idx": 1,
        "exp_en": "Under Section 23(1) of the Advocates Act 1961, the Attorney General of India has statutory pre-audience and precedence over all other advocates in all courts across India.",
        "exp_ta": "1961 வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 23(1)-ன் கீழ், இந்திய தலைமை வழக்கறிஞர் இந்தியாவின் அனைத்து நீதிமன்றங்களிலும் பிற அனைத்து வழக்கறிஞர்களை விடவும் முதலிட முன்னுரிமை கொண்டுள்ளார்.",
        "tip": "Order of precedence: (1) Attorney General, (2) Solicitor General, (3) Additional Solicitors General.",
        "fact": "He is the ex-officio leader of the Indian Bar."
    },
    # 25
    {
        "stem_en": "Does the Attorney General of India possess the constitutional power to vote in the proceedings of Parliament?",
        "stem_ta": "நாடாளுமன்ற நடவடிக்கைகளில் வாக்களிக்கும் அரசியலமைப்பு அதிகாரம் இந்திய தலைமை வழக்கறிஞருக்கு உண்டா?",
        "options": [("Yes, in both Houses", "ஆம், இரு அவைகளிலும் உண்டு"), ("No, he has no right to vote in Parliament", "இல்லை, அவருக்கு நாடாளுமன்றத்தில் வாக்களிக்கும் உரிமை இல்லை"), ("Yes, but only in joint sittings", "ஆம், ஆனால் கூட்டு அமர்வுகளில் மட்டுமே"), ("Yes, in case of a tie", "ஆம், சமநிலை ஏற்படும் போது மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "Article 88 explicitly states that the Attorney General shall not by virtue of this Article be entitled to vote in any House of Parliament or joint sitting.",
        "exp_ta": "சரத்து 88, தலைமை வழக்கறிஞர் நாடாளுமன்றத்தின் எந்த அவையிலும் அல்லது கூட்டு அமர்விலும் வாக்களிக்க உரிமை பெற்றவர் அல்ல என்று திட்டவட்டமாக கூறுகிறது.",
        "tip": "He can speak and participate, but CANNOT vote under any circumstances.",
        "fact": "Voting in Parliament is strictly reserved for elected or nominated Members of Parliament."
    },
    # 26
    {
        "stem_en": "Under which Article of the Constitution can the Attorney General be named as a member of any Parliamentary Committee?",
        "stem_ta": "எந்த அரசியலமைப்பு சரத்தின் கீழ் தலைமை வழக்கறிஞர் ஏதேனும் ஒரு நாடாளுமன்றக் குழுவின் உறுப்பினராக நியமிக்கப்படலாம்?",
        "options": [("Article 76", "சரத்து 76"), ("Article 88", "சரத்து 88"), ("Article 102", "சரத்து 102"), ("Article 118", "சரத்து 118")],
        "correct_idx": 1,
        "exp_en": "Article 88 provides that the Attorney General has the right to speak and take part in the proceedings of 'any committee of Parliament of which he may be named a member', without the right to vote.",
        "exp_ta": "சரத்து 88-ன் படி, தலைமை வழக்கறிஞர் தான் உறுப்பினராக பெயரிடப்படும் எந்தவொரு நாடாளுமன்றக் குழுவின் நடவடிக்கைகளிலும் வாக்களிக்கும் உரிமையின்றி பேசவும் பங்கேற்கவும் உரிமை உண்டு.",
        "tip": "Parliament can appoint him to Joint Select Committees on legal/constitutional bills.",
        "fact": "Even in such committees, he cannot vote on any division or report."
    },
    # 27
    {
        "stem_en": "What is the primary constitutional duty of the Attorney General of India under Article 76(2)?",
        "stem_ta": "சரத்து 76(2)-ன் கீழ் இந்திய தலைமை வழக்கறிஞரின் முதன்மையான அரசியலமைப்பு கடமை என்ன?",
        "options": [
            ("To administer the judicial appointments", "நீதிமன்ற நியமனங்களை நிர்வகிப்பது"),
            ("To give advice to the Government of India upon legal matters and perform other legal duties referred by the President", "இந்திய அரசாங்கத்திற்கு சட்ட விவகாரங்களில் ஆலோசனை வழங்குவதும் குடியரசுத் தலைவரால் ஒப்படைக்கப்படும் சட்டப் பணிகளை ஆற்றுவதும்"),
            ("To draft election manifestos", "தேர்தல் அறிக்கைகளை வரைவது"),
            ("To act as Lokpal of India", "இந்தியாவின் லோக்பாலாக செயல்படுவது")
        ],
        "correct_idx": 1,
        "exp_en": "Article 76(2) provides that it shall be the duty of the Attorney General to give advice to the Government of India upon such legal matters, and to perform such other duties of a legal character, as may from time to time be referred or assigned to him by the President.",
        "exp_ta": "சரத்து 76(2)-ன் படி, குடியரசுத் தலைவரால் அனுப்பப்படும் சட்ட விவகாரங்களில் இந்திய அரசாங்கத்திற்கு ஆலோசனை வழங்குவதும், ஒப்படைக்கப்படும் பிற சட்டப் பணிகளை நிறைவேற்றுவதும் தலைமை வழக்கறிஞரின் கடமையாகும்.",
        "tip": "He advises the Government of India; he does not decide policy or pass executive orders.",
        "fact": "His opinions are advisory and not strictly binding on the Government."
    },
    # 28
    {
        "stem_en": "Which of the following is NOT a qualification required to be appointed as the Attorney General of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞராக நியமிக்கப்படுவதற்கு கீழ்க்கண்டவற்றில் எது அவசியமான தகுதி அல்ல?",
        "options": [
            ("He must be a citizen of India", "அவர் இந்திய குடிமகனாக இருக்க வேண்டும்"),
            ("He must have been an advocate of a High Court for at least 15 years", "அவர் குறைந்தது 15 ஆண்டுகள் உயர்நீதிமன்ற வழக்கறிஞராக பணியாற்றியிருக்க வேண்டும்"),
            ("He must have been a judge of some High Court for at least 5 years", "அவர் குறைந்தது 5 ஆண்டுகள் ஏதேனும் உயர்நீதிமன்ற நீதிபதியாக பணியாற்றியிருக்க வேண்டும்"),
            ("He must be an eminent jurist in the opinion of the President", "அவர் குடியரசுத் தலைவரின் பார்வையில் ஒரு சிறந்த சட்ட நிபுணராக இருக்க வேண்டும்")
        ],
        "correct_idx": 1,
        "exp_en": "Under Article 124(3), the qualification for an advocate is at least 10 years (not 15 years) in a High Court. Therefore, 'at least 15 years' is incorrect.",
        "exp_ta": "சரத்து 124(3)-ன் கீழ், உயர்நீதிமன்ற வழக்கறிஞராக 10 ஆண்டுகள் பணியாற்றியிருக்க வேண்டும் (15 ஆண்டுகள் அல்ல). எனவே 15 ஆண்டுகள் என்பது தவறானது.",
        "tip": "High Court Advocate requirement is 10 years; High Court Judge requirement is 5 years.",
        "fact": "The 'eminent jurist' category is available for Supreme Court Judge / Attorney General, but not for High Court Judge."
    },
    # 29
    {
        "stem_en": "Can the President appoint an 'eminent jurist' as the Attorney General of India?",
        "stem_ta": "குடியரசுத் தலைவர் ஒரு சிறந்த சட்ட அறிஞரை (Eminent Jurist) இந்திய தலைமை வழக்கறிஞராக நியமிக்க முடியுமா?",
        "options": [("No, only sitting High Court judges can be appointed", "இல்லை, பதவியிலுள்ள உயர்நீதிமன்ற நீதிபதிகளை மட்டுமே நியமிக்க முடியும்"), ("Yes, because an eminent jurist is qualified to be appointed as a Supreme Court Judge under Article 124(3)(c)", "ஆம், ஏனெனில் சரத்து 124(3)(c)-ன் கீழ் ஒரு சிறந்த சட்ட அறிஞர் உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுடையவர்"), ("Only with the consent of Chief Justice of India", "தலைமை நீதிபதியின் ஒப்புதலுடன் மட்டுமே"), ("Only during financial emergency", "நிதி அவசரநிலையின் போது மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "Since the Attorney General must be qualified to be a Supreme Court judge under Article 76(1), and Article 124(3)(c) allows an 'eminent jurist in the opinion of the President' to be appointed a SC judge, an eminent jurist can legally be appointed AG.",
        "exp_ta": "சரத்து 76(1)-ன் படி உச்ச நீதிமன்ற நீதிபதிக்குரிய தகுதி தேவைப்படுவதாலும், சரத்து 124(3)(c)-ன் கீழ் சிறந்த சட்ட அறிஞர் உச்ச நீதிமன்ற நீதிபதியாக தகுதி பெற்றிருப்பதாலும், அவரை தலைமை வழக்கறிஞராக நியமிக்க முடியும்.",
        "tip": "This theoretical qualification has rarely been used in practice; eminent practicing Senior Advocates are usually appointed.",
        "fact": "This category does not exist for the appointment of an Advocate General under Article 165."
    },
    # 30
    {
        "stem_en": "Does the Constitution prescribe any minimum age or maximum retirement age for the Attorney General of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞருக்கு ஏதேனும் குறைந்தபட்ச வயது அல்லது ஓய்வுபெறும் அதிகபட்ச வயதை அரசியலமைப்பு நிர்ணயித்துள்ளதா?",
        "options": [("Yes, retirement at 65 years", "ஆம், 65 வயதில் ஓய்வு"), ("No, the Constitution prescribes neither a minimum age nor an upper age limit", "இல்லை, அரசியலமைப்பு குறைந்தபட்ச வயதையோ அல்லது ஓய்வுபெறும் உச்ச வரம்பையோ நிர்ணயிக்கவில்லை"), ("Yes, retirement at 62 years", "ஆம், 62 வயதில் ஓய்வு"), ("Minimum age of 35 years and maximum of 70 years", "குறைந்தபட்சம் 35 வயது மற்றும் அதிகபட்சம் 70 வயது")],
        "correct_idx": 1,
        "exp_en": "The Constitution does not specify any minimum age or retirement age for the Attorney General. He holds office during the pleasure of the President.",
        "exp_ta": "தலைமை வழக்கறிஞருக்கு குறைந்தபட்ச வயதையோ அல்லது அதிகபட்ச ஓய்வுபெறும் வயதையோ அரசியலமைப்பு குறிப்பிடவில்லை. அவர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிக்கிறார்.",
        "tip": "Supreme Court judges retire at 65, but this retirement age does NOT apply to the Attorney General.",
        "fact": "K.K. Venugopal served as Attorney General until the age of 91."
    },
    # 31
    {
        "stem_en": "Under the Law Officers (Conditions of Service) Rules 1987, what is the usual term for which an Attorney General is initially appointed by the Union Government?",
        "stem_ta": "1987 சட்ட அதிகாரிகள் விதிகளின் கீழ், மத்திய அரசால் ஒரு தலைமை வழக்கறிஞர் வழக்கமாக ஆரம்பத்தில் எத்தனை ஆண்டு காலத்திற்கு நியமிக்கப்படுகிறார்?",
        "options": [("5 years", "5 ஆண்டுகள்"), ("3 years", "3 ஆண்டுகள்"), ("6 years", "6 ஆண்டுகள்"), ("1 year only", "1 ஆண்டு மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "While the Constitution specifies no tenure, the executive terms of appointment under Law Officers Rules typically specify an initial term of 3 years, extendable at the discretion of the Government.",
        "exp_ta": "அரசியலமைப்பு பதவிக்காலத்தை குறிப்பிடாத போதிலும், நிர்வாக விதிகளின் கீழ் வழக்கமாக ஆரம்பத்தில் 3 ஆண்டு காலத்திற்கு நியமிக்கப்பட்டு பின்னர் நீட்டிக்கப்படுகிறது.",
        "tip": "Constitutional tenure = Pleasure of President; Administrative notification = usually 3 years.",
        "fact": "K.K. Venugopal received multiple one-year extensions after his initial 3-year term."
    },
    # 32
    {
        "stem_en": "Which of the following bodies is the Attorney General of India an ex-officio member of?",
        "stem_ta": "கீழ்க்கண்ட எந்த அமைப்பில் இந்திய தலைமை வழக்கறிஞர் பதவிவழி (Ex-officio) உறுப்பினராக உள்ளார்?",
        "options": [("Law Commission of India", "இந்திய சட்ட ஆணையம்"), ("Bar Council of India (BCI)", "இந்திய பார் கவுன்சில் (BCI)"), ("UPSC", "UPSC"), ("Finance Commission", "நிதி ஆணையம்")],
        "correct_idx": 1,
        "exp_en": "Under Section 4(1)(a) of the Advocates Act 1961, the Attorney General of India is an ex-officio member of the Bar Council of India.",
        "exp_ta": "1961 வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 4(1)(a)-ன் கீழ், இந்திய தலைமை வழக்கறிஞர் இந்திய பார் கவுன்சிலின் (BCI) பதவிவழி உறுப்பினராக உள்ளார்.",
        "tip": "The Solicitor General is also an ex-officio member of the Bar Council of India under Section 4(1)(b).",
        "fact": "He represents the interests of the legal profession and judiciary."
    },
    # 33
    {
        "stem_en": "Can the Attorney General of India give legal advice to private parties against whom the Government of India is in litigation?",
        "stem_ta": "இந்திய அரசாங்கம் வழக்காடும் வழக்குகளில் சம்பந்தப்பட்ட தனியார் நபர்களுக்கு இந்திய தலைமை வழக்கறிஞர் சட்ட ஆலோசனை வழங்க முடியுமா?",
        "options": [("Yes, if paid private fee", "ஆம், கட்டணம் பெற்றால்"), ("No, he is strictly prohibited from advising or holding briefs against the Government of India", "இல்லை, இந்திய அரசாங்கத்திற்கு எதிராக ஆலோசனை வழங்கவோ ஆஜராகவோ அவருக்கு கடுமையான தடை உள்ளது"), ("Only with court permission", "நீதிமன்ற அனுமதியுடன் மட்டுமே"), ("Only after Parliament approves", "நாடாளுமன்றம் ஒப்புதல் அளித்த பிறகு மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "The Attorney General is strictly prohibited from advising or holding briefs against the Government of India in any court or tribunal.",
        "exp_ta": "எந்தவொரு நீதிமன்றத்திலும் அல்லது தீர்ப்பாயத்திலும் இந்திய அரசாங்கத்திற்கு எதிராக ஆலோசனை வழங்கவோ அல்லது வாதாடவோ தலைமை வழக்கறிஞருக்கு முழுமையான தடை உள்ளது.",
        "tip": "Fundamental ethical limitation to prevent conflict of interest.",
        "fact": "He also cannot advise any party in a case where he is likely to be called upon to advise GoI."
    },
    # 34
    {
        "stem_en": "Who among the following was the Attorney General of India during the declaration of Internal Emergency in 1975?",
        "stem_ta": "1975-ல் உள்நாட்டு அவசரநிலை பிரகடனம் செய்யப்பட்ட போது இந்தியாவின் தலைமை வழக்கறிஞராக இருந்தவர் யார்?",
        "options": [("M.C. Setalvad", "எம்.சி. செதல்வாட்"), ("Niren De", "நிரேன் டே"), ("Soli Sorabjee", "சோலி சோராப்ஜி"), ("Fali S. Nariman", "பாலி எஸ். நாரிமன்")],
        "correct_idx": 1,
        "exp_en": "Niren De was the Attorney General of India from November 1968 to March 1977, representing the Indira Gandhi government in the infamous ADM Jabalpur (Habeas Corpus) case during the Emergency.",
        "exp_ta": "நிரேன் டே 1968 முதல் 1977 வரை தலைமை வழக்கறிஞராக இருந்தார்; அவசரநிலைக் காலத்தில் வரலாற்று முக்கியத்துவம் வாய்ந்த ஏடிஎம் ஜபல்பூர் வழக்கில் இந்திரா காந்தி அரசுக்காக வாதாடினார்.",
        "tip": "Fali S. Nariman was the Additional Solicitor General who resigned in protest when Emergency was declared.",
        "fact": "Niren De argued that during Emergency, citizens could not enforce Article 21 even in cases of unlawful deprivation of life."
    },
    # 35
    {
        "stem_en": "Under Section 15 of the Contempt of Courts Act 1971, whose prior written consent is required for a private citizen to initiate criminal contempt proceedings in the Supreme Court?",
        "stem_ta": "1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் பிரிவு 15-ன் கீழ், ஒரு தனிநபர் உச்ச நீதிமன்றத்தில் குற்றவியல் அவமதிப்பு வழக்கை தொடர யாருடைய எழுத்துப்பூர்வ முன்ஒப்புதல் அவசியம்?",
        "options": [("Chief Justice of India", "இந்திய தலைமை நீதிபதி"), ("Attorney General of India (or Solicitor General)", "இந்திய தலைமை வழக்கறிஞர் (அல்லது சொலிசிட்டர் ஜெனரல்)"), ("Union Law Minister", "மத்திய சட்ட அமைச்சர்"), ("President of India", "இந்திய குடியரசுத் தலைவர்")],
        "correct_idx": 1,
        "exp_en": "Under Section 15(1)(b) of the Contempt of Courts Act 1971, a motion for criminal contempt in the Supreme Court moved by any other person requires the prior consent in writing of the Attorney General (or Solicitor General).",
        "exp_ta": "1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் பிரிவு 15(1)(b)-ன் கீழ், உச்ச நீதிமன்றத்தில் குற்றவியல் நீதிமன்ற அவமதிப்பு வழக்கை தொடர தலைமை வழக்கறிஞரின் (அல்லது சொலிசிட்டர் ஜெனரல்) எழுத்துப்பூர்வ முன்ஒப்புதல் கட்டாயமாகும்.",
        "tip": "High Court criminal contempt requires consent of Advocate General of the State.",
        "fact": "This statutory filter prevents frivolous contempt petitions from wasting the Supreme Court's time."
    },
    # 36
    {
        "stem_en": "By constitutional convention, when does the Attorney General of India generally resign from his office?",
        "stem_ta": "அரசியலமைப்பு மரபுப்படி, இந்திய தலைமை வழக்கறிஞர் பொதுவாக எப்போது தனது பதவியை ராஜினாமா செய்கிறார்?",
        "options": [
            ("Every 5 years automatically", "ஒவ்வொரு 5 ஆண்டிற்கும் தானாக"),
            ("When the Council of Ministers (Government) resigns or is replaced", "மத்திய அமைச்சரவை (அரசாங்கம்) பதவி விலகும் போது அல்லது புதிய அரசு அமையும் போது"),
            ("When the Chief Justice of India retires", "இந்திய தலைமை நீதிபதி ஓய்வுபெறும் போது"),
            ("When the Lok Sabha Speaker is changed", "மக்களவை சபாநாயகர் மாற்றப்படும் போது")
        ],
        "correct_idx": 1,
        "exp_en": "By convention, the Attorney General resigns when the government (the council of ministers) resigns or is replaced, as he is appointed on its advice to act as its legal counsel.",
        "exp_ta": "அரசியலமைப்பு மரபுப்படி, ஒரு அரசாங்கம் பதவி விலகும் போதோ அல்லது புதிய அரசு பொறுப்பேற்கும் போதோ தலைமை வழக்கறிஞரும் தனது பதவியை ராஜினாமா செய்கிறார்.",
        "tip": "Since he is appointed on the advice of the outgoing ministry, a new ministry appoints its own trusted legal advisor.",
        "fact": "However, the incoming government has the option to reappoint or continue the existing Attorney General."
    },
    # 37
    {
        "stem_en": "Is the salary and remuneration of the Attorney General of India charged upon the Consolidated Fund of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞரின் ஊதியம் இந்திய தொகுப்பு நிதியில் 'சுமத்தப்பட்ட' (Charged) செலவினமா?",
        "options": [("Yes, under Article 112(3)", "ஆம், சரத்து 112(3)-ன் கீழ்"), ("No, it is not charged upon the Consolidated Fund of India (it is voted by Parliament)", "இல்லை, இது இந்திய தொகுப்பு நிதியில் சுமத்தப்பட்ட செலவினம் அல்ல (நாடாளுமன்றத்தால் வாக்களிக்கப்படும் செலவு)"), ("Charged only during war", "போர்க் காலத்தில் மட்டுமே சுமத்தப்படும்"), ("Paid from Contingency Fund", "அவசரக்கால நிதியிலிருந்து வழங்கப்படுகிறது")],
        "correct_idx": 1,
        "exp_en": "Unlike the salaries of SC Judges, CAG, and UPSC members, the remuneration of the Attorney General is NOT charged upon the Consolidated Fund of India under Article 112(3); it is part of the voted budget of the Law Ministry.",
        "exp_ta": "உச்ச நீதிமன்ற நீதிபதிகள், CAG ஆகியோரின் ஊதியம் போலன்றி, தலைமை வழக்கறிஞரின் ஊதியம் சரத்து 112(3)-ன் கீழ் இந்திய தொகுப்பு நிதியில் சுமத்தப்பட்ட செலவு அல்ல; இது நாடாளுமன்றத்தால் வாக்களிக்கப்படும் செலவினமாகும்.",
        "tip": "High-yield trap: CAG and SC judge salaries are CHARGED; Attorney General remuneration is NOT charged.",
        "fact": "This reflects that the AG holds office during pleasure, unlike independent constitutional watchdogs."
    },
    # 38
    {
        "stem_en": "In which landmark 1978 judgment did Attorney General S.V. Gupte argue for the Union of India regarding personal liberty under Article 21?",
        "stem_ta": "1978-ல் எந்த வரலாற்று சிறப்புமிக்க வழக்கில் சரத்து 21-ன் கீழான தனிநபர் சுதந்திரம் தொடர்பாக மத்திய அரசுக்காக தலைமை வழக்கறிஞர் எஸ்.வி. குப்தே வாதாடினார்?",
        "options": [("Kesavananda Bharati case", "கேசவானந்த பாரதி வழக்கு"), ("Maneka Gandhi v. Union of India", "மேனகா காந்தி எதிர் இந்திய ஒன்றியம்"), ("Minerva Mills case", "மினர்வா மில்ஸ் வழக்கு"), ("Golaknath case", "கோலக்நாத் வழக்கு")],
        "correct_idx": 1,
        "exp_en": "In the landmark Maneka Gandhi v. Union of India (1978) passport impounding case, Attorney General S.V. Gupte appeared for the Union of India before the 7-judge Constitution Bench.",
        "exp_ta": "1978-ல் பாஸ்போர்ட் முடக்கப்பட்ட மேனகா காந்தி எதிர் இந்திய ஒன்றியம் வழக்கில், 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வின் முன் மத்திய அரசுக்காக தலைமை வழக்கறிஞர் எஸ்.வி. குப்தே ஆஜரானார்.",
        "tip": "Maneka Gandhi expanded Article 21 to include 'due process of law'.",
        "fact": "S.V. Gupte served as AG during the Janata Party government headed by Morarji Desai."
    },
    # 39
    {
        "stem_en": "Can the Attorney General of India be a member of any political party while holding office?",
        "stem_ta": "பதவியில் இருக்கும் போது இந்திய தலைமை வழக்கறிஞர் ஏதேனும் ஓர் அரசியல் கட்சியில் உறுப்பினராக இருக்க முடியுமா?",
        "options": [("Yes, mandatory requirement", "ஆம், கட்டாயத் தேவை"), ("There is no constitutional bar, but by strong convention and professional propriety, the AG functions as an apolitical legal officer", "அரசியலமைப்பு தடை எதுவும் இல்லை, ஆனால் மரபுப்படி அவர் அரசியல் சார்பற்ற சட்ட அதிகாரியாகவே செயல்படுகிறார்"), ("Must be a sitting Lok Sabha MP", "அவர் மக்களவை எம்.பி-யாக இருக்க வேண்டும்"), ("Must belong to the ruling party", "ஆளும் கட்சியைச் சேர்ந்தவராக இருக்க வேண்டும்")],
        "correct_idx": 1,
        "exp_en": "The Constitution contains no disqualification regarding party membership, but by established tradition and judicial ethics, the Attorney General operates as a non-political senior jurist representing the Republic.",
        "exp_ta": "அரசியல் கட்சி உறுப்பினர் தொடர்பாக அரசியலமைப்பில் வெளிப்படையான தடை இல்லை என்றாலும், மரபுப்படி தலைமை வழக்கறிஞர் அரசியல் சார்பின்றி குடியரசின் சட்ட அதிகாரியாக செயல்படுகிறார்.",
        "tip": "Unlike the UK where the Attorney General is an elected politician and MP, in India he is an apolitical jurist.",
        "fact": "Top senior advocates of the Bar are traditionally appointed regardless of formal party affiliation."
    },
    # 40
    {
        "stem_en": "Who represents the Government of India in litigation before the Supreme Court under Article 131 (Original Jurisdiction suits between Centre and States)?",
        "stem_ta": "மத்திய-மாநில அரசுகளுக்கு இடையிலான அசல் அதிகார வரம்பு (சரத்து 131) வழக்குகளில் உச்ச நீதிமன்றத்தில் இந்திய அரசின் சார்பில் ஆஜராகி வாதாடுபவர் யார்?",
        "options": [("Union Home Minister", "மத்திய உள்துறை அமைச்சர்"), ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"), ("Law Secretary", "சட்ட செயலாளர்"), ("Cabinet Secretary", "கேபினட் செயலாளர்")],
        "correct_idx": 1,
        "exp_en": "Under Article 76 and presidential instructions, the Attorney General represents the Union of India in all Article 131 constitutional disputes instituted in the Supreme Court between the Union and one or more States.",
        "exp_ta": "சரத்து 76 மற்றும் குடியரசுத் தலைவரின் உத்தரவுகளின்படி, மத்திய-மாநில அரசுகளுக்கு இடையிலான சரத்து 131 அசல் அதிகார வரம்பு வழக்குகளில் இந்திய அரசின் சார்பில் தலைமை வழக்கறிஞர் ஆஜராகிறார்.",
        "tip": "Article 131 covers exclusive original disputes between Centre and States in Supreme Court.",
        "fact": "State Governments are represented in such suits by their respective Advocates General."
    },
    # 41
    {
        "stem_en": "Can the Attorney General of India be removed from office on the ground of 'proved misbehaviour or incapacity' through Parliamentary impeachment?",
        "stem_ta": "நாடாளுமன்ற கண்டனத் தீர்மானத்தின் மூலம் 'நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது இயலாமை' என்ற அடிப்படையில் இந்திய தலைமை வழக்கறிஞரை பதவியிலிருந்து நீக்க முடியுமா?",
        "options": [("Yes, exactly like a Supreme Court Judge", "ஆம், உச்ச நீதிமன்ற நீதிபதியைப் போல சரியாக அதே முறையில்"), ("No, he holds office during the pleasure of the President and can be removed at any time without impeachment", "இல்லை, அவர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் இருப்பதால் கண்டனத் தீர்மானம் இன்றி எந்நேரத்திலும் நீக்கப்படலாம்"), ("Only with the approval of both Houses by simple majority", "இரு அவைகளின் எளிய பெரும்பான்மை ஒப்புதலுடன் மட்டுமே"), ("Only after judicial inquiry by CJI", "தலைமை நீதிபதியின் விசாரணைக்குப் பிறகு மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "The Attorney General does NOT enjoy security of tenure like a Supreme Court judge or CAG. Under Article 76(4), he holds office during the pleasure of the President and can be removed at any time without any parliamentary process.",
        "exp_ta": "தலைமை வழக்கறிஞருக்கு உச்ச நீதிமன்ற நீதிபதி அல்லது CAG போல பதவிப் பாதுகாப்பு இல்லை. சரத்து 76(4)-ன் படி அவர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் இருப்பதால், நாடாளுமன்ற கண்டனத் தீர்மானம் இன்றி எந்நேரத்திலும் நீக்கப்படலாம்.",
        "tip": "Pleasure doctrine governs AG; Impeachment governs SC Judges, CAG, and CEC.",
        "fact": "No grounds of removal are specified in Article 76."
    },
    # 42
    {
        "stem_en": "Which constitutional officer of a State corresponds at the state level to the Attorney General of India at the Union level?",
        "stem_ta": "மத்திய அளவில் உள்ள இந்திய தலைமை வழக்கறிஞருக்கு (AG) இணையாக மாநில அளவில் செயல்படும் அரசியலமைப்பு அதிகாரி யார்?",
        "options": [("Public Prosecutor", "அரசு வழக்கறிஞர் (Public Prosecutor)"), ("Advocate General of the State", "மாநில தலைமை வழக்கறிஞர் (அட்வகேட் ஜெனரல்)"), ("Government Pleader", "அரசு பிளீடர் (Government Pleader)"), ("State Law Secretary", "மாநில சட்ட செயலாளர்")],
        "correct_idx": 1,
        "exp_en": "Under Article 165 of the Constitution, the Advocate General of the State corresponds to the Attorney General of India at the state level.",
        "exp_ta": "அரசியலமைப்பின் சரத்து 165-ன் கீழ் உள்ள மாநில தலைமை வழக்கறிஞர் (Advocate General), மத்திய அளவில் உள்ள அட்டர்னி ஜெனரலுக்கு இணையான மாநில அரசியலமைப்பு அதிகாரியாவார்.",
        "tip": "Union: Article 76 (Attorney General) <---> State: Article 165 (Advocate General).",
        "fact": "Both share parallel rights to participate in legislative proceedings without voting rights (Art 88 vs Art 177)."
    },
    # 43
    {
        "stem_en": "Under which Article of the Constitution does the Advocate General of a State have rights in the State Legislature parallel to the Attorney General's rights under Article 88?",
        "stem_ta": "சரத்து 88-ன் கீழ் அட்டர்னி ஜெனரலுக்கு உள்ள உரிமைகளுக்கு இணையாக, மாநில சட்டமன்றத்தில் மாநில தலைமை வழக்கறிஞருக்கு உரிமை வழங்கும் சரத்து எது?",
        "options": [("Article 165", "சரத்து 165"), ("Article 177", "சரத்து 177"), ("Article 194", "சரத்து 194"), ("Article 213", "சரத்து 213")],
        "correct_idx": 1,
        "exp_en": "Article 177 gives the Advocate General the right to speak and take part in the proceedings of the State Legislative Assembly (and Legislative Council) without the right to vote, mirroring Article 88 for the Attorney General.",
        "exp_ta": "சரத்து 177, மாநில தலைமை வழக்கறிஞருக்கு சட்டமன்றத்தில் வாக்களிக்கும் உரிமையின்றி பேசவும் பங்கேற்கவும் உரிமை அளிக்கிறது; இது மத்திய அளவில் சரத்து 88-க்கு இணையானது.",
        "tip": "Art 88 (Union Attorney General in Parliament) <---> Art 177 (State Advocate General in Legislature).",
        "fact": "Both articles prohibit voting by the law officer in the legislative body."
    },
    # 44
    {
        "stem_en": "Who among the following distinguished jurists served twice as the Attorney General of India (1989-1990 and 1998-2004)?",
        "stem_ta": "கீழ்க்கண்ட சிறந்த சட்ட வல்லுநர்களில் இருமுறை (1989-1990 மற்றும் 1998-2004) இந்திய தலைமை வழக்கறிஞராக பணியாற்றியவர் யார்?",
        "options": [("M.C. Setalvad", "எம்.சி. செதல்வாட்"), ("Soli Sorabjee", "சோலி சோராப்ஜி"), ("Mukul Rohatgi", "முகுல் ரோஹத்கி"), ("Fali S. Nariman", "பாலி எஸ். நாரிமன்")],
        "correct_idx": 1,
        "exp_en": "Soli Jehangir Sorabjee served as the Attorney General of India twice: first from December 1989 to December 1990 under V.P. Singh, and second from April 1998 to June 2004 under Atal Bihari Vajpayee.",
        "exp_ta": "சோலி சோராப்ஜி இருமுறை இந்திய தலைமை வழக்கறிஞராக பணியாற்றினார்: முதலில் 1989-1990-ல் வி.பி. சிங் ஆட்சியில், பின்னர் 1998-2004-ல் வாஜ்பாய் ஆட்சியில்.",
        "tip": "Milon K. Banerjee also served two non-consecutive terms (1992-1996 and 2004-2009).",
        "fact": "Soli Sorabjee was awarded the Padma Vibhushan in 2002 for his defence of freedom of speech."
    },
    # 45
    {
        "stem_en": "Which Attorney General of India appeared for the Union in the historic 13-judge Kesavananda Bharati case (1973)?",
        "stem_ta": "1973-ல் வரலாற்று சிறப்புமிக்க 13 நீதிபதிகள் கொண்ட கேசவானந்த பாரதி வழக்கில் மத்திய அரசுக்காக ஆஜரான இந்திய தலைமை வழக்கறிஞர் யார்?",
        "options": [("M.C. Setalvad", "எம்.சி. செதல்வாட்"), ("Niren De", "நிரேன் டே"), ("C.K. Daphtary", "சி.கே. தப்தாரி"), ("K. Parasaran", "கே. பராசரன்")],
        "correct_idx": 1,
        "exp_en": "Attorney General Niren De appeared for the Union of India in Kesavananda Bharati v. State of Kerala (1973) alongside Solicitor General Lal Narayan Sinha.",
        "exp_ta": "1973-ல் கேசவானந்த பாரதி வழக்கில் இந்திய அரசுக்காக தலைமை வழக்கறிஞர் நிரேன் டே மற்றும் சொலிசிட்டர் ஜெனரல் லால் நாராயண் சின்ஹா ஆகியோர் ஆஜரானார்கள்.",
        "tip": "N.A. Palkhivala argued for Kesavananda Bharati; Niren De argued for the Union of India.",
        "fact": "The 13-judge bench established the Basic Structure doctrine by a narrow 7:6 majority."
    },
    # 46
    {
        "stem_en": "Which veteran jurist from Tamil Nadu served as the Attorney General of India under Prime Ministers Indira Gandhi and Rajiv Gandhi (1983-1989)?",
        "stem_ta": "பிரதமர்கள் இந்திரா காந்தி மற்றும் ராஜீவ் காந்தியின் ஆட்சிக் காலத்தில் (1983-1989) இந்திய தலைமை வழக்கறிஞராக பணியாற்றிய தமிழ்நாட்டைச் சேர்ந்த மூத்த சட்ட வல்லுநர் யார்?",
        "options": [("Alladi Krishnaswamy Iyer", "அல்லாடி கிருஷ்ணசாமி ஐயர்"), ("K. Parasaran", "கே. பராசரன்"), ("V. Bhashyam Aiyangar", "வி. பாஷ்யம் ஐயங்கார்"), ("P.S. Sivaswami Iyer", "பி.எஸ். சிவசாமி ஐயர்")],
        "correct_idx": 1,
        "exp_en": "Senior Advocate K. Parasaran, from Tamil Nadu, served as the 9th Attorney General of India from 1983 to 1989, previously serving as Advocate General of Tamil Nadu (1976-1977) and Solicitor General (1980-1983).",
        "exp_ta": "தமிழ்நாட்டைச் சேர்ந்த மூத்த வழக்கறிஞர் கே. பராசரன் 1983 முதல் 1989 வரை இந்தியாவின் 9-வது தலைமை வழக்கறிஞராக பணியாற்றினார்; அதற்கு முன் தமிழ்நாடு அட்வகேட் ஜெனரலாகவும் பணியாற்றினார்.",
        "tip": "Known as the 'Pitamaha' of the Indian Bar; was awarded Padma Bhushan and Padma Vibhushan.",
        "fact": "He successfully represented the deity in the landmark Ayodhya Ram Janmabhoomi title dispute in 2019."
    },
    # 47
    {
        "stem_en": "What is the primary function of the Additional Solicitors General of India?",
        "stem_ta": "இந்திய கூடுதல் சொலிசிட்டர் ஜெனரல்களின் (ASG) முதன்மையான பணி என்ன?",
        "options": [
            ("To supervise the state police forces", "மாநில காவல் படைகளை மேற்பார்வையிடுவது"),
            ("To assist the Attorney General and Solicitor General in conducting litigation on behalf of the Union of India in the Supreme Court and High Courts", "உச்ச நீதிமன்றம் மற்றும் உயர்நீதிமன்றங்களில் இந்திய அரசு சார்பிலான வழக்குகளை நடத்துவதில் தலைமை வழக்கறிஞர் மற்றும் சொலிசிட்டர் ஜெனரலுக்கு உதவுவது"),
            ("To audit government accounts", "அரசு கணக்குகளை தணிக்கை செய்வது"),
            ("To act as election observers", "தேர்தல் பார்வையாளர்களாக செயல்படுவது")
        ],
        "correct_idx": 1,
        "exp_en": "Additional Solicitors General (ASG) assist the Attorney General and Solicitor General in handling the massive volume of government litigation in the Supreme Court and various High Court benches.",
        "exp_ta": "உச்ச நீதிமன்றம் மற்றும் பல்வேறு உயர்நீதிமன்றங்களில் இந்திய அரசு தொடர்பான வழக்குகளை நடத்துவதில் தலைமை வழக்கறிஞர் மற்றும் சொலிசிட்டர் ஜெனரலுக்கு கூடுதல் சொலிசிட்டர் ஜெனரல்கள் உதவுகின்றனர்.",
        "tip": "ASGs are stationed at the Supreme Court in New Delhi and at various High Courts (e.g., Madras, Bombay, Calcutta).",
        "fact": "They are non-constitutional law officers appointed by the central government."
    },
    # 48
    {
        "stem_en": "In the performance of his constitutional duties, does the Attorney General of India have the right to take part in joint sittings of Parliament?",
        "stem_ta": "தனது அரசியலமைப்பு பணிகளை ஆற்றுவதில், நாடாளுமன்றத்தின் கூட்டு அமர்வுகளில் (Joint Sitting) பங்கேற்கும் உரிமை இந்திய தலைமை வழக்கறிஞருக்கு உண்டா?",
        "options": [("No, joint sittings are restricted to MPs only", "இல்லை, கூட்டு அமர்வு எம்.பி-க்களுக்கு மட்டுமே"), ("Yes, under Article 88 he has the right to speak and take part in any joint sitting of the Houses", "ஆம், சரத்து 88-ன் கீழ் அவைகளின் எந்தவொரு கூட்டு அமர்விலும் பேசவும் பங்கேற்கவும் அவருக்கு உரிமை உண்டு"), ("Only if invited by the Speaker", "சபாநாயகர் அழைத்தால் மட்டுமே"), ("Only during financial crisis", "நிதி நெருக்கடியின் போது மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "Article 88 explicitly mentions that the Attorney General has the right to speak in, and otherwise take part in the proceedings of, 'any joint sitting of the Houses', though he cannot vote.",
        "exp_ta": "சரத்து 88, நாடாளுமன்றத்தின் இரு அவைகளின் 'கூட்டு அமர்விலும்' தலைமை வழக்கறிஞர் பேசவும் பங்கேற்கவும் உரிமை உண்டு என்று வெளிப்படையாக கூறுகிறது (ஆனால் வாக்களிக்க முடியாது).",
        "tip": "Article 108 governs Joint Sittings; Article 88 gives the AG the right of audience therein.",
        "fact": "He can address the joint sitting to explain complex constitutional questions."
    },
    # 49
    {
        "stem_en": "Is the advice tendered by the Attorney General of India binding on the Government of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞர் வழங்கும் சட்ட ஆலோசனை இந்திய அரசாங்கத்தை கட்டுப்படுத்துமா?",
        "options": [("Yes, strictly binding under Article 76", "ஆம், சரத்து 76-ன் கீழ் கட்டாயமாக கட்டுப்படுத்தும்"), ("No, his advice is consultative and advisory in nature and not legally binding", "இல்லை, அவரது ஆலோசனை வெறும் ஆலோசனை தன்மை கொண்டது மட்டுமே; சட்டப்படி அரசை கட்டுப்படுத்தாது"), ("Binding only in criminal matters", "குற்றவியல் விவகாரங்களில் மட்டுமே கட்டுப்படுத்தும்"), ("Binding only if endorsed by CJI", "தலைமை நீதிபதி ஒப்புதல் அளித்தால் மட்டுமே")],
        "correct_idx": 1,
        "exp_en": "The opinions and advice rendered by the Attorney General are purely advisory in nature and are not legally binding on the Government of India or the Cabinet.",
        "exp_ta": "தலைமை வழக்கறிஞர் வழங்கும் சட்ட ஆலோசனைகள் வெறும் ஆலோசனை வடிவமே ஆகும்; அவை இந்திய அரசாங்கத்தையோ அல்லது அமைச்சரவையையோ சட்டப்பூர்வமாக கட்டுப்படுத்தாது.",
        "tip": "The government is free to take a different legal course or seek alternative opinions.",
        "fact": "The government may also consult the Solicitor General or private senior advocates."
    },
    # 50
    {
        "stem_en": "Who among the following was the only Attorney General of India to have also served as a Judge of the Supreme Court of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞராகவும் பணியாற்றி, பின்னர் உச்ச நீதிமன்ற நீதிபதியாகவும் பணியாற்றிய ஒரே நபர் யார்?",
        "options": [("M.C. Setalvad", "எம்.சி. செதல்வாட்"), ("None, no Attorney General has later become a Supreme Court Judge (though N. Santosh Hegde went from SG to SC Judge)", "எவருமில்லை, எந்த தலைமை வழக்கறிஞரும் பின்னர் உச்ச நீதிமன்ற நீதிபதியாகவில்லை (ஆனால் சந்தோஷ் ஹெக்டே சொலிசிட்டர் ஜெனரலிலிருந்து உச்ச நீதிமன்ற நீதிபதியானார்)"), ("K. Parasaran", "கே. பராசரன்"), ("Soli Sorabjee", "சோலி சோராப்ஜி")],
        "correct_idx": 1,
        "exp_en": "No Attorney General of India has ever subsequently served as a Judge of the Supreme Court of India. (However, Solicitor General N. Santosh Hegde was directly elevated from Solicitor General to Supreme Court Judge in 1999).",
        "exp_ta": "இந்திய வரலாற்றில் தலைமை வழக்கறிஞராக இருந்த எவரும் பின்னர் உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட்டதில்லை (இருப்பினும் சொலிசிட்டர் ஜெனரலாக இருந்த என். சந்தோஷ் ஹெக்டே நேரடியாக உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட்டார்).",
        "tip": "Classic TNPSC trap: While AG must be qualified to be a SC Judge, no AG has actually served as a SC Judge.",
        "fact": "M.C. Setalvad declined elevation to the Supreme Court as a judge, preferring to remain at the Bar."
    }
]

def build_ag_easy():
    questions = []
    for i, item in enumerate(raw_easy_data):
        qid = f"AG_E_{i+1:03d}"
        opts = item["options"]
        correct_idx = item["correct_idx"]
        correct_key = ["A", "B", "C", "D"][correct_idx]
        
        why_en = {}
        why_ta = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if idx == correct_idx:
                why_en[key] = f"Option {key} is the correct constitutional provision under Article 76 / 88."
                why_ta[key] = f"அரசியலமைப்பு சரத்து 76 / 88-ன் கீழ் தெரிவு {key} சரியான விடையாகும்."
            else:
                why_en[key] = f"Option {key} ({opts[idx][0]}) is incorrect."
                why_ta[key] = f"தெரிவு {key} ({opts[idx][1]}) தவறானது."
                
        q = make_ag_q(
            qid=qid,
            diff="Easy",
            qtype="Single Choice",
            subtopic="Constitutional Framework of Attorney General",
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
            tags=["polity", "attorney_general_of_india", "easy"]
        )
        questions.append(q)
    return questions

def main():
    questions = build_ag_easy()
    print(f"Generated {len(questions)} raw Easy questions.")
    
    # Balance keys to 13 B, 12 C, 12 D, 13 A
    balanced = balance_question_keys(questions, {"A": 13, "B": 13, "C": 12, "D": 12})
    
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "attorney_general_easy.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, indent=2, ensure_ascii=False)
        
    print(f"Saved balanced Easy MCQs to {out_file}")
    
    validator = ContentValidator()
    report = validator.validate_file(out_file, expected_count=50, expected_prefix="AG_E_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
    if not report.is_valid:
        for iss in report.issues:
            print("Issue:", iss.message)

if __name__ == "__main__":
    main()
