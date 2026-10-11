from contextlib import nullcontext

import streamlit as st


NOTES_LANGUAGE_OPTIONS = ["English", "தமிழ்", "Both"]


def get_notes_language_mode() -> str:
    """Return the normalized Notes display-language preference."""
    mode = str(st.session_state.get("notes_language_mode", "Both"))
    return mode if mode in NOTES_LANGUAGE_OPTIONS else "Both"


def render_language_control(scope: str) -> str:
    """Render one stable Notes-level English/Tamil/Both selector."""
    from core.navigation_v2.navigation_state import get_selected_subject

    if get_selected_subject().lower() == "general_tamil":
        st.session_state["notes_language_mode"] = "தமிழ்"
        st.markdown(
            '<div style="margin-bottom: 15px;"><span class="progress-pill" style="background:#F0FDF4; color:#166534; border:1px solid #BBF7D0; font-weight:700;">🌐 தமிழ் வழி கற்றல் (General Tamil — Tamil-Only Mode)</span></div>',
            unsafe_allow_html=True,
        )
        return "தமிழ்"

    clean_scope = "".join(ch if ch.isalnum() or ch == "_" else "_" for ch in str(scope))
    widget_key = f"notes_language_selector_{clean_scope}"
    current_mode = get_notes_language_mode()
    if widget_key not in st.session_state:
        st.session_state[widget_key] = current_mode

    mode = st.radio(
        "🌐 Display Language",
        NOTES_LANGUAGE_OPTIONS,
        horizontal=True,
        key=widget_key,
    )
    st.session_state["notes_language_mode"] = mode
    return mode


def _has_language_value(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, dict, set)):
        return bool(value)
    return True


def bilingual_panels(
    english_value,
    tamil_value,
    english_label: str = "🇬🇧 English",
    tamil_label: str = "🇮🇳 தமிழ்",
):
    """Return the language panels appropriate for the active Notes mode."""
    has_english = _has_language_value(english_value)
    has_tamil = _has_language_value(tamil_value)
    mode = get_notes_language_mode()

    if mode == "English":
        return [("en", nullcontext())] if has_english else [("ta", nullcontext())] if has_tamil else []
    if mode == "தமிழ்":
        return [("ta", nullcontext())] if has_tamil else [("en", nullcontext())] if has_english else []
    if has_english and has_tamil:
        english_tab, tamil_tab = st.tabs([english_label, tamil_label])
        return [("en", english_tab), ("ta", tamil_tab)]
    if has_english:
        return [("en", nullcontext())]
    if has_tamil:
        return [("ta", nullcontext())]
    return []


SECTION_TITLE_MAP = {
    "Definition & Core Concept": ("Definition & Core Concept", "வரையறை & அடிப்படைக் கருத்து"),
    "Definition": ("Definition", "வரையறை & அடிப்படைக் கருத்து"),
    "Grammar Rules": ("Grammar Rules", "இலக்கண விதிகள்"),
    "Confusing Word Bank": ("Confusing Word Bank", "குழப்பமான சொற்கள் & பொருள் வேறுபாடு"),
    "Vocabulary Bank": ("Vocabulary Bank", "சொற்களஞ்சியம்"),
    "Word Bank": ("Word Bank", "சொல் வங்கி"),
    "Error Spotting & Corrections": ("Error Spotting & Corrections", "பிழை திருத்தம் & பயிற்சி"),
    "Error Spotting": ("Error Spotting", "பிழை திருத்தம் & பயிற்சி"),
    "Important Fact Box": ("Important Fact Box", "முக்கிய தகவல்கள்"),
    "Fact Box": ("Fact Box", "முக்கிய தகவல்கள்"),
    "Quick Revision Bullet Summary": ("Quick Revision Bullet Summary", "விரைவு மீள்பார்வை"),
    "Quick Revision": ("Quick Revision", "விரைவு மீள்பார்வை"),
    "TNPSC Trap Points — Common Student Mistakes": ("TNPSC Trap Points — Common Student Mistakes", "TNPSC தேர்வுப் பொறிகள் — பொதுவான தவறுகள்"),
    "Trap Points": ("Trap Points", "TNPSC தேர்வுப் பொறிகள் — பொதுவான தவறுகள்"),
    "Interactive Flashcards / Revision Deck": ("Interactive Flashcards / Revision Deck", "மீள்பார்வை அட்டைகள்"),
    "Revision Cards": ("Revision Cards", "மீள்பார்வை அட்டைகள்"),
    "Interactive Mind Map / Concept Flowchart": ("Interactive Mind Map / Concept Flowchart", "நினைவுக் கருத்துப்படம்"),
    "Mind Map": ("Mind Map", "நினைவுக் கருத்துப்படம்"),
    "Topic Breakdown": ("Topic Breakdown", "பாடப் பகுப்பாய்வு"),
    "Knowledge Graph": ("Knowledge Graph", "அறிவுக் வரைபடம்"),
}


def localized_title(english_title: str, tamil_title: str = "") -> str:
    """Choose a section title without discarding an available translation."""
    english_title = str(english_title or "").strip()
    tamil_title = str(tamil_title or "").strip()
    mode = get_notes_language_mode()
    if mode == "English":
        return english_title or tamil_title
    if mode == "தமிழ்":
        return tamil_title or english_title
    if english_title and tamil_title and english_title != tamil_title:
        return f"{english_title} / {tamil_title}"
    return english_title or tamil_title


def localized_section_title(title: str) -> str:
    """Localized section title mapped per language preference."""
    if title in SECTION_TITLE_MAP:
        en_t, ta_t = SECTION_TITLE_MAP[title]
        return localized_title(en_t, ta_t)
    clean_title = title.strip().replace("_", " ").title()
    if clean_title in SECTION_TITLE_MAP:
        en_t, ta_t = SECTION_TITLE_MAP[clean_title]
        return localized_title(en_t, ta_t)
    return localized_title(title, "")



def render_bottom_actions(subject, topic):
    """
    Renders the standardized Bottom Actions Bar for TNPSC Nova AI Notes Engine.
    Actions: Practice MCQ, Revision Cards, Ask AI, Bookmark, Share
    """
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("### 🚀 **Quick Actions**")

    st.markdown(
        """
        <style>
        @media (max-width: 640px) {
            div[data-testid="stHorizontalBlock"]:has(.notes-bottom-actions-marker) {
                flex-direction: column !important;
                gap: 8px !important;
            }
            div[data-testid="stHorizontalBlock"]:has(.notes-bottom-actions-marker) > div[data-testid="column"] {
                width: 100% !important;
                min-width: 100% !important;
                flex: 1 1 100% !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown('<span class="notes-bottom-actions-marker" style="display:none;"></span>', unsafe_allow_html=True)
        if st.button("🧠 Practice MCQ", key="btn_bottom_practice", use_container_width=True):
            st.session_state.test_subject = subject
            st.session_state.test_topic = topic
            st.session_state.notes_practice_trigger = True
            st.success("🎯 Practice session initialized!")

    with col2:
        if st.button("🎴 Flashcards", key="btn_bottom_flashcards", use_container_width=True):
            st.session_state.show_revision_cards = not st.session_state.get("show_revision_cards", False)

    with col3:
        if st.button("🤖 Ask AI Teacher", key="btn_bottom_ai", use_container_width=True):
            st.session_state.ai_teacher_active = True
            st.info("💡 AI Teacher activated. Ask any question below!")

    with col4:
        is_bookmarked = st.session_state.get(f"bookmark_{topic}", False)
        bookmark_label = "🔖 Bookmarked" if is_bookmarked else "🔖 Bookmark"
        if st.button(bookmark_label, key="btn_bottom_bookmark", use_container_width=True):
            st.session_state[f"bookmark_{topic}"] = not is_bookmarked
            st.rerun()

    with col5:
        if st.button("📤 Share Note", key="btn_bottom_share", use_container_width=True):
            st.toast(f"📋 Link copied for topic: {topic}")


def section_anchor(sec_id):
    """Helper to inject an HTML anchor target for TOC navigation."""
    st.markdown(f'<div id="{sec_id}"></div>', unsafe_allow_html=True)
