# -*- coding: utf-8 -*-
"""
Builder for Electoral Reforms Medium 50 MCQs (ER_M_001 to ER_M_050).
Strictly adheres to the 24-field TNPSC Nova AI schema.
"""

import json
import os
from er_mcq_helper import make_er_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

OUTPUT_PATH = os.path.join("data", "questions", "polity", "electoral_reforms_medium.json")

def get_medium_questions():
    qs = []

    # ER_M_001
    qs.append(make_er_q(
        qid="ER_M_001", diff="Medium", qtype="Single-Choice", subtopic="Candidate Disclosures",
        en_stem="In which case did the Supreme Court rule that a Returning Officer can reject the nomination paper of a candidate if columns in the Form 26 affidavit are left blank despite notice?",
        ta_stem="படிவம் 26 உறுதிமொழிப் பத்திரத்தில் உள்ள பத்திகளை அறிவிப்பு அளித்தும் நிரப்பாமல் காலியாக விட்டால், தேர்தல் நடத்தும் அலுவலர் வேட்புமனுவை நிராகரிக்கலாம் என்று உச்ச நீதிமன்றம் எந்த வழக்கில் தீர்ப்பளித்தது?",
        en_a="Resurgence India v. Election Commission of India (2013)", ta_a="ரீசர்ஜன்ஸ் இந்தியா எதிர் இந்திய தேர்தல் ஆணையம் (2013)",
        en_b="Lily Thomas v. Union of India (2013)", ta_b="லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (2013)",
        en_c="People's Union for Civil Liberties v. Union of India (2003)", ta_c="மக்கள் சிவில் உரிமைகள் சங்கம் எதிர் இந்திய ஒன்றியம் (2003)",
        en_d="Common Cause v. Union of India (1996)", ta_d="காமன் காஸ் எதிர் இந்திய ஒன்றியம் (1996)",
        correct_key="A",
        exp_en="In Resurgence India v. ECI (2013), the Supreme Court held that if a candidate fails to fill in all the blanks in Form 26 affidavit even after being reminded by the Returning Officer, their nomination paper is liable to be rejected, because an incomplete affidavit violates the voter's Right to Know.",
        exp_ta="ரீசர்ஜன்ஸ் இந்தியா எதிர் ECI (2013) வழக்கில், தேர்தல் நடத்தும் அலுவலர் நினைவூட்டிய பின்னரும் படிவம் 26 உறுதிமொழிப் பத்திரத்தில் ஏதேனும் பத்திகளை நிரப்பாமல் காலியாக விட்டால் அந்த வேட்புமனு நிராகரிக்கப்படத்தக்கது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        why_a_en="Correct. Resurgence India (2013) mandated rejection of nominations with blank columns in Form 26.",
        why_a_ta="சரியானது. படிவம் 26-ல் காலியிடங்கள் இருந்தால் வேட்புமனுவை நிராகரிக்க ரீசர்ஜன்ஸ் இந்தியா வழக்கு உத்தரவிட்டது.",
        why_b_en="Incorrect. Lily Thomas (2013) dealt with disqualification of convicted legislators.",
        why_b_ta="தவறானது. லில்லி தாமஸ் வழக்கு தண்டனை பெற்ற மக்கள் பிரதிநிதிகளின் தகுதிநீக்கம் பற்றியது.",
        why_c_en="Incorrect. PUCL (2003) invalidated the ordinance attempting to dilute candidate disclosures.",
        why_c_ta="தவறானது. PUCL (2003) வெளிப்படைத்தன்மையை நீர்த்துப்போகச் செய்த அவசரச் சட்டத்தை ரத்து செய்தது.",
        why_d_en="Incorrect. Common Cause (1996) dealt with political party expenditure accounts.",
        why_d_ta="தவறானது. காமன் காஸ் (1996) கட்சிகளின் தேர்தல் செலவுக் கணக்குகள் பற்றியது.",
        tip_en="A candidate cannot write 'N/A' or leave blanks; they must state 'Nil' or 'Not Applicable' or 'Not Known'.",
        tip_ta="வேட்பாளர்கள் எதையும் காலியாக விடக்கூடாது; எதுவும் இல்லை என்றால் 'Nil' அல்லது 'Not Known' என்று குறிப்பிட வேண்டும்.",
        fact_en="This verdict closed a major loophole where candidates evaded disclosing criminal cases by simply leaving fields blank.",
        fact_ta="குற்றப்பின்னணியை மறைக்க வேட்பாளர்கள் பத்திகளை காலியாக விடும் தந்திரத்திற்கு இத்தீர்ப்பு முற்றுப்புள்ளி வைத்தது.",
        tags=["Resurgence India 2013", "Form 26", "Nomination Rejection"]
    ))

    # ER_M_002
    qs.append(make_er_q(
        qid="ER_M_002", diff="Medium", qtype="Single-Choice", subtopic="Candidate Disclosures",
        en_stem="In Lok Prahari v. Union of India (2018), what additional mandatory disclosure was directed by the Supreme Court to be included in candidate affidavits?",
        ta_stem="லோக் பிரஹாரி எதிர் இந்திய ஒன்றியம் (2018) வழக்கில், வேட்பாளர் உறுதிமொழிப் பத்திரத்தில் கூடுதலாக சேர்க்கப்பட வேண்டும் என்று உச்ச நீதிமன்றம் உத்தரவிட்ட கட்டாயத் தகவல் எது?",
        en_a="Sources of income of the candidate, their spouse, and dependents, and contracts with government", ta_a="வேட்பாளர், அவரது மனைவி/கணவர் மற்றும் சார்ந்திருப்போரின் வருமான ஆதாரங்கள் மற்றும் அரசுடனான ஒப்பந்தங்கள்",
        en_b="Complete biometric data and DNA profiling of family members", ta_b="குடும்ப உறுப்பினர்களின் முழு பயோமெட்ரிக் மற்றும் டிஎன்ஏ விவரங்கள்",
        en_c="All social media passwords and email credentials", ta_c="அனைத்து சமூக ஊடக கடவுச்சொற்கள் மற்றும் மின்னஞ்சல் விவரங்கள்",
        en_d="List of all relatives residing outside the country", ta_d="வெளிநாட்டில் வசிக்கும் அனைத்து உறவினர்களின் பட்டியல்",
        correct_key="A",
        exp_en="In Lok Prahari v. Union of India (2018), the Supreme Court directed the Union Government to amend Form 26 to mandate that candidates must disclose their sources of income, the sources of income of their spouse and dependents, and details of contracts entered into by them or their family/firms with the government.",
        exp_ta="லோக் பிரஹாரி வழக்கில் (2018), வேட்பாளர், அவரது துணைவர் மற்றும் அவரைச் சார்ந்திருப்போரின் வருமான ஆதாரங்களையும், அவர்கள் அரசுடன் செய்துள்ள ஒப்பந்த விவரங்களையும் படிவம் 26-ல் வெளிப்படுத்துவதைக் கட்டாயமாக்க உச்ச நீதிமன்றம் உத்தரவிட்டது.",
        why_a_en="Correct. Disclosure of sources of income and government contracts.",
        why_a_ta="சரியானது. வருமான ஆதாரங்கள் மற்றும் அரசு ஒப்பந்தங்களை வெளிப்படுத்துதல்.",
        why_b_en="Incorrect. Biometric/DNA profiling is not required.",
        why_b_ta="தவறானது. பயோமெட்ரிக் விவரங்கள் கோரப்படுவதில்லை.",
        why_c_en="Incorrect. Social media credentials are not disclosed.",
        why_c_ta="தவறானது. சமூக ஊடக கடவுச்சொற்கள் கோரப்படுவதில்லை.",
        why_d_en="Incorrect. Foreign relative lists are not required.",
        why_d_ta="தவறானது. வெளிநாட்டு உறவினர்கள் பட்டியல் அவசியமில்லை.",
        tip_en="This was aimed at checking the disproportionate asset growth of lawmakers while in office.",
        tip_ta="பதவியில் இருக்கும் போது மக்கள் பிரதிநிதிகளின் சொத்துக்கள் அபரிமிதமாக உயர்வதைக் கட்டுப்படுத்த இது கொண்டுவரப்பட்டது.",
        fact_en="Following this, the Conduct of Elections Rules, 1961 were amended in February 2019 to incorporate these fields into Form 26.",
        fact_ta="இத்தீர்ப்பைத் தொடர்ந்து 2019 பிப்ரவரியில் தேர்தல் நடத்தை விதிகள் திருத்தப்பட்டு படிவம் 26-ல் இப்பிரிவுகள் சேர்க்கப்பட்டன.",
        tags=["Lok Prahari 2018", "Sources of Income", "Form 26 Amendment"]
    ))

    # ER_M_003
    qs.append(make_er_q(
        qid="ER_M_003", diff="Medium", qtype="Single-Choice", subtopic="Criminalisation of Politics",
        en_stem="In Public Interest Foundation v. Union of India (2018), what timeline was mandated for political parties and candidates to publish criminal antecedents in widely circulated newspapers and on websites?",
        ta_stem="பொது நல அறக்கட்டளை (Public Interest Foundation) எதிர் இந்திய ஒன்றியம் (2018) வழக்கில், அரசியல் கட்சிகளும் வேட்பாளர்களும் குற்றப்பின்னணி விவரங்களை செய்தித்தாள்கள் மற்றும் இணையதளத்தில் வெளியிட நிர்ணயிக்கப்பட்ட விதிமுறை என்ன?",
        en_a="At least thrice in widely circulated newspapers and on TV channels during the campaign period", ta_a="பிரச்சார காலத்தில் பரவலாக புழக்கத்தில் உள்ள செய்தித்தாள்கள் மற்றும் தொலைக்காட்சிகளில் குறைந்தது 3 முறை வெளியிட வேண்டும்",
        en_b="Only once on the day after the election results are declared", ta_b="தேர்தல் முடிவுகள் வெளியான மறுநாள் ஒருமுறை மட்டும்",
        en_c="Weekly for 6 months prior to the election announcement", ta_c="தேர்தல் அறிவிப்புக்கு முன் 6 மாதங்களுக்கு வாரம் ஒருமுறை",
        en_d="Only if a rival candidate files a formal objection", ta_d="எதிர் வேட்பாளர் எழுத்துப்பூர்வ ஆட்சேபனை தெரிவித்தால் மட்டுமே",
        correct_key="A",
        exp_en="A 5-judge Constitution Bench in Public Interest Foundation (2018) directed that candidates and political parties fielding them must publish criminal antecedents at least thrice in widely circulated national and local newspapers and electronic media between nomination and polling.",
        exp_ta="2018-ல் 5 நீதிபதிகள் கொண்ட அரசியல் சாசன அமர்வு, வேட்புமனு தாக்கல் செய்வதற்கும் வாக்குப்பதிவுக்கும் இடைப்பட்ட காலத்தில் வேட்பாளரின் குற்றப்பின்னணி விவரங்களை முன்னணி நாளிதழ்கள் மற்றும் தொலைக்காட்சிகளில் குறைந்தது 3 முறை விளம்பரமாக வெளியிட வேண்டும் என்று உத்தரவிட்டது.",
        why_a_en="Correct. At least thrice in print and electronic media.",
        why_a_ta="சரியானது. அச்சு மற்றும் காட்சி ஊடகங்களில் குறைந்தது 3 முறை வெளியிட வேண்டும்.",
        why_b_en="Incorrect. Must be published before the poll, not after results.",
        why_b_ta="தவறானது. தேர்தலுக்கு முன்பே வெளியிட வேண்டும்.",
        why_c_en="Incorrect. 6-month prior publication is not the rule.",
        why_c_ta="தவறானது. 6 மாத காலக்கெடு இல்லை.",
        why_d_en="Incorrect. Mandatory for all candidates with criminal records, not dependent on objections.",
        why_d_ta="தவறானது. ஆட்சேபனையின்றி தானாகவே வெளியிட வேண்டும்.",
        tip_en="ECI formulated Form C1 (for candidate) and Form C2 (for party) to standardize these publications.",
        tip_ta="இவ்விவரங்களை வெளியிட தேர்தல் ஆணையம் படிவம் C1 (வேட்பாளருக்கு) மற்றும் படிவம் C2 (கட்சிக்கு) ஆகியவற்றை உருவாக்கியது.",
        fact_en="Brajesh Singh v. Sunil Arora (2021) added that parties must publish this within 48 hours of selecting the candidate.",
        fact_ta="பிரஜேஷ் சிங் (2021) வழக்கில், வேட்பாளர் தேர்வு செய்யப்பட்ட 48 மணி நேரத்திற்குள் வெளியிட வேண்டும் என மேலும் காலக்கெடு விதிக்கப்பட்டது.",
        tags=["Public Interest Foundation 2018", "Criminal Antecedents", "Publication Mandate"]
    ))

    # ER_M_004
    qs.append(make_er_q(
        qid="ER_M_004", diff="Medium", qtype="Single-Choice", subtopic="Criminalisation of Politics",
        en_stem="In Brajesh Singh v. Sunil Arora (2021), what strict timeline did the Supreme Court lay down for political parties to publish the criminal antecedents of a selected candidate?",
        ta_stem="பிரஜேஷ் சிங் எதிர் சுனில் அரோரா (2021) வழக்கில், தேர்வு செய்யப்பட்ட வேட்பாளரின் குற்றப்பின்னணி விவரங்களை அரசியல் கட்சிகள் வெளியிட உச்ச நீதிமன்றம் விதித்த கடுமையான காலக்கெடு என்ன?",
        en_a="Within 48 hours of candidate selection or not less than 2 weeks before the first date for filing nominations", ta_a="வேட்பாளர் தேர்வு செய்யப்பட்ட 48 மணி நேரத்திற்குள் அல்லது வேட்புமனு தொடங்குவதற்கு குறைந்தது 2 வாரங்களுக்கு முன்",
        en_b="Within 10 days after the counting of votes", ta_b="வாக்கு எண்ணிக்கைக்குப் பிறகு 10 நாட்களுக்குள்",
        en_c="Within 24 hours of casting the vote", ta_c="வாக்களித்த 24 மணி நேரத்திற்குள்",
        en_d="Within 30 days of the gazette notification", ta_d="அரசிதழ் அறிவிக்கைக்குப் பிறகு 30 நாட்களுக்குள்",
        correct_key="A",
        exp_en="In Brajesh Singh v. Sunil Arora (2021), the Supreme Court modified its earlier directions, mandating that political parties must publish candidate details in newspapers, social media, and website within 48 hours of selection or not less than two weeks before the first date for filing nominations.",
        exp_ta="பிரஜேஷ் சிங் வழக்கில் (2021), உச்ச நீதிமன்றம் தனது உத்தரவை மாற்றியமைத்து, வேட்பாளர் தேர்ந்தெடுக்கப்பட்ட 48 மணி நேரத்திற்குள் அல்லது வேட்புமனு தொடங்குவதற்கு குறைந்தது 2 வாரங்களுக்கு முன்பாக குற்றப்பின்னணியை வெளியிட வேண்டும் எனக் கட்டளையிட்டது.",
        why_a_en="Correct. Within 48 hours of selection or not less than 2 weeks before first date of nomination.",
        why_a_ta="சரியானது. தேர்வு செய்யப்பட்ட 48 மணி நேரத்திற்குள் அல்லது மனு தாக்கல் தொடங்குவதற்கு 2 வாரங்களுக்கு முன்.",
        why_b_en="Incorrect. Counting is post-election.",
        why_b_ta="தவறானது. தேர்தல் முடிந்த பின் அல்ல.",
        why_c_en="Incorrect. Voting day is irrelevant to nomination publication.",
        why_c_ta="தவறானது. வாக்குப்பதிவு தினத்திற்கு தொடர்பில்லை.",
        why_d_en="Incorrect. 30 days is too late.",
        why_d_ta="தவறானது. 30 நாட்கள் மிகவும் தாமதமானது.",
        tip_en="The court also fined several major national and state political parties for contempt in this case.",
        tip_ta="இவ்வழக்கில் நீதிமன்ற உத்தரவை மீறியதற்காக பல முன்னணி தேசிய மற்றும் மாநிலக் கட்சிகளுக்கு உச்ச நீதிமன்றம் நீதிமன்ற அவமதிப்பு அபராதம் விதித்தது.",
        fact_en="Parties must also submit a compliance report to the ECI within 72 hours of selecting such a candidate.",
        fact_ta="அத்தகைய வேட்பாளரைத் தேர்வு செய்த 72 மணி நேரத்திற்குள் ECI-க்கு இணக்க அறிக்கை சமர்ப்பிக்க வேண்டும்.",
        tags=["Brajesh Singh 2021", "48 Hours Mandate", "Criminal Records"]
    ))

    # ER_M_005
    qs.append(make_er_q(
        qid="ER_M_005", diff="Medium", qtype="Single-Choice", subtopic="VVPAT Verification",
        en_stem="In N. Chandrababu Naidu v. Union of India (April 2019), what quota of VVPAT slip verification per assembly constituency/segment was mandated by the Supreme Court?",
        ta_stem="என். சந்திரபாபு நாயுடு எதிர் இந்திய ஒன்றியம் (ஏப்ரல் 2019) வழக்கில், ஒவ்வொரு சட்டமன்றத் தொகுதிக்கும் எத்தனை வாக்குச்சாவடிகளில் VVPAT சீட்டுகளை எண்ணி சரிபார்க்க உச்ச நீதிமன்றம் உத்தரவிட்டது?",
        en_a="5 polling stations per assembly constituency/segment", ta_a="ஒவ்வொரு சட்டமன்றத் தொகுதிக்கும் 5 வாக்குச்சாவடிகள்",
        en_b="1 polling station per assembly constituency/segment", ta_b="ஒவ்வொரு சட்டமன்றத் தொகுதிக்கும் 1 வாக்குச்சாவடி",
        en_c="50% of all polling stations", ta_c="அனைத்து வாக்குச்சாவடிகளிலும் 50%",
        en_d="10 polling stations per parliamentary constituency", ta_d="நாடாளுமன்றத் தொகுதிக்கு 10 வாக்குச்சாவடிகள்",
        correct_key="A",
        exp_en="In N. Chandrababu Naidu (2019), the Supreme Court bench headed by CJI Ranjan Gogoi increased the random physical verification of VVPAT slips from 1 polling station per assembly constituency/segment to 5 polling stations per assembly constituency/segment.",
        exp_ta="சந்திரபாபு நாயுடு வழக்கில் (2019), தலைமை நீதிபதி ரஞ்சன் கோகோய் தலைமையிலான அமர்வு, ஒரு தொகுதிக்கு 1 வாக்குச்சாவடி என்றிருந்த VVPAT சரிபார்ப்பை, சட்டமன்றத் தொகுதிக்கு தலா 5 வாக்குச்சாவடிகள் என உயர்த்தி உத்தரவிட்டது.",
        why_a_en="Correct. 5 polling stations per assembly constituency/segment.",
        why_a_ta="சரியானது. சட்டமன்றத் தொகுதிக்கு தலா 5 வாக்குச்சாவடிகள்.",
        why_b_en="Incorrect. 1 polling station was the initial administrative guideline of ECI before the court increased it.",
        why_b_ta="தவறானது. 1 வாக்குச்சாவடி என்பது ECI-ன் முந்தைய வழிகாட்டுதல்.",
        why_c_en="Incorrect. Petitioners requested 50%, but the court rejected that request.",
        why_c_ta="தவறானது. மனுதாரர்கள் 50% கோரினர், ஆனால் நீதிமன்றம் அதை ஏற்கவில்லை.",
        why_d_en="Incorrect. The unit of count is assembly segment, not parliamentary constituency as a whole.",
        why_d_ta="தவறானது. சட்டமன்றத் தொகுதியே இதற்கான அடிப்படை அலகாகும்.",
        tip_en="For a parliamentary constituency with 6 assembly segments, 6 x 5 = 30 polling stations have their VVPAT slips physically counted.",
        tip_ta="6 சட்டமன்றத் தொகுதிகள் கொண்ட ஒரு மக்களவைத் தொகுதியில் 6 x 5 = 30 வாக்குச்சாவடிகளில் VVPAT சீட்டுகள் எண்ணப்படும்.",
        fact_en="Rule 56D of Conduct of Elections Rules allows a candidate to request counting of VVPAT slips in any station.",
        fact_ta="விதி 56D-ன் படி வேட்பாளர் எந்த ஒரு வாக்குச்சாவடியின் VVPAT சீட்டுகளையும் எண்ணக் கோரி மனு செய்யலாம்.",
        tags=["Chandrababu Naidu 2019", "VVPAT Verification", "5 Polling Stations"]
    ))

    # ER_M_006
    qs.append(make_er_q(
        qid="ER_M_006", diff="Medium", qtype="Single-Choice", subtopic="VVPAT Verification",
        en_stem="In the Association for Democratic Reforms v. ECI (April 2024) judgment regarding EVM-VVPAT integrity, what key safeguard was directed by the Supreme Court?",
        ta_stem="EVM-VVPAT நம்பகத்தன்மை குறித்த ADR எதிர் ECI (ஏப்ரல் 2024) தீர்ப்பில், உச்ச நீதிமன்றம் வழங்கிய முக்கிய பாதுகாப்பு உத்தரவு எது?",
        en_a="Symbol Loading Units (SLUs) must be sealed in containers and preserved in strongrooms for 45 days post-results", ta_a="சின்னம் பதிவேற்றும் கருவிகள் (SLU) சீலிடப்பட்டு தேர்தல் முடிவுக்குப் பின் 45 நாட்கள் பாதுகாப்பு அறைகளில் வைக்கப்பட வேண்டும்",
        en_b="Return to 100% paper ballots for all future general elections", ta_b="எதிர்கால அனைத்து பொதுத்தேர்தல்களிலும் 100% காகித வாக்குச்சீட்டு முறைக்கு திரும்புதல்",
        en_c="Physical counting of 100% VVPAT paper slips in all constituencies", ta_c="அனைத்து தொகுதிகளிலும் 100% VVPAT காகித சீட்டுகளை கட்டாயம் எண்ணுதல்",
        en_d="Deployment of foreign software auditors during the polling process", ta_d="வாக்குப்பதிவின் போது வெளிநாட்டு மென்பொருள் தணிக்கையாளர்களை நியமித்தல்",
        correct_key="A",
        exp_en="On 26 April 2024, the Supreme Court bench (Justices Sanjiv Khanna and Dipankar Datta) rejected 100% VVPAT counting, but directed that: (1) SLUs must be sealed and stored in strongrooms for 45 days, and (2) candidates finishing 2nd or 3rd can seek micro-controller verification of 5% of EVMs per assembly segment upon paying expenses.",
        exp_ta="2024 ஏப்ரல் 26 அன்று, உச்ச நீதிமன்றம் 100% VVPAT சீட்டுகளை எண்ணும் கோரிக்கையை நிராகரித்தது; எனினும் (1) SLU கருவிகள் சீலிடப்பட்டு 45 நாட்கள் காப்பகத்தில் வைக்கப்பட வேண்டும், (2) 2-வது மற்றும் 3-வது இடம் பிடித்த வேட்பாளர்கள் கட்டணம் செலுத்தி 5% EVM நுண்கட்டுப்படுத்திகளை (Microcontrollers) சரிபார்க்கக் கோரலாம் என உத்தரவிட்டது.",
        why_a_en="Correct. Sealing and preservation of SLUs for 45 days.",
        why_a_ta="சரியானது. SLU கருவிகளை சீலிட்டு 45 நாட்கள் பாதுகாக்க உத்தரவிட்டது.",
        why_b_en="Incorrect. Supreme Court explicitly rejected returning to paper ballots.",
        why_b_ta="தவறானது. காகித வாக்குச்சீட்டு முறைக்கு திரும்புவதை உச்ச நீதிமன்றம் திட்டவட்டமாக மறுத்தது.",
        why_c_en="Incorrect. 100% VVPAT counting was rejected as regressive and unnecessary.",
        why_c_ta="தவறானது. 100% VVPAT எண்ணும் கோரிக்கை நிராகரிக்கப்பட்டது.",
        why_d_en="Incorrect. No foreign auditors are allowed.",
        why_d_ta="தவறானது. வெளிநாட்டு தணிக்கையாளர்களுக்கு அனுமதியில்லை.",
        tip_en="45 days corresponds to the statutory deadline for filing an Election Petition under Section 81 of RPA 1951.",
        tip_ta="45 நாட்கள் என்பது மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 81-ன் கீழ் தேர்தல் மனு தாக்கல் செய்வதற்கான காலக்கெடுவாகும்.",
        fact_en="The court affirmed that EVMs are standalone machines with OTP firmware that cannot be hacked remotely.",
        fact_ta="EVM இயந்திரங்கள் இணையத் தொடர்பற்ற தனியானவை மற்றும் ஹேக் செய்ய முடியாதவை என்பதை நீதிமன்றம் மீண்டும் உறுதிப்படுத்தியது.",
        tags=["Supreme Court 2024", "VVPAT Verification", "SLU Sealing"]
    ))

    # ER_M_007
    qs.append(make_er_q(
        qid="ER_M_007", diff="Medium", qtype="Single-Choice", subtopic="VVPAT Verification",
        en_stem="Under the Supreme Court's April 2024 ruling, candidates who secure which positions in an election can request engineering verification of the EVM microcontrollers?",
        ta_stem="உச்ச நீதிமன்றத்தின் ஏப்ரல் 2024 தீர்ப்பின்படி, தேர்தலில் எந்த இடங்களைப் பெற்ற வேட்பாளர்கள் EVM நுண்கட்டுப்படுத்திகளை பொறியியல் சரிபார்ப்புக்கு உட்படுத்தக் கோரலாம்?",
        en_a="Candidates placed second or third (runners-up)", ta_a="இரண்டாவது அல்லது மூன்றாவது இடம் பிடித்த வேட்பாளர்கள்",
        en_b="Any contesting candidate regardless of votes secured", ta_b="பெற்ற வாக்குகளைப் பொருட்படுத்தாமல் போட்டியிட்ட எந்த ஒரு வேட்பாளரும்",
        en_c="Only the candidate who won the election", ta_c="தேர்தலில் வெற்றி பெற்ற வேட்பாளர் மட்டுமே",
        en_d="Only independent candidates who lost their deposit", ta_d="வைப்புத்தொகையை இழந்த சுயேச்சை வேட்பாளர்கள் மட்டுமே",
        correct_key="A",
        exp_en="In ADR v. ECI (2024), the Supreme Court ruled that candidates placed 2nd or 3rd behind the highest polled candidate can identify and seek verification of the burnt microcontroller memory of 5% of EVMs per assembly segment, by submitting a written request within 7 days of results.",
        exp_ta="2024 ADR தீர்ப்பில், வெற்றி பெற்ற வேட்பாளருக்கு அடுத்தபடியாக 2-வது அல்லது 3-வது இடத்தைப் பிடித்த வேட்பாளர்கள், முடிவுகள் வெளியான 7 நாட்களுக்குள் மனு அளித்து, ஒரு தொகுதிக்கு 5% EVM நுண்கட்டுப்படுத்திகளை சரிபார்க்கக் கோரலாம் என நீதிமன்றம் உத்தரவிட்டது.",
        why_a_en="Correct. Restricted to 2nd and 3rd placed candidates to prevent frivolous abuse.",
        why_a_ta="சரியானது. வீண் புகார்களைத் தவிர்க்க 2-வது மற்றும் 3-வது இடம்பிடித்த வேட்பாளர்களுக்கு மட்டுமே இவ்வாய்ப்பு.",
        why_b_en="Incorrect. Not open to all candidates.",
        why_b_ta="தவறானது. அனைத்து வேட்பாளர்களுக்கும் அல்ல.",
        why_c_en="Incorrect. The winning candidate has no need to challenge.",
        why_c_ta="தவறானது. வெற்றி பெற்றவர் கோர வேண்டிய அவசியமில்லை.",
        why_d_en="Incorrect. Independent candidates with lost deposits cannot demand this.",
        why_d_ta="தவறானது. வைப்புத்தொகை இழந்தவர்கள் கோர முடியாது.",
        tip_en="The request must be made within 7 days of the declaration of results.",
        tip_ta="தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட 7 நாட்களுக்குள் இக்கோரிக்கையை முன்வைக்க வேண்டும்.",
        fact_en="If the verification detects any tampering, the inspection fee is fully refunded to the candidate.",
        fact_ta="சரிபார்ப்பில் ஏதேனும் முறைகேடு கண்டறியப்பட்டால், வேட்பாளர் செலுத்திய ஆய்வுக்கட்டணம் முழுமையாகத் திருப்பித் தரப்படும்.",
        tags=["EVM Verification", "2nd and 3rd Candidate", "Supreme Court 2024"]
    ))

    # ER_M_008
    qs.append(make_er_q(
        qid="ER_M_008", diff="Medium", qtype="Single-Choice", subtopic="Electoral Bonds Judgment",
        en_stem="Which amendment made by the Finance Act, 2017 to the Companies Act, 2013 was struck down by the Supreme Court in the 2024 Electoral Bonds verdict?",
        ta_stem="2024 தேர்தல் பத்திரங்கள் தீர்ப்பில், 2017 நிதிச் சட்டத்தால் கம்பெனிகள் சட்டம் 2013-ல் செய்யப்பட்ட எந்த திருத்தத்தை உச்ச நீதிமன்றம் ரத்து செய்தது?",
        en_a="Removal of the cap of 7.5% of net profit on corporate donations and removal of company-wise disclosure", ta_a="நிறுவன நன்கொடைகளுக்கான 7.5% நிகர லாப வரம்பை நீக்கியது மற்றும் நிறுவனம் வாரியான வெளிப்படைத்தன்மையை நீக்கியது",
        en_b="Mandatory requirement to register all companies under Section 8", ta_b="அனைத்து நிறுவனங்களையும் பிரிவு 8-ன் கீழ் பதிவு செய்வதை கட்டாயமாக்கியது",
        en_c="Imposition of a 50% windfall tax on corporate political contributions", ta_c="அரசியல் நன்கொடைகள் மீது 50% கூடுதல் வரி விதித்தது",
        en_d="Prohibition on Indian companies from employing foreign directors", ta_d="இந்திய நிறுவனங்கள் வெளிநாட்டு இயக்குநர்களை நியமிக்க விதித்த தடை",
        correct_key="A",
        exp_en="The Supreme Court in ADR v. UOI (2024) held that the amendment to Section 182(1) of the Companies Act, 2013—which removed the ceiling of 7.5% of average net profits for corporate donations and allowed loss-making / shell companies to donate unlimited amounts anonymously—was manifestly arbitrary and unconstitutional.",
        exp_ta="2024 ADR தீர்ப்பில், நிறுவனங்கள் தங்களது சராசரி நிகர லாபத்தில் 7.5% மட்டுமே நன்கொடை அளிக்கலாம் என்ற உச்சவரம்பை நீக்கியதையும், நஷ்டத்தில் இயங்கும் போலி நிறுவனங்கள் வரம்பற்ற நன்கொடை வழங்க அனுமதித்த கம்பெனிகள் சட்டம் பிரிவு 182 திருத்தத்தையும் உச்ச நீதிமன்றம் ரத்து செய்தது.",
        why_a_en="Correct. Removal of the 7.5% cap and company disclosure was struck down.",
        why_a_ta="சரியானது. 7.5% லாப வரம்பை நீக்கிய திருத்தத்தை உச்ச நீதிமன்றம் ரத்து செய்தது.",
        why_b_en="Incorrect. Section 8 deals with non-profit companies.",
        why_b_ta="தவறானது. பிரிவு 8 தொண்டு நிறுவனங்கள் பற்றியது.",
        why_c_en="Incorrect. No windfall tax was imposed.",
        why_c_ta="தவறானது. கூடுதல் வரி எதுவும் விதிக்கப்படவில்லை.",
        why_d_en="Incorrect. Foreign directors was not the issue.",
        why_d_ta="தவறானது. வெளிநாட்டு இயக்குநர்கள் பிரச்சனை அல்ல.",
        tip_en="Section 182 originally prevented loss-making companies from funneling black money into politics.",
        tip_ta="பிரிவு 182 முன்னதாக நஷ்டத்தில் இயங்கும் நிறுவனங்கள் கறுப்புப் பணத்தை அரசியலில் நுழைப்பதைத் தடுத்து வந்தது.",
        fact_en="The court held that treating profit-making and loss-making companies equally for unlimited political contributions violates Article 14.",
        fact_ta="லாபம் ஈட்டும் மற்றும் நஷ்டமடையும் நிறுவனங்களை ஒரே மாதிரி கருதி வரம்பற்ற நன்கொடையை அனுமதிப்பது சரத்து 14-க்கு எதிரானது என நீதிமன்றம் கூறியது.",
        tags=["Electoral Bonds", "Section 182", "Companies Act", "Corporate Funding"]
    ))

    # ER_M_009
    qs.append(make_er_q(
        qid="ER_M_009", diff="Medium", qtype="Single-Choice", subtopic="Political Party Donations",
        en_stem="Under Section 29C of the Representation of the People Act, 1951, political parties must prepare and submit an annual contribution report to the ECI for all individual donations exceeding what monetary threshold?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 29C-ன் கீழ், அரசியல் கட்சிகள் எந்தத் தொகைக்கு மேல் பெறப்படும் தனிநபர் நன்கொடைகள் அனைத்திற்கும் ஆண்டறிக்கை தயாரித்து தேர்தல் ஆணையத்திடம் சமர்ப்பிக்க வேண்டும்?",
        en_a="₹20,000", ta_a="₹20,000",
        en_b="₹2,000", ta_b="₹2,000",
        en_c="₹50,000", ta_c="₹50,000",
        en_d="₹1,00,000", ta_d="₹1,00,000",
        correct_key="A",
        exp_en="Section 29C(1) of RPA 1951 requires the treasurer of every political party to prepare a report in respect of each contribution exceeding ₹20,000 received from any person or company in a financial year and submit it to the ECI to claim tax exemption under Section 13A of the Income Tax Act.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 29C(1)-ன் படி, ஒரு நிதியாண்டில் எந்தவொரு நபர் அல்லது நிறுவனத்திடமிருந்தும் ₹20,000-க்கு மேல் பெறப்படும் அனைத்து நன்கொடைகளுக்கும் அரசியல் கட்சிகள் அறிக்கை தயாரித்து ECI-யிடம் சமர்ப்பிக்க வேண்டும்; அப்போதுதான் வருமான வரி விலக்கு பெற முடியும்.",
        why_a_en="Correct. ₹20,000 is the statutory reporting threshold under Section 29C of RPA 1951.",
        why_a_ta="சரியானது. பிரிவு 29C-ன் கீழான அறிக்கை வரம்பு ₹20,000 ஆகும்.",
        why_b_en="Incorrect. ₹2,000 is the cash donation limit introduced in the 2017 Union Budget under Section 13A of IT Act.",
        why_b_ta="தவறானது. ₹2,000 என்பது ரொக்கமாக நன்கொடை பெறுவதற்கான உச்சவரம்பாகும்.",
        why_c_en="Incorrect. ₹50,000 is incorrect.",
        why_c_ta="தவறானது. ₹50,000 தவறானது.",
        why_d_en="Incorrect. ₹1,00,000 is incorrect.",
        why_d_ta="தவறானது. ₹1,00,000 தவறானது.",
        tip_en="Do not confuse: Maximum anonymous CASH donation allowed = ₹2,000; Threshold for reporting donor name under Section 29C = ₹20,000.",
        tip_ta="குழப்ப வேண்டாம்: ரொக்கமாகப் பெறக்கூடிய அதிகபட்ச வரம்பு = ₹2,000; ECI-க்கு பெயர் விவரம் தெரிவிக்க வேண்டிய வரம்பு = ₹20,000.",
        fact_en="Parties that fail to submit this report before the due date for filing Income Tax return lose their 100% tax exemption under Section 13A.",
        fact_ta="வருமான வரி தாக்கல் செய்யும் தேதிக்குள் இந்த அறிக்கையை சமர்ப்பிக்கத் தவறினால் பிரிவு 13A-ன் கீழான 100% வரிவிலக்கு ரத்தாகும்.",
        tags=["Section 29C", "₹20000 Threshold", "Donation Reporting"]
    ))

    # ER_M_010
    qs.append(make_er_q(
        qid="ER_M_010", diff="Medium", qtype="Single-Choice", subtopic="Political Funding",
        en_stem="What is the maximum limit on anonymous cash donations that a registered political party can accept from any single person under Section 13A of the Income Tax Act (amended in 2017)?",
        ta_stem="2017-ல் திருத்தப்பட்ட வருமான வரிச் சட்டம் பிரிவு 13A-ன் கீழ், ஒரு பதிவு செய்யப்பட்ட அரசியல் கட்சி ஒரு நபரிடமிருந்து ரொக்கமாகப் பெறக்கூடிய அதிகபட்ச நன்கொடை வரம்பு என்ன?",
        en_a="₹2,000", ta_a="₹2,000",
        en_b="₹20,000", ta_b="₹20,000",
        en_c="₹5,000", ta_c="₹5,000",
        en_d="₹10,000", ta_d="₹10,000",
        correct_key="A",
        exp_en="By the Finance Act, 2017, Section 13A of the Income Tax Act was amended to reduce the ceiling on cash donations from ₹20,000 to ₹2,000 per person, mandating that any donation exceeding ₹2,000 must be received through cheque, bank draft, electronic clearing system, or electoral bonds (now struck down).",
        exp_ta="2017 நிதிச் சட்டத்தின் மூலம், வருமான வரிச் சட்டம் பிரிவு 13A திருத்தப்பட்டு, ஒருவர் ரொக்கமாக அளிக்கக்கூடிய நன்கொடை உச்சவரம்பு ₹20,000-லிருந்து ₹2,000 ஆகக் குறைக்கப்பட்டது. ₹2,000-க்கு மேற்பட்ட தொகையை காசோலை அல்லது வங்கிப் பரிவர்த்தனை மூலம் மட்டுமே பெற முடியும்.",
        why_a_en="Correct. ₹2,000 is the maximum cash donation limit.",
        why_a_ta="சரியானது. ரொக்க நன்கொடைக்கான உச்சவரம்பு ₹2,000.",
        why_b_en="Incorrect. ₹20,000 was the previous cash limit before 2017.",
        why_b_ta="தவறானது. 2017-க்கு முன்பு ₹20,000 ஆக இருந்தது.",
        why_c_en="Incorrect. ₹5,000 is incorrect.",
        why_c_ta="தவறானது. ₹5,000 தவறானது.",
        why_d_en="Incorrect. ₹10,000 is incorrect.",
        why_d_ta="தவறானது. ₹10,000 தவறானது.",
        tip_en="ECI has further recommended that cash donations to political parties should be completely banned.",
        tip_ta="அரசியல் கட்சிகளுக்கு ரொக்க நன்கொடைகளை முழுமையாக தடை செய்ய வேண்டும் என்று தேர்தல் ஆணையம் பரிந்துரைத்துள்ளது.",
        fact_en="This reform was introduced in the 2017 Union Budget presented by Finance Minister Arun Jaitley.",
        fact_ta="இச்சீர்திருத்தம் 2017 மத்திய பட்ஜெட்டில் நிதி அமைச்சர் அருண் ஜேட்லியால் அறிவிக்கப்பட்டது.",
        tags=["Cash Donation Limit", "₹2000", "Section 13A"]
    ))

    # ER_M_011
    qs.append(make_er_q(
        qid="ER_M_011", diff="Medium", qtype="Single-Choice", subtopic="Election Expenditure Limits",
        en_stem="Following the 2022 revision of election expenditure limits, what is the maximum ceiling on campaign expenditure for a Lok Sabha candidate in bigger states (like UP, Maharashtra, Bihar, Tamil Nadu)?",
        ta_stem="2022 தேர்தல் செலவு உச்சவரம்பு திருத்தத்திற்குப் பிறகு, பெரிய மாநிலங்களில் (உ.பி., மகாராஷ்டிரா, தமிழ்நாடு போன்றவை) ஒரு மக்களவை வேட்பாளர் செய்யக்கூடிய அதிகபட்ச தேர்தல் பிரச்சார செலவு வரம்பு என்ன?",
        en_a="₹95 Lakhs", ta_a="₹95 லட்சம்",
        en_b="₹70 Lakhs", ta_b="₹70 லட்சம்",
        en_c="₹40 Lakhs", ta_c="₹40 லட்சம்",
        en_d="₹1.50 Crore", ta_d="₹1.50 கோடி",
        correct_key="A",
        exp_en="In January 2022, the Ministry of Law and Justice amended Rule 90 of the Conduct of Elections Rules, 1961, enhancing the election expenditure ceiling for Lok Sabha candidates in bigger states from ₹70 Lakhs to ₹95 Lakhs (and from ₹54 Lakhs to ₹75 Lakhs in smaller states and UTs).",
        exp_ta="2022 ஜனவரியில் தேர்தல் நடத்தை விதிகள் 1961-ன் விதி 90 திருத்தப்பட்டு, பெரிய மாநிலங்களில் போட்டியிடும் மக்களவை வேட்பாளரின் தேர்தல் செலவு வரம்பு ₹70 லட்சத்திலிருந்து ₹95 லட்சமாக உயர்த்தப்பட்டது (சிறிய மாநிலங்களில் ₹75 லட்சம்).",
        why_a_en="Correct. ₹95 Lakhs for bigger states in Lok Sabha elections.",
        why_a_ta="சரியானது. மக்களவைத் தேர்தலில் பெரிய மாநிலங்களுக்கு ₹95 லட்சம்.",
        why_b_en="Incorrect. ₹70 Lakhs was the earlier limit set in 2014.",
        why_b_ta="தவறானது. ₹70 லட்சம் என்பது 2014-ல் நிர்ணயிக்கப்பட்ட முந்தைய வரம்பு.",
        why_c_en="Incorrect. ₹40 Lakhs is the enhanced limit for State Legislative Assembly in bigger states.",
        why_c_ta="தவறானது. ₹40 லட்சம் என்பது பெரிய மாநில சட்டசபைத் தேர்தலுக்கான வரம்பு.",
        why_d_en="Incorrect. ₹1.5 Crore is incorrect.",
        why_d_ta="தவறானது. ₹1.5 கோடி தவறானது.",
        tip_en="Summary: Lok Sabha = ₹95 Lakhs (Bigger states) / ₹75 Lakhs (Smaller states). Assembly = ₹40 Lakhs (Bigger states) / ₹28 Lakhs (Smaller states).",
        tip_ta="சுருக்கம்: மக்களவை = ₹95 லட்சம் (பெரிய மாநிலங்கள்) / ₹75 லட்சம் (சிறியவை). சட்டசபை = ₹40 லட்சம் (பெரியவை) / ₹28 லட்சம் (சிறியவை).",
        fact_en="A committee comprising Harish Kumar and Umesh Sinha recommended this expenditure revision taking inflation into account.",
        fact_ta="ஹரிஷ் குமார் மற்றும் உமேஷ் சின்ஹா குழு பணவீக்கத்தைக் கருத்தில் கொண்டு இந்த உயர்வை பரிந்துரைத்தது.",
        tags=["Expenditure Limit 2022", "₹95 Lakhs", "Rule 90"]
    ))

    # ER_M_012
    qs.append(make_er_q(
        qid="ER_M_012", diff="Medium", qtype="Single-Choice", subtopic="Election Expenditure Limits",
        en_stem="What is the revised maximum campaign expenditure limit for a candidate contesting a State Legislative Assembly election in bigger states as per the 2022 notification?",
        ta_stem="2022 அறிவிக்கையின்படி, பெரிய மாநிலங்களில் சட்டமன்றத் தேர்தலில் போட்டியிடும் ஒரு வேட்பாளருக்கான அதிகபட்ச தேர்தல் பிரச்சார செலவு வரம்பு என்ன?",
        en_a="₹40 Lakhs", ta_a="₹40 லட்சம்",
        en_b="₹28 Lakhs", ta_b="₹28 லட்சம்",
        en_c="₹20 Lakhs", ta_c="₹20 லட்சம்",
        en_d="₹50 Lakhs", ta_d="₹50 லட்சம்",
        correct_key="A",
        exp_en="Under the amended Rule 90 of Conduct of Elections Rules, 1961 (notified in Jan 2022), the expenditure limit for a Legislative Assembly candidate in bigger states was raised from ₹28 Lakhs to ₹40 Lakhs (and from ₹20 Lakhs to ₹28 Lakhs in smaller states).",
        exp_ta="2022 ஜனவரியில் திருத்தப்பட்ட விதி 90-ன் படி, பெரிய மாநிலங்களில் ஒரு சட்டமன்ற வேட்பாளரின் தேர்தல் செலவு வரம்பு ₹28 லட்சத்திலிருந்து ₹40 லட்சமாக உயர்த்தப்பட்டது (சிறிய மாநிலங்களில் ₹28 லட்சம்).",
        why_a_en="Correct. ₹40 Lakhs for Assembly candidates in bigger states.",
        why_a_ta="சரியானது. பெரிய மாநில சட்டமன்றத் தேர்தலில் ₹40 லட்சம்.",
        why_b_en="Incorrect. ₹28 Lakhs was the previous ceiling in bigger states, and is the current ceiling in smaller states.",
        why_b_ta="தவறானது. ₹28 லட்சம் என்பது முந்தைய வரம்பு (மற்றும் சிறிய மாநிலங்களுக்கான தற்போதைய வரம்பு).",
        why_c_en="Incorrect. ₹20 Lakhs was the previous ceiling in smaller states.",
        why_c_ta="தவறானது. ₹20 லட்சம் என்பது சிறிய மாநிலங்களின் முந்தைய வரம்பு.",
        why_d_en="Incorrect. ₹50 Lakhs is incorrect.",
        why_d_ta="தவறானது. ₹50 லட்சம் தவறானது.",
        tip_en="Note that while there is an expenditure limit for candidates, there is currently NO statutory ceiling on expenditure by political parties.",
        tip_ta="வேட்பாளர்களுக்கு செலவு வரம்பு உள்ள போதிலும், அரசியல் கட்சிகள் செய்யும் செலவுக்கு தற்போது எவ்வித சட்டப்பூர்வ உச்சவரம்பும் இல்லை.",
        fact_en="Law Commission's 255th Report recommended introducing spending caps on political parties as well.",
        fact_ta="சட்ட ஆணையத்தின் 255-வது அறிக்கை அரசியல் கட்சிகளுக்கும் தேர்தல் செலவு வரம்பு விதிக்கப்பட வேண்டும் என பரிந்துரைத்தது.",
        tags=["Assembly Expenditure Limit", "₹40 Lakhs", "2022 Revision"]
    ))

    # ER_M_013
    qs.append(make_er_q(
        qid="ER_M_013", diff="Medium", qtype="Single-Choice", subtopic="Star Campaigners",
        en_stem="Under Section 77(1) Explanation 2 of the Representation of the People Act, 1951, how many 'Star Campaigners' can a recognized political party nominate for an election?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 77(1) விளக்கம் 2-ன் கீழ், ஒரு அங்கீகரிக்கப்பட்ட அரசியல் கட்சி ஒரு தேர்தலுக்கு அதிகபட்சமாக எத்தனை 'நட்சத்திரப் பிரச்சாரகர்களை' (Star Campaigners) நியமிக்க முடியும்?",
        en_a="Up to 40 Star Campaigners", ta_a="40 நட்சத்திரப் பிரச்சாரகர்கள் வரை",
        en_b="Up to 20 Star Campaigners", ta_b="20 நட்சத்திரப் பிரச்சாரகர்கள் வரை",
        en_c="Up to 50 Star Campaigners", ta_c="50 நட்சத்திரப் பிரச்சாரகர்கள் வரை",
        en_d="Unlimited Star Campaigners", ta_d="எண்ணிக்கை வரம்பின்றி எத்தனை பேர் வேண்டுமானாலும்",
        correct_key="A",
        exp_en="Under Section 77(1) of RPA 1951, a recognized political party (National or State) can nominate up to 40 leaders as star campaigners, whereas a registered unrecognised party can nominate up to 20 leaders. Their travel expenses are not added to candidate expenditure.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 77(1)-ன் படி, அங்கீகரிக்கப்பட்ட அரசியல் கட்சி அதிகபட்சமாக 40 நட்சத்திரப் பிரச்சாரகர்களையும், பதிவு செய்யப்பட்ட அங்கீகாரமற்ற கட்சி 20 நட்சத்திரப் பிரச்சாரகர்களையும் நியமிக்கலாம். இவர்களது பயணச் செலவு வேட்பாளரின் கணக்கில் சேராது.",
        why_a_en="Correct. 40 for recognized parties.",
        why_a_ta="சரியானது. அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு 40 பேர் வரை.",
        why_b_en="Incorrect. 20 is the limit for registered UNRECOGNIZED political parties.",
        why_b_ta="தவறானது. 20 என்பது பதிவு செய்யப்பட்ட அங்கீகாரமற்ற கட்சிகளுக்கான வரம்பு.",
        why_c_en="Incorrect. 50 is incorrect.",
        why_c_ta="தவறானது. 50 தவறானது.",
        why_d_en="Incorrect. Star campaigners are strictly capped by statute.",
        why_d_ta="தவறானது. சட்டப்பூர்வ வரம்பு உண்டு.",
        tip_en="List of star campaigners must be communicated to the ECI and CEO within 7 days from the election notification date.",
        tip_ta="தேர்தல் அறிவிக்கை வெளியான 7 நாட்களுக்குள் நட்சத்திரப் பிரச்சாரகர்களின் பட்டியலை தேர்தல் ஆணையத்திடம் சமர்ப்பிக்க வேண்டும்.",
        fact_en="If a star campaigner shares the stage with a candidate and actively seeks votes specifically for that candidate, their expenses are added to the candidate's account.",
        fact_ta="நட்சத்திரப் பிரச்சாரகர் வேட்பாளருடன் மேடையைப் பகிர்ந்து கொண்டு அவருக்காக மட்டுமே வாக்குக் கேட்டால், அந்த மேடைச் செலவு வேட்பாளரின் கணக்கில் சேர்க்கப்படும்.",
        tags=["Star Campaigners", "40 Leaders", "Section 77"]
    ))

    # ER_M_014
    qs.append(make_er_q(
        qid="ER_M_014", diff="Medium", qtype="Single-Choice", subtopic="Corrupt Practices",
        en_stem="In the landmark Abhiram Singh v. C.D. Commachen (2017) judgment, how did the 7-judge Constitution Bench interpret the phrase 'his religion' in Section 123(3) of RPA 1951?",
        ta_stem="அபிராம் சிங் எதிர் சி.டி. கொம்மாச்சன் (2017) வரலாற்று சிறப்புமிக்க வழக்கில், மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 123(3)-ல் உள்ள 'அவரது மதம்' என்ற சொற்றொடரை 7 நீதிபதிகள் அரசியல் சாசன அமர்வு எவ்வாறு விளக்கியது?",
        en_a="It includes the religion of the candidate, their agent, rival candidates, and the voters (broad interpretation)", ta_a="இது வேட்பாளர், அவரது முகவர், எதிர் வேட்பாளர்கள் மற்றும் வாக்காளர்களின் மதம் ஆகிய அனைத்தையும் உள்ளடக்கும் (விரிவான விளக்கம்)",
        en_b="It refers strictly and exclusively to the candidate's own personal religion only", ta_b="இது வேட்பாளரின் சொந்த மதத்தை மட்டுமே பிரத்யேகமாகக் குறிக்கும்",
        en_c="It excludes appeals based on caste and language entirely", ta_c="ஜாதி மற்றும் மொழி அடிப்படையிலான பிரச்சாரங்களை முழுமையாக விலக்குகிறது",
        en_d="It permits appeals to religion if made in private indoor gatherings", ta_d="உட்புற தனிப்பட்ட கூட்டங்களில் மதத்தின் பெயரால் வாக்குக் கேட்க அனுமதிக்கிறது",
        correct_key="A",
        exp_en="In Abhiram Singh (2017), a 4:3 majority bench held that Section 123(3) prohibits any appeal to religion, race, caste, community, or language—whether of the candidate, rival candidates, or the voters. An appeal to the identity of the voters to solicit votes or prejudice elections is a corrupt practice.",
        exp_ta="அபிராம் சிங் (2017) வழக்கில் 4:3 பெரும்பான்மை தீர்ப்பில், வேட்பாளர், அவரது எதிர்த்தரப்பு வேட்பாளர் அல்லது வாக்காளர்கள் ஆகிய எவரது மதம், இனம், ஜாதி, மொழி அடிப்படையிலும் வாக்குக் கேட்பது ஊழல் நடைமுறையாகும் (Corrupt Practice) என பரந்த விளக்கம் அளிக்கப்பட்டது.",
        why_a_en="Correct. Purposive interpretation covering candidate, rival, and voters.",
        why_a_ta="சரியானது. வேட்பாளர், எதிர்த்தரப்பு மற்றும் வாக்காளர்கள் அனைவரின் மத அடையாளமும் இதில் அடங்கும்.",
        why_b_en="Incorrect. Narrow interpretation was rejected by the majority.",
        why_b_ta="தவறானது. குறுகிய விளக்கம் பெரும்பான்மை அமர்வால் நிராகரிக்கப்பட்டது.",
        why_c_en="Incorrect. Section 123(3) explicitly includes caste and language.",
        why_c_ta="தவறானது. ஜாதி மற்றும் மொழியும் சட்டத்தில் தெளிவாகக் குறிப்பிடப்பட்டுள்ளது.",
        why_d_en="Incorrect. All religious appeals are barred irrespective of venue.",
        why_d_ta="தவறானது. எவ்விடத்திலும் மதத்தின் பெயரால் வாக்குக் கேட்க முடியாது.",
        tip_en="This verdict established secularism as an active constraint on electoral campaigning.",
        tip_ta="இத்தீர்ப்பு தேர்தல் பிரச்சாரங்களில் மதச்சார்பின்மையை ஒரு கட்டாயக் கட்டுப்பாடாக நிலைநிறுத்தியது.",
        fact_en="CJI T.S. Thakur headed the 7-judge Constitution Bench that delivered this 4:3 verdict on 2 January 2017.",
        fact_ta="2017 ஜனவரி 2 அன்று தலைமை நீதிபதி டி.எஸ். தாக்கூர் தலைமையிலான 7 நீதிபதிகள் அமர்வு இத்தீர்ப்பை வழங்கியது.",
        tags=["Abhiram Singh 2017", "Section 123(3)", "Corrupt Practices", "Secularism"]
    ))

    # ER_M_015
    qs.append(make_er_q(
        qid="ER_M_015", diff="Medium", qtype="Single-Choice", subtopic="Test Vote Procedure",
        en_stem="Under Rule 49MA of the Conduct of Elections Rules, 1961, what consequence faces an elector who makes a false declaration alleging that the VVPAT paper slip showed a candidate different from the one voted for?",
        ta_stem="தேர்தல் நடத்தை விதிகள் 1961 விதி 49MA-ன் கீழ், VVPAT சீட்டு தான் வாக்களித்த வேட்பாளரை காட்டவில்லை என்று தவறான பொய்யான புகாரை அளிக்கும் வாக்காளருக்கு ஏற்படும் விளைவு என்ன?",
        en_a="Prosecution under Section 177 of IPC (imprisonment up to 6 months or fine or both)", ta_a="இந்திய தண்டனைச் சட்டம் பிரிவு 177-ன் கீழ் வழக்குப்பதிவு (6 மாதங்கள் வரை சிறை அல்லது அபராதம்)",
        en_b="Immediate permanent cancellation of the voter's citizenship", ta_b="வாக்காளரின் இந்திய குடியுரிமை உடனடியாக நிரந்தரமாக ரத்து செய்யப்படும்",
        en_c="Lifetime ban from voting in all future Indian elections", ta_c="எதிர்கால அனைத்து இந்திய தேர்தல்களிலும் வாக்களிக்க வாழ்நாள் தடை",
        en_d="Deduction of 100 points from their civil credit score", ta_d="அவர்களது சிவில் மதிப்பெண்ணிலிருந்து 100 புள்ளிகள் குறைக்கப்படும்",
        correct_key="A",
        exp_en="Under Rule 49MA, if an elector alleges a VVPAT malfunction, the Presiding Officer permits a 'test vote'. If the test vote proves the allegation false and the machine accurate, the elector can be prosecuted under Section 177 of the Indian Penal Code (giving false information) with imprisonment up to 6 months or fine up to ₹1,000 or both.",
        exp_ta="விதி 49MA-ன் கீழ், ஒரு வாக்காளர் அளித்த புகார் மாதிரி வாக்கெடுப்பில் (Test vote) பொய் என நிரூபிக்கப்பட்டால், தவறான தகவல் அளித்ததற்காக இந்திய தண்டனைச் சட்டம் பிரிவு 177-ன் கீழ் 6 மாதம் வரை சிறைத்தண்டனை அல்லது ₹1,000 அபராதம் விதிக்கப்படலாம்.",
        why_a_en="Correct. Section 177 IPC prosecution (up to 6 months imprisonment or fine).",
        why_a_ta="சரியானது. IPC பிரிவு 177-ன் கீழ் 6 மாத சிறை அல்லது அபராதம்.",
        why_b_en="Incorrect. Citizenship cannot be cancelled for this.",
        why_b_ta="தவறானது. குடியுரிமை ரத்து செய்யப்படாது.",
        why_c_en="Incorrect. No lifetime voting ban applies.",
        why_c_ta="தவறானது. வாழ்நாள் வாக்களிக்கும் தடை இல்லை.",
        why_d_en="Incorrect. India has no civic credit score system.",
        why_d_ta="தவறானது. இந்தியாவில் அத்தகைய அமைப்பு இல்லை.",
        tip_en="Before the test vote is conducted, the Presiding Officer must warn the elector in writing about the penal consequences of Section 177 IPC.",
        tip_ta="மாதிரி வாக்கெடுப்பு நடத்துவதற்கு முன், வாக்குச்சாவடி தலைமை அலுவலர் இப்பிரிவு குறித்த எச்சரிக்கையை வாக்காளரிடம் எழுத்துப்பூர்வமாக தெரிவிக்க வேண்டும்.",
        fact_en="Test votes are recorded in Form 17A and accounted for in the final result under Rule 49MA(2).",
        fact_ta="மாதிரி வாக்குகள் படிவம் 17A-ல் பதிவு செய்யப்பட்டு இறுதி முடிவில் கணக்கில் எடுத்துக்கொள்ளப்படும்.",
        tags=["Rule 49MA", "Test Vote", "Section 177 IPC"]
    ))

    # ER_M_016
    qs.append(make_er_q(
        qid="ER_M_016", diff="Medium", qtype="Single-Choice", subtopic="Model Code of Conduct",
        en_stem="In which year was a specific chapter on 'Election Manifestos' added to the Model Code of Conduct following Supreme Court directions in S. Subramaniam Balaji v. State of Tamil Nadu?",
        ta_stem="எஸ். சுப்பிரமணியம் பாலாஜி எதிர் தமிழ்நாடு அரசு வழக்கில் உச்ச நீதிமன்றத்தின் வழிகாட்டுதலைத் தொடர்ந்து, மாதிரி தேர்தல் நடத்தை விதிகளில் 'தேர்தல் தேர்தல் அறிக்கைகள்' (Election Manifestos) குறித்த தனி அத்தியாயம் எந்த ஆண்டு சேர்க்கப்பட்டது?",
        en_a="2014", ta_a="2014",
        en_b="2004", ta_b="2004",
        en_c="1996", ta_c="1996",
        en_d="2019", ta_d="2019",
        correct_key="A",
        exp_en="In S. Subramaniam Balaji v. State of TN (July 2013), the Supreme Court held that while freebies in manifestos do not constitute a corrupt practice under Section 123, they influence the level-playing field. Following this, ECI framed guidelines on Election Manifestos and incorporated Part VIII into the MCC in February 2014.",
        exp_ta="எஸ். சுப்பிரமணியம் பாலாஜி வழக்கில் (2013), தேர்தல் அறிக்கைகளில் இலவசங்களை அறிவிப்பது தேர்தல் களத்தை பாதிக்கிறது என உச்ச நீதிமன்றம் கூறியதைத் தொடர்ந்து, தேர்தல் ஆணையம் 2014 பிப்ரவரியில் தேர்தல் அறிக்கைகளுக்கான வழிகாட்டுதல்களை மாதிரி நடத்தை விதிகளின் பகுதி VIII-ல் இணைத்தது.",
        why_a_en="Correct. Added in 2014 following the July 2013 Balaji verdict.",
        why_a_ta="சரியானது. 2013 பாலாஜி தீர்ப்பைத் தொடர்ந்து 2014-ல் சேர்க்கப்பட்டது.",
        why_b_en="Incorrect. 2004 was before the judgment.",
        why_b_ta="தவறானது. 2004 தீர்ப்பிற்கு முந்தையது.",
        why_c_en="Incorrect. 1996 was too early.",
        why_c_ta="தவறானது. 1996 மிக முந்தையது.",
        why_d_en="Incorrect. 2019 was the 17th Lok Sabha election year.",
        why_d_ta="தவறானது. 2019-ல் 17-வது மக்களவைத் தேர்தல் நடந்தது.",
        tip_en="Part VIII mandates that manifestos must reflect rationale for promises and indicate the ways and means to meet the financial requirements.",
        tip_ta="பகுதி VIII-ன் படி, வாக்குறுதிகளுக்கான நிதி ஆதாரங்களை எவ்வாறு திரட்டுவது என்பதையும் தேர்தல் அறிக்கையில் குறிப்பிட வேண்டும்.",
        fact_en="Manifestos also cannot be released during the prohibited 48-hour campaign silence period.",
        fact_ta="தேர்தலுக்கு முந்தைய 48 மணி நேர அமைதிக்காலத்தில் தேர்தல் அறிக்கைகளை வெளியிடவும் தடை விதிக்கப்பட்டுள்ளது.",
        tags=["Election Manifesto", "Subramaniam Balaji 2013", "MCC Part VIII", "2014"]
    ))

    # ER_M_017
    qs.append(make_er_q(
        qid="ER_M_017", diff="Medium", qtype="Single-Choice", subtopic="Corrupt Practices",
        en_stem="Under Section 123(7) of the Representation of the People Act, 1951, obtaining or procuring assistance from which category of persons for the furtherance of election prospects is a corrupt practice?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 123(7)-ன் கீழ், தேர்தல் வெற்றிக்காக எந்தப் பிரிவினரின் உதவியைப் பெறுவது ஊழல் நடைமுறையாகும் (Corrupt Practice)?",
        en_a="Persons in the service of the Government (Gazetted officers, police, armed forces, revenue officers)", ta_a="அரசுப் பணியில் உள்ள நபர்கள் (கெசட்டட் அதிகாரிகள், காவல்துறை, ராணுவம், வருவாய்த்துறை அதிகாரிகள்)",
        en_b="Private chartered accountants auditing party accounts", ta_b="கட்சி கணக்குகளைத் தணிக்கை செய்யும் தனியார் பட்டயக் கணக்காளர்கள்",
        en_c="Voluntary workers from non-governmental organizations", ta_c="அரசு சாரா தன்னார்வ தொண்டு நிறுவனங்களின் ஊழியர்கள்",
        en_d="Contractual advertisement designers and social media influencers", ta_d="ஒப்பந்த விளம்பர வடிவமைப்பாளர்கள் மற்றும் சமூக ஊடக பிரபலங்கள்",
        correct_key="A",
        exp_en="Section 123(7) of RPA 1951 defines obtaining or procuring assistance from gazetted officers, district magistrates, revenue officers, members of the armed forces, and police officers for the furtherance of the prospects of a candidate's election as a corrupt practice, which can nullify the election.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 123(7)-ன் படி, அரசு ஊழியர்கள், நீதிபதிகள், வருவாய்த்துறை அதிகாரிகள், காவல்துறையினர் மற்றும் ராணுவத்தினரின் உதவியை ஒரு வேட்பாளர் தனது தேர்தல் ஆதாயத்திற்காகப் பெறுவது கடுமையான ஊழல் நடைமுறையாகும்; இது தேர்தலையே ரத்து செய்ய வழிவகுக்கும்.",
        why_a_en="Correct. Procuring assistance from government servants is a corrupt practice under Section 123(7).",
        why_a_ta="சரியானது. அரசு ஊழியர்களின் உதவியைப் பெறுவது பிரிவு 123(7)-ன் கீழ் ஊழல் நடைமுறையாகும்.",
        why_b_en="Incorrect. Private accountants can be legitimately hired.",
        why_b_ta="தவறானது. தனியார் கணக்காளர்களை நியமிக்கலாம்.",
        why_c_en="Incorrect. NGO workers are not public servants.",
        why_c_ta="தவறானது. NGO ஊழியர்கள் அரசு ஊழியர்கள் அல்ல.",
        why_d_en="Incorrect. Commercial designers can be legally engaged.",
        why_d_ta="தவறானது. வணிக ரீதியான வடிவமைப்பாளர்களை ஈடுபடுத்தலாம்.",
        tip_en="This was the exact provision on which Indira Gandhi's 1971 election from Rae Bareli was set aside by the Allahabad High Court in 1975 (Yashpal Kapoor's assistance).",
        tip_ta="1975-ல் இந்திரா காந்தியின் ரேபரேலி தேர்தல் அலகாபாத் உயர் நீதிமன்றத்தால் ரத்து செய்யப்பட்டதற்கு இப்பிரிவே (யஷ்பால் கபூர் அரசுப்பணி விவகாரம்) காரணமாக அமைந்தது.",
        fact_en="Section 123(7) upholds the strict neutrality of the permanent civil service in elections.",
        fact_ta="தேர்தலில் நிரந்தர குடிமைப்பணியாளர்களின் கண்டிப்பான நடுநிலைமையை உறுதி செய்ய இப்பிரிவு உருவாக்கப்பட்டது.",
        tags=["Section 123(7)", "Corrupt Practice", "Government Servants Assistance"]
    ))

    # ER_M_018
    qs.append(make_er_q(
        qid="ER_M_018", diff="Medium", qtype="Single-Choice", subtopic="Anti-Defection Law",
        en_stem="Which Constitutional Amendment Act introduced the 10th Schedule (Anti-Defection Law) to curb the menace of opportunistic party hopping by legislators?",
        ta_stem="சட்டமன்ற உறுப்பினர்களின் சந்தர்ப்பவாத கட்சித் தாவல்களைத் தடுப்பதற்காக 10-வது அட்டவணையை (கட்சித் தாவல் தடைச் சட்டம்) அறிமுகப்படுத்திய அரசியலமைப்புச் சட்டத்திருத்தம் எது?",
        en_a="52nd Constitutional Amendment Act, 1985", ta_a="52-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1985",
        en_b="44th Constitutional Amendment Act, 1978", ta_b="44-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1978",
        en_c="91st Constitutional Amendment Act, 2003", ta_c="91-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2003",
        en_d="61st Constitutional Amendment Act, 1988", ta_d="61-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1988",
        correct_key="A",
        exp_en="The 52nd Constitutional Amendment Act, 1985 added the Tenth Schedule to the Constitution of India, providing for the disqualification of members of Parliament and State Legislatures on the ground of defection. It was enacted under Prime Minister Rajiv Gandhi.",
        exp_ta="52-வது அரசியலமைப்புச் சட்டத்திருத்தம் 1985, இந்திய அரசியலமைப்பில் 10-வது அட்டவணையை இணைத்து, கட்சித் தாவல் அடிப்படையில் நாடாளுமன்ற மற்றும் சட்டமன்ற உறுப்பினர்களை தகுதிநீக்கம் செய்வதற்கான விதிகளை உருவாக்கியது.",
        why_a_en="Correct. 52nd Amendment Act, 1985 introduced the 10th Schedule.",
        why_a_ta="சரியானது. 52-வது திருத்தச் சட்டம் 1985 பத்தாவது அட்டவணையை அறிமுகப்படுத்தியது.",
        why_b_en="Incorrect. 44th Amendment reversed emergency excesses.",
        why_b_ta="தவறானது. 44-வது திருத்தம் அவசரநிலை மாற்றங்களை நீக்கியது.",
        why_c_en="Incorrect. 91st Amendment (2003) strengthened anti-defection by removing the 1/3rd split exemption.",
        why_c_ta="தவறானது. 91-வது திருத்தம் (2003) மூன்றில் ஒரு பங்கு பிளவு விலக்கை நீக்கியது.",
        why_d_en="Incorrect. 61st Amendment lowered voting age to 18.",
        why_d_ta="தவறானது. 61-வது திருத்தம் வாக்களிக்கும் வயதை 18 ஆகக் குறைத்தது.",
        tip_en="Tenth Schedule was inserted into Articles 102(2) and 191(2).",
        tip_ta="பத்தாவது அட்டவணை சரத்து 102(2) மற்றும் 191(2)-ல் இணைக்கப்பட்டது.",
        fact_en="Popularly called the 'Anti-Defection Law', it was designed to stop the infamous 'Aaya Ram, Gaya Ram' culture of the late 1960s.",
        fact_ta="1960-களின் பிற்பகுதியில் நிலவிய 'ஆயா ராம், கயா ராம்' கட்சித் தாவல் கலாச்சாரத்திற்கு முற்றுப்புள்ளி வைக்க இது கொண்டுவரப்பட்டது.",
        tags=["52nd Amendment", "10th Schedule", "Anti-Defection Law", "1985"]
    ))

    # ER_M_019
    qs.append(make_er_q(
        qid="ER_M_019", diff="Medium", qtype="Single-Choice", subtopic="Anti-Defection Law",
        en_stem="Which provision of the 10th Schedule was deleted by the 91st Constitutional Amendment Act, 2003 because it was widely abused for engineering mass defections?",
        ta_stem="கூకుக் கட்சித் தாவல்களுக்கு தவறாகப் பயன்படுத்தப்பட்டதால், 91-வது அரசியலமைப்புச் சட்டத்திருத்தம் 2003-ன் மூலம் 10-வது அட்டவணையில் இருந்து நீக்கப்பட்ட விதி எது?",
        en_a="Exemption from disqualification in case of a split by one-third (1/3rd) members of the legislature party", ta_a="சட்டமன்றக் கட்சியில் மூன்றில் ஒரு பங்கு (1/3) உறுப்பினர்கள் பிளவுபட்டால் தகுதிநீக்கத்திலிருந்து விலக்கு அளிக்கும் விதி",
        en_b="Exemption for nominated members joining a party within 6 months", ta_b="நியமன உறுப்பினர்கள் 6 மாதங்களுக்குள் கட்சியில் சேர்வதற்கான விலக்கு",
        en_c="Exemption in case of merger of two-thirds (2/3rd) members", ta_c="மூன்றில் இரண்டு பங்கு (2/3) உறுப்பினர்கள் இணையும் போதான விலக்கு",
        en_d="Disqualification on voluntarily giving up membership", ta_d="சுயமாக கட்சி உறுப்பினர் பதவியை துறக்கும் போதான தகுதிநீக்கம்",
        correct_key="A",
        exp_en="The 91st Constitutional Amendment Act, 2003 omitted Paragraph 3 of the Tenth Schedule, which had earlier exempted members from disqualification if a split occurred involving not less than one-third of the legislature party. Now, only a merger involving not less than two-thirds (2/3rds) under Paragraph 4 is recognized.",
        exp_ta="91-வது அரசியலமைப்புச் சட்டத்திருத்தம் 2003, பத்தாவது அட்டவணையின் பத்தி 3-ஐ நீக்கியது. அப்பத்தி சட்டமன்றக் கட்சியில் மூன்றில் ஒரு பங்கு உறுப்பினர்கள் பிளவுபட்டால் தகுதிநீக்கத்திலிருந்து விலக்கு அளித்திருந்தது. தற்போது பத்தி 4-ன் கீழ் 2/3 பங்கு உறுப்பினர்கள் இணையும் சேர்க்கை மட்டுமே அனுமதிக்கப்படுகிறது.",
        why_a_en="Correct. 1/3rd split exemption under Paragraph 3 was deleted.",
        why_a_ta="சரியானது. பத்தி 3-ன் கீழான 1/3 பங்கு பிளவு விதி நீக்கப்பட்டது.",
        why_b_en="Incorrect. Nominated members joining within 6 months remains valid.",
        why_b_ta="தவறானது. நியமன உறுப்பினர்கள் விதி இப்போதும் தொடர்கிறது.",
        why_c_en="Incorrect. 2/3rd merger under Paragraph 4 is still retained in the Constitution.",
        why_c_ta="தவறானது. 2/3 பங்கு இணைப்பு விதி இன்றும் நடைமுறையில் உள்ளது.",
        why_d_en="Incorrect. Voluntarily giving up membership is the core ground for disqualification under Para 2(1)(a).",
        why_d_ta="தவறானது. சுயமாக உறுப்பினர் பதவியை கைவிடுவது தகுதிநீக்கத்திற்கான முதன்மைக் காரணமாகும்.",
        tip_en="Remember: 1/3rd Split is GONE (deleted in 2003); 2/3rd Merger REMAINS valid.",
        tip_ta="நினைவில் கொள்க: 1/3 பிளவு நீக்கப்பட்டுவிட்டது (2003); 2/3 இணைப்பு மட்டுமே செல்லும்.",
        fact_en="The 91st Amendment also capped the Council of Ministers at 15% of the total strength of the Lok Sabha / Legislative Assembly (minimum 12 in states).",
        fact_ta="91-வது திருத்தம் அமைச்சரவையின் அளவை சட்டமன்றத்தின் மொத்த பலத்தில் 15% ஆகக் கட்டுப்படுத்தியது (குறைந்தபட்சம் 12 அமைச்சர்கள்).",
        tags=["91st Amendment", "Paragraph 3 Deleted", "1/3rd Split", "Anti-Defection"]
    ))

    # ER_M_020
    qs.append(make_er_q(
        qid="ER_M_020", diff="Medium", qtype="Single-Choice", subtopic="Judicial Review of Speaker's Decision",
        en_stem="In which landmark judgment did the Supreme Court hold that the Speaker's decision under the Tenth Schedule is subject to judicial review, striking down Paragraph 7?",
        ta_stem="பத்தாவது அட்டவணையின் பத்தி 7-ஐ ரத்து செய்து, சபாநாயகரின் தகுதிநீக்க முடிவு நீதிமன்ற மறுஆய்வுக்கு (Judicial Review) உட்பட்டது என்று உச்ச நீதிமன்றம் எந்த வரலாற்று சிறப்புமிக்க வழக்கில் தீர்ப்பளித்தது?",
        en_a="Kihoto Hollohan v. Zachillhu (1992)", ta_a="கிகோட்டோ ஹோல்லோஹான் எதிர் ஜாச்சிலு (1992)",
        en_b="Indira Nehru Gandhi v. Raj Narain (1975)", ta_b="இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975)",
        en_c="Minerva Mills v. Union of India (1980)", ta_c="மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
        en_d="Golaknath v. State of Punjab (1967)", ta_d="கோலக்நாத் எதிர் பஞ்சாப் அரசு (1967)",
        correct_key="A",
        exp_en="In Kihoto Hollohan v. Zachillhu (1992), a Constitution Bench upheld the validity of the 10th Schedule but struck down Paragraph 7 (which excluded court jurisdiction) as unconstitutional for lack of state ratification under Article 368(2). The court ruled that the Speaker acts as a tribunal and their order is open to judicial review.",
        exp_ta="கிகோட்டோ ஹோல்லோஹான் (1992) வழக்கில், உச்ச நீதிமன்றம் பத்தாவது அட்டவணையின் செல்லுபடியை உறுதி செய்த அதே வேளையில், நீதிமன்ற அதிகார வரம்பைத் தடுத்த பத்தி 7-ஐ ரத்து செய்தது. சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுவதால் அவரது முடிவு நீதிப் புனராய்வுக்கு உட்பட்டது என தீர்ப்பளித்தது.",
        why_a_en="Correct. Kihoto Hollohan (1992) established judicial review over Speaker's decisions under 10th Schedule.",
        why_a_ta="சரியானது. கிகோட்டோ ஹோல்லோஹான் வழக்கு சபாநாயகரின் முடிவை நீதிப் புனராய்வுக்கு உட்படுத்தியது.",
        why_b_en="Incorrect. Raj Narain case dealt with Prime Minister's election.",
        why_b_ta="தவறானது. ராஜ் நாராயண் வழக்கு பிரதமர் தேர்தல் பற்றியது.",
        why_c_en="Incorrect. Minerva Mills strengthened basic structure and DPSP-FR balance.",
        why_c_ta="தவறானது. மினர்வா மில்ஸ் அடிப்படை உரிமைகள்-வழிகாட்டு நெறிகள் சமநிலையைக் கையாண்டது.",
        why_d_en="Incorrect. Golaknath barred constitutional amendments curtailing fundamental rights.",
        why_d_ta="தவறானது. கோலக்நாத் அடிப்படை உரிமைகளை திருத்த முடியாது என்றது.",
        tip_en="However, courts will not intervene at an interlocutory stage prior to the Speaker taking a final decision.",
        tip_ta="இருப்பினும், சபாநாயகர் இறுதி முடிவு எடுப்பதற்கு முந்தைய இடைக்கால நிலையில் நீதிமன்றங்கள் தலையிடாது.",
        fact_en="In Keisham Meghachandra Singh (2020), the Supreme Court recommended setting up an independent permanent tribunal to decide defection cases.",
        fact_ta="2020 மேகச்சந்திரா வழக்கில், கட்சித் தாவல் வழக்குகளை விசாரிக்க நிரந்தர தீர்ப்பாயம் அமைக்க உச்ச நீதிமன்றம் பரிந்துரைத்தது.",
        tags=["Kihoto Hollohan 1992", "Judicial Review", "Speaker Powers", "10th Schedule"]
    ))

    # ER_M_021
    qs.append(make_er_q(
        qid="ER_M_021", diff="Medium", qtype="Single-Choice", subtopic="Anti-Defection Law",
        en_stem="In Keisham Meghachandra Singh v. Hon'ble Speaker, Manipur (2020), what outer time limit did the Supreme Court lay down for Speakers to decide disqualification petitions under the 10th Schedule, absent exceptional reasons?",
        ta_stem="கீஷம் மேகச்சந்திர சிங் எதிர் மணிப்பூர் சபாநாயகர் (2020) வழக்கில், விதிவிலக்கான காரணங்கள் தவிர்த்து, பத்தாவது அட்டவணையின் கீழான தகுதிநீக்க மனுக்கள் மீது சபாநாயகர் முடிவு எடுக்க உச்ச நீதிமன்றம் நிர்ணயித்த காலக்கெடு என்ன?",
        en_a="3 months", ta_a="3 மாதங்கள்",
        en_b="6 months", ta_b="6 மாதங்கள்",
        en_c="1 month", ta_c="1 மாதம்",
        en_d="1 year", ta_d="1 ஆண்டு",
        correct_key="A",
        exp_en="In Keisham Meghachandra Singh (2020), the Supreme Court held that the Speaker must decide a disqualification petition filed under the Tenth Schedule within a reasonable period, which, absent exceptional circumstances, should be within 3 months.",
        exp_ta="கீஷம் மேகச்சந்திர சிங் (2020) வழக்கில், சபாநாயகர் பத்தாவது அட்டவணையின் கீழான தகுதிநீக்க மனுக்கள் மீது நியாயமான காலத்திற்குள், அதாவது விதிவிலக்கான சூழ்நிலைகள் இல்லாத வரை 3 மாதங்களுக்குள் முடிவு எடுக்க வேண்டும் என்று உச்ச நீதிமன்றம் உத்தரவிட்டது.",
        why_a_en="Correct. 3 months outer limit for Speaker's decision.",
        why_a_ta="சரியானது. சபாநாயகர் முடிவு எடுக்க 3 மாத காலக்கெடு.",
        why_b_en="Incorrect. 6 months is the target period for High Courts to conclude election petitions under Section 86(7).",
        why_b_ta="தவறானது. 6 மாதங்கள் என்பது தேர்தல் மனுவை விசாரிக்க உயர் நீதிமன்றத்திற்கான கால அளவு.",
        why_c_en="Incorrect. 1 month is too short.",
        why_c_ta="தவறானது. 1 மாதம் மிகவும் குறுகியது.",
        why_d_en="Incorrect. 1 year was deemed an unreasonable delay by the court.",
        why_d_ta="தவறானது. 1 ஆண்டு என்பது நியாயமற்ற தாமதமாகக் கருதப்பட்டது.",
        tip_en="Speakers historically sat on defection petitions for years to protect incumbent governments; this ruling curtailed that practice.",
        tip_ta="ஆளும் கட்சியைப் பாதுகாக்க சபாநாயகர்கள் மனுக்கள் மீது முடிவெடுக்காமல் பல ஆண்டுகள் இழுத்தடித்த வழக்கத்தை இத்தீர்ப்பு கட்டுப்படுத்தியது.",
        fact_en="Justice R.F. Nariman authored this landmark verdict advocating an independent constitutional tribunal.",
        fact_ta="நீதிபதி ஆர்.எஃப். நாரிமன் சுதந்திரமான தீர்ப்பாயத்தை பரிந்துரைத்து இத்தீர்ப்பை எழுதினார்.",
        tags=["Keisham Meghachandra 2020", "3 Months Deadline", "Speaker Disqualification"]
    ))

    # ER_M_022
    qs.append(make_er_q(
        qid="ER_M_022", diff="Medium", qtype="Single-Choice", subtopic="Right to Vote Legal Status",
        en_stem="In Anukul Chandra Pradhan v. Union of India (1997) and People's Union for Civil Liberties v. Union of India (2004), how did the Supreme Court classify the nature of the 'Right to Vote' in India?",
        ta_stem="அனுகுல் சந்திர பிரதான் (1997) மற்றும் PUCL (2004) வழக்குகளில், இந்தியாவில் 'வாக்களிக்கும் உரிமை'யின் சட்டப்பூர்வ தன்மையை உச்ச நீதிமன்றம் எவ்வாறு வகைப்படுத்தியது?",
        en_a="Statutory Right created by statute (subject to statutory limitations)", ta_a="சட்டத்தின் மூலம் உருவாக்கப்பட்ட சட்டப்பூர்வ உரிமை (Statutory Right)",
        en_b="Absolute Fundamental Right guaranteed under Part III", ta_b="பகுதி III-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட முழுமையான அடிப்படை உரிமை",
        en_c="Customary Common Law Right", ta_c="வழக்கத்திலமைந்த பொதுச்சட்ட உரிமை",
        en_d="Non-justiciable Directive Principle under Part IV", ta_d="நீதிமன்றத்தால் செயல்படுத்த முடியாத வழிகாட்டு நெறிமுறை (பகுதி IV)",
        correct_key="A",
        exp_en="The Supreme Court has consistently held (in NP Ponnuswami 1952, Jamuna Prasad 1954, Jyoti Basu 1982, Anukul Chandra Pradhan 1997, and PUCL 2004) that the Right to Vote is neither a Fundamental Right nor a Common Law right, but a pure Statutory Right governed by the provisions of the statute (RPA 1951).",
        exp_ta="பொன்னுசாமி (1952), ஜோதி பாசு (1982), அனுகுல் சந்திர பிரதான் (1997) மற்றும் PUCL (2004) வழக்குகளில், வாக்களிக்கும் உரிமை என்பது அடிப்படை உரிமை அல்ல; அது மக்கள் பிரதிநிதித்துவச் சட்டத்தால் உருவாக்கப்பட்டு வரையறுக்கப்பட்ட ஒரு 'சட்டப்பூர்வ உரிமை' (Statutory Right) என்று உச்ச நீதிமன்றம் திட்டவட்டமாக தீர்ப்பளித்துள்ளது.",
        why_a_en="Correct. Right to vote is a Statutory Right.",
        why_a_ta="சரியானது. வாக்களிக்கும் உரிமை ஒரு சட்டப்பூர்வ உரிமையாகும்.",
        why_b_en="Incorrect. It is NOT a Fundamental Right under Part III.",
        why_b_ta="தவறானது. இது பகுதி III-ன் கீழான அடிப்படை உரிமை அல்ல.",
        why_c_en="Incorrect. Common law rights do not create franchise in India.",
        why_c_ta="தவறானது. இது பொதுச்சட்ட உரிமை அல்ல.",
        why_d_en="Incorrect. It is not a Directive Principle under Part IV.",
        why_d_ta="தவறானது. இது பகுதி IV-ன் வழிகாட்டு நெறிமுறை அல்ல.",
        tip_en="Note the distinction: Right to KNOW about candidates is a Fundamental Right under Art 19(1)(a); Right to VOTE itself is a Statutory Right under RPA 1951.",
        tip_ta="வேறுபாட்டை கவனிக்கவும்: வேட்பாளரைப் பற்றி அறியும் உரிமை அடிப்படை உரிமை (சரத்து 19(1)(a)); ஆனால் வாக்களிக்கும் உரிமை சட்டப்பூர்வ உரிமையாகும் (RPA 1951).",
        fact_en="Because it is a statutory right, Section 62(5) of RPA 1951 legitimately prohibits prisoners from voting.",
        fact_ta="இது சட்டப்பூர்வ உரிமை என்பதால் தான், மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 62(5)-ன் கீழ் சிறைக்கைதிகள் வாக்களிப்பது தடை செய்யப்பட்டுள்ளது.",
        tags=["Right to Vote", "Statutory Right", "Anukul Chandra Pradhan", "PUCL"]
    ))

    # ER_M_023
    qs.append(make_er_q(
        qid="ER_M_023", diff="Medium", qtype="Single-Choice", subtopic="Prisoners Voting Rights",
        en_stem="Under Section 62(5) of the Representation of the People Act, 1951, which category of persons is legally prohibited from voting at any election?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 62(5)-ன் கீழ், எந்தப் பிரிவினர் எந்தவொரு தேர்தலிலும் வாக்களிக்க சட்டப்பூர்வமாக தடை செய்யப்பட்டுள்ளனர்?",
        en_a="Persons confined in prison (whether convicted or undertrial) or in lawful custody of the police", ta_a="சிறையில் அடைக்கப்பட்டுள்ள நபர்கள் (தண்டனை பெற்றவர்கள் அல்லது விசாரணைக் கைதிகள்) அல்லது காவல் கட்டுப்பாட்டில் உள்ளவர்கள்",
        en_b="Persons detained under any law providing for preventive detention", ta_b="தடுப்புக்காவல் சட்டங்களின் கீழ் அடைக்கப்பட்டுள்ள நபர்கள்",
        en_c="Senior citizens above 80 years of age living in care homes", ta_c="முதியோர் இல்லங்களில் வசிக்கும் 80 வயதுக்கு மேற்பட்ட மூத்த குடிமக்கள்",
        en_d="Non-resident Indian citizens residing abroad", ta_d="வெளிநாட்டில் வசிக்கும் வெளிநாடு வாழ் இந்தியர்கள்",
        correct_key="A",
        exp_en="Section 62(5) of RPA 1951 states that no person shall vote at any election if confined in a prison, whether under a sentence of imprisonment or transportation or otherwise, or is in the lawful custody of the police. However, the proviso explicitly protects persons subjected to preventive detention, who can vote via postal ballot.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 62(5)-ன் படி, சிறைத்தண்டனை பெற்றவர்கள், விசாரணைக் கைதிகள் அல்லது காவல் கட்டுப்பாட்டில் உள்ள எவரும் வாக்களிக்க முடியாது. ஆனால், தடுப்புக் காவலில் (Preventive Detention) உள்ள நபர்கள் தபால் வாக்கு மூலம் வாக்களிக்க விதிவிலக்கு அளிக்கப்பட்டுள்ளது.",
        why_a_en="Correct. Prisoners (convicts and undertrials) cannot vote under Section 62(5).",
        why_a_ta="சரியானது. தண்டனை மற்றும் விசாரணைக் கைதிகள் பிரிவு 62(5)-ன் கீழ் வாக்களிக்க முடியாது.",
        why_b_en="Incorrect. Persons under preventive detention ARE allowed to vote via postal ballot under the proviso to Section 62(5).",
        why_b_ta="தவறானது. தடுப்புக் காவலில் உள்ளவர்கள் தபால் வாக்கு மூலம் வாக்களிக்கலாம்.",
        why_c_en="Incorrect. Senior citizens have full voting rights and home voting.",
        why_c_ta="தவறானது. மூத்த குடிமக்களுக்கு முழு வாக்குரிமை உண்டு.",
        why_d_en="Incorrect. NRIs enrolled in the electoral roll have voting rights under Section 20A.",
        why_d_ta="தவறானது. NRI-களுக்கு பிரிவு 20A-ன் கீழ் வாக்குரிமை உண்டு.",
        tip_en="Key distinction for TNPSC: Undertrial prisoners in jail CANNOT vote; but persons under PREVENTIVE detention CAN vote via postal ballot.",
        tip_ta="முக்கிய TNPSC வேறுபாடு: சிறையில் உள்ள விசாரணைக் கைதி வாக்களிக்க முடியாது; ஆனால் தடுப்புக் காவலில் உள்ளவர் தபால் வாக்கு போடலாம்.",
        fact_en="The Supreme Court upheld the constitutional validity of Section 62(5) in Anukul Chandra Pradhan (1997).",
        fact_ta="1997 அனுகுல் சந்திர பிரதான் வழக்கில் பிரிவு 62(5)-ன் அரசியலமைப்பு செல்லுபடியை உச்ச நீதிமன்றம் உறுதி செய்தது.",
        tags=["Section 62(5)", "Prisoners Voting", "Preventive Detention Proviso"]
    ))

    # ER_M_024
    qs.append(make_er_q(
        qid="ER_M_024", diff="Medium", qtype="Single-Choice", subtopic="Election Petitions",
        en_stem="On which of the following grounds can the High Court declare the election of a returned candidate to be void under Section 100 of the Representation of the People Act, 1951?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 100-ன் கீழ், எந்தக் காரணத்தின் அடிப்படையில் வெற்றி பெற்ற வேட்பாளரின் தேர்தலை உயர் நீதிமன்றம் செல்லாது என அறிவிக்க முடியும்?",
        en_a="Improper acceptance of any nomination, or commission of any corrupt practice by the candidate or their election agent", ta_a="வேட்புமனு தவறாக ஏற்றுக்கொள்ளப்பட்டது அல்லது வேட்பாளர்/முகவரால் ஊழல் நடைமுறைகள் செய்யப்பட்டது நிரூபிக்கப்பட்டால்",
        en_b="The winning candidate belonged to a political party not having representation in the Rajya Sabha", ta_b="வெற்றி பெற்ற வேட்பாளர் மாநிலங்களவையில் பிரதிநிதித்துவம் இல்லாத கட்சியைச் சேர்ந்தவர் என்பதால்",
        en_c="The voter turnout in the constituency was less than 50%", ta_c="அத்தொகுதியில் பதிவான வாக்குகள் 50%-க்கும் குறைவாக இருந்ததால்",
        en_d="The election was conducted on a day declared as a public holiday", ta_d="தேர்தல் அரசு விடுமுறை நாளில் நடத்தப்பட்டது என்பதால்",
        correct_key="A",
        exp_en="Under Section 100(1) of RPA 1951, the High Court shall declare an election void if: (a) on the date of election the candidate was not qualified or disqualified, (b) any corrupt practice has been committed by the returned candidate or their election agent, (c) any nomination has been improperly rejected, or (d) the result has been materially affected by improper acceptance of nomination or non-compliance with the Constitution or RPA.",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 100(1)-ன் படி, தகுதியின்மை, வேட்பாளரால் ஊழல் நடைமுறைகள் செய்யப்பட்டது, வேட்புமனு தவறாக ஏற்றுக்கொள்ளப்பட்டது அல்லது நிராகரிக்கப்பட்டது, அல்லது அரசியலமைப்பு விதிகளுக்கு முரணாக தேர்தல் நடத்தப்பட்டு முடிவு பாதிக்கப்பட்டது போன்ற காரணங்களுக்காக தேர்தலை செல்லாது என அறிவிக்கலாம்.",
        why_a_en="Correct. Improper acceptance of nomination or corrupt practices under Section 100.",
        why_a_ta="சரியானது. வேட்புமனு தவறாக ஏற்கப்படுவது அல்லது ஊழல் நடைமுறைகள் பிரிவு 100-ன் கீழ் தேர்தலை ரத்து செய்ய வழிவகுக்கும்.",
        why_b_en="Incorrect. Rajya Sabha representation is completely irrelevant.",
        why_b_ta="தவறானது. மாநிலங்களவை பிரதிநிதித்துவத்திற்கு தொடர்பில்லை.",
        why_c_en="Incorrect. Turnout percentage does not affect validity.",
        why_c_ta="தவறானது. வாக்குப்பதிவு சதவீதம் தேர்தலை ரத்து செய்யாது.",
        why_d_en="Incorrect. Elections are commonly held on holidays.",
        why_d_ta="தவறானது. விடுமுறை நாட்களில் தேர்தல் நடத்துவது குற்றமல்ல.",
        tip_en="If a nomination is improperly REJECTED, the election is automatically void without having to prove material effect.",
        tip_ta="வேட்புமனு தவறாக நிராகரிக்கப்பட்டால், தேர்தல் முடிவு பாதிக்கப்பட்டது என்பதை நிரூபிக்காமலேயே தேர்தல் தானாக ரத்தாகும்.",
        fact_en="Under Section 101, the High Court can also declare another candidate duly elected if they received a majority of lawful votes.",
        fact_ta="பிரிவு 101-ன் படி சட்டப்பூர்வ பெரும்பான்மை பெற்ற மற்றொரு வேட்பாளரை வெற்றியாளராகவும் உயர் நீதிமன்றம் அறிவிக்கலாம்.",
        tags=["Section 100", "Election Void", "High Court Grounds"]
    ))

    # ER_M_025
    qs.append(make_er_q(
        qid="ER_M_025", diff="Medium", qtype="Single-Choice", subtopic="Election Commission Autonomy",
        en_stem="In the landmark T.N. Seshan v. Union of India (1995) judgment, what did the Supreme Court hold regarding the status and voting power of Election Commissioners relative to the Chief Election Commissioner?",
        ta_stem="வரலாற்று சிறப்புமிக்க டி.என். சேஷன் எதிர் இந்திய ஒன்றியம் (1995) வழக்கில், தலைமை தேர்தல் ஆணையருடன் ஒப்பிடுகையில் தேர்தல் ஆணையர்களின் அந்தஸ்து மற்றும் வாக்குரிமை குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        en_a="The CEC and Election Commissioners are at par with equal voting power, and decisions must be made unanimously or by majority", ta_a="தலைமை தேர்தல் ஆணையரும் மற்ற தேர்தல் ஆணையர்களும் சம அந்தஸ்து மற்றும் சம வாக்குரிமை கொண்டவர்கள்; முடிவுகள் ஒருமனதாக அல்லது பெரும்பான்மை அடிப்படையில் எடுக்கப்பட வேண்டும்",
        en_b="The CEC holds absolute veto power over any decision taken by the Election Commissioners", ta_b="தேர்தல் ஆணையர்கள் எடுக்கும் எந்தவொரு முடிவையும் நிராகரிக்கும் முழு வீட்டோ அதிகாரம் தலைமை தேர்தல் ஆணையருக்கு உண்டு",
        en_c="The Election Commissioners are merely subordinate advisory staff to the CEC", ta_c="தேர்தல் ஆணையர்கள் தலைமை தேர்தல் ஆணையருக்கு கீழ்ப்பட்ட வெறும் ஆலோசகர்கள் மட்டுமே",
        en_d="The Election Commissioners can only vote if the CEC is physically absent", ta_d="தலைமை தேர்தல் ஆணையர் வராதபோது மட்டுமே மற்ற தேர்தல் ஆணையர்கள் வாக்களிக்க முடியும்",
        correct_key="A",
        exp_en="In T.N. Seshan v. UOI (1995), a 5-judge Constitution Bench held that the CEC is not superior to other Election Commissioners in decision-making. The CEC is merely 'primus inter pares' (first among equals) to preside over meetings. Under Section 10 of the 1991 Act, all business must be transacted unanimously, or in case of difference of opinion, by the majority.",
        exp_ta="டி.என். சேஷன் (1995) வழக்கில், தலைமை தேர்தல் ஆணையர் மற்ற ஆணையர்களை விட உயர்ந்தவர் அல்ல; அவர் 'சமமானவர்களில் முதன்மையானவர்' (Primus inter pares) மட்டுமே என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. முடிவுகள் ஒருமனதாகவோ அல்லது பெரும்பான்மை அடிப்படையிலோ எடுக்கப்பட வேண்டும்.",
        why_a_en="Correct. ECI is a multi-member body where decisions are taken by majority and commissioners have equal status.",
        why_a_ta="சரியானது. ஆணையர்கள் சம அந்தஸ்து மற்றும் பெரும்பான்மை வாக்குரிமை கொண்டவர்கள்.",
        why_b_en="Incorrect. CEC has no veto power.",
        why_b_ta="தவறானது. தலைமை தேர்தல் ஆணையருக்கு வீட்டோ அதிகாரம் இல்லை.",
        why_c_en="Incorrect. Commissioners are not subordinates.",
        why_c_ta="தவறானது. அவர்கள் கீழ்ப்பட்ட அதிகாரிகள் அல்ல.",
        why_d_en="Incorrect. Commissioners always participate in all decisions.",
        why_d_ta="தவறானது. அனைத்து முடிவுகளிலும் சமமாகப் பங்கேற்பர்.",
        tip_en="The salary and conditions of service of all three commissioners are identical to that of a Supreme Court Judge.",
        tip_ta="மூன்று ஆணையர்களின் ஊதியம் மற்றும் படிகள் உச்ச நீதிமன்ற நீதிபதிக்கு இணையானதாகும்.",
        fact_en="The only constitutional distinction is tenure protection: the CEC can be removed only like a Supreme Court Judge, whereas ECs can be removed on the recommendation of the CEC.",
        fact_ta="ஒரே அரசியலமைப்பு வேறுபாடு பணிப் பாதுகாப்பு மட்டுமே: CEC-ஐ உச்ச நீதிமன்ற நீதிபதி போல மட்டுமே நீக்க முடியும், மற்ற ஆணையர்களை CEC பரிந்துரையின் பேரில் நீக்கலாம்.",
        tags=["TN Seshan 1995", "ECI Equality", "Majority Rule", "Primus Inter Pares"]
    ))

    # ER_M_026
    qs.append(make_er_q(
        qid="ER_M_026", diff="Medium", qtype="Single-Choice", subtopic="CEC and ECs Appointment 2023",
        en_stem="Under Section 5 of the Chief Election Commissioner and other Election Commissioners Act, 2023, what is the minimum qualifying administrative background required for appointment as CEC or EC?",
        ta_stem="தலைமைத் தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்கள் சட்டம், 2023 பிரிவு 5-ன் கீழ், CEC அல்லது EC ஆக நியமிக்கப்பட தேவையான குறைந்தபட்ச நிர்வாகத் தகுதி என்ன?",
        en_a="Persons who are holding or have held a post equivalent to the rank of Secretary to the Government of India", ta_a="இந்திய அரசின் செயலாளர் அந்தஸ்துக்கு இணையான பதவியை வகிக்கும் அல்லது வகித்த நபர்கள்",
        en_b="Serving or retired Judges of the Supreme Court or High Courts exclusively", ta_b="உச்ச நீதிமன்றம் அல்லது உயர் நீதிமன்றத்தின் தற்போதைய அல்லது ஓய்வுபெற்ற நீதிபதிகள் மட்டுமே",
        en_c="Members of Parliament who have served for at least two terms", ta_c="குறைந்தது இருமுறை பதவி வகித்த நாடாளுமன்ற உறுப்பினர்கள்",
        en_d="Senior advocates with at least 25 years of practice in the Supreme Court", ta_d="உச்ச நீதிமன்றத்தில் 25 ஆண்டுகள் பயிற்சி பெற்ற மூத்த வழக்கறிஞர்கள்",
        correct_key="A",
        exp_en="Section 5 of the 2023 Act specifies that the Chief Election Commissioner and other Election Commissioners shall be appointed from amongst persons who are holding or have held a post equivalent to the rank of Secretary to the Government of India and have knowledge of and experience in management and conduct of elections.",
        exp_ta="2023 சட்டத்தின் பிரிவு 5, இந்திய அரசின் செயலாளர் (Secretary to GoI) அந்தஸ்துக்கு இணையான பதவியை வகிக்கும் அல்லது வகித்த மற்றும் தேர்தல் மேலாண்மையில் அனுபவமும் அறிவும் கொண்ட நபர்களிலிருந்தே CEC மற்றும் EC நியமிக்கப்பட வேண்டும் என்று கூறுகிறது.",
        why_a_en="Correct. Secretary to the Government of India rank or equivalent.",
        why_a_ta="சரியானது. இந்திய அரசின் செயலாளர் அந்தஸ்து அல்லது அதற்கு இணையான பதவி.",
        why_b_en="Incorrect. Judicial background is not a statutory prerequisite.",
        why_b_ta="தவறானது. நீதித்துறை அனுபவம் கட்டாய நிபந்தனை அல்ல.",
        why_c_en="Incorrect. Active politicians/MPs are excluded.",
        why_c_ta="தவறானது. எம்.பி-க்களுக்கு இதில் இடமில்லை.",
        why_d_en="Incorrect. Advocates are not the target group.",
        why_d_ta="தவறானது. வழக்கறிஞர்களுக்கானது அல்ல.",
        tip_en="This codified the long-standing convention of appointing senior IAS officers of Secretary rank to the Election Commission.",
        tip_ta="செயலாளர் அந்தஸ்திலான மூத்த IAS அதிகாரிகளை தேர்தல் ஆணையத்திற்கு நியமிக்கும் நீண்டகால நடைமுறைக்கு இது சட்ட வடிவம் கொடுத்தது.",
        fact_en="The Act also provides that their salary, dearness allowance, and conditions of service shall be equal to the salary of a Judge of the Supreme Court.",
        fact_ta="இவர்களின் ஊதியம், அகவிலைப்படி மற்றும் சேவை நிபந்தனைகள் உச்ச நீதிமன்ற நீதிபதியின் ஊதியத்திற்கு சமமாக இருக்கும் என இச்சட்டம் கூறுகிறது.",
        tags=["CEC Act 2023", "Secretary Rank", "Section 5 Eligibility"]
    ))

    # ER_M_027
    qs.append(make_er_q(
        qid="ER_M_027", diff="Medium", qtype="Single-Choice", subtopic="Law Commission Reports",
        en_stem="The Law Commission of India's landmark 170th Report on 'Reform of the Electoral Laws' (submitted in May 1999) was headed by which eminent jurist?",
        ta_stem="1999 மே மாதம் சமர்ப்பிக்கப்பட்ட 'தேர்தல் சட்டங்களின் சீர்திருத்தம்' குறித்த இந்திய சட்ட ஆணையத்தின் 170-வது வரலாற்று சிறப்புமிக்க அறிக்கைக்கு தலைமை தாங்கிய நீதிபதி யார்?",
        en_a="Justice B.P. Jeevan Reddy", ta_a="நீதிபதி பி.பி. ஜீவன் ரெட்டி",
        en_b="Justice A.P. Shah", ta_b="நீதிபதி ஏ.பி. ஷா",
        en_c="Justice M.N. Venkatachaliah", ta_c="நீதிபதி எம்.என். வெங்கடாசலையா",
        en_d="Justice K.S. Hegde", ta_d="நீதிபதி கே.எஸ். ஹெக்டே",
        correct_key="A",
        exp_en="The 15th Law Commission of India, headed by Justice B.P. Jeevan Reddy, submitted its comprehensive 170th Report titled 'Reform of the Electoral Laws' in May 1999, recommending simultaneous elections, pre-poll alliance regulation, candidate disclosure, and partial list-system.",
        exp_ta="நீதிபதி பி.பி. ஜீவன் ரெட்டி தலைமையிலான 15-வது இந்திய சட்ட ஆணையம் 1999 மே மாதம் 'தேர்தல் சட்டங்களின் சீர்திருத்தம்' குறித்த தனது விரிவான 170-வது அறிக்கையை சமர்ப்பித்தது. ஒரே நேரத்தில் தேர்தல், கூட்டணிகள் முறைப்படுத்தல் போன்றவற்றை இது பரிந்துரைத்தது.",
        why_a_en="Correct. Justice B.P. Jeevan Reddy headed the 15th Law Commission (170th Report).",
        why_a_ta="சரியானது. நீதிபதி பி.பி. ஜீவன் ரெட்டி 170-வது அறிக்கையை வழங்கினார்.",
        why_b_en="Incorrect. Justice A.P. Shah headed the 20th Law Commission (244th & 255th Reports on electoral reforms).",
        why_b_ta="தவறானது. நீதிபதி ஏ.பி. ஷா 244 மற்றும் 255-வது அறிக்கைகளை வழங்கினார்.",
        why_c_en="Incorrect. Justice M.N. Venkatachaliah headed the NCRWC (2000-2002).",
        why_c_ta="தவறானது. நீதிபதி வெங்கடாசலையா NCRWC அரசியலமைப்பு மறுஆய்வு ஆணையத்திற்கு தலைமை தாங்கினார்.",
        why_d_en="Incorrect. Justice K.S. Hegde was a former Speaker.",
        why_d_ta="தவறானது. கே.எஸ். ஹெக்டே முன்னாள் சபாநாயகர்.",
        tip_en="170th Report (1999) = Justice B.P. Jeevan Reddy; 255th Report (2015) = Justice A.P. Shah.",
        tip_ta="170-வது அறிக்கை (1999) = நீதிபதி பி.பி. ஜீவன் ரெட்டி; 255-வது அறிக்கை (2015) = நீதிபதி ஏ.பி. ஷா.",
        fact_en="The 170th Report was the first official commission report to recommend introducing an additional 25% seats filled via Proportional Representation (List System).",
        fact_ta="கூடுதலாக 25% இடங்களை விகிதாச்சார பிரதிநிதித்துவப் பட்டியல் முறை (List System) மூலம் நிரப்பலாம் என 170-வது அறிக்கை முதலில் பரிந்துரைத்தது.",
        tags=["170th Law Commission", "Justice Jeevan Reddy", "1999"]
    ))

    # ER_M_028
    qs.append(make_er_q(
        qid="ER_M_028", diff="Medium", qtype="Single-Choice", subtopic="Law Commission Reports",
        en_stem="Which Law Commission Report submitted in March 2015 dealt exhaustively with 'Electoral Reforms', covering paid news, opinion polls, political finance, and disqualification on framing of charges?",
        ta_stem="2015 மார்ச்சில் சமர்ப்பிக்கப்பட்ட எந்த இந்திய சட்ட ஆணைய அறிக்கை ஊதியச் செய்தி, கருத்துக்கணிப்புகள், அரசியல் நிதி மற்றும் குற்றப்பத்திரிகை தாக்கல் அடிப்படையில் தகுதிநீக்கம் உள்ளிட்ட 'தேர்தல் சீர்திருத்தங்களை' விரிவாக ஆராய்ந்தது?",
        en_a="255th Report", ta_a="255-வது அறிக்கை",
        en_b="170th Report", ta_b="170-வது அறிக்கை",
        en_c="244th Report", ta_c="244-வது அறிக்கை",
        en_d="262nd Report", ta_d="262-வது அறிக்கை",
        correct_key="A",
        exp_en="The 20th Law Commission, headed by Justice A.P. Shah, submitted its seminal 255th Report on 'Electoral Reforms' in March 2015, recommending regulation of political finance, independent ECI appointment mechanism, anti-defection amendments, and disqualification on framing of charges for heinous offences.",
        exp_ta="நீதிபதி ஏ.பி. ஷா தலைமையிலான 20-வது சட்ட ஆணையம் 2015 மார்ச்சில் 'தேர்தல் சீர்திருத்தங்கள்' குறித்த தனது 255-வது அறிக்கையை சமர்ப்பித்தது. அரசியல் கட்சிகளின் நிதி கட்டுப்பாடு, ECI நியமன முறை மாற்றம் போன்றவற்றை இது பரிந்துரைத்தது.",
        why_a_en="Correct. 255th Report (March 2015) is the primary Law Commission report on Electoral Reforms.",
        why_a_ta="சரியானது. 255-வது அறிக்கை (2015) தேர்தல் சீர்திருத்தங்கள் பற்றியது.",
        why_b_en="Incorrect. 170th Report was submitted in 1999 under Justice Jeevan Reddy.",
        why_b_ta="தவறானது. 170-வது அறிக்கை 1999-ல் சமர்ப்பிக்கப்பட்டது.",
        why_c_en="Incorrect. 244th Report (February 2014) dealt specifically with 'Electoral Disqualifications' (criminalisation of politics).",
        why_c_ta="தவறானது. 244-வது அறிக்கை குற்றப்பின்னணி கொண்டோரின் தகுதிநீக்கம் பற்றியது மட்டுமே.",
        why_d_en="Incorrect. 262nd Report (August 2015) dealt with the death penalty.",
        why_d_ta="தவறானது. 262-வது அறிக்கை மரண தண்டனை பற்றியது.",
        tip_en="244th Report = Electoral Disqualifications (Feb 2014); 255th Report = Comprehensive Electoral Reforms (March 2015).",
        tip_ta="244-வது அறிக்கை = தகுதிநீக்கங்கள் (2014); 255-வது அறிக்கை = விரிவான தேர்தல் சீர்திருத்தங்கள் (2015).",
        fact_en="The 255th Report recommended introducing Section 29D in RPA 1951 to cap corporate political donations.",
        fact_ta="நிறுவனங்களின் அரசியல் நன்கொடைகளுக்கு உச்சவரம்பு விதிக்க பிரிவு 29D சேர்க்கப்பட வேண்டும் என 255-வது அறிக்கை கூறியது.",
        tags=["255th Law Commission", "Justice AP Shah", "2015 Report"]
    ))

    # ER_M_029
    qs.append(make_er_q(
        qid="ER_M_029", diff="Medium", qtype="Single-Choice", subtopic="NCRWC Recommendations",
        en_stem="The National Commission to Review the Working of the Constitution (NCRWC, 2002) headed by Justice M.N. Venkatachaliah recommended which major reform regarding the appointment of the Chief Election Commissioner?",
        ta_stem="நீதிபதி எம்.என். வெங்கடாசலையா தலைமையிலான அரசியலமைப்பு மறுஆய்வு தேசிய ஆணையம் (NCRWC, 2002), தலைமை தேர்தல் ஆணையர் நியமனம் தொடர்பாக பரிந்துரைத்த முக்கிய சீர்திருத்தம் எது?",
        en_a="Appointment by the President on the recommendation of a Committee consisting of the PM, Leader of Opposition, and CJI", ta_a="பிரதமர், எதிர்க்கட்சித் தலைவர் மற்றும் தலைமை நீதிபதி கொண்ட குழுவின் பரிந்துரையின் பேரில் குடியரசுத் தலைவரால் நியமிக்கப்பட வேண்டும்",
        en_b="Direct national popular election of the CEC by all registered voters", ta_b="அனைத்து வாக்காளர்களாலும் தலைமை தேர்தல் ஆணையர் நேரடியாக மக்களால் தேர்ந்தெடுக்கப்பட வேண்டும்",
        en_c="Automatic promotion of the senior-most Cabinet Secretary to the post of CEC", ta_c="மூத்த அமைச்சரவைச் செயலாளருக்கு தலைமை தேர்தல் ஆணையராக தானியங்கி பதவி உயர்வு அளிப்பது",
        en_d="Appointment exclusively by a collegium of retired CECs", ta_d="ஓய்வுபெற்ற தலைமை தேர்தல் ஆணையர்களின் கொலீஜியத்தால் மட்டுமே நியமிக்கப்படுவது",
        correct_key="A",
        exp_en="The NCRWC (Venkatachaliah Commission, 2002) recommended that the Chief Election Commissioner and other Election Commissioners should be appointed by the President on the recommendation of a committee comprising the Prime Minister, Leader of the Opposition in Lok Sabha, Speaker of Lok Sabha, Deputy Chairman of Rajya Sabha, and the Chief Justice of India.",
        exp_ta="NCRWC (2002) ஆணையம், பிரதமர், மக்களவை எதிர்க்கட்சித் தலைவர், மக்களவை சபாநாயகர், மாநிலங்களவை துணைத் தலைவர் மற்றும் உச்ச நீதிமன்ற தலைமை நீதிபதி ஆகியோர் அடங்கிய குழுவின் பரிந்துரையின் பேரில் குடியரசுத் தலைவரால் தேர்தல் ஆணையர்கள் நியமிக்கப்பட வேண்டும் என்று பரிந்துரைத்தது.",
        why_a_en="Correct. High-level committee including PM, LoP, and CJI.",
        why_a_ta="சரியானது. பிரதமர், எதிர்க்கட்சித் தலைவர் மற்றும் தலைமை நீதிபதி அடங்கிய உயர்நிலைக் குழு.",
        why_b_en="Incorrect. Popular election of CEC is not practiced in parliamentary democracies.",
        why_b_ta="தவறானது. நேரடி மக்களால் தேர்தல் நடத்த பரிந்துரைக்கப்படவில்லை.",
        why_c_en="Incorrect. Bureaucratic auto-promotion was rejected.",
        why_c_ta="தவறானது. தானியங்கி பதவி உயர்வு நிராகரிக்கப்பட்டது.",
        why_d_en="Incorrect. Retired CEC collegium was never recommended.",
        why_d_ta="தவறானது. ஓய்வுபெற்ற ஆணையர் கொலீஜியம் பரிந்துரைக்கப்படவில்லை.",
        tip_en="This exact committee pattern was later cited by the Supreme Court in the Anoop Baranwal (2023) judgment.",
        tip_ta="இதே குழு மாதிரியைத் தான் 2023 அனூப் பரன்வால் வழக்கில் உச்ச நீதிமன்ற அரசியல் சாசன அமர்வு மேற்கோள் காட்டியது.",
        fact_en="NCRWC submitted its report in March 2002 during the Atal Bihari Vajpayee government.",
        fact_ta="வாஜ்பாய் ஆட்சிக் காலத்தில் 2002 மார்ச்சில் NCRWC தனது அறிக்கையை சமர்ப்பித்தது.",
        tags=["NCRWC 2002", "Venkatachaliah Commission", "ECI Appointment"]
    ))

    # ER_M_030
    qs.append(make_er_q(
        qid="ER_M_030", diff="Medium", qtype="Single-Choice", subtopic="Anoop Baranwal Judgment 2023",
        en_stem="In the landmark Anoop Baranwal v. Union of India (March 2023) judgment, what selection committee composition was laid down by the 5-judge Constitution Bench until Parliament enacted a law?",
        ta_stem="அனூப் பரன்வால் எதிர் இந்திய ஒன்றியம் (மார்ச் 2023) தீர்ப்பில், நாடாளுமன்றம் சட்டம் இயற்றும் வரை தேர்தல் ஆணையர்களை நியமிக்க 5 நீதிபதிகள் அரசியல் சாசன அமர்வு உருவாக்கிய தேர்வுக் குழு எது?",
        en_a="Prime Minister, Leader of the Opposition in Lok Sabha, and the Chief Justice of India", ta_a="பிரதமர், மக்களவை எதிர்க்கட்சித் தலைவர் மற்றும் இந்திய தலைமை நீதிபதி",
        en_b="Prime Minister, Union Home Minister, and Speaker of Lok Sabha", ta_b="பிரதமர், மத்திய உள்துறை அமைச்சர் மற்றும் மக்களவை சபாநாயகர்",
        en_c="President of India, Vice-President, and Chief Justice of India", ta_c="இந்திய குடியரசுத் தலைவர், துணைக் குடியரசுத் தலைவர் மற்றும் தலைமை நீதிபதி",
        en_d="Speaker of Lok Sabha, Chairman of Rajya Sabha, and Attorney General", ta_d="மக்களவை சபாநாயகர், மாநிலங்களவைத் தலைவர் மற்றும் அட்டர்னி ஜெனரல்",
        correct_key="A",
        exp_en="On 2 March 2023, a unanimous 5-judge Constitution Bench headed by Justice K.M. Joseph ruled in Anoop Baranwal that until Parliament enacts a law under Article 324(2), the appointment of CEC and ECs shall be made by the President on the advice of a committee comprising the Prime Minister, the Leader of Opposition in Lok Sabha, and the Chief Justice of India.",
        exp_ta="2023 மார்ச் 2 அன்று நீதிபதி கே.எம். ஜோசப் தலைமையிலான 5 நீதிபதிகள் அமர்வு, நாடாளுமன்றம் சட்டமியற்றும் வரை பிரதமர், மக்களவை எதிர்க்கட்சித் தலைவர் மற்றும் இந்திய தலைமை நீதிபதி ஆகியோர் அடங்கிய குழுவின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர் நியமனம் செய்ய வேண்டும் என உத்தரவிட்டது.",
        why_a_en="Correct. PM, Leader of Opposition, and Chief Justice of India (CJI).",
        why_a_ta="சரியானது. பிரதமர், எதிர்க்கட்சித் தலைவர் மற்றும் இந்திய தலைமை நீதிபதி.",
        why_b_en="Incorrect. Home Minister and Speaker were not in the interim committee.",
        why_b_ta="தவறானது. உள்துறை அமைச்சரும் சபாநாயகரும் இல்லை.",
        why_c_en="Incorrect. President makes the appointment, not part of committee.",
        why_c_ta="தவறானது. குடியரசுத் தலைவர் நியமனம் செய்பவர், குழுவில் இருக்க மாட்டார்.",
        why_d_en="Incorrect. Attorney General was not part.",
        why_d_ta="தவறானது. அட்டர்னி ஜெனரல் இதில் இல்லை.",
        tip_en="In December 2023, Parliament exercised its constitutional power under Article 324(2) to pass the Appointment Act, which replaced the CJI with a Union Cabinet Minister.",
        tip_ta="2023 டிசம்பரில் நாடாளுமன்றம் சட்டமியற்றி, தலைமை நீதிபதிக்குப் பதிலாக ஒரு மத்திய கேபினட் அமைச்சரை சேர்த்தது.",
        fact_en="Article 324(2) explicitly provides that appointments are 'subject to the provisions of any law made in that behalf by Parliament'.",
        fact_ta="சரத்து 324(2) நியமனங்கள் 'நாடாளுமன்றம் இயற்றும் சட்டத்தின் விதிகளுக்கு உட்பட்டது' என்று தெளிவாகக் கூறுகிறது.",
        tags=["Anoop Baranwal 2023", "CJI Inclusion", "Article 324(2)"]
    ))

    # ER_M_031
    qs.append(make_er_q(
        qid="ER_M_031", diff="Medium", qtype="Single-Choice", subtopic="Corrupt Practices vs Electoral Offences",
        en_stem="What is the key legal distinction between a 'Corrupt Practice' (under Section 123 of RPA 1951) and an 'Electoral Offence' (under Chapter III of RPA 1951)?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 123-ன் கீழான 'ஊழல் நடைமுறை' (Corrupt Practice) மற்றும் அத்தியாயம் III-ன் கீழான 'தேர்தல் குற்றம்' (Electoral Offence) ஆகியவற்றுக்கு இடையேயான முக்கிய சட்ட வேறுபாடு என்ன?",
        en_a="Corrupt practices are civil grounds tried in election petitions to void an election; Electoral offences are criminal offences tried in criminal courts attracting jail/fine", ta_a="ஊழல் நடைமுறைகள் தேர்தலை ரத்து செய்ய தேர்தல் மனுவில் விசாரிக்கப்படும் உரிமையியல் காரணங்கள்; தேர்தல் குற்றங்கள் சிறை/அபராதம் விதிக்கும் குற்றவியல் நீதிமன்றங்களால் விசாரிக்கப்படுபவை",
        en_b="Corrupt practices apply only to voters; electoral offences apply only to government officials", ta_b="ஊழல் நடைமுறைகள் வாக்காளர்களுக்கு மட்டுமே பொருந்தும்; தேர்தல் குற்றங்கள் அரசு ஊழியர்களுக்கு மட்டுமே பொருந்தும்",
        en_c="Corrupt practices are triable only by the President; electoral offences are tried by the Lok Sabha Speaker", ta_c="ஊழல் நடைமுறைகளை குடியரசுத் தலைவர் மட்டுமே விசாரிக்க முடியும்; குற்றங்களை சபாநாயகர் விசாரிக்கிறார்",
        en_d="There is no legal difference; both terms are completely synonymous in Indian law", ta_d="எவ்வித சட்ட வேறுபாடும் இல்லை; இரண்டு சொற்களும் முழுமையான ஒரே பொருள் கொண்டவை",
        correct_key="A",
        exp_en="Corrupt practices (Section 123 of RPA 1951) are grounds on which the High Court can declare an election void under Section 100 via an Election Petition. In contrast, Electoral Offences (Sections 125 to 136 of RPA 1951 and Chapter IXA of IPC) are penal crimes prosecuted in ordinary criminal courts resulting in imprisonment and fines.",
        exp_ta="ஊழல் நடைமுறைகள் (பிரிவு 123) என்பது உயர் நீதிமன்றத்தில் தேர்தல் மனு தாக்கல் செய்து தேர்தலை ரத்து செய்வதற்கான காரணங்களாகும்; தேர்தல் குற்றங்கள் (பிரிவு 125-136) என்பது குற்றவியல் நீதிமன்றங்களில் வழக்குப் பதிவு செய்யப்பட்டு சிறை அல்லது அபராதம் விதிக்கப்படும் தண்டனைக்குரிய குற்றங்களாகும்.",
        why_a_en="Correct. Corrupt practices void elections in High Court; electoral offences lead to criminal punishment.",
        why_a_ta="சரியானது. ஊழல் நடைமுறைகள் தேர்தலை ரத்து செய்யும்; தேர்தல் குற்றங்கள் சிறைத் தண்டனைக்கு வழிவகுக்கும்.",
        why_b_en="Incorrect. Both can apply to candidates and other persons.",
        why_b_ta="தவறானது. இரண்டும் வேட்பாளர்களுக்கும் பிறருக்கும் பொருந்தும்.",
        why_c_en="Incorrect. High Court and criminal courts try them respectively.",
        why_c_ta="தவறானது. உயர் நீதிமன்றம் மற்றும் குற்றவியல் நீதிமன்றங்கள் முறையே விசாரிக்கின்றன.",
        why_d_en="Incorrect. Distinct legal categories under RPA 1951.",
        why_d_ta="தவறானது. இரண்டும் சட்டரீதியாக வேறுபட்டவை.",
        tip_en="Booth capturing is both a corrupt practice under Section 123(8) AND an electoral offence under Section 135A.",
        tip_ta="வாக்குச்சாவடி கைப்பற்றுதல் பிரிவு 123(8)-ன் கீழ் ஊழல் நடைமுறையாகவும், பிரிவு 135A-ன் கீழ் குற்றவியல் குற்றமாகவும் ஒரே நேரத்தில் கருதப்படுகிறது.",
        fact_en="A finding of corrupt practice by the High Court can lead to disqualification for up to 6 years under Section 8A upon reference to the President.",
        fact_ta="ஊழல் நடைமுறையில் ஈடுபட்டது நிரூபிக்கப்பட்டால் பிரிவு 8A-ன் கீழ் 6 ஆண்டுகள் வரை தகுதிநீக்கம் செய்யப்படலாம்.",
        tags=["Corrupt Practice vs Electoral Offence", "Section 123", "Election Law Distinction"]
    ))

    # ER_M_032
    qs.append(make_er_q(
        qid="ER_M_032", diff="Medium", qtype="Single-Choice", subtopic="Booth Capturing",
        en_stem="Which section was inserted into the Representation of the People Act, 1951 in 1989 to make 'Booth Capturing' a cognizable penal offence punishable with imprisonment up to 5 years?",
        ta_stem="வாக்குச்சாவடி கைப்பற்றுதலை (Booth Capturing) 5 ஆண்டுகள் வரை சிறைத்தண்டனைக்குரிய குற்றவியல் குற்றமாக மாற்றுவதற்காக 1989-ல் மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ல் சேர்க்கப்பட்ட பிரிவு எது?",
        en_a="Section 135A", ta_a="பிரிவு 135A",
        en_b="Section 123(1)", ta_b="பிரிவு 123(1)",
        en_c="Section 61A", ta_c="பிரிவு 61A",
        en_d="Section 29A", ta_d="பிரிவு 29A",
        correct_key="A",
        exp_en="Section 135A was inserted into RPA 1951 by an amendment in 1989, making booth capturing a cognizable criminal offence punishable with imprisonment for not less than 1 year which may extend to 3 years (or 3 to 5 years if committed by a person in government service).",
        exp_ta="1989 திருத்தச் சட்டத்தின் மூலம் பிரிவு 135A இணைக்கப்பட்டு, வாக்குச்சாவடி கைப்பற்றுதல் ஒரு கடுமையான குற்றவியல் குற்றமாக்கப்பட்டது. இதற்கு 1 முதல் 3 ஆண்டுகள் வரையிலும் (அரசு ஊழியராக இருந்தால் 3 முதல் 5 ஆண்டுகள் வரையிலும்) சிறைத்தண்டனை விதிக்கப்படும்.",
        why_a_en="Correct. Section 135A criminalises booth capturing.",
        why_a_ta="சரியானது. பிரிவு 135A வாக்குச்சாவடி கைப்பற்றுதலை குற்றமாக்குகிறது.",
        why_b_en="Incorrect. Section 123(1) defines bribery as a corrupt practice.",
        why_b_ta="தவறானது. பிரிவு 123(1) லஞ்சம் கொடுப்பதை வரையறுக்கிறது.",
        why_c_en="Incorrect. Section 61A authorizes EVMs.",
        why_c_ta="தவறானது. பிரிவு 61A வாக்குப்பதிவு இயந்திரங்களுக்கானது.",
        why_d_en="Incorrect. Section 29A governs registration of political parties.",
        why_d_ta="தவறானது. பிரிவு 29A கட்சிகள் பதிவு பற்றியது.",
        tip_en="Under Section 58A, the ECI has the power to adjourn or cancel elections in a polling station or entire constituency on grounds of booth capturing.",
        tip_ta="பிரிவு 58A-ன் கீழ் வாக்குச்சாவடி கைப்பற்றப்பட்டால் வாக்குப்பதிவை ரத்து செய்ய ECI-க்கு முழு அதிகாரம் உண்டு.",
        fact_en="The introduction of EVMs drastically reduced physical booth capturing across India.",
        fact_ta="EVM பயன்பாட்டிற்கு வந்த பிறகு நாட்டில் வாக்குச்சாவடி கைப்பற்றுதல் முறைகேடு பெருமளவு ஒழிக்கப்பட்டது.",
        tags=["Section 135A", "Booth Capturing", "1989 Amendment"]
    ))

    # ER_M_033
    qs.append(make_er_q(
        qid="ER_M_033", diff="Medium", qtype="Single-Choice", subtopic="Remote Voting for Migrants",
        en_stem="What prototype system did the Election Commission of India demonstrate to political parties in January 2023 to enable domestic migrant workers to vote without traveling to their home states?",
        ta_stem="உள்நாட்டு புலம்பெயர் தொழிலாளர்கள் தங்களது சொந்த மாநிலத்திற்கு பயணம் செய்யாமல் வாக்களிக்க உதவும் வகையில், 2023 ஜனவரியில் அரசியல் கட்சிகளுக்கு தேர்தல் ஆணையம் செயல்விளக்கம் அளித்த முன்மாதிரி அமைப்பு எது?",
        en_a="Multi-Constituency Remote Electronic Voting Machine (RVM)", ta_a="பல தொகுதிகளுக்கான தொலைதூர மின்னணு வாக்குப்பதிவு இயந்திரம் (RVM)",
        en_b="Blockchain-based Internet Voting Terminal", ta_b="பிளாக்செயின் அடிப்படையிலான இணைய வாக்குப்பதிவு முனையம்",
        en_c="Universal Mobile App Voting (UMAV)", ta_c="பொது மொபைல் செயலி வாக்குப்பதிவு",
        en_d="Automated Postal Ballot Kiosks", ta_d="தானியங்கி தபால் வாக்கு கியோஸ்க்குகள்",
        correct_key="A",
        exp_en="In January 2023, ECI demonstrated a prototype Remote Electronic Voting Machine (RVM) developed with ECIL and BEL. A single modified remote polling unit can handle voting for up to 72 different constituencies simultaneously for domestic migrants.",
        exp_ta="2023 ஜனவரியில், ECI மற்றும் பொதுத்துறை நிறுவனங்களான ECIL, BEL இணைந்து உருவாக்கிய தொலைதூர மின்னணு வாக்குப்பதிவு இயந்திரத்தை (RVM) செயல்விளக்கம் செய்து காட்டியது. ஒரே ஒரு தொலைதூர வாக்குச்சாவடி ஒரே நேரத்தில் 72 வெவ்வேறு தொகுதிகளுக்கான வாக்குகளைப் பதிவு செய்ய முடியும்.",
        why_a_en="Correct. Multi-Constituency Remote EVM (RVM).",
        why_a_ta="சரியானது. பல தொகுதிகளுக்கான தொலைதூர மின்னணு வாக்குப்பதிவு இயந்திரம் (RVM).",
        why_b_en="Incorrect. Internet voting was not proposed due to cybersecurity risks.",
        why_b_ta="தவறானது. பாதுகாப்பு காரணங்களால் இணைய வாக்குப்பதிவு ஏற்கப்படவில்லை.",
        why_c_en="Incorrect. Mobile app voting is not permitted for national elections.",
        why_c_ta="தவறானது. மொபைல் வாக்குப்பதிவு அனுமதிக்கப்படவில்லை.",
        why_d_en="Incorrect. Postal kiosks was not the system.",
        why_d_ta="தவறானது. தபால் கியோஸ்க்குகள் அல்ல.",
        tip_en="The RVM operates on the same standalone, non-networked principles as the traditional EVM, but uses a dynamic digital ballot display.",
        tip_ta="RVM இணையத் தொடர்பற்ற தனியான EVM போன்றே செயல்படும்; ஆனால் டிஜிட்டல் திரை மூலம் சின்னங்களைக் காட்டும்.",
        fact_en="Implementation was put on hold after political parties demanded deeper consultation on defining 'migrant' and logistical safeguards.",
        fact_ta="புலம்பெயர்ந்தோரை வரையறுப்பது மற்றும் பாதுகாப்பு நடைமுறைகள் குறித்து எதிர்க்கட்சிகள் எழுப்பிய கேள்விகளால் இது தற்காலிகமாக நிறுத்தி வைக்கப்பட்டுள்ளது.",
        tags=["RVM", "Remote Voting", "Migrant Workers", "ECI 2023"]
    ))

    # ER_M_034
    qs.append(make_er_q(
        qid="ER_M_034", diff="Medium", qtype="Single-Choice", subtopic="Election Laws Amendment 2021",
        en_stem="The Election Laws (Amendment) Act, 2021 amended the Representation of the People Act, 1950 to make voter registration language gender-neutral by substituting 'wife' with which term for service voters?",
        ta_stem="தேர்தல் சட்டங்கள் (திருத்தச்) சட்டம், 2021 பணி வாக்காளர்களுக்கு பாலின சமத்துவத்தை வழங்கும் வகையில், மக்கள் பிரதிநிதித்துவச் சட்டம் 1950-ல் 'மனைவி' (Wife) என்ற சொல்லுக்குப் பதிலாக எந்த சொல்லை மாற்றியது?",
        en_a="'Spouse'", ta_a="'துணைவர்' (Spouse)",
        en_b="'Partner'", ta_b="'கூட்டாளி' (Partner)",
        en_c="'Dependent'", ta_c="'சார்ந்திருப்பவர்' (Dependent)",
        en_d="'Nominee'", ta_d="'பரிந்துரைக்கப்படுபவர்' (Nominee)",
        correct_key="A",
        exp_en="Previously, Section 20(6) of RPA 1950 allowed the 'wife' of a service voter (e.g. army officer) to be enrolled as a service voter with her husband, but did not permit the 'husband' of a female army officer to be so enrolled. The 2021 amendment substituted 'wife' with 'spouse', making the statute gender-neutral.",
        exp_ta="முன்பு பிரிவு 20(6)-ன் கீழ், ஆண் ராணுவ அதிகாரியின் 'மனைவி' பணி வாக்காளராகப் பதிவு செய்ய அனுமதிக்கப்பட்டார்; ஆனால் பெண் ராணுவ அதிகாரியின் 'கணவர்' அவ்வாறு பதிவு செய்ய சட்டத்தில் இடமில்லை. 2021 திருத்தம் 'மனைவி' என்பதற்குப் பதிலாக 'துணைவர்' (Spouse) என்று மாற்றி பாலின சமத்துவத்தை ஏற்படுத்தியது.",
        why_a_en="Correct. 'Spouse' replaced 'wife' in Section 20 of RPA 1950.",
        why_a_ta="சரியானது. 'மனைவி' என்ற சொல்லுக்குப் பதிலாக 'துணைவர்' (Spouse) என மாற்றப்பட்டது.",
        why_b_en="Incorrect. Partner is not legal terminology used.",
        why_b_ta="தவறானது. சட்டச் சொல் அல்ல.",
        why_c_en="Incorrect. Dependent is broader and inaccurate.",
        why_c_ta="தவறானது. தவறான சொல்.",
        why_d_en="Incorrect. Nominee is for insurance/banking.",
        why_d_ta="தவறானது. காப்பீடு/வங்கிக்குரிய சொல்.",
        tip_en="This progressive amendment enabled male spouses of female service personnel to exercise service voting rights.",
        tip_ta="இத்திருத்தம் பெண் ராணுவ அதிகாரிகளின் கணவர்களும் பணி வாக்காளர் வசதியைப் பெற வழிவகுத்தது.",
        fact_en="The amendment also empowered electoral registration officers to requisition premises for polling and storage of voting machines.",
        fact_ta="வாக்குப்பதிவு மற்றும் இயந்திரங்களைப் பாதுகாக்க வளாகங்களை கையகப்படுத்தும் அதிகாரத்தையும் இச்சட்டத்திருத்தம் வழங்கியது.",
        tags=["Election Laws 2021", "Gender Neutral", "Spouse", "Service Voters"]
    ))

    # ER_M_035
    qs.append(make_er_q(
        qid="ER_M_035", diff="Medium", qtype="Single-Choice", subtopic="Recognition of Political Parties",
        en_stem="Under the Election Symbols (Reservation and Allotment) Order, 1968, which of the following is ONE of the criteria for a political party to be recognized as a 'State Party'?",
        ta_stem="தேர்தல் சின்னங்கள் (ஒதுக்கீடு) ஆணை 1968-ன் கீழ், ஓர் அரசியல் கட்சி 'மாநிலக் கட்சி' (State Party) என அங்கீகரிக்கப்பட வேண்டிய தகுதிகளில் ஒன்று எது?",
        en_a="Securing at least 6% of valid votes polled in the state assembly election AND winning at least 2 assembly seats", ta_a="மாநில சட்டமன்றத் தேர்தலில் பதிவான செல்லுபடியாகும் வாக்குகளில் குறைந்தது 6% வாக்குகளுடன் 2 சட்டமன்றத் தொகுதிகளில் வெற்றி பெறுதல்",
        en_b="Securing at least 1% of total votes across all states in India", ta_b="இந்தியாவின் அனைத்து மாநிலங்களிலும் சேர்த்து குறைந்தது 1% வாக்குகள் பெறுதல்",
        en_c="Winning at least 10 seats in the Rajya Sabha", ta_c="மாநிலங்களவையில் குறைந்தது 10 இடங்களில் வெற்றி பெறுதல்",
        en_d="Having a membership base of at least 50 lakh verified card-holding members", ta_d="குறைந்தது 50 லட்சம் அட்டைதாரர்களை உறுப்பினர்களாகக் கொண்டிருத்தல்",
        correct_key="A",
        exp_en="Under the Symbols Order, 1968, a party is recognized as a State Party if it fulfills any of these conditions: (1) 6% valid votes in Assembly + 2 Assembly seats, (2) 6% valid votes in Lok Sabha from the state + 1 Lok Sabha seat, (3) 3% of total Assembly seats or 3 seats (whichever is more), (4) 1 Lok Sabha seat for every 25 seats allocated to the state, or (5) 8% of total valid votes in the state in Assembly or Lok Sabha.",
        exp_ta="சின்னங்கள் ஆணை 1968-ன் கீழ் மாநிலக் கட்சியாக அங்கீகரிக்கப்பட: (1) சட்டசபைத் தேர்தலில் 6% வாக்குகள் + 2 தொகுதிகளில் வெற்றி, அல்லது (2) மக்களவைத் தேர்தலில் 6% வாக்குகள் + 1 மக்களவைத் தொகுதி வெற்றி, அல்லது (3) மொத்த சட்டசபையில் 3% இடங்கள் அல்லது 3 இடங்கள் வெற்றி, அல்லது (4) 25 தொகுதிகளுக்கு 1 மக்களவை தொகுதி வெற்றி, அல்லது (5) 8% வாக்குகள் பெறுதல்.",
        why_a_en="Correct. 6% votes + 2 assembly seats is a standard criterion.",
        why_a_ta="சரியானது. 6% வாக்குகள் + 2 சட்டமன்றத் தொகுதிகளில் வெற்றி.",
        why_b_en="Incorrect. 1% is far below any threshold.",
        why_b_ta="தவறானது. 1% மிகவும் குறைவானது.",
        why_c_en="Incorrect. Rajya Sabha seats are not criteria for party recognition.",
        why_c_ta="தவறானது. மாநிலங்களவை இடங்கள் அங்கீகார தகுதியல்ல.",
        why_d_en="Incorrect. Membership numbers are irrelevant to statutory recognition.",
        why_d_ta="தவறானது. கட்சி உறுப்பினர் எண்ணிக்கை அளவுகோல் அல்ல.",
        tip_en="Condition 5 (8% vote share alone without winning any seat) was added by ECI in 2011.",
        tip_ta="தொகுதி வெற்றி பெறாவிட்டாலும் 8% வாக்குகள் பெற்றால் அங்கீகாரம் பெறும் விதி 2011-ல் சேர்க்கப்பட்டது.",
        fact_en="Recognized state parties get an exclusive reserved symbol in that state, free airtime on Doordarshan/AIR, and up to 40 star campaigners.",
        fact_ta="அங்கீகரிக்கப்பட்ட மாநில கட்சிகளுக்கு மாநிலத்தில் நிரந்தர சின்னம், தூர்தர்ஷனில் இலவச பிரச்சார நேரம் மற்றும் 40 நட்சத்திரப் பிரச்சாரகர்கள் சலுகை கிடைக்கும்.",
        tags=["State Party Recognition", "Symbols Order 1968", "6% Votes Plus 2 Seats"]
    ))

    # ER_M_036
    qs.append(make_er_q(
        qid="ER_M_036", diff="Medium", qtype="Single-Choice", subtopic="Recognition of Political Parties",
        en_stem="To be recognized as a 'National Party', in how many states must a political party be recognized as a State Party under the Symbols Order, 1968?",
        ta_stem="தேர்தல் சின்னங்கள் ஆணை 1968-ன் கீழ், ஓர் அரசியல் கட்சி 'தேசியக் கட்சி' (National Party) என அங்கீகரிக்கப்பட குறைந்தது எத்தனை மாநிலங்களில் மாநிலக் கட்சியாக அங்கீகரிக்கப்பட்டிருக்க வேண்டும்?",
        en_a="At least 4 states", ta_a="குறைந்தது 4 மாநிலங்கள்",
        en_b="At least 3 states", ta_b="குறைந்தது 3 மாநிலங்கள்",
        en_c="At least 6 states", ta_c="குறைந்தது 6 மாநிலங்கள்",
        en_d="At least 8 states", ta_d="குறைந்தது 8 மாநிலங்கள்",
        correct_key="A",
        exp_en="Under Paragraph 6B of the Election Symbols (Reservation and Allotment) Order, 1968, a political party is eligible to be recognized as a National Party if it is recognized as a State Party in at least four (4) states.",
        exp_ta="தேர்தல் சின்னங்கள் ஆணை 1968-ன் பத்தி 6B-ன் படி, ஓர் அரசியல் கட்சி குறைந்தது நான்கு (4) மாநிலங்களில் மாநிலக் கட்சியாக அங்கீகரிக்கப்பட்டிருந்தால், அது தேசியக் கட்சியாக அங்கீகரிக்கப்பட தகுதி பெறுகிறது.",
        why_a_en="Correct. Recognized in at least 4 states.",
        why_a_ta="சரியானது. குறைந்தது 4 மாநிலங்களில் மாநிலக் கட்சியாக இருக்க வேண்டும்.",
        why_b_en="Incorrect. 3 states is for winning 2% Lok Sabha seats from 3 different states.",
        why_b_ta="தவறானது. 3 மாநிலங்கள் என்பது மக்களவை 2% இடங்களை வெல்வதற்கான நிபந்தனை.",
        why_c_en="Incorrect. 6 states is incorrect.",
        why_c_ta="தவறானது. 6 மாநிலங்கள் தவறானது.",
        why_d_en="Incorrect. 8 states is incorrect.",
        why_d_ta="தவறானது. 8 மாநிலங்கள் தவறானது.",
        tip_en="Aam Aadmi Party (AAP) achieved National Party status in April 2023 by qualifying as a state party in Delhi, Punjab, Goa, and Gujarat (4 states).",
        tip_ta="ஆம் ஆத்மி கட்சி டெல்லி, பஞ்சாப், கோவா, குஜராத் (4 மாநிலங்கள்) ஆகிய மாநிலங்களில் அங்கீகாரம் பெற்று 2023-ல் தேசியக் கட்சியாக உயர்ந்தது.",
        fact_en="Other two criteria: (i) 6% valid votes in 4 states + 4 Lok Sabha seats, OR (ii) 2% of total Lok Sabha seats (11 seats) elected from at least 3 states.",
        fact_ta="மற்ற தகுதிகள்: (i) 4 மாநிலங்களில் 6% வாக்குகள் + 4 மக்களவை இடங்கள், அல்லது (ii) குறைந்தது 3 மாநிலங்களிலிருந்து 2% மக்களவை இடங்கள் (11 இடங்கள்) வெற்றி.",
        tags=["National Party Criteria", "4 States Recognition", "Symbols Order"]
    ))

    # ER_M_037
    qs.append(make_er_q(
        qid="ER_M_037", diff="Medium", qtype="Single-Choice", subtopic="Party Deregistration",
        en_stem="In Indian National Congress v. Institute of Social Welfare (2002), what did the Supreme Court rule regarding the power of the Election Commission to deregister a political party under Section 29A of RPA 1951?",
        ta_stem="இந்திய தேசிய காங்கிரஸ் எதிர் சமூக நல நிறுவனம் (2002) வழக்கில், மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 29A-ன் கீழ் ஓர் அரசியல் கட்சியின் பதிவை ரத்து செய்யும் (Deregistration) தேர்தல் ஆணையத்தின் அதிகாரம் குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        en_a="ECI has no general statutory power to deregister a political party, except in 3 rare exceptions (fraud, party dissolution, or disloyalty to Constitution)", ta_a="3 அரிய விதிவிலக்குகள் தவிர (மோசடி, கட்சி கலைப்பு, அரசியலமைப்புக்கு துரோகம்) கட்சிகளின் பதிவை ரத்து செய்ய தேர்தல் ஆணையத்திற்கு பொதுவான சட்ட அதிகாரம் இல்லை",
        en_b="ECI has absolute unfettered power to deregister any party at will for poor electoral performance", ta_b="தேர்தல் தோல்விகளுக்காக எந்தக் கட்சியையும் தன் விருப்பப்படி ரத்து செய்ய ECI-க்கு முழு அதிகாரம் உண்டு",
        en_c="Only the Supreme Court has the power to register or deregister political parties", ta_c="உச்ச நீதிமன்றத்திற்கு மட்டுமே கட்சிகளை பதிவு செய்ய அல்லது ரத்து செய்ய அதிகாரம் உண்டு",
        en_d="Deregistration can be done by a simple executive order of the Union Home Ministry", ta_d="மத்திய உள்துறை அமைச்சகத்தின் சாதாரண நிர்வாக உத்தரவு மூலம் கட்சியை ரத்து செய்யலாம்",
        correct_key="A",
        exp_en="In Indian National Congress v. Institute of Social Welfare (2002), the Supreme Court ruled that Section 29A is an administrative, quasi-judicial power that does not confer power on ECI to deregister a political party once registered, except in 3 narrow exceptions: (1) registration obtained through fraud/forgery, (2) party has ceased to exist under its own constitution, or (3) party violates its solemn declaration under Section 29A(5) to adhere to the Constitution.",
        exp_ta="2002 காங்கிரஸ் வழக்கில், பிரிவு 29A என்பது நிர்வாக ரீதியானது என்றும், ஒருமுறை பதிவு செய்த கட்சியை ரத்து செய்ய தேர்தல் ஆணையத்திற்கு பொது அதிகாரம் இல்லை என்றும் உச்ச நீதிமன்றம் கூறியது. (1) மோசடி மூலம் பதிவு, (2) கட்சி சுயமாக கலைக்கப்படுவது, (3) அரசியலமைப்பு விசுவாச உறுதிமொழியை மீறுவது ஆகிய 3 சூழல்களில் மட்டுமே ரத்து செய்ய முடியும்.",
        why_a_en="Correct. ECI lacks general power to deregister parties absent the 3 exceptions.",
        why_a_ta="சரியானது. 3 விதிவிலக்குகள் தவிர கட்சியை ரத்து செய்ய ECI-க்கு சட்ட அதிகாரம் இல்லை.",
        why_b_en="Incorrect. ECI cannot deregister parties for poor performance.",
        why_b_ta="தவறானது. தேர்தல் தோல்விக்காக பதிவை ரத்து செய்ய முடியாது.",
        why_c_en="Incorrect. Section 29A vests registration in ECI, not Supreme Court.",
        why_c_ta="தவறானது. பிரிவு 29A தேர்தல் ஆணையத்திற்கு பதிவு அதிகாரத்தை வழங்குகிறது.",
        why_d_en="Incorrect. Executive cannot deregister political parties.",
        why_d_ta="தவறானது. அரசு நிர்வாகத்தால் ரத்து செய்ய முடியாது.",
        tip_en="Because of this limitation, ECI has repeatedly written to the Law Ministry requesting explicit statutory power to deregister defunct and inactive parties.",
        tip_ta="இக்குறையை நீக்க, செயல்படாத கட்சிகளின் பதிவை ரத்து செய்ய தங்களுக்கு சட்டப்பூர்வ அதிகாரம் வழங்க வேண்டும் என ECI மத்திய அரசிடம் கோரி வருகிறது.",
        fact_en="ECI bypasses this limitation by 'delisting' inactive parties, which deprives them of income tax exemption and common symbol benefits.",
        fact_ta="ECI செயல்படாத கட்சிகளை 'பட்டியலிலிருந்து நீக்குவதன்' (Delisting) மூலம் அவற்றின் வரிவிலக்கு மற்றும் சின்ன சலுகைகளை முடக்குகிறது.",
        tags=["Deregistration of Parties", "Section 29A", "Supreme Court 2002"]
    ))

    # ER_M_038
    qs.append(make_er_q(
        qid="ER_M_038", diff="Medium", qtype="Single-Choice", subtopic="Model Code of Conduct Enforceability",
        en_stem="Why has the Election Commission of India consistently opposed giving statutory backing to the Model Code of Conduct (MCC) by enacting it into an Act of Parliament?",
        ta_stem="மாதிரி தேர்தல் நடத்தை விதிகளை (MCC) நாடாளுமன்றச் சட்டமாக மாற்றி சட்டப்பூர்வ அந்தஸ்து வழங்குவதை இந்திய தேர்தல் ஆணையம் தொடர்ந்து எதிர்ப்பது ஏன்?",
        en_a="Because legal trials in courts would take months/years, defeating the speedy 45-day election window, whereas MCC allows instant administrative action", ta_a="நீதிமன்ற விசாரணைகள் பல மாதங்கள்/ஆண்டுகள் நீடித்து 45 நாள் தேர்தல் சுழற்சியை வீணாக்கிவிடும்; ஆனால் தற்போதைய MCC உடனடி நிர்வாக நடவடிக்கையை அனுமதிக்கிறது",
        en_b="Because the Constitution explicitly prohibits the Election Commission from enforcing statutory laws", ta_b="தேர்தல் ஆணையம் சட்டங்களை அமல்படுத்த அரசியலமைப்பு தடை விதித்துள்ளது என்பதால்",
        en_c="Because political parties would have to be dissolved if convicted of any breach", ta_c="விதிமீறலுக்காக அரசியல் கட்சிகள் அனைத்தும் கலைக்கப்பட நேரிடும் என்பதால்",
        en_d="Because the Model Code of Conduct applies exclusively to local panchayat elections", ta_d="மாதிரி நடத்தை விதிகள் உள்ளாட்சித் தேர்தல்களுக்கு மட்டுமே பொருந்தும் என்பதால்",
        correct_key="A",
        exp_en="ECI has opposed making MCC a statutory law because any violation would have to be tried in regular criminal courts with rights of appeal, taking years to reach a verdict. Under Article 324, the MCC operates as an agile administrative tool that allows ECI to issue warnings, ban leaders from campaigning for 48-72 hours, and transfer biased officers within hours.",
        exp_ta="MCC-ஐ சட்டமாக்கினால், விதிமீறல்கள் வழக்கமான நீதிமன்றங்களுக்குச் சென்று பல ஆண்டுகள் வழக்கு நீடிக்கும்; தேர்தல் முடிந்துவிடும். ஆனால் தற்போதைய நடைமுறையில் சரத்து 324-ன் கீழ் ECI உடனடி எச்சரிக்கை விடுக்கவும், தலைவர்கள் பிரச்சாரம் செய்ய 48-72 மணி நேர தடை விதிக்கவும், அதிகாரிகளை உடனே மாற்றவும் முடிகிறது.",
        why_a_en="Correct. Instant swift administrative action during the short election window.",
        why_a_ta="சரியானது. குறுகிய தேர்தல் காலத்தில் உடனடி நிர்வாக நடவடிக்கை எடுக்க உதவுகிறது.",
        why_b_en="Incorrect. ECI routinely enforces RPA 1950 and RPA 1951.",
        why_b_ta="தவறானது. ECI மக்கள் பிரதிநிதித்துவச் சட்டங்களை அமல்படுத்துகிறது.",
        why_c_en="Incorrect. Dissolution of parties is not a statutory consequence.",
        why_c_ta="தவறானது. கட்சிகள் கலைக்கப்படாது.",
        why_d_en="Incorrect. MCC applies to all parliamentary and assembly elections.",
        why_d_ta="தவறானது. இது அனைத்து சட்டமன்ற மற்றும் நாடாளுமன்ற தேர்தல்களுக்கும் பொருந்தும்.",
        tip_en="Standing Parliamentary Committee on Personnel, Public Grievances, Law and Justice (2013) had recommended giving statutory backing to MCC.",
        tip_ta="நாடாளுமன்ற நிலைக்குழு (2013) MCC-க்கு சட்ட அந்தஸ்து வழங்க பரிந்துரைத்தது; ஆனால் ECI அதை ஏற்கவில்லை.",
        fact_en="ECI temporarily bars campaigning leaders using its inherent powers under Article 324.",
        fact_ta="சரத்து 324-ன் கீழான உள்ளார்ந்த அதிகாரத்தைப் பயன்படுத்தி விதிமீறும் தலைவர்களுக்கு தற்காலிக பிரச்சார தடையை ECI விதிக்கிறது.",
        tags=["MCC Non-Statutory Rationale", "Article 324", "Speedy Enforcement"]
    ))

    # ER_M_039
    qs.append(make_er_q(
        qid="ER_M_039", diff="Medium", qtype="Single-Choice", subtopic="Delimitation Commission",
        en_stem="Under Article 329(a) and the Delimitation Act, how did the Supreme Court characterize the legal status of an order issued by the Delimitation Commission in Meghraj Kothari v. Delimitation Commission (1967)?",
        ta_stem="சரத்து 329(a) மற்றும் மறுவரையறை சட்டத்தின் கீழ், மேக்ராஜ் கோத்தாரி வழக்கில் (1967) தொகுதி மறுவரையறை ஆணையத்தின் உத்தரவுகளின் சட்டப்பூர்வ அந்தஸ்தை உச்ச நீதிமன்றம் எவ்வாறு விவரித்தது?",
        en_a="Once published in the Gazette, Delimitation orders acquire the force of law and cannot be questioned in any court", ta_a="அரசிதழில் வெளியிடப்பட்டவுடன், மறுவரையறை ஆணைகள் சட்டத்தின் முழு அந்தஸ்தைப் பெறுகின்றன; எந்தவொரு நீதிமன்றத்திலும் அவற்றை எதிர்த்து கேள்வி கேட்க முடியாது",
        en_b="Delimitation orders are mere preliminary recommendations that require ratification by every state legislature", ta_b="அவை வெறும் ஆரம்பப் பரிந்துரைகள் மட்டுமே; ஒவ்வொரு மாநில சட்டமன்றமும் அவற்றை அங்கீகரிக்க வேண்டும்",
        en_c="Delimitation orders can be stayed by any District Court upon a voter's petition", ta_c="வாக்காளரின் மனுவின் பேரில் எந்தவொரு மாவட்ட நீதிமன்றமும் தடை விதிக்க முடியும்",
        en_d="Delimitation orders lapse automatically after 1 year if not approved by the Supreme Court", ta_d="உச்ச நீதிமன்றத்தால் அங்கீகரிக்கப்படாவிட்டால் 1 ஆண்டில் தானாக காலாவதியாகிவிடும்",
        correct_key="A",
        exp_en="In Meghraj Kothari v. Delimitation Commission (1967), the Supreme Court held that once the Delimitation Commission publishes its final orders in the Gazette of India under the Delimitation Act, they acquire the full force of law and, by virtue of Article 329(a), cannot be called in question in any court of law.",
        exp_ta="மேக்ராஜ் கோத்தாரி (1967) வழக்கில், தொகுதி மறுவரையறை ஆணையம் தனது இறுதி உத்தரவை அரசிதழில் வெளியிட்டவுடன், அது நாடாளுமன்ற சட்டத்தின் முழு அந்தஸ்தைப் பெறுகிறது என்றும், சரத்து 329(a)-ன் படி எந்த நீதிமன்றமும் அதை மறுஆய்வு செய்ய முடியாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        why_a_en="Correct. Acquires full force of law; immune from judicial challenge under Article 329(a).",
        why_a_ta="சரியானது. சட்ட அந்தஸ்து பெறுகிறது; சரத்து 329(a)-ன் கீழ் நீதிமன்ற தலையீட்டிலிருந்து முழு விலக்கு உண்டு.",
        why_b_en="Incorrect. State legislatures have no ratification role.",
        why_b_ta="தவறானது. சட்டமன்றங்களின் ஒப்புதல் தேவையில்லை.",
        why_c_en="Incorrect. No court can question it.",
        why_c_ta="தவறானது. நீதிமன்றங்கள் கேள்வி கேட்க முடியாது.",
        why_d_en="Incorrect. The orders remain permanently in force until the next delimitation.",
        why_d_ta="தவறானது. அடுத்த மறுவரையறை வரை தொடர்ந்து அமலில் இருக்கும்.",
        tip_en="Article 329(a) bars the interference of courts in electoral matters concerning delimitation or allotment of seats.",
        tip_ta="சரத்து 329(a) தொகுதி மறுவரையறை அல்லது இட ஒதுக்கீடு தொடர்பான விவகாரங்களில் நீதிமன்றங்கள் தலையிடுவதைத் தடை செய்கிறது.",
        fact_en="India has constituted four Delimitation Commissions so far: in 1952, 1962, 1972, and 2002.",
        fact_ta="இந்தியாவில் இதுவரை நான்கு முறை (1952, 1962, 1972, 2002) தொகுதி மறுவரையறை ஆணையங்கள் அமைக்கப்பட்டுள்ளன.",
        tags=["Meghraj Kothari 1967", "Delimitation Orders", "Article 329(a)"]
    ))

    # ER_M_040
    qs.append(make_er_q(
        qid="ER_M_040", diff="Medium", qtype="Single-Choice", subtopic="First-Past-The-Post System",
        en_stem="Which major electoral reform was recommended by the 170th Law Commission Report (1999) to address the drawback of the First-Past-The-Post (FPTP) system where a party can win a majority of seats with a minority of popular votes?",
        ta_stem="குறைந்த வாக்கு சதவீதத்தைப் பெற்ற ஒரு கட்சி அதிக இடங்களை வெல்லும் முதல்-நிலைக் கடந்தவர் வெற்றி (FPTP) முறையின் குறையை சரிசெய்ய, 170-வது சட்ட ஆணைய அறிக்கை (1999) பரிந்துரைத்த முக்கிய தேர்தல் சீர்திருத்தம் எது?",
        en_a="Introducing an additional 25% seats filled through the Proportional Representation List System", ta_a="விகிதாச்சார பிரதிநிதித்துவப் பட்டியல் முறை (List System) மூலம் நிரப்பப்படும் கூடுதல் 25% இடங்களை அறிமுகப்படுத்துவது",
        en_b="Abolishing the Lok Sabha and replacing it with a nominated technocratic senate", ta_b="மக்களவையை ஒழித்துவிட்டு நியமன நிபுணர் அவையை உருவாக்குவது",
        en_c="Mandating that every candidate must secure at least 90% of votes to win", ta_c="வெற்றி பெற ஒவ்வொரு வேட்பாளரும் குறைந்தது 90% வாக்குகளைப் பெற வேண்டும் எனக் கட்டாயமாக்குவது",
        en_d="Restricting the right to vote only to income-tax paying citizens", ta_d="வருமான வரி செலுத்துவோருக்கு மட்டுமே வாக்குரிமை என கட்டுப்படுத்துவது",
        correct_key="A",
        exp_en="The 170th Law Commission Report (1999) recommended increasing the strength of the Lok Sabha by 25% (adding ~136 seats) and filling these additional seats through the Proportional Representation (List System), creating a hybrid electoral model similar to Germany's Mixed Member Proportional (MMP) system.",
        exp_ta="170-வது சட்ட ஆணைய அறிக்கை (1999), மக்களவை இடங்களின் எண்ணிக்கையை 25% அதிகரித்து (~136 இடங்கள்), அந்த கூடுதல் இடங்களை விகிதாச்சார பட்டியல் முறை (List System) மூலம் நிரப்ப பரிந்துரைத்தது; இது ஜெர்மனியின் கலப்பு தேர்தல் முறை போன்றதாகும்.",
        why_a_en="Correct. 25% additional seats filled via List System of Proportional Representation.",
        why_a_ta="சரியானது. பட்டியல் முறை மூலம் நிரப்பப்படும் 25% கூடுதல் இடங்கள்.",
        why_b_en="Incorrect. Abolishing Lok Sabha is contrary to democracy.",
        why_b_ta="தவறானது. மக்களவையை ஒழிப்பது ஜனநாயகத்திற்கு எதிரானது.",
        why_c_en="Incorrect. 90% threshold is impossible in multi-candidate elections.",
        why_c_ta="தவறானது. நடைமுறைக்கு சாத்தியமற்றது.",
        why_d_en="Incorrect. India is committed to Universal Adult Suffrage under Article 326.",
        why_d_ta="தவறானது. இந்தியா வயதுவந்தோர் அனைவருக்கும் வாக்குரிமை அளித்துள்ளது.",
        tip_en="In the 2014 Lok Sabha elections, a party won 282 seats (52% of seats) with 31% of the national vote share, illustrating the manufactured majority under FPTP.",
        tip_ta="2014 மக்களவைத் தேர்தலில் 31% வாக்குகள் பெற்ற ஒரு கட்சி 282 இடங்களை (52%) வென்றது, இது FPTP முறையின் போக்கைக் காட்டுகிறது.",
        fact_en="NCRWC (2002) also examined the Proportional Representation system but concluded that FPTP remains better suited for India's stability and local accountability.",
        fact_ta="NCRWC (2002) இம்முறையை ஆராய்ந்த போதிலும், இந்தியாவின் ஸ்திரத்தன்மைக்கு FPTP முறையே சிறந்தது என முடிவு செய்தது.",
        tags=["170th Law Commission", "Proportional Representation", "List System", "FPTP Alternative"]
    ))

    # ER_M_041
    qs.append(make_er_q(
        qid="ER_M_041", diff="Medium", qtype="Single-Choice", subtopic="State Funding Debates",
        en_stem="Why did the Indrajit Gupta Committee (1998) strictly recommend that State Funding of Elections should be provided ONLY in KIND (facilities, paper, fuel) and NOT in cash?",
        ta_stem="தேர்தல்களுக்கான அரசு நிதியுதவி ரொக்கப் பணமாக இல்லாமல், பொருள் உதவியாக (காகிதம், எரிபொருள், ஒளிபரப்பு நேரம்) மட்டுமே வழங்கப்பட வேண்டும் என்று இந்திரஜித் குப்தா குழு (1998) திட்டவட்டமாக பரிந்துரைத்தது ஏன்?",
        en_a="To prevent the diversion and siphoning of cash funds by unscrupulous parties, ensuring aid directly translates into campaign facilities", ta_a="ரொக்கப் பணம் தவறாகப் பயன்படுத்தப்படுவதையும் திசைதிருப்பப்படுவதையும் தடுத்து, உதவி நேரடியாக பிரச்சார வசதிகளுக்குப் பயன்படுவதை உறுதி செய்ய",
        en_b="Because the Reserve Bank of India has a shortage of physical paper currency during election years", ta_b="தேர்தல் ஆண்டுகளில் ரிசர்வ் வங்கியிடம் ரூபாய் நோட்டுகள் தட்டுப்பாடு ஏற்படும் என்பதால்",
        en_c="Because cash transactions are prohibited under the Constitution of India", ta_c="இந்திய அரசியலமைப்பின் கீழ் ரொக்கப் பரிவர்த்தனைகள் தடை செய்யப்பட்டுள்ளன என்பதால்",
        en_d="Because political parties do not have registered bank accounts to accept cash", ta_d="அரசியல் கட்சிகளிடம் வங்கி கணக்குகள் இருக்காது என்பதால்",
        correct_key="A",
        exp_en="The Indrajit Gupta Committee recognized that providing direct cash subsidies to political parties would lead to misuse, embezzlement, and creation of dummy parties solely to collect state money. Therefore, it strictly restricted state funding to non-cash assistance in kind (free airtime, designated premises, printing paper, petrol/diesel, loudspeakers, and copies of electoral rolls).",
        exp_ta="நேரடியாக ரொக்கப் பணம் வழங்கினால் அரசியல் கட்சிகள் அதை தவறாகப் பயன்படுத்தவும், அரசுப் பணத்தைப் பெறுவதற்காகவே போலி கட்சிகள் தோன்றவும் வழிவகுக்கும் என்பதை உணர்ந்த இந்திரஜித் குப்தா குழு, இலவச ஒளிபரப்பு நேரம், காகிதம், எரிபொருள், ஒலிபெருக்கிகள் போன்ற பொருளுதவி வடிவில் மட்டுமே நிதியுதவி வழங்கப்பட வேண்டும் என பரிந்துரைத்தது.",
        why_a_en="Correct. Prevents corruption, cash diversion, and emergence of bogus parties.",
        why_a_ta="சரியானது. ஊழல், நிதி திசைதிருப்பல் மற்றும் போலி கட்சிகள் உருவாவதைத் தடுக்கிறது.",
        why_b_en="Incorrect. Currency shortage is false.",
        why_b_ta="தவறானது. ரூபாய் நோட்டு தட்டுப்பாடு தவறான காரணம்.",
        why_c_en="Incorrect. Cash transactions are not unconstitutional.",
        why_c_ta="தவறானது. அரசியலமைப்பு தடை விதிக்கவில்லை.",
        why_d_en="Incorrect. All recognized parties maintain bank accounts.",
        why_d_ta="தவறானது. அனைத்து கட்சிகளுக்கும் வங்கிக் கணக்குகள் உண்டு.",
        tip_en="The committee also recommended establishing a dedicated National Election Fund with joint contributions from Centre and States.",
        tip_ta="மத்திய மற்றும் மாநில அரசுகளின் பங்களிப்புடன் தேசிய தேர்தல் நிதியை (National Election Fund) உருவாக்கவும் இக்குழு பரிந்துரைத்தது.",
        fact_en="Second Administrative Reforms Commission (2007) also endorsed partial state funding to reduce the role of illicit black money.",
        fact_ta="இரண்டாவது நிர்வாக சீர்திருத்த ஆணையமும் (2007) கறுப்புப் பண ஆதிக்கத்தைக் குறைக்க பகுதி அரசு நிதியுதவியை ஆதரித்தது.",
        tags=["Indrajit Gupta 1998", "Funding in Kind", "State Funding of Elections"]
    ))

    # ER_M_042
    qs.append(make_er_q(
        qid="ER_M_042", diff="Medium", qtype="Single-Choice", subtopic="Model Code of Conduct Powers",
        en_stem="Which constitutional power enables the Election Commission of India to take administrative actions—such as transferring biased police officers or postponing elections—which are not explicitly spelled out in the RPA statutes?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டங்களில் வெளிப்படையாகக் குறிப்பிடப்படாத போதிலும், ஒருதலைப்பட்சமாக செயல்படும் அதிகாரிகளை மாற்றுவது அல்லது தேர்தலை ஒத்திவைப்பது போன்ற நிர்வாக நடவடிக்கைகளை எடுக்க ECI-க்கு அதிகாரம் அளிக்கும் அரசியலமைப்பு சரத்து எது?",
        en_a="Plenary powers under Article 324 (Superintendence, direction, and control)", ta_a="சரத்து 324-ன் கீழான முழுமையான வரம்பற்ற அதிகாரங்கள் (மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாடு)",
        en_b="Advisory jurisdiction under Article 143", ta_b="சரத்து 143-ன் கீழான ஆலோசனை அதிகார வரம்பு",
        en_c="Ordinance making power under Article 123", ta_c="சரத்து 123-ன் கீழான அவசரச் சட்டம் இயற்றும் அதிகாரம்",
        en_d="Writ jurisdiction under Article 32", ta_d="சரத்து 32-ன் கீழான நீதிப்பேராணை அதிகாரம்",
        correct_key="A",
        exp_en="In Mohinder Singh Gill v. Chief Election Commissioner (1978), the Supreme Court ruled that Article 324 operates as a reservoir of plenary administrative power. Where statutory law is silent, the Election Commission can draw upon its inherent powers under Article 324 to ensure free and fair elections.",
        exp_ta="மொஹிந்தர் சிங் கில் (1978) வழக்கில், சரத்து 324 தேர்தல் ஆணையத்திற்கு ஒரு பரந்த அதிகாரக் களஞ்சியமாக செயல்படுகிறது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. சட்டம் அமைதியாக இருக்கும் இடங்களில், சுதந்திரமான நியாயமான தேர்தலை உறுதி செய்ய சரத்து 324-ன் கீழ் ECI தன்னிச்சையான நடவடிக்கைகளை எடுக்க முடியும்.",
        why_a_en="Correct. Plenary powers under Article 324 cover unprovided fields.",
        why_a_ta="சரியானது. சரத்து 324 சட்டம் குறிப்பிடாத பகுதிகளையும் உள்ளடக்கும் பரந்த அதிகாரத்தை வழங்குகிறது.",
        why_b_en="Incorrect. Article 143 is the President's power to consult the Supreme Court.",
        why_b_ta="தவறானது. சரத்து 143 குடியரசுத் தலைவரின் ஆலோசனை வரம்பு.",
        why_c_en="Incorrect. Article 123 is the President's ordinance power.",
        why_c_ta="தவறானது. சரத்து 123 குடியரசுத் தலைவரின் அவசரச் சட்ட அதிகாரம்.",
        why_d_en="Incorrect. Article 32 is Supreme Court's writ jurisdiction.",
        why_d_ta="தவறானது. சரத்து 32 உச்ச நீதிமன்றத்தின் நீதிப்பேராணை அதிகாரம்.",
        tip_en="Mohinder Singh Gill (1978) is the foundational precedent for ECI's independent executive authority.",
        tip_ta="மொஹிந்தர் சிங் கில் வழக்கு ECI-ன் தன்னாட்சி அதிகாரத்திற்கான மிக முக்கிய முன்மாதிரியாகும்.",
        fact_en="However, the court cautioned that Article 324 cannot be exercised in direct contravention of a valid statute passed by Parliament.",
        fact_ta="இருப்பினும், நாடாளுமன்றம் இயற்றிய சட்டத்திற்கு நேர் மாறாக சரத்து 324-ஐப் பயன்படுத்த முடியாது என நீதிமன்றம் எச்சரித்தது.",
        tags=["Article 324", "Mohinder Singh Gill 1978", "Plenary Powers", "ECI Authority"]
    ))

    # ER_M_043
    qs.append(make_er_q(
        qid="ER_M_043", diff="Medium", qtype="Single-Choice", subtopic="Disqualification on Framing of Charges",
        en_stem="Why did the Law Commission of India (244th Report) and the Second Administrative Reforms Commission (4th Report) recommend that disqualification of candidates should occur at the stage of 'framing of charges' by a court, rather than awaiting final conviction?",
        ta_stem="இறுதி தண்டனைத் தீர்ப்பு வரும் வரை காத்திருக்காமல், நீதிமன்றத்தால் 'குற்றச்சாட்டுகள் பதிவு செய்யப்படும்' (Framing of charges) நிலையிலேயே வேட்பாளர்களை தகுதிநீக்கம் செய்ய வேண்டும் என்று சட்ட ஆணையமும் (244-வது அறிக்கை) இரண்டாவது ARC-யும் பரிந்துரைத்தது ஏன்?",
        en_a="Because criminal trials in India take decades to conclude, allowing tainted persons to contest multiple elections and hold ministerial office while on trial", ta_a="இந்தியாவில் குற்றவியல் வழக்குகள் முடிய பல தசாப்தங்கள் ஆவதால், குற்றம் சாட்டப்பட்டவர்கள் பல தேர்தல்களில் போட்டியிட்டு அமைச்சராகவும் நீடிப்பதைத் தடுக்க",
        en_b="Because the Indian Penal Code explicitly mandates that framed charges equal proven guilt", ta_b="குற்றச்சாட்டு பதிவு செய்யப்பட்டாலே குற்றம் நிரூபிக்கப்பட்டதாக IPC கூறுவதால்",
        en_c="Because the Supreme Court has abolished the presumption of innocence in electoral cases", ta_c="தேர்தல் வழக்குகளில் குற்றமற்றவர் என்ற அனுமானத்தை உச்ச நீதிமன்றம் நீக்கிவிட்டது என்பதால்",
        en_d="Because political parties have requested the government to automatically disqualify all opposition members", ta_d="எதிர்க்கட்சி உறுப்பினர்களை தகுதிநீக்கம் செய்ய கட்சிகள் கோரியதால்",
        correct_key="A",
        exp_en="Both the 244th Law Commission Report (2014) and the 2nd ARC Report on Ethics in Governance (2007) pointed out that criminal trials in India suffer from enormous judicial delay, often taking 15-20 years. Awaiting final conviction allows politicians facing heinous charges (murder, rape, extortion) to serve multiple legislative terms.",
        exp_ta="இந்தியாவில் குற்றவியல் வழக்குகள் முடிய 15-20 ஆண்டுகள் ஆவதால், கொலை, பாலியல் வன்கொடுமை போன்ற கொடூரக் குற்றச்சாட்டுகளை எதிர்கொள்ளும் அரசியல்வாதிகள் வழக்கு முடியும் வரை தொடர்ந்து பல தேர்தல்களில் போட்டியிட்டு சட்டமியற்றுபவர்களாகத் திகழ்வதை முடிவுக்குக் கொண்டுவரவே இப்பரிந்துரை முன்வைக்கப்பட்டது.",
        why_a_en="Correct. Massive trial delays allow tainted politicians to retain power for decades.",
        why_a_ta="சரியானது. நீதிமன்ற விசாரணையில் ஏற்படும் நீண்ட தாமதத்தால் குற்றப்பின்னணி கொண்டோர் தொடர்ந்து ஆட்சியில் நீடிப்பதைத் தடுக்க.",
        why_b_en="Incorrect. Framing of charges does not establish guilt under IPC.",
        why_b_ta="தவறானது. குற்றச்சாட்டு பதிவு குற்றத்தை நிரூபிக்காது.",
        why_c_en="Incorrect. Presumption of innocence remains a core doctrine of Indian jurisprudence.",
        why_c_ta="தவறானது. குற்றமற்றவர் என்ற அனுமானம் தொடர்கிறது.",
        why_d_en="Incorrect. Frivolous option.",
        why_d_ta="தவறானது. பொருத்தமற்ற காரணம்.",
        tip_en="To prevent political vendetta, both reports recommended that only charges framed at least one year before the election for offences punishable with 5+ years prison should trigger disqualification.",
        tip_ta="அரசியல் பழிவாங்கலைத் தடுக்க, 5 ஆண்டுகள் சிறை தண்டனைக்குரிய குற்றங்களில் தேர்தலுக்கு 1 ஆண்டுக்கு முன் பதிவு செய்யப்பட்ட குற்றச்சாட்டுகளை மட்டுமே பரிசீலிக்க பரிந்துரைக்கப்பட்டது.",
        fact_en="Parliament has not yet enacted this recommendation into law due to political resistance.",
        fact_ta="அரசியல் கட்சிகளின் தயக்கம் காரணமாக நாடாளுமன்றம் இன்னும் இச்சீர்திருத்தத்தை சட்டமாக்கவில்லை.",
        tags=["Framing of Charges", "244th Law Commission", "Second ARC", "Judicial Delays"]
    ))

    # ER_M_044
    qs.append(make_er_q(
        qid="ER_M_044", diff="Medium", qtype="Single-Choice", subtopic="106th Constitutional Amendment Act 2023",
        en_stem="Which newly inserted Article under the 106th Constitutional Amendment Act, 2023 provides for the reservation of seats for women in the Legislative Assemblies of the States?",
        ta_stem="106-வது அரசியலமைப்புச் சட்டத்திருத்தம் 2023-ன் மூலம் புதிதாக இணைக்கப்பட்ட எந்த சரத்து, மாநில சட்டமன்றங்களில் பெண்களுக்கு இடஒதுக்கீட்டை வழங்குகிறது?",
        en_a="Article 332A", ta_a="சரத்து 332A",
        en_b="Article 330A", ta_b="சரத்து 330A",
        en_c="Article 334A", ta_c="சரத்து 334A",
        en_d="Article 239AA(2)(ba)", ta_d="சரத்து 239AA(2)(ba)",
        correct_key="A",
        exp_en="The 106th Constitutional Amendment Act, 2023 inserted Article 332A to provide that seats shall be reserved for women in the Legislative Assembly of every State (including one-third of the seats reserved for SCs and STs). Article 330A provides women reservation in Lok Sabha.",
        exp_ta="106-வது அரசியலமைப்புச் சட்டத்திருத்தம் 2023, சரத்து 332A-ஐ இணைத்து ஒவ்வொரு மாநில சட்டமன்றத்திலும் பெண்களுக்கு மூன்றில் ஒரு பங்கு (33%) இடஒதுக்கீட்டை வழங்குகிறது. சரத்து 330A மக்களவைக்கான மகளிர் இடஒதுக்கீட்டைக் கையாள்கிறது.",
        why_a_en="Correct. Article 332A governs women reservation in State Legislative Assemblies.",
        why_a_ta="சரியானது. சரத்து 332A மாநில சட்டமன்றங்களுக்கான மகளிர் இடஒதுக்கீட்டை வழங்குகிறது.",
        why_b_en="Incorrect. Article 330A governs women reservation in the Lok Sabha (House of the People).",
        why_b_ta="தவறானது. சரத்து 330A மக்களவைக்கான மகளிர் இடஒதுக்கீடு பற்றியது.",
        why_c_en="Incorrect. Article 334A contains the commencement and 15-year sunset clause.",
        why_c_ta="தவறானது. சரத்து 334A நடைமுறைப்படுத்தல் மற்றும் 15 ஆண்டு கால வரம்பு பற்றியது.",
        why_d_en="Incorrect. Article 239AA(2)(ba) provides women reservation in the Delhi Legislative Assembly.",
        why_d_ta="தவறானது. சரத்து 239AA(2)(ba) டெல்லி சட்டமன்றத்திற்கான மகளிர் இடஒதுக்கீடு.",
        tip_en="Memory trick: 330 = Lok Sabha SC/ST -> 330A = Lok Sabha Women; 332 = Assembly SC/ST -> 332A = Assembly Women.",
        tip_ta="நினைவு உத்தி: 330 மக்களவை SC/ST -> 330A மக்களவை பெண்கள்; 332 சட்டசபை SC/ST -> 332A சட்டசபை பெண்கள்.",
        fact_en="Seats reserved for women will be rotated after each subsequent delimitation exercise under Parliament law.",
        fact_ta="ஒவ்வொரு தொகுதி மறுவரையறைக்குப் பிறகும் பெண்களுக்கு ஒதுக்கப்பட்ட தொகுதிகள் சுழற்சி முறையில் மாற்றப்படும்.",
        tags=["Article 332A", "Women Reservation", "106th Amendment"]
    ))

    # ER_M_045
    qs.append(make_er_q(
        qid="ER_M_045", diff="Medium", qtype="Single-Choice", subtopic="106th Constitutional Amendment Act 2023",
        en_stem="Under Article 330A and 332A of the Constitution, what sub-quota is provided for women belonging to Scheduled Castes and Scheduled Tribes within the 33% women's reservation?",
        ta_stem="அரசியலமைப்பின் சரத்து 330A மற்றும் 332A-ன் கீழ், பெண்களுக்கான 33% இடஒதுக்கீட்டிற்குள் பட்டியல் சாதியினர் (SC) மற்றும் பழங்குடியினர் (ST) பெண்களுக்கு வழங்கப்படும் உள்-ஒதுக்கீடு என்ன?",
        en_a="One-third (1/3rd) of the total seats reserved for SCs and STs respectively", ta_a="முறையே SC மற்றும் ST பிரிவினருக்கு ஒதுக்கப்பட்ட மொத்த இடங்களில் மூன்றில் ஒரு பங்கு (1/3)",
        en_b="A separate flat 50% reservation across all constituencies", ta_b="அனைத்து தொகுதிகளிலும் தனித்தனியாக 50% இடஒதுக்கீடு",
        en_c="No sub-quota is provided; it is purely on general merit", ta_c="உள்-ஒதுக்கீடு எதுவும் இல்லை; பொது தகுதி அடிப்படையில் மட்டுமே",
        en_d="10% reservation exclusively for backward minority women", ta_d="பிற்படுத்தப்பட்ட சிறுபான்மையின பெண்களுக்கு 10% பிரத்யேக ஒதுக்கீடு",
        correct_key="A",
        exp_en="Articles 330A(2) and 332A(2) specify that as nearly as may be, one-third of the total number of seats reserved under Articles 330 and 332 for Scheduled Castes and Scheduled Tribes shall be reserved for women belonging to the Scheduled Castes or the Scheduled Tribes.",
        exp_ta="சரத்து 330A(2) மற்றும் 332A(2)-ன் படி, சரத்து 330 மற்றும் 332-ன் கீழ் SC மற்றும் ST பிரிவினருக்கு ஒதுக்கப்பட்ட மொத்த இடங்களில் மூன்றில் ஒரு பங்கு (33%) இடங்கள் அப்பிரிவைச் சேர்ந்த பெண்களுக்கு ஒதுக்கப்படும் (உள்-ஒதுக்கீடு).",
        why_a_en="Correct. 1/3rd of SC and ST seats are reserved for SC/ST women.",
        why_a_ta="சரியானது. SC மற்றும் ST இடங்களில் மூன்றில் ஒரு பங்கு பெண்களுக்கு ஒதுக்கப்படுகிறது.",
        why_b_en="Incorrect. 50% is not the constitutional fraction.",
        why_b_ta="தவறானது. 50% அல்ல.",
        why_c_en="Incorrect. SC/ST sub-quota is explicitly guaranteed.",
        why_c_ta="தவறானது. SC/ST உள்-ஒதுக்கீடு தெளிவாக உத்தரவாதம் செய்யப்பட்டுள்ளது.",
        why_d_en="Incorrect. There is no OBC or minority sub-quota in the 106th Amendment.",
        why_d_ta="தவறானது. OBC அல்லது சிறுபான்மையினருக்கான உள்-ஒதுக்கீடு இதில் இல்லை.",
        tip_en="The lack of an OBC sub-quota in the 106th Amendment was the primary point of debate raised by opposition parties in Parliament.",
        tip_ta="106-வது சட்டத்திருத்தத்தில் OBC பெண்களுக்கான உள்-ஒதுக்கீடு இல்லாததே நாடாளுமன்றத்தில் பிரதான விவாதப் புள்ளியாக அமைந்தது.",
        fact_en="This horizontal reservation ensures that intersectional representation of marginalized women is constitutionally guaranteed.",
        fact_ta="இந்த கிடைமட்ட இடஒதுக்கீடு விளிம்புநிலை பெண்களின் பிரதிநிதித்துவத்தை உறுதி செய்கிறது.",
        tags=["Article 330A", "SC ST Women Sub-Quota", "106th Amendment"]
    ))

    # ER_M_046
    qs.append(make_er_q(
        qid="ER_M_046", diff="Medium", qtype="Single-Choice", subtopic="Delimitation Commission Composition",
        en_stem="Who serves as the ex-officio members of the Delimitation Commission constituted by the Central Government under the Delimitation Act, 2002?",
        ta_stem="மறுவரையறை சட்டம் 2002-ன் கீழ் மத்திய அரசால் அமைக்கப்படும் தொகுதி மறுவரையறை ஆணையத்தில் அலுவல்சார் உறுப்பினர்களாக (Ex-officio members) யார் செயல்படுகின்றனர்?",
        en_a="Chief Election Commissioner (or an EC nominated by him) and the State Election Commissioner of the concerned State", ta_a="தலைமைத் தேர்தல் ஆணையர் (அல்லது அவரால் பரிந்துரைக்கப்படும் ஒரு ஆணையர்) மற்றும் சம்பந்தப்பட்ட மாநில தேர்தல் ஆணையர்",
        en_b="Union Law Minister and Speaker of the State Assembly", ta_b="மத்திய சட்ட அமைச்சர் மற்றும் மாநில சட்டமன்ற சபாநாயகர்",
        en_c="Cabinet Secretary and Chief Secretary of the State", ta_c="மத்திய கேபினட் செயலாளர் மற்றும் மாநில தலைமைச் செயலாளர்",
        en_d="Attorney General of India and Advocate General of the State", ta_d="இந்திய அட்டர்னி ஜெனரல் மற்றும் மாநில அட்வகேட் ஜெனரல்",
        correct_key="A",
        exp_en="Under Section 3 of the Delimitation Act, 2002, the Delimitation Commission consists of three members: (1) Chairperson, who is a retired or serving Supreme Court Judge appointed by the Centre, (2) the Chief Election Commissioner or an Election Commissioner nominated by CEC (ex-officio), and (3) the State Election Commissioner of the State concerned (ex-officio).",
        exp_ta="தொகுதி மறுவரையறை சட்டம் 2002 பிரிவு 3-ன் படி, ஆணையத்தில் 3 உறுப்பினர்கள் உள்ளனர்: (1) தலைவர் – ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதி, (2) தலைமை தேர்தல் ஆணையர் அல்லது அவரால் நியமிக்கப்படும் தேர்தல் ஆணையர் (அலுவல்சார்), (3) சம்பந்தப்பட்ட மாநில தேர்தல் ஆணையர் (அலுவல்சார்).",
        why_a_en="Correct. CEC (or EC) and concerned State Election Commissioner are the two ex-officio members.",
        why_a_ta="சரியானது. CEC மற்றும் மாநில தேர்தல் ஆணையர் ஆகியோர் அலுவல்சார் உறுப்பினர்கள் ஆவர்.",
        why_b_en="Incorrect. Law Minister is not on the commission.",
        why_b_ta="தவறானது. சட்ட அமைச்சர் உறுப்பினரல்ல.",
        why_c_en="Incorrect. Chief Secretary is not a member.",
        why_c_ta="தவறானது. தலைமைச் செயலாளர் உறுப்பினரல்ல.",
        why_d_en="Incorrect. Law officers are not members.",
        why_d_ta="தவறானது. அரசு வழக்கறிஞர்கள் உறுப்பினரல்ல.",
        tip_en="In addition, 5 Lok Sabha MPs and 5 State MLAs from each state are nominated by the Speaker as Associate Members (without voting power).",
        tip_ta="கூடுதலாக, ஒவ்வொரு மாநிலத்திலிருந்தும் 5 மக்களவை எம்.பி.க்கள் மற்றும் 5 எம்.எல்.ஏ.க்கள் வாக்குரிமையற்ற இணை உறுப்பினர்களாக (Associate Members) நியமிக்கப்படுகின்றனர்.",
        fact_en="The 2002 Commission chaired by Justice Kuldip Singh redrew constituency boundaries across the country.",
        fact_ta="நீதிபதி குல்தீப் சிங் தலைமையிலான 2002 ஆணையம் நாடு முழுவதும் தொகுதி எல்லைகளை மாற்றியமைத்தது.",
        tags=["Delimitation Commission Composition", "Section 3", "Justice Kuldip Singh"]
    ))

    # ER_M_047
    qs.append(make_er_q(
        qid="ER_M_047", diff="Medium", qtype="Single-Choice", subtopic="Electoral Trusts Scheme",
        en_stem="Under the Electoral Trusts Scheme notified by the Central Government in 2013, what minimum percentage of the total contributions received in a financial year must an Electoral Trust distribute to registered political parties?",
        ta_stem="மத்திய அரசால் 2013-ல் அறிவிக்கப்பட்ட தேர்தல் அறக்கட்டளைகள் (Electoral Trusts) திட்டத்தின் கீழ், ஒரு நிதியாண்டில் பெறப்பட்ட மொத்த நன்கொடைகளில் குறைந்தபட்சம் எத்தனை சதவீதத்தை அரசியல் கட்சிகளுக்கு அறக்கட்டளை விநியோகிக்க வேண்டும்?",
        en_a="95% of total contributions", ta_a="மொத்த நன்கொடைகளில் 95%",
        en_b="50% of total contributions", ta_b="மொத்த நன்கொடைகளில் 50%",
        en_c="75% of total contributions", ta_c="மொத்த நன்கொடைகளில் 75%",
        en_d="80% of total contributions", ta_d="மொத்த நன்கொடைகளில் 80%",
        correct_key="A",
        exp_en="Under the Electoral Trusts Scheme, 2013 framed under Section 17CA of the Income Tax Act, an approved Electoral Trust must distribute at least 95% of the total contributions received by it in any financial year to eligible registered political parties, retaining not more than 5% for administrative expenses.",
        exp_ta="வருமான வரிச் சட்டம் பிரிவு 17CA-ன் கீழான தேர்தல் அறக்கட்டளைகள் திட்டம் 2013-ன் படி, ஓர் அங்கீகரிக்கப்பட்ட தேர்தல் அறக்கட்டளை தான் ஒரு நிதியாண்டில் திரட்டிய மொத்த நன்கொடைகளில் குறைந்தது 95%-ஐ தகுதியான பதிவு செய்யப்பட்ட அரசியல் கட்சிகளுக்கு வழங்க வேண்டும் (நிர்வாகச் செலவுக்கு 5% மட்டுமே வைக்கலாம்).",
        why_a_en="Correct. At least 95% must be distributed to political parties.",
        why_a_ta="சரியானது. குறைந்தது 95% தொகையை கட்சிகளுக்கு பகிர்ந்தளிக்க வேண்டும்.",
        why_b_en="Incorrect. 50% is too low.",
        why_b_ta="தவறானது. 50% மிகவும் குறைவு.",
        why_c_en="Incorrect. 75% is incorrect.",
        why_c_ta="தவறானது. 75% தவறானது.",
        why_d_en="Incorrect. 80% is incorrect.",
        why_d_ta="தவறானது. 80% தவறானது.",
        tip_en="Unlike Electoral Bonds, Electoral Trusts must submit an annual contribution report to the ECI disclosing donor names and beneficiary parties, ensuring complete transparency.",
        tip_ta="தேர்தல் பத்திரங்களைப் போலன்றி, தேர்தல் அறக்கட்டளைகள் நன்கொடை கொடுத்தோர் மற்றும் பெற்ற கட்சிகளின் விவரங்களை ECI-யிடம் வெளிப்படையாக சமர்ப்பிக்க வேண்டும்.",
        fact_en="Electoral Trusts cannot accept contributions in cash or from foreign citizens/companies.",
        fact_ta="தேர்தல் அறக்கட்டளைகள் ரொக்கமாகவோ அல்லது வெளிநாட்டு நபர்கள்/நிறுவனங்களிடமிருந்தோ நன்கொடைகளைப் பெற முடியாது.",
        tags=["Electoral Trusts 2013", "95 Percent Rule", "Political Funding"]
    ))

    # ER_M_048
    qs.append(make_er_q(
        qid="ER_M_048", diff="Medium", qtype="Single-Choice", subtopic="Foreign Contributions to Parties",
        en_stem="Under Section 29B of the Representation of the People Act, 1951, from which of the following sources is a political party strictly prohibited from accepting any political donation?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 29B-ன் கீழ், எந்த மூலத்திலிருந்து ஓர் அரசியல் கட்சி அரசியல் நன்கொடைகளைப் பெறுவது சட்டப்படி திட்டவட்டமாக தடை செய்யப்பட்டுள்ளது?",
        en_a="From a foreign source and from any Government company", ta_a="வெளிநாட்டு மூலாதாரங்கள் மற்றும் அரசு நிறுவனங்களிடமிருந்து (Government Companies)",
        en_b="From any individual Indian citizen residing in rural areas", ta_b="கிராமப்புறங்களில் வசிக்கும் தனிநபர் இந்திய குடிமக்களிடமிருந்து",
        en_c="From private Indian commercial banks", ta_c="தனியார் இந்திய வணிக வங்கிகளிடமிருந்து",
        en_d="From registered domestic non-profit societies", ta_d="பதிவு செய்யப்பட்ட உள்நாட்டு தொண்டு சங்கங்களிடமிருந்து",
        correct_key="A",
        exp_en="Section 29B of the Representation of the People Act, 1951 explicitly prohibits political parties from accepting any contribution from a 'foreign source' (as defined under Section 2(1)(j) of FCRA) or from any 'Government company' (as defined under Section 2(45) of Companies Act).",
        exp_ta="மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 29B, வெளிநாட்டு மூலாதாரங்கள் (FCRA சட்டத்தின்படி) மற்றும் அரசுக்குச் சொந்தமான பொதுத்துறை நிறுவனங்கள் (Government Companies) ஆகியவற்றிலிருந்து அரசியல் கட்சிகள் நன்கொடை பெறுவதை திட்டவட்டமாகத் தடை செய்கிறது.",
        why_a_en="Correct. Banned from foreign sources and government companies under Section 29B.",
        why_a_ta="சரியானது. வெளிநாட்டு ஆதாரங்கள் மற்றும் அரசு நிறுவனங்களிடமிருந்து நன்கொடை பெற முடியாது.",
        why_b_en="Incorrect. Indian citizens can donate freely.",
        why_b_ta="தவறானது. இந்திய குடிமக்கள் நன்கொடை அளிக்கலாம்.",
        why_c_en="Incorrect. Indian private banks can donate via statutory channels under Companies Act.",
        why_c_ta="தவறானது. தனியார் வங்கிகள் சட்ட விதிகளுக்குட்பட்டு அளிக்கலாம்.",
        why_d_en="Incorrect. Domestic societies can donate subject to their bylaws.",
        why_d_ta="தவறானது. உள்நாட்டு சங்கங்கள் நன்கொடை அளிக்கலாம்.",
        tip_en="Section 3 of the Foreign Contribution (Regulation) Act, 2010 (FCRA) also independently bars candidates, legislators, and political parties from accepting foreign funds.",
        tip_ta="FCRA சட்டம் பிரிவு 3-ம் வேட்பாளர்கள் மற்றும் கட்சிகள் வெளிநாட்டு நிதி பெறுவதைத் தடை செய்கிறது.",
        fact_en="However, the Finance Act 2016 retroactively amended FCRA's definition of 'foreign source' to exempt Indian subsidiaries of foreign companies.",
        fact_ta="2016 நிதிச் சட்டம் மூலம் FCRA-ன் 'வெளிநாட்டு மூலாதாரம்' என்ற வரையறை பின்னோக்கி திருத்தப்பட்டு வெளிநாட்டு துணை நிறுவனங்களுக்கு சில விலக்குகள் அளிக்கப்பட்டன.",
        tags=["Section 29B", "Foreign Source Bar", "Government Company Bar"]
    ))

    # ER_M_049
    qs.append(make_er_q(
        qid="ER_M_049", diff="Medium", qtype="Single-Choice", subtopic="Simultaneous Elections Recommendations",
        en_stem="What two-phase operational model was recommended by the High-Level Committee on Simultaneous Elections (Kovind Committee, 2024)?",
        ta_stem="ஒரே நேரத்தில் தேர்தல் நடத்துவது குறித்த உயர்நிலைக் குழு (கோவிந்த் குழு, 2024) பரிந்துரைத்த இரு-கட்ட செயல்பாட்டு மாதிரி எது?",
        en_a="First phase: Simultaneous elections to Lok Sabha and State Legislative Assemblies; Second phase: Municipalities and Panchayats elections within 100 days", ta_a="முதற்கட்டம்: மக்களவை மற்றும் சட்டமன்றங்களுக்கு ஒரே நேரத்தில் தேர்தல்; இரண்டாம் கட்டம்: அடுத்த 100 நாட்களுக்குள் நகராட்சி மற்றும் பஞ்சாயத்துத் தேர்தல்கள்",
        en_b="First phase: Elections in Northern states; Second phase: Elections in Southern states after 2.5 years", ta_b="முதற்கட்டம்: வட மாநிலங்களில் தேர்தல்; இரண்டாம் கட்டம்: 2.5 ஆண்டுகளுக்குப் பின் தென் மாநிலங்களில் தேர்தல்",
        en_c="First phase: Electronic voting only for urban areas; Second phase: Paper ballots for rural areas", ta_c="முதற்கட்டம்: நகர்ப்புறங்களுக்கு மட்டும் EVM; இரண்டாம் கட்டம்: கிராமப்புறங்களுக்கு காகித வாக்குச்சீட்டு",
        en_d="First phase: Presidential election; Second phase: Prime Ministerial popular election", ta_d="முதற்கட்டம்: குடியரசுத் தலைவர் தேர்தல்; இரண்டாம் கட்டம்: பிரதமர் நேரடித் தேர்தல்",
        correct_key="A",
        exp_en="The Kovind High-Level Committee (March 2024) recommended a synchronized two-step strategy: (1) in the first step, simultaneous elections will be held for the Lok Sabha and all State Legislative Assemblies through an 'Appointed Date' under a new Article 82A, and (2) in the second step, elections to Municipalities and Panchayats will be held within 100 days of the general elections under Article 324A.",
        exp_ta="கோவிந்த் குழு (2024), சரத்து 82A-ன் கீழ் முதலில் மக்களவை மற்றும் அனைத்து மாநில சட்டமன்றங்களுக்கும் ஒரே நேரத்தில் தேர்தலை நடத்தவும், பின்னர் சரத்து 324A-ன் கீழ் அடுத்த 100 நாட்களுக்குள் நகராட்சிகள் மற்றும் பஞ்சாயத்துகளுக்கு தேர்தலை நடத்தி முடிக்கவும் பரிந்துரைத்தது.",
        why_a_en="Correct. Lok Sabha + Assemblies first, followed by Local Bodies within 100 days.",
        why_a_ta="சரியானது. முதலில் மக்களவை + சட்டமன்றங்கள்; அடுத்த 100 நாட்களுக்குள் உள்ளாட்சித் தேர்தல்கள்.",
        why_b_en="Incorrect. Regional bifurcation is not the recommendation.",
        why_b_ta="தவறானது. பிராந்திய ரீதியாக பிரிக்க பரிந்துரைக்கப்படவில்லை.",
        why_c_en="Incorrect. Uniform EVM use across the nation.",
        why_c_ta="தவறானது. நாடு முழுவதும் ஒரே சீரான EVM முறை.",
        why_d_en="Incorrect. Prime Minister direct election is contrary to the Westminster model.",
        why_d_ta="தவறானது. நாடாளுமன்ற ஜனநாயகத்திற்கு எதிரானது.",
        tip_en="The committee also recommended creating a Single Electoral Roll and Single EPIC card for Lok Sabha, Assembly, and Local Body elections (amending Article 325).",
        tip_ta="அனைத்து தேர்தல்களுக்கும் ஒரே வாக்காளர் பட்டியல் மற்றும் ஒரே வாக்காளர் அட்டையை உருவாக்கவும் (சரத்து 325 திருத்தம்) இக்குழு பரிந்துரைத்தது.",
        fact_en="If a State Assembly dissolves early (hung assembly/no-confidence), fresh elections will be held only for the remainder of the unexpired term.",
        fact_ta="இடையில் ஆட்சி கவிழ்ந்தால், அடுத்த பொதுத்தேர்தல் வரையிலான எஞ்சிய காலத்திற்கு மட்டுமே புதிய சட்டமன்றம் தேர்ந்தெடுக்கப்படும்.",
        tags=["Kovind Committee 2024", "Simultaneous Elections", "Two-Phase Model", "Article 82A"]
    ))

    # ER_M_050
    qs.append(make_er_q(
        qid="ER_M_050", diff="Medium", qtype="Single-Choice", subtopic="Model Code of Conduct Guidelines",
        en_stem="Under the Model Code of Conduct, what restriction is placed on ministers and candidates regarding the use of official government vehicles, aircraft, and guest houses during election campaigns?",
        ta_stem="மாதிரி தேர்தல் நடத்தை விதிகளின் கீழ், தேர்தல் பிரச்சாரங்களின் போது அரசு வாகனங்கள், விமானங்கள் மற்றும் அரசு விருந்தினர் மாளிகைகளைப் பயன்படுத்துவது குறித்து அமைச்சர்கள் மற்றும் வேட்பாளர்கள் மீது உள்ள கட்டுப்பாடு என்ன?",
        en_a="Government transport, aircraft, and machinery cannot be used for furthering the election interests of the ruling party or any candidate", ta_a="ஆளும் கட்சி அல்லது எந்தவொரு வேட்பாளரின் தேர்தல் பிரச்சாரத்திற்காகவும் அரசு வாகனங்கள், விமானங்கள் மற்றும் இயந்திரங்களைப் பயன்படுத்தக் கூடாது",
        en_b="Ministers are permitted unlimited free use of government helicopters for political rallies", ta_b="அரசியல் பொதுக்கூட்டங்களுக்கு அரசு ஹெலிகாப்டர்களை அமைச்சர்கள் வரம்பின்றி இலவசமாகப் பயன்படுத்தலாம்",
        en_c="Only opposition party leaders are prohibited from using government circuit houses", ta_c="எதிர்க்கட்சித் தலைவர்கள் மட்டுமே அரசு விருந்தினர் மாளிகைகளைப் பயன்படுத்த தடை விதிக்கப்படுகிறது",
        en_d="Government vehicles can be used if they display party flags of all contesting parties", ta_d="அனைத்து கட்சிகளின் கொடிகளையும் கட்டினால் அரசு வாகனங்களைப் பிரச்சாரத்திற்குப் பயன்படுத்தலாம்",
        correct_key="A",
        exp_en="Part VII of the Model Code of Conduct (Party in Power) strictly mandates that government vehicles, machinery, aircraft, and personnel shall not be used for electioneering or furthering the interests of the party in power, ensuring a level playing field for all contestants.",
        exp_ta="மாதிரி தேர்தல் நடத்தை விதிகளின் பகுதி VII (ஆளும்கட்சிக்கான விதிகள்), ஆளும் கட்சியின் தேர்தல் நலனுக்காக அரசு வாகனங்கள், விமானங்கள், இயந்திரங்கள் அல்லது அரசு ஊழியர்களைப் பயன்படுத்துவதைத் திட்டவட்டமாகத் தடை செய்கிறது; அனைத்து போட்டியாளர்களுக்கும் சமமான தேர்தல் களத்தை இது உறுதி செய்கிறது.",
        why_a_en="Correct. Complete ban on combining official work with electioneering using state resources.",
        why_a_ta="சரியானது. தேர்தல் பிரச்சாரத்திற்கு அரசு வளங்கள் மற்றும் வாகனங்களைப் பயன்படுத்த முழுமையான தடை.",
        why_b_en="Incorrect. Strict prohibition applies even to the Prime Minister (except for security escort provided by SPG under security guidelines).",
        why_b_ta="தவறானது. பாதுகாப்பு நடைமுறைகள் தவிர பிரச்சாரத்திற்கு அரசு போக்குவரத்து தடை செய்யப்பட்டுள்ளது.",
        why_c_en="Incorrect. Circuit houses must be accessible to all candidates on equal terms, without monopoly by ruling party.",
        why_c_ta="தவறானது. விருந்தினர் மாளிகைகள் அனைவருக்கும் சமமாக கிடைக்க வேண்டும்.",
        why_d_en="Incorrect. Displaying party flags on government vehicles is strictly illegal.",
        why_d_ta="தவறானது. அரசு வாகனத்தில் கட்சிக் கொடி கட்டுவது சட்டவிரோதமானது.",
        tip_en="Rest houses and dak bungalows cannot be monopolised by the ruling party or its ministers.",
        tip_ta="அரசு ஓய்வு இல்லங்களை ஆளும் கட்சியோ அல்லது அமைச்சர்களோ முற்றுரிமையாக ஆக்கிரமிக்க முடியாது.",
        fact_en="Commercial payments must be made if any government property (like public grounds) is used for rallies, available on a first-come, first-served basis.",
        fact_ta="பொது மைதானங்களைப் பயன்படுத்தினால் உரிய வாடகைக் கட்டணம் செலுத்தப்பட வேண்டும், அனைவருக்கும் சம வாய்ப்பு அளிக்கப்பட வேண்டும்.",
        tags=["MCC Part VII", "Party in Power", "Misuse of Government Machinery"]
    ))

    return qs

def main():
    raw_qs = get_medium_questions()
    print(f"Total raw questions: {len(raw_qs)}")
    assert len(raw_qs) == 50, f"Expected 50, got {len(raw_qs)}"
    
    # Check ID sequence
    for idx, q in enumerate(raw_qs, 1):
        expected_id = f"ER_M_{idx:03d}"
        assert q["id"] == expected_id, f"ID mismatch at {idx}: {q['id']} != {expected_id}"
        
    # Check uniqueness of English stems
    stems = [q["question_en"].strip().lower() for q in raw_qs]
    assert len(set(stems)) == 50, f"Duplicate stems found: {len(set(stems))} unique out of 50"
    
    # Balance keys to roughly 13 A, 13 B, 12 C, 12 D
    balanced = balance_question_keys(raw_qs, target_counts={"A": 13, "B": 13, "C": 12, "D": 12})
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved to {OUTPUT_PATH}")
    
    # Validate with ContentValidator
    validator = ContentValidator()
    report = validator.validate_file(OUTPUT_PATH, expected_count=50, expected_prefix="ER_M_")
    print(report.summary())
    assert report.is_valid, "Validation failed!"

if __name__ == "__main__":
    main()
