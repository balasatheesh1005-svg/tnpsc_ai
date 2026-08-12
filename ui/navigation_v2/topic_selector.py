import html
from textwrap import dedent
import streamlit as st
from core.navigation_v2.navigation_state import (
    check_repository_availability,
    clear_selected_subject,
    get_available_topics,
    get_selected_subject,
    set_global_topic,
)


def validate_topic_card(topic: dict, availability: dict = None) -> dict:
    """
    Validates every topic dictionary and availability payload before rendering.
    Enforces safe fallback values for missing fields to guarantee stability.
    """
    if not isinstance(topic, dict):
        topic = {}
    if not isinstance(availability, dict):
        availability = {}

    topic_id = str(topic.get("topic_id") or topic.get("id") or "unknown_topic")
    display_title = str(topic.get("display_title") or topic.get("title") or "Untitled Topic")
    subject = str(topic.get("subject") or "polity")

    try:
        part = int(topic.get("part", 1))
    except (ValueError, TypeError):
        part = 1

    try:
        total_parts = int(topic.get("total_parts", 1))
    except (ValueError, TypeError):
        total_parts = 1

    has_notes = bool(availability.get("notes", False))
    has_gt = bool(availability.get("grand_test", False))

    practice_keys = [
        "easy",
        "medium",
        "hard",
        "statement_based",
        "assertion_reason",
        "match_the_following",
        "chronology",
    ]
    qs_count = sum(1 for k in practice_keys if availability.get(k))

    notes_status = "📖 Notes Ready" if has_notes else "📖 Notes Pending"
    gt_status = "🏆 Grand Test Ready" if has_gt else "🏆 Grand Test Not Available"
    practice_status = f"{qs_count} Practice Repos" if qs_count > 0 else "0 Practice Repos"

    return {
        "topic_id": topic_id,
        "display_title": display_title,
        "subject": subject,
        "part": max(1, part),
        "total_parts": max(1, total_parts),
        "has_notes": has_notes,
        "has_gt": has_gt,
        "qs_count": qs_count,
        "notes_status": notes_status,
        "gt_status": gt_status,
        "practice_status": practice_status,
    }


def render_topic_selector():
    subject = get_selected_subject() or "polity"
    subj_title = subject.title()

    c_hdr, c_btn = st.columns([3, 1], gap="small")
    with c_hdr:
        st.markdown(
            dedent(
                f"""
                <div>
                    <span style="font-size: 0.8rem; font-weight: 800; color: #2563EB; text-transform: uppercase;">Subject: {html.escape(subj_title)}</span>
                    <h2 style="margin: 2px 0 10px 0; color: #0F172A;">📖 Select Topic</h2>
                </div>
                """
            ).strip(),
            unsafe_allow_html=True,
        )
    with c_btn:
        if st.button("⬅️ Change Subject", key="btn_change_subject_from_topic"):
            clear_selected_subject()
            st.rerun()

    raw_topics_meta = get_available_topics(subject)
    if not isinstance(raw_topics_meta, list):
        raw_topics_meta = []

    print("[DEBUG] get_available_topics('polity'):", get_available_topics("polity"))

    search_q = st.text_input("🔍 Search Topic:", placeholder="Type to filter topics...", key="topic_search_filter")
    filtered_topics = raw_topics_meta
    if search_q and search_q.strip():
        q_lower = search_q.strip().lower()
        filtered_topics = [
            t for t in raw_topics_meta
            if isinstance(t, dict) and (
                q_lower in str(t.get("display_title", "")).lower() or q_lower in str(t.get("topic_id", "")).lower()
            )
        ]

    if not filtered_topics:
        st.warning(f"No topics found for subject '{subj_title}'.")
        return

    cols = st.columns(2, gap="medium")
    for idx, raw_topic in enumerate(filtered_topics):
        col = cols[idx % 2]
        
        # Fetch availability safely
        try:
            topic_id_lookup = raw_topic.get("topic_id") if isinstance(raw_topic, dict) else str(raw_topic)
            print("[DEBUG] topic_id:", topic_id_lookup)
            avail = check_repository_availability(subject, topic_id_lookup)
            print("[DEBUG] check_repository_availability:", avail)
        except Exception:
            avail = {}

        card_data = validate_topic_card(raw_topic, avail)

        # Build pills
        part_badge_html = ""
        if card_data["total_parts"] > 1:
            part_badge_html = (
                f'<span style="display:inline-block; padding:3px 10px; border-radius:12px; '
                f'background:#F1F5F9; color:#475569; font-weight:700; font-size:0.78rem; '
                f'border:1px solid #E2E8F0;">Part {card_data["part"]} of {card_data["total_parts"]}</span>'
            )

        if card_data["has_notes"]:
            notes_badge_html = (
                '<span style="display:inline-block; padding:3px 10px; border-radius:12px; '
                'background:#EFF6FF; color:#2563EB; font-weight:700; font-size:0.78rem; '
                'border:1px solid #BFDBFE;">📖 Notes Ready</span>'
            )
        else:
            notes_badge_html = (
                '<span style="display:inline-block; padding:3px 10px; border-radius:12px; '
                'background:#F8FAFC; color:#64748B; font-weight:700; font-size:0.78rem; '
                'border:1px solid #E2E8F0;">📖 Notes Pending</span>'
            )

        if card_data["has_gt"]:
            gt_badge_html = (
                '<span style="display:inline-block; padding:3px 10px; border-radius:12px; '
                'background:#FEF3C7; color:#D97706; font-weight:700; font-size:0.78rem; '
                'border:1px solid #FDE68A;">🏆 Grand Test Ready</span>'
            )
        else:
            gt_badge_html = (
                '<span style="display:inline-block; padding:3px 10px; border-radius:12px; '
                'background:#F8FAFC; color:#94A3B8; font-weight:700; font-size:0.78rem; '
                'border:1px solid #E2E8F0;">🏆 Grand Test Not Available</span>'
            )

        repos_badge_html = (
            f'<span style="display:inline-block; padding:3px 10px; border-radius:12px; '
            f'background:#F1F5F9; color:#334155; font-weight:700; font-size:0.78rem; '
            f'border:1px solid #E2E8F0;">{html.escape(card_data["practice_status"])}</span>'
        )

        badges_list = [b for b in [part_badge_html, notes_badge_html, gt_badge_html, repos_badge_html] if b]
        badges_container_html = f'<div style="display: flex; flex-wrap: wrap; gap: 6px; min-height: 64px; align-content: flex-start; margin-bottom: 12px;">{"".join(badges_list)}</div>'

        with col:
            with st.container(border=True):
                st.markdown(
                    dedent(
                        f"""
                        <div style="min-height: 48px; margin-bottom: 8px;">
                            <h4 style="margin: 0; color: #0F172A; font-size: 1.05rem; font-weight: 700; line-height: 1.3;">
                                {html.escape(card_data['display_title'])}
                            </h4>
                        </div>
                        """
                    ).strip(),
                    unsafe_allow_html=True,
                )

                st.markdown(badges_container_html, unsafe_allow_html=True)

                if st.button(
                    "Enter Topic Hub 🚀",
                    key=f"select_top_{idx}_{card_data['topic_id'][:12]}",
                    type="primary",
                    use_container_width=True,
                ):
                    set_global_topic(subject, card_data["topic_id"])
                    st.session_state["nav_view"] = "topic_hub"
                    st.rerun()
