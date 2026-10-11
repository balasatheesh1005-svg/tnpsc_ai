import datetime
import logging
from typing import Dict, List, Any, Optional
import streamlit as st

from core.mentor_memory import get_memory
from core.progress_ai import get_progress
from core.revision_engine import (
    get_intelligent_revision_plan,
    get_revision_analytics_v2,
)
from core.streak_ai import get_streak
from core.weakness_ai import get_weakness
from core.xp_ai import get_level_progress, get_user_xp

logger = logging.getLogger(__name__)


def format_subject_name(subject: str) -> str:
    """Helper to format subject name cleanly."""
    if not subject:
        return "General"
    return str(subject).replace("_", " ").replace("-", " ").title()


def format_topic_name(topic: str) -> str:
    """Helper to format topic name cleanly."""
    if not topic:
        return "General"
    return str(topic).replace("_", " ").replace("-", " ").title()



def _calculate_star_rating(value: float, min_val: float = 0, max_val: float = 100) -> int:
    """Helper to convert continuous metric to 1-5 star integer rating."""
    if value <= min_val:
        return 1
    pct = (value - min_val) / (max_val - min_val)
    if pct < 0.2:
        return 1
    elif pct < 0.4:
        return 2
    elif pct < 0.6:
        return 3
    elif pct < 0.8:
        return 4
    else:
        return 5


from core.performance import measure_time, record_cache_hit, record_cache_miss
from core.engine_cache import ENGINE_CACHE_KEY_PREFIX


@measure_time("Learning Intelligence Engine")
def get_learning_intelligence(
    user: str = None, context: Optional[Any] = None, force_refresh: bool = False
) -> Dict[str, Any]:
    """
    Learning Intelligence Engine V2 - Single Source of Truth.
    Synthesizes data across Progress, Weakness, Revision V2, XP, Streak, and Memory engines
    to determine WHY the student is weak and generate actionable recovery intelligence.
    """
    user_str = str(user or "Guest")
    cache_key = f"{ENGINE_CACHE_KEY_PREFIX}Learning Intelligence Engine_{user_str}"
    if hasattr(st, "session_state") and not force_refresh and cache_key in st.session_state:
        record_cache_hit("Learning Intelligence Engine")
        return st.session_state[cache_key]
    record_cache_miss("Learning Intelligence Engine")

    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    # 1. Fetch Engine Data using shared context
    progress_rows = get_progress(user, context=ctx) or []
    weakness_data = get_weakness(user, context=ctx) or {}
    revision_plan = get_intelligent_revision_plan(user, context=ctx)
    revision_analytics = get_revision_analytics_v2(user, context=ctx)
    streak = get_streak(user, context=ctx)
    xp_data = get_user_xp(user, context=ctx)
    memory = get_memory(user, context=ctx)

    # Check for meaningful test history
    has_history = len(progress_rows) > 0 or bool(weakness_data)

    if not has_history:
        result = {
            "subject": "Not enough data yet",
            "topic": "Not enough data yet",
            "repository": "N/A",
            "question_type": "N/A",
            "difficulty": "N/A",
            "learning_strength": "Not enough data yet",
            "learning_weakness": "Not enough data yet",
            "weak_topic": None,
            "strong_subject": None,
            "mastered_count": 0,
            "pending_count": 0,
            "root_cause": "No Test History",
            "root_explanation": "Complete practice tests to unlock diagnostic learning root causes.",
            "learning_bottleneck": "No test history yet",
            "recovery_plan": [],
            "estimated_recovery": "N/A",
            "current_mastery": 0.0,
            "mastery_probability": 0.0,
            "learning_dna": {k: 1 for k in ["knowledge", "memory", "application", "analysis", "speed", "accuracy", "consistency", "revision"]},
            "recommendation": "Begin with Indian Polity: Fundamental Rights to establish your initial learning baseline.",
            "mentor_insight": "Welcome! Complete your first practice test to unlock personalized learning intelligence.",
            "is_eligible": False,
        }
        if hasattr(st, "session_state"):
            st.session_state[cache_key] = result
        return result

    # 2. Analyze Subject & Topic Performance Breakdowns from REAL data
    all_accuracies = [float(r.get("accuracy", 0)) for r in progress_rows if r.get("accuracy") is not None]
    overall_acc = sum(all_accuracies) / len(all_accuracies) if all_accuracies else 0.0

    # Dynamic Mastered & Pending Topics calculation
    mastered_topics = set(
        str(r.get("topic", "")).strip()
        for r in progress_rows
        if float(r.get("accuracy", 0)) >= 80.0
    )
    all_topics = set(str(r.get("topic", "")).strip() for r in progress_rows if r.get("topic"))
    mastered_count = len(mastered_topics)
    pending_count = len(all_topics - mastered_topics)

    # Categorize accuracies by sub-repository pattern
    foundation_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "easy" in str(r.get("topic", "")).lower() or "notes" in str(r.get("topic", "")).lower()]
    medium_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "medium" in str(r.get("topic", "")).lower()]
    hard_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "hard" in str(r.get("topic", "")).lower()]
    assertion_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "assertion" in str(r.get("topic", "")).lower()]
    statement_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "statement" in str(r.get("topic", "")).lower()]
    chronology_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "chronology" in str(r.get("topic", "")).lower()]
    pyq_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "pyq" in str(r.get("topic", "")).lower()]

    avg_foundation = sum(foundation_accs) / len(foundation_accs) if foundation_accs else overall_acc
    avg_hard = sum(hard_accs) / len(hard_accs) if hard_accs else overall_acc
    avg_assertion = sum(assertion_accs) / len(assertion_accs) if assertion_accs else overall_acc
    avg_statement = sum(statement_accs) / len(statement_accs) if statement_accs else overall_acc
    avg_chronology = sum(chronology_accs) / len(chronology_accs) if chronology_accs else overall_acc

    # Strong Subject derived from real progress
    subj_accs = {}
    for r in progress_rows:
        s = str(r.get("subject", "")).strip().title()
        if s and r.get("accuracy") is not None:
            subj_accs.setdefault(s, []).append(float(r["accuracy"]))
    strong_subject = max(subj_accs.keys(), key=lambda k: sum(subj_accs[k]) / len(subj_accs[k])) if subj_accs else None

    # Weak Topic from real weakness data
    weak_topic = None
    if weakness_data:
        top_weak = sorted(weakness_data.items(), key=lambda x: x[1], reverse=True)[0][0]
        if "-" in top_weak:
            weak_topic = top_weak.split("-", 1)[1]
        else:
            weak_topic = top_weak

    # 3. Determine Root Cause
    if len(progress_rows) < 5 and not weakness_data:
        root_cause = "Early Learning Stage"
        root_explanation = "Complete more practice sets across topics to unlock detailed root-cause diagnosis."
    elif avg_assertion < 55 and assertion_accs:
        root_cause = "Concept Application"
        root_explanation = "Foundational knowledge is intact, but higher-order logical linking in Assertion & Reason requires practice."
    elif avg_chronology < 55 and chronology_accs:
        root_cause = "Chronological Recall"
        root_explanation = "Historical event sequences and timeline dates require spaced chronological ordering revision."
    elif avg_statement < 55 and statement_accs:
        root_cause = "Multi-Statement Analysis"
        root_explanation = "Evaluating multiple statement combinations requires process-of-elimination techniques."
    elif avg_hard < 55 and hard_accs:
        root_cause = "Application Skills"
        root_explanation = "Difficulty spikes in Hard repository questions reveal a need for deeper concept integration."
    elif overall_acc < 50:
        root_cause = "Foundational Knowledge Gap"
        root_explanation = "Key terms and definitions require initial study notes review before attempting mock tests."
    else:
        root_cause = "Timed Performance Stress"
        root_explanation = "Accuracy drops slightly under test conditions. Practice consistent timed sets to solidify recall."

    # 4. Determine Learning Bottleneck
    subj = strong_subject or revision_plan.get("level1_subject", "General")
    topic = weak_topic or revision_plan.get("level2_topic", "General")
    repo = revision_plan.get("level3_repository", "Foundation Repository")
    qtype = revision_plan.get("level4_question_type", "Concept Questions")
    bottleneck_acc = round(overall_acc, 1)

    learning_bottleneck = f"{subj} ↓ {topic}" if weak_topic else "No critical bottleneck detected"

    # 5. Determine Learning Strength & Weakness
    if strong_subject:
        learning_strength = f"Strong in {strong_subject}"
    elif avg_foundation >= 75:
        learning_strength = "Foundational Knowledge & Key Terms"
    elif streak >= 5:
        learning_strength = "Daily Consistency & Study Habit"
    else:
        learning_strength = "Consistent Practice Habit"

    if weak_topic:
        learning_weakness = f"Needs Practice in {weak_topic.replace('_', ' ').title()}"
    elif len(progress_rows) < 5:
        learning_weakness = "Not enough data yet"
    else:
        learning_weakness = "No critical weakness recorded"

    # 6. Generate Rule-Based 4-Step Recovery Plan
    if weak_topic:
        recovery_plan = [
            f"Step 1: Revise {weak_topic.replace('_', ' ').title()} notes & key concepts",
            f"Step 2: Practice targeted {weak_topic.replace('_', ' ').title()} practice set",
            f"Step 3: Attempt PYQ Repository questions",
            f"Step 4: Take full Grand Test to verify topic mastery",
        ]
    else:
        recovery_plan = []

    # 7. Calculate Estimated Recovery Sessions & Time
    if bottleneck_acc < 45:
        estimated_recovery = "3 Sessions (2 Revision Cycles)"
        rec_sessions_count = 3
    elif bottleneck_acc < 65:
        estimated_recovery = "2 Sessions (1 Revision Cycle)"
        rec_sessions_count = 2
    else:
        estimated_recovery = "1 Focused Session"
        rec_sessions_count = 1

    # 8. Calculate Topic Mastery Probability
    current_mastery = round(bottleneck_acc, 1)
    projected_mastery = min(95.0, round(current_mastery + (15.0 * rec_sessions_count), 1))

    # 9. Calculate 8-Dimension Learning DNA (1 to 5 Stars)
    revision_prog = revision_analytics.get("progress", {})
    rev_pct = revision_prog.get("percentage", 80)

    learning_dna = {
        "knowledge": _calculate_star_rating(avg_foundation, 40, 100),
        "memory": _calculate_star_rating(overall_acc, 30, 95),
        "application": _calculate_star_rating(avg_hard, 30, 95),
        "analysis": _calculate_star_rating(avg_assertion, 30, 95),
        "speed": _calculate_star_rating(min(100, len(progress_rows) * 10), 10, 100),
        "accuracy": _calculate_star_rating(overall_acc, 30, 95),
        "consistency": _calculate_star_rating(streak, 0, 7),
        "revision": _calculate_star_rating(rev_pct, 20, 100),
    }

    # 10. Generate Recommendation & Mentor Insight
    if weak_topic:
        recommendation = f"Focus practice on {weak_topic.replace('_', ' ').title()} to improve mastery."
        mentor_insight = f"Targeted practice in {weak_topic.replace('_', ' ').title()} will significantly boost your exam readiness."
    else:
        recommendation = "Continue daily practice to build your subject mastery profile."
        mentor_insight = "Keep up consistent practice across topics to refine your readiness metrics."

    # 11. Final Engine Output JSON Schema
    result = {
        "subject": subj,
        "topic": topic,
        "repository": repo,
        "question_type": qtype,
        "difficulty": revision_plan.get("level5_difficulty", "Medium"),
        "learning_strength": learning_strength,
        "learning_weakness": learning_weakness,
        "weak_topic": weak_topic,
        "strong_subject": strong_subject,
        "mastered_count": mastered_count,
        "pending_count": pending_count,
        "root_cause": root_cause,
        "root_explanation": root_explanation,
        "learning_bottleneck": learning_bottleneck,
        "recovery_plan": recovery_plan,
        "estimated_recovery": estimated_recovery,
        "current_mastery": current_mastery,
        "mastery_probability": projected_mastery,
        "learning_dna": learning_dna,
        "recommendation": recommendation,
        "mentor_insight": mentor_insight,
        "is_eligible": len(progress_rows) >= 5,
    }

    if hasattr(st, "session_state"):
        st.session_state[cache_key] = result

    return result
