# scratch_preamble_medium_helper.py

def make_medium_q(q_id, subject, topic, difficulty, question_type, q_en, q_ta,
                  opts_en, opts_ta, correct_ans, exp_en, exp_ta, wno_dict,
                  tip_en, tip_ta, rev_en, rev_ta, sources, bloom, est_sec, pyq_sim, tags):
    
    options_struct = []
    for i, letter in enumerate(["A", "B", "C", "D"]):
        options_struct.append({
            "id": letter,
            "en": opts_en[i],
            "ta": opts_ta[i]
        })

    return {
        "id": q_id,
        "subject": subject,
        "topic": topic,
        "difficulty": difficulty,
        "question_type": question_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": options_struct,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": wno_dict,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": sources,
        "bloom_level": bloom,
        "estimated_time_sec": est_sec,
        "pyq_similarity": pyq_sim,
        "tags": tags,
        # Flat schema compatibility
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

print("Preamble Medium helper loaded successfully.")
