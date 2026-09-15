# -*- coding: utf-8 -*-
"""
Build 25 Reasoning (Assertion-Reason) MCQs for Parliamentary Privileges (PP_R_001 to PP_R_025)
TNPSC Nova AI Content Engine
"""
import json
import os
import shutil
from collections import Counter
from parliamentary_privileges_mcq_helper import make_pp_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_reasoning_questions():
    questions = []

    reasoning_specs = [
        # R_001
        ("001", "Freedom of Speech", "Medium",
         "Assertion (A): Freedom of speech in Parliament under Article 105(1) is not subject to the reasonable restrictions enumerated in Article 19(2).\nReason (R): Members of Parliament must be able to express thoughts and air public grievances without fear of prosecution for defamation, contempt of court, or other ordinary statutory offences.",
         "கூற்று (A): உறுப்பு 105(1)-ன் கீழ் நாடாளுமன்றத்தில் வழங்கப்படும் பேச்சுரிமை, உறுப்பு 19(2)-ல் உள்ள நியாயமான கட்டுப்பாடுகளுக்கு உட்படாது.\nகாரணம் (R): அவதூறு, நீதிமன்ற அவமதிப்பு போன்ற குற்றச்சாட்டுகளுக்கு அஞ்சாமல் மக்கள் குறைகளையும் கருத்துக்களையும் எம்பிக்கள் வெளிப்படையாகப் பேச வேண்டியது அவசியமாகும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Article 105(1) guarantees untrammeled free debate inside Parliament free from Article 19(2) statutory limitations to protect the democratic vitality of the House.",
         "உறுப்பு 105(1) அவையின் சுதந்திரமான விவாதத்தைப் பாதுகாக்க உறுப்பு 19(2)-ன் கட்டுப்பாடுகளிலிருந்து விடுபட்ட பேச்சுரிமையை வழங்குகிறது; எனவே (R) என்பது (A)-வின் சரியான விளக்கமாகும்."),

        # R_002
        ("002", "Judicial Immunity", "Medium",
         "Assertion (A): Under Article 105(2), no civil or criminal suit can be filed in any court against an MP for anything said or any vote given in Parliament.\nReason (R): The purpose of parliamentary immunity is to preserve the independence and supremacy of the legislature in discharging its constitutional functions.",
         "கூற்று (A): உறுப்பு 105(2)-ன் கீழ், நாடாளுமன்றத்தில் பேசிய எதற்கும் அல்லது அளித்த வாக்கிற்கும் எம்பி மீது எந்த நீதிமன்றத்திலும் சிவில் அல்லது குற்றவியல் வழக்கு தொடர முடியாது.\nகாரணம் (R): நாடாளுமன்ற சிறப்புரிமைகளின் நோக்கம் சட்டமன்றம் தனது பணிகளைச் செய்வதில் சுதந்திரமாகவும் தன்னாட்சியுடனும் இயங்குவதைப் பாதுகாப்பதே ஆகும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Under Tej Kiran Jain (1970), the immunity under Article 105(2) is complete and absolute to protect legislative autonomy from judicial interference.",
         "உறுப்பு 105(2) நாடாளுமன்ற சுயாட்சியைப் பாதுகாக்கவே முழுமையான நீதிமன்ற விலக்களிப்பை வழங்குகிறது; எனவே (R) சரியான விளக்கமாகும்."),

        # R_003
        ("003", "Civil Arrest Restriction", "Medium",
         "Assertion (A): Members of Parliament are immune from arrest in civil proceedings for 40 days before and 40 days after a session, but enjoy no immunity from arrest in criminal cases.\nReason (R): The administration of criminal justice and maintenance of public order cannot be compromised by extending personal immunity to crimes committed by legislators.",
         "கூற்று (A): எம்பிக்களுக்கு கூட்டத்தொடருக்கு 40 நாட்களுக்கு முன்பும் பின்பும் சிவில் வழக்குகளில் கைதிலிருந்து விலக்கு உண்டு; ஆனால் குற்றவியல் வழக்குகளில் எந்த விலக்களிப்பும் கிடையாது.\nகாரணம் (R): குற்றவியல் நீதியை நிர்வகிப்பதும் சட்டம் ஒழுங்கைப் பராமரிப்பதும் சட்டமன்ற உறுப்பினர்களின் தனிப்பட்ட பாதுகாப்புக்காக சமரசம் செய்யப்பட முடியாது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Section 135A CPC confers immunity exclusively in civil cases; criminal law applies uniformly to all persons, and MPs enjoy no special shield against criminal arrest.",
         "சிவில் வழக்குகளில் மட்டுமே கைது விலக்கு உண்டு; குற்றவியல் சட்டம் அனைவருக்கும் சமமாகப் பொருந்தும் என்பதால் குற்றங்களில் எம்பிக்களுக்கு விலக்கு கிடையாது; (R) சரியான விளக்கம்."),

        # R_004
        ("004", "Bribery Ruling 2024", "Hard",
         "Assertion (A): In Sita Soren v. Union of India (2024), the Supreme Court ruled that legislators accepting bribes to vote or speak in the legislature can be criminally prosecuted under the Prevention of Corruption Act.\nReason (R): Bribery is an independent offence complete upon acceptance, and creating immunity for corruption subverts the integrity of representative democracy and the rule of law.",
         "கூற்று (A): சீதா சோரன் (2024) வழக்கில், அவையில் பேச அல்லது வாக்களிக்க லஞ்சம் வாங்கும் சட்டமன்ற உறுப்பினர்கள் மீது ஊழல் தடுப்புச் சட்டத்தின் கீழ் வழக்கு தொடரலாம் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): லஞ்சம் என்பது பெற்றவுடனேயே முடிவடையும் தனிப்பட்ட குற்றமாகும்; ஊழலுக்கு விலக்களிப்பு வழங்குவது பிரதிநிதித்துவ ஜனநாயகத்தையும் சட்டத்தின் ஆட்சியையும் சீர்குலைத்துவிடும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The 7-judge bench unanimously held that Article 105(2) does not immunize bribery because accepting bribes has no legitimate nexus to legislative functioning and destroys democratic trust.",
         "லஞ்சம் வாங்குவது சட்டமன்றப் பணியோடு தொடர்புடையது அல்ல என்பதால் உறுப்பு 105(2) லஞ்சத்திற்கு பாதுகாப்பு அளிக்காது என உச்ச நீதிமன்றம் தெளிவாகக் கூறியது; (R) சரியான விளக்கம்."),

        # R_005
        ("005", "Article 121 and Article 211", "Medium",
         "Assertion (A): The conduct of a Supreme Court or High Court judge in discharge of judicial duties cannot be discussed in Parliament, except upon an impeachment motion under Article 124(4).\nReason (R): Article 121 ensures the absolute independence of the judiciary from political criticism and harassment on the floor of the legislature.",
         "கூற்று (A): பதவிநீக்கத் தீர்மானத்தின் மீதான விவாதத்தைத் தவிர, உச்ச அல்லது உயர் நீதிமன்ற நீதிபதிகளின் நடத்தை குறித்து நாடாளுமன்றத்தில் விவாதிக்க முடியாது.\nகாரணம் (R): உறுப்பு 121 சட்டமன்ற விவாதங்களின் மூலம் நீதித்துறை அரசியல் விமர்சனங்களுக்கும் அச்சுறுத்தல்களுக்கும் ஆளாகாமல் அதன் முழுமையான சுதந்திரத்தைப் பாதுகாக்கிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Article 121 secures judicial independence by barring legislative speeches evaluating judicial orders, preserving the separation of powers.",
         "நீதித்துறையின் சுதந்திரத்தைப் பாதுகாக்கவும் அதிகாரப் பிரிவினையை நிலைநிறுத்தவுமே நீதிபதிகளின் நடத்தை குறித்த விவாதங்களை உறுப்பு 121 தடை செய்கிறது; (R) சரியான விளக்கம்."),

        # R_006
        ("006", "Article 122 Procedural Irregularity", "Hard",
         "Assertion (A): Courts are constitutionally prohibited from questioning the validity of proceedings in Parliament on grounds of irregularity of procedure.\nReason (R): The Supreme Court in Raja Ram Pal (2007) held that parliamentary proceedings are completely immune from judicial review even when tainted by patent illegality or constitutional invalidity.",
         "கூற்று (A): நடைமுறை முறைகேடு என்ற காரணத்தின் அடிப்படையில் நாடாளுமன்ற நடவடிக்கைகளின் செல்லுபடியாகும் தன்மையை நீதிமன்றங்கள் கேள்வி கேட்பதை அரசியலமைப்பு தடை செய்கிறது.\nகாரணம் (R): அப்பட்டமான சட்டவிரோதம் அல்லது அரசியலமைப்பு மீறல் இருந்தாலும் கூட நாடாளுமன்ற நடவடிக்கைகள் நீதிமன்ற ஆய்வுக்கு அப்பாற்பட்டவை என ராஜா ராம் பால் (2007) வழக்கில் கூறப்பட்டது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "C",
         "Assertion (A) is true under Article 122(1). Reason (R) is false because Raja Ram Pal established that patent illegality, substantive unconstitutionality, and violations of fundamental rights ARE subject to judicial review.",
         "கூற்று (A) உறுப்பு 122(1)-ன் படி உண்மை. காரணம் (R) தவறு, ஏனெனில் அப்பட்டமான சட்டவிரோதம் அல்லது அரசியலமைப்பு மீறல் இருந்தால் நீதிமன்றங்கள் தலையிடலாம் என ராஜா ராம் பால் தீர்ப்பில் கூறப்பட்டுள்ளது."),

        # R_007
        ("007", "Precincts of Parliament", "Medium",
         "Assertion (A): A police officer cannot arrest a sitting Member of Parliament within the precincts of the Parliament House without obtaining the prior permission of the Presiding Officer.\nReason (R): The Presiding Officer is the sole guardian of the House, and unauthorized arrests inside precincts would violate the dignity and orderly proceedings of the legislature.",
         "கூற்று (A): அவைத் தலைவரின் முன் அனுமதியின்றி நாடாளுமன்ற வளாகத்திற்குள் எந்த ஒரு எம்பியையும் ஒரு காவல் அதிகாரி கைது செய்ய முடியாது.\nகாரணம் (R): அவைத் தலைவரே அவையின் ஒரே பாதுகாவலராவார்; வளாகத்திற்குள் அனுமதியின்றி கைது செய்வது அவையின் மாண்பையும் முறைப்படியான விவாதங்களையும் பாதிக்கும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The precincts of the House are under the absolute control of the Presiding Officer; executing legal process or making arrests without permission breaches parliamentary privilege.",
         "நாடாளுமன்ற வளாகம் அவைத் தலைவரின் முழுக் கட்டுப்பாட்டில் உள்ளது; அனுமதியின்றி கைது செய்வது அவையின் மாண்பை மீறுவதாகும்; (R) சரியான விளக்கம்."),

        # R_008
        ("008", "Secret Sitting Disclosure", "Medium",
         "Assertion (A): Publishing or disclosing any portion of the proceedings of a secret sitting of the House is treated as a gross breach of privilege and contempt.\nReason (R): Secret sittings are held on matters of grave national security and policy, where confidentiality is essential to protect the public interest.",
         "கூற்று (A): அவையின் ரகசிய அமர்வின் விவாதங்களின் எந்தவொரு பகுதியையும் வெளியிடுவது கடுமையான சிறப்புரிமை மீறல் மற்றும் அவமதிப்பாகக் கருதப்படுகிறது.\nகாரணம் (R): நாட்டின் தீவிர பாதுகாப்பு மற்றும் கொள்கை சார்ந்த விவகாரங்களில் பொதுநலனைப் பாதுகாக்க ரகசியத்தன்மை இன்றியமையாதது என்பதால் ரகசிய அமர்வுகள் நடத்தப்படுகின்றன.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Rule 252 of Lok Sabha explicitly designates disclosure of secret sittings as gross breach of privilege to safeguard state secrets.",
         "அரசின் ரகசியங்களைப் பாதுகாக்கவே ரகசிய அமர்வு விவாதங்களை வெளியிடுவது கடுமையான சிறப்புரிமை மீறலாகக் கருதப்படுகிறது; (R) சரியான விளக்கம்."),

        # R_009
        ("009", "Article 361A Malice", "Medium",
         "Assertion (A): A journalist publishing an accurate report of parliamentary debates can still be sued for defamation if the publication is proved to have been made with malice.\nReason (R): The constitutional immunity conferred by Article 361A is conditional upon the report being substantially true and made in good faith without malice.",
         "கூற்று (A): நாடாளுமன்ற விவாதங்களைச் சரியாக வெளியிட்டிருந்தாலும், அந்த வெளியீடு கெட்ட எண்ணத்தோடு (malice) செய்யப்பட்டது என நிரூபிக்கப்பட்டால் பத்திரிகையாளர் மீது அவதூறு வழக்கு தொடரலாம்.\nகாரணம் (R): உறுப்பு 361A-ன் கீழான அரசியலமைப்புப் பாதுகாப்பு அந்த அறிக்கை கணிசமான உண்மையாகவும், துவேஷம் இல்லாமலும் நல்லெண்ணத்தில் வெளியிடப்பட்டால் மட்டுமே கிடைக்கும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The proviso to Article 361A(1) expressly excludes malicious publications from immunity, making bona fides an essential condition for press protection.",
         "உறுப்பு 361A-ன் படி துவேஷத்துடன் வெளியிடப்படும் அறிக்கைகளுக்கு பாதுகாப்பு கிடைக்காது; எனவே நல்லெண்ணம் கட்டாயமாகும்; (R) சரியான விளக்கம்."),

        # R_010
        ("010", "Codification of Privileges", "Hard",
         "Assertion (A): Parliament of India has enacted a comprehensive statutory code exhaustively defining all parliamentary privileges under Article 105(3).\nReason (R): Codifying privileges by ordinary statute would make them subject to Fundamental Rights and judicial review under Article 13 of the Constitution.",
         "கூற்று (A): இந்திய நாடாளுமன்றம் உறுப்பு 105(3)-ன் கீழ் அனைத்து நாடாளுமன்ற சிறப்புரிமைகளையும் தொகுத்து ஒரு விரிவான சட்டத்தை இயற்றியுள்ளது.\nகாரணம் (R): சிறப்புரிமைகளை சாதாரண சட்டமாகத் தொகுத்தால் அவை உறுப்பு 13-ன் கீழ் அடிப்படை உரிமைகளுக்கும் நீதித்துறை மறுஆய்விற்கும் உட்பட்டுவிடும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "D",
         "Assertion (A) is false because Parliament has never enacted a codifying privileges statute. Reason (R) is true and represents the exact reason why Parliament has resisted codification.",
         "கூற்று (A) தவறு, ஏனெனில் நாடாளுமன்றம் இதுவரை சிறப்புரிமைகளைச் சட்டமாகத் தொகுக்கவில்லை. காரணம் (R) உண்மை, ஏனெனில் சட்டமாக்கினால் நீதித்துறை ஆய்வுக்கு உட்பட நேரிடும் என்பதே தொகுக்கப்படாததற்கான காரணமாகும்."),

        # R_011
        ("011", "Searchlight Majority", "Medium",
         "Assertion (A): In the 1959 Searchlight case, the Supreme Court held that the legislative privilege to prohibit publication of debates overrode the citizen's freedom of speech under Article 19(1)(a).\nReason (R): The Constitution Bench held that the specific constitutional provision in Article 194(3) was not controlled by the general fundamental right under Article 19(1)(a).",
         "கூற்று (A): 1959-ன் சர்ச்லைட் வழக்கில், விவாதங்களை வெளியிட தடை செய்யும் சட்டமன்ற சிறப்புரிமை குடிமகனின் உறுப்பு 19(1)(a)-ன் கீழான பேச்சுரிமையை விட மேலோங்கும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): உறுப்பு 194(3)-ல் உள்ள குறிப்பிட்ட அரசியலமைப்பு விதி, உறுப்பு 19(1)(a)-ன் பொதுவான அடிப்படை உரிமையால் கட்டுப்படுத்தப்படாது என அரசியலமைப்பு அமர்வு கருதியது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The majority applied the rule of harmonious construction by treating Article 194(3) as a special provision prevailing over Article 19(1)(a).",
         "உறுப்பு 194(3) ஒரு சிறப்பு விதியாகக் கருதப்பட்டு உறுப்பு 19(1)(a)-வை விட மேலோங்கும் என பெரும்பான்மை தீர்ப்பில் சமரசம் செய்யப்பட்டது; (R) சரியான விளக்கம்."),

        # R_012
        ("012", "Keshav Singh General Warrant", "Hard",
         "Assertion (A): Under the Indian constitutional framework, a general or unspeaking warrant of arrest issued by the Speaker of a Legislative Assembly is completely immune from judicial review by the High Court.\nReason (R): Unlike the British House of Commons, Indian legislatures are creatures of a written Constitution and are subject to the supremacy of the Constitution and fundamental rights.",
         "கூற்று (A): இந்திய அரசியலமைப்பு கட்டமைப்பில், சட்டமன்ற சபாநாயகரால் பிறப்பிக்கப்படும் காரணம் குறிப்பிடப்படாத பொது வாரண்ட் உயர் நீதிமன்ற ஆய்விலிருந்து முழுமையாக விலக்களிக்கப்படுகிறது.\nகாரணம் (R): பிரிட்டிஷ் நாடாளுமன்றம் போலில்லாமல், இந்திய சட்டமன்றங்கள் எழுதப்பட்ட அரசியலமைப்பால் உருவாக்கப்பட்டவை மற்றும் அரசியலமைப்பு மேலாதிக்கத்திற்கும் அடிப்படை உரிமைகளுக்கும் உட்பட்டவை.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "D",
         "Assertion (A) is false because Keshav Singh (1965) established that even general warrants of the legislature are subject to judicial review under Articles 21, 22, and 226. Reason (R) is true.",
         "கூற்று (A) தவறு, ஏனெனில் கேசவ் சிங் தீர்ப்பின்படி பொது வாரண்டுகளும் நீதிமன்ற ஆய்வுக்கு உட்பட்டவை. காரணம் (R) உண்மை, ஏனெனில் இந்திய சட்டமன்றங்கள் அரசியலமைப்புக்கு உட்பட்டவை."),

        # R_013
        ("013", "Committee of Privileges Membership", "Medium",
         "Assertion (A): The Committee of Privileges in Lok Sabha consists of 15 members, whereas in Rajya Sabha it consists of 10 members.\nReason (R): The proportional strength of members reflects the relative total membership sizes of Lok Sabha (543) and Rajya Sabha (245).",
         "கூற்று (A): மக்களவை சிறப்புரிமைக் குழு 15 உறுப்பினர்களையும், மாநிலங்களவை சிறப்புரிமைக் குழு 10 உறுப்பினர்களையும் கொண்டுள்ளது.\nகாரணம் (R): குழுக்களின் இந்த உறுப்பினர் எண்ணிக்கை மக்களவை (543) மற்றும் மாநிலங்களவை (245) ஆகியவற்றின் மொத்த பலத்தைப் பிரதிபலிக்கிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The committee sizes are fixed under respective Rules of Procedure reflecting the structural ratio between both Houses of Parliament.",
         "அவைகளின் மொத்த உறுப்பினர்களின் விகிதத்திற்கு ஏற்பவே மக்களவையில் 15 உறுப்பினர்களும் மாநிலங்களவையில் 10 உறுப்பினர்களும் நிர்ணயிக்கப்பட்டுள்ளனர்; (R) சரியான விளக்கம்."),

        # R_014
        ("014", "Expulsion vs Disqualification", "Medium",
         "Assertion (A): When an MP is expelled from the House by a resolution, they are not automatically disqualified from contesting the resulting by-election.\nReason (R): Disqualification from contesting parliamentary elections can only be created by an express provision of the Constitution or a law enacted by Parliament.",
         "கூற்று (A): அவையின் தீர்மானம் மூலம் ஒரு எம்பி பதவிநீக்கம் செய்யப்படும் போது, இடைத்தேர்தலில் போட்டியிடுவதிலிருந்து அவர் தானாகவே தகுதிநீக்கம் செய்யப்படுவதில்லை.\nகாரணம் (R): தேர்தலில் போட்டியிடுவதற்கான தகுதியிழப்பை அரசியலமைப்பு விதியோ அல்லது நாடாளுமன்றச் சட்டமோ மட்டுமே உருவாக்க முடியும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Expulsion vacates the seat under internal disciplinary power; it does not constitute statutory disqualification under the Representation of the People Act, 1951.",
         "பதவிநீக்கம் இடத்தை மட்டுமே காலி செய்கிறது; மக்கள் பிரதிநிதித்துவச் சட்டத்தின் கீழ் தடை இல்லாதவரை இடைத்தேர்தலில் மீண்டும் போட்டியிட முடியும்; (R) சரியான விளக்கம்."),

        # R_015
        ("015", "Presidential Immunity Distinction", "Medium",
         "Assertion (A): The President of India is completely immune from any criminal proceedings whatsoever during their term of office under Article 361.\nReason (R): Members of Parliament enjoy identical total immunity from criminal proceedings during their 5-year tenure under Article 105.",
         "கூற்று (A): உறுப்பு 361-ன் கீழ் இந்தியக் குடியரசுத் தலைவருக்கு பதவிக்காலத்தில் எந்தவொரு குற்றவியல் நடவடிக்கையிலிருந்தும் முழுமையான விலக்களிப்பு உண்டு.\nகாரணம் (R): நாடாளுமன்ற உறுப்பினர்களுக்கும் உறுப்பு 105-ன் கீழ் தங்களின் 5 ஆண்டு பதவிக்காலத்தில் அதே போன்ற முழுமையான குற்றவியல் விலக்களிப்பு உண்டு.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "C",
         "Assertion (A) is true under Article 361(2). Reason (R) is completely false because MPs have NO criminal immunity under Article 105 or any other provision.",
         "கூற்று (A) உறுப்பு 361(2)-ன் படி உண்மை. காரணம் (R) முற்றிலும் தவறு, ஏனெனில் எம்பிக்களுக்கு குற்றவியல் வழக்குகளில் எந்தப் பாதுகாப்பும் கிடையாது."),

        # R_016
        ("016", "Jury Service Exemption", "Medium",
         "Assertion (A): A member of Parliament cannot be compelled to attend as a witness in a civil court while Parliament is in session without the leave of the House.\nReason (R): The primary constitutional obligation of an elected legislator is attendance and participation in the proceedings of Parliament.",
         "கூற்று (A): நாடாளுமன்றக் கூட்டத்தொடர் நடக்கும் போது, அவையின் அனுமதியின்றி ஒரு எம்பியை சிவில் நீதிமன்றத்தில் சாட்சியாளராக ஆஜராகுமாறு கட்டாயப்படுத்த முடியாது.\nகாரணம் (R): தேர்ந்தெடுக்கப்பட்ட ஒரு சட்டமன்ற உறுப்பினரின் முதன்மையான அரசியலமைப்பு கடமை நாடாளுமன்ற நடவடிக்கைகளில் கலந்துகொள்வதே ஆகும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Attendance in Parliament takes precedence over all civil court summons; legislators are protected from distractions during legislative sessions.",
         "நாடாளுமன்றக் கடமையே முதன்மையானது என்பதால் கூட்டத்தொடர் நடக்கும் போது நீதிமன்ற சாட்சியாளராக ஆஜராவதிலிருந்து விலக்கு உண்டு; (R) சரியான விளக்கம்."),

        # R_017
        ("017", "Feroze Gandhi Act Restoration", "Hard",
         "Assertion (A): The Parliamentary Proceedings (Protection of Publication) Act, 1956 was repealed during the National Emergency in 1975.\nReason (R): The 44th Constitutional Amendment Act, 1978 permanently constitutionalized these protections by introducing Article 361A into the Constitution.",
         "கூற்று (A): 1956-ஆம் ஆண்டின் நாடாளுமன்ற நடவடிக்கைகள் (வெளியீடு பாதுகாப்பு) சட்டம் 1975-ன் தேசிய அவசரநிலையின் போது ரத்து செய்யப்பட்டது.\nகாரணம் (R): 44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 உறுப்பு 361A-ஐ அரசியலமைப்பில் சேர்த்ததன் மூலம் இந்தப் பாதுகாப்பை நிரந்தரமாக்கியது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "B",
         "Both statements are historically true, but (R) describes the subsequent restoration rather than explaining why the Indira Gandhi government repealed it during the Emergency.",
         "இரண்டு கூற்றுகளும் உண்மையானவை; ஆனால் (R) என்பது 44வது திருத்தத்தின் மீட்பு நடவடிக்கையே அன்றி அவசரநிலைக் காலத்தில் ரத்து செய்யப்பட்டதற்கான காரணமல்ல; எனவே (R) சரியான விளக்கமல்ல."),

        # R_018
        ("018", "Sub Judice Convention", "Medium",
         "Assertion (A): Members of Parliament are conventionally restricted from discussing matters that are sub judice before a court of law.\nReason (R): Unrestricted legislative debate on active trials could prejudice the administration of justice and compromise the fair trial rights of litigants.",
         "கூற்று (A): நீதிமன்றத்தில் விசாரணையில் உள்ள (sub judice) விவகாரங்கள் குறித்து நாடாளுமன்றத்தில் விவாதிப்பது மரபு ரீதியாக கட்டுப்படுத்தப்படுகிறது.\nகாரணம் (R): நிலுவையில் உள்ள வழக்குகள் மீதான கட்டுப்பாடற்ற விவாதம் நீதி நிர்வாகத்தைப் பாதிக்கலாம் மற்றும் வழக்காடிகளின் நியாயமான விசாரணை உரிமையை சமரசம் செய்யலாம்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The sub judice rule preserves the fair trial rights of accused and prevents political interference with judicial determination.",
         "நீதிமன்ற விசாரணையின் நடுநிலையைப் பாதுகாக்கவும் வழக்காடிகளின் உரிமையைக் காக்கவுமே இந்த மரபு கடைப்பிடிக்கப்படுகிறது; (R) சரியான விளக்கம்."),

        # R_019
        ("019", "Expunction Privilege Violation", "Medium",
         "Assertion (A): Publishing portions of parliamentary speeches that have been expunged by the Speaker constitutes a breach of privilege and contempt of the House.\nReason (R): Once words are expunged from the record by the Speaker, they cease to be part of the official proceedings and lose all constitutional publication immunity.",
         "கூற்று (A): சபாநாயகரால் நீக்கப்பட்ட நாடாளுமன்றப் பேச்சின் பகுதிகளை வெளியிடுவது சிறப்புரிமை மீறல் மற்றும் அவமதிப்பாகும்.\nகாரணம் (R): சபாநாயகரால் சொற்கள் நீக்கப்பட்டவுடன், அவை அதிகாரப்பூர்வ பதிவின் அங்கமாக இருப்பது முடிவுக்கு வருகிறது மற்றும் அனைத்து வெளியீட்டுப் பாதுகாப்பையும் இழக்கிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Expunged words have no legal existence on the official record; disseminating them circumvents the Speaker's order and amounts to contempt.",
         "நீக்கப்பட்ட சொற்களுக்கு சட்டபூர்வ இருப்பு கிடையாது; அவற்றை வெளியிடுவது சபாநாயகரின் உத்தரவை அவமதிப்பதாகும்; (R) சரியான விளக்கம்."),

        # R_020
        ("020", "RTI Exemption Section 8(1)(c)", "Medium",
         "Assertion (A): A citizen cannot obtain copies of confidential internal working papers of the Committee of Privileges under the Right to Information Act, 2005.\nReason (R): Section 8(1)(c) of the RTI Act explicitly exempts information the disclosure of which would cause a breach of privilege of Parliament or State Legislature.",
         "கூற்று (A): 2005-ன் தகவல் அறியும் உரிமைச் சட்டத்தின் கீழ் சிறப்புரிமைக் குழுவின் ரகசிய உள் ஆவணங்களை ஒரு குடிமகன் பெற முடியாது.\nகாரணம் (R): RTI சட்டத்தின் பிரிவு 8(1)(c) நாடாளுமன்ற அல்லது சட்டமன்ற சிறப்புரிமை மீறலுக்கு வழிவகுக்கும் தகவல்களை வெளிப்படுத்துவதிலிருந்து விலக்கு அளிக்கிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Section 8(1)(c) protects legislative privilege by shielding committee deliberations from premature disclosure under RTI.",
         "நாடாளுமன்ற சிறப்புரிமைகளைப் பாதுகாக்கவே RTI பிரிவு 8(1)(c) குழு ஆவணங்களை முன்கூட்டியே வெளியிடுவதைத் தடுக்கிறது; (R) சரியான விளக்கம்."),

        # R_021
        ("021", "Contempt Imprisonment Expiry", "Medium",
         "Assertion (A): A person committed to prison by order of the House for contempt of Parliament is automatically entitled to be released upon the prorogation of the House.\nReason (R): The penal power of Parliament to commit a person to prison terminates with the prorogation of the session in which the committal took place.",
         "கூற்று (A): நாடாளுமன்ற அவமதிப்பிற்காக சிறையிலடைக்கப்பட்ட நபர், கூட்டத்தொடர் முடக்கப்படும் (prorogation) போது தானாகவே விடுவிக்கப்பட தகுதியுடையவராகிறார்.\nகாரணம் (R): ஒரு நபரை சிறையில் அடைக்கும் நாடாளுமன்றத்தின் தண்டனை அதிகாரம், அந்த கூட்டத்தொடர் முடிவுக்கு வருவதோடு முடிவுக்கு வருகிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Under established British and Indian parliamentary practice, committal to prison by the legislature cannot outlast the session of the House.",
         "நாடாளுமன்றத்தின் சிறைக்காவல் உத்தரவு கூட்டத்தொடர் முடிவடைவதைத் தாண்டி நீடிக்க முடியாது என்பதால் முடக்கப்பட்டதும் நபர் விடுவிக்கப்படுவார்; (R) சரியான விளக்கம்."),

        # R_022
        ("022", "44th Amendment House of Commons", "Medium",
         "Assertion (A): The 44th Constitutional Amendment Act, 1978 removed the express words 'House of Commons of the Parliament of the United Kingdom' from Article 105(3) and Article 194(3).\nReason (R): Retaining a permanent reference to a foreign colonial legislature in the foundational text of the Indian Constitution was deemed inappropriate for a sovereign republic.",
         "கூற்று (A): 44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 உறுப்புகள் 105(3) மற்றும் 194(3)-லிருந்து 'பிரிட்டிஷ் நாடாளுமன்றத்தின் பொது மக்கள் அவை' என்ற வெளிப்படையான சொற்களை நீக்கியது.\nகாரணம் (R): ஒரு சுதந்திர இறையாண்மை கொண்ட குடியரசின் அரசியலமைப்பில் காலனித்துவ வெளிநாட்டு நாடாளுமன்றத்தைப் பற்றிய நிரந்தர குறிப்பு இருப்பது பொருத்தமற்றதாகக் கருதப்பட்டது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The 44th Amendment omitted direct reference to the British House of Commons for reasons of national dignity, fixing the reference to the privileges existing as of June 1979.",
         "தேசிய மாண்பைக் கருத்தில் கொண்டே பிரிட்டிஷ் சபை பற்றிய குறிப்பு நீக்கப்பட்டு 1979 நிலவரப்படி நிலைநிறுத்தப்பட்டது; (R) சரியான விளக்கம்."),

        # R_023
        ("023", "Arrest Information Failure", "Medium",
         "Assertion (A): When an MP is arrested on a criminal charge, failure of the arresting authority to immediately inform the Speaker constitutes a breach of privilege.\nReason (R): The House has a sovereign right to know why any of its members is prevented from attending to their parliamentary duties.",
         "கூற்று (A): ஒரு எம்பி குற்றவியல் வழக்கில் கைது செய்யப்படும் போது, சபாநாயகருக்கு உடனடியாக தகவல் தெரிவிக்கத் தவறுவது சிறப்புரிமை மீறலாகும்.\nகாரணம் (R): தனது உறுப்பினர் ஏன் நாடாளுமன்றக் கடமைகளில் பங்கேற்பதிலிருந்து தடுக்கப்பட்டுள்ளார் என்பதை அறியும் இறையாண்மை உரிமை அவைக்கு உண்டு.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "Under Lok Sabha Rules 229 and 230, arresting authorities must immediately notify the Speaker; failure obstructs the House's knowledge of its composition.",
         "மக்களவை விதிகள் 229 மற்றும் 230-ன் படி தகவலை உடனடியாகத் தெரிவிக்கத் தவறுவது அவையின் பணிகளுக்கு இடையூறு செய்வதால் உரிமை மீறலாகும்; (R) சரியான விளக்கம்."),

        # R_024
        ("024", "Attorney General Privilege", "Medium",
         "Assertion (A): The Attorney General of India enjoys all parliamentary privileges and immunities under Article 105(4) when participating in parliamentary proceedings.\nReason (R): Under Article 76, the Attorney General is an ex-officio voting Member of the Council of Ministers.",
         "கூற்று (A): நாடாளுமன்ற நடவடிக்கைகளில் பங்கேற்கும் போது இந்திய தலைமை வழக்கறிஞர் (AGI) உறுப்பு 105(4)-ன் கீழ் அனைத்து நாடாளுமன்ற சிறப்புரிமைகளையும் அனுபவிக்கிறார்.\nகாரணம் (R): உறுப்பு 76-ன் கீழ் தலைமை வழக்கறிஞர் அமைச்சரவையின் பதவிவழி வாக்களிக்கும் உறுப்பினராவார்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "C",
         "Assertion (A) is true under Article 105(4) read with Article 88. Reason (R) is completely false because the Attorney General is NOT a minister, not a member of Parliament, and has no right to vote under Article 88.",
         "கூற்று (A) உறுப்புகள் 105(4) மற்றும் 88-ன் படி உண்மை. காரணம் (R) முற்றிலும் தவறு, ஏனெனில் தலைமை வழக்கறிஞர் அமைச்சரும் அல்ல, அவருக்கு வாக்களிக்கும் உரிமையும் இல்லை."),

        # R_025
        ("025", "Basic Structure Privileges", "Hard",
         "Assertion (A): The parliamentary privileges conferred under Article 105 cannot be utilized by Parliament to destroy the Basic Structure of the Indian Constitution.\nReason (R): Judicial review, democracy, and the rule of law are cardinal pillars of the Basic Structure that limit the exercise of all constitutional and statutory powers in India.",
         "கூற்று (A): உறுப்பு 105-ன் கீழ் வழங்கப்பட்டுள்ள நாடாளுமன்ற சிறப்புரிமைகளை இந்திய அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பைத் தகர்க்க நாடாளுமன்றம் பயன்படுத்த முடியாது.\nகாரணம் (R): நீதித்துறை ஆய்வு, ஜனநாயகம், மற்றும் சட்டத்தின் ஆட்சி ஆகியவை இந்தியாவின் அனைத்து அரசியலமைப்பு மற்றும் சட்ட அதிகாரங்களைக் கட்டுப்படுத்தும் அடிப்படைக் கட்டமைப்பின் முக்கியத் தூண்களாகும்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
         "(A) is true but (R) is false",
         "(A) is false but (R) is true", "A",
         "The Basic Structure Doctrine (Kesavananda Bharati) is supreme over all constitutional provisions; parliamentary privileges operate within the constitutional framework and cannot abrogate basic features.",
         "அடிப்படைக் கட்டமைப்பு கோட்பாடு அனைத்திற்கும் மேலானது; சிறப்புரிமைகள் அதற்குட்பட்டு செயல்பட வேண்டுமே தவிர அடிப்படைக் கட்டமைப்பை மீற முடியாது; (R) சரியான விளக்கம்.")
    ]

    for item in reasoning_specs:
        num, subtopic, diff, en_stem, ta_stem, en_a, en_b, en_c, en_d, correct_key, exp_en, exp_ta = item
        qid = f"PP_R_{num}"
        why_a_en = f"Evaluation of Option A: Standard assertion-reason logic."
        why_a_ta = f"ஆப்ஷன் A மதிப்பீடு: கூற்று-காரணம் தருக்க பகுப்பாய்வு."
        why_b_en = f"Evaluation of Option B: Distractor assessment."
        why_b_ta = f"ஆப்ஷன் B மதிப்பீடு: மாற்று காரண மதிப்பீடு."
        why_c_en = f"Evaluation of Option C: Distractor assessment."
        why_c_ta = f"ஆப்ஷன் C மதிப்பீடு: கூற்று சரி ஆனால் காரணம் தவறு என்ற நிலை."
        why_d_en = f"Evaluation of Option D: Distractor assessment."
        why_d_ta = f"ஆப்ஷன் D மதிப்பீடு: கூற்று தவறு ஆனால் காரணம் சரி என்ற நிலை."
        tip_en = "Verify if Reason directly provides the underlying constitutional justification for the Assertion."
        tip_ta = "கூற்றுக்கான சரியான அரசியலமைப்பு நியாயத்தை காரணம் நேரடியாக விளக்குகிறதா என்பதை சரிபார்க்கவும்."
        fact_en = "Under Sita Soren (2024), bribery does not enjoy immunity under Article 105(2)."
        fact_ta = "சீதா சோரன் (2024) தீர்ப்பின்படி லஞ்சத்திற்கு உறுப்பு 105(2)-ன் கீழ் விலக்களிப்பு கிடையாது."

        q = make_pp_q(
            qid, diff, "reasoning", subtopic,
            en_stem, ta_stem,
            en_a, en_a, en_b, en_b, en_c, en_c, en_d, en_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Apply locked randomizer
    balanced_questions = randomize_and_balance_dataset(questions, seed=206)

    keys = [q["correct_answer"] for q in balanced_questions]
    counts = Counter(keys)
    print("Part 2B PP Reasoning Key counts:", counts)
    assert len(balanced_questions) == 25
    for opt in ["A", "B", "C", "D"]:
        assert 6 <= counts[opt] <= 7

    out_path = "data/questions/polity/parliamentary_privileges_reasoning.json"
    alias_path = "data/questions/polity/parliamentary_privileges_assertion_reason.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_questions, f, indent=2, ensure_ascii=False)
    shutil.copyfile(out_path, alias_path)
    print(f"Successfully wrote 25 reasoning MCQs to {out_path} and {alias_path}")

if __name__ == "__main__":
    get_reasoning_questions()
