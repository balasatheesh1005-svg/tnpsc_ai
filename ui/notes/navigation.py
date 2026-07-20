import streamlit as st


def render_sticky_toc(available_sections):
    """
    Renders an automated, clickable Sticky Table of Contents based on available JSON sections.
    """
    if not available_sections:
        return

    st.markdown('<div class="nova-toc-sticky animate-fade-in">', unsafe_allow_html=True)
    st.markdown("##### 📍 **Table of Contents**")

    # Render section jump pills in horizontal columns/scroll bar
    cols = st.columns(min(len(available_sections), 6))
    
    for idx, (sec_id, sec_title, icon) in enumerate(available_sections):
        col = cols[idx % len(cols)]
        with col:
            # Anchor jump link using Markdown HTML anchor
            st.markdown(
                f'<a href="#{sec_id}" style="text-decoration:none;">'
                f'<span class="nova-chip" style="cursor:pointer; display:block; text-align:center;">'
                f'{icon} {sec_title}</span></a>',
                unsafe_allow_html=True,
            )

    st.markdown('</div>', unsafe_allow_html=True)
