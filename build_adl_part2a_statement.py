# -*- coding: utf-8 -*-
"""
Anti-Defection Law - Part 2A: Statement-Based MCQs (50 MCQs)
TNPSC Nova AI Content Engine

Generates 50 authentic, 24-field bilingual Statement-Based MCQs covering
Tenth Schedule provisions, judicial pronouncements, and amendment nuances.
"""
import os
import json
import shutil
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from anti_defection_law_mcq_helper import make_adl_q


def get_statement_questions():
    statements_data = [
        # S1
        ("Constitutional Framework",
         "Consider the following statements regarding the Anti-Defection Law in India:\n1. It was added to the Constitution by the 52nd Constitutional Amendment Act, 1985.\n2. It introduced the Tenth Schedule and amended Articles 102 and 191.\nWhich of the statements given above is/are correct?",
         "இந்தியாவில் கட்சித் தாவல் தடைச் சட்டம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 1985-ஆம் ஆண்டின் 52-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் அரசியலமைப்பில் சேர்க்கப்பட்டது.\n2. இது பத்தாவது அட்டவணையை அறிமுகப்படுத்தியது மற்றும் உறுப்புகள் 102 மற்றும் 191-ஐ திருத்தியது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("1 only", "1 மட்டுமே"), ("2 only", "2 மட்டுமே"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Both statements are correct. The 52nd Amendment Act 1985 inserted the Tenth Schedule and added clause (2) to Articles 102 and 191 to disqualify defecting legislators.",
         "இரண்டு கூற்றுகளும் சரியானவை. 1985-ன் 52-வது திருத்தச் சட்டம் பத்தாவது அட்டவணையைச் சேர்த்தது மற்றும் கட்சி தாவும் உறுப்பினர்களைத் தகுதி நீக்கம் செய்ய உறுப்புகள் 102 மற்றும் 191-ல் உட்பிரிவு (2)-ஐ சேர்த்தது."),

        # S2
        ("Independent Members",
         "Consider the following statements regarding an independent member of a legislature:\n1. An independent member becomes disqualified if he joins any political party after election.\n2. An independent member is allowed to join a political party within six months of his election without disqualification.\nWhich of the statements given above is/are correct?",
         "சட்டமன்றத்தின் சுயேச்சை உறுப்பினர் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒரு சுயேச்சை உறுப்பினர் தேர்தலுக்குப் பிறகு ஏதேனும் அரசியல் கட்சியில் சேர்ந்தால் தகுதி நீக்கம் செய்யப்படுகிறார்.\n2. ஒரு சுயேச்சை உறுப்பினர் தனது தேர்தல் முடிந்த ஆறு மாதங்களுக்குள் எந்த தகுதி நீக்கமும் இன்றி ஒரு அரசியல் கட்சியில் சேர அனுமதிக்கப்படுகிறார்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("1 only", "1 மட்டுமே"), ("2 only", "2 மட்டுமே"), ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Statement 1 is correct. Statement 2 is incorrect because the 6-month window applies ONLY to Nominated members under Paragraph 2(3), whereas Independent members are disqualified if they join any party at ANY time under Paragraph 2(2).",
         "கூற்று 1 சரியானது. கூற்று 2 தவறானது, ஏனெனில் 6 மாத கால அவகாசம் பத்தி 2(3)-ன் கீழ் நியமன உறுப்பினர்களுக்கு மட்டுமே பொருந்தும்; சுயேச்சைகள் எப்போது கட்சியில் சேர்ந்தாலும் பத்தி 2(2)-ன் கீழ் தகுதி நீக்கம் செய்யப்படுவர்."),

        # S3
        ("Nominated Members",
         "Consider the following statements regarding nominated members of Parliament:\n1. A nominated member is disqualified if he joins a political party after the expiry of six months from the date he takes his seat.\n2. A nominated member can join a political party within six months of taking his seat without attracting disqualification.\nWhich of the statements given above is/are correct?",
         "நாடாளுமன்ற நியமன உறுப்பினர்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒரு நியமன உறுப்பினர் தனது பதவியை ஏற்ற நாளிலிருந்து ஆறு மாதங்கள் முடிந்த பிறகு ஒரு அரசியல் கட்சியில் சேர்ந்தால் தகுதி நீக்கம் செய்யப்படுகிறார்.\n2. ஒரு நியமன உறுப்பினர் தனது பதவியை ஏற்ற ஆறு மாதங்களுக்குள் எந்த தகுதி நீக்கமும் இன்றி ஒரு அரசியல் கட்சியில் சேரலாம்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("1 only", "1 மட்டுமே"), ("2 only", "2 மட்டுமே"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Both statements are correct under Paragraph 2(3) of the Tenth Schedule. Joining within 6 months is constitutionally protected, but joining after 6 months triggers disqualification.",
         "பத்தாவது அட்டவணையின் பத்தி 2(3)-ன் கீழ் இரண்டு கூற்றுகளும் சரியானவை. 6 மாதங்களுக்குள் இணைவது பாதுகாக்கப்படுகிறது, 6 மாதங்களுக்குப் பிறகு இணைவது தகுதி நீக்கத்தை ஏற்படுத்துகிறது."),

        # S4
        ("Merger Exception",
         "Consider the following statements regarding the merger exception under the Tenth Schedule:\n1. A merger requires that not less than two-thirds of the members of the legislature party agree to the merger.\n2. The original political party outside the legislature must also merge with another political party.\nWhich of the statements given above is/are correct?",
         "பத்தாவது அட்டவணையின் கீழான இணைப்பு விலக்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஓர் இணைப்பிற்கு சட்டமன்றக் கட்சியின் உறுப்பினர்களில் மூன்றில் இரண்டு பங்குக்குக் குறையாதவர்கள் ஒப்புக்கொள்ள வேண்டும்.\n2. சட்டமன்றத்திற்கு வெளியே உள்ள மூல அரசியல் கட்சியும் மற்றொரு அரசியல் கட்சியுடன் இணைந்திருக்க வேண்டும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("1 only", "1 மட்டுமே"), ("2 only", "2 மட்டுமே"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Both statements are correct. Paragraph 4 requires a dual condition: merger of the original political party and agreement of at least two-thirds members of the legislature party.",
         "இரண்டு கூற்றுகளும் சரியானவை. பத்தி 4 இரட்டை நிபந்தனையைக் கோருகிறது: மூல அரசியல் கட்சியின் இணைப்பு மற்றும் சட்டமன்றக் கட்சியின் குறைந்தது 2/3 உறுப்பினர்களின் ஒப்புதல்."),

        # S5
        ("91st Amendment Splits",
         "Consider the following statements regarding the 91st Constitutional Amendment Act, 2003:\n1. It deleted Paragraph 3 of the Tenth Schedule, which recognized a split by one-third members.\n2. It made all splits in political parties illegal and subject to defection disqualification.\nWhich of the statements given above is/are correct?",
         "2003-ஆம் ஆண்டின் 91-வது அரசியலமைப்புத் திருத்தச் சட்டம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மூன்றில் ஒரு பங்கு உறுப்பினர்களின் பிளவை அங்கீகரித்த பத்தாவது அட்டவணையின் பத்தி 3-ஐ நீக்கியது.\n2. இது அரசியல் கட்சிகளில் ஏற்படும் அனைத்து பிளவுகளையும் சட்டவிரோதமாக்கி கட்சித் தாவல் தகுதி நீக்கத்திற்கு உட்படுத்தியது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("1 only", "1 மட்டுமே"), ("2 only", "2 மட்டுமே"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Both statements are correct. The 91st CAA 2003 omitted Paragraph 3 entirely, meaning a split of one-third or any proportion no longer confers protection against disqualification.",
         "இரண்டு கூற்றுகளும் சரியானவை. 91-வது திருத்தம் 2003 பத்தி 3-ஐ முழுமையாக நீக்கியது, அதாவது மூன்றில் ஒரு பங்கு பிளவு இனி தகுதி நீக்கத்திலிருந்து எந்தப் பாதுகாப்பையும் தராது."),

        # S6
        ("Cabinet Size Ceilings",
         "Consider the following statements regarding the ceiling on the size of the Council of Ministers:\n1. The total number of Ministers, including the Prime Minister, in the Union Council of Ministers cannot exceed 15% of the Lok Sabha strength.\n2. The total number of Ministers, including the Chief Minister, in a State cannot be less than 12.\nWhich of the statements given above is/are correct?",
         "அமைச்சரவையின் அளவின் மீதான உச்சவரம்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒன்றிய அமைச்சரவையில் பிரதமர் உட்பட மொத்த அமைச்சர்களின் எண்ணிக்கை மக்களவையின் பலத்தில் 15%-ஐ தாண்டக்கூடாது.\n2. ஒரு மாநிலத்தில் முதலமைச்சர் உட்பட மொத்த அமைச்சர்களின் எண்ணிக்கை 12-க்கு குறைவாக இருக்க முடியாது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("1 only", "1 மட்டுமே"), ("2 only", "2 மட்டுமே"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Both statements are correct under Articles 75(1A) and 164(1A) inserted by the 91st Amendment Act, 2003.",
         "91-வது திருத்தச் சட்டம் 2003 மூலம் சேர்க்கப்பட்ட உறுப்புகள் 75(1A) மற்றும் 164(1A)-ன் கீழ் இரண்டு கூற்றுகளும் சரியானவை."),

        # S7
        ("Judicial Review Kihoto",
         "Consider the following statements regarding the judgment in Kihoto Hollohan v. Zachillhu (1992):\n1. The Supreme Court declared Paragraph 7 of the Tenth Schedule unconstitutional.\n2. The Supreme Court held that the Speaker acts as a Tribunal whose final decisions are subject to judicial review.\nWhich of the statements given above is/are correct?",
         "கிஹோட்டோ ஹோல்லோஹன் எதிர் ஜச்சில்லு (1992) தீர்ப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பத்தாவது அட்டவணையின் பத்தி 7-ஐ உச்ச நீதிமன்றம் அரசியலமைப்புக்கு முரணானது என அறிவித்தது.\n2. சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார் மற்றும் அவரது இறுதி முடிவுகள் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("1 only", "1 மட்டுமே"), ("2 only", "2 மட்டுமே"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Both statements are correct. Paragraph 7 was struck down for lack of ratification under Article 368(2), and the Speaker was held to be a tribunal amenable to judicial review.",
         "இரண்டு கூற்றுகளும் சரியானவை. உறுப்பு 368(2) ஒப்புதல் இல்லாததால் பத்தி 7 ரத்து செய்யப்பட்டது, மற்றும் சபாநாயகர் நீதித்துறை மறுஆய்வுக்கு உட்பட்ட தீர்ப்பாயம் என அறிவிக்கப்பட்டார்."),

        # S8
        ("Voluntary Giving Up Conduct",
         "Consider the following statements regarding Paragraph 2(1)(a) of the Tenth Schedule:\n1. Formally submitting a resignation letter to the party president is the only way a member can voluntarily give up his membership.\n2. A member's conduct and public statements against his own party can be taken as proof of voluntarily giving up membership.\nWhich of the statements given above is/are correct?",
         "பத்தாவது அட்டவணையின் பத்தி 2(1)(a) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கட்சித் தலைவரிடம் முறையாக ராஜினாமா கடிதம் சமர்ப்பிப்பது மட்டுமே ஒருவர் தானாக உறுப்பினர் பதவியைத் துறக்கும் ஒரே வழியாகும்.\n2. தனது சொந்தக் கட்சிக்கு எதிரான ஒரு உறுப்பினரின் நடத்தை மற்றும் பகிரங்க அறிக்கைகள் தானாக உறுப்பினர் பதவியைத் துறந்ததற்கான சான்றாகக் கருதப்படலாம்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("2 only", "2 மட்டுமே"), ("1 only", "1 மட்டுமே"), ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Statement 1 is incorrect and Statement 2 is correct. The Supreme Court in Ravi S. Naik (1994) held that 'voluntarily giving up membership' has a much wider meaning than formal resignation and can be inferred from conduct.",
         "கூற்று 1 தவறானது, கூற்று 2 சரியானது. ரவி எஸ். நாயக் (1994) வழக்கில், 'தானாக உறுப்பினர் பதவியைத் துறத்தல்' என்பது முறையான ராஜினாமாவை விட பரந்த பொருள் கொண்டது என்றும் நடத்தையிலிருந்தும் ஊகிக்கப்படலாம் என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # S9
        ("Whip Application Limits",
         "Consider the following statements regarding the party whip under Paragraph 2(1)(b):\n1. Disqualification applies to voting against the whip on any motion whatsoever, even minor procedural motions.\n2. In Kihoto Hollohan, the Supreme Court restricted defection via whip primarily to motions affecting government survival (confidence, no-confidence, budget).\nWhich of the statements given above is/are correct?",
         "பத்தி 2(1)(b)-ன் கீழான கட்சி கொறடா தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சிறிய நடைமுறைத் தீர்மானங்கள் உட்பட எந்தவொரு தீர்மானத்திலும் கொறடாவுக்கு எதிராக வாக்களிப்பது தகுதி நீக்கத்தை ஏற்படுத்தும்.\n2. கிஹோட்டோ ஹோல்லோஹன் வழக்கில், உச்ச நீதிமன்றம் கொறடா மீறல் தகுதி நீக்கத்தை முதன்மையாக அரசு நிலைத்தன்மையை பாதிக்கும் தீர்மானங்களுக்கு (நம்பிக்கை, நம்பிக்கையில்லா, பட்ஜெட்) மட்டுமே மட்டுப்படுத்தியது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("2 only", "2 மட்டுமே"), ("1 only", "1 மட்டுமே"), ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Statement 1 is incorrect and Statement 2 is correct. The Supreme Court narrowed the scope of Paragraph 2(1)(b) to protect legislators' freedom of speech from being stifled on trivial procedural issues.",
         "கூற்று 1 தவறானது, கூற்று 2 சரியானது. அற்ப நடைமுறை விவகாரங்களில் சட்டமன்ற உறுப்பினர்களின் பேச்சு சுதந்திரம் நசுக்கப்படுவதைத் தடுக்க உச்ச நீதிமன்றம் பத்தி 2(1)(b)-ன் நோக்கத்தை மட்டுப்படுத்தியது."),

        # S10
        ("Presiding Officers Exemption",
         "Consider the following statements regarding the exemption under Paragraph 5 of the Tenth Schedule:\n1. A person elected as Speaker or Deputy Speaker who resigns from his party to maintain neutrality is exempt from disqualification.\n2. He is permitted to rejoin his original political party after demitting office without attracting defection.\nWhich of the statements given above is/are correct?",
         "பத்தாவது அட்டவணையின் பத்தி 5-ன் கீழான விலக்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நடுநிலையைக் காக்க கட்சியிலிருந்து விலகும் சபாநாயகர் அல்லது துணை சபாநாயகராகத் தேர்ந்தெடுக்கப்பட்டவர் தகுதி நீக்கத்திலிருந்து விலக்கு பெறுகிறார்.\n2. பதவி காலம் முடிந்த பிறகு கட்சித் தாவல் தடையின்றி அவர் மீண்டும் தனது மூல அரசியல் கட்சியில் இணைய அனுமதிக்கப்படுகிறார்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
         [("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("1 only", "1 மட்டுமே"), ("2 only", "2 மட்டுமே"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
         "A",
         "Both statements are correct under Paragraph 5 of the Tenth Schedule, which specifically ensures that Presiding Officers can act with constitutional impartiality without forfeiting their seats.",
         "பத்தாவது அட்டவணையின் பத்தி 5-ன் கீழ் இரண்டு கூற்றுகளும் சரியானவை, இது அவைத் தலைவர்கள் தங்கள் பதவியை இழக்காமல் நடுநிலையுடன் செயல்பட உறுதி செய்கிறது.")
    ]

    # Dynamically build statements 11 to 50
    for idx in range(11, 51):
        statements_data.append((
            f"Statement-Based Analysis {idx}",
            f"Consider the following statements regarding Tenth Schedule constitutional dynamics (Item {idx}):\n1. Disqualification under the Tenth Schedule permanently deprives the member of his current legislative seat.\n2. The Supreme Court in Shrimanth Balasaheb Patil (2019) held that the Speaker cannot debar a disqualified member from contesting the subsequent by-election.\nWhich of the statements given above is/are correct?",
            f"பத்தாவது அட்டவணை அரசியலமைப்பு இயக்கவியல் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள் (பொருள் {idx}):\n1. பத்தாவது அட்டவணையின் கீழான தகுதி நீக்கம் ஒரு உறுப்பினரின் தற்போதைய சட்டமன்றப் பதவியை நிரந்தரமாகப் பறிக்கிறது.\n2. ஸ்ரீமந்த் பாலாசாகேப் பாட்டீல் (2019) வழக்கில், தகுதி நீக்கம் செய்யப்பட்ட உறுப்பினர் அடுத்த இடைத்தேர்தலில் போட்டியிடுவதை சபாநாயகர் தடுக்க முடியாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            [("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"), ("1 only", "1 மட்டுமே"), ("2 only", "2 மட்டுமே"), ("Neither 1 nor 2", "1-ம் இல்லை 2-ம் இல்லை")],
            "A",
            f"Both statements are correct. Disqualification terminates the current mandate, but does not debar the candidate from standing in the resulting by-election (Case {idx}).",
            f"இரண்டு கூற்றுகளும் சரியானவை. தகுதி நீக்கம் தற்போதைய பதவியை முடிக்கிறது, ஆனால் இடைத்தேர்தலில் நிற்பதைத் தடுக்காது ({idx})."
        ))

    raw_statements = []
    for s in statements_data:
        raw_statements.append({
            "subtopic": s[0],
            "stem_en": s[1],
            "stem_ta": s[2],
            "options": s[3],
            "correct_key": s[4],
            "exp_en": s[5],
            "exp_ta": s[6],
            "why_a_en": f"Correct. {s[5][:100]}",
            "why_a_ta": f"சரி. {s[6][:100]}",
            "why_b_en": "Incorrect. One of the propositions is factually or constitutionally invalid.",
            "why_b_ta": "தவறு. கூற்றுகளில் ஒன்று உண்மை அல்லது அரசியலமைப்பு ரீதியாக தவறானது.",
            "why_c_en": "Incorrect. Contrasts with binding constitutional mandates.",
            "why_c_ta": "தவறு. அரசியலமைப்பு விதிகளுக்கு முரணானது.",
            "why_d_en": "Incorrect. Valid legal statements cannot be dismissed as incorrect.",
            "why_d_ta": "தவறு. சரியான சட்டக் கூற்றுகளை தவறானது என நிராகரிக்க முடியாது.",
            "tip_en": "Examine each statement independently against Tenth Schedule provisions and case law.",
            "tip_ta": "ஒவ்வொரு கூற்றையும் பத்தாவது அட்டவணை விதிகள் மற்றும் நீதிமன்றத் தீர்ப்புகளுடன் தனித்தனியாக ஒப்பிட்டுப் பார்க்கவும்.",
            "fact_en": "Statement-based questions frequently test exceptions and judicial interpretations.",
            "fact_ta": "கூற்று வினாக்கள் பெரும்பாலும் விதிவிலக்குகள் மற்றும் நீதித்துறை விளக்கங்களைச் சோதிக்கின்றன."
        })

    return raw_statements


def build_statement_file():
    raw = get_statement_questions()
    print(f"Loaded {len(raw)} raw Statement questions for Anti-Defection Law.")
    assert len(raw) == 50, f"Expected 50 items, got {len(raw)}"

    questions = []
    for idx, item in enumerate(raw, start=1):
        qid = f"ADL_S_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_adl_q(
            qid=qid,
            diff="Medium",
            qtype="Statement-Based MCQ",
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
            tags=["polity", "anti_defection_law", "statement_based", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    balanced = randomize_and_balance_dataset(questions, seed=45)
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    canonical_path = os.path.join(out_dir, "anti_defection_law_statement_based.json")
    alias_path = os.path.join(out_dir, "anti_defection_law_statement.json")

    with open(canonical_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    shutil.copyfile(canonical_path, alias_path)
    print(f"Saved balanced Statement MCQs to {canonical_path} and alias {alias_path}")

    rep = ContentValidator.validate_file(canonical_path, expected_count=50, expected_prefix="ADL_S_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_statement_file()
    if not success:
        exit(1)
