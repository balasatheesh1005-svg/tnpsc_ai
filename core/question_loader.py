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

    file_paths = [
        f"data/questions/{subject}/{repo_basename}_{repo_type}.json",
        f"data/questions/{subject}/{repo_id}_{repo_type}.json",
    ]

    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                with open(file_path, encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"❌ Error loading question file {file_path}: {e}")
                return []

    print(f"❌ Missing question repository file for repo_id='{repo_id}', type='{repo_type}'")
    return []
