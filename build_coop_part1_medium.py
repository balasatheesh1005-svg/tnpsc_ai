# -*- coding: utf-8 -*-
"""
Co-operative Societies - Part 1: Medium MCQs (50 Questions: CS_M_001 to CS_M_050)
TNPSC Nova AI Content Engine
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from cooperative_societies_mcq_helper import make_coop_q


def get_medium_raw_questions():
    return [
        # 1. Grounds for Board Supersession
        {
            "subtopic": "Supersession and Suspension of Board - Article 243ZL",
            "stem_en": "Under Article 243ZL(1), which of the following is NOT an enumerated constitutional ground for the supersession or suspension of a co-operative society's board?",
            "stem_ta": "சரத்து 243ZL(1)-ன் கீழ், பின்வருவனவற்றில் எது ஒரு கூட்டுறவு சங்க வாரியத்தை இடைநீக்கம் செய்வதற்கான அரசியலமைப்பில் குறிப்பிடப்பட்ட காரணங்களில் ஒன்று அல்ல?",
            "options": [
                ("The board adopting an ideological stance critical of the ruling political party", "ஆளும் அரசியல் கட்சியை விமர்சிக்கும் கருத்தியல் நிலைப்பாட்டை வாரியம் எடுப்பது"),
                ("Persistent default in the performance of duties", "கடமைகளைச் செய்வதில் தொடர்ந்து தவறிழைப்பது"),
                ("Negligence in the performance of duties", "கடமைகளைச் செய்வதில் அலட்சியம் காட்டுவது"),
                ("Stalemate in the constitution or functions of the board", "வாரியத்தின் உருவாக்கம் அல்லது செயல்பாடுகளில் முட்டுக்கட்டை ஏற்படுவது")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZL(1) enumerates 4 strict grounds for supersession: persistent default, negligence, acts prejudicial to interests of society, and stalemate. Political disagreement is strictly impermissible as a ground for executive supersession.",
            "exp_ta": "சரத்து 243ZL(1) இடைநீக்கத்திற்கு 4 காரணங்களை மட்டுமே குறிப்பிடுகிறது: தொடர் தவறிழைப்பு, அலட்சியம், சங்க நலனுக்கு எதிரான செயல்கள் மற்றும் செயல்பாட்டு முட்டுக்கட்டை. அரசியல் கருத்து வேறுபாடு ஒருபோதும் இடைநீக்கத்திற்கான காரணமாக இருக்க முடியாது.",
            "why_a_en": "Correct. Political opposition is not a constitutional ground for superseding an autonomous cooperative board.",
            "why_a_ta": "சரி. தன்னாட்சி பெற்ற கூட்டுறவு வாரியத்தை இடைநீக்கம் செய்ய அரசியல் எதிர்ப்பு அரசியலமைப்பு ரீதியான காரணம் அல்ல.",
            "why_b_en": "Incorrect. Persistent default is an enumerated ground under Article 243ZL(1)(a).",
            "why_b_ta": "தவறு. தொடர் தவறிழைப்பு சரத்து 243ZL(1)(a)-ன் கீழ் உள்ள காரணமாகும்.",
            "why_c_en": "Incorrect. Negligence in performance is explicitly enumerated under Article 243ZL(1)(a).",
            "why_c_ta": "தவறு. கடமைகளைச் செய்வதில் அலட்சியம் என்பது வெளிப்படையாகக் கூறப்பட்டுள்ளது.",
            "why_d_en": "Incorrect. Stalemate is explicitly enumerated under Article 243ZL(1)(c).",
            "why_d_ta": "தவறு. முட்டுக்கட்டை ஏற்படுவது சரத்து 243ZL(1)(c)-ன் கீழ் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளது.",
            "tip_en": "Article 243ZL strictly limits arbitrary political supersession of boards by ruling state parties.",
            "tip_ta": "சரத்து 243ZL ஆளும் கட்சிகளால் தன்னிச்சையாக கூட்டுறவு வாரியங்கள் கலைக்கப்படுவதைத் தடுக்கிறது.",
            "fact_en": "Before supersession, the board must be given a reasonable opportunity of showing cause.",
            "fact_ta": "இடைநீக்கத்திற்கு முன், வாரியத்திற்கு விளக்கம் அளிக்க நியாயமான வாய்ப்பு வழங்கப்பட வேண்டும்."
        },

        # 2. Casual Vacancy on Board
        {
            "subtopic": "Board Composition & Term - Article 243ZJ",
            "stem_en": "Under Article 243ZJ(2) proviso, when can a casual vacancy on the board of a co-operative society be filled by nomination/co-option by the board itself rather than through an election?",
            "stem_ta": "சரத்து 243ZJ(2) வரம்பின் கீழ், ஒரு கூட்டுறவு சங்க வாரியத்தில் ஏற்படும் தற்செயலான காலியிடம் தேர்தலுக்குப் பதிலாக வாரியத்தாலேயே எப்போது நிரப்பப்படலாம்?",
            "options": [
                ("Where the remainder of the term of office of the board is less than half of its original term", "வாரியத்தின் மீதமுள்ள பதவிக்காலம் அதன் அசல் பதவிக்காலத்தில் பாதியை விடக் குறைவாக இருக்கும் போது"),
                ("Where the vacancy is for a reserved Women seat", "காலியிடம் பெண்களுக்கான இடஒதுக்கீட்டு இடமாக இருக்கும் போது"),
                ("Whenever the Registrar permits in writing", "பதிவாளர் எழுத்துப்பூர்வமாக அனுமதிக்கும் போதெல்லாம்"),
                ("Where the remaining term is less than 3 months", "மீதமுள்ள பதவிக்காலம் 3 மாதங்களுக்கும் குறைவாக இருக்கும் போது")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZJ(2) second proviso provides that the State Legislature may provide that casual vacancies can be filled by nomination by the board if the remaining term is less than half of its original term (i.e. less than 2.5 years).",
            "exp_ta": "சரத்து 243ZJ(2) இரண்டாவது வரம்பின் படி, வாரியத்தின் மீதமுள்ள பதவிக்காலம் அதன் அசல் பதவிக்காலத்தில் பாதியை விடக் குறைவாக இருக்கும் பட்சத்தில் (அதாவது 2.5 ஆண்டுகளுக்குக் குறைவாக), காலியிடங்களை வாரியமே நியமனம் மூலம் நிரப்ப மாநிலச் சட்டமன்றம் வழிவகை செய்யலாம்.",
            "why_a_en": "Correct. The constitutional threshold is 'less than half of its original term'.",
            "why_a_ta": "சரி. அரசியலமைப்பு வரம்பு 'அசல் பதவிக்காலத்தில் பாதியை விடக் குறைவு' என்பதாகும்.",
            "why_b_en": "Incorrect. Category of seat does not bypass general election unless remaining term is less than half.",
            "why_b_ta": "தவறு. மீதமுள்ள காலம் பாதியை விடக் குறைவாக இருந்தால் மட்டுமே இது பொருந்தும்.",
            "why_c_en": "Incorrect. Registrar's discretion does not override constitutional timeframe.",
            "why_c_ta": "தவறு. பதிவாளரின் விருப்ப அதிகாரம் அரசியலமைப்பு வரம்பை மீற முடியாது.",
            "why_d_en": "Incorrect. The threshold is half of the term (2.5 years), not 3 months.",
            "why_d_ta": "தவறு. வரம்பு பாதியாகும் (2.5 ஆண்டுகள்), 3 மாதங்கள் அல்ல.",
            "tip_en": "If more than half the term (2.5+ years) remains, an election is mandatory to fill the casual vacancy.",
            "tip_ta": "பாதிக்கும் மேலான பதவிக்காலம் மீதமிருந்தால், தேர்தல் நடத்துவது கட்டாயமாகும்.",
            "fact_en": "This mirrors provisions in Representation of the People Act, 1951 for parliamentary bye-elections.",
            "fact_ta": "இது நாடாளுமன்ற இடைத்தேர்தல்களுக்கான மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் விதிகளை ஒத்துள்ளது."
        },

        # 3. Banking Cooperatives Supersession Limit
        {
            "subtopic": "Supersession and Suspension of Board - Article 243ZL",
            "stem_en": "What is the maximum period of board supersession permitted under Article 243ZL for co-operative societies carrying on the business of banking?",
            "stem_ta": "வங்கித் தொழில் செய்யும் கூட்டுறவு சங்கங்களுக்கு சரத்து 243ZL-ன் கீழ் அனுமதிக்கப்படும் வாரிய இடைநீக்கத்தின் அதிகபட்ச காலம் என்ன?",
            "options": [
                ("1 year", "1 ஆண்டு"),
                ("6 months", "6 மாதங்கள்"),
                ("2 years", "2 ஆண்டுகள்"),
                ("3 years", "3 ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZL(1) second proviso specifies that in the case of a co-operative society carrying on the business of banking, the maximum period of supersession shall be one year instead of six months.",
            "exp_ta": "சரத்து 243ZL(1) இரண்டாவது வரம்பு, வங்கித் தொழில் செய்யும் ஒரு கூட்டுறவு சங்கத்தைப் பொறுத்தவரை, இடைநீக்கத்தின் அதிகபட்ச காலம் ஆறு மாதங்களுக்குப் பதிலாக ஒரு ஆண்டாக இருக்கும் என்று குறிப்பிடுகிறது.",
            "why_a_en": "Correct. Exactly 1 year is the limit for banking cooperatives.",
            "why_a_ta": "சரி. வங்கி கூட்டுறவுகளுக்கு சரியாக 1 ஆண்டு வரம்பாகும்.",
            "why_b_en": "Incorrect. 6 months is the limit for non-banking societies.",
            "why_b_ta": "தவறு. 6 மாதங்கள் வங்கி அல்லாத சங்கங்களுக்கான வரம்பு.",
            "why_c_en": "Incorrect. 2 years exceeds constitutional allowance.",
            "why_c_ta": "தவறு. 2 ஆண்டுகள் அரசியலமைப்பு வரம்பை மீறியது.",
            "why_d_en": "Incorrect. 3 years is incorrect.",
            "why_d_ta": "தவறு. 3 ஆண்டுகள் தவறானது.",
            "tip_en": "Banking cooperatives need longer resolution time to protect depositors' money and restructure bad loans.",
            "tip_ta": "வைப்பீட்டாளர்களின் பணத்தைப் பாதுகாக்கவும் கடன்களை மறுசீரமைக்கவும் வங்கி கூட்டுறவுகளுக்கு கூடுதல் அவகாசம் தேவைப்படுகிறது.",
            "fact_en": "For banking cooperatives, supersession must also comply with RBI directives under Banking Regulation Act.",
            "fact_ta": "வங்கி கூட்டுறவுகளுக்கு, இடைநீக்கம் வங்கி ஒழுங்குமுறைச் சட்டத்தின் கீழ் RBI-ன் வழிகாட்டுதல்களுக்கும் இணங்க வேண்டும்."
        },

        # 4. Qualifications of Cooperative Auditors
        {
            "subtopic": "Audit of Accounts - Article 243ZM",
            "stem_en": "Under Article 243ZM(1), who among the following is constitutionally eligible to be empaneled by the State to audit cooperative society accounts?",
            "stem_ta": "சரத்து 243ZM(1)-ன் கீழ், கூட்டுறவு சங்கக் கணக்குகளைத் தணிக்கை செய்ய மாநில அரசால் பட்டியலில் சேர்க்கப்பட அரசியலமைப்பு ரீதியாக தகுதியுடையவர் யார்?",
            "options": [
                ("Chartered Accountants within the meaning of the Chartered Accountants Act, 1949, or cooperative auditors from an approved government panel", "பட்டயக் கணக்காளர்கள் சட்டம் 1949-ன் கீழ் உள்ள பட்டயக் கணக்காளர்கள் (CAs), அல்லது அங்கீகரிக்கப்பட்ட அரசுப் பட்டியலிலுள்ள கூட்டுறவுத் தணிக்கையாளர்கள்"),
                ("Any registered graduate in commerce", "வணிகவியலில் பட்டம் பெற்ற எந்தவொரு பட்டதாரியும்"),
                ("Any member of the executive board with 5 years experience", "5 ஆண்டுகள் அனுபவம் கொண்ட நிர்வாக வாரியத்தின் எந்தவொரு உறுப்பினரும்"),
                ("Only the District Collector's personal staff", "மாவட்ட ஆட்சியரின் தனிப்பட்ட பணியாளர்கள் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZM(1) provides that every co-operative society shall be audited by an auditor or auditing firm appointed from a panel approved by the State Government, possessing qualifications of Chartered Accountant (under CA Act 1949) or government cooperative audit certification.",
            "exp_ta": "சரத்து 243ZM(1) ஒவ்வொரு கூட்டுறவு சங்கமும், பட்டயக் கணக்காளர் தகுதி (CA சட்டம் 1949) அல்லது அரசு கூட்டுறவு தணிக்கைச் சான்றிதழ் பெற்று மாநில அரசால் அங்கீகரிக்கப்பட்ட பட்டியலில் உள்ள தணிக்கையாளர் அல்லது நிறுவனத்தால் தணிக்கை செய்யப்பட வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Correct. Chartered Accountants or certified cooperative auditors from approved state panel.",
            "why_a_ta": "சரி. பட்டயக் கணக்காளர்கள் அல்லது அங்கீகரிக்கப்பட்ட அரசுப் பட்டியலிலுள்ள சான்றளிக்கப்பட்ட தணிக்கையாளர்கள்.",
            "why_b_en": "Incorrect. A general commerce degree is not a statutory auditing qualification.",
            "why_b_ta": "தவறு. பொது வணிகவியல் பட்டம் சட்டப்பூர்வ தணிக்கைத் தகுதி அல்ல.",
            "why_c_en": "Incorrect. Board members auditing their own society would cause conflict of interest.",
            "why_c_ta": "தவறு. வாரிய உறுப்பினர்களே தணிக்கை செய்வது நலன் முரண்பாட்டை ஏற்படுத்தும்.",
            "why_d_en": "Incorrect. District Collector's personal staff cannot conduct statutory cooperative audit.",
            "why_d_ta": "தவறு. மாவட்ட ஆட்சியர் பணியாளர்கள் சட்டப்பூர்வ தணிக்கை செய்ய முடியாது.",
            "tip_en": "In Tamil Nadu, the Department of Cooperative Audit functions as an independent department to ensure audit integrity.",
            "tip_ta": "தமிழ்நாட்டில், தணிக்கை நாணயத்தை உறுதி செய்ய கூட்டுறவுத் தணிக்கைத் துறை தனித் துறையாகச் செயல்படுகிறது.",
            "fact_en": "The auditor is appointed by the General Body from the government-approved panel.",
            "fact_ta": "அரசு அங்கீகரித்த பட்டியலிலிருந்து பொதுக்குழுவாலேயே தணிக்கையாளர் நியமிக்கப்படுகிறார்."
        },

        # 5. Cooperative Education Fund
        {
            "subtopic": "Rights of Members - Article 243ZO",
            "stem_en": "Article 243ZO provides for member education and training. Under state cooperative laws (such as TN Act 1983), societies are required to contribute a percentage of their net profit to which statutory fund?",
            "stem_ta": "சரத்து 243ZO உறுப்பினர் கல்வி மற்றும் பயிற்சிக்கு வழிவகை செய்கிறது. மாநிலக் கூட்டுறவுச் சட்டங்களின் கீழ் (TN சட்டம் 1983 போன்றவை), சங்கங்கள் தங்கள் நிகர லாபத்தில் ஒரு குறிப்பிட்ட சதவீதத்தை எந்த சட்டப்பூர்வ நிதிக்கு வழங்க வேண்டும்?",
            "options": [
                ("Cooperative Education Fund", "கூட்டுறவுக் கல்வி நிதி"),
                ("Prime Minister's Relief Fund", "பிரதமரின் நிவாரண நிதி"),
                ("Chief Minister's Public Relief Fund", "முதலமைச்சரின் பொது நிவாரண நிதி"),
                ("Consolidated Fund of the State", "மாநிலத்தின் ஒருங்கிணைந்த நிதி")
            ],
            "correct_key": "A",
            "exp_en": "Under state cooperative legislation, every profitable cooperative society must allocate a specified percentage (e.g. 2% to 3% in Tamil Nadu) of its net profit to the Cooperative Education Fund, managed by the state Cooperative Union for member awareness, staff training, and leadership development.",
            "exp_ta": "மாநிலக் கூட்டுறவுச் சட்டங்களின் கீழ், லாபம் ஈட்டும் ஒவ்வொரு கூட்டுறவு சங்கமும் தனது நிகர லாபத்தில் ஒரு குறிப்பிட்ட சதவீதத்தை (எ.கா. தமிழ்நாட்டில் 2% முதல் 3% வரை) உறுப்பினர் விழிப்புணர்வு, பணியாளர் பயிற்சி மற்றும் தலைமைத்துவ மேம்பாட்டிற்காக கூட்டுறவுக் கல்வி நிதிக்கு ஒதுக்க வேண்டும்.",
            "why_a_en": "Correct. Cooperative Education Fund is the designated statutory fund.",
            "why_a_ta": "சரி. கூட்டுறவுக் கல்வி நிதி என்பது இதற்கான சட்டப்பூர்வ நிதியாகும்.",
            "why_b_en": "Incorrect. PM Relief Fund is for national disasters.",
            "why_b_ta": "தவறு. பிரதமரின் நிவாரண நிதி பேரிடர்களுக்கானது.",
            "why_c_en": "Incorrect. CM Relief Fund is for state emergency assistance.",
            "why_c_ta": "தவறு. முதலமைச்சர் நிவாரண நிதி மாநில அவசர உதவிகளுக்கானது.",
            "why_d_en": "Incorrect. It is not paid into general state revenues.",
            "why_d_ta": "தவறு. இது பொது மாநில வருவாயில் செலுத்தப்படுவதில்லை.",
            "tip_en": "Cooperative Principle #5 is 'Education, Training, and Information' - funded through this statutory allocation.",
            "tip_ta": "கூட்டுறவுக் கொள்கை 5 என்பது 'கல்வி, பயிற்சி மற்றும் தகவல்' - இது இச்சட்டப்பூர்வ நிதி மூலம் நிதியளிக்கப்படுகிறது.",
            "fact_en": "In Tamil Nadu, the Tamil Nadu Cooperative Union (TNCU) administers the Cooperative Education Fund.",
            "fact_ta": "தமிழ்நாட்டில், தமிழ்நாடு கூட்டுறவு ஒன்றியம் (TNCU) கூட்டுறவுக் கல்வி நிதியை நிர்வகிக்கிறது."
        },

        # 6. Surcharge Proceedings in Tamil Nadu (Section 87)
        {
            "subtopic": "Tamil Nadu Cooperative Governance",
            "stem_en": "Under Section 87 of the Tamil Nadu Co-operative Societies Act, 1983, what proceedings can be initiated against a past or present officer for misappropriation, breach of trust, or causing deficiency in society assets?",
            "stem_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 87-ன் கீழ், சங்கத்தின் சொத்துக்களில் நிதி மோசடி, நம்பிக்கை துரோகம் அல்லது இழப்பு ஏற்படுத்திய முன்னாள் அல்லது இந்நாள் அதிகாரிக்கு எதிராக என்ன நடவடிக்கை தொடங்கப்படலாம்?",
            "options": [
                ("Surcharge proceedings to recover the loss with interest", "வட்டியுடன் இழப்பை மீட்டெடுப்பதற்கான கூடுதல் தீர்வு (சர்சார்ஜ்) நடவடிக்கைகள்"),
                ("Immediate cancellation of Indian citizenship", "இந்தியக் குடியுரிமையை உடனடியாக ரத்து செய்தல்"),
                ("Direct court martial proceedings", "நேரடி ராணுவ நீதிமன்ற விசாரணை"),
                ("Immediate dissolution of the entire district bank", "முழு மாவட்ட வங்கியையும் உடனடியாகக் கலைத்தல்")
            ],
            "correct_key": "A",
            "exp_en": "Section 87 of the TN Co-operative Societies Act, 1983 provides for Surcharge proceedings: if an inquiry (Sec 81), inspection (Sec 82), or audit shows that any person has misappropriated, fraudulently retained, or caused deficiency in assets, the Registrar may order him to repay or restore the money with interest.",
            "exp_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 87 சர்சார்ஜ் (Surcharge) நடவடிக்கைகளை வழங்குகிறது: விசாரணை (பிரிவு 81), ஆய்வு (பிரிவு 82) அல்லது தணிக்கையில் நிதி மோசடி அல்லது சொத்து இழப்பு கண்டறியப்பட்டால், சம்பந்தப்பட்ட நபர் பணத்தை வட்டியுடன் திருப்பிச் செலுத்த பதிவாளர் உத்தரவிடலாம்.",
            "why_a_en": "Correct. Section 87 surcharge proceedings recover misappropriated cooperative funds.",
            "why_a_ta": "சரி. பிரிவு 87 சர்சார்ஜ் நடவடிக்கை மோசடி செய்யப்பட்ட கூட்டுறவு நிதியை மீட்கிறது.",
            "why_b_en": "Incorrect. Citizenship is under Central Government (Citizenship Act 1955), not state cooperative law.",
            "why_b_ta": "தவறு. குடியுரிமை மத்திய அரசின் அதிகார வரம்பிற்கு உட்பட்டது.",
            "why_c_en": "Incorrect. Court martial applies to armed forces under military law.",
            "why_c_ta": "தவறு. ராணுவ நீதிமன்ற விசாரணை முப்படைகளுக்கு மட்டுமே பொருந்தும்.",
            "why_d_en": "Incorrect. Individual malfeasance does not dissolve the entire district bank.",
            "why_d_ta": "தவறு. தனிநபர் தவறுக்காக மாவட்ட வங்கி கலைக்கப்படுவதில்லை.",
            "tip_en": "TN Cooperative Act Audit trail: Section 81 (Inquiry) -> Section 87 (Surcharge) -> Section 152 (Tribunal Appeal).",
            "tip_ta": "TN கூட்டுறவு சட்ட நடைமுறை: பிரிவு 81 (விசாரணை) -> பிரிவு 87 (சர்சார்ஜ்) -> பிரிவு 152 (தீர்ப்பாய மேல்முறையீடு).",
            "fact_en": "Limitation for initiating surcharge under Section 87 is 7 years from the date of the act.",
            "fact_ta": "பிரிவு 87-ன் கீழ் சர்சார்ஜ் நடவடிக்கை தொடங்குவதற்கான கால வரம்பு தவறு நிகழ்ந்த தேதியிலிருந்து 7 ஆண்டுகள் ஆகும்."
        },

        # 7. Statutory Inquiry in Tamil Nadu (Section 81)
        {
            "subtopic": "Tamil Nadu Cooperative Governance",
            "stem_en": "Under Section 81 of the Tamil Nadu Co-operative Societies Act, 1983, who possesses the statutory authority to order an inquiry into the constitution, working, and financial condition of a cooperative society?",
            "stem_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 81-ன் கீழ், ஒரு கூட்டுறவு சங்கத்தின் அமைப்பு, செயல்பாடு மற்றும் நிதி நிலைமை குறித்து விசாரணைக்கு உத்தரவிட சட்டப்பூர்வ அதிகாரம் யாருக்கு உள்ளது?",
            "options": [
                ("The Registrar of Co-operative Societies (suo motu or on application)", "கூட்டுறவு சங்கங்களின் பதிவாளர் (தாமாகவோ அல்லது விண்ணப்பத்தின் பேரிலோ)"),
                ("The Chief Judicial Magistrate exclusively", "தலைமை நீதித்துறை நடுவர் மட்டுமே"),
                ("The District Superintendent of Police", "மாவட்ட காவல் கண்காணிப்பாளர்"),
                ("The Union Minister of Agriculture", "மத்திய வேளாண்மை அமைச்சர்")
            ],
            "correct_key": "A",
            "exp_en": "Section 81 empowers the Registrar of Co-operative Societies, of his own motion (suo motu) or on application by a majority of the board or not less than one-third of members, to hold an inquiry into the constitution, working, and financial condition of a society.",
            "exp_ta": "பிரிவு 81 கூட்டுறவு சங்கங்களின் பதிவாளருக்கு, தனது சொந்த விருப்பத்தின் பேரிலோ (suo motu) அல்லது வாரியத்தின் பெரும்பான்மையினர் அல்லது மூன்றில் ஒரு பங்கு உறுப்பினர்களின் விண்ணப்பத்தின் பேரிலோ, ஒரு சங்கத்தின் அமைப்பு, செயல்பாடு மற்றும் நிதி நிலைமை குறித்து விசாரணை நடத்த அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Correct. The Registrar orders a Section 81 inquiry.",
            "why_a_ta": "சரி. பதிவாளர் பிரிவு 81 விசாரணையை உத்தரவிடுகிறார்.",
            "why_b_en": "Incorrect. Section 81 is an administrative-quasi-judicial inquiry ordered by the Registrar.",
            "why_b_ta": "தவறு. பிரிவு 81 என்பது பதிவாளரால் உத்தரவிடப்படும் நிர்வாக-பகுதி நீதி விசாரணை.",
            "why_c_en": "Incorrect. Police only investigate criminal cases registered under IPC/CrPC.",
            "why_c_ta": "தவறு. காவல்துறை குற்றவியல் வழக்குகளை மட்டுமே விசாரிக்கிறது.",
            "why_d_en": "Incorrect. State cooperatives fall under state jurisdiction (List II Entry 32).",
            "why_d_ta": "தவறு. மாநிலக் கூட்டுறவுகள் மாநில அதிகார வரம்பிற்கு உட்பட்டவை.",
            "tip_en": "A Section 81 inquiry report must be completed within 3 months (extendable up to 6 months).",
            "tip_ta": "பிரிவு 81 விசாரணை அறிக்கை 3 மாதங்களுக்குள் முடிக்கப்பட வேண்டும் (6 மாதங்கள் வரை நீட்டிக்கப்படலாம்).",
            "fact_en": "Section 81 inquiry often serves as the prerequisite foundation for Section 87 surcharge action.",
            "fact_ta": "பிரிவு 81 விசாரணை அறிக்கையே பெரும்பாலும் பிரிவு 87 சர்சார்ஜ் நடவடிக்கைக்கு அடித்தளமாக அமைகிறது."
        },

        # 8. Tamil Nadu Co-operative Tribunal (Section 152)
        {
            "subtopic": "Tamil Nadu Cooperative Governance",
            "stem_en": "Under Section 152 of the Tamil Nadu Co-operative Societies Act, 1983, who constitutes the Tamil Nadu Co-operative Tribunal to hear appeals against surcharge and dispute orders?",
            "stem_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 152-ன் கீழ், சர்சார்ஜ் மற்றும் சர்ச்சை உத்தரவுகளுக்கு எதிரான மேல்முறையீடுகளை விசாரிக்க தமிழ்நாடு கூட்டுறவு தீர்ப்பாயத்தை அமைப்பவர் யார்?",
            "options": [
                ("The Principal District Judge (District Judge) of the district designated by the Government", "அரசால் நியமிக்கப்பட்ட மாவட்ட முதன்மை அமர்வு நீதிபதி (மாவட்ட நீதிபதி)"),
                ("The Chief Secretary to Government", "அரசுத் தலைமைச் செயலாளர்"),
                ("The Deputy Registrar of Cooperatives", "கூட்டுறவு துணைப் பதிவாளர்"),
                ("The Director of Vigilance and Anti-Corruption", "ஊழல் தடுப்பு மற்றும் கண்காணிப்பு இயக்குநர்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 152 of the TN Act 1983, the Government constitutes Cooperative Tribunals, and the Principal District Judge of the district functions as the Tribunal to hear appeals against orders passed by the Registrar under Sections 87, 90, 118, etc.",
            "exp_ta": "1983 TN சட்டத்தின் பிரிவு 152-ன் கீழ், அரசு கூட்டுறவு தீர்ப்பாயங்களை அமைக்கிறது; மேலும் மாவட்ட முதன்மை அமர்வு நீதிபதியே பதிவாளர் பிறப்பித்த உத்தரவுகளுக்கு (பிரிவுகள் 87, 90 போன்றவை) எதிரான மேல்முறையீடுகளை விசாரிக்கும் தீர்ப்பாயமாகச் செயல்படுகிறார்.",
            "why_a_en": "Correct. Principal District Judge acts as the Co-operative Tribunal.",
            "why_a_ta": "சரி. மாவட்ட முதன்மை அமர்வு நீதிபதியே கூட்டுறவுத் தீர்ப்பாயமாகச் செயல்படுகிறார்.",
            "why_b_en": "Incorrect. Chief Secretary is head of the civil service, not a judicial tribunal.",
            "why_b_ta": "தவறு. தலைமைச் செயலாளர் ஆட்சிப் பணித் தலைவர், நீதித்துறைத் தீர்ப்பாயம் அல்ல.",
            "why_c_en": "Incorrect. Deputy Registrar is the officer whose order is being appealed against.",
            "why_c_ta": "தவறு. துணைப் பதிவாளரின் உத்தரவுக்கு எதிராகவே மேல்முறையீடு செய்யப்படுகிறது.",
            "why_d_en": "Incorrect. DVAC is an investigative police wing.",
            "why_d_ta": "தவறு. DVAC புலனாய்வுக் காவல் பிரிவு.",
            "tip_en": "Orders of the Co-operative Tribunal can be challenged before the Madras High Court under Article 226/227.",
            "tip_ta": "கூட்டுறவுத் தீர்ப்பாயத்தின் உத்தரவுகளை மெட்ராஸ் உயர் நீதிமன்றத்தில் சரத்து 226/227-ன் கீழ் எதிர்த்து வழக்கு தொடரலாம்.",
            "fact_en": "Special Cooperative Tribunals exist in every revenue district of Tamil Nadu.",
            "fact_ta": "தமிழ்நாட்டின் ஒவ்வொரு வருவாய் மாவட்டத்திலும் சிறப்பு கூட்டுறவு தீர்ப்பாயங்கள் உள்ளன."
        },

        # 9. Tripartite Agreement under Vaidyanathan Committee
        {
            "subtopic": "Committees and Reforms",
            "stem_en": "Under the Vaidyanathan Committee revival package for rural credit cooperatives, what tripartite Memorandum of Understanding (MoU) was signed by participating States?",
            "stem_ta": "ஊரகக் கடன் கூட்டுறவு சங்கங்களுக்கான வைத்தியநாதன் குழுவின் புத்துயிரூட்டல் தொகுப்பின் கீழ், பங்கேற்கும் மாநிலங்களால் கையெழுத்திடப்பட்ட முத்தரப்பு புரிந்துணர்வு ஒப்பந்தம் (MoU) யாருக்கிடையிலானது?",
            "options": [
                ("Government of India, State Government, and NABARD", "இந்திய அரசு, மாநில அரசு மற்றும் நபார்டு (NABARD)"),
                ("State Government, RBI, and Commercial Banks", "மாநில அரசு, ரிசர்வ் வங்கி மற்றும் வணிக வங்கிகள்"),
                ("Ministry of Agriculture, World Bank, and IMF", "வேளாண் அமைச்சகம், உலக வங்கி மற்றும் IMF"),
                ("District Cooperative Bank, PACS, and Farmers Association", "மாவட்ட கூட்டுறவு வங்கி, PACS மற்றும் விவசாயிகள் சங்கம்")
            ],
            "correct_key": "A",
            "exp_en": "The Vaidyanathan Committee reform package required a tripartite MoU between the Central Government, the State Government, and NABARD to share accumulated losses and implement statutory cooperative autonomy reforms.",
            "exp_ta": "வைத்தியநாதன் குழுவின் சீர்திருத்தத் திட்டம் திரட்டப்பட்ட நஷ்டங்களைப் பகிர்ந்து கொள்வதற்கும், சட்டப்பூர்வ தன்னாட்சி சீர்திருத்தங்களை அமல்படுத்துவதற்கும் மத்திய அரசு, மாநில அரசு மற்றும் நபார்டு இடையே முத்தரப்பு ஒப்பந்தத்தை கட்டாயமாக்கியது.",
            "why_a_en": "Correct. Tripartite MoU was between Centre, State, and NABARD.",
            "why_a_ta": "சரி. முத்தரப்பு ஒப்பந்தம் மத்திய அரசு, மாநில அரசு மற்றும் நபார்டு இடையிலானது.",
            "why_b_en": "Incorrect. Commercial banks were not signatories.",
            "why_b_ta": "தவறு. வணிக வங்கிகள் இதில் கையொப்பமிடவில்லை.",
            "why_c_en": "Incorrect. World Bank was a co-financier, not direct tripartite signatory to state MoUs.",
            "why_c_ta": "தவறு. உலக வங்கி நிதி உதவியாளர் மட்டுமே.",
            "why_d_en": "Incorrect. PACS are grassroots beneficiaries, not signing governments.",
            "why_d_ta": "தவறு. PACS-கள் பயனாளிகள், அரசு தரப்பு அல்ல.",
            "tip_en": "Sharing pattern of accumulated losses: Central Govt (68%), State Govt (28%), Cooperative Structure (4%).",
            "tip_ta": "நஷ்டப் பகிர்வு விகிதம்: மத்திய அரசு (68%), மாநில அரசு (28%), கூட்டுறவு அமைப்பு (4%).",
            "fact_en": "25 States signed the MoU to implement the Vaidyanathan Committee reforms.",
            "fact_ta": "வைத்தியநாதன் குழு சீர்திருத்தங்களைச் செயல்படுத்த 25 மாநிலங்கள் இந்த ஒப்பந்தத்தில் கையெழுத்திட்டன."
        },

        # 10. Multi-State Cooperative Societies (Amendment) Act, 2023
        {
            "subtopic": "Recent Legislative Reforms (2023)",
            "stem_en": "Which independent statutory body was created by the Multi-State Co-operative Societies (Amendment) Act, 2023 to conduct democratic elections in multi-state cooperatives?",
            "stem_ta": "பல்மாநிலக் கூட்டுறவு சங்கங்களில் ஜனநாயக ரீதியில் தேர்தல்களை நடத்துவதற்காக 2023-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டத்தால் உருவாக்கப்பட்ட சுதந்திரமான சட்டப்பூர்வ அமைப்பு எது?",
            "options": [
                ("Co-operative Election Authority", "கூட்டுறவுத் தேர்தல் ஆணையம்"),
                ("National Cooperative Commission", "தேசிய கூட்டுறவு ஆணையம்"),
                ("Election Commission of India", "இந்தியத் தேர்தல் ஆணையம்"),
                ("Central Vigilance Commission", "மத்திய ஊழல் கண்காணிப்பு ஆணையம்")
            ],
            "correct_key": "A",
            "exp_en": "The MSCS (Amendment) Act, 2023 inserted Section 45 to establish the 'Co-operative Election Authority' consisting of a Chairperson, Vice-Chairperson, and up to 3 members appointed by the Central Government to conduct fair elections in multi-state societies.",
            "exp_ta": "2023 MSCS திருத்தச் சட்டம் பிரிவு 45-ஐச் சேர்த்து, பல்மாநில சங்கங்களில் நேர்மையான தேர்தல்களை நடத்த மத்திய அரசால் நியமிக்கப்படும் தலைவர், துணைத்தலைவர் மற்றும் 3 உறுப்பினர்களைக் கொண்ட 'கூட்டுறவுத் தேர்தல் ஆணையத்தை' (Co-operative Election Authority) நிறுவியது.",
            "why_a_en": "Correct. Co-operative Election Authority was established under the 2023 amendment.",
            "why_a_ta": "சரி. கூட்டுறவுத் தேர்தல் ஆணையம் 2023 திருத்தச் சட்டத்தின் கீழ் நிறுவப்பட்டது.",
            "why_b_en": "Incorrect. National Cooperative Commission is not the election body.",
            "why_b_ta": "தவறு. தேசிய கூட்டுறவு ஆணையம் தேர்தல் அமைப்பு அல்ல.",
            "why_c_en": "Incorrect. ECI conducts parliamentary and state assembly polls.",
            "why_c_ta": "தவறு. ECI நாடாளுமன்ற/சட்டமன்ற தேர்தல்களை நடத்துகிறது.",
            "why_d_en": "Incorrect. CVC is an anti-corruption body.",
            "why_d_ta": "தவறு. CVC ஊழல் தடுப்பு அமைப்பு.",
            "tip_en": "The 2023 Act also introduced a 'Co-operative Ombudsman' for member grievances and a 'Cooperative Rehabilitation and Development Fund'.",
            "tip_ta": "2023 சட்டம் உறுப்பினர் குறைகளுக்காக 'கூட்டுறவு குறைதீர்ப்பாளர்' மற்றும் 'கூட்டுறவு மறுவாழ்வு மற்றும் மேம்பாட்டு நிதியையும்' அறிமுகப்படுத்தியது.",
            "fact_en": "The 2023 Act mandates that no board member can be elected for more than 2 consecutive terms.",
            "fact_ta": "2023 சட்டம் எந்தவொரு வாரிய உறுப்பினரும் தொடர்ந்து 2 பதவிக்காலங்களுக்கு மேல் தேர்ந்தெடுக்கப்பட முடியாது என்று விதிக்கிறது."
        },

        # 11. Cooperative Ombudsman under MSCS Act 2023
        {
            "subtopic": "Recent Legislative Reforms (2023)",
            "stem_en": "Under the Multi-State Co-operative Societies (Amendment) Act, 2023, what is the role of the newly created 'Co-operative Ombudsman'?",
            "stem_ta": "2023-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டத்தின் கீழ், புதிதாக உருவாக்கப்பட்ட 'கூட்டுறவு குறைதீர்ப்பாளரின்' (Co-operative Ombudsman) பணி என்ன?",
            "options": [
                ("To inquire into member grievances regarding deposits, shares, and service deficiencies in a time-bound manner", "வைப்புத்தொகை, பங்குகள் மற்றும் சேவை குறைபாடுகள் தொடர்பான உறுப்பினர்களின் குறைகளை காலக்கெடுவிற்குள் விசாரித்தல்"),
                ("To fix minimum support prices for agricultural commodities", "விவசாயப் பொருட்களுக்கான குறைந்தபட்ச ஆதரவு விலையை நிர்ணயித்தல்"),
                ("To audit the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கியைத் தணிக்கை செய்தல்"),
                ("To determine international export tariffs on cooperative milk", "கூட்டுறவு பாலுக்கான சர்வதேச ஏற்றுமதி வரிகளைத் தீர்மானித்தல்")
            ],
            "correct_key": "A",
            "exp_en": "The 2023 Amendment created the Co-operative Ombudsman to provide an independent, accessible forum for member grievance redressal regarding deposits, shares, transfer of securities, and corrupt practices within multi-state societies.",
            "exp_ta": "2023 திருத்தச் சட்டம் பல்மாநில சங்கங்களில் வைப்புத்தொகை, பங்குகள், பத்திரங்கள் பரிமாற்றம் மற்றும் ஊழல் முறைகேடுகள் குறித்த உறுப்பினர் குறைகளைத் தீர்ப்பதற்கு ஒரு சுதந்திரமான குறைதீர்ப்பாளரை உருவாக்கியது.",
            "why_a_en": "Correct. Ombudsman resolves member grievances against multi-state cooperatives.",
            "why_a_ta": "சரி. குறைதீர்ப்பாளர் பல்மாநில கூட்டுறவுகளுக்கு எதிரான உறுப்பினர் குறைகளைத் தீர்க்கிறார்.",
            "why_b_en": "Incorrect. CACP recommends MSP, not cooperative ombudsman.",
            "why_b_ta": "தவறு. CACP குறைந்தபட்ச ஆதரவு விலையை பரிந்துரைக்கிறது.",
            "why_c_en": "Incorrect. CAG and appointed auditors audit public institutions, not cooperative ombudsman.",
            "why_c_ta": "தவறு. RBI தணிக்கை இவருடைய பணி அல்ல.",
            "why_d_en": "Incorrect. Ministry of Commerce determines tariffs.",
            "why_d_ta": "தவறு. வர்த்தக அமைச்சகம் வரிகளைத் தீர்மானிக்கிறது.",
            "tip_en": "Ombudsman provides speedy settlement within 3 months, avoiding prolonged civil litigation.",
            "tip_ta": "குறைதீர்ப்பாளர் நீண்ட நீதிமன்ற வழக்குகளைத் தவிர்த்து 3 மாதங்களுக்குள் விரைவான தீர்வை வழங்குகிறார்.",
            "fact_en": "Ombudsman is appointed by the Central Government with territorial jurisdiction specified.",
            "fact_ta": "குறிப்பிட்ட பிராந்திய அதிகார வரம்புடன் மத்திய அரசால் குறைதீர்ப்பாளர் நியமிக்கப்படுகிறார்."
        },

        # 12. Primary Agricultural Cooperative Credit Societies (PACS) Computerization
        {
            "subtopic": "Digital Transformation & Modernization",
            "stem_en": "What is the primary objective of the Central Sector Scheme for Computerization of Primary Agricultural Credit Societies (PACS) launched in 2022?",
            "stem_ta": "2022-ல் தொடங்கப்பட்ட தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கங்களை (PACS) கணினிமயமாக்குவதற்கான மத்தியத் துறைத் திட்டத்தின் முதன்மை நோக்கம் என்ன?",
            "options": [
                ("To integrate 63,000 functional PACS onto an Enterprise Resource Planning (ERP)-based common national software linked with NABARD", "நபார்டுடன் இணைக்கப்பட்ட ERP அடிப்படையிலான பொதுவான தேசிய மென்பொருளில் 63,000 செயல்படும் PACS-களை ஒருங்கிணைப்பது"),
                ("To privatize all PACS into private non-banking financial companies", "அனைத்து PACS-களையும் தனியார் வங்கி சாரா நிதி நிறுவனங்களாக தனியார்மயமாக்குவது"),
                ("To replace all primary cooperatives with public sector bank branches", "அனைத்து தொடக்க கூட்டுறவுகளையும் பொதுத்துறை வங்கி கிளைகளாக மாற்றுவது"),
                ("To abolish agricultural credit in rural villages", "கிராமங்களில் விவசாயக் கடனை ஒழிப்பது")
            ],
            "correct_key": "A",
            "exp_en": "In June 2022, the Cabinet Committee on Economic Affairs approved the computerization of 63,000 functional PACS with a budget of over Rs. 2,500 crore to bring efficiency, transparency, and seamless integration onto a national ERP software connected to NABARD and DCCBs.",
            "exp_ta": "2022 ஜூன் மாதம், பொருளாதார விவகாரங்களுக்கான அமைச்சரவைக் குழு ரூ. 2,500 கோடிக்கும் அதிகமான பட்ஜெட்டில் 63,000 செயல்படும் PACS-களை கணினிமயமாக்க ஒப்புதல் அளித்தது; இது நபார்டு மற்றும் DCCB-களுடன் இணைக்கப்பட்ட தேசிய ERP மென்பொருளில் வெளிப்படைத்தன்மையைக் கொண்டுவருகிறது.",
            "why_a_en": "Correct. 63,000 PACS are being computerized on a common ERP national platform.",
            "why_a_ta": "சரி. 63,000 PACS-கள் ஒரு பொதுவான தேசிய ERP தளத்தில் கணினிமயமாக்கப்பட்டு வருகின்றன.",
            "why_b_en": "Incorrect. It is strengthening cooperatives, not privatizing them.",
            "why_b_ta": "தவறு. கூட்டுறவுகளை தனியார்மயமாக்குவது அல்ல.",
            "why_c_en": "Incorrect. PACS maintain their independent cooperative identity.",
            "why_c_ta": "தவறு. PACS-கள் தங்கள் தனித்துவமான அடையாளத்தைத் தக்கவைத்துக் கொள்கின்றன.",
            "why_d_en": "Incorrect. It expands credit access, does not abolish it.",
            "why_d_ta": "தவறு. இது கடன் வசதியை விரிவுபடுத்துகிறது.",
            "tip_en": "PACS computerization enables PACS to act as Common Service Centres (CSCs), fertilizer outlets, and custom hiring centers.",
            "tip_ta": "PACS கணினிமயமாக்கல் அவை பொது சேவை மையங்களாக (CSC) மற்றும் உர விற்பனை நிலையங்களாகச் செயல்பட உதவுகிறது.",
            "fact_en": "Model By-laws for PACS were formulated in 2022 allowing PACS to undertake 25+ business activities.",
            "fact_ta": "PACS-கள் 25-க்கும் மேற்பட்ட வணிக நடவடிக்கைகளை மேற்கொள்ள அனுமதிக்கும் மாதிரி துணைவிதிகள் 2022-ல் உருவாக்கப்பட்டன."
        },

        # 13. Model By-laws for PACS (2022)
        {
            "subtopic": "Digital Transformation & Modernization",
            "stem_en": "The Model By-laws for PACS circulated by the Ministry of Cooperation in 2022 enable PACS to diversify into which of the following multidimensional services?",
            "stem_ta": "2022-ல் கூட்டுறவு அமைச்சகத்தால் வெளியிடப்பட்ட PACS-களுக்கான மாதிரி துணைவிதிகள், PACS-கள் பின்வரும் எந்தப் பலபரிமாண சேவைகளில் ஈடுபட உதவுகின்றன?",
            "options": [
                ("Common Service Centres (CSCs), retail petrol/LPG dealerships, dairy, fisheries, and grain storage", "பொது சேவை மையங்கள் (CSCs), சில்லறை பெட்ரோல்/LPG விற்பனை, பால் பண்ணை, மீன்வளம் மற்றும் தானிய சேமிப்பு"),
                ("Commercial airline passenger services exclusively", "வணிக ரீதியான விமான பயணிகள் போக்குவரத்து மட்டுமே"),
                ("Issuing sovereign national currency", "நாட்டின் இறையாண்மை நாணயத்தை வெளியிடுதல்"),
                ("Foreign embassy visa processing", "வெளிநாட்டுத் தூதரக விசா செயலாக்கம்")
            ],
            "correct_key": "A",
            "exp_en": "The Model By-laws drafted in 2022 enable PACS to become multi-purpose economic hubs, diversifying into over 25 activities including dairy, fisheries, setting up godowns, procurement, LPG/petrol retail outlets, and operating as Common Service Centres (CSCs).",
            "exp_ta": "2022-ல் உருவாக்கப்பட்ட மாதிரி துணைவிதிகள் PACS-களை பல்நோக்கு பொருளாதார மையங்களாக மாற்றுகின்றன; பால் பண்ணை, மீன்வளம், கிடங்குகள் அமைத்தல், கொள்முதல், எல்பிஜி/பெட்ரோல் விற்பனை மற்றும் பொது சேவை மையங்களாக (CSC) செயல்படுவது உள்ளிட்ட 25-க்கும் மேற்பட்ட நடவடிக்கைகளில் அவை ஈடுபடலாம்.",
            "why_a_en": "Correct. Model By-laws transform PACS into vibrant rural multi-purpose hubs.",
            "why_a_ta": "சரி. மாதிரி துணைவிதிகள் PACS-களை பல்நோக்கு ஊரக மையங்களாக மாற்றுகின்றன.",
            "why_b_en": "Incorrect. Airlines are large capital enterprises outside PACS scope.",
            "why_b_ta": "தவறு. விமான சேவைகள் PACS வரம்பிற்கு அப்பாற்பட்டவை.",
            "why_c_en": "Incorrect. Currency issuance is the sovereign monopoly of RBI.",
            "why_c_ta": "தவறு. நாணயம் வெளியிடுவது ரிசர்வ் வங்கியின் இறையாண்மை அதிகாரம்.",
            "why_d_en": "Incorrect. Diplomatic visa processing is an exclusive Ministry of External Affairs power.",
            "why_d_ta": "தவறு. விசா வழங்குவது வெளியுறவு அமைச்சகத்தின் பணி.",
            "tip_en": "Over 50,000 PACS have already on-boarded as Common Service Centres (CSCs) offering 300+ government services in villages.",
            "tip_ta": "50,000-க்கும் மேற்பட்ட PACS-கள் கிராமங்களில் 300+ அரசு சேவைகளை வழங்கும் பொது சேவை மையங்களாக (CSCs) இணைந்துள்ளன.",
            "fact_en": "World's Largest Grain Storage Plan in the Cooperative Sector was launched in 2023 leveraging PACS godowns.",
            "fact_ta": "PACS கிடங்குகளைப் பயன்படுத்தி கூட்டுறவுத் துறையில் உலகின் மிகப்பெரிய தானிய சேமிப்புத் திட்டம் 2023-ல் தொடங்கப்பட்டது."
        },

        # 14. World's Largest Grain Storage Scheme
        {
            "subtopic": "National Cooperative Initiatives",
            "stem_en": "The 'World's Largest Grain Storage Plan in the Cooperative Sector' approved in 2023 aims to create what decentralized storage capacity at the PACS level?",
            "stem_ta": "2023-ல் அங்கீகரிக்கப்பட்ட 'கூட்டுறவுத் துறையில் உலகின் மிகப்பெரிய தானிய சேமிப்புத் திட்டம்' PACS மட்டத்தில் என்ன பரவலாக்கப்பட்ட சேமிப்புத் திறனை உருவாக்குவதை நோக்கமாகக் கொண்டுள்ளது?",
            "options": [
                ("700 Lakh Metric Tonnes (70 Million Tonnes) over 5 years", "5 ஆண்டுகளில் 700 லட்சம் மெட்ரிக் டன் (70 மில்லியன் டன்)"),
                ("10 Lakh Metric Tonnes", "10 லட்சம் மெட்ரிக் டன்"),
                ("50,000 Metric Tonnes", "50,000 மெட்ரிக் டன்"),
                ("1 Crore Metric Tonnes only", "1 கோடி மெட்ரிக் டன் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "On 31st May 2023, the Union Cabinet approved the pilot project for the 'World's Largest Grain Storage Plan in Cooperative Sector' to create 700 Lakh Metric Tonnes of storage capacity across PACS, reducing post-harvest distress sales and food grain wastage.",
            "exp_ta": "2023 மே 31 அன்று, மத்திய அமைச்சரவை PACS-கள் முழுவதும் 700 லட்சம் மெட்ரிக் டன் சேமிப்புத் திறனை உருவாக்கி, அறுவடைக்குப் பிந்தைய அவசர விற்பனை மற்றும் தானிய விரயத்தைக் குறைக்க உலகின் மிகப்பெரிய தானிய சேமிப்புத் திட்டத்திற்கு ஒப்புதல் அளித்தது.",
            "why_a_en": "Correct. Target is 700 Lakh MT (70 Million Tonnes) storage.",
            "why_a_ta": "சரி. இலக்கு 700 லட்சம் மெட்ரிக் டன் சேமிப்புத் திறன் ஆகும்.",
            "why_b_en": "Incorrect. 10 Lakh MT is too small.",
            "why_b_ta": "தவறு. 10 லட்சம் மெட்ரிக் டன் மிகக் குறைவு.",
            "why_c_en": "Incorrect. 50,000 MT is negligible for a national scheme.",
            "why_c_ta": "தவறு. 50,000 மெட்ரிக் டன் தேசிய திட்டத்திற்குப் போதாது.",
            "why_d_en": "Incorrect. Target is 7 Crore MT (700 Lakh MT), not 1 Crore MT.",
            "why_d_ta": "தவறு. இலக்கு 7 கோடி மெட்ரிக் டன் (700 லட்சம் MT).",
            "tip_en": "Converges schemes like Agriculture Infrastructure Fund (AIF), AMI, and PMKSY.",
            "tip_ta": "வேளாண் உள்கட்டமைப்பு நிதி (AIF) மற்றும் PMKSY போன்ற திட்டங்களை இது ஒருங்கிணைக்கிறது.",
            "fact_en": "Farmers can store crops in PACS godowns and obtain warehouse receipt pledge loans without distress selling.",
            "fact_ta": "விவசாயிகள் PACS கிடங்குகளில் தானியங்களைச் சேமித்து கிடங்கு ரசீது அடமானக் கடன்களைப் பெறலாம்."
        },

        # 15. Three New National Cooperative Societies (2023)
        {
            "subtopic": "Institutional Architecture - National Level",
            "stem_en": "In January 2023, the Union Cabinet approved the promotion of three new apex Multi-State Cooperative Societies under the MSCS Act, 2002 covering which three distinct strategic sectors?",
            "stem_ta": "2023 ஜனவரியில், மத்திய அமைச்சரவை MSCS சட்டம் 2002-ன் கீழ் எந்த மூன்று தனித்துவமான மூலோபாயத் துறைகளை உள்ளடக்கிய மூன்று புதிய தலைமைக் கூட்டுறவு சங்கங்களை அமைக்க ஒப்புதல் அளித்தது?",
            "options": [
                ("Organic Produce, Seeds, and Exports", "இயற்கை வேளாண் பொருட்கள், விதைகள், மற்றும் ஏற்றுமதி"),
                ("Coal Mining, Steel Manufacturing, and Petroleum", "நிலக்கரி சுரங்கம், எஃகு உற்பத்தி, மற்றும் பெட்ரோலியம்"),
                ("Nuclear Power, Space Satellites, and Defense Weapons", "அணுசக்தி, விண்வெளி செயற்கைக்கோள்கள், மற்றும் பாதுகாப்பு ஆயுதங்கள்"),
                ("Telecommunications, Road Highways, and Shipping Ports", "தொலைத்தொடர்பு, தேசிய நெடுஞ்சாலைகள், மற்றும் துறைமுகங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "In January 2023, the Union Cabinet approved the establishment of 3 national-level multi-state cooperative societies: 1. National Cooperative Organics Ltd (NCOL), 2. Bharatiya Beej Sahakari Samiti Ltd (BBSSL - Seeds), and 3. National Cooperative Exports Ltd (NCEL).",
            "exp_ta": "2023 ஜனவரியில், மத்திய அமைச்சரவை 3 தேசிய அளவிலான பல்மாநில கூட்டுறவு சங்கங்களை அமைக்க ஒப்புதல் அளித்தது: 1. தேசிய கூட்டுறவு இயற்கை வேளாண் நிறுவனம் (NCOL), 2. பாரதிய பீஜ் கூட்டுறவு சங்கம் (BBSSL - விதைகள்), மற்றும் 3. தேசிய கூட்டுறவு ஏற்றுமதி நிறுவனம் (NCEL).",
            "why_a_en": "Correct. Organics, Seeds, and Exports are the 3 designated national cooperative societies.",
            "why_a_ta": "சரி. இயற்கை பொருட்கள், விதைகள் மற்றும் ஏற்றுமதி ஆகியவை அந்த மூன்று புதிய சங்கங்களாகும்.",
            "why_b_en": "Incorrect. Heavy industries are governed by public/private corporate models.",
            "why_b_ta": "தவறு. கனரகத் தொழில்கள் கார்ப்பரேட் மாதிரிகளால் ஆளப்படுகின்றன.",
            "why_c_en": "Incorrect. Strategic defense and atomic energy are statutory central monopolies.",
            "why_c_ta": "தவறு. பாதுகாப்பு மற்றும் அணுசக்தி மத்திய அரசின் நேரடி கட்டுப்பாட்டில் உள்ளன.",
            "why_d_en": "Incorrect. Infrastructure sectors are handled by NHAI, Port Trusts, etc.",
            "why_d_ta": "தவறு. உள்கட்டமைப்புத் துறைகள் NHAI போன்றவற்றால் நிர்வகிக்கப்படுகின்றன.",
            "tip_en": "NCEL exports cooperative products globally; BBSSL ensures certified indigenous seeds; NCOL certifies and brands organic farm produce.",
            "tip_ta": "NCEL கூட்டுறவுப் பொருட்களை ஏற்றுமதி செய்கிறது; BBSSL சான்றளிக்கப்பட்ட விதைகளை வழங்குகிறது; NCOL இயற்கை உணவுகளை சான்றளித்து சந்தைப்படுத்துகிறது.",
            "fact_en": "These societies are promoted by leading cooperatives including Amul, IFFCO, KRIBHCO, NAFED, and NCDC.",
            "fact_ta": "அமுல், இஃப்கோ, கிரிப்கோ, நாஃபெட் மற்றும் என்சிடிசி ஆகியவை இணைந்து இவற்றை நிறுவியுள்ளன."
        },

        # 16. National Cooperative Exports Limited (NCEL)
        {
            "subtopic": "Institutional Architecture - National Level",
            "stem_en": "What is the primary mandate of the National Cooperative Exports Limited (NCEL) registered under the Multi-State Co-operative Societies Act?",
            "stem_ta": "பல்மாநில கூட்டுறவு சங்கங்கள் சட்டத்தின் கீழ் பதிவு செய்யப்பட்ட தேசிய கூட்டுறவு ஏற்றுமதி நிறுவனத்தின் (NCEL) முதன்மைப் பணி என்ன?",
            "options": [
                ("To facilitate direct global export of agricultural produce and manufactured goods produced by cooperatives across India", "இந்தியா முழுவதும் உள்ள கூட்டுறவுகளால் உற்பத்தி செய்யப்படும் விவசாயப் பொருட்கள் மற்றும் உற்பத்திப் பொருட்களை நேரடியாக உலகளவில் ஏற்றுமதி செய்ய உதவுவது"),
                ("To import foreign military equipment", "வெளிநாட்டு ராணுவ தளவாடங்களை இறக்குமதி செய்வது"),
                ("To regulate foreign direct investment in private airlines", "தனியார் விமான நிறுவனங்களில் அந்நிய நேரடி முதலீட்டை ஒழுங்குபடுத்துவது"),
                ("To print passport booklets for international travel", "சர்வதேச பயணத்திற்கான கடவுச்சீட்டு புத்தகங்களை அச்சிடுவது")
            ],
            "correct_key": "A",
            "exp_en": "NCEL serves as an overarching umbrella organization to tap global market demand for Indian agricultural produce, dairy, sugar, and spices, ensuring that cooperative farmers receive higher export price realization directly.",
            "exp_ta": "NCEL இந்திய விவசாயப் பொருட்கள், பால் பொருட்கள், சர்க்கரை மற்றும் மசாலாப் பொருட்களுக்கான உலகளாவிய தேவையைப் பூர்த்தி செய்து, கூட்டுறவு விவசாயிகளுக்கு நேரடி ஏற்றுமதி விலை ஆதாயம் கிடைக்கச் செய்யும் தலைமை அமைப்பாகச் செயல்படுகிறது.",
            "why_a_en": "Correct. Direct agricultural and cooperative exports are NCEL's mandate.",
            "why_a_ta": "சரி. கூட்டுறவுப் பொருட்களை நேரடியாக ஏற்றுமதி செய்வதே NCEL-ன் பணியாகும்.",
            "why_b_en": "Incorrect. Defense imports are handled by Ministry of Defence.",
            "why_b_ta": "தவறு. பாதுகாப்பு இறக்குமதி பாதுகாப்பு அமைச்சகத்தின் பணி.",
            "why_c_en": "Incorrect. FDI regulation is done by DPIIT and RBI.",
            "why_c_ta": "தவறு. FDI ஒழுங்குமுறை DPIIT மற்றும் ரிசர்வ் வங்கியால் செய்யப்படுகிறது.",
            "why_d_en": "Incorrect. Passports are printed by India Security Press under MEA.",
            "why_d_ta": "தவறு. கடவுச்சீட்டு வெளியுறவு அமைச்சகத்தால் அச்சிடப்படுகிறது.",
            "tip_en": "NCEL is headquartered in New Delhi with authorized share capital of Rs. 2,000 crore.",
            "tip_ta": "NCEL ரூ. 2,000 கோடி அங்கீகரிக்கப்பட்ட பங்கு மூலதனத்துடன் புது தில்லியைத் தலைமையிடமாகக் கொண்டுள்ளது.",
            "fact_en": "NCEL has already executed multi-million dollar wheat, rice, and sugar export contracts to friendly foreign nations.",
            "fact_ta": "நட்பு நாடுகளுக்கு கோதுமை, அரிசி மற்றும் சர்க்கரை ஏற்றுமதி ஒப்பந்தங்களை NCEL ஏற்கனவே நிறைவேற்றியுள்ளது."
        },

        # 17. Bharatiya Beej Sahakari Samiti Limited (BBSSL)
        {
            "subtopic": "Institutional Architecture - National Level",
            "stem_en": "The newly established Bharatiya Beej Sahakari Samiti Limited (BBSSL) focuses on which critical aspect of the agricultural value chain?",
            "stem_ta": "புதிதாக நிறுவப்பட்ட பாரதிய பீஜ் கூட்டுறவு சங்கம் (BBSSL) விவசாய மதிப்புச் சங்கிலியின் எந்த முக்கியமான அம்சத்தில் கவனம் செலுத்துகிறது?",
            "options": [
                ("Conservation, certification, and distribution of indigenous, certified quality seeds through cooperatives", "கூட்டுறவுகள் மூலம் உள்நாட்டு, சான்றளிக்கப்பட்ட தரமான விதைகளைப் பாதுகாத்தல், சான்றளித்தல் மற்றும் விநியோகித்தல்"),
                ("Manufacture of synthetic chemical fertilizers", "செயற்கை இரசாயன உரங்கள் தயாரிப்பு"),
                ("Satellite telecommunications for weather monitoring", "வானிலை கண்காணிப்புக்கான செயற்கைக்கோள் தொலைத்தொடர்பு"),
                ("Construction of railway freight corridors", "ரயில் சரக்கு வழித்தடங்களை அமைத்தல்")
            ],
            "correct_key": "A",
            "exp_en": "BBSSL acts as an apex multi-state cooperative for certified seed production, preservation of traditional and indigenous seed varieties, genetic enhancement, and distribution to farmers through PACS, reducing reliance on private seed monopolies.",
            "exp_ta": "BBSSL சான்றளிக்கப்பட்ட விதை உற்பத்தி, பாரம்பரிய மற்றும் உள்நாட்டு விதை ரகங்களைப் பாதுகாத்தல், மரபணு மேம்பாடு மற்றும் PACS மூலம் விவசாயிகளுக்கு விநியோகித்தல் ஆகியவற்றிற்கான தலைமை பல்மாநிலக் கூட்டுறவாகச் செயல்பட்டு, தனியார் விதை நிறுவனங்களின் ஆதிக்கத்தைக் குறைக்கிறது.",
            "why_a_en": "Correct. BBSSL is dedicated to seeds (Beej) conservation and distribution.",
            "why_a_ta": "சரி. BBSSL விதைகள் (Beej) பாதுகாப்பு மற்றும் விநியோகத்திற்காக அர்ப்பணிக்கப்பட்டுள்ளது.",
            "why_b_en": "Incorrect. Chemical fertilizers are produced by IFFCO/KRIBHCO.",
            "why_b_ta": "தவறு. இரசாயன உரங்கள் இஃப்கோ/கிரிப்கோவால் தயாரிக்கப்படுகின்றன.",
            "why_c_en": "Incorrect. Weather monitoring is done by IMD and ISRO.",
            "why_c_ta": "தவறு. வானிலை கண்காணிப்பு IMD மற்றும் இஸ்ரோவின் பணி.",
            "why_d_en": "Incorrect. Railway freight is handled by Dedicated Freight Corridor Corporation.",
            "why_d_ta": "தவறு. ரயில் சரக்கு போக்குவரத்து ரயில்வேயின் பணி.",
            "tip_en": "Remember: 'Beej' = Seeds; BBSSL = National Cooperative Seed Society.",
            "tip_ta": "நினைவில் கொள்க: 'பீஜ்' (Beej) = விதைகள்; BBSSL = தேசிய கூட்டுறவு விதை சங்கம்.",
            "fact_en": "India's certified seed replacement rate will be accelerated through BBSSL's network.",
            "fact_ta": "BBSSL கட்டமைப்பு மூலம் இந்தியாவின் சான்றளிக்கப்பட்ட விதை மாற்று விகிதம் துரிதப்படுத்தப்படும்."
        },

        # 18. National Cooperative Organics Limited (NCOL)
        {
            "subtopic": "Institutional Architecture - National Level",
            "stem_en": "Under which official brand name has the National Cooperative Organics Limited (NCOL) launched its certified organic food products across India?",
            "stem_ta": "தேசிய கூட்டுறவு இயற்கை வேளாண் நிறுவனம் (NCOL) தனது சான்றளிக்கப்பட்ட இயற்கை உணவுப் பொருட்களை இந்தியா முழுவதும் எந்த அதிகாரப்பூர்வ பிராண்ட் பெயரில் அறிமுகப்படுத்தியுள்ளது?",
            "options": [
                ("'Bharat Organics'", "'பாரத் ஆர்கானிக்ஸ்' (Bharat Organics)"),
                ("'Amul Pure'", "'அமுல் பியூர்'"),
                ("'Coop Green'", "'கூப் கிரீன்'"),
                ("'Sahakar Organic'", "'சககார் ஆர்கானிக்'")
            ],
            "correct_key": "A",
            "exp_en": "National Cooperative Organics Limited (NCOL) markets authentic, certified organic food products under the brand name 'Bharat Organics', providing testing, organic certification, processing, and direct marketing to fetch premium prices for organic farmers.",
            "exp_ta": "தேசிய கூட்டுறவு இயற்கை வேளாண் நிறுவனம் (NCOL) 'பாரத் ஆர்கானிக்ஸ்' (Bharat Organics) என்ற பிராண்ட் பெயரில் உண்மையான, சான்றளிக்கப்பட்ட இயற்கை உணவுப் பொருட்களை சந்தைப்படுத்துகிறது; இது இயற்கை விவசாயிகளுக்கு கூடுதல் விலை கிடைக்கச் செய்கிறது.",
            "why_a_en": "Correct. 'Bharat Organics' is NCOL's flagship commercial brand.",
            "why_a_ta": "சரி. 'பாரத் ஆர்கானிக்ஸ்' என்பது NCOL-ன் முதன்மை பிராண்டாகும்.",
            "why_b_en": "Incorrect. Amul is a distinct dairy brand.",
            "why_b_ta": "தவறு. அமுல் ஒரு தனி பால் பிராண்ட்.",
            "why_c_en": "Incorrect. 'Coop Green' is not the brand name.",
            "why_c_ta": "தவறு. 'கூப் கிரீன்' அல்ல.",
            "why_d_en": "Incorrect. 'Sahakar Organic' is not the registered brand.",
            "why_d_ta": "தவறு. 'சககார் ஆர்கானிக்' அல்ல.",
            "tip_en": "Products include pulses, rice, wheat, honey, and jaggery certified by accredited organic laboratories.",
            "tip_ta": "இதில் பருப்பு வகைகள், அரிசி, கோதுமை, தேன் மற்றும் வெல்லம் ஆகியவை ஆய்வகங்களால் சான்றளிக்கப்பட்டு விற்பனை செய்யப்படுகின்றன.",
            "fact_en": "Profits generated by NCOL are transferred directly into the bank accounts of organic farmers.",
            "fact_ta": "NCOL ஈட்டும் லாபம் நேரடியாக இயற்கை விவசாயிகளின் வங்கிக் கணக்குகளுக்கு மாற்றப்படுகிறது."
        },

        # 19. Cooperative Credit Structure Layers in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "What is the apex banking institution of the short-term rural cooperative credit structure in Tamil Nadu?",
            "stem_ta": "தமிழ்நாட்டில் குறுகிய கால ஊரகக் கூட்டுறவுக் கடன் கட்டமைப்பின் தலைமை வங்கி நிறுவனம் எது?",
            "options": [
                ("Tamil Nadu State Apex Co-operative Bank (TNSC Bank)", "தமிழ்நாடு மாநில தலைமைக் கூட்டுறவு வங்கி (TNSC Bank)"),
                ("State Bank of India Chennai Circle", "பாரத ஸ்டேட் வங்கி சென்னை வட்டம்"),
                ("NABARD Tamil Nadu Regional Office", "நபார்டு தமிழ்நாடு மண்டல அலுவலகம்"),
                ("Tamil Nadu Industrial Investment Corporation (TIIC)", "தமிழ்நாடு தொழில் முதலீட்டுக் கழகம் (TIIC)")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu State Apex Co-operative Bank Limited (TNSC Bank), established in 1905, is the apex institution for the short-term cooperative credit structure in Tamil Nadu, serving through 23 District Central Co-operative Banks (DCCBs) and over 4,400 PACS.",
            "exp_ta": "1905-ல் நிறுவப்பட்ட தமிழ்நாடு மாநில தலைமைக் கூட்டுறவு வங்கி (TNSC Bank), தமிழ்நாட்டின் குறுகிய காலக் கூட்டுறவுக் கடன் கட்டமைப்பின் உச்ச அமைப்பாகும்; இது 23 மாவட்ட மத்தியக் கூட்டுறவு வங்கிகள் (DCCBs) மற்றும் 4,400-க்கும் மேற்பட்ட PACS-கள் மூலம் செயல்படுகிறது.",
            "why_a_en": "Correct. TNSC Bank is the apex cooperative bank in Tamil Nadu.",
            "why_a_ta": "சரி. TNSC வங்கி தமிழ்நாட்டின் தலைமைக் கூட்டுறவு வங்கியாகும்.",
            "why_b_en": "Incorrect. SBI is a commercial scheduled bank.",
            "why_b_ta": "தவறு. SBI ஒரு வர்த்தக வங்கி.",
            "why_c_en": "Incorrect. NABARD is a national refinancing institution.",
            "why_c_ta": "தவறு. நபார்டு தேசிய மறுநிதியளிப்பு நிறுவனம்.",
            "why_d_en": "Incorrect. TIIC is a state industrial finance corporation.",
            "why_d_ta": "தவறு. TIIC என்பது மாநில தொழில் நிதி நிறுவனம்.",
            "tip_en": "3-Tier TN Cooperative Credit: Village = PACS -> District = DCCBs (23 in TN) -> State Apex = TNSC Bank.",
            "tip_ta": "3 அடுக்கு TN கூட்டுறவு கடன்: கிராமம் = PACS -> மாவட்டம் = DCCBs (23 வங்கிகள்) -> மாநில தலைமை = TNSC வங்கி.",
            "fact_en": "TNSC Bank is one of the oldest state cooperative banks in India, functioning for over a century.",
            "fact_ta": "TNSC வங்கி ஒரு நூற்றாண்டுக்கும் மேலாகச் செயல்பட்டு வரும் இந்தியாவின் மிகப்பழமையான மாநிலக் கூட்டுறவு வங்கிகளில் ஒன்றாகும்."
        },

        # 20. TANSCERD Institution
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "What is the primary role of the Tamil Nadu Agricultural and Rural Development Bank (TNCSARD / TANSCERD) in the state credit hierarchy?",
            "stem_ta": "மாநிலக் கடன் படிநிலையில் தமிழ்நாடு கூட்டுறவு மாநில வேளாண்மை மற்றும் ஊரக வளர்ச்சி வங்கியின் (TNCSARD) முதன்மைப் பணி என்ன?",
            "options": [
                ("Providing long-term investment credit for agriculture, tractor purchase, minor irrigation, and land development", "விவசாயம், டிராக்டர் வாங்குதல், சிறுபாசனம் மற்றும் நில மேம்பாட்டிற்கு நீண்ட கால முதலீட்டுக் கடன்களை வழங்குவது"),
                ("Regulating multi-state urban cooperative banks", "பல்மாநில நகர்ப்புற கூட்டுறவு வங்கிகளை ஒழுங்குபடுத்துவது"),
                ("Printing currency for state cooperative institutions", "மாநில கூட்டுறவு நிறுவனங்களுக்கான பணத்தை அச்சிடுவது"),
                ("Managing foreign direct investments in state ports", "மாநில துறைமுகங்களில் அந்நிய நேரடி முதலீட்டை நிர்வகிப்பது")
            ],
            "correct_key": "A",
            "exp_en": "The Long-Term Cooperative Credit Structure in Tamil Nadu is a 2-tier federal structure with the Tamil Nadu Co-operative State Agriculture and Rural Development Bank (TNCSARDB) at the state level and Primary Agriculture and Rural Development Banks (PCARDBs) at the taluk/block level providing long-term loans up to 15-20 years.",
            "exp_ta": "தமிழ்நாட்டில் நீண்ட காலக் கூட்டுறவுக் கடன் அமைப்பு 2 அடுக்கு அமைப்பாகும்: மாநில அளவில் தமிழ்நாடு கூட்டுறவு மாநில வேளாண்மை மற்றும் ஊரக வளர்ச்சி வங்கியும் (TNCSARDB), தாலுகா அளவில் தொடக்க வேளாண்மை மற்றும் ஊரக வளர்ச்சி வங்கிகளும் (PCARDBs) 15-20 ஆண்டுகள் வரையிலான நீண்ட காலக் கடன்களை வழங்குகின்றன.",
            "why_a_en": "Correct. Long-term capital investment credit for farming is TNCSARD's mandate.",
            "why_a_ta": "சரி. விவசாயத்திற்கான நீண்ட கால மூலதனக் கடன்களை வழங்குவதே இதன் பணியாகும்.",
            "why_b_en": "Incorrect. RBI regulates urban cooperative banks.",
            "why_b_ta": "தவறு. RBI நகர்ப்புற கூட்டுறவு வங்கிகளை ஒழுங்குபடுத்துகிறது.",
            "why_c_en": "Incorrect. Only RBI prints currency in India.",
            "why_c_ta": "தவறு. RBI மட்டுமே பணத்தை அச்சிடுகிறது.",
            "why_d_en": "Incorrect. Ports are unrelated.",
            "why_d_ta": "தவறு. துறைமுகங்கள் தொடர்பற்றவை.",
            "tip_en": "Short-term credit = 3-Tier (PACS -> DCCB -> TNSC Bank); Long-term credit = 2-Tier (PCARDB -> TNCSARDB).",
            "tip_ta": "குறுகிய கால கடன் = 3 அடுக்கு (PACS -> DCCB -> TNSC வங்கி); நீண்ட கால கடன் = 2 அடுக்கு (PCARDB -> TNCSARDB).",
            "fact_en": "Long-term loans finance capital creation like borewells, solar pumps, farm mechanization, and horticulture.",
            "fact_ta": "ஆழ்துளைக் கிணறுகள், சோலார் பம்புகள், இயந்திரமயமாக்கல் மற்றும் தோட்டக்கலை போன்ற மூலதன உருவாக்கத்திற்கு நீண்ட காலக் கடன்கள் உதவுகின்றன."
        },

        # 21. Chaudhary Brahm Perkash Committee (1991)
        {
            "subtopic": "Committees and Commissions",
            "stem_en": "Which expert committee appointed by the Planning Commission in 1991 drafted the landmark 'Model Cooperatives Act' to free cooperatives from state control?",
            "stem_ta": "கூட்டுறவுகளை அரசின் கட்டுப்பாட்டிலிருந்து விடுவிப்பதற்காக 1991-ல் திட்டக் குழுவால் நியமிக்கப்பட்டு புகழ்பெற்ற 'மாதிரி கூட்டுறவுச் சட்டத்தை' (Model Cooperatives Act) வரைந்த நிபுணர் குழு எது?",
            "options": [
                ("Chaudhary Brahm Perkash Committee", "சவுத்ரி பிரம்ம பிரகாஷ் குழு"),
                ("Sarkaria Commission", "சர்க்காரியா ஆணையம்"),
                ("Punchhi Commission", "பூஞ்சி ஆணையம்"),
                ("Verghese Kurien Task Force", "வர்கீஸ் குரியன் பணிக்குழு")
            ],
            "correct_key": "A",
            "exp_en": "The Planning Commission appointed an Expert Committee in 1990 under Chaudhary Brahm Perkash (India's prominent cooperative leader and Delhi's first Chief Minister) which submitted the 'Model Cooperatives Act, 1991', advocating voluntary formation, self-reliance, and stripping Registrar of arbitrary supersession powers.",
            "exp_ta": "திட்டக் குழு 1990-ல் சவுத்ரி பிரம்ம பிரகாஷ் தலைமையில் ஒரு நிபுணர் குழுவை அமைத்தது; இக்குழு 1991-ல் 'மாதிரி கூட்டுறவுச் சட்டத்தை' சமர்ப்பித்து, தன்னாட்சி, சுயசார்பு மற்றும் பதிவாளரின் தன்னிச்சையான அதிகாரங்களைக் கட்டுப்படுத்துவதை வலியுறுத்தியது.",
            "why_a_en": "Correct. Chaudhary Brahm Perkash drafted the 1991 Model Cooperatives Act.",
            "why_a_ta": "சரி. சவுத்ரி பிரம்ம பிரகாஷ் 1991 மாதிரி கூட்டுறவுச் சட்டத்தை வரைந்தார்.",
            "why_b_en": "Incorrect. Sarkaria Commission dealt with Centre-State Relations (1983-88).",
            "why_b_ta": "தவறு. சர்க்காரியா ஆணையம் மத்திய-மாநில உறவுகளைக் கையாண்டது.",
            "why_c_en": "Incorrect. Punchhi Commission dealt with Centre-State Relations (2007-10).",
            "why_c_ta": "தவறு. பூஞ்சி ஆணையம் மத்திய-மாநில உறவுகளைக் கையாண்டது.",
            "why_d_en": "Incorrect. Kurien was NDDB chairman, not chair of this planning commission committee.",
            "why_d_ta": "தவறு. குரியன் NDDB தலைவராக இருந்தார்.",
            "tip_en": "The 1991 Model Act inspired state parallel cooperative acts like Andhra Pradesh Mutually Aided Cooperative Societies Act (MACS Act 1995).",
            "tip_ta": "1991 மாதிரி சட்டம் ஆந்திரப் பிரதேச MACS சட்டம் 1995 போன்ற அரசு நிதியற்ற தன்னாட்சி கூட்டுறவுச் சட்டங்களுக்கு வழிகாட்டியது.",
            "fact_en": "Chaudhary Brahm Perkash is celebrated as the champion of cooperative autonomy in independent India.",
            "fact_ta": "சுதந்திர இந்தியாவில் கூட்டுறவு தன்னாட்சியின் முன்னோடியாக சவுத்ரி பிரம்ம பிரகாஷ் போற்றப்படுகிறார்."
        },

        # 22. Shivaji Rao Patil Committee (2009)
        {
            "subtopic": "Committees and Commissions",
            "stem_en": "The High-Powered Committee on Co-operatives (2009) whose recommendations directly provided the foundation for the 97th Constitutional Amendment was chaired by whom?",
            "stem_ta": "97வது அரசியலமைப்புத் திருத்தச் சட்டத்திற்கு நேரடி அடித்தளத்தை வழங்கிய கூட்டுறவுக்கான உயர்மட்டக் குழு (2009) யாருடைய தலைமையில் அமைக்கப்பட்டது?",
            "options": [
                ("Shivaji Rao Patil", "சிவாஜி ராவ் பாட்டீல்"),
                ("Montek Singh Ahluwalia", "மாண்டேக் சிங் அலுவாலியா"),
                ("C. Rangarajan", "சி. ரங்கராஜன்"),
                ("M.S. Swaminathan", "எம்.எஸ். சுவாமிநாதன்")
            ],
            "correct_key": "A",
            "exp_en": "The High-Powered Committee on Co-operatives constituted under the chairmanship of veteran cooperator Shivaji Rao Patil submitted its report in 2009, strongly recommending constitutional amendments to guarantee autonomous, democratic, and professional cooperative governance.",
            "exp_ta": "மூத்த கூட்டுறவுத் தலைவர் சிவாஜி ராவ் பாட்டீல் தலைமையில் அமைக்கப்பட்ட கூட்டுறவுக்கான உயர்மட்டக் குழு 2009-ல் தனது அறிக்கையை சமர்ப்பித்தது; இது தன்னாட்சி, ஜனநாயக மற்றும் தொழில்முறை கூட்டுறவு நிர்வாகத்தை உத்தரவாதம் செய்ய அரசியலமைப்புத் திருத்தத்தைப் பரிந்துரைத்தது.",
            "why_a_en": "Correct. Shivaji Rao Patil Committee led to the 97th CAA 2011.",
            "why_a_ta": "சரி. சிவாஜி ராவ் பாட்டீல் குழுவே 97வது திருத்தத்திற்கு வழிவகுத்தது.",
            "why_b_en": "Incorrect. Ahluwalia was Deputy Chairman of Planning Commission.",
            "why_b_ta": "தவறு. அலுவாலியா திட்டக் குழு துணைத் தலைவராக இருந்தார்.",
            "why_c_en": "Incorrect. Rangarajan chaired the Economic Advisory Council.",
            "why_c_ta": "தவறு. ரங்கராஜன் பொருளாதார ஆலோசனைக் குழுவின் தலைவராக இருந்தார்.",
            "why_d_en": "Incorrect. Swaminathan chaired the National Commission on Farmers (2004-06).",
            "why_d_ta": "தவறு. சுவாமிநாதன் தேசிய விவசாயிகள் ஆணையத்தின் தலைவராக இருந்தார்.",
            "tip_en": "Patil Committee recommended: Fixed 5-year tenure, max 21 directors, SC/ST and Women reservation, and independent election commission.",
            "tip_ta": "பாட்டீல் குழு பரிந்துரைத்தவை: நிலையான 5 ஆண்டு காலம், அதிகபட்சம் 21 இயக்குநர்கள், SC/ST மற்றும் மகளிர் இடஒதுக்கீடு, மற்றும் தனி தேர்தல் ஆணையம்.",
            "fact_en": "These exact recommendations became Articles 243ZJ, 243ZK, and 243ZL in Part IX-B.",
            "fact_ta": "இந்தப் பரிந்துரைகளே பகுதி IX-B-ல் சரத்துகள் 243ZJ, 243ZK, மற்றும் 243ZL ஆக மாறின."
        },

        # 23. Maclagan Committee (1914-15)
        {
            "subtopic": "Historical Committees",
            "stem_en": "Which colonial committee on cooperation (1914-15) recommended the structural division of cooperatives into primary societies, central banks, and apex provincial banks?",
            "stem_ta": "கூட்டுறவுகளை தொடக்கச் சங்கங்கள், மத்திய வங்கிகள் மற்றும் மாகாண தலைprocess வங்கிகள் என கட்டமைப்பு ரீதியாகப் பிரிக்கப் பரிந்துரைத்த காலனித்துவ காலக் கூட்டுறவுக் குழு (1914-15) எது?",
            "options": [
                ("Maclagan Committee", "மெக்லகன் குழு"),
                ("Hunter Commission", "ஹண்டர் ஆணையம்"),
                ("Babington Smith Committee", "பாபிங்டன் ஸ்மித் குழு"),
                ("Hilton Young Commission", "ஹில்டன் யங் ஆணையம்")
            ],
            "correct_key": "A",
            "exp_en": "The Maclagan Committee on Cooperation in India (1914-15), appointed by the British Government, analyzed cooperative finance and recommended the 3-tier federal structure (Primary Societies at village, Central Cooperative Banks at district, and Provincial Cooperative Banks at apex).",
            "exp_ta": "பிரிட்டிஷ் அரசால் அமைக்கப்பட்ட இந்தியக் கூட்டுறவுக்கான மெக்லகன் குழு (1914-15), கூட்டுறவு நிதியை ஆய்வு செய்து 3 அடுக்கு கூட்டாட்சி அமைப்பை (கிராமத்தில் தொடக்கச் சங்கங்கள், மாவட்டத்தில் மத்திய கூட்டுறவு வங்கிகள், மாகாண அளவில் தலைமைக் கூட்டுறவு வங்கி) பரிந்துரைத்தது.",
            "why_a_en": "Correct. Sir Edward Maclagan headed this seminal committee.",
            "why_a_ta": "சரி. சர் எட்வர்ட் மெக்லகன் இந்த முக்கிய குழுவிற்குத் தலைமை தாங்கினார்.",
            "why_b_en": "Incorrect. Hunter Commission investigated Jallianwala Bagh massacre (1919).",
            "why_b_ta": "தவறு. ஹண்டர் ஆணையம் ஜாலியன்வாலாபாக் படுகொலையை விசாரித்தது.",
            "why_c_en": "Incorrect. Babington Smith Committee dealt with Indian currency and exchange (1919).",
            "why_c_ta": "தவறு. பாபிங்டன் ஸ்மித் குழு நாணயம் மற்றும் மாற்று விகிதத்தைக் கையாண்டது.",
            "why_d_en": "Incorrect. Hilton Young Commission recommended creation of Reserve Bank of India (1926).",
            "why_d_ta": "தவறு. ஹில்டன் யங் ஆணையம் ரிசர்வ் வங்கியை உருவாக்கப் பரிந்துரைத்தது.",
            "tip_en": "Maclagan Committee emphasized: 'One member, one vote', building strong reserve funds, and careful scrutiny of loan repayments.",
            "tip_ta": "மெக்லகன் குழு வலியுறுத்தியவை: 'ஒரு உறுப்பினர், ஒரு வாக்கு', வலுவான காப்பு நிதி மற்றும் கடன் திருப்பிச் செலுத்துதலைக் கண்காணித்தல்.",
            "fact_en": "The report remains a foundational classic of cooperative banking architecture in South Asia.",
            "fact_ta": "தெற்காசியாவின் கூட்டுறவு வங்கிக் கட்டமைப்பில் இந்த அறிக்கை ஒரு வரலாற்றுச் சிறப்புமிக்க ஆவணமாகத் திகழ்கிறது."
        },

        # 24. Royal Commission on Agriculture (1928) Quote
        {
            "subtopic": "Historical Committees",
            "stem_en": "The Royal Commission on Agriculture in India (1928), chaired by Lord Linlithgow, famously observed which of the following about cooperatives?",
            "stem_ta": "லின்லித்கோ பிரபு தலைமையிலான விவசாயத்திற்கான ராயல் கமிஷன் (1928), கூட்டுறவு பற்றி பின்வருவனவற்றில் எதனைப் பிரபலமாகக் குறிப்பிட்டது?",
            "options": [
                ("'If cooperation fails, there will fail the best hope of rural India'", "'கூட்டுறவு தோற்றுப்போனால், கிராமப்புற இந்தியாவின் மிகச்சிறந்த நம்பிக்கையே தோற்றுப்போகும்'"),
                ("'Cooperation is incompatible with Indian agriculture'", "'கூட்டுறவு இந்திய விவசாயத்திற்கு பொருந்தாத ஒன்று'"),
                ("'All rural credit should be handed over to foreign banks'", "'அனைத்து கிராமப்புறக் கடன்களும் வெளிநாட்டு வங்கிகளிடம் ஒப்படைக்கப்பட வேண்டும்'"),
                ("'Cooperative societies must be abolished within a decade'", "'பத்தாண்டுகளுக்குள் கூட்டுறவு சங்கங்கள் ஒழிக்கப்பட வேண்டும்'")
            ],
            "correct_key": "A",
            "exp_en": "The Royal Commission on Agriculture (1928) emphasized the irreplaceable role of cooperatives in transforming rural livelihoods, stating: 'If cooperation fails, there will fail the best hope of rural India.'",
            "exp_ta": "விவசாயத்திற்கான ராயல் கமிஷன் (1928) கிராமப்புற வாழ்வாதாரத்தை மாற்றுவதில் கூட்டுறவின் ஈடுசெய்ய முடியாத பங்கை வலியுறுத்தி, 'கூட்டுறவு தோற்றுப்போனால், கிராமப்புற இந்தியாவின் மிகச்சிறந்த நம்பிக்கையே தோற்றுப்போகும்' எனக் குறிப்பிட்டது.",
            "why_a_en": "Correct. Famous verbatim quote from the 1928 report.",
            "why_a_ta": "சரி. 1928 அறிக்கையின் புகழ்பெற்ற வரிகள்.",
            "why_b_en": "Incorrect. Commission strongly affirmed cooperatives, did not call them incompatible.",
            "why_b_ta": "தவறு. ஆணையம் கூட்டுறவை ஆதரித்தது.",
            "why_c_en": "Incorrect. Foreign banks were never recommended for rural credit.",
            "why_c_ta": "தவறு. வெளிநாட்டு வங்கிகள் பரிந்துரைக்கப்படவில்லை.",
            "why_d_en": "Incorrect. Abolition was never contemplated.",
            "why_d_ta": "தவறு. ஒழிப்பது ஒருபோதும் பரிந்துரைக்கப்படவில்லை.",
            "tip_en": "Linlithgow later served as Viceroy of India from 1936 to 1943.",
            "tip_ta": "லின்லித்கோ பின்னர் 1936 முதல் 1943 வரை இந்தியாவின் வைஸ்ராயாகப் பணியாற்றினார்.",
            "fact_en": "The 1928 Commission also recommended establishment of the Imperial (now Indian) Council of Agricultural Research (ICAR).",
            "fact_ta": "1928 ஆணையமே இந்திய வேளாண் ஆராய்ச்சிக் குழுமத்தை (ICAR) நிறுவவும் பரிந்துரைத்தது."
        },

        # 25. Mutually Aided Cooperative Societies Act (MACS Act)
        {
            "subtopic": "State Cooperative Innovations",
            "stem_en": "Which State in India pioneered the 'Mutually Aided Co-operative Societies Act' (MACS Act) in 1995 to enable cooperatives with zero government shareholding to function entirely free from state bureaucratic control?",
            "stem_ta": "அரசுப் பங்கு மூலதனம் இல்லாத கூட்டுறவு சங்கங்கள் அரசின் அதிகாரத்துவக் கட்டுப்பாட்டிலிருந்து முற்றிலும் விடுபட்டுச் செயல்பட 1995-ல் 'பரஸ்பர உதவி கூட்டுறவு சங்கங்கள் சட்டத்தை' (MACS Act) முதன்முதலில் இயற்றிய இந்திய மாநிலம் எது?",
            "options": [
                ("Andhra Pradesh", "ஆந்திரப் பிரதேசம்"),
                ("Tamil Nadu", "தமிழ்நாடு"),
                ("West Bengal", "மேற்கு வங்காளம்"),
                ("Uttar Pradesh", "உத்தரப் பிரதேசம்")
            ],
            "correct_key": "A",
            "exp_en": "Andhra Pradesh enacted the historic Andhra Pradesh Mutually Aided Co-operative Societies Act (AP MACS Act, 1995) based on the Brahm Perkash Model Act, creating a parallel cooperative framework where societies accepting no government aid enjoyed complete self-governance.",
            "exp_ta": "பிரம்ம பிரகாஷ் மாதிரி சட்டத்தின் அடிப்படையில் ஆந்திரப் பிரதேசம் வரலாற்றுச் சிறப்புமிக்க MACS சட்டம் 1995-ஐ இயற்றியது; இது அரசிடமிருந்து நிதி உதவி பெறாத சங்கங்களுக்கு முழுமையான சுயாட்சி அதிகாரங்களை வழங்கியது.",
            "why_a_en": "Correct. Andhra Pradesh was the first state to pass the MACS Act in 1995.",
            "why_a_ta": "சரி. 1995-ல் MACS சட்டத்தை இயற்றிய முதல் மாநிலம் ஆந்திரப் பிரதேசம்.",
            "why_b_en": "Incorrect. Tamil Nadu maintains a unified Act (TN Act 1983).",
            "why_b_ta": "தவறு. தமிழ்நாடு 1983 சட்டத்தைக் கொண்டுள்ளது.",
            "why_c_en": "Incorrect. West Bengal enacted a parallel law later.",
            "why_c_ta": "தவறு. மேற்கு வங்கம் பின்னர் சட்டத்தை இயற்றியது.",
            "why_d_en": "Incorrect. UP did not pioneer the MACS law.",
            "why_d_ta": "தவறு. உத்தரப் பிரதேசம் முன்னோடி அல்ல.",
            "tip_en": "MACS model: No government funds = No Registrar interference in elections, management, or audit.",
            "tip_ta": "MACS மாதிரி: அரசு நிதி இல்லை = தேர்தல், மேலாண்மை அல்லது தணிக்கையில் பதிவாளரின் தலையீடு இல்லை.",
            "fact_en": "Over 9 other States subsequently enacted parallel self-reliant cooperative laws inspired by Andhra Pradesh.",
            "fact_ta": "ஆந்திராவைப் பின்பற்றி 9-க்கும் மேற்பட்ட பிற மாநிலங்கள் பின்னர் இத்தகைய தன்னாட்சி சட்டங்களை இயற்றின."
        },

        # 26. Difference between Cooperative and Commercial Company
        {
            "subtopic": "Comparative Analysis",
            "stem_en": "Which of the following core features fundamentally distinguishes a Co-operative Society from a Joint Stock Commercial Company?",
            "stem_ta": "பின்வரும் எந்த முக்கிய அம்சம் ஒரு கூட்டுறவு சங்கத்தை ஒரு கூட்டுப் பங்கு வணிக நிறுவனத்திலிருந்து அடிப்படையில் வேறுபடுத்துகிறது?",
            "options": [
                ("Cooperative motive is 'Service and Mutual Assistance', whereas Company motive is 'Profit Maximization'", "கூட்டுறவின் நோக்கம் 'சேவை மற்றும் பரஸ்பர உதவி', ஆனால் நிறுவனத்தின் நோக்கம் 'லாபத்தை அதிகரிப்பது'"),
                ("A cooperative society cannot earn any surplus at all", "ஒரு கூட்டுறவு சங்கத்தால் எவ்வித உபரியையும் ஈட்டவே முடியாது"),
                ("A joint stock company gives every shareholder only one vote regardless of shares", "வணிக நிறுவனம் அனைத்துப் பங்குதாரர்களுக்கும் பங்குகளின் எண்ணிக்கையைப் பொருட்படுத்தாமல் ஒரு வாக்கை மட்டுமே அளிக்கிறது"),
                ("Cooperative membership is strictly hereditary and closed to the public", "கூட்டுறவு உறுப்பினர் சேர்க்கை பரம்பரையானது மற்றும் பொதுமக்களுக்கு மூடப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "The primary objective of a co-operative society is mutual self-help and service to members with limited return on capital, whereas a commercial company's primary driving objective is maximizing shareholder wealth and profit.",
            "exp_ta": "ஒரு கூட்டுறவு சங்கத்தின் முதன்மை நோக்கம் பரஸ்பர சுயஉதவி மற்றும் உறுப்பினர்களுக்கான சேவையாகும் (மூலதனத்திற்கு வரம்புக்குட்பட்ட வட்டி); ஆனால் ஒரு வணிக நிறுவனத்தின் முதன்மை நோக்கம் பங்குதாரர்களின் செல்வத்தையும் லாபத்தையும் அதிகரிப்பதாகும்.",
            "why_a_en": "Correct. Primary motive difference: Service/Mutual aid vs Profit maximization.",
            "why_a_ta": "சரி. முதன்மை நோக்கம்: சேவை/பரஸ்பர உதவி vs லாபத்தை அதிகரிப்பது.",
            "why_b_en": "Incorrect. Cooperatives can and do earn surplus to build reserves and pay patronage bonus.",
            "why_b_ta": "தவறு. கூட்டுறவுகள் சேம நிதியை உருவாக்க உபரி ஈட்ட முடியும்.",
            "why_c_en": "Incorrect. Companies operate on 'One Share, One Vote'.",
            "why_c_ta": "தவறு. நிறுவனங்கள் 'ஒரு பங்கு, ஒரு வாக்கு' அடிப்படையில் செயல்படுகின்றன.",
            "why_d_en": "Incorrect. Open and voluntary membership is a core cooperative principle.",
            "why_d_ta": "தவறு. திறந்த மற்றும் தன்னார்வ உறுப்பினர் சேர்க்கை கூட்டுறவின் அடிப்படைக் கொள்கை.",
            "tip_en": "Remember: In cooperatives, capital is an instrument of service; in companies, capital is the master.",
            "tip_ta": "நினைவில் கொள்க: கூட்டுறவில் மூலதனம் சேவைக்கான கருவி; நிறுவனத்தில் மூலதனமே எஜமானன்.",
            "fact_en": "Surplus in a cooperative is distributed as 'patronage dividend' based on business transacted by the member.",
            "fact_ta": "கூட்டுறவில் உபரி என்பது உறுப்பினர் சங்கத்துடன் செய்த வணிகத்தின் அடிப்படையில் 'பயன்பாட்டு ஈவுத்தொகையாக' பகிரப்படுகிறது."
        },

        # 27. Cooperatives vs Self-Help Groups (SHGs)
        {
            "subtopic": "Comparative Analysis",
            "stem_en": "In what crucial structural and legal aspect does a registered Co-operative Society differ from an informal Self-Help Group (SHG)?",
            "stem_ta": "எந்த முக்கியமான கட்டமைப்பு மற்றும் சட்ட அம்சத்தில் ஒரு பதிவுசெய்யப்பட்ட கூட்டுறவு சங்கம் ஒரு முறைசாரா சுயஉதவிக் குழுவிலிருந்து (SHG) வேறுபடுகிறது?",
            "options": [
                ("A Co-operative Society is a registered body corporate with perpetual succession and common seal, whereas an SHG is typically an informal unregistered association", "கூட்டுறவு சங்கம் என்பது நிரந்தரத் தொடர்ச்சி மற்றும் பொது முத்திரையைக் கொண்ட சட்டப்பூர்வ அமைப்பாகும், ஆனால் SHG என்பது பொதுவாக ஒரு முறைசாரா பதிவு செய்யப்படாத அமைப்பாகும்"),
                ("An SHG has a maximum limit of 21 directors under Article 243ZJ", "ஒரு SHG சரத்து 243ZJ-ன் கீழ் அதிகபட்சம் 21 இயக்குநர்களைக் கொண்டுள்ளது"),
                ("A Co-operative Society cannot borrow from banks", "கூட்டுறவு சங்கத்தால் வங்கிகளிலிருந்து கடன் பெற முடியாது"),
                ("An SHG requires a statutory government audit by a Chartered Accountant", "ஒரு SHG பட்டயக் கணக்காளரால் சட்டப்பூர்வ அரசுத் தணிக்கை செய்யப்பட வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "A registered cooperative society is a distinct legal entity (juristic person) created under statute with perpetual succession, common seal, and power to hold property and sue or be sued. In contrast, an SHG is an informal group (usually 10-20 members) governed by mutual trust and linked to banks via the SHG-Bank Linkage Programme.",
            "exp_ta": "ஒரு பதிவுசெய்யப்பட்ட கூட்டுறவு சங்கம் என்பது சட்டத்தின் கீழ் உருவாக்கப்பட்ட நிரந்தரத் தொடர்ச்சி, பொது முத்திரை மற்றும் சொத்துக்களை வைத்திருக்கவும் வழக்குத் தொடரவும் அதிகாரம் கொண்ட தனி சட்டப்பூர்வ அமைப்பாகும் (body corporate). ஆனால் SHG என்பது பரஸ்பர நம்பிக்கையால் வழிநடத்தப்படும் முறைசாரா அமைப்பாகும் (10-20 உறுப்பினர்கள்).",
            "why_a_en": "Correct. Body corporate status distinguishes cooperatives from informal SHGs.",
            "why_a_ta": "சரி. சட்டப்பூர்வ அந்தஸ்து (Body corporate) கூட்டுறவை முறைசாரா SHG-யிலிருந்து வேறுபடுத்துகிறது.",
            "why_b_en": "Incorrect. Article 243ZJ applies exclusively to cooperatives, not SHGs.",
            "why_b_ta": "தவறு. சரத்து 243ZJ கூட்டுறவுகளுக்கு மட்டுமே பொருந்தும், SHG-க்கு அல்ல.",
            "why_c_en": "Incorrect. Cooperatives borrow extensively from DCCBs and NABARD.",
            "why_c_ta": "தவறு. கூட்டுறவுகள் வங்கிகளிலிருந்து கடன் பெறுகின்றன.",
            "why_d_en": "Incorrect. SHGs maintain simple internal registers, not statutory CA audits.",
            "why_d_ta": "தவறு. SHG-களுக்கு சட்டப்பூர்வ CA தணிக்கை தேவையில்லை.",
            "tip_en": "PACS = Formal registered cooperative; SHG = Informal village group (NABARD SHG-Bank Linkage model).",
            "tip_ta": "PACS = முறையான பதிவுபெற்ற கூட்டுறவு; SHG = முறைசாரா கிராமக் குழு (நபார்டு வங்கி இணைப்பு மாதிரி).",
            "fact_en": "SHGs can federate into Primary Level Federations (PLFs) and Village Poverty Reduction Committees (VPRCs).",
            "fact_ta": "சுயஉதவிக் குழுக்கள் கிராம அளவில் கூட்டமைப்புகளாக ஒருங்கிணைக்கப்படலாம்."
        },

        # 28. Consumer Cooperatives in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "In Tamil Nadu, which cooperative institutional network runs the majority of Fair Price Shops (FPS) under the Public Distribution System (PDS)?",
            "stem_ta": "தமிழ்நாட்டில், பொது விநியோகத் திட்டத்தின் (PDS) கீழ் பெரும்பாலான நியாயவிலைக் கடைகளை (FPS) நடத்தும் கூட்டுறவு நிறுவனக் கட்டமைப்பு எது?",
            "options": [
                ("Primary Agricultural Cooperative Credit Societies and Consumer Cooperative Wholesale Stores", "தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கங்கள் மற்றும் நுகர்வோர் கூட்டுறவு மொத்த விற்பனைப் பண்டகசாலைகள்"),
                ("Private multinational supermarket chains", "தனியார் பன்னாட்டு பல்பொருள் அங்காடி சங்கிலிகள்"),
                ("National Agricultural Cooperative Marketing Federation (NAFED) directly", "நாஃபெட் (NAFED) நிறுவனம் நேரடியாக"),
                ("Village Panchayats under their own administrative budget", "கிராம ஊராட்சிகள் தங்கள் சொந்த நிர்வாக பட்ஜெட்டில்")
            ],
            "correct_key": "A",
            "exp_en": "In Tamil Nadu, over 93% of the 35,000+ Fair Price Shops under the universal PDS are operated by cooperative societies (primarily PACS and Consumer Cooperative Wholesale Stores like TUCS and Chinthamani).",
            "exp_ta": "தமிழ்நாட்டில், உலகளாவிய பொது விநியோகத் திட்டத்தின் கீழ் உள்ள 35,000-க்கும் மேற்பட்ட நியாயவிலைக் கடைகளில் 93%-க்கும் அதிகமானவை கூட்டுறவு சங்கங்களால் (முக்கியமாக PACS மற்றும் சிந்தாமணி, TUCS போன்ற நுகர்வோர் கூட்டுறவு மொத்த விற்பனை பண்டகசாலைகள்) நடத்தப்படுகின்றன.",
            "why_a_en": "Correct. Cooperatives run over 93% of PDS fair price shops in Tamil Nadu.",
            "why_a_ta": "சரி. தமிழ்நாட்டில் 93%-க்கும் அதிகமான ரேஷன் கடைகளைக் கூட்டுறவுகளே நடத்துகின்றன.",
            "why_b_en": "Incorrect. Private retail chains are not entrusted with universal PDS in TN.",
            "why_b_ta": "தவறு. தனியார் நிறுவனங்களிடம் ரேஷன் கடைகள் ஒப்படைக்கப்படவில்லை.",
            "why_c_en": "Incorrect. NAFED operates at national level for procurement, not local PDS shops.",
            "why_c_ta": "தவறு. நாஃபெட் தேசிய அளவிலான கொள்முதல் அமைப்பு.",
            "why_d_en": "Incorrect. Panchayats do not run the PDS shops; cooperative societies do.",
            "why_d_ta": "தவறு. ஊராட்சிகள் கடைகளை நடத்துவதில்லை, கூட்டுறவுகளே நடத்துகின்றன.",
            "tip_en": "Tamil Nadu operates a 'Universal PDS' (providing subsidized/free rice to all cardholders), unique in India.",
            "tip_ta": "தமிழ்நாடு இந்தியாவில் தனித்துவமான 'உலகளாவிய பொது விநியோகத் திட்டத்தை' (அனைவருக்கும் இலவச அரிசி) செயல்படுத்துகிறது.",
            "fact_en": "This model ensures food security reaching the remotest hamlets via village cooperatives.",
            "fact_ta": "இம்மாதிரி கிராமக் கூட்டுறவுகள் மூலம் கடைக்கோடி கிராமங்களுக்கும் உணவுப் பாதுகாப்பை உறுதி செய்கிறது."
        },

        # 29. NAFED Functions
        {
            "subtopic": "National Cooperative Marketing",
            "stem_en": "What is the primary role of the National Agricultural Cooperative Marketing Federation of India Limited (NAFED) established in 1958?",
            "stem_ta": "1958-ல் நிறுவப்பட்ட இந்திய தேசிய வேளாண் கூட்டுறவு விற்பனைக் கூட்டமைப்பின் (NAFED) முதன்மைப் பணி என்ன?",
            "options": [
                ("Procurement, marketing, and export of agricultural produce, pulses, and oilseeds, including Price Support Scheme (PSS) operations", "விலை ஆதரவுத் திட்டத்தின் (PSS) கீழ் பருப்பு வகைகள் மற்றும் எண்ணெய் வித்துக்கள் உள்ளிட்ட விவசாயப் பொருட்களைக் கொள்முதல் செய்தல், சந்தைப்படுத்துதல் மற்றும் ஏற்றுமதி செய்தல்"),
                ("Regulating commercial banks in urban areas", "நகர்ப்புறங்களில் உள்ள வணிக வங்கிகளை ஒழுங்குபடுத்துவது"),
                ("Manufacture of railway rolling stock", "ரயில் பெட்டிகள் தயாரிப்பது"),
                ("Conducting election to State Legislative Assemblies", "மாநில சட்டமன்றங்களுக்கான தேர்தலை நடத்துவது")
            ],
            "correct_key": "A",
            "exp_en": "NAFED was established on 2nd October 1958 under the Multi-State Co-operative Societies Act to promote cooperative marketing of agricultural produce. It functions as the Central Nodal Agency for procurement of pulses and oilseeds under the Price Support Scheme (PSS) at MSP.",
            "exp_ta": "விவசாயப் பொருட்களின் கூட்டுறவு சந்தைப்படுத்தலை ஊக்குவிப்பதற்காக 1958 அக்டோபர் 2 அன்று MSCS சட்டத்தின் கீழ் NAFED தொடங்கப்பட்டது. இது குறைந்தபட்ச ஆதரவு விலையில் (MSP) பருப்பு வகைகள் மற்றும் எண்ணெய் வித்துக்களைக் கொள்முதல் செய்வதற்கான மத்திய நோடல் முகமையாகச் செயல்படுகிறது.",
            "why_a_en": "Correct. NAFED is the central nodal agency for procurement of pulses and oilseeds at MSP.",
            "why_a_ta": "சரி. NAFED என்பது பருப்பு மற்றும் எண்ணெய் வித்துக்களின் கொள்முதலுக்கான மத்திய அரசு முகமையாகும்.",
            "why_b_en": "Incorrect. RBI regulates banks.",
            "why_b_ta": "தவறு. RBI வங்கிகளை ஒழுங்குபடுத்துகிறது.",
            "why_c_en": "Incorrect. Railway stock is manufactured by ICF/RCF.",
            "why_c_ta": "தவறு. ரயில் பெட்டிகள் ICF போன்றவற்றால் தயாரிக்கப்படுகின்றன.",
            "why_d_en": "Incorrect. Assembly elections are conducted by ECI under Article 324.",
            "why_d_ta": "தவறு. சட்டமன்றத் தேர்தலை இந்தியத் தேர்தல் ஆணையம் நடத்துகிறது.",
            "tip_en": "NAFED maintains national buffer stocks of pulses and onion under the Price Stabilization Fund (PSF).",
            "tip_ta": "NAFED விலை நிலைப்படுத்தல் நிதியின் (PSF) கீழ் பருப்பு மற்றும் வெங்காயத்தின் தேசிய இருப்புக்களைப் பராமரிக்கிறது.",
            "fact_en": "NAFED is an apex national multi-state marketing cooperative registered under MSCS Act.",
            "fact_ta": "NAFED என்பது MSCS சட்டத்தின் கீழ் பதிவுசெய்யப்பட்ட உச்ச தேசிய பல்மாநில விற்பனைக் கூட்டுறவாகும்."
        },

        # 30. TRIFED Functions
        {
            "subtopic": "National Cooperative Marketing",
            "stem_en": "The Tribal Cooperative Marketing Development Federation of India (TRIFED), established in 1987, functions primarily under the administrative control of which Union Ministry?",
            "stem_ta": "1987-ல் நிறுவப்பட்ட இந்திய பழங்குடியினர் கூட்டுறவு சந்தைப்படுத்தல் மேம்பாட்டுக் கூட்டமைப்பு (TRIFED) முதன்மையாக எந்த மத்திய அமைச்சகத்தின் நிர்வாகக் கட்டுப்பாட்டின் கீழ் செயல்படுகிறது?",
            "options": [
                ("Ministry of Tribal Affairs", "பழங்குடியினர் விவகாரங்கள் அமைச்சகம்"),
                ("Ministry of Finance", "நிதி அமைச்சகம்"),
                ("Ministry of Cooperation", "கூட்டுறவு அமைச்சகம்"),
                ("Ministry of Heavy Industries", "கனரகத் தொழில்கள் அமைச்சகம்")
            ],
            "correct_key": "A",
            "exp_en": "TRIFED was established in August 1987 under the Multi-State Co-operative Societies Act, 1984 as a national-level apex body functioning under the administrative control of the Ministry of Tribal Affairs to market Minor Forest Produce (MFP) and tribal handicrafts (Tribes India).",
            "exp_ta": "சிறு வன உற்பத்திப் பொருட்கள் (MFP) மற்றும் பழங்குடியினர் கைவினைப் பொருட்களை (Tribes India) சந்தைப்படுத்துவதற்காக பழங்குடியினர் விவகாரங்கள் அமைச்சகத்தின் நிர்வாகக் கட்டுப்பாட்டின் கீழ் 1987 ஆகஸ்டில் TRIFED தேசிய அளவிலான உச்ச அமைப்பாக நிறுவப்பட்டது.",
            "why_a_en": "Correct. TRIFED operates under the Ministry of Tribal Affairs.",
            "why_a_ta": "சரி. TRIFED பழங்குடியினர் விவகாரங்கள் அமைச்சகத்தின் கீழ் செயல்படுகிறது.",
            "why_b_en": "Incorrect. Ministry of Finance manages fiscal and budget policy.",
            "why_b_ta": "தவறு. நிதி அமைச்சகம் பட்ஜெட் கொள்கையை நிர்வகிக்கிறது.",
            "why_c_en": "Incorrect. Though a cooperative, TRIFED is administratively under Ministry of Tribal Affairs.",
            "why_c_ta": "தவறு. இது கூட்டுறவாக இருந்தாலும், பழங்குடியினர் விவகாரங்கள் அமைச்சகத்தின் கீழ் வருகிறது.",
            "why_d_en": "Incorrect. Heavy industries are unrelated to tribal forest products.",
            "why_d_ta": "தவறு. கனரகத் தொழில்கள் தொடர்பற்றவை.",
            "tip_en": "TRIFED implements the 'Pradhan Mantri Van Dhan Yojana' (PMVDY) establishing Van Dhan Vikas Kendras for tribal SHGs.",
            "tip_ta": "TRIFED பழங்குடியினருக்காக 'பிரதம மந்திரி வன்தன் யோஜனா' (PMVDY) திட்டத்தை செயல்படுத்துகிறது.",
            "fact_en": "TRIFED markets products through its retail chain 'Tribes India'.",
            "fact_ta": "TRIFED 'டிரைப்ஸ் இந்தியா' (Tribes India) என்ற விற்பனை நிலையங்கள் மூலம் பொருட்களை விற்கிறது."
        },

        # 31. KRIBHCO Cooperative
        {
            "subtopic": "National Cooperative Landmarks",
            "stem_en": "What is the primary industrial manufacturing activity of Krishak Bharati Cooperative Limited (KRIBHCO)?",
            "stem_ta": "கிரிஷக் பாரதி கூட்டுறவு நிறுவனத்தின் (KRIBHCO) முதன்மைத் தொழில் உற்பத்தி நடவடிக்கை என்ன?",
            "options": [
                ("Production of chemical and bio-fertilizers (Urea, Ammonia)", "இரசாயன மற்றும் உயிர் உரங்கள் உற்பத்தி (யூரியா, அம்மோனியா)"),
                ("Commercial civil aviation", "வணிக ரீதியான சிவில் விமானப் போக்குவரத்து"),
                ("Petroleum crude refining", "கச்சா பெட்ரோலிய சுத்திகரிப்பு"),
                ("Telecommunications hardware", "தொலைத்தொடர்பு வன்பொருள் தயாரிப்பு")
            ],
            "correct_key": "A",
            "exp_en": "Krishak Bharati Cooperative Limited (KRIBHCO) was incorporated in 1980 under the Multi-State Cooperative Societies Act as an apex national cooperative society for the manufacturing and distribution of fertilizer, bio-fertilizers, and certified seeds.",
            "exp_ta": "கிரிஷக் பாரதி கூட்டுறவு நிறுவனம் (KRIBHCO) உரங்கள், உயிர் உரங்கள் மற்றும் சான்றளிக்கப்பட்ட விதைகளை உற்பத்தி செய்து விநியோகிப்பதற்காக 1980-ல் MSCS சட்டத்தின் கீழ் ஒரு தேசிய தலைமைக் கூட்டுறவு சங்கமாக நிறுவப்பட்டது.",
            "why_a_en": "Correct. Fertilizer and agricultural input manufacturing is KRIBHCO's core business.",
            "why_a_ta": "சரி. உர உற்பத்தி மற்றும் விநியோகமே கிரிப்கோவின் முதன்மைப் பணியாகும்.",
            "why_b_en": "Incorrect. Aviation is unrelated.",
            "why_b_ta": "தவறு. விமானப் போக்குவரத்து தொடர்பற்றது.",
            "why_c_en": "Incorrect. Petroleum refining is done by IOCL, BPCL, etc.",
            "why_c_ta": "தவறு. பெட்ரோலிய சுத்திகரிப்பு IOCL போன்ற நிறுவனங்களால் செய்யப்படுகிறது.",
            "why_d_en": "Incorrect. Telecommunications is handled by telecom companies.",
            "why_d_ta": "தவறு. தொலைத்தொடர்பு தொடர்பற்றது.",
            "tip_en": "KRIBHCO operates its massive flagship urea manufacturing plant at Hazira in Gujarat.",
            "tip_ta": "KRIBHCO தனது மிகப்பெரிய யூரியா உற்பத்தி ஆலையை குஜராத்தில் உள்ள ஹசீராவில் இயக்குகிறது.",
            "fact_en": "KRIBHCO is a multi-state cooperative owned by thousands of primary agricultural cooperatives across India.",
            "fact_ta": "KRIBHCO என்பது இந்தியா முழுவதிலும் உள்ள ஆயிரக்கணக்கான வேளாண் கூட்டுறவுகளுக்குச் சொந்தமான பல்மாநில அமைப்பாகும்."
        },

        # 32. Urban Cooperative Banks (UCBs) vs Commercial Banks
        {
            "subtopic": "Banking Cooperatives",
            "stem_en": "Which of the following is a structural feature that distinguishes Urban Co-operative Banks (UCBs) from Scheduled Commercial Banks (SCBs)?",
            "stem_ta": "பின்வருவனவற்றில் நகர்ப்புறக் கூட்டுறவு வங்கிகளை (UCBs) திட்டமிடப்பட்ட வணிக வங்கிகளிலிருந்து (SCBs) வேறுபடுத்தும் கட்டமைப்பு அம்சம் எது?",
            "options": [
                ("UCBs are organized on a cooperative principle of democratic member ownership, whereas SCBs are investor-owned joint stock companies", "UCB-கள் ஜனநாயக உறுப்பினர் உரிமையின் கூட்டுறவுக் கொள்கையின் அடிப்படையில் அமைக்கப்பட்டவை, ஆனால் SCB-கள் முதலீட்டாளர்களுக்குச் சொந்தமான கூட்டுப் பங்கு நிறுவனங்கள்"),
                ("UCB deposits are not covered by DICGC insurance", "UCB வைப்புத்தொகைகள் DICGC காப்பீட்டின் கீழ் பாதுகாக்கப்படுவதில்லை"),
                ("UCBs cannot accept demand deposits from citizens", "UCB-கள் பொதுமக்களிடமிருந்து கேட்பு வைப்புகளை (Savings/Current) ஏற்க முடியாது"),
                ("UCBs are completely exempt from Cash Reserve Ratio (CRR) norms", "UCB-களுக்கு ரொக்க இருப்பு விகித (CRR) விதிமுறைகளிலிருந்து முழு விலக்கு அளிக்கப்பட்டுள்ளது")
            ],
            "correct_key": "A",
            "exp_en": "UCBs are primary cooperative banks owned by borrower and depositor members following 'one member, one vote', whereas commercial banks are joint-stock corporations driven by shareholder returns. Like commercial banks, UCB deposits ARE insured by DICGC up to Rs. 5 lakh.",
            "exp_ta": "UCB-கள் 'ஒரு உறுப்பினர், ஒரு வாக்கு' என்ற கொள்கையைப் பின்பற்றும் கடன் வாங்குவோர் மற்றும் வைப்பீட்டாளர் உறுப்பினர்களுக்குச் சொந்தமான கூட்டுறவு வங்கிகளாகும்; ஆனால் வணிக வங்கிகள் பங்குதாரர்களின் லாபத்தால் இயக்கப்படும் நிறுவனங்களாகும். வணிக வங்கிகளைப் போலவே, UCB வைப்புத்தொகைகளும் DICGC மூலம் ரூ. 5 லட்சம் வரை காப்பீடு செய்யப்படுகின்றன.",
            "why_a_en": "Correct. Democratic member ownership vs shareholder-driven capitalism.",
            "why_a_ta": "சரி. ஜனநாயக உறுப்பினர் உரிமை vs பங்குதாரர் தலைமையிலான வணிக அமைப்பு.",
            "why_b_en": "Incorrect. UCB deposits ARE insured by DICGC up to Rs. 5 lakh.",
            "why_b_ta": "தவறு. UCB வைப்புகளும் DICGC மூலம் ரூ. 5 லட்சம் வரை காப்பீடு செய்யப்படுகின்றன.",
            "why_c_en": "Incorrect. UCBs accept savings and current demand deposits.",
            "why_c_ta": "தவறு. UCB-கள் சேமிப்பு மற்றும் நடப்புக் கணக்கு வைப்புகளை ஏற்கின்றன.",
            "why_d_en": "Incorrect. UCBs must maintain CRR and SLR as mandated by RBI.",
            "why_d_ta": "தவறு. UCB-கள் RBI விதித்த CRR மற்றும் SLR-ஐப் பராமரிக்க வேண்டும்.",
            "tip_en": "DICGC insurance protects depositor money in all eligible cooperative banks up to Rs. 5,00,000.",
            "tip_ta": "DICGC காப்பீடு அனைத்து தகுதியுள்ள கூட்டுறவு வங்கிகளிலும் வைப்பீட்டாளர் பணத்தை ரூ. 5,00,000 வரை பாதுகாக்கிறது.",
            "fact_en": "There are over 1,500 Urban Cooperative Banks across India.",
            "fact_ta": "இந்தியா முழுவதும் 1,500-க்கும் மேற்பட்ட நகர்ப்புறக் கூட்டுறவு வங்கிகள் உள்ளன."
        },

        # 33. Doctrine of Severability in Rajendra N. Shah
        {
            "subtopic": "Judicial Pronouncements - Landmark Ruling",
            "stem_en": "In Union of India v. Rajendra N. Shah (2021), what legal doctrine was applied by the Supreme Court majority to uphold Part IX-B for Multi-State Co-operative Societies while striking it down for State Co-operatives?",
            "stem_ta": "மத்திய அரசு v. ராஜேந்திர என். ஷா (2021) வழக்கில், உச்ச நீதிமன்ற பெரும்பான்மை அமர்வு மாநிலக் கூட்டுறவுகளுக்கு பகுதி IX-B-ஐ ரத்து செய்த அதே வேளையில், பல்மாநிலக் கூட்டுறவுகளுக்கு அதை உறுதி செய்ய எந்த சட்டக் கோட்பாட்டைப் பயன்படுத்தியது?",
            "options": [
                ("Doctrine of Severability", "பிரித்தெடுப்புக் கோட்பாடு (Doctrine of Severability)"),
                ("Doctrine of Eclipse", "மறைப்புக் கோட்பாடு (Doctrine of Eclipse)"),
                ("Doctrine of Pith and Substance", "அடிநாதக் கோட்பாடு (Doctrine of Pith and Substance)"),
                ("Doctrine of Colourable Legislation", "மறைமுகச் சட்டமியற்றல் கோட்பாடு (Doctrine of Colourable Legislation)")
            ],
            "correct_key": "A",
            "exp_en": "The Supreme Court applied the Doctrine of Severability (severing the unconstitutional portions affecting State cooperatives under List II Entry 32 from the constitutional portions governing Multi-State cooperatives under List I Entry 44 and Union Territories).",
            "exp_ta": "உச்ச நீதிமன்றம் பிரித்தெடுப்புக் கோட்பாட்டைப் பயன்படுத்தியது (பட்டியல் II பதிவு 32-ன் கீழ் மாநில கூட்டுறவுகளைப் பாதிக்கும் அரசியலமைப்பிற்கு முரணான பகுதிகளைப் பிரித்து நீக்கிவிட்டு, பட்டியல் I பதிவு 44-ன் கீழ் பல்மாநில கூட்டுறவுகள் மற்றும் யூனியன் பிரதேசங்களை நிர்வகிக்கும் பகுதிகளைத் தக்கவைத்தது).",
            "why_a_en": "Correct. Doctrine of Severability saved Part IX-B for Multi-State cooperatives.",
            "why_a_ta": "சரி. பிரித்தெடுப்புக் கோட்பாடே பல்மாநில கூட்டுறவுகளுக்கு பகுதி IX-B-ஐக் காப்பாற்றியது.",
            "why_b_en": "Incorrect. Doctrine of Eclipse deals with pre-constitutional laws overshadowed by fundamental rights.",
            "why_b_ta": "தவறு. மறைப்புக் கோட்பாடு அடிப்படை உரிமைகளால் மறைக்கப்படும் முந்தைய சட்டங்கள் பற்றியது.",
            "why_c_en": "Incorrect. Pith and Substance tests legislative competence over subject matter overlaps.",
            "why_c_ta": "தவறு. அடிநாதக் கோட்பாடு சட்டமன்ற அதிகார வரம்பு மேலெழுதலை ஆராய்கிறது.",
            "why_d_en": "Incorrect. Colourable Legislation means doing indirectly what cannot be done directly.",
            "why_d_ta": "தவறு. மறைமுகச் சட்டமியற்றல் என்பது நேரடியாகச் செய்ய முடியாததை மறைமுகமாகச் செய்வது.",
            "tip_en": "Justice K.M. Joseph dissented on this point, arguing that Part IX-B was an indivisible legislative code that could not be severed.",
            "tip_ta": "நீதிபதி கே.எம். ஜோசப் இதில் மாறுபட்டு, பகுதி IX-B பிரிக்க முடியாத ஒன்று என வாதிட்டார்.",
            "fact_en": "Because of severability, Parliament did not need to enact a new constitutional amendment for multi-state cooperatives.",
            "fact_ta": "பிரித்தெடுப்புக் கோட்பாட்டினால், பல்மாநில கூட்டுறவுகளுக்கு நாடாளுமன்றம் புதிய அரசியலமைப்புத் திருத்தத்தை இயற்ற வேண்டிய அவசியமில்லாமல் போனது."
        },

        # 34. Article 368(2) Proviso Ratification Requirement
        {
            "subtopic": "Constitutional Amendment Procedure",
            "stem_en": "Why was the 97th Constitutional Amendment Act, 2011 held unconstitutional for State cooperatives in Union of India v. Rajendra N. Shah?",
            "stem_ta": "மத்திய அரசு v. ராஜேந்திர என். ஷா வழக்கில் 97வது அரசியலமைப்புத் திருத்தச் சட்டம், 2011 மாநிலக் கூட்டுறவுகளுக்கு அரசியலமைப்பிற்கு முரணானது என ஏன் அறிவிக்கப்பட்டது?",
            "options": [
                ("It directly curtailed State legislative powers over List II Entry 32 without being ratified by at least half of State Legislatures under Article 368(2) proviso", "சரத்து 368(2) வரம்பின் கீழ் குறைந்தபட்சம் பாதி மாநில சட்டமன்றங்களின் ஒப்புதலைப் பெறாமல், பட்டியல் II பதிவு 32-ன் மீதான மாநிலங்களின் சட்டமன்ற அதிகாரத்தை நேரடியாகக் குறைத்ததால்"),
                ("It was not passed by a special majority in Lok Sabha", "மக்களவையில் சிறப்புப் பெரும்பான்மையுடன் நிறைவேற்றப்படாததால்"),
                ("It was not signed by the President of India", "இந்தியக் குடியரசுத் தலைவரால் கையொப்பமிடப்படாததால்"),
                ("It violated the secular structure of the Preamble", "முகப்புரையின் மதச்சார்பற்ற கட்டமைப்பை மீறியதால்")
            ],
            "correct_key": "A",
            "exp_en": "Under the proviso to Article 368(2), any constitutional amendment that impacts Chapter V of Part VI, Chapter I of Part XI, or the legislative Lists in the Seventh Schedule MUST be ratified by the legislatures of not less than one-half of the States. The 97th Amendment failed to obtain state ratification.",
            "exp_ta": "சரத்து 368(2) வரம்பு நிபந்தனையின் கீழ், பகுதி VI அத்தியாயம் V, பகுதி XI அத்தியாயம் I அல்லது ஏழாவது அட்டவணையின் சட்டமன்றப் பட்டியல்களைப் பாதிக்கும் எந்தவொரு அரசியலமைப்புத் திருத்தமும் குறைந்தபட்சம் பாதி மாநில சட்டமன்றங்களால் அங்கீகரிக்கப்பட வேண்டும். 97வது திருத்தம் மாநில ஒப்புதலைப் பெறத் தவறியது.",
            "why_a_en": "Correct. Lack of mandatory Article 368(2) state ratification proved fatal for Part IX-B on State cooperatives.",
            "why_a_ta": "சரி. சரத்து 368(2) வரம்பின் கீழ் கட்டாய மாநில அங்கீகாரம் பெறாததே மாநில கூட்டுறவுகளுக்கான பகுதி IX-B செல்லாதாகக் காரணமாக அமைந்தது.",
            "why_b_en": "Incorrect. It was passed by special majority in both Houses of Parliament.",
            "why_b_ta": "தவறு. நாடாளுமன்றத்தின் இரு அவைகளிலும் சிறப்புப் பெரும்பான்மையுடன் நிறைவேற்றப்பட்டது.",
            "why_c_en": "Incorrect. It received Presidential assent in January 2012.",
            "why_c_ta": "தவறு. 2012 ஜனவரியில் குடியரசுத் தலைவர் ஒப்புதல் அளித்தார்.",
            "why_d_en": "Incorrect. Secularism was not an issue in this case.",
            "why_d_ta": "தவறு. மதச்சார்பின்மை இந்த வழக்கில் ஒரு பிரச்சினையாக இல்லை.",
            "tip_en": "Federal balance check: When Parliament amends provisions affecting exclusive State subjects, 50% State ratification is compulsory.",
            "tip_ta": "கூட்டாட்சி சமநிலை: மாநிலப் பாடங்களைப் பாதிக்கும் சட்டங்களை நாடாளுமன்றம் திருத்தும்போது, 50% மாநில சட்டமன்றங்களின் ஒப்புதல் கட்டாயமாகும்.",
            "fact_en": "Gujarat High Court was the first to strike down Part IX-B on this ground in 2013.",
            "fact_ta": "குஜராத் உயர் நீதிமன்றம் 2013-ல் முதன்முதலில் இதே அடிப்படையில் பகுதி IX-B-ஐ ரத்து செய்தது."
        },

        # 35. Article 243ZI Core Mandate
        {
            "subtopic": "Constitutional Provisions - Article 243ZI",
            "stem_en": "What fundamental principles of cooperation are explicitly mandated to be incorporated into state laws under Article 243ZI?",
            "stem_ta": "சரத்து 243ZI-ன் கீழ் மாநிலச் சட்டங்களில் வெளிப்படையாக இணைக்கப்பட வேண்டும் என்று கட்டாயமாக்கப்பட்ட கூட்டுறவின் அடிப்படைக் கொள்கைகள் எவை?",
            "options": [
                ("Voluntary formation, democratic member-control, member-economic participation, and autonomous functioning", "தன்னார்வ உருவாக்கம், ஜனநாயக உறுப்பினர் கட்டுப்பாடு, உறுப்பினர் பொருளாதாரப் பங்களிப்பு, மற்றும் தன்னாட்சி செயல்பாடு"),
                ("Compulsory state take-over, bureaucratic supervision, and price-fixing", "கட்டாய அரசு கையகப்படுத்தல், அதிகாரத்துவ மேற்பார்வை மற்றும் விலை நிர்ணயம்"),
                ("Absolute immunity from financial audit and civil litigation", "நிதித் தணிக்கை மற்றும் சிவில் வழக்குகளிலிருந்து முழுமையான விலக்கு"),
                ("Lifetime tenure for the founding president", "நிறுவனத் தலைவருக்கு வாழ்நாள் பதவிக்காலம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZI states: 'Subject to the provisions of this Part, the Legislature of a State may, by law, make provisions with respect to the incorporation, regulation and winding up of co-operative societies based on the principles of voluntary formation, democratic member-control, member-economic participation and autonomous functioning.'",
            "exp_ta": "சரத்து 243ZI கூறுகிறது: 'இந்த பகுதியின் விதிகளுக்கு உட்பட்டு, ஒரு மாநிலத்தின் சட்டமன்றமானது, தன்னார்வ உருவாக்கம், ஜனநாயக உறுப்பினர் கட்டுப்பாடு, உறுப்பினர் பொருளாதாரப் பங்களிப்பு மற்றும் தன்னாட்சி செயல்பாடு ஆகிய கொள்கைகளின் அடிப்படையில் கூட்டுறவு சங்கங்களை அமைத்தல், ஒழுங்குபடுத்துதல் மற்றும் கலைத்தல் தொடர்பான விதிகளைச் சட்டத்தின் மூலம் உருவாக்கலாம்.'",
            "why_a_en": "Correct. These 4 principles are verbatim enumerated in Article 243ZI.",
            "why_a_ta": "சரி. இந்த 4 கொள்கைகளும் சரத்து 243ZI-ல் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளன.",
            "why_b_en": "Incorrect. Bureaucratic take-over contradicts cooperative principles.",
            "why_b_ta": "தவறு. அதிகாரத்துவ ஆதிக்கம் கூட்டுறவுக் கொள்கைகளுக்கு எதிரானது.",
            "why_c_en": "Incorrect. Audit is constitutionally mandated under Article 243ZM.",
            "why_c_ta": "தவறு. தணிக்கை அரசியலமைப்பு ரீதியாகக் கட்டாயமாக்கப்பட்டுள்ளது.",
            "why_d_en": "Incorrect. 5-year fixed term is mandated under Article 243ZJ.",
            "why_d_ta": "தவறு. 5 ஆண்டு பதவிக்காலம் மட்டுமே அனுமதிக்கப்படுகிறது.",
            "tip_en": "Article 243ZI embeds international ICA principles into the constitutional text.",
            "tip_ta": "சரத்து 243ZI சர்வதேச ICA கொள்கைகளை இந்திய அரசியலமைப்பில் ஒருங்கிணைக்கிறது.",
            "fact_en": "Article 243ZI is the opening substantive article of Part IX-B.",
            "fact_ta": "சரத்து 243ZI என்பது பகுதி IX-B-ன் தொடக்க முக்கிய சரத்தாகும்."
        },

        # 36. Disqualification of Board Members
        {
            "subtopic": "Board Members Disqualification - Article 243ZQ",
            "stem_en": "Which of the following is a standard constitutional and statutory ground for disqualification of a person from being elected or continuing as a board member of a cooperative society?",
            "stem_ta": "பின்வருவனவற்றில் எது ஒரு நபர் கூட்டுறவு சங்க வாரிய உறுப்பினராகத் தேர்ந்தெடுக்கப்படுவதற்கோ அல்லது தொடர்வதற்கோ தகுதியிழப்பு செய்வதற்கான நிலையான அரசியலமைப்பு மற்றும் சட்டப்பூர்வ காரணமாகும்?",
            "options": [
                ("Defaulting on repayment of loan borrowed from the co-operative society for a prescribed period", "கூட்டுறவு சங்கத்தில் பெற்ற கடனை குறிப்பிட்ட காலத்திற்குத் திருப்பிச் செலுத்தாமல் தவறிழைத்தல் (டிஃபால்டர்)"),
                ("Holding an educational degree from an accredited university", "அங்கீகரிக்கப்பட்ட பல்கலைக்கழகத்தில் பட்டம் பெற்றிருப்பது"),
                ("Belonging to a Scheduled Caste or Scheduled Tribe category", "பட்டியல் சாதியினர் அல்லது பழங்குடியினர் பிரிவைச் சேர்ந்தவராக இருப்பது"),
                ("Exercising voting rights in the Annual General Meeting", "வருடாந்திர பொதுக்குழு கூட்டத்தில் வாக்குரிமையைப் பயன்படுத்துவது")
            ],
            "correct_key": "A",
            "exp_en": "Under state cooperative laws and model acts, a member who defaults on loan repayments, holds an office of profit, has been convicted of an offence involving moral turpitude, or has contractual conflicts of interest with the society is disqualified from the board.",
            "exp_ta": "மாநிலக் கூட்டுறவுச் சட்டங்களின் கீழ், கடனைத் திருப்பிச் செலுத்தத் தவறியவர் (டிஃபால்டர்), ஆதாயம் தரும் பதவி வகிப்பவர், குற்றவியல் வழக்கில் தண்டனை பெற்றவர் அல்லது சங்கத்துடன் வணிக ஒப்பந்த நலன் முரண்பாடு கொண்டவர் வாரிய உறுப்பினர் பதவிக்கு தகுதியற்றவர் ஆவார்.",
            "why_a_en": "Correct. Loan default is the most common statutory disqualification.",
            "why_a_ta": "சரி. கடன் தவறிழைப்பது மிகவும் பொதுவான சட்டப்பூர்வ தகுதியிழப்பாகும்.",
            "why_b_en": "Incorrect. Education is an asset, not a disqualification.",
            "why_b_ta": "தவறு. கல்வித் தகுதி தகுதியிழப்பு அல்ல.",
            "why_c_en": "Incorrect. Article 243ZJ explicitly reserves seats for SC/ST members.",
            "why_c_ta": "தவறு. SC/ST உறுப்பினர்களுக்கு சரத்து 243ZJ-ல் இடஒதுக்கீடு உள்ளது.",
            "why_d_en": "Incorrect. Voting in AGM is a fundamental member right.",
            "why_d_ta": "தவறு. AGM-ல் வாக்களிப்பது உறுப்பினரின் அடிப்படை உரிமை.",
            "tip_en": "A defaulter cannot stand for election to the board of directors in any cooperative in India.",
            "tip_ta": "இந்தியாவில் எந்தவொரு கூட்டுறவிலும் கடன் தவறிழைத்தவர் இயக்குநர் வாரியத் தேர்தலில் போட்டியிட முடியாது.",
            "fact_en": "This rule prevents borrowers from misusing board power to forgive or delay their own debts.",
            "fact_ta": "கடன் வாங்கியவர்கள் தங்கள் கடனைத் தள்ளுபடி செய்ய வாரிய அதிகாரத்தைத் தவறாகப் பயன்படுத்துவதை இது தடுக்கிறது."
        },

        # 37. Cooperative Sugar Factories in India
        {
            "subtopic": "Sectoral Cooperative Successes",
            "stem_en": "Which State in India pioneered the cooperative sugar factory movement starting with the Pravara Cooperative Sugar Factory established by Vithalrao Vikhe Patil in 1948?",
            "stem_ta": "1948-ல் வித்தல்ராவ் விக்கே பாட்டீலால் நிறுவப்பட்ட பிரவரா கூட்டுறவு சர்க்கரை ஆலையுடன் தொடங்கி, இந்தியாவில் கூட்டுறவு சர்க்கரை ஆலை இயக்கத்திற்கு முன்னோடியாகத் திகழ்ந்த மாநிலம் எது?",
            "options": [
                ("Maharashtra", "மகாராஷ்டிரா"),
                ("Tamil Nadu", "தமிழ்நாடு"),
                ("Bihar", "பீகார்"),
                ("Punjab", "பஞ்சாப்")
            ],
            "correct_key": "A",
            "exp_en": "Maharashtra pioneered cooperative agro-processing with the Pravara Cooperative Sugar Factory at Pravaranagar (Ahmednagar district) in 1948, led by Vithalrao Vikhe Patil and supported by economist Prof. D.R. Gadgil.",
            "exp_ta": "1948-ல் வித்தல்ராவ் விக்கே பாட்டீல் மற்றும் பொருளாதார அறிஞர் பேராசிரியர் D.R. காட்கில் ஆதரவுடன் அகமதுநகர் மாவட்டத்தின் பிரவராநகரில் அமைக்கப்பட்ட பிரவரா கூட்டுறவு சர்க்கரை ஆலையுடன் மகாராஷ்டிரா கூட்டுறவு வேளாண் பதப்படுத்துதலில் முன்னோடியாகத் திகழ்ந்தது.",
            "why_a_en": "Correct. Maharashtra is the heartland of cooperative sugar factories.",
            "why_a_ta": "சரி. மகாராஷ்டிரா கூட்டுறவு சர்க்கரை ஆலைகளின் தாயகமாகும்.",
            "why_b_en": "Incorrect. Tamil Nadu has cooperative sugar mills, but Maharashtra pioneered the movement.",
            "why_b_ta": "தவறு. தமிழ்நாட்டிலும் ஆலைகள் உள்ளன, ஆனால் மகாராஷ்டிரா முன்னோடியாகும்.",
            "why_c_en": "Incorrect. Bihar sugar industry was largely private and historically declined.",
            "why_c_ta": "தவறு. பீகாரில் தனியார் ஆலைகள் இருந்தன.",
            "why_d_en": "Incorrect. Punjab is known for wheat and dairy, not sugar cooperative movement.",
            "why_d_ta": "தவறு. பஞ்சாப் சர்க்கரை கூட்டுறவுக்குப் பெயர் பெற்றதல்ல.",
            "tip_en": "Prof. D.R. Gadgil later chaired the Planning Commission and formulated the famous Gadgil Formula for central assistance.",
            "tip_ta": "பேராசிரியர் D.R. காட்கில் பின்னர் திட்டக் குழுவின் தலைவராக இருந்து புகழ்பெற்ற காட்கில் சூத்திரத்தை உருவாக்கினார்.",
            "fact_en": "Sugar cooperatives transformed rural political economy and social capital in Western Maharashtra.",
            "fact_ta": "சர்க்கரை கூட்டுறவுகள் மேற்கு மகாராஷ்டிராவின் கிராமப்புற அரசியல் மற்றும் பொருளாதாரத்தை மாற்றியமைத்தன."
        },

        # 38. Operation Flood and Dairy Cooperatives
        {
            "subtopic": "Sectoral Cooperative Successes",
            "stem_en": "Launched in 1970, 'Operation Flood' (the White Revolution) replicated which cooperative institutional model across India?",
            "stem_ta": "1970-ல் தொடங்கப்பட்ட 'ஆபரேஷன் ஃபிளட்' (வெண்மைப் புரட்சி) இந்தியா முழுவதும் எந்தக் கூட்டுறவு நிறுவன மாதிரியைப் பிரதிபலித்தது?",
            "options": [
                ("The Anand (Amul) 3-Tier Dairy Cooperative Model", "ஆனந்த் (அமுல்) 3-அடுக்கு பால் கூட்டுறவு மாதிரி"),
                ("The British Rochdale Consumer Model", "பிரிட்டிஷ் ரோச்டேல் நுகர்வோர் மாதிரி"),
                ("The German Raiffeisen Credit Model", "ஜெர்மன் ரைஃபெய்சன் கடன் மாதிரி"),
                ("The Soviet Kolkhoz Collective Farming Model", "சோவியத் கோல்கோஸ் கூட்டுப் பண்ணை மாதிரி")
            ],
            "correct_key": "A",
            "exp_en": "Operation Flood, spearheaded by the National Dairy Development Board (NDDB) under Dr. Verghese Kurien, replicated the Anand pattern (Village Milk Cooperative -> District Cooperative Milk Union -> State Milk Federation) transforming India from a milk-deficient nation into the world's largest milk producer.",
            "exp_ta": "டாக்டர் வர்கீஸ் குரியன் தலைமையிலான தேசிய பால் மேம்பாட்டு வாரியம் (NDDB) வழிநடத்திய ஆபரேஷன் ஃபிளட், ஆனந்த் மாதிரியை (கிராமக் கூட்டுறவு -> மாவட்ட பால் ஒன்றியம் -> மாநிலக் கூட்டமைப்பு) நாடு முழுவதும் செயல்படுத்தி, இந்தியாவை உலகின் மிகப்பெரிய பால் உற்பத்தியாளராக மாற்றியது.",
            "why_a_en": "Correct. The Anand 3-tier model was the foundation of Operation Flood.",
            "why_a_ta": "சரி. ஆனந்த் 3-அடுக்கு மாதிரியே ஆபரேஷன் ஃபிளட்டின் அடித்தளமாகும்.",
            "why_b_en": "Incorrect. Rochdale was a consumer retail store model.",
            "why_b_ta": "தவறு. ரோச்டேல் நுகர்வோர் அங்காடி மாதிரி.",
            "why_c_en": "Incorrect. Raiffeisen is for rural credit.",
            "why_c_ta": "தவறு. ரைஃபெய்சன் ஊரகக் கடனுக்கானது.",
            "why_d_en": "Incorrect. Kolkhoz was state-coerced collective farming, not voluntary cooperation.",
            "why_d_ta": "தவறு. கோல்கோஸ் சோவியத் கட்டாய கூட்டுப் பண்ணை முறை.",
            "tip_en": "Operation Flood had three phases: Phase I (1970-80), Phase II (1981-85), and Phase III (1985-96).",
            "tip_ta": "ஆபரேஷன் ஃபிளட் மூன்று கட்டங்களைக் கொண்டது: கட்டம் I (1970-80), கட்டம் II (1981-85), கட்டம் III (1985-96).",
            "fact_en": "India is today the world's largest producer of milk, contributing over 24% of global milk production.",
            "fact_ta": "இந்தியா இன்று உலகின் மிகப்பெரிய பால் உற்பத்தியாளராகத் திகழ்கிறது, உலக உற்பத்தியில் 24%-க்கும் அதிகமாகப் பங்களிக்கிறது."
        },

        # 39. Co-option Rules and Disqualification
        {
            "subtopic": "Board Composition - Article 243ZJ",
            "stem_en": "Under Article 243ZJ, which of the following is TRUE regarding the functional status of co-opted members on the board of a co-operative society?",
            "stem_ta": "சரத்து 243ZJ-ன் கீழ், கூட்டுறவு சங்க வாரியத்தில் இணைத்துக் கொள்ளப்படும் உறுப்பினர்களின் பணி நிலை குறித்து பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("They cannot be elected as Chairperson or Vice-Chairperson of the co-operative society", "அவர்கள் கூட்டுறவு சங்கத்தின் தலைவர் அல்லது துணைத்தலைவராகத் தேர்ந்தெடுக்கப்பட முடியாது"),
                ("They are eligible to contest for the post of President of the society", "அவர்கள் சங்கத்தின் தலைவர் பதவிக்குப் போட்டியிடத் தகுதியுடையவர்கள்"),
                ("They have 2 votes each in every board resolution", "ஒவ்வொரு வாரியத் தீர்மானத்திலும் அவர்களுக்கு தலா 2 வாக்குகள் உண்டு"),
                ("They are counted to determine whether the 21 director ceiling has been breached", "21 இயக்குநர்கள் என்ற உச்சவரம்பு மீறப்பட்டுள்ளதா என்பதைத் தீர்மானிக்க அவர்கள் கணக்கிடப்படுகிறார்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZJ(1) explicitly mandates: 'Provided also that such co-opted members shall not have the right to vote in any election of the co-operative society in their capacity as such member or be eligible to be elected as office bearers of the board.'",
            "exp_ta": "சரத்து 243ZJ(1) வெளிப்படையாகக் கூறுகிறது: 'அத்தகைய இணை உறுப்பினர்கள் அந்தத் தகுதியில் கூட்டுறவு சங்கத்தின் எந்தவொரு தேர்தலிலும் வாக்களிக்கவோ அல்லது வாரியத்தின் நிர்வாகிகளாகத் தேர்ந்தெடுக்கப்படவோ உரிமை கொண்டிருக்க மாட்டார்கள்.'",
            "why_a_en": "Correct. Co-opted members cannot become Chairperson/Vice-Chairperson (office bearers).",
            "why_a_ta": "சரி. இணை உறுப்பினர்கள் தலைவர் அல்லது துணைத்தலைவர் ஆக முடியாது.",
            "why_b_en": "Incorrect. They are barred from standing for office-bearer posts.",
            "why_b_ta": "தவறு. அவர்கள் நிர்வாகி பதவிகளுக்குப் போட்டியிடத் தடை விதிக்கப்பட்டுள்ளது.",
            "why_c_en": "Incorrect. Nobody gets 2 votes; and co-opted members cannot vote in elections.",
            "why_c_ta": "தவறு. எவருக்கும் 2 வாக்குகள் வழங்கப்படுவதில்லை.",
            "why_d_en": "Incorrect. Co-opted members are over and above the 21-director ceiling.",
            "why_d_ta": "தவறு. அவர்கள் 21 இயக்குநர்கள் வரம்பிற்கு அப்பாற்பட்டவர்கள்.",
            "tip_en": "Office bearers = Chairperson, Vice-Chairperson, President, Vice-President, Managing Director.",
            "tip_ta": "நிர்வாகிகள் = தலைவர், துணைத்தலைவர், மேலாண்மை இயக்குநர்.",
            "fact_en": "Co-opted members are brought in purely for professional technical expertise (banking, audit, management).",
            "fact_ta": "இணை உறுப்பினர்கள் தொழில்முறை தொழில்நுட்ப நிபுணத்துவத்திற்காக மட்டுமே (வங்கி, மேலாண்மை) சேர்க்கப்படுகிறார்கள்."
        },

        # 40. Primary Co-operative Agriculture and Rural Development Banks (PCARDBs)
        {
            "subtopic": "Tamil Nadu Cooperative Credit",
            "stem_en": "In Tamil Nadu, Primary Co-operative Agriculture and Rural Development Banks (PCARDBs) specialize in providing which category of financial assistance to farmers?",
            "stem_ta": "தமிழ்நாட்டில், தொடக்கக் கூட்டுறவு வேளாண்மை மற்றும் ஊரக வளர்ச்சி வங்கிகள் (PCARDBs) விவசாயிகளுக்கு எந்த வகைக் கடன் உதவிகளை வழங்குவதில் நிபுணத்துவம் பெற்றுள்ளன?",
            "options": [
                ("Long-term investment loans for farm mechanization, land reclamation, and minor irrigation", "விவசாய இயந்திரமயமாக்கல், நிலச் சீர்திருத்தம் மற்றும் சிறுபாசனத்திற்கான நீண்ட கால முதலீட்டுக் கடன்கள்"),
                ("Short-term crop cultivation loans for seasonal seeds and fertilizers only", "பருவக்கால விதைகள் மற்றும் உரங்களுக்கான குறுகிய கால பயிர்க்கடன்கள் மட்டுமே"),
                ("Daily microfinance credit for urban street vendors only", "நகர்ப்புற தெருவோர வியாபாரிகளுக்கான தினசரி நுண்கடன் மட்டுமே"),
                ("Foreign exchange loans for multinational corporations", "பன்னாட்டு நிறுவனங்களுக்கான அந்நியச் செலாவணிக் கடன்கள்")
            ],
            "correct_key": "A",
            "exp_en": "PCARDBs (formerly Land Development Banks) provide medium and long-term loans (ranging from 5 to 15-20 years) to farmers for capital formation, minor irrigation (wells, pump sets), tractors, power tillers, and plantation crops.",
            "exp_ta": "PCARDBs (முன்பு நிலவள வங்கிகள் என அழைக்கப்பட்டவை) மூலதன உருவாக்கம், சிறுபாசனம் (கிணறுகள், பம்புசெட்டுகள்), டிராக்டர்கள் மற்றும் தோட்டப்பயிர்களுக்காக விவசாயிகளுக்கு நடுத்தர மற்றும் நீண்ட காலக் கடன்களை (5 முதல் 15-20 ஆண்டுகள் வரை) வழங்குகின்றன.",
            "why_a_en": "Correct. Long-term capital asset creation loans are PCARDB's primary function.",
            "why_a_ta": "சரி. நீண்ட கால மூலதன சொத்து உருவாக்கக் கடன்களே PCARDB-ன் முதன்மைப் பணியாகும்.",
            "why_b_en": "Incorrect. Short-term crop loans are provided by PACS, not PCARDBs.",
            "why_b_ta": "தவறு. குறுகிய கால பயிர்க்கடன்களை PACS-கள் வழங்குகின்றன.",
            "why_c_en": "Incorrect. Microfinance for vendors is provided by Urban Cooperative Banks/MFIs.",
            "why_c_ta": "தவறு. தெருவோர வியாபாரிகள் கடன் UCB-களால் வழங்கப்படுகிறது.",
            "why_d_en": "Incorrect. Foreign exchange is handled by authorized commercial bank dealers.",
            "why_d_ta": "தவறு. அந்நியச் செலாவணி வணிக வங்கிகளால் கையாளப்படுகிறது.",
            "tip_en": "Remember the distinction in TN: Short-Term Structure = PACS; Long-Term Structure = PCARDB.",
            "tip_ta": "TN வேறுபாட்டை நினைவில் கொள்க: குறுகிய கால அமைப்பு = PACS; நீண்ட கால அமைப்பு = PCARDB.",
            "fact_en": "PCARDBs are affiliated to the Tamil Nadu State Apex Cooperative Agriculture and Rural Development Bank (TNSCARDB).",
            "fact_ta": "PCARDB-கள் தமிழ்நாடு மாநில தலைமைக் கூட்டுறவு வேளாண்மை மற்றும் ஊரக வளர்ச்சி வங்கியுடன் இணைக்கப்பட்டுள்ளன."
        },

        # 41. Audit of Apex Cooperatives Placement before Legislature
        {
            "subtopic": "Audit of Accounts - Article 243ZM",
            "stem_en": "Under Article 243ZM(3), what must the State Government do with the annual audit report of every apex co-operative society?",
            "stem_ta": "சரத்து 243ZM(3)-ன் கீழ், ஒவ்வொரு தலைமைக் கூட்டுறவு சங்கத்தின் வருடாந்திர தணிக்கை அறிக்கையை மாநில அரசு என்ன செய்ய வேண்டும்?",
            "options": [
                ("Cause it to be laid before the State Legislature in the manner provided by law", "சட்டத்தால் வழங்கப்பட்ட முறையில் மாநிலச் சட்டமன்றத்தின் முன் வைக்க வேண்டும்"),
                ("Keep it classified in the state archives for 20 years", "மாநில ஆவணக் காப்பகத்தில் 20 ஆண்டுகளுக்கு ரகசியமாக வைக்க வேண்டும்"),
                ("Forward it to the International Monetary Fund (IMF)", "சர்வதேச நாணய நிதியத்திற்கு (IMF) அனுப்பி வைக்க வேண்டும்"),
                ("Publish it exclusively in foreign financial newspapers", "வெளிநாட்டு நிதி நாளிதழ்களில் மட்டுமே வெளியிட வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZM(3) provides that the audit report of the accounts of an apex co-operative society shall be laid before the State Legislature in the manner, as may be provided by the State Legislature by law, ensuring legislative oversight.",
            "exp_ta": "சரத்து 243ZM(3) ஒரு தலைமைக் கூட்டுறவு சங்கத்தின் கணக்குகளின் தணிக்கை அறிக்கையானது, மாநிலச் சட்டமன்றத்தால் சட்டத்தின் மூலம் வழங்கப்படக்கூடிய முறையில், சட்டமன்றத்தின் முன் வைக்கப்பட வேண்டும் என்று சட்டமன்றக் கண்காணிப்பை உறுதி செய்கிறது.",
            "why_a_en": "Correct. It must be laid before the State Legislature.",
            "why_a_ta": "சரி. இது மாநிலச் சட்டமன்றத்தின் முன் வைக்கப்பட வேண்டும்.",
            "why_b_en": "Incorrect. It is a public transparency document, not a secret file.",
            "why_b_ta": "தவறு. இது வெளிப்படையான ஆவணம், ரகசியக் கோப்பு அல்ல.",
            "why_c_en": "Incorrect. IMF has no oversight over state cooperatives.",
            "why_c_ta": "தவறு. IMF-க்கு இதில் எவ்வித தொடர்பும் இல்லை.",
            "why_d_en": "Incorrect. It is laid before the state legislature, not foreign newspapers.",
            "why_d_ta": "தவறு. மாநில சட்டமன்றத்தில் சமர்ப்பிக்கப்பட வேண்டும்.",
            "tip_en": "This mirrors Article 151(2) where CAG reports on state accounts are laid before State Legislatures.",
            "tip_ta": "இது CAG தணிக்கை அறிக்கைகள் சட்டமன்றத்தில் வைக்கப்படும் சரத்து 151(2)-ஐப் போன்றது.",
            "fact_en": "Apex societies handle thousands of crores of public and government funds, requiring legislative scrutiny.",
            "fact_ta": "தலைமைச் சங்கங்கள் ஆயிரக்கணக்கான கோடி ரூபாய் பொது நிதியைக் கையாள்வதால் சட்டமன்ற ஆய்வு அவசியமாகிறது."
        },

        # 42. Election Disqualification - Two Child Norm Controversy
        {
            "subtopic": "Election Disqualifications",
            "stem_en": "In several States (such as Rajasthan, Haryana, and Maharashtra), cooperative election rules prescribe disqualification for candidates having more than how many living children?",
            "stem_ta": "பல மாநிலங்களில் (ராஜஸ்தான், ஹரியானா மற்றும் மகாராஷ்டிரா போன்றவை), கூட்டுறவுத் தேர்தல் விதிகள் எத்தனைக்கும் மேற்பட்ட உயிருடன் இருக்கும் குழந்தைகளைக் கொண்ட வேட்பாளர்களுக்கு தகுதியிழப்பை நிர்ணயிக்கின்றன?",
            "options": [
                ("More than 2 children (Two-child norm)", "2 குழந்தைகளுக்கு மேல் (இரு குழந்தை விதி)"),
                ("More than 1 child", "1 குழந்தைக்கு மேல்"),
                ("More than 3 children", "3 குழந்தைகளுக்கு மேல்"),
                ("More than 4 children", "4 குழந்தைகளுக்கு மேல்")
            ],
            "correct_key": "A",
            "exp_en": "Several state cooperative legislations (modeled on local body election rules) enacted the 'Two-Child Norm', disqualifying individuals having more than two living children born after a cutoff date from contesting cooperative board elections, upheld by the Supreme Court in Javed v. State of Haryana (2003).",
            "exp_ta": "பல மாநிலக் கூட்டுறவுச் சட்டங்கள் (உள்ளாட்சித் தேர்தல் விதிகளைப் பின்பற்றி) 'இரு குழந்தை விதியை' அமல்படுத்தின; குறிப்பிட்ட தேதிக்குப் பிறகு இரண்டுக்கும் மேற்பட்ட குழந்தைகளைப் பெற்றவர்கள் கூட்டுறவு வாரியத் தேர்தலில் போட்டியிட தகுதியற்றவர்கள் ஆவர் (உச்ச நீதிமன்றம் ஜாவேத் எதிர் ஹரியானா அரசு (2003) வழக்கில் இதை உறுதி செய்தது).",
            "why_a_en": "Correct. The two-child norm is the statutory disqualification in several state laws.",
            "why_a_ta": "சரி. இரு குழந்தை விதி பல மாநிலச் சட்டங்களில் சட்டப்பூர்வ தகுதியிழப்பாக உள்ளது.",
            "why_b_en": "Incorrect. One child norm was never implemented in India.",
            "why_b_ta": "தவறு. ஒரு குழந்தை விதி இந்தியாவில் அமல்படுத்தப்படவில்லை.",
            "why_c_en": "Incorrect. Limit is 2 children.",
            "why_c_ta": "தவறு. வரம்பு 2 குழந்தைகள்.",
            "why_d_en": "Incorrect. Limit is 2 children.",
            "why_d_ta": "தவறு. வரம்பு 2 குழந்தைகள்.",
            "tip_en": "Tamil Nadu has NOT enacted the two-child norm for local body or cooperative elections.",
            "tip_ta": "தமிழ்நாடு உள்ளாட்சி அல்லது கூட்டுறவுத் தேர்தல்களுக்கு இரு குழந்தை விதியை அமல்படுத்தவில்லை.",
            "fact_en": "Certain states like Rajasthan have recently relaxed or reviewed this norm.",
            "fact_ta": "ராஜஸ்தான் போன்ற சில மாநிலங்கள் சமீபத்தில் இந்த விதியை தளர்த்தியுள்ளன."
        },

        # 43. Multi-State Co-operative Societies Registration Requirement
        {
            "subtopic": "Multi-State Co-operative Framework",
            "stem_en": "Under the Multi-State Co-operative Societies Act, 2002, what is the minimum statutory membership requirement to register a new multi-state cooperative society with individuals as members?",
            "stem_ta": "2002-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் சட்டத்தின் கீழ், தனிநபர்களை உறுப்பினர்களாகக் கொண்ட புதிய பல்மாநில கூட்டுறவு சங்கத்தைப் பதிவு செய்வதற்கான குறைந்தபட்ச சட்டப்பூர்வ உறுப்பினர் தேவை என்ன?",
            "options": [
                ("At least 50 persons from each of the States concerned (at least two States)", "சம்பந்தப்பட்ட ஒவ்வொரு மாநிலத்திலிருந்தும் குறைந்தபட்சம் 50 நபர்கள் (குறைந்தது இரண்டு மாநிலங்கள்)"),
                ("Only 2 persons from across India", "இந்தியா முழுவதிலுமிருந்து 2 நபர்கள் மட்டுமே"),
                ("At least 500 persons from a single district", "ஒரே மாவட்டத்திலிருந்து குறைந்தபட்சம் 500 நபர்கள்"),
                ("At least 1,000 corporate shareholders", "குறைந்தபட்சம் 1,000 கார்ப்பரேட் பங்குதாரர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Section 6 of the MSCS Act, 2002 stipulates that for an application consisting of individuals, there must be at least 50 persons from each of the States concerned (minimum two States), ensuring genuine interstate representation.",
            "exp_ta": "2002 MSCS சட்டத்தின் பிரிவு 6, தனிநபர்களைக் கொண்ட விண்ணப்பத்திற்கு சம்பந்தப்பட்ட ஒவ்வொரு மாநிலத்திலிருந்தும் குறைந்தபட்சம் 50 நபர்கள் (குறைந்தது இரண்டு மாநிலங்கள்) இருக்க வேண்டும் என்று கட்டாயமாக்குகிறது; இது உண்மையான மாநிலங்களுக்கு இடையேயான பிரதிநிதித்துவத்தை உறுதி செய்கிறது.",
            "why_a_en": "Correct. At least 50 members from each participating State.",
            "why_a_ta": "சரி. சம்பந்தப்பட்ட ஒவ்வொரு மாநிலத்திலிருந்தும் குறைந்தது 50 உறுப்பினர்கள் இருக்க வேண்டும்.",
            "why_b_en": "Incorrect. 2 persons cannot form a multi-state cooperative.",
            "why_b_ta": "தவறு. 2 நபர்கள் பல்மாநில கூட்டுறவை அமைக்க முடியாது.",
            "why_c_en": "Incorrect. Single district members form a state cooperative, not multi-state.",
            "why_c_ta": "தவறு. ஒரே மாவட்ட உறுப்பினர்கள் மாநிலக் கூட்டுறவையே அமைக்க முடியும்.",
            "why_d_en": "Incorrect. Corporate shareholders are not the basis of cooperative formation.",
            "why_d_ta": "தவறு. கார்ப்பரேட் பங்குதாரர்கள் கூட்டுறவின் அடிப்படை அல்ல.",
            "tip_en": "If membership consists of other co-operative societies, at least 5 societies from each of the two states must apply.",
            "tip_ta": "உறுப்பினர்களாக பிற கூட்டுறவு சங்கங்கள் இருந்தால், இரண்டு மாநிலங்களிலிருந்தும் தலா குறைந்தது 5 சங்கங்கள் விண்ணப்பிக்க வேண்டும்.",
            "fact_en": "Registration applications are submitted to the Central Registrar of Cooperative Societies in New Delhi.",
            "fact_ta": "பதிவு விண்ணப்பங்கள் புது தில்லியில் உள்ள மத்திய கூட்டுறவுப் பதிவாளரிடம் சமர்ப்பிக்கப்படுகின்றன."
        },

        # 44. Co-operative Principles - Limited Interest on Capital
        {
            "subtopic": "Core Principles of Cooperation",
            "stem_en": "Why do cooperative principles and state cooperative acts place a statutory ceiling on the maximum dividend that can be paid on share capital?",
            "stem_ta": "கூட்டுறவுக் கொள்கைகளும் மாநிலக் கூட்டுறவுச் சட்டங்களும் பங்கு மூலதனத்திற்கு வழங்கப்படும் அதிகபட்ச ஈவுத்தொகைக்கு ஏன் சட்டப்பூர்வ உச்சவரம்பை விதிக்கின்றன?",
            "options": [
                ("To prevent capital investment from becoming speculative and ensure that human labor and member patronage remain paramount over capital", "மூலதன முதலீடு ஊக வணிகமாக மாறுவதைத் தடுக்கவும், மூலதனத்தை விட மனித உழைப்பும் உறுப்பினர் பயன்பாடும் முதன்மையாக இருப்பதை உறுதி செய்யவும்"),
                ("Because cooperatives are legally prohibited from making any profits", "ஏனெனில் கூட்டுறவுகள் சட்டப்படி எந்த லாபமும் ஈட்டத் தடை விதிக்கப்பட்டுள்ளது"),
                ("To force members to invest exclusively in government securities", "உறுப்பினர்களை அரசுப் பத்திரங்களில் மட்டுமே முதலீடு செய்ய கட்டாயப்படுத்த"),
                ("Because state governments confiscate all cooperative surplus", "ஏனெனில் மாநில அரசுகள் அனைத்து கூட்டுறவு உபரிகளையும் பறிமுதல் செய்கின்றன")
            ],
            "correct_key": "A",
            "exp_en": "Cooperative Principle #3 (Member Economic Participation) and state acts (e.g. TN Act 1983 Section 72) restrict dividend on share capital (typically capped at 14% or 20%) so that capital does not exploit the enterprise; remaining surplus is shared as patronage refund or directed to reserve funds.",
            "exp_ta": "கூட்டுறவுக் கொள்கை 3 (உறுப்பினர் பொருளாதாரப் பங்களிப்பு) மற்றும் மாநிலச் சட்டங்கள் பங்கு மூலதனத்திற்கான ஈவுத்தொகையைக் கட்டுப்படுத்துகின்றன (பொதுவாக 14% அல்லது 20% வரை உச்சவரம்பு); இது மூலதனம் ஆதிக்கம் செலுத்துவதைத் தடுத்து, மீதமுள்ள உபரியை பயன்பாட்டு போனஸாகப் பகிர அல்லது சேம நிதிக்கு மாற்ற உதவுகிறது.",
            "why_a_en": "Correct. Limited interest on capital prevents speculative capitalist exploitation of cooperatives.",
            "why_a_ta": "சரி. மூலதனத்திற்கான வரம்புக்குட்பட்ட வட்டி ஊக வணிகச் சுரண்டலைத் தடுக்கிறது.",
            "why_b_en": "Incorrect. Cooperatives can generate surplus; they simply restrict how capital is compensated.",
            "why_b_ta": "தவறு. கூட்டுறவுகள் உபரி ஈட்ட முடியும்; மூலதனத்திற்கு வழங்கப்படும் தொகையே கட்டுப்படுத்தப்படுகிறது.",
            "why_c_en": "Incorrect. There is no compulsion to invest exclusively in government securities.",
            "why_c_ta": "தவறு. அரசுப் பத்திரங்களில் மட்டுமே முதலீடு செய்ய வேண்டும் என்ற கட்டாயம் இல்லை.",
            "why_d_en": "Incorrect. State governments do not confiscate cooperative surplus.",
            "why_d_ta": "தவறு. அரசு உபரியைப் பறிமுதல் செய்வதில்லை.",
            "tip_en": "In Tamil Nadu, Rule 85 of TN Cooperative Societies Rules caps maximum dividend on paid-up share capital at 14%.",
            "tip_ta": "தமிழ்நாட்டில், TN கூட்டுறவு சங்கங்கள் விதி 85-ன் படி செலுத்தப்பட்ட பங்கு மூலதனத்திற்கான அதிகபட்ச ஈவுத்தொகை 14% என வரம்பிடுகிறது.",
            "fact_en": "Patronage dividend rewards the active user of the cooperative, not the passive investor.",
            "fact_ta": "பயன்பாட்டு ஈவுத்தொகை செயலற்ற முதலீட்டாளருக்கு அல்லாமல், சங்கத்தைப் பயன்படுத்திய சுறுசுறுப்பான உறுப்பினருக்குப் பலனளிக்கிறது."
        },

        # 45. Tribal Development and TRIFED MFP Minimum Support Price
        {
            "subtopic": "Tribal Cooperatives",
            "stem_en": "Which scheme implemented by TRIFED provides a safety net for tribal gatherers by fixing Minimum Support Price (MSP) for Minor Forest Produce (MFP)?",
            "stem_ta": "TRIFED-ஆல் செயல்படுத்தப்படும் எந்தத் திட்டம் சிறு வன உற்பத்திப் பொருட்களுக்கு (MFP) குறைந்தபட்ச ஆதரவு விலையை (MSP) நிர்ணயிப்பதன் மூலம் பழங்குடி சேகரிப்பாளர்களுக்குப் பாதுகாப்பு வலையை வழங்குகிறது?",
            "options": [
                ("Mechanism for Marketing of Minor Forest Produce through Minimum Support Price (MSP for MFP Scheme)", "குறைந்தபட்ச ஆதரவு விலை மூலம் சிறு வன உற்பத்திப் பொருட்களை சந்தைப்படுத்துவதற்கான வழிமுறைத் திட்டம் (MSP for MFP)"),
                ("Pradhan Mantri Fasal Bima Yojana", "பிரதம மந்திரி பயிர் காப்பீட்டுத் திட்டம்"),
                ("National Rural Livelihood Mission", "தேசிய ஊரக வாழ்வாதார இயக்கம்"),
                ("PM KISAN Scheme", "பிஎம் கிசான் திட்டம்")
            ],
            "correct_key": "A",
            "exp_en": "The Central Sector Scheme 'Mechanism for Marketing of Minor Forest Produce (MFP) through Minimum Support Price (MSP) and Development of Value Chain for MFP' was introduced in 2013-14 under the Ministry of Tribal Affairs with TRIFED as the central nodal agency.",
            "exp_ta": "பழங்குடியினர் விவகாரங்கள் அமைச்சகத்தின் கீழ் TRIFED-ஐ மத்திய நோடல் முகமையாகக் கொண்டு 'சிறு வன உற்பத்திப் பொருட்களுக்கு குறைந்தபட்ச ஆதரவு விலை மூலம் சந்தைப்படுத்துதல் மற்றும் மதிப்புச் சங்கிலி மேம்பாட்டுத் திட்டம்' 2013-14-ல் தொடங்கப்பட்டது.",
            "why_a_en": "Correct. MSP for MFP is TRIFED's flagship price-support mechanism.",
            "why_a_ta": "சரி. MSP for MFP திட்டம் TRIFED-ன் முதன்மை விலை ஆதரவுத் திட்டமாகும்.",
            "why_b_en": "Incorrect. PMFBY is a crop insurance scheme for farmers.",
            "why_b_ta": "தவறு. PMFBY என்பது பயிர் காப்பீட்டுத் திட்டம்.",
            "why_c_en": "Incorrect. NRLM focuses on rural women self-help groups.",
            "why_c_ta": "தவறு. NRLM ஊரக மகளிர் சுயஉதவிக் குழுக்களில் கவனம் செலுத்துகிறது.",
            "why_d_en": "Incorrect. PM KISAN provides Rs. 6000 annual income support to farmers.",
            "why_d_ta": "தவறு. பிஎம் கிசான் விவசாயிகளுக்கு ஆண்டுக்கு ரூ. 6000 வருமான உதவி வழங்குகிறது.",
            "tip_en": "Over 87 minor forest produces (tamarind, honey, mahua flowers, lac, tendu leaves) are covered under MSP.",
            "tip_ta": "புளி, தேன், மஹுவா பூக்கள், அரக்கு, தெண்டு இலைகள் உட்பட 87-க்கும் மேற்பட்ட சிறு வனப் பொருட்கள் MSP-ன் கீழ் கொண்டுவரப்பட்டுள்ளன.",
            "fact_en": "Van Dhan Vikas Kendras value-add these forest products locally through tribal cooperatives.",
            "fact_ta": "வன்தன் விகாஸ் கேந்திராக்கள் பழங்குடியினர் கூட்டுறவுகள் மூலம் இந்த வனப் பொருட்களை உள்ளூரிலேயே மதிப்புக் கூட்டுகின்றன."
        },

        # 46. Cooperative Training Infrastructure in India
        {
            "subtopic": "Education and Training",
            "stem_en": "Which premier national institute situated in Pune functions as the apex management training institute for the cooperative sector in India?",
            "stem_ta": "புனேவில் அமைந்துள்ள எந்த முதன்மை தேசிய நிறுவனம் இந்தியாவின் கூட்டுறவுத் துறைக்கான உச்ச மேலாண்மை பயிற்சி நிறுவனமாகச் செயல்படுகிறது?",
            "options": [
                ("Vaikunth Mehta National Institute of Co-operative Management (VAMNICOM)", "வைகுந்த் மேத்தா தேசிய கூட்டுறவு மேலாண்மை நிறுவனம் (VAMNICOM)"),
                ("National Institute of Rural Development (NIRDPR), Hyderabad", "தேசிய ஊரக வளர்ச்சி நிறுவனம் (NIRDPR), ஹைதராபாத்"),
                ("Indian Institute of Public Administration (IIPA), New Delhi", "இந்திய பொது நிர்வாக நிறுவனம் (IIPA), புது தில்லி"),
                ("Lal Bahadur Shastri National Academy of Administration (LBSNAA), Mussoorie", "லால் பகதூர் சாஸ்திரி தேசிய நிர்வாக அகாடமி (LBSNAA), முசோரி")
            ],
            "correct_key": "A",
            "exp_en": "The Vaikunth Mehta National Institute of Co-operative Management (VAMNICOM) in Pune, Maharashtra, established under the National Council for Cooperative Training (NCCT), is the apex national training and research institute for cooperative management in India.",
            "exp_ta": "மகாராஷ்டிராவின் புனேவில் அமைந்துள்ள வைகுந்த் மேத்தா தேசிய கூட்டுறவு மேலாண்மை நிறுவனம் (VAMNICOM), தேசிய கூட்டுறவு பயிற்சிக் குழுவின் (NCCT) கீழ் இயங்கும் இந்தியாவின் உச்ச கூட்டுறவு மேலாண்மை பயிற்சி மற்றும் ஆராய்ச்சி நிறுவனமாகும்.",
            "why_a_en": "Correct. VAMNICOM Pune is the apex cooperative management institute.",
            "why_a_ta": "சரி. புனேவில் உள்ள VAMNICOM உச்ச கூட்டுறவு மேலாண்மை நிறுவனமாகும்.",
            "why_b_en": "Incorrect. NIRDPR focuses on general panchayati raj and rural development.",
            "why_b_ta": "தவறு. NIRDPR பொது ஊரக வளர்ச்சியில் கவனம் செலுத்துகிறது.",
            "why_c_en": "Incorrect. IIPA focuses on civil service training and public policy.",
            "why_c_ta": "தவறு. IIPA பொது நிர்வாகப் பயிற்சியைக் கையாள்கிறது.",
            "why_d_en": "Incorrect. LBSNAA trains IAS and civil service officers.",
            "why_d_ta": "தவறு. LBSNAA ஐ.ஏ.எஸ் அதிகாரிகளுக்குப் பயிற்சி அளிக்கிறது.",
            "tip_en": "Named after Vaikunthbhai Mehta, a revered pioneer of cooperative banking in India.",
            "tip_ta": "இந்தியாவில் கூட்டுறவு வங்கியின் முன்னோடியான வைகுந்த்பாய் மேத்தாவின் நினைவாகப் பெயரிடப்பட்டது.",
            "fact_en": "VAMNICOM offers an AICTE-approved Post Graduate Diploma in Cooperative Business Management.",
            "fact_ta": "VAMNICOM கூட்டுறவு வணிக மேலாண்மையில் AICTE அங்கீகரித்த முதுகலை டிப்ளமோ படிப்பை வழங்குகிறது."
        },

        # 47. State Cooperative Societies Registrar - Quasi-Judicial Powers
        {
            "subtopic": "Regulatory Framework - Registrar",
            "stem_en": "Under state cooperative societies legislation, which of the following represents a quasi-judicial power exercised by the Registrar of Co-operative Societies?",
            "stem_ta": "மாநிலக் கூட்டுறவு சங்கங்களின் சட்டத்தின் கீழ், பின்வருவனவற்றில் எது கூட்டுறவு சங்கங்களின் பதிவாளரால் பயன்படுத்தப்படும் பகுதி-நீதித்துறை (quasi-judicial) அதிகாரத்தைக் குறிக்கிறது?",
            "options": [
                ("Arbitrating and deciding statutory disputes touching the business and constitution of a society under Section 90", "பிரிவு 90-ன் கீழ் ஒரு சங்கத்தின் வணிகம் மற்றும் அமைப்பு தொடர்பான சட்டப்பூர்வ சர்ச்சைகளை நடுவராக விசாரித்துத் தீர்ப்பளித்தல்"),
                ("Promulgating presidential ordinances during legislative recess", "சட்டமன்ற இடைவேளையின் போது குடியரசுத் தலைவர் அவசரச் சட்டங்களைப் பிறப்பிப்பது"),
                ("Exercising pardoning powers under Article 161", "சரத்து 161-ன் கீழ் மன்னிப்பளிக்கும் அதிகாரத்தைப் பயன்படுத்துவது"),
                ("Presiding over sessions of the State Legislative Assembly", "மாநில சட்டமன்றக் கூட்டங்களுக்குத் தலைமை தாங்குவது")
            ],
            "correct_key": "A",
            "exp_en": "The Registrar functions as a quasi-judicial tribunal to arbitrate disputes under Section 90 of the TN Act 1983 (and corresponding sections in other state acts) touching the constitution, management, or business of a cooperative society, with powers of a civil court regarding summons and evidence.",
            "exp_ta": "1983 TN சட்டத்தின் பிரிவு 90-ன் கீழ் (மற்றும் பிற மாநிலச் சட்டங்களில் உள்ள தொடர்புடைய பிரிவுகள்) ஒரு கூட்டுறவு சங்கத்தின் அமைப்பு, மேலாண்மை அல்லது வணிகம் தொடர்பான சர்ச்சைகளை விசாரித்துத் தீர்ப்பளிக்க பதிவாளர் ஒரு பகுதி-நீதிமன்றமாகச் செயல்படுகிறார்; அழைப்பாணை மற்றும் சாட்சியங்களை விசாரிப்பதில் அவருக்கு சிவில் நீதிமன்ற அதிகாரங்கள் உண்டு.",
            "why_a_en": "Correct. Dispute arbitration under Section 90 is a classic quasi-judicial power of the Registrar.",
            "why_a_ta": "சரி. பிரிவு 90-ன் கீழ் சர்ச்சைகளை நடுவராக விசாரிப்பது பதிவாளரின் பகுதி-நீதித்துறை அதிகாரமாகும்.",
            "why_b_en": "Incorrect. Ordinance promulgation is an executive power of Governor (Art 213) / President (Art 123).",
            "why_b_ta": "தவறு. அவசரச் சட்டம் ஆளுநர்/குடியரசுத் தலைவரின் அதிகாரம்.",
            "why_c_en": "Incorrect. Pardoning power is exclusively vested in the Governor (Art 161) and President (Art 72).",
            "why_c_ta": "தவறு. மன்னிப்பளிக்கும் அதிகாரம் ஆளுநர்/குடியரசுத் தலைவருக்கு மட்டுமே உண்டு.",
            "why_d_en": "Incorrect. Speaker presides over the State Legislative Assembly.",
            "why_d_ta": "தவறு. சபாநாயகரே சட்டமன்றத்திற்குத் தலைமை தாங்குகிறார்.",
            "tip_en": "Civil court jurisdiction is barred in matters where the Registrar has statutory arbitration jurisdiction.",
            "tip_ta": "பதிவாளருக்கு சட்டப்பூர்வ நடுவர் அதிகாரம் உள்ள விஷயங்களில் சிவில் நீதிமன்றங்களின் தலையீட்டிற்குத் தடை விதிக்கப்பட்டுள்ளது.",
            "fact_en": "Appeals against the Registrar's arbitration award lie before the Co-operative Tribunal.",
            "fact_ta": "பதிவாளரின் நடுவர் தீர்ப்பிற்கு எதிரான மேல்முறையீடு கூட்டுறவுத் தீர்ப்பாயத்தில் செய்யப்பட வேண்டும்."
        },

        # 48. Primary Weavers Cooperative Societies in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "What is the primary function of Primary Weavers Co-operative Societies (PWCS) operating across districts like Kanchipuram, Salem, and Madurai?",
            "stem_ta": "காஞ்சிபுரம், சேலம் மற்றும் மதுரை போன்ற மாவட்டங்களில் செயல்படும் தொடக்க நெசவாளர் கூட்டுறவு சங்கங்களின் (PWCS) முதன்மைப் பணி என்ன?",
            "options": [
                ("Supplying yarn and raw materials to weaver members and procuring finished handloom fabrics at fair wages", "நெசவாளர் உறுப்பினர்களுக்கு நூல் மற்றும் மூலப்பொருட்களை வழங்கி, நெய்யப்பட்ட கைத்தறித் துணிகளை நியாயமான கூலிக்குக் கொள்முதல் செய்வது"),
                ("Manufacturing heavy diesel locomotives", "கனரக டீசல் என்ஜின்களைத் தயாரிப்பது"),
                ("Refining imported crude oil into aviation fuel", "இறக்குமதி செய்யப்பட்ட கச்சா எண்ணெயை விமான எரிபொருளாகச் சுத்திகரிப்பது"),
                ("Conducting geological surveys of continental shelves", "கண்டத் திட்டுக்களின் புவியியல் ஆய்வுகளை நடத்துவது")
            ],
            "correct_key": "A",
            "exp_en": "Primary Weavers Co-operative Societies (PWCS) provide raw materials (cotton, silk, dyes) to weaver members, ensure continuous employment at guaranteed living wages, and channel finished handloom products to apex marketing agencies like Co-optex.",
            "exp_ta": "தொடக்க நெசவாளர் கூட்டுறவு சங்கங்கள் (PWCS) நெசவாளர் உறுப்பினர்களுக்கு மூலப்பொருட்களை (பருத்தி, பட்டு, சாயங்கள்) வழங்கி, உத்தரவாதமான கூலியுடன் தொடர் வேலைவாய்ப்பை உறுதி செய்து, முடிக்கப்பட்ட கைத்தறித் துணிகளை கோ-ஆப்டெக்ஸ் போன்ற உச்ச விற்பனை அமைப்புகளுக்கு அனுப்புகின்றன.",
            "why_a_en": "Correct. PWCS supply yarn, ensure wages, and procure handloom fabrics.",
            "why_a_ta": "சரி. நூல் வழங்குதல், கூலி உறுதி செய்தல் மற்றும் துணி கொள்முதல் ஆகியவையே PWCS-ன் பணிகளாகும்.",
            "why_b_en": "Incorrect. Locomotives are heavy engineering, unrelated to weavers.",
            "why_b_ta": "தவறு. என்ஜின் தயாரிப்பு நெசவாளர்களுக்குத் தொடர்பற்றது.",
            "why_c_en": "Incorrect. Petroleum refining is done by oil refineries.",
            "why_c_ta": "தவறு. எண்ணெய் சுத்திகரிப்பு தொடர்பற்றது.",
            "why_d_en": "Incorrect. Geological surveys are done by Geological Survey of India.",
            "why_d_ta": "தவறு. புவியியல் ஆய்வு GSI-ன் பணி.",
            "tip_en": "Famous silk handloom hubs like Kanchipuram and Arani have world-renowned primary silk weavers cooperatives.",
            "tip_ta": "காஞ்சிபுரம் மற்றும் ஆரணி போன்ற புகழ்பெற்ற பட்டு கைத்தறி மையங்கள் உலகப் புகழ்பெற்ற தொடக்க பட்டு நெசவாளர் கூட்டுறவுகளைக் கொண்டுள்ளன.",
            "fact_en": "Co-optex acts as the apex federation for over 1,100 primary weavers cooperative societies in Tamil Nadu.",
            "fact_ta": "தமிழ்நாட்டில் உள்ள 1,100-க்கும் மேற்பட்ட தொடக்க நெசவாளர் கூட்டுறவு சங்கங்களுக்கு கோ-ஆப்டெக்ஸ் தலைமை அமைப்பாகச் செயல்படுகிறது."
        },

        # 49. Cooperative Principles - Concern for Community
        {
            "subtopic": "Core Principles of Cooperation",
            "stem_en": "Which of the 7 International Co-operative Alliance (ICA) principles emphasizes that cooperatives must work for the sustainable development of their local communities through policies approved by members?",
            "stem_ta": "உறுப்பினர்களால் அங்கீகரிக்கப்பட்ட கொள்கைகள் மூலம் கூட்டுறவுகள் தங்கள் உள்ளூர் சமூகங்களின் நிலையான வளர்ச்சிக்காக உழைக்க வேண்டும் என்பதை வலியுறுத்தும் 7 சர்வதேச கூட்டுறவு கூட்டணி (ICA) கொள்கைகளில் ஒன்று எது?",
            "options": [
                ("Concern for Community (Principle 7)", "சமூகத்தின் மீதான அக்கறை (கொள்கை 7)"),
                ("Autonomy and Independence (Principle 4)", "தன்னாட்சி மற்றும் சுதந்திரம் (கொள்கை 4)"),
                ("Member Economic Participation (Principle 3)", "உறுப்பினர் பொருளாதாரப் பங்களிப்பு (கொள்கை 3)"),
                ("Voluntary and Open Membership (Principle 1)", "தன்னார்வ மற்றும் திறந்த உறுப்பினர் சேர்க்கை (கொள்கை 1)")
            ],
            "correct_key": "A",
            "exp_en": "Principle 7 of the ICA Statement of Cooperative Identity is 'Concern for Community': 'Cooperatives work for the sustainable development of their communities through policies approved by their members.'",
            "exp_ta": "ICA கூட்டுறவு அடையாள அறிக்கையின் கொள்கை 7 என்பது 'சமூகத்தின் மீதான அக்கறை' ஆகும்: 'கூட்டுறவுகள் தங்கள் உறுப்பினர்களால் அங்கீகரிக்கப்பட்ட கொள்கைகள் மூலம் தங்கள் சமூகங்களின் நிலையான வளர்ச்சிக்காக உழைக்கின்றன.'",
            "why_a_en": "Correct. Principle 7 is specifically 'Concern for Community'.",
            "why_a_ta": "சரி. கொள்கை 7 குறிப்பாக 'சமூகத்தின் மீதான அக்கறை' பற்றியதாகும்.",
            "why_b_en": "Incorrect. Principle 4 deals with autonomy from external government control.",
            "why_b_ta": "தவறு. கொள்கை 4 தன்னாட்சி மற்றும் சுதந்திரத்தைக் குறிக்கிறது.",
            "why_c_en": "Incorrect. Principle 3 deals with capital contribution and surplus distribution.",
            "why_c_ta": "தவறு. கொள்கை 3 மூலதனப் பங்களிப்பைக் குறிக்கிறது.",
            "why_d_en": "Incorrect. Principle 1 deals with non-discriminatory admission of members.",
            "why_d_ta": "தவறு. கொள்கை 1 பாகுபாடற்ற உறுப்பினர் சேர்க்கையைக் குறிக்கிறது.",
            "tip_en": "Cooperatives fulfill Principle 7 by setting up hospitals, schools, rural libraries, and disaster relief funds.",
            "tip_ta": "கூட்டுறவுகள் மருத்துவமனைகள், பள்ளிகள், கிராம நூலகங்கள் மற்றும் பேரிடர் நிவாரண நிதிகளை அமைப்பதன் மூலம் கொள்கை 7-ஐ நிறைவேற்றுகின்றன.",
            "fact_en": "In Tamil Nadu, cooperatives contribute to the Common Good Fund used for social welfare causes.",
            "fact_ta": "தமிழ்நாட்டில், சமூக நலப் பணிகளுக்காகப் பயன்படுத்தப்படும் 'பொது நன்மை நிதிக்கு' (Common Good Fund) கூட்டுறவுகள் பங்களிக்கின்றன."
        },

        # 50. Justice K.M. Joseph's Dissent in Rajendra N. Shah
        {
            "subtopic": "Judicial Pronouncements - Landmark Ruling",
            "stem_en": "In the landmark Supreme Court decision of Union of India v. Rajendra N. Shah (2021), what was the distinctive dissenting stance taken by Justice K.M. Joseph?",
            "stem_ta": "மத்திய அரசு v. ராஜேந்திர என். ஷா (2021) வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்றத் தீர்ப்பில், நீதிபதி கே.எம். ஜோசப் எடுத்த தனித்துவமான மாறுபட்ட கருத்து (Dissenting view) என்ன?",
            "options": [
                ("He held that Part IX-B was an indivisible legislative whole and was therefore entirely unconstitutional, refusing to sever it for Multi-State cooperatives", "பகுதி IX-B என்பது பிரிக்க முடியாத ஒரு முழுமையான சட்டத்தொகுப்பு என்பதால் அது முற்றிலும் அரசியலமைப்பிற்கு முரணானது என்றும், பல்மாநில கூட்டுறவுகளுக்கு அதைப் பிரித்துத் தக்கவைக்க முடியாது என்றும் அவர் தீர்ப்பளித்தார்"),
                ("He held that the entire 97th Amendment including Article 19(1)(c) was valid for all states", "சரத்து 19(1)(c) உட்பட முழு 97வது திருத்தமும் அனைத்து மாநிலங்களுக்கும் செல்லும் என்று அவர் கூறினார்"),
                ("He ruled that Parliament has exclusive jurisdiction over agriculture", "விவசாயத்தின் மீது நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரம் உண்டு என்று அவர் தீர்ப்பளித்தார்"),
                ("He ordered the immediate abolition of all cooperative societies in India", "இந்தியாவில் உள்ள அனைத்து கூட்டுறவு சங்கங்களையும் உடனடியாக ஒழிக்க அவர் உத்தரவிட்டார்")
            ],
            "correct_key": "A",
            "exp_en": "Justice K.M. Joseph dissented from the majority on the issue of severability. He held that Parliament enacted Part IX-B as an integrated, indivisible scheme for all cooperatives and since it was invalid for lack of state ratification under Article 368(2), the entire Part IX-B must fall, even for multi-state cooperatives.",
            "exp_ta": "பிரித்தெடுப்புக் கோட்பாட்டில் நீதிபதி கே.எம். ஜோசப் பெரும்பான்மை அமர்விலிருந்து மாறுபட்டார். நாடாளுமன்றம் பகுதி IX-B-ஐ அனைத்துக் கூட்டுறவுகளுக்குமான ஒருங்கிணைந்த பிரிக்க முடியாத திட்டமாக இயற்றியதால், சரத்து 368(2) மாநில ஒப்புதல் இல்லாததால் பகுதி IX-B முழுவதுமே (பல்மாநில கூட்டுறவுகள் உட்பட) செல்லாது என அவர் கருதினார்.",
            "why_a_en": "Correct. Justice Joseph dissented, holding Part IX-B non-severable and completely void.",
            "why_a_ta": "சரி. நீதிபதி ஜோசப் பகுதி IX-B-ஐப் பிரிக்க முடியாது எனவும் முற்றிலும் செல்லாது எனவும் மாறுபட்ட தீர்ப்பளித்தார்.",
            "why_b_en": "Incorrect. He agreed with the majority that Part IX-B could not apply to State cooperatives without ratification.",
            "why_b_ta": "தவறு. மாநில ஒப்புதல் இன்றி மாநிலங்களுக்குப் பொருந்தாது என்பதை அவரும் ஒப்புக்கொண்டார்.",
            "why_c_en": "Incorrect. Agriculture is Entry 14 of State List.",
            "why_c_ta": "தவறு. விவசாயம் மாநிலப் பட்டியல் பதிவு 14.",
            "why_d_en": "Incorrect. No court ever ordered the abolition of cooperatives.",
            "why_d_ta": "தவறு. எந்த நீதிமன்றமும் கூட்டுறவை ஒழிக்க உத்தரவிடவில்லை.",
            "tip_en": "Majority (2:1): Nariman & Gavai JJ (Severable; Part IX-B survives for Multi-State & UTs); Minority (1): Joseph J (Non-severable; Part IX-B completely unconstitutional).",
            "tip_ta": "பெரும்பான்மை (2:1): நாரிமன் & கவாய் (பிரித்தெடுக்கலாம்; பல்மாநிலங்களுக்குச் செல்லும்); சிறுபான்மை (1): ஜோசப் (பிரிக்க முடியாது; முழுமையாகச் செல்லாது).",
            "fact_en": "All 3 judges unanimously upheld the validity of Article 19(1)(c) and Article 43B.",
            "fact_ta": "அனைத்து 3 நீதிபதிகளும் சரத்து 19(1)(c) மற்றும் சரத்து 43B செல்லுபடியாகும் என்பதை ஒருமனதாக ஏற்றுக்கொண்டனர்."
        }
    ]


def build_medium_file():
    raw_qs = get_medium_raw_questions()
    print(f"Loaded {len(raw_qs)} raw Medium questions.")
    assert len(raw_qs) == 50, f"Expected 50 questions, got {len(raw_qs)}"

    questions = []
    for idx, item in enumerate(raw_qs, start=1):
        qid = f"CS_M_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_coop_q(
            qid=qid,
            diff="Medium",
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
            tags=["polity", "cooperative_societies", "medium", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    # Randomize and balance answer keys: 12-13 per option, max run <= 2
    balanced = randomize_and_balance_dataset(questions, seed=101)
    key_dist = Counter(q["correct_answer"] for q in balanced)
    print(f"Balanced Key Distribution: {dict(key_dist)}")

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cooperative_societies_medium.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Medium MCQs to {out_path}")

    # Validation
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="CS_M_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_medium_file()
    if not success:
        exit(1)
