import streamlit as st
from core.mentor_chat import mentor_reply


def render_mentor(section, typing_effect, user):
    st.markdown("## 🤖 Nova Personal Mentor")
    section("🧑‍🏫 Personal Mentor")

    if "mentor_chat" not in st.session_state:
        st.session_state.mentor_chat = [
            {
                "role": "assistant",
                "content": f"Hello {user}! I am your Nova Mentor. How can I help you today?",
            }
        ]

    # Helper Chips
    st.write("Quick Topics:")
    cols = st.columns(4)
    chips = [
        "Weak Topic",
        "Rank",
        "Accuracy",
        "XP",
        "Level",
        "Revision",
        "Study Plan",
    ]

    for i, topic in enumerate(chips):
        if cols[i % 4].button(topic, key=f"chip_{topic}", use_container_width=True):
            st.session_state.mentor_chat.append({"role": "user", "content": topic})
            reply = mentor_reply(topic, user)
            st.session_state.mentor_chat.append({"role": "assistant", "content": reply})
            st.rerun()

    st.markdown("---")

    # Render Chat History
    for msg in st.session_state.mentor_chat:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Chat Input
    if prompt := st.chat_input("Ask your mentor"):
        st.session_state.mentor_chat.append({"role": "user", "content": prompt})
        reply = mentor_reply(prompt, user)
        st.session_state.mentor_chat.append({"role": "assistant", "content": reply})
        st.rerun()
