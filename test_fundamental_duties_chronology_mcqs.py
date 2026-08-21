import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def test_fundamental_duties_chronology():
    target_file = "data/questions/polity/fundamental_duties_chronology.json"
    assert os.path.exists(target_file), f"File not found: {target_file}"
    
    with open(target_file, "r", encoding="utf-8") as f:
        questions = json.load(f)
        
    print(f"Loaded {len(questions)} questions from {target_file}")
    assert len(questions) == 25, f"Expected exactly 25 questions, got {len(questions)}"
    
    required_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "events", "options", "correct_answer", "explanation",
        "why_not_others", "tnpsc_tip", "revision_fact", "source_reference",
        "bloom_level", "estimated_time_sec", "pyq_similarity", "tags",
        "question_en", "question_ta", "options_en", "options_ta", "answer",
        "explanation_en", "explanation_ta"
    ]
    
    ans_dist = {"A": 0, "B": 0, "C": 0, "D": 0}
    diff_dist = {"Easy": 0, "Medium": 0, "Hard": 0}
    
    previous_answers = []
    
    for idx, q in enumerate(questions, 1):
        # 1. Field presence
        for field in required_fields:
            assert field in q, f"Q{idx} ({q.get('id')}) missing field '{field}'"
            
        # 2. ID formatting
        expected_id = f"FD_CHRONO_{idx:03d}"
        assert q["id"] == expected_id, f"Q{idx} ID mismatch: expected {expected_id}, got {q['id']}"
        
        # 3. Counts check
        assert len(q["events"]) == 4, f"Q{idx} events count != 4"
        assert len(q["options"]) == 4, f"Q{idx} options count != 4"
        assert len(q["options_en"]) == 4, f"Q{idx} options_en count != 4"
        assert len(q["options_ta"]) == 4, f"Q{idx} options_ta count != 4"
        
        # 4. OPTION UNIQUENESS CHECK
        en_opts = [opt["en"] for opt in q["options"]]
        ta_opts = [opt["ta"] for opt in q["options"]]
        
        assert len(set(en_opts)) == 4, f"Q{idx} has DUPLICATE English options: {en_opts}"
        assert len(set(ta_opts)) == 4, f"Q{idx} has DUPLICATE Tamil options: {ta_opts}"
        assert len(set(q["options_en"])) == 4, f"Q{idx} options_en has DUPLICATES: {q['options_en']}"
        assert len(set(q["options_ta"])) == 4, f"Q{idx} options_ta has DUPLICATES: {q['options_ta']}"
        
        # 5. Answer alignment
        ca = q["correct_answer"]
        assert ca in ["A", "B", "C", "D"], f"Q{idx} invalid correct_answer: {ca}"
        assert q["answer"] == ca.lower(), f"Q{idx} answer lowercase mismatch: {q['answer']} vs {ca}"
        
        ans_dist[ca] += 1
        diff_dist[q["difficulty"]] += 1
        previous_answers.append(ca)
        
        # Check consecutive identical answers (no 4 in a row)
        if len(previous_answers) >= 4:
            assert not (previous_answers[-1] == previous_answers[-2] == previous_answers[-3] == previous_answers[-4]), \
                f"Q{idx} long consecutive run of answer '{ca}'"
        
        # 6. WNO indicator check
        wno_ca = q["why_not_others"][ca]
        assert "Correct" in wno_ca["en"] or wno_ca["en"].startswith("Correct"), f"Q{idx} WNO EN for correct_answer {ca} does not state Correct"
        assert "சரி" in wno_ca["ta"] or wno_ca["ta"].startswith("சரி"), f"Q{idx} WNO TA for correct_answer {ca} does not state Correct"
        
        # 7. Bilingual check
        assert len(q["question"]["en"].strip()) > 0, f"Q{idx} empty EN question"
        assert len(q["question"]["ta"].strip()) > 0, f"Q{idx} empty TA question"
        assert len(q["tnpsc_tip"]["en"].strip()) > 0, f"Q{idx} empty EN TNPSC tip"
        assert len(q["tnpsc_tip"]["ta"].strip()) > 0, f"Q{idx} empty TA TNPSC tip"
        assert len(q["revision_fact"]["en"].strip()) > 0, f"Q{idx} empty EN revision fact"
        assert len(q["revision_fact"]["ta"].strip()) > 0, f"Q{idx} empty TA revision fact"
        assert len(q["explanation"]["en"].strip()) > 0, f"Q{idx} empty EN explanation"
        assert len(q["explanation"]["ta"].strip()) > 0, f"Q{idx} empty TA explanation"

    print("\n--- STATISTICAL RESULTS ---")
    print(f"Answer Distribution: {ans_dist}")
    print(f"Difficulty Distribution: {diff_dist}")
    
    assert diff_dist["Easy"] >= 4, "Too few Easy questions"
    assert diff_dist["Medium"] >= 10, "Too few Medium questions"
    assert diff_dist["Hard"] >= 5, "Too few Hard questions"

    print("\nSUCCESS: All static schema, bilingual, option uniqueness, and distribution tests PASSED!")

if __name__ == "__main__":
    test_fundamental_duties_chronology()
