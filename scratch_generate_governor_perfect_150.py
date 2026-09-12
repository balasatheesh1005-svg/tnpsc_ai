# scratch_generate_governor_perfect_150.py
import json, os, sys

# Set standard output encoding for utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Starting generation of 150 Governor MCQs...")

# We will define 50 Easy, 50 Medium, 50 Hard in structured data
easy_items = []
medium_items = []
hard_items = []

# Let's create helper builder function
def create_mcq(id_str, subject, topic, difficulty, qtype, q_en, q_ta, opts_list, correct_ans, exp_en, exp_ta, why_not_dict, tip_en, tip_ta, rev_en, rev_ta, bloom, time_sec=60, tags=None):
    if tags is None:
        tags = ["Governor", "Polity", "Part VI"]
    
    # opts_list is list of tuples: [("A", en, ta), ("B", en, ta), ...]
    options_objs = []
    options_en = []
    options_ta = []
    for opt_id, o_en, o_ta in opts_list:
        options_objs.append({"id": opt_id, "en": o_en, "ta": o_ta})
        options_en.append(o_en)
        options_ta.append(o_ta)
        
    correct_upper = correct_ans.upper()
    answer_lower = correct_ans.lower()

    # Ensure why_not_others format
    formatted_why_not = {}
    for letter in ["A", "B", "C", "D"]:
        if letter in why_not_dict:
            wn = why_not_dict[letter]
            if isinstance(wn, dict):
                formatted_why_not[letter] = {"en": wn.get("en", ""), "ta": wn.get("ta", "")}
            else:
                formatted_why_not[letter] = {"en": str(wn), "ta": str(wn)}
        else:
            formatted_why_not[letter] = {"en": "Option explanation.", "ta": "தேர்வு விளக்கம்."}

    return {
        "id": id_str,
        "subject": subject,
        "topic": topic,
        "difficulty": difficulty,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "question_en": q_en,
        "question_ta": q_ta,
        "options": options_objs,
        "options_en": options_en,
        "options_ta": options_ta,
        "correct_answer": correct_upper,
        "answer": answer_lower,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": formatted_why_not,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT Class 11 Indian Constitution at Work"],
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": "Standard",
        "tags": tags
    }

print("Helper defined.")
