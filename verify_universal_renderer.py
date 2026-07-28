import json
import os
import sys

# Ensure root workspace directory is in python path
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")

from ui.question_engine.parser import UniversalQuestionAdapter, NormalizedQuestion


def run_universal_renderer_qa():
    print("==================================================")
    print("RUNNING UNIVERSAL QUESTION RENDERER QA SUITE")
    print("==================================================")

    # 1. Test Grand Test Repository (100 Questions)
    gt_file = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_grand_test.json"
    assert os.path.exists(gt_file), f"Grand test file not found at {gt_file}"

    with open(gt_file, encoding="utf-8") as f:
        gt_questions = json.load(f)

    print(f"\n[TEST 1] Loaded {len(gt_questions)} Grand Test Questions.")
    
    type_counts = {}
    for idx, raw_q in enumerate(gt_questions, 1):
        q: NormalizedQuestion = UniversalQuestionAdapter.normalize(raw_q)
        
        # Verify normalized object properties
        assert q.id == f"HB_GT_{idx:03d}", f"ID mismatch for Q{idx}"
        assert len(q.question_en) > 10, f"Q{idx} question_en empty"
        assert len(q.options) == 4, f"Q{idx} options count != 4"
        assert q.correct_answer in ["A", "B", "C", "D"], f"Q{idx} invalid correct_answer"
        assert q.explanation.en != "", f"Q{idx} explanation_en empty"

        type_counts[q.question_type] = type_counts.get(q.question_type, 0) + 1

    print("--- Grand Test Normalization Passed! ---")
    print(f"  Normalized Question Types: {type_counts}")

    # 2. Test Legacy Repository (Easy Polity Questions)
    legacy_file = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_easy.json"
    if os.path.exists(legacy_file):
        with open(legacy_file, encoding="utf-8") as f:
            legacy_questions = json.load(f)
            
        print(f"\n[TEST 2] Loaded {len(legacy_questions)} Legacy Easy Polity Questions.")
        for idx, raw_q in enumerate(legacy_questions, 1):
            q: NormalizedQuestion = UniversalQuestionAdapter.normalize(raw_q)
            assert len(q.question_en) > 0, f"Legacy Q{idx} empty text"
            assert len(q.options) >= 2, f"Legacy Q{idx} insufficient options"
            assert q.correct_answer in ["A", "B", "C", "D"], f"Legacy Q{idx} invalid answer"

        print("--- Legacy Dataset Normalization Passed! ---")

    # 3. Test Synthetic Malformed & Missing Field JSON Payloads
    print("\n[TEST 3] Testing Malformed / Dynamic Schema Variants...")
    
    # Variant A: Missing question_en, relying on question dict
    var_a = {
        "id": "VAR_001",
        "question": {"en": "What is the capital of Tamil Nadu?", "ta": "தமிழ்நாட்டின் தலைநகரம் எது?"},
        "options": {"A": "Chennai", "B": "Madurai", "C": "Coimbatore", "D": "Trichy"},
        "correct": "A"
    }
    q_a = UniversalQuestionAdapter.normalize(var_a)
    assert q_a.question_en == "What is the capital of Tamil Nadu?"
    assert q_a.question_ta == "தமிழ்நாட்டின் தலைநகரம் எது?"
    assert q_a.correct_answer == "A"
    print("  [OK] Variant A (Question Dict & Correct key) passed.")

    # Variant B: Parallel options_en and options_ta lists
    var_b = {
        "id": "VAR_002",
        "question_en": "Select the correct statement regarding Regulating Act 1773:",
        "options_en": ["It created Board of Control", "It created Supreme Court at Fort William"],
        "options_ta": ["கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது", "வில்லியம் கோட்டையில் உச்ச நீதிமன்றத்தை உருவாக்கியது"],
        "answer": "B"
    }
    q_b = UniversalQuestionAdapter.normalize(var_b)
    assert len(q_b.options) == 2
    assert q_b.options[0].en == "It created Board of Control"
    assert q_b.options[0].ta == "கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது"
    assert q_b.correct_answer == "B"
    assert q_b.question_type == "Statement Based"
    print("  [OK] Variant B (Parallel option lists & Auto Statement detection) passed.")

    print("\n==================================================")
    print("ALL UNIVERSAL RENDERER QA CHECKS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    run_universal_renderer_qa()
