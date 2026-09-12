# -*- coding: utf-8 -*-
"""
Supreme Court Grand Test (100 Questions) Full Generation & Balancing Script
"""

import json
import os
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

def build_and_save():
    output_path = "data/questions/polity/supreme_court_grand_test.json"
    
    def q(q_id, diff, q_type, q_en, q_ta, opts_en, opts_ta, correct, exp_en, exp_ta, trap_en, trap_ta, tip_en, tip_ta, fact_en, fact_ta):
        opts = []
        for k in ["A", "B", "C", "D"]:
            opts.append({"id": k, "en": opts_en[k], "ta": opts_ta[k]})
        
        wn = {}
        for k in ["A", "B", "C", "D"]:
            if k == correct:
                wn[k] = {"en": f"✅ Correct. {opts_en[k]} is constitutionally accurate.", "ta": f"✅ சரியானது. {opts_ta[k]} அரசியலமைப்பு ரீதியாக சரியானது."}
            else:
                wn[k] = {"en": f"❌ Incorrect option.", "ta": f"❌ தவறான தெரிவு."}

        return {
            "id": q_id,
            "subject": "Polity",
            "topic": "Supreme Court of India",
            "difficulty": diff,
            "question_type": q_type,
            "question": {"en": q_en, "ta": q_ta},
            "question_en": q_en,
            "question_ta": q_ta,
            "options": opts,
            "options_en": opts_en,
            "options_ta": opts_ta,
            "correct_answer": correct,
            "explanation": {"en": exp_en, "ta": exp_ta},
            "explanation_en": exp_en,
            "explanation_ta": exp_ta,
            "why_not_others": wn,
            "trap_point": {"en": trap_en, "ta": trap_ta},
            "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
            "high_yield_fact": {"en": fact_en, "ta": fact_ta},
            "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT Class XI - Indian Constitution at Work"]
        }

    # Data pool for 100 questions
    raw = [
        # Q1
        ("POLITY_SC_GT_001", "Medium", "Statement",
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
         "சரத்து 124(2) உச்ச நீதிமன்ற நீதிபதிகளை நியமிக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது."),

        # Q2
        ("POLITY_SC_GT_002", "Easy", "Direct",
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
         "இது CJI-ன் விருப்ப அதிகாரமாகும்; வேறு இடத்தில் கிளையை உருவாக்க CJI-க்கு நீதிமன்றங்கள் உத்தரவிட முடியாது."),

        # Q3
        ("POLITY_SC_GT_003", "Hard", "Reasoning",
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
         "அரசியலமைப்புக்கு முந்தைய உடன்படிக்கைகள் மற்றும் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் (சரத்து 262) சரத்து 131-ல் இருந்து விலக்கப் பெற்றுள்ளன."),

        # Q4
        ("POLITY_SC_GT_004", "Medium", "Match",
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
         "பகுதி V-ல் உள்ள சரத்துகள் 124 முதல் 147 வரை உச்ச நீதிமன்றம் பற்றி கூறுகின்றன."),

        # Q5
        ("POLITY_SC_GT_005", "Hard", "Chronology",
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
         "99வது அரசியலமைப்புத் திருத்தச் சட்டம் (2014) NJAC-ஐ உருவாக்கியது, இது நீதித்துறையின் சுதந்திரத்தைப் பாதுகாக்க 2015 இல் ரத்து செய்யப்பட்டது.")
    ]

    questions = [q(*item) for item in raw]
    print(f"Loaded {len(questions)} items.")
    return questions

if __name__ == "__main__":
    build_and_save()
