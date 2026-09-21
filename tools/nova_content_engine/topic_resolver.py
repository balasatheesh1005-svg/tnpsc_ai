import json
import os
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from core.topics_loader import get_topic_metadata_list, get_topic_metadata_by_id


ACTIVE_TOPIC_FILE = "data/pipeline_status/active_topic.json"


KNOWN_PREFIXES = {
    "centre_state_relations": "CSR",
    "high_court": "HC",
    "supreme_court": "SC",
    "governor": "GOV",
    "president": "PRES",
    "vice_president": "VP",
    "prime_minister": "PM",
    "chief_minister_state_council_of_ministers": "CM",
    "state_legislature": "SL",
    "parliament": "PARL",
    "fundamental_rights": "FR",
    "fundamental_duties": "FD",
    "directive_principles": "DPSP",
    "preamble": "PRE",
    "citizenship": "CIT",
    "historical_background": "HB",
    "making_of_indian_constitution": "MIC",
    "salient_features_of_the_indian_constitution": "SF",
    "amendments": "CA",
    "inter_state_relations": "ISR",
    "emergency_provisions": "EP",
    "panchayati_raj": "PR",
    "municipalities": "MUN",
    "union_territory": "UT",
    "election_commission": "EC",
    "electoral_reforms": "ER",
    "cag": "CAG",
    "attorney_general_of_india": "AGI",
    "advocate_general": "AG",
    "finance_commission": "FC",
    "upsc_state_psc": "PSC",
    "constitutional_schedules": "SCH",
    "schedules": "SCH",
    "niti_aayog": "NA",
    "tribunals": "TRI",
    "official_language": "OL",
    "anti_defection_law": "ADL",
    "judicial_review_activism_pil": "JRAP",
    "parliamentary_committees": "PC",
    "parliamentary_privileges": "PP",
    "political_parties_pressure_groups": "PPPG",
    "special_provisions_states": "SPS",
    "state_election_finance_commissions": "SEFC",
    "cooperative_societies": "CS",
}


@dataclass
class ResolvedTopic:
    subject: str
    topic_id: str
    repository_id: str
    display_title: str
    base_name: str
    id_prefix: str
    total_parts: int


from .economy_mcq_config import ECONOMY_PREFIX_MAP


def derive_prefix(base_name: str, subject: str = "polity") -> str:
    if subject.lower() == "economy" and base_name in ECONOMY_PREFIX_MAP:
        return ECONOMY_PREFIX_MAP[base_name]
    if base_name in KNOWN_PREFIXES:
        return KNOWN_PREFIXES[base_name]
    if base_name in ECONOMY_PREFIX_MAP:
        return ECONOMY_PREFIX_MAP[base_name]
    words = [w for w in base_name.split("_") if w]
    if len(words) > 1:
        return "".join([w[0].upper() for w in words])
    return words[0][:3].upper() if words else "MCQ"


def get_active_topic() -> Optional[str]:
    if os.path.exists(ACTIVE_TOPIC_FILE):
        try:
            with open(ACTIVE_TOPIC_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("topic_id")
        except Exception:
            return None
    return None


def set_active_topic(topic_id: str, subject: str = "polity") -> None:
    os.makedirs(os.path.dirname(ACTIVE_TOPIC_FILE), exist_ok=True)
    with open(ACTIVE_TOPIC_FILE, "w", encoding="utf-8") as f:
        json.dump({"topic_id": topic_id, "subject": subject}, f, indent=2)


def resolve_topic(
    query_or_id: Optional[str] = None,
    subject: str = "polity"
) -> ResolvedTopic:
    """
    Topic resolution engine.
    Priority:
      1. Explicit argument / query (e.g. 'centre_state_relations', 'Centre-State Relations')
      2. Active topic from active_topic.json
      3. First in-progress topic from data/pipeline_status/
      4. Default to canonical starting topic for subject
    """
    subj = subject.lower().strip()
    candidate = None

    if query_or_id and query_or_id.strip():
        candidate = query_or_id.strip()
    else:
        candidate = get_active_topic()

    all_topics = get_topic_metadata_list(subj)
    matched_meta = None

    if candidate:
        clean_cand = candidate.lower().strip().replace("-", "_").replace("–", "_").replace(" ", "_")
        if not clean_cand.startswith(f"{subj}_"):
            clean_cand_full = f"{subj}_{clean_cand}"
        else:
            clean_cand_full = clean_cand

        # Try exact topic_id match
        for t in all_topics:
            if t["topic_id"].lower() == clean_cand_full.lower() or t["topic_id"].lower() == clean_cand.lower():
                matched_meta = t
                break

        # Try display_title match
        if not matched_meta:
            for t in all_topics:
                dt_clean = t["display_title"].lower().replace("-", "_").replace("–", "_").replace(" ", "_")
                if clean_cand in dt_clean or dt_clean in clean_cand:
                    matched_meta = t
                    break

    # Fallback to in-progress status file or default
    if not matched_meta:
        status_dir = "data/pipeline_status"
        if os.path.exists(status_dir):
            for fname in os.listdir(status_dir):
                if fname.endswith(".json") and fname != "active_topic.json":
                    pot_id = fname[:-5]
                    try:
                        meta = get_topic_metadata_by_id(subj, pot_id)
                        if meta:
                            matched_meta = meta
                            break
                    except Exception:
                        pass

    if not matched_meta:
        default_id = "economy_nature_and_structure_of_indian_economy" if subj == "economy" else "polity_centre_state_relations"
        matched_meta = get_topic_metadata_by_id(subj, default_id)

    topic_id = matched_meta["topic_id"]
    repo_id = matched_meta.get("repository_id", topic_id)
    display_title = matched_meta.get("display_title", topic_id)
    total_parts = matched_meta.get("total_parts", 3)

    base_name = topic_id
    if base_name.startswith(f"{subj}_"):
        base_name = base_name[len(subj) + 1:]

    if repo_id and repo_id.startswith(f"{subj}_"):
        repo_base = repo_id[len(subj) + 1:]
        if repo_base in ["constitutional_schedules", "constitutional_amendments"]:
            base_name = repo_base

    prefix = derive_prefix(base_name, subj)

    # Persist as active topic
    set_active_topic(topic_id, subj)

    return ResolvedTopic(
        subject=subj,
        topic_id=topic_id,
        repository_id=repo_id,
        display_title=display_title,
        base_name=base_name,
        id_prefix=prefix,
        total_parts=total_parts
    )
