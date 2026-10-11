import re
import streamlit as st
from ui.notes.layout import bilingual_panels, localized_section_title, section_anchor
from ui.notes.components.header import format_hero_display_title

LATEX_CMD_RE = re.compile(r'\\[a-zA-Z]+|[\^{}]')


def clean_fallback_text(s: str) -> str:
    """Fallback text cleaning for raw LaTeX commands."""
    if not s or not isinstance(s, str):
        return ""
    s = re.sub(r'\\text\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\frac\{([^}]*)\}\{([^}]*)\}', r'(\1 / \2)', s)
    s = re.sub(r'\\sqrt\{([^}]*)\}', r'√(\1)', s)
    s = s.replace(r'\times', '×').replace(r'\div', '÷').replace(r'\quad', '  ').replace(r'\qquad', '    ')
    s = s.replace(r'\cdot', '·').replace(r'\pi', 'π').replace(r'\sum', 'Σ').replace(r'\Delta', 'Δ')
    s = s.replace(r'\iff', '⇔').replace(r'\implies', '⇒').replace(r'\leftarrow', '←').replace(r'\rightarrow', '→')
    s = s.replace(r'\le', '≤').replace(r'\ge', '≥').replace(r'\neq', '≠').replace(r'\approx', '≈')
    s = s.replace(r'\left', '').replace(r'\right', '')
    s = s.replace(r'\\', '\n')
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    s = re.sub(r'[{}]', '', s)
    return s.strip()


def render_safe_formula(formula_val):
    """
    Renders a formula safely using KaTeX if valid LaTeX, 
    plain text if no LaTeX commands, 
    or cleaned fallback if malformed.
    """
    if not formula_val or not isinstance(formula_val, str):
        return

    f_str = formula_val.strip()
    if not f_str:
        return

    has_latex_cmd = bool(LATEX_CMD_RE.search(f_str))

    if not has_latex_cmd:
        st.markdown(
            f'<div style="background-color: #F8FAFC; border-left: 4px solid #2563EB; padding: 10px 14px; margin: 6px 0; border-radius: 6px; font-family: ui-monospace, monospace; font-size: 1.02rem; color: #0F172A;">{f_str}</div>',
            unsafe_allow_html=True,
        )
        return

    if (f_str.startswith("$$") and f_str.endswith("$$")) or (f_str.startswith("$") and f_str.endswith("$")):
        latex_expr = f_str
    else:
        latex_expr = f"$$\n{f_str}\n$$"

    try:
        st.markdown(latex_expr)
    except Exception:
        cleaned = clean_fallback_text(f_str)
        st.markdown(
            f'<div style="background-color: #F8FAFC; border-left: 4px solid #2563EB; padding: 10px 14px; margin: 6px 0; border-radius: 6px; font-family: ui-monospace, monospace; font-size: 1.02rem; color: #0F172A;">{cleaned}</div>',
            unsafe_allow_html=True,
        )


def render_definition(definition_data):
    """
    Renders Component 2: Bilingual Definition Card
    Theme Accent: Blue (#2563EB)
    """
    if not definition_data:
        return

    section_anchor("sec_definition")
    st.markdown('<div class="nova-card nova-definition-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown(f"### 📘 **{localized_section_title('Definition & Core Concept')}**")

    if isinstance(definition_data, dict):
        en_text = definition_data.get("en", "")
        ta_text = definition_data.get("ta", "")

        for language, panel in bilingual_panels(en_text, ta_text):
            with panel:
                text = en_text if language == "en" else ta_text
                st.markdown(
                    f'<p style="font-size: 1.05rem; line-height: 1.6; color: #1E293B;">{text}</p>',
                    unsafe_allow_html=True,
                )
    elif isinstance(definition_data, str):
        st.markdown(f'<p style="font-size: 1.05rem; line-height: 1.6;">{definition_data}</p>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def render_formula_sheet(formula_data):
    """
    Renders Component 7: Formula Sheet
    Supports LaTeX math rendering, mixed text/math, plain text formulas.
    """
    if not formula_data:
        return

    section_anchor("sec_formula_sheet")
    st.markdown('<div class="nova-card nova-formula-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown(f"### 📐 **{localized_section_title('Formula Sheet')}**")

    if isinstance(formula_data, list):
        total_items = len(formula_data)
        for idx, item in enumerate(formula_data, 1):
            if isinstance(item, dict):
                title = item.get("title") or item.get("name") or f"Formula {idx}"
                st.markdown(f"##### **{title}**")

                formula_val = item.get("formula") or item.get("expression") or item.get("value")
                if formula_val:
                    render_safe_formula(formula_val)

                explanation = item.get("explanation")
                if explanation:
                    if isinstance(explanation, dict):
                        en_exp = explanation.get("en", "")
                        ta_exp = explanation.get("ta", "")
                        for lang, panel in bilingual_panels(en_exp, ta_exp):
                            with panel:
                                exp_text = en_exp if lang == "en" else ta_exp
                                if exp_text:
                                    st.markdown(f'<p style="color: #475569; font-size: 0.95rem; margin-top: 4px;">{exp_text}</p>', unsafe_allow_html=True)
                    elif isinstance(explanation, str):
                        st.markdown(f'<p style="color: #475569; font-size: 0.95rem; margin-top: 4px;">{explanation}</p>', unsafe_allow_html=True)

                if idx < total_items:
                    st.markdown("<hr style='margin: 12px 0; border: none; border-top: 1px solid #E2E8F0;' />", unsafe_allow_html=True)

            elif isinstance(item, str):
                render_safe_formula(item)
    elif isinstance(formula_data, dict):
        for key, val in formula_data.items():
            st.markdown(f"##### **{format_hero_display_title(key)}**")
            if isinstance(val, str):
                render_safe_formula(val)
            elif isinstance(val, dict):
                formula_val = val.get("formula") or val.get("expression") or str(val)
                render_safe_formula(formula_val)

    st.markdown("</div>", unsafe_allow_html=True)

