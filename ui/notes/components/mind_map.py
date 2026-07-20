import streamlit as st
from ui.notes.layout import section_anchor


def render_mind_map(mind_map_data):
    """
    Renders Component 18: Hierarchical Mind Map Card
    Theme Accent: Teal (#0D9488)
    Expandable, Collapsible, Zoom Ready, Export Action Chips.
    """
    if not mind_map_data:
        return

    section_anchor("sec_mind_map")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #F0FDFA; border-left: 5px solid #0D9488;">', unsafe_allow_html=True)
    st.markdown("### 🗺️ **Visual Concept Mind Map**")

    # Action Toolbar
    col_a, col_b = st.columns([3, 1])
    with col_b:
        st.markdown('<span class="nova-chip" style="background:#CCFBF1; color:#0F766E;">🔍 Zoom Ready</span> <span class="nova-chip" style="background:#CCFBF1; color:#0F766E;">📥 Export PNG</span>', unsafe_allow_html=True)

    if isinstance(mind_map_data, list):
        st.markdown("**Core Branches:**")
        cols = st.columns(min(len(mind_map_data), 3))
        for idx, node in enumerate(mind_map_data):
            col = cols[idx % len(cols)]
            with col:
                node_name = node.get("title", node) if isinstance(node, dict) else str(node)
                st.markdown(
                    f"""
                    <div style="background: white; border: 2px solid #0D9488; border-radius: 12px; padding: 0.85rem; text-align: center; font-weight: 700; color: #0F766E; margin-bottom: 0.5rem; box-shadow: 0 4px 10px rgba(13, 148, 136, 0.15);">
                        🌿 {node_name}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
    elif isinstance(mind_map_data, dict):
        for root, children in mind_map_data.items():
            with st.expander(f"🌳 Branch: {root}", expanded=True):
                if isinstance(children, list):
                    for child in children:
                        st.markdown(f"↳ 🍃 **{child}**")
                else:
                    st.write(children)

    st.markdown("</div>", unsafe_allow_html=True)
