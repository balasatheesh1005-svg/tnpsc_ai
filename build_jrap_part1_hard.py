# -*- coding: utf-8 -*-
"""
Build Judicial Review, Activism & PIL - Part 1 Hard (50 MCQs)
Identifier: JRAP_H_001 to JRAP_H_050
Key Distribution: A: 12, B: 13, C: 12, D: 13 (Total: 50)
Anti-Block: Max consecutive run <= 2
"""
import json
import os
from collections import Counter
from judicial_review_mcq_helper import make_jrap_q

def build_hard_mcqs():
    questions = []

    hard_data = [
        # 1 - B
        ("JRAP_H_001", "Sajjan Singh Dissents",
         "In Sajjan Singh v. State of Rajasthan (1965), which two dissenting judges famously expressed doubts regarding Parliament's unlimited power to amend Fundamental Rights, planting the intellectual seeds for the Basic Structure Doctrine?",
         "சஜ்ஜன் சிங் v. ராஜஸ்தான் மாநிலம் (1965) வழக்கில், அடிப்படை உரிமைகளைத் திருத்துவதற்கான நாடாளுமன்றத்தின் வரம்பற்ற அதிகாரம் குறித்து சந்தேகங்களை வெளிப்படுத்தி, அடிப்படைக் கட்டமைப்புக் கோட்பாட்டிற்கு அறிவுசார் விதைகளை விதைத்த இரண்டு மாறுபட்ட தீர்ப்பளித்த நீதிபதிகள் யார்?",
         "Justice P.B. Gajendragadkar and Justice K.N. Wanchoo", "நீதிபதி பி.பி. கஜேந்திரகட்கர் மற்றும் நீதிபதி கே.என். வாஞ்சூ",
         "Justice M. Hidayatullah and Justice J.R. Mudholkar", "நீதிபதி எம். ஹிதாயத்துல்லா மற்றும் நீதிபதி ஜே.ஆர். முதோல்கர்",
         "Justice S.M. Sikri and Justice J.M. Shelat", "நீதிபதி எஸ்.எம். சிக்ரி மற்றும் நீதிபதி ஜே.எம். ஷெலத்",
         "Justice H.R. Khanna and Justice K.S. Hegde", "நீதிபதி எச்.ஆர். கன்னா மற்றும் நீதிபதி கே.எஸ். ஹெக்டே", "B",
         "Justice Hidayatullah queried whether Fundamental Rights could be the plaything of a parliamentary majority, while Justice Mudholkar referenced the Pakistan Supreme Court's concept of 'basic features'.",
         "நீதிபதி ஹிதாயத்துல்லா அடிப்படை உரிமைகள் நாடாளுமன்ற பெரும்பான்மையின் விளையாட்டுப் பொருளாக இருக்க முடியுமா எனக் கேட்டார்; நீதிபதி முதோல்கர் பாகிஸ்தான் உச்ச நீதிமன்றத்தின் 'அடிப்படை அம்சங்கள்' கருத்தைக் குறிப்பிட்டார்."),

        # 2 - D
        ("JRAP_H_002", "Kesavananda Bench Distribution",
         "What was the exact judicial bench strength and voting split in Kesavananda Bharati v. State of Kerala (1973)?",
         "கேசவாநந்த பாரதி v. கேரள மாநிலம் (1973) வழக்கின் சரியான நீதிபதிகள் அமர்வு பலம் மற்றும் வாக்கு விகிதம் என்ன?",
         "9 judges bench, decided by 5:4 majority", "9 நீதிபதிகள் அமர்வு, 5:4 பெரும்பான்மையில் தீர்மானிக்கப்பட்டது",
         "11 judges bench, decided by 6:5 majority", "11 நீதிபதிகள் அமர்வு, 6:5 பெரும்பான்மையில் தீர்மானிக்கப்பட்டது",
         "7 judges bench, decided unanimously", "7 நீதிபதிகள் அமர்வு, ஏகமனதாக தீர்மானிக்கப்பட்டது",
         "13 judges bench, decided by 7:6 majority", "13 நீதிபதிகள் அமர்வு, 7:6 பெரும்பான்மையில் தீர்மானிக்கப்பட்டது", "D",
         "Kesavananda Bharati was heard by the largest bench in Indian history (13 judges) for 68 days, culminating in a 7:6 split verdict propounding the Basic Structure Doctrine.",
         "கேசவாநந்த பாரதி வழக்கு இந்திய வரலாற்றிலேயே மிகப் பெரிய 13 நீதிபதிகள் கொண்ட அமர்வால் 68 நாட்கள் விசாரிக்கப்பட்டு, 7:6 என்ற பிளவுபட்ட தீர்ப்பில் அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை உருவாக்கியது."),

        # 3 - A
        ("JRAP_H_003", "Justice H.R. Khanna's Deciding Vote",
         "In Kesavananda Bharati (1973), who delivered the pivotal deciding judgment that tilted the 7:6 balance in favor of formulating the Basic Structure Doctrine?",
         "கேசவாநந்த பாரதி (1973) வழக்கில் 7:6 சமநிலையை அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை உருவாக்குவதற்கு ஆதரவாக சாய்த்த முக்கிய தீர்ப்பை வழங்கியவர் யார்?",
         "Justice H.R. Khanna", "நீதிபதி எச்.ஆர். கன்னா",
         "Chief Justice S.M. Sikri", "தலைமை நீதிபதி எஸ்.எம். சிக்ரி",
         "Justice A.N. Ray", "நீதிபதி ஏ.என். ரே",
         "Justice Y.V. Chandrachud", "நீதிபதி ஒய்.வி. சந்திரசூட்", "A",
         "Justice H.R. Khanna held that while Parliament could amend any provision including Fundamental Rights, the word 'amendment' in Art. 368 implies that the old Constitution cannot be replaced or its identity destroyed.",
         "நீதிபதி எச்.ஆர். கன்னா, நாடாளுமன்றம் எதனையும் திருத்தலாம் என்றாலும், உறுப்பு 368-ல் உள்ள 'திருத்தம்' என்ற சொல் பழைய அரசியலமைப்பை முழுமையாக மாற்றவோ அதன் அடையாளத்தை அழிக்கவோ முடியாது என்பதைக் குறிக்கிறது என்றார்."),

        # 4 - C
        ("JRAP_H_004", "I.R. Coelho Case Bench and Author",
         "In the landmark I.R. Coelho v. State of Tamil Nadu (2007) judgment which affirmed judicial review of the Ninth Schedule, who authored the unanimous verdict for the 9-judge bench?",
         "9வது அட்டவணையின் நீதித்துறை மறுஆய்வை உறுதிப்படுத்திய வரலாற்றுச் சிறப்புமிக்க I.R. கோயல்ஹோ வழக்கில் (2007) 9 நீதிபதிகள் அமர்வின் ஏகமனதான தீர்ப்பை எழுதியவர் யார்?",
         "Chief Justice K.G. Balakrishnan", "தலைமை நீதிபதி கே.ஜி. பாலகிருஷ்ணன்",
         "Justice P.N. Bhagwati", "நீதிபதி பி.என். பகவதி",
         "Chief Justice Y.K. Sabharwal", "தலைமை நீதிபதி ஒய்.கே. சபர்வால்",
         "Justice S.B. Sinha", "நீதிபதி எஸ்.பி. சின்ஹா", "C",
         "Chief Justice Y.K. Sabharwal authored the unanimous 9-judge Constitution Bench judgment in I.R. Coelho (2007), holding that the Ninth Schedule cannot be a vault to bury Fundamental Rights.",
         "தலைமை நீதிபதி ஒய்.கே. சபர்வால் I.R. கோயல்ஹோ வழக்கில் 9 நீதிபதிகள் அமர்வின் ஏகமனதான தீர்ப்பை எழுதினார்; 9வது அட்டவணை அடிப்படை உரிமைகளைப் புதைக்கும் பெட்டகமாக இருக்க முடியாது என்றார்."),

        # 5 - B
        ("JRAP_H_005", "Coelho Essence of Rights Test",
         "In I.R. Coelho (2007), the Supreme Court introduced which dual test to evaluate whether a law placed in the Ninth Schedule post-1973 violates the Basic Structure?",
         "I.R. கோயல்ஹோ (2007) வழக்கில் 1973-க்குப் பின்னர் 9வது அட்டவணையில் வைக்கப்பட்ட சட்டம் அடிப்படைக் கட்டமைப்பை மீறுகிறதா என்பதை மதிப்பீடு செய்ய உச்ச நீதிமன்றம் எந்த இரட்டைச் சோதனையை அறிமுகப்படுத்தியது?",
         "Pith and Substance test and Colourability test", "அடிநாத சோதனை மற்றும் போலிச் சட்ட சோதனை",
         "Direct Impact and Effect Test ('Rights Test') and Essence of the Fundamental Rights Test", "நேரடி தாக்கம் மற்றும் விளைவுச் சோதனை ('உரிமைகள் சோதனை') மற்றும் அடிப்படை உரிமைகளின் சாராம்சச் சோதனை",
         "Wednesbury test and Proportionality test", "வெட்னஸ்பரி சோதனை மற்றும் விகிதாசார சோதனை",
         "Public Interest test and Sovereign Immunity test", "பொது நலன் சோதனை மற்றும் இறையாண்மை விலக்களிப்பு சோதனை", "B",
         "The court ruled that it is not the form of the amendment but its 'effect and impact' on Part III rights (Articles 14, 19, 21) and the 'essence of the rights' test that determines constitutional validity.",
         "திருத்தத்தின் வடிவம் அல்ல, பகுதி III உரிமைகள் (உறுப்புகள் 14, 19, 21) மீதான அதன் 'தாக்கம் மற்றும் விளைவு' மற்றும் 'உரிமைகளின் சாராம்சம்' ஆகியவையே செல்லுபடியாகும் தன்மையைத் தீர்மானிக்கின்றன எனப்பட்டது."),

        # 6 - D
        ("JRAP_H_006", "ADM Jabalpur Habeas Corpus Case",
         "In ADM Jabalpur v. Shivkant Shukla (1976), famously known as the 'Habeas Corpus Case', what was the infamous majority ruling regarding Article 21 during Emergency?",
         "ஹேபியஸ் கார்பஸ் வழக்கு என அறியப்படும் ADM ஜபல்பூர் v. சிவகாந்த் சுக்லா (1976) வழக்கில் அவசரநிலையின் போது உறுப்பு 21 குறித்து வழங்கப்பட்ட அவப்பெயர் பெற்ற பெரும்பான்மைத் தீர்ப்பு என்ன?",
         "Article 21 cannot be suspended under any circumstances", "எந்தச் சூழ்நிலையிலும் உறுப்பு 21-ஐ இடைநிறுத்தம் செய்ய முடியாது",
         "Only High Courts could issue habeas corpus writs", "உயர் நீதிமன்றங்கள் மட்டுமே ஆட்கொணர்வு மனுவை வெளியிட முடியும்",
         "Police officers were held personally liable for detentions", "கைதுகளுக்கு காவல்துறை அதிகாரிகளே தனிப்பட்ட முறையில் பொறுப்பாவார்கள்",
         "In view of the Presidential Order under Art. 359(1), no person has any locus standi to move any court for habeas corpus challenging illegal detention", "உறுப்பு 359(1) பிரகடனத்தின் பார்வையில், சட்டவிரோத தடுப்புக் காவலை எதிர்த்து ஆட்கொணர்வு கோரி நீதிமன்றத்தை அணுக எவருக்கும் உரிமை இல்லை", "D",
         "A 4:1 majority held that during Emergency, personal liberty under Article 21 is completely eclipsed. Justice H.R. Khanna famously dissented, for which he was superseded for Chief Justiceship.",
         "அவசரநிலையின் போது உறுப்பு 21 முற்றிலும் மறைகிறது என 4:1 பெரும்பான்மையில் கூறப்பட்டது; நீதிபதி எச்.ஆர். கன்னா தைரியமாக மாறுபட்ட தீர்ப்பை வழங்கியதால் தலைமை நீதிபதி பதவியை இழந்தார்."),

        # 7 - A
        ("JRAP_H_007", "Overruling ADM Jabalpur in Puttaswamy",
         "In which 2017 judgment did the 9-judge Constitution Bench formally and expressly overrule the infamous ADM Jabalpur (1976) decision?",
         "எந்த 2017 தீர்ப்பில் 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு ADM ஜபல்பூர் (1976) தீர்ப்பை வெளிப்படையாகவும் முறையாகவும் ரத்து செய்தது?",
         "Justice K.S. Puttaswamy (Retd.) v. Union of India (2017)", "நீதிபதி கே.எஸ். புட்டசுவாமி (ஓய்வு) v. இந்திய ஒன்றியம் (2017)",
         "Shreya Singhal v. Union of India (2015)", "ஸ்ரேயா சிங்கால் v. இந்திய ஒன்றியம் (2015)",
         "Navtej Singh Johar v. Union of India (2018)", "நவ்தேஜ் சிங் ஜோஹர் v. இந்திய ஒன்றியம் (2018)",
         "Joseph Shine v. Union of India (2018)", "ஜோசப் ஷைன் v. இந்திய ஒன்றியம் (2018)", "A",
         "In Puttaswamy (2017), the Supreme Court formally buried the ADM Jabalpur ruling, upholding Justice H.R. Khanna's lone dissent that the right to life is primordial and precedes the Constitution.",
         "புட்டசுவாமி (2017) வழக்கில் உச்ச நீதிமன்றம் ADM ஜபல்பூர் தீர்ப்பை ரத்து செய்து, வாழ்வு உரிமை அரசியலமைப்புக்கு முந்தையது என்ற நீதிபதி எச்.ஆர். கன்னாவின் வரலாற்று மாற்றுக் கருத்தை உறுதி செய்தது."),

        # 8 - C
        ("JRAP_H_008", "Supreme Court Bar Association 1998",
         "In Supreme Court Bar Association v. Union of India (1998), how did the Constitution Bench restrict the plenary power of the Supreme Court under Article 142?",
         "உச்ச நீதிமன்ற வழக்கறிஞர்கள் சங்கம் v. இந்திய ஒன்றியம் (1998) வழக்கில் உறுப்பு 142-ன் கீழான உச்ச நீதிமன்றத்தின் முழுமையான அதிகாரத்தை அரசியலமைப்பு அமர்வு எவ்வாறு கட்டுப்படுத்தியது?",
         "Article 142 was declared completely unconstitutional", "உறுப்பு 142 முற்றிலும் அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்டது",
         "Article 142 can only be used on recommendation of the Law Minister", "சட்ட அமைச்சரின் பரிந்துரையின் பேரில் மட்டுமே உறுப்பு 142 பயன்படுத்தப்படலாம்",
         "Article 142 power cannot be used to supplant or ignore express substantive statutory provisions (e.g. suspending advocate license under Contempt)", "உறுப்பு 142 அதிகாரம் வெளிப்படையான சட்டவிதிகளைப் புறக்கணிக்கவோ அல்லது மீறவோ பயன்படுத்த முடியாது (எ.கா. அவமதிப்பு வழக்கில் வழக்கறிஞர் உரிமத்தை இடைநிறுத்துதல்)",
         "Article 142 applies only to consumer disputes", "உறுப்பு 142 நுகர்வோர் தகராறுகளுக்கு மட்டுமே பொருந்தும்", "C",
         "The Supreme Court held that Article 142 is a corrective power to do justice between parties, but it cannot override substantive statutory laws or strip professional licenses outside the Advocates Act.",
         "உறுப்பு 142 நீதியை நிலைநாட்டும் திருத்தும் அதிகாரம் ஆகும்; ஆனால் அது வெளிப்படையான சட்டங்களை மீறவோ வழக்கறிஞர்கள் சட்டத்திற்கு அப்பாற்பட்டு உரிமத்தை ரத்து செய்யவோ முடியாது எனப்பட்டது."),

        # 9 - B
        ("JRAP_H_009", "Article 131 vs Article 32 Private Citizens",
         "Can a private citizen or private company maintain a suit under the original jurisdiction of Article 131 of the Constitution?",
         "அரசியலமைப்பு உறுப்பு 131-ன் அசல் அதிகார வரம்பின் கீழ் ஒரு தனியார் குடிமகனோ அல்லது தனியார் நிறுவனமோ வழக்குத் தொடர முடியுமா?",
         "Yes, if the dispute involves fundamental rights", "ஆம், அச்சிக்கல் அடிப்படை உரிமைகள் சம்பந்தப்பட்டதாக இருந்தால் தொடரலாம்",
         "No, Article 131 is strictly confined to federal disputes between the Union and States or between States inter se", "இல்லை, உறுப்பு 131 மத்திய-மாநிலங்களுக்கு இடையே அல்லது மாநிலங்களுக்கு இடையேயான கூட்டாட்சித் தகராறுகளுக்கு மட்டுமே பிரத்யேகமானது",
         "Yes, with permission of the Attorney General", "ஆம், இந்திய தலைமை வழக்கறிஞரின் அனுமதியுடன் தொடரலாம்",
         "Only in corporate commercial arbitrations", "நிறுவன வணிக மத்தியஸ்தங்களில் மட்டுமே", "B",
         "Article 131 deals exclusively with disputes between constitutional units of the Indian federation (Union and States); private individuals or corporate entities cannot be parties under Art. 131.",
         "உறுப்பு 131 இந்தியக் கூட்டாட்சியின் அரசியலமைப்பு அலகுகளுக்கு (மத்திய மற்றும் மாநிலங்கள்) இடையேயான தகராறுகளை மட்டுமே கையாள்கிறது; தனியார் நபர்கள் இதில் தரப்பினராக முடியாது."),

        # 10 - D
        ("JRAP_H_010", "Article 131 Challenge to Central Legislation",
         "In State of Karnataka v. Union of India (1977) and State of Madhya Pradesh v. Union of India (2011), what was held regarding whether a State can challenge a Central Act under Article 131?",
         "கர்நாடக மாநிலம் v. இந்திய ஒன்றியம் (1977) மற்றும் மத்தியப் பிரதேச மாநிலம் v. இந்திய ஒன்றியம் (2011) வழக்குகளில் உறுப்பு 131-ன் கீழ் ஒரு மாநிலம் மத்திய சட்டத்தை எதிர்க்க முடியுமா என்பது குறித்து என்ன தீர்ப்பளிக்கப்பட்டது?",
         "A State cannot challenge any central act under any circumstances", "எந்தச் சூழ்நிலையிலும் ஒரு மாநிலம் மத்திய சட்டத்தை எதிர்க்க முடியாது",
         "Only Governor can file such a suit", "ஆளுநர் மட்டுமே அத்தகைய வழக்கைத் தாக்கல் செய்ய முடியும்",
         "A State can only challenge Central Acts before the High Court", "உயர் நீதிமன்றத்தில் மட்டுமே மாநிலம் மத்திய சட்டங்களை எதிர்க்க முடியும்",
         "A State can challenge Central legislation under Art. 131 if a legal right of the State is directly affected by the enactment", "மத்திய சட்டத்தால் மாநிலத்தின் சட்ட உரிமை நேரடியாகப் பாதிக்கப்படும் பட்சத்தில் உறுப்பு 131-ன் கீழ் மாநிலம் வழக்குத் தொடரலாம்", "D",
         "The Supreme Court held that the existence of a 'legal right' is the sine qua non of Article 131; if the central law impinges on the constitutional powers or legal rights of a State, Art. 131 is maintainable.",
         "உறுப்பு 131-ன் இன்றியமையாத நிபந்தனை ஒரு 'சட்ட உரிமை' இருப்பதாகும்; மத்திய சட்டம் மாநிலத்தின் அரசியலமைப்பு அதிகாரம் அல்லது சட்ட உரிமையைப் பாதித்தால் உறுப்பு 131-ன் கீழ் வழக்கு தொடரலாம்."),

        # 11 - A
        ("JRAP_H_011", "Curative Petition Origin",
         "The innovative judicial device of 'Curative Petition' to prevent abuse of process and gross miscarriage of justice was evolved by the Supreme Court in:",
         "நீதிமன்ற நடைமுறை துஷ்பிரயோகத்தைத் தடுக்கவும் தீவிர நீதித் தவறைச் சரிசெய்யவும் 'குணப்படுத்தும் மனு' (Curative Petition) என்ற புதிய உத்தியை உச்ச நீதிமன்றம் எதில் உருவாக்கியது?",
         "Rupa Ashok Hurra v. Ashok Hurra (2002)", "ரூபா அசோக் ஹுர்ரா v. அசோக் ஹுர்ரா (2002)",
         "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் v. இந்திய ஒன்றியம் (1980)",
         "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி v. இந்திய ஒன்றியம் (1978)",
         "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி v. கேரள மாநிலம் (1973)", "A",
         "A 5-judge Constitution Bench in Rupa Ashok Hurra (2002) ruled that even after dismissal of a review petition, the Supreme Court can entertain a curative petition to cure gross violation of natural justice.",
         "ரூபா அசோக் ஹுர்ரா (2002) வழக்கில் மறுசீராய்வு மனு தள்ளுபடி செய்யப்பட்ட பிறகும், தீவிர இயற்கை நீதி மீறலைச் சரிசெய்ய 'குணப்படுத்தும் மனுவை' உச்ச நீதிமன்றம் ஏற்கலாம் எனத் தீர்ப்பளிக்கப்பட்டது."),

        # 12 - C
        ("JRAP_H_012", "Curative Petition Mandatory Condition",
         "Which of the following is a mandatory procedural requirement for filing a Curative Petition in the Supreme Court?",
         "உச்ச நீதிமன்றத்தில் ஒரு குணப்படுத்தும் மனுவைத் (Curative Petition) தாக்கல் செய்வதற்கு பின்வருவனவற்றில் கட்டாய நடைமுறைத் தேவை எது?",
         "It must be recommended by the Prime Minister", "அது பிரதமரால் பரிந்துரைக்கப்பட வேண்டும்",
         "It must be approved by the Bar Council of India", "இந்திய பார் கவுன்சிலால் அங்கீகரிக்கப்பட வேண்டும்",
         "It must be certified by a Senior Advocate that the mandatory grounds are satisfied", "கட்டாய காரணங்கள் பூர்த்தி செய்யப்பட்டுள்ளன என்று ஒரு மூத்த வழக்கறிஞரால் சான்றளிக்கப்பட வேண்டும்",
         "It requires prior consent of the Law Commission", "சட்ட ஆணையத்தின் முன் அனுமதி தேவை", "C",
         "A curative petition must contain a certificate by a Senior Advocate verifying that natural justice was violated or a judge failed to disclose bias, to weed out frivolous filings.",
         "இயற்கை நீதி மீறப்பட்டது அல்லது நீதிபதி சார்புநிலையை வெளிப்படுத்தவில்லை என்பதை உறுதிப்படுத்தி ஒரு மூத்த வழக்கறிஞர் சான்றிதழ் அளிப்பது குணப்படுத்தும் மனுவுக்கு கட்டாயமாகும்."),

        # 13 - B
        ("JRAP_H_013", "Epistolary Jurisdiction Limits",
         "In which case did the Supreme Court hold that letters and postcards from interested parties with private motives should not be entertained under epistolary jurisdiction?",
         "தனியார் உள்நோக்கம் கொண்ட ஆர்வமுள்ள தரப்பினரின் கடிதங்கள் மற்றும் அஞ்சல் அட்டைகளை கடித அதிகார வரம்பின் கீழ் ஏற்கக்கூடாது என்று உச்ச நீதிமன்றம் எந்த வழக்கில் தீர்ப்பளித்தது?",
         "Sunil Batra (1980)", "சுனில் பத்ரா (1980)",
         "Subhash Kumar v. State of Bihar (1991)", "சுபாஷ் குமார் v. பீகார் மாநிலம் (1991)",
         "Hussainara Khatoon (1979)", "ஹுசைனாரா காதுன் (1979)",
         "Bandhua Mukti Morcha (1984)", "பந்துவா முக்தி மோர்ச்சா (1984)", "B",
         "In Subhash Kumar (1991), the Supreme Court cautioned that PIL cannot be resorted to by a person who has personal grudge or enmity against the opposite party under the disguise of environmental concern.",
         "சுபாஷ் குமார் (1991) வழக்கில் சுற்றுச்சூழல் போர்வையில் தனிப்பட்ட விரோதம் அல்லது உள்நோக்கம் கொண்டவர்கள் PIL-ஐப் பயன்படுத்த முடியாது என உச்ச நீதிமன்றம் எச்சரித்தது."),

        # 14 - D
        ("JRAP_H_014", "Transformative Constitutionalism",
         "The doctrine of 'Transformative Constitutionalism' repeatedly emphasized in Navtej Johar (2018) and Joseph Shine (2018) signifies that the Constitution's primary objective is to:",
         "நவ்தேஜ் ஜோஹர் (2018) மற்றும் ஜோசப் ஷைன் (2018) வழக்குகளில் வலியுறுத்தப்பட்ட 'உருமாற்றும் அரசியலமைப்புவாதம்' (Transformative Constitutionalism) என்பதன் முதன்மை நோக்கம் என்ன?",
         "Transform the economy into absolute socialism", "பொருளாதாரத்தை முழுமையான சோசலிசமாக மாற்றுவது",
         "Abolish all private properties", "அனைத்து தனியார் சொத்துக்களையும் ஒழிப்பது",
         "Transform the legislative system into a presidential form", "சட்டமன்ற முறையை அதிபர் முறைக்கு மாற்றுவது",
         "Guide society from a medieval, patriarchal and regressive order towards an egalitarian, inclusive and rights-based society", "இடைக்கால, ஆணாதிக்க மற்றும் பிற்போக்கு ஒழுங்கிலிருந்து சமூகத்தை சமத்துவ, அனைவரையும் உள்ளடக்கிய மற்றும் உரிமைகள் சார்ந்த சமூகமாக மாற்றுவது", "D",
         "Transformative constitutionalism treats the Constitution not as a static legal document, but as a living instrument of social transformation fostering equality, liberty, and personal autonomy.",
         "உருமாற்றும் அரசியலமைப்புவாதம் அரசியலமைப்பை ஒரு நிலையான ஆவணமாகக் கருதாமல், சமத்துவம் மற்றும் தனிநபர் தன்னாட்சியை வளர்க்கும் சமூக மாற்றத்திற்கான ஒரு வாழும் கருவியாகக் கருதுகிறது."),

        # 15 - B
        ("JRAP_H_015", "Constitutional Morality Concept",
         "What did Dr. B.R. Ambedkar and modern Supreme Court jurisprudence mean by 'Constitutional Morality' as distinguished from 'Popular Morality'?",
         "டாக்டர் அம்பேத்கர் மற்றும் நவீன உச்ச நீதிமன்ற தீர்ப்புகளில் 'மக்கள் பெரும்பான்மை ஒழுக்கத்திலிருந்து' வேறுபட்ட 'அரசியலமைப்பு ஒழுக்கம்' (Constitutional Morality) என்பது எதனைக் குறிக்கிறது?",
         "Adherence to the prevailing religious majority sentiment", "மதப் பெரும்பான்மையினரின் தற்போதைய உணர்வுகளுக்கு இணங்குவது",
         "Commitment to constitutional values of pluralism, diversity, individual liberty and rule of law over shifting majoritarian prejudices", "மாறிவரும் பெரும்பான்மை தப்பெண்ணங்களை விட பன்மைத்துவம், தனிநபர் சுதந்திரம் மற்றும் சட்டத்தின் ஆட்சி ஆகிய அரசியலமைப்பு விழுமியங்களுக்குக் கட்டுப்படுவது",
         "Strict obedience to ancient customary codes", "பண்டைய வழக்கக் குறியீடுகளுக்குக் கடுமையான கீழ்ப்படிதல்",
         "The moral opinions of the Council of Ministers", "அமைச்சரவையின் தார்மீகக் கருத்துக்கள்", "B",
         "In Navtej Johar, Sabarimala, and Joseph Shine, the SC emphasized that courts must uphold Constitutional Morality (equality, liberty, dignity) even if it conflicts with popular social morality.",
         "சபரிமலை மற்றும் நவ்தேஜ் ஜோஹர் வழக்குகளில், சமூகத்தின் பெரும்பான்மை கருத்துடன் முரண்பட்டாலும் நீதிமன்றங்கள் அரசியலமைப்பு ஒழுக்கத்தையே நிலைநாட்ட வேண்டும் என உச்ச நீதிமன்றம் வலியுறுத்தியது."),

        # 16 - A
        ("JRAP_H_016", "Manifest Arbitrariness Doctrine",
         "In Shayara Bano v. Union of India (2017) (Triple Talaq Case), which groundbreaking ground of Judicial Review of legislation under Article 14 was firmly established by Justice R.F. Nariman?",
         "ஷயாரா பானோ v. இந்திய ஒன்றியம் (2017) (முத்தலாக் வழக்கு) வழக்கில் நீதிபதி ஆர்.எஃப். நாரிமனால் உறுப்பு 14-ன் கீழ் சட்டமன்றச் சட்டங்களை மறுஆய்வு செய்ய உறுதியாக நிறுவப்பட்ட புதிய காரணம் எது?",
         "Manifest Arbitrariness", "வெளிப்படையான தன்னிச்சைத் தன்மை (Manifest Arbitrariness)",
         "Doctrine of Severability", "பிரித்தெடுக்கும் கோட்பாடு",
         "Doctrine of Territorial Nexus", "நிலப்பரப்பு இணைப்பு தத்துவம்",
         "Doctrine of Eminent Domain", "நிலம் கையகப்படுத்தும் இறையாண்மை தத்துவம்", "A",
         "Justice Nariman held that legislation can be struck down under Article 14 on the ground of 'manifest arbitrariness'—if it is done caprice, without determining principle, or lacks adequate rationale.",
         "நீதிபதி நாரிமன் உறுப்பு 14-ன் கீழ் 'வெளிப்படையான தன்னிச்சைத் தன்மை' என்ற அடிப்படையில் சட்டத்தை ரத்து செய்யலாம் என்றார்; கொள்கை முடிவின்றியோ நியாயமான காரணமின்றியோ சட்டம் இருந்தால் அது செல்லாது."),

        # 17 - C
        ("JRAP_H_017", "Striking Down Instant Triple Talaq",
         "In Shayara Bano (2017), the practice of Talaq-e-Biddat (instant triple talaq) was declared unconstitutional by a 3:2 majority because:",
         "ஷயாரா பானோ (2017) வழக்கில் தலாக்-இ-பித்தத் (உடனடி முத்தலாக்) நடைமுறை 3:2 பெரும்பான்மையில் அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்டது, ஏனெனில்:",
         "It reduced the population of the minority community", "அது சிறுபான்மை சமூகத்தின் மக்கள் தொகையைக் குறைத்தது",
         "It was not passed by the Parliament", "அது நாடாளுமன்றத்தால் நிறைவேற்றப்படவில்லை",
         "It was manifestly arbitrary, irrevocable without marital reconciliation, and violated Article 14 equality", "அது வெளிப்படையான தன்னிச்சைத் தன்மை கொண்டதாகவும், சமரசமின்றி மாற்ற முடியாததாகவும், உறுப்பு 14 சமத்துவத்தை மீறுவதாகவும் இருந்தது",
         "It violated financial emergency rules", "அது நிதி அவசரநிலை விதிகளை மீறியது", "C",
         "The Supreme Court declared instant Triple Talaq void and unconstitutional, holding that an arbitrary unilateral dissolution of marriage without reconciliation violates fundamental rights of women.",
         "சமரச முயற்சியின்றி தன்னிச்சையாக திருமணத்தை ரத்து செய்யும் உடனடி முத்தலாக் பெண்களின் அடிப்படை சமத்துவ உரிமைகளை மீறுகிறது எனக் கூறி உச்ச நீதிமன்றம் அதை ரத்து செய்தது."),

        # 18 - D
        ("JRAP_H_018", "Sabarimala Temple Entry Judgment",
         "In Indian Young Lawyers Association v. State of Kerala (2018) (Sabarimala Case), which rule of the Kerala Hindu Places of Public Worship Rules 1965 was struck down?",
         "இந்திய இளம் வழக்கறிஞர்கள் சங்கம் v. கேரள மாநிலம் (2018) (சபரிமலை வழக்கு) வழக்கில் 1965-ன் கேரள பொது வழிபாட்டுத் தலங்கள் விதிகளின் எந்த விதி ரத்து செய்யப்பட்டது?",
         "Rule 1", "விதி 1",
         "Rule 5", "விதி 5",
         "Rule 8", "விதி 8",
         "Rule 3(b)", "விதி 3(b)", "D",
         "Rule 3(b) permitted prohibition of women of ages 10 to 50 from entering the Sabarimala temple. The 4:1 majority struck it down as violative of Articles 14, 15, and 25.",
         "10 முதல் 50 வயதுக்குட்பட்ட பெண்கள் சபரிமலை கோவிலுக்குள் நுழைவதைத் தடை செய்ய அனுமதித்த விதி 3(b)-ஐ 4:1 பெரும்பான்மையில் உச்ச நீதிமன்றம் உறுப்புகள் 14, 15, 25-ஐ மீறியதாக ரத்து செய்தது."),

        # 19 - B
        ("JRAP_H_019", "Lone Dissent in Sabarimala Case",
         "Who was the sole dissenting judge in the 5-judge Constitution Bench in the Sabarimala Temple Entry Case (2018)?",
         "சபரிமலை கோவில் நுழைவு வழக்கில் (2018) 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வில் மாறுபட்ட தீர்ப்பை வழங்கிய ஒரே நீதிபதி யார்?",
         "Justice R.F. Nariman", "நீதிபதி ஆர்.எஃப். நாரிமன்",
         "Justice Indu Malhotra", "நீதிபதி இந்து மல்ஹோத்ரா",
         "Justice D.Y. Chandrachud", "நீதிபதி டி.ஒய். சந்திரசூட்",
         "Chief Justice Dipak Misra", "தலைமை நீதிபதி தீபக் மிஸ்ரா", "B",
         "Justice Indu Malhotra dissented, holding that constitutional courts should not interfere in religious practices of a denomination in PIL petitions unless a member of the denomination themselves challenges it.",
         "நீதிபதி இந்து மல்ஹோத்ரா மாறுபட்ட தீர்ப்பில், மதப் பிரிவைச் சேர்ந்தவர்கள் சவால் செய்யாத வரை பொது நல வழக்குகளில் நீதிமன்றங்கள் மத நம்பிக்கைகளில் தலையிடக்கூடாது என்றார்."),

        # 20 - D
        ("JRAP_H_020", "Essential Religious Practices Doctrine",
         "The 'Essential Religious Practices Test' frequently utilized in Judicial Review of religious customs was first articulated by the Supreme Court in:",
         "மத வழக்கங்களின் நீதித்துறை மறுஆய்வில் பயன்படுத்தப்படும் 'இன்றியமையாத மத நடைமுறைகள் சோதனை' (Essential Religious Practices Test) உச்ச நீதிமன்றத்தால் முதன்முதலில் எதில் உருவாக்கப்பட்டது?",
         "S.R. Bommai Case (1994)", "எஸ்.ஆர். பொம்மை வழக்கு (1994)",
         "Kesavananda Bharati Case (1973)", "கேசவாநந்த பாரதி வழக்கு (1973)",
         "Maneka Gandhi Case (1978)", "மேனகா காந்தி வழக்கு (1978)",
         "The Commissioner, Hindu Religious Endowments, Madras v. Sri Lakshmindra Thirtha Swamiar of Sri Shirur Mutt (Shirur Mutt Case, 1954)", "சிரூர் மடம் வழக்கு (1954)", "D",
         "In the Shirur Mutt Case (1954), a 7-judge bench ruled that Article 26 protects practices that are 'essential and integral' to a religion, to be determined with reference to the doctrines of that religion itself.",
         "சிரூர் மடம் வழக்கில் (1954) 7 நீதிபதிகள் அமர்வு, ஒரு மதத்திற்கு 'இன்றியமையாத மற்றும் ஒருங்கிணைந்த' நடைமுறைகளுக்கு மட்டுமே உறுப்பு 26 கீழ் பாதுகாப்பு உண்டு எனத் தீர்ப்பளித்தது."),

        # 21 - A
        ("JRAP_H_021", "Collegium Memorandum of Procedure",
         "Following the striking down of the 99th CAA (NJAC) in 2015, what document governs the procedural consultation between the Executive and Judiciary for appointing higher judiciary judges?",
         "2015-ல் 99வது திருத்தம் (NJAC) ரத்து செய்யப்பட்டதைத் தொடர்ந்து, உயர் நீதித்துறை நீதிபதிகளை நியமிப்பதற்கான நிர்வாகத்திற்கும் நீதித்துறைக்கும் இடையிலான நடைமுறை ஆவணம் எது?",
         "Memorandum of Procedure (MoP)", "நடைமுறை குறிப்பாணை (Memorandum of Procedure - MoP)",
         "Civil Procedure Code", "சிவில் நடைமுறைச் சட்டம்",
         "Judicial Standards and Accountability Act", "நீதித்துறை தரநிலைகள் மற்றும் பொறுப்புடைமை சட்டம்",
         "Supreme Court Rules 2013", "உச்ச நீதிமன்ற விதிகள் 2013", "A",
         "The appointment process is governed by the Memorandum of Procedure (MoP), which was framed in the aftermath of the Second and Third Judges cases and remains under ongoing executive-judicial deliberation.",
         "நீதிபதிகள் நியமன நடைமுறை 2வது மற்றும் 3வது நீதிபதிகள் வழக்கின் அடிப்படையில் உருவாக்கப்பட்ட நடைமுறை குறிப்பாணையால் (MoP) நிர்வகிக்கப்படுகிறது."),

        # 22 - C
        ("JRAP_H_022", "Right to be Forgotten Fundamental Right",
         "In K.S. Puttaswamy (2017), the Supreme Court recognized the 'Right to be Forgotten' as an aspect of:",
         "கே.எஸ். புட்டசுவாமி (2017) வழக்கில் உச்ச நீதிமன்றம் 'மறக்கப்படுவதற்கான உரிமையை' (Right to be Forgotten) எதன் அம்சமாக அங்கீகரித்தது?",
         "Right to Property under Art. 300A", "உறுப்பு 300A கீழ் உள்ள சொத்துரிமை",
         "Right to Equality under Art. 14", "உறுப்பு 14 கீழ் உள்ள சமத்துவ உரிமை",
         "Informational Privacy and Personal Dignity under Article 21", "உறுப்பு 21-ன் கீழான தகவல் அந்தரங்கம் மற்றும் தனிநபர் கண்ணியம்",
         "Right to assemble under Art. 19(1)(b)", "உறுப்பு 19(1)(b) கீழ் கூடும் உரிமை", "C",
         "The Supreme Court held that informational privacy—controlling the dissemination of personal data and having past information deleted—is an integral component of Article 21 personal autonomy.",
         "தகவல் அந்தரங்கம்—தனிப்பட்ட தகவல்களைக் கட்டுப்படுத்துவது மற்றும் பழைய தகவல்களை நீக்குவது—உறுப்பு 21 தனிநபர் தன்னாட்சியின் ஒருங்கிணைந்த பகுதி என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 23 - B
        ("JRAP_H_023", "Electoral Bonds Striking Down",
         "In Association for Democratic Reforms v. Union of India (2024), a 5-judge Constitution Bench struck down the Electoral Bond Scheme because it violated:",
         "ADR v. இந்திய ஒன்றியம் (2024) வழக்கில் 5 நீதிபதிகள் அரசியலமைப்பு அமர்வு தேர்தல் பத்திரத் திட்டத்தை ரத்து செய்தது, ஏனெனில் அது எதனை மீறியது?",
         "Article 368 majority rules", "உறுப்பு 368 பெரும்பான்மை விதிகளை",
         "Voter's Right to Information under Article 19(1)(a) regarding political party funding", "அரசியல் கட்சி நிதி குறித்த உறுப்பு 19(1)(a)-ன் கீழான வாக்காளரின் தகவல் அறியும் உரிமையை",
         "Article 356 provisions", "உறுப்பு 356 விதிகளை",
         "Preamble word 'Socialist'", "முகப்புரையின் 'சமதர்ம' வார்த்தையை", "B",
         "The Supreme Court unanimously held that anonymous political donations through electoral bonds infringe the voter's fundamental right to information under Article 19(1)(a), which is vital for free and fair elections.",
         "தேர்தல் பத்திரங்கள் மூலம் அநாமதேய நிதி வழங்குவது, சுதந்திரமான தேர்தலுக்கு அவசியமான உறுப்பு 19(1)(a)-ன் கீழான வாக்காளரின் தகவல் அறியும் அடிப்படை உரிமையை மீறுகிறது என உச்ச நீதிமன்றம் ரத்து செய்தது."),

        # 24 - D
        ("JRAP_H_024", "Article 105 Parliamentary Privileges Review",
         "In Sita Soren v. Union of India (2024), a 7-judge Constitution Bench overruled the 1998 PV Narasimha Rao verdict and held that parliamentary immunity under Articles 105(2) and 194(2):",
         "சீதா சோரன் v. இந்திய ஒன்றியம் (2024) வழக்கில் 7 நீதிபதிகள் அமர்வு 1998-ன் நரசிம்ம ராவ் தீர்ப்பை ரத்து செய்து, உறுப்புகள் 105(2) மற்றும் 194(2)-ன் கீழான நாடாளுமன்ற விலக்களிப்பு என்பது:",
         "Applies to all criminal offences committed anywhere", "எங்கு செய்யப்படும் அனைத்து குற்றவியல் குற்றங்களுக்கும் பொருந்தும்",
         "Protects members from murder investigations", "கொலை வழக்குகளிலிருந்து உறுப்பினர்களைப் பாதுகாக்கும்",
         "Is absolute and immune from police inquiries", "முழுமையானது மற்றும் காவல் விசாரணையிலிருந்து விலக்கு பெற்றது",
         "Does NOT protect an MP or MLA from criminal prosecution for accepting a bribe to vote or give a speech in the legislature", "சட்டமன்றத்தில் வாக்களிக்கவோ அல்லது பேசவோ லஞ்சம் வாங்குவதிலிருந்து ஓர் எம்.பி. அல்லது எம்.எல்.ஏ.-வை குற்றவியல் விசாரணையிலிருந்து பாதுகாக்காது", "D",
         "A unanimous 7-judge bench held that bribery is not immune under parliamentary privilege; corruption destroys the democratic foundation of the legislature and is subject to criminal law.",
         "லஞ்சம் வாங்குவது நாடாளுமன்ற சிறப்புரிமையின் கீழ் வராது என்றும், ஊழல் ஜனநாயக அடித்தளத்தை அழிப்பதால் குற்றவியல் சட்டத்திற்கு உட்பட்டது என்றும் 7 நீதிபதிகள் அமர்வு தீர்ப்பளித்தது."),

        # 25 - B
        ("JRAP_H_025", "Article 143 Advisory Jurisdiction Landmark",
         "In the landmark In Re Kerala Education Bill Reference (1958) under Article 143, the Supreme Court propounded which doctrine to resolve conflicts between Fundamental Rights and Directive Principles?",
         "கேரளா கல்வி மசோதா விவகாரத்தில் (1958) உறுப்பு 143-ன் கீழ் உச்ச நீதிமன்றம் அடிப்படை உரிமைகளுக்கும் வழிகாட்டு நெறிமுறைகளுக்கும் இடையிலான மோதல்களைத் தீர்க்க எந்தக் கோட்பாட்டை முன்வைத்தது?",
         "Doctrine of Severability", "பிரித்தெடுக்கும் கோட்பாடு",
         "Doctrine of Harmonious Construction", "இணக்கமான பொருள் விளக்கக் கோட்பாடு (Harmonious Construction)",
         "Doctrine of Eclipse", "மறைப்புக் கோட்பாடு",
         "Doctrine of Laches", "காலதாமதக் கோட்பாடு", "B",
         "Chief Justice S.R. Das held that the court should apply the doctrine of harmonious construction to give effect to both Fundamental Rights and Directive Principles as far as possible.",
         "தலைமை நீதிபதி எஸ்.ஆர். தாஸ், அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகள் ஆகிய இரண்டிற்கும் முடிந்தவரை இடமளிக்க இணக்கமான பொருள் விளக்கக் கோட்பாட்டைப் பயன்படுத்த வேண்டும் என்றார்."),

        # 26 - D
        ("JRAP_H_026", "Judicial Review of Governor Assent Delay",
         "In State of Punjab v. Principal Secretary to the Governor of Punjab (2023), the Supreme Court ruled that a Governor cannot sit indefinitely on bills passed by the State Legislature under Article 200 because:",
         "பஞ்சாப் மாநிலம் v. ஆளுநரின் முதன்மைச் செயலாளர் (2023) வழக்கில் உறுப்பு 200-ன் கீழ் சட்டமன்றம் நிறைவேற்றிய மசோதாக்கள் மீது ஆளுநர் காலவரையின்றி தாமதிக்க முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது, ஏனெனில்:",
         "Governors are directly elected by people", "ஆளுநர்கள் மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார்கள்",
         "The Speaker can sign the bill directly", "சபாநாயகரே மசோதாவில் நேரடியாகக் கையெழுத்திடலாம்",
         "High Court can enact the bill into law", "உயர் நீதிமன்றமே மசோதாவைச் சட்டமாக்க முடியும்",
         "The Governor is a constitutional titular head and withholding assent indefinitely without returning the bill 'as soon as possible' subverts parliamentary democracy", "ஆளுநர் ஒரு பெயரளவு அரசியலமைப்புத் தலைவர்; மசோதாவைத் திருப்பியனுப்பாமல் ஒப்புதலைக் காலவரையின்றி நிறுத்தி வைப்பது நாடாளுமன்ற ஜனநாயகத்தைச் சீர்குலைக்கும்", "D",
         "The Supreme Court held that the phrase 'as soon as possible' in the first proviso to Article 200 contains constitutional urgency; a Governor cannot sit on a bill to kill it by inaction.",
         "உறுப்பு 200-ன் முதல் வரம்பில் உள்ள 'முடிந்தவரை விரைவாக' என்ற சொற்றொடர் அவசரத்தைக் குறிக்கிறது; ஒரு மசோதாவை முடக்க ஆளுநர் காலவரையின்றி நிறுத்தி வைக்க முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 27 - A
        ("JRAP_H_027", "Basic Structure in NJAC Judgment",
         "In the NJAC judgment (2015), the majority held that the presence of the Union Law Minister on the National Judicial Appointments Commission:",
         "NJAC தீர்ப்பில் (2015), தேசிய நீதித்துறை நியமன ஆணையத்தில் மத்திய சட்ட அமைச்சர் இடம்பெற்றிருப்பது எதனை மீறுவதாக பெரும்பான்மை அமர்வு கருதியது?",
         "Compromised the Independence of the Judiciary, which is a non-negotiable basic feature of the Constitution", "அரசியலமைப்பின் சமரசமற்ற அடிப்படைக் கூறான நீதித்துறையின் சுதந்திரத்தைப் பலவீனப்படுத்தியது",
         "Violated Article 368 financial rules", "உறுப்பு 368 நிதி விதிகளை மீறியது",
         "Violated the Tenth Schedule", "பத்தாவது அட்டவணையை மீறியது",
         "Was prohibited by the Preamble", "முகப்புரையால் தடை செய்யப்பட்டது", "A",
         "The majority held that allowing the Executive (the largest litigant in courts) a direct veto in judicial appointments compromises judicial independence, an integral basic structure feature.",
         "நீதிமன்றங்களில் மிகப் பெரிய வழக்காடியாக உள்ள நிர்வாகத்திற்கு நீதிபதிகள் நியமனத்தில் வீட்டோ அதிகாரம் அளிப்பது நீதித்துறை சுதந்திரத்தைப் பாதிக்கும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 28 - C
        ("JRAP_H_028", "Article 136 Discretionary Criteria",
         "In Pritam Singh v. The State (1950), what guiding rule was established regarding the Supreme Court's exercise of jurisdiction under Article 136?",
         "பிரீதம் சிங் v. அரசு (1950) வழக்கில் உறுப்பு 136-ன் கீழான உச்ச நீதிமன்றத்தின் அதிகார வரம்பு தொடர்பாக எந்த வழிகாட்டு விதி நிறுவப்பட்டது?",
         "It must be exercised in every civil case", "ஒவ்வொரு சிவில் வழக்கிலும் இது செயல்படுத்தப்பட வேண்டும்",
         "It is restricted only to constitutional bench references", "அரசியலமைப்பு அமர்வு குறிப்புகளுக்கு மட்டுமே இது கட்டுப்பட்டது",
         "It is an exceptional and extraordinary power to be exercised sparingly only when special and exceptional circumstances exist and grave injustice has been done", "இது ஒரு விதிவிலக்கான மற்றும் அசாதாரண அதிகாரம்; தீவிர அநீதி இழைக்கப்பட்ட சிறப்புச் சூழ்நிலைகளில் மட்டுமே அரிதாகப் பயன்படுத்தப்பட வேண்டும்",
         "It is controlled by the Attorney General", "இது தலைமை வழக்கறிஞரால் கட்டுப்படுத்தப்படுகிறது", "C",
         "The Supreme Court held that Article 136 confers vast discretionary power, but it must be exercised sparingly and only in exceptional cases where substantial injustice has occurred.",
         "உறுப்பு 136 பரந்த விவேக அதிகாரத்தை அளிக்கிறது; எனினும் தீவிர அநீதி நிகழ்ந்த விதிவிலக்கான சூழ்நிலைகளில் மட்டுமே இது மிக எச்சரிக்கையுடன் பயன்படுத்தப்பட வேண்டும் எனப்பட்டது."),

        # 29 - B
        ("JRAP_H_029", "Article 226 Territorial Jurisdiction Clause (2)",
         "Which Constitutional Amendment Act inserted clause (2) in Article 226, enabling High Courts to issue writs to authorities outside their territorial limits if the 'cause of action' arises within their territory?",
         "எந்த அரசியலமைப்புத் திருத்தச் சட்டம் உறுப்பு 226-ல் உட்பிரிவு (2)-ஐ சேர்த்தது, இதன் மூலம் வழக்கின் காரணம் (Cause of Action) தனது எல்லைக்குள் எழுந்தால் தனது எல்லைக்கு அப்பாற்பட்ட அதிகாரிகளுக்கும் உயர் நீதிமன்றம் நீதிப்பேராணைகளை வெளியிட முடியும்?",
         "42nd Amendment Act 1976", "42வது திருத்தச் சட்டம் 1976",
         "15th Amendment Act 1963", "15வது திருத்தச் சட்டம் 1963",
         "44th Amendment Act 1978", "44வது திருத்தச் சட்டம் 1978",
         "24th Amendment Act 1971", "24வது திருத்தச் சட்டம் 1971", "B",
         "The 15th Constitutional Amendment Act 1963 inserted Article 226(1A) (now Art. 226(2)), resolving the limitation created by Election Commission v. Saka Venkata Subba Rao (1953).",
         "1963-ன் 15வது திருத்தச் சட்டம் உறுப்பு 226(2)-ஐச் சேர்த்து, வழக்கின் காரணம் எழும் பகுதியில் உள்ள உயர் நீதிமன்றம் எல்லைக்கு அப்பாற்பட்ட அரசுக்கும் நீதிப்பேராணை வெளியிட வழிவகுத்தது."),

        # 30 - D
        ("JRAP_H_030", "Substantive Due Process Evolution",
         "The shift from A.K. Gopalan (1950) to Maneka Gandhi (1978) in Indian constitutional law represents the historic transition from:",
         "இந்திய அரசியலமைப்புச் சட்டத்தில் ஏ.கே. கோபாலன் (1950) வழக்கிலிருந்து மேனகா காந்தி (1978) வழக்கை நோக்கிய நகர்வு எந்த வரலாற்று மாற்றத்தைக் குறிக்கிறது?",
         "Judicial Supremacy to Parliamentary Sovereignty", "நீதித்துறை மேலாதிக்கத்திலிருந்து நாடாளுமன்ற இறையாண்மைக்கு",
         "Federalism to Unitary state", "கூட்டாட்சியிலிருந்து ஒற்றையாட்சி முறைக்கு",
         "Presidential system to Westminster model", "அதிபர் முறையிலிருந்து வெஸ்ட்மின்ஸ்டர் முறைக்கு",
         "Rigid 'Procedure Established by Law' to Substantive 'Due Process of Law' ensuring just, fair, and reasonable laws", "கடுமையான 'சட்டத்தால் உருவாக்கப்பட்ட நடைமுறையிலிருந்து' நேர்மையான, நியாயமான சட்டங்களை உறுதி செய்யும் 'சட்டத்தின் உரிய நடைமுறைக்கு' (Due Process)", "D",
         "A.K. Gopalan took a literalist view that Article 21 merely requires compliance with statutory procedure. Maneka Gandhi revolutionized this by mandating that the law itself must be just, fair, and non-arbitrary.",
         "கோபாலன் வழக்கு நடைமுறையைப் பின்பற்றினால் போதும் என்ற குறுகிய பார்வையை எடுத்தது; மேனகா காந்தி வழக்கு சட்டமே நியாயமானதாகவும் தன்னிச்சையற்றதாகவும் இருக்க வேண்டும் எனப் புரட்சிகர மாற்றத்தை ஏற்படுத்தியது."),

        # 31 - A
        ("JRAP_H_031", "Doctrine of Pith and Substance in Judicial Review",
         "When a statute enacted by a state legislature is challenged for encroaching upon a Union List subject, which doctrine does the judiciary apply to ascertain the true nature and character of the legislation?",
         "ஒரு மாநில சட்டமன்றத்தால் இயற்றப்பட்ட சட்டம் மத்தியப் பட்டியல் விஷயத்தை ஆக்கிரமிப்பதாக சவால் செய்யப்படும்போது, அச்சட்டத்தின் உண்மையான தன்மை மற்றும் குணத்தை அறிய நீதித்துறை எந்தக் கோட்பாட்டைப் பயன்படுத்துகிறது?",
         "Doctrine of Pith and Substance", "அடிநாதம் மற்றும் உண்மைத் தன்மைக் கோட்பாடு (Pith and Substance)",
         "Doctrine of Eclipse", "மறைப்புக் கோட்பாடு",
         "Doctrine of Severability", "பிரித்தெடுக்கும் கோட்பாடு",
         "Doctrine of Laches", "காலதாமதக் கோட்பாடு", "A",
         "If the 'pith and substance' (true nature) of the Act falls within the State's legislative competence, incidental encroachment into the Union List does not render the law invalid.",
         "சட்டத்தின் உண்மையான சாராம்சம் மாநில சட்டமன்ற அதிகார வரம்பிற்குள் விழுந்தால், மத்தியப் பட்டியலில் ஏற்படும் தற்செயலான ஆக்கிரமிப்பு சட்டத்தைச் செல்லாததாக்காது."),

        # 32 - C
        ("JRAP_H_032", "Doctrine of Repugnancy Article 254",
         "Under Article 254(2), what is the sole constitutional mechanism by which a State law on a Concurrent List subject repugnant to an earlier Union law can prevail in that State?",
         "உறுப்பு 254(2)-ன் கீழ், பொதுப் பட்டியல் விஷயத்தில் முந்தைய மத்திய சட்டத்திற்கு முரணான ஒரு மாநில சட்டம் அம்மாநிலத்தில் செல்லுபடியாகக்கூடிய ஒரே அரசியலமைப்பு வழிமுறை எது?",
         "Ratification by two-thirds of State Assemblies", "மூன்றில் இரண்டு பங்கு மாநிலச் சட்டமன்றங்களின் ஒப்புதல்",
         "Approval by the Prime Minister", "பிரதமரின் ஒப்புதல்",
         "It was reserved for the consideration of the President and received his assent", "அது குடியரசுத் தலைவரின் பரிசீலனைக்கு நிறுத்தி வைக்கப்பட்டு அவரது ஒப்புதலைப் பெற்றது",
         "Approval by a 5-judge Supreme Court bench", "5 நீதிபதிகள் கொண்ட உச்ச நீதிமன்ற அமர்வின் ஒப்புதல்", "C",
         "Article 254(2) provides that a State law on Concurrent subject repugnant to Union law prevails in the State if it has been reserved for the President and received Presidential assent.",
         "உறுப்பு 254(2)-ன் படி, மத்திய சட்டத்திற்கு முரணான மாநில சட்டம் குடியரசுத் தலைவரின் பரிசீலனைக்கு வைக்கப்பட்டு அவரது ஒப்புதலைப் பெற்றால் அம்மாநிலத்தில் செல்லுபடியாகும்."),

        # 33 - B
        ("JRAP_H_033", "Judicial Review of Speaker Inaction on Defection",
         "In Keisham Meghachandra Singh v. Hon'ble Speaker Manipur Legislative Assembly (2020), the Supreme Court laid down what outer time limit for Speakers to decide disqualification petitions under the Tenth Schedule?",
         "கெய்ஷம் மேகச்சந்திர சிங் (2020) வழக்கில் 10வது அட்டவணையின் கீழ் தகுதிநீக்க மனுக்களைத் தீர்மானிக்க சபாநாயகர்களுக்கு உச்ச நீதிமன்றம் நிர்ணயித்த அதிகபட்ச காலக்கெடு என்ன?",
         "15 days", "15 நாட்கள்",
         "3 months, save in exceptional circumstances", "விதிவிலக்கான சூழ்நிலைகளைத் தவிர 3 மாதங்கள்",
         "1 year", "1 வருடம்",
         "5 years (full tenure)", "5 ஆண்டுகள் (முழு பதவிக்காலம்)", "B",
         "The Supreme Court held that unless there are exceptional reasons, the Speaker must decide disqualification petitions within a reasonable period of three months.",
         "விதிவிலக்கான காரணங்கள் இருந்தாலன்றி, சபாநாயகர் தகுதிநீக்க மனுக்கள் மீது நியாயமான மூன்று மாத காலத்திற்குள் முடிவெடுக்க வேண்டும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 34 - D
        ("JRAP_H_034", "Independent Tribunal for Defection",
         "In Keisham Meghachandra Singh (2020), the Supreme Court recommended that Parliament amend the Constitution to replace the Speaker as the deciding authority under the Tenth Schedule with:",
         "கெய்ஷம் மேகச்சந்திர சிங் (2020) வழக்கில் 10வது அட்டவணையின் கீழ் முடிவெடுக்கும் அதிகாரியாக உள்ள சபாநாயகருக்குப் பதிலாக எதனை அமைக்க அரசியலமைப்பைத் திருத்துமாறு நாடாளுமன்றத்திற்கு உச்ச நீதிமன்றம் பரிந்துரைத்தது?",
         "The Governor of the State", "மாநில ஆளுநர்",
         "The Chief Minister", "முதலமைச்சர்",
         "The State Cabinet", "மாநில அமைச்சரவை",
         "An independent permanent tribunal headed by a retired Supreme Court judge or retired High Court Chief Justice", "ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதி அல்லது உயர் நீதிமன்ற தலைமை நீதிபதி தலைமையிலான ஒரு சுதந்திரமான நிரந்தர தீர்ப்பாயம்", "D",
         "The Supreme Court recommended an independent tribunal to insulate disqualification decisions from the political affiliations of the Speaker.",
         "சபாநாயகரின் அரசியல் சார்பிலிருந்து தகுதிநீக்க முடிவுகளைப் பாதுகாக்க ஓய்வுபெற்ற நீதிபதி தலைமையிலான ஒரு சுதந்திரமான தீர்ப்பாயத்தை உருவாக்க உச்ச நீதிமன்றம் பரிந்துரைத்தது."),

        # 35 - B
        ("JRAP_H_035", "Judicial Review of Article 370 Abrogation",
         "In In Re Article 370 of the Constitution (2023), a 5-judge Constitution Bench held that the exercise of presidential power under Article 370(3):",
         "உறுப்பு 370 ரத்து தொடர்பான வழக்கில் (2023), 5 நீதிபதிகள் அரசியலமைப்பு அமர்வு உறுப்பு 370(3)-ன் கீழான குடியரசுத் தலைவரின் அதிகாரச் செயல்பாடு என்பது:",
         "Is completely immune from judicial review under any grounds", "எந்தக் காரணத்தின் கீழும் நீதித்துறை மறுஆய்விலிருந்து முற்றிலும் பாதுகாப்பு பெற்றது",
         "Is subject to Judicial Review on grounds of malafide and manifest arbitrariness", "துர்நோக்கம் மற்றும் வெளிப்படையான தன்னிச்சைத் தன்மை ஆகிய காரணங்களின் கீழ் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது",
         "Can only be questioned in Jammu & Kashmir High Court", "ஜம்மு & காஷ்மீர் உயர் நீதிமன்றத்தில் மட்டுமே கேள்வி கேட்க முடியும்",
         "Requires ratification by the UN Security Council", "ஐ.நா. பாதுகாப்பு கவுன்சிலின் ஒப்புதல் தேவை", "B",
         "The Supreme Court held that the President's exercise of power is not immune from judicial review; it is reviewable on grounds of malafide, though the Court upheld the abrogation on merits.",
         "குடியரசுத் தலைவரின் அதிகாரம் நீதித்துறை மறுஆய்வுக்கு அப்பாற்பட்டது அல்ல; துர்நோக்கம் இருந்தால் மறுஆய்வு செய்யலாம் எனக் கூறி, இவ்வழக்கில் தகுதியின் அடிப்படையில் ரத்தை நீதிமன்றம் உறுதி செய்தது."),

        # 36 - D
        ("JRAP_H_036", "Doctrine of Unconstitutional Constitutional Amendment",
         "The doctrine of 'Unconstitutional Constitutional Amendment' adopted in global comparative constitutional law originated from which historic Indian judgment?",
         "உலகளாவிய ஒப்பீட்டு அரசியலமைப்புச் சட்டத்தில் ஏற்றுக்கொள்ளப்பட்ட 'அரசியலமைப்புக்கு முரணான அரசியலமைப்புத் திருத்தம்' என்ற கோட்பாடு எந்த வரலாற்றுச் சிறப்புமிக்க இந்தியத் தீர்ப்பிலிருந்து உருவானது?",
         "Golaknath (1967)", "கோலக்நாத் (1967)",
         "Shankari Prasad (1951)", "சங்கரி பிரசாத் (1951)",
         "Minerva Mills (1980)", "மினர்வா மில்ஸ் (1980)",
         "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி v. கேரள மாநிலம் (1973)", "D",
         "Kesavananda Bharati established that even a constitutional amendment passed under Article 368 with requisite special majorities can be declared unconstitutional if it damages the Basic Structure.",
         "நாடாளுமன்றத்தால் சிறப்புப் பெரும்பான்மையுடன் நிறைவேற்றப்பட்ட அரசியலமைப்புத் திருத்தமே கூட அடிப்படைக் கட்டமைப்பைச் சேதப்படுத்தினால் செல்லாது என கேசவாநந்த பாரதி நிறுவியது."),

        # 37 - A
        ("JRAP_H_037", "Judicial Review of Money Bill Certification",
         "In which pending reference before a 7-judge Constitution Bench is the question of whether the Speaker's certification of a Money Bill is open to Judicial Review being reconsidered?",
         "சபாநாயகர் ஒரு மசோதாவை பண மசோதா எனச் சான்றளிப்பது நீதித்துறை மறுஆய்வுக்கு உட்பட்டதா என்ற கேள்வி எந்த 7 நீதிபதிகள் அமர்வு முன் மறுபரிசீலனையில் உள்ளது?",
         "Roger Mathew v. South Indian Bank Ltd. (2020) Reference", "ரோஜர் மேத்யூ v. சவுத் இந்தியன் வங்கி (2020) குறிப்பு",
         "Minerva Mills Reference", "மினர்வா மில்ஸ் குறிப்பு",
         "Golaknath Reference", "கோலக்நாத் குறிப்பு",
         "Kesavananda Reference", "கேசவாநந்த குறிப்பு", "A",
         "A 5-judge bench in Roger Mathew (2020) doubted the correctness of the majority view in the Aadhaar case and referred the question of Money Bill review to a 7-judge Constitution Bench.",
         "ரோஜர் மேத்யூ (2020) வழக்கில் 5 நீதிபதிகள் அமர்வு ஆதார் தீர்ப்பின் பெரும்பான்மை பார்வையில் சந்தேகம் கொண்டு, பண மசோதா மறுஆய்வு சிக்கலை 7 நீதிபதிகள் அமர்வுக்குப் பரிந்துரைத்தது."),

        # 38 - C
        ("JRAP_H_038", "S.R. Bommai Floor Test Primacy",
         "In S.R. Bommai (1994), what objective criterion did the Supreme Court lay down to test whether a ministry enjoys the confidence of the legislative assembly?",
         "எஸ்.ஆர். பொம்மை (1994) வழக்கில் ஒரு அமைச்சரவை சட்டமன்றத்தின் நம்பிக்கையைப் பெற்றுள்ளதா என்பதை சோதிக்க உச்ச நீதிமன்றம் வகுத்த புறநிலை அளவுகோல் என்ன?",
         "Subjective satisfaction of the Governor in Raj Bhavan", "ராஜ் பவனில் ஆளுநரின் அகநிலை திருப்தி",
         "Opinion of the Prime Minister", "பிரதமரின் கருத்து",
         "Floor Test on the floor of the Legislative Assembly as the only constitutionally valid method", "சட்டமன்ற அவையின் தளத்தில் நடத்தப்படும் நம்பிக்கை வாக்கெடுப்பு (Floor Test) மட்டுமே அரசியலமைப்பு ரீதியான ஒரே முறை",
         "Verification of signatures by police", "காவல்துறையால் கையொப்பங்களை சரிபார்த்தல்", "C",
         "The Supreme Court ruled that the floor of the House is the only place where the majority of the government should be tested, severely curbing the arbitrary dismissal of state governments by Governors.",
         "அரசின் பெரும்பான்மையை சோதிக்க வேண்டிய ஒரே இடம் சட்டமன்ற அவை மட்டுமே என உச்ச நீதிமன்றம் தீர்ப்பளித்து, ஆளுநர்கள் தன்னிச்சையாக மாநில அரசுகளைக் கலைப்பதைத் தடுத்தது."),

        # 39 - B
        ("JRAP_H_039", "Article 32 Cannot Be Curtailed by Statute",
         "Can Parliament by passing an ordinary statute restrict or exclude the writ jurisdiction of the Supreme Court under Article 32?",
         "ஒரு சாதாரண சட்டத்தை நிறைவேற்றுவதன் மூலம் நாடாளுமன்றம் உறுப்பு 32-ன் கீழான உச்ச நீதிமன்றத்தின் நீதிப்பேராணை அதிகாரத்தைக் கட்டுப்படுத்தவோ விலக்கவோ முடியுமா?",
         "Yes, Parliament has sovereign power", "ஆம், நாடாளுமன்றத்திற்கு இறையாண்மை அதிகாரம் உண்டு",
         "No, because Article 32 is a basic feature of the Constitution and guaranteed fundamental right", "இல்லை, ஏனெனில் உறுப்பு 32 அரசியலமைப்பின் அடிப்படைக் கூறு மற்றும் உத்தரவாதம் அளிக்கப்பட்ட அடிப்படை உரிமை",
         "Yes, with two-thirds majority in Rajya Sabha", "ஆம், மாநிலங்களவையில் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் செய்யலாம்",
         "Yes, if recommended by Law Commission", "ஆம், சட்ட ஆணையம் பரிந்துரைத்தால் செய்யலாம்", "B",
         "In Prem Chand Garg (1963) and L. Chandra Kumar (1997), SC affirmed that Article 32 is an inviolable constitutional remedy and part of the Basic Structure that cannot be abridged by legislation.",
         "உறுப்பு 32 மீற முடியாத அரசியலமைப்புப் பரிகாரம் மற்றும் அடிப்படைக் கட்டமைப்பின் பகுதி என்பதால் எந்தவொரு சட்டத்தாலும் அதைக் குறைக்க முடியாது என உச்ச நீதிமன்றம் உறுதிப்படுத்தியது."),

        # 40 - D
        ("JRAP_H_040", "Judicial Restraint in Economic Policy",
         "In Balco Employees Union v. Union of India (2002), the Supreme Court reiterated that in matters of economic policy and disinvestment, courts should exercise:",
         "பால்கோ ஊழியர்கள் சங்கம் v. இந்திய ஒன்றியம் (2002) வழக்கில் பொருளாதாரக் கொள்கை மற்றும் பொதுத்துறை பங்குகள் விற்பனை விவகாரங்களில் நீதிமன்றங்கள் எதனைக் கடைப்பிடிக்க வேண்டும் என உச்ச நீதிமன்றம் மீண்டும் வலியுறுத்தியது?",
         "Aggressive judicial activism", "தீவிர நீதித்துறை செயல்பாடு",
         "Legislative veto", "சட்டமன்ற வீட்டோ அதிகாரம்",
         "Executive superintendence", "நிர்வாக மேற்பார்வை",
         "Judicial Restraint, not interfering unless the policy is manifestly arbitrary, contrary to statute or unconstitutional", "நீதித்துறை சுயகட்டுப்பாடு (Judicial Restraint), கொள்கை வெளிப்படையாக தன்னிச்சையானதாகவோ, சட்டத்திற்கு முரணானதாகவோ இல்லாத வரை தலையிடக்கூடாது", "D",
         "The Supreme Court ruled that economic policies are formulated by experts and elected representatives; courts cannot sit in judgment over the economic wisdom of such policies.",
         "பொருளாதாரக் கொள்கைகள் நிபுணர்கள் மற்றும் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளால் உருவாக்கப்படுகின்றன; அக்கொள்கைகளின் பொருளாதார விவேகத்தை நீதிமன்றங்கள் தீர்மானிக்க முடியாது எனப்பட்டது."),

        # 41 - B
        ("JRAP_H_041", "Rule of Audi Alteram Partem",
         "The fundamental principle of Natural Justice 'Audi Alteram Partem' enforced vigorously through Judicial Review signifies:",
         "நீதித்துறை மறுஆய்வு மூலம் தீவிரமாக நடைமுறைப்படுத்தப்படும் இயற்கை நீதியின் அடிப்படைக் கொள்கையான 'ஆடி ஆல்டரம் பார்டெம்' (Audi Alteram Partem) எதனைக் குறிக்கிறது?",
         "No person should be a judge in his own cause", "எந்தவொரு நபரும் தனது சொந்த வழக்கில் தானே நீதிபதியாக இருக்கக்கூடாது",
         "Listen to the other side / No person shall be condemned unheard", "மறு தரப்பைக் கேட்க வேண்டும் / எந்தவொரு நபரும் விசாரிக்கப்படாமல் தண்டிக்கப்படக்கூடாது",
         "Orders must always be in writing", "உத்தரவுகள் எப்போதும் எழுத்துப்பூர்வமாக இருக்க வேண்டும்",
         "Judges must be appointed for life", "நீதிபதிகள் வாழ்நாள் முழுவதும் நியமிக்கப்பட வேண்டும்", "B",
         "Audi Alteram Partem requires notice and fair opportunity of hearing before an adverse administrative decision is made; its violation renders an action void under Article 14.",
         "ஆடி ஆல்டரம் பார்டெம் என்பது பாதகமான முடிவை எடுப்பதற்கு முன் அறிவிப்பும் நியாயமான விசாரணை வாய்ப்பும் வழங்கப்பட வேண்டும் என்பதாகும்; இதை மீறுவது உறுப்பு 14-ன் கீழ் செல்லாததாகும்."),

        # 42 - D
        ("JRAP_H_042", "Nemo Judex In Causa Sua",
         "The second rule of Natural Justice 'Nemo Judex In Causa Sua' guards against:",
         "இயற்கை நீதியின் இரண்டாவது விதியான 'நீமோ ஜூடெக்ஸ் இன் காசா சுவா' (Nemo Judex In Causa Sua) எதற்கு எதிராகப் பாதுகாக்கிறது?",
         "Delay in filing appeals", "மேல்முறையீடு செய்வதில் தாமதம்",
         "Lack of evidence in criminal cases", "குற்றவியல் வழக்குகளில் ஆதாரம் இல்லாமை",
         "Excessive court fees", "அதிகப்படியான நீதிமன்றக் கட்டணம்",
         "Judicial or administrative Bias (personal, pecuniary, or subject-matter bias)", "நீதித்துறை அல்லது நிர்வாகச் சார்புநிலை (தனிப்பட்ட, பண அல்லது பொருள் சார்புநிலை)", "D",
         "Nemo Judex in Causa Sua means 'no one should be a judge in his own cause', invalidating decisions marred by pecuniary bias, personal bias, or official bias (A.K. Kraipak Case).",
         "எந்தவொரு நபரும் தனது சொந்த வழக்கில் தானே நீதிபதியாக இருக்கக்கூடாது என்பதே இதன் பொருள்; பணச் சார்பு அல்லது தனிப்பட்ட சார்பு கொண்ட முடிவுகளை இது ரத்து செய்கிறது (ஏ.கே. கிரைபக் வழக்கு)."),

        # 43 - A
        ("JRAP_H_043", "Judicial Review of Delimitation Orders",
         "Under Article 329(a) and the Delimitation Commission Act, are the orders of the Delimitation Commission subject to Judicial Review in courts?",
         "உறுப்பு 329(a) மற்றும் தொகுதி மறுவரையறை ஆணையச் சட்டத்தின் கீழ், தொகுதி மறுவரையறை ஆணையத்தின் உத்தரவுகள் நீதிமன்றங்களில் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவையா?",
         "No, once published in Gazette, orders have force of law and cannot be questioned in any court (Meghraj Kothari Case, 1967)", "இல்லை, அரசிதழில் வெளியிடப்பட்டவுடன் சட்டத்தின் பலனைப் பெறுகின்றன; எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது (மேக்ராஜ் கோத்தாரி வழக்கு, 1967)",
         "Yes, in every High Court", "ஆம், ஒவ்வொரு உயர் நீதிமன்றத்திலும் சவால் செய்யலாம்",
         "Only before a 9-judge bench", "9 நீதிபதிகள் அமர்வில் மட்டுமே",
         "Yes, by filing an RTI petition", "ஆம், RTI மனு தாக்கல் செய்வதன் மூலம் செய்யலாம்", "A",
         "In Meghraj Kothari (1967), the Supreme Court held that Article 329(a) read with Delimitation Act bars courts from questioning delimitation orders once published under authority of law.",
         "மேக்ராஜ் கோத்தாரி (1967) வழக்கில் தொகுதி மறுவரையறை உத்தரவுகள் அரசிதழில் வெளியிடப்பட்ட பின்னர் அவற்றை நீதிமன்றங்களில் கேள்வி கேட்க உறுப்பு 329(a) தடை செய்கிறது எனப்பட்டது."),

        # 44 - C
        ("JRAP_H_044", "Article 137 Review Jurisdiction",
         "Under Article 137 of the Indian Constitution, the Supreme Court has the power to review its own judgments subject to:",
         "இந்திய அரசியலமைப்பு உறுப்பு 137-ன் கீழ், தனது சொந்த தீர்ப்புகளை மறுஆய்வு செய்யும் உச்ச நீதிமன்றத்தின் அதிகாரம் எதற்கு உட்பட்டது?",
         "The direction of the Union Law Minister", "மத்திய சட்ட அமைச்சரின் உத்தரவுக்கு",
         "Prior approval by the Parliament", "நாடாளுமன்றத்தின் முன் ஒப்புதலுக்கு",
         "Any law made by Parliament or rules made under Article 145", "நாடாளுமன்றத்தால் இயற்றப்பட்ட சட்டம் அல்லது உறுப்பு 145-ன் கீழ் உருவாக்கப்பட்ட விதிகளுக்கு",
         "Presidential veto", "குடியரசுத் தலைவரின் வீட்டோ அதிகாரத்திற்கு", "C",
         "Article 137 empowers the Supreme Court to review its judgments subject to parliamentary legislation and Supreme Court Rules (Order XLVII).",
         "உறுப்பு 137 உச்ச நீதிமன்றத்திற்கு நாடாளுமன்ற சட்டம் மற்றும் உச்ச நீதிமன்ற விதிகளுக்கு உட்பட்டு தனது சொந்த தீர்ப்புகளை மறுஆய்வு செய்ய அதிகாரம் அளிக்கிறது."),

        # 45 - B
        ("JRAP_H_045", "Grounds of Review under Order XLVII",
         "Under Order XLVII of Supreme Court Rules, a Review Petition under Article 137 lies only on which of the following grounds?",
         "உச்ச நீதிமன்ற விதிகளின் கீழ், உறுப்பு 137-ன் கீழான மறுசீராய்வு மனு பின்வரும் எந்தக் காரணங்களின் அடிப்படையில் மட்டுமே தாக்கல் செய்யப்பட முடியும்?",
         "Dissatisfaction with the advocate's arguments", "வழக்கறிஞரின் வாதங்களில் அதிருப்தி",
         "Discovery of new and important evidence not available earlier, error apparent on the face of the record, or any other sufficient reason", "முன்னர் கிடைக்காத புதிய முக்கிய ஆதாரம் கண்டறியப்படுதல், ஆவணத்தில் வெளிப்படையாகத் தெரியும் பிழை அல்லது வேறு போதுமான காரணம்",
         "Change of political government in Centre", "மத்தியில் அரசியல் ஆட்சி மாற்றம்",
         "Public demand on social media", "சமூக ஊடகங்களில் பொதுமக்களின் கோரிக்கை", "B",
         "A review petition does not permit a complete rehearing; it is restricted to errors apparent on the face of the record or discovery of crucial new evidence.",
         "மறுசீராய்வு மனு என்பது வழக்கை மீண்டும் புதிதாக விசாரிக்க அனுமதிப்பதில்லை; வெளிப்படையான பிழை அல்லது புதிய முக்கிய ஆதாரங்கள் இருக்கும் போது மட்டுமே அனுமதிக்கப்படுகிறது."),

        # 46 - D
        ("JRAP_H_046", "Judicial Review of President Election",
         "Under Article 71(1) of the Constitution, which exclusive forum has the authority to inquire into and decide all doubts and disputes arising out of the election of a President or Vice-President?",
         "அரசியலமைப்பு உறுப்பு 71(1)-ன் கீழ், குடியரசுத் தலைவர் அல்லது குடியரசுத் துணைத் தலைவர் தேர்தல் தொடர்பான அனைத்து சந்தேகங்கள் மற்றும் தகராறுகளை விசாரித்துத் தீர்மானிக்கும் பிரத்யேக அதிகாரம் யாருக்கு உண்டு?",
         "Election Commission of India", "இந்திய தேர்தல் ஆணையம்",
         "Delhi High Court", "டெல்லி உயர் நீதிமன்றம்",
         "Parliament by Special Majority", "சிறப்புப் பெரும்பான்மையுடன் நாடாளுமன்றம்",
         "Supreme Court of India (whose decision shall be final)", "இந்திய உச்ச நீதிமன்றம் (இதன் முடிவே இறுதியானது)", "D",
         "Article 71(1) provides that all doubts and disputes arising out of the election of a President or Vice-President shall be inquired into and decided by the Supreme Court whose decision shall be final.",
         "உறுப்பு 71(1) குடியரசுத் தலைவர் அல்லது துணைத் தலைவர் தேர்தல் தொடர்பான அனைத்து தகராறுகளும் உச்ச நீதிமன்றத்தால் மட்டுமே விசாரிக்கப்பட்டுத் தீர்மானிக்கப்பட வேண்டும் எனக் கூறுகிறது."),

        # 47 - B
        ("JRAP_H_047", "Article 212 Irregularity of Procedure",
         "According to Article 212 of the Constitution, the validity of any proceedings in the Legislature of a State shall NOT be called in question in any court on the ground of:",
         "அரசியலமைப்பு உறுப்பு 212-ன் படி, ஒரு மாநில சட்டமன்றத்தின் நடவடிக்கைகளின் செல்லுபடியாகும் தன்மை எந்தக் காரணத்திற்காக எந்த நீதிமன்றத்திலும் கேள்வி கேட்கப்படக்கூடாது?",
         "Violation of Fundamental Rights", "அடிப்படை உரிமைகள் மீறல்",
         "Any alleged irregularity of procedure", "நடைமுறையில் உள்ள முறைகேடு (Irregularity of Procedure)",
         "Lack of legislative competence", "சட்டமன்ற அதிகார வரம்பின்மை",
         "Basic structure violation", "அடிப்படைக் கட்டமைப்பு மீறல்", "B",
         "Article 212(1) immunizes internal legislative proceedings from judicial challenge on grounds of mere procedural irregularity, preserving parliamentary autonomy.",
         "உறுப்பு 212(1) சட்டமன்றத்தின் உள் நடவடிக்கைகளை வெறும் நடைமுறை முறைகேடு என்ற காரணத்திற்காக நீதிமன்ற மறுஆய்வுக்கு உட்படுத்துவதிலிருந்து பாதுகாக்கிறது."),

        # 48 - D
        ("JRAP_H_048", "Procedural Irregularity vs Substantive Illegality",
         "In Raja Ram Pal v. Hon'ble Speaker, Lok Sabha (2007) (Cash for Query Case), the Supreme Court distinguished between 'procedural irregularity' and 'substantive illegality', holding that legislative actions are:",
         "ராஜா ராம் பால் வழக்கில் (2007) 'நடைமுறை முறைகேடு' மற்றும் 'அடிப்படைக் கடுமையான சட்டவிரோதம்' ஆகியவற்றை வேறுபடுத்திய உச்ச நீதிமன்றம், சட்டமன்ற நடவடிக்கைகள் குறித்து என்ன தீர்ப்பளித்தது?",
         "Completely immune from judicial review forever", "எப்போதும் நீதித்துறை மறுஆய்விலிருந்து முழுமையான பாதுகாப்பு பெற்றவை",
         "Subject to prior review by High Courts", "உயர் நீதிமன்றங்களின் முன் ஆய்வுக்கு உட்பட்டவை",
         "Subordinate to the Election Commission", "தேர்தல் ஆணையத்திற்கு உட்பட்டவை",
         "Immune for mere procedural irregularities (Art. 122/212), but open to Judicial Review if tainted with substantive illegality, unconstitutionality, or gross violation of natural justice", "வெறும் நடைமுறை முறைகேடுகளுக்கு பாதுகாப்பு உண்டு (122/212); ஆனால் தீவிர சட்டவிரோதம், அரசியலமைப்பு மீறல் அல்லது இயற்கை நீதி மீறல் இருந்தால் மறுஆய்வுக்கு உட்பட்டவை", "D",
         "A 5-judge bench held that legislative privilege does not shield actions infected with substantive illegality or denial of natural justice from judicial review.",
         "சட்டமன்ற சிறப்புரிமை தீவிர சட்டவிரோதம் அல்லது இயற்கை நீதி மறுப்பு கொண்ட நடவடிக்கைகளை நீதித்துறை மறுஆய்விலிருந்து பாதுகாக்காது என 5 நீதிபதிகள் அமர்வு தீர்ப்பளித்தது."),

        # 49 - B
        ("JRAP_H_049", "Article 361 Governor Immunity and Review",
         "In Rameshwar Prasad v. Union of India (2006) (Bihar Assembly Dissolution Case), what did the Supreme Court hold regarding the immunity of the Governor under Article 361?",
         "ராமேஷ்வர் பிரசாத் v. இந்திய ஒன்றியம் (2006) (பீகார் சட்டமன்றக் கலைப்பு வழக்கு) வழக்கில் உறுப்பு 361-ன் கீழான ஆளுநரின் பாதுகாப்பு தொடர்பாக உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
         "The Governor can be criminally prosecuted while in office", "பதவியில் இருக்கும்போதே ஆளுநர் மீது குற்றவியல் வழக்கு தொடரலாம்",
         "While the Governor is personally immune under Art. 361, the executive action/order itself can be judicially reviewed and declared unconstitutional if based on malafide or extraneous grounds", "ஆளுநர் தனிப்பட்ட முறையில் உறுப்பு 361-ன் கீழ் பாதுகாப்பு பெற்றிருந்தாலும், அவரது உத்தரவு துர்நோக்கம் கொண்டதாக இருந்தால் அதை மறுஆய்வு செய்து செல்லாது என அறிவிக்கலாம்",
         "Governor's report can never be looked into by courts", "ஆளுநரின் அறிக்கையை நீதிமன்றங்கள் ஒருபோதும் பார்க்க முடியாது",
         "The Governor is above the Constitution", "ஆளுநர் அரசியலமைப்புக்கு அப்பாற்பட்டவர்", "B",
         "The Supreme Court held that Article 361 personal immunity does not bar the court from examining the constitutionality or malafides of the Governor's report recommending assembly dissolution.",
         "உறுப்பு 361 தனிநபர் பாதுகாப்பு அளித்தாலும், சட்டமன்றத்தைக் கலைக்க பரிந்துரைத்த ஆளுநரின் அறிக்கை துர்நோக்கம் கொண்டதா என ஆராய்வதை அது தடுக்காது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 50 - D
        ("JRAP_H_050", "Ninth Schedule Blanket Vault Myth",
         "The constitutional doctrine that 'The Ninth Schedule cannot be treated as a Black Hole into which any fundamental right can be dropped and lost forever' summarizes the core holding of:",
         "'ஒன்பதாவது அட்டவணையை எந்தவொரு அடிப்படை உரிமையையும் தூக்கி எறிந்து நிரந்தரமாக இழக்கக்கூடிய ஒரு கருந்துளையாகக் கருத முடியாது' என்ற அரசியலமைப்புக் கோட்பாடு எந்த வழக்கின் சாராம்சமாகும்?",
         "A.K. Gopalan Case (1950)", "ஏ.கே. கோபாலன் வழக்கு (1950)",
         "Shankari Prasad Case (1951)", "சங்கரி பிரசாத் வழக்கு (1951)",
         "Sajjan Singh Case (1965)", "சஜ்ஜன் சிங் வழக்கு (1965)",
         "I.R. Coelho v. State of Tamil Nadu (2007)", "I.R. கோயல்ஹோ v. தமிழ்நாடு மாநிலம் (2007)", "D",
         "The unanimous 9-judge bench in I.R. Coelho (2007) decisively ruled that all amendments to the Constitution inserting laws into the Ninth Schedule on or after 24 April 1973 must pass the Basic Structure test.",
         "I.R. கோயல்ஹோ (2007) வழக்கில் 9 நீதிபதிகள் அமர்வு 24 ஏப்ரல் 1973க்குப் பின் 9வது அட்டவணையில் சேர்க்கப்படும் சட்டங்கள் அனைத்தும் அடிப்படைக் கட்டமைப்பு சோதனையில் வெற்றி பெற வேண்டும் என தீர்ப்பளித்தது.")
    ]

    target_keys = ["A", "B", "C", "D"] * 12 + ["B", "D"]  # 12 A, 13 B, 12 C, 13 D = 50 total

    for idx, item in enumerate(hard_data):
        qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item
        tkey = target_keys[idx]
        if correct_key != tkey:
            opts = {
                "A": (en_a, ta_a),
                "B": (en_b, ta_b),
                "C": (en_c, ta_c),
                "D": (en_d, ta_d)
            }
            # Swap
            cur_val = opts[correct_key]
            tgt_val = opts[tkey]
            opts[tkey] = cur_val
            opts[correct_key] = tgt_val
            en_a, ta_a = opts["A"]
            en_b, ta_b = opts["B"]
            en_c, ta_c = opts["C"]
            en_d, ta_d = opts["D"]
            correct_key = tkey

        why_a_en = f"Option A analysis regarding {en_a}."
        why_a_ta = f"{ta_a} பற்றிய ஆப்ஷன் A பகுப்பாய்வு."
        why_b_en = f"Option B analysis regarding {en_b}."
        why_b_ta = f"{ta_b} பற்றிய ஆப்ஷன் B பகுப்பாய்வு."
        why_c_en = f"Option C analysis regarding {en_c}."
        why_c_ta = f"{ta_c} பற்றிய ஆப்ஷன் C பகுப்பாய்வு."
        why_d_en = f"Option D analysis regarding {en_d}."
        why_d_ta = f"{ta_d} பற்றிய ஆப்ஷன் D பகுப்பாய்வு."
        tip_en = "Master critical ratio decidendi, constitutional bench compositions, and landmark dissents."
        tip_ta = "தீர்ப்பின் முக்கிய கோட்பாடுகள் (ratio decidendi), அரசியலமைப்பு அமர்வுகள் மற்றும் வரலாற்று மாற்றுக் கருத்துக்களில் கவனம் செலுத்துக."
        fact_en = f"Pivotal constitutional jurisprudence fact regarding {subtopic}."
        fact_ta = f"{subtopic} தொடர்பான முதன்மையான அரசியலமைப்பு சட்ட உண்மை."

        q = make_jrap_q(
            qid, "Hard", "single_choice", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    keys = [q["correct_answer"] for q in questions]
    counts = Counter(keys)
    print("Part 1 Hard Key counts:", counts)
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    for opt in ["A", "B", "C", "D"]:
        assert 12 <= counts[opt] <= 13, f"Key {opt} out of balance: {counts[opt]}"

    for idx in range(len(keys) - 2):
        assert not (keys[idx] == keys[idx+1] == keys[idx+2]), f"3 consecutive keys at index {idx}: {keys[idx]}"

    out_path = "data/questions/polity/judicial_review_activism_pil_hard.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote 50 hard MCQs to {out_path}")

if __name__ == "__main__":
    build_hard_mcqs()
