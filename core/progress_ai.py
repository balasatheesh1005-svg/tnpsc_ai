import logging
from core.session import current_user_id, current_username
from core.supabase_client import supabase
from core.topics_loader import get_topic_metadata_by_id

logger = logging.getLogger(__name__)


from core.user_identity import resolve_user_id as _resolve_user_id


def save_progress(user=None, subject="", topic="", accuracy=0, topic_id=None, repository_id=None):
    """
    Saves user progress record to public.users_progress using user_id UUID.
    """
    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error("[DATA INTEGRITY ALERT] save_progress failed: user_id IS NULL.")
        return []

    subj = str(subject or "").lower().strip()
    lookup = topic_id or repository_id or topic
    meta = get_topic_metadata_by_id(subj, lookup)

    r_id = meta.get("repository_id", lookup)

    # Determine display username for audit/logging column only (privacy-safe)
    from core.user_identity import get_safe_public_identity

    if isinstance(user, str) and not (len(user) == 36 and user.count("-") == 4):
        display_username = get_safe_public_identity(user, seed=user_id)
    else:
        display_username = get_safe_public_identity(current_username(), seed=user_id)

    data = {
        "user_id": user_id,
        "username": display_username,  # Audit column only
        "subject": subj,
        "topic": r_id,
        "accuracy": accuracy,
    }

    response = supabase.table("users_progress").insert(data).execute()
    return response.data or []


def get_progress(user=None, context=None):
    """
    Retrieves user progress records from public.users_progress matching user_id UUID or pre-fetched context.
    """
    if context is not None and hasattr(context, "progress") and context.progress is not None:
        return context.progress

    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error("[DATA INTEGRITY ALERT] get_progress failed: user_id IS NULL.")
        return []

    response = (
        supabase.table("users_progress").select("*").eq("user_id", user_id).execute()
    )

    rows = response.data or []
    for row in rows:
        if row.get("user_id") is None:
            logger.error(
                f"[DATA INTEGRITY ALERT] Progress record id={row.get('id')} has user_id IS NULL!"
            )

    return rows


def aggregate_topic_progress(progress_data):
    """
    Pure deterministic aggregation helper for TNPSC Nova AI user progress records.
    Groups raw test attempts into unique logical topic entries by:
        (Subject, Repository, Note Part)
    Computes mean attempt accuracy (rounded to 1 decimal place) and attempt counts.
    Safely ignores invalid, non-numeric, or missing accuracy rows without throwing errors.
    """
    import pandas as pd

    empty_cols = ["Subject", "Repository", "Note Part", "Accuracy (%)", "Attempts"]
    if progress_data is None:
        return pd.DataFrame(columns=empty_cols)

    if isinstance(progress_data, pd.DataFrame):
        df = progress_data.copy()
    elif isinstance(progress_data, list):
        if not progress_data:
            return pd.DataFrame(columns=empty_cols)
        df = pd.DataFrame(progress_data)
    else:
        return pd.DataFrame(columns=empty_cols)

    if df.empty or "accuracy" not in df.columns:
        return pd.DataFrame(columns=empty_cols)

    # Safe numeric coercion for accuracy (drops None, nan, non-numeric strings)
    df["accuracy"] = pd.to_numeric(df["accuracy"], errors="coerce")
    df = df.dropna(subset=["accuracy"])
    if df.empty:
        return pd.DataFrame(columns=empty_cols)

    # Normalize subject and topic metadata if not already normalized
    if "repo_display" not in df.columns or "part_display" not in df.columns or "subject" not in df.columns:
        subjects = []
        repo_titles = []
        part_titles = []
        for _, row in df.iterrows():
            raw_subj = row.get("subject")
            subj = str(raw_subj if raw_subj is not None else "polity").lower().strip()
            if not subj:
                subj = "polity"
            subjects.append(subj)

            lookup = str(row.get("topic_id") or row.get("repository_id") or row.get("topic") or "").strip()
            meta = get_topic_metadata_by_id(subj, lookup)

            repo_basename = meta.get("repository_id") or lookup or "Topic"
            if repo_basename.startswith(f"{subj}_"):
                repo_basename = repo_basename[len(subj) + 1:]

            repo_titles.append(repo_basename.replace("_", " ").title())
            part_titles.append(meta.get("display_title") or repo_basename.replace("_", " ").title())

        df["subject"] = subjects
        df["repo_display"] = repo_titles
        df["part_display"] = part_titles

    part_avg = df.groupby(["subject", "repo_display", "part_display"])["accuracy"].agg(["mean", "count"]).reset_index()
    part_avg.columns = empty_cols
    part_avg["Accuracy (%)"] = part_avg["Accuracy (%)"].round(1)

    return part_avg

