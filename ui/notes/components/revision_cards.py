import re
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
        en = _extract_str(val.get("en"))
        ta = _extract_str(val.get("ta"))
        if en and ta:
            return f"{en}\n\n(தமிழ்: {ta})"
        return en or ta or default
    if isinstance(val, list):
        items = [_extract_str(x) for x in val if x]
        if not items:
            return default
        if len(items) == 1:
            return items[0]
        return "\n".join(f"• {item}" for item in items)
    return str(val)


def _normalize_cards(cards_data) -> list:
    """
    Normalizes any input payload into a standardized list of dict cards:
    [{'id': ..., 'front': ..., 'back': ..., 'title': ...}]
    Handles list of dicts, list of strings, and dicts with 'en'/'ta' lists.
    """
    if not cards_data:
        return []

    # Case 1: Dict payload
    if isinstance(cards_data, dict):
        # 1a. If dict contains a list under standard keys, extract it
        for key in ["revision_cards", "flashcards", "cards", "timeline", "important_facts"]:
            if key in cards_data and isinstance(cards_data[key], list):
                cards_data = cards_data[key]
                break
        else:
            # 1b. If dict contains parallel "en" and "ta" lists of revision points (e.g. quick_revision, must_remember)
            en_list = cards_data.get("en", [])
            ta_list = cards_data.get("ta", [])
            if isinstance(en_list, list) or isinstance(ta_list, list):
                en_items = en_list if isinstance(en_list, list) else [en_list]
                ta_items = ta_list if isinstance(ta_list, list) else [ta_list]
                max_len = max(len(en_items), len(ta_items))
                card_list = []
                for i in range(max_len):
                    en_txt = _extract_str(en_items[i]) if i < len(en_items) else ""
                    ta_txt = _extract_str(ta_items[i]) if i < len(ta_items) else ""

                    front_txt = f"Revision Point #{i + 1}"
                    if ":" in en_txt and len(en_txt.split(":", 1)[0]) < 40:
                        parts = en_txt.split(":", 1)
                        front_txt = parts[0].strip()
                        en_txt = parts[1].strip()
                    if ":" in ta_txt and len(ta_txt.split(":", 1)[0]) < 40:
                        parts_ta = ta_txt.split(":", 1)
                        ta_txt = parts_ta[1].strip()

                    back_txt = en_txt
                    if ta_txt:
                        back_txt += f"\n\n(தமிழ்: {ta_txt})"

                    card_list.append({
                        "id": f"card_{i + 1}",
                        "front": front_txt,
                        "back": back_txt,
                        "title": f"Revision Point #{i + 1}"
                    })
                return card_list
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
            title = _extract_str(item.get("title") or item.get("topic"), "")

            # Front extraction
            front_en = (
                item.get("front_en")
                or item.get("front")
                or item.get("flashcard_front")
                or item.get("question")
                or item.get("fact_en")
                or item.get("concept")
            )
            front_ta = item.get("front_ta") or item.get("fact_ta")

            if front_en and front_ta:
                front = f"{_extract_str(front_en)}\n\n(தமிழ்: {_extract_str(front_ta)})"
            elif front_en:
                front = _extract_str(front_en)
            elif front_ta:
                front = _extract_str(front_ta)
            elif title:
                front = title
            else:
                front = f"Flashcard #{idx + 1}"

            # Back extraction
            back_en = (
                item.get("back_en")
                or item.get("back")
                or item.get("flashcard_back")
                or item.get("one_line_revision")
                or item.get("content_en")
                or item.get("answer")
                or item.get("points")
                or item.get("event")
                or item.get("details")
                or item.get("explanation")
                or item.get("description")
            )
            back_ta = item.get("back_ta") or item.get("content_ta")

            if back_en and back_ta:
                back = f"{_extract_str(back_en)}\n\n(தமிழ்: {_extract_str(back_ta)})"
            elif back_en:
                back = _extract_str(back_en)
            elif back_ta:
                back = _extract_str(back_ta)
            else:
                back = front if front != f"Flashcard #{idx + 1}" else "No additional details available for this card."
        else:
            front = f"Flashcard #{idx + 1}"
            back = _extract_str(item, "Details")

        normalized.append({
            "id": card_id,
            "front": front,
            "back": back,
            "title": title
        })

    return normalized


def render_revision_cards(cards_data):
    """
    Renders Component 17: Production-Grade Interactive Flashcard UI
    Features: Tap to Reveal Answer/Fact, Next/Prev Swiper, Stable Session State across reruns.
    """
    if not validate_flashcards(cards_data):
        st.error("VALIDATION FAILED: Invalid flashcards payload.")
        return

    cards = _normalize_cards(cards_data)
    total_cards = len(cards)

    if total_cards == 0:
        st.info("ℹ️ No flashcards available for this topic.")
        return

    # Determine stable topic / deck identifier
    topic_id = (
        st.session_state.get("selected_topic_id")
        or st.session_state.get("topic_id")
        or "default_deck"
    )
    clean_topic_id = re.sub(r"[^a-zA-Z0-9_]", "_", str(topic_id))

    deck_key = f"fc_deck_{clean_topic_id}"
    index_key = f"fc_index_{clean_topic_id}"
    flipped_key = f"fc_flipped_{clean_topic_id}"
    completed_key = f"fc_completed_{clean_topic_id}"

    # Initialize deck session state on topic change or initial load
    if st.session_state.get("active_fc_deck") != deck_key:
        st.session_state.active_fc_deck = deck_key
        st.session_state[index_key] = 0
        st.session_state[flipped_key] = False
        st.session_state[completed_key] = False

    if index_key not in st.session_state:
        st.session_state[index_key] = 0

    if flipped_key not in st.session_state:
        st.session_state[flipped_key] = False

    if completed_key not in st.session_state:
        st.session_state[completed_key] = False

    # Index safety clamping
    if st.session_state[index_key] >= total_cards:
        st.session_state[index_key] = max(0, total_cards - 1)
    if st.session_state[index_key] < 0:
        st.session_state[index_key] = 0

    curr_idx = st.session_state[index_key]
    is_flipped = st.session_state[flipped_key]

    # Global session state aliases for backward compatibility
    st.session_state.flashcard_cards = cards
    st.session_state.flashcard_index = curr_idx
    st.session_state.flashcard_flipped = is_flipped
    st.session_state.current_flashcard_index = curr_idx
    st.session_state.flashcard_reveal = is_flipped

    section_anchor("sec_revision_cards")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #FAFAF9; border-left: 5px solid #0284C7; margin-bottom: 2rem;">', unsafe_allow_html=True)
    st.markdown("### 🎴 **Interactive Flashcards / Revision Deck**")

    # Render Completion State if deck finished
    if st.session_state[completed_key]:
        st.markdown(
            """
            <div style="text-align: center; padding: 2.5rem 1.5rem; background: #F0FDF4; border-radius: 14px; border: 1px solid #BBF7D0; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎉</div>
                <h2 style="color: #166534; margin: 0 0 0.5rem 0; font-size: 1.5rem;">Revision Deck Complete!</h2>
                <p style="color: #15803D; font-size: 1rem; margin: 0;">You have successfully reviewed all cards in this topic.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        def restart_deck_cb():
            st.session_state[index_key] = 0
            st.session_state[flipped_key] = False
            st.session_state[completed_key] = False
            st.session_state.flashcard_index = 0
            st.session_state.flashcard_flipped = False

        def review_last_cb():
            st.session_state[completed_key] = False

        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.button("🔄 Restart Deck", key=f"btn_restart_{clean_topic_id}", on_click=restart_deck_cb, use_container_width=True)
        with col_res2:
            st.button("📜 Review Last Card", key=f"btn_review_last_{clean_topic_id}", on_click=review_last_cb, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)
        return

    card = cards[curr_idx]
    card_title = card.get("title", "")

    # Card Counter Display (e.g. Card 1 of 10)
    counter_html = f"**Card {curr_idx + 1} of {total_cards}**"
    if card_title:
        counter_html += f" — *{card_title}*"
    st.markdown(counter_html)

    # Card Content Display
    card_content = card["back"] if is_flipped else card["front"]
    side_label = "BACK (ANSWER / REVISION)" if is_flipped else "FRONT (QUESTION / PROMPT)"
    side_color = "#16A34A" if is_flipped else "#0284C7"
    formatted_content = card_content.replace("\n", "<br>")

    st.markdown(
        f"""
        <div class="nova-flashcard" style="padding: 1.5rem; border-radius: 14px; background: white; border: 2px solid {side_color}; margin-bottom: 1rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); min-height: 150px;">
            <div style="font-size:0.85rem; font-weight:800; text-transform:uppercase; letter-spacing:0.05em; color:{side_color}; margin-bottom:0.75rem;">
                {side_label}
            </div>
            <div style="font-size:1.15rem; font-weight:600; color:#0F172A; line-height:1.6;">
                {formatted_content}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Callback handlers for navigation and flip
    def flip_card_cb():
        st.session_state[flipped_key] = not st.session_state.get(flipped_key, False)
        st.session_state.flashcard_flipped = st.session_state[flipped_key]

    def prev_card_cb():
        st.session_state[index_key] = max(0, st.session_state.get(index_key, 0) - 1)
        st.session_state[flipped_key] = False
        st.session_state.flashcard_index = st.session_state[index_key]
        st.session_state.flashcard_flipped = False

    def next_card_cb():
        if st.session_state.get(index_key, 0) < total_cards - 1:
            st.session_state[index_key] += 1
            st.session_state[flipped_key] = False
            st.session_state.flashcard_index = st.session_state[index_key]
            st.session_state.flashcard_flipped = False
        else:
            st.session_state[completed_key] = True

    # Stable button widget keys
    key_flip = f"btn_fc_flip_{clean_topic_id}"
    key_prev = f"btn_fc_prev_{clean_topic_id}"
    key_next = f"btn_fc_next_{clean_topic_id}"

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("🔄 Flip / Reveal", key=key_flip, on_click=flip_card_cb, use_container_width=True)

    with col2:
        is_first = curr_idx <= 0
        st.button("⬅️ Previous", key=key_prev, on_click=prev_card_cb, disabled=is_first, use_container_width=True)

    with col3:
        is_last = curr_idx >= total_cards - 1
        button_label = "Finish 🎉" if is_last else "Next ➡️"
        st.button(button_label, key=key_next, on_click=next_card_cb, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)
