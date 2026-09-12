# -*- coding: utf-8 -*-
"""
Supreme Court Grand Test Block 1 (Questions 1 to 25)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def mk_q(idx, diff, q_type, q_en, q_ta, opts_en, opts_ta, correct_key, exp_en, exp_ta, trap_en, trap_ta, tip_en, tip_ta, fact_en, fact_ta):
    return {
        "id": f"POLITY_SC_GT_{idx:03d}",
        "subject": "Polity",
        "topic": "Supreme Court of India",
        "difficulty": diff,
        "question_type": q_type,
        "question_en": q_en,
        "question_ta": q_ta,
        "opts_en": opts_en,
        "opts_ta": opts_ta,
        "correct_key": correct_key,
        "exp_en": exp_en,
        "exp_ta": exp_ta,
        "trap_en": trap_en,
        "trap_ta": trap_ta,
        "tip_en": tip_en,
        "tip_ta": tip_ta,
        "fact_en": fact_en,
        "fact_ta": fact_ta
    }

def get_block1():
    b1 = []

    # Q1
    b1.append(mk_q(1, "Medium", "Statement",
        "Consider the following statements regarding the appointment of judges to the Supreme Court of India:\n1. The Chief Justice of India is appointed by the President after consultation with such judges of the Supreme Court and High Courts as the President deems necessary.\n2. In the Third Judges Case (1998), the Supreme Court held that the recommendation of CJI without consulting a collegium of four senior-most judges of the SC is not binding on the Government.\n3. The seniority rule for appointing the senior-most judge of the SC as CJI has been strictly followed without exception since 1950.\nWhich of the statements given above is/are correct?",
        "இந்திய உச்ச நீதிமன்ற நீதிபதிகள் நியமனம் குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. குடியரசுத் தலைவரால் தேவையானதாகக் கருதப்படும் உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகளுடன் ஆலோசித்த பிறகே இந்திய தலைமை நீதிபதி நியமிக்கப்படுகிறார்.\n2. மூன்றாவது நீதிபதிகள் வழக்கில் (1998), உச்ச நீதிமன்றத்தின் நான்கு மூத்த நீதிபதிகள் கொண்ட குழுவைக் கலந்தாலோசிக்காமல் தலைமை நீதிபதி அளிக்கும் பரிந்துரை அரசைக்கட்டுப்படுத்தாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n3. 1950 முதல் எந்தவித விதிவிலக்கும் இன்றி உச்ச நீதிமன்றத்தின் மிக மூத்த நீதிபதியை தலைமை நீதிபதியாக நியமிக்கும் மூப்பு விதி கண்டிப்பாக பின்பற்றப்பட்டு வருகிறது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
        {"A": "1 and 2 only", "B": "2 and 3 only", "C": "1 and 3 only", "D": "1, 2 and 3"},
        {"A": "1 மற்றும் 2 மட்டும்", "B": "2 மற்றும் 3 மட்டும்", "C": "1 மற்றும் 3 மட்டும்", "D": "1, 2 மற்றும் 3"},
        "A",
        "Statements 1 and 2 are correct. Under Article 124(2), judges are appointed by the President. In the 3rd Judges Case (1998), CJI must consult a collegium of 4 senior-most SC judges. Statement 3 is incorrect because the seniority rule was violated twice: A.N. Ray (1973) superseding 3 senior judges and M.U. Beg (1977) superseding H.R. Khanna.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. சரத்து 124(2)-ன் படி நீதிபதிகளை குடியரசுத் தலைவர் நியமிக்கிறார். 3வது நீதிபதிகள் வழக்கில் (1998) 4 மூத்த நீதிபதிகள் கொண்ட கொலீஜியத்தைக் கலந்தாலோசிக்க வேண்டும் என தீர்ப்பளிக்கப்பட்டது. கூற்று 3 தவறானது, ஏனெனில் 1973-ல் ஏ.என். ரே மற்றும் 1977-ல் எம்.யு. பேக் நியமனத்தின் போது மூப்பு விதி மீறப்பட்டது.",
        "Candidates often assume the seniority rule was never broken. It was broken in 1973 (A.N. Ray) and 1977 (M.U. Beg).",
        "மூப்பு விதி ஒருபோதும் மீறப்படவில்லை என்று தேர்வர்கள் தவறாகக் கருதுகின்றனர். அது 1973 மற்றும் 1977 இல் மீறப்பட்டது.",
        "Remember: 2nd Judges Case (1993) established Collegium (CJI + 2). 3rd Judges Case (1998) expanded it to CJI + 4.",
        "நினைவில் கொள்க: 2வது நீதிபதிகள் வழக்கு (1993) கொலீஜியத்தை (CJI + 2) உருவாக்கியது. 3வது நீதிபதிகள் வழக்கு (1998) அதை (CJI + 4) என விரிவுபடுத்தியது.",
        "Article 124(2) empowers the President to appoint judges of the Supreme Court.",
        "சரத்து 124(2) உச்ச நீதிமன்ற நீதிபதிகளை நியமிக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது."))

    # Q2
    b1.append(mk_q(2, "Easy", "Direct",
        "Under Article 130 of the Constitution, who is authorized to appoint other place or places as the seat of the Supreme Court of India?",
        "அரசியலமைப்பின் சரத்து 130 இன் படி, உச்ச நீதிமன்றத்தின் அமர்வை டெல்லி தவிர பிற இடங்களுக்கு மாற்றும் அதிகாரம் யாருக்கு உள்ளது?",
        {"A": "The Parliament by enacting a law", "B": "The Chief Justice of India with the approval of the President", "C": "The President of India on the advice of the Union Cabinet", "D": "The Law Commission of India"},
        {"A": "சட்டம் இயற்றுவதன் மூலம் நாடாளுமன்றத்திற்கு", "B": "குடியரசுத் தலைவரின் ஒப்புதலுடன் இந்திய தலைமை நீதிபதிக்கு", "C": "மத்திய அமைச்சரவையின் ஆலோசனையின் பேரில் குடியரசுத் தலைவருக்கு", "D": "இந்திய சட்ட ஆணையத்திற்கு"},
        "B",
        "Article 130 declares Delhi as the seat of the SC. However, it authorizes the Chief Justice of India to appoint any other place or places as seat of SC, but only with the previous approval of the President.",
        "சரத்து 130 டெல்லியை உச்ச நீதிமன்றத்தின் அமர்வாக அறிவிக்கிறது. இருப்பினும், குடியரசுத் தலைவரின் முன் ஒப்புதலுடன் இந்திய தலைமை நீதிபதி பிற இடங்களையும் அமர்வாக நியமிக்க அதிகாரம் பெற்றுள்ளார்.",
        "Candidates often mistakenly select 'Parliament' because Parliament changes judge numbers and salaries.",
        "நீதிபதிகளின் எண்ணிக்கை மற்றும் சம்பளத்தை நாடாளுமன்றம் மாற்றுவதால், தேர்வர்கள் இதையும் 'நாடாளுமன்றம்' எனத் தவறாகத் தேர்ந்தெடுக்கின்றனர்.",
        "Seat of SC = Article 130 = CJI + Approval of President.",
        "உச்ச நீதிமன்றத்தின் அமர்வு = சரத்து 130 = CJI + குடியரசுத் தலைவரின் ஒப்புதல்.",
        "This provision is discretionary for the CJI; no court can compel the CJI to issue directions to create a bench elsewhere.",
        "இது CJI-ன் விருப்ப அதிகாரமாகும்; வேறு இடத்தில் கிளையை உருவாக்க CJI-க்கு நீதிமன்றங்கள் உத்தரவிட முடியாது."))

    # Q3
    b1.append(mk_q(3, "Hard", "Reasoning",
        "Assertion (A): A dispute involving a private citizen and a State Government cannot be entertained by the Supreme Court under its Original Jurisdiction under Article 131.\nReason (R): Article 131 exclusively deals with federal disputes arising between the Centre and one or more States, or between two or more States.",
        "கூற்று (A): அரசியலமைப்புச் சரத்து 131-ன் கீழ் உச்ச நீதிமன்றத்தின் மூல அதிகார வரம்பில் ஒரு தனிநபருக்கும் மாநில அரசுக்கும் இடையிலான தகராறை விசாரிக்க முடியாது.\nகாரணம் (R): சரத்து 131 என்பது மத்திய அரசுக்கும் ஒன்று அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கும் இடையே அல்லது இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு இடையிலான கூட்டாட்சி சர்ச்சைகளை மட்டுமே பிரத்தியேகமாகக் கையாள்கிறது.",
        {"A": "Both (A) and (R) are true and (R) is the correct explanation of (A)", "B": "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "C": "(A) is true but (R) is false", "D": "(A) is false but (R) is true"},
        {"A": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்", "B": "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமல்ல", "C": "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு", "D": "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி"},
        "A",
        "Both (A) and (R) are true and (R) explains (A). Under Article 131, the Supreme Court has exclusive original jurisdiction over intergovernmental federal disputes. A suit brought by a private citizen against a state or the Union cannot be brought under Article 131.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும். சரத்து 131-ன் கீழ் கூட்டாட்சி அரசாங்கங்களுக்கு இடையேயான வழக்குகளை மட்டுமே உச்ச நீதிமன்றம் மூல அதிகார வரம்பில் விசாரணை செய்ய முடியும். தனிநபர் தொடுக்கும் வழக்கு சரத்து 131-ன் கீழ் வராது.",
        "Do not confuse Article 32 (Writ jurisdiction accessible to private citizens) with Article 131 (Exclusive Federal Original Jurisdiction between Governments).",
        "தனிநபர்கள் அணுகக்கூடிய சரத்து 32-ஐ, அரசாங்கங்களுக்கு இடையிலான சரத்து 131 மூல அதிகார வரம்புடன் குழப்பிக் கொள்ள வேண்டாம்.",
        "Article 131 requires a dispute involving a legal right, not a political question.",
        "சரத்து 131 சட்டபூர்வ உரிமை சார்ந்த தகராறை மட்டுமே கோருகிறது, அரசியல் கேள்வியை அல்ல.",
        "Pre-constitution treaties and inter-state river water disputes (Art 262) are explicitly excluded from Article 131 jurisdiction.",
        "அரசியலமைப்புக்கு முந்தைய உடன்படிக்கைகள் மற்றும் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் (சரத்து 262) சரத்து 131-ல் இருந்து விலக்கப் பெற்றுள்ளன."))

    # Q4
    b1.append(mk_q(4, "Medium", "Match",
        "Match List-I (Constitutional Article) with List-II (Provision) and select the correct answer using the code given below:\n\nList-I:\na) Article 124\nb) Article 129\nc) Article 131\nd) Article 143\n\nList-II:\n1. Advisory Jurisdiction of Supreme Court\n2. Establishment and Composition of Supreme Court\n3. Court of Record and Power to Punish for Contempt\n4. Original Jurisdiction in Federal Disputes",
        "பட்டியல்-I ஐ (அரசியலமைப்புச் சரத்து) பட்டியல்-II உடன் (வகைமுறை) பொருத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல்-I:\na) சரத்து 124\nb) சரத்து 129\nc) சரத்து 131\nd) சரத்து 143\n\nபட்டியல்-II:\n1. உச்ச நீதிமன்றத்தின் ஆலோசனை அதிகார வரம்பு\n2. உச்ச நீதிமன்றத்தின் உருவாக்கம் மற்றும் அமைவு\n3. ஆவண நீதிமன்றம் மற்றும் நீதிமன்ற அவமதிப்புக்குத் தண்டிக்கும் அதிகாரம்\n4. கூட்டாட்சி சர்ச்சைகளில் மூல அதிகார வரம்பு",
        {"A": "a-2, b-3, c-4, d-1", "B": "a-3, b-2, c-1, d-4", "C": "a-2, b-4, c-3, d-1", "D": "a-1, b-3, c-4, d-2"},
        {"A": "a-2, b-3, c-4, d-1", "B": "a-3, b-2, c-1, d-4", "C": "a-2, b-4, c-3, d-1", "D": "a-1, b-3, c-4, d-2"},
        "A",
        "Correct matching:\nArticle 124 -> Establishment & Composition of SC (2)\nArticle 129 -> Court of Record & Contempt (3)\nArticle 131 -> Original Jurisdiction in Federal Disputes (4)\nArticle 143 -> Advisory Jurisdiction (1)",
        "சரியான பொருத்தம்:\nசரத்து 124 -> உச்ச நீதிமன்ற உருவாக்கம் மற்றும் அமைவு (2)\nசரத்து 129 -> ஆவண நீதிமன்றம் மற்றும் அவமதிப்புத் தண்டனை (3)\nசரத்து 131 -> கூட்டாட்சி சர்ச்சைகளில் மூல அதிகார வரம்பு (4)\nசரத்து 143 -> ஆலோசனை அதிகார வரம்பு (1)",
        "Article 129 (Court of record) and Article 141 (Binding law) are often confused by candidates.",
        "சரத்து 129 (ஆவண நீதிமன்றம்) மற்றும் சரத்து 141 (கட்டுப்படுத்தும் சட்டம்) ஆகியவற்றை தேர்வர்கள் அடிக்கடி குழப்பிக் கொள்கிறார்கள்.",
        "Memorize core anchors: Art 124 = Setup, Art 129 = Record, Art 131 = Federal, Art 143 = Advisory.",
        "முக்கிய சரத்துகளை நினைவில் கொள்க: 124 = அமைப்பு, 129 = ஆவணம், 131 = கூட்டாட்சி, 143 = ஆலோசனை.",
        "Articles 124 to 147 in Part V of the Constitution deal with the Supreme Court.",
        "பகுதி V-ல் உள்ள சரத்துகள் 124 முதல் 147 வரை உச்ச நீதிமன்றம் பற்றி கூறுகின்றன."))

    # Q5
    b1.append(mk_q(5, "Hard", "Chronology",
        "Arrange the following judicial decisions and developments regarding Judicial Appointments in chronological order:\n1. Second Judges Case (Supreme Court Advocates-on-Record Association v. Union of India)\n2. First Judges Case (S.P. Gupta v. Union of India)\n3. Fourth Judges Case (NJAC Act declared unconstitutional)\n4. Third Judges Case (Presidential Reference on Collegium expansion)",
        "நீதிபதிகள் நியமனம் தொடர்பான பின்வரும் நீதித்துறை தீர்ப்புகள் மற்றும் நிகழ்வுகளை காலவரிசைப்படி அமைக்கவும்:\n1. இரண்டாவது நீதிபதிகள் வழக்கு (உச்ச நீதிமன்ற வழக்கறிஞர்கள் வழக்கு)\n2. முதல் நீதிபதிகள் வழக்கு (எஸ்.பி. குப்தா எதிர் இந்திய யூனியன்)\n3. நான்காவது நீதிபதிகள் வழக்கு (NJAC சட்டம் செல்லாது என அறிவிக்கப்பட்டது)\n4. மூன்றாவது நீதிபதிகள் வழக்கு (கொலீஜியம் விரிவாக்கம் குறித்த குடியரசுத் தலைவர் ஆலோசனை)",
        {"A": "2 -> 1 -> 4 -> 3", "B": "1 -> 2 -> 3 -> 4", "C": "2 -> 4 -> 1 -> 3", "D": "4 -> 2 -> 1 -> 3"},
        {"A": "2 -> 1 -> 4 -> 3", "B": "1 -> 2 -> 3 -> 4", "C": "2 -> 4 -> 1 -> 3", "D": "4 -> 2 -> 1 -> 3"},
        "A",
        "Chronology of Judicial Appointment Cases:\n1. First Judges Case (S.P. Gupta): 1981 (Executive primacy)\n2. Second Judges Case: 1993 (Collegium created: CJI + 2)\n3. Third Judges Case: 1998 (Collegium expanded: CJI + 4)\n4. Fourth Judges Case: 2015 (NJAC struck down under 99th Amendment)\nHence, the correct sequence is 2 -> 1 -> 4 -> 3.",
        "நீதிபதிகள் நியமன வழக்குகளின் காலவரிசை:\n1. முதல் நீதிபதிகள் வழக்கு (எஸ்.பி. குப்தா): 1981\n2. இரண்டாவது நீதிபதிகள் வழக்கு: 1993 (கொலீஜியம் உருவாக்கம்: CJI + 2)\n3. மூன்றாவது நீதிபதிகள் வழக்கு: 1998 (கொலீஜியம் விரிவாக்கம்: CJI + 4)\n4. நான்காவது நீதிபதிகள் வழக்கு: 2015 (99வது திருத்தம் மூலம் வந்த NJAC ரத்து)\nஎனவே சரியான வரிசை 2 -> 1 -> 4 -> 3.",
        "Do not confuse the 1993 2nd Judges Case (CJI + 2) with the 1998 3rd Judges Case (CJI + 4).",
        "1993-ன் 2வது நீதிபதிகள் வழக்கையும் (CJI + 2), 1998-ன் 3வது நீதிபதிகள் வழக்கையும் (CJI + 4) குழப்பிக் கொள்ளக் கூடாது.",
        "Years to remember: 1st=1981, 2nd=1993, 3rd=1998, 4th=2015.",
        "நினைவில் கொள்ள வேண்டிய ஆண்டுகள்: 1வது=1981, 2வது=1993, 3வது=1998, 4வது=2015.",
        "The 99th Constitutional Amendment Act (2014) established NJAC, which was invalidated in 2015 by the SC to preserve Judicial Independence.",
        "99வது அரசியலமைப்புத் திருத்தச் சட்டம் (2014) NJAC-ஐ உருவாக்கியது, இது நீதித்துறையின் சுதந்திரத்தைப் பாதுகாக்க 2015 இல் ரத்து செய்யப்பட்டது."))

    # Q6
    b1.append(mk_q(6, "Medium", "Direct",
        "Under Article 124(3) of the Constitution, which of the following is NOT a prescribed qualification for appointment as a judge of the Supreme Court of India?",
        "அரசியலமைப்பின் சரத்து 124(3)-ன் கீழ், இந்திய உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படுவதற்கான தகுதிகளில் எது தவறானது?",
        {"A": "He must be a citizen of India", "B": "He should have been a judge of a High Court for at least 5 years", "C": "He should have been an advocate of a High Court for at least 10 years", "D": "He must have attained the minimum age of 45 years"},
        {"A": "அவர் இந்தியக் குடிமகனாக இருக்க வேண்டும்", "B": "அவர் குறைந்தபட்சம் 5 ஆண்டுகள் உயர் நீதிமன்ற நீதிபதியாக பணியாற்றியிருக்க வேண்டும்", "C": "அவர் குறைந்தபட்சம் 10 ஆண்டுகள் உயர் நீதிமன்ற வழக்கறிஞராக பணியாற்றியிருக்க வேண்டும்", "D": "அவர் குறைந்தபட்சம் 45 வயதை அடைந்திருக்க வேண்டும்"},
        "D",
        "Article 124(3) does NOT prescribe any minimum age for appointment as a judge of the Supreme Court. The qualifications are: 1. Citizen of India, 2. HC Judge for 5 years OR HC Advocate for 10 years OR Distinguished jurist in the opinion of the President.",
        "சரத்து 124(3) உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படுவதற்கு எந்தவொரு குறைந்தபட்ச வயதையும் குறிப்பிடவில்லை. தகுதிகள்: 1. இந்தியக் குடிமகன், 2. 5 ஆண்டுகள் உயர் நீதிமன்ற நீதிபதி அல்லது 10 ஆண்டுகள் வழக்கறிஞர் அல்லது குடியரசுத் தலைவரின் பார்வையில் சிறந்த சட்ட நிபுணர்.",
        "Candidates often confuse maximum retirement age (65 years) with a non-existent minimum age requirement.",
        "தேர்வர்கள் அதிகபட்ச ஓய்வுபெறும் வயதை (65 வயது) குறைந்தபட்ச வயதுத் தகுதியுடன் குழப்பிக் கொள்கிறார்கள்.",
        "No minimum age is prescribed in the Constitution for SC or HC judges.",
        "உச்ச நீதிமன்றம் அல்லது உயர் நீதிமன்ற நீதிபதிகளுக்கு அரசியலமைப்பில் குறைந்தபட்ச வயது குறிப்பிடப்படவில்லை.",
        "A distinguished jurist can be appointed to the SC, but NOT to a High Court under Article 217.",
        "சிறந்த சட்ட நிபுணர் உச்ச நீதிமன்றத்திற்கு நியமிக்கப்படலாம், ஆனால் சரத்து 217-ன் கீழ் உயர் நீதிமன்றத்திற்கு நியமிக்கப்பட முடியாது."))

    # Q7
    b1.append(mk_q(7, "Hard", "Statement",
        "Consider the following statements regarding the removal procedure of a Supreme Court Judge under Article 124(4) and the Judges (Inquiry) Act, 1968:\n1. A removal motion signed by at least 100 members in Lok Sabha or 50 members in Rajya Sabha must be given to the Speaker/Chairman.\n2. The Speaker/Chairman is constitutionally bound to admit the motion and cannot refuse it.\n3. If admitted, a 3-member committee consisting of the CJI or a SC judge, a Chief Justice of a High Court, and a distinguished jurist is constituted to investigate the charges.\nWhich of the statements given above are correct?",
        "சரத்து 124(4) மற்றும் நீதிபதிகள் (விசாரணை) சட்டம் 1968-ன் கீழ் உச்ச நீதிமன்ற நீதிபதியை நீக்கும் நடைமுறை பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. மக்களவையில் குறைந்தது 100 உறுப்பினர்கள் அல்லது மாநிலங்களவையில் 50 உறுப்பினர்கள் கையெழுத்திட்ட நீக்கத் தீர்மானம் சபாநாயகர்/தலைவரிடம் வழங்கப்பட வேண்டும்.\n2. சபாநாயகர்/தலைவர் அந்தத் தீர்மானத்தை ஏற்றுக்கொள்வது அரசியலமைப்பு ரீதியாகக் கட்டாயமாகும், அவர் அதை நிராகரிக்க முடியாது.\n3. தீர்மானம் ஏற்றுக்கொள்ளப்பட்டால், CJI அல்லது உச்ச நீதிமன்ற நீதிபதி, உயர் நீதிமன்ற தலைமை நீதிபதி மற்றும் சிறந்த சட்ட நிபுணர் கொண்ட 3 உறுப்பினர் குழு விசாரணைக்காக அமைக்கப்படுகிறது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1 and 3 only", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1, 2 and 3"},
        {"A": "1 மற்றும் 3 மட்டும்", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1, 2 மற்றும் 3"},
        "A",
        "Statements 1 and 3 are correct. Statement 2 is incorrect because the Speaker or Chairman HAS THE DISCRETION to admit or refuse to admit the removal motion.",
        "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் நீக்கத் தீர்மானத்தை ஏற்கவோ அல்லது நிராகரிக்கவோ சபாநாயகருக்கு/தலைவருக்கு முழு அதிகாரம் (விருப்ப உரிமை) உண்டு.",
        "Candidates mistakenly believe the Speaker must accept the motion if the required signatures (100 LS / 50 RS) are present.",
        "தேவையான கையெழுத்துகள் (100 LS / 50 RS) இருந்தால் சபாநாயகர் தீர்மானத்தை ஏற்க வேண்டும் என்று தேர்வர்கள் தவறாக நம்புகின்றனர்.",
        "Removal requires Special Majority of Parliament: Majority of total membership + 2/3 of members present and voting in each House.",
        "நீக்கத்திற்கு நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மை தேவை: மொத்த உறுப்பினர்களில் பெரும்பான்மை + வருகை தந்து வாக்களிப்பவர்களில் 2/3 பங்கு.",
        "Grounds for removal under Article 124(4): Proved misbehaviour or Incapacity.",
        "சரத்து 124(4)-ன் கீழ் நீக்கத்திற்கான காரணங்கள்: நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது திறனின்மை."))

    # Q8
    b1.append(mk_q(8, "Medium", "Scenario",
        "When the office of the Chief Justice of India is vacant, or when the CJI is by reason of absence or otherwise unable to perform the duties of his office, who appoints an Acting Chief Justice under Article 126?",
        "இந்தியத் தலைமை நீதிபதி பதவி காலியாக இருக்கும் போதோ, அல்லது தற்காலிகமாக கடமைகளை ஆற்ற முடியாத போதோ, சரத்து 126-ன் கீழ் செயல் தலைமை நீதிபதியை நியமிப்பவர் யார்?",
        {"A": "The Senior-most judge of the Supreme Court automatically takes over without any formal order", "B": "The President of India appoints another judge of the Supreme Court to perform the duties", "C": "The Collegium of Supreme Court judges nominates the Acting CJI", "D": "The Union Law Minister appoints the Acting CJI"},
        {"A": "உச்ச நீதிமன்றத்தின் மூத்த நீதிபதி எந்த உத்தரவும் இன்றி தானாகவே பொறுப்பேற்பார்", "B": "இந்தியக் குடியரசுத் தலைவர் உச்ச நீதிமன்றத்தின் மற்றொரு நீதிபதியை பொறுப்புகளை ஆற்ற நியமிக்கிறார்", "C": "உச்ச நீதிமன்ற நீதிபதிகள் கொலீஜியம் செயல் தலைமை நீதிபதியை பரிந்துரைக்கிறது", "D": "மத்திய சட்ட அமைச்சர் செயல் தலைமை நீதிபதியை நியமிக்கிறார்"},
        "B",
        "Under Article 126, when the office of CJI is vacant or the CJI is absent, the duties of the office shall be performed by such one of the other judges of the SC as the President may appoint for the purpose.",
        "சரத்து 126-ன் படி, CJI பதவி காலியாக இருக்கும்போது அல்லது அவர் இல்லாவிட்டால், குடியரசுத் தலைவரால் நியமிக்கப்படும் உச்ச நீதிமன்றத்தின் மற்றொரு நீதிபதி அப்பொறுப்புகளை ஆற்றுவார்.",
        "Candidates assume auto-assumption by seniority without President's appointment order.",
        "குடியரசுத் தலைவரின் நியமன உத்தரவு இன்றி மூப்பு அடிப்படையில் தானாகவே பொறுப்பேற்பார் என தேர்வர்கள் கருதுகின்றனர்.",
        "Article 126 = Acting CJI appointed by President.",
        "சரத்து 126 = குடியரசுத் தலைவரால் நியமிக்கப்படும் செயல் தலைமை நீதிபதி.",
        "Acting CJI must be a sitting judge of the Supreme Court.",
        "செயல் தலைமை நீதிபதி உச்ச நீதிமன்றத்தின் தற்போதைய நீதிபதியாக இருக்க வேண்டும்."))

    # Q9
    b1.append(mk_q(9, "Hard", "Direct",
        "Under Article 127 of the Constitution, who can appoint an Ad Hoc Judge of the Supreme Court, and what conditions must be satisfied?",
        "அரசியலமைப்பின் சரத்து 127-ன் கீழ், உச்ச நீதிமன்றத்திற்கு தற்காலிக (அட் ஹாக்) நீதிபதியை நியமிப்பவர் யார் மற்றும் என்ன நிபந்தனைகள் நிறைவு செய்யப்பட வேண்டும்?",
        {"A": "The President of India on recommendation of Union Cabinet", "B": "The Chief Justice of India with previous consent of the President and consultation with the Chief Justice of the concerned High Court", "C": "The Chief Justice of India independently without any consent", "D": "Parliament by enacting a special law"},
        {"A": "மத்திய அமைச்சரவையின் பரிந்துரையின் பேரில் இந்தியக் குடியரசுத் தலைவர்", "B": "குடியரசுத் தலைவரின் முன் ஒப்புதலுடனும் சம்பந்தப்பட்ட உயர் நீதிமன்ற தலைமை நீதிபதியின் கலந்தாலோசனையுடனும் இந்திய தலைமை நீதிபதி", "C": "எந்த ஒப்புதலும் இன்றி சுயாதீனமாக இந்திய தலைமை நீதிபதி", "D": "சிறப்புச் சட்டம் இயற்றுவதன் மூலம் நாடாளுமன்றம்"},
        "B",
        "Under Article 127, if there is a lack of quorum of SC judges to hold or continue any session, the CJI can appoint a judge of a High Court (qualified for SC) as an ad hoc judge of the SC, but only with previous consent of the President and after consultation with the CJI of the concerned HC.",
        "சரத்து 127-ன் படி, உச்ச நீதிமன்ற அமர்வை நடத்த நீதிபதிகளின் எண்ணிக்கை (கோரம்) பற்றாக்குறையாக இருந்தால், குடியரசுத் தலைவரின் முன் ஒப்புதலுடனும் சம்பந்தப்பட்ட உயர் நீதிமன்ற தலைமை நீதிபதியைக் கலந்தாலோசித்தும் CJI ஒரு உயர் நீதிமன்ற நீதிபதியை தற்காலிக நீதிபதியாக நியமிக்கலாம்.",
        "Ad hoc judges are appointed under Article 127 ONLY when there is a lack of quorum in Supreme Court.",
        "உச்ச நீதிமன்றத்தில் நீதிபதிகளின் கோரம் (குறைந்தபட்ச எண்ணிக்கை) இல்லாதபோது மட்டுமே சரத்து 127-ன் கீழ் தற்காலிக நீதிபதிகள் நியமிக்கப்படுகிறார்கள்.",
        "Ad hoc judges enjoy all jurisdiction, powers, and privileges of a Supreme Court judge while attending sessions.",
        "தற்காலிக நீதிபதிகள் அமர்வுகளில் பங்கேற்கும்போது உச்ச நீதிமன்ற நீதிபதியின் அனைத்து அதிகாரங்களையும் சலுகைகளையும் அனுபவிக்கிறார்கள்.",
        "Only a High Court judge qualified for SC appointment can be appointed as an Ad Hoc judge.",
        "உச்ச நீதிமன்றத்திற்குத் தகுதியுடைய உயர் நீதிமன்ற நீதிபதி மட்டுமே தற்காலிக நீதிபதியாக நியமிக்கப்பட முடியும்."))

    # Q10
    b1.append(mk_q(10, "Medium", "Direct",
        "Under Article 125 of the Constitution, how are the salaries, allowances, pensions, and administrative expenses of the Supreme Court judges determined and charged?",
        "சரத்து 125-ன் படி, உச்ச நீதிமன்ற நீதிபதிகளின் சம்பளம், படிகள், ஓய்வூதியம் மற்றும் நிர்வாகச் செலவுகள் எவ்வாறு தீர்மானிக்கப்படுகின்றன மற்றும் எதிலிருந்து வழங்கப்படுகின்றன?",
        {"A": "Determined by President and charged on Contingency Fund of India", "B": "Determined by Parliament by law and charged on the Consolidated Fund of India", "C": "Determined by Law Commission and voted by Lok Sabha annually", "D": "Determined by Finance Commission and split between Centre and States"},
        {"A": "குடியரசுத் தலைவரால் தீர்மானிக்கப்பட்டு இந்தியாவின் அவசரகால நிதியிலிருந்து வழங்கப்படுகிறது", "B": "நாடாளுமன்றச் சட்டத்தால் தீர்மானிக்கப்பட்டு இந்தியாவின் தொகுப்பு நிதியிலிருந்து (Consolidated Fund) வழங்கப்படுகிறது", "C": "சட்ட ஆணையத்தால் தீர்மானிக்கப்பட்டு மக்களவையால் ஆண்டுதோறும் வாக்களிக்கப்படுகிறது", "D": "நிதி ஆணையத்தால் தீர்மானிக்கப்பட்டு மத்திய-மாநில அரசுகளிடையே பிரிக்கப்படுகிறது"},
        "B",
        "Article 125 states salaries are determined by Parliament by law. Article 112(3)(d) provides that salaries, allowances, and pensions of SC judges and administrative expenses of SC (Art 146) are CHARGED on the Consolidated Fund of India and are NON-VOTABLE by Parliament.",
        "சரத்து 125-ன் படி சம்பளம் நாடாளுமன்ற சட்டத்தால் தீர்மானிக்கப்படுகிறது. சரத்து 112(3)(d)-ன் படி நீதிபதிகளின் சம்பளம், ஓய்வூதியம் மற்றும் நிர்வாகச் செலவுகள் இந்தியாவின் தொகுப்பு நிதியில் பொறுப்பளிக்கப்பட்டவையாகும் (Charged), இதற்கு நாடாளுமன்றத்தில் வாக்கெடுப்பு தேவைப்படாது.",
        "Salaries cannot be varied to their disadvantage after appointment, EXCEPT during a Financial Emergency under Article 360.",
        "நியமனத்திற்குப் பிறகு அவர்களின் சம்பளத்தைக் குறைக்க முடியாது; ஆனால் சரத்து 360 நிதி அவசரநிலையின் போது குறைக்கலாம்.",
        "Charged Expenditure = Non-votable by Parliament (Discussion is allowed).",
        "பொறுப்பளிக்கப்பட்ட செலவினம் (Charged Expenditure) = நாடாளுமன்ற வாக்கெடுப்பிற்கு உட்படாதது (விவாதிக்கலாம்).",
        "Pensions of SC judges are charged on the Consolidated Fund of INDIA.",
        "உச்ச நீதிமன்ற நீதிபதிகளின் ஓய்வூதியம் இந்தியாவின் தொகுப்பு நிதியில் பொறுப்பளிக்கப்பட்டுள்ளது."))

    # Q11
    b1.append(mk_q(11, "Hard", "Statement",
        "Consider the following statements regarding the Supreme Court as a 'Court of Record' under Article 129 of the Constitution:\n1. The judgments, proceedings, and acts of the Supreme Court are recorded for perpetual memory and testimony.\n2. The records of the Supreme Court have evidentiary value and cannot be questioned when produced before any subordinate court.\n3. The Supreme Court has the power to punish for contempt of itself, but it cannot punish for contempt of High Courts or Subordinate Courts.\nWhich of the statements given above is/are correct?",
        "அரசியலமைப்பின் சரத்து 129-ன் கீழ் உச்ச நீதிமன்றம் ஒரு 'ஆவண நீதிமன்றம்' (Court of Record) என்பது பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உச்ச நீதிமன்றத்தின் தீர்ப்புகள், நடவடிக்கைகள் மற்றும் செயல்கள் நிரந்தர நினைவிற்காகவும் சான்றாகவும் பதிவு செய்யப்படுகின்றன.\n2. உச்ச நீதிமன்றத்தின் பதிவுகள் சான்றாதார மதிப்பைக் கொண்டவை, அவற்றை எந்தவொரு கீழமை நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது.\n3. உச்ச நீதிமன்றத்திற்கு தன்னை அவமதிப்பவர்களுக்குத் தண்டிக்கும் அதிகாரம் உண்டு, ஆனால் உயர் நீதிமன்றங்கள் அல்லது கீழமை நீதிமன்றங்களை அவமதிப்பவர்களுக்குத் தண்டிக்கும் அதிகாரம் இல்லை.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
        {"A": "1 and 2 only", "B": "2 and 3 only", "C": "1 and 3 only", "D": "1, 2 and 3"},
        {"A": "1 மற்றும் 2 மட்டும்", "B": "2 மற்றும் 3 மட்டும்", "C": "1 மற்றும் 3 மட்டும்", "D": "1, 2 மற்றும் 3"},
        "A",
        "Statements 1 and 2 are correct. Statement 3 is incorrect because in Extraordinary High Court Cases, the Supreme Court held that its power to punish for contempt under Article 129 includes the power to punish for contempt of High Courts, Subordinate Courts, and Tribunals throughout India.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சரத்து 129-ன் கீழ் உச்ச நீதிமன்றத்தின் அவமதிப்புத் தண்டனை அதிகாரம் என்பது உயர் நீதிமன்றங்கள், கீழமை நீதிமன்றங்கள் மற்றும் தீர்ப்பாயங்களை அவமதிப்பதையும் உள்ளடக்கும்.",
        "Candidates often believe SC can only punish contempt of ITSELF. The SC's contempt jurisdiction extends over all courts in India.",
        "உச்ச நீதிமன்றம் தன்னை அவமதிப்பதை மட்டுமே தண்டிக்க முடியும் என தேர்வர்கள் தவறாகக் கருதுகின்றனர். நாட்டின் அனைத்து நீதிமன்ற அவமதிப்பையும் தண்டிக்கும் அதிகாரம் அதற்கு உண்டு.",
        "Court of Record (Art 129) includes two powers: Perpetual legal memory & Power to punish for contempt.",
        "ஆவண நீதிமன்றம் (சரத்து 129) இரண்டு அதிகாரங்களைக் கொண்டது: நிரந்தரச் சான்றாதாரப் பதிவு & அவமதிப்புத் தண்டனை அதிகாரம்.",
        "Article 215 makes High Courts Courts of Record with similar powers.",
        "சரத்து 215 உயர் நீதிமன்றங்களை ஆவண நீதிமன்றங்களாக மாற்றுகிறது."))

    # Q12
    b1.append(mk_q(12, "Medium", "Scenario",
        "A citizen's Fundamental Right is violated by an executive order of a State Government. The citizen directly approaches the Supreme Court under Article 32 instead of the High Court under Article 226. Which of the following is correct regarding Supreme Court's position?",
        "மாநில அரசின் நிர்வாக உத்தரவால் ஒரு குடிமகனின் அடிப்படை உரிமை மீறப்படுகிறது. அக்குடிமகன் உயர் நீதிமன்றத்திற்குச் செல்லாமல் நேரடியாக உச்ச நீதிமன்றத்தை சரத்து 32-ன் கீழ் அணுகுகிறார். உச்ச நீதிமன்றத்தின் நிலைப்பாடு குறித்த பின்வரும் கூற்றுகளில் எது சரியானது?",
        {"A": "The Supreme Court MUST entertain the petition because Article 32 is itself a Fundamental Right", "B": "The Supreme Court will reject the petition because High Court jurisdiction under Article 226 is mandatory first", "C": "The Supreme Court can entertain it only if the Governor permits", "D": "The Supreme Court can issue writs only for civil rights, not fundamental rights"},
        {"A": "சரத்து 32 என்பதே ஒரு அடிப்படை உரிமை என்பதால் உச்ச நீதிமன்றம் மனுவை கண்டிப்பாக விசாரணை செய்ய வேண்டும்", "B": "சரத்து 226-ன் கீழ் உயர் நீதிமன்ற அதிகார வரம்பை முதலில் அணுகுவது கட்டாயம் என்பதால் மனுவை நிராகரிக்கும்", "C": "ஆளுநர் அனுமதித்தால் மட்டுமே உச்ச நீதிமன்றம் விசாரிக்க முடியும்", "D": "உச்ச நீதிமன்றம் சிவில் உரிமைகளுக்கு மட்டுமே பேராணைகளை வெளியிட முடியும், அடிப்படை உரிமைகளுக்கு அல்ல"},
        "A",
        "Under Article 32, the right to move the Supreme Court for enforcement of Fundamental Rights is itself a guaranteed Fundamental Right. While the SC encourages litigants to approach HCs first, it CANNOT refuse to entertain an Article 32 petition.",
        "சரத்து 32-ன் படி அடிப்படை உரிமைகளை அமல்படுத்த உச்ச நீதிமன்றத்தை அணுகும் உரிமையே ஒரு அடிப்படை உரிமையாகும். உயர் நீதிமன்றத்தை முதலில் அணுகுமாறு கூறினாலும், சரத்து 32 மனுவை விசாரிக்க உச்ச நீதிமன்றம் மறுக்க முடியாது.",
        "Unlike High Court under Article 226 (discretionary), Supreme Court under Article 32 is a GUARANTOR and PROTECTOR of Fundamental Rights; it cannot refuse.",
        "சரத்து 226-ன் கீழ் உயர் நீதிமன்ற அதிகாரம் விரும்பத்தக்கது; ஆனால் சரத்து 32-ன் கீழ் உச்ச நீதிமன்றம் அடிப்படை உரிமைகளின் பாதுகாப்பாளராக உள்ளதால் மறுக்க முடியாது.",
        "Article 32 is part of the Basic Structure of the Constitution and cannot be suspended except during National Emergency (Art 359).",
        "சரத்து 32 அரசியலமைப்பின் அடிப்படை கட்டமைப்பின் ஒரு பகுதியாகும்.",
        "Article 32 applies ONLY to Fundamental Rights, whereas Article 226 applies to Fundamental Rights AND ordinary legal rights.",
        "சரத்து 32 அடிப்படை உரிமைகளுக்கு மட்டுமே பொருந்தும்; சரத்து 226 சாதாரண சட்ட உரிமைகளுக்கும் பொருந்தும்."))

    # Q13
    b1.append(mk_q(13, "Hard", "Match",
        "Match List-I (Writ Name) with List-II (Literal Meaning & Constitutional Scope):\n\nList-I:\na) Habeas Corpus\nb) Mandamus\nc) Certiorari\nd) Quo-Warranto\n\nList-II:\n1. 'We Command' - Issued to compel a public official to perform a mandatory statutory duty\n2. 'To have the body of' - Remedy against illegal detention by public or private entities\n3. 'By what authority' - Issued to prevent illegal usurpation of a public office\n4. 'To be certified' - Issued to quash an order passed by a lower court/tribunal exceeding jurisdiction",
        "பட்டியல்-I (பேராணை பெயர்) பட்டியல்-II உடன் (நேரடிப் பொருள் மற்றும் நோக்கம்) பொருத்துக:\n\nபட்டியல்-I:\na) ஆட்கொணர்வுப் பேராணை (Habeas Corpus)\nb) கட்டளையுறுத்தும் பேராணை (Mandamus)\nc) நெறிமுறைப்படுத்தும் பேராணை (Certiorari)\nd) தகுதிகாண் பேராணை (Quo-Warranto)\n\nபட்டியல்-II:\n1. 'நாங்கள் கட்டளையிடுகிறோம்' - சட்டப்பூர்வக் கடமையை ஆற்ற பொது அதிகாரியைப் பணிப்பது\n2. 'உடலைக் கொணர்க' - சட்டவிரோதக் காவலுக்கு எதிரான நிவாரணம்\n3. 'எந்த அதிகாரத்தின் அடிப்படையில்' - பொதுப் பதவியை சட்டவிரோதமாகக் கைப்பற்றுவதைத் தடுப்பது\n4. 'சான்றளிக்கப்பட வேண்டும்' - அதிகார வரம்பை மீறிய கீழ் நீதிமன்ற உத்தரவை ரத்து செய்வது",
        {"A": "a-2, b-1, c-4, d-3", "B": "a-1, b-2, c-3, d-4", "C": "a-2, b-4, c-1, d-3", "D": "a-3, b-1, c-4, d-2"},
        {"A": "a-2, b-1, c-4, d-3", "B": "a-1, b-2, c-3, d-4", "C": "a-2, b-4, c-1, d-3", "D": "a-3, b-1, c-4, d-2"},
        "A",
        "Correct Match:\na) Habeas Corpus -> 'To have the body of' (2)\nb) Mandamus -> 'We Command' (1)\nc) Certiorari -> 'To be certified' (4)\nd) Quo-Warranto -> 'By what authority' (3)",
        "சரியான பொருத்தம்:\na) Habeas Corpus -> உடலைக் கொணர்க (2)\nb) Mandamus -> நாங்கள் கட்டளையிடுகிறோம் (1)\nc) Certiorari -> சான்றளிக்கப்பட வேண்டும் (4)\nd) Quo-Warranto -> எந்த அதிகாரத்தின் அடிப்படையில் (3)",
        "Quo-Warranto can be moved by ANY interested person, not necessarily the aggrieved party (relaxation of locus standi).",
        "தகுதிகாண் பேராணையை (Quo-Warranto) பாதிக்கப்பட்ட நபர் மட்டுமே தொடர வேண்டியதில்லை; எந்தவொரு ஆர்வமுள்ள நபரும் தொடரலாம்.",
        "Mandamus CANNOT be issued against the President, State Governors, or a Private Individual.",
        "குடியரசுத் தலைவர், ஆளுநர்கள் அல்லது தனிநபர்களுக்கு எதிராக கட்டளையுறுத்தும் பேராணையை வெளியிட முடியாது.",
        "Certiorari is both preventive and curative.",
        "நெறிமுறைப்படுத்தும் பேராணை த தடுப்பு மற்றும் நிவாரணத் தன்மையுடையது."))

    # Q14
    b1.append(mk_q(14, "Hard", "Statement",
        "Consider the following statements regarding Special Leave Petition (SLP) under Article 136 of the Constitution:\n1. It is a discretionary extra-ordinary power vested in the Supreme Court to grant special leave to appeal from any judgment or decree in any cause or matter.\n2. It can be granted against any court or tribunal in India, including courts constituted by or under any law relating to the Armed Forces.\n3. Article 136 does not confer a right of appeal upon any party, but merely confers a discretionary power on the SC to grant leave to appeal.\nWhich of the statements given above is/are correct?",
        "அரசியலமைப்பின் சரத்து 136-ன் கீழ் சிறப்பு விடுப்பு மனு (SLP) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது எந்தவொரு வழக்கில் தீர்ப்பு அல்லது உத்தரவுக்கு எதிராக மேல்முறையீடு செய்ய சிறப்பு அனுமதி அளிக்கும் உச்ச நீதிமன்றத்தின் தன்னாட்சி அதிகாரமாகும்.\n2. முப்படைகள் தொடர்பான சட்டத்தின் கீழ் அமைக்கப்பட்ட ராணுவ நீதிமன்றங்களின் உத்தரவுகளுக்கும் எதிராக இதைப் பயன்படுத்தலாம்.\n3. சரத்து 136 எந்தவொரு தரப்பினருக்கும் மேல்முறையீட்டு உரிமையை வழங்கவில்லை, மாறாக உச்ச நீதிமன்றத்திற்கு அனுமதி வழங்கும் விருப்ப அதிகாரத்தை மட்டுமே அளிக்கிறது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
        {"A": "1 and 3 only", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1, 2 and 3"},
        {"A": "1 மற்றும் 3 மட்டும்", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1, 2 மற்றும் 3"},
        "A",
        "Statements 1 and 3 are correct. Statement 2 is incorrect because Article 136(2) EXPLICITLY EXCLUDES any judgment, determination, sentence, or order passed by any court or tribunal constituted by or under any law relating to the Armed Forces.",
        "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் சரத்து 136(2) ராணுவச் சட்டத்தின் கீழ் அமைக்கப்பட்ட முப்படை நீதிமன்றங்களின் தீர்ப்புகளுக்கு விலக்கு அளிக்கிறது.",
        "Candidates overlook Article 136(2) which explicitly bars military court appeals under SLP.",
        "சரத்து 136(2) ராணுவ நீதிமன்றத் தீர்ப்புகளுக்கு விலக்களிப்பதை தேர்வர்கள் தவறவிட்டு விடுகிறார்கள்.",
        "SLP is a plenary and wide power, covering civil, criminal, income tax, revenue, and labor matters.",
        "SLP என்பது சிவில், குற்றவியல், வருமான வரி, வருவாய் மற்றும் தொழிலாளர் பிரச்சினைகளை உள்ளடக்கிய பரந்த அதிகாரமாகும்.",
        "SLP is granted only in exceptional cases involving substantial questions of law or grave injustice.",
        "கடுமையான அநீதி அல்லது முக்கிய சட்டக் கேள்வி உள்ள வழக்குகளில் மட்டுமே SLP அனுமதிக்கப்படுகிறது."))

    # Q15
    b1.append(mk_q(15, "Medium", "Direct",
        "Under Article 137 of the Constitution, the Supreme Court has the power to review any judgment pronounced or order made by it. On what grounds was the concept of 'Curative Petition' evolved by the Supreme Court?",
        "சரத்து 137-ன் படி உச்ச நீதிமன்றத்திற்குத் தனது தீர்ப்புகளை மறுஆய்வு செய்யும் (Review Jurisdiction) அதிகாரம் உள்ளது. உச்ச நீதிமன்றத்தால் 'சீராய்வு மனு' (Curative Petition) என்ற கோட்பாடு எந்த மைல்கல் வழக்கில் உருவாக்கப்பட்டது?",
        {"A": "Kesavananda Bharati v. State of Kerala (1973)", "B": "Rupa Ashok Hurra v. Ashok Hurra (2002)", "C": "Maneka Gandhi v. Union of India (1978)", "D": "Minerva Mills v. Union of India (1980)"},
        {"A": "கேசவானந்த பாரதி எதிர் கேரளா (1973)", "B": "ரூபா அசோக் ஹுர்ரா எதிர் அசோக் ஹுர்ரா (2002)", "C": "மேனகா காந்தி எதிர் இந்திய யூனியன் (1978)", "D": "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)"},
        "B",
        "The Supreme Court evolved the concept of 'Curative Petition' in Rupa Ashok Hurra v. Ashok Hurra (2002) to cure gross miscarriage of justice after a review petition under Article 137 has been dismissed.",
        "சரத்து 137-ன் கீழான சீராய்வு மனு தள்ளுபடி செய்யப்பட்ட பிறகு, கடுமையான அநீதியைச் சரிசெய்ய 'ரூபா அசோக் ஹுர்ரா எதிர் அசோக் ஹுர்ரா (2002)' வழக்கில் உச்ச நீதிமன்றத்தால் சீராய்வு மனு (Curative Petition) உருவாக்கப்பட்டது.",
        "Review Petition (Art 137) comes FIRST. Curative Petition is the LAST judicial resort after Review Petition is dismissed.",
        "சரத்து 137-ன் கீழ் சீராய்வு மனு (Review Petition) முதன்மையானது. அது தள்ளுபடியான பிறகே Curative Petition தாக்கல் செய்ய முடியும்.",
        "Curative Petition must be certified by a Senior Advocate and circulated to a bench of 3 senior-most judges + judges who passed the original order.",
        "Curative Petition மூத்த வழக்கறிஞரால் சான்றளிக்கப்பட்டு மூத்த நீதிபதிகளுக்கு சுற்றறிக்கையாக அனுப்பப்பட வேண்டும்.",
        "Grounds for Curative Petition: Violation of natural justice or apprehension of judicial bias.",
        "இயற்கை நீதி மீறல் அல்லது நீதிபதியின் சார்புத் தன்மை ஆகியவை சீராய்வு மனுவிற்கான காரணங்களாகும்."))

    # Q16
    b1.append(mk_q(16, "Hard", "Statement",
        "Consider the following statements regarding the Advisory Jurisdiction of the Supreme Court under Article 143:\n1. Under Clause (1), the President may refer any question of law or fact of public importance to the Supreme Court for its opinion.\n2. Under Clause (2), the President may refer disputes arising out of pre-constitution treaties, agreements, or engagements to the Supreme Court.\n3. The Supreme Court is bound to give its opinion on Clause (1) matters, but has discretion to refuse opinion on Clause (2) matters.\nWhich of the statements given above is/are correct?",
        "சரத்து 143-ன் கீழ் உச்ச நீதிமன்றத்தின் ஆலோசனை அதிகார வரம்பு பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. பிரிவு (1)-ன் கீழ், பொது முக்கியத்துவம் வாய்ந்த எந்தவொரு சட்ட அல்லது உண்மை சார்ந்த கேள்வியையும் குடியரசுத் தலைவர் உச்ச நீதிமன்றத்தின் ஆலோசனைக் கருத்துக்காக அனுப்பலாம்.\n2. பிரிவு (2)-ன் கீழ், அரசியலமைப்புக்கு முந்தைய உடன்படிக்கைகள் மற்றும் ஒப்பந்தங்கள் தொடர்பான சர்ச்சைகளைக் குடியரசுத் தலைவர் உச்ச நீதிமன்றத்திற்கு அனுப்பலாம்.\n3. பிரிவு (1) விவகாரங்களில் உச்ச நீதிமன்றம் கருத்து தெரிவிப்பது கட்டாயமாகும், ஆனால் பிரிவு (2) விவகாரங்களில் கருத்தைத் தெரிவிக்க மறுக்க அதிகாரம் உண்டு.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
        {"A": "1 and 2 only", "B": "2 and 3 only", "C": "1 and 3 only", "D": "1, 2 and 3"},
        {"A": "1 மற்றும் 2 மட்டும்", "B": "2 மற்றும் 3 மட்டும்", "C": "1 மற்றும் 3 மட்டும்", "D": "1, 2 மற்றும் 3"},
        "A",
        "Statements 1 and 2 are correct. Statement 3 is INCORRECT (Trap point). Under Clause (1), the Supreme Court MAY tender or refuse to tender its opinion (e.g. Ayodhya Reference 1994). Under Clause (2), the Supreme Court MUST obligatorily tender its opinion.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது (TNPSC பொறி). பிரிவு (1)-ல் உச்ச நீதிமன்றம் கருத்து தெரிவிக்கலாம் அல்லது மறுக்கலாம் (எ.கா. அயோத்தி வழக்கு 1994). ஆனால் பிரிவு (2)-ல் கருத்து தெரிவிப்பது உச்ச நீதிமன்றத்திற்கு கட்டாயமாகும்.",
        "Candidates get the obligation reversed: Clause 1 (Public importance) = Optional to render opinion; Clause 2 (Pre-constitution treaty) = Mandatory to render opinion.",
        "தேர்வர்கள் இதை மாற்றி நினைத்துக்கொள்கிறார்கள்: பிரிவு 1 = கருத்து கூறுவது விருப்ப உரிமை; பிரிவு 2 = கருத்து கூறுவது கட்டாயம்.",
        "In BOTH cases, the opinion rendered by the Supreme Court is ADVISORY only and NOT binding on the President or subordinate courts.",
        "இரண்டு பிரிவுகளிலுமே உச்ச நீதிமன்றத்தின் கருத்து ஆலோசனையே அன்றி குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது.",
        "Advisory references require a bench of at least 5 judges under Article 145(3).",
        "ஆலோசனை விவகாரங்களை விசாரிக்க குறைந்தது 5 நீதிபதிகள் கொண்ட அமர்வு தேவை."))

    # Q17
    b1.append(mk_q(17, "Medium", "Direct",
        "Article 141 of the Constitution states that 'The law declared by the Supreme Court shall be binding on all courts within the territory of India'. Which of the following is an exception or limitation to Article 141?",
        "சரத்து 141 'உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் இந்தியாவின் அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும்' எனக் கூறுகிறது. இதற்கான விதிவிலக்கு அல்லது வரம்பு எது?",
        {"A": "The law declared by Supreme Court does NOT bind the Supreme Court itself; it can review or depart from its own earlier decisions", "B": "High Courts are not bound by Supreme Court decisions if their local High Court rules differ", "C": "District Courts can override Supreme Court rulings in criminal cases", "D": "State Assemblies can pass a resolution declaring a Supreme Court judgment non-binding in that state"},
        {"A": "உச்ச நீதிமன்றம் அறிவிக்கும் சட்டம் உச்ச நீதிமன்றத்தையே கட்டுப்படுத்தாது; அது தனது முந்தைய தீர்ப்பை மறுஆய்வு செய்யலாம் அல்லது மாற்றலாம்", "B": "உயர் நீதிமன்ற விதிகள் வேறுபட்டால் உச்ச நீதிமன்றத் தீர்ப்புகள் உயர் நீதிமன்றங்களைக் கட்டுப்படுத்தாது", "C": "குற்றவியல் வழக்குகளில் மாவட்ட நீதிமன்றங்கள் உச்ச நீதிமன்றத் தீர்ப்புகளை நிராகரிக்கலாம்", "D": "மாநில சட்டமன்றங்கள் தீர்மானம் நிறைவேற்றி உச்ச நீதிமன்றத் தீர்ப்பை அம்மாநிலத்தில் செல்லாததாக்கலாம்"},
        "A",
        "Article 141 binds 'all courts within the territory of India'. However, in Bengal Immunity Co. v. State of Bihar (1955), the Supreme Court held that it is NOT bound by its own previous decisions and can depart from them when convinced of an error.",
        "சரத்து 141 அனைத்து கீழ் நீதிமன்றங்களையும் கட்டுப்படுத்துகிறது. ஆனால் 'பெங்கால் இம்யூனிட்டி வழக்கு (1955)'-ல் உச்ச நீதிமன்றம் தனது சொந்த முந்தைய தீர்ப்புகளுக்குக் கட்டுப்பட்டதல்ல என்றும், தவறு என உணர்ந்தால் அதை மாற்றலாம் என்றும் தீர்ப்பளித்தது.",
        "Candidates assume Article 141 binds the Supreme Court itself indefinitely. SC is free to overrule its own precedents (e.g. Golaknath overruled by Kesavananda).",
        "சரத்து 141 உச்ச நீதிமன்றத்தையும் கட்டுப்படுத்தும் என தேர்வர்கள் தவறாக எண்ணுகின்றனர். உச்ச நீதிமன்றம் தனது முந்தைய தீர்ப்புகளை மாற்ற முடியும்.",
        "The expression 'law declared' includes ratio decidendi of judgments.",
        "சட்டம் என்பது தீர்ப்பின் முதன்மை சட்டக் கொள்கையை (Ratio Decidendi) குறிக்கும்.",
        "Obiter dicta of Supreme Court also carries great persuasive weight on subordinate courts.",
        "ஒபிடர் டிக்டா (துணை கருத்துகள்) கீழ் நீதிமன்றங்களுக்கு மிகுந்த வழிகாட்டுதல் மதிப்பைக் கொண்டது."))

    # Q18
    b1.append(mk_q(18, "Hard", "Scenario",
        "Under Article 142(1) of the Constitution, the Supreme Court may pass such decree or make such order as is necessary for doing 'complete justice' in any cause or matter pending before it. Which of the following correctly reflects the constitutional limitation of Article 142?",
        "அரசியலமைப்பின் சரத்து 142(1)-ன் படி உச்ச நீதிமன்றம் தன் முன் உள்ள வழக்கில் 'முழுமையான நீதி' (Complete Justice) வழங்குவதற்கான உத்தரவுகளைப் பிறப்பிக்கலாம். இதற்கான அரசியலமைப்பு வரம்பு எது?",
        {"A": "Article 142 gives unlimited powers that can override express statutory prohibitions laid down by Parliament", "B": "Article 142 powers cannot be used to supplant or override substantive statutory provisions directly dealing with the subject", "C": "Article 142 can be exercised only during Emergency declared under Article 352", "D": "Article 142 orders require prior ratification by the Union Cabinet"},
        {"A": "சரத்து 142 நாடாளுமன்றச் சட்டங்களின் வெளிப்படையான தடைகளையும் மீறக்கூடிய வரம்பற்ற அதிகாரத்தை அளிக்கிறது", "B": "சரத்து 142-ன் அதிகாரத்தை நாடாளுமன்றத்தின் வெளிப்படையான சட்டப் பிரிவுகளை நேரடியாக மீறவோ அல்லது அழிக்கவோ பயன்படுத்த முடியாது", "C": "சரத்து 352 அவசரநிலையின் போது மட்டுமே சரத்து 142-ஐப் பயன்படுத்த முடியும்", "D": "சரத்து 142 உத்தரவுகளுக்கு மத்திய அமைச்சரவையின் முன் ஒப்புதல் தேவை"},
        "B",
        "In Supreme Court Bar Association v. Union of India (1998), the Supreme Court held that powers under Article 142 are inherent and supplementary, but CANNOT be used to ignore or override express statutory provisions passed by Parliament.",
        "உச்ச நீதிமன்ற பார் அசோசியேஷன் எதிர் இந்திய யூனியன் (1998) வழக்கில், சரத்து 142 அதிகாரங்கள் கூடுதல் தன்மையுடையவை என்றும், நாடாளுமன்றத்தின் வெளிப்படையான சட்டப் விதிகளை மீறப் பயன்படுத்தப்படக் கூடாது என்றும் உச்ச நீதிமன்றம் தெளிவுபடுத்தியது.",
        "Article 142 is often termed as 'Judicial Activism tool', but it cannot violate express statutory commands or Fundamental Rights.",
        "சரத்து 142 நீதித்துறை செயல்பாட்டின் கருவியாகக் கருதப்பட்டாலும், அது நேரடி சட்ட விதிகளை மீற முடியாது.",
        "Orders under Article 142 are enforceable throughout the territory of India in such manner as prescribed by Parliament.",
        "சரத்து 142 உத்தரவுகள் இந்தியா முழுவதும் அமல்படுத்தத்தக்கவை.",
        "Landmark Article 142 applications: Union Carbide Bhopal gas tragedy compensation, Ayodhya land title order.",
        "போபால் நச்சு வாயு வழக்கு நிவாரணம் மற்றும் அயோத்தி வழக்கு ஆகியவற்றில் சரத்து 142 பயன்படுத்தப்பட்டது."))

    # Q19
    b1.append(mk_q(19, "Medium", "Match",
        "Match List-I (Appellate Article) with List-II (Nature of Constitutional Appellate Jurisdiction):\n\nList-I:\na) Article 132\nb) Article 133\nc) Article 134\nd) Article 134A\n\nList-II:\n1. Appeal in Civil Matters involving substantial question of law\n2. Appeal in Constitutional cases certified by High Court\n3. Certificate for Appeal issued by High Court suo motu or on application\n4. Appeal in Criminal Matters (Death sentence reversal / fitness)",
        "பட்டியல்-I (மேல்முறையீட்டுச் சரத்து) பட்டியல்-II உடன் (அதிகார வரம்பின் தன்மை) பொருத்துக:\n\nபட்டியல்-I:\na) சரத்து 132\nb) சரத்து 133\nc) சரத்து 134\nd) சரத்து 134A\n\nபட்டியல்-II:\n1. முக்கிய சட்டக் கேள்வி அடங்கிய சிவில் வழக்குகள் மேல்முறையீடு\n2. உயர் நீதிமன்றத்தால் சான்றளிக்கப்பட்ட அரசியலமைப்பு வழக்குகள் மேல்முறையீடு\n3. மேல்முறையீட்டுச் சான்றிதழ் வழங்கும் உயர் நீதிமன்ற அதிகாரம்\n4. குற்றவியல் வழக்குகள் மேல்முறையீடு (மரண தண்டனை மாற்றம்/சான்றிதழ்)",
        {"A": "a-2, b-1, c-4, d-3", "B": "a-1, b-2, c-3, d-4", "C": "a-2, b-4, c-1, d-3", "D": "a-3, b-1, c-4, d-2"},
        {"A": "a-2, b-1, c-4, d-3", "B": "a-1, b-2, c-3, d-4", "C": "a-2, b-4, c-1, d-3", "D": "a-3, b-1, c-4, d-2"},
        "A",
        "Correct Match:\na) Article 132 -> Constitutional appeals (2)\nb) Article 133 -> Civil appeals (1)\nc) Article 134 -> Criminal appeals (4)\nd) Article 134A -> Certificate for appeal to Supreme Court (3)",
        "சரியான பொருத்தம்:\na) சரத்து 132 -> அரசியலமைப்பு மேல்முறையீடு (2)\nb) சரத்து 133 -> சிவில் மேல்முறையீடு (1)\nc) சரத்து 134 -> குற்றவியல் மேல்முறையீடு (4)\nd) சரத்து 134A -> மேல்முறையீட்டுச் சான்றிதழ் (3)",
        "Article 134A was inserted by the 44th Amendment Act, 1978 to streamline issuance of certificates by High Courts.",
        "சரத்து 134A என்பது 1978-ன் 44வது திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டது.",
        "In Criminal Appeals under Article 134(1)(a)&(b), an appeal lies AS OF RIGHT to SC if High Court reverses an acquittal and sentences accused to death.",
        "கீழ் நீதிமன்றத்தின் விடுதலையை உயர் நீதிமன்றம் ரத்து செய்து மரண தண்டனை விதித்தால், சரத்து 134-ன் கீழ் நேரடியாக உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்யலாம்.",
        "Civil Appeals under Art 133 no longer require a minimum monetary threshold (removed by 30th CAA 1972).",
        "சிவில் மேல்முறையீடுகளுக்கு குறைந்தபட்ச பண வரம்பு 30வது திருத்தம் 1972 மூலம் நீக்கப்பட்டது."))

    # Q20
    b1.append(mk_q(20, "Medium", "Direct",
        "The Supreme Court of India was inaugurated on January 28, 1950. How did its jurisdiction compare with its predecessor, the Federal Court of India established under the Government of India Act, 1935?",
        "இந்திய உச்ச நீதிமன்றம் ஜனவரி 28, 1950 அன்று தொடங்கப்பட்டது. 1935 இந்திய அரசாங்கச் சட்டத்தின் கீழ் அமைக்கப்பட்ட கூட்டாட்சி நீதிமன்றத்துடன் (Federal Court) ஒப்பிடும்போது உச்ச நீதிமன்றத்தின் அதிகார வரம்பு எவ்வாறு உள்ளது?",
        {"A": "Supreme Court has narrower jurisdiction than the Federal Court because appeals to Privy Council were retained", "B": "Supreme Court replaced both the Federal Court of India and the Judicial Committee of the Privy Council, having wider jurisdiction", "C": "Supreme Court has jurisdiction only over constitutional matters, whereas Federal Court heard all civil and criminal cases", "D": "Federal Court had supreme writ powers whereas Supreme Court does not have writ powers"},
        {"A": "பிரிவி கவுன்சில் மேல்முறையீடு நீடித்ததால் உச்ச நீதிமன்றத்திற்கு கூட்டாட்சி நீதிமன்றத்தை விட குறைந்த அதிகாரமே இருந்தது", "B": "உச்ச நீதிமன்றமானது கூட்டாட்சி நீதிமன்றம் மற்றும் பிரிவி கவுன்சில் ஆகிய இரண்டின் இடத்தையும் பிடித்து, பரந்த அதிகார வரம்பைப் பெற்றது", "C": "உச்ச நீதிமன்றத்திற்கு அரசியலமைப்பு வழக்குகளில் மட்டுமே அதிகாரம் உள்ளது, கூட்டாட்சி நீதிமன்றத்திற்கு அனைத்து வழக்குகளிலும் அதிகாரம் இருந்தது", "D": "கூட்டாட்சி நீதிமன்றத்திற்கு மேலான பேராணை அதிகாரம் இருந்தது, உச்ச நீதிமன்றத்திற்கு பேராணை அதிகாரம் இல்லை"},
        "B",
        "The Supreme Court succeeded the Federal Court of India (1937-1950). Under the Abolition of Privy Council Jurisdiction Act 1949, the SC also inherited the appellate jurisdiction of the British Privy Council, making it wider than the Federal Court.",
        "உச்ச நீதிமன்றம் கூட்டாட்சி நீதிமன்றத்தின் (1937-1950) இடத்தையும், 1949 பிரிவி கவுன்சில் ஒழிப்புச் சட்டத்தின் மூலம் பிரிவி கவுன்சிலின் மேல்முறையீட்டு அதிகாரத்தையும் பிடித்து, பரந்த அதிகார வரம்பைப் பெற்றது.",
        "The Federal Court of India had restricted appellate jurisdiction (appeals lay to Privy Council in London). SC abolished Privy Council appeals.",
        "கூட்டாட்சி நீதிமன்றத்திற்கு வரம்பிற்குட்பட்ட மேல்முறையீட்டு அதிகாரமே இருந்தது; லண்டன் பிரிவி கவுன்சிலுக்கு மேல்முறையீடு செய்ய வேண்டியிருந்தது.",
        "Article 135 allows SC to exercise jurisdiction over matters covered under Federal Court jurisdiction prior to Constitution.",
        "சரத்து 135 பழைய கூட்டாட்சி நீதிமன்ற அதிகார வரம்புகளை உச்ச நீதிமன்றம் தொடர அனுமதிக்கிறது.",
        "Inauguration date of Supreme Court: January 28, 1950 (Two days after Republic Day).",
        "உச்ச நீதிமன்றம் தொடங்கப்பட்ட நாள்: ஜனவரி 28, 1950."))

    # Q21
    b1.append(mk_q(21, "Hard", "Chronology",
        "Arrange the following landmark Supreme Court cases on Constitutional Amending Power and Fundamental Rights in chronological order:\n1. Sajjan Singh v. State of Rajasthan\n2. Golaknath v. State of Punjab\n3. Shankari Prasad v. Union of India\n4. Kesavananda Bharati v. State of Kerala",
        "அரசியலமைப்புச் திருத்த அதிகாரம் மற்றும் அடிப்படை உரிமைகள் தொடர்பான பின்வரும் உச்ச நீதிமன்ற மைல்கல் வழக்குகளைக் காலவரிசைப்படி அமைக்கவும்:\n1. சஜ்ஜன் சிங் எதிர் ராஜஸ்தான் மாநிலம்\n2. கோலக்நாத் எதிர் பஞ்சாப் மாநிலம்\n3. சங்கரி பிரசாத் எதிர் இந்திய யூனியன்\n4. கேசவானந்த பாரதி எதிர் கேரளா மாநிலம்",
        {"A": "3 -> 1 -> 2 -> 4", "B": "1 -> 3 -> 2 -> 4", "C": "3 -> 2 -> 1 -> 4", "D": "2 -> 3 -> 1 -> 4"},
        {"A": "3 -> 1 -> 2 -> 4", "B": "1 -> 3 -> 2 -> 4", "C": "3 -> 2 -> 1 -> 4", "D": "2 -> 3 -> 1 -> 4"},
        "A",
        "Chronological order of Cases:\n1. Shankari Prasad v. Union of India (1951) - 1st CAA upheld\n2. Sajjan Singh v. State of Rajasthan (1965) - 17th CAA upheld\n3. Golaknath v. State of Punjab (1967) - Fundamental Rights made unamendable\n4. Kesavananda Bharati v. State of Kerala (1973) - Basic Structure Doctrine established\nHence, 3 -> 1 -> 2 -> 4.",
        "வழக்குகளின் காலவரிசை:\n1. சங்கரி பிரசாத் வழக்கு (1951) - 1வது திருத்தம் செல்லுபடியானது\n2. சஜ்ஜன் சிங் வழக்கு (1965) - 17வது திருத்தம் செல்லுபடியானது\n3. கோலக்நாத் வழக்கு (1967) - அடிப்படை உரிமைகளைத் திருத்த முடியாது எனத் தீர்ப்பு\n4. கேசவானந்த பாரதி வழக்கு (1973) - அடிப்படை கட்டமைப்பு கோட்பாடு உருவாக்கம்\nஎனவே, 3 -> 1 -> 2 -> 4.",
        "Candidates confuse Golaknath (1967) and Sajjan Singh (1965). Sajjan Singh reaffirmed Shankari Prasad before Golaknath reversed both.",
        "கோலக்நாத் (1967) மற்றும் சஜ்ஜன் சிங் (1965) ஆண்டுகளை தேர்வர்கள் குழப்பிக்கொள்கிறார்கள்.",
        "Bench strengths: Shankari Prasad (5), Sajjan Singh (5), Golaknath (11), Kesavananda Bharati (13).",
        "நீதிபதிகள் அமர்வு எண்ணிக்கை: சங்கரி பிரசாத் (5), சஜ்ஜன் சிங் (5), கோலக்நாத் (11), கேசவானந்த பாரதி (13).",
        "Kesavananda Bharati is the largest constitutional bench in Indian legal history (13 judges, 7:6 majority).",
        "கேசவானந்த பாரதி வழக்கு இந்திய வரலாற்றிலேயே மிகப்பெரிய அமர்வாகும் (13 நீதிபதிகள்)."))

    # Q22
    b1.append(mk_q(22, "Medium", "Direct",
        "In the landmark Kesavananda Bharati Case (1973), by what majority did the 13-judge Constitutional Bench establish the 'Basic Structure Doctrine'?",
        "வரலாற்றுச் சிறப்புமிக்க கேசவானந்த பாரதி வழக்கில் (1973), 13 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு எந்த பெரும்பான்மையில் 'அடிப்படை கட்டமைப்பு கோட்பாட்டை' நிறுவியது?",
        {"A": "Unanimous (13:0)", "B": "7 : 6 Majority", "C": "11 : 2 Majority", "D": "9 : 4 Majority"},
        {"A": "ஒருமனதாக (13:0)", "B": "7 : 6 பெரும்பான்மை", "C": "11 : 2 பெரும்பான்மை", "D": "9 : 4 பெரும்பான்மை"},
        "B",
        "The Kesavananda Bharati judgment was delivered on April 24, 1973, by a narrow majority of 7 to 6. The 7 majority judges included Chief Justice S.M. Sikri.",
        "கேசவானந்த பாரதி தீர்ப்பு ஏப்ரல் 24, 1973 அன்று 7:6 என்ற குறுகிய பெரும்பான்மையில் தலைமை நீதிபதி எஸ்.எம். சிக்ரி தலைமையிலான அமர்வால் வழங்கப்பட்டது.",
        "Do not confuse Golaknath majority (6:5) with Kesavananda Bharati majority (7:6).",
        "கோலக்நாத் வழக்கின் பெரும்பான்மையையும் (6:5), கேசவானந்த பாரதி வழக்கின் பெரும்பான்மையையும் (7:6) குழப்பிக் கொள்ள வேண்டாம்.",
        "The judgment upheld 24th Amendment Act but ruled Parliament cannot alter the 'Basic Structure' of the Constitution.",
        "இத்தீர்ப்பு 24வது திருத்தத்தை ஏற்றுக் கொண்டது, ஆனால் அடிப்படை கட்டமைப்பை மாற்ற நாடாளுமன்றத்திற்கு அதிகாரம் இல்லை என்றது.",
        "April 24, 1973 is also remembered as Sachin Tendulkar's birthday (easy memory trick!).",
        "ஏப்ரல் 24, 1973 என்பது நினைவு கூரத்தக்க நாளாகும்."))

    # Q23
    b1.append(mk_q(23, "Hard", "Scenario",
        "In Minerva Mills v. Union of India (1980), which section of the 42nd Constitutional Amendment Act, 1976 that gave unlimited amending power to Parliament and excluded judicial review was struck down by the Supreme Court?",
        "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980) வழக்கில், நாடாளுமன்றத்திற்கு வரம்பற்ற திருத்த அதிகாரத்தை வழங்கி நீதித்துறை மறுஆய்வை விலக்கிய 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் எந்தப் பிரிவை உச்ச நீதிமன்றம் ரத்து செய்தது?",
        {"A": "Section 4 and Section 55 (Clauses 4 and 5 of Article 368)", "B": "Section 2 and Section 3", "C": "Section 51A", "D": "Section 31C in its entirety"},
        {"A": "பிரிவு 4 மற்றும் பிரிவு 55 (சரத்து 368-ன் உட்பிரிவுகள் 4 மற்றும் 5)", "B": "பிரிவு 2 மற்றும் பிரிவு 3", "C": "பிரிவு 51A", "D": "பிரிவு 31C முழுமையாக"},
        "A",
        "In Minerva Mills (1980), the SC struck down Clauses (4) and (5) of Article 368 (inserted by Sec 55 of 42nd CAA) which declared no constitutional amendment could be questioned in any court. SC held Judicial Review and Limited Amending Power are Basic Features.",
        "மினர்வா மில்ஸ் (1980) வழக்கில், அரசியலமைப்புத் திருத்தங்களை நீதிமன்றத்தில் கேள்வி கேட்க முடியாது என்ற சரத்து 368(4) மற்றும் (5)-ஐ உச்ச நீதிமன்றம் ரத்து செய்தது. நீதித்துறை மறுஆய்வும், வரம்பிற்குட்பட்ட திருத்த அதிகாரமும் அடிப்படை அம்சங்கள் என அறிவித்தது.",
        "Parliament has limited amending power; it cannot convert a limited amending power into an absolute power.",
        "நாடாளுமன்றத்திற்கு வரம்பிற்குட்பட்ட திருத்த அதிகாரமே உள்ளது; அதை வரம்பற்ற அதிகாரமாக மாற்ற முடியாது.",
        "Minerva Mills established a harmony between Fundamental Rights (Part III) and DPSP (Part IV).",
        "மினர்வா மில்ஸ் வழக்கு அடிப்படை உரிமைகளுக்கும் வழிகாட்டு நெறிமுறைகளுக்கும் இடையே இணக்கத்தை ஏற்படுத்தியது.",
        "Judicial Review is a pillar of Indian Constitutionalism.",
        "நீதித்துறை மறுஆய்வு இந்திய அரசியலமைப்பின் முக்கியத் தூணாகும்."))

    # Q24
    b1.append(mk_q(24, "Medium", "Direct",
        "Public Interest Litigation (PIL) in India originated through judicial innovation. Who among the following Supreme Court Judges are regarded as the key pioneers of PIL in India?",
        "இந்தியாவில் பொது நல வழக்கு (PIL) நீதித்துறையின் புதிய முயற்சியால் உருவானது. இந்தியாவில் PIL-ன் முன்னோடிகளாகக் கருதப்படும் உச்ச நீதிமன்ற நீதிபதிகள் யார்?",
        {"A": "Justice H.J. Kania and Justice Patanjali Sastri", "B": "Justice V.R. Krishna Iyer and Justice P.N. Bhagwati", "C": "Justice A.N. Ray and Justice M.U. Beg", "D": "Justice Y.V. Chandrachud and Justice R.S. Pathak"},
        {"A": "நீதிபதி எச்.ஜே. கானியா மற்றும் நீதிபதி பதஞ்சலி சாஸ்திரி", "B": "நீதிபதி வி.ஆர். கிருஷ்ணய்யர் மற்றும் நீதிபதி பி.என். பகவதி", "C": "நீதிபதி ஏ.என். ரே மற்றும் நீதிபதி எம்.யு. பேக்", "D": "நீதிபதி ஒய்.வி. சந்திரசூட் மற்றும் நீதிபதி ஆர்.எஸ். பாடக்"},
        "B",
        "Justices V.R. Krishna Iyer and P.N. Bhagwati were the pioneers of Public Interest Litigation (PIL) in the late 1970s and early 1980s (S.P. Gupta case 1981), relaxing the traditional rule of Locus Standi.",
        "1970-களின் இறுதியில் மற்றும் 1980-களின் தொடக்கத்தில் (எஸ்.பி. குப்தா வழக்கு 1981) பாரம்பரிய 'பாதிக்கப்பட்ட நபரே வழக்கிட வேண்டும்' (Locus Standi) என்ற விதியைத் தளர்த்தி, நீதிபதிகள் வி.ஆர். கிருஷ்ணய்யர் மற்றும் பி.என். பகவதி பொது நல வழக்கை உருவாக்கினர்.",
        "S.P. Gupta v. Union of India (1981) is also known as the First Judges Case and PIL Case.",
        "எஸ்.பி. குப்தா வழக்கு (1981) முதல் நீதிபதிகள் வழக்கு என்றும் பொது நல வழக்கு என்றும் அழைக்கப்படுகிறது.",
        "Epistolary Jurisdiction means treating a postcard or letter from a citizen as a writ petition.",
        "கடிதம் அல்லது அஞ்சல் அட்டையை மனுவாக ஏற்றுக்கொள்வது கடித அதிகார வரம்பு (Epistolary Jurisdiction) எனப்படும்.",
        "PIL originated in the USA in the 1960s as 'Public Interest Law'.",
        "பொது நல வழக்கு முதன்முதலில் 1960-களில் அமெரிக்காவில் தோன்றியது."))

    # Q25
    b1.append(mk_q(25, "Hard", "Scenario",
        "Under Article 139A of the Constitution (Transfer of Cases), under what circumstances can the Supreme Court withdraw cases pending before High Courts to itself?",
        "சரத்து 139A (வழக்குகள் இடமாற்றம்)-ன் கீழ் எந்த சூழ்நிலைகளில் உச்ச நீதிமன்றம் உயர் நீதிமன்றங்களில் நிலுவையில் உள்ள வழக்குகளைத் தன்பால் மாற்றிக் கொள்ள முடியும்?",
        {"A": "If cases involving the same or substantially the same questions of law are pending before the Supreme Court and one or more High Courts, and the SC is satisfied that such questions are substantial questions of general importance", "B": "If any political party submits a petition to the Chief Justice of India", "C": "Only if the High Court voluntarily surrenders its jurisdiction", "D": "Only during a National Emergency under Article 352"},
        {"A": "ஒரே மாதிரியான அல்லது சாரம்சத்தில் ஒரே சட்டக் கேள்விகள் உச்ச நீதிமன்றத்திலும் ஒன்றுக்கு மேற்பட்ட உயர் நீதிமன்றங்களிலும் நிலுவையில் இருந்து, அவை பொது முக்கியத்துவம் வாய்ந்தவை என உச்ச நீதிமன்றம் திருப்தியடைந்தால்", "B": "ஏதேனும் ஓர் அரசியல் கட்சி இந்தியத் தலைமை நீதிபதியிடம் மனு சமர்ப்பித்தால்", "C": "உயர் நீதிமன்றம் தன் அதிகார வரம்பைத் தானாக முன்வந்து துறந்தால் மட்டுமே", "D": "சரத்து 352 தேசிய அவசரநிலையின் போது மட்டுமே"},
        "A",
        "Article 139A(1) was inserted by the 42nd Amendment Act, 1976 (modified by 44th CAA 1978). It allows SC to withdraw cases involving same/substantially same questions of law from HCs to itself, acting on application of Attorney General or on its own motion.",
        "சரத்து 139A(1) என்பது 1976-ன் 42வது திருத்தத்தின் மூலம் சேர்க்கப்பட்டது. ஒரே மாதிரியான சட்டக் கேள்வி நிலுவையில் இருந்தால், தலைமை வழக்கறிஞர் மனுவின் பேரிலோ அல்லது தானாக முன்வந்தோ உச்ச நீதிமன்றம் வழக்குகளைத் தன்பால் மாற்றலாம்.",
        "Article 139A(2) also allows SC to transfer any case/appeal from one High Court to another High Court in the interest of justice.",
        "சரத்து 139A(2) ஒரு உயர் நீதிமன்றத்திலிருந்து மற்றொரு உயர் நீதிமன்றத்திற்கு வழக்குகளை மாற்ற உச்ச நீதிமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Attorney General of India or an aggrieved party can apply under Article 139A.",
        "இந்திய தலைமை வழக்கறிஞரும் சரத்து 139A-ன் கீழ் விண்ணப்பிக்கலாம்.",
        "Article 139A ensures uniform interpretation of national laws.",
        "சரத்து 139A தேசிய சட்டங்களில் சீரான விளக்கத்தை உறுதி செய்கிறது."))

    return b1

if __name__ == "__main__":
    b1 = get_block1()
    print(f"Block 1 loaded with {len(b1)} questions.")
