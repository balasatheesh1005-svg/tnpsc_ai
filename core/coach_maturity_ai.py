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

    # 1. State Classification
    if attempt_count == 0:
        state = "NO_DATA"
    elif attempt_count < 5:
        state = "EARLY_INSIGHTS"
    else:
        state = "PERSONALIZED_COACH"

    # 2. Topic & Subject Performance Analysis
    subjects_set = set(str(r.get("subject", "")).strip().title() for r in progress_rows if r.get("subject"))
    topics_set = set(str(r.get("topic", "")).strip() for r in progress_rows if r.get("topic"))
    subjects_attempted = len(subjects_set)
    topics_attempted = len(topics_set)

    all_accuracies = [float(r.get("accuracy", 0)) for r in progress_rows if r.get("accuracy") is not None]
    avg_accuracy = round(sum(all_accuracies) / len(all_accuracies), 1) if all_accuracies else 0.0

    # Mastered topics: accuracy >= 80%
    mastered_topics_set = set(
        str(r.get("topic", "")).strip()
        for r in progress_rows
        if float(r.get("accuracy", 0)) >= 80.0
    )
    mastered_count = len(mastered_topics_set)
    pending_count = len(topics_set - mastered_topics_set)

    # Strong subject from real progress rows
    strong_subject = None
    if progress_rows:
        subj_accs = {}
        for r in progress_rows:
            s = str(r.get("subject", "")).strip().title()
            if s and r.get("accuracy") is not None:
                subj_accs.setdefault(s, []).append(float(r["accuracy"]))
        if subj_accs:
            strong_subject = max(subj_accs.keys(), key=lambda k: sum(subj_accs[k]) / len(subj_accs[k]))

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

    # 3. Metric-Specific Eligibility Gates
    readiness_eligible = (state == "PERSONALIZED_COACH")
    prediction_eligible = (state == "PERSONALIZED_COACH")
    weakness_eligible = has_weakness_data
    mock_eligible = has_mock_data
    mastery_eligible = (state in ["EARLY_INSIGHTS", "PERSONALIZED_COACH"] and topics_attempted > 0)
    timing_eligible = False  # Current schema does not record answer duration

    return {
        "state": state,
        "attempt_count": attempt_count,
        "subjects_attempted": subjects_attempted,
        "topics_attempted": topics_attempted,
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
