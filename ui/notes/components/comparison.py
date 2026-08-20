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
    st.markdown("### ⚖️ **Comparison Tables**")

    if isinstance(comparison_data, list):
        for comp in comparison_data:
            if isinstance(comp, dict):
                title_en = comp.get("title_en") or comp.get("title") or "Comparison"
                title_ta = comp.get("title_ta") or comp.get("title") or title_en
                st.subheader(f"📊 {title_en}")

                headers_en = comp.get("headers_en", [])
                headers_ta = comp.get("headers_ta", [])
                rows_en = comp.get("rows_en", [])
                rows_ta = comp.get("rows_ta", [])
                points = comp.get("points", {})
                en_list = points.get("en", [])
                ta_list = points.get("ta", [])

                if headers_en or rows_en or en_list or ta_list:
                    tab1, tab2 = st.tabs(["🇬🇧 English Table", "🇮🇳 தமிழ் அட்டவணை"])

                    with tab1:
                        if headers_en and rows_en:
                            table_html = "<table style='width:100%; border-collapse:collapse; background:white; border-radius:8px; overflow:hidden; margin-bottom:15px;'>"
                            table_html += "<tr>"
                            for h in headers_en:
                                table_html += f"<th style='background:#0891B2; color:white; padding:10px; text-align:left; border:1px solid #0891B2;'>{h}</th>"
                            table_html += "</tr>"
                            for row in rows_en:
                                table_html += "<tr>"
                                for cell in row:
                                    table_html += f"<td style='padding:8px 12px; border:1px solid #E2E8F0; color:#1E293B;'>{cell}</td>"
                                table_html += "</tr>"
                            table_html += "</table>"
                            st.markdown(table_html, unsafe_allow_html=True)
                        elif en_list:
                            table_html = "<table style='width:100%; border-collapse:collapse; background:white; border-radius:8px; overflow:hidden;'><tr><th style='background:#0891B2; color:white; padding:10px; text-align:left;'>Feature / Point</th></tr>"
                            for item in en_list:
                                table_html += f"<tr><td style='padding:8px 12px; border-bottom:1px solid #E2E8F0; color:#1E293B;'>{item}</td></tr>"
                            table_html += "</table>"
                            st.markdown(table_html, unsafe_allow_html=True)

                    with tab2:
                        if headers_ta and rows_ta:
                            table_html = "<table style='width:100%; border-collapse:collapse; background:white; border-radius:8px; overflow:hidden; margin-bottom:15px;'>"
                            table_html += "<tr>"
                            for h in headers_ta:
                                table_html += f"<th style='background:#0891B2; color:white; padding:10px; text-align:left; border:1px solid #0891B2;'>{h}</th>"
                            table_html += "</tr>"
                            for row in rows_ta:
                                table_html += "<tr>"
                                for cell in row:
                                    table_html += f"<td style='padding:8px 12px; border:1px solid #E2E8F0; color:#1E293B;'>{cell}</td>"
                                table_html += "</tr>"
                            table_html += "</table>"
                            st.markdown(table_html, unsafe_allow_html=True)
                        elif ta_list:
                            table_html = "<table style='width:100%; border-collapse:collapse; background:white; border-radius:8px; overflow:hidden;'><tr><th style='background:#0891B2; color:white; padding:10px; text-align:left;'>அம்சம் / குறிப்பு</th></tr>"
                            for item in ta_list:
                                table_html += f"<tr><td style='padding:8px 12px; border-bottom:1px solid #E2E8F0; color:#1E293B;'>{item}</td></tr>"
                            table_html += "</table>"
                            st.markdown(table_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
