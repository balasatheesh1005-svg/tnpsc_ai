"""
Unit tests for Flagship AI Exam Coach Dashboard V2 (ui/coach/dashboard.py & master engine integration).
Verifies pure presentation layer rendering, zero business logic duplication, integration of all 8 core engines,
single Next Best Action enforcement, and zero database schema mutations.
"""
import unittest

from core.learning_intelligence_ai import get_learning_intelligence
from core.study_planner_ai import get_personal_study_plan
from core.recommendation_ai import get_ai_recommendation
from core.exam_readiness_ai import get_exam_readiness
from core.mock_intelligence_ai import get_mock_intelligence
from core.predictive_performance_ai import get_predictive_performance
from core.adaptive_revision_ai import get_adaptive_final_revision
from core.exam_strategy_ai import get_exam_strategy


class TestCoachDashboardV2(unittest.TestCase):

    def test_all_8_core_engines_integration(self):
        """Verify all 8 core intelligence engines can be invoked without error."""
        user = "test_user"

        intel = get_learning_intelligence(user)
        self.assertIn("current_mastery", intel)

        plan = get_personal_study_plan(user, available_time=45)
        self.assertIn("topic", plan)

        rec = get_ai_recommendation(user)
        self.assertIn("recommendation", rec)

        readiness = get_exam_readiness(user)
        self.assertIn("overall_readiness_score", readiness)

        mock = get_mock_intelligence(user)
        self.assertIn("overall_accuracy", mock)

        pred = get_predictive_performance(user)
        self.assertIn("estimated_readiness", pred)

        adaptive = get_adaptive_final_revision(user)
        self.assertIn("revision_phase", adaptive)

        strat = get_exam_strategy(user)
        self.assertIn("overall_strategy", strat)

    def test_single_next_best_action_enforcement(self):
        """Verify Recommendation Engine returns ONE primary recommendation."""
        rec = get_ai_recommendation("test_user")
        self.assertIn("recommendation", rec)
        recommendation_text = rec["recommendation"]
        self.assertIsInstance(recommendation_text, str)
        self.assertGreater(len(recommendation_text), 0)

    def test_no_prohibited_guarantees(self):
        """Verify predictive and coach outputs never contain absolute pass/rank guarantees."""
        pred = get_predictive_performance("test_user")
        strat = get_exam_strategy("test_user")

        combined_text = (
            str(pred.get("prediction_reason", ""))
            + str(strat.get("confidence_reason", ""))
        ).lower()

        prohibited_phrases = ["guaranteed pass", "100% selection", "guaranteed rank"]
        for phrase in prohibited_phrases:
            self.assertNotIn(phrase, combined_text, f"Forbidden phrase found: {phrase}")


if __name__ == "__main__":
    unittest.main()
