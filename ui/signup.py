import streamlit as st

from core.auth import sign_up


def render_signup_page():
    st.markdown("### Sign Up")
    with st.form("signup_form", clear_on_submit=False):
        full_name = st.text_input("Full Name", placeholder="Your full name")
        username = st.text_input("Username", placeholder="unique_username")
        email = st.text_input("Email", placeholder="you@example.com")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button(
            "Create Account",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        with st.spinner("Creating your account..."):
            success, message = sign_up(
                full_name,
                username,
                email,
                password,
                confirm_password,
            )
        if success:
            st.success(message)
            if "user_id" in st.session_state:
                st.rerun()
            st.session_state["auth_page"] = "login"
        else:
            st.error(message)

    st.caption("Already have an account?")
    if st.button("Back to login", type="tertiary", use_container_width=True):
        st.session_state["auth_page"] = "login"
        st.rerun()
