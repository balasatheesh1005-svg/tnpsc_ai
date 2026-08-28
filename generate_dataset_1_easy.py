# -*- coding: utf-8 -*-
"""
Generator for Dataset 1: Prime Minister Easy MCQs (50 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from pm_mcq_helpers import build_q, make_options, make_distractor

def generate_easy():
    qs = []
    
    # Q1: Article 75(1) Appointment
    qs.append(build_q(
        "POLITY_PM_EASY_001", "Easy", "Easy MCQ",
        "Under which Article of the Indian Constitution is the Prime Minister formally appointed by the President?",
        "இந்திய அரசியலமைப்பின் எந்த உறுப்பின் கீழ் பிரதமர் குடியரசுத் தலைவரால் முறைப்படி நியமிக்கப்படுகிறார்?",
        make_options(
            "Article 74(1)", "உறுப்பு 74(1)",
            "Article 75(1)", "உறுப்பு 75(1)",
            "Article 77(1)", "உறுப்பு 77(1)",
            "Article 78", "உறுப்பு 78"
        ),
        "B",
        "Article 75(1) explicitly states that the Prime Minister shall be appointed by the President. Other ministers are appointed by the President on the advice of the Prime Minister.",
        "அரசியலமைப்பு உறுப்பு 75(1) பிரதமரை குடியரசுத் தலைவர் நியமிப்பார் எனத் தெளிவாகக் கூறுகிறது. மற்ற அமைச்சர்கள் பிரதமரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவரால் நியமிக்கப்படுகின்றனர்.",
        make_distractor(
            "B",
            "Article 74(1) provides for a Council of Ministers with the PM at the head to aid and advise the President, not the appointment clause.",
            "உறுப்பு 74(1) குடியரசுத் தலைவருக்கு உதவவும் ஆலோசணைகள் வழங்கவும் பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவையை வழங்குகிறது; இது நியமனப் பிரிவு அல்ல.",
            "Article 75(1) is the exact constitutional provision empowering the President to appoint the Prime Minister.",
            "உறுப்பு 75(1) குடியரசுத் தலைவருக்குப் பிரதமரை நியமிக்க அதிகாரம் அளிக்கும் துல்லியமான அரசியலமைப்பு விதியாகும்.",
            "Article 77(1) mandates that all executive actions of the Government of India shall be expressed to be taken in the name of the President.",
            "உறுப்பு 77(1) இந்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவரின் பெயரிலேயே மேற்கொள்ளப்பட வேண்டும் என ஆணையிடுகிறது.",
            "Article 78 details the constitutional duties of the Prime Minister to furnish information to the President.",
            "உறுப்பு 78 குடியரசுத் தலைவருக்குத் தகவல்களை வழங்குவதில் பிரதமருக்கு உள்ள அரசியலமைப்பு சார்ந்த கடமைகளை விவரிக்கிறது."
        ),
        "Always remember Article 75(1) is for appointment, while Article 74(1) is for aid and advice.",
        "எப்போதும் நினைவில் கொள்க: நியமனத்திற்கு உறுப்பு 75(1), உதவி மற்றும் ஆலோசனைக்கு உறுப்பு 74(1).",
        "Confusing Article 74(1) (Aid & Advice) with Article 75(1) (Appointment).",
        "உறுப்பு 74(1) (உதவி & ஆலோசனை) மற்றும் உறுப்பு 75(1) (நியமனம்) ஆகியவற்றை குழப்பிக் கொள்ளுதல்.",
        ["Prime Minister Notes Part 1 - Section 1: Constitutional Position (Art 75(1))"]
    ))

    # Q2: Real vs Nominal Executive
    qs.append(build_q(
        "POLITY_PM_EASY_002", "Easy", "Easy MCQ",
        "In the Indian parliamentary system, the Prime Minister holds which of the following executive positions?",
        "இந்திய நாடாளுமன்ற அமைப்பில், பிரதமர் பின்வரும் எந்த நிர்வாகப் பதவியை வகிக்கிறார்?",
        make_options(
            "Nominal Executive (De Jure Head)", "பெயரளவு நிர்வாகி (சட்டபூர்வத் தலைவர்)",
            "Real Executive (De Facto Head)", "உண்மையான நிர்வாகி (உண்மைத் தலைவர்)",
            "Head of State", "நாட்டின் தலைவர் (Head of State)",
            "Judicial Head of Union", "ஒன்றியத்தின் நீதித் துறைத் தலைவர்"
        ),
        "B",
        "In India's parliamentary system, the President is the nominal executive (De Jure Head of State), while the Prime Minister is the real executive (De Facto Head of Government).",
        "இந்திய நாடாளுமன்ற ஜனநாயகத்தில், குடியரசுத் தலைவர் பெயரளவு நிர்வாகியாவார் (சட்டபூர்வத் தலைவர்); ஆனால் பிரதமர் உண்மையான நிர்வாகியாவார் (உண்மைத் தலைவர்).",
        make_distractor(
            "B",
            "The President is the nominal executive (De Jure Head of State), whereas the PM exercises real political and executive authority.",
            "குடியரசுத் தலைவர் பெயரளவு நிர்வாகியாவார்; பிரதமர் உண்மையான அரசியல் மற்றும் நிர்வாக அதிகாரத்தைப் பயன்படுத்துகிறார்.",
            "The Prime Minister is the Real Executive (De Facto Head of Government) who exercises actual power.",
            "பிரதமர் உண்மையான நிர்வாகியாவார் (De Facto Head of Government), அவரே உண்மையான அதிகாரத்தைச் செலுத்துகிறார்.",
            "The Head of State is the President of India, whereas the Prime Minister is the Head of Government.",
            "நாட்டின் தலைவர் (Head of State) குடியரசுத் தலைவர் ஆவார்; பிரதமர் அரசின் தலைவர் (Head of Government) ஆவார்.",
            "The Chief Justice of India heads the judicial branch, not the Prime Minister.",
            "இந்தியத் தலைமை நீதிபதியே நீதித் துறையின் தலைவராவார்; பிரதமர் அல்ல."
        ),
        "TNPSC distinction: President = Head of State (De Jure), PM = Head of Government (De Facto).",
        "TNPSC வேறுபாடு: குடியரசுத் தலைவர் = நாட்டின் தலைவர் (De Jure), பிரதமர் = அரசின் தலைவர் (De Facto).",
        "Confusing Head of State with Head of Government.",
        "நாட்டின் தலைவரையும் அரசின் தலைவரையும் குழப்பிக் கொள்ளுதல்.",
        ["Prime Minister Notes Part 1 - Section 2: Nominal vs Real Executive"]
    ))

    # Q3: Article 75(5) Six Month Rule
    qs.append(build_q(
        "POLITY_PM_EASY_003", "Easy", "Easy MCQ",
        "A person who is not a member of either House of Parliament can be appointed as Prime Minister for a maximum period of:",
        "நாடாளுமன்றத்தின் எந்தவொரு அவையிலும் உறுப்பினராக இல்லாத ஒருவரை அதிகபட்சமாக எவ்வளவு காலத்திற்கு பிரதமராக நியமிக்க முடியும்?",
        make_options(
            "3 months", "3 மாதங்கள்",
            "6 months", "6 மாதங்கள்",
            "1 year", "1 ஆண்டு",
            "5 years", "5 ஆண்டுகள்"
        ),
        "B",
        "Under Article 75(5), a minister (including the PM) who is not a member of Parliament for six consecutive months ceases to be a minister unless elected/nominated to either House.",
        "உறுப்பு 75(5)-ன் படி, நாடாளுமன்றத்தின் இரு அவைகளிலும் உறுப்பினராக இல்லாத ஒருவர் பிரதமராக நியமிக்கப்பட்டால், 6 மாதங்களுக்குள் ஏதேனும் ஒரு அவைக்குத் தேர்ந்தெடுக்கப்பட வேண்டும்.",
        make_distractor(
            "B",
            "Three months is not the constitutional period specified under Article 75(5).",
            "3 மாதங்கள் என்பது உறுப்பு 75(5)-ன் கீழ் குறிப்பிடப்பட்ட அரசியலமைப்பு காலம் அல்ல.",
            "Six months is the exact limit provided by Article 75(5) and upheld by the Supreme Court in 1997.",
            "6 மாதங்கள் என்பது உறுப்பு 75(5)-ல் குறிப்பிடப்பட்டு 1997-ல் உச்ச நீதிமன்றத்தால் உறுதி செய்யப்பட்ட துல்லியமான வரம்பாகும்.",
            "One year exceeds the mandatory six-month parliamentary membership requirement under Article 75(5).",
            "1 ஆண்டு என்பது உறுப்பு 75(5)-ன் கீழ் உள்ள 6 மாத அவகாச வரம்பை விட அதிகமாகும்.",
            "Five years is the normal term of the Lok Sabha, not the non-member grace period.",
            "5 ஆண்டுகள் என்பது மக்களவையின் சாதாரண ஆயுட்காலம்; உறுப்பினர் அல்லாதவருக்கான சலுகைக் காலம் அல்ல."
        ),
        "Art 75(5) applies to both PM and Ministers: max 6 months without being an MP.",
        "உறுப்பு 75(5) பிரதமர் மற்றும் அமைச்சர்கள் இருவருக்குமே பொருந்தும்: எம்பியாக இல்லாமல் அதிகபட்சம் 6 மாதங்கள் மட்டுமே பதவி வகிக்க முடியும்.",
        "Thinking that a PM must be an elected MP at the exact time of taking oath.",
        "பதவியேற்கும் போதே பிரதமர் கட்டாயம் தேர்ந்தெடுக்கப்பட்ட எம்பியாக இருக்க வேண்டும் என நினைப்பது தவறாகும்.",
        ["Prime Minister Notes Part 1 - Section 4: Article 75(5) Six-Month Rule"]
    ))

    # Q4: Article 75(3) Collective Responsibility
    qs.append(build_q(
        "POLITY_PM_EASY_004", "Easy", "Easy MCQ",
        "According to Article 75(3) of the Constitution, the Council of Ministers headed by the Prime Minister is collectively responsible to:",
        "அரசியலமைப்பு உறுப்பு 75(3)-ன் படி, பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவை யாருக்குக் கூட்டாகப் பொறுப்புடையது?",
        make_options(
            "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
            "The Parliament as a whole", "நாடாளுமன்றம் முழுவதற்கும்",
            "The House of the People (Lok Sabha)", "மக்களவைக்கு (Lok Sabha)",
            "The Council of States (Rajya Sabha)", "மாநிலங்களவைக்கு (Rajya Sabha)"
        ),
        "C",
        "Article 75(3) specifically states that the Council of Ministers shall be collectively responsible to the House of the People (Lok Sabha).",
        "அரசியலமைப்பு உறுப்பு 75(3) அமைச்சரவை மக்களவைக்கே (House of the People) கூட்டாகப் பொறுப்புடையது எனத் தெளிவாகக் குறிப்பிடுகிறது.",
        make_distractor(
            "C",
            "Individual responsibility (Art 75(2)) is to the President, but collective responsibility is strictly to the Lok Sabha.",
            "தனிநபர் பொறுப்பு (உறுப்பு 75(2)) குடியரசுத் தலைவருக்கு உரித்தானது; ஆனால் கூட்டுப் பொறுப்பு மக்களவைக்கு மட்டுமே உரியது.",
            "While ministers interact with Parliament, collective responsibility is constitutionally anchored specifically in the Lok Sabha.",
            "அமைச்சர்கள் நாடாளுமன்றத்தை எதிர்கொண்டாலும், அரசியலமைப்பு ரீதியாகக் கூட்டுப் பொறுப்பு மக்களவைக்கு மட்டுமே உரித்தானது.",
            "The Lok Sabha alone represents the directly elected representatives who can pass a No-Confidence Motion.",
            "மக்களவை மட்டுமே நம்பிக்கையில்லாத் தீர்மானத்தைக் கொண்டுவரக்கூடிய நேரடியாகத் தேர்ந்தெடுக்கப்பட்ட அமைப்பாகும்.",
            "Rajya Sabha cannot pass a No-Confidence Motion against the Council of Ministers.",
            "மாநிலங்களவையால் அமைச்சரவைக்கு எதிராக நம்பிக்கையில்லாத் தீர்மானத்தைக் கொண்டுவர முடியாது."
        ),
        "Key exam keyword: Collective responsibility = Lok Sabha (Art 75(3)); Individual responsibility = President (Art 75(2)).",
        "முக்கிய தேர்வு குறிப்பு: கூட்டுப் பொறுப்பு = மக்களவை (75(3)); தனிநபர் பொறுப்பு = குடியரசுத் தலைவர் (75(2)).",
        "Choosing Parliament as a whole instead of Lok Sabha specifically.",
        "மக்களவைக்கு பதிலாக பொதுவான நாடாளுமன்றத்தைத் தேர்ந்தெடுப்பது TNPSC தேர்வுத் தவறாகும்.",
        ["Prime Minister Notes Part 1 - Section 1: Article 75(3) Collective Responsibility"]
    ))

    # Q5: Article 78 Duties
    qs.append(build_q(
        "POLITY_PM_EASY_005", "Easy", "Easy MCQ",
        "Which Article of the Constitution defines the duties of the Prime Minister with respect to furnishing information to the President?",
        "குடியரசுத் தலைவருக்குத் தகவல்களை வழங்குவது தொடர்பான பிரதமரின் கடமைகளை வரையறுக்கும் அரசியலமைப்பு உறுப்பு எது?",
        make_options(
            "Article 74", "உறுப்பு 74",
            "Article 75", "உறுப்பு 75",
            "Article 77", "உறுப்பு 77",
            "Article 78", "உறுப்பு 78"
        ),
        "D",
        "Article 78 outlines the constitutional duties of the Prime Minister to communicate all decisions of the Council of Ministers to the President and furnish information as requested.",
        "அரசியலமைப்பு உறுப்பு 78 அமைச்சரவையின் அனைத்து முடிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவிப்பதும், அவர் கேட்கும் தகவல்களை வழங்குவதும் பிரதமரின் கடமை எனக் கூறுகிறது.",
        make_distractor(
            "D",
            "Article 74 relates to Council of Ministers aiding and advising the President.",
            "உறுப்பு 74 குடியரசுத் தலைவருக்கு உதவவும் ஆலோசனை வழங்கவும் அமைச்சரவை இருப்பதை விவரிக்கிறது.",
            "Article 75 covers appointment, tenure, responsibility, oath, and qualifications of ministers.",
            "உறுப்பு 75 அமைச்சர்களின் நியமனம், பதவிக்காலம், பொறுப்பு, உறுதிமொழி மற்றும் தகுதிகளைப் பற்றியதாகும்.",
            "Article 77 deals with the conduct of executive business of the Government of India.",
            "உறுப்பு 77 இந்திய அரசாங்கத்தின் நிர்வாக நடவடிக்கைகளை நடத்துவது பற்றியதாகும்.",
            "Article 78 is the exact constitutional mandate defining the PM's duties to inform the President.",
            "உறுப்பு 78 குடியரசுத் தலைவருக்குத் தகவல் தெரிவிக்கும் பிரதமரின் கடமைகளை வரையறுக்கும் துல்லியமான அரசியலமைப்பு விதியாகும்."
        ),
        "Remember: Art 78 is the 'bridge of communication' between the PM and the President.",
        "நினைவில் கொள்க: உறுப்பு 78 என்பது பிரதமருக்கும் குடியரசுத் தலைவருக்குமான 'தகவல் தொடர்புகான பாலம்' ஆகும்.",
        "Confusing Article 77 (Conduct of Business) with Article 78 (Duties of PM).",
        "உறுப்பு 77 (நிர்வாக நடத்தைகள்) மற்றும் உறுப்பு 78 (பிரதமரின் கடமைகள்) ஆகியவற்றை குழப்பிக் கொள்ளுதல்.",
        ["Prime Minister Notes Part 2 - Section 1: Article 78 Duties"]
    ))

    # Q6: Minimum Age for PM
    qs.append(build_q(
        "POLITY_PM_EASY_006", "Easy", "Easy MCQ",
        "What is the minimum age required to become the Prime Minister of India if the candidate is a member of the Lok Sabha?",
        "ஒருவர் மக்களவை உறுப்பினராக இருக்கும் பட்சத்தில், இந்தியப் பிரதமராவதற்குத் தேவையான குறைந்தபட்ச வயது என்ன?",
        make_options(
            "21 years", "21 ஆண்டுகள்",
            "25 years", "25 ஆண்டுகள்",
            "30 years", "30 ஆண்டுகள்",
            "35 years", "35 ஆண்டுகள்"
        ),
        "B",
        "The minimum age for Lok Sabha membership is 25 years (Art 84). Hence, a Lok Sabha member can become PM at age 25. If from Rajya Sabha, the minimum age is 30 years.",
        "மக்களவை உறுப்பினராவதற்கான குறைந்தபட்ச வயது 25 ஆண்டுகள் (உறுப்பு 84). எனவே மக்களவை உறுப்பினர் 25 வயதிலேயே பிரதமராக முடியும். மாநிலங்களவை உறுப்பினர் எனில் 30 வயதாகும்.",
        make_distractor(
            "B",
            "21 years is the minimum age for contesting Panchayat/Local Body elections, not Parliament.",
            "21 வயது என்பது உள்ளாட்சித் தேர்தல்களில் போட்டியிடுவதற்கான குறைந்தபட்ச வயதாகும்.",
            "25 years is the correct constitutional minimum age for Lok Sabha members becoming Prime Minister.",
            "25 ஆண்டுகள் என்பது மக்களவை உறுப்பினர் மூலம் பிரதமராவதற்கான சரியான குறைந்தபட்ச அரசியலமைப்பு வயதாகும்.",
            "30 years is the minimum age required if the PM candidate is chosen from the Rajya Sabha.",
            "30 வயது என்பது பிரதமர் மாநிலங்களவை உறுப்பினராக இருக்கும் பட்சத்தில் தேவைப்படும் குறைந்தபட்ச வயதாகும்.",
            "35 years is the minimum age required to become President or Vice-President of India.",
            "35 வயது என்பது குடியரசுத் தலைவர் அல்லது துணைக் குடியரசுத் தலைவராவதற்கான குறைந்தபட்ச வயதாகும்."
        ),
        "Age checklist: Local bodies=21, Lok Sabha/PM=25, Rajya Sabha/PM=30, President/VP=35.",
        "வயது வரம்பு பட்டியல்: உள்ளாட்சி=21, மக்களவை/பிரதமர்=25, மாநிலங்களவை/பிரதமர்=30, குடியரசுத் தலைவர்/துணைக் குடியரசுத் தலைவர்=35.",
        "Confusing Lok Sabha PM minimum age (25) with President minimum age (35).",
        "மக்களவை பிரதமரின் குறைந்தபட்ச வயதையும் (25) குடியரசுத் தலைவரின் குறைந்தபட்ச வயதையும் (35) குழப்பிக் கொள்ளுதல்.",
        ["Prime Minister Notes Part 1 - Section 4: Minimum Age Qualifications"]
    ))

    # Q7: Chairman of NITI Aayog
    qs.append(build_q(
        "POLITY_PM_EASY_007", "Easy", "Easy MCQ",
        "Who serves as the Ex-Officio Chairperson of NITI Aayog?",
        "நிதி ஆயோக்கின் (NITI Aayog) பதவிவழித் தலைவராகச் செயல்படுபவர் யார்?",
        make_options(
            "Union Finance Minister", "ஒன்றிய நிதியமைச்சர்",
            "President of India", "இந்தியக் குடியரசுத் தலைவர்",
            "Prime Minister of India", "இந்தியப் பிரதமர்",
            "Governor of Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி ஆளுநர்"
        ),
        "C",
        "The Prime Minister of India is the Ex-Officio Chairperson of NITI Aayog (National Institution for Transforming India), succeeding the former Planning Commission.",
        "இந்தியப் பிரதமர் நிதி ஆயோக்கின் (NITI Aayog) பதவிவழித் தலைவராகச் (Ex-Officio Chairperson) செயல்படுகிறார்.",
        make_distractor(
            "C",
            "The Finance Minister is a key member/minister in NITI Aayog, but the PM is the Chairperson.",
            "நிதியமைச்சர் நிதி ஆயோக்கின் முக்கிய அமைச்சரவை உறுப்பினராவார், ஆனால் பிரதமர் தலைவராவார்.",
            "The President is not involved in executive chairmanships of policy bodies like NITI Aayog.",
            "குடியரசுத் தலைவர் நிதி ஆயோக் போன்ற கொள்கை அமைப்புகளின் தலைவராகச் செயல்படுவதில்லை.",
            "The Prime Minister is constitutionally and executive-wise designated as Ex-Officio Chairperson of NITI Aayog.",
            "பிரதமர் நிதி ஆயோக்கின் பதவிவழித் தலைவராக நிர்வாக ரீதியாக நியமிக்கப்பட்டுள்ளார்.",
            "The RBI Governor heads India's central bank and monetary policy committee, not NITI Aayog.",
            "ஆர்பிஐ ஆளுநர் ரிசர்வ் வங்கியின் தலைவராவார்; நிதி ஆயோக்கின் தலைவர் அல்ல."
        ),
        "PM is Ex-Officio Chairman of NITI Aayog, Inter-State Council, National Integration Council, and National Water Resources Council.",
        "நிதி ஆயோக், மாநிலங்களுக்கு இடையேயான குழு, தேசிய ஒருமைப்பாட்டு கவுன்சில் ஆகியவற்றின் தலைவர் பிரதமராவார்.",
        "Assuming the Union Finance Minister heads NITI Aayog.",
        "ஒன்றிய நிதியமைச்சரே நிதி ஆயோக்கின் தலைவர் எனத் தவறாகக் கருதுதல்.",
        ["Prime Minister Notes Part 2 - Section 5: Institutional Ex-Officio Chairmanships"]
    ))

    # Q8: Oath Administration
    qs.append(build_q(
        "POLITY_PM_EASY_008", "Easy", "Easy MCQ",
        "Who administers the Oath of Office and Secrecy to the Prime Minister of India?",
        "இந்தியப் பிரதமருக்கு பதவிப் பிரமாணமும் இரகசியக் காப்புப் பிரமாணமும் செய்து வைப்பவர் யார்?",
        make_options(
            "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
            "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்",
            "President of India", "இந்தியக் குடியரசுத் தலைவர்",
            "Outgoing Prime Minister", "பதவி விலகும் பிரதமர்"
        ),
        "C",
        "Under Article 75(4), before a Minister (including PM) enters upon office, the President (or a person appointed by him) administers the oaths of office and secrecy according to the Third Schedule.",
        "அரசியலமைப்பு உறுப்பு 75(4)-ன் படி, பிரதமர் பதவியேற்கும் முன், 3வது அட்டவணையின்படி குடியரசுத் தலைவர் அவர்களுக்குப் பதவிப் பிரமாணமும் இரகசியக் காப்புப் பிரமாணமும் செய்து வைக்கிறார்.",
        make_distractor(
            "C",
            "The Chief Justice of India administers oath to the President, not to the Prime Minister.",
            "இந்தியத் தலைமை நீதிபதி குடியரசுத் தலைவருக்குப் பிரமாணம் செய்து வைக்கிறார்; பிரதமருக்கு அல்ல.",
            "The Speaker of Lok Sabha presides over Lok Sabha debates and does not administer oath to PM.",
            "சபாநாயகர் மக்களவை விவாதங்களை நடத்துபவர்; பிரதமருக்குப் பிரமாணம் செய்து வைப்பவர் அல்ல.",
            "The President of India is constitutionally authorized under Article 75(4) to administer oaths to the PM.",
            "அரசியலமைப்பு உறுப்பு 75(4)-ன் கீழ் பிரதமருக்குப் பிரமாணம் செய்து வைக்க குடியரசுத் தலைவருக்கே அதிகாரம் உள்ளது.",
            "The outgoing PM has no constitutional role in administering oaths to the successor.",
            "பதவி விலகும் பிரதமருக்குப் புதிய பிரதமருக்குப் பிரமாணம் செய்து வைக்கும் அரசியலமைப்பு அதிகாரம் இல்லை."
        ),
        "CJI administers oath to President; President administers oath to PM, Vice-President, and CJI.",
        "குடியரசுத் தலைவருக்கு CJI பிரமாணம் செய்து வைப்பார்; பிரதமர், துணைக் குடியரசுத் தலைவர், CJI ஆகியோருக்கு குடியரசுத் தலைவர் பிரமாணம் செய்து வைப்பார்.",
        "Confusing oath of President (by CJI) with oath of PM (by President).",
        "குடியரசுத் தலைவரின் பிரமாணத்தையும் பிரதமரின் பிரமாணத்தையும் குழப்பிக் கொள்ளுதல்.",
        ["Prime Minister Notes Part 1 - Section 5: Oath Administration (Art 75(4))"]
    ))

    # Q9: Inter-State Council Chairman
    qs.append(build_q(
        "POLITY_PM_EASY_009", "Easy", "Easy MCQ",
        "Under Article 263, who is the Chairperson of the Inter-State Council?",
        "அரசியலமைப்பு உறுப்பு 263-ன் கீழ் அமைக்கப்படும் மாநிலங்களுக்கு இடையேயான குழுவின் (Inter-State Council) தலைவர் யார்?",
        make_options(
            "Union Home Minister", "ஒன்றிய உள்துறை அமைச்சர்",
            "Prime Minister of India", "இந்தியப் பிரதமர்",
            "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
            "Chairman of Rajya Sabha", "மாநிலங்களவைத் தலைவர்"
        ),
        "B",
        "The Inter-State Council set up under Article 263 (established in 1990 based on Sarkaria Commission recommendations) is chaired by the Prime Minister of India.",
        "அரசியலமைப்பு உறுப்பு 263-ன் கீழ் (சர்க்காரியா ஆணைய பரிந்துரையால் 1990-ல் அமைக்கப்பட்ட) மாநிலங்களுக்கு இடையேயான குழுவின் தலைவராக இந்தியப் பிரதமர் செயல்படுகிறார்.",
        make_distractor(
            "B",
            "The Union Home Minister is a prominent member, but not the Chairman of the Inter-State Council.",
            "ஒன்றிய உள்துறை அமைச்சர் இதில் முக்கிய உறுப்பினராவார், ஆனால் தலைவர் அல்ல.",
            "The Prime Minister is the constitutional Chairperson of the Inter-State Council under Article 263.",
            "பிரதமரே உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையேயான குழுவின் தலைவராவார்.",
            "The Chief Justice of India does not participate in administrative councils like the Inter-State Council.",
            "இந்தியத் தலைமை நீதிபதி மாநிலங்களுக்கு இடையேயான குழு போன்ற நிர்வாக அமைப்புகளில் பங்கேற்பதில்லை.",
            "The Chairman of Rajya Sabha (Vice-President) presides over Rajya Sabha, not Inter-State Council.",
            "மாநிலங்களவைத் தலைவர் மாநிலங்களவையை நடத்துபவர்; இக்குழுவின் தலைவர் அல்ல."
        ),
        "Inter-State Council created under Art 263 -> Chaired by PM (Sarkaria Commission rec).",
        "உறுப்பு 263-ன் கீழ் அமைக்கப்பட்ட மாநிலங்களுக்கு இடையேயான குழு -> தலைவர் பிரதமர்.",
        "Thinking Union Home Minister chairs the Inter-State Council instead of PM.",
        "உள்துறை அமைச்சரே இதன் தலைவர் எனக் குழம்புவது TNPSC பொதுத் தவறாகும்.",
        ["Prime Minister Notes Part 2 - Section 5: Article 263 Inter-State Council"]
    ))

    # Q10: First PM of India
    qs.append(build_q(
        "POLITY_PM_EASY_010", "Easy", "Easy MCQ",
        "Who was the first Prime Minister of Independent India and also had the longest tenure in office?",
        "சுதந்திர இந்தியாவின் முதல் பிரதமராகவும், மிக நீண்ட காலம் பதவி வகித்த பிரதமராகவும் இருந்தவர் யார்?",
        make_options(
            "Sardar Vallabhbhai Patel", "சர்மித் சர்தார் வல்லபாய் படேல்",
            "Jawaharlal Nehru", "ஜவஹர்லால் நேரு",
            "Lal Bahadur Shastri", "லால் பகதூர் சாஸ்திரி",
            "Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்"
        ),
        "B",
        "Pandit Jawaharlal Nehru was India's first Prime Minister (August 15, 1947 – May 27, 1964) and holds the record for the longest continuous tenure (16 years and 286 days).",
        "பண்டிட் ஜவஹர்லால் நேரு சுதந்திர இந்தியாவின் முதல் பிரதமராவார் (15 ஆகஸ்ட் 1947 - 27 மே 1964); அவரே மிக நீண்ட காலம் (16 ஆண்டுகள் 286 நாட்கள்) பதவி வகித்தவராவார்.",
        make_distractor(
            "B",
            "Sardar Vallabhbhai Patel was India's first Deputy Prime Minister and first Home Minister.",
            "சர்தார் வல்லபாய் படேல் இந்தியாவின் முதல் துணைப் பிரதமரும் முதல் உள்துறை அமைச்சருமாவார்.",
            "Jawaharlal Nehru served continuously from 1947 until his death in 1964 as India's first and longest-serving PM.",
            "ஜவஹர்லால் நேரு 1947 முதல் 1964 வரை இந்தியாவின் முதல் மற்றும் மிக நீண்ட காலம் பதவி வகித்த பிரதமராக இருந்தார்.",
            "Lal Bahadur Shastri succeeded Nehru as India's second Prime Minister in 1964.",
            "லால் பகதூர் சாஸ்திரி 1964-ல் நேருவுக்குப் பிறகு இந்தியாவின் 2வது பிரதமரானார்.",
            "Dr. B.R. Ambedkar was India's first Law Minister and Chairman of the Drafting Committee.",
            "டாக்டர் பி.ஆர். அம்பேத்கர் இந்தியாவின் முதல் சட்ட அமைச்சரும் வரைவுக் குழுவின் தலைவருமாவார்."
        ),
        "Nehru = First PM & Longest Serving PM (1947–1964).",
        "நேரு = முதல் பிரதமர் & மிக நீண்ட காலம் பதவி வகித்தவர் (1947–1964).",
        "Confusing Deputy PM (Patel) with PM (Nehru).",
        "துணைப் பிரதமரையும் பிரதமரையும் குழப்பிக் கொள்ளுதல்.",
        ["Prime Minister Notes Part 1 - Section 2: Historical Prime Ministers Overview"]
    ))

    # Save initial 10 to check progress, continue loop for full 50...
    # Generating remaining 40 questions (Q11 to Q50) with high specificity:

    # Q11: First Woman PM
    qs.append(build_q(
        "POLITY_PM_EASY_011", "Easy", "Easy MCQ",
        "Who was the first woman Prime Minister of India?",
        "இந்தியாவின் முதல் பெண் பிரதமர் யார்?",
        make_options(
            "Sarojini Naidu", "சரோஜினி நாயுடு",
            "Sucheta Kripalani", "சுசேதா கிருபாளனி",
            "Indira Gandhi", "இந்திரா காந்தி",
            "Pratibha Patil", "பிரதிபா பாட்டீல்"
        ),
        "C",
        "Indira Gandhi became India's first female Prime Minister in 1966. Sarojini Naidu was first woman Governor, Sucheta Kripalani was first woman CM, Pratibha Patil was first woman President.",
        "இந்திரா காந்தி 1966-ல் இந்தியாவின் முதல் பெண் பிரதமரானார். சரோஜினி நாயுடு முதல் பெண் ஆளுநர், சுசேதா கிருபாளனி முதல் பெண் முதல்வர், பிரதிபா பாட்டீல் முதல் பெண் குடியரசுத் தலைவர்.",
        make_distractor(
            "C",
            "Sarojini Naidu was the first female Governor of an Indian state (UP).",
            "சரோஜினி நாயுடு இந்தியாவின் முதல் பெண் ஆளுநர் (உத்தரப் பிரதேசம்).",
            "Sucheta Kripalani was the first female Chief Minister of an Indian state (UP).",
            "சுசேதா கிருபாளனி இந்தியாவின் முதல் பெண் முதல்வர் (உத்தரப் பிரதேசம்).",
            "Indira Gandhi served as India's first woman Prime Minister from 1966 to 1977 and 1980 to 1984.",
            "இந்திரா காந்தி இந்தியாவின் முதல் பெண் பிரதமராகச் பணியாற்றினார்.",
            "Pratibha Patil was India's first woman President (2007–2012).",
            "பிரதிபா பாட்டீல் இந்தியாவின் முதல் பெண் குடியரசுத் தலைவராவார்."
        ),
        "First women landmarks: CM=Sucheta Kripalani, Governor=Sarojini Naidu, PM=Indira Gandhi, President=Pratibha Patil.",
        "முக்கிய பெண் தலைவர்கள்: முதல்வர்=சுசேதா, ஆளுநர்=சரோஜினி, பிரதமர்=இந்திரா காந்தி, குடியரசுத் தலைவர்=பிரதிபா பாட்டீல்.",
        "Confusing female CM, Governor, PM and President roles.",
        "பெண் முதல்வர், ஆளுநர், பிரதமர், குடியரசுத் தலைவர் பதவிகளைக் குழப்புவது.",
        ["Prime Minister Notes Part 1 - Section 2: Historical Prime Ministers"]
    ))

    # Q12: 91st Amendment 15% limit
    qs.append(build_q(
        "POLITY_PM_EASY_012", "Easy", "Easy MCQ",
        "Which Constitutional Amendment Act capped the total number of ministers, including the Prime Minister, at 15% of the total strength of the Lok Sabha?",
        "பிரதமர் உட்பட மொத்த அமைச்சர்களின் எண்ணிக்கையை மக்களவையின் மொத்த உறுப்பினர்களில் 15% ஆக வரம்பிட்ட அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        make_options(
            "42nd Amendment Act, 1976", "42-வது திருத்தச் சட்டம், 1976",
            "44th Amendment Act, 1978", "44-வது திருத்தச் சட்டம், 1978",
            "91st Amendment Act, 2003", "91-வது திருத்தச் சட்டம், 2003",
            "86th Amendment Act, 2002", "86-வது திருத்தச் சட்டம், 2002"
        ),
        "C",
        "The 91st Constitutional Amendment Act of 2003 inserted Article 75(1A), restricting the size of the Union Council of Ministers (including PM) to 15% of Lok Sabha membership.",
        "2003-ஆம் ஆண்டின் 91-வது அரசியலமைப்புத் திருத்தச் சட்டம் உறுப்பு 75(1A)-ஐ இணைத்து, பிரதமர் உட்பட அமைச்சர்களின் எண்ணிக்கையை மக்களவை பலத்தில் 15% ஆக வரம்பிட்டது.",
        make_distractor(
            "C",
            "42nd Amendment 1976 made Presidential aid and advice binding under Article 74.",
            "42வது திருத்தம் குடியரசுத் தலைவருக்கு அமைச்சரவையின் ஆலோசனையைக் கட்டாயமாக்கியது.",
            "44th Amendment 1978 added reconsideration clause in Article 74(1).",
            "44வது திருத்தம் அமைச்சரவை ஆலோசனையை மறுபரிசீலனைக்கு அனுப்பும் உரிமையை வழங்கியது.",
            "91st Amendment 2003 added Art 75(1A) setting the 15% limit on Council of Ministers size.",
            "91வது திருத்தம் 2003 உறுப்பு 75(1A)-ல் 15% அமைச்சரவை வரம்பை நிர்ணயித்தது.",
            "86th Amendment 2002 made Right to Education a Fundamental Right under Article 21A.",
            "86வது திருத்தம் 2002 கல்வி உரிமையை அடிப்படை உரிமையாக்கியது."
        ),
        "91st Amendment 2003 = 15% limit on Council of Ministers size (including PM).",
        "91வது திருத்தம் 2003 = 15% அமைச்சரவை வரம்பு (பிரதமர் உட்பட).",
        "Confusing 44th Amendment with 91st Amendment on Council of Ministers rules.",
        "44வது மற்றும் 91வது திருத்தங்களைக் குழப்பிக் கொள்ளுதல்.",
        ["Prime Minister Notes Part 1 - Section 1: Article 75(1A) Size Limit"]
    ))

    # Q13: Resignation of PM effect
    qs.append(build_q(
        "POLITY_PM_EASY_013", "Easy", "Easy MCQ",
        "What happens to the Union Council of Ministers if the Prime Minister resigns or dies while in office?",
        "பிரதமர் பதவியில் இருக்கும் போது ராஜினாமா செய்தாலோ அல்லது இறந்தாலோ ஒன்றிய அமைச்சரவைக்கு என்ன நிகழும்?",
        make_options(
            "Only the PM's office becomes vacant, other ministers continue.", "பிரதமர் பதவி மட்டுமே காலியாகும், மற்ற அமைச்சர்கள் தொடர்வார்கள்.",
            "The Council of Ministers automatically dissolves.", "அமைச்சரவை தானாகவே கலைந்துவிடும் (Dissolves).",
            "The Vice-President automatically becomes Prime Minister.", "துணைக் குடியரசுத் தலைவர் தானாகவே பிரதமராவார்.",
            "Lok Sabha is automatically dissolved.", "மக்களவை தானாகவே கலைக்கப்படும்."
        ),
        "B",
        "Since the Prime Minister is the keystone of the Cabinet arch, the resignation or death of an incumbent PM automatically dissolves the Council of Ministers.",
        "பிரதமரே அமைச்சரவையின் மையத் தூண் (Keystone of Cabinet arch) என்பதால், அவர் பதவி விலகினாலும் அல்லது இறந்தாலும் அமைச்சரவை தானாகவே கலைந்துவிடும்.",
        make_distractor(
            "B",
            "Individual ministers cannot function without the PM; the entire Council collapses.",
            "பிரதமர் இல்லாமல் தனிப்பட்ட அமைச்சர்கள் செயல்பட முடியாது; முழு அமைச்சரவையும் வீழும்.",
            "The resignation or death of the Prime Minister automatically dissolves the Council of Ministers.",
            "பிரதமரின் ராஜினாமா அல்லது இறப்பு அமைச்சரவையைத் தானாகவே கலைத்துவிடும்.",
            "The Vice-President presides over Rajya Sabha and does not step in as PM automatically.",
            "துணைக் குடியரசுத் தலைவர் தானாகப் பிரதமராக முடியாது; குடியரசுத் தலைவர் புதிய பிரதமரை நியமிக்க வேண்டும்.",
            "The Lok Sabha does not dissolve automatically; only the Council of Ministers dissolves to allow a new PM to be appointed.",
            "மக்களவை தானாகக் கலையாது; புதிய பிரதமரை நியமிக்க அமைச்சரவை மட்டுமே கலைகிறது."
        ),
        "Keystone concept: PM's resignation/death = Council of Ministers dissolves; Minister's resignation/death = Vacancy created.",
        "மையக் கோட்பாடு: பிரதமரின் இறப்பு/ராஜினாமா = அமைச்சரவை கலைப்பு; அமைச்சரின் இறப்பு/ராஜினாமா = வெறுமனே காலியிடம்.",
        "Thinking that the Vice-President becomes PM upon PM's death.",
        "பிரதமர் இறந்தால் துணைக் குடியரசுத் தலைவர் பிரதமராவார் என நினைப்பது தவறு (அமெரிக்க அதிபர் முறை வேறு).",
        ["Prime Minister Notes Part 1 - Section 2: Leadership & Keystone Role"]
    ))

    # Q14: First Non-Congress PM
    qs.append(build_q(
        "POLITY_PM_EASY_014", "Easy", "Easy MCQ",
        "Who was the first non-Congress Prime Minister of India?",
        "இந்தியாவின் முதல் காங்கிரஸ் அல்லாத பிரதமர் யார்?",
        make_options(
            "Charan Singh", "சரன் சிங்",
            "Morarji Desai", "மொரார்ஜி தேசாய்",
            "Atal Bihari Vajpayee", "அடல் பிஹாரி வாஜ்பாய்",
            "V.P. Singh", "வி.பி. சிங்"
        ),
        "B",
        "Morarji Desai became India's first non-Congress Prime Minister in March 1977, heading the Janata Party government after the Emergency.",
        "மொரார்ஜி தேசாய் 1977 மார்ச்சில் அவசரநிலைக்குப் பிறகு ஜனதா கட்சி சார்பில் இந்தியாவின் முதல் காங்கிரஸ் அல்லாத பிரதமரானார்.",
        make_distractor(
            "B",
            "Charan Singh headed a coalition government later in 1979 after Desai resigned.",
            "சரன் சிங் 1979-ல் மொரார்ஜி தேசாய் விலகிய பிறகே பிரதமரானார்.",
            "Morarji Desai led the Janata Party to power in 1977 as the first non-Congress PM.",
            "மொரார்ஜி தேசாய் 1977-ல் ஜனதா கட்சியின் தலைவராக முதல் காங்கிரஸ் அல்லாத பிரதமரானார்.",
            "Atal Bihari Vajpayee was the first non-Congress PM to complete a full 5-year term (1999–2004).",
            "வாஜ்பாய் 5 ஆண்டு கால முழு ஆட்சியை நிறைவு செய்த முதல் காங்கிரஸ் அல்லாத பிரதமராவார்.",
            "V.P. Singh led the National Front government in 1989.",
            "வி.பி. சிங் 1989-ல் தேசிய முன்னணி அரசை வழிநடத்தினார்."
        ),
        "First non-Congress PM = Morarji Desai (1977); First non-Congress PM to finish full 5-yr term = Vajpayee (1999–2004).",
        "முதல் காங்கிரஸ் அல்லாத பிரதமர் = மொரார்ஜி தேசாய்; 5 ஆண்டுகள் நிறைவு செய்தவர் = வாஜ்பாய்.",
        "Confusing Morarji Desai (1977) with Vajpayee (1996/1999).",
        "மொரார்ஜி தேசாய் மற்றும் வாஜ்பாய் ஆகிய இருவரின் சாதனைகளைக் குழப்புவது.",
        ["Prime Minister Notes Part 1 - Section 2: Historical Prime Ministers"]
    ))

    # Q15: Article 74 Advice Court Bar
    qs.append(build_q(
        "POLITY_PM_EASY_015", "Easy", "Easy MCQ",
        "According to Article 74(2) of the Indian Constitution, the question whether any, and if so what, advice was tendered by Ministers to the President:",
        "இந்திய அரசியலமைப்பு உறுப்பு 74(2)-ன் படி, அமைச்சர்கள் குடியரசுத் தலைவருக்கு ஏதேனும் ஆலோசனை வழங்கினார்களா, வழங்கினால் அது என்ன என்ற கேள்வி:",
        make_options(
            "Shall be inquired into by the Supreme Court only", "உச்ச நீதிமன்றத்தால் மட்டுமே விசாரிக்கப்பட வேண்டும்",
            "Shall not be inquired into in any court", "எந்தவொரு நீதிமன்றத்திலும் விசாரிக்கப்படக் கூடாது",
            "Shall be reviewed by Parliament", "நாடாளுமன்றத்தால் மறுபரிசீலனை செய்யப்பட வேண்டும்",
            "Shall be published in the Official Gazette", "அரசிதழில் வெளியிடப்பட வேண்டும்"
        ),
        "B",
        "Article 74(2) explicitly bars judicial inquiry by stating: 'The question whether any, and if so what, advice was tendered by Ministers to the President shall not be inquired into in any court.'",
        "அரசியலமைப்பு உறுப்பு 74(2) 'அமைச்சர்கள் குடியரசுத் தலைவருக்கு வழங்கிய ஆலோசனை குறித்து எந்தவொரு நீதிமன்றமும் விசாரிக்கக் கூடாது' எனத் துல்லியமாகத் தடை விதிக்கிறது.",
        make_distractor(
            "B",
            "Courts are expressly barred from inquiring into Ministerial advice under Article 74(2).",
            "உறுப்பு 74(2)-ன் கீழ் நீதிமன்றங்கள் அமைச்சரவை ஆலோசனையை விசாரிக்கத் தடை விதிக்கப்பட்டுள்ளது.",
            "Article 74(2) creates an absolute constitutional immunity preventing judicial inspection of ministerial advice.",
            "உறுப்பு 74(2) நீதிமன்றங்கள் ஆலோசனையை ஆய்வு செய்வதைத் தடுக்கும் முமுமையான பாதுகாப்பை வழங்குகிறது.",
            "Parliament discusses government business but does not inquire into confidential advice to President under Art 74(2).",
            "நாடாளுமன்றம் அரசைக் கேள்வி கேட்கலாம், ஆனால் உறுப்பு 74(2)-ன் கீழ் உள்ள இரகசிய ஆலோசனையை ஆய்வு செய்வதில்லை.",
            "Ministerial advice to President is confidential and never published in the Gazette.",
            "அமைச்சரவை ஆலோசனை இரகசியமானது; அரசிதழில் வெளியிடப்படுவதில்லை."
        ),
        "Art 74(2) protects secrecy of advice: No court can inquire into advice tendered by ministers to President.",
        "உறுப்பு 74(2) ஆலோசனையின் இரகசியத்தைப் பாதுகாக்கிறது: நீதிமன்றங்கள் இதை விசாரிக்க முடியாது.",
        "Thinking Supreme Court has jurisdiction to inspect advice under Article 74(2).",
        "உச்ச நீதிமன்றம் உறுப்பு 74(2) ஆலோசனையை ஆய்வு செய்ய முடியும் என தவறாகக் நினைப்பது.",
        ["Prime Minister Notes Part 1 - Section 1: Article 74(2) Judicial Immunity"]
    ))

    # Q16: PM who never faced Parliament
    qs.append(build_q(
        "POLITY_PM_EASY_016", "Easy", "Easy MCQ",
        "Who among the following Prime Ministers of India never faced the Parliament during his tenure?",
        "இந்தியப் பிரதமர்களில் தனது பதவிக் காலத்தில் நாடாளுமன்றத்தையே எதிர்கொள்ளாத ஒரே பிரதமர் யார்?",
        make_options(
            "Chandra Shekhar", "சந்திர சேகர்",
            "Charan Singh", "சரன் சிங்",
            "H.D. Deve Gowda", "எச்.டி. தேவேகவுடா",
            "I.K. Gujral", "ஐ.கே. குஜ்ரால்"
        ),
        "B",
        "Chaudhary Charan Singh served as Prime Minister from July 1979 to January 1980 and resigned before the Lok Sabha convened, making him the only PM who never faced Parliament.",
        "சவுத்ரி சரன் சிங் 1979 ஜூலை முதல் 1980 ஜனவரி வரை பிரதமராக இருந்தார். மக்களவை கூடுவதற்கு முன்பே ராஜினாமா செய்ததால் நாடாளுமன்றத்தையே எதிர்கொள்ளாத ஒரே பிரதமரானார்.",
        make_distractor(
            "B",
            "Chandra Shekhar faced Parliament and proved his majority in 1990.",
            "சந்திர சேகர் 1990-ல் நாடாளுமன்றத்தை எதிர்கொண்டு பெரும்பான்மையை நிரூபித்தார்.",
            "Charan Singh resigned prior to the scheduled Lok Sabha session after Congress withdrew support.",
            "காங்கிரஸ் ஆதரவை திரும்பப் பெற்றதால் சரன் சிங் நாடாளுமன்றக் கூட்டம் தொடங்குவதற்கு முன்பே பதவி விலகினார்.",
            "H.D. Deve Gowda faced Parliament and was defeated on a confidence motion in 1997.",
            "தேவேகவுடா 1997-ல் நாடாளுமன்றத்தை எதிர்கொண்டார்.",
            "I.K. Gujral addressed Parliament during his tenure in 1997.",
            "ஐ.கே. குஜ்ரால் 1997-ல் நாடாளுமன்றத்தை எதிர்கொண்டார்."
        ),
        "Unique TNPSC fact: Charan Singh = Only PM who never faced Parliament.",
        "TNPSC தனித்துவமான உண்மை: சரன் சிங் = நாடாளுமன்றத்தை எதிர்கொள்ளாத ஒரே பிரதமர்.",
        "Confusing Charan Singh with Chandra Shekhar.",
        "சரன் சிங்கையும் சந்திர சேகரையும் குழப்பிக் கொள்ளுதல்.",
        ["Prime Minister Notes Part 1 - Section 2: Historical Prime Ministers"]
    ))

    # Q17: First PM defeated by No Confidence Motion
    qs.append(build_q(
        "POLITY_PM_EASY_017", "Easy", "Easy MCQ",
        "Who was the first Prime Minister of India to be forced out of office by a No-Confidence Motion passed in the Lok Sabha?",
        "மக்களவையில் நம்பிக்கையில்லாத் தீர்மானம் நிறைவேற்றப்பட்டதன் மூலம் பதவியிழந்த முதல் இந்தியப் பிரதமர் யார்?",
        make_options(
            "Morarji Desai", "மொரார்ஜி தேசாய்",
            "V.P. Singh", "வி.பி. சிங்",
            "Atal Bihari Vajpayee", "அடல் பிஹாரி வாஜ்பாய்",
            "H.D. Deve Gowda", "எச்.டி. தேவேகவுடா"
        ),
        "B",
        "Vishwanath Pratap (V.P.) Singh was the first Prime Minister to lose office following the passage of a No-Confidence Motion on November 7, 1990.",
        "விஸ்வநாத் பிரதாப் (வி.பி.) சிங் 1990 நவம்பர் 7 அன்று மக்களவையில் நம்பிக்கையில்லாத் தீர்மானம் தோற்கடிக்கப்பட்டதால் பதவியிழந்த முதல் பிரதமராவார்.",
        make_distractor(
            "B",
            "Morarji Desai resigned in July 1979 before the vote on no-confidence motion was concluded.",
            "மொரார்ஜி தேசாய் நம்பிக்கையில்லாத் தீர்மான வாக்கெடுப்பு முடிவதற்கு முன்பே ராஜினாமா செய்தார்.",
            "V.P. Singh actually faced the vote on the floor of Lok Sabha and was defeated in Nov 1990.",
            "வி.பி. சிங் 1990 நவம்பரில் மக்களவையில் ஓட்டெடுப்பை எதிர்கொண்டு நம்பிக்கையில்லாத் தீர்மானத்தில் தோற்கடிக்கப்பட்டார்.",
            "Vajpayee lost a Confidence Motion by 1 vote in 1999, but V.P. Singh was first in 1990.",
            "வாஜ்பாய் 1999-ல் 1 வாக்கில் நம்பிக்கை வாக்கெடுப்பில் தோற்றார்; ஆனால் முதல் பிரதமர் வி.பி. சிங் ஆவார்.",
            "Deve Gowda lost a confidence vote later in April 1997.",
            "தேவேகவுடா 1997 ஏப்ரலில்தான் நம்பிக்கை வாக்கெடுப்பில் தோற்றார்."
        ),
        "First PM to lose No-Confidence Motion = V.P. Singh (Nov 1990). Morarji Desai resigned before vote in 1979.",
        "நம்பிக்கையில்லாத் தீர்மானத்தில் தோற்ற முதல் பிரதமர் = வி.பி. சிங் (1990). மொரார்ஜி தேசாய் வாக்கெடுப்புக்கு முன்பே ராஜினாமா செய்தார்.",
        "Assuming Morarji Desai was defeated by no-confidence motion.",
        "மொரார்ஜி தேசாயே தீர்மானத்தில் தோற்றார் எனக் கருதுவது தவறு.",
        ["Prime Minister Notes Part 3 - Section 1: No-Confidence Motion History"]
    ))

    # Q18: Article 88 Right to Speak
    qs.append(build_q(
        "POLITY_PM_EASY_018", "Easy", "Easy MCQ",
        "Under Article 88, a Union Minister has the right to speak and participate in the proceedings of either House of Parliament, but cannot vote in a House unless:",
        "உறுப்பு 88-ன் படி, ஒரு ஒன்றிய அமைச்சர் நாடாளுமன்றத்தின் எந்த அவையிலும் பேசவும் பங்கேற்கவும் உரிமை உண்டு; ஆனால் எந்த அவையில் வாக்களிக்க முடியாது?",
        make_options(
            "He is a Cabinet Minister", "அவர் அமைச்சரவை (Cabinet) அமைச்சராக இருந்தால் ஒழிய",
            "He is a member of that specific House", "அவர் குறிப்பிட்ட அவையின் உறுப்பினராக இருந்தால் ஒழிய",
            "He obtains permission from the President", "குடியரசுத் தலைவரிடம் அனுமதி பெற்றால் ஒழிய",
            "He has served for at least 5 years", "அவர் குறைந்தபட்சம் 5 ஆண்டுகள் பணியாற்றினால் ஒழிய"
        ),
        "B",
        "Article 88 allows every Minister to speak and take part in both Lok Sabha and Rajya Sabha, but explicitly specifies that a Minister can vote ONLY in the House of which he is a member.",
        "அரசியலமைப்பு உறுப்பு 88 ஒரு அமைச்சர் இரு அவைகளிலும் பேசலாம் எனக் கூறுகிறது; ஆனால் அவர் உறுப்பினராக உள்ள அவையில் மட்டுமே வாக்களிக்க முடியும்.",
        make_distractor(
            "B",
            "Cabinet rank gives executive authority, but does not grant voting rights in a House where the Minister is not a member.",
            "கேபினட் பதவி உறுப்பினர் அல்லாத அவையில் வாக்களிக்கும் உரிமையை வழங்காது.",
            "Article 88 restricts voting strictly to the House in which the Minister holds membership.",
            "உறுப்பு 88 வாக்களிக்கும் உரிமையை அமைச்சர் உறுப்பினராக இருக்கும் அவைக்கு மட்டுமே வரையறுக்கிறது.",
            "The President cannot grant voting rights in Parliament contrary to Article 88.",
            "குடியரசுத் தலைவர் உறுப்பு 88-க்கு மாறாக வாக்களிக்கும் உரிமையை வழங்க முடியாது.",
            "Tenure length does not alter the mandatory parliamentary voting rule under Article 88.",
            "பதவிக் காலம் வாக்களிக்கும் விதியை மாற்றாது."
        ),
        "Art 88 golden rule: Speak in BOTH houses, Vote ONLY in OWN house.",
        "உறுப்பு 88 தங்க விதி: இரு அவைகளிலும் பேசலாம்; சொந்த அவையில் மட்டுமே வாக்களிக்க முடியும்.",
        "Thinking a Minister can vote in both Houses under Article 88.",
        "அமைச்சர் இரு அவைகளிலும் வாக்களிக்கலாம் என நினைப்பது தவறான கருத்தாகும்.",
        ["Prime Minister Notes Part 1 - Section 6: Article 88 Rights in Parliament"]
    ))

    # Q19: Cabinet word in Constitution
    qs.append(build_q(
        "POLITY_PM_EASY_019", "Easy", "Easy MCQ",
        "The word 'Cabinet' was not in the original Constitution of India. In which Article was it inserted by the 44th Constitutional Amendment Act, 1978?",
        "'கேபினட்' (Cabinet) என்ற சொல் மூல அரசியலமைப்பில் இல்லை. 1978-ஆம் ஆண்டின் 44-வது திருத்தச் சட்டத்தின் மூலம் இது எந்த உறுப்பில் சேர்க்கப்பட்டது?",
        make_options(
            "Article 74", "உறுப்பு 74",
            "Article 75", "உறுப்பு 75",
            "Article 352", "உறுப்பு 352",
            "Article 78", "உறுப்பு 78"
        ),
        "C",
        "The term 'Cabinet' appears only ONCE in the Indian Constitution, inserted into Article 352 by the 44th Amendment Act (1978), defining it as the Council consisting of PM and other Cabinet Ministers.",
        "'கேபினட்' என்ற சொல் அரசியலமைப்பில் ஒரே ஒரு முறை மட்டுமே இடம்பெறுகிறது. 44-வது திருத்தச் சட்டம் (1978) மூலம் உறுப்பு 352-ல் 'தேசிய அவசரநிலை' அறிவிப்பு தொடர்பான பகுதியில் இது சேர்க்கப்பட்டது.",
        make_distractor(
            "C",
            "Article 74 refers to Council of Ministers (Mantriparishad), not Cabinet (Mantrimandal).",
            "உறுப்பு 74 அமைச்சரவை (Council of Ministers) என்றே குறிப்பிடுகிறது.",
            "Article 75 details ministers' appointment and responsibility without using the term Cabinet.",
            "உறுப்பு 75 கேபினட் என்ற சொல்லைப் பயன்படுத்தவில்லை.",
            "Article 352 is the ONLY constitutional article where the word 'Cabinet' is explicitly defined.",
            "உறுப்பு 352 மட்டுமே 'கேபினட்' என்ற சொல் இடம்பெற்றுள்ள ஒரே அரசியலமைப்பு உறுப்பாகும்.",
            "Article 78 outlines PM's duties to President and does not mention Cabinet.",
            "உறுப்பு 78 கேபினட் என்ற சொல்லைக் கொண்டிருக்கவில்லை."
        ),
        "TNPSC favorite trap: Word 'Cabinet' appears ONLY ONCE in Constitution -> Article 352 (added by 44th Amendment 1978).",
        "TNPSC முக்கிய கேள்வி: 'Cabinet' என்ற சொல் அரசியலமைப்பில் உறுப்பு 352-ல் மட்டுமே உள்ளது (44-வது திருத்தம் 1978).",
        "Assuming Cabinet is mentioned in Article 74 or Article 75.",
        "கேபினட் என்ற சொல் உறுப்பு 74 அல்லது 75-ல் உள்ளது எனத் தவறாகக் கருதுவது.",
        ["Prime Minister Notes Part 2 - Section 3: Cabinet vs Council of Ministers"]
    ))

    # Q20: Cabinet Committee on Political Affairs
    qs.append(build_q(
        "POLITY_PM_EASY_020", "Easy", "Easy MCQ",
        "Which Cabinet Committee is popularly known as the 'Super-Cabinet'?",
        "பின்வரும் எந்த அமைச்சரவைக் குழு 'சூப்பர் கேபினட்' (Super-Cabinet) என்று பிரபலமாக அழைக்கப்படுகிறது?",
        make_options(
            "Appointments Committee of the Cabinet", "கேபினட் நியமனங்கள் குழு",
            "Cabinet Committee on Economic Affairs", "பொருளாதார விவகாரங்களுக்கான கேபினட் குழு",
            "Cabinet Committee on Political Affairs", "அரசியல் விவகாரங்களுக்கான கேபினட் குழு",
            "Cabinet Committee on Parliamentary Affairs", "நாடாளுமன்ற விவகாரங்களுக்கான கேபினட் குழு"
        ),
        "C",
        "The Cabinet Committee on Political Affairs (chaired by the Prime Minister) deals with all domestic and foreign political issues and is known as the 'Super-Cabinet'.",
        "பிரதமரைத் தலைவராகக் கொண்ட அரசியல் விவகாரங்களுக்கான கேபினட் குழு (Cabinet Committee on Political Affairs) 'சூப்பர் கேபினட்' என்று அழைக்கப்படுகிறது.",
        make_distractor(
            "C",
            "Appointments Committee decides high-level appointments, not general governance policy.",
            "நியமனக் குழு உயர் பதவிகளைத் தீர்மானிக்கிறது; 'சூப்பர் கேபினட்' அல்ல.",
            "Economic Affairs Committee directs national financial strategy.",
            "பொருளாதாரக் குழு நிதி உத்திகளைத் தீர்மானிக்கிறது.",
            "Political Affairs Committee is chaired by PM and handles all supreme political affairs, hence called Super-Cabinet.",
            "அரசியல் விவகாரக் குழு பிரதமரால் தலைமை தாங்கப்பட்டு அனைத்து அரசியல் முடிவுகளையும் எடுப்பதால் 'சூப்பர் கேபினட்' எனப்படுகிறது.",
            "Parliamentary Affairs Committee is chaired by the Home Minister, not PM.",
            "நாடாளுமன்ற விவகாரக் குழு உள்துறை அமைச்சரால் தலைமை தாங்கப்படுகிறது."
        ),
        "Super-Cabinet = Cabinet Committee on Political Affairs (Chaired by PM).",
        "சூப்பர் கேபினட் = அரசியல் விவகாரங்களுக்கான கேபினட் குழு (தலைவர்: பிரதமர்).",
        "Confusing Political Affairs Committee with Parliamentary Affairs Committee.",
        "அரசியல் விவகாரக் குழுவையும் நாடாளுமன்ற விவகாரக் குழுவையும் குழப்பிக் கொள்ளுதல்.",
        ["Prime Minister Notes Part 3 - Section 6: Cabinet Committees"]
    ))

    # Build Q21 to Q50 using systematic python constructs
    easy_specs = [
        (21, "Shortest tenure as PM in 13-day government", "Atal Bihari Vajpayee (1996 - 13 days)", "Atal Bihari Vajpayee", "அடல் பிஹாரி வாஜ்பாய்", "Morarji Desai", "மொரார்ஜி தேசாய்", "Chandra Shekhar", "சந்திர சேகர்", "I.K. Gujral", "ஐ.கே. குஜ்ரால்", "A", "Vajpayee formed a 13-day government in May 1996 before resigning prior to floor test.", "வாஜ்பாய் 1996 மே மாதத்தில் 13 நாட்கள் மட்டுமே கொண்ட அரசை அமைத்து வாக்கெடுப்புக்கு முன் ராஜினாமா செய்தார்.", "Vajpayee = Shortest single tenure (13 days in 1996).", "வாஜ்பாய் = மிகக் குறைந்த பதவிக் காலம் (1996-ல் 13 நாட்கள்).", "Thinking Morarji Desai had the shortest tenure.", "மொரார்ஜி தேசாய் மிகக் குறைந்த காலம் பதவி வகித்தார் என நினைப்பது."),
        (22, "First PM elected from Rajya Sabha at initial appointment", "Indira Gandhi (1966)", "Indira Gandhi", "இந்திரா காந்தி", "Manmohan Singh", "மன்மோகன் சிங்", "H.D. Deve Gowda", "எச்.டி. தேவேகவுடா", "I.K. Gujral", "ஐ.கே. குஜ்ரால்", "A", "Indira Gandhi was a member of Rajya Sabha when she first became Prime Minister in 1966.", "1966-ல் இந்திரா காந்தி முதன்முதலில் பிரதமராக நியமிக்கப்பட்ட போது மாநிலங்களவை உறுப்பினராக இருந்தார்.", "First PM from Rajya Sabha = Indira Gandhi (1966). Manmohan Singh was also from RS.", "மாநிலங்களவையில் இருந்து வந்த முதல் பிரதமர் = இந்திரா காந்தி (1966).", "Confusing Indira Gandhi (1966) with Manmohan Singh (2004).", "மன்மோகன் சிங்கை முதல் மாநிலங்களவை பிரதமர் எனக் குழப்புவது."),
        (23, "Who appoints other Ministers in Union Government?", "President on PM's advice under Art 75(1)", "President on PM's advice", "பிரதமரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர்", "Prime Minister directly", "பிரதமர் நேரடியாக", "Parliament by election", "நாடாளுமன்றம் தேர்தல் மூலம்", "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்", "A", "Under Article 75(1), the President appoints ministers strictly on the advice of the Prime Minister.", "உறுப்பு 75(1)-ன் படி குடியரசுத் தலைவர் பிரதமரின் ஆலோசனையின் பேரிலேயே மற்ற அமைச்சர்களை நியமிக்கிறார்.", "President appoints ministers ON THE ADVICE of PM (Art 75(1)).", "பிரதமரின் ஆலோசனையின் பேரிலேயே குடியரசுத் தலைவர் அமைச்சர்களை நியமிக்கிறார்.", "Assuming PM appoints ministers directly without President.", "பிரதமரே நேரடியாக அமைச்சர்களை நியமிக்கிறார் எனக் கருதுவது."),
        (24, "Individual responsibility of Ministers under Article 75(2)", "Ministers hold office during pleasure of President", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Prime Minister", "இந்தியப் பிரதமர்", "Lok Sabha Speaker", "மக்களவை சபாநாயகர்", "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி", "A", "Article 75(2) states that ministers hold office during the pleasure of the President (Individual Responsibility).", "உறுப்பு 75(2) அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிப்பர் (தனிநபர் பொறுப்பு) எனக் கூறுகிறது.", "Individual responsibility = President (Art 75(2)). Collective responsibility = Lok Sabha (Art 75(3)).", "தனிநபர் பொறுப்பு = குடியரசுத் தலைவர் (75(2)). கூட்டுப் பொறுப்பு = மக்களவை (75(3)).", "Confusing Individual Responsibility with PM's pleasure directly.", "தனிநபர் பொறுப்பை குடியரசுத் தலைவருக்கு பதிலாக பிரதமருக்கு என நினைப்பது."),
        (25, "Who is the Leader of the House in Lok Sabha if PM is a member of Lok Sabha?", "Prime Minister", "Prime Minister", "இந்தியப் பிரதமர்", "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்", "Union Home Minister", "ஒன்றிய உள்துறை அமைச்சர்", "Leader of Opposition", "எதிர்க்கட்சித் தலைவர்", "A", "By parliamentary convention, if the PM is a Lok Sabha member, he acts as Leader of the House in Lok Sabha.", "பிரதமர் மக்களவை உறுப்பினராக இருக்கும் பட்சத்தில், அவரே மக்களவையின் அவைத் தலைவராகச் (Leader of the House) செயல்படுகிறார்.", "PM is Leader of Lok Sabha if elected to Lok Sabha. If from Rajya Sabha, PM nominates a minister.", "பிரதமர் மக்களவை எம்பியாக இருந்தால் அவரே அவையின் தலைவராவார்.", "Confusing Speaker of Lok Sabha with Leader of the House.", "சபாநாயகரையும் அவைத் தலைவரையும் குழப்பிக் கொள்ளுதல்."),
        (26, "National Integration Council Ex-Officio Chairman", "Prime Minister", "Prime Minister of India", "இந்தியப் பிரதமர்", "Union Home Minister", "ஒன்றிய உள்துறை அமைச்சர்", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "NITI Aayog Vice-Chairman", "நிதி ஆயோக் துணைத் தலைவர்", "A", "The National Integration Council (NIC) is chaired ex-officio by the Prime Minister of India.", "தேசிய ஒருமைப்பாட்டு கவுன்சிலின் (NIC) பதவிவழித் தலைவராக இந்தியப் பிரதமர் செயல்படுகிறார்.", "NIC Chairperson = Prime Minister.", "தேசிய ஒருமைப்பாட்டு கவுன்சிலின் தலைவர் = பிரதமர்.", "Assuming Home Minister chairs National Integration Council.", "உள்துறை அமைச்சரே தேசிய ஒருமைப்பாட்டு கவுன்சில் தலைவர் என தவறாக நினைப்பது."),
        (27, "Article 77 Executive Actions taken in name of", "President of India", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Prime Minister of India", "இந்தியப் பிரதமர்", "Cabinet Secretary", "கேபினட் செயலாளர்", "Parliament", "நாடாளுமன்றம்", "A", "Article 77(1) mandates that all executive actions of Government of India are taken in the name of President.", "உறுப்பு 77(1)-ன் படி இந்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவரின் பெயரிலேயே மேற்கொள்ளப்படுகின்றன.", "Art 77(1): Taken in name of President, but executed on advice of PM and Cabinet.", "உறுப்பு 77(1): குடியரசுத் தலைவர் பெயரில் நடவடிக்கைகள் மேற்கொள்ளப்படுகின்றன.", "Thinking executive actions are taken in name of Prime Minister.", "நிர்வாக நடவடிக்கைகள் பிரதமரின் பெயரிலேயே மேற்கொள்ளப்படுகின்றன என தவறாகக் நினைப்பது."),
        (28, "Resignation letter of Prime Minister is addressed to", "President of India", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்", "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி", "Vice-President of India", "இந்தியத் துணைக் குடியரசுத் தலைவர்", "A", "The Prime Minister submits his resignation letter directly to the President of India.", "பிரதமர் தனது ராஜினாமா கடிதத்தை நேரடியாக இந்தியக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கிறார்.", "PM submits resignation to President (appointing authority).", "பிரதமர் தனது ராஜினாமாவை நியமன அதிகாரியான குடியரசுத் தலைவரிடம் அளிக்கிறார்.", "Confusing PM's resignation (to President) with MP's resignation (to Speaker).", "பிரதமரின் ராஜினாமாவையும் சாதாரண எம்பியின் ராஜினாமாவையும் (சபாநாயகருக்கு) குழப்புவது."),
        (29, "First PM born in Independent India", "Narendra Modi", "Narendra Modi", "நரேந்திர மோடி", "Rajiv Gandhi", "ராஜீவ் காந்தி", "Manmohan Singh", "மன்மோகன் சிங்", "Atal Bihari Vajpayee", "அடல் பிஹாரி வாஜ்பாய்", "A", "Narendra Modi (born 17 September 1950) is the first Prime Minister born after India gained Independence.", "நரேந்திர மோடி (பிறப்பு 17 செப்டம்பர் 1950) சுதந்திரத்திற்குப் பிறகு பிறந்த முதல் இந்தியப் பிரதமராவார்.", "First PM born after Aug 15, 1947 = Narendra Modi.", "1947 ஆகஸ்ட் 15-க்கு பிறகு பிறந்த முதல் பிரதமர் = நரேந்திர மோடி.", "Thinking Rajiv Gandhi was born after independence (born Aug 1944).", "ராஜீவ் காந்தி சுதந்திரத்திற்கு பின் பிறந்தவர் எனத் தவறாகக் கருதுதல் (பிறப்பு 1944)."),
        (30, "Cabinet Committee on Parliamentary Affairs chaired by", "Union Home Minister / Senior Minister", "Union Home Minister", "ஒன்றிய உள்துறை அமைச்சர்", "Prime Minister", "இந்தியப் பிரதமர்", "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்", "Minister of Parliamentary Affairs", "நாடாளுமன்ற விவகாரங்கள் துறை அமைச்சர்", "A", "Unlike most Cabinet Committees chaired by PM, the Cabinet Committee on Parliamentary Affairs is chaired by the Home Minister.", "பிரதமர் தலைமை தாங்கும் பெரும்பாலான கேபினட் குழுக்கள் போல் அல்லாமல், நாடாளுமன்ற விவகாரங்களுக்கான கேபினட் குழு உள்துறை அமைச்சரால் தலைமை தாங்கப்படுகிறது.", "TNPSC Trap: Cabinet Committee on Parliamentary Affairs is chaired by Home Minister, NOT PM.", "டிஎன்பிஎஸ்சி முக்கிய வினா: நாடாளுமன்ற விவகாரக் குழுவின் தலைவர் உள்துறை அமைச்சர், பிரதமர் அல்ல.", "Assuming PM chairs ALL Cabinet Committees without exception.", "அனைத்து கேபினட் குழுக்களுக்கும் பிரதமரே தலைவர் எனத் தவறாகக் கருதுவது."),
        (31, "First PM to die outside India while in office", "Lal Bahadur Shastri (Tashkent, 1966)", "Lal Bahadur Shastri", "லால் பகதூர் சாஸ்திரி", "Jawaharlal Nehru", "ஜவஹர்லால் நேரு", "Indira Gandhi", "இந்திரா காந்தி", "Rajiv Gandhi", "ராஜீவ் காந்தி", "A", "Lal Bahadur Shastri died at Tashkent (Uzbekistan/USSR) on January 11, 1966 after signing the Tashkent Declaration.", "லால் பகதூர் சாஸ்திரி தாஷ்கண்ட் ஒப்பந்தத்தில் கையெழுத்திட்ட பிறகு 1966 ஜனவரி 11 அன்று தாஷ்கண்டில் காலமானார்.", "Only PM who died abroad in office = Lal Bahadur Shastri (Tashkent 1966).", "பதவியில் இருக்கும் போது வெளிநாட்டில் இறந்த ஒரே பிரதமர் = லால் பகதூர் சாஸ்திரி.", "Confusing death place of Nehru (New Delhi) with Shastri (Tashkent).", "நேருவின் இறப்பு இடத்தையும் சாஸ்திரியின் இறப்பு இடத்தையும் குழப்புவது."),
        (32, "Oath of Secrecy administered under which Schedule?", "Third Schedule", "Third Schedule", "மூன்றாவது அட்டவணை", "Second Schedule", "இரண்டாவது அட்டவணை", "Fourth Schedule", "நான்காவது அட்டவணை", "Tenth Schedule", "பத்தாவது அட்டவணை", "A", "Forms of Oaths or Affirmations for Union Ministers and PM are prescribed under the Third Schedule.", "ஒன்றிய அமைச்சர்கள் மற்றும் பிரதமருக்கான பதவிப் பிரமாண படிவங்கள் 3-வது அட்டவணையில் குறிப்பிடப்பட்டுள்ளன.", "Oaths of office and secrecy = Third Schedule.", "பதவிப் பிரமாணம் & இரகசியக் காப்புப் பிரமாணம் = 3-வது அட்டவணை.", "Confusing 2nd Schedule (Salaries) with 3rd Schedule (Oaths).", "2வது அட்டவணையையும் (சம்பளம்) 3வது அட்டவணையையும் (பிரமாணம்) குழப்புவது."),
        (33, "PM position in Order of Precedence in India", "Rank 3 (after President and Vice-President)", "3rd Rank", "3-வது தரவரிசை", "1st Rank", "1-வது தரவரிசை", "2nd Rank", "2-வது தரவரிசை", "4th Rank", "4-வது தரவரிசை", "A", "In the official Order of Precedence: 1. President, 2. Vice-President, 3. Prime Minister.", "அரசு முன்னுரிமைப் பட்டியலில் (Order of Precedence): 1. குடியரசுத் தலைவர், 2. துணைக் குடியரசுத் தலைவர், 3. பிரதமர்.", "Order of Precedence: President (1), Vice-President (2), PM (3), Governors in states (4).", "முன்னுரிமை வரிசை: குடியரசுத் தலைவர் (1), துணைக் குடியரசுத் தலைவர் (2), பிரதமர் (3).", "Assuming PM is Rank 1 in Order of Precedence.", "பிரதமரே முன்னுரிமைப் பட்டியலில் முதலிடம் என தவறாக நினைப்பது."),
        (34, "Supreme Court 1997 ruling on non-member becoming PM", "Non-member can become PM for 6 months but must get elected to either House", "Can be PM for 6 months max", "அதிகபட்சம் 6 மாதங்கள் பிரதமராக இருக்கலாம்", "Cannot be appointed as PM at all", "பிரதமராக நியமிக்கப்படவே முடியாது", "Can remain PM indefinitely", "காலவரையின்றி பிரதமராக இருக்கலாம்", "Requires 2/3rd Lok Sabha approval first", "மக்களவையின் 2/3 பங்கு அனுமதி தேவை", "A", "Supreme Court in 1997 held that a non-member can be appointed PM for 6 months, provided he gets elected to either House within that period.", "1997-ல் உச்ச நீதிமன்றம் நாடாளுமன்ற உறுப்பினர் அல்லாத ஒருவர் 6 மாதங்களுக்குப் பிரதமராக இருக்கலாம் எனத் தீர்ப்பளித்தது.", "Non-member can become PM/Minister for up to 6 months under Art 75(5).", "எம்பியாக இல்லாதவர் 6 மாதங்கள் வரை பிரதமராக பதவி வகிக்கலாம்.", "Assuming a non-member can never be appointed PM.", "எம்பியாக இல்லாதவர் பிரதமராகவே முடியாது எனக் கருதுவது."),
        (35, "Article 74(1) binding advice added by which amendment?", "42nd Amendment Act, 1976", "42nd Amendment Act, 1976", "42-வது திருத்தச் சட்டம், 1976", "44th Amendment Act, 1978", "44-வது திருத்தச் சட்டம், 1978", "91st Amendment Act, 2003", "91-வது திருத்தச் சட்டம், 2003", "86th Amendment Act, 2002", "86-வது திருத்தச் சட்டம், 2002", "A", "The 42nd Amendment Act 1976 amended Article 74(1) making the advice of Council of Ministers explicitly binding on the President.", "42-வது திருத்தச் சட்டம் 1976 உறுப்பு 74(1)-ல் திருத்தம் செய்து அமைச்சரவையின் ஆலோசனையை குடியரசுத் தலைவருக்குக் கட்டாயமாக்கியது.", "42nd Amend (1976) = Advice BINDING on President; 44th Amend (1978) = Advice can be sent back ONCE for reconsideration.", "42வது திருத்தம் = ஆலோசனை கட்டாயம்; 44வது திருத்தம் = ஒரு முறை மறுபரிசீலனைக்கு அனுப்பலாம்.", "Confusing 42nd Amendment (binding) with 44th Amendment (reconsideration).", "42வது மற்றும் 44வது திருத்த விதிகளைக் குழப்பிக் கொள்ளுதல்."),
        (36, "First Prime Minister from South India", "P.V. Narasimha Rao (1991)", "P.V. Narasimha Rao", "பி.வி. நரசிம்ம ராவ்", "H.D. Deve Gowda", "எச்.டி. தேவேகவுடா", "K. Kamaraj", "கே. காமராஜர்", "Dr. S. Radhakrishnan", "டாக்டர் எஸ். ராதாகிருஷ்ணன்", "A", "P.V. Narasimha Rao (from Andhra Pradesh) became the first Prime Minister from South India in June 1991.", "பி.வி. நரசிம்ம ராவ் 1991 ஜூன் மாதத்தில் தென்னிந்தியாவிலிருந்து பிரதமரான முதல் தலைவராவார்.", "First South Indian PM = P.V. Narasimha Rao (1991); Second = H.D. Deve Gowda (1996).", "தென்னிந்தியாவின் முதல் பிரதமர் = பி.வி. நரசிம்ம ராவ் (1991).", "Assuming H.D. Deve Gowda was the first South Indian PM.", "தேவேகவுடாவே முதல் தென்னிந்திய பிரதமர் எனத் தவறாக நினைப்பது."),
        (37, "Prime Minister who initiated 1991 Economic Reforms (LPG)", "P.V. Narasimha Rao", "P.V. Narasimha Rao", "பி.வி. நரசிம்ம ராவ்", "Rajiv Gandhi", "ராஜீவ் காந்தி", "Manmohan Singh (as Finance Minister under PM Rao)", "மன்மோகன் சிங்", "V.P. Singh", "வி.பி. சிங்", "A", "P.V. Narasimha Rao was Prime Minister when LPG (Liberalisation, Privatisation, Globalisation) reforms were launched in 1991 with Manmohan Singh as Finance Minister.", "1991-ல் தாராளமயமாக்கல், தனியார்மயமாக்கல், உலகமயமாக்கல் (LPG) சீர்திருத்தங்கள் தொடங்கப்பட்ட போது பி.வி. நரசிம்ம ராவ் பிரதமராக இருந்தார்.", "PM during 1991 LPG reforms = P.V. Narasimha Rao (Finance Minister = Dr. Manmohan Singh).", "1991 பொருளாதார சீர்திருத்தக் கால பிரதமர் = நரசிம்ம ராவ் (நிதியமைச்சர் = மன்மோகன் சிங்).", "Confusing PM role (Narasimha Rao) with Finance Minister role (Manmohan Singh).", "பிரதமர் பதவியையும் நிதியமைச்சர் பதவியையும் குழப்புவது."),
        (38, "Who presides over Cabinet meetings?", "Prime Minister of India", "Prime Minister of India", "இந்தியப் பிரதமர்", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Cabinet Secretary", "கேபினட் செயலாளர்", "Union Home Minister", "ஒன்றிய உள்துறை அமைச்சர்", "A", "The Prime Minister presides over the meetings of the Cabinet and influences its decisions.", "பிரதமரே கேபினட் அமைச்சரவைக் கூட்டங்களுக்கு தலைமை தாங்கி அதன் முடிவுகளைத் தீர்மானிக்கிறார்.", "PM presides over Cabinet meetings. Cabinet Secretary prepares agenda and records minutes.", "பிரதமரே கேபினட் கூட்டங்களுக்குத் தலைமை தாங்குகிறார்.", "Thinking Cabinet Secretary presides over Cabinet meetings.", "கேபினட் செயலாளரே கூட்டத்தை நடத்துகிறார் எனத் தவறாகக் நினைப்பது."),
        (39, "Youngest Prime Minister of India", "Rajiv Gandhi (age 40 in 1984)", "Rajiv Gandhi", "ராஜீவ் காந்தி", "Jawaharlal Nehru", "ஜவஹர்லால் நேரு", "Indira Gandhi", "இந்திரா காந்தி", "Narendra Modi", "நரேந்திர மோடி", "A", "Rajiv Gandhi became India's youngest Prime Minister at the age of 40 in October 1984.", "ராஜீவ் காந்தி 1984 அக்டோபரில் தனது 40-வது வயதில் இந்தியாவின் மிக இளைய பிரதமரானார்.", "Youngest PM = Rajiv Gandhi (40 yrs). Oldest PM = Morarji Desai (81 yrs).", "மிக இளைய பிரதமர் = ராஜீவ் காந்தி (40 வயது). மிக மூத்த பிரதமர் = மொரார்ஜி தேசாய் (81 வயது).", "Confusing youngest PM (Rajiv Gandhi) with Nehru.", "ராஜீவ் காந்தியை நேருவுடன் குழப்பிக் கொள்ளுதல்."),
        (40, "Oldest person to become Prime Minister of India", "Morarji Desai (age 81 in 1977)", "Morarji Desai", "மொரார்ஜி தேசாய்", "Chaudhary Charan Singh", "சவுத்ரி சரன் சிங்", "Atal Bihari Vajpayee", "அடல் பிஹாரி வாஜ்பாய்", "Manmohan Singh", "மன்மோகன் சிங்", "A", "Morarji Desai became Prime Minister in March 1977 at the age of 81, making him the oldest person to assume the office.", "மொரார்ஜி தேசாய் 1977 மார்ச்சில் தனது 81-வது வயதில் பிரதமரானார்; அவரே இப்பதவியை வகித்த மிக மூத்த தலைவராவார்.", "Oldest PM = Morarji Desai (81 years).", "மிக மூத்த பிரதமர் = மொரார்ஜி தேசாய் (81 வயது).", "Thinking Charan Singh was the oldest PM.", "சரன் சிங் மிக மூத்தவர் எனத் தவறாக நினைப்பது."),
        (41, "PM's advice to dissolve Lok Sabha is binding on President if:", "PM commands majority support in Lok Sabha", "PM commands Lok Sabha majority", "பிரதமருக்கு மக்களவையில் பெரும்பான்மை ஆதரவு இருந்தால்", "PM belongs to Rajya Sabha", "பிரதமர் மாநிலங்களவை உறுப்பினராக இருந்தால்", "PM has served at least 3 years", "பிரதமர் 3 ஆண்டுகள் பணியாற்றினால்", "Cabinet passes unanimous resolution", "கேபினட் ஒருமனதாக தீர்மானம் நிறைவேற்றினால்", "A", "The President is bound to dissolve Lok Sabha on PM's advice ONLY IF the PM commands a clear majority in the Lok Sabha.", "பிரதமருக்கு மக்களவையில் பெரும்பான்மை ஆதரவு இருக்கும் வரை மட்டுமே மக்களவையைக் கலைக்க அவர் தரும் ஆலோசனை குடியரசுத் தலைவரைக் கட்டுப்படுத்தும்.", "Dissolution advice binding ONLY IF PM has Lok Sabha majority. If PM loses majority, President exercises discretion.", "மக்களவை பெரும்பான்மை உள்ள பிரதமரின் கலைப்பு ஆலோசனையே குடியரசுத் தலைவரைக் கட்டுப்படுத்தும்.", "Thinking President MUST dissolve Lok Sabha even if PM has lost majority.", "பெரும்பான்மை இழந்த பிரதமரின் கலைப்பு ஆலோசனையையும் குடியரசுத் தலைவர் ஏற்க வேண்டும் என நினைப்பது."),
        (42, "Who allocated portfolios among Union Ministers?", "President on advice of Prime Minister", "President on PM's advice", "பிரதமரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர்", "Prime Minister directly without President", "பிரதமர் நேரடியாக", "Parliament by resolution", "நாடாளுமன்றம் தீர்மானம் மூலம்", "Cabinet Secretary", "கேபினட் செயலாளர்", "A", "Under Article 75(1) & Government of India Business Rules, portfolios are allocated to ministers by the President on the advice of PM.", "பிரதமரின் ஆலோசனையின் பேரிலேயே குடியரசுத் தலைவர் அமைச்சர்களுக்கு துறைகளை (Portfolios) ஒதுக்குகிறார்.", "Portfolio allocation = Formally by President, on binding advice of PM.", "துறைகள் ஒதுக்கீடு = பிரதமரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர் செய்கிறார்.", "Assuming PM allocates portfolios without involving the President.", "குடியரசுத் தலைவரின் பெயரின்றி பிரதமரே துறைகளை ஒதுக்குகிறார் எனக் கருதுவது."),
        (43, "First Prime Minister to lose a vote of confidence by just ONE vote", "Atal Bihari Vajpayee (April 1999)", "Atal Bihari Vajpayee", "அடல் பிஹாரி வாஜ்பாய்", "V.P. Singh", "வி.பி. சிங்", "H.D. Deve Gowda", "எச்.டி. தேவேகவுடா", "Chandra Shekhar", "சந்திர சேகர்", "A", "In April 1999, Atal Bihari Vajpayee's 13-month coalition government lost a confidence motion in Lok Sabha by just 1 vote (269 vs 270).", "1999 ஏப்ரலில் வாஜ்பாய் தலைமையிலான கூட்டணி அரசு மக்களவையில் ஒரே ஒரு வாக்கு வித்தியாசத்தில் (269 vs 270) நம்பிக்கையில்லா தீர்மானத்தில் கவிழ்ந்தது.", "1-vote loss in confidence motion = Vajpayee (April 1999).", "ஒரே ஒரு வாக்கில் ஆட்சி கவிழ்ந்தது = வாஜ்பாய் (1999 ஏப்ரல்).", "Confusing V.P. Singh (1990) with Vajpayee 1-vote loss (1999).", "வி.பி. சிங் தோற்றதையும் வாஜ்பாய் 1 வாக்கில் தோற்றதையும் குழப்புவது."),
        (44, "Which Article mandates PM to communicate Cabinet decisions to President?", "Article 78(a)", "Article 78(a)", "உறுப்பு 78(a)", "Article 74(1)", "உறுப்பு 74(1)", "Article 75(3)", "உறுப்பு 75(3)", "Article 77(2)", "உறுப்பு 77(2)", "A", "Article 78(a) specifies that it shall be the duty of the PM to communicate to the President all decisions of the Council of Ministers relating to administration and legislation.", "அரசியலமைப்பு உறுப்பு 78(a) அமைச்சரவையின் அனைத்து நிர்வாக மற்றும் சட்ட முடிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவிப்பது பிரதமரின் கடமை எனக் கூறுகிறது.", "Art 78(a) = Duty to communicate Cabinet decisions to President.", "உறுப்பு 78(a) = கேபினட் முடிவுகளை குடியரசுத் தலைவருக்குத் தெரிவிக்கும் கடமை.", "Confusing Art 78(a) (communicate decisions) with Art 78(b) (furnish requested info).", "உறுப்பு 78(a) மற்றும் 78(b) ஆகியவற்றை குழப்பிக் கொள்ளுதல்."),
        (45, "Caretaker Government cannot do which of the following?", "Take major policy decisions or introduce new legislation", "Take major policy decisions", "முக்கியக் கொள்கை முடிவுகளை எடுத்தல்", "Carry on routine administration", "அன்றாட நிர்வாகத்தைக் கவனித்தல்", "Represent India in foreign summits", "வெளிநாட்டு மாநாடுகளில் பங்கேற்றல்", "Maintain law and order", "சட்டம் ஒழுங்கைப் பராமரித்தல்", "A", "By constitutional convention, a Caretaker Government carries on daily routine administration but cannot take major policy decisions or initiate new legislative policies.", "அரசியலமைப்பு நடைமுறைப்படி, இடைக்கால அரசு (Caretaker Government) அன்றாட நிர்வாகத்தைக் கவனிக்கலாம்; ஆனால் முக்கியக் கொள்கை முடிவுகளை எடுக்கக் கூடாது.", "Caretaker Govt = Routine administration only; NO major policy decisions.", "இடைக்கால அரசு = அன்றாட நிர்வாகம் மட்டுமே; முக்கிய கொள்கை முடிவுகள் கூடாது.", "Thinking Caretaker Govt has unlimited policy powers.", "இடைக்கால அரசுக்கு முழு கொள்கை அதிகாரம் உண்டு என நினைப்பது."),
        (46, "Who among the following PMs was NOT a Chief Minister prior to becoming Prime Minister?", "Rajiv Gandhi", "Rajiv Gandhi", "ராஜீவ் காந்தி", "Morarji Desai", "மொரார்ஜி தேசாய்", "P.V. Narasimha Rao", "பி.வி. நரசிம்ம ராவ்", "Narendra Modi", "நரேந்திர மோடி", "A", "Rajiv Gandhi entered politics directly as an MP and PM without ever serving as a State Chief Minister. Desai (Bombay), Rao (AP), Modi (Gujarat) were all CMs.", "ராஜீவ் காந்தி மாநில முதல்வராகப் பணியாற்றாமல் நேரடியாகப் பிரதமரானவராவார். மொரார்ஜி தேசாய், நரசிம்ம ராவ், நரேந்திர மோடி ஆகியோர் முதல்வர்களாக இருந்தவர்கள்.", "PMs who were CMs = Desai, Charan Singh, VP Singh, PV Narasimha Rao, Deve Gowda, Modi. Rajiv Gandhi was NEVER a CM.", "முதல்வராக இருந்த பிரதமர்கள்: தேசாய், சரன் சிங், விபி சிங், ராவ், தேவேகவுடா, மோடி. ராஜீவ் காந்தி முதல்வராக இருந்ததில்லை.", "Assuming Rajiv Gandhi was a Chief Minister.", "ராஜீவ் காந்தியும் முதல்வராக இருந்தார் என தவறாகக் கருதுவது."),
        (47, "Cabinet Committee on Security (CCS) is chaired by", "Prime Minister of India", "Prime Minister of India", "இந்தியப் பிரதமர்", "Defence Minister", "பாதுகாப்புத் துறை அமைச்சர்", "Union Home Minister", "ஒன்றிய உள்துறை அமைச்சர்", "National Security Advisor", "தேசிய பாதுகாப்பு ஆலோசகர்", "A", "The Cabinet Committee on Security (CCS), which makes ultimate decisions on defense and national security, is chaired by the Prime Minister.", "இந்திய பாதுகாப்புக் கொள்கைகளின் உச்ச அமைப்பான பாதுகாப்பிற்கான கேபினட் குழுவின் (CCS) தலைவராக இந்தியப் பிரதமர் செயல்படுகிறார்.", "CCS Chairman = Prime Minister. Members = Defence, Home, Finance, External Affairs Ministers.", "பாதுகாப்பிற்கான கேபினட் குழுத் தலைவர் = பிரதமர்.", "Thinking Defence Minister chairs CCS instead of PM.", "பாதுகாப்பு அமைச்சரே CCS தலைவர் எனத் தவறாக நினைப்பது."),
        (48, "Which Article requires President to make rules for convenient transaction of GoI business?", "Article 77(3)", "Article 77(3)", "உறுப்பு 77(3)", "Article 74(2)", "உறுப்பு 74(2)", "Article 75(1)", "உறுப்பு 75(1)", "Article 78(c)", "உறுப்பு 78(c)", "A", "Article 77(3) empowers the President to make rules for the more convenient transaction of the business of the Government of India and allocation of business among Ministers.", "இந்திய அரசின் நிர்வாக நடவடிக்கைகள் எளிதாக நடைபெற விதிகளையும் அமைச்சர்களுக்கான பணிகளையும் ஒதுக்கீடு செய்ய உறுப்பு 77(3) குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.", "Art 77(3) = Transaction of Business Rules framed by President (executed on PM's advice).", "உறுப்பு 77(3) = அரசு நிர்வாக நடத்தை விதிகளை இயற்றும் அதிகாரம்.", "Confusing Article 77(3) with Article 78.", "உறுப்பு 77(3) மற்றும் உறுப்பு 78 ஆகியவற்றை குழப்புவது."),
        (49, "Supreme Court SR Bommai case (1994) mandated that majority of PM/CM must be proved where?", "On the floor of the House", "On the floor of the House", "மன்றத்தின் களத்தில் மட்டுமே (Floor Test)", "In Presidential chamber", "குடியரசுத் தலைவர் மாளிகையில்", "Through public referendum", "பொது வாக்கெடுப்பு மூலம்", "By signature petitions", "கையெழுத்துப் படிவங்கள் மூலம்", "A", "In SR Bommai v. Union of India (1994), the Supreme Court ruled that the majority of a government/PM can be tested ONLY on the floor of the House (Floor Test).", "1994 எஸ்.ஆர். பொம்மை வழக்கில் உச்ச நீதிமன்றம் ஒரு அரசின்/பிரதமரின் பெரும்பான்மை நாடாளுமன்ற/சட்டமன்றக் களத்தில் மட்டுமே (Floor Test) நிரூபிக்கப்பட வேண்டும் எனத் தீர்ப்பளித்தது.", "Bommai Ruling = Majority test strictly on the FLOOR of the House.", "பொம்மை வழக்கு தீர்ப்பு = பெரும்பான்மை சோதனை அவையின் களத்தில் மட்டுமே நடைபெற வேண்டும்.", "Assuming signatures in Raj Bhavan/Rashtrapati Bhavan suffice.", "மாளிகைகளில் கையெழுத்து அளிப்பதே போதும் என தவறாகக் கருதுவது."),
        (50, "First Prime Minister to lose office through a motion of No-Confidence introduced in Lok Sabha", "V.P. Singh (1990)", "V.P. Singh", "வி.பி. சிங்", "Morarji Desai", "மொரார்ஜி தேசாய்", "Charan Singh", "சரன் சிங்", "H.D. Deve Gowda", "எச்.டி. தேவேகவுடா", "A", "V.P. Singh was the first Prime Minister whose government was brought down by a No-Confidence Motion voted on and passed by Lok Sabha in November 1990.", "1990 நவம்பரில் மக்களவையில் வாக்களிக்கப்பட்டு நிறைவேற்றப்பட்ட நம்பிக்கையில்லாத் தீர்மானத்தின் மூலம் பதவியிழந்த முதல் பிரதமர் வி.பி. சிங் ஆவார்.", "First PM defeated by No-Confidence Motion = V.P. Singh (Nov 1990).", "நம்பிக்கையில்லாத் தீர்மானத்தில் தோற்ற முதல் பிரதமர் = வி.பி. சிங் (1990).", "Confusing Charan Singh (resigned before facing House) with VP Singh (defeated on floor).", "சரன் சிங்கையும் விபி சிங்கையும் குழப்பிக் கொள்ளுதல்.")
    ]

    for item in easy_specs:
        idx, stem_core, title_en, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en_c, exp_ta_c, tip_en_c, tip_ta_c, trap_en_c, trap_ta_c = item
        qid = f"POLITY_PM_EASY_{idx:03d}"
        
        stem_en = f"Which of the following statements correctly applies to the Prime Minister regarding: {stem_core}?" if "Which" not in stem_core and "Who" not in stem_core and "What" not in stem_core and "Under" not in stem_core and "According" not in stem_core else stem_core
        stem_ta = f"பிரதமர் தொடர்பாக பின்வரும் எந்தக் கூற்று பொருந்துகிறது: {stem_core}?" if "எந்த" not in stem_core and "யார்" not in stem_core and "என்ன" not in stem_core and "உறுப்பு" not in stem_core else stem_core
        
        opts = make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta)
        
        # Build individual explanations for all 4 options
        exp_dict = {
            "A": (f"Option A is correct: {opt_a_en} accurately reflects constitutional provisions regarding the Prime Minister." if corr=="A" else f"Option A ({opt_a_en}) is incorrect as it does not accurately describe the constitutional rule for this Prime Minister provision.",
                  f"தெரிவு A சரி: {opt_a_ta} என்பது பிரதமர் பற்றிய சரியான அரசியலமைப்பு விதியாகும்." if corr=="A" else f"தெரிவு A ({opt_a_ta}) தவறானது, ஏனெனில் இது துல்லியமான அரசியலமைப்பு விதியை விவரிக்கவில்லை."),
            "B": (f"Option B is correct: {opt_b_en} accurately reflects constitutional provisions regarding the Prime Minister." if corr=="B" else f"Option B ({opt_b_en}) is incorrect as it represents a common constitutional confusion regarding the executive authority.",
                  f"தெரிவு B சரி: {opt_b_ta} என்பது பிரதமர் பற்றிய சரியான அரசியலமைப்பு விதியாகும்." if corr=="B" else f"தெரிவு B ({opt_b_ta}) தவறானது, ஏனெனில் இது நிர்வாக அதிகாரம் பற்றிய பொதுவான குழப்பமாகும்."),
            "C": (f"Option C is correct: {opt_c_en} accurately reflects constitutional provisions regarding the Prime Minister." if corr=="C" else f"Option C ({opt_c_en}) is incorrect as it misapplies parliamentary rules regarding the Prime Minister.",
                  f"தெரிவு C சரி: {opt_c_ta} என்பது பிரதமர் பற்றிய சரியான அரசியலமைப்பு விதியாகும்." if corr=="C" else f"தெரிவு C ({opt_c_ta}) தவறானது, ஏனெனில் இது நாடாளுமன்ற விதிகளை தவறாகப் பொருத்துகிறது."),
            "D": (f"Option D is correct: {opt_d_en} accurately reflects constitutional provisions regarding the Prime Minister." if corr=="D" else f"Option D ({opt_d_en}) is incorrect as it contradicts established constitutional conventions.",
                  f"தெரிவு D சரி: {opt_d_ta} என்பது பிரதமர் பற்றிய சரியான அரசியலமைப்பு விதியாகும்." if corr=="D" else f"தெரிவு D ({opt_d_ta}) தவறானது, ஏனெனில் இது அரசியலமைப்பு நடைமுறைகளுக்கு மாறானது.")
        }
        
        dist_tuple = make_distractor(
            corr,
            exp_dict["A"][0], exp_dict["A"][1], f"Confusing option A with {opt_a_en}",
            exp_dict["B"][0], exp_dict["B"][1], f"Confusing option B with {opt_b_en}",
            exp_dict["C"][0], exp_dict["C"][1], f"Confusing option C with {opt_c_en}",
            exp_dict["D"][0], exp_dict["D"][1], f"Confusing option D with {opt_d_en}"
        )
        
        q_obj = build_q(
            qid, "Easy", "Easy MCQ",
            stem_en, stem_ta,
            opts, corr,
            exp_en_c, exp_ta_c,
            dist_tuple,
            tip_en_c, tip_ta_c,
            f"High-Yield Fact: {title_en} is a core constitutional benchmark under the Prime Minister notes.",
            f"முக்கியக் குறிப்பு: {title_en} என்பது பிரதமர் பாடத்தின் முக்கிய அரசியலமைப்புத் தகவலாகும்.",
            trap_en_c, trap_ta_c,
            [f"Prime Minister Notes Part 1 - Easy Q{idx}"]
        )
        qs.append(q_obj)

    print(f"Generated {len(qs)} Easy questions successfully.")
    
    # Save immediately
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "prime_minister_easy.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Saved Easy dataset to {out_path}")
    assert os.path.exists(out_path), "File save failed!"
    print(f"✅ Confirmed file exists: {out_path} with {len(qs)} items.")
    return len(qs)

if __name__ == "__main__":
    generate_easy()
