import os
import re
from pathlib import Path
from typing import Dict, List, Optional
import streamlit as st

from core.topics_loader import (
    get_topic_metadata_by_id,
    get_topic_metadata_list,
    get_topics,
)

DEFAULT_SUBJECT = "polity"
DEFAULT_TOPIC_ID = "polity_historical_background_part1"


def init_navigation_state():
    """Ensure global navigation state keys exist in st.session_state without overriding active subject/topic selection flows."""
    if "nav_view" not in st.session_state or not st.session_state["nav_view"]:
        st.session_state["nav_view"] = "topic_hub"

    nav_view = st.session_state["nav_view"]

    if nav_view == "subject_select":
        return

    if nav_view == "topic_select":
        if "selected_subject" not in st.session_state or not st.session_state["selected_subject"]:
            st.session_state["selected_subject"] = DEFAULT_SUBJECT
        return

    if "selected_subject" not in st.session_state or not st.session_state["selected_subject"]:
        st.session_state["selected_subject"] = DEFAULT_SUBJECT

    if "selected_topic_id" not in st.session_state or not st.session_state["selected_topic_id"]:
        set_global_topic(st.session_state["selected_subject"], DEFAULT_TOPIC_ID)


def get_selected_subject() -> str:
    init_navigation_state()
    return st.session_state.get("selected_subject") or DEFAULT_SUBJECT


def get_selected_topic_id() -> str:
    init_navigation_state()
    return st.session_state.get("selected_topic_id") or DEFAULT_TOPIC_ID


def get_selected_repository_id() -> str:
    init_navigation_state()
    if "selected_repository_id" in st.session_state and st.session_state["selected_repository_id"]:
        return st.session_state["selected_repository_id"]
    meta = get_selected_topic_metadata()
    return meta.get("repository_id", "polity_historical_background")


def get_selected_display_title() -> str:
    meta = get_selected_topic_metadata()
    return meta.get("display_title", "Historical Background Part 1")


def get_selected_topic_metadata() -> Dict[str, any]:
    init_navigation_state()
    if "selected_topic_metadata" in st.session_state and st.session_state["selected_topic_metadata"]:
        return st.session_state["selected_topic_metadata"]
    subj = get_selected_subject()
    topic_id = st.session_state.get("selected_topic_id", DEFAULT_TOPIC_ID)
    meta = get_topic_metadata_by_id(subj, topic_id)
    st.session_state["selected_topic_metadata"] = meta
    return meta


def get_selected_topic() -> str:
    """Legacy helper: returns UI display title."""
    return get_selected_display_title()


def get_selected_topic_key() -> str:
    """Legacy helper: returns repository_id."""
    return get_selected_repository_id()


def set_global_topic(subject: str, topic_id_or_title: str):
    """Sets global selected subject and topic metadata using permanent IDs."""
    subj = subject.lower().strip()
    meta = get_topic_metadata_by_id(subj, topic_id_or_title)

    st.session_state["selected_subject"] = subj
    st.session_state["selected_topic_id"] = meta["topic_id"]
    st.session_state["selected_repository_id"] = meta["repository_id"]
    st.session_state["selected_topic_metadata"] = meta
    st.session_state["selected_topic"] = meta["display_title"]
    st.session_state["nav_view"] = "topic_hub"


def clear_selected_topic():
    st.session_state["selected_topic_id"] = None
    st.session_state["selected_repository_id"] = None
    st.session_state["selected_topic_metadata"] = None
    st.session_state["selected_topic"] = None
    st.session_state["nav_view"] = "topic_select"
    st.session_state["active_practice_setup"] = None


def clear_selected_subject():
    st.session_state["selected_subject"] = None
    clear_selected_topic()
    st.session_state["nav_view"] = "subject_select"


def has_selected_topic() -> bool:
    return bool(st.session_state.get("selected_subject") and st.session_state.get("selected_topic_id"))


def get_available_subjects() -> List[Dict[str, str]]:
    """Returns all available subjects."""
    notes_dir = Path("data/notes")
    subjects = []
    
    known_names = {
        "polity": {"name": "Polity & Governance", "icon": "🏛️", "desc": "Indian Constitution, Union & State Executive, Judiciary, Panchayati Raj"},
        "history": {"name": "History & Culture", "icon": "📜", "desc": "Ancient, Medieval & Modern Indian History, Art & Heritage"},
        "economy": {"name": "Indian Economy", "icon": "💰", "desc": "Economic Planning, RBI, Finance Commission, GST & Agriculture"},
        "geography": {"name": "Geography of India & TN", "icon": "🌍", "desc": "Physical Geography, Climate, Rivers, Soil, Minerals & Human Geography"},
        "inm": {"name": "Indian National Movement", "icon": "🇮🇳", "desc": "National Renaissance, Freedom Movement, Leaders & TN Freedom Fighters"},
        "aptitude": {"name": "Aptitude & Mental Ability", "icon": "🧮", "desc": "Simplification, Percentage, Ratio, LCM-HCF, Reasoning & Data Analysis"},
        "science": {"name": "General Science", "icon": "🔬", "desc": "Physics, Chemistry, Biology & Environmental Science"},
    }

    if notes_dir.exists():
        for p in sorted(notes_dir.iterdir()):
            if p.is_dir():
                s_id = p.name.lower()
                meta = known_names.get(s_id, {"name": s_id.title(), "icon": "📚", "desc": f"Complete study material and questions for {s_id.title()}"})
                subjects.append({
                    "id": s_id,
                    "title": meta["name"],
                    "icon": meta["icon"],
                    "description": meta["desc"],
                })

    if not subjects:
        subjects = [{
            "id": "polity",
            "title": "Polity & Governance",
            "icon": "🏛️",
            "description": "Indian Constitution, Governance, Rights & Administration",
        }]

    return subjects


def get_available_topics(subject: str) -> List[Dict[str, any]]:
    """Returns topic metadata list for a given subject."""
    return get_topic_metadata_list(subject)


def check_repository_availability(subject: str, topic_id_or_title: str) -> Dict[str, bool]:
    """Checks file existence for notes (via topic_id) and questions (via repository_id)."""
    default_res = {
        "notes": False,
        "easy": False,
        "medium": False,
        "hard": False,
        "statement_based": False,
        "assertion_reason": False,
        "match_the_following": False,
        "chronology": False,
        "grand_test": False,
        "pyq": False,
    }
    if not subject or not topic_id_or_title:
        return default_res

    try:
        subj = subject.lower().strip()
        meta = get_topic_metadata_by_id(subj, topic_id_or_title)
        if not meta or not isinstance(meta, dict):
            return default_res

        topic_id = meta.get("topic_id", "")
        repository_id = meta.get("repository_id", "")

        note_basename = topic_id
        if note_basename.startswith(f"{subj}_"):
            note_basename = note_basename[len(subj) + 1 :]

        repo_basename = repository_id
        if repo_basename.startswith(f"{subj}_"):
            repo_basename = repo_basename[len(subj) + 1 :]

        base_n = f"data/notes/{subj}"
        base_q = f"data/questions/{subj}"

        note_candidates = [
            f"{base_n}/{note_basename}.json",
            f"{base_n}/{note_basename.replace('part', 'part_')}.json" if "part" in note_basename and "part_" not in note_basename else f"{base_n}/{note_basename}.json",
        ]
        notes_exist = any(os.path.exists(p) for p in note_candidates)

        return {
            "notes": notes_exist,
            "easy": os.path.exists(f"{base_q}/{repo_basename}_easy.json"),
            "medium": os.path.exists(f"{base_q}/{repo_basename}_medium.json"),
            "hard": os.path.exists(f"{base_q}/{repo_basename}_hard.json"),
            "statement_based": os.path.exists(f"{base_q}/{repo_basename}_statement_based.json") or os.path.exists(f"{base_q}/{repo_basename}_statement.json"),
            "assertion_reason": os.path.exists(f"{base_q}/{repo_basename}_assertion_reason.json") or os.path.exists(f"{base_q}/{repo_basename}_reasoning.json") or os.path.exists(f"{base_q}/{repo_basename}_assertion.json"),
            "match_the_following": os.path.exists(f"{base_q}/{repo_basename}_match_the_following.json") or os.path.exists(f"{base_q}/{repo_basename}_match.json"),
            "chronology": os.path.exists(f"{base_q}/{repo_basename}_chronology.json"),
            "grand_test": os.path.exists(f"{base_q}/{repo_basename}_grand_test.json"),
            "pyq": os.path.exists(f"{base_q}/{repo_basename}_pyq.json") or os.path.exists(f"{base_q}/{repo_basename}_pyq_practice.json"),
        }
    except Exception:
        return default_res
