import json
import os
import re
from pathlib import Path
import streamlit as st

from core.navigation_v2.navigation_state import (
    discover_note_parts,
    get_selected_display_title,
    get_selected_repository_id,
    get_selected_subject,
    get_selected_topic_id,
)
from core.streamlit_ui_engine import render_notes
from ui.notes.layout import get_notes_language_mode


@st.cache_data
def load_note(file_path: str, mtime: float = 0):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return None


def render_2_minute_revision_card(data: dict, display_title: str, subject: str):
    """Renders the 2-Minute Quick Revision Card at the bottom of Notes."""
    content = data.get("content", data) if isinstance(data, dict) else {}
    content = content if isinstance(content, dict) else {}

    def localized_items(value):
        if not isinstance(value, dict):
            if isinstance(value, list):
                return [str(item) for item in value if item]
            return [str(value)] if value else []

        english = value.get("en", [])
        tamil = value.get("ta", [])
        english = english if isinstance(english, list) else [english] if english else []
        tamil = tamil if isinstance(tamil, list) else [tamil] if tamil else []
        mode = get_notes_language_mode()
        if mode == "English":
            return [str(item) for item in english if item]
        if mode == "தமிழ்":
            return [str(item) for item in tamil if item]

        paired = []
        for index in range(max(len(english), len(tamil))):
            en_text = str(english[index]) if index < len(english) and english[index] else ""
            ta_text = str(tamil[index]) if index < len(tamil) and tamil[index] else ""
            if en_text and ta_text:
                paired.append(f"{en_text}  \n_{ta_text}_")
            elif en_text or ta_text:
                paired.append(en_text or ta_text)
        return paired

    st.markdown("---")
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%); padding: 18px 22px; border-radius: 14px; color: white; margin-bottom: 20px; border: 1px solid #334155;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <div>
                    <span class="progress-pill" style="background:#DCFCE7; color:#15803D; font-weight:800; font-size:0.8rem;">
                        ✅ Notes Completed
                    </span>
                    <h3 style="margin: 8px 0 2px 0; color: #F8FAFC; font-size: 1.35rem;">⚡ 2-Minute Quick Revision</h3>
                    <p style="color: #94A3B8; font-size: 0.85rem; margin: 0;">
                        Rapid key points summary for <b>{display_title}</b> before starting practice.
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="medium")

    # 1. Key Points
    with col1:
        st.markdown(
            """
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #2563EB; padding: 14px; border-radius: 10px; margin-bottom: 12px;">
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 0.98rem;">• Key Points</h4>
            """,
            unsafe_allow_html=True,
        )
        key_pts = []
        if isinstance(data, dict):
            outcomes = data.get("learning_outcomes", {}).get("Understand", {})
            key_pts.extend(localized_items(outcomes)[:3])
            if len(key_pts) < 3:
                key_pts.extend(localized_items(content.get("quick_revision", {}))[: 3 - len(key_pts)])

        for pt in key_pts[:3]:
            st.markdown(f"- {pt}")
        st.markdown("</div>", unsafe_allow_html=True)

    # 2. Important Facts
    with col2:
        st.markdown(
            """
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #16A34A; padding: 14px; border-radius: 10px; margin-bottom: 12px;">
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 0.98rem;">• Important Facts</h4>
            """,
            unsafe_allow_html=True,
        )
        facts = []
        if isinstance(content, dict):
            facts.extend(localized_items(content.get("important_facts", {}))[:3])

        for f in facts[:3]:
            st.markdown(f"- {f}")
        st.markdown("</div>", unsafe_allow_html=True)

    articles = content.get("important_articles", data.get("important_articles", []))
    third_panel_title = "Important Articles & Provisions" if articles else "Quick Revision"

    col3, col4 = st.columns(2, gap="medium")

    # 3. Important Articles
    with col3:
        st.markdown(
            f"""
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #D97706; padding: 14px; border-radius: 10px; margin-bottom: 12px;">
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 0.98rem;">• {third_panel_title}</h4>
            """,
            unsafe_allow_html=True,
        )
        third_panel_items = []
        if articles and isinstance(articles, list):
            for a in articles[:3]:
                if isinstance(a, dict):
                    article_titles = localized_items(a.get("title", {}))
                    title = article_titles[0] if article_titles else ""
                    third_panel_items.append(f"Article {a.get('article', '')}: {title}")
                elif isinstance(a, str):
                    third_panel_items.append(a)
        else:
            third_panel_items.extend(localized_items(content.get("quick_revision", {}))[:3])

        for item in third_panel_items[:3]:
            st.markdown(f"- {item}")
        st.markdown("</div>", unsafe_allow_html=True)

    # 4. TNPSC Traps
    with col4:
        st.markdown(
            """
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #DC2626; padding: 14px; border-radius: 10px; margin-bottom: 12px;">
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 0.98rem;">• TNPSC Traps & Common Pitfalls</h4>
            """,
            unsafe_allow_html=True,
        )
        traps = []
        t_list = content.get("tnpsc_traps", [])
        if isinstance(t_list, list):
            for trap in t_list:
                if isinstance(trap, dict):
                    traps.extend(localized_items(trap.get("points", {})))
                elif trap:
                    traps.append(str(trap))

        for trap in traps[:3]:
            st.markdown(f"- {trap}")
        st.markdown("</div>", unsafe_allow_html=True)


def render_notes_page(section):
    section("📘 Topic Notes")

    subject = get_selected_subject().lower()
    topic_id = get_selected_topic_id()
    repository_id = get_selected_repository_id()
    display_title = get_selected_display_title()

    note_basename = topic_id
    if note_basename.startswith(f"{subject}_"):
        note_basename = note_basename[len(subject) + 1 :]

    repo_basename = repository_id
    if repo_basename.startswith(f"{subject}_"):
        repo_basename = repo_basename[len(subject) + 1 :]

    # Dynamic multi-part discovery
    parts_map = discover_note_parts(subject, note_basename)
    if not parts_map and repo_basename:
        parts_map = discover_note_parts(subject, repo_basename)

    if not parts_map:
        st.warning(f"📭 Notes for '{display_title}' are coming soon in the next content update.")
        st.info("💡 You can attempt practice questions or grand tests for this topic in the Study Hub.")
        return

    # Numeric sorting of part numbers (1, 2, 3...)
    part_numbers = sorted(parts_map.keys())
    session_part_key = f"selected_part_{topic_id}"

    # Auto-detect part from topic_id if user navigated to a specific part entry (e.g. polity_electoral_reforms_part_2)
    match_part = re.search(r"_part_?(\d+)$", topic_id.lower())
    suggested_part = int(match_part.group(1)) if match_part and int(match_part.group(1)) in part_numbers else None

    if session_part_key not in st.session_state or st.session_state[session_part_key] not in part_numbers:
        st.session_state[session_part_key] = suggested_part or part_numbers[0]

    selected_part_num = st.session_state[session_part_key]

    hdr_col, btn_col = st.columns([3, 1], gap="small")
    with hdr_col:
        st.markdown(
            f"""
            <div style="margin-bottom: 12px;">
                <span class="progress-pill" style="background:#EFF6FF; color:#2563EB; font-weight:800;">
                    🏛️ Subject: {subject.title()}
                </span>
                <span class="progress-pill" style="background:#F8FAFC; color:#0F172A; font-weight:800;">
                    📖 Topic: {display_title}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with btn_col:
        if st.button("Continue Learning →", key="notes_switch_topic_btn", use_container_width=True):
            st.session_state["main_menu"] = "🏠 Home"
            st.session_state["nav_view"] = "topic_hub"
            st.rerun()

    # Part Selector UI (if multiple parts exist)
    if len(part_numbers) > 1:
        st.markdown("##### 📚 Select Module Part:")
        p_cols = st.columns(len(part_numbers))
        for idx, p_num in enumerate(part_numbers):
            is_active = p_num == selected_part_num
            btn_type = "primary" if is_active else "secondary"
            btn_label = f"📖 Part {p_num}"
            if p_cols[idx].button(btn_label, key=f"btn_part_sel_{topic_id}_{p_num}", type=btn_type, use_container_width=True):
                st.session_state[session_part_key] = p_num
                st.rerun()
        st.markdown("---")

    # Load and Render Selected Part with mtime cache-invalidation
    selected_file_path = parts_map[selected_part_num]
    file_mtime = os.path.getmtime(selected_file_path) if os.path.exists(selected_file_path) else 0
    data = load_note(selected_file_path, mtime=file_mtime)

    # Source Identity Debug Output (Console + UI)
    print(f"[NOTES_LOADER] CURRENT TOPIC: {note_basename} | CURRENT PART: {selected_part_num} | LOADED FILE: {selected_file_path}")
    st.caption(f"📌 **CURRENT TOPIC**: `{note_basename}` | **CURRENT PART**: `{selected_part_num} of {len(part_numbers)}` | **LOADED FILE**: `{selected_file_path}`")

    if data is None:
        st.error(f"❌ Error loading notes payload for Part {selected_part_num}.")
        st.info("Please select another available part or contact support.")
        return

    identity = data.get("meta", {}) if isinstance(data, dict) else {}
    identity = identity if isinstance(identity, dict) else {}
    content_scope = identity.get("topic_id") or f"{topic_id}_part_{selected_part_num}"
    previous_scope = st.session_state.get("_active_notes_content_scope")
    if previous_scope and previous_scope != content_scope:
        fixed_mind_map_keys = {
            "mm_node_progress",
            "mind_map_expanded",
            "mm_view_mode_selector",
            "input_mm_search",
        }
        mind_map_prefixes = ("show_mm_", "quiz_radio_", "btn_mm_", "btn_sub_quiz_")
        for state_key in list(st.session_state.keys()):
            if state_key in fixed_mind_map_keys or state_key.startswith(mind_map_prefixes):
                del st.session_state[state_key]
    st.session_state["_active_notes_content_scope"] = content_scope
    st.session_state["notes_content_scope"] = content_scope

    try:
        render_notes(data)
        st.caption(f"UI Type: {data.get('ui_type', 'unknown')} | Part {selected_part_num} of {len(part_numbers)}")

        # Render 2-Minute Revision Card
        render_2_minute_revision_card(data, display_title, subject)

    except Exception as e:
        st.error(f"❌ Error rendering Part {selected_part_num} notes.")
        st.exception(e)

    st.markdown("---")
    if st.button("📝 Start Practice", type="primary", use_container_width=True, key="btn_notes_start_practice"):
        from core.question_engine.practice_session import start_practice_session
        started = start_practice_session(subject, topic_id, repository_id, display_title, "easy")
        if started:
            st.session_state["study_stage"] = "practice_easy"
            st.session_state["main_menu"] = "🏠 Home"
            st.rerun()
        else:
            st.error("No practice questions found for this topic.")
