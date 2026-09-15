# -*- coding: utf-8 -*-
"""
Anti-Defection Law - Part 1: Easy (50 MCQs)
TNPSC Nova AI Content Engine

Generates 50 authentic, 24-field bilingual MCQs covering foundational concepts
of the Tenth Schedule, Articles 102(2), 191(2), 52nd CAA 1985, and basic rules.
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from anti_defection_law_mcq_helper import make_adl_q


def get_easy_raw():
    return [
        {
            "subtopic": "Constitutional Amendment",
            "stem_en": "Which Constitutional Amendment Act added the Anti-Defection Law to the Indian Constitution?",
            "stem_ta": "இந்திய அரசியலமைப்பில் கட்சித் தாவல் தடைச் சட்டத்தைச் சேர்த்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
            "options": [
                ("52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1985"),
                ("42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976"),
                ("44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978"),
                ("61st Constitutional Amendment Act, 1988", "61-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1988")
            ],
            "correct_key": "A",
            "exp_en": "The Anti-Defection Law was introduced by the 52nd Constitutional Amendment Act of 1985 under the Rajiv Gandhi government, inserting the Tenth Schedule into the Constitution.",
            "exp_ta": "ராஜீவ் காந்தி அரசாங்கத்தின் கீழ் 1985-ஆம் ஆண்டின் 52-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் பத்தாவது அட்டவணை சேர்க்கப்பட்டு கட்சித் தாவல் தடைச் சட்டம் அறிமுகப்படுத்தப்பட்டது.",
            "why_a_en": "Correct. The 52nd CAA 1985 introduced the Tenth Schedule containing the anti-defection provisions.",
            "why_a_ta": "சரி. 52-வது திருத்தச் சட்டம் 1985 கட்சித் தாவல் விதிகளைக் கொண்ட பத்தாவது அட்டவணையை அறிமுகப்படுத்தியது.",
            "why_b_en": "Incorrect. 42nd CAA 1976 introduced Fundamental Duties and amended the Preamble.",
            "why_b_ta": "தவறு. 42-வது திருத்தம் 1976 அடிப்படைக் கடமைகளை அறிமுகப்படுத்தியது மற்றும் முகப்புரையைத் திருத்தியது.",
            "why_c_en": "Incorrect. 44th CAA 1978 restored civil liberties curtailed during the Emergency.",
            "why_c_ta": "தவறு. 44-வது திருத்தம் 1978 அவசரநிலையின் போது குறைக்கப்பட்ட குடிமை உரிமைகளை மீட்டெடுத்தது.",
            "why_d_en": "Incorrect. 61st CAA 1988 lowered the voting age from 21 to 18.",
            "why_d_ta": "தவறு. 61-வது திருத்தம் 1988 வாக்களிக்கும் வயதை 21-லிருந்து 18 ஆகக் குறைத்தது.",
            "tip_en": "Remember: 52nd CAA 1985 = 10th Schedule = Anti-Defection Law.",
            "tip_ta": "நினைவில் கொள்க: 52-வது திருத்தம் 1985 = 10-வது அட்டவணை = கட்சித் தாவல் தடைச் சட்டம்.",
            "fact_en": "The 52nd Amendment Act 1985 amended Articles 101, 102, 190, and 191, and added the Tenth Schedule.",
            "fact_ta": "52-வது திருத்தச் சட்டம் 1985 உறுப்புகள் 101, 102, 190, மற்றும் 191-ஐ திருத்தி, பத்தாவது அட்டவணையைச் சேர்த்தது."
        },
        {
            "subtopic": "Schedules of Constitution",
            "stem_en": "In which Schedule of the Constitution of India are the provisions relating to disqualification on ground of defection contained?",
            "stem_ta": "கட்சித் தாவல் காரணத்தினால் ஏற்படும் தகுதி நீக்கம் தொடர்பான விதிகள் இந்திய அரசியலமைப்பின் எந்த அட்டவணையில் உள்ளன?",
            "options": [
                ("Tenth Schedule", "பத்தாவது அட்டவணை"),
                ("Eighth Schedule", "எட்டாவது அட்டவணை"),
                ("Ninth Schedule", "ஒன்பதாவது அட்டவணை"),
                ("Eleventh Schedule", "பதினோராவது அட்டவணை")
            ],
            "correct_key": "A",
            "exp_en": "Provisions as to disqualification on ground of defection are contained in the Tenth Schedule of the Constitution of India.",
            "exp_ta": "கட்சித் தாவல் காரணத்தினால் ஏற்படும் தகுதி நீக்கம் தொடர்பான விதிகள் இந்திய அரசியலமைப்பின் பத்தாவது அட்டவணையில் உள்ளடக்கப்பட்டுள்ளன.",
            "why_a_en": "Correct. Tenth Schedule deals specifically with disqualification of MPs and MLAs on ground of defection.",
            "why_a_ta": "சரி. பத்தாவது அட்டவணை கட்சித் தாவல் அடிப்படையில் எம்.பி மற்றும் எம்.எல்.ஏ-க்களின் தகுதி நீக்கம் பற்றி விரிவாகக் கூறுகிறது.",
            "why_b_en": "Incorrect. Eighth Schedule lists the 22 recognized official languages.",
            "why_b_ta": "தவறு. எட்டாவது அட்டவணை 22 அங்கீகரிக்கப்பட்ட அதிகாரப்பூர்வ மொழிகளைப் பட்டியலிடுகிறது.",
            "why_c_en": "Incorrect. Ninth Schedule protects land reform laws from judicial review under Article 31B.",
            "why_c_ta": "தவறு. ஒன்பதாவது அட்டவணை நிலச் சீர்திருத்தச் சட்டங்களை உறுப்பு 31B-ன் கீழ் நீதித்துறை மறுஆய்விலிருந்து பாதுகாக்கிறது.",
            "why_d_en": "Incorrect. Eleventh Schedule lists 29 functional items of Panchayati Raj institutions.",
            "why_d_ta": "தவறு. பதினோராவது அட்டவணை பஞ்சாயத்து ராஜ் அமைப்புகளின் 29 அதிகாரப் பணிகளைப் பட்டியலிடுகிறது.",
            "tip_en": "Tenth Schedule = Anti-defection (10 letters in 'DEFECTION' almost helps mnemonic).",
            "tip_ta": "பத்தாவது அட்டவணை = கட்சித் தாவல் தடை.",
            "fact_en": "The Tenth Schedule consists of 8 Paragraphs (Paragraph 3 was deleted in 2003).",
            "fact_ta": "பத்தாவது அட்டவணை 8 பத்திகளைக் கொண்டுள்ளது (பத்தி 3 2003-ல் நீக்கப்பட்டது)."
        },
        {
            "subtopic": "Constitutional Articles",
            "stem_en": "Which Articles of the Indian Constitution state that a person shall be disqualified for being a member if so disqualified under the Tenth Schedule?",
            "stem_ta": "பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கம் செய்யப்பட்டால் ஒருவர் உறுப்பினராக இருப்பதற்கு தகுதியற்றவர் என்று கூறும் இந்திய அரசியலமைப்பு உறுப்புகள் எவை?",
            "options": [
                ("Articles 102(2) and 191(2)", "உறுப்புகள் 102(2) மற்றும் 191(2)"),
                ("Articles 101(1) and 190(1)", "உறுப்புகள் 101(1) மற்றும் 190(1)"),
                ("Articles 105(2) and 194(2)", "உறுப்புகள் 105(2) மற்றும் 194(2)"),
                ("Articles 108 and 110", "உறுப்புகள் 108 மற்றும் 110")
            ],
            "correct_key": "A",
            "exp_en": "Article 102(2) for Parliament members and Article 191(2) for State Legislature members explicitly specify disqualification under the Tenth Schedule.",
            "exp_ta": "நாடாளுமன்ற உறுப்பினர்களுக்கு உறுப்பு 102(2) மற்றும் மாநில சட்டமன்ற உறுப்பினர்களுக்கு உறுப்பு 191(2) பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கம் பற்றி வெளிப்படையாகக் குறிப்பிடுகின்றன.",
            "why_a_en": "Correct. Articles 102(2) and 191(2) are the substantive constitutional provisions linking to the Tenth Schedule.",
            "why_a_ta": "சரி. உறுப்புகள் 102(2) மற்றும் 191(2) பத்தாவது அட்டவணையுடன் இணைக்கும் நேரடி அரசியலமைப்பு விதிகளாகும்.",
            "why_b_en": "Incorrect. Articles 101(1) and 190(1) deal with vacation of seats due to double membership.",
            "why_b_ta": "தவறு. உறுப்புகள் 101(1) மற்றும் 190(1) இரட்டை உறுப்பினர் பதவியால் ஏற்படும் இடங்கள் காலியாதலைக் கையாள்கின்றன.",
            "why_c_en": "Incorrect. Articles 105(2) and 194(2) deal with parliamentary and state legislative privileges.",
            "why_c_ta": "தவறு. உறுப்புகள் 105(2) மற்றும் 194(2) நாடாளுமன்ற மற்றும் சட்டமன்ற சலுகைகளைக் கையாள்கின்றன.",
            "why_d_en": "Incorrect. Article 108 deals with Joint Sitting, and Article 110 deals with Money Bills.",
            "why_d_ta": "தவறு. உறுப்பு 108 கூட்டுக்கூட்டம் பற்றியும், உறுப்பு 110 பண மசோதா பற்றியும் கூறுகின்றன.",
            "tip_en": "Article 102(1) = general disqualifications of MPs; Article 102(2) = defection. Same for 191(1) & 191(2) for MLAs.",
            "tip_ta": "உறுப்பு 102(1) = எம்.பி-க்களின் பொதுவான தகுதியிழப்புகள்; உறுப்பு 102(2) = கட்சித் தாவல். எம்.எல்.ஏ-க்களுக்கு 191(1) & 191(2).",
            "fact_en": "Clause (2) was added to both Articles 102 and 191 by the 52nd Constitutional Amendment Act 1985.",
            "fact_ta": "உறுப்புகள் 102 மற்றும் 191 இரண்டிலும் உட்பிரிவு (2) 1985-ன் 52-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டது."
        },
        {
            "subtopic": "Deciding Authority",
            "stem_en": "Who is the competent authority to decide any question regarding disqualification of a Lok Sabha member under the Tenth Schedule?",
            "stem_ta": "பத்தாவது அட்டவணையின் கீழ் மக்களவை உறுப்பினரின் தகுதி நீக்கம் தொடர்பான எந்தவொரு வினாவையும் தீர்மானிக்கும் தகுதிவாய்ந்த அதிகாரம் யாருக்கு உள்ளது?",
            "options": [
                ("Speaker of the Lok Sabha", "மக்களவை சபாநாயகர்"),
                ("President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("Election Commission of India", "இந்தியத் தேர்தல் ஆணையம்"),
                ("Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்")
            ],
            "correct_key": "A",
            "exp_en": "According to Paragraph 6(1) of the Tenth Schedule, questions of disqualification of a member of the House are decided by the Chairman or the Speaker of that House.",
            "exp_ta": "பத்தாவது அட்டவணையின் பத்தி 6(1)-ன் படி, அவையின் உறுப்பினர் ஒருவரின் தகுதி நீக்கம் தொடர்பான வினாக்கள் அந்த அவையின் தலைவர் அல்லது சபாநாயகரால் தீர்மானிக்கப்படுகின்றன.",
            "why_a_en": "Correct. Paragraph 6 designates the Speaker of Lok Sabha / Chairman of Rajya Sabha as the deciding authority.",
            "why_a_ta": "சரி. பத்தி 6 மக்களவை சபாநாயகர் / மாநிலங்களவைத் தலைவரைத் தீர்மானிக்கும் அதிகாரியாக நியமிக்கிறது.",
            "why_b_en": "Incorrect. President decides pre-election disqualifications under Article 103, not Tenth Schedule defections.",
            "why_b_ta": "தவறு. உறுப்பு 103-ன் கீழ் தேர்தலுக்கு முந்தைய தகுதியிழப்புகளைக் குடியரசுத் தலைவர் தீர்மானிக்கிறார், பத்தாவது அட்டவணை கட்சித் தாவலை அல்ல.",
            "why_c_en": "Incorrect. Election Commission tenders binding advice under Article 103, but has no direct deciding power under Tenth Schedule.",
            "why_c_ta": "தவறு. தேர்தல் ஆணையம் உறுப்பு 103-ன் கீழ் ஆலோசனை வழங்குகிறது, ஆனால் பத்தாவது அட்டவணையின் கீழ் நேரடி முடிவு அதிகாரம் இல்லை.",
            "why_d_en": "Incorrect. Supreme Court exercises judicial review only after the Speaker renders a final decision.",
            "why_d_ta": "தவறு. சபாநாயகர் இறுதி முடிவை வழங்கிய பின்னரே உச்ச நீதிமன்றம் நீதித்துறை மறுஆய்வை மேற்கொள்கிறது.",
            "tip_en": "Under 10th Schedule, presiding officer (Speaker/Chairman) is the primary tribunal.",
            "tip_ta": "10-வது அட்டவணையின் கீழ், அவைத் தலைவரே (சபாநாயகர்/தலைவர்) முதன்மைத் தீர்ப்பாயம் ஆவார்.",
            "fact_en": "The decision of the Speaker under Paragraph 6 is deemed to be a proceeding in Parliament under Article 122/212.",
            "fact_ta": "பத்தி 6-ன் கீழ் சபாநாயகரின் முடிவு உறுப்பு 122/212-ன் கீழ் நாடாளுமன்ற நடவடிக்கையாகக் கருதப்படுகிறது."
        },
        {
            "subtopic": "Deciding Authority",
            "stem_en": "If any question arises as to whether the Speaker or Chairman of a House has become subject to disqualification under the Tenth Schedule, who decides the question?",
            "stem_ta": "ஒரு அவையின் சபாநாயகர் அல்லது தலைவர் பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கத்திற்கு உள்ளாகிவிட்டாரா என்ற வினா எழுந்தால், அதை யார் தீர்மானிப்பார்?",
            "options": [
                ("A member of the House elected by the House for that purpose", "அந்த நோக்கத்திற்காக அவையால் தேர்ந்தெடுக்கப்பட்ட அவையின் ஓர் உறுப்பினர்"),
                ("President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
                ("Leader of the Opposition", "எதிர்க்கட்சித் தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "Under the proviso to Paragraph 6(1) of the Tenth Schedule, if a question arises regarding the Chairman or Speaker himself, it shall be decided by such member of the House as the House may elect in this behalf.",
            "exp_ta": "பத்தாவது அட்டவணையின் பத்தி 6(1)-ன் நிபந்தனையின்படி, தலைவர் அல்லது சபாநாயகர் மீதே வினா எழுந்தால், அந்த நோக்கத்திற்காக அவையால் தேர்ந்தெடுக்கப்படும் உறுப்பினர் ஒருவரால் அது தீர்மானிக்கப்படும்.",
            "why_a_en": "Correct. Proviso to Paragraph 6(1) provides for election of a member by the House to decide allegations against the Presiding Officer.",
            "why_a_ta": "சரி. பத்தி 6(1)-ன் நிபந்தனை அவைத் தலைவர் மீதான குற்றச்சாட்டுகளைத் தீர்மானிக்க அவையால் ஓர் உறுப்பினரைத் தேர்ந்தெடுக்க வழிவகை செய்கிறது.",
            "why_b_en": "Incorrect. The President has no jurisdiction under Tenth Schedule even if the Speaker is challenged.",
            "why_b_ta": "தவறு. சபாநாயகர் மீது புகார் கூறப்பட்டாலும் குடியரசுத் தலைவருக்கு பத்தாவது அட்டவணையின் கீழ் அதிகாரம் இல்லை.",
            "why_c_en": "Incorrect. The Chief Justice does not decide defection petitions directly.",
            "why_c_ta": "தவறு. தலைமை நீதிபதி கட்சித் தாவல் மனுக்களை நேரடியாகத் தீர்மானிப்பதில்லை.",
            "why_d_en": "Incorrect. Leader of Opposition is not given statutory deciding authority.",
            "why_d_ta": "தவறு. எதிர்க்கட்சித் தலைவருக்கு சட்டப்பூர்வ தீர்மானிக்கும் அதிகாரம் வழங்கப்படவில்லை.",
            "tip_en": "Remember the specific exception: Speaker vs Speaker defection = House elects an ad-hoc member.",
            "tip_ta": "குறிப்பிட்ட விதிவிலக்கு: சபாநாயகருக்கு எதிரான கட்சித் தாவல் புகார் = அவையே ஒரு உறுப்பினரைத் தேர்ந்தெடுத்துத் தீர்மானிக்கும்.",
            "fact_en": "This ensures the doctrine of nemo judex in causa sua (no one should be a judge in their own cause).",
            "fact_ta": "இது 'எவரும் தன் சொந்த வழக்கில் நீதிபதியாக இருக்க முடியாது' என்ற இயற்கை நீதிக் கோட்பாட்டை உறுதி செய்கிறது."
        },
        {
            "subtopic": "Grounds for Disqualification",
            "stem_en": "Under Paragraph 2(1)(a) of the Tenth Schedule, a member belonging to a political party is disqualified if he:",
            "stem_ta": "பத்தாவது அட்டவணையின் பத்தி 2(1)(a)-ன் கீழ், ஓர் அரசியல் கட்சியைச் சேர்ந்த உறுப்பினர் எப்போது தகுதி நீக்கம் செய்யப்படுகிறார்?",
            "options": [
                ("Voluntarily gives up membership of such political party", "அத்தகைய அரசியல் கட்சியின் உறுப்பினர் பதவியை தானாக முன்வந்து துறந்தால்"),
                ("Is expelled by his political party for indiscipline", "கட்டுப்பாடின்மைக்காக அவரது அரசியல் கட்சியால் நீக்கப்பட்டால்"),
                ("Criticizes the party leadership in a private party meeting", "ஒரு தனிப்பட்ட எல்லையிலான கட்சிக் கூட்டத்தில் கட்சித் தலைமையை விமர்சித்தால்"),
                ("Votes according to his conscience during Presidential elections", "குடியரசுத் தலைவர் தேர்தலின் போது தனது மனசாட்சியின்படி வாக்களித்தால்")
            ],
            "correct_key": "A",
            "exp_en": "Paragraph 2(1)(a) explicitly states that a member is disqualified if he voluntarily gives up the membership of the political party on whose ticket he was elected.",
            "exp_ta": "பத்தி 2(1)(a) தெளிவாகக் கூறுவதாவது, தான் தேர்ந்தெடுக்கப்பட்ட அரசியல் கட்சியின் உறுப்பினர் பதவியை ஒருவர் தானாக முன்வந்து துறந்தால் அவர் தகுதி நீக்கம் செய்யப்படுவார்.",
            "why_a_en": "Correct. Voluntarily giving up party membership is the first substantive ground under Paragraph 2(1)(a).",
            "why_a_ta": "சரி. கட்சியின் உறுப்பினர் பதவியை தானாக முன்வந்து துறத்தல் என்பது பத்தி 2(1)(a)-ன் கீழான முதல் அடிப்படைக் காரணமாகும்.",
            "why_b_en": "Incorrect. Expulsion by a political party does NOT attract disqualification under Tenth Schedule (G. Viswanathan case, 1996).",
            "why_b_ta": "தவறு. கட்சியால் நீக்கப்படுவது (expulsion) பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கத்தை ஏற்படுத்தாது (ஜி. விஸ்வநாதன் வழக்கு, 1996).",
            "why_c_en": "Incorrect. Internal party criticism within party forums is not defection under the Tenth Schedule.",
            "why_c_ta": "தவறு. உட்கட்சிக் கூட்டங்களில் கட்சியை விமர்சிப்பது பத்தாவது அட்டவணையின் கீழ் கட்சித் தாவலாகாது.",
            "why_d_en": "Incorrect. Whip cannot be issued in Presidential/Vice-Presidential elections (conducted by secret ballot under separate laws).",
            "why_d_ta": "தவறு. குடியரசுத் தலைவர் தேர்தலில் கொறடா உத்தரவு பிறப்பிக்க முடியாது (ரகசிய வாக்கெடுப்பு மூலம் நடத்தப்படுகிறது).",
            "tip_en": "Crucial distinction: 'Resigning/giving up membership' = Disqualified. 'Expelled by party' = NOT disqualified from House.",
            "tip_ta": "முக்கிய வேறுபாடு: 'தானாக விலகுதல்' = தகுதி நீக்கம். 'கட்சியிலிருந்து நீக்கப்படுதல்' = அவையிலிருந்து தகுதி நீக்கம் இல்லை.",
            "fact_en": "An expelled member remains an unattached member in the legislature until the end of the term.",
            "fact_ta": "கட்சியால் நீக்கப்பட்ட உறுப்பினர் பதவிக்காலம் முடியும் வரை அவையில் 'இணைக்கப்படாத உறுப்பினர்' (unattached member) ஆகத் தொடர்கிறார்."
        },
        {
            "subtopic": "Grounds for Disqualification",
            "stem_en": "Under Paragraph 2(1)(b) of the Tenth Schedule, voting or abstaining contrary to the party direction requires condonation within how many days to prevent disqualification?",
            "stem_ta": "பத்தாவது அட்டவணையின் பத்தி 2(1)(b)-ன் கீழ், கட்சி உத்தரவுக்கு எதிராக வாக்களிப்பது அல்லது புறக்கணிப்பது தகுதி நீக்கத்தைத் தவிர்க்க எத்தனை நாட்களுக்குள் கட்சியால் மன்னிக்கப்பட வேண்டும்?",
            "options": [
                ("15 days", "15 நாட்கள்"),
                ("30 days", "30 நாட்கள்"),
                ("60 days", "60 நாட்கள்"),
                ("90 days", "90 நாட்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Such voting or abstention must not have been condoned by the political party or person authorized by it within 15 days from the date of such voting or abstention.",
            "exp_ta": "அத்தகைய வாக்களிப்பு அல்லது புறக்கணிப்பு நடந்த நாளிலிருந்து 15 நாட்களுக்குள் சம்பந்தப்பட்ட அரசியல் கட்சியால் அல்லது அதன் அங்கீகரிக்கப்பட்ட நபரால் அது மன்னிக்கப்பட்டிருக்கக் கூடாது.",
            "why_a_en": "Correct. Paragraph 2(1)(b) specifies exactly 15 days for party condonation.",
            "why_a_ta": "சரி. பத்தி 2(1)(b) கட்சி மன்னிப்பு வழங்குவதற்கு சரியாக 15 நாட்கள் அவகாசத்தைக் குறிப்பிடுகிறது.",
            "why_b_en": "Incorrect. 30 days is for rules laying under Paragraph 8.",
            "why_b_ta": "தவறு. 30 நாட்கள் என்பது பத்தி 8-ன் கீழ் விதிகளை அவையில் சமர்ப்பிப்பதற்கான காலமாகும்.",
            "why_c_en": "Incorrect. 60 days relates to absence from House sittings under Article 101(4)/190(4).",
            "why_c_ta": "தவறு. 60 நாட்கள் என்பது அவைக் கூட்டங்களுக்கு வராமல் இருப்பது தொடர்பான காலமாகும் (உறுப்பு 101(4)).",
            "why_d_en": "Incorrect. 90 days / 3 months is the reasonable period for Speaker disposal under Keisham Meghachandra Singh.",
            "why_d_ta": "தவறு. 90 நாட்கள் என்பது சபாநாயகர் மனுவை முடிக்க உச்ச நீதிமன்றம் கூறிய பரிந்துரை காலமாகும்.",
            "tip_en": "Whip condonation window = 15 calendar days.",
            "tip_ta": "கொறடா மீறல் மன்னிப்புக் காலம் = 15 நாட்கள்.",
            "fact_en": "Prior permission can also be taken from the political party before voting/abstaining contrary to directions.",
            "fact_ta": "கட்சி உத்தரவுக்கு எதிராக வாக்களிப்பதற்கு/புறக்கணிப்பதற்கு முன் கட்சியிடம் முன்அனுமதியும் பெறலாம்."
        },
        {
            "subtopic": "Independent Members",
            "stem_en": "What happens if an independently elected member of Parliament joins a political party after his election?",
            "stem_ta": "சுயேச்சையாகத் தேர்ந்தெடுக்கப்பட்ட ஒரு நாடாளுமன்ற உறுப்பினர் தனது தேர்தலுக்குப் பிறகு ஓர் அரசியல் கட்சியில் சேர்ந்தால் என்ன நிகழும்?",
            "options": [
                ("He is disqualified from being a member of the House", "அவர் அவையின் உறுப்பினராக இருப்பதிலிருந்து தகுதி நீக்கம் செய்யப்படுவார்"),
                ("He can join any party within six months without disqualification", "அவர் எந்த தகுதி நீக்கமும் இன்றி ஆறு மாதங்களுக்குள் எந்தக் கட்சியிலும் சேரலாம்"),
                ("He loses his seat only if he joins the ruling party", "ஆளும்கட்சியில் சேர்ந்தால் மட்டுமே அவர் தனது இடத்தை இழப்பார்"),
                ("He remains a member but cannot vote on Money Bills", "அவர் உறுப்பினராக நீடிப்பார், ஆனால் பண மசோதாக்களில் வாக்களிக்க முடியாது")
            ],
            "correct_key": "A",
            "exp_en": "Under Paragraph 2(2) of the Tenth Schedule, an elected member who has been elected as an independent candidate is disqualified if he joins ANY political party after such election.",
            "exp_ta": "பத்தாவது அட்டவணையின் பத்தி 2(2)-ன் படி, சுயேச்சை வேட்பாளராகத் தேர்ந்தெடுக்கப்பட்ட ஓர் உறுப்பினர் தேர்தலுக்குப் பிறகு எந்தவொரு அரசியல் கட்சியிலும் சேர்ந்தால் தகுதி நீக்கம் செய்யப்படுவார்.",
            "why_a_en": "Correct. Paragraph 2(2) imposes an absolute bar on independent members joining any political party post-election.",
            "why_a_ta": "சரி. பத்தி 2(2) சுயேச்சை உறுப்பினர்கள் தேர்தலுக்குப் பின் எந்தக் கட்சியிலும் சேருவதற்கு முழுமையான தடை விதிக்கிறது.",
            "why_b_en": "Incorrect. The six-month window applies ONLY to Nominated members, NEVER to Independent members.",
            "why_b_ta": "தவறு. ஆறு மாத அவகாசம் நியமன உறுப்பினர்களுக்கு மட்டுமே பொருந்தும், சுயேச்சை உறுப்பினர்களுக்கு ஒருபோதும் பொருந்தாது.",
            "why_c_en": "Incorrect. Joining any party (ruling or opposition) triggers disqualification.",
            "why_c_ta": "தவறு. எந்தக் கட்சியில் சேர்ந்தாலும் (ஆளும் கட்சி அல்லது எதிர்க் கட்சி) தகுதி நீக்கம் ஏற்படும்.",
            "why_d_en": "Incorrect. Disqualification results in complete loss of membership, not partial voting restrictions.",
            "why_d_ta": "தவறு. தகுதி நீக்கம் என்பது உறுப்பினர் பதவியையே முழுமையாகப் பறிப்பதாகும்.",
            "tip_en": "TNPSC Classic Trap: Independent members get 0 months; Nominated members get 6 months.",
            "tip_ta": "டிஎன்பிஎஸ்சி முக்கியப் பொறி: சுயேச்சை உறுப்பினருக்கு 0 மாத அவகாசம்; நியமன உறுப்பினருக்கு 6 மாத அவகாசம்.",
            "fact_en": "An independent member can, however, support a government from outside or be appointed as a Minister without joining a party.",
            "fact_ta": "ஒரு சுயேச்சை உறுப்பினர் கட்சியில் சேராமல் வெளியில் இருந்து அரசுக்கு ஆதரவளிக்கலாம் அல்லது அமைச்சராகவும் நியமிக்கப்படலாம்."
        },
        {
            "subtopic": "Nominated Members",
            "stem_en": "Under Paragraph 2(3) of the Tenth Schedule, a nominated member of a House is disqualified if he joins a political party:",
            "stem_ta": "பத்தாவது அட்டவணையின் பத்தி 2(3)-ன் கீழ், ஒரு அவையின் நியமன உறுப்பினர் எப்போது அரசியல் கட்சியில் சேர்ந்தால் தகுதி நீக்கம் செய்யப்படுவார்?",
            "options": [
                ("After the expiry of six months from taking his seat", "தனது பதவியை ஏற்ற நாளிலிருந்து ஆறு மாதங்கள் முடிந்த பிறகு"),
                ("Within six months from the date on which he takes his seat", "தனது பதவியை ஏற்ற நாளிலிருந்து ஆறு மாதங்களுக்குள்"),
                ("Immediately on the date of his nomination by the President", "குடியரசுத் தலைவரால் நியமனம் செய்யப்பட்ட அதே நாளில்"),
                ("Nominated members are never allowed to join any party", "நியமன உறுப்பினர்கள் எப்போதுமே எந்தக் கட்சியிலும் சேர அனுமதிக்கப்படுவதில்லை")
            ],
            "correct_key": "A",
            "exp_en": "A nominated member is disqualified if he joins any political party AFTER the expiry of six months from the date on which he takes his seat (Paragraph 2(3)). He may join within six months without disqualification.",
            "exp_ta": "ஒரு நியமன உறுப்பினர் தனது பதவியை ஏற்ற நாளிலிருந்து ஆறு மாத கால அவகாசம் முடிந்த பிறகு ஏதேனும் அரசியல் கட்சியில் சேர்ந்தால் தகுதி நீக்கம் செய்யப்படுவார் (பத்தி 2(3)). ஆறு மாதங்களுக்குள் அவர் சேர்ந்தால் தகுதி நீக்கம் இல்லை.",
            "why_a_en": "Correct. Joining after 6 months incurs disqualification.",
            "why_a_ta": "சரி. 6 மாதங்களுக்குப் பிறகு கட்சியில் சேருவது தகுதி நீக்கத்தை ஏற்படுத்துகிறது.",
            "why_b_en": "Incorrect. Joining within 6 months is permitted and does not attract disqualification.",
            "why_b_ta": "தவறு. 6 மாதங்களுக்குள் கட்சியில் சேர அனுமதிக்கப்பட்டுள்ளது மற்றும் தகுதி நீக்கம் ஏற்படாது.",
            "why_c_en": "Incorrect. Joining immediately within 6 months is constitutionally protected.",
            "why_c_ta": "தவறு. 6 மாதங்களுக்குள் உடனடியாகச் சேருவது அரசியலமைப்பு ரீதியாகப் பாதுகாக்கப்பட்டுள்ளது.",
            "why_d_en": "Incorrect. Nominated members are permitted to join within the 6-month window.",
            "why_d_ta": "தவறு. நியமன உறுப்பினர்கள் 6 மாத கால அவகாசத்திற்குள் கட்சியில் சேர அனுமதிக்கப்படுகின்றனர்.",
            "tip_en": "Nominated member: Within 6 months = SAFE. After 6 months = DISQUALIFIED.",
            "tip_ta": "நியமன உறுப்பினர்: 6 மாதங்களுக்குள் = பாதுகாப்பு. 6 மாதங்களுக்குப் பிறகு = தகுதி நீக்கம்.",
            "fact_en": "Once a nominated member joins a political party within 6 months, he is treated as a member belonging to that political party for defection purposes.",
            "fact_ta": "ஒரு நியமன உறுப்பினர் 6 மாதங்களுக்குள் கட்சியில் சேர்ந்தவுடன், அவர் கட்சித் தாவல் நோக்கங்களுக்காக அக்கட்சியைச் சேர்ந்தவராகவே கருதப்படுவார்."
        },
        {
            "subtopic": "91st Constitutional Amendment",
            "stem_en": "Which Constitutional Amendment Act deleted Paragraph 3 of the Tenth Schedule, thereby removing the defense of 'split'?",
            "stem_ta": "பத்தாவது அட்டவணையின் பத்தி 3-ஐ நீக்கி, 'பிளவு' என்ற தற்காப்பை ரத்து செய்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
            "options": [
                ("91st Constitutional Amendment Act, 2003", "91-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"),
                ("86th Constitutional Amendment Act, 2002", "86-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2002"),
                ("89th Constitutional Amendment Act, 2003", "89-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"),
                ("93rd Constitutional Amendment Act, 2005", "93-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2005")
            ],
            "correct_key": "A",
            "exp_en": "The 91st Constitutional Amendment Act, 2003 deleted Paragraph 3 of the Tenth Schedule, which earlier protected defectors if one-third of the legislature party members split away.",
            "exp_ta": "2003-ஆம் ஆண்டின் 91-வது அரசியலமைப்புத் திருத்தச் சட்டம் பத்தாவது அட்டவணையின் பத்தி 3-ஐ நீக்கியது; முன்னதாக மூன்றில் ஒரு பங்கு சட்டமன்றக் கட்சியினர் பிளவுபட்டால் தகுதி நீக்கத்திலிருந்து பாதுகாப்பு இருந்தது.",
            "why_a_en": "Correct. 91st CAA 2003 deleted Paragraph 3 (split provision) to stop wholesale defections.",
            "why_a_ta": "சரி. 91-வது திருத்தம் 2003 மொத்தக் கட்சித் தாவல்களைத் தடுக்க பத்தி 3-ஐ (பிளவு விதி) நீக்கியது.",
            "why_b_en": "Incorrect. 86th CAA 2002 introduced Right to Education (Article 21A).",
            "why_b_ta": "தவறு. 86-வது திருத்தம் 2002 கல்வி உரிமையை (உறுப்பு 21A) அறிமுகப்படுத்தியது.",
            "why_c_en": "Incorrect. 89th CAA 2003 bifurcated National Commission for SCs and STs.",
            "why_c_ta": "தவறு. 89-வது திருத்தம் 2003 பழங்குடியினருக்கான தனித் தேசிய ஆணையத்தை உருவாக்கியது.",
            "why_d_en": "Incorrect. 93rd CAA 2005 provided reservations in private educational institutions.",
            "why_d_ta": "தவறு. 93-வது திருத்தம் 2005 தனியார் கல்வி நிறுவனங்களில் இடஒதுக்கீடு வழங்கியது.",
            "tip_en": "Key year: 2003 = 91st CAA = Split deleted + 15% Council of Ministers ceiling.",
            "tip_ta": "முக்கிய ஆண்டு: 2003 = 91-வது திருத்தம் = பிளவு பாதுகாப்பு நீக்கம் + அமைச்சரவைக்கு 15% உச்சவரம்பு.",
            "fact_en": "Before 2003, a split of 1/3rd members was legal; after 2003, only a merger of 2/3rd members is recognized.",
            "fact_ta": "2003-க்கு முன், 1/3 உறுப்பினர்களின் பிளவு சட்டப்பூர்வமானது; 2003-க்குப் பின், 2/3 உறுப்பினர்களின் இணைப்பு மட்டுமே அங்கீகரிக்கப்படுகிறது."
        }
    ]

# Generate remaining 40 questions to complete 50
def get_remaining_easy_questions():
    q_data = [
        # 11
        ("Historical Context",
         "The infamous political phrase 'Aaya Ram Gaya Ram' that inspired the Anti-Defection Law originated in 1967 in which Indian State?",
         "கட்சித் தாவல் தடைச் சட்டத்திற்கு வித்திட்ட புகழ்பெற்ற 'ஆயா ராம் கயா ராம்' என்ற அரசியல் முழக்கம் 1967-ல் எந்த இந்திய மாநிலத்தில் உருவானது?",
         [("Haryana", "ஹரியானா"), ("Punjab", "பஞ்சாப்"), ("Uttar Pradesh", "உத்தரப் பிரதேசம்"), ("Bihar", "பீகார்")],
         "A",
         "The phrase originated in 1967 when Gaya Lal, an MLA from Hassanpur constituency in Haryana, changed his political party thrice within a single fortnight.",
         "1967-ல் ஹரியானாவின் ஹசன்பூர் தொகுதி எம்.எல்.ஏ கயா லால் ஒரே பதினைந்து நாட்களில் மூன்று முறை தனது அரசியல் கட்சியை மாற்றியபோது இந்த முழக்கம் உருவானது.",
         "Gaya Lal was an MLA in Haryana Legislative Assembly in 1967.",
         "கயா லால் 1967-ல் ஹரியானா சட்டமன்றத்தின் எம்.எல்.ஏ-வாக இருந்தார்.",
         "Punjab had political instability but was not the origin of this specific phrase.",
         "பஞ்சாபில் அரசியல் உறுதியற்ற தன்மை இருந்தது, ஆனால் இந்த முழக்கம் அங்கு உருவாகவில்லை.",
         "Uttar Pradesh had coalition governments but the phrase belongs to Haryana.",
         "உத்தரப் பிரதேசத்தில் கூட்டணிகள் இருந்தன, ஆனால் இந்த வாசகம் ஹரியானாவிற்குரியது.",
         "Bihar had SVD governments, but the incident happened in Haryana.",
         "பீகாரில் சம்யுக்தா விதாயக் தள் ஆட்சிகள் இருந்தன, ஆனால் இந்த நிகழ்வு ஹரியானாவில் நடந்தது.",
         "Gaya Lal = Haryana = 1967 = Aaya Ram Gaya Ram.",
         "கயா லால் = ஹரியானா = 1967 = ஆயா ராம் கயா ராம்.",
         "Gaya Lal shifted from Congress to United Front, then back to Congress, and within nine hours back to United Front.",
         "கயா லால் காங்கிரஸிலிருந்து ஐக்கிய முன்னணிக்கும், மீண்டும் காங்கிரஸுக்கும், ஒன்பது மணி நேரத்திற்குள் மீண்டும் ஐக்கிய முன்னணிக்கும் தாவினார்."),

        # 12
        ("Historical Context",
         "Which Prime Minister of India was in office when the Anti-Defection Law (52nd Amendment) was enacted in 1985?",
         "1985-ல் கட்சித் தாவல் தடைச் சட்டம் (52-வது திருத்தம்) இயற்றப்பட்டபோது பதவியில் இருந்த இந்தியப் பிரதமர் யார்?",
         [("Rajiv Gandhi", "ராஜீவ் காந்தி"), ("Indira Gandhi", "இந்திரா காந்தி"), ("Morarji Desai", "மொரார்ஜி தேசாய்"), ("V.P. Singh", "வி.பி. சிங்")],
         "A",
         "The 52nd Amendment Act 1985 was piloted and passed under the tenure of Prime Minister Rajiv Gandhi.",
         "52-வது திருத்தச் சட்டம் 1985 பிரதமர் ராஜீவ் காந்தியின் ஆட்சிக் காலத்தில் கொண்டுவரப்பட்டு நிறைவேற்றப்பட்டது.",
         "Rajiv Gandhi secured massive mandate in 1984 and passed the 52nd CAA in 1985.",
         "ராஜீவ் காந்தி 1984 தேர்தலில் மகத்தான வெற்றி பெற்று 1985-ல் 52-வது திருத்தச் சட்டத்தை நிறைவேற்றினார்.",
         "Indira Gandhi was assassinated in October 1984 prior to this enactment.",
         "இந்திரா காந்தி இந்தச் சட்டம் இயற்றப்படுவதற்கு முன்பு 1984 அக்டோபரில் படுகொலை செய்யப்பட்டார்.",
         "Morarji Desai headed Janata Party govt (1977-1979) and introduced the 48th Bill which lapsed.",
         "மொரார்ஜி தேசாய் 48-வது மசோதாவை அறிமுகப்படுத்தினார், ஆனால் அது நிறைவேறாமல் காலாவதியானது.",
         "V.P. Singh became Prime Minister later in 1989.",
         "வி.பி. சிங் பின்னர் 1989-ல் தான் பிரதமரானார்.",
         "Rajiv Gandhi passed 52nd CAA 1985.",
         "ராஜீவ் காந்தி 1985-ல் 52-வது திருத்தத்தை நிறைவேற்றினார்.",
         "The bill was passed unanimously in both Lok Sabha and Rajya Sabha in January 1985.",
         "இந்த மசோதா 1985 ஜனவரியில் மக்களவை மற்றும் மாநிலங்களவை இரண்டிலும் ஒருமனதாக நிறைவேற்றப்பட்டது."),

        # 13
        ("Committees on Defection",
         "Which committee was constituted by the Lok Sabha in 1967 under the chairmanship of the Union Home Minister to study the problem of defection?",
         "கட்சித் தாவல் பிரச்சனையை ஆராய ஒன்றிய உள்துறை அமைச்சரின் தலைமையில் 1967-ல் அமைக்கப்பட்ட குழு எது?",
         [("Y.B. Chavan Committee", "ஒய்.பி. சவான் குழு"), ("Sarkaria Commission", "சர்க்காரியா ஆணையம்"), ("Dinesh Goswami Committee", "தினேஷ் கோஸ்வாமி குழு"), ("Swaran Singh Committee", "சுவரண் சிங் குழு")],
         "A",
         "Following a Lok Sabha resolution in December 1967, the Committee on Defections was constituted under Union Home Minister Y.B. Chavan and submitted its report in 1969.",
         "டிசம்பர் 1967-ல் மக்களவைத் தீர்மானத்தைத் தொடர்ந்து, ஒன்றிய உள்துறை அமைச்சர் ஒய்.பி. சவான் தலைமையில் கட்சித் தாவல் குழு அமைக்கப்பட்டு 1969-ல் அறிக்கை சமர்ப்பித்தது.",
         "Y.B. Chavan Committee was the first official committee to examine defections in 1968.",
         "ஒய்.பி. சவான் குழுவே 1968-ல் கட்சித் தாவல்களை ஆராய்ந்த முதல் அதிகாரப்பூர்வ குழுவாகும்.",
         "Sarkaria Commission (1983-1988) examined Centre-State relations.",
         "சர்க்காரியா ஆணையம் (1983-1988) மத்திய-மாநில உறவுகளை ஆராய்ந்தது.",
         "Dinesh Goswami Committee (1990) examined electoral reforms.",
         "தினேஷ் கோஸ்வாமி குழு (1990) தேர்தல் சீர்திருத்தங்களை ஆராய்ந்தது.",
         "Swaran Singh Committee (1976) recommended Fundamental Duties.",
         "சுவரண் சிங் குழு (1976) அடிப்படைக் கடமைகளைப் பரிந்துரைத்தது.",
         "1st Committee on Defection = Y.B. Chavan (1968).",
         "கட்சித் தாவல் குறித்த முதல் குழு = ஒய்.பி. சவான் (1968).",
         "The Chavan Committee recommended that defecting legislators should be barred from ministerial posts for a specified period.",
         "கட்சி தாவும் உறுப்பினர்கள் குறிப்பிட்ட காலத்திற்கு அமைச்சர் பதவிகளை வகிக்கத் தடை விதிக்க வேண்டும் என்று சவான் குழு பரிந்துரைத்தது."),

        # 14
        ("Exceptions to Defection",
         "Under Paragraph 4 of the Tenth Schedule, a merger of a political party is recognized only if not less than what proportion of members of the legislature party agree?",
         "பத்தாவது அட்டவணையின் பத்தி 4-ன் கீழ், ஒரு அரசியல் கட்சியின் இணைப்பு செல்லுபடியாக சட்டமன்றக் கட்சி உறுப்பினர்களில் குறையாமல் எத்தனை பங்கு உறுப்பினர்கள் ஒப்புக்கொள்ள வேண்டும்?",
         [("Two-thirds (2/3rd)", "மூன்றில் இரண்டு பங்கு (2/3)"), ("One-third (1/3rd)", "மூன்றில் ஒரு பங்கு (1/3)"), ("One-half (1/2)", "பாதி (1/2)"), ("Three-fourths (3/4th)", "நான்கில் மூன்று பங்கு (3/4)")],
         "A",
         "Paragraph 4(2) of the Tenth Schedule provides that merger of a political party is deemed to have taken place only if not less than two-thirds of the members of the legislature party agree.",
         "பத்தாவது அட்டவணையின் பத்தி 4(2)-ன் படி, சட்டமன்றக் கட்சியின் உறுப்பினர்களில் மூன்றில் இரண்டு பங்குக்குக் குறையாதவர்கள் ஒப்புக்கொண்டால் மட்டுமே ஓர் அரசியல் கட்சியின் இணைப்பு நடந்ததாகக் கருதப்படும்.",
         "Two-thirds is the mandatory threshold under Paragraph 4(2).",
         "மூன்றில் இரண்டு பங்கு என்பது பத்தி 4(2)-ன் கீழ் கட்டாய வரம்பாகும்.",
         "One-third was the old split threshold under Paragraph 3, which was deleted in 2003.",
         "மூன்றில் ஒரு பங்கு என்பது பத்தி 3-ன் கீழ் பழைய பிளவு வரம்பு, இது 2003-ல் நீக்கப்பட்டது.",
         "One-half is not a threshold in the Tenth Schedule.",
         "பாதி என்பது பத்தாவது அட்டவணையில் ஒரு வரம்பு அல்ல.",
         "Three-fourths is not the required constitutional fraction.",
         "நான்கில் மூன்று பங்கு என்பது அரசியலமைப்பு ரீதியாகத் தேவையான பின்னம் அல்ல.",
         "Merger exemption threshold = 2/3rd of legislature party.",
         "இணைப்பு விலக்கு வரம்பு = சட்டமன்றக் கட்சியில் 2/3 பங்கு.",
         "The merger must take place between the original political party and another political party.",
         "இந்த இணைப்பு மூல அரசியல் கட்சிக்கும் மற்றொரு அரசியல் கட்சிக்கும் இடையே நிகழ வேண்டும்."),

        # 15
        ("Exceptions to Defection",
         "Which constitutional dignitary is exempted from disqualification under Paragraph 5 of the Tenth Schedule upon voluntarily giving up party membership?",
         "பத்தாவது அட்டவணையின் பத்தி 5-ன் கீழ், கட்சி உறுப்பினர் பதவியைத் தானாகத் துறந்தாலும் தகுதி நீக்கத்திலிருந்து விலக்கு அளிக்கப்படும் அரசியலமைப்புப் பிரமுகர் யார்?",
         [("Speaker or Deputy Speaker of Lok Sabha / State Legislative Assembly", "மக்களவை / மாநில சட்டமன்றத்தின் சபாநாயகர் அல்லது துணை சபாநாயகர்"), ("Prime Minister of India", "இந்தியப் பிரதமர்"), ("Chief Minister of a State", "ஒரு மாநிலத்தின் முதலமைச்சர்"), ("Leader of the Opposition", "எதிர்க்கட்சித் தலைவர்")],
         "A",
         "Paragraph 5 provides a special exemption to the Speaker/Deputy Speaker of Lok Sabha/Assembly and Chairman/Deputy Chairman of Rajya Sabha/Council if they resign from their party to maintain neutrality.",
         "அவைத் தலைவர் நடுநிலையைக் காப்பதற்காக கட்சியிலிருந்து ராஜினாமா செய்தால் தகுதி நீக்கத்திலிருந்து பத்தி 5 சிறப்பு விலக்கு அளிக்கிறது.",
         "Presiding officers are exempt under Paragraph 5 to uphold impartial conduct of the House.",
         "அவையின் நடுநிலையான நடத்தையைக் காக்க பத்தி 5-ன் கீழ் அவைத் தலைவர்களுக்கு விலக்கு அளிக்கப்பட்டுள்ளது.",
         "Prime Minister has no exemption under Paragraph 5.",
         "பிரதமருக்கு பத்தி 5-ன் கீழ் எந்த விலக்கும் இல்லை.",
         "Chief Minister has no exemption under Paragraph 5.",
         "முதலமைச்சருக்கு பத்தி 5-ன் கீழ் எந்த விலக்கும் இல்லை.",
         "Leader of Opposition enjoys no exemption under Paragraph 5.",
         "எதிர்க்கட்சித் தலைவருக்கு பத்தி 5-ன் கீழ் எந்த விலக்கும் இல்லை.",
         "Presiding Officer exemption = Paragraph 5.",
         "அவைத் தலைவர்களுக்கான விலக்கு = பத்தி 5.",
         "They can rejoin their party after demitting office without attracting defection.",
         "பதவி காலம் முடிந்த பிறகு அவர்கள் கட்சித் தாவல் தடையின்றி மீண்டும் தங்கள் கட்சியில் இணையலாம்."),

        # 16
        ("Judicial Review",
         "In which landmark case did the Supreme Court hold that the Speaker's decision under the Tenth Schedule is subject to judicial review?",
         "பத்தாவது அட்டவணையின் கீழ் சபாநாயகரின் முடிவு நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்று உச்ச நீதிமன்றம் எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில் தீர்ப்பளித்தது?",
         [("Kihoto Hollohan v. Zachillhu (1992)", "கிஹோட்டோ ஹோல்லோஹன் எதிர் ஜச்சில்லு (1992)"), ("Kesavananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள அரசு (1973)"), ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)"), ("Indira Gandhi v. Raj Narain (1975)", "இந்திரா காந்தி எதிர் ராஜ் நாராயணன் (1975)")],
         "A",
         "In Kihoto Hollohan v. Zachillhu (1992), a Constitution Bench held that while acting under the Tenth Schedule, the Speaker/Chairman acts as a Tribunal subject to judicial review.",
         "கிஹோட்டோ ஹோல்லோஹன் எதிர் ஜச்சில்லு (1992) வழக்கில், பத்தாவது அட்டவணையின் கீழ் சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார், எனவே அவரது முடிவு நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்று தீர்ப்பளிக்கப்பட்டது.",
         "Kihoto Hollohan (1992) is the foundational case establishing judicial review over defection orders.",
         "கிஹோட்டோ ஹோல்லோஹன் (1992) கட்சித் தாவல் முடிவுகள் மீதான நீதித்துறை மறுஆய்வை நிலைநாட்டிய அடிப்படை வழக்காகும்.",
         "Kesavananda Bharati (1973) established the Basic Structure doctrine.",
         "கேசவானந்த பாரதி (1973) அடிப்படை கட்டமைப்பு கோட்பாட்டை நிறுவியது.",
         "Minerva Mills (1980) affirmed balance between Fundamental Rights and DPSP.",
         "மினர்வா மில்ஸ் (1980) அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகளுக்கு இடையேயான சமநிலையை உறுதி செய்தது.",
         "Indira Gandhi v. Raj Narain (1975) struck down the 39th Amendment.",
         "இந்திரா காந்தி எதிர் ராஜ் நாராயணன் (1975) 39-வது திருத்தத்தை ரத்து செய்தது.",
         "Kihoto Hollohan 1992 = Tenth Schedule judicial review.",
         "கிஹோட்டோ ஹோல்லோஹன் 1992 = பத்தாவது அட்டவணை நீதித்துறை மறுஆய்வு.",
         "The court struck down Paragraph 7 which barred court jurisdiction because it was not ratified by states.",
         "நீதிமன்ற அதிகார வரம்பைத் தடுத்த பத்தி 7 மாநிலங்களால் அங்கீகரிக்கப்படாததால் அதை நீதிமன்றம் ரத்து செய்தது."),

        # 17
        ("Judicial Review",
         "Which Paragraph of the Tenth Schedule was struck down by the Supreme Court in the Kihoto Hollohan case (1992)?",
         "கிஹோட்டோ ஹோல்லோஹன் வழக்கில் (1992) உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்ட பத்தாவது அட்டவணையின் பத்தி எது?",
         [("Paragraph 7", "பத்தி 7"), ("Paragraph 3", "பத்தி 3"), ("Paragraph 6", "பத்தி 6"), ("Paragraph 8", "பத்தி 8")],
         "A",
         "Paragraph 7 of the Tenth Schedule, which barred the jurisdiction of courts in defection matters, was held unconstitutional because it affected the powers of High Courts and Supreme Court without state ratification under Article 368(2).",
         "கட்சித் தாவல் விவகாரங்களில் நீதிமன்றங்களின் அதிகார வரம்பைத் தடுத்த பத்தாவது அட்டவணையின் பத்தி 7, உறுப்பு 368(2)-ன் கீழ் மாநிலங்களின் ஒப்புதல் இன்றி நீதிமன்ற அதிகாரங்களைப் பாதித்ததால் அரசியலமைப்புக்கு முரணானது என ரத்து செய்யப்பட்டது.",
         "Paragraph 7 attempted to oust judicial review and was declared invalid.",
         "பத்தி 7 நீதித்துறை மறுஆய்வை நீக்க முயன்றதால் செல்லாது என அறிவிக்கப்பட்டது.",
         "Paragraph 3 was deleted by Parliament through the 91st CAA in 2003, not struck down in 1992.",
         "பத்தி 3 நாடாளுமன்றத்தால் 2003-ல் 91-வது திருத்தம் மூலம் நீக்கப்பட்டது, 1992-ல் ரத்து செய்யப்படவில்லை.",
         "Paragraph 6 designates the Speaker as tribunal and was upheld as valid.",
         "பத்தி 6 சபாநாயகரைத் தீர்ப்பாயமாக நியமிக்கிறது, அது செல்லுபடியாகும் என உறுதி செய்யப்பட்டது.",
         "Paragraph 8 deals with rule-making power and remains valid.",
         "பத்தி 8 விதி செய்யும் அதிகாரம் பற்றியது மற்றும் தொடர்ந்து நடைமுறையில் உள்ளது.",
         "Paragraph 7 struck down = Kihoto Hollohan 1992.",
         "பத்தி 7 ரத்து செய்யப்பட்டது = கிஹோட்டோ ஹோல்லோஹன் 1992.",
         "The doctrine of severability was applied: Paragraph 7 was severed while the rest of the Schedule remained valid.",
         "பிரித்தெடுக்கும் கோட்பாடு பயன்படுத்தப்பட்டது: பத்தி 7 மட்டும் நீக்கப்பட்டு மற்ற பகுதிகள் செல்லுபடியாயின."),

        # 18
        ("Voluntary Giving Up",
         "In which case did the Supreme Court hold that 'voluntarily giving up membership' is not synonymous with formal resignation and can be inferred from conduct?",
         "'தானாக முன்வந்து உறுப்பினர் பதவியைத் துறத்தல்' என்பது வெறும் முறையான ராஜினாமா மட்டுமல்ல, ஒருவரது நடத்தையிலிருந்தும் ஊகிக்கப்படலாம் என்று உச்ச நீதிமன்றம் எந்த வழக்கில் தீர்ப்பளித்தது?",
         [("Ravi S. Naik v. Union of India (1994)", "ரவி எஸ். நாயக் எதிர் இந்திய ஒன்றியம் (1994)"), ("S.R. Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994)"), ("Vishaka v. State of Rajasthan (1997)", "விசாகா எதிர் ராஜஸ்தான் அரசு (1997)"), ("Shayara Bano v. Union of India (2017)", "ஷயாரா பானோ எதிர் இந்திய ஒன்றியம் (2017)")],
         "A",
         "In Ravi S. Naik v. Union of India (1994), the Supreme Court ruled that 'voluntarily giving up membership' has a wider meaning than formal resignation; conduct such as openly supporting another party amounts to defection.",
         "ரவி எஸ். நாயக் எதிர் இந்திய ஒன்றியம் (1994) வழக்கில், 'தானாக முன்வந்து உறுப்பினர் பதவியைத் துறத்தல்' என்பது முறையான ராஜினாமாவை விட பரந்த பொருள் கொண்டது என்றும், மற்றொரு கட்சிக்கு வெளிப்படையாக ஆதரவளிக்கும் நடத்தை கட்சித் தாவலாகக் கருதப்படும் என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         "Ravi S. Naik (1994) settled that conduct infers voluntary resignation from party.",
         "ரவி எஸ். நாயக் (1994) ஒருவரது நடத்தை மூலமே கட்சித் துறத்தலை ஊகிக்கலாம் என்பதை உறுதிப்படுத்தியது.",
         "S.R. Bommai (1994) dealt with Article 356 and secularism.",
         "எஸ்.ஆர். பொம்மை (1994) உறுப்பு 356 மற்றும் மதச்சார்பின்மை தொடர்பானது.",
         "Vishaka (1997) laid down guidelines against workplace sexual harassment.",
         "விசாகா (1997) பணியிடப் பாலியல் தொல்லைக்கு எதிரான வழிகாட்டுதல்களை வழங்கியது.",
         "Shayara Bano (2017) declared instant triple talaq unconstitutional.",
         "ஷயாரா பானோ (2017) உடனடி முத்தலாக் முறையை அரசியலமைப்புக்கு முரணானது என அறிவித்தது.",
         "Conduct = Voluntarily giving up membership = Ravi S. Naik (1994).",
         "நடத்தை = தானாக உறுப்பினர் பதவியைத் துறத்தல் = ரவி எஸ். நாயக் (1994).",
         "Accompanying opposition leaders to the Governor to withdraw support from one's own government was held to be defection.",
         "சொந்த அரசுக்கு அளித்து வந்த ஆதரவை விலக்கிக் கொள்ள ஆளுநரிடம் எதிர்க் கட்சித் தலைவர்களுடன் செல்வது கட்சித் தாவலாகக் கருதப்பட்டது."),

        # 19
        ("Expulsion from Party",
         "What was held by the Supreme Court in G. Viswanathan v. Speaker, Tamil Nadu Legislative Assembly (1996) regarding an expelled legislator?",
         "கட்சியிலிருந்து நீக்கப்பட்ட ஒரு சட்டமன்ற உறுப்பினர் குறித்து ஜி. விஸ்வநாதன் எதிர் தமிழ்நாடு சட்டமன்ற சபாநாயகர் (1996) வழக்கில் உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
         [("An expelled member continues to belong to that party in the legislature until he joins another party", "கட்சியிலிருந்து நீக்கப்பட்ட உறுப்பினர் மற்றொரு கட்சியில் சேரும் வரை சட்டமன்றத்தில் அக்கட்சியைச் சேர்ந்தவராகவே தொடர்கிறார்"), ("Expelled member is automatically disqualified from the Assembly", "கட்சியிலிருந்து நீக்கப்பட்ட உறுப்பினர் தானாகவே சட்டமன்றத்திலிருந்து தகுதி நீக்கம் செய்யப்படுகிறார்"), ("Expelled member becomes an independent member permanently", "கட்சியிலிருந்து நீக்கப்பட்ட உறுப்பினர் நிரந்தரமாக சுயேச்சை உறுப்பினராக மாறுகிறார்"), ("Expelled member must immediately resign and contest by-elections", "நீக்கப்பட்ட உறுப்பினர் உடனடியாக ராஜினாமா செய்து இடைத்தேர்தலில் போட்டியிட வேண்டும்")],
         "A",
         "In G. Viswanathan (1996), the Supreme Court held that even after expulsion by the party outside the House, the member continues to belong to that political party for Tenth Schedule purposes until he joins another party.",
         "ஜி. விஸ்வநாதன் (1996) வழக்கில், அவைக்கு வெளியே கட்சியால் நீக்கப்பட்ட பின்னரும், அந்த உறுப்பினர் மற்றொரு கட்சியில் இணையும் வரை பத்தாவது அட்டவணையின் நோக்கங்களுக்காக அக்கட்சியைச் சேர்ந்தவராகவே தொடர்கிறார் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         "G. Viswanathan held expelled members are deemed to belong to the original party in the House.",
         "நீக்கப்பட்ட உறுப்பினர்கள் அவையில் மூலக் கட்சியைச் சேர்ந்தவர்களாகவே கருதப்படுவர் என்று ஜி. விஸ்வநாதன் வழக்கு கூறியது.",
         "Expulsion by party does not disqualify from legislature.",
         "கட்சியால் நீக்கப்படுவது சட்டமன்றத்திலிருந்து தகுதி நீக்கத்தை ஏற்படுத்தாது.",
         "They are not categorized as constitutional independent members.",
         "அவர்கள் அரசியலமைப்பு ரீதியான சுயேச்சை உறுப்பினர்களாகக் கருதப்படுவதில்லை.",
         "No requirement to contest by-elections arises until disqualified.",
         "தகுதி நீக்கம் செய்யப்படும் வரை இடைத்தேர்தலில் போட்டியிட வேண்டிய அவசியமில்லை.",
         "Expelled MLA joining another party = Defection (G. Viswanathan 1996).",
         "நீக்கப்பட்ட எம்.எல்.ஏ மற்றொரு கட்சியில் இணைந்தால் = கட்சித் தாவல் (ஜி. விஸ்வநாதன் 1996).",
         "Therefore, if an expelled member subsequently joins another political party, he incurs disqualification under Tenth Schedule.",
         "எனவே, நீக்கப்பட்ட உறுப்பினர் பின்னர் மற்றொரு அரசியல் கட்சியில் சேர்ந்தால், அவர் பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கம் செய்யப்படுவார்."),

        # 20
        ("Whip Application",
         "In Kihoto Hollohan (1992), the Supreme Court restricted the application of a party whip under Paragraph 2(1)(b) primarily to:",
         "கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில், உச்ச நீதிமன்றம் பத்தி 2(1)(b)-ன் கீழ் கட்சி கொறடாவின் பயன்பாட்டை முதன்மையாக எதற்கு மட்டுமே மட்டுப்படுத்தியது?",
         [("Votes determining government survival (confidence, no-confidence, money bills) or matters central to party policy", "அரசாங்கத்தின் நிலைத்தன்மையை நிர்ணயிக்கும் வாக்கெடுப்புகள் (நம்பிக்கை, நம்பிக்கையில்லாத் தீர்மானம், பண மசோதா) அல்லது கட்சியின் கொள்கை தொடர்பான முக்கிய விவகாரங்கள்"), ("Every minor procedural motion in the House", "அவையில் நடைபெறும் ஒவ்வொரு சிறிய நடைமுறைத் தீர்மானங்கள்"), ("Presidential and Vice-Presidential elections", "குடியரசுத் தலைவர் மற்றும் குடியரசுத் துணைத் தலைவர் தேர்தல்கள்"), ("Rajya Sabha biennial elections conducted by open ballot", "திறந்த வாக்கெடுப்பு மூலம் நடத்தப்படும் மாநிலங்களவை இருபதாண்டுத் தேர்தல்கள்")],
         "A",
         "The Supreme Court held that disqualification for voting against a whip should strictly apply where government stability is at stake (confidence, no-confidence, budget/money bills) or where the motion is a matter of central party policy.",
         "அரசாங்கத்தின் நிலைத்தன்மை சம்பந்தப்பட்ட (நம்பிக்கை, நம்பிக்கையில்லாத் தீர்மானம், நிதிநிலை/பண மசோதாக்கள்) அல்லது கட்சியின் மையக் கொள்கை தொடர்பான வாக்கெடுப்புகளுக்கு மட்டுமே கொறடா மீறல் தகுதி நீக்கம் கடுமையாகப் பொருந்த வேண்டும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         "Kihoto Hollohan restricted whip penalty to vital motions affecting government survival.",
         "கிஹோட்டோ ஹோல்லோஹன் அரசு நிலைத்தன்மையை பாதிக்கும் முக்கியத் தீர்மானங்களுக்கு மட்டுமே கொறடா தண்டனையைக் கட்டுப்படுத்தியது.",
         "Procedural motions do not generally warrant Tenth Schedule disqualification.",
         "நடைமுறைத் தீர்மானங்கள் பொதுவாக பத்தாவது அட்டவணை தகுதி நீக்கத்தை ஏற்படுத்துவதில்லை.",
         "Presidential elections are governed by the Presidential and Vice-Presidential Elections Act 1952, not party whip.",
         "குடியரசுத் தலைவர் தேர்தல்கள் தனியான சட்டம் மூலம் நிர்வகிக்கப்படுகின்றன, கட்சி கொறடாவால் அல்ல.",
         "Rajya Sabha voting violation does not attract Tenth Schedule defection (Kuldip Nayar case 2006).",
         "மாநிலங்களவை தேர்தல் வாக்கெடுப்பு மீறல் பத்தாவது அட்டவணை தகுதி நீக்கத்தை ஏற்படுத்தாது (குல்தீப் நாயர் வழக்கு 2006).",
         "Whip defection = Government survival votes (Confidence / No-Confidence / Money Bills).",
         "கொறடா கட்சித் தாவல் = அரசாங்க நிலைத்தன்மை வாக்கெடுப்புகள் (நம்பிக்கை / நம்பிக்கையில்லா / பண மசோதாக்கள்).",
         "This balances party discipline with freedom of speech of elected legislators.",
         "இது கட்சி ஒழுக்கத்தையும் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் பேச்சு சுதந்திரத்தையும் சமநிலைப்படுத்துகிறது.")
    ]

    # Add 30 more items to reach 50
    for i in range(21, 51):
        idx = i
        if idx == 21:
            q_data.append((
                "91st Amendment Ceilings",
                "What is the maximum limit placed on the size of the Union Council of Ministers by the 91st Constitutional Amendment Act, 2003?",
                "2003-ஆம் ஆண்டின் 91-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் ஒன்றிய அமைச்சரவையின் அளவின் மீது விதிக்கப்பட்ட அதிகபட்ச வரம்பு என்ன?",
                [("15% of the total strength of the Lok Sabha", "மக்களவையின் மொத்த பலத்தில் 15%"), ("10% of the total strength of the Lok Sabha", "மக்களவையின் மொத்த பலத்தில் 10%"), ("20% of the total strength of Parliament", "நாடாளுமன்றத்தின் மொத்த பலத்தில் 20%"), ("50 Ministers maximum", "அதிகபட்சமாக 50 அமைச்சர்கள்")],
                "A",
                "Article 75(1A), inserted by the 91st Amendment Act 2003, limits the total number of Ministers, including the Prime Minister, to 15% of the total number of members of the House of the People.",
                "91-வது திருத்தச் சட்டம் 2003 மூலம் சேர்க்கப்பட்ட உறுப்பு 75(1A), பிரதமர் உட்பட மொத்த அமைச்சர்களின் எண்ணிக்கையை மக்களவையின் மொத்த உறுப்பினர்களின் எண்ணிக்கையில் 15% ஆகக் கட்டுப்படுத்துகிறது.",
                "Article 75(1A) specifies 15% of Lok Sabha strength.",
                "உறுப்பு 75(1A) மக்களவையின் பலத்தில் 15% எனக் குறிப்பிடுகிறது.",
                "10% is the ceiling for Delhi UT Cabinet under Article 239AA, not the Union Cabinet.",
                "10% என்பது டெல்லி அமைச்சரவைக்கான உச்சவரம்பு (உறுப்பு 239AA), ஒன்றிய அமைச்சரவைக்கு அல்ல.",
                "The percentage is calculated on Lok Sabha only, not total Parliament.",
                "இந்த சதவீதம் மக்களவைக்கு மட்டுமே கணக்கிடப்படுகிறது, மொத்த நாடாளுமன்றத்திற்கு அல்ல.",
                "There is no fixed numerical limit of 50 in the Constitution.",
                "அரசியலமைப்பில் 50 என்ற நிலையான எண் வரம்பு எதுவும் இல்லை.",
                "Union Ministry ceiling = 15% of Lok Sabha (Art 75(1A)).",
                "ஒன்றிய அமைச்சரவை உச்சவரம்பு = மக்களவையில் 15% (உறுப்பு 75(1A)).",
                "In a Lok Sabha of 543 members, the maximum number of ministers including the PM cannot exceed 81."
            ))
        elif idx == 22:
            q_data.append((
                "91st Amendment Ceilings",
                "Under Article 164(1A) of the Constitution, what is the minimum number of Ministers (including the Chief Minister) prescribed for a State?",
                "அரசியலமைப்பின் 164(1A) உறுப்பின் கீழ், ஒரு மாநிலத்திற்கு பரிந்துரைக்கப்பட்ட குறைந்தபட்ச அமைச்சர்களின் எண்ணிக்கை (முதலமைச்சர் உட்பட) என்ன?",
                [("12 Ministers", "12 அமைச்சர்கள்"), ("10 Ministers", "10 அமைச்சர்கள்"), ("15 Ministers", "15 அமைச்சர்கள்"), ("7 Ministers", "7 அமைச்சர்கள்")],
                "A",
                "Article 164(1A) provides that the number of Ministers, including the Chief Minister, in a State shall not be less than twelve.",
                "உறுப்பு 164(1A) ஒரு மாநிலத்தில் முதலமைச்சர் உட்பட அமைச்சர்களின் எண்ணிக்கை பன்னிரண்டுக்கு குறையாமல் இருக்க வேண்டும் என்று கூறுகிறது.",
                "Article 164(1A) mandates minimum 12 ministers in every State.",
                "உறுப்பு 164(1A) ஒவ்வொரு மாநிலத்திலும் குறைந்தபட்சம் 12 அமைச்சர்கள் இருக்க வேண்டும் எனக் கட்டளையிடுகிறது.",
                "10 is not the minimum for States; 10% applies to Delhi.",
                "10 என்பது மாநிலங்களுக்கான குறைந்தபட்ச வரம்பு அல்ல.",
                "15 is the percentage ceiling, not the minimum absolute number.",
                "15 என்பது சதவீத உச்சவரம்பு, குறைந்தபட்ச எண்ணிக்கை அல்ல.",
                "7 applies to Delhi UT Council of Ministers (Article 239AA).",
                "7 என்பது டெல்லி யூனியன் பிரதேச அமைச்சரவைக்குப் பொருந்தும் (உறுப்பு 239AA).",
                "State Ministry: Max 15% of Assembly, Min 12 Ministers (Art 164(1A)).",
                "மாநில அமைச்சரவை: அதிகபட்சம் 15%, குறைந்தபட்சம் 12 அமைச்சர்கள் (உறுப்பு 164(1A)).",
                "The minimum limit of 12 does not apply to Union Territories with assemblies like Puducherry or Delhi."
            ))
        elif idx == 23:
            q_data.append((
                "Bar on Ministerial Office",
                "Which Articles added by the 91st Amendment Act, 2003 debar disqualified defectors from being appointed as Ministers?",
                "கட்சி தாவியவர்கள் அமைச்சர்களாக நியமிக்கப்படுவதைத் தடை செய்ய 91-வது திருத்தச் சட்டம் 2003 மூலம் சேர்க்கப்பட்ட உறுப்புகள் எவை?",
                [("Articles 75(1B) and 164(1B)", "உறுப்புகள் 75(1B) மற்றும் 164(1B)"), ("Articles 74(2) and 163(2)", "உறுப்புகள் 74(2) மற்றும் 163(2)"), ("Articles 77(3) and 166(3)", "உறுப்புகள் 77(3) மற்றும் 166(3)"), ("Articles 78 and 167", "உறுப்புகள் 78 மற்றும் 167")],
                "A",
                "Articles 75(1B) for the Union and 164(1B) for States state that a member disqualified under the Tenth Schedule shall also be disqualified to be appointed as a Minister.",
                "ஒன்றியத்திற்கு உறுப்பு 75(1B) மற்றும் மாநிலங்களுக்கு 164(1B) பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கம் செய்யப்பட்ட உறுப்பினர் அமைச்சராக நியமிக்கப்படுவதற்கும் தகுதியற்றவர் என்று கூறுகின்றன.",
                "Articles 75(1B) and 164(1B) were specifically inserted by the 91st CAA 2003.",
                "உறுப்புகள் 75(1B) மற்றும் 164(1B) 91-வது திருத்தச் சட்டம் 2003 மூலம் சேர்க்கப்பட்டன.",
                "Articles 74(2) and 163(2) bar courts from inquiring into advice tendered by ministers.",
                "உறுப்புகள் 74(2) மற்றும் 163(2) அமைச்சர்கள் வழங்கிய ஆலோசனையை நீதிமன்றங்கள் விசாரிப்பதைத் தடுக்கின்றன.",
                "Articles 77(3) and 166(3) deal with allocation of government business rules.",
                "உறுப்புகள் 77(3) மற்றும் 166(3) அரசு அலுவல் ஒதுக்கீட்டு விதிகளைக் கையாள்கின்றன.",
                "Articles 78 and 167 define duties of Prime Minister and Chief Minister towards President and Governor.",
                "உறுப்புகள் 78 மற்றும் 167 பிரதமர் மற்றும் முதலமைச்சரின் கடமைகளை வரையறுக்கின்றன.",
                "Bar on Defectors as Ministers = Arts 75(1B) & 164(1B).",
                "கட்சி தாவியவர்கள் அமைச்சராவதற்குத் தடை = உறுப்புகள் 75(1B) & 164(1B).",
                "The bar continues until the expiry of their term or until they get re-elected."
            ))
        elif idx == 24:
            q_data.append((
                "Remunerative Political Post",
                "Which Article of the Constitution bars a person disqualified under the Tenth Schedule from holding any remunerative political post?",
                "பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கம் செய்யப்பட்ட ஒருவர் எந்தவொரு ஊதியம் பெறும் அரசியல் பதவியையும் வகிப்பதைத் தடை செய்யும் அரசியலமைப்பு உறுப்பு எது?",
                [("Article 361B", "உறுப்பு 361B"), ("Article 361A", "உறுப்பு 361A"), ("Article 368", "உறுப்பு 368"), ("Article 370", "உறுப்பு 370")],
                "A",
                "Article 361B, inserted by the 91st Constitutional Amendment Act 2003, debars a disqualified defector from holding any remunerative political post under the government.",
                "2003-ஆம் ஆண்டின் 91-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட உறுப்பு 361B, தகுதி நீக்கம் செய்யப்பட்ட கட்சி தாவியவர் அரசின் கீழ் எந்தவொரு ஊதியம் பெறும் அரசியல் பதவியையும் வகிப்பதைத் தடை செய்கிறது.",
                "Article 361B specifically prohibits remunerative political appointments for defectors.",
                "உறுப்பு 361B கட்சி தாவியவர்களுக்கு ஊதியம் பெறும் அரசியல் நியமனங்களைத் திட்டவட்டமாகத் தடை செய்கிறது.",
                "Article 361A provides protection for publication of parliamentary proceedings.",
                "உறுப்பு 361A நாடாளுமன்ற நடவடிக்கைகளை வெளியிடுவதற்கான பாதுகாப்பை வழங்குகிறது.",
                "Article 368 deals with constitutional amendments.",
                "உறுப்பு 368 அரசியலமைப்புத் திருத்தங்களைக் கையாள்கிறது.",
                "Article 370 dealt with temporary provisions regarding Jammu & Kashmir.",
                "உறுப்பு 370 ஜம்மு காஷ்மீர் தொடர்பான தற்காலிக விதிகளைக் கையாண்டது.",
                "Article 361B = Bar on remunerative political post for defectors.",
                "உறுப்பு 361B = கட்சி தாவியவர்களுக்கு ஊதியம் பெறும் அரசியல் பதவிக்குத் தடை.",
                "Remunerative political post includes any office under central/state government where remuneration is paid from public revenue."
            ))
        elif idx == 25:
            q_data.append((
                "Deciding Authority Nature",
                "According to the Supreme Court in Kihoto Hollohan (1992), while deciding defection petitions, the Speaker acts as a:",
                "கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில் உச்ச நீதிமன்றத்தின்படி, கட்சித் தாவல் மனுக்களைத் தீர்மானிக்கும் போது சபாநாயகர் எவ்வாறு செயல்படுகிறார்?",
                [("Quasi-judicial Tribunal", "அரை-நீதித்துறை தீர்ப்பாயம்"), ("Administrative Authority only", "நிர்வாக அதிகாரி மட்டுமே"), ("Political Leader of the House", "அவையின் அரசியல் தலைவர்"), ("Arbitrator without judicial accountability", "நீதித்துறைப் பொறுப்பற்ற நடுவர்")],
                "A",
                "The Supreme Court held that the office of the Speaker, while deciding disqualification petitions under the Tenth Schedule, acts as a Tribunal exercising quasi-judicial power.",
                "பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்க மனுக்களைத் தீர்மானிக்கும் போது சபாநாயகர் அரை-நீதித்துறை அதிகாரத்தைச் செலுத்தும் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
                "Speaker acts as a Tribunal exercising judicial powers of the State.",
                "சபாநாயகர் அரசின் நீதித்துறை அதிகாரங்களைச் செலுத்தும் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார்.",
                "He does not act as a purely administrative authority.",
                "அவர் முற்றிலும் நிர்வாக அதிகாரியாகச் செயல்படுவதில்லை.",
                "Political role is separate from his tribunal role under Tenth Schedule.",
                "அவரது அரசியல் பங்கு பத்தாவது அட்டவணையின் கீழான தீர்ப்பாய பங்கிலிருந்து வேறுபட்டது.",
                "Arbitrators act under contract law; Speaker acts as a constitutional tribunal.",
                "சபாநாயகர் ஒரு அரசியலமைப்புத் தீர்ப்பாயமாகச் செயல்படுகிறார்.",
                "Speaker under Tenth Schedule = Tribunal.",
                "பத்தாவது அட்டவணையின் கீழ் சபாநாயகர் = தீர்ப்பாயம்.",
                "Because the Speaker acts as a Tribunal, his orders are amenable to the writ jurisdiction of High Courts and Supreme Court."
            ))
        elif idx == 26:
            q_data.append((
                "Initiation of Proceedings",
                "Can the Speaker initiate disqualification proceedings suo motu under the Tenth Schedule without receiving a petition?",
                "மனு எதுவும் பெறப்படாமல் சபாநாயகர் பத்தாவது அட்டவணையின் கீழ் தன்னிச்சையாக (suo motu) தகுதி நீக்க நடவடிக்கைகளைத் தொடங்க முடியுமா?",
                [("No, proceedings can only be initiated on a petition by a member of the House", "முடியாது, அவையின் ஓர் உறுப்பினர் மனு அளித்த பின்னரே நடவடிக்கைகளைத் தொடங்க முடியும்"), ("Yes, Speaker has absolute power to initiate proceedings suo motu anytime", "ஆம், சபாநாயகருக்கு எப்போது வேண்டுமானாலும் தன்னிச்சையாகத் தொடங்கும் முழு அதிகாரம் உண்டு"), ("Yes, provided the Governor directs him to do so", "ஆம், ஆளுநர் அவருக்கு உத்தரவிட்டால் செய்யலாம்"), ("Yes, on the recommendation of the Chief Minister", "ஆம், முதலமைச்சரின் பரிந்துரையின் பேரில் செய்யலாம்")],
                "A",
                "Under the Members of Lok Sabha/Assembly (Disqualification on Ground of Defection) Rules, disqualification proceedings can only be initiated on a written petition filed by any member of that House.",
                "கட்சித் தாவல் விதிகளின்படி, அந்த அவையின் உறுப்பினர் எவரேனும் எழுத்துப்பூர்வ மனு தாக்கல் செய்தால் மட்டுமே தகுதி நீக்க நடவடிக்கைகளைத் தொடங்க முடியும்.",
                "A petition by a member of the House is mandatory; no suo motu action is permissible.",
                "அவை உறுப்பினர் ஒருவர் மனு அளிப்பது கட்டாயம்; தன்னிச்சையாக நடவடிக்கை எடுக்க முடியாது.",
                "Speaker cannot take suo motu cognizance of defection.",
                "கட்சித் தாவல் குறித்து சபாநாயகர் தன்னிச்சையாகக் கவனத்தில் கொள்ள முடியாது.",
                "Governor has no power to direct the Speaker under Tenth Schedule.",
                "பத்தாவது அட்டவணையின் கீழ் சபாநாயகருக்கு உத்தரவிட ஆளுநருக்கு அதிகாரம் இல்லை.",
                "Chief Minister's recommendation cannot replace a formal petition.",
                "முதலமைச்சரின் பரிந்துரை முறையான மனுவுக்கு மாற்றாகாது.",
                "No Suo Motu action by Speaker under 10th Schedule.",
                "10-வது அட்டவணையின் கீழ் சபாநாயகர் தன்னிச்சையாக நடவடிக்கை எடுக்க முடியாது.",
                "Any member of the House can file the petition, even if not belonging to the defector's party."
            ))
        elif idx == 27:
            q_data.append((
                "Rule Making Power",
                "Under Paragraph 8 of the Tenth Schedule, who is empowered to make rules to give effect to the provisions of the Schedule?",
                "பத்தாவது அட்டவணையின் பத்தி 8-ன் கீழ், அட்டவணையின் விதிகளைச் செயல்படுத்த விதிமுறைகளை உருவாக்கும் அதிகாரம் யாருக்கு உள்ளது?",
                [("Chairman or Speaker of the respective House", "அந்தந்த அவையின் தலைவர் அல்லது சபாநாயகர்"), ("President of India", "இந்தியக் குடியரசுத் தலைவர்"), ("Election Commission of India", "இந்தியத் தேர்தல் ஆணையம்"), ("Parliament by law", "நாடாளுமன்றம் சட்டத்தின் மூலம்")],
                "A",
                "Paragraph 8 of the Tenth Schedule empowers the Chairman or Speaker of a House to make rules for giving effect to the provisions of the Schedule for that House.",
                "பத்தாவது அட்டவணையின் பத்தி 8 அந்தந்த அவையின் தலைவர் அல்லது சபாநாயகருக்கு அந்த அவையின் விதிகளைச் செயல்படுத்த விதிமுறைகளை உருவாக்கும் அதிகாரத்தை அளிக்கிறது.",
                "Paragraph 8 explicitly vests rule-making power in the Chairman/Speaker.",
                "பத்தி 8 விதி செய்யும் அதிகாரத்தை தலைவர்/சபாநாயகருக்கு வெளிப்படையாக வழங்குகிறது.",
                "President has rule-making powers under Article 77, not under Tenth Schedule.",
                "குடியரசுத் தலைவருக்கு உறுப்பு 77-ன் கீழ் அதிகாரம் உண்டு, பத்தாவது அட்டவணையின் கீழ் அல்ல.",
                "Election Commission does not make rules for the internal functioning of legislature under Tenth Schedule.",
                "தேர்தல் ஆணையம் சட்டமன்றத்தின் உள் செயல்பாட்டிற்கான விதிகளை உருவாக்குவதில்லை.",
                "Parliament does not frame the internal procedure rules under Paragraph 8.",
                "நாடாளுமன்றம் பத்தி 8-ன் கீழான உள் நடைமுறை விதிகளை உருவாக்குவதில்லை.",
                "Rule-making authority = Speaker/Chairman (Paragraph 8).",
                "விதி செய்யும் அதிகாரம் = சபாநாயகர்/தலைவர் (பத்தி 8).",
                "Rules framed by the Speaker must be laid before the House for a total period of 30 days."
            ))
        elif idx == 28:
            q_data.append((
                "Laying of Rules",
                "Rules made by the Speaker/Chairman under Paragraph 8 of the Tenth Schedule must be laid before the House for a period of:",
                "பத்தாவது அட்டவணையின் பத்தி 8-ன் கீழ் சபாநாயகர்/தலைவரால் உருவாக்கப்பட்ட விதிகள் எத்தனை நாட்கள் அவையின் முன் சமர்ப்பிக்கப்பட வேண்டும்?",
                [("30 days", "30 நாட்கள்"), ("14 days", "14 நாட்கள்"), ("60 days", "60 நாட்கள்"), ("90 days", "90 நாட்கள்")],
                "A",
                "Paragraph 8(2) specifies that rules made by the Presiding Officer must be laid before the House for a total period of 30 days, and are subject to modification or disapproval by the House.",
                "பத்தி 8(2)-ன் படி, அவைத் தலைவரால் உருவாக்கப்பட்ட விதிகள் மொத்தம் 30 நாட்கள் அவையின் முன் வைக்கப்பட வேண்டும், மேலும் அவை அவையின் திருத்தத்திற்கு அல்லது நிராகரிப்பிற்கு உட்பட்டவை.",
                "Paragraph 8(2) specifies a 30-day laying requirement.",
                "பத்தி 8(2) சரியாக 30 நாட்கள் சமர்ப்பிக்கும் கால அளவைக் குறிப்பிடுகிறது.",
                "14 days is for Money Bill delay in Rajya Sabha.",
                "14 நாட்கள் என்பது மாநிலங்களவையில் பண மசோதா தாமத காலம்.",
                "60 days is for seat vacation on grounds of continuous absence.",
                "60 நாட்கள் என்பது தொடர் வருகையின்மையால் இடம் காலியாவது.",
                "90 days is not the statutory laying period.",
                "90 நாட்கள் என்பது சமர்ப்பிக்கும் காலம் அல்ல.",
                "Paragraph 8 rules laying = 30 days.",
                "பத்தி 8 விதிகள் சமர்ப்பிப்பு = 30 நாட்கள்.",
                "The 30 days may be comprised in one session or in two or more successive sessions."
            ))
        elif idx == 29:
            q_data.append((
                "Pre-election vs Post-election",
                "Under Article 103 of the Constitution, who decides questions regarding general disqualifications under Article 102(1)?",
                "அரசியலமைப்பின் 103-வது உறுப்பின் கீழ், உறுப்பு 102(1)-ன் கீழான பொதுவான தகுதியிழப்புகள் தொடர்பான வினாக்களை யார் தீர்மானிக்கிறார்?",
                [("President of India acting on the binding opinion of Election Commission", "தேர்தல் ஆணையத்தின் கட்டாய ஆலோசனையின்படி செயல்படும் இந்தியக் குடியரசுத் தலைவர்"), ("Speaker of Lok Sabha acting independently", "தன்னிச்சையாகச் செயல்படும் மக்களவை சபாநாயகர்"), ("Supreme Court of India directly", "நேரடியாக இந்திய உச்ச நீதிமன்றம்"), ("Attorney General of India", "இந்திய அரசுத் தலைமை வழக்கறிஞர்")],
                "A",
                "Under Article 103, questions of disqualification under Article 102(1) (e.g. office of profit, unsound mind) are decided by the President according to the binding opinion of the Election Commission.",
                "உறுப்பு 103-ன் கீழ், உறுப்பு 102(1)-ன் கீழான தகுதியிழப்பு வினாக்கள் (எ.கா. ஆதாயம் தரும் பதவி, மனநலக்குறைவு) தேர்தல் ஆணையத்தின் கட்டாயக் கருத்தின்படி குடியரசுத் தலைவரால் தீர்மானிக்கப்படுகின்றன.",
                "President acts on ECI binding advice under Article 103 for Art 102(1) disqualifications.",
                "உறுப்பு 102(1) தகுதியிழப்புகளுக்கு 103-ன் கீழ் தேர்தல் ஆணையத்தின் ஆலோசனைப்படி குடியரசுத் தலைவர் முடிவு செய்கிறார்.",
                "Speaker decides ONLY defection questions under Article 102(2) and Tenth Schedule.",
                "சபாநாயகர் உறுப்பு 102(2) மற்றும் பத்தாவது அட்டவணையின் கீழான கட்சித் தாவல் வினாக்களை மட்டுமே தீர்மானிக்கிறார்.",
                "Supreme Court has appellate/judicial review jurisdiction, not initial deciding power.",
                "உச்ச நீதிமன்றத்திற்கு மேல்முறையீடு/மறுஆய்வு அதிகாரம் மட்டுமே உள்ளது.",
                "Attorney General gives legal advice to government, not decides disqualifications.",
                "அரசுத் தலைமை வழக்கறிஞர் சட்ட ஆலோசனை மட்டுமே வழங்குகிறார்.",
                "Art 102(1) disqualification = President on ECI advice (Art 103). Art 102(2) defection = Speaker.",
                "உறுப்பு 102(1) தகுதியிழப்பு = தேர்தல் ஆணைய ஆலோசனைப்படி குடியரசுத் தலைவர். 102(2) கட்சித் தாவல் = சபாநாயகர்.",
                "The parallel provision for State Legislatures is Article 192, where the Governor decides on ECI's opinion."
            ))
        elif idx == 30:
            q_data.append((
                "Whip Authority",
                "Who issues the party direction or 'Whip' inside the legislature on behalf of a political party?",
                "ஒரு அரசியல் கட்சியின் சார்பில் சட்டமன்றத்திற்குள் கட்சியின் உத்தரவு அல்லது 'கொறடா' உத்தரவை வெளியிடுவது யார்?",
                [("Chief Whip appointed by the political party", "அரசியல் கட்சியால் நியமிக்கப்பட்ட முதன்மைக் கொறடா"), ("Speaker of the House", "அவையின் சபாநாயகர்"), ("Governor of the State", "மாநில ஆளுநர்"), ("Election Commission of India", "இந்தியத் தேர்தல் ஆணையம்")],
                "A",
                "A 'Whip' is an official of a political party appointed to ensure party discipline and voting obedience among its legislators inside the House.",
                "அவைக்குள் உள்ள தனது உறுப்பினர்களிடையே கட்சி ஒழுக்கத்தையும் வாக்களிக்கும் கீழ்ப்படிதலையும் உறுதி செய்ய ஓர் அரசியல் கட்சியால் நியமிக்கப்படும் அதிகாரி 'கொறடா' ஆவார்.",
                "Chief Whip is the authorized party official under legislative rules.",
                "முதன்மைக் கொறடா சட்டமன்ற விதிகளின் கீழ் அங்கீகரிக்கப்பட்ட கட்சி அதிகாரி ஆவார்.",
                "Speaker is a neutral presiding officer and never issues a party whip.",
                "சபாநாயகர் ஒரு நடுநிலையான அவைத் தலைவர் மற்றும் கட்சி கொறடா உத்தரவை வெளியிட மாட்டார்.",
                "Governor is the executive head and has no role in internal party voting instructions.",
                "ஆளுநர் நிர்வாகத் தலைவர் மற்றும் கட்சி வாக்கெடுப்பு அறிவுறுத்தல்களில் அவருக்குப் பங்கில்லை.",
                "Election Commission conducts elections and does not control floor voting.",
                "தேர்தல் ஆணையம் தேர்தல்களை நடத்துகிறது மற்றும் அவையில் வாக்களிப்பதைக் கட்டுப்படுத்துவதில்லை.",
                "Party whip is issued by Chief Whip / authorized person.",
                "கட்சி கொறடா உத்தரவு முதன்மைக் கொறடாவால் வெளியிடப்படுகிறது.",
                "The office of Whip is not mentioned in the Constitution of India; it is based on parliamentary conventions."
            ))
        elif idx == 31:
            q_data.append((
                "Types of Whips",
                "Which type of Whip is the most serious, binding members to be present and vote strictly according to party lines?",
                "உறுப்பினர்கள் அவையில் ஆஜராகி கட்சியின் வழிகாட்டுதலின்படி கண்டிப்பாக வாக்களிக்கக் கட்டளையிடும் மிகக் கடுமையான கொறடா வகை எது?",
                [("Three-line Whip", "மூன்று-வரிக் கொறடா"), ("One-line Whip", "ஒரு-வரிக் கொறடா"), ("Two-line Whip", "இரண்டு-வரிக் கொறடா"), ("Four-line Whip", "நான்கு-வரிக் கொறடா")],
                "A",
                "A Three-line Whip is underlined three times and denotes the highest urgency, mandating members to be present and vote strictly according to party directions, violation of which may invite defection proceedings.",
                "மூன்று-வரிக் கொறடா மூன்று முறை அடிக்கோடிடப்பட்டு அதிகபட்ச அவசரத்தைக் குறிக்கிறது; உறுப்பினர்கள் அவையில் ஆஜராகி கட்சியின் உத்தரவுப்படி கண்டிப்பாக வாக்களிக்க வேண்டும், இதை மீறினால் கட்சித் தாவல் நடவடிக்கைகள் தொடங்கப்படலாம்.",
                "Three-line whip is the most authoritative and strictly enforced whip.",
                "மூன்று-வரிக் கொறடா மிகவும் அதிகாரப்பூர்வமான மற்றும் கண்டிப்பாக அமல்படுத்தப்படும் கொறடாவாகும்.",
                "One-line whip is non-binding and merely informs about upcoming business.",
                "ஒரு-வரிக் கொறடா கட்டாயமற்றது மற்றும் வரவிருக்கும் அலுவல்களைத் தெரிவிப்பது மட்டுமே.",
                "Two-line whip directs members to be present but does not always mandate a specific vote.",
                "இரண்டு-வரிக் கொறடா ஆஜராகுமாறு அறிவுறுத்துகிறது, ஆனால் எப்போதும் குறிப்பிட்ட வாக்கை கட்டாயமாக்குவதில்லை.",
                "Four-line whip does not exist in parliamentary convention.",
                "நான்கு-வரிக் கொறடா என்ற நடைமுறை நாடாளுமன்ற மரபில் இல்லை.",
                "Most serious whip = Three-line Whip.",
                "மிகக் கடுமையான கொறடா = மூன்று-வரிக் கொறடா.",
                "Breach of a three-line whip on a crucial vote often triggers Paragraph 2(1)(b) proceedings."
            ))
        elif idx == 32:
            q_data.append((
                "Resignation vs Defection",
                "Under Article 190(3)(b), can the Speaker reject an MLA's resignation if it is not voluntary or genuine?",
                "உறுப்பு 190(3)(b)-ன் கீழ், ஒரு சட்டமன்ற உறுப்பினரின் ராஜினாமா தானாக முன்வந்து அளிக்கப்படவில்லை அல்லது உண்மையானதல்ல என்றால் சபாநாயகர் அதை நிராகரிக்க முடியுமா?",
                [("Yes, Speaker must satisfy himself that the resignation is voluntary and genuine", "ஆம், ராஜினாமா தானாக முன்வந்ததும் உண்மையானதும் என்பதை சபாநாயகர் உறுதி செய்ய வேண்டும்"), ("No, Speaker is bound to accept any resignation immediately upon submission", "இல்லை, சமர்ப்பித்தவுடன் சபாநாயகர் உடனடியாக எந்தவொரு ராஜினாமாவையும் ஏற்கக் கடமைப்பட்டுள்ளார்"), ("No, only the Governor can accept or reject resignations", "இல்லை, ஆளுநர் மட்டுமே ராஜினாமாவை ஏற்கவோ நிராகரிக்கவோ முடியும்"), ("No, only High Court can verify genuine resignations", "இல்லை, உயர் நீதிமன்றம் மட்டுமே உண்மையான ராஜினாமாவைச் சரிபார்க்க முடியும்")],
                "A",
                "Under Article 190(3)(b) (and Art 101(3)(b) for MPs), the Speaker shall not accept a resignation if, from information received or after such inquiry as he thinks fit, he is satisfied that such resignation is not voluntary or genuine.",
                "உறுப்பு 190(3)(b)-ன் கீழ், பெறப்பட்ட தகவல்கள் அல்லது விசாரணையின் அடிப்படையில் ராஜினாமா தானாக முன்வந்ததல்ல அல்லது உண்மையானதல்ல என்று திருப்தியடைந்தால் சபாநாயகர் அதனை ஏற்றுக்கொள்ளக் கூடாது.",
                "Speaker has the constitutional power and duty to verify voluntariness and genuineness.",
                "ராஜினாமாவின் நம்பகத்தன்மையையும் தானாக முன்வந்த தன்மையையும் சரிபார்க்க சபாநாயகருக்கு அரசியலமைப்பு கடமை உண்டு.",
                "Resignations are not automatically accepted without verification.",
                "சரிபார்ப்பு இல்லாமல் ராஜினாமாக்கள் தானாக ஏற்றுக்கொள்ளப்படுவதில்லை.",
                "Governor does not accept legislative resignations.",
                "ஆளுநர் சட்டமன்ற ராஜினாமாக்களை ஏற்றுக்கொள்வதில்லை.",
                "High Court does not substitute for the Speaker's inquiry at the threshold.",
                "உயர் நீதிமன்றம் சபாநாயகரின் விசாரணைக்கு மாற்றாக அமையாது.",
                "Resignation verification = Speaker under Art 101(3)(b) / 190(3)(b).",
                "ராஜினாமா சரிபார்ப்பு = உறுப்பு 101(3)(b) / 190(3)(b)-ன் கீழ் சபாநாயகர்.",
                "This provision was inserted by the 33rd Constitutional Amendment Act 1974."
            ))
        elif idx == 33:
            q_data.append((
                "By-election Eligibility",
                "Can a legislator disqualified under the Tenth Schedule contest the by-election for the seat rendered vacant by his disqualification?",
                "பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கம் செய்யப்பட்ட ஒரு சட்டமன்ற உறுப்பினர், தனது தகுதி நீக்கத்தால் காலியான இடத்திற்கான இடைத்தேர்தலில் போட்டியிட முடியுமா?",
                [("Yes, he is eligible to contest the by-election immediately", "ஆம், அவர் உடனடியாக இடைத்தேர்தலில் போட்டியிட தகுதியுடையவர்"), ("No, he is debarred from contesting elections for 6 years", "இல்லை, அவர் 6 ஆண்டுகளுக்குத் தேர்தலில் போட்டியிடத் தடை விதிக்கப்படுகிறார்"), ("No, he cannot contest until the full term of the assembly expires", "இல்லை, சட்டமன்றத்தின் முழுப் பதவிக்காலம் முடியும் வரை அவர் போட்டியிட முடியாது"), ("Only if the Election Commission grants a special waiver", "தேர்தல் ஆணையம் சிறப்பு விலக்கு அளித்தால் மட்டுமே முடியும்")],
                "A",
                "In Shrimanth Balasaheb Patil v. Speaker, Karnataka (2019), the Supreme Court clarified that the Tenth Schedule does not disqualify a member from contesting subsequent by-elections for the remaining term.",
                "ஸ்ரீமந்த் பாலாசாகேப் பாட்டீல் எதிர் சபாநாயகர், கர்நாடகா (2019) வழக்கில், பத்தாவது அட்டவணை தகுதி நீக்கம் செய்யப்பட்ட உறுப்பினர் எஞ்சிய காலத்திற்கான இடைத்தேர்தலில் போட்டியிடுவதைத் தடுக்காது என்று உச்ச நீதிமன்றம் தெளிவுபடுத்தியது.",
                "Supreme Court held Speaker cannot bar defectors from contesting by-elections.",
                "கட்சி தாவியவர்கள் இடைத்தேர்தலில் போட்டியிடுவதை சபாநாயகர் தடுக்க முடியாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
                "There is no 6-year bar under Tenth Schedule (unlike corrupt practices under RPA 1951).",
                "மக்கள் பிரதிநிதித்துவச் சட்டத்தைப் போன்ற 6 ஆண்டுத் தடை பத்தாவது அட்டவணையில் இல்லை.",
                "Disqualification terminates current seat but does not disqualify from contesting fresh elections.",
                "தகுதி நீக்கம் தற்போதைய பதவியை மட்டுமே பறிக்கிறது, புதிய தேர்தலில் போட்டியிடுவதைத் தடுக்காது.",
                "No special waiver from ECI is required.",
                "தேர்தல் ஆணையத்தின் சிறப்பு விலக்கு எதுவும் தேவையில்லை.",
                "Defector CAN contest by-election immediately (Karnataka MLAs case 2019).",
                "கட்சி தாவியவர் உடனடியாக இடைத்தேர்தலில் போட்டியிடலாம் (கர்நாடக எம்.எல்.ஏ-க்கள் வழக்கு 2019).",
                "Speaker has no power under Tenth Schedule to specify the duration of disqualification."
            ))
        elif idx == 34:
            q_data.append((
                "Exemption Conditions",
                "Under Paragraph 4(1) of the Tenth Schedule, what is the prerequisite for a merger of a legislature party to be valid?",
                "பத்தாவது அட்டவணையின் பத்தி 4(1)-ன் கீழ், ஒரு சட்டமன்றக் கட்சியின் இணைப்பு செல்லுபடியாக என்ன முன்நிபந்தனை தேவை?",
                [("The original political party must merge with another political party", "மூல அரசியல் கட்சி மற்றொரு அரசியல் கட்சியுடன் இணைந்திருக்க வேண்டும்"), ("The Governor must approve the merger beforehand", "ஆளுநர் முன்கூட்டியே இணைப்பிற்கு ஒப்புதல் அளித்திருக்க வேண்டும்"), ("The Election Commission must issue a gazette notification", "தேர்தல் ஆணையம் அரசிதழ் அறிவிப்பை வெளியிட வேண்டும்"), ("All members of the party must unanimously vote for merger", "கட்சியின் அனைத்து உறுப்பினர்களும் ஒருமனதாக இணைப்பிற்கு வாக்களிக்க வேண்டும்")],
                "A",
                "Paragraph 4(1) states that disqualification does not apply where a member's original political party merges with another political party and he claims that he and other members have become members of such other political party.",
                "பத்தி 4(1)-ன் படி, ஒரு உறுப்பினரின் மூல அரசியல் கட்சி மற்றொரு அரசியல் கட்சியுடன் இணையும் போது மற்றும் அவரும் பிற உறுப்பினர்களும் அத்தகைய புதிய கட்சியின் உறுப்பினர்களாகிவிட்டதாகக் கூறினால் தகுதி நீக்கம் பொருந்தாது.",
                "Merger of the original political party is the primary prerequisite.",
                "மூல அரசியல் கட்சியின் இணைப்பு முதன்மையான முன்நிபந்தனையாகும்.",
                "Governor has no role in approving political party mergers.",
                "அரசியல் கட்சி இணைப்புகளுக்கு ஒப்புதல் அளிப்பதில் ஆளுநருக்குப் பங்கில்லை.",
                "Gazette notification by ECI is not a constitutional condition in Paragraph 4.",
                "தேர்தல் ஆணையத்தின் அரசிதழ் அறிவிப்பு பத்தி 4-ல் அரசியலமைப்பு நிபந்தனை அல்ல.",
                "Unanimity is not required; two-thirds majority in legislature party suffices.",
                "முழு ஒருமனதான முடிவு தேவையில்லை; சட்டமன்றக் கட்சியில் மூன்றில் இரண்டு பங்கு பெரும்பான்மை போதுமானது.",
                "Merger requires: Original party merger + 2/3rd legislature party agreement.",
                "இணைப்பிற்குத் தேவை: மூலக் கட்சி இணைப்பு + சட்டமன்றக் கட்சியில் 2/3 பங்கு ஒப்புதல்.",
                "A standalone group inside the legislature cannot merge without the original party merging."
            ))
        elif idx == 35:
            q_data.append((
                "Natural Justice",
                "In Tenth Schedule proceedings, must the Speaker comply with the principles of natural justice?",
                "பத்தாவது அட்டவணை நடவடிக்கைகளில், சபாநாயகர் இயற்கை நீதிக் கோட்பாடுகளைப் பின்பற்ற வேண்டுமா?",
                [("Yes, reasonable opportunity of being heard must be provided to the member", "ஆம், சம்பந்தப்பட்ட உறுப்பினருக்கு தனது தரப்பை எடுத்துரைக்க நியாயமான வாய்ப்பு வழங்கப்பட வேண்டும்"), ("No, Speaker has summary powers without requiring any hearing", "இல்லை, சபாநாயகருக்கு எந்த விசாரணையும் இன்றி உடனடி நடவடிக்கை எடுக்கும் அதிகாரம் உண்டு"), ("Only if the member belongs to the ruling party", "உறுப்பினர் ஆளும் கட்சியைச் சேர்ந்தவராக இருந்தால் மட்டுமே பொருந்தும்"), ("Natural justice does not apply to parliamentary proceedings", "நாடாளுமன்ற நடவடிக்கைகளுக்கு இயற்கை நீதி பொருந்தாது")],
                "A",
                "In Kihoto Hollohan (1992), the Supreme Court affirmed that the Speaker acts as a Tribunal and must comply with the minimal requirements of natural justice, including giving notice and an opportunity to be heard.",
                "கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில், சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுவதால் அறிவிப்பு வழங்குதல் மற்றும் விளக்கம் அளிக்க வாய்ப்பளித்தல் உள்ளிட்ட இயற்கை நீதியின் குறைந்தபட்ச தேவைகளைப் பின்பற்ற வேண்டும் என்று உச்ச நீதிமன்றம் உறுதிப்படுத்தியது.",
                "Natural justice is an indispensable requirement of judicial/quasi-judicial decision making.",
                "நீதித்துறை/அரை-நீதித்துறை முடிவெடுப்பதில் இயற்கை நீதி தவிர்க்க முடியாத தேவையாகும்.",
                "Summary dismissal without hearing violates Article 14.",
                "விளக்கம் கேட்காமல் உடனடியாக பதவி நீக்கம் செய்வது உறுப்பு 14-ஐ மீறுவதாகும்.",
                "Applies equally to all members regardless of party.",
                "கட்சி வேறுபாடின்றி அனைத்து உறுப்பினர்களுக்கும் சமமாகப் பொருந்தும்.",
                "Parliamentary proceedings as a tribunal are subject to natural justice.",
                "தீர்ப்பாயமாக நடைபெறும் நடவடிக்கைகள் இயற்கை நீதிக்கு உட்பட்டவை.",
                "Speaker must follow Natural Justice (Audi alteram partem).",
                "சபாநாயகர் இயற்கை நீதியைப் பின்பற்ற வேண்டும் (மறுதரப்பு நியாயத்தைக் கேட்டல்).",
                "Violation of natural justice is one of the recognized grounds for judicial review of defection orders."
            ))
        elif idx == 36:
            q_data.append((
                "Speaker Delay",
                "In Keisham Meghachandra Singh v. Hon'ble Speaker, Manipur (2020), what did the Supreme Court recommend for deciding defection cases?",
                "கீஷம் மேகசந்திர சிங் எதிர் மணிப்பூர் சபாநாயகர் (2020) வழக்கில் கட்சித் தாவல் வழக்குகளைத் தீர்மானிக்க உச்ச நீதிமன்றம் என்ன பரிந்துரைத்தது?",
                [("Creation of an independent permanent tribunal headed by a retired judge", "ஓய்வுபெற்ற நீதிபதியின் தலைமையில் ஒரு சுதந்திரமான நிரந்தர தீர்ப்பாயத்தை உருவாக்குதல்"), ("Abolition of the Tenth Schedule completely", "பத்தாவது அட்டவணையை முழுமையாக ரத்து செய்தல்"), ("Transferring all powers exclusively to the Governor", "அனைத்து அதிகாரங்களையும் ஆளுநருக்கு மட்டுமே மாற்றுதல்"), ("Allowing members to change parties freely during elections", "தேர்தல் காலத்தில் உறுப்பினர்கள் சுதந்திரமாகக் கட்சி மாற அனுமதித்தல்")],
                "A",
                "The Supreme Court observed that Parliament should consider substituting the Speaker with an independent Tribunal headed by a retired Supreme Court judge or High Court Chief Justice to decide defection cases impartially.",
                "கட்சித் தாவல் வழக்குகளை நடுநிலையுடன் தீர்மானிக்க, சபாநாயகருக்குப் பதிலாக ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதி அல்லது உயர் நீதிமன்றத் தலைமை நீதிபதி தலைமையிலான ஒரு சுதந்திரமான தீர்ப்பாயத்தை அமைப்பது குறித்து நாடாளுமன்றம் பரிசீலிக்க வேண்டும் என்று உச்ச நீதிமன்றம் குறிப்பிட்டது.",
                "Supreme Court recommended an independent permanent tribunal headed by a judge.",
                "ஓய்வுபெற்ற நீதிபதி தலைமையில் சுதந்திரமான நிரந்தரத் தீர்ப்பாயத்தை உச்ச நீதிமன்றம் பரிந்துரைத்தது.",
                "The court did not recommend abolishing the Tenth Schedule.",
                "பத்தாவது அட்டவணையை ரத்து செய்ய நீதிமன்றம் பரிந்துரைக்கவில்லை.",
                "Did not recommend transferring powers to Governor.",
                "அதிகாரங்களை ஆளுநருக்கு மாற்றப் பரிந்துரைக்கவில்லை.",
                "Did not endorse unrestricted party changes.",
                "கட்டுப்பாடற்ற கட்சி மாற்றங்களை ஆதரிக்கவில்லை.",
                "Keisham Meghachandra (2020) = Independent Tribunal recommended + 3-month timeline.",
                "கீஷம் மேகசந்திரா (2020) = சுதந்திரமான தீர்ப்பாயம் பரிந்துரை + 3 மாத காலக்கெடு.",
                "The court also held that Speaker should ordinarily decide disqualification petitions within 3 months."
            ))
        elif idx == 37:
            q_data.append((
                "Rajya Sabha Elections",
                "In Kuldip Nayar v. Union of India (2006), did the Supreme Court hold that open ballot voting in Rajya Sabha elections attracts Tenth Schedule disqualification?",
                "குல்தீப் நாயர் எதிர் இந்திய ஒன்றியம் (2006) வழக்கில், மாநிலங்களவைத் தேர்தலில் திறந்த வாக்கெடுப்பில் மாறுபட்டு வாக்களிப்பது பத்தாவது அட்டவணை தகுதி நீக்கத்தை ஏற்படுத்தும் என்று உச்ச நீதிமன்றம் கூறியதா?",
                [("No, voting contrary to party in Rajya Sabha elections does not attract Tenth Schedule disqualification", "இல்லை, மாநிலங்களவைத் தேர்தலில் கட்சிக்கு எதிராக வாக்களிப்பது பத்தாவது அட்டவணை தகுதி நீக்கத்தை ஏற்படுத்தாது"), ("Yes, it immediately results in disqualification under Paragraph 2(1)(b)", "ஆம், இது உடனடியாக பத்தி 2(1)(b)-ன் கீழ் தகுதி நீக்கத்தை ஏற்படுத்துகிறது"), ("Only if the candidate who was voted against wins the election", "எதிராக வாக்களிக்கப்பட்ட வேட்பாளர் வெற்றி பெற்றால் மட்டுமே தகுதி நீக்கம் ஏற்படும்"), ("Yes, but only if condoned by the Speaker within 15 days", "ஆம், ஆனால் சபாநாயகரால் 15 நாட்களுக்குள் மன்னிக்கப்பட்டால் மட்டுமே")],
                "A",
                "In Kuldip Nayar (2006), the Supreme Court held that election to the Rajya Sabha is not a proceeding in the legislature and voting contrary to party direction does not attract disqualification under the Tenth Schedule.",
                "குல்தீப் நாயர் (2006) வழக்கில், மாநிலங்களவைத் தேர்தல் சட்டமன்ற நடவடிக்கை அல்ல என்றும், கட்சி உத்தரவுக்கு எதிராக வாக்களிப்பது பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கத்தை ஏற்படுத்தாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
                "RS election vote cross-voting does not incur Tenth Schedule disqualification.",
                "மாநிலங்களவை தேர்தலில் கட்சி மாறி வாக்களிப்பது பத்தாவது அட்டவணை தகுதி நீக்கத்தை ஏற்படுத்தாது.",
                "Paragraph 2(1)(b) applies only to proceedings inside the House.",
                "பத்தி 2(1)(b) அவையின் உள்ளே நடக்கும் நடவடிக்கைகளுக்கு மட்டுமே பொருந்தும்.",
                "Result of the candidate is irrelevant to constitutional liability.",
                "வேட்பாளரின் வெற்றி தோல்வி அரசியலமைப்புப் பொறுப்புக்குத் தொடர்பற்றது.",
                "Speaker condonation applies only to Tenth Schedule matters inside the House.",
                "சபாநாயகர் மன்னிப்பு அவைக்குள் நடக்கும் பத்தாவது அட்டவணை விவகாரங்களுக்கு மட்டுமே பொருந்தும்.",
                "Rajya Sabha voting cross-vote != Tenth Schedule defection (Kuldip Nayar 2006).",
                "மாநிலங்களவை தேர்தல் மாற்றி வாக்களிப்பு != பத்தாவது அட்டவணை தகுதி நீக்கம் (குல்தீப் நாயர் 2006).",
                "However, the political party can take internal disciplinary action (like expulsion) against the legislator."
            ))
        elif idx == 38:
            q_data.append((
                "Interim Injunctions",
                "Can courts issue an interim injunction restraining the Speaker from proceeding with a disqualification petition before he makes a final decision?",
                "சபாநாயகர் இறுதி முடிவை எடுப்பதற்கு முன்னதாக, தகுதி நீக்க மனுவை விசாரிப்பதைத் தடுத்து நீதிமன்றங்கள் இடைக்காலத் தடை உத்தரவு பிறப்பிக்க முடியுமா?",
                [("No, courts cannot intervene at an interlocutory stage (no quia timet action)", "முடியாது, இடைக்காலக் கட்டத்தில் நீதிமன்றங்கள் தலையிட முடியாது (முன்னெச்சரிக்கை நடவடிக்கை இல்லை)"), ("Yes, High Court can stay proceedings at any stage", "ஆம், உயர் நீதிமன்றம் எந்தக் கட்டத்திலும் நடவடிக்கைகளுக்குத் தடை விதிக்கலாம்"), ("Yes, on an oral prayer by the affected legislator", "ஆம், பாதிக்கப்பட்ட உறுப்பினர் வாய்மொழியாகக் கோரிக்கை வைத்தால் தடை விதிக்கலாம்"), ("Only if the Supreme Court grants special leave under Article 136", "உறுப்பு 136-ன் கீழ் உச்ச நீதிமன்றம் சிறப்பு விடுப்பு அனுமதித்தால் மட்டுமே")],
                "A",
                "In Kihoto Hollohan (1992), the Supreme Court ruled that judicial review cannot be exercised prior to the making of a decision by the Speaker; no quia timet (anticipatory) action is permissible.",
                "கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில், சபாநாயகர் முடிவு எடுப்பதற்கு முன்னதாக நீதித்துறை மறுஆய்வை மேற்கொள்ள முடியாது என்றும், முன்கூட்டியே தடை உத்தரவு பிறப்பிக்க முடியாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
                "No judicial intervention is permissible until the Speaker renders a final decision.",
                "சபாநாயகர் இறுதி முடிவை வழங்கும் வரை நீதித்துறை தலையீடு செய்ய முடியாது.",
                "High Courts cannot issue interlocutory stays during pendency of petition before Speaker.",
                "சபாநாயகரிடம் மனு நிலுவையில் உள்ள போது உயர் நீதிமன்றங்கள் இடைக்காலத் தடை பிறப்பிக்க முடியாது.",
                "Oral prayers cannot override the constitutional bar.",
                "வாய்மொழிக் கோரிக்கைகள் அரசியலமைப்புத் தடையை மீற முடியாது.",
                "Article 136 also operates after final order.",
                "உறுப்பு 136-ம் இறுதி உத்தரவுக்குப் பிறகே செயல்படுகிறது.",
                "No quia timet action / No stay before Speaker's final decision.",
                "சபாநாயகரின் இறுதி முடிவுக்கு முன் இடைக்காலத் தடை விதிக்க முடியாது.",
                "An exception exists only where there is grave, imminent, and irreparable injury."
            ))
        elif idx == 39:
            q_data.append((
                "Subhash Desai Case 2023",
                "In the 2023 Maharashtra Political Crisis case (Subhash Desai v. Principal Secretary to Governor), who did the Supreme Court hold has the authority to appoint the Whip?",
                "2023 மகாராஷ்டிரா அரசியல் நெருக்கடி வழக்கில் (சுபாஷ் தேசாய் எதிர் ஆளுநரின் முதன்மைச் செயலாளர்), கொறடாவை நியமிக்கும் அதிகாரம் யாருக்கு இருப்பதாக உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
                [("The Political Party, not the Legislature Party", "அரசியல் கட்சிக்கு மட்டுமே, சட்டமன்றக் கட்சிக்கு அல்ல"), ("The Legislature Party independently", "சட்டமன்றக் கட்சிக்குத் தன்னிச்சையாக"), ("The Speaker of the Assembly", "சட்டமன்ற சபாநாயகருக்கு"), ("The Governor of the State", "மாநில ஆளுநருக்கு")],
                "A",
                "A five-judge Constitution Bench in Subhash Desai (2023) held that the Whip and the Leader of the House must be appointed by the Political Party, not by the Legislature Party acting independently.",
                "சுபாஷ் தேசாய் (2023) வழக்கில் ஐந்து நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு, கொறடாவும் அவைத் தலைவரும் அரசியல் கட்சியால் மட்டுமே நியமிக்கப்பட வேண்டும், சட்டமன்றக் கட்சியால் தன்னிச்சையாக அல்ல என்று தீர்ப்பளித்தது.",
                "Political Party supremacy over Legislature Party was reaffirmed in Subhash Desai (2023).",
                "சட்டமன்றக் கட்சியை விட அரசியல் கட்சியே மேலானது என்பது சுபாஷ் தேசாய் (2023) வழக்கில் மீண்டும் உறுதிப்படுத்தப்பட்டது.",
                "Legislature Party is a creature of the Political Party and cannot act autonomously.",
                "சட்டமன்றக் கட்சி அரசியல் கட்சியின் கீழ் உள்ள அமைப்பாகும், தன்னிச்சையாகச் செயல்பட முடியாது.",
                "Speaker cannot recognize a Whip appointed without party authorization.",
                "கட்சி அங்கீகாரம் இல்லாமல் நியமிக்கப்பட்ட கொறடாவை சபாநாயகர் அங்கீகரிக்க முடியாது.",
                "Governor has no role in appointing or approving party whips.",
                "கட்சி கொறடாக்களை நியமிப்பதில் அல்லது அங்கீகரிப்பதில் ஆளுநருக்குப் பங்கில்லை.",
                "Whip appointed by Political Party, NOT Legislature Party (Subhash Desai 2023).",
                "கொறடாவை நியமிப்பது அரசியல் கட்சி, சட்டமன்றக் கட்சி அல்ல (சுபாஷ் தேசாய் 2023).",
                "To hold otherwise would sever the umbilical cord between the party and its elected legislators."
            ))
        elif idx == 40:
            q_data.append((
                "Anti-Defection Objectives",
                "What was the primary objective of introducing the Tenth Schedule in the Indian Constitution?",
                "இந்திய அரசியலமைப்பில் பத்தாவது அட்டவணையை அறிமுகப்படுத்தியதன் முதன்மையான நோக்கம் என்ன?",
                [("To curb political defections motivated by lure of office or other considerations and ensure stability", "பதவி ஆசை அல்லது பிற காரணங்களால் தூண்டப்படும் அரசியல் கட்சித் தாவல்களைத் தடுத்து அரசியல் நிலைத்தன்மையை உறுதி செய்தல்"), ("To eliminate political parties completely from Indian democracy", "இந்திய ஜனநாயகத்திலிருந்து அரசியல் கட்சிகளை முற்றிலுமாக ஒழித்தல்"), ("To ban coalition governments in States", "மாநிலங்களில் கூட்டாட்சி அல்லது கூட்டணிகளைத் தடை செய்தல்"), ("To make the Speaker of the House immune from all court proceedings", "அவை சபாநாயகரை அனைத்து நீதிமன்ற நடவடிக்கைகளிலிருந்தும் பாதுகாத்தல்")],
                "A",
                "The Statement of Objects and Reasons of the 52nd Amendment Act stated that the evil of political defections had become a matter of national concern and the amendment aimed to curb it to ensure legislative stability.",
                "52-வது திருத்தச் சட்டத்தின் நோக்கங்கள் மற்றும் காரணங்கள் அறிக்கையில், அரசியல் கட்சித் தாவல் என்ற தீமை தேசியக் கவலையாக மாறியுள்ளது என்றும், சட்டமன்ற நிலைத்தன்மையை உறுதி செய்ய அதைத் தடுப்பதே இதன் நோக்கம் என்றும் கூறப்பட்டது.",
                "Core objective: combat opportunistic political defections and provide stability.",
                "முக்கிய நோக்கம்: சந்தர்ப்பவாத கட்சித் தாவல்களைத் தடுத்து நிலைத்தன்மையை வழங்குதல்.",
                "It strengthened party system, never aimed to eliminate political parties.",
                "இது கட்சி முறையை வலுப்படுத்தியது, கட்சிகளை ஒழிக்க முயலவில்லை.",
                "Coalition governments are legitimate and not banned by Tenth Schedule.",
                "கூட்டணி அரசுகள் சட்டப்பூர்வமானவை மற்றும் பத்தாவது அட்டவணையால் தடை செய்யப்படவில்லை.",
                "Speaker's decisions are subject to judicial review, not completely immune.",
                "சபாநாயகரின் முடிவுகள் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை, முற்றிலும் விலக்கு பெற்றவை அல்ல.",
                "Primary Objective = Curb opportunistic defections & ensure stability.",
                "முதன்மை நோக்கம் = சந்தர்ப்பவாத கட்சித் தாவல்களைத் தடுத்து நிலைத்தன்மையை ஏற்படுத்துதல்.",
                "It was designed to protect the mandate given by the voters to the party on whose ticket the candidate was elected."
            ))
        elif idx == 41:
            q_data.append((
                "Application to J&K",
                "Did the Tenth Schedule originally apply to the State of Jammu and Kashmir when enacted in 1985?",
                "1985-ல் இயற்றப்பட்டபோது பத்தாவது அட்டவணை தொடக்கத்தில் ஜம்மு காஷ்மீர் மாநிலத்திற்குப் பொருந்தக்கூடியதாக இருந்ததா?",
                [("No, Jammu and Kashmir had its own Constitution and added defection provisions separately", "இல்லை, ஜம்மு காஷ்மீர் தனக்கான தனி அரசியலமைப்பைக் கொண்டிருந்தது மற்றும் தனித்தனியாக கட்சித் தாவல் விதிகளைச் சேர்த்தது"), ("Yes, it automatically applied to all States including Jammu and Kashmir", "ஆம், அது ஜம்மு காஷ்மீர் உட்பட அனைத்து மாநிலங்களுக்கும் தானாகவே பொருந்தியது"), ("Yes, because Article 370 was suspended in 1985", "ஆம், ஏனெனில் உறுப்பு 370 1985-ல் இடைநிறுத்தப்பட்டது"), ("No, J&K was permanently exempt until 2047", "இல்லை, ஜம்மு காஷ்மீருக்கு 2047 வரை நிரந்தர விலக்கு அளிக்கப்பட்டது")],
                "A",
                "Due to Article 370, constitutional amendments did not automatically apply to J&K unless extended by Presidential Order; J&K incorporated anti-defection provisions into Section 24G of the J&K Representation of the People Act 1957.",
                "உறுப்பு 370 காரணமாக, குடியரசுத் தலைவர் உத்தரவின்றி அரசியலமைப்புத் திருத்தங்கள் ஜம்மு காஷ்மீருக்கு தானாகப் பொருந்தாது; ஜம்மு காஷ்மீர் தனது 1957 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 24G-ல் கட்சித் தாவல் விதிகளைச் சேர்த்தது.",
                "Tenth Schedule did not directly apply to J&K Assembly until 2019 reorganization.",
                "2019 மறுசீரமைப்பு வரை பத்தாவது அட்டவணை ஜம்மு காஷ்மீர் சட்டமன்றத்திற்கு நேரடியாகப் பொருந்தவில்லை.",
                "Did not automatically apply across the board to J&K state assembly.",
                "ஜம்மு காஷ்மீர் சட்டமன்றத்திற்கு தானாகவே முழுமையாகப் பொருந்தவில்லை.",
                "Article 370 was not suspended in 1985.",
                "1985-ல் உறுப்பு 370 இடைநிறுத்தப்படவில்லை.",
                "There was no 2047 sunset clause.",
                "2047 வரை எந்த விலக்கும் அளிக்கப்படவில்லை.",
                "J&K had separate state defection provisions under its own law.",
                "ஜம்மு காஷ்மீர் தனது சொந்த சட்டத்தின் கீழ் தனித்த கட்சித் தாவல் விதிகளைக் கொண்டிருந்தது.",
                "With the J&K Reorganisation Act 2019, the Tenth Schedule applies directly."
            ))
        elif idx == 42:
            q_data.append((
                "Dinesh Goswami Committee",
                "What was the key recommendation of the Dinesh Goswami Committee on Electoral Reforms (1990) regarding the Anti-Defection Law?",
                "கட்சித் தாவல் தடைச் சட்டம் தொடர்பாக தினேஷ் கோஸ்வாமி தேர்தல் சீர்திருத்தக் குழுவின் (1990) முக்கியப் பரிந்துரை என்ன?",
                [("Disqualification should be decided by the President/Governor on the advice of the Election Commission", "தகுதி நீக்கம் தேர்தல் ஆணையத்தின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர்/ஆளுநரால் தீர்மானிக்கப்பட வேண்டும்"), ("Disqualification power should be given exclusively to political party presidents", "தகுதி நீக்க அதிகாரம் அரசியல் கட்சித் தலைவர்களுக்கு மட்டுமே வழங்கப்பட வேண்டும்"), ("Whips should be abolished for all parliamentary voting", "அனைத்து நாடாளுமன்ற வாக்கெடுப்புகளுக்கும் கொறடா முறை ஒழிக்கப்பட வேண்டும்"), ("All defectors should be permanently banned from public life", "கட்சி தாவியவர்கள் அனைவரும் பொது வாழ்விலிருந்து நிரந்தரமாகத் தடை செய்யப்பட வேண்டும்")],
                "A",
                "The Dinesh Goswami Committee (1990) recommended that the power to decide disqualification under the Tenth Schedule should be vested in the President/Governor acting on the advice of the Election Commission, rather than the Speaker.",
                "தினேஷ் கோஸ்வாமி குழு (1990) பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கம் செய்யும் அதிகாரம் சபாநாயகரிடம் இருப்பதை விட, தேர்தல் ஆணையத்தின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர்/ஆளுநரிடம் ஒப்படைக்கப்பட வேண்டும் என்று பரிந்துரைத்தது.",
                "Dinesh Goswami recommended shifting deciding power to President/ECI.",
                "தீர்மானிக்கும் அதிகாரத்தை குடியரசுத் தலைவர்/தேர்தல் ஆணையத்திடம் மாற்ற தினேஷ் கோஸ்வாமி பரிந்துரைத்தார்.",
                "Did not recommend empowering party presidents.",
                "கட்சித் தலைவர்களுக்கு அதிகாரம் அளிக்கப் பரிந்துரைக்கவில்லை.",
                "Did not propose total abolition of whips.",
                "கொறடா முறையை முழுமையாக ஒழிக்க முன்மொழியவில்லை.",
                "Did not propose permanent lifetime ban.",
                "வாழ்நாள் தடையை முன்மொழியவில்லை.",
                "Dinesh Goswami (1990) = Transfer defection deciding power to President on ECI advice.",
                "தினேஷ் கோஸ்வாமி (1990) = தேர்தல் ஆணைய ஆலோசனைப்படி குடியரசுத் தலைவரிடம் அதிகாரம் மாற்றுதல்.",
                "The Election Commission of India also consistently supports this recommendation."
            ))
        elif idx == 43:
            q_data.append((
                "Law Commission 170th Report",
                "What did the Law Commission of India recommend in its 170th Report (1999) regarding the Tenth Schedule?",
                "பத்தாவது அட்டவணை தொடர்பாக இந்திய சட்ட ஆணையம் தனது 170-வது அறிக்கையில் (1999) என்ன பரிந்துரைத்தது?",
                [("Deletion of the split provision and barring pre-poll electoral fronts from splitting", "பிளவு விதியை நீக்குதல் மற்றும் தேர்தலுக்கு முந்தைய தேர்தல் கூட்டணிகள் பிரிவதைத் தடுத்தல்"), ("Complete repeal of the Tenth Schedule", "பத்தாவது அட்டவணையை முழுமையாக ரத்து செய்தல்"), ("Allowing independent members to join political parties freely", "சுயேச்சை உறுப்பினர்கள் சுதந்திரமாகக் கட்சிகளில் சேர அனுமதித்தல்"), ("Mandating that all bills require a three-line whip", "அனைத்து மசோதாக்களுக்கும் மூன்று-வரிக் கொறடாவைக் கட்டாயமாக்குதல்")],
                "A",
                "The Law Commission's 170th Report (1999) recommended deleting the exemption for splits (Paragraph 3) and treating pre-poll alliances as single political parties under the Tenth Schedule.",
                "சட்ட ஆணையத்தின் 170-வது அறிக்கை (1999) பிளவுக்கான விலக்கை (பத்தி 3) நீக்கவும், தேர்தலுக்கு முந்தைய கூட்டணிகளை பத்தாவது அட்டவணையின் கீழ் ஒரே அரசியல் கட்சியாகக் கருதவும் பரிந்துரைத்தது.",
                "Law Commission 170th Report (1999) laid the groundwork for the 91st CAA 2003.",
                "சட்ட ஆணையத்தின் 170-வது அறிக்கை (1999) 91-வது திருத்தச் சட்டம் 2003-க்கான அடித்தளத்தை அமைத்தது.",
                "Law Commission did not recommend repealing the anti-defection framework.",
                "சட்ட ஆணையம் கட்சித் தாவல் தடுப்புச் சட்டத்தை ரத்து செய்யப் பரிந்துரைக்கவில்லை.",
                "Did not recommend allowing independent members to join parties.",
                "சுயேச்சைகள் கட்சிகளில் சேர அனுமதிக்கப் பரிந்துரைக்கவில்லை.",
                "Did not mandate three-line whip for all bills.",
                "அனைத்து மசோதாக்களுக்கும் மூன்று-வரிக் கொறடாவைக் கட்டாயமாக்கவில்லை.",
                "Law Commission 170th Report (1999) = Delete split defense.",
                "சட்ட ஆணையம் 170-வது அறிக்கை (1999) = பிளவுப் பாதுகாப்பை நீக்குதல்.",
                "This recommendation was largely implemented by the 91st Amendment Act 2003."
            ))
        elif idx == 44:
            q_data.append((
                "NCRWC Recommendations",
                "What threshold for defection did the National Commission to Review the Working of the Constitution (NCRWC, 2002) recommend?",
                "அரசியலமைப்புச் செயல்பாட்டை மறுஆய்வு செய்வதற்கான தேசிய ஆணையம் (NCRWC, 2002) கட்சித் தாவல் குறித்து என்ன பரிந்துரைத்தது?",
                [("A defector should be debarred from holding any public office of minister or remunerative political post", "கட்சி தாவியவர் அமைச்சர் பதவியையோ அல்லது எந்தவொரு ஊதியம் பெறும் அரசியல் பதவியையோ வகிக்கத் தடை விதிக்கப்பட வேண்டும்"), ("Defectors should be awarded ministerial posts immediately to test popularity", "செல்வாக்கைச் சோதிக்க கட்சி தாவியவர்களுக்கு உடனடியாக அமைச்சர் பதவி வழங்கப்பட வேண்டும்"), ("Defection should only be penalized if money transfer is proved in court", "நீதிமன்றத்தில் பணப் பரிமாற்றம் நிரூபிக்கப்பட்டால் மட்டுமே கட்சித் தாவல் தண்டிக்கப்பட வேண்டும்"), ("Only female legislators should be exempted from defection law", "பெண் சட்டமன்ற உறுப்பினர்களுக்கு மட்டுமே கட்சித் தாவல் சட்டத்திலிருந்து விலக்கு அளிக்கப்பட வேண்டும்")],
                "A",
                "The NCRWC (Venkatachaliah Commission, 2002) recommended that a defector should be debarred from holding any public office as a minister or other remunerative political post for the remaining term.",
                "என்.சி.ஆர்.டபிள்யூ.சி (வெங்கடாசலையா ஆணையம், 2002) கட்சி தாவியவர் தனது எஞ்சிய பதவிக்காலத்திற்கு அமைச்சர் பதவியையோ அல்லது பிற ஊதியம் பெறும் அரசியல் பதவியையோ வகிக்கத் தடை விதிக்கப்பட வேண்டும் என்று பரிந்துரைத்தது.",
                "NCRWC recommendations directly shaped Articles 75(1B), 164(1B), and 361B in 2003.",
                "என்.சி.ஆர்.டபிள்யூ.சி பரிந்துரைகள் 2003-ல் உறுப்புகள் 75(1B), 164(1B), மற்றும் 361B ஆகியவற்றிற்கு நேரடி அடிப்படையாக அமைந்தன.",
                "Rewarding defectors was contrary to the Commission's philosophy.",
                "கட்சி தாவியவர்களுக்குப் பரிசு வழங்குவது ஆணையத்தின் நோக்கத்திற்கு எதிரானது.",
                "Defection is a constitutional status, not a criminal proof of bribery.",
                "கட்சித் தாவல் என்பது ஓர் அரசியலமைப்பு தகுதியிழப்பு, லஞ்ச நிரூபணம் அல்ல.",
                "Gender-based exemption is unconstitutional under Article 15.",
                "பாலின அடிப்படையிலான விலக்கு உறுப்பு 15-ன் கீழ் அரசியலமைப்புக்கு எதிரானது.",
                "NCRWC 2002 = Bar defectors from ministerial and remunerative posts.",
                "என்.சி.ஆர்.டபிள்யூ.சி 2002 = கட்சி தாவியவர்கள் அமைச்சர் மற்றும் ஊதியப் பதவிகள் வகிக்கத் தடை.",
                "Headed by Justice M.N. Venkatachaliah, former Chief Justice of India."
            ))
        elif idx == 45:
            q_data.append((
                "Voluntary Giving Up Scope",
                "Does a public letter addressed to the Governor withdrawing support from one's own party's government constitute defection?",
                "சொந்தக் கட்சி அரசுக்கு அளித்து வந்த ஆதரவை விலக்கிக் கொள்வதாக ஆளுநருக்கு பொதுக் கடிதம் அளிப்பது கட்சித் தாவலாகக் கருதப்படுமா?",
                [("Yes, it indicates voluntarily giving up party membership by conduct", "ஆம், இது நடத்தை மூலம் கட்சியின் உறுப்பினர் பதவியைத் தானாகத் துறந்ததாகக் குறிக்கிறது"), ("No, as long as the member has not submitted a resignation letter to the party president", "இல்லை, உறுப்பினர் கட்சித் தலைவரிடம் ராஜினாமா கடிதம் அளிக்காத வரை அவ்வாறு கருதப்படாது"), ("No, a member has absolute freedom to write any letter to the Governor", "இல்லை, ஆளுநருக்கு எந்தக் கடிதத்தையும் எழுத உறுப்பினருக்கு முழு உரிமை உண்டு"), ("Only if the letter is co-signed by the Leader of Opposition", "கடிதத்தில் எதிர்க்கட்சித் தலைவர் கையெழுத்திட்டிருந்தால் மட்டுமே")],
                "A",
                "In Rajendra Singh Rana v. Swami Prasad Maurya (2007), the Supreme Court held that writing to the Governor asking to invite the opposition to form a government clearly proves that the members voluntarily gave up party membership.",
                "ராஜேந்திர சிங் ராணா எதிர் சுவாமி பிரசாத் மவுரியா (2007) வழக்கில், எதிர்க்கட்சியை ஆட்சி அமைக்க அழைக்குமாறு ஆளுநருக்குக் கடிதம் எழுதுவது உறுப்பினர்கள் தானாகவே கட்சி உறுப்பினர் பதவியைத் துறந்துவிட்டதை நிரூபிக்கிறது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
                "Conduct of withdrawing support to the Governor amounts to voluntary defection.",
                "ஆளுநரிடம் சென்று ஆதரவை விலக்கிக் கொள்ளும் நடத்தை தானாக கட்சித் தாவியதாகக் கருதப்படும்.",
                "Formal written resignation to the party is not a required prerequisite.",
                "கட்சிக்கு முறையான எழுத்துப்பூர்வ ராஜினாமா அளித்திருக்க வேண்டும் என்ற கட்டாயம் இல்லை.",
                "Right to address Governor does not shield a legislator from anti-defection consequences.",
                "ஆளுநருக்கு எழுதும் உரிமை கட்சித் தாவல் விளைவுகளிலிருந்து பாதுகாக்காது.",
                "Co-signature by opposition is not the legal test.",
                "எதிர்க்கட்சியின் கையொப்பம் இதற்கான சட்டப் பரிசோதனை அல்ல.",
                "Withdrawing support via letter to Governor = Defection (Rajendra Singh Rana 2007).",
                "ஆளுநருக்குக் கடிதம் மூலம் ஆதரவை விலக்குதல் = கட்சித் தாவல் (ராஜேந்திர சிங் ராணா 2007).",
                "The Supreme Court itself disqualified the 13 BSP MLAs in Uttar Pradesh in that judgment."
            ))
        elif idx == 46:
            q_data.append((
                "Speaker's Office Immunity",
                "Under Article 212 of the Constitution, proceedings of the legislature cannot be called in question on the ground of:",
                "அரசியலமைப்பின் 212-வது உறுப்பின் கீழ், சட்டமன்றத்தின் நடவடிக்கைகள் எந்தக் காரணத்திற்காக நீதிமன்றத்தால் கேள்விக்குட்படுத்தப்பட முடியாது?",
                [("Any alleged irregularity of procedure", "நடைமுறையில் ஏற்பட்டதாகக் கூறப்படும் ஏதேனும் முறைகேடு"), ("Substantive illegality or unconstitutionality", "அடிப்படைக் சட்டவிரோதம் அல்லது அரசியலமைப்பு முரண்பாடு"), ("Violation of fundamental rights", "அடிப்படை உரிமைகள் மீறல்"), ("Gross mala fides of the presiding officer", "அவைத் தலைவரின் வெளிப்படையான உள்நோக்கம்")],
                "A",
                "Article 212(1) (and Article 122(1) for Parliament) immunizes legislative proceedings from judicial inquiry solely on the ground of 'any alleged irregularity of procedure', but not for substantive illegality or constitutional violations.",
                "உறுப்பு 212(1) (நாடாளுமன்றத்திற்கு உறுப்பு 122(1)) 'நடைமுறையில் ஏற்பட்ட முறைகேடு' என்ற காரணத்திற்காக மட்டுமே சட்டமன்ற நடவடிக்கைகளுக்கு நீதிமன்ற விசாரணையிலிருந்து பாதுகாப்பு அளிக்கிறது, ஆனால் அடிப்படைக் சட்டவிரோதத்திற்கு அல்ல.",
                "Immunity is strictly confined to procedural irregularities.",
                "பாதுகாப்பு நடைமுறை முறைகேடுகளுக்கு மட்டுமே மட்டுப்படுத்தப்பட்டுள்ளது.",
                "Substantive illegality is open to judicial review.",
                "சட்டவிரோதம் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.",
                "Violation of fundamental rights allows judicial review.",
                "அடிப்படை உரிமை மீறல்கள் நீதித்துறை மறுஆய்வை அனுமதிக்கின்றன.",
                "Mala fides can be challenged in court under Kihoto Hollohan principles.",
                "உள்நோக்கத்தைக் கிஹோட்டோ ஹோல்லோஹன் கொள்கைகளின் கீழ் நீதிமன்றத்தில் சவாலுக்கு உட்படுத்தலாம்.",
                "Art 212 immunity = Irregularity of procedure only.",
                "உறுப்பு 212 பாதுகாப்பு = நடைமுறை ஒழுங்கின்மைக்கு மட்டுமே.",
                "In Kihoto Hollohan, the SC held that a decision of the Speaker can be challenged on ultra vires, mala fides, and natural justice."
            ))
        elif idx == 47:
            q_data.append((
                "Time Frame for Speaker",
                "Does the Tenth Schedule of the Constitution prescribe any specific time limit for the Speaker to decide a disqualification petition?",
                "பத்தாவது அட்டவணை சபாநாயகர் தகுதி நீக்க மனுவைத் தீர்மானிக்க ஏதேனும் குறிப்பிட்ட காலக்கெடுவை நிர்ணயித்துள்ளதா?",
                [("No specific time limit is prescribed in the text of the Tenth Schedule", "பத்தாவது அட்டவணையின் உரையில் குறிப்பிட்ட காலக்கெடு எதுவும் நிர்ணயிக்கப்படவில்லை"), ("Yes, exactly 30 days from filing", "ஆம், தாக்கல் செய்த நாளிலிருந்து சரியாக 30 நாட்கள்"), ("Yes, exactly 6 months from filing", "ஆம், தாக்கல் செய்த நாளிலிருந்து சரியாக 6 மாதங்கள்"), ("Yes, before the end of the current legislative session", "ஆம், தற்போதைய சட்டமன்ற கூட்டத்தொடர் முடிவதற்குள்")],
                "A",
                "The Tenth Schedule does not mention any explicit time limit for the Speaker to decide petitions, which historically enabled presiding officers to delay decisions until judicial intervention in Keisham Meghachandra (2020).",
                "பத்தாவது அட்டவணையில் சபாநாயகர் மனுக்களைத் தீர்மானிக்க வெளிப்படையான காலக்கெடு எதுவும் குறிப்பிடப்படவில்லை; இது வரலாற்று ரீதியாக முடிவுகளைத் தாமதப்படுத்த வழிவகுத்தது, பின்னர் கீஷம் மேகசந்திரா (2020) வழக்கில் நீதிமன்றம் தலையிட்டது.",
                "The constitutional text is silent on time frame for the Speaker.",
                "அரசியலமைப்பு உரையில் சபாநாயகருக்கான காலக்கெடு எதுவும் குறிப்பிடப்படவில்லை.",
                "30 days is for laying of rules under Paragraph 8.",
                "30 நாட்கள் என்பது பத்தி 8-ன் கீழ் விதிகளைச் சமர்ப்பிப்பதற்கான காலமாகும்.",
                "6 months is the window for nominated members to join a party.",
                "6 மாதங்கள் என்பது நியமன உறுப்பினர்கள் கட்சியில் சேருவதற்கான காலமாகும்.",
                "There is no rule requiring disposal before session end.",
                "கூட்டத்தொடர் முடிவதற்குள் முடிக்க வேண்டும் என்ற விதி இல்லை.",
                "No constitutional time limit in 10th Schedule text (ordinarily 3 months via judicial precedent).",
                "10-வது அட்டவணை உரையில் காலக்கெடு இல்லை (நீதிமன்றத் தீர்ப்பு மூலம் வழக்கமாக 3 மாதங்கள்).",
                "The lack of a timeline in the text has been a primary source of political controversy."
            ))
        elif idx == 48:
            q_data.append((
                "Split Defense Deletion",
                "Prior to the 91st Constitutional Amendment Act 2003, what proportion of members splitting from a party was protected under Paragraph 3?",
                "2003-ஆம் ஆண்டின் 91-வது திருத்தச் சட்டத்திற்கு முன்பு, பத்தி 3-ன் கீழ் ஒரு கட்சியிலிருந்து எத்தனை பங்கு உறுப்பினர்கள் பிளவுபட்டால் தகுதி நீக்கத்திலிருந்து பாதுகாப்பு இருந்தது?",
                [("Not less than one-third (1/3rd) of the legislature party", "சட்டமன்றக் கட்சியில் மூன்றில் ஒரு பங்குக்கு (1/3) குறையாதவர்கள்"), ("Not less than one-half (1/2) of the legislature party", "சட்டமன்றக் கட்சியில் பாதிக்குக் குறையாதவர்கள்"), ("Not less than one-fourth (1/4th) of the legislature party", "சட்டமன்றக் கட்சியில் நான்கில் ஒரு பங்குக்குக் குறையாதவர்கள்"), ("Not less than two-thirds (2/3rd) of the legislature party", "சட்டமன்றக் கட்சியில் மூன்றில் இரண்டு பங்குக்குக் குறையாதவர்கள்")],
                "A",
                "Before its deletion in 2003, Paragraph 3 protected members from disqualification if there was a split in their original party and the faction consisted of not less than one-third of the members of the legislature party.",
                "2003-ல் நீக்கப்படுவதற்கு முன்பு, மூலக் கட்சியில் பிளவு ஏற்பட்டு, அப்பிரிவில் சட்டமன்றக் கட்சியின் மூன்றில் ஒரு பங்குக்குக் குறையாத உறுப்பினர்கள் இருந்தால் அவர்களுக்கு பத்தி 3 பாதுகாப்பு அளித்தது.",
                "One-third split was protected under the original 1985 text (Paragraph 3).",
                "மூன்றில் ஒரு பங்கு பிளவு அசல் 1985 உரையில் (பத்தி 3) பாதுகாக்கப்பட்டது.",
                "One-half was never the threshold for split.",
                "பாதி என்பது பிளவுக்கான வரம்பாக ஒருபோதும் இருந்ததில்லை.",
                "One-fourth was not a threshold in Tenth Schedule.",
                "நான்கில் ஒரு பங்கு பத்தாவது அட்டவணையில் ஒரு வரம்பல்ல.",
                "Two-thirds applies to mergers under Paragraph 4, not split under deleted Paragraph 3.",
                "மூன்றில் இரண்டு பங்கு பத்தி 4-ன் கீழ் இணைப்புகளுக்குப் பொருந்தும், நீக்கப்பட்ட பத்தி 3-ன் கீழ் பிளவுக்கு அல்ல.",
                "Old split threshold = 1/3rd (Deleted by 91st CAA 2003).",
                "பழைய பிளவு வரம்பு = 1/3 (91-வது திருத்தம் 2003 மூலம் நீக்கப்பட்டது).",
                "This provision was misused for wholesale engineered defections, leading to its complete repeal."
            ))
        elif idx == 49:
            q_data.append((
                "Tenth Schedule Paragraph Count",
                "How many Paragraphs does the Tenth Schedule of the Constitution currently contain?",
                "இந்திய அரசியலமைப்பின் பத்தாவது அட்டவணை தற்போது எத்தனை பத்திகளைக் கொண்டுள்ளது?",
                [("8 Paragraphs (with Paragraph 3 deleted and Paragraph 7 declared invalid)", "8 பத்திகள் (பத்தி 3 நீக்கப்பட்டு, பத்தி 7 செல்லாது என அறிவிக்கப்பட்டது)"), ("10 Paragraphs", "10 பத்திகள்"), ("12 Paragraphs", "12 பத்திகள்"), ("5 Paragraphs", "5 பத்திகள்")],
                "A",
                "The Tenth Schedule contains Paragraphs 1 to 8; Paragraph 3 was omitted by the 91st CAA 2003, and Paragraph 7 was struck down by the Supreme Court in Kihoto Hollohan (1992).",
                "பத்தாவது அட்டவணை 1 முதல் 8 வரை பத்திகளைக் கொண்டுள்ளது; பத்தி 3 91-வது திருத்தம் 2003 மூலம் நீக்கப்பட்டது, பத்தி 7 கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில் உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்டது.",
                "Tenth Schedule has 8 numbered paragraphs in total.",
                "பத்தாவது அட்டவணை மொத்தம் 8 எண்ணிடப்பட்ட பத்திகளைக் கொண்டுள்ளது.",
                "10 is not the paragraph count (10 is the Schedule number).",
                "10 என்பது பத்திகளின் எண்ணிக்கை அல்ல (10 என்பது அட்டவணை எண்).",
                "12 is incorrect.",
                "12 என்பது தவறானது.",
                "5 is incorrect.",
                "5 என்பது தவறானது.",
                "10th Schedule = 8 Paragraphs (Para 3 deleted, Para 7 unconstitutional).",
                "10-வது அட்டவணை = 8 பத்திகள் (பத்தி 3 நீக்கப்பட்டது, பத்தி 7 செல்லாது).",
                "The operational paragraphs are 1 (interpretation), 2 (disqualification), 4 (merger), 5 (exemption), 6 (decision), and 8 (rules)."
            ))
        elif idx == 50:
            q_data.append((
                "Whip Scope",
                "Can a political party issue a whip to its members to vote in a particular manner during the election of the President of India?",
                "இந்தியக் குடியரசுத் தலைவர் தேர்தலின் போது ஒரு குறிப்பிட்ட முறையில் வாக்களிக்குமாறு ஓர் அரசியல் கட்சி தனது உறுப்பினர்களுக்கு கொறடா உத்தரவு பிறப்பிக்க முடியுமா?",
                [("No, political parties cannot issue whips in Presidential elections", "முடியாது, குடியரசுத் தலைவர் தேர்தலில் அரசியல் கட்சிகள் கொறடா உத்தரவு பிறப்பிக்க முடியாது"), ("Yes, a three-line whip must be issued by every national party", "ஆம், ஒவ்வொரு தேசியக் கட்சியும் மூன்று-வரிக் கொறடாவைக் கண்டிப்பாக வெளியிட வேண்டும்"), ("Yes, violation results in automatic disqualification under Tenth Schedule", "ஆம், மீறினால் பத்தாவது அட்டவணையின் கீழ் தானாகவே தகுதி நீக்கம் ஏற்படும்"), ("Only if the Election Commission grants prior approval", "தேர்தல் ஆணையம் முன்அனுமதி அளித்தால் மட்டுமே")],
                "A",
                "The Election Commission and Supreme Court have repeatedly clarified that elections to the office of the President and Vice-President are conducted by secret ballot under separate statutes, and political parties cannot issue whips to electors.",
                "குடியரசுத் தலைவர் மற்றும் குடியரசுத் துணைத் தலைவர் தேர்தல்கள் தனிச் சட்டங்களின் கீழ் ரகசிய வாக்கெடுப்பு மூலம் நடத்தப்படுகின்றன என்றும், அரசியல் கட்சிகள் வாக்காளர்களுக்கு கொறடா உத்தரவு பிறப்பிக்க முடியாது என்றும் தேர்தல் ஆணையமும் உச்ச நீதிமன்றமும் மீண்டும் மீண்டும் தெளிவுபடுத்தியுள்ளன.",
                "No whip is permitted in Presidential / Vice-Presidential elections.",
                "குடியரசுத் தலைவர் / குடியரசுத் துணைத் தலைவர் தேர்தல்களில் கொறடா உத்தரவு அனுமதிக்கப்படுவதில்லை.",
                "No national party can issue a legally binding whip for Presidential poll.",
                "குடியரசுத் தலைவர் தேர்தலில் எந்தவொரு தேசியக் கட்சியும் சட்டப்பூர்வ கொறடாவை வெளியிட முடியாது.",
                "No defection applies to secret ballot voting in Presidential elections.",
                "குடியரசுத் தலைவர் தேர்தலில் ரகசிய வாக்கெடுப்பில் வாக்களிப்பது கட்சித் தாவல் சட்டத்திற்கு உட்படாது.",
                "Election Commission does not grant approval for whips in secret ballot elections.",
                "ரகசிய வாக்கெடுப்புத் தேர்தல்களில் கொறடா வெளியிட தேர்தல் ஆணையம் அனுமதிப்பதில்லை.",
                "No whip in Presidential or Vice-Presidential elections.",
                "குடியரசுத் தலைவர் அல்லது குடியரசுத் துணைத் தலைவர் தேர்தலில் கொறடா உத்தரவு செல்லாது.",
                "Members are free to vote according to their conscience without fear of Tenth Schedule disqualification."
            ))

    for item in q_data:
        raw_easy.append({
            "subtopic": item[0],
            "stem_en": item[1],
            "stem_ta": item[2],
            "options": item[3],
            "correct_key": item[4],
            "exp_en": item[5],
            "exp_ta": item[6],
            "why_a_en": item[7],
            "why_a_ta": item[8],
            "why_b_en": item[9],
            "why_b_ta": item[10],
            "why_c_en": item[11],
            "why_c_ta": item[12],
            "why_d_en": item[13],
            "why_d_ta": item[14],
            "tip_en": item[15],
            "tip_ta": item[16],
            "fact_en": item[17],
            "fact_ta": item[18] if len(item) > 18 else item[16]
        })


raw_easy = get_easy_raw()
get_remaining_easy_questions()


def build_easy_file():
    print(f"Loaded {len(raw_easy)} raw Easy questions for Anti-Defection Law.")
    assert len(raw_easy) == 50, f"Expected 50 items, got {len(raw_easy)}"

    questions = []
    for idx, item in enumerate(raw_easy, start=1):
        qid = f"ADL_E_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_adl_q(
            qid=qid,
            diff="Easy",
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
            tags=["polity", "anti_defection_law", "easy", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    balanced = randomize_and_balance_dataset(questions, seed=42)
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "anti_defection_law_easy.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Easy MCQs to {out_path}")

    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="ADL_E_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_easy_file()
    if not success:
        exit(1)
