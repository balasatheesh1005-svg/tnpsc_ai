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


def planner_task_card_html(task_item: dict) -> HtmlFragment:
    """Render glass card for an individual Study Planner task."""
    p_num = task_item.get("priority", 1)
    p_label = html.escape(str(task_item.get("priority_label", "Critical")))
    task_name = html.escape(str(task_item.get("task", "Study Task")))
    subject = html.escape(str(task_item.get("subject", "General")))
    topic = html.escape(str(task_item.get("topic", "General")))
    repo = html.escape(str(task_item.get("repository", "Standard")))
    qtype = html.escape(str(task_item.get("question_type", "MCQ")))
    duration = int(task_item.get("duration", 15))
    reason = html.escape(str(task_item.get("reason", "Learning Need")))
    benefit = html.escape(str(task_item.get("expected_benefit", "Improve Mastery")))
    reward = html.escape(str(task_item.get("reward", "+25 XP")))

    badge_bg = "#EF4444" if p_num == 1 else ("#F97316" if p_num == 2 else ("#3B82F6" if p_num <= 4 else "#10B981"))

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 18px; margin-bottom: 14px; border-left: 5px solid {badge_bg};">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background: {badge_bg}; color: white; font-size: 0.78rem; font-weight: 900; padding: 4px 10px; border-radius: 999px; text-transform: uppercase;">
                    Priority #{p_num} • {p_label}
                </span>
                <span style="color: #0F172A; font-weight: 900; font-size: 1.05rem;">
                    {task_name}
                </span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background: rgba(37, 99, 235, 0.1); color: #2563EB; font-size: 0.85rem; font-weight: 850; padding: 4px 10px; border-radius: 8px;">
                    ⏱️ {duration} Mins
                </span>
                <span style="background: rgba(245, 158, 11, 0.12); color: #D97706; font-size: 0.85rem; font-weight: 900; padding: 4px 10px; border-radius: 8px;">
                    🏆 {reward}
                </span>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; background: rgba(248, 250, 252, 0.85); padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0; margin-bottom: 10px;">
            <div>
                <span style="color: #64748B; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; display: block;">Subject & Topic</span>
                <span style="color: #0F172A; font-weight: 850; font-size: 0.9rem;">{subject} → {topic}</span>
            </div>
            <div>
                <span style="color: #64748B; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; display: block;">Repository & Pattern</span>
                <span style="color: #0F172A; font-weight: 850; font-size: 0.9rem;">{repo} ({qtype})</span>
            </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; font-size: 0.85rem;">
            <div style="color: #475569; font-weight: 750;">
                💡 <strong>Reason:</strong> {reason}
            </div>
            <div style="color: #166534; font-weight: 800; background: rgba(34, 197, 94, 0.08); padding: 4px 10px; border-radius: 6px; border: 1px solid rgba(34, 197, 94, 0.2);">
                📈 <strong>Expected Benefit:</strong> {benefit}
            </div>
        </div>
    </div>
    """)


def planner_sequence_timeline_html(sequence_items: list) -> HtmlFragment:
    """Render step-by-step visual timeline for Study Sequence."""
    steps_markup = ""
    for item in sequence_items:
        step_num = item.get("step", 1)
        action = html.escape(str(item.get("action", "Task")))
        subj = html.escape(str(item.get("subject", "")))
        top = html.escape(str(item.get("topic", "")))
        repo = html.escape(str(item.get("repository", "")))
        qtype = html.escape(str(item.get("question_type", "")))
        dur = html.escape(str(item.get("duration_str", f"{item.get('duration', 15)} Mins")))
        reward = html.escape(str(item.get("reward", "+25 XP")))

        steps_markup += f"""
        <div style="display: flex; align-items: flex-start; gap: 14px; position: relative; padding-bottom: 16px;">
            <div style="background: linear-gradient(135deg, #2563EB, #1D4ED8); color: white; border-radius: 50%; width: 32px; height: 32px; display: grid; place-items: center; font-size: 0.9rem; font-weight: 900; flex-shrink: 0; box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);">
                {step_num}
            </div>
            <div style="flex: 1; background: rgba(255, 255, 255, 0.85); border: 1px solid #E2E8F0; border-radius: 14px; padding: 12px 16px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px;">
                    <span style="color: #0F172A; font-weight: 900; font-size: 0.98rem;">{action}</span>
                    <span style="background: rgba(37, 99, 235, 0.08); color: #2563EB; font-weight: 850; font-size: 0.8rem; padding: 2px 8px; border-radius: 6px;">⏱️ {dur}</span>
                </div>
                <div style="color: #64748B; font-size: 0.85rem; font-weight: 750; margin-top: 4px;">
                    {subj} → {top} <span style="color: #94A3B8;">|</span> {repo} ({qtype})
                </div>
            </div>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 16px;">
            📅 Study Sequence Timeline
        </div>
        <div style="position: relative;">
            {steps_markup}
        </div>
    </div>
    """)


def recommendation_hero_card_html(rec_data: dict) -> HtmlFragment:
    """Render prominent Hero glass card for Primary Recommendation."""
    primary = html.escape(str(rec_data.get("recommendation", "Revise Key Concepts")))
    priority = html.escape(str(rec_data.get("priority", "Critical")))
    subject = html.escape(str(rec_data.get("subject", "General")))
    topic = html.escape(str(rec_data.get("topic", "General")))
    repo = html.escape(str(rec_data.get("repository", "Hard Repository")))
    qtype = html.escape(str(rec_data.get("question_type", "Assertion & Reason")))
    confidence = int(rec_data.get("confidence", 94))
    conf_reason = html.escape(str(rec_data.get("confidence_reason", "Engine calculation aligned")))

    priority_bg = "#EF4444" if priority == "Critical" else ("#F97316" if priority == "High" else "#2563EB")

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 24px; background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(239, 246, 255, 0.95)); border: 1px solid rgba(37, 99, 235, 0.3); border-left: 6px solid {priority_bg}; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="background: {priority_bg}; color: white; font-size: 0.8rem; font-weight: 900; padding: 4px 12px; border-radius: 999px; text-transform: uppercase;">
                    ⭐ Primary Recommendation • {priority} Priority
                </span>
            </div>
            <div style="background: rgba(37, 99, 235, 0.1); color: #2563EB; font-size: 0.88rem; font-weight: 900; padding: 6px 14px; border-radius: 999px; border: 1px solid rgba(37, 99, 235, 0.2);">
                🎯 {confidence}% AI Confidence
            </div>
        </div>

        <div style="color: #0F172A; font-size: 1.4rem; font-weight: 950; line-height: 1.3; margin-bottom: 14px;">
            {primary}
        </div>

        <div style="display: flex; gap: 10px; flex-wrap: wrap; background: rgba(248, 250, 252, 0.9); padding: 12px 16px; border-radius: 14px; border: 1px solid #E2E8F0; margin-bottom: 12px;">
            <div style="flex: 1; min-width: 150px;">
                <span style="color: #64748B; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; display: block;">Subject & Topic</span>
                <span style="color: #0F172A; font-weight: 850; font-size: 0.92rem;">{subject} → {topic}</span>
            </div>
            <div style="flex: 1; min-width: 150px;">
                <span style="color: #64748B; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; display: block;">Target Repository</span>
                <span style="color: #0F172A; font-weight: 850; font-size: 0.92rem;">{repo} ({qtype})</span>
            </div>
        </div>

        <div style="color: #64748B; font-size: 0.82rem; font-weight: 750;">
            ℹ️ <strong>Confidence Detail:</strong> {conf_reason}
        </div>
    </div>
    """)


def recommendation_risk_alert_html(rec_data: dict) -> HtmlFragment:
    """Render Risk Alert Indicator card."""
    risk = html.escape(str(rec_data.get("risk", "Optimal Progress")))
    level = html.escape(str(rec_data.get("risk_level", "Low")))
    desc = html.escape(str(rec_data.get("risk_description", "No active learning risks.")))

    if level == "Critical":
        bg_color = "linear-gradient(135deg, rgba(254, 242, 242, 0.95), rgba(254, 226, 226, 0.95))"
        border_color = "rgba(239, 68, 68, 0.4)"
        text_color = "#991B1B"
        badge_bg = "#EF4444"
        icon = "⚠️"
    elif level == "High":
        bg_color = "linear-gradient(135deg, rgba(255, 251, 235, 0.95), rgba(254, 243, 199, 0.95))"
        border_color = "rgba(245, 158, 11, 0.4)"
        text_color = "#92400E"
        badge_bg = "#F97316"
        icon = "⚡"
    elif level == "Medium":
        bg_color = "linear-gradient(135deg, rgba(239, 246, 255, 0.95), rgba(219, 234, 254, 0.95))"
        border_color = "rgba(59, 130, 246, 0.4)"
        text_color = "#1E40AF"
        badge_bg = "#3B82F6"
        icon = "ℹ️"
    else:
        bg_color = "linear-gradient(135deg, rgba(240, 253, 244, 0.95), rgba(220, 252, 231, 0.95))"
        border_color = "rgba(34, 197, 94, 0.4)"
        text_color = "#166534"
        badge_bg = "#10B981"
        icon = "✅"

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; background: {bg_color}; border: 1px solid {border_color};">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <div style="color: {text_color}; font-size: 0.8rem; font-weight: 900; text-transform: uppercase;">
                {icon} Risk Detection System
            </div>
            <span style="background: {badge_bg}; color: white; font-size: 0.75rem; font-weight: 900; padding: 2px 10px; border-radius: 999px; text-transform: uppercase;">
                {level} Risk
            </span>
        </div>
        <div style="color: #0F172A; font-size: 1.1rem; font-weight: 900; margin-bottom: 4px;">
            {risk}
        </div>
        <div style="color: #475569; font-size: 0.88rem; font-weight: 750;">
            {desc}
        </div>
    </div>
    """)


def readiness_hero_card_html(readiness_data: dict) -> HtmlFragment:
    """Render Hero Card with Circular Readiness Ring and Classification Level."""
    score = int(readiness_data.get("overall_readiness", 74))
    level = html.escape(str(readiness_data.get("level", "Exam Ready")))
    reason = html.escape(str(readiness_data.get("readiness_reason", "")))

    if score >= 90:
        ring_color = "#10B981"
        badge_bg = "#10B981"
    elif score >= 76:
        ring_color = "#2563EB"
        badge_bg = "#2563EB"
    elif score >= 51:
        ring_color = "#0284C7"
        badge_bg = "#0284C7"
    elif score >= 26:
        ring_color = "#F97316"
        badge_bg = "#F97316"
    else:
        ring_color = "#EF4444"
        badge_bg = "#EF4444"

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 24px; margin-bottom: 20px; background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 249, 255, 0.95)); border: 1px solid rgba(2, 132, 199, 0.3);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div style="flex: 1; min-width: 220px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: {badge_bg}; color: white; font-size: 0.8rem; font-weight: 900; padding: 4px 12px; border-radius: 999px; text-transform: uppercase;">
                        🎯 Level: {level}
                    </span>
                    <span style="color: #64748B; font-size: 0.78rem; font-weight: 800;">
                        Current Preparation Level
                    </span>
                </div>
                <div style="color: #0F172A; font-size: 1.5rem; font-weight: 950; line-height: 1.3; margin-bottom: 8px;">
                    Overall Exam Readiness Score
                </div>
                <div style="color: #475569; font-size: 0.88rem; font-weight: 750; line-height: 1.4;">
                    Evaluated deterministically across Topic Mastery, Repository Depth, Revision Health, Consistency, and PYQ readiness.
                </div>
            </div>

            <div style="text-align: center; background: rgba(255, 255, 255, 0.9); padding: 18px 24px; border-radius: 20px; border: 2px solid {ring_color}; box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06); min-width: 140px;">
                <div style="color: {ring_color}; font-size: 3.2rem; font-weight: 950; line-height: 1;">
                    {score}%
                </div>
                <div style="color: #64748B; font-size: 0.75rem; font-weight: 900; text-transform: uppercase; margin-top: 4px;">
                    Readiness Score
                </div>
            </div>
        </div>
    </div>
    """)


def subject_readiness_grid_html(subjects_list: list) -> HtmlFragment:
    """Render Subject Readiness Cards Grid."""
    cards_html = ""
    for item in subjects_list:
        subj = html.escape(str(item.get("subject", "Subject")))
        score = int(item.get("score", 50))

        bar_color = "#10B981" if score >= 80 else ("#2563EB" if score >= 65 else ("#F97316" if score >= 50 else "#EF4444"))

        cards_html += f"""
        <div style="background: rgba(255, 255, 255, 0.85); border: 1px solid #E2E8F0; border-radius: 14px; padding: 14px 16px; margin-bottom: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="color: #0F172A; font-weight: 900; font-size: 0.95rem;">{subj}</span>
                <span style="color: {bar_color}; font-weight: 950; font-size: 1rem;">{score}%</span>
            </div>
            <div style="background: #E2E8F0; border-radius: 999px; height: 8px; overflow: hidden;">
                <div style="background: {bar_color}; width: {score}%; height: 100%; border-radius: 999px;"></div>
            </div>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px;">
            📚 Subject-wise Preparation Readiness
        </div>
        <div>
            {cards_html}
        </div>
    </div>
    """)


def strengths_improvements_card_html(strengths: list, improvements: list) -> HtmlFragment:
    """Render Dual Badge Card for Strengths & Priority Improvements."""
    str_markup = ""
    for s in strengths:
        str_markup += f"""
        <div style="display: flex; align-items: center; gap: 8px; background: rgba(34, 197, 94, 0.08); color: #166534; border: 1px solid rgba(34, 197, 94, 0.2); padding: 8px 12px; border-radius: 10px; font-weight: 850; font-size: 0.85rem; margin-bottom: 6px;">
            <span>💪</span> {html.escape(s)}
        </div>
        """

    imp_markup = ""
    for imp in improvements:
        imp_markup += f"""
        <div style="display: flex; align-items: center; gap: 8px; background: rgba(245, 158, 11, 0.08); color: #92400E; border: 1px solid rgba(245, 158, 11, 0.2); padding: 8px 12px; border-radius: 10px; font-weight: 850; font-size: 0.85rem; margin-bottom: 6px;">
            <span>⚠️</span> {html.escape(imp)}
        </div>
        """

    return _fragment(f"""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
        <div class="nova-glass-card" style="padding: 20px;">
            <div style="font-size: 1.02rem; font-weight: 900; color: #166534; margin-bottom: 12px;">
                💪 Identified Preparation Strengths
            </div>
            <div>
                {str_markup}
            </div>
        </div>

        <div class="nova-glass-card" style="padding: 20px;">
            <div style="font-size: 1.02rem; font-weight: 900; color: #92400E; margin-bottom: 12px;">
                ⚠️ Priority Improvement Directives
            </div>
            <div>
                {imp_markup}
            </div>
        </div>
    </div>
    """)


def mock_hero_card_html(mock_data: dict) -> HtmlFragment:
    """Render Mock Hero Card with Accuracy Ring and Attempt Ratio Bar."""
    acc = int(mock_data.get("overall_accuracy", 74))
    level = html.escape(str(mock_data.get("mock_level", "Good")))
    ratio = mock_data.get("correct_vs_wrong", {})
    c_pct = int(ratio.get("correct", acc))
    w_pct = int(ratio.get("wrong", 14))
    s_pct = int(ratio.get("skipped", 12))
    att_rate = int(mock_data.get("attempt_rate", 88))

    ring_color = "#10B981" if acc >= 85 else ("#2563EB" if acc >= 75 else ("#F97316" if acc >= 60 else "#EF4444"))

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 24px; margin-bottom: 20px; background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(243, 244, 246, 0.95)); border: 1px solid rgba(107, 114, 128, 0.3);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div style="flex: 1; min-width: 240px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: {ring_color}; color: white; font-size: 0.8rem; font-weight: 900; padding: 4px 12px; border-radius: 999px; text-transform: uppercase;">
                        🎯 Mock Performance: {level}
                    </span>
                    <span style="color: #64748B; font-size: 0.78rem; font-weight: 800;">
                        {att_rate}% Attempt Rate
                    </span>
                </div>
                <div style="color: #0F172A; font-size: 1.5rem; font-weight: 950; line-height: 1.3; margin-bottom: 12px;">
                    Observed Mock Exam Performance
                </div>

                <div style="background: rgba(248, 250, 252, 0.9); padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.78rem; font-weight: 850; margin-bottom: 6px;">
                        <span style="color: #16A34A;">✓ Correct: {c_pct}%</span>
                        <span style="color: #DC2626;">✗ Wrong: {w_pct}%</span>
                        <span style="color: #64748B;">⊘ Skipped: {s_pct}%</span>
                    </div>
                    <div style="display: flex; height: 10px; border-radius: 999px; overflow: hidden; background: #E2E8F0;">
                        <div style="background: #16A34A; width: {c_pct}%;"></div>
                        <div style="background: #DC2626; width: {w_pct}%;"></div>
                        <div style="background: #94A3B8; width: {s_pct}%;"></div>
                    </div>
                </div>
            </div>

            <div style="text-align: center; background: rgba(255, 255, 255, 0.9); padding: 18px 24px; border-radius: 20px; border: 2px solid {ring_color}; box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06); min-width: 140px;">
                <div style="color: {ring_color}; font-size: 3.2rem; font-weight: 950; line-height: 1;">
                    {acc}%
                </div>
                <div style="color: #64748B; font-size: 0.75rem; font-weight: 900; text-transform: uppercase; margin-top: 4px;">
                    Mock Accuracy
                </div>
            </div>
        </div>
    </div>
    """)


def mock_time_analysis_card_html(mock_data: dict) -> HtmlFragment:
    """Render Time Management Analysis Card."""
    avg_time = int(mock_data.get("time_per_question", 58))
    analysis = html.escape(str(mock_data.get("time_analysis", "")))
    slowest = html.escape(str(mock_data.get("slowest_section", "Economy")))

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; background: linear-gradient(135deg, rgba(239, 246, 255, 0.95), rgba(255, 251, 235, 0.95)); border: 1px solid rgba(245, 158, 11, 0.3);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A;">
                ⏱️ Time Management Analysis
            </div>
            <span style="background: rgba(37, 99, 235, 0.1); color: #2563EB; font-size: 0.82rem; font-weight: 850; padding: 4px 12px; border-radius: 999px;">
                Avg {avg_time} sec / Question
            </span>
        </div>
        <div style="color: #334155; font-size: 0.92rem; font-weight: 750; line-height: 1.4; background: rgba(255, 255, 255, 0.85); padding: 12px 16px; border-radius: 12px; border: 1px solid #E2E8F0;">
            💡 {analysis}
        </div>
    </div>
    """)


def mock_qtype_performance_html(qtypes_list: list) -> HtmlFragment:
    """Render Question Type Performance Cards Grid."""
    cards_html = ""
    for item in qtypes_list:
        q_label = html.escape(str(item.get("type", "Question Type")))
        score = int(item.get("accuracy", 60))

        bar_color = "#10B981" if score >= 75 else ("#2563EB" if score >= 65 else ("#F97316" if score >= 55 else "#EF4444"))

        cards_html += f"""
        <div style="background: rgba(255, 255, 255, 0.85); border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 14px; margin-bottom: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="color: #0F172A; font-weight: 850; font-size: 0.9rem;">{q_label}</span>
                <span style="color: {bar_color}; font-weight: 950; font-size: 0.95rem;">{score}%</span>
            </div>
            <div style="background: #E2E8F0; border-radius: 999px; height: 6px; overflow: hidden;">
                <div style="background: {bar_color}; width: {score}%; height: 100%; border-radius: 999px;"></div>
            </div>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px;">
            📝 Question Type Behavioral Performance
        </div>
        <div>
            {cards_html}
        </div>
    </div>
    """)


def mock_mistakes_strengths_html(mistakes: list, strengths: list) -> HtmlFragment:
    """Render Dual Badge Card for Mistake Patterns vs Strengths."""
    m_markup = ""
    for m in mistakes:
        m_markup += f"""
        <div style="display: flex; align-items: center; gap: 8px; background: rgba(239, 68, 68, 0.08); color: #B91C1C; border: 1px solid rgba(239, 68, 68, 0.2); padding: 8px 12px; border-radius: 10px; font-weight: 850; font-size: 0.85rem; margin-bottom: 6px;">
            <span>⚠</span> {html.escape(m)}
        </div>
        """

    s_markup = ""
    for s in strengths:
        s_markup += f"""
        <div style="display: flex; align-items: center; gap: 8px; background: rgba(34, 197, 94, 0.08); color: #166534; border: 1px solid rgba(34, 197, 94, 0.2); padding: 8px 12px; border-radius: 10px; font-weight: 850; font-size: 0.85rem; margin-bottom: 6px;">
            <span>💪</span> {html.escape(s)}
        </div>
        """

    return _fragment(f"""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
        <div class="nova-glass-card" style="padding: 20px;">
            <div style="font-size: 1.02rem; font-weight: 900; color: #B91C1C; margin-bottom: 12px;">
                ⚠ Detected Mistake Patterns & Weak Habits
            </div>
            <div>
                {m_markup}
            </div>
        </div>

        <div class="nova-glass-card" style="padding: 20px;">
            <div style="font-size: 1.02rem; font-weight: 900; color: #166534; margin-bottom: 12px;">
                💪 Observed Exam Strengths
            </div>
            <div>
                {s_markup}
            </div>
        </div>
    </div>
    """)


# ================= PREDICTIVE PERFORMANCE ENGINE V2 CARDS =================

def predictive_hero_card_html(pred_data: dict) -> HtmlFragment:
    """Render Master Hero Card for Predictive Performance V2."""
    readiness_range = html.escape(str(pred_data.get("estimated_readiness", "75–79%")))
    mock_range = html.escape(str(pred_data.get("estimated_mock_accuracy", "76–80%")))
    curr_readiness = int(pred_data.get("current_readiness", 72))
    curr_mock = int(pred_data.get("current_mock_accuracy", 74))
    confidence = int(pred_data.get("prediction_confidence", 92))
    trend = html.escape(str(pred_data.get("readiness_trend", "Improving")))

    conf_bg = "#10B981" if confidence >= 85 else ("#2563EB" if confidence >= 70 else "#F97316")

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 24px; margin-bottom: 20px; background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 58, 138, 0.95)); border: 1px solid rgba(147, 197, 253, 0.3); color: white;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div style="flex: 1; min-width: 260px;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                    <span style="background: rgba(59, 130, 246, 0.25); color: #93C5FD; border: 1px solid rgba(147, 197, 253, 0.4); font-size: 0.78rem; font-weight: 900; padding: 4px 12px; border-radius: 999px; text-transform: uppercase;">
                        🔮 Future Outcome Projections
                    </span>
                    <span style="background: {conf_bg}; color: white; font-size: 0.78rem; font-weight: 900; padding: 4px 12px; border-radius: 999px;">
                        🎯 {confidence}% Confidence
                    </span>
                </div>
                <div style="color: white; font-size: 1.6rem; font-weight: 950; line-height: 1.3; margin-bottom: 6px;">
                    Predictive Performance Engine V2
                </div>
                <p style="color: #CBD5E1; font-size: 0.88rem; margin: 0; font-weight: 600;">
                    Single projection authority for TNPSC Nova AI • Estimating future readiness & mock trends using rule-based learning signals.
                </p>
            </div>

            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                <div style="text-align: center; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 14px 20px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.15); min-width: 130px;">
                    <div style="color: #93C5FD; font-size: 0.75rem; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">
                        Current Readiness
                    </div>
                    <div style="color: white; font-size: 1.8rem; font-weight: 950; line-height: 1;">
                        {curr_readiness}%
                    </div>
                    <div style="color: #34D399; font-size: 0.85rem; font-weight: 900; margin-top: 6px;">
                        ➔ {readiness_range}
                    </div>
                </div>

                <div style="text-align: center; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 14px 20px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.15); min-width: 130px;">
                    <div style="color: #93C5FD; font-size: 0.75rem; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">
                        Next Mock Acc.
                    </div>
                    <div style="color: white; font-size: 1.8rem; font-weight: 950; line-height: 1;">
                        {curr_mock}%
                    </div>
                    <div style="color: #60A5FA; font-size: 0.85rem; font-weight: 900; margin-top: 6px;">
                        ➔ {mock_range}
                    </div>
                </div>
            </div>
        </div>
    </div>
    """)


def predictive_comparison_cards_html(pred_data: dict) -> HtmlFragment:
    """Render 6 Side-by-Side Current vs Estimated Comparison Cards."""
    dims = pred_data.get("dimensions", {})
    cards_markup = ""

    icons = {
        "readiness": "📚",
        "mock_accuracy": "📝",
        "topic_mastery": "🎯",
        "revision_health": "🔄",
        "consistency": "📅",
        "repo_completion": "📂",
    }

    for key, d in dims.items():
        name = html.escape(str(d.get("name", key)))
        curr = int(d.get("current", 70))
        est_range = html.escape(str(d.get("estimated_range", "72-76%")))
        trend = html.escape(str(d.get("trend", "Improving")))
        icon = icons.get(key, "📊")

        t_color = "#10B981" if trend == "Improving" else ("#2563EB" if trend == "Stable" else "#F97316")

        cards_markup += f"""
        <div class="nova-glass-card" style="padding: 16px; border-radius: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">{icon} {name}</span>
                <span style="background: rgba(16, 185, 129, 0.12); color: {t_color}; font-size: 0.72rem; font-weight: 900; padding: 2px 8px; border-radius: 999px;">
                    {trend}
                </span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-top: 10px;">
                <div>
                    <div style="font-size: 0.72rem; color: #64748B; font-weight: 800; text-transform: uppercase;">Current</div>
                    <div style="font-size: 1.4rem; font-weight: 950; color: #0F172A;">{curr}%</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 0.72rem; color: #2563EB; font-weight: 850; text-transform: uppercase;">Projected</div>
                    <div style="font-size: 1.4rem; font-weight: 950; color: #2563EB;">{est_range}</div>
                </div>
            </div>
            <div style="background: #E2E8F0; border-radius: 999px; height: 6px; margin-top: 10px; overflow: hidden;">
                <div style="background: linear-gradient(90deg, #2563EB, #10B981); width: {curr}%; height: 100%; border-radius: 999px;"></div>
            </div>
        </div>
        """

    return _fragment(f"""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px;">
        {cards_markup}
    </div>
    """)


def predictive_confidence_card_html(pred_data: dict) -> HtmlFragment:
    """Render Prediction Confidence Meter & Rationale Card."""
    confidence = int(pred_data.get("prediction_confidence", 92))
    reason = html.escape(str(pred_data.get("confidence_reason", "Sufficient learning data.")))

    c_color = "#10B981" if confidence >= 85 else ("#2563EB" if confidence >= 70 else "#F97316")

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A;">
                🎯 Prediction Confidence Score
            </div>
            <span style="background: {c_color}; color: white; font-size: 0.85rem; font-weight: 900; padding: 4px 12px; border-radius: 999px;">
                {confidence}% Confidence
            </span>
        </div>

        <div style="background: #F1F5F9; border-radius: 999px; height: 12px; overflow: hidden; margin-bottom: 12px;">
            <div style="background: {c_color}; width: {confidence}%; height: 100%; border-radius: 999px; transition: width 0.5s ease;"></div>
        </div>

        <div style="background: rgba(248, 250, 252, 0.9); border: 1px solid #E2E8F0; padding: 12px 14px; border-radius: 12px; color: #334155; font-size: 0.88rem; font-weight: 700;">
            <span style="font-weight: 900; color: #0F172A;">Rationale:</span> {reason}
        </div>
    </div>
    """)


def predictive_explanation_card_html(pred_data: dict) -> HtmlFragment:
    """Render 'Why This Projection?' Rationale & Safety Policy Card."""
    bullets = pred_data.get("explanation_bullets", [])
    reason = html.escape(str(pred_data.get("prediction_reason", "")))
    projection = html.escape(str(pred_data.get("mentor_projection", "")))

    bullet_markup = ""
    for b in bullets:
        bullet_markup += f"""
        <div style="display: flex; align-items: flex-start; gap: 8px; margin-bottom: 6px; font-size: 0.88rem; color: #334155; font-weight: 700;">
            <span style="color: #2563EB; font-weight: 900;">•</span>
            <span>{html.escape(b)}</span>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
        <div style="font-size: 1.08rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
            📖 Why This Projection? (Engine Rationale)
        </div>

        <div style="background: #EFF6FF; border-left: 4px solid #2563EB; padding: 12px 16px; border-radius: 8px; margin-bottom: 14px; color: #1E40AF; font-size: 0.9rem; font-weight: 800;">
            {reason}
        </div>

        <div style="margin-bottom: 14px;">
            <div style="font-size: 0.85rem; font-weight: 900; color: #475569; text-transform: uppercase; margin-bottom: 8px;">
                Key Learning Factors Evaluated:
            </div>
            {bullet_markup}
        </div>

        <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 12px; padding: 12px 14px;">
            <div style="font-size: 0.85rem; font-weight: 900; color: #92400E; margin-bottom: 4px;">
                💡 Future AI Mentor Guidance:
            </div>
            <div style="color: #78350F; font-size: 0.88rem; font-weight: 700; line-height: 1.4;">
                {projection}
            </div>
        </div>

        <div style="color: #94A3B8; font-size: 0.76rem; font-weight: 750; margin-top: 14px; text-align: center; border-top: 1px solid #F1F5F9; padding-top: 8px;">
            ⚠ All predictions are estimates based on available learning signals. Never guarantees exam pass, score, or selection rank.
        </div>
    </div>
    """)


def adaptive_revision_hero_card_html(plan: dict) -> HtmlFragment:
    """Render Master Hero Card for Adaptive Final Revision Engine V2."""
    phase = html.escape(str(plan.get("revision_phase", "30-Day Plan")))
    days = int(plan.get("days_remaining", 30))
    daily_target = html.escape(str(plan.get("daily_target", "Revise 3 topics + 40 MCQs + 1 PYQ set")))
    est_comp = html.escape(str(plan.get("estimated_completion", "85% estimated revision completion")))

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 24px; margin-bottom: 20px; background: linear-gradient(135deg, #0F172A, #1E3A8A, #2563EB); border: 1px solid rgba(147, 197, 253, 0.3); color: white;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div style="flex: 1; min-width: 260px;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                    <span style="background: rgba(59, 130, 246, 0.25); color: #93C5FD; border: 1px solid rgba(147, 197, 253, 0.4); font-size: 0.78rem; font-weight: 900; padding: 4px 12px; border-radius: 999px; text-transform: uppercase;">
                        ⚡ Adaptive Revision Strategy V2
                    </span>
                    <span style="background: #10B981; color: white; font-size: 0.78rem; font-weight: 900; padding: 4px 12px; border-radius: 999px;">
                        📅 {phase}
                    </span>
                </div>
                <div style="color: white; font-size: 1.65rem; font-weight: 950; line-height: 1.25; margin-bottom: 6px;">
                    Single Personalized Revision Authority
                </div>
                <p style="color: #CBD5E1; font-size: 0.88rem; margin: 0; font-weight: 600;">
                    Automated, deterministic strategy generated from readiness, mock behavior, prediction trends, and revision analytics.
                </p>
            </div>

            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                <div style="text-align: center; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 14px 20px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.15); min-width: 130px;">
                    <div style="color: #93C5FD; font-size: 0.75rem; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">
                        Timeline Remaining
                    </div>
                    <div style="color: white; font-size: 1.8rem; font-weight: 950; line-height: 1;">
                        {days} Days
                    </div>
                    <div style="color: #34D399; font-size: 0.82rem; font-weight: 900; margin-top: 6px;">
                        🎯 Active Phase
                    </div>
                </div>

                <div style="text-align: center; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 14px 20px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.15); min-width: 150px;">
                    <div style="color: #93C5FD; font-size: 0.75rem; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">
                        Estimated Target
                    </div>
                    <div style="color: #60A5FA; font-size: 0.88rem; font-weight: 900; line-height: 1.3;">
                        {est_comp}
                    </div>
                </div>
            </div>
        </div>
    </div>
    """)


def adaptive_revision_priority_cards_html(plan: dict) -> HtmlFragment:
    """Render Priority Subjects & Priority Topics Cards."""
    subjects = plan.get("priority_subjects", ["Geography", "Economy", "Current Affairs"])
    topics = plan.get("priority_topics", ["Indian Economy", "Physical Geography", "Environment"])

    subj_badges = ""
    for s in subjects:
        subj_badges += f"""
        <div style="background: rgba(37, 99, 235, 0.1); border: 1px solid rgba(37, 99, 235, 0.2); border-radius: 12px; padding: 10px 14px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">🎯 {html.escape(s)}</span>
            <span style="background: #2563EB; color: white; font-size: 0.72rem; font-weight: 900; padding: 2px 10px; border-radius: 999px;">Priority Focus</span>
        </div>
        """

    topic_badges = ""
    for t in topics:
        topic_badges += f"""
        <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 12px; padding: 10px 14px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 0.92rem; font-weight: 850; color: #78350F;">📚 {html.escape(t)}</span>
            <span style="background: #F59E0B; color: white; font-size: 0.72rem; font-weight: 900; padding: 2px 10px; border-radius: 999px;">High Yield</span>
        </div>
        """

    return _fragment(f"""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin-bottom: 20px;">
        <div class="nova-glass-card" style="padding: 20px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                🎯 Priority Subjects
            </div>
            {subj_badges}
        </div>

        <div class="nova-glass-card" style="padding: 20px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                📚 Priority Topics
            </div>
            {topic_badges}
        </div>
    </div>
    """)


def adaptive_revision_order_timeline_html(plan: dict) -> HtmlFragment:
    """Render Revision Order Timeline Grid."""
    order = plan.get("revision_order", ["Economy", "Geography", "Science", "History"])

    items_html = ""
    for idx, item in enumerate(order, 1):
        items_html += f"""
        <div style="background: white; border: 1px solid #E2E8F0; border-radius: 14px; padding: 14px; text-align: center; position: relative; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);">
            <div style="background: #2563EB; color: white; width: 26px; height: 26px; border-radius: 50%; display: grid; place-items: center; font-size: 0.78rem; font-weight: 950; margin: 0 auto 8px auto;">
                {idx}
            </div>
            <div style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">{html.escape(item)}</div>
            <div style="font-size: 0.75rem; color: #64748B; font-weight: 700; margin-top: 4px;">Step {idx} Phase</div>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px;">
            🔄 Revision Order Timeline
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
            {items_html}
        </div>
    </div>
    """)


def adaptive_revision_cycles_card_html(plan: dict) -> HtmlFragment:
    """Render 4-Stage Revision Cycles Card."""
    cycles = plan.get("revision_cycles", ["Concept", "Practice", "PYQ", "Rapid Recall"])

    cycle_colors = ["#2563EB", "#0EA5E9", "#10B981", "#8B5CF6"]
    cycle_icons = ["💡", "📝", "📜", "⚡"]

    cards_html = ""
    for idx, cycle in enumerate(cycles):
        color = cycle_colors[idx % len(cycle_colors)]
        icon = cycle_icons[idx % len(cycle_icons)]
        cards_html += f"""
        <div style="background: rgba(248, 250, 252, 0.9); border-left: 4px solid {color}; border-radius: 12px; padding: 12px 14px;">
            <div style="font-size: 0.75rem; font-weight: 900; color: {color}; text-transform: uppercase;">Cycle {idx + 1}</div>
            <div style="font-size: 0.95rem; font-weight: 900; color: #0F172A; margin-top: 2px;">{icon} {html.escape(cycle)}</div>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px;">
            🔄 Structured Revision Cycles
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
            {cards_html}
        </div>
    </div>
    """)


def adaptive_revision_risk_card_html(plan: dict) -> HtmlFragment:
    """Render Revision Risk Analysis Card."""
    risks = plan.get("risk_analysis", ["Low Geography readiness", "Weak Assertion & Reason performance"])

    risk_items = ""
    for r in risks:
        risk_items += f"""
        <div style="display: flex; align-items: flex-start; gap: 10px; background: rgba(254, 242, 242, 0.8); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 12px; padding: 12px 14px; margin-bottom: 8px;">
            <span style="font-size: 1.1rem; line-height: 1;">⚠️</span>
            <div style="color: #991B1B; font-size: 0.88rem; font-weight: 750; line-height: 1.4;">
                {html.escape(r)}
            </div>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px; display: flex; align-items: center; gap: 8px;">
            ⚠ Revision Risk Analysis & Actionable Guidance
        </div>
        {risk_items}
    </div>
    """)


def adaptive_revision_mentor_card_html(plan: dict) -> HtmlFragment:
    """Render Mentor Revision Advice Card."""
    advice = html.escape(str(plan.get("mentor_advice", "Focus on Geography and Economy first.")))

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px; background: linear-gradient(135deg, rgba(255, 251, 235, 0.95), rgba(254, 243, 199, 0.95)); border: 1px solid rgba(245, 158, 11, 0.35);">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <span style="font-size: 1.4rem;">🧠</span>
            <div style="font-size: 1.05rem; font-weight: 950; color: #92400E;">
            "{advice}"
        </div>
    </div>
    """)


def exam_strategy_hero_card_html(strat: dict) -> HtmlFragment:
    """Render Master Hero Card for Exam Strategy Engine V2."""
    overall = html.escape(str(strat.get("overall_strategy", "Strength-First Execution Strategy")))
    confidence = int(strat.get("strategy_confidence", 91))
    reason = html.escape(str(strat.get("confidence_reason", "Consistent mock history & stable readiness.")))

    conf_color = "#10B981" if confidence >= 85 else ("#2563EB" if confidence >= 70 else "#F97316")

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 24px; margin-bottom: 20px; background: linear-gradient(135deg, #0F172A, #1E3A8A, #2563EB); border: 1px solid rgba(147, 197, 253, 0.3); color: white;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div style="flex: 1; min-width: 260px;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                    <span style="background: rgba(59, 130, 246, 0.25); color: #93C5FD; border: 1px solid rgba(147, 197, 253, 0.4); font-size: 0.78rem; font-weight: 900; padding: 4px 12px; border-radius: 999px; text-transform: uppercase;">
                        🎯 Exam Execution Strategy V2
                    </span>
                    <span style="background: {conf_color}; color: white; font-size: 0.78rem; font-weight: 900; padding: 4px 12px; border-radius: 999px;">
                        🎯 {confidence}% Confidence
                    </span>
                </div>
                <div style="color: white; font-size: 1.65rem; font-weight: 950; line-height: 1.25; margin-bottom: 6px;">
                    {overall}
                </div>
                <p style="color: #CBD5E1; font-size: 0.88rem; margin: 0; font-weight: 600;">
                    Single pre-exam strategy authority for TNPSC Nova AI • Personalized subject order, time allocation & skip framework.
                </p>
            </div>

            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                <div style="text-align: center; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 14px 20px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.15); min-width: 150px;">
                    <div style="color: #93C5FD; font-size: 0.75rem; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">
                        Strategy Rationale
                    </div>
                    <div style="color: white; font-size: 0.85rem; font-weight: 750; line-height: 1.35;">
                        {reason}
                    </div>
                </div>
            </div>
        </div>
    </div>
    """)


def exam_strategy_subject_flow_html(strat: dict) -> HtmlFragment:
    """Render Subject Attempt Order Flow View."""
    order = strat.get("subject_order", ["History", "Polity", "Science", "Economy", "Current Affairs"])

    flow_items = ""
    for idx, subj in enumerate(order, 1):
        arrow = '<div style="font-size: 1.2rem; font-weight: 900; color: #2563EB; margin: 0 4px;">➔</div>' if idx < len(order) else ""
        flow_items += f"""
        <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 8px;">
            <div style="background: white; border: 1px solid #E2E8F0; border-radius: 14px; padding: 10px 16px; display: flex; align-items: center; gap: 10px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);">
                <span style="background: #2563EB; color: white; width: 24px; height: 24px; border-radius: 50%; display: grid; place-items: center; font-size: 0.75rem; font-weight: 950;">
                    {idx}
                </span>
                <span style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">{html.escape(subj)}</span>
            </div>
            {arrow}
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px; display: flex; align-items: center; gap: 8px;">
            📚 Subject Attempt Order (Strength-First Sequence)
        </div>
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 8px;">
            {flow_items}
        </div>
    </div>
    """)


def exam_strategy_time_plan_html(strat: dict) -> HtmlFragment:
    """Render Section-Wise Time Allocation Progress Bars."""
    time_plan = strat.get("time_plan", [])
    total_mins = int(strat.get("dashboard_sections", {}).get("total_exam_minutes", 180))

    bars_markup = ""
    for item in time_plan:
        subj = html.escape(str(item.get("subject", "")))
        mins = int(item.get("minutes", 0))
        pct = min(100, max(5, int(round((mins / total_mins) * 100))))
        
        color = "#2563EB" if "Review" not in subj else "#10B981"

        bars_markup += f"""
        <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; font-size: 0.88rem; font-weight: 850;">
                <span style="color: #0F172A;">{subj}</span>
                <span style="color: {color}; font-weight: 950;">{mins} min ({pct}%)</span>
            </div>
            <div style="background: #E2E8F0; border-radius: 999px; height: 8px; overflow: hidden;">
                <div style="background: {color}; width: {pct}%; height: 100%; border-radius: 999px;"></div>
            </div>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A;">
                ⏱ Section-wise Time Allocation
            </div>
            <span style="background: rgba(37, 99, 235, 0.12); color: #2563EB; font-size: 0.8rem; font-weight: 900; padding: 4px 12px; border-radius: 999px;">
                Total: {total_mins} Minutes
            </span>
        </div>
        {bars_markup}
    </div>
    """)


def exam_strategy_question_rules_html(strat: dict) -> HtmlFragment:
    """Render Question Decision Rules & Skip Strategy Card."""
    q_rules = strat.get("question_strategy", [])
    skip_rules = strat.get("skip_strategy", [])
    review_rules = strat.get("review_order", [])

    q_items = ""
    for r in q_rules:
        q_items += f"""
        <div style="display: flex; align-items: flex-start; gap: 8px; margin-bottom: 6px; font-size: 0.88rem; color: #334155; font-weight: 700;">
            <span style="color: #2563EB; font-weight: 900;">•</span>
            <span>{html.escape(r)}</span>
        </div>
        """

    skip_items = ""
    for r in skip_rules:
        skip_items += f"""
        <div style="display: flex; align-items: flex-start; gap: 8px; margin-bottom: 6px; font-size: 0.88rem; color: #78350F; font-weight: 700;">
            <span style="color: #F59E0B; font-weight: 900;">•</span>
            <span>{html.escape(r)}</span>
        </div>
        """

    review_items = ""
    for idx, r in enumerate(review_rules, 1):
        review_items += f"""
        <div style="background: rgba(248, 250, 252, 0.9); border: 1px solid #E2E8F0; border-radius: 10px; padding: 8px 12px; margin-bottom: 6px; font-size: 0.85rem; font-weight: 850; color: #0F172A; display: flex; align-items: center; justify-content: space-between;">
            <span>{idx}. {html.escape(r)}</span>
            <span style="background: rgba(37, 99, 235, 0.1); color: #2563EB; font-size: 0.72rem; font-weight: 900; padding: 2px 8px; border-radius: 999px;">Priority {idx}</span>
        </div>
        """

    return _fragment(f"""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin-bottom: 20px;">
        <div class="nova-glass-card" style="padding: 20px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                📝 Question Decision Framework
            </div>
            {q_items}
        </div>

        <div class="nova-glass-card" style="padding: 20px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                ⏭ Skip & Return Strategy
            </div>
            <div style="background: rgba(254, 243, 199, 0.5); border-left: 4px solid #F59E0B; padding: 10px 14px; border-radius: 8px; margin-bottom: 10px;">
                {skip_items}
            </div>
        </div>

        <div class="nova-glass-card" style="padding: 20px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                🔄 Review Strategy Order
            </div>
            {review_items}
        </div>
    </div>
    """)


def exam_strategy_risk_card_html(strat: dict) -> HtmlFragment:
    """Render Risk Awareness Callouts Card."""
    risks = strat.get("risk_alerts", [])

    risk_items = ""
    for r in risks:
        risk_items += f"""
        <div style="display: flex; align-items: flex-start; gap: 10px; background: rgba(254, 242, 242, 0.8); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 12px; padding: 12px 14px; margin-bottom: 8px;">
            <span style="font-size: 1.1rem; line-height: 1;">⚠️</span>
            <div style="color: #991B1B; font-size: 0.88rem; font-weight: 750; line-height: 1.4;">
                {html.escape(r)}
            </div>
        </div>
        """

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
        <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px; display: flex; align-items: center; gap: 8px;">
            ⚠ Risk Awareness & Prevention
        </div>
        {risk_items}
    </div>
    """)


def exam_strategy_mentor_card_html(strat: dict) -> HtmlFragment:
    """Render Mentor Strategy Advice Card."""
    advice = html.escape(str(strat.get("mentor_strategy", "Begin with History to build momentum.")))

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px; background: linear-gradient(135deg, rgba(239, 246, 255, 0.95), rgba(219, 234, 254, 0.95)); border: 1px solid rgba(37, 99, 235, 0.35);">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <span style="font-size: 1.4rem;">🧠</span>
            <div style="font-size: 1.05rem; font-weight: 950; color: #1D4ED8;">
                AI Mentor Strategy Advice
            </div>
        </div>
        <div style="color: #1E40AF; font-size: 0.95rem; font-weight: 700; line-height: 1.55; background: rgba(255, 255, 255, 0.7); padding: 14px 16px; border-radius: 14px; border: 1px solid rgba(37, 99, 235, 0.2);">
            "{advice}"
        </div>
    </div>
    """)


def coach_hero_card_html(user_name: str, readiness_data: dict, recommendation_data: dict, streak: int) -> HtmlFragment:
    """Render Flagship Hero Card for AI Exam Coach Dashboard V2."""
    name = html.escape(str(user_name or "Aspirant"))
    score = int(readiness_data.get("overall_readiness_score", 70))
    level = html.escape(str(readiness_data.get("readiness_level", "Developing Readiness")))
    focus = html.escape(str(recommendation_data.get("recommendation", "Modern India Revision")))

    msg = f"Good day, {name}! You are currently at the {level} stage. Today's primary focus: {focus}."

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 26px; margin-bottom: 22px; background: linear-gradient(135deg, #0F172A, #1E3A8A, #2563EB); border: 1px solid rgba(147, 197, 253, 0.35); color: white; box-shadow: 0 16px 36px rgba(37, 99, 235, 0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 18px;">
            <div style="flex: 1; min-width: 280px;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                    <span style="background: rgba(59, 130, 246, 0.3); color: #93C5FD; border: 1px solid rgba(147, 197, 253, 0.4); font-size: 0.8rem; font-weight: 900; padding: 4px 14px; border-radius: 999px; text-transform: uppercase;">
                        🤖 AI Exam Coach Flagship
                    </span>
                    <span style="background: #10B981; color: white; font-size: 0.8rem; font-weight: 900; padding: 4px 14px; border-radius: 999px;">
                        🔥 {streak} Day Streak
                    </span>
                </div>
                <div style="color: white; font-size: 1.8rem; font-weight: 950; line-height: 1.25; margin-bottom: 8px;">
                    Welcome back, {name}! 👋
                </div>
                <div style="background: rgba(255, 255, 255, 0.12); backdrop-filter: blur(10px); border-left: 4px solid #60A5FA; padding: 12px 16px; border-radius: 10px; color: #E2E8F0; font-size: 0.92rem; font-weight: 700; line-height: 1.45;">
                    "{msg}"
                </div>
            </div>

            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                <div style="text-align: center; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(12px); padding: 16px 22px; border-radius: 18px; border: 1px solid rgba(255, 255, 255, 0.2); min-width: 140px;">
                    <div style="color: #93C5FD; font-size: 0.75rem; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">
                        Overall Readiness
                    </div>
                    <div style="color: white; font-size: 2.2rem; font-weight: 950; line-height: 1;">
                        {score}%
                    </div>
                    <div style="color: #34D399; font-size: 0.82rem; font-weight: 900; margin-top: 6px;">
                        {level}
                    </div>
                </div>

                <div style="text-align: center; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(12px); padding: 16px 22px; border-radius: 18px; border: 1px solid rgba(255, 255, 255, 0.2); min-width: 150px;">
                    <div style="color: #93C5FD; font-size: 0.75rem; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">
                        Today's Focus
                    </div>
                    <div style="color: #60A5FA; font-size: 0.95rem; font-weight: 950; line-height: 1.35; margin-top: 4px;">
                        {focus}
                    </div>
                </div>
            </div>
        </div>
    </div>
    """)


def coach_next_best_action_card_html(rec_data: dict) -> HtmlFragment:
    """Render ONE Single Primary Next Best Action Card."""
    action = html.escape(str(rec_data.get("recommendation", "Complete Economy Revision")))
    reason = html.escape(str(rec_data.get("reason", "Highest impact on readiness trajectory.")))
    priority = html.escape(str(rec_data.get("priority", "HIGH")))

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 22px; margin-bottom: 22px; background: linear-gradient(135deg, rgba(236, 253, 245, 0.96), rgba(209, 250, 229, 0.96)); border: 1px solid rgba(16, 185, 129, 0.4); box-shadow: 0 12px 28px rgba(16, 185, 129, 0.12);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 1.3rem;">⚡</span>
                <span style="font-size: 1.05rem; font-weight: 950; color: #065F46;">Section 9 — Next Best Action</span>
            </div>
            <span style="background: #10B981; color: white; font-size: 0.75rem; font-weight: 900; padding: 4px 12px; border-radius: 999px;">
                Priority: {priority}
            </span>
        </div>
        <div style="font-size: 1.35rem; font-weight: 950; color: #047857; margin-bottom: 6px;">
            🎯 {action}
        </div>
        <div style="color: #064E3B; font-size: 0.9rem; font-weight: 700; line-height: 1.45;">
            <span style="font-weight: 900;">Why now?</span> {reason}
        </div>
    </div>
    """)


def coach_mentor_summary_card_html(readiness_data: dict, rec_data: dict, revision_data: dict) -> HtmlFragment:
    """Render Unified AI Mentor Summary Card."""
    readiness_level = html.escape(str(readiness_data.get("readiness_level", "Developing Readiness")))
    focus = html.escape(str(rec_data.get("recommendation", "Geography Revision")))
    phase = html.escape(str(revision_data.get("revision_phase", "30-Day Plan")))

    summary_text = (
        f"You are steadily improving in the {readiness_level} phase. "
        f"Focus on {focus} today as part of your {phase}. "
        "Complete your daily practice set before advancing to the next revision cycle."
    )

    return _fragment(f"""
    <div class="nova-glass-card" style="padding: 22px; margin-bottom: 22px; background: linear-gradient(135deg, rgba(254, 243, 199, 0.95), rgba(253, 230, 138, 0.95)); border: 1px solid rgba(245, 158, 11, 0.4);">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <span style="font-size: 1.4rem;">🧠</span>
            <div style="font-size: 1.05rem; font-weight: 950; color: #92400E;">
                Section 10 — Unified AI Mentor Executive Summary
            </div>
        </div>
        <div style="color: #78350F; font-size: 0.95rem; font-weight: 750; line-height: 1.6; background: rgba(255, 255, 255, 0.7); padding: 14px 18px; border-radius: 14px; border: 1px solid rgba(245, 158, 11, 0.25);">
            "{summary_text}"
        </div>
    </div>
    """)











