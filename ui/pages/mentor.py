import streamlit as st


def render_mentor(section, typing_effect, user):
    st.markdown("## 🤖 Your Personal AI Mentor")
    section("🧑‍🏫 Personal Mentor")

    from core.mentor_ai import mentor_advice

    msg = mentor_advice(user)

    st.success(msg)
    # 🔔 notification clear
    if st.session_state.get("mentor_notification"):
        st.success("🎯 New guidance available!")
        st.session_state["mentor_notification"] = False

    # 💬 chat history show
    for msg in st.session_state.mentor_chat:

        if msg["role"] == "assistant":
            with st.chat_message("assistant"):
                typing_effect(msg["content"])  # 🔥 HERE

        else:
            st.chat_message("user").write(msg["content"])

    # 🧠 user reply
    user_msg = st.chat_input("Ask your mentor...")

    if user_msg:
        st.session_state.mentor_chat.append({"role": "user", "content": user_msg})

        from core.ai_teacher import ai_teacher

        reply = ai_teacher(user_msg, user)

        st.session_state.mentor_chat.append({"role": "assistant", "content": reply})

        st.rerun()
