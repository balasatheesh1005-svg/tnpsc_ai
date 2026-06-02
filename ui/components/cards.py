import html
from textwrap import dedent
from typing import NamedTuple

import streamlit as st


class HtmlFragment(NamedTuple):
    markup: str


def _html(markup):
    return dedent(markup).strip()


def _fragment(markup):
    return HtmlFragment(_html(markup))


def html_fragment(markup):
    return _fragment(markup)


def _render_fragment(fragment):
    if fragment is None:
        return ""
    if isinstance(fragment, HtmlFragment):
        return fragment.markup
    return html.escape(str(fragment))


def render_card_styles():
    st.markdown(
        _html(
            """
        <style>
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-color: var(--nova-line);
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.76);
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
            transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
            overflow: hidden;
            backdrop-filter: blur(14px);
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:hover {
            transform: translateY(-4px);
            box-shadow: 0 18px 34px rgba(15, 23, 42, 0.13);
        }

        div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMetric"] {
            width: 100%;
            min-height: 88px;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMetricLabel"] {
            color: var(--nova-muted);
            font-size: 0.88rem;
            font-weight: 750;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMetricValue"] {
            color: var(--nova-primary);
            font-size: clamp(1.45rem, 7vw, 2rem);
            font-weight: 900;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMetricDelta"] {
            color: var(--nova-accent);
        }

        .metric-accent {
            display: block;
            width: 42px;
            height: 5px;
            border-radius: 999px;
            margin-bottom: 0.45rem;
        }

        .metric-accent.streak { background: var(--nova-warning); }
        .metric-accent.accuracy { background: var(--nova-accent); }
        .metric-accent.rank { background: var(--nova-gold); }
        .metric-accent.tests { background: var(--nova-success); }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.metric-accent.streak) {
            border-color: rgba(245, 158, 11, 0.32);
            background: linear-gradient(180deg, rgba(255, 251, 235, 0.88) 0%, rgba(255, 255, 255, 0.78) 48%);
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.metric-accent.accuracy) {
            border-color: rgba(37, 99, 235, 0.28);
            background: linear-gradient(180deg, rgba(239, 246, 255, 0.9) 0%, rgba(255, 255, 255, 0.78) 48%);
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.metric-accent.rank) {
            border-color: rgba(217, 119, 6, 0.32);
            background: linear-gradient(180deg, rgba(254, 243, 199, 0.9) 0%, rgba(255, 255, 255, 0.78) 48%);
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.metric-accent.tests) {
            border-color: rgba(34, 197, 94, 0.3);
            background: linear-gradient(180deg, rgba(236, 253, 245, 0.9) 0%, rgba(255, 255, 255, 0.78) 48%);
        }

        .nova-glass-card {
            border: 1px solid rgba(226, 232, 240, 0.86);
            border-radius: 22px;
            padding: clamp(16px, 5vw, 22px);
            background: rgba(255, 255, 255, 0.74);
            box-shadow: 0 16px 36px rgba(15, 23, 42, 0.08);
            margin-top: 0.15rem;
            transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
            backdrop-filter: blur(16px);
        }

        .nova-glass-card:hover {
            transform: translateY(-4px);
            border-color: rgba(37, 99, 235, 0.28);
            box-shadow: 0 22px 46px rgba(15, 23, 42, 0.13);
        }

        .nova-card-title {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--nova-primary);
            font-size: clamp(1.05rem, 4vw, 1.22rem);
            font-weight: 900;
            margin: 0 0 0.65rem;
            letter-spacing: 0;
            line-height: 1.2;
        }

        .nova-card-value {
            color: var(--nova-primary);
            font-size: clamp(1.25rem, 6vw, 1.75rem);
            line-height: 1.2;
            font-weight: 900;
            margin: 0;
            overflow-wrap: anywhere;
        }

        .nova-card-copy {
            color: var(--nova-muted);
            font-size: 0.95rem;
            line-height: 1.55;
            margin: 0.45rem 0 0;
        }

        .nova-section-title {
            display: flex;
            align-items: center;
            gap: 0.55rem;
            color: var(--nova-primary);
            font-size: clamp(1.08rem, 4vw, 1.28rem);
            font-weight: 900;
            letter-spacing: 0;
            margin: 0.85rem 0 0.25rem;
            line-height: 1.2;
        }

        .nova-section-title::before {
            content: "";
            width: 5px;
            height: 1.35rem;
            border-radius: 999px;
            background: linear-gradient(180deg, var(--nova-accent), var(--nova-success));
            flex: 0 0 auto;
        }

        .nova-section-title span {
            color: var(--nova-muted);
            font-size: 0.76rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0;
        }

        .analytics-grid,
        .achievement-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.75rem;
            margin-top: 0.85rem;
        }

        .analytics-item {
            border: 1px solid rgba(226, 232, 240, 0.86);
            border-radius: 16px;
            background: rgba(248, 250, 252, 0.82);
            padding: 0.85rem;
            min-width: 0;
        }

        .analytics-label {
            color: var(--nova-muted);
            font-size: 0.78rem;
            font-weight: 800;
            margin-bottom: 0.25rem;
        }

        .analytics-value {
            color: var(--nova-primary);
            font-size: clamp(1rem, 4.5vw, 1.35rem);
            font-weight: 900;
            line-height: 1.15;
            overflow-wrap: anywhere;
        }

        .gauge-wrap {
            display: grid;
            grid-template-columns: 132px minmax(0, 1fr);
            gap: 1rem;
            align-items: center;
        }

        .accuracy-gauge {
            width: 132px;
            height: 132px;
            border-radius: 50%;
            display: grid;
            place-items: center;
            background:
                radial-gradient(circle at center, rgba(255,255,255,0.98) 0 56%, transparent 57%),
                conic-gradient(var(--nova-accent) var(--accuracy), #E2E8F0 0);
            box-shadow: inset 0 0 0 1px #E2E8F0, 0 14px 26px rgba(37, 99, 235, 0.14);
        }

        .accuracy-gauge-value {
            color: var(--nova-primary);
            font-size: 1.55rem;
            font-weight: 950;
        }

        .achievement-card {
            display: grid;
            grid-template-columns: 36px minmax(0, 1fr);
            gap: 0.7rem;
            align-items: start;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            background: rgba(248, 250, 252, 0.84);
            padding: 0.85rem;
        }

        .achievement-card.unlocked {
            border-color: rgba(34, 197, 94, 0.35);
            background: linear-gradient(180deg, rgba(236, 253, 245, 0.9), rgba(255, 255, 255, 0.74));
        }

        .achievement-card.locked {
            opacity: 0.78;
        }

        .achievement-icon {
            width: 36px;
            height: 36px;
            display: grid;
            place-items: center;
            border-radius: 999px;
            color: #FFFFFF;
            background: #94A3B8;
            font-weight: 900;
        }

        .achievement-card.unlocked .achievement-icon {
            background: var(--nova-success);
        }

        .achievement-title {
            color: var(--nova-primary);
            font-size: 0.93rem;
            font-weight: 900;
            line-height: 1.2;
        }

        .achievement-copy {
            color: var(--nova-muted);
            font-size: 0.78rem;
            line-height: 1.35;
            margin-top: 0.2rem;
        }

        .achievement-state {
            display: inline-flex;
            align-items: center;
            margin-top: 0.45rem;
            border-radius: 999px;
            padding: 0.18rem 0.5rem;
            background: #E2E8F0;
            color: #475569;
            font-size: 0.72rem;
            font-weight: 850;
        }

        .achievement-card.unlocked .achievement-state {
            background: #DCFCE7;
            color: #166534;
        }

        .mini-stat {
            border-left: 4px solid var(--nova-accent);
            padding-left: 0.85rem;
            margin-top: 0.8rem;
        }

        div[data-testid="stLineChart"] {
            border-radius: 16px;
            overflow: hidden;
        }

        @media (max-width: 640px) {
            div[data-testid="stVerticalBlockBorderWrapper"]:hover,
            .nova-glass-card:hover {
                transform: translateY(-2px);
            }

            .nova-glass-card {
                border-radius: 18px;
                padding: 16px;
            }

            .analytics-grid,
            .achievement-grid,
            .gauge-wrap {
                grid-template-columns: 1fr;
            }

            .accuracy-gauge {
                width: 118px;
                height: 118px;
            }
        }
        </style>
        """
        ),
        unsafe_allow_html=True,
    )


def section_title(title, eyebrow=None):
    suffix = f" <span>{html.escape(str(eyebrow))}</span>" if eyebrow else ""
    st.markdown(
        f'<div class="nova-section-title">{html.escape(str(title))}{suffix}</div>',
        unsafe_allow_html=True,
    )


def metric_card(theme, label, value, delta):
    with st.container(border=True):
        st.markdown(
            f'<span class="metric-accent {html.escape(str(theme))}"></span>',
            unsafe_allow_html=True,
        )
        st.metric(label=label, value=value, delta=delta, delta_color="off")


def glass_card_html(title, value=None, body=None, extra_html=None):
    value_html = (
        f'<p class="nova-card-value">{html.escape(str(value))}</p>' if value is not None else ""
    )
    body_html = (
        f'<p class="nova-card-copy">{html.escape(str(body))}</p>' if body is not None else ""
    )
    return _html(
        f"""
    <section class="nova-glass-card">
        <div class="nova-card-title">{html.escape(str(title))}</div>
        {value_html}
        {body_html}
        {_render_fragment(extra_html)}
    </section>
    """
    )


def glass_card(title, value=None, body=None, extra_html=None):
    st.markdown(
        glass_card_html(title, value=value, body=body, extra_html=extra_html),
        unsafe_allow_html=True,
    )


def analytics_grid(items):
    cells = []
    for label, value in items:
        cells.append(
            _html(
                f"""
            <div class="analytics-item">
                <div class="analytics-label">{html.escape(str(label))}</div>
                <div class="analytics-value">{html.escape(str(value))}</div>
            </div>
            """
            )
        )
    return HtmlFragment(f'<div class="analytics-grid">{"".join(cells)}</div>')


def accuracy_gauge(value, body):
    safe_value = max(0, min(100, float(value or 0)))
    return _fragment(
        f"""
    <div class="gauge-wrap">
        <div class="accuracy-gauge" style="--accuracy: {safe_value * 3.6}deg;">
            <div class="accuracy-gauge-value">{safe_value:g}%</div>
        </div>
        <p class="nova-card-copy">{html.escape(str(body))}</p>
    </div>
    """
    )


def achievement_card(title, description, unlocked):
    state_class = "unlocked" if unlocked else "locked"
    state_label = "Unlocked" if unlocked else "Locked"
    icon = "✓" if unlocked else "○"

    return _fragment(
        f"""
    <div class="achievement-card {state_class}">
        <div class="achievement-icon">{icon}</div>
        <div>
            <div class="achievement-title">{html.escape(str(title))}</div>
            <div class="achievement-copy">{html.escape(str(description))}</div>
            <div class="achievement-state">{state_label}</div>
        </div>
    </div>
    """
    )


def achievement_grid(achievements):
    cards = "".join(
        achievement_card(title, description, unlocked).markup
        for title, description, unlocked in achievements
    )
    return HtmlFragment(f'<div class="achievement-grid">{cards}</div>')
