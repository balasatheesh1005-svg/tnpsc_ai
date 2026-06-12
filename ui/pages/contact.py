import streamlit as st
from ui.components.cards import glass_card_html, html_fragment, render_card_styles


def render_contact_page(section_func):
    """Renders the Contact & Support page."""
    render_card_styles()  # Ensure card styles are loaded

    section_func("📞 Contact & Support")

    # Introduction Section
    st.markdown(
        """
        <div style="
            background:#ffffff;
            padding:20px;
            border-radius:12px;
            box-shadow:0 2px 8px rgba(0,0,0,0.1);
            margin-bottom:15px;
            text-align: center;
        ">
            <h3 style="color:#0F172A; margin-bottom: 10px;">Need help?</h3>
            <p style="color:#4A5568; font-size: 1rem; line-height: 1.5;">
                Reach out to us for any assistance or feedback regarding your preparation. 
                We are here to help you succeed!
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Contact Details Card
    contact_info = """
    <div style="text-align: center; padding: 10px;">
        <p style="font-size: 1.1rem; margin-bottom: 10px; color: #1E293B;">
            <strong>Email:</strong> <br>
            <a href="mailto:support@tnpscnovaai.com" style="color: #2563EB; text-decoration: none; font-weight: bold;">support@tnpscnovaai.com</a>
        </p>
        <div style="display: inline-block; background: #F1F5F9; padding: 8px 16px; border-radius: 20px; color: #64748B; font-size: 0.85rem; font-weight: 600;">
            ⏱️ Response Time: 24–48 Hours
        </div>
    </div>
    """

    st.html(glass_card_html("📩 Contact Info", extra_html=html_fragment(contact_info)))

    # Support Topics Card
    topics_list = """
    <div style="padding: 5px;">
        <ul style="list-style-type: none; padding: 0; margin: 0; color: #475569;">
            <li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="margin-right: 10px;">•</span> Account Issues</li>
            <li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="margin-right: 10px;">•</span> Progress Issues</li>
            <li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="margin-right: 10px;">•</span> Revision Issues</li>
            <li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="margin-right: 10px;">•</span> AI Teacher Issues</li>
            <li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="margin-right: 10px;">•</span> Feedback & Suggestions</li>
        </ul>
    </div>
    """

    st.html(glass_card_html("🛠️ Support Topics", extra_html=html_fragment(topics_list)))

    # Footer
    st.markdown(
        """
        <div style="
            text-align: center;
            margin-top: 30px;
            padding: 15px;
            color: #6B7280;
            font-size: 1rem;
            font-weight: 500;
        ">
            Thank you for using TNPSC Nova AI ❤️
        </div>
        """,
        unsafe_allow_html=True,
    )
