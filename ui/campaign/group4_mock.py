"""TNPSC Group 4 Free Mini Mock - Campaign UI Renderer.

Provides the complete public marketing funnel without requiring authentication.
All campaign state is stored in Streamlit session state under the `campaign_group4_` namespace.
Zero database writes.
Zero XP / streak / progress writes.
"""

from __future__ import annotations

import html
import time
from typing import Any, Dict, List, Optional
import streamlit as st

from core.campaign.group4_curated_questions import (
    ANALYSIS_BUCKETS,
    BUCKET_APTITUDE,
    BUCKET_GENERAL_STUDIES,
    BUCKET_GENERAL_TAMIL,
    CampaignManifestError,
    calculate_campaign_results,
    load_group4_campaign_questions,
)
from ui.question_engine.parser import NormalizedQuestion


# ---------------- SESSION STATE HELPERS ----------------

def _init_campaign_state() -> None:
    """Ensure basic campaign keys exist in session state."""
    if "campaign_group4_stage" not in st.session_state:
        st.session_state["campaign_group4_stage"] = "landing"
    if "campaign_group4_questions" not in st.session_state:
        st.session_state["campaign_group4_questions"] = None
    if "campaign_group4_index" not in st.session_state:
        st.session_state["campaign_group4_index"] = 0
    if "campaign_group4_answers" not in st.session_state:
        st.session_state["campaign_group4_answers"] = {}
    if "campaign_group4_started_at" not in st.session_state:
        st.session_state["campaign_group4_started_at"] = None
    if "campaign_group4_result" not in st.session_state:
        st.session_state["campaign_group4_result"] = None
    if "campaign_group4_review_filter" not in st.session_state:
        st.session_state["campaign_group4_review_filter"] = "all"


def _reset_campaign_test(start_stage: str = "test") -> None:
    """Reset campaign test session while preserving the loaded questions if available."""
    # Remove only campaign_group4_* keys
    keys_to_clear = [k for k in list(st.session_state.keys()) if k.startswith("campaign_group4_")]
    for k in keys_to_clear:
        del st.session_state[k]

    st.session_state["campaign_group4_stage"] = start_stage
    st.session_state["campaign_group4_index"] = 0
    st.session_state["campaign_group4_answers"] = {}
    st.session_state["campaign_group4_started_at"] = time.time()
    st.session_state["campaign_group4_result"] = None
    st.session_state["campaign_group4_review_filter"] = "all"

    try:
        st.session_state["campaign_group4_questions"] = load_group4_campaign_questions()
    except CampaignManifestError as e:
        st.session_state["campaign_group4_error"] = str(e)


# ---------------- CSS STYLING ----------------

def _inject_campaign_styles() -> None:
    """Inject responsive, mobile-first styling for campaign viewports."""
    st.markdown(
        """
        <style>
            /* Base container styling */
            .campaign-container {
                max-width: 650px;
                margin: 0 auto;
                padding: 10px 14px;
            }
            .hero-card {
                background: linear-gradient(135deg, #1E3A8A 0%, #1E40AF 50%, #2563EB 100%);
                border-radius: 18px;
                padding: 24px 20px;
                color: #FFFFFF;
                text-align: center;
                box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.35);
                margin-bottom: 20px;
            }
            .hero-badge-row {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 8px;
                margin: 14px 0 16px 0;
            }
            .hero-badge {
                background: rgba(255, 255, 255, 0.18);
                backdrop-filter: blur(8px);
                border: 1px solid rgba(255, 255, 255, 0.25);
                color: #FFFFFF;
                padding: 4px 12px;
                border-radius: 100px;
                font-size: 0.82em;
                font-weight: 700;
            }
            .value-box {
                background: #F8FAFC;
                border: 1px solid #E2E8F0;
                border-radius: 14px;
                padding: 16px 18px;
                margin-bottom: 20px;
            }
            .value-item {
                display: flex;
                align-items: center;
                gap: 10px;
                font-size: 0.95em;
                font-weight: 600;
                color: #1E293B;
                margin: 8px 0;
            }
            .value-check {
                color: #16A34A;
                font-weight: 900;
                font-size: 1.1em;
            }
            .friction-text {
                text-align: center;
                font-size: 0.82em;
                color: #64748B;
                margin-top: 10px;
                font-weight: 600;
            }
            .question-card {
                background: #FFFFFF;
                border: 1px solid #CBD5E1;
                border-radius: 14px;
                padding: 18px;
                margin-bottom: 16px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.03);
            }
            .section-pill {
                display: inline-block;
                background: #EEF2FF;
                color: #4F46E5;
                font-size: 0.78em;
                font-weight: 800;
                padding: 3px 10px;
                border-radius: 6px;
                margin-bottom: 10px;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            .q-stem-ta {
                font-size: 1.12em;
                font-weight: 700;
                color: #0F172A;
                line-height: 1.5;
                margin-bottom: 8px;
            }
            .q-stem-en {
                font-size: 0.95em;
                font-weight: 500;
                color: #475569;
                line-height: 1.45;
                margin-bottom: 14px;
            }
            .stat-metric-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
                margin-bottom: 16px;
            }
            @media (min-width: 480px) {
                .stat-metric-grid {
                    grid-template-columns: repeat(3, 1fr);
                }
            }
            .stat-box {
                background: #F8FAFC;
                border: 1px solid #E2E8F0;
                border-radius: 12px;
                padding: 12px;
                text-align: center;
            }
            .stat-val {
                font-size: 1.35em;
                font-weight: 800;
                color: #1E293B;
                margin-bottom: 2px;
            }
            .stat-lbl {
                font-size: 0.75em;
                font-weight: 700;
                color: #64748B;
                text-transform: uppercase;
            }
            .bucket-table {
                width: 100%;
                border-collapse: collapse;
                margin: 12px 0;
                font-size: 0.88em;
            }
            .bucket-table th {
                background: #F1F5F9;
                color: #334155;
                text-align: left;
                padding: 10px 8px;
                font-weight: 700;
                border-bottom: 2px solid #CBD5E1;
            }
            .bucket-table td {
                padding: 10px 8px;
                border-bottom: 1px solid #E2E8F0;
                color: #1E293B;
            }
            .review-card {
                background: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 12px;
                padding: 16px;
                margin-bottom: 16px;
            }
            .badge-correct {
                background: #DCFCE7;
                color: #15803D;
                font-weight: 700;
                font-size: 0.8em;
                padding: 3px 8px;
                border-radius: 6px;
            }
            .badge-wrong {
                background: #FEE2E2;
                color: #B91C1C;
                font-weight: 700;
                font-size: 0.8em;
                padding: 3px 8px;
                border-radius: 6px;
            }
            .badge-unanswered {
                background: #F1F5F9;
                color: #475569;
                font-weight: 700;
                font-size: 0.8em;
                padding: 3px 8px;
                border-radius: 6px;
            }
            .review-opt {
                padding: 8px 12px;
                border-radius: 8px;
                margin: 6px 0;
                font-size: 0.92em;
            }
            .review-opt-correct {
                background: #ECFDF5;
                border: 1px solid #10B981;
                font-weight: 700;
                color: #065F46;
            }
            .review-opt-wrong {
                background: #FEF2F2;
                border: 1px solid #EF4444;
                color: #991B1B;
            }
            .review-opt-normal {
                background: #F8FAFC;
                border: 1px solid #E2E8F0;
                color: #334155;
            }
            .explanation-box {
                background: #F0FDF4;
                border-left: 4px solid #16A34A;
                padding: 12px 14px;
                border-radius: 0 8px 8px 0;
                margin-top: 10px;
                font-size: 0.9em;
                color: #166534;
            }
            /* Hide Streamlit default header/sidebar on campaign page for immersion */
            [data-testid="stSidebar"] { display: none; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------- LANDING STAGE ----------------

def _render_landing_stage() -> None:
    """Render mobile-first public campaign landing hero and value points."""
    st.markdown('<div class="campaign-container">', unsafe_allow_html=True)

    # Hero card
    st.markdown(
        """
        <div class="hero-card">
            <div style="font-size: 0.9em; font-weight: 800; letter-spacing: 1.5px; opacity: 0.9; margin-bottom: 4px;">
                TNPSC GROUP 4
            </div>
            <h1 style="color: #FFFFFF; font-size: 1.85em; font-weight: 900; margin: 0 0 10px 0; line-height: 1.2;">
                இலவச Mini Mock Test
            </h1>
            <div class="hero-badge-row">
                <span class="hero-badge">25 Questions</span>
                <span class="hero-badge">தமிழ்</span>
                <span class="hero-badge">Instant Result</span>
                <span class="hero-badge">Weakness Analysis</span>
            </div>
            <p style="font-size: 0.95em; line-height: 1.5; margin: 0; opacity: 0.95;">
                உங்கள் Group 4 தயார்நிலை எப்படி இருக்கிறது என்பதை இந்த இலவச Mini Mock மூலம் தெரிந்துகொள்ளுங்கள்.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Value points box
    st.markdown(
        """
        <div class="value-box">
            <div class="value-item">
                <span class="value-check">✓</span>
                <span>உடனடி மதிப்பெண் & துல்லியமான பகுப்பாய்வு</span>
            </div>
            <div class="value-item">
                <span class="value-check">✓</span>
                <span>ஒவ்வொரு கேள்விக்கும் தெளிவான சரியான விடை & விளக்கம்</span>
            </div>
            <div class="value-item">
                <span class="value-check">✓</span>
                <span>பாடவாரியாக நீங்கள் மேம்படுத்த வேண்டிய பகுதிகள்</span>
            </div>
            <div class="value-item">
                <span class="value-check">✓</span>
                <span>100% இலவசம் — எவ்வித கட்டணமும் இல்லை</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Primary CTA
    if st.button(
        "இலவச தேர்வை தொடங்குங்கள் 🚀",
        key="campaign_start_test_btn",
        type="primary",
        use_container_width=True,
    ):
        _reset_campaign_test(start_stage="test")
        st.rerun()

    # Friction / Trust text
    st.markdown(
        """
        <div class="friction-text">
            பதிவு தேவையில்லை • 100% இலவசம்
        </div>
        <div style="text-align: center; margin-top: 24px; padding-top: 16px; border-top: 1px solid #E2E8F0;">
            <div style="font-weight: 800; color: #1E293B; font-size: 0.95em;">TNPSC Nova AI</div>
            <div style="font-size: 0.8em; color: #64748B; margin-top: 2px;">
                உங்கள் அரசு வேலை நோக்கி ஒரு படி முன்னால்
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- TEST RUNNER STAGE ----------------

def _render_test_stage() -> None:
    """Render deterministic 1-question-at-a-time test runner."""
    questions: Optional[List[NormalizedQuestion]] = st.session_state.get("campaign_group4_questions")

    # Guard: load if not loaded yet
    if not questions:
        try:
            questions = load_group4_campaign_questions()
            st.session_state["campaign_group4_questions"] = questions
            st.session_state["campaign_group4_started_at"] = time.time()
        except CampaignManifestError as e:
            st.error("தேர்வுக்கான வினாக்களை ஏற்றுவதில் சிக்கல் ஏற்பட்டுள்ளது. சிறிது நேரம் கழித்து மீண்டும் முயற்சிக்கவும்.")
            st.caption(f"Integrity Notice: {e}")
            if st.button("முகப்பு பக்கத்திற்கு திரும்புக", key="campaign_error_home_btn"):
                st.session_state["campaign_group4_stage"] = "landing"
                st.rerun()
            return

    curr_idx = st.session_state.get("campaign_group4_index", 0)
    total_q = len(questions)

    if curr_idx < 0:
        curr_idx = 0
    elif curr_idx >= total_q:
        curr_idx = total_q - 1
    st.session_state["campaign_group4_index"] = curr_idx

    q = questions[curr_idx]
    answers: Dict[int, str] = st.session_state.get("campaign_group4_answers", {})
    answered_count = len(answers)

    st.markdown('<div class="campaign-container">', unsafe_allow_html=True)

    # Top tracker & progress bar
    st.progress((curr_idx + 1) / total_q)

    top_c1, top_c2 = st.columns([2, 1])
    with top_c1:
        st.markdown(
            f'<div style="font-size: 0.92em; font-weight: 800; color: #1E293B;">'
            f'கேள்வி {curr_idx + 1} / {total_q} <span style="font-weight: 500; color: #64748B;">(Question {curr_idx + 1} of {total_q})</span>'
            f'</div>',
            unsafe_allow_html=True,
        )
    with top_c2:
        st.markdown(
            f'<div style="text-align: right; font-size: 0.82em; font-weight: 700; color: #2563EB;">'
            f'பதிலளித்தவை: {answered_count}/{total_q}'
            f'</div>',
            unsafe_allow_html=True,
        )

    # Bucket Section indicator
    bucket_label = getattr(q, "campaign_bucket", "General Studies")
    st.markdown(
        f'<div style="margin-top: 8px;"><span class="section-pill">{html.escape(bucket_label)}</span></div>',
        unsafe_allow_html=True,
    )

    # Question stem card
    stem_ta = q.question_ta.strip() if q.question_ta else ""
    stem_en = q.question_en.strip() if q.question_en else ""

    stem_html = '<div class="question-card">'
    if stem_ta:
        stem_html += f'<div class="q-stem-ta">{html.escape(stem_ta)}</div>'
    if stem_en and stem_en != stem_ta and stem_en != "Question text not available.":
        stem_html += f'<div class="q-stem-en">{html.escape(stem_en)}</div>'
    stem_html += '</div>'
    st.markdown(stem_html, unsafe_allow_html=True)

    # Options presentation
    option_labels = []
    opt_keys = []
    for opt in q.options:
        opt_id = opt.id.upper()
        opt_keys.append(opt_id)
        # Display Tamil text if available, along with English if distinct
        ta_txt = opt.ta.strip() if opt.ta else ""
        en_txt = opt.en.strip() if opt.en else ""
        if ta_txt and en_txt and ta_txt != en_txt:
            display_str = f"({opt_id})  {ta_txt} / {en_txt}"
        else:
            display_str = f"({opt_id})  {ta_txt or en_txt}"
        option_labels.append(display_str)

    # Radio selection preservation
    current_saved_ans = answers.get(curr_idx)
    default_radio_idx = None
    if current_saved_ans in opt_keys:
        default_radio_idx = opt_keys.index(current_saved_ans)

    radio_key = f"campaign_radio_q_{curr_idx}"
    user_selection = st.radio(
        label=f"கேள்வி {curr_idx + 1} தேர்வு",
        options=option_labels,
        index=default_radio_idx,
        key=radio_key,
        label_visibility="collapsed",
    )

    # If user selected an option, update in-memory answers state
    if user_selection is not None:
        selected_key = opt_keys[option_labels.index(user_selection)]
        if answers.get(curr_idx) != selected_key:
            answers[curr_idx] = selected_key
            st.session_state["campaign_group4_answers"] = answers

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # Navigation buttons
    col_prev, col_next = st.columns([1, 1], gap="small")

    with col_prev:
        if st.button(
            "⬅️ முந்தையது",
            key=f"campaign_prev_btn_{curr_idx}",
            disabled=(curr_idx == 0),
            use_container_width=True,
        ):
            st.session_state["campaign_group4_index"] = max(0, curr_idx - 1)
            st.rerun()

    with col_next:
        if curr_idx < total_q - 1:
            if st.button(
                "அடுத்தது ➡️",
                key=f"campaign_next_btn_{curr_idx}",
                type="primary",
                use_container_width=True,
            ):
                st.session_state["campaign_group4_index"] = curr_idx + 1
                st.rerun()
        else:
            # On final question 25, highlight primary submit
            if st.button(
                "தேர்வை சமர்ப்பிக்கவும் 🏁",
                key="campaign_submit_primary_btn",
                type="primary",
                use_container_width=True,
            ):
                _submit_campaign_test(questions)
                st.rerun()

    # Floating / bottom submit button accessible anytime
    if curr_idx < total_q - 1:
        st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)
        unans_count = total_q - len(answers)
        submit_label = (
            f"தேர்வை சமர்ப்பிக்கவும் 🏁 ({unans_count} விடுபட்டவை)"
            if unans_count > 0
            else "தேர்வை சமர்ப்பிக்கவும் 🏁"
        )
        if st.button(
            submit_label,
            key="campaign_early_submit_btn",
            use_container_width=True,
        ):
            _submit_campaign_test(questions)
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def _submit_campaign_test(questions: List[NormalizedQuestion]) -> None:
    """Freeze snapshot and calculate in-memory test results."""
    started_at = st.session_state.get("campaign_group4_started_at", time.time())
    elapsed = int(time.time() - (started_at or time.time()))
    answers = st.session_state.get("campaign_group4_answers", {})

    result_data = calculate_campaign_results(
        questions=questions,
        answers=answers,
        elapsed_time=elapsed,
    )
    st.session_state["campaign_group4_result"] = result_data
    st.session_state["campaign_group4_stage"] = "result"


# ---------------- RESULT STAGE ----------------

def _render_result_stage() -> None:
    """Render truthful, evidence-based 3-bucket result screen with conversion CTA."""
    res = st.session_state.get("campaign_group4_result")
    questions = st.session_state.get("campaign_group4_questions")

    if not res or not questions:
        st.session_state["campaign_group4_stage"] = "landing"
        st.rerun()
        return

    st.markdown('<div class="campaign-container">', unsafe_allow_html=True)

    # Result Header
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="font-size: 0.85em; font-weight: 800; color: #2563EB; text-transform: uppercase; letter-spacing: 1px;">
                TNPSC Group 4 Mini Mock
            </div>
            <h1 style="color: #0F172A; font-size: 1.75em; font-weight: 900; margin: 4px 0 6px 0;">
                உங்கள் முடிவு
            </h1>
            <p style="font-size: 0.9em; color: #64748B; margin: 0;">
                இந்த Mini Mock அடிப்படையில் கணக்கிடப்பட்ட உங்கள் உடனடி தேர்வு முடிவு
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Score Metrics Grid
    correct = res["correct"]
    wrong = res["wrong"]
    unanswered = res["unanswered"]
    accuracy = res["accuracy"]
    elapsed_sec = res["elapsed_time_sec"]
    mins = elapsed_sec // 60
    secs = elapsed_sec % 60
    time_str = f"{mins}m {secs}s" if mins > 0 else f"{secs}s"

    st.markdown(
        f"""
        <div class="stat-metric-grid">
            <div class="stat-box" style="border-color: #93C5FD; background: #EFF6FF;">
                <div class="stat-val" style="color: #1D4ED8;">{correct} / 25</div>
                <div class="stat-lbl" style="color: #2563EB;">மதிப்பெண் (Score)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="color: #15803D;">{correct}</div>
                <div class="stat-lbl">சரி (Correct)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="color: #B91C1C;">{wrong}</div>
                <div class="stat-lbl">தவறு (Wrong)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="color: #64748B;">{unanswered}</div>
                <div class="stat-lbl">விடுபட்டவை (Skipped)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="color: #4F46E5;">{accuracy}%</div>
                <div class="stat-lbl">துல்லியம் (Accuracy)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="color: #0F172A;">{time_str}</div>
                <div class="stat-lbl">நேரம் (Time Taken)</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 3-Bucket Performance Breakdown
    st.markdown(
        """
        <div style="margin: 20px 0 8px 0; font-size: 1.05em; font-weight: 800; color: #1E293B;">
            📊 பாடவாரி செயல்திறன் (Section-wise Breakdown)
        </div>
        """,
        unsafe_allow_html=True,
    )

    buckets = res["bucket_breakdown"]
    table_rows = ""
    for b_name in ANALYSIS_BUCKETS:
        b_data = buckets.get(b_name, {})
        tot = b_data.get("total", 0)
        att = b_data.get("answered", 0)
        corr = b_data.get("correct", 0)
        acc = b_data.get("accuracy", 0.0)

        # Bilingual label
        b_label_ta = {
            BUCKET_GENERAL_TAMIL: "பொதுத்தமிழ் (General Tamil)",
            BUCKET_GENERAL_STUDIES: "பொது அறிவு (General Studies)",
            BUCKET_APTITUDE: "திறனறிவு (Aptitude & Mental Ability)",
        }.get(b_name, b_name)

        table_rows += f"""
        <tr>
            <td style="font-weight: 700;">{html.escape(b_label_ta)}</td>
            <td style="text-align: center;">{tot}</td>
            <td style="text-align: center;">{att}</td>
            <td style="text-align: center; color: #15803D; font-weight: 700;">{corr}</td>
            <td style="text-align: center; font-weight: 700;">{acc}%</td>
        </tr>
        """

    st.markdown(
        f"""
        <table class="bucket-table">
            <thead>
                <tr>
                    <th>பகுதி (Section)</th>
                    <th style="text-align: center;">மொத்தம்</th>
                    <th style="text-align: center;">முயற்சித்தவை</th>
                    <th style="text-align: center;">சரி</th>
                    <th style="text-align: center;">துல்லியம்</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )

    # Truthful Improvement Analysis Box
    strongest = res.get("strongest_bucket")
    improvement = res.get("improvement_bucket")
    answered_total = res.get("answered", 0)

    st.markdown(
        """
        <div style="margin: 18px 0 8px 0; font-size: 1.05em; font-weight: 800; color: #1E293B;">
            🎯 இந்த Mini Mock அடிப்படையில் வழிகாட்டல்
        </div>
        """,
        unsafe_allow_html=True,
    )

    if answered_total < 3:
        analysis_box = """
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 14px 16px; font-size: 0.9em; color: #475569; line-height: 1.5;">
            <strong>போதுமான கேள்விகள் முயற்சிக்கப்படவில்லை:</strong> உங்கள் பலம் மற்றும் மேம்படுத்த வேண்டிய பகுதிகளை துல்லியமாக அறிய, அனைத்து கேள்விகளையும் முயற்சி செய்து மீண்டும் பார்க்கவும்.
        </div>
        """
    else:
        strong_label = {
            BUCKET_GENERAL_TAMIL: "பொதுத்தமிழ்",
            BUCKET_GENERAL_STUDIES: "பொது அறிவு",
            BUCKET_APTITUDE: "திறனறிவு & கணிதம்",
        }.get(strongest, strongest)

        weak_label = {
            BUCKET_GENERAL_TAMIL: "பொதுத்தமிழ்",
            BUCKET_GENERAL_STUDIES: "பொது அறிவு",
            BUCKET_APTITUDE: "திறனறிவு & கணிதம்",
        }.get(improvement, improvement)

        analysis_content = ""
        if strongest:
            analysis_content += (
                f"<div style='margin-bottom: 6px; color: #166534; font-weight: 600;'>"
                f"🌟 <strong>அதிக மதிப்பெண் பெற்ற பகுதி:</strong> {html.escape(strong_label)}"
                f"</div>"
            )
        if improvement:
            analysis_content += (
                f"<div style='color: #9A3412; font-weight: 600;'>"
                f"📌 <strong>மேம்படுத்த வேண்டிய பகுதி:</strong> {html.escape(weak_label)}"
                f"<div style='font-size: 0.9em; font-weight: 400; color: #7C2D12; margin-top: 4px;'>"
                f"இந்த 25 கேள்விகள் கொண்ட Mini Mock அடிப்படையில், நீங்கள் {html.escape(weak_label)} பகுதியில் கூடுதல் கவனம் செலுத்துவது உங்கள் ஒட்டுமொத்த மதிப்பெண்ணை உயர்த்த உதவும்."
                f"</div>"
                f"</div>"
            )
        else:
            analysis_content += (
                f"<div style='color: #166534; font-weight: 600;'>"
                f"🎉 அனைத்து பகுதிகளிலும் சிறந்த செயல்திறனை வெளிப்படுத்தியுள்ளீர்கள்!"
                f"</div>"
            )

        analysis_box = f"""
        <div style="background: #FFFBEB; border: 1px solid #FDE68A; border-radius: 12px; padding: 14px 16px; font-size: 0.92em; line-height: 1.5;">
            {analysis_content}
        </div>
        """

    st.markdown(analysis_box, unsafe_allow_html=True)
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    # Conversion Box
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); border-radius: 16px; padding: 20px; color: #FFFFFF; text-align: center; margin-bottom: 16px;">
            <div style="font-size: 1.15em; font-weight: 800; margin-bottom: 6px; line-height: 1.35;">
                உங்கள் முழு Progress-ஐ சேமித்து தொடர்ந்து பயிற்சி செய்யுங்கள்
            </div>
            <div style="font-size: 0.86em; color: #94A3B8; margin-bottom: 16px;">
                பாடவாரி குறிப்புகள் • தினசரி தேர்வுகள் • AI ஆசிரியர் வழிகாட்டல்
            </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "TNPSC Nova AI-ல் இலவசமாக தொடங்குங்கள் 🎯",
        key="campaign_signup_conversion_btn",
        type="primary",
        use_container_width=True,
    ):
        # Cleanly exit campaign query param and transition to authenticated signup page
        if "campaign" in st.query_params:
            del st.query_params["campaign"]
        st.session_state["auth_page"] = "signup"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Secondary Actions (Review Answers & Retake)
    col_act1, col_act2 = st.columns([1, 1], gap="small")
    with col_act1:
        if st.button(
            "விடைகளை சரிபார்க்கவும் 📖",
            key="campaign_view_review_btn",
            use_container_width=True,
        ):
            st.session_state["campaign_group4_stage"] = "review"
            st.rerun()

    with col_act2:
        if st.button(
            "மீண்டும் முயற்சி செய் 🔄",
            key="campaign_retake_btn",
            use_container_width=True,
        ):
            _reset_campaign_test(start_stage="test")
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- REVIEW STAGE ----------------

def _render_review_stage() -> None:
    """Render solution review with explanations without leaking internal repository details."""
    questions: Optional[List[NormalizedQuestion]] = st.session_state.get("campaign_group4_questions")
    answers: Dict[int, str] = st.session_state.get("campaign_group4_answers", {})

    if not questions:
        st.session_state["campaign_group4_stage"] = "landing"
        st.rerun()
        return

    st.markdown('<div class="campaign-container">', unsafe_allow_html=True)

    # Top return button
    col_back, col_title = st.columns([1, 2])
    with col_back:
        if st.button("⬅️ முடிவுக்குத் திரும்பு", key="campaign_review_back_btn", use_container_width=True):
            st.session_state["campaign_group4_stage"] = "result"
            st.rerun()
    with col_title:
        st.markdown(
            '<div style="font-size: 1.1em; font-weight: 800; color: #1E293B; padding-top: 4px;">விடைகள் & விளக்கம்</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<hr style='margin: 12px 0 16px 0; border: none; border-top: 1px solid #E2E8F0;' />", unsafe_allow_html=True)

    # Render each of the 25 questions
    for idx, q in enumerate(questions):
        user_choice = answers.get(idx)
        correct_ans = q.correct_answer.upper()
        bucket_label = getattr(q, "campaign_bucket", "General Studies")

        # Determine state badge
        if user_choice is None:
            badge_html = '<span class="badge-unanswered">⚪ விடுபட்டது</span>'
        elif user_choice == correct_ans:
            badge_html = '<span class="badge-correct">✅ சரியானது</span>'
        else:
            badge_html = f'<span class="badge-wrong">❌ தவறானது (உங்கள் தேர்வு: {html.escape(user_choice)})</span>'

        st.markdown(
            f"""
            <div class="review-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 0.85em; font-weight: 800; color: #475569;">
                        கேள்வி {idx + 1} / 25 • <span style="color: #4F46E5;">{html.escape(bucket_label)}</span>
                    </span>
                    {badge_html}
                </div>
            """,
            unsafe_allow_html=True,
        )

        # Question stem
        q_ta = q.question_ta.strip() if q.question_ta else ""
        q_en = q.question_en.strip() if q.question_en else ""
        st.markdown(f'<div class="q-stem-ta" style="font-size: 1.02em;">{html.escape(q_ta)}</div>', unsafe_allow_html=True)
        if q_en and q_en != q_ta and q_en != "Question text not available.":
            st.markdown(f'<div class="q-stem-en" style="font-size: 0.88em; margin-bottom: 10px;">{html.escape(q_en)}</div>', unsafe_allow_html=True)

        # Options
        for opt in q.options:
            opt_id = opt.id.upper()
            ta_txt = opt.ta.strip() if opt.ta else ""
            en_txt = opt.en.strip() if opt.en else ""
            if ta_txt and en_txt and ta_txt != en_txt:
                opt_display = f"({opt_id})  {ta_txt} / {en_txt}"
            else:
                opt_display = f"({opt_id})  {ta_txt or en_txt}"

            if opt_id == correct_ans:
                opt_class = "review-opt review-opt-correct"
                suffix = " &nbsp;✔️ <strong>[சரியான விடை]</strong>"
            elif user_choice == opt_id:
                opt_class = "review-opt review-opt-wrong"
                suffix = " &nbsp;✖️ <em>[உங்கள் தேர்வு]</em>"
            else:
                opt_class = "review-opt review-opt-normal"
                suffix = ""

            st.markdown(
                f'<div class="{opt_class}">{html.escape(opt_display)}{suffix}</div>',
                unsafe_allow_html=True,
            )

        # Explanation
        exp_ta = q.explanation.ta.strip() if (q.explanation and q.explanation.ta) else ""
        exp_en = q.explanation.en.strip() if (q.explanation and q.explanation.en) else ""
        exp_body = exp_ta or exp_en or "விளக்கம் விரைவில் புதுப்பிக்கப்படும்."

        st.markdown(
            f"""
            <div class="explanation-box">
                <div style="font-weight: 800; font-size: 0.9em; margin-bottom: 4px;">💡 விளக்கம்:</div>
                <div style="line-height: 1.45;">{html.escape(exp_body)}</div>
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Bottom conversion actions
    st.markdown(
        """
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 18px; text-align: center; margin: 20px 0 30px 0;">
            <div style="font-weight: 800; color: #1E293B; font-size: 1.05em; margin-bottom: 6px;">
                உங்கள் முழு Progress-ஐ சேமித்து தொடர்ந்து பயிற்சி செய்யுங்கள்
            </div>
            <div style="font-size: 0.85em; color: #64748B; margin-bottom: 14px;">
                இலவசமாக பதிவு செய்து அனைத்து பாடங்களையும் இன்றே தொடங்குங்கள்!
            </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "TNPSC Nova AI-ல் இலவசமாக தொடங்குங்கள் 🎯",
        key="campaign_review_signup_btn",
        type="primary",
        use_container_width=True,
    ):
        if "campaign" in st.query_params:
            del st.query_params["campaign"]
        st.session_state["auth_page"] = "signup"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- MAIN CAMPAIGN ROUTER ----------------

def render_group4_campaign() -> None:
    """Primary router for the Group 4 public marketing funnel.

    Operates completely unauthenticated.
    Produces zero database writes and maintains all state in session state.
    """
    _init_campaign_state()
    _inject_campaign_styles()

    stage = st.session_state.get("campaign_group4_stage", "landing")

    if stage == "test":
        _render_test_stage()
    elif stage == "result":
        _render_result_stage()
    elif stage == "review":
        _render_review_stage()
    else:
        _render_landing_stage()
