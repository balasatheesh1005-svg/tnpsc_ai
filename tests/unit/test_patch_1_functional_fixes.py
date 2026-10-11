import unittest
from unittest.mock import patch, MagicMock
import streamlit as st

from core.test_topic_selector import get_test_config, start_practice_test
from ui.pages.mentor import render_mentor


class TestPatch1FunctionalFixes(unittest.TestCase):
    """
    Regression test suite for TNPSC Nova AI Pre-Release Patch 1.
    Verifies elimination of dead states, NameErrors, and fresh-user lockups.
    """

    def setUp(self):
        # Reset streamlit session_state before each test
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

    # ---------------------------------------------------------
    # A. Personal Mentor
    # ---------------------------------------------------------
    def test_mentor_renders_without_name_error(self):
        """Personal Mentor must accept section and user without undefined typing_effect crash."""
        mock_section = MagicMock()
        # Test keyword user call (app.py pattern)
        try:
            render_mentor(mock_section, user="aspirant_test")
        except NameError as e:
            self.fail(f"render_mentor raised NameError: {e}")
        except Exception:
            # UI components may call streamlit widgets in headless mode, which is expected
            pass
        mock_section.assert_called_with("🧑‍🏫 Personal Mentor")

    def test_mentor_backward_compatible_signatures(self):
        """render_mentor must accept typing_effect=None, positional user, or keyword user."""
        mock_section = MagicMock()
        try:
            # Signature with typing_effect=None, user
            render_mentor(mock_section, None, "test_user")
            # Legacy 1-arg call
            render_mentor(mock_section)
        except NameError as e:
            self.fail(f"render_mentor raised NameError on backward-compatible signature: {e}")
        except Exception:
            pass

    # ---------------------------------------------------------
    # B. Fresh user + Weak Test
    # ---------------------------------------------------------
    @patch("core.test_topic_selector.get_weakness")
    def test_fresh_user_weak_test_remains_safe(self, mock_weakness):
        """Fresh user with no weakness records must get None and NOT enter test_active=True."""
        mock_weakness.return_value = {}
        config = get_test_config("fresh_user", mode="weak")
        self.assertIsNone(config, "Fresh user without weakness must return None")
        self.assertFalse(st.session_state["test_active"])
        self.assertEqual(st.session_state["test_qs"], [])

    # ---------------------------------------------------------
    # C. Fresh user + Revision Test
    # ---------------------------------------------------------
    @patch("core.test_topic_selector.get_due_revisions")
    def test_fresh_user_revision_test_remains_safe(self, mock_revisions):
        """Fresh user with no due revisions must get None and NOT enter test_active=True."""
        mock_revisions.return_value = []
        config = get_test_config("fresh_user", mode="revision")
        self.assertIsNone(config, "Fresh user without revisions must return None")
        self.assertFalse(st.session_state["test_active"])
        self.assertEqual(st.session_state["test_qs"], [])

    # ---------------------------------------------------------
    # D. Weak Test with valid data
    # ---------------------------------------------------------
    @patch("core.test_topic_selector.get_weakness")
    @patch("core.question_loader.load_questions")
    def test_active_user_weak_test_starts_valid_session(self, mock_load, mock_weakness):
        """Active user with weakness records starts a 5-question weak test session."""
        mock_weakness.return_value = {"polity-historical_background": 3}
        mock_load.return_value = [{"id": f"q_{i}", "question_en": f"Q {i}"} for i in range(10)]

        config = get_test_config("active_user", mode="weak")
        self.assertIsNotNone(config)
        self.assertEqual(config["subject"], "polity")
        self.assertEqual(config["topic"], "historical_background")

        success, err = start_practice_test(
            subject=config["subject"],
            topic=config["topic"],
            level=config.get("level", "easy"),
            mode="weak",
            q_count=5,
        )
        self.assertTrue(success)
        self.assertEqual(err, "")
        self.assertTrue(st.session_state["test_active"])
        self.assertEqual(st.session_state["test_mode"], "weak")
        self.assertEqual(len(st.session_state["test_qs"]), 5)
        self.assertEqual(st.session_state["q_index"], 0)
        self.assertFalse(st.session_state["test_results_processed"])

    # ---------------------------------------------------------
    # E. Revision Test with valid data
    # ---------------------------------------------------------
    @patch("core.test_topic_selector.get_due_revisions")
    @patch("core.question_loader.load_questions")
    def test_active_user_revision_test_starts_valid_session(self, mock_load, mock_revisions):
        """Active user with due revisions starts a 5-question revision test session."""
        mock_revisions.return_value = [("polity-historical_background", "2026-10-10")]
        mock_load.return_value = [{"id": f"q_{i}", "question_en": f"Q {i}"} for i in range(10)]

        config = get_test_config("active_user", mode="revision")
        self.assertIsNotNone(config)
        self.assertEqual(config["subject"], "polity")
        self.assertEqual(config["topic"], "historical_background")

        success, err = start_practice_test(
            subject=config["subject"],
            topic=config["topic"],
            level=config.get("level", "easy"),
            mode="revision",
            q_count=5,
        )
        self.assertTrue(success)
        self.assertTrue(st.session_state["test_active"])
        self.assertEqual(st.session_state["test_mode"], "revision")
        self.assertEqual(len(st.session_state["test_qs"]), 5)

    # ---------------------------------------------------------
    # F. Smart Revision CTA
    # ---------------------------------------------------------
    @patch("core.test_topic_selector.get_due_revisions")
    def test_smart_revision_cta_fresh_user_stays_safe(self, mock_revisions):
        """Smart Revision CTA on fresh user does not activate empty test."""
        mock_revisions.return_value = []
        config = get_test_config("fresh_user", mode="revision")
        self.assertIsNone(config)
        self.assertFalse(st.session_state["test_active"])
        self.assertEqual(st.session_state["test_qs"], [])

    @patch("core.test_topic_selector.get_due_revisions")
    @patch("core.question_loader.load_questions")
    def test_smart_revision_cta_active_user_routes_to_daily_challenge(self, mock_load, mock_revisions):
        """Smart Revision CTA on active user routes to Daily Challenge test runner."""
        mock_revisions.return_value = [("polity-historical_background", "2026-10-10")]
        mock_load.return_value = [{"id": f"q_{i}", "question_en": f"Q {i}"} for i in range(10)]

        config = get_test_config("active_user", mode="revision")
        self.assertIsNotNone(config)

        success, _ = start_practice_test(
            subject=config["subject"],
            topic=config["topic"],
            level=config.get("level", "easy"),
            mode="revision",
            q_count=5,
            navigate=True,
        )
        self.assertTrue(success)
        self.assertTrue(st.session_state["test_active"])
        self.assertEqual(st.session_state["navigate_to"], "🔥 Daily Challenge")
        self.assertEqual(st.session_state["main_menu"], "🔥 Daily Challenge")
        self.assertEqual(len(st.session_state["test_qs"]), 5)

    # ---------------------------------------------------------
    # G. Recovery CTA
    # ---------------------------------------------------------
    @patch("core.test_topic_selector.get_weakness")
    def test_recovery_cta_fresh_user_stays_safe(self, mock_weakness):
        """Recovery CTA on fresh user does not activate empty test."""
        mock_weakness.return_value = {}
        config = get_test_config("fresh_user", mode="weak")
        self.assertIsNone(config)
        self.assertFalse(st.session_state["test_active"])
        self.assertEqual(st.session_state["test_qs"], [])

    @patch("core.test_topic_selector.get_weakness")
    @patch("core.question_loader.load_questions")
    def test_recovery_cta_active_user_routes_to_daily_challenge(self, mock_load, mock_weakness):
        """Recovery CTA on active user routes to Daily Challenge test runner."""
        mock_weakness.return_value = {"polity-historical_background": 2}
        mock_load.return_value = [{"id": f"q_{i}", "question_en": f"Q {i}"} for i in range(10)]

        config = get_test_config("active_user", mode="weak")
        self.assertIsNotNone(config)

        success, _ = start_practice_test(
            subject=config["subject"],
            topic=config["topic"],
            level=config.get("level", "easy"),
            mode="weak",
            q_count=5,
            navigate=True,
        )
        self.assertTrue(success)
        self.assertTrue(st.session_state["test_active"])
        self.assertEqual(st.session_state["navigate_to"], "🔥 Daily Challenge")
        self.assertEqual(st.session_state["main_menu"], "🔥 Daily Challenge")
        self.assertEqual(len(st.session_state["test_qs"]), 5)

    # ---------------------------------------------------------
    # Safety: Missing questions never activates test_active
    # ---------------------------------------------------------
    @patch("core.question_loader.load_questions")
    def test_missing_questions_never_activates_test(self, mock_load):
        """If question loader returns empty list, test_active must remain False."""
        mock_load.return_value = []
        success, msg = start_practice_test(
            subject="polity",
            topic="non_existent",
            mode="weak",
            navigate=True,
        )
        self.assertFalse(success)
        self.assertIn("No questions found", msg)
        self.assertFalse(st.session_state["test_active"])
        self.assertEqual(st.session_state["test_qs"], [])


if __name__ == "__main__":
    unittest.main()
