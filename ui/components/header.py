import html

import streamlit as st


def _to_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def render_header_styles():
    st.markdown(
        """
        <style>
        .nova-hero {
            width: 100%;
            border-radius: 26px;
            padding: clamp(20px, 6vw, 34px);
            margin: 0 0 1rem 0;
            color: #FFFFFF;
            background:
                radial-gradient(circle at 88% 12%, rgba(34, 197, 94, 0.34), transparent 28%),
                linear-gradient(135deg, #0F172A 0%, #1E3A8A 54%, #2563EB 100%);
            box-shadow: 0 22px 48px rgba(15, 23, 42, 0.22);
            overflow: hidden;
        }

        .nova-hero-kicker {
            display: inline-flex;
            align-items: center;
            min-height: 28px;
            padding: 4px 10px;
            border: 1px solid rgba(255, 255, 255, 0.22);
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.12);
            color: rgba(255, 255, 255, 0.9);
            font-size: 0.78rem;
            font-weight: 750;
            letter-spacing: 0;
            margin-bottom: 0.9rem;
        }

        .nova-hero-title {
            margin: 0;
            color: #FFFFFF;
            font-size: clamp(1.7rem, 8vw, 3.15rem);
            line-height: 1.05;
            font-weight: 950;
            letter-spacing: 0;
            overflow-wrap: anywhere;
        }

        .nova-hero-subtitle {
            margin: 0.7rem 0 0;
            color: rgba(255, 255, 255, 0.88);
            font-size: clamp(0.98rem, 3.8vw, 1.2rem);
            line-height: 1.45;
            max-width: 640px;
        }

        .nova-hero-stats {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.65rem;
            margin-top: 1.25rem;
        }

        .nova-hero-stat {
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 16px;
            padding: 0.75rem;
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(12px);
            min-width: 0;
        }

        .nova-hero-stat-value {
            color: #FFFFFF;
            font-size: clamp(1rem, 5vw, 1.35rem);
            font-weight: 950;
            line-height: 1.1;
            overflow-wrap: anywhere;
        }

        .nova-hero-stat-label {
            margin-top: 0.2rem;
            color: rgba(255, 255, 255, 0.72);
            font-size: 0.72rem;
            font-weight: 800;
        }

        @media (max-width: 767px) {
            .nova-hero {
                border-radius: 20px;
                padding: 20px;
            }

            .nova-hero-stats {
                grid-template-columns: repeat(2, minmax(0, 1fr));
                grid-auto-rows: 1fr;
                gap: 0.85rem;
                align-items: stretch;
            }

            .nova-hero-stat {
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                min-height: 125px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_dashboard_hero(username, rank, accuracy, streak):
    safe_username = html.escape(str(username or "Aspirant"))
    rank_text = f"#{rank}" if rank else "Not ranked"
    accuracy_value = _to_float(accuracy)
    streak_value = int(_to_float(streak))

    st.markdown(
        f"""
        <section class="nova-hero">
            <div class="nova-hero-kicker">🏛️ TNPSC NOVA AI</div>
            <h1 class="nova-hero-title">Welcome back, {safe_username}</h1>
            <p class="nova-hero-subtitle">India's AI Powered TNPSC Preparation Platform</p>
            <div class="nova-hero-stats">
                <div class="nova-hero-stat">
                    <div class="nova-hero-stat-value">{html.escape(str(rank_text))}</div>
                    <div class="nova-hero-stat-label">Rank</div>
                </div>
                <div class="nova-hero-stat">
                    <div class="nova-hero-stat-value">{accuracy_value:g}%</div>
                    <div class="nova-hero-stat-label">Accuracy</div>
                </div>
                <div class="nova-hero-stat">
                    <div class="nova-hero-stat-value">{streak_value}</div>
                    <div class="nova-hero-stat-label">Day Streak</div>
                </div>
                <div class="nova-hero-stat">
                    <div class="nova-hero-stat-value">AI</div>
                    <div class="nova-hero-stat-label">Mentor Mode</div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_branding(username, rank, accuracy, streak):
    safe_username = html.escape(str(username or "Aspirant"))
    rank_text = f"#{rank}" if rank else "--"
    accuracy_value = _to_float(accuracy)
    streak_value = int(_to_float(streak))

    st.markdown(
        f"""
        <div class="sidebar-brand">
            <div class="sidebar-brand-mark">🏛️</div>
            <div class="sidebar-brand-title">TNPSC<br>Nova AI</div>
            <div class="sidebar-brand-copy">Premium AI preparation for focused TNPSC aspirants.</div>
        </div>
        <div class="sidebar-welcome">
            <div class="sidebar-welcome-label">Welcome</div>
            <div class="sidebar-welcome-name">{safe_username}</div>
            <div class="sidebar-stat-row">
                <div class="sidebar-stat">
                    <div class="sidebar-stat-value">{html.escape(str(rank_text))}</div>
                    <div class="sidebar-stat-label">Rank</div>
                </div>
                <div class="sidebar-stat">
                    <div class="sidebar-stat-value">{accuracy_value:g}%</div>
                    <div class="sidebar-stat-label">Accuracy</div>
                </div>
                <div class="sidebar-stat">
                    <div class="sidebar-stat-value">{streak_value}</div>
                    <div class="sidebar-stat-label">Streak</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
