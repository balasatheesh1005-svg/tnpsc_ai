import unittest
from unittest.mock import patch
import streamlit as st

from core.recommendation_ai import get_ai_recommendation
from core.user_context import UserContext
from ui.components.cards import recommendation_hero_card_html, recommendation_risk_alert_html


class TestRecommendationTruth(unittest.TestCase):
    """
    Comprehensive truth audit and evidence gating test matrix for AI Recommendation Engine.
    Covers Cases 1 to 10 as specified in P1 Batch 2 specification.
    """

    def setUp(self):
        for key in list(st.session_state.keys()):
            del st.session_state[key]

    def tearDown(self):
        for key in list(st.session_state.keys()):
            del st.session_state[key]

    # -------------------------------------------------------------------------
    # CASE 1 — ZERO DATA
    # -------------------------------------------------------------------------
    @patch("core.recommendation_ai.get_progress", return_value=[])
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.recommendation_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_progress", return_value=[])
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    @patch("core.learning_intelligence_ai.get_progress", return_value=[])
    @patch("core.learning_intelligence_ai.get_weakness", return_value={})
    def test_case_1_zero_data(self, *mocks):
        """Zero-data learner receives useful starting path with zero synthetic claims."""
        rec = get_ai_recommendation("fresh_user_zero", force_refresh=True)

        self.assertEqual(rec["recommendation_type"], "Starter Path")
        self.assertIn("Fundamental Rights", rec["recommendation"])
        self.assertEqual(rec["risk"], "No Diagnostic Baseline")
        self.assertEqual(rec["risk_level"], "Low")

        # No fake confidence %
        self.assertIsNone(rec["confidence"])
        self.assertEqual(rec["evidence_tier"], "TIER_0_NO_DATA")
        self.assertEqual(rec["evidence_label"], "No Data")

        # No fake weakness
        self.assertNotIn("weak topic", rec["explanation"].lower())

        # No fake mastery gain or fake XP
        benefit = rec["estimated_benefit"]
        self.assertNotIn("+5%", str(benefit))
        self.assertNotIn("+10%", str(benefit))
        self.assertNotIn("+40 XP", str(benefit))
        self.assertNotIn("+50 XP", str(benefit))

        # Hero card renders cleanly without error or numeric percentage
        hero_html = recommendation_hero_card_html(rec).markup
        self.assertNotIn("% AI Confidence", hero_html)
        self.assertIn("Evidence: No Data", hero_html)

    # -------------------------------------------------------------------------
    # CASE 2 — TWO ATTEMPTS / 80% (LOW-DATA REPRODUCTION)
    # -------------------------------------------------------------------------
    @patch("core.recommendation_ai.get_streak", return_value=0)
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    def test_case_2_two_attempts_80_percent(self, *mocks):
        """Two attempts at 80% should be classified as Early Signal without fake 75% confidence."""
        sample_progress = [
            {"id": "1", "subject": "History", "topic": "Indus Valley", "accuracy": 80.0},
            {"id": "2", "subject": "History", "topic": "Indus Valley", "accuracy": 80.0},
        ]
        ctx = UserContext(
            user_id="u_two_att",
            username="u_two_att",
            progress=sample_progress,
            weakness={},
            streak=0,
            xp={"xp": 20, "level": 1},
        )

        with patch("core.recommendation_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_weakness", return_value={}):

            rec = get_ai_recommendation("u_two_att", context=ctx, force_refresh=True)

            # Evidence tier must reflect Early Signal
            self.assertEqual(rec["evidence_tier"], "TIER_1_EARLY_SIGNAL")
            self.assertEqual(rec["evidence_label"], "Early Signal")
            self.assertIsNone(rec["confidence"])

            # Risk must be grounded, not an ungrounded habit judgment
            self.assertEqual(rec["risk"], "Early Learning Baseline")
            self.assertEqual(rec["risk_level"], "Low")
            self.assertNotIn("Low Revision Habit", rec["risk"])

    # -------------------------------------------------------------------------
    # CASE 3 — NO REVISION HISTORY
    # -------------------------------------------------------------------------
    @patch("core.recommendation_ai.get_streak", return_value=1)
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=1)
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    def test_case_3_no_revision_history_does_not_infer_habit(self, *mocks):
        """Learners without revision history must not be labeled with a 'Low Revision Habit'."""
        sample_progress = [
            {"id": "1", "subject": "Polity", "topic": "Preamble", "accuracy": 70.0},
            {"id": "2", "subject": "Polity", "topic": "Preamble", "accuracy": 75.0},
        ]
        ctx = UserContext(
            user_id="u_no_rev",
            username="u_no_rev",
            progress=sample_progress,
            weakness={},
            streak=1,
            xp={"xp": 20, "level": 1},
        )

        with patch("core.recommendation_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_weakness", return_value={}):

            rec = get_ai_recommendation("u_no_rev", context=ctx, force_refresh=True)
            self.assertNotEqual(rec["risk"], "Low Revision Habit")
            self.assertNotIn("Low Revision Habit", rec["risk_description"])

    # -------------------------------------------------------------------------
    # CASE 4 — REAL WEAKNESS
    # -------------------------------------------------------------------------
    @patch("core.recommendation_ai.get_streak", return_value=2)
    @patch("core.coach_maturity_ai.get_streak", return_value=2)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    def test_case_4_real_weakness(self, *mocks):
        """When actual weakness exists, recommendation reason must ground in that weakness."""
        sample_progress = [
            {"id": "1", "subject": "History", "topic": "Guptas", "accuracy": 40.0},
            {"id": "2", "subject": "History", "topic": "Guptas", "accuracy": 35.0},
            {"id": "3", "subject": "History", "topic": "Guptas", "accuracy": 45.0},
        ]
        sample_weakness = {"history-guptas": 5}
        ctx = UserContext(
            user_id="u_weak",
            username="u_weak",
            progress=sample_progress,
            weakness=sample_weakness,
            streak=2,
            xp={"xp": 50, "level": 1},
        )

        with patch("core.recommendation_ai.get_progress", return_value=sample_progress), \
             patch("core.recommendation_ai.get_weakness", return_value=sample_weakness), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_weakness", return_value=sample_weakness), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_weakness", return_value=sample_weakness):

            rec = get_ai_recommendation("u_weak", context=ctx, force_refresh=True)

            self.assertEqual(rec["recommendation_type"], "Continue Recovery")
            self.assertIn("Guptas", rec["recommendation"])
            self.assertEqual(rec["priority"], "High")
            self.assertEqual(rec["risk"], "Concept Weakness Identified")
            self.assertEqual(rec["risk_level"], "High")
            self.assertIn("Guptas", rec["risk_description"])

    # -------------------------------------------------------------------------
    # CASE 5 — DIFFICULTY PROGRESSION
    # -------------------------------------------------------------------------
    @patch("core.recommendation_ai.get_streak", return_value=3)
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=3)
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    def test_case_5_difficulty_progression(self, *mocks):
        """Difficulty recommendation remains structured and deterministic."""
        sample_progress = [
            {"id": "1", "subject": "Polity", "topic": "Parliament", "accuracy": 90.0},
            {"id": "2", "subject": "Polity", "topic": "Parliament", "accuracy": 90.0},
            {"id": "3", "subject": "Polity", "topic": "Parliament", "accuracy": 85.0},
            {"id": "4", "subject": "Polity", "topic": "Parliament", "accuracy": 95.0},
            {"id": "5", "subject": "Polity", "topic": "Parliament", "accuracy": 90.0},
        ]
        ctx = UserContext(
            user_id="u_diff",
            username="u_diff",
            progress=sample_progress,
            weakness={},
            streak=3,
            xp={"xp": 100, "level": 2},
        )

        with patch("core.recommendation_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_weakness", return_value={}):

            rec = get_ai_recommendation("u_diff", context=ctx, force_refresh=True)
            self.assertIn(rec["repository"], ["Easy Repository", "Medium Repository", "Hard Repository", "Foundation Repository"])
            self.assertIsInstance(rec["question_type"], str)

    # -------------------------------------------------------------------------
    # CASE 6 — XP TRUTH
    # -------------------------------------------------------------------------
    @patch("core.recommendation_ai.get_progress", return_value=[])
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_progress", return_value=[])
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    @patch("core.learning_intelligence_ai.get_progress", return_value=[])
    @patch("core.learning_intelligence_ai.get_weakness", return_value={})
    def test_case_6_xp_truth(self, *mocks):
        """Precise fixed XP claim (+40 XP or +50 XP) must be absent."""
        rec = get_ai_recommendation("u_xp", force_refresh=True)
        benefit = rec["estimated_benefit"]

        self.assertNotIn("+40 XP", str(benefit.get("xp")))
        self.assertNotIn("+50 XP", str(benefit.get("xp")))
        self.assertIn("XP", str(benefit.get("xp")))

    # -------------------------------------------------------------------------
    # CASE 7 — MASTERY IMPACT TRUTH
    # -------------------------------------------------------------------------
    @patch("core.recommendation_ai.get_progress", return_value=[{"id": "1", "accuracy": 70.0}])
    @patch("core.recommendation_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_progress", return_value=[{"id": "1", "accuracy": 70.0}])
    @patch("core.coach_maturity_ai.get_weakness", return_value={})
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    @patch("core.learning_intelligence_ai.get_progress", return_value=[{"id": "1", "accuracy": 70.0}])
    @patch("core.learning_intelligence_ai.get_weakness", return_value={})
    def test_case_7_mastery_impact_truth(self, *mocks):
        """Unsupported numeric future mastery gains like +5% or +10% must be absent."""
        rec = get_ai_recommendation("u_mastery", force_refresh=True)
        benefit = rec["estimated_benefit"]

        self.assertNotIn("+5%", str(benefit.get("mastery")))
        self.assertNotIn("+10%", str(benefit.get("mastery")))
        self.assertNotIn("+15%", str(benefit.get("mastery")))
        self.assertNotIn("+20%", str(benefit.get("mastery")))
        # Must be qualitative
        self.assertIsInstance(benefit.get("focus") or benefit.get("mastery"), str)

    # -------------------------------------------------------------------------
    # CASE 8 — RICHER DATA
    # -------------------------------------------------------------------------
    def test_case_8_richer_data(self):
        """With sufficient attempts, recommendation remains valid and evidence tier is Reliable or Developing."""
        sample_progress = [
            {"id": str(i), "subject": "History" if i < 4 else ("Polity" if i < 8 else "Geography"),
             "topic": f"Topic_{i}", "accuracy": 75.0 + (i % 15)}
            for i in range(12)
        ]
        sample_progress.append({"id": "13", "subject": "General", "topic": "grand_test_1", "accuracy": 82.0})

        ctx = UserContext(
            user_id="u_rich",
            username="u_rich",
            progress=sample_progress,
            weakness={},
            streak=5,
            xp={"xp": 650, "level": 4},
        )

        with patch("core.recommendation_ai.get_progress", return_value=sample_progress), \
             patch("core.recommendation_ai.get_weakness", return_value={}), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_weakness", return_value={}), \
             patch("core.coach_maturity_ai.get_streak", return_value=5), \
             patch("core.coach_maturity_ai.get_revision_overview", return_value={}), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_weakness", return_value={}):

            rec = get_ai_recommendation("u_rich", context=ctx, force_refresh=True)

            self.assertIn(rec["evidence_label"], ["Developing", "Reliable"])
            self.assertIsNone(rec["confidence"])
            self.assertTrue(len(rec["recommendation"]) > 0)

    # -------------------------------------------------------------------------
    # CASE 9 — NONE / MISSING DATA SAFETY
    # -------------------------------------------------------------------------
    @patch("core.recommendation_ai.get_progress", return_value=None)
    @patch("core.recommendation_ai.get_weakness", return_value=None)
    @patch("core.recommendation_ai.get_streak", return_value=None)
    @patch("core.coach_maturity_ai.get_progress", return_value=None)
    @patch("core.coach_maturity_ai.get_weakness", return_value=None)
    @patch("core.coach_maturity_ai.get_streak", return_value=None)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value=None)
    @patch("core.learning_intelligence_ai.get_progress", return_value=None)
    @patch("core.learning_intelligence_ai.get_weakness", return_value=None)
    def test_case_9_none_missing_data_resilience(self, *mocks):
        """Engine must not crash with TypeError or produce None% when upstream data is None."""
        rec = get_ai_recommendation("u_none", force_refresh=True)

        self.assertIsNotNone(rec)
        self.assertIsInstance(rec["recommendation"], str)
        self.assertIsNone(rec["confidence"])
        self.assertNotIn("None%", str(rec))

        # Hero card must render cleanly
        hero_html = recommendation_hero_card_html(rec).markup
        self.assertNotIn("None%", hero_html)

        # Risk alert card must render cleanly
        risk_html = recommendation_risk_alert_html(rec).markup
        self.assertNotIn("None", risk_html)

    # -------------------------------------------------------------------------
    # CASE 10 — REASON EVIDENCE GROUNDING
    # -------------------------------------------------------------------------
    @patch("core.recommendation_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value={})
    def test_case_10_reason_evidence_grounding(self, *mocks):
        """Reasons must strictly reflect the presence or absence of evidence."""
        # 1. With overdue items: reason must mention overdue revisions
        overdue_analytics = {
            "overdue": [{"topic": "indus_valley"}],
            "due_today": [],
            "progress": {"percentage": 20},
        }
        with patch("core.recommendation_ai.get_progress", return_value=[{"id": "1", "accuracy": 70.0}]), \
             patch("core.recommendation_ai.get_weakness", return_value={}), \
             patch("core.recommendation_ai.get_revision_analytics_v2", return_value=overdue_analytics), \
             patch("core.coach_maturity_ai.get_progress", return_value=[{"id": "1", "accuracy": 70.0}]), \
             patch("core.coach_maturity_ai.get_weakness", return_value={}), \
             patch("core.learning_intelligence_ai.get_progress", return_value=[{"id": "1", "accuracy": 70.0}]), \
             patch("core.learning_intelligence_ai.get_weakness", return_value={}):

            rec = get_ai_recommendation("u_overdue", force_refresh=True)
            self.assertEqual(rec["risk"], "Overdue Revision Risk")
            self.assertEqual(rec["priority"], "Critical")
            self.assertIn("overdue", rec["explanation"].lower())


if __name__ == "__main__":
    unittest.main()
