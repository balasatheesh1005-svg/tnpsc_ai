import pandas as pd
import streamlit as st

from core.weakness_ai import get_weakness


def render_weakness_page(section, user):
    section("🧠 Weakness")

    weak_data = get_weakness(user)

    if weak_data:

        # ---------------- DATAFRAME ----------------

        df = pd.DataFrame(list(weak_data.items()), columns=["Topic", "Weakness"])

        # ---------------- SPLIT ----------------

        df[["Subject", "Subtopic"]] = df["Topic"].str.split("-", expand=True)

        # ---------------- CLEAN ----------------

        df["Subtopic"] = df["Subtopic"].str.replace("_", " ").str.title()

        # ---------------- COLOR ----------------

        def color_map(val):

            if val >= 4:
                return "background-color:" "#ff4d4d;" "color:white"

            elif val >= 2:
                return "background-color:" "#ffc107"

            else:
                return "background-color:" "#28a745;" "color:white"

        # ---------------- BAR ----------------

        def bar(val):

            return "█" * int(val)

        # ---------------- APPLY ----------------

        df["Level"] = df["Weakness"].apply(bar)

        # ---------------- HEATMAP ----------------

        st.markdown("### 🔥 Weakness Heatmap")

        st.dataframe(
            df.style.map(color_map, subset=["Weakness"]), use_container_width=True
        )

        # ---------------- VISUAL ----------------

        st.markdown("### 📊 Visual Strength")

        st.table(df[["Subject", "Subtopic", "Level"]])

    else:

        st.success("🔥 No Weakness!")
