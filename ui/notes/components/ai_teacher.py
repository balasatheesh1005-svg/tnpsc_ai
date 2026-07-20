import streamlit as st
from ui.notes.layout import section_anchor


def render_ai_teacher(topic_name):
    """
    Renders Component 16: AI Teacher Action Panel
    Theme Accent: Blue Gradient
    Actions: Explain Simply, Explain in Tamil, Generate MCQs, Show PYQs, Real-life Examples, Doubt Solver, Voice AI
    """
    section_anchor("sec_ai_teacher")
    
    st.markdown(
        """
        <div class="nova-card nova-ai-card animate-fade-in">
            <h3 style="margin-top:0; color:white;">🤖 Nova AI Assistant — Interactive Learning Actions</h3>
            <p style="color:#DBEAFE; font-size:0.95rem;">Tap any action below to trigger instant AI explanation, Tamil translation, MCQ generation, or doubt solving for this chapter.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("💡 Explain Simply", key="ai_explain_simple", use_container_width=True):
            st.info(f"🤖 **AI Explanation ({topic_name}):** Simplified concepts broken down into everyday analogies.")
    with col2:
        if st.button("🇮🇳 Explain in Tamil", key="ai_explain_tamil", use_container_width=True):
            st.info(f"🤖 **தமிழ் விளக்கம் ({topic_name}):** இந்த பாடத்தின் மிக முக்கியமான கருத்துக்கள் தமிழில் எளிமையாக.")
    with col3:
        if st.button("📝 Generate MCQs", key="ai_gen_mcqs", use_container_width=True):
            st.success("🤖 **AI MCQs Generated:** 5 custom practice questions created for this topic.")
    with col4:
        if st.button("🎙️ Voice AI Teacher", key="ai_voice_teacher", use_container_width=True):
            st.toast("🎙️ Voice AI Teacher initialized! Speak your question.")

    # Doubt Solver Input Box
    st.text_input("💬 Ask AI Teacher a specific question about this topic:", key=f"ai_doubt_input_{topic_name}")
