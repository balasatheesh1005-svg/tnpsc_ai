import json
import os

def validate_repository():
    json_path = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_grand_test.json"
    assert os.path.exists(json_path), "Grand test file does not exist!"

    with open(json_path, encoding="utf-8") as f:
        questions = json.load(f)

    assert len(questions) == 100, f"Expected 100 questions, found {len(questions)}"
    
    answer_dist = {"A": 0, "B": 0, "C": 0, "D": 0}
    seen_questions = set()

    for idx, q in enumerate(questions, 1):
        q_id = q.get("id")
        assert q_id == f"HB_GT_{idx:03d}", f"Q{idx} ID mismatch: {q_id}"
        
        # Check required top-level keys
        required_keys = [
            "id", "subject", "topic", "difficulty", "question_type", "question",
            "options", "correct_answer", "explanation", "why_not_others",
            "tnpsc_tip", "revision_fact", "source_reference", "bloom_level",
            "estimated_time_sec", "pyq_similarity", "tags", "question_en",
            "question_ta", "options_en", "options_ta", "answer", "explanation_en", "explanation_ta"
        ]
        for k in required_keys:
            assert k in q, f"Q{idx} missing key: {k}"

        # Check non-empty text
        q_en = q["question"]["en"].strip()
        q_ta = q["question"]["ta"].strip()
        assert len(q_en) > 10, f"Q{idx} question_en too short!"
        assert len(q_ta) > 10, f"Q{idx} question_ta too short!"
        assert "Regarding Government of India Act" not in q_en, f"Q{idx} contains placeholder text!"

        # Check uniqueness
        assert q_en not in seen_questions, f"Q{idx} duplicate question text!"
        seen_questions.add(q_en)

        # Check options
        opts = q["options"]
        assert len(opts) == 4, f"Q{idx} does not have 4 options!"
        opt_ids = [o["id"] for o in opts]
        assert opt_ids == ["A", "B", "C", "D"], f"Q{idx} option IDs not A,B,C,D: {opt_ids}"

        for o in opts:
            assert len(o["en"].strip()) > 0, f"Q{idx} option {o['id']} EN empty!"
            assert len(o["ta"].strip()) > 0, f"Q{idx} option {o['id']} TA empty!"

        # Check correct_answer
        ans = q["correct_answer"]
        assert ans in ["A", "B", "C", "D"], f"Q{idx} invalid correct_answer: {ans}"
        answer_dist[ans] += 1

        # Check why_not_others
        wno = q["why_not_others"]
        for opt_let in ["A", "B", "C", "D"]:
            assert opt_let in wno, f"Q{idx} why_not_others missing {opt_let}"
            assert len(wno[opt_let]["en"].strip()) > 0, f"Q{idx} why_not_others {opt_let} EN empty!"
            assert len(wno[opt_let]["ta"].strip()) > 0, f"Q{idx} why_not_others {opt_let} TA empty!"

        # Check tnpsc_tip & revision_fact
        assert len(q["tnpsc_tip"]["en"].strip()) > 0, f"Q{idx} tnpsc_tip EN empty!"
        assert len(q["tnpsc_tip"]["ta"].strip()) > 0, f"Q{idx} tnpsc_tip TA empty!"
        assert len(q["revision_fact"]["en"].strip()) > 0, f"Q{idx} revision_fact EN empty!"
        assert len(q["revision_fact"]["ta"].strip()) > 0, f"Q{idx} revision_fact TA empty!"

    print("==================================================")
    print("ALL 100 GRAND TEST QUESTIONS PASSED VALIDATION!")
    print("==================================================")
    print("Answer Key Distribution:", answer_dist)
    print("Unique Questions Count:", len(seen_questions))

if __name__ == "__main__":
    validate_repository()
