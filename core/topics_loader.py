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


def validate_topic_registration(topic_meta: dict) -> bool:
    """Validates that a topic metadata dictionary contains all required fields."""
    required_fields = ["topic_id", "display_title", "part", "total_parts", "subject"]
    if not isinstance(topic_meta, dict):
        print(
            "VALIDATION FAILED\n\n"
            f"Reason: Expected dict, got {type(topic_meta).__name__}\n"
            "Missing field: all\n"
            "File: core/topics_loader.py\n"
            "Function: validate_topic_registration"
        )
        return False

    for field in required_fields:
        if field not in topic_meta or topic_meta[field] is None or str(topic_meta[field]).strip() == "":
            print(
                "VALIDATION FAILED\n\n"
                f"Reason: Required field '{field}' is missing or empty\n"
                f"Missing field: {field}\n"
                "File: core/topics_loader.py\n"
                "Function: validate_topic_registration"
            )
            return False

    return True


def get_topic_metadata_list(subject: str) -> List[Dict[str, any]]:
    subj = subject.lower().strip()
    file_path = f"data/structure/{subj}_structure.json"

    topics_list = []
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            raw_topics = data.get("topics", [])
            topics_list = [_normalize_metadata(subj, t) for t in raw_topics]
        except Exception as e:
            print(f"⚠️ Error reading topic structure for {subj}: {e}")

    # Auto-discover note JSON files in data/notes/{subj}/ if not already registered
    notes_dir = f"data/notes/{subj}"
    if os.path.exists(notes_dir):
        existing_ids = {t["topic_id"] for t in topics_list}
        for filename in sorted(os.listdir(notes_dir)):
            if filename.endswith(".json"):
                base_name = filename[:-5]
                auto_id = f"{subj}_{base_name}"
                if auto_id not in existing_ids:
                    note_path = os.path.join(notes_dir, filename)
                    display_title = base_name.replace("_", " ").title()
                    part = 1
                    total_parts = 1
                    try:
                        with open(note_path, "r", encoding="utf-8") as nf:
                            note_data = json.load(nf)
                            meta_block = note_data.get("meta") or note_data.get("metadata") or {}
                            if isinstance(meta_block, dict):
                                display_title = meta_block.get("display_title") or display_title
                                auto_id = meta_block.get("topic_id") or auto_id
                                part = meta_block.get("part", 1)
                                total_parts = meta_block.get("total_parts", 1)
                    except Exception:
                        pass

                    if auto_id in existing_ids:
                        continue

                    new_topic = {
                        "topic_id": auto_id,
                        "repository_id": auto_id,
                        "display_title": display_title,
                        "part": part,
                        "total_parts": total_parts,
                        "subject": subj,
                    }
                    topics_list.append(new_topic)
                    existing_ids.add(auto_id)

    validated_topics = []
    for t in topics_list:
        if validate_topic_registration(t):
            validated_topics.append(t)

    return validated_topics


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

    # 4. Flexible match on cleaned alpha-numeric title/id (e.g. matching variations like "Prime Minister – Part 1")
    query_clean = re.sub(r"[^a-z0-9]", "", query.lower())
    for meta in meta_list:
        meta_id_clean = re.sub(r"[^a-z0-9]", "", meta["topic_id"].lower())
        meta_title_clean = re.sub(r"[^a-z0-9]", "", meta["display_title"].lower())
        if query_clean == meta_id_clean or query_clean == meta_title_clean:
            return meta

    # Fallback auto-constructed metadata
    return _normalize_metadata(subj, query)


def get_topic_key(subject: str, topic: str) -> str:
    """Legacy helper function for backward compatibility."""
    meta = get_topic_metadata_by_id(subject, topic)
    return meta["repository_id"]


def format_subject_name(subject: str) -> str:
    """Formats raw subject string for display."""
    if not subject:
        return "General"
    return str(subject).replace("_", " ").replace("-", " ").title()


def format_topic_name(topic: str) -> str:
    """Formats raw topic string for display."""
    if not topic:
        return "General"
    return str(topic).replace("_", " ").replace("-", " ").title()

