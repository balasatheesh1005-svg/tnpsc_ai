import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.question_loader import load_questions

def run_audit():
    print("==========================================================================")
    print("🚀 AUDITING FUNDAMENTAL DUTIES GRAND TEST MCQs (100 MCQs)")
    print("==========================================================================")

    file_path = "data/questions/polity/fundamental_duties_grand_test.json"
    assert os.path.exists(file_path), f"❌ File not found: {file_path}"
    
    with open(file_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"\n[FILE AUDIT] {file_path}: {len(questions)} questions found.")
    assert len(questions) == 100, f"❌ Expected 100 questions, got {len(questions)}"

    required_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "options", "correct_answer", "explanation",
        "why_not_others", "tnpsc_tip", "revision_fact", "source_reference",
        "bloom_level", "estimated_time_sec", "pyq_similarity", "tags",
        "question_en", "question_ta", "options_en", "options_ta", "answer",
        "explanation_en", "explanation_ta"
    ]

    ans_dist = {"A": 0, "B": 0, "C": 0, "D": 0}
    diff_dist = {"Easy": 0, "Medium": 0, "Hard": 0}
    previous_answers = []

    for idx, q in enumerate(questions, 1):
        # 1. Field completeness
        for field in required_fields:
            assert field in q, f"❌ Q{idx} ({q.get('id')}) missing field: {field}"

        # 2. ID convention
        expected_id = f"FD_GT_{idx:03d}"
        assert q["id"] == expected_id, f"❌ Q{idx} ID mismatch: expected {expected_id}, got {q['id']}"

        # 3. Exactly 4 options & option uniqueness
        assert len(q["options"]) == 4, f"❌ Q{idx} options count != 4"
        assert len(q["options_en"]) == 4, f"❌ Q{idx} options_en count != 4"
        assert len(q["options_ta"]) == 4, f"❌ Q{idx} options_ta count != 4"

        en_opts = [opt["en"] for opt in q["options"]]
        ta_opts = [opt["ta"] for opt in q["options"]]
        assert len(set(en_opts)) == 4, f"❌ Q{idx} has duplicate EN options: {en_opts}"
        assert len(set(ta_opts)) == 4, f"❌ Q{idx} has duplicate TA options: {ta_opts}"

        # 4. Correct answer valid
        ca = q["correct_answer"].upper()
        assert ca in ["A", "B", "C", "D"], f"❌ Q{idx} invalid correct_answer: {ca}"
        assert q["answer"] == ca.lower(), f"❌ Q{idx} answer lowercase mismatch: {q['answer']} vs {ca}"
        
        ans_dist[ca] += 1
        diff_dist[q["difficulty"]] = diff_dist.get(q["difficulty"], 0) + 1
        previous_answers.append(ca)

        # Check no 4 consecutive identical answers
        if len(previous_answers) >= 4:
            assert not (previous_answers[-1] == previous_answers[-2] == previous_answers[-3] == previous_answers[-4]), \
                f"❌ Q{idx} long consecutive run of answer '{ca}'"

        # 5. WNO check
        wno_ca = q["why_not_others"][ca]
        assert "Correct" in wno_ca["en"] or wno_ca["en"].startswith("Correct"), f"❌ Q{idx} WNO EN for {ca} missing Correct indicator"
        assert "சரி" in wno_ca["ta"] or wno_ca["ta"].startswith("சரி"), f"❌ Q{idx} WNO TA for {ca} missing Correct indicator"

        # 6. Bilingual verification
        assert len(q["question"]["en"].strip()) > 0, f"❌ Q{idx} empty question en"
        assert len(q["question"]["ta"].strip()) > 0, f"❌ Q{idx} empty question ta"
        assert len(q["explanation"]["en"].strip()) > 0, f"❌ Q{idx} empty explanation en"
        assert len(q["explanation"]["ta"].strip()) > 0, f"❌ Q{idx} empty explanation ta"
        assert len(q["tnpsc_tip"]["en"].strip()) > 0, f"❌ Q{idx} empty tnpsc_tip en"
        assert len(q["tnpsc_tip"]["ta"].strip()) > 0, f"❌ Q{idx} empty tnpsc_tip ta"
        assert len(q["revision_fact"]["en"].strip()) > 0, f"❌ Q{idx} empty revision_fact en"
        assert len(q["revision_fact"]["ta"].strip()) > 0, f"❌ Q{idx} empty revision_fact ta"

    print("\n--- AUDIT RESULTS ---")
    print(f"Answer Distribution: {ans_dist} (Target: A:25, B:25, C:25, D:25)")
    print(f"Difficulty Distribution: {diff_dist}")

    assert ans_dist == {"A": 25, "B": 25, "C": 25, "D": 25}, f"❌ Answer distribution mismatch: {ans_dist}"

    print("\n--- TESTING MATCH & CHRONOLOGY UNIQUE OPTIONS ---")
    mc_count = 0
    for q_obj in questions:
        if q_obj["question_type"] in ["Match", "Chronology"]:
            mc_count += 1
            opts = [o["en"] for o in q_obj["options"]]
            assert len(set(opts)) == 4, f"❌ Q {q_obj['id']} Match/Chronology options not unique: {opts}"
    print(f"✅ Verified {mc_count} Match/Chronology questions have 4 unique options each!")

    print("\n--- TESTING PART LOADING ---")
    for part in ["polity_fundamental_duties_part_1", "polity_fundamental_duties_part_2", "polity_fundamental_duties_part_3"]:
        part_qs = load_questions("polity_fundamental_duties", "grand_test")
        assert len(part_qs) == 100, f"❌ Loaded {len(part_qs)} questions for {part}"
        print(f"✅ Topic ID: {part} -> Loaded {len(part_qs)} Grand Test questions")

    print("\nSUCCESS: All Fundamental Duties Grand Test assertions and part loading PASSED!")

if __name__ == "__main__":
    run_audit()
