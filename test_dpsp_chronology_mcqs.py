import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test_dpsp_chronology():
    target_file = "data/questions/polity/directive_principles_chronology.json"
    assert os.path.exists(target_file), f"File not found: {target_file}"
    
    with open(target_file, "r", encoding="utf-8") as f:
        questions = json.load(f)
        
    print(f"Loaded {len(questions)} questions from {target_file}")
    assert len(questions) == 25, f"Expected 25 questions, got {len(questions)}"
    
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
    
    for idx, q in enumerate(questions, 1):
        for field in required_fields:
            assert field in q, f"Q{idx} ({q.get('id')}) missing field '{field}'"
            
        expected_id = f"DPSP_CHRONO_{idx:03d}"
        assert q["id"] == expected_id, f"Q{idx} ID mismatch: expected {expected_id}, got {q['id']}"
        
        assert len(q["events"]) == 4, f"Q{idx} events count != 4"
        assert len(q["options"]) == 4, f"Q{idx} options count != 4"
        assert len(q["options_en"]) == 4, f"Q{idx} options_en count != 4"
        assert len(q["options_ta"]) == 4, f"Q{idx} options_ta count != 4"
        
        ca = q["correct_answer"]
        assert ca in ["A", "B", "C", "D"], f"Q{idx} invalid correct_answer: {ca}"
        assert q["answer"] == ca.lower(), f"Q{idx} answer lowercase mismatch: {q['answer']} vs {ca}"
        
        ans_dist[ca] += 1
        diff_dist[q["difficulty"]] += 1
        
        # WNO indicator check
        wno_ca = q["why_not_others"][ca]
        assert "Correct" in wno_ca["en"] or wno_ca["en"].startswith("Correct"), f"Q{idx} WNO EN for correct_answer {ca} does not state Correct"
        assert "சரி" in wno_ca["ta"] or wno_ca["ta"].startswith("சரி"), f"Q{idx} WNO TA for correct_answer {ca} does not state Correct"
        
        # Bilingual check
        assert len(q["question"]["en"].strip()) > 0, f"Q{idx} empty EN question"
        assert len(q["question"]["ta"].strip()) > 0, f"Q{idx} empty TA question"
        assert len(q["tnpsc_tip"]["en"].strip()) > 0, f"Q{idx} empty EN TNPSC tip"
        assert len(q["tnpsc_tip"]["ta"].strip()) > 0, f"Q{idx} empty TA TNPSC tip"

    print("\n--- AUDIT RESULTS ---")
    print(f"Answer Distribution: {ans_dist} (Target: A:6, B:6, C:6, D:7)")
    print(f"Difficulty Distribution: {diff_dist} (Target: Easy: 5, Medium: 12-13, Hard: 7-8)")

    assert ans_dist["A"] == 6, f"Expected 6 A, got {ans_dist['A']}"
    assert ans_dist["B"] == 6, f"Expected 6 B, got {ans_dist['B']}"
    assert ans_dist["C"] == 6, f"Expected 6 C, got {ans_dist['C']}"
    assert ans_dist["D"] == 7, f"Expected 7 D, got {ans_dist['D']}"
    
    print("\nSUCCESS: All static schema, bilingual, and distribution assertions PASSED!")

if __name__ == "__main__":
    test_dpsp_chronology()
