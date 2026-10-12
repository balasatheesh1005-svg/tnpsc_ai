import streamlit as st

from core.auth import logout, update_password, validate_password_reset


def render_reset_password_page():
    st.markdown("### Reset Password")

    # Handle link errors (invalid / expired token)
    recovery_error = st.session_state.get("recovery_error")
    if recovery_error:
        st.error(recovery_error)
        st.caption("Please request a new password reset link from the login page.")
        if st.button("Back to Login", type="primary", use_container_width=True):
            logout()
            st.session_state.pop("recovery_error", None)
            st.session_state.pop("recovery_tokens", None)
            st.session_state.pop("recovery_session_active", None)
            st.session_state["auth_page"] = "login"
            st.rerun()
        return

    # Handle success state after updating password
    reset_success = st.session_state.get("password_reset_success")
    if reset_success:
        st.success(reset_success)
        if st.button("Proceed to Login", type="primary", use_container_width=True):
            logout()
            st.session_state.pop("password_reset_success", None)
            st.session_state.pop("recovery_tokens", None)
            st.session_state.pop("recovery_session_active", None)
            st.session_state.pop("recovery_error", None)
            st.session_state["auth_page"] = "login"
            st.rerun()
        return

    # Guard against direct navigation or stale state without an active recovery session
    if not st.session_state.get("recovery_session_active"):
        st.error("This password reset link is invalid or has expired. Please request a new reset link.")
        if st.button("Back to Login", type="primary", use_container_width=True):
            logout()
            st.session_state.pop("recovery_error", None)
            st.session_state.pop("password_reset_success", None)
            st.session_state.pop("recovery_tokens", None)
            st.session_state.pop("recovery_session_active", None)
            st.session_state["auth_page"] = "login"
            st.rerun()
        return

    # Dedicated New Password + Confirm New Password form
    with st.form("reset_password_form", clear_on_submit=False):
        new_password = st.text_input(
            "New Password",
            type="password",
            placeholder="At least 8 characters",
        )
        confirm_password = st.text_input(
            "Confirm New Password",
            type="password",
            placeholder="Re-enter new password",
        )
        submitted = st.form_submit_button(
            "Update Password",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        valid, msg = validate_password_reset(new_password, confirm_password)
        if not valid:
            st.error(msg)
        else:
            with st.spinner("Updating password..."):
                success, message = update_password(new_password, confirm_password)
            if success:
                st.session_state["password_reset_success"] = message
                st.session_state.pop("recovery_session_active", None)
                st.rerun()
            else:
                st.error(message)

    if st.button("Back to Login", type="tertiary", use_container_width=True):
        logout()
        st.session_state.pop("recovery_tokens", None)
        st.session_state.pop("recovery_session_active", None)
        st.session_state.pop("recovery_error", None)
        st.session_state["auth_page"] = "login"
        st.rerun()
