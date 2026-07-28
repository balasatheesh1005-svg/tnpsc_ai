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
        _html("""
        <style>
        html, body {
            overflow-x: hidden;
            width: 100%;
            max-width: 100vw;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-color: var(--nova-line);
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.76);
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
            transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
            overflow: hidden;
            backdrop-filter: blur(14px);
            line-height: 1.2;
            font-weight: 900;
            word-break: break-word;
            overflow-wrap: anywhere;
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
            word-break: break-word;
            overflow-wrap: anywhere;
        }

        .nova-card-copy {
            color: var(--nova-muted);
            font-size: 0.95rem;
            line-height: 1.55;
            margin: 0.45rem 0 0;
        }

        .nova-plan-row,
        .nova-plan-footer {
            display: grid;
            grid-template-columns: max-content minmax(0, 1fr);
            gap: 0.75rem 1rem;
            align-items: center;
            margin-top: 1rem;
        }

        .nova-plan-label {
            color: var(--nova-primary);
            font-size: 0.96rem;
            font-weight: 900;
            line-height: 1.3;
            white-space: nowrap;
        }

        .nova-plan-row .nova-card-copy,
        .nova-plan-footer .nova-card-copy {
            margin: 0;
        }

        .nova-plan-footer {
            margin-top: 1.25rem;
            border-top: 1px solid rgba(226, 232, 240, 0.76);
            padding-top: 1rem;
        }

        .revision-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .revision-list {
            display: grid;
            gap: 0.75rem;
            margin-top: 0.75rem;
        }

        .revision-item {
            border: 1px solid rgba(226, 232, 240, 0.86);
            border-radius: 16px;
            padding: 0.85rem;
            background: rgba(248, 250, 252, 0.92);
            display: grid;
            gap: 0.35rem;
        }

        .revision-item-title {
            color: var(--nova-primary);
            font-size: 0.98rem;
            font-weight: 900;
            margin: 0;
            line-height: 1.2;
        }

        .revision-item-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            align-items: center;
            justify-content: space-between;
            color: #475569;
            font-size: 0.9rem;
        }

        .revision-badge {
            border-radius: 999px;
            padding: 0.22rem 0.6rem;
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 0.02em;
            background: rgba(37, 99, 235, 0.12);
            color: #1D4ED8;
        }

        .revision-badge.overdue {
            background: rgba(239, 68, 68, 0.12);
            color: #B91C1C;
        }

        .revision-badge.today {
            background: rgba(251, 191, 36, 0.16);
            color: #92400E;
        }

        .revision-badge.upcoming {
            background: rgba(34, 197, 94, 0.16);
            color: #166534;
        }

        .daily-mission-list {
            display: grid;
            gap: 0.75rem;
            margin-top: 0.75rem;
        }

        .daily-mission-item {
            display: grid;
            grid-template-columns: 2rem minmax(0, 1fr);
            gap: 0.7rem;
            align-items: center;
            border: 1px solid rgba(226, 232, 240, 0.86);
            border-radius: 16px;
            padding: 0.85rem;
            background: rgba(248, 250, 252, 0.92);
        }

        .daily-mission-status {
            width: 2rem;
            height: 2rem;
            display: grid;
            place-items: center;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.78);
            font-size: 1.05rem;
            box-shadow: inset 0 0 0 1px rgba(226, 232, 240, 0.9);
        }

        .daily-mission-label {
            color: var(--nova-primary);
            font-size: 0.98rem;
            font-weight: 900;
            line-height: 1.25;
            overflow-wrap: anywhere;
        }

        .daily-mission-footer {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 0.65rem;
            margin-top: 1rem;
            border-top: 1px solid rgba(226, 232, 240, 0.76);
            padding-top: 0.85rem;
            color: #92400E;
            font-size: 0.9rem;
            font-weight: 900;
        }

        .daily-mission-claimed {
            margin-top: 0.85rem;
            border-radius: 999px;
            padding: 0.65rem 0.9rem;
            background: rgba(236, 253, 245, 0.95);
            color: #166534;
            font-size: 0.92rem;
            font-weight: 900;
            text-align: center;
            border: 1px solid rgba(34, 197, 94, 0.28);
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.daily-mission-list) div[data-testid="stButton"] button {
            width: 100%;
            min-height: 2.75rem;
            border-radius: 999px;
            border: 0;
            background: linear-gradient(135deg, #FBBF24, #F59E0B);
            color: #111827;
            font-weight: 900;
            box-shadow: 0 12px 24px rgba(245, 158, 11, 0.22);
        }

        .question-card {
            border: 1px solid rgba(37, 99, 235, 0.14);
            border-radius: 26px;
            padding: 1.25rem;
            background: rgba(255, 255, 255, 0.88);
            box-shadow: 0 24px 58px rgba(15, 23, 42, 0.08);
            margin-top: 1rem;
        }

        .question-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-bottom: 1rem;
        }

        .question-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.45rem 0.85rem;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 800;
            letter-spacing: 0.01em;
            white-space: nowrap;
        }

        .question-badge.subject {
            color: #0F172A;
            background: rgba(59, 130, 246, 0.12);
            border: 1px solid rgba(59, 130, 246, 0.18);
        }

        .question-badge.difficulty {
            color: #111827;
            background: rgba(251, 191, 36, 0.16);
            border: 1px solid rgba(245, 158, 11, 0.22);
        }

        .question-title {
            font-size: 22px;
            font-weight: 700;
            margin: 0 0 0.75rem;
            color: var(--nova-primary);
            line-height: 1.2;
        }

        .progress-header {
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            gap: 0.75rem;
            align-items: center;
            margin-bottom: 1rem;
        }

        .progress-details {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
            align-items: center;
            color: var(--nova-primary);
            font-weight: 700;
        }

        .progress-pill {
            border-radius: 999px;
            padding: 0.45rem 0.85rem;
            background: rgba(37, 99, 235, 0.12);
            color: #1D4ED8;
            font-size: 0.92rem;
            font-weight: 800;
        }

        .success-pill {
            border-radius: 999px;
            padding: 0.45rem 0.85rem;
            background: rgba(16, 185, 129, 0.16);
            color: #047857;
            font-size: 0.92rem;
            font-weight: 800;
        }

        .answer-feedback {
            border: 1px solid rgba(148, 163, 184, 0.28);
            border-radius: 22px;
            padding: 1rem;
            background: rgba(248, 250, 252, 0.94);
            margin-top: 1rem;
        }

        .answer-feedback.correct {
            border-color: rgba(16, 185, 129, 0.32);
            background: rgba(236, 253, 245, 0.94);
            color: #065F46;
        }

        .answer-feedback.wrong {
            border-color: rgba(239, 68, 68, 0.32);
            background: rgba(254, 226, 226, 0.96);
            color: #991B1B;
        }

        .explanation-card {
            border: 1px solid rgba(37, 99, 235, 0.16);
            border-radius: 24px;
            padding: 1.2rem;
            background: rgba(255, 255, 255, 0.93);
            margin-top: 1rem;
        }

        .explanation-card h4 {
            margin: 0 0 0.75rem;
            font-size: 1rem;
            color: var(--nova-primary);
            font-weight: 900;
        }

        .explanation-card p {
            margin: 0;
            color: var(--nova-muted);
            line-height: 1.65;
        }

        .revision-empty-state {
            border: 1px solid rgba(16, 185, 129, 0.22);
            background: rgba(236, 253, 245, 0.95);
            color: #166534;
            border-radius: 18px;
            padding: 1rem;
            text-align: center;
            display: grid;
            gap: 0.35rem;
        }

        .revision-empty-state .nova-card-title {
            color: #047857;
            font-size: 1rem;
            margin-bottom: 0.25rem;
        }

        .revision-empty-state .nova-card-copy {
            color: #166534;
            margin-top: 0;
        }

        .revision-start-button {
            display: inline-block;
            margin-top: 1rem;
            padding: 0.75rem 1rem;
            border-radius: 999px;
            background: linear-gradient(135deg, #2563EB, #0EA5E9);
            color: #FFFFFF;
            font-weight: 800;
            text-decoration: none;
            box-shadow: 0 10px 24px rgba(14, 165, 233, 0.18);
        }

        .nova-hidden-recommendation {
            display: none;
            visibility: hidden;
            height: 0;
            overflow: hidden;
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
            box-shadow: 0 0 0 6px rgba(148, 163, 184, 0.1);
        }

        .achievement-icon.bronze {
            background: linear-gradient(180deg, #c2410c, #f59e0b);
            box-shadow: 0 14px 30px rgba(249, 115, 22, 0.18);
        }

        .achievement-icon.silver {
            background: linear-gradient(180deg, #e5e7eb, #9ca3af);
            color: #111827;
            box-shadow: 0 14px 30px rgba(148, 163, 184, 0.18);
        }

        .achievement-icon.gold {
            background: linear-gradient(180deg, #fde68a, #fbbf24);
            color: #92400e;
            box-shadow: 0 14px 30px rgba(245, 158, 11, 0.18);
        }

        .achievement-card.bronze.unlocked {
            border-color: rgba(181, 108, 44, 0.35);
            background: linear-gradient(180deg, rgba(255, 244, 229, 0.9), rgba(255, 255, 255, 0.74));
        }

        .achievement-card.silver.unlocked {
            border-color: rgba(148, 163, 184, 0.35);
            background: linear-gradient(180deg, rgba(248, 250, 252, 0.92), rgba(255, 255, 255, 0.74));
        }

        .achievement-card.gold.unlocked {
            border-color: rgba(245, 158, 11, 0.35);
            background: linear-gradient(180deg, rgba(255, 247, 237, 0.9), rgba(255, 255, 255, 0.74));
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

        div[data-testid="stProgress"] > div > div {
            min-height: 18px !important;
            height: 18px !important;
            border-radius: 999px !important;
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
            .gauge-wrap,
            .nova-plan-row,
            .revision-grid {
                grid-template-columns: 1fr;
            }

            .progress-header,
            .question-badges {
                display: block;
            }

            .question-card,
            .answer-feedback,
            .explanation-card {
                padding: 1rem;
            }

            .revision-item-meta {
                flex-direction: column;
                align-items: flex-start;
            }

            div[data-testid="stProgress"] > div > div {
                min-height: 18px !important;
                height: 18px !important;
                border-radius: 999px !important;
            }

            .accuracy-gauge {
                width: 118px;
                height: 118px;
            }
        }
        </style>
        """),
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
        f'<p class="nova-card-value">{html.escape(str(value))}</p>'
        if value is not None
        else ""
    )
    body_html = (
        f'<p class="nova-card-copy">{html.escape(str(body))}</p>'
        if body is not None
        else ""
    )
    return _html(f"""
    <section class="nova-glass-card">
        <div class="nova-card-title">{html.escape(str(title))}</div>
        {value_html}
        {body_html}
        {_render_fragment(extra_html)}
    </section>
    """)


def glass_card(title, value=None, body=None, extra_html=None):
    st.html(glass_card_html(title, value=value, body=body, extra_html=extra_html))


def study_plan_card_html(
    title,
    revision,
    practice,
    goal,
    estimated_time=None,
    message=None,
    raw_recommendation=None,
):
    estimated_html = (
        f'<div class="nova-plan-footer">'
        f'<div class="nova-plan-label">⏱ Estimated Time</div>'
        f'<div class="nova-card-copy">{html.escape(str(estimated_time))}</div>'
        "</div>"
        if estimated_time is not None
        else ""
    )
    message_html = (
        f'<p class="nova-card-copy">{html.escape(str(message))}</p>'
        if message is not None
        else ""
    )
    hidden_recommendation = (
        f'<div class="nova-hidden-recommendation">{html.escape(str(raw_recommendation))}</div>'
        if raw_recommendation is not None
        else ""
    )
    return _html(f"""
    <section class="nova-glass-card">
        <div class="nova-card-title">{html.escape(str(title))}</div>
        {message_html}
        <div class="nova-plan-row">
            <div class="nova-plan-label">📚 Revision</div>
            <div class="nova-card-copy">{html.escape(str(revision))}</div>
        </div>
        <div class="nova-plan-row">
            <div class="nova-plan-label">📝 Practice</div>
            <div class="nova-card-copy"><strong>{html.escape(str(practice))}</strong></div>
        </div>
        <div class="nova-plan-row">
            <div class="nova-plan-label">🎯 Goal</div>
            <div class="nova-card-copy">{html.escape(str(goal))}</div>
        </div>
        {estimated_html}
        {hidden_recommendation}
    </section>
    """)


def analytics_grid(items):
    cells = []
    for label, value in items:
        cells.append(_html(f"""
            <div class="analytics-item">
                <div class="analytics-label">{html.escape(str(label))}</div>
                <div class="analytics-value">{html.escape(str(value))}</div>
            </div>
            """))
    return HtmlFragment(f'<div class="analytics-grid">{"".join(cells)}</div>')


def accuracy_gauge(value, body):
    safe_value = max(0, min(100, float(value or 0)))
    return _fragment(f"""
    <div class="gauge-wrap">
        <div class="accuracy-gauge" style="--accuracy: {safe_value * 3.6}deg;">
            <div class="accuracy-gauge-value">{safe_value:g}%</div>
        </div>
        <p class="nova-card-copy">{html.escape(str(body))}</p>
    </div>
    """)


def achievement_card(title, description, unlocked, level=None):
    state_class = "unlocked" if unlocked else "locked"
    level_class = html.escape(str(level)) if level else ""
    level_icon = {
        "bronze": "🥉",
        "silver": "🥈",
        "gold": "🏆",
    }.get(level, "✓" if unlocked else "○")
    state_label = "Unlocked" if unlocked else "Locked"

    classes = "achievement-card"
    if state_class:
        classes += f" {state_class}"
    if level_class:
        classes += f" {level_class}"

    icon_classes = "achievement-icon"
    if level_class:
        icon_classes += f" {level_class}"

    return _fragment(f"""
    <div class="{classes}">
        <div class="{icon_classes}">{level_icon}</div>
        <div>
            <div class="achievement-title">{html.escape(str(title))}</div>
            <div class="achievement-copy">{html.escape(str(description))}</div>
            <div class="achievement-state">{state_label}</div>
        </div>
    </div>
    """)


def achievement_grid(achievements):
    cards = "".join(
        achievement_card(title, description, unlocked, level).markup
        for title, description, unlocked, level in achievements
    )
    return HtmlFragment(f'<div class="achievement-grid">{cards}</div>')


def repository_progress_card(repo_type: str, completed_count: int, total_repos: int = 9) -> HtmlFragment:
    pct = int((max(1, completed_count) / max(1, total_repos)) * 100)
    formatted_name = repo_type.replace("_", " ").title()
    return _fragment(f"""
    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 16px; border-radius: 14px; margin-bottom: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap; gap: 8px;">
            <div>
                <span style="font-weight: 800; color: #0F172A; font-size: 0.95rem;">
                    📊 Repository Progress: <b>{html.escape(formatted_name)}</b>
                </span>
            </div>
            <span style="background: #2563EB; color: white; padding: 4px 12px; border-radius: 12px; font-weight: 800; font-size: 0.85rem;">
                {completed_count} / {total_repos} Completed ({pct}%)
            </span>
        </div>
        <div style="width: 100%; background: #E2E8F0; height: 10px; border-radius: 5px; overflow: hidden;">
            <div style="width: {pct}%; background: linear-gradient(90deg, #2563EB, #16A34A); height: 100%; transition: width 0.4s ease;"></div>
        </div>
    </div>
    """)


def learning_journey_roadmap(current_repo_type: str, avail: dict) -> HtmlFragment:
    stages = [
        ("notes", "Study Notes", "📖"),
        ("easy", "Easy", "🟢"),
        ("medium", "Medium", "🟡"),
        ("hard", "Hard", "🔴"),
        ("statement_based", "Statement", "📋"),
        ("assertion_reason", "Assertion & Reason", "⚖️"),
        ("match_the_following", "Match the Following", "📊"),
        ("chronology", "Chronology", "⏱️"),
        ("pyq", "PYQ", "🏛️"),
        ("grand_test", "Grand Test", "🏆"),
    ]

    curr_key = current_repo_type.lower().strip()
    order_keys = [s[0] for s in stages if s[0] != "notes"]
    curr_idx = order_keys.index(curr_key) if curr_key in order_keys else 0

    items_html = ""
    for idx, (key, label, icon) in enumerate(stages):
        if key == "notes":
            status_badge = "✅"
            bg_color = "#DCFCE7"
            text_color = "#15803D"
            border_color = "#86EFAC"
        else:
            stage_order_idx = order_keys.index(key)
            if stage_order_idx < curr_idx:
                status_badge = "✅"
                bg_color = "#DCFCE7"
                text_color = "#15803D"
                border_color = "#86EFAC"
            elif stage_order_idx == curr_idx:
                status_badge = "⏳ Current"
                bg_color = "#DBEAFE"
                text_color = "#1E40AF"
                border_color = "#93C5FD"
            elif avail.get(key, False):
                status_badge = "🟢 Ready"
                bg_color = "#F0FDF4"
                text_color = "#166534"
                border_color = "#BBF7D0"
            else:
                status_badge = "🔒 Locked"
                bg_color = "#F8FAFC"
                text_color = "#64748B"
                border_color = "#E2E8F0"

        arrow = " → " if idx < len(stages) - 1 else ""
        items_html += f"""
        <div style="display:inline-flex; align-items:center; margin: 3px 2px;">
            <div style="background:{bg_color}; border:1px solid {border_color}; color:{text_color}; padding:5px 10px; border-radius:8px; font-weight:700; font-size:0.78rem; white-space:nowrap;">
                {icon} {html.escape(label)} <span style="font-size:0.72rem; opacity:0.95;">({status_badge})</span>
            </div>
            <span style="color:#94A3B8; font-weight:700; margin:0 3px; font-size:0.8rem;">{arrow}</span>
        </div>
        """

    return _fragment(f"""
    <div style="background: #FFFFFF; border: 1px solid #E2E8F0; padding: 14px; border-radius: 14px; margin-bottom: 16px;">
        <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 0.92rem; font-weight: 800;">🧭 Learning Journey Roadmap</h4>
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 2px;">
            {items_html}
        </div>
    </div>
    """)


def micro_motivation_banner(accuracy: int, streak: int, curr_idx: int) -> HtmlFragment:
    messages = []
    if accuracy >= 90:
        messages.append("🌟 Outstanding consistency! You are operating at top TNPSC accuracy levels.")
    elif accuracy >= 75:
        messages.append("📈 Solid progress! You are steadily building strong subject recall.")
    elif accuracy < 50:
        messages.append("💡 Keep pushing! Review detailed explanations to solidify weaker concepts.")

    if streak >= 7:
        messages.append("🔥 7-Day Streak Active! Your continuous effort guarantees long-term retention.")

    if curr_idx == 6:
        messages.append("🚀 Great momentum! Only two repositories remaining before Grand Test.")
    elif curr_idx == 7:
        messages.append("🏆 Milestone Unlocked! Grand Test is now unlocked for complete topic mastery.")

    if not messages:
        messages.append("💪 Every question practiced brings you closer to TNPSC success!")

    selected_msg = messages[0]
    return _fragment(f"""
    <div style="background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); border-left: 4px solid #2563EB; padding: 12px 16px; border-radius: 8px; margin-bottom: 16px; color: #1E40AF; font-weight: 700; font-size: 0.88rem;">
        {html.escape(selected_msg)}
    </div>
    """)


def mentor_personality_banner(message: str) -> HtmlFragment:
    return _fragment(f"""
    <div style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); border-left: 5px solid #3B82F6; padding: 18px 24px; border-radius: 18px; margin-bottom: 20px; box-shadow: 0 12px 28px rgba(15, 23, 42, 0.15); backdrop-filter: blur(14px);">
        <div style="display: flex; align-items: center; gap: 14px;">
            <span style="font-size: 1.8rem; background: rgba(59, 130, 246, 0.2); border-radius: 50%; width: 46px; height: 46px; display: grid; place-items: center;">🧠</span>
            <div>
                <span style="color: #93C5FD; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;">Nova AI Mentor Intelligence</span>
                <div style="color: #FFFFFF; font-size: 1.15rem; font-weight: 800; margin-top: 2px;">"{html.escape(message)}"</div>
            </div>
        </div>
    </div>
    """)


def latest_achievement_single_card(title: str, description: str, level: str = "gold") -> HtmlFragment:
    return _fragment(f"""
    <div class="achievement-card unlocked {html.escape(level)}" style="margin-top: 0.5rem;">
        <div class="achievement-icon {html.escape(level)}">🏆</div>
        <div>
            <div class="achievement-title">{html.escape(title)}</div>
            <div class="achievement-copy">{html.escape(description)}</div>
            <div class="achievement-state">✅ Most Recent Unlock</div>
        </div>
    </div>
    """)


def revision_5level_target_card(target: dict) -> HtmlFragment:
    s = html.escape(str(target.get("level1_subject", "Polity")))
    t = html.escape(str(target.get("level2_topic", "Fundamental Rights")))
    r = html.escape(str(target.get("level3_repository", "Hard Repository")))
    q = html.escape(str(target.get("level4_question_type", "Assertion & Reason")))
    est = html.escape(str(target.get("estimated_time_mins", 12)))
    status = html.escape(str(target.get("status", "Due Today")))
    acc = target.get("accuracy", 50)

    return _fragment(f"""
    <div class="nova-glass-card" style="border-left: 5px solid #2563EB; background: linear-gradient(135deg, rgba(239, 246, 255, 0.95) 0%, rgba(255, 255, 255, 0.88) 100%); padding: 20px;">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; margin-bottom: 12px; gap: 8px;">
            <span style="background: rgba(37, 99, 235, 0.12); color: #1D4ED8; font-size: 0.78rem; font-weight: 850; padding: 4px 10px; border-radius: 999px;">
                🎯 5-Level Target • {status}
            </span>
            <span style="color: #475569; font-size: 0.85rem; font-weight: 800;">
                ⏱️ Estimated {est} mins
            </span>
        </div>
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 8px; font-size: 1.05rem; font-weight: 900; color: #0F172A; margin: 8px 0 14px;">
            <span>{s}</span>
            <span style="color: #2563EB;">↓</span>
            <span>{t}</span>
            <span style="color: #2563EB;">↓</span>
            <span>{r}</span>
            <span style="color: #2563EB;">↓</span>
            <span style="background: #2563EB; color: white; padding: 2px 10px; border-radius: 8px;">{q}</span>
        </div>
        <div style="color: #64748B; font-size: 0.88rem; font-weight: 750;">
            📊 Current Sub-Repository Accuracy: <strong style="color: #0F172A;">{acc}%</strong>
        </div>
    </div>
    """)


def revision_progress_card(completed: int, remaining: int, percentage: int) -> HtmlFragment:
    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-weight: 850; color: #0F172A; font-size: 0.95rem;">📊 Daily Revision Progress</span>
            <span style="background: #DCFCE7; color: #15803D; font-weight: 850; font-size: 0.85rem; padding: 4px 12px; border-radius: 12px;">
                {percentage}% Completed
            </span>
        </div>
        <div style="width: 100%; background: #E2E8F0; height: 10px; border-radius: 5px; overflow: hidden; margin-bottom: 12px;">
            <div style="width: {percentage}%; background: linear-gradient(90deg, #2563EB, #16A34A); height: 100%; transition: width 0.4s ease;"></div>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.88rem; font-weight: 750; color: #475569;">
            <span>✅ Completed Today: <strong>{completed}</strong></span>
            <span>⏳ Remaining: <strong>{remaining}</strong></span>
        </div>
    </div>
    """)


def learning_dna_grid(dna: dict) -> HtmlFragment:
    dimensions = [
        ("Knowledge", dna.get("knowledge", 5), "🧠"),
        ("Memory", dna.get("memory", 4), "💡"),
        ("Application", dna.get("application", 2), "⚙️"),
        ("Analysis", dna.get("analysis", 1), "🔍"),
        ("Speed", dna.get("speed", 4), "⚡"),
        ("Accuracy", dna.get("accuracy", 3), "🎯"),
        ("Consistency", dna.get("consistency", 5), "🔥"),
        ("Revision Habit", dna.get("revision", 4), "📅"),
    ]

    cards_html = ""
    for label, stars, icon in dimensions:
        star_str = "★" * stars + "☆" * (5 - stars)
        cards_html += f"""
        <div style="background: rgba(248, 250, 252, 0.88); border: 1px solid #E2E8F0; border-radius: 14px; padding: 12px; text-align: center;">
            <div style="font-size: 1.3rem; margin-bottom: 2px;">{icon}</div>
            <div style="color: #475569; font-size: 0.78rem; font-weight: 800; text-transform: uppercase;">{html.escape(label)}</div>
            <div style="color: #F59E0B; font-size: 1.05rem; font-weight: 900; margin-top: 4px;">{star_str}</div>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px; display: flex; align-items: center; gap: 8px;">
            <span>🧬 Learning DNA Profile</span>
            <span style="font-size: 0.78rem; background: rgba(59, 130, 246, 0.12); color: #2563EB; padding: 2px 8px; border-radius: 999px; font-weight: 800;">8 Dimensions</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;">
            {cards_html}
        </div>
    </div>
    """)


def root_cause_bottleneck_card(root_cause: str, explanation: str, bottleneck: str) -> HtmlFragment:
    rc = html.escape(str(root_cause))
    exp = html.escape(str(explanation))
    btn = html.escape(str(bottleneck))

    return _fragment(f"""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px;">
        <div class="nova-glass-card" style="border-left: 5px solid #EF4444; padding: 20px;">
            <div style="color: #DC2626; font-size: 0.78rem; font-weight: 850; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">
                🔍 Root Cause Detected
            </div>
            <div style="color: #0F172A; font-size: 1.35rem; font-weight: 950; margin-bottom: 8px;">
                {rc}
            </div>
            <div style="color: #475569; font-size: 0.9rem; line-height: 1.5; font-weight: 700;">
                {exp}
            </div>
        </div>
        <div class="nova-glass-card" style="border-left: 5px solid #F59E0B; padding: 20px;">
            <div style="color: #D97706; font-size: 0.78rem; font-weight: 850; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">
                ⚠️ Current Learning Bottleneck
            </div>
            <div style="color: #0F172A; font-size: 1.05rem; font-weight: 900; line-height: 1.4; margin-bottom: 8px; background: rgba(245, 158, 11, 0.1); padding: 8px 12px; border-radius: 10px; border: 1px solid rgba(245, 158, 11, 0.3);">
                {btn}
            </div>
            <div style="color: #64748B; font-size: 0.85rem; font-weight: 750;">
                The single largest obstacle preventing Topic Mastery.
            </div>
        </div>
    </div>
    """)


def recovery_plan_timeline(steps: list, estimated_sessions: str) -> HtmlFragment:
    steps_html = ""
    for idx, s in enumerate(steps, 1):
        steps_html += f"""
        <div style="display: flex; align-items: center; gap: 12px; padding: 10px 14px; background: rgba(248, 250, 252, 0.9); border: 1px solid #E2E8F0; border-radius: 12px; margin-bottom: 8px;">
            <span style="background: #2563EB; color: white; border-radius: 50%; width: 26px; height: 26px; display: grid; place-items: center; font-size: 0.82rem; font-weight: 900; flex-shrink: 0;">{idx}</span>
            <span style="color: #0F172A; font-weight: 850; font-size: 0.92rem;">{html.escape(s)}</span>
        </div>
        """

    est = html.escape(str(estimated_sessions))
    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
            <span style="font-size: 1.05rem; font-weight: 900; color: #0F172A;">🛠️ Actionable Recovery Plan</span>
            <span style="background: #DBEAFE; color: #1E40AF; font-size: 0.82rem; font-weight: 850; padding: 4px 12px; border-radius: 999px;">
                ⏱️ Estimated: {est}
            </span>
        </div>
        <div>
            {steps_html}
        </div>
    </div>
    """)


def mastery_probability_ring(current_pct: float, projected_pct: float) -> HtmlFragment:
    c = round(current_pct, 1)
    p = round(projected_pct, 1)

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; text-align: center;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px;">
            📈 Projected Topic Mastery Probability
        </div>
        <div style="display: flex; justify-content: center; align-items: center; gap: 24px; flex-wrap: wrap;">
            <div>
                <div style="color: #64748B; font-size: 0.8rem; font-weight: 800; text-transform: uppercase;">Current Mastery</div>
                <div style="color: #0F172A; font-size: 2rem; font-weight: 950; margin-top: 2px;">{c}%</div>
            </div>
            <div style="font-size: 1.8rem; color: #2563EB; font-weight: 900;">➜</div>
            <div>
                <div style="color: #166534; font-size: 0.8rem; font-weight: 800; text-transform: uppercase;">Expected Mastery</div>
                <div style="color: #16A34A; font-size: 2.2rem; font-weight: 950; margin-top: 2px;">{p}%</div>
            </div>
        </div>
        <div style="color: #64748B; font-size: 0.85rem; font-weight: 750; margin-top: 12px; background: rgba(34, 197, 94, 0.08); padding: 8px; border-radius: 8px; border: 1px solid rgba(34, 197, 94, 0.2);">
            🎯 Completing the recommended recovery plan is expected to increase Topic Mastery to <strong>{p}%</strong>.
        </div>
    </div>
    """)



