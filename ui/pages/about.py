import streamlit as st
from ui.components.cards import glass_card_html, html_fragment, render_card_styles


def render_about_page(section_func):
    render_card_styles()  # Ensure card styles are loaded

    section_func("ℹ️ About TNPSC Nova AI")

    st.markdown(
        """
        <div style="
            background:#ffffff;
            padding:15px;
            border-radius:12px;
            box-shadow:0 2px 8px rgba(0,0,0,0.1);
            margin-bottom:15px;
            text-align: center;
        ">
            <h3 style="color:#0F172A; margin-bottom: 10px;">TNPSC Nova AI</h3>
            <p style="color:#4A5568; font-size: 1rem; line-height: 1.5;">
                TNPSC Nova AI is an AI-powered TNPSC preparation platform designed to help aspirants learn, practice, revise, and track progress efficiently.
            </p>
            <p style="color:#6B7280; font-size: 0.85rem; margin-top: 15px;">
                <strong>Version:</strong> 1.0.0
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    features_list = """
    <ul style="list-style-type: none; padding: 0; margin: 0;">
        <li style="margin-bottom: 8px;"><span style="color: #22C55E; font-weight: bold;">✅</span> Daily Tests</li>
        <li style="margin-bottom: 8px;"><span style="color: #22C55E; font-weight: bold;">✅</span> AI Teacher</li>
        <li style="margin-bottom: 8px;"><span style="color: #22C55E; font-weight: bold;">✅</span> Personal Mentor</li>
        <li style="margin-bottom: 8px;"><span style="color: #22C55E; font-weight: bold;">✅</span> Mentor Chat</li>
        <li style="margin-bottom: 8px;"><span style="color: #22C55E; font-weight: bold;">✅</span> Weak Topic Practice</li>
        <li style="margin-bottom: 8px;"><span style="color: #22C55E; font-weight: bold;">✅</span> Revision Scheduler</li>
        <li style="margin-bottom: 8px;"><span style="color: #22C55E; font-weight: bold;">✅</span> XP & Level System</li>
        <li style="margin-bottom: 8px;"><span style="color: #22C55E; font-weight: bold;">✅</span> Leaderboards</li>
    </ul>
    """

    st.html(glass_card_html("✨ Features", extra_html=html_fragment(features_list)))

    st.html(
        glass_card_html(
            "🎯 Mission",
            extra_html=html_fragment("""
            <p style="color:#4A5568; font-size: 1rem; line-height: 1.5; text-align: center;">
                To become India's No.1 AI-powered TNPSC preparation platform.
            </p>
            """),
        )
    )

    st.markdown(
        """
        <div style="
            text-align: center;
            margin-top: 30px;
            padding: 15px;
            border-top: 1px solid #E2E8F0;
            color: #6B7280;
            font-size: 0.9rem;
        ">
            Made for TNPSC Aspirants 🇮🇳
        </div>
        """,
        unsafe_allow_html=True,
    )
