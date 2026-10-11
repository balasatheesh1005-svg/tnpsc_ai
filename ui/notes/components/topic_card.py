import re
import streamlit as st
from ui.notes.layout import bilingual_panels, localized_section_title, localized_title, section_anchor
from ui.notes.components.definition import render_safe_formula

LATEX_CMD_RE = re.compile(r'\\[a-zA-Z]+|[\^{}]')


FIELD_LABEL_MAP = {
    "meanings": ("Meanings", "பொருள் / வேறுபாடு"),
    "distinction": ("Distinction", "பொருள் வேறுபாடு"),
    "foreign_word": ("Foreign Word", "பிறமொழிச் சொல்"),
    "pure_tamil": ("Pure Tamil", "தூய தமிழ்"),
    "word": ("Word", "சொல்"),
    "antonym": ("Antonym", "எதிர்ச்சொல்"),
    "feature": ("Feature", "சிறப்பு / இலக்கணம்"),
    "explanation": ("Explanation", "விளக்கம்"),
    "split": ("Split Form", "பிரித்தல்"),
    "rule": ("Grammar Rule", "புணர்ச்சி விதி"),
    "root": ("Root Word", "வேர்ச்சொல்"),
    "derived": ("Derived Word", "உருவான சொல்"),
    "finite_verb": ("Finite Verb", "வினைமுற்று"),
    "relative_participle": ("Relative Participle", "பெயரெச்சம்"),
    "verbal_participle": ("Verbal Participle", "வினையெச்சம்"),
    "participial_noun": ("Participial Noun", "வினையாலணையும் பெயர்"),
    "incorrect": ("Incorrect Form", "தவறான வடிவம்"),
    "correct": ("Correct Form", "சரியான வடிவம்"),
    "reason": ("Reason", "காரணம்"),
    "example": ("Example", "எடுத்துக்காட்டு"),
    "pair": ("Word Group", "சொற்கள்"),
}


def _extract_header_text(item: dict, default_index: int) -> tuple[str, str]:
    """
    Derives meaningful title from item dictionary across Tamil-only and bilingual schemas.
    Returns (header_text, title_key_used).
    """
    title_ta = item.get("title_ta", "")

    # Priority key list for titles
    title_keys = [
        "title",
        "pair",
        "word",
        "foreign_word",
        "root",
        "derived",
        "incorrect",
        "heading",
        "name",
        "concept",
    ]

    for key in title_keys:
        val = item.get(key)
        if val and isinstance(val, str) and val.strip():
            header = localized_title(val.strip(), title_ta) if title_ta else val.strip()
            return header, key

    # Fallback to English title if available
    en_title = item.get("title_en", "")
    if en_title:
        header = localized_title(en_title, title_ta)
        return header, "title_en"

    return f"Item {default_index + 1}", ""


def _render_dict_item_body(item: dict, title_key: str):
    """
    Renders all meaningful available fields inside an expanded card item.
    Avoids raw JSON dumps and handles custom domain key-value pairs cleanly.
    """
    points = item.get("points")
    if isinstance(points, dict):
        en_pts = points.get("en", [])
        ta_pts = points.get("ta", [])
        for language, panel in bilingual_panels(en_pts, ta_pts):
            with panel:
                for point in en_pts if language == "en" else ta_pts:
                    st.markdown(f"• {point}")
        return

    elif isinstance(points, list):
        for point in points:
            st.markdown(f"• {point}")
        return

    elif "content_en" in item or "content_ta" in item:
        content_en = item.get("content_en", "")
        content_ta = item.get("content_ta", "")
        for language, panel in bilingual_panels(content_en, content_ta):
            with panel:
                st.write(content_en if language == "en" else content_ta)
        return

    elif "question" in item:
        st.markdown(f"**Question:** {item.get('question')}")
        if "solution" in item:
            st.markdown(f"**Solution:** `{item.get('solution')}`")
        if "answer" in item:
            st.success(f"**Answer:** {item.get('answer')}")
        return

    # Generic domain-specific key-value renderer
    skip_keys = {"title", "title_en", "title_ta", "heading", "id", "part_id", "node_id", "card_id", title_key}
    remaining_keys = [k for k in item.keys() if k not in skip_keys and item.get(k)]

    if not remaining_keys:
        val = item.get(title_key)
        if val and title_key != "title":
            st.markdown(f"{val}")
        return

    for key in remaining_keys:
        val = item.get(key)
        if not val:
            continue

        label_en, label_ta = FIELD_LABEL_MAP.get(
            key, (key.replace("_", " ").title(), key.replace("_", " ").title())
        )
        display_label = localized_title(label_en, label_ta)

        if isinstance(val, str):
            if key.lower() in ("formula", "formulas", "expression") or LATEX_CMD_RE.search(val):
                st.markdown(f"**{display_label}:**")
                render_safe_formula(val)
            elif " | " in val:
                st.markdown(f"**📌 {display_label}:**")
                parts = [p.strip() for p in val.split(" | ") if p.strip()]
                for p in parts:
                    if "=" in p:
                        left, right = p.split("=", 1)
                        st.markdown(f"- **{left.strip()}**: {right.strip()}")
                    else:
                        st.markdown(f"- {p}")
            elif "=" in val and len(val.split("=")) == 2 and not val.startswith("http"):
                left, right = val.split("=", 1)
                st.markdown(f"**{display_label}:** **{left.strip()}** ➔ {right.strip()}")
            else:
                st.markdown(f"**{display_label}:** {val}")
        elif isinstance(val, list):
            st.markdown(f"**📌 {display_label}:**")
            for sub_item in val:
                st.markdown(f"- {sub_item}")
        elif isinstance(val, dict):
            en_val = val.get("en", "")
            ta_val = val.get("ta", "")
            if en_val or ta_val:
                for language, panel in bilingual_panels(en_val, ta_val):
                    with panel:
                        st.write(en_val if language == "en" else ta_val)
            else:
                st.write(val)
        else:
            st.markdown(f"**{display_label}:** {val}")


def render_topic_cards(section_key, section_data, section_meta=None):
    """
    Renders Component 7: Expandable Topic Cards with nested subtopics and media support.
    """
    if not section_data:
        return

    section_meta = section_meta if isinstance(section_meta, dict) else {}
    raw_title = section_meta.get("title_en") or section_key.replace("_", " ").title()
    sec_title = localized_title(raw_title, section_meta.get("title_ta", "")) if section_meta.get("title_ta") else localized_section_title(raw_title)
    section_anchor(f"sec_{section_key}")

    st.markdown(f"### 📌 **{sec_title}**")

    if isinstance(section_data, list):
        for idx, item in enumerate(section_data):
            if isinstance(item, dict):
                header_text, title_key = _extract_header_text(item, idx)

                with st.expander(f"🔹 {header_text}", expanded=(idx == 0)):
                    _render_dict_item_body(item, title_key)

            elif isinstance(item, str):
                st.markdown(f"• {item}")
    elif isinstance(section_data, dict):
        with st.expander(f"🔹 {sec_title}", expanded=True):
            en_pts = section_data.get("en", [])
            ta_pts = section_data.get("ta", [])
            if isinstance(en_pts, list) or isinstance(ta_pts, list):
                en_values = en_pts if isinstance(en_pts, list) else [en_pts]
                ta_values = ta_pts if isinstance(ta_pts, list) else [ta_pts]
                for language, panel in bilingual_panels(en_values, ta_values):
                    with panel:
                        for point in en_values if language == "en" else ta_values:
                            st.markdown(f"• {point}")
            else:
                _render_dict_item_body(section_data, "")

    st.markdown("---")

