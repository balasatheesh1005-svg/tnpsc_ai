# -*- coding: utf-8 -*-
"""
Full Supreme Court Grand Test 100 Questions Generator
Outputs to data/questions/polity/supreme_court_grand_test.json
"""

import json
import os
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

def build_and_save_dataset():
    output_path = "data/questions/polity/supreme_court_grand_test.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

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

    raw = []

    # 1
    raw.append(("POLITY_SC_GT_001", "Medium", "Statement",
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

    # 2
    raw.append(("POLITY_SC_GT_002", "Easy", "Direct",
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

    questions = [q(*item) for item in raw]
    print(f"Base questions: {len(questions)}")
    return questions

if __name__ == "__main__":
    build_and_save_dataset()
