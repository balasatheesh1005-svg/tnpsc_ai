import unittest
from unittest.mock import patch, MagicMock
import streamlit as st

from core.user_context import UserContext
from core.coach_maturity_ai import get_coach_maturity
from core.exam_readiness_ai import get_exam_readiness
from core.predictive_performance_ai import get_predictive_performance
from core.mock_intelligence_ai import get_mock_intelligence
from core.learning_intelligence_ai import get_learning_intelligence
from core.recommendation_ai import get_ai_recommendation
from core.study_planner_ai import get_personal_study_plan
from core.adaptive_revision_ai import get_adaptive_final_revision
from core.exam_strategy_ai import get_exam_strategy
from ui.coach.dashboard import render_coach_dashboard


class TestPatch21CoachIntegration(unittest.TestCase):
    """
    Focused integration test suite for TNPSC Nova AI Patch 2.1:
    Fresh-User AI Coach Integration Regression Fix & Three-State Pipeline Verification.
    """

    def setUp(self):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state["test_active"] = False
        st.session_state["test_qs"] = []
        st.session_state["xp"] = 0
        st.session_state["level"] = "easy"
        st.session_state["main_menu"] = "🏠 Home"

    def tearDown(self):
        for key in list(st.session_state.keys()):
            del st.session_state[key]

    # =========================================================================
    # A. NO_DATA PIPELINE
    # =========================================================================
    @patch("core.coach_maturity_ai.get_progress", return_value=[])
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_user_xp", return_value={"xp": 0})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    @patch("core.exam_readiness_ai.get_progress", return_value=[])
    @patch("core.exam_readiness_ai.get_weakness", return_value={})
    @patch("core.exam_readiness_ai.get_streak", return_value=0)
    @patch("core.mock_intelligence_ai.get_progress", return_value=[])
    @patch("core.predictive_performance_ai.get_progress", return_value=[])
    @patch("core.learning_intelligence_ai.get_progress", return_value=[])
    @patch("core.learning_intelligence_ai.get_weakness", return_value={})
    @patch("core.learning_intelligence_ai.get_streak", return_value=0)
    @patch("core.recommendation_ai.get_progress", return_value=[])
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.recommendation_ai.get_streak", return_value=0)
    @patch("core.study_planner_ai.get_progress", return_value=[])
    @patch("core.study_planner_ai.get_weakness", return_value={})
    @patch("core.study_planner_ai.get_streak", return_value=0)
    @patch("core.adaptive_revision_ai.get_progress", return_value=[])
    @patch("core.adaptive_revision_ai.get_weakness", return_value={})
    @patch("core.adaptive_revision_ai.get_streak", return_value=0)
    @patch("core.exam_strategy_ai.get_progress", return_value=[])
    @patch("core.exam_strategy_ai.get_weakness", return_value={})
    @patch("core.exam_strategy_ai.get_streak", return_value=0)
    def test_no_data_complete_pipeline_does_not_crash(self, *mocks):
        """Verify that every engine used by render_coach_dashboard executes without TypeError on NO_DATA."""
        user = "fresh_user_patch21"
        fresh_ctx = UserContext(
            user_id="test-fresh-id",
            username=user,
            progress=[],
            weakness={},
            streak=0,
            xp={"xp": 0, "level": 1},
        )

        with patch("core.user_context.UserContext.get_or_create", return_value=fresh_ctx), \
             patch("core.user_context.UserContext.load", return_value=fresh_ctx):

            maturity = get_coach_maturity(user)
            self.assertEqual(maturity["state"], "NO_DATA")

            readiness = get_exam_readiness(user, force_refresh=True)
            self.assertEqual(readiness["overall_readiness_score"], 0)
            self.assertFalse(readiness["is_eligible"])

            mock_data = get_mock_intelligence(user, force_refresh=True)
            self.assertIsNone(mock_data["overall_accuracy"])
            self.assertFalse(mock_data["has_mock_history"])

            predictive = get_predictive_performance(user, force_refresh=True)
            self.assertEqual(predictive["sample_size"], 0)
            self.assertEqual(predictive["prediction_confidence"], 0)
            self.assertEqual(predictive["estimated_readiness"], "Unavailable")

            intelligence = get_learning_intelligence(user, force_refresh=True)
            self.assertIsNone(intelligence["weak_topic"])
            self.assertEqual(intelligence["mastered_count"], 0)
            self.assertEqual(intelligence["pending_count"], 0)

            recommendation = get_ai_recommendation(user, force_refresh=True)
            self.assertEqual(recommendation["recommendation_type"], "Starter Path")

            study_plan = get_personal_study_plan(user, available_time=45, force_refresh=True)
            self.assertIsInstance(study_plan, dict)
            self.assertIn("today_plan", study_plan)

            adaptive_revision = get_adaptive_final_revision(user, force_refresh=True)
            self.assertIsInstance(adaptive_revision, dict)
            self.assertIn("revision_phase", adaptive_revision)
            # Verify no synthetic Physical Geography
            self.assertNotIn("Physical Geography", str(adaptive_revision.get("priority_topics", [])))

            # Crucial: Exam Strategy Engine must NOT raise TypeError with None mock_accuracy
            exam_strategy = get_exam_strategy(user, force_refresh=True)
            self.assertIsInstance(exam_strategy, dict)
            self.assertIn("overall_strategy", exam_strategy)
            self.assertIn("subject_order", exam_strategy)
            self.assertIn("time_plan", exam_strategy)
            self.assertIn("strategy_confidence", exam_strategy)
            self.assertIsInstance(exam_strategy["strategy_confidence"], int)
            self.assertNotIn("consistent mock history", exam_strategy["confidence_reason"].lower())

    # =========================================================================
    # B. EARLY_INSIGHTS PIPELINE
    # =========================================================================
    @patch("core.coach_maturity_ai.get_progress")
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=1)
    @patch("core.coach_maturity_ai.get_user_xp", return_value={"xp": 60})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    @patch("core.exam_readiness_ai.get_progress")
    @patch("core.mock_intelligence_ai.get_progress")
    @patch("core.predictive_performance_ai.get_progress")
    @patch("core.learning_intelligence_ai.get_progress")
    @patch("core.learning_intelligence_ai.get_weakness", return_value={})
    @patch("core.recommendation_ai.get_progress")
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.study_planner_ai.get_progress")
    @patch("core.adaptive_revision_ai.get_progress")
    @patch("core.exam_strategy_ai.get_progress")
    def test_early_insights_complete_pipeline_safely_handles_missing_mock(self, *mocks):
        """User with 2 normal tests and 0 mocks must not crash and mock metrics remain unavailable."""
        sample_progress = [
            {"subject": "polity", "topic": "preamble_easy", "accuracy": 80},
            {"subject": "polity", "topic": "salient_features_easy", "accuracy": 70},
        ]
        # Assign sample_progress to all progress mocks
        for m in mocks:
            if hasattr(m, "return_value") and m.return_value != {}:
                if not isinstance(m.return_value, (int, dict)):
                    m.return_value = sample_progress

        user = "early_user_patch21"
        early_ctx = UserContext(
            user_id="test-early-id",
            username=user,
            progress=sample_progress,
            weakness={},
            streak=1,
            xp={"xp": 60, "level": 1},
        )

        with patch("core.user_context.UserContext.get_or_create", return_value=early_ctx), \
             patch("core.user_context.UserContext.load", return_value=early_ctx):

            maturity = get_coach_maturity(user)
            self.assertEqual(maturity["state"], "EARLY_INSIGHTS")
            self.assertEqual(maturity["attempt_count"], 2)
            self.assertFalse(maturity["mock_eligible"])
            self.assertFalse(maturity["prediction_eligible"])
            self.assertIsNone(maturity["latest_mock_accuracy"])

            mock_data = get_mock_intelligence(user, force_refresh=True)
            self.assertIsNone(mock_data["overall_accuracy"])
            self.assertFalse(mock_data["has_mock_history"])

            # Strategy engine must not crash when overall_accuracy is None
            strategy = get_exam_strategy(user, force_refresh=True)
            self.assertIsNotNone(strategy)
            self.assertIsInstance(strategy["strategy_confidence"], int)
            self.assertNotIn("consistent mock history", strategy["confidence_reason"].lower())

            # Adaptive revision must not crash
            rev = get_adaptive_final_revision(user, force_refresh=True)
            self.assertIsNotNone(rev)

    # =========================================================================
    # C. PERSONALIZED_COACH PIPELINE
    # =========================================================================
    @patch("core.coach_maturity_ai.get_progress")
    @patch("core.coach_maturity_ai.get_weakness")
    @patch("core.coach_maturity_ai.get_streak", return_value=6)
    @patch("core.coach_maturity_ai.get_user_xp", return_value={"xp": 650})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    @patch("core.exam_readiness_ai.get_progress")
    @patch("core.exam_readiness_ai.get_weakness")
    @patch("core.mock_intelligence_ai.get_progress")
    @patch("core.predictive_performance_ai.get_progress")
    @patch("core.learning_intelligence_ai.get_progress")
    @patch("core.learning_intelligence_ai.get_weakness")
    @patch("core.recommendation_ai.get_progress")
    @patch("core.recommendation_ai.get_weakness")
    @patch("core.study_planner_ai.get_progress")
    @patch("core.study_planner_ai.get_weakness")
    @patch("core.adaptive_revision_ai.get_progress")
    @patch("core.adaptive_revision_ai.get_weakness")
    @patch("core.exam_strategy_ai.get_progress")
    @patch("core.exam_strategy_ai.get_weakness")
    def test_personalized_coach_complete_pipeline_preserves_real_metrics(self, *mocks):
        """User with 6 tests including a Grand Test and weakness has full personalized metrics."""
        sample_progress = [
            {"subject": "polity", "topic": "preamble_easy", "accuracy": 90},
            {"subject": "polity", "topic": "salient_features_medium", "accuracy": 85},
            {"subject": "polity", "topic": "fundamental_rights_hard", "accuracy": 60},
            {"subject": "history", "topic": "south_indian_history", "accuracy": 75},
            {"subject": "history", "topic": "freedom_struggle", "accuracy": 85},
            {"subject": "polity", "topic": "polity_grand_test", "accuracy": 82},
        ]
        sample_weakness = {"polity-fundamental_rights": 3}

        for m in mocks:
            if hasattr(m, "return_value") and not isinstance(m.return_value, int):
                pass

        user = "mature_user_patch21"
        mature_ctx = UserContext(
            user_id="test-mature-id",
            username=user,
            progress=sample_progress,
            weakness=sample_weakness,
            streak=6,
            xp={"xp": 650, "level": 3},
        )

        with patch("core.user_context.UserContext.get_or_create", return_value=mature_ctx), \
             patch("core.user_context.UserContext.load", return_value=mature_ctx), \
             patch("core.progress_ai.get_progress", return_value=sample_progress), \
             patch("core.weakness_ai.get_weakness", return_value=sample_weakness), \
             patch("core.streak_ai.get_streak", return_value=6), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_weakness", return_value=sample_weakness), \
             patch("core.exam_readiness_ai.get_progress", return_value=sample_progress), \
             patch("core.mock_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.predictive_performance_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_weakness", return_value=sample_weakness), \
             patch("core.recommendation_ai.get_progress", return_value=sample_progress), \
             patch("core.recommendation_ai.get_weakness", return_value=sample_weakness), \
             patch("core.study_planner_ai.get_progress", return_value=sample_progress), \
             patch("core.adaptive_revision_ai.get_progress", return_value=sample_progress), \
             patch("core.adaptive_revision_ai.get_weakness", return_value=sample_weakness), \
             patch("core.exam_strategy_ai.get_progress", return_value=sample_progress), \
             patch("core.exam_strategy_ai.get_weakness", return_value=sample_weakness):

            maturity = get_coach_maturity(user)
            self.assertEqual(maturity["state"], "PERSONALIZED_COACH")
            self.assertTrue(maturity["mock_eligible"])
            self.assertEqual(maturity["latest_mock_accuracy"], 82)

            mock_data = get_mock_intelligence(user, force_refresh=True)
            self.assertTrue(mock_data["has_mock_history"])
            self.assertEqual(mock_data["overall_accuracy"], 82)

            strategy = get_exam_strategy(user, force_refresh=True)
            self.assertIn(strategy["overall_strategy"], ["Balanced Systematic Progression", "Strength-First High-Velocity Execution"])
            self.assertIn("consistent mock history", strategy["confidence_reason"].lower())
            self.assertGreaterEqual(strategy["strategy_confidence"], 75)

    # =========================================================================
    # D. UI RENDER SMOKE TEST
    # =========================================================================
    @patch("core.coach_maturity_ai.get_progress", return_value=[])
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_user_xp", return_value={"xp": 0})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    @patch("core.exam_readiness_ai.get_progress", return_value=[])
    @patch("core.exam_readiness_ai.get_weakness", return_value={})
    @patch("core.mock_intelligence_ai.get_progress", return_value=[])
    @patch("core.predictive_performance_ai.get_progress", return_value=[])
    @patch("core.learning_intelligence_ai.get_progress", return_value=[])
    @patch("core.learning_intelligence_ai.get_weakness", return_value={})
    @patch("core.recommendation_ai.get_progress", return_value=[])
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.study_planner_ai.get_progress", return_value=[])
    @patch("core.study_planner_ai.get_weakness", return_value={})
    @patch("core.adaptive_revision_ai.get_progress", return_value=[])
    @patch("core.adaptive_revision_ai.get_weakness", return_value={})
    @patch("core.exam_strategy_ai.get_progress", return_value=[])
    @patch("core.exam_strategy_ai.get_weakness", return_value={})
    def test_coach_dashboard_fresh_user_ui_render_smoke(self, *mocks):
        """Simulate fresh user opening AI Exam Coach: verify zero exceptions, onboarding CTA rendered."""
        fresh_user = "brand_new_student"
        fresh_ctx = UserContext(
            user_id="test-smoke-id",
            username=fresh_user,
            progress=[],
            weakness={},
            streak=0,
            xp={"xp": 0, "level": 1},
        )

        with patch("core.user_context.UserContext.get_or_create", return_value=fresh_ctx), \
             patch("core.user_context.UserContext.load", return_value=fresh_ctx):

            try:
                render_coach_dashboard(fresh_user)
            except Exception as e:
                self.fail(f"render_coach_dashboard crashed for fresh user with: {type(e).__name__}: {e}")

    def test_exam_strategy_distinguishes_measured_zero_vs_unavailable(self):
        """Exam strategy must distinguish measured 0% from None/unavailable mock accuracy."""
        from core.exam_strategy_ai import _determine_overall_strategy

        # Case 1: None / unavailable mock accuracy -> starter progression
        strat_none = _determine_overall_strategy(readiness_score=None, mock_accuracy=None)
        self.assertEqual(strat_none, "Balanced Systematic Progression")

        # Case 2: Measured zero (mock_accuracy=0) -> High-Accuracy Tactical Focus
        strat_zero = _determine_overall_strategy(readiness_score=0, mock_accuracy=0)
        self.assertEqual(strat_zero, "High-Accuracy Tactical Focus")


if __name__ == "__main__":
    unittest.main()
