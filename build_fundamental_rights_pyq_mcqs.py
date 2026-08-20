# -*- coding: utf-8 -*-
"""
Builder Script for Fundamental Rights 50 PYQ Practice MCQs Repository
Target Paths:
 - data/questions/polity/fundamental_rights_pyq.json
 - data/questions/polity/fundamental_rights_pyq_practice.json
"""

import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

target_path_1 = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\fundamental_rights_pyq.json")
target_path_2 = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\fundamental_rights_pyq_practice.json")

target_path_1.parent.mkdir(parents=True, exist_ok=True)

def make_pyq_q(q_id, difficulty, q_type, q_en, q_ta,
               opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
               correct_ans, exp_en, exp_ta,
               wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
               tip_en, tip_ta, rev_en, rev_ta, sources, bloom, est_time, tags):

    letters = ["A", "B", "C", "D"]
    opts_en = [opt_a_en, opt_b_en, opt_c_en, opt_d_en]
    opts_ta = [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta]

    opts = [
        {"id": letters[i], "en": opts_en[i], "ta": opts_ta[i]}
        for i in range(4)
    ]

    wnos = {
        "A": {"en": wno_a_en, "ta": wno_a_ta},
        "B": {"en": wno_b_en, "ta": wno_b_ta},
        "C": {"en": wno_c_en, "ta": wno_c_ta},
        "D": {"en": wno_d_en, "ta": wno_d_ta}
    }

    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Fundamental Rights",
        "difficulty": difficulty,
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": wnos,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": sources,
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High" if "Pattern" in sources[0] else "Exact PYQ",
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

# ==============================================================================
# 50 PYQ PRACTICE MCQS (FR_PYQ_001 to FR_PYQ_050)
# Target Answer Breakdown: A: 12, B: 12, C: 13, D: 13
# Difficulty Breakdown: Easy: 10 (20%), Medium: 26 (52%), Hard: 14 (28%)
# ==============================================================================

# FR_PYQ_001 (Easy | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_001", "Easy", "Direct MCQ",
    "Part III of the Constitution of India (Articles 12 to 35) is rightly described as which of the following?",
    "இந்திய அரசியலமைப்பின் பகுதி III (பிரிவுகள் 12 முதல் 35 வரை) பின்வருவனவற்றில் எவ்வாறு சரியாக விவரிக்கப்படுகிறது?",
    "Magna Carta of India", "இந்தியாவின் மகா சாசனம்",
    "Instrument of Instructions", "அறிவுறுத்தல் கருவி",
    "Directive Principles of Governance", "ஆளுகையின் வழிகாட்டு நெறிமுறைகள்",
    "Charter of Fundamental Duties", "அடிப்படை கடமைகளின் சாசனம்",
    "A",
    "Part III of the Indian Constitution containing Fundamental Rights (Articles 12 to 35) is described as the 'Magna Carta of India', inspired by the English Magna Carta of 1215.",
    "அடிப்படை உரிமைகளைக் (பிரிவுகள் 12 முதல் 35) கொண்ட இந்திய அரசியலமைப்பின் பகுதி III 1215-ன் ஆங்கிலேய மகா சாசனத்தால் ஈர்க்கப்பட்டு 'இந்தியாவின் மகா சாசனம்' என விவரிக்கப்படுகிறது.",
    "Correct. Part III is historically known as the Magna Carta of India.", "சரி. பகுதி III வரலாற்று ரீதியாக இந்தியாவின் மகா சாசனம் என அழைக்கப்படுகிறது.",
    "Incorrect. Instrument of Instructions refers to Directive Principles derived from the 1935 Act.", "தவறு. அறிவுறுத்தல் கருவி என்பது 1935 ஆம் ஆண்டு சட்டத்திலிருந்து பெறப்பட்ட அரசு நெறிமுறைகளைக் குறிக்கிறது.",
    "Incorrect. Directive Principles of Governance refers to Part IV.", "தவறு. ஆளுகையின் வழிகாட்டு நெறிமுறைகள் என்பது பகுதி IV-ஐக் குறிக்கிறது.",
    "Incorrect. Charter of Duties refers to Part IVA (Article 51A).", "தவறு. கடமைகளின் சாசனம் என்பது பகுதி IVA (பிரிவு 51A)-ஐக் குறிக்கிறது.",
    "TNPSC Trap: Magna Carta of India = Part III (Fundamental Rights). Instrument of Instructions = Part IV (DPSPs).",
    "TNPSC பொறி: இந்தியாவின் மகா சாசனம் = பகுதி III (அடிப்படை உரிமைகள்). அறிவுறுத்தல் கருவி = பகுதி IV (அரசு நெறிமுறைகள்).",
    "Part III (Articles 12-35) was originally borrowed from the US Bill of Rights and is called Magna Carta of India.",
    "பகுதி III (பிரிவுகள் 12-35) அமெரிக்க உரிமைகள் மசோதாவிலிருந்து பெறப்பட்டு இந்தியாவின் மகா சாசனம் என அழைக்கப்படுகிறது.",
    ["TNPSC Group 1 2022 PYQ", "M. Laxmikanth - Indian Polity"], "Remember", 45, ["Polity", "Fundamental Rights", "Part III", "Magna Carta"]
))

# FR_PYQ_002 (Easy | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_002", "Easy", "Direct MCQ",
    "Under the Constitution of India, the Right to Equality is guaranteed by a group of how many Articles?",
    "இந்திய அரசியலமைப்பின் கீழ், சமத்துவ உரிமை எத்தனை பிரிவுகளைக் கொண்ட குழுவால் உறுதி செய்யப்படுகிறது?",
    "Four Articles (Articles 14 to 17)", "நான்கு பிரிவுகள் (பிரிவுகள் 14 முதல் 17 வரை)",
    "Five Articles (Articles 14 to 18)", "ஐந்து பிரிவுகள் (பிரிவுகள் 14 முதல் 18 வரை)",
    "Six Articles (Articles 14 to 19)", "ஆறு பிரிவுகள் (பிரிவுகள் 14 முதல் 19 வரை)",
    "Three Articles (Articles 14 to 16)", "மூன்று பிரிவுகள் (பிரிவுகள் 14 முதல் 16 வரை)",
    "B",
    "The Right to Equality comprises 5 Articles: Article 14 (Equality before Law), Article 15 (Prohibition of Discrimination), Article 16 (Equality of Opportunity in Public Employment), Article 17 (Abolition of Untouchability), and Article 18 (Abolition of Titles).",
    "சமத்துவ உரிமை 5 பிரிவுகளை உள்ளடக்கியது: பிரிவு 14 (சட்டத்தின் முன் சமன்), பிரிவு 15 (பாகுபாடு தடை), பிரிவு 16 (பொது வேலைவாய்ப்பில் சம வாய்ப்பு), பிரிவு 17 (தீண்டாமை ஒழிப்பு), மற்றும் பிரிவு 18 (பட்டம் ஒழிப்பு).",
    "Incorrect. Articles 14 to 17 leaves out Article 18.", "தவறு. பிரிவுகள் 14 முதல் 17 என்பது பிரிவு 18-ஐ விட்டுவிடுகிறது.",
    "Correct. Five Articles (14, 15, 16, 17, 18) constitute the Right to Equality.", "சரி. ஐந்து பிரிவுகள் (14, 15, 16, 17, 18) சமத்துவ உரிமையை உருவாக்குகின்றன.",
    "Incorrect. Article 19 belongs to Right to Freedom, not Right to Equality.", "தவறு. பிரிவு 19 சுதந்திர உரிமைக்கு உரியது, சமத்துவ உரிமைக்கு அல்ல.",
    "Incorrect. Articles 14 to 16 covers only 3 articles.", "தவறு. பிரிவுகள் 14 முதல் 16 வரை 3 பிரிவுகளை மட்டுமே உள்ளடக்கியது.",
    "TNPSC Trap: Fundamental Rights categories count: Right to Equality (5 Articles: 14-18), Right to Freedom (4 Articles: 19-22), Right against Exploitation (2 Articles: 23-24).",
    "TNPSC பொறி: அடிப்படை உரிமை பிரிவுகள்: சமத்துவ உரிமை (5 பிரிவுகள்: 14-18), சுதந்திர உரிமை (4 பிரிவுகள்: 19-22), சுரண்டலுக்கு எதிரான உரிமை (2 பிரிவுகள்: 23-24).",
    "Original Fundamental Rights = 7 Categories. Present Fundamental Rights = 6 Categories (Property deleted by 44th CAA 1978).",
    "மூல அடிப்படை உரிமைகள் = 7 பிரிவுகள். தற்போதைய அடிப்படை உரிமைகள் = 6 பிரிவுகள் (சொத்துரிமை 44-வது திருத்தத்தால் நீக்கப்பட்டது).",
    ["TNPSC Group 2 2018 PYQ", "M. Laxmikanth - Indian Polity"], "Remember", 45, ["Polity", "Fundamental Rights", "Right to Equality", "Articles 14-18"]
))

# FR_PYQ_003 (Easy | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_003", "Easy", "Direct MCQ",
    "Article 17 of the Constitution of India deals with which of the following?",
    "இந்திய அரசியலமைப்பின் பிரிவு 17 பின்வருவனவற்றில் எதைப் பற்றிப் பேசுகிறது?",
    "Abolition of Titles", "பட்டங்கள் ஒழிப்பு",
    "Right to Free Education", "இலவசக் கல்வி உரிமை",
    "Abolition of Untouchability", "தீண்டாமை ஒழிப்பு",
    "Protection against arrest and detention", "கைது மற்றும் தடுப்புக் காவலுக்கு எதிரான பாதுகாப்பு",
    "C",
    "Article 17 of the Constitution abolishes 'Untouchability' and forbids its practice in any form. The enforcement of any disability arising out of Untouchability is made an offence punishable by law.",
    "அரசியலமைப்பின் பிரிவு 17 'தீண்டாமை'யை ஒழித்து அதன் எந்தவொரு வடிவத்தையும் தடுக்கிறது. தீண்டாமையால் ஏற்படும் இயலாமையை அமல்படுத்துவது சட்டப்படி தண்டனைக்குரிய குற்றமாகும்.",
    "Incorrect. Abolition of Titles is covered under Article 18.", "தவறு. பட்டங்கள் ஒழிப்பு பிரிவு 18-ன் கீழ் வருகிறது.",
    "Incorrect. Right to Free Education is covered under Article 21A.", "தவறு. இலவசக் கல்வி உரிமை பிரிவு 21A-ன் கீழ் வருகிறது.",
    "Correct. Article 17 deals with Abolition of Untouchability.", "சரி. பிரிவு 17 தீண்டாமை ஒழிப்பு பற்றிப் பேசுகிறது.",
    "Incorrect. Protection against arrest is covered under Article 22.", "தவறு. கைதுக்கு எதிரான பாதுகாப்பு பிரிவு 22-ன் கீழ் வருகிறது.",
    "TNPSC Trap: Parliament enacted the Untouchability (Offences) Act 1955 under Article 35, renamed as the Protection of Civil Rights Act 1955 in 1976.",
    "TNPSC பொறி: நாடாளுமன்றம் பிரிவு 35-ன் கீழ் தீண்டாமை (குற்றங்கள்) சட்டம் 1955-ஐ இயற்றியது, இது 1976-ல் உரிமைகள் பாதுகாப்புச் சட்டம் 1955 என பெயர் மாற்றம் செய்யப்பட்டது.",
    "Article 17 is an absolute right with no reasonable restrictions clause.",
    "பிரிவு 17 என்பது எந்தக் கட்டுப்பாட்டு விதியும் இல்லாத ஒரு முழுமையான அடிப்படை உரிமையாகும்.",
    ["TNPSC Group 4 2019 PYQ", "Samacheer Kalvi 10th Social"], "Remember", 45, ["Polity", "Fundamental Rights", "Article 17", "Untouchability"]
))

# FR_PYQ_004 (Easy | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_004", "Easy", "Direct MCQ",
    "Which Article of the Constitution was called the 'Heart and Soul of the Constitution' by Dr. B.R. Ambedkar?",
    "டாக்டர் பி.ஆர். அம்பேத்கர் அவர்களால் அரசியலமைப்பின் 'இதயம் மற்றும் ஆன்மா' என்று அழைக்கப்பட்ட பிரிவு எது?",
    "Article 14 (Equality before Law)", "பிரிவு 14 (சட்டத்தின் முன் சமன்)",
    "Article 19 (Right to Freedom of Speech)", "பிரிவு 19 (பேச்சு சுதந்திர உரிமை)",
    "Article 21 (Protection of Life and Liberty)", "பிரிவு 21 (வாழ்வுரிமை மற்றும் தனிநபர் சுதந்திரம்)",
    "Article 32 (Right to Constitutional Remedies)", "பிரிவு 32 (அரசியலமைப்பு பரிகார உரிமை)",
    "D",
    "Dr. B.R. Ambedkar declared Article 32 (Right to Constitutional Remedies) as the 'very soul of the Constitution and the very heart of it', because without remedies, rights are meaningless.",
    "டாக்டர் பி.ஆர். அம்பேத்கர் பிரிவு 32-ஐ (அரசியலமைப்பு பரிகார உரிமை) 'அரசியலமைப்பின் ஆன்மா மற்றும் இதயம்' என்று அறிவித்தார், ஏனெனில் பரிகாரங்கள் இன்றி உரிமைகள் அர்த்தமற்றவை.",
    "Incorrect. Article 14 guarantees equality before law.", "தவறு. பிரிவு 14 சட்டத்தின் முன் சமத்துவத்தை உறுதி செய்கிறது.",
    "Incorrect. Article 19 guarantees six fundamental freedoms.", "தவறு. பிரிவு 19 ஆறு அடிப்படை சுதந்திரங்களை உறுதி செய்கிறது.",
    "Incorrect. Article 21 guarantees protection of life and personal liberty.", "தவறு. பிரிவு 21 வாழ்வுரிமை மற்றும் தனிநபர் சுதந்திரத்தை உறுதி செய்கிறது.",
    "Correct. Article 32 was called the Heart and Soul of the Constitution by Dr. Ambedkar.", "சரி. பிரிவு 32 டாக்டர் அம்பேத்கரால் அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா என அழைக்கப்பட்டது.",
    "TNPSC Trap: Ambedkar called Article 32 the 'Heart and Soul of the Constitution'. Supreme Court in Minerva Mills called the balance between FRs & DPSPs the Basic Structure. Preamble is called the Soul of Constitution by Thakur Das Bhargava.",
    "TNPSC பொறி: அம்பேத்கர் பிரிவு 32-ஐ 'இதயம் மற்றும் ஆன்மா' என்றார். தாகூர் தாஸ் பார்கவா முகவுரையை 'அரசியலமைப்பின் ஆன்மா' என்றார்.",
    "Article 32 gives the right to move the Supreme Court directly by appropriate proceedings for enforcement of Part III rights.",
    "பகுதி III உரிமைகளை அமல்படுத்த நேரடியாக உச்சநீதிமன்றத்தை அணுகும் உரிமையை பிரிவு 32 வழங்குகிறது.",
    ["TNPSC Group 1 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Remember", 45, ["Polity", "Fundamental Rights", "Article 32", "Ambedkar"]
))

# FR_PYQ_005 (Easy | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_005", "Easy", "Direct MCQ",
    "Right to Education was inserted as a Fundamental Right under Article 21A by which Constitutional Amendment Act?",
    "எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் கல்வி உரிமை பிரிவு 21A-ன் கீழ் அடிப்படை உரிமையாக சேர்க்கப்பட்டது?",
    "86th Constitutional Amendment Act, 2002", "86-வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "91st Constitutional Amendment Act, 2003", "91-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "103rd Constitutional Amendment Act, 2019", "103-வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
    "A",
    "The 86th Constitutional Amendment Act, 2002 added Article 21A making free and compulsory education a Fundamental Right for children aged 6 to 14 years. It also changed Article 45 in DPSPs and added 11th Fundamental Duty under Article 51A(k).",
    "86-வது அரசியலமைப்பு திருத்தச் சட்டம், 2002 பிரிவு 21A-வைச் சேர்த்து 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச கட்டாயக் கல்வியை அடிப்படை உரிமையாக்கியது.",
    "Correct. 86th CAA 2002 inserted Article 21A.", "சரி. 86-வது திருத்தம் 2002 பிரிவு 21A-வைச் சேர்த்தது.",
    "Incorrect. 44th CAA 1978 deleted Right to Property.", "தவறு. 44-வது திருத்தம் 1978 சொத்துரிமையை நீக்கியது.",
    "Incorrect. 91st CAA 2003 limited Cabinet size to 15%.", "தவறு. 91-வது திருத்தம் 2003 அமைச்சரவை அளவை 15% எனக் கட்டுப்படுத்தியது.",
    "Incorrect. 103rd CAA 2019 introduced 10% EWS reservation.", "தவறு. 103-வது திருத்தம் 2019 10% EWS இடஒதுக்கீட்டை அறிமுகப்படுத்தியது.",
    "TNPSC Trap: 86th CAA 2002 affected three Parts: Part III (Inserted Art 21A), Part IV (Amended Art 45 for 0-6 yrs), Part IVA (Inserted 11th Duty Art 51A(k)). RTE Act was passed in 2009 & came into force on April 1, 2010.",
    "TNPSC பொறி: 86-வது திருத்தம் 2002 மூன்று பகுதிகளைப் பாதித்தது: பகுதி III (பிரிவு 21A), பகுதி IV (பிரிவு 45), பகுதி IVA (பிரிவு 51A(k)). RTE சட்டம் 2009-ல் நிறைவேற்றப்பட்டு 2010 ஏப்ரல் 1-ல் அமலுக்கு வந்தது.",
    "Article 21A guarantees free and compulsory education for all children between 6 and 14 years.",
    "பிரிவு 21A 6 முதல் 14 வயது வரையிலான அனைத்துக் குழந்தைகளுக்கும் இலவச கட்டாயக் கல்வியை உறுதி செய்கிறது.",
    ["TNPSC Group 2A 2017 PYQ", "M. Laxmikanth - Indian Polity"], "Remember", 45, ["Polity", "Fundamental Rights", "Article 21A", "86th CAA"]
))

# FR_PYQ_006 (Easy | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_006", "Easy", "Direct MCQ",
    "What is the literal English meaning of the Latin legal term 'Habeas Corpus'?",
    "'ஹேபியஸ் கார்பஸ்' என்ற இலத்தீன் சட்டச் சொல்லின் நேரடி ஆங்கிலப் பொருள் என்ன?",
    "We Command", "நாங்கள் கட்டளையிடுகிறோம்",
    "To Have the Body of", "ஆளைக் கொண்டு வாருங்கள் / உடலைப் பெற்றிருத்தல்",
    "By What Authority", "எந்த அதிகாரத்தின் கீழ்",
    "To be Certified", "சான்றளிப்பதாக",
    "B",
    "'Habeas Corpus' literally means 'To have the body of'. It is an order issued by a court to produce a detained person before it to determine the legality of detention.",
    "'ஹேபியஸ் கார்பஸ்' என்பதன் நேரடிப் பொருள் 'ஆளைக் கொண்டு வாருங்கள்' அல்லது 'உடலைப் பெற்றிருத்தல்' ஆகும். இது சட்டவிரோத தடுப்புக் காவலைத் தடுக்க நீதிமன்றத்தால் பிறப்பிக்கப்படும் ஆணையாளையாகும்.",
    "Incorrect. 'We Command' is the literal meaning of Mandamus.", "தவறு. 'நாங்கள் கட்டளையிடுகிறோம்' என்பது மேண்டமஸ் பேராணையின் பொருளாகும்.",
    "Correct. Habeas Corpus literally means 'To have the body of'.", "சரி. ஹேபியஸ் கார்பஸ் என்பதன் நேரடிப் பொருள் 'ஆளைக் கொண்டு வாருங்கள்' என்பதாகும்.",
    "Incorrect. 'By What Authority' is the literal meaning of Quo-Warranto.", "தவறு. 'எந்த அதிகாரத்தின் கீழ்' என்பது குவோ-வாரண்டோ பேராணையின் பொருளாகும்.",
    "Incorrect. 'To be Certified' is the literal meaning of Certiorari.", "தவறு. 'சான்றளிப்பதாக' என்பது செர்ஷியோரரை பேராணையின் பொருளாகும்.",
    "TNPSC Trap: Habeas Corpus can be issued against BOTH public authorities AND private individuals. It is the bulwark of individual liberty against illegal detention.",
    "TNPSC பொறி: ஹேபியஸ் கார்பஸ் அரசு அமைப்புகள் மற்றும் தனியார் நபர்கள் இருவருக்கும் எதிராகப் பிறப்பிக்கப்படலாம். இது சட்டவிரோதக் காவலுக்கு எதிரான தனிநபர் சுதந்திரத்தின் அரணாகும்.",
    "Writ Meanings: Habeas Corpus = To have the body of. Mandamus = We Command. Quo-Warranto = By What Authority. Certiorari = To be certified. Prohibition = To forbid.",
    "பேராணைப் பொருள்கள்: ஹேபியஸ் கார்பஸ் = ஆளைக் கொண்டு வா. மேண்டமஸ் = கட்டளையிடுகிறோம். குவோ-வாரண்டோ = எந்த அதிகாரம். செர்ஷியோரரை = சான்றளித்தல். புரோஹிபிஷன் = தடுத்தல்.",
    ["TNPSC Assistant Conservator 2018 PYQ", "Samacheer Kalvi Political Science"], "Remember", 45, ["Polity", "Fundamental Rights", "Writs", "Habeas Corpus"]
))

# FR_PYQ_007 (Easy | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_007", "Easy", "Direct MCQ",
    "By which Constitutional Amendment Act was the Right to Property deleted from the list of Fundamental Rights in Part III?",
    "எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் பகுதி III-ல் உள்ள அடிப்படை உரிமைகள் பட்டியலிலிருந்து சொத்துரிமை நீக்கப்பட்டது?",
    "24th Constitutional Amendment Act, 1971", "24-வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "86th Constitutional Amendment Act, 2002", "86-வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
    "C",
    "The 44th Constitutional Amendment Act, 1978 enacted under the Morarji Desai Government repealed Article 19(1)(f) and Article 31 from Part III, and re-inserted property right as a legal right under Article 300A in Part XII.",
    "மொரார்ஜி தேசாய் தலைமையிலான அரசின் 44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 பகுதி III-லிருந்து பிரிவு 19(1)(f) மற்றும் பிரிவு 31-ஐ நீக்கி, பகுதி XII-ல் பிரிவு 300A-ன் கீழ் சொத்துரிமையைச் சட்ட உரிமையாக்கியது.",
    "Incorrect. 24th CAA 1971 affirmed Parliament power to amend FRs.", "தவறு. 24-வது திருத்தம் 1971 அடிப்படை உரிமைகளைத் திருத்தும் நாடாளுமன்ற அதிகாரத்தை உறுதி செய்தது.",
    "Incorrect. 42nd CAA 1976 added Fundamental Duties and Preamble words.", "தவறு. 42-வது திருத்தம் 1976 அடிப்படை கடமைகளைச் சேர்த்தது.",
    "Correct. 44th CAA 1978 deleted Right to Property from Part III.", "சரி. 44-வது திருத்தம் 1978 சொத்துரிமையை பகுதி III-லிருந்து நீக்கியது.",
    "Incorrect. 86th CAA 2002 added Right to Education.", "தவறு. 86-வது திருத்தம் 2002 கல்வி உரிமையைச் சேர்த்தது.",
    "TNPSC Trap: Right to Property is NO LONGER a Fundamental Right, but remains a Legal, Statutory, and Constitutional Right under Article 300A.",
    "TNPSC பொறி: சொத்துரிமை இனி அடிப்படை உரிமை அல்ல, ஆனால் பிரிவு 300A-ன் கீழ் ஒரு சட்டபூர்வ மற்றும் அரசியலமைப்பு உரிமையாகும்.",
    "Consequence of 44th CAA 1978: Property disputes cannot be taken directly to SC under Article 32, but can be taken to HC under Article 226.",
    "44-வது திருத்தத்தின் விளைவு: சொத்து தகராறுகளுக்கு பிரிவு 32-ன் கீழ் நேரடியாக உச்சநீதிமன்றம் செல்ல முடியாது, ஆனால் பிரிவு 226-ன் கீழ் உயர்நீதிமன்றம் செல்லலாம்.",
    ["TNPSC Group 1 2015 PYQ", "M. Laxmikanth - Indian Polity"], "Remember", 45, ["Polity", "Fundamental Rights", "Right to Property", "44th CAA"]
))

# FR_PYQ_008 (Easy | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_008", "Easy", "Direct MCQ",
    "Fundamental Rights guaranteed under Part III of the Constitution of India are:",
    "இந்திய அரசியலமைப்பின் பகுதி III-ன் கீழ் உறுதி செய்யப்பட்ட அடிப்படை உரிமைகள் என்பவை:",
    "Non-justiciable and non-enforceable by courts", "நீதிமன்றங்களால் விசாரிக்கப்பட முடியாதவை மற்றும் அமல்படுத்த முடியாதவை",
    "Justiciable only in High Courts under Article 226", "பிரிவு 226-ன் கீழ் உயர்நீதிமன்றங்களில் மட்டுமே விசாரிக்கப்படக் கூடியவை",
    "Non-justiciable but enforceable by Parliament", "நீதிமன்றங்களால் விசாரிக்கப்பட முடியாதவை ஆனால் நாடாளுமன்றத்தால் அமல்படுத்தத்தக்கவை",
    "Justiciable and directly enforceable by Courts of Law", "நீதிமன்றங்களால் விசாரிக்கப்படக் கூடியவை மற்றும் நேரடியாக அமல்படுத்தத்தக்கவை",
    "D",
    "Fundamental Rights are 'Justiciable', meaning aggrieved citizens can directly move the Supreme Court (Article 32) or High Courts (Article 226) for their legal enforcement if violated.",
    "அடிப்படை உரிமைகள் 'நீதிமன்ற விசாரணைக்கு உட்பட்டவை' (Justiciable), அதாவது அவை மீறப்பட்டால் பாதிக்கப்பட்ட குடிமக்கள் உச்சநீதிமன்றத்தை (பிரிவு 32) அல்லது உயர்நீதிமன்றங்களை (பிரிவு 226) நேரடியாக அணுகி அமல்படுத்த முடியும்.",
    "Incorrect. DPSPs in Part IV are non-justiciable; FRs in Part III are justiciable.", "தவறு. பகுதி IV-ல் உள்ள அரசு நெறிமுறைகளே நீதிமன்ற விசாரணைக்கு அப்பாற்பட்டவை; பகுதி III உரிமைகள் விசாரணைக்குட்பட்டவை.",
    "Incorrect. FRs are justiciable in both Supreme Court (Art 32) and High Courts (Art 226).", "தவறு. அடிப்படை உரிமைகள் உச்சநீதிமன்றம் (32) மற்றும் உயர்நீதிமன்றங்கள் (226) இரண்டிலும் விசாரிக்கப்படக் கூடியவை.",
    "Incorrect. FRs are enforceable by courts, not non-justiciable.", "தவறு. அடிப்படை உரிமைகள் நீதிமன்றங்களால் அமல்படுத்தத்தக்கவை.",
    "Correct. Fundamental Rights are justiciable and enforceable by courts.", "சரி. அடிப்படை உரிமைகள் நீதிமன்ற விசாரணைக்கு உட்பட்டவை மற்றும் அமல்படுத்தத்தக்கவை.",
    "TNPSC Trap: Part III (Fundamental Rights) = Justiciable. Part IV (Directive Principles) = Non-Justiciable. Part IVA (Fundamental Duties) = Non-Justiciable.",
    "TNPSC பொறி: பகுதி III (அடிப்படை உரிமைகள்) = நீதிமன்ற விசாரணைக்கு உட்பட்டவை. பகுதி IV (அரசு நெறிமுறைகள்) = விசாரணைக்கு அப்பாற்பட்டவை. பகுதி IVA (அடிப்படை கடமைகள்) = விசாரணைக்கு அப்பாற்பட்டவை.",
    "Justiciability allows individuals to seek writ remedies for violation of Part III rights.",
    "நீதிமன்ற விசாரணைத் தன்மை பகுதி III உரிமைகள் மீறப்படும் போது தனிநபர்கள் பேராணை பரிகாரங்களைப் பெற அனுமதிக்கிறது.",
    ["TNPSC Group 2 2015 PYQ", "Samacheer Kalvi Political Science"], "Remember", 45, ["Polity", "Fundamental Rights", "Justiciability", "Part III"]
))

# FR_PYQ_009 (Medium | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_009", "Medium", "Direct MCQ",
    "Which writ is issued by the Supreme Court or High Court to direct a public authority or official to perform a mandatory public duty which they have failed or refused to perform?",
    "ஒரு பொது அதிகாரி செய்யத் தவறிய அல்லது மறுத்த சட்டப்பூர்வ பொதுக் கடமையைச் செய்ய வற்புறுத்தி உச்சநீதிமன்றம் அல்லது உயர்நீதிமன்றத்தால் பிறப்பிக்கப்படும் பேராணை எது?",
    "Mandamus", "மேண்டமஸ் (கட்டளையுறுத்தும் பேராணை)",
    "Quo-Warranto", "குவோ-வாரண்டோ (தகுதி வினவும் பேராணை)",
    "Certiorari", "செர்ஷியோரரை (ஆவணக் கேட்புப் பேராணை)",
    "Prohibition", "புரோஹிபிஷன் (தடைப் பேராணை)",
    "A",
    "The writ of Mandamus literally means 'We Command'. It is a command issued to a public official, public body, lower court, or tribunal directing them to perform a mandatory statutory duty which they have failed or refused to perform.",
    "மேண்டமஸ் பேராணையின் நேரடிப் பொருள் 'நாங்கள் கட்டளையிடுகிறோம்' ஆகும். இது ஒரு பொது அதிகாரி செய்யத் தவறிய சட்டப்பூர்வ கடமையைச் செய்ய உத்தரவிடும் ஆணையாளையாகும்.",
    "Correct. Mandamus directs performance of a public duty.", "சரி. மேண்டமஸ் பொதுக் கடமையைச் செய்ய உத்தரவிடுகிறது.",
    "Incorrect. Quo-Warranto inquires into the legality of claim to a public office.", "தவறு. குவோ-வாரண்டோ பொதுப் பதவி உரிமையின் சட்டப்பூர்வத் தன்மையை விசாரிக்கிறது.",
    "Incorrect. Certiorari quashes an order already passed by a lower tribunal.", "தவறு. செர்ஷியோரரை கீழ்நீதிமன்ற உத்தரவை ரத்து செய்ய உதவுகிறது.",
    "Incorrect. Prohibition prevents a lower court from continuing a case beyond its jurisdiction.", "தவறு. புரோஹிபிஷன் கீழ்நீதிமன்றம் தனது அதிகார வரம்பைத் தாண்டி செயல்படுவதைத் தடுக்கிறது.",
    "TNPSC Trap: Mandamus CANNOT be issued against: 1. Private individuals, 2. Departmental instructions lacking statutory force, 3. Discretionary duties, 4. President or Governors (Article 361).",
    "TNPSC பொறி: மேண்டமஸ் பொருந்தாத நபர்கள்: 1. தனியார் நபர்கள், 2. சட்டப்பூர்வ பலமில்லாத துறைசார் அறிவுறுத்தல்கள், 3. விருப்பக் கடமைகள், 4. குடியரசுத் தலைவர் அல்லது ஆளுநர்கள் (பிரிவு 361).",
    "Mandamus is used to enforce mandatory public duties imposed by law on public authorities.",
    "பொது அதிகாரிகளுக்கு சட்டத்தால் விதிக்கப்பட்ட கட்டாயப் பொதுக் கடமைகளை அமல்படுத்த மேண்டமஸ் பயன்படுகிறது.",
    ["TNPSC EO 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Writs", "Mandamus"]
))

# FR_PYQ_010 (Medium | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_010", "Medium", "Direct MCQ",
    "Which of the following titles/honours is explicitly PERMITTED under Article 18 of the Constitution of India?",
    "இந்திய அரசியலமைப்பின் பிரிவு 18-ன் கீழ் பின்வரும் எந்தப் பட்டங்கள்/விருதுகள் தெளிவாக அனுமதிக்கப்படுகின்றன?",
    "Hereditary titles of nobility like Maharaja, Raja Bahadur, and Rai Sahib", "மகாராஜா, ராஜா பகதூர், ராய் சாஹிப் போன்ற பரம்பரைப் பட்டங்கள்",
    "Military and Academic distinctions like Param Vir Chakra, Bharat Ratna, and Doctorate", "பரம் வீர் சக்ரா, பாரத ரத்னா, மற்றும் முனைவர் போன்ற ராணுவ மற்றும் கல்விச் சிறப்புப் பட்டங்கள்",
    "Foreign titles conferred on Indian citizens without Presidential consent", "குடியரசுத் தலைவர் அனுமதியின்றி இந்தியக் குடிமக்களுக்கு வழங்கப்படும் வெளிநாட்டுப் பட்டங்கள்",
    "Titles conferred by State Legislatures on prominent businessmen", "முன்னணி தொழிலதிபர்களுக்கு மாநில சட்டமன்றங்களால் வழங்கப்படும் பட்டங்கள்",
    "B",
    "Article 18(1) abolishes titles, but explicitly EXEMPTS military and academic distinctions. In Balaji Raghavan v. Union of India (1996), the Supreme Court upheld National Awards (Bharat Ratna, Padma Vibhushan) as decorations, provided they are not used as suffixes or prefixes to names.",
    "பிரிவு 18(1) பட்டங்களை ஒழிக்கிறது, ஆனால் ராணுவ மற்றும் கல்விச் சிறப்புகளுக்கு விலக்கு அளிக்கிறது. பாலாஜி ராகவன் வழக்கின்படி (1996) தேசிய விருதுகள் (பாரத ரத்னா) பெயரின் முன்னொட்டாகவோ பின்னொட்டாகவோ பயன்படுத்தப்படக் கூடாது.",
    "Incorrect. Hereditary nobility titles are strictly abolished by Article 18.", "தவறு. பரம்பரைப் பட்டங்கள் பிரிவு 18-ல் முற்றிலும் ஒழிக்கப்பட்டுள்ளன.",
    "Correct. Military and academic distinctions are explicitly exempted under Article 18.", "சரி. ராணுவ மற்றும் கல்விச் சிறப்புகள் பிரிவு 18-ல் தெளிவாக விலக்களிக்கப்பட்டுள்ளன.",
    "Incorrect. Foreign titles require prior consent of the President under Article 18(2).", "தவறு. வெளிநாட்டுப் பட்டங்களுக்கு பிரிவு 18(2)-ன் கீழ் குடியரசுத் தலைவர் முன்அனுமதி தேவை.",
    "Incorrect. State Legislatures cannot confer nobility titles.", "தவறு. மாநில சட்டமன்றங்கள் பட்டங்களை வழங்க முடியாது.",
    "TNPSC Trap: National Awards (Bharat Ratna, Padma Awards) are NOT 'titles' under Article 18, but constitutional decorations. However, recipients CANNOT use them as prefix/suffix to their names.",
    "TNPSC பொறி: தேசிய விருதுகள் (பாரத ரத்னா, பத்ம விருதுகள்) பிரிவு 18-ன் கீழ் 'பட்டங்கள்' அல்ல. ஆனால் விருதைப்பெற்றவர்கள் அவற்றை பெயரின் முன்/பின் பயன்படுத்தக் கூடாது.",
    "Article 18 = Abolition of Titles (Exempts Military & Academic distinctions).",
    "பிரிவு 18 = பட்டங்கள் ஒழிப்பு (ராணுவ & கல்விச் சிறப்புகளுக்கு விலக்கு).",
    ["TNPSC Group 1 2017 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 18", "Titles"]
))

# FR_PYQ_011 (Medium | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_011", "Medium", "Direct MCQ",
    "Prohibition of traffic in human beings, 'begar' (unpaid forced labour), and other similar forms of forced labour is guaranteed under which Article?",
    "மனித கடத்தல், 'கொத்தடிமை' (ஊதியமில்லா கட்டாய உழைப்பு) மற்றும் பிற வடிவிலான கட்டாய உழைப்புத் தடை எந்தப் பிரிவின் கீழ் உறுதி செய்யப்படுகிறது?",
    "Article 21", "பிரிவு 21",
    "Article 22", "பிரிவு 22",
    "Article 23", "பிரிவு 23",
    "Article 24", "பிரிவு 24",
    "C",
    "Article 23 prohibits trafficking in human beings, begar, and other forced labour. Any contravention of this provision is an offence punishable in accordance with law. Parliament passed the Bonded Labour System (Abolition) Act 1976 under this Article.",
    "பிரிவு 23 மனித கடத்தல், கொத்தடிமை மற்றும் கட்டாய உழைப்பைத் தடுக்கிறது. இவிதியை மீறுவது சட்டப்படி தண்டனைக்குரிய குற்றமாகும். நாடாளுமன்றம் இதன்கீழ் கொத்தடிமை முறை (ஒழிப்பு) சட்டம் 1976-ஐ இயற்றியது.",
    "Incorrect. Article 21 guarantees Right to Life and Liberty.", "தவறு. பிரிவு 21 வாழ்வுரிமை மற்றும் சுதந்திரத்தை உறுதி செய்கிறது.",
    "Incorrect. Article 22 provides protection against arrest and detention.", "தவறு. பிரிவு 22 கைதுக்கு எதிரான பாதுகாப்பை வழங்குகிறது.",
    "Correct. Article 23 prohibits human trafficking and forced labour.", "சரி. பிரிவு 23 மனித கடத்தல் மற்றும் கட்டாய உழைப்பைத் தடுக்கிறது.",
    "Incorrect. Article 24 prohibits child labour in hazardous employment.", "தவறு. பிரிவு 24 ஆபத்தான வேலைகளில் குழந்தை தொழிலாளர் முறையைத் தடுக்கிறது.",
    "TNPSC Trap: Exception to Article 23: State CAN impose compulsory service for public purposes (e.g. military service or social service), provided it does not discriminate on grounds ONLY of religion, race, caste, or class.",
    "TNPSC பொறி: பிரிவு 23-ன் விதிவிலக்கு: பொது நோக்கங்களுக்காக (ராணுவ சேவை போன்றவை) அரசு கட்டாய சேவையை விதிக்கலாம், ஆனால் அதில் மதம், இனம், சாதி அடிப்படையில் பாகுபாடு இருக்கக் கூடாது.",
    "Right against Exploitation consists of two Articles: Article 23 (Forced Labour & Trafficking) and Article 24 (Child Labour).",
    "சுரண்டலுக்கு எதிரான உரிமை இரண்டு பிரிவுகளைக் கொண்டது: பிரிவு 23 (கட்டாய உழைப்பு & கடத்தல்) மற்றும் பிரிவு 24 (குழந்தை தொழிலாளர்).",
    ["TNPSC Group 2 2022 PYQ", "Samacheer Kalvi Political Science"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 23", "Forced Labour"]
))

# FR_PYQ_012 (Medium | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_012", "Medium", "Direct MCQ",
    "Article 24 of the Indian Constitution strictly prohibits the employment of children in any factory, mine, or other hazardous work below what age?",
    "இந்திய அரசியலமைப்பின் பிரிவு 24 எந்த வயதிற்குட்பட்ட குழந்தைகளை தொழிற்சாலை, சுரங்கம் அல்லது பிற ஆபத்தான வேலைகளில் அமர்த்துவதை உறுதியாகத் தடுக்கிறது?",
    "18 years", "18 வயது",
    "16 years", "16 வயது",
    "15 years", "15 வயது",
    "14 years", "14 வயது",
    "D",
    "Article 24 provides that no child below the age of 14 years shall be employed to work in any factory or mine or engaged in any other hazardous employment. Parliament amended the Child Labour (Prohibition and Regulation) Act in 2016 banning employment of children under 14 in all occupations.",
    "பிரிவு 24 14 வயதிற்குட்பட்ட எந்தவொரு குழந்தையையும் தொழிற்சாலை, சுரங்கம் அல்லது பிற ஆபத்தான பணிகளில் அமர்த்துவதைத் தடுக்கிறது. 2016 திருத்தச் சட்டம் 14 வயதிற்குட்பட்ட குழந்தைகளை அனைத்துத் தொழில்களிலும் அமர்த்துவதைத் தடை செய்தது.",
    "Incorrect. 18 years is the age limit for adolescent hazard protection under 2016 Act.", "தவறு. 18 வயது என்பது 2016 சட்டத்தின் கீழ் வளர்இளம் பருவத்தினருக்கான வரம்பாகும்.",
    "Incorrect. 16 years is not the constitutional age limit in Article 24.", "தவறு. 16 வயது என்பது பிரிவு 24-ன் அரசியலமைப்பு வயது வரம்பல்ல.",
    "Incorrect. 15 years is not the Article 24 threshold.", "தவறு. 15 வயது என்பது பிரிவு 24-ன் வரம்பல்ல.",
    "Correct. Article 24 threshold age is 14 years.", "சரி. பிரிவு 24-ன் அரசியலமைப்பு வயது வரம்பு 14 வயது ஆகும்.",
    "TNPSC Trap: Child Labour Amendment Act 2016: Complete ban on employment of children below 14 years in ALL occupations. Ban on employment of adolescents (14-18 years) in HAZARDOUS occupations.",
    "TNPSC பொறி: குழந்தை தொழிலாளர் திருத்தச் சட்டம் 2016: 14 வயதிற்குட்பட்ட குழந்தைகளை அனைத்துத் தொழில்களிலும் அமர்த்த முழுத் தடை. 14-18 வயது வளர்இளம் பருவத்தினரை ஆபத்தான தொழில்களில் அமர்த்தத் தடை.",
    "Article 24 safeguards children from exploitation in hazardous industrial environments.",
    "பிரிவு 24 குழந்தைகளை ஆபத்தான தொழிற்துறை சூழல்களில் சுரண்டப்படுவதிலிருந்து பாதுகாக்கிறது.",
    ["TNPSC Group 4 2022 PYQ", "Samacheer Kalvi 10th Social"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 24", "Child Labour"]
))

# FR_PYQ_013 (Medium | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_013", "Medium", "Direct MCQ",
    "Which writ prevents the illegal usurpation of a public office by a person who is not legally qualified to hold that office?",
    "ஒரு பொதுப் பதவியை வகிக்கச் சட்டப்பூர்வ தகுதியற்ற ஒருவர் அப்பதவியைச் சட்டவிரோதமாகக் கைப்பற்றுவதைத் தடுக்கும் பேராணை எது?",
    "Quo-Warranto", "குவோ-வாரண்டோ (தகுதி வினவும் பேராணை)",
    "Certiorari", "செர்ஷியோரரை (ஆவணக் கேட்புப் பேராணை)",
    "Mandamus", "மேண்டமஸ் (கட்டளையுறுத்தும் பேராணை)",
    "Habeas Corpus", "ஹேபியஸ் கார்பஸ் (ஆட்கொணர்வுப் பேராணை)",
    "A",
    "The writ of Quo-Warranto literally means 'By What Authority or Warrant'. It is issued to inquire into the legality of a person's claim to a public office created by statute or Constitution, preventing illegal occupation.",
    "குவோ-வாரண்டோ என்பதன் பொருள் 'எந்த அதிகாரத்தின் கீழ்' என்பதாகும். இது ஒரு நபர் சட்டப்பூர்வ பொதுப் பதவியைக் கோருவதன் சட்டப்பூர்வத் தன்மையை விசாரித்து, சட்டவிரோத ஆக்கிரமிப்பைத் தடுக்கிறது.",
    "Correct. Quo-Warranto prevents illegal usurpation of public office.", "சரி. குவோ-வாரண்டோ பொதுப் பதவியைச் சட்டவிரோதமாகக் கைப்பற்றுவதைத் தடுக்கிறது.",
    "Incorrect. Certiorari quashes an order passed by a tribunal lacking jurisdiction.", "தவறு. செர்ஷியோரரை அதிகார வரம்பற்ற தீர்ப்பாய உத்தரவை ரத்து செய்கிறது.",
    "Incorrect. Mandamus directs performance of a mandatory duty.", "தவறு. மேண்டமஸ் கட்டாயக் கடமையைச் செய்ய உத்தரவிடுகிறது.",
    "Incorrect. Habeas Corpus releases persons illegally detained.", "தவறு. ஹேபியஸ் கார்பஸ் சட்டவிரோதமாகக் காவலில் வைக்கப்பட்டவரை விடுவிக்கிறது.",
    "TNPSC Trap: Unlike other four writs, Quo-Warranto can be sought by ANY interested person, even if he is not the personally aggrieved party.",
    "TNPSC பொறி: பிற நான்கு பேராணைகளைப் போலன்றி, குவோ-வாரண்டோ பேராணையை நேரடியாகப் பாதிக்கப்படாத எந்தவொரு ஆர்வமுள்ள நபரும் நீதிமன்றத்தில் கோர முடியும்.",
    "Quo-Warranto applies ONLY to substantive public offices of permanent character created by statute or Constitution.",
    "குவோ-வாரண்டோ சட்டம் அல்லது அரசியலமைப்பால் உருவாக்கப்பட்ட நிரந்தர பொதுப் பதவிகளுக்கு மட்டுமே பொருந்தும்.",
    ["TNPSC Group 1 2021 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Writs", "Quo-Warranto"]
))

# FR_PYQ_014 (Medium | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_014", "Medium", "Direct MCQ",
    "Article 15(1) of the Constitution prohibits discrimination by the State against any citizen on grounds ONLY of which five factors?",
    "அரசியலமைப்பின் பிரிவு 15(1) எந்த ஐந்து காரணங்களின் அடிப்படையில் மட்டுமே குடிமக்களுக்கு எதிராக அரசு பாகுபாடு காட்டுவதைத் தடுக்கிறது?",
    "Religion, Race, Caste, Sex, and Residence", "மதம், இனம், சாதி, பாலினம், மற்றும் இருப்பிடம்",
    "Religion, Race, Caste, Sex, and Place of birth", "மதம், இனம், சாதி, பாலினம், மற்றும் பிறந்த இடம்",
    "Religion, Race, Caste, Sex, Descent, and Residence", "மதம், இனம், சாதி, பாலினம், வம்சாவளி, மற்றும் இருப்பிடம்",
    "Religion, Language, Caste, Sex, and Place of birth", "மதம், மொழி, சாதி, பாலினம், மற்றும் பிறந்த இடம்",
    "B",
    "Article 15(1) states: 'The State shall not discriminate against any citizen on grounds only of religion, race, caste, sex, place of birth or any of them.' Note that Residence and Descent are in Article 16(2), NOT Article 15(1).",
    "பிரிவு 15(1) கூறுவது: 'மதம், இனம், சாதி, பாலினம், பிறந்த இடம் ஆகிய காரணங்களின் அடிப்படையில் மட்டுமே எந்தவொரு குடிமகனுக்கும் எதிராக அரசு பாகுபாடு காட்டக் கூடாது.' இருப்பிடம் மற்றும் வம்சாவளி பிரிவு 16(2)-ல் உள்ளது, 15(1)-ல் இல்லை.",
    "Incorrect. Residence is not a ground under Article 15(1).", "தவறு. இருப்பிடம் என்பது பிரிவு 15(1)-ன் கீழ் உள்ள காரணியல்ல.",
    "Correct. Article 15(1) lists 5 grounds: Religion, Race, Caste, Sex, Place of birth.", "சரி. பிரிவு 15(1) 5 காரணங்களைக் கூறுகிறது: மதம், இனம், சாதி, பாலினம், பிறந்த இடம்.",
    "Incorrect. Descent and Residence belong to Article 16(2).", "தவறு. வம்சாவளி மற்றும் இருப்பிடம் பிரிவு 16(2)-க்கு உரியவை.",
    "Incorrect. Language is not listed in Article 15(1).", "தவறு. மொழி என்பது பிரிவு 15(1)-ல் பட்டியலிடப்படவில்லை.",
    "TNPSC Trap: Article 15(1) has 5 grounds (Religion, Race, Caste, Sex, Place of birth). Article 16(2) has 7 grounds (Adds Descent & Residence).",
    "TNPSC பொறி: பிரிவு 15(1)-ல் 5 காரணங்கள் உள்ளன. பிரிவு 16(2)-ல் 7 காரணங்கள் உள்ளன (வம்சாவளி & இருப்பிடம் சேர்க்கப்பட்டுள்ளன).",
    "The word 'ONLY' in Article 15(1) means discrimination based on other grounds (like residence or language) is not prohibited by Art 15(1).",
    "பிரிவு 15(1)-ல் 'மட்டுமே' என்ற சொல் பிற காரணங்களின் அடிப்படையில் (இருப்பிடம் அல்லது மொழி) பாகுபாடு காட்டுவது 15(1)-ல் தடுக்கப்படவில்லை என்பதைக் குறிக்கிறது.",
    ["TNPSC Group 2 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 15", "Discrimination"]
))

# FR_PYQ_015 (Medium | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_015", "Medium", "Direct MCQ",
    "The fundamental right protection against self-incrimination ('No person accused of any offence shall be compelled to be a witness against himself') is guaranteed under:",
    "தன்னைக் குற்றவாளியாகக் காட்டும் சாட்சியத்தை அளிக்குமாறு வற்புறுத்தப்படக் கூடாது என்ற சுய-குற்றச்சாட்டு எதிர்ப்புப் பாதுகாப்பு எந்தப் பிரிவில் உறுதி செய்யப்பட்டுள்ளது?",
    "Article 20(1)", "பிரிவு 20(1)",
    "Article 20(2)", "பிரிவு 20(2)",
    "Article 20(3)", "பிரிவு 20(3)",
    "Article 21", "பிரிவு 21",
    "C",
    "Article 20(3) guarantees immunity against self-incrimination. It applies ONLY to an accused person facing a criminal charge, protecting against compelled oral or documentary evidence of personal knowledge.",
    "பிரிவு 20(3) சுய-குற்றச்சாட்டு எதிர்ப்பைப் பாதுகாக்கிறது. இது குற்றவியல் குற்றச்சாட்டை எதிர்கொள்ளும் நபர் தனக்கு எதிராக சாட்சியம் அளிக்க வற்புறுத்தப்படுவதைத் தடுக்கிறது.",
    "Incorrect. Article 20(1) protects against Ex-Post Facto Law.", "தவறு. பிரிவு 20(1) பின்னோக்கிய குற்றவியல் சட்டத்திற்கு எதிராகப் பாதுகாக்கிறது.",
    "Incorrect. Article 20(2) protects against Double Jeopardy.", "தவறு. பிரிவு 20(2) இரட்டைத் தண்டனைக்கு எதிராகப் பாதுகாக்கிறது.",
    "Correct. Article 20(3) protects against Self-Incrimination.", "சரி. பிரிவு 20(3) சுய-குற்றச்சாட்டு எதிர்ப்பைப் பாதுகாக்கிறது.",
    "Incorrect. Article 21 guarantees Right to Life and Personal Liberty.", "தவறு. பிரிவு 21 வாழ்வுரிமை மற்றும் தனிநபர் சுதந்திரத்தைப் பாதுகாக்கிறது.",
    "TNPSC Trap: Article 20(3) protection covers compulsory ORAL and DOCUMENTARY testimony disclosing personal knowledge, but DOES NOT cover thumb impression, specimen signature, handwriting, or blood samples (Selvi Case 2010). Narco-analysis and Polygraph without consent violate Art 20(3).",
    "TNPSC பொறி: பிரிவு 20(3) வாய்மொழி & ஆவணச் சாட்சியங்களுக்குப் பொருந்தும், ஆனால் பெருவிரல் ரேகை, கையொப்பம், ரத்த மாதிரிகளுக்குப் பொருந்தாது (செல்வி வழக்கு 2010). சம்மதமில்லாத நார்ோ-பகுப்பாய்வு 20(3)-ஐ மீறுகிறது.",
    "Article 20 contains 3 safeguards: 20(1) Ex-Post Facto, 20(2) Double Jeopardy, 20(3) Self-Incrimination.",
    "பிரிவு 20 3 பாதுகாப்புகளைக் கொண்டது: 20(1) பின்னோக்கிய சட்டம், 20(2) இரட்டைத் தண்டனை, 20(3) சுய-குற்றச்சாட்டு.",
    ["TNPSC ASO 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 20(3)", "Self Incrimination"]
))

# FR_PYQ_016 (Medium | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_016", "Medium", "Direct MCQ",
    "Freedom of conscience and the right freely to profess, practice, and propagate religion under Article 25 is subject to which constitutional limitations?",
    "பிரிவு 25-ன் கீழ் மனசாட்சி சுதந்திரம் மற்றும் மதத்தைப் பின்பற்றவும் பரப்பவும் உள்ள உரிமை எந்த அரசியலமைப்பு வரம்புகளுக்கு உட்பட்டது?",
    "Public order only", "பொது அமைதி மட்டுமே",
    "Morality and health only", "ஒழுக்கம் மற்றும் சுகாதாரம் மட்டுமே",
    "Sovereignty and integrity of India only", "இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு மட்டுமே",
    "Public order, morality, health, and other provisions of Part III", "பொது அமைதி, ஒழுக்கம், சுகாதாரம், மற்றும் பகுதி III-ன் பிற விதிகள்",
    "D",
    "Article 25(1) states: 'Subject to public order, morality and health and to the other provisions of this Part, all persons are equally entitled to freedom of conscience and the right freely to profess, practise and propagate religion.'",
    "பிரிவு 25(1) கூறுவது: 'பொது அமைதி, ஒழுக்கம் மற்றும் சுகாதாரம் மற்றும் இந்த பகுதியின் பிற விதிகளுக்கு உட்பட்டு, அனைவரும் மனசாட்சி சுதந்திரத்திற்கும் மதத்தைப் பின்பற்றவும் பரப்பவும் சம உரிமை உடையவர்கள்.'",
    "Incorrect. Public order is only one of the constitutional limitations.", "தவறு. பொது அமைதி என்பது வரம்புகளில் ஒன்று மட்டுமே.",
    "Incorrect. Morality and health are not the sole limitations.", "தவறு. ஒழுக்கம் மற்றும் சுகாதாரம் மட்டுமே வரம்புகள் அல்ல.",
    "Incorrect. Sovereignty and integrity is a restriction under Art 19, not specified in Art 25(1).", "தவறு. இறையாண்மை மற்றும் ஒருமைப்பாடு என்பது பிரிவு 19-ன் கீழ் உள்ள கட்டுப்பாடாகும்.",
    "Correct. Article 25 is subject to Public Order, Morality, Health, and other Part III provisions.", "சரி. பிரிவு 25 பொது அமைதி, ஒழுக்கம், சுகாதாரம் மற்றும் பகுதி III-ன் பிற விதிகளுக்கு உட்பட்டது.",
    "TNPSC Trap: Article 25 includes right to PROPAGATE religion (exposition of tenets), but DOES NOT include right to FORCIBLY CONVERT another person (Rev Stainislaus Case 1977).",
    "TNPSC பொறி: பிரிவு 25 மதத்தைப் பரப்பும் உரிமையை உள்ளடக்கியது, ஆனால் ஒருவரைப் பலவந்தமாக மதமாற்றம் செய்யும் உரிமையை உள்ளடக்காது (ஸ்டேனிஸ்லாஸ் வழக்கு 1977).",
    "Article 25 protects both religious beliefs (doctrines) and religious practices (rituals).",
    "பிரிவு 25 மத நம்பிக்கைகள் (கோட்பாடுகள்) மற்றும் மதச் சடங்குகள் இரண்டையும் பாதுகாக்கிறது.",
    ["TNPSC Group 1 2014 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 25", "Freedom of Religion"]
))

# FR_PYQ_017 (Medium | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_017", "Medium", "Direct MCQ",
    "Which Article of the Constitution guarantees that any section of citizens residing in India having a distinct language, script, or culture of its own has the right to conserve the same?",
    "இந்தியாவில் வசிக்கும் குடிமக்களின் எந்தவொரு பிரிவினரும் தங்களின் தனித்துவமான மொழி, எழுத்து அல்லது கலாச்சாரத்தைப் பாதுகாக்க உரிமை கொண்டுள்ளனர் என எந்தப் பிரிவு உறுதி செய்கிறது?",
    "Article 29(1)", "பிரிவு 29(1)",
    "Article 30(1)", "பிரிவு 30(1)",
    "Article 26", "பிரிவு 26",
    "Article 28", "பிரிவு 28",
    "A",
    "Article 29(1) guarantees protection of language, script, and culture to 'any section of citizens' (minority or majority). Article 29(2) forbids denial of admission into state-aided educational institutions on grounds only of religion, race, caste, or language.",
    "பிரிவு 29(1) 'குடிமக்களின் எந்தவொரு பிரிவினருக்கும்' (சிறுபான்மையினர் அல்லது பெரும்பான்மையினர்) தங்களது மொழி, எழுத்து மற்றும் கலாச்சாரத்தைப் பாதுகாக்கும் உரிமையை உறுதி செய்கிறது.",
    "Correct. Article 29(1) protects language, script, and culture of any section of citizens.", "சரி. பிரிவு 29(1) குடிமக்கள் பிரிவினரின் மொழி, எழுத்து மற்றும் கலாச்சாரத்தைப் பாதுகாக்கிறது.",
    "Incorrect. Article 30(1) confers right on minorities to establish educational institutions.", "தவறு. பிரிவு 30(1) சிறுபான்மையினருக்குக் கல்வி நிறுவனங்கள் அமைக்கும் உரிமையை வழங்குகிறது.",
    "Incorrect. Article 26 guarantees denominational religious rights.", "தவறு. பிரிவு 26 மதப் பிரிவுகளின் உரிமைகளை உறுதி செய்கிறது.",
    "Incorrect. Article 28 deals with religious instruction in educational institutions.", "தவறு. பிரிவு 28 கல்வி நிறுவனங்களில் மத போதனை பற்றிப் பேசுகிறது.",
    "TNPSC Trap: Article 29(1) applies to 'ANY section of citizens' (Minorities + Majorities). Article 30(1) applies EXCLUSIVELY to 'Religious and Linguistic Minorities'.",
    "TNPSC பொறி: பிரிவு 29(1) 'குடிமக்களின் எந்தவொரு பிரிவினருக்கும்' பொருந்தும். பிரிவு 30(1) 'மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே' பொருந்தும்.",
    "Cultural and Educational Rights are contained in Articles 29 and 30.",
    "கலாச்சார மற்றும் கல்வி உரிமைகள் பிரிவுகள் 29 மற்றும் 30-ல் அடங்கியுள்ளன.",
    ["TNPSC Group 2 2013 PYQ", "Samacheer Kalvi Political Science"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 29", "Minority Rights"]
))

# FR_PYQ_018 (Medium | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_018", "Medium", "Direct MCQ",
    "Under Article 30(1) of the Constitution of India, the fundamental right to establish and administer educational institutions of their choice is conferred upon:",
    "இந்திய அரசியலமைப்பின் பிரிவு 30(1)-ன் கீழ் தங்களுக்கு விருப்பமான கல்வி நிறுவனங்களை நிறுவி நிர்வகிக்கும் அடிப்படை உரிமை யாருக்கு வழங்கப்பட்டுள்ளது?",
    "All citizens of India irrespective of religion or language", "மதம் அல்லது மொழி வேறுபாடின்றி இந்தியாவின் அனைத்துக் குடிமக்களுக்கும்",
    "Religious and Linguistic minorities ONLY", "மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே",
    "Linguistic minorities ONLY", "மொழி சிறுபான்மையினருக்கு மட்டுமே",
    "Socially and Educationally Backward Classes (SEBCs)", "சமூக ரீதியாகவும் கல்வி ரீதியாகவும் பின்தங்கிய வகுப்பினருக்கு",
    "B",
    "Article 30(1) states: 'All minorities, whether based on religion or language, shall have the right to establish and administer educational institutions of their choice.' Note that Article 30 recognizes ONLY Religious and Linguistic minorities (not ethnic or racial minorities).",
    "பிரிவு 30(1) கூறுவது: 'மதம் அல்லது மொழியை அடிப்படையாகக் கொண்ட அனைத்து சிறுபான்மையினரும் தங்களுக்கு விருப்பமான கல்வி நிறுவனங்களை நிறுவி நிர்வகிக்க உரிமை உண்டு.' பிரிவு 30 மத மற்றும் மொழி சிறுபான்மையினரை மட்டுமே அங்கீகரிக்கிறது.",
    "Incorrect. Article 30(1) is restricted to minorities, not all citizens.", "தவறு. பிரிவு 30(1) சிறுபான்மையினருக்கு மட்டுமேயானது, அனைத்துக் குடிமக்களுக்கும் அல்ல.",
    "Correct. Article 30(1) right is conferred exclusively on Religious and Linguistic minorities.", "சரி. பிரிவு 30(1) உரிமை மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே வழங்கப்பட்டுள்ளது.",
    "Incorrect. Article 30(1) covers both religious AND linguistic minorities.", "தவறு. பிரிவு 30(1) மத மற்றும் மொழி சிறுபான்மையினர் இருவரையும் உள்ளடக்கியது.",
    "Incorrect. Article 30(1) does not deal with backward class reservation.", "தவறு. பிரிவு 30(1) பின்தங்கிய வகுப்பு இடஒதுக்கீடு பற்றியது அல்ல.",
    "TNPSC Trap: The term 'Minority' is NOT defined anywhere in the Constitution of India. In TMA Pai Foundation Case (2002), SC held that unit for determining minority status is the STATE, not the whole country.",
    "TNPSC பொறி: 'சிறுபான்மையினர்' என்ற சொல் இந்திய அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை. டி.எம்.ஏ. பை வழக்கில் (2002) சிறுபான்மையினர் அந்தஸ்தைத் தீர்மானிக்கும் அலகு மாநிலமே தவிர நாடு முழுவதுமல்ல எனத் தீர்ப்பளிக்கப்பட்டது.",
    "Article 30 confers three rights on minorities: 1. Establish institutions, 2. Administer institutions, 3. Non-discrimination in state aid.",
    "பிரிவு 30 சிறுபான்மையினருக்கு 3 உரிமைகளை வழங்குகிறது: 1. நிறுவனங்களை நிறுவுதல், 2. நிர்வகித்தல், 3. அரசு நிதியுதவியில் பாகுபாடின்மை.",
    ["TNPSC Group 1 2022 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 30", "Minority Institutions"]
))

# FR_PYQ_019 (Medium | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_019", "Medium", "Direct MCQ",
    "Where is the Right to Property located in the Constitution of India at present following its deletion from Part III?",
    "பகுதி III-லிருந்து நீக்கப்பட்ட பின் தற்போதைய இந்திய அரசியலமைப்பில் சொத்துரிமை எங்கு அமைந்துள்ளது?",
    "Article 31 in Part III", "பகுதி III-ல் உள்ள பிரிவு 31",
    "Article 19(1)(f) in Part III", "பகுதி III-ல் உள்ள பிரிவு 19(1)(f)",
    "Article 300A in Part XII", "பகுதி XII-ல் உள்ள பிரிவு 300A",
    "Article 368 in Part XX", "பகுதி XX-ல் உள்ள பிரிவு 368",
    "C",
    "The 44th Constitutional Amendment Act, 1978 removed Right to Property from Part III and placed it as a Constitutional / Legal Right under Article 300A in Part XII (Finance, Property, Contracts and Suits).",
    "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 சொத்துரிமையை பகுதி III-லிருந்து நீக்கி, பகுதி XII-ல் (நிதி, சொத்து, ஒப்பந்தங்கள்) பிரிவு 300A-ன் கீழ் அரசியலமைப்பு / சட்ட உரிமையாக வைத்தது.",
    "Incorrect. Article 31 was repealed from Part III by 44th CAA 1978.", "தவறு. பிரிவு 31 44-வது திருத்தத்தால் பகுதி III-லிருந்து நீக்கப்பட்டது.",
    "Incorrect. Article 19(1)(f) was repealed by 44th CAA 1978.", "தவறு. பிரிவு 19(1)(f) 44-வது திருத்தத்தால் நீக்கப்பட்டது.",
    "Correct. Article 300A in Part XII is the current location of Right to Property.", "சரி. பகுதி XII-ல் உள்ள பிரிவு 300A சொத்துரிமையின் தற்போதைய இடமாகும்.",
    "Incorrect. Article 368 deals with Constitutional Amendment procedure.", "தவறு. பிரிவு 368 அரசியலமைப்பு திருத்த நடைமுறையைப் பற்றியது.",
    "TNPSC Trap: Executive action depriving property without authority of law violates Article 300A. But Parliament or State Legislature CAN pass a valid law to acquire private property for public purpose.",
    "TNPSC பொறி: சட்ட அதிகாரமின்றி சொத்தைப் பறிக்கும் நிர்வாக நடவடிக்கை பிரிவு 300A-ஐ மீறுகிறது. ஆனால் நாடாளுமன்றம் பொது நோக்கத்திற்காகச் சொத்தைக் கையகப்படுத்தச் சட்டம் இயற்றலாம்.",
    "Article 300A states: 'No person shall be deprived of his property save by authority of law.'",
    "பிரிவு 300A கூறுவது: 'சட்டத்தின் அதிகாரத்தினால் அன்றி எவரும் தமது சொத்திலிருந்து வஞ்சிக்கப்படக் கூடாது.'",
    ["TNPSC Group 2A 2016 PYQ", "Samacheer Kalvi Political Science"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 300A", "Right to Property"]
))

# FR_PYQ_020 (Medium | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_020", "Medium", "Direct MCQ",
    "Which judicial writ is issued by a Superior Court to quash an illegal order already passed by an inferior court or quasi-judicial tribunal in excess of jurisdiction?",
    "அதிகார வரம்பை மீறி கீழ்நீதிமன்றம் அல்லது பகுதி-நீதிமன்றத் தீர்ப்பாயத்தால் ஏற்கனவே பிறப்பிக்கப்பட்ட சட்டவிரோத உத்தரவை ரத்து செய்ய மேல்நீதிமன்றத்தால் பிறப்பிக்கப்படும் பேராணை எது?",
    "Prohibition", "புரோஹிபிஷன் (தடைப் பேராணை)",
    "Mandamus", "மேண்டமஸ் (கட்டளையுறுத்தும் பேராணை)",
    "Quo-Warranto", "குவோ-வாரண்டோ (தகுதி வினவும் பேராணை)",
    "Certiorari", "செர்ஷியோரரை (ஆவணக் கேட்புப் பேராணை)",
    "D",
    "Certiorari literally means 'To be Certified'. It is issued by a higher court to a lower court or tribunal to transfer a case to itself or to QUASH an illegal order already passed in excess of jurisdiction or violating natural justice.",
    "செர்ஷியோரரை என்பதன் பொருள் 'சான்றளிப்பதாக' என்பதாகும். இது அதிகார வரம்பை மீறி அல்லது இயற்கை நீதியை மீறி பிறப்பிக்கப்பட்ட உத்தரவை ரத்து செய்ய மேல்நீதிமன்றத்தால் பிறப்பிக்கப்படும் ஆணையாளையாகும்.",
    "Incorrect. Prohibition prevents an ongoing proceeding (issued before order).", "தவறு. புரோஹிபிஷன் நடப்பில் உள்ள வழக்கைத் தடுக்கிறது (உத்தரவுக்கு முன் பிறப்பிக்கப்படுவது).",
    "Incorrect. Mandamus directs performance of a public duty.", "தவறு. மேண்டமஸ் பொதுக் கடமையைச் செய்ய உத்தரவிடுகிறது.",
    "Incorrect. Quo-Warranto inquires into public office title.", "தவறு. குவோ-வாரண்டோ பொதுப் பதவி உரிமையை விசாரிக்கிறது.",
    "Correct. Certiorari quashes an order already passed in excess of jurisdiction.", "சரி. செர்ஷியோரரை அதிகார வரம்பை மீறி பிறப்பிக்கப்பட்ட உத்தரவை ரத்து செய்கிறது.",
    "TNPSC Trap: Difference between Prohibition & Certiorari: Prohibition is ONLY PREVENTIVE (issued when proceedings are pending). Certiorari is BOTH PREVENTIVE AND CURATIVE (issued after order has been passed).",
    "TNPSC பொறி: புரோஹிபிஷன் vs செர்ஷியோரரை: புரோஹிபிஷன் தடுப்பு மட்டுமே (வழக்கு நிலுவையில் இருக்கும் போது). செர்ஷியோரரை தடுப்பு மற்றும் ரத்து செய்யும் குணப்படுத்தும் தன்மையுடையது (உத்தரவு பிறப்பிக்கப்பட்ட பின்).",
    "In 1991, Supreme Court ruled that Certiorari can be issued even against administrative authorities affecting rights of individuals.",
    "1991-ல் உச்சநீதிமன்றம் தனிநபர் உரிமைகளைப் பாதிக்கும் நிர்வாக அதிகாரிகளுக்கு எதிராகவும் செர்ஷியோரரை பிறப்பிக்கப்படலாம் எனத் தீர்ப்பளித்தது.",
    ["TNPSC Group 1 2020 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Writs", "Certiorari"]
))

# FR_PYQ_021 (Hard | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_021", "Hard", "Direct MCQ",
    "Which group of Fundamental Rights under Part III is conferred EXCLUSIVELY on Citizens of India and is NOT available to foreign nationals?",
    "பகுதி III-ன் கீழ் உள்ள எந்த அடிப்படை உரிமைகள் குழு இந்தியக் குடிமக்களுக்கு மட்டுமே உரித்தானவை, வெளிநாட்டினருக்குக் கிடைக்காதவை?",
    "Articles 15, 16, 19, 29, and 30", "பிரிவுகள் 15, 16, 19, 29, மற்றும் 30",
    "Articles 14, 19, 21, 22, and 32", "பிரிவுகள் 14, 19, 21, 22, மற்றும் 32",
    "Articles 14, 15, 16, 20, and 21", "பிரிவுகள் 14, 15, 16, 20, மற்றும் 21",
    "Articles 19, 20, 21, 21A, and 22", "பிரிவுகள் 19, 20, 21, 21A, மற்றும் 22",
    "A",
    "Fundamental Rights available ONLY to Citizens: Articles 15 (Prohibition of Discrimination), 16 (Equality in Public Employment), 19 (Six Freedoms), 29 (Protection of Culture), and 30 (Minority Institutions). All other FRs (14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28) apply to ALL persons (citizens + foreigners).",
    "குடிமக்களுக்கு மட்டுமே உரித்தான உரிமைகள்: பிரிவுகள் 15 (பாகுபாடு தடை), 16 (பொது வேலைவாய்ப்பு), 19 (ஆறு சுதந்திரங்கள்), 29 (கலாச்சார பாதுகாப்பு), மற்றும் 30 (சிறுபான்மை நிறுவனங்கள்). பிற உரிமைகள் (14, 20, 21 போன்றவை) அனைவருக்கும் பொருந்தும்.",
    "Correct. Articles 15, 16, 19, 29, 30 are available ONLY to citizens.", "சரி. பிரிவுகள் 15, 16, 19, 29, 30 குடிமக்களுக்கு மட்டுமே உரித்தானவை.",
    "Incorrect. Article 14 and Article 21 apply to foreigners as well.", "தவறு. பிரிவுகள் 14 மற்றும் 21 வெளிநாட்டினருக்கும் பொருந்தும்.",
    "Incorrect. Article 14 and Article 20 apply to all persons.", "தவறு. பிரிவுகள் 14 மற்றும் 20 அனைவருக்கும் பொருந்தும்.",
    "Incorrect. Articles 20, 21, 21A, 22 apply to all persons.", "தவறு. பிரிவுகள் 20, 21, 21A, 22 அனைவருக்கும் பொருந்தும்.",
    "TNPSC Trap: Remember the shortcut code: '15, 16, 19, 29, 30' = CITIZENS ONLY. Enemy Aliens get no protection under Article 22(3).",
    "TNPSC பொறி: நினைவில் வைக்க குறுக்குவழிக் குறியீடு: '15, 16, 19, 29, 30' = குடிமக்கள் மட்டுமே. எதிரி நாட்டின் குடிமக்களுக்கு பிரிவு 22(3) பாதுகாப்பு கிடையாது.",
    "Foreigners enjoy rights under Articles 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28 while residing in India.",
    "வெளிநாட்டினர் இந்தியாவில் வசிக்கும் போது பிரிவுகள் 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28 ஆகிய உரிமைகளை அனுபவிக்கின்றனர்.",
    ["TNPSC Group 1 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Citizenship", "Foreigners"]
))

# FR_PYQ_022 (Hard | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_022", "Hard", "Direct MCQ",
    "Which Article of the Constitution explicitly empowers the State to make provision for reservation of appointments or posts in favour of any backward class of citizens not adequately represented in State services?",
    "அரசுப் பணிகளில் போதிய பிரதிநிதித்துவம் பெறாத எந்தவொரு பின்தங்கிய வகுப்பு குடிமக்களுக்கும் நியமனங்கள் அல்லது பணியிடங்களில் இடஒதுக்கீடு செய்ய அரசுக்கு எந்தப் பிரிவு தெளிவாக அதிகாரம் அளிக்கிறது?",
    "Article 15(4)", "பிரிவு 15(4)",
    "Article 16(4)", "பிரிவு 16(4)",
    "Article 16(2)", "பிரிவு 16(2)",
    "Article 17", "பிரிவு 17",
    "B",
    "Article 16(4) empowers the State to make provision for reservation of appointments or posts in favour of any backward class of citizens which, in the opinion of the State, is not adequately represented in the services under the State.",
    "பிரிவு 16(4) அரசின் கீழ் உள்ள பணிகளில் போதிய பிரதிநிதித்துவம் பெறாத எந்தவொரு பின்தங்கிய வகுப்பு குடிமக்களுக்கும் பணியிடங்களில் இடஒதுக்கீடு செய்ய அரசுக்கு அதிகாரம் அளிக்கிறது.",
    "Incorrect. Article 15(4) enables special provisions in educational institutions and social welfare.", "தவறு. பிரிவு 15(4) கல்வி நிறுவனங்கள் மற்றும் சமூக நலனில் சிறப்பு விதிகளை அளிக்கிறது.",
    "Correct. Article 16(4) is the constitutional foundation for public employment reservation.", "சரி. பிரிவு 16(4) பொது வேலைவாய்ப்பு இடஒதுக்கீட்டின் அரசியலமைப்பு அடிப்படையாகும்.",
    "Incorrect. Article 16(2) prohibits discrimination in employment on 7 grounds.", "தவறு. பிரிவு 16(2) வேலைவாய்ப்பில் 7 காரணங்களின் கீழ் பாகுபாடு காட்டுவதைத் தடுக்கிறது.",
    "Incorrect. Article 17 abolishes untouchability.", "தவறு. பிரிவு 17 தீண்டாமையை ஒழிக்கிறது.",
    "TNPSC Trap: Article 15(4) = Reservation in Educational Institutions / Social schemes. Article 16(4) = Reservation in Public Employment posts.",
    "TNPSC பொறி: பிரிவு 15(4) = கல்வி நிறுவனங்கள் / சமூகத் திட்டங்களில் இடஒதுக்கீடு. பிரிவு 16(4) = பொது வேலைவாய்ப்புப் பணியிடங்களில் இடஒதுக்கீடு.",
    "Article 16(4) requires two conditions: 1. Backward Class of citizens, 2. Not adequately represented in State services.",
    "பிரிவு 16(4) இரண்டு நிபந்தனைகளைக் கோருகிறது: 1. பின்தங்கிய வகுப்பு குடிமக்கள், 2. அரசுப் பணிகளில் போதிய பிரதிநிதித்துவம் பெறாமை.",
    ["TNPSC Group 2 2018 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Article 16(4)", "Reservation"]
))

# FR_PYQ_023 (Hard | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_023", "Hard", "Direct MCQ",
    "The landmark Supreme Court Mandal Case judgment capping total reservation at 50% and introducing the 'Creamy Layer' exclusion rule was delivered in which case?",
    "மொத்த இடஒதுக்கீட்டை 50% ஆக வரம்பிட்டு 'கிரீமி லேயர்' (சலுகைப்படை) விலக்கு விதியை அறிமுகப்படுத்திய வரலாற்றுச் சிறப்புமிக்க உச்சநீதிமன்ற மண்டல் வழக்கு தீர்ப்பு எந்த வழக்கில் வழங்கப்பட்டது?",
    "State of Madras v. Champakam Dorairajan (1951)", "மதராஸ் மாநிலம் எதிராக சண்பகம் துரைராஜன் (1951)",
    "M. Nagaraj v. Union of India (2006)", "எம். நாகராஜ் எதிராக இந்திய யூனியன் (2006)",
    "Indra Sawhney v. Union of India (1992)", "இந்திரா சகானி எதிராக இந்திய யூனியன் (1992)",
    "Janhit Abhiyan v. Union of India (2022)", "ஜன்ஹித் அபியான் எதிராக இந்திய யூனியன் (2022)",
    "C",
    "In Indra Sawhney v. Union of India (1992) (Mandal Case), a 9-judge bench upheld 27% OBC reservation under Article 16(4), but laid down key rules: 1. Exclusion of Creamy Layer, 2. 50% ceiling cap on total reservation, 3. No reservation in promotions (later amended by 77th CAA).",
    "இந்திரா சகானி வழக்கின் (1992 - மண்டல் வழக்கு) 9 நீதிபதிகள் அமர்வு பிரிவு 16(4)-ன் கீழ் 27% OBC இடஒதுக்கீட்டை உறுதி செய்தது, மேலும் 50% உச்சவரம்பு மற்றும் கிரீமி லேயர் விலக்கு விதியை வகுத்தது.",
    "Incorrect. Champakam Dorairajan (1951) led to 1st CAA adding Art 15(4).", "தவறு. சண்பகம் துரைராஜன் வழக்கு (1951) பிரிவு 15(4)-ஐச் சேர்த்த 1-வது திருத்தத்திற்கு வழிவகுத்தது.",
    "Incorrect. M. Nagaraj (2006) laid down catch-up rule and quantifiable data for SC/ST promotion reservation.", "தவறு. எம். நாகராஜ் வழக்கு (2006) SC/ST பதவி உயர்வு இடஒதுக்கீட்டிற்கான அளவிடக்கூடிய தகவல்களைக் கோரியது.",
    "Correct. Indra Sawhney (1992) capped reservation at 50% and introduced Creamy Layer.", "சரி. இந்திரா சகானி வழக்கு (1992) இடஒதுக்கீட்டை 50% ஆக வரம்பிட்டு கிரீமி லேயரை அறிமுகப்படுத்தியது.",
    "Incorrect. Janhit Abhiyan (2022) upheld 103rd CAA 10% EWS reservation.", "தவறு. ஜன்ஹித் அபியான் வழக்கு (2022) 103-வது திருத்தமான 10% EWS இடஒதுக்கீட்டை உறுதி செய்தது.",
    "TNPSC Trap: Indra Sawhney 1992 ruled against reservation in promotions. 77th CAA 1995 inserted Article 16(4A) permitting promotion reservation for SC/STs.",
    "TNPSC பொறி: இந்திரா சகானி வழக்கு பதவி உயர்வு இடஒதுக்கீட்டிற்கு எதிராகத் தீர்ப்பளித்தது. 77-வது திருத்தம் 1995 பிரிவு 16(4A)-ஐச் சேர்த்து SC/ST-க்கு பதவி உயர்வு இடஒதுக்கீட்டை அனுமதித்தது.",
    "Indra Sawhney (1992) 9-Judge Bench: 50% cap on reservation + Creamy Layer exclusion + Permanent statutory body for OBC list.",
    "இந்திரா சகானி (1992) 9-நீதிபதிகள் அமர்வு: 50% இடஒதுக்கீடு வரம்பு + கிரீமி லேயர் விலக்கு + OBC பட்டியலுக்கான நிரந்தர சட்டப்பூர்வ வாரியம்.",
    ["TNPSC Group 1 2021 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Indra Sawhney Case", "Mandal Case"]
))

# FR_PYQ_024 (Hard | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_024", "Hard", "Direct MCQ",
    "In which landmark case did the Supreme Court propound the 'Basic Structure Doctrine', holding that Parliament cannot amend the fundamental features of the Constitution under Article 368?",
    "நாடாளுமன்றம் பிரிவு 368-ன் கீழ் அரசியலமைப்பின் அடிப்படை அம்சங்களைத் திருத்த முடியாது எனக்கூறி, உச்சநீதிமன்றம் 'அடிப்படை அமைப்புக் கோட்பாட்டை' எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில் உருவாக்கியது?",
    "Shankari Prasad v. Union of India (1951)", "சங்கரி பிரசாத் எதிராக இந்திய யூனியன் (1951)",
    "Sajjan Singh v. State of Rajasthan (1965)", "சஜ்ஜன் சிங் எதிராக ராஜஸ்தான் மாநிலம் (1965)",
    "I.C. Golaknath v. State of Punjab (1967)", "ஐ.சி. கோலக்நாத் எதிராக பஞ்சாப் மாநிலம் (1967)",
    "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிராக கேரளா மாநிலம் (1973)",
    "D",
    "In Kesavananda Bharati v. State of Kerala (April 24, 1973), a 13-judge Bench (largest ever in SC history) by a 7:6 majority propounded the 'Basic Structure Doctrine'. It overruled Golaknath, holding that Parliament can amend any part of the Constitution including Part III, but CANNOT alter or destroy its Basic Structure.",
    "கேசவாநந்த பாரதி வழக்கின் (ஏப்ரல் 24, 1973) 13 நீதிபதிகள் அமர்வு (7:6 பெரும்பான்மை) 'அடிப்படை அமைப்புக் கோட்பாட்டை' உருவாக்கியது. நாடாளுமன்றம் பகுதி III உட்பட எதையும் திருத்தலாம், ஆனால் அடிப்படை அமைப்பை மாற்ற முடியாது எனத் தீர்ப்பளித்தது.",
    "Incorrect. Shankari Prasad (1951) held Parliament can amend Fundamental Rights.", "தவறு. சங்கரி பிரசாத் (1951) நாடாளுமன்றம் அடிப்படை உரிமைகளைத் திருத்தலாம் எனக் கூறியது.",
    "Incorrect. Sajjan Singh (1965) upheld Shankari Prasad ruling.", "தவறு. சஜ்ஜன் சிங் (1965) சங்கரி பிரசாத் தீர்ப்பை உறுதி செய்தது.",
    "Incorrect. Golaknath (1967) held Fundamental Rights are transcendental and unamendable.", "தவறு. கோலக்நாத் (1967) அடிப்படை உரிமைகள் திருத்த முடியாதவை எனக் கூறியது.",
    "Correct. Kesavananda Bharati (1973) propounded the Basic Structure Doctrine.", "சரி. கேசவாநந்த பாரதி (1973) அடிப்படை அமைப்புக் கோட்பாட்டை உருவாக்கியது.",
    "TNPSC Trap: Shankari Prasad (1951) = FRs Amendable. Golaknath (1967) = FRs Unamendable. Kesavananda Bharati (1973) = FRs Amendable, BUT Basic Structure Unamendable.",
    "TNPSC பொறி: சங்கரி பிரசாத் (1951) = திருத்தலாம். கோலக்நாத் (1967) = திருத்த முடியாது. கேசவாநந்த பாரதி (1973) = திருத்தலாம், ஆனால் அடிப்படை அமைப்பை திருத்த முடியாது.",
    "Kesavananda Bharati bench of 13 Judges is the largest judicial bench in Indian Supreme Court history.",
    "13 நீதிபதிகள் கொண்ட கேசவாநந்த பாரதி அமர்வு இந்திய உச்சநீதிமன்ற வரலாற்றிலேயே மிகப்பெரிய நீதித்துறை அமர்வாகும்.",
    ["TNPSC Group 1 2022 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Kesavananda Bharati", "Basic Structure"]
))

# FR_PYQ_025 (Easy | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_025", "Easy", "Direct MCQ",
    "How many fundamental freedoms are currently guaranteed under Article 19(1) of the Constitution of India?",
    "இந்திய அரசியலமைப்பின் பிரிவு 19(1)-ன் கீழ் தற்போது எத்தனை அடிப்படை சுதந்திரங்கள் உறுதி செய்யப்பட்டுள்ளன?",
    "6", "6",
    "7", "7",
    "8", "8",
    "5", "5",
    "A",
    "Article 19(1) originally guaranteed 7 freedoms. Following the deletion of Right to Property under Article 19(1)(f) by the 44th Constitutional Amendment Act 1978, currently 6 freedoms remain: 1. Speech & Expression, 2. Assembly, 3. Association, 4. Movement, 5. Residence, 6. Profession.",
    "பிரிவு 19(1) தொடக்கத்தில் 7 சுதந்திரங்களை உறுதி செய்தது. 44-வது திருத்தம் 1978 மூலம் பிரிவு 19(1)(f) சொத்துரிமை நீக்கப்பட்ட பின் தற்போது 6 சுதந்திரங்கள் உள்ளன.",
    "Correct. Currently 6 freedoms are guaranteed under Article 19.", "சரி. தற்போது பிரிவு 19-ன் கீழ் 6 சுதந்திரங்கள் உள்ளன.",
    "Incorrect. 7 was the original count before 44th CAA 1978.", "தவறு. 7 என்பது 44-வது திருத்தம் 1978-க்கு முந்தைய எண்ணிக்கையாகும்.",
    "Incorrect. 8 is not the count.", "தவறு. 8 என்பது எண்ணிக்கையல்ல.",
    "Incorrect. 5 is not the count.", "தவறு. 5 என்பது எண்ணிக்கையல்ல.",
    "TNPSC Trap: Deleted freedom under Art 19: Article 19(1)(f) - Right to acquire, hold and dispose of property (Deleted by 44th CAA 1978).",
    "TNPSC பொறி: பிரிவு 19-ல் நீக்கப்பட்ட சுதந்திரம்: பிரிவு 19(1)(f) - சொத்து சம்பாதிக்க, வைத்திருக்க மற்றும் விற்க உரிமை (44-வது திருத்தத்தால் நீக்கப்பட்டது).",
    "Article 19 freedoms are available ONLY to Citizens of India (not to foreigners or legal corporations).",
    "பிரிவு 19 சுதந்திரங்கள் இந்தியக் குடிமக்களுக்கு மட்டுமே உரித்தானவை (வெளிநாட்டினருக்கோ நிறுவனங்களுக்கோ அல்ல).",
    ["TNPSC Group 4 2018 PYQ", "Samacheer Kalvi 10th Social"], "Remember", 45, ["Polity", "Fundamental Rights", "Article 19", "Six Freedoms"]
))

# FR_PYQ_026 (Easy | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_026", "Easy", "Direct MCQ",
    "The constitutional safeguard 'No person shall be prosecuted and punished for the same offence more than once' under Article 20(2) is known as:",
    "பிரிவு 20(2)-ன் கீழ் 'எந்தவொரு நபரும் ஒரே குற்றத்திற்காக ஒன்றுக்கு மேற்பட்ட முறை விசாரிக்கப்பட்டு தண்டிக்கப்படக் கூடாது' என்ற பாதுகாப்பு எவ்வாறு அழைக்கப்படுகிறது?",
    "Ex-Post Facto Law", "பின்னோக்கிய விளைவுச் சட்டம்",
    "Protection against Double Jeopardy", "இரட்டைத் தண்டனைக்கு எதிரான பாதுகாப்பு",
    "Protection against Self-Incrimination", "சுய-குற்றச்சாட்டுக்கு எதிரான பாதுகாப்பு",
    "Rule of Law", "சட்டத்தின் ஆட்சி",
    "B",
    "Article 20(2) provides immunity against 'Double Jeopardy' (Nemo debet bis vexari), meaning no person shall be prosecuted and punished for the same offence more than once in a judicial court.",
    "பிரிவு 20(2) 'இரட்டைத் தண்டனைக்கு' எதிரான பாதுகாப்பை வழங்குகிறது, அதாவது நீதிமன்றத்தின் முன் ஒரே குற்றத்திற்காக ஒரு நபர் ஒரு முறைக்கு மேல் தண்டிக்கப்படக் கூடாது.",
    "Incorrect. Ex-Post Facto Law refers to retrospective criminal legislation under Art 20(1).", "தவறு. பின்னோக்கிய விளைவுச் சட்டம் என்பது பிரிவு 20(1)-ன் கீழ் வரும்.",
    "Correct. Article 20(2) is Protection against Double Jeopardy.", "சரி. பிரிவு 20(2) என்பது இரட்டைத் தண்டனைக்கு எதிரான பாதுகாப்பாகும்.",
    "Incorrect. Self-Incrimination refers to Article 20(3).", "தவறு. சுய-குற்றச்சாட்டு என்பது பிரிவு 20(3)-க்கு உரியது.",
    "Incorrect. Rule of Law is embodied under Article 14.", "தவறு. சட்டத்தின் ஆட்சி பிரிவு 14-ன் கீழ் அடங்கியுள்ளது.",
    "TNPSC Trap: Article 20(2) applies ONLY to proceedings before a Judicial Court or Tribunal. Departmental disciplinary action or administrative fines do NOT constitute prosecution for Double Jeopardy.",
    "TNPSC பொறி: பிரிவு 20(2) நீதித்துறை நீதிமன்றங்கள் அல்லது தீர்ப்பாயங்களுக்கு மட்டுமே பொருந்தும். துறைசார் ஒழுங்கு நடவடிக்கையோ நிர்வாக அபராதமோ இரட்டைத் தண்டனைத் தடையை ஏற்படுத்தாது.",
    "Double Jeopardy protection requires BOTH prior prosecution AND punishment before a Court.",
    "இரட்டைத் தண்டனைப் பாதுகாப்பு பெற நீதிமன்றத்தின் முன் முந்தைய விசாரணை மற்றும் தண்டனை இரண்டும் இருக்க வேண்டும்.",
    ["TNPSC Group 2 2015 PYQ", "M. Laxmikanth - Indian Polity"], "Remember", 45, ["Polity", "Fundamental Rights", "Article 20(2)", "Double Jeopardy"]
))

# FR_PYQ_027 (Medium | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_027", "Medium", "Direct MCQ",
    "Under Article 22(4) of the Constitution, what is the maximum period a person can be detained under a preventive detention law without obtaining the opinion of an Advisory Board?",
    "பிரிவு 22(4)-ன் கீழ், ஆலோசனைக் குழுவின் கருத்தைப் பெறாமல் தடுப்புக் காவல் சட்டத்தின் கீழ் ஒருவரை அதிகபட்சமாக எவ்வளவு காலம் காவலில் வைக்க முடியும்?",
    "1 Month", "1 மாதம்",
    "2 Months", "2 மாதங்கள்",
    "3 Months", "3 மாதங்கள்",
    "6 Months", "6 மாதங்கள்",
    "C",
    "Article 22(4) provides that no law providing for preventive detention shall authorize the detention of a person for a longer period than 3 months unless an Advisory Board (consisting of HC judges) reports sufficient cause before expiration.",
    "பிரிவு 22(4) ஆலோசனைக் குழு (உயர்நீதிமன்ற நீதிபதிகள் கொண்ட குழு) போதிய காரணம் தெரிவிக்கும் வரை தடுப்புக் காவலை 3 மாதங்களுக்கு மேல் நீட்டிக்க முடியாது எனக் கூறுகிறது.",
    "Incorrect. 1 Month is not the constitutional limit under Art 22(4).", "தவறு. 1 மாதம் என்பது அரசியலமைப்பு வரம்பல்ல.",
    "Incorrect. 44th CAA 1978 proposed reducing limit to 2 months, but that provision has NOT been brought into force yet.", "தவறு. 44-வது திருத்தம் 1978 வரம்பை 2 மாதங்களாகக் குறைக்க முன்மொழிந்தது, ஆனால் அவ்விதி இதுவரை அமல்படுத்தப்படவில்லை.",
    "Correct. 3 Months is the present operative constitutional maximum limit.", "சரி. 3 மாதங்கள் என்பது தற்போதைய செயல்பாட்டு அரசியலமைப்பு அதிகபட்ச வரம்பாகும்.",
    "Incorrect. 6 Months is not the initial Advisory Board threshold.", "தவறு. 6 மாதங்கள் என்பது தொடக்க ஆலோசனைக் குழு வரம்பல்ல.",
    "TNPSC Trap: Note that 44th CAA 1978 passed a clause reducing detention without Advisory Board from 3 months to 2 months, BUT THIS AMENDMENT HAS STILL NOT BEEN NOTIFIED/ENFORCED. The present limit remains 3 MONTHS.",
    "TNPSC பொறி: 44-வது திருத்தம் 1978 தடுப்புக் காவல் வரம்பை 3 மாதங்களிலிருந்து 2 மாதங்களாகக் குறைக்க முன்மொழிந்தது, ஆனால் அவ்விதி இதுவரை அமலுக்கு வரவில்லை. தற்போதைய வரம்பு 3 மாதங்கள் மட்டுமே.",
    "Advisory Board consists of persons who are, or have been, or are qualified to be appointed as Judges of a High Court.",
    "ஆலோசனைக் குழு உயர்நீதிமன்ற நீதிபதிகளாக உள்ளவர்கள் அல்லது தகுதியானவர்களைக் கொண்டுள்ளது.",
    ["TNPSC Group 1 2017 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 22", "Preventive Detention"]
))

# FR_PYQ_028 (Medium | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_028", "Medium", "Direct MCQ",
    "Who is exclusively authorized under Article 33 of the Constitution of India to restrict or modify the application of Fundamental Rights to members of the Armed Forces and Police Forces?",
    "ஆயுதப் படைகள் மற்றும் காவல்துறைப் பணியாளர்களுக்கு அடிப்படை உரிமைகள் பொருந்தும் எல்லையைக் கட்டுப்படுத்த அல்லது மாற்றியமைக்க பிரிவு 33-ன் கீழ் யாருக்கு மட்டுமே அதிகாரம் அளிக்கப்பட்டுள்ளது?",
    "President of India", "இந்தியக் குடியரசுத் தலைவர்",
    "Union Home Minister", "மத்திய உள்துறை அமைச்சர்",
    "State Legislatures", "மாநில சட்டமன்றங்கள்",
    "Parliament of India", "இந்திய நாடாளுமன்றம்",
    "D",
    "Article 33 empowers Parliament of India EXCLUSIVELY to determine by law to what extent Fundamental Rights shall apply to members of Armed Forces, Para-military forces, Police forces, and Intelligence organizations, to ensure proper discharge of duties and maintenance of discipline.",
    "பிரிவு 33 ஆயுதப் படைகள், காவல் படைகள் மற்றும் உளவு அமைப்புகளுக்கு அடிப்படை உரிமைகளைக் கட்டுப்படுத்தும் சட்டங்களை இயற்றும் அதிகாரத்தை இந்திய நாடாளுமன்றத்திற்கு மட்டுமே வழங்குகிறது.",
    "Incorrect. President cannot modify Art 33 rights without Parliamentary law.", "தவறு. நாடாளுமன்றச் சட்டமின்றி குடியரசுத் தலைவர் பிரிவு 33 உரிமைகளை மாற்ற முடியாது.",
    "Incorrect. Union Home Minister has no constitutional legislative power.", "தவறு. மத்திய உள்துறை அமைச்சருக்கு அரசியலமைப்புச் சட்ட அதிகாரமில்லை.",
    "Incorrect. State Legislatures have NO power under Article 33/35.", "தவறு. மாநில சட்டமன்றங்களுக்கு பிரிவு 33/35-ன் கீழ் எந்த அதிகாரமும் இல்லை.",
    "Correct. Parliament of India alone has exclusive power under Article 33.", "சரி. இந்திய நாடாளுமன்றத்திற்கு மட்டுமே பிரிவு 33-ன் கீழ் தனி அதிகாரம் உண்டு.",
    "TNPSC Trap: Under Article 35(a)(i), power to make laws under Article 33 rests EXCLUSIVELY with Parliament, NOT State Legislatures (even for state police forces).",
    "TNPSC பொறி: பிரிவு 35(a)(i)-ன் படி பிரிவு 33-ன் கீழ் சட்டங்களை நாடாளுமன்றம் மட்டுமே இயற்ற முடியும், மாநில சட்டமன்றங்கள் இயற்ற முடியாது (மாநில காவல் படைகளுக்கும் இதுவே பொருந்தும்).",
    "Parliament enacted Army Act 1950, Navy Act 1950, Air Force Act 1950, and Police Forces (Restriction of Rights) Act 1966 under Article 33.",
    "நாடாளுமன்றம் பிரிவு 33-ன் கீழ் ராணுவச் சட்டம் 1950, கடற்படைச் சட்டம் 1950, விமானப்படைச் சட்டம் 1950 ஆகியவற்றை இயற்றியது.",
    ["TNPSC Assistant Director 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 33", "Armed Forces"]
))

# FR_PYQ_029 (Medium | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_029", "Medium", "Direct MCQ",
    "Which Article of the Constitution empowers Parliament to enact an Act of Indemnity protecting government servants for acts done during the operation of Martial Law in any area?",
    "எந்தவொரு பகுதியிலும் ராணுவச் சட்டம் (Martial Law) அமலில் இருக்கும் போது அரசுப் பணியாளர்கள் செய்த செயல்களுக்குப் பாதுகாப்பு அளிக்கும் நஷ்டஈட்டுச் சட்டத்தை இயற்ற நாடாளுமன்றத்திற்கு எந்தப் பிரிவு அதிகாரம் அளிக்கிறது?",
    "Article 34", "பிரிவு 34",
    "Article 33", "பிரிவு 33",
    "Article 35", "பிரிவு 35",
    "Article 32", "பிரிவு 32",
    "A",
    "Article 34 provides for restrictions on Fundamental Rights while Martial Law is in force in any area. It empowers Parliament to indemnify any person in government service for acts done in connection with maintenance or restoration of order.",
    "பிரிவு 34 ராணுவச் சட்டம் அமலில் இருக்கும் போது அடிப்படை உரிமைகளைக் கட்டுப்படுத்துகிறது. ஒழுங்கைப் பராமரிக்க அரசுப் பணியாளர்கள் செய்த செயல்களுக்கு நஷ்டஈட்டுச் சட்டம் இயற்ற இது நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
    "Correct. Article 34 deals with Martial Law and Act of Indemnity.", "சரி. பிரிவு 34 ராணுவச் சட்டம் மற்றும் நஷ்டஈட்டுச் சட்டம் பற்றிப் பேசுகிறது.",
    "Incorrect. Article 33 deals with Armed Forces restrictions.", "தவறு. பிரிவு 33 ஆயுதப் படைக் கட்டுப்பாடுகள் பற்றிப் பேசுகிறது.",
    "Incorrect. Article 35 deals with legislation to give effect to Part III.", "தவறு. பிரிவு 35 பகுதி III-ஐ அமல்படுத்தும் சட்டங்கள் பற்றிப் பேசுகிறது.",
    "Incorrect. Article 32 deals with Constitutional Remedies.", "தவறு. பிரிவு 32 அரசியலமைப்பு பரிகாரங்கள் பற்றிப் பேசுகிறது.",
    "TNPSC Trap: The term 'Martial Law' is NOT defined anywhere in the Constitution of India. It means military rule under extraordinary circumstances of insurrection or war.",
    "TNPSC பொறி: 'ராணுவச் சட்டம்' (Martial Law) என்ற சொல் இந்திய அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை. இது அசாதாரண ராணுவ ஆட்சியைக் குறிக்கிறது.",
    "Martial Law (Article 34) affects ONLY Fundamental Rights, whereas National Emergency (Article 352) affects FRs, Centre-State relations, and legislative powers.",
    "ராணுவச் சட்டம் (பிரிவு 34) அடிப்படை உரிமைகளை மட்டுமே பாதிக்கும், ஆனால் தேசிய அவசரநிலை (பிரிவு 352) மத்திய-மாநில உறவுகளையும் பாதிக்கும்.",
    ["TNPSC Group 1 2020 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 34", "Martial Law"]
))

# FR_PYQ_030 (Medium | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_030", "Medium", "Direct MCQ",
    "Under Article 28 of the Constitution, religious instruction is COMPLETELY PROHIBITED in which category of educational institutions?",
    "அரசியலமைப்பின் பிரிவு 28-ன் கீழ் எந்த வகை கல்வி நிறுவனங்களில் மத போதனை முற்றிலும் தடை செய்யப்பட்டுள்ளது?",
    "Institutions recognized by the State", "அரசால் அங்கீகரிக்கப்பட்ட நிறுவனங்கள்",
    "Institutions wholly maintained out of State funds", "முழுவதும் அரசு நிதியில் பராமரிக்கப்படும் நிறுவனங்கள்",
    "Institutions administered by the State but established under a trust/endowment", "அரசால் நிர்வகிக்கப்படும் ஆனால் அறக்கட்டளையின் கீழ் நிறுவப்பட்ட நிறுவனங்கள்",
    "Institutions receiving aid out of State funds", "அரசிடமிருந்து நிதியுதவி பெறும் நிறுவனங்கள்",
    "B",
    "Article 28(1) states: 'No religious instruction shall be provided in any educational institution wholly maintained out of State funds.' Article 28 classifies institutions into 4 types: 1. Wholly maintained by State = Religion COMPLETELY BANNED. 2. Administered by State but established under Trust = Religion PERMITTED. 3. Recognized by State = Voluntary basis. 4. Receiving aid = Voluntary basis.",
    "பிரிவு 28(1) கூறுவது: 'முழுவதும் அரசு நிதியில் பராமரிக்கப்படும் எந்தவொரு கல்வி நிறுவனத்திலும் மத போதனை வழங்கப்படக் கூடாது.' இங்கு மத போதனை முற்றிலும் தடை செய்யப்பட்டுள்ளது.",
    "Incorrect. Recognized institutions permit voluntary religious instruction.", "தவறு. அங்கீகரிக்கப்பட்ட நிறுவனங்களில் விருப்பத்தின் பேரில் மத போதனை அனுமதிக்கப்படுகிறது.",
    "Correct. Wholly maintained State institutions completely ban religious instruction.", "சரி. முழுவதும் அரசு நிதியில் இயங்கும் நிறுவனங்களில் மத போதனை முற்றிலும் தடை செய்யப்பட்டுள்ளது.",
    "Incorrect. State-administered trust institutions permit religious instruction.", "தவறு. அறக்கட்டளை மூலம் நிறுவப்பட்டு அரசால் நிர்வகிக்கப்படும் நிறுவனங்களில் மத போதனை அனுமதிக்கப்படுகிறது.",
    "Incorrect. Aided institutions permit voluntary religious instruction.", "தவறு. அரசிடம் நிதியுதவி பெறும் நிறுவனங்களில் விருப்பத்தின் பேரில் மத போதனை அனுமதிக்கப்படுகிறது.",
    "TNPSC Trap: Category 2 (Institutions administered by State BUT established under an endowment/trust requiring religious instruction) CAN impart religious instruction (Article 28(2) Exception).",
    "TNPSC பொறி: வகை 2 (அறக்கட்டளை மூலம் நிறுவப்பட்டு அரசால் நிர்வகிக்கப்படும் நிறுவனங்கள்) மத போதனை வழங்க அனுமதி உண்டு (பிரிவு 28(2) விதிவிலக்கு).",
    "Article 28 distinguishes four categories of educational institutions regarding religious instruction.",
    "பிரிவு 28 மத போதனை தொடர்பாக நான்கு வகை கல்வி நிறுவனங்களை வேறுபடுத்துகிறது.",
    ["TNPSC Group 2A 2017 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 28", "Religious Instruction"]
))

# FR_PYQ_031 (Hard | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_031", "Hard", "Direct MCQ",
    "Following the 44th Constitutional Amendment Act 1978, enforcement of which pair of Fundamental Rights CANNOT be suspended even during a proclamation of National Emergency under Article 352?",
    "44-வது அரசியலமைப்பு திருத்தச் சட்டம் 1978-ஐத் தொடர்ந்து, பிரிவு 352-ன் கீழ் தேசிய அவசரநிலை பிரகடனம் செய்யப்பட்டாலும் எந்த ஜோடி அடிப்படை உரிமைகளின் அமலாக்கத்தை இடைநிறுத்த முடியாது?",
    "Articles 14 and 19", "பிரிவுகள் 14 மற்றும் 19",
    "Articles 19 and 21", "பிரிவுகள் 19 மற்றும் 21",
    "Articles 20 and 21", "பிரிவுகள் 20 மற்றும் 21",
    "Articles 21 and 22", "பிரிவுகள் 21 மற்றும் 22",
    "C",
    "The 44th Constitutional Amendment Act, 1978 amended Article 359 so that the President CANNOT suspend the right to move courts for enforcement of Articles 20 (Protection in respect of conviction for offences) and 21 (Protection of life and personal liberty) during National Emergency.",
    "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 பிரிவு 359-ஐத் திருத்தியது, இதன் மூலம் தேசிய அவசரநிலையின் போதும் பிரிவுகள் 20 (குற்ற தண்டனைப் பாதுகாப்பு) மற்றும் 21 (வாழ்வுரிமை) அமலாக்கத்தை இடைநிறுத்த முடியாது.",
    "Incorrect. Article 14 and 19 can be suspended during emergency.", "தவறு. பிரிவுகள் 14 மற்றும் 19 அவசரநிலையின் போது இடைநிறுத்தப்படலாம்.",
    "Incorrect. Article 19 is automatically suspended under Article 358 during external emergency.", "தவறு. பிரிவு 19 வெளிவாரி அவசரநிலையின் போது தானாக இடைநிறுத்தப்படும்.",
    "Correct. Articles 20 and 21 CANNEVER be suspended under any emergency.", "சரி. பிரிவுகள் 20 மற்றும் 21 எந்தவொரு அவசரநிலையிலும் ஒருபோதும் இடைநிறுத்தப்பட முடியாது.",
    "Incorrect. Article 22 can be suspended under Article 359 order.", "தவறு. பிரிவு 22 பிரிவு 359 உத்தரவின் கீழ் இடைநிறுத்தப்படலாம்.",
    "TNPSC Trap: Article 358 automatically suspends Article 19 ONLY during External Emergency (War/External Aggression), NOT Internal Emergency (Armed Rebellion). Article 359 suspends enforcement of specified FRs EXCEPT Articles 20 and 21.",
    "TNPSC பொறி: பிரிவு 358 வெளிவாரி அவசரநிலையின் போது மட்டுமே பிரிவு 19-ஐ தானாக இடைநிறுத்தும் (போர்/அன்னிய ஆக்கிரமிப்பு). பிரிவு 359 பிரிவுகள் 20 மற்றும் 21 தவிர பிற உரிமைகளை இடைநிறுத்தும்.",
    "Articles 20 and 21 remain enforceable by courts even during the gravest National Emergency.",
    "மிகக் கடுமையான தேசிய அவசரநிலையின் போதும் பிரிவுகள் 20 மற்றும் 21 நீதிமன்றங்களால் அமல்படுத்தத்தக்கவையாகத் தொடர்கின்றன.",
    ["TNPSC Group 1 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Emergency", "Articles 20 and 21"]
))

# FR_PYQ_032 (Hard | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_032", "Hard", "Direct MCQ",
    "Which of the following is NOT included within the scope of 'law' defined under Article 13(3)(a) of the Constitution for checking inconsistency with Part III?",
    "பகுதி III-உடன் முரண்பாட்டைச் சரிபார்க்க பிரிவு 13(3)(a)-ன் கீழ் வரையறுக்கப்பட்ட 'சட்டம்' என்ற எல்லைக்குள் பின்வருவனவற்றில் எது சேர்க்கப்படவில்லை?",
    "Ordinances issued by the President or State Governors", "குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்களால் பிறப்பிக்கப்பட்ட அவசரச் சட்டங்கள்",
    "Bye-laws, Rules, Regulations, or Notifications issued by municipal bodies or statutory boards", "நகராட்சி அமைப்புகள் அல்லது சட்டப்பூர்வ வாரியங்களால் வெளியிடப்பட்ட துணை விதிகள், விதிகள், ஒழுங்குமுறைகள்",
    "Customs or Usages having the force of law in the territory of India", "இந்திய ভূখণ্ডத்தில் சட்டப்பூர்வ பலம் கொண்ட பழக்கவழக்கங்கள் அல்லது வழக்கங்கள்",
    "Constitutional Amendment Acts passed under Article 368", "பிரிவு 368-ன் கீழ் நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்தச் சட்டங்கள்",
    "D",
    "In Kesavananda Bharati case (1973) and 24th CAA (1971), it was affirmed that a Constitutional Amendment Act passed under Article 368 is constituent law, NOT ordinary 'law' within the meaning of Article 13(2). Amendments are challenged under Basic Structure Doctrine, NOT Article 13.",
    "கேசவாநந்த பாரதி வழக்கில் (1973) பிரிவு 368-ன் கீழ் நிறைவேற்றப்படும் அரசியலமைப்பு திருத்தச் சட்டம் பிரிவு 13(2)-ன் கீழ் வரும் சாதாரண 'சட்டம்' அல்ல எனத் தெளிவுபடுத்தப்பட்டது. அவை அடிப்படை அமைப்புக் கோட்பாட்டின் கீழ் கேள்வி கேட்கப்படுகின்றன.",
    "Incorrect. Ordinances fall under statutory temporary law in Art 13(3)(a).", "தவறு. அவசரச் சட்டங்கள் பிரிவு 13(3)(a)-ன் கீழ் தற்காலிகச் சட்டமாக வருகின்றன.",
    "Incorrect. Bye-laws and notifications fall under delegated executive law in Art 13(3)(a).", "தவறு. துணை விதிகள் மற்றும் அறிவிக்கைகள் பிரிவு 13(3)(a)-ன் கீழ் வருகின்றன.",
    "Incorrect. Customs having force of law fall under non-statutory law in Art 13(3)(a).", "தவறு. சட்டப் பலம் கொண்ட பழக்கவழக்கங்கள் பிரிவு 13(3)(a)-ன் கீழ் வருகின்றன.",
    "Correct. Constitutional Amendments are NOT 'law' under Article 13.", "சரி. அரசியலமைப்பு திருத்தங்கள் பிரிவு 13-ன் கீழ் 'சட்டம்' அல்ல.",
    "TNPSC Trap: Article 13(3)(a) defines 'law' broadly to include: Permanent laws, Temporary laws (Ordinances), Statutory instruments (Rules, Bye-laws), and Non-statutory sources (Custom/Usage).",
    "TNPSC பொறி: பிரிவு 13(3)(a) 'சட்டம்' என்பதை பரந்த அளவில் வரையறுக்கிறது: நிரந்தரச் சட்டங்கள், தற்காலிகச் சட்டங்கள் (அவசரச் சட்டம்), சட்டப்பூர்வக் கருவிகள், மற்றும் பழக்கவழக்கங்கள்.",
    "Constitutional Amendment is constituent law, distinct from ordinary legislative law under Article 13.",
    "அரசியலமைப்பு திருத்தம் என்பது அரசியலமைப்பு உருவாக்கும் அதிகாரமாகும், இது பிரிவு 13-ன் சாதாரண சட்டத்திலிருந்து வேறுபட்டது.",
    ["TNPSC Group 1 2021 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Article 13", "Definition of Law"]
))

# FR_PYQ_033 (Hard | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_033", "Hard", "Direct MCQ",
    "In which landmark case did the Supreme Court hold that the Indian Constitution is founded on the bedrock of the balance between Fundamental Rights and Directive Principles?",
    "அடிப்படை உரிமைகளுக்கும் அரசு வழிகாட்டு நெறிமுறைகளுக்கும் இடையிலான சமநிலை என்ற அடித்தளத்தில் தான் இந்திய அரசியலமைப்பு அமைந்துள்ளது என உச்சநீதிமன்றம் எந்த வழக்கில் தீர்ப்பளித்தது?",
    "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (1980)",
    "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிராக கேரளா மாநிலம் (1973)",
    "I.C. Golaknath v. State of Punjab (1967)", "ஐ.சி. கோலக்நாத் எதிராக பஞ்சாப் மாநிலம் (1967)",
    "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி எதிராக இந்திய யூனியன் (1978)",
    "A",
    "In Minerva Mills v. Union of India (1980), the Supreme Court struck down Section 4 of 42nd CAA 1976 and declared: 'The Indian Constitution is founded on the bedrock of the balance between Part III and Part IV. To give absolute primacy to one over the other is to disturb the harmony of the Constitution.'",
    "மினர்வா மில்ஸ் வழக்கில் (1980) உச்சநீதிமன்றம் 42-வது திருத்தத்தின் பிரிவு 4-ஐ ரத்து செய்து: 'பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையே அரசியலமைப்பின் அடித்தளம்' என அறிவித்தது.",
    "Correct. Minerva Mills (1980) established the harmony between Part III and Part IV as Basic Structure.", "சரி. மினர்வா மில்ஸ் (1980) பகுதி III மற்றும் IV இடையிலான சமநிலையை அடிப்படை அமைப்பு எனக் கூறியது.",
    "Incorrect. Kesavananda Bharati (1973) propounded Basic Structure Doctrine generally.", "தவறு. கேசவாநந்த பாரதி (1973) பொதுவாக அடிப்படை அமைப்புக் கோட்பாட்டை உருவாக்கியது.",
    "Incorrect. Golaknath (1967) held Fundamental Rights are unamendable.", "தவறு. கோலக்நாத் (1967) அடிப்படை உரிமைகள் திருத்த முடியாதவை எனக் கூறியது.",
    "Incorrect. Maneka Gandhi (1978) introduced procedural due process under Article 21.", "தவறு. மேனகா காந்தி (1978) பிரிவு 21-ல் நீதியான நடைமுறையை அறிமுகப்படுத்தியது.",
    "TNPSC Trap: Part III vs Part IV evolution: Champakam Dorairajan (1951) = FR Primacy. Kerala Education Bill (1958) = Harmonious Construction. Minerva Mills (1980) = Balance between FRs & DPSPs is Basic Structure.",
    "TNPSC பொறி: பகுதி III vs IV வளர்ச்சி: சண்பகம் துரைராஜன் (1951) = அடிப்படை உரிமை மேலாதிக்கம். கேரளா கல்வி மசோதா (1958) = இணக்கமான விளக்கம். மினர்வா மில்ஸ் (1980) = சமநிலையே அடிப்படை அமைப்பு.",
    "Minerva Mills (1980) affirmed Judicial Review and FR-DPSP balance as inviolable Basic Structure features.",
    "மினர்வா மில்ஸ் (1980) நீதித்துறை மறுஆய்வு மற்றும் உரிமைகள்-நெறிமுறைகள் சமநிலையை அடிப்படை அமைப்பாக உறுதிப்படுத்தியது.",
    ["TNPSC Group 1 2018 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Minerva Mills Case", "FR vs DPSP"]
))

# FR_PYQ_034 (Medium | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_034", "Medium", "Direct MCQ",
    "Article 15(4) empowering the State to make special provision for the advancement of socially and educationally backward classes was added to the Constitution by which Amendment following the Champakam Dorairajan case?",
    "சண்பகம் துரைராஜன் வழக்கைத் தொடர்ந்து, சமூக ரீதியாகவும் கல்வி ரீதியாகவும் பின்தங்கிய வகுப்பினரின் முன்னேற்றத்திற்காக சிறப்பு விதிகளை செய்ய அரசுக்கு அதிகாரம் அளிக்கும் பிரிவு 15(4) எந்தத் திருத்தத்தின் மூலம் சேர்க்கப்பட்டது?",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "1st Constitutional Amendment Act, 1951", "1-வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
    "77th Constitutional Amendment Act, 1995", "77-வது அரசியலமைப்பு திருத்தச் சட்டம், 1995",
    "93rd Constitutional Amendment Act, 2005", "93-வது அரசியலமைப்பு திருத்தச் சட்டம், 2005",
    "B",
    "Following the Supreme Court judgment in State of Madras v. Champakam Dorairajan (1951) striking down communal G.O. in medical admissions, Jawaharlal Nehru Government enacted the 1st Constitutional Amendment Act 1951 inserting Article 15(4).",
    "சண்பகம் துரைராஜன் வழக்கில் (1951) வகுப்புவாத அரசாணையை உச்சநீதிமன்றம் ரத்து செய்ததைத் தொடர்ந்து, ஜவகர்லால் நேரு அரசு 1-வது திருத்தச் சட்டம் 1951 மூலம் பிரிவு 15(4)-ஐச் சேர்த்தது.",
    "Incorrect. 42nd CAA was enacted in 1976.", "தவறு. 42-வது திருத்தம் 1976-ல் கொண்டுவரப்பட்டது.",
    "Correct. 1st CAA 1951 inserted Article 15(4).", "சரி. 1-வது திருத்தம் 1951 பிரிவு 15(4)-ஐச் சேர்த்தது.",
    "Incorrect. 77th CAA 1995 inserted Article 16(4A) for promotion reservation.", "தவறு. 77-வது திருத்தம் 1995 பிரிவு 16(4A)-ஐச் சேர்த்தது.",
    "Incorrect. 93rd CAA 2005 inserted Article 15(5) for educational reservation.", "தவறு. 93-வது திருத்தம் 2005 பிரிவு 15(5)-ஐச் சேர்த்தது.",
    "TNPSC Trap: Champakam Dorairajan Case (1951) was the very first major Fundamental Rights decision of the Supreme Court, prompting the 1st Constitutional Amendment Act 1951.",
    "TNPSC பொறி: சண்பகம் துரைராஜன் வழக்கு (1951) உச்சநீதிமன்றத்தின் மிக முதல் பெரிய அடிப்படை உரிமைகள் தீர்ப்பாகும், இது 1-வது திருத்தச் சட்டம் 1951-க்கு வழிவகுத்தது.",
    "1st CAA 1951 added Article 15(4), Article 31A, Article 31B, and Ninth Schedule to the Constitution.",
    "1-வது திருத்தம் 1951 அரசியலமைப்பில் பிரிவு 15(4), பிரிவு 31A, பிரிவு 31B மற்றும் 9-வது அட்டவணையைச் சேர்த்தது.",
    ["TNPSC Group 2 2017 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "1st CAA 1951", "Article 15(4)"]
))

# FR_PYQ_035 (Medium | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_035", "Medium", "Direct MCQ",
    "Which Constitutional Amendment Act introduced 10% reservation for Economically Weaker Sections (EWS) in education and public employment by inserting Articles 15(6) and 16(6)?",
    "பிரிவுகள் 15(6) மற்றும் 16(6)-ஐச் சேர்ப்பதன் மூலம் கல்வி மற்றும் பொது வேலைவாய்ப்பில் பொருளாதாரத்தில் நலிவடைந்த பிரிவினருக்கு (EWS) 10% இடஒதுக்கீட்டை எந்த அரசியலமைப்பு திருத்தச் சட்டம் அறிமுகப்படுத்தியது?",
    "101st Constitutional Amendment Act, 2016", "101-வது அரசியலமைப்பு திருத்தச் சட்டம், 2016",
    "102nd Constitutional Amendment Act, 2018", "102-வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
    "103rd Constitutional Amendment Act, 2019", "103-வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
    "104th Constitutional Amendment Act, 2020", "104-வது அரசியலமைப்பு திருத்தச் சட்டம், 2020",
    "C",
    "The 103rd Constitutional Amendment Act, 2019 inserted Articles 15(6) and 16(6) providing up to 10% reservation for Economically Weaker Sections (EWS) among citizens other than SCs, STs, and OBCs. Upheld in Janhit Abhiyan Case (2022).",
    "103-வது அரசியலமைப்பு திருத்தச் சட்டம், 2019 பிரிவுகள் 15(6) மற்றும் 16(6)-ஐச் சேர்த்து SC, ST, OBC தவிர்த்த பொருளாதாரத்தில் பின்தங்கிய பிரிவினருக்கு 10% இடஒதுக்கீட்டை வழங்கியது.",
    "Incorrect. 101st CAA 2016 introduced Goods and Services Tax (GST).", "தவறு. 101-வது திருத்தம் 2016 சரக்கு மற்றும் சேவை வரியை (GST) அறிமுகப்படுத்தியது.",
    "Incorrect. 102nd CAA 2018 gave constitutional status to NCBC (Article 338B).", "தவறு. 102-வது திருத்தம் 2018 NCBC-க்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
    "Correct. 103rd CAA 2019 introduced 10% EWS reservation.", "சரி. 103-வது திருத்தம் 2019 10% EWS இடஒதுக்கீட்டை அறிமுகப்படுத்தியது.",
    "Incorrect. 104th CAA 2020 extended SC/ST Lok Sabha reservation & removed Anglo-Indian nomination.", "தவறு. 104-வது திருத்தம் 2020 ஏங்லோ-இந்தியன் நியமனத்தை நீக்கியது.",
    "TNPSC Trap: Recent Constitutional Amendments matching: 101st = GST, 102nd = NCBC, 103rd = EWS Reservation, 104th = SC/ST Extension & Anglo-Indian Removal, 106th = Women's Reservation (Nari Shakti Vandan).",
    "TNPSC பொறி: சமீபத்திய திருத்தப் பொருத்தம்: 101 = GST, 102 = NCBC, 103 = EWS இடஒதுக்கீடு, 104 = SC/ST நீட்டிப்பு & ஆங்கிலோ-இந்தியன் நீக்கம், 106 = மகளிர் இடஒதுக்கீடு.",
    "103rd CAA added Articles 15(6) and 16(6) for EWS reservation.", "103-வது திருத்தம் EWS இடஒதுக்கீட்டிற்காக பிரிவுகள் 15(6) மற்றும் 16(6)-ஐச் சேர்த்தது.",
    ["TNPSC Group 1 2022 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "103rd CAA", "EWS Reservation"]
))

# FR_PYQ_036 (Medium | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_036", "Medium", "Direct MCQ",
    "In Justice K.S. Puttaswamy (Retd.) v. Union of India (2017), a 9-judge bench of the Supreme Court unanimously declared the Right to Privacy as an intrinsic part of which Article?",
    "நீதிபதி கே.எஸ். புட்டசுவாமி எதிராக இந்திய யூனியன் (2017) வழக்கில், உச்சநீதிமன்றத்தின் 9 நீதிபதிகள் அமர்வு தனிமனித தனியுரிமையை (Right to Privacy) எந்தப் பிரிவின் ஒரு அங்கமாக ஒருமனதாக அறிவித்தது?",
    "Article 14", "பிரிவு 14",
    "Article 19", "பிரிவு 19",
    "Article 25", "பிரிவு 25",
    "Article 21", "பிரிவு 21",
    "D",
    "In Justice K.S. Puttaswamy v. Union of India (August 24, 2017), a 9-judge Bench unanimously held that the Right to Privacy is a Fundamental Right protected as an intrinsic part of the Right to Life and Personal Liberty under Article 21.",
    "நீதிபதி கே.எஸ். புட்டசுவாமி வழக்கில் (2017) 9 நீதிபதிகள் கொண்ட அமர்வு தனியுரிமை (Right to Privacy) என்பது பிரிவு 21-ன் கீழ் வாழ்வுரிமை மற்றும் தனிநபர் சுதந்திரத்தின் ஒருங்கிணைந்த பகுதி என ஒருமனதாகத் தீர்ப்பளித்தது.",
    "Incorrect. Article 14 deals with Equality before Law.", "தவறு. பிரிவு 14 சட்டத்தின் முன் சமத்துவம் பற்றியது.",
    "Incorrect. Article 19 deals with Six Freedoms.", "தவறு. பிரிவு 19 ஆறு சுதந்திரங்கள் பற்றியது.",
    "Incorrect. Article 25 deals with Freedom of Conscience.", "தவறு. பிரிவு 25 மனசாட்சி சுதந்திரம் பற்றியது.",
    "Correct. Article 21 contains Right to Privacy under Puttaswamy ruling.", "சரி. பிரிவு 21 புட்டசுவாமி தீர்ப்பின்படி தனியுரிமையை உள்ளடக்கியது.",
    "TNPSC Trap: Rights declared as part of Article 21: Right to Privacy (Puttaswamy 2017), Right to Livelihood (Olga Tellis 1985), Right to Clean Environment (Subhash Kumar 1991), Right to Speedy Trial (Hussainara Khatoon 1979).",
    "TNPSC பொறி: பிரிவு 21-ன் அங்கமாக அறிவிக்கப்பட்ட உரிமைகள்: தனியுரிமை (புட்டசுவாமி 2017), வாழ்வாதார உரிமை (ஒல்கா டெல்லிஸ் 1985), சுத்தமான சுற்றுச்சூழல் (சுபாஷ் குமார் 1991).",
    "Puttaswamy 2017 overruled MP Sharma (1954) and Kharak Singh (1962) to hold Privacy as a fundamental right.",
    "புட்டசுவாமி 2017 தீர்ப்பு எம்.பி. சர்மா மற்றும் கரக் சிங் வழக்குகளை ரத்து செய்து தனியுரிமையை அடிப்படை உரிமையாக்கியது.",
    ["TNPSC Group 1 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Puttaswamy Case", "Right to Privacy"]
))

# FR_PYQ_037 (Hard | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_037", "Hard", "Direct MCQ",
    "Why is the writ jurisdiction of High Courts under Article 226 considered constitutionally wider in scope than that of the Supreme Court under Article 32?",
    "பிரிவு 32-ன் கீழ் உச்சநீதிமன்றத்தின் பேராணை அதிகாரத்தை விட பிரிவு 226-ன் கீழ் உயர்நீதிமன்றத்தின் பேராணை அதிகாரம் அரசியலமைப்பு ரீதியாக ஏன் பரந்த எல்லை கொண்டதாகக் கருதப்படுகிறது?",
    "High Courts can issue writs for the enforcement of Fundamental Rights as well as ordinary legal rights, whereas Supreme Court can issue writs ONLY for Fundamental Rights", "உயர்நீதிமன்றங்கள் அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்ட உரிமைகள் இரண்டிற்கும் பேராணைகளை வெளியிடலாம், ஆனால் உச்சநீதிமன்றம் அடிப்படை உரிமைகளுக்கு மட்டுமே பேராணைகளை வெளியிட முடியும்",
    "High Court decisions under Article 226 cannot be challenged in appeal before the Supreme Court", "பிரிவு 226-ன் கீழ் உயர்நீதிமன்ற தீர்ப்புகளை உச்சநீதிமன்றத்தில் மேல்முறையீடு செய்ய முடியாது",
    "High Courts have territorial writ jurisdiction over the entire territory of India", "உயர்நீதிமன்றங்கள் இந்தியா முழுமைக்கும் புவியியல் பேராணை அதிகார வரம்பைக் கொண்டுள்ளன",
    "Supreme Court requires prior resolution of Parliament before issuing any writ", "உச்சநீதிமன்றம் எந்தவொரு பேராணையையும் வெளியிடுவதற்கு முன் நாடாளுமன்றத்தின் முன்அனுமதியைப் பெற வேண்டும்",
    "A",
    "Subject-matter scope: Supreme Court under Article 32 can issue writs ONLY for enforcement of Fundamental Rights. High Court under Article 226 can issue writs for Fundamental Rights AND 'for any other purpose' (enforcement of ordinary legal rights). Hence Article 226 is wider in subject scope.",
    "பொருள் எல்லை: பிரிவு 32-ன் கீழ் உச்சநீதிமன்றம் அடிப்படை உரிமைகளுக்கு மட்டுமே பேராணைகளை வெளியிட முடியும். பிரிவு 226-ன் கீழ் உயர்நீதிமன்றம் அடிப்படை உரிமைகள் மற்றும் பிற சட்ட உரிமைகளுக்கும் பேராணைகளை வெளியிட முடியும்.",
    "Correct. High Courts cover FRs plus ordinary legal rights under Article 226.", "சரி. உயர்நீதிமன்றங்கள் பிரிவு 226-ன் கீழ் அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்ட உரிமைகளையும் உள்ளடக்குகின்றன.",
    "Incorrect. High Court decisions under Art 226 are appealable to the Supreme Court.", "தவறு. உயர்நீதிமன்ற தீர்ப்புகள் உச்சநீதிமன்றத்தில் மேல்முறையீடு செய்யத்தக்கவை.",
    "Incorrect. Supreme Court has nationwide territorial jurisdiction under Art 32, whereas High Court jurisdiction is restricted to its State territory.", "தவறு. உச்சநீதிமன்றம் இந்தியா முழுமைக்கும் அதிகார வரம்பு கொண்டது.",
    "Incorrect. No parliamentary permission is needed for judicial writs.", "தவறு. பேராணைகளுக்கு நாடாளுமன்ற அனுமதி தேவையில்லை.",
    "TNPSC Trap: Subject-matter Scope: High Court (Art 226) > Supreme Court (Art 32). Territorial Scope: Supreme Court (Art 32) > High Court (Art 226). Remedy nature: Art 32 is itself a Fundamental Right; Art 226 is a discretionary remedy.",
    "TNPSC பொறி: பொருள் எல்லை: உயர்நீதிமன்றம் (226) > உச்சநீதிமன்றம் (32). புவியியல் எல்லை: உச்சநீதிமன்றம் (32) > உயர்நீதிமன்றம் (226). பரிகாரத் தன்மை: பிரிவு 32 தானே ஒரு அடிப்படை உரிமை.",
    "Article 32 is a guaranteed Fundamental Right, whereas Article 226 is a discretionary constitutional remedy.",
    "பிரிவு 32 என்பது உத்திரவாதம் அளிக்கப்பட்ட அடிப்படை உரிமையாகும், ஆனால் பிரிவு 226 என்பது விருப்ப அரசியலமைப்பு பரிகாரமாகும்.",
    ["TNPSC Group 2 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Article 32", "Article 226", "Writ Jurisdiction"]
))

# FR_PYQ_038 (Hard | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_038", "Hard", "Direct MCQ",
    "The writ of Prohibition (issued to stop an ongoing proceeding in excess of jurisdiction) can be issued ONLY against which category of authorities?",
    "அதிகார வரம்பை மீறி நடப்பில் உள்ள வழக்கைத் தடுப்பதற்காக வெளியிடப்படும் புரோஹிபிஷன் (தடைப்) பேராணை எந்த வகை அதிகாரிகளுக்கு எதிராக மட்டுமே வெளியிடப்பட முடியும்?",
    "Administrative authorities and private individuals", "நிர்வாக அதிகாரிகள் மற்றும் தனியார் நபர்கள்",
    "Judicial and Quasi-judicial authorities only", "நீதித்துறை மற்றும் பகுதி-நீதித்துறை அதிகாரிகள் மட்டுமே",
    "Legislative assemblies and municipal corporations", "சட்டமன்றங்கள் மற்றும் நகராட்சி அமைப்புகள்",
    "Private corporations and statutory commercial boards", "தனியார் நிறுவனங்கள் மற்றும் சட்டப்பூர்வ வணிக வாரியங்கள்",
    "B",
    "The writ of Prohibition is issued by a higher court to a lower court or quasi-judicial tribunal to prevent it from exceeding its jurisdiction or usurping jurisdiction not legally vested. It DOES NOT lie against administrative bodies, legislative bodies, or private individuals.",
    "புரோஹிபிஷன் பேராணை ஒரு மேல்நீதிமன்றத்தால் கீழ்நீதிமன்றம் அல்லது பகுதி-நீதிமன்றத் தீர்ப்பாயத்திற்கு எதிராக மட்டுமே பிறப்பிக்கப்படும். இது நிர்வாக அமைப்புகள், சட்டமன்றங்கள் அல்லது தனியார் நபர்களுக்கு எதிராகப் பொருந்தாது.",
    "Incorrect. Prohibition does not lie against administrative authorities or private individuals.", "தவறு. புரோஹிபிஷன் நிர்வாக அதிகாரிகளுக்கோ தனியாருக்கோ எதிராகப் பொருந்தாது.",
    "Correct. Prohibition lies ONLY against judicial and quasi-judicial bodies.", "சரி. புரோஹிபிஷன் நீதித்துறை மற்றும் பகுதி-நீதித்துறை அமைப்புகளுக்கு எதிராக மட்டுமே பொருந்தும்.",
    "Incorrect. Prohibition does not lie against legislative assemblies.", "தவறு. புரோஹிபிஷன் சட்டமன்றங்களுக்கு எதிராகப் பொருந்தாது.",
    "Incorrect. Prohibition does not lie against private corporations.", "தவறு. புரோஹிபிஷன் தனியார் நிறுவனங்களுக்கு எதிராகப் பொருந்தாது.",
    "TNPSC Trap: Certiorari can lie against administrative authorities affecting rights (since 1991 ruling), BUT Prohibition remains confined ONLY to judicial and quasi-judicial authorities.",
    "TNPSC பொறி: செர்ஷியோரரை 1991 தீர்ப்பிற்குப் பின் நிர்வாக அதிகாரிகளுக்கும் பொருந்தும், ஆனால் புரோஹிபிஷன் நீதித்துறை மற்றும் பகுதி-நீதித்துறை அமைப்புகளுக்கு மட்டுமே பொருந்தும்.",
    "Prohibition means 'To forbid' and operates while proceedings are pending before a tribunal.",
    "புரோஹிபிஷன் என்பது 'தடுத்தல்' எனப்பொருள்படும், இது வழக்கு நிலுவையில் இருக்கும் போது செயல்படுகிறது.",
    ["TNPSC Group 1 2015 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Writs", "Prohibition"]
))

# FR_PYQ_039 (Medium | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_039", "Medium", "Direct MCQ",
    "Under Article 26 of the Constitution, every religious denomination or any section thereof has the fundamental right to do which of the following?",
    "அரசியலமைப்பின் பிரிவு 26-ன் கீழ், ஒவ்வொரு மதப் பிரிவும் அல்லது அதன் உட்பிரிவும் பின்வரும் எதைச் செய்ய அடிப்படை உரிமை கொண்டுள்ளன?",
    "Establish educational institutions with mandatory state funding", "கட்டாய அரசு நிதியுதவியுடன் கல்வி நிறுவனங்களை நிறுவுதல்",
    "Levy compulsory taxes on pilgrims for promoting their religion", "தங்களது மதத்தைப் பரப்ப பக்தர்கள் மீது கட்டாய வரிகளை விதித்தல்",
    "Establish and maintain institutions for religious and charitable purposes and manage its own affairs in matters of religion", "மத மற்றும் தர்ம நிறுவனங்களை நிறுவி பராமரித்தல் மற்றும் மத விவகாரங்களில் தங்களது சொந்த காரியங்களை நிர்வகித்தல்",
    "Enforce religious doctrines on non-believing citizens", "நம்பிக்கையற்ற குடிமக்கள் மீது மதக் கோட்பாடுகளைக் கட்டாயப்படுத்துதல்",
    "C",
    "Article 26 guarantees four rights to every religious denomination: (a) Establish and maintain institutions for religious and charitable purposes; (b) Manage its own affairs in matters of religion; (c) Own and acquire movable and immovable property; (d) Administer such property in accordance with law.",
    "பிரிவு 26 மதப் பிரிவுகளுக்கு 4 உரிமைகளை வழங்குகிறது: (a) மத மற்றும் தர்ம நிறுவனங்களை நிறுவி பராமரித்தல்; (b) மத விவகாரங்களை நிர்வகித்தல்; (c) அசையும் அசையா சொத்துக்களைப் பெறுதல்; (d) சொத்துக்களை சட்டப்படி நிர்வகித்தல்.",
    "Incorrect. State funding is governed by Articles 28 and 30.", "தவறு. அரசு நிதியுதவி பிரிவுகள் 28 மற்றும் 30-ல் சொல்லப்பட்டுள்ளது.",
    "Incorrect. Levying taxes for religion is forbidden by Article 27.", "தவறு. மதத்திற்காக வரி விதிப்பது பிரிவு 27-ல் தடை செய்யப்பட்டுள்ளது.",
    "Correct. Article 26 guarantees right to establish institutions and manage religious affairs.", "சரி. பிரிவு 26 நிறுவனங்களை நிறுவி மத விவகாரங்களை நிர்வகிக்கும் உரிமையை அளிக்கிறது.",
    "Incorrect. Article 26 does not allow enforcing doctrines on non-believers.", "தவறு. பிரிவு 26 நம்பிக்கையற்றோர் மீது மதக் கோட்பாடுகளைக் திணிக்க அனுமதிக்காது.",
    "TNPSC Trap: Article 26 protects 'Religious Denominations'. A religious denomination must satisfy 3 conditions (SP Mittal Case 1983): 1. Collection of individuals with common faith, 2. Common organization, 3. Designated by a distinctive name. (e.g. Ramakrishna Mission is a denomination, but Aurobindo Society is NOT).",
    "TNPSC பொறி: மதப் பிரிவு 3 நிபந்தனைகளை நிறைவு செய்ய வேண்டும் (எஸ்.பி. மிட்டல் வழக்கு 1983): பொதுவான நம்பிக்கை, பொதுவான அமைப்பு, தனித்துவமான பெயர். (எ.கா. ராமகிருஷ்ணா மிஷன் மதப்பிரிவு, ஆரோவில் சொசைட்டி அல்ல).",
    "Article 26 guarantees collective / corporate freedom of religion.",
    "பிரிவு 26 மதத்தின் கூட்டு / நிறுவன சுதந்திரத்தை உறுதி செய்கிறது.",
    ["TNPSC Group 2 2018 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 26", "Religious Denomination"]
))

# FR_PYQ_040 (Easy | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_040", "Easy", "Direct MCQ",
    "Under Article 21A, free and compulsory education is guaranteed by the State to all children of which age group?",
    "பிரிவு 21A-ன் கீழ், எந்த வயதுக் குழுவைச் சேர்ந்த அனைத்துக் குழந்தைகளுக்கும் இலவச மற்றும் கட்டாயக் கல்வியை அரசு உறுதி செய்கிறது?",
    "0 to 6 years", "0 முதல் 6 ஆண்டுகள்",
    "5 to 15 years", "5 முதல் 15 ஆண்டுகள்",
    "6 to 18 years", "6 முதல் 18 ஆண்டுகள்",
    "6 to 14 years", "6 முதல் 14 ஆண்டுகள்",
    "D",
    "Article 21A provides that the State shall provide free and compulsory education to all children of the age of six to fourteen years in such manner as the State may, by law, determine.",
    "பிரிவு 21A 6 முதல் 14 வயது வரையிலான அனைத்துக் குழந்தைகளுக்கும் இலவச மற்றும் கட்டாயக் கல்வியை அரசு வழங்க வேண்டும் எனக் கூறுகிறது.",
    "Incorrect. 0 to 6 years is covered under Article 45 (Early Childhood Care).", "தவறு. 0 முதல் 6 ஆண்டுகள் என்பது பிரிவு 45-ன் கீழ் வருகிறது.",
    "Incorrect. 5 to 15 years is not the constitutional age bracket.", "தவறு. 5 முதல் 15 ஆண்டுகள் என்பது அரசியலமைப்பு வயது வரம்பல்ல.",
    "Incorrect. 6 to 18 years is the Persons with Disabilities Act age limit.", "தவறு. 6 முதல் 18 ஆண்டுகள் என்பது மாற்றுத்திறனாளிகள் சட்ட வரம்பாகும்.",
    "Correct. Article 21A age group is 6 to 14 years.", "சரி. பிரிவு 21A-ன் வயது வரம்பு 6 முதல் 14 ஆண்டுகள் ஆகும்.",
    "TNPSC Trap: Age brackets matching: Article 21A = 6 to 14 years (Fundamental Right). Article 45 = Below 6 years (Early Childhood Care DPSP). Article 51A(k) = 6 to 14 years (Duty of Parent/Guardian).",
    "TNPSC பொறி: வயது வரம்பு பொருத்தம்: பிரிவு 21A = 6 முதல் 14 ஆண்டுகள் (அடிப்படை உரிமை). பிரிவு 45 = 6 வயதிற்கு உட்பட்டோர் (முன்செய் பராமரிப்பு). பிரிவு 51A(k) = 6 முதல் 14 ஆண்டுகள் (பெற்றோர் கடமை).",
    "Right to Education Act 2009 was enacted to operationalize Article 21A.",
    "பிரிவு 21A-வை அமல்படுத்த கல்வி உரிமைச் சட்டம் 2009 இயற்றப்பட்டது.",
    ["TNPSC Group 4 2019 PYQ", "Samacheer Kalvi 10th Social"], "Remember", 45, ["Polity", "Fundamental Rights", "Article 21A", "Age Group"]
))

# FR_PYQ_041 (Hard | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_041", "Hard", "Direct MCQ",
    "Article 16(4A) providing reservation in matters of promotion with consequential seniority for Scheduled Castes and Scheduled Tribes in public employment was inserted by which Constitutional Amendment Act?",
    "பொது வேலைவாய்ப்பில் பட்டியலின மற்றும் பழங்குடியினருக்குத் தொடர்ச்சியான மூப்புரிமையுடன் (Consequential Seniority) பதவி உயர்வில் இடஒதுக்கீடு வழங்கும் பிரிவு 16(4A) எந்த திருத்தத்தால் சேர்க்கப்பட்டது?",
    "77th CAA, 1995 (and amended by 85th CAA, 2001)", "77-வது திருத்தம், 1995 (மற்றும் 85-வது திருத்தம், 2001 மூலம் திருத்தப்பட்டது)",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "86th Constitutional Amendment Act, 2002", "86-வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
    "93rd Constitutional Amendment Act, 2005", "93-வது அரசியலமைப்பு திருத்தச் சட்டம், 2005",
    "A",
    "The 77th Constitutional Amendment Act 1995 inserted Article 16(4A) permitting reservation in promotions for SCs/STs, nullifying Indra Sawhney ruling on promotion. The 85th Constitutional Amendment Act 2001 subsequently added 'consequential seniority' to Article 16(4A).",
    "77-வது அரசியலமைப்பு திருத்தச் சட்டம் 1995 பிரிவு 16(4A)-ஐச் சேர்த்து SC/ST-க்கு பதவி உயர்வு இடஒதுக்கீட்டை அனுமதித்தது. 85-வது திருத்தம் 2001 இதனுடன் 'தொடர்ச்சியான மூப்புரிமை'யைச் சேர்த்தது.",
    "Correct. 77th CAA 1995 added Article 16(4A) for promotion reservation.", "சரி. 77-வது திருத்தம் 1995 பிரிவு 16(4A)-ஐச் சேர்த்தது.",
    "Incorrect. 44th CAA 1978 deleted Right to Property.", "தவறு. 44-வது திருத்தம் 1978 சொத்துரிமையை நீக்கியது.",
    "Incorrect. 86th CAA 2002 inserted Article 21A.", "தவறு. 86-வது திருத்தம் 2002 பிரிவு 21A-வைச் சேர்த்தது.",
    "Incorrect. 93rd CAA 2005 inserted Article 15(5) for private educational reservation.", "தவறு. 93-வது திருத்தம் 2005 பிரிவு 15(5)-ஐச் சேர்த்தது.",
    "TNPSC Trap: Reservation Amendments: 77th CAA = Article 16(4A) Promotion Reservation. 81st CAA = Article 16(4B) Carry-Forward / Backlog 50% Rule Exception. 85th CAA = Consequential Seniority. 93rd CAA = Article 15(5) OBC Reservation in Higher Education.",
    "TNPSC பொறி: இடஒதுக்கீட்டுத் திருத்தங்கள்: 77-வது = பிரிவு 16(4A) பதவி உயர்வு. 81-வது = பிரிவு 16(4B) நிலுவைப் பணியிட 50% விதி விலக்கு. 85-வது = தொடர்ச்சியான மூப்புரிமை. 93-வது = பிரிவு 15(5) உயர்கல்வி இடஒதுக்கீடு.",
    "M. Nagaraj Case (2006) upheld 77th, 81st, 82nd, and 85th CAAs subject to quantifiable data on backwardness & efficiency.",
    "எம். நாகராஜ் வழக்கு (2006) 77, 81, 82, 85-வது திருத்தங்களை பின்தங்கிய நிலைக்கான தரவுகளுக்கு உட்பட்டு உறுதி செய்தது.",
    ["TNPSC Group 1 2021 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "77th CAA", "Article 16(4A)"]
))

# FR_PYQ_042 (Medium | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_042", "Medium", "Direct MCQ",
    "Article 20(1) guarantees protection against Ex-Post Facto Law. What is the true legal meaning of this constitutional protection?",
    "பிரிவு 20(1) பின்னோக்கிய விளைவுச் சட்டத்திற்கு எதிரான பாதுகாப்பை உறுதி செய்கிறது. இந்த அரசியலமைப்புப் பாதுகாப்பின் உண்மையான சட்டப்பூர்வ பொருள் என்ன?",
    "Civil liabilities and tax obligations cannot be imposed with retrospective effect", "உரிமையியல் பொறுப்புகளையும் வரிப் பொறுப்புகளையும் பின்னோக்கிய அமல் தேதியுடன் விதிக்க முடியாது",
    "No person shall be convicted of any offence except for violation of a law in force at the time of the commission of the act", "ஒரு செயல் செய்யப்பட்ட நேரத்தில் அமலில் உள்ள சட்டத்தை மீறியதைத் தவிர வேறு எதற்காகவும் எந்த நபரும் தண்டிக்கப்படக் கூடாது",
    "State cannot increase tax rates for past financial years", "கடந்த நிதியாண்டுகளுக்கான வரி விகிதங்களை அரசு உயர்த்த முடியாது",
    "Rules of criminal trial procedure cannot be altered during pending trials", "நிலுவையில் உள்ள விசாரணைகளின் போது குற்றவியல் விசாரணை நடைமுறை விதிகளை மாற்ற முடியாது",
    "B",
    "Article 20(1) contains two protections: 1. No person shall be convicted of an offence except for violation of a law in force at the time of the commission of the act (retrospective criminal conviction banned); 2. No person shall be subjected to a penalty greater than that prescribed by law at the time of offence.",
    "பிரிவு 20(1) கூறுவது: குற்றம் செய்யப்பட்ட நேரத்தில் அமலில் உள்ள சட்டத்தை மீறியதற்காக அன்றி வேறு எதற்காகவும் எந்த நபரும் தண்டிக்கப்படக் கூடாது, மேலும் குற்றம் செய்த நேரத்தில் விதிக்கப்பட்ட தண்டனையை விட அதிக தண்டனை விதிக்கப்படக் கூடாது.",
    "Incorrect. Civil liabilities and taxes CAN be imposed retrospectively.", "தவறு. உரிமையியல் மற்றும் வரிப் பொறுப்புகளைப் பின்னோக்கிய தேதியில் விதிக்க முடியும்.",
    "Correct. Article 20(1) prohibits retrospective criminal convictions and penalties.", "சரி. பிரிவு 20(1) பின்னோக்கிய குற்றவியல் தண்டனைகளைத் தடுக்கிறது.",
    "Incorrect. Tax rate changes can apply retrospectively.", "தவறு. வரி விகித மாற்றங்கள் பின்னோக்கிய தேதியில் பொருந்தலாம்.",
    "Incorrect. Procedural trial changes CAN apply to pending trials.", "தவறு. நடைமுறை மாற்றங்கள் நிலுவை விசாரணைகளுக்குப் பொருந்தலாம்.",
    "TNPSC Trap: Article 20(1) immunity applies ONLY to CRIMINAL offences and criminal penalties, NOT to civil liabilities, tax enactments, preventive detention, or trial procedures.",
    "TNPSC பொறி: பிரிவு 20(1) பாதுகாப்பு குற்றவியல் குற்றங்கள் மற்றும் தண்டனைகளுக்கு மட்டுமே பொருந்தும்; உரிமையியல், வரி, தடுப்புக் காவல் அல்லது விசாரணை நடைமுறைகளுக்குப் பொருந்தாது.",
    "Ex-Post Facto Law protection prevents punishing an act that was lawful when committed.",
    "பின்னோக்கிய சட்டம் ஒரு செயல் செய்யப்பட்ட போது அது சட்டப்பூர்வமானதாக இருந்தால் பின்னர் தண்டிக்கப்படுவதைத் தடுக்கிறது.",
    ["TNPSC Group 2 2019 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 20(1)", "Ex Post Facto"]
))

# FR_PYQ_043 (Hard | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_043", "Hard", "Direct MCQ",
    "In which landmark judgment did the Supreme Court overrule its narrow interpretation in A.K. Gopalan (1950) and hold that 'procedure established by law' under Article 21 must be just, fair, and reasonable?",
    "ஏ.கே. கோபாலன் வழக்கில் (1950) அளித்த குறுகிய விளக்கத்தை ரத்து செய்து, பிரிவு 21-ன் கீழ் 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை' என்பது நீதியான, நியாயமான மற்றும் ஏதுவான ஒன்றாக இருக்க வேண்டும் என உச்சநீதிமன்றம் எந்த வழக்கில் தீர்ப்பளித்தது?",
    "I.C. Golaknath v. State of Punjab (1967)", "ஐ.சி. கோலக்நாத் எதிராக பஞ்சாப் மாநிலம் (1967)",
    "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிராக கேரளா மாநிலம் (1973)",
    "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி எதிராக இந்திய யூனியன் (1978)",
    "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (1980)",
    "C",
    "In Maneka Gandhi v. Union of India (1978), the Supreme Court overruled A.K. Gopalan (1950) narrow view, holding that Article 21 is not merely a protection against arbitrary executive action, but also against arbitrary legislative action. The procedure depriving personal liberty must satisfy the test of 'Just, Fair and Reasonable' (procedural due process).",
    "மேனகா காந்தி வழக்கில் (1978) உச்சநீதிமன்றம் ஏ.கே. கோபாலன் (1950) தீர்ப்பை ரத்து செய்து, பிரிவு 21-ன் கீழ் தனிநபர் சுதந்திரத்தைப் பறிக்கும் நடைமுறை நீதியான, நியாயமானதாக இருக்க வேண்டும் எனத் தீர்ப்பளித்தது.",
    "Incorrect. Golaknath (1967) dealt with amendability of Fundamental Rights.", "தவறு. கோலக்நாத் (1967) அடிப்படை உரிமைகள் திருத்தம் பற்றியது.",
    "Incorrect. Kesavananda Bharati (1973) propounded Basic Structure Doctrine.", "தவறு. கேசவாநந்த பாரதி (1973) அடிப்படை அமைப்புக் கோட்பாட்டை உருவாக்கியது.",
    "Correct. Maneka Gandhi (1978) introduced procedural due process under Article 21.", "சரி. மேனகா காந்தி (1978) பிரிவு 21-ன் கீழ் நீதியான நடைமுறையை அறிமுகப்படுத்தியது.",
    "Incorrect. Minerva Mills (1980) dealt with FR-DPSP balance.", "தவறு. மினர்வா மில்ஸ் (1980) உரிமைகள்-நெறிமுறைகள் சமநிலை பற்றியது.",
    "TNPSC Trap: Golden Triangle of Fundamental Rights: Articles 14, 19, and 21 are mutually connected and inter-linked as established in Maneka Gandhi Case (1978).",
    "TNPSC பொறி: அடிப்படை உரிமைகளின் தங்க முக்கோணம்: பிரிவுகள் 14, 19, மற்றும் 21 ஆகியவை மேனகா காந்தி வழக்கில் (1978) நிறுவப்பட்டபடி ஒன்றுக்கொன்று தொடர்புடையவை.",
    "Maneka Gandhi judgment expanded Article 21 from mere protection of body to right to live with human dignity.",
    "மேனகா காந்தி தீர்ப்பு பிரிவு 21-ஐ வெறும் உடல் பாதுகாப்பிலிருந்து மனித கண்ணியத்துடன் வாழும் உரிமையாக விரிவுபடுத்தியது.",
    ["TNPSC Group 1 2020 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Maneka Gandhi Case", "Article 21"]
))

# FR_PYQ_044 (Medium | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_044", "Medium", "Direct MCQ",
    "Article 27 of the Constitution provides freedom from payment of taxes if the proceeds are specifically appropriated for what purpose?",
    "எந்த நோக்கத்திற்காக நிதி சிறப்பாக ஒதுக்கப்பட்டால் வரி செலுத்த வேண்டிய அவசியமில்லை என அரசியலமைப்பின் பிரிவு 27 சுதந்திரம் அளிக்கிறது?",
    "Construction of government schools and public hospitals", "அரசுப் பள்ளிகள் மற்றும் பொது மருத்துவமனைகள் கட்டுதல்",
    "Maintenance of historical national monuments and heritage sites", "வரலாற்றுச் சிறப்புமிக்க தேசிய நினைவிடங்கள் பராமரிப்பு",
    "Expenditure on armed forces welfare and defence funds", "ஆயுதப் படை நல நிதிகள் மீதான செலவினம்",
    "Promotion or maintenance of any particular religion or religious denomination", "குறிப்பிட்ட மதம் அல்லது மதப் பிரிவை பரப்புதல் அல்லது பராமரித்தல்",
    "D",
    "Article 27 states: 'No person shall be compelled to pay any taxes, the proceeds of which are specifically appropriated in payment of expenses for the promotion or maintenance of any particular religion or religious denomination.'",
    "பிரிவு 27 கூறுவது: 'குறிப்பிட்ட மதம் அல்லது மதப் பிரிவை பரப்புவதற்காக அல்லது பராமரிப்பதற்காக ஆகும் செலவுகளுக்காக எவரும் எந்தவொரு வரியையும் செலுத்துமாறு வற்புறுத்தப்படக் கூடாது.'",
    "Incorrect. Educational construction is a general secular purpose.", "தவறு. கல்வித்துறை கட்டுமானம் ஒரு மதச்சார்பற்ற பொது நோக்கமாகும்.",
    "Incorrect. Monument maintenance is a secular heritage purpose.", "தவறு. நினைவிட பராமரிப்பு மதச்சார்பற்ற பாரம்பரிய நோக்கமாகும்.",
    "Incorrect. Defence expenditure is a general public purpose.", "தவறு. பாதுகாப்புச் செலவினம் பொது நோக்கமாகும்.",
    "Correct. Article 27 prohibits levying taxes for promotion of any specific religion.", "சரி. பிரிவு 27 குறிப்பிட்ட மதத்தைப் பரப்ப வரி விதிப்பதைத் தடுக்கிறது.",
    "TNPSC Trap: Article 27 prohibits TAXES (general compulsory levy without direct service), but DOES NOT prohibit FEES (levied for specific services rendered to pilgrims, like sanitation and security).",
    "TNPSC பொறி: பிரிவு 27 வரிகளை (TAXES) மட்டுமே தடுக்கிறது, கட்டணங்களைத் (FEES) தடுக்காது (பக்தர்களுக்கு சுகாதாரப் பாதுகாப்பு வழங்க கட்டணம் வசூலிக்கலாம்).",
    "Article 27 ensures secular nature of state treasury; public money cannot be used to promote one religion.",
    "பிரிவு 27 அரசு கருவூலத்தின் மதச்சார்பற்ற தன்மையை உறுதி செய்கிறது; பொதுப் பணம் ஒரு மதத்தைப் பரப்பப் பயன்படக்கூடாது.",
    ["TNPSC Group 2A 2017 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 27", "Secular Treasury"]
))

# FR_PYQ_045 (Medium | Target Ans: A)
questions.append(make_pyq_q(
    "FR_PYQ_045", "Medium", "Direct MCQ",
    "The judicial writ of Mandamus CANNOT be issued against which of the following high constitutional office-holders for the performance of their official duties?",
    "பின்வரும் எந்த உயர் அரசியலமைப்புப் பதவி வகிப்பவர்களுக்கு எதிராக அவர்களின் அதிகாரப்பூர்வ கடமைகளைச் செய்யுமாறு மேண்டமஸ் பேராணையைப் பிறப்பிக்க முடியாது?",
    "President of India or State Governors", "இந்தியக் குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்கள்",
    "Collector of a Revenue District", "வருவாய் மாவட்ட ஆட்சியர்",
    "Chairman of a State Public Service Commission", "மாநில அரசுப் பணியாளர் தேர்வாணையத் தலைவர்",
    "Municipal Corporation Commissioner", "மாநகராட்சி ஆணையர்",
    "A",
    "Under Article 361 of the Constitution and judicial precedents, the writ of Mandamus does NOT lie against the President of India or State Governors for the performance of the duties of their office.",
    "பிரிவு 361 மற்றும் நீதிமன்ற முன்மாதிரிகளின்படி, இந்தியக் குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்களுக்கு எதிராகத் தங்களது அதிகாரப்பூர்வ கடமைகளைச் செய்யுமாறு மேண்டமஸ் பிறப்பிக்க முடியாது.",
    "Correct. President and Governors are immune from Mandamus under Article 361.", "சரி. பிரிவு 361-ன் கீழ் குடியரசுத் தலைவர் மற்றும் ஆளுநர்களுக்கு மேண்டமஸ் விலக்களிக்கப்பட்டுள்ளது.",
    "Incorrect. District Collectors are public officers subject to Mandamus.", "தவறு. மாவட்ட ஆட்சியர்களுக்கு எதிராக மேண்டமஸ் பிறப்பிக்கப்படலாம்.",
    "Incorrect. SPSC Chairman is a statutory/constitutional public officer subject to Mandamus.", "தவறு. தேர்வாணையத் தலைவருக்கு எதிராக மேண்டமஸ் பொருந்தும்.",
    "Incorrect. Municipal Commissioner is a public officer subject to Mandamus.", "தவறு. மாநகராட்சி ஆணையருக்கு எதிராக மேண்டமஸ் பொருந்தும்.",
    "TNPSC Trap: Mandamus Exceptions list: 1. President / State Governors (Art 361), 2. Private individuals, 3. Discretionary duties, 4. Contractual duties, 5. Chief Justice of HC/SC acting in judicial capacity.",
    "TNPSC பொறி: மேண்டமஸ் விலக்குகள் பட்டியல்: 1. குடியரசுத் தலைவர் / ஆளுநர்கள் (பிரிவு 361), 2. தனியார் நபர்கள், 3. விருப்பக் கடமைகள், 4. ஒப்பந்தப் பொறுப்புகள், 5. நீதித்துறை நீதிபதிகள்.",
    "Mandamus enforces non-discretionary mandatory public duties on executive officers.",
    "மேண்டமஸ் நிர்வாக அதிகாரிகளுக்கு சட்டத்தால் விதிக்கப்பட்ட கட்டாயக் கடமைகளை அமல்படுத்துகிறது.",
    ["TNPSC Group 1 2017 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Mandamus Exceptions", "Article 361"]
))

# FR_PYQ_046 (Medium | Target Ans: B)
questions.append(make_pyq_q(
    "FR_PYQ_046", "Medium", "Direct MCQ",
    "Under Article 35 of the Constitution, the power to make laws prescribing punishment for offences under Part III (such as Article 17 Untouchability and Article 23 Forced Labour) rests EXCLUSIVELY with:",
    "பிரிவு 35-ன் கீழ், பகுதி III-ன் கீழ் உள்ள குற்றங்களுக்கு (பிரிவு 17 தீண்டாமை, பிரிவு 23 கட்டாய உழைப்பு) தண்டனை வழங்கும் சட்டங்களை இயற்றும் அதிகாரம் யாருக்கு மட்டுமே உண்டு?",
    "State Legislatures", "மாநில சட்டமன்றங்கள்",
    "Parliament of India", "இந்திய நாடாளுமன்றம்",
    "Supreme Court of India", "இந்திய உச்சநீதிமன்றம்",
    "Union Home Ministry", "மத்திய உள்துறை அமைச்சகம்",
    "B",
    "Article 35(a)(ii) explicitly lays down that Parliament ALONE (and not State Legislatures) shall have power to make laws prescribing punishment for acts declared as offences under Part III (like Art 17 & Art 23), ensuring countrywide uniformity.",
    "பிரிவு 35(a)(ii) பகுதி III-ன் கீழ் குற்றங்களாக அறிவிக்கப்பட்ட செயல்களுக்கு (பிரிவு 17 & 23) தண்டனை வழங்கும் சட்டங்களை நாடாளுமன்றம் மட்டுமே இயற்ற முடியும் எனக் தெளிவுபடுத்துகிறது.",
    "Incorrect. State Legislatures have NO power to make laws under Article 35 for Part III offences.", "தவறு. மாநில சட்டமன்றங்களுக்கு பகுதி III குற்றங்களுக்கு சட்டமியற்றும் அதிகாரமில்லை.",
    "Correct. Parliament of India alone has exclusive power under Article 35.", "சரி. இந்திய நாடாளுமன்றத்திற்கு மட்டுமே பிரிவு 35-ன் கீழ் தனி அதிகாரம் உண்டு.",
    "Incorrect. Supreme Court interprets laws, does not enact criminal penal statutes.", "தவறு. உச்சநீதிமன்றம் சட்டங்களை விளக்குகிறது, குற்றவியல் சட்டங்களை இயற்றுவதில்லை.",
    "Incorrect. Home Ministry is executive branch, not legislative body.", "தவறு. உள்துறை அமைச்சகம் நிர்வாகத் துறையாகும்.",
    "TNPSC Trap: Parliament enacted Protection of Civil Rights Act 1955 (Art 17) and Bonded Labour System (Abolition) Act 1976 (Art 23) using its exclusive legislative power under Article 35.",
    "TNPSC பொறி: நாடாளுமன்றம் பிரிவு 35-ன் கீழ் உள்ள தனி அதிகாரத்தைப் பயன்படுத்தி உரிமைகள் பாதுகாப்புச் சட்டம் 1955 மற்றும் கொத்தடிமை ஒழிப்புச் சட்டம் 1976 ஆகியவற்றை இயற்றியது.",
    "Article 35 guarantees uniformity throughout India in respect of Fundamental Rights laws and penalties.",
    "பிரிவு 35 அடிப்படை உரிமைகள் சட்டங்கள் மற்றும் தண்டனைகளில் இந்தியா முழுவதும் சீரான தன்மையை உறுதி செய்கிறது.",
    ["TNPSC Group 2 2018 PYQ", "M. Laxmikanth - Indian Polity"], "Understand", 45, ["Polity", "Fundamental Rights", "Article 35", "Parliament Power"]
))

# FR_PYQ_047 (Hard | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_047", "Hard", "Direct MCQ",
    "Which of the following bodies has been declared by the Supreme Court to be an instrumentality/agency of the State falling within the definition of 'State' under Article 12?",
    "பின்வரும் அமைப்புகளில் எது பிரிவு 12-ன் கீழ் 'அரசு' என்ற வரையறைக்குள் வரும் அமைப்பாக உச்சநீதிமன்றத்தால் அறிவிக்கப்பட்டுள்ளது?",
    "BCCI (Board of Control for Cricket in India)", "BCCI (இந்திய கிரிக்கெட் கட்டுப்பாட்டு வாரியம்)",
    "NCERT (National Council of Educational Research and Training)", "NCERT (தேசிய கல்வியியல் ஆராய்ச்சி மற்றும் பயிற்சிக் குழு)",
    "LIC, ONGC, and SAIL", "LIC, ONGC, மற்றும் SAIL",
    "Private Unaided Schools", "தனியார் நிதியுதவி பெறாப் பள்ளிகள்",
    "C",
    "Statutory corporations like Life Insurance Corporation (LIC), Oil and Natural Gas Corporation (ONGC), and Steel Authority of India Limited (SAIL) have been declared 'State' under Article 12 (RD Shetty Case 1979). BCCI and NCERT have been held NOT to be 'State' under Article 12 by SC.",
    "LIC, ONGC, SAIL போன்ற சட்டப்பூர்வக் கழகங்கள் பிரிவு 12-ன் கீழ் 'அரசு' என உச்சநீதிமன்றத்தால் அறிவிக்கப்பட்டுள்ளன. BCCI மற்றும் NCERT ஆகியவை பிரிவு 12 'அரசு' அல்ல எனத் தீர்ப்பளிக்கப்பட்டுள்ளது.",
    "Incorrect. BCCI is held NOT to be State under Article 12 (Zee Telefilms Case 2005).", "தவறு. BCCI பிரிவு 12-ன் கீழ் அரசு அல்ல எனக் கருதப்படுகிறது (ஜீ டெலிஃபிலிம்ஸ் வழக்கு 2005).",
    "Incorrect. NCERT is held NOT to be State under Article 12 (Chander Mohan Khanna Case 1991).", "தவறு. NCERT பிரிவு 12-ன் கீழ் அரசு அல்ல எனக் கருதப்படுகிறது (சந்தர் மோகன் கன்னா வழக்கு 1991).",
    "Correct. LIC, ONGC, and SAIL are statutory instrumentalities falling under Article 12.", "சரி. LIC, ONGC, SAIL ஆகியவை பிரிவு 12-ன் கீழ் வரும் அமைப்புகளாகும்.",
    "Incorrect. Private unaided schools are not instrumentalities under Art 12.", "தவறு. தனியார் நிதியுதவி பெறாப் பள்ளிகள் பிரிவு 12-ன் கீழ் அரசு அல்ல.",
    "TNPSC Trap: Test for 'Other Authorities' under Article 12 (Ajay Hasia Case 1981): 1. Entire share capital held by Govt, 2. Deep & pervasive State control, 3. Monopoly status conferred by State, 4. Public functions performed.",
    "TNPSC பொறி: பிரிவு 12-ன் கீழ் அமைப்புகளுக்கான சோதனைகள் (அஜய் ஹாசியா வழக்கு 1981): 1. அரசின் முழுப் பங்கு மூலதனம், 2. ஆழமான அரசு கட்டுப்பாடு, 3. ஏகபோக அந்தஸ்து, 4. பொதுப் பணிகள்.",
    "Article 12 expanded definition ensures citizens can enforce Part III rights against statutory corporations.",
    "பிரிவு 12-ன் பரந்த வரையறை குடிமக்கள் சட்டப்பூர்வக் கழகங்களுக்கு எதிராக பகுதி III உரிமைகளை அமல்படுத்துவதை உறுதி செய்கிறது.",
    ["TNPSC Group 1 2022 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Article 12", "Instrumentality of State"]
))

# FR_PYQ_048 (Hard | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_048", "Hard", "Direct MCQ",
    "In L. Chandra Kumar v. Union of India (1997), a 7-judge bench of the Supreme Court declared that the Judicial Review jurisdiction of High Courts (Article 226) and Supreme Court (Article 32) is an integral feature of:",
    "எல். சந்திர குமார் எதிராக இந்திய யூனியன் (1997) வழக்கில், உச்சநீதிமன்றத்தின் 7 நீதிபதிகள் அமர்வு உயர்நீதிமன்றங்கள் (பிரிவு 226) மற்றும் உச்சநீதிமன்றத்தின் (பிரிவு 32) நீதித்துறை மறுஆய்வு அதிகார வரம்பு எதன் ஒரு ஒருங்கிணைந்த அம்சம் என அறிவித்தது?",
    "Directive Principles of State Policy", "அரசு வழிகாட்டு நெறிமுறைகள்",
    "Parliamentary Supremacy over Judiciary", "நீதித்துறை மீதான நாடாளுமன்ற மேலாதிக்கம்",
    "State Autonomy and Federalism", "மாநில தன்னாட்சி மற்றும் கூட்டாட்சி",
    "Basic Structure of the Constitution", "அரசியலமைப்பின் அடிப்படை அமைப்பு (Basic Structure)",
    "D",
    "In L. Chandra Kumar v. Union of India (1997), the Supreme Court struck down clauses of Articles 323A and 323B which excluded High Court jurisdiction under Article 226 over Tribunals, holding that Judicial Review under Articles 32 and 226 is an inviolable Basic Structure feature.",
    "எல். சந்திர குமார் வழக்கில் (1997) உச்சநீதிமன்றம் தீர்ப்பாயங்கள் மீதான உயர்நீதிமன்ற அதிகார வரம்பை நீக்கிய பிரிவுகளை ரத்து செய்து, பிரிவுகள் 32 மற்றும் 226-ன் கீழ் நீதித்துறை மறுஆய்வு என்பது அடிப்படை அமைப்பின் அத்தியாவசிய அம்சம் எனத் தீர்ப்பளித்தது.",
    "Incorrect. Judicial review is not part of DPSPs.", "தவறு. நீதித்துறை மறுஆய்வு அரசு நெறிமுறைகளின் பகுதியல்ல.",
    "Incorrect. Indian Judiciary is independent, not subordinate to Parliament.", "தவறு. இந்திய நீதித்துறை சுதந்திரமானது, நாடாளுமன்றத்திற்கு உட்பட்டதல்ல.",
    "Incorrect. State autonomy is federalism, distinct from judicial review.", "தவறு. மாநில தன்னாட்சி என்பது கூட்டாட்சி தத்துவமாகும்.",
    "Correct. Judicial review under Arts 32 & 226 is an inviolable Basic Structure feature.", "சரி. பிரிவுகள் 32 & 226-ன் கீழ் நீதித்துறை மறுஆய்வு என்பது அடிப்படை அமைப்பின் அம்சமாகும்.",
    "TNPSC Trap: Post-L. Chandra Kumar (1997), decisions of Administrative Tribunals (like CAT) MUST be challenged before a Division Bench of the High Court FIRST, before going to the Supreme Court.",
    "TNPSC பொறி: எல். சந்திர குமார் (1997) தீர்ப்பிற்குப் பின், நிர்வாகத் தீர்ப்பாயங்களின் உத்தரவுகளை உச்சநீதிமன்றம் செல்லும் முன் முதலில் உயர்நீதிமன்ற அமர்வின் முன் மட்டுமே மேல்முறையீடு செய்ய முடியும்.",
    "L. Chandra Kumar (1997) restored the writ jurisdiction of High Courts over statutory and administrative tribunals.",
    "எல். சந்திர குமார் (1997) தீர்ப்பாயங்கள் மீது உயர்நீதிமன்றங்களின் பேராணை அதிகார வரம்பை மீண்டும் மீட்டெடுத்தது.",
    ["TNPSC Group 1 2021 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "L. Chandra Kumar Case", "Judicial Review"]
))

# FR_PYQ_049 (Hard | Target Ans: C)
questions.append(make_pyq_q(
    "FR_PYQ_049", "Hard", "Direct MCQ",
    "In State of Madras v. Champakam Dorairajan (1951), the Supreme Court laid down which relationship between Fundamental Rights (Part III) and Directive Principles (Part IV)?",
    "மதராஸ் மாநிலம் எதிராக சண்பகம் துரைராஜன் (1951) வழக்கில், அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு நெறிமுறைகள் (பகுதி IV) இடையே என்ன தொடர்பை உச்சநீதிமன்றம் வகுத்தது?",
    "Directive Principles shall override Fundamental Rights in case of conflict", "முரண்பாடு ஏற்படும் போது அரசு நெறிமுறைகளே அடிப்படை உரிமைகளை விட மேலோங்கும்",
    "Both are equal and conflicts must be resolved by Parliament by passing ordinary law", "இரண்டும் சமமானவை மற்றும் முரண்பாடுகளை நாடாளுமன்றம் சாதாரண சட்டம் மூலம் தீர்க்க வேண்டும்",
    "Fundamental Rights shall prevail over Directive Principles (DPSPs must run as subsidiary to Part III)", "அடிப்படை உரிமைகளே அரசு நெறிமுறைகளை விட மேலோங்கும் (நெறிமுறைகள் பகுதி III-க்கு துணையாகவே செயல்பட வேண்டும்)",
    "Fundamental Duties shall override Fundamental Rights", "அடிப்படை கடமைகளே அடிப்படை உரிமைகளை விட மேலோங்கும்",
    "C",
    "In State of Madras v. Champakam Dorairajan (1951), the Supreme Court ruled that in case of any conflict between Fundamental Rights and Directive Principles, Fundamental Rights prevail. DPSPs have to conform to and run as subsidiary to Fundamental Rights.",
    "சண்பகம் துரைராஜன் வழக்கில் (1951) அடிப்படை உரிமைகள் மற்றும் அரசு நெறிமுறைகள் இடையே முரண்பாடு ஏற்படும் போது அடிப்படை உரிமைகளே மேலோங்கும் என்றும், நெறிமுறைகள் பகுதி III-க்கு துணையாகச் செயல்பட வேண்டும் என்றும் உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    "Incorrect. DPSPs do not override FRs under Champakam Dorairajan ruling.", "தவறு. சண்பகம் துரைராஜன் தீர்ப்பில் நெறிமுறைகள் உரிமைகளை மேலோங்கவில்லை.",
    "Incorrect. Court gave legal primacy to Part III, not equality.", "தவறு. நீதிமன்றம் பகுதி III-க்கு சட்டப்பூர்வ மேலாதிக்கம் அளித்தது.",
    "Correct. Champakam Dorairajan (1951) held FRs prevail over DPSPs.", "சரி. சண்பகம் துரைராஜன் (1951) அடிப்படை உரிமைகளே மேலோங்கும் எனக் கூறியது.",
    "Incorrect. Fundamental Duties were not in existence in 1951.", "தவறு. 1951-ல் அடிப்படை கடமைகள் இருக்கவில்லை.",
    "TNPSC Trap: Shift over time: Champakam Dorairajan (1951) = FR Primacy. 25th CAA 1971 = Added Art 31C making DPSPs 39(b) & (c) superior to Arts 14 & 19. Minerva Mills (1980) = Balance between FRs and DPSPs is Basic Structure.",
    "TNPSC பொறி: கால மாற்றத்தில் வளர்ச்சி: சண்பகம் துரைராஜன் (1951) = அடிப்படை உரிமை மேலாதிக்கம். 25-வது திருத்தம் 1971 = பிரிவு 31C மூலம் 39(b) & (c) நெறிமுறைகளுக்கு முன்னுரிமை. மினர்வா மில்ஸ் (1980) = சமநிலையே அடிப்படை அமைப்பு.",
    "Champakam Dorairajan case led directly to the 1st Constitutional Amendment Act 1951 inserting Article 15(4).",
    "சண்பகம் துரைராஜன் வழக்கு நேரடியாக பிரிவு 15(4)-ஐச் சேர்த்த 1-வது திருத்தச் சட்டம் 1951-க்கு வழிவகுத்தது.",
    ["TNPSC Group 2 2015 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Champakam Dorairajan", "FR vs DPSP"]
))

# FR_PYQ_050 (Hard | Target Ans: D)
questions.append(make_pyq_q(
    "FR_PYQ_050", "Hard", "Direct MCQ",
    "Article 31C, inserted by the 25th Constitutional Amendment Act 1971, protected laws giving effect to Directive Principles in Article 39(b) and (c) from being challenged for violating which Fundamental Rights?",
    "25-வது அரசியலமைப்பு திருத்தச் சட்டம் 1971 மூலம் சேர்க்கப்பட்ட பிரிவு 31C, பிரிவு 39(b) மற்றும் (c)-ல் உள்ள அரசு நெறிமுறைகளை அமல்படுத்தும் சட்டங்களை எந்த அடிப்படை உரிமைகளை மீறுவதாக சவால் செய்வதிலிருந்து பாதுகாத்தது?",
    "Articles 25 and 26", "பிரிவுகள் 25 மற்றும் 26",
    "Articles 29 and 30", "பிரிவுகள் 29 மற்றும் 30",
    "Articles 21 and 22", "பிரிவுகள் 21 மற்றும் 22",
    "Articles 14 and 19", "பிரிவுகள் 14 மற்றும் 19",
    "D",
    "Article 31C (inserted by 25th CAA 1971) laid down that no law giving effect to Directive Principles under Article 39(b) [distribution of material resources] and Article 39(c) [prevention of concentration of wealth] shall be deemed void on the ground that it is inconsistent with Articles 14 and 19.",
    "25-வது திருத்தம் 1971 மூலம் சேர்க்கப்பட்ட பிரிவு 31C, பிரிவு 39(b) (பொருள் வளங்கள் விநியோகம்) மற்றும் 39(c) (செல்வக் குவிப்புத் தடுப்பு) நெறிமுறைகளை அமல்படுத்தும் சட்டங்களை பிரிவுகள் 14 மற்றும் 19-ஐ மீறுகின்றன என ரத்து செய்ய முடியாது எனக் கூறியது.",
    "Incorrect. Articles 25 & 26 deal with religion, not protected by Art 31C.", "தவறு. பிரிவுகள் 25 & 26 மதச் சுதந்திரம் பற்றியவை.",
    "Incorrect. Articles 29 & 30 deal with minority rights.", "தவறு. பிரிவுகள் 29 & 30 சிறுபான்மையினர் உரிமைகள் பற்றியவை.",
    "Incorrect. Articles 21 & 22 deal with life and detention.", "தவறு. பிரிவுகள் 21 & 22 வாழ்வுரிமை மற்றும் கைது பற்றியவை.",
    "Correct. Article 31C protects Article 39(b) & (c) laws against Articles 14 and 19.", "சரி. பிரிவு 31C பிரிவு 39(b) & (c) சட்டங்களை பிரிவுகள் 14 மற்றும் 19-க்கு எதிராகப் பாதுகாக்கிறது.",
    "TNPSC Trap: Famous legal maxim regarding Article 31C: 'Where Article 31C comes in, Article 14 goes out.' Supreme Court upheld 1st clause of Art 31C in Kesavananda Bharati case (1973).",
    "TNPSC பொறி: பிரிவு 31C பற்றிய புகழ்பெற்ற சட்டப் பழமொழி: 'பிரிவு 31C நுழையும் போது, பிரிவு 14 வெளியேறுகிறது.' கேசவாநந்த பாரதி வழக்கில் (1973) பிரிவு 31C-ன் முதல் பகுதி உறுதி செய்யப்பட்டது.",
    "Article 31C establishes that implementing socio-economic equality DPSPs 39(b) & (c) takes precedence over individual Articles 14 & 19.",
    "பிரிவு 31C சமூக-பொருளாதார சமத்துவ நெறிமுறைகள் 39(b) & (c)-ஐ அமல்படுத்துவது தனிநபர் பிரிவுகள் 14 & 19-ஐ விட முன்னுரிமை பெறுகிறது என்பதை நிறுவுகிறது.",
    ["TNPSC Group 1 2022 PYQ", "M. Laxmikanth - Indian Polity"], "Analyze", 60, ["Polity", "Fundamental Rights", "Article 31C", "25th CAA"]
))

# Save full 50 questions dataset to BOTH file paths
print(f"Total PYQ Practice questions compiled: {len(questions)}")
assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"

with open(target_path_1, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print(f"✅ Successfully wrote 50 PYQ MCQs to {target_path_1}")

with open(target_path_2, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print(f"✅ Successfully wrote 50 PYQ MCQs to {target_path_2}")
