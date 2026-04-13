import streamlit as st

from core.weakness_ai import get_weakness
from core.revision_ai import get_revision_topics

user = "satheesh"
def show_dashboard(user):

    st.title("📊 Your Dashboard")

    # -------------------------------
    # WEAKNESS SECTION
    # -------------------------------
    st.markdown("## 🧠 Your Weak Topics")

    weak_data = get_weakness(user)

    if not weak_data:
        st.success("🔥 No Weakness! Super!")
    else:
        for topic, count in weak_data.items():
            st.write(f"{topic} → ❌ {count}")

    # -------------------------------
    # SMART REVISION 🔁
    # -------------------------------
    st.markdown("## 🔁 Smart Revision")

    rev_topics = get_revision_topics(user)

    if not rev_topics:
        st.success("🔥 No revision needed")
    else:
        for t in rev_topics:
            st.write(f"🔁 Revise: {t}")

from core.streak_ai import get_streak

st.markdown("## 📊 Smart Dashboard")

streak = get_streak(user)
st.info(f"🔥 Streak: {streak} days")

# Weak focus
weak = get_weakness(user)

if weak:
    top_weak = max(weak, key=weak.get)
    st.warning(f"⚠️ Focus Today: {top_weak}")
else:
    st.success("🔥 No weak topics!")            