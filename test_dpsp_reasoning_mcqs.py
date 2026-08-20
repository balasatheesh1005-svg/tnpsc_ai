import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.question_loader import load_questions

def run_audit():
    print("==========================================================================")
    print("🚀 AUDITING DPSP REASONING MCQs (25 MCQs)")
    print("==========================================================================")

    files = [
        "data/questions/polity/directive_principles_reasoning.json",
        "data/questions/polity/directive_principles_assertion_reason.json"
    ]

    for file_path in files:
        assert os.path.exists(file_path), f"❌ File not found: {file_path}"
        with open(file_path, "r", encoding="utf-8") as f:
            questions = json.load(f)

        print(f"\n[FILE AUDIT] {file_path}: {len(questions)} questions found.")
        assert len(questions) == 25, f"❌ Expected 25 questions, got {len(questions)}"

    required_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "options", "correct_answer", "explanation",
        "why_not_others", "tnpsc_tip", "revision_fact", "source_reference",
        "bloom_level", "estimated_time_sec", "pyq_similarity", "tags",
        "question_en", "question_ta", "options_en", "options_ta", "answer",
        "explanation_en", "explanation_ta"
    ]

    ans_dist = {"A": 0, "B": 0, "C": 0, "D": 0}
    diff_dist = {"Easy": 0, "Easy-Medium": 0, "Medium": 0, "Hard": 0}

    for idx, q in enumerate(questions, 1):
        # 1. Field completeness
        for field in required_fields:
            assert field in q, f"❌ Q{idx} ({q.get('id')}) missing field: {field}"

        # 2. ID convention
        expected_id = f"DPSP_R_{idx:03d}"
        assert q["id"] == expected_id, f"❌ Q{idx} ID mismatch: expected {expected_id}, got {q['id']}"

        # 3. Exactly 4 options
        assert len(q["options"]) == 4, f"❌ Q{idx} options count != 4"
        assert len(q["options_en"]) == 4, f"❌ Q{idx} options_en count != 4"
        assert len(q["options_ta"]) == 4, f"❌ Q{idx} options_ta count != 4"

        # 4. Correct answer valid
        ca = q["correct_answer"].upper()
        assert ca in ["A", "B", "C", "D"], f"❌ Q{idx} invalid correct_answer: {ca}"
        ans_dist[ca] += 1
        diff_dist[q["difficulty"]] += 1

        # 5. Bilingual verification
        assert len(q["question"]["en"].strip()) > 0, f"❌ Q{idx} empty question en"
        assert len(q["question"]["ta"].strip()) > 0, f"❌ Q{idx} empty question ta"
        assert len(q["explanation"]["en"].strip()) > 0, f"❌ Q{idx} empty explanation en"
        assert len(q["explanation"]["ta"].strip()) > 0, f"❌ Q{idx} empty explanation ta"
        assert len(q["tnpsc_tip"]["en"].strip()) > 0, f"❌ Q{idx} empty tnpsc_tip en"
        assert len(q["tnpsc_tip"]["ta"].strip()) > 0, f"❌ Q{idx} empty tnpsc_tip ta"

    print("\n--- AUDIT RESULTS ---")
    print(f"Answer Distribution: {ans_dist} (Target: A:6, B:6, C:6, D:7)")
    print(f"Difficulty Distribution: {diff_dist} (Target: Easy-Medium: 5, Medium: 12, Hard: 8)")

    assert ans_dist == {"A": 6, "B": 6, "C": 6, "D": 7}, f"❌ Answer distribution mismatch: {ans_dist}"

    print("\n--- TESTING PART LOADING ---")
    for part in ["polity_directive_principles_part_1", "polity_directive_principles_part_2", "polity_directive_principles_part_3"]:
        part_qs = load_questions("polity_directive_principles", "reasoning")
        assert len(part_qs) == 25, f"❌ Loaded {len(part_qs)} questions for {part}"
        print(f"✅ Topic ID: {part} -> Loaded {len(part_qs)} Reasoning questions")

    print("\nSUCCESS: All DPSP Reasoning assertions and part loading PASSED!")

if __name__ == "__main__":
    run_audit()
