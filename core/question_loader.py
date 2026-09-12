import json
import os
from typing import List, Dict, Any, Optional
import streamlit as st

from core.topics_loader import get_topic_metadata_by_id


@st.cache_data
def load_questions(
    repository_id_or_subject: str,
    repository_type_or_topic: str = "easy",
    level: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Loads practice or grand test questions by repository_id and repository_type.
    
    Supports new ID signature:
      load_questions("polity_historical_background", "easy")
      
    And legacy signature:
      load_questions("polity", "historical_background", "easy")
      load_questions("polity", "Historical Background Part 1", "easy")
    """
    if level is not None:
        # Legacy 3-argument call: (subject, topic/title, level)
        subject = repository_id_or_subject.lower().strip()
        topic_input = repository_type_or_topic
        repo_type = level.lower().strip()
        meta = get_topic_metadata_by_id(subject, topic_input)
        repo_id = meta["repository_id"]
    else:
        # New 2-argument call: (repository_id, repository_type)
        arg1 = repository_id_or_subject.strip()
        repo_type = repository_type_or_topic.lower().strip()
        
        if "_" in arg1:
            subject = arg1.split("_", 1)[0].lower()
            repo_id = arg1
        else:
            subject = "polity"
            repo_id = f"{subject}_{arg1}"

    repo_basename = repo_id
    if repo_basename.startswith(f"{subject}_"):
        repo_basename = repo_basename[len(subject) + 1:]

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
        "upsc_state_psc": ["upsc_state_psc", "upsc", "upsc_psc"],
        "upsc": ["upsc", "upsc_state_psc", "upsc_psc"],
        "constitutional_statutory_bodies": ["constitutional_statutory_bodies", "csb"],
        "csb": ["csb", "constitutional_statutory_bodies"],
    }
    if repo_basename in alias_map:
        for alias in alias_map[repo_basename]:
            if alias not in repo_basenames:
                repo_basenames.append(alias)

    type_candidates = [repo_type]
    if repo_type in ["statement", "statement_based"]:
        type_candidates = ["statement_based", "statement"]
    elif repo_type in ["match", "match_the_following"]:
        type_candidates = ["match_the_following", "match"]
    elif repo_type in ["assertion", "assertion_reason", "reasoning"]:
        type_candidates = ["reasoning", "assertion_reason", "assertion"]
    elif repo_type in ["pyq", "pyq_practice"]:
        type_candidates = ["pyq", "pyq_practice"]

    file_paths = []
    for cand in type_candidates:
        for r_base in repo_basenames:
            file_paths.append(f"data/questions/{subject}/{r_base}_{cand}.json")
            file_paths.append(f"data/questions/{subject}/{subject}_{r_base}_{cand}.json")
        file_paths.append(f"data/questions/{subject}/{repo_id}_{cand}.json")

    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                with open(file_path, encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[ERROR] Error loading question file {file_path}: {e}")
                return []

    print(f"[MISSING] Missing question repository file for repo_id='{repo_id}', type='{repo_type}'")
    return []

