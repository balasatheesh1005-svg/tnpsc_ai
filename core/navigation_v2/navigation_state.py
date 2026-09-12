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


def discover_note_parts(subject: str, topic_id_or_base: str) -> Dict[int, str]:
    """
    Discovers all available note part files for a given subject and topic identifier.
    Returns a dict mapping integer part numbers (1, 2, 3...) to file paths.
    """
    if not subject or not topic_id_or_base:
        return {}

    subj = subject.lower().strip()
    notes_dir = Path(f"data/notes/{subj}")
    if not notes_dir.exists():
        return {}

    clean_base = topic_id_or_base.lower().strip()
    if clean_base.startswith(f"{subj}_"):
        clean_base = clean_base[len(subj) + 1 :]

    # Strip trailing part suffix if query passed was e.g. "state_election_finance_commissions_part_1"
    base_no_part = re.sub(r"_part_?\d+$", "", clean_base)

    candidate_bases = [base_no_part]
    alias_map = {
        "amendments": ["constitutional_amendments", "amendments"],
        "constitutional_amendments": ["constitutional_amendments", "amendments"],
        "schedules": ["constitutional_schedules", "schedules"],
        "constitutional_schedules": ["constitutional_schedules", "schedules"],
        "attorney_general_of_india": ["attorney_general", "attorney_general_of_india"],
        "attorney_general": ["attorney_general", "attorney_general_of_india"],
        "advocate_general": ["advocate_general"],
        "cm_state_council_ministers": ["chief_minister_state_council_of_ministers", "cm_state_council_ministers"],
        "chief_minister_state_council_of_ministers": ["chief_minister_state_council_of_ministers", "cm_state_council_ministers"],
    }
    if base_no_part in alias_map:
        for alias in alias_map[base_no_part]:
            if alias not in candidate_bases:
                candidate_bases.append(alias)

    s1 = re.sub(r"_(of|in|the|a|for)_(india|state|states|municipalities|panchayats)$", "", base_no_part)
    if s1 not in candidate_bases:
        candidate_bases.append(s1)
    s2 = re.sub(r"_(of|in|the|a|for)_.*$", "", base_no_part)
    if s2 not in candidate_bases:
        candidate_bases.append(s2)

    parts_found = {}

    for c_base in candidate_bases:
        # 1. Direct check for single-file note: c_base.json
        single_file = notes_dir / f"{c_base}.json"
        if single_file.exists():
            parts_found[1] = str(single_file).replace("\\", "/")

        # 2. Pattern scan for multi-part files
        for p_file in sorted(notes_dir.glob("*.json")):
            fname_no_ext = p_file.stem.lower()

            if fname_no_ext == c_base or fname_no_ext.startswith(f"{c_base}_part"):
                part_num = None
                match = re.search(r"_part_?(\d+)$", fname_no_ext)
                if match:
                    part_num = int(match.group(1))
                else:
                    try:
                        with open(p_file, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            meta = data.get("metadata") or data.get("meta") or {}
                            if isinstance(meta, dict) and "part" in meta:
                                part_num = int(meta["part"])
                    except Exception:
                        pass

                if part_num is None and fname_no_ext == c_base:
                    part_num = 1

                if part_num is not None:
                    parts_found[part_num] = str(p_file).replace("\\", "/")

        if parts_found:
            break

    return dict(sorted(parts_found.items()))



def check_repository_availability(subject: str, topic_id_or_title: str) -> Dict[str, any]:
    """Checks file existence for notes (via topic_id) and questions (via repository_id)."""
    default_res = {
        "notes": False,
        "parts_found": 0,
        "parts_map": {},
        "total_parts": 1,
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

        repo_basenames = [repo_basename]
        alias_map = {
            "finance_commission": ["finance_commission", "fc"],
            "fc": ["fc", "finance_commission"],
            "attorney_general": ["attorney_general", "ag"],
            "ag": ["ag", "attorney_general"],
            "advocate_general": ["advocate_general", "advg"],
            "advg": ["advg", "advocate_general"],
            "cag": ["cag", "comptroller_and_auditor_general"],
            "election_commission": ["election_commission", "ec"],
            "ec": ["ec", "election_commission"],
            "panchayati_raj": ["panchayati_raj", "pr"],
            "pr": ["pr", "panchayati_raj"],
            "municipalities": ["municipalities", "mun"],
            "mun": ["mun", "municipalities"],
            "electoral_reforms": ["electoral_reforms", "er"],
            "er": ["er", "electoral_reforms"],
            "inter_state_relations": ["inter_state_relations", "isr"],
            "isr": ["isr", "inter_state_relations"],
            "constitutional_amendments": ["constitutional_amendments", "amendments", "ca"],
            "amendments": ["constitutional_amendments", "amendments", "ca"],
            "constitutional_schedules": ["constitutional_schedules", "schedules", "sch"],
            "schedules": ["constitutional_schedules", "schedules", "sch"],
        }
        if repo_basename in alias_map:
            for alias in alias_map[repo_basename]:
                if alias not in repo_basenames:
                    repo_basenames.append(alias)

        base_q = f"data/questions/{subj}"

        parts_map = discover_note_parts(subj, note_basename)
        if not parts_map and repo_basename:
            parts_map = discover_note_parts(subj, repo_basename)

        notes_exist = len(parts_map) > 0
        total_parts = max(int(meta.get("total_parts", 1)), len(parts_map))

        def _any_exists(suffixes):
            for rb in repo_basenames:
                for suf in suffixes:
                    if os.path.exists(f"{base_q}/{rb}_{suf}.json") or os.path.exists(f"{base_q}/{subj}_{rb}_{suf}.json"):
                        return True
            return False

        return {
            "notes": notes_exist,
            "parts_found": len(parts_map),
            "parts_map": parts_map,
            "total_parts": total_parts,
            "easy": _any_exists(["easy"]),
            "medium": _any_exists(["medium"]),
            "hard": _any_exists(["hard"]),
            "statement_based": _any_exists(["statement_based", "statement"]),
            "assertion_reason": _any_exists(["assertion_reason", "reasoning", "assertion"]),
            "match_the_following": _any_exists(["match_the_following", "match"]),
            "chronology": _any_exists(["chronology"]),
            "grand_test": _any_exists(["grand_test"]),
            "pyq": _any_exists(["pyq", "pyq_practice"]),
        }

    except Exception:
        return default_res

