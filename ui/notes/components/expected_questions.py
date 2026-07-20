import streamlit as st
from ui.notes.layout import section_anchor


def render_expected_questions(eq_data):
    """
    Renders Component 13: Expected Question Areas Card
    Theme Accent: Orange (#EA580C) with Question Type Chips.
    """
    if not eq_data:
        return

    section_anchor("sec_expected_questions")
    st.markdown('<div class="nova-card nova-expected-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown("### 🎯 **Expected Question Areas & Types**")

    # Render Question Type Chips
    st.markdown(
        """
        <div style="margin-bottom: 1rem;">
            <span class="nova-chip" style="background:#FFEDD5; color:#C2410C;">📝 Statement Type</span>
            <span class="nova-chip" style="background:#FFEDD5; color:#C2410C;">⚡ Assertion-Reason</span>
            <span class="nova-chip" style="background:#FFEDD5; color:#C2410C;">🔄 Match the Following</span>
            <span class="nova-chip" style="background:#FFEDD5; color:#C2410C;">⏳ Chronology Order</span>
            <span class="nova-chip" style="background:#FFEDD5; color:#C2410C;">💼 Case Study / Scenario</span>
            <span class="nova-chip" style="background:#FFEDD5; color:#C2410C;">📜 PYQ Trend</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if isinstance(eq_data, list):
        for idx, q in enumerate(eq_data):
            if isinstance(q, dict):
                q_text = q.get("question", q.get("area", f"Expected Question {idx+1}"))
                q_type = q.get("type", "Standard MCQ")
                st.markdown(f"🔸 **[{q_type}]** {q_text}")
            elif isinstance(q, str):
                st.markdown(f"🔸 {q}")
    elif isinstance(eq_data, dict):
        en = eq_data.get("en", [])
        ta = eq_data.get("ta", [])
        tab1, tab2 = st.tabs(["🇬🇧 English", "🇮🇳 தமிழ்"])
        with tab1:
            for item in en if isinstance(en, list) else [en]:
                st.markdown(f"🔸 {item}")
        with tab2:
            for item in ta if isinstance(ta, list) else [ta]:
                st.markdown(f"🔸 {item}")

    st.markdown("</div>", unsafe_allow_html=True)
