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
