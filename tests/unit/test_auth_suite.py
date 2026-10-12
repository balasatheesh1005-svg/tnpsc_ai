import inspect
import sys
import unittest
from unittest.mock import MagicMock, patch

from core.auth import (
    _friendly_auth_error,
    _sanitize_log_message,
    handle_recovery_callback,
    login,
    normalize_mobile,
    send_password_reset,
    sign_up,
    update_password,
    validate_password_reset,
    validate_signup,
)


class TestAuthSuite(unittest.TestCase):
    """P0 Unit Test Suite for Auth, Validation, Privacy Sanitization, and Session Flows."""

    # 1. normalize_mobile()
    def test_normalize_mobile_basic(self):
        self.assertEqual(normalize_mobile("9876543210"), "9876543210")
        self.assertEqual(normalize_mobile(""), "")
        self.assertEqual(normalize_mobile(None), "")

    # 2. valid Indian mobile numbers
    def test_valid_indian_mobile_numbers(self):
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "9876543210", "Password123", "Password123")
        self.assertTrue(valid, f"Expected valid signup, got: {msg}")
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "8765432109", "Password123", "Password123")
        self.assertTrue(valid, f"Expected valid signup, got: {msg}")

    # 3. spaces/hyphens normalization
    def test_mobile_normalization_spaces_hyphens(self):
        self.assertEqual(normalize_mobile("98765 43210"), "9876543210")
        self.assertEqual(normalize_mobile("98765-43210"), "9876543210")
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "98765 43210", "Password123", "Password123")
        self.assertTrue(valid, f"Expected valid normalization for spaces, got: {msg}")
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "98765-43210", "Password123", "Password123")
        self.assertTrue(valid, f"Expected valid normalization for hyphens, got: {msg}")

    # 4. invalid starting digit
    def test_invalid_starting_digit(self):
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "1234567890", "Password123", "Password123")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter a valid 10-digit mobile number.")

    # 5. too short
    def test_mobile_too_short(self):
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "987654321", "Password123", "Password123")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter a valid 10-digit mobile number.")

    # 6. too long
    def test_mobile_too_long(self):
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "98765432100", "Password123", "Password123")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter a valid 10-digit mobile number.")

    # 7. alphabetic input
    def test_mobile_alphabetic(self):
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "abcdefghij", "Password123", "Password123")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter a valid 10-digit mobile number.")

    # 8. +91 behavior according to current production contract
    def test_mobile_country_code_plus91(self):
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "+919876543210", "Password123", "Password123")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter a valid 10-digit mobile number.")

    # 9. valid email
    def test_valid_email(self):
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "9876543210", "Password123", "Password123")
        self.assertTrue(valid)

    # 10. invalid email
    def test_invalid_email(self):
        valid, msg = validate_signup("Full Name", "valid_user", "invalidemail", "9876543210", "Password123", "Password123")
        self.assertFalse(valid)
        self.assertEqual(msg, "Enter a valid email address.")

    # 11. password rules
    def test_password_length_rule(self):
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "9876543210", "pass", "pass")
        self.assertFalse(valid)
        self.assertEqual(msg, "Password must contain at least 8 characters.")

    # 12. password mismatch
    def test_password_mismatch(self):
        valid, msg = validate_signup("Full Name", "valid_user", "user@example.com", "9876543210", "Password123", "Different123")
        self.assertFalse(valid)
        self.assertEqual(msg, "Passwords do not match.")

    # 13. friendly duplicate-user error
    def test_friendly_duplicate_error(self):
        msg = _friendly_auth_error("User already registered", context="signup")
        self.assertEqual(msg, "This email is already registered.")

    # 14. rate-limit error mapping
    def test_friendly_rate_limit_error(self):
        msg = _friendly_auth_error("429 Too Many Requests rate limit reached", context="signup")
        self.assertEqual(msg, "Too many attempts. Please try again later.")

    # 15. unknown error sanitization
    def test_friendly_unknown_error(self):
        msg = _friendly_auth_error("Unexpected internal exception xyz", context="signup")
        self.assertEqual(msg, "Something went wrong. Please try again.")

    # 16. PII log sanitization (email, mobile, JWT/bearer token)
    def test_pii_log_sanitization(self):
        raw_msg = "Error for user john@example.com with phone 9876543210 and token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
        sanitized = _sanitize_log_message(raw_msg)
        self.assertNotIn("john@example.com", sanitized)
        self.assertIn("[REDACTED_EMAIL]", sanitized)
        self.assertNotIn("9876543210", sanitized)
        self.assertIn("[REDACTED_MOBILE]", sanitized)
        self.assertNotIn("eyJhbGci", sanitized)
        self.assertIn("[REDACTED_TOKEN]", sanitized)

    # 17. signup metadata contains (username, full_name, mobile_number)
    @patch("core.auth.email_exists", return_value=False)
    @patch("core.auth.username_exists", return_value=False)
    @patch("core.auth.supabase")
    def test_signup_metadata_structure(self, mock_supabase, mock_user_exists, mock_email_exists):
        mock_response = MagicMock()
        mock_response.user = MagicMock(id="test-uuid")
        mock_response.session = None
        mock_supabase.auth.sign_up.return_value = mock_response

        success, msg = sign_up("Test User", "test_user_p0", "test_p0@example.com", "98765 43210", "Password123", "Password123")
        self.assertTrue(success)
        mock_supabase.auth.sign_up.assert_called_once()
        call_args = mock_supabase.auth.sign_up.call_args[0][0]
        self.assertEqual(call_args["email"], "test_p0@example.com")
        metadata = call_args["options"]["data"]
        self.assertEqual(metadata["full_name"], "Test User")
        self.assertEqual(metadata["username"], "test_user_p0")
        self.assertEqual(metadata["mobile_number"], "9876543210")

    # 18. email-confirmation session=None flow
    @patch("core.auth.email_exists", return_value=False)
    @patch("core.auth.username_exists", return_value=False)
    @patch("core.auth.supabase")
    def test_email_confirmation_session_none(self, mock_supabase, mock_user_exists, mock_email_exists):
        mock_response = MagicMock()
        mock_response.user = MagicMock(id="test-uuid")
        mock_response.session = None
        mock_supabase.auth.sign_up.return_value = mock_response

        success, msg = sign_up("Test User", "test_user_p0", "test_p0@example.com", "9876543210", "Password123", "Password123")
        self.assertTrue(success)
        self.assertIn("Account created. Please check your email", msg)

    # 19. verify signup does NOT perform client-side profile insert/upsert
    def test_signup_no_client_side_upsert(self):
        source = inspect.getsource(sign_up)
        self.assertNotIn('supabase.table("profiles").upsert', source)
        self.assertNotIn('supabase.table("profiles").insert', source)

    # 20. login self-healing path remains available
    def test_login_self_healing_available(self):
        source = inspect.getsource(login)
        self.assertIn('supabase.table("profiles").upsert', source)

    # 21. send_password_reset validation
    def test_send_password_reset_invalid_email(self):
        success, msg = send_password_reset("invalid_email")
        self.assertFalse(success)
        self.assertEqual(msg, "Enter a valid email address.")

    @patch("core.auth.supabase")
    def test_send_password_reset_success(self, mock_supabase):
        success, msg = send_password_reset("user@example.com")
        self.assertTrue(success)
        self.assertIn("Password reset link has been sent", msg)
        mock_supabase.auth.reset_password_for_email.assert_called_once_with("user@example.com")

    # 22. validate_password_reset
    def test_validate_password_reset_rules(self):
        # Mismatch
        valid, msg = validate_password_reset("Password123", "Mismatch456")
        self.assertFalse(valid)
        self.assertEqual(msg, "Passwords do not match.")

        # Too short
        valid, msg = validate_password_reset("short", "short")
        self.assertFalse(valid)
        self.assertEqual(msg, "Password must contain at least 8 characters.")

        # Valid
        valid, msg = validate_password_reset("SecurePass123", "SecurePass123")
        self.assertTrue(valid)
        self.assertIsNone(msg)

    # 23. update_password success
    @patch("core.auth.supabase")
    def test_update_password_success(self, mock_supabase):
        mock_supabase.auth.update_user.return_value = MagicMock()
        success, msg = update_password("NewSecurePass123", "NewSecurePass123")
        self.assertTrue(success)
        self.assertIn("Password has been updated successfully", msg)
        mock_supabase.auth.update_user.assert_called_once_with({"password": "NewSecurePass123"})
        mock_supabase.auth.sign_out.assert_called_once()

    # 24. update_password failure
    @patch("core.auth.supabase")
    def test_update_password_failure(self, mock_supabase):
        mock_supabase.auth.update_user.side_effect = Exception("Auth session missing")
        success, msg = update_password("NewSecurePass123", "NewSecurePass123")
        self.assertFalse(success)

    # 25. handle_recovery_callback with error in query params
    @patch("streamlit.query_params", {"error": "access_denied", "error_description": "Email link is invalid or has expired"})
    @patch("streamlit.session_state", {})
    def test_recovery_callback_error_params(self):
        import streamlit as st
        handled = handle_recovery_callback()
        self.assertTrue(handled)
        self.assertEqual(st.session_state.get("auth_page"), "reset_password")
        self.assertIn("invalid or has expired", st.session_state.get("recovery_error", ""))

    # 26. handle_recovery_callback with token_hash
    @patch("core.auth.supabase")
    def test_recovery_callback_token_hash_success(self, mock_supabase):
        import streamlit as st
        mock_response = MagicMock()
        mock_response.session = MagicMock()
        mock_supabase.auth.verify_otp.return_value = mock_response

        with patch("streamlit.query_params", {"token_hash": "test_hash", "type": "recovery"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertTrue(handled)
            self.assertTrue(st.session_state.get("recovery_session_active"))
            self.assertEqual(st.session_state.get("auth_page"), "reset_password")
            mock_supabase.auth.verify_otp.assert_called_once_with({"token_hash": "test_hash", "type": "recovery"})

    # 27. handle_recovery_callback with PKCE code
    @patch("core.auth.supabase")
    def test_recovery_callback_code_success(self, mock_supabase):
        import streamlit as st
        mock_response = MagicMock()
        mock_response.session = MagicMock()
        mock_supabase.auth.exchange_code_for_session.return_value = mock_response

        with patch("streamlit.query_params", {"code": "auth_code_pkce"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertTrue(handled)
            self.assertTrue(st.session_state.get("recovery_session_active"))
            self.assertEqual(st.session_state.get("auth_page"), "reset_password")

    # 28. handle_recovery_callback with access_token
    @patch("core.auth.supabase")
    def test_recovery_callback_access_token_success(self, mock_supabase):
        import streamlit as st
        mock_response = MagicMock()
        mock_response.session = MagicMock()
        mock_supabase.auth.set_session.return_value = mock_response

        with patch("streamlit.query_params", {"access_token": "at_123", "refresh_token": "rt_123", "type": "recovery"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertTrue(handled)
            self.assertTrue(st.session_state.get("recovery_session_active"))
            self.assertEqual(st.session_state.get("auth_page"), "reset_password")

    # 29. handle_recovery_callback with invalid/expired token_hash
    @patch("core.auth.supabase")
    def test_recovery_callback_token_hash_expired(self, mock_supabase):
        import streamlit as st
        mock_supabase.auth.verify_otp.side_effect = Exception("Token expired or invalid")

        with patch("streamlit.query_params", {"token_hash": "expired_hash", "type": "recovery"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertFalse(handled)
            self.assertIn("invalid or has expired", st.session_state.get("recovery_error", ""))
            self.assertEqual(st.session_state.get("auth_page"), "reset_password")

    # 30. handle_recovery_callback with no params
    def test_recovery_callback_no_params(self):
        import streamlit as st
        with patch("streamlit.query_params", {}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertFalse(handled)
            self.assertNotIn("auth_page", st.session_state)

    # 31. handle_recovery_callback with invalid/expired PKCE code
    @patch("core.auth.supabase")
    def test_recovery_callback_code_expired(self, mock_supabase):
        import streamlit as st
        mock_supabase.auth.exchange_code_for_session.side_effect = Exception("Code expired or invalid")

        with patch("streamlit.query_params", {"code": "invalid_code", "type": "recovery"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertFalse(handled)
            self.assertIn("invalid or has expired", st.session_state.get("recovery_error", ""))
            self.assertEqual(st.session_state.get("auth_page"), "reset_password")
            self.assertFalse(st.session_state.get("recovery_session_active", False))

    # 32. handle_recovery_callback with malformed callback (type=recovery but missing tokens)
    def test_recovery_callback_malformed_missing_token(self):
        import streamlit as st
        with patch("streamlit.query_params", {"type": "recovery"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertFalse(handled)
            self.assertIn("invalid or has expired", st.session_state.get("recovery_error", ""))
            self.assertEqual(st.session_state.get("auth_page"), "reset_password")
            self.assertFalse(st.session_state.get("recovery_session_active", False))

    # 33. handle_recovery_callback with malformed access_token (missing refresh_token)
    @patch("core.auth.supabase")
    def test_recovery_callback_malformed_access_token_missing_refresh(self, mock_supabase):
        import streamlit as st
        with patch("streamlit.query_params", {"access_token": "at_123", "type": "recovery"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertFalse(handled)
            mock_supabase.auth.set_session.assert_not_called()
            self.assertIn("invalid or has expired", st.session_state.get("recovery_error", ""))
            self.assertEqual(st.session_state.get("auth_page"), "reset_password")

    # 34. handle_recovery_callback ignores non-recovery callbacks (e.g. signup confirmation)
    @patch("core.auth.supabase")
    def test_recovery_callback_non_recovery_type_ignored(self, mock_supabase):
        import streamlit as st
        # token_hash with type=signup
        with patch("streamlit.query_params", {"token_hash": "signup_hash", "type": "signup"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertFalse(handled)
            mock_supabase.auth.verify_otp.assert_not_called()
            self.assertNotIn("auth_page", st.session_state)
            self.assertNotIn("recovery_session_active", st.session_state)

        # code with type=signup
        with patch("streamlit.query_params", {"code": "signup_code", "type": "signup"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertFalse(handled)
            mock_supabase.auth.exchange_code_for_session.assert_not_called()
            self.assertNotIn("auth_page", st.session_state)

        # access_token with type=signup
        with patch("streamlit.query_params", {"access_token": "at_123", "refresh_token": "rt_123", "type": "signup"}), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertFalse(handled)
            mock_supabase.auth.set_session.assert_not_called()
            self.assertNotIn("auth_page", st.session_state)

    # 35. update_password fails safely when no authenticated recovery session exists
    @patch("core.auth.supabase")
    def test_update_password_no_active_session(self, mock_supabase):
        mock_supabase.auth.get_session.return_value = None
        success, msg = update_password("NewSecurePass123", "NewSecurePass123")
        self.assertFalse(success)
        self.assertIn("invalid or has expired", msg)
        mock_supabase.auth.update_user.assert_not_called()

    # 36. update_password validation guards (short password and mismatch)
    @patch("core.auth.supabase")
    def test_update_password_validation_short_and_mismatch(self, mock_supabase):
        # Mismatch
        success, msg = update_password("Password123", "Mismatch456")
        self.assertFalse(success)
        self.assertEqual(msg, "Passwords do not match.")
        mock_supabase.auth.update_user.assert_not_called()

        # Short password with confirm
        success, msg = update_password("short", "short")
        self.assertFalse(success)
        self.assertEqual(msg, "Password must contain at least 8 characters.")
        mock_supabase.auth.update_user.assert_not_called()

        # Short password without confirm
        success, msg = update_password("short")
        self.assertFalse(success)
        self.assertEqual(msg, "Password must contain at least 8 characters.")
        mock_supabase.auth.update_user.assert_not_called()

    # 37. successful recovery state cleanup and query parameter clearing
    @patch("core.auth.clear_auth_session")
    @patch("core.auth.supabase")
    def test_recovery_state_cleanup_and_query_clearing(self, mock_supabase, mock_clear_session):
        import streamlit as st
        mock_response = MagicMock()
        mock_response.session = MagicMock()
        mock_supabase.auth.verify_otp.return_value = mock_response

        # Step 1: verify OTP clears query params and previous session
        class TrackedQueryParams(dict):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.cleared = False

            def clear(self):
                self.cleared = True
                super().clear()

        params = TrackedQueryParams({"token_hash": "hash_123", "type": "recovery"})
        with patch("streamlit.query_params", params), \
             patch("streamlit.session_state", {}):
            handled = handle_recovery_callback()
            self.assertTrue(handled)
            self.assertTrue(params.cleared)
            mock_clear_session.assert_called()

        # Step 2: update_password invokes sign_out and clear_auth_session
        mock_supabase.auth.get_session.return_value = MagicMock()
        mock_supabase.auth.update_user.return_value = MagicMock()
        mock_clear_session.reset_mock()
        mock_supabase.auth.sign_out.reset_mock()

        success, msg = update_password("NewSecurePass123", "NewSecurePass123")
        self.assertTrue(success)
        mock_supabase.auth.sign_out.assert_called_once()
        mock_clear_session.assert_called_once()


if __name__ == "__main__":
    unittest.main()

