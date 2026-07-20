import streamlit as st
from ui.notes.layout import section_anchor


def render_knowledge_graph(graph_data, default_topic="Topic Nodes"):
    """
    Renders Component 19: Interactive Knowledge Graph Card
    Theme Accent: Violet (#7C3AED)
    Shows concept linkage and relationship node chains.
    """
    section_anchor("sec_knowledge_graph")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #F5F3FF; border-left: 5px solid #7C3AED;">', unsafe_allow_html=True)
    st.markdown("### 🕸️ **Interactive Knowledge Graph & Concept Linkage**")

    # Sample relationship chain nodes if graph_data is absent or a list
    nodes = []
    if isinstance(graph_data, list):
        nodes = graph_data
    elif isinstance(graph_data, dict):
        nodes = graph_data.get("nodes", [default_topic, "Constitutional Evolution", "Acts & Legislation", "Key Provisions", "PYQ Application"])
    else:
        nodes = [default_topic, "Constitutional Evolution", "Acts & Legislation", "Key Provisions", "PYQ Application"]

    # Render interactive horizontal/wrap node flow
    html_chain = "<div style='display:flex; flex-wrap:wrap; align-items:center; gap:0.5rem; margin-top:0.75rem;'>"
    for idx, node in enumerate(nodes):
        node_title = node.get("title", node) if isinstance(node, dict) else str(node)
        html_chain += f"""
        <div style='background:#7C3AED; color:white; padding:0.5rem 1rem; border-radius:20px; font-weight:700; font-size:0.88rem; box-shadow:0 4px 12px rgba(124, 58, 237, 0.25); cursor:pointer;'>
            {node_title}
        </div>
        """
        if idx < len(nodes) - 1:
            html_chain += "<span style='font-size:1.2rem; color:#7C3AED; font-weight:900;'>➔</span>"
    html_chain += "</div>"

    st.markdown(html_chain, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
