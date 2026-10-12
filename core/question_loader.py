import json
import os
from typing import List, Dict, Any, Optional
import streamlit as st

from core.topics_loader import get_topic_metadata_by_id, normalize_repo_basename


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
        if subject in ["gt", "gt_"]:
            subject = "general_tamil"
        topic_input = repository_type_or_topic
        repo_type = level.lower().strip()
        meta = get_topic_metadata_by_id(subject, topic_input)
        repo_id = meta["repository_id"]
    else:
        # New 2-argument call: (repository_id, repository_type)
        arg1 = repository_id_or_subject.strip()
        repo_type = repository_type_or_topic.lower().strip()
        
        if arg1.startswith("gt_") or arg1.startswith("general_tamil_"):
            subject = "general_tamil"
            repo_id = arg1
        elif arg1.startswith("tna_") or arg1.startswith("tn_administration_"):
            subject = "tn_administration"
            repo_id = arg1
        elif arg1.startswith("ts_") or arg1.startswith("tamil_society_"):
            subject = "tamil_society"
            repo_id = arg1
        elif "_" in arg1:
            subject = arg1.split("_", 1)[0].lower()
            if subject in ["gt", "gt_"]:
                subject = "general_tamil"
            repo_id = arg1
        else:
            subject = "polity"
            repo_id = f"{subject}_{arg1}"

    repo_basename = normalize_repo_basename(subject, repo_id)

    repo_basenames = [repo_basename]
    if repo_id != repo_basename and repo_id not in repo_basenames:
        repo_basenames.append(repo_id)
    alias_map = {
        "finance_commission": ["finance_commission", "fc"],
        "fc": ["fc", "finance_commission"],
        "attorney_general_of_india": ["attorney_general_of_india", "attorney_general", "ag"],
        "attorney_general": ["attorney_general", "attorney_general_of_india", "ag"],
        "ag": ["ag", "attorney_general", "attorney_general_of_india"],
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
        "directive_principles": ["directive_principles", "dpsp", "directive_principles_of_state_policy"],
        "directive_principles_of_state_policy": ["directive_principles", "dpsp", "directive_principles_of_state_policy"],
        "dpsp": ["directive_principles", "dpsp", "directive_principles_of_state_policy"],
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
    elif repo_type in ["grand", "grand_test"]:
        type_candidates = ["grand_test", "grand"]

    file_paths = []
    for cand in type_candidates:
        for r_base in repo_basenames:
            file_paths.append(f"data/questions/{subject}/{r_base}_{cand}.json")
            file_paths.append(f"data/questions/{subject}/{subject}_{r_base}_{cand}.json")
        file_paths.append(f"data/questions/{subject}/{repo_id}_{cand}.json")

    # 1. Try legacy split files first
    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                with open(file_path, encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[ERROR] Error loading question file {file_path}: {e}")
                return []

    # 2. Try consolidated Gold bank files (e.g., gt_u1_piritthu_serththu_ezhuthuthal_gold.json)
    gold_candidates = []
    for r_base in repo_basenames:
        gold_candidates.append(f"data/questions/{subject}/{r_base}_gold.json")
        gold_candidates.append(f"data/questions/{subject}/{subject}_{r_base}_gold.json")
    gold_candidates.append(f"data/questions/{subject}/{repo_id}_gold.json")

    for gold_path in gold_candidates:
        if os.path.exists(gold_path):
            try:
                with open(gold_path, encoding="utf-8") as f:
                    raw_data = json.load(f)
                all_qs = raw_data.get("questions", []) if isinstance(raw_data, dict) else raw_data
                return _filter_gold_questions(all_qs, repo_type)
            except Exception as e:
                print(f"[ERROR] Error loading Gold question file {gold_path}: {e}")
                return []

    print(f"[MISSING] Missing question repository file for repo_id='{repo_id}', type='{repo_type}'")
    return []


def _filter_gold_questions(questions: List[Dict[str, Any]], repo_type: str) -> List[Dict[str, Any]]:
    """Filters consolidated Gold bank questions in-memory by requested practice mode."""
    mode = repo_type.lower().strip()

    if mode in ["easy", "medium", "hard"]:
        return [q for q in questions if str(q.get("difficulty", "")).lower().strip() == mode]

    if mode in ["statement", "statement_based"]:
        target_types = {"statement evaluation", "statement_evaluation", "statement", "statement based"}
        return [q for q in questions if str(q.get("question_type", "")).lower().strip() in target_types]

    if mode in ["match", "match_the_following"]:
        target_types = {"match", "match_the_following", "match the following"}
        return [q for q in questions if str(q.get("question_type", "")).lower().strip() in target_types]

    if mode in ["assertion", "assertion_reason", "reasoning"]:
        target_types = {"assertion reason", "assertion_reason", "assertion & reason", "assertion", "reasoning"}
        return [q for q in questions if str(q.get("question_type", "")).lower().strip() in target_types]

    if mode in ["pyq", "pyq_practice"]:
        return [q for q in questions if q.get("question_origin") == "OFFICIAL_TNPSC_PYQ" or "pyq" in str(q.get("tags", [])).lower()]

    if mode in ["grand", "grand_test"]:
        return questions

    return questions


def clear_questions_cache():
    """Clears the Streamlit cache for load_questions."""
    try:
        load_questions.clear()
    except Exception:
        pass


