import json
import os
import re
from typing import Dict, List, Optional
import streamlit as st


def _normalize_string_to_id(subject: str, title: str) -> str:
    subj = subject.lower().strip()
    clean_title = title.lower()
    clean_title = re.sub(r"[^a-z0-9_ ]", "", clean_title).replace(" ", "_")
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
        return False
    for field in required_fields:
        if field not in topic_meta or topic_meta[field] is None or str(topic_meta[field]).strip() == "":
            return False
    return True


def normalize_base_topic_id(subject: str, raw_id_or_filename: str) -> str:
    subj = subject.lower().strip()
    s = raw_id_or_filename.lower().strip()

    # Strip .json extension if present
    if s.endswith(".json"):
        s = s[:-5]

    # Prefix with subject if missing
    if not s.startswith(f"{subj}_"):
        s = f"{subj}_{s}"

    # Strip part suffix pattern (_part_1, _part1, _part_01, etc.)
    base_id = re.sub(r"_part_?\d+$", "", s, flags=re.IGNORECASE)

    # Alias mapping to canonical repository_ids
    aliases = {
        "polity_advocate": "polity_advocate_general",
        "advocate_general": "polity_advocate_general",
        "polity_historical_background_part": "polity_historical_background",
        "polity_attorney_general": "polity_attorney_general_of_india",
        "polity_constitutional_amendments": "polity_amendments",
        "polity_constitutional_schedules": "polity_schedules",
    }

    return aliases.get(base_id, base_id)


def format_title_from_base_id(subject: str, base_id: str) -> str:
    subj = subject.lower().strip()
    clean = base_id
    if clean.startswith(f"{subj}_"):
        clean = clean[len(subj) + 1 :]

    known_titles = {
        "historical_background": "Historical Background",
        "making_of_indian_constitution": "Making of Indian Constitution",
        "constituent_assembly_formation_and_composition": "Constituent Assembly Formation and Composition",
        "salient_features_of_the_indian_constitution": "Salient Features of the Indian Constitution",
        "preamble": "Preamble",
        "fundamental_rights": "Fundamental Rights",
        "directive_principles": "Directive Principles of State Policy",
        "fundamental_duties": "Fundamental Duties",
        "president": "President of India",
        "vice_president": "Vice-President of India",
        "prime_minister": "Prime Minister of India",
        "parliament": "Parliament of India",
        "attorney_general_of_india": "Attorney General of India",
        "state_government": "State Government",
        "indian_judiciary": "Indian Judiciary",
        "local_government": "Local Government",
        "constitutional_bodies": "Constitutional Bodies",
        "non_constitutional_bodies": "Non-Constitutional Bodies",
        "amendments": "Constitutional Amendments",
        "schedules": "Constitutional Schedules",
        "governor": "Governor of a State",
        "supreme_court": "Supreme Court of India",
        "high_court": "High Courts in India",
        "electoral_reforms": "Electoral Reforms",
        "advocate_general": "Advocate General of a State",
        "anti_defection_law": "Anti-Defection Law",
        "cag": "Comptroller & Auditor General (CAG)",
        "centre_state_relations": "Centre–State Relations",
        "chief_minister_state_council_of_ministers": "Chief Minister & State Council of Ministers",
        "cm_state_council_ministers": "Chief Minister & State Council of Ministers",
        "citizenship": "Citizenship of India",
        "constitutional_statutory_bodies": "Constitutional & Statutory Bodies",
        "cooperative_societies": "Co-operative Societies",
        "election_commission": "Election Commission of India",
        "emergency_provisions": "Emergency Provisions",
        "finance_commission": "Finance Commission of India",
        "inter_state_relations": "Inter-State Relations",
        "judicial_review_activism_pil": "Judicial Review, Activism & PIL",
        "municipalities": "Local Government – Municipalities",
        "niti_aayog": "NITI Aayog",
        "official_language": "Official Language",
        "panchayati_raj": "Local Government – Panchayati Raj",
        "parliamentary_committees": "Parliamentary Committees",
        "parliamentary_privileges": "Parliamentary Privileges",
        "political_parties_pressure_groups": "Political Parties & Pressure Groups",
        "special_provisions_states": "Special Provisions for States",
        "state_election_finance_commissions": "State Election & Finance Commissions",
        "state_legislature": "State Legislature",
        "tribunals": "Tribunals",
        "union_territory": "Union & Its Territory",
        "upsc_state_psc": "UPSC & State Public Service Commissions",
    }

    if clean in known_titles:
        return known_titles[clean]

    return clean.replace("_", " ").title()


def get_topic_metadata_list(subject: str) -> List[Dict[str, any]]:
    subj = subject.lower().strip()
    file_path = f"data/structure/{subj}_structure.json"
    notes_dir = f"data/notes/{subj}"

    grouped_topics: Dict[str, Dict[str, any]] = {}
    topic_order: List[str] = []

    # 1. Load registry structure entries
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            raw_topics = data.get("topics", [])
            for item in raw_topics:
                if not isinstance(item, dict):
                    continue
                raw_id = item.get("topic_id") or item.get("repository_id") or ""
                base_id = normalize_base_topic_id(subj, raw_id)
                disp_title = item.get("display_title") or format_title_from_base_id(subj, base_id)
                disp_title = re.sub(r"\s*[–-]?\s*Part\s*\d+.*$", "", disp_title, flags=re.IGNORECASE).strip()

                total_parts = int(item.get("total_parts", 1))
                part = int(item.get("part", 1))

                if base_id not in grouped_topics:
                    topic_order.append(base_id)
                    grouped_topics[base_id] = {
                        "topic_id": base_id,
                        "repository_id": item.get("repository_id") or base_id,
                        "display_title": disp_title,
                        "part": 1,
                        "total_parts": max(total_parts, part),
                        "subject": subj,
                    }
                else:
                    grouped_topics[base_id]["total_parts"] = max(grouped_topics[base_id]["total_parts"], total_parts, part)
        except Exception as e:
            print(f"⚠️ Error reading topic structure for {subj}: {e}")

    # 2. Auto-discover notes files and update total_parts / discover un-registered topics
    if os.path.exists(notes_dir):
        for filename in sorted(os.listdir(notes_dir)):
            if not filename.endswith(".json"):
                continue
            base_id = normalize_base_topic_id(subj, filename[:-5])

            part_num = 1
            m = re.search(r"_part_?(\d+)$", filename[:-5], flags=re.IGNORECASE)
            if m:
                part_num = int(m.group(1))

            if base_id not in grouped_topics:
                topic_order.append(base_id)
                disp_title = format_title_from_base_id(subj, base_id)
                grouped_topics[base_id] = {
                    "topic_id": base_id,
                    "repository_id": base_id,
                    "display_title": disp_title,
                    "part": 1,
                    "total_parts": part_num,
                    "subject": subj,
                }
            else:
                grouped_topics[base_id]["total_parts"] = max(grouped_topics[base_id]["total_parts"], part_num)

    validated_topics = []
    for base_id in topic_order:
        t = grouped_topics[base_id]
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
    """Finds canonical topic metadata by topic_id, repository_id, display_title, or part variant."""
    subj = subject.lower().strip()
    meta_list = get_topic_metadata_list(subj)

    if not topic_id_or_title:
        return meta_list[0] if meta_list else _normalize_metadata(subj, "default_topic")

    query = str(topic_id_or_title).strip()
    canonical_query_id = normalize_base_topic_id(subj, query)

    # 1. Exact match on canonical topic_id
    for meta in meta_list:
        if meta["topic_id"] == query or meta["topic_id"] == canonical_query_id:
            return meta

    # 2. Match on repository_id
    for meta in meta_list:
        if meta["repository_id"] == query or meta["repository_id"] == canonical_query_id:
            return meta

    # 3. Match on display_title
    for meta in meta_list:
        if meta["display_title"].lower() == query.lower():
            return meta

    # 4. Flexible match on cleaned alpha-numeric title/id
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


