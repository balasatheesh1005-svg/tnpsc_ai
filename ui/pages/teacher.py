import streamlit as st

from core.ai_teacher import ai_teacher


def render_teacher(section, user):
    section("🤖 AI Teacher")

    q = st.text_input("Ask doubt")

    if st.button("Ask"):
        if q:
            with st.spinner("Thinking..."):
                ans = ai_teacher(q, user)
                st.success(ans)
