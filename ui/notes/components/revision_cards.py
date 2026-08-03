import streamlit as st
from ui.notes.layout import section_anchor


def validate_flashcards(cards_data) -> bool:
    """Validates flashcards data structure before rendering."""
    if cards_data is None:
        print(
            "VALIDATION FAILED\n\n"
            "File: ui/notes/components/revision_cards.py\n"
            "Function: validate_flashcards\n"
            "Reason: cards_data payload is None"
        )
        return False
    return True


def _extract_str(val, default=""):
    """Recursively unpack string values from string, dict, or list structures."""
    if val is None:
        return default
    if isinstance(val, str):
        return val.strip()
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, dict):
        if "en" in val and val["en"]:
            return _extract_str(val["en"], default)
        if "ta" in val and val["ta"]:
            return _extract_str(val["ta"], default)
        for v in val.values():
            if v:
                res = _extract_str(v, default)
                if res:
                    return res
        return default
    if isinstance(val, list):
        items = [_extract_str(x) for x in val if x]
        if not items:
            return default
        if len(items) == 1:
            return items[0]
        return "\n".join(f"• {item}" for item in items)
    return str(val)


def _normalize_cards(cards_data) -> list:
    """Normalizes any input payload into a standardized list of dict cards with front, back, title, id."""
    if not cards_data:
        return []

    if isinstance(cards_data, dict):
        for key in ["flashcards", "revision_cards", "cards", "timeline", "important_facts"]:
            if key in cards_data and isinstance(cards_data[key], list):
                cards_data = cards_data[key]
                break
        else:
            cards_data = [cards_data]

    if not isinstance(cards_data, list):
        cards_data = [cards_data]

    normalized = []
    for idx, item in enumerate(cards_data):
        card_id = f"card_{idx + 1}"
        front = ""
        back = ""
        title = ""

        if isinstance(item, dict):
            card_id = _extract_str(item.get("id") or item.get("card_id"), f"card_{idx + 1}")

            front_raw = (
                item.get("flashcard_front")
                or item.get("front")
                or item.get("question")
                or item.get("title")
                or item.get("year")
                or item.get("fact")
                or item.get("concept")
            )
            front = _extract_str(front_raw, f"Flashcard #{idx + 1}")

            back_raw = (
                item.get("flashcard_back")
                or item.get("back")
                or item.get("one_line_revision")
                or item.get("answer")
                or item.get("points")
                or item.get("event")
                or item.get("details")
                or item.get("explanation")
                or item.get("description")
            )
            back = _extract_str(back_raw, "")

            title_raw = (
                item.get("title")
                if (item.get("front") or item.get("question") or item.get("flashcard_front"))
                else None
            )
            title = _extract_str(title_raw, "")
        else:
            front = f"Flashcard #{idx + 1}"
            back = _extract_str(item, "Details")
            title = ""

        if not front.strip():
            front = f"Flashcard #{idx + 1}"

        if not back.strip():
            back = front if front != f"Flashcard #{idx + 1}" else "No additional details available for this card."

        normalized.append({
            "id": card_id,
            "front": front,
            "back": back,
            "title": title
        })

    return normalized


def render_revision_cards(cards_data):
    """
    Renders Component 17: Interactive Flashcard UI
    Features: Tap to Reveal Answer/Fact, Next/Prev Swiper, State Persistence across reruns.
    """
    if not validate_flashcards(cards_data):
        st.error("VALIDATION FAILED: Invalid flashcards payload.")
        return

    cards = _normalize_cards(cards_data)
    total_cards = len(cards)

    if total_cards == 0:
        st.info("ℹ️ No flashcards available for this topic.")
        return

    if "flashcard_index" not in st.session_state:
        st.session_state.flashcard_index = st.session_state.get("current_flashcard_index", 0)

    if "flashcard_flipped" not in st.session_state:
        st.session_state.flashcard_flipped = st.session_state.get("flashcard_reveal", False)

    st.session_state.current_flashcard_index = st.session_state.flashcard_index
    st.session_state.flashcard_reveal = st.session_state.flashcard_flipped

    if st.session_state.flashcard_index >= total_cards:
        st.session_state.flashcard_index = max(0, total_cards - 1)
    if st.session_state.flashcard_index < 0:
        st.session_state.flashcard_index = 0

    st.session_state.current_flashcard_index = st.session_state.flashcard_index

    curr_idx = st.session_state.flashcard_index
    card = cards[curr_idx]
    card_id = card.get("id", f"card_{curr_idx + 1}")
    is_flipped = st.session_state.flashcard_flipped

    section_anchor("sec_revision_cards")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #FAFAF9; border-left: 5px solid #0284C7;">', unsafe_allow_html=True)
    st.markdown("### 🎴 **Interactive Flashcards / Revision Deck**")

    card_title = card.get("title", "")
    if card_title:
        st.markdown(f"**Card {curr_idx + 1} of {total_cards}** — *{card_title}*")
    else:
        st.markdown(f"**Card {curr_idx + 1} of {total_cards}**")

    card_content = card["back"] if is_flipped else card["front"]
    side_label = "BACK (ANSWER / REVISION)" if is_flipped else "FRONT (QUESTION / PROMPT)"
    formatted_content = card_content.replace("\n", "<br>")

    st.markdown(
        f"""
        <div class="nova-flashcard" style="padding: 1.5rem; border-radius: 12px; background: white; border: 1px solid #E2E8F0; margin-bottom: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <div style="font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; color:#0284C7; margin-bottom:0.5rem;">
                {side_label}
            </div>
            <div style="font-size:1.15rem; font-weight:600; color:#0F172A; line-height:1.6;">
                {formatted_content}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    def flip_card_cb():
        st.session_state.flashcard_flipped = not st.session_state.get("flashcard_flipped", False)
        st.session_state.flashcard_reveal = st.session_state.flashcard_flipped

    def prev_card_cb():
        st.session_state.flashcard_index = max(0, st.session_state.get("flashcard_index", 0) - 1)
        st.session_state.flashcard_flipped = False
        st.session_state.current_flashcard_index = st.session_state.flashcard_index
        st.session_state.flashcard_reveal = False

    def next_card_cb():
        st.session_state.flashcard_index = min(total_cards - 1, st.session_state.get("flashcard_index", 0) + 1)
        st.session_state.flashcard_flipped = False
        st.session_state.current_flashcard_index = st.session_state.flashcard_index
        st.session_state.flashcard_reveal = False

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("🔄 Flip / Reveal", key="btn_fc_flip", on_click=flip_card_cb, use_container_width=True)

    with col2:
        is_first = curr_idx <= 0
        st.button("⬅️ Previous", key="btn_fc_prev", on_click=prev_card_cb, disabled=is_first, use_container_width=True)

    with col3:
        is_last = curr_idx >= total_cards - 1
        st.button("Next ➡️", key="btn_fc_next", on_click=next_card_cb, disabled=is_last, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)
