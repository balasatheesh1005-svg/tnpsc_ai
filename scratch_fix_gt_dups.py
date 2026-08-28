import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

gt_path = 'data/questions/polity/president_grand_test.json'
with open(gt_path, 'r', encoding='utf-8') as f:
    gt_data = json.load(f)

replacements = {
    'POLITY_PRESIDENT_GT_082': {
        "id": "POLITY_PRESIDENT_GT_082",
        "subject": "Polity",
        "topic": "President",
        "difficulty": "hard",
        "question_type": "MCQ",
        "question": {
            "en": "In which landmark case did the Supreme Court rule that successive re-promulgation of ordinances without placing them before the legislature is a colorable exercise of power and unconstitutional?",
            "ta": "சட்டமன்றத்தின் முன் வைக்காமல் அவசரச் சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது அரசியலமைப்புக்கு எதிரான அதிகார அத்துமீறல் என்று உச்ச நீதிமன்றம் எந்த முக்கிய வழக்கில் தீர்ப்பளித்தது?"
        },
        "question_en": "In which landmark case did the Supreme Court rule that successive re-promulgation of ordinances without placing them before the legislature is a colorable exercise of power and unconstitutional?",
        "question_ta": "சட்டமன்றத்தின் முன் வைக்காமல் அவசரச் சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது அரசியலமைப்புக்கு எதிரான அதிகார அத்துமீறல் என்று உச்ச நீதிமன்றம் எந்த முக்கிய வழக்கில் தீர்ப்பளித்தது?",
        "options": [
            {
                "id": "A",
                "en": "D.C. Wadhwa v. State of Bihar (1987)",
                "ta": "D.C. வாத்வா எதிர் பீகார் மாநிலம் (1987)"
            },
            {
                "id": "B",
                "en": "S.R. Bommai v. Union of India (1994)",
                "ta": "S.R. பொம்மை எதிர் இந்திய யூனியன் (1994)"
            },
            {
                "id": "C",
                "en": "Kehar Singh v. Union of India (1988)",
                "ta": "கேஹர் சிங் எதிர் இந்திய யூனியன் (1988)"
            },
            {
                "id": "D",
                "en": "Shamsher Singh v. State of Punjab (1974)",
                "ta": "ஷாம்ஷேர் சிங் எதிர் பஞ்சாப் மாநிலம் (1974)"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "In D.C. Wadhwa v. State of Bihar (1987), the Supreme Court ruled that re-promulgating ordinances without getting them passed by the legislature is a fraud on the Constitution and unconstitutional.",
            "ta": "D.C. வாத்வா எதிர் பீகார் மாநிலம் (1987) வழக்கில், சட்டமன்றத்தின் ஒப்புதல் பெறாமல் அவசரச் சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது அரசியலமைப்பை ஏமாற்றும் செயலாகும் மற்றும் செல்லாதது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "explanation_en": "In D.C. Wadhwa v. State of Bihar (1987), the Supreme Court ruled that re-promulgating ordinances without getting them passed by the legislature is a fraud on the Constitution and unconstitutional.",
        "explanation_ta": "D.C. வாத்வா எதிர் பீகார் மாநிலம் (1987) வழக்கில், சட்டமன்றத்தின் ஒப்புதல் பெறாமல் அவசரச் சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது அரசியலமைப்பை ஏமாற்றும் செயலாகும் மற்றும் செல்லாதது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "source_reference": "President Part 2 Notes - Section 5 (Ordinance Power)",
        "trap_point": {
            "en": "Do not confuse D.C. Wadhwa case (Ordinances) with S.R. Bommai case (President's Rule Article 356).",
            "ta": "D.C. வாத்வா வழக்கை (அவசரச்சட்டம்) S.R. பொம்மை வழக்குடன் (உறுப்பு 356 குடியரசுத் தலைவர் ஆட்சி) குழப்பிக் கொள்ள வேண்டாம்."
        }
    },
    'POLITY_PRESIDENT_GT_083': {
        "id": "POLITY_PRESIDENT_GT_083",
        "subject": "Polity",
        "topic": "President",
        "difficulty": "medium",
        "question_type": "MCQ",
        "question": {
            "en": "Under Article 60 of the Indian Constitution, what is the specific oath taken by the President of India upon assuming office?",
            "ta": "இந்திய அரசியலமைப்பின் 60-வது உறுப்பின் கீழ், குடியரசுத் தலைவர் பதவியேற்கும் போது ஏற்கும் குறிப்பிட்ட உறுதிமொழி யாது?"
        },
        "question_en": "Under Article 60 of the Indian Constitution, what is the specific oath taken by the President of India upon assuming office?",
        "question_ta": "இந்திய அரசியலமைப்பின் 60-வது உறுப்பின் கீழ், குடியரசுத் தலைவர் பதவியேற்கும் போது ஏற்கும் குறிப்பிட்ட உறுதிமொழி யாது?",
        "options": [
            {
                "id": "A",
                "en": "To preserve, protect and defend the Constitution and the law",
                "ta": "அரசியலமைப்பு மற்றும் சட்டத்தைப் பேணிப் பாதுகாத்து அரணாக நிற்பேன்"
            },
            {
                "id": "B",
                "en": "To bear true faith and allegiance to the Constitution of India",
                "ta": "இந்திய அரசியலமைப்பிற்கு உண்மையாகவும் விசுவாசமாகவும் இருப்பேன்"
            },
            {
                "id": "C",
                "en": "To maintain the secrecy of official proceedings",
                "ta": "அதிகாரப்பூர்வ நடவடிக்கைகளின் ரகசியத்தைக் காப்பேன்"
            },
            {
                "id": "D",
                "en": "To uphold the sovereignty and integrity of India only",
                "ta": "இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாட்டை மட்டுமே நிலைநிறுத்துவேன்"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Under Article 60, the President swears to faithfully execute the office, preserve, protect and defend the Constitution and the law, and devote himself to the service and well-being of the people.",
            "ta": "உறுப்பு 60-ன் கீழ், குடியரசுத் தலைவர் தனது பணியைச் செவ்வனே செய்யவும், அரசியலமைப்பு மற்றும் சட்டத்தைப் பேணிப் பாதுகாத்து அரணாக நிற்கவும், மக்களின் சேவை மற்றும் நலனுக்குத் தன்னை அர்ப்பணிக்கவும் உறுதிமொழி ஏற்கிறார்."
        },
        "explanation_en": "Under Article 60, the President swears to faithfully execute the office, preserve, protect and defend the Constitution and the law, and devote himself to the service and well-being of the people.",
        "explanation_ta": "உறுப்பு 60-ன் கீழ், குடியரசுத் தலைவர் தனது பணியைச் செவ்வனே செய்யவும், அரசியலமைப்பு மற்றும் சட்டத்தைப் பேணிப் பாதுகாத்து அரணாக நிற்கவும், மக்களின் சேவை மற்றும் நலனுக்குத் தன்னை அர்ப்பணிக்கவும் உறுதிமொழி ஏற்கிறார்.",
        "source_reference": "President Part 1 Notes - Section 7 (Oath Article 60)",
        "trap_point": {
            "en": "Only the President and Governor take oath to 'preserve, protect and defend' the Constitution. Ministers and MPs take oath of 'allegiance' to the Constitution.",
            "ta": "குடியரசுத் தலைவரும் ஆளுநரும் மட்டுமே அரசியலமைப்பைப் 'பேணிப் பாதுகாக்கும்' உறுதிமொழி ஏற்கின்றனர். அமைச்சர்களும் எம்பிக்களும் அரசியலமைப்பிற்கு 'விசுவாசமாக' இருக்கும் உறுதிமொழி ஏற்கின்றனர்."
        }
    },
    'POLITY_PRESIDENT_GT_085': {
        "id": "POLITY_PRESIDENT_GT_085",
        "subject": "Polity",
        "topic": "President",
        "difficulty": "hard",
        "question_type": "MCQ",
        "question": {
            "en": "What population census data is currently used to calculate the value of vote of an MLA for Presidential elections until the year 2026?",
            "ta": "2026 ஆம் ஆண்டு வரை குடியரசுத் தலைவர் தேர்தலுக்கான சட்டமன்ற உறுப்பினரின் (MLA) வாக்கின் மதிப்பைத் கணக்கிட தற்போது எந்த மக்கள் தொகை கணக்கெடுப்பு தரவு பயன்படுத்தப்படுகிறது?"
        },
        "question_en": "What population census data is currently used to calculate the value of vote of an MLA for Presidential elections until the year 2026?",
        "question_ta": "2026 ஆம் ஆண்டு வரை குடியரசுத் தலைவர் தேர்தலுக்கான சட்டமன்ற உறுப்பினரின் (MLA) வாக்கின் மதிப்பைத் கணக்கிட தற்போது எந்த மக்கள் தொகை கணக்கெடுப்பு தரவு பயன்படுத்தப்படுகிறது?",
        "options": [
            {
                "id": "A",
                "en": "1971 Census",
                "ta": "1971 மக்கள் தொகை கணக்கெடுப்பு"
            },
            {
                "id": "B",
                "en": "1991 Census",
                "ta": "1991 மக்கள் தொகை கணக்கெடுப்பு"
            },
            {
                "id": "C",
                "en": "2001 Census",
                "ta": "2001 மக்கள் தொகை கணக்கெடுப்பு"
            },
            {
                "id": "D",
                "en": "2011 Census",
                "ta": "2011 மக்கள் தொகை கணக்கெடுப்பு"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "As per the 84th Constitutional Amendment Act 2001, the population figures of the 1971 Census continue to be used for determining the value of votes in Presidential elections until the first census after 2026.",
            "ta": "84-வது அரசியலமைப்பு திருத்தச் சட்டம் 2001-ன் படி, 2026-க்குப் பிந்தைய முதல் மக்கள் தொகை கணக்கெடுப்பு வரை குடியரசுத் தலைவர் தேர்தலில் வாக்கு மதிப்பைக் கணக்கிட 1971-ம் ஆண்டின் மக்கள் தொகை கணக்கெடுப்பே பயன்படுத்தப்படுகிறது."
        },
        "explanation_en": "As per the 84th Constitutional Amendment Act 2001, the population figures of the 1971 Census continue to be used for determining the value of votes in Presidential elections until the first census after 2026.",
        "explanation_ta": "84-வது அரசியலமைப்பு திருத்தச் சட்டம் 2001-ன் படி, 2026-க்குப் பிந்தைய முதல் மக்கள் தொகை கணக்கெடுப்பு வரை குடியரசுத் தலைவர் தேர்தலில் வாக்கு மதிப்பைக் கணக்கிட 1971-ம் ஆண்டின் மக்கள் தொகை கணக்கெடுப்பே பயன்படுத்தப்படுகிறது.",
        "source_reference": "President Part 1 Notes - Section 3 (Value of Votes Article 55)",
        "trap_point": {
            "en": "Do not confuse the 1971 census (used for vote value calculation until 2026) with the 2001 census (used for delimitation of constituencies).",
            "ta": "வாக்கு மதிப்பு கணக்கீட்டிற்குப் பயன்படும் 1971 கணக்கெடுப்பை, தொகுதி மறுவரையறைக்குப் பயன்படும் 2001 கணக்கெடுப்புடன் குழப்ப வேண்டாம்."
        }
    },
    'POLITY_PRESIDENT_GT_089': {
        "id": "POLITY_PRESIDENT_GT_089",
        "subject": "Polity",
        "topic": "President",
        "difficulty": "medium",
        "question_type": "MCQ",
        "question": {
            "en": "Which constitutional provision explicitly bars courts from inquiring into whether any advice was tendered by Ministers to the President?",
            "ta": "அமைச்சர்கள் குடியரசுத் தலைவருக்கு வழங்கிய ஆலோசனை குறித்து எந்த நீதிமன்றமும் விசாரிக்கக் கூடாது என்று எந்த அரசியலமைப்பு விதிக் கூறு வெளிப்படையாகத் தடை விதிக்கிறது?"
        },
        "question_en": "Which constitutional provision explicitly bars courts from inquiring into whether any advice was tendered by Ministers to the President?",
        "question_ta": "அமைச்சர்கள் குடியரசுத் தலைவருக்கு வழங்கிய ஆலோசனை குறித்து எந்த நீதிமன்றமும் விசாரிக்கக் கூடாது என்று எந்த அரசியலமைப்பு விதிக் கூறு வெளிப்படையாகத் தடை விதிக்கிறது?",
        "options": [
            {
                "id": "A",
                "en": "Article 74(2)",
                "ta": "உறுப்பு 74(2)"
            },
            {
                "id": "B",
                "en": "Article 75(3)",
                "ta": "உறுப்பு 75(3)"
            },
            {
                "id": "C",
                "en": "Article 78(b)",
                "ta": "உறுப்பு 78(b)"
            },
            {
                "id": "D",
                "en": "Article 124(2)",
                "ta": "உறுப்பு 124(2)"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 74(2) states that the question whether any, and if so what, advice was tendered by Ministers to the President shall not be inquired into in any court.",
            "ta": "உறுப்பு 74(2)-ன் படி, அமைச்சர்கள் குடியரசுத் தலைவருக்கு ஏதேனும் ஆலோசனை வழங்கினார்களா, அவ்வாறு வழங்கினால் அது என்ன ஆலோசனை என்பது குறித்து எந்த நீதிமன்றத்திலும் விசாரணை செய்ய முடியாது."
        },
        "explanation_en": "Article 74(2) states that the question whether any, and if so what, advice was tendered by Ministers to the President shall not be inquired into in any court.",
        "explanation_ta": "உறுப்பு 74(2)-ன் படி, அமைச்சர்கள் குடியரசுத் தலைவருக்கு ஏதேனும் ஆலோசனை வழங்கினார்களா, அவ்வாறு வழங்கினால் அது என்ன ஆலோசனை என்பது குறித்து எந்த நீதிமன்றத்திலும் விசாரணை செய்ய முடியாது.",
        "source_reference": "President Part 2 Notes - Section 9 (Article 74 Relationship)",
        "trap_point": {
            "en": "Courts cannot inquire into ministerial advice itself (Art 74(2)), but courts can inquire into the material on which the advice was based (S.R. Bommai case).",
            "ta": "நீதிமன்றங்கள் அமைச்சர்களின் ஆலோசனையை விசாரிக்க முடியாது (உறுப்பு 74(2)), ஆனால் அந்த ஆலோசனை எதன் அடிப்படையில் வழங்கப்பட்டது என்பதற்கான ஆதாரங்களை விசாரிக்க முடியும் (S.R. பொம்மை வழக்கு)."
        }
    },
    'POLITY_PRESIDENT_GT_097': {
        "id": "POLITY_PRESIDENT_GT_097",
        "subject": "Polity",
        "topic": "President",
        "difficulty": "easy",
        "question_type": "MCQ",
        "question": {
            "en": "Under Article 53(1) of the Indian Constitution, the executive power of the Union is exercised by the President either directly or through:",
            "ta": "இந்திய அரசியலமைப்பின் 53(1) உறுப்பின் படி, ஒன்றியத்தின் நிர்வாக அதிகாரம் குடியரசுத் தலைவரால் நேரடியாகவோ அல்லது யாரின் மூலமாகவோ செலுத்தப்படுகிறது?"
        },
        "question_en": "Under Article 53(1) of the Indian Constitution, the executive power of the Union is exercised by the President either directly or through:",
        "question_ta": "இந்திய அரசியலமைப்பின் 53(1) உறுப்பின் படி, ஒன்றியத்தின் நிர்வாக அதிகாரம் குடியரசுத் தலைவரால் நேரடியாகவோ அல்லது யாரின் மூலமாகவோ செலுத்தப்படுகிறது?",
        "options": [
            {
                "id": "A",
                "en": "Officers subordinate to him in accordance with the Constitution",
                "ta": "அரசியலமைப்பிற்கு இணங்க அவருக்குக் கீழ்நிலையிலுள்ள அலுவலர்கள்"
            },
            {
                "id": "B",
                "en": "The Supreme Court of India exclusively",
                "ta": "இந்திய உச்ச நீதிமன்றம் மட்டுமே"
            },
            {
                "id": "C",
                "en": "State Governors acting independently",
                "ta": "சுயாதீனமாக செயல்படும் மாநில ஆளுநர்கள்"
            },
            {
                "id": "D",
                "en": "Union Public Service Commission",
                "ta": "ஒன்றிய அரசுப் பணியாளர் தேர்வாணையம்"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 53(1) mandates that the executive power of the Union is vested in the President and exercised by him either directly or through officers subordinate to him in accordance with the Constitution.",
            "ta": "உறுப்பு 53(1)-ன் படி, ஒன்றியத்தின் நிர்வாக அதிகாரம் குடியரசுத் தலைவரிடம் ஒப்படைக்கப்பட்டுள்ளது, அதை அவர் நேரடியாகவோ அல்லது அரசியலமைப்பிற்கு இணங்க அவருக்குக் கீழ்நிலையிலுள்ள அலுவலர்கள் மூலமாகவோ செலுத்துகிறார்."
        },
        "explanation_en": "Article 53(1) mandates that the executive power of the Union is vested in the President and exercised by him either directly or through officers subordinate to him in accordance with the Constitution.",
        "explanation_ta": "உறுப்பு 53(1)-ன் படி, ஒன்றியத்தின் நிர்வாக அதிகாரம் குடியரசுத் தலைவரிடம் ஒப்படைக்கப்பட்டுள்ளது, அதை அவர் நேரடியாகவோ அல்லது அரசியலமைப்பிற்கு இணங்க அவருக்குக் கீழ்நிலையிலுள்ள அலுவலர்கள் மூலமாகவோ செலுத்துகிறார்.",
        "source_reference": "President Part 1 Notes - Section 1 (Executive Power Article 53)",
        "trap_point": {
            "en": "Ministers are constitutional 'officers subordinate' to the President for the purpose of Article 53(1) (Shamsher Singh case).",
            "ta": "உறுப்பு 53(1)-ன் நோக்கத்திற்காக அமைச்சர்கள் குடியரசுத் தலைவருக்குக் கீழ்நிலையிலுள்ள அரசியலமைப்பு 'அலுவலர்கள்' ஆவர் (ஷாம்ஷேர் சிங் வழக்கு)."
        }
    }
}

for i, q in enumerate(gt_data):
    qid = q.get('id')
    if qid in replacements:
        print(f"Replacing duplicate {qid} at index {i}")
        gt_data[i] = replacements[qid]

with open(gt_path, 'w', encoding='utf-8') as f:
    json.load # test write
    json.dump(gt_data, f, ensure_ascii=False, indent=2)

print("Replacement complete. New count:", len(gt_data))
