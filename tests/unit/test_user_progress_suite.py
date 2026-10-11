"""
Unit Test Suite for TNPSC Nova AI User Progress, XP, Streak, Weakness, and Revision Engine.
P2 User Data & Persistence Automation.
NO LIVE SUPABASE CONNECTION - USES DETERMINISTIC IN-MEMORY TEST DOUBLES.
"""

import datetime
import unittest
from unittest.mock import patch, MagicMock

from tests.helpers.test_helpers import FakeSupabaseClient, FakeDate

import core.progress_ai as progress_module
import core.xp_ai as xp_module
import core.streak_ai as streak_module
import core.weakness_ai as weakness_module
import core.revision_ai as revision_module
import core.user_identity as user_identity_module
import core.supabase_client as supabase_client_module
import core.mentor_memory as mentor_memory_module
import core.leaderboard_ai as leaderboard_module


class TestUserProgressSuite(unittest.TestCase):
    def setUp(self):
        self.fake_supabase = FakeSupabaseClient()
        self.test_user_id = "00000000-0000-0000-0000-000000000001"
        self.test_username = "test_p2_user"

        # Patch supabase client across all relevant modules
        self.patches = [
            patch.object(supabase_client_module, "supabase", self.fake_supabase),
            patch.object(progress_module, "supabase", self.fake_supabase),
            patch.object(xp_module, "supabase", self.fake_supabase),
            patch.object(streak_module, "supabase", self.fake_supabase),
            patch.object(weakness_module, "supabase", self.fake_supabase),
            patch.object(revision_module, "supabase", self.fake_supabase),
            patch.object(user_identity_module, "supabase", self.fake_supabase),
            patch.object(mentor_memory_module, "supabase", self.fake_supabase),
            patch.object(leaderboard_module, "supabase", self.fake_supabase),
            patch.object(streak_module, "date", FakeDate),
            patch.object(revision_module.datetime, "date", FakeDate),
        ]
        for p in self.patches:
            p.start()


        # Clear st.session_state
        import streamlit as st
        for k in list(st.session_state.keys()):
            del st.session_state[k]

        # Populate fake profiles row so resolve_user_id works for username lookups
        self.fake_supabase.table("profiles").insert({
            "id": self.test_user_id,
            "username": self.test_username,
            "full_name": "Test P2 User",
        })
        self.fake_supabase.stats["writes"] = 0

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.fake_supabase.reset()
        import streamlit as st
        for k in list(st.session_state.keys()):
            del st.session_state[k]

    # =========================================================================
    # 4. USER PROGRESS TESTS
    # =========================================================================

    def test_save_and_get_progress_new_user(self):
        """Test representative flow for saving and retrieving progress for a user."""
        res = progress_module.save_progress(
            user=self.test_user_id,
            subject="polity",
            topic="polity_historical_background",
            accuracy=85.0,
        )
        self.assertTrue(len(res) > 0)
        self.assertEqual(res[0]["subject"], "polity")
        self.assertEqual(res[0]["accuracy"], 85.0)

        # Retrieve progress
        records = progress_module.get_progress(user=self.test_user_id)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["user_id"], self.test_user_id)

    def test_get_progress_with_pre_fetched_context(self):
        """Test that get_progress returns context.progress when context is provided."""
        mock_context = MagicMock()
        mock_context.progress = [{"subject": "history", "accuracy": 100}]
        res = progress_module.get_progress(user=self.test_user_id, context=mock_context)
        self.assertEqual(res, mock_context.progress)

    def test_save_progress_invalid_user_returns_empty(self):
        """Test that save_progress with invalid user returns empty list."""
        with patch.object(progress_module, "_resolve_user_id", return_value=None):
            res = progress_module.save_progress(user=None, subject="polity", topic="test", accuracy=50)
            self.assertEqual(res, [])

    # =========================================================================
    # 5. XP / LEVEL TESTS
    # =========================================================================

    def test_get_level_from_xp_thresholds(self):
        """Test level calculation from XP thresholds."""
        self.assertEqual(xp_module.get_level_from_xp(0), 1)
        self.assertEqual(xp_module.get_level_from_xp(99), 1)
        self.assertEqual(xp_module.get_level_from_xp(100), 2)
        self.assertEqual(xp_module.get_level_from_xp(249), 2)
        self.assertEqual(xp_module.get_level_from_xp(250), 3)
        self.assertEqual(xp_module.get_level_from_xp(500), 4)
        self.assertEqual(xp_module.get_level_from_xp(1000), 5)
        self.assertEqual(xp_module.get_level_from_xp(2000), 6)
        self.assertEqual(xp_module.get_level_from_xp(3500), 7)
        self.assertEqual(xp_module.get_level_from_xp(5000), 8)
        self.assertEqual(xp_module.get_level_from_xp(7500), 9)
        self.assertEqual(xp_module.get_level_from_xp(10000), 10)
        self.assertEqual(xp_module.get_level_from_xp(15000), 10)

    def test_new_user_default_xp_state(self):
        """Test that new user defaults to 0 XP and Level 1."""
        user_xp = xp_module.get_user_xp(user_id=self.test_user_id)
        self.assertEqual(user_xp["xp"], 0)
        self.assertEqual(user_xp["level"], 1)

    def test_add_xp_and_level_up(self):
        """Test adding XP increments total XP and triggers level_up flag on threshold."""
        # Add 50 XP
        result = xp_module.add_xp(user_id=self.test_user_id, amount=50, reward_type="test")
        self.assertEqual(result["new_xp"], 50)
        self.assertEqual(result["new_level"], 1)
        self.assertFalse(result["level_up"])

        # Add another 60 XP -> Total 110 XP (Level 2)
        result2 = xp_module.add_xp(user_id=self.test_user_id, amount=60, reward_type="test")
        self.assertEqual(result2["new_xp"], 110)
        self.assertEqual(result2["new_level"], 2)
        self.assertTrue(result2["level_up"])
        self.assertEqual(result2["old_level"], 1)

    def test_get_level_progress_and_max_level_boundary(self):
        """Test get_level_progress output and max level behavior."""
        xp_module.add_xp(user_id=self.test_user_id, amount=150)
        progress = xp_module.get_level_progress(user_id=self.test_user_id)
        self.assertEqual(progress["current_xp"], 150)
        self.assertEqual(progress["current_level"], 2)
        self.assertEqual(progress["next_level"], 3)
        self.assertEqual(progress["next_level_target"], 250)
        self.assertEqual(progress["xp_for_next"], 100)

        # Max level test
        xp_module.add_xp(user_id=self.test_user_id, amount=10000)
        max_prog = xp_module.get_level_progress(user_id=self.test_user_id)
        self.assertEqual(max_prog["current_level"], 10)
        self.assertEqual(max_prog["progress_percent"], 100.0)

    def test_is_achievement_unlocked(self):
        """Test achievement unlocking based on user level."""
        self.assertFalse(xp_module.is_achievement_unlocked(self.test_user_id, "level_2"))
        xp_module.add_xp(user_id=self.test_user_id, amount=100)
        self.assertTrue(xp_module.is_achievement_unlocked(self.test_user_id, "level_2"))
        self.assertFalse(xp_module.is_achievement_unlocked(self.test_user_id, "level_5"))

    # =========================================================================
    # 6. STREAK TESTS
    # =========================================================================

    def test_streak_lifecycle(self):
        """Test first activity, same-day repeat, next-day activity, and missed-day reset."""
        base_date = datetime.date(2026, 10, 1)

        # 1. First activity -> streak = 1
        FakeDate.set_today(base_date)
        s1 = streak_module.update_streak(user=self.test_user_id)
        self.assertEqual(s1, 1)

        # 2. Same-day repeat -> streak remains 1
        s2 = streak_module.update_streak(user=self.test_user_id)
        self.assertEqual(s2, 1)

        # 3. Next-day activity -> streak = 2
        FakeDate.set_today(base_date + datetime.timedelta(days=1))
        s3 = streak_module.update_streak(user=self.test_user_id)
        self.assertEqual(s3, 2)

        # 4. Missed-day activity (gap of 4 days) -> streak resets to 1
        FakeDate.set_today(base_date + datetime.timedelta(days=5))
        s4 = streak_module.update_streak(user=self.test_user_id)
        self.assertEqual(s4, 1)

    # =========================================================================
    # 7. WEAKNESS ENGINE TESTS
    # =========================================================================

    def test_weakness_lifecycle(self):
        """Test wrong answer increments weakness, correct answer reduces weakness."""
        subj, topic = "polity", "preamble"

        # Initial weakness -> empty
        initial_weak = weakness_module.get_weakness(username=self.test_user_id)
        self.assertEqual(initial_weak, {})

        # Add weakness (wrong answer)
        weakness_module.add_weakness(username=self.test_user_id, subject=subj, topic=topic)
        weak1 = weakness_module.get_weakness(username=self.test_user_id)
        self.assertEqual(weak1.get("polity-preamble"), 1)

        # Add weakness again (second wrong answer)
        weakness_module.add_weakness(username=self.test_user_id, subject=subj, topic=topic)
        weak2 = weakness_module.get_weakness(username=self.test_user_id)
        self.assertEqual(weak2.get("polity-preamble"), 2)

        # Reduce weakness (correct answer)
        weakness_module.reduce_weakness(username=self.test_user_id, subject=subj, topic=topic)
        weak3 = weakness_module.get_weakness(username=self.test_user_id)
        self.assertEqual(weak3.get("polity-preamble"), 1)

        # Reduce weakness below zero -> remains 0
        weakness_module.reduce_weakness(username=self.test_user_id, subject=subj, topic=topic)
        weakness_module.reduce_weakness(username=self.test_user_id, subject=subj, topic=topic)
        weak4 = weakness_module.get_weakness(username=self.test_user_id)
        self.assertEqual(weak4.get("polity-preamble"), 0)

    def test_get_most_weak_topic(self):
        """Test identifying topic with highest weakness count."""
        weakness_module.add_weakness(username=self.test_user_id, subject="polity", topic="preamble")
        weakness_module.add_weakness(username=self.test_user_id, subject="history", topic="indus_valley")
        weakness_module.add_weakness(username=self.test_user_id, subject="history", topic="indus_valley")

        most_weak = weakness_module.get_most_weak_topic(username=self.test_user_id)
        self.assertEqual(most_weak, ("history-indus_valley", 2))

    # =========================================================================
    # 8. REVISION ENGINE TESTS
    # =========================================================================

    def test_revision_progression_and_due_dates(self):
        """Test adding revision topic, updating spacing levels, and querying due revisions."""
        base_date = datetime.date(2026, 10, 1)

        FakeDate.set_today(base_date)

        # Add revision item -> level 1, next_due = 2026-10-02
        revision_module.add_revision(user=self.test_user_id, topic="polity-citizenship")

        # Update revision -> level 2, spacing interval 3 days -> next_due = 2026-10-04
        revision_module.update_revision(user=self.test_user_id, topic_key="polity-citizenship")

        # Query overview as of 2026-10-05 (when next_due of 2026-10-04 is overdue)
        FakeDate.set_today(base_date + datetime.timedelta(days=4))

        overview = revision_module.get_revision_overview(user=self.test_user_id)
        self.assertEqual(overview["total"], 1)
        self.assertEqual(len(overview["overdue"]), 1)
        self.assertEqual(overview["overdue"][0]["topic"], "citizenship")
        self.assertEqual(overview["overdue"][0]["level"], 2)

    # =========================================================================
    # 9. LEADERBOARD RPC TESTS
    # =========================================================================

    def test_leaderboard_uses_get_global_leaderboard_rpc(self):
        """Test get_top_users calls get_global_leaderboard RPC and maps contract."""
        import core.leaderboard_ai as leaderboard_module

        # Populate progress rows for two users in fake store
        self.fake_supabase.store["users_progress"] = [
            {"username": "user_a", "accuracy": 90.0},
            {"username": "user_a", "accuracy": 100.0},
            {"username": "user_b", "accuracy": 70.0},
        ]

        top_users = leaderboard_module.get_top_users()

        # Verify RPC was called
        rpc_calls = self.fake_supabase.stats["rpc_calls"]
        self.assertTrue(any(call[0] == "get_global_leaderboard" for call in rpc_calls))

        # Verify UI contract format: list of tuples (username, avg_accuracy)
        self.assertEqual(top_users, [("user_a", 95.0), ("user_b", 70.0)])

    def test_leaderboard_handles_rpc_failure_safely(self):
        """Test get_top_users returns empty list on RPC exception without crashing."""
        import core.leaderboard_ai as leaderboard_module

        with patch.object(leaderboard_module.supabase, "rpc", side_effect=Exception("RPC Network Failure")):
            top_users = leaderboard_module.get_top_users()
            self.assertEqual(top_users, [])


if __name__ == "__main__":
    unittest.main()

