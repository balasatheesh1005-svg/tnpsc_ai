import html
import streamlit as st

from core.learning_intelligence_ai import get_learning_intelligence
from ui.components.cards import (
    glass_card,
    learning_dna_grid,
    mastery_probability_ring,
    mentor_personality_banner,
    recovery_plan_timeline,
    render_card_styles,
    root_cause_bottleneck_card,
    section_title,
)
from ui.theme import render_theme_css


def render_learning_intelligence_dashboard(user: str = None):
    """
    Renders Learning Intelligence Dashboard V2.
    Visualizes pre-computed outputs from Learning Intelligence Engine V2.
    Answers WHY the student is weak and how to recover.
    """
    if user is None:
        user = st.session_state.get("username", "")

    render_theme_css()
    render_card_styles()

    # Fetch Engine V2 Master Intelligence (Zero UI Calculation)
    intel = get_learning_intelligence(user)

    # ---------------- 8. MENTOR INSIGHT ----------------
    mentor_msg = intel.get("mentor_insight", "Focus on your targeted recovery plan to build topic mastery.")
    st.html(mentor_personality_banner(mentor_msg).markup)

    # ---------------- HEADER TITLE ----------------
    section_title("Learning Intelligence Engine V2", "Personalized Diagnostic & Recovery Intelligence")

    # ---------------- 7. CURRENT RECOMMENDATION ----------------
    rec_text = intel.get("recommendation", "Execute your recovery plan to boost accuracy.")
    glass_card("🎯 Current Recommendation", value="Actionable Target", body=rec_text)

    # CTA Button
    col_cta, _ = st.columns([2, 1])
    with col_cta:
        if st.button("⚡ Start Recovery Session →", type="primary", use_container_width=True):
            st.session_state.update(
                {
                    "q_index": 0,
                    "score": 0,
                    "answered": False,
                    "test_active": True,
                    "test_mode": "weak",
                    "test_results_processed": False,
                    "test_subject": intel.get("subject", "polity").lower(),
                    "test_topic": intel.get("topic", "general").lower(),
                }
            )
            st.rerun()

    st.write("")

    # ---------------- 1. LEARNING DNA ----------------
    dna = intel.get("learning_dna", {})
    st.html(learning_dna_grid(dna).markup)

    st.write("")

    # ---------------- 2. ROOT CAUSE & 3. LEARNING BOTTLENECK ----------------
    root_cause = intel.get("root_cause", "Concept Application")
    explanation = intel.get("root_explanation", "Focus on analytical reasoning practice.")
    bottleneck = intel.get("learning_bottleneck", "History ↓ Modern India ↓ Hard Repository ↓ Assertion & Reason")

    st.html(root_cause_bottleneck_card(root_cause, explanation, bottleneck).markup)

    st.write("")

    # ---------------- 4. RECOVERY PLAN & 5. ESTIMATED RECOVERY ----------------
    recovery_steps = intel.get("recovery_plan", [])
    estimated_sessions = intel.get("estimated_recovery", "3 Sessions")

    st.html(recovery_plan_timeline(recovery_steps, estimated_sessions).markup)

    st.write("")

    # ---------------- 6. TOPIC MASTERY PROBABILITY ----------------
    current_mastery = intel.get("current_mastery", 68.0)
    projected_mastery = intel.get("mastery_probability", 90.0)

    st.html(mastery_probability_ring(current_mastery, projected_mastery).markup)

    st.write("")

    # ---------------- DIAGNOSTIC STRENGTH & WEAKNESS ----------------
    col_str, col_wk = st.columns(2, gap="small")
    with col_str:
        glass_card(
            "💪 Key Learning Strength",
            value=intel.get("learning_strength", "Knowledge"),
            body="Based on high foundational recall across practice sets.",
        )
    with col_wk:
        glass_card(
            "⚠️ Priority Focus Area",
            value=intel.get("learning_weakness", "Assertion & Reason"),
            body="Lowest accuracy sub-repository requiring targeted revision.",
        )
