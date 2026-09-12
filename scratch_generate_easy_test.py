import json

def create_easy_questions():
    questions = []
    
    # 1. CM_E_001 (A)
    questions.append({
        "id": "CM_E_001",
        "subject": "Polity",
        "topic": "Chief Minister & State Council of Ministers",
        "difficulty": "Easy",
        "question_type": "Easy",
        "question": {
            "en": "Which Article of the Indian Constitution provides for a Council of Ministers with the Chief Minister at the head to aid and advise the Governor?",
            "ta": "ஆளுநருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரை தலைவராகக் கொண்ட அமைச்சரவை அமைப்பதற்கு வழிவகை செய்யும் இந்திய அரசியலமைப்பு உறுப்பு எது?"
        },
        "question_en": "Which Article of the Indian Constitution provides for a Council of Ministers with the Chief Minister at the head to aid and advise the Governor?",
        "question_ta": "ஆளுநருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரை தலைவராகக் கொண்ட அமைச்சரவை அமைப்பதற்கு வழிவகை செய்யும் இந்திய அரசியலமைப்பு உறுப்பு எது?",
        "options": [
            {"id": "A", "en": "Article 163", "ta": "உறுப்பு 163"},
            {"id": "B", "en": "Article 164", "ta": "உறுப்பு 164"},
            {"id": "C", "en": "Article 167", "ta": "உறுப்பு 167"},
            {"id": "D", "en": "Article 169", "ta": "உறுப்பு 169"}
        ],
        "options_en": ["Article 163", "Article 164", "Article 167", "Article 169"],
        "options_ta": ["உறுப்பு 163", "உறுப்பு 164", "உறுப்பு 167", "உறுப்பு 169"],
        "correct_answer": "A",
        "answer": "a",
        "explanation": {
            "en": "Article 163(1) mandates that there shall be a Council of Ministers with the Chief Minister at the head to aid and advise the Governor in the exercise of his functions, except in matters where the Governor acts in discretion.",
            "ta": "உறுப்பு 163(1)-ன்படி, ஆளுநர் தனது விருப்புரிமை அதிகாரங்களைத் தவிர மற்ற பணிகளை நிறைவேற்ற அவருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரைத் தலைவராகக் கொண்ட அமைச்சரவை ஒன்று இருக்க வேண்டும்."
        },
        "explanation_en": "Article 163(1) mandates that there shall be a Council of Ministers with the Chief Minister at the head to aid and advise the Governor in the exercise of his functions, except in matters where the Governor acts in discretion.",
        "explanation_ta": "உறுப்பு 163(1)-ன்படி, ஆளுநர் தனது விருப்புரிமை அதிகாரங்களைத் தவிர மற்ற பணிகளை நிறைவேற்ற அவருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரைத் தலைவராகக் கொண்ட அமைச்சரவை ஒன்று இருக்க வேண்டும்.",
        "why_not_others": {
            "A": {"en": "Correct. Article 163 provides for aid and advice of Council of Ministers to Governor.", "ta": "சரி. உறுப்பு 163 ஆளுநருக்கு அமைச்சரவையின் உதவி மற்றும் ஆலோசனையைக் குறிப்பிடுகிறது."},
            "B": {"en": "Incorrect. Article 164 deals with appointment, tenure, responsibility, oath, and salaries of Ministers.", "ta": "தவறு. உறுப்பு 164 அமைச்சர்களின் நியமனம், பதவிக்காலம், பொறுப்புடைமை, உறுதிமொழி மற்றும் ஊதியங்களைக் கையாள்கிறது."},
            "C": {"en": "Incorrect. Article 167 specifies the duties of Chief Minister with respect to furnishing information to Governor.", "ta": "தவறு. உறுப்பு 167 ஆளுநருக்குத் தகவல் தெரிவிப்பதில் முதலமைச்சரின் கடமைகளைக் குறிப்பிடுகிறது."},
            "D": {"en": "Incorrect. Article 169 deals with creation or abolition of Legislative Councils in States.", "ta": "தவறு. உறுப்பு 169 மாநிலங்களில் சட்ட மேலவைகளை உருவாக்குதல் அல்லது நீக்குதலைக் கையாள்கிறது."}
        },
        "tnpsc_tip": {
            "en": "Article 163 at the State level corresponds to Article 74 at the Union level.",
            "ta": "மாநில அளவில் உறுப்பு 163 என்பது மத்திய அளவில் உறுப்பு 74-க்கு இணையானதாகும்."
        },
        "revision_fact": {
            "en": "Article 163 mandates the Council of Ministers with CM at the head to aid and advise the Governor.",
            "ta": "ஆளுநருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரைத் தலைவராகக் கொண்ட அமைச்சரவை இருக்க வேண்டும் என உறுப்பு 163 கூறுகிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Chief Minister", "State Council of Ministers", "Polity"]
    })

    # 2. CM_E_002 (B)
    questions.append({
        "id": "CM_E_002",
        "subject": "Polity",
        "topic": "Chief Minister & State Council of Ministers",
        "difficulty": "Easy",
        "question_type": "Easy",
        "question": {
            "en": "Under Article 164(1) of the Indian Constitution, who appoints the Chief Minister of a State?",
            "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 164(1)-ன் கீழ், ஒரு மாநிலத்தின் முதலமைச்சரை நியமிப்பவர் யார்?"
        },
        "question_en": "Under Article 164(1) of the Indian Constitution, who appoints the Chief Minister of a State?",
        "question_ta": "இந்திய அரசியலமைப்பின் உறுப்பு 164(1)-ன் கீழ், ஒரு மாநிலத்தின் முதலமைச்சரை நியமிப்பவர் யார்?",
        "options": [
            {"id": "A", "en": "President of India", "ta": "இந்தியக் குடியரசுத் தலைவர்"},
            {"id": "B", "en": "Governor of the State", "ta": "மாநில ஆளுநர்"},
            {"id": "C", "en": "Speaker of the Legislative Assembly", "ta": "சட்டமன்றப் பேரவைத் தலைவர்"},
            {"id": "D", "en": "Chief Justice of the High Court", "ta": "உயர் நீதிமன்றத் தலைமை நீதிபதி"}
        ],
        "options_en": ["President of India", "Governor of the State", "Speaker of the Legislative Assembly", "Chief Justice of the High Court"],
        "options_ta": ["இந்தியக் குடியரசுத் தலைவர்", "மாநில ஆளுநர்", "சட்டமன்றப் பேரவைத் தலைவர்", "உயர் நீதிமன்றத் தலைமை நீதிபதி"],
        "correct_answer": "B",
        "answer": "b",
        "explanation": {
            "en": "Article 164(1) provides that the Chief Minister shall be appointed by the Governor, and the other Ministers shall be appointed by the Governor on the advice of the Chief Minister.",
            "ta": "உறுப்பு 164(1)-ன்படி, முதலமைச்சர் ஆளுநரால் நியமிக்கப்படுவார், மேலும் பிற அமைச்சர்கள் முதலமைச்சரின் ஆலோசனையின் பேரில் ஆளுநரால் நியமிக்கப்படுவார்கள்."
        },
        "explanation_en": "Article 164(1) provides that the Chief Minister shall be appointed by the Governor, and the other Ministers shall be appointed by the Governor on the advice of the Chief Minister.",
        "explanation_ta": "உறுப்பு 164(1)-ன்படி, முதலமைச்சர் ஆளுநரால் நியமிக்கப்படுவார், மேலும் பிற அமைச்சர்கள் முதலமைச்சரின் ஆலோசனையின் பேரில் ஆளுநரால் நியமிக்கப்படுவார்கள்.",
        "why_not_others": {
            "A": {"en": "Incorrect. President appoints Prime Minister and Union Ministers, not State Chief Ministers.", "ta": "தவறு. குடியரசுத் தலைவர் பிரதமரையும் மத்திய அமைச்சர்களையும் நியமிக்கிறார், மாநில முதலமைச்சரை அல்ல."},
            "B": {"en": "Correct. Governor appoints the Chief Minister under Article 164(1).", "ta": "சரி. உறுப்பு 164(1)-ன் கீழ் ஆளுநர் முதலமைச்சரை நியமிக்கிறார்."},
            "C": {"en": "Incorrect. Speaker presides over Legislative Assembly sessions.", "ta": "தவறு. சபாநாயகர் சட்டமன்றப் பேரவைக் கூட்டங்களைத் தலைமை தாங்குகிறார்."},
            "D": {"en": "Incorrect. Chief Justice of High Court administers oath of office to the Governor.", "ta": "தவறு. உயர் நீதிமன்றத் தலைமை நீதிபதி ஆளுநருக்குப் பதவிப் பிரமாணம் செய்து வைக்கிறார்."}
        },
        "tnpsc_tip": {
            "en": "Remember: Appointment of CM is by Governor (Art 164(1)); Appointment of PM is by President (Art 75(1)).",
            "ta": "நினைவில் கொள்க: முதலமைச்சர் ஆளுநரால் நியமிக்கப்படுகிறார் (உறுப்பு 164(1)); பிரதமர் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார் (உறுப்பு 75(1))."
        },
        "revision_fact": {
            "en": "The Governor appoints the Chief Minister under Article 164(1).",
            "ta": "உறுப்பு 164(1)-ன் கீழ் ஆளுநர் முதலமைச்சரை நியமிக்கிறார்."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Chief Minister", "State Council of Ministers", "Polity"]
    })

    return questions

if __name__ == "__main__":
    q_list = create_easy_questions()
    print(f"Generated {len(q_list)} test questions.")
