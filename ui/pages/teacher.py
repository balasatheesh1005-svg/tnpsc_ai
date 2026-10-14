import streamlit as st

from core.ai_teacher import ai_teacher


def render_teacher(section, user=None):
    section("🤖 AI Teacher")

    st.markdown(
        """
        <div style="color: #475569; font-size: 0.92rem; font-weight: 500; margin-top: -6px; margin-bottom: 18px; line-height: 1.5;">
            Ask questions on TNPSC syllabus topics, constitutional articles, historical dates, or economic reforms.
            Verified answers are retrieved directly from authentic Nova AI study notes.
        </div>
        """,
        unsafe_allow_html=True,
    )

    q = st.text_input(
        "Ask doubt",
        placeholder="e.g. When was GST implemented? What is Article 279A? Indus Valley Civilization...",
        label_visibility="collapsed",
    )

    if st.button("Ask AI Teacher", use_container_width=True):
        if q and q.strip():
            with st.spinner("Retrieving verified note evidence..."):
                ans = ai_teacher(q.strip(), user)
                if "Answer கிடைக்கவில்லை" in ans or "INSUFFICIENT EVIDENCE" in ans:
                    st.info(ans)
                else:
                    st.success(ans)
        else:
            st.warning("Please enter a question or topic to search.")
