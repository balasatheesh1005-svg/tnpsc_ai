import streamlit as st
import pandas as pd
from ui.notes.layout import bilingual_panels, localized_title, section_anchor


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
                st.subheader(f"📊 {localized_title(title_en, title_ta)}")

                headers_en = comp.get("headers_en", [])
                headers_ta = comp.get("headers_ta", [])
                rows_en = comp.get("rows_en", [])
                rows_ta = comp.get("rows_ta", [])
                points = comp.get("points", {})
                en_list = points.get("en", [])
                ta_list = points.get("ta", [])

                if headers_en or rows_en or en_list or ta_list:
                    english_data = rows_en or en_list
                    tamil_data = rows_ta or ta_list
                    for language, panel in bilingual_panels(
                        english_data,
                        tamil_data,
                        "🇬🇧 English Table",
                        "🇮🇳 தமிழ் அட்டவணை",
                    ):
                        with panel:
                            if language == "en":
                                headers = headers_en
                                rows = rows_en
                                points_list = en_list
                                fallback_header = "Feature / Point"
                            else:
                                headers = headers_ta
                                rows = rows_ta
                                points_list = ta_list
                                fallback_header = "அம்சம் / குறிப்பு"

                            if headers and rows:
                                table_html = "<table style='width:100%; border-collapse:collapse; background:white; border-radius:8px; overflow:hidden; margin-bottom:15px;'>"
                                table_html += "<tr>"
                                for header in headers:
                                    table_html += f"<th style='background:#0891B2; color:white; padding:10px; text-align:left; border:1px solid #0891B2;'>{header}</th>"
                                table_html += "</tr>"
                                for row in rows:
                                    table_html += "<tr>"
                                    for cell in row:
                                        table_html += f"<td style='padding:8px 12px; border:1px solid #E2E8F0; color:#1E293B;'>{cell}</td>"
                                    table_html += "</tr>"
                                table_html += "</table>"
                                st.markdown(table_html, unsafe_allow_html=True)
                            elif points_list:
                                table_html = f"<table style='width:100%; border-collapse:collapse; background:white; border-radius:8px; overflow:hidden;'><tr><th style='background:#0891B2; color:white; padding:10px; text-align:left;'>{fallback_header}</th></tr>"
                                for item in points_list:
                                    table_html += f"<tr><td style='padding:8px 12px; border-bottom:1px solid #E2E8F0; color:#1E293B;'>{item}</td></tr>"
                                table_html += "</table>"
                                st.markdown(table_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
