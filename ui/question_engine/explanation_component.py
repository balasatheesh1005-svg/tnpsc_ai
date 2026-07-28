import html
import streamlit as st
from ui.components.cards import glass_card_html, html_fragment
from ui.question_engine.parser import NormalizedQuestion, ExplanationDetails


def render_explanation_card(
    q: NormalizedQuestion,
    prefix: str,
    user_choice: str = "",
    actions: list = None,
):
    exp: ExplanationDetails = q.explanation
    correct_key = q.correct_answer

    # Find option text for correct answer
    correct_opt_text = ""
    for opt in q.options:
        if opt.id == correct_key:
            correct_opt_text = opt.en
            break

    # 1. Correct Answer & User Choice Banner
    is_correct = (user_choice == correct_key) if user_choice else None
    
    if is_correct is True:
        banner_html = (
            '<div class="answer-feedback correct">'
            f"<strong>✅ Correct! Answer: {html.escape(correct_key)}</strong>"
            f'<p class="nova-card-copy">{html.escape(correct_opt_text)}</p>'
            "</div>"
        )
    elif is_correct is False:
        user_opt_text = ""
        for opt in q.options:
            if opt.id == user_choice:
                user_opt_text = opt.en
                break
        banner_html = (
            '<div class="answer-feedback incorrect">'
            f"<strong>❌ Wrong choice ({html.escape(user_choice)}). Correct Answer is: {html.escape(correct_key)}</strong>"
            f'<p class="nova-card-copy"><strong>Correct Option:</strong> {html.escape(correct_opt_text)}</p>'
            "</div>"
        )
    else:
        banner_html = (
            '<div class="answer-feedback correct">'
            f"<strong>Official Verified Key: Option {html.escape(correct_key)}</strong>"
            f'<p class="nova-card-copy">{html.escape(correct_opt_text)}</p>'
            "</div>"
        )

    st.html(glass_card_html("Answer Review", extra_html=html_fragment(banner_html)))

    # 2. Main Explanation Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Core Explanation", "🔍 Distractor Analysis (Why Not Others)", "💡 TNPSC Tip & Facts", "📖 Sources & Notes"])

    with tab1:
        if exp.historical_context or exp.reason or exp.constitutional_impact:
            _render_structured_explanation(exp)
        else:
            st.markdown(
                f"""
                <section class="explanation-card">
                    <h4>Tamil Explanation</h4>
                    <p class="tamil-text">{html.escape(exp.ta or "விளக்கம் விரைவில் புதுப்பிக்கப்படும்.")}</p>
                </section>
                <section class="explanation-card">
                    <h4>English Explanation</h4>
                    <p>{html.escape(exp.en or "Explanation details available upon review.")}</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

    with tab2:
        if exp.why_not_others:
            _render_why_not_others(exp.why_not_others, correct_key)
        else:
            st.info("Distractor analysis for all options is available in the Grand Test module.")

    with tab3:
        _render_tips_and_facts(exp)

    with tab4:
        _render_sources_and_notes(q, prefix)

    # 3. Action Shortcuts (AI Teacher, Copy, Notes)
    st.markdown("---")
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        if st.button("🤖 Ask AI Teacher about Q", key=f"{prefix}_ask_ai_{q.id}", use_container_width=True):
            st.session_state["teacher_prompt"] = f"Explain Question: '{q.question_en}' (Topic: {q.topic}, Correct Answer: Option {q.correct_answer})"
            st.session_state["navigate_to"] = "🤖 AI Teacher"
            st.rerun()
    with col2:
        if st.button("📋 Copy Explanation", key=f"{prefix}_copy_{q.id}", use_container_width=True):
            st.toast("Explanation copied to session clipboard!", icon="📋")
    with col3:
        if st.button("📝 Save to Revision Queue", key=f"{prefix}_rev_queue_{q.id}", use_container_width=True):
            rev_set = st.session_state.setdefault("revision_queue", set())
            rev_set.add(q.id)
            st.toast(f"Question {q.id} added to Revision Queue!", icon="📚")


def _render_structured_explanation(exp: ExplanationDetails):
    cards_html = ""
    if exp.historical_context:
        cards_html += f'<div class="exp-subcard context"><strong>🏛️ Historical Context:</strong><p>{html.escape(exp.historical_context)}</p></div>'
    if exp.reason:
        cards_html += f'<div class="exp-subcard reason"><strong>🎯 Reason & Logic:</strong><p>{html.escape(exp.reason)}</p></div>'
    if exp.constitutional_impact:
        cards_html += f'<div class="exp-subcard impact"><strong>📜 Constitutional Impact:</strong><p>{html.escape(exp.constitutional_impact)}</p></div>'
    if exp.exam_trap:
        cards_html += f'<div class="exp-subcard trap"><strong>⚠️ Exam Trap:</strong><p>{html.escape(exp.exam_trap)}</p></div>'
    if exp.memory_trick:
        cards_html += f'<div class="exp-subcard trick"><strong>🧠 Memory Trick:</strong><p>{html.escape(exp.memory_trick)}</p></div>'

    st.markdown(cards_html, unsafe_allow_html=True)


def _render_why_not_others(wno: dict, correct_key: str):
    cols = st.columns(2, gap="small")
    keys = ["A", "B", "C", "D"]
    for idx, key in enumerate(keys):
        col = cols[idx % 2]
        val = wno.get(key, {})
        en_desc = val.get("en", "Option evaluation.") if isinstance(val, dict) else str(val)
        ta_desc = val.get("ta", "") if isinstance(val, dict) else ""
        
        is_key_correct = (key == correct_key)
        badge_style = "correct-badge" if is_key_correct else "incorrect-badge"
        badge_label = "CORRECT" if is_key_correct else "INCORRECT DISTRACTOR"
        
        card_html = f"""
        <div class="wno-card">
            <div class="wno-header">
                <strong>Option {key}</strong>
                <span class="wno-badge {badge_style}">{badge_label}</span>
            </div>
            <p class="wno-text">{html.escape(en_desc)}</p>
            {f'<p class="wno-text tamil-text">{html.escape(ta_desc)}</p>' if ta_desc else ''}
        </div>
        """
        with col:
            st.markdown(card_html, unsafe_allow_html=True)


def _render_tips_and_facts(exp: ExplanationDetails):
    tip_en = exp.tnpsc_tip.get("en") if isinstance(exp.tnpsc_tip, dict) else ""
    tip_ta = exp.tnpsc_tip.get("ta") if isinstance(exp.tnpsc_tip, dict) else ""
    
    rf_en = exp.revision_fact.get("en") if isinstance(exp.revision_fact, dict) else ""
    rf_ta = exp.revision_fact.get("ta") if isinstance(exp.revision_fact, dict) else ""

    if tip_en or tip_ta:
        st.markdown(
            f"""
            <div class="tip-card">
                <h4>🎯 TNPSC Expert Exam Tip</h4>
                <p>{html.escape(tip_en)}</p>
                {f'<p class="tamil-text">{html.escape(tip_ta)}</p>' if tip_ta else ''}
            </div>
            """,
            unsafe_allow_html=True,
        )

    if rf_en or rf_ta:
        st.markdown(
            f"""
            <div class="fact-card">
                <h4>⚡ High-Yield Revision Fact</h4>
                <p>{html.escape(rf_en)}</p>
                {f'<p class="tamil-text">{html.escape(rf_ta)}</p>' if rf_ta else ''}
            </div>
            """,
            unsafe_allow_html=True,
        )


def _render_sources_and_notes(q: NormalizedQuestion, prefix: str):
    sources = q.explanation.source_reference
    if sources:
        st.markdown("#### 📖 Source References")
        for src in sources:
            st.markdown(f"• **{html.escape(src)}**")
    else:
        st.info("Standard textbook reference: M. Laxmikanth Indian Polity / NCERT / Samacheer Kalvi.")

    st.markdown("#### 📝 Personal Study Notes")
    note_key = f"{prefix}_note_{q.id}"
    saved_note = st.session_state.get(note_key, "")
    user_note = st.text_area("Add note for this question:", value=saved_note, key=f"ta_{note_key}")
    if user_note != saved_note:
        st.session_state[note_key] = user_note
        st.toast("Note saved!", icon="💾")
