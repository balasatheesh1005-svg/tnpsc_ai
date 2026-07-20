import streamlit as st


def render_header(metadata):
    """
    Renders Component 1: Hero Header Card
    Displays Subject, Topic, Difficulty Badge, Reading Time, Progress %, Completion Status.
    """
    subject = metadata.get("subject", "General Knowledge").title()
    topic = metadata.get("topic", "TNPSC Topic").title()
    difficulty = metadata.get("difficulty", "Medium").title()
    reading_time = metadata.get("reading_time", "5 mins")
    completion_pct = metadata.get("completion_pct", 85)

    # Color badge mapping
    diff_color = "#22C55E" if difficulty.lower() == "easy" else "#F59E0B" if difficulty.lower() == "medium" else "#EF4444"

    st.markdown(
        f"""
        <div class="nova-card animate-fade-in" style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 60%, #1E40AF 100%); color: white; padding: 2rem; border-radius: 20px; box-shadow: 0 12px 30px rgba(15, 23, 42, 0.3);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                <span class="nova-badge" style="background-color: rgba(59, 130, 246, 0.25); color: #93C5FD; border: 1px solid rgba(147, 197, 253, 0.3);">
                    📘 {subject}
                </span>
                <span class="nova-badge" style="background-color: {diff_color}22; color: {diff_color}; border: 1px solid {diff_color}55;">
                    ⚡ {difficulty}
                </span>
            </div>
            <h1 style="color: #FFFFFF; font-size: 2.1rem; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.2;">
                {topic}
            </h1>
            <div style="display: flex; gap: 1.5rem; align-items: center; font-size: 0.9rem; color: #CBD5E1; margin-top: 1rem;">
                <span>⏱️ Reading Time: <strong>{reading_time}</strong></span>
                <span>📊 Estimated Completion: <strong>{completion_pct}%</strong></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(completion_pct / 100.0)
