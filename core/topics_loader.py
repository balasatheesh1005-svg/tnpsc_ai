import json
import os
import re
from typing import Dict, List, Optional
import streamlit as st


def _normalize_string_to_id(subject: str, title: str) -> str:
    subj = subject.lower().strip()
    clean_title = title.lower()
    clean_title = re.sub(r"[^a-z0-9_ ]", "", clean_title).replace(" ", "_")
    # Clean redundant part separators if any
    clean_title = re.sub(r"_+", "_", clean_title).strip("_")
    return f"{subj}_{clean_title}"


def _normalize_metadata(subject: str, item) -> Dict[str, any]:
    subj = subject.lower().strip()
    if isinstance(item, dict):
        topic_id = item.get("topic_id") or _normalize_string_to_id(subj, item.get("display_title", "topic"))
        repository_id = item.get("repository_id") or topic_id
        display_title = item.get("display_title") or item.get("topic_id", "Topic")
        part = item.get("part", 1)
        total_parts = item.get("total_parts", 1)
        return {
            "topic_id": topic_id,
            "repository_id": repository_id,
            "display_title": display_title,
            "part": part,
            "total_parts": total_parts,
            "subject": subj,
        }

    # Handle string item legacy fallback
    title_str = str(item)
    topic_id = _normalize_string_to_id(subj, title_str)
    return {
        "topic_id": topic_id,
        "repository_id": topic_id,
        "display_title": title_str,
        "part": 1,
        "total_parts": 1,
        "subject": subj,
    }


@st.cache_data
def get_topic_metadata_list(subject: str) -> List[Dict[str, any]]:
    subj = subject.lower().strip()
    file_path = f"data/structure/{subj}_structure.json"

    if not os.path.exists(file_path):
        # Fallback list if file missing
        default_titles = [
            "Historical Background Part 1",
            "Historical Background Part 2",
            "Historical Background Part 3",
            "Historical Background Part 4",
            "Making of Indian Constitution",
            "Features of Indian Constitution",
            "Preamble",
            "Fundamental Rights",
        ]
        return [_normalize_metadata(subj, t) for t in default_titles]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        raw_topics = data.get("topics", [])
        return [_normalize_metadata(subj, t) for t in raw_topics]
    except Exception as e:
        print(f"⚠️ Error reading topic structure for {subj}: {e}")
        return []


def get_topics(subject: str) -> List[Dict[str, any]]:
    """Returns list of topic metadata dictionaries for the subject."""
    return get_topic_metadata_list(subject)


def get_display_topics(subject: str) -> List[str]:
    """Returns list of display title strings for UI drop downs."""
    meta_list = get_topic_metadata_list(subject)
    return [m["display_title"] for m in meta_list]


def get_topic_metadata_by_id(subject: str, topic_id_or_title: str) -> Dict[str, any]:
    """Finds topic metadata by topic_id, repository_id, or display_title."""
    subj = subject.lower().strip()
    meta_list = get_topic_metadata_list(subj)

    if not topic_id_or_title:
        return meta_list[0] if meta_list else _normalize_metadata(subj, "default_topic")

    query = str(topic_id_or_title).strip()
    query_id = _normalize_string_to_id(subj, query)

    # 1. Exact match on topic_id
    for meta in meta_list:
        if meta["topic_id"] == query or meta["topic_id"] == query_id:
            return meta

    # 2. Match on display_title
    for meta in meta_list:
        if meta["display_title"].lower() == query.lower():
            return meta

    # 3. Match on repository_id
    for meta in meta_list:
        if meta["repository_id"] == query or meta["repository_id"] == query_id:
            return meta

    # Fallback auto-constructed metadata
    return _normalize_metadata(subj, query)


def get_topic_key(subject: str, topic: str) -> str:
    """Legacy helper function for backward compatibility."""
    meta = get_topic_metadata_by_id(subject, topic)
    return meta["repository_id"]
