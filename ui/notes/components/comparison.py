import streamlit as st
import pandas as pd
from ui.notes.layout import section_anchor


def render_comparison(comparison_data):
    """
    Renders Component 8: Responsive Comparison Table Card
    Theme Accent: Cyan (#0891B2)
    Renders structured comparison as clean responsive HTML table (never bullets).
    """
    if not comparison_data:
        return

    section_anchor("sec_comparison")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #ECFEFF; border-left: 5px solid #0891B2;">', unsafe_allow_html=True)
    st.markdown("### ⚖️ **Comparison Table**")

    if isinstance(comparison_data, list):
        for comp in comparison_data:
            if isinstance(comp, dict):
                title = comp.get("title", "Comparison")
                st.subheader(f"📊 {title}")
                
                points = comp.get("points", {})
                en_list = points.get("en", [])
                ta_list = points.get("ta", [])

                if en_list or ta_list:
                    tab1, tab2 = st.tabs(["🇬🇧 English Table", "🇮🇳 தமிழ் அட்டவணை"])
                    
                    with tab1:
                        if en_list:
                            # Render two-column comparison card grid or table
                            table_html = "<table style='width:100%; border-collapse:collapse; background:white; border-radius:8px; overflow:hidden;'><tr><th style='background:#0891B2; color:white; padding:10px; text-align:left;'>Feature / Point</th></tr>"
                            for item in en_list:
                                table_html += f"<tr><td style='padding:8px 12px; border-bottom:1px solid #E2E8F0; color:#1E293B;'>{item}</td></tr>"
                            table_html += "</table>"
                            st.markdown(table_html, unsafe_allow_html=True)

                    with tab2:
                        if ta_list:
                            table_html = "<table style='width:100%; border-collapse:collapse; background:white; border-radius:8px; overflow:hidden;'><tr><th style='background:#0891B2; color:white; padding:10px; text-align:left;'>அம்சம் / குறிப்பு</th></tr>"
                            for item in ta_list:
                                table_html += f"<tr><td style='padding:8px 12px; border-bottom:1px solid #E2E8F0; color:#1E293B;'>{item}</td></tr>"
                            table_html += "</table>"
                            st.markdown(table_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
