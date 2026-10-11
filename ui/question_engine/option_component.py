from typing import List, Tuple
import streamlit as st
from ui.question_engine.parser import NormalizedQuestion, OptionItem
from ui.question_engine.body_component import validate_image_path


def render_option_cards(
    q: NormalizedQuestion,
    prefix: str,
    disabled: bool = False,
    selected_option_key: str = "",
) -> Tuple[str, List[str]]:
    lang_mode = st.session_state.get(f"{prefix}_lang_mode", "BOTH")
    options = q.options

    if not options and not (q.option_images and any(q.option_images.values())):
        st.info("Options are not available for this question.")
        return "", []

    # Check if option images are present
    has_images = bool(q.option_images and isinstance(q.option_images, dict) and any(v for v in q.option_images.values() if v))

    if has_images:
        return _render_visual_option_cards(
            q=q,
            prefix=prefix,
            disabled=disabled,
            selected_option_key=selected_option_key,
            lang_mode=lang_mode,
        )

    # Standard Text Option Cards
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


def _render_visual_option_cards(
    q: NormalizedQuestion,
    prefix: str,
    disabled: bool = False,
    selected_option_key: str = "",
    lang_mode: str = "BOTH",
) -> Tuple[str, List[str]]:
    option_keys = ["A", "B", "C", "D"]
    opt_images = q.option_images or {}
    opt_alts = q.option_images_alt or {}
    options = q.options or []

    # Mobile-first 2x2 grid rendering
    r1_col1, r1_col2 = st.columns(2)
    r2_col1, r2_col2 = st.columns(2)
    grid_cols = [r1_col1, r1_col2, r2_col1, r2_col2]

    for idx, opt_id in enumerate(option_keys):
        col = grid_cols[idx]
        with col:
            img_path = opt_images.get(opt_id)
            img_alt = opt_alts.get(opt_id)

            # Match OptionItem if text is also provided
            opt_item = next((o for o in options if o.id == opt_id), None)
            opt_text = opt_item.get_display_text(lang_mode) if opt_item else ""

            st.markdown(f"**Option {opt_id}**")
            if img_path and validate_image_path(img_path):
                st.image(img_path, caption=img_alt or None, use_container_width=True)
            elif img_path:
                st.warning(f"⚠️ Image {opt_id} missing")

            if opt_text and opt_text != "Question text not available.":
                st.caption(opt_text)

    # Selection Radio Button
    radio_choices = []
    opt_map = {}
    for opt_id in option_keys:
        label = f"Option {opt_id}"
        radio_choices.append(label)
        opt_map[label] = opt_id

    default_idx = 0
    if selected_option_key and selected_option_key in option_keys:
        default_idx = option_keys.index(selected_option_key)

    radio_key = f"{prefix}_radio_{q.id}"
    selected_label = st.radio(
        "Select the best answer",
        radio_choices,
        index=default_idx,
        key=radio_key,
        disabled=disabled,
        label_visibility="collapsed",
    )

    chosen_key = opt_map.get(selected_label, "A")
    return chosen_key, radio_choices
