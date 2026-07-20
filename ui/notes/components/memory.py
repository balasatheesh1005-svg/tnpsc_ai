import streamlit as st
from ui.notes.layout import section_anchor


def render_memory_tricks(memory_data):
    """
    Renders Component 10: Memory Tricks / Mnemonics Card
    Theme Accent: Purple (#9333EA), Large Typography, Memorable Design
    """
    if not memory_data:
        return

    section_anchor("sec_memory")
    st.markdown('<div class="nova-card nova-memory-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown("### 🧠 **Memory Tricks & Mnemonics**")

    if isinstance(memory_data, list):
        for item in memory_data:
            if isinstance(item, dict):
                en = item.get("en", item.get("mnemonic", ""))
                ta = item.get("ta", "")
                if en or ta:
                    tab1, tab2 = st.tabs(["🇬🇧 English Trick", "🇮🇳 தமிழ் Trick"])
                    with tab1:
                        st.markdown(f'<div style="font-size: 1.15rem; font-weight: 700; color: #7E22CE; background: #FAF5FF; padding: 1rem; border-radius: 12px;">🔑 {en}</div>', unsafe_allow_html=True)
                    with tab2:
                        st.markdown(f'<div style="font-size: 1.15rem; font-weight: 700; color: #7E22CE; background: #FAF5FF; padding: 1rem; border-radius: 12px;">🔑 {ta}</div>', unsafe_allow_html=True)
            elif isinstance(item, str):
                st.markdown(f'<div style="font-size: 1.1rem; font-weight: 700; color: #7E22CE; margin-bottom: 0.5rem;">🔑 {item}</div>', unsafe_allow_html=True)
    elif isinstance(memory_data, str):
        st.markdown(f'<div style="font-size: 1.15rem; font-weight: 700; color: #7E22CE;">🔑 {memory_data}</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
