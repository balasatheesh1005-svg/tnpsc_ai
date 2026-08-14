import json
import os
import sys

sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")

from ui.question_engine.parser import UniversalQuestionAdapter, NormalizedQuestion

def verify_sf_renderer():
    print("==================================================")
    print("RUNNING SALIENT FEATURES UNIVERSAL RENDERER QA SUITE")
    print("==================================================")

    gt_file = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\salient_features_of_the_indian_constitution_grand_test.json"
    assert os.path.exists(gt_file), f"Grand test file not found at {gt_file}"

    with open(gt_file, encoding="utf-8") as f:
        gt_questions = json.load(f)

    print(f"\nLoaded {len(gt_questions)} Grand Test Questions.")
    
    type_counts = {}
    for idx, raw_q in enumerate(gt_questions, 1):
        q: NormalizedQuestion = UniversalQuestionAdapter.normalize(raw_q)
        
        # Verify normalized object properties
        assert q.id == f"SF_GT_{idx:03d}", f"ID mismatch for Q{idx}"
        assert len(q.question_en) > 10, f"Q{idx} question_en empty"
        assert len(q.question_ta) > 10, f"Q{idx} question_ta empty"
        assert len(q.options) == 4, f"Q{idx} options count != 4"
        assert q.correct_answer in ["A", "B", "C", "D"], f"Q{idx} invalid correct_answer"
        assert q.explanation.en != "", f"Q{idx} explanation_en empty"
        assert q.explanation.ta != "", f"Q{idx} explanation_ta empty"

        type_counts[q.question_type] = type_counts.get(q.question_type, 0) + 1

    print("--- Salient Features Grand Test Universal Renderer Normalization Passed! ---")
    print(f"Normalized Question Types: {type_counts}")

    print("\n==================================================")
    print("ALL UNIVERSAL RENDERER QA CHECKS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    verify_sf_renderer()
