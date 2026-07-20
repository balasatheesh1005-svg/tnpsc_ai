import streamlit as st
from ui.notes.layout import section_anchor


def render_timeline(timeline_data):
    """
    Renders Component 6: Vertical Timeline Card
    Theme Accent: Indigo (#4F46E5)
    Renders timeline as a clean vertical timeline UI (never plain bullet points).
    """
    if not timeline_data:
        return

    section_anchor("sec_timeline")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #EEF2FF; border-left: 5px solid #4F46E5;">', unsafe_allow_html=True)
    st.markdown("### ⏳ **Chronological Timeline**")

    if isinstance(timeline_data, list):
        st.markdown('<div class="nova-timeline-container">', unsafe_allow_html=True)
        for idx, item in enumerate(timeline_data):
            if isinstance(item, dict):
                year = item.get("year", item.get("date", f"Phase {idx+1}"))
                event = item.get("event", item.get("title", ""))
                desc = item.get("desc", item.get("description", ""))
                
                st.markdown(
                    f"""
                    <div class="nova-timeline-item">
                        <span style="font-weight: 800; color: #4F46E5; font-size: 1.05rem;">{year}</span> — 
                        <strong style="color: #1E293B;">{event}</strong>
                        {f'<p style="color: #475569; font-size: 0.9rem; margin-top: 0.25rem;">{desc}</p>' if desc else ''}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            elif isinstance(item, str):
                st.markdown(
                    f"""
                    <div class="nova-timeline-item">
                        <strong style="color: #1E293B;">{item}</strong>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
