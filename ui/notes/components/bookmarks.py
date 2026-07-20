import streamlit as st
from ui.notes.layout import section_anchor


def render_bookmarks(topic_name):
    """
    Renders Component 20a: Bookmarks Tool
    Allows bookmarking any section for later quick access.
    """
    section_anchor("sec_bookmarks")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #F8FAFC; border-left: 5px solid #64748B;">', unsafe_allow_html=True)
    st.markdown("### 🔖 **Bookmark Section & Quick Saver**")

    bookmarked_sections = st.session_state.get(f"bookmarks_{topic_name}", [])

    col1, col2 = st.columns([3, 1])
    with col1:
        new_bm = st.text_input("Add a custom bookmark note / anchor point:", key=f"inp_bm_{topic_name}")
    with col2:
        if st.button("➕ Save Bookmark", key=f"btn_save_bm_{topic_name}", use_container_width=True):
            if new_bm:
                bookmarked_sections.append(new_bm)
                st.session_state[f"bookmarks_{topic_name}"] = bookmarked_sections
                st.success("Saved!")

    if bookmarked_sections:
        st.markdown("**Your Saved Bookmarks for this Topic:**")
        for bm in bookmarked_sections:
            st.markdown(f"📍 {bm}")

    st.markdown("</div>", unsafe_allow_html=True)
