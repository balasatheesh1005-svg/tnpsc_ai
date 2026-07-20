import streamlit as st
from ui.notes.layout import section_anchor


def render_pyq_reference(pyq_data):
    """
    Renders Component 14: PYQ References Card
    Displays Year, Exam, Question Number, Difficulty, Expected Similar Questions.
    """
    if not pyq_data:
        return

    section_anchor("sec_pyq_reference")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #ECFDF5; border-left: 5px solid #059669;">', unsafe_allow_html=True)
    st.markdown("### 📜 **Previous Year Question (PYQ) References**")

    if isinstance(pyq_data, list):
        for idx, pyq in enumerate(pyq_data):
            if isinstance(pyq, dict):
                year = pyq.get("year", "2021-2024")
                exam = pyq.get("exam", "TNPSC Group 1/2")
                q_no = pyq.get("q_no", pyq.get("question_no", f"Q{idx+1}"))
                diff = pyq.get("difficulty", "Medium")
                question = pyq.get("question", "")

                st.markdown(
                    f"""
                    <div style="background: white; border-radius: 12px; padding: 1rem; margin-bottom: 0.75rem; border: 1px solid #A7F3D0;">
                        <div style="display: flex; gap: 0.5rem; margin-bottom: 0.5rem;">
                            <span class="nova-badge" style="background:#D1FAE5; color:#047857;">📅 {year}</span>
                            <span class="nova-badge" style="background:#D1FAE5; color:#047857;">🏛️ {exam}</span>
                            <span class="nova-badge" style="background:#D1FAE5; color:#047857;">🔢 {q_no}</span>
                            <span class="nova-badge" style="background:#FEF3C7; color:#B45309;">⚡ {diff}</span>
                        </div>
                        {f'<p style="color:#064E3B; font-weight:600;">{question}</p>' if question else ''}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            elif isinstance(pyq, str):
                st.markdown(f"📜 **{pyq}**")

    st.markdown("</div>", unsafe_allow_html=True)
