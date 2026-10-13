import logging
from typing import Dict, Any, Optional

from core.progress_ai import get_progress
from core.weakness_ai import get_weakness
from core.streak_ai import get_streak
from core.xp_ai import get_user_xp
from core.revision_engine import get_revision_overview

logger = logging.getLogger(__name__)


def get_coach_maturity(user: Optional[str] = None, context: Optional[Any] = None) -> Dict[str, Any]:
    """
    Canonical Coach Maturity & Metric Eligibility Gate.
    
    Evaluates real user history from current database tables:
    - users_progress (attempt counts, accuracy, completed topics)
    - users_weakness (recorded weakness areas)
    - user_streaks (daily consistency)
    - user_revisions (scheduled revision queue)
    
    Returns 3-state maturity classification:
    - NO_DATA: 0 completed tests
    - EARLY_INSIGHTS: 1-4 completed tests
    - PERSONALIZED_COACH: 5+ completed tests
    
    Also provides granular metric-specific eligibility flags.
    """
    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    progress_rows = get_progress(user, context=ctx) or []
    weakness_data = get_weakness(user, context=ctx) or {}
    streak = get_streak(user, context=ctx) or 0
    xp_data = get_user_xp(user, context=ctx) or {}
    revision_overview = get_revision_overview(user, context=ctx) or {}

    attempt_count = len(progress_rows)

    # 1. Topic & Subject Performance Analysis
    # Build detailed subject-level evidence mapping
    subject_evidence: Dict[str, Dict[str, Any]] = {}
    for r in progress_rows:
        subj_raw = str(r.get("subject", "")).strip()
        if not subj_raw:
            continue
        subj_norm = subj_raw.lower().replace("_", " ").replace("-", " ")
        if subj_norm not in subject_evidence:
            subject_evidence[subj_norm] = {
                "display_name": subj_raw.title(),
                "attempt_count": 0,
                "scores": [],
                "topics": set(),
            }
        subject_evidence[subj_norm]["attempt_count"] += 1
        acc = r.get("accuracy")
        if acc is not None:
            try:
                subject_evidence[subj_norm]["scores"].append(float(acc))
            except (ValueError, TypeError):
                pass
        top_raw = str(r.get("topic", "")).strip()
        if top_raw:
            subject_evidence[subj_norm]["topics"].add(top_raw)

    # Finalize average accuracy per subject in evidence map
    subject_evidence_map: Dict[str, Dict[str, Any]] = {}
    for s_norm, s_data in subject_evidence.items():
        avg_acc = (
            round(sum(s_data["scores"]) / len(s_data["scores"]), 1)
            if s_data["scores"]
            else None
        )
        subject_evidence_map[s_norm] = {
            "subject": s_data["display_name"],
            "attempt_count": s_data["attempt_count"],
            "avg_accuracy": avg_acc,
            "topics": list(s_data["topics"]),
        }

    subjects_attempted = len(subject_evidence_map)
    observed_subjects = [s_data["subject"] for s_data in subject_evidence_map.values()]
    observed_topics = list(set(str(r.get("topic", "")).strip() for r in progress_rows if r.get("topic")))
    topics_attempted = len(observed_topics)

    all_accuracies = [float(r.get("accuracy", 0)) for r in progress_rows if r.get("accuracy") is not None]
    avg_accuracy = round(sum(all_accuracies) / len(all_accuracies), 1) if all_accuracies else 0.0

    # Mock attempts identification
    mock_rows = [
        r for r in progress_rows
        if "grand_test" in str(r.get("topic", "")).lower() or "mock" in str(r.get("topic", "")).lower()
    ]
    mock_count = len(mock_rows)
    has_mock_data = mock_count > 0

    latest_mock_accuracy = None
    if has_mock_data:
        latest_mock = mock_rows[-1]
        if latest_mock.get("accuracy") is not None:
            latest_mock_accuracy = int(round(float(latest_mock["accuracy"])))

    # Revision data check
    due_today = revision_overview.get("due_today", [])
    overdue = revision_overview.get("overdue", [])
    has_revision_data = bool(due_today or overdue)

    # 2. State & Tier Classification
    if attempt_count == 0:
        state = "NO_DATA"
        tier = "TIER_0_NO_DATA"
        tier_label = "No Data"
    elif attempt_count < 5:
        state = "EARLY_INSIGHTS"
        tier = "TIER_1_EARLY_SIGNAL"
        tier_label = "Early Signal"
    elif subjects_attempted < 3 or not has_mock_data:
        state = "PERSONALIZED_COACH"
        tier = "TIER_2_DEVELOPING"
        tier_label = "Developing"
    else:
        state = "PERSONALIZED_COACH"
        tier = "TIER_3_RELIABLE"
        tier_label = "Reliable"

    # Mastered topics: accuracy >= 80%
    mastered_topics_set = set(
        str(r.get("topic", "")).strip()
        for r in progress_rows
        if float(r.get("accuracy", 0)) >= 80.0
    )
    mastered_count = len(mastered_topics_set)
    pending_count = len(set(observed_topics) - mastered_topics_set)

    # Strong subject from real progress rows
    strong_subject = None
    if subject_evidence_map:
        assessed_with_scores = [
            (s_info["subject"], s_info["avg_accuracy"])
            for s_info in subject_evidence_map.values()
            if s_info["avg_accuracy"] is not None
        ]
        if assessed_with_scores:
            strong_subject = max(
                assessed_with_scores,
                key=lambda x: (x[1] if x[1] is not None else 0.0)
            )[0]

    # Weak topic from real weakness records
    weak_topic = None
    has_weakness_data = bool(weakness_data)
    if has_weakness_data:
        top_weak = sorted(weakness_data.items(), key=lambda x: x[1], reverse=True)[0][0]
        if "-" in top_weak:
            parts = top_weak.split("-", 1)
            weak_topic = parts[1].replace("_", " ").title()
        else:
            weak_topic = top_weak.replace("_", " ").title()

    # 3. Metric-Specific Eligibility Gates
    readiness_eligible = (state == "PERSONALIZED_COACH" and subjects_attempted >= 2)
    prediction_eligible = (state == "PERSONALIZED_COACH" and subjects_attempted >= 2 and has_mock_data)
    weakness_eligible = has_weakness_data
    mock_eligible = has_mock_data
    mastery_eligible = (state in ["EARLY_INSIGHTS", "PERSONALIZED_COACH"] and topics_attempted > 0)
    timing_eligible = False  # Current schema does not record answer duration

    return {
        "state": state,
        "tier": tier,
        "tier_label": tier_label,
        "attempt_count": attempt_count,
        "observed_test_count": attempt_count,
        "subjects_attempted": subjects_attempted,
        "observed_subjects": observed_subjects,
        "topics_attempted": topics_attempted,
        "observed_topics": observed_topics,
        "subject_evidence_map": subject_evidence_map,
        "mock_count": mock_count,
        "has_weakness_data": has_weakness_data,
        "has_revision_data": has_revision_data,
        "has_mock_data": has_mock_data,
        "readiness_eligible": readiness_eligible,
        "weakness_eligible": weakness_eligible,
        "mock_eligible": mock_eligible,
        "prediction_eligible": prediction_eligible,
        "mastery_eligible": mastery_eligible,
        "timing_eligible": timing_eligible,
        "avg_accuracy": avg_accuracy,
        "strong_subject": strong_subject,
        "weak_topic": weak_topic,
        "mastered_count": mastered_count,
        "pending_count": pending_count,
        "latest_mock_accuracy": latest_mock_accuracy,
        "streak": streak,
        "xp": xp_data.get("xp", 0) if isinstance(xp_data, dict) else 0,
    }


def normalize_subject_key(subject: Optional[str]) -> str:
    """Canonical normalizer for subject lookup."""
    if not subject:
        return ""
    return str(subject).strip().lower().replace("_", " ").replace("-", " ")


def has_subject_evidence(
    subject: str,
    user: Optional[str] = None,
    context: Optional[Any] = None,
    progress_rows: Optional[list] = None,
) -> bool:
    """
    Deterministic gate checking whether genuine learner activity exists for a subject.
    """
    norm_subj = normalize_subject_key(subject)
    if not norm_subj:
        return False

    rows = progress_rows
    if rows is None:
        from core.user_context import UserContext
        ctx = context or UserContext.get_or_create(user)
        rows = get_progress(user, context=ctx) or []

    for r in rows:
        row_subj = normalize_subject_key(r.get("subject"))
        if row_subj == norm_subj:
            return True
    return False


def get_subject_evidence(
    subject: str,
    user: Optional[str] = None,
    context: Optional[Any] = None,
    progress_rows: Optional[list] = None,
) -> Optional[Dict[str, Any]]:
    """
    Returns verified evidence dict for a subject:
    {'attempt_count': int, 'avg_accuracy': float, 'topics': list}
    Returns None if no evidence exists for this subject.
    """
    norm_subj = normalize_subject_key(subject)
    if not norm_subj:
        return None

    rows = progress_rows
    if rows is None:
        from core.user_context import UserContext
        ctx = context or UserContext.get_or_create(user)
        rows = get_progress(user, context=ctx) or []

    matching = [r for r in rows if normalize_subject_key(r.get("subject")) == norm_subj]
    if not matching:
        return None

    scores = []
    topics = set()
    for r in matching:
        acc = r.get("accuracy")
        if acc is not None:
            try:
                scores.append(float(acc))
            except (ValueError, TypeError):
                pass
        top = str(r.get("topic", "")).strip()
        if top:
            topics.add(top)

    avg_acc = round(sum(scores) / len(scores), 1) if scores else None
    return {
        "subject": subject,
        "attempt_count": len(matching),
        "avg_accuracy": avg_acc,
        "topics": list(topics),
    }


def has_topic_evidence(
    subject: str,
    topic: str,
    user: Optional[str] = None,
    context: Optional[Any] = None,
    progress_rows: Optional[list] = None,
) -> bool:
    """
    Deterministic gate checking whether genuine learner activity exists for a topic.
    """
    norm_subj = normalize_subject_key(subject)
    norm_top = str(topic or "").strip().lower().replace("_", " ").replace("-", " ")
    if not norm_subj or not norm_top:
        return False

    rows = progress_rows
    if rows is None:
        from core.user_context import UserContext
        ctx = context or UserContext.get_or_create(user)
        rows = get_progress(user, context=ctx) or []

    for r in rows:
        row_subj = normalize_subject_key(r.get("subject"))
        row_top = str(r.get("topic", "")).strip().lower().replace("_", " ").replace("-", " ")
        if row_subj == norm_subj and (norm_top in row_top or row_top in norm_top):
            return True
    return False

