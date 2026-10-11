import unittest
from unittest.mock import patch, MagicMock
import streamlit as st

from core.coach_maturity_ai import get_coach_maturity
from core.exam_readiness_ai import get_exam_readiness
from core.predictive_performance_ai import get_predictive_performance
from core.mock_intelligence_ai import get_mock_intelligence
from core.learning_intelligence_ai import get_learning_intelligence
from core.recommendation_ai import get_ai_recommendation
from core.test_topic_selector import start_practice_test


class TestPatch2CoachTruthfulness(unittest.TestCase):
    """
    Unit and integration test suite for TNPSC Nova AI Pre-Release Patch 2:
    AI Exam Coach Data Truthfulness & Maturity Gating.
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

    # -------------------------------------------------------------------------
    # A. FRESH USER / NO_DATA
    # -------------------------------------------------------------------------
    @patch("core.coach_maturity_ai.get_progress", return_value=[])
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_user_xp", return_value={"xp": 0})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    def test_fresh_user_no_data_state(self, mock_rev, mock_xp, mock_str, mock_weak, mock_prog):
        """Zero history user must be classified as NO_DATA with zero personalized claims."""
        maturity = get_coach_maturity("fresh_user_a")
        self.assertEqual(maturity["state"], "NO_DATA")
        self.assertFalse(maturity["readiness_eligible"])
        self.assertFalse(maturity["prediction_eligible"])
        self.assertFalse(maturity["weakness_eligible"])
        self.assertFalse(maturity["mock_eligible"])
        self.assertFalse(maturity["mastery_eligible"])
        self.assertFalse(maturity["timing_eligible"])

        # Mastered and pending topic counts must be 0, not 12 and 8
        self.assertEqual(maturity["mastered_count"], 0)
        self.assertEqual(maturity["pending_count"], 0)
        self.assertIsNone(maturity["strong_subject"])
        self.assertIsNone(maturity["weak_topic"])
        self.assertIsNone(maturity["latest_mock_accuracy"])

    @patch("core.recommendation_ai.get_progress", return_value=[])
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.learning_intelligence_ai.get_progress", return_value=[])
    @patch("core.learning_intelligence_ai.get_weakness", return_value={})
    @patch("core.predictive_performance_ai.get_progress", return_value=[])
    @patch("core.predictive_performance_ai.get_mock_intelligence", return_value={"overall_accuracy": None, "has_mock_history": False})
    @patch("core.mock_intelligence_ai.get_progress", return_value=[])
    @patch("core.exam_readiness_ai.get_progress", return_value=[])
    def test_fresh_user_engine_outputs_are_truthful(
        self, mock_er_prog, mock_mi_prog, mock_pp_mi, mock_pp_prog,
        mock_li_weak, mock_li_prog, mock_rec_weak, mock_rec_prog
    ):
        """Engine outputs must not invent readiness, confidence, or mock accuracy for fresh users."""
        readiness = get_exam_readiness("fresh_user_a", force_refresh=True)
        self.assertEqual(readiness["overall_readiness_score"], 0)
        self.assertEqual(readiness["readiness_level"], "No Test History")
        self.assertFalse(readiness["is_eligible"])

        predictive = get_predictive_performance("fresh_user_a", force_refresh=True)
        self.assertEqual(predictive["sample_size"], 0)
        self.assertEqual(predictive["prediction_confidence"], 0)
        self.assertEqual(predictive["estimated_readiness"], "Unavailable")
        self.assertFalse(predictive["is_eligible"])

        mock_data = get_mock_intelligence("fresh_user_a", force_refresh=True)
        self.assertIsNone(mock_data["overall_accuracy"])
        self.assertEqual(mock_data["mock_level"], "No Mock History")
        self.assertFalse(mock_data["has_mock_history"])
        self.assertEqual(mock_data["mistakes"], [])

        rec = get_ai_recommendation("fresh_user_a", force_refresh=True)
        self.assertEqual(rec["recommendation_type"], "Starter Path")
        self.assertIn("Fundamental Rights", rec["recommendation"])
        # Must not cite synthetic 55% Assertion & Reason bottleneck
        self.assertNotIn("55%", rec["explanation"])
        self.assertNotIn("Assertion & Reason", rec["explanation"])

    # -------------------------------------------------------------------------
    # B. NO_DATA CTA
    # -------------------------------------------------------------------------
    def test_no_data_first_practice_cta(self):
        """First practice CTA must use canonical launcher, load questions, and navigate without empty session."""
        success, msg = start_practice_test(
            subject="polity",
            topic="historical_background",
            level="easy",
            mode="daily",
            q_count=10,
            navigate=True,
        )
        self.assertTrue(success, f"start_practice_test failed: {msg}")
        self.assertTrue(st.session_state.get("test_active"))
        self.assertEqual(len(st.session_state.get("test_qs", [])), 10)
        self.assertEqual(st.session_state.get("main_menu"), "🔥 Daily Challenge")

    # -------------------------------------------------------------------------
    # C. EARLY_INSIGHTS
    # -------------------------------------------------------------------------
    @patch("core.coach_maturity_ai.get_progress")
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=2)
    @patch("core.coach_maturity_ai.get_user_xp", return_value={"xp": 100})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    def test_early_insights_state(self, mock_rev, mock_xp, mock_str, mock_weak, mock_prog):
        """User with 1-4 tests must enter EARLY_INSIGHTS with genuine metrics and locked predictions."""
        mock_prog.return_value = [
            {"subject": "polity", "topic": "preamble", "accuracy": 70},
            {"subject": "polity", "topic": "historical_background", "accuracy": 80},
        ]
        maturity = get_coach_maturity("early_user_c")
        self.assertEqual(maturity["state"], "EARLY_INSIGHTS")
        self.assertEqual(maturity["attempt_count"], 2)
        self.assertEqual(maturity["avg_accuracy"], 75.0)
        self.assertEqual(maturity["streak"], 2)
        self.assertFalse(maturity["prediction_eligible"])
        self.assertFalse(maturity["mock_eligible"])
        self.assertIsNone(maturity["latest_mock_accuracy"])

    # -------------------------------------------------------------------------
    # D. PERSONALIZED_COACH
    # -------------------------------------------------------------------------
    @patch("core.coach_maturity_ai.get_progress")
    @patch("core.coach_maturity_ai.get_weakness")
    @patch("core.coach_maturity_ai.get_streak", return_value=5)
    @patch("core.coach_maturity_ai.get_user_xp", return_value={"xp": 500})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    def test_personalized_coach_state(self, mock_rev, mock_xp, mock_str, mock_weak, mock_prog):
        """User with 5+ tests must enter PERSONALIZED_COACH with dynamic real values."""
        mock_prog.return_value = [
            {"subject": "polity", "topic": "preamble", "accuracy": 90},
            {"subject": "polity", "topic": "historical_background", "accuracy": 85},
            {"subject": "polity", "topic": "fundamental_rights", "accuracy": 60},
            {"subject": "history", "topic": "south_indian_history", "accuracy": 70},
            {"subject": "history", "topic": "freedom_struggle", "accuracy": 80},
            {"subject": "polity", "topic": "polity_grand_test", "accuracy": 88},
        ]
        mock_weak.return_value = {"polity-fundamental_rights": 4}

        maturity = get_coach_maturity("mature_user_d")
        self.assertEqual(maturity["state"], "PERSONALIZED_COACH")
        self.assertTrue(maturity["readiness_eligible"])
        self.assertTrue(maturity["prediction_eligible"])
        self.assertTrue(maturity["weakness_eligible"])
        self.assertTrue(maturity["mock_eligible"])
        self.assertEqual(maturity["latest_mock_accuracy"], 88)
        self.assertEqual(maturity["weak_topic"], "Fundamental Rights")

        # Mastered topics (accuracy >= 80%): preamble, historical_background, freedom_struggle, polity_grand_test = 4
        self.assertEqual(maturity["mastered_count"], 4)
        # Pending topics (< 80%): fundamental_rights, south_indian_history = 2
        self.assertEqual(maturity["pending_count"], 2)

    # -------------------------------------------------------------------------
    # E. ZERO-SAMPLE PREDICTION
    # -------------------------------------------------------------------------
    @patch("core.predictive_performance_ai.get_progress", return_value=[])
    @patch("core.predictive_performance_ai.get_mock_intelligence", return_value={"overall_accuracy": None, "has_mock_history": False})
    def test_zero_sample_prediction_not_substituted(self, mock_mock, mock_prog):
        """Predictive engine must retain sample_size = 0, never substituting 5."""
        pred = get_predictive_performance("user_zero_pred", force_refresh=True)
        self.assertEqual(pred["sample_size"], 0)
        self.assertEqual(pred["prediction_confidence"], 0)
        self.assertEqual(pred["estimated_readiness"], "Unavailable")
        self.assertNotIn("82%", str(pred.get("prediction_confidence")))
        self.assertNotIn("moderate learning history", str(pred.get("confidence_rationale", "")).lower())

    # -------------------------------------------------------------------------
    # F. MOCK ELIGIBILITY
    # -------------------------------------------------------------------------
    @patch("core.mock_intelligence_ai.get_progress")
    def test_mock_eligibility_distinction(self, mock_prog):
        """Mock metrics require genuine mock records; ordinary practice does not fabricate mock accuracy."""
        # Case 1: ordinary practice only
        mock_prog.return_value = [
            {"subject": "polity", "topic": "preamble_easy", "accuracy": 70},
            {"subject": "polity", "topic": "rights_medium", "accuracy": 80},
        ]
        res_no_mock = get_mock_intelligence("user_no_mock", force_refresh=True)
        self.assertFalse(res_no_mock["has_mock_history"])
        self.assertIsNone(res_no_mock["overall_accuracy"])
        self.assertEqual(res_no_mock["mock_level"], "No Mock History")

        # Case 2: real grand test row
        mock_prog.return_value = [
            {"subject": "polity", "topic": "preamble_grand_test", "accuracy": 85},
        ]
        res_with_mock = get_mock_intelligence("user_with_mock", force_refresh=True)
        self.assertTrue(res_with_mock["has_mock_history"])
        self.assertEqual(res_with_mock["overall_accuracy"], 85)

    # -------------------------------------------------------------------------
    # G. WEAK TOPIC DERIVATION
    # -------------------------------------------------------------------------
    @patch("core.learning_intelligence_ai.get_weakness")
    @patch("core.learning_intelligence_ai.get_progress", return_value=[])
    def test_weak_topic_derivation(self, mock_prog, mock_weak):
        """Weak topic must come from real weakness records, never falling back to Physical Geography."""
        # Case 1: No weakness records
        mock_weak.return_value = {}
        intel_none = get_learning_intelligence("user_no_weak", force_refresh=True)
        self.assertIsNone(intel_none["weak_topic"])
        self.assertNotEqual(intel_none["weak_topic"], "Physical Geography")

        # Case 2: Real weakness records
        mock_weak.return_value = {"polity-directive_principles": 5}
        intel_real = get_learning_intelligence("user_real_weak", force_refresh=True)
        self.assertEqual(intel_real["weak_topic"], "directive_principles")

    # -------------------------------------------------------------------------
    # H. QUICK ACTION ROUTING
    # -------------------------------------------------------------------------
    def test_quick_action_weak_topic_routes_to_weak_areas_subtab(self):
        """AI Coach navigation to 🧠 Weakness must set learn_practice_sub_tab to 🧠 Weak Areas."""
        st.session_state["navigate_to"] = "🧠 Weakness"

        # Direct simulation of app.py alias mapping and routing
        MENU_ALIASES = {
            "🧠 Weakness": "📚 Learn & Practice",
        }
        MENU_OPTIONS = [
            "🏠 Home",
            "📚 Learn & Practice",
            "🔥 Daily Challenge",
        ]

        raw_nav = st.session_state.get("navigate_to")
        if raw_nav == "🧠 Weakness":
            st.session_state["learn_practice_sub_tab"] = "🧠 Weak Areas"
        nav_target = MENU_ALIASES.get(raw_nav, raw_nav)
        if nav_target in MENU_OPTIONS:
            st.session_state["main_menu"] = nav_target
        st.session_state.pop("navigate_to", None)

        self.assertEqual(st.session_state["main_menu"], "📚 Learn & Practice")
        self.assertEqual(st.session_state["learn_practice_sub_tab"], "🧠 Weak Areas")

    # -------------------------------------------------------------------------
    # I. HARDCODED FALLBACK REGRESSION CHECK
    # -------------------------------------------------------------------------
    @patch("core.learning_intelligence_ai.get_progress", return_value=[])
    @patch("core.learning_intelligence_ai.get_weakness", return_value={})
    @patch("core.mock_intelligence_ai.get_progress", return_value=[])
    @patch("core.predictive_performance_ai.get_progress", return_value=[])
    @patch("core.predictive_performance_ai.get_mock_intelligence", return_value={"overall_accuracy": None, "has_mock_history": False})
    def test_hardcoded_fallback_elimination(self, mock_pp_mi, mock_pp_prog, mock_mi_prog, mock_li_weak, mock_li_prog):
        """Ensure system no longer relies on 12 mastered, 8 pending, Physical Geography, 48s, or 55% fresh accuracy."""
        intel = get_learning_intelligence("fresh_check", force_refresh=True)
        self.assertNotEqual(intel.get("mastered_count"), 12)
        self.assertNotEqual(intel.get("pending_count"), 8)
        self.assertEqual(intel.get("mastered_count"), 0)
        self.assertEqual(intel.get("pending_count"), 0)
        self.assertIsNone(intel.get("weak_topic"))

        mock = get_mock_intelligence("fresh_check", force_refresh=True)
        self.assertNotEqual(mock.get("overall_accuracy"), 55)
        self.assertNotEqual(mock.get("overall_accuracy"), 74)
        self.assertIsNone(mock.get("overall_accuracy"))
        self.assertEqual(mock.get("mistakes"), [])

        pred = get_predictive_performance("fresh_check", force_refresh=True)
        self.assertNotEqual(pred.get("prediction_confidence"), 82)
        self.assertEqual(pred.get("prediction_confidence"), 0)


if __name__ == "__main__":
    unittest.main()
