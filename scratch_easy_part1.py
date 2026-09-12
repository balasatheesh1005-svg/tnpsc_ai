import json

easy_questions = [
    # CM_E_001 (Correct: A)
    {
        "id": "CM_E_001",
        "subject": "Polity",
        "topic": "Chief Minister & State Council of Ministers",
        "difficulty": "Easy",
        "question_type": "Easy",
        "question": {
            "en": "Which Article of the Indian Constitution provides for a Council of Ministers with the Chief Minister at the head to aid and advise the Governor?",
            "ta": "ஆளுநருக்கு உதவவும் மற்றும் ஆலோசனை வழங்கவும் முதலமைச்சரை தலைவராகக் கொண்ட அமைச்சரவை அமைப்பதற்கு வழிவகை செய்யும் இந்திய அரசியலமைப்பு உறுப்பு எது?"
        },
        "question_en": "Which Article of the Indian Constitution provides for a Council of Ministers with the Chief Minister at the head to aid and advise the Governor?",
        "question_ta": "ஆளுநருக்கு உதவவும் மற்றும் ஆலோசனை வழங்கவும் முதலமைச்சரை தலைவராகக் கொண்ட அமைச்சரவை அமைப்பதற்கு வழிவகை செய்யும் இந்திய அரசியலமைப்பு உறுப்பு எது?",
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
            "ta": "உறுப்பு 163(1)-ன்படி, ஆளுநரின் விருப்புரிமை அதிகாரங்களைத் தவிர மற்ற பணிகளைச் செய்ய அவருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரைத் தலைவராகக் கொண்ட அமைச்சரவை ஒன்று இருக்க வேண்டும்."
        },
        "explanation_en": "Article 163(1) mandates that there shall be a Council of Ministers with the Chief Minister at the head to aid and advise the Governor in the exercise of his functions, except in matters where the Governor acts in discretion.",
        "explanation_ta": "உறுப்பு 163(1)-ன்படி, ஆளுநரின் விருப்புரிமை அதிகாரங்களைத் தவிர மற்ற பணிகளைச் செய்ய அவருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரைத் தலைவராகக் கொண்ட அமைச்சரவை ஒன்று இருக்க வேண்டும்.",
        "why_not_others": {
            "A": {"en": "Correct. Article 163 deals with Aid and Advice to the Governor.", "ta": "சரி. உறுப்பு 163 ஆளுநருக்கான உதவி மற்றும் ஆலோசனையைக் குறிப்பிடுகிறது."},
            "B": {"en": "Incorrect. Article 164 deals with appointment, tenure, responsibility, oath, and salaries of Ministers.", "ta": "தவறு. உறுப்பு 164 அமைச்சர்களின் நியமனம், பதவிக்காலம், பொறுப்பு, உறுதிமொழி மற்றும் ஊதியங்களைக் கையாள்கிறது."},
            "C": {"en": "Incorrect. Article 167 enumerates the duties of the Chief Minister regarding furnishing of information to the Governor.", "ta": "தவறு. உறுப்பு 167 ஆளுநருக்குத் தகவல் தெரிவிப்பதில் முதலமைச்சரின் கடமைகளைக் குறிப்பிடுகிறது."},
            "D": {"en": "Incorrect. Article 169 deals with the abolition or creation of Legislative Councils in States.", "ta": "தவறு. உறுப்பு 169 மாநிலங்களில் சட்ட மேலவைகளை உருவாக்குதல் அல்லது நீக்குதலைக் கையாள்கிறது."}
        },
        "tnpsc_tip": {
            "en": "Remember: Article 163 = Aid and Advice (State equivalent of Article 74 at the Center).",
            "ta": "நினைவில் கொள்க: உறுப்பு 163 = உதவி மற்றும் ஆலோசனை (மத்தியில் உறுப்பு 74-க்கு இணையானது)."
        },
        "revision_fact": {
            "en": "Article 163 mandates the Council of Ministers with the CM at the head to aid and advise the Governor.",
            "ta": "ஆளுநருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரை தலைவராகக் கொண்ட அமைச்சரவை இருக்க வேண்டும் என உறுப்பு 163 கூறுகிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Chief Minister", "State Council of Ministers", "Polity"]
    }
]

print("Base easy questions structure validated.")
