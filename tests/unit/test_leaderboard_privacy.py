import re
import unittest
from unittest.mock import MagicMock, patch

from core.leaderboard_ai import get_top_users
from core.progress_ai import save_progress
from core.session import (
    clear_auth_session,
    current_user_email,
    current_user_id,
    current_username,
    get_session_identity,
    save_auth_session,
)
from core.user_identity import (
    generate_safe_learner_label,
    get_safe_public_identity,
    is_safe_public_username,
    is_valid_uuid,
)
from ui.pages.leaderboard import render_leaderboard


class TestLeaderboardPrivacyAndSafeDisplayIdentity(unittest.TestCase):
    """
    P0 Batch 3: Leaderboard Privacy & Safe Display Identity Test Suite.
    Guarantees raw emails, phone numbers, auth UUIDs, and tokens NEVER leak to the public leaderboard.
    """

    def setUp(self):
        clear_auth_session()
        import streamlit as st
        if hasattr(st, "session_state"):
            st.session_state.pop("leaderboard_top_users_cache", None)

    def tearDown(self):
        clear_auth_session()
        import streamlit as st
        if hasattr(st, "session_state"):
            st.session_state.pop("leaderboard_top_users_cache", None)

    # =========================================================================
    # CORE UNIT TESTS: SAFE IDENTITY RESOLUTION (CASES 1 - 4, 8)
    # =========================================================================

    def test_case_1_safe_username_preserved(self):
        """CASE 1: Safe username (ArunTNPSC) is preserved exactly."""
        public_id = get_safe_public_identity("ArunTNPSC")
        self.assertEqual(public_id, "ArunTNPSC")
        self.assertTrue(is_safe_public_username("ArunTNPSC"))

    def test_case_2_raw_email_never_leaked(self):
        """CASE 2: Raw email (student@example.com) must never appear in public identity."""
        emails = [
            "student@example.com",
            "abc123@yahoo.com",
            "person@outlook.com",
            "satheesh123@gmail.com",
        ]
        for email in emails:
            public_id = get_safe_public_identity(email)
            self.assertNotIn("@", public_id)
            self.assertNotIn("example.com", public_id)
            self.assertNotIn("yahoo.com", public_id)
            self.assertNotIn("outlook.com", public_id)
            self.assertNotIn("gmail.com", public_id)
            # Local part of email must NOT be used directly as fallback
            local_part = email.split("@")[0]
            self.assertNotEqual(public_id, local_part)
            # Must match neutral generated label format
            self.assertTrue(public_id.startswith("Learner "))

    def test_case_3_null_username_fallback(self):
        """CASE 3: Null username produces a safe neutral learner label."""
        public_id = get_safe_public_identity(None)
        self.assertTrue(public_id.startswith("Learner"))
        self.assertNotIn("None", public_id)
        self.assertNotIn("null", public_id)

    def test_case_4_empty_username_fallback(self):
        """CASE 4: Empty/whitespace username produces a safe neutral learner label."""
        for empty_val in ["", "   ", "\t\n"]:
            public_id = get_safe_public_identity(empty_val)
            self.assertTrue(public_id.startswith("Learner"))

    def test_case_8_multiple_fallback_learners_distinct(self):
        """
        CASE 8: Multiple fallback learners do not catastrophically collapse to an identical label
        when distinct seeds/identifiers exist, and do not expose underlying identifiers.
        """
        user_seeds = [
            "alpha@example.com",
            "beta@example.com",
            "gamma@example.com",
            "delta@example.com",
            "epsilon@example.com",
        ]
        labels = [get_safe_public_identity(s) for s in user_seeds]

        # All labels must be valid Learner #### format
        for lbl in labels:
            self.assertTrue(re.match(r"^Learner \d{4}$", lbl), f"Unexpected label format: {lbl}")

        # Unique seeds must yield diverse labels (not all identical)
        unique_labels = set(labels)
        self.assertEqual(len(unique_labels), len(user_seeds))

        # None of the original emails should be contained in the label
        for seed in user_seeds:
            for lbl in labels:
                self.assertNotIn(seed, lbl)

    def test_uuid_never_exposed_as_public_identity(self):
        """UUID user_id must never be rendered as a public username."""
        raw_uuid = "550e8400-e29b-41d4-a716-446655440000"
        public_id = get_safe_public_identity(raw_uuid)
        self.assertNotEqual(public_id, raw_uuid)
        self.assertNotIn("550e8400", public_id)
        self.assertTrue(public_id.startswith("Learner "))

    def test_phone_and_tokens_never_exposed(self):
        """Phone numbers and JWT tokens must never be rendered as public identities."""
        phone = "+919876543210"
        public_id = get_safe_public_identity(phone)
        self.assertNotIn("9876543210", public_id)
        self.assertTrue(public_id.startswith("Learner "))

        jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.xyz"
        public_id_token = get_safe_public_identity(jwt_token)
        self.assertNotIn("eyJ", public_id_token)
        self.assertTrue(public_id_token.startswith("Learner "))

    def test_profile_fullname_fallback_when_safe(self):
        """When username is absent, safe full_name is prioritized before Learner label."""
        public_id = get_safe_public_identity(raw_identifier=None, full_name="Kavitha Raman")
        self.assertEqual(public_id, "Kavitha Raman")

        # But if full_name is an email, it is rejected and safely falls back
        unsafe_fn = get_safe_public_identity(raw_identifier=None, full_name="kavitha@gmail.com")
        self.assertNotIn("@", unsafe_fn)
        self.assertTrue(unsafe_fn.startswith("Learner "))

    # =========================================================================
    # SESSION & PROGRESS INTEGRATION (CASE 6)
    # =========================================================================

    def test_case_6_session_with_missing_username_does_not_set_email(self):
        """
        CASE 6: Session/profile with username missing and email present must NOT
        set public leaderboard identity (st.session_state['username']) to raw email.
        """
        fake_session = {"access_token": "fake-at", "refresh_token": "fake-rt"}
        fake_user = {"id": "00000000-0000-0000-0000-000000000001", "email": "learner@gmail.com"}
        fake_profile = {
            "id": "00000000-0000-0000-0000-000000000001",
            "username": None,
            "full_name": None,
            "email": "learner@gmail.com",
        }

        save_auth_session(fake_session, fake_user, fake_profile)

        # Public username must NOT be the email address
        self.assertNotEqual(current_username(), "learner@gmail.com")
        self.assertNotIn("@", current_username())
        self.assertTrue(current_username().startswith("Learner "))

        # Private email is still securely accessible for authenticated functions
        self.assertEqual(current_user_email(), "learner@gmail.com")

        # Session identity dict reflects sanitized username and private email
        identity = get_session_identity()
        self.assertNotEqual(identity["username"], "learner@gmail.com")
        self.assertEqual(identity["email"], "learner@gmail.com")

    @patch("core.progress_ai.supabase")
    def test_save_progress_sanitizes_email_before_db_insert(self, mock_supabase):
        """Progress insertion must sanitize raw email so users_progress table never stores email."""
        mock_execute = MagicMock()
        mock_execute.execute.return_value = MagicMock(data=[{"id": 1}])
        mock_supabase.table.return_value.insert.return_value = mock_execute

        import streamlit as st
        st.session_state["user_id"] = "00000000-0000-0000-0000-000000000001"

        # User passes raw email as identity
        save_progress(
            user="victim@example.com",
            subject="economy",
            topic="gst",
            accuracy=90,
        )

        # Inspect what was inserted into table
        insert_args = mock_supabase.table.return_value.insert.call_args[0][0]
        self.assertNotEqual(insert_args["username"], "victim@example.com")
        self.assertNotIn("@", insert_args["username"])
        self.assertTrue(insert_args["username"].startswith("Learner "))

    # =========================================================================
    # LEADERBOARD RPC & UI SANITIZATION (CASES 5, 7, PRIVACY SCAN)
    # =========================================================================

    @patch("core.leaderboard_ai.supabase")
    def test_case_5_legacy_leaderboard_rpc_row_sanitized(self, mock_supabase):
        """
        CASE 5: Legacy leaderboard RPC returning raw emails is sanitized by get_top_users
        and UI renderer before display.
        """
        # Simulate legacy database with email in username column
        legacy_rpc_rows = [
            {"username": "ArunTNPSC", "accuracy": 98.0},
            {"username": "legacy_user@example.com", "accuracy": 92.0},
            {"username": None, "accuracy": 85.0},
            {"username": "550e8400-e29b-41d4-a716-446655440000", "accuracy": 80.0},
        ]
        mock_supabase.rpc.return_value.execute.return_value = MagicMock(data=legacy_rpc_rows)

        leaders = get_top_users()

        # Check get_top_users output contract
        usernames = [u for u, s in leaders]
        self.assertIn("ArunTNPSC", usernames)
        self.assertNotIn("legacy_user@example.com", usernames)
        self.assertNotIn("550e8400-e29b-41d4-a716-446655440000", usernames)

        for u in usernames:
            self.assertNotIn("@", u)
            self.assertFalse(is_valid_uuid(u))

    def test_case_7_current_user_highlighting_preserved(self):
        """
        CASE 7: Existing safe current-user username is highlighted as '(You)'
        and ranking is accurately preserved.
        """
        fake_session = {"access_token": "fake-at", "refresh_token": "fake-rt"}
        fake_user = {"id": "00000000-0000-0000-0000-000000000001", "email": "me@tnpsc.org"}
        fake_profile = {
            "id": "00000000-0000-0000-0000-000000000001",
            "username": "ArunTNPSC",
            "full_name": "Arun",
        }
        save_auth_session(fake_session, fake_user, fake_profile)

        captured_writes = []
        captured_markdowns = []

        mock_section = MagicMock()
        with patch("streamlit.write", side_effect=lambda x: captured_writes.append(str(x))), \
             patch("streamlit.markdown", side_effect=lambda x: captured_markdowns.append(str(x))), \
             patch("core.leaderboard_ai.supabase") as mock_sb:

            mock_sb.rpc.return_value.execute.return_value = MagicMock(
                data=[
                    {"username": "TopperOne", "accuracy": 99.0},
                    {"username": "ArunTNPSC", "accuracy": 95.0},
                    {"username": "other@example.com", "accuracy": 88.0},
                ]
            )

            render_leaderboard(mock_section)

        all_rendered = " ".join(captured_writes + captured_markdowns)

        # Current user ArunTNPSC should be highlighted with (You)
        self.assertTrue(any("ArunTNPSC (You)" in m for m in captured_markdowns))
        # Raw email must NOT be anywhere in rendered output
        self.assertNotIn("other@example.com", all_rendered)
        self.assertNotIn("@", all_rendered)
        # Ranks must be preserved
        self.assertIn("1. TopperOne", all_rendered)
        self.assertIn("2. ArunTNPSC", all_rendered)
        self.assertIn("3. Learner", all_rendered)

    def test_phase_7_synthetic_privacy_scan(self):
        """
        PHASE 7: Privacy Scan. Verify simulated leaderboard output with adversarial data
        contains zero instances of email domains, auth UUIDs, tokens, or raw dictionaries.
        """
        adversarial_rows = [
            {"username": "hacker@example.com", "accuracy": 95.0},
            {"username": "victim@gmail.com", "accuracy": 90.0},
            {"username": "user@yahoo.com", "accuracy": 85.0},
            {"username": "admin@outlook.com", "accuracy": 80.0},
            {"username": "b6a83e0c-3f41-4c12-9c98-123456789abc", "accuracy": 75.0},
            {"username": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", "accuracy": 70.0},
            {"username": "+919876543210", "accuracy": 65.0},
            {"username": "SafeLearnerTN", "accuracy": 60.0},
        ]

        captured = []
        with patch("streamlit.write", side_effect=lambda x: captured.append(str(x))), \
             patch("streamlit.markdown", side_effect=lambda x: captured.append(str(x))), \
             patch("core.leaderboard_ai.supabase") as mock_sb:

            mock_sb.rpc.return_value.execute.return_value = MagicMock(data=adversarial_rows)
            render_leaderboard(MagicMock())

        full_output = "\n".join(captured)

        # Zero email domain occurrences
        self.assertNotIn("@example.com", full_output)
        self.assertNotIn("@gmail.com", full_output)
        self.assertNotIn("@yahoo.com", full_output)
        self.assertNotIn("@outlook.com", full_output)
        self.assertNotIn("@", full_output)

        # Zero UUID occurrences
        self.assertNotIn("b6a83e0c-3f41-4c12-9c98-123456789abc", full_output)

        # Zero tokens or phone numbers
        self.assertNotIn("eyJ", full_output)
        self.assertNotIn("9876543210", full_output)

        # Safe username rendered intact
        self.assertIn("SafeLearnerTN", full_output)


if __name__ == "__main__":
    unittest.main()
