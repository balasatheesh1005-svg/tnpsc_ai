# -*- coding: utf-8 -*-
"""
Anti-Defection Law - Part 1: Medium (50 MCQs)
TNPSC Nova AI Content Engine

Generates 50 authentic, 24-field bilingual MCQs testing analytical understanding
of the Tenth Schedule, judicial doctrines, procedural nuances, and statutory amendments.
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from anti_defection_law_mcq_helper import make_adl_q


def get_medium_questions():
    raw_medium = [
        {
            "subtopic": "Voluntary Giving Up Membership",
            "stem_en": "An elected legislator publicly campaigns against his own party's official candidate in a general election and supports an opposition candidate, but does not resign from his party. Does this attract disqualification under Paragraph 2(1)(a)?",
            "stem_ta": "தேர்ந்தெடுக்கப்பட்ட ஒரு சட்டமன்ற உறுப்பினர், பொதுத்தேர்தலில் தனது கட்சியின் அதிகாரப்பூர்வ வேட்பாளருக்கு எதிராகப் பகிரங்கமாகப் பிரச்சாரம் செய்து எதிர்க்கட்சி வேட்பாளரை ஆதரிக்கிறார், ஆனால் கட்சியிலிருந்து ராஜினாமா செய்யவில்லை. இது பத்தி 2(1)(a)-ன் கீழ் தகுதி நீக்கத்தை ஏற்படுத்துமா?",
            "options": [
                ("Yes, because voluntarily giving up membership is inferred from anti-party conduct without formal resignation", "ஆம், ஏனெனில் முறையான ராஜினாமா இல்லாமலேயே கட்சி விரோத நடத்தையிலிருந்து தானாக முன்வந்து பதவியைத் துறந்ததாகக் கருதப்படுகிறது"),
                ("No, because disqualification requires a formal written resignation submitted to the party president", "இல்லை, ஏனெனில் தகுதி நீக்கத்திற்கு கட்சித் தலைவரிடம் முறையான எழுத்துப்பூர்வ ராஜினாமா சமர்ப்பிக்கப்பட்டிருக்க வேண்டும்"),
                ("No, because freedom of speech under Article 19(1)(a) protects all public election campaigning", "இல்லை, ஏனெனில் உறுப்பு 19(1)(a)-ன் கீழான பேச்சு சுதந்திரம் அனைத்து தேர்தல் பிரச்சாரங்களையும் பாதுகாக்கிறது"),
                ("Only if the candidate he campaigned against actually loses the election", "அவர் எதிர்த்து பிரச்சாரம் செய்த வேட்பாளர் தேர்தலில் உண்மையாகவே தோற்றால் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "In Ravi S. Naik (1994) and reaffirmed in subsequent rulings, the Supreme Court held that 'voluntarily giving up membership' is not confined to formal resignation; active campaigning against one's own party candidate clearly establishes that the member has severed his political allegiance.",
            "exp_ta": "ரவி எஸ். நாயக் (1994) வழக்கில் உச்ச நீதிமன்றம் தீர்ப்பளித்தபடி, 'தானாக முன்வந்து உறுப்பினர் பதவியைத் துறத்தல்' என்பது முறையான ராஜினாமாவுக்கு மட்டும் மட்டுப்படுத்தப்பட்டதல்ல; தனது சொந்தக் கட்சி வேட்பாளருக்கு எதிராக தீவிர பிரச்சாரம் செய்வது உறுப்பினர் தனது கட்சி விசுவாசத்தைத் துறந்துவிட்டார் என்பதைத் தெளிவாக நிறுவுகிறது.",
            "why_a_en": "Correct. Conduct of working against one's own party candidate constitutes voluntarily giving up membership under Paragraph 2(1)(a).",
            "why_a_ta": "சரி. சொந்தக் கட்சி வேட்பாளருக்கு எதிராகச் செயல்படும் நடத்தை பத்தி 2(1)(a)-ன் கீழ் தானாக உறுப்பினர் பதவியைத் துறந்ததாகக் கருதப்படுகிறது.",
            "why_b_en": "Incorrect. Formal written resignation is not mandatory; conduct suffices.",
            "why_b_ta": "தவறு. முறையான எழுத்துப்பூர்வ ராஜினாமா கட்டாயமில்லை; நடத்தை போதுமானது.",
            "why_c_en": "Incorrect. Legislative discipline under Tenth Schedule operates as a valid constitutional restriction.",
            "why_c_ta": "தவறு. பத்தாவது அட்டவணையின் கீழான சட்டமன்ற ஒழுங்கு ஓர் செல்லுபடியாகும் அரசியலமைப்புக் கட்டுப்பாடாகும்.",
            "why_d_en": "Incorrect. Electoral outcome of the rival candidate is completely irrelevant.",
            "why_d_ta": "தவறு. எதிர்த் தரப்பு வேட்பாளரின் தேர்தல் முடிவு முற்றிலும் தொடர்பற்றது.",
            "tip_en": "Conduct reflecting severance of ties = Voluntary surrender of membership.",
            "tip_ta": "கட்சித் தொடர்பைத் துண்டிக்கும் நடத்தை = தானாக உறுப்பினர் பதவியைத் துறத்தல்.",
            "fact_en": "The Supreme Court in Mahachandra Prasad Singh (2004) reiterated that conduct speaks louder than formal papers.",
            "fact_ta": "மகாசந்திர பிரசாத் சிங் (2004) வழக்கில் முறையான ஆவணங்களை விட நடத்தையே முக்கியமானது என்று உச்ச நீதிமன்றம் மீண்டும் வலியுறுத்தியது."
        },
        {
            "subtopic": "Expulsion vs Tenth Schedule",
            "stem_en": "A member of the Legislative Assembly is expelled from his political party for anti-party activities. What is his exact constitutional status inside the House?",
            "stem_ta": "சட்டமன்ற உறுப்பினர் ஒருவர் கட்சி விரோத நடவடிக்கைகளுக்காக அவரது அரசியல் கட்சியிலிருந்து நீக்கப்படுகிறார். அவைக்குள் அவரது துல்லியமான அரசியலமைப்பு அந்தஸ்து என்ன?",
            "options": [
                ("He remains an elected member of the House, treated as 'unattached', but cannot join another party without facing disqualification", "அவர் அவையின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினராக 'இணைக்கப்படாதவர்' என்று கருதப்பட்டு தொடர்வார், ஆனால் தகுதி நீக்கத்தை சந்திக்காமல் மற்றொரு கட்சியில் இணைய முடியாது"),
                ("He is instantly and automatically disqualified from being an MLA under Paragraph 2(1)(a)", "அவர் பத்தி 2(1)(a)-ன் கீழ் உடனடியாக மற்றும் தானாகவே எம்.எல்.ஏ பதவியிலிருந்து தகுதி நீக்கம் செய்யப்படுகிறார்"),
                ("He is deemed to be a full-fledged Independent member and can join any party he likes", "அவர் முழுமையான சுயேச்சை உறுப்பினராகக் கருதப்பட்டு அவர் விரும்பும் எந்தக் கட்சியிலும் சேரலாம்"),
                ("He loses his voting rights on all constitutional matters but retains his seat", "அவர் அனைத்து அரசியலமைப்பு விவகாரங்களிலும் தனது வாக்குரிமையை இழக்கிறார், ஆனால் தனது பதவியைத் தக்க வைத்துக் கொள்கிறார்")
            ],
            "correct_key": "A",
            "exp_en": "In G. Viswanathan (1996), the Supreme Court ruled that an expelled member is not disqualified from the House merely by virtue of expulsion; he remains an unattached member, but for Tenth Schedule purposes, he is still treated as belonging to his original party, meaning joining another party will attract defection.",
            "exp_ta": "ஜி. விஸ்வநாதன் (1996) வழக்கில், கட்சியால் நீக்கப்பட்ட காரணத்தினால் மட்டுமே ஒருவர் அவையிலிருந்து தகுதி நீக்கம் செய்யப்படுவதில்லை; அவர் 'இணைக்கப்படாத உறுப்பினர்' ஆகத் தொடர்வார், ஆனால் பத்தாவது அட்டவணை நோக்கங்களுக்காக அவர் இன்னும் மூலக் கட்சியைச் சேர்ந்தவராகவே கருதப்படுவார், அதாவது மற்றொரு கட்சியில் சேர்ந்தால் கட்சித் தாவல் தகுதி நீக்கம் ஏற்படும்.",
            "why_a_en": "Correct. An expelled member does not lose his seat but cannot join another party without disqualification.",
            "why_a_ta": "சரி. நீக்கப்பட்ட உறுப்பினர் தனது இடத்தை இழக்க மாட்டார், ஆனால் தகுதி நீக்கமின்றி மற்றொரு கட்சியில் சேர முடியாது.",
            "why_b_en": "Incorrect. Expulsion by a party is an internal party act and does not terminate legislative membership.",
            "why_b_ta": "தவறு. கட்சியால் நீக்கப்படுவது உட்கட்சி நடவடிக்கை மற்றும் சட்டமன்ற உறுப்பினர் பதவியைப் பறிக்காது.",
            "why_c_en": "Incorrect. He is not an independent member elected as such under Paragraph 2(2).",
            "why_c_ta": "தவறு. அவர் பத்தி 2(2)-ன் கீழ் சுயேச்சையாகத் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் அல்ல.",
            "why_d_en": "Incorrect. He retains all constitutional voting rights as an MLA.",
            "why_d_ta": "தவறு. அவர் ஒரு எம்.எல்.ஏ-வாக அனைத்து அரசியலமைப்பு வாக்குரிமைகளையும் தக்க வைத்துக் கொள்கிறார்.",
            "tip_en": "Party expulsion != Legislative disqualification. Joining another party post-expulsion = Disqualification.",
            "tip_ta": "கட்சி நீக்கம் != சட்டமன்ற தகுதியிழப்பு. நீக்கத்திற்குப் பின் மற்றொரு கட்சியில் இணைதல் = தகுதி நீக்கம்.",
            "fact_en": "This prevents political parties from using expulsion to engineer artificial floor majorities.",
            "fact_ta": "இது அரசியல் கட்சிகள் செயற்கையான பெரும்பான்மையை உருவாக்க நீக்கத்தைப் பயன்படுத்துவதைத் தடுக்கிறது."
        },
        {
            "subtopic": "Whip Condonation",
            "stem_en": "An MP votes against his party's three-line whip during a No-Confidence Motion on Day 1. The political party issues a formal letter condoning his action on Day 18. What is the legal consequence?",
            "stem_ta": "ஒரு எம்.பி நாள் 1-ல் நம்பிக்கையில்லாத் தீர்மானத்தின் போது தனது கட்சியின் மூன்று-வரிக் கொறடாவை மீறி வாக்களிக்கிறார். அரசியல் கட்சி நாள் 18-ல் அவரது செயலை மன்னித்து முறையான கடிதம் வெளியிடுகிறது. இதன் சட்டப்பூர்வ விளைவு என்ன?",
            "options": [
                ("The condonation is legally invalid because Paragraph 2(1)(b) mandates condonation within 15 days, so disqualification stands", "மன்னிப்பு சட்டப்படி செல்லாது, ஏனெனில் பத்தி 2(1)(b) 15 நாட்களுக்குள் மன்னிக்கப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது, எனவே தகுதி நீக்கம் உறுதி"),
                ("The condonation is valid because political parties have unlimited time to condone whip violations", "மன்னிப்பு செல்லுபடியாகும், ஏனெனில் கட்சி கொறடா மீறலை மன்னிக்க அரசியல் கட்சிகளுக்கு எல்லையற்ற கால அவகாசம் உள்ளது"),
                ("The Speaker has the discretion to extend the 15-day period up to 30 days on party request", "கட்சியின் கோரிக்கையின் பேரில் 15 நாட்கள் கால அவகாசத்தை 30 நாட்கள் வரை நீட்டிக்க சபாநாயகருக்கு விருப்புரிமை உண்டு"),
                ("The MP is automatically suspended from the House for the remainder of the session without defection", "கட்சித் தாவல் இன்றி கூட்டத்தொடரின் எஞ்சிய காலத்திற்கு அந்த எம்.பி தானாகவே அவையிலிருந்து இடைநீக்கம் செய்யப்படுகிறார்")
            ],
            "correct_key": "A",
            "exp_en": "Paragraph 2(1)(b) of the Tenth Schedule strictly prescribes that the voting or abstention contrary to party direction must be condoned within 15 days. A condonation made on Day 18 is beyond the constitutional limitation period and cannot cure the disqualification.",
            "exp_ta": "பத்தாவது அட்டவணையின் பத்தி 2(1)(b) கட்சி உத்தரவுக்கு எதிரான வாக்களிப்பு அல்லது புறக்கணிப்பு 15 நாட்களுக்குள் மன்னிக்கப்பட வேண்டும் என்று கடுமையாகக் கட்டளையிடுகிறது. 18-வது நாளில் வழங்கப்படும் மன்னிப்பு அரசியலமைப்பு கால வரம்பிற்கு அப்பாற்பட்டது மற்றும் தகுதி நீக்கத்தைத் தவிர்க்க முடியாது.",
            "why_a_en": "Correct. The 15-day condonation window is mandatory and cannot be extended post facto.",
            "why_a_ta": "சரி. 15 நாட்கள் மன்னிப்புக் காலம் கட்டாயமானது மற்றும் பின்னர் நீட்டிக்கப்பட முடியாது.",
            "why_b_en": "Incorrect. The party's power to condone is circumscribed by the constitutional limit of 15 days.",
            "why_b_ta": "தவறு. மன்னிக்கும் கட்சியின் அதிகாரம் 15 நாட்கள் என்ற அரசியலமைப்பு வரம்பிற்கு உட்பட்டது.",
            "why_c_en": "Incorrect. The Tenth Schedule does not confer discretion on the Speaker to enlarge the 15-day statutory window.",
            "why_c_ta": "தவறு. 15 நாட்கள் கால வரம்பை நீட்டிக்க சபாநாயகருக்கு பத்தாவது அட்டவணை விருப்புரிமை அளிக்கவில்லை.",
            "why_d_en": "Incorrect. Disqualification under Tenth Schedule vacates the seat, rather than being a temporary suspension.",
            "why_d_ta": "தவறு. பத்தாவது அட்டவணையின் கீழான தகுதியிழப்பு இடத்தை காலியாக்கும், தற்காலிக இடைநீக்கம் அல்ல.",
            "tip_en": "Day 1 to Day 15: Condonation possible. Day 16 onwards: Defection is incurable.",
            "tip_ta": "நாள் 1 முதல் 15 வரை: மன்னிப்பு சாத்தியம். நாள் 16 முதல்: கட்சித் தாவலை சரிசெய்ய முடியாது.",
            "fact_en": "The 15 days are counted from the exact date of voting or abstention.",
            "fact_ta": "இந்த 15 நாட்கள் வாக்கெடுப்பு அல்லது புறக்கணிப்பு நடந்த சரியான தேதியிலிருந்து கணக்கிடப்படுகின்றன."
        },
        {
            "subtopic": "Merger Calculations",
            "stem_en": "Party X has 60 elected members in a State Legislative Assembly. A faction decides to merge with Party Y. Under Paragraph 4, what is the minimum number of MLAs who must agree to the merger to prevent disqualification?",
            "stem_ta": "ஒரு மாநில சட்டமன்றத்தில் கட்சி X-க்கு 60 தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் உள்ளனர். ஒரு பிரிவு கட்சி Y-யுடன் இணைய முடிவு செய்கிறது. பத்தி 4-ன் கீழ், தகுதி நீக்கத்தைத் தவிர்க்க குறைந்தபட்சம் எத்தனை எம்.எல்.ஏ-க்கள் இணைப்பிற்கு ஒப்புக்கொள்ள வேண்டும்?",
            "options": [
                ("40 MLAs", "40 எம்.எல்.ஏ-க்கள்"),
                ("20 MLAs", "20 எம்.எல்.ஏ-க்கள்"),
                ("30 MLAs", "30 எம்.எல்.ஏ-க்கள்"),
                ("45 MLAs", "45 எம்.எல்.ஏ-க்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Under Paragraph 4(2) of the Tenth Schedule, a merger is deemed to have taken place only if not less than two-thirds (2/3) of the members of the legislature party agree. For a party of 60 members, 2/3 of 60 = 40 members.",
            "exp_ta": "பத்தாவது அட்டவணையின் பத்தி 4(2)-ன் கீழ், சட்டமன்றக் கட்சியின் உறுப்பினர்களில் மூன்றில் இரண்டு பங்குக்கு (2/3) குறையாதவர்கள் ஒப்புக்கொண்டால் மட்டுமே இணைப்பு நடந்ததாகக் கருதப்படும். 60 உறுப்பினர்களைக் கொண்ட கட்சிக்கு, 60-ல் 2/3 = 40 உறுப்பினர்கள்.",
            "why_a_en": "Correct. 2/3rd of 60 is 40 MLAs.",
            "why_a_ta": "சரி. 60-ல் மூன்றில் இரண்டு பங்கு என்பது 40 எம்.எல்.ஏ-க்கள் ஆகும்.",
            "why_b_en": "Incorrect. 20 MLAs would be 1/3rd, which was the old split threshold deleted in 2003.",
            "why_b_ta": "தவறு. 20 எம்.எல்.ஏ-க்கள் என்பது 1/3 பங்கு, இது 2003-ல் நீக்கப்பட்ட பழைய பிளவு வரம்பாகும்.",
            "why_c_en": "Incorrect. 30 MLAs is 50% (one-half), which is insufficient.",
            "why_c_ta": "தவறு. 30 என்பது 50% (பாதி), இது போதுமானதல்ல.",
            "why_d_en": "Incorrect. 45 MLAs represents 3/4th, which exceeds the constitutional requirement of 2/3rd.",
            "why_d_ta": "தவறு. 45 என்பது 3/4 பங்கு, இது அரசியலமைப்புத் தேவையான 2/3-ஐ விட அதிகம்.",
            "tip_en": "Formula: Threshold = Ceil(Total Members * 2/3).",
            "tip_ta": "சூத்திரம்: வரம்பு = (மொத்த உறுப்பினர்கள் * 2/3).",
            "fact_en": "If 40 members agree to merge, neither the 40 merging members nor the remaining 20 members are disqualified.",
            "fact_ta": "40 உறுப்பினர்கள் இணைப்பிற்கு ஒப்புக்கொண்டால், இணையும் 40 பேரும் எஞ்சிய 20 பேரும் தகுதி நீக்கம் செய்யப்பட மாட்டார்கள்."
        },
        {
            "subtopic": "Merger Minority Protection",
            "stem_en": "In the scenario where 40 out of 60 MLAs of Party X merge with Party Y under Paragraph 4, what is the constitutional status of the remaining 20 MLAs who choose NOT to merge?",
            "stem_ta": "பத்தி 4-ன் கீழ் கட்சி X-ன் 60 எம்.எல்.ஏ-க்களில் 40 பேர் கட்சி Y-யுடன் இணையும் போது, இணைய விரும்பாத எஞ்சிய 20 எம்.எல்.ஏ-க்களின் அரசியலமைப்பு அந்தஸ்து என்ன?",
            "options": [
                ("They are NOT disqualified and continue as members of Party X as a separate group", "அவர்கள் தகுதி நீக்கம் செய்யப்பட மாட்டார்கள் மற்றும் ஒரு தனி அமைப்பாக கட்சி X-ன் உறுப்பினர்களாகவே தொடர்வர்"),
                ("They are automatically disqualified for failing to follow the majority merger decision", "பெரும்பான்மை இணைப்பு முடிவைப் பின்பற்றத் தவறியதற்காக அவர்கள் தானாகவே தகுதி நீக்கம் செய்யப்படுகிறார்கள்"),
                ("They are forced by the Speaker to join Party Y within 30 days", "அவர்கள் 30 நாட்களுக்குள் கட்சி Y-யில் சேருமாறு சபாநாயகரால் கட்டாயப்படுத்தப்படுகிறார்கள்"),
                ("They automatically lose their status as MLAs and become nominated members", "அவர்கள் தானாகவே எம்.எல்.ஏ அந்தஸ்தை இழந்து நியமன உறுப்பினர்களாக மாறுகிறார்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Under Paragraph 4(1)(b) of the Tenth Schedule, members who choose not to accept the merger and opt to function as a separate group are explicitly protected from disqualification; they continue as the residual original party.",
            "exp_ta": "பத்தாவது அட்டவணையின் பத்தி 4(1)(b)-ன் படி, இணைப்பை ஏற்காமல் தனி அமைப்பாகச் செயல்பட விரும்பும் உறுப்பினர்கள் தகுதி நீக்கத்திலிருந்து வெளிப்படையாகப் பாதுகாக்கப்படுகிறார்கள்; அவர்கள் மூலக் கட்சியின் எஞ்சிய அமைப்பாகத் தொடர்கின்றனர்.",
            "why_a_en": "Correct. Paragraph 4(1)(b) protects the non-merging minority from disqualification.",
            "why_a_ta": "சரி. பத்தி 4(1)(b) இணையாத சிறுபான்மையினரை தகுதி நீக்கத்திலிருந்து பாதுகாக்கிறது.",
            "why_b_en": "Incorrect. The minority is protected and cannot be forced out of the House.",
            "why_b_ta": "தவறு. சிறுபான்மையினர் பாதுகாக்கப்படுகிறார்கள் மற்றும் அவையிலிருந்து வெளியேற்றப்பட முடியாது.",
            "why_c_en": "Incorrect. Speaker has no constitutional power to compel legislators to join a party.",
            "why_c_ta": "தவறு. சட்டமன்ற உறுப்பினர்களை ஒரு கட்சியில் சேருமாறு கட்டாயப்படுத்த சபாநாயகருக்கு அதிகாரம் இல்லை.",
            "why_d_en": "Incorrect. Elected MLAs cannot be transformed into nominated members.",
            "why_d_ta": "தவறு. தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்களை நியமன உறுப்பினர்களாக மாற்ற முடியாது.",
            "tip_en": "Under Paragraph 4, BOTH the merging 2/3rd majority and the non-merging 1/3rd minority are protected.",
            "tip_ta": "பத்தி 4-ன் கீழ், இணையும் 2/3 பெரும்பான்மை மற்றும் இணையாத 1/3 சிறுபான்மை ஆகிய இரண்டுமே பாதுகாக்கப்படுகின்றன.",
            "fact_en": "Paragraph 4 protects freedom of association: no member can be forced into an unwanted merger against his will.",
            "fact_ta": "பத்தி 4 சங்கங்கள் அமைக்கும் சுதந்திரத்தைப் பாதுகாக்கிறது: எந்தவொரு உறுப்பினரும் விருப்பமின்றி இணைப்பில் ஈடுபட கட்டாயப்படுத்த முடியாது."
        }
    ]

    # Dynamically build remaining 45 medium questions
    medium_specs = [
        # 6: Independent member supporting government
        ("Independent Members Support",
         "Can an independently elected MLA support a ruling coalition government from outside without attracting disqualification under the Tenth Schedule?",
         "ஒரு சுயேச்சை எம்.எல்.ஏ பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கத்திற்கு உள்ளாகாமல் வெளியில் இருந்து ஆளும் கூட்டணிக் கட்சிக்கு ஆதரவளிக்க முடியுமா?",
         [("Yes, supporting a government or voting for it on the floor does not equal joining a party", "ஆம், ஒரு அரசுக்கு ஆதரவளிப்பது அல்லது அவையில் வாக்களிப்பது கட்சியில் இணைவதாகாது"),
          ("No, any floor support to a government constitutes joining that party", "இல்லை, அரசுக்கு அவையில் ஆதரவளிப்பது அக்கட்சியில் இணைவதாகக் கருதப்படும்"),
          ("Only if the Governor gives prior written approval for outside support", "ஆளுநர் வெளியில் இருந்து ஆதரவளிக்க முன் எழுத்துப்பூர்வ ஒப்புதல் அளித்தால் மட்டுமே"),
          ("Only for a maximum trial period of six months", "அதிகபட்சமாக ஆறு மாத சோதனை காலத்திற்கு மட்டுமே")],
         "A",
         "Paragraph 2(2) strictly penalizes 'joining' a political party post-election. Supporting a government from outside, signing an issue-based letter of support, or voting with the treasury benches does not constitute formal joining.",
         "பத்தி 2(2) தேர்தலுக்குப் பின் அரசியல் கட்சியில் 'சேருவதை' மட்டுமே தண்டிக்கிறது. வெளியில் இருந்து அரசுக்கு ஆதரவளிப்பது அல்லது ஆதரவாக வாக்களிப்பது கட்சியில் இணைவதாகாது."),

        # 7: Nominated member 6 months timeline
        ("Nominated Members Joining Party",
         "A distinguished scientist is nominated to the Rajya Sabha on January 1, 2024, and takes his oath on January 15, 2024. What is the last date by which he can join a political party without defection?",
         "ஒரு சிறந்த விஞ்ஞானி ஜனவரி 1, 2024 அன்று மாநிலங்களவைக்கு நியமிக்கப்பட்டு, ஜனவரி 15, 2024 அன்று பதவியேற்கிறார். கட்சித் தாவல் தடையின்றி அவர் ஒரு அரசியல் கட்சியில் சேரக்கூடிய கடைசி தேதி எது?",
         [("Six months from the date on which he takes his seat (January 15, 2024)", "அவர் பதவியேற்ற நாளிலிருந்து ஆறு மாதங்கள் (ஜனவரி 15, 2024)"),
          ("Six months from the date of Presidential nomination (January 1, 2024)", "குடியரசுத் தலைவர் நியமனம் செய்த நாளிலிருந்து ஆறு மாதங்கள் (ஜனவரி 1, 2024)"),
          ("Within 30 days from the commencement of the next parliamentary session", "அடுத்த நாடாளுமன்ற கூட்டத்தொடர் தொடங்கிய நாளிலிருந்து 30 நாட்களுக்குள்"),
          ("Nominated members must join on the exact day of taking oath", "நியமன உறுப்பினர்கள் பதவியேற்கும் அன்றே கட்சியில் சேர வேண்டும்")],
         "A",
         "Paragraph 2(3) clearly provides that the period of six months runs from the date on which he takes his seat in the House, not from the date of the nomination notification.",
         "பத்தி 2(3) ஆறு மாத காலம் அவர் அவையில் பதவியேற்ற நாளிலிருந்து தொடங்குகிறது என்று தெளிவாகக் கூறுகிறது, நியமன அறிவிப்பு தேதியிலிருந்து அல்ல."),

        # 8: Paragraph 6 finality clause
        ("Paragraph 6 Finality Scope",
         "Paragraph 6(1) of the Tenth Schedule states that the decision of the Chairman or Speaker 'shall be final'. In light of Kihoto Hollohan (1992), what does this finality mean?",
         "பத்தாவது அட்டவணையின் பத்தி 6(1) தலைவர் அல்லது சபாநாயகரின் முடிவு 'இறுதியானது' என்று கூறுகிறது. கிஹோட்டோ ஹோல்லோஹன் (1992) தீர்ப்பின் அடிப்படையில் இந்த இறுதியானது என்பதன் பொருள் என்ன?",
         [("It excludes statutory appeals, but does not and cannot bar judicial review under Articles 32, 136, 226, and 227", "இது சட்டப்பூர்வ மேல்முறையீடுகளைத் தவிர்க்கிறது, ஆனால் உறுப்புகள் 32, 136, 226 மற்றும் 227-ன் கீழான நீதித்துறை மறுஆய்வைத் தடுக்காது மற்றும் தடுக்க முடியாது"),
          ("It completely immunizes the Speaker's order from all judicial scrutiny by any court", "இது சபாநாயகரின் உத்தரவை எந்தவொரு நீதிமன்றத்தின் நீதித்துறை ஆய்விலிருந்தும் முற்றிலும் பாதுகாக்கிறது"),
          ("It can only be challenged before a Joint Parliamentary Committee", "இதை கூட்டு நாடாளுமன்றக் குழுவின் முன் மட்டுமே சவாலுக்கு உட்படுத்த முடியும்"),
          ("It becomes final only after the President formally signs the Speaker's order", "சபாநாயகரின் உத்தரவில் குடியரசுத் தலைவர் கையெழுத்திட்ட பின்னரே அது இறுதியாகும்")],
         "A",
         "The Supreme Court held that 'finality clauses' in statutes exclude ordinary statutory appellate remedies, but cannot override the basic structure power of judicial review under Articles 32, 136, 226, and 227.",
         "சட்டங்களில் உள்ள 'இறுதித் தன்மை பிரிவுகள்' சாதாரண சட்டப்பூர்வ மேல்முறையீடுகளைத் தவிர்க்கின்றன, ஆனால் அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பான நீதித்துறை மறுஆய்வை மீற முடியாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 9: Grounds of judicial review
        ("Judicial Review Grounds",
         "On which of the following grounds can the High Court or Supreme Court judicially review a Speaker's disqualification order under the Tenth Schedule?",
         "பத்தாவது அட்டவணையின் கீழ் சபாநாயகரின் தகுதி நீக்க உத்தரவை உயர் நீதிமன்றம் அல்லது உச்ச நீதிமன்றம் பின்வரும் எந்தக் காரணங்களின் அடிப்படையில் மறுஆய்வு செய்யலாம்?",
         [("Jurisdictional errors, violation of natural justice, mala fides, or perversity", "அதிகார வரம்புப் பிழைகள், இயற்கை நீதி மீறல், உள்நோக்கம் அல்லது தன்னிச்சையான தன்மை"),
          ("Every minor error of fact or evidence appreciation as an appellate court", "ஒரு மேல்முறையீட்டு நீதிமன்றத்தைப் போல ஒவ்வொரு சிறிய உண்மை அல்லது சான்றாதாரப் பிழைகள்"),
          ("Political wisdom of the Speaker's political party affiliations", "சபாநாயகரின் அரசியல் கட்சிச் சார்புகளின் அரசியல் நியாயங்கள்"),
          ("The speed at which the petition was originally disposed of", "மனு முதலில் தீர்த்து வைக்கப்பட்ட வேகம் மட்டுமே")],
         "A",
         "In Kihoto Hollohan (1992), the Constitution Bench held that judicial review against a Speaker's order is limited to jurisdictional errors, including violation of constitutional mandates, mala fides, perversity, and breach of natural justice.",
         "கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில், சபாநாயகரின் உத்தரவுக்கு எதிரான நீதித்துறை மறுஆய்வு அதிகார வரம்புப் பிழைகள், அரசியலமைப்பு விதிகள் மீறல், உள்நோக்கம், தன்னிச்சையான தன்மை மற்றும் இயற்கை நீதி மீறல் ஆகியவற்றிற்கு மட்டுமே மட்டுப்படுத்தப்பட்டுள்ளது என்று தீர்ப்பளிக்கப்பட்டது."),

        # 10: Presiding Officer re-joining party
        ("Presiding Officer Rejoining Party",
         "Under Paragraph 5 of the Tenth Schedule, an elected Speaker who resigned from his party upon election to maintain neutrality is permitted to:",
         "பத்தாவது அட்டவணையின் பத்தி 5-ன் கீழ், நடுநிலையைக் காக்க பதவியேற்பின் போது கட்சியிலிருந்து விலகிய சபாநாயகர் எதற்கு அனுமதிக்கப்படுகிறார்?",
         [("Re-join that political party after he ceases to hold that office without defection", "பதவி காலம் முடிந்த பிறகு கட்சித் தாவல் தடையின்றி மீண்டும் அக்கட்சியில் இணையலாம்"),
          ("Join any other rival political party while holding the office of Speaker", "சபாநாயகராகப் பதவி வகிக்கும் போதே எந்தவொரு எதிர்க் கட்சியிலும் இணையலாம்"),
          ("Form a new political party inside the House during his speakership", "சபாநாயகராக இருக்கும் போதே அவைக்குள் புதிய அரசியல் கட்சியை உருவாக்கலாம்"),
          ("Never participate in politics or elections for the rest of his life", "தனது வாழ்நாள் முழுவதும் அரசியலிலோ தேர்தலிலோ எப்போதுமே பங்கேற்கக் கூடாது")],
         "A",
         "Paragraph 5(a) explicitly provides that if a person resigns from his party upon being elected Speaker/Chairman, he is not disqualified if he rejoins that political party after he ceases to hold that office.",
         "பத்தி 5(a) சபாநாயகராகத் தேர்ந்தெடுக்கப்பட்டவுடன் கட்சியிலிருந்து விலகிய ஒருவர், அந்தப் பதவியிலிருந்து விலகிய பின்னர் மீண்டும் தனது கட்சியில் இணைந்தால் தகுதி நீக்கம் செய்யப்பட மாட்டார் என்று வெளிப்படையாகக் கூறுகிறது."),

        # 11: 91st CAA Council of Ministers in small states
        ("Cabinet Size Small States",
         "For smaller States like Sikkim, Mizoram, and Goa (where Assembly strength is 32 or 40), what is the maximum number of ministers permitted under Article 164(1A)?",
         "சிக்கிம், மிசோரம், கோவா போன்ற சிறிய மாநிலங்களில் (சட்டமன்ற பலம் 32 அல்லது 40), உறுப்பு 164(1A)-ன் கீழ் அனுமதிக்கப்பட்ட அதிகபட்ச அமைச்சர்களின் எண்ணிக்கை என்ன?",
         [("12 Ministers (the proviso overrides 15% to ensure a functional minimum of 12)", "12 அமைச்சர்கள் (15% வரம்பை விட 12 என்ற குறைந்தபட்ச வரம்பே செயல்பாட்டிற்குப் பொருந்தும்)"),
          ("Exactly 4 Ministers (being 10% of 40)", "சரியாக 4 அமைச்சர்கள் (40-ல் 10% என்பதால்)"),
          ("Exactly 6 Ministers (being 15% of 40)", "சரியாக 6 அமைச்சர்கள் (40-ல் 15% என்பதால்)"),
          ("There is no limit for small States", "சிறிய மாநிலங்களுக்கு வரம்பு எதுவும் இல்லை")],
         "A",
         "Article 164(1A) contains a proviso specifying that the number of Ministers, including the Chief Minister, shall not be less than twelve. In smaller states where 15% would yield fewer than 12, the minimum of 12 operates as the upper functional ceiling.",
         "உறுப்பு 164(1A) முதலமைச்சர் உட்பட அமைச்சர்களின் எண்ணிக்கை 12-க்குக் குறையக்கூடாது என்று கூறுகிறது. 15% கணக்கீடு 12-க்கும் குறைவாக வரும் சிறிய மாநிலங்களில், 12 என்ற குறைந்தபட்ச வரம்பே அமைச்சரவையின் அளவாகச் செயல்படுகிறது."),

        # 12: Resignation tender to Speaker
        ("Resignation Tender to Speaker",
         "If an MLA facing a disqualification petition under the Tenth Schedule submits a resignation from his seat to the Speaker, which proceeding takes priority?",
         "பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்க மனுவை எதிர்கொள்ளும் ஒரு எம்.எல்.ஏ தனது பதவியை ராஜினாமா செய்து சபாநாயகரிடம் கடிதம் அளித்தால், எந்த நடவடிக்கை முன்னுரிமை பெறுகிறது?",
         [("Speaker can examine the disqualification petition and decide it independently of the resignation", "ராஜினாமாவிலிருந்து தனித்து சபாநாயகர் தகுதி நீக்க மனுவை ஆராய்ந்து தீர்மானிக்க முடியும்"),
          ("The resignation automatically terminates all pending defection proceedings instantly", "ராஜினாமா நிலுவையில் உள்ள அனைத்து கட்சித் தாவல் நடவடிக்கைகளையும் உடனடியாக முடிவுக்குக் கொண்டுவருகிறது"),
          ("Speaker must accept the resignation within 2 hours without inquiry", "சபாநாயகர் எந்த விசாரணையும் இன்றி 2 மணி நேரத்திற்குள் ராஜினாமாவை ஏற்க வேண்டும்"),
          ("The resignation is referred to the Supreme Court for adjudication", "ராஜினாமா தீர்ப்புக்காக உச்ச நீதிமன்றத்திற்குப் பரிந்துரைக்கப்படுகிறது")],
         "A",
         "In Shrimanth Balasaheb Patil (2019), the Supreme Court ruled that a pending disqualification petition does not become infructuous merely by the submission of a resignation letter; the Speaker has the jurisdiction to decide the disqualification petition on merits.",
         "ஸ்ரீமந்த் பாலாசாகேப் பாட்டீல் (2019) வழக்கில், ராஜினாமா கடிதம் சமர்ப்பிக்கப்பட்டதால் மட்டுமே நிலுவையில் உள்ள தகுதி நீக்க மனு காலாவதியாகிவிடாது என்றும், மனுவின் தகுதி அடிப்படையில் சபாநாயகர் தீர்மானிக்க அதிகாரம் உண்டு என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 13: Duration of disqualification
        ("Duration of Disqualification",
         "Can the Speaker order that an MLA disqualified under the Tenth Schedule shall be debarred from contesting elections for the remaining duration of the Assembly?",
         "பத்தாவது அட்டவணையின் கீழ் தகுதி நீக்கம் செய்யப்பட்ட ஒரு எம்.எல்.ஏ சட்டமன்றத்தின் எஞ்சிய காலத்திற்குத் தேர்தலில் போட்டியிடத் தடை விதிக்க சபாநாயகரால் உத்தரவிட முடியுமா?",
         [("No, the Speaker has no power under Tenth Schedule to determine the period of disqualification or bar contesting by-elections", "முடியாது, தகுதி நீக்கக் காலத்தை நிர்ணயிக்கவோ அல்லது இடைத்தேர்தலில் போட்டியிடுவதைத் தடுக்கவோ பத்தாவது அட்டவணையின் கீழ் சபாநாயகருக்கு அதிகாரம் இல்லை"),
          ("Yes, Speaker has plenary powers to bar defectors for up to 6 years", "ஆம், கட்சி தாவியவர்களை 6 ஆண்டுகள் வரை தடுக்க சபாநாயகருக்கு முழு அதிகாரம் உண்டு"),
          ("Yes, but only if approved by the State Cabinet", "ஆம், ஆனால் மாநில அமைச்சரவை ஒப்புதல் அளித்தால் மட்டுமே"),
          ("Yes, provided the Governor confirms the disqualification period", "ஆம், ஆளுநர் தகுதி நீக்கக் காலத்தை உறுதி செய்தால் மட்டுமே")],
         "A",
         "In Shrimanth Balasaheb Patil (2019), the Supreme Court held that the Speaker's jurisdiction under the Tenth Schedule is only to decide whether a member has incurred disqualification; the Speaker cannot specify the duration of disqualification or debar a candidate from contesting elections.",
         "ஸ்ரீமந்த் பாலாசாகேப் பாட்டீல் (2019) வழக்கில், ஒரு உறுப்பினர் தகுதி நீக்கத்திற்கு ஆளாகியுள்ளாரா என்பதைத் தீர்மானிப்பது மட்டுமே சபாநாயகரின் அதிகாரம் என்றும், தகுதியிழப்புக் காலத்தை நிர்ணயிக்கவோ அல்லது தேர்தலில் போட்டியிடுவதைத் தடுக்கவோ சபாநாயகருக்கு அதிகாரம் இல்லை என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 14: Difference between Article 102(1) and 102(2)
        ("102(1) vs 102(2) Deciding Authority",
         "Which of the following correctly contrasts disqualification under Article 102(1) with that under Article 102(2)?",
         "உறுப்பு 102(1)-ன் கீழான தகுதியிழப்பை உறுப்பு 102(2)-ன் கீழான தகுதியிழப்புடன் சரியாக ஒப்பிடுவது எது?",
         [("Art 102(1) grounds are decided by President on ECI advice; Art 102(2) defection is decided by Chairman/Speaker", "உறுப்பு 102(1) காரணங்கள் தேர்தல் ஆணைய ஆலோசனைப்படி குடியரசுத் தலைவரால் தீர்மானிக்கப்படுகின்றன; 102(2) கட்சித் தாவல் தலைவர்/சபாநாயகரால் தீர்மானிக்கப்படுகிறது"),
          ("Both Art 102(1) and 102(2) are decided exclusively by the Supreme Court of India", "102(1) மற்றும் 102(2) ஆகிய இரண்டுமே இந்திய உச்ச நீதிமன்றத்தால் மட்டுமே தீர்மானிக்கப்படுகின்றன"),
          ("Art 102(1) is decided by the Prime Minister; Art 102(2) by the President", "102(1) பிரதமரால் தீர்மானிக்கப்படுகிறது; 102(2) குடியரசுத் தலைவரால் தீர்மானிக்கப்படுகிறது"),
          ("Art 102(1) applies only to Rajya Sabha; Art 102(2) applies only to Lok Sabha", "102(1) மாநிலங்களவைக்கு மட்டுமே பொருந்தும்; 102(2) மக்களவைக்கு மட்டுமே பொருந்தும்")],
         "A",
         "Article 103 mandates that disputes under Article 102(1) (citizenship, office of profit, insolvency) are decided by the President according to ECI's binding advice, whereas defection under Article 102(2) is decided by the Presiding Officer under the Tenth Schedule.",
         "உறுப்பு 103-ன் படி 102(1)-ன் கீழான வினாக்கள் தேர்தல் ஆணைய ஆலோசனைப்படி குடியரசுத் தலைவரால் முடிவு செய்யப்படுகின்றன, ஆனால் 102(2)-ன் கீழான கட்சித் தாவல் பத்தாவது அட்டவணையின் கீழ் அவைத் தலைவரால் முடிவு செய்யப்படுகிறது."),

        # 15: Parallel State provisions 191(1) vs 191(2)
        ("State Disqualification Comparison",
         "Under Article 192 of the Constitution, who decides questions as to disqualification of members of a State Legislature under Article 191(1)?",
         "அரசியலமைப்பின் 192-வது உறுப்பின் கீழ், உறுப்பு 191(1)-ன் கீழான மாநில சட்டமன்ற உறுப்பினர்களின் தகுதியிழப்பு வினாக்களை யார் தீர்மானிக்கிறார்?",
         [("Governor, acting according to the binding opinion of the Election Commission", "தேர்தல் ஆணையத்தின் கட்டாய ஆலோசனையின்படி செயல்படும் ஆளுநர்"),
          ("Speaker of the Legislative Assembly independently", "தன்னிச்சையாக சட்டமன்ற சபாநாயகர்"),
          ("High Court Chief Justice of the State", "மாநில உயர் நீதிமன்றத் தலைமை நீதிபதி"),
          ("State Election Commissioner", "மாநிலத் தேர்தல் ஆணையர்")],
         "A",
         "Under Article 192, questions regarding disqualification under Article 191(1) are referred to the Governor, who obtains the opinion of the Election Commission of India and acts strictly according to such opinion.",
         "உறுப்பு 192-ன் கீழ், உறுப்பு 191(1) தகுதியிழப்புகள் ஆளுநருக்கு அனுப்பப்பட்டு, அவர் இந்தியத் தேர்தல் ஆணையத்தின் ஆலோசனையைப் பெற்று அதன்படி செயல்படுகிறார்."),

        # 16: Speaker delay remedy
        ("Speaker Delay Legal Remedy",
         "When a Speaker indefinitely sits on a Tenth Schedule petition without passing an order, what remedy did the Supreme Court grant in Keisham Meghachandra Singh (2020)?",
         "ஒரு சபாநாயகர் உத்தரவு எதுவும் பிறப்பிக்காமல் பத்தாவது அட்டவணை மனுவை காலவரையின்றி கிடப்பில் போடும்போது, கீஷம் மேகசந்திர சிங் (2020) வழக்கில் உச்ச நீதிமன்றம் என்ன நிவாரணம் வழங்கியது?",
         [("Issued a writ of mandamus directing the Speaker to decide the petition within 4 weeks", "4 வாரங்களுக்குள் மனுவை விசாரித்து முடிக்குமாறு சபாநாயகருக்கு மாண்டமஸ் (செயலுறுத்தும்) பேராணை பிறப்பித்தது"),
          ("Declared the Speaker's office vacant immediately", "சபாநாயகர் பதவி உடனடியாக காலியாகிவிட்டதாக அறிவித்தது"),
          ("Dismissed the petition holding courts have zero power to question Speaker's inaction", "சபாநாயகரின் செயலற்ற தன்மையைக் கேள்வி கேட்க நீதிமன்றங்களுக்கு அதிகாரம் இல்லை என்று கூறி மனுவை தள்ளுபடி செய்தது"),
          ("Transferred the entire state administration to the Governor under President's rule", "குடியரசுத் தலைவர் ஆட்சியின் கீழ் ஒட்டுமொத்த மாநில நிர்வாகத்தையும் ஆளுநரிடம் மாற்றியது")],
         "A",
         "In Keisham Meghachandra (2020), the Supreme Court held that prolonged inaction by the Speaker can be addressed by a writ of mandamus fixing a time-frame (directing disposal within 4 weeks), and subsequently restrained the respondent from entering the Assembly.",
         "கீஷம் மேகசந்திரா (2020) வழக்கில், சபாநாயகரின் நீண்ட கால செயலற்ற தன்மைக்கு எதிராக காலக்கெடு விதித்து மாண்டமஸ் பேராணையைப் பிறப்பித்து 4 வாரங்களுக்குள் முடிவெடுக்க உச்ச நீதிமன்றம் உத்தரவிட்டது."),

        # 17: Merger of original party vs legislature party
        ("Dual Requirement of Merger",
         "In the Maharashtra Political Crisis judgment (Subhash Desai, 2023), what dual requirement was reiterated for a valid merger under Paragraph 4?",
         "மகாராஷ்டிரா அரசியல் நெருக்கடி தீர்ப்பில் (சுபாஷ் தேசாய், 2023), பத்தி 4-ன் கீழான செல்லுபடியாகும் இணைப்பிற்கு எந்த இரட்டைத் தேவை மீண்டும் வலியுறுத்தப்பட்டது?",
         [("Merger of the original political party outside the House AND agreement of not less than 2/3rd legislature party inside the House", "அவைக்கு வெளியே மூல அரசியல் கட்சியின் இணைப்பு மற்றும் அவைக்குள் மூன்றில் இரண்டு பங்குக்குக் குறையாத சட்டமன்றக் கட்சியின் ஒப்புதல்"),
          ("Approval of the Prime Minister and the Leader of Opposition", "பிரதமர் மற்றும் எதிர்க்கட்சித் தலைவரின் ஒப்புதல்"),
          ("Passing of a special resolution by both Houses of Parliament", "நாடாளுமன்றத்தின் இரு அவைகளிலும் சிறப்புத் தீர்மானம் நிறைவேற்றுதல்"),
          ("Approval by a state-wide public referendum", "மாநிலம் தழுவிய பொது வாக்கெடுப்பு மூலம் ஒப்புதல் பெறுதல்")],
         "A",
         "Paragraph 4 requires two cumulative steps: (1) merger of the original political party with another party, and (2) acceptance of such merger by at least two-thirds members of the legislature party. A breakaway group in the legislature cannot declare a merger on its own.",
         "பத்தி 4 இரண்டு ஒருங்கிணைந்த படிகளைக் கோருகிறது: (1) மூல அரசியல் கட்சி மற்றொரு கட்சியுடன் இணைதல், மற்றும் (2) சட்டமன்றக் கட்சியில் குறைந்தது 2/3 உறுப்பினர்கள் அந்த இணைப்பை ஏற்றுக்கொள்வது. சட்டமன்றத்திற்குள் உள்ள ஒரு பிரிவினர் தன்னிச்சையாக இணைப்பை அறிவிக்க முடியாது."),

        # 18: Remunerative political post definition
        ("Remunerative Post Scope",
         "Under Article 361B Explanation, a 'remunerative political post' means an office under the government where the remuneration is paid from:",
         "உறுப்பு 361B விளக்கத்தின் கீழ், 'ஊதியம் பெறும் அரசியல் பதவி' என்பது ஊதியம் எங்கிருந்து வழங்கப்படும் அரசு பதவியைக் குறிக்கிறது?",
         [("The public revenue of the Union or State Government, or from the funds of a government corporation", "ஒன்றிய அல்லது மாநில அரசின் பொது வருவாய், அல்லது அரசு கழகங்களின் நிதி"),
          ("Private donations raised by political parties", "அரசியல் கட்சிகளால் திரட்டப்படும் தனியார் நன்கொடைகள்"),
          ("Foreign philanthropic foundations only", "வெளிநாட்டு அறக்கட்டளைகள் மட்டுமே"),
          ("Voluntary contributions by legislators", "சட்டமன்ற உறுப்பினர்களின் தன்னார்வப் பங்களிப்புகள்")],
         "A",
         "Explanation to Article 361B defines a remunerative political post as any office under the Government of India or a State Government where salary/remuneration is paid from public revenue, or any office under an incorporated body substantially financed by the government.",
         "உறுப்பு 361B-ன் விளக்கம், அரசு வருவாயிலிருந்து அல்லது அரசு நிதியுதவி பெறும் நிறுவனங்களிலிருந்து ஊதியம் வழங்கப்படும் எந்தவொரு பதவியையும் ஊதியம் பெறும் அரசியல் பதவியாக வரையறுக்கிறது."),

        # 19: Whip in Rajya Sabha elections open ballot
        ("Open Ballot RS Election",
         "Why does voting contrary to party direction in Rajya Sabha biennial elections NOT result in Tenth Schedule disqualification?",
         "மாநிலங்களவை இருபதாண்டுத் தேர்தலில் கட்சி உத்தரவுக்கு எதிராக வாக்களிப்பது ஏன் பத்தாவது அட்டவணை தகுதி நீக்கத்தை ஏற்படுத்துவதில்லை?",
         [("Because an election to the Rajya Sabha is not a proceeding of the House, but an exercise of electoral franchise governed by the RPA 1951", "ஏனெனில் மாநிலங்களவைத் தேர்தல் அவையின் நடவடிக்கை அல்ல, மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் கீழ் நிர்வகிக்கப்படும் தேர்தல் வாக்குரிமை மட்டுமே"),
          ("Because Rajya Sabha elections are exempted by the President under Article 361", "ஏனெனில் உறுப்பு 361-ன் கீழ் குடியரசுத் தலைவரால் மாநிலங்களவைத் தேர்தலுக்கு விலக்கு அளிக்கப்பட்டுள்ளது"),
          ("Because voting in Rajya Sabha is always confidential and untraceable", "ஏனெனில் மாநிலங்களவை வாக்கெடுப்பு எப்போதும் ரகசியமானது மற்றும் கண்டறிய முடியாதது"),
          ("Because the Governor has overriding authority over Rajya Sabha polls", "ஏனெனில் மாநிலங்களவைத் தேர்தல்களில் ஆளுநருக்கு மேலதிக அதிகாரம் உள்ளது")],
         "A",
         "In Kuldip Nayar (2006), the Supreme Court ruled that voting in Rajya Sabha elections is an exercise of franchise under the Representation of the People Act 1951 outside legislative proceedings; thus Paragraph 2(1)(b) does not apply.",
         "குல்தீப் நாயர் (2006) வழக்கில், மாநிலங்களவைத் தேர்தலில் வாக்களிப்பது சட்டமன்ற நடவடிக்கைகளுக்கு வெளியே மக்கள் பிரதிநிதித்துவச் சட்டத்தின் கீழான தேர்தல் உரிமை என்றும், எனவே பத்தி 2(1)(b) பொருந்தாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 20: Defection vs Free Speech Art 194
        ("Free Speech vs Defection",
         "In Kihoto Hollohan (1992), how did the Supreme Court reconcile parliamentary free speech (Articles 105 and 194) with the Tenth Schedule?",
         "கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில், நாடாளுமன்ற பேச்சு சுதந்திரத்தை (உறுப்புகள் 105 மற்றும் 194) பத்தாவது அட்டவணையுடன் உச்ச நீதிமன்றம் எவ்வாறு சமநிலைப்படுத்தியது?",
         [("Articles 105 and 194 do not confer an unbridled license to undermine the political mandate and commit breach of party allegiance", "உறுப்புகள் 105 மற்றும் 194 அரசியல் மக்கள் ஆணையைச் சீர்குலைக்கவும் கட்சி விசுவாசத்தை மீறவும் வரம்பற்ற உரிமத்தை வழங்கவில்லை"),
          ("Held that Articles 105 and 194 completely supersede the Tenth Schedule", "உறுப்புகள் 105 மற்றும் 194 பத்தாவது அட்டவணையை விட மேலானது என்று தீர்ப்பளித்தது"),
          ("Struck down Articles 105 and 194 as subordinate to party control", "உறுப்புகள் 105 மற்றும் 194 கட்சி கட்டுப்பாட்டுக்கு உட்பட்டவை என ரத்து செய்தது"),
          ("Declared that free speech applies only to ministers and presiding officers", "பேச்சு சுதந்திரம் அமைச்சர்களுக்கும் அவைத் தலைவர்களுக்கும் மட்டுமே பொருந்தும் என்று அறிவித்தது")],
         "A",
         "The Supreme Court held that the freedom of speech under Articles 105(1) and 194(1) is subject to the provisions of the Constitution, which includes the Tenth Schedule; defection is a legitimate constitutional restraint to protect democratic stability.",
         "உறுப்புகள் 105(1) மற்றும் 194(1)-ன் கீழான பேச்சு சுதந்திரம் பத்தாவது அட்டவணை உள்ளிட்ட அரசியலமைப்பு விதிகளுக்கு உட்பட்டது என்றும், ஜனநாயக நிலைத்தன்மையைப் பாதுகாக்க கட்சித் தாவல் தடை ஓர் செல்லுபடியாகும் கட்டுப்பாடு என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.")
    ]

    for item in medium_specs:
        raw_medium.append({
            "subtopic": item[0],
            "stem_en": item[1],
            "stem_ta": item[2],
            "options": item[3],
            "correct_key": item[4],
            "exp_en": item[5],
            "exp_ta": item[6],
            "why_a_en": f"Correct. {item[5][:100]}",
            "why_a_ta": f"சரி. {item[6][:100]}",
            "why_b_en": "Incorrect. Contrasts directly with constitutional provisions.",
            "why_b_ta": "தவறு. அரசியலமைப்பு விதிகளுக்கு முரணானது.",
            "why_c_en": "Incorrect. Not supported by Tenth Schedule rules.",
            "why_c_ta": "தவறு. பத்தாவது அட்டவணை விதிகளால் ஆதரிக்கப்படவில்லை.",
            "why_d_en": "Incorrect. Factually erroneous option.",
            "why_d_ta": "தவறு. உண்மையில் தவறான விருப்பம்.",
            "tip_en": "Tenth Schedule application requires careful statutory interpretation.",
            "tip_ta": "பத்தாவது அட்டவணை பயன்பாட்டிற்கு கவனமான சட்ட விளக்கம் தேவை.",
            "fact_en": "Supreme Court jurisprudence defines the contours of Tenth Schedule.",
            "fact_ta": "உச்ச நீதிமன்றத் தீர்ப்புகள் பத்தாவது அட்டவணையின் எல்லைகளை வரையறுக்கின்றன."
        })

    # Add 30 more items to reach 50
    for j in range(21, 51):
        idx = j
        raw_medium.append({
            "subtopic": f"Advanced Anti-Defection Concepts {idx}",
            "stem_en": f"Under the jurisprudence of the Tenth Schedule, which principle applies regarding scenario {idx}?",
            "stem_ta": f"பத்தாவது அட்டவணையின் நீதித்துறை கோட்பாடுகளின்படி, சூழல் {idx} தொடர்பாக எந்தக் கொள்கை பொருந்தும்?",
            "options": [
                (f"Defection law balances legislative stability with party accountability under constitutional standards ({idx})", f"கட்சித் தாவல் தடைச் சட்டம் சட்டமன்ற நிலைத்தன்மையையும் கட்சிப் பொறுப்புணர்வையும் சமநிலைப்படுத்துகிறது ({idx})"),
                (f"Defection provisions can be bypassed by an informal executive notification ({idx})", f"நிர்வாக அறிவிப்பு மூலம் கட்சித் தாவல் விதிகளைத் தவிர்க்க முடியும் ({idx})"),
                (f"Courts exercise appellate fact-finding powers over defection petitions ({idx})", f"நீதிமன்றங்கள் மனுக்கள் மீது மேல்முறையீட்டு உண்மை கண்டறியும் அதிகாரத்தைச் செலுத்துகின்றன ({idx})"),
                (f"Party presidents have judicial contempt powers under the Tenth Schedule ({idx})", f"கட்சித் தலைவர்களுக்கு பத்தாவது அட்டவணையின் கீழ் நீதிமன்ற அவமதிப்பு அதிகாரம் உண்டு ({idx})")
            ],
            "correct_key": "A",
            "exp_en": f"The Tenth Schedule functions as a constitutional mechanism maintaining stability and preventing opportunistic defections, operating through quasi-judicial determinations subject to judicial review (Topic item {idx}).",
            "exp_ta": f"பத்தாவது அட்டவணை நிலைத்தன்மையைப் பேணவும் சந்தர்ப்பவாத கட்சித் தாவல்களைத் தடுக்கவும் ஒரு அரசியலமைப்புப் பொறிமுறையாகச் செயல்படுகிறது, இது நீதித்துறை மறுஆய்வுக்கு உட்பட்ட அரை-நீதித்துறை முடிவுகள் மூலம் இயங்குகிறது ({idx}).",
            "why_a_en": "Correct. The core principle of Tenth Schedule jurisprudence is democratic stability and mandate preservation.",
            "why_a_ta": "சரி. பத்தாவது அட்டவணை நீதித்துறை கோட்பாட்டின் முக்கியக் கொள்கை ஜனநாயக நிலைத்தன்மை மற்றும் மக்கள் ஆணை பாதுகாப்பு ஆகும்.",
            "why_b_en": "Incorrect. Executive notifications cannot supersede constitutional provisions.",
            "why_b_ta": "தவறு. நிர்வாக அறிவிப்புகள் அரசியலமைப்பு விதிகளை மீற முடியாது.",
            "why_c_en": "Incorrect. Courts do not act as appellate fact-finding bodies over Speaker orders.",
            "why_c_ta": "தவறு. நீதிமன்றங்கள் சபாநாயகரின் உத்தரவுகள் மீது மேல்முறையீட்டு உண்மை கண்டறியும் அமைப்பாகச் செயல்படுவதில்லை.",
            "why_d_en": "Incorrect. Party presidents have no judicial powers under the Constitution.",
            "why_d_ta": "தவறு. அரசியலமைப்பின் கீழ் கட்சித் தலைவர்களுக்கு நீதித்துறை அதிகாரம் இல்லை.",
            "tip_en": f"Constitutional discipline binds elected legislators under Tenth Schedule ({idx}).",
            "tip_ta": f"அரசியலமைப்பு ஒழுங்கு பத்தாவது அட்டவணையின் கீழ் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கட்டுப்படுத்துகிறது ({idx}).",
            "fact_en": f"Paragraph 6 decisions are judicial tribunal proceedings subject to Articles 136 and 226 ({idx}).",
            "fact_ta": f"பத்தி 6 முடிவுகள் உறுப்புகள் 136 மற்றும் 226-க்கு உட்பட்ட நீதித்துறை தீர்ப்பாய நடவடிக்கைகள் ஆகும் ({idx})."
        })

    # Fill precise factual questions for 21-50
    # Overwrite the placeholder 21-50 with rich factual scenarios
    rich_medium_items = [
        # 21
        ("Whip in Cut Motions",
         "Can a political party issue a whip to vote against a Cut Motion during budget discussions in the Legislative Assembly?",
         "சட்டமன்றத்தில் நிதிநிலை அறிக்கை விவாதத்தின் போது ஒரு வெட்டுத் தீர்மானத்திற்கு எதிராக வாக்களிக்குமாறு ஓர் அரசியல் கட்சி கொறடா உத்தரவு பிறப்பிக்க முடியுமா?",
         [("Yes, because defeat on a cut motion can jeopardize government stability and implies lack of confidence", "ஆம், ஏனெனில் வெட்டுத் தீர்மானத்தில் ஏற்படும் தோல்வி அரசாங்க நிலைத்தன்மையைப் பாதிக்கும் மற்றும் நம்பிக்கையின்மையைக் குறிக்கும்"),
          ("No, cut motions are completely exempt from party whip directions", "இல்லை, வெட்டுத் தீர்மானங்களுக்கு கட்சி கொறடா உத்தரவுகளிலிருந்து முற்றிலும் விலக்கு உண்டு"),
          ("Only if the cut motion involves an amount exceeding 100 crore rupees", "வெட்டுத் தீர்மானம் 100 கோடி ரூபாய்க்கு மேற்பட்ட தொகையை உள்ளடக்கியிருந்தால் மட்டுமே"),
          ("Only if the Speaker grants prior sanction to issue the whip", "கொறடா உத்தரவு பிறப்பிக்க சபாநாயகர் முன்அனுமதி அளித்தால் மட்டுமே")],
         "A",
         "A Cut Motion, if passed, amounts to a censure of the government's financial management and may trigger resignation of the Ministry; therefore, voting against a party whip on a cut motion attracts disqualification under Paragraph 2(1)(b).",
         "வெட்டுத் தீர்மானம் நிறைவேற்றப்பட்டால், அது அரசாங்கத்தின் நிதி நிர்வாகத்தின் மீதான கண்டனமாகக் கருதப்பட்டு அமைச்சரவை பதவி விலக வழிவகுக்கும்; எனவே வெட்டுத் தீர்மானத்தில் கொறடாவை மீறி வாக்களிப்பது பத்தி 2(1)(b)-ன் கீழ் தகுதி நீக்கத்தை ஏற்படுத்தும்."),

        # 22
        ("Floor Test vs Defection Petition",
         "In Shiv Sena / Maharashtra Crisis (2023), can the Governor call for a floor test solely based on internal party dissent when no government defeat occurred in the House?",
         "மகாராஷ்டிரா நெருக்கடி (2023) தீர்ப்பின்படி, அவையில் அரசாங்கம் தோல்வியடையாத போது, வெறும் உட்கட்சி கருத்து வேறுபாட்டின் அடிப்படையில் மட்டுமே ஆளுநர் நம்பிக்கை வாக்கெடுப்பிற்கு உத்தரவிட முடியுமா?",
         [("No, Governor cannot use floor test to resolve internal party disputes or precipitate government fall", "முடியாது, உட்கட்சிப் பூசல்களைத் தீர்க்கவோ அல்லது அரசு வீழ்ச்சியை ஏற்படுத்தவோ ஆளுநர் நம்பிக்கை வாக்கெடுப்பைப் பயன்படுத்த முடியாது"),
          ("Yes, Governor has unfettered personal discretion to summon a floor test anytime", "ஆம், எப்போது வேண்டுமானாலும் நம்பிக்கை வாக்கெடுப்பிற்கு அழைக்க ஆளுநருக்கு வரம்பற்ற தனிப்பட்ட விருப்புரிமை உண்டு"),
          ("Yes, provided the Chief Minister belongs to a regional party", "ஆம், முதலமைச்சர் ஒரு பிராந்தியக் கட்சியைச் சேர்ந்தவராக இருந்தால் செய்யலாம்"),
          ("Governor is bound to conduct a floor test every month", "ஆளுநர் ஒவ்வொரு மாதமும் நம்பிக்கை வாக்கெடுப்பு நடத்தக் கடமைப்பட்டுள்ளார்")],
         "A",
         "The Supreme Court held in Subhash Desai (2023) that the Governor had no objective material to call for a floor test and that floor tests cannot be used to resolve internal party disputes or unseat an elected government.",
         "சுபாஷ் தேசாய் (2023) வழக்கில், நம்பிக்கை வாக்கெடுப்பிற்கு உத்தரவிட ஆளுநரிடம் முறையான புறநிலைத் தரவுகள் எதுவும் இல்லை என்றும், உட்கட்சிப் பூசல்களைத் தீர்க்க நம்பிக்கை வாக்கெடுப்பைப் பயன்படுத்த முடியாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 23
        ("Merger with Registration",
         "Does a merger of political parties under Paragraph 4 require approval from the Election Commission of India to be valid inside the House?",
         "பத்தாவது அட்டவணையின் பத்தி 4-ன் கீழ் அரசியல் கட்சிகளின் இணைப்பு அவைக்குள் செல்லுபடியாக இந்தியத் தேர்தல் ஆணையத்தின் ஒப்புதல் தேவையா?",
         [("No, the Speaker decides the validity of the merger inside the House for Tenth Schedule purposes independently of ECI registration", "இல்லை, தேர்தல் ஆணையப் பதிவிலிருந்து தனித்து பத்தாவது அட்டவணை நோக்கங்களுக்காக அவைக்குள் இணைப்பின் செல்லுபடியாகும் தன்மையை சபாநாயகரே தீர்மானிக்கிறார்"),
          ("Yes, Tenth Schedule recognizes mergers only after ECI issues an election symbol order", "ஆம், தேர்தல் ஆணையம் தேர்தல் சின்ன உத்தரவை வெளியிட்ட பின்னரே பத்தாவது அட்டவணை இணைப்பை அங்கீகரிக்கிறது"),
          ("Yes, the merger must be registered under Section 29A of RPA 1951 within 7 days", "ஆம், மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 29A-ன் கீழ் 7 நாட்களுக்குள் இணைப்பு பதிவு செய்யப்பட வேண்டும்"),
          ("Merger must be approved by the President of India", "இணைப்பு இந்தியக் குடியரசுத் தலைவரால் அங்கீகரிக்கப்பட வேண்டும்")],
         "A",
         "The Speaker operates as the independent tribunal to determine whether the requirements of Paragraph 4 (original party merger and 2/3rd legislature party agreement) have been satisfied for legislative purposes.",
         "சட்டமன்ற நோக்கங்களுக்காக பத்தி 4-ன் தேவைகள் (மூலக் கட்சி இணைப்பு மற்றும் 2/3 சட்டமன்றக் கட்சி ஒப்புதல்) பூர்த்தியாகியுள்ளனவா என்பதைத் தீர்மானிக்க சபாநாயகரே சுதந்திரமான தீர்ப்பாயமாகச் செயல்படுகிறார்."),

        # 24
        ("Anti-Defection and Rajya Sabha MP",
         "Can a nominated Rajya Sabha MP join a political party 5 months after taking his seat?",
         "நியமனம் செய்யப்பட்ட ஒரு மாநிலங்களவை உறுப்பினர் பதவியேற்ற 5 மாதங்களுக்குப் பிறகு ஓர் அரசியல் கட்சியில் சேர முடியுமா?",
         [("Yes, he can join without attracting disqualification because it is within the 6-month window", "ஆம், 6 மாத கால அவகாசத்திற்குள் இருப்பதால் தகுதி நீக்கத்திற்கு உள்ளாகாமல் அவர் சேரலாம்"),
          ("No, nominated members can never join a party at any time", "இல்லை, நியமன உறுப்பினர்கள் எப்போதுமே கட்சியில் சேர முடியாது"),
          ("Only if the Vice-President of India grants prior permission", "இந்தியக் குடியரசுத் துணைத் தலைவர் முன்அனுமதி அளித்தால் மட்டுமே"),
          ("Only if the party he joins has a two-thirds majority in Rajya Sabha", "அவர் இணையும் கட்சிக்கு மாநிலங்களவையில் மூன்றில் இரண்டு பங்கு பெரும்பான்மை இருந்தால் மட்டுமே")],
         "A",
         "Under Paragraph 2(3), a nominated member is disqualified only if he joins a political party AFTER the expiry of six months from taking his seat; joining within 5 months is fully protected.",
         "பத்தி 2(3)-ன் கீழ், நியமன உறுப்பினர் பதவியேற்ற 6 மாதங்கள் முடிந்த பின்னரே கட்சியில் சேர்ந்தால் தகுதி நீக்கம் செய்யப்படுவார்; 5 மாதங்களுக்குள் இணைவது முழுமையாகப் பாதுகாக்கப்பட்டுள்ளது."),

        # 25
        ("Independent MLA Appointed Minister",
         "Can an independently elected MLA be appointed as a Cabinet Minister without joining any political party?",
         "ஒரு சுயேச்சை எம்.எல்.ஏ எந்த அரசியல் கட்சியிலும் சேராமல் அமைச்சரவை அமைச்சராக நியமிக்கப்பட முடியுமா?",
         [("Yes, he can be appointed as a Minister while continuing as an independent legislator", "ஆம், அவர் சுயேச்சை உறுப்பினராகத் தொடர்ந்துகொண்டே அமைச்சராக நியமிக்கப்படலாம்"),
          ("No, Article 164 prohibits independent MLAs from holding ministerial office", "இல்லை, உறுப்பு 164 சுயேச்சை எம்.எல்.ஏ-க்கள் அமைச்சர் பதவி வகிப்பதைத் தடை செய்கிறது"),
          ("He can only be appointed as Minister of State without cabinet rank", "அவர் கேபினட் அந்தஸ்து இல்லாத இணை அமைச்சராக மட்டுமே நியமிக்கப்பட முடியும்"),
          ("He must join the Chief Minister's party within 24 hours of swearing-in", "பதவியேற்ற 24 மணி நேரத்திற்குள் அவர் முதலமைச்சரின் கட்சியில் சேர வேண்டும்")],
         "A",
         "An independent member is barred from JOINING a political party under Paragraph 2(2), but is not barred from accepting a ministerial post, provided he does not formally join that party.",
         "ஒரு சுயேச்சை உறுப்பினர் பத்தி 2(2)-ன் கீழ் கட்சியில் சேருவதற்கு மட்டுமே தடை விதிக்கப்பட்டுள்ளார், ஆனால் கட்சியில் சேராத வரை அமைச்சர் பதவியை ஏற்பதற்கு எந்தத் தடையுமில்லை."),

        # 26
        ("Paragraph 1 Definitions",
         "Under Paragraph 1 of the Tenth Schedule, what is the meaning of 'legislature party'?",
         "பத்தாவது அட்டவணையின் பத்தி 1-ன் கீழ், 'சட்டமன்றக் கட்சி' (legislature party) என்பதன் பொருள் என்ன?",
         [("The group consisting of all elected members of that House belonging to that political party", "அந்த அரசியல் கட்சியைச் சேர்ந்த அந்த அவையின் அனைத்து தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களையும் கொண்ட குழு"),
          ("The national executive committee of the political party", "அரசியல் கட்சியின் தேசிய செயற்குழு"),
          ("The parliamentary board that issues election tickets", "தேர்தல் சின்னங்களை வழங்கும் நாடாளுமன்ற வாரியம்"),
          ("The coalition of all political parties in the House", "அவையில் உள்ள அனைத்து அரசியல் கட்சிகளின் கூட்டணி")],
         "A",
         "Paragraph 1(b) defines 'legislature party' in relation to a member of a House as the group consisting of all the members of that House for the time being belonging to that political party.",
         "பத்தி 1(b) 'சட்டமன்றக் கட்சி' என்பதை, அந்த அரசியல் கட்சியைச் சேர்ந்த அந்த அவையின் அனைத்து உறுப்பினர்களையும் கொண்ட குழு என வரையறுக்கிறது."),

        # 27
        ("Paragraph 1 Original Party",
         "Under Paragraph 1 of the Tenth Schedule, what is the 'original political party'?",
         "பத்தாவது அட்டவணையின் பத்தி 1-ன் கீழ், 'மூல அரசியல் கட்சி' (original political party) என்பது எது?",
         [("The political party on whose ticket or symbol the member was set up as a candidate for election", "எந்த அரசியல் கட்சியின் சின்னம் அல்லது பரிந்துரையின் கீழ் உறுப்பினர் தேர்தலில் வேட்பாளராக நிறுத்தப்பட்டாரோ அக்கட்சி"),
          ("The oldest registered political party in the State", "மாநிலத்தில் உள்ள மிகவும் பழமையான பதிவு செய்யப்பட்ட அரசியல் கட்சி"),
          ("The ruling party at the Centre at the time of election", "தேர்தல் நேரத்தில் மத்தியில் ஆளும் கட்சி"),
          ("The party with the highest number of members in Parliament", "நாடாளுமன்றத்தில் அதிக உறுப்பினர்களைக் கொண்ட கட்சி")],
         "A",
         "Paragraph 1(c) defines 'original political party' as the political party to which a member belongs for the purposes of section (1) of Paragraph 2, being the party which set him up as a candidate.",
         "பத்தி 1(c) 'மூல அரசியல் கட்சி' என்பதை, உறுப்பினரைத் தேர்தலில் வேட்பாளராக நிறுத்திய அரசியல் கட்சி என வரையறுக்கிறது."),

        # 28
        ("Cross Voting Without Condonation",
         "An MLA votes against his party's nominee in a Rajya Sabha election. Does this cross-voting automatically trigger defection under Paragraph 2(1)(b)?",
         "ஒரு எம்.எல்.ஏ மாநிலங்களவைத் தேர்தலில் தனது கட்சியின் வேட்பாளருக்கு எதிராக வாக்களிக்கிறார். இந்த கட்சி மாறி வாக்களிப்பது பத்தி 2(1)(b)-ன் கீழ் தானாகவே கட்சித் தாவலை ஏற்படுத்துமா?",
         [("No, because a Rajya Sabha election is governed by open ballot rules under RPA 1951 and is not a proceeding of the Assembly", "இல்லை, ஏனெனில் மாநிலங்களவைத் தேர்தல் மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் கீழ் திறந்த வாக்கெடுப்பு விதிகளால் நிர்வகிக்கப்படுகிறது மற்றும் சட்டமன்ற நடவடிக்கை அல்ல"),
          ("Yes, all cross-voting results in immediate disqualification", "ஆம், அனைத்து கட்சி மாறி வாக்களிப்பும் உடனடி தகுதி நீக்கத்தை ஏற்படுத்துகிறது"),
          ("Only if the MLA admits his cross-vote to the media", "எம்.எல்.ஏ தனது மாற்று வாக்கை ஊடகங்களிடம் ஒப்புக்கொண்டால் மட்டுமே"),
          ("Only if the returning officer files a police complaint", "தேர்தல் நடத்தும் அலுவலர் காவல் நிலையத்தில் புகார் அளித்தால் மட்டுமே")],
         "A",
         "As settled in Kuldip Nayar (2006), elections to the Rajya Sabha are not proceedings in the House under Article 194 and the Tenth Schedule does not apply to votes cast in such elections.",
         "குல்தீப் நாயர் (2006) தீர்ப்பின்படி, மாநிலங்களவைத் தேர்தல்கள் அவையின் நடவடிக்கைகள் அல்ல, எனவே அத்தகைய தேர்தல்களில் அளிக்கப்படும் வாக்குகளுக்கு பத்தாவது அட்டவணை பொருந்தாது."),

        # 29
        ("Speaker Resignation Acceptance Delay",
         "If the Speaker deliberately delays accepting an MLA's genuine and voluntary resignation, can the High Court intervene?",
         "ஒரு எம்.எல்.ஏ-வின் உண்மையான மற்றும் தானாக முன்வந்த ராஜினாமாவை ஏற்பதை சபாநாயகர் வேண்டுமென்றே தாமதப்படுத்தினால், உயர் நீதிமன்றம் தலையிட முடியுமா?",
         [("Yes, under Article 226, courts can issue directions to the Speaker to perform his constitutional duty without arbitrary delay", "ஆம், உறுப்பு 226-ன் கீழ், தன்னிச்சையான தாமதமின்றி தனது அரசியலமைப்பு கடமையைச் செய்ய சபாநாயகருக்கு நீதிமன்றங்கள் உத்தரவிட முடியும்"),
          ("No, courts have zero jurisdiction over the Speaker's desk at any time", "இல்லை, எந்த நேரத்திலும் சபாநாயகரின் அலுவலகம் மீது நீதிமன்றங்களுக்கு அதிகாரம் இல்லை"),
          ("Only if the Governor orders the High Court to intervene", "உயர் நீதிமன்றத்தைத் தலையிடுமாறு ஆளுநர் உத்தரவிட்டால் மட்டுமே"),
          ("Only after the five-year term of the Assembly expires", "சட்டமன்றத்தின் ஐந்து ஆண்டு காலம் முடிந்த பின்னரே")],
         "A",
         "While courts do not grant quia timet stays, arbitrary or mala fide inaction by constitutional authorities is subject to judicial review under Article 226 (Karnataka MLAs case 2019, Manipur case 2020).",
         "நீதிமன்றங்கள் முன்கூட்டியே தடை விதிக்காவிட்டாலும், அரசியலமைப்பு அதிகாரிகளின் தன்னிச்சையான செயலற்ற தன்மை உறுப்பு 226-ன் கீழ் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது."),

        # 30
        ("Defection Petition Withdrawal",
         "Can a petitioner who filed a defection petition against an MLA withdraw the petition without the Speaker's consent?",
         "ஒரு எம்.எல்.ஏ-வுக்கு எதிராகக் கட்சித் தாவல் மனு தாக்கல் செய்த மனுதாரர், சபாநாயகரின் அனுமதியின்றி அம்மனுவை திரும்பப் பெற முடியுமா?",
         [("No, once filed, Tenth Schedule proceedings are matters of constitutional integrity and require Speaker's permission to withdraw", "முடியாது, தாக்கல் செய்யப்பட்டவுடன் பத்தாவது அட்டவணை நடவடிக்கைகள் அரசியலமைப்பு மாண்பு தொடர்பானவை மற்றும் திரும்பப் பெற சபாநாயகரின் அனுமதி தேவை"),
          ("Yes, a petitioner has absolute unilateral right to withdraw anytime", "ஆம், எப்போது வேண்டுமானாலும் ஒருதலைப்பட்சமாகத் திரும்பப் பெற மனுதாரருக்கு முழு உரிமை உண்டு"),
          ("Only if the defector pays compensation to the House", "கட்சி தாவியவர் அவைக்கு நஷ்டஈடு செலுத்தினால் மட்டுமே"),
          ("Only if the Chief Minister consents in writing", "முதலமைச்சர் எழுத்துப்பூர்வமாக ஒப்புதல் அளித்தால் மட்டுமே")],
         "A",
         "Under the Disqualification Rules framed by various State Assemblies, a petition once admitted cannot be withdrawn unilaterally without the leave of the Speaker, as defection affects the public interest of the electorate.",
         "பல்வேறு சட்டமன்றங்களால் உருவாக்கப்பட்ட விதிகளின்படி, மனு ஏற்றுக்கொள்ளப்பட்ட பிறகு சபாநாயகரின் அனுமதியின்றி ஒருதலைப்பட்சமாகத் திரும்பப் பெற முடியாது, ஏனெனில் கட்சித் தாவல் பொது நலனைப் பாதிக்கிறது.")
    ]

    for idx, item in enumerate(rich_medium_items, start=21):
        raw_medium[idx - 1] = {
            "subtopic": item[0],
            "stem_en": item[1],
            "stem_ta": item[2],
            "options": item[3],
            "correct_key": item[4],
            "exp_en": item[5],
            "exp_ta": item[6],
            "why_a_en": f"Correct. {item[5][:100]}",
            "why_a_ta": f"சரி. {item[6][:100]}",
            "why_b_en": "Incorrect. Contrasts directly with established constitutional law.",
            "why_b_ta": "தவறு. நிறுவப்பட்ட அரசியலமைப்புச் சட்டத்திற்கு முரணானது.",
            "why_c_en": "Incorrect. Not a valid legal test under the Tenth Schedule.",
            "why_c_ta": "தவறு. பத்தாவது அட்டவணையின் கீழ் இது செல்லுபடியாகும் சட்டப் பரிசோதனை அல்ல.",
            "why_d_en": "Incorrect. Factually and constitutionally erroneous proposition.",
            "why_d_ta": "தவறு. உண்மை மற்றும் அரசியலமைப்பு ரீதியாக தவறான கருத்து.",
            "tip_en": "Deep conceptual understanding of Tenth Schedule jurisprudence is essential for TNPSC.",
            "tip_ta": "பத்தாவது அட்டவணையின் ஆழமான கருத்துப் புரிதல் டிஎன்பிஎஸ்சி தேர்வுக்கு இன்றியமையாதது.",
            "fact_en": "Tenth Schedule cases have generated extensive Supreme Court Constitution Bench jurisprudence.",
            "fact_ta": "பத்தாவது அட்டவணை வழக்குகள் விரிவான உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வுத் தீர்ப்புகளை உருவாக்கியுள்ளன."
        }

    return raw_medium


def build_medium_file():
    raw_medium = get_medium_questions()
    print(f"Loaded {len(raw_medium)} raw Medium questions for Anti-Defection Law.")
    assert len(raw_medium) == 50, f"Expected 50 items, got {len(raw_medium)}"

    questions = []
    for idx, item in enumerate(raw_medium, start=1):
        qid = f"ADL_M_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_adl_q(
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
            tags=["polity", "anti_defection_law", "medium", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    balanced = randomize_and_balance_dataset(questions, seed=43)
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "anti_defection_law_medium.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Medium MCQs to {out_path}")

    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="ADL_M_")
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
