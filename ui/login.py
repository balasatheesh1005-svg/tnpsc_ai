import streamlit as st

from core.auth import login, send_password_reset


def render_login_page():
    st.markdown("### Login")
    with st.form("login_form", clear_on_submit=False):
        identifier = st.text_input(
            "Email or Username",
            placeholder="you@example.com or username",
        )
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button(
            "Login",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        with st.spinner("Signing in..."):
            success, message = login(identifier, password)
        if success:
            st.success(message)
            st.session_state["auth_page"] = "login"
            st.rerun()
        else:
            st.error(message)

    if st.button("Forgot Password?", type="tertiary", use_container_width=True):
        st.session_state["show_password_reset"] = not st.session_state.get(
            "show_password_reset",
            False,
        )

    if st.session_state.get("show_password_reset", False):
        with st.form("password_reset_form", clear_on_submit=False):
            reset_email = st.text_input("Email", placeholder="you@example.com")
            reset_submitted = st.form_submit_button(
                "Send Reset Link",
                type="primary",
                use_container_width=True,
            )

        if reset_submitted:
            with st.spinner("Sending reset email..."):
                success, message = send_password_reset(reset_email)
            if success:
                st.success(message)
                st.session_state["show_password_reset"] = False
            else:
                st.error(message)

    st.caption("New to TNPSC Nova AI?")
    if st.button("Create an account", type="tertiary", use_container_width=True):
        st.session_state["auth_page"] = "signup"
        st.rerun()
