import streamlit as st
from ui.notes.layout import section_anchor


def render_revision_cards(cards_data):
    """
    Renders Component 17: Interactive Flashcard UI
    Features: Tap to Reveal Answer/Fact, Next Card Swiper, Spaced Repetition Readiness.
    """
    if not cards_data:
        return

    section_anchor("sec_revision_cards")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #FAFAF9; border-left: 5px solid #0284C7;">', unsafe_allow_html=True)
    st.markdown("### 🎴 **Interactive Flashcards / Revision Deck**")

    # State key for current card index
    card_idx_key = "flashcard_idx"
    reveal_key = "flashcard_reveal"

    if card_idx_key not in st.session_state:
        st.session_state[card_idx_key] = 0
    if reveal_key not in st.session_state:
        st.session_state[reveal_key] = False

    total_cards = len(cards_data)
    curr_idx = st.session_state[card_idx_key] % max(total_cards, 1)
    card_item = cards_data[curr_idx] if curr_idx < total_cards else {}

    # Extract front and back of card
    if isinstance(card_item, dict):
        front = card_item.get("front", card_item.get("title", card_item.get("year", "Key Term")))
        back = card_item.get("back", card_item.get("points", card_item.get("event", "Details")))
        if isinstance(back, dict):
            back = ", ".join(back.get("en", []))
    elif isinstance(card_item, str):
        front = f"Flashcard #{curr_idx + 1}"
        back = card_item
    else:
        front = f"Flashcard #{curr_idx + 1}"
        back = str(card_item)

    # Render Flashcard UI container
    st.markdown(f"**Card {curr_idx + 1} of {total_cards}**")
    
    card_container = st.container()
    with card_container:
        st.markdown(
            f"""
            <div class="nova-flashcard">
                <div style="font-size:0.85rem; text-transform:uppercase; letter-spacing:0.05em; color:#64748B; margin-bottom:0.5rem;">
                    {'BACK (ANSWER)' if st.session_state[reveal_key] else 'FRONT (QUESTION / PROMPT)'}
                </div>
                <div style="font-size:1.25rem; font-weight:700; color:#0F172A;">
                    {back if st.session_state[reveal_key] else front}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 Flip / Reveal", key="btn_fc_flip", use_container_width=True):
            st.session_state[reveal_key] = not st.session_state[reveal_key]
            st.rerun()
    with col2:
        if st.button("⬅️ Previous", key="btn_fc_prev", use_container_width=True):
            st.session_state[card_idx_key] = (curr_idx - 1) % max(total_cards, 1)
            st.session_state[reveal_key] = False
            st.rerun()
    with col3:
        if st.button("Next ➡️", key="btn_fc_next", use_container_width=True):
            st.session_state[card_idx_key] = (curr_idx + 1) % max(total_cards, 1)
            st.session_state[reveal_key] = False
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
