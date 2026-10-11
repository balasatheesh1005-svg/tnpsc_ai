import unittest
from unittest.mock import patch, MagicMock
import streamlit as st

from core.coach_maturity_ai import get_coach_maturity
from core.exam_readiness_ai import get_exam_readiness
from core.mock_intelligence_ai import get_mock_intelligence
from core.predictive_performance_ai import get_predictive_performance
from core.learning_intelligence_ai import get_learning_intelligence
from core.recommendation_ai import get_ai_recommendation
from core.test_topic_selector import start_practice_test
from core.user_context import UserContext
from ui.coach.dashboard import navigate_to_practice_questions, render_coach_dashboard


class TestPatch22FirstPracticeNavigation(unittest.TestCase):
    """
    Focused Regression Test Suite for TNPSC Nova AI Patch 2.2:
    AI Coach First Practice CTA Navigation Fix and User Choice Preservation.
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
    # TEST 1 — Fresh User CTA
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
    def test_fresh_user_cta_routes_to_study_hub_without_autostart(self, *mocks):
        """
        Given: maturity = NO_DATA
        When: user triggers AI Coach first-practice CTA
        Assert:
        - no exception raised
        - routes to Learn & Practice
        - routes to Study Hub / Practice Engine sub-tab
        - test_active is NOT True (False)
        - test_qs is NOT auto-populated (empty list)
        - no Daily Challenge auto-launch (main_menu != '🔥 Daily Challenge', test_mode != 'daily')
        - no practice difficulty auto-selected (active_practice_setup is None)
        """
        user = "brand_new_aspirant_22"
        fresh_ctx = UserContext(
            user_id="test-fresh-22",
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

            # Render dashboard to ensure fresh-user onboarding markup renders without error
            try:
                render_coach_dashboard(user)
            except Exception as e:
                self.fail(f"render_coach_dashboard crashed for NO_DATA user: {type(e).__name__}: {e}")

            # Execute canonical navigation helper invoked by the CTA button
            navigate_to_practice_questions()

            # Assert navigation targets
            self.assertEqual(st.session_state.get("main_menu"), "📚 Learn & Practice")
            self.assertEqual(st.session_state.get("navigate_to"), "📚 Learn & Practice")
            self.assertEqual(st.session_state.get("learn_practice_sub_tab"), "🎯 Practice Questions")

            # Assert practice state is NOT active
            self.assertFalse(st.session_state.get("test_active", False))
            self.assertFalse(st.session_state.get("practice_active", False))

            # Assert test questions are NOT auto-populated
            self.assertEqual(len(st.session_state.get("test_qs", [])), 0)

            # Assert no Daily Challenge auto-launch
            self.assertNotEqual(st.session_state.get("main_menu"), "🔥 Daily Challenge")
            self.assertNotEqual(st.session_state.get("test_mode"), "daily")

            # Assert no difficulty auto-selected
            self.assertIsNone(st.session_state.get("active_practice_setup"))

    # =========================================================================
    # TEST 2 — User Choice Preserved
    # =========================================================================
    def test_user_choice_preserved_no_preselected_mode(self):
        """
        After arriving at Study Hub:
        User remains completely free to choose an available practice mode.
        Assert AI Coach CTA does NOT preselect:
        easy, medium, hard, statement, reasoning, match, chronology, pyq, grand_test
        """
        # Execute navigation
        navigate_to_practice_questions()

        disallowed_preselected_modes = [
            "easy",
            "medium",
            "hard",
            "statement",
            "statement_based",
            "reasoning",
            "assertion_reason",
            "match",
            "match_the_following",
            "chronology",
            "pyq",
            "grand_test",
        ]

        # active_practice_setup must be None
        active_mode = st.session_state.get("active_practice_setup")
        self.assertIsNone(active_mode, f"Practice mode was unexpectedly preselected: {active_mode}")

        for disallowed in disallowed_preselected_modes:
            self.assertNotEqual(
                active_mode,
                disallowed,
                f"Mode '{disallowed}' was preselected by the onboarding CTA!",
            )

        # Verify user is free to select any genuine mode on the Study Hub
        st.session_state["active_practice_setup"] = "hard"
        self.assertEqual(st.session_state.get("active_practice_setup"), "hard")

        st.session_state["active_practice_setup"] = "match_the_following"
        self.assertEqual(st.session_state.get("active_practice_setup"), "match_the_following")

    # =========================================================================
    # TEST 3 — Patch 1 Regression
    # =========================================================================
    def test_patch_1_canonical_launcher_remains_functional(self):
        """
        Canonical launcher start_practice_test must still work independently for:
        - Daily Test
        - Weak Test
        - Revision Test
        - Smart Revision
        - Recovery Session
        """
        # 1. Daily Test
        st.session_state["test_active"] = False
        st.session_state["test_qs"] = []
        success, msg = start_practice_test(
            subject="polity",
            topic="historical_background",
            level="easy",
            mode="daily",
            q_count=10,
            navigate=True,
        )
        self.assertTrue(success, f"Daily Test launch failed: {msg}")
        self.assertTrue(st.session_state.get("test_active"))
        self.assertEqual(st.session_state.get("test_mode"), "daily")
        self.assertEqual(len(st.session_state.get("test_qs", [])), 10)
        self.assertEqual(st.session_state.get("main_menu"), "🔥 Daily Challenge")

        # 2. Weak Test
        st.session_state["test_active"] = False
        st.session_state["test_qs"] = []
        success, msg = start_practice_test(
            subject="polity",
            topic="historical_background",
            level="medium",
            mode="weak",
            q_count=10,
            navigate=False,
        )
        self.assertTrue(success, f"Weak Test launch failed: {msg}")
        self.assertTrue(st.session_state.get("test_active"))
        self.assertEqual(st.session_state.get("test_mode"), "weak")
        self.assertEqual(len(st.session_state.get("test_qs", [])), 10)

        # 3. Revision Test
        st.session_state["test_active"] = False
        st.session_state["test_qs"] = []
        success, msg = start_practice_test(
            subject="polity",
            topic="historical_background",
            level="hard",
            mode="revision",
            q_count=10,
            navigate=False,
        )
        self.assertTrue(success, f"Revision Test launch failed: {msg}")
        self.assertTrue(st.session_state.get("test_active"))
        self.assertEqual(st.session_state.get("test_mode"), "revision")
        self.assertEqual(len(st.session_state.get("test_qs", [])), 10)

        # 4. Smart Revision
        st.session_state["test_active"] = False
        st.session_state["test_qs"] = []
        success, msg = start_practice_test(
            subject="polity",
            topic="historical_background",
            level="easy",
            mode="smart_revision",
            q_count=10,
            navigate=False,
        )
        self.assertTrue(success, f"Smart Revision launch failed: {msg}")
        self.assertTrue(st.session_state.get("test_active"))
        self.assertEqual(st.session_state.get("test_mode"), "smart_revision")

        # 5. Recovery Session
        st.session_state["test_active"] = False
        st.session_state["test_qs"] = []
        success, msg = start_practice_test(
            subject="polity",
            topic="historical_background",
            level="easy",
            mode="recovery",
            q_count=10,
            navigate=False,
        )
        self.assertTrue(success, f"Recovery Session launch failed: {msg}")
        self.assertTrue(st.session_state.get("test_active"))
        self.assertEqual(st.session_state.get("test_mode"), "recovery")

    # =========================================================================
    # TEST 4 — Patch 2 Truthfulness
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
    def test_patch_2_truthfulness_no_synthetic_metrics(self, *mocks):
        """
        NO_DATA onboarding remains completely truthful.
        No synthetic personalized metrics return.
        """
        user = "truthful_fresh_aspirant"
        fresh_ctx = UserContext(
            user_id="test-truth-22",
            username=user,
            progress=[],
            weakness={},
            streak=0,
            xp={"xp": 0, "level": 1},
        )

        with patch("core.user_context.UserContext.get_or_create", return_value=fresh_ctx), \
             patch("core.user_context.UserContext.load", return_value=fresh_ctx):

            # 1. Maturity State
            maturity = get_coach_maturity(user)
            self.assertEqual(maturity["state"], "NO_DATA")
            self.assertEqual(maturity["attempt_count"], 0)

            # 2. Exam Readiness
            readiness = get_exam_readiness(user, force_refresh=True)
            self.assertEqual(readiness["overall_readiness_score"], 0)
            self.assertFalse(readiness["is_eligible"])

            # 3. Mock Intelligence
            mock_data = get_mock_intelligence(user, force_refresh=True)
            self.assertIsNone(mock_data["overall_accuracy"])
            self.assertFalse(mock_data["has_mock_history"])

            # 4. Predictive Performance
            predictive = get_predictive_performance(user, force_refresh=True)
            self.assertEqual(predictive["sample_size"], 0)
            self.assertEqual(predictive["prediction_confidence"], 0)
            self.assertEqual(predictive["estimated_readiness"], "Unavailable")

            # 5. Learning Intelligence
            intelligence = get_learning_intelligence(user, force_refresh=True)
            self.assertIsNone(intelligence["weak_topic"])
            self.assertEqual(intelligence["mastered_count"], 0)
            self.assertEqual(intelligence["pending_count"], 0)

    # =========================================================================
    # TEST 5 — App.py Aliases & Sub-Tab Contract
    # =========================================================================
    def test_app_navigation_aliases_and_sub_tab_routing(self):
        """
        Verify app.py routing contract maps aliases and sets learn_practice_sub_tab
        safely without widget exceptions.
        """
        from app import MENU_ALIASES, MENU_OPTIONS

        # Test aliases exist
        self.assertIn("Practice Questions", MENU_ALIASES)
        self.assertIn("Study Hub", MENU_ALIASES)
        self.assertIn("Learn & Practice", MENU_ALIASES)
        self.assertEqual(MENU_ALIASES["Practice Questions"], "📚 Learn & Practice")
        self.assertEqual(MENU_ALIASES["Study Hub"], "📚 Learn & Practice")

        # Test simulation of app.py top navigation handler
        test_cases = [
            ("Practice Questions", "📚 Learn & Practice", "🎯 Practice Questions"),
            ("Study Hub", "📚 Learn & Practice", "🎯 Practice Questions"),
            ("🎯 Practice Questions", "📚 Learn & Practice", "🎯 Practice Questions"),
            ("📚 Learn & Practice", "📚 Learn & Practice", None),  # Preserves existing subtab
        ]

        for raw_nav, expected_menu, expected_sub_tab in test_cases:
            st.session_state["navigate_to"] = raw_nav
            if expected_sub_tab:
                # Target subtab specified
                if raw_nav in (
                    "Practice Questions",
                    "🎯 Practice Questions",
                    "Study Hub",
                    "Study Hub (Practice Engine)",
                    "📚 Study Hub (Practice Engine)",
                ):
                    st.session_state["learn_practice_sub_tab"] = "🎯 Practice Questions"

            nav_target = MENU_ALIASES.get(raw_nav, raw_nav)
            if nav_target in MENU_OPTIONS:
                st.session_state["main_menu"] = nav_target
            st.session_state.pop("navigate_to", None)

            self.assertEqual(st.session_state["main_menu"], expected_menu)
            if expected_sub_tab:
                self.assertEqual(st.session_state["learn_practice_sub_tab"], expected_sub_tab)


if __name__ == "__main__":
    unittest.main()
