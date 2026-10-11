import os
import html
import re
import streamlit as st
from ui.question_engine.parser import NormalizedQuestion

ALLOWED_ASSET_ROOT = os.path.normpath("assets/questions/visual_reasoning")


def validate_image_path(path: str) -> bool:
    if not path or not isinstance(path, str):
        return False
    clean_path = path.strip()
    if not clean_path:
        return False
    # Reject external URLs or data URIs
    if clean_path.startswith(("http://", "https://", "data:")):
        return False
    # Reject absolute paths (Windows drive letter or leading slashes)
    if clean_path.startswith(("/", "\\")) or re.match(r"^[a-zA-Z]:", clean_path):
        return False
    # Reject path traversal
    normalized_rel = os.path.normpath(clean_path)
    if ".." in normalized_rel.replace("\\", "/").split("/"):
        return False
    # Path must be inside approved root
    clean_posix = clean_path.replace("\\", "/")
    if not clean_posix.startswith("assets/questions/visual_reasoning/"):
        return False
    # Must exist on disk
    if not (os.path.exists(clean_path) and os.path.isfile(clean_path)):
        return False
    return True


def _render_question_image(q: NormalizedQuestion):
    if not q.question_image:
        return

    if validate_image_path(q.question_image):
        st.image(
            q.question_image,
            caption=q.question_image_alt or None,
            use_container_width=True,
        )
    else:
        st.warning(f"⚠️ Question image unavailable ({q.question_image})")


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

    if q.question_image:
        _render_question_image(q)


def _render_direct_mcq_layout(q: NormalizedQuestion, lang_mode: str):
    en_text = q.question_en
    ta_text = q.question_ta

    if (lang_mode in ["EN", "BOTH"] and en_text and en_text != "Question text not available.") or (lang_mode in ["TA", "BOTH"] and ta_text):
        html_content = '<section class="nova-glass-card question-card">'
        if lang_mode in ["EN", "BOTH"] and en_text and en_text != "Question text not available.":
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
