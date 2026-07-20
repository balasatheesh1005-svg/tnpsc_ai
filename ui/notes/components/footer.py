import streamlit as st


def render_footer(metadata):
    """
    Renders Component 22: Analytics Footer Card
    Displays Time Spent, Revision Due Status, Weakness Recommendation Card, Platform Credits.
    """
    subject = metadata.get("subject", "General").title()
    topic = metadata.get("topic", "Topic").title()
    reading_time = metadata.get("reading_time", "5 mins")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="nova-card animate-fade-in" style="background-color: #0F172A; color: #94A3B8; border-left: 5px solid #38BDF8; border-radius: 18px; padding: 1.75rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
                <div>
                    <h4 style="color:#F8FAFC; margin:0 0 0.4rem 0;">📊 Reading Analytics & Performance Status</h4>
                    <p style="margin:0; font-size:0.88rem;">Subject: <strong style="color:#38BDF8;">{subject}</strong> | Topic: <strong style="color:#38BDF8;">{topic}</strong></p>
                </div>
                <div style="display:flex; gap:0.75rem;">
                    <span class="nova-badge" style="background:rgba(56, 189, 248, 0.15); color:#38BDF8; border:1px solid rgba(56, 189, 248, 0.3);">
                        ⏱️ Time: {reading_time}
                    </span>
                    <span class="nova-badge" style="background:rgba(34, 197, 94, 0.15); color:#4ADE80; border:1px solid rgba(34, 197, 94, 0.3);">
                        📅 Revision Due: 3 Days
                    </span>
                </div>
            </div>
            <hr style="border-color:#334155; margin:1rem 0;">
            <div style="display:flex; justify-content:space-between; font-size:0.8rem; color:#64748B;">
                <span>TNPSC Nova AI Generic Notes Rendering Engine v2.0</span>
                <span>Powered by Nova AI Modular Component Architecture</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
