import html
import re
import streamlit as st
from ui.question_engine.parser import NormalizedQuestion


def render_question_body(q: NormalizedQuestion, lang_mode: str = "BOTH"):
    qtype = q.question_type

    # Dynamic render strategy based on question type
    if qtype == "Statement Based":
        _render_statement_layout(q, lang_mode)
    elif qtype == "Assertion & Reason":
        _render_assertion_reason_layout(q, lang_mode)
    elif qtype == "Match the Following":
        _render_match_following_layout(q, lang_mode)
    elif qtype == "Chronology":
        _render_chronology_layout(q, lang_mode)
    else:
        _render_direct_mcq_layout(q, lang_mode)


def _render_direct_mcq_layout(q: NormalizedQuestion, lang_mode: str):
    en_text = q.question_en
    ta_text = q.question_ta

    html_content = '<section class="nova-glass-card question-card">'
    if lang_mode in ["EN", "BOTH"] and en_text:
        html_content += f'<div class="question-title">{html.escape(en_text)}</div>'
    if lang_mode in ["TA", "BOTH"] and ta_text:
        html_content += f'<p class="nova-card-copy tamil-text">{html.escape(ta_text)}</p>'
    html_content += "</section>"

    st.markdown(html_content, unsafe_allow_html=True)


def _render_statement_layout(q: NormalizedQuestion, lang_mode: str):
    en_text = q.question_en
    ta_text = q.question_ta

    # Extract intro prompt vs numbered statements
    en_intro, en_statements = _parse_statements(en_text)
    ta_intro, ta_statements = _parse_statements(ta_text)

    st.markdown('<section class="nova-glass-card question-card">', unsafe_allow_html=True)
    
    if lang_mode in ["EN", "BOTH"] and en_intro:
        st.markdown(f'<div class="question-title">{html.escape(en_intro)}</div>', unsafe_allow_html=True)
    if lang_mode in ["TA", "BOTH"] and ta_intro:
        st.markdown(f'<p class="nova-card-copy tamil-text">{html.escape(ta_intro)}</p>', unsafe_allow_html=True)

    # Render statement cards
    if en_statements:
        for idx, stmt_en in enumerate(en_statements, 1):
            stmt_ta = ta_statements[idx - 1] if idx - 1 < len(ta_statements) else ""
            
            stmt_html = f'<div class="statement-card"><span class="statement-num">Statement {idx}</span>'
            if lang_mode in ["EN", "BOTH"] and stmt_en:
                stmt_html += f'<div class="statement-text-en">{html.escape(stmt_en)}</div>'
            if lang_mode in ["TA", "BOTH"] and stmt_ta:
                stmt_html += f'<div class="statement-text-ta tamil-text">{html.escape(stmt_ta)}</div>'
            stmt_html += "</div>"
            st.markdown(stmt_html, unsafe_allow_html=True)

    st.markdown("</section>", unsafe_allow_html=True)


def _parse_statements(text: str):
    if not text:
        return "", []
    
    # Split by numbered items like 1., 2., 3. or 1), 2)
    lines = text.split("\n")
    intro = []
    statements = []
    
    for line in lines:
        line_s = line.strip()
        if not line_s:
            continue
        if re.match(r"^\d+[\.\)]\s*", line_s):
            clean_stmt = re.sub(r"^\d+[\.\)]\s*", "", line_s)
            statements.append(clean_stmt)
        else:
            if not statements:
                intro.append(line_s)
            else:
                statements.append(line_s)
                
    return " ".join(intro), statements


def _render_assertion_reason_layout(q: NormalizedQuestion, lang_mode: str):
    en_text = q.question_en
    ta_text = q.question_ta

    st.markdown('<section class="nova-glass-card question-card">', unsafe_allow_html=True)
    st.markdown('<div class="question-type-badge-large">Assertion & Reason</div>', unsafe_allow_html=True)

    # Extract Assertion (A) and Reason (R)
    assertion_en, reason_en = _parse_ar(en_text)
    assertion_ta, reason_ta = _parse_ar(ta_text)

    # Assertion Card
    ar_html = '<div class="ar-container">'
    ar_html += '<div class="ar-box assertion-box"><span class="ar-label">Assertion (A)</span>'
    if lang_mode in ["EN", "BOTH"] and assertion_en:
        ar_html += f'<div class="ar-text-en">{html.escape(assertion_en)}</div>'
    if lang_mode in ["TA", "BOTH"] and assertion_ta:
        ar_html += f'<div class="ar-text-ta tamil-text">{html.escape(assertion_ta)}</div>'
    ar_html += "</div>"

    # Reason Card
    ar_html += '<div class="ar-box reason-box"><span class="ar-label">Reason (R)</span>'
    if lang_mode in ["EN", "BOTH"] and reason_en:
        ar_html += f'<div class="ar-text-en">{html.escape(reason_en)}</div>'
    if lang_mode in ["TA", "BOTH"] and reason_ta:
        ar_html += f'<div class="ar-text-ta tamil-text">{html.escape(reason_ta)}</div>'
    ar_html += "</div></div></section>"

    st.markdown(ar_html, unsafe_allow_html=True)


def _parse_ar(text: str):
    if not text:
        return "", ""
    
    a_match = re.search(r"Assertion\s*\(?A\)?\s*:\s*(.*?)(?=Reason\s*\(?R\)?\s*:|$)", text, re.IGNORECASE | re.DOTALL)
    r_match = re.search(r"Reason\s*\(?R\)?\s*:\s*(.*)", text, re.IGNORECASE | re.DOTALL)

    assertion = a_match.group(1).strip() if a_match else text
    reason = r_match.group(1).strip() if r_match else ""
    return assertion, reason


def _render_match_following_layout(q: NormalizedQuestion, lang_mode: str):
    _render_direct_mcq_layout(q, lang_mode)


def _render_chronology_layout(q: NormalizedQuestion, lang_mode: str):
    _render_direct_mcq_layout(q, lang_mode)
