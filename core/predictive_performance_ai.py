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


def _format_range(current_val: Optional[float], low_delta: float, high_delta: float) -> str:
    """Format projected metric range strictly as a string range (e.g., '75–79%')."""
    if current_val is None:
        return "Not assessed"
    low_bound = min(97, int(round(current_val + low_delta)))
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
    progress_rows = get_progress(user, context=ctx) or []
    weakness_data = get_weakness(user, context=ctx) or {}
    streak = get_streak(user, context=ctx) or 0
    xp_data = get_user_xp(user, context=ctx) or {}

    # 2. Extract Baseline Metrics with Strict Evidence Verification
    sample_size = len(progress_rows)
    observed_subjects = list(set(
        format_subject_name(r.get("subject", "")).strip()
        for r in progress_rows
        if r.get("subject")
    ))
    subjects_count = len(observed_subjects)

    # Mock attempts check
    mock_rows = [
        r for r in progress_rows
        if "grand_test" in str(r.get("topic", "")).lower() or "mock" in str(r.get("topic", "")).lower()
    ]
    mock_count = len(mock_rows)
    has_mock_data = mock_count > 0

    if has_mock_data:
        raw_mock_acc = mock_data.get("overall_accuracy")
        curr_mock_acc = int(round(raw_mock_acc)) if raw_mock_acc is not None else None
    else:
        curr_mock_acc = None

    raw_readiness = readiness_data.get("overall_score") or readiness_data.get("overall_readiness_score")
    curr_readiness = int(round(raw_readiness)) if raw_readiness is not None else None

    all_accs = [float(r.get("accuracy", 0)) for r in progress_rows if r.get("accuracy") is not None]
    curr_mastery = int(round(sum(all_accs) / len(all_accs))) if all_accs else None

    has_rev_data = bool(revision_analytics.get("total", 0) > 0 or revision_analytics.get("progress", {}).get("completed", 0) > 0)
    if has_rev_data:
        rev_prog = revision_analytics.get("progress", {})
        curr_rev_health = int(round(float(rev_prog.get("percentage", 75.0))))
    else:
        curr_rev_health = None

    if streak > 0:
        curr_consistency = min(100, int(round((streak * 8.0) + 40.0)))
    else:
        curr_consistency = None

    readiness_dims = readiness_data.get("readiness_dimensions", {})
    raw_repo = readiness_dims.get("repository_completion")
    curr_repo = int(round(float(raw_repo))) if raw_repo is not None else None

    # Evidence Eligibility Gate: requires >= 5 tests AND >= 2 subjects
    is_eligible = (sample_size >= 5 and subjects_count >= 2)

    if sample_size == 0:
        est_readiness = "Unavailable"
        readiness_trend = "No Data"
        est_mock_acc = "Unavailable"
        mock_trend = "No Data"
        est_mastery = "Unavailable"
        mastery_trend = "No Data"
        est_rev_health = "Unavailable"
        revision_trend = "No Data"
        est_consistency = "Unavailable"
        consistency_trend = "No Data"
        est_repo = "Unavailable"
        repo_trend = "No Data"
        confidence = 0
        conf_reason = "No learning history available yet. Complete daily practice tests to generate performance projections."
        expl_bullets = [
            "Complete initial practice sessions to begin tracking performance trajectory.",
            "Prediction confidence requires at least 5 completed practice sessions across multiple subjects.",
        ]
        pred_reason = "Performance trajectory projections unlock after completing initial practice tests."
        mentor_proj = "Begin with daily practice tests to establish your performance baseline."
    elif not is_eligible:
        # Early User / Low Data: Honest locked states, no fake predictions
        est_readiness = "More practice data required"
        readiness_trend = "Early Signal"
        est_mastery = "More practice data required"
        mastery_trend = "Early Signal"

        est_mock_acc = "Need Mock Data" if not has_mock_data else "More practice data required"
        mock_trend = "Not assessed" if not has_mock_data else "Early Signal"

        est_rev_health = "Not assessed" if curr_rev_health is None else "More practice data required"
        revision_trend = "Not assessed" if curr_rev_health is None else "Early Signal"

        est_consistency = "Not assessed" if curr_consistency is None else "More practice data required"
        consistency_trend = "Not assessed" if curr_consistency is None else "Early Signal"

        est_repo = "Not assessed" if curr_repo is None else "More practice data required"
        repo_trend = "Not assessed" if curr_repo is None else "Early Signal"

        confidence = min(35, 10 + (sample_size * 8))
        conf_reason = (
            f"More practice data required for reliable prediction. "
            f"Currently observed: {subjects_count} subject(s) across {sample_size} test(s). "
            f"5+ tests across at least 2 subjects required for mature trajectory projections."
        )
        expl_bullets = [
            "TNPSC-wide performance projections require broader subject evidence.",
            f"Observed preliminary signal: {sample_size} test(s) in {', '.join(observed_subjects) if observed_subjects else 'History'}.",
            "Complete full-length or sectional mock exams to establish mock accuracy projection baseline.",
        ]
        pred_reason = "Performance trajectory projections unlock after completing practice tests across multiple subjects."
        mentor_proj = "Focus on completing initial practice across multiple subjects before relying on predictive trajectories."
    else:
        # Sufficient Evidence: Compute projected ranges
        momentum_factor = 1.2 if streak >= 5 else (1.0 if streak >= 2 else 0.8)
        rev_factor = 1.1 if (curr_rev_health is not None and curr_rev_health >= 70) else 0.85

        r_low_delta = max(1.0, 2.5 * momentum_factor * rev_factor)
        r_high_delta = max(r_low_delta + 2.0, 5.5 * momentum_factor * rev_factor)
        est_readiness = _format_range(curr_readiness, r_low_delta, r_high_delta)
        readiness_trend = _classify_trend(curr_readiness or 50, r_low_delta)

        if has_mock_data and curr_mock_acc is not None:
            m_low_delta = max(1.0, 2.0 * momentum_factor)
            m_high_delta = max(m_low_delta + 2.0, 5.0 * momentum_factor)
            est_mock_acc = _format_range(curr_mock_acc, m_low_delta, m_high_delta)
            mock_trend = _classify_trend(curr_mock_acc, m_low_delta)
        else:
            est_mock_acc = "Need Mock Data"
            mock_trend = "Not assessed"

        t_low_delta = max(1.5, 3.0 * momentum_factor)
        t_high_delta = max(t_low_delta + 2.0, 6.0 * momentum_factor)
        est_mastery = _format_range(curr_mastery, t_low_delta, t_high_delta)
        mastery_trend = _classify_trend(curr_mastery or 50, t_low_delta)

        if curr_rev_health is not None:
            rev_low_delta = max(1.0, 3.0 * rev_factor)
            rev_high_delta = max(rev_low_delta + 2.0, 7.0 * rev_factor)
            est_rev_health = _format_range(curr_rev_health, rev_low_delta, rev_high_delta)
            revision_trend = _classify_trend(curr_rev_health, rev_low_delta)
        else:
            est_rev_health = "Not assessed"
            revision_trend = "Not assessed"

        if curr_consistency is not None:
            c_low_delta = max(1.0, 2.0 * momentum_factor)
            c_high_delta = max(c_low_delta + 1.5, 4.5 * momentum_factor)
            est_consistency = _format_range(curr_consistency, c_low_delta, c_high_delta)
            consistency_trend = _classify_trend(curr_consistency, c_low_delta)
        else:
            est_consistency = "Not assessed"
            consistency_trend = "Not assessed"

        if curr_repo is not None:
            repo_low_delta = max(1.0, 2.5 * momentum_factor)
            repo_high_delta = max(repo_low_delta + 2.0, 5.5 * momentum_factor)
            est_repo = _format_range(curr_repo, repo_low_delta, repo_high_delta)
            repo_trend = _classify_trend(curr_repo, repo_low_delta)
        else:
            est_repo = "Not assessed"
            repo_trend = "Not assessed"

        base_confidence = 70
        if sample_size >= 15:
            base_confidence += 12
        elif sample_size >= 5:
            base_confidence += 6

        if streak >= 5:
            base_confidence += 8
        elif streak >= 2:
            base_confidence += 4

        if curr_rev_health is not None and curr_rev_health >= 70:
            base_confidence += 6

        confidence = max(50, min(96, base_confidence))

        if confidence >= 88:
            conf_reason = "Rich learning history, consistent study streak, and sufficient performance data across tests."
        elif confidence >= 75:
            conf_reason = "Moderate learning history and steady revision activity. Projections are well-supported."
        else:
            conf_reason = "Sparse activity history or developing study streak. Complete more daily practice tests to refine accuracy."

        expl_bullets = [
            f"Observed topic mastery ({curr_mastery}%) provides a reliable baseline for next test performance." if curr_mastery is not None else "Developing topic mastery.",
            f"Active learning streak ({streak} days) supports continued gradual performance gains." if streak > 0 else "Establishing daily study habit.",
        ]
        if has_mock_data and curr_mock_acc is not None:
            expl_bullets.append(f"Observed mock exam accuracy ({curr_mock_acc}%) anchors full-length test trajectory.")
        else:
            expl_bullets.append("Attempt full-length mock exams to anchor exam-day test trajectory.")

        pred_reason = (
            f"Based on observed learning signals and a study streak ({streak} days), "
            f"current trajectory indicates steady progress across practiced areas."
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
    result = {
        "is_eligible": is_eligible,
        "sample_size": sample_size,
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
