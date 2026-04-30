import streamlit as st

def generate_cards_from_notes(content):

    cards = []

    for section in content.values():
        if isinstance(section, list):
            for item in section:
                for en, ta in zip(
                    item["points"]["en"],
                    item["points"]["ta"]
                ):
                    cards.append({
                        "question": en,
                        "answer": ta
                    })

    return cards


def revision_cards(cards):

    if "card_index" not in st.session_state:
        st.session_state.card_index = 0

    idx = st.session_state.card_index
    card = cards[idx]

    st.subheader(card["question"])

    if st.button("👀 Show Answer"):
        st.success(card["answer"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Previous") and idx > 0:
            st.session_state.card_index -= 1

    with col2:
        if st.button("➡️ Next") and idx < len(cards)-1:
            st.session_state.card_index += 1