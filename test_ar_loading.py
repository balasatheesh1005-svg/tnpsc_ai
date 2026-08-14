import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.question_loader import load_questions
from ui.question_engine.parser import UniversalQuestionAdapter, NormalizedQuestion

def test_ar_questions():
    print("==================================================")
    print("TESTING ASSERTION & REASON PRACTICE QUESTION LOADING")
    print("==================================================")

    repo_id = "polity_salient_features_of_the_indian_constitution"
    qs = load_questions(repo_id, "assertion_reason")

    print(f"\nLoaded {len(qs)} Assertion & Reason questions for {repo_id}")
    assert len(qs) == 25, f"Expected 25 questions, got {len(qs)}"

    for idx, raw_q in enumerate(qs, 1):
        q: NormalizedQuestion = UniversalQuestionAdapter.normalize(raw_q)
        assert len(q.question_en) > 10, f"Q{idx} empty question text"
        assert len(q.options) == 4, f"Q{idx} options count != 4"
        assert q.correct_answer in ["A", "B", "C", "D"], f"Q{idx} invalid correct answer"

    print("\n--- All 25 Assertion & Reason Practice Questions Normalized & Validated Successfully! ---")

if __name__ == "__main__":
    test_ar_questions()
