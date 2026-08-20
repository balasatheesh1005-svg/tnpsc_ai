# -*- coding: utf-8 -*-
"""
Generator Script for 50 TNPSC Group 1 Standard PYQ Practice MCQs
Topic: Preamble of the Constitution of India
Target Output:
  - data/questions/polity/preamble_pyq.json
  - data/questions/polity/preamble_pyq_practice.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

raw_questions = [
    # 1 (A)
    {
        "q_en": "Which date is explicitly mentioned in the Preamble of the Constitution of India as the date of its adoption, enactment, and giving to themselves?",
        "q_ta": "இந்திய அரசியலமைப்பின் முகவுரையில் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட, இயற்றப்பட்ட மற்றும் நமக்கு நாமே வழங்கப்பட்ட நாளாக வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ள தேதி எது?",
        "opts": [
            {"id": "A", "en": "26th November 1949", "ta": "26 நவம்பர் 1949"},
            {"id": "B", "en": "26th January 1950", "ta": "26 ஜனவரி 1950"},
            {"id": "C", "en": "15th August 1947", "ta": "15 ஆகஸ்ட் 1947"},
            {"id": "D", "en": "9th December 1946", "ta": "9 டிசம்பர் 1946"}
        ],
        "ans": "A",
        "exp_en": "The Preamble concludes with: '...in our Constituent Assembly this twenty-sixth day of November, 1949, do hereby adopt, enact and give to ourselves this Constitution.'",
        "exp_ta": "முகவுரையின் இறுதியில்: '...1949 நவம்பர் இருபத்தாறாம் நாளாகிய இன்று, நமது அரசியலமைப்பு நிர்ணய அவையில் இந்த அரசியலமைப்பை ஏற்று, இயற்றி, நமக்கு நாமே வழங்கிக் கொள்கிறோம்' எனக் குறிப்பிடப்பட்டுள்ளது.",
        "tip_en": "Date of Adoption = Nov 26, 1949; Date of Commencement = Jan 26, 1950.",
        "tip_ta": "ஏற்றுக்கொள்ளப்பட்ட தேதி = நவம்பர் 26, 1949; நடைமுறைக்கு வந்த தேதி = ஜனவரி 26, 1950.",
        "fact_en": "Nov 26 is celebrated as Constitution Day (Samvidhan Divas) in India since 2015.",
        "fact_ta": "நவம்பர் 26 ஆம் தேதி 2015 முதல் இந்தியாவில் அரசியலமைப்பு தினமாக (சம்விதான் திவாஸ்) கொண்டாடப்படுகிறது.",
        "diff": "Easy", "type": "Direct PYQ Pattern"
    },

    # 2 (B)
    {
        "q_en": "The Preamble of the Indian Constitution is based on which historic resolution introduced in the Constituent Assembly?",
        "q_ta": "இந்திய அரசியலமைப்பின் முகவுரை அரசியலமைப்பு நிர்ணய அவையில் அறிமுகப்படுத்தப்பட்ட எந்த வரலாற்றுச் சிறப்புமிக்க தீர்மானத்தை அடிப்படையாகக் கொண்டது?",
        "opts": [
            {"id": "A", "en": "Quit India Resolution", "ta": "வெள்ளையனே வெளியேறு தீர்மானம்"},
            {"id": "B", "en": "Objectives Resolution", "ta": "குறிக்கோள் தீர்மானம்"},
            {"id": "C", "en": "Poorna Swaraj Resolution", "ta": "பூரண சுயராஜ்ய தீர்மானம்"},
            {"id": "D", "en": "Mountbatten Plan", "ta": "மவுண்ட்பேட்டன் திட்டம்"}
        ],
        "ans": "B",
        "exp_en": "The Preamble is based on the 'Objectives Resolution', drafted and moved by Jawaharlal Nehru on December 13, 1946, and adopted on January 22, 1947.",
        "exp_ta": "முகவுரை என்பது பண்டித ஜவஹர்லால் நேருவால் டிசம்பர் 13, 1946 இல் முன்மொழியப்பட்டு ஜனவரி 22, 1947 இல் ஏற்றுக்கொள்ளப்பட்ட 'குறிக்கோள் தீர்மானத்தை' அடிப்படையாகக் கொண்டது.",
        "tip_en": "Objectives Resolution moved = Dec 13, 1946; Adopted = Jan 22, 1947.",
        "tip_ta": "குறிக்கோள் தீர்மானம் முன்மொழியப்பட்டது = டிசம்பர் 13, 1946; ஏற்கப்பட்டது = ஜனவரி 22, 1947.",
        "fact_en": "The modified version of Objectives Resolution forms the present Preamble.",
        "fact_ta": "குறிக்கோள் தீர்மானத்தின் திருத்தப்பட்ட வடிவமே தற்போதைய முகவுரையாக உள்ளது.",
        "diff": "Easy", "type": "Direct PYQ Pattern"
    },

    # 3 (C)
    {
        "q_en": "How many times has the Preamble of the Constitution of India been amended since its enactment in 1949?",
        "q_ta": "1949 இல் இயற்றப்பட்டதிலிருந்து இந்திய அரசியலமைப்பின் முகவுரை இதுவரை எத்தனை முறை திருத்தப்பட்டுள்ளது?",
        "opts": [
            {"id": "A", "en": "Three times", "ta": "மூன்று முறை"},
            {"id": "B", "en": "Two times", "ta": "இரண்டு முறை"},
            {"id": "C", "en": "Only once", "ta": "ஒரே ஒரு முறை மட்டுமே"},
            {"id": "D", "en": "Never amended", "ta": "ஒருபோதும் திருத்தப்படவில்லை"}
        ],
        "ans": "C",
        "exp_en": "The Preamble has been amended only once so far, by the 42nd Constitutional Amendment Act of 1976.",
        "exp_ta": "முகவுரை இதுவரை 1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது.",
        "tip_en": "Preamble amended ONLY ONCE by 42nd Amendment Act 1976.",
        "tip_ta": "முகவுரை 1976-ன் 42வது திருத்தச் சட்டத்தால் ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டது.",
        "fact_en": "42nd Constitutional Amendment Act 1976 added three new words: Socialist, Secular, Integrity.",
        "fact_ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டம் 1976 மூன்று புதிய சொற்களைச் சேர்த்தது: சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு.",
        "diff": "Easy", "type": "Direct PYQ Pattern"
    },

    # 4 (D)
    {
        "q_en": "Which Constitutional Amendment Act inserted the words 'Socialist', 'Secular', and 'Integrity' into the Preamble?",
        "q_ta": "எந்த அரசியலமைப்புத் திருத்தச் சட்டம் 'சமதர்ம' (Socialist), 'மதச்சார்பற்ற' (Secular) மற்றும் 'ஒருமைப்பாடு' (Integrity) ஆகிய சொற்களை முகவுரையில் சேர்த்தது?",
        "opts": [
            {"id": "A", "en": "44th Constitutional Amendment Act, 1978", "ta": "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978"},
            {"id": "B", "en": "24th Constitutional Amendment Act, 1971", "ta": "24வது அரசியலமைப்புத் திருத்தச் சட்டம், 1971"},
            {"id": "C", "en": "86th Constitutional Amendment Act, 2002", "ta": "86வது அரசியலமைப்புத் திருத்தச் சட்டம், 2002"},
            {"id": "D", "en": "42nd Constitutional Amendment Act, 1976", "ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976"}
        ],
        "ans": "D",
        "exp_en": "The 42nd Constitutional Amendment Act, 1976 added three words to the Preamble: 'Socialist', 'Secular', and 'Integrity'.",
        "exp_ta": "1976-ன் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் முகவுரையில் மூன்று சொற்களைச் சேர்த்தது: 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு'.",
        "tip_en": "Mnemonic: SSI = Socialist, Secular, Integrity added by 42nd Amendment in 1976.",
        "tip_ta": "நினைவில் கொள்ள: SSI = சமதர்ம (Socialist), மதச்சார்பற்ற (Secular), ஒருமைப்பாடு (Integrity) - 42வது திருத்தம் 1976.",
        "fact_en": "42nd Amendment is also known as the 'Mini-Constitution'.",
        "fact_ta": "42வது திருத்தம் 'குறு அரசியலமைப்பு' என்றும் அழைக்கப்படுகிறது.",
        "diff": "Easy", "type": "Direct PYQ Pattern"
    },

    # 5 (A)
    {
        "q_en": "What is the correct chronological/textual sequence of the words describing the Nature of the Indian State in the Preamble?",
        "q_ta": "முகவுரையில் இந்திய அரசின் தன்மையை விவரிக்கும் சொற்களின் சரியான உரை வரிசை எது?",
        "opts": [
            {"id": "A", "en": "Sovereign, Socialist, Secular, Democratic, Republic", "ta": "இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு"},
            {"id": "B", "en": "Sovereign, Democratic, Republic, Socialist, Secular", "ta": "இறையாண்மை, ஜனநாயக, குடியரசு, சமதர்ம, மதச்சார்பற்ற"},
            {"id": "C", "en": "Sovereign, Secular, Socialist, Democratic, Republic", "ta": "இறையாண்மை, மதச்சார்பற்ற, சமதர்ம, ஜனநாயக, குடியரசு"},
            {"id": "D", "en": "Socialist, Secular, Sovereign, Democratic, Republic", "ta": "சமதர்ம, மதச்சார்பற்ற, இறையாண்மை, ஜனநாயக, குடியரசு"}
        ],
        "ans": "A",
        "exp_en": "The correct sequence in the present Preamble is: Sovereign, Socialist, Secular, Democratic, Republic (S-S-S-D-R).",
        "exp_ta": "தற்போதைய முகவுரையில் உள்ள சரியான வரிசை: இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு."
    },

    # 6 (B)
    {
        "q_en": "What is the correct sequential order of the core Objectives specified in the Preamble of the Constitution of India?",
        "q_ta": "இந்திய அரசியலமைப்பின் முகவுரையில் குறிப்பிடப்பட்டுள்ள முக்கிய குறிக்கோள்களின் சரியான வரிசை எது?",
        "opts": [
            {"id": "A", "en": "Liberty, Equality, Fraternity, Justice", "ta": "சுதந்திரம், சமத்துவம், சகோதரத்துவம், நீதி"},
            {"id": "B", "en": "Justice, Liberty, Equality, Fraternity", "ta": "நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்"},
            {"id": "C", "en": "Equality, Justice, Liberty, Fraternity", "ta": "சமத்துவம், நீதி, சுதந்திரம், சகோதரத்துவம்"},
            {"id": "D", "en": "Fraternity, Liberty, Equality, Justice", "ta": "சகோதரத்துவம், சுதந்திரம், சமத்துவம், நீதி"}
        ],
        "ans": "B",
        "exp_en": "The correct order of objectives in the Preamble is: Justice, Liberty, Equality, Fraternity (J-L-E-F).",
        "exp_ta": "முகவுரையில் உள்ள குறிக்கோள்களின் சரியான வரிசை: நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்."
    },

    # 7 (C)
    {
        "q_en": "Which eminent jurist and constitutional expert described the Preamble as the 'Identity Card of the Constitution'?",
        "q_ta": "முகவுரையை 'அரசியலமைப்பின் அடையாள அட்டை' என்று வர்ணித்த புகழ்பெற்ற சட்ட வல்லுநர் மற்றும் அரசியலமைப்பு நிபுணர் யார்?",
        "opts": [
            {"id": "A", "en": "Dr. B.R. Ambedkar", "ta": "டாக்டர் பி.ஆர். அம்பேத்கர்"},
            {"id": "B", "en": "K.M. Munshi", "ta": "கே.எம். முன்ஷி"},
            {"id": "C", "en": "N.A. Palkhivala", "ta": "என்.ஏ. பல்கிவாலா"},
            {"id": "D", "en": "Sir Alladi Krishnaswami Iyer", "ta": "சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர்"}
        ],
        "ans": "C",
        "exp_en": "N.A. Palkhivala, an eminent jurist and constitutional expert, called the Preamble the 'Identity Card of the Constitution'.",
        "exp_ta": "புகழ்பெற்ற சட்ட வல்லுநரான என்.ஏ. பல்கிவாலா முகவுரையை 'அரசியலமைப்பின் அடையாள அட்டை' என்று அழைத்தார்."
    },

    # 8 (D)
    {
        "q_en": "Who amongst the following constitutional scholars characterized the Preamble as the 'Horoscope of our Sovereign Democratic Republic'?",
        "q_ta": "பின்வரும் அரசியலமைப்பு அறிஞர்களில் முகவுரையை 'நமது இறையாண்மை கொண்ட ஜனநாயக குடியரசின் ஜாதகம்' என்று வர்ணித்தவர் யார்?",
        "opts": [
            {"id": "A", "en": "Pandit Thakur Das Bhargava", "ta": "பண்டிட் தாக்கூர் தாஸ் பார்கவா"},
            {"id": "B", "en": "Sir Ernest Barker", "ta": "சர் எர்னஸ்ட் பார்கர்"},
            {"id": "C", "en": "Dr. Rajendra Prasad", "ta": "டாக்டர் ராஜேந்திர பிரசாத்"},
            {"id": "D", "en": "Dr. K.M. Munshi", "ta": "டாக்டர் கே.எம். முன்ஷி"}
        ],
        "ans": "D",
        "exp_en": "Dr. K.M. Munshi, a member of the Drafting Committee, described the Preamble as the 'Horoscope of our Sovereign Democratic Republic'.",
        "exp_ta": "வரைவுக் குழுவின் உறுப்பினரான டாக்டர் கே.எம். முன்ஷி முகவுரையை 'நமது இறையாண்மை கொண்ட ஜனநாயக குடியரசின் ஜாதகம்' என்று வர்ணித்தார்."
    },

    # 9 (A)
    {
        "q_en": "In which historic advisory reference case did the Supreme Court explicitly opine that the Preamble is NOT a part of the Constitution?",
        "q_ta": "எந்த வரலாற்றுச் சிறப்புமிக்க ஆலோசனைக் கருத்து வழக்கில் முகவுரை என்பது அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் வெளிப்படையாகக் கூறியது?",
        "opts": [
            {"id": "A", "en": "In re Berubari Union Case (1960)", "ta": "பெருபாரி யூனியன் வழக்கு (1960)"},
            {"id": "B", "en": "Kesavananda Bharati Case (1973)", "ta": "கேசவானந்த பாரதி வழக்கு (1973)"},
            {"id": "C", "en": "Minerva Mills Case (1980)", "ta": "மினர்வா மில்ஸ் வழக்கு (1980)"},
            {"id": "D", "en": "S.R. Bommai Case (1994)", "ta": "எஸ்.ஆர். பொம்மை வழக்கு (1994)"}
        ],
        "ans": "A",
        "exp_en": "In the Berubari Union Reference Case (1960), the Supreme Court opined that the Preamble shows the general purpose behind constitutional provisions, but is NOT a part of the Constitution.",
        "exp_ta": "பெருபாரி யூனியன் வழக்கில் (1960), முகவுரை அரசியலமைப்பு விதிகளின் பொதுவான நோக்கத்தைக் காட்டுகிறது, ஆனால் அது அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் கூறியது."
    },

    # 10 (B)
    {
        "q_en": "In which landmark case did a 13-judge Constitutional Bench of the Supreme Court reject the Berubari opinion and hold that the Preamble IS a part of the Constitution?",
        "q_ta": "எந்த மைல்கல் வழக்கில் உச்ச நீதிமன்றத்தின் 13 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு பெருபாரி கருத்தை நிராகரித்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி தான் என்று தீர்ப்பளித்தது?",
        "opts": [
            {"id": "A", "en": "Golak Nath v. State of Punjab (1967)", "ta": "கோலக் நாத் எதிர் பஞ்சாப் மாநிலம் (1967)"},
            {"id": "B", "en": "Kesavananda Bharati v. State of Kerala (1973)", "ta": "கேசவானந்த பாரதி எதிர் கேரளா மாநிலம் (1973)"},
            {"id": "C", "en": "Maneka Gandhi v. Union of India (1978)", "ta": "மேனகா காந்தி எதிர் இந்திய யூனியன் (1978)"},
            {"id": "D", "en": "S.R. Bommai v. Union of India (1994)", "ta": "எஸ்.ஆர். பொம்மை எதிர் இந்திய யூனியன் (1994)"}
        ],
        "ans": "B",
        "exp_en": "In Kesavananda Bharati Case (1973), the Supreme Court explicitly overruled the Berubari Union opinion and held that the Preamble is a part of the Constitution.",
        "exp_ta": "கேசவானந்த பாரதி வழக்கில் (1973), உச்ச நீதிமன்றம் பெருபாரி அபிப்ராயத்தை வெளிப்படையாக ரத்து செய்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்று தீர்ப்பளித்தது."
    },

    # 11 (C)
    {
        "q_en": "In which landmark judgment did the Supreme Court lay down that Secularism is a part of the 'Basic Structure' of the Indian Constitution?",
        "q_ta": "எந்த மைல்கல் தீர்ப்பில் உச்ச நீதிமன்றம் மதச்சார்பின்மை என்பது இந்திய அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பின்' ஒரு பகுதி என்று அறிவித்தது?",
        "opts": [
            {"id": "A", "en": "Shankari Prasad Case (1951)", "ta": "சங்கரி பிரசாத் வழக்கு (1951)"},
            {"id": "B", "en": "Sajjan Singh Case (1965)", "ta": "சஜ்ஜன் சிங் வழக்கு (1965)"},
            {"id": "C", "en": "S.R. Bommai v. Union of India (1994)", "ta": "எஸ்.ஆர். பொம்மை எதிர் இந்திய யூனியன் (1994)"},
            {"id": "D", "en": "Minerva Mills Case (1980)", "ta": "மினர்வா மில்ஸ் வழக்கு (1980)"}
        ],
        "ans": "C",
        "exp_en": "In S.R. Bommai v. Union of India (1994), a nine-judge bench of the Supreme Court held that Secularism is one of the basic features of the Constitution.",
        "exp_ta": "எஸ்.ஆர். பொம்மை வழக்கில் (1994), 9 நீதிபதிகள் கொண்ட அமர்வு மதச்சார்பின்மை அரசியலமைப்பின் அடிப்படை அம்சங்களில் ஒன்று என்று தீர்ப்பளித்தது."
    },

    # 12 (D)
    {
        "q_en": "In which 1995 judgment did the Supreme Court once again re-affirm that the Preamble is an integral part of the Constitution of India?",
        "q_ta": "எந்த 1995 ஆம் ஆண்டு தீர்ப்பில் உச்ச நீதிமன்றம் முகவுரை இந்திய அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என்பதை மீண்டும் உறுதிப்படுத்தியது?",
        "opts": [
            {"id": "A", "en": "Indira Sawhney Case (1992)", "ta": "இந்திரா சாவ்னி வழக்கு (1992)"},
            {"id": "B", "en": "Vishaka Case (1997)", "ta": "விசாகா வழக்கு (1997)"},
            {"id": "C", "en": "Supreme Court Advocates-on-Record Case (1993)", "ta": "சுப்ரீம் கோர்ட் வழக்கறிஞர்கள் சங்க வழக்கு (1993)"},
            {"id": "D", "en": "LIC of India v. Consumer Education & Research Centre (1995)", "ta": "எல்.ஐ.சி எதிர் நுகர்வோர் கல்வி மற்றும் ஆராய்ச்சி மையம் (1995)"}
        ],
        "ans": "D",
        "exp_en": "In LIC of India Case (1995), the Supreme Court again held that the Preamble is an integral part of the Constitution.",
        "exp_ta": "எல்.ஐ.சி வழக்கில் (1995), முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என்று உச்ச நீதிமன்றம் மீண்டும் தீர்ப்பளித்தது."
    },

    # 13 (A)
    {
        "q_en": "Who is declared as the ultimate source of authority of the Constitution of India in its Preamble?",
        "q_ta": "இந்திய அரசியலமைப்பின் முகவுரையில் அதன் அதிகாரத்தின் இறுதி ஆதாரமாக யார் அறிவிக்கப்பட்டுள்ளனர்?",
        "opts": [
            {"id": "A", "en": "The People of India", "ta": "இந்திய மக்கள்"},
            {"id": "B", "en": "The Parliament of India", "ta": "இந்திய நாடாளுமன்றம்"},
            {"id": "C", "en": "The Supreme Court of India", "ta": "இந்திய உச்ச நீதிமன்றம்"},
            {"id": "D", "en": "The President of India", "ta": "இந்தியக் குடியரசுத் தலைவர்"}
        ],
        "ans": "A",
        "exp_en": "The opening words 'We, the People of India' state that the Constitution derives its authority directly from the people of India.",
        "exp_ta": "'இந்திய மக்களாகிய நாம்' என்ற தொடக்க வார்த்தைகள் அரசியலமைப்பு தனது அதிகாரத்தை நேரடியாக இந்திய மக்களிடமிருந்தே பெறுகிறது என்பதைக் குறிக்கிறது."
    },

    # 14 (B)
    {
        "q_en": "What are the three distinct dimensions of Justice guaranteed in the Preamble of the Constitution of India?",
        "q_ta": "இந்திய அரசியலமைப்பின் முகவுரையில் உத்தரவாதம் அளிக்கப்பட்டுள்ள நீதியின் மூன்று வெவ்வேறான பரிமாணங்கள் எவை?",
        "opts": [
            {"id": "A", "en": "Legal, Executive and Judicial", "ta": "சட்ட, நிர்வாக மற்றும் நீதித் துறை"},
            {"id": "B", "en": "Social, Economic and Political", "ta": "சமூக, பொருளாதார மற்றும் அரசியல்"},
            {"id": "C", "en": "Moral, Cultural and Educational", "ta": "ஒழுக்க, பண்பாட்டு மற்றும் கல்வி"},
            {"id": "D", "en": "Civil, Criminal and Constitutional", "ta": "சிவில், குற்றவியல் மற்றும் அரசியலமைப்பு"}
        ],
        "ans": "B",
        "exp_en": "The Preamble secures 'Justice - Social, Economic and Political' through various provisions of Fundamental Rights and Directive Principles.",
        "exp_ta": "முகவுரை அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகளின் மூலம் 'சமூக, பொருளாதார மற்றும் அரசியல் நீதியை' உறுதி செய்கிறது."
    },

    # 15 (C)
    {
        "q_en": "The ideal of Justice—social, economic, and political—in the Preamble of the Indian Constitution was inspired by which historical event?",
        "q_ta": "இந்திய அரசியலமைப்பு முகவுரையில் உள்ள நீதி (சமூக, பொருளாதார மற்றும் அரசியல்) என்ற உன்னத இலட்சியம் எந்த வரலாற்று நிகழ்விலிருந்து ஈர்க்கப்பட்டது?",
        "opts": [
            {"id": "A", "en": "American War of Independence (1776)", "ta": "அமெரிக்க சுதந்திரப் போர் (1776)"},
            {"id": "B", "en": "French Revolution (1789)", "ta": "பிரெஞ்சுப் புரட்சி (1789)"},
            {"id": "C", "en": "Russian Revolution (1917)", "ta": "ரஷ்யப் புரட்சி (1917)"},
            {"id": "D", "en": "Glorious Revolution in Britain (1688)", "ta": "பிரிட்டனின் மாண்புமிகு புரட்சி (1688)"}
        ],
        "ans": "C",
        "exp_en": "The ideal of Justice (social, economic, and political) in our Preamble has been taken from the Russian Revolution (1917).",
        "exp_ta": "நமது முகவுரையில் உள்ள நீதி (சமூக, பொருளாதார, அரசியல்) என்ற இலட்சியம் ரஷ்யப் புரட்சியிலிருந்து (1917) பெறப்பட்டது."
    },

    # 16 (D)
    {
        "q_en": "The ideals of Liberty, Equality, and Fraternity in the Preamble of the Indian Constitution were derived from which famous historical revolution?",
        "q_ta": "இந்திய அரசியலமைப்பின் முகவுரையில் உள்ள சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் ஆகிய இலட்சியங்கள் எந்த புகழ்பெற்ற வரலாற்றுப் புரட்சியிலிருந்து பெறப்பட்டன?",
        "opts": [
            {"id": "A", "en": "Industrial Revolution", "ta": "தொழிற்புரட்சி"},
            {"id": "B", "en": "Russian Revolution", "ta": "ரஷ்யப் புரட்சி"},
            {"id": "C", "en": "Chinese Revolution", "ta": "சீனப் புரட்சி"},
            {"id": "D", "en": "French Revolution", "ta": "பிரெஞ்சுப் புரட்சி"}
        ],
        "ans": "D",
        "exp_en": "The ideals of Liberty, Equality, and Fraternity in our Preamble have been taken from the French Revolution (1789–1799).",
        "exp_ta": "முகவுரையில் உள்ள சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் ஆகிய இலட்சியங்கள் பிரெஞ்சுப் புரட்சியிலிருந்து (1789–1799) பெறப்பட்டன."
    },

    # 17 (A)
    {
        "q_en": "How many specific types/facets of 'Liberty' are explicitly secured to all Indian citizens in the Preamble?",
        "q_ta": "முகவுரையில் அனைத்து இந்திய குடிமக்களுக்கும் எத்தனை குறிப்பிட்ட வகையான 'சுதந்திரங்கள்' வெளிப்படையாக உறுதி செய்யப்பட்டுள்ளன?",
        "opts": [
            {"id": "A", "en": "Five (Thought, Expression, Belief, Faith, Worship)", "ta": "ஐந்து (எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி, வழிபாடு)"},
            {"id": "B", "en": "Three (Speech, Movement, Association)", "ta": "மூன்று (பேச்சு, நடமாட்டம், சங்கம்)"},
            {"id": "C", "en": "Four (Trade, Residence, Religion, Life)", "ta": "நான்கு (வணிகம், குடியிருப்பு, மதம், வாழ்வு)"},
            {"id": "D", "en": "Six (Assembly, Residence, Occupation, Speech, Press, Life)", "ta": "ஆறு (கூட்டம், குடியிருப்பு, தொழில், பேச்சு, பத்திரிகை, வாழ்வு)"}
        ],
        "ans": "A",
        "exp_en": "The Preamble secures Liberty of 5 kinds: Thought, Expression, Belief, Faith, and Worship.",
        "exp_ta": "முகவுரை 5 வகையான சுதந்திரங்களை உறுதி செய்கிறது: எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி மற்றும் வழிபாடு."
    },

    # 18 (B)
    {
        "q_en": "What are the two specific categories of 'Equality' guaranteed to citizens in the Preamble?",
        "q_ta": "முகவுரையில் குடிமக்களுக்கு உத்தரவாதம் அளிக்கப்பட்ட 'சமத்துவத்தின்' இரண்டு குறிப்பிட்ட பிரிவுகள் எவை?",
        "opts": [
            {"id": "A", "en": "Equality of Wealth and Property", "ta": "செல்வம் மற்றும் சொத்துச் சமத்துவம்"},
            {"id": "B", "en": "Equality of Status and Opportunity", "ta": "அந்தஸ்து மற்றும் வாய்ப்பில் சமத்துவம்"},
            {"id": "C", "en": "Equality of Religion and Caste", "ta": "மதம் மற்றும் சாதிச் சமத்துவம்"},
            {"id": "D", "en": "Equality of Rights and Duties", "ta": "உரிமைகள் மற்றும் கடமைகளில் சமத்துவம்"}
        ],
        "ans": "B",
        "exp_en": "The Preamble secures to all citizens 'Equality of status and of opportunity'.",
        "exp_ta": "முகவுரை அனைத்து குடிமக்களுக்கும் 'அந்தஸ்திலும் வாய்ப்பிலும் சமத்துவத்தை' உறுதி செய்கிறது."
    },

    # 19 (C)
    {
        "q_en": "Prior to the 42nd Constitutional Amendment in 1976, how was India described in the original Preamble of 1949?",
        "q_ta": "1976-ன் 42வது அரசியலமைப்புத் திருத்தத்திற்கு முன், 1949-ன் அசல் முகவுரையில் இந்தியா எவ்வாறு விவரிக்கப்பட்டது?",
        "opts": [
            {"id": "A", "en": "Sovereign Secular Democratic Republic", "ta": "இறையாண்மை மதச்சார்பற்ற ஜனநாயக குடியரசு"},
            {"id": "B", "en": "Sovereign Socialist Republic", "ta": "இறையாண்மை சமதர்ம குடியரசு"},
            {"id": "C", "en": "Sovereign Democratic Republic", "ta": "இறையாண்மை கொண்ட ஜனநாயக குடியரசு"},
            {"id": "D", "en": "Federal Socialist Republic", "ta": "கூட்டாட்சி சமதர்ம குடியரசு"}
        ],
        "ans": "C",
        "exp_en": "Originally (in 1949), India was described as a 'Sovereign Democratic Republic'. The words 'Socialist' and 'Secular' were added in 1976.",
        "exp_ta": "முதலில் (1949 இல்), இந்தியா 'இறையாண்மை கொண்ட ஜனநாயக குடியரசு' என விவரிக்கப்பட்டது. 1976 இல் 'சமதர்ம' மற்றும் 'மதச்சார்பற்ற' சொற்கள் சேர்க்கப்பட்டன."
    },

    # 20 (D)
    {
        "q_en": "Which noble objective in the Preamble assures both 'the dignity of the individual' and 'the unity and integrity of the Nation'?",
        "q_ta": "முகவுரையில் உள்ள எந்த உன்னத குறிக்கோள் 'தனிநபரின் கண்ணியம்' மற்றும் 'நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு' ஆகிய இரண்டையும் உறுதி செய்கிறது?",
        "opts": [
            {"id": "A", "en": "Justice", "ta": "நீதி"},
            {"id": "B", "en": "Liberty", "ta": "சுதந்திரம்"},
            {"id": "C", "en": "Equality", "ta": "சமத்துவம்"},
            {"id": "D", "en": "Fraternity", "ta": "சகோதரத்துவம்"}
        ],
        "ans": "D",
        "exp_en": "The Preamble resolves to promote 'Fraternity assuring the dignity of the individual and the unity and integrity of the Nation'.",
        "exp_ta": "முகவுரை 'தனிநபரின் கண்ணியத்தையும் நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாட்டையும் உறுதிப்படுத்தும் சகோதரத்துவத்தை' வளர்க்க உறுதியேற்கிறது."
    },

    # 21 (A)
    {
        "q_en": "Which expression in the original 1949 Preamble was substituted by the 42nd Amendment Act of 1976 to include the word 'Integrity'?",
        "q_ta": "1976-ன் 42வது திருத்தச் சட்டத்தின் மூலம் 'ஒருமைப்பாடு' என்ற சொல்லைச் சேர்க்க அசல் 1949 முகவுரையில் இருந்த எந்தத் தொடர் மாற்றப்பட்டது?",
        "opts": [
            {"id": "A", "en": "'Unity of the Nation' was replaced by 'Unity and Integrity of the Nation'", "ta": "'நாட்டின் ஒற்றுமை' என்பதற்குப் பதிலாக 'நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு' என மாற்றப்பட்டது"},
            {"id": "B", "en": "'Sovereignty of India' was replaced by 'Unity and Integrity'", "ta": "'இந்தியாவின் இறையாண்மை' என்பதற்குப் பதிலாக 'ஒற்றுமை மற்றும் ஒருமைப்பாடு' என மாற்றப்பட்டது"},
            {"id": "C", "en": "'Fraternity' was replaced by 'Integrity'", "ta": "'சகோதரத்துவம்' என்பதற்குப் பதிலாக 'ஒருமைப்பாடு' என மாற்றப்பட்டது"},
            {"id": "D", "en": "'Security of State' was replaced by 'Integrity of Nation'", "ta": "'மாநிலத்தின் பாதுகாப்பு' என்பதற்குப் பதிலாக 'நாட்டின் ஒருமைப்பாடு' என மாற்றப்பட்டது"}
        ],
        "ans": "A",
        "exp_en": "The 42nd Amendment Act 1976 substituted the phrase 'Unity of the Nation' with 'Unity and Integrity of the Nation'.",
        "exp_ta": "42வது திருத்தச் சட்டம் 1976 'நாட்டின் ஒற்றுமை' என்ற தொடருக்குப் பதிலாக 'நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு' என மாற்றியது."
    },

    # 22 (B)
    {
        "q_en": "What is the precise legal status of the provisions contained in the Preamble of the Constitution of India in a court of law?",
        "q_ta": "நீதிமன்றத்தில் இந்திய அரசியலமைப்பின் முகவுரையில் உள்ள விதிகளின் துல்லியமான சட்ட அந்தஸ்து என்ன?",
        "opts": [
            {"id": "A", "en": "Fully justiciable and enforceable like Fundamental Rights", "ta": "அடிப்படை உரிமைகளைப் போல முழுமையாக நீதிமன்றத்தால் நிலைநிறுத்தக்கூடியவை"},
            {"id": "B", "en": "Non-justiciable and non-enforceable in any court of law", "ta": "எந்தவொரு நீதிமன்றத்திலும் நேரடியாக நிலைநிறுத்த முடியாதவை மற்றும் அமல்படுத்த முடியாதவை"},
            {"id": "C", "en": "Enforceable only during a National Emergency", "ta": "தேசிய அவசரநிலையின் போது மட்டுமே அமல்படுத்தக்கூடியவை"},
            {"id": "D", "en": "Enforceable only by the High Courts under Article 226", "ta": "உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றங்களால் மட்டுமே அமல்படுத்தக்கூடியவை"}
        ],
        "ans": "B",
        "exp_en": "The Preamble is non-justiciable; its provisions are not enforceable in courts of law (held in Berubari & Kesavananda Bharati).",
        "exp_ta": "முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது; அதன் விதிகளை நீதிமன்றங்களில் நேரடியாக அமல்படுத்த முடியாது."
    },

    # 23 (C)
    {
        "q_en": "Which of the following statements correctly describes the Preamble's relationship with the legislative powers of Parliament?",
        "q_ta": "நாடாளுமன்றத்தின் சட்டமியற்றும் அதிகாரங்களுடன் முகவுரையின் உறவை பின்வரும் கூற்றுகளில் எது சரியாக விவரிக்கிறது?",
        "opts": [
            {"id": "A", "en": "It is an independent source of substantive power to the Legislature", "ta": "இது சட்டமன்றத்திற்குச் சட்டமியற்றும் அதிகாரத்தை வழங்கும் ஒரு சுயாதீன மூலமாகும்"},
            {"id": "B", "en": "It imposes an absolute prohibition upon the legislative powers of Parliament", "ta": "இது நாடாளுமன்றத்தின் சட்டமியற்றும் அதிகாரங்கள் மீது முழுமையான தடையை விதிக்கிறது"},
            {"id": "C", "en": "It is neither a source of power to the Legislature nor a prohibition upon the powers of the Legislature", "ta": "இது சட்டமன்றத்திற்கு அதிகாரத்தை வழங்கும் மூலமும் அல்ல, சட்டமன்ற அதிகாரங்கள் மீதான தடையுமல்ல"},
            {"id": "D", "en": "It overrides all Ordinary Laws and Constitutional Amendments automatically", "ta": "இது அனைத்து சாதாரணச் சட்டங்களையும் அரசியலமைப்புத் திருத்தங்களையும் தானாகவே மேலெழுதுகிறது"}
        ],
        "ans": "C",
        "exp_en": "The Supreme Court laid down that the Preamble is neither a source of power to legislature nor a prohibition upon the powers of legislature.",
        "exp_ta": "முகவுரை சட்டமன்றத்திற்கு அதிகாரத்தை வழங்கும் மூலமும் அல்ல, சட்டமன்றத்தின் அதிகாரங்கள் மீதான தடையாகவும் அமையாது என்று உச்ச நீதிமன்றம் கூறியுள்ளது."
    },

    # 24 (D)
    {
        "q_en": "On which exact date was the historic 'Objectives Resolution' introduced by Pandit Jawaharlal Nehru in the Constituent Assembly?",
        "q_ta": "பண்டித ஜவஹர்லால் நேருவால் அரசியலமைப்பு நிர்ணய அவையில் வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானம்' எந்த தேதியில் அறிமுகப்படுத்தப்பட்டது?",
        "opts": [
            {"id": "A", "en": "9th December 1946", "ta": "9 டிசம்பர் 1946"},
            {"id": "B", "en": "11th December 1946", "ta": "11 டிசம்பர் 1946"},
            {"id": "C", "en": "22nd January 1947", "ta": "22 ஜனவரி 1947"},
            {"id": "D", "en": "13th December 1946", "ta": "13 டிசம்பர் 1946"}
        ],
        "ans": "D",
        "exp_en": "Jawaharlal Nehru moved the historic Objectives Resolution in the Constituent Assembly on December 13, 1946.",
        "exp_ta": "ஜவஹர்லால் நேரு வரலாற்றுச் சிறப்புமிக்க குறிக்கோள் தீர்மானத்தை டிசம்பர் 13, 1946 அன்று அரசியலமைப்பு அவையில் முன்மொழிந்தார்."
    },

    # 25 (A)
    {
        "q_en": "On which date was the 'Objectives Resolution' unanimously adopted by the Constituent Assembly?",
        "q_ta": "குறிக்கோள் தீர்மானம் அரசியலமைப்பு நிர்ணய அவையால் ஏகமனதாக ஏற்றுக்கொள்ளப்பட்ட தேதி எது?",
        "opts": [
            {"id": "A", "en": "22nd January 1947", "ta": "22 ஜனவரி 1947"},
            {"id": "B", "en": "13th December 1946", "ta": "13 டிசம்பர் 1946"},
            {"id": "C", "en": "26th November 1949", "ta": "26 நவம்பர் 1949"},
            {"id": "D", "en": "15th August 1947", "ta": "15 ஆகஸ்ட் 1947"}
        ],
        "ans": "A",
        "exp_en": "The Objectives Resolution was unanimously adopted by the Constituent Assembly on January 22, 1947.",
        "exp_ta": "குறிக்கோள் தீர்மானம் ஜனவரி 22, 1947 அன்று அரசியலமைப்பு நிர்ணய அவையால் ஏகமனதாக ஏற்றுக்கொள்ளப்பட்டது."
    },

    # 26 (B)
    {
        "q_en": "On which date was the Preamble voted upon and enacted LAST by the Constituent Assembly?",
        "q_ta": "அரசியலமைப்பு நிர்ணய அவையால் முகவுரை வாக்களிக்கப்பட்டு இறுதியாக இயற்றப்பட்ட தேதி எது?",
        "opts": [
            {"id": "A", "en": "26th November 1949", "ta": "26 நவம்பர் 1949"},
            {"id": "B", "en": "17th October 1949", "ta": "17 அக்டோபர் 1949"},
            {"id": "C", "en": "22nd January 1947", "ta": "22 ஜனவரி 1947"},
            {"id": "D", "en": "26th January 1950", "ta": "26 ஜனவரி 1950"}
        ],
        "ans": "B",
        "exp_en": "The Constituent Assembly took up the Preamble for voting and enacted it on October 17, 1949, after the rest of the Constitution was passed.",
        "exp_ta": "அரசியலமைப்பின் மற்ற பகுதிகள் நிறைவேற்றப்பட்ட பிறகு, அக்டோபர் 17, 1949 அன்று முகவுரை வாக்களிக்கப்பட்டு இயற்றப்பட்டது."
    },

    # 27 (C)
    {
        "q_en": "Which famous English political scientist paid tribute to the Indian Preamble by quoting it at the opening of his book 'Principles of Social and Political Theory' (1951)?",
        "q_ta": "தனது 'சமூக மற்றும் அரசியல் கோட்பாட்டின் கொள்கைகள்' (1951) புத்தகத்தின் தொடக்கத்தில் இந்திய முகவுரையை மேற்கோள் காட்டி பெருமைப்படுத்திய புகழ்பெற்ற ஆங்கில அரசியல் அறிஞர் யார்?",
        "opts": [
            {"id": "A", "en": "Harold Laski", "ta": "ஹரோல்ட் லாஸ்கி"},
            {"id": "B", "en": "A.V. Dicey", "ta": "ஏ.வி. டைசி"},
            {"id": "C", "en": "Sir Ernest Barker", "ta": "சர் எர்னஸ்ட் பார்கர்"},
            {"id": "D", "en": "Ivor Jennings", "ta": "ஐவர் ஜென்னிங்ஸ்"}
        ],
        "ans": "C",
        "exp_en": "Sir Ernest Barker, a distinguished English political scientist, quoted the Preamble of Indian Constitution at the opening of his book (1951) and called it the 'Key-note'.",
        "exp_ta": "சர் எர்னஸ்ட் பார்கர் தனது 1951 புத்தகத்தின் தொடக்கத்தில் இந்திய முகவுரையை மேற்கோள் காட்டி அதை 'முக்கிய குறிப்பு' (Key-note) என்று அழைத்தார்."
    },

    # 28 (D)
    {
        "q_en": "Who described the Preamble as 'the most precious part of the Constitution', 'the Soul of the Constitution', and 'a Jewel set in the Constitution'?",
        "q_ta": "முகவுரையை 'அரசியலமைப்பின் மிகவும் விலையேறப்பெற்ற பகுதி', 'அரசியலமைப்பின் ஆன்மா' மற்றும் 'அரசியலமைப்பில் பதிக்கப்பட்ட ஆபரணம்' என்று வர்ணித்தவர் யார்?",
        "opts": [
            {"id": "A", "en": "K.M. Munshi", "ta": "கே.எம். முன்ஷி"},
            {"id": "B", "en": "N.A. Palkhivala", "ta": "என்.ஏ. பல்கிவாலா"},
            {"id": "C", "en": "Dr. B.R. Ambedkar", "ta": "டாக்டர் பி.ஆர். அம்பேத்கர்"},
            {"id": "D", "en": "Pandit Thakur Das Bhargava", "ta": "பண்டிட் தாக்கூர் தாஸ் பார்கவா"}
        ],
        "ans": "D",
        "exp_en": "Pandit Thakur Das Bhargava, a member of the Constituent Assembly, praised the Preamble as the Soul and Jewel of the Constitution.",
        "exp_ta": "அரசியலமைப்பு அவையின் உறுப்பினரான பண்டிட் தாக்கூர் தாஸ் பார்கவா முகவுரையை அரசியலமைப்பின் ஆன்மா மற்றும் ஆபரணம் எனப் போற்றினார்."
    },

    # 29 (A)
    {
        "q_en": "Who amongst the following Constituent Assembly members observed that 'The Preamble to our Constitution expresses what we had thought or dreamt so long'?",
        "q_ta": "'நமது அரசியலமைப்பின் முகவுரை நாம் இவ்வளவு காலம் என்ன நினைத்தோம் அல்லது கனவு கண்டோம் என்பதை வெளிப்படுத்துகிறது' என்று கூறிய அரசியலமைப்பு அவையின் உறுப்பினர் யார்?",
        "opts": [
            {"id": "A", "en": "Sir Alladi Krishnaswami Iyer", "ta": "சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர்"},
            {"id": "B", "en": "Dr. K.M. Munshi", "ta": "டாக்டர் கே.எம். முன்ஷி"},
            {"id": "C", "en": "Gopala Swamy Ayyangar", "ta": "கோபால சாமி அய்யங்கார்"},
            {"id": "D", "en": "T.T. Krishnamachari", "ta": "டி.டி. கிருஷ்ணமாச்சாரி"}
        ],
        "ans": "A",
        "exp_en": "Sir Alladi Krishnaswami Iyer remarked that the Preamble expresses what we had thought or dreamt so long.",
        "exp_ta": "சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர் முகவுரை நாம் இவ்வளவு காலம் என்ன நினைத்தோம் அல்லது கனவு கண்டோம் என்பதை வெளிப்படுத்துகிறது எனக் குறிப்பிட்டார்."
    },

    # 30 (B)
    {
        "q_en": "Which Committee's recommendations formed the primary basis for the enactment of the 42nd Constitutional Amendment Act, 1976?",
        "q_ta": "1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தை இயற்றுவதற்கு எந்தக் குழுவின் பரிந்துரைகள் முதன்மை அடிப்படையாக அமைந்தன?",
        "opts": [
            {"id": "A", "en": "Sarkaria Commission", "ta": "சர்க்காரியா ஆணையம்"},
            {"id": "B", "en": "Swaran Singh Committee", "ta": "சுரன் சிங் குழு"},
            {"id": "C", "en": "Balwant Rai Mehta Committee", "ta": "பல்வந்த் ராய் மேத்தா குழு"},
            {"id": "D", "en": "M.N. Venkatachaliah Commission", "ta": "எம்.என். வெங்கடாசலையா ஆணையம்"}
        ],
        "ans": "B",
        "exp_en": "The Sardar Swaran Singh Committee (1976) recommended constitutional amendments, including changes to the Preamble.",
        "exp_ta": "சர்தார் சுரன் சிங் குழு (1976) முகவுரையில் மாற்றங்கள் உட்பட அரசியலமைப்புத் திருத்தங்களைப் பரிந்துரைத்தது."
    },

    # 31 (C)
    {
        "q_en": "On which exact date did the changes made to the Preamble by the 42nd Constitutional Amendment Act, 1976 officially come into force?",
        "q_ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டம் 1976 மூலம் முகவுரையில் செய்யப்பட்ட மாற்றங்கள் அதிகாரப்பூர்வமாக நடைமுறைக்கு வந்த தேதி எது?",
        "opts": [
            {"id": "A", "en": "18th December 1976", "ta": "18 டிசம்பர் 1976"},
            {"id": "B", "en": "26th November 1976", "ta": "26 நவம்பர் 1976"},
            {"id": "C", "en": "3rd January 1977", "ta": "3 ஜனவரி 1977"},
            {"id": "D", "en": "26th January 1977", "ta": "26 ஜனவரி 1977"}
        ],
        "ans": "C",
        "exp_en": "The 42nd Amendment Act received Presidential assent on Dec 18, 1976, and section 2 amending the Preamble came into force on January 3, 1977.",
        "exp_ta": "42வது திருத்தச் சட்டம் டிசம்பர் 18, 1976 இல் குடியரசுத் தலைவரின் ஒப்புதலைப் பெற்றது, மேலும் முகவுரையைத் திருத்தும் பிரிவு ஜனவரி 3, 1977 இல் நடைமுறைக்கு வந்தது."
    },

    # 32 (D)
    {
        "q_en": "Which of the following words does NOT find any mention in the Preamble of the Constitution of India?",
        "q_ta": "பின்வரும் சொற்களில் எது இந்திய அரசியலமைப்பின் முகவுரையில் எந்த இடத்திலும் இடம்பெறவில்லை?",
        "opts": [
            {"id": "A", "en": "Secular", "ta": "மதச்சார்பற்ற"},
            {"id": "B", "en": "Fraternity", "ta": "சகோதரத்துவம்"},
            {"id": "C", "en": "Integrity", "ta": "ஒருமைப்பாடு"},
            {"id": "D", "en": "Federal", "ta": "கூட்டாட்சி"}
        ],
        "ans": "D",
        "exp_en": "The word 'Federal' is NOT mentioned anywhere in the Preamble (nor in Article 1, which uses 'Union of States').",
        "exp_ta": "'கூட்டாட்சி' (Federal) என்ற சொல் முகவுரையிலோ அல்லது அரசியலமைப்பிலோ எங்கும் இடம்பெறவில்லை."
    },

    # 33 (A)
    {
        "q_en": "In Indian constitutional jurisprudence, what does the concept of 'Distributive Justice' mentioned in the Preamble represent?",
        "q_ta": "இந்திய சட்டவியலில், முகவுரையில் குறிப்பிடப்பட்டுள்ள 'பகிர்வு நீதி' (Distributive Justice) என்ற கருத்து எதனைக் குறிக்கிறது?",
        "opts": [
            {"id": "A", "en": "Combination of Social Justice and Economic Justice", "ta": "சமூக நீதி மற்றும் பொருளாதார நீதியின் சேர்க்கை"},
            {"id": "B", "en": "Combination of Political Justice and Judicial Review", "ta": "அரசியல் நீதி மற்றும் நீதித்துறை ஆய்வின் சேர்க்கை"},
            {"id": "C", "en": "Equal distribution of seats in Parliament", "ta": "நாடாளுமன்றத்தில் இடங்களின் சமமான பங்கீடு"},
            {"id": "D", "en": "Distribution of powers between Centre and States", "ta": "மத்திய மற்றும் மாநில அரசுகளுக்கு இடையேயான அதிகாரப் பங்கீடு"}
        ],
        "ans": "A",
        "exp_en": "Social Justice and Economic Justice combined together form what is known as 'Distributive Justice'.",
        "exp_ta": "சமூக நீதியும் பொருளாதார நீதியும் இணைந்து 'பகிர்வு நீதி' என்று அழைக்கப்படுகிறது."
    },

    # 34 (B)
    {
        "q_en": "Which Part of the Constitution of India serves as the direct policy instrument to realize the Preamble's objective of Socio-Economic Justice?",
        "q_ta": "முகவுரையின் சமூக-பொருளாதார நீதி என்ற குறிக்கோளை நனவாக்குவதற்கான நேரடி கொள்கைக் கருவியாக இந்திய அரசியலமைப்பின் எந்தப் பகுதி செயல்படுகிறது?",
        "opts": [
            {"id": "A", "en": "Part III - Fundamental Rights", "ta": "பகுதி III - அடிப்படை உரிமைகள்"},
            {"id": "B", "en": "Part IV - Directive Principles of State Policy", "ta": "பகுதி IV - அரசு வழிகாட்டு நெறிமுறைகள்"},
            {"id": "C", "en": "Part IV-A - Fundamental Duties", "ta": "பகுதி IV-A - அடிப்படை கடமைகள்"},
            {"id": "D", "en": "Part IX - The Panchayats", "ta": "பகுதி IX - பஞ்சாயத்துகள்"}
        ],
        "ans": "B",
        "exp_en": "Part IV (Directive Principles of State Policy) directs the State to secure a social order for the promotion of welfare of people (Art 38, 39).",
        "exp_ta": "பகுதி IV (அரசு வழிகாட்டு நெறிமுறைகள்) சமூக-பொருளாதார நீதியை அடைவதற்கான வழிகாட்டுதல்களை அரசுக்கு வழங்குகிறது."
    },

    # 35 (C)
    {
        "q_en": "Which Article under Part III specifically translates the Preamble's objective of 'Equality of Opportunity' into a justiciable Fundamental Right?",
        "q_ta": "பகுதி III-ன் கீழ் உள்ள எந்த உறுப்பு முகவுரையின் 'வாய்ப்பில் சமத்துவம்' என்ற குறிக்கோளை நிலைநிறுத்தக்கூடிய அடிப்படை உரிமையாக மாற்றுகிறது?",
        "opts": [
            {"id": "A", "en": "Article 14", "ta": "உறுப்பு 14"},
            {"id": "B", "en": "Article 15", "ta": "உறுப்பு 15"},
            {"id": "C", "en": "Article 16", "ta": "உறுப்பு 16"},
            {"id": "D", "en": "Article 18", "ta": "உறுப்பு 18"}
        ],
        "ans": "C",
        "exp_en": "Article 16 guarantees equality of opportunity for all citizens in matters relating to employment or appointment to any office under the State.",
        "exp_ta": "உறுப்பு 16 பொது வேலைவாய்ப்பில் அனைத்து குடிமக்களுக்கும் வாய்ப்பில் சமத்துவத்தை உத்தரவாதம் செய்கிறது."
    },

    # 36 (D)
    {
        "q_en": "Which clause of Fundamental Duties (Article 51A) directly reflects the Preamble's ideal of promoting 'Fraternity and Common Brotherhood'?",
        "q_ta": "அடிப்படை கடமைகளின் (உறுப்பு 51A) எந்தப் பிரிவு முகவுரையின் 'சகோதரத்துவம் மற்றும் பொதுவான சகோதர உணர்வு' என்ற இலட்சியத்தை நேரடியாகப் பிரதிபலிக்கிறது?",
        "opts": [
            {"id": "A", "en": "Article 51A(a)", "ta": "உறுப்பு 51A(a)"},
            {"id": "B", "en": "Article 51A(c)", "ta": "உறுப்பு 51A(c)"},
            {"id": "C", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "D", "en": "Article 51A(e)", "ta": "உறுப்பு 51A(e)"}
        ],
        "ans": "D",
        "exp_en": "Article 51A(e) directs every citizen to promote harmony and the spirit of common brotherhood amongst all the people of India.",
        "exp_ta": "உறுப்பு 51A(e) அனைத்து மக்களிடையே நல்லிணக்கத்தையும் பொதுவான சகோதரத்துவ உணர்வையும் வளர்க்க ஒவ்வொரு குடிமகனுக்கும் கட்டளையிடுகிறது."
    },

    # 37 (A)
    {
        "q_en": "What does the term 'Republic' in the Preamble signify regarding the political structure of India?",
        "q_ta": "இந்தியாவின் அரசியல் அமைப்பு தொடர்பாக முகவுரையில் உள்ள 'குடியரசு' என்ற சொல் எதனைக் குறிக்கிறது?",
        "opts": [
            {"id": "A", "en": "Vesting of political sovereignty in the people and having an elected Head of State for a fixed period", "ta": "அரசியல் இறையாண்மை மக்களிடம் இருப்பது மற்றும் தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவரைக் குறிப்பிட்ட காலத்திற்கு கொண்டிருப்பது"},
            {"id": "B", "en": "Supreme authority vested in a hereditary monarch subject to Parliament", "ta": "நாடாளுமன்றத்திற்கு உட்பட்ட பரம்பரை மன்னரிடம் உச்ச அதிகாரம் இருப்பது"},
            {"id": "C", "en": "Complete independence from international treaties and international courts", "ta": "சர்வதேச ஒப்பந்தங்கள் மற்றும் சர்வதேச நீதிமன்றங்களிலிருந்து முழுமையான சுதந்திரம்"},
            {"id": "D", "en": "A single party rule where all offices are reserved for ruling party members", "ta": "ஆளும் கட்சி உறுப்பினர்களுக்கு அனைத்து பதவிகளும் ஒதுக்கப்படும் ஒரு கட்சி ஆட்சி"}
        ],
        "ans": "A",
        "exp_en": "A Republic signifies political sovereignty vested in the people (no hereditary monarch) and all public offices open to every citizen.",
        "exp_ta": "குடியரசு என்பது மக்களிடம் உள்ள அரசியல் இறையாண்மையையும் (பரம்பரை மன்னர் இல்லாமை) அனைத்து பொதுப்பதவிகளும் குடிமக்களுக்கு திறந்திருப்பதையும் குறிக்கிறது."
    },

    # 38 (B)
    {
        "q_en": "Which statement correctly captures the nature of 'Secularism' as embodied in the Preamble and Constitution of India?",
        "q_ta": "இந்திய முகவுரை மற்றும் அரசியலமைப்பில் உள்ள 'மதச்சார்பின்மையின்' தன்மையை எந்தக் கூற்று சரியாகப் படம்பிடிக்கிறது?",
        "opts": [
            {"id": "A", "en": "Anti-religious state prohibiting all religious practices in public", "ta": "பொதுவெளியில் அனைத்து மதப் பழக்கவழக்கங்களையும் தடைசெய்யும் மத எதிர்ப்பு அரசு"},
            {"id": "B", "en": "Positive secularism ensuring equal status, respect, and support for all religions ('Sarva Dharma Sambhava')", "ta": "அனைத்து மதங்களுக்கும் சமமான அந்தஸ்து, மரியாதை மற்றும் ஆதரவை உறுதி செய்யும் நேர்மறை மதச்சார்பின்மை ('சர்வ தர்ம சமபாவா')"},
            {"id": "C", "en": "State recognizing Hinduism as the official state religion while tolerating minority faiths", "ta": "சிறுபான்மை மதங்களைச் சகித்துக் கொண்டு இந்து மதத்தை அதிகாரப்பூர்வ அரசு மதமாக அங்கீகரிக்கும் அரசு"},
            {"id": "D", "en": "Strict Western separation forbidding any financial or educational aid to religious institutions", "ta": "மத நிறுவனங்களுக்கு நிதி அல்லது கல்வி உதவிகளை முற்றிலும் தடைசெய்யும் கண்டிப்பான மேற்கத்திய பிரிவினை"}
        ],
        "ans": "B",
        "exp_en": "Indian secularism is positive secularism, giving equal status, respect, and protection to all religions.",
        "exp_ta": "இந்திய மதச்சார்பின்மை என்பது நேர்மறை மதச்சார்பின்மை ஆகும்; இது அனைத்து மதங்களுக்கும் சமமான மரியாதை மற்றும் பாதுகாப்பை அளிக்கிறது."
    },

    # 39 (C)
    {
        "q_en": "How has the Supreme Court defined the 'Socialism' mentioned in the Indian Preamble in D.S. Nakara v. Union of India (1983)?",
        "q_ta": "டி.எஸ். நகாரா வழக்கில் (1983) இந்திய முகவுரையில் குறிப்பிடப்பட்டுள்ள 'சமதர்மத்தை' உச்ச நீதிமன்றம் எவ்வாறு வரையறுத்துள்ளது?",
        "opts": [
            {"id": "A", "en": "Totalitarian state communism involving nationalization of all private assets", "ta": "அனைத்து தனியார் சொத்துக்களையும் அரசுடைமையாக்கும் சர்வாதிகார அரசு கம்யூனிசம்"},
            {"id": "B", "en": "Pure capitalist economy driven solely by free market forces", "ta": "சுதந்திர சந்தை சக்திகளால் மட்டுமே இயக்கப்படும் தூய முதலாளித்துவ பொருளாதாரம்"},
            {"id": "C", "en": "A blend of Marxism and Gandhism leaning heavily towards Gandhian socialism and a mixed economy", "ta": "மார்க்சியம் மற்றும் காந்தியத்தின் கலவை; குறிப்பாக காந்திய சமதர்மம் மற்றும் கலப்புப் பொருளாதாரத்தை நோக்கி சாய்வது"},
            {"id": "D", "en": "Complete abolition of all private business enterprises", "ta": "அனைத்து தனியார் வணிக நிறுவனங்களையும் முற்றிலும் ஒழிப்பது"}
        ],
        "ans": "C",
        "exp_en": "In D.S. Nakara Case (1983), SC held that Indian socialism is a blend of Marxism and Gandhism, leaning heavily towards Gandhian socialism.",
        "exp_ta": "டி.எஸ். நகாரா வழக்கில் (1983), இந்திய சமதர்மம் மார்க்சியம் மற்றும் காந்தியத்தின் கலவை என்றும் காந்திய சமதர்மத்தை நோக்கி சாய்வது என்றும் உச்ச நீதிமன்றம் கூறியது."
    },

    # 40 (D)
    {
        "q_en": "Can Parliament amend the Preamble of the Constitution under Article 368?",
        "q_ta": "உறுப்பு 368-ன் கீழ் நாடாளுமன்றம் அரசியலமைப்பின் முகவுரையைத் திருத்த முடியுமா?",
        "opts": [
            {"id": "A", "en": "No, Preamble can never be amended under any circumstances", "ta": "இல்லை, எந்தச் சூழ்நிலையிலும் முகவுரையைத் திருத்த முடியாது"},
            {"id": "B", "en": "Yes, Parliament can amend any part of Preamble including destroying Basic Features", "ta": "ஆம், அடிப்படை அம்சங்களை அழிப்பது உட்பட முகவுரையின் எந்தப் பகுதியையும் நாடாளுமன்றம் திருத்தலாம்"},
            {"id": "C", "en": "Only with the prior consent of three-fourths of State Assemblies", "ta": "மூன்றில் முக்கால் பங்கு மாநில சட்டமன்றங்களின் முன் அனுமதியுடன் மட்டுமே"},
            {"id": "D", "en": "Yes, Parliament can amend Preamble subject to the limitation that 'Basic Features' within it cannot be altered or destroyed", "ta": "ஆம், முகவுரையில் உள்ள 'அடிப்படை அம்சங்களை' மாற்றவோ அழிக்கவோ முடியாது என்ற வரம்பிற்கு உட்பட்டு நாடாளுமன்றம் முகவுரையைத் திருத்தலாம்"}
        ],
        "ans": "D",
        "exp_en": "In Kesavananda Bharati (1973), SC held that Preamble CAN be amended under Art 368, provided the Basic Features are not altered or destroyed.",
        "exp_ta": "கேசவானந்த பாரதி வழக்கில் (1973), அடிப்படை அம்சங்கள் மாற்றப்படாமல் அல்லது அழிக்கப்படாமல் இருந்தால் முகவுரையைத் திருத்தலாம் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
    },

    # 41 (A)
    {
        "q_en": "What was the fundamental ground on which the 13-judge bench in Kesavananda Bharati case held that Preamble IS part of the Constitution?",
        "q_ta": "கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் அமர்வு முகவுரை அரசியலமைப்பின் ஒரு பகுதி தான் என்று தீர்ப்பளித்ததன் அடிப்படை காரணம் என்ன?",
        "opts": [
            {"id": "A", "en": "Preamble was debated, voted upon, and enacted by Constituent Assembly under the motion 'that Preamble stand part of Constitution'", "ta": "அரசியலமைப்பு அவையில் 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக நிற்க வேண்டும்' என்ற பிரேரணையுடன் விவாதிக்கப்பட்டு, வாக்களிக்கப்பட்டு இயற்றப்பட்டது"},
            {"id": "B", "en": "Preamble was drafted by the British Parliament in 1947", "ta": "முகவுரை 1947 இல் பிரிட்டிஷ் நாடாளுமன்றத்தால் வரைவு செய்யப்பட்டது"},
            {"id": "C", "en": "Preamble contains the list of Fundamental Rights", "ta": "முகவுரையில் அடிப்படை உரிமைகளின் பட்டியல் உள்ளது"},
            {"id": "D", "en": "Preamble was declared as justiciable by Article 32", "ta": "முகவுரை உறுப்பு 32-ன் கீழ் நீதிமன்றத்தால் நிலைநிறுத்தக்கூடியதாக அறிவிக்கப்பட்டது"}
        ],
        "ans": "A",
        "exp_en": "The Supreme Court noted that Constituent Assembly President Dr. Rajendra Prasad put the motion: 'The question is that Preamble stand part of Constitution. The motion was adopted.'",
        "exp_ta": "அரசியலமைப்பு அவைத் தலைவர் 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக நிற்க வேண்டும்' என்ற பிரேரணையை நிறைவேற்றியதை உச்ச நீதிமன்றம் சுட்டிக்காட்டியது."
    },

    # 42 (B)
    {
        "q_en": "Which core elements derived from the Preamble were declared as part of 'Basic Structure' in Kesavananda Bharati (1973)?",
        "q_ta": "கேசவானந்த பாரதி (1973) வழக்கில் முகவுரையிலிருந்து பெறப்பட்ட எந்த முக்கிய கூறுகள் 'அடிப்படை கட்டமைப்பின்' பகுதியாக அறிவிக்கப்பட்டன?",
        "opts": [
            {"id": "A", "en": "Right to Property and Presidential form of government", "ta": "சொத்துரிமை மற்றும் அதிபர் முறை அரசாங்கம்"},
            {"id": "B", "en": "Sovereignty of India, Democratic and Republican nature of polity, and Secular character", "ta": "இந்தியாவின் இறையாண்மை, ஜனநாயக மற்றும் குடியரசுத் தன்மை மற்றும் மதச்சார்பற்ற இயல்பு"},
            {"id": "C", "en": "Two-party political system and compulsory voting", "ta": "இரு கட்சி அரசியல் முறை மற்றும் கட்டாய வாக்களிப்பு"},
            {"id": "D", "en": "Unitary system of administration and English as sole official language", "ta": "ஒற்றையாட்சி நிர்வாக முறை மற்றும் ஆங்கிலம் மட்டுமே அதிகாரப்பூர்வ மொழியாக இருப்பது"}
        ],
        "ans": "B",
        "exp_en": "Chief Justice S.M. Sikri enumerated basic features including Supremacy of Constitution, Republican & Democratic form, Secular character, and Sovereignty.",
        "exp_ta": "தலைமை நீதிபதி எஸ்.எம். சிக்ரி அரசியலமைப்பின் மேலாதிக்கம், குடியரசு மற்றும் ஜனநாயக முறை, மதச்சார்பற்ற தன்மை, இறையாண்மை ஆகியவற்றை அடிப்படை அம்சங்களாகப் பட்டியலிட்டார்."
    },

    # 43 (C)
    {
        "q_en": "What is the established judicial principle regarding the use of Preamble in interpreting constitutional provisions?",
        "q_ta": "அரசியலமைப்பு விதிகளை விளக்குவதில் முகவுரையைப் பயன்படுத்துவது குறித்த நிறுவப்பட்ட நீதித்துறை கொள்கை என்ன?",
        "opts": [
            {"id": "A", "en": "Preamble overrides clear and unambiguous provisions of the Constitution", "ta": "முகவுரை அரசியலமைப்பின் தெளிவான விதிகளை மேலெழுதுகிறது"},
            {"id": "B", "en": "Preamble can never be referred to in any court proceeding", "ta": "எந்தவொரு நீதிமன்ற நடவடிக்கையிலும் முகவுரையைக் குறிப்பிட முடியாது"},
            {"id": "C", "en": "When terms of any Article are ambiguous or have two meanings, Preamble serves as an interpretive key to determine true intent", "ta": "அரசியலமைப்பு உறுப்பின் வாசகங்கள் தெளிவற்றதாகவோ அல்லது இருபொருள் கொண்டதாகவோ இருக்கும்போது, உண்மையான நோக்கத்தைத் தீர்மானிக்க முகவுரை விளக்கச் சாவியாகச் செயல்படுகிறது"},
            {"id": "D", "en": "Preamble is used only to interpret statutory tax laws", "ta": "சட்டப்பூர்வ வரிச் சட்டங்களை விளக்குவதற்கு மட்டுமே முகவுரை பயன்படுகிறது"}
        ],
        "ans": "C",
        "exp_en": "Where the language of a constitutional provision is ambiguous, the interpretation aligning with Preamble's vision is adopted.",
        "exp_ta": "அரசியலமைப்பு விதியின் வாசகங்கள் தெளிவற்றதாக இருக்கும்போது, முகவுரையின் நோக்கத்துடன் ஒத்துப்போகும் விளக்கமே ஏற்றுக்கொள்ளப்படுகிறது."
    },

    # 44 (D)
    {
        "q_en": "Which of the following statements concerning the Preamble of India is INCORRECT?",
        "q_ta": "இந்திய முகவுரை தொடர்பான பின்வரும் கூற்றுகளில் எது தவறானது?",
        "opts": [
            {"id": "A", "en": "It declares the date of adoption of the Constitution as Nov 26, 1949", "ta": "இது அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட தேதியை நவம்பர் 26, 1949 என அறிவிக்கிறது"},
            {"id": "B", "en": "It embodies the basic philosophy and fundamental values of the Constitution", "ta": "இது அரசியலமைப்பின் அடிப்படை தத்துவம் மற்றும் உன்னத விழுமியங்களை உள்ளடக்கியுள்ளது"},
            {"id": "C", "en": "It was amended by the 42nd Amendment Act of 1976", "ta": "இது 1976-ன் 42வது திருத்தச் சட்டத்தால் திருத்தப்பட்டது"},
            {"id": "D", "en": "It can be directly enforced in the Supreme Court under Article 32 to obtain legal remedies", "ta": "சட்ட நிவாரணம் பெற உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தில் நேரடியாக இதை அமல்படுத்த முடியும்"}
        ],
        "ans": "D",
        "exp_en": "Statement D is INCORRECT because the Preamble is non-justiciable and cannot be directly enforced under Article 32 or in any court of law.",
        "exp_ta": "கூற்று D தவறானது; ஏனெனில் முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது, உறுப்பு 32-ன் கீழ் நேரடியாக அமல்படுத்த முடியாது."
    },

    # 45 (A)
    {
        "q_en": "Under whose Prime Ministership was the 42nd Constitutional Amendment Act of 1976 enacted?",
        "q_ta": "யாருடைய பிரதம மந்திரி பதவிக் காலத்தில் 1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்பட்டது?",
        "opts": [
            {"id": "A", "en": "Indira Gandhi", "ta": "இந்திரா காந்தி"},
            {"id": "B", "en": "Morarji Desai", "ta": "மொரார்ஜி தேசாய்"},
            {"id": "C", "en": "Jawaharlal Nehru", "ta": "ஜவஹர்லால் நேரு"},
            {"id": "D", "en": "Lal Bahadur Shastri", "ta": "லால் பகதூர் சாஸ்திரி"}
        ],
        "ans": "A",
        "exp_en": "The 42nd Constitutional Amendment Act 1976 was enacted during the internal emergency under the Prime Ministership of Smt. Indira Gandhi.",
        "exp_ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டம் 1976 திருமதி இந்திரா காந்தி பிரதமராக இருந்தபோது உள்நாட்டு அவசரநிலையின் போது இயற்றப்பட்டது."
    },

    # 46 (B)
    {
        "q_en": "Which President of India gave presidential assent to the historic 42nd Constitutional Amendment Act, 1976?",
        "q_ta": "வரலாற்றுச் சிறப்புமிக்க 42வது அரசியலமைப்புத் திருத்தச் சட்டம் 1976-க்கு ஒப்புதல் அளித்த இந்தியக் குடியரசுத் தலைவர் யார்?",
        "opts": [
            {"id": "A", "en": "Dr. S. Radhakrishnan", "ta": "டாக்டர் எஸ். ராதாகிருஷ்ணன்"},
            {"id": "B", "en": "Fakhruddin Ali Ahmed", "ta": "பக்ருதீன் அலி அகமது"},
            {"id": "C", "en": "Neelam Sanjiva Reddy", "ta": "நீலம் சஞ்சீவ ரெட்டி"},
            {"id": "D", "en": "V.V. Giri", "ta": "வி.வி. கிரி"}
        ],
        "ans": "B",
        "exp_en": "President Fakhruddin Ali Ahmed gave assent to the 42nd Constitutional Amendment Act on December 18, 1976.",
        "exp_ta": "குடியரசுத் தலைவர் பக்ருதீன் அலி அகமது டிசம்பர் 18, 1976 அன்று 42வது திருத்தச் சட்டத்திற்கு ஒப்புதல் அளித்தார்."
    },

    # 47 (C)
    {
        "q_en": "Which expression in the Preamble signifies that India is an independent state, neither a dominion nor a dependency of any foreign nation?",
        "q_ta": "முகவுரையில் உள்ள எந்தத் தொடர் இந்தியா எந்தவொரு வெளிநாட்டின் ஆதிக்கத்திலோ அல்லது சார்பிலோ இல்லாத ஒரு சுயாதீனமான அரசு என்பதைக் குறிக்கிறது?",
        "opts": [
            {"id": "A", "en": "Democratic", "ta": "ஜனநாயக"},
            {"id": "B", "en": "Republic", "ta": "குடியரசு"},
            {"id": "C", "en": "Sovereign", "ta": "இறையாண்மை"},
            {"id": "D", "en": "Secular", "ta": "மதச்சார்பற்ற"}
        ],
        "ans": "C",
        "exp_en": "'Sovereign' implies that India is neither a dependency nor a dominion of any other nation, but an independent state capable of conducting its own internal & external affairs.",
        "exp_ta": "'இறையாண்மை' என்பது இந்தியா எந்தவொரு வெளிநாட்டின் ஆதிக்கத்திலோ சார்பிலோ இல்லாமல் தன் உள்நாட்டு, வெளிநாட்டு விவகாரங்களை தானே நடத்தும் சுதந்திரமான நாடு என்பதைக் குறிக்கிறது."
    },

    # 48 (D)
    {
        "q_en": "Which of the following forms of Liberty is NOT mentioned in the Preamble of the Constitution of India?",
        "q_ta": "பின்வரும் சுதந்திர வடிவங்களில் எது இந்திய அரசியலமைப்பின் முகவுரையில் குறிப்பிடப்படவில்லை?",
        "opts": [
            {"id": "A", "en": "Liberty of Thought", "ta": "எண்ண சுதந்திரம்"},
            {"id": "B", "en": "Liberty of Belief", "ta": "நம்பிக்கை சுதந்திரம்"},
            {"id": "C", "en": "Liberty of Worship", "ta": "வழிபாட்டு சுதந்திரம்"},
            {"id": "D", "en": "Liberty of Trade and Commerce", "ta": "வர்த்தகம் மற்றும் வணிக சுதந்திரம்"}
        ],
        "ans": "D",
        "exp_en": "The Preamble secures Liberty of Thought, Expression, Belief, Faith, and Worship. 'Liberty of Trade and Commerce' is NOT in the Preamble (it is regulated in Part XIII Articles 301-307).",
        "exp_ta": "முகவுரை எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி மற்றும் வழிபாடு ஆகிய 5 சுதந்திரங்களை மட்டுமே வழங்குகிறது. 'வர்த்தகம் மற்றும் வணிக சுதந்திரம்' முகவுரையில் இல்லை."
    },

    # 49 (A)
    {
        "q_en": "Who was the Chief Justice of India who headed the historic 13-judge bench in the Kesavananda Bharati Case (1973)?",
        "q_ta": "கேசவானந்த பாரதி வழக்கில் (1973) வரலாற்றுச் சிறப்புமிக்க 13 நீதிபதிகள் அமர்வுக்கு தலைமை தாங்கிய இந்தியத் தலைமை நீதிபதி யார்?",
        "opts": [
            {"id": "A", "en": "CJI S.M. Sikri", "ta": "தலைமை நீதிபதி எஸ்.எம். சிக்ரி"},
            {"id": "B", "en": "CJI A.N. Ray", "ta": "தலைமை நீதிபதி ஏ.என். ரே"},
            {"id": "C", "en": "CJI K. Subba Rao", "ta": "தலைமை நீதிபதி கே. சுப்பா ராவ்"},
            {"id": "D", "en": "CJI Y.V. Chandrachud", "ta": "தலைமை நீதிபதி ஒய்.வி. சந்திரசூட்"}
        ],
        "ans": "A",
        "exp_en": "Chief Justice S.M. Sikri headed the 13-judge bench in Kesavananda Bharati v. State of Kerala (1973).",
        "exp_ta": "தலைமை நீதிபதி எஸ்.எம். சிக்ரி 1973-ன் கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் கொண்ட அமர்விற்கு தலைமை தாங்கினார்."
    },

    # 50 (B)
    {
        "q_en": "What is the primary four-fold purpose served by the Preamble of the Constitution of India?",
        "q_ta": "இந்திய அரசியலமைப்பின் முகவுரை நிறைவேற்றும் முதன்மையான நான்கு அம்ச நோக்கம் என்ன?",
        "opts": [
            {"id": "A", "en": "To list the Fundamental Rights, Duties, DPSP, and Emergency Provisions", "ta": "அடிப்படை உரிமைகள், கடமைகள், வழிகாட்டு நெறிமுறைகள் மற்றும் அவசரநிலை விதிகளை பட்டியலிடுவது"},
            {"id": "B", "en": "To declare the source of authority, nature of Indian state, objectives of Constitution, and date of adoption", "ta": "அதிகாரத்தின் மூலம், இந்திய அரசின் தன்மை, அரசியலமைப்பின் குறிக்கோள்கள் மற்றும் ஏற்றுக்கொள்ளப்பட்ட தேதியை அறிவிப்பது"},
            {"id": "C", "en": "To define the administrative powers of Governor, Chief Minister, Prime Minister, and President", "ta": "ஆளுநர், முதலமைச்சர், பிரதமர் மற்றும் குடியரசுத் தலைவரின் நிர்வாக அதிகாரங்களை வரையறுப்பது"},
            {"id": "D", "en": "To enumerate the tax collection powers of Union, State, and Municipal authorities", "ta": "மத்திய, மாநில மற்றும் நகராட்சி அமைப்புகளின் வரி வசூல் அதிகாரங்களைப் பட்டியலிடுவது"}
        ],
        "ans": "B",
        "exp_en": "The Preamble serves 4 core purposes: 1. Source of authority (People), 2. Nature of State (S-S-S-D-R), 3. Objectives (J-L-E-F), 4. Date of adoption (Nov 26, 1949).",
        "exp_ta": "முகவுரை 4 முக்கிய நோக்கங்களை நிறைவேற்றுகிறது: 1. அதிகாரத்தின் மூலம் (மக்கள்), 2. அரசின் தன்மை, 3. குறிக்கோள்கள், 4. ஏற்றுக்கொள்ளப்பட்ட தேதி (நவம்பர் 26, 1949)."
    }
]

print(f"Total raw questions defined: {len(raw_questions)}")

# Construct full dual-schema question list
full_questions = []

for idx, item in enumerate(raw_questions, 1):
    q_id = f"PRE_PYQ_{idx:03d}"
    correct_ans = item["ans"]
    
    # Generate why_not_others
    why_not = {}
    for opt in item["opts"]:
        opt_key = opt["id"]
        if opt_key == correct_ans:
            why_not[opt_key] = {
                "en": f"Correct. {opt['en']} is the correct answer.",
                "ta": f"சரி. {opt['ta']} என்பது சரியான விடையாகும்."
            }
        else:
            why_not[opt_key] = {
                "en": f"Incorrect. {opt['en']} is not the correct choice for this question.",
                "ta": f"தவறு. {opt['ta']} என்பது இக்கேள்விக்கான சரியான தேர்வு அல்ல."
            }
            
    q_obj = {
        "id": q_id,
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": item.get("diff", "Medium"),
        "question_type": item.get("type", "Direct PYQ Pattern"),
        "question": {
            "en": item["q_en"],
            "ta": item["q_ta"]
        },
        "options": item["opts"],
        "correct_answer": correct_ans,
        "explanation": {
            "en": item["exp_en"],
            "ta": item["exp_ta"]
        },
        "why_not_others": why_not,
        "tnpsc_tip": {
            "en": item.get("tip_en", "Focus on accurate dates, keywords, and constitutional amendments."),
            "ta": item.get("tip_ta", "துல்லியமான தேதிகள், சொற்கள் மற்றும் திருத்தங்களில் கவனம் செலுத்துங்கள்.")
        },
        "revision_fact": {
            "en": item.get("fact_en", "Preamble summarizes the noble vision and objectives of the Constitution."),
            "ta": item.get("fact_ta", "முகவுரை அரசியலமைப்பின் உன்னத நோக்கங்களைச் சுருக்குகிறது.")
        },
        "source_reference": [
            "TNPSC Group 1 Previous Year Question Papers",
            "M. Laxmikanth - Indian Polity",
            "Samacheer Kalvi Political Science"
        ],
        "bloom_level": "Understand" if item.get("diff") == "Easy" else "Analyze",
        "estimated_time_sec": 45 if item.get("diff") == "Easy" else 60,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "TNPSC PYQ Practice", "PYQ Pattern"],
        
        # Flat legacy fields
        "question_en": item["q_en"],
        "question_ta": item["q_ta"],
        "options_en": [o["en"] for o in item["opts"]],
        "options_ta": [o["ta"] for o in item["opts"]],
        "answer": correct_ans.lower(),
        "explanation_en": item["exp_en"],
        "explanation_ta": item["exp_ta"]
    }
    
    full_questions.append(q_obj)

print(f"Constructed {len(full_questions)} full dual-schema questions.")

target_files = [
    "data/questions/polity/preamble_pyq.json",
    "data/questions/polity/preamble_pyq_practice.json"
]

for tf in target_files:
    os.makedirs(os.path.dirname(tf), exist_ok=True)
    with open(tf, "w", encoding="utf-8") as f:
        json.dump(full_questions, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {len(full_questions)} questions to '{tf}'")
