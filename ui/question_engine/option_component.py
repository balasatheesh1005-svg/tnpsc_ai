from typing import List, Tuple
import streamlit as st
from ui.question_engine.parser import NormalizedQuestion, OptionItem


def render_option_cards(
    q: NormalizedQuestion,
    prefix: str,
    disabled: bool = False,
    selected_option_key: str = "",
) -> Tuple[str, List[str]]:
    lang_mode = st.session_state.get(f"{prefix}_lang_mode", "BOTH")
    options = q.options

    if not options:
        st.info("Options are not available for this question.")
        return "", []

    # Build formatted option label choices for radio button
    option_labels = []
    opt_map = {}  # formatted_label -> OptionItem.id

    for opt in options:
        opt_id = opt.id
        display_text = opt.get_display_text(lang_mode)
        formatted_label = f"{opt_id}. {display_text}"
        option_labels.append(formatted_label)
        opt_map[formatted_label] = opt_id

    # Determine default index
    default_idx = 0
    if selected_option_key:
        for idx, opt in enumerate(options):
            if opt.id == selected_option_key:
                default_idx = idx
                break

    radio_key = f"{prefix}_radio_{q.id}"
    selected_label = st.radio(
        "Select the best answer",
        option_labels,
        index=default_idx,
        key=radio_key,
        disabled=disabled,
        label_visibility="collapsed",
    )

    chosen_key = opt_map.get(selected_label, "")
    return chosen_key, option_labels
