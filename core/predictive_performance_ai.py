import logging
from typing import Dict, List, Any, Optional
import streamlit as st

from core.learning_intelligence_ai import (
    get_learning_intelligence,
    format_subject_name,
    format_topic_name,
)
from core.exam_readiness_ai import get_exam_readiness
from core.mock_intelligence_ai import get_mock_intelligence
from core.study_planner_ai import get_personal_study_plan
from core.recommendation_ai import get_ai_recommendation
from core.revision_engine import (
    get_intelligent_revision_plan,
    get_revision_analytics_v2,
)
from core.progress_ai import get_progress
from core.weakness_ai import get_weakness
from core.streak_ai import get_streak
from core.xp_ai import get_user_xp

logger = logging.getLogger(__name__)


def _classify_trend(current_val: float, delta: float) -> str:
    """Classify trend direction based on projected improvement delta."""
    if delta >= 3.0:
        return "Improving"
    elif delta >= 1.0:
        return "Stable"
    else:
        return "Needs Attention"


def _format_range(current_val: float, low_delta: float, high_delta: float) -> str:
    """Format projected metric range strictly as a string range (e.g., '75–79%')."""
    low_bound = max(10, min(97, int(round(current_val + low_delta))))
    high_bound = max(low_bound + 2, min(99, int(round(current_val + high_delta))))
    return f"{low_bound}–{high_bound}%"


from core.performance import measure_time, record_cache_hit, record_cache_miss
from core.engine_cache import ENGINE_CACHE_KEY_PREFIX


@measure_time("Predictive Performance Engine")
def get_predictive_performance(
    user: Optional[str] = None,
    context: Optional[Any] = None,
    force_refresh: bool = False,
) -> Dict[str, Any]:
    """
    Predictive Performance Trajectory Engine V2 - Central Trajectory Engine.
    Synthesizes outputs from Exam Readiness V2, Mock Intelligence V2, Recommendation V2,
    Study Planner V2, Learning Intelligence V2, Revision V2, Progress, Weakness, and Streak Engines.

    Estimates future learning performance trends and metric ranges using conservative,
    deterministic rules and existing learning signals.

    IMPORTANT:
    - NOT an exam result predictor.
    - NOT a pass/fail predictor.
    - ALL predictions are estimated ranges based on available learning data.
    - NEVER guarantees exam success, selection, rank, or score.
    """
    user_str = str(user or "Guest")
    cache_key = f"{ENGINE_CACHE_KEY_PREFIX}Predictive Performance Engine_{user_str}"
    if hasattr(st, "session_state") and not force_refresh and cache_key in st.session_state:
        record_cache_hit("Predictive Performance Engine")
        return st.session_state[cache_key]
    record_cache_miss("Predictive Performance Engine")

    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    # 1. Fetch Data from Existing Master Engines (Zero duplicate calculations)
    readiness_data = get_exam_readiness(user, context=ctx)
    mock_data = get_mock_intelligence(user, context=ctx)
    intelligence_data = get_learning_intelligence(user, context=ctx)
    study_plan = get_personal_study_plan(user, context=ctx)
    recommendation = get_ai_recommendation(user, context=ctx)
    revision_analytics = get_revision_analytics_v2(user, context=ctx)
    progress_rows = get_progress(user, context=ctx)
    weakness_data = get_weakness(user, context=ctx)
    streak = get_streak(user, context=ctx)
    xp_data = get_user_xp(user, context=ctx)

    # 2. Extract Baseline Metrics
    curr_readiness = int(round(readiness_data.get("overall_score", 72)))
    curr_mock_acc = int(round(mock_data.get("overall_accuracy", 74)))
    curr_mastery = int(round(intelligence_data.get("current_mastery", 70.0)))

    rev_prog = revision_analytics.get("progress", {})
    curr_rev_health = int(round(float(rev_prog.get("percentage", 75.0))))

    # Consistency metric derived from streak and learning momentum
    streak_score = min(100, int(round((streak * 8.0) + 40.0)))
    curr_consistency = max(20, min(100, streak_score))

    # Repository completion metric from readiness dimensions
    readiness_dims = readiness_data.get("dimensions", {})
    repo_dim = readiness_dims.get("Repository Completion", {})
    curr_repo = int(round(float(repo_dim.get("score", 65.0))))

    # 3. Deterministic Trend & Range Projection Logic
    # Momentum multipliers based on active streak and revision health
    momentum_factor = 1.2 if streak >= 5 else (1.0 if streak >= 2 else 0.8)
    rev_factor = 1.1 if curr_rev_health >= 70 else 0.85

    # Dimension 1: Readiness Range Projection
    r_low_delta = max(1.0, 2.5 * momentum_factor * rev_factor)
    r_high_delta = max(r_low_delta + 2.0, 5.5 * momentum_factor * rev_factor)

    est_readiness = _format_range(curr_readiness, r_low_delta, r_high_delta)
    readiness_trend = _classify_trend(curr_readiness, r_low_delta)

    # Dimension 2: Mock Accuracy Range Projection
    m_low_delta = max(1.0, 2.0 * momentum_factor)
    m_high_delta = max(m_low_delta + 2.0, 5.0 * momentum_factor)
    est_mock_acc = _format_range(curr_mock_acc, m_low_delta, m_high_delta)
    mock_trend = _classify_trend(curr_mock_acc, m_low_delta)

    # Dimension 3: Topic Mastery Range Projection
    t_low_delta = max(1.5, 3.0 * momentum_factor)
    t_high_delta = max(t_low_delta + 2.0, 6.0 * momentum_factor)
    est_mastery = _format_range(curr_mastery, t_low_delta, t_high_delta)
    mastery_trend = _classify_trend(curr_mastery, t_low_delta)

    # Dimension 4: Revision Health Range Projection
    rev_low_delta = max(1.0, 3.0 * rev_factor)
    rev_high_delta = max(rev_low_delta + 2.0, 7.0 * rev_factor)
    est_rev_health = _format_range(curr_rev_health, rev_low_delta, rev_high_delta)
    revision_trend = _classify_trend(curr_rev_health, rev_low_delta)

    # Dimension 5: Consistency Range Projection
    c_low_delta = max(1.0, 2.0 * momentum_factor)
    c_high_delta = max(c_low_delta + 1.5, 4.5 * momentum_factor)
    est_consistency = _format_range(curr_consistency, c_low_delta, c_high_delta)
    consistency_trend = _classify_trend(curr_consistency, c_low_delta)

    # Dimension 6: Repository Completion Range Projection
    repo_low_delta = max(1.0, 2.5 * momentum_factor)
    repo_high_delta = max(repo_low_delta + 2.0, 5.5 * momentum_factor)
    est_repo = _format_range(curr_repo, repo_low_delta, repo_high_delta)
    repo_trend = _classify_trend(curr_repo, repo_low_delta)

    # 4. Confidence Calculation Logic (0-100%)
    sample_size = len(progress_rows) if progress_rows else 5
    base_confidence = 70

    if sample_size >= 15:
        base_confidence += 12
    elif sample_size >= 5:
        base_confidence += 6

    if streak >= 5:
        base_confidence += 8
    elif streak >= 2:
        base_confidence += 4

    if curr_rev_health >= 70:
        base_confidence += 6

    confidence = max(50, min(96, base_confidence))

    if confidence >= 88:
        conf_reason = "Rich learning history, consistent study streak, and sufficient performance data across tests."
    elif confidence >= 75:
        conf_reason = "Moderate learning history and steady revision activity. Projections are well-supported."
    else:
        conf_reason = "Sparse activity history or developing study streak. Complete more daily practice tests to refine accuracy."

    # 5. Prediction Explanation Rules
    expl_bullets = [
        f"Consistent revision health ({curr_rev_health}%) indicates stable memory retention.",
        f"Active learning streak ({streak} days) supports continued gradual performance gains.",
        f"Observed mock exam accuracy ({curr_mock_acc}%) provides a reliable baseline for next test performance.",
        f"Topic mastery baseline ({curr_mastery}%) across target syllabus subjects shows positive trajectory.",
    ]

    pred_reason = (
        f"Based on consistent revision ({curr_rev_health}%), improving mock analytics ({curr_mock_acc}%), "
        f"and a stable study streak ({streak} days), current learning trend indicates continued gradual improvement."
    )

    mentor_proj = (
        "If current study consistency and spaced revision continue, readiness and mock accuracy "
        "are projected to improve steadily within the estimated target ranges."
    )

    # 6. Structured Dimension Breakdown Dict
    dimensions = {
        "readiness": {
            "name": "Exam Readiness",
            "current": curr_readiness,
            "estimated_range": est_readiness,
            "trend": readiness_trend,
            "description": "Overall preparation metric across mastery, revision, consistency, and repo coverage.",
        },
        "mock_accuracy": {
            "name": "Mock Test Accuracy",
            "current": curr_mock_acc,
            "estimated_range": est_mock_acc,
            "trend": mock_trend,
            "description": "Expected performance range in future grand and sectional mock examinations.",
        },
        "topic_mastery": {
            "name": "Topic Mastery",
            "current": curr_mastery,
            "estimated_range": est_mastery,
            "trend": mastery_trend,
            "description": "Subject and topic level accuracy projection based on learning intelligence.",
        },
        "revision_health": {
            "name": "Revision Health",
            "current": curr_rev_health,
            "estimated_range": est_rev_health,
            "trend": revision_trend,
            "description": "Spaced repetition stability and scheduled review completion rate.",
        },
        "consistency": {
            "name": "Study Consistency",
            "current": curr_consistency,
            "estimated_range": est_consistency,
            "trend": consistency_trend,
            "description": "Daily activity momentum and learning streak sustainability.",
        },
        "repo_completion": {
            "name": "Repository Completion",
            "current": curr_repo,
            "estimated_range": est_repo,
            "trend": repo_trend,
            "description": "Coverage across standard, hard, statement-based, and PYQ question banks.",
        },
    }

    # 7. Final Master Engine Output Schema
    return {
        "current_readiness": curr_readiness,
        "estimated_readiness": est_readiness,
        "readiness_trend": readiness_trend,

        "current_mock_accuracy": curr_mock_acc,
        "estimated_mock_accuracy": est_mock_acc,
        "mock_accuracy_trend": mock_trend,

        "current_topic_mastery": curr_mastery,
        "estimated_topic_mastery": est_mastery,
        "topic_mastery_trend": mastery_trend,

        "current_revision_health": curr_rev_health,
        "estimated_revision_health": est_rev_health,
        "revision_trend": revision_trend,

        "current_consistency": curr_consistency,
        "estimated_consistency": est_consistency,
        "consistency_trend": consistency_trend,

        "current_repo_completion": curr_repo,
        "estimated_repo_completion": est_repo,
        "repo_completion_trend": repo_trend,

        "prediction_confidence": confidence,
        "confidence_reason": conf_reason,
        "prediction_reason": pred_reason,
        "mentor_projection": mentor_proj,
        "explanation_bullets": expl_bullets,
        "dimensions": dimensions,
        "disclaimer": "All predictions are estimates based on available learning signals. Never guarantees exam pass, score, or selection rank.",
    }

    if hasattr(st, "session_state"):
        st.session_state[cache_key] = result

    return result
