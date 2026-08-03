"""
Unit tests for Exam Strategy Engine V2 (core/exam_strategy_ai.py).
Verifies pre-exam strategy generation, personalized subject ordering, section time allocation summation,
question decision rules, review ordering, non-fear risk analysis, and confidence calculations.
"""
import unittest

from core.exam_strategy_ai import (
    get_exam_strategy,
    _determine_overall_strategy,
)


class TestExamStrategyEngineV2(unittest.TestCase):

    def test_overall_strategy_determination(self):
        """Verify strategy theme classification based on readiness & mock accuracy."""
        self.assertEqual(_determine_overall_strategy(85, 85), "Strength-First High-Velocity Execution")
        self.assertEqual(_determine_overall_strategy(70, 75), "Balanced Systematic Progression")
        self.assertEqual(_determine_overall_strategy(55, 60), "High-Accuracy Tactical Focus")

    def test_master_schema_conformance(self):
        """Verify master exam strategy schema returns all required keys."""
        strat = get_exam_strategy("test_user")

        required_keys = [
            "overall_strategy",
            "subject_order",
            "time_plan",
            "question_strategy",
            "skip_strategy",
            "review_order",
            "risk_alerts",
            "strategy_confidence",
            "confidence_reason",
            "mentor_strategy",
            "dashboard_sections",
        ]
        for key in required_keys:
            self.assertIn(key, strat, f"Missing required key in exam strategy schema: {key}")

    def test_subject_order_generation(self):
        """Verify personalized subject attempt order is generated."""
        strat = get_exam_strategy("test_user")
        order = strat["subject_order"]
        self.assertIsInstance(order, list)
        self.assertGreaterEqual(len(order), 3)

    def test_time_allocation_sum_matches_total(self):
        """Verify total allocated section minutes equals configured total exam duration strictly."""
        for total_mins in [180, 150, 120]:
            strat = get_exam_strategy("test_user", total_exam_minutes=total_mins)
            time_plan = strat["time_plan"]
            total_sum = sum(item["minutes"] for item in time_plan)
            self.assertEqual(
                total_sum,
                total_mins,
                f"Sum of section minutes ({total_sum}) does not equal total_exam_minutes ({total_mins})",
            )

    def test_non_fear_language_in_risk_alerts(self):
        """Verify risk alerts use constructive, non-fear guidance."""
        strat = get_exam_strategy("test_user")
        alerts = strat["risk_alerts"]
        combined_text = " ".join(alerts).lower()

        forbidden_fear_words = [
            "fail",
            "disaster",
            "hopeless",
            "doomed",
            "panic",
            "guaranteed failure",
        ]
        for word in forbidden_fear_words:
            self.assertNotIn(word, combined_text, f"Fear-based word found in risk alerts: {word}")

    def test_no_answer_generation(self):
        """Verify strategy engine generates execution strategy ONLY, zero answers or cheating guidance."""
        strat = get_exam_strategy("test_user")
        combined_text = (
            str(strat.get("question_strategy", ""))
            + str(strat.get("mentor_strategy", ""))
        ).lower()

        prohibited_phrases = [
            "correct option is a",
            "option b is answer",
            "cheat sheet",
            "answer key",
        ]
        for phrase in prohibited_phrases:
            self.assertNotIn(phrase, combined_text, f"Prohibited answer phrase found: {phrase}")

    def test_confidence_score_range(self):
        """Verify strategy confidence score is between 0 and 100."""
        strat = get_exam_strategy("test_user")
        conf = strat["strategy_confidence"]
        self.assertIsInstance(conf, int)
        self.assertGreaterEqual(conf, 50)
        self.assertLessEqual(conf, 100)


if __name__ == "__main__":
    unittest.main()
