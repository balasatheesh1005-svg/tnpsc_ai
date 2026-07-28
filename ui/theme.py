import streamlit as st


COLORS = {
    "primary": "#0F172A",
    "accent": "#2563EB",
    "success": "#22C55E",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "gold": "#D97706",
    "muted": "#64748B",
    "card": "#FFFFFF",
    "line": "#E2E8F0",
    "soft": "#F8FAFC",
    "sidebar": "#EEF2FF",
}


def render_theme_css():
    st.markdown(
        f"""
        <style>
        /*
         * Remove Streamlit-owned sharing/branding controls only.  Keep the
         * toolbar itself because Streamlit renders the collapsed-sidebar
         * opener inside it.
         */
        [data-testid="stToolbarActions"],
        [data-testid="stAppDeployButton"],
        [data-testid="stMainMenu"],
        #MainMenu,
        .stDeployButton,
        footer,
        [data-testid="stFooter"],
        #viewerBadge_link,
        [class*="viewerBadge_container"],
        [class*="viewerBadge_link"] {{
            display: none !important;
            visibility: hidden !important;
        }}

        /* Keep both sidebar controls operable above page content at all times. */
        [data-testid="stToolbar"]:has([data-testid="stExpandSidebarButton"]),
        [data-testid="stExpandSidebarButton"],
        [data-testid="stSidebarCollapseButton"] {{
            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;
            pointer-events: auto !important;
            position: relative;
            z-index: 1000000 !important;
        }}

        :root {{
            --nova-primary: {COLORS["primary"]};
            --nova-accent: {COLORS["accent"]};
            --nova-success: {COLORS["success"]};
            --nova-warning: {COLORS["warning"]};
            --nova-danger: {COLORS["danger"]};
            --nova-gold: {COLORS["gold"]};
            --nova-muted: {COLORS["muted"]};
            --nova-card: {COLORS["card"]};
            --nova-line: {COLORS["line"]};
            --nova-soft: {COLORS["soft"]};
            --nova-sidebar: {COLORS["sidebar"]};
        }}

        .block-container {{
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 980px;
        }}

        div[data-testid="stVerticalBlock"] {{
            gap: 0.85rem;
        }}

        div[data-testid="column"] {{
            min-width: 0;
        }}

        .stButton>button {{
            width: 100%;
            min-height: 3rem;
            border: 0;
            border-radius: 14px;
            color: #FFFFFF;
            font-weight: 850;
            background: linear-gradient(135deg, var(--nova-primary), var(--nova-accent));
            box-shadow: 0 12px 24px rgba(37, 99, 235, 0.22);
        }}

        .stButton>button:hover {{
            border: 0;
            color: #FFFFFF;
            transform: translateY(-1px);
            box-shadow: 0 16px 30px rgba(37, 99, 235, 0.3);
        }}

        section[data-testid="stSidebar"] {{
            background:
                radial-gradient(circle at 20% 0%, rgba(37, 99, 235, 0.16), transparent 34%),
                linear-gradient(180deg, #F8FAFC 0%, var(--nova-sidebar) 100%);
            border-right: 1px solid rgba(148, 163, 184, 0.28);
        }}

        section[data-testid="stSidebar"] > div {{
            padding: 1rem 0.85rem;
        }}

        section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
            gap: 0.75rem;
        }}

        .sidebar-brand {{
            border: 1px solid rgba(255, 255, 255, 0.72);
            border-radius: 24px;
            padding: 1rem;
            color: #FFFFFF;
            background:
                radial-gradient(circle at 88% 12%, rgba(34, 197, 94, 0.35), transparent 30%),
                linear-gradient(135deg, var(--nova-primary), #1D4ED8);
            box-shadow: 0 18px 36px rgba(15, 23, 42, 0.16);
        }}

        .sidebar-brand-mark {{
            width: 42px;
            height: 42px;
            display: grid;
            place-items: center;
            border-radius: 14px;
            background: rgba(255, 255, 255, 0.16);
            font-size: 1.35rem;
            margin-bottom: 0.75rem;
        }}

        .sidebar-brand-title {{
            font-size: 1.08rem;
            font-weight: 950;
            line-height: 1.12;
            letter-spacing: 0;
        }}

        .sidebar-brand-copy {{
            margin-top: 0.35rem;
            color: rgba(255, 255, 255, 0.82);
            font-size: 0.78rem;
            line-height: 1.35;
        }}

        .sidebar-welcome {{
            border: 1px solid rgba(226, 232, 240, 0.92);
            border-radius: 20px;
            padding: 0.9rem;
            background: rgba(255, 255, 255, 0.78);
            box-shadow: 0 12px 24px rgba(15, 23, 42, 0.06);
            backdrop-filter: blur(14px);
        }}

        .sidebar-welcome-label {{
            color: var(--nova-muted);
            font-size: 0.75rem;
            font-weight: 850;
            text-transform: uppercase;
            letter-spacing: 0;
        }}

        .sidebar-welcome-name {{
            color: var(--nova-primary);
            font-size: 1rem;
            font-weight: 950;
            margin-top: 0.2rem;
            overflow-wrap: anywhere;
        }}

        .sidebar-stat-row {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.35rem;
            margin-top: 0.75rem;
        }}

        .sidebar-stat {{
            border-radius: 12px;
            padding: 0.45rem;
            background: #F8FAFC;
            text-align: center;
        }}

        .sidebar-stat-value {{
            color: var(--nova-primary);
            font-size: 0.84rem;
            font-weight: 950;
            line-height: 1.1;
        }}

        .sidebar-stat-label {{
            color: var(--nova-muted);
            font-size: 0.66rem;
            font-weight: 800;
            margin-top: 0.15rem;
        }}

        section[data-testid="stSidebar"] .nav {{
            background: rgba(255, 255, 255, 0.82) !important;
            border: 1px solid rgba(226, 232, 240, 0.92) !important;
            border-radius: 24px !important;
            padding: 0.75rem !important;
            box-shadow: 0 18px 36px rgba(15, 23, 42, 0.08) !important;
            backdrop-filter: blur(14px);
        }}

        section[data-testid="stSidebar"] .nav-link {{
            border-radius: 999px !important;
            margin: 0.28rem 0 !important;
            padding: 0.78rem 0.95rem !important;
            color: #334155 !important;
            font-weight: 800 !important;
            letter-spacing: 0 !important;
            transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease, color 180ms ease !important;
        }}

        section[data-testid="stSidebar"] .nav-link:hover {{
            background: #EFF6FF !important;
            color: var(--nova-accent) !important;
            transform: translateX(3px);
        }}

        section[data-testid="stSidebar"] .nav-link.active {{
            background: linear-gradient(135deg, var(--nova-primary), var(--nova-accent)) !important;
            color: #FFFFFF !important;
            box-shadow: 0 12px 24px rgba(37, 99, 235, 0.26) !important;
        }}

        section[data-testid="stSidebar"] .nav-link i {{
            margin-right: 0.65rem !important;
        }}

        @media (max-width: 640px) {{
            .block-container {{
                padding-left: 0.75rem;
                padding-right: 0.75rem;
            }}

            section[data-testid="stSidebar"] .nav {{
                border-radius: 18px !important;
                padding: 0.55rem !important;
            }}

            section[data-testid="stSidebar"] .nav-link {{
                border-radius: 16px !important;
                padding: 0.72rem 0.82rem !important;
            }}
        }}

        /* --- UNIVERSAL QUESTION RENDERER STYLES --- */
        .statement-card {{
            background: rgba(248, 250, 252, 0.9);
            border: 1px solid rgba(226, 232, 240, 0.8);
            border-left: 4px solid var(--nova-accent);
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 10px;
        }}
        .statement-num {{
            font-size: 0.75rem;
            font-weight: 800;
            color: var(--nova-accent);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: block;
            margin-bottom: 4px;
        }}
        .statement-text-en {{ font-size: 0.95rem; font-weight: 600; color: #0F172A; }}
        .statement-text-ta {{ font-size: 0.9rem; color: #334155; margin-top: 4px; }}

        .ar-container {{ display: flex; flex-direction: column; gap: 10px; margin-top: 10px; }}
        .ar-box {{ border-radius: 14px; padding: 14px 18px; border: 1px solid #E2E8F0; }}
        .assertion-box {{ background: rgba(37, 99, 235, 0.05); border-left: 5px solid #2563EB; }}
        .reason-box {{ background: rgba(147, 51, 234, 0.05); border-left: 5px solid #9333EA; }}
        .ar-label {{ font-size: 0.78rem; font-weight: 850; text-transform: uppercase; display: block; margin-bottom: 4px; }}
        .assertion-box .ar-label {{ color: #2563EB; }}
        .reason-box .ar-label {{ color: #9333EA; }}

        .exp-subcard {{ border-radius: 12px; padding: 12px 16px; margin-bottom: 10px; border-left: 4px solid #94A3B8; background: #F8FAFC; }}
        .exp-subcard.context {{ border-left-color: #2563EB; background: #EFF6FF; }}
        .exp-subcard.reason {{ border-left-color: #059669; background: #ECFDF5; }}
        .exp-subcard.impact {{ border-left-color: #7C3AED; background: #F5F3FF; }}
        .exp-subcard.trap {{ border-left-color: #DC2626; background: #FEF2F2; }}
        .exp-subcard.trick {{ border-left-color: #D97706; background: #FFFBEB; }}

        .wno-card {{ background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px; margin-bottom: 10px; }}
        .wno-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }}
        .wno-badge {{ font-size: 0.68rem; font-weight: 850; padding: 2px 8px; border-radius: 99px; }}
        .correct-badge {{ background: #DCFCE7; color: #15803D; }}
        .incorrect-badge {{ background: #F1F5F9; color: #64748B; }}

        .tip-card {{ background: linear-gradient(135deg, #FEF3C7, #FDE68A); border-radius: 14px; padding: 14px 18px; color: #78350F; margin-bottom: 12px; }}
        .fact-card {{ background: linear-gradient(135deg, #E0E7FF, #C7D2FE); border-radius: 14px; padding: 14px 18px; color: #3730A3; margin-bottom: 12px; }}

        .timer-pill {{ background: #FEF2F2 !important; color: #DC2626 !important; border: 1px solid #FECACA !important; font-weight: 800 !important; }}
        .bloom {{ background: #F3E8FF !important; color: #7E22CE !important; }}
        .tamil-text {{ font-family: system-ui, -apple-system, sans-serif; line-height: 1.5; }}
        </style>
        """,
        unsafe_allow_html=True,
    )
