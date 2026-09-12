# -*- coding: utf-8 -*-
"""
Grand Test Batch 4: SCH_GT_076 to SCH_GT_100
Covers:
- Ninth Schedule (076)
- Tenth Schedule (077-084)
- Eleventh Schedule (085-092)
- Twelfth Schedule (093-100)
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import make_sch_q

def get_batch4():
    qs = []

    # GT076
    qs.append(make_sch_q(
        "SCH_GT_076", "Medium", "Conceptual", "Ninth Schedule",
        "What was the primary socio-economic objective behind creating the Ninth Schedule via the 1st Constitutional Amendment Act in 1951?",
        "1951-ல் 1வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் ஒன்பதாவது அட்டவணையை உருவாக்கியதன் முதன்மையான சமூக-பொருளாதார நோக்கம் என்ன?",
        "To protect agrarian land reform and abolition of Zamindari laws from judicial invalidation under fundamental rights", "விவசாய நிலச் சீர்திருத்தம் மற்றும் ஜமீன்தாரி ஒழிப்புச் சட்டங்களை அடிப்படை உரிமைகளின் கீழான நீதிமன்ற ரத்திலிருந்து பாதுகாப்பது",
        "To establish special economic export processing zones along coastal ports", "கடலோர துறைமுகங்களில் சிறப்பு பொருளாதார ஏற்றுமதி மண்டலங்களை நிறுவுவது",
        "To nationalize all private commercial banking institutions across the country", "நாடு முழுவதும் உள்ள அனைத்து தனியார் வணிக வங்கிகளையும் தேசியமயமாக்குவது",
        "To create a unified national goods and services indirect tax regime", "ஒருங்கிணைந்த தேசிய சரக்கு மற்றும் சேவை மறைமுக வரி முறையை உருவாக்குவது",
        "A",
        "The primary purpose of inserting Article 31B and the Ninth Schedule in 1951 was to immunize state land reform legislations (abolition of Zamindari and Jagirdari systems) from challenges under Articles 14, 19, and 31.",
        "1951-ல் சரத்து 31B மற்றும் ஒன்பதாவது அட்டவணையைச் சேர்த்ததன் முதன்மை நோக்கம், மாநில நிலச் சீர்திருத்தச் சட்டங்களை (ஜமீன்தாரி மற்றும் ஜாகிர்தாரி ஒழிப்பு) சரத்துகள் 14, 19 மற்றும் 31-ன் கீழான சவால்களிலிருந்து பாதுகாப்பதாகும்.",
        "Correct. Protecting Zamindari abolition and agrarian land reforms was the foundational purpose.", "சரியானது. ஜமீன்தாரி ஒழிப்பு மற்றும் நிலச் சீர்திருத்தங்களைப் பாதுகாப்பதே தொடக்க நோக்கமாகும்.",
        "Incorrect. SEZs were created decades later under modern trade policies.", "தவறானது. சிறப்பு பொருளாதார மண்டலங்கள் பல தசாப்தங்களுக்குப் பின் உருவாக்கப்பட்டன.",
        "Incorrect. Bank nationalization occurred in 1969/1980.", "தவறானது. வங்கிகள் தேசியமயமாக்கல் 1969/1980-ல் நடைபெற்றது.",
        "Incorrect. GST was created via the 101st Amendment in 2016.", "தவறானது. ஜிஎஸ்டி 2016-ல் 101வது திருத்தம் மூலம் உருவாக்கப்பட்டது.",
        "Origin of Ninth Schedule: Overcoming judicial strikes against Bihar Land Reforms Act in Kameshwar Singh case (1951).",
        "ஒன்பதாவது அட்டவணையின் தோற்றம்: காமேஷ்வர் சிங் வழக்கில் (1951) பீகார் நிலச் சீர்திருத்தச் சட்டம் ரத்து செய்யப்பட்டதை முறியடிக்க உருவாக்கப்பட்டது."
    ))

    # GT077
    qs.append(make_sch_q(
        "SCH_GT_077", "Easy", "Conceptual", "Tenth Schedule",
        "Under Paragraph 2(1)(a) of the Tenth Schedule, when does an elected member of a House belonging to any political party incur disqualification?",
        "பத்தாவது அட்டவணையின் பத்தி 2(1)(a)-ன் கீழ், எந்தவொரு அரசியல் கட்சியைச் சேர்ந்த தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் எப்போது தகுதியிழப்புக்கு ஆளாகிறார்?",
        "If the member voluntarily gives up membership of such political party", "அவர் அத்தகைய அரசியல் கட்சியின் உறுப்பினர் பதவியை தானாக முன்வந்து துறந்தால்",
        "If the member criticizes a municipal policy in a private blog post", "ஒரு உறுப்பினர் ஒரு தனிப்பட்ட வலைப்பதிவில் நகராட்சி கொள்கையை விமர்சித்தால்",
        "If the member is absent from a parliamentary committee meeting due to illness", "உடல்நலக்குறைவு காரணமாக ஒரு பாராளுமன்றக் குழுக் கூட்டத்திற்கு வராமல் இருந்தால்",
        "If the member attends an international cultural exchange conference", "ஒரு சர்வதேச கலாச்சார பரிமாற்ற மாநாட்டில் கலந்து கொண்டால்",
        "A",
        "Paragraph 2(1)(a) of the Tenth Schedule provides that a member of a House belonging to any political party shall be disqualified for being a member of the House if he has voluntarily given up his membership of such political party.",
        "பத்தாவது அட்டவணையின் பத்தி 2(1)(a) குறிப்பிடுகிறது: ஒரு அரசியல் கட்சியைச் சார்ந்த அவையின் உறுப்பினர் ஒருவர், அத்தகைய அரசியல் கட்சியின் உறுப்பினர் பதவியை தானாக முன்வந்து துறந்தால் அவர் அவையின் உறுப்பினராக இருப்பதற்கு தகுதியற்றவர் ஆவார்.",
        "Correct. Voluntarily giving up membership is the primary ground under Para 2(1)(a).", "சரியானது. தானாக முன்வந்து உறுப்பினர் பதவியைத் துறப்பது பத்தி 2(1)(a)-ன் கீழான முதன்மைக் காரணமாகும்.",
        "Incorrect. Criticizing a policy in private speech does not invoke defection.", "தவறானது. தனிப்பட்ட பேச்சில் கொள்கையை விமர்சிப்பது கட்சித்தாவல் ஆகாது.",
        "Incorrect. Committee absence does not invoke defection.", "தவறானது. குழுக் கூட்டத்திற்கு வராமல் இருப்பது கட்சித்தாவல் ஆகாது.",
        "Incorrect. Attending conferences is permitted.", "தவறானது. மாநாடுகளில் பங்கேற்பது அனுமதிக்கப்படுகிறது.",
        "Paragraph 2(1)(a): Resignation from party or actions implying severance triggers disqualification.",
        "பத்தி 2(1)(a): கட்சியிலிருந்து விலகுதல் அல்லது விலகுவதைக் குறிக்கும் செயல்கள் தகுதியிழப்பைத் தூண்டுகின்றன."
    ))

    # GT078
    qs.append(make_sch_q(
        "SCH_GT_078", "Hard", "Conceptual", "Tenth Schedule",
        "In the landmark Ravi S. Naik v. Union of India (1994) case, how did the Supreme Court interpret the phrase 'voluntarily gives up his membership' in the Tenth Schedule?",
        "வரலாற்றுச் சிறப்புமிக்க ரவி எஸ். நாயக் எதிர் இந்திய யூனியன் (1994) வழக்கில், பத்தாவது அட்டவணையில் உள்ள 'தானாக முன்வந்து தனது உறுப்பினர் பதவியைத் துறத்தல்' என்ற சொற்றொடரை உச்சநீதிமன்றம் எவ்வாறு விளக்கியது?",
        "It has a wider connotation than formal resignation; conduct can demonstrate that a member has voluntarily given up membership", "இது முறையான ராஜினாமாவை விட பரந்த பொருளைக் கொண்டது; ஒரு உறுப்பினரின் நடத்தை அவர் தானாக முன்வந்து பதவியைத் துறந்துள்ளார் என்பதைக் காட்ட முடியும்",
        "It strictly requires a formal written and notarized resignation letter submitted directly to the party president", "கட்சித் தலைவரிடம் நேரடியாகச் சமர்ப்பிக்கப்படும் முறையான எழுத்துப்பூர்வமான மற்றும் நோட்டரி செய்யப்பட்ட ராஜினாமாக் கடிதம் கண்டிப்பாகத் தேவை",
        "It applies only if a member formally joins an internationally banned terrorist organization", "ஒரு உறுப்பினர் சர்வதேச அளவில் தடைசெய்யப்பட்ட பயங்கரவாத அமைப்பில் முறையாக இணைந்தால் மட்டுமே பொருந்தும்",
        "It requires a unanimous resolution passed by the national executive committee of the party", "கட்சியின் தேசிய செயற்குழுவால் நிறைவேற்றப்படும் ஏகமனதான தீர்மானம் தேவைப்படுகிறது",
        "A",
        "In Ravi S. Naik (1994), the Supreme Court clarified that 'voluntarily gives up membership' is not synonymous with resignation. Even in the absence of a formal resignation, an inference can be drawn from the conduct of a member (such as publicly aligning with opposition) that they have voluntarily given up membership.",
        "ரவி எஸ். நாயக் (1994) வழக்கில், உச்சநீதிமன்றம் தெளிவுபடுத்தியது: 'தானாக முன்வந்து உறுப்பினர் பதவியைத் துறப்பது' என்பது ராஜினாமா செய்வதற்கு இணையானது அல்ல. முறையான ராஜினாமா கடிதம் இல்லாவிட்டாலும், ஒரு உறுப்பினரின் நடத்தையிலிருந்து (எதிர்க்கட்சியுடன் வெளிப்படையாக இணைவது போன்றவை) அவர் தானாகவே உறுப்பினர் பதவியைத் துறந்துவிட்டார் என்று முடிவு செய்யலாம்.",
        "Correct. Conduct-based inference was established in Ravi S. Naik (1994).", "சரியானது. நடத்தை அடிப்படையிலான முடிவு ரவி எஸ். நாயக் வழக்கில் (1994) நிறுவப்பட்டது.",
        "Incorrect. Written resignation is not mandatory to establish defection.", "தவறானது. கட்சித்தாவலை நிறுவ எழுத்துப்பூர்வ ராஜினாமா கட்டாயமில்லை.",
        "Incorrect. Terrorist ban has no connection to Tenth Schedule jurisprudence.", "தவறானது. பயங்கரவாத தடைக்கும் பத்தாவது அட்டவணைக்கும் தொடர்பில்லை.",
        "Incorrect. National executive resolution is not a constitutional prerequisite.", "தவறானது. தேசிய செயற்குழு தீர்மானம் அரசியலமைப்பு முன்நிபந்தனை அல்ல.",
        "Ravi S. Naik Principle: Supporting another party or defying whip outside assembly can constitute 'voluntarily giving up membership'.",
        "ரவி எஸ். நாயக் கோட்பாடு: மற்றொரு கட்சியை ஆதரிப்பது அல்லது கட்சிக்கு எதிராக செயல்படுவது 'தானாக முன்வந்து உறுப்பினர் பதவியைத் துறத்தல்' ஆகும்."
    ))

    # GT079
    qs.append(make_sch_q(
        "SCH_GT_079", "Medium", "Conceptual", "Tenth Schedule",
        "Under Paragraph 2(1)(b) of the Tenth Schedule, within how many days must a political party condone unauthorized voting or abstention to prevent a member's disqualification?",
        "பத்தாவது அட்டவணையின் பத்தி 2(1)(b)-ன் கீழ், ஒரு உறுப்பினரின் தகுதியிழப்பைத் தடுக்க, அனுமதியற்ற வாக்களிப்பு அல்லது வாக்கெடுப்பைப் புறக்கணித்ததை அரசியல் கட்சி எத்தனை நாட்களுக்குள் மன்னிக்க வேண்டும்?",
        "Within 15 days from the date of such voting or abstention", "அத்தகைய வாக்களிப்பு அல்லது புறக்கணிப்பு நடந்த தேதியிலிருந்து 15 நாட்களுக்குள்",
        "Within 30 days from the date of the session's adjournment", "கூட்டத்தொடர் ஒத்திவைக்கப்பட்ட தேதியிலிருந்து 30 நாட்களுக்குள்",
        "Within 7 days from the issuance of a show-cause notice", "காரணம் கேட்கும் அறிவிப்பு வெளியிடப்பட்ட 7 நாட்களுக்குள்",
        "Within 60 days following the Speaker's formal inquiry", "சபாநாயகரின் முறையான விசாரணைக்கு பின் 60 நாட்களுக்குள்",
        "A",
        "Paragraph 2(1)(b) provides that voting or abstaining contrary to the party direction (whip) disqualifies a member unless such voting or abstention is condoned by the political party within 15 days from the date of such voting or abstention.",
        "பத்தி 2(1)(b) குறிப்பிடுகிறது: கட்சி உத்தரவுக்கு (கொறடா) மாறாக வாக்களிப்பது அல்லது வாக்கெடுப்பைப் புறக்கணிப்பது ஒரு உறுப்பினரைத் தகுதியிழக்கச் செய்யும்; அத்தகைய வாக்களிப்பு அல்லது புறக்கணிப்பு நடந்த தேதியிலிருந்து 15 நாட்களுக்குள் அரசியல் கட்சியால் மன்னிக்கப்பட்டால் மட்டுமே தகுதியிழப்பு ஏற்படாது.",
        "Correct. 15 days is the strict constitutional window for party condonation.", "சரியானது. கட்சியின் மன்னிப்பிற்கு 15 நாட்கள் என்பது கடுமையான அரசியலமைப்பு அவகாசமாகும்.",
        "Incorrect. 30 days is incorrect.", "தவறானது. 30 நாட்கள் என்பது தவறானது.",
        "Incorrect. 7 days is incorrect.", "தவறானது. 7 நாட்கள் என்பது தவறானது.",
        "Incorrect. 60 days is incorrect.", "தவறானது. 60 நாட்கள் என்பது தவறானது.",
        "Whip Condonation: Political party has exactly 15 days to condone defiance of whip under Paragraph 2(1)(b).",
        "கொறடா மன்னிப்பு: பத்தி 2(1)(b)-ன் கீழ் கொறடா மீறலை மன்னிக்க அரசியல் கட்சிக்கு சரியாக 15 நாட்கள் அவகாசம் உள்ளது."
    ))

    # GT080
    qs.append(make_sch_q(
        "SCH_GT_080", "Medium", "Conceptual", "Tenth Schedule",
        "What major structural amendment was made to the Tenth Schedule by the 91st Constitutional Amendment Act, 2003 regarding splits in political parties?",
        "அரசியல் கட்சிகளில் ஏற்படும் பிளவுகள் தொடர்பாக 91வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003 மூலம் பத்தாவது அட்டவணையில் செய்யப்பட்ட முக்கிய கட்டமைப்புத் திருத்தம் என்ன?",
        "Omitted Paragraph 3, thereby deleting the defense of one-third split in a political party", "பத்தி 3-ஐ நீக்கியது, இதன் மூலம் அரசியல் கட்சியில் மூன்றில் ஒரு பங்கு பிளவு என்ற பாதுகாப்பை ரத்து செய்தது",
        "Reduced the required merger threshold from two-thirds to one-half", "இணைப்புக்குத் தேவையான வரம்பை மூன்றில் இரண்டிலிருந்து பாதியாகக் குறைத்தது",
        "Transferred the deciding authority from the Speaker to the Chief Election Commissioner", "முடிவெடுக்கும் அதிகாரத்தை சபாநாயகரிடமிருந்து தலைமை தேர்தல் ஆணையருக்கு மாற்றியது",
        "Exempted all Rajya Sabha members from the application of anti-defection law", "அனைத்து மாநிலங்களவை உறுப்பினர்களுக்கும் கட்சித்தாவல் சட்டத்திலிருந்து விலக்கு அளித்தது",
        "A",
        "The 91st Constitutional Amendment Act, 2003 omitted Paragraph 3 of the Tenth Schedule, which had previously protected members from disqualification if at least one-third of the legislature party split away. Now, only mergers (Paragraph 4) are recognized.",
        "91வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003, பத்தாவது அட்டவணையின் பத்தி 3-ஐ நீக்கியது; இது முன்னர் சட்டமன்றக் கட்சியில் மூன்றில் ஒரு பங்கு உறுப்பினர்கள் பிரிந்தால் தகுதியிழப்பிலிருந்து பாதுகாப்பளித்தது. இப்போது இணைப்புகள் (பத்தி 4) மட்டுமே அங்கீகரிக்கப்படுகின்றன.",
        "Correct. 91st CAA deleted Paragraph 3 (the 1/3rd split loophole).", "சரியானது. 91வது திருத்தம் பத்தி 3-ஐ (1/3 பிளவு ஓட்டை) நீக்கியது.",
        "Incorrect. Merger threshold remains two-thirds under Paragraph 4.", "தவறானது. இணைப்பு வரம்பு பத்தி 4-ன் கீழ் 2/3 ஆக நீடிக்கிறது.",
        "Incorrect. Speaker remains the deciding authority.", "தவறானது. சபாநாயகரே முடிவெடுக்கும் அதிகாரியாகத் தொடர்கிறார்.",
        "Incorrect. Rajya Sabha members remain fully covered by the Tenth Schedule.", "தவறானது. மாநிலங்களவை உறுப்பினர்கள் தொடர்ந்து பத்தாவது அட்டவணைக்கு உட்பட்டவர்களே.",
        "91st CAA 2003: Abolished 1/3rd split defense; capped council of ministers at 15% (Art 75(1A) & 164(1A)).",
        "91வது திருத்தம் 2003: 1/3 பங்கு பிளவு பாதுகாப்பை ஒழித்தது; அமைச்சரவை அளவை 15% ஆகக் கட்டுப்படுத்தியது (சரத்து 75(1A) & 164(1A))."
    ))

    # GT081
    qs.append(make_sch_q(
        "SCH_GT_081", "Easy", "Conceptual", "Tenth Schedule",
        "Under Paragraph 4(2) of the Tenth Schedule, a merger of a political party is recognized only if what fraction of the members of the legislature party agree to such merger?",
        "பத்தாவது அட்டவணையின் பத்தி 4(2)-ன் கீழ், சட்டமன்றக் கட்சியின் உறுப்பினர்களில் எத்தனை பங்கு உறுப்பினர்கள் அத்தகைய இணைப்பிற்கு ஒப்புக்கொண்டால் மட்டுமே ஒரு அரசியல் கட்சியின் இணைப்பு அங்கீகரிக்கப்படும்?",
        "Not less than two-thirds (2/3rds) of the members of the legislature party", "சட்டமன்றக் கட்சியின் உறுப்பினர்களில் மூன்றில் இரண்டு பங்குக்கு (2/3) குறையாதவர்கள்",
        "At least one-third (1/3rd) of the members of the legislature party", "சட்டமன்றக் கட்சியின் உறுப்பினர்களில் குறைந்தபட்சம் மூன்றில் ஒரு பங்கு (1/3)",
        "At least three-fourths (3/4ths) of the members of the legislature party", "சட்டமன்றக் கட்சியின் உறுப்பினர்களில் குறைந்தபட்சம் நான்கில் மூன்று பங்கு (3/4)",
        "A simple majority of 50% plus one member of the legislature party", "சட்டமன்றக் கட்சியின் எளிய பெரும்பான்மையான 50% மற்றும் ஒரு உறுப்பினர்",
        "A",
        "Paragraph 4(2) of the Tenth Schedule provides that the merger of the original political party of a member of a House shall be deemed to have taken place if, and only if, not less than two-thirds of the members of the legislature party concerned have agreed to such merger.",
        "பத்தாவது அட்டவணையின் பத்தி 4(2) குறிப்பிடுகிறது: சம்பந்தப்பட்ட சட்டமன்றக் கட்சியின் உறுப்பினர்களில் மூன்றில் இரண்டு பங்குக்குக் குறையாதவர்கள் அத்தகைய இணைப்பிற்கு ஒப்புக்கொண்டால் மட்டுமே மூல அரசியல் கட்சியின் இணைப்பு நடந்ததாகக் கருதப்படும்.",
        "Correct. Merger requires agreement of not less than 2/3rds of legislature party members.", "சரியானது. இணைப்பிற்கு சட்டமன்றக் கட்சி உறுப்பினர்களில் 2/3 பங்கு குறையாமல் ஒப்புதல் தேவை.",
        "Incorrect. 1/3rd was the old split threshold deleted by the 91st CAA.", "தவறானது. 1/3 என்பது 91வது திருத்தத்தால் நீக்கப்பட்ட பழைய பிளவு வரம்பு.",
        "Incorrect. 3/4ths is incorrect.", "தவறானது. 3/4 என்பது தவறானது.",
        "Incorrect. Simple majority is insufficient for constitutional merger defense.", "தவறானது. அரசியலமைப்பு இணைப்புப் பாதுகாப்பிற்கு எளிய பெரும்பான்மை போதாது.",
        "Merger Rule (Tenth Schedule Para 4): 2/3rds of the legislature party must agree to merge into another party.",
        "இணைப்பு விதி (பத்தாவது அட்டவணை பத்தி 4): மற்றொரு கட்சியுடன் இணைய சட்டமன்றக் கட்சியின் 2/3 பங்கு உறுப்பினர்கள் ஒப்புக்கொள்ள வேண்டும்."
    ))

    # GT082
    qs.append(make_sch_q(
        "SCH_GT_082", "Hard", "Conceptual", "Tenth Schedule",
        "In Keisham Meghachandra Singh v. Hon'ble Speaker, Manipur (2020), what outer time frame did the Supreme Court suggest for the Speaker to decide disqualification petitions under the Tenth Schedule?",
        "கெய்ஷம் மேகசந்திர சிங் எதிர் மணிப்பூர் சபாநாயகர் (2020) வழக்கில், பத்தாவது அட்டவணையின் கீழான தகுதியிழப்பு மனுக்கள் மீது முடிவெடுக்க சபாநாயகருக்கு உச்சநீதிமன்றம் பரிந்துரைத்த அதிகபட்ச கால வரம்பு என்ன?",
        "Within a reasonable period, ordinarily 3 months, absent exceptional circumstances", "விதிவிலக்கான சூழ்நிலைகள் இல்லாத வரை, பொதுவாக 3 மாதங்களுக்குள் நியாயமான காலத்திற்குள்",
        "Within exactly 14 days from the date of petition filing", "மனு தாக்கல் செய்யப்பட்ட தேதியிலிருந்து சரியாக 14 நாட்களுக்குள்",
        "Within 6 months from the end of the legislative budget session", "சட்டமன்ற பட்ஜெட் கூட்டத்தொடர் முடிவடைந்த 6 மாதங்களுக்குள்",
        "Within 1 year with automatic transfer to the High Court thereafter", "1 ஆண்டிற்குள், அதன் பிறகு தானாக உயர்நீதிமன்றத்திற்கு மாற்றப்படும் வகையில்",
        "A",
        "In Keisham Meghachandra Singh (2020), a 3-judge bench headed by Justice R.F. Nariman ruled that the Speaker must decide disqualification petitions within a reasonable period, ordinarily within three months, and recommended establishing an independent tribunal to replace the Speaker for deciding defection petitions.",
        "கெய்ஷம் மேகசந்திர சிங் (2020) வழக்கில், நீதிபதி ஆர்.எஃப். நாரிமன் தலைமையிலான 3 நீதிபதிகள் கொண்ட அமர்வு, சபாநாயகர் தகுதியிழப்பு மனுக்களை ஒரு நியாயமான காலத்திற்குள் (பொதுவாக மூன்று மாதங்களுக்குள்) தீர்மானிக்க வேண்டும் என்றும், கட்சித்தாவல் மனுக்களை விசாரிக்க சபாநாயகருக்குப் பதிலாக ஒரு சுயாதீன தீர்ப்பாயத்தை உருவாக்கப் பரிந்துரைத்தது.",
        "Correct. Keisham Meghachandra Singh (2020) suggested 3 months ordinarily.", "சரியானது. கெய்ஷம் மேகசந்திர சிங் வழக்கு பொதுவாக 3 மாத காலத்தை பரிந்துரைத்தது.",
        "Incorrect. 14 days is incorrect.", "தவறானது. 14 நாட்கள் என்பது தவறானது.",
        "Incorrect. 6 months is incorrect.", "தவறானது. 6 மாதங்கள் என்பது தவறானது.",
        "Incorrect. 1 year is incorrect.", "தவறானது. 1 ஆண்டு என்பது தவறானது.",
        "Keisham Meghachandra Case (2020): Supreme Court prescribed 3-month norm for Speakers to decide defection cases.",
        "கெய்ஷம் மேகசந்திர வழக்கு (2020): கட்சித்தாவல் வழக்குகளைத் தீர்க்க சபாநாயகர்களுக்கு 3 மாத கால விதிமுறையை உச்சநீதிமன்றம் பரிந்துரைத்தது."
    ))

    # GT083
    qs.append(make_sch_q(
        "SCH_GT_083", "Hard", "Conceptual", "Tenth Schedule",
        "In the landmark Kihoto Hollohan v. Zachillhu (1992) judgment, which Paragraph of the Tenth Schedule was declared unconstitutional by the Supreme Court?",
        "வரலாற்றுச் சிறப்புமிக்க கிகோட்டோ ஹோல்லோஹன் எதிர் ஜாச்சில்கு (1992) தீர்ப்பில், பத்தாவது அட்டவணையின் எந்தப் பத்தி உச்சநீதிமன்றத்தால் அரசியலமைப்பிற்கு முரணானது என அறிவிக்கப்பட்டது?",
        "Paragraph 7 (which excluded the jurisdiction of all courts over defection decisions)", "பத்தி 7 (கட்சித்தாவல் முடிவுகள் மீதான அனைத்து நீதிமன்றங்களின் அதிகார வரம்பையும் விலக்கியது)",
        "Paragraph 2 (which prescribed grounds for disqualification on defection)", "பத்தி 2 (கட்சித்தாவல் மீதான தகுதியிழப்புக்கான காரணங்களைக் குறிப்பிட்டது)",
        "Paragraph 4 (which recognized party mergers with two-thirds majority)", "பத்தி 4 (மூன்றில் இரண்டு பெரும்பான்மையுடன் கட்சி இணைப்புகளை அங்கீகரித்தது)",
        "Paragraph 6 (which made the Speaker's decision final)", "பத்தி 6 (சபாநாயகரின் முடிவை இறுதியானது என அறிவித்தது)",
        "A",
        "In Kihoto Hollohan (1992), the Supreme Court struck down Paragraph 7 of the Tenth Schedule because it took away the jurisdiction of High Courts (Art 226) and the Supreme Court (Art 136) without ratification by the states under Article 368(2). However, the rest of the Tenth Schedule was upheld, and the Speaker's decision was made subject to judicial review.",
        "கிகோட்டோ ஹோல்லோஹன் (1992) வழக்கில், உச்சநீதிமன்றம் பத்தாவது அட்டவணையின் பத்தி 7-ஐ ரத்து செய்தது; ஏனெனில் அது சரத்து 368(2)-ன் கீழ் மாநிலங்களின் ஒப்புதல் பெறாமல் உயர்நீதிமன்றங்கள் (சரத்து 226) மற்றும் உச்சநீதிமன்றத்தின் (சரத்து 136) அதிகார வரம்பைப் பறித்தது. இருப்பினும் பிற பகுதிகள் உறுதி செய்யப்பட்டு, சபாநாயகரின் முடிவு நீதிப் புனராய்வுக்கு உட்படுத்தப்பட்டது.",
        "Correct. Paragraph 7 was struck down in Kihoto Hollohan (1992).", "சரியானது. கிகோட்டோ ஹோல்லோஹன் வழக்கில் பத்தி 7 ரத்து செய்யப்பட்டது.",
        "Incorrect. Paragraph 2 was upheld.", "தவறானது. பத்தி 2 உறுதி செய்யப்பட்டது.",
        "Incorrect. Paragraph 4 was upheld.", "தவறானது. பத்தி 4 உறுதி செய்யப்பட்டது.",
        "Incorrect. Paragraph 6 was upheld subject to judicial review.", "தவறானது. பத்தி 6 நீதிப் புனராய்வுக்கு உட்பட்டு உறுதி செய்யப்பட்டது.",
        "Kihoto Hollohan (1992): Para 7 unconstitutional; Speaker acts as a tribunal; decision subject to judicial review.",
        "கிகோட்டோ ஹோல்லோஹன் (1992): பத்தி 7 செல்லாது; சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார்; அவரது முடிவு நீதிப் புனராய்வுக்கு உட்பட்டது."
    ))

    # GT084
    qs.append(make_sch_q(
        "SCH_GT_084", "Medium", "Conceptual", "Tenth Schedule",
        "Under Paragraph 5 of the Tenth Schedule, which constitutional dignitaries are exempted from disqualification if they sever ties with their political party upon being elected?",
        "பத்தாவது அட்டவணையின் பத்தி 5-ன் கீழ், எந்த அரசியலமைப்புப் பொறுப்பாளர்கள் தேர்ந்தெடுக்கப்பட்டவுடன் தங்கள் அரசியல் கட்சியுடனான தொடர்பைத் துண்டித்துக் கொண்டால் தகுதியிழப்பிலிருந்து விலக்கு அளிக்கப்படுகிறார்கள்?",
        "Speaker and Deputy Speaker of the Lok Sabha, and Chairman and Deputy Chairman of the Rajya Sabha / State Presiding Officers", "மக்களவை சபாநாயகர் மற்றும் துணை சபாநாயகர், மற்றும் மாநிலங்களவைத் தலைவர் மற்றும் துணைத் தலைவர் / மாநில அவைத் தலைவர்கள்",
        "The Prime Minister and the Leader of the Opposition", "பிரதம மந்திரி மற்றும் எதிர்க்கட்சித் தலைவர்",
        "The Chief Ministers of all Union Territories and special category States", "அனைத்து யூனியன் பிரதேசங்கள் மற்றும் சிறப்பு அந்தஸ்து மாநிலங்களின் முதலமைச்சர்கள்",
        "The Attorney-General of India and Advocate Generals of States", "இந்திய தலைமை வழக்கறிஞர் மற்றும் மாநிலங்களின் அட்வகேட் ஜெனரல்கள்",
        "A",
        "Paragraph 5 of the Tenth Schedule provides an exemption for presiding officers: a person elected as Speaker or Deputy Speaker of Lok Sabha, Chairman or Deputy Chairman of Rajya Sabha, or presiding officer of a State Legislature does not face disqualification if they resign from their political party to maintain impartiality, or rejoin after leaving office.",
        "பத்தாவது அட்டவணையின் பத்தி 5 அவைத் தலைவர்களுக்கு விலக்கு அளிக்கிறது: மக்களவை சபாநாயகர் அல்லது துணை சபாநாயகர், மாநிலங்களவைத் தலைவர் அல்லது துணைத் தலைவர், அல்லது மாநில அவைத் தலைவர்களாகத் தேர்ந்தெடுக்கப்பட்ட ஒருவர் நடுநிலைமையைப் பேண கட்சியில் இருந்து விலகினாலோ அல்லது பதவி முடிந்த பின் மீண்டும் இணைந்தாலோ தகுதியிழப்பை எதிர்கொள்ள மாட்டார்.",
        "Correct. Presiding officers are exempted under Paragraph 5 to protect institutional neutrality.", "சரியானது. நடுநிலைமையைப் பாதுகாக்க பத்தி 5-ன் கீழ் அவைத் தலைவர்களுக்கு விலக்கு அளிக்கப்பட்டுள்ளது.",
        "Incorrect. Prime Minister and Leader of Opposition have no exemption.", "தவறானது. பிரதமர் மற்றும் எதிர்க்கட்சித் தலைவருக்கு விலக்கு இல்லை.",
        "Incorrect. Chief Ministers enjoy no anti-defection exemption.", "தவறானது. முதலமைச்சர்களுக்கு கட்சித்தாவல் விலக்கு கிடையாது.",
        "Incorrect. Law officers are not elected members of the House.", "தவறானது. சட்ட அதிகாரிகள் அவையின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் அல்ல.",
        "Paragraph 5 Exemption: Preserving the neutrality of the Speaker's office from partisan strings.",
        "பத்தி 5 விலக்கு: சபாநாயகர் பதவியின் நடுநிலைமையைக் கட்சிச் சார்பிலிருந்து பாதுகாப்பது."
    ))

    # GT085
    qs.append(make_sch_q(
        "SCH_GT_085", "Easy", "Conceptual", "Eleventh Schedule",
        "Which Article of the Indian Constitution links the 29 functional matters of the Eleventh Schedule to the powers, authority, and responsibilities of Panchayats?",
        "இந்திய அரசியலமைப்பின் எந்த சரத்து பதினோராவது அட்டவணையின் 29 செயல்பாட்டு விஷயங்களை பஞ்சாயத்துகளின் அதிகாரங்கள் மற்றும் பொறுப்புகளுடன் இணைக்கிறது?",
        "Article 243G", "சரத்து 243G",
        "Article 243W", "சரத்து 243W",
        "Article 243I", "சரத்து 243I",
        "Article 243K", "சரத்து 243K",
        "A",
        "Article 243G provides that the Legislature of a State may by law endow the Panchayats with powers and authority, including with respect to matters listed in the Eleventh Schedule.",
        "சரத்து 243G குறிப்பிடுகிறது: பதினோராவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள விஷயங்கள் உட்பட பஞ்சாயத்துகளுக்கு தேவையான அதிகாரங்களை மாநில சட்டமன்றம் சட்டம் மூலம் வழங்கலாம்.",
        "Correct. Article 243G governs the Eleventh Schedule.", "சரியானது. சரத்து 243G பதினோராவது அட்டவணையை நிர்வகிக்கிறது.",
        "Incorrect. Article 243W governs the Twelfth Schedule for Municipalities.", "தவறானது. சரத்து 243W நகராட்சிகளுக்கான பன்னிரண்டாவது அட்டவணையை நிர்வகிக்கிறது.",
        "Incorrect. Article 243I governs the State Finance Commission.", "தவறானது. சரத்து 243I மாநில நிதி ஆணையத்தை நிர்வகிக்கிறது.",
        "Incorrect. Article 243K governs the State Election Commission.", "தவறானது. சரத்து 243K மாநில தேர்தல் ஆணையத்தை நிர்வகிக்கிறது.",
        "Eleventh Schedule: Article 243G (Panchayats, 29 subjects). Twelfth Schedule: Article 243W (Municipalities, 18 subjects).",
        "பதினோராவது அட்டவணை: சரத்து 243G (பஞ்சாயத்துகள், 29 விஷயங்கள்). பன்னிரண்டாவது அட்டவணை: சரத்து 243W (நகராட்சிகள், 18 விஷயங்கள்)."
    ))

    # GT086
    qs.append(make_sch_q(
        "SCH_GT_086", "Easy", "Conceptual", "Eleventh Schedule",
        "How many functional items or subjects are enumerated in the Eleventh Schedule of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் பதினோராவது அட்டவணையில் எத்தனை செயல்பாட்டு உருப்படிகள் அல்லது பாடங்கள் பட்டியலிடப்பட்டுள்ளன?",
        "29 functional subjects", "29 செயல்பாட்டு பாடங்கள்",
        "18 functional subjects", "18 செயல்பாட்டு பாடங்கள்",
        "22 functional subjects", "22 செயல்பாட்டு பாடங்கள்",
        "33 functional subjects", "33 செயல்பாட்டு பாடங்கள்",
        "A",
        "The Eleventh Schedule contains exactly 29 functional items placed within the purview of Panchayati Raj Institutions under the 73rd Constitutional Amendment Act, 1992.",
        "1992-ன் 73வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் கீழ் பஞ்சாயத்து ராஜ் அமைப்புகளின் அதிகார வரம்பிற்குள் வைக்கப்பட்ட சரியாக 29 செயல்பாட்டு விஷயங்களை பதினோராவது அட்டவணை கொண்டுள்ளது.",
        "Correct. 29 subjects in the Eleventh Schedule.", "சரியானது. பதினோராவது அட்டவணையில் 29 பாடங்கள்.",
        "Incorrect. 18 subjects is the count in the Twelfth Schedule (Municipalities).", "தவறானது. 18 பாடங்கள் என்பது பன்னிரண்டாவது அட்டவணையில் உள்ள எண்ணிக்கை (நகராட்சிகள்).",
        "Incorrect. 22 is the number of scheduled languages in Eighth Schedule.", "தவறானது. 22 என்பது எட்டாவது அட்டவணையில் உள்ள மொழிகளின் எண்ணிக்கை.",
        "Incorrect. 33 is incorrect.", "தவறானது. 33 என்பது தவறானது.",
        "Schedule Subject Counts: Eleventh Schedule (Panchayats) = 29; Twelfth Schedule (Municipalities) = 18.",
        "அட்டவணை பாடங்களின் எண்ணிக்கை: பதினோராவது அட்டவணை (பஞ்சாயத்துகள்) = 29; பன்னிரண்டாவது அட்டவணை (நகராட்சிகள்) = 18."
    ))

    # GT087
    qs.append(make_sch_q(
        "SCH_GT_087", "Medium", "Conceptual", "Eleventh Schedule",
        "Which of the following is Item 1 listed in the Eleventh Schedule of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் பதினோராவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள உருப்படி 1 (முதல் பாடம்) எது?",
        "Agriculture, including agricultural extension", "விவசாய விரிவாக்கம் உட்பட விவசாயம்",
        "Land improvement and soil conservation", "நில மேம்பாடு மற்றும் மண் பாதுகாப்பு",
        "Minor irrigation, water management, and watershed development", "சிறு பாசனம், நீர் மேலாண்மை மற்றும் நீர்ப்பிடிப்புப் பகுதி மேம்பாடு",
        "Animal husbandry, dairying, and poultry", "கால்நடை பராமரிப்பு, பால் பண்ணை மற்றும் கோழி வளர்ப்பு",
        "A",
        "Item 1 of the Eleventh Schedule is: 'Agriculture, including agricultural extension.' Item 2 is Land improvement; Item 3 is Minor irrigation; Item 4 is Animal husbandry.",
        "பதினோராவது அட்டவணையின் உருப்படி 1: 'விவசாய விரிவாக்கம் உட்பட விவசாயம்.' உருப்படி 2 நில மேம்பாடு; உருப்படி 3 சிறு பாசனம்; உருப்படி 4 கால்நடை பராமரிப்பு.",
        "Correct. Agriculture, including agricultural extension is Item 1.", "சரியானது. விவசாய விரிவாக்கம் உட்பட விவசாயம் என்பது உருப்படி 1 ஆகும்.",
        "Incorrect. Land improvement is Item 2.", "தவறானது. நில மேம்பாடு என்பது உருப்படி 2.",
        "Incorrect. Minor irrigation is Item 3.", "தவறானது. சிறு பாசனம் என்பது உருப்படி 3.",
        "Incorrect. Animal husbandry is Item 4.", "தவறானது. கால்நடை பராமரிப்பு என்பது உருப்படி 4.",
        "Top of Eleventh Schedule: 1. Agriculture; 2. Land improvement; 3. Minor irrigation; 4. Animal husbandry; 5. Fisheries.",
        "பதினோராவது அட்டவணையின் தொடக்கம்: 1. விவசாயம்; 2. நில மேம்பாடு; 3. சிறு பாசனம்; 4. கால்நடை பராமரிப்பு; 5. மீன்வளம்."
    ))

    # GT088
    qs.append(make_sch_q(
        "SCH_GT_088", "Medium", "Conceptual", "Eleventh Schedule",
        "Which committee recommended constitutional recognition for Panchayati Raj Institutions in 1986, directly leading to the drafting of the 73rd Amendment and Eleventh Schedule?",
        "1986-ல் பஞ்சாயத்து ராஜ் அமைப்புகளுக்கு அரசியலமைப்பு அங்கீகாரம் வழங்க பரிந்துரைத்து, 73வது திருத்தம் மற்றும் பதினோராவது அட்டவணை வரைவுக்கு நேரடியாக வழிவகுத்த குழு எது?",
        "L.M. Singhvi Committee (1986)", "எல்.எம். சிங்வி குழு (1986)",
        "Balwant Rai Mehta Committee (1957)", "பல்வந்த் ராய் மேத்தா குழு (1957)",
        "Ashok Mehta Committee (1977)", "அசோக் மேத்தா குழு (1977)",
        "G.V.K. Rao Committee (1985)", "ஜி.வி.கே. ராவ் குழு (1985)",
        "A",
        "The L.M. Singhvi Committee, appointed in 1986 by Rajiv Gandhi, recommended that Panchayati Raj Institutions should be constitutionally recognized, protected, and preserved by adding a new chapter in the Constitution, which led to the 73rd Amendment and Eleventh Schedule.",
        "1986-ல் ராஜீவ் காந்தியால் நியமிக்கப்பட்ட எல்.எம். சிங்வி குழு, அரசியலமைப்பில் ஒரு புதிய அத்தியாயத்தைச் சேர்ப்பதன் மூலம் பஞ்சாயத்து ராஜ் அமைப்புகள் அரசியலமைப்பு ரீதியாக அங்கீகரிக்கப்பட்டு பாதுகாக்கப்பட வேண்டும் என்று பரிந்துரைத்தது; இது 73வது திருத்தம் மற்றும் 11வது அட்டவணைக்கு வழிவகுத்தது.",
        "Correct. L.M. Singhvi Committee (1986) recommended constitutional status for Panchayats.", "சரியானது. எல்.எம். சிங்வி குழு (1986) பஞ்சாயத்துகளுக்கு அரசியலமைப்பு அந்தஸ்தைப் பரிந்துரைத்தது.",
        "Incorrect. Balwant Rai Mehta (1957) recommended 3-tier Panchayati Raj.", "தவறானது. பல்வந்த் ராய் மேத்தா (1957) 3 அடுக்கு பஞ்சாயத்து முறையைப் பரிந்துரைத்தது.",
        "Incorrect. Ashok Mehta (1977) recommended 2-tier system.", "தவறானது. அசோக் மேத்தா (1977) 2 அடுக்கு முறையைப் பரிந்துரைத்தது.",
        "Incorrect. G.V.K. Rao (1985) focused on administrative arrangements for rural development.", "தவறானது. ஜி.வி.கே. ராவ் (1985) ஊரக வளர்ச்சிக்கான நிர்வாக ஏற்பாடுகளில் கவனம் செலுத்தியது.",
        "Panchayati Raj Chronology: Balwant Rai Mehta (1957) -> Ashok Mehta (1977) -> G.V.K. Rao (1985) -> L.M. Singhvi (1986) -> 73rd CAA (1992).",
        "பஞ்சாயத்து ராஜ் காலவரிசை: பல்வந்த் ராய் மேத்தா (1957) -> அசோக் மேத்தா (1977) -> ஜி.வி.கே. ராவ் (1985) -> எல்.எம். சிங்வி (1986) -> 73வது திருத்தம் (1992)."
    ))

    # GT089
    qs.append(make_sch_q(
        "SCH_GT_089", "Hard", "Conceptual", "Eleventh Schedule",
        "Under the Eleventh Schedule, which functional entry pertains to 'Non-conventional energy sources' (such as solar and biogas installations in rural areas)?",
        "பதினோராவது அட்டவணையின் கீழ், 'பாரம்பரியமற்ற எரிசக்தி ஆதாரங்கள்' (கிராமப்புறங்களில் சூரிய ஒளி மற்றும் உயிரி எரிவாயு அமைப்புகள் போன்றவை) தொடர்பான செயல்பாட்டுப் பதிவு எது?",
        "Item 15", "உருப்படி 15",
        "Item 8", "உருப்படி 8",
        "Item 22", "உருப்படி 22",
        "Item 28", "உருப்படி 28",
        "A",
        "Item 15 of the Eleventh Schedule specifies: 'Non-conventional energy sources.' Under this, Panchayats promote solar street lighting, biogas plants, and clean rural energy.",
        "பதினோராவது அட்டவணையின் உருப்படி 15 குறிப்பிடுகிறது: 'பாரம்பரியமற்ற எரிசக்தி ஆதாரங்கள்.' இதன் கீழ், பஞ்சாயத்துகள் சூரிய ஒளி தெருவிளக்குகள், பயோகேஸ் ஆலைகள் மற்றும் தூய கிராமப்புற ஆற்றலை ஊக்குவிக்கின்றன.",
        "Correct. Item 15 is Non-conventional energy sources.", "சரியானது. உருப்படி 15 என்பது பாரம்பரியமற்ற எரிசக்தி ஆதாரங்கள்.",
        "Incorrect. Item 8 is Small scale industries, including food processing.", "தவறானது. உருப்படி 8 சிறுதொழில்கள் பற்றியது.",
        "Incorrect. Item 22 is Markets and fairs.", "தவறானது. உருப்படி 22 சந்தைகள் மற்றும் திருவிழாக்கள்.",
        "Incorrect. Item 28 is Public distribution system.", "தவறானது. உருப்படி 28 பொது விநியோக முறை.",
        "Eleventh Schedule Entry 15: Promotes rural renewable energy and decentralised solar initiatives.",
        "பதினோராவது அட்டவணை பதிவு 15: கிராமப்புற புதுப்பிக்கத்தக்க எரிசக்தி மற்றும் பரவலாக்கப்பட்ட சூரிய திட்டங்களை ஊக்குவிக்கிறது."
    ))

    # GT090
    qs.append(make_sch_q(
        "SCH_GT_090", "Hard", "Conceptual", "Eleventh Schedule",
        "In the Eleventh Schedule of the Constitution, under which specific Item is the 'Poverty alleviation programme' included?",
        "அரசியலமைப்பின் பதினோராவது அட்டவணையில், 'வறுமை ஒழிப்புத் திட்டம்' எந்த குறிப்பிட்ட உருப்படியின் கீழ் சேர்க்கப்பட்டுள்ளது?",
        "Item 16", "உருப்படி 16",
        "Item 10", "உருப்படி 10",
        "Item 20", "உருப்படி 20",
        "Item 25", "உருப்படி 25",
        "A",
        "Item 16 of the Eleventh Schedule specifies: 'Poverty alleviation programme.' This serves as the constitutional anchor for flagship rural livelihood programs like MGNREGA and NRLM implemented through Gram Panchayats.",
        "பதினோராவது அட்டவணையின் உருப்படி 16 குறிப்பிடுகிறது: 'வறுமை ஒழிப்புத் திட்டம்.' இது கிராம பஞ்சாயத்துகள் மூலம் செயல்படுத்தப்படும் மகாத்மா காந்தி ஊரக வேலைவாய்ப்புத் திட்டம் (MGNREGA) மற்றும் NRLM போன்ற முதன்மை ஊரக வாழ்வாதாரத் திட்டங்களுக்கான அரசியலமைப்பு அடிப்படையாகச் செயல்படுகிறது.",
        "Correct. Item 16 is Poverty alleviation programme.", "சரியானது. உருப்படி 16 என்பது வறுமை ஒழிப்புத் திட்டம்.",
        "Incorrect. Item 10 is Rural housing.", "தவறானது. உருப்படி 10 கிராமப்புற வீட்டுவசதி.",
        "Incorrect. Item 20 is Technical training and vocational education.", "தவறானது. உருப்படி 20 தொழில்நுட்பப் பயிற்சி மற்றும் தொழிற்கல்வி.",
        "Incorrect. Item 25 is Women and child development.", "தவறானது. உருப்படி 25 பெண்கள் மற்றும் குழந்தைகள் மேம்பாடு.",
        "Item 16 Eleventh Schedule: Constitutional mandate for Gram Panchayats to identify beneficiaries and implement MGNREGA.",
        "உருப்படி 16 பதினோராவது அட்டவணை: பயனாளிகளை அடையாளம் காணவும் MGNREGA-வை செயல்படுத்தவும் கிராம பஞ்சாயத்துகளுக்கான அரசியலமைப்பு அதிகாரம்."
    ))

    # GT091
    qs.append(make_sch_q(
        "SCH_GT_091", "Medium", "Conceptual", "Eleventh Schedule",
        "Are the 29 functional subjects listed in the Eleventh Schedule automatically devolved to Panchayati Raj Institutions, or does devolution depend on State legislation?",
        "பதினோராவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள 29 செயல்பாட்டுப் பாடங்கள் பஞ்சாயத்து ராஜ் அமைப்புகளுக்குத் தானாகவே மாற்றப்படுகின்றனவா, அல்லது அந்த மாற்றம் மாநிலச் சட்டத்தைப் பொறுத்ததா?",
        "Devolution is discretionary and depends entirely on the Legislature of each State passing enabling legislation under Article 243G", "அதிகாரப் பகிர்வு விருப்பத்திற்குரியது மற்றும் சரத்து 243G-ன் கீழ் ஒவ்வொரு மாநில சட்டமன்றமும் சட்டம் இயற்றுவதைப் பொறுத்தது",
        "Devolution is automatic and self-executing across all States without requiring any State laws", "எந்தவொரு மாநில சட்டமும் தேவையின்றி அனைத்து மாநிலங்களிலும் அதிகாரப் பகிர்வு தானாகவே நடைமுறைக்கு வருகிறது",
        "Devolution is decided solely by the Union Ministry of Panchayati Raj through executive notifications", "அதிகாரப் பகிர்வு மத்திய பஞ்சாயத்து ராஜ் அமைச்சகத்தால் நிர்வாக அறிவிப்புகள் மூலம் மட்டுமே தீர்மானிக்கப்படுகிறது",
        "Devolution requires annual presidential approval through a national ordinance", "அதிகாரப் பகிர்வுக்கு தேசிய அவசரச் சட்டம் மூலம் ஆண்டுதோறும் குடியரசுத் தலைவரின் ஒப்புதல் தேவைப்படுகிறது",
        "A",
        "Article 243G uses the operative word 'may': '...the Legislature of a State may, by law, endow the Panchayats with such powers and authority...'. Hence, the transfer of the 29 subjects is non-mandatory and varies widely across States (e.g., Kerala has devolved all 29 subjects, while others have devolved fewer).",
        "சரத்து 243G 'வழங்கலாம்' (may) என்ற வார்த்தையைப் பயன்படுத்துகிறது: 'ஒரு மாநிலத்தின் சட்டமன்றம், சட்டத்தின் மூலம், பஞ்சாயத்துகளுக்கு அத்தகைய அதிகாரங்களையும் அதிகார வரம்பையும் வழங்கலாம்...'. எனவே 29 பாடங்களை மாற்றுவது கட்டாயமற்றது மற்றும் மாநிலத்திற்கு மாநிலம் வேறுபடுகிறது (எ.கா. கேரளா 29 பாடங்களையும் மாற்றியுள்ளது, மற்றவை குறைவாக மாற்றியுள்ளன).",
        "Correct. Devolution is discretionary under Article 243G ('may by law endow').", "சரியானது. சரத்து 243G-ன் கீழ் அதிகாரப் பகிர்வு மாநிலத்தின் விருப்பத்திற்குரியது.",
        "Incorrect. Eleventh Schedule provisions are not self-executing.", "தவறானது. 11வது அட்டவணை தானாக நடைமுறைக்கு வருவதில்லை.",
        "Incorrect. Centre cannot directly devolve subjects under state jurisdiction.", "தவறானது. மாநில அதிகாரத்தில் மத்திய அரசு நேரடியாக தலையிட முடியாது.",
        "Incorrect. No presidential annual approval is needed.", "தவறானது. குடியரசுத் தலைவரின் வருடாந்திர ஒப்புதல் தேவையில்லை.",
        "Voluntary vs Compulsory Provisions: The 29 subjects under Eleventh Schedule (Art 243G) are voluntary provisions left to state legislative discretion.",
        "விருப்ப vs கட்டாய விதிகள்: பதினோராவது அட்டவணையின் கீழ் உள்ள 29 பாடங்கள் (சரத்து 243G) மாநில சட்டமன்றத்தின் விருப்பத்திற்கு விடப்பட்ட விருப்ப விதிகளாகும்."
    ))

    # GT092
    qs.append(make_sch_q(
        "SCH_GT_092", "Medium", "Conceptual", "Eleventh Schedule",
        "Under the Tamil Nadu Panchayats Act, 1994, which tier of Panchayati Raj has direct responsibility for providing street lights, village roads, and drinking water from the Eleventh Schedule?",
        "தமிழ்நாடு பஞ்சாயத்துகள் சட்டம் 1994-ன் கீழ், பதினோராவது அட்டவணையில் உள்ள தெருவிளக்குகள், கிராமச் சாலைகள் மற்றும் குடிநீர் வழங்குவதற்கான நேரடிப் பொறுப்பு பஞ்சாயத்து ராஜின் எந்த அடுக்குக்கு உள்ளது?",
        "Village Panchayat (Gram Panchayat)", "கிராம பஞ்சாயத்து (Gram Panchayat)",
        "Panchayat Union (Block level)", "பஞ்சாயத்து யூனியன் / ஊராட்சி ஒன்றியம்",
        "District Panchayat (Zilla level)", "மாவட்ட பஞ்சாயத்து / மாவட்ட ஊராட்சி",
        "District Collectorate Planning Cell", "மாவட்ட ஆட்சியர் திட்டப் பிரிவு",
        "A",
        "Under the Tamil Nadu Panchayats Act, 1994, mandatory civic duties such as village roads, street lighting, sanitation, and drinking water supply (core Eleventh Schedule functions) are the direct statutory duty of Village Panchayats.",
        "தமிழ்நாடு பஞ்சாயத்துகள் சட்டம் 1994-ன் கீழ், கிராமச் சாலைகள், தெருவிளக்குகள், துப்புரவு மற்றும் குடிநீர் வழங்கல் (முக்கிய 11வது அட்டவணை பணிகள்) போன்ற கட்டாய குடிமைப் பணிகள் கிராம பஞ்சாயத்துகளின் நேரடி சட்டப்பூர்வ கடமையாகும்.",
        "Correct. Village Panchayats handle ground-level civic delivery in Tamil Nadu.", "சரியானது. தமிழ்நாட்டில் கிராம அளவிலான அடிப்படைப் பணிகளை கிராம பஞ்சாயத்துகள் கையாள்கின்றன.",
        "Incorrect. Panchayat Union handles inter-village coordination and secondary education.", "தவறானது. ஊராட்சி ஒன்றியம் கிராமங்களுக்கு இடையேயான ஒருங்கிணைப்பைக் கையாள்கிறது.",
        "Incorrect. District Panchayat plays an advisory and overarching planning role.", "தவறானது. மாவட்ட ஊராட்சி ஆலோசனைக் குழுவாக செயல்படுகிறது.",
        "Incorrect. Collectorate cell is a bureaucratic unit, not an elected PR tier.", "தவறானது. ஆட்சியர் திட்டப் பிரிவு என்பது அரசு நிர்வாகப் பிரிவு, உள்ளாட்சி அமைப்பு அல்ல.",
        "TN Panchayats 3-Tier System: Village Panchayat (direct elections for President & ward members), Panchayat Union, and District Panchayat.",
        "தமிழக பஞ்சாயத்து 3 அடுக்கு முறை: கிராம பஞ்சாயத்து (தலைவர் & வார்டு உறுப்பினர்களுக்கு நேரடித் தேர்தல்), ஊராட்சி ஒன்றியம், மற்றும் மாவட்ட ஊராட்சி."
    ))

    # GT093
    qs.append(make_sch_q(
        "SCH_GT_093", "Easy", "Conceptual", "Twelfth Schedule",
        "Which Article of the Indian Constitution links the 18 functional matters of the Twelfth Schedule to the powers and responsibilities of Municipalities?",
        "இந்திய அரசியலமைப்பின் எந்த சரத்து பன்னிரண்டாவது அட்டவணையின் 18 செயல்பாட்டு விஷயங்களை நகராட்சிகளின் அதிகாரங்கள் மற்றும் பொறுப்புகளுடன் இணைக்கிறது?",
        "Article 243W", "சரத்து 243W",
        "Article 243G", "சரத்து 243G",
        "Article 243Q", "சரத்து 243Q",
        "Article 243ZA", "சரத்து 243ZA",
        "A",
        "Article 243W provides that the Legislature of a State may by law endow Municipalities with powers and authority, including with respect to the matters listed in the Twelfth Schedule.",
        "சரத்து 243W குறிப்பிடுகிறது: பன்னிரண்டாவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள விஷயங்கள் உட்பட நகராட்சிகளுக்கு தேவையான அதிகாரங்களை மாநில சட்டமன்றம் சட்டம் மூலம் வழங்கலாம்.",
        "Correct. Article 243W governs the Twelfth Schedule for Municipalities.", "சரியானது. சரத்து 243W நகராட்சிகளுக்கான பன்னிரண்டாவது அட்டவணையை நிர்வகிக்கிறது.",
        "Incorrect. Article 243G governs Eleventh Schedule for Panchayats.", "தவறானது. சரத்து 243G பஞ்சாயத்துகளுக்கான பதினோராவது அட்டவணையை நிர்வகிக்கிறது.",
        "Incorrect. Article 243Q deals with the constitution of Municipalities.", "தவறானது. சரத்து 243Q நகராட்சிகளை அமைப்பதைக் கையாள்கிறது.",
        "Incorrect. Article 243ZA deals with elections to Municipalities.", "தவறானது. சரத்து 243ZA நகராட்சித் தேர்தல்களைக் கையாள்கிறது.",
        "Schedules and Local Bodies: 11th Schedule (Art 243G, 29 items) vs 12th Schedule (Art 243W, 18 items).",
        "அட்டவணைகளும் உள்ளாட்சி அமைப்புகளும்: 11வது அட்டவணை (சரத்து 243G, 29 உருப்படிகள்) vs 12வது அட்டவணை (சரத்து 243W, 18 உருப்படிகள்)."
    ))

    # GT094
    qs.append(make_sch_q(
        "SCH_GT_094", "Easy", "Conceptual", "Twelfth Schedule",
        "How many functional items or subjects are enumerated in the Twelfth Schedule of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் பன்னிரண்டாவது அட்டவணையில் எத்தனை செயல்பாட்டு உருப்படிகள் அல்லது பாடங்கள் பட்டியலிடப்பட்டுள்ளன?",
        "18 functional subjects", "18 செயல்பாட்டு பாடங்கள்",
        "29 functional subjects", "29 செயல்பாட்டு பாடங்கள்",
        "12 functional subjects", "12 செயல்பாட்டு பாடங்கள்",
        "25 functional subjects", "25 செயல்பாட்டு பாடங்கள்",
        "A",
        "The Twelfth Schedule contains exactly 18 functional items placed within the purview of Urban Local Bodies (Municipalities) under the 74th Constitutional Amendment Act, 1992.",
        "1992-ன் 74வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் கீழ் நகர்ப்புற உள்ளாட்சி அமைப்புகளின் (நகராட்சிகள்) அதிகார வரம்பிற்குள் வைக்கப்பட்ட சரியாக 18 செயல்பாட்டு விஷயங்களை பன்னிரண்டாவது அட்டவணை கொண்டுள்ளது.",
        "Correct. 18 subjects in the Twelfth Schedule.", "சரியானது. பன்னிரண்டாவது அட்டவணையில் 18 பாடங்கள்.",
        "Incorrect. 29 is the number in the Eleventh Schedule.", "தவறானது. 29 என்பது பதினோராவது அட்டவணையில் உள்ள எண்ணிக்கை.",
        "Incorrect. 12 is the total number of Schedules in the Constitution.", "தவறானது. 12 என்பது அரசியலமைப்பில் உள்ள மொத்த அட்டவணைகளின் எண்ணிக்கை.",
        "Incorrect. 25 is incorrect.", "தவறானது. 25 என்பது தவறானது.",
        "Twelfth Schedule: 18 items added by 74th CAA 1992.",
        "பன்னிரண்டாவது அட்டவணை: 1992-ன் 74வது திருத்தத்தால் சேர்க்கப்பட்ட 18 உருப்படிகள்."
    ))

    # GT095
    qs.append(make_sch_q(
        "SCH_GT_095", "Medium", "Conceptual", "Twelfth Schedule",
        "Which of the following is Item 1 listed in the Twelfth Schedule of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் பன்னிரண்டாவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள உருப்படி 1 (முதல் பாடம்) எது?",
        "Urban planning including town planning", "நகரத் திட்டமிடல் உட்பட நகர்ப்புற திட்டமிடல்",
        "Regulation of land-use and construction of buildings", "நிலப் பயன்பாடு மற்றும் கட்டிடங்களின் கட்டுமானத்தை ஒழுங்குபடுத்துதல்",
        "Planning for economic and social development", "பொருளாதார மற்றும் சமூக வளர்ச்சிக்கான திட்டமிடல்",
        "Roads and bridges", "சாலைகள் மற்றும் பாலங்கள்",
        "A",
        "Item 1 of the Twelfth Schedule is: 'Urban planning including town planning.' Item 2 is Regulation of land-use; Item 3 is Planning for economic and social development; Item 4 is Roads and bridges.",
        "பன்னிரண்டாவது அட்டவணையின் உருப்படி 1: 'நகரத் திட்டமிடல் உட்பட நகர்ப்புற திட்டமிடல்.' உருப்படி 2 நிலப் பயன்பாட்டு ஒழுங்குமுறை; உருப்படி 3 பொருளாதார மற்றும் சமூக வளர்ச்சிக்கான திட்டமிடல்; உருப்படி 4 சாலைகள் மற்றும் பாலங்கள்.",
        "Correct. Urban planning including town planning is Item 1.", "சரியானது. நகரத் திட்டமிடல் உட்பட நகர்ப்புற திட்டமிடல் என்பது உருப்படி 1 ஆகும்.",
        "Incorrect. Regulation of land-use is Item 2.", "தவறானது. நிலப் பயன்பாட்டு ஒழுங்குமுறை என்பது உருப்படி 2.",
        "Incorrect. Economic and social planning is Item 3.", "தவறானது. பொருளாதார மற்றும் சமூக திட்டமிடல் என்பது உருப்படி 3.",
        "Incorrect. Roads and bridges is Item 4.", "தவறானது. சாலைகள் மற்றும் பாலங்கள் என்பது உருப்படி 4.",
        "Top of Twelfth Schedule: 1. Urban planning; 2. Land use regulation; 3. Economic/social planning; 4. Roads & bridges; 5. Water supply.",
        "பன்னிரண்டாவது அட்டவணையின் தொடக்கம்: 1. நகர்ப்புற திட்டமிடல்; 2. நிலப் பயன்பாடு; 3. பொருளாதார/சமூக திட்டமிடல்; 4. சாலைகள் & பாலங்கள்; 5. குடிநீர் வழங்கல்."
    ))

    # GT096
    qs.append(make_sch_q(
        "SCH_GT_096", "Hard", "Conceptual", "Twelfth Schedule",
        "Which specific Item in the Twelfth Schedule of the Indian Constitution assigns 'Fire services' to Municipalities?",
        "இந்திய அரசியலமைப்பின் பன்னிரண்டாவது அட்டவணையில் உள்ள எந்த குறிப்பிட்ட உருப்படி 'தீயணைப்பு சேவைகளை' நகராட்சிகளுக்கு ஒதுக்குகிறது?",
        "Item 7", "உருப்படி 7",
        "Item 3", "உருப்படி 3",
        "Item 11", "உருப்படி 11",
        "Item 15", "உருப்படி 15",
        "A",
        "Item 7 of the Twelfth Schedule specifically enumerates: 'Fire services.' This empowers urban civic bodies to maintain municipal fire brigades and fire safety inspection units.",
        "பன்னிரண்டாவது அட்டவணையின் உருப்படி 7 குறிப்பிடுகிறது: 'தீயணைப்பு சேவைகள்.' இது நகர்ப்புற குடிமை அமைப்புகளுக்கு தீயணைப்புப் படைகள் மற்றும் தீ பாதுகாப்பு ஆய்வுப் பிரிவுகளைப் பராமரிக்க அதிகாரம் அளிக்கிறது.",
        "Correct. Item 7 of the Twelfth Schedule is Fire services.", "சரியானது. பன்னிரண்டாவது அட்டவணையின் உருப்படி 7 தீயணைப்பு சேவைகள் ஆகும்.",
        "Incorrect. Item 3 is Planning for economic and social development.", "தவறானது. உருப்படி 3 பொருளாதார மற்றும் சமூக வளர்ச்சிக்கான திட்டமிடல்.",
        "Incorrect. Item 11 is Urban poverty alleviation.", "தவறானது. உருப்படி 11 நகர்ப்புற வறுமை ஒழிப்பு.",
        "Incorrect. Item 15 is Cattle pounds and prevention of cruelty to animals.", "தவறானது. உருப்படி 15 மாட்டுத் தொழுவங்கள் மற்றும் விலங்குகள் வதை தடுப்பு.",
        "Twelfth Schedule Item 7: Fire services (Essential safety infrastructure for high-density urban agglomerations).",
        "பன்னிரண்டாவது அட்டவணை உருப்படி 7: தீயணைப்பு சேவைகள் (அடர்த்தியான நகர்ப்புறங்களுக்கான அத்தியாவசிய பாதுகாப்பு கட்டமைப்பு)."
    ))

    # GT097
    qs.append(make_sch_q(
        "SCH_GT_097", "Hard", "Conceptual", "Twelfth Schedule",
        "Which Item of the Twelfth Schedule specifies 'Burials and burial grounds; cremations, cremation grounds and electric crematoriums'?",
        "பன்னிரண்டாவது அட்டவணையின் எந்த உருப்படி 'இடுகாடுகள் மற்றும் அடக்கம் செய்யும் இடங்கள்; சுடுகாடுகள், தகன மைதானங்கள் மற்றும் மின்சார மயானங்கள்' ஆகியவற்றைக் குறிப்பிடுகிறது?",
        "Item 14", "உருப்படி 14",
        "Item 6", "உருப்படி 6",
        "Item 10", "உருப்படி 10",
        "Item 18", "உருப்படி 18",
        "A",
        "Item 14 of the Twelfth Schedule explicitly covers: 'Burials and burial grounds; cremations, cremation grounds and electric crematoriums.' Municipal corporations maintain these facilities under this constitutional item.",
        "பன்னிரண்டாவது அட்டவணையின் உருப்படி 14 குறிப்பிடுகிறது: 'இடுகாடுகள் மற்றும் அடக்கம் செய்யும் இடங்கள்; சுடுகாடுகள், தகன மைதானங்கள் மற்றும் மின்சார மயானங்கள்.' இந்த அரசியலமைப்பு உருப்படியின் கீழ் மாநகராட்சிகள் இந்த வசதிகளைப் பராமரிக்கின்றன.",
        "Correct. Item 14 is Burials, cremations, and electric crematoriums.", "சரியானது. உருப்படி 14 என்பது இடுகாடுகள், சுடுகாடுகள் மற்றும் மின்சார மயானங்கள்.",
        "Incorrect. Item 6 is Public health, sanitation conservancy, and solid waste management.", "தவறானது. உருப்படி 6 பொது சுகாதாரம் மற்றும் கழிவு மேலாண்மை.",
        "Incorrect. Item 10 is Slum improvement and upgradation.", "தவறானது. உருப்படி 10 குடிசைப் பகுதி மேம்பாடு.",
        "Incorrect. Item 18 is Regulation of slaughterhouses and tanneries.", "தவறானது. உருப்படி 18 இறைச்சிக் கூடங்கள் மற்றும் தோல் பதனிடும் தொழிற்சாலைகள் ஒழுங்குமுறை.",
        "Twelfth Schedule Item 14: Mandates municipal administration of burial grounds and crematoriums.",
        "பன்னிரண்டாவது அட்டவணை உருப்படி 14: மயானங்கள் மற்றும் தகன மைதானங்களை நகராட்சி நிர்வகிப்பதை கட்டாயமாக்குகிறது."
    ))

    # GT098
    qs.append(make_sch_q(
        "SCH_GT_098", "Medium", "Conceptual", "Twelfth Schedule",
        "Which Item of the Twelfth Schedule pertains to 'Slum improvement and upgradation' in urban areas?",
        "நகர்ப்புறங்களில் 'குடிசைப் பகுதி மேம்பாடு மற்றும் தரமுயர்த்துதல்' தொடர்பான பன்னிரண்டாவது அட்டவணையின் உருப்படி எது?",
        "Item 10", "உருப்படி 10",
        "Item 5", "உருப்படி 5",
        "Item 12", "உருப்படி 12",
        "Item 17", "உருப்படி 17",
        "A",
        "Item 10 of the Twelfth Schedule specifies: 'Slum improvement and upgradation.' This provides the constitutional framework for municipal programs like the Pradhan Mantri Awas Yojana (Urban) and state slum clearance boards.",
        "பன்னிரண்டாவது அட்டவணையின் உருப்படி 10 குறிப்பிடுகிறது: 'குடிசைப் பகுதி மேம்பாடு மற்றும் தரமுயர்த்துதல்.' இது பிரதான் மந்திரி அவாஸ் யோஜனா (நகர்ப்புறம்) மற்றும் தமிழ்நாடு குடிசை மாற்று வாரியம் போன்ற திட்டங்களுக்கான அரசியலமைப்பு கட்டமைப்பை வழங்குகிறது.",
        "Correct. Item 10 is Slum improvement and upgradation.", "சரியானது. உருப்படி 10 என்பது குடிசைப் பகுதி மேம்பாடு மற்றும் தரமுயர்த்துதல்.",
        "Incorrect. Item 5 is Water supply for domestic, industrial, and commercial purposes.", "தவறானது. உருப்படி 5 குடிநீர் வழங்கல்.",
        "Incorrect. Item 12 is Provision of urban amenities like parks, gardens, and playgrounds.", "தவறானது. உருப்படி 12 பூங்காக்கள், தோட்டங்கள் போன்ற நகர்ப்புற வசதிகள்.",
        "Incorrect. Item 17 is Public amenities including street lighting, parking lots, and bus stops.", "தவறானது. உருப்படி 17 தெருவிளக்குகள், பேருந்து நிறுத்தங்கள் போன்ற பொது வசதிகள்.",
        "Twelfth Schedule Item 10: Constitutional basis for urban in-situ slum rehabilitation and affordable housing.",
        "பன்னிரண்டாவது அட்டவணை உருப்படி 10: நகர்ப்புற குடிசை மறுவாழ்வு மற்றும் மலிவு விலை வீடுகளுக்கான அரசியலமைப்பு அடிப்படை."
    ))

    # GT099
    qs.append(make_sch_q(
        "SCH_GT_099", "Easy", "Conceptual", "Twelfth Schedule",
        "Which Constitutional Amendment Act introduced Part IXA and the Twelfth Schedule into the Constitution of India in 1992?",
        "1992-ல் இந்திய அரசியலமைப்பில் பகுதி IXA மற்றும் பன்னிரண்டாவது அட்டவணையை அறிமுகப்படுத்திய அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "74th Constitutional Amendment Act, 1992", "74வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "65th Constitutional Amendment Act, 1990", "65வது அரசியலமைப்புத் திருத்தச் சட்டம், 1990",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்புத் திருத்தச் சட்டம், 2002",
        "A",
        "The 74th Constitutional Amendment Act, 1992 inserted Part IXA ('The Municipalities') comprising Articles 243P to 243ZG and the Twelfth Schedule into the Constitution, coming into force on June 1, 1993.",
        "74வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992, அரசியலமைப்பில் சரத்துகள் 243P முதல் 243ZG வரையிலான பகுதி IXA ('நகராட்சிகள்') மற்றும் பன்னிரண்டாவது அட்டவணையைச் சேர்த்தது (1993 ஜூன் 1 முதல் அமலுக்கு வந்தது).",
        "Correct. 74th CAA 1992 added the Twelfth Schedule.", "சரியானது. 74வது திருத்தம் 1992 பன்னிரண்டாவது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 73rd CAA 1992 added Eleventh Schedule (Panchayats).", "தவறானது. 73வது திருத்தம் 1992 பதினோராவது அட்டவணையைச் சேர்த்தது (பஞ்சாயத்துகள்).",
        "Incorrect. 65th CAA 1990 dealt with SC/ST Commission.", "தவறானது. 65வது திருத்தம் SC/ST ஆணையம் பற்றியது.",
        "Incorrect. 86th CAA 2002 inserted Article 21A (Right to Education).", "தவறானது. 86வது திருத்தம் 2002 சரத்து 21A-வைச் சேர்த்தது.",
        "Local Self-Government Amendments: 73rd CAA (Panchayats, Part IX, 11th Schedule) & 74th CAA (Municipalities, Part IXA, 12th Schedule).",
        "உள்ளாட்சித் திருத்தங்கள்: 73வது திருத்தம் (பஞ்சாயத்துகள், பகுதி IX, 11வது அட்டவணை) & 74வது திருத்தம் (நகராட்சிகள், பகுதி IXA, 12வது அட்டவணை)."
    ))

    # GT100
    qs.append(make_sch_q(
        "SCH_GT_100", "Hard", "Conceptual", "Twelfth Schedule",
        "Under Article 243ZD of Part IXA, which constitutional body at the district level is mandated to consolidate the development plans prepared by Panchayats (Eleventh Schedule) and Municipalities (Twelfth Schedule)?",
        "பகுதி IXA-ன் சரத்து 243ZD-ன் கீழ், பஞ்சாயத்துகள் (பதினோராவது அட்டவணை) மற்றும் நகராட்சிகள் (பன்னிரண்டாவது அட்டவணை) தயாரிக்கும் வளர்ச்சித் திட்டங்களை ஒருங்கிணைக்க கட்டாயப்படுத்தப்பட்டுள்ள மாவட்ட அளவிலான அரசியலமைப்பு அமைப்பு எது?",
        "District Planning Committee (DPC)", "மாவட்ட திட்டமிடும் குழு (District Planning Committee - DPC)",
        "District Rural Development Agency (DRDA)", "மாவட்ட ஊரக வளர்ச்சி முகமை (DRDA)",
        "State Planning Commission Regional Directorate", "மாநில திட்டக் குழு பிராந்திய இயக்குநரகம்",
        "District Vigilance and Monitoring Committee (DISHA)", "மாவட்ட கண்காணிப்புக் குழு (திஷா)",
        "A",
        "Article 243ZD mandates the constitution of a District Planning Committee (DPC) in every State at the district level to consolidate the plans prepared by the Panchayats and the Municipalities in the district and to prepare a draft development plan for the district as a whole.",
        "சரத்து 243ZD ஒவ்வொரு மாநிலத்திலும் மாவட்ட அளவில் ஒரு மாவட்ட திட்டமிடும் குழுவை (DPC) அமைக்க கட்டாயமாக்குகிறது; இது மாவட்டத்தில் உள்ள பஞ்சாயத்துகள் மற்றும் நகராட்சிகளால் தயாரிக்கப்பட்ட திட்டங்களை ஒருங்கிணைத்து மாவட்டம் முழுவதற்குமான வரைவு வளர்ச்சித் திட்டத்தைத் தயாரிக்கிறது.",
        "Correct. Article 243ZD mandates the District Planning Committee.", "சரியானது. சரத்து 243ZD மாவட்ட திட்டமிடும் குழுவை கட்டாயமாக்குகிறது.",
        "Incorrect. DRDA is a registered society for centrally sponsored schemes, not a constitutional Article 243ZD body.", "தவறானது. DRDA என்பது ஒரு பதிவு செய்யப்பட்ட சங்கம், அரசியலமைப்பு அமைப்பு அல்ல.",
        "Incorrect. State Planning Commission is an executive body of the State government.", "தவறானது. மாநில திட்டக் குழு என்பது ஒரு நிர்வாக அமைப்பாகும்.",
        "Incorrect. DISHA is a parliamentary monitoring committee for central welfare schemes.", "தவறானது. திஷா என்பது மத்திய திட்டங்களுக்கான பாராளுமன்றக் கண்காணிப்புக் குழு.",
        "Article 243ZD Bridge: Bridges rural (11th Schedule) and urban (12th Schedule) governance into a single coherent district master plan.",
        "சரத்து 243ZD இணைப்பு: கிராமப்புற (11வது அட்டவணை) மற்றும் நகர்ப்புற (12வது அட்டவணை) நிர்வாகத்தை ஒரே ஒருங்கிணைந்த மாவட்ட வளர்ச்சித் திட்டமாக இணைக்கிறது."
    ))

    return qs

if __name__ == "__main__":
    qs = get_batch4()
    print(f"Batch 4 generated {len(qs)} questions.")
